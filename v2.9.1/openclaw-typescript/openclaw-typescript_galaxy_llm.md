# ARCHITECTURAL_BRIEF: openclaw-typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 5746 analyzed artifact(s), 886583 LOC.
- **Load-bearing artifact:** `src/agents/schema/typebox.ts` -- 61 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/plugin-sdk/index.ts` -- pulls in 146 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/commands/channels.adds-non-default-telegram-account.test.ts` at magnitude 11013.11 (structural weight, not risk).
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
| Total Artifacts | 5913 |
| Analyzed Artifacts (Scanned) | 5746 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 167 |
| Total LOC | 886583 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.84 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.278 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0863 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 88 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 4740 | 771980 | 82.5% |
| SWIFT | 514 | 72967 | 8.9% |
| MARKDOWN | 128 | 0 | 2.2% |
| KOTLIN | 102 | 15605 | 1.8% |
| SHELL | 61 | 7261 | 1.1% |
| JSON | 52 | 2686 | 0.9% |
| PLAINTEXT | 44 | 1 | 0.8% |
| JAVASCRIPT | 29 | 5270 | 0.5% |
| XML | 19 | 0 | 0.3% |
| GO | 14 | 1654 | 0.2% |
| CSS | 13 | 6468 | 0.2% |
| PYTHON | 11 | 1250 | 0.2% |
| DOCKERFILE | 6 | 136 | 0.1% |
| YAML | 5 | 318 | 0.1% |
| HTML | 5 | 815 | 0.1% |
| BATCH | 1 | 69 | 0.0% |
| RUBY | 1 | 84 | 0.0% |
| M4 | 1 | 19 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `3.263`
> **Composition Archetype:** `Flat Modular Platform` (z +3.26; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 31%, Declarative / Non-Code 20%, Callbacks & Closures Files 10%, Large Core Modules (3) 8%, Compute Cores Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5574 | 97.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 171 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 167*

**Composition by Extension & Reason:**
- `.prose`: 64x Excluded (Unsupported Extension: '.prose')
- `.png`: 22x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sandbox-browser'), 1x Excluded (Unsupported Extension: '.sandbox-common')
- `.ts`: 5x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 51 exceeds 500 chars), 1x Excluded (Saturation: Line 56 exceeds 500 chars)
- `.md`: 2x Excluded (Machine-Generated Source Code Signature: 256 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3121 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2972 LOC)
- `.ttf`: 4x Excluded (Explicitly Denied Extension: '.ttf')
- `.swift`: 2x Excluded (Machine-Generated Source Code Signature: 3326 LOC), 1x Excluded (Machine-Generated Source Code Signature: 39 LOC), 1x Excluded (Machine-Generated Source Code Signature: 84 LOC)
- `.tar`: 4x Excluded (Explicitly Denied Extension: '.tar')
- `.example`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.example')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 3x Excluded (Unsupported Extension: '.toml')
- `.jsonc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.resolved`: 2x Excluded (Unsupported Extension: '.resolved')
- `.xcconfig`: 2x Excluded (Unsupported Extension: '.xcconfig')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 27.5 | 17.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 27.6 | 26.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.9 | 7.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 44.9 | 24.7 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.9 | 11.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 59.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7236 | 1848 | 3 | `extensions/bluebubbles/src/monitor.test.ts` |
| cleanup | 1065 | 338 | 0 | `src/gateway/server.auth.test.ts` |
| guards | 63339 | 4214 | 29 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| danger | 9259 | 1788 | 4 | `scripts/pr` |
| concurrency | 54232 | 2951 | 27 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| connectivity | 16956 | 3227 | 8 | `src/plugin-sdk/index.ts` |
| io | 22978 | 2118 | 12 | `scripts/pr` |
| crypto | 2 | 1 | 0 | `scripts/ghsa-patch.mjs` |
| ipc | 251 | 163 | 0 | `src/slack/send.blocks.test.ts` |
| time | 3446 | 968 | 2 | `extensions/bluebubbles/src/monitor.test.ts` |
| serialization | 2169 | 820 | 1 | `src/gateway/session-utils.fs.test.ts` |
| regex | 2151 | 816 | 1 | `src/auto-reply/reply/line-directives.ts` |
| events | 4036 | 988 | 2 | `src/config/schema.help.ts` |
| tests | 52035 | 1982 | 27 | `src/agents/subagent-announce.format.test.ts` |
| docs | 3899 | 724 | 1 | `src/config/types.tools.ts` |
| debt | 2027 | 315 | 0 | `scripts/pr` |
| mutation | 148891 | 5154 | 66 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| dead_code | 3597 | 1307 | 2 | `src/discord/monitor/provider.test.ts` |
| credential | 163 | 71 | 0 | `src/config/redact-snapshot.test.ts` |
| threat | 849 | 293 | 0 | `apps/android/app/src/main/java/ai/openclaw/android/ui/SettingsSheet.kt` |
| ml_ai | 2816 | 738 | 1 | `scripts/pr` |
| ui | 4739 | 288 | 0 | `ui/src/styles/components.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/pr` (Hits: 349)
- `scripts/codesign-mac-app.sh` (Hits: 166)
- `src/security/audit.test.ts` (Hits: 157)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typebox.ts** (`src/agents/schema/typebox.ts`) — 61 inbound connections
2. **ws.ts** (`src/infra/ws.ts`) — 35 inbound connections
3. **prompts.ts** (`src/wizard/prompts.ts`) — 20 inbound connections
4. **GatewaySession.kt** (`apps/android/app/src/main/java/ai/openclaw/android/gateway/GatewaySession.kt`) — 15 inbound connections
5. **format-relative.ts** (`src/infra/format-time/format-relative.ts`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/plugin-sdk/index.ts`) — 146 outbound dependencies
2. **index.ts** (`src/plugins/runtime/index.ts`) — 85 outbound dependencies
3. **ChatMarkdown.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMarkdown.kt`) — 83 outbound dependencies
4. **types.ts** (`src/plugins/runtime/types.ts`) — 81 outbound dependencies
5. **OnboardingFlow.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `mergeConfig` **(Defensive Guards)** (@ `src/agents/memory-search.ts`) -> Impact: **738.8** | LOC: 216
- `processMessage` **(Many-Argument Workhorses)** (@ `extensions/bluebubbles/src/monitor-processing.ts`) -> Impact: **588.3** | LOC: 959
- `renderApp` **(Defensive Guards)** (@ `ui/src/ui/app-render.ts`) -> Impact: **433.5** | LOC: 1004
- `monitorMattermostProvider` **(Defensive Guards)** (@ `extensions/mattermost/src/mattermost/monitor.ts`) -> Impact: **425.4** | LOC: 843
- `runEmbeddedPiAgent` **(Many-Argument Workhorses)** (@ `src/agents/pi-embedded-runner/run.ts`) -> Impact: **420.6** | LOC: 973
- `attachGatewayWsMessageHandler` **(Many-Argument Workhorses)** (@ `src/gateway/server/ws-connection/message-handler.ts`) -> Impact: **405.8** | LOC: 961
- `renderSessionsCard` **(Many-Argument Workhorses)** (@ `ui/src/ui/views/usage-render-overview.ts`) -> Impact: **392.1** | LOC: 242
- `runEmbeddedAttempt` **(Many-Argument Workhorses)** (@ `src/agents/pi-embedded-runner/run/attempt.ts`) -> Impact: **374.9** | LOC: 1105
- `modelsStatusCommand` **(Many-Argument Workhorses)** (@ `src/commands/models/list.status-command.ts`) -> Impact: **363.9** | LOC: 626
- `createSignalEventHandler` **(Defensive Guards)** (@ `src/signal/monitor/event-handler.ts`) -> Impact: **360.4** | LOC: 674

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/agents` | 437 | 53991.28 | 20.58% | 1.12% |
| `src/commands` | 252 | 46880.09 | 30.34% | 0.4% |
| `src/infra` | 267 | 30872.47 | 29.74% | 4.45% |
| `apps/macos/Sources/OpenClaw` | 196 | 29412.08 | 50.4% | 37.01% |
| `src/gateway` | 192 | 25592.11 | 25.95% | 0.46% |
| `src/auto-reply/reply` | 158 | 23296.74 | 26.81% | 0.81% |
| `src/config` | 176 | 15401.46 | 14.98% | 2.22% |
| `src/cli` | 135 | 15033.31 | 34.37% | 0.89% |
| `src/browser` | 101 | 12059.13 | 36.04% | 1.91% |
| `src/discord/monitor` | 66 | 11702.67 | 23.4% | 1.91% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/memory/test-runtime-mocks.ts` -> **100.0%** Exposure
- `apps/macos/Sources/OpenClaw/CanvasWindowController+Testing.swift` -> **99.9999%** Exposure
- `src/test-utils/imessage-test-plugin.ts` -> **99.9996%** Exposure
- `extensions/voice-call/src/providers/base.ts` -> **99.9994%** Exposure
- `src/daemon/node-service.ts` -> **99.9975%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Swabble/Sources/SwabbleCore/Hooks/HookExecutor.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenController.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenRecordService.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenWebView.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Settings/SettingsTab.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/discord/monitor/provider.test.ts` -> **33** Orphaned Functions | **0** Duplicates
- `apps/ios/Tests/NodeAppModelInvokeTests.swift` -> **29** Orphaned Functions | **0** Duplicates
- `apps/android/app/src/main/java/ai/openclaw/android/NodeRuntime.kt` -> **29** Orphaned Functions | **0** Duplicates
- `apps/ios/Sources/Gateway/GatewayConnectionController.swift` -> **27** Orphaned Functions | **0** Duplicates
- `apps/ios/Sources/Model/NodeAppModel.swift` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/agents/models-config.falls-back-default-baseurl-token-exchange-fails.test.ts` -> **100.0%** Exposure
- `src/commands/doctor.migrates-routing-allowfrom-channels-whatsapp-allowfrom.test.ts` -> **100.0%** Exposure
- `src/config/env-preserve.test.ts` -> **100.0%** Exposure
- `src/config/redact-snapshot.test.ts` -> **100.0%** Exposure
- `src/gateway/startup-auth.test.ts` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `29` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8447` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/commands/channels.adds-non-default-telegram-account.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 11013.11 | **LOC:** 607 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (17.5%), Mutation Surface (formerly State Flux) (10.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 58`, `args: 29`, `func_start: 15`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `concurrency: 32`, `import: 8`
* *Defense:* `safety: 95`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` auth-profiles.js, clack-prompter.js, channel-test-helpers.js, channels.js, channels.mock-harness.js, test-runtime-config-helpers.js, vitest
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/auto-reply/reply/abort.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4161.88 | **LOC:** 346 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Connectivity (formerly Api Exposure) (62.9%), Guard Balance (formerly Safety Score) (57.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 65`, `args: 15`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 11`, `concurrency: 3`, `import: 15`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` agent-scope.js, pi-embedded.js, subagent-registry.js, sessions-helpers.js, config.js, sessions.js, globals.js, session-key.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/src/ui/controllers/usage.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2946.04 | **LOC:** 316 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.21; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.0%), Complexity Load (formerly Cognitive Load) (65.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 62`, `args: 20`, `func_start: 18`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.21
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000862
  * `Imports (Out-Degree: 1):` gateway.ts, types.ts, usage.ts
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/commands/onboard-auth.credentials.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2859.93 | **LOC:** 169 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (73.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 155
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 48`, `args: 10`, `func_start: 8`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `concurrency: 35`, `import: 3`
* *Defense:* `safety: 28`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` onboard-auth.js, test-wizard-helpers.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/bash-tools.exec.approval-id.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2700.68 | **LOC:** 341 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (92.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 139
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 103`, `args: 36`, `func_start: 8`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 17`, `concurrency: 49`, `import: 10`
* *Defense:* `safety: 12`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exec-obfuscation-detect.js, bash-tools.exec.js, gateway.js, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Model/NodeAppModel.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2657.6 | **LOC:** 2731 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.5%), Complexity Load (formerly Cognitive Load) (97.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.2301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startNodeGatewayLoop` **(Many-Argument Workhorses)** (Impact: 147.7)
  * `startOperatorGatewayLoop` **(Many-Argument Workhorses)** (Impact: 83.7)
  * `handleCanvasA2UIAction` **(Defensive Guards)** (Impact: 47.6)
  * `handleCanvasInvoke` **(Defensive Guards)** (Impact: 42.2)
  * `setScenePhase` **(Defensive Guards)** (Impact: 27.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 122 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 943
* *State Mutation (weighted view):* 477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 886`, `args: 163`, `func_start: 113`, `class_start: 27`
* *Risk/State:* `state_mutation: 215`, `unreferenced_by_name: 26`
* *Architecture:* `io: 15`, `concurrency: 333`, `import: 9`
* *Defense:* `safety: 240`, `doc: 2`, `sync_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Observation, OpenClawChatUI, OpenClawKit, OpenClawProtocol, Security, SwiftUI, UIKit, UserNotifications...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/discord/chunk.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2611.61 | **LOC:** 278 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (63.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 32`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 8`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chunk.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/onboard-auth.config-core.kilocode.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2506.74 | **LOC:** 207 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (92.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (12.3%), Complexity Load (formerly Cognitive Load) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 39`, `args: 25`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 3`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 44`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` model-auth.js, config.js, model-input.js, env.js, onboard-auth.config-core.js, onboard-auth.credentials.js, onboard-auth.models.js, node:fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/infra/bonjour-discovery.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2491.86 | **LOC:** 312 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.5%), Mutation Surface (formerly State Flux) (30.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 47`, `args: 21`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 5`
* *Architecture:* `concurrency: 13`, `import: 3`
* *Defense:* `safety: 9`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exec.js, bonjour-discovery.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Voice/TalkModeManager.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2355.7 | **LOC:** 2139 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `playAssistant` **(Defensive Guards)** (Impact: 93.3)
  * `buildIncrementalSpeechContext` **(Defensive Guards)** (Impact: 57.0)
  * `reloadConfig` **(Defensive Guards)** (Impact: 55.8)
  * `waitForChatCompletion` **(Defensive Guards)** (Impact: 43.8)
  * `processTranscript` **(Many-Argument Workhorses)** (Impact: 43.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 215 instances
* *Concurrency (weighted view):* 536
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 651`, `structural_boundaries: 549`, `args: 110`, `func_start: 90`, `class_start: 13`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 285`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 181`, `import: 8`
* *Defense:* `safety: 170`, `doc: 3`, `sync_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVFAudio, Foundation, OSLog, Observation, OpenClawChatUI, OpenClawKit, OpenClawProtocol, Speech
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/models-config.fills-missing-provider-apikey-from-env-var.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2194.28 | **LOC:** 311 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.0%), Mutation Surface (formerly State Flux) (21.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 50`, `args: 15`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 28`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 27`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` config.js, validation.js, agent-paths.js, models-config.e2e-harness.js, models-config.js, models-config.test-utils.js, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/pi-embedded-runner/run.overflow-compaction.mocks.shared.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2166.07 | **LOC:** 199 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (16.7%), Complexity Load (formerly Cognitive Load) (16.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 83`, `args: 67`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/pi-embedded-runner/run/images.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2046.83 | **LOC:** 313 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (8.0%), Guard Balance (formerly Safety Score) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 63`, `args: 32`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 46`, `concurrency: 18`, `import: 7`
* *Defense:* `safety: 35`, `test: 87`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` host-sandbox-fs-bridge.js, unsafe-mounted-sandbox.js, images.js, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/synology-chat/src/channel.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1837.86 | **LOC:** 424 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (20.1%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 70`, `args: 53`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 10`, `concurrency: 21`, `import: 3`
* *Defense:* `safety: 5`, `test: 91`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` channel.js, plugin-sdk, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hooks/internal-hooks.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1685.55 | **LOC:** 459 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 74`, `args: 43`, `func_start: 10`
* *Risk/State:* None
* *Architecture:* `concurrency: 25`, `import: 2`
* *Defense:* `safety: 9`, `test: 77`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` internal-hooks.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/memory/qmd-manager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1681.12 | **LOC:** 1901 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.5%), Complexity Load (formerly Cognitive Load) (86.0%), Guard Balance (formerly Safety Score) (52.4%)
- **Documentation Coverage:** 98.8764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Defensive Guards)** (Impact: 79.6)
  * `parseListedCollections` **(Compute Cores)** (Impact: 53.7)
  * `runSearchAttempt` **(Defensive Guards)** (Impact: 48.1)
  * `runQueryAcrossCollections` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `diversifyResultsBySource` **(Defensive Guards)** (Impact: 36.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 82 instances
* *Concurrency (weighted view):* 366
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 395`, `args: 120`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`
* *Architecture:* `io: 112`, `api: 9`, `concurrency: 161`, `import: 18`
* *Defense:* `safety: 124`, `doc: 1`, `immutability_locks: 17`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` agent-scope.js, config.js, paths.js, subsystem.js, backend-config.js, fs-utils.js, qmd-query-parser.js, qmd-scope.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/bluebubbles/src/monitor-processing.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1567.0 | **LOC:** 1447 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.6%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.9%), Complexity Load (formerly Cognitive Load) (60.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processMessage` **(Many-Argument Workhorses)** (Impact: 588.3)
  * `log` **(Compute Cores)** (Impact: 114.0)
  * `isSenderAllowed` **(Defensive Guards)** (Impact: 90.0)
  * `sanitizeReplyDirectiveText` **(Compute Cores)** (Impact: 80.3)
  * `deliver` **(Defensive Guards)** (Impact: 75.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 425`, `structural_boundaries: 140`, `args: 47`, `func_start: 40`
* *Risk/State:* `state_mutation: 50`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 21`, `import: 13`
* *Defense:* `safety: 111`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` attachments.js, chat.js, history.js, media-send.js, monitor-normalize.js, monitor-reply-cache.js, monitor-shared.js, probe.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/auto-reply/reply/export-html/template.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1546.44 | **LOC:** 1853 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (71.7%)
- **Documentation Coverage:** 70.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderToolCall` **(Defensive Guards)** (Impact: 114.7)
  * `renderResultImages` **(Defensive Guards)** (Impact: 76.9)
  * `renderEntry` **(Defensive Guards)** (Impact: 59.6)
  * `formatToolCall` **(Defensive Guards)** (Impact: 53.9)
  * `recalculateVisualStructure` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* /** * Recompute indentation/connectors for the filtered view * * Filtering can hide intermediate ent...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 191 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 350`, `args: 92`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 7`, `state_mutation: 218`, `unreferenced_by_name: 5`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 149`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/msteams/src/media-helpers.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1523.32 | **LOC:** 203 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (59.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 82`, `args: 44`, `func_start: 24`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 20`, `concurrency: 58`, `import: 2`
* *Defense:* `safety: 1`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` media-helpers.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/TalkModeRuntime.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1327.48 | **LOC:** 1052 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (99.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchTalkConfig` **(Defensive Guards)** (Impact: 81.7)
  * `playElevenLabs` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `preparePlaybackInput` **(Defensive Guards)** (Impact: 50.6)
  * `resolveVoiceId` **(Stateful Encapsulated Methods)** (Impact: 27.5)
  * `latestAssistantText` **(Defensive Guards)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 477
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 381`, `structural_boundaries: 311`, `args: 58`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `state_mutation: 80`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 137`, `import: 6`
* *Defense:* `safety: 92`, `sync_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVFoundation, Foundation, OSLog, OpenClawChatUI, OpenClawKit, Speech
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/doctor-config-flow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1292.14 | **LOC:** 1743 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (72.9%), Concurrency Surface (formerly Concurrency) (66.4%), Complexity Load (formerly Cognitive Load) (53.2%)
- **Documentation Coverage:** 97.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAndMaybeMigrateDoctorConfig` **(Compute Cores)** (Impact: 122.7)
  * `ensureWildcard` **(Many-Argument Workhorses)** (Impact: 75.8)
  * `maybeRepairOpenPolicyAllowFrom` **(Defensive Guards)** (Impact: 68.4)
    * *Intent:* /** * Scan all channel configs for dmPolicy="open" without allowFrom including "*". * This configura...
  * `scanMutableAllowlistEntries` **(Compute Cores)** (Impact: 55.6)
  * `maybeRepairTelegramAllowFromUsernames` **(Compute Cores)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 117 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 281`, `args: 69`, `func_start: 41`
* *Risk/State:* `state_mutation: 125`
* *Architecture:* `io: 44`, `api: 4`, `concurrency: 24`, `import: 23`
* *Defense:* `safety: 48`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` registry.js, allow-from.js, api.js, command-format.js, config.js, dangerous-name-matching.js, plugin-auto-enable.js, types.tools.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/models-config.providers.nvidia.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1263.98 | **LOC:** 116 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 38`, `args: 17`, `func_start: 11`
* *Risk/State:* None
* *Architecture:* `io: 6`, `concurrency: 23`, `import: 8`
* *Defense:* `safety: 26`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env.js, model-auth.js, models-config.providers.js, node:fs, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/system-prompt-stability.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1251.63 | **LOC:** 156 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 32`, `args: 18`, `func_start: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `concurrency: 20`, `import: 3`
* *Defense:* `safety: 15`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` workspace.js, workspace.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/discord/monitor/native-command.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1240.8 | **LOC:** 1730 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.163; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchDiscordCommandInteraction` **(Defensive Guards)** (Impact: 234.8)
  * `handleDiscordModelPickerInteraction` **(Many-Argument Workhorses)** (Impact: 164.2)
  * `readStore` **(Defensive Guards)** (Impact: 105.0)
  * `resolveDiscordModelPickerRoute` **(Defensive Guards)** (Impact: 51.1)
  * `deliverDiscordInteractionReply` **(Defensive Guards)** (Impact: 44.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 143
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 312`, `args: 93`, `func_start: 52`, `class_start: 4`
* *Risk/State:* `state_mutation: 44`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `concurrency: 93`, `import: 36`
* *Defense:* `safety: 148`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` identity.js, chunk.js, commands-registry.js, inbound-context.js, model-selection.js, provider-dispatcher.js, types.js, command-gating.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ui/src/ui/app.ts` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 99.9575%)
- `ui/src/ui/app-render.ts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 79.3035%)
- `ui/src/ui/app-gateway.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9839%)
- `ui/src/ui/app-settings.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9449%)
- `ui/src/ui/test-helpers/app-mount.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 96.0834%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ui/src/ui/navigation.ts` -> **Severity: 0.21** (Embedded: 0.0029 * Error Risk: 71.8375%)
- `src/wizard/prompts.ts` -> **Severity: 0.196** (Embedded: 0.0035 * Error Risk: 56.3934%)
- `ui/src/ui/app.ts` -> **Severity: 0.18** (Embedded: 0.002 * Error Risk: 88.6909%)
- `ui/src/ui/uuid.ts` -> **Severity: 0.178** (Embedded: 0.0019 * Error Risk: 93.445%)
- `ui/src/i18n/lib/translate.ts` -> **Severity: 0.164** (Embedded: 0.0021 * Error Risk: 80.1445%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/agents/schema/typebox.ts` -> **Severity: 847.4** (Blast Radius: 8.474 * Doc Risk: 100.0%)
- `src/infra/ws.ts` -> **Severity: 524.7** (Blast Radius: 5.247 * Doc Risk: 100.0%)
- `src/wizard/prompts.ts` -> **Severity: 286.4** (Blast Radius: 2.864 * Doc Risk: 100.0%)
- `ui/src/ui/views/config-form.shared.ts` -> **Severity: 197.5** (Blast Radius: 1.975 * Doc Risk: 100.0%)
- `test/mocks/baileys.ts` -> **Severity: 182.5** (Blast Radius: 1.825 * Doc Risk: 100.0%)

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
