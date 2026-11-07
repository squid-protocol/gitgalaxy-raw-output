# ARCHITECTURAL_BRIEF: retrofit
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/square/retrofit` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 523 analyzed artifact(s), 46375 LOC.
- **Load-bearing artifact:** `retrofit/src/main/java/retrofit2/Retrofit.java` -- 154 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` -- pulls in 49 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `retrofit/android-test/debug.keystore` at magnitude 5000.0 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1109 |
| Analyzed Artifacts (Scanned) | 523 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 586 |
| Total LOC | 46375 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 47.2% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4411 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2791 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8184 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 306 | 28151 | 58.5% |
| PLAINTEXT | 34 | 1 | 6.5% |
| XML | 32 | 0 | 6.1% |
| MARKDOWN | 31 | 0 | 5.9% |
| JAVASCRIPT | 31 | 1313 | 5.9% |
| GROOVY | 30 | 633 | 5.7% |
| CSS | 30 | 14288 | 5.7% |
| KOTLIN | 16 | 1152 | 3.1% |
| HTML | 4 | 435 | 0.8% |
| JSON | 3 | 29 | 0.6% |
| YAML | 2 | 171 | 0.4% |
| SHELL | 1 | 106 | 0.2% |
| BATCH | 1 | 71 | 0.2% |
| PROTO | 1 | 10 | 0.2% |
| TYPESCRIPT | 1 | 15 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 522 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Declarative / Non-Code 25%, Generic / Templated Code Files 24%, State Mutators Files 5%, Large Core Modules (3) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 457 | 87.4% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 64 | 12.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 586*

