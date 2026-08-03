# ARCHITECTURAL_BRIEF: @azure_msal-node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@azure_msal-node` |
| **Timestamp** | `2026-08-03T21:07:44.655506+00:00` |
| **Scan Duration** | `0.34s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 75 malicious artifacts.

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
| Total Artifacts | 78 |
| Analyzed Artifacts (Scanned) | 77 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 6257 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 75 | 6257 | 97.4% |
| MARKDOWN | 1 | 0 | 1.3% |
| PLAINTEXT | 1 | 0 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.641`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 32 | 41.6% |
| file_cluster_8 | 24 | 31.2% |
| file_cluster_4 | 14 | 18.2% |
| file_cluster_16 | 3 | 3.9% |
| file_cluster_7 | 1 | 1.3% |
| file_cluster_0 | 1 | 1.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 18.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 93.4 | 33.2 | 17.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Testing Exposure | 0.3 | 80.0 | 26.9 | 2.5 | 80.0 |
| API Exposure | 0.7 | 15.8 | 4.9 | 4.0 | 4.0 |
| Concurrency Exposure | 0.0 | 100.0 | 37.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 36.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.4 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 86.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 3.2 | 100.0 | 46.8 | 31.5 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 49.8 | 11.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 41.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/client/ManagedIdentitySources/AzureArc.ts` (Hits: 13)
- `package/src/network/LoopbackClient.ts` (Hits: 6)
- `package/src/error/ManagedIdentityError.ts` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`package/README.md`) — 0 inbound connections
2. **package.json** (`package/package.json`) — 0 inbound connections
3. **CacheHelpers.ts** (`package/src/cache/CacheHelpers.ts`) — 0 inbound connections
4. **ITokenCache.ts** (`package/src/cache/ITokenCache.ts`) — 0 inbound connections
5. **NodeStorage.ts** (`package/src/cache/NodeStorage.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`package/src/index.ts`) — 30 outbound dependencies
2. **PublicClientApplication.ts** (`package/src/client/PublicClientApplication.ts`) — 18 outbound dependencies
3. **ClientApplication.ts** (`package/src/client/ClientApplication.ts`) — 17 outbound dependencies
4. **ManagedIdentityClient.ts** (`package/src/client/ManagedIdentityClient.ts`) — 14 outbound dependencies
5. **ConfidentialClientApplication.ts** (`package/src/client/ConfidentialClientApplication.ts`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `acquireTokenWithManagedIdentity` (@ `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts`) -> Impact: **224.9** | LOC: 116
- `acquireTokenSilent` (@ `package/src/client/ClientApplication.ts`) -> Impact: **175.0** | LOC: 70
- `getServerTokenResponseAsync` (@ `package/src/client/ManagedIdentitySources/AzureArc.ts`) -> Impact: **170.2** | LOC: 117
- `getCachedAuthenticationResult` (@ `package/src/client/ClientCredentialClient.ts`) -> Impact: **155.8** | LOC: 100
- `getCachedAuthenticationResult` (@ `package/src/client/OnBehalfOfClient.ts`) -> Impact: **149.9** | LOC: 87
  * *Intent:* // Any failure falls back to interactive request, once we implement distributed cache, we plan to handle `createRefreshRequiredError` to refresh using...
- `acquireTokenInteractive` (@ `package/src/client/PublicClientApplication.ts`) -> Impact: **134.4** | LOC: 43
- `acquireTokenSilent` (@ `package/src/client/PublicClientApplication.ts`) -> Impact: **134.1** | LOC: 37
- `mergeUpdates` (@ `package/src/cache/TokenCache.ts`) -> Impact: **105.6** | LOC: 33
- `sendRequest` (@ `package/src/network/HttpClient.ts`) -> Impact: **97.4** | LOC: 78
  * *Intent:* /** * Sends an HTTP GET request to the specified URL. * * This method handles GET requests with optional timeout support. The timeout * is implemented...
- `acquireTokenByRefreshToken` (@ `package/src/client/ClientApplication.ts`) -> Impact: **90.7** | LOC: 51

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `acquireTokenSilent` (@ `package/src/client/ClientApplication.ts`) -> **O(2^N) [Recursive]**
- `acquireTokenWithManagedIdentity` (@ `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts`) -> **O(2^N) [Recursive]**
- `mergeUpdates` (@ `package/src/cache/TokenCache.ts`) -> **O(2^N) [Recursive]**
- `acquireTokenByRefreshToken` (@ `package/src/client/ClientApplication.ts`) -> **O(2^N) [Recursive]**
- `acquireCachedTokenSilent` (@ `package/src/client/ClientApplication.ts`) -> **O(2^N) [Recursive]**
- `acquireTokenInteractive` (@ `package/src/client/PublicClientApplication.ts`) -> **O(2^N) [Recursive]**
- `acquireTokenSilent` (@ `package/src/client/PublicClientApplication.ts`) -> **O(2^N) [Recursive]**
- `signOut` (@ `package/src/client/PublicClientApplication.ts`) -> **O(2^N) [Recursive]**
- `getAllAccounts` (@ `package/src/cache/TokenCache.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `removeAccount` (@ `package/src/cache/TokenCache.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `executeTokenRequest` (@ `package/src/client/ClientCredentialClient.ts`) -> DB Complexity: **20**
- `getServerTokenResponseAsync` (@ `package/src/client/ManagedIdentitySources/AzureArc.ts`) -> DB Complexity: **20**
- `getCachedAuthenticationResult` (@ `package/src/client/OnBehalfOfClient.ts`) -> DB Complexity: **18**
  * *Intent:* // Any failure falls back to interactive request, once we implement distributed cache, we plan to handle `createRefreshRequiredError` to refresh using...
- `createJwt` (@ `package/src/client/ClientAssertion.ts`) -> DB Complexity: **15**
- `constructor` (@ `package/src/client/BaseClient.ts`) -> DB Complexity: **14**
- `createTokenRequestBody` (@ `package/src/client/UsernamePasswordClient.ts`) -> DB Complexity: **14**
- `serialize` (@ `package/src/cache/TokenCache.ts`) -> DB Complexity: **13**
- `constructor` (@ `package/src/client/ClientApplication.ts`) -> DB Complexity: **13**
  * *Intent:* /**
- `createTokenRequestBody` (@ `package/src/client/ClientCredentialClient.ts`) -> DB Complexity: **13**
- `acquireToken` (@ `package/src/client/ClientCredentialClient.ts`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `package/src/client` | 13 | 401.54 | 41.22% | 3.01% |
| `package/src/cache` | 4 | 128.52 | 28.52% | 0.0% |
| `package/src/client/ManagedIdentitySources` | 7 | 118.4 | 7.59% | 41.09% |
| `package/src/network` | 4 | 53.62 | 50.37% | 20.02% |
| `package/src/request` | 16 | 37.87 | 4.25% | 0.0% |
| `package/src/retry` | 5 | 26.54 | 22.38% | 17.37% |
| `package/src/config` | 3 | 22.89 | 36.64% | 65.45% |
| `package/src/cache/serializer` | 3 | 21.57 | 4.82% | 15.96% |
| `package/src/cache/distributed` | 3 | 15.25 | 20.0% | 32.47% |
| `package/src/utils` | 4 | 14.37 | 5.93% | 70.89% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `package/src/config/ManagedIdentityId.ts` -> **99.9999%** Exposure
- `package/src/crypto/CryptoProvider.ts` -> **99.9999%** Exposure
- `package/src/utils/TimeUtils.ts` -> **99.9992%** Exposure
- `package/src/error/NodeAuthError.ts` -> **99.95%** Exposure
- `package/src/utils/EncodingUtils.ts` -> **99.4472%** Exposure
### Highest State Flux (Mutation/Volatility)
- `package/src/client/ClientAssertion.ts` -> **100.0%** Exposure
- `package/src/client/PublicClientApplication.ts` -> **100.0%** Exposure
- `package/src/config/ManagedIdentityId.ts` -> **100.0%** Exposure
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **100.0%** Exposure
- `package/src/network/HttpClientWithRetries.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/error/NodeAuthError.ts` -> **10** Orphaned Functions | **0** Duplicates
- `package/src/crypto/CryptoProvider.ts` -> **9** Orphaned Functions | **0** Duplicates
- `package/src/client/ManagedIdentitySources/AzureArc.ts` -> **4** Orphaned Functions | **0** Duplicates
- `package/src/config/ManagedIdentityId.ts` -> **0** Orphaned Functions | **4** Duplicates
- `package/src/cache/distributed/DistributedCachePlugin.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`package/src/cache/TokenCache.ts`** -> AI Confidence: **99.31%**
2. **`package/src/client/ManagedIdentitySources/AzureArc.ts`** -> AI Confidence: **99.31%**
3. **`package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts`** -> AI Confidence: **99.31%**
4. **`package/src/client/ClientApplication.ts`** -> AI Confidence: **99.24%**
5. **`package/src/client/ConfidentialClientApplication.ts`** -> AI Confidence: **99.24%**
6. **`package/src/client/ManagedIdentityClient.ts`** -> AI Confidence: **99.24%**
7. **`package/src/client/PublicClientApplication.ts`** -> AI Confidence: **99.24%**
8. **`package/src/client/ManagedIdentitySources/AppService.ts`** -> AI Confidence: **99.18%**
9. **`package/src/response/ManagedIdentityTokenResponse.ts`** -> AI Confidence: **99.17%**
10. **`package/src/client/ManagedIdentitySources/Imds.ts`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `package/src/cache/NodeStorage.ts` -> **100.0%** Exposure
- `package/src/cache/TokenCache.ts` -> **100.0%** Exposure
- `package/src/client/BaseClient.ts` -> **100.0%** Exposure
- `package/src/client/ClientApplication.ts` -> **100.0%** Exposure
- `package/src/client/ClientAssertion.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `package/src/client/ClientAssertion.ts` -> **99.9718%** Exposure
### Algorithmic DoS Exposure
- `package/src/cache/NodeStorage.ts` -> **100.0%** Exposure
- `package/src/cache/TokenCache.ts` -> **100.0%** Exposure
- `package/src/cache/distributed/DistributedCachePlugin.ts` -> **100.0%** Exposure
- `package/src/cache/serializer/Deserializer.ts` -> **100.0%** Exposure
- `package/src/cache/serializer/Serializer.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/retry/ImdsRetryPolicy.ts` (TYPESCRIPT) -> Cumulative Risk: **900.68**
- **Archetype:** `file_cluster_4` (Distance: 11.69 IQR)
- **Magnitude:** 13.1 | **LOC:** 123 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `pauseForRetry` (Impact: 65.5), `MIN_EXPONENTIAL_BACKOFF_MS` (Impact: 6.2), `MAX_EXPONENTIAL_BACKOFF_MS` (Impact: 6.2)

### 2. `package/src/network/LoopbackClient.ts` (TYPESCRIPT) -> Cumulative Risk: **884.87**
- **Archetype:** `file_cluster_4` (Distance: 11.909 IQR)
- **Magnitude:** 16.59 | **LOC:** 117 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `listenForAuthCode` (Impact: 81.4), `getRedirectUri` (Impact: 20.5), `closeServer` (Impact: 11.3)

### 3. `package/src/config/ManagedIdentityId.ts` (TYPESCRIPT) -> Cumulative Risk: **882.48**
- **Archetype:** `file_cluster_13` (Distance: 11.895 IQR)
- **Magnitude:** 13.67 | **LOC:** 74 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 90.3), `id` (Impact: 3.5), `idType` (Impact: 3.5)

### 4. `package/src/client/PublicClientApplication.ts` (TYPESCRIPT) -> Cumulative Risk: **875.76**
- **Archetype:** `file_cluster_4` (Distance: 12.945 IQR)
- **Magnitude:** 75.13 | **LOC:** 406 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `acquireTokenInteractive` (Impact: 134.4), `acquireTokenSilent` (Impact: 134.1), `acquireTokenByDeviceCode` (Impact: 68.3)

### 5. `package/src/client/ClientCredentialClient.ts` (TYPESCRIPT) -> Cumulative Risk: **875.53**
- **Archetype:** `file_cluster_4` (Distance: 11.585 IQR)
- **Magnitude:** 51.55 | **LOC:** 432 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getCachedAuthenticationResult` (Impact: 155.8), `createTokenRequestBody` (Impact: 75.5), `acquireToken` (Impact: 49.8)

### 6. `package/src/cache/TokenCache.ts` (TYPESCRIPT) -> Cumulative Risk: **871.55**
- **Archetype:** `file_cluster_4` (Distance: 13.234 IQR)
- **Magnitude:** 77.3 | **LOC:** 399 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mergeUpdates` (Impact: 105.6), `getAllAccounts` (Impact: 85.7), `removeAccount` (Impact: 79.0)

### 7. `package/src/network/HttpClientWithRetries.ts` (TYPESCRIPT) -> Cumulative Risk: **869.07**
- **Archetype:** `file_cluster_4` (Distance: 11.642 IQR)
- **Magnitude:** 12.78 | **LOC:** 90 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sendNetworkRequestAsync` (Impact: 11.6), `sendNetworkRequestAsyncHelper` (Impact: 8.6), `constructor` (Impact: 3.5)

### 8. `package/src/client/ClientAssertion.ts` (TYPESCRIPT) -> Cumulative Risk: **867.32**
- **Archetype:** `file_cluster_13` (Distance: 12.587 IQR)
- **Magnitude:** 19.81 | **LOC:** 203 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getJwt` (Impact: 41.3), `createJwt` (Impact: 22.2), `fromCertificate` (Impact: 15.8)

### 9. `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT) -> Cumulative Risk: **854.49**
- **Archetype:** `file_cluster_4` (Distance: 11.899 IQR)
- **Magnitude:** 51.83 | **LOC:** 416 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getCachedAuthenticationResult` (Impact: 149.9), `createTokenRequestBody` (Impact: 68.0), `acquireToken` (Impact: 41.1)

### 10. `package/src/client/DeviceCodeClient.ts` (TYPESCRIPT) -> Cumulative Risk: **846.88**
- **Archetype:** `file_cluster_4` (Distance: 11.588 IQR)
- **Magnitude:** 39.03 | **LOC:** 415 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `continuePolling` (Impact: 86.1), `acquireTokenWithDeviceCode` (Impact: 58.9), `createTokenRequestBody` (Impact: 28.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/client/ClientApplication.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.926 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.744 IQR)
- **Top Global Matches:** file_cluster_4: 11.926, file_cluster_13: 12.167, file_cluster_8: 12.393
- **Magnitude:** 77.69 | **LOC:** 684 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (49.3487%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acquireTokenSilent` (Impact: 175.0 | O(2^N) | DB: 7)
  * `acquireTokenByRefreshToken` (Impact: 90.7 | O(2^N) | DB: 6)
  * `acquireTokenByCode` (Impact: 89.7 | O(2^N) | DB: 8)
    * *Intent:* /** * Creates the URL of the authorization request, letting the user input credentials and consent t...
  * `acquireCachedTokenSilent` (Impact: 73.8 | O(2^N) | DB: 1)
  * `getAuthCodeUrl` (Impact: 41.2 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 44`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 100`, `dead_code: 1`
* *Architecture:* `api: 3`, `concurrency: 139`, `import: 17`
* *Defense:* `safety: 12`, `doc: 19`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, AuthorizationUrlRequest.js, node, Constants.js, CryptoProvider.js, AuthorizationCodeRequest.js, RefreshTokenRequest.js, SilentFlowRequest.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/TokenCache.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.234 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.056 IQR)
- **Top Global Matches:** file_cluster_4: 13.234, file_cluster_13: 13.538, file_cluster_17: 13.669
- **Magnitude:** 77.3 | **LOC:** 399 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (49.7057%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeUpdates` (Impact: 105.6 | O(2^N) | DB: 1)
  * `getAllAccounts` (Impact: 85.7 | O(2^N) | DB: 7)
    * *Intent:* /**
  * `removeAccount` (Impact: 79.0 | O(2^N) | DB: 7)
  * `getAccountByHomeId` (Impact: 44.8 | O(N^5) | DB: 1)
    * *Intent:* /** * API that retrieves all accounts currently in cache to the user */
  * `getAccountByLocalId` (Impact: 44.8 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 38`, `args: 20`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 159`, `dead_code: 2`
* *Architecture:* `api: 9`, `concurrency: 108`, `import: 8`
* *Defense:* `safety: 7`, `doc: 30`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, CryptoProvider.js, ITokenCache.js, Serializer.js, NodeStorage.js, Deserializer.js, SerializerTypes.js, GuidGenerator.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/PublicClientApplication.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.945 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.858 IQR)
- **Top Global Matches:** file_cluster_4: 12.945, file_cluster_13: 13.115, file_cluster_8: 13.465
- **Magnitude:** 75.13 | **LOC:** 406 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.9228%), Tech Debt (15.2827%)
**Top Internal Functions/Classes:**
  * `acquireTokenInteractive` (Impact: 134.4 | O(2^N) | DB: 8)
  * `acquireTokenSilent` (Impact: 134.1 | O(2^N) | DB: 9)
  * `acquireTokenByDeviceCode` (Impact: 68.3 | O(2^N) | DB: 7)
    * *Intent:* * - clientID: the application ID of your application. You can obtain one by registering your applica...
  * `waitForRedirectUri` (Impact: 57.5 | O(N^6) | DB: 1)
  * `signOut` (Impact: 48.9 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 43`, `args: 23`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 124`, `import: 18`
* *Defense:* `safety: 8`, `doc: 17`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommonDeviceCodeRequest.js, DeviceCodeRequest.js, AuthorizationUrlRequest.js, node, Constants.js, AuthorizationCodeRequest.js, SilentFlowRequest.js, RefreshTokenRequest.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.899 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.196 IQR)
- **Top Global Matches:** file_cluster_4: 11.899, file_cluster_8: 11.99, file_cluster_13: 12.167
- **Magnitude:** 51.83 | **LOC:** 416 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (51.0342%), Tech Debt (8.741%)
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` (Impact: 149.9 | O(2^N) | DB: 18)
    * *Intent:* // Any failure falls back to interactive request, once we implement distributed cache, we plan to ha...
  * `createTokenRequestBody` (Impact: 68.0 | O(N^5) | DB: 13)
  * `acquireToken` (Impact: 41.1 | O(N^4) | DB: 10)
  * `readAccessTokenFromCacheForOBO` (Impact: 32.3 | O(N^4) | DB: 3)
  * `readIdTokenFromCacheForOBO` (Impact: 9.8 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 127`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 70`, `import: 5`
* *Defense:* `safety: 5`, `doc: 15`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BaseClient.js, CommonOnBehalfOfRequest.js, node, Constants.js, EncodingUtils.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ClientCredentialClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.585 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.859 IQR)
- **Top Global Matches:** file_cluster_4: 11.585, file_cluster_8: 11.828, file_cluster_13: 11.912
- **Magnitude:** 51.55 | **LOC:** 432 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (62.5709%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` (Impact: 155.8 | O(N^5) | DB: 4)
  * `createTokenRequestBody` (Impact: 75.5 | O(N^5) | DB: 13)
  * `acquireToken` (Impact: 49.8 | O(N^5) | DB: 13)
  * `readAccessTokenFromCache` (Impact: 26.0 | O(N^4))
  * `executeTokenRequest` (Impact: 24.9 | O(N^4) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 28`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `dead_code: 2`
* *Architecture:* `api: 5`, `concurrency: 63`, `import: 5`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BaseClient.js, node, Constants.js, Configuration.js, CommonClientCredentialRequest.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.694 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.299 IQR)
- **Top Global Matches:** file_cluster_13: 11.694, file_cluster_4: 11.987, file_cluster_8: 12.0
- **Magnitude:** 49.16 | **LOC:** 416 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (22.4531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acquireTokenWithManagedIdentity` (Impact: 224.9 | O(2^N) | DB: 12)
  * `getManagedIdentityUserAssignedIdQueryPar` (Impact: 79.0 | O(N^6) | DB: 3)
  * `getServerTokenResponse` (Impact: 75.9 | O(N^5) | DB: 1)
  * `getValidatedEnvVariableUrlString` (Impact: 21.2 | O(N^5))
  * `constructor` (Impact: 4.3 | O(N^2) | DB: 5)
    * *Intent:* /** * Base class for all Managed Identity sources. Provides common functionality for * authenticatin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`, `dead_code: 1`
* *Architecture:* `api: 11`, `concurrency: 22`, `import: 11`
* *Defense:* `safety: 9`, `doc: 46`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, ManagedIdentityRequest.js, TimeUtils.js, CryptoProvider.js, ManagedIdentityRequestParameters.js, NodeStorage.js, ManagedIdentityId.js, ManagedIdentityTokenResponse.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/NodeStorage.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.928 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.353 IQR)
- **Top Global Matches:** file_cluster_4: 12.928, file_cluster_8: 13.085, file_cluster_13: 13.117
- **Magnitude:** 43.79 | **LOC:** 566 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (48.7872%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cacheToInMemoryCache` (Impact: 66.5 | O(N^4))
  * `updateCredentialCacheKey` (Impact: 22.1 | O(N^5) | DB: 6)
  * `getServerTelemetry` (Impact: 17.6 | O(N^4) | DB: 1)
  * `removeItem` (Impact: 11.3 | O(N^3) | DB: 5)
  * `getAuthorityMetadata` (Impact: 11.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 40`, `args: 37`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`
* *Architecture:* `api: 24`, `concurrency: 48`, `import: 5`
* *Defense:* `safety: 14`, `doc: 60`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, Serializer.js, CacheHelpers.js, Deserializer.js, SerializerTypes.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/DeviceCodeClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.588 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.278 IQR)
- **Top Global Matches:** file_cluster_4: 11.588, file_cluster_8: 11.637, file_cluster_13: 11.751
- **Magnitude:** 39.03 | **LOC:** 415 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (41.0592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `continuePolling` (Impact: 86.1 | O(N^5) | DB: 4)
  * `acquireTokenWithDeviceCode` (Impact: 58.9 | O(N^6) | DB: 11)
  * `createTokenRequestBody` (Impact: 28.6 | O(N^4) | DB: 9)
  * `createQueryString` (Impact: 26.5 | O(N^4) | DB: 4)
  * `createExtraQueryParameters` (Impact: 12.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 21`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 83`, `dead_code: 1`
* *Architecture:* `api: 5`, `concurrency: 58`, `import: 5`
* *Defense:* `safety: 1`, `doc: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommonDeviceCodeRequest.js, BaseClient.js, node, Constants.js, ClientAuthErrorCodes.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/AzureArc.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.314 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.406 IQR)
- **Top Global Matches:** file_cluster_13: 11.314, file_cluster_0: 11.436, file_cluster_4: 11.605
- **Magnitude:** 32.97 | **LOC:** 416 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (9.848%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `getServerTokenResponseAsync` (Impact: 170.2 | O(N^6) | DB: 20)
  * `tryCreate` (Impact: 67.1 | O(N^5))
  * `getEnvironmentVariables` (Impact: 31.4 | O(N^5) | DB: 2)
    * *Intent:* /** * Creates a new instance of the AzureArc managed identity source. * * @param logger - Logger ins...
  * `constructor` (Impact: 6.2 | O(N^3) | DB: 1)
    * *Intent:* /** * Azure Arc managed identity source implementation for acquiring tokens from Azure Arc-enabled s...
  * `createRequest` (Impact: 5.9 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `dead_code: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 13`, `api: 9`, `concurrency: 14`, `import: 11`
* *Defense:* `safety: 17`, `doc: 30`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, path, CryptoProvider.js, ManagedIdentityRequestParameters.js, NodeStorage.js, ManagedIdentityError.js, ManagedIdentityTokenResponse.js, Constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ConfidentialClientApplication.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.616 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.872 IQR)
- **Top Global Matches:** file_cluster_4: 11.616, file_cluster_13: 11.796, file_cluster_8: 12.165
- **Magnitude:** 23.13 | **LOC:** 304 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (68.5418%), Tech Debt (15.0489%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 70.7 | O(N^5) | DB: 11)
    * *Intent:* /** * This class is to be used to acquire tokens for confidential client applications (webApp, webAP...
  * `acquireTokenOnBehalfOf` (Impact: 68.0 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `concurrency: 54`, `import: 13`
* *Defense:* `safety: 7`, `doc: 4`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientCredentialClient.js, OnBehalfOfRequest.js, CommonOnBehalfOfRequest.js, node, Constants.js, ClientCredentialRequest.js, Configuration.js, ClientApplication.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/UsernamePasswordClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.202 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.082 IQR)
- **Top Global Matches:** file_cluster_4: 11.202, file_cluster_8: 11.215, file_cluster_13: 11.376
- **Magnitude:** 20.01 | **LOC:** 222 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (49.3386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createTokenRequestBody` (Impact: 84.0 | O(N^5) | DB: 14)
  * `acquireToken` (Impact: 11.7 | O(2^N) | DB: 11)
    * *Intent:* /** * Oauth2.0 Password grant client * Note: We are only supporting public clients for password gran...
  * `executeTokenRequest` (Impact: 5.2 | O(N^3) | DB: 5)
  * `constructor` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`
* *Architecture:* `api: 2`, `concurrency: 39`, `import: 4`
* *Defense:* `doc: 9`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BaseClient.js, CommonUsernamePasswordRequest.js, node, Constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ClientAssertion.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.587 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.039 IQR)
- **Top Global Matches:** file_cluster_13: 12.587, file_cluster_8: 13.006, file_cluster_0: 13.023
- **Magnitude:** 19.81 | **LOC:** 203 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (34.565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getJwt` (Impact: 41.3 | O(N^4) | DB: 10)
    * *Intent:* /** * Initialize the ClientAssertion class from the certificate passed by the user * @param thumbpri...
  * `createJwt` (Impact: 22.2 | O(N^4) | DB: 15)
  * `fromCertificate` (Impact: 15.8 | O(N^4) | DB: 1)
    * *Intent:* /** * Initialize the ClientAssertion class from the clientAssertion passed by the user
  * `fromCertificateWithSha256Thumbprint` (Impact: 15.8 | O(N^4) | DB: 1)
  * `parseCertificate` (Impact: 14.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `doc: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jsonwebtoken, node, Constants.js, CryptoProvider.js, EncodingUtils.js, ClientAuthErrorCodes.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/HttpClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.121 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.313 IQR)
- **Top Global Matches:** file_cluster_4: 12.121, file_cluster_16: 12.384, file_cluster_13: 12.396
- **Magnitude:** 17.58 | **LOC:** 222 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (47.9074%), Tech Debt (34.732%)
**Top Internal Functions/Classes:**
  * `sendRequest` (Impact: 97.4 | O(N^5) | DB: 5)
    * *Intent:* /** * Sends an HTTP GET request to the specified URL. * * This method handles GET requests with opti...
  * `getFetchHeaders` (Impact: 12.7 | O(N^2))
  * `sendGetRequestAsync` (Impact: 4.8 | O(N^2) | DB: 1)
  * `getHeaderDict` (Impact: 3.5 | O(N^2))
  * `sendPostRequestAsync` (Impact: 3.3 | O(N^2) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 16`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 39`, `import: 2`
* *Defense:* `safety: 7`, `doc: 28`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, Constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/LoopbackClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.909 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.533 IQR)
- **Top Global Matches:** file_cluster_4: 11.909, file_cluster_13: 11.938, file_cluster_8: 12.342
- **Magnitude:** 16.59 | **LOC:** 117 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (48.5679%), Tech Debt (21.2567%)
**Top Internal Functions/Classes:**
  * `listenForAuthCode` (Impact: 81.4 | O(N^6) | DB: 13)
  * `getRedirectUri` (Impact: 20.5 | O(N^3) | DB: 4)
  * `closeServer` (Impact: 11.3 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 14`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 1`, `doc: 7`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ILoopbackClient.js, node, Constants.js, http, NodeAuthError.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentityClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.966 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.752 IQR)
- **Top Global Matches:** file_cluster_13: 9.966, file_cluster_8: 10.028, file_cluster_7: 10.539
- **Magnitude:** 15.54 | **LOC:** 190 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (20.2185%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `selectManagedIdentitySource` (Impact: 49.4 | O(N^4))
  * `getManagedIdentitySource` (Impact: 32.5 | O(N^5) | DB: 5)
  * `sendManagedIdentityTokenRequest` (Impact: 21.4 | O(N^5) | DB: 6)
  * `allEnvironmentVariablesAreDefined` (Impact: 7.5 | O(N^4))
  * `constructor` (Impact: 4.3 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 14`
* *Defense:* `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MachineLearning.js, NodeStorage.js, node, Constants.js, CryptoProvider.js, BaseManagedIdentitySource.js, AppService.js, CloudShell.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/config/ManagedIdentityId.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.895 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.7 IQR)
- **Top Global Matches:** file_cluster_13: 11.895, file_cluster_8: 11.963, file_cluster_0: 12.409
- **Magnitude:** 13.67 | **LOC:** 74 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (65.4614%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 90.3 | O(N^5) | DB: 8)
  * `id` (Impact: 3.5 | O(N^2) | DB: 1)
  * `idType` (Impact: 3.5 | O(N^2) | DB: 1)
  * `id` (Impact: 3.1 | O(N^2) | DB: 1)
  * `idType` (Impact: 3.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ManagedIdentityError.js, Constants.js, Configuration.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/retry/ImdsRetryPolicy.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.69 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.846 IQR)
- **Top Global Matches:** file_cluster_4: 11.69, file_cluster_13: 11.923, file_cluster_8: 12.177
- **Magnitude:** 13.1 | **LOC:** 123 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (48.4553%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `pauseForRetry` (Impact: 65.5 | O(N^6) | DB: 6)
  * `MIN_EXPONENTIAL_BACKOFF_MS` (Impact: 6.2 | O(2^N))
  * `MAX_EXPONENTIAL_BACKOFF_MS` (Impact: 6.2 | O(2^N))
    * *Intent:* /*
  * `EXPONENTIAL_DELTA_BACKOFF_MS` (Impact: 6.2 | O(2^N))
    * *Intent:* /* * these are defined here as static variables despite being defined as constants outside of the * ...
  * `HTTP_STATUS_GONE_RETRY_AFTER_MS` (Impact: 6.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 15`, `import: 3`
* *Defense:* `doc: 6`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IHttpRetryPolicy.js, node, ExponentialRetryStrategy.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/serializer/Deserializer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.761 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.668 IQR)
- **Top Global Matches:** file_cluster_8: 9.761, file_cluster_7: 10.206, file_cluster_16: 10.311
- **Magnitude:** 12.8 | **LOC:** 222 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (5.8101%), Tech Debt (20.6864%)
**Top Internal Functions/Classes:**
  * `deserializeAllCache` (Impact: 30.9 | O(N^4) | DB: 5)
  * `deserializeAccounts` (Impact: 19.8 | O(N^6) | DB: 2)
    * *Intent:* /**
  * `deserializeAccessTokens` (Impact: 13.8 | O(N^6))
  * `deserializeRefreshTokens` (Impact: 13.4 | O(N^6))
  * `deserializeIdTokens` (Impact: 13.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 15`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SerializerTypes.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/HttpClientWithRetries.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.642 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.929 IQR)
- **Top Global Matches:** file_cluster_4: 11.642, file_cluster_13: 12.135, file_cluster_8: 12.245
- **Magnitude:** 12.78 | **LOC:** 90 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (99.9926%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `sendNetworkRequestAsync` (Impact: 11.6 | O(N^4) | DB: 8)
  * `sendNetworkRequestAsyncHelper` (Impact: 8.6 | O(N^3) | DB: 2)
  * `constructor` (Impact: 3.5 | O(N^2) | DB: 3)
  * `sendGetRequestAsync` (Impact: 3.3 | O(N^2) | DB: 1)
  * `sendPostRequestAsync` (Impact: 3.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 1`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 56`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IHttpRetryPolicy.js, node, Constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/distributed/DistributedCachePlugin.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.168 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.565 IQR)
- **Top Global Matches:** file_cluster_4: 12.168, file_cluster_13: 12.689, file_cluster_8: 12.981
- **Magnitude:** 10.72 | **LOC:** 73 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9992%), Tech Debt (97.3978%)
**Top Internal Functions/Classes:**
  * `afterCacheAccess` (Impact: 33.1 | O(N^5) | DB: 5)
    * *Intent:* /** * Deserializes the cache before accessing it * @param cacheContext - TokenCacheContext */
  * `beforeCacheAccess` (Impact: 4.3 | O(N^2) | DB: 2)
  * `constructor` (Impact: 2.8 | O(N^2) | DB: 2)
    * *Intent:* /** * Cache plugin that serializes data to the cache and deserializes data from the cache
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `concurrency: 44`, `import: 4`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ICacheClient.js, node, IPartitionManager.js, TokenCache.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/request/InteractiveRequest.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.059 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.803 IQR)
- **Top Global Matches:** file_cluster_13: 11.059, file_cluster_16: 11.371, file_cluster_2: 11.571
- **Magnitude:** 9.31 | **LOC:** 41 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, ILoopbackClient.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/BaseClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.072 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.464 IQR)
- **Top Global Matches:** file_cluster_8: 11.072, file_cluster_16: 11.127, file_cluster_13: 11.162
- **Magnitude:** 8.68 | **LOC:** 159 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (38.6891%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createTokenRequestHeaders` (Impact: 20.0 | O(2^N) | DB: 1)
    * *Intent:* // set Authority
  * `executePostToTokenEndpoint` (Impact: 11.6 | O(2^N) | DB: 5)
  * `createTokenQueryParameters` (Impact: 7.3 | O(2^N) | DB: 3)
    * *Intent:* /** * Wraps sendPostRequestAsync with necessary preflight and postflight logic * @param thumbprint -...
  * `sendPostRequest` (Impact: 4.8 | O(2^N) | DB: 4)
  * `constructor` (Impact: 4.2 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 2`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` packageMetadata.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/Imds.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.56 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.956 IQR)
- **Top Global Matches:** file_cluster_8: 9.56, file_cluster_13: 9.588, file_cluster_7: 9.815
- **Magnitude:** 8.57 | **LOC:** 194 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.7767%), Tech Debt (51.602%)
**Top Internal Functions/Classes:**
  * `tryCreate` (Impact: 54.1 | O(N^6) | DB: 1)
    * *Intent:* /** * Constructs an Imds instance with the specified configuration. * * @param logger - Logger insta...
  * `createRequest` (Impact: 12.1 | O(N^5) | DB: 2)
  * `constructor` (Impact: 6.2 | O(N^3) | DB: 1)
    * *Intent:* /** * Managed Identity source implementation for Azure Instance Metadata Service (IMDS).
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* `doc: 19`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, ImdsRetryPolicy.js, CryptoProvider.js, ManagedIdentityRequestParameters.js, NodeStorage.js, ManagedIdentityId.js, Constants.js, BaseManagedIdentitySource.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/ServiceFabric.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.629 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.078 IQR)
- **Top Global Matches:** file_cluster_8: 9.629, file_cluster_13: 9.687, file_cluster_7: 9.891
- **Magnitude:** 8.12 | **LOC:** 218 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.2937%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `tryCreate` (Impact: 42.2 | O(N^4) | DB: 3)
    * *Intent:* /**
  * `createRequest` (Impact: 12.0 | O(N^5) | DB: 3)
  * `getEnvironmentVariables` (Impact: 6.8 | O(N^5))
  * `constructor` (Impact: 6.7 | O(N^3) | DB: 2)
    * *Intent:* /** * Original source of code: https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/identity/Azu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 7`
* *Defense:* `safety: 2`, `doc: 23`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, CryptoProvider.js, NodeStorage.js, ManagedIdentityRequestParameters.js, ManagedIdentityId.js, Constants.js, BaseManagedIdentitySource.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/MachineLearning.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.945 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.997 IQR)
- **Top Global Matches:** file_cluster_13: 9.945, file_cluster_8: 10.1, file_cluster_7: 10.3
- **Magnitude:** 7.87 | **LOC:** 220 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.0179%), Tech Debt (46.1017%)
**Top Internal Functions/Classes:**
  * `createRequest` (Impact: 28.4 | O(N^5) | DB: 3)
    * *Intent:* * * This method validates the Azure Machine Learning environment by checking for the required * MSI_...
  * `tryCreate` (Impact: 26.5 | O(N^4))
  * `constructor` (Impact: 6.7 | O(N^3) | DB: 2)
    * *Intent:* /** * Machine Learning Managed Identity Source implementation for Azure Machine Learning environment...
  * `getEnvironmentVariables` (Impact: 4.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 2`, `doc: 23`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node, CryptoProvider.js, ManagedIdentityRequestParameters.js, NodeStorage.js, ManagedIdentityId.js, Constants.js, BaseManagedIdentitySource.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/src/packageMetadata.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.29 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, immutability_locks: 2, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/src/request/ClientCredentialRequest.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, doc: 2, generics: 2
- `package/src/utils/EncodingUtils.ts` (TYPESCRIPT) | Magnitude: 3.14 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, doc: 8, structural_boundaries: 7, regex_execution: 5
- `package/src/cache/ITokenCache.ts` (TYPESCRIPT) | Magnitude: 3.1 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 5, args: 4, func_start: 4, concurrency: 4
- `package/src/config/Configuration.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 117, branch: 31, structural_boundaries: 23, sec_high_risk_execution: 18
- `package/src/crypto/CryptoProvider.ts` (TYPESCRIPT) | Magnitude: 6.9 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 46, concurrency: 22, doc: 18, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/src/request/SilentFlowRequest.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, indent_spaces: 3, generics: 2
- `package/src/request/CommonClientCredentialRequest.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, doc: 4, branch: 3, structural_boundaries: 3
- `package/src/request/CommonOnBehalfOfRequest.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.262 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, doc: 3, generics: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/src/client/UsernamePasswordClient.ts` (TYPESCRIPT) | Magnitude: 20.01 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 52, concurrency: 39, structural_boundaries: 14
- `package/src/network/LoopbackClient.ts` (TYPESCRIPT) | Magnitude: 16.59 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 32, branch: 20, concurrency: 18
- `package/src/client/DeviceCodeClient.ts` (TYPESCRIPT) | Magnitude: 39.03 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 320, state_mutation: 83, concurrency: 58, branch: 31
- `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT) | Magnitude: 51.83 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 316, state_mutation: 127, concurrency: 70, branch: 29
- `package/src/cache/NodeStorage.ts` (TYPESCRIPT) | Magnitude: 43.79 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 304, state_mutation: 96, doc: 60, concurrency: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `package/src/cache/distributed/ICacheClient.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `package/src/request/CommonDeviceCodeRequest.ts` (TYPESCRIPT) | Magnitude: 6.33 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, doc: 5, structural_boundaries: 4, branch: 3
- `package/src/client/ManagedIdentitySources/Imds.ts` (TYPESCRIPT) | Magnitude: 8.57 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, doc: 19, structural_boundaries: 14, state_mutation: 8
- `package/src/request/OnBehalfOfRequest.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 3, doc: 3, generics: 2
- `package/src/error/ManagedIdentityError.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 10, safety: 10, api: 4
- `package/src/client/BaseClient.ts` (TYPESCRIPT) | Magnitude: 8.68 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 29, doc: 14, structural_boundaries: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/config/ManagedIdentityRequestParameters.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/error/ManagedIdentityErrorCodes.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/retry/LinearRetryStrategy.ts` -> **Severity: 1298.692** (Blast Radius: 12.987 * Doc Risk: 99.9994%)
- `package/src/index.ts` -> **Severity: 1298.684** (Blast Radius: 12.987 * Doc Risk: 99.9988%)
- `package/src/utils/NetworkUtils.ts` -> **Severity: 1298.296** (Blast Radius: 12.987 * Doc Risk: 99.9689%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
