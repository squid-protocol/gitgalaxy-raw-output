# ARCHITECTURAL_BRIEF: openclaw-typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/openclaw-typescript` |
| **Timestamp** | `2026-08-03T21:17:36.529525+00:00` |
| **Scan Duration** | `14.18s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3398 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Modularity | 0.7754 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `5.778`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2455 | 67.4% |
| file_cluster_13 | 480 | 13.2% |
| file_cluster_4 | 370 | 10.2% |
| file_cluster_17 | 84 | 2.3% |
| file_cluster_2 | 48 | 1.3% |
| file_cluster_0 | 25 | 0.7% |
| file_cluster_16 | 14 | 0.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 32.3 | 24.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 22.2 | 14.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 32.5 | 2.6 | 80.0 |
| API Exposure | 0.0 | 19.6 | 6.0 | 6.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 42.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.6 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 95.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 54.8 | 55.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.0 | 1.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `renderApp` (@ `ui/src/ui/app-render.ts`) -> Impact: **1947.2** | LOC: 1004
- `vectorToBlob` (@ `src/memory/manager-embedding-ops.ts`) -> Impact: **1746.9** | LOC: 770
- `mergeConfig` (@ `src/agents/memory-search.ts`) -> Impact: **1638.7** | LOC: 216
- `initPromise` (@ `src/browser/extension-relay.ts`) -> Impact: **1511.3** | LOC: 709
- `formatCliCommand` (@ `src/security/audit-channel.ts`) -> Impact: **1371.3** | LOC: 481
- `createMatrixRoomMessageHandler` (@ `extensions/matrix/src/matrix/monitor/handler.ts`) -> Impact: **1311.0** | LOC: 659
- `xmlEscapeAttr` (@ `src/media-understanding/apply.ts`) -> Impact: **1290.2** | LOC: 485
  * *Intent:* /**
- `processMessage` (@ `extensions/bluebubbles/src/monitor-processing.ts`) -> Impact: **1243.7** | LOC: 674
- `createSignalEventHandler` (@ `src/signal/monitor/event-handler.ts`) -> Impact: **1228.7** | LOC: 674
- `buildFallbackNick` (@ `extensions/irc/src/client.ts`) -> Impact: **1165.7** | LOC: 313

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `start` (@ `Swabble/Sources/SwabbleCore/Speech/SpeechPipeline.swift`) -> **O(2^N) [Recursive]**
- `start` (@ `apps/ios/Sources/Gateway/GatewayDiscoveryModel.swift`) -> **O(2^N) [Recursive]**
- `pedometer` (@ `apps/ios/Sources/Motion/MotionService.swift`) -> **O(2^N) [Recursive]**
- `activities` (@ `apps/ios/Sources/Motion/MotionService.swift`) -> **O(2^N) [Recursive]**
- `renderNode` (@ `apps/macos/Sources/OpenClaw/ChannelConfigForm.swift`) -> **O(2^N) [Recursive]**
- `node` (@ `apps/macos/Sources/OpenClaw/ConfigSchemaSupport.swift`) -> **O(2^N) [Recursive]**
- `configure` (@ `apps/macos/Sources/OpenClaw/ControlChannel.swift`) -> **O(2^N) [Recursive]**
- `request` (@ `apps/macos/Sources/OpenClaw/GatewayConnection.swift`) -> **O(2^N) [Recursive]**
  * *Intent:* // MARK: - Low-level request
- `run` (@ `apps/macos/Sources/OpenClaw/NodeMode/MacNodeModeCoordinator.swift`) -> **O(2^N) [Recursive]**
- `send` (@ `apps/macos/Sources/OpenClaw/NotificationManager.swift`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `vectorToBlob` (@ `src/memory/manager-embedding-ops.ts`) -> DB Complexity: **214**
- `read_config_gateway_token_[Truncated]` (@ `docker-setup.sh`) -> DB Complexity: **200**
- `OnboardingFlow` (@ `apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`) -> DB Complexity: **151**
- `extractExecutableFromExecLine` (@ `src/browser/chrome.executables.ts`) -> DB Complexity: **149**
- `ConnectTabScreen` (@ `apps/android/app/src/main/java/ai/openclaw/android/ui/ConnectTabScreen.kt`) -> DB Complexity: **143**
- `SettingsSheet` (@ `apps/android/app/src/main/java/ai/openclaw/android/ui/SettingsSheet.kt`) -> DB Complexity: **118**
- `is_root` (@ `setup-podman.sh`) -> DB Complexity: **114**
- `registerPluginsCli` (@ `src/cli/plugins-cli.ts`) -> DB Complexity: **113**
- `GatewayStep` (@ `apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`) -> DB Complexity: **112**
- `readSessionMessages` (@ `src/gateway/session-utils.fs.ts`) -> DB Complexity: **109**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `apps/macos/Sources/OpenClaw` | 194 | 66278.32 | 49.89% | 47.07% |
| `apps/shared/OpenClawKit/Sources/OpenClawKit` | 52 | 8162.38 | 60.57% | 71.14% |
| `__monolith__` | 18 | 6199.76 | 20.71% | 2.63% |
| `apps/macos/Tests/OpenClawIPCTests` | 97 | 6052.94 | 12.82% | 0.0% |
| `apps/shared/OpenClawKit/Sources/OpenClawChatUI` | 14 | 4365.8 | 58.55% | 14.39% |
| `apps/ios/Sources/Model` | 3 | 3896.32 | 59.59% | 55.25% |
| `apps/ios/Sources/Gateway` | 14 | 3791.68 | 46.89% | 49.94% |
| `apps/android/app/src/main/java/ai/openclaw/android/ui` | 13 | 3595.16 | 59.59% | 24.74% |
| `apps/macos/Sources/OpenClaw/NodeMode` | 5 | 3465.1 | 71.54% | 28.08% |
| `apps/android/app/src/main/java/ai/openclaw/android/voice` | 6 | 3387.4 | 75.21% | 51.98% |

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
- `Swabble/Sources/swabble/Commands/TestHookCommand.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Settings/SettingsTab.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Settings/VoiceWakeWordsSettingsView.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/channels/dock.ts` -> **3** Orphaned Functions | **45** Duplicates
- `apps/ios/Sources/Model/NodeAppModel.swift` -> **39** Orphaned Functions | **0** Duplicates
- `apps/ios/Tests/NodeAppModelInvokeTests.swift` -> **29** Orphaned Functions | **0** Duplicates
- `src/cli/program/register.subclis.ts` -> **0** Orphaned Functions | **28** Duplicates
- `src/commands/doctor-config-flow.ts` -> **0** Orphaned Functions | **28** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`apps/android/app/src/main/java/ai/openclaw/android/MainActivity.kt`** -> AI Confidence: **99.48%**
2. **`apps/android/app/src/main/java/ai/openclaw/android/NodeForegroundService.kt`** -> AI Confidence: **99.48%**
3. **`apps/android/app/src/main/java/ai/openclaw/android/NodeRuntime.kt`** -> AI Confidence: **99.48%**
4. **`apps/android/app/src/main/java/ai/openclaw/android/PermissionRequester.kt`** -> AI Confidence: **99.48%**
5. **`apps/android/app/src/main/java/ai/openclaw/android/ScreenCaptureRequester.kt`** -> AI Confidence: **99.48%**
6. **`apps/android/app/src/main/java/ai/openclaw/android/SecurePrefs.kt`** -> AI Confidence: **99.48%**
7. **`apps/android/app/src/main/java/ai/openclaw/android/chat/ChatController.kt`** -> AI Confidence: **99.48%**
8. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewayDiscovery.kt`** -> AI Confidence: **99.48%**
9. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt`** -> AI Confidence: **99.48%**
10. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewayTls.kt`** -> AI Confidence: **99.48%**
11. **`apps/android/app/src/main/java/ai/openclaw/android/node/AppUpdateHandler.kt`** -> AI Confidence: **99.48%**
12. **`apps/android/app/src/main/java/ai/openclaw/android/node/CameraCaptureManager.kt`** -> AI Confidence: **99.48%**
13. **`apps/android/app/src/main/java/ai/openclaw/android/node/CameraHandler.kt`** -> AI Confidence: **99.48%**
14. **`apps/android/app/src/main/java/ai/openclaw/android/node/CanvasController.kt`** -> AI Confidence: **99.48%**
15. **`apps/android/app/src/main/java/ai/openclaw/android/node/ConnectionManager.kt`** -> AI Confidence: **99.48%**
16. **`apps/android/app/src/main/java/ai/openclaw/android/node/DeviceHandler.kt`** -> AI Confidence: **99.48%**
17. **`apps/android/app/src/main/java/ai/openclaw/android/node/DeviceNotificationListenerService.kt`** -> AI Confidence: **99.48%**
18. **`apps/android/app/src/main/java/ai/openclaw/android/node/GatewayEventHandler.kt`** -> AI Confidence: **99.48%**
19. **`apps/android/app/src/main/java/ai/openclaw/android/node/InvokeCommandRegistry.kt`** -> AI Confidence: **99.48%**
20. **`apps/android/app/src/main/java/ai/openclaw/android/node/InvokeDispatcher.kt`** -> AI Confidence: **99.48%**
21. **`apps/android/app/src/main/java/ai/openclaw/android/node/LocationCaptureManager.kt`** -> AI Confidence: **99.48%**
22. **`apps/android/app/src/main/java/ai/openclaw/android/node/LocationHandler.kt`** -> AI Confidence: **99.48%**
23. **`apps/android/app/src/main/java/ai/openclaw/android/node/ScreenRecordManager.kt`** -> AI Confidence: **99.48%**
24. **`apps/android/app/src/main/java/ai/openclaw/android/node/SmsManager.kt`** -> AI Confidence: **99.48%**
25. **`apps/android/app/src/main/java/ai/openclaw/android/tools/ToolDisplay.kt`** -> AI Confidence: **99.48%**
26. **`apps/android/app/src/main/java/ai/openclaw/android/ui/CameraHudOverlay.kt`** -> AI Confidence: **99.48%**
27. **`apps/android/app/src/main/java/ai/openclaw/android/ui/CanvasScreen.kt`** -> AI Confidence: **99.48%**
28. **`apps/android/app/src/main/java/ai/openclaw/android/ui/ConnectTabScreen.kt`** -> AI Confidence: **99.48%**
29. **`apps/android/app/src/main/java/ai/openclaw/android/ui/GatewayConfigResolver.kt`** -> AI Confidence: **99.48%**
30. **`apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`** -> AI Confidence: **99.48%**
31. **`apps/android/app/src/main/java/ai/openclaw/android/ui/OpenClawTheme.kt`** -> AI Confidence: **99.48%**
32. **`apps/android/app/src/main/java/ai/openclaw/android/ui/PostOnboardingTabs.kt`** -> AI Confidence: **99.48%**
33. **`apps/android/app/src/main/java/ai/openclaw/android/ui/SettingsSheet.kt`** -> AI Confidence: **99.48%**
34. **`apps/android/app/src/main/java/ai/openclaw/android/ui/TalkOrbOverlay.kt`** -> AI Confidence: **99.48%**
35. **`apps/android/app/src/main/java/ai/openclaw/android/ui/VoiceTabScreen.kt`** -> AI Confidence: **99.48%**
36. **`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatComposer.kt`** -> AI Confidence: **99.48%**
37. **`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMarkdown.kt`** -> AI Confidence: **99.48%**
38. **`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMessageListCard.kt`** -> AI Confidence: **99.48%**
39. **`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMessageViews.kt`** -> AI Confidence: **99.48%**
40. **`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatSheetContent.kt`** -> AI Confidence: **99.48%**
41. **`apps/android/app/src/main/java/ai/openclaw/android/voice/MicCaptureManager.kt`** -> AI Confidence: **99.48%**
42. **`apps/android/app/src/main/java/ai/openclaw/android/voice/TalkModeManager.kt`** -> AI Confidence: **99.48%**
43. **`apps/android/app/src/main/java/ai/openclaw/android/voice/VoiceWakeManager.kt`** -> AI Confidence: **99.48%**
44. **`apps/android/benchmark/src/main/java/ai/openclaw/android/benchmark/StartupMacrobenchmark.kt`** -> AI Confidence: **99.48%**
45. **`src/agents/pi-embedded-subscribe.handlers.messages.ts`** -> AI Confidence: **99.48%**
46. **`src/agents/pi-tools.ts`** -> AI Confidence: **99.48%**
47. **`src/agents/system-prompt.ts`** -> AI Confidence: **99.48%**
48. **`src/agents/tools/sessions-list-tool.ts`** -> AI Confidence: **99.48%**
49. **`src/auto-reply/reply/directive-handling.impl.ts`** -> AI Confidence: **99.48%**
50. **`src/cli/cron-cli/register.cron-edit.ts`** -> AI Confidence: **99.48%**
51. **`src/cli/daemon-cli/status.print.ts`** -> AI Confidence: **99.48%**
52. **`src/commands/channels/capabilities.ts`** -> AI Confidence: **99.48%**
53. **`src/config/sessions/metadata.ts`** -> AI Confidence: **99.48%**
54. **`src/cron/normalize.ts`** -> AI Confidence: **99.48%**
55. **`src/cron/service/store.ts`** -> AI Confidence: **99.48%**
56. **`src/gateway/server-runtime-config.ts`** -> AI Confidence: **99.48%**
57. **`src/gateway/ws-log.ts`** -> AI Confidence: **99.48%**
58. **`src/security/audit-channel.ts`** -> AI Confidence: **99.48%**
59. **`extensions/bluebubbles/src/media-send.ts`** -> AI Confidence: **99.39%**
60. **`extensions/bluebubbles/src/monitor-processing.ts`** -> AI Confidence: **99.39%**
61. **`extensions/feishu/src/bot.ts`** -> AI Confidence: **99.39%**
62. **`extensions/llm-task/src/llm-task-tool.ts`** -> AI Confidence: **99.39%**
63. **`extensions/matrix/src/matrix/client/config.ts`** -> AI Confidence: **99.39%**
64. **`extensions/matrix/src/matrix/monitor/handler.ts`** -> AI Confidence: **99.39%**
65. **`extensions/msteams/src/monitor-handler/message-handler.ts`** -> AI Confidence: **99.39%**
66. **`extensions/tlon/src/monitor/index.ts`** -> AI Confidence: **99.39%**
67. **`src/agents/bash-tools.exec-host-gateway.ts`** -> AI Confidence: **99.39%**
68. **`src/agents/bash-tools.exec-host-node.ts`** -> AI Confidence: **99.39%**
69. **`src/agents/bash-tools.exec.ts`** -> AI Confidence: **99.39%**
70. **`src/agents/cli-runner.ts`** -> AI Confidence: **99.39%**
71. **`src/agents/openclaw-tools.ts`** -> AI Confidence: **99.39%**
72. **`src/agents/pi-embedded-runner/run/payloads.ts`** -> AI Confidence: **99.39%**
73. **`src/agents/pi-embedded-subscribe.handlers.tools.ts`** -> AI Confidence: **99.39%**
74. **`src/agents/pi-tools.policy.ts`** -> AI Confidence: **99.39%**
75. **`src/agents/subagent-spawn.ts`** -> AI Confidence: **99.39%**
76. **`src/agents/tools/cron-tool.ts`** -> AI Confidence: **99.39%**
77. **`src/agents/tools/telegram-actions.ts`** -> AI Confidence: **99.39%**
78. **`src/auto-reply/reply/block-streaming.ts`** -> AI Confidence: **99.39%**
79. **`src/auto-reply/reply/commands-allowlist.ts`** -> AI Confidence: **99.39%**
80. **`src/auto-reply/reply/directive-handling.model.ts`** -> AI Confidence: **99.39%**
81. **`src/auto-reply/reply/directive-handling.persist.ts`** -> AI Confidence: **99.39%**
82. **`src/auto-reply/reply/get-reply-directives.ts`** -> AI Confidence: **99.39%**
83. **`src/auto-reply/reply/get-reply-run.ts`** -> AI Confidence: **99.39%**
84. **`src/auto-reply/reply/groups.ts`** -> AI Confidence: **99.39%**
85. **`src/auto-reply/reply/reply-delivery.ts`** -> AI Confidence: **99.39%**
86. **`src/auto-reply/reply/route-reply.ts`** -> AI Confidence: **99.39%**
87. **`src/auto-reply/reply/session.ts`** -> AI Confidence: **99.39%**
88. **`src/auto-reply/status.ts`** -> AI Confidence: **99.39%**
89. **`src/browser/config.ts`** -> AI Confidence: **99.39%**
90. **`src/cli/cron-cli/register.cron-add.ts`** -> AI Confidence: **99.39%**
91. **`src/cli/daemon-cli/status.gather.ts`** -> AI Confidence: **99.39%**
92. **`src/cli/gateway-cli/run.ts`** -> AI Confidence: **99.39%**
93. **`src/cli/nodes-cli/register.invoke.ts`** -> AI Confidence: **99.39%**
94. **`src/cli/qr-cli.ts`** -> AI Confidence: **99.39%**
95. **`src/cli/update-cli/status.ts`** -> AI Confidence: **99.39%**
96. **`src/commands/agent/delivery.ts`** -> AI Confidence: **99.39%**
97. **`src/commands/agent/session-store.ts`** -> AI Confidence: **99.39%**
98. **`src/commands/agent/session.ts`** -> AI Confidence: **99.39%**
99. **`src/commands/doctor-config-flow.ts`** -> AI Confidence: **99.39%**
100. **`src/commands/doctor-security.ts`** -> AI Confidence: **99.39%**
101. **`src/commands/gateway-status.ts`** -> AI Confidence: **99.39%**
102. **`src/commands/health.ts`** -> AI Confidence: **99.39%**
103. **`src/config/defaults.ts`** -> AI Confidence: **99.39%**
104. **`src/config/validation.ts`** -> AI Confidence: **99.39%**
105. **`src/cron/isolated-agent/run.ts`** -> AI Confidence: **99.39%**
106. **`src/discord/monitor/message-handler.preflight.ts`** -> AI Confidence: **99.39%**
107. **`src/gateway/client.ts`** -> AI Confidence: **99.39%**
108. **`src/gateway/server-methods/agent.ts`** -> AI Confidence: **99.39%**
109. **`src/gateway/server-methods/exec-approval.ts`** -> AI Confidence: **99.39%**
110. **`src/gateway/server-methods/system.ts`** -> AI Confidence: **99.39%**
111. **`src/gateway/server-node-events.ts`** -> AI Confidence: **99.39%**
112. **`src/gateway/sessions-patch.ts`** -> AI Confidence: **99.39%**
113. **`src/hooks/gmail-ops.ts`** -> AI Confidence: **99.39%**
114. **`src/imessage/monitor/inbound-processing.ts`** -> AI Confidence: **99.39%**
115. **`src/imessage/send.ts`** -> AI Confidence: **99.39%**
116. **`src/infra/exec-approvals.ts`** -> AI Confidence: **99.39%**
117. **`src/infra/outbound/message-action-params.ts`** -> AI Confidence: **99.39%**
118. **`src/infra/outbound/message-action-runner.ts`** -> AI Confidence: **99.39%**
119. **`src/infra/outbound/message.ts`** -> AI Confidence: **99.39%**
120. **`src/infra/session-cost-usage.ts`** -> AI Confidence: **99.39%**
121. **`src/media-understanding/apply.ts`** -> AI Confidence: **99.39%**
122. **`src/security/audit-extra.sync.ts`** -> AI Confidence: **99.39%**
123. **`src/security/audit.ts`** -> AI Confidence: **99.39%**
124. **`src/signal/monitor/event-handler.ts`** -> AI Confidence: **99.39%**
125. **`src/slack/monitor/events/interactions.ts`** -> AI Confidence: **99.39%**
126. **`src/slack/monitor/provider.ts`** -> AI Confidence: **99.39%**
127. **`src/telegram/bot.ts`** -> AI Confidence: **99.39%**
128. **`src/tui/tui-session-actions.ts`** -> AI Confidence: **99.39%**
129. **`src/web/accounts.ts`** -> AI Confidence: **99.39%**
130. **`extensions/diagnostics-otel/src/service.ts`** -> AI Confidence: **99.35%**
131. **`src/commands/agent.ts`** -> AI Confidence: **99.35%**
132. **`src/commands/agents.commands.identity.ts`** -> AI Confidence: **99.35%**
133. **`src/commands/channels/status.ts`** -> AI Confidence: **99.35%**
134. **`src/commands/models/scan.ts`** -> AI Confidence: **99.35%**
135. **`src/infra/outbound/targets.ts`** -> AI Confidence: **99.35%**
136. **`src/secrets/audit.ts`** -> AI Confidence: **99.35%**
137. **`src/slack/send.ts`** -> AI Confidence: **99.35%**
138. **`src/tts/tts.ts`** -> AI Confidence: **99.35%**
139. **`apps/macos/Sources/OpenClaw/WebChatSwiftUI.swift`** -> AI Confidence: **99.34%**
140. **`apps/android/app/src/main/java/ai/openclaw/android/InstallResultReceiver.kt`** -> AI Confidence: **99.34%**
141. **`apps/android/app/src/main/java/ai/openclaw/android/gateway/DeviceIdentityStore.kt`** -> AI Confidence: **99.34%**
142. **`apps/android/app/src/main/java/ai/openclaw/android/node/A2UIHandler.kt`** -> AI Confidence: **99.34%**
143. **`apps/android/app/src/main/java/ai/openclaw/android/node/DebugHandler.kt`** -> AI Confidence: **99.34%**
144. **`apps/android/app/src/main/java/ai/openclaw/android/node/NodeUtils.kt`** -> AI Confidence: **99.34%**
145. **`apps/android/app/src/main/java/ai/openclaw/android/node/NotificationsHandler.kt`** -> AI Confidence: **99.34%**
146. **`apps/android/app/src/main/java/ai/openclaw/android/ui/RootScreen.kt`** -> AI Confidence: **99.34%**
147. **`extensions/twitch/src/status.ts`** -> AI Confidence: **99.34%**
148. **`src/agents/memory-search.ts`** -> AI Confidence: **99.34%**
149. **`src/agents/sandbox/config.ts`** -> AI Confidence: **99.34%**
150. **`src/auto-reply/reply/queue/settings.ts`** -> AI Confidence: **99.34%**
151. **`src/commands/sandbox-explain.ts`** -> AI Confidence: **99.34%**
152. **`src/infra/skills-remote.ts`** -> AI Confidence: **99.34%**
153. **`src/plugins/update.ts`** -> AI Confidence: **99.34%**
154. **`src/tts/tts-core.ts`** -> AI Confidence: **99.34%**
155. **`apps/ios/Sources/Calendar/CalendarService.swift`** -> AI Confidence: **99.32%**
156. **`apps/ios/Sources/Motion/MotionService.swift`** -> AI Confidence: **99.32%**
157. **`apps/macos/Tests/OpenClawIPCTests/CommandResolverTests.swift`** -> AI Confidence: **99.32%**
158. **`apps/macos/Tests/OpenClawIPCTests/GatewayFrameDecodeTests.swift`** -> AI Confidence: **99.32%**
159. **`apps/android/app/src/main/java/ai/openclaw/android/DeviceNames.kt`** -> AI Confidence: **99.32%**
160. **`apps/android/app/src/main/java/ai/openclaw/android/node/JpegSizeLimiter.kt`** -> AI Confidence: **99.32%**
161. **`src/browser/chrome.profile-decoration.ts`** -> AI Confidence: **99.32%**
162. **`src/commands/agent/run-context.ts`** -> AI Confidence: **99.32%**
163. **`src/config/types.tools.ts`** -> AI Confidence: **99.32%**
164. **`src/discord/monitor/sender-identity.ts`** -> AI Confidence: **99.32%**
165. **`src/infra/heartbeat-visibility.ts`** -> AI Confidence: **99.32%**
166. **`src/telegram/probe.ts`** -> AI Confidence: **99.32%**
167. **`src/web/auto-reply/session-snapshot.ts`** -> AI Confidence: **99.32%**
168. **`apps/ios/Sources/Gateway/GatewayConnectionController.swift`** -> AI Confidence: **99.31%**
169. **`apps/ios/Sources/Model/NodeAppModel.swift`** -> AI Confidence: **99.31%**
170. **`apps/ios/Sources/OpenClawApp.swift`** -> AI Confidence: **99.31%**
171. **`apps/ios/Sources/Voice/TalkModeManager.swift`** -> AI Confidence: **99.31%**
172. **`apps/macos/Sources/OpenClaw/MenuBar.swift`** -> AI Confidence: **99.31%**
173. **`apps/macos/Sources/OpenClaw/NodePairingApprovalPrompter.swift`** -> AI Confidence: **99.31%**
174. **`apps/macos/Sources/OpenClaw/PermissionManager.swift`** -> AI Confidence: **99.31%**
175. **`apps/macos/Sources/OpenClaw/VoiceWakeSettings.swift`** -> AI Confidence: **99.31%**
176. **`apps/shared/OpenClawKit/Sources/OpenClawChatUI/ChatViewModel.swift`** -> AI Confidence: **99.31%**
177. **`extensions/acpx/src/runtime.ts`** -> AI Confidence: **99.31%**
178. **`extensions/bluebubbles/src/actions.ts`** -> AI Confidence: **99.31%**
179. **`extensions/bluebubbles/src/attachments.ts`** -> AI Confidence: **99.31%**
180. **`extensions/bluebubbles/src/channel.ts`** -> AI Confidence: **99.31%**
181. **`extensions/bluebubbles/src/chat.ts`** -> AI Confidence: **99.31%**
182. **`extensions/bluebubbles/src/monitor.ts`** -> AI Confidence: **99.31%**
183. **`extensions/bluebubbles/src/send.ts`** -> AI Confidence: **99.31%**
184. **`extensions/feishu/src/docx.ts`** -> AI Confidence: **99.31%**
185. **`extensions/feishu/src/media.ts`** -> AI Confidence: **99.31%**
186. **`extensions/feishu/src/monitor.ts`** -> AI Confidence: **99.31%**
187. **`extensions/feishu/src/reply-dispatcher.ts`** -> AI Confidence: **99.31%**
188. **`extensions/feishu/src/send.ts`** -> AI Confidence: **99.31%**
189. **`extensions/googlechat/src/channel.ts`** -> AI Confidence: **99.31%**
190. **`extensions/googlechat/src/monitor.ts`** -> AI Confidence: **99.31%**
191. **`extensions/irc/src/channel.ts`** -> AI Confidence: **99.31%**
192. **`extensions/irc/src/inbound.ts`** -> AI Confidence: **99.31%**
193. **`extensions/irc/src/send.ts`** -> AI Confidence: **99.31%**
194. **`extensions/matrix/src/channel.ts`** -> AI Confidence: **99.31%**
195. **`extensions/matrix/src/matrix/client/shared.ts`** -> AI Confidence: **99.31%**
196. **`extensions/matrix/src/matrix/monitor/index.ts`** -> AI Confidence: **99.31%**
197. **`extensions/matrix/src/matrix/send.ts`** -> AI Confidence: **99.31%**
198. **`extensions/matrix/src/matrix/send/client.ts`** -> AI Confidence: **99.31%**
199. **`extensions/mattermost/src/channel.ts`** -> AI Confidence: **99.31%**
200. **`extensions/mattermost/src/mattermost/monitor.ts`** -> AI Confidence: **99.31%**
201. **`extensions/msteams/src/channel.ts`** -> AI Confidence: **99.31%**
202. **`extensions/msteams/src/messenger.ts`** -> AI Confidence: **99.31%**
203. **`extensions/msteams/src/monitor.ts`** -> AI Confidence: **99.31%**
204. **`extensions/msteams/src/send.ts`** -> AI Confidence: **99.31%**
205. **`extensions/nextcloud-talk/src/channel.ts`** -> AI Confidence: **99.31%**
206. **`extensions/nextcloud-talk/src/inbound.ts`** -> AI Confidence: **99.31%**
207. **`extensions/nextcloud-talk/src/monitor.ts`** -> AI Confidence: **99.31%**
208. **`extensions/nostr/src/nostr-profile-http.ts`** -> AI Confidence: **99.31%**
209. **`extensions/synology-chat/src/channel.ts`** -> AI Confidence: **99.31%**
210. **`extensions/tlon/src/channel.ts`** -> AI Confidence: **99.31%**
211. **`extensions/twitch/src/plugin.ts`** -> AI Confidence: **99.31%**
212. **`extensions/voice-call/src/cli.ts`** -> AI Confidence: **99.31%**
213. **`extensions/voice-call/src/manager/events.ts`** -> AI Confidence: **99.31%**
214. **`extensions/voice-call/src/manager/outbound.ts`** -> AI Confidence: **99.31%**
215. **`extensions/voice-call/src/providers/plivo.ts`** -> AI Confidence: **99.31%**
216. **`extensions/voice-call/src/providers/twilio.ts`** -> AI Confidence: **99.31%**
217. **`extensions/voice-call/src/runtime.ts`** -> AI Confidence: **99.31%**
218. **`extensions/voice-call/src/webhook.ts`** -> AI Confidence: **99.31%**
219. **`extensions/zalo/src/channel.ts`** -> AI Confidence: **99.31%**
220. **`extensions/zalo/src/monitor.ts`** -> AI Confidence: **99.31%**
221. **`extensions/zalouser/src/channel.ts`** -> AI Confidence: **99.31%**
222. **`src/acp/client.ts`** -> AI Confidence: **99.31%**
223. **`src/acp/control-plane/manager.core.ts`** -> AI Confidence: **99.31%**
224. **`src/acp/control-plane/manager.identity-reconcile.ts`** -> AI Confidence: **99.31%**
225. **`src/acp/runtime/session-meta.ts`** -> AI Confidence: **99.31%**
226. **`src/acp/translator.ts`** -> AI Confidence: **99.31%**
227. **`src/agents/acp-spawn.ts`** -> AI Confidence: **99.31%**
228. **`src/agents/agent-scope.ts`** -> AI Confidence: **99.31%**
229. **`src/agents/anthropic-payload-log.ts`** -> AI Confidence: **99.31%**
230. **`src/agents/apply-patch.ts`** -> AI Confidence: **99.31%**
231. **`src/agents/auth-profiles/oauth.ts`** -> AI Confidence: **99.31%**
232. **`src/agents/auth-profiles/store.ts`** -> AI Confidence: **99.31%**
233. **`src/agents/bash-tools.exec-runtime.ts`** -> AI Confidence: **99.31%**
234. **`src/agents/bash-tools.process.ts`** -> AI Confidence: **99.31%**
235. **`src/agents/cache-trace.ts`** -> AI Confidence: **99.31%**
236. **`src/agents/cli-credentials.ts`** -> AI Confidence: **99.31%**
237. **`src/agents/cli-runner/helpers.ts`** -> AI Confidence: **99.31%**
238. **`src/agents/model-auth.ts`** -> AI Confidence: **99.31%**
239. **`src/agents/model-fallback.ts`** -> AI Confidence: **99.31%**
240. **`src/agents/model-selection.ts`** -> AI Confidence: **99.31%**
241. **`src/agents/models-config.providers.ts`** -> AI Confidence: **99.31%**
242. **`src/agents/pi-embedded-helpers/bootstrap.ts`** -> AI Confidence: **99.31%**
243. **`src/agents/pi-embedded-runner/compact.ts`** -> AI Confidence: **99.31%**
244. **`src/agents/pi-embedded-runner/extensions.ts`** -> AI Confidence: **99.31%**
245. **`src/agents/pi-embedded-runner/google.ts`** -> AI Confidence: **99.31%**
246. **`src/agents/pi-embedded-runner/model.ts`** -> AI Confidence: **99.31%**
247. **`src/agents/pi-embedded-runner/run/attempt.ts`** -> AI Confidence: **99.31%**
248. **`src/agents/pi-embedded-runner/run/images.ts`** -> AI Confidence: **99.31%**
249. **`src/agents/pi-embedded-runner/run/params.ts`** -> AI Confidence: **99.31%**
250. **`src/agents/pi-embedded-runner/system-prompt.ts`** -> AI Confidence: **99.31%**
251. **`src/agents/pi-embedded-subscribe.tools.ts`** -> AI Confidence: **99.31%**
252. **`src/agents/pi-extensions/compaction-safeguard.ts`** -> AI Confidence: **99.31%**
253. **`src/agents/pi-tool-definition-adapter.ts`** -> AI Confidence: **99.31%**
254. **`src/agents/pi-tools.before-tool-call.ts`** -> AI Confidence: **99.31%**
255. **`src/agents/pi-tools.read.ts`** -> AI Confidence: **99.31%**
256. **`src/agents/sandbox/browser.ts`** -> AI Confidence: **99.31%**
257. **`src/agents/sandbox/context.ts`** -> AI Confidence: **99.31%**
258. **`src/agents/sandbox/docker.ts`** -> AI Confidence: **99.31%**
259. **`src/agents/sandbox/fs-bridge.ts`** -> AI Confidence: **99.31%**
260. **`src/agents/sandbox/runtime-status.ts`** -> AI Confidence: **99.31%**
261. **`src/agents/session-tool-result-guard.ts`** -> AI Confidence: **99.31%**
262. **`src/agents/skills-install-download.ts`** -> AI Confidence: **99.31%**
263. **`src/agents/skills-install.ts`** -> AI Confidence: **99.31%**
264. **`src/agents/skills-status.ts`** -> AI Confidence: **99.31%**
265. **`src/agents/skills/env-overrides.ts`** -> AI Confidence: **99.31%**
266. **`src/agents/skills/refresh.ts`** -> AI Confidence: **99.31%**
267. **`src/agents/skills/workspace.ts`** -> AI Confidence: **99.31%**
268. **`src/agents/subagent-announce.ts`** -> AI Confidence: **99.31%**
269. **`src/agents/subagent-registry.ts`** -> AI Confidence: **99.31%**
270. **`src/agents/tools/browser-tool.ts`** -> AI Confidence: **99.31%**
271. **`src/agents/tools/canvas-tool.ts`** -> AI Confidence: **99.31%**
272. **`src/agents/tools/discord-actions-messaging.ts`** -> AI Confidence: **99.31%**
273. **`src/agents/tools/gateway-tool.ts`** -> AI Confidence: **99.31%**
274. **`src/agents/tools/image-tool.ts`** -> AI Confidence: **99.31%**
275. **`src/agents/tools/memory-tool.ts`** -> AI Confidence: **99.31%**
276. **`src/agents/tools/message-tool.ts`** -> AI Confidence: **99.31%**
277. **`src/agents/tools/nodes-tool.ts`** -> AI Confidence: **99.31%**
278. **`src/agents/tools/session-status-tool.ts`** -> AI Confidence: **99.31%**
279. **`src/agents/tools/sessions-history-tool.ts`** -> AI Confidence: **99.31%**
280. **`src/agents/tools/sessions-send-tool.a2a.ts`** -> AI Confidence: **99.31%**
281. **`src/agents/tools/sessions-send-tool.ts`** -> AI Confidence: **99.31%**
282. **`src/agents/tools/slack-actions.ts`** -> AI Confidence: **99.31%**
283. **`src/agents/tools/subagents-tool.ts`** -> AI Confidence: **99.31%**
284. **`src/agents/tools/web-fetch.ts`** -> AI Confidence: **99.31%**
285. **`src/agents/tools/web-search.ts`** -> AI Confidence: **99.31%**
286. **`src/agents/workspace-run.ts`** -> AI Confidence: **99.31%**
287. **`src/auto-reply/chunk.ts`** -> AI Confidence: **99.31%**
288. **`src/auto-reply/commands-registry.ts`** -> AI Confidence: **99.31%**
289. **`src/auto-reply/reply.triggers.trigger-handling.filters-usage-summary-current-model-provider.cases.ts`** -> AI Confidence: **99.31%**
290. **`src/auto-reply/reply/abort.ts`** -> AI Confidence: **99.31%**
291. **`src/auto-reply/reply/agent-runner-execution.ts`** -> AI Confidence: **99.31%**
292. **`src/auto-reply/reply/agent-runner-memory.ts`** -> AI Confidence: **99.31%**
293. **`src/auto-reply/reply/agent-runner-payloads.ts`** -> AI Confidence: **99.31%**
294. **`src/auto-reply/reply/agent-runner-utils.ts`** -> AI Confidence: **99.31%**
295. **`src/auto-reply/reply/agent-runner.ts`** -> AI Confidence: **99.31%**
296. **`src/auto-reply/reply/bash-command.ts`** -> AI Confidence: **99.31%**
297. **`src/auto-reply/reply/commands-acp/diagnostics.ts`** -> AI Confidence: **99.31%**
298. **`src/auto-reply/reply/commands-acp/lifecycle.ts`** -> AI Confidence: **99.31%**
299. **`src/auto-reply/reply/commands-acp/shared.ts`** -> AI Confidence: **99.31%**
300. **`src/auto-reply/reply/commands-compact.ts`** -> AI Confidence: **99.31%**
301. **`src/auto-reply/reply/commands-config.ts`** -> AI Confidence: **99.31%**
302. **`src/auto-reply/reply/commands-core.ts`** -> AI Confidence: **99.31%**
303. **`src/auto-reply/reply/commands-models.ts`** -> AI Confidence: **99.31%**
304. **`src/auto-reply/reply/commands-session-abort.ts`** -> AI Confidence: **99.31%**
305. **`src/auto-reply/reply/commands-session.ts`** -> AI Confidence: **99.31%**
306. **`src/auto-reply/reply/commands-status.ts`** -> AI Confidence: **99.31%**
307. **`src/auto-reply/reply/commands-subagents/action-send.ts`** -> AI Confidence: **99.31%**
308. **`src/auto-reply/reply/commands-subagents/shared.ts`** -> AI Confidence: **99.31%**
309. **`src/auto-reply/reply/commands-system-prompt.ts`** -> AI Confidence: **99.31%**
310. **`src/auto-reply/reply/directive-handling.auth.ts`** -> AI Confidence: **99.31%**
311. **`src/auto-reply/reply/directive-handling.parse.ts`** -> AI Confidence: **99.31%**
312. **`src/auto-reply/reply/dispatch-acp.ts`** -> AI Confidence: **99.31%**
313. **`src/auto-reply/reply/dispatch-from-config.ts`** -> AI Confidence: **99.31%**
314. **`src/auto-reply/reply/get-reply-directives-apply.ts`** -> AI Confidence: **99.31%**
315. **`src/auto-reply/reply/get-reply-inline-actions.ts`** -> AI Confidence: **99.31%**
316. **`src/auto-reply/reply/get-reply.ts`** -> AI Confidence: **99.31%**
317. **`src/auto-reply/reply/memory-flush.ts`** -> AI Confidence: **99.31%**
318. **`src/auto-reply/reply/model-selection.ts`** -> AI Confidence: **99.31%**
319. **`src/auto-reply/reply/reply-elevated.ts`** -> AI Confidence: **99.31%**
320. **`src/auto-reply/reply/reply-payloads.ts`** -> AI Confidence: **99.31%**
321. **`src/auto-reply/reply/session-reset-model.ts`** -> AI Confidence: **99.31%**
322. **`src/auto-reply/reply/session-updates.ts`** -> AI Confidence: **99.31%**
323. **`src/auto-reply/reply/stage-sandbox-media.ts`** -> AI Confidence: **99.31%**
324. **`src/browser/bridge-server.ts`** -> AI Confidence: **99.31%**
325. **`src/browser/chrome.ts`** -> AI Confidence: **99.31%**
326. **`src/browser/client-fetch.ts`** -> AI Confidence: **99.31%**
327. **`src/browser/extension-relay.ts`** -> AI Confidence: **99.31%**
328. **`src/browser/profiles-service.ts`** -> AI Confidence: **99.31%**
329. **`src/browser/pw-session.ts`** -> AI Confidence: **99.31%**
330. **`src/browser/routes/agent.act.ts`** -> AI Confidence: **99.31%**
331. **`src/browser/routes/agent.snapshot.ts`** -> AI Confidence: **99.31%**
332. **`src/channels/dock.ts`** -> AI Confidence: **99.31%**
333. **`src/channels/plugins/actions/telegram.ts`** -> AI Confidence: **99.31%**
334. **`src/channels/plugins/catalog.ts`** -> AI Confidence: **99.31%**
335. **`src/channels/plugins/directory-config.ts`** -> AI Confidence: **99.31%**
336. **`src/channels/plugins/group-mentions.ts`** -> AI Confidence: **99.31%**
337. **`src/channels/plugins/onboarding/discord.ts`** -> AI Confidence: **99.31%**
338. **`src/channels/plugins/onboarding/helpers.ts`** -> AI Confidence: **99.31%**
339. **`src/channels/plugins/onboarding/signal.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Swabble/Sources/SwabbleCore/Config/Config.swift` -> **100.0%** Exposure
- `Swabble/Sources/SwabbleCore/Speech/SpeechPipeline.swift` -> **100.0%** Exposure
- `Swabble/Sources/SwabbleKit/WakeWordGate.swift` -> **100.0%** Exposure
- `Swabble/Sources/swabble/main.swift` -> **100.0%** Exposure
- `apps/ios/ShareExtension/ShareViewController.swift` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `apps/macos/Tests/OpenClawIPCTests/GatewayEndpointStoreTests.swift` -> **100.0%** Exposure
- `setup-podman.sh` -> **100.0%** Exposure
- `extensions/voice-call/src/types.ts` -> **100.0%** Exposure
- `src/cli/browser-cli-actions-input/register.files-downloads.ts` -> **100.0%** Exposure
- `src/cli/hooks-cli.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `Swabble/Sources/SwabbleCore/Config/Config.swift` -> **100.0%** Exposure
- `Swabble/Sources/SwabbleCore/Support/AttributedString+Sentences.swift` -> **100.0%** Exposure
- `Swabble/Sources/SwabbleCore/Support/TranscriptsStore.swift` -> **100.0%** Exposure
- `Swabble/Sources/SwabbleKit/WakeWordGate.swift` -> **100.0%** Exposure
- `apps/ios/ShareExtension/ShareViewController.swift` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `33` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4525` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `apps/shared/OpenClawKit/Sources/OpenClawKit/CanvasCommandParams.swift` (SWIFT) -> Cumulative Risk: **1025.33**
- **Archetype:** `file_cluster_4` (Distance: 13.156 IQR)
- **Magnitude:** 173.16 | **LOC:** 77 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `init` (Impact: 28.6), `init` (Impact: 17.1), `encode` (Impact: 13.6)

