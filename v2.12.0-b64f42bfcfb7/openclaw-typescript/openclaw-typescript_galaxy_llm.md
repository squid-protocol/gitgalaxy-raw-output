# ARCHITECTURAL_BRIEF: openclaw-typescript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 5768 analyzed artifact(s), 890452 LOC.
- **Load-bearing artifact:** `src/config/config.ts` -- 950 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/plugin-sdk/index.ts` -- pulls in 146 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/commands/channels.adds-non-default-telegram-account.test.ts` at magnitude 9150.85 (structural weight, not risk).
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
| Total Artifacts | 5929 |
| Analyzed Artifacts (Scanned) | 5768 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 161 |
| Total LOC | 890452 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6486 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.055 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.7738 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 834 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 4745 | 773830 | 82.3% |
| SWIFT | 516 | 73048 | 8.9% |
| MARKDOWN | 131 | 0 | 2.3% |
| KOTLIN | 102 | 15605 | 1.8% |
| SHELL | 62 | 7366 | 1.1% |
| JSON | 52 | 2686 | 0.9% |
| PLAINTEXT | 42 | 1 | 0.7% |
| JAVASCRIPT | 29 | 5270 | 0.5% |
| YAML | 23 | 2678 | 0.4% |
| XML | 19 | 0 | 0.3% |
| GO | 14 | 1654 | 0.2% |
| CSS | 13 | 6468 | 0.2% |
| DOCKERFILE | 6 | 136 | 0.1% |
| PYTHON | 6 | 723 | 0.1% |
| HTML | 5 | 815 | 0.1% |
| BATCH | 1 | 69 | 0.0% |
| RUBY | 1 | 84 | 0.0% |
| M4 | 1 | 19 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 5767 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 30%, Declarative / Non-Code 20%, Callbacks & Closures Files 9%, Large Core Modules (3) 8%, Compute Cores Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5595 | 97.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 172 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 161*

