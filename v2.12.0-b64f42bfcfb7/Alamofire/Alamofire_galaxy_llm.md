# ARCHITECTURAL_BRIEF: Alamofire
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Alamofire/Alamofire` |
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
- **Scope:** 146 analyzed artifact(s), 26623 LOC.
- **Load-bearing artifact:** `Tests/TestHelpers.swift` -- 30 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `.github/workflows/ci.yml` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Tests/Resources/Certificates/selfSignedAndMalformedCerts/randomGibberish.crt` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 566 |
| Analyzed Artifacts (Scanned) | 146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 420 |
| Total LOC | 26623 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 25.8% |
| Dominant Lang | SWIFT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4795 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3413 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5545 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SWIFT | 96 | 25659 | 65.8% |
| JSON | 19 | 507 | 13.0% |
| MARKDOWN | 12 | 0 | 8.2% |
| XML | 10 | 0 | 6.8% |
| PLAINTEXT | 4 | 1 | 2.7% |
| YAML | 3 | 433 | 2.1% |
| RUBY | 2 | 23 | 1.4% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 144 |
| unknown | unknown | 1 |
| utf-32-le | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Large Core Modules (2) 16%, Large Core Modules (3) 14%, Declarative / Non-Code 9%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 130 | 89.0% |
| Unknown | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15 | 10.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 420*

