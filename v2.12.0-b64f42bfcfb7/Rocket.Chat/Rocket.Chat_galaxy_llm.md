# ARCHITECTURAL_BRIEF: Rocket.Chat
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/RocketChat/Rocket.Chat.git` |
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
- **Scope:** 2867 analyzed artifact(s), 166841 LOC.
- **Load-bearing artifact:** `packages/rest-typings/src/v1/Ajv.ts` -- 161 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/core-typings/src/index.ts` -- pulls in 115 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ee/packages/federation-matrix/tests/end-to-end/messaging.spec.ts` at magnitude 46542.72 (structural weight, not risk).
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
| Total Artifacts | 9691 |
| Analyzed Artifacts (Scanned) | 2867 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6824 |
| Total LOC | 166841 |
| Volatility Index | 0.024 |
| % Scanned of codebase = | 29.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9193 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2094 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6984 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 276 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2512 | 155814 | 87.6% |
| JSON | 113 | 5506 | 3.9% |
| MARKDOWN | 95 | 0 | 3.3% |
| PLAINTEXT | 78 | 6 | 2.7% |
| YAML | 38 | 2587 | 1.3% |
| CSS | 10 | 257 | 0.3% |
| JAVASCRIPT | 9 | 1899 | 0.3% |
| DOCKERFILE | 6 | 468 | 0.2% |
| XML | 4 | 1 | 0.1% |
| HTML | 1 | 13 | 0.0% |
| SHELL | 1 | 290 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2861 |
| unknown | unknown | 6 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 29%, Declarative / Non-Code 22%, Generic / Templated Code Files 18%, Callbacks & Closures Files 11%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2693 | 93.9% |
| Unknown | 6 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 167 | 5.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6824*

**Composition by Extension & Reason:**
- `.ts`: 3904x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.tsx`: 1973x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 22 exceeds 500 chars), 1x Excluded (Saturation: Line 58 exceeds 500 chars)
- `.json`: 98x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 4808 LOC), 2x Excluded (Massive Static Asset Blob: 2720 LOC)
- `.js`: 140x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 107x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sublime-project')
- `.snap`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.snap), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `.scss`: 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 44x Excluded (Explicitly Denied Extension: '.png')
- `.ttf`: 44x Excluded (Explicitly Denied Extension: '.ttf')
- `.svg`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 22x Excluded (Explicitly Denied Extension: '.woff2')
- `.woff`: 21x Excluded (Explicitly Denied Extension: '.woff')
- `.txt`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.3 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.8 | 13.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 28.9 | 22.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.6 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.7 | 0.8 | 0.2 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 77.8 | 7.3 | 5.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1274 | 484 | 1 | `packages/apps-engine/src/server/managers/AppListenerManager.ts` |
| cleanup | 94 | 54 | 0 | `ee/apps/ddp-streamer/src/Client.ts` |
| guards | 5736 | 898 | 4 | `ee/packages/federation-matrix/tests/end-to-end/messaging.spec.ts` |
| danger | 3101 | 532 | 2 | `ee/packages/abac/src/service.spec.ts` |
| concurrency | 10457 | 726 | 8 | `ee/packages/federation-matrix/tests/end-to-end/dms.spec.ts` |
| connectivity | 11114 | 2274 | 8 | `packages/models/src/models/Users.ts` |
| io | 1857 | 210 | 0 | `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts` |
| crypto | 15 | 12 | 0 | `packages/node-poplib/src/index.js` |
| ipc | 25 | 16 | 0 | `packages/apps-engine/src/server/runtime/deno/AppsEngineDenoRuntime.ts` |
| time | 682 | 154 | 0 | `packages/models/src/models/LivechatRooms.ts` |
| serialization | 90 | 57 | 0 | `packages/release-changelog/src/getGitHubInfo.ts` |
| regex | 194 | 82 | 0 | `ee/packages/federation-matrix/src/helpers/message.parsers.ts` |
| events | 1425 | 213 | 0 | `packages/node-poplib/src/index.js` |
| tests | 6282 | 269 | 0 | `ee/packages/federation-matrix/tests/end-to-end/room.spec.ts` |
| docs | 701 | 212 | 0 | `packages/eslint-config/index.js` |
| debt | 783 | 215 | 0 | `.github/actions/docker-image-size-tracker/action.yml` |
| mutation | 20186 | 1913 | 16 | `packages/rest-typings/src/v1/omnichannel.ts` |
| dead_code | 352 | 121 | 0 | `packages/apps-engine/tests/server/accessors/AppAccessors.test.ts` |
| credential | 125 | 16 | 0 | `.github/actions/update-version-durability/package-lock.json` |
| threat | 25 | 5 | 0 | `packages/message-parser/tests/emoji.test.ts` |
| ml_ai | 188 | 51 | 0 | `ee/packages/federation-matrix/tests/end-to-end/dms.spec.ts` |
| ui | 3451 | 685 | 4 | `packages/ui-client/src/components/Header/Header.stories.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts` (Hits: 186)
- `packages/message-parser/tests/link.test.ts` (Hits: 134)
- `packages/server-fetch/tests/checkForSsrf.spec.ts` (Hits: 116)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Ajv.ts** (`packages/rest-typings/src/v1/Ajv.ts`) — 161 inbound connections
2. **IBaseModel.ts** (`packages/model-typings/src/models/IBaseModel.ts`) — 80 inbound connections
3. **index.ts** (`packages/apps-engine/src/server/bridges/index.ts`) — 77 inbound connections
4. **BaseRaw.ts** (`packages/models/src/models/BaseRaw.ts`) — 73 inbound connections
5. **IRocketChatRecord.ts** (`packages/core-typings/src/IRocketChatRecord.ts`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/core-typings/src/index.ts`) — 115 outbound dependencies
2. **index.ts** (`packages/ui-contexts/src/index.ts`) — 105 outbound dependencies
3. **index.ts** (`packages/model-typings/src/index.ts`) — 83 outbound dependencies
4. **modelClasses.ts** (`packages/models/src/modelClasses.ts`) — 75 outbound dependencies
5. **index.ts** (`packages/rest-typings/src/index.ts`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `reducer` **(Many-Argument Workhorses)** (@ `apps/uikit-playground/src/Context/reducer.ts`) -> Impact: **108.4** | LOC: 229
- `handleMediaMessage` **(Many-Argument Workhorses)** (@ `ee/packages/federation-matrix/src/events/message.ts`) -> Impact: **102.4** | LOC: 88
- `executeListener` **(Type Conversions)** (@ `packages/apps-engine/src/server/managers/AppListenerManager.ts`) -> Impact: **98.2** | LOC: 129
  * *Intent:* /* eslint-disable-next-line complexity */
- `POP3Client` **(Many-Argument Workhorses)** (@ `packages/node-poplib/src/index.js`) -> Impact: **80.4** | LOC: 248
  * *Intent:* // Constructor
- `findRoomsWithCriteria` **(Compute Cores)** (@ `packages/models/src/models/LivechatRooms.ts`) -> Impact: **78.7** | LOC: 103
- `findModTarget` **(Many-Argument Workhorses)** (@ `packages/mongo-adapter/src/updateFilter.ts`) -> Impact: **74.8** | LOC: 97
- `method` **(Many-Argument Workhorses)** (@ `packages/http-router/src/Router.ts`) -> Impact: **74.5** | LOC: 149
- `message` **(I/O & Config Routines)** (@ `ee/packages/federation-matrix/src/events/message.ts`) -> Impact: **74.2** | LOC: 304
- `push` **(Many-Argument Workhorses)** (@ `packages/mongo-adapter/src/updateFilter.ts`) -> Impact: **72.8** | LOC: 96
- `Compare and generate report` **(I/O & Config Routines)** (@ `.github/actions/docker-image-size-tracker/action.yml`) -> Impact: **69.5** | LOC: 271

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `ee/packages/federation-matrix/tests/end-to-end` | 5 | 49933.45 | 98.08% | 0.0% |
| `ee/packages/federation-matrix/docker-compose/traefik/certs` | 3 | 15000.0 | 0.0% | 0.0% |
| `packages/models/src/models` | 78 | 10913.8 | 25.62% | 2.23% |
| `packages/model-typings/src/models` | 82 | 6444.4 | 27.84% | 1.18% |
| `__monolith__` | 17 | 5851.66 | 0.73% | 1.41% |
| `ee/packages/federation-matrix/docker-compose/hs1` | 3 | 5027.64 | 0.0% | 0.0% |
| `apps/meteor/ee/server/services` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/apps-engine/src/server/accessors` | 63 | 2185.22 | 21.74% | 0.29% |
| `packages/apps-engine/src/server/managers` | 19 | 2094.18 | 54.76% | 2.33% |
| `packages/ui-client/src/components/Wizard` | 19 | 1954.6 | 12.07% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/core-services/src/types/IFederationService.ts` -> **100.0%** Exposure
- `packages/tools/src/objectMap.ts` -> **99.9996%** Exposure
- `packages/ui-voip/src/hooks/useMediaCallAction.ts` -> **99.9981%** Exposure
- `packages/ui-voip/src/views/MediaCallWidget/OngoingCall.stories.tsx` -> **99.9848%** Exposure
- `scripts/todo-issue/src/github.ts` -> **99.9639%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/node-poplib/src/index.js` -> **100.0%** Exposure
- `apps/uikit-playground/src/Components/CodeEditor/Extensions/payloadLinter.ts` -> **100.0%** Exposure
- `apps/uikit-playground/src/Components/ComponentSideBar/SliderBtn.tsx` -> **100.0%** Exposure
- `apps/uikit-playground/src/Components/DropDown/itemsStyle.ts` -> **100.0%** Exposure
- `ee/packages/federation-matrix/src/helpers/validateFederatedUsername.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ee/packages/abac/src/service.spec.ts` -> **15** Orphaned Functions | **10** Duplicates
- `packages/apps-engine/tests/server/accessors/AppAccessors.test.ts` -> **16** Orphaned Functions | **0** Duplicates
- `packages/apps-engine/tests/server/managers/AppApiManager.test.ts` -> **9** Orphaned Functions | **5** Duplicates
- `packages/apps-engine/tests/server/managers/AppRuntimeManager.test.ts` -> **14** Orphaned Functions | **0** Duplicates
- `packages/apps-engine/tests/server/managers/AppSettingsManager.test.ts` -> **13** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/ui-client/src/components/PasswordVerifier/PasswordVerifiers.spec.tsx` -> **100.0%** Exposure
- `packages/apps-engine/tests/test-data/bridges/cloudBridge.ts` -> **99.9997%** Exposure
- `packages/apps-engine/tests/test-data/utilities.ts` -> **45.1416%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3743` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ee/packages/federation-matrix/tests/end-to-end/messaging.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.973)
- **Top Global Matches:** file_cluster_12: 7.973, file_cluster_10: 8.3, file_cluster_7: 9.284
- **Magnitude:** 46542.72 | **LOC:** 1388 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.6%), Guard Balance (formerly Safety Score) (10.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Concurrency (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 349`, `args: 126`, `func_start: 51`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 11`, `planned_debt: 2`
* *Architecture:* `io: 44`, `concurrency: 194`, `import: 9`
* *Defense:* `safety: 407`, `test: 344`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` file.helper, messages.helper, rooms.helper, users.helper, constants, config, synapse-client, core-typings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/ee/server/services/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/hs1/hs1.signing.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/element-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/hs1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/rc1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ui-client/src/components/Wizard/useWizard.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.094)
- **Top Global Matches:** file_cluster_10: 6.094, file_cluster_13: 9.185, file_cluster_2: 9.644
- **Magnitude:** 1481.8 | **LOC:** 133 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (28.8%), Guard Balance (formerly Safety Score) (21.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 57`, `args: 36`, `func_start: 8`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 24`, `import: 3`
* *Defense:* `safety: 22`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` StepNode, useWizard, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/models/src/models/Users.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.749)
- **Top Global Matches:** file_cluster_0: 6.749, file_cluster_15: 7.624, file_cluster_11: 9.246
- **Magnitude:** 1465.76 | **LOC:** 3366 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.8%), Concurrency Surface (formerly Concurrency) (54.3%), Guard Balance (formerly Safety Score) (51.2%)
- **Documentation Coverage:** 95.1435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getNextLeastBusyAgent` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `getLastAvailableAgentRouted` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `findByActiveUsersExcept` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `findPaginatedByActiveUsersExcept` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `findUsersByIdentifiers` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 334`, `args: 239`, `func_start: 226`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 46`, `dead_code: 2`, `planned_debt: 19`
* *Architecture:* `io: 2`, `api: 222`, `concurrency: 62`, `import: 8`
* *Defense:* `safety: 24`, `doc: 12`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.308
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002221
  * `Imports (Out-Degree: 5):` helpers, index, BaseRaw, core-typings, model-typings, string-helpers, mongodb
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `ee/packages/federation-matrix/tests/end-to-end/dms.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.403)
- **Top Global Matches:** file_cluster_10: 6.403, file_cluster_11: 8.033, file_cluster_13: 9.159
- **Magnitude:** 1399.82 | **LOC:** 1867 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 69.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.3%), Guard Balance (formerly Safety Score) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitForRoomEvent` **(Callbacks & Closures)** (Impact: 2.7)
  * `listener` **(Callbacks & Closures)** (Impact: 1.6)
  * `matrixId` **(Interface Declarations)** (Impact: 1.1)
  * `matrixId` **(Interface Declarations)** (Impact: 1.1)
  * `matrixId` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 178 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 1256
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 422`, `args: 180`, `func_start: 103`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 101`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `concurrency: 366`, `import: 12`
* *Defense:* `safety: 28`, `test: 345`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` api-data, rooms.helper, users.helper, constants, retry, config, synapse-client, withTimeout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/models/src/models/LivechatRooms.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.222)
- **Top Global Matches:** file_cluster_0: 8.222, file_cluster_15: 9.084, file_cluster_4: 9.243
- **Magnitude:** 1356.22 | **LOC:** 2825 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Guard Balance (formerly Safety Score) (54.4%)
- **Documentation Coverage:** 99.2188% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findRoomsWithCriteria` **(Compute Cores)** (Impact: 78.7)
  * `findRoomsByVisitorIdAndMessageWithCriteria` **(Compute Cores)** (Impact: 34.1)
  * `saveRoomById` **(Compute Cores)** (Impact: 28.8)
  * `getQueueMetrics` **(I/O & Config Routines)** (Impact: 27.8)
  * `findAllRooms` **(Compute Cores)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 156`, `args: 133`, `func_start: 130`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 98`
* *Architecture:* `io: 9`, `api: 127`, `concurrency: 50`, `import: 8`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002184
  * `Imports (Out-Degree: 3):` readSecondaryPreferred, updater, BaseRaw, core-typings, model-typings, string-helpers, mongodb
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/model-typings/src/models/IUsersModel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.467)
- **Top Global Matches:** file_cluster_5: 9.467, file_cluster_7: 13.391, file_cluster_12: 14.105
- **Magnitude:** 1061.78 | **LOC:** 438 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.5%), Guard Balance (formerly Safety Score) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findPaginatedByActiveUsersExcept` **(Generic / Templated Code)** (Impact: 21.6)
  * `getNextLeastBusyAgent` **(Compute Cores)** (Impact: 16.0)
  * `getLastAvailableAgentRouted` **(Compute Cores)** (Impact: 16.0)
  * `findByActiveUsersExcept` **(Generic / Templated Code)** (Impact: 13.6)
  * `findPaginatedByActiveLocalUsersExcept` **(Generic / Templated Code)** (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 45`, `args: 220`, `func_start: 220`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 39`, `duplicate_logic: 2`
* *Architecture:* `api: 219`, `concurrency: 157`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000349
  * `Imports (Out-Degree: 2):` DocumentWithProjection, IBaseModel, core-typings, mongodb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/models/src/models/Subscriptions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.869)
