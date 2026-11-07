# ARCHITECTURAL_BRIEF: AFNetworking
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AFNetworking/AFNetworking.git` |
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
- **Scope:** 132 analyzed artifact(s), 9938 LOC.
- **Load-bearing artifact:** `Tests/Tests/AFTestCase.h` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Framework/AFNetworking.h` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `fastlane/.env` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 211 |
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 79 |
| Total LOC | 9938 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.6% |
| Dominant Lang | OBJECTIVE-C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.442 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2209 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7831 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| OBJECTIVE-C | 74 | 9082 | 56.1% |
| JSON | 25 | 579 | 18.9% |
| XML | 16 | 0 | 12.1% |
| MARKDOWN | 7 | 0 | 5.3% |
| SWIFT | 4 | 140 | 3.0% |
| RUBY | 3 | 53 | 2.3% |
| YAML | 2 | 83 | 1.5% |
| PLAINTEXT | 1 | 1 | 0.8% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 131 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Type Conversions Files 30%, Large Core Modules 16%, Declarative / Non-Code 5%, Large Core Modules (3) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 124 | 93.9% |
| Unknown | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 79*

**Composition by Extension & Reason:**
- `.cer`: 27x Excluded (Unsupported Extension: '.cer')
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.xcworkspacedata'), 1x Excluded (Unsupported Extension: '.entitlements')
- `.xcscheme`: 9x Excluded (Unsupported Extension: '.xcscheme')
- `.pbxproj`: 3x Excluded (Unsupported Extension: '.pbxproj')
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.m`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pch`: 2x Excluded (Unsupported Extension: '.pch')
- `.modulemap`: 1x Excluded (Unsupported Extension: '.modulemap')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.catalyst`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.default`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.deploy`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.macos`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.1 | 12.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 25.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 98.7 | 12.6 | 6.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 42.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1787 | 64 | 35 | `AFNetworking/AFURLRequestSerialization.m` |
| cleanup | 0 | 0 | 0 | - |
| guards | 170 | 32 | 3 | `AFNetworking/AFURLRequestSerialization.m` |
| danger | 237 | 36 | 5 | `AFNetworking/AFURLRequestSerialization.m` |
| concurrency | 84 | 16 | 2 | `AFNetworking/AFURLSessionManager.m` |
| connectivity | 1007 | 66 | 24 | `AFNetworking/AFURLRequestSerialization.m` |
| io | 237 | 25 | 3 | `AFNetworking/AFURLSessionManager.m` |
| crypto | 0 | 0 | 0 | - |
| ipc | 83 | 4 | 0 | `AFNetworking/AFURLSessionManager.m` |
| time | 9 | 3 | 0 | `UIKit+AFNetworking/AFNetworkActivityIndicatorManager.m` |
| serialization | 18 | 9 | 0 | `AFNetworking/AFURLRequestSerialization.m` |
| regex | 0 | 0 | 0 | - |
| events | 72 | 9 | 0 | `AFNetworking/AFURLSessionManager.m` |
| tests | 407 | 20 | 8 | `Tests/Tests/AFHTTPSessionManagerTests.m` |
| docs | 381 | 20 | 5 | `AFNetworking/AFURLSessionManager.h` |
| debt | 21 | 8 | 0 | `AFNetworking/AFURLResponseSerialization.m` |
| mutation | 1476 | 51 | 27 | `AFNetworking/AFURLRequestSerialization.m` |
| dead_code | 432 | 48 | 8 | `Tests/Tests/AFSecurityPolicyTests.m` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 5 | 3 | 0 | `Example/iOS Example/Views/PostTableViewCell.m` |
| ui | 10 | 9 | 0 | `Example/tvOS Example/ViewController.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `AFNetworking/AFURLSessionManager.m` (Hits: 70)
- `Tests/Tests/AFSecurityPolicyTests.m` (Hits: 42)
- `AFNetworking/AFURLRequestSerialization.m` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AFTestCase.h** (`Tests/Tests/AFTestCase.h`) — 21 inbound connections
2. **AFURLResponseSerialization.h** (`AFNetworking/AFURLResponseSerialization.h`) — 13 inbound connections
3. **AFURLSessionManager.h** (`AFNetworking/AFURLSessionManager.h`) — 12 inbound connections
4. **AFURLRequestSerialization.h** (`AFNetworking/AFURLRequestSerialization.h`) — 11 inbound connections
5. **AFNetworkReachabilityManager.h** (`AFNetworking/AFNetworkReachabilityManager.h`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AFNetworking.h** (`Framework/AFNetworking.h`) — 19 outbound dependencies
2. **AFHTTPSessionManager.m** (`AFNetworking/AFHTTPSessionManager.m`) — 13 outbound dependencies
3. **UIKit+AFNetworking.h** (`UIKit+AFNetworking/UIKit+AFNetworking.h`) — 10 outbound dependencies
4. **AFNetworking.h** (`AFNetworking/AFNetworking.h`) — 9 outbound dependencies
5. **AFNetworkReachabilityManager.m** (`AFNetworking/AFNetworkReachabilityManager.m`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `downloadImageForURLRequest` **(Many-Argument Workhorses)** (@ `UIKit+AFNetworking/AFImageDownloader.m`) -> Impact: **57.2** | LOC: 115
- `evaluateServerTrust` **(Compute Cores)** (@ `AFNetworking/AFSecurityPolicy.m`) -> Impact: **45.3** | LOC: 74
  * *Intent:* #pragma mark -
- `AFInflatedImageFromResponseWithDataAtScale` **(Many-Argument Workhorses)** (@ `AFNetworking/AFURLResponseSerialization.m`) -> Impact: **44.5** | LOC: 91
- `URLSession` **(Many-Argument Workhorses)** (@ `AFNetworking/AFURLSessionManager.m`) -> Impact: **42.5** | LOC: 46
- `URLSession` **(Many-Argument Workhorses)** (@ `AFNetworking/AFURLSessionManager.m`) -> Impact: **41.8** | LOC: 75
  * *Intent:* #pragma mark - NSURLSessionTaskDelegate
- `setImageWithURLRequest` **(Many-Argument Workhorses)** (@ `UIKit+AFNetworking/UIImageView+AFNetworking.m`) -> Impact: **36.9** | LOC: 68
- `setImageForState` **(Many-Argument Workhorses)** (@ `UIKit+AFNetworking/UIButton+AFNetworking.m`) -> Impact: **34.8** | LOC: 60
- `setBackgroundImageForState` **(Many-Argument Workhorses)** (@ `UIKit+AFNetworking/UIButton+AFNetworking.m`) -> Impact: **34.8** | LOC: 60
- `requestBySerializingRequest` **(Many-Argument Workhorses)** (@ `AFNetworking/AFURLRequestSerialization.m`) -> Impact: **34.6** | LOC: 53
  * *Intent:* #pragma mark - AFURLRequestSerialization
- `validateResponse` **(Many-Argument Workhorses)** (@ `AFNetworking/AFURLResponseSerialization.m`) -> Impact: **32.5** | LOC: 50
  * *Intent:* #pragma mark -

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `fastlane` | 2 | 5001.28 | 0.0% | 0.0% |
| `AFNetworking` | 14 | 3060.8 | 30.34% | 42.7% |
| `Tests/Tests` | 23 | 1342.26 | 2.84% | 0.0% |
| `UIKit+AFNetworking` | 19 | 1276.74 | 35.57% | 18.97% |
| `__monolith__` | 7 | 117.72 | 7.43% | 0.0% |
| `Example/tvOS Example` | 5 | 87.34 | 11.0% | 0.0% |
| `Example/Today Extension Example` | 3 | 82.1 | 19.42% | 0.0% |
| `Example/macOS Example` | 5 | 59.88 | 4.22% | 0.0% |
| `Example/watchOS Example Extension` | 5 | 48.12 | 0.0% | 0.0% |
| `Example/iOS Example` | 4 | 44.62 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `AFNetworking/AFURLResponseSerialization.h` -> **99.9999%** Exposure
- `AFNetworking/AFHTTPSessionManager.m` -> **93.8421%** Exposure
- `AFNetworking/AFURLResponseSerialization.m` -> **92.4142%** Exposure
- `UIKit+AFNetworking/AFAutoPurgingImageCache.m` -> **82.9436%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **80.6679%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `AFNetworking.podspec` -> **100.0%** Exposure
- `Example/iOS Example/Views/PostTableViewCell.m` -> **100.0%** Exposure
- `UIKit+AFNetworking/AFAutoPurgingImageCache.m` -> **99.9997%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **99.986%** Exposure
- `AFNetworking/AFURLResponseSerialization.m` -> **99.981%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Tests/Tests/AFSecurityPolicyTests.m` -> **46** Orphaned Functions | **0** Duplicates
- `Tests/Tests/AFHTTPSessionManagerTests.m` -> **43** Orphaned Functions | **0** Duplicates
- `Tests/Tests/AFURLSessionManagerTests.m` -> **35** Orphaned Functions | **0** Duplicates
- `AFNetworking/AFURLSessionManager.m` -> **30** Orphaned Functions | **0** Duplicates
- `AFNetworking/AFURLRequestSerialization.m` -> **26** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `251` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `fastlane/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `AFNetworking/AFURLRequestSerialization.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.729)
- **Top Global Matches:** file_cluster_12: 6.729, file_cluster_7: 8.84, file_cluster_5: 9.117
- **Magnitude:** 888.9 | **LOC:** 1398 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 6.772; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.8%), Debt Markers (formerly Tech Debt) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.3464% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `requestBySerializingRequest` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* #pragma mark - AFURLRequestSerialization
  * `multipartFormRequestWithMethod` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `requestWithMultipartFormRequest` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `AFQueryStringPairsFromKeyAndValue` **(Compute Cores)** (Impact: 22.3)
  * `appendPartWithFileURL` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 136`, `args: 75`, `func_start: 100`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 156`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `io: 22`, `api: 91`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 24`, `doc: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.772
  * `Choke Point (Betweenness):` 0.000352 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 2):` AFURLRequestSerialization.h, CoreServices.h, MobileCoreServices.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `AFNetworking/AFURLSessionManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.817)