**Composition by Extension & Reason:**
- `.html`: 41x Excluded (Machine-Generated Source Code Signature: 127 LOC), 29x Excluded (Machine-Generated Source Code Signature: 120 LOC), 24x Excluded (Machine-Generated Source Code Signature: 19 LOC)
- `no_extension`: 26x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 7x Unsupported Format (.pro)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.jar`: 1x Excluded (Explicitly Denied Extension: '.jar')
- `.processors`: 1x Unsupported Format (.processors)
- `.processor`: 1x Unsupported Format (.processor)
- `.release`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snapshot`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 7095 LOC)
- `.mdx`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.6 | 37.1 | 48.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.1 | 7.4 | 4.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 75.3 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 198 | 81 | 1 | `retrofit/src/main/java/retrofit2/RequestFactory.java` |
| cleanup | 25 | 20 | 0 | `retrofit/src/main/java/retrofit2/BuiltInConverters.java` |
| guards | 3001 | 278 | 14 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| danger | 2048 | 239 | 9 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| concurrency | 718 | 64 | 3 | `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` |
| connectivity | 2616 | 290 | 14 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| io | 295 | 50 | 0 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `gradlew` |
| time | 9 | 3 | 0 | `retrofit-adapters/scala/src/test/java/retrofit2/adapter/scala/FutureTest.java` |
| serialization | 24 | 8 | 0 | `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` |
| regex | 12 | 8 | 0 | `retrofit/src/main/java/retrofit2/RequestFactory.java` |
| events | 762 | 100 | 5 | `retrofit/java-test/src/test/java/retrofit2/CallTest.java` |
| tests | 2998 | 127 | 16 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| docs | 301 | 112 | 2 | `retrofit/src/main/java/retrofit2/Retrofit.java` |
| debt | 260 | 49 | 0 | `retrofit/java-test/src/test/java/retrofit2/CallTest.java` |
| mutation | 5572 | 289 | 29 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| dead_code | 1268 | 237 | 7 | `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `website/public/2.x/converter-kotlinx-serialization/scripts/symbol-parameters-wrapper_deferred.js` |
| ml_ai | 12 | 4 | 0 | `retrofit-mock/src/main/java/retrofit2/mock/NetworkBehavior.java` |
| ui | 331 | 59 | 2 | `website/public/2.x/converter-kotlinx-serialization/styles/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (Hits: 34)
- `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/index.html` (Hits: 28)
- `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/as-converter-factory.html` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Retrofit.java** (`retrofit/src/main/java/retrofit2/Retrofit.java`) — 154 inbound connections
2. **Response.java** (`retrofit/src/main/java/retrofit2/Response.java`) — 115 inbound connections
3. **GET.java** (`retrofit/src/main/java/retrofit2/http/GET.java`) — 97 inbound connections
4. **Converter.java** (`retrofit/src/main/java/retrofit2/Converter.java`) — 59 inbound connections
5. **Call.java** (`retrofit/src/main/java/retrofit2/Call.java`) — 54 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **RequestFactoryTest.java** (`retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java`) — 49 outbound dependencies
2. **RetrofitTest.java** (`retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java`) — 45 outbound dependencies
3. **RequestFactory.java** (`retrofit/src/main/java/retrofit2/RequestFactory.java`) — 45 outbound dependencies
4. **MoshiConverterFactoryTest.java** (`retrofit-converters/moshi/src/test/java/retrofit2/converter/moshi/MoshiConverterFactoryTest.java`) — 36 outbound dependencies
5. **CallTest.java** (`retrofit/java-test/src/test/java/retrofit2/CallTest.java`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseParameterAnnotation` **(Many-Argument Workhorses)** (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **248.7** | LOC: 457
- `resolve` **(Many-Argument Workhorses)** (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **51.5** | LOC: 71
- `parseMethodAnnotation` **(Defensive Guards)** (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **37.2** | LOC: 37
- `equals` **(Defensive Guards)** (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **31.6** | LOC: 44
  * *Intent:* /** Returns true if {@code a} and {@code b} are equal. */
- `getGenericSupertype` **(Compute Cores)** (@ `retrofit/src/main/java/retrofit2/Utils.java`) -> Impact: **25.6** | LOC: 31
  * *Intent:* /** * Returns the generic supertype for {@code supertype}. For example, given a class {@code * IntegerSet}, the result for when supertype is {@code Se...
- `enqueue` **(Generic / Templated Code)** (@ `retrofit-mock/src/main/java/retrofit2/mock/BehaviorCall.java`) -> Impact: **22.8** | LOC: 60
- `canonicalizeForPath` **(Stateful Encapsulated Methods)** (@ `retrofit/src/main/java/retrofit2/RequestBuilder.java`) -> Impact: **21.1** | LOC: 31
- `togglePlatformDependent` **(Defensive Guards)** (@ `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js`) -> Impact: **20.1** | LOC: 21
- `parseParameter` **(Stateful Encapsulated Methods)** (@ `retrofit/src/main/java/retrofit2/RequestFactory.java`) -> Impact: **19.7** | LOC: 37
- `RequestBuilder` **(Many-Argument Workhorses)** (@ `retrofit/src/main/java/retrofit2/RequestBuilder.java`) -> Impact: **19.6** | LOC: 31

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `retrofit/android-test` | 2 | 5022.74 | 7.09% | 0.0% |
| `retrofit/src/main/java/retrofit2` | 28 | 2233.52 | 24.4% | 36.09% |
| `retrofit/java-test/src/test/java/retrofit2` | 17 | 2140.24 | 2.04% | 0.0% |
| `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2` | 27 | 1652.18 | 23.76% | 0.0% |
| `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3` | 27 | 1650.12 | 23.76% | 0.0% |
| `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava` | 19 | 1110.98 | 14.91% | 0.0% |
| `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization` | 2 | 871.46 | 21.83% | 0.0% |
| `retrofit-mock/src/test/java/retrofit2/mock` | 5 | 500.38 | 16.25% | 0.0% |
| `website/public/2.x/converter-kotlinx-serialization` | 2 | 456.06 | 9.31% | 0.0% |
| `retrofit-mock/src/main/java/retrofit2/mock` | 8 | 442.36 | 39.4% | 19.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `retrofit-adapters/java8/src/main/java/retrofit2/adapter/java8/Java8CallAdapterFactory.java` -> **99.9988%** Exposure
- `retrofit-adapters/rxjava2/src/main/java/retrofit2/adapter/rxjava2/BodyObservable.java` -> **99.998%** Exposure
- `retrofit-adapters/rxjava3/src/main/java/retrofit2/adapter/rxjava3/BodyObservable.java` -> **99.998%** Exposure
- `retrofit-adapters/guava/src/main/java/retrofit2/adapter/guava/GuavaCallAdapterFactory.java` -> **99.9608%** Exposure
- `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/BodyOnSubscribe.java` -> **99.956%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gradlew` -> **100.0%** Exposure
- `retrofit/src/main/java/retrofit2/Platform.java` -> **100.0%** Exposure
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
- **Unknown Dependencies:** `3197` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `retrofit/android-test/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RequestFactoryTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.92)
- **Top Global Matches:** file_cluster_5: 6.92, file_cluster_7: 9.049, file_cluster_12: 10.314
- **Magnitude:** 786.72 | **LOC:** 3422 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **49**; blast radius 0.992; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.8%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encodedPathParametersAndPathTraversal` **(Annotated & Test Methods)** (Impact: 2.7)
  * `multipartPartMapWithEncoding` **(Annotated & Test Methods)** (Impact: 2.7)
  * `multipartWithEncoding` **(Annotated & Test Methods)** (Impact: 2.6)
  * `multipartPartMap` **(Annotated & Test Methods)** (Impact: 2.6)
  * `simpleMultipart` **(Annotated & Test Methods)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 878`, `args: 344`, `func_start: 273`, `class_start: 176`
* *Risk/State:* `safety_bypasses: 231`, `state_mutation: 64`, `duplicate_logic: 26`, `unreferenced_by_name: 168`
* *Architecture:* `io: 34`, `api: 172`, `import: 49`
* *Defense:* `safety: 147`, `test: 661`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 0.000125 | `Ripple Effect (Closeness):` 0.001916
  * `Imports (Out-Degree: 26):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.math.BigInteger, java.net.URI, java.util.Arrays, java.util.Arrays.asList, java.util.Collections, java.util.Collections.emptyList...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `retrofit/java-test/src/test/java/retrofit2/CallTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.781)
- **Top Global Matches:** file_cluster_5: 6.781, file_cluster_12: 9.303, file_cluster_0: 9.553
- **Magnitude:** 579.74 | **LOC:** 1522 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.3%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `conversionProblemIncomingMaskedByConverterIsUnwrapped` **(Annotated & Test Methods)** (Impact: 3.8)
  * `fatalErrorsAreNotCaughtEnqueue` **(Annotated & Test Methods)** (Impact: 3.5)
  * `requestThrowingBeforeEnqueueFailsEnqueue` **(Annotated & Test Methods)** (Impact: 3.4)
  * `requestThrowingNonFatalErrorBeforeEnqueueFailsEnqueue` **(Annotated & Test Methods)** (Impact: 3.4)
  * `requestAfterEnqueueFailingThrows` **(Annotated & Test Methods)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Concurrency (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 462`, `args: 108`, `func_start: 106`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 47`, `duplicate_logic: 52`, `unreferenced_by_name: 46`
* *Architecture:* `io: 2`, `api: 104`, `concurrency: 51`, `import: 33`
* *Defense:* `safety: 60`, `test: 169`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.io.InterruptedIOException, java.lang.annotation.Annotation, java.lang.reflect.Type, java.util.concurrent.CountDownLatch, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.SECONDS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestFactory.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.46)
- **Top Global Matches:** file_cluster_6: 11.46, file_cluster_4: 12.939, file_cluster_5: 16.042
- **Magnitude:** 498.96 | **LOC:** 873 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **45**; blast radius 12.36; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.1%), Guard Balance (formerly Safety Score) (58.8%), Complexity Load (formerly Cognitive Load) (45.6%), Debt Markers (formerly Tech Debt) (8.6%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseParameterAnnotation` **(Many-Argument Workhorses)** (Impact: 248.7)
  * `parseMethodAnnotation` **(Defensive Guards)** (Impact: 37.2)
  * `parseParameter` **(Stateful Encapsulated Methods)** (Impact: 19.7)
  * `parseHeaders` **(Stateful Encapsulated Methods)** (Impact: 13.3)
  * `boxIfPrimitive` **(Stateful Encapsulated Methods)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 179`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 48`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `import: 45`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.36
  * `Choke Point (Betweenness):` 0.021561 | `Ripple Effect (Closeness):` 0.121593
  * `Imports (Out-Degree: 29):` java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.Method, java.lang.reflect.ParameterizedType, java.lang.reflect.Type, java.net.URI, java.util.ArrayList, java.util.LinkedHashSet...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.51)
