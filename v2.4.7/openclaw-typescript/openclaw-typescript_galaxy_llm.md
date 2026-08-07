# ARCHITECTURAL_BRIEF: openclaw-typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/openclaw-typescript` |
| **Timestamp** | `2026-08-07T05:19:42.592993+00:00` |
| **Scan Duration** | `13.86s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3398 malicious artifacts.

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
| Total Artifacts | 5623 |
| Analyzed Artifacts (Scanned) | 3644 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1979 |
| Total LOC | 538107 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.8% |
| Dominant Lang | SWIFT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.773 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4087 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9987 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2798 | 445566 | 76.8% |
| SWIFT | 511 | 68347 | 14.0% |
| MARKDOWN | 122 | 0 | 3.3% |
| KOTLIN | 78 | 13795 | 2.1% |
| JSON | 45 | 2243 | 1.2% |
| PLAINTEXT | 42 | 1 | 1.2% |
| XML | 18 | 0 | 0.5% |
| CSS | 10 | 5282 | 0.3% |
| YAML | 5 | 318 | 0.1% |
| JAVASCRIPT | 5 | 1178 | 0.1% |
| HTML | 4 | 618 | 0.1% |
| SHELL | 3 | 566 | 0.1% |
| DOCKERFILE | 1 | 39 | 0.0% |
| BATCH | 1 | 70 | 0.0% |
| RUBY | 1 | 84 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.712`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2426 | 66.6% |
| file_cluster_13 | 494 | 13.6% |
| file_cluster_4 | 381 | 10.5% |
| file_cluster_17 | 88 | 2.4% |
| file_cluster_2 | 47 | 1.3% |
| file_cluster_0 | 25 | 0.7% |
| file_cluster_16 | 15 | 0.4% |
| file_cluster_1 | 2 | 0.1% |
| Unknown | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 163 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1979*