- **Top Global Matches:** file_cluster_12: 7.817, file_cluster_15: 9.458, file_cluster_16: 10.157
- **Magnitude:** 799.2 | **LOC:** 1275 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 13.917; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (74.4%), Concurrency Surface (formerly Concurrency) (73.2%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 98.5816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `URLSession` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `URLSession` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* #pragma mark - NSURLSessionTaskDelegate
  * `respondsToSelector` **(Type Conversions)** (Impact: 15.0)
  * `observeValueForKeyPath` **(Type Conversions)** (Impact: 14.0)
    * *Intent:* #pragma mark - NSProgress Tracking
  * `URLSession` **(Many-Argument Workhorses)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 77`, `args: 73`, `func_start: 104`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 110`, `unreferenced_by_name: 30`
* *Architecture:* `io: 70`, `api: 83`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 12`, `doc: 3`, `sync_locks: 4`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.917
  * `Choke Point (Betweenness):` 0.001028 | `Ripple Effect (Closeness):` 0.048855
  * `Imports (Out-Degree: 1):` AFURLSessionManager.h, runtime.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `AFNetworking/AFURLResponseSerialization.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.276)
- **Top Global Matches:** file_cluster_12: 7.276, file_cluster_5: 9.244, file_cluster_7: 9.334
- **Magnitude:** 518.1 | **LOC:** 837 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AFInflatedImageFromResponseWithDataAtScale` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `validateResponse` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* #pragma mark -
  * `AFJSONObjectByRemovingKeysWithNullValues` **(Type Conversions)** (Impact: 25.5)
  * `responseObjectForResponse` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* #pragma mark - AFURLResponseSerialization
  * `responseObjectForResponse` **(Type Conversions)** (Impact: 15.4)
    * *Intent:* #pragma mark - AFURLResponseSerialization
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 107`, `args: 37`, `func_start: 53`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 74`, `fragile_debt: 1`, `duplicate_logic: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`, `api: 40`, `concurrency: 3`, `import: 7`
* *Defense:* `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AFURLResponseSerialization.h, Cocoa.h, CoreGraphics.h, TargetConditionals.h, UIKit.h, WatchKit.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `UIKit+AFNetworking/AFImageDownloader.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.925)
- **Top Global Matches:** file_cluster_4: 8.925, file_cluster_12: 8.94, file_cluster_15: 9.147
- **Magnitude:** 289.66 | **LOC:** 422 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Guard Balance (formerly Safety Score) (62.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `downloadImageForURLRequest` **(Many-Argument Workhorses)** (Impact: 57.2)
  * `cancelTaskForImageDownloadReceipt` **(Type Conversions)** (Impact: 7.0)
  * `enqueueMergedTask` **(Type Conversions)** (Impact: 6.2)
  * `initWithSessionManager` **(Type Conversions)** (Impact: 5.7)
  * `safelyStartNextTaskIfNecessary` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 47`, `args: 18`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 43`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 33`, `concurrency: 15`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AFHTTPSessionManager.h, AFImageDownloader.h, TargetConditionals.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFSecurityPolicyTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.604)