- **Top Global Matches:** file_cluster_0: 5.869, file_cluster_15: 8.999, file_cluster_12: 10.002
- **Magnitude:** 1042.72 | **LOC:** 2180 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.272; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.1%), Guard Balance (formerly Safety Score) (50.9%)
- **Documentation Coverage:** 96.5398% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findConnectedUsersExcept` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `findByRoomIdAndNotAlertOrOpenExcludingUserIds` **(Defensive Guards)** (Impact: 18.6)
  * `addUnreadThreadByRoomIdAndUserIds` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* // ////////////////////////////////////////////////////////////////// // threads
  * `createWithRoomAndUser` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* // INSERT
  * `findUsersInRoles` **(Generic / Templated Code)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 204
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 213`, `args: 151`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 143`, `concurrency: 154`, `import: 8`
* *Defense:* `safety: 9`, `doc: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.272
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002221
  * `Imports (Out-Degree: 5):` index, BaseRaw, core-typings, model-typings, string-helpers, lodash, mem, mongodb
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/apps-engine/src/server/AppManager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_15: 7.912, file_cluster_16: 8.127, file_cluster_11: 8.383
- **Magnitude:** 1008.88 | **LOC:** 1241 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **24**; blast radius 2.448; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.5%), Complexity Load (formerly Cognitive Load) (74.5%), Connectivity (formerly Api Exposure) (56.1%)
- **Documentation Coverage:** 54.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* /** Gets the Apps which match the filter passed in. */
  * `update` **(Many-Argument Workhorses)** (Impact: 22.3)
  * `changeStatus` **(Defensive Guards)** (Impact: 19.3)
  * `updateAppsMarketplaceInfo` **(Defensive Guards)** (Impact: 17.6)
  * `constructor` **(I/O & Config Routines)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 60 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 492
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 299`, `args: 89`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `state_mutation: 80`
* *Architecture:* `io: 2`, `api: 48`, `concurrency: 192`, `import: 28`
* *Defense:* `safety: 46`, `doc: 22`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.448
  * `Choke Point (Betweenness):` 0.002525 | `Ripple Effect (Closeness):` 0.027409
  * `Imports (Out-Degree: 35):` AppStatus, metadata, IPermission, users, IGetAppsFilter, ProxiedApp, bridges, IInternalPersistenceBridge...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `packages/models/src/models/Rooms.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.726)