**Composition by Extension & Reason:**
- `.ts`: 1837x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 56 exceeds 500 chars)
- `.prose`: 52x Excluded (Unsupported Extension: '.prose'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sandbox-browser'), 1x Excluded (Unsupported Extension: '.sandbox-common')
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.swift`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 3326 LOC), 1x Excluded (Machine-Generated Source Code Signature: 84 LOC)
- `.md`: 2x Excluded (Machine-Generated Source Code Signature: 256 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3121 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 4x Excluded (Explicitly Denied Extension: '.ttf')
- `.example`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.example')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 3x Excluded (Unsupported Extension: '.toml')
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jsonc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.resolved`: 2x Excluded (Unsupported Extension: '.resolved')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 32.7 | 25.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 23.1 | 16.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 27.6 | 2.5 | 80.0 |
| API Exposure | 0.0 | 19.6 | 6.1 | 6.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.6 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.9 | 30.5 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/memory/qmd-manager.ts` (Hits: 105)
- `setup-podman.sh` (Hits: 97)
- `src/config/schema.help.ts` (Hits: 85)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typebox.ts** (`src/agents/schema/typebox.ts`) — 53 inbound connections
2. **prompts.ts** (`src/wizard/prompts.ts`) — 18 inbound connections
3. **ws.ts** (`src/infra/ws.ts`) — 17 inbound connections
4. **GatewaySession.kt** (`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt`) — 14 inbound connections
5. **MainViewModel.kt** (`apps/android/app/src/main/java/ai/openclaw/android/MainViewModel.kt`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/plugin-sdk/index.ts`) — 146 outbound dependencies
2. **index.ts** (`src/plugins/runtime/index.ts`) — 85 outbound dependencies
3. **ChatMarkdown.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMarkdown.kt`) — 83 outbound dependencies
4. **types.ts** (`src/plugins/runtime/types.ts`) — 81 outbound dependencies
5. **OnboardingFlow.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `mergeConfig` (@ `src/agents/memory-search.ts`) -> Impact: **824.7** | LOC: 216
- `renderApp` (@ `ui/src/ui/app-render.ts`) -> Impact: **592.2** | LOC: 1004
- `formatCliCommand` (@ `src/security/audit-channel.ts`) -> Impact: **562.9** | LOC: 481
- `initPromise` (@ `src/browser/extension-relay.ts`) -> Impact: **527.4** | LOC: 709
- `processMessage` (@ `extensions/bluebubbles/src/monitor-processing.ts`) -> Impact: **517.7** | LOC: 674
- `createSignalEventHandler` (@ `src/signal/monitor/event-handler.ts`) -> Impact: **511.7** | LOC: 674
- `readSessionMessages` (@ `src/gateway/session-utils.fs.ts`) -> Impact: **476.3** | LOC: 581
- `processDiscordMessage` (@ `src/discord/monitor/message-handler.process.ts`) -> Impact: **475.9** | LOC: 719
- `vectorToBlob` (@ `src/memory/manager-embedding-ops.ts`) -> Impact: **465.6** | LOC: 770
- `createMatrixRoomMessageHandler` (@ `extensions/matrix/src/matrix/monitor/handler.ts`) -> Impact: **458.9** | LOC: 659

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `apps/macos/Sources/OpenClaw` | 194 | 32485.62 | 49.81% | 47.07% |
| `__monolith__` | 18 | 5998.76 | 20.7% | 2.63% |
| `apps/shared/OpenClawKit/Sources/OpenClawKit` | 52 | 5047.88 | 61.05% | 73.06% |
| `apps/macos/Tests/OpenClawIPCTests` | 97 | 3644.64 | 13.12% | 0.0% |
| `apps/android/app/src/main/java/ai/openclaw/android/ui` | 13 | 2796.46 | 59.83% | 26.07% |
| `apps/android/app/src/main/java/ai/openclaw/android/voice` | 6 | 2665.1 | 75.21% | 55.76% |
| `apps/android/app/src/main/java/ai/openclaw/android/node` | 21 | 2414.78 | 60.31% | 45.01% |
| `apps/shared/OpenClawKit/Sources/OpenClawChatUI` | 14 | 2392.9 | 58.84% | 22.95% |
| `src/agents` | 169 | 2338.49 | 29.22% | 25.23% |
| `apps/ios/Sources/Gateway` | 14 | 1996.98 | 46.92% | 51.52% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Swabble/Sources/swabble/Commands/HealthCommand.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/MicCommands.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/SetupCommand.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/StartStopCommands.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/StatusCommand.swift` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Swabble/Sources/SwabbleCore/Config/Config.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/SetupCommand.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/StartStopCommands.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/Commands/TestHookCommand.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Settings/SettingsTab.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/tui/tui.ts` -> **13** Orphaned Functions | **63** Duplicates
- `src/commands/doctor-config-flow.ts` -> **0** Orphaned Functions | **64** Duplicates
- `src/channels/dock.ts` -> **3** Orphaned Functions | **49** Duplicates
- `src/agents/subagent-registry.ts` -> **0** Orphaned Functions | **47** Duplicates
- `src/config/io.ts` -> **10** Orphaned Functions | **34** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/agents/pi-embedded-subscribe.handlers.messages.ts`** -> AI Confidence: **99.48%**
2. **`src/agents/pi-tools.ts`** -> AI Confidence: **99.48%**
3. **`src/agents/system-prompt.ts`** -> AI Confidence: **99.48%**
4. **`src/agents/tools/sessions-list-tool.ts`** -> AI Confidence: **99.48%**
5. **`src/auto-reply/reply/directive-handling.impl.ts`** -> AI Confidence: **99.48%**
6. **`src/cli/cron-cli/register.cron-edit.ts`** -> AI Confidence: **99.48%**
7. **`src/cli/daemon-cli/status.print.ts`** -> AI Confidence: **99.48%**
8. **`src/commands/channels/capabilities.ts`** -> AI Confidence: **99.48%**
9. **`src/config/sessions/metadata.ts`** -> AI Confidence: **99.48%**
10. **`src/cron/normalize.ts`** -> AI Confidence: **99.48%**
11. **`src/cron/service/store.ts`** -> AI Confidence: **99.48%**
12. **`src/gateway/server-runtime-config.ts`** -> AI Confidence: **99.48%**
13. **`src/gateway/ws-log.ts`** -> AI Confidence: **99.48%**
14. **`src/security/audit-channel.ts`** -> AI Confidence: **99.48%**
15. **`extensions/bluebubbles/src/media-send.ts`** -> AI Confidence: **99.39%**
16. **`extensions/bluebubbles/src/monitor-processing.ts`** -> AI Confidence: **99.39%**
17. **`extensions/feishu/src/bot.ts`** -> AI Confidence: **99.39%**
18. **`extensions/llm-task/src/llm-task-tool.ts`** -> AI Confidence: **99.39%**
19. **`extensions/matrix/src/matrix/client/config.ts`** -> AI Confidence: **99.39%**
20. **`extensions/matrix/src/matrix/monitor/handler.ts`** -> AI Confidence: **99.39%**
21. **`extensions/msteams/src/monitor-handler/message-handler.ts`** -> AI Confidence: **99.39%**
22. **`extensions/tlon/src/monitor/index.ts`** -> AI Confidence: **99.39%**
23. **`src/agents/bash-tools.exec-host-gateway.ts`** -> AI Confidence: **99.39%**
24. **`src/agents/bash-tools.exec-host-node.ts`** -> AI Confidence: **99.39%**
25. **`src/agents/bash-tools.exec.ts`** -> AI Confidence: **99.39%**
26. **`src/agents/cli-runner.ts`** -> AI Confidence: **99.39%**
27. **`src/agents/openclaw-tools.ts`** -> AI Confidence: **99.39%**
28. **`src/agents/pi-embedded-runner/run/payloads.ts`** -> AI Confidence: **99.39%**
29. **`src/agents/pi-embedded-subscribe.handlers.tools.ts`** -> AI Confidence: **99.39%**
30. **`src/agents/pi-tools.policy.ts`** -> AI Confidence: **99.39%**
31. **`src/agents/subagent-spawn.ts`** -> AI Confidence: **99.39%**
32. **`src/agents/tools/cron-tool.ts`** -> AI Confidence: **99.39%**
33. **`src/agents/tools/telegram-actions.ts`** -> AI Confidence: **99.39%**
34. **`src/auto-reply/reply/block-streaming.ts`** -> AI Confidence: **99.39%**
35. **`src/auto-reply/reply/commands-allowlist.ts`** -> AI Confidence: **99.39%**
36. **`src/auto-reply/reply/directive-handling.model.ts`** -> AI Confidence: **99.39%**
37. **`src/auto-reply/reply/directive-handling.persist.ts`** -> AI Confidence: **99.39%**
38. **`src/auto-reply/reply/get-reply-directives.ts`** -> AI Confidence: **99.39%**
39. **`src/auto-reply/reply/get-reply-run.ts`** -> AI Confidence: **99.39%**
40. **`src/auto-reply/reply/groups.ts`** -> AI Confidence: **99.39%**
41. **`src/auto-reply/reply/reply-delivery.ts`** -> AI Confidence: **99.39%**
42. **`src/auto-reply/reply/route-reply.ts`** -> AI Confidence: **99.39%**
43. **`src/auto-reply/reply/session.ts`** -> AI Confidence: **99.39%**
44. **`src/auto-reply/status.ts`** -> AI Confidence: **99.39%**
45. **`src/browser/config.ts`** -> AI Confidence: **99.39%**
46. **`src/cli/cron-cli/register.cron-add.ts`** -> AI Confidence: **99.39%**
47. **`src/cli/daemon-cli/status.gather.ts`** -> AI Confidence: **99.39%**
48. **`src/cli/gateway-cli/run.ts`** -> AI Confidence: **99.39%**
49. **`src/cli/nodes-cli/register.invoke.ts`** -> AI Confidence: **99.39%**
50. **`src/cli/qr-cli.ts`** -> AI Confidence: **99.39%**
51. **`src/cli/update-cli/status.ts`** -> AI Confidence: **99.39%**
52. **`src/commands/agent/delivery.ts`** -> AI Confidence: **99.39%**
53. **`src/commands/agent/session-store.ts`** -> AI Confidence: **99.39%**
54. **`src/commands/agent/session.ts`** -> AI Confidence: **99.39%**
55. **`src/commands/doctor-config-flow.ts`** -> AI Confidence: **99.39%**
56. **`src/commands/doctor-security.ts`** -> AI Confidence: **99.39%**
57. **`src/commands/gateway-status.ts`** -> AI Confidence: **99.39%**
58. **`src/commands/health.ts`** -> AI Confidence: **99.39%**
59. **`src/config/defaults.ts`** -> AI Confidence: **99.39%**
60. **`src/config/validation.ts`** -> AI Confidence: **99.39%**
61. **`src/cron/isolated-agent/run.ts`** -> AI Confidence: **99.39%**
62. **`src/discord/monitor/message-handler.preflight.ts`** -> AI Confidence: **99.39%**
63. **`src/gateway/client.ts`** -> AI Confidence: **99.39%**
64. **`src/gateway/server-methods/agent.ts`** -> AI Confidence: **99.39%**
65. **`src/gateway/server-methods/exec-approval.ts`** -> AI Confidence: **99.39%**
66. **`src/gateway/server-methods/system.ts`** -> AI Confidence: **99.39%**
67. **`src/gateway/server-node-events.ts`** -> AI Confidence: **99.39%**
68. **`src/gateway/sessions-patch.ts`** -> AI Confidence: **99.39%**
69. **`src/hooks/gmail-ops.ts`** -> AI Confidence: **99.39%**
70. **`src/imessage/monitor/inbound-processing.ts`** -> AI Confidence: **99.39%**
71. **`src/imessage/send.ts`** -> AI Confidence: **99.39%**
72. **`src/infra/exec-approvals.ts`** -> AI Confidence: **99.39%**
73. **`src/infra/outbound/message-action-params.ts`** -> AI Confidence: **99.39%**
74. **`src/infra/outbound/message-action-runner.ts`** -> AI Confidence: **99.39%**
75. **`src/infra/outbound/message.ts`** -> AI Confidence: **99.39%**
76. **`src/infra/session-cost-usage.ts`** -> AI Confidence: **99.39%**
77. **`src/media-understanding/apply.ts`** -> AI Confidence: **99.39%**
78. **`src/security/audit-extra.sync.ts`** -> AI Confidence: **99.39%**
79. **`src/security/audit.ts`** -> AI Confidence: **99.39%**
80. **`src/signal/monitor/event-handler.ts`** -> AI Confidence: **99.39%**
81. **`src/slack/monitor/events/interactions.ts`** -> AI Confidence: **99.39%**
82. **`src/slack/monitor/provider.ts`** -> AI Confidence: **99.39%**
83. **`src/telegram/bot.ts`** -> AI Confidence: **99.39%**
84. **`src/tui/tui-session-actions.ts`** -> AI Confidence: **99.39%**
85. **`src/web/accounts.ts`** -> AI Confidence: **99.39%**
86. **`extensions/diagnostics-otel/src/service.ts`** -> AI Confidence: **99.35%**
87. **`src/commands/agent.ts`** -> AI Confidence: **99.35%**
88. **`src/commands/agents.commands.identity.ts`** -> AI Confidence: **99.35%**
89. **`src/commands/channels/status.ts`** -> AI Confidence: **99.35%**
90. **`src/commands/models/scan.ts`** -> AI Confidence: **99.35%**
91. **`src/infra/outbound/targets.ts`** -> AI Confidence: **99.35%**
92. **`src/secrets/audit.ts`** -> AI Confidence: **99.35%**
93. **`src/slack/send.ts`** -> AI Confidence: **99.35%**
94. **`src/tts/tts.ts`** -> AI Confidence: **99.35%**
95. **`extensions/twitch/src/status.ts`** -> AI Confidence: **99.34%**
96. **`src/agents/memory-search.ts`** -> AI Confidence: **99.34%**
97. **`src/agents/sandbox/config.ts`** -> AI Confidence: **99.34%**
98. **`src/auto-reply/reply/queue/settings.ts`** -> AI Confidence: **99.34%**
99. **`src/commands/sandbox-explain.ts`** -> AI Confidence: **99.34%**
100. **`src/infra/skills-remote.ts`** -> AI Confidence: **99.34%**
101. **`src/plugins/update.ts`** -> AI Confidence: **99.34%**
102. **`src/tts/tts-core.ts`** -> AI Confidence: **99.34%**
103. **`apps/macos/Tests/OpenClawIPCTests/GatewayFrameDecodeTests.swift`** -> AI Confidence: **99.32%**
104. **`src/browser/chrome.profile-decoration.ts`** -> AI Confidence: **99.32%**
105. **`src/commands/agent/run-context.ts`** -> AI Confidence: **99.32%**
106. **`src/config/types.tools.ts`** -> AI Confidence: **99.32%**
107. **`src/discord/monitor/sender-identity.ts`** -> AI Confidence: **99.32%**
108. **`src/infra/heartbeat-visibility.ts`** -> AI Confidence: **99.32%**
109. **`src/telegram/probe.ts`** -> AI Confidence: **99.32%**
110. **`src/web/auto-reply/session-snapshot.ts`** -> AI Confidence: **99.32%**
111. **`apps/ios/Sources/Gateway/GatewayConnectionController.swift`** -> AI Confidence: **99.31%**
112. **`apps/ios/Sources/Model/NodeAppModel.swift`** -> AI Confidence: **99.31%**
113. **`apps/ios/Sources/OpenClawApp.swift`** -> AI Confidence: **99.31%**
114. **`apps/macos/Sources/OpenClaw/NodePairingApprovalPrompter.swift`** -> AI Confidence: **99.31%**
115. **`apps/macos/Sources/OpenClaw/VoiceWakeSettings.swift`** -> AI Confidence: **99.31%**
116. **`apps/macos/Sources/OpenClaw/WebChatSwiftUI.swift`** -> AI Confidence: **99.31%**
117. **`apps/shared/OpenClawKit/Sources/OpenClawChatUI/ChatViewModel.swift`** -> AI Confidence: **99.31%**
118. **`apps/android/app/src/main/java/ai/openclaw/android/chat/ChatController.kt`** -> AI Confidence: **99.31%**
119. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewayDiscovery.kt`** -> AI Confidence: **99.31%**
120. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt`** -> AI Confidence: **99.31%**
121. **`apps/android/app/src/main/java/ai/openclaw/android/node/AppUpdateHandler.kt`** -> AI Confidence: **99.31%**
122. **`apps/android/app/src/main/java/ai/openclaw/android/node/CameraCaptureManager.kt`** -> AI Confidence: **99.31%**
123. **`apps/android/app/src/main/java/ai/openclaw/android/node/CameraHandler.kt`** -> AI Confidence: **99.31%**
124. **`apps/android/app/src/main/java/ai/openclaw/android/node/CanvasController.kt`** -> AI Confidence: **99.31%**
125. **`apps/android/app/src/main/java/ai/openclaw/android/node/GatewayEventHandler.kt`** -> AI Confidence: **99.31%**
126. **`apps/android/app/src/main/java/ai/openclaw/android/node/InvokeDispatcher.kt`** -> AI Confidence: **99.31%**
127. **`apps/android/app/src/main/java/ai/openclaw/android/node/LocationCaptureManager.kt`** -> AI Confidence: **99.31%**
128. **`apps/android/app/src/main/java/ai/openclaw/android/node/LocationHandler.kt`** -> AI Confidence: **99.31%**
129. **`apps/android/app/src/main/java/ai/openclaw/android/node/ScreenRecordManager.kt`** -> AI Confidence: **99.31%**
130. **`apps/android/app/src/main/java/ai/openclaw/android/tools/ToolDisplay.kt`** -> AI Confidence: **99.31%**
131. **`apps/android/app/src/main/java/ai/openclaw/android/ui/GatewayConfigResolver.kt`** -> AI Confidence: **99.31%**
132. **`apps/android/app/src/main/java/ai/openclaw/android/voice/MicCaptureManager.kt`** -> AI Confidence: **99.31%**
133. **`apps/android/app/src/main/java/ai/openclaw/android/voice/TalkModeManager.kt`** -> AI Confidence: **99.31%**
134. **`extensions/acpx/src/runtime.ts`** -> AI Confidence: **99.31%**
135. **`extensions/bluebubbles/src/actions.ts`** -> AI Confidence: **99.31%**
136. **`extensions/bluebubbles/src/attachments.ts`** -> AI Confidence: **99.31%**
137. **`extensions/bluebubbles/src/channel.ts`** -> AI Confidence: **99.31%**
138. **`extensions/bluebubbles/src/chat.ts`** -> AI Confidence: **99.31%**
139. **`extensions/bluebubbles/src/monitor.ts`** -> AI Confidence: **99.31%**
140. **`extensions/bluebubbles/src/send.ts`** -> AI Confidence: **99.31%**
141. **`extensions/feishu/src/docx.ts`** -> AI Confidence: **99.31%**
142. **`extensions/feishu/src/media.ts`** -> AI Confidence: **99.31%**
143. **`extensions/feishu/src/monitor.ts`** -> AI Confidence: **99.31%**
144. **`extensions/feishu/src/reply-dispatcher.ts`** -> AI Confidence: **99.31%**
145. **`extensions/feishu/src/send.ts`** -> AI Confidence: **99.31%**
146. **`extensions/googlechat/src/channel.ts`** -> AI Confidence: **99.31%**
147. **`extensions/googlechat/src/monitor.ts`** -> AI Confidence: **99.31%**
148. **`extensions/irc/src/channel.ts`** -> AI Confidence: **99.31%**
149. **`extensions/irc/src/inbound.ts`** -> AI Confidence: **99.31%**
150. **`extensions/irc/src/send.ts`** -> AI Confidence: **99.31%**
151. **`extensions/matrix/src/channel.ts`** -> AI Confidence: **99.31%**
152. **`extensions/matrix/src/matrix/client/shared.ts`** -> AI Confidence: **99.31%**
153. **`extensions/matrix/src/matrix/monitor/index.ts`** -> AI Confidence: **99.31%**
154. **`extensions/matrix/src/matrix/send.ts`** -> AI Confidence: **99.31%**
155. **`extensions/matrix/src/matrix/send/client.ts`** -> AI Confidence: **99.31%**
156. **`extensions/mattermost/src/channel.ts`** -> AI Confidence: **99.31%**
157. **`extensions/mattermost/src/mattermost/monitor.ts`** -> AI Confidence: **99.31%**
158. **`extensions/msteams/src/channel.ts`** -> AI Confidence: **99.31%**
159. **`extensions/msteams/src/messenger.ts`** -> AI Confidence: **99.31%**
160. **`extensions/msteams/src/monitor.ts`** -> AI Confidence: **99.31%**
161. **`extensions/msteams/src/send.ts`** -> AI Confidence: **99.31%**
162. **`extensions/nextcloud-talk/src/channel.ts`** -> AI Confidence: **99.31%**
163. **`extensions/nextcloud-talk/src/inbound.ts`** -> AI Confidence: **99.31%**
164. **`extensions/nextcloud-talk/src/monitor.ts`** -> AI Confidence: **99.31%**
165. **`extensions/nostr/src/nostr-profile-http.ts`** -> AI Confidence: **99.31%**
166. **`extensions/synology-chat/src/channel.ts`** -> AI Confidence: **99.31%**
167. **`extensions/tlon/src/channel.ts`** -> AI Confidence: **99.31%**
168. **`extensions/twitch/src/plugin.ts`** -> AI Confidence: **99.31%**
169. **`extensions/voice-call/src/cli.ts`** -> AI Confidence: **99.31%**
170. **`extensions/voice-call/src/manager/events.ts`** -> AI Confidence: **99.31%**
171. **`extensions/voice-call/src/manager/outbound.ts`** -> AI Confidence: **99.31%**
172. **`extensions/voice-call/src/providers/plivo.ts`** -> AI Confidence: **99.31%**
173. **`extensions/voice-call/src/providers/twilio.ts`** -> AI Confidence: **99.31%**
174. **`extensions/voice-call/src/runtime.ts`** -> AI Confidence: **99.31%**
175. **`extensions/voice-call/src/webhook.ts`** -> AI Confidence: **99.31%**
176. **`extensions/zalo/src/channel.ts`** -> AI Confidence: **99.31%**
177. **`extensions/zalo/src/monitor.ts`** -> AI Confidence: **99.31%**
178. **`extensions/zalouser/src/channel.ts`** -> AI Confidence: **99.31%**
179. **`src/acp/client.ts`** -> AI Confidence: **99.31%**
180. **`src/acp/control-plane/manager.core.ts`** -> AI Confidence: **99.31%**
181. **`src/acp/control-plane/manager.identity-reconcile.ts`** -> AI Confidence: **99.31%**
182. **`src/acp/runtime/session-meta.ts`** -> AI Confidence: **99.31%**
183. **`src/acp/translator.ts`** -> AI Confidence: **99.31%**
184. **`src/agents/acp-spawn.ts`** -> AI Confidence: **99.31%**
185. **`src/agents/agent-scope.ts`** -> AI Confidence: **99.31%**
186. **`src/agents/anthropic-payload-log.ts`** -> AI Confidence: **99.31%**
187. **`src/agents/apply-patch.ts`** -> AI Confidence: **99.31%**
188. **`src/agents/auth-profiles/oauth.ts`** -> AI Confidence: **99.31%**
189. **`src/agents/auth-profiles/store.ts`** -> AI Confidence: **99.31%**
190. **`src/agents/bash-tools.exec-runtime.ts`** -> AI Confidence: **99.31%**
191. **`src/agents/bash-tools.process.ts`** -> AI Confidence: **99.31%**
192. **`src/agents/cache-trace.ts`** -> AI Confidence: **99.31%**
193. **`src/agents/cli-credentials.ts`** -> AI Confidence: **99.31%**
194. **`src/agents/cli-runner/helpers.ts`** -> AI Confidence: **99.31%**
195. **`src/agents/model-auth.ts`** -> AI Confidence: **99.31%**
196. **`src/agents/model-fallback.ts`** -> AI Confidence: **99.31%**
197. **`src/agents/model-selection.ts`** -> AI Confidence: **99.31%**
198. **`src/agents/models-config.providers.ts`** -> AI Confidence: **99.31%**
199. **`src/agents/pi-embedded-helpers/bootstrap.ts`** -> AI Confidence: **99.31%**
200. **`src/agents/pi-embedded-runner/compact.ts`** -> AI Confidence: **99.31%**
201. **`src/agents/pi-embedded-runner/extensions.ts`** -> AI Confidence: **99.31%**
202. **`src/agents/pi-embedded-runner/google.ts`** -> AI Confidence: **99.31%**
203. **`src/agents/pi-embedded-runner/model.ts`** -> AI Confidence: **99.31%**
204. **`src/agents/pi-embedded-runner/run/attempt.ts`** -> AI Confidence: **99.31%**
205. **`src/agents/pi-embedded-runner/run/images.ts`** -> AI Confidence: **99.31%**
206. **`src/agents/pi-embedded-runner/run/params.ts`** -> AI Confidence: **99.31%**
207. **`src/agents/pi-embedded-runner/system-prompt.ts`** -> AI Confidence: **99.31%**
208. **`src/agents/pi-embedded-subscribe.tools.ts`** -> AI Confidence: **99.31%**
209. **`src/agents/pi-extensions/compaction-safeguard.ts`** -> AI Confidence: **99.31%**
210. **`src/agents/pi-tool-definition-adapter.ts`** -> AI Confidence: **99.31%**
211. **`src/agents/pi-tools.before-tool-call.ts`** -> AI Confidence: **99.31%**
212. **`src/agents/pi-tools.read.ts`** -> AI Confidence: **99.31%**
213. **`src/agents/sandbox/browser.ts`** -> AI Confidence: **99.31%**
214. **`src/agents/sandbox/context.ts`** -> AI Confidence: **99.31%**
215. **`src/agents/sandbox/docker.ts`** -> AI Confidence: **99.31%**
216. **`src/agents/sandbox/fs-bridge.ts`** -> AI Confidence: **99.31%**
217. **`src/agents/sandbox/runtime-status.ts`** -> AI Confidence: **99.31%**
218. **`src/agents/session-tool-result-guard.ts`** -> AI Confidence: **99.31%**
219. **`src/agents/skills-install-download.ts`** -> AI Confidence: **99.31%**
220. **`src/agents/skills-install.ts`** -> AI Confidence: **99.31%**
221. **`src/agents/skills-status.ts`** -> AI Confidence: **99.31%**
222. **`src/agents/skills/env-overrides.ts`** -> AI Confidence: **99.31%**
223. **`src/agents/skills/refresh.ts`** -> AI Confidence: **99.31%**
224. **`src/agents/skills/workspace.ts`** -> AI Confidence: **99.31%**
225. **`src/agents/subagent-announce.ts`** -> AI Confidence: **99.31%**
226. **`src/agents/subagent-registry.ts`** -> AI Confidence: **99.31%**
227. **`src/agents/tools/browser-tool.ts`** -> AI Confidence: **99.31%**
228. **`src/agents/tools/canvas-tool.ts`** -> AI Confidence: **99.31%**
229. **`src/agents/tools/discord-actions-messaging.ts`** -> AI Confidence: **99.31%**
230. **`src/agents/tools/gateway-tool.ts`** -> AI Confidence: **99.31%**
231. **`src/agents/tools/image-tool.ts`** -> AI Confidence: **99.31%**
232. **`src/agents/tools/memory-tool.ts`** -> AI Confidence: **99.31%**
233. **`src/agents/tools/message-tool.ts`** -> AI Confidence: **99.31%**
234. **`src/agents/tools/nodes-tool.ts`** -> AI Confidence: **99.31%**
235. **`src/agents/tools/session-status-tool.ts`** -> AI Confidence: **99.31%**
236. **`src/agents/tools/sessions-history-tool.ts`** -> AI Confidence: **99.31%**
237. **`src/agents/tools/sessions-send-tool.a2a.ts`** -> AI Confidence: **99.31%**
238. **`src/agents/tools/sessions-send-tool.ts`** -> AI Confidence: **99.31%**
239. **`src/agents/tools/slack-actions.ts`** -> AI Confidence: **99.31%**
240. **`src/agents/tools/subagents-tool.ts`** -> AI Confidence: **99.31%**
241. **`src/agents/tools/web-fetch.ts`** -> AI Confidence: **99.31%**
242. **`src/agents/tools/web-search.ts`** -> AI Confidence: **99.31%**
243. **`src/agents/workspace-run.ts`** -> AI Confidence: **99.31%**
244. **`src/auto-reply/chunk.ts`** -> AI Confidence: **99.31%**
245. **`src/auto-reply/commands-registry.ts`** -> AI Confidence: **99.31%**
246. **`src/auto-reply/reply.triggers.trigger-handling.filters-usage-summary-current-model-provider.cases.ts`** -> AI Confidence: **99.31%**
247. **`src/auto-reply/reply/abort.ts`** -> AI Confidence: **99.31%**
248. **`src/auto-reply/reply/agent-runner-execution.ts`** -> AI Confidence: **99.31%**
249. **`src/auto-reply/reply/agent-runner-memory.ts`** -> AI Confidence: **99.31%**
250. **`src/auto-reply/reply/agent-runner-payloads.ts`** -> AI Confidence: **99.31%**
251. **`src/auto-reply/reply/agent-runner-utils.ts`** -> AI Confidence: **99.31%**
252. **`src/auto-reply/reply/agent-runner.ts`** -> AI Confidence: **99.31%**
253. **`src/auto-reply/reply/bash-command.ts`** -> AI Confidence: **99.31%**
254. **`src/auto-reply/reply/commands-acp/diagnostics.ts`** -> AI Confidence: **99.31%**
255. **`src/auto-reply/reply/commands-acp/lifecycle.ts`** -> AI Confidence: **99.31%**
256. **`src/auto-reply/reply/commands-acp/shared.ts`** -> AI Confidence: **99.31%**
257. **`src/auto-reply/reply/commands-compact.ts`** -> AI Confidence: **99.31%**
258. **`src/auto-reply/reply/commands-config.ts`** -> AI Confidence: **99.31%**
259. **`src/auto-reply/reply/commands-core.ts`** -> AI Confidence: **99.31%**
260. **`src/auto-reply/reply/commands-models.ts`** -> AI Confidence: **99.31%**
261. **`src/auto-reply/reply/commands-session-abort.ts`** -> AI Confidence: **99.31%**
262. **`src/auto-reply/reply/commands-session.ts`** -> AI Confidence: **99.31%**
263. **`src/auto-reply/reply/commands-status.ts`** -> AI Confidence: **99.31%**
264. **`src/auto-reply/reply/commands-subagents/action-send.ts`** -> AI Confidence: **99.31%**
265. **`src/auto-reply/reply/commands-subagents/shared.ts`** -> AI Confidence: **99.31%**
266. **`src/auto-reply/reply/commands-system-prompt.ts`** -> AI Confidence: **99.31%**
267. **`src/auto-reply/reply/directive-handling.auth.ts`** -> AI Confidence: **99.31%**
268. **`src/auto-reply/reply/directive-handling.parse.ts`** -> AI Confidence: **99.31%**
269. **`src/auto-reply/reply/dispatch-acp.ts`** -> AI Confidence: **99.31%**
270. **`src/auto-reply/reply/dispatch-from-config.ts`** -> AI Confidence: **99.31%**
271. **`src/auto-reply/reply/get-reply-directives-apply.ts`** -> AI Confidence: **99.31%**
272. **`src/auto-reply/reply/get-reply-inline-actions.ts`** -> AI Confidence: **99.31%**
273. **`src/auto-reply/reply/get-reply.ts`** -> AI Confidence: **99.31%**
274. **`src/auto-reply/reply/memory-flush.ts`** -> AI Confidence: **99.31%**
275. **`src/auto-reply/reply/model-selection.ts`** -> AI Confidence: **99.31%**
276. **`src/auto-reply/reply/reply-elevated.ts`** -> AI Confidence: **99.31%**
277. **`src/auto-reply/reply/reply-payloads.ts`** -> AI Confidence: **99.31%**
278. **`src/auto-reply/reply/session-reset-model.ts`** -> AI Confidence: **99.31%**
279. **`src/auto-reply/reply/session-updates.ts`** -> AI Confidence: **99.31%**
280. **`src/auto-reply/reply/stage-sandbox-media.ts`** -> AI Confidence: **99.31%**
281. **`src/browser/bridge-server.ts`** -> AI Confidence: **99.31%**
282. **`src/browser/chrome.ts`** -> AI Confidence: **99.31%**
283. **`src/browser/client-fetch.ts`** -> AI Confidence: **99.31%**
284. **`src/browser/extension-relay.ts`** -> AI Confidence: **99.31%**
285. **`src/browser/profiles-service.ts`** -> AI Confidence: **99.31%**
286. **`src/browser/pw-session.ts`** -> AI Confidence: **99.31%**
287. **`src/browser/routes/agent.act.ts`** -> AI Confidence: **99.31%**
288. **`src/browser/routes/agent.snapshot.ts`** -> AI Confidence: **99.31%**
289. **`src/channels/dock.ts`** -> AI Confidence: **99.31%**
290. **`src/channels/plugins/actions/telegram.ts`** -> AI Confidence: **99.31%**
291. **`src/channels/plugins/catalog.ts`** -> AI Confidence: **99.31%**
292. **`src/channels/plugins/directory-config.ts`** -> AI Confidence: **99.31%**
293. **`src/channels/plugins/group-mentions.ts`** -> AI Confidence: **99.31%**
294. **`src/channels/plugins/onboarding/discord.ts`** -> AI Confidence: **99.31%**
295. **`src/channels/plugins/onboarding/helpers.ts`** -> AI Confidence: **99.31%**
296. **`src/channels/plugins/onboarding/signal.ts`** -> AI Confidence: **99.31%**
297. **`src/channels/plugins/onboarding/slack.ts`** -> AI Confidence: **99.31%**
298. **`src/channels/plugins/onboarding/whatsapp.ts`** -> AI Confidence: **99.31%**
299. **`src/channels/plugins/types.adapters.ts`** -> AI Confidence: **99.31%**
300. **`src/channels/plugins/types.core.ts`** -> AI Confidence: **99.31%**
301. **`src/cli/acp-cli.ts`** -> AI Confidence: **99.31%**
302. **`src/cli/browser-cli-actions-input/register.files-downloads.ts`** -> AI Confidence: **99.31%**
303. **`src/cli/browser-cli-inspect.ts`** -> AI Confidence: **99.31%**
304. **`src/cli/browser-cli-manage.ts`** -> AI Confidence: **99.31%**
305. **`src/cli/browser-cli-state.ts`** -> AI Confidence: **99.31%**
306. **`src/cli/completion-cli.ts`** -> AI Confidence: **99.31%**
307. **`src/cli/config-cli.ts`** -> AI Confidence: **99.31%**
308. **`src/cli/cron-cli/shared.ts`** -> AI Confidence: **99.31%**
309. **`src/cli/daemon-cli/install.ts`** -> AI Confidence: **99.31%**
310. **`src/cli/daemon-cli/lifecycle-core.ts`** -> AI Confidence: **99.31%**
311. **`src/cli/daemon-cli/shared.ts`** -> AI Confidence: **99.31%**
312. **`src/cli/devices-cli.ts`** -> AI Confidence: **99.31%**
313. **`src/cli/directory-cli.ts`** -> AI Confidence: **99.31%**
314. **`src/cli/dns-cli.ts`** -> AI Confidence: **99.31%**
315. **`src/cli/exec-approvals-cli.ts`** -> AI Confidence: **99.31%**
316. **`src/cli/hooks-cli.ts`** -> AI Confidence: **99.31%**
317. **`src/cli/logs-cli.ts`** -> AI Confidence: **99.31%**
318. **`src/cli/memory-cli.ts`** -> AI Confidence: **99.31%**
319. **`src/cli/node-cli/daemon.ts`** -> AI Confidence: **99.31%**
320. **`src/cli/nodes-cli/register.camera.ts`** -> AI Confidence: **99.31%**
321. **`src/cli/nodes-cli/register.canvas.ts`** -> AI Confidence: **99.31%**
322. **`src/cli/nodes-cli/register.screen.ts`** -> AI Confidence: **99.31%**
323. **`src/cli/nodes-cli/register.status.ts`** -> AI Confidence: **99.31%**
324. **`src/cli/nodes-cli/rpc.ts`** -> AI Confidence: **99.31%**
325. **`src/cli/pairing-cli.ts`** -> AI Confidence: **99.31%**
326. **`src/cli/plugins-cli.ts`** -> AI Confidence: **99.31%**
327. **`src/cli/program/config-guard.ts`** -> AI Confidence: **99.31%**
328. **`src/cli/secrets-cli.ts`** -> AI Confidence: **99.31%**
329. **`src/cli/security-cli.ts`** -> AI Confidence: **99.31%**
330. **`src/cli/update-cli/update-command.ts`** -> AI Confidence: **99.31%**
331. **`src/cli/update-cli/wizard.ts`** -> AI Confidence: **99.31%**
332. **`src/commands/agent-via-gateway.ts`** -> AI Confidence: **99.31%**
333. **`src/commands/agents.bindings.ts`** -> AI Confidence: **99.31%**
334. **`src/commands/agents.commands.add.ts`** -> AI Confidence: **99.31%**
335. **`src/commands/agents.commands.bind.ts`** -> AI Confidence: **99.31%**
336. **`src/commands/agents.commands.list.ts`** -> AI Confidence: **99.31%**
337. **`src/commands/auth-choice.apply-helpers.ts`** -> AI Confidence: **99.31%**
338. **`src/commands/auth-choice.apply.anthropic.ts`** -> AI Confidence: **99.31%**
339. **`src/commands/auth-choice.apply.api-providers.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4525` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `apps/shared/OpenClawKit/Sources/OpenClawKit/CanvasCommandParams.swift` (SWIFT) -> Cumulative Risk: **825.7**
- **Archetype:** `file_cluster_4` (Distance: 13.126 IQR)
- **Magnitude:** 140.66 | **LOC:** 77 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `init` (Impact: 16.6), `init` (Impact: 11.5), `init` (Impact: 8.2)