- **Top Global Matches:** file_cluster_12: 7.604, file_cluster_7: 7.92, file_cluster_5: 10.249
- **Magnitude:** 200.32 | **LOC:** 549 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.1%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AFUTTrustWithCertificate` **(Parameter Forwarders)** (Impact: 1.9)
  * `testPolicyWithPublicKeyPinningModeHasHTTPBinOrgPinnedCertificate` **(Callbacks & Closures)** (Impact: 1.6)
  * `testPolicyWithCertificatePinningModeHasHTTPBinOrgPinnedCertificate` **(Callbacks & Closures)** (Impact: 1.6)
  * `testPolicyWithPublicKeyPinningAllowsHTTPBinOrgServerTrustWithEntireCertificateChainPinned` **(I/O & Config Routines)** (Impact: 1.5)
  * `testPolicyWithCertificatePinningAllowsHTTPBinOrgServerTrustWithEntireCertificateChainPinned` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 3`, `func_start: 56`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 69`, `unreferenced_by_name: 46`
* *Architecture:* `io: 42`, `api: 46`, `import: 2`
* *Defense:* `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AFSecurityPolicy.h, AFTestCase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `AFNetworking/AFHTTPSessionManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.373)
- **Top Global Matches:** file_cluster_5: 7.373, file_cluster_7: 8.282, file_cluster_12: 8.758
- **Magnitude:** 192.06 | **LOC:** 358 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Debt Markers (formerly Tech Debt) (93.8%), Concurrency Surface (formerly Concurrency) (78.2%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dataTaskWithHTTPMethod` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `POST` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `setSecurityPolicy` **(Type Conversions)** (Impact: 10.6)
  * `initWithCoder` **(Type Conversions)** (Impact: 8.3)
  * `initWithBaseURL` **(Type Conversions)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 33`, `args: 20`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 19`, `unreferenced_by_name: 14`
