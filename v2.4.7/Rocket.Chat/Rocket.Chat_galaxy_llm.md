# ARCHITECTURAL_BRIEF: Rocket.Chat
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/Rocket.Chat` |
| **Timestamp** | `2026-08-07T04:10:28.710361+00:00` |
| **Scan Duration** | `30.0s` |
| **Git Branch** | `develop` |
| **Git Commit** | `8ebf44bf53420a9c35a517b419af4100e0070f09` |
| **Git Remote** | `https://github.com/RocketChat/Rocket.Chat.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6981 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Total Artifacts | 9673 |
| Analyzed Artifacts (Scanned) | 7510 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2163 |
| Total LOC | 444603 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 77.6% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1412 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1013 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 6866 | 406502 | 91.4% |
| JSON | 165 | 7199 | 2.2% |
| MARKDOWN | 114 | 0 | 1.5% |
| JAVASCRIPT | 101 | 9611 | 1.3% |
| CSS | 95 | 18441 | 1.3% |
| PLAINTEXT | 90 | 10 | 1.2% |
| XML | 42 | 735 | 0.6% |
| YAML | 15 | 902 | 0.2% |
| DOCKERFILE | 8 | 552 | 0.1% |
| CSV | 4 | 13 | 0.1% |
| HTML | 4 | 118 | 0.1% |
| SHELL | 3 | 316 | 0.0% |
| PHP | 3 | 204 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.902`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 3627 | 48.3% |
| file_cluster_8 | 2305 | 30.7% |
| file_cluster_4 | 827 | 11.0% |
| file_cluster_2 | 299 | 4.0% |
| file_cluster_16 | 101 | 1.3% |
| file_cluster_17 | 99 | 1.3% |
| file_cluster_0 | 34 | 0.5% |
| Unknown | 10 | 0.1% |
| file_cluster_11 | 5 | 0.1% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_9 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 194 | 2.6% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2163*

**Composition by Extension & Reason:**
- `.ts`: 1357x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.tsx`: 155x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 10 exceeds 500 chars), 1x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.json`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 4808 LOC), 2x Excluded (Massive Static Asset Blob: 2720 LOC)
- `.md`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 35527 LOC exceeds safe regex boundaries)
- `.snap`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.snap), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `no_extension`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.sublime-project')
- `.js`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 44x Excluded (Explicitly Denied Extension: '.png')
- `.ttf`: 44x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 22x Excluded (Explicitly Denied Extension: '.woff2')
- `.woff`: 21x Excluded (Explicitly Denied Extension: '.woff')
- `.mp3`: 17x Excluded (Explicitly Denied Extension: '.mp3')
- `.txt`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 8x Excluded (Explicitly Denied Extension: '.zip')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 21.4 | 7.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 17.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.9 | 2.3 | 0.0 |
| API Exposure | 0.0 | 20.0 | 5.2 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 28.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 88.1 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 82.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.1 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 76.2 | 5.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.6 | 26.8 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts` (Hits: 186)
- `apps/meteor/tests/end-to-end/api/chat.ts` (Hits: 143)
- `apps/meteor/tests/unit/app/meteor-accounts-saml/data.ts` (Hits: 78)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **models.ts** (`apps/meteor/server/models.ts`) — 572 inbound connections
2. **meteor.ts** (`apps/meteor/tests/mocks/client/meteor.ts`) — 315 inbound connections
3. **mongodb.ts** (`apps/meteor/tests/mocks/server/mongodb.ts`) — 268 inbound connections
4. **check.mts** (`packages/i18n/src/scripts/check.mts`) — 106 inbound connections
5. **queryKeys.ts** (`packages/ui-voip/src/utils/queryKeys.ts`) — 106 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/core-typings/src/index.ts`) — 115 outbound dependencies
2. **index.ts** (`packages/ui-contexts/src/index.ts`) — 105 outbound dependencies
3. **importPackages.ts** (`apps/meteor/server/importPackages.ts`) — 83 outbound dependencies
4. **index.ts** (`packages/model-typings/src/index.ts`) — 83 outbound dependencies
5. **modelClasses.ts** (`packages/models/src/modelClasses.ts`) — 75 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `loadAPI` (@ `apps/meteor/ee/server/apps/communication/rest.ts`) -> Impact: **258.8** | LOC: 708
- `describe` (@ `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts`) -> Impact: **257.9** | LOC: 898
- `handleError` (@ `apps/meteor/ee/server/apps/communication/rest.ts`) -> Impact: **257.5** | LOC: 681
- `addManagementRoutes` (@ `apps/meteor/ee/server/apps/communication/rest.ts`) -> Impact: **216.8** | LOC: 687
- `actionDefault` (@ `apps/meteor/client/views/room/Header/Omnichannel/QuickActions/hooks/useQuickActions.tsx`) -> Impact: **198.4** | LOC: 288
- `getCharset` (@ `apps/meteor/server/services/messages/hooks/AfterSaveOEmbed.ts`) -> Impact: **194.8** | LOC: 327
  * *Intent:* // Detect encoding // Priority: // Detected == HTTP Header > Detected == HTML meta > HTTP Header > HTML meta > Detected > Default (utf-8) // See also:...
- `describe` (@ `apps/meteor/tests/end-to-end/api/livechat/19-business-hours.ts`) -> Impact: **183.6** | LOC: 866
- `describe` (@ `apps/meteor/tests/end-to-end/api/livechat/11-livechat.ts`) -> Impact: **182.8** | LOC: 815
- `describe` (@ `apps/meteor/tests/end-to-end/api/chat.ts`) -> Impact: **175.9** | LOC: 1612
- `describe` (@ `ee/packages/federation-matrix/src/helpers/message.parsers.spec.ts`) -> Impact: **174.3** | LOC: 507

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ee/packages/federation-matrix/docker-compose/traefik/certs` | 6 | 30000.0 | 0.0% | 0.0% |
| `__monolith__` | 16 | 5141.42 | 3.2% | 1.6% |
| `apps/meteor/ee/server/services` | 7 | 5121.8 | 2.98% | 0.0% |
| `ee/packages/federation-matrix/docker-compose/hs1` | 3 | 5027.64 | 1.67% | 0.0% |
| `ee/packages/federation-matrix/docker-compose/traefik/certs/ca` | 1 | 5000.0 | 0.0% | 0.0% |
| `apps/meteor/tests/end-to-end/api` | 43 | 2775.33 | 75.34% | 0.0% |
| `apps/meteor/tests/end-to-end/api/livechat` | 28 | 2522.34 | 98.52% | 0.0% |
| `packages/models/src/models` | 78 | 1335.49 | 79.1% | 4.13% |
| `apps/meteor/app/apps/server/converters` | 15 | 1182.83 | 71.83% | 9.98% |
| `apps/meteor` | 19 | 981.6 | 8.93% | 15.79% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/livechat/src/components/Modal/manager.js` -> **100.0%** Exposure
- `apps/meteor/app/apps/server/bridges/outboundCommunication.ts` -> **100.0%** Exposure
- `apps/meteor/app/custom-sounds/server/methods/listCustomSounds.ts` -> **100.0%** Exposure
- `apps/meteor/app/discussion/server/hooks/propagateDiscussionMetadata.ts` -> **100.0%** Exposure
- `apps/meteor/app/emoji-custom/server/methods/insertOrUpdateEmoji.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `apps/meteor/app/custom-oauth/server/custom_oauth_server.js` -> **100.0%** Exposure
- `apps/meteor/app/irc/server/irc-bridge/index.js` -> **100.0%** Exposure
- `apps/meteor/app/irc/server/irc-bridge/localHandlers/onCreateRoom.js` -> **100.0%** Exposure
- `apps/meteor/app/irc/server/irc-bridge/localHandlers/onCreateUser.js` -> **100.0%** Exposure
- `apps/meteor/app/irc/server/irc-bridge/localHandlers/onLogin.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `apps/meteor/tests/end-to-end/api/rooms.ts` -> **0** Orphaned Functions | **374** Duplicates
- `apps/meteor/tests/end-to-end/api/livechat/00-rooms.ts` -> **0** Orphaned Functions | **304** Duplicates
- `apps/meteor/tests/end-to-end/api/abac.ts` -> **0** Orphaned Functions | **220** Duplicates
- `apps/meteor/tests/end-to-end/api/methods.ts` -> **0** Orphaned Functions | **197** Duplicates
- `apps/meteor/tests/end-to-end/api/livechat/contacts.ts` -> **0** Orphaned Functions | **193** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/model-typings/src/models/ILivechatRoomsModel.ts`** -> AI Confidence: **99.34%**
2. **`packages/model-typings/src/models/IMessagesModel.ts`** -> AI Confidence: **99.32%**
3. **`apps/meteor/app/authentication/server/startup/index.js`** -> AI Confidence: **99.31%**
4. **`apps/meteor/app/custom-oauth/server/custom_oauth_server.js`** -> AI Confidence: **99.31%**
5. **`apps/meteor/app/emoji-custom/server/startup/emoji-custom.js`** -> AI Confidence: **99.31%**
6. **`apps/meteor/app/irc/server/servers/RFC2813/index.js`** -> AI Confidence: **99.31%**
7. **`apps/meteor/packages/rocketchat-version/plugin/compile-version.js`** -> AI Confidence: **99.31%**
8. **`packages/livechat/src/components/Messages/Message/index.js`** -> AI Confidence: **99.31%**
9. **`packages/livechat/src/components/Messages/MessageList/index.js`** -> AI Confidence: **99.31%**
10. **`apps/meteor/app/2fa/server/code/index.ts`** -> AI Confidence: **99.31%**
11. **`apps/meteor/app/api/server/helpers/parseJsonQuery.ts`** -> AI Confidence: **99.31%**
12. **`apps/meteor/app/api/server/v1/commands.ts`** -> AI Confidence: **99.31%**
13. **`apps/meteor/app/apps/server/bridges/commands.ts`** -> AI Confidence: **99.31%**
14. **`apps/meteor/app/autotranslate/server/autotranslate.ts`** -> AI Confidence: **99.31%**
15. **`apps/meteor/app/autotranslate/server/googleTranslate.ts`** -> AI Confidence: **99.31%**
16. **`apps/meteor/app/channel-settings/server/methods/saveRoomSettings.ts`** -> AI Confidence: **99.31%**
17. **`apps/meteor/app/cloud/server/functions/syncWorkspace/index.ts`** -> AI Confidence: **99.31%**
18. **`apps/meteor/app/crowd/server/crowd.ts`** -> AI Confidence: **99.31%**
19. **`apps/meteor/app/importer-slack/server/SlackImporter.ts`** -> AI Confidence: **99.31%**
20. **`apps/meteor/app/integrations/server/api/api.ts`** -> AI Confidence: **99.31%**
21. **`apps/meteor/app/integrations/server/methods/incoming/addIncomingIntegration.ts`** -> AI Confidence: **99.31%**
22. **`apps/meteor/app/integrations/server/methods/incoming/updateIncomingIntegration.ts`** -> AI Confidence: **99.31%**
23. **`apps/meteor/app/integrations/server/methods/outgoing/updateOutgoingIntegration.ts`** -> AI Confidence: **99.31%**
24. **`apps/meteor/app/livechat/server/hooks/processRoomAbandonment.ts`** -> AI Confidence: **99.31%**
25. **`apps/meteor/app/mail-messages/server/functions/sendMail.ts`** -> AI Confidence: **99.31%**
26. **`apps/meteor/app/push/server/push.ts`** -> AI Confidence: **99.31%**
27. **`apps/meteor/app/reactions/client/methods/setReaction.ts`** -> AI Confidence: **99.31%**
28. **`apps/meteor/app/reactions/server/setReaction.ts`** -> AI Confidence: **99.31%**
29. **`apps/meteor/app/settings/server/SettingsRegistry.ts`** -> AI Confidence: **99.31%**
30. **`apps/meteor/app/slackbridge/server/RocketAdapter.ts`** -> AI Confidence: **99.31%**
31. **`apps/meteor/app/slackbridge/server/SlackAdapter.ts`** -> AI Confidence: **99.31%**
32. **`apps/meteor/app/smarsh-connector/server/functions/generateEml.ts`** -> AI Confidence: **99.31%**
33. **`apps/meteor/client/components/UserCard/UserCard.tsx`** -> AI Confidence: **99.31%**
34. **`apps/meteor/client/components/UserInfo/UserInfo.tsx`** -> AI Confidence: **99.31%**
35. **`apps/meteor/client/components/deviceManagement/DeviceManagementTable/DeviceManagementTable.tsx`** -> AI Confidence: **99.31%**
36. **`apps/meteor/client/components/message/hooks/useNormalizedMessage.ts`** -> AI Confidence: **99.31%**
37. **`apps/meteor/client/components/message/variants/ThreadMessagePreview.tsx`** -> AI Confidence: **99.31%**
38. **`apps/meteor/client/components/message/variants/room/RoomMessageContent.tsx`** -> AI Confidence: **99.31%**
39. **`apps/meteor/client/components/message/variants/thread/ThreadMessageContent.tsx`** -> AI Confidence: **99.31%**
40. **`apps/meteor/client/hooks/notification/useNotification.ts`** -> AI Confidence: **99.31%**
41. **`apps/meteor/client/hooks/roomActions/useVideoCallRoomAction.tsx`** -> AI Confidence: **99.31%**
42. **`apps/meteor/client/meteor/login/facebook.ts`** -> AI Confidence: **99.31%**
43. **`apps/meteor/client/meteor/minimongo/Cursor.ts`** -> AI Confidence: **99.31%**
44. **`apps/meteor/client/meteor/minimongo/LocalCollection.ts`** -> AI Confidence: **99.31%**
45. **`apps/meteor/client/sidebar/RoomList/SidebarItemTemplateWithData.tsx`** -> AI Confidence: **99.31%**
46. **`apps/meteor/client/sidebar/hooks/useRoomList.ts`** -> AI Confidence: **99.31%**
47. **`apps/meteor/client/views/account/security/ChangePassword.tsx`** -> AI Confidence: **99.31%**
48. **`apps/meteor/client/views/admin/ABAC/ABACAttributesTab/AttributesForm.tsx`** -> AI Confidence: **99.31%**
49. **`apps/meteor/client/views/admin/ABAC/ABACLogsTab/LogsPage.tsx`** -> AI Confidence: **99.31%**
50. **`apps/meteor/client/views/admin/ABAC/ABACRoomsTab/RoomsPage.tsx`** -> AI Confidence: **99.31%**
51. **`apps/meteor/client/views/admin/ABAC/ABACSettingTab/SettingField.tsx`** -> AI Confidence: **99.31%**
52. **`apps/meteor/client/views/admin/customUserStatus/CustomUserStatusService.tsx`** -> AI Confidence: **99.31%**
53. **`apps/meteor/client/views/admin/emailInbox/EmailInboxForm.tsx`** -> AI Confidence: **99.31%**
54. **`apps/meteor/client/views/admin/engagementDashboard/channels/ChannelsOverview.tsx`** -> AI Confidence: **99.31%**
55. **`apps/meteor/client/views/admin/engagementDashboard/messages/MessagesPerChannelSection.tsx`** -> AI Confidence: **99.31%**
56. **`apps/meteor/client/views/admin/integrations/incoming/EditIncomingWebhook.tsx`** -> AI Confidence: **99.31%**
57. **`apps/meteor/client/views/admin/integrations/incoming/IncomingWebhookForm.tsx`** -> AI Confidence: **99.31%**
58. **`apps/meteor/client/views/admin/integrations/outgoing/EditOutgoingWebhook.tsx`** -> AI Confidence: **99.31%**
59. **`apps/meteor/client/views/admin/integrations/outgoing/history/HistoryItem.tsx`** -> AI Confidence: **99.31%**
60. **`apps/meteor/client/views/admin/moderation/helpers/ContextMessage.tsx`** -> AI Confidence: **99.31%**
61. **`apps/meteor/client/views/admin/rooms/EditRoom.tsx`** -> AI Confidence: **99.31%**
62. **`apps/meteor/client/views/admin/settings/Setting/Setting.tsx`** -> AI Confidence: **99.31%**
63. **`apps/meteor/client/views/admin/settings/Setting/inputs/CodeMirror/CodeMirror.tsx`** -> AI Confidence: **99.31%**
64. **`apps/meteor/client/views/admin/subscription/components/cards/AppsUsageCard/AppsUsageCard.tsx`** -> AI Confidence: **99.31%**
65. **`apps/meteor/client/views/admin/users/AdminUserForm.tsx`** -> AI Confidence: **99.31%**
66. **`apps/meteor/client/views/admin/users/AdminUserSetRandomPasswordContent.tsx`** -> AI Confidence: **99.31%**
67. **`apps/meteor/client/views/admin/users/UsersTable/UsersTable.tsx`** -> AI Confidence: **99.31%**
68. **`apps/meteor/client/views/admin/users/UsersTable/UsersTableRow.tsx`** -> AI Confidence: **99.31%**
69. **`apps/meteor/client/views/admin/workspace/VersionCard/VersionCard.tsx`** -> AI Confidence: **99.31%**
70. **`apps/meteor/client/views/marketplace/AppDetailsPage/AppDetailsPageHeader.tsx`** -> AI Confidence: **99.31%**
71. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppStatus/AppStatus.tsx`** -> AI Confidence: **99.31%**
72. **`apps/meteor/client/views/marketplace/AppsRoute.tsx`** -> AI Confidence: **99.31%**
73. **`apps/meteor/client/views/marketplace/components/MarketplaceHeader.tsx`** -> AI Confidence: **99.31%**
74. **`apps/meteor/client/views/marketplace/hooks/useAppMenu.tsx`** -> AI Confidence: **99.31%**
75. **`apps/meteor/client/views/navigation/NavigationRegion.tsx`** -> AI Confidence: **99.31%**
76. **`apps/meteor/client/views/navigation/providers/RoomsNavigationProvider.tsx`** -> AI Confidence: **99.31%**
77. **`apps/meteor/client/views/navigation/sidebar/RoomList/SidebarItemWithData.tsx`** -> AI Confidence: **99.31%**
78. **`apps/meteor/client/views/omnichannel/agents/AgentsTable/AgentsTable.tsx`** -> AI Confidence: **99.31%**
79. **`apps/meteor/client/views/omnichannel/agents/AgentsTable/AgentsTableRow.tsx`** -> AI Confidence: **99.31%**
80. **`apps/meteor/client/views/omnichannel/analytics/InterchangeableChart.tsx`** -> AI Confidence: **99.31%**
81. **`apps/meteor/client/views/omnichannel/cannedResponses/components/CannedResponsesComposer/CannedResponsesComposer.tsx`** -> AI Confidence: **99.31%**
82. **`apps/meteor/client/views/omnichannel/cannedResponses/modals/CannedResponseEdit.tsx`** -> AI Confidence: **99.31%**
83. **`apps/meteor/client/views/omnichannel/cannedResponses/modals/CannedResponsesTable.tsx`** -> AI Confidence: **99.31%**
84. **`apps/meteor/client/views/omnichannel/cannedResponses/modals/CreateCannedResponse/CreateCannedResponseModal.tsx`** -> AI Confidence: **99.31%**
85. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessagePreview/OutboundMessagePreview.tsx`** -> AI Confidence: **99.31%**
86. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/forms/RecipientForm/RecipientForm.tsx`** -> AI Confidence: **99.31%**
87. **`apps/meteor/client/views/omnichannel/customFields/CustomFieldsTable.tsx`** -> AI Confidence: **99.31%**
88. **`apps/meteor/client/views/omnichannel/customFields/EditCustomFields.tsx`** -> AI Confidence: **99.31%**
89. **`apps/meteor/client/views/omnichannel/departments/DepartmentsTable/DepartmentsTable.tsx`** -> AI Confidence: **99.31%**
90. **`apps/meteor/client/views/omnichannel/departments/EditDepartmentWithData.tsx`** -> AI Confidence: **99.31%**
91. **`apps/meteor/client/views/omnichannel/directory/chats/ChatInfo/ChatInfo.tsx`** -> AI Confidence: **99.31%**
92. **`apps/meteor/client/views/omnichannel/directory/chats/ChatInfo/RoomEdit/RoomEdit.tsx`** -> AI Confidence: **99.31%**
93. **`apps/meteor/client/views/omnichannel/directory/chats/ChatsTable/ChatsTable.tsx`** -> AI Confidence: **99.31%**
94. **`apps/meteor/client/views/omnichannel/directory/contacts/ContactTable.tsx`** -> AI Confidence: **99.31%**
95. **`apps/meteor/client/views/omnichannel/modals/CloseChatModal.tsx`** -> AI Confidence: **99.31%**
96. **`apps/meteor/client/views/omnichannel/queueList/QueueListTable.tsx`** -> AI Confidence: **99.31%**
97. **`apps/meteor/client/views/omnichannel/routes.ts`** -> AI Confidence: **99.31%**
98. **`apps/meteor/client/views/omnichannel/slaPolicies/SlaEdit.tsx`** -> AI Confidence: **99.31%**
99. **`apps/meteor/client/views/omnichannel/slaPolicies/SlaTable.tsx`** -> AI Confidence: **99.31%**
100. **`apps/meteor/client/views/omnichannel/tags/TagsTable.tsx`** -> AI Confidence: **99.31%**
101. **`apps/meteor/client/views/omnichannel/triggers/EditTrigger.tsx`** -> AI Confidence: **99.31%**
102. **`apps/meteor/client/views/omnichannel/units/UnitEdit.tsx`** -> AI Confidence: **99.31%**
103. **`apps/meteor/client/views/omnichannel/units/UnitsTable.tsx`** -> AI Confidence: **99.31%**
104. **`apps/meteor/client/views/outlookCalendar/OutlookEventsList/OutlookEventsList.tsx`** -> AI Confidence: **99.31%**
105. **`apps/meteor/client/views/room/Header/Omnichannel/QuickActions/hooks/useQuickActions.tsx`** -> AI Confidence: **99.31%**
106. **`apps/meteor/client/views/room/Header/RoomHeader.tsx`** -> AI Confidence: **99.31%**
107. **`apps/meteor/client/views/room/MessageList/MessageListItem.tsx`** -> AI Confidence: **99.31%**
108. **`apps/meteor/client/views/room/body/hooks/useUnreadMessages.ts`** -> AI Confidence: **99.31%**
109. **`apps/meteor/client/views/room/composer/ComposerMessage.tsx`** -> AI Confidence: **99.31%**
110. **`apps/meteor/client/views/room/composer/messageBox/MessageBox.tsx`** -> AI Confidence: **99.31%**
111. **`apps/meteor/client/views/room/composer/messageBox/MessageBoxActionsToolbar/hooks/useAudioMessageAction.ts`** -> AI Confidence: **99.31%**
112. **`apps/meteor/client/views/room/composer/messageBox/MessageBoxActionsToolbar/hooks/useVideoMessageAction.ts`** -> AI Confidence: **99.31%**
113. **`apps/meteor/client/views/room/contextualBar/Info/RoomInfo/RoomInfo.tsx`** -> AI Confidence: **99.31%**
114. **`apps/meteor/client/views/room/contextualBar/MessageSearchTab/MessageSearchTab.tsx`** -> AI Confidence: **99.31%**
115. **`apps/meteor/client/views/room/contextualBar/NotificationPreferences/NotificationPreferencesWithData.tsx`** -> AI Confidence: **99.31%**
116. **`apps/meteor/client/views/room/contextualBar/RoomMembers/RoomMembersWithData.tsx`** -> AI Confidence: **99.31%**
117. **`apps/meteor/client/views/room/hooks/useUserInfoActions/actions/useMuteUserAction.tsx`** -> AI Confidence: **99.31%**
118. **`apps/meteor/ee/app/livechat-enterprise/server/hooks/afterTakeInquiry.ts`** -> AI Confidence: **99.31%**
119. **`apps/meteor/ee/app/livechat-enterprise/server/services/omnichannel.internalService.ts`** -> AI Confidence: **99.31%**
120. **`apps/meteor/server/methods/registerUser.ts`** -> AI Confidence: **99.31%**
121. **`apps/meteor/server/methods/saveUserProfile.ts`** -> AI Confidence: **99.31%**
122. **`apps/meteor/server/modules/notifications/notifications.module.ts`** -> AI Confidence: **99.31%**
123. **`apps/meteor/server/publications/messages.ts`** -> AI Confidence: **99.31%**
124. **`apps/meteor/server/services/media-call/service.ts`** -> AI Confidence: **99.31%**
125. **`apps/meteor/server/services/messages/hooks/AfterSaveOEmbed.ts`** -> AI Confidence: **99.31%**
126. **`apps/meteor/server/services/omnichannel-integrations/providers/twilio.ts`** -> AI Confidence: **99.31%**
127. **`apps/meteor/server/ufs/ufs-server.ts`** -> AI Confidence: **99.31%**
128. **`apps/meteor/server/ufs/ufs-store.ts`** -> AI Confidence: **99.31%**
129. **`ee/packages/abac/src/index.ts`** -> AI Confidence: **99.31%**
130. **`ee/packages/federation-matrix/src/FederationMatrix.ts`** -> AI Confidence: **99.31%**
131. **`ee/packages/federation-matrix/src/events/member.ts`** -> AI Confidence: **99.31%**
132. **`ee/packages/federation-matrix/src/events/message.ts`** -> AI Confidence: **99.31%**
133. **`ee/packages/media-calls/src/server/MediaCallServer.ts`** -> AI Confidence: **99.31%**
134. **`packages/agenda/src/Agenda.ts`** -> AI Confidence: **99.31%**
135. **`packages/agenda/src/Job.ts`** -> AI Confidence: **99.31%**
136. **`packages/apps-engine/deno-runtime/handlers/listener/handler.ts`** -> AI Confidence: **99.31%**
137. **`packages/apps-engine/deno-runtime/handlers/uikit/handler.ts`** -> AI Confidence: **99.31%**
138. **`packages/apps-engine/src/definition/messages/IMessage.ts`** -> AI Confidence: **99.31%**
139. **`packages/apps-engine/src/server/managers/AppLicenseManager.ts`** -> AI Confidence: **99.31%**
140. **`packages/apps-engine/src/server/managers/AppVideoConfProviderManager.ts`** -> AI Confidence: **99.31%**
141. **`packages/apps-engine/src/server/runtime/deno/AppsEngineDenoRuntime.ts`** -> AI Confidence: **99.31%**
142. **`packages/core-typings/src/IRoom.ts`** -> AI Confidence: **99.31%**
143. **`packages/fuselage-ui-kit/src/blocks/VideoConferenceBlock/VideoConferenceBlock.tsx`** -> AI Confidence: **99.31%**
144. **`packages/livechat/src/components/Alert/index.tsx`** -> AI Confidence: **99.31%**
145. **`packages/livechat/src/components/Composer/index.tsx`** -> AI Confidence: **99.31%**
146. **`packages/livechat/src/components/Messages/FileAttachmentIcon/index.tsx`** -> AI Confidence: **99.31%**
147. **`packages/livechat/src/components/Screen/Header.tsx`** -> AI Confidence: **99.31%**
148. **`packages/livechat/src/store/index.tsx`** -> AI Confidence: **99.31%**
149. **`packages/media-signaling/src/lib/Call.ts`** -> AI Confidence: **99.31%**
150. **`packages/models/src/models/BaseRaw.ts`** -> AI Confidence: **99.31%**
151. **`packages/models/src/models/LivechatRooms.ts`** -> AI Confidence: **99.31%**
152. **`packages/models/src/models/Users.ts`** -> AI Confidence: **99.31%**
153. **`packages/server-fetch/src/index.ts`** -> AI Confidence: **99.31%**
154. **`packages/ui-client/src/components/EmojiPicker/index.ts`** -> AI Confidence: **99.31%**
155. **`packages/ui-client/src/components/InfoPanel/index.ts`** -> AI Confidence: **99.31%**
156. **`packages/ui-client/src/components/Modal/GenericModal/GenericModal.tsx`** -> AI Confidence: **99.31%**
157. **`packages/ui-client/src/components/Page/index.ts`** -> AI Confidence: **99.31%**
158. **`packages/ui-voip/src/components/DevicePicker.tsx`** -> AI Confidence: **99.31%**
159. **`packages/ui-voip/src/views/MediaCallWidget/index.ts`** -> AI Confidence: **99.31%**
160. **`packages/web-ui-registration/src/RegisterForm.tsx`** -> AI Confidence: **99.31%**
161. **`packages/web-ui-registration/src/ResetPassword/ResetPasswordPage.tsx`** -> AI Confidence: **99.31%**
162. **`apps/meteor/packages/rocketchat-i18n/package.js`** -> AI Confidence: **99.29%**
163. **`apps/meteor/packages/rocketchat-livechat/package.js`** -> AI Confidence: **99.29%**
164. **`packages/apps-engine/scripts/deno-cache.js`** -> AI Confidence: **99.29%**
165. **`apps/meteor/app/api/server/helpers/isUserFromParams.ts`** -> AI Confidence: **99.29%**
166. **`apps/meteor/app/push/server/definition.ts`** -> AI Confidence: **99.29%**
167. **`apps/meteor/client/views/account/preferences/useAccountPreferencesValues.ts`** -> AI Confidence: **99.29%**
168. **`apps/meteor/definition/externals/meteor/logging.d.ts`** -> AI Confidence: **99.29%**
169. **`apps/meteor/ee/server/apps/marketplace/MarketplaceAPIClient.ts`** -> AI Confidence: **99.29%**
170. **`apps/meteor/tests/e2e/federation/config/constants.ts`** -> AI Confidence: **99.29%**
171. **`packages/apps-engine/src/definition/email/IEmailDescriptor.ts`** -> AI Confidence: **99.29%**
172. **`packages/apps-engine/src/definition/livechat/IDepartment.ts`** -> AI Confidence: **99.29%**
173. **`packages/base64/src/base64.ts`** -> AI Confidence: **99.29%**
174. **`packages/core-typings/src/ILivechatDepartment.ts`** -> AI Confidence: **99.29%**
175. **`packages/core-typings/src/IPushNotificationConfig.ts`** -> AI Confidence: **99.29%**
176. **`packages/core-typings/src/OauthConfig.ts`** -> AI Confidence: **99.29%**
177. **`packages/model-typings/src/models/IUsersModel.ts`** -> AI Confidence: **99.29%**
178. **`packages/tools/src/convertPathsIntoSubObjects.ts`** -> AI Confidence: **99.29%**
179. **`apps/meteor/tests/e2e/containers/saml/Dockerfile`** -> AI Confidence: **99.29%**
180. **`ee/packages/federation-matrix/tests/scripts/run-integration-tests.sh`** -> AI Confidence: **99.29%**
181. **`apps/meteor/tests/e2e/containers/saml/config/simplesamlphp/authsources.php`** -> AI Confidence: **99.29%**
182. **`apps/meteor/tests/e2e/containers/saml/config/simplesamlphp/saml20-sp-remote.php`** -> AI Confidence: **99.29%**
183. **`.github/actions/update-version-durability/index.js`** -> AI Confidence: **99.24%**
184. **`apps/meteor/app/irc/server/irc-bridge/index.js`** -> AI Confidence: **99.24%**
185. **`packages/livechat/src/routes/Chat/component.js`** -> AI Confidence: **99.24%**
186. **`packages/livechat/src/routes/Chat/container.js`** -> AI Confidence: **99.24%**
187. **`apps/meteor/app/2fa/server/functions/resetTOTP.ts`** -> AI Confidence: **99.24%**
188. **`apps/meteor/app/api/server/ApiClass.ts`** -> AI Confidence: **99.24%**
189. **`apps/meteor/app/api/server/api.ts`** -> AI Confidence: **99.24%**
190. **`apps/meteor/app/apps/server/bridges/listeners.ts`** -> AI Confidence: **99.24%**
191. **`apps/meteor/app/apps/server/bridges/livechat.ts`** -> AI Confidence: **99.24%**
192. **`apps/meteor/app/apps/server/bridges/rooms.ts`** -> AI Confidence: **99.24%**
193. **`apps/meteor/app/authorization/client/hasPermission.ts`** -> AI Confidence: **99.24%**
194. **`apps/meteor/app/autotranslate/server/deeplTranslate.ts`** -> AI Confidence: **99.24%**
195. **`apps/meteor/app/channel-settings/server/functions/saveRoomType.ts`** -> AI Confidence: **99.24%**
196. **`apps/meteor/app/cloud/server/functions/syncWorkspace/syncCloudData.ts`** -> AI Confidence: **99.24%**
197. **`apps/meteor/app/discussion/server/methods/createDiscussion.ts`** -> AI Confidence: **99.24%**
198. **`apps/meteor/app/file-upload/server/config/GridFS.ts`** -> AI Confidence: **99.24%**
199. **`apps/meteor/app/file-upload/server/methods/sendFileMessage.ts`** -> AI Confidence: **99.24%**
200. **`apps/meteor/app/invites/server/functions/findOrCreateInvite.ts`** -> AI Confidence: **99.24%**
201. **`apps/meteor/app/livechat/imports/server/rest/sms.ts`** -> AI Confidence: **99.24%**
202. **`apps/meteor/app/livechat/server/api/v1/message.ts`** -> AI Confidence: **99.24%**
203. **`apps/meteor/app/livechat/server/api/v1/room.ts`** -> AI Confidence: **99.24%**
204. **`apps/meteor/app/livechat/server/hooks/markRoomResponded.ts`** -> AI Confidence: **99.24%**
205. **`apps/meteor/app/livechat/server/hooks/sendToCRM.ts`** -> AI Confidence: **99.24%**
206. **`apps/meteor/app/notification-queue/server/NotificationQueue.ts`** -> AI Confidence: **99.24%**
207. **`apps/meteor/app/slashcommands-hide/server/hide.ts`** -> AI Confidence: **99.24%**
208. **`apps/meteor/app/slashcommands-inviteall/server/server.ts`** -> AI Confidence: **99.24%**
209. **`apps/meteor/app/slashcommands-status/server/status.ts`** -> AI Confidence: **99.24%**
210. **`apps/meteor/app/ui-message/client/ActionManager.ts`** -> AI Confidence: **99.24%**
211. **`apps/meteor/app/version-check/server/functions/checkVersionUpdate.ts`** -> AI Confidence: **99.24%**
212. **`apps/meteor/app/webdav/server/methods/uploadFileToWebdav.ts`** -> AI Confidence: **99.24%**
213. **`apps/meteor/client/components/message/content/attachments/DefaultAttachment.tsx`** -> AI Confidence: **99.24%**
214. **`apps/meteor/client/components/message/toolbar/useReplyInDMAction.ts`** -> AI Confidence: **99.24%**
215. **`apps/meteor/client/components/message/variants/RoomMessage.tsx`** -> AI Confidence: **99.24%**
216. **`apps/meteor/client/hooks/roomActions/useE2EERoomAction.ts`** -> AI Confidence: **99.24%**
217. **`apps/meteor/client/hooks/useRoomMenuActions.ts`** -> AI Confidence: **99.24%**
218. **`apps/meteor/client/navbar/NavBarPagesGroup/actions/CreateChannelModal.tsx`** -> AI Confidence: **99.24%**
219. **`apps/meteor/client/providers/OmnichannelProvider.tsx`** -> AI Confidence: **99.24%**
220. **`apps/meteor/client/views/account/profile/AccountProfileForm.tsx`** -> AI Confidence: **99.24%**
221. **`apps/meteor/client/views/account/security/AccountSecurityPage.tsx`** -> AI Confidence: **99.24%**
222. **`apps/meteor/client/views/account/security/ChangePassphrase.tsx`** -> AI Confidence: **99.24%**
223. **`apps/meteor/client/views/account/tokens/AccountTokensTable/AccountTokensTable.tsx`** -> AI Confidence: **99.24%**
224. **`apps/meteor/client/views/admin/customEmoji/CustomEmoji.tsx`** -> AI Confidence: **99.24%**
225. **`apps/meteor/client/views/admin/deviceManagement/DeviceManagementAdminTable/DeviceManagementAdminTable.tsx`** -> AI Confidence: **99.24%**
226. **`apps/meteor/client/views/admin/deviceManagement/DeviceManagementInfo/DeviceManagementInfo.tsx`** -> AI Confidence: **99.24%**
227. **`apps/meteor/client/views/admin/engagementDashboard/messages/MessagesSentSection.tsx`** -> AI Confidence: **99.24%**
228. **`apps/meteor/client/views/admin/engagementDashboard/users/ActiveUsersSection.tsx`** -> AI Confidence: **99.24%**
229. **`apps/meteor/client/views/admin/engagementDashboard/users/NewUsersSection.tsx`** -> AI Confidence: **99.24%**
230. **`apps/meteor/client/views/admin/engagementDashboard/users/UsersByTimeOfTheDaySection.tsx`** -> AI Confidence: **99.24%**
231. **`apps/meteor/client/views/admin/import/NewImportPage.tsx`** -> AI Confidence: **99.24%**
232. **`apps/meteor/client/views/admin/integrations/IntegrationsTable.tsx`** -> AI Confidence: **99.24%**
233. **`apps/meteor/client/views/admin/invites/InvitesPage.tsx`** -> AI Confidence: **99.24%**
234. **`apps/meteor/client/views/admin/moderation/ModerationConsoleTable.tsx`** -> AI Confidence: **99.24%**
235. **`apps/meteor/client/views/admin/moderation/UserReports/ModConsoleUsersTable.tsx`** -> AI Confidence: **99.24%**
236. **`apps/meteor/client/views/admin/permissions/UsersInRole/UsersInRolePage.tsx`** -> AI Confidence: **99.24%**
237. **`apps/meteor/client/views/admin/rooms/RoomRow.tsx`** -> AI Confidence: **99.24%**
238. **`apps/meteor/client/views/admin/rooms/RoomsTable.tsx`** -> AI Confidence: **99.24%**
239. **`apps/meteor/client/views/admin/routes.tsx`** -> AI Confidence: **99.24%**
240. **`apps/meteor/client/views/admin/subscription/SubscriptionPage.tsx`** -> AI Confidence: **99.24%**
241. **`apps/meteor/client/views/admin/subscription/components/cards/PlanCard/PlanCardPremium.tsx`** -> AI Confidence: **99.24%**
242. **`apps/meteor/client/views/admin/subscription/components/cards/PlanCard/PlanCardTrial.tsx`** -> AI Confidence: **99.24%**
243. **`apps/meteor/client/views/admin/users/AdminUsersPage.tsx`** -> AI Confidence: **99.24%**
244. **`apps/meteor/client/views/audit/components/SecurityLogsTable.tsx`** -> AI Confidence: **99.24%**
245. **`apps/meteor/client/views/directory/tabs/channels/ChannelsTable/ChannelsTable.tsx`** -> AI Confidence: **99.24%**
246. **`apps/meteor/client/views/directory/tabs/users/UsersTable/UsersTable.tsx`** -> AI Confidence: **99.24%**
247. **`apps/meteor/client/views/marketplace/AppDetailsPage/AppDetailsPage.tsx`** -> AI Confidence: **99.24%**
248. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppDetails/AppDetails.tsx`** -> AI Confidence: **99.24%**
249. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppInstances/AppInstances.tsx`** -> AI Confidence: **99.24%**
250. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppLogs/AppLogs.tsx`** -> AI Confidence: **99.24%**
251. **`apps/meteor/client/views/marketplace/AppsPage/AppsPageContent.tsx`** -> AI Confidence: **99.24%**
252. **`apps/meteor/client/views/marketplace/hooks/useAppInfo.ts`** -> AI Confidence: **99.24%**
253. **`apps/meteor/client/views/navigation/sidepanel/SidepanelItem/RoomSidePanelItem.tsx`** -> AI Confidence: **99.24%**
254. **`apps/meteor/client/views/navigation/sidepanel/hooks/useRoomMenuActions.ts`** -> AI Confidence: **99.24%**
255. **`apps/meteor/client/views/navigation/sidepanel/omnichannel/InquireSidePanelItem.tsx`** -> AI Confidence: **99.24%**
256. **`apps/meteor/client/views/oauth/components/CurrentUserDisplay.tsx`** -> AI Confidence: **99.24%**
257. **`apps/meteor/client/views/omnichannel/businessHours/EditBusinessHours.tsx`** -> AI Confidence: **99.24%**
258. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/OutboundMessageWizard.tsx`** -> AI Confidence: **99.24%**
259. **`apps/meteor/client/views/omnichannel/contactHistory/MessageList/ContactHistoryMessage.tsx`** -> AI Confidence: **99.24%**
260. **`apps/meteor/client/views/omnichannel/contactHistory/MessageList/ContactHistoryMessagesList.tsx`** -> AI Confidence: **99.24%**
261. **`apps/meteor/client/views/omnichannel/contactInfo/EditContactInfo.tsx`** -> AI Confidence: **99.24%**
262. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoChannels/ContactInfoChannelsItem.tsx`** -> AI Confidence: **99.24%**
263. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoHistory/ContactInfoHistoryMessages.tsx`** -> AI Confidence: **99.24%**
264. **`apps/meteor/client/views/omnichannel/departments/EditDepartment.tsx`** -> AI Confidence: **99.24%**
265. **`apps/meteor/client/views/omnichannel/managers/ManagersTable.tsx`** -> AI Confidence: **99.24%**
266. **`apps/meteor/client/views/omnichannel/monitors/MonitorsTable.tsx`** -> AI Confidence: **99.24%**
267. **`apps/meteor/client/views/omnichannel/tags/TagEdit.tsx`** -> AI Confidence: **99.24%**
268. **`apps/meteor/client/views/omnichannel/triggers/TriggersTable.tsx`** -> AI Confidence: **99.24%**
269. **`apps/meteor/client/views/room/Header/ParentRoom/ParentTeam.tsx`** -> AI Confidence: **99.24%**
270. **`apps/meteor/client/views/room/MessageList/providers/MessageListProvider.tsx`** -> AI Confidence: **99.24%**
271. **`apps/meteor/client/views/room/body/DropTargetOverlay.tsx`** -> AI Confidence: **99.24%**
272. **`apps/meteor/client/views/room/composer/messageBox/MessageBoxActionsToolbar/MessageBoxActionsToolbar.tsx`** -> AI Confidence: **99.24%**
273. **`apps/meteor/client/views/room/contextualBar/ExportMessages/useDownloadExportMutation.ts`** -> AI Confidence: **99.24%**
274. **`apps/meteor/client/views/room/contextualBar/Info/EditRoomInfo/EditRoomInfo.tsx`** -> AI Confidence: **99.24%**
275. **`apps/meteor/client/views/room/contextualBar/PruneMessages/PruneMessagesWithData.tsx`** -> AI Confidence: **99.24%**
276. **`apps/meteor/client/views/room/contextualBar/RoomFiles/components/FileItemMenu.tsx`** -> AI Confidence: **99.24%**
277. **`apps/meteor/client/views/room/contextualBar/RoomMembers/RoomMembers.tsx`** -> AI Confidence: **99.24%**
278. **`apps/meteor/client/views/room/contextualBar/Threads/Thread.tsx`** -> AI Confidence: **99.24%**
279. **`apps/meteor/client/views/room/contextualBar/Threads/ThreadList.tsx`** -> AI Confidence: **99.24%**
280. **`apps/meteor/client/views/room/contextualBar/Threads/hooks/useThreadsList.ts`** -> AI Confidence: **99.24%**
281. **`apps/meteor/client/views/room/contextualBar/VideoConference/VideoConfPopups/VideoConfPopup/IncomingPopup.tsx`** -> AI Confidence: **99.24%**
282. **`apps/meteor/client/views/room/hooks/useUserInfoActions/useUserInfoActions.ts`** -> AI Confidence: **99.24%**
283. **`apps/meteor/client/views/room/providers/RoomToolboxProvider.tsx`** -> AI Confidence: **99.24%**
284. **`apps/meteor/client/views/root/hooks/loggedIn/useNotifyUser.ts`** -> AI Confidence: **99.24%**
285. **`apps/meteor/client/views/teams/contextualBar/info/TeamsInfo.tsx`** -> AI Confidence: **99.24%**
286. **`apps/meteor/ee/server/apps/communication/rest.ts`** -> AI Confidence: **99.24%**
287. **`apps/meteor/ee/server/apps/marketplace/fetchMarketplaceApps.ts`** -> AI Confidence: **99.24%**
288. **`apps/meteor/ee/server/apps/marketplace/fetchMarketplaceCategories.ts`** -> AI Confidence: **99.24%**
289. **`apps/meteor/server/features/EmailInbox/EmailInbox_Incoming.ts`** -> AI Confidence: **99.24%**
290. **`apps/meteor/server/features/EmailInbox/EmailInbox_Outgoing.ts`** -> AI Confidence: **99.24%**
291. **`apps/meteor/server/methods/browseChannels.ts`** -> AI Confidence: **99.24%**
292. **`apps/meteor/server/methods/channelsList.ts`** -> AI Confidence: **99.24%**
293. **`apps/meteor/server/routes/avatar/user.ts`** -> AI Confidence: **99.24%**
294. **`apps/meteor/server/services/calendar/service.ts`** -> AI Confidence: **99.24%**
295. **`apps/meteor/server/services/meteor/service.ts`** -> AI Confidence: **99.24%**
296. **`apps/meteor/server/services/omnichannel/queue.ts`** -> AI Confidence: **99.24%**
297. **`apps/meteor/server/services/room/service.ts`** -> AI Confidence: **99.24%**
298. **`apps/meteor/server/services/team/service.ts`** -> AI Confidence: **99.24%**
299. **`apps/meteor/server/startup/initialData.ts`** -> AI Confidence: **99.24%**
300. **`apps/meteor/server/startup/serverRunning.ts`** -> AI Confidence: **99.24%**
301. **`ee/packages/media-calls/src/internal/SignalProcessor.ts`** -> AI Confidence: **99.24%**
302. **`ee/packages/media-calls/src/server/CallDirector.ts`** -> AI Confidence: **99.24%**
303. **`ee/packages/media-calls/src/sip/Session.ts`** -> AI Confidence: **99.24%**
304. **`ee/packages/media-calls/src/sip/providers/IncomingSipCall.ts`** -> AI Confidence: **99.24%**
305. **`ee/packages/media-calls/src/sip/providers/OutgoingSipCall.ts`** -> AI Confidence: **99.24%**
306. **`ee/packages/omnichannel-services/src/OmnichannelTranscript.ts`** -> AI Confidence: **99.24%**
307. **`packages/apps-engine/deno-runtime/handlers/app/construct.ts`** -> AI Confidence: **99.24%**
308. **`packages/apps-engine/deno-runtime/handlers/app/handleUploadEvents.ts`** -> AI Confidence: **99.24%**
309. **`packages/apps-engine/src/server/accessors/ModifyCreator.ts`** -> AI Confidence: **99.24%**
310. **`packages/apps-engine/src/server/compiler/AppPackageParser.ts`** -> AI Confidence: **99.24%**
311. **`packages/apps-engine/src/server/managers/AppListenerManager.ts`** -> AI Confidence: **99.24%**
312. **`packages/apps-engine/src/server/oauth2/OAuth2Client.ts`** -> AI Confidence: **99.24%**
313. **`packages/core-services/src/LocalBroker.ts`** -> AI Confidence: **99.24%**
314. **`packages/livechat/src/components/Form/HookFormExample/stories.tsx`** -> AI Confidence: **99.24%**
315. **`packages/livechat/src/components/Screen/ScreenProvider.tsx`** -> AI Confidence: **99.24%**
316. **`packages/livechat/src/lib/triggerActions.ts`** -> AI Confidence: **99.24%**
317. **`packages/livechat/src/routes/LeaveMessage/index.tsx`** -> AI Confidence: **99.24%**
318. **`packages/livechat/src/routes/Register/index.tsx`** -> AI Confidence: **99.24%**
319. **`packages/release-action/src/index.ts`** -> AI Confidence: **99.24%**
320. **`packages/ui-client/src/components/Header/index.ts`** -> AI Confidence: **99.24%**
321. **`packages/ui-client/src/components/Page/PageHeaderNoShadow.tsx`** -> AI Confidence: **99.24%**
322. **`packages/ui-client/src/components/Wizard/index.ts`** -> AI Confidence: **99.24%**
323. **`packages/ui-voip/src/components/Cards/index.ts`** -> AI Confidence: **99.24%**
324. **`packages/web-ui-registration/src/LoginForm.tsx`** -> AI Confidence: **99.24%**
325. **`apps/meteor/app/apps/server/converters/messages.js`** -> AI Confidence: **99.23%**
326. **`apps/meteor/app/api/server/middlewares/authenticationHono.ts`** -> AI Confidence: **99.23%**
327. **`apps/meteor/app/authorization/server/methods/addUserToRole.ts`** -> AI Confidence: **99.23%**
328. **`apps/meteor/app/authorization/server/methods/removeUserFromRole.ts`** -> AI Confidence: **99.23%**
329. **`apps/meteor/app/cors/server/cors.ts`** -> AI Confidence: **99.23%**
330. **`apps/meteor/app/custom-sounds/server/methods/insertOrUpdateSound.ts`** -> AI Confidence: **99.23%**
331. **`apps/meteor/app/invites/server/functions/sendInvitationEmail.ts`** -> AI Confidence: **99.23%**
332. **`apps/meteor/app/livechat/server/sendMessageBySMS.ts`** -> AI Confidence: **99.23%**
333. **`apps/meteor/app/oauth2-server-config/server/admin/functions/addOAuthApp.ts`** -> AI Confidence: **99.23%**
334. **`apps/meteor/app/version-check/server/functions/buildVersionUpdateMessage.ts`** -> AI Confidence: **99.23%**
335. **`apps/meteor/client/components/message/content/UrlPreviews.tsx`** -> AI Confidence: **99.23%**
336. **`apps/meteor/client/components/message/toolbar/useTranslateAction.ts`** -> AI Confidence: **99.23%**
337. **`apps/meteor/client/components/message/toolbar/useViewOriginalTranslationAction.ts`** -> AI Confidence: **99.23%**
338. **`apps/meteor/client/hooks/roomActions/useThreadRoomAction.tsx`** -> AI Confidence: **99.23%**
339. **`apps/meteor/client/meteor/login/google.ts`** -> AI Confidence: **99.23%**
340. **`apps/meteor/client/navbar/NavBarPagesGroup/actions/CreateTeamModal.tsx`** -> AI Confidence: **99.23%**
341. **`apps/meteor/client/navbar/NavBarSettingsToolbar/UserMenu/UserMenuHeader.tsx`** -> AI Confidence: **99.23%**
342. **`apps/meteor/client/views/admin/import/ImportOperationSummary.tsx`** -> AI Confidence: **99.23%**
343. **`apps/meteor/client/views/admin/mailer/MailerPage.tsx`** -> AI Confidence: **99.23%**
344. **`apps/meteor/client/views/admin/permissions/EditRolePage.tsx`** -> AI Confidence: **99.23%**
345. **`apps/meteor/client/views/admin/subscription/components/cards/MACCard.tsx`** -> AI Confidence: **99.23%**
346. **`apps/meteor/client/views/directory/tabs/users/UsersTable/UsersTableRow.tsx`** -> AI Confidence: **99.23%**
347. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppLogs/Filters/TimeFilterSelect.tsx`** -> AI Confidence: **99.23%**
348. **`apps/meteor/client/views/marketplace/AppsPage/AppsPageContentBody.tsx`** -> AI Confidence: **99.23%**
349. **`apps/meteor/client/views/mediaCallHistory/MediaCallHistoryContextualbar.tsx`** -> AI Confidence: **99.23%**
350. **`apps/meteor/client/views/modal/uikit/ModalBlock.tsx`** -> AI Confidence: **99.23%**
351. **`apps/meteor/client/views/navigation/sidepanel/SidePanelRouter.tsx`** -> AI Confidence: **99.23%**
352. **`apps/meteor/client/views/omnichannel/businessHours/BusinessHoursTable.tsx`** -> AI Confidence: **99.23%**
353. **`apps/meteor/client/views/room/MessageList/hooks/useAutoTranslate.ts`** -> AI Confidence: **99.23%**
354. **`apps/meteor/client/views/room/body/hooks/useGoToHomeOnRemoved.ts`** -> AI Confidence: **99.23%**
355. **`apps/meteor/client/views/room/contextualBar/Threads/components/ThreadListItem.tsx`** -> AI Confidence: **99.23%**
356. **`apps/meteor/client/views/room/hooks/useUserInfoActions/actions/useAddUserAction.tsx`** -> AI Confidence: **99.23%**
357. **`apps/meteor/client/views/room/providers/UserCardProvider.tsx`** -> AI Confidence: **99.23%**
358. **`apps/meteor/ee/app/livechat-enterprise/server/api/triggers.ts`** -> AI Confidence: **99.23%**
359. **`apps/meteor/ee/app/livechat-enterprise/server/hooks/checkAgentBeforeTakeInquiry.ts`** -> AI Confidence: **99.23%**
360. **`apps/meteor/ee/app/livechat-enterprise/server/hooks/handleNextAgentPreferredEvents.ts`** -> AI Confidence: **99.23%**
361. **`apps/meteor/server/methods/saveUserPreferences.ts`** -> AI Confidence: **99.23%**
362. **`apps/meteor/server/ufs/ufs-local.ts`** -> AI Confidence: **99.23%**
363. **`apps/uikit-playground/src/Context/reducer.ts`** -> AI Confidence: **99.23%**
364. **`ee/packages/pdf-worker/src/templates/ChatTranscript/components/Message.tsx`** -> AI Confidence: **99.23%**
365. **`packages/apps-engine/src/server/bridges/LivechatBridge.ts`** -> AI Confidence: **99.23%**
366. **`packages/apps-engine/src/server/managers/AppOutboundCommunicationProviderManager.ts`** -> AI Confidence: **99.23%**
367. **`packages/apps-engine/src/server/managers/AppSlashCommandManager.ts`** -> AI Confidence: **99.23%**
368. **`packages/livechat/src/routes/Chat/connector.tsx`** -> AI Confidence: **99.23%**
369. **`packages/models/src/models/Messages.ts`** -> AI Confidence: **99.23%**
370. **`packages/models/src/models/Subscriptions.ts`** -> AI Confidence: **99.23%**
371. **`packages/ui-client/src/components/MultiSelectCustom/MultiSelectCustom.tsx`** -> AI Confidence: **99.23%**
372. **`apps/meteor/client/views/room/contextualBar/Info/EditRoomInfo/useEditRoomInitialValues.ts`** -> AI Confidence: **99.22%**
373. **`packages/core-typings/src/IStats.ts`** -> AI Confidence: **99.22%**
374. **`apps/meteor/app/utils/client/getURL.ts`** -> AI Confidence: **99.2%**
375. **`apps/meteor/app/api/server/default/openApi.ts`** -> AI Confidence: **99.18%**
376. **`apps/meteor/app/api/server/v1/autotranslate.ts`** -> AI Confidence: **99.18%**
377. **`apps/meteor/app/api/server/v1/calendar.ts`** -> AI Confidence: **99.18%**
378. **`apps/meteor/app/api/server/v1/chat.ts`** -> AI Confidence: **99.18%**
379. **`apps/meteor/app/api/server/v1/integrations.ts`** -> AI Confidence: **99.18%**
380. **`apps/meteor/app/api/server/v1/moderation.ts`** -> AI Confidence: **99.18%**
381. **`apps/meteor/app/api/server/v1/settings.ts`** -> AI Confidence: **99.18%**
382. **`apps/meteor/app/api/server/v1/teams.ts`** -> AI Confidence: **99.18%**
383. **`apps/meteor/app/api/server/v1/videoConference.ts`** -> AI Confidence: **99.18%**
384. **`apps/meteor/app/apps/server/bridges/oauthApps.ts`** -> AI Confidence: **99.18%**
385. **`apps/meteor/app/apps/server/bridges/uploads.ts`** -> AI Confidence: **99.18%**
386. **`apps/meteor/app/apps/server/converters/threads.ts`** -> AI Confidence: **99.18%**
387. **`apps/meteor/app/cloud/server/functions/supportedVersionsToken/supportedVersionsToken.ts`** -> AI Confidence: **99.18%**
388. **`apps/meteor/app/e2e/server/methods/setRoomKeyID.ts`** -> AI Confidence: **99.18%**
389. **`apps/meteor/app/file/server/file.server.ts`** -> AI Confidence: **99.18%**
390. **`apps/meteor/app/importer-csv/server/CsvImporter.ts`** -> AI Confidence: **99.18%**
391. **`apps/meteor/app/importer/server/methods/getImportFileData.ts`** -> AI Confidence: **99.18%**
392. **`apps/meteor/app/importer/server/methods/startImport.ts`** -> AI Confidence: **99.18%**
393. **`apps/meteor/app/integrations/server/methods/outgoing/addOutgoingIntegration.ts`** -> AI Confidence: **99.18%**
394. **`apps/meteor/app/livechat/imports/server/rest/inquiries.ts`** -> AI Confidence: **99.18%**
395. **`apps/meteor/app/livechat/server/api/v1/transcript.ts`** -> AI Confidence: **99.18%**
396. **`apps/meteor/app/livechat/server/business-hour/BusinessHourManager.ts`** -> AI Confidence: **99.18%**
397. **`apps/meteor/app/message-star/server/starMessage.ts`** -> AI Confidence: **99.18%**
398. **`apps/meteor/app/meteor-accounts-saml/server/listener.ts`** -> AI Confidence: **99.18%**
399. **`apps/meteor/app/push/server/methods.ts`** -> AI Confidence: **99.18%**
400. **`apps/meteor/app/search/server/service/SearchResultValidationService.ts`** -> AI Confidence: **99.18%**
401. **`apps/meteor/app/slashcommands-invite/server/server.ts`** -> AI Confidence: **99.18%**
402. **`apps/meteor/app/slashcommands-join/server/server.ts`** -> AI Confidence: **99.18%**
403. **`apps/meteor/app/slashcommands-kick/server/server.ts`** -> AI Confidence: **99.18%**
404. **`apps/meteor/app/slashcommands-msg/server/server.ts`** -> AI Confidence: **99.18%**
405. **`apps/meteor/app/slashcommands-mute/server/mute.ts`** -> AI Confidence: **99.18%**
406. **`apps/meteor/app/slashcommands-topic/client/topic.ts`** -> AI Confidence: **99.18%**
407. **`apps/meteor/app/threads/server/hooks/aftersavemessage.ts`** -> AI Confidence: **99.18%**
408. **`apps/meteor/app/threads/server/methods/followMessage.ts`** -> AI Confidence: **99.18%**
409. **`apps/meteor/app/threads/server/methods/unfollowMessage.ts`** -> AI Confidence: **99.18%**
410. **`apps/meteor/app/user-status/server/methods/setUserStatus.ts`** -> AI Confidence: **99.18%**
411. **`apps/meteor/app/utils/client/lib/SDKClient.ts`** -> AI Confidence: **99.18%**
412. **`apps/meteor/app/webdav/server/methods/getFileFromWebdav.ts`** -> AI Confidence: **99.18%**
413. **`apps/meteor/app/webdav/server/methods/getWebdavFileList.ts`** -> AI Confidence: **99.18%**
414. **`apps/meteor/client/apps/RealAppsEngineUIHost.ts`** -> AI Confidence: **99.18%**
415. **`apps/meteor/client/components/UserAndRoomAutoCompleteMultiple/UserAndRoomAutoCompleteMultiple.tsx`** -> AI Confidence: **99.18%**
416. **`apps/meteor/client/components/message/MessageToolbarHolder.tsx`** -> AI Confidence: **99.18%**
417. **`apps/meteor/client/components/message/content/MessageActions.tsx`** -> AI Confidence: **99.18%**
418. **`apps/meteor/client/components/message/content/ThreadMetrics.tsx`** -> AI Confidence: **99.18%**
419. **`apps/meteor/client/components/message/content/attachments/file/ImageAttachment.tsx`** -> AI Confidence: **99.18%**
420. **`apps/meteor/client/components/message/toolbar/MessageToolbarActionMenu.tsx`** -> AI Confidence: **99.18%**
421. **`apps/meteor/client/contexts/AppsContext.tsx`** -> AI Confidence: **99.18%**
422. **`apps/meteor/client/hooks/roomActions/useCallsRoomAction.ts`** -> AI Confidence: **99.18%**
423. **`apps/meteor/client/hooks/roomActions/useMediaCallRoomAction.spec.tsx`** -> AI Confidence: **99.18%**
424. **`apps/meteor/client/hooks/useAppSlashCommands.ts`** -> AI Confidence: **99.18%**
425. **`apps/meteor/client/hooks/useMessageboxAppsActionButtons.ts`** -> AI Confidence: **99.18%**
426. **`apps/meteor/client/meteor/startup/accounts.ts`** -> AI Confidence: **99.18%**
427. **`apps/meteor/client/navbar/NavBarControls/NavBarControlsWithData.tsx`** -> AI Confidence: **99.18%**
428. **`apps/meteor/client/navbar/NavBarPagesGroup/hooks/useCreateNewItems.tsx`** -> AI Confidence: **99.18%**
429. **`apps/meteor/client/navbar/NavBarSearch/NavBarSearchItemWithData.tsx`** -> AI Confidence: **99.18%**
430. **`apps/meteor/client/navbar/NavBarSettingsToolbar/UserMenu/EditStatusModal.tsx`** -> AI Confidence: **99.18%**
431. **`apps/meteor/client/providers/CustomSoundProvider/CustomSoundProvider.tsx`** -> AI Confidence: **99.18%**
432. **`apps/meteor/client/providers/ServerProvider.tsx`** -> AI Confidence: **99.18%**
433. **`apps/meteor/client/providers/SettingsProvider.tsx`** -> AI Confidence: **99.18%**
434. **`apps/meteor/client/providers/TranslationProvider.tsx`** -> AI Confidence: **99.18%**
435. **`apps/meteor/client/sidebar/header/MatrixFederationSearch/MatrixFederationManageServerModal.tsx`** -> AI Confidence: **99.18%**
436. **`apps/meteor/client/startup/routes.tsx`** -> AI Confidence: **99.18%**
437. **`apps/meteor/client/startup/startup.ts`** -> AI Confidence: **99.18%**
438. **`apps/meteor/client/uikit/hooks/useMessageBlockContextValue.ts`** -> AI Confidence: **99.18%**
439. **`apps/meteor/client/views/account/deviceManagement/DeviceManagementAccountTable/DeviceManagementAccountTable.tsx`** -> AI Confidence: **99.18%**
440. **`apps/meteor/client/views/account/profile/AccountProfilePage.tsx`** -> AI Confidence: **99.18%**
441. **`apps/meteor/client/views/admin/ABAC/ABACRoomsTab/RoomForm.tsx`** -> AI Confidence: **99.18%**
442. **`apps/meteor/client/views/admin/ABAC/ABACSettingTab/AbacEnabledToggle.tsx`** -> AI Confidence: **99.18%**
443. **`apps/meteor/client/views/admin/customEmoji/AddCustomEmoji.tsx`** -> AI Confidence: **99.18%**
444. **`apps/meteor/client/views/admin/customEmoji/CustomEmojiRoute.tsx`** -> AI Confidence: **99.18%**
445. **`apps/meteor/client/views/admin/customEmoji/EditCustomEmojiWithData.tsx`** -> AI Confidence: **99.18%**
446. **`apps/meteor/client/views/admin/customSounds/CustomSoundsPage.tsx`** -> AI Confidence: **99.18%**
447. **`apps/meteor/client/views/admin/customSounds/EditCustomSound.tsx`** -> AI Confidence: **99.18%**
448. **`apps/meteor/client/views/admin/customUserStatus/CustomUserStatusFormWithData.tsx`** -> AI Confidence: **99.18%**
449. **`apps/meteor/client/views/admin/customUserStatus/CustomUserStatusTable/CustomUserStatusTable.tsx`** -> AI Confidence: **99.18%**
450. **`apps/meteor/client/views/admin/deviceManagement/DeviceManagementAdminRoute.tsx`** -> AI Confidence: **99.18%**
451. **`apps/meteor/client/views/admin/emailInbox/EmailInboxFormWithData.tsx`** -> AI Confidence: **99.18%**
452. **`apps/meteor/client/views/admin/engagementDashboard/users/UsersTab.tsx`** -> AI Confidence: **99.18%**
453. **`apps/meteor/client/views/admin/import/ImportHistoryPage.tsx`** -> AI Confidence: **99.18%**
454. **`apps/meteor/client/views/admin/integrations/EditIntegrationsPageWithData.tsx`** -> AI Confidence: **99.18%**
455. **`apps/meteor/client/views/admin/integrations/IntegrationsPage.tsx`** -> AI Confidence: **99.18%**
456. **`apps/meteor/client/views/admin/integrations/outgoing/history/OutgoingWebhookHistoryPage.tsx`** -> AI Confidence: **99.18%**
457. **`apps/meteor/client/views/admin/invites/InviteRow.tsx`** -> AI Confidence: **99.18%**
458. **`apps/meteor/client/views/admin/moderation/MessageContextFooter.tsx`** -> AI Confidence: **99.18%**
459. **`apps/meteor/client/views/admin/moderation/ModConsoleReportDetails.tsx`** -> AI Confidence: **99.18%**
460. **`apps/meteor/client/views/admin/oauthApps/EditOauthAppWithData.tsx`** -> AI Confidence: **99.18%**
461. **`apps/meteor/client/views/admin/permissions/EditRolePageWithData.tsx`** -> AI Confidence: **99.18%**
462. **`apps/meteor/client/views/admin/permissions/PermissionsTable/PermissionsTable.tsx`** -> AI Confidence: **99.18%**
463. **`apps/meteor/client/views/admin/permissions/PermissionsTable/RoleCell.tsx`** -> AI Confidence: **99.18%**
464. **`apps/meteor/client/views/admin/permissions/UsersInRole/UsersInRoleTable/UsersInRoleTableRow.tsx`** -> AI Confidence: **99.18%**
465. **`apps/meteor/client/views/admin/settings/Setting/inputs/LookupSettingInput.tsx`** -> AI Confidence: **99.18%**
466. **`apps/meteor/client/views/admin/settings/SettingsGroupCard.tsx`** -> AI Confidence: **99.18%**
467. **`apps/meteor/client/views/admin/subscription/surface/UiKitSubscriptionLicense.tsx`** -> AI Confidence: **99.18%**
468. **`apps/meteor/client/views/admin/users/AdminUserFormWithData.tsx`** -> AI Confidence: **99.18%**
469. **`apps/meteor/client/views/admin/users/UsersTable/UsersTableFilters.tsx`** -> AI Confidence: **99.18%**
470. **`apps/meteor/client/views/admin/workspace/DeploymentCard/DeploymentCard.tsx`** -> AI Confidence: **99.18%**
471. **`apps/meteor/client/views/admin/workspace/WorkspaceRoute.tsx`** -> AI Confidence: **99.18%**
472. **`apps/meteor/client/views/audit/components/AuditForm.tsx`** -> AI Confidence: **99.18%**
473. **`apps/meteor/client/views/audit/components/AuditLogEntry.tsx`** -> AI Confidence: **99.18%**
474. **`apps/meteor/client/views/audit/components/SecurityLogDisplayModal.tsx`** -> AI Confidence: **99.18%**
475. **`apps/meteor/client/views/audit/components/tabs/RoomsTab.tsx`** -> AI Confidence: **99.18%**
476. **`apps/meteor/client/views/directory/tabs/teams/TeamsTable/TeamsTableRow.tsx`** -> AI Confidence: **99.18%**
477. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppReleases/AppReleases.tsx`** -> AI Confidence: **99.18%**
478. **`apps/meteor/client/views/marketplace/AppInstallPage.tsx`** -> AI Confidence: **99.18%**
479. **`apps/meteor/client/views/marketplace/hooks/useInstallApp.tsx`** -> AI Confidence: **99.18%**
480. **`apps/meteor/client/views/mediaCallHistory/CallHistoryRowInternalUser.tsx`** -> AI Confidence: **99.18%**
481. **`apps/meteor/client/views/oauth/components/AuthorizationFormPage.tsx`** -> AI Confidence: **99.18%**
482. **`apps/meteor/client/views/omnichannel/additionalForms/BusinessHoursMultiple.tsx`** -> AI Confidence: **99.18%**
483. **`apps/meteor/client/views/omnichannel/businessHours/BusinessHoursRouter.tsx`** -> AI Confidence: **99.18%**
484. **`apps/meteor/client/views/omnichannel/cannedResponses/modals/CannedResponseEditWithData.tsx`** -> AI Confidence: **99.18%**
485. **`apps/meteor/client/views/omnichannel/cannedResponses/modals/CannedResponsesPage.tsx`** -> AI Confidence: **99.18%**
486. **`apps/meteor/client/views/omnichannel/components/AutoCompleteContact/AutoCompleteContact.tsx`** -> AI Confidence: **99.18%**
487. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/AutoCompleteOutboundProvider.tsx`** -> AI Confidence: **99.18%**
488. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/TemplatePlaceholderSelector/TemplatePlaceholderSelector.tsx`** -> AI Confidence: **99.18%**
489. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/TemplatePreview.tsx`** -> AI Confidence: **99.18%**
490. **`apps/meteor/client/views/omnichannel/components/outboundMessage/hooks/useOutboundProvidersList.ts`** -> AI Confidence: **99.18%**
491. **`apps/meteor/client/views/omnichannel/contactHistory/MessageList/useHistoryMessageList.ts`** -> AI Confidence: **99.18%**
492. **`apps/meteor/client/views/omnichannel/contactInfo/AdvancedContactModal.tsx`** -> AI Confidence: **99.18%**
493. **`apps/meteor/client/views/omnichannel/contactInfo/ContactInfo/ReviewContactModal.tsx`** -> AI Confidence: **99.18%**
494. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoChannels/useBlockChannel.tsx`** -> AI Confidence: **99.18%**
495. **`apps/meteor/client/views/omnichannel/customFields/CustomFieldsPage.tsx`** -> AI Confidence: **99.18%**
496. **`apps/meteor/client/views/omnichannel/departments/DepartmentAgentsTable/AddAgent.tsx`** -> AI Confidence: **99.18%**
497. **`apps/meteor/client/views/omnichannel/directory/components/ContactField.tsx`** -> AI Confidence: **99.18%**
498. **`apps/meteor/client/views/omnichannel/directory/components/PriorityField.tsx`** -> AI Confidence: **99.18%**
499. **`apps/meteor/client/views/omnichannel/directory/components/SlaField.tsx`** -> AI Confidence: **99.18%**
500. **`apps/meteor/client/views/omnichannel/directory/components/SourceField.tsx`** -> AI Confidence: **99.18%**
501. **`apps/meteor/client/views/omnichannel/hooks/useOmnichannelPrioritiesConfig.ts`** -> AI Confidence: **99.18%**
502. **`apps/meteor/client/views/omnichannel/hooks/useOmnichannelPrioritiesMenu.tsx`** -> AI Confidence: **99.18%**
503. **`apps/meteor/client/views/omnichannel/priorities/PriorityEditForm.tsx`** -> AI Confidence: **99.18%**
504. **`apps/meteor/client/views/omnichannel/reports/ReportsPage.tsx`** -> AI Confidence: **99.18%**
505. **`apps/meteor/client/views/omnichannel/reports/hooks/useAgentsSection.tsx`** -> AI Confidence: **99.18%**
506. **`apps/meteor/client/views/omnichannel/tags/TagEditWithData.tsx`** -> AI Confidence: **99.18%**
507. **`apps/meteor/client/views/omnichannel/triggers/TriggersPage.tsx`** -> AI Confidence: **99.18%**
508. **`apps/meteor/client/views/omnichannel/triggers/actions/ActionExternalServiceUrl.tsx`** -> AI Confidence: **99.18%**
509. **`apps/meteor/client/views/omnichannel/webhooks/WebhooksPageContainer.tsx`** -> AI Confidence: **99.18%**
510. **`apps/meteor/client/views/room/E2EESetup/RoomE2EESetup.tsx`** -> AI Confidence: **99.18%**
511. **`apps/meteor/client/views/room/Header/Header.tsx`** -> AI Confidence: **99.18%**
512. **`apps/meteor/client/views/room/Header/Omnichannel/QuickActions/QuickActionOptions.tsx`** -> AI Confidence: **99.18%**
513. **`apps/meteor/client/views/room/Header/RoomToolbox/RoomToolboxE2EESetup.tsx`** -> AI Confidence: **99.18%**
514. **`apps/meteor/client/views/room/MessageList/hooks/useJumpToMessage.ts`** -> AI Confidence: **99.18%**
515. **`apps/meteor/client/views/room/RoomInvite.tsx`** -> AI Confidence: **99.18%**
516. **`apps/meteor/client/views/room/RoomOpenerEmbedded.tsx`** -> AI Confidence: **99.18%**
517. **`apps/meteor/client/views/room/composer/ComposerContainer.tsx`** -> AI Confidence: **99.18%**
518. **`apps/meteor/client/views/room/composer/ComposerFederation/ComposerFederation.tsx`** -> AI Confidence: **99.18%**
519. **`apps/meteor/client/views/room/composer/messageBox/MessageComposerFileItem.tsx`** -> AI Confidence: **99.18%**
520. **`apps/meteor/client/views/room/contextualBar/BannedUsers/BannedUsersItem.tsx`** -> AI Confidence: **99.18%**
521. **`apps/meteor/client/views/room/contextualBar/Discussions/DiscussionsList.tsx`** -> AI Confidence: **99.18%**
522. **`apps/meteor/client/views/room/contextualBar/Discussions/useDiscussionsList.ts`** -> AI Confidence: **99.18%**
523. **`apps/meteor/client/views/room/contextualBar/PruneMessages/PruneMessages.tsx`** -> AI Confidence: **99.18%**
524. **`apps/meteor/client/views/room/contextualBar/RoomFiles/RoomFiles.tsx`** -> AI Confidence: **99.18%**
525. **`apps/meteor/client/views/room/contextualBar/RoomFiles/RoomFilesWithData.tsx`** -> AI Confidence: **99.18%**
526. **`apps/meteor/client/views/room/contextualBar/RoomMembers/InviteUsers/InviteUsersWithData.tsx`** -> AI Confidence: **99.18%**
527. **`apps/meteor/client/views/room/contextualBar/Threads/components/ThreadListMessage.tsx`** -> AI Confidence: **99.18%**
528. **`apps/meteor/client/views/room/contextualBar/Threads/components/ThreadMessageList.tsx`** -> AI Confidence: **99.18%**
529. **`apps/meteor/client/views/room/contextualBar/VideoConference/VideoConfPopups/VideoConfPopup/TimedVideoConfPopup.tsx`** -> AI Confidence: **99.18%**
530. **`apps/meteor/client/views/room/hooks/useUserInfoActions/actions/useBanUserAction.tsx`** -> AI Confidence: **99.18%**
531. **`apps/meteor/client/views/room/hooks/useUserInfoActions/actions/useChangeLeaderAction.ts`** -> AI Confidence: **99.18%**
532. **`apps/meteor/client/views/room/modals/FileUploadModal/MediaPreview.tsx`** -> AI Confidence: **99.18%**
533. **`apps/meteor/client/views/room/modals/ReportMessageModal/ReportMessageModal.tsx`** -> AI Confidence: **99.18%**
534. **`apps/meteor/client/views/room/webdav/WebdavFilePickerModal/WebdavFilePickerGrid/WebdavFilePickerGrid.tsx`** -> AI Confidence: **99.18%**
535. **`apps/meteor/client/views/teams/contextualBar/channels/AddExistingModal/AddExistingModal.tsx`** -> AI Confidence: **99.18%**
536. **`apps/meteor/client/views/teams/contextualBar/channels/TeamsChannels.tsx`** -> AI Confidence: **99.18%**
537. **`apps/meteor/client/views/teams/contextualBar/channels/TeamsChannelsWithData.tsx`** -> AI Confidence: **99.18%**
538. **`apps/meteor/ee/app/api-enterprise/server/canned-responses.ts`** -> AI Confidence: **99.18%**
539. **`apps/meteor/ee/server/api/abac/index.ts`** -> AI Confidence: **99.18%**
540. **`apps/meteor/ee/server/api/audit.ts`** -> AI Confidence: **99.18%**
541. **`apps/meteor/ee/server/api/roles.ts`** -> AI Confidence: **99.18%**
542. **`apps/meteor/ee/server/api/sessions.ts`** -> AI Confidence: **99.18%**
543. **`apps/meteor/ee/server/patches/verifyContactChannel.ts`** -> AI Confidence: **99.18%**
544. **`apps/meteor/server/features/EmailInbox/EmailInbox.ts`** -> AI Confidence: **99.18%**
545. **`apps/meteor/server/methods/addAllUserToRoom.ts`** -> AI Confidence: **99.18%**
546. **`apps/meteor/server/methods/deleteUser.ts`** -> AI Confidence: **99.18%**
547. **`apps/meteor/server/methods/muteUserInRoom.ts`** -> AI Confidence: **99.18%**
548. **`apps/meteor/server/methods/readMessages.ts`** -> AI Confidence: **99.18%**
549. **`apps/meteor/server/methods/resetAvatar.ts`** -> AI Confidence: **99.18%**
550. **`apps/meteor/server/methods/sendForgotPasswordEmail.ts`** -> AI Confidence: **99.18%**
551. **`apps/meteor/server/methods/unmuteUserInRoom.ts`** -> AI Confidence: **99.18%**
552. **`apps/meteor/server/publications/settings/index.ts`** -> AI Confidence: **99.18%**
553. **`apps/meteor/server/services/image/service.ts`** -> AI Confidence: **99.18%**
554. **`apps/meteor/server/services/omnichannel/service.ts`** -> AI Confidence: **99.18%**
555. **`apps/meteor/tests/end-to-end/api/livechat/08-triggers.ts`** -> AI Confidence: **99.18%**
556. **`apps/meteor/tests/end-to-end/api/livechat/19-business-hours.ts`** -> AI Confidence: **99.18%**
557. **`apps/meteor/tests/end-to-end/api/roles.ts`** -> AI Confidence: **99.18%**
558. **`apps/meteor/tests/end-to-end/api/users.ts`** -> AI Confidence: **99.18%**
559. **`apps/meteor/tests/mocks/data.ts`** -> AI Confidence: **99.18%**
560. **`apps/meteor/tests/unit/server/services/calendar/service.tests.ts`** -> AI Confidence: **99.18%**
561. **`ee/apps/authorization-service/src/service.ts`** -> AI Confidence: **99.18%**
562. **`ee/apps/ddp-streamer/src/DDPStreamer.ts`** -> AI Confidence: **99.18%**
563. **`ee/apps/ddp-streamer/src/Streamer.ts`** -> AI Confidence: **99.18%**
564. **`ee/apps/ddp-streamer/src/service.ts`** -> AI Confidence: **99.18%**
565. **`ee/packages/abac/src/user-auto-removal.spec.ts`** -> AI Confidence: **99.18%**
566. **`ee/packages/media-calls/src/internal/agents/UserActorAgent.ts`** -> AI Confidence: **99.18%**
567. **`packages/apps-engine/deno-runtime/handlers/scheduler-handler.ts`** -> AI Confidence: **99.18%**
568. **`packages/apps-engine/src/server/accessors/MessageBuilder.ts`** -> AI Confidence: **99.18%**
569. **`packages/apps-engine/src/server/accessors/Notifier.ts`** -> AI Confidence: **99.18%**
570. **`packages/apps-engine/src/server/bridges/MessageBridge.ts`** -> AI Confidence: **99.18%**
571. **`packages/apps-engine/src/server/bridges/VideoConferenceBridge.ts`** -> AI Confidence: **99.18%**
572. **`packages/apps-engine/src/server/managers/UIActionButtonManager.ts`** -> AI Confidence: **99.18%**
573. **`packages/core-typings/src/IMessage/IMessage.ts`** -> AI Confidence: **99.18%**
574. **`packages/ddp-client/src/ClientStream.ts`** -> AI Confidence: **99.18%**
575. **`packages/ddp-client/src/DDPSDK.ts`** -> AI Confidence: **99.18%**
576. **`packages/fuselage-ui-kit/src/elements/ChannelsSelectElement/MultiChannelsSelectElement.tsx`** -> AI Confidence: **99.18%**
577. **`packages/gazzodown/src/elements/LinkSpan.tsx`** -> AI Confidence: **99.18%**
578. **`packages/livechat/src/components/Form/stories.tsx`** -> AI Confidence: **99.18%**
579. **`packages/livechat/src/components/Messages/index.ts`** -> AI Confidence: **99.18%**
580. **`packages/livechat/src/components/uiKit/message/StaticSelectElement/index.tsx`** -> AI Confidence: **99.18%**
581. **`packages/livechat/src/providers/ServerProvider.tsx`** -> AI Confidence: **99.18%**
582. **`packages/models/src/models/Sessions.ts`** -> AI Confidence: **99.18%**
583. **`packages/release-action/src/utils.ts`** -> AI Confidence: **99.18%**
584. **`packages/rest-typings/src/apps/index.ts`** -> AI Confidence: **99.18%**
585. **`packages/rest-typings/src/v1/teams/index.ts`** -> AI Confidence: **99.18%**
586. **`packages/ui-client/src/views/setupWizard/SetupWizardRoute.tsx`** -> AI Confidence: **99.18%**
587. **`packages/ui-client/src/views/setupWizard/providers/SetupWizardProvider.tsx`** -> AI Confidence: **99.18%**
588. **`packages/ui-client/src/views/setupWizard/steps/OrganizationInfoStep.tsx`** -> AI Confidence: **99.18%**
589. **`packages/ui-kit/src/rendering/ActionOf.ts`** -> AI Confidence: **99.18%**
590. **`packages/ui-voip/src/views/MediaCallHistoryTable/CallHistoryTableRow.tsx`** -> AI Confidence: **99.18%**
591. **`packages/web-ui-registration/src/ResetPasswordForm.tsx`** -> AI Confidence: **99.18%**
592. **`packages/web-ui-registration/src/SecretRegisterForm.tsx`** -> AI Confidence: **99.18%**
593. **`packages/web-ui-registration/src/components/LoginSwitchLanguageFooter.tsx`** -> AI Confidence: **99.18%**
594. **`apps/meteor/app/irc/server/servers/RFC2813/localCommandHandlers.js`** -> AI Confidence: **99.17%**
595. **`apps/meteor/app/irc/server/servers/RFC2813/parseMessage.js`** -> AI Confidence: **99.17%**
596. **`apps/meteor/app/file-upload/server/methods/isImagePreviewSupported.ts`** -> AI Confidence: **99.17%**
597. **`apps/meteor/app/utils/lib/getDefaultSubscriptionPref.ts`** -> AI Confidence: **99.17%**
598. **`apps/meteor/app/utils/server/placeholders.ts`** -> AI Confidence: **99.17%**
599. **`apps/meteor/client/cachedStores/SubscriptionsCachedStore.ts`** -> AI Confidence: **99.17%**
600. **`apps/meteor/client/views/account/profile/getProfileInitialValues.ts`** -> AI Confidence: **99.17%**
601. **`apps/meteor/client/views/omnichannel/departments/utils/getFormInititalValues.ts`** -> AI Confidence: **99.17%**
602. **`apps/meteor/definition/externals/meteor/http.d.ts`** -> AI Confidence: **99.17%**
603. **`apps/meteor/ee/server/local-services/instance/getTransporter.ts`** -> AI Confidence: **99.17%**
604. **`apps/meteor/playwright.config.ts`** -> AI Confidence: **99.17%**
605. **`apps/meteor/server/services/messages/hooks/BeforeSaveSpotify.ts`** -> AI Confidence: **99.17%**
606. **`apps/meteor/server/startup/migrations/v323.ts`** -> AI Confidence: **99.17%**
607. **`apps/meteor/server/ufs/ufs-config.ts`** -> AI Confidence: **99.17%**
608. **`packages/apps-engine/src/definition/email/IEmail.ts`** -> AI Confidence: **99.17%**
609. **`packages/apps-engine/src/definition/rooms/IRoomRaw.ts`** -> AI Confidence: **99.17%**
610. **`packages/apps-engine/src/definition/users/IUserCreationOptions.ts`** -> AI Confidence: **99.17%**
611. **`packages/apps-engine/src/server/permissions/AppPermissions.ts`** -> AI Confidence: **99.17%**
612. **`packages/core-typings/src/IPermission.ts`** -> AI Confidence: **99.17%**
613. **`packages/core-typings/src/IServerInfo.ts`** -> AI Confidence: **99.17%**
614. **`packages/core-typings/src/IUpload.ts`** -> AI Confidence: **99.17%**
615. **`packages/core-typings/src/import/IImportChannel.ts`** -> AI Confidence: **99.17%**
616. **`packages/core-typings/src/import/IImportContact.ts`** -> AI Confidence: **99.17%**
617. **`packages/core-typings/src/import/IImportMessage.ts`** -> AI Confidence: **99.17%**
618. **`packages/core-typings/src/import/IImportUser.ts`** -> AI Confidence: **99.17%**
619. **`packages/livechat/src/definitions/agents.d.ts`** -> AI Confidence: **99.17%**
620. **`packages/livechat/src/lib/email.ts`** -> AI Confidence: **99.17%**
621. **`packages/model-typings/src/models/IRoomsModel.ts`** -> AI Confidence: **99.17%**
622. **`packages/model-typings/src/models/ISubscriptionsModel.ts`** -> AI Confidence: **99.17%**
623. **`packages/models/src/models/setUpdatedAt.ts`** -> AI Confidence: **99.17%**
624. **`packages/sha256/src/utf8Encode.ts`** -> AI Confidence: **99.17%**
625. **`packages/tools/src/isRecord.spec.ts`** -> AI Confidence: **99.17%**
626. **`packages/tools/src/validateEmail.ts`** -> AI Confidence: **99.17%**
627. **`packages/ui-voip/src/views/MediaCallWidget/OngoingCallWithScreen.tsx`** -> AI Confidence: **99.17%**
628. **`scripts/todo-issue/src/diff.ts`** -> AI Confidence: **99.17%**
629. **`apps/meteor/install.sh`** -> AI Confidence: **99.17%**
630. **`apps/meteor/tests/e2e/containers/saml/config/simplesamlphp/config.php`** -> AI Confidence: **99.17%**
631. **`packages/livechat/src/components/Screen/index.js`** -> AI Confidence: **99.16%**
632. **`apps/meteor/app/2fa/server/code/EmailCheck.ts`** -> AI Confidence: **99.16%**
633. **`apps/meteor/app/api/server/v1/groups.ts`** -> AI Confidence: **99.16%**
634. **`apps/meteor/app/api/server/v1/misc.ts`** -> AI Confidence: **99.16%**
635. **`apps/meteor/app/api/server/v1/rooms.ts`** -> AI Confidence: **99.16%**
636. **`apps/meteor/app/api/server/v1/users.ts`** -> AI Confidence: **99.16%**
637. **`apps/meteor/app/apps/server/bridges/messages.ts`** -> AI Confidence: **99.16%**
638. **`apps/meteor/app/apps/server/bridges/users.ts`** -> AI Confidence: **99.16%**
639. **`apps/meteor/app/channel-settings/server/functions/saveRoomEncrypted.ts`** -> AI Confidence: **99.16%**
640. **`apps/meteor/app/cloud/server/methods.ts`** -> AI Confidence: **99.16%**
641. **`apps/meteor/app/file-upload/ufs/AmazonS3/server.ts`** -> AI Confidence: **99.16%**
642. **`apps/meteor/app/importer-pending-files/server/PendingFileImporter.ts`** -> AI Confidence: **99.16%**
643. **`apps/meteor/app/livechat/imports/server/rest/users.ts`** -> AI Confidence: **99.16%**
644. **`apps/meteor/app/livechat/server/api/v1/agent.ts`** -> AI Confidence: **99.16%**
645. **`apps/meteor/app/livechat/server/api/v1/visitor.ts`** -> AI Confidence: **99.16%**
646. **`apps/meteor/app/livechat/server/startup.ts`** -> AI Confidence: **99.16%**
647. **`apps/meteor/app/mailer/server/api.ts`** -> AI Confidence: **99.16%**
648. **`apps/meteor/app/message-pin/server/pinMessage.ts`** -> AI Confidence: **99.16%**
649. **`apps/meteor/app/slashcommands-archiveroom/server/server.ts`** -> AI Confidence: **99.16%**
650. **`apps/meteor/app/slashcommands-unarchiveroom/server/server.ts`** -> AI Confidence: **99.16%**
651. **`apps/meteor/client/apps/orchestrator.ts`** -> AI Confidence: **99.16%**
652. **`apps/meteor/client/components/CreateDiscussion/CreateDiscussion.tsx`** -> AI Confidence: **99.16%**
653. **`apps/meteor/client/components/GazzodownText.tsx`** -> AI Confidence: **99.16%**
654. **`apps/meteor/client/components/avatar/RoomAvatarEditor.tsx`** -> AI Confidence: **99.16%**
655. **`apps/meteor/client/components/avatar/UserAvatarEditor/UserAvatarEditor.tsx`** -> AI Confidence: **99.16%**
656. **`apps/meteor/client/components/message/MessageHeader.tsx`** -> AI Confidence: **99.16%**
657. **`apps/meteor/client/components/message/content/attachments/QuoteAttachment.tsx`** -> AI Confidence: **99.16%**
658. **`apps/meteor/client/components/message/content/attachments/file/GenericFileAttachment.tsx`** -> AI Confidence: **99.16%**
659. **`apps/meteor/client/components/message/variants/SystemMessage.tsx`** -> AI Confidence: **99.16%**
660. **`apps/meteor/client/components/message/variants/ThreadMessage.tsx`** -> AI Confidence: **99.16%**
661. **`apps/meteor/client/providers/AuthenticationProvider/AuthenticationProvider.tsx`** -> AI Confidence: **99.16%**
662. **`apps/meteor/client/sidebar/header/MatrixFederationSearch/FederatedRoomList.tsx`** -> AI Confidence: **99.16%**
663. **`apps/meteor/client/views/admin/ABAC/ABACAttributesTab/AttributesPage.tsx`** -> AI Confidence: **99.16%**
664. **`apps/meteor/client/views/admin/ABAC/AdminABACPage.tsx`** -> AI Confidence: **99.16%**
665. **`apps/meteor/client/views/admin/ABAC/AdminABACRoute.tsx`** -> AI Confidence: **99.16%**
666. **`apps/meteor/client/views/admin/engagementDashboard/EngagementDashboardPage.tsx`** -> AI Confidence: **99.16%**
667. **`apps/meteor/client/views/admin/import/ImportProgressPage.tsx`** -> AI Confidence: **99.16%**
668. **`apps/meteor/client/views/admin/import/ImportRoute.tsx`** -> AI Confidence: **99.16%**
669. **`apps/meteor/client/views/admin/integrations/IntegrationsRoute.tsx`** -> AI Confidence: **99.16%**
670. **`apps/meteor/client/views/admin/moderation/UserReports/UserReportInfo.tsx`** -> AI Confidence: **99.16%**
671. **`apps/meteor/client/views/admin/permissions/PermissionsContextBar.tsx`** -> AI Confidence: **99.16%**
672. **`apps/meteor/client/views/admin/settings/Setting/MemoizedSetting.tsx`** -> AI Confidence: **99.16%**
673. **`apps/meteor/client/views/admin/settings/groups/LDAPGroupPage.tsx`** -> AI Confidence: **99.16%**
674. **`apps/meteor/client/views/admin/users/AdminUserInfoWithData.tsx`** -> AI Confidence: **99.16%**
675. **`apps/meteor/client/views/admin/users/hooks/useAdminUserInfoActions.ts`** -> AI Confidence: **99.16%**
676. **`apps/meteor/client/views/admin/workspace/WorkspacePage.tsx`** -> AI Confidence: **99.16%**
677. **`apps/meteor/client/views/composer/EmojiPicker/EmojiPicker.tsx`** -> AI Confidence: **99.16%**
678. **`apps/meteor/client/views/directory/tabs/teams/TeamsTable/TeamsTable.tsx`** -> AI Confidence: **99.16%**
679. **`apps/meteor/client/views/home/DefaultHomePage.tsx`** -> AI Confidence: **99.16%**
680. **`apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppLogs/AppLogsItem.tsx`** -> AI Confidence: **99.16%**
681. **`apps/meteor/client/views/marketplace/hooks/useAppInstallationHandler.tsx`** -> AI Confidence: **99.16%**
682. **`apps/meteor/client/views/marketplace/hooks/useFilteredApps.ts`** -> AI Confidence: **99.16%**
683. **`apps/meteor/client/views/mediaCallHistory/CallHistoryPage.tsx`** -> AI Confidence: **99.16%**
684. **`apps/meteor/client/views/omnichannel/agents/AgentInfo.tsx`** -> AI Confidence: **99.16%**
685. **`apps/meteor/client/views/omnichannel/cannedResponses/components/CannedResponseForm.tsx`** -> AI Confidence: **99.16%**
686. **`apps/meteor/client/views/omnichannel/cannedResponses/contextualBar/CannedResponse/WrapCannedResponseList.tsx`** -> AI Confidence: **99.16%**
687. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/forms/MessageForm/MessageForm.tsx`** -> AI Confidence: **99.16%**
688. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/forms/RecipientForm/components/ChannelField.tsx`** -> AI Confidence: **99.16%**
689. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/forms/RecipientForm/components/ContactField.tsx`** -> AI Confidence: **99.16%**
690. **`apps/meteor/client/views/omnichannel/components/outboundMessage/components/OutboundMessageWizard/forms/RepliesForm/RepliesForm.tsx`** -> AI Confidence: **99.16%**
691. **`apps/meteor/client/views/omnichannel/contactInfo/ContactInfo/ContactInfo.tsx`** -> AI Confidence: **99.16%**
692. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoDetails/ContactInfoDetails.tsx`** -> AI Confidence: **99.16%**
693. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoDetails/ContactInfoPhoneEntry.tsx`** -> AI Confidence: **99.16%**
694. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoHistory/ContactInfoHistory.tsx`** -> AI Confidence: **99.16%**
695. **`apps/meteor/client/views/omnichannel/contactInfo/tabs/ContactInfoHistory/ContactInfoHistoryItem.tsx`** -> AI Confidence: **99.16%**
696. **`apps/meteor/client/views/omnichannel/departments/DepartmentsTable/DepartmentItemMenu.tsx`** -> AI Confidence: **99.16%**
697. **`apps/meteor/client/views/omnichannel/directory/OmnichannelDirectoryPage.tsx`** -> AI Confidence: **99.16%**
698. **`apps/meteor/client/views/omnichannel/directory/chats/ChatsTable/ChatsTableRow.tsx`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `packages/ui-client/src/components/PasswordVerifier/PasswordVerifiers.spec.tsx` -> **100.0%** Exposure
- `apps/meteor/server/configuration/pushNotification.ts` -> **99.7127%** Exposure
- `apps/meteor/tests/end-to-end/api/livechat/11-email-inbox.ts` -> **99.1938%** Exposure
- `apps/meteor/tests/unit/app/meteor-accounts-saml/data.ts` -> **87.2818%** Exposure
- `apps/meteor/tests/end-to-end/api/users.ts` -> **86.7387%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `15070` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/media-signaling/src/lib/media/MediaStreamTrackWrapper.ts` (TYPESCRIPT) -> Cumulative Risk: **761.96**
- **Archetype:** `file_cluster_4` (Distance: 14.221 IQR)
- **Magnitude:** 20.35 | **LOC:** 149 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8968%)
- **Heaviest Functions:** `constructor` (Impact: 12.2), `setMuted` (Impact: 10.6), `ended` (Impact: 4.2)