### 2. `apps/shared/OpenClawKit/Sources/OpenClawKit/CalendarCommands.swift` (SWIFT) -> Cumulative Risk: **760.0**
- **Archetype:** `file_cluster_4` (Distance: 12.797 IQR)
- **Magnitude:** 157.84 | **LOC:** 94 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 18.9), `init` (Impact: 9.3), `init` (Impact: 8.2)

### 3. `apps/shared/OpenClawKit/Sources/OpenClawKit/LocationCommands.swift` (SWIFT) -> Cumulative Risk: **758.35**
- **Archetype:** `file_cluster_4` (Distance: 13.216 IQR)
- **Magnitude:** 99.12 | **LOC:** 58 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 16.9), `init` (Impact: 8.2)

### 4. `apps/shared/OpenClawKit/Sources/OpenClawKit/WatchCommands.swift` (SWIFT) -> Cumulative Risk: **755.79**
- **Archetype:** `file_cluster_4` (Distance: 12.491 IQR)
- **Magnitude:** 151.2 | **LOC:** 96 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 31.0), `init` (Impact: 4.2), `init` (Impact: 3.1)

### 5. `apps/shared/OpenClawKit/Sources/OpenClawKit/SystemCommands.swift` (SWIFT) -> Cumulative Risk: **755.7**
- **Archetype:** `file_cluster_4` (Distance: 12.639 IQR)
- **Magnitude:** 145.18 | **LOC:** 89 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 34.3), `init` (Impact: 10.4), `init` (Impact: 1.9)