### 2. `apps/macos/Sources/OpenClaw/CronJobsStore.swift` (SWIFT) -> Cumulative Risk: **984.23**
- **Archetype:** `file_cluster_4` (Distance: 12.211 IQR)
- **Magnitude:** 538.86 | **LOC:** 201 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Documentation (99.9995%)
- **Heaviest Functions:** `handle` (Impact: 110.7), `refreshJobs` (Impact: 48.7), `start` (Impact: 44.0)

### 3. `apps/macos/Sources/OpenClaw/ExecApprovalsSocket.swift` (SWIFT) -> Cumulative Risk: **952.07**
- **Archetype:** `file_cluster_4` (Distance: 12.127 IQR)
- **Magnitude:** 1331.44 | **LOC:** 788 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle` (Impact: 172.2), `handleClient` (Impact: 140.0), `buildAccessoryView` (Impact: 111.7)

### 4. `apps/macos/Sources/OpenClaw/ExecApprovals.swift` (SWIFT) -> Cumulative Risk: **949.21**
- **Archetype:** `file_cluster_8` (Distance: 13.199 IQR)
- **Magnitude:** 1844.12 | **LOC:** 795 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9998%)
- **Heaviest Functions:** `resolve` (Impact: 221.6), `normalizeIncoming` (Impact: 155.9), `mergeAgents` (Impact: 79.4)

### 5. `apps/macos/Sources/OpenClaw/MenuBar.swift` (SWIFT) -> Cumulative Risk: **948.72**
- **Archetype:** `file_cluster_4` (Distance: 11.939 IQR)
- **Magnitude:** 539.72 | **LOC:** 475 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `applicationDidFinishLaunching` (Impact: 46.5), `updater` (Impact: 45.5), `isDeveloperIDSigned` (Impact: 34.0)

### 6. `apps/shared/OpenClawKit/Sources/OpenClawKit/TalkSystemSpeechSynthesizer.swift` (SWIFT) -> Cumulative Risk: **947.26**
- **Archetype:** `file_cluster_4` (Distance: 11.083 IQR)
- **Magnitude:** 287.2 | **LOC:** 117 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Documentation (99.9942%)
- **Heaviest Functions:** `speak` (Impact: 178.9), `finishCurrent` (Impact: 27.3), `handleFinish` (Impact: 15.3)

### 7. `src/agents/sandbox/fs-bridge.ts` (TYPESCRIPT) -> Cumulative Risk: **940.94**
- **Archetype:** `file_cluster_4` (Distance: 11.751 IQR)
- **Magnitude:** 39.04 | **LOC:** 367 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `assertPathSafety` (Impact: 40.2), `coerceStatType` (Impact: 10.7), `resolveMountByContainerPath` (Impact: 9.4)

### 8. `apps/macos/Sources/OpenClaw/NodesStore.swift` (SWIFT) -> Cumulative Risk: **928.48**
- **Archetype:** `file_cluster_4` (Distance: 12.003 IQR)
- **Magnitude:** 178.06 | **LOC:** 111 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.8104%)
- **Heaviest Functions:** `refresh` (Impact: 48.1), `start` (Impact: 44.0), `isCancelled` (Impact: 17.1)

### 9. `apps/macos/Sources/OpenClaw/OnboardingWizard.swift` (SWIFT) -> Cumulative Risk: **923.05**
- **Archetype:** `file_cluster_17` (Distance: 12.04 IQR)
- **Magnitude:** 655.96 | **LOC:** 420 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9989%)
- **Heaviest Functions:** `submit` (Impact: 87.9), `startIfNeeded` (Impact: 69.4), `submit` (Impact: 66.3)

### 10. `ui/src/ui/gateway.ts` (TYPESCRIPT) -> Cumulative Risk: **918.85**
- **Archetype:** `file_cluster_4` (Distance: 14.327 IQR)
- **Magnitude:** 67.74 | **LOC:** 361 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sendConnect` (Impact: 189.9), `handleMessage` (Impact: 118.8), `reject` (Impact: 26.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_4` (Drift: 12.642 IQR)
- **Top Global Matches:** file_cluster_4: 12.642, file_cluster_8: 12.806, file_cluster_0: 12.988
- **Magnitude:** 3557.02 | **LOC:** 2731 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (83.4451%), Tech Debt (55.1431%)
**Top Internal Functions/Classes:**
  * `handleCanvasInvoke` (Impact: 668.8 | O(N^6) | DB: 9)
  * `startVoiceWakeSync` (Impact: 159.2 | O(N^6) | DB: 3)
    * *Intent:* // If talk is enabled, voice wake should not grab the mic.
  * `refreshShareRouteFromGateway` (Impact: 154.4 | O(N^6) | DB: 12)
  * `init` (Impact: 134.0 | O(N^6) | DB: 9)
  * `handleLocationInvoke` (Impact: 130.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 341`, `args: 93`, `func_start: 87`, `class_start: 22`
* *Risk/State:* `state_mutation: 265`, `orphaned_logic: 39`
* *Architecture:* `io: 8`, `api: 53`, `concurrency: 225`, `import: 9`
* *Defense:* `safety: 126`, `doc: 2`, `sync_locks: 22`, `immutability_locks: 241`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Security, os, OpenClawChatUI, UIKit, OpenClawProtocol, Observation, OpenClawKit, UserNotifications...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/TalkModeRuntime.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.015 IQR)
- **Top Global Matches:** file_cluster_4: 12.015, file_cluster_8: 12.146, file_cluster_0: 12.454
- **Magnitude:** 2808.28 | **LOC:** 1052 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (87.0303%), Tech Debt (9.23%)
**Top Internal Functions/Classes:**
  * `fetchTalkConfig` (Impact: 429.8 | O(N^5))
  * `preparePlaybackInput` (Impact: 255.9 | O(N^6))
  * `playElevenLabs` (Impact: 220.2 | O(N^6))
  * `startRecognition` (Impact: 115.6 | O(N^4) | DB: 1)
  * `sendAndSpeak` (Impact: 110.0 | O(N^5))
    * *Intent:* // MARK: - Gateway + TTS
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 236`, `args: 56`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `state_mutation: 103`, `orphaned_logic: 2`
* *Architecture:* `api: 39`, `concurrency: 157`, `import: 6`
* *Defense:* `safety: 92`, `sync_locks: 27`, `immutability_locks: 200`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawChatUI, OSLog, OpenClawKit, Speech, Foundation, AVFoundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/MenuSessionsInjector.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.493, file_cluster_4: 11.751, file_cluster_0: 11.885
- **Magnitude:** 2534.32 | **LOC:** 1241 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (54.6335%), Tech Debt (13.5938%)
**Top Internal Functions/Classes:**
  * `inject` (Impact: 271.5 | O(N^6) | DB: 3)
  * `menuWillOpen` (Impact: 169.4 | O(2^N))
  * `injectNodes` (Impact: 137.8 | O(N^5) | DB: 1)
  * `resetSession` (Impact: 123.9 | O(2^N))
  * `gatewayEntry` (Impact: 117.9 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 191`, `args: 62`, `func_start: 57`, `class_start: 7`