### 2. `apps/meteor/app/ui-message/client/ActionManager.ts` (TYPESCRIPT) -> Cumulative Risk: **757.81**
- **Archetype:** `file_cluster_4` (Distance: 13.199 IQR)
- **Magnitude:** 34.89 | **LOC:** 314 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9997%), Concurrency (99.9934%)
- **Heaviest Functions:** `handleServerInteraction` (Impact: 50.3), `emitInteraction` (Impact: 24.0), `async` (Impact: 21.9)

### 3. `packages/agenda/src/Job.ts` (TYPESCRIPT) -> Cumulative Risk: **750.39**
- **Archetype:** `file_cluster_4` (Distance: 14.491 IQR)
- **Magnitude:** 45.4 | **LOC:** 294 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `debug` (Impact: 46.2), `_computeFromInterval` (Impact: 44.3), `debug` (Impact: 11.8)

### 4. `apps/meteor/server/email/IMAPInterceptor.ts` (TYPESCRIPT) -> Cumulative Risk: **746.78**
- **Archetype:** `file_cluster_4` (Distance: 13.933 IQR)
- **Magnitude:** 48.8 | **LOC:** 244 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9684%)
- **Heaviest Functions:** `on` (Impact: 52.3), `imapFetch` (Impact: 12.4), `messagecb` (Impact: 11.4)