### 6. `apps/shared/OpenClawKit/Sources/OpenClawKit/PhotosCommands.swift` (SWIFT) -> Cumulative Risk: **754.48**
- **Archetype:** `file_cluster_4` (Distance: 13.478 IQR)
- **Magnitude:** 80.98 | **LOC:** 42 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `init` (Impact: 8.2), `init` (Impact: 5.2), `init` (Impact: 1.9)

### 7. `apps/shared/OpenClawKit/Sources/OpenClawKit/MotionCommands.swift` (SWIFT) -> Cumulative Risk: **753.48**
- **Archetype:** `file_cluster_4` (Distance: 12.457 IQR)
- **Magnitude:** 141.38 | **LOC:** 96 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 14.0), `init` (Impact: 8.2), `init` (Impact: 5.4)

### 8. `apps/shared/OpenClawKit/Sources/OpenClawKit/RemindersCommands.swift` (SWIFT) -> Cumulative Risk: **750.61**
- **Archetype:** `file_cluster_4` (Distance: 12.811 IQR)
- **Magnitude:** 127.5 | **LOC:** 83 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `init` (Impact: 12.9), `init` (Impact: 8.0), `init` (Impact: 5.4)

### 9. `apps/shared/OpenClawKit/Sources/OpenClawKit/CameraCommands.swift` (SWIFT) -> Cumulative Risk: **749.24**
- **Archetype:** `file_cluster_4` (Distance: 12.82 IQR)
- **Magnitude:** 108.8 | **LOC:** 69 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `init` (Impact: 19.3), `init` (Impact: 15.3)

