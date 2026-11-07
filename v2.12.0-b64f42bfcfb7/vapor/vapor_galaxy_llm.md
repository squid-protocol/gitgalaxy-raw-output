# ARCHITECTURAL_BRIEF: vapor
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vapor/vapor` |
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
- **Scope:** 319 analyzed artifact(s), 29060 LOC.
- **Load-bearing artifact:** `Sources/Vapor/Application.swift` -- 35 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Tests/VaporTests/ServerTests.swift` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Tests/VaporTests/Utilities/expired.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 328 |
| Analyzed Artifacts (Scanned) | 319 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 29060 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 97.3% |
| Dominant Lang | SWIFT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6469 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.112 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7266 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SWIFT | 293 | 28130 | 91.8% |
| MARKDOWN | 7 | 0 | 2.2% |
| PLAINTEXT | 5 | 3 | 1.6% |
| YAML | 4 | 143 | 1.3% |
| C | 4 | 781 | 1.3% |
| XML | 3 | 0 | 0.9% |
| HTML | 3 | 3 | 0.9% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 318 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 16%, Parameter Forwarders Files 15%, Large Core Modules (2) 15%, Data / Markup / Trivial 13%, Large Core Modules (3) 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 307 | 96.2% |
| Unknown | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.modulemap`: 1x Excluded (Unsupported Extension: '.modulemap')
- `.swift`: 1x Excluded (Saturation: Line 67 exceeds 500 chars)
- `.crt`: 1x Excluded (Unsupported Extension: '.crt')
- `.txt`: 1x Excluded (Embedded Array/Matrix Payload: 1838 commas in 600 LOC)
- `.env`: 1x Excluded (Unsupported Extension: '.env')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 19.1 | 10.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.7 | 32.0 | 45.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 74.4 | 6.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 42.3 | 27.7 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 83.6 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.3 | 66.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 247 | 75 | 2 | `Tests/VaporTests/BaseNTests.swift` |
| cleanup | 156 | 35 | 1 | `Tests/VaporTests/RouteTests.swift` |
| guards | 1906 | 241 | 13 | `Tests/VaporTests/ValidationTests.swift` |
| danger | 267 | 81 | 3 | `Sources/Vapor/URLEncodedForm/URLEncodedFormDecoder.swift` |
| concurrency | 1935 | 184 | 14 | `Tests/VaporTests/ConditionalResponseCompressionTests.swift` |
| connectivity | 2666 | 283 | 19 | `Sources/Vapor/HTTP/Headers/HTTPHeaders+Name.swift` |
| io | 9 | 3 | 0 | `Tests/VaporTests/FileTests.swift` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `Sources/Vapor/Environment/Environment.swift` |
| time | 34 | 9 | 0 | `Tests/VaporTests/HTTPCacheTests.swift` |
| serialization | 46 | 12 | 0 | `Sources/Vapor/Content/JSONCoder+Custom.swift` |
| regex | 1 | 1 | 0 | `Sources/Vapor/Validation/Validators/Pattern.swift` |
| events | 339 | 40 | 2 | `Sources/Vapor/Application.swift` |
| tests | 1952 | 57 | 12 | `Tests/VaporTests/URLEncodedFormTests.swift` |
| docs | 3687 | 175 | 35 | `Sources/Vapor/HTTP/Headers/HTTPHeaders+Name.swift` |
| debt | 105 | 29 | 0 | `Tests/VaporTests/ApplicationTests.swift` |
| mutation | 5422 | 251 | 44 | `Tests/VaporTests/ServerTests.swift` |
| dead_code | 859 | 190 | 7 | `Tests/VaporTests/URLEncodedFormTests.swift` |
| credential | 12 | 6 | 0 | `Tests/VaporTests/ValidationTests.swift` |
| threat | 8 | 2 | 0 | `Tests/VaporTests/BaseNTests.swift` |
| ml_ai | 34 | 11 | 0 | `Sources/Vapor/URLEncodedForm/URLQueryFragmentConvertible.swift` |
| ui | 28 | 16 | 0 | `Sources/Vapor/Response/Response.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Tests/VaporTests/FileTests.swift` (Hits: 7)
- `Sources/Vapor/Utilities/FileIO.swift` (Hits: 1)
- `Tests/VaporTests/AsyncFileTests.swift` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Application.swift** (`Sources/Vapor/Application.swift`) — 35 inbound connections
2. **Abort.swift** (`Sources/Vapor/Error/Abort.swift`) — 33 inbound connections
3. **Base32.swift** (`Sources/Vapor/Utilities/Base32.swift`) — 14 inbound connections
4. **Logger+Report.swift** (`Sources/Vapor/Logging/Logger+Report.swift`) — 7 inbound connections
5. **HTTPMediaType.swift** (`Sources/Vapor/HTTP/Headers/HTTPMediaType.swift`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ServerTests.swift** (`Tests/VaporTests/ServerTests.swift`) — 16 outbound dependencies
2. **ClientTests.swift** (`Tests/VaporTests/ClientTests.swift`) — 11 outbound dependencies
3. **ConditionalResponseCompressionTests.swift** (`Tests/VaporTests/ConditionalResponseCompressionTests.swift`) — 11 outbound dependencies
4. **HTTPServer.swift** (`Sources/Vapor/HTTP/Server/HTTPServer.swift`) — 9 outbound dependencies
5. **FileIO.swift** (`Sources/Vapor/Utilities/FileIO.swift`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `routes` **(Defensive Guards)** (@ `Sources/Development/routes.swift`) -> Impact: **71.9** | LOC: 307
- `testValidate` **(Defensive Guards)** (@ `Tests/VaporTests/ValidationTests.swift`) -> Impact: **71.5** | LOC: 910
- `asyncStreamFile` **(Many-Argument Workhorses)** (@ `Sources/Vapor/Utilities/FileIO.swift`) -> Impact: **64.1** | LOC: 107
  * *Intent:* /// app.get("file-stream") { req in /// return req.fileio.asyncStreamFile(at: "/path/to/file.txt") /// } /// /// Async equivalent of ``streamFile(at:c...
- `streamFile` **(Many-Argument Workhorses)** (@ `Sources/Vapor/Utilities/FileIO.swift`) -> Impact: **60.9** | LOC: 100
  * *Intent:* /// the `"ETag"` header and is capable of responding `304 Not Modified` if the file in question /// has not been modified since last served. This meth...
- `init` **(Many-Argument Workhorses)** (@ `Sources/Vapor/Utilities/URI.swift`) -> Impact: **59.4** | LOC: 56
  * *Intent:* /// Construct a ``URI`` from various subcomponents. /// /// Percent encoding is added to each component (if necessary) automatically. There is current...
- `getData` **(Stateful Encapsulated Methods)** (@ `Sources/Vapor/URLEncodedForm/URLEncodedFormEncoder.swift`) -> Impact: **58.5** | LOC: 269
- `download` **(Many-Argument Workhorses)** (@ `Sources/Vapor/HTTP/EndpointCache.swift`) -> Impact: **55.2** | LOC: 105
- `channelRead` **(Many-Argument Workhorses)** (@ `Sources/Vapor/HTTP/Server/HTTPServerRequestDecoder.swift`) -> Impact: **53.3** | LOC: 96
- `vapor_bcrypt_hashpass` **(Many-Argument Workhorses)** (@ `Sources/CVaporBcrypt/bcrypt.c`) -> Impact: **52.5** | LOC: 110
  * *Intent:* /* * the core bcrypt function */
- `write` **(Defensive Guards)** (@ `Sources/Vapor/HTTP/Server/HTTPServerResponseEncoder.swift`) -> Impact: **47.6** | LOC: 52
  * *Intent:* /// > Note: `self.promise` is the promise that completes the original write to `HTTPServerResponseEncoder` that /// > triggers the streaming response;...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Tests/VaporTests` | 49 | 5856.1 | 20.01% | 0.0% |