**Composition by Extension & Reason:**
- `.prose`: 64x Excluded (Unsupported Extension: '.prose')
- `.png`: 22x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.sandbox-browser'), 1x Excluded (Unsupported Extension: '.sandbox-common')
- `.ts`: 5x Unsupported Format (.undeterminable)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 248, Signals: 0)
- `.ttf`: 4x Excluded (Explicitly Denied Extension: '.ttf')
- `.tar`: 4x Excluded (Explicitly Denied Extension: '.tar')
- `.example`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.example')
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 3121 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2972 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 3x Excluded (Unsupported Extension: '.toml')
- `.jsonc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.resolved`: 2x Excluded (Unsupported Extension: '.resolved')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcconfig`: 2x Excluded (Unsupported Extension: '.xcconfig')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.6 | 15.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.9 | 28.2 | 40.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.5 | 7.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 44.8 | 24.1 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.1 | 11.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 19.5 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6996 | 1834 | 3 | `extensions/bluebubbles/src/monitor.test.ts` |
| cleanup | 1065 | 338 | 0 | `src/gateway/server.auth.test.ts` |
| guards | 63335 | 4221 | 29 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| danger | 9263 | 1791 | 4 | `scripts/pr` |
| concurrency | 54288 | 2958 | 27 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| connectivity | 16597 | 3230 | 8 | `src/plugin-sdk/index.ts` |
| io | 23274 | 2121 | 12 | `scripts/pr` |
| crypto | 197 | 194 | 0 | `src/gateway/server.auth.test.ts` |
| ipc | 254 | 164 | 0 | `src/slack/send.blocks.test.ts` |
| time | 3446 | 968 | 2 | `extensions/bluebubbles/src/monitor.test.ts` |
| serialization | 2173 | 821 | 1 | `src/gateway/session-utils.fs.test.ts` |
| regex | 2149 | 815 | 1 | `src/auto-reply/reply/line-directives.ts` |
| events | 4051 | 994 | 2 | `src/config/schema.help.ts` |
| tests | 52070 | 1985 | 27 | `src/agents/subagent-announce.format.test.ts` |
| docs | 3955 | 735 | 1 | `src/config/types.tools.ts` |
| debt | 2620 | 441 | 0 | `scripts/pr` |
| mutation | 149557 | 5167 | 66 | `apps/ios/Sources/Model/NodeAppModel.swift` |
| dead_code | 3420 | 1217 | 2 | `src/discord/monitor/provider.test.ts` |
| credential | 301 | 82 | 0 | `scripts/run-openclaw-podman.sh` |
| threat | 43 | 18 | 0 | `src/telegram/status-reaction-variants.test.ts` |
| ml_ai | 2781 | 718 | 1 | `scripts/pr` |
| ui | 4835 | 290 | 0 | `ui/src/styles/components.css` |

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

1. **config.ts** (`src/config/config.ts`) — 950 inbound connections
2. **runtime.ts** (`src/runtime.ts`) — 313 inbound connections
3. **utils.ts** (`src/utils.ts`) — 214 inbound connections
4. **sessions.ts** (`src/config/sessions.ts`) — 191 inbound connections
5. **session-key.ts** (`src/routing/session-key.ts`) — 172 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/plugin-sdk/index.ts`) — 146 outbound dependencies
2. **index.ts** (`src/plugins/runtime/index.ts`) — 85 outbound dependencies
3. **ChatMarkdown.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/chat/ChatMarkdown.kt`) — 83 outbound dependencies
4. **types.ts** (`src/plugins/runtime/types.ts`) — 81 outbound dependencies
5. **OnboardingFlow.kt** (`apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `mergeConfig` **(Defensive Guards)** (@ `src/agents/memory-search.ts`) -> Impact: **586.8** | LOC: 216
- `processMessage` **(Many-Argument Workhorses)** (@ `extensions/bluebubbles/src/monitor-processing.ts`) -> Impact: **487.9** | LOC: 959
- `monitorMattermostProvider` **(Defensive Guards)** (@ `extensions/mattermost/src/mattermost/monitor.ts`) -> Impact: **351.9** | LOC: 843
- `runEmbeddedPiAgent` **(Many-Argument Workhorses)** (@ `src/agents/pi-embedded-runner/run.ts`) -> Impact: **340.0** | LOC: 973
- `attachGatewayWsMessageHandler` **(Many-Argument Workhorses)** (@ `src/gateway/server/ws-connection/message-handler.ts`) -> Impact: **329.5** | LOC: 961
- `runEmbeddedAttempt` **(Many-Argument Workhorses)** (@ `src/agents/pi-embedded-runner/run/attempt.ts`) -> Impact: **325.4** | LOC: 1105
- `agentCommand` **(Many-Argument Workhorses)** (@ `src/commands/agent.ts`) -> Impact: **317.9** | LOC: 598
- `handleDiscordMessagingAction` **(Many-Argument Workhorses)** (@ `src/agents/tools/discord-actions-messaging.ts`) -> Impact: **314.3** | LOC: 473
- `createSignalEventHandler` **(Defensive Guards)** (@ `src/signal/monitor/event-handler.ts`) -> Impact: **302.4** | LOC: 674
- `modelsStatusCommand` **(Many-Argument Workhorses)** (@ `src/commands/models/list.status-command.ts`) -> Impact: **301.5** | LOC: 626

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/agents` | 438 | 47657.75 | 18.79% | 1.28% |
| `src/commands` | 252 | 38646.01 | 28.37% | 0.83% |
| `apps/macos/Sources/OpenClaw` | 197 | 28192.8 | 48.69% | 36.82% |
| `src/infra` | 267 | 26635.43 | 28.27% | 3.79% |
| `src/gateway` | 192 | 22789.23 | 24.92% | 0.77% |
| `src/auto-reply/reply` | 158 | 16341.98 | 25.05% | 1.08% |
| `src/config` | 176 | 14559.02 | 14.93% | 2.37% |
| `src/cli` | 135 | 13154.74 | 30.54% | 0.98% |
| `src/browser` | 101 | 10436.97 | 34.54% | 3.76% |
| `src/memory` | 84 | 10234.46 | 30.95% | 2.51% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/memory/test-runtime-mocks.ts` -> **100.0%** Exposure
- `apps/macos/Sources/OpenClaw/CanvasWindowController+Testing.swift` -> **99.9999%** Exposure
- `src/browser/control-service.ts` -> **99.9997%** Exposure
- `src/test-utils/imessage-test-plugin.ts` -> **99.9992%** Exposure
- `apps/android/app/src/main/java/ai/openclaw/android/node/NodeUtils.kt` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Swabble/Sources/SwabbleCore/Hooks/HookExecutor.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenController.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenRecordService.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Screen/ScreenWebView.swift` -> **100.0%** Exposure
- `apps/ios/Sources/Settings/SettingsTab.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/telegram/bot.create-telegram-bot.test.ts` -> **0** Orphaned Functions | **45** Duplicates
- `src/discord/monitor/provider.test.ts` -> **33** Orphaned Functions | **0** Duplicates
- `apps/ios/Tests/NodeAppModelInvokeTests.swift` -> **29** Orphaned Functions | **0** Duplicates
- `apps/android/app/src/main/java/ai/openclaw/android/NodeRuntime.kt` -> **29** Orphaned Functions | **0** Duplicates
- `src/telegram/bot.test.ts` -> **0** Orphaned Functions | **28** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `docker-setup.sh` -> **100.0%** Exposure
- `scripts/run-openclaw-podman.sh` -> **100.0%** Exposure
- `scripts/test-install-sh-e2e-docker.sh` -> **100.0%** Exposure
- `src/agents/models-config.falls-back-default-baseurl-token-exchange-fails.test.ts` -> **100.0%** Exposure
- `src/commands/doctor.migrates-routing-allowfrom-channels-whatsapp-allowfrom.test.ts` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `64` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8437` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/commands/channels.adds-non-default-telegram-account.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.092)
- **Top Global Matches:** file_cluster_10: 5.092, file_cluster_2: 6.299, file_cluster_13: 7.006
- **Magnitude:** 9150.85 | **LOC:** 607 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (28.5%), Complexity Load (formerly Cognitive Load) (14.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 58`, `args: 29`, `func_start: 15`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `concurrency: 32`, `import: 8`
* *Defense:* `safety: 95`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` auth-profiles.js, clack-prompter.js, channel-test-helpers.js, channels.js, channels.mock-harness.js, test-runtime-config-helpers.js, vitest
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Model/NodeAppModel.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.442)
- **Top Global Matches:** file_cluster_4: 6.442, file_cluster_6: 10.923, file_cluster_16: 11.746
- **Magnitude:** 2571.0 | **LOC:** 2731 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.084; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.5%), Complexity Load (formerly Cognitive Load) (97.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 98.2301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startNodeGatewayLoop` **(Many-Argument Workhorses)** (Impact: 134.5)
  * `startOperatorGatewayLoop` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `handleCanvasA2UIAction` **(Defensive Guards)** (Impact: 40.6)
  * `handleCanvasInvoke` **(Defensive Guards)** (Impact: 38.0)
  * `setScenePhase` **(Defensive Guards)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 122 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 943
* *State Mutation (weighted view):* 477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 577`, `structural_boundaries: 886`, `args: 163`, `func_start: 113`, `class_start: 27`
* *Risk/State:* `state_mutation: 215`, `unreferenced_by_name: 26`
* *Architecture:* `io: 15`, `concurrency: 333`, `import: 9`
* *Defense:* `safety: 240`, `doc: 2`, `sync_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.084
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000347
  * `Imports (Out-Degree: 42):` Observation, OpenClawChatUI, OpenClawKit, OpenClawProtocol, Security, SwiftUI, UIKit, UserNotifications...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/agents/bash-tools.exec.approval-id.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.635)
- **Top Global Matches:** file_cluster_10: 4.635, file_cluster_2: 7.077, file_cluster_13: 7.576
- **Magnitude:** 2518.19 | **LOC:** 341 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (92.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 139
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 103`, `args: 36`, `func_start: 8`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 17`, `concurrency: 49`, `import: 10`
* *Defense:* `safety: 12`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` exec-obfuscation-detect.js, bash-tools.exec.js, gateway.js, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/ios/Sources/Voice/TalkModeManager.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.406)
- **Top Global Matches:** file_cluster_4: 6.406, file_cluster_6: 9.678, file_cluster_16: 12.407
- **Magnitude:** 2292.9 | **LOC:** 2139 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.121; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `playAssistant` **(Defensive Guards)** (Impact: 79.2)
  * `reloadConfig` **(Defensive Guards)** (Impact: 53.8)
  * `processTranscript` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `buildIncrementalSpeechContext` **(Defensive Guards)** (Impact: 42.8)
  * `waitForChatCompletion` **(Defensive Guards)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 215 instances