### 10. `extensions/voice-call/src/manager/timers.ts` (TYPESCRIPT) -> Cumulative Risk: **749.17**
- **Archetype:** `file_cluster_4` (Distance: 11.379 IQR)
- **Magnitude:** 12.16 | **LOC:** 113 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (92.4142%), Cognitive Load (90.025%)
- **Heaviest Functions:** `resolveTranscriptWaiter` (Impact: 13.1), `waitForFinalTranscript` (Impact: 12.1), `onTimeout` (Impact: 9.2)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Model/NodeAppModel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.608 IQR)
- **Top Global Matches:** file_cluster_4: 12.608, file_cluster_8: 12.79, file_cluster_0: 12.965
- **Magnitude:** 1821.32 | **LOC:** 2731 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6576%), Tech Debt (60.2201%)
**Top Internal Functions/Classes:**
  * `handleCanvasInvoke` (Impact: 201.5)
  * `handleLocationInvoke` (Impact: 47.6)
  * `startVoiceWakeSync` (Impact: 46.6)
    * *Intent:* // If talk is enabled, voice wake should not grab the mic.
  * `refreshShareRouteFromGateway` (Impact: 46.2)
  * `refreshBrandingFromGateway` (Impact: 42.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 428`, `args: 101`, `func_start: 87`, `class_start: 22`
* *Risk/State:* `state_mutation: 265`, `orphaned_logic: 42`
* *Architecture:* `io: 8`, `api: 53`, `concurrency: 225`, `import: 9`
* *Defense:* `safety: 126`, `doc: 2`, `sync_locks: 22`, `immutability_locks: 241`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, os, SwiftUI, OpenClawChatUI, UserNotifications, Security, UIKit, OpenClawKit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/voice/TalkModeManager.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.472 IQR)
- **Top Global Matches:** file_cluster_4: 13.472, file_cluster_13: 13.636, file_cluster_8: 13.648
- **Magnitude:** 1589.18 | **LOC:** 1318 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (32.5996%)
**Top Internal Functions/Classes:**
  * `playAssistant` (Impact: 64.7)
  * `streamPcm` (Impact: 51.3)
  * `ensureSystemTts` (Impact: 44.6)
  * `reloadConfig` (Impact: 44.6)
  * `fetchLatestAssistantText` (Impact: 39.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 254`, `args: 72`, `func_start: 65`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 366`, `duplicate_logic: 3`, `orphaned_logic: 13`
* *Architecture:* `api: 2`, `concurrency: 185`, `import: 42`
* *Defense:* `safety: 76`, `immutability_locks: 200`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` android.media.AudioAttributes, kotlinx.coroutines.flow.StateFlow, androidx.core.content.ContextCompat, android.os.Looper, android.media.MediaPlayer, kotlinx.coroutines.Dispatchers, kotlinx.serialization.json.JsonArray, kotlinx.serialization.json.JsonElement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/TalkModeRuntime.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.981 IQR)
- **Top Global Matches:** file_cluster_4: 11.981, file_cluster_8: 12.127, file_cluster_0: 12.43
- **Magnitude:** 1332.78 | **LOC:** 1052 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1267%), Tech Debt (9.23%)
**Top Internal Functions/Classes:**
  * `fetchTalkConfig` (Impact: 145.7)
  * `preparePlaybackInput` (Impact: 75.9)
  * `playElevenLabs` (Impact: 67.2)
  * `startRecognition` (Impact: 48.1)
  * `latestAssistantText` (Impact: 41.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 288`, `args: 58`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `state_mutation: 103`, `orphaned_logic: 2`
* *Architecture:* `api: 39`, `concurrency: 157`, `import: 6`
* *Defense:* `safety: 92`, `sync_locks: 27`, `immutability_locks: 200`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVFoundation, Foundation, OpenClawChatUI, Speech, OpenClawKit, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/NodeMode/MacNodeRuntime.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.748 IQR)
- **Top Global Matches:** file_cluster_8: 11.748, file_cluster_4: 11.755, file_cluster_17: 12.107
- **Magnitude:** 1173.06 | **LOC:** 1003 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.3351%), Tech Debt (11.1693%)
**Top Internal Functions/Classes:**
  * `handleCanvasInvoke` (Impact: 113.2)
  * `handleCameraInvoke` (Impact: 101.5)
  * `handleSystemExecApprovalsSet` (Impact: 65.3)
  * `handleInvoke` (Impact: 60.5)
  * `handleLocationInvoke` (Impact: 57.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 358`, `structural_boundaries: 252`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `state_mutation: 139`, `orphaned_logic: 4`
* *Architecture:* `io: 11`, `concurrency: 122`, `import: 4`
* *Defense:* `safety: 68`, `sync_locks: 6`, `immutability_locks: 155`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, OpenClawIPC, AppKit, OpenClawKit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/MenuSessionsInjector.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.468 IQR)
- **Top Global Matches:** file_cluster_8: 11.468, file_cluster_4: 11.707, file_cluster_17: 11.852
- **Magnitude:** 1047.42 | **LOC:** 1241 | **CtrlFlow:** 58.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.6335%), Tech Debt (13.5938%)
**Top Internal Functions/Classes:**
  * `inject` (Impact: 81.4)
  * `injectNodes` (Impact: 48.4)
  * `gatewayEntry` (Impact: 35.6)
  * `menuWillOpen` (Impact: 35.2)
  * `menuWindowWidth` (Impact: 27.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 248`, `args: 69`, `func_start: 57`, `class_start: 7`
* *Risk/State:* `state_mutation: 97`, `orphaned_logic: 7`
* *Architecture:* `api: 8`, `concurrency: 85`, `import: 4`
* *Defense:* `safety: 95`, `sync_locks: 12`, `immutability_locks: 178`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, Foundation, AppKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/auto-reply/reply/export-html/template.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.496 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.369 IQR)
- **Top Global Matches:** file_cluster_8: 12.496, file_cluster_17: 12.546, file_cluster_4: 12.894
- **Magnitude:** 1022.92 | **LOC:** 1853 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5566%), Tech Debt (20.8686%)
**Top Internal Functions/Classes:**
  * `renderToolCall` (Impact: 145.4)
  * `renderEntry` (Impact: 71.7)
  * `filterNodes` (Impact: 46.8)
  * `computeStats` (Impact: 44.7)
  * `getTreeNodeDisplayHtml` (Impact: 43.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 242`, `args: 57`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 228`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 15`, `concurrency: 14`
* *Defense:* `safety: 120`, `doc: 15`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Gateway/GatewayConnectionController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.106 IQR)
- **Top Global Matches:** file_cluster_8: 12.106, file_cluster_4: 12.184, file_cluster_17: 12.243
- **Magnitude:** 1010.7 | **LOC:** 1056 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.4056%), Tech Debt (92.216%)
**Top Internal Functions/Classes:**
  * `maybeAutoConnect` (Impact: 93.9)
  * `resolveBonjourServiceToHostPort` (Impact: 70.2)
  * `connectDiscoveredGateway` (Impact: 54.5)
  * `connectManual` (Impact: 34.3)
  * `extractHostPort` (Impact: 30.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 227`, `args: 84`, `func_start: 68`, `class_start: 5`
* *Risk/State:* `state_mutation: 142`, `duplicate_logic: 7`, `orphaned_logic: 27`
* *Architecture:* `io: 19`, `concurrency: 61`, `import: 17`
* *Defense:* `safety: 58`, `doc: 3`, `sync_locks: 7`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVFoundation, Foundation, Observation, SwiftUI, Photos, EventKit, Speech, CoreMotion...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ExecApprovals.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.179 IQR)
- **Top Global Matches:** file_cluster_8: 13.179, file_cluster_4: 13.243, file_cluster_17: 13.284
- **Magnitude:** 990.42 | **LOC:** 795 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.2337%), Tech Debt (63.9369%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 89.6)
  * `normalizeIncoming` (Impact: 53.0)
  * `mergeAgents` (Impact: 32.6)
  * `ensureFile` (Impact: 30.5)
  * `migrateLegacyPattern` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 197`, `args: 49`, `func_start: 42`, `class_start: 20`
* *Risk/State:* `state_mutation: 236`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 9`, `api: 2`, `concurrency: 35`, `import: 4`
* *Defense:* `safety: 80`, `immutability_locks: 146`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, CryptoKit, Security, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/GatewayConnection.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.917 IQR)
- **Top Global Matches:** file_cluster_4: 11.917, file_cluster_8: 12.234, file_cluster_17: 12.549
- **Magnitude:** 940.38 | **LOC:** 743 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.0755%), Tech Debt (91.603%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 88.6)
    * *Intent:* // MARK: - Low-level request
  * `canonicalizeSessionKey` (Impact: 36.6)
  * `sendAgent` (Impact: 30.3)
  * `sessionsPreview` (Impact: 21.2)
    * *Intent:* // MARK: - Sessions
  * `skillsUpdate` (Impact: 20.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 200`, `args: 56`, `func_start: 53`, `class_start: 11`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 72`, `duplicate_logic: 8`, `orphaned_logic: 11`
* *Architecture:* `api: 1`, `concurrency: 205`, `import: 5`
* *Defense:* `safety: 62`, `doc: 5`, `sync_locks: 3`, `immutability_locks: 96`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, OpenClawChatUI, OpenClawProtocol, OpenClawKit, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.887 IQR)
- **Top Global Matches:** file_cluster_13: 12.887, file_cluster_2: 12.95, file_cluster_8: 13.136
- **Magnitude:** 900.56 | **LOC:** 1210 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.9535%), Tech Debt (8.5497%)
**Top Internal Functions/Classes:**
  * `OnboardingFlow` (Impact: 108.3)
  * `GatewayStep` (Impact: 61.8)
  * `PermissionsStep` (Impact: 33.3)
  * `FinalStep` (Impact: 33.3)
  * `GatewayModeChip` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 108`, `args: 25`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 547`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 12`, `import: 79`
* *Defense:* `safety: 6`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` androidx.compose.ui.text.style.TextOverflow, androidx.compose.animation.AnimatedVisibility, androidx.compose.foundation.shape.RoundedCornerShape, androidx.compose.foundation.layout.fillMaxSize, androidx.compose.runtime.remember, android.os.Build, androidx.compose.foundation.layout.windowInsetsPadding, androidx.compose.foundation.layout.only...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/shared/OpenClawKit/Sources/OpenClawChatUI/ChatViewModel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.284 IQR)
- **Top Global Matches:** file_cluster_4: 12.284, file_cluster_17: 12.474, file_cluster_8: 12.544
- **Magnitude:** 791.04 | **LOC:** 686 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8317%), Tech Debt (34.1312%)
**Top Internal Functions/Classes:**
  * `handleAgentEvent` (Impact: 61.8)
  * `messageIdentityKey` (Impact: 50.4)
  * `handleChatEvent` (Impact: 44.6)
  * `performSend` (Impact: 30.2)
  * `reconcileMessageIDs` (Impact: 29.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 157`, `args: 42`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 130`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 91`, `import: 7`
* *Defense:* `safety: 58`, `sync_locks: 5`, `immutability_locks: 80`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, Foundation, AppKit, UniformTypeIdentifiers, UIKit, OpenClawKit, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/AppState.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.05 IQR)
- **Top Global Matches:** file_cluster_4: 12.05, file_cluster_8: 12.442, file_cluster_0: 12.588
- **Magnitude:** 790.42 | **LOC:** 732 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.7278%), Tech Debt (25.4701%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 114.7)
  * `updatedRemoteGatewayConfig` (Impact: 81.6)
  * `applyConfigOverrides` (Impact: 63.4)
  * `syncGatewayConfigIfNeeded` (Impact: 51.5)
  * `updateRemoteTarget` (Impact: 26.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 137`, `args: 31`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `state_mutation: 121`, `orphaned_logic: 9`
* *Architecture:* `io: 50`, `concurrency: 158`, `import: 5`
* *Defense:* `safety: 61`, `doc: 2`, `sync_locks: 8`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, Foundation, ServiceManagement, AppKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ExecApprovalsSocket.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.098 IQR)
- **Top Global Matches:** file_cluster_4: 12.098, file_cluster_8: 12.135, file_cluster_0: 12.335
- **Magnitude:** 738.54 | **LOC:** 788 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.8086%), Tech Debt (63.838%)
**Top Internal Functions/Classes:**
  * `handle` (Impact: 60.4)
  * `buildAccessoryView` (Impact: 58.0)
  * `handleClient` (Impact: 48.0)
  * `requestDecisionSync` (Impact: 28.8)
  * `readLine` (Impact: 26.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 175`, `args: 42`, `func_start: 28`, `class_start: 14`
* *Risk/State:* `state_mutation: 198`, `duplicate_logic: 8`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 74`, `import: 6`
* *Defense:* `safety: 33`, `sync_locks: 5`, `immutability_locks: 110`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, Darwin, CryptoKit, AppKit, OpenClawKit, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClawDiscovery/GatewayDiscoveryModel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.504 IQR)
- **Top Global Matches:** file_cluster_4: 12.504, file_cluster_17: 12.734, file_cluster_8: 12.742
- **Magnitude:** 724.82 | **LOC:** 683 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.2266%), Tech Debt (66.5504%)
**Top Internal Functions/Classes:**
  * `updateGateways` (Impact: 43.4)
  * `parseGatewayTXT` (Impact: 33.8)
  * `scheduleWideAreaFallback` (Impact: 27.6)
  * `ensureServiceResolution` (Impact: 26.2)
  * `init` (Impact: 25.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 176`, `args: 50`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 159`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 36`, `concurrency: 86`, `import: 5`
* *Defense:* `safety: 53`, `sync_locks: 8`, `immutability_locks: 122`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, Foundation, Network, OpenClawKit, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/NodePairingApprovalPrompter.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.543 IQR)
- **Top Global Matches:** file_cluster_4: 11.543, file_cluster_8: 11.742, file_cluster_13: 11.937
- **Magnitude:** 692.74 | **LOC:** 683 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.0256%), Tech Debt (8.8467%)
**Top Internal Functions/Classes:**
  * `handle` (Impact: 35.5)
  * `resolveSSHTarget` (Impact: 33.0)
  * `trySilentApproveIfPossible` (Impact: 31.1)
  * `presentAlert` (Impact: 26.8)
  * `loadPendingRequestsFromGateway` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 162`, `args: 35`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 114`, `import: 9`