* *Architecture:* `api: 13`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AFHTTPSessionManager.h, AFURLRequestSerialization.h, AFURLResponseSerialization.h, Availability.h, Security.h, TargetConditionals.h, UIKit.h, WatchKit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `UIKit+AFNetworking/AFNetworkActivityIndicatorManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.64)
- **Top Global Matches:** file_cluster_15: 7.64, file_cluster_11: 7.961, file_cluster_13: 8.383
- **Magnitude:** 188.68 | **LOC:** 240 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateCurrentStateForNetworkActivityChange` **(I/O & Config Routines)** (Impact: 11.2)
  * `setCurrentState` **(Type Conversions)** (Impact: 11.1)
    * *Intent:* #pragma mark - Internal State Management
  * `setNetworkActivityIndicatorVisible` **(Type Conversions)** (Impact: 6.3)
  * `AFNetworkRequestFromNotification` **(Compute Cores)** (Impact: 4.6)
  * `activationDelayTimerFired` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 7`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `concurrency: 8`, `import: 2`
* *Defense:* `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.398
  * `Choke Point (Betweenness):` 0.00047 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 3):` AFNetworkActivityIndicatorManager.h, AFURLSessionManager.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `AFNetworking/AFSecurityPolicy.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.482)
- **Top Global Matches:** file_cluster_7: 9.482, file_cluster_12: 9.819, file_cluster_5: 10.544
- **Magnitude:** 177.5 | **LOC:** 342 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (65.4%), Debt Markers (formerly Tech Debt) (60.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateServerTrust` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* #pragma mark -
  * `setPinnedCertificates` **(Type Conversions)** (Impact: 7.9)
  * `AFPublicKeyForCertificate` **(I/O & Config Routines)** (Impact: 7.4)
  * `AFPublicKeyTrustChainForServerTrust` **(Compute Cores)** (Impact: 7.4)
  * `AFSecKeyGetData` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* // // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR // IMPLIED, INCLUDI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 34`, `args: 14`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 29`, `unreferenced_by_name: 7`
* *Architecture:* `io: 10`, `api: 13`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 1):` AFSecurityPolicy.h, AssertMacros.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `UIKit+AFNetworking/UIButton+AFNetworking.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.427)
- **Top Global Matches:** file_cluster_12: 7.427, file_cluster_15: 7.778, file_cluster_16: 8.379
- **Magnitude:** 175.36 | **LOC:** 303 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (53.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setImageForState` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `setBackgroundImageForState` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `af_imageDownloadReceiptKeyForState` **(Compute Cores)** (Impact: 10.5)
  * `af_backgroundImageDownloadReceiptKeyForState` **(Compute Cores)** (Impact: 10.5)
  * `cancelImageDownloadTaskForState` **(Type Conversions)** (Impact: 3.2)
    * *Intent:* #pragma mark -
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 27`, `args: 21`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AFImageDownloader.h, UIButton+AFNetworking.h, UIImageView+AFNetworking.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFHTTPSessionManagerTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.497)
- **Top Global Matches:** file_cluster_12: 7.497, file_cluster_7: 7.92, file_cluster_5: 9.449
- **Magnitude:** 170.46 | **LOC:** 695 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.8%), Connectivity (formerly Api Exposure) (11.7%), Complexity Load (formerly Cognitive Load) (5.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUploadProgressIsReportedForStreamingPost` **(I/O & Config Routines)** (Impact: 4.2)
  * `testUploadProgressIsReportedForPOST` **(I/O & Config Routines)** (Impact: 4.0)
  * `testThatRedirectBlockIsCalledWhen302IsEncountered` **(I/O & Config Routines)** (Impact: 3.5)
  * `testThatSerializationErrorGeneratesErrorAndNullTaskForGET` **(I/O & Config Routines)** (Impact: 3.2)
  * `testAuthenticationChallengeHandlerCredentialResult` **(Callbacks & Closures)** (Impact: 3.2)
    * *Intent:* # pragma mark - Custom Authentication Challenge Handler
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 31`, `args: 33`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 32`, `unreferenced_by_name: 43`
* *Architecture:* `io: 11`, `api: 45`, `import: 3`
* *Defense:* `safety: 7`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` AFHTTPSessionManager.h, AFSecurityPolicy.h, AFTestCase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFURLSessionManagerTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.176)
- **Top Global Matches:** file_cluster_2: 7.176, file_cluster_10: 7.466, file_cluster_15: 7.53
- **Magnitude:** 161.88 | **LOC:** 551 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (12.2%), Complexity Load (formerly Cognitive Load) (3.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUploadTaskDoesReportProgress` **(I/O & Config Routines)** (Impact: 4.3)
  * `setUp` **(I/O & Config Routines)** (Impact: 4.0)
  * `testBackgroundManagerReturnsExpectedClassForUploadTask` **(I/O & Config Routines)** (Impact: 3.8)
  * `testBackgroundManagerReturnsExpectedClassForDataTask` **(I/O & Config Routines)** (Impact: 3.6)
  * `testBackgroundManagerReturnsExpectedClassForDownloadTask` **(I/O & Config Routines)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 19`, `args: 12`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `unreferenced_by_name: 35`
* *Architecture:* `io: 7`, `api: 46`, `import: 3`
* *Defense:* `safety: 4`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AFTestCase.h, AFURLSessionManager.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFImageDownloaderTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.097)
- **Top Global Matches:** file_cluster_10: 6.097, file_cluster_2: 7.868, file_cluster_13: 8.185
- **Magnitude:** 160.32 | **LOC:** 601 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.5%), Concurrency Surface (formerly Concurrency) (47.9%), Complexity Load (formerly Cognitive Load) (11.6%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shouldCacheImage` **(Type Conversions)** (Impact: 6.4)
    * *Intent:* #pragma mark -
  * `testThatItCanDownloadAndCancelAndDownloadAgain` **(I/O & Config Routines)** (Impact: 4.5)
  * `testThatImageCacheIsPromptedShouldCacheNot` **(Callbacks & Closures)** (Impact: 3.8)
  * `addImage` **(Type Conversions)** (Impact: 3.8)
  * `testThatImageCacheIsPromptedShouldCache` **(Callbacks & Closures)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 47`, `args: 33`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `state_mutation: 55`, `unreferenced_by_name: 23`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 2`
* *Defense:* `doc: 1`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AFImageDownloader.h, AFTestCase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `AFNetworking/AFNetworkReachabilityManager.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.779)
- **Top Global Matches:** file_cluster_12: 6.779, file_cluster_7: 8.434, file_cluster_5: 9.665
- **Magnitude:** 141.96 | **LOC:** 270 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Concurrency Surface (formerly Concurrency) (94.7%), Debt Markers (formerly Tech Debt) (77.3%), Complexity Load (formerly Cognitive Load) (72.0%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AFNetworkReachabilityStatusForFlags` **(Compute Cores)** (Impact: 13.8)
  * `AFStringFromNetworkReachabilityStatus` **(Compute Cores)** (Impact: 10.5)
  * `keyPathsForValuesAffectingValueForKey` **(Type Conversions)** (Impact: 6.0)
    * *Intent:* #pragma mark - NSKeyValueObserving
  * `startMonitoring` **(Type Conversions)** (Impact: 5.5)
    * *Intent:* #pragma mark -
  * `AFPostReachabilityStatusChange` **(State Mutators)** (Impact: 4.1)
    * *Intent:* /** * Queue a status change notification for the main thread. * * This is done to ensure that the no...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 33`, `args: 12`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 17`, `unreferenced_by_name: 7`
* *Architecture:* `api: 16`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AFNetworkReachabilityManager.h, inet.h, ifaddrs.h, netdb.h, in.h, in6.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `UIKit+AFNetworking/AFAutoPurgingImageCache.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.883)
- **Top Global Matches:** file_cluster_13: 7.883, file_cluster_15: 8.086, file_cluster_2: 8.401
- **Magnitude:** 139.34 | **LOC:** 206 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.3%), Complexity Load (formerly Cognitive Load) (94.6%), Debt Markers (formerly Tech Debt) (82.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addImage` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `initWithMemoryCapacity` **(Type Conversions)** (Impact: 4.4)
  * `initWithImage` **(Type Conversions)** (Impact: 4.1)
    * *Intent:* #import "AFAutoPurgingImageCache.h"
  * `imageCacheKeyFromURLRequest` **(Type Conversions)** (Impact: 3.8)
  * `removeImageWithIdentifier` **(Type Conversions)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 10`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 6`
* *Architecture:* `api: 24`, `concurrency: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AFAutoPurgingImageCache.h, TargetConditionals.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `UIKit+AFNetworking/WKWebView+AFNetworking.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.242)
- **Top Global Matches:** file_cluster_12: 8.242, file_cluster_0: 8.667, file_cluster_15: 9.169
- **Magnitude:** 97.42 | **LOC:** 155 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 6.772; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.5%), Complexity Load (formerly Cognitive Load) (91.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadRequest` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `loadRequest` **(Many-Argument Workhorses)** (Impact: 10.9)
    * *Intent:* #pragma mark -
  * `sessionManager` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* #pragma mark -
  * `responseSerializer` **(Generic / Templated Code)** (Impact: 2.5)
  * `af_setURLSessionTask` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 14`, `args: 7`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.772
  * `Choke Point (Betweenness):` 0.000528 | `Ripple Effect (Closeness):` 0.015267
  * `Imports (Out-Degree: 6):` AFHTTPSessionManager.h, AFURLRequestSerialization.h, AFURLResponseSerialization.h, WKWebView+AFNetworking.h, runtime.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `AFNetworking/AFURLSessionManager.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.042)
- **Top Global Matches:** file_cluster_5: 10.042, file_cluster_7: 11.222, file_cluster_12: 12.065
- **Magnitude:** 94.04 | **LOC:** 517 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 48.823; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.7%), Guard Balance (formerly Safety Score) (49.8%), Concurrency Surface (formerly Concurrency) (22.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dataTaskWithRequest` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
  * `uploadTaskWithRequest` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
  * `uploadTaskWithRequest` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
  * `downloadTaskWithRequest` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
  * `downloadTaskWithResumeData` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 20`, `api: 47`, `concurrency: 1`, `import: 6`
* *Defense:* `doc: 92`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 48.823
  * `Choke Point (Betweenness):` 0.006224 | `Ripple Effect (Closeness):` 0.114673
  * `Imports (Out-Degree: 5):` AFCompatibilityMacros.h, AFNetworkReachabilityManager.h, AFSecurityPolicy.h, AFURLRequestSerialization.h, AFURLResponseSerialization.h, Foundation.h
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `UIKit+AFNetworking/UIImageView+AFNetworking.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.154)
- **Top Global Matches:** file_cluster_12: 7.154, file_cluster_15: 7.979, file_cluster_16: 8.547
- **Magnitude:** 90.16 | **LOC:** 160 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%), Guard Balance (formerly Safety Score) (59.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setImageWithURLRequest` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `cancelImageDownloadTask` **(I/O & Config Routines)** (Impact: 2.3)
  * `sharedImageDownloader` **(Type Conversions)** (Impact: 2.1)
    * *Intent:* #pragma mark -
  * `setImageWithURL` **(Type Conversions)** (Impact: 2.1)
  * `af_setActiveImageDownloadReceipt` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 14`, `args: 8`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AFImageDownloader.h, UIImageView+AFNetworking.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFHTTPRequestSerializationTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.6)
- **Top Global Matches:** file_cluster_12: 7.6, file_cluster_5: 9.035, file_cluster_7: 9.246
- **Magnitude:** 89.16 | **LOC:** 245 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (78.9%), Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (13.9%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatHTTPHeaderValueCanBeSetToReferenceCountedStringFromMultipleThreadsWithoutCrashing` **(I/O & Config Routines)** (Impact: 4.0)
  * `testQueryStringSerializationCanFailWithError` **(I/O & Config Routines)** (Impact: 2.9)
  * `testThatEmojiIsProperlyEncoded` **(I/O & Config Routines)** (Impact: 2.7)
    * *Intent:* #pragma mark - #3028 tests //https://github.com/AFNetworking/AFNetworking/pull/3028
  * `initWithURLRequest` **(Type Conversions)** (Impact: 1.8)
    * *Intent:* // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN // THE SOFTWARE. #impor...
  * `read` **(Type Conversions)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 3`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 30`, `concurrency: 3`, `import: 2`
* *Defense:* `test: 23`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AFTestCase.h, AFURLRequestSerialization.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `AFNetworking/AFURLRequestSerialization.h` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.425)
- **Top Global Matches:** file_cluster_5: 8.425, file_cluster_7: 9.993, file_cluster_12: 10.319
- **Magnitude:** 78.22 | **LOC:** 480 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **4**; blast radius 28.16; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.2%), Guard Balance (formerly Safety Score) (56.0%), Debt Markers (formerly Tech Debt) (28.1%), Test Surface (formerly Verification) (2.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multipartFormRequestWithMethod` **(Type Conversions)** (Impact: 2.7)
    * *Intent:* */
  * `appendPartWithFileURL` **(Type Conversions)** (Impact: 2.7)
    * *Intent:* */
  * `appendPartWithInputStream` **(Type Conversions)** (Impact: 2.7)
    * *Intent:* */
  * `requestWithMethod` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
  * `appendPartWithFileData` **(Type Conversions)** (Impact: 2.4)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 20`, `func_start: 23`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 37`, `import: 4`
* *Defense:* `doc: 55`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116443
  * `Imports (Out-Degree: 0):` Foundation.h, TargetConditionals.h, UIKit.h, WatchKit.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `Tests/Tests/AFAutoPurgingImageCacheTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.058)
- **Top Global Matches:** file_cluster_2: 7.058, file_cluster_13: 7.859, file_cluster_15: 7.861
- **Magnitude:** 73.7 | **LOC:** 242 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.6%), Connectivity (formerly Api Exposure) (11.1%), Complexity Load (formerly Cognitive Load) (7.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatPrioritizedImagesWithOldestLastAccessDatesAreRemovedDuringPurge` **(I/O & Config Routines)** (Impact: 7.4)
  * `testThatImagesArePurgedWhenCapcityIsReached` **(I/O & Config Routines)** (Impact: 4.9)
    * *Intent:* #pragma mark - Purging
  * `setUp` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, // OUT OF OR IN CON...
  * `testImageIsNotReturnedWhenURLDoesntMatch` **(I/O & Config Routines)** (Impact: 1.5)
  * `testDuplicateImageAddedToCacheIsReturned` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 18`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AFAutoPurgingImageCache.h, XCTest.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `UIKit+AFNetworking/UIProgressView+AFNetworking.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.022)
