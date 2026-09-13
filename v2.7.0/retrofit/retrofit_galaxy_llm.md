# ARCHITECTURAL_BRIEF: retrofit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/square/retrofit` |
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
| Total Artifacts | 1109 |
| Analyzed Artifacts (Scanned) | 453 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 656 |
| Total LOC | 44357 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 40.8% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4297 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4786 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6885 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 306 | 28151 | 67.5% |
| PLAINTEXT | 31 | 1 | 6.8% |
| JAVASCRIPT | 29 | 1255 | 6.4% |
| CSS | 28 | 13222 | 6.2% |
| MARKDOWN | 26 | 0 | 5.7% |
| KOTLIN | 16 | 1152 | 3.5% |
| XML | 7 | 0 | 1.5% |
| HTML | 4 | 435 | 0.9% |
| JSON | 2 | 6 | 0.4% |
| BATCH | 1 | 71 | 0.2% |
| PROTO | 1 | 10 | 0.2% |
| GROOVY | 1 | 39 | 0.2% |
| TYPESCRIPT | 1 | 15 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 395 | 87.2% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 12.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 656*

**Composition by Extension & Reason:**
- `.html`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 37x Excluded (Machine-Generated Source Code Signature: 127 LOC), 27x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `no_extension`: 24x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 253 LOC)
- `.gradle`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 7x Unsupported Format (.pro)
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.json5`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')
- `.properties`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.processors`: 1x Unsupported Format (.processors)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.7 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 44.1 | 48.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.9 | 8.8 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 45.3 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 21.5 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 67.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 198 | 81 | 1 | `retrofit/src/main/java/retrofit2/RequestFactory.java` |
| cleanup | 25 | 20 | 0 | `retrofit/src/main/java/retrofit2/BuiltInConverters.java` |
| guards | 2996 | 276 | 16 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| danger | 2013 | 232 | 10 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| concurrency | 713 | 62 | 5 | `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` |
| connectivity | 2616 | 288 | 15 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| io | 268 | 46 | 1 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 9 | 3 | 0 | `retrofit-adapters/scala/src/test/java/retrofit2/adapter/scala/FutureTest.java` |
| serialization | 24 | 8 | 0 | `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` |
| regex | 9 | 7 | 0 | `retrofit/src/main/java/retrofit2/RequestFactory.java` |
| events | 762 | 100 | 6 | `retrofit/java-test/src/test/java/retrofit2/CallTest.java` |
| tests | 2998 | 127 | 17 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| docs | 293 | 108 | 2 | `retrofit/src/main/java/retrofit2/Retrofit.java` |
| debt | 251 | 47 | 1 | `retrofit/java-test/src/test/java/retrofit2/CallTest.java` |
| mutation | 5442 | 278 | 32 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| dead_code | 1272 | 238 | 8 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 184 | 94 | 1 | `retrofit/kotlin-test/src/test/java/retrofit2/KotlinSuspendTest.kt` |
| ml_ai | 12 | 4 | 0 | `retrofit-mock/src/main/java/retrofit2/mock/NetworkBehavior.java` |
| ui | 311 | 55 | 2 | `website/public/2.x/converter-kotlinx-serialization/styles/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.9412**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (Hits: 34)
- `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/index.html` (Hits: 28)
- `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/as-converter-factory.html` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Retrofit.java** (`retrofit/src/main/java/retrofit2/Retrofit.java`) — 133 inbound connections
2. **Response.java** (`retrofit/src/main/java/retrofit2/Response.java`) — 100 inbound connections
3. **GET.java** (`retrofit/src/main/java/retrofit2/http/GET.java`) — 97 inbound connections
4. **Converter.java** (`retrofit/src/main/java/retrofit2/Converter.java`) — 58 inbound connections
5. **Call.java** (`retrofit/src/main/java/retrofit2/Call.java`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RequestFactoryTest.java** (`retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java`) — 49 outbound dependencies
2. **RetrofitTest.java** (`retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) — 45 outbound dependencies
3. **RequestFactory.java** (`retrofit/src/main/java/retrofit2/RequestFactory.java`) — 45 outbound dependencies
4. **MoshiConverterFactoryTest.java** (`retrofit-converters/moshi/src/test/java/retrofit2/converter/moshi/MoshiConverterFactoryTest.java`) — 36 outbound dependencies
5. **CallTest.java** (`retrofit/java-test/src/test/java/retrofit2/CallTest.java`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseParameterAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **349.3** | LOC: 457
- `resolve` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **69.5** | LOC: 71
- `equals` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **38.6** | LOC: 44
  * *Intent:* /** Returns true if {@code a} and {@code b} are equal. */
- `parseMethodAnnotation` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **37.2** | LOC: 37
- `getGenericSupertype` (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **33.5** | LOC: 31
  * *Intent:* /** * Returns the generic supertype for {@code supertype}. For example, given a class {@code * IntegerSet}, the result for when supertype is {@code Se...
- `parseParameter` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **28.7** | LOC: 37
- `request` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`) -> Impact: **25.5** | LOC: 30
- `emitResponse` (@ `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/CallArbiter.java`) -> Impact: **24.0** | LOC: 27
- `enqueue` (@ `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java`) -> Impact: **22.8** | LOC: 60
- `parseHeaders` (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **22.0** | LOC: 24

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `retrofit/android-test` | 1 | 5000.0 | 0.0% | 0.0% |
| `retrofit/java-test/src/test/java/retrofit2` | 17 | 2635.74 | 9.05% | 0.0% |
| `retrofit/src/main/java/retrofit2` | 28 | 2605.22 | 28.35% | 35.98% |
| `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2` | 27 | 1729.88 | 24.56% | 0.0% |
| `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3` | 27 | 1727.82 | 24.56% | 0.0% |
| `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava` | 19 | 1138.48 | 15.65% | 0.0% |
| `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization` | 2 | 871.46 | 21.83% | 0.0% |
| `samples/src/main/java/com/example/retrofit` | 14 | 537.42 | 17.67% | 0.0% |
| `retrofit-mock/src/test/java/retrofit2/mock` | 5 | 508.58 | 38.5% | 0.0% |
| `website/public/2.x/converter-kotlinx-serialization` | 2 | 456.06 | 9.31% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` -> **99.9988%** Exposure
- `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/BodyObservable.java` -> **99.998%** Exposure
- `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/BodyObservable.java` -> **99.998%** Exposure
- `retrofit-adapters/guava/src/main/java/retrofit2/adapter/guava/GuavaCallAdapterFactory.java` -> **99.9608%** Exposure
- `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/BodyOnSubscribe.java` -> **99.956%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `retrofit/src/main/java/retrofit2/Platform.java` -> **100.0%** Exposure
- `retrofit/test-helpers/src/main/java/retrofit2/helpers/NonMatchingConverterFactory.java` -> **100.0%** Exposure
- `website/public/1.x/converter-jackson/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-protobuf/script.js` -> **100.0%** Exposure
- `website/public/1.x/converter-simplexml/script.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` -> **168** Orphaned Functions | **26** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/CallTest.java` -> **46** Orphaned Functions | **52** Duplicates
- `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` -> **72** Orphaned Functions | **12** Duplicates
- `retrofit-mock/src/test/java/retrofit2/mock/CallsTest.java` -> **16** Orphaned Functions | **15** Duplicates
- `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` -> **10** Orphaned Functions | **11** Duplicates

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
- **Unknown Dependencies:** `3184` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java` (JAVA) -> Cumulative Risk: **705.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 131.86 | **LOC:** 178 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9998%)
- **Heaviest Functions:** `enqueue` (Impact: 22.8), `run` (Impact: 12.7), `execute` (Impact: 5.5)

### 2. `retrofit/src/main/java/retrofit2/RequestBuilder.java` (JAVA) -> Cumulative Risk: **660.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 224.94 | **LOC:** 299 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (97.3145%)
- **Heaviest Functions:** `canonicalizeForPath` (Impact: 21.1), `RequestBuilder` (Impact: 19.6), `get` (Impact: 16.9)

### 3. `website/public/2.x/converter-kotlinx-serialization/scripts/navigation-loader.js` (JAVASCRIPT) -> Cumulative Risk: **643.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.82 | **LOC:** 96 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `scrollNavigationToSelectedElement` (Impact: 8.8), `revealNavigationForCurrentPage` (Impact: 7.9), `revealParents` (Impact: 4.6)

### 4. `retrofit/src/main/java/retrofit2/OkHttpCall.java` (JAVA) -> Cumulative Risk: **588.34**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 157.42 | **LOC:** 353 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.9167%), Tech Debt (91.6162%), State Flux (86.7078%)
- **Heaviest Functions:** `enqueue` (Impact: 10.5), `getRawCall` (Impact: 8.2), `parseResponse` (Impact: 6.1)

### 5. `retrofit/src/main/java/retrofit2/CompletableFutureCallAdapterFactory.java` (JAVA) -> Cumulative Risk: **581.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 102.04 | **LOC:** 158 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `onResponse` (Impact: 5.6), `cancel` (Impact: 3.2), `CallCancelCompletableFuture` (Impact: 3.0)

### 6. `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` (JAVA) -> Cumulative Risk: **538.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 77.32 | **LOC:** 176 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9988%), Concurrency (99.9984%), Documentation (92.0%)
- **Heaviest Functions:** `adapt` (Impact: 7.3), `onResponse` (Impact: 5.6), `adapt` (Impact: 4.2)

### 7. `retrofit-mock/src/main/java/retrofit2/mock/MockRetrofit.java` (JAVA) -> Cumulative Risk: **536.2**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 62.72 | **LOC:** 84 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `build` (Impact: 3.2), `Builder` (Impact: 3.1), `networkBehavior` (Impact: 3.1)

### 8. `retrofit/src/main/java/retrofit2/KotlinExtensions.kt` (KOTLIN) -> Cumulative Risk: **532.91**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 36.38 | **LOC:** 126 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.7669%), Concurrency (94.845%), Documentation (78.5714%)
- **Heaviest Functions:** `onResponse` (Impact: 9.7), `onResponse` (Impact: 5.5), `onFailure` (Impact: 1.9)

### 9. `retrofit/src/main/java/retrofit2/Utils.java` (JAVA) -> Cumulative Risk: **527.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 406.5 | **LOC:** 558 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (87.2727%), State Flux (83.2018%), Verification (80.0%)
- **Heaviest Functions:** `resolve` (Impact: 69.5), `equals` (Impact: 38.6), `getGenericSupertype` (Impact: 33.5)

### 10. `retrofit-mock/src/main/java/retrofit2/mock/Calls.java` (JAVA) -> Cumulative Risk: **515.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 107.6 | **LOC:** 215 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (91.7349%), Concurrency (90.2227%), Documentation (80.8511%)
- **Heaviest Functions:** `enqueue` (Impact: 10.7), `execute` (Impact: 4.7), `FakeCall` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `retrofit/android-test/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1092.82 | **LOC:** 3422 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `multipartPartMapWithEncoding` (Impact: 7.7)
  * `multipartWithEncoding` (Impact: 7.6)
  * `malformedAnnotationRelativeUrlThrows` (Impact: 6.8)
  * `malformedParameterRelativeUrlThrows` (Impact: 6.8)
  * `headersDoNotOverwriteEachOther` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *Amplified Sql Injection:* 18 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 878`, `args: 344`, `func_start: 273`, `class_start: 176`
* *Risk/State:* `safety_bypasses: 231`, `state_mutation: 64`, `duplicate_logic: 26`, `unreferenced_by_name: 168`
* *Architecture:* `io: 34`, `api: 172`, `import: 49`
* *Defense:* `safety: 147`, `test: 661`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.math.BigInteger, java.net.URI, java.util.Arrays, java.util.Arrays.asList, java.util.Collections, java.util.Collections.emptyList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 645.56 | **LOC:** 873 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.6898%), Tech Debt (8.5505%)
**Top Internal Functions/Classes:**
  * `parseParameterAnnotation` (Impact: 349.3)
  * `parseMethodAnnotation` (Impact: 37.2)
  * `parseParameter` (Impact: 28.7)
  * `parseHeaders` (Impact: 22.0)
  * `boxIfPrimitive` (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 179`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 48`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `import: 45`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.Method, java.lang.reflect.ParameterizedType, java.lang.reflect.Type, java.net.URI, java.util.ArrayList, java.util.LinkedHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 620.54 | **LOC:** 1806 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unresolvableResponseTypeThrows` (Impact: 16.1)
  * `unresolvableParameterTypeThrows` (Impact: 16.1)
  * `callAdapterFactoryQueriedCanDelegateTwiceWithoutRecursion` (Impact: 14.9)
  * `callAdapterFactoryQueriedCanDelegate` (Impact: 12.2)
  * `callAdapterFactoryQueried` (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 505`, `args: 133`, `func_start: 123`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 14`, `duplicate_logic: 12`, `unreferenced_by_name: 72`
* *Architecture:* `api: 117`, `concurrency: 54`, `import: 45`
* *Defense:* `safety: 80`, `doc: 1`, `test: 197`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.lang.annotation.Annotation, java.lang.annotation.Retention, java.lang.annotation.RetentionPolicy.RUNTIME, java.lang.reflect.ParameterizedType, java.lang.reflect.Type, java.net.MalformedURLException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/CallTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 579.74 | **LOC:** 1522 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `conversionProblemIncomingMaskedByConverterIsUnwrapped` (Impact: 3.8)
  * `fatalErrorsAreNotCaughtEnqueue` (Impact: 3.5)
  * `requestThrowingBeforeEnqueueFailsEnqueue` (Impact: 3.4)
  * `requestThrowingNonFatalErrorBeforeEnqueueFailsEnqueue` (Impact: 3.4)
  * `requestAfterEnqueueFailingThrows` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Concurrency (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 462`, `args: 108`, `func_start: 106`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 47`, `duplicate_logic: 52`, `unreferenced_by_name: 46`
* *Architecture:* `io: 2`, `api: 104`, `concurrency: 51`, `import: 33`
* *Defense:* `safety: 60`, `test: 169`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.io.InterruptedIOException, java.lang.annotation.Annotation, java.lang.reflect.Type, java.util.concurrent.CountDownLatch, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.SECONDS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 463.15 | **LOC:** 151 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9046%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 64`, `args: 29`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 28`, `api: 32`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js, symbol-parameters-wrapper_deferred.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 438.38 | **LOC:** 147 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6179%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 55`, `args: 25`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 26`, `api: 32`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` playground.min.js, logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/as-converter-factory.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 408.31 | **LOC:** 128 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.7501%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 43`, `args: 22`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 27`, `api: 30`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js, symbol-parameters-wrapper_deferred.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Utils.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 406.5 | **LOC:** 558 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.6381%), Tech Debt (34.5352%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 69.5)
  * `equals` (Impact: 38.6)
    * *Intent:* /** Returns true if {@code a} and {@code b} are equal. */
  * `getGenericSupertype` (Impact: 33.5)
    * *Intent:* /** * Returns the generic supertype for {@code supertype}. For example, given a class {@code * Integ...
  * `hasUnresolvableType` (Impact: 18.5)
  * `getRawType` (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 138`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 19`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 42`, `doc: 7`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.Array, java.lang.reflect.GenericArrayType, java.lang.reflect.GenericDeclaration, java.lang.reflect.Method, java.lang.reflect.ParameterizedType, java.lang.reflect.Type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Retrofit.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 287.2 | **LOC:** 717 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.1153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadServiceMethod` (Impact: 21.6)
  * `validateServiceInterface` (Impact: 18.5)
  * `invoke` (Impact: 12.7)
  * `nextRequestBodyConverter` (Impact: 11.8)
    * *Intent:* /** * Returns a {@link Converter} for {@code type} to {@link RequestBody} from the available * {@lin...
  * `nextResponseBodyConverter` (Impact: 11.6)
    * *Intent:* /** * Returns a {@link Converter} for {@link ResponseBody} to {@code type} from the available * {@li...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 92`, `args: 27`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 47`
* *Architecture:* `api: 30`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 20`, `doc: 28`, `sync_locks: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 99.57
  * `Choke Point (Betweenness):` 0.002682 | `Ripple Effect (Closeness):` 0.280261
  * `Imports (Out-Degree: 4):` java.lang.annotation.Annotation, java.lang.reflect.InvocationHandler, java.lang.reflect.Method, java.lang.reflect.Modifier, java.lang.reflect.Proxy, java.lang.reflect.Type, java.net.URL, java.util.ArrayDeque...
  * `Imported By (In-Degree: 133):` (Excluded from Brief to save tokens)

### `retrofit/src/main/java/retrofit2/ParameterHandler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 225.28 | **LOC:** 459 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9841%), Tech Debt (12.2901%)
**Top Internal Functions/Classes:**
  * `apply` (Impact: 17.3)
  * `apply` (Impact: 17.3)
  * `apply` (Impact: 13.5)
  * `apply` (Impact: 13.1)
  * `apply` (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 85`, `args: 35`, `func_start: 35`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 49`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `import: 8`
* *Defense:* `safety: 8`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.IOException, java.lang.reflect.Array, java.lang.reflect.Method, java.util.Map, java.util.Objects, javax.annotation.Nullable, okhttp3.MultipartBody, okhttp3.RequestBody
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 224.94 | **LOC:** 299 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.5855%), Tech Debt (88.1269%)
**Top Internal Functions/Classes:**
  * `canonicalizeForPath` (Impact: 21.1)
  * `RequestBuilder` (Impact: 19.6)
  * `get` (Impact: 16.9)
  * `addQueryParam` (Impact: 14.9)
  * `addHeader` (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 48`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 37`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.io.IOException, java.util.regex.Pattern, javax.annotation.Nullable, okhttp3.FormBody, okhttp3.Headers, okhttp3.HttpUrl, okhttp3.MediaType, okhttp3.MultipartBody...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 220.48 | **LOC:** 372 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.0322%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `togglePlatformDependent` (Impact: 20.1)
  * `handleAnchor` (Impact: 15.4)
  * `setItem` (Impact: 8.9)
  * `searchForContentTarget` (Impact: 8.8)
  * `scrollToElementInContent` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 71`, `args: 49`, `func_start: 26`
* *Risk/State:* `state_mutation: 29`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 4`, `concurrency: 1`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.51
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006637
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/FlowableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 216.24 | **LOC:** 348 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 5`, `unreferenced_by_name: 11`
* *Architecture:* `api: 28`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.Flowable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 216.24 | **LOC:** 348 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 93`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 5`, `unreferenced_by_name: 11`
* *Architecture:* `api: 28`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 25`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.Observable, io.reactivex.Observer, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/FlowableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 215.8 | **LOC:** 338 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.4)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 5`, `unreferenced_by_name: 11`
* *Architecture:* `api: 28`, `concurrency: 17`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Flowable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 215.8 | **LOC:** 338 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.4)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 89`, `args: 34`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 5`, `unreferenced_by_name: 11`
* *Architecture:* `api: 28`, `concurrency: 17`, `import: 18`
* *Defense:* `test: 22`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Observable, io.reactivex.rxjava3.core.Observer, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/MaybeThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 200.66 | **LOC:** 287 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.4)
  * `responseThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 79`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 22`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.Maybe, io.reactivex.MaybeObserver, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/MaybeThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 200.22 | **LOC:** 280 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.3)
  * `responseThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 75`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 22`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Maybe, io.reactivex.rxjava3.core.MaybeObserver, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 198.4 | **LOC:** 284 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.4)
  * `responseThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 78`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 21`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.Single, io.reactivex.SingleObserver, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 197.96 | **LOC:** 277 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.6)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.3)
  * `responseThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 74`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 21`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Single, io.reactivex.rxjava3.core.SingleObserver, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 191.26 | **LOC:** 338 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setUp` (Impact: 3.1)
  * `asyncCanBeCanceled` (Impact: 2.8)
  * `asyncCanBeCanceledBeforeStart` (Impact: 2.6)
  * `asyncFailureTriggersFailureAfterDelay` (Impact: 2.5)
  * `asyncSuccessCalledAfterDelay` (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Concurrency (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 83`, `args: 26`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 11`
* *Architecture:* `api: 24`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 10`, `test: 36`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.util.Random, java.util.concurrent.CountDownLatch, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS, java.util.concurrent.TimeUnit.SECONDS, java.util.concurrent.atomic.AtomicLong...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 186.6 | **LOC:** 344 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.8474%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 5.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 5.8)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 5.0)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 4.7)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 96`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 11`, `duplicate_logic: 11`, `unreferenced_by_name: 10`
* *Architecture:* `api: 30`, `concurrency: 17`, `import: 19`
* *Defense:* `safety: 6`, `test: 22`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Rule, org.junit.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 170.62 | **LOC:** 330 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 3.9)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 94`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 11`, `duplicate_logic: 11`, `unreferenced_by_name: 10`
* *Architecture:* `api: 30`, `concurrency: 17`, `import: 17`
* *Defense:* `test: 22`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Rule, org.junit.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 163.68 | **LOC:** 293 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.5046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resultThrowingInOnErrorDeliveredToPlugin` (Impact: 5.0)
  * `bodyThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` (Impact: 4.8)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.5)
  * `responseThrowingInOnSuccessDeliveredToPlugin` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 86`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 12`, `duplicate_logic: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 26`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Ignore, org.junit.Rule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `retrofit/src/main/java/retrofit2/RequestFactory.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 645.56
- `retrofit/src/main/java/retrofit2/Invocation.java` -> **Jesse Wilson** (100.0% isolated ownership) | Magnitude: 55.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 0.006** (Bridge: 0.0005 * Flux: 11.6846%)
- `retrofit/test-helpers/src/main/java/retrofit2/helpers/NonMatchingConverterFactory.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/RxJavaCallAdapterFactory.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.4802%)
- `retrofit-converters/gson/src/main/java/retrofit2/converter/gson/GsonConverterFactory.java` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 11.9203%)
- `retrofit-mock/src/main/java/retrofit2/mock/BehaviorDelegate.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 37.6731%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 25.74** (Embedded: 0.2803 * Error Risk: 91.8435%)
- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 13.949** (Embedded: 0.2213 * Error Risk: 63.026%)
- `retrofit/src/main/java/retrofit2/http/GET.java` -> **Severity: 12.681** (Embedded: 0.2283 * Error Risk: 55.5485%)
- `retrofit/src/main/java/retrofit2/http/Header.java` -> **Severity: 10.375** (Embedded: 0.1882 * Error Risk: 55.1248%)
- `retrofit/src/main/java/retrofit2/Converter.java` -> **Severity: 9.599** (Embedded: 0.146 * Error Risk: 65.7332%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 1687.632** (Blast Radius: 99.57 * Doc Risk: 16.9492%)
- `retrofit/test-helpers/src/main/java/retrofit2/helpers/ToStringConverterFactory.java` -> **Severity: 584.9** (Blast Radius: 5.849 * Doc Risk: 100.0%)
- `retrofit-converters/kotlinx-serialization/src/main/java/retrofit2/converter/kotlinx/serialization/Serializer.kt` -> **Severity: 265.7** (Blast Radius: 2.657 * Doc Risk: 100.0%)
- `retrofit/test-helpers/src/main/java/retrofit2/helpers/ObjectInstanceConverterFactory.java` -> **Severity: 222.6** (Blast Radius: 2.226 * Doc Risk: 100.0%)
- `retrofit-converters/wire/src/test/java/retrofit2/converter/wire/Phone.java` -> **Severity: 167.2** (Blast Radius: 1.672 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