| `Tests/VaporTests/Utilities` | 10 | 5163.02 | 4.38% | 0.0% |
| `Sources/Vapor/Utilities` | 26 | 1788.82 | 16.66% | 38.98% |
| `Sources/Vapor/HTTP/Headers` | 16 | 1461.62 | 21.88% | 22.94% |
| `Sources/Vapor/HTTP/Server` | 8 | 1183.42 | 26.17% | 16.53% |
| `Sources/Vapor/URLEncodedForm` | 7 | 778.72 | 23.28% | 48.65% |
| `Sources/CVaporBcrypt` | 4 | 745.92 | 35.52% | 9.61% |
| `Sources/Vapor/Concurrency` | 14 | 662.78 | 22.88% | 31.51% |
| `Sources/Vapor/Content` | 11 | 645.48 | 26.03% | 42.77% |
| `Sources/Vapor/Middleware` | 9 | 439.78 | 19.55% | 45.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Sources/Vapor/Utilities/Base64.swift` -> **100.0%** Exposure
- `Sources/Vapor/Utilities/Base32.swift` -> **99.9989%** Exposure
- `Sources/Vapor/Commands/BootCommand.swift` -> **99.9925%** Exposure
- `Sources/XCTVapor/XCTVaporTests.swift` -> **99.9665%** Exposure
- `Sources/Vapor/Utilities/Extendable.swift` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Sources/Vapor/Commands/RoutesCommand.swift` -> **100.0%** Exposure
- `Sources/Vapor/Content/JSONCoder+Custom.swift` -> **100.0%** Exposure
- `Sources/Vapor/Error/Abort.swift` -> **100.0%** Exposure
- `Sources/Vapor/HTTP/Headers/HTTPCookies.swift` -> **100.0%** Exposure
- `Sources/Vapor/HTTP/Headers/HTTPHeaderExpires.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Tests/VaporTests/URLEncodedFormTests.swift` -> **47** Orphaned Functions | **0** Duplicates
- `Tests/VaporTests/ServerTests.swift` -> **36** Orphaned Functions | **2** Duplicates
- `Tests/VaporTests/ConditionalResponseCompressionTests.swift` -> **37** Orphaned Functions | **0** Duplicates
- `Tests/VaporTests/HTTPHeaderTests.swift` -> **34** Orphaned Functions | **0** Duplicates
- `Tests/VaporTests/ApplicationTests.swift` -> **15** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `Sources/Development/configure.swift` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `642` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Tests/VaporTests/Utilities/expired.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/VaporTests/ServerTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.817)
- **Top Global Matches:** file_cluster_10: 7.817, file_cluster_11: 8.527, file_cluster_15: 8.543
- **Magnitude:** 791.1 | **LOC:** 1496 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (36.1%)
- **Documentation Coverage:** 98.1132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testHTTP2RequestDecompression` **(I/O & Config Routines)** (Impact: 18.9)
  * `testDeprecatedServerStartMethods` **(Annotated & Test Methods)** (Impact: 18.4)
  * `testHTTP1RequestDecompression` **(I/O & Config Routines)** (Impact: 16.6)
  * `testRequestBodyBackpressureWorks` **(I/O & Config Routines)** (Impact: 14.3)
  * `testRequestBodyStreamGetsFinalisedEvenIfClientDisappears` **(Defensive Guards)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 270
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 441`, `args: 115`, `func_start: 53`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 170`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 36`
* *Architecture:* `concurrency: 95`, `import: 16`
* *Defense:* `safety: 57`, `doc: 18`, `test: 182`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AsyncHTTPClient, Atomics, Dispatch, Foundation, NIOConcurrencyHelpers, NIOCore, NIOFoundationCompat, NIOHTTP1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/VaporTests/ConditionalResponseCompressionTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.68)
- **Top Global Matches:** file_cluster_10: 6.68, file_cluster_11: 7.167, file_cluster_15: 8.349
- **Magnitude:** 675.62 | **LOC:** 817 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (33.6%)
- **Documentation Coverage:** 97.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertResponseCompression` **(Generic / Templated Code)** (Impact: 10.4)
  * `assertCompressed` **(Defensive Guards)** (Impact: 7.0)
  * `assertUncompressed` **(Defensive Guards)** (Impact: 7.0)
  * `testUnknownType` **(Callbacks & Closures)** (Impact: 3.5)
  * `testImage` **(Callbacks & Closures)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 475
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 841`, `args: 70`, `func_start: 45`, `class_start: 4`
* *Risk/State:* `state_mutation: 39`, `unreferenced_by_name: 37`
* *Architecture:* `concurrency: 380`, `import: 11`
* *Defense:* `safety: 7`, `doc: 22`, `test: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AsyncHTTPClient, Atomics, Foundation, NIOConcurrencyHelpers, NIOCore, NIOHTTP1, NIOPosix, NIOSSL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/HTTP/Server/HTTPServer.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.421)
- **Top Global Matches:** file_cluster_9: 7.421, file_cluster_15: 9.904, file_cluster_0: 10.079
- **Magnitude:** 530.96 | **LOC:** 817 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 3.812; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.9%), Concurrency Surface (formerly Concurrency) (49.4%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `init` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `start` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `init` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `init` **(Many-Argument Workhorses)** (Impact: 26.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 51 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 120`, `args: 39`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 79`
* *Architecture:* `api: 35`, `concurrency: 16`, `import: 9`
* *Defense:* `safety: 43`, `doc: 99`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.812
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 7):` Logging, NIOConcurrencyHelpers, NIOCore, NIOExtras, NIOHTTP1, NIOHTTP2, NIOHTTPCompression, NIOPosix...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Sources/CVaporBcrypt/blf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.29)
- **Top Global Matches:** file_cluster_15: 5.29, file_cluster_2: 6.906, file_cluster_16: 7.267
- **Magnitude:** 456.5 | **LOC:** 658 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.371; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Vapor_Blowfish_expandstate` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `Vapor_Blowfish_expand0state` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `vapor_blf_cbc_decrypt` **(Many-Argument Workhorses)** (Impact: 11.3)
  * `vapor_blf_cbc_encrypt` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `Vapor_Blowfish_stream2word` **(Many-Argument Workhorses)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 13`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 163`, `unreferenced_by_name: 8`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.371
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 1):` blf.h, types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Sources/Vapor/Utilities/FileIO.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.225)
- **Top Global Matches:** file_cluster_4: 8.225, file_cluster_6: 10.769, file_cluster_16: 13.359
- **Magnitude:** 393.76 | **LOC:** 624 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (48.2%)
- **Documentation Coverage:** 29.0323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asyncStreamFile` **(Many-Argument Workhorses)** (Impact: 64.1)
    * *Intent:* /// app.get("file-stream") { req in /// return req.fileio.asyncStreamFile(at: "/path/to/file.txt") /...
  * `streamFile` **(Many-Argument Workhorses)** (Impact: 60.9)
    * *Intent:* /// the `"ETag"` header and is capable of responding `304 Not Modified` if the file in question /// ...
  * `readFile` **(Many-Argument Workhorses)** (Impact: 16.9)
    * *Intent:* /// Reads the contents of a file at the supplied path in chunks. /// /// for try await chunk in try ...
  * `asByteBufferBounds` **(Stateful Encapsulated Methods)** (Impact: 16.9)
  * `generateETagHash` **(Stateful Encapsulated Methods)** (Impact: 9.4)
    * *Intent:* /// Generates a fresh ETag for a file or returns its currently cached one. /// - Parameters: /// - p...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 156`, `args: 37`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 45`, `import: 9`
* *Defense:* `safety: 40`, `doc: 150`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Crypto, Foundation, Logging, NIOConcurrencyHelpers, NIOCore, NIOHTTP1, NIOPosix, _NIOFileSystem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/URLEncodedForm/URLEncodedFormEncoder.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.934)
- **Top Global Matches:** file_cluster_4: 8.934, file_cluster_0: 9.222, file_cluster_15: 10.594
- **Magnitude:** 325.64 | **LOC:** 431 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 9.543; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.1%), Debt Markers (formerly Tech Debt) (96.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 34.1463% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getData` **(Stateful Encapsulated Methods)** (Impact: 58.5)
  * `encode` **(Defensive Guards)** (Impact: 31.7)
  * `encodeDate` **(Defensive Guards)** (Impact: 14.8)
  * `encode` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /// See `KeyedEncodingContainerProtocol`
  * `encode` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* /// See `SingleValueEncodingContainer`
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 141`, `args: 37`, `func_start: 34`, `class_start: 11`
* *Risk/State:* `state_mutation: 49`, `duplicate_logic: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 27`, `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.543
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.012579
  * `Imports (Out-Degree: 2):` Foundation, NIOCore, NIOHTTP1
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Tests/VaporTests/PipelineTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.877)
- **Top Global Matches:** file_cluster_4: 8.877, file_cluster_10: 9.532, file_cluster_11: 10.301
- **Magnitude:** 315.84 | **LOC:** 443 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.0%), Guard Balance (formerly Safety Score) (45.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEchoHandlers` **(Compute Cores)** (Impact: 22.4)
  * `testAsyncEchoHandlers` **(I/O & Config Routines)** (Impact: 10.1)
  * `testStreamingOffEventLoop` **(Callbacks & Closures)** (Impact: 8.1)
  * `testEOFFraming` **(Callbacks & Closures)** (Impact: 7.3)
  * `testCorrectResponseOrderOverVaporTCP` **(Callbacks & Closures)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 170
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 189`, `args: 33`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 45`, `import: 9`
* *Defense:* `safety: 11`, `test: 49`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AsyncHTTPClient, NIOConcurrencyHelpers, NIOCore, NIOEmbedded, NIOHTTP1.HTTPParserError, NIOPosix.ClientBootstrap, VaporTestUtils, XCTVapor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/VaporTests/AsyncRequestTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.03)
- **Top Global Matches:** file_cluster_0: 8.03, file_cluster_10: 8.328, file_cluster_11: 8.644
- **Magnitude:** 284.74 | **LOC:** 438 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.3%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_testRequestBodyBackpressureWorksWithAsyncStreaming` **(I/O & Config Routines)** (Impact: 14.7)
    * *Intent:* // TODO: Re-enable once it reliably works and doesn't cause issues with trying to shut the applicati...
  * `testStreamingRequestBodyCleansUp` **(Defensive Guards)** (Impact: 7.7)
  * `testStreamingRequest` **(I/O & Config Routines)** (Impact: 4.8)
  * `testRequestIdForwarding` **(Callbacks & Closures)** (Impact: 4.8)
  * `testLargeBodyCollectionDoesntCrash` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* // https://github.com/vapor/vapor/issues/2985
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 145
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 156`, `args: 37`, `func_start: 24`, `class_start: 8`
* *Risk/State:* `state_mutation: 29`, `planned_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `concurrency: 40`, `import: 8`
* *Defense:* `safety: 23`, `doc: 1`, `test: 37`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AsyncHTTPClient, Atomics, NIOConcurrencyHelpers, NIOCore, NIOFoundationCompat, Vapor, XCTVapor, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/VaporTests/AsyncClientTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.153)
- **Top Global Matches:** file_cluster_10: 8.153, file_cluster_0: 8.203, file_cluster_13: 8.257
- **Magnitude:** 276.4 | **LOC:** 373 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 2.371; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withRemoteApp` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* // MARK: - Helpers
  * `testBoilerplateClient` **(Annotated & Test Methods)** (Impact: 6.5)
  * `log` **(Many-Argument Workhorses)** (Impact: 6.2)
  * `clientConfigurationChange` **(Annotated & Test Methods)** (Impact: 3.0)
  * `clientConfigurationCantBeChangedAfterClientHasBeenUsed` **(Annotated & Test Methods)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 174`, `args: 42`, `func_start: 19`, `class_start: 10`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 56`, `import: 8`
* *Defense:* `safety: 7`, `test: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.371
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 2):` Logging, NIOConcurrencyHelpers, NIOCore, NIOEmbedded, NIOFoundationCompat, Testing, Vapor, VaporTesting
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Tests/VaporTests/AsyncFileTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.353)
- **Top Global Matches:** file_cluster_10: 7.353, file_cluster_11: 8.414, file_cluster_15: 9.096
- **Magnitude:** 265.3 | **LOC:** 353 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (40.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testStreamFileContentHeaderTail` **(Defensive Guards)** (Impact: 7.3)
  * `testStreamFileContentHeaderStart` **(Defensive Guards)** (Impact: 7.3)
  * `testStreamFileContentHeadersWithin` **(Defensive Guards)** (Impact: 7.1)
  * `testStreamFileNull` **(Callbacks & Closures)** (Impact: 4.0)
  * `testStreamFileContentHeadersOnlyFirstByte` **(Callbacks & Closures)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 187
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 205`, `args: 56`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `concurrency: 87`, `import: 8`
* *Defense:* `safety: 18`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Crypto, NIOCore, NIOHTTP1, Vapor, XCTVapor, XCTest, _NIOFileSystem, _NIOFileSystemFoundationCompat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/HTTP/Server/HTTPServerRequestDecoder.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.19)
- **Top Global Matches:** file_cluster_4: 6.19, file_cluster_15: 9.081, file_cluster_16: 9.783
- **Magnitude:** 254.48 | **LOC:** 412 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 3.096; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (26.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `channelRead` **(Many-Argument Workhorses)** (Impact: 53.3)
  * `handleBodyStreamStateResult` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `userInboundEventTriggered` **(Defensive Guards)** (Impact: 27.6)
  * `errorCaught` **(Type Conversions)** (Impact: 11.2)
  * `lookup` **(Defensive Guards)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 103`, `args: 37`, `func_start: 17`, `class_start: 9`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 25`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 18`, `doc: 12`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007075
  * `Imports (Out-Degree: 0):` Foundation, Logging, NIOCore, NIOHTTP1, X509
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Sources/Vapor/URLEncodedForm/URLEncodedFormDecoder.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.055)
- **Top Global Matches:** file_cluster_0: 7.055, file_cluster_15: 7.79, file_cluster_11: 8.303
- **Magnitude:** 250.9 | **LOC:** 546 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 5.042; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.1%), Concurrency Surface (formerly Concurrency) (87.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (43.6%)
- **Documentation Coverage:** 79.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Defensive Guards)** (Impact: 25.6)
  * `decodeDate` **(Defensive Guards)** (Impact: 21.4)
  * `decode` **(Defensive Guards)** (Impact: 16.4)
  * `init` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `decode` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 156`, `args: 48`, `func_start: 34`, `class_start: 9`
* *Risk/State:* `state_mutation: 27`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 11`, `concurrency: 9`, `import: 3`
* *Defense:* `safety: 38`, `doc: 90`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.042
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.012579
  * `Imports (Out-Degree: 3):` Foundation, NIOCore, NIOHTTP1
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Sources/Vapor/HTTP/Headers/HTTPHeaders+Name.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.243)
- **Top Global Matches:** file_cluster_15: 6.243, file_cluster_2: 7.316, file_cluster_11: 7.713
- **Magnitude:** 237.92 | **LOC:** 515 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 5.434; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (48.5%), Guard Balance (formerly Safety Score) (41.5%), Connectivity (formerly Api Exposure) (17.0%), Mutation Surface (formerly State Flux) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `first` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* /// Returns the first header value with the supplied name. /// - Parameter name: The header field na...
  * `add` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /// Add a header name/value pair to the block. /// /// This method is strictly additive: if there ar...
  * `replaceOrAdd` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /// Add a header name/value pair to the block, replacing any previous values for the /// same header...
  * `hash` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /// See `Hashable`
  * `init` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /// Create a HTTP header name with the provided String.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`, `args: 11`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 209`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 1`, `doc: 243`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010063
  * `Imports (Out-Degree: 0):` NIOHTTP1
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Sources/CVaporBcrypt/bcrypt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.645)
- **Top Global Matches:** file_cluster_8: 7.645, file_cluster_6: 17.693, file_cluster_3: 20.217
- **Magnitude:** 234.38 | **LOC:** 261 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.9%), Guard Balance (formerly Safety Score) (82.7%), Debt Markers (formerly Tech Debt) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vapor_bcrypt_hashpass` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* /* * the core bcrypt function */
  * `decode_base64` **(Stateful Encapsulated Methods)** (Impact: 17.9)
    * *Intent:* #define CHAR64(c) ( (c) > 127 ? 255 : index_64[(c)]) /* * read buflen (after decoding) bytes of data...
  * `vapor_encode_base64` **(Many-Argument Workhorses)** (Impact: 9.6)
    * *Intent:* /* * Turn len bytes of data into base64 encoded data. * This works without = padding. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 14`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 54`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bcrypt.h, blf.h, ctype.h, errno.h, stdio.h, stdlib.h, string.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/HTTP/Headers/HTTPCookies.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.956)
- **Top Global Matches:** file_cluster_4: 7.956, file_cluster_6: 8.287, file_cluster_15: 14.325
- **Magnitude:** 224.14 | **LOC:** 292 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 3.602; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.5%), Complexity Load (formerly Cognitive Load) (39.5%)
- **Documentation Coverage:** 7.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init?` **(Defensive Guards)** (Impact: 29.0)
  * `init` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* /// Creates a new `HTTPCookieValue`. /// /// let cookie = HTTPCookieValue(string: "123") /// /// - p...
  * `serialize` **(Defensive Guards)** (Impact: 19.0)
    * *Intent:* // MARK: Methods /// Serializes an `HTTPCookie` to a `String`.
  * `init` **(Callbacks & Closures)** (Impact: 3.2)
  * `init` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /// See `ExpressibleByDictionaryLiteral`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 62`, `args: 21`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `state_mutation: 40`, `unreferenced_by_name: 2`
