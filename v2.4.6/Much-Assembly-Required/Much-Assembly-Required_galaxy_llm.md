# ARCHITECTURAL_BRIEF: Much-Assembly-Required
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/Much-Assembly-Required` |
| **Timestamp** | `2026-08-03T19:26:36.960291+00:00` |
| **Scan Duration** | `1.98s` |
| **Git Branch** | `master` |
| **Git Commit** | `ac374f5b525615da3ecb36b08cc5fc53ab73dc96` |
| **Git Remote** | `https://github.com/simon987/Much-Assembly-Required.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 379 malicious artifacts.

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
| Total Artifacts | 451 |
| Analyzed Artifacts (Scanned) | 400 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 51 |
| Total LOC | 34141 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5209 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2753 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0588 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 323 | 12507 | 80.8% |
| JAVASCRIPT | 43 | 12838 | 10.8% |
| TYPESCRIPT | 10 | 8403 | 2.5% |
| XML | 8 | 0 | 2.0% |
| PLAINTEXT | 7 | 0 | 1.8% |
| MARKDOWN | 2 | 0 | 0.5% |
| JSON | 2 | 82 | 0.5% |
| DOCKERFILE | 1 | 6 | 0.2% |
| CSS | 1 | 261 | 0.2% |
| RUBY | 1 | 5 | 0.2% |
| SHELL | 1 | 12 | 0.2% |
| YAML | 1 | 27 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.639`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 197 | 49.2% |
| file_cluster_13 | 180 | 45.0% |
| file_cluster_0 | 8 | 2.0% |
| file_cluster_4 | 2 | 0.5% |
| file_cluster_7 | 1 | 0.2% |
| file_cluster_16 | 1 | 0.2% |
| file_cluster_11 | 1 | 0.2% |
| file_cluster_15 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 51*

**Composition by Extension & Reason:**
- `.java`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.vm`: 7x Unsupported Format (.vm)
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 105225 LOC exceeds safe regex boundaries)
- `.iml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.json`: 1x Excluded (Massive Static Asset Blob: 12161 LOC)
- `.woff`: 1x Excluded (Explicitly Denied Extension: '.woff')
- `.woff2`: 1x Excluded (Explicitly Denied Extension: '.woff2')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.1 | 7.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 41.6 | 55.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.5 | 25.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.9 | 2.4 | 80.0 |
| API Exposure | 0.0 | 13.7 | 6.6 | 6.9 | 8.6 |
| Concurrency Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.3 | 13.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 66.5 | 88.2 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 58.0 | 92.3 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 30.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Server/src/main/resources/static/js/ace/ace.js` (Hits: 18)
- `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` (Hits: 8)
- `Server/src/main/typescript/phaser.d.ts` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Status.java** (`Server/src/main/java/net/simon987/server/assembly/Status.java`) — 91 inbound connections
2. **GameServer.java** (`Server/src/main/java/net/simon987/server/GameServer.java`) — 66 inbound connections
3. **Instruction.java** (`Server/src/main/java/net/simon987/server/assembly/Instruction.java`) — 46 inbound connections
4. **LogManager.java** (`Server/src/main/java/net/simon987/server/logging/LogManager.java`) — 43 inbound connections
5. **Target.java** (`Server/src/main/java/net/simon987/server/assembly/Target.java`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ace.js** (`Server/src/main/resources/static/js/ace/ace.js`) — 87 outbound dependencies
2. **GameServer.java** (`Server/src/main/java/net/simon987/server/GameServer.java`) — 23 outbound dependencies
3. **Cubot.java** (`Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java`) — 19 outbound dependencies
4. **UserCreationListener.java** (`Plugin Cubot/src/main/java/net/simon987/cubotplugin/event/UserCreationListener.java`) — 16 outbound dependencies
5. **HackedNPC.java** (`Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **6149.7** | LOC: 1429
- `Isometric` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **2857.8** | LOC: 1157
  * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **2153.5** | LOC: 701
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **1456.4** | LOC: 351
- `updateTexture` (@ `Server/src/main/typescript/phaser.d.ts`) -> Impact: **1281.7** | LOC: 934
- `define` (@ `Server/src/main/resources/static/js/ace/ext-searchbox.js`) -> Impact: **567.9** | LOC: 506
- `addIsoSprite` (@ `Server/src/main/typescript/phaser.plugin.isometric.d.ts`) -> Impact: **500.9** | LOC: 361
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **358.2** | LOC: 235
- `Operand` (@ `Server/src/test/java/net/simon987/server/assembly/OperandTest.java`) -> Impact: **350.8** | LOC: 136
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **340.2** | LOC: 72

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `tick` (@ `Plugin NPC/src/main/java/net/simon987/npcplugin/HarvestTask.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `save` (@ `Server/src/main/java/net/simon987/server/GameServer.java`) -> **O(2^N) [Recursive]**
- `parseInstruction` (@ `Server/src/main/java/net/simon987/server/assembly/Assembler.java`) -> **O(2^N) [Recursive]**
- `Operand` (@ `Server/src/main/java/net/simon987/server/assembly/Operand.java`) -> **O(2^N) [Recursive]**
- `load` (@ `Server/src/main/java/net/simon987/server/plugin/PluginManager.java`) -> **O(2^N) [Recursive]**
- `handle` (@ `Server/src/main/java/net/simon987/server/websocket/TerrainRequestHandler.java`) -> **O(2^N) [Recursive]**
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> **O(2^N) [Recursive]**
- `define` (@ `Server/src/main/resources/static/js/ace/mode-mar.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /* ***** BEGIN LICENSE BLOCK ***** * Distributed under the BSD license: * * Copyright (c) 2012, Ajax.org B.V. * All rights reserved. * * Redistributio...
- `Isometric` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
- `tick` (@ `Server/src/main/java/net/simon987/server/GameServer.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Isometric` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> DB Complexity: **542**
  * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> DB Complexity: **360**
- `define` (@ `Server/src/main/resources/static/js/ace/ext-searchbox.js`) -> DB Complexity: **151**
- `initialiseAnimations` (@ `Server/src/main/resources/static/js/mar.js`) -> DB Complexity: **119**
- `initialiseAnimations` (@ `Server/src/main/typescript/MarGame.ts`) -> DB Complexity: **119**
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> DB Complexity: **106**
- `constructor` (@ `Server/src/main/typescript/GameObject.ts`) -> DB Complexity: **54**
- `DefaultInstructionSet` (@ `Server/src/main/java/net/simon987/server/assembly/DefaultInstructionSet.java`) -> DB Complexity: **49**
  * *Intent:* /** * Map of aliasses, stored in mnemonic : Instruction format
- `updateObject` (@ `Server/src/main/resources/static/js/mar.js`) -> DB Complexity: **27**
- `updateObject` (@ `Server/src/main/typescript/GameObject.ts`) -> DB Complexity: **27**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Server/src/main/resources/static/js/ace` | 40 | 16749.92 | 5.31% | 24.82% |
| `Server/src/main/resources/static/js` | 3 | 8187.64 | 74.86% | 36.24% |
| `Server/src/main/java/net/simon987/server/assembly` | 18 | 3033.32 | 12.44% | 47.22% |
| `Plugin NPC/src/main/java/net/simon987/npcplugin` | 21 | 2816.48 | 26.22% | 77.08% |
| `Plugin Cubot/src/main/java/net/simon987/cubotplugin` | 17 | 2347.42 | 36.38% | 87.34% |
| `Server/src/main/java/net/simon987/server/assembly/instruction` | 76 | 1832.3 | 16.48% | 60.5% |
| `Server/src/main/java/net/simon987/server/game/objects` | 15 | 1217.27 | 10.04% | 17.18% |
| `Server/src/main/java/net/simon987/server/game/world` | 13 | 1117.54 | 7.11% | 48.86% |
| `Server/src/main/java/net/simon987/server/websocket` | 12 | 788.56 | 35.88% | 67.05% |
| `Server/src/main/typescript` | 11 | 778.11 | 33.08% | 75.08% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotBattery.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotCore.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotHardwareModule.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotKeyboard.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLaser.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/event/UserCreationListener.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/DefaultInstructionSet.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/DivInstruction.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/MulInstruction.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/NegInstruction.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Server/src/main/resources/static/js/mar.js` -> **4** Orphaned Functions | **57** Duplicates
- `Server/src/main/typescript/phaser.d.ts` -> **19** Orphaned Functions | **21** Duplicates
- `Server/src/main/typescript/GameObject.ts` -> **1** Orphaned Functions | **37** Duplicates
- `Server/src/main/typescript/p2.d.ts` -> **8** Orphaned Functions | **13** Duplicates
- `Server/src/main/typescript/GameClient.ts` -> **4** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java`** -> AI Confidence: **99.39%**
2. **`Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java`** -> AI Confidence: **99.31%**
3. **`Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLaser.java`** -> AI Confidence: **99.31%**
4. **`Plugin NPC/src/main/java/net/simon987/npcplugin/HarvestTask.java`** -> AI Confidence: **99.31%**
5. **`Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java`** -> AI Confidence: **99.31%**
6. **`Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldUtils.java`** -> AI Confidence: **99.31%**
7. **`Plugin Plant/src/main/java/net/simon987/biomassplugin/WorldUtils.java`** -> AI Confidence: **99.31%**
8. **`Server/src/main/java/net/simon987/server/assembly/Assembler.java`** -> AI Confidence: **99.31%**
9. **`Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java`** -> AI Confidence: **99.31%**
10. **`Server/src/main/resources/static/js/ace/ace.js`** -> AI Confidence: **99.31%**
11. **`Server/src/main/typescript/Console.ts`** -> AI Confidence: **99.29%**
12. **`Server/src/main/typescript/MarGame.ts`** -> AI Confidence: **99.29%**
13. **`Server/src/main/typescript/phaser.d.ts`** -> AI Confidence: **99.29%**
14. **`Server/src/main/typescript/phaser.plugin.isometric.d.ts`** -> AI Confidence: **99.29%**
15. **`Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java`** -> AI Confidence: **99.24%**
16. **`Server/src/main/java/net/simon987/server/game/objects/GameObject.java`** -> AI Confidence: **99.24%**
17. **`Server/src/main/java/net/simon987/server/game/world/World.java`** -> AI Confidence: **99.24%**
18. **`Server/src/main/java/net/simon987/server/plugin/PluginManager.java`** -> AI Confidence: **99.24%**
19. **`Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotInventory.java`** -> AI Confidence: **99.23%**
20. **`Server/src/main/java/net/simon987/server/game/objects/GameRegistry.java`** -> AI Confidence: **99.23%**
21. **`Server/src/main/java/net/simon987/server/game/world/WorldGenerator.java`** -> AI Confidence: **99.23%**
22. **`Server/src/main/java/net/simon987/server/web/FloppyUploadRoute.java`** -> AI Confidence: **99.23%**
23. **`Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java`** -> AI Confidence: **99.18%**
24. **`Plugin NPC/src/main/java/net/simon987/npcplugin/RadioReceiverHardware.java`** -> AI Confidence: **99.18%**
25. **`Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java`** -> AI Confidence: **99.18%**
26. **`Plugin NPC/src/main/java/net/simon987/npcplugin/event/VaultWorldUpdateListener.java`** -> AI Confidence: **99.18%**
27. **`Plugin Plant/src/main/java/net/simon987/biomassplugin/event/WorldCreationListener.java`** -> AI Confidence: **99.18%**
28. **`Plugin Plant/src/main/java/net/simon987/biomassplugin/event/WorldUpdateListener.java`** -> AI Confidence: **99.18%**
29. **`Server/src/main/java/net/simon987/server/assembly/Memory.java`** -> AI Confidence: **99.18%**
30. **`Server/src/main/java/net/simon987/server/websocket/CodeUploadHandler.java`** -> AI Confidence: **99.18%**
31. **`plugin-contruction/src/main/java/net/simon987/constructionplugin/BluePrint.java`** -> AI Confidence: **99.18%**
32. **`Server/src/main/resources/static/js/phaser-plugin-isometric.js`** -> AI Confidence: **99.17%**
33. **`Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java`** -> AI Confidence: **99.16%**
34. **`Server/src/main/java/net/simon987/server/GameServer.java`** -> AI Confidence: **99.16%**
35. **`Server/src/main/java/net/simon987/server/assembly/CPU.java`** -> AI Confidence: **99.16%**
36. **`Server/src/main/java/net/simon987/server/game/GameUniverse.java`** -> AI Confidence: **99.16%**
37. **`Server/src/main/java/net/simon987/server/game/world/TileMap.java`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotBattery.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotDrill.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotFloppyDrive.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Server/src/main/java/net/simon987/server/assembly/CPU.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/Instruction.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/BrkInstruction.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/CallInstruction.java` -> **100.0%** Exposure
- `Server/src/main/java/net/simon987/server/assembly/instruction/CmpInstruction.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotBattery.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotDrill.java` -> **100.0%** Exposure
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotFloppyDrive.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1256` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA) -> Cumulative Risk: **967.67**
- **Archetype:** `file_cluster_0` (Distance: 12.264 IQR)
- **Magnitude:** 663.3 | **LOC:** 340 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `jsonSerialise` (Impact: 61.0), `setParent` (Impact: 45.0), `getParent` (Impact: 40.3)

### 2. `Server/src/main/typescript/GameObject.ts` (TYPESCRIPT) -> Cumulative Risk: **957.6**
- **Archetype:** `file_cluster_8` (Distance: 13.17 IQR)
- **Magnitude:** 114.15 | **LOC:** 889 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `updateObject` (Impact: 71.0), `walk` (Impact: 70.3), `updateHologram` (Impact: 68.8)

### 3. `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT) -> Cumulative Risk: **881.3**
- **Archetype:** `file_cluster_8` (Distance: 13.701 IQR)
- **Magnitude:** 3434.6 | **LOC:** 1946 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `MarGame` (Impact: 125.8), `handle` (Impact: 90.8), `handleObjectsUpdate` (Impact: 86.8)

### 4. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` (JAVA) -> Cumulative Risk: **872.82**
- **Archetype:** `file_cluster_13` (Distance: 11.409 IQR)
- **Magnitude:** 263.36 | **LOC:** 131 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 215.8), `CubotComPort` (Impact: 3.1), `getId` (Impact: 3.1)

### 5. `Server/src/main/java/net/simon987/server/assembly/instruction/MulInstruction.java` (JAVA) -> Cumulative Risk: **872.2**
- **Archetype:** `file_cluster_8` (Distance: 12.167 IQR)
- **Magnitude:** 66.2 | **LOC:** 61 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `execute` (Impact: 12.9), `execute` (Impact: 11.3), `MulInstruction` (Impact: 3.2)

### 6. `Plugin NPC/src/main/java/net/simon987/npcplugin/HarvesterNPC.java` (JAVA) -> Cumulative Risk: **863.83**
- **Archetype:** `file_cluster_13` (Distance: 11.193 IQR)
- **Magnitude:** 115.52 | **LOC:** 96 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9971%)
- **Heaviest Functions:** `update` (Impact: 50.9), `onDeadCallback` (Impact: 8.6), `jsonSerialise` (Impact: 6.5)

### 7. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLeg.java` (JAVA) -> Cumulative Risk: **858.87**
- **Archetype:** `file_cluster_13` (Distance: 11.082 IQR)
- **Magnitude:** 124.94 | **LOC:** 75 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9995%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 88.0), `CubotLeg` (Impact: 3.1), `getId` (Impact: 3.1)

### 8. `Server/src/main/typescript/GameClient.ts` (TYPESCRIPT) -> Cumulative Risk: **857.16**
- **Archetype:** `file_cluster_8` (Distance: 12.734 IQR)
- **Magnitude:** 46.3 | **LOC:** 499 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `handle` (Impact: 75.6), `connectToGameServer` (Impact: 45.5), `getServerInfo` (Impact: 27.1)

### 9. `Server/src/main/java/net/simon987/server/assembly/instruction/ShrInstruction.java` (JAVA) -> Cumulative Risk: **855.31**
- **Archetype:** `file_cluster_13` (Distance: 11.654 IQR)
- **Magnitude:** 45.08 | **LOC:** 67 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `execute` (Impact: 10.8), `execute` (Impact: 9.8), `ShrInstruction` (Impact: 2.7)

### 10. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotFloppyDrive.java` (JAVA) -> Cumulative Risk: **849.23**
- **Archetype:** `file_cluster_13` (Distance: 10.825 IQR)
- **Magnitude:** 142.58 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9955%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 96.1), `CubotFloppyDrive` (Impact: 10.8), `CubotFloppyDrive` (Impact: 3.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.3 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.627 IQR)
- **Top Global Matches:** file_cluster_11: 15.3, file_cluster_13: 15.51, file_cluster_8: 15.528
- **Magnitude:** 15141.56 | **LOC:** 19384 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 360
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (16.9738%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 6149.7 | O(2^N) | DB: 360)
  * `define` (Impact: 2153.5 | O(N^6) | DB: 106)
  * `define` (Impact: 1456.4 | O(N^6) | DB: 25)
  * `define` (Impact: 358.2 | O(N^4) | DB: 22)
  * `define` (Impact: 340.2 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1516`, `structural_boundaries: 1142`, `args: 539`, `func_start: 571`
* *Risk/State:* `safety_bypasses: 266`, `high_risk_execution: 2`, `state_mutation: 3891`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 18`, `api: 159`, `concurrency: 85`, `import: 52`
* *Defense:* `safety: 201`, `doc: 5`, `immutability_locks: 7`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dragdrop_handler, oop, selection, multi_select_handler, dom, fixoldbrowsers, folding, useragent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_15` (Drift: 16.231 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.263 IQR)
- **Top Global Matches:** file_cluster_15: 16.231, file_cluster_11: 16.327, file_cluster_8: 16.452
- **Magnitude:** 3958.46 | **LOC:** 4447 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 542
- **Risk Profile:** Cognitive Load (47.4202%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Isometric` (Impact: 2857.8 | O(2^N) | DB: 542)
    * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 77`, `args: 71`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1086`
* *Architecture:* None
* *Defense:* `safety: 72`, `doc: 263`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.701 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.052 IQR)
- **Top Global Matches:** file_cluster_8: 13.701, file_cluster_11: 13.782, file_cluster_15: 13.91
- **Magnitude:** 3434.6 | **LOC:** 1946 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 119
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.3681%)
**Top Internal Functions/Classes:**
  * `MarGame` (Impact: 125.8 | O(N^6) | DB: 26)
  * `handle` (Impact: 90.8 | O(N^5) | DB: 1)
  * `handleObjectsUpdate` (Impact: 86.8 | O(N^6) | DB: 18)
  * `updateObject` (Impact: 85.2 | O(N^5) | DB: 27)
  * `initialiseAnimations` (Impact: 81.4 | O(N^3) | DB: 119)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 265`, `args: 236`, `func_start: 207`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 1300`, `duplicate_logic: 57`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `concurrency: 4`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/ace/ext-searchbox.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.83 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.521 IQR)
- **Top Global Matches:** file_cluster_8: 12.83, file_cluster_13: 13.137, file_cluster_15: 13.184
- **Magnitude:** 913.46 | **LOC:** 511 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (72.7519%), Tech Debt (10.0997%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 567.9 | O(N^6) | DB: 151)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 50`, `args: 48`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 327`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` event, lang, hash_handler, keys, dom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/editor.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.696 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.696 IQR)
- **Top Global Matches:** file_cluster_8: 12.696, file_cluster_17: 12.768, file_cluster_2: 12.891
- **Magnitude:** 794.58 | **LOC:** 572 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (77.1595%), Tech Debt (9.3451%)
**Top Internal Functions/Classes:**
  * `parseInstruction` (Impact: 181.6 | O(N^6) | DB: 19)
  * `getOperandType` (Impact: 125.4 | O(N^4) | DB: 5)
  * `parseDWInstruction` (Impact: 121.8 | O(N^6) | DB: 6)
  * `checkForORGInstruction` (Impact: 49.5 | O(N^5) | DB: 4)
  * `checkForEQUInstruction` (Impact: 41.2 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 69`, `args: 18`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 154`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 3`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.466
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002506
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/Assembler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.402 IQR)
- **Top Global Matches:** file_cluster_8: 11.402, file_cluster_13: 11.507, file_cluster_7: 11.671
- **Magnitude:** 768.12 | **LOC:** 607 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.4777%), Tech Debt (85.7604%)
**Top Internal Functions/Classes:**
  * `parseDWInstruction` (Impact: 215.5 | O(N^6))
    * *Intent:* /** * Check for labels in a line and save it * * @param line Line to check * @param result Current a...
  * `parseInstruction` (Impact: 161.8 | O(N^6))
  * `parseDUPOperator16` (Impact: 62.5 | O(N^5))
  * `encodeInstructions` (Impact: 62.2 | O(N^5) | DB: 3)
    * *Intent:* /** * Check for and handle the EQU instruction *
  * `checkForEQUInstruction` (Impact: 54.8 | O(N^5) | DB: 1)
    * *Intent:* //Label value is casted to byte
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 68`, `args: 19`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 15`, `duplicate_logic: 5`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 24`, `doc: 54`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.412
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.005013
  * `Imports (Out-Degree: 2):` net.simon987.server.assembly.exception.*, java.util.HashMap, java.util.regex.Pattern, org.apache.commons.text.StringEscapeUtils, java.io.DataOutputStream, java.nio.charset.StandardCharsets, net.simon987.server.logging.LogManager, java.io.IOException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.264 IQR)
- **Top Global Matches:** file_cluster_0: 12.264, file_cluster_13: 12.297, file_cluster_4: 12.439
- **Magnitude:** 663.3 | **LOC:** 340 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (81.5746%), Tech Debt (99.995%)
**Top Internal Functions/Classes:**
  * `jsonSerialise` (Impact: 61.0 | O(2^N) | DB: 5)
  * `setParent` (Impact: 45.0 | O(2^N) | DB: 2)
  * `getParent` (Impact: 40.3 | O(2^N))
  * `getFloppyData` (Impact: 40.3 | O(2^N))
  * `getConsoleMode` (Impact: 40.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 85`, `args: 38`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 89`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 30`, `concurrency: 16`, `import: 15`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` net.simon987.server.GameServer, java.util.Map, java.util.ArrayList, net.simon987.server.game.objects.Direction, net.simon987.server.game.item.Item, net.simon987.server.assembly.*, net.simon987.server.game.objects.ControllableUnit, org.bson.Document...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/world/World.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.012 IQR)
- **Top Global Matches:** file_cluster_13: 11.012, file_cluster_8: 11.193, file_cluster_16: 11.305
- **Magnitude:** 610.06 | **LOC:** 443 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (14.0635%), Tech Debt (35.4605%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 109.0 | O(2^N))
  * `getMapInfo` (Impact: 71.1 | O(2^N))
  * `getRandomTileWithAdjacent` (Impact: 43.9 | O(N^6))
  * `getRandomPassableTile` (Impact: 31.2 | O(N^5))
  * `getNeighbouringLoadedWorlds` (Impact: 31.1 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 65`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `api: 41`, `import: 15`
* *Defense:* `safety: 2`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.422
  * `Choke Point (Betweenness):` 0.006284 | `Ripple Effect (Closeness):` 0.152129
  * `Imports (Out-Degree: 8):` net.simon987.server.GameServer, org.bson.types.ObjectId, java.util.ArrayList, org.bson.Document, net.simon987.server.game.GameUniverse, java.util.concurrent.ConcurrentHashMap, net.simon987.server.game.objects.Updatable, java.util.List...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/GameServer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.565 IQR)
- **Top Global Matches:** file_cluster_13: 10.565, file_cluster_8: 10.739, file_cluster_0: 11.138
- **Magnitude:** 606.86 | **LOC:** 351 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (43.9993%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `save` (Impact: 241.4 | O(2^N) | DB: 3)
  * `tick` (Impact: 122.0 | O(2^N))
  * `load` (Impact: 80.0 | O(2^N) | DB: 2)
  * `run` (Impact: 31.4 | O(N^5))
  * `GameServer` (Impact: 24.8 | O(N^4) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 82`, `args: 17`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 34`
* *Architecture:* `api: 28`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.741
  * `Choke Point (Betweenness):` 0.02293 | `Ripple Effect (Closeness):` 0.218379
  * `Imports (Out-Degree: 16):` net.simon987.server.event.GameEventDispatcher, net.simon987.server.user.User, net.simon987.server.logging.LogManager, com.mongodb.MongoClientException, net.simon987.server.plugin.ServerPlugin, net.simon987.server.game.objects.GameRegistry, net.simon987.server.crypto.SecretKeyGenerator, com.mongodb.client.*...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.628 IQR)
- **Top Global Matches:** file_cluster_13: 11.628, file_cluster_0: 11.677, file_cluster_8: 11.791
- **Magnitude:** 605.1 | **LOC:** 606 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (28.7569%), Tech Debt (25.1327%)
**Top Internal Functions/Classes:**
  * `jsonSerialise` (Impact: 51.1 | O(2^N) | DB: 7)
  * `toString` (Impact: 40.5 | O(2^N))
  * `detachHardware` (Impact: 34.1 | O(N^4) | DB: 2)
  * `mongoSerialise` (Impact: 33.4 | O(2^N) | DB: 9)
  * `reset` (Impact: 24.8 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 113`, `args: 51`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 80`, `duplicate_logic: 2`
* *Architecture:* `api: 87`, `import: 16`
* *Defense:* `doc: 20`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.329
  * `Choke Point (Betweenness):` 0.000628 | `Ripple Effect (Closeness):` 0.015038
  * `Imports (Out-Degree: 13):` net.simon987.server.game.item.Item, net.simon987.server.user.User, net.simon987.server.game.objects.*, net.simon987.server.game.item.ItemVoid, net.simon987.server.assembly.Status, net.simon987.server.GameServer, net.simon987.cubotplugin.event.DeathEvent, net.simon987.server.assembly.exception.CancelledException...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/CPU.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.007 IQR)
- **Top Global Matches:** file_cluster_8: 11.007, file_cluster_13: 11.032, file_cluster_7: 11.355
- **Magnitude:** 491.38 | **LOC:** 470 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (48.86%), Tech Debt (76.731%)
**Top Internal Functions/Classes:**
  * `executeInstruction` (Impact: 142.3 | O(N^6))
    * *Intent:* /*
  * `executeSourceIsRegister` (Impact: 67.7 | O(N^5))
  * `executeImmediateValueMem` (Impact: 67.7 | O(N^5))
  * `execute` (Impact: 36.0 | O(N^5) | DB: 1)
  * `CPU` (Impact: 9.0 | O(N^3) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 101`, `args: 22`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 64`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 34`, `import: 10`
* *Defense:* `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.915
  * `Choke Point (Betweenness):` 0.009451 | `Ripple Effect (Closeness):` 0.127731
  * `Imports (Out-Degree: 9):` net.simon987.server.GameServer, net.simon987.server.event.CpuInitialisationEvent, net.simon987.server.game.objects.HardwareHost, org.bson.Document, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.assembly.instruction.*, net.simon987.server.assembly.exception.CancelledException, net.simon987.server.io.MongoSerializable...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.356 IQR)
- **Top Global Matches:** file_cluster_13: 10.356, file_cluster_8: 10.776, file_cluster_16: 10.956
- **Magnitude:** 455.72 | **LOC:** 174 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (34.6058%), Tech Debt (78.8648%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 237.5 | O(2^N) | DB: 9)
  * `initWithDependencies` (Impact: 81.4 | O(2^N))
  * `loadInFolder` (Impact: 72.0 | O(N^6) | DB: 14)
    * *Intent:* /** * Load all plugins in plugins folder, if it doesn't exist, create it * * @return true if all the...
  * `getPluginByName` (Impact: 17.8 | O(N^4))
  * `getPluginByName` (Impact: 6.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 39`, `args: 10`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 17`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 7`, `import: 14`
* *Defense:* `safety: 5`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.259
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.138158
  * `Imports (Out-Degree: 2):` net.simon987.server.GameServer, java.io.InputStream, java.util.ArrayList, java.util.Properties, java.util.List, java.net.URL, java.net.URLClassLoader, net.simon987.server.logging.LogManager...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/Operand.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.912 IQR)
- **Top Global Matches:** file_cluster_8: 9.912, file_cluster_7: 10.196, file_cluster_13: 10.336
- **Magnitude:** 425.12 | **LOC:** 277 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (10.9533%), Tech Debt (98.0358%)
**Top Internal Functions/Classes:**
  * `Operand` (Impact: 190.6 | O(2^N) | DB: 1)
  * `parseRegExpr` (Impact: 123.7 | O(N^5))
    * *Intent:* /**
  * `parseImmediate` (Impact: 41.5 | O(N^5))
  * `parseLabel` (Impact: 20.8 | O(N^3))
    * *Intent:* /** * Attempt to parse an integer *
  * `parseReg` (Impact: 11.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 30`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 10`, `doc: 24`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.736
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.005013
  * `Imports (Out-Degree: 1):` java.util.HashMap, net.simon987.server.assembly.exception.InvalidOperandException
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.906 IQR)
- **Top Global Matches:** file_cluster_13: 10.906, file_cluster_8: 11.052, file_cluster_7: 11.176
- **Magnitude:** 412.18 | **LOC:** 342 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.5295%), Tech Debt (76.0053%)
**Top Internal Functions/Classes:**
  * `setcc` (Impact: 180.6 | O(N^4))
  * `encode` (Impact: 33.5 | O(N^3))
  * `seta` (Impact: 9.3 | O(N^2))
    * *Intent:* /** * Encodes the instruction. Writes the result in the outputStream. * Needs one operand of Operand...
  * `setae` (Impact: 9.3 | O(N^2))
    * *Intent:* // This will catch the off case that someone uses the mnemonic 'setcc'
  * `setbe` (Impact: 9.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 53`, `args: 36`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 22`, `import: 12`
* *Defense:* `doc: 21`, `sync_locks: 28`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.util.Map, java.util.HashMap, net.simon987.server.assembly.exception.InvalidMnemonicException, net.simon987.server.assembly.exception.IllegalOperandException, net.simon987.server.assembly.OperandType, net.simon987.server.assembly.Instruction, java.io.ByteArrayOutputStream, net.simon987.server.assembly.Status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/test/java/net/simon987/server/assembly/OperandTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.121 IQR)
- **Top Global Matches:** file_cluster_8: 13.121, file_cluster_13: 13.137, file_cluster_0: 13.333
- **Magnitude:** 365.08 | **LOC:** 154 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (33.5276%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Operand` (Impact: 350.8 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 48`, `args: 1`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 42`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.util.HashMap, net.simon987.server.assembly.exception.InvalidOperandException, org.junit.Assert.fail, org.junit.Assert.assertEquals, org.junit.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.13 IQR)
- **Top Global Matches:** file_cluster_13: 10.13, file_cluster_8: 10.166, file_cluster_7: 10.498
- **Magnitude:** 362.36 | **LOC:** 276 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.9382%), Tech Debt (57.6638%)
**Top Internal Functions/Classes:**
  * `incrementLocation` (Impact: 141.1 | O(N^5) | DB: 1)
    * *Intent:* /** * Current World of the object */
  * `getAdjacentTile` (Impact: 36.9 | O(N^3))
  * `getAdjacentTileCount` (Impact: 34.6 | O(N^5))
    * *Intent:* /** * Get the first directly adjacent tile (starting east, going clockwise) */
  * `getFrontTile` (Impact: 28.6 | O(N^3))
  * `setObjectId` (Impact: 3.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 56`, `args: 26`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 40`, `import: 9`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.76
  * `Choke Point (Betweenness):` 0.004298 | `Ripple Effect (Closeness):` 0.133723
  * `Imports (Out-Degree: 5):` net.simon987.server.GameServer, org.bson.types.ObjectId, java.util.ArrayList, org.bson.Document, net.simon987.server.io.JSONSerializable, org.json.simple.JSONObject, net.simon987.server.io.MongoSerializable, java.awt.*...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/phaser.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.994 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.264 IQR)
- **Top Global Matches:** file_cluster_8: 12.994, file_cluster_7: 13.564, file_cluster_0: 13.668
- **Magnitude:** 351.22 | **LOC:** 7686 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (21.3014%), Tech Debt (24.985%)
**Top Internal Functions/Classes:**
  * `updateTexture` (Impact: 1281.7 | O(N^4) | DB: 3)
  * `update` (Impact: 275.1 | O(2^N))
  * `timer` (Impact: 212.9 | O(2^N))
  * `updateRender` (Impact: 145.6 | O(N^2))
  * `update` (Impact: 95.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1711`, `structural_boundaries: 348`, `args: 2061`, `func_start: 2070`, `class_start: 181`
* *Risk/State:* `safety_bypasses: 731`, `state_mutation: 43`, `duplicate_logic: 21`, `orphaned_logic: 19`
* *Architecture:* `io: 8`, `api: 4`
* *Defense:* `safety: 792`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.197 IQR)
- **Top Global Matches:** file_cluster_13: 10.197, file_cluster_8: 10.449, file_cluster_0: 10.706
- **Magnitude:** 329.96 | **LOC:** 135 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (76.4459%), Tech Debt (99.3484%)
**Top Internal Functions/Classes:**
  * `handleInterrupt` (Impact: 294.2 | O(N^6) | DB: 6)
  * `CubotLidar` (Impact: 3.1 | O(N^2))
  * `getId` (Impact: 3.1 | O(N^2))
  * `CubotLidar` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 13`, `args: 4`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 18`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.util.ArrayList, org.bson.Document, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.assembly.Memory, net.simon987.server.game.pathfinding.Node, net.simon987.server.game.pathfinding.Pathfinder, net.simon987.server.assembly.HardwareModule, net.simon987.server.assembly.Status
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/HarvestTask.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.958 IQR)
- **Top Global Matches:** file_cluster_13: 8.958, file_cluster_8: 9.263, file_cluster_0: 9.511
- **Magnitude:** 299.06 | **LOC:** 108 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (9.712%), Tech Debt (96.9302%)
**Top Internal Functions/Classes:**
  * `tick` (Impact: 284.9 | O(2^N) | DB: 1)
    * *Intent:* /**
  * `checkCompleted` (Impact: 3.1 | O(N^2))
  * `HarvestTask` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 3`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.util.ArrayList, net.simon987.server.game.objects.Direction, net.simon987.server.game.objects.GameObject, net.simon987.server.logging.LogManager, net.simon987.server.game.objects.InventoryHolder, net.simon987.server.assembly.Util, java.util.Random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/GameUniverse.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.039 IQR)
- **Top Global Matches:** file_cluster_13: 11.039, file_cluster_8: 11.414, file_cluster_16: 11.587
- **Magnitude:** 289.56 | **LOC:** 293 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.1831%), Tech Debt (95.0943%)
**Top Internal Functions/Classes:**
  * `getOrCreateUser` (Impact: 43.1 | O(N^5) | DB: 1)
  * `getObject` (Impact: 28.7 | O(N^4))
  * `getWorld` (Impact: 23.9 | O(N^3))
  * `getGuestUsername` (Impact: 20.8 | O(N^4))
  * `loadWorld` (Impact: 12.8 | O(N^3) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 57`, `args: 25`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 28`, `duplicate_logic: 4`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 4`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.628
  * `Choke Point (Betweenness):` 0.004005 | `Ripple Effect (Closeness):` 0.145195
  * `Imports (Out-Degree: 8):` net.simon987.server.GameServer, net.simon987.server.game.world.WorldGenerator, org.bson.types.ObjectId, org.bson.Document, java.util.concurrent.ConcurrentHashMap, com.mongodb.client.MongoCursor, net.simon987.server.game.objects.GameObject, net.simon987.server.assembly.exception.CancelledException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/objects/GameRegistry.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.328 IQR)
- **Top Global Matches:** file_cluster_13: 11.328, file_cluster_8: 11.563, file_cluster_16: 11.622
- **Magnitude:** 286.32 | **LOC:** 150 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (31.1179%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deserializeGameObject` (Impact: 51.4 | O(N^4))
  * `deserializeItem` (Impact: 51.4 | O(N^4))
  * `makeItem` (Impact: 41.0 | O(N^5))
    * *Intent:* /**
  * `makeTile` (Impact: 41.0 | O(N^5))
  * `deserializeHardware` (Impact: 32.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 47`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 12`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 12`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.256
  * `Choke Point (Betweenness):` 0.001795 | `Ripple Effect (Closeness):` 0.141775
  * `Imports (Out-Degree: 4):` java.lang.reflect.InvocationTargetException, org.bson.Document, net.simon987.server.game.item.Item, java.util.HashMap, net.simon987.server.logging.LogManager, net.simon987.server.assembly.HardwareModule, net.simon987.server.game.world.Tile
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/websocket/SocketServer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.974 IQR)
- **Top Global Matches:** file_cluster_13: 10.974, file_cluster_0: 11.359, file_cluster_8: 11.364
- **Magnitude:** 278.56 | **LOC:** 187 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (34.1121%), Tech Debt (20.2268%)
**Top Internal Functions/Classes:**
  * `onMessage` (Impact: 88.3 | O(2^N))
  * `tick` (Impact: 73.3 | O(2^N) | DB: 4)
    * *Intent:* /**
  * `sendString` (Impact: 21.1 | O(2^N))
  * `sendJSONObject` (Impact: 14.3 | O(N^3))
  * `charArraysToJSON` (Impact: 13.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 45`, `args: 12`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 25`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.45
  * `Choke Point (Betweenness):` 0.002266 | `Ripple Effect (Closeness):` 0.138866
  * `Imports (Out-Degree: 5):` net.simon987.server.GameServer, org.eclipse.jetty.websocket.api.annotations.OnWebSocketClose, net.simon987.server.web.GuestPolicy, org.json.simple.JSONArray, java.util.ArrayList, org.eclipse.jetty.websocket.api.Session, net.simon987.server.game.objects.ControllableUnit, java.util.List...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.409 IQR)
- **Top Global Matches:** file_cluster_13: 11.409, file_cluster_11: 11.622, file_cluster_0: 11.678
- **Magnitude:** 263.36 | **LOC:** 131 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `handleInterrupt` (Impact: 215.8 | O(N^6) | DB: 10)
  * `CubotComPort` (Impact: 3.1 | O(N^2))
  * `getId` (Impact: 3.1 | O(N^2))
  * `CubotComPort` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 17`, `args: 4`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 30`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.util.ArrayList, org.bson.Document, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.game.objects.GameObject, net.simon987.server.assembly.HardwareModule, net.simon987.server.assembly.Status, java.awt.*, net.simon987.server.game.objects.MessageReceiver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/RegisterSet.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.8 IQR)
- **Top Global Matches:** file_cluster_13: 11.8, file_cluster_8: 12.153, file_cluster_0: 12.168
- **Magnitude:** 241.38 | **LOC:** 212 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.6173%), Tech Debt (99.8739%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 35.1 | O(2^N) | DB: 1)
  * `get` (Impact: 27.4 | O(2^N))
  * `getRegister` (Impact: 23.0 | O(N^4))
  * `getIndex` (Impact: 20.6 | O(N^4))
    * *Intent:* /** * Create an empty Register set
  * `deserialize` (Impact: 15.5 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 29`, `duplicate_logic: 4`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.432
  * `Choke Point (Betweenness):` 0.000482 | `Ripple Effect (Closeness):` 0.065163
  * `Imports (Out-Degree: 2):` java.util.ArrayList, org.json.simple.JSONArray, org.bson.Document, java.util.HashMap, java.util.List, org.json.simple.JSONObject, net.simon987.server.io.MongoSerializable, net.simon987.server.logging.LogManager
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.232 IQR)
- **Top Global Matches:** file_cluster_13: 11.232, file_cluster_8: 11.586, file_cluster_7: 11.901
- **Magnitude:** 209.4 | **LOC:** 262 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (41.0816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VaultDimension` (Impact: 172.7 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` net.simon987.server.GameServer, net.simon987.npcplugin.world.TileVaultFloor, org.bson.types.ObjectId, net.simon987.server.game.world.Location, java.util.ArrayList, net.simon987.server.game.objects.Direction, java.util.HashMap, java.util.Random...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA) | Magnitude: 663.3 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 241, state_mutation: 89, structural_boundaries: 85, branch: 48
- `Plugin NPC/src/main/java/net/simon987/npcplugin/Obstacle.java` (JAVA) | Magnitude: 84.76 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 20, func_start: 16, api: 16
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/ItemBluePrint.java` (JAVA) | Magnitude: 56.42 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 14, func_start: 9, api: 9
- `Server/src/test/java/net/simon987/server/FakeConfiguration.java` (JAVA) | Magnitude: 29.58 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, api: 10, structural_boundaries: 9, args: 5
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/Obstacle.java` (JAVA) | Magnitude: 82.94 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 22, func_start: 18, api: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT) | Magnitude: 15141.56 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5118, state_mutation: 3891, branch: 1516, structural_boundaries: 1142

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Server/src/main/java/net/simon987/server/assembly/instruction/XchgInstruction.java` (JAVA) | Magnitude: 11.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, api: 4, import: 4
- `Server/src/main/java/net/simon987/server/game/objects/ItemsContainer.java` (JAVA) | Magnitude: 63.54 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 18, args: 10, func_start: 9
- `Server/src/main/java/net/simon987/server/event/WorldGenerationEvent.java` (JAVA) | Magnitude: 11.4 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 4, func_start: 3
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetgInstructionTest.java` (JAVA) | Magnitude: 29.56 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 18, structural_boundaries: 12, func_start: 7
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetnleInstructionTest.java` (JAVA) | Magnitude: 29.56 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 18, structural_boundaries: 12, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT) | Magnitude: 3958.46 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1086, indent_spaces: 672, doc: 263, branch: 199

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Server/src/main/java/net/simon987/server/user/UserStatsHelper.java` (JAVA) | Magnitude: 41.3 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 25, state_mutation: 19, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Server/src/main/java/net/simon987/server/Main.java` (JAVA) | Magnitude: 13.8 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, concurrency: 6, import: 3
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` (JAVA) | Magnitude: 49.58 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, state_mutation: 14, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Server/src/main/java/net/simon987/server/assembly/InstructionSet.java` (JAVA) | Magnitude: 25.12 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 3, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Server/src/main/java/net/simon987/server/assembly/AssemblyResult.java` (JAVA) | Magnitude: 75.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 20, doc: 16, branch: 10
- `Server/src/main/java/net/simon987/server/websocket/MessageHandler.java` (JAVA) | Magnitude: 18.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, args: 1, func_start: 1
- `Server/src/main/java/net/simon987/server/game/world/Tile.java` (JAVA) | Magnitude: 18.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, api: 8, structural_boundaries: 7, doc: 7
- `Server/src/main/java/net/simon987/server/game/world/WorldGenerator.java` (JAVA) | Magnitude: 167.22 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 25, branch: 21, encapsulation: 15
- `Server/src/test/java/net/simon987/server/assembly/OperandTest.java` (JAVA) | Magnitude: 365.08 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, func_start: 56, test: 55, structural_boundaries: 48

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 2.161** (Bridge: 0.0229 * Flux: 94.234%)
- `Server/src/main/java/net/simon987/server/assembly/CPU.java` -> **Severity: 0.944** (Bridge: 0.0095 * Flux: 99.9212%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 0.611** (Bridge: 0.0063 * Flux: 97.1573%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 0.391** (Bridge: 0.004 * Flux: 97.6344%)
- `Server/src/main/java/net/simon987/server/user/User.java` -> **Severity: 0.329** (Bridge: 0.0034 * Flux: 97.9164%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 17.011** (Embedded: 0.23 * Error Risk: 73.9707%)
- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 16.816** (Embedded: 0.2184 * Error Risk: 77.0057%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 13.023** (Embedded: 0.1452 * Error Risk: 89.6928%)
- `Server/src/main/java/net/simon987/server/user/User.java` -> **Severity: 12.967** (Embedded: 0.1574 * Error Risk: 82.3665%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 12.401** (Embedded: 0.1521 * Error Risk: 81.5191%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Server/src/main/java/net/simon987/server/ServerConfiguration.java` -> **Severity: 8927.1** (Blast Radius: 89.271 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 8558.966** (Blast Radius: 103.863 * Doc Risk: 82.4063%)
- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 3473.176** (Blast Radius: 34.741 * Doc Risk: 99.9734%)
- `Server/src/main/java/net/simon987/server/assembly/Status.java` -> **Severity: 2823.094** (Blast Radius: 28.231 * Doc Risk: 99.9998%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 1542.195** (Blast Radius: 15.422 * Doc Risk: 99.9997%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