* *Defense:* `safety: 42`, `sync_locks: 7`, `immutability_locks: 113`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, Foundation, UserNotifications, OSLog, OpenClawIPC, AppKit, OpenClawKit, OpenClawDiscovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/GatewayEndpointStore.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.006 IQR)
- **Top Global Matches:** file_cluster_8: 11.006, file_cluster_4: 11.315, file_cluster_0: 11.445
- **Magnitude:** 649.88 | **LOC:** 729 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8404%), Tech Debt (27.0127%)
**Top Internal Functions/Classes:**
  * `resolveGatewayPassword` (Impact: 51.5)
  * `dashboardURL` (Impact: 50.4)
  * `ensureRemoteConfig` (Impact: 45.3)
  * `maybeFallbackToTailnet` (Impact: 37.2)
  * `resolveGatewayToken` (Impact: 31.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 124`, `args: 30`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `api: 12`, `concurrency: 61`, `import: 3`
* *Defense:* `safety: 86`, `doc: 6`, `sync_locks: 3`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, ConcurrencyExtras, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/chat/ChatController.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.614 IQR)
- **Top Global Matches:** file_cluster_4: 12.614, file_cluster_13: 12.911, file_cluster_8: 12.938
- **Magnitude:** 634.84 | **LOC:** 541 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendMessage` (Impact: 38.2)
  * `handleAgentEvent` (Impact: 36.4)
  * `handleChatEvent` (Impact: 36.2)
  * `parseAssistantDeltaText` (Impact: 30.7)
  * `parseSessions` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 85`, `args: 30`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 154`
* *Architecture:* `api: 8`, `concurrency: 133`, `import: 17`
* *Defense:* `safety: 26`, `sync_locks: 7`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ai.openclaw.android.gateway.GatewaySession, kotlinx.coroutines.flow.StateFlow, kotlinx.coroutines.flow.asStateFlow, kotlinx.serialization.json.JsonElement, kotlinx.serialization.json.JsonArray, kotlinx.coroutines.delay, kotlinx.coroutines.CoroutineScope, kotlinx.serialization.json.buildJsonObject...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `apps/macos/Sources/OpenClawMacCLI/WizardCommand.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.443 IQR)
- **Top Global Matches:** file_cluster_8: 11.443, file_cluster_17: 11.705, file_cluster_4: 11.749
- **Magnitude:** 632.84 | **LOC:** 538 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5528%), Tech Debt (9.1223%)
**Top Internal Functions/Classes:**
  * `promptAnswer` (Impact: 80.3)
  * `runWizard` (Impact: 66.0)
  * `sendConnect` (Impact: 51.0)
  * `promptMultiSelect` (Impact: 48.4)
  * `promptSelect` (Impact: 45.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 102`, `args: 21`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `concurrency: 32`, `import: 4`
* *Defense:* `safety: 51`, `immutability_locks: 117`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Darwin, OpenClawKit, OpenClawProtocol, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/shared/OpenClawKit/Sources/OpenClawKit/GatewayNodeSession.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.097 IQR)
- **Top Global Matches:** file_cluster_4: 12.097, file_cluster_0: 12.529, file_cluster_8: 12.63
- **Magnitude:** 629.74 | **LOC:** 443 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (22.1625%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 57.0)
  * `invokeWithTimeout` (Impact: 43.8)
  * `decodeParamsJSON` (Impact: 30.2)
  * `handleEvent` (Impact: 28.0)
  * `handlePush` (Impact: 23.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 114`, `args: 34`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 5`
* *Architecture:* `api: 24`, `concurrency: 153`, `import: 3`
* *Defense:* `safety: 40`, `sync_locks: 8`, `immutability_locks: 73`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, OSLog, OpenClawProtocol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/voice/MicCaptureManager.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.176 IQR)
- **Top Global Matches:** file_cluster_4: 13.176, file_cluster_13: 13.345, file_cluster_8: 13.486
- **Magnitude:** 618.42 | **LOC:** 524 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleGatewayEvent` (Impact: 36.7)
  * `sendQueuedIfIdle` (Impact: 33.7)
  * `parseAssistantText` (Impact: 28.7)
  * `scheduleRestart` (Impact: 25.3)
  * `onError` (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 96`, `args: 34`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`
* *Architecture:* `api: 12`, `concurrency: 92`, `import: 22`
* *Defense:* `safety: 26`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.294
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kotlinx.coroutines.flow.StateFlow, androidx.core.content.ContextCompat, android.os.Looper, kotlinx.serialization.json.JsonArray, android.speech.RecognizerIntent, kotlinx.serialization.json.JsonPrimitive, kotlinx.serialization.json.JsonObject, kotlinx.coroutines.CoroutineScope...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.441 IQR)
- **Top Global Matches:** file_cluster_4: 12.441, file_cluster_13: 12.451, file_cluster_8: 12.473
- **Magnitude:** 618.36 | **LOC:** 690 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.11%), Tech Debt (30.691%)
**Top Internal Functions/Classes:**
  * `normalizeCanvasHostUrl` (Impact: 53.4)
  * `buildConnectParams` (Impact: 36.3)
  * `handleInvokeEvent` (Impact: 35.2)
  * `handleEvent` (Impact: 24.9)
  * `isLoopbackHost` (Impact: 22.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 125`, `args: 46`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 84`, `duplicate_logic: 4`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 79`, `import: 30`