**Composition by Extension & Reason:**
- `.html`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cer`: 18x Excluded (Unsupported Extension: '.cer')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.js`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.xcscheme`: 7x Excluded (Unsupported Extension: '.xcscheme')
- `.xctestplan`: 5x Excluded (Unsupported Extension: '.xctestplan')
- `.css`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbxproj`: 3x Excluded (Unsupported Extension: '.pbxproj')
- `.crt`: 2x Excluded (Unsupported Extension: '.crt')
- `.der`: 2x Excluded (Explicitly Denied Extension: '.der')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 77.0 | 15.4 | 11.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 75.0 | 29.3 | 40.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 16.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 68.8 | 3.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 26.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.7 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.2 | 21.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 203 | 47 | 5 | `Source/Features/URLEncodedFormEncoder.swift` |
| cleanup | 28 | 13 | 0 | `Source/Features/AuthenticationInterceptor.swift` |
| guards | 1856 | 79 | 40 | `Tests/SessionTests.swift` |
| danger | 167 | 36 | 4 | `Source/Features/ResponseSerialization.swift` |
| concurrency | 1758 | 67 | 43 | `Tests/ConcurrencyTests.swift` |
| connectivity | 1331 | 54 | 31 | `Source/Features/EventMonitor.swift` |
| io | 237 | 31 | 2 | `Source/Features/EventMonitor.swift` |
| crypto | 0 | 0 | 0 | - |
| ipc | 160 | 15 | 0 | `Source/Features/EventMonitor.swift` |
| time | 8 | 4 | 0 | `Tests/AuthenticationInterceptorTests.swift` |
| serialization | 31 | 11 | 0 | `Source/Core/ParameterEncoder.swift` |
| regex | 0 | 0 | 0 | - |
| events | 149 | 4 | 0 | `Tests/CombineTests.swift` |
| tests | 2473 | 33 | 61 | `Tests/ResponseSerializationTests.swift` |
| docs | 4081 | 49 | 107 | `Source/Core/Session.swift` |
| debt | 72 | 17 | 2 | `Source/Features/Concurrency.swift` |
| mutation | 6649 | 92 | 155 | `Tests/RequestTests.swift` |
| dead_code | 1101 | 77 | 20 | `Tests/ServerTrustEvaluatorTests.swift` |
| credential | 1 | 1 | 0 | `Tests/ParameterEncoderTests.swift` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 37 | 10 | 0 | `Source/Features/RetryPolicy.swift` |
| ui | 22 | 7 | 0 | `watchOS Example/watchOS Example WatchKit Extension/ContentView.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Source/Features/EventMonitor.swift` (Hits: 70)
- `Tests/MultipartFormDataTests.swift` (Hits: 34)
- `Tests/NSLoggingEventMonitor.swift` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TestHelpers.swift** (`Tests/TestHelpers.swift`) — 30 inbound connections
2. **RequestInterceptorTests.swift** (`Tests/RequestInterceptorTests.swift`) — 13 inbound connections
3. **EventMonitor.swift** (`Source/Features/EventMonitor.swift`) — 8 inbound connections
4. **ResponseSerialization.swift** (`Source/Features/ResponseSerialization.swift`) — 8 inbound connections
5. **URLConvertible+URLRequestConvertible.swift** (`Source/Core/URLConvertible+URLRequestConvertible.swift`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ci.yml** (`.github/workflows/ci.yml`) — 5 outbound dependencies
2. **MultipartFormData.swift** (`Source/Features/MultipartFormData.swift`) — 4 outbound dependencies
3. **RequestTests.swift** (`Tests/RequestTests.swift`) — 4 outbound dependencies
4. **Alamofire.swift** (`Source/Alamofire.swift`) — 3 outbound dependencies
5. **Combine.swift** (`Source/Features/Combine.swift`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `encode` **(Many-Argument Workhorses)** (@ `Source/Core/ParameterEncoding.swift`) -> Impact: **91.4** | LOC: 200
  * *Intent:* /// Creates a `URLRequest` by encoding parameters and applying them on the passed request. /// /// - Parameters: /// - urlRequest: `URLRequestConverti...
- `set` **(Defensive Guards)** (@ `Source/Features/URLEncodedFormEncoder.swift`) -> Impact: **50.5** | LOC: 51
  * *Intent:* /// Recursive backing method to `set(to:at:)`.
- `init` **(Many-Argument Workhorses)** (@ `Source/Core/Session.swift`) -> Impact: **34.0** | LOC: 32
  * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on which to perform all response serialization. By defa...
- `urlSession` **(Many-Argument Workhorses)** (@ `Source/Core/SessionDelegate.swift`) -> Impact: **32.7** | LOC: 27
- `init` **(Many-Argument Workhorses)** (@ `Source/Core/Session.swift`) -> Impact: **30.5** | LOC: 33
  * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on which to perform all response serialization. By defa...
- `prepare` **(Defensive Guards)** (@ `Example/Source/MasterViewController.swift`) -> Impact: **29.4** | LOC: 33
  * *Intent:* // MARK: - UIStoryboardSegue
- `serialize` **(Defensive Guards)** (@ `Source/Features/ResponseSerialization.swift`) -> Impact: **28.2** | LOC: 27
- `testThatDataStreamWorksCorrectlyWithMultipleSerialQueues` **(I/O & Config Routines)** (@ `Tests/DataStreamTests.swift`) -> Impact: **27.9** | LOC: 79
- `testThatWebSocketsCanHaveMultipleHandlers` **(I/O & Config Routines)** (@ `Tests/WebSocketTests.swift`) -> Impact: **27.8** | LOC: 75
- `urlSession` **(Defensive Guards)** (@ `Source/Core/SessionDelegate.swift`) -> Impact: **27.6** | LOC: 13

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Tests` | 44 | 9109.5 | 17.34% | 0.0% |
| `Tests/Resources/Certificates/selfSignedAndMalformedCerts` | 1 | 5000.0 | 0.0% | 0.0% |
| `Source/Core` | 18 | 3797.7 | 24.97% | 50.75% |
| `Source/Features` | 18 | 3591.36 | 26.46% | 41.69% |
| `Example/Source` | 3 | 204.42 | 45.13% | 0.0% |
| `__monolith__` | 8 | 161.28 | 6.5% | 0.0% |
| `Source/Extensions` | 6 | 126.46 | 15.16% | 41.35% |
| `Documentation` | 6 | 80.48 | 0.0% | 0.0% |
| `watchOS Example/watchOS Example WatchKit Extension` | 5 | 66.08 | 4.89% | 23.9% |
| `.github/workflows` | 1 | 64.42 | 3.91% | 46.89% |

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
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `168` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Tests/Resources/Certificates/selfSignedAndMalformedCerts/randomGibberish.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/DataStreamTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.867)
- **Top Global Matches:** file_cluster_6: 10.867, file_cluster_4: 11.366, file_cluster_9: 14.73
- **Magnitude:** 843.6 | **LOC:** 1320 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (39.9%), Concurrency Surface (formerly Concurrency) (16.3%), Dead Code Surface (formerly Dead Code) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatDataStreamWorksCorrectlyWithMultipleSerialQueues` **(I/O & Config Routines)** (Impact: 27.9)
  * `testThatDataStreamWorksCorrectlyWithMultipleConcurrentQueues` **(I/O & Config Routines)** (Impact: 26.6)
  * `testThatDataCanBeStreamedAndDecodedAtTheSameTime` **(I/O & Config Routines)** (Impact: 24.7)
  * `testThatDataCanBeStreamedManyTimes` **(I/O & Config Routines)** (Impact: 21.6)
  * `testThatDataStreamsCanBeRetried` **(Annotated & Test Methods)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 116 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 172`, `args: 86`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`, `unreferenced_by_name: 31`
* *Architecture:* `concurrency: 37`, `import: 2`
* *Defense:* `safety: 42`, `test: 127`, `sync_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Alamofire, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/SessionTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.173)
- **Top Global Matches:** file_cluster_9: 9.173, file_cluster_0: 9.884, file_cluster_10: 9.908
- **Magnitude:** 825.0 | **LOC:** 2017 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `retry` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `executeAuthorizationHeaderTest` **(Stateful Encapsulated Methods)** (Impact: 19.1)
  * `testThatSessionCallsRequestRetrierForAllResponseSerializersThatThrowError` **(I/O & Config Routines)** (Impact: 16.7)
  * `testThatDownloadRequestWithInvalidURLStringThrowsResponseHandlerError` **(Annotated & Test Methods)** (Impact: 14.3)
  * `testThatRetriedRequestsCanBeMassCancelled` **(Annotated & Test Methods)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 215`, `args: 144`, `func_start: 65`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `unreferenced_by_name: 52`
* *Architecture:* `io: 4`, `concurrency: 58`, `import: 2`
* *Defense:* `safety: 102`, `test: 276`, `sync_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Core/Session.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.648)
- **Top Global Matches:** file_cluster_0: 7.648, file_cluster_15: 9.273, file_cluster_9: 10.14
- **Magnitude:** 767.12 | **LOC:** 1458 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Debt Markers (formerly Tech Debt) (48.3%), Mutation Surface (formerly State Flux) (45.8%), Guard Balance (formerly Safety Score) (42.5%)
- **Documentation Coverage:** 44.3182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on wh...
  * `init` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /// careful testing and profiling. `nil` by default. /// - serializationQueue: `DispatchQueue` on wh...
  * `download` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* /// - method: `HTTPMethod` for the `URLRequest`. `.get` by default. /// - parameters: `Parameters` (...
  * `download` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* /// - convertible: `URLConvertible` value to be used as the `URLRequest`'s `URL`. /// - method: `HTT...
  * `performSetupOperations` **(Defensive Guards)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 220`, `args: 63`, `func_start: 57`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 21`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 15`, `api: 50`, `concurrency: 50`, `import: 1`
* *Defense:* `safety: 33`, `doc: 479`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/RequestTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.488)
- **Top Global Matches:** file_cluster_10: 7.488, file_cluster_13: 8.516, file_cluster_12: 9.614
- **Magnitude:** 755.6 | **LOC:** 1888 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (83.3%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (30.6%), Dead Code Surface (formerly Dead Code) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testRequestResponseWithProgress` **(Annotated & Test Methods)** (Impact: 13.1)
  * `testPOSTRequestWithJSONParametersCURLDescription` **(I/O & Config Routines)** (Impact: 12.7)
  * `testThatDataRequestOnHTTPResponseCanCancel` **(Annotated & Test Methods)** (Impact: 12.6)
  * `testPOSTRequestWithBase64EncodedImages` **(Annotated & Test Methods)** (Impact: 12.4)
  * `testThatDataRequestOnHTTPResponseCanAllow` **(Annotated & Test Methods)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 179`, `args: 209`, `func_start: 67`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 175`, `dead_code: 1`, `unreferenced_by_name: 65`
* *Architecture:* `io: 2`, `concurrency: 112`, `import: 4`
* *Defense:* `safety: 72`, `test: 191`, `sync_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Alamofire, Foundation, Testing, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Features/EventMonitor.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.536)
- **Top Global Matches:** file_cluster_0: 8.536, file_cluster_15: 9.505, file_cluster_13: 10.877
- **Magnitude:** 664.66 | **LOC:** 920 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **1**; blast radius 11.863; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.3%), Connectivity (formerly Api Exposure) (15.2%)
- **Documentation Coverage:** 96.9582% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Generic / Templated Code)** (Impact: 23.6)
    * *Intent:* /// Event called when a `DownloadRequest` calls a `DownloadResponseSerializer` and creates a generic...
  * `request` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `request` **(Compute Cores)** (Impact: 10.1)
  * `request` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `request` **(Many-Argument Workhorses)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 239`, `args: 177`, `func_start: 176`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 70`, `api: 178`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 18`, `doc: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055862
  * `Imports (Out-Degree: 0):` Foundation
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Source/Core/Request.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.784)
- **Top Global Matches:** file_cluster_15: 8.784, file_cluster_0: 9.11, file_cluster_10: 9.283
- **Magnitude:** 625.92 | **LOC:** 1249 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.54; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (75.3%), Guard Balance (formerly Safety Score) (49.5%)
- **Documentation Coverage:** 5.6338% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cURLDescription` **(Defensive Guards)** (Impact: 26.4)
    * *Intent:* /// cURL representation of the instance. /// /// - Returns: The cURL equivalent of the instance.
  * `init` **(Generic / Templated Code)** (Impact: 12.1)
    * *Intent:* /// Default initializer for the `Request` superclass. /// /// - Parameters: /// - id: `UUID` used fo...
  * `retryOrFinish` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* /// Called to determine whether retry will be triggered for the particular error, or whether the ins...
  * `appendResponseSerializer` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* /// Appends the response serialization closure to the instance. /// /// - Note: This method will als...
  * `canTransitionTo` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /// Determines whether `self` can be transitioned to the provided `State`.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 125
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 186`, `args: 78`, `func_start: 54`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 72`, `unreferenced_by_name: 23`
* *Architecture:* `io: 2`, `api: 62`, `concurrency: 50`, `import: 1`
* *Defense:* `safety: 58`, `doc: 330`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.54
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.006897
  * `Imports (Out-Degree: 4):` Foundation
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/Features/URLEncodedFormEncoder.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.553)
- **Top Global Matches:** file_cluster_0: 7.553, file_cluster_15: 8.655, file_cluster_16: 9.165
- **Magnitude:** 559.02 | **LOC:** 1142 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 7.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.0%), Guard Balance (formerly Safety Score) (53.4%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Defensive Guards)** (Impact: 50.5)
    * *Intent:* /// Recursive backing method to `set(to:at:)`.
  * `convert` **(Stateful Encapsulated Methods)** (Impact: 14.7)
  * `encode` **(Type Conversions)** (Impact: 13.5)
    * *Intent:* /// Encodes the date according to the encoding. /// /// - Parameter date: The `Date` to encode. /// ...
  * `encode` **(Compute Cores)** (Impact: 13.3)
  * `encode` **(Type Conversions)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 299`, `args: 92`, `func_start: 85`, `class_start: 26`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 80`, `duplicate_logic: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 31`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 22`, `doc: 194`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.894
  * `Choke Point (Betweenness):` 0.000144 | `Ripple Effect (Closeness):` 0.013793
  * `Imports (Out-Degree: 2):` Foundation
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Tests/CombineTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.0)
- **Top Global Matches:** file_cluster_10: 9.0, file_cluster_13: 9.007, file_cluster_0: 9.143
- **Magnitude:** 540.0 | **LOC:** 1475 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.5%), Concurrency Surface (formerly Concurrency) (21.3%), Complexity Load (formerly Cognitive Load) (20.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatDataStreamRequestCanBePublishedWithMultipleHandlers` **(Callbacks & Closures)** (Impact: 12.9)
  * `testThatDataRequestCanPublishValueWithFailure` **(Annotated & Test Methods)** (Impact: 9.4)
  * `testThatDataStreamRequestCanPublishValueWithFailure` **(Annotated & Test Methods)** (Impact: 9.4)
  * `testThatDownloadRequestCanPublishValueWithFailure` **(Annotated & Test Methods)** (Impact: 9.4)
  * `testThatMultipleDataRequestPublishersCanBeChained` **(Annotated & Test Methods)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 137`, `args: 130`, `func_start: 53`, `class_start: 4`
* *Risk/State:* `state_mutation: 74`, `unreferenced_by_name: 52`
* *Architecture:* `concurrency: 47`, `import: 3`
* *Defense:* `safety: 65`, `test: 96`, `sync_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Alamofire, Combine, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/DownloadTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.16)
- **Top Global Matches:** file_cluster_9: 9.16, file_cluster_12: 12.52, file_cluster_10: 12.662
- **Magnitude:** 505.86 | **LOC:** 1053 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.8%), Complexity Load (formerly Cognitive Load) (28.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatCancelledDownloadCanBeResumedWithResumeData` **(Annotated & Test Methods)** (Impact: 18.0)
  * `testDownloadRequestWithParameters` **(Defensive Guards)** (Impact: 15.8)
  * `testThatCancelledDownloadProducesMatchingResumeData` **(Annotated & Test Methods)** (Impact: 14.9)
  * `testDownloadRequest` **(Defensive Guards)** (Impact: 14.8)
  * `testDownloadRequestWithProgress` **(Annotated & Test Methods)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 110`, `args: 109`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 63`, `unreferenced_by_name: 30`
* *Architecture:* `io: 8`, `concurrency: 29`, `import: 3`
* *Defense:* `safety: 55`, `test: 190`, `sync_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Alamofire, Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/ConcurrencyTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.441)
- **Top Global Matches:** file_cluster_11: 8.441, file_cluster_10: 8.529, file_cluster_13: 8.924
- **Magnitude:** 494.14 | **LOC:** 876 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (43.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatDelayedUploadStreamResultsInMultipleProgressValues` **(I/O & Config Routines)** (Impact: 23.2)
  * `testThatDataOnHTTPResponseCanCancel` **(Annotated & Test Methods)** (Impact: 10.7)
  * `sendData` **(Defensive Guards)** (Impact: 10.0)
  * `testThatDataStreamTaskCanBeCancelledAfterStreamTurnsOffAutomaticCancellation` **(I/O & Config Routines)** (Impact: 6.5)
  * `testThatDataStreamTaskIsCancelledByCancellingIteration` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 294
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 180`, `args: 57`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `state_mutation: 18`, `duplicate_logic: 3`, `unreferenced_by_name: 41`
* *Architecture:* `concurrency: 164`, `import: 2`
* *Defense:* `safety: 17`, `test: 80`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Alamofire, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/WebSocketTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.222)
- **Top Global Matches:** file_cluster_4: 9.222, file_cluster_6: 10.017, file_cluster_9: 12.941
- **Magnitude:** 459.2 | **LOC:** 741 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.1%), Complexity Load (formerly Cognitive Load) (36.9%), Concurrency Surface (formerly Concurrency) (14.9%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatWebSocketsCanHaveMultipleHandlers` **(I/O & Config Routines)** (Impact: 27.8)
  * `testOnePingOnly` **(I/O & Config Routines)** (Impact: 23.4)
  * `testThatWebSocketsCanReceiveADecodableMessage` **(I/O & Config Routines)** (Impact: 16.3)
  * `testThatWebSocketsCanSendAndReceiveMessages` **(I/O & Config Routines)** (Impact: 15.5)
  * `testThatWebSocketsCanReceiveMessageEvents` **(I/O & Config Routines)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 134`, `args: 37`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 72`, `unreferenced_by_name: 15`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 1`, `test: 73`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/MultipartFormDataTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.737)