### 5. `packages/ddp-client/src/Connection.ts` (TYPESCRIPT) -> Cumulative Risk: **744.76**
- **Archetype:** `file_cluster_4` (Distance: 13.943 IQR)
- **Magnitude:** 24.89 | **LOC:** 222 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Safety Score (99.0144%)
- **Heaviest Functions:** `connect` (Impact: 14.4), `super` (Impact: 7.7), `onopen` (Impact: 6.5)

### 6. `packages/ui-voip/src/hooks/useTonePlayer.ts` (TYPESCRIPT) -> Cumulative Risk: **742.21**
- **Archetype:** `file_cluster_4` (Distance: 12.9 IQR)
- **Magnitude:** 11.52 | **LOC:** 125 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (94.6665%)
- **Heaviest Functions:** `play` (Impact: 17.1), `useTonePlayer` (Impact: 13.3), `setSinkId` (Impact: 4.8)

### 7. `apps/meteor/app/api/server/v1/rooms.ts` (TYPESCRIPT) -> Cumulative Risk: **738.39**
- **Archetype:** `file_cluster_4` (Distance: 12.453 IQR)
- **Magnitude:** 146.1 | **LOC:** 1386 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 17.6%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9777%)
- **Heaviest Functions:** `post` (Impact: 36.2), `post` (Impact: 28.1), `get` (Impact: 17.8)