- **Top Global Matches:** file_cluster_13: 6.51, file_cluster_2: 8.283, file_cluster_10: 8.593
- **Magnitude:** 463.15 | **LOC:** 151 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (30.8%), Complexity Load (formerly Cognitive Load) (19.9%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 64`, `args: 29`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 28`, `api: 32`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js, symbol-parameters-wrapper_deferred.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/java-test/src/test/java/retrofit2/RetrofitTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.316)
- **Top Global Matches:** file_cluster_5: 6.316, file_cluster_12: 8.844, file_cluster_7: 9.692
- **Magnitude:** 458.94 | **LOC:** 1806 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (77.7%), Guard Balance (formerly Safety Score) (44.4%), Connectivity (formerly Api Exposure) (12.7%), Complexity Load (formerly Cognitive Load) (11.8%)
- **Documentation Coverage:** 99.1031% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotationParsingFailureObservedByWaitingThreads` **(Annotated & Test Methods)** (Impact: 5.2)
  * `unresolvableResponseTypeThrows` **(I/O & Config Routines)** (Impact: 4.1)
  * `unresolvableParameterTypeThrows` **(I/O & Config Routines)** (Impact: 4.0)
  * `callAdapterFactoryQueriedCanDelegateTwiceWithoutRecursion` **(Annotated & Test Methods)** (Impact: 4.0)
  * `callCallCustomAdapter` **(Annotated & Test Methods)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 505`, `args: 133`, `func_start: 123`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 14`, `duplicate_logic: 12`, `unreferenced_by_name: 72`
* *Architecture:* `api: 117`, `concurrency: 54`, `import: 45`
* *Defense:* `safety: 80`, `doc: 1`, `test: 197`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.lang.annotation.Annotation, java.lang.annotation.Retention, java.lang.annotation.RetentionPolicy.RUNTIME, java.lang.reflect.ParameterizedType, java.lang.reflect.Type, java.net.MalformedURLException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.534)
- **Top Global Matches:** file_cluster_13: 6.534, file_cluster_2: 8.251, file_cluster_12: 8.574
- **Magnitude:** 438.38 | **LOC:** 147 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (31.7%), Complexity Load (formerly Cognitive Load) (18.6%), Connectivity (formerly Api Exposure) (14.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 55`, `args: 25`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 26`, `api: 32`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` playground.min.js, logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/public/2.x/converter-kotlinx-serialization/kotlinx-serialization/retrofit2.converter.kotlinx.serialization/as-converter-factory.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.868)
- **Top Global Matches:** file_cluster_13: 6.868, file_cluster_2: 8.514, file_cluster_12: 8.564
- **Magnitude:** 408.31 | **LOC:** 128 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (37.2%), Complexity Load (formerly Cognitive Load) (23.8%), Connectivity (formerly Api Exposure) (14.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 43`, `args: 22`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 27`, `api: 30`, `concurrency: 18`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` logo-icon.svg, clipboard.js, main.js, navigation-loader.js, platform-content-handler.js, prism.js, sourceset_dependencies.js, symbol-parameters-wrapper_deferred.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/Utils.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.636)
- **Top Global Matches:** file_cluster_5: 8.636, file_cluster_12: 11.105, file_cluster_7: 11.146
- **Magnitude:** 318.8 | **LOC:** 558 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 23.505; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Mutation Surface (formerly State Flux) (77.3%), Complexity Load (formerly Cognitive Load) (44.3%)
- **Documentation Coverage:** 87.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `equals` **(Defensive Guards)** (Impact: 31.6)
    * *Intent:* /** Returns true if {@code a} and {@code b} are equal. */
  * `getGenericSupertype` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /** * Returns the generic supertype for {@code supertype}. For example, given a class {@code * Integ...
  * `WildcardTypeImpl` **(Compute Cores)** (Impact: 14.7)
  * `hasUnresolvableType` **(Defensive Guards)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 138`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 19`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 17`
* *Defense:* `safety: 42`, `doc: 7`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.505
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142581
  * `Imports (Out-Degree: 0):` java.io.IOException, java.lang.annotation.Annotation, java.lang.reflect.Array, java.lang.reflect.GenericArrayType, java.lang.reflect.GenericDeclaration, java.lang.reflect.Method, java.lang.reflect.ParameterizedType, java.lang.reflect.Type...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `retrofit/src/main/java/retrofit2/Retrofit.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.595)
- **Top Global Matches:** file_cluster_5: 6.595, file_cluster_7: 9.872, file_cluster_12: 9.992
- **Magnitude:** 249.1 | **LOC:** 717 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **154** in-repo importer(s); it depends on **25**; blast radius 81.968; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (79.1%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (43.4%), Concurrency Surface (formerly Concurrency) (25.0%)
- **Documentation Coverage:** 14.0351% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateServiceInterface` **(Stateful Encapsulated Methods)** (Impact: 12.9)
  * `loadServiceMethod` **(Defensive Guards)** (Impact: 12.9)
  * `invoke` **(Compute Cores)** (Impact: 8.7)
  * `nextRequestBodyConverter` **(I/O & Config Routines)** (Impact: 7.8)
    * *Intent:* /** * Returns a {@link Converter} for {@code type} to {@link RequestBody} from the available * {@lin...
  * `nextResponseBodyConverter` **(I/O & Config Routines)** (Impact: 7.6)
    * *Intent:* /** * Returns a {@link Converter} for {@link ResponseBody} to {@code type} from the available * {@li...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 92`, `args: 27`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 47`
* *Architecture:* `api: 30`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 20`, `doc: 28`, `sync_locks: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 81.968
  * `Choke Point (Betweenness):` 0.024193 | `Ripple Effect (Closeness):` 0.273504
  * `Imports (Out-Degree: 9):` java.lang.annotation.Annotation, java.lang.reflect.InvocationHandler, java.lang.reflect.Method, java.lang.reflect.Modifier, java.lang.reflect.Proxy, java.lang.reflect.Type, java.net.URL, java.util.ArrayDeque...
  * `Imported By (In-Degree: 154):` (Excluded from Brief to save tokens)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/FlowableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.739)
- **Top Global Matches:** file_cluster_5: 6.739, file_cluster_7: 10.171, file_cluster_12: 10.738
- **Magnitude:** 216.24 | **LOC:** 348 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.3%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.common.truth.Truth.assertThat, io.reactivex.Flowable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.785)
- **Top Global Matches:** file_cluster_5: 6.785, file_cluster_7: 10.203, file_cluster_12: 10.768
- **Magnitude:** 216.24 | **LOC:** 348 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.3%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.common.truth.Truth.assertThat, io.reactivex.Observable, io.reactivex.Observer, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/FlowableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.788)
- **Top Global Matches:** file_cluster_5: 6.788, file_cluster_7: 10.224, file_cluster_12: 10.836
- **Magnitude:** 215.8 | **LOC:** 338 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (65.2%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Flowable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.834)
- **Top Global Matches:** file_cluster_5: 6.834, file_cluster_7: 10.256, file_cluster_12: 10.865
- **Magnitude:** 215.8 | **LOC:** 338 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (65.2%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Observable, io.reactivex.rxjava3.core.Observer, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit/src/main/java/retrofit2/RequestBuilder.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.896)
- **Top Global Matches:** file_cluster_5: 7.896, file_cluster_12: 8.349, file_cluster_7: 8.423
- **Magnitude:** 212.94 | **LOC:** 299 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 1.622; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.4%), Debt Markers (formerly Tech Debt) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canonicalizeForPath` **(Stateful Encapsulated Methods)** (Impact: 21.1)
  * `RequestBuilder` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `get` **(I/O & Config Routines)** (Impact: 14.9)
  * `addQueryParam` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `addHeader` **(Defensive Guards)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 48`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 37`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.622
  * `Choke Point (Betweenness):` 0.001048 | `Ripple Effect (Closeness):` 0.096096
  * `Imports (Out-Degree: 6):` java.io.IOException, java.util.regex.Pattern, javax.annotation.Nullable, okhttp3.FormBody, okhttp3.Headers, okhttp3.HttpUrl, okhttp3.MediaType, okhttp3.MultipartBody...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `website/public/2.x/converter-kotlinx-serialization/scripts/platform-content-handler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.051)
- **Top Global Matches:** file_cluster_10: 7.051, file_cluster_15: 8.498, file_cluster_16: 9.214
- **Magnitude:** 211.48 | **LOC:** 372 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 1.148; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (43.0%), Connectivity (formerly Api Exposure) (29.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `togglePlatformDependent` **(Defensive Guards)** (Impact: 20.1)
  * `handleAnchor` **(Callbacks & Closures)** (Impact: 15.4)
  * `searchForContentTarget` **(Callbacks & Closures)** (Impact: 8.8)
  * `scrollToElementInContent` **(Callbacks & Closures)** (Impact: 8.2)
  * `filterButtonHandler` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 71`, `args: 49`, `func_start: 26`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `io: 4`, `api: 3`, `concurrency: 1`
* *Defense:* `safety: 31`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005747
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `retrofit/src/main/java/retrofit2/ParameterHandler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.075)
- **Top Global Matches:** file_cluster_5: 8.075, file_cluster_7: 11.284, file_cluster_14: 12.136
- **Magnitude:** 205.28 | **LOC:** 459 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 1.264; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.2%), Complexity Load (formerly Cognitive Load) (22.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Compute Cores)** (Impact: 12.1)
  * `apply` **(Compute Cores)** (Impact: 12.1)
  * `apply` **(Generic / Templated Code)** (Impact: 10.0)
  * `apply` **(Generic / Templated Code)** (Impact: 9.7)
  * `apply` **(Generic / Templated Code)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 85`, `args: 35`, `func_start: 35`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 49`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `import: 8`
* *Defense:* `safety: 8`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.095828
  * `Imports (Out-Degree: 3):` java.io.IOException, java.lang.reflect.Array, java.lang.reflect.Method, java.util.Map, java.util.Objects, javax.annotation.Nullable, okhttp3.MultipartBody, okhttp3.RequestBody
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/MaybeThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_5: 6.995, file_cluster_7: 10.27, file_cluster_12: 11.235
- **Magnitude:** 199.66 | **LOC:** 287 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (71.7%), Connectivity (formerly Api Exposure) (9.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
  * `responseThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 79`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 22`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, io.reactivex.Maybe, io.reactivex.MaybeObserver, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/MaybeThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.071)
- **Top Global Matches:** file_cluster_5: 7.071, file_cluster_7: 10.348, file_cluster_12: 11.362
- **Magnitude:** 199.22 | **LOC:** 280 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.3)
  * `responseThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 75`, `args: 28`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 22`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Maybe, io.reactivex.rxjava3.core.MaybeObserver, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava2/src/test/java/retrofit2/adapter/rxjava2/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.992)
- **Top Global Matches:** file_cluster_5: 6.992, file_cluster_7: 10.281, file_cluster_12: 11.269
- **Magnitude:** 197.4 | **LOC:** 284 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (72.2%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
  * `responseThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 78`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 21`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 16`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, io.reactivex.Single, io.reactivex.SingleObserver, io.reactivex.disposables.Disposable, io.reactivex.exceptions.CompositeException, io.reactivex.exceptions.Exceptions, io.reactivex.exceptions.UndeliverableException, io.reactivex.plugins.RxJavaPlugins...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava3/src/test/java/retrofit2/adapter/rxjava3/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.071)
- **Top Global Matches:** file_cluster_5: 7.071, file_cluster_7: 10.361, file_cluster_12: 11.399
- **Magnitude:** 196.96 | **LOC:** 277 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.6%), Connectivity (formerly Api Exposure) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.6)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.8)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.3)
  * `responseThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 74`, `args: 27`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 18`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 21`, `concurrency: 17`, `import: 19`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, io.reactivex.rxjava3.core.Single, io.reactivex.rxjava3.core.SingleObserver, io.reactivex.rxjava3.disposables.Disposable, io.reactivex.rxjava3.exceptions.CompositeException, io.reactivex.rxjava3.exceptions.Exceptions, io.reactivex.rxjava3.plugins.RxJavaPlugins, java.util.concurrent.atomic.AtomicReference...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-mock/src/test/java/retrofit2/mock/BehaviorDelegateTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.025)
- **Top Global Matches:** file_cluster_5: 7.025, file_cluster_0: 9.796, file_cluster_12: 10.282
- **Magnitude:** 190.26 | **LOC:** 338 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (49.8%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asyncCanBeCanceled` **(Annotated & Test Methods)** (Impact: 2.8)
  * `asyncCanBeCanceledBeforeStart` **(Annotated & Test Methods)** (Impact: 2.6)
  * `asyncFailureTriggersFailureAfterDelay` **(Annotated & Test Methods)** (Impact: 2.5)
  * `asyncSuccessCalledAfterDelay` **(Annotated & Test Methods)** (Impact: 2.5)
  * `asyncFailureCalledAfterDelay` **(Annotated & Test Methods)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Concurrency (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 83`, `args: 26`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `planned_debt: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 11`
* *Architecture:* `api: 24`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 10`, `test: 36`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` com.google.common.truth.Truth.assertThat, java.io.IOException, java.util.Random, java.util.concurrent.CountDownLatch, java.util.concurrent.TimeUnit, java.util.concurrent.TimeUnit.MILLISECONDS, java.util.concurrent.TimeUnit.SECONDS, java.util.concurrent.atomic.AtomicLong...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingSafeSubscriberTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.893)
- **Top Global Matches:** file_cluster_5: 6.893, file_cluster_7: 10.05, file_cluster_12: 10.376
- **Magnitude:** 186.6 | **LOC:** 344 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (63.3%), Complexity Load (formerly Cognitive Load) (41.8%), Connectivity (formerly Api Exposure) (11.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 5.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 5.8)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 5.0)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.7)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.7)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Rule, org.junit.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/ObservableThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.752)
- **Top Global Matches:** file_cluster_5: 6.752, file_cluster_7: 9.814, file_cluster_12: 10.567
- **Magnitude:** 170.62 | **LOC:** 330 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (42.9%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.8)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.9)
  * `bodyThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
  * `responseThrowingInOnCompleteDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Rule, org.junit.Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `retrofit-adapters/rxjava/src/test/java/retrofit2/adapter/rxjava/SingleThrowingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.922)
- **Top Global Matches:** file_cluster_5: 6.922, file_cluster_7: 10.055, file_cluster_12: 11.017
- **Magnitude:** 162.68 | **LOC:** 293 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.915; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (69.7%), Complexity Load (formerly Cognitive Load) (53.0%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bodyThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.8)
  * `responseThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.8)
  * `resultThrowingInOnErrorDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 4.0)
  * `bodyThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
  * `responseThrowingInOnSuccessDeliveredToPlugin` **(Annotated & Test Methods)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 86`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 12`, `duplicate_logic: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 26`, `concurrency: 17`, `import: 20`
* *Defense:* `test: 13`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` com.google.common.truth.Truth.assertThat, java.util.concurrent.atomic.AtomicReference, okhttp3.mockwebserver.MockResponse, okhttp3.mockwebserver.MockWebServer, okhttp3.mockwebserver.SocketPolicy.DISCONNECT_AFTER_REQUEST, org.junit.Before, org.junit.Ignore, org.junit.Rule...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `retrofit/kotlin-test/src/test/java/retrofit2/KotlinUnitTest.java` (JAVA) | Magnitude: 12.14 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 23, import: 9, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `retrofit-adapters/rxjava/src/main/java/retrofit2/adapter/rxjava/BodyOnSubscribe.java` (JAVA) | Magnitude: 27.52 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 22, generics: 11, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `retrofit/java-test/src/test/java/retrofit2/ResponseTest.java` (JAVA) | Magnitude: 43.5 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 175, test: 68, structural_boundaries: 32, core_var_decl: 20

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `retrofit/src/main/java/retrofit2/OkHttpCall.java` -> **Severity: 2.218** (Bridge: 0.0241 * Flux: 92.0932%)
- `retrofit/src/main/java/retrofit2/RequestFactory.java` -> **Severity: 1.922** (Bridge: 0.0216 * Flux: 89.1408%)
- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 0.181** (Bridge: 0.0155 * Flux: 11.6846%)
- `retrofit-converters/moshi/src/main/java/retrofit2/converter/moshi/MoshiConverterFactory.java` -> **Severity: 0.17** (Bridge: 0.0017 * Flux: 99.8736%)
- `retrofit/src/main/java/retrofit2/RequestBuilder.java` -> **Severity: 0.105** (Bridge: 0.001 * Flux: 99.9998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 21.333** (Embedded: 0.2735 * Error Risk: 78.0%)
- `retrofit/src/main/java/retrofit2/Converter.java` -> **Severity: 12.575** (Embedded: 0.2096 * Error Risk: 60.0%)
- `retrofit/src/main/java/retrofit2/Response.java` -> **Severity: 11.281** (Embedded: 0.179 * Error Risk: 63.0189%)
- `retrofit/src/main/java/retrofit2/Utils.java` -> **Severity: 11.075** (Embedded: 0.1426 * Error Risk: 77.6744%)
- `retrofit/src/main/java/retrofit2/OkHttpCall.java` -> **Severity: 10.772** (Embedded: 0.1626 * Error Risk: 66.2319%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `retrofit/src/main/java/retrofit2/OkHttpCall.java` -> **Severity: 4719.74** (Blast Radius: 48.295 * Doc Risk: 97.7273%)
- `retrofit/src/main/java/retrofit2/Utils.java` -> **Severity: 2051.345** (Blast Radius: 23.505 * Doc Risk: 87.2727%)
- `retrofit/src/main/java/retrofit2/Retrofit.java` -> **Severity: 1150.429** (Blast Radius: 81.968 * Doc Risk: 14.0351%)
- `retrofit/src/main/java/retrofit2/RequestFactory.java` -> **Severity: 1147.714** (Blast Radius: 12.36 * Doc Risk: 92.8571%)
- `retrofit/src/main/java/retrofit2/BuiltInConverters.java` -> **Severity: 864.9** (Blast Radius: 8.649 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 45 literal sites + 2 sites through wrappers = 47

- `callFailure` (function, debug_prints, primitive): 2 call sites in 1 files -- `retrofit/src/main/java/retrofit2/OkHttpCall.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12123 call pairs -- scoped 22.2%, unique 0.3%, ambiguous 23.2%, external 54.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 11312 | 22.3% | 0.3% | 23.3% | 54.1% |
| kotlin | 534 | 21.3% | 0.9% | 31.6% | 46.1% |
| javascript | 256 | 18.4% | 0.0% | 0.0% | 81.6% |
| groovy | 11 | 0.0% | 0.0% | 36.4% | 63.6% |
| shell | 10 | 30.0% | 0.0% | 0.0% | 70.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