- **Top Global Matches:** file_cluster_0: 6.726, file_cluster_15: 10.351, file_cluster_11: 11.022
- **Magnitude:** 1001.56 | **LOC:** 2368 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.242; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findChildrenOfTeam` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `findByNameOrFnameContainingAndTypes` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `getChannelsWithNumberOfMessagesBetweenDateQuery` **(I/O & Config Routines)** (Impact: 21.7)
  * `findAllByTypesAndDiscussionAndTeam` **(Generic / Templated Code)** (Impact: 13.4)
  * `findPaginatedByNameOrFNameAndRoomIdsIncludingTeamRooms` **(Many-Argument Workhorses)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 165
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 224`, `args: 162`, `func_start: 159`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 155`, `concurrency: 140`, `import: 8`
* *Defense:* `safety: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.242
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00211
  * `Imports (Out-Degree: 6):` index, readSecondaryPreferred, updater, BaseRaw, core-typings, model-typings, string-helpers, mongodb
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/media-signaling/src/lib/Call.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.158)
- **Top Global Matches:** file_cluster_16: 7.158, file_cluster_15: 8.237, file_cluster_4: 8.43
- **Magnitude:** 926.2 | **LOC:** 1381 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 69.2%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.241; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Concurrency Surface (formerly Concurrency) (97.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.4%)
- **Documentation Coverage:** 89.8551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initializeRemoteCall` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* /** initialize a call with the data received from the server on a 'new' signal; this gets executed o...
  * `processSignal` **(Defensive Guards)** (Impact: 26.1)
  * `addStateTimeout` **(Stateful Encapsulated Methods)** (Impact: 21.6)
  * `setContractState` **(Defensive Guards)** (Impact: 21.4)
  * `onWebRTCConnectionStateChange` **(Stateful Encapsulated Methods)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 78
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 240`, `args: 93`, `func_start: 86`, `class_start: 3`
* *Risk/State:* `state_mutation: 77`
* *Architecture:* `api: 57`, `concurrency: 38`, `import: 12`
* *Defense:* `safety: 73`, `doc: 7`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.241
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000785
  * `Imports (Out-Degree: 11):` definition, call, client, logger, media, services, server, NegotiationManager...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/models/src/models/Messages.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.804)