### 8. `apps/meteor/app/apps/server/bridges/api.ts` (TYPESCRIPT) -> Cumulative Risk: **733.3**
- **Archetype:** `file_cluster_4` (Distance: 13.006 IQR)
- **Magnitude:** 12.88 | **LOC:** 128 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9961%)
- **Heaviest Functions:** `_appApiExecutor` (Impact: 15.2), `constructor` (Impact: 8.2), `_verifyApi` (Impact: 5.6)

### 9. `packages/agenda/src/Agenda.ts` (TYPESCRIPT) -> Cumulative Risk: **725.64**
- **Archetype:** `file_cluster_4` (Distance: 14.388 IQR)
- **Magnitude:** 122.79 | **LOC:** 985 | **CtrlFlow:** 58.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.994%)
- **Heaviest Functions:** `_runOrRetry` (Impact: 33.4), `_findAndLockNextJob` (Impact: 32.7), `_lockOnTheFly` (Impact: 21.8)

### 10. `packages/ui-voip/src/providers/useMediaSessionInstance.ts` (TYPESCRIPT) -> Cumulative Risk: **724.92**
- **Archetype:** `file_cluster_13` (Distance: 12.486 IQR)
- **Magnitude:** 18.67 | **LOC:** 195 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.997%), Safety Score (89.1414%)
- **Heaviest Functions:** `makeInstance` (Impact: 13.9), `useMediaSessionInstance` (Impact: 12.2), `getInstance` (Impact: 10.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/ee/server/services/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/hs1/hs1.signing.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/ca/rootCA.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/element-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/element.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/hs1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/hs1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/rc1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ee/packages/federation-matrix/docker-compose/traefik/certs/rc1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/livechat/src/routes/Chat/container.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.701 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.115 IQR)
- **Top Global Matches:** file_cluster_4: 13.701, file_cluster_17: 14.203, file_cluster_13: 14.232
- **Magnitude:** 830.22 | **LOC:** 426 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `useQueuePositionChangeSubscription` (Impact: 164.7)
  * `componentDidUpdate` (Impact: 22.1)
  * `onFinishChat` (Impact: 13.6)
  * `doFileUpload` (Impact: 13.3)
  * `handleSubmit` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 114`, `args: 37`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 176`