- **Top Global Matches:** file_cluster_15: 6.737, file_cluster_2: 7.839, file_cluster_0: 8.021
- **Magnitude:** 452.16 | **LOC:** 968 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.2%), Complexity Load (formerly Cognitive Load) (31.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `boundary` **(Compute Cores)** (Impact: 9.2)
  * `testThatStreamBodyPartHasUnexpectedLength` **(Defensive Guards)** (Impact: 8.3)
  * `testWritingMultipleEncodedBodyPartsWithVaryingTypesToDisk` **(I/O & Config Routines)** (Impact: 8.1)
  * `testWritingMultipleEncodedStreamBodyPartsToDisk` **(I/O & Config Routines)** (Impact: 8.0)
  * `testWritingMultipleEncodedDataBodyPartsToDisk` **(I/O & Config Routines)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 169`, `args: 26`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `state_mutation: 179`, `unreferenced_by_name: 24`
* *Architecture:* `io: 34`, `import: 3`
* *Defense:* `safety: 49`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Alamofire, Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Core/WebSocketRequest.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.851)
- **Top Global Matches:** file_cluster_0: 7.851, file_cluster_12: 8.975, file_cluster_5: 9.466
- **Magnitude:** 376.62 | **LOC:** 571 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 8.452; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `streamSerializer` **(Generic / Templated Code)** (Impact: 13.4)
  * `close` **(Defensive Guards)** (Impact: 11.6)
  * `streamMessageEvents` **(Generic / Templated Code)** (Impact: 11.4)
  * `sendPing` **(Defensive Guards)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 132`, `args: 64`, `func_start: 32`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 25`, `planned_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 41`, `concurrency: 47`, `import: 1`
* *Defense:* `safety: 38`, `doc: 13`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.452
  * `Choke Point (Betweenness):` 0.000287 | `Ripple Effect (Closeness):` 0.006897
  * `Imports (Out-Degree: 3):` Foundation
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/Features/Concurrency.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.51)
- **Top Global Matches:** file_cluster_5: 8.51, file_cluster_0: 8.762, file_cluster_12: 10.581
- **Magnitude:** 376.04 | **LOC:** 963 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (44.8%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 24.7706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStream` **(Stateful Encapsulated Methods)** (Impact: 19.0)
  * `createStream` **(Stateful Encapsulated Methods)** (Impact: 12.9)
  * `serializingString` **(Generic / Templated Code)** (Impact: 5.4)
    * *Intent:* /// /// - Parameters: /// - shouldAutomaticallyCancel: `Bool` determining whether or not the request...
  * `serializingString` **(Generic / Templated Code)** (Impact: 5.4)
    * *Intent:* /// /// - Parameters: /// - shouldAutomaticallyCancel: `Bool` determining whether or not the request...
  * `makeAsyncIterator` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 147`, `args: 100`, `func_start: 61`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 15`, `duplicate_logic: 14`, `unreferenced_by_name: 19`
* *Architecture:* `api: 64`, `concurrency: 98`, `import: 1`
* *Defense:* `safety: 25`, `doc: 278`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/UploadTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.852)
- **Top Global Matches:** file_cluster_10: 9.852, file_cluster_9: 10.098, file_cluster_4: 10.47
- **Magnitude:** 371.92 | **LOC:** 897 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.3%), Complexity Load (formerly Cognitive Load) (24.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeMultipartFormDataUploadRequestWithProgress` **(Defensive Guards)** (Impact: 26.0)
    * *Intent:* #endif // MARK: Combined Test Execution
  * `testUploadDataRequestWithProgress` **(I/O & Config Routines)** (Impact: 18.1)
  * `testThatAccessingMultipartFormDataURLIsThreadSafe` **(I/O & Config Routines)** (Impact: 15.2)
  * `testThatUploadingMultipartFormDataSetsContentTypeHeader` **(Annotated & Test Methods)** (Impact: 12.9)
  * `testThatUploadingMultipartFormDataWorksWhenAppendingBodyPartsInURLRequestConvertible` **(Annotated & Test Methods)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 78`, `args: 88`, `func_start: 27`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 73`, `unreferenced_by_name: 25`
* *Architecture:* `io: 1`, `concurrency: 25`, `import: 3`
* *Defense:* `safety: 55`, `test: 90`, `sync_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Alamofire, Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/ResponseTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.294)
- **Top Global Matches:** file_cluster_9: 9.294, file_cluster_0: 13.583, file_cluster_10: 13.776
- **Magnitude:** 341.16 | **LOC:** 676 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (34.9%), Complexity Load (formerly Cognitive Load) (32.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatResponseJSONReturnsSuccessResultForGETRequest` **(Defensive Guards)** (Impact: 14.6)
  * `testThatResponseJSONReturnsSuccessResultForPOSTRequest` **(Defensive Guards)** (Impact: 14.6)
  * `testThatTryMapCatchesTransformationError` **(Defensive Guards)** (Impact: 11.7)
  * `testThatTryMapErrorCatchesTransformationError` **(Defensive Guards)** (Impact: 11.5)
  * `testThatMapErrorTransformsFailureValue` **(Annotated & Test Methods)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 71`, `args: 53`, `func_start: 24`, `class_start: 12`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 20`
* *Architecture:* `concurrency: 23`, `import: 3`
* *Defense:* `safety: 38`, `test: 136`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Alamofire, Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Core/SessionDelegate.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.148)
- **Top Global Matches:** file_cluster_9: 8.148, file_cluster_15: 9.695, file_cluster_0: 10.102
- **Magnitude:** 325.62 | **LOC:** 388 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 5.831; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.6%), Mutation Surface (formerly State Flux) (39.9%), Debt Markers (formerly Tech Debt) (31.5%), Concurrency Surface (formerly Concurrency) (23.9%)
- **Documentation Coverage:** 81.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `urlSession` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `urlSession` **(Defensive Guards)** (Impact: 27.6)
  * `urlSession` **(Defensive Guards)** (Impact: 23.3)
  * `urlSession` **(Defensive Guards)** (Impact: 23.0)
  * `urlSession` **(Defensive Guards)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 74`, `args: 25`, `func_start: 25`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 5`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 21`, `api: 18`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 28`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.831
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013793
  * `Imports (Out-Degree: 0):` Foundation
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Tests/ResponseSerializationTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.786)
- **Top Global Matches:** file_cluster_13: 7.786, file_cluster_11: 7.896, file_cluster_0: 8.094
- **Magnitude:** 320.46 | **LOC:** 1412 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (25.6%), Complexity Load (formerly Cognitive Load) (4.4%), Connectivity (formerly Api Exposure) (0.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Compute Cores)** (Impact: 13.6)
  * `testThatCustomResponseSerializersCanBeWrittenWithoutCompilerIssues` **(Annotated & Test Methods)** (Impact: 8.2)
  * `testThatJSONResponseSerializerFailsWhenDataIsInvalidJSON` **(Annotated & Test Methods)** (Impact: 7.8)
  * `testThatJSONResponseSerializerFailsWhenDataIsInvalidJSON` **(Annotated & Test Methods)** (Impact: 7.8)
  * `testThatStringResponseSerializerFailsWithUTF32DataAndUTF8ProvidedEncoding` **(I/O & Config Routines)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 215`, `args: 103`, `func_start: 101`, `class_start: 16`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 68`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 90`, `test: 289`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Alamofire, Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Features/ResponseSerialization.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.613)