* *Defense:* `safety: 59`, `sync_locks: 4`, `immutability_locks: 144`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.598
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` okhttp3.Response, kotlinx.serialization.json.JsonElement, kotlinx.coroutines.Dispatchers, kotlinx.serialization.json.JsonArray, kotlinx.coroutines.TimeoutCancellationException, kotlinx.serialization.json.JsonPrimitive, kotlinx.serialization.json.JsonObject, kotlinx.coroutines.isActive...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `apps/android/app/src/main/java/ai/openclaw/android/NodeRuntime.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.525 IQR)
- **Top Global Matches:** file_cluster_4: 12.525, file_cluster_13: 12.722, file_cluster_16: 12.951
- **Magnitude:** 559.44 | **LOC:** 815 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (12.6266%)
**Top Internal Functions/Classes:**
  * `requestCanvasRehydrate` (Impact: 31.9)
  * `init` (Impact: 18.4)
  * `updateStatus` (Impact: 18.2)
  * `applyMainSessionKey` (Impact: 14.3)
  * `maybeNavigateToA2uiOnConnect` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 64`, `args: 22`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 190`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 249`, `import: 39`
* *Defense:* `safety: 4`, `sync_locks: 3`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` kotlinx.coroutines.flow.StateFlow, androidx.core.content.ContextCompat, kotlinx.coroutines.Dispatchers, kotlinx.serialization.json.JsonArray, ai.openclaw.android.gateway.GatewayEndpoint, ai.openclaw.android.gateway.DeviceAuthStore, ai.openclaw.android.voice.VoiceConversationEntry, ai.openclaw.android.gateway.GatewayDiscovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ChannelsSettings+ChannelState.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.32 IQR)
- **Top Global Matches:** file_cluster_17: 13.32, file_cluster_8: 13.442, file_cluster_13: 13.719
- **Magnitude:** 537.96 | **LOC:** 509 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (22.5919%)
**Top Internal Functions/Classes:**
  * `channelHasError` (Impact: 95.5)
  * `channelLastCheck` (Impact: 64.5)
  * `channelEnabled` (Impact: 49.6)
  * `channelDetails` (Impact: 30.2)
  * `channelTint` (Impact: 25.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 177`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`, `orphaned_logic: 6`
* *Architecture:* `import: 2`
* *Defense:* `safety: 83`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SwiftUI, OpenClawProtocol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/ShareExtension/ShareViewController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.076 IQR)
- **Top Global Matches:** file_cluster_4: 12.076, file_cluster_8: 12.116, file_cluster_17: 12.207
- **Magnitude:** 536.48 | **LOC:** 549 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1169%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendMessageToGateway` (Impact: 68.3)
  * `extractSharedContent` (Impact: 47.9)
  * `shouldRetryWithLegacyClientId` (Impact: 36.8)
  * `sanitizeDraftFragment` (Impact: 21.1)
  * `prepareDraft` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 122`, `args: 33`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `api: 5`, `concurrency: 60`, `import: 5`