* *Architecture:* `api: 5`, `concurrency: 286`, `import: 22`
* *Defense:* `safety: 35`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` throttle, react-i18next, room, baseUrl, component, useRoomMessagesSubscription, api, constants...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/00-rooms.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.051 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.054 IQR)
- **Top Global Matches:** file_cluster_4: 13.051, file_cluster_8: 13.686, file_cluster_17: 13.765
- **Magnitude:** 508.21 | **LOC:** 3861 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 151.9)
  * `describe` (Impact: 78.3)
  * `describe` (Impact: 73.9)
  * `describe` (Impact: 48.0)
  * `describe` (Impact: 47.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 1188`, `args: 741`, `func_start: 667`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 510`, `planned_debt: 5`, `duplicate_logic: 304`
* *Architecture:* `io: 24`, `api: 1`, `concurrency: 2862`, `import: 26`
* *Defense:* `safety: 135`, `test: 833`, `immutability_locks: 269`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` units, tags, utils, path, api-data, mocha, priorities, apps-data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 466.16 | **LOC:** 23308 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/app/custom-oauth/server/custom_oauth_server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.217 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.746 IQR)
- **Top Global Matches:** file_cluster_4: 13.217, file_cluster_13: 13.581, file_cluster_0: 13.859
- **Magnitude:** 461.16 | **LOC:** 552 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (37.2482%)
**Top Internal Functions/Classes:**
  * `getAccessToken` (Impact: 49.2)
  * `configure` (Impact: 31.2)
  * `normalizeIdentity` (Impact: 20.8)
  * `updateOrCreateUserFromExternalService` (Impact: 10.2)
  * `getEmailFromPath` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 51`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 228`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 84`, `import: 18`
* *Defense:* `safety: 8`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` server, meteor, check, server-fetch, notifyListener, oauth, oauth, service-configuration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `apps/meteor/app/apps/server/converters/rooms.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.593 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.866 IQR)
- **Top Global Matches:** file_cluster_4: 11.593, file_cluster_8: 11.909, file_cluster_11: 12.244
- **Magnitude:** 427.18 | **LOC:** 458 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `convertAppRoom` (Impact: 61.7)
  * `convertRoom` (Impact: 37.5)
  * `convertRoomRaw` (Impact: 24.7)
  * `__getRoomCloser` (Impact: 11.6)
  * `mapUserLookup` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 123`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 5`, `concurrency: 105`, `import: 3`
* *Defense:* `safety: 34`, `immutability_locks: 41`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` transformMappedData, rooms, models
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/abac.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.142 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.198 IQR)
- **Top Global Matches:** file_cluster_4: 12.142, file_cluster_8: 12.688, file_cluster_17: 13.055
- **Magnitude:** 396.55 | **LOC:** 2617 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 68.7)
  * `describe` (Impact: 59.6)
  * `describe` (Impact: 50.4)
  * `describe` (Impact: 29.1)
  * `describe` (Impact: 25.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 775`, `args: 625`, `func_start: 437`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 385`, `duplicate_logic: 220`
* *Architecture:* `api: 10`, `concurrency: 2453`, `import: 13`
* *Defense:* `safety: 23`, `test: 690`, `immutability_locks: 166`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` teams.helper, permissions.helper, mocha, api-data, mongodb, api-client, rooms.helper, users.helper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/rooms.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.527 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.556 IQR)
- **Top Global Matches:** file_cluster_4: 12.527, file_cluster_8: 12.765, file_cluster_17: 13.199
- **Magnitude:** 387.7 | **LOC:** 4591 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 135.6)
  * `describe` (Impact: 50.6)
  * `describe` (Impact: 40.1)
  * `describe` (Impact: 40.0)
  * `describe` (Impact: 39.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 1150`, `args: 1226`, `func_start: 992`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 490`, `duplicate_logic: 374`
* *Architecture:* `io: 43`, `api: 50`, `concurrency: 1700`, `import: 20`
* *Defense:* `safety: 162`, `test: 1411`, `immutability_locks: 141`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` chat.helper, teams.helper, path, permissions.helper, mocha, api-data, sleep, roles.helper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/unit/app/mentions/client.tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.601 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 7.386 IQR)
- **Top Global Matches:** file_cluster_8: 9.601, file_cluster_0: 9.82, file_cluster_15: 10.287
- **Magnitude:** 344.12 | **LOC:** 315 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2887%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 49.9)
  * `describe` (Impact: 32.0)
  * `describe` (Impact: 18.8)
  * `describe` (Impact: 14.8)
  * `describe` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 106`, `args: 70`, `func_start: 94`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 1`, `duplicate_logic: 59`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* `test: 91`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chai, MentionsParser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 322.86 | **LOC:** 16143 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/end-to-end/api/livechat/contacts.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.679 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.927 IQR)