* *Architecture:* `api: 21`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 18`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012579
  * `Imports (Out-Degree: 0):` Foundation, NIOHTTP1
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `Tests/VaporTests/HTTPHeaderTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.177)
- **Top Global Matches:** file_cluster_11: 6.177, file_cluster_15: 6.939, file_cluster_16: 8.267
- **Magnitude:** 219.88 | **LOC:** 493 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.1%), Complexity Load (formerly Cognitive Load) (23.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 85.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testContentDispositionQuotedFilename` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* // https://github.com/vapor/vapor/issues/2439
  * `testCookie_parsing` **(Compute Cores)** (Impact: 11.8)
  * `testAcceptType` **(I/O & Config Routines)** (Impact: 10.6)
  * `testCookie_invalidCookie` **(Compute Cores)** (Impact: 9.6)
  * `testMultipleCookieHeaders` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* // https://github.com/vpor/vapor/issues/3435
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 168`, `args: 74`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`, `unreferenced_by_name: 34`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`, `doc: 5`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` NIOHTTP1, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/Utilities/URI.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.653)
- **Top Global Matches:** file_cluster_4: 6.653, file_cluster_6: 9.774, file_cluster_15: 12.174
- **Magnitude:** 198.68 | **LOC:** 340 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 4.335; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (72.4%), Guard Balance (formerly Safety Score) (48.5%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* /// Construct a ``URI`` from various subcomponents. /// /// Percent encoding is added to each compon...
  * `init` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `init` **(Compute Cores)** (Impact: 16.0)
  * `init` **(Compute Cores)** (Impact: 13.4)
  * `init` **(Compute Cores)** (Impact: 2.9)
    * *Intent:* /// Designated initializer. /// /// - Parameter value: The string representation for the desired sch...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 57`, `args: 23`, `func_start: 10`, `class_start: 5`
* *Risk/State:* `state_mutation: 15`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 12`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.335
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009434
  * `Imports (Out-Degree: 0):` Foundation.URLComponents
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Sources/Vapor/Application.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.788)
- **Top Global Matches:** file_cluster_0: 7.788, file_cluster_11: 8.395, file_cluster_15: 8.524
- **Magnitude:** 195.3 | **LOC:** 359 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **5**; blast radius 32.426; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (94.0%), Guard Balance (formerly Safety Score) (50.9%), Complexity Load (formerly Cognitive Load) (37.4%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Stateful Encapsulated Methods)** (Impact: 10.4)
    * *Intent:* // async flag here is just to stop the compiler from complaining about duplicates
  * `asyncShutdown` **(Defensive Guards)** (Impact: 6.5)
  * `shutdown` **(I/O & Config Routines)** (Impact: 5.4)
  * `asyncBoot` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /// Called when the applications starts up, will trigger the lifecycle handlers. The asynchronous ve...
  * `make` **(Parameter Forwarders)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 109`, `args: 38`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 2`
* *Architecture:* `api: 30`, `concurrency: 33`, `import: 5`
* *Defense:* `safety: 12`, `doc: 33`, `sync_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.426
  * `Choke Point (Betweenness):` 0.001419 | `Ripple Effect (Closeness):` 0.110148
  * `Imports (Out-Degree: 4):` ConsoleKit, Logging, NIOConcurrencyHelpers, NIOCore, NIOPosix
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `Sources/Vapor/HTTP/Headers/HTTPHeaders+Directive.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.086)
- **Top Global Matches:** file_cluster_16: 6.086, file_cluster_15: 6.82, file_cluster_11: 7.917
- **Magnitude:** 187.74 | **LOC:** 305 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.371; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.2%), Complexity Load (formerly Cognitive Load) (31.7%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nextDirective` **(Stateful Encapsulated Methods)** (Impact: 12.7)
  * `nextDirectiveValue` **(Stateful Encapsulated Methods)** (Impact: 12.5)
  * `firstUnescapedDoubleQuote` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `firstIndex` **(Stateful Encapsulated Methods)** (Impact: 9.0)
    * *Intent:* /// Returns the first index matching any of the passed in Characters, nil if no match
  * `getSeparatorCharacters` **(Stateful Encapsulated Methods)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 95`, `args: 31`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 2`
* *Architecture:* `import: 1`
* *Defense:* `safety: 9`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.371
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 1):` NIOHTTP1
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Sources/Vapor/Utilities/DotEnv.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.277)
- **Top Global Matches:** file_cluster_16: 7.277, file_cluster_15: 7.79, file_cluster_0: 9.07
- **Magnitude:** 184.06 | **LOC:** 474 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.419; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.6%), Mutation Surface (formerly State Flux) (89.3%), Guard Balance (formerly Safety Score) (45.9%), Complexity Load (formerly Cognitive Load) (17.4%)
- **Documentation Coverage:** 34.4828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* /// Reads the dotenv files relevant to the environment and loads them into the process. /// /// let ...
  * `load` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* /// Reads the dotenv files relevant to the environment and loads them into the process. /// /// let ...
  * `parseLineValue` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `countDistance` **(Stateful Encapsulated Methods)** (Impact: 10.8)
  * `parseNext` **(Stateful Encapsulated Methods)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 105`, `args: 26`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 15`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 14`, `doc: 145`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.419
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.003145
  * `Imports (Out-Degree: 1):` Android, Darwin, Glibc, Logging, Musl, NIOCore, NIOPosix, _NIOFileSystem
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Tests/VaporTests/AsyncAuthTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.937)
- **Top Global Matches:** file_cluster_11: 6.937, file_cluster_15: 7.25, file_cluster_10: 7.668
- **Magnitude:** 183.76 | **LOC:** 368 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.2%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSessionAuthentication` **(I/O & Config Routines)** (Impact: 11.1)
  * `authenticate` **(Generic / Templated Code)** (Impact: 7.6)
  * `authenticate` **(Generic / Templated Code)** (Impact: 7.3)
  * `authenticate` **(Compute Cores)** (Impact: 7.2)
  * `authenticate` **(Compute Cores)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 130`, `args: 35`, `func_start: 30`, `class_start: 21`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 9`, `unreferenced_by_name: 11`
* *Architecture:* `concurrency: 39`, `import: 4`
* *Defense:* `safety: 2`, `doc: 6`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Android.sleep, Vapor, XCTVapor, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Sources/Vapor/Utilities/Base64.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.842)
- **Top Global Matches:** file_cluster_4: 9.842, file_cluster_0: 10.281, file_cluster_13: 10.426
- **Magnitude:** 176.6 | **LOC:** 171 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 35.926; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.1%)
- **Documentation Coverage:** 80.6452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode64` **(Stateful Encapsulated Methods)** (Impact: 36.9)
    * *Intent:* /// Specialization of ``decode(_:base:using:)`` for Base64 with no ignores and optional padding.
  * `encode64` **(Stateful Encapsulated Methods)** (Impact: 25.4)
    * *Intent:* /// Specialization of ``encode(_:base:pad:using:)`` for Base64.
  * `init?` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* /// Decode a string in canonical Base32-encoded representation.
  * `init?` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* /// Decode a string in Bcrypt-flavored Base64-encoded representation.
  * `base64Bytes` **(Defensive Guards)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 51`, `args: 32`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 23`, `duplicate_logic: 10`, `unreferenced_by_name: 2`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `safety: 13`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.926
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02673
  * `Imports (Out-Degree: 1):` Foundation.Data
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Sources/Vapor/Utilities/BaseN.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.743)
- **Top Global Matches:** file_cluster_4: 10.743, file_cluster_6: 11.769, file_cluster_16: 15.064
- **Magnitude:** 173.62 | **LOC:** 179 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 46.631; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.2%), Guard Balance (formerly Safety Score) (41.3%), Complexity Load (formerly Cognitive Load) (34.0%), Concurrency Surface (formerly Concurrency) (18.4%)
- **Documentation Coverage:** 70.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Stateful Encapsulated Methods)** (Impact: 43.7)
    * *Intent:* /// Fundamental decode: Transform any given byte sequence encoded with BaseN to an unencoded byte se...
  * `init` **(Stateful Encapsulated Methods)** (Impact: 30.6)
  * `encode` **(Stateful Encapsulated Methods)** (Impact: 21.5)
    * *Intent:* /// Fundamental encode: Transform any given byte sequence into a BaseN-encoded sequence of bytes des...
  * `init` **(Stateful Encapsulated Methods)** (Impact: 17.8)
  * `decode` **(Generic / Templated Code)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 43`, `args: 16`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 12`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 20`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 46.631
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.02673
  * `Imports (Out-Degree: 2):` Algorithms, Foundation.Data
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Tests/VaporTests/AsyncSessionTests.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.094)
- **Top Global Matches:** file_cluster_11: 7.094, file_cluster_10: 7.173, file_cluster_15: 7.217
- **Magnitude:** 170.18 | **LOC:** 148 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSessionDestroy` **(Callbacks & Closures)** (Impact: 12.7)
  * `testInvalidCookie` **(I/O & Config Routines)** (Impact: 7.4)
  * `readSession` **(Compute Cores)** (Impact: 5.4)
  * `updateSession` **(Parameter Forwarders)** (Impact: 4.2)
  * `createSession` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 60`, `args: 18`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 10`