* *Concurrency (weighted view):* 536
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 605`, `structural_boundaries: 549`, `args: 110`, `func_start: 90`, `class_start: 13`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 285`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 181`, `import: 8`
* *Defense:* `safety: 170`, `doc: 3`, `sync_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000462
  * `Imports (Out-Degree: 8):` AVFAudio, Foundation, OSLog, Observation, OpenClawChatUI, OpenClawKit, OpenClawProtocol, Speech
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/infra/bonjour-discovery.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.73)
- **Top Global Matches:** file_cluster_12: 5.73, file_cluster_10: 6.607, file_cluster_2: 7.196
- **Magnitude:** 2163.53 | **LOC:** 312 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.5%), Mutation Surface (formerly State Flux) (30.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 47`, `args: 21`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 5`
* *Architecture:* `concurrency: 13`, `import: 3`
* *Defense:* `safety: 9`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` exec.js, bonjour-discovery.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/models-config.fills-missing-provider-apikey-from-env-var.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.385)
- **Top Global Matches:** file_cluster_10: 5.385, file_cluster_2: 6.672, file_cluster_13: 7.238
- **Magnitude:** 2114.28 | **LOC:** 311 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.9%), Complexity Load (formerly Cognitive Load) (36.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 50`, `args: 15`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 28`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 27`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` config.js, validation.js, agent-paths.js, models-config.e2e-harness.js, models-config.js, models-config.test-utils.js, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/onboard-auth.config-core.kilocode.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.85)
- **Top Global Matches:** file_cluster_10: 4.85, file_cluster_2: 7.19, file_cluster_13: 7.601
- **Magnitude:** 2098.82 | **LOC:** 207 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (92.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (20.5%), Mutation Surface (formerly State Flux) (12.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 39`, `args: 25`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 3`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 44`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` model-auth.js, config.js, model-input.js, env.js, onboard-auth.config-core.js, onboard-auth.credentials.js, onboard-auth.models.js, node:fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/onboard-auth.credentials.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.876)
- **Top Global Matches:** file_cluster_10: 6.876, file_cluster_0: 7.371, file_cluster_2: 8.705
- **Magnitude:** 1993.61 | **LOC:** 169 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (50.0%), Mutation Surface (formerly State Flux) (47.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Concurrency (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 48`, `args: 10`, `func_start: 8`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `concurrency: 35`, `import: 3`
* *Defense:* `safety: 28`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` onboard-auth.js, test-wizard-helpers.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/pi-embedded-runner/run.overflow-compaction.mocks.shared.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.549)
- **Top Global Matches:** file_cluster_10: 5.549, file_cluster_0: 8.298, file_cluster_2: 8.417
- **Magnitude:** 1753.76 | **LOC:** 199 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 0.102; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (16.7%), Complexity Load (formerly Cognitive Load) (14.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 83`, `args: 67`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.00052
  * `Imports (Out-Degree: 1):` types.js, vitest
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/agents/pi-embedded-runner/run/images.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.321)
- **Top Global Matches:** file_cluster_10: 5.321, file_cluster_2: 7.721, file_cluster_13: 8.144
- **Magnitude:** 1644.71 | **LOC:** 313 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (24.7%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 63`, `args: 32`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 46`, `concurrency: 18`, `import: 7`
* *Defense:* `safety: 35`, `test: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` host-sandbox-fs-bridge.js, unsafe-mounted-sandbox.js, images.js, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/memory/qmd-manager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.344)
- **Top Global Matches:** file_cluster_4: 6.344, file_cluster_6: 10.834, file_cluster_16: 11.157
- **Magnitude:** 1565.92 | **LOC:** 1901 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.144; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.4%), Complexity Load (formerly Cognitive Load) (84.6%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 98.8372% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Defensive Guards)** (Impact: 72.7)
  * `parseListedCollections` **(Compute Cores)** (Impact: 50.9)
  * `runQueryAcrossCollections` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `diversifyResultsBySource` **(Defensive Guards)** (Impact: 31.7)
  * `pickDocLocation` **(Stateful Encapsulated Methods)** (Impact: 31.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 366
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 395`, `args: 120`, `func_start: 81`, `class_start: 1`
* *Risk/State:* `state_mutation: 110`
* *Architecture:* `io: 112`, `api: 6`, `concurrency: 161`, `import: 18`
* *Defense:* `safety: 124`, `doc: 1`, `immutability_locks: 17`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.000407 | `Ripple Effect (Closeness):` 0.059801
  * `Imports (Out-Degree: 12):` agent-scope.js, config.js, paths.js, subsystem.js, backend-config.js, fs-utils.js, qmd-query-parser.js, qmd-scope.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/auto-reply/reply/export-html/template.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_6: 6.436, file_cluster_4: 10.206, file_cluster_8: 15.627
- **Magnitude:** 1352.24 | **LOC:** 1853 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (69.8%), Guard Balance (formerly Safety Score) (60.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 70.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderToolCall` **(Defensive Guards)** (Impact: 101.9)
  * `renderEntry` **(Defensive Guards)** (Impact: 55.3)
  * `recalculateVisualStructure` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* /** * Recompute indentation/connectors for the filtered view * * Filtering can hide intermediate ent...
  * `getTreeNodeDisplayHtml` **(Defensive Guards)** (Impact: 42.1)
    * *Intent:* /** * Get display text for tree node (returns HTML string). */
  * `filterNodes` **(Defensive Guards)** (Impact: 38.1)
    * *Intent:* /** * Filter flat nodes based on current filterMode and searchQuery. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 594
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 350`, `args: 92`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 7`, `state_mutation: 218`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 6`
* *Defense:* `safety: 149`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/TalkModeRuntime.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.314)
- **Top Global Matches:** file_cluster_4: 7.314, file_cluster_16: 11.439, file_cluster_6: 11.755
- **Magnitude:** 1289.58 | **LOC:** 1052 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.12; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (99.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchTalkConfig` **(Defensive Guards)** (Impact: 72.7)
  * `playElevenLabs` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `preparePlaybackInput` **(Defensive Guards)** (Impact: 47.7)
  * `normalizedTalkProviders` **(Defensive Guards)** (Impact: 22.4)
  * `resolveVoiceId` **(Stateful Encapsulated Methods)** (Impact: 22.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 477
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 311`, `args: 58`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `state_mutation: 80`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 137`, `import: 6`
* *Defense:* `safety: 92`, `sync_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.12
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000173
  * `Imports (Out-Degree: 6):` AVFoundation, Foundation, OSLog, OpenClawChatUI, OpenClawKit, Speech
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/config/config.compaction-settings.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.832)
- **Top Global Matches:** file_cluster_10: 5.832, file_cluster_2: 7.761, file_cluster_13: 8.238
- **Magnitude:** 1207.66 | **LOC:** 81 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 13`, `args: 7`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `concurrency: 9`, `import: 3`
* *Defense:* `safety: 40`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` config.js, test-helpers.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/commands/doctor-config-flow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.425)
- **Top Global Matches:** file_cluster_6: 6.425, file_cluster_4: 11.393, file_cluster_8: 14.62
- **Magnitude:** 1182.04 | **LOC:** 1743 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **22**; blast radius 0.188; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (66.4%), Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadAndMaybeMigrateDoctorConfig` **(Compute Cores)** (Impact: 102.9)
  * `maybeRepairOpenPolicyAllowFrom` **(Defensive Guards)** (Impact: 62.8)
    * *Intent:* /** * Scan all channel configs for dmPolicy="open" without allowFrom including "*". * This configura...
  * `scanMutableAllowlistEntries` **(Compute Cores)** (Impact: 55.6)
  * `ensureWildcard` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `maybeRepairTelegramAllowFromUsernames` **(Compute Cores)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 114 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 281`, `args: 69`, `func_start: 41`
* *Risk/State:* `state_mutation: 125`
* *Architecture:* `io: 44`, `api: 2`, `concurrency: 24`, `import: 23`
* *Defense:* `safety: 48`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 0.00029 | `Ripple Effect (Closeness):` 0.002327
  * `Imports (Out-Degree: 19):` registry.js, allow-from.js, api.js, command-format.js, config.js, dangerous-name-matching.js, plugin-auto-enable.js, types.tools.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/agents/system-prompt-stability.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.116)
- **Top Global Matches:** file_cluster_10: 5.116, file_cluster_2: 6.93, file_cluster_13: 7.449
- **Magnitude:** 1162.46 | **LOC:** 156 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 32`, `args: 18`, `func_start: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `concurrency: 20`, `import: 3`
* *Defense:* `safety: 15`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` workspace.js, workspace.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/pi-embedded-runner/run.overflow-compaction.loop.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.86)
- **Top Global Matches:** file_cluster_10: 4.86, file_cluster_2: 6.302, file_cluster_12: 7.086
- **Magnitude:** 1146.53 | **LOC:** 339 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.4%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 42`, `args: 17`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `concurrency: 22`, `import: 7`
* *Defense:* `safety: 15`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` pi-embedded-helpers.js, logger.js, run.js, run.overflow-compaction.fixture.js, run.overflow-compaction.mocks.shared.js, run.overflow-compaction.shared-test.js, types.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/models-config.providers.nvidia.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.665)
- **Top Global Matches:** file_cluster_10: 5.665, file_cluster_2: 8.433, file_cluster_13: 8.546
- **Magnitude:** 1094.27 | **LOC:** 116 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 38`, `args: 17`, `func_start: 11`
* *Risk/State:* None
* *Architecture:* `io: 6`, `concurrency: 23`, `import: 8`
* *Defense:* `safety: 26`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` env.js, model-auth.js, models-config.providers.js, node:fs, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/macos/Sources/OpenClaw/MenuSessionsInjector.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.353)
- **Top Global Matches:** file_cluster_4: 6.353, file_cluster_16: 8.003, file_cluster_15: 9.324
- **Magnitude:** 1050.32 | **LOC:** 1241 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.078; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (58.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inject` **(Defensive Guards)** (Impact: 43.6)
  * `injectNodes` **(Compute Cores)** (Impact: 29.1)
  * `buildNodeSubmenu` **(Defensive Guards)** (Impact: 26.4)
  * `gatewayEntry` **(I/O & Config Routines)** (Impact: 20.7)
  * `menuWillOpen` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 170
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 264`, `args: 69`, `func_start: 57`, `class_start: 7`
* *Risk/State:* `state_mutation: 173`, `unreferenced_by_name: 11`
* *Architecture:* `api: 8`, `concurrency: 65`, `import: 4`
* *Defense:* `safety: 95`, `sync_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000173
  * `Imports (Out-Degree: 15):` AppKit, Foundation, Observation, SwiftUI
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `extensions/bluebubbles/src/monitor-processing.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.23)
- **Top Global Matches:** file_cluster_4: 6.23, file_cluster_15: 10.409, file_cluster_16: 11.583
- **Magnitude:** 1043.5 | **LOC:** 1447 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.083; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.6%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.9%), Complexity Load (formerly Cognitive Load) (55.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processMessage` **(Many-Argument Workhorses)** (Impact: 487.9)
  * `deliver` **(Many-Argument Workhorses)** (Impact: 63.0)
  * `processReaction` **(Defensive Guards)** (Impact: 38.0)
  * `planHistoryBackfillAttempt` **(Defensive Guards)** (Impact: 24.1)
  * `chatsMatch` **(Compute Cores)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 140`, `args: 47`, `func_start: 40`
* *Risk/State:* `state_mutation: 50`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 21`, `import: 13`
* *Defense:* `safety: 111`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000693
  * `Imports (Out-Degree: 11):` attachments.js, chat.js, history.js, media-send.js, monitor-normalize.js, monitor-reply-cache.js, monitor-shared.js, probe.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/memory/qmd-manager.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.416)
- **Top Global Matches:** file_cluster_10: 6.416, file_cluster_15: 8.284, file_cluster_12: 8.651
- **Magnitude:** 1034.56 | **LOC:** 2334 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (78.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createMockChild` **(Defensive Guards)** (Impact: 15.4)
  * `createManager` **(Defensive Guards)** (Impact: 13.5)
  * `all` **(Compute Cores)** (Impact: 12.2)
  * `isMcporterCommand` **(Compute Cores)** (Impact: 6.0)
  * `installOpenSpy` **(Callbacks & Closures)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 82 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 668
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 633`, `args: 237`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 102`, `duplicate_logic: 18`, `unreferenced_by_name: 1`
* *Architecture:* `io: 130`, `concurrency: 258`, `import: 11`
* *Defense:* `safety: 77`, `test: 171`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` config.js, backend-config.js, qmd-manager.js, node:child_process, node:events, promises, node:os, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/agents/pi-tools.create-openclaw-coding-tools.adds-claude-style-aliases-schemas-without-dropping-d.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.592)
- **Top Global Matches:** file_cluster_10: 6.592, file_cluster_2: 8.117, file_cluster_13: 8.197
- **Magnitude:** 1027.01 | **LOC:** 94 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (13.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 36`, `args: 17`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 18`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 22`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pi-tools.js, fast-coding-tools.js, host-sandbox-fs-bridge.js, pi-tools-sandbox-context.js, promises, node:os, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/discord/monitor/native-command.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_4: 7.049, file_cluster_6: 10.021, file_cluster_15: 12.748
- **Magnitude:** 1015.5 | **LOC:** 1730 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **35**; blast radius 0.086; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Complexity Load (formerly Cognitive Load) (57.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatchDiscordCommandInteraction` **(Defensive Guards)** (Impact: 208.0)
  * `handleDiscordModelPickerInteraction` **(Many-Argument Workhorses)** (Impact: 134.2)
  * `resolveDiscordModelPickerRoute` **(Defensive Guards)** (Impact: 44.1)
  * `deliverDiscordInteractionReply` **(Defensive Guards)** (Impact: 38.3)
  * `isDiscordUnknownInteraction` **(Defensive Guards)** (Impact: 26.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 143
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 312`, `args: 93`, `func_start: 52`, `class_start: 4`
* *Risk/State:* `state_mutation: 44`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 93`, `import: 36`
* *Defense:* `safety: 148`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.086
  * `Choke Point (Betweenness):` 0.001567 | `Ripple Effect (Closeness):` 0.066912
  * `Imports (Out-Degree: 35):` identity.js, chunk.js, commands-registry.js, inbound-context.js, model-selection.js, provider-dispatcher.js, types.js, command-gating.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/memory/manager-sync-ops.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.383)
- **Top Global Matches:** file_cluster_4: 6.383, file_cluster_6: 9.635, file_cluster_16: 11.944
- **Magnitude:** 975.0 | **LOC:** 1217 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.072; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (88.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runSync` **(Defensive Guards)** (Impact: 71.9)
  * `runSafeReindex` **(Defensive Guards)** (Impact: 36.5)
  * `syncSessionFiles` **(Compute Cores)** (Impact: 33.6)
  * `runUnsafeReindex` **(Defensive Guards)** (Impact: 24.9)
  * `syncMemoryFiles` **(Defensive Guards)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 200
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 200`, `args: 74`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 106`
* *Architecture:* `io: 52`, `api: 8`, `concurrency: 75`, `import: 27`
* *Defense:* `safety: 90`, `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.072
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.053554
  * `Imports (Out-Degree: 19):` agent-scope.js, memory-search.js, config.js, paths.js, subsystem.js, transcript-events.js, utils.js, embeddings-gemini.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/auto-reply/reply.test-harness.ts` (TYPESCRIPT) | Magnitude: 102.92 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 21, globals: 16, io: 15
- `extensions/matrix/src/matrix/send-queue.ts` (TYPESCRIPT) | Magnitude: 55.8 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 20, concurrency: 13, branch: 9
- `src/infra/archive.ts` (TYPESCRIPT) | Magnitude: 387.26 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 417, structural_boundaries: 145, branch: 90, core_var_decl: 71
- `src/web/reconnect.ts` (TYPESCRIPT) | Magnitude: 36.3 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 19, branch: 9, api: 7
- `extensions/feishu/src/types.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 32, branch: 23, api: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/cli/program/routes.ts` (TYPESCRIPT) | Magnitude: 346.74 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 86, core_var_decl: 58, branch: 40
- `src/auto-reply/reply/reply-elevated.test.ts` (TYPESCRIPT) | Magnitude: 7.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, test: 17, structural_boundaries: 13, args: 7
- `src/agents/memory-search.test.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 235, test: 32, core_var_decl: 25, branch: 24
- `src/browser/routes/agent.storage.ts` (TYPESCRIPT) | Magnitude: 240.54 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 395, structural_boundaries: 95, concurrency: 56, core_var_decl: 51
- `src/cli/program.nodes-media.test.ts` (TYPESCRIPT) | Magnitude: 181.84 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 281, structural_boundaries: 66, concurrency: 37, args: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `apps/shared/OpenClawKit/Tests/OpenClawKitTests/ChatViewModelTests.swift` (SWIFT) | Magnitude: 512.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 613, structural_boundaries: 221, concurrency: 210, core_var_decl: 72
- `apps/ios/Sources/Model/NodeAppModel+Canvas.swift` (SWIFT) | Magnitude: 82.74 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 27, branch: 20, concurrency: 11
- `apps/macos/Sources/OpenClaw/NodeMode/MacNodeLocationService.swift` (SWIFT) | Magnitude: 147.68 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 48, concurrency: 24, branch: 20
- `src/memory/temporal-decay.test.ts` (TYPESCRIPT) | Magnitude: 72.28 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 34, io: 30, concurrency: 26
- `src/infra/os-summary.ts` (TYPESCRIPT) | Magnitude: 11.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 13, core_var_decl: 7, design_snake_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/commands/models/shared.test.ts` (TYPESCRIPT) | Magnitude: 10.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 21, args: 10, test: 8
- `src/test-utils/channel-plugins.ts` (TYPESCRIPT) | Magnitude: 44.88 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 24, branch: 18, core_var_decl: 10
- `src/commands/health.snapshot.test.ts` (TYPESCRIPT) | Magnitude: 136.64 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 201, structural_boundaries: 71, branch: 43, test: 34
- `src/telegram/bot-native-command-menu.test.ts` (TYPESCRIPT) | Magnitude: 194.49 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 107, test: 25, structural_boundaries: 21, args: 13
- `extensions/nostr/src/nostr-bus.fuzz.test.ts` (TYPESCRIPT) | Magnitude: 58.1 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 387, test: 158, structural_boundaries: 155, args: 129

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `apps/ios/Tests/GatewaySettingsStoreTests.swift` (SWIFT) | Magnitude: 62.96 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 157, core_var_decl: 31, structural_boundaries: 27, test: 20
- `ui/vitest.config.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 3, import: 2, branch: 1
- `ui/src/ui/views/channels.imessage.ts` (TYPESCRIPT) | Magnitude: 10.76 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 23, core_var_decl: 12, design_snake_case: 12
- `apps/macos/Sources/OpenClaw/CanvasFileWatcher.swift` (SWIFT) | Magnitude: 11.58 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, args: 3, func_start: 3
- `src/line/flex-templates/message.ts` (TYPESCRIPT) | Magnitude: 3.28 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 5, import: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/claude-auth-status.sh` (SHELL) | Magnitude: 23.29 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 174, io: 109, branch: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ui/src/ui/views/channels.discord.ts` (TYPESCRIPT) | Magnitude: 12.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 23, core_var_decl: 12, design_snake_case: 12
- `ui/src/ui/views/channels.slack.ts` (TYPESCRIPT) | Magnitude: 12.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 23, core_var_decl: 12, design_snake_case: 12
- `.github/workflows/ci.yml` (YAML) | Magnitude: 158.0 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 671, branch: 110, structural_boundaries: 50, args: 50
- `src/test-utils/repo-scan.ts` (TYPESCRIPT) | Magnitude: 102.24 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 37, branch: 33, core_var_decl: 22
- `src/acp/secret-file.ts` (TYPESCRIPT) | Magnitude: 10.52 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 4, safety: 4, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `extensions/voice-call/src/providers/stt-openai-realtime.ts` (TYPESCRIPT) | Magnitude: 201.96 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 78, args: 36, branch: 35
- `src/imessage/monitor/echo-cache.ts` (TYPESCRIPT) | Magnitude: 55.62 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 22, branch: 21, core_var_decl: 15
- `extensions/voice-call/src/media-stream.ts` (TYPESCRIPT) | Magnitude: 296.6 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 354, structural_boundaries: 98, branch: 83, args: 45
- `apps/macos/Sources/OpenClaw/WebChatManager.swift` (SWIFT) | Magnitude: 114.66 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 99, branch: 33, structural_boundaries: 29, state_mutation: 22
- `apps/macos/Sources/OpenClaw/GatewayDiscoveryHelpers.swift` (SWIFT) | Magnitude: 71.0 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 61, branch: 33, structural_boundaries: 26, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/commands/agents.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `src/extensionAPI.ts` (TYPESCRIPT) | Magnitude: 23.26 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8, indent_spaces: 4
- `src/commands/channels.ts` (TYPESCRIPT) | Magnitude: 29.28 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 21, api: 14, import: 14, dependency_injection: 2
- `src/commands/models.ts` (TYPESCRIPT) | Magnitude: 25.66 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, api: 10, import: 10
- `src/config/prototype-keys.ts` (TYPESCRIPT) | Magnitude: 11.52 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, reflection_metaprogramming: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `apps/shared/OpenClawKit/Sources/OpenClawKit/TalkPromptBuilder.swift` (SWIFT) | Magnitude: 20.66 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 4, state_mutation: 4, branch: 3
- `assets/chrome-extension/options.html` (HTML) | Magnitude: 77.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, core_var_decl: 22, design_snake_case: 22, structural_boundaries: 20
- `apps/macos/Sources/OpenClaw/AboutSettings.swift` (SWIFT) | Magnitude: 51.52 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 31, ui_framework: 31, branch: 29
- `src/agents/together-models.ts` (TYPESCRIPT) | Magnitude: 7.7 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 6, api: 3, args: 1
- `src/logging/timestamps.ts` (TYPESCRIPT) | Magnitude: 4.78 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 12, core_var_decl: 11, design_snake_case: 7, design_camel_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/agents/workspace.ts` (TYPESCRIPT) | Magnitude: 453.8 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 155, core_var_decl: 98, concurrency: 91
- `src/cli/update-cli/progress.ts` (TYPESCRIPT) | Magnitude: 102.74 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 116, branch: 38, structural_boundaries: 28, core_var_decl: 17
- `src/auto-reply/reply/typing-mode.ts` (TYPESCRIPT) | Magnitude: 128.18 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 55, branch: 36, core_var_decl: 18
- `src/commands/auth-choice.apply.api-providers.ts` (TYPESCRIPT) | Magnitude: 337.3 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 620, branch: 82, structural_boundaries: 82, core_var_decl: 44
- `src/gateway/gateway-models.profiles.live.test.ts` (TYPESCRIPT) | Magnitude: 755.16 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1156, branch: 266, structural_boundaries: 204, core_var_decl: 191

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/commands/doctor.e2e-harness.ts` (TYPESCRIPT) | Magnitude: 123.18 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 133, args: 45, core_var_decl: 38
- `src/channels/plugins/config-schema.test.ts` (TYPESCRIPT) | Magnitude: 15.62 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 16, test: 8, core_var_decl: 7
- `ui/src/ui/views/usage-render-details.test.ts` (TYPESCRIPT) | Magnitude: 4.48 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 107, test: 31, core_var_decl: 17, structural_boundaries: 16
- `vitest.extensions.config.ts` (TYPESCRIPT) | Magnitude: 16.26 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 6, branch: 5, structural_boundaries: 5, core_var_decl: 3
- `vitest.gateway.config.ts` (TYPESCRIPT) | Magnitude: 16.26 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 6, branch: 5, structural_boundaries: 5, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/commands/agents.config.ts` (TYPESCRIPT) | Magnitude: 145.36 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 162, branch: 69, structural_boundaries: 42, core_var_decl: 38
- `apps/macos/Sources/OpenClaw/NodeServiceManager.swift` (SWIFT) | Magnitude: 116.82 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 130, branch: 58, structural_boundaries: 42, core_var_decl: 35
- `ui/src/ui/controllers/chat.ts` (TYPESCRIPT) | Magnitude: 248.1 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 232, branch: 65, structural_boundaries: 64, state_mutation: 36
- `src/shared/config-eval.ts` (TYPESCRIPT) | Magnitude: 117.04 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 135, branch: 57, structural_boundaries: 51, core_var_decl: 24
- `src/agents/tool-mutation.ts` (TYPESCRIPT) | Magnitude: 147.36 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 159, branch: 64, structural_boundaries: 39, core_var_decl: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/agents/bootstrap-files.test.ts` (TYPESCRIPT) | Magnitude: 24.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 33, args: 17, io: 14
- `scripts/test-live-models-docker.sh` (SHELL) | Magnitude: 2.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 16, core_var_decl: 16, design_upper_case: 16, structural_boundaries: 12
- `src/gateway/agent-prompt.test.ts` (TYPESCRIPT) | Magnitude: 16.7 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 25, test: 13, args: 12
- `src/commands/onboard-interactive.test.ts` (TYPESCRIPT) | Magnitude: 9.8 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 27, test: 14, args: 13
- `src/browser/pw-session.create-page.navigation-guard.test.ts` (TYPESCRIPT) | Magnitude: 19.76 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 33, args: 17, closures: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/daemon/paths.ts` (TYPESCRIPT) | Magnitude: 32.06 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, branch: 14, structural_boundaries: 12, core_var_decl: 9
- `src/cli/npm-resolution.ts` (TYPESCRIPT) | Magnitude: 83.46 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 102, branch: 42, structural_boundaries: 28, args: 7
- `src/gateway/live-tool-probe-utils.ts` (TYPESCRIPT) | Magnitude: 23.96 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, branch: 11, structural_boundaries: 10, args: 2
- `src/channels/plugins/normalize/shared.ts` (TYPESCRIPT) | Magnitude: 16.12 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, branch: 7, structural_boundaries: 7, args: 2
- `src/agents/sandbox/runtime-status.ts` (TYPESCRIPT) | Magnitude: 86.66 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, branch: 24, structural_boundaries: 24, state_mutation: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/config/validation.ts` -> **Severity: 4.106** (Bridge: 0.0411 * Flux: 100.0%)
- `src/plugins/registry.ts` -> **Severity: 3.95** (Bridge: 0.0527 * Flux: 74.8894%)
- `src/plugins/runtime.ts` -> **Severity: 2.774** (Bridge: 0.0278 * Flux: 99.9254%)
- `src/plugins/manifest-registry.ts` -> **Severity: 1.616** (Bridge: 0.02 * Flux: 80.7775%)
- `src/infra/outbound/deliver.ts` -> **Severity: 1.351** (Bridge: 0.0204 * Flux: 66.1271%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/runtime.ts` -> **Severity: 8.598** (Embedded: 0.1488 * Error Risk: 57.7931%)
- `src/config/runtime-overrides.ts` -> **Severity: 7.524** (Embedded: 0.1383 * Error Risk: 54.4004%)
- `src/config/paths.ts` -> **Severity: 7.44** (Embedded: 0.1762 * Error Risk: 42.213%)
- `src/globals.ts` -> **Severity: 7.428** (Embedded: 0.1529 * Error Risk: 48.5718%)
- `src/logging/subsystem.ts` -> **Severity: 7.412** (Embedded: 0.141 * Error Risk: 52.5723%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/utils.ts` -> **Severity: 976.303** (Blast Radius: 11.797 * Doc Risk: 82.7586%)
- `src/infra/home-dir.ts` -> **Severity: 783.3** (Blast Radius: 7.833 * Doc Risk: 100.0%)
- `src/channels/chat-type.ts` -> **Severity: 717.2** (Blast Radius: 7.172 * Doc Risk: 100.0%)
- `src/runtime.ts` -> **Severity: 685.0** (Blast Radius: 6.85 * Doc Risk: 100.0%)
- `src/globals.ts` -> **Severity: 665.6** (Blast Radius: 6.656 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1694 literal sites + 110 sites through wrappers = 1804
- **`panics_and_aborts`:** 5299 literal sites + 102 sites through wrappers = 5401

- `logProgress` (function, debug_prints, primitive): 37 call sites in 1 files -- `src/gateway/gateway-models.profiles.live.test.ts`
- `logInfo` (function, debug_prints, primitive): 35 call sites in 1 files -- `scripts/label-open-issues.ts`
- `failInvalidOption` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `src/acp/control-plane/runtime-options.ts`
- `persistCallRecord` (function, debug_prints, primitive): 11 call sites in 3 files -- `extensions/voice-call/src/manager/store.ts`
- `logStep` (function, debug_prints, primitive): 8 call sites in 1 files -- `scripts/label-open-issues.ts`
- `sanitizeNotificationText` (function, panics_and_aborts, primitive): 7 call sites in 2 files -- `apps/android/app/src/main/java/ai/openclaw/android/node/DeviceNotificationListenerService.kt`
- `isPermissionGranted` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `apps/android/app/src/main/java/ai/openclaw/android/ui/OnboardingFlow.kt`
- `logHeader` (function, debug_prints, primitive): 6 call sites in 1 files -- `scripts/label-open-issues.ts`
- `exitWithError` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `src/cli/exec-approvals-cli.ts`
- `fail` (function, debug_prints, primitive): 5 call sites in 1 files -- `scripts/ghsa-patch.mjs`
- `fail` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `scripts/ghsa-patch.mjs`
- `jsonField` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `apps/android/app/src/main/java/ai/openclaw/android/ui/GatewayConfigResolver.kt`
*(+43 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 92356 call pairs -- scoped 33.8%, unique 1.0%, ambiguous 13.2%, external 51.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 72720 | 35.8% | 0.0% | 13.2% | 51.0% |
| swift | 13390 | 29.0% | 6.4% | 17.2% | 47.5% |
| kotlin | 3868 | 20.4% | 1.5% | 4.0% | 74.0% |
| javascript | 939 | 21.3% | 0.0% | 16.5% | 62.2% |
| shell | 824 | 28.5% | 0.1% | 0.0% | 71.4% |
| go | 374 | 16.0% | 9.4% | 0.0% | 74.6% |
| python | 194 | 17.0% | 0.0% | 0.5% | 82.5% |
| ruby | 27 | 3.7% | 0.0% | 0.0% | 96.3% |
| html | 20 | 0.0% | 0.0% | 0.0% | 100.0% |

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