- **Top Global Matches:** file_cluster_4: 12.679, file_cluster_8: 13.238, file_cluster_13: 13.615
- **Magnitude:** 288.62 | **LOC:** 1882 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 174.0)
  * `describe` (Impact: 54.1)
  * `describe` (Impact: 38.3)
  * `describe` (Impact: 24.7)
  * `describe` (Impact: 24.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 500`, `args: 585`, `func_start: 581`
* *Risk/State:* `state_mutation: 272`, `duplicate_logic: 193`
* *Architecture:* `api: 8`, `concurrency: 1524`, `import: 13`
* *Defense:* `safety: 49`, `test: 540`, `immutability_locks: 162`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` permissions.helper, api-data, mocha, constants, rooms, api-client, validation.helper, users...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/app/apps/server/converters/messages.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.009 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.304 IQR)
- **Top Global Matches:** file_cluster_4: 11.009, file_cluster_8: 11.274, file_cluster_13: 11.438
- **Magnitude:** 285.92 | **LOC:** 342 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertAppMessage` (Impact: 58.3)
  * `convertMessage` (Impact: 19.8)
  * `_convertAttachmentsToApp` (Impact: 17.0)
  * `_convertAppAttachments` (Impact: 16.1)
  * `fileId` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `api: 4`, `concurrency: 70`, `import: 7`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 20`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` cachedFunction, convertMessageFiles, tools, core-typings, models, transformMappedData, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/tests/unit/app/utils/lib/getURL.tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.68 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_8: 9.68, file_cluster_13: 10.135, file_cluster_0: 10.288
- **Magnitude:** 277.62 | **LOC:** 163 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.5249%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testCases` (Impact: 72.8)
  * `testPaths` (Impact: 25.6)
  * `testPaths` (Impact: 16.4)
  * `describe` (Impact: 11.9)
  * `testPaths` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 47`, `args: 30`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 3`, `duplicate_logic: 39`, `orphaned_logic: 1`