- **Top Global Matches:** file_cluster_0: 7.613, file_cluster_15: 10.615, file_cluster_11: 11.179
- **Magnitude:** 314.48 | **LOC:** 533 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **1**; blast radius 17.773; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.4%), Debt Markers (formerly Tech Debt) (68.6%), Concurrency Surface (formerly Concurrency) (63.1%), Guard Balance (formerly Safety Score) (40.1%)
- **Documentation Coverage:** 15.6863% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Defensive Guards)** (Impact: 28.2)
  * `serialize` **(Defensive Guards)** (Impact: 25.7)
  * `serialize` **(Defensive Guards)** (Impact: 21.1)
    * *Intent:* /// Serialize the response `Data` into the provided type. /// /// - Parameters: /// - request: `URLR...
  * `serialize` **(Defensive Guards)** (Impact: 18.8)
  * `serialize` **(Defensive Guards)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 135`, `args: 27`, `func_start: 27`, `class_start: 25`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 63`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 25`, `doc: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.773
  * `Choke Point (Betweenness):` 0.000335 | `Ripple Effect (Closeness):` 0.055862
  * `Imports (Out-Degree: 1):` Foundation
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Tests/AuthenticationInterceptorTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.091)
- **Top Global Matches:** file_cluster_6: 9.091, file_cluster_4: 13.772, file_cluster_8: 15.015
- **Magnitude:** 312.2 | **LOC:** 710 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.3%), Complexity Load (formerly Cognitive Load) (24.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatInterceptorThrowsMissingCredentialErrorWhenCredentialIsNilAndRequestShouldBeRetried` **(I/O & Config Routines)** (Impact: 20.1)
  * `testThatInterceptorThrowsExcessiveRefreshErrorWhenExcessiveRefreshOccurs` **(I/O & Config Routines)** (Impact: 20.1)
  * `testThatInterceptorRethrowsRefreshErrorFromAdapt` **(I/O & Config Routines)** (Impact: 19.9)
  * `testThatInterceptorRethrowsRefreshErrorFromRetry` **(I/O & Config Routines)** (Impact: 19.9)
  * `testThatInterceptorThrowsMissingCredentialErrorWhenCredentialIsNil` **(Annotated & Test Methods)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 65`, `args: 24`, `func_start: 22`, `class_start: 5`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 19`
* *Architecture:* `concurrency: 15`, `import: 2`
* *Defense:* `safety: 24`, `test: 123`, `sync_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Features/MultipartFormData.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.383)
- **Top Global Matches:** file_cluster_16: 5.383, file_cluster_15: 6.563, file_cluster_11: 8.765
- **Magnitude:** 275.16 | **LOC:** 586 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 7.967; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (51.0%), Complexity Load (formerly Cognitive Load) (20.5%), Debt Markers (formerly Tech Debt) (10.2%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /// Creates a body part from the file and appends it to the instance. /// /// The body part data wil...
  * `writeBodyStream` **(Stateful Encapsulated Methods)** (Impact: 17.0)
  * `writeEncodedData` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* /// Writes all appended body parts to the given file `URL`. /// /// This process is facilitated by r...
  * `encodeBodyStream` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `mimeType` **(Stateful Encapsulated Methods)** (Impact: 12.0)
    * *Intent:* // MARK: - Private - Mime Type
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 110`, `args: 30`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 13`, `import: 4`
* *Defense:* `safety: 17`, `doc: 107`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.967
  * `Choke Point (Betweenness):` 0.000239 | `Ripple Effect (Closeness):` 0.02069
  * `Imports (Out-Degree: 2):` CoreServices, Foundation, MobileCoreServices, UniformTypeIdentifiers
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Tests/ValidationTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.006)
- **Top Global Matches:** file_cluster_10: 8.006, file_cluster_13: 8.934, file_cluster_9: 9.046
- **Magnitude:** 274.88 | **LOC:** 878 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.9%), Complexity Load (formerly Cognitive Load) (15.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatCustomValidationCanThrowCustomError` **(Callbacks & Closures)** (Impact: 10.7)
  * `testThatValidationExtensionCanThrowCustomError` **(Defensive Guards)** (Impact: 10.7)
  * `testThatContentTypeValidationFailureSortsPossibleContentTypes` **(I/O & Config Routines)** (Impact: 10.6)
  * `testThatValidationForRequestWithUnacceptableStatusCodeAndContentTypeResponseFailsWithContentTypeError` **(Annotated & Test Methods)** (Impact: 10.0)
  * `testThatValidationForRequestWithUnacceptableContentTypeResponseFails` **(Annotated & Test Methods)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 137`, `args: 77`, `func_start: 25`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `duplicate_logic: 2`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `concurrency: 21`, `import: 2`
* *Defense:* `safety: 29`, `test: 66`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Foundation, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Source/Core/ParameterEncoding.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.773)
- **Top Global Matches:** file_cluster_4: 6.773, file_cluster_6: 11.058, file_cluster_9: 11.283
- **Magnitude:** 264.4 | **LOC:** 350 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.863; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (59.9%), Guard Balance (formerly Safety Score) (47.6%), Complexity Load (formerly Cognitive Load) (31.6%)
- **Documentation Coverage:** 21.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode` **(Many-Argument Workhorses)** (Impact: 91.4)
    * *Intent:* /// Creates a `URLRequest` by encoding parameters and applying them on the passed request. /// /// -...
  * `queryComponents` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* /// Creates a percent-escaped, URL encoded query string components from the given key-value pair rec...
  * `encode` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* // MARK: Encoding
  * `encode` **(Compute Cores)** (Impact: 11.0)
    * *Intent:* /// Provide a custom array key encoding with the given closure.
  * `encode` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* // MARK: Encoding
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 60`, `args: 12`, `func_start: 12`, `class_start: 9`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 25`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 17`, `doc: 82`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.863
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006897
  * `Imports (Out-Degree: 2):` Foundation
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Source/Core/DataStreamRequest.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.153)
- **Top Global Matches:** file_cluster_0: 8.153, file_cluster_5: 8.596, file_cluster_12: 9.255
- **Magnitude:** 255.74 | **LOC:** 594 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 6.51; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (83.1%), Mutation Surface (formerly State Flux) (72.9%), Guard Balance (formerly Safety Score) (41.1%)
- **Documentation Coverage:** 22.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 13.6)
    * *Intent:* /// by default. /// - convertible: `URLRequestConvertible` value used to create `URLRequest`s for th...
  * `didReceiveResponse` **(Defensive Guards)** (Impact: 8.1)
  * `validate` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* /// Validates the `URLRequest` and `HTTPURLResponse` received for the instance using the provided `V...
  * `responseStream` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* /// Adds a `StreamHandler` which uses the provided `DataStreamSerializer` to process incoming `Data`...
  * `asInputStream` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* #if !canImport(FoundationNetworking) // If we not using swift-corelibs-foundation. /// Produces an `...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 120`, `args: 45`, `func_start: 28`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`, `duplicate_logic: 2`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 43`, `concurrency: 56`, `import: 1`