* *Risk/State:* `state_mutation: 97`, `orphaned_logic: 7`
* *Architecture:* `api: 8`, `concurrency: 85`, `import: 4`
* *Defense:* `safety: 95`, `sync_locks: 12`, `immutability_locks: 178`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AppKit, Foundation, SwiftUI, Observation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/NodeMode/MacNodeRuntime.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.758 IQR)
- **Top Global Matches:** file_cluster_8: 11.758, file_cluster_4: 11.78, file_cluster_17: 12.128
- **Magnitude:** 2491.16 | **LOC:** 1003 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (84.9608%), Tech Debt (11.1693%)
**Top Internal Functions/Classes:**
  * `handleCanvasInvoke` (Impact: 325.6 | O(N^5) | DB: 6)
  * `handleCameraInvoke` (Impact: 291.6 | O(N^5) | DB: 14)
  * `handleSystemExecApprovalsSet` (Impact: 183.8 | O(N^5) | DB: 3)
  * `handleInvoke` (Impact: 176.8 | O(N^5))
  * `handleLocationInvoke` (Impact: 157.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 216`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `state_mutation: 139`, `orphaned_logic: 4`
* *Architecture:* `io: 11`, `concurrency: 122`, `import: 4`
* *Defense:* `safety: 68`, `sync_locks: 6`, `immutability_locks: 155`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawKit, AppKit, Foundation, OpenClawIPC
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/GatewayConnection.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.934 IQR)
- **Top Global Matches:** file_cluster_4: 11.934, file_cluster_8: 12.22, file_cluster_17: 12.56
- **Magnitude:** 2206.88 | **LOC:** 743 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (89.7508%), Tech Debt (91.603%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 578.6 | O(2^N) | DB: 2)
    * *Intent:* // MARK: - Low-level request
  * `canonicalizeSessionKey` (Impact: 108.2 | O(N^5))
  * `sessionsPreview` (Impact: 72.6 | O(2^N) | DB: 1)
    * *Intent:* // MARK: - Sessions
  * `skillsUpdate` (Impact: 72.3 | O(2^N) | DB: 1)
  * `sendAgent` (Impact: 61.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 147`, `args: 56`, `func_start: 53`, `class_start: 11`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 70`, `duplicate_logic: 8`, `orphaned_logic: 11`
* *Architecture:* `api: 1`, `concurrency: 205`, `import: 5`
* *Defense:* `safety: 62`, `doc: 5`, `sync_locks: 3`, `immutability_locks: 96`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawChatUI, OSLog, OpenClawProtocol, OpenClawKit, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/voice/TalkModeManager.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.797 IQR)
- **Top Global Matches:** file_cluster_8: 13.797, file_cluster_4: 13.83, file_cluster_13: 13.881
- **Magnitude:** 2008.88 | **LOC:** 1318 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (9.9357%)
**Top Internal Functions/Classes:**
  * `streamPcm` (Impact: 124.8 | O(N^4) | DB: 2)
  * `playAssistant` (Impact: 124.7 | O(N^3) | DB: 27)
  * `ensureSystemTts` (Impact: 86.2 | O(N^3) | DB: 7)
  * `reloadConfig` (Impact: 65.4 | O(N^2) | DB: 11)
  * `start` (Impact: 58.9 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `args: 72`, `func_start: 65`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 366`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `concurrency: 185`, `import: 42`
* *Defense:* `safety: 76`, `immutability_locks: 200`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kotlinx.coroutines.delay, kotlinx.coroutines.flow.MutableStateFlow, kotlinx.coroutines.Job, kotlinx.serialization.json.JsonElement, android.media.AudioAttributes, android.util.Log, android.speech.tts.TextToSpeech, android.content.Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Gateway/GatewayConnectionController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.145 IQR)
- **Top Global Matches:** file_cluster_8: 12.145, file_cluster_4: 12.256, file_cluster_17: 12.311
- **Magnitude:** 1867.0 | **LOC:** 1056 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (58.4056%), Tech Debt (70.0977%)
**Top Internal Functions/Classes:**
  * `maybeAutoConnect` (Impact: 270.6 | O(N^5) | DB: 3)
  * `resolveBonjourServiceToHostPort` (Impact: 232.3 | O(N^6) | DB: 5)
  * `connectDiscoveredGateway` (Impact: 131.7 | O(N^4) | DB: 3)
  * `connectManual` (Impact: 82.3 | O(N^4) | DB: 3)
  * `isLoopbackHost` (Impact: 54.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 158`, `args: 79`, `func_start: 68`, `class_start: 5`
* *Risk/State:* `state_mutation: 142`, `duplicate_logic: 2`, `orphaned_logic: 25`
* *Architecture:* `io: 19`, `concurrency: 61`, `import: 17`
* *Defense:* `safety: 58`, `doc: 3`, `sync_locks: 7`, `immutability_locks: 161`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Photos, Security, CoreMotion, CoreLocation, UIKit, Network, Observation, OpenClawKit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ExecApprovals.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.199 IQR)
- **Top Global Matches:** file_cluster_8: 13.199, file_cluster_4: 13.279, file_cluster_17: 13.318
- **Magnitude:** 1844.12 | **LOC:** 795 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (90.2337%), Tech Debt (63.9369%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 221.6 | O(N^4))
  * `normalizeIncoming` (Impact: 155.9 | O(N^5) | DB: 3)
  * `mergeAgents` (Impact: 79.4 | O(N^4) | DB: 4)
  * `migrateLegacyPattern` (Impact: 75.4 | O(N^5))
  * `recordAllowlistUse` (Impact: 75.0 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 155`, `args: 49`, `func_start: 42`, `class_start: 20`
* *Risk/State:* `state_mutation: 236`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 9`, `api: 2`, `concurrency: 35`, `import: 4`
* *Defense:* `safety: 80`, `immutability_locks: 146`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptoKit, Security, OSLog, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/auto-reply/reply/export-html/template.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.518 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.373 IQR)
- **Top Global Matches:** file_cluster_8: 12.518, file_cluster_17: 12.575, file_cluster_4: 12.921
- **Magnitude:** 1599.92 | **LOC:** 1853 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (48.6168%), Tech Debt (13.0892%)
**Top Internal Functions/Classes:**
  * `renderToolCall` (Impact: 419.1 | O(N^5) | DB: 23)
  * `renderEntry` (Impact: 170.4 | O(N^4) | DB: 8)
  * `filterNodes` (Impact: 90.1 | O(N^3) | DB: 1)
  * `computeStats` (Impact: 86.2 | O(N^3) | DB: 3)
  * `getTreeNodeDisplayHtml` (Impact: 83.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 242`, `args: 57`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 232`, `orphaned_logic: 6`
* *Architecture:* `io: 15`, `concurrency: 14`
* *Defense:* `safety: 120`, `doc: 15`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/shared/OpenClawKit/Sources/OpenClawChatUI/ChatViewModel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.318 IQR)
- **Top Global Matches:** file_cluster_4: 12.318, file_cluster_17: 12.504, file_cluster_8: 12.559
- **Magnitude:** 1536.14 | **LOC:** 686 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (95.1352%), Tech Debt (34.1312%)
**Top Internal Functions/Classes:**
  * `handleAgentEvent` (Impact: 182.6 | O(N^5))
  * `handleChatEvent` (Impact: 108.4 | O(N^4))
  * `messageIdentityKey` (Impact: 99.6 | O(N^3))
  * `bootstrap` (Impact: 96.9 | O(2^N))
    * *Intent:* // MARK: - Internals
  * `performSend` (Impact: 82.2 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 121`, `args: 38`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 130`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 91`, `import: 7`
* *Defense:* `safety: 58`, `sync_locks: 5`, `immutability_locks: 80`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UIKit, OSLog, Observation, OpenClawKit, UniformTypeIdentifiers, AppKit, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/AppState.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.063 IQR)
- **Top Global Matches:** file_cluster_4: 12.063, file_cluster_8: 12.441, file_cluster_0: 12.592
- **Magnitude:** 1470.32 | **LOC:** 732 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (91.7278%), Tech Debt (25.4701%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 279.0 | O(N^4) | DB: 72)
  * `updatedRemoteGatewayConfig` (Impact: 240.4 | O(N^5) | DB: 2)
  * `applyConfigOverrides` (Impact: 155.3 | O(N^4))
  * `syncGatewayConfigIfNeeded` (Impact: 148.5 | O(N^5) | DB: 3)
  * `updateRemoteTarget` (Impact: 52.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 113`, `args: 25`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `state_mutation: 121`, `orphaned_logic: 9`
* *Architecture:* `io: 50`, `concurrency: 158`, `import: 5`
* *Defense:* `safety: 61`, `doc: 2`, `sync_locks: 8`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, ServiceManagement, AppKit, Foundation, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/GatewayEndpointStore.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.029 IQR)
- **Top Global Matches:** file_cluster_8: 11.029, file_cluster_4: 11.359, file_cluster_0: 11.476
- **Magnitude:** 1400.98 | **LOC:** 729 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (40.1636%), Tech Debt (27.0127%)
**Top Internal Functions/Classes:**
  * `resolveGatewayPassword` (Impact: 149.9 | O(N^5))
  * `ensureRemoteConfig` (Impact: 123.3 | O(N^5))
  * `dashboardURL` (Impact: 117.4 | O(N^4) | DB: 4)
  * `resolveGatewayToken` (Impact: 89.2 | O(N^5))
  * `setMode` (Impact: 88.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 96`, `args: 30`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `api: 12`, `concurrency: 61`, `import: 3`
* *Defense:* `safety: 86`, `doc: 6`, `sync_locks: 3`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, OSLog, ConcurrencyExtras
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ExecApprovalsSocket.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.127 IQR)
- **Top Global Matches:** file_cluster_4: 12.127, file_cluster_8: 12.151, file_cluster_0: 12.356
- **Magnitude:** 1331.44 | **LOC:** 788 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (84.4457%), Tech Debt (63.838%)
**Top Internal Functions/Classes:**
  * `handle` (Impact: 172.2 | O(N^5) | DB: 2)
  * `handleClient` (Impact: 140.0 | O(N^5) | DB: 7)
  * `buildAccessoryView` (Impact: 111.7 | O(N^3))
  * `requestDecision` (Impact: 71.8 | O(N^6))
  * `requestDecisionSync` (Impact: 62.8 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 147`, `args: 40`, `func_start: 28`, `class_start: 14`
* *Risk/State:* `state_mutation: 198`, `duplicate_logic: 8`, `orphaned_logic: 2`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 74`, `import: 6`
* *Defense:* `safety: 33`, `sync_locks: 5`, `immutability_locks: 110`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OSLog, OpenClawKit, Darwin, Foundation, AppKit, CryptoKit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/NodePairingApprovalPrompter.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.57 IQR)
- **Top Global Matches:** file_cluster_4: 11.57, file_cluster_8: 11.752, file_cluster_13: 11.952
- **Magnitude:** 1330.74 | **LOC:** 683 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (85.9449%), Tech Debt (8.8467%)
**Top Internal Functions/Classes:**
  * `handle` (Impact: 120.5 | O(N^6))
  * `loadPendingRequestsFromGateway` (Impact: 86.4 | O(N^6) | DB: 3)
  * `resolveSSHTarget` (Impact: 79.7 | O(N^4))
  * `presentAlert` (Impact: 63.7 | O(N^4))
  * `apply` (Impact: 62.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 132`, `args: 31`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 114`, `import: 9`
* *Defense:* `safety: 42`, `sync_locks: 7`, `immutability_locks: 113`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawDiscovery, OSLog, OpenClawProtocol, Observation, OpenClawKit, OpenClawIPC, UserNotifications, AppKit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/VoiceWakeTester.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.666 IQR)
- **Top Global Matches:** file_cluster_4: 11.666, file_cluster_8: 11.749, file_cluster_0: 11.886
- **Magnitude:** 1322.88 | **LOC:** 482 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (80.377%), Tech Debt (33.678%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 529.6 | O(2^N) | DB: 2)
  * `holdUntilSilence` (Impact: 103.0 | O(N^5))
  * `handleResult` (Impact: 82.2 | O(N^4))
  * `maybeLogDebug` (Impact: 75.0 | O(N^4))
  * `scheduleSilenceCheck` (Impact: 70.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 74`, `args: 25`, `func_start: 17`, `class_start: 5`
* *Risk/State:* `state_mutation: 64`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `concurrency: 66`, `import: 4`
* *Defense:* `safety: 37`, `sync_locks: 10`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, Speech, SwabbleKit, AVFoundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/shared/OpenClawKit/Sources/OpenClawKit/GatewayNodeSession.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.141 IQR)
- **Top Global Matches:** file_cluster_4: 12.141, file_cluster_0: 12.568, file_cluster_8: 12.662
- **Magnitude:** 1309.24 | **LOC:** 443 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (22.1625%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 309.0 | O(2^N))
  * `invokeWithTimeout` (Impact: 143.8 | O(N^6) | DB: 4)
  * `handleEvent` (Impact: 68.2 | O(N^4))
  * `decodeParamsJSON` (Impact: 68.2 | O(N^4))
  * `handlePush` (Impact: 68.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 87`, `args: 33`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `state_mutation: 81`, `orphaned_logic: 5`
* *Architecture:* `api: 24`, `concurrency: 158`, `import: 3`
* *Defense:* `safety: 40`, `sync_locks: 8`, `immutability_locks: 73`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, OpenClawProtocol, OSLog
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClawMacCLI/WizardCommand.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.451 IQR)
- **Top Global Matches:** file_cluster_8: 11.451, file_cluster_17: 11.729, file_cluster_4: 11.776
- **Magnitude:** 1307.44 | **LOC:** 538 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (62.5528%), Tech Debt (9.1223%)
**Top Internal Functions/Classes:**
  * `runWizard` (Impact: 215.8 | O(N^6) | DB: 3)
  * `sendConnect` (Impact: 139.3 | O(N^5) | DB: 1)
  * `promptAnswer` (Impact: 116.0 | O(N^2))
  * `runWizardCommand` (Impact: 96.0 | O(N^6))
  * `promptMultiSelect` (Impact: 90.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 81`, `args: 21`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `concurrency: 32`, `import: 4`
* *Defense:* `safety: 51`, `immutability_locks: 117`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawKit, Foundation, OpenClawProtocol, Darwin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClawDiscovery/GatewayDiscoveryModel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.543 IQR)
- **Top Global Matches:** file_cluster_4: 12.543, file_cluster_8: 12.763, file_cluster_17: 12.769
- **Magnitude:** 1304.42 | **LOC:** 683 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (89.2266%), Tech Debt (66.5504%)
**Top Internal Functions/Classes:**
  * `updateGateways` (Impact: 123.9 | O(N^5))
  * `start` (Impact: 95.2 | O(2^N))
  * `scheduleWideAreaFallback` (Impact: 92.5 | O(N^6) | DB: 1)
  * `ensureServiceResolution` (Impact: 75.4 | O(N^5))
  * `parseGatewayTXT` (Impact: 65.6 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 138`, `args: 45`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 159`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 36`, `concurrency: 86`, `import: 5`
* *Defense:* `safety: 53`, `sync_locks: 8`, `immutability_locks: 122`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OSLog, Network, Observation, OpenClawKit, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClawIPC/IPC.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.196 IQR)
- **Top Global Matches:** file_cluster_8: 11.196, file_cluster_4: 11.344, file_cluster_7: 11.512
- **Magnitude:** 1240.06 | **LOC:** 417 | **CtrlFlow:** 90.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (36.7293%), Tech Debt (62.3165%)
**Top Internal Functions/Classes:**
  * `encode` (Impact: 729.5 | O(2^N) | DB: 1)
  * `init` (Impact: 365.3 | O(N^4))
  * `init` (Impact: 17.1 | O(N^2))
  * `init` (Impact: 15.3 | O(N^2))
  * `init` (Impact: 9.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 29`, `args: 5`, `func_start: 5`, `class_start: 13`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 28`, `concurrency: 30`, `import: 2`
* *Defense:* `safety: 14`, `doc: 19`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, CoreGraphics
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.317 IQR)
- **Top Global Matches:** file_cluster_13: 13.317, file_cluster_2: 13.334, file_cluster_8: 13.504
- **Magnitude:** 1228.06 | **LOC:** 1210 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (98.9535%), Tech Debt (8.5497%)
**Top Internal Functions/Classes:**
  * `OnboardingFlow` (Impact: 285.0 | O(N^5) | DB: 151)
  * `GatewayStep` (Impact: 135.6 | O(N^4) | DB: 112)
  * `FinalStep` (Impact: 49.1 | O(N^2))
  * `PermissionsStep` (Impact: 48.3 | O(N^2) | DB: 27)
  * `StepRail` (Impact: 43.9 | O(N^5) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `args: 25`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 547`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 12`, `import: 79`
* *Defense:* `safety: 6`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` androidx.compose.foundation.layout.fillMaxHeight, androidx.compose.ui.text.style.TextOverflow, androidx.compose.material.icons.automirrored.filled.ArrowBack, androidx.compose.foundation.shape.RoundedCornerShape, androidx.compose.material3.Icon, androidx.compose.material3.SwitchDefaults, com.journeyapps.barcodescanner.ScanOptions, androidx.compose.foundation.layout.navigationBarsPadding...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ControlChannel.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.745 IQR)
- **Top Global Matches:** file_cluster_4: 11.745, file_cluster_8: 11.921, file_cluster_13: 12.147
- **Magnitude:** 1172.56 | **LOC:** 429 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (88.024%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `friendlyGatewayMessage` (Impact: 157.8 | O(N^5))
  * `scheduleRecovery` (Impact: 135.2 | O(N^6))
  * `configure` (Impact: 121.0 | O(2^N))
  * `routeWorkActivity` (Impact: 118.6 | O(N^4))
  * `health` (Impact: 111.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 74`, `args: 18`, `func_start: 18`, `class_start: 7`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 9`, `concurrency: 74`, `import: 5`
* *Defense:* `safety: 46`, `sync_locks: 3`, `immutability_locks: 88`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenClawProtocol, Observation, OpenClawKit, Foundation, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/ShareExtension/ShareViewController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.111 IQR)
- **Top Global Matches:** file_cluster_4: 12.111, file_cluster_8: 12.136, file_cluster_17: 12.239
- **Magnitude:** 1132.48 | **LOC:** 549 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (78.9828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendMessageToGateway` (Impact: 218.1 | O(N^6) | DB: 17)
  * `extractSharedContent` (Impact: 160.5 | O(N^6) | DB: 9)
  * `shouldRetryWithLegacyClientId` (Impact: 90.4 | O(N^4))
  * `sanitizeDraftFragment` (Impact: 51.3 | O(N^4))
  * `loadURLValue` (Impact: 42.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 101`, `args: 33`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `api: 5`, `concurrency: 60`, `import: 5`
* *Defense:* `safety: 47`, `sync_locks: 4`, `immutability_locks: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, UIKit, OpenClawKit, UniformTypeIdentifiers, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/PermissionManager.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.728 IQR)
- **Top Global Matches:** file_cluster_4: 10.728, file_cluster_8: 10.986, file_cluster_0: 11.131
- **Magnitude:** 1114.54 | **LOC:** 507 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (82.2871%), Tech Debt (99.4324%)
**Top Internal Functions/Classes:**
  * `status` (Impact: 271.9 | O(2^N) | DB: 1)
  * `ensureNotifications` (Impact: 76.1 | O(N^4))
  * `request` (Impact: 67.4 | O(N^5))
  * `ensureLocation` (Impact: 61.2 | O(N^4))
  * `ensureMicrophone` (Impact: 55.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 122`, `args: 40`, `func_start: 35`, `class_start: 9`
* *Risk/State:* `state_mutation: 33`, `duplicate_logic: 11`, `orphaned_logic: 6`
* *Architecture:* `api: 5`, `concurrency: 123`, `import: 10`
* *Defense:* `safety: 23`, `doc: 4`, `sync_locks: 20`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ApplicationServices, CoreLocation, CoreGraphics, Observation, OpenClawIPC, Speech, UserNotifications, AppKit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/ChannelConfigForm.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.806 IQR)
- **Top Global Matches:** file_cluster_17: 11.806, file_cluster_2: 11.887, file_cluster_8: 11.926
- **Magnitude:** 1111.72 | **LOC:** 364 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (33.9676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderNode` (Impact: 477.3 | O(2^N))
  * `renderStringField` (Impact: 127.0 | O(N^6))
  * `renderArray` (Impact: 113.8 | O(N^6) | DB: 5)
  * `renderAdditionalProperties` (Impact: 65.6 | O(N^6) | DB: 4)
  * `renderNumberField` (Impact: 61.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 43`, `args: 22`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `import: 1`
* *Defense:* `safety: 49`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `apps/macos/Sources/OpenClaw/HeartbeatStore.swift` (SWIFT) | Magnitude: 71.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, branch: 16, safety: 10, state_mutation: 9
- `apps/macos/Tests/OpenClawIPCTests/VoiceWakeRuntimeTests.swift` (SWIFT) | Magnitude: 77.82 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, immutability_locks: 22, test: 19, decorators: 11
- `apps/macos/Tests/OpenClawIPCTests/AudioInputDeviceObserverTests.swift` (SWIFT) | Magnitude: 11.4 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, test: 4, decorators: 4
- `apps/ios/Tests/NodeAppModelInvokeTests.swift` (SWIFT) | Magnitude: 572.8 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 430, immutability_locks: 131, concurrency: 101, test: 98
- `ui/src/ui/views/channels.nostr-profile-form.ts` (TYPESCRIPT) | Magnitude: 12.92 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 239, branch: 75, structural_boundaries: 58, safety: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/telegram/bot/types.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 8, indent_spaces: 8, branch: 7
- `src/config/types.signal.ts` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, branch: 18, doc: 14, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/tui/components/custom-editor.ts` (TYPESCRIPT) | Magnitude: 19.3 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 69, indent_spaces: 55, branch: 32, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/infra/provider-usage.fetch.gemini.ts` (TYPESCRIPT) | Magnitude: 8.81 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, branch: 18, state_mutation: 18, structural_boundaries: 10
- `src/commands/channels/logs.ts` (TYPESCRIPT) | Magnitude: 8.41 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 33, branch: 31, immutability_locks: 24
- `src/auto-reply/reply/commands-status.ts` (TYPESCRIPT) | Magnitude: 8.43 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, branch: 49, structural_boundaries: 36, immutability_locks: 25
- `src/config/agent-dirs.ts` (TYPESCRIPT) | Magnitude: 11.25 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 75, branch: 42, structural_boundaries: 30, immutability_locks: 20
- `src/commands/agent/delivery.ts` (TYPESCRIPT) | Magnitude: 16.79 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 197, branch: 89, immutability_locks: 37, structural_boundaries: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/channels/plugins/bluebubbles-actions.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, generics: 6, immutability_locks: 5
- `src/infra/map-size.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, branch: 4, state_mutation: 3, structural_boundaries: 2
- `src/agents/sandbox/types.docker.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, generics: 4, ui_framework: 3
- `src/plugin-sdk/config-paths.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, safety: 7, branch: 4, structural_boundaries: 4
- `extensions/voice-call/src/config.ts` (TYPESCRIPT) | Magnitude: 14.75 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 210, branch: 104, doc: 69, safety: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `apps/macos/Sources/OpenClaw/AboutSettings.swift` (SWIFT) | Magnitude: 78.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 164, state_mutation: 52, branch: 45, structural_boundaries: 31
- `src/channels/allowlists/resolve-utils.ts` (TYPESCRIPT) | Magnitude: 11.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, branch: 53, structural_boundaries: 33, immutability_locks: 31
- `src/agents/pi-extensions/session-manager-runtime-registry.ts` (TYPESCRIPT) | Magnitude: 2.37 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, branch: 7, state_mutation: 6
- `src/slack/scopes.ts` (TYPESCRIPT) | Magnitude: 13.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 86, branch: 31, structural_boundaries: 26, args: 15
- `src/agents/tools/sessions-announce-target.ts` (TYPESCRIPT) | Magnitude: 0.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, branch: 40, safety: 21, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `apps/macos/Sources/OpenClaw/ConfigSettings.swift` (SWIFT) | Magnitude: 571.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 351, branch: 103, structural_boundaries: 66, immutability_locks: 56
- `apps/macos/Sources/OpenClaw/TailscaleIntegrationSection.swift` (SWIFT) | Magnitude: 483.34 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 348, branch: 108, state_mutation: 94, structural_boundaries: 70
- `apps/ios/Sources/Screen/ScreenTab.swift` (SWIFT) | Magnitude: 17.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, ui_framework: 6, state_mutation: 2
- `apps/ios/Sources/RootTabs.swift` (SWIFT) | Magnitude: 67.06 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 100, state_mutation: 39, structural_boundaries: 22, branch: 21
- `apps/macos/Sources/OpenClaw/GeneralSettings.swift` (SWIFT) | Magnitude: 396.7 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 644, branch: 139, ui_framework: 85, structural_boundaries: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `extensions/qwen-portal-auth/oauth.ts` (TYPESCRIPT) | Magnitude: 5.95 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 136, branch: 49, structural_boundaries: 37, concurrency: 32
- `src/signal/daemon.ts` (TYPESCRIPT) | Magnitude: 15.67 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, branch: 46, structural_boundaries: 35, state_mutation: 33
- `src/plugins/services.ts` (TYPESCRIPT) | Magnitude: 5.67 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 24, branch: 13, concurrency: 12
- `apps/macos/Sources/OpenClaw/VoiceSessionCoordinator.swift` (SWIFT) | Magnitude: 341.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, branch: 39, structural_boundaries: 21, state_mutation: 21
- `src/canvas-host/server.ts` (TYPESCRIPT) | Magnitude: 14.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 385, structural_boundaries: 140, branch: 116, args: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ui/src/ui/chat/constants.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, api: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/web/auto-reply/types.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, branch: 18, structural_boundaries: 14, generics: 5
- `extensions/msteams/src/attachments/remote-media.ts` (TYPESCRIPT) | Magnitude: 1.65 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, branch: 13, structural_boundaries: 13, concurrency: 6
- `src/cron/run-log.ts` (TYPESCRIPT) | Magnitude: 24.65 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 352, branch: 197, structural_boundaries: 89, immutability_locks: 64
- `src/canvas-host/file-resolver.ts` (TYPESCRIPT) | Magnitude: 5.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, branch: 11, io: 10
- `src/cli/daemon-cli/shared.ts` (TYPESCRIPT) | Magnitude: 17.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 51, branch: 48, state_mutation: 27

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/agents/schema/typebox.ts` -> **Severity: 1098.68** (Blast Radius: 12.132 * Doc Risk: 90.5605%)
- `src/wizard/prompts.ts` -> **Severity: 432.865** (Blast Radius: 4.334 * Doc Risk: 99.8765%)
- `src/infra/ws.ts` -> **Severity: 361.831** (Blast Radius: 4.108 * Doc Risk: 88.0797%)
- `apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt` -> **Severity: 170.401** (Blast Radius: 2.598 * Doc Risk: 65.5894%)
- `extensions/msteams/src/sdk.ts` -> **Severity: 139.589** (Blast Radius: 1.396 * Doc Risk: 99.992%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