* *Architecture:* `io: 47`, `import: 3`
* *Defense:* `safety: 3`, `test: 25`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` proxyquire, chai, stringUtils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/packages/meteor-cookies/cookies.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.263 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.967 IQR)
- **Top Global Matches:** file_cluster_11: 14.263, file_cluster_13: 14.268, file_cluster_8: 14.387
- **Magnitude:** 276.88 | **LOC:** 618 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1241%), Tech Debt (18.6122%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 23.2)
  * `deserialize` (Impact: 18.6)
  * `constructor` (Impact: 18.0)
  * `parse` (Impact: 15.2)
    * *Intent:* * @license * (The MIT License) * * Copyright (c) 2012-2014 Roman Shtylman <shtylman@gmail.com> * Cop...
  * `get` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 51`, `args: 16`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 1`, `import: 3`
* *Defense:* `safety: 29`, `doc: 41`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` meteor, fetch, webapp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/livechat/src/lib/triggers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.383 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.408 IQR)
- **Top Global Matches:** file_cluster_4: 13.383, file_cluster_17: 13.764, file_cluster_13: 13.801
- **Magnitude:** 259.8 | **LOC:** 210 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.056%), Tech Debt (74.0465%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 42.3)
  * `when` (Impact: 15.4)
  * `fire` (Impact: 8.7)
  * `init` (Impact: 6.8)
  * `schedule` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 40`, `args: 30`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 49`, `import: 6`
