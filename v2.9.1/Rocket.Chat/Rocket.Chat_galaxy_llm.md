# ARCHITECTURAL_BRIEF: Rocket.Chat
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/RocketChat/Rocket.Chat.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 8899 analyzed artifact(s), 608032 LOC.
- **Load-bearing artifact:** `apps/meteor/server/models.ts` -- 817 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `apps/meteor/app/ui/client/lib/codeMirror/codeMirror.ts` -- pulls in 141 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 9672 |
| Analyzed Artifacts (Scanned) | 8899 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 773 |
| Total LOC | 608032 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 92.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8154 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1147 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 10.3878 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1188 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 8186 | 565281 | 92.0% |
| JSON | 189 | 7400 | 2.1% |
| JAVASCRIPT | 138 | 13881 | 1.6% |
| MARKDOWN | 118 | 0 | 1.3% |
| CSS | 95 | 18436 | 1.1% |
| PLAINTEXT | 90 | 10 | 1.0% |
| XML | 42 | 735 | 0.5% |
| YAML | 15 | 995 | 0.2% |
| DOCKERFILE | 8 | 552 | 0.1% |
| SHELL | 5 | 359 | 0.1% |
| HTML | 5 | 151 | 0.1% |
| CSV | 4 | 13 | 0.0% |
| PHP | 3 | 204 | 0.0% |
| BATCH | 1 | 15 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.102`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.10; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 20%, Declarative / Non-Code 18%, Generic / Templated Code Files 17%, Callbacks & Closures Files 16%, Large Core Modules (2) 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8685 | 97.6% |
| Unknown | 10 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 198 | 2.2% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 773*

**Composition by Extension & Reason:**
- `.ts`: 152x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 6 exceeds 500 chars), 2x Packed Payload Guard (Impossible Density: 3.01 hits/line)
- `.md`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 35527 LOC exceeds safe regex boundaries)
- `.json`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 4808 LOC), 2x Excluded (Massive Static Asset Blob: 2720 LOC)
- `.snap`: 45x Excluded (Unsupported Extension: '.snap'), 19x Unsupported Format (.snap), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `no_extension`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.sublime-project')
- `.png`: 44x Excluded (Explicitly Denied Extension: '.png')
- `.ttf`: 44x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 53, Signals: 0)
- `.woff2`: 22x Excluded (Explicitly Denied Extension: '.woff2')
- `.tsx`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 10 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.woff`: 21x Excluded (Explicitly Denied Extension: '.woff')
- `.mp3`: 17x Excluded (Explicitly Denied Extension: '.mp3')
- `.txt`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 121 LOC), 1x Packed Payload Guard (Impossible Density: 3.40 hits/line)
- `.zip`: 8x Excluded (Explicitly Denied Extension: '.zip')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.6 | 6.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 19.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 24.7 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.1 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 76.2 | 5.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2956 | 1214 | 1 | `apps/meteor/client/lib/federation/Federation.spec.ts` |
| cleanup | 553 | 250 | 0 | `apps/meteor/tests/e2e/federation/tests/channel/public.spec.ts` |
| guards | 20302 | 3592 | 5 | `ee/packages/federation-matrix/tests/end-to-end/messaging.spec.ts` |
| danger | 8630 | 1962 | 2 | `ee/packages/abac/src/service.spec.ts` |
| concurrency | 56719 | 3279 | 12 | `apps/meteor/tests/end-to-end/api/livechat/00-rooms.ts` |
| connectivity | 22624 | 6997 | 5 | `packages/models/src/models/Users.ts` |
| io | 5358 | 751 | 0 | `apps/meteor/app/emoji-emojione/client/people-sprites.css` |
| crypto | 9 | 4 | 0 | `packages/node-poplib/src/index.js` |
| ipc | 139 | 58 | 0 | `apps/meteor/tests/end-to-end/api/chat.ts` |
| time | 3019 | 684 | 0 | `apps/meteor/tests/end-to-end/api/livechat/17-dashboards-ee.ts` |
| serialization | 797 | 277 | 0 | `apps/meteor/tests/end-to-end/api/methods.ts` |
| regex | 1338 | 508 | 0 | `apps/meteor/app/markdown/lib/parser/original/markdown.js` |
| events | 4224 | 894 | 1 | `packages/node-poplib/src/index.js` |
| tests | 41657 | 981 | 2 | `apps/meteor/tests/end-to-end/api/users.ts` |
| docs | 2391 | 908 | 1 | `packages/eslint-config/index.js` |
| debt | 2360 | 768 | 0 | `apps/meteor/tests/unit/app/importer/server/userConverter.spec.ts` |
| mutation | 88113 | 6816 | 23 | `apps/meteor/tests/end-to-end/api/livechat/00-rooms.ts` |
| dead_code | 1169 | 567 | 0 | `apps/meteor/app/ui/client/lib/codeMirror/codeMirror.ts` |
| credential | 93 | 29 | 0 | `packages/message-parser/tests/link.test.ts` |
| threat | 1018 | 401 | 0 | `packages/apps-engine/src/server/managers/AppListenerManager.ts` |
| ml_ai | 601 | 239 | 0 | `apps/meteor/tests/end-to-end/api/rooms.ts` |
| ui | 20844 | 2932 | 7 | `apps/meteor/client/views/admin/integrations/outgoing/OutgoingWebhookForm.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `apps/meteor/app/emoji-emojione/client/people-sprites.css` (Hits: 911)
- `apps/meteor/app/emoji-emojione/client/activity-sprites.css` (Hits: 221)
- `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts` (Hits: 186)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **models.ts** (`apps/meteor/server/models.ts`) — 817 inbound connections
2. **meteor.ts** (`apps/meteor/tests/mocks/client/meteor.ts`) — 445 inbound connections
3. **mongodb.ts** (`apps/meteor/tests/mocks/server/mongodb.ts`) — 325 inbound connections
4. **notifyListener.ts** (`apps/meteor/app/lib/server/lib/notifyListener.ts`) — 169 inbound connections
5. **hasPermission.ts** (`apps/meteor/app/authorization/server/functions/hasPermission.ts`) — 147 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **codeMirror.ts** (`apps/meteor/app/ui/client/lib/codeMirror/codeMirror.ts`) — 141 outbound dependencies
2. **importPackages.ts** (`apps/meteor/server/importPackages.ts`) — 83 outbound dependencies
3. **modelClasses.ts** (`packages/models/src/modelClasses.ts`) — 75 outbound dependencies
4. **i18n.ts** (`apps/meteor/server/lib/i18n.ts`) — 70 outbound dependencies
5. **index.ts** (`packages/rest-typings/src/index.ts`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `loadAPI` **(I/O & Config Routines)** (@ `apps/meteor/ee/server/apps/communication/rest.ts`) -> Impact: **225.7** | LOC: 1233
- `addManagementRoutes` **(I/O & Config Routines)** (@ `apps/meteor/ee/server/apps/communication/rest.ts`) -> Impact: **224.6** | LOC: 1212
- `getCharset` **(Many-Argument Workhorses)** (@ `apps/meteor/server/services/messages/hooks/AfterSaveOEmbed.ts`) -> Impact: **182.6** | LOC: 327
  * *Intent:* // Detect encoding // Priority: // Detected == HTTP Header > Detected == HTML meta > HTTP Header > HTML meta > Detected > Default (utf-8) // See also:...
- `useComposerBoxPopup` **(Defensive Guards)** (@ `apps/meteor/client/views/room/composer/hooks/useComposerBoxPopup.ts`) -> Impact: **151.9** | LOC: 237
- `executeTriggerUrl` **(Many-Argument Workhorses)** (@ `apps/meteor/app/integrations/server/lib/triggerHandler.ts`) -> Impact: **151.3** | LOC: 297
- `saveUserProfile` **(Many-Argument Workhorses)** (@ `apps/meteor/server/methods/saveUserProfile.ts`) -> Impact: **127.1** | LOC: 172
- `getInitialValue` **(Defensive Guards)** (@ `apps/meteor/client/views/admin/integrations/outgoing/EditOutgoingWebhook.tsx`) -> Impact: **115.9** | LOC: 31
- `saveDepartment` **(Many-Argument Workhorses)** (@ `apps/meteor/app/livechat/server/lib/departmentsLib.ts`) -> Impact: **114.2** | LOC: 128
  * *Intent:* /** */
- `isSettingRange` **(Compute Cores)** (@ `packages/core-typings/src/ISetting.ts`) -> Impact: **111.0** | LOC: 99
- `reducer` **(Many-Argument Workhorses)** (@ `apps/uikit-playground/src/Context/reducer.ts`) -> Impact: **110.3** | LOC: 231

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `apps/meteor/tests/end-to-end/api/livechat` | 28 | 84656.73 | 100.0% | 0.0% |
| `apps/meteor/tests/end-to-end/api` | 45 | 62037.07 | 83.34% | 0.0% |
| `ee/packages/federation-matrix/tests/end-to-end` | 5 | 50351.31 | 98.18% | 0.0% |
| `ee/packages/federation-matrix/docker-compose/traefik/certs` | 6 | 30000.0 | 0.0% | 0.0% |
| `apps/meteor/tests/e2e` | 70 | 22378.07 | 26.6% | 0.0% |
| `ee/packages/federation-matrix/src/helpers` | 8 | 19795.29 | 33.48% | 3.36% |
| `apps/meteor/tests/e2e/omnichannel` | 55 | 17049.29 | 43.64% | 0.0% |
| `packages/models/src/models` | 78 | 10935.5 | 25.48% | 2.63% |
| `apps/meteor/tests/e2e/federation/tests/messaging` | 4 | 8012.07 | 100.0% | 0.0% |
| `apps/meteor/server/settings` | 35 | 7149.84 | 12.0% | 3.11% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `apps/meteor/definition/externals/emojione.d.ts` -> **100.0%** Exposure
- `apps/meteor/definition/externals/meteor/accounts-base.d.ts` -> **100.0%** Exposure
- `apps/meteor/definition/externals/meteor/ddp-common.d.ts` -> **100.0%** Exposure
- `packages/core-services/src/types/IFederationService.ts` -> **100.0%** Exposure
- `apps/meteor/definition/externals/meteor/mongo.d.ts` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `apps/meteor/app/custom-oauth/server/transform_helpers.js` -> **100.0%** Exposure
- `apps/meteor/app/irc/server/servers/RFC2813/parseMessage.js` -> **100.0%** Exposure
- `apps/meteor/app/markdown/lib/parser/filtered/filtered.js` -> **100.0%** Exposure
- `apps/meteor/packages/meteor-cookies/cookies.js` -> **100.0%** Exposure
- `apps/meteor/packages/rocketchat-livechat/assets/rocket-livechat.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `apps/meteor/tests/unit/app/lib/server/apps/disableAppsWithAddonsCallback.spec.ts` -> **0** Orphaned Functions | **21** Duplicates
- `apps/meteor/definition/externals/meteor/accounts-base.d.ts` -> **18** Orphaned Functions | **0** Duplicates
- `ee/packages/abac/src/service.spec.ts` -> **15** Orphaned Functions | **2** Duplicates
- `packages/apps-engine/tests/server/accessors/AppAccessors.test.ts` -> **16** Orphaned Functions | **0** Duplicates
- `apps/meteor/packages/rocketchat-livechat/assets/rocket-livechat.js` -> **15** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/ui-client/src/components/PasswordVerifier/PasswordVerifiers.spec.tsx` -> **100.0%** Exposure
- `packages/apps-engine/tests/test-data/bridges/cloudBridge.ts` -> **99.9997%** Exposure
- `apps/meteor/server/configuration/pushNotification.ts` -> **99.7127%** Exposure
- `apps/meteor/tests/end-to-end/api/livechat/11-email-inbox.ts` -> **99.1938%** Exposure
- `apps/meteor/tests/unit/app/apps/server/mocks/models/Rooms.mock.js` -> **90.5779%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18287` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ee/packages/federation-matrix/tests/end-to-end/messaging.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 46542.72 | **LOC:** 1388 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` file.helper, messages.helper, rooms.helper, users.helper, constants, config, synapse-client, core-typings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 19383.98 | **LOC:** 1751 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.2%), Guard Balance (formerly Safety Score) (34.2%), Complexity Load (formerly Cognitive Load) (20.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 154`, `args: 82`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 186`, `concurrency: 128`, `import: 1`
* *Defense:* `safety: 18`, `test: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` message.parsers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/methods.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 15945.05 | **LOC:** 3659 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (81.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.5%), Guard Balance (formerly Safety Score) (22.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 149 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 932
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 670`, `args: 363`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 207`, `planned_debt: 2`
* *Architecture:* `io: 13`, `concurrency: 187`, `import: 16`
* *Defense:* `safety: 33`, `test: 931`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` api-data, chat.helper, constants, rooms, permissions.helper, rooms.helper, user, users.helper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/contacts.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 14147.43 | **LOC:** 1882 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (20.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 296 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 1859
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 508`, `args: 173`, `func_start: 101`
* *Risk/State:* `state_mutation: 152`
* *Architecture:* `concurrency: 379`, `import: 13`
* *Defense:* `safety: 41`, `test: 540`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` api-data, custom-fields, rooms, users, permissions.helper, users.helper, validation.helper, constants...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/11-livechat.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 10590.04 | **LOC:** 845 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (21.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 191 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 1288
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 389`, `args: 112`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 85`
* *Architecture:* `io: 8`, `concurrency: 333`, `import: 14`
* *Defense:* `safety: 53`, `test: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sleep, api-data, custom-fields, department, rooms, users, utils, permissions.helper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/19-business-hours.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 7840.79 | **LOC:** 903 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (7.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (4.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 102 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 765
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 299`, `args: 67`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`
* *Architecture:* `concurrency: 255`, `import: 16`
* *Defense:* `safety: 62`, `test: 220`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sleep, api-data, businessHours, department, rooms, users, permissions.helper, user...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/17-dashboards-ee.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 6595.49 | **LOC:** 822 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.4%), Guard Balance (formerly Safety Score) (12.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 100 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 723
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 271`, `args: 98`, `func_start: 77`
* *Risk/State:* `state_mutation: 70`
* *Architecture:* `concurrency: 223`, `import: 9`
* *Defense:* `safety: 44`, `test: 269`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api-data, department, rooms, permissions.helper, utils, constants, core-typings, chai...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server-fetch/tests/checkForSsrf.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5894.41 | **LOC:** 554 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (14.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 163`, `args: 124`, `func_start: 27`
* *Risk/State:* None
* *Architecture:* `io: 116`, `concurrency: 64`, `import: 2`
* *Defense:* `safety: 12`, `test: 297`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` checkForSsrf, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/ee/server/services/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/hs1/hs1.signing.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/ca/rootCA.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/element-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/element.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/hs1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/hs1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/rc1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/rc1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/incoming-integrations.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4968.92 | **LOC:** 1658 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (90.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.3%), Guard Balance (formerly Safety Score) (20.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 66 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 509
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 433`, `args: 221`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 85`
* *Architecture:* `concurrency: 179`, `import: 14`
* *Defense:* `safety: 19`, `test: 433`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api-data, integration.helper, permissions.helper, rooms.helper, teams.helper, user, users.helper, api-client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/00-rooms.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4830.54 | **LOC:** 3861 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.0%), Guard Balance (formerly Safety Score) (23.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSubscriptionForRoom` **(Callbacks & Closures)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 627 instances
* *Amplified Cascading Flux:* 84 instances
* *Concurrency (weighted view):* 4249
* *State Mutation (weighted view):* 502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 1354`, `args: 423`, `func_start: 206`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 334`, `planned_debt: 5`
* *Architecture:* `io: 24`, `concurrency: 1114`, `import: 26`
* *Defense:* `safety: 168`, `test: 928`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` definition, api-data, apps-data, custom-fields, department, priorities, rooms, tags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/10-departments.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4721.62 | **LOC:** 1023 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (15.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 154 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 1045
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 351`, `args: 106`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`
* *Architecture:* `concurrency: 275`, `import: 14`
* *Defense:* `safety: 19`, `test: 325`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api-data, department, rooms, units, permissions.helper, user, users.helper, constants...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/apps/video-conferences.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4447.5 | **LOC:** 1013 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.2%), Guard Balance (formerly Safety Score) (18.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 113 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 729
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 253`, `args: 110`, `func_start: 23`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `concurrency: 164`, `import: 10`
* *Defense:* `safety: 5`, `test: 313`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api-data, helper, permissions.helper, rooms.helper, user, users.helper, constants, chai...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/24-routing.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3619.44 | **LOC:** 649 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (19.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Concurrency (weighted view):* 623
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 308`, `args: 80`, `func_start: 33`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `concurrency: 283`, `import: 12`
* *Defense:* `safety: 31`, `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api-data, rooms, permissions.helper, user, users.helper, constants, faker, api-client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/client/views/hooks/useMemberList.spec.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3487.74 | **LOC:** 404 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (53.8%), Mutation Surface (formerly State Flux) (45.3%), Guard Balance (formerly Safety Score) (31.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 130`, `args: 68`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 7`
* *Architecture:* `concurrency: 38`, `import: 6`
* *Defense:* `safety: 28`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` useMembersList, core-typings, mock-providers, ui-contexts, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/ee/server/hooks/federation/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3348.24 | **LOC:** 371 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 38.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.055; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 232
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 98`, `args: 24`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `dead_code: 3`, `planned_debt: 6`
* *Architecture:* `concurrency: 57`, `import: 15`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` notifyListener, callbacks, afterBanFromRoomCallback, afterLeaveRoomCallback, afterRemoveFromRoomCallback, afterUnbanFromRoomCallback, beforeAddUserToRoom, beforeChangeRoomRole...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ee/packages/federation-matrix/src/FederationMatrix.ts` -> Churn: **76.24%** | Cog Load: 90.6058% | Debt: 11.3853%
- `ee/packages/federation-matrix/src/events/member.ts` -> Churn: **61.16%** | Cog Load: 77.7882% | Debt: 15.6251%
- `apps/meteor/server/services/room/service.ts` -> Churn: **58.67%** | Cog Load: 100.0% | Debt: 11.0189%
- `packages/media-signaling/src/lib/Call.ts` -> Churn: **55.33%** | Cog Load: 58.5897% | Debt: 0.0%
- `apps/meteor/app/api/server/v1/rooms.ts` -> Churn: **54.83%** | Cog Load: 54.534% | Debt: 8.0357%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `apps/meteor/tests/end-to-end/api/livechat/contacts.ts` -> **Abhinav Kumar** (100.0% isolated ownership) | Magnitude: 14147.43
- `apps/meteor/tests/end-to-end/api/livechat/11-livechat.ts` -> **Júlia Jaeger Foresti** (100.0% isolated ownership) | Magnitude: 10590.04
- `apps/meteor/tests/end-to-end/api/livechat/19-business-hours.ts` -> **Lucas Pelegrino** (100.0% isolated ownership) | Magnitude: 7840.79
- `apps/meteor/tests/end-to-end/api/livechat/17-dashboards-ee.ts` -> **Kevin Aleman** (100.0% isolated ownership) | Magnitude: 6595.49
- `packages/server-fetch/tests/checkForSsrf.spec.ts` -> **Julio Araujo** (100.0% isolated ownership) | Magnitude: 5894.41

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/apps-engine/src/server/managers/UIActionButtonManager.ts` -> **Severity: 0.249** (Bridge: 0.0027 * Flux: 93.9509%)
- `packages/apps-engine/src/server/AppManager.ts` -> **Severity: 0.235** (Bridge: 0.0024 * Flux: 98.6166%)
- `apps/meteor/app/ui-utils/client/lib/LegacyRoomManager.ts` -> **Severity: 0.17** (Bridge: 0.0018 * Flux: 96.9116%)
- `apps/meteor/client/lib/chats/readStateManager.ts` -> **Severity: 0.083** (Bridge: 0.0018 * Flux: 46.4576%)
- `apps/meteor/app/apps/server/bridges/bridges.js` -> **Severity: 0.076** (Bridge: 0.0008 * Flux: 99.4889%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `apps/meteor/client/lib/streamer/emitter.ts` -> **Severity: 4.359** (Embedded: 0.0675 * Error Risk: 64.5656%)
- `apps/meteor/tests/mocks/client/meteor.ts` -> **Severity: 3.591** (Embedded: 0.0556 * Error Risk: 64.5656%)
- `packages/core-services/src/lib/mongo.ts` -> **Severity: 2.582** (Embedded: 0.0368 * Error Risk: 70.2063%)
- `packages/livechat/src/lib/locale.js` -> **Severity: 2.17** (Embedded: 0.0286 * Error Risk: 75.925%)
- `packages/livechat/src/i18next.ts` -> **Severity: 2.116** (Embedded: 0.0338 * Error Risk: 62.5811%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `apps/meteor/tests/mocks/server/mongodb.ts` -> **Severity: 2420.2** (Blast Radius: 24.202 * Doc Risk: 100.0%)
- `apps/meteor/server/database/utils.ts` -> **Severity: 823.2** (Blast Radius: 9.996 * Doc Risk: 82.3529%)
- `apps/meteor/client/lib/streamer/emitter.ts` -> **Severity: 766.5** (Blast Radius: 7.665 * Doc Risk: 100.0%)
- `packages/livechat/src/i18next.ts` -> **Severity: 566.3** (Blast Radius: 5.663 * Doc Risk: 100.0%)
- `apps/meteor/client/lib/queryKeys.ts` -> **Severity: 479.4** (Blast Radius: 4.794 * Doc Risk: 100.0%)

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