* *Defense:* `safety: 47`, `sync_locks: 4`, `immutability_locks: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, os, UniformTypeIdentifiers, UIKit, OpenClawKit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `apps/macos/Sources/OpenClaw/HeartbeatStore.swift` (SWIFT) | Magnitude: 35.06 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, branch: 16, safety: 10, structural_boundaries: 9
- `apps/ios/Tests/ScreenControllerTests.swift` (SWIFT) | Magnitude: 68.66 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 65, test: 29, branch: 23, immutability_locks: 16
- `apps/ios/Tests/NodeAppModelInvokeTests.swift` (SWIFT) | Magnitude: 399.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 430, immutability_locks: 131, concurrency: 101, branch: 100
- `apps/macos/Tests/OpenClawIPCTests/VoiceWakeRuntimeTests.swift` (SWIFT) | Magnitude: 45.52 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, immutability_locks: 22, test: 19, structural_boundaries: 18
- `apps/macos/Tests/OpenClawIPCTests/AudioInputDeviceObserverTests.swift` (SWIFT) | Magnitude: 7.9 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, test: 4, decorators: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/telegram/bot/types.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 8, indent_spaces: 8, branch: 7
- `src/config/types.signal.ts` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, branch: 18, doc: 14, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/tui/components/custom-editor.ts` (TYPESCRIPT) | Magnitude: 11.33 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 69, indent_spaces: 55, branch: 32, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/infra/provider-usage.fetch.gemini.ts` (TYPESCRIPT) | Magnitude: 6.85 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, branch: 18, state_mutation: 18, structural_boundaries: 10
- `extensions/diagnostics-otel/src/service.ts` (TYPESCRIPT) | Magnitude: 93.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 603, branch: 221, structural_boundaries: 95, immutability_locks: 92
- `src/commands/channels/logs.ts` (TYPESCRIPT) | Magnitude: 8.41 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 33, branch: 31, immutability_locks: 24
- `src/agents/pi-embedded-subscribe.ts` (TYPESCRIPT) | Magnitude: 18.95 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 52, branch: 39, immutability_locks: 37
- `apps/macos/Sources/OpenClaw/TalkOverlay.swift` (SWIFT) | Magnitude: 108.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 33, branch: 30, immutability_locks: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `apps/android/app/src/main/java/ai/openclaw/android/ui/chat/SessionFilters.kt` (KOTLIN) | Magnitude: 97.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 27, branch: 26, immutability_locks: 16
- `src/channels/plugins/bluebubbles-actions.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, generics: 6, immutability_locks: 5
- `src/infra/map-size.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, branch: 4, state_mutation: 3, structural_boundaries: 2
- `src/agents/sandbox/types.docker.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, generics: 4, ui_framework: 3
- `src/plugin-sdk/config-paths.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, safety: 7, branch: 4, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `apps/macos/Sources/OpenClaw/AboutSettings.swift` (SWIFT) | Magnitude: 78.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 164, state_mutation: 52, branch: 45, structural_boundaries: 31
- `apps/macos/Sources/OpenClaw/ConfigSettings.swift` (SWIFT) | Magnitude: 284.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 351, branch: 103, structural_boundaries: 80, immutability_locks: 56
- `src/channels/allowlists/resolve-utils.ts` (TYPESCRIPT) | Magnitude: 10.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, branch: 53, structural_boundaries: 33, immutability_locks: 31
- `src/agents/pi-extensions/session-manager-runtime-registry.ts` (TYPESCRIPT) | Magnitude: 4.49 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, branch: 7, state_mutation: 6
- `src/agents/tools/sessions-announce-target.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, branch: 40, safety: 21, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `apps/macos/Sources/OpenClaw/TailscaleIntegrationSection.swift` (SWIFT) | Magnitude: 297.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 348, branch: 108, state_mutation: 94, structural_boundaries: 79
- `apps/ios/Sources/Screen/ScreenTab.swift` (SWIFT) | Magnitude: 17.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, ui_framework: 6, state_mutation: 2
- `apps/shared/OpenClawKit/Sources/OpenClawChatUI/ChatComposer.swift` (SWIFT) | Magnitude: 210.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 434, branch: 98, state_mutation: 87, structural_boundaries: 75
- `apps/ios/Sources/RootTabs.swift` (SWIFT) | Magnitude: 67.06 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 100, state_mutation: 39, structural_boundaries: 22, branch: 21
- `apps/macos/Sources/OpenClaw/GeneralSettings.swift` (SWIFT) | Magnitude: 210.8 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 644, branch: 139, structural_boundaries: 88, ui_framework: 85

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `extensions/qwen-portal-auth/oauth.ts` (TYPESCRIPT) | Magnitude: 6.45 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 136, branch: 49, structural_boundaries: 37, concurrency: 32
- `src/browser/extension-relay.ts` (TYPESCRIPT) | Magnitude: 128.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 809, branch: 281, structural_boundaries: 183, immutability_locks: 116
- `apps/shared/OpenClawKit/Sources/OpenClawKit/AudioStreamingProtocols.swift` (SWIFT) | Magnitude: 15.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, args: 4, func_start: 4, class_start: 4
- `apps/macos/Sources/OpenClaw/ScreenRecordService.swift` (SWIFT) | Magnitude: 274.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 226, branch: 95, structural_boundaries: 49, immutability_locks: 39
- `src/plugins/services.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 24, branch: 13, concurrency: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ui/src/ui/chat/constants.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, api: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/web/auto-reply/types.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, branch: 18, structural_boundaries: 14, generics: 5
- `extensions/msteams/src/attachments/remote-media.ts` (TYPESCRIPT) | Magnitude: 1.65 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, branch: 13, structural_boundaries: 13, concurrency: 6
- `src/cli/daemon-cli/shared.ts` (TYPESCRIPT) | Magnitude: 16.21 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 51, branch: 48, state_mutation: 27
- `src/web/inbound/send-api.ts` (TYPESCRIPT) | Magnitude: 12.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 99, branch: 37, structural_boundaries: 21, concurrency: 19
- `src/canvas-host/file-resolver.ts` (TYPESCRIPT) | Magnitude: 4.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, branch: 11, io: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/agents/schema/typebox.ts` -> **Severity: 821.142** (Blast Radius: 12.132 * Doc Risk: 67.684%)
- `src/wizard/prompts.ts` -> **Severity: 429.362** (Blast Radius: 4.334 * Doc Risk: 99.0684%)
- `src/infra/ws.ts` -> **Severity: 205.4** (Blast Radius: 4.108 * Doc Risk: 50.0%)
- `extensions/msteams/src/sdk.ts` -> **Severity: 138.299** (Blast Radius: 1.396 * Doc Risk: 99.0684%)
- `apps/android/app/src/main/java/ai/openclaw/android/SecurePrefs.kt` -> **Severity: 61.619** (Blast Radius: 0.761 * Doc Risk: 80.9706%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