- **Top Global Matches:** file_cluster_0: 5.804, file_cluster_15: 8.55, file_cluster_12: 9.456
- **Magnitude:** 912.5 | **LOC:** 1876 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.3%), Guard Balance (formerly Safety Score) (52.3%)
- **Documentation Coverage:** 99.0338% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `removeByIdPinnedTimestampLimitAndUsers` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `findVisibleByRoomIdBetweenTimestampsNotContainingTypes` **(Many-Argument Workhorses)** (Impact: 18.8)
  * `findVisibleByRoomIdNotContainingTypesAndUsers` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `findVisibleByRoomIdBeforeTimestampNotContainingTypes` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `countVisibleByRoomIdBetweenTimestampsNotContainingTypes` **(Many-Argument Workhorses)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 148
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 156`, `args: 109`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 31`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 102`, `concurrency: 103`, `import: 7`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002184
  * `Imports (Out-Degree: 2):` readSecondaryPreferred, BaseRaw, core-typings, model-typings, rest-typings, string-helpers, mongodb
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `ee/packages/federation-matrix/src/FederationMatrix.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.115)
- **Top Global Matches:** file_cluster_4: 7.115, file_cluster_6: 10.101, file_cluster_9: 12.43
- **Magnitude:** 783.14 | **LOC:** 1026 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.459; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleThreadedMessage` **(Defensive Guards)** (Impact: 39.6)
  * `removeReaction` **(Many-Argument Workhorses)** (Impact: 31.7)
  * `created` **(Callbacks & Closures)** (Impact: 28.1)
  * `getQuoteMessage` **(Stateful Encapsulated Methods)** (Impact: 26.5)
  * `notifyRoomRead` **(Defensive Guards)** (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 271
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 212`, `args: 49`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `planned_debt: 7`
* *Architecture:* `api: 24`, `concurrency: 156`, `import: 13`
* *Defense:* `safety: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.459
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00109
  * `Imports (Out-Degree: 5):` createOrUpdateFederatedUser, extractDomainFromMatrixUserId, message.parsers, validateFederatedUsername, MatrixMediaService, core-services, core-typings, federation-sdk...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ee/packages/federation-matrix/tests/end-to-end/ban.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.344)
- **Top Global Matches:** file_cluster_12: 7.344, file_cluster_7: 7.811, file_cluster_10: 8.125
- **Magnitude:** 771.53 | **LOC:** 315 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 252
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 91`, `args: 36`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 21`
* *Architecture:* `concurrency: 67`, `import: 10`
* *Defense:* `safety: 1`, `test: 53`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` rooms.ts, api-data, rooms.helper, users.helper, constants, retry, config, synapse-client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/omni-core/src/visitor/create.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.281)
- **Top Global Matches:** file_cluster_0: 7.281, file_cluster_12: 7.856, file_cluster_13: 7.929
- **Magnitude:** 753.69 | **LOC:** 117 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.366; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.8%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 19`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 1`, `concurrency: 10`, `import: 5`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.366
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000698
  * `Imports (Out-Degree: 0):` core-typings, logger, models, patch-injection, tools
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/model-typings/src/models/IRoomsModel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.668)
- **Top Global Matches:** file_cluster_0: 8.668, file_cluster_5: 10.516, file_cluster_12: 12.982
- **Magnitude:** 727.96 | **LOC:** 350 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.247; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findChildrenOfTeam` **(Generic / Templated Code)** (Impact: 11.0)
  * `findAllByTypesAndDiscussionAndTeam` **(Generic / Templated Code)** (Impact: 10.8)
  * `findByNameOrFnameContainingAndTypes` **(Generic / Templated Code)** (Impact: 10.1)
  * `findByNameOrFNameAndTypesNotInIds` **(Generic / Templated Code)** (Impact: 7.7)
  * `findOneByNameAndType` **(Generic / Templated Code)** (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 30`, `args: 156`, `func_start: 156`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `planned_debt: 1`