* *Defense:* `safety: 39`, `doc: 141`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.51
  * `Choke Point (Betweenness):` 0.000192 | `Ripple Effect (Closeness):` 0.006897
  * `Imports (Out-Degree: 3):` Foundation
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Source/Features/AuthenticationInterceptor.swift` (SWIFT) | Magnitude: 160.78 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 155, doc: 131, structural_boundaries: 56, branch: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Tests/CombineTests.swift` (SWIFT) | Magnitude: 540.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1052, core_var_decl: 222, branch: 185, design_camel_case: 140
- `Source/Features/NetworkReachabilityManager.swift` (SWIFT) | Magnitude: 106.64 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 144, doc: 58, structural_boundaries: 52, branch: 44
- `Tests/RequestInterceptorTests.swift` (SWIFT) | Magnitude: 230.02 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 453, core_var_decl: 135, structural_boundaries: 123, design_snake_case: 101

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Tests/ConcurrencyTests.swift` (SWIFT) | Magnitude: 494.14 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 522, structural_boundaries: 180, concurrency: 164, core_var_decl: 144
- `Source/Core/URLConvertible+URLRequestConvertible.swift` (SWIFT) | Magnitude: 35.82 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 30, doc: 29, indent_spaces: 19, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Source/Alamofire.swift` (SWIFT) | Magnitude: 19.24 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, api: 4, doc: 3, import: 3
- `Tests/ResponseSerializationTests.swift` (SWIFT) | Magnitude: 320.46 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 813, test: 289, core_var_decl: 254, design_snake_case: 248

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Example/Source/AppDelegate.swift` (SWIFT) | Magnitude: 13.98 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, branch: 5, explicit_casts: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Source/Core/AFError.swift` -> **Jon Shier** (100.0% isolated ownership) | Magnitude: 86.26
- `.github/workflows/ci.yml` -> **Jon Shier** (100.0% isolated ownership) | Magnitude: 64.42

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Source/Features/ResponseSerialization.swift` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 85.4443%)
- `Source/Core/WebSocketRequest.swift` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 97.595%)
- `Source/Features/MultipartFormData.swift` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 99.6023%)
- `Source/Core/Request.swift` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9716%)
- `Source/Core/DataStreamRequest.swift` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 72.9446%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Tests/TestHelpers.swift` -> **Severity: 12.079** (Embedded: 0.2302 * Error Risk: 52.4699%)
- `Source/Core/URLConvertible+URLRequestConvertible.swift` -> **Severity: 6.345** (Embedded: 0.1474 * Error Risk: 43.0454%)
- `Tests/RequestInterceptorTests.swift` -> **Severity: 3.753** (Embedded: 0.0949 * Error Risk: 39.5439%)
- `Source/Features/EventMonitor.swift` -> **Severity: 2.528** (Embedded: 0.0559 * Error Risk: 45.2588%)
- `Source/Features/RetryPolicy.swift` -> **Severity: 2.399** (Embedded: 0.0604 * Error Risk: 39.723%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Tests/TestHelpers.swift` -> **Severity: 10274.3** (Blast Radius: 102.743 * Doc Risk: 100.0%)
- `Tests/RequestInterceptorTests.swift` -> **Severity: 2944.079** (Blast Radius: 30.779 * Doc Risk: 95.6522%)
- `Source/Features/EventMonitor.swift` -> **Severity: 1150.215** (Blast Radius: 11.863 * Doc Risk: 96.9582%)
- `Tests/FileManager+AlamofireTests.swift` -> **Severity: 942.3** (Blast Radius: 9.423 * Doc Risk: 100.0%)
- `Source/Core/WebSocketRequest.swift` -> **Severity: 845.2** (Blast Radius: 8.452 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 8 literal sites + 1 sites through wrappers = 9

- `monitorReachability` (function, debug_prints, primitive): 1 call sites in 1 files -- `Example/Source/MasterViewController.swift`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7503 call pairs -- scoped 12.0%, unique 9.0%, ambiguous 32.2%, external 46.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| swift | 7481 | 12.0% | 9.0% | 32.3% | 46.7% |
| ruby | 22 | 0.0% | 0.0% | 0.0% | 100.0% |

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