- **Top Global Matches:** file_cluster_12: 8.022, file_cluster_7: 8.081, file_cluster_5: 9.767
- **Magnitude:** 63.8 | **LOC:** 127 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (82.2%), Debt Markers (formerly Tech Debt) (77.7%), Mutation Surface (formerly State Flux) (64.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `observeValueForKeyPath` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* #pragma mark - NSKeyValueObserving
  * `setProgressWithUploadProgressOfTask` **(Type Conversions)** (Impact: 4.1)
    * *Intent:* #pragma mark -
  * `setProgressWithDownloadProgressOfTask` **(Type Conversions)** (Impact: 4.1)
  * `af_setUploadProgressAnimated` **(Type Conversions)** (Impact: 1.6)
  * `af_setDownloadProgressAnimated` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 6`, `args: 5`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AFURLSessionManager.h, UIProgressView+AFNetworking.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example/Today Extension Example/TodayViewController.m` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.27)
- **Top Global Matches:** file_cluster_15: 8.27, file_cluster_13: 8.457, file_cluster_0: 8.549
- **Magnitude:** 60.02 | **LOC:** 107 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (58.3%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `widgetPerformUpdateWithCompletionHandler` **(Compute Cores)** (Impact: 9.3)
  * `setPost` **(Type Conversions)** (Impact: 3.6)
  * `savePost` **(Type Conversions)** (Impact: 3.4)
  * `loadSavedPost` **(Type Conversions)** (Impact: 3.4)
  * `viewWillAppear` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 5`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 13`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AFNetworking, NotificationCenter.h, Post.h, TodayViewController.h, User.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFNetworkActivityManagerTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_12: 6.995, file_cluster_7: 7.563, file_cluster_10: 9.269
- **Magnitude:** 56.28 | **LOC:** 202 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (8.7%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatVisibilityDelaysAreApplied` **(I/O & Config Routines)** (Impact: 4.8)
  * `testThatIndicatorBlockIsOnlyCalledOnceEachForStartAndEndForMultipleRequests` **(I/O & Config Routines)** (Impact: 4.5)
  * `testThatNetworkActivityIndicatorTurnsOnAndOffIndicatorWhenRequestSucceeds` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* #pragma mark -
  * `testThatNetworkActivityIndicatorTurnsOnAndOffIndicatorWhenRequestFails` **(I/O & Config Routines)** (Impact: 4.3)
  * `testThatIndicatorKVOOnlyTriggerOnce` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 9`, `args: 10`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `unreferenced_by_name: 7`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AFHTTPSessionManager.h, AFNetworkActivityIndicatorManager.h, AFTestCase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Tests/AFJSONSerializationTests.m` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.922)
- **Top Global Matches:** file_cluster_12: 7.922, file_cluster_2: 9.402, file_cluster_11: 9.446
- **Magnitude:** 55.34 | **LOC:** 229 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.276; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.5%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testThatJSONRequestSerializationHandlesParametersDictionary` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* #pragma mark -
  * `testThatJSONRequestSerializationHandlesParametersArray` **(I/O & Config Routines)** (Impact: 1.5)
  * `testThatJSONRequestSerializationHandlesInvalidParameters` **(I/O & Config Routines)** (Impact: 1.5)
  * `testThatJSONRequestSerializationErrorsWithInvalidJSON` **(I/O & Config Routines)** (Impact: 1.5)
  * `testThatJSONRemovesKeysWithNullValues` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `unreferenced_by_name: 16`
* *Architecture:* `io: 6`, `api: 20`, `import: 3`
* *Defense:* `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AFTestCase.h, AFURLRequestSerialization.h, AFURLResponseSerialization.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `Tests/Tests/AFUIImageViewTests.m` (OBJECTIVE-C) | Magnitude: 43.56 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 95, api: 14, state_mutation: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `UIKit+AFNetworking/UIProgressView+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 63.8 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 51, explicit_casts: 19, branch: 12, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Tests/Tests/AFPropertyListRequestSerializerTests.m` (OBJECTIVE-C) | Magnitude: 9.5 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 4, api: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `UIKit+AFNetworking/UIActivityIndicatorView+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 43.6 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 39, explicit_casts: 17, func_start: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `UIKit+AFNetworking/UIRefreshControl+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 42.06 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, explicit_casts: 17, func_start: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `Tests/Tests/AFHTTPResponseSerializationTests.m` (OBJECTIVE-C) | Magnitude: 26.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, test: 17, explicit_casts: 12, api: 9
- `Example/iOS Example/Views/PostTableViewCell.m` (OBJECTIVE-C) | Magnitude: 34.78 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 13, explicit_casts: 11, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `UIKit+AFNetworking/AFImageDownloader.m` (OBJECTIVE-C) | Magnitude: 289.66 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 47, explicit_casts: 46, state_mutation: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `Tests/Tests/AFTestCase.h` (OBJECTIVE-C) | Magnitude: 17.68 | Delta: **0.197** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: api: 10, explicit_casts: 10, func_start: 6, args: 5
- `AFNetworking/AFHTTPSessionManager.h` (OBJECTIVE-C) | Magnitude: 40.9 | Delta: **0.213** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 40, doc: 25, bitwise_ops: 22, safety_bypasses: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `AFNetworking/AFURLSessionManager.m` -> **Severity: 0.103** (Bridge: 0.001 * Flux: 99.8697%)
- `UIKit+AFNetworking/WKWebView+AFNetworking.m` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.8716%)
- `UIKit+AFNetworking/AFNetworkActivityIndicatorManager.m` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 99.9709%)
- `AFNetworking/AFURLRequestSerialization.m` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 99.986%)
- `Example/iOS Example/Views/PostTableViewCell.m` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `AFNetworking/AFURLResponseSerialization.h` -> **Severity: 9.219** (Embedded: 0.1299 * Error Risk: 70.9836%)
- `Tests/Tests/AFTestCase.h` -> **Severity: 8.376** (Embedded: 0.1606 * Error Risk: 52.1415%)
- `AFNetworking/AFURLRequestSerialization.h` -> **Severity: 6.526** (Embedded: 0.1164 * Error Risk: 56.0417%)
- `AFNetworking/AFHTTPSessionManager.h` -> **Severity: 5.985** (Embedded: 0.0748 * Error Risk: 80.0%)
- `AFNetworking/AFURLSessionManager.h` -> **Severity: 5.711** (Embedded: 0.1147 * Error Risk: 49.8039%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Tests/Tests/AFTestCase.h` -> **Severity: 4479.0** (Blast Radius: 44.79 * Doc Risk: 100.0%)
- `AFNetworking/AFURLSessionManager.m` -> **Severity: 1371.96** (Blast Radius: 13.917 * Doc Risk: 98.5816%)
- `Example/iOS Example/Views/PostTableViewCell.h` -> **Severity: 1348.0** (Blast Radius: 13.48 * Doc Risk: 100.0%)
- `Example/tvOS Example/Gravatar.swift` -> **Severity: 976.2** (Blast Radius: 9.762 * Doc Risk: 100.0%)
- `Example/iOS Example/Views/PostTableViewCell.m` -> **Severity: 789.3** (Blast Radius: 7.893 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 318 literal sites + 1 sites through wrappers = 319

- `AFImageWithDataAtScale` (function, memory_alloc, primitive): 1 call sites in 1 files -- `AFNetworking/AFURLResponseSerialization.m`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3284 call pairs -- scoped 27.4%, unique 1.2%, ambiguous 2.3%, external 69.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| objective-c | 3251 | 27.7% | 1.1% | 2.2% | 69.0% |
| ruby | 21 | 0.0% | 0.0% | 0.0% | 100.0% |
| swift | 12 | 16.7% | 8.3% | 8.3% | 66.7% |

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