* *Architecture:* `api: 156`, `concurrency: 113`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000698
  * `Imports (Out-Degree: 2):` updater, IBaseModel, core-typings, mongodb
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/apps-engine/src/server/managers/AppListenerManager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.388)
- **Top Global Matches:** file_cluster_16: 7.388, file_cluster_10: 9.214, file_cluster_15: 9.498
- **Magnitude:** 724.06 | **LOC:** 1284 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.316; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (95.8%), Guard Balance (formerly Safety Score) (48.9%), Mutation Surface (formerly State Flux) (45.2%)
- **Documentation Coverage:** 98.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeListener` **(Type Conversions)** (Impact: 98.2)
    * *Intent:* /* eslint-disable-next-line complexity */
  * `executeUIKitInteraction` **(Defensive Guards)** (Impact: 25.0)
  * `executePostMessageSent` **(Stateful Encapsulated Methods)** (Impact: 17.7)
  * `executePreMessageSentPrevent` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* // Messages
  * `executePreMessageDeletePrevent` **(Stateful Encapsulated Methods)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 225
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 314`, `args: 82`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`
* *Architecture:* `api: 10`, `concurrency: 165`, `import: 22`
* *Defense:* `safety: 41`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.316
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.019768
  * `Imports (Out-Degree: 7):` email, exceptions, externalComponent, livechat, ILivechatEventContext, messages, metadata, rooms...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 710.54 | **LOC:** 35527 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/agenda/src/Agenda.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.463)
- **Top Global Matches:** file_cluster_12: 7.463, file_cluster_5: 8.12, file_cluster_0: 9.667
- **Magnitude:** 699.36 | **LOC:** 985 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.467; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (89.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_findAndLockNextJob` **(Defensive Guards)** (Impact: 29.2)
  * `constructor` **(Compute Cores)** (Impact: 18.4)
  * `define` **(Generic / Templated Code)** (Impact: 16.8)
  * `mongo` **(Defensive Guards)** (Impact: 14.2)
  * `processJobs` **(Compute Cores)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 203
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 159`, `args: 64`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 70`
* *Architecture:* `io: 21`, `api: 34`, `concurrency: 88`, `import: 12`
* *Defense:* `safety: 52`, `doc: 4`, `sync_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.467
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001246
  * `Imports (Out-Degree: 7):` Job, JobProcessingQueue, createJob, IJob, JobDefinition, hasMongoProtocol, noCallback, debug...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/model-typings/src/models/ISubscriptionsModel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.7)
- **Top Global Matches:** file_cluster_0: 8.7, file_cluster_5: 9.585, file_cluster_12: 12.175
- **Magnitude:** 673.04 | **LOC:** 348 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (96.5%), Complexity Load (formerly Cognitive Load) (91.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findConnectedUsersExcept` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `setAsReadByRoomIdAndUserId` **(Generic / Templated Code)** (Impact: 10.1)
  * `findByRoomIdAndNotAlertOrOpenExcludingUserIds` **(Generic / Templated Code)** (Impact: 7.4)
  * `incGroupMentionsAndUnreadForRoomIdExcludingUserId` **(Generic / Templated Code)** (Impact: 7.0)
  * `incUserMentionsAndUnreadForRoomIdAndUserIds` **(Generic / Templated Code)** (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 30`, `args: 147`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 142`, `concurrency: 101`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000349
  * `Imports (Out-Degree: 2):` DocumentWithProjection, IBaseModel, core-typings, mongodb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/random/src/RandomGenerator.ts` (TYPESCRIPT) | Magnitude: 29.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 13, args: 8, func_start: 8
- `packages/ui-contexts/src/UserContext.ts` (TYPESCRIPT) | Magnitude: 10.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 80, indent_tabs: 39, args: 37, closures: 24
- `packages/apps-engine/deno-runtime/lib/messenger.ts` (TYPESCRIPT) | Magnitude: 193.36 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 99, structural_boundaries: 75, concurrency: 33, api: 28
- `packages/apps-engine/deno-runtime/handlers/app/handleSetStatus.ts` (TYPESCRIPT) | Magnitude: 12.58 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 11, import: 7, branch: 5
- `ee/packages/pdf-worker/src/templates/ChatTranscript/ChatTranscript.stories.tsx` (TYPESCRIPT) | Magnitude: 3.84 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 12, import: 6, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/ui-contexts/src/UserCardContext.ts` (TYPESCRIPT) | Magnitude: 17.36 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 20, indent_tabs: 10, args: 8, closures: 7
- `packages/message-parser/tests/phoneNumber.test.ts` (TYPESCRIPT) | Magnitude: 15.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 3, import: 2, args: 1
- `packages/ui-contexts/src/AuthorizationContext.ts` (TYPESCRIPT) | Magnitude: 29.8 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 62, args: 38, indent_tabs: 27, closures: 23
- `packages/apps-engine/tests/test-data/utilities.ts` (TYPESCRIPT) | Magnitude: 312.06 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 610, structural_boundaries: 182, args: 86, func_start: 77
- `packages/apps-engine/tests/server/managers/AppRuntimeManager.test.ts` (TYPESCRIPT) | Magnitude: 42.78 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 59, args: 35, closures: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/apps-engine/deno-runtime/lib/room.ts` (TYPESCRIPT) | Magnitude: 78.04 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 65, api: 22, structural_boundaries: 21, branch: 16
- `packages/media-signaling/src/lib/media/MediaStreamManager.ts` (TYPESCRIPT) | Magnitude: 80.76 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 36, args: 22, branch: 17
- `packages/apps-engine/tests/server/managers/AppListenerManager.test.ts` (TYPESCRIPT) | Magnitude: 5.62 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 15, args: 8, import: 6
- `packages/apps-engine/src/server/bridges/AppActivationBridge.ts` (TYPESCRIPT) | Magnitude: 36.7 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 20, concurrency: 15, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/apps-engine/src/server/managers/AppVideoConfProvider.ts` (TYPESCRIPT) | Magnitude: 73.3 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 83, structural_boundaries: 37, concurrency: 24, api: 13
- `packages/rest-typings/src/v1/statistics.ts` (TYPESCRIPT) | Magnitude: 8.14 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 30, core_var_decl: 13, design_pascal_case: 11
- `packages/core-typings/src/ILivechatDepartment.ts` (TYPESCRIPT) | Magnitude: 17.78 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 35, branch: 21, structural_boundaries: 4, api: 2
- `scripts/todo-issue/src/github.ts` (TYPESCRIPT) | Magnitude: 181.7 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 201, structural_boundaries: 60, planned_debt: 49, concurrency: 41
- `ee/packages/omni-core-ee/src/isDepartmentCreationAvailable.spec.ts` (TYPESCRIPT) | Magnitude: 66.22 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 26, indent_tabs: 20, concurrency: 13, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `apps/uikit-playground/src/Components/CodeEditor/Extensions/payloadLinter.ts` (TYPESCRIPT) | Magnitude: 38.08 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 46, branch: 14, structural_boundaries: 14, state_mutation: 7
- `packages/apps-engine/src/server/bridges/IInternalFederationBridge.ts` (TYPESCRIPT) | Magnitude: 7.28 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 3, structural_boundaries: 2, args: 2, func_start: 2
- `packages/core-services/src/types/IOmnichannelTranscriptService.ts` (TYPESCRIPT) | Magnitude: 4.72 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 4, api: 2, core_var_decl: 2
- `packages/apps-engine/src/server/bridges/AppBridges.ts` (TYPESCRIPT) | Magnitude: 62.48 | Delta: **0.195** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 60, indent_tabs: 53, api: 30, args: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/ui-voip/src/providers/MediaCallLogger.ts` (TYPESCRIPT) | Magnitude: 19.8 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 9, args: 5, func_start: 5
- `packages/agenda/src/lib/noCallback.ts` (TYPESCRIPT) | Magnitude: 4.8 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/apps-engine/deno-runtime/lib/parseArgs.ts` (TYPESCRIPT) | Magnitude: 3.78 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 4, api: 2, branch: 1
- `ee/packages/media-calls/src/definition/IMediaCallAgent.ts` (TYPESCRIPT) | Magnitude: 29.46 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 13, api: 9, args: 8
- `packages/tools/src/objectMap.spec.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 87, core_var_decl: 21, design_snake_case: 21, structural_boundaries: 17
- `ee/packages/pdf-worker/src/strategies/ChatTranscript.ts` (TYPESCRIPT) | Magnitude: 58.42 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 24, branch: 22, args: 8
- `packages/apps-engine/tests/test-data/bridges/commandBridge.ts` (TYPESCRIPT) | Magnitude: 54.82 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 20, concurrency: 12, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/apps-engine/src/server/managers/AppVideoConfProviderManager.ts` (TYPESCRIPT) | Magnitude: 139.04 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 157, structural_boundaries: 45, branch: 29, args: 17
- `packages/apps-engine/src/server/accessors/EmailCreator.ts` (TYPESCRIPT) | Magnitude: 8.74 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 7, api: 3, import: 3
- `packages/apps-engine/src/server/accessors/SlashCommandsExtend.ts` (TYPESCRIPT) | Magnitude: 9.74 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 7, api: 3, concurrency: 3
- `packages/apps-engine/src/server/accessors/ApiExtend.ts` (TYPESCRIPT) | Magnitude: 8.74 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 7, api: 3, import: 3
- `packages/apps-engine/src/server/accessors/UploadCreator.ts` (TYPESCRIPT) | Magnitude: 29.08 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 15, import: 5, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/ui-voip/src/views/MediaCallWidget/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 7, structural_boundaries: 7, api: 7, import: 7
- `packages/core-typings/src/ldap/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6
- `packages/media-signaling/src/definition/signals/server/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6
- `packages/fuselage-ui-kit/src/stories/payloads/index.ts` (TYPESCRIPT) | Magnitude: 25.2 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 10, import: 10
- `apps/uikit-playground/src/Components/FlowContainer/UIKitWrapper/UIKitWrapper.scss` (CSS) | Magnitude: 0.68 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 5, indent_spaces: 5, class_start: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/core-typings/src/omnichannel/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, api: 6, import: 6
- `packages/media-signaling/src/definition/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, api: 6, import: 6
- `packages/core-typings/src/ILivechatAgent.ts` (TYPESCRIPT) | Magnitude: 18.46 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 9, branch: 6, api: 3
- `packages/fuselage-ui-kit/src/stories/payloads/conditional.ts` (TYPESCRIPT) | Magnitude: 16.38 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 6, immutability_locks: 2, safety: 1
- `packages/apps/src/index.ts` (TYPESCRIPT) | Magnitude: 18.12 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ee/apps/omnichannel-transcript/src/i18n.ts` (TYPESCRIPT) | Magnitude: 16.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 8, import: 5, decorators: 3
- `packages/release-changelog/src/getGitHubInfo.ts` (TYPESCRIPT) | Magnitude: 50.86 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 140, structural_boundaries: 21, branch: 16, args: 11
- `packages/core-typings/src/ldap/ILDAPLoginRequest.ts` (TYPESCRIPT) | Magnitude: 14.12 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 4, branch: 2, structural_boundaries: 2, class_start: 1
- `packages/apps-engine/deno-runtime/lib/accessors/builders/LivechatMessageBuilder.ts` (TYPESCRIPT) | Magnitude: 131.3 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 137, structural_boundaries: 59, api: 34, args: 31
- `packages/core-typings/src/federation/v1/IFederationEvent.ts` (TYPESCRIPT) | Magnitude: 16.2 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, class_start: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ee/packages/abac/src/index.ts` (TYPESCRIPT) | Magnitude: 524.7 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 472, structural_boundaries: 158, branch: 144, concurrency: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/omni-core/src/visitor/create.spec.ts` (TYPESCRIPT) | Magnitude: 331.19 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 585, core_var_decl: 90, structural_boundaries: 74, test: 74
- `ee/packages/federation-matrix/src/helpers/createOrUpdateFederatedUser.spec.ts` (TYPESCRIPT) | Magnitude: 100.58 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 75, structural_boundaries: 27, decorators: 24, test: 23
- `ee/packages/omnichannel-services/src/OmnichannelTranscript.spec.ts` (TYPESCRIPT) | Magnitude: 142.81 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 137, test: 50, structural_boundaries: 36, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/apps-engine/src/server/managers/AppLicenseManager.ts` (TYPESCRIPT) | Magnitude: 62.68 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 24, branch: 18, import: 8
- `packages/rest-typings/src/default/index.ts` (TYPESCRIPT) | Magnitude: 16.84 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 13, branch: 9, generics: 3
- `packages/ui-client/src/components/CustomScrollbars/CustomScrollbars.tsx` (TYPESCRIPT) | Magnitude: 25.96 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 28, structural_boundaries: 18, branch: 11, core_var_decl: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ee/packages/federation-matrix/src/FederationMatrix.ts` -> Churn: **77.8%** | Cog Load: 89.8476% | Debt: 11.0874%
- `ee/packages/federation-matrix/src/events/member.ts` -> Churn: **66.33%** | Cog Load: 75.5901% | Debt: 14.6746%
- `ee/packages/federation-matrix/tests/end-to-end/dms.spec.ts` -> Churn: **66.33%** | Cog Load: 100.0% | Debt: 0.0%
- `ee/packages/federation-matrix/tests/end-to-end/room.spec.ts` -> Churn: **65.08%** | Cog Load: 98.6229% | Debt: 0.0%
- `packages/media-signaling/src/lib/Call.ts` -> Churn: **59.43%** | Cog Load: 57.845% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/apps-engine/src/server/AppManager.ts` -> **Douglas Gubert** (100.0% isolated ownership) | Magnitude: 1008.88
- `ee/packages/federation-matrix/tests/end-to-end/ban.spec.ts` -> **Guilherme Gazzo** (100.0% isolated ownership) | Magnitude: 771.53
- `packages/omni-core/src/visitor/create.ts` -> **Kevin Aleman** (100.0% isolated ownership) | Magnitude: 753.69
- `packages/apps-engine/src/server/managers/AppListenerManager.ts` -> **Douglas Gubert** (100.0% isolated ownership) | Magnitude: 724.06
- `ee/packages/abac/src/index.ts` -> **Kevin Aleman** (100.0% isolated ownership) | Magnitude: 524.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/apps-engine/src/server/AppManager.ts` -> **Severity: 0.249** (Bridge: 0.0025 * Flux: 98.4844%)
- `packages/apps-engine/src/server/managers/AppAccessorManager.ts` -> **Severity: 0.126** (Bridge: 0.0013 * Flux: 98.4303%)
- `packages/apps-engine/src/server/managers/AppApi.ts` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 97.2722%)
- `packages/apps-engine/src/server/runtime/deno/AppsEngineDenoRuntime.ts` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 98.4855%)
- `packages/apps-engine/src/server/managers/AppVideoConfProviderManager.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 89.4248%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/apps-engine/src/server/runtime/AppsEngineRuntime.ts` -> **Severity: 1.815** (Embedded: 0.0227 * Error Risk: 80.0%)
- `packages/core-typings/src/utils.ts` -> **Severity: 1.688** (Embedded: 0.0211 * Error Risk: 80.0%)
- `packages/model-typings/src/models/IBaseModel.ts` -> **Severity: 1.483** (Embedded: 0.0279 * Error Risk: 53.1311%)
- `packages/apps-engine/src/server/AppManager.ts` -> **Severity: 1.457** (Embedded: 0.0274 * Error Risk: 53.1407%)
- `packages/apps-engine/src/server/logging/AppConsole.ts` -> **Severity: 1.347** (Embedded: 0.0199 * Error Risk: 67.6344%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/rest-typings/src/v1/Ajv.ts` -> **Severity: 2760.3** (Blast Radius: 27.603 * Doc Risk: 100.0%)
- `packages/model-typings/src/models/IBaseModel.ts` -> **Severity: 1165.5** (Blast Radius: 11.655 * Doc Risk: 100.0%)
- `packages/models/src/models/BaseRaw.ts` -> **Severity: 990.911** (Blast Radius: 10.47 * Doc Risk: 94.6429%)
- `packages/model-typings/src/updater.ts` -> **Severity: 739.215** (Blast Radius: 10.349 * Doc Risk: 71.4286%)
- `packages/core-services/src/types/ServiceClass.ts` -> **Severity: 690.0** (Blast Radius: 6.9 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 1085 literal sites + 2 sites through wrappers = 1087

- `queryCapabilities` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/mock-providers/src/MockedAppRootBuilder.tsx`
- `queryPreferences` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/mock-providers/src/MockedAppRootBuilder.tsx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12957 call pairs -- scoped 26.8%, unique 0.0%, ambiguous 22.9%, external 50.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 12735 | 27.1% | 0.0% | 23.0% | 49.9% |
| javascript | 199 | 3.0% | 0.0% | 21.1% | 75.9% |
| shell | 23 | 43.5% | 0.0% | 0.0% | 56.5% |

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