* *Defense:* `safety: 13`, `doc: 6`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` api, emitter, triggerActions, triggerConditions, triggerUtils, store
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/meteor/ee/server/apps/orchestrator.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.77 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_4: 12.77, file_cluster_13: 12.956, file_cluster_0: 13.288
- **Magnitude:** 236.02 | **LOC:** 402 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (89.5665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 10.1)
  * `triggerEvent` (Impact: 7.7)
  * `load` (Impact: 6.0)
  * `updateAppsMarketplaceInfo` (Impact: 4.8)
    * *Intent:* // This needs to happen sequentially to keep track of app limits
  * `getLogStorage` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 51`, `args: 28`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 108`
* *Architecture:* `io: 6`, `api: 18`, `concurrency: 43`, `import: 18`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` meteor, path, isTesting, AppManager, os, MarketplaceAPIClient, canEnableApp, storage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ee/packages/federation-matrix/src/types/ICallbacks.ts` (TYPESCRIPT) | Magnitude: 1.08 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 8, branch: 4, args: 4
- `apps/meteor/app/statistics/server/functions/sendUsageReport.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 18, import: 10, concurrency: 5
- `apps/meteor/server/services/authorization/canAccessRoom.ts` (TYPESCRIPT) | Magnitude: 11.08 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 34, branch: 33, concurrency: 17
- `ee/packages/omni-core-ee/src/isDepartmentCreationAvailable.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 6, args: 2, api: 2
- `apps/meteor/app/utils/lib/templateVarHandler.ts` (TYPESCRIPT) | Magnitude: 2.76 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 24, state_mutation: 9, branch: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `apps/meteor/packages/meteor-cookies/cookies.js` (JAVASCRIPT) | Magnitude: 276.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 211, state_mutation: 162, branch: 95, structural_boundaries: 51
- `apps/meteor/client/router/index.tsx` (TYPESCRIPT) | Magnitude: 31.15 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 242, state_mutation: 182, branch: 66, structural_boundaries: 55
- `apps/meteor/client/router/page.ts` (TYPESCRIPT) | Magnitude: 44.98 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 169, state_mutation: 161, branch: 70, io: 58
- `packages/random/src/AleaRandomGenerator.ts` (TYPESCRIPT) | Magnitude: 9.04 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 74, state_mutation: 28, structural_boundaries: 15, args: 11
- `packages/models/src/proxify.ts` (TYPESCRIPT) | Magnitude: 5.96 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 24, branch: 11, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `apps/meteor/client/views/room/hooks/useFirstUnreadMessageId.ts` (TYPESCRIPT) | Magnitude: 0.65 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 5, import: 2, immutability_locks: 2
- `apps/meteor/client/views/root/hooks/useEmojiOne.ts` (TYPESCRIPT) | Magnitude: 4.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 13, branch: 8, args: 6
- `apps/meteor/tests/e2e/federation/utils/register-user.ts` (TYPESCRIPT) | Magnitude: 0.69 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 7, concurrency: 3, import: 3
- `ee/packages/abac/src/pdp/LocalPDP.ts` (TYPESCRIPT) | Magnitude: 4.45 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 76, structural_boundaries: 24, concurrency: 12, branch: 10
- `packages/model-typings/src/models/IIntegrationHistoryModel.ts` (TYPESCRIPT) | Magnitude: 5.55 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, generics: 9, ui_framework: 8, indent_tabs: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/model-typings/src/models/ILivechatBusinessHoursModel.ts` (TYPESCRIPT) | Magnitude: 43.09 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 28, generics: 20, structural_boundaries: 17, ui_framework: 14
- `packages/core-typings/src/IOmnichannelAgent.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, api: 2, class_start: 1, generics: 1
- `packages/model-typings/src/models/INpsModel.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 9, generics: 9, ui_framework: 7
- `apps/meteor/definition/externals/meteor/accounts-base.d.ts` (TYPESCRIPT) | Magnitude: 2.22 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 57, args: 21, func_start: 19, structural_boundaries: 17
- `packages/core-typings/src/federation/v1/IFederationServer.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, class_start: 1, api: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `apps/meteor/client/views/admin/import/PrepareChannels.tsx` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 74, structural_boundaries: 27, ui_framework: 24, generics: 16
- `apps/meteor/client/views/teams/contextualBar/info/ConvertToChannelModal/BaseConvertToChannelModal.tsx` (TYPESCRIPT) | Magnitude: 1.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 55, structural_boundaries: 23, ui_framework: 15, branch: 13
- `apps/meteor/app/livechat/imports/server/rest/appearance.ts` (TYPESCRIPT) | Magnitude: 8.19 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 107, structural_boundaries: 35, branch: 20, state_mutation: 13
- `apps/meteor/client/meteor/minimongo/Cursor.ts` (TYPESCRIPT) | Magnitude: 89.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 609, state_mutation: 315, branch: 205, structural_boundaries: 149
- `apps/meteor/client/views/marketplace/AppDetailsPage/tabs/AppLogs/AppLogs.tsx` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 97, structural_boundaries: 50, branch: 41, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `apps/meteor/client/views/room/contextualBar/Threads/components/ThreadListMessage.tsx` (TYPESCRIPT) | Magnitude: 0.41 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 65, ui_framework: 17, structural_boundaries: 16, generics: 16
- `packages/model-typings/src/models/ISessionsModel.ts` (TYPESCRIPT) | Magnitude: 8.25 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 116, generics: 45, concurrency: 41, ui_framework: 34
- `apps/meteor/client/views/admin/settings/Setting/inputs/IntSettingInput.tsx` (TYPESCRIPT) | Magnitude: 0.71 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 11, ui_framework: 8, generics: 8
- `packages/ui-client/src/components/Page/Page.stories.tsx` (TYPESCRIPT) | Magnitude: 1.35 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 21, ui_framework: 19, generics: 19
- `apps/meteor/client/views/omnichannel/cannedResponses/components/CannedResponsesComposer/CannedResponsesComposer.tsx` (TYPESCRIPT) | Magnitude: 5.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 99, ui_framework: 27, structural_boundaries: 25, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `apps/meteor/app/emoji-custom/server/methods/deleteEmojiCustom.ts` (TYPESCRIPT) | Magnitude: 2.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 20, concurrency: 12, import: 7
- `apps/meteor/client/views/root/hooks/useIframe.ts` (TYPESCRIPT) | Magnitude: 12.11 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 70, branch: 23, structural_boundaries: 18, immutability_locks: 13
- `apps/meteor/ee/app/livechat-enterprise/server/api/triggers.ts` (TYPESCRIPT) | Magnitude: 5.69 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 101, concurrency: 20, structural_boundaries: 14, immutability_locks: 13
- `apps/meteor/ee/server/configuration/videoConference.ts` (TYPESCRIPT) | Magnitude: 2.49 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 31, structural_boundaries: 28, concurrency: 20, branch: 12
- `packages/omni-core/src/isDepartmentCreationAvailable.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, concurrency: 3, decorators: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `scripts/todo-issue/src/github.ts` (TYPESCRIPT) | Magnitude: 19.44 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 201, planned_debt: 54, structural_boundaries: 48, concurrency: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/apps-engine/src/definition/accessors/IExperimentalRead.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/apps-engine/src/definition/email/IPreEmailSentContext.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 2, class_start: 1, safety: 1
- `apps/meteor/client/meteor/login/saml.ts` (TYPESCRIPT) | Magnitude: 3.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 30, branch: 16, args: 12
- `apps/meteor/server/startup/callbacks.ts` (TYPESCRIPT) | Magnitude: 0.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 9, args: 4, import: 4
- `apps/meteor/tests/end-to-end/api/subscriptions.ts` (TYPESCRIPT) | Magnitude: 30.89 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 433, test: 140, args: 119, structural_boundaries: 105
- `apps/meteor/app/autotranslate/server/functions/saveSettings.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 58, branch: 16, structural_boundaries: 14, concurrency: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/apps-engine/src/definition/uikit/blocks/Objects.ts` (TYPESCRIPT) | Magnitude: 1.83 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 7, doc: 6, class_start: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ee/packages/federation-matrix/src/FederationMatrix.ts` -> Churn: **76.24%** | Cog Load: 99.9922% | Debt: 11.0874%
- `ee/packages/federation-matrix/src/events/member.ts` -> Churn: **61.16%** | Cog Load: 89.1445% | Debt: 15.4885%
- `apps/meteor/server/services/room/service.ts` -> Churn: **58.67%** | Cog Load: 100.0% | Debt: 10.238%
- `apps/meteor/server/services/media-call/service.ts` -> Churn: **55.42%** | Cog Load: 100.0% | Debt: 0.0%
- `packages/media-signaling/src/lib/Call.ts` -> Churn: **55.33%** | Cog Load: 87.6141% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `apps/meteor/app/apps/server/converters/rooms.js` -> **デワンシュ** (100.0% isolated ownership) | Magnitude: 427.18
- `apps/meteor/tests/end-to-end/api/livechat/contacts.ts` -> **Abhinav Kumar** (100.0% isolated ownership) | Magnitude: 288.62
- `apps/meteor/app/apps/server/converters/messages.js` -> **Pierre Lehnen** (100.0% isolated ownership) | Magnitude: 285.92
- `apps/meteor/tests/end-to-end/api/livechat/11-livechat.ts` -> **Júlia Jaeger Foresti** (100.0% isolated ownership) | Magnitude: 210.65
- `apps/meteor/packages/rocketchat-version/plugin/compile-version.js` -> **Guilherme Gazzo** (100.0% isolated ownership) | Magnitude: 178.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/apps-engine/src/server/AppManager.ts` -> **Severity: 0.162** (Bridge: 0.0016 * Flux: 100.0%)
- `packages/apps-engine/src/server/managers/UIActionButtonManager.ts` -> **Severity: 0.158** (Bridge: 0.0016 * Flux: 100.0%)
- `apps/meteor/app/apps/server/bridges/bridges.js` -> **Severity: 0.096** (Bridge: 0.001 * Flux: 99.9998%)
- `packages/apps-engine/src/server/ProxiedApp.ts` -> **Severity: 0.083** (Bridge: 0.0008 * Flux: 99.9908%)
- `apps/meteor/app/apps/server/bridges/activation.ts` -> **Severity: 0.081** (Bridge: 0.0008 * Flux: 97.1417%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `apps/meteor/client/views/room/contexts/RoomContext.ts` -> **Severity: 353.4** (Blast Radius: 3.534 * Doc Risk: 100.0%)
- `apps/meteor/app/apps/server/bridges/bridges.js` -> **Severity: 326.6** (Blast Radius: 3.266 * Doc Risk: 100.0%)
- `packages/livechat/src/lib/locale.js` -> **Severity: 314.682** (Blast Radius: 3.372 * Doc Risk: 93.322%)
- `packages/message-parser/src/definitions.ts` -> **Severity: 240.7** (Blast Radius: 2.407 * Doc Risk: 100.0%)
- `packages/livechat/src/lib/hooks.ts` -> **Severity: 220.5** (Blast Radius: 2.205 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