* *Architecture:* `concurrency: 23`, `import: 4`
* *Defense:* `safety: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` NIOHTTP1, Vapor, XCTVapor, XCTest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Sources/Vapor/Routing/RoutesBuilder+WebSocket.swift` (SWIFT) | Magnitude: 30.14 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, doc: 18, structural_boundaries: 14, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Tests/VaporTests/AsyncClientTests.swift` (SWIFT) | Magnitude: 276.4 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 278, structural_boundaries: 174, concurrency: 56, args: 42
- `Tests/VaporTests/MiddlewareTests.swift` (SWIFT) | Magnitude: 117.22 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 209, structural_boundaries: 101, test: 71, concurrency: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Tests/VaporTests/AsyncMiddlewareTests.swift` (SWIFT) | Magnitude: 61.38 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 53, test: 22, concurrency: 21
- `Tests/VaporTests/AsyncSessionTests.swift` (SWIFT) | Magnitude: 170.18 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 60, concurrency: 23, args: 18
- `Sources/Vapor/Utilities/RFC1123.swift` (SWIFT) | Magnitude: 67.38 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 33, core_var_decl: 27, state_mutation: 25
- `Sources/Vapor/Core/Core.swift` (SWIFT) | Magnitude: 35.32 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 44, args: 15, safety: 12
- `Sources/Vapor/Commands/RoutesCommand.swift` (SWIFT) | Magnitude: 88.84 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 22, branch: 17, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Sources/Vapor/Responder/Application+Responder.swift` (SWIFT) | Magnitude: 55.92 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 29, args: 11, api: 11
- `Tests/VaporTests/DotEnvTests.swift` (SWIFT) | Magnitude: 41.44 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 75, core_var_decl: 50, state_mutation: 30, design_upper_case: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Tests/VaporTests/Utilities/CapturingMetricsSystem.swift` (SWIFT) | Magnitude: 74.56 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 47, func_start: 20, args: 17
- `Sources/VaporTesting/+TestingHTTPResponse.swift` (SWIFT) | Magnitude: 51.22 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 94, core_var_decl: 21, structural_boundaries: 18, design_pascal_case: 12
- `Sources/Vapor/Multipart/File+Multipart.swift` (SWIFT) | Magnitude: 31.56 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 17, branch: 11, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Sources/Vapor/Concurrency/RequestBody+Concurrency.swift` (SWIFT) | Magnitude: 68.66 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 37, branch: 32, doc: 21

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Sources/Vapor/HTTP/Headers/HTTPCookies.swift` -> **Gwynne Raskind** (100.0% isolated ownership) | Magnitude: 224.14
- `Tests/VaporTests/HTTPHeaderTests.swift` -> **Gwynne Raskind** (100.0% isolated ownership) | Magnitude: 219.88
- `Tests/VaporTests/AsyncAuthTests.swift` -> **Honza Dvorsky** (100.0% isolated ownership) | Magnitude: 183.76
- `Tests/VaporTests/AuthenticationTests.swift` -> **Honza Dvorsky** (100.0% isolated ownership) | Magnitude: 134.12
- `Sources/VaporTestUtils/TestingApplication.swift` -> **Tibor Bödecs** (100.0% isolated ownership) | Magnitude: 108.3

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Sources/Vapor/Application.swift` -> **Severity: 0.133** (Bridge: 0.0014 * Flux: 93.9509%)
- `Sources/Vapor/Error/Abort.swift` -> **Severity: 0.055** (Bridge: 0.0005 * Flux: 100.0%)
- `Sources/Vapor/Utilities/Base32.swift` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 99.9999%)
- `Sources/Development/configure.swift` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 99.7201%)
- `Sources/Vapor/URLEncodedForm/URLEncodedFormDecoder.swift` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 93.0862%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Sources/Vapor/Error/Abort.swift` -> **Severity: 6.753** (Embedded: 0.1146 * Error Risk: 58.9251%)
- `Sources/Vapor/Application.swift` -> **Severity: 5.607** (Embedded: 0.1101 * Error Risk: 50.8999%)
- `Sources/Vapor/Logging/Logger+Report.swift` -> **Severity: 5.397** (Embedded: 0.0818 * Error Risk: 65.9902%)
- `Sources/Vapor/Error/ErrorSource.swift` -> **Severity: 4.12** (Embedded: 0.0709 * Error Risk: 58.0716%)
- `Sources/Vapor/Commands/RoutesCommand.swift` -> **Severity: 3.862** (Embedded: 0.0582 * Error Risk: 66.3822%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Sources/Vapor/Utilities/BaseN.swift` -> **Severity: 3291.598** (Blast Radius: 46.631 * Doc Risk: 70.5882%)
- `Sources/Vapor/Utilities/Base64.swift` -> **Severity: 2897.259** (Blast Radius: 35.926 * Doc Risk: 80.6452%)
- `Sources/Vapor/Application.swift` -> **Severity: 2161.734** (Blast Radius: 32.426 * Doc Risk: 66.6667%)
- `Sources/Vapor/Utilities/Base32.swift` -> **Severity: 1755.6** (Blast Radius: 33.649 * Doc Risk: 52.1739%)
- `Sources/Vapor/Error/Abort.swift` -> **Severity: 1257.325** (Blast Radius: 50.293 * Doc Risk: 25.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6007 call pairs -- scoped 14.0%, unique 4.4%, ambiguous 43.3%, external 38.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| swift | 5980 | 13.8% | 4.3% | 43.5% | 38.3% |
| c | 27 | 51.9% | 18.5% | 0.0% | 29.6% |

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
