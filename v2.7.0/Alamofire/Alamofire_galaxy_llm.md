# ARCHITECTURAL_BRIEF: Alamofire
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Alamofire/Alamofire` |
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
| Total Artifacts | 566 |
| Analyzed Artifacts (Scanned) | 158 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 408 |
| Total LOC | 25907 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 27.9% |
| Dominant Lang | SWIFT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SWIFT | 95 | 25356 | 60.1% |
| PLAINTEXT | 23 | 21 | 14.6% |
| JSON | 19 | 507 | 12.0% |
| XML | 10 | 0 | 6.3% |
| MARKDOWN | 9 | 0 | 5.7% |
| RUBY | 2 | 23 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.483`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 126 | 79.7% |
| Unknown | 21 | 13.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 7.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 408*

**Composition by Extension & Reason:**
- `.html`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.xcscheme`: 7x Excluded (Unsupported Extension: '.xcscheme')
- `.xctestplan`: 5x Excluded (Unsupported Extension: '.xctestplan')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbxproj`: 3x Excluded (Unsupported Extension: '.pbxproj')
- `.der`: 2x Excluded (Explicitly Denied Extension: '.der')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 77.0 | 15.9 | 11.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.4 | 24.9 | 24.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 15.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 68.8 | 3.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.7 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 73.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 45.1 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 243 | 49 | 5 | `Source/Features/URLEncodedFormEncoder.swift` |
| cleanup | 28 | 13 | 0 | `Source/Features/AuthenticationInterceptor.swift` |
| guards | 1824 | 78 | 39 | `Tests/SessionTests.swift` |
| danger | 166 | 35 | 4 | `Source/Features/ResponseSerialization.swift` |
| concurrency | 1716 | 65 | 42 | `Tests/ConcurrencyTests.swift` |
| connectivity | 1304 | 52 | 25 | `Source/Features/EventMonitor.swift` |
| io | 232 | 30 | 2 | `Source/Features/EventMonitor.swift` |
| crypto | 0 | 0 | 0 | - |
| ipc | 158 | 14 | 0 | `Source/Features/EventMonitor.swift` |
| time | 8 | 4 | 0 | `Tests/AuthenticationInterceptorTests.swift` |
| serialization | 30 | 10 | 0 | `Source/Core/ParameterEncoder.swift` |
| regex | 0 | 0 | 0 | - |
| events | 149 | 4 | 0 | `Tests/CombineTests.swift` |
| tests | 2473 | 33 | 55 | `Tests/ResponseSerializationTests.swift` |
| docs | 3809 | 47 | 82 | `Source/Core/Session.swift` |
| debt | 68 | 16 | 0 | `Source/Features/Concurrency.swift` |
| mutation | 6587 | 90 | 141 | `Tests/RequestTests.swift` |
| dead_code | 1116 | 77 | 20 | `Tests/ServerTrustEvaluatorTests.swift` |
| credential | 1 | 1 | 0 | `Tests/ParameterEncoderTests.swift` |
| threat | 98 | 28 | 1 | `Source/Core/Request.swift` |
| ml_ai | 37 | 10 | 0 | `Source/Features/RetryPolicy.swift` |
| ui | 22 | 7 | 0 | `watchOS Example/watchOS Example WatchKit Extension/ContentView.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Source/Features/EventMonitor.swift` (Hits: 70)
- `Tests/MultipartFormDataTests.swift` (Hits: 34)
- `Tests/NSLoggingEventMonitor.swift` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Combine.swift** (`Source/Features/Combine.swift`) — 2 inbound connections
2. **AdvancedUsage.md** (`Documentation/AdvancedUsage.md`) — 1 inbound connections
3. **Alamofire.podspec** (`Alamofire.podspec`) — 0 inbound connections
4. **Gemfile** (`Gemfile`) — 0 inbound connections
5. **IDEWorkspaceChecks.plist** (`Alamofire.xcodeproj/project.xcworkspace/xcshareddata/IDEWorkspaceChecks.plist`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **MultipartFormData.swift** (`Source/Features/MultipartFormData.swift`) — 4 outbound dependencies
2. **RequestTests.swift** (`Tests/RequestTests.swift`) — 4 outbound dependencies
3. **Alamofire.swift** (`Source/Alamofire.swift`) — 3 outbound dependencies
4. **Combine.swift** (`Source/Features/Combine.swift`) — 3 outbound dependencies
5. **AuthenticationTests.swift** (`Tests/AuthenticationTests.swift`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `encode` (@ `Source/Core/ParameterEncoding.swift`) -> Impact: **96.6** | LOC: 200
  * *Intent:* /// Creates a `URLRequest` by encoding parameters and applying them on the passed request. /// /// - Parameters: /// - urlRequest: `URLRequestConverti...
- `set` (@ `Source/Features/URLEncodedFormEncoder.swift`) -> Impact: **54.5** | LOC: 51
  * *Intent:* /// Recursive backing method to `set(to:at:)`.
- `init` (@ `Source/Core/Session.swift`) -> Impact: **41.3** | LOC: 32
  * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on which to perform all response serialization. By defa...
- `urlSession` (@ `Source/Core/SessionDelegate.swift`) -> Impact: **34.9** | LOC: 27
- `init` (@ `Source/Core/Session.swift`) -> Impact: **30.5** | LOC: 33
  * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on which to perform all response serialization. By defa...
- `serialize` (@ `Source/Features/ResponseSerialization.swift`) -> Impact: **30.4** | LOC: 27
- `append` (@ `Source/Features/MultipartFormData.swift`) -> Impact: **30.3** | LOC: 70
  * *Intent:* /// Creates a body part from the file and appends it to the instance. /// /// The body part data will be encoded using the following format: /// /// -...
- `urlSession` (@ `Source/Core/SessionDelegate.swift`) -> Impact: **30.0** | LOC: 13
- `prepare` (@ `Example/Source/MasterViewController.swift`) -> Impact: **29.4** | LOC: 33
  * *Intent:* // MARK: - UIStoryboardSegue
- `executeMultipartFormDataUploadRequestWithProgress` (@ `Tests/UploadTests.swift`) -> Impact: **28.8** | LOC: 67
  * *Intent:* #endif // MARK: Combined Test Execution

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Tests/Resources/Certificates/alamofire-org` | 12 | 60000.0 | 0.0% | 0.0% |
| `Tests/Resources/Certificates/selfSignedAndMalformedCerts` | 5 | 25000.0 | 0.0% | 0.0% |
| `Tests/Resources/Certificates/expired-badssl-com` | 4 | 20000.0 | 0.0% | 0.0% |
| `Tests` | 44 | 9275.5 | 17.7% | 0.0% |
| `Source/Features` | 18 | 3615.56 | 26.44% | 41.69% |
| `Source/Core` | 17 | 3597.54 | 25.47% | 50.11% |
| `Example/Source` | 3 | 211.42 | 46.02% | 0.0% |
| `__monolith__` | 8 | 161.28 | 6.5% | 0.0% |
| `Source/Extensions` | 6 | 128.46 | 15.93% | 41.35% |
| `Documentation` | 6 | 80.48 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Source/Core/UploadRequest.swift` -> **99.9295%** Exposure
- `Source/Features/Concurrency.swift` -> **99.925%** Exposure
- `Source/Features/Validation.swift` -> **99.548%** Exposure
- `Source/Core/Notifications.swift` -> **99.1614%** Exposure
- `Source/Features/Combine.swift` -> **98.0708%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Alamofire.podspec` -> **100.0%** Exposure
- `Source/Extensions/StringEncoding+Alamofire.swift` -> **100.0%** Exposure
- `Source/Core/Request.swift` -> **99.9716%** Exposure
- `Source/Core/ParameterEncoding.swift` -> **99.9063%** Exposure
- `Source/Features/AuthenticationInterceptor.swift` -> **99.6491%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Tests/ParameterEncoderTests.swift` -> **86** Orphaned Functions | **0** Duplicates
- `Tests/ResponseSerializationTests.swift` -> **68** Orphaned Functions | **0** Duplicates
- `Tests/RequestTests.swift` -> **65** Orphaned Functions | **0** Duplicates
- `Tests/CombineTests.swift` -> **52** Orphaned Functions | **0** Duplicates
- `Tests/SessionTests.swift` -> **52** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `162` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Source/Core/WebSocketRequest.swift` (SWIFT) -> Cumulative Risk: **657.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 378.02 | **LOC:** 571 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), State Flux (97.595%)
- **Heaviest Functions:** `init` (Impact: 13.6), `streamSerializer` (Impact: 13.4), `close` (Impact: 11.6)

### 2. `Source/Features/URLEncodedFormEncoder.swift` (SWIFT) -> Cumulative Risk: **556.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 564.42 | **LOC:** 1142 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.1803%), Verification (80.0%), Documentation (77.7778%)
- **Heaviest Functions:** `set` (Impact: 54.5), `convert` (Impact: 14.7), `encode` (Impact: 13.5)

### 3. `Source/Core/DataRequest.swift` (SWIFT) -> Cumulative Risk: **526.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 211.02 | **LOC:** 463 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9992%), State Flux (92.8403%), Verification (80.0%)
- **Heaviest Functions:** `_response` (Impact: 23.4), `init` (Impact: 12.9), `updateDownloadProgress` (Impact: 10.4)

### 4. `Source/Features/Combine.swift` (SWIFT) -> Cumulative Risk: **514.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 236.8 | **LOC:** 653 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9984%), Tech Debt (98.0708%), State Flux (77.8534%)
- **Heaviest Functions:** `request` (Impact: 6.3), `publishString` (Impact: 5.5), `publishString` (Impact: 5.5)

### 5. `Source/Features/MultipartUpload.swift` (SWIFT) -> Cumulative Risk: **508.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 22.36 | **LOC:** 100 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.8976%), Tech Debt (93.5379%)
- **Heaviest Functions:** `build` (Impact: 5.3), `init` (Impact: 2.4), `asURLRequest` (Impact: 1.4)

### 6. `Source/Core/UploadRequest.swift` (SWIFT) -> Cumulative Risk: **493.47**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 75.34 | **LOC:** 178 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9295%), State Flux (98.095%), Concurrency (85.0473%)
- **Heaviest Functions:** `init` (Impact: 13.7), `task` (Impact: 12.7), `inputStream` (Impact: 5.7)

### 7. `Source/Core/Request.swift` (SWIFT) -> Cumulative Risk: **487.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 631.12 | **LOC:** 1249 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), State Flux (99.9716%), Tech Debt (75.3311%)
- **Heaviest Functions:** `cURLDescription` (Impact: 27.4), `appendResponseSerializer` (Impact: 12.4), `init` (Impact: 12.1)

### 8. `Source/Core/DataStreamRequest.swift` (SWIFT) -> Cumulative Risk: **453.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 258.84 | **LOC:** 594 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (83.1117%), State Flux (72.9446%)
- **Heaviest Functions:** `init` (Impact: 13.6), `didReceiveResponse` (Impact: 9.8), `validate` (Impact: 8.1)

### 9. `Source/Features/AuthenticationInterceptor.swift` (SWIFT) -> Cumulative Risk: **453.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 160.78 | **LOC:** 401 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.992%), State Flux (99.6491%), Documentation (61.5385%)
- **Heaviest Functions:** `adapt` (Impact: 24.0), `retry` (Impact: 19.6), `refresh` (Impact: 15.2)

### 10. `Source/Features/RequestCompression.swift` (SWIFT) -> Cumulative Risk: **449.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 52.9 | **LOC:** 147 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (88.0797%), State Flux (79.1391%), Documentation (55.5556%)
- **Heaviest Functions:** `adapt` (Impact: 23.8), `deflate` (Impact: 1.8), `adler32Checksum` (Impact: 1.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Tests/Resources/Certificates/alamofire-org/alamofire-root-ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/alamofire-signing-ca1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/alamofire-signing-ca2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/expired.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/missing-dns-name-and-uri.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/multiple-dns-names.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/signed-by-ca1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/signed-by-ca2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/test.alamofire.org.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/valid-dns-name.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/valid-uri.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/alamofire-org/wildcard.alamofire.org.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/expired-badssl-com/expired.badssl.com-intermediate-ca-1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/expired-badssl-com/expired.badssl.com-intermediate-ca-2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/expired-badssl-com/expired.badssl.com-leaf.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/expired-badssl-com/expired.badssl.com-root-ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/certDER.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/certDER.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/certPEM.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/certPEM.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/randomGibberish.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/DataStreamTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 863.6 | **LOC:** 1320 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5017%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testThatDataStreamWorksCorrectlyWithMultipleSerialQueues` (Impact: 27.9)
  * `testThatDataStreamWorksCorrectlyWithMultipleConcurrentQueues` (Impact: 26.6)
  * `testThatDataCanBeStreamedAndDecodedAtTheSameTime` (Impact: 24.7)
  * `testThatDataCanBeStreamedManyTimes` (Impact: 21.6)
  * `testThatDataStreamCanBeCancelledInClosure` (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 172`, `args: 86`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`, `unreferenced_by_name: 31`
* *Architecture:* `concurrency: 37`, `import: 2`
* *Defense:* `safety: 42`, `test: 127`, `sync_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alamofire, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/SessionTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 854.0 | **LOC:** 2017 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.2256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `retry` (Impact: 19.4)
  * `executeAuthorizationHeaderTest` (Impact: 19.1)
  * `testThatSessionCallsRequestRetrierForAllResponseSerializersThatThrowError` (Impact: 16.7)
  * `testThatDownloadRequestWithInvalidURLStringThrowsResponseHandlerError` (Impact: 14.3)
  * `testThatRetriedRequestsCanBeMassCancelled` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 215`, `args: 144`, `func_start: 65`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `unreferenced_by_name: 52`
* *Architecture:* `io: 4`, `concurrency: 58`, `import: 2`
* *Defense:* `safety: 102`, `test: 276`, `sync_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Core/Session.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 769.42 | **LOC:** 1458 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.271%), Tech Debt (48.2983%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 41.3)
    * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on wh...
  * `init` (Impact: 30.5)
    * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on wh...
  * `download` (Impact: 23.0)
    * *Intent:* /// - method: `HTTPMethod` for the `URLRequest`. `.get` by default. /// - parameters: `Parameters` (...
  * `download` (Impact: 23.0)
    * *Intent:* /// - convertible: `URLConvertible` value to be used as the `URLRequest`'s `URL`. /// - method: `HTT...
  * `streamRequest` (Impact: 20.0)
    * *Intent:* /// - encoder: `ParameterEncoder` to be used to encode the `parameters` value into the /// `URLReque...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 220`, `args: 63`, `func_start: 57`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 21`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 15`, `api: 50`, `concurrency: 50`, `import: 1`
* *Defense:* `safety: 33`, `doc: 479`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/RequestTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 764.6 | **LOC:** 1888 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.9832%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRequestResponseWithProgress` (Impact: 14.1)
  * `testPOSTRequestWithJSONParametersCURLDescription` (Impact: 12.7)
  * `testThatDataRequestOnHTTPResponseCanCancel` (Impact: 12.6)
  * `testPOSTRequestWithBase64EncodedImages` (Impact: 12.4)
  * `testThatDataRequestOnHTTPResponseCanAllow` (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 179`, `args: 209`, `func_start: 67`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 175`, `dead_code: 1`, `unreferenced_by_name: 65`
* *Architecture:* `io: 2`, `concurrency: 112`, `import: 4`
* *Defense:* `safety: 72`, `test: 191`, `sync_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Alamofire, Foundation, Testing, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Source/Core/AFError.swift` -> **Jon Shier** (100.0% isolated ownership) | Magnitude: 87.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Source/Features/Combine.swift` -> **Severity: 0.385** (Embedded: 0.0127 * Error Risk: 30.2218%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Example/Source/AppDelegate.swift` -> **Severity: 622.9** (Blast Radius: 6.229 * Doc Risk: 100.0%)
- `Example/Source/DetailViewController.swift` -> **Severity: 622.9** (Blast Radius: 6.229 * Doc Risk: 100.0%)
- `Example/Source/MasterViewController.swift` -> **Severity: 622.9** (Blast Radius: 6.229 * Doc Risk: 100.0%)
- `Source/Core/RequestTaskMap.swift` -> **Severity: 622.9** (Blast Radius: 6.229 * Doc Risk: 100.0%)
- `Source/Core/WebSocketRequest.swift` -> **Severity: 622.9** (Blast Radius: 6.229 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
