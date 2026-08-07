# ARCHITECTURAL_BRIEF: Much-Assembly-Required
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/Much-Assembly-Required` |
| **Timestamp** | `2026-08-07T03:49:01.843919+00:00` |
| **Scan Duration** | `1.95s` |
| **Git Branch** | `master` |
| **Git Commit** | `ac374f5b525615da3ecb36b08cc5fc53ab73dc96` |
| **Git Remote** | `https://github.com/simon987/Much-Assembly-Required.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 379 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.656`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 197 | 49.2% |
| file_cluster_13 | 181 | 45.2% |
| file_cluster_0 | 8 | 2.0% |
| file_cluster_4 | 1 | 0.2% |
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
| Error & Exception Exposure | 0.0 | 100.0 | 46.8 | 55.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 47.6 | 28.8 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.7 | 2.4 | 0.0 |
| API Exposure | 0.0 | 13.7 | 6.6 | 6.9 | 8.6 |
| Concurrency Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.3 | 13.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.2 | 47.6 | 0.0 |
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

- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **685.5** | LOC: 1429
- `escapeHTML` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **594.4** | LOC: 1392
- `updateTexture` (@ `Server/src/main/typescript/phaser.d.ts`) -> Impact: **540.7** | LOC: 934
- `IsoSprite` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **476.7** | LOC: 1068
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **463.1** | LOC: 701
- `Isometric` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **457.9** | LOC: 1157
  * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
- `constructor` (@ `Server/src/main/typescript/phaser.d.ts`) -> Impact: **330.6** | LOC: 220
- `define` (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **277.6** | LOC: 351
- `preUpdate` (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **213.0** | LOC: 623
- `addIsoSprite` (@ `Server/src/main/typescript/phaser.plugin.isometric.d.ts`) -> Impact: **211.2** | LOC: 361

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Server/src/main/resources/static/js/ace` | 40 | 8760.62 | 5.91% | 28.58% |
| `Server/src/main/resources/static/js` | 3 | 5610.44 | 77.02% | 92.55% |
| `Plugin NPC/src/main/java/net/simon987/npcplugin` | 21 | 1548.68 | 27.26% | 82.5% |
| `Server/src/main/java/net/simon987/server/assembly` | 18 | 1476.62 | 12.39% | 49.27% |
| `Server/src/main/java/net/simon987/server/assembly/instruction` | 76 | 1348.5 | 16.48% | 60.5% |
| `Plugin Cubot/src/main/java/net/simon987/cubotplugin` | 17 | 1284.32 | 36.25% | 89.29% |
| `Server/src/main/java/net/simon987/server/game/objects` | 15 | 803.17 | 10.01% | 19.98% |
| `Server/src/main/typescript` | 11 | 762.59 | 31.8% | 84.93% |
| `Server/src/main/java/net/simon987/server/game/world` | 13 | 567.54 | 7.11% | 52.18% |
| `Server/src/test/java/net/simon987/server/assembly/instruction` | 31 | 552.62 | 17.66% | 0.0% |

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
- `Server/src/main/typescript/phaser.d.ts` -> **54** Orphaned Functions | **90** Duplicates
- `Server/src/main/resources/static/js/mar.js` -> **13** Orphaned Functions | **64** Duplicates
- `Server/src/main/resources/static/js/ace/ace.js` -> **21** Orphaned Functions | **50** Duplicates
- `Server/src/main/resources/static/js/phaser-plugin-isometric.js` -> **28** Orphaned Functions | **18** Duplicates
- `Server/src/main/typescript/p2.d.ts` -> **14** Orphaned Functions | **31** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1256` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA) -> Cumulative Risk: **749.86**
- **Archetype:** `file_cluster_0` (Distance: 12.221 IQR)
- **Magnitude:** 335.3 | **LOC:** 340 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9985%), Tech Debt (99.995%), Safety Score (97.2729%)
- **Heaviest Functions:** `detachHardware` (Impact: 15.3), `jsonSerialise` (Impact: 14.4), `setKeyboardBuffer` (Impact: 10.1)

### 2. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` (JAVA) -> Cumulative Risk: **662.78**
- **Archetype:** `file_cluster_13` (Distance: 11.256 IQR)
- **Magnitude:** 115.76 | **LOC:** 131 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.996%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 70.7), `getId` (Impact: 2.4), `CubotComPort` (Impact: 2.1)

### 3. `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA) -> Cumulative Risk: **640.15**
- **Archetype:** `file_cluster_13` (Distance: 10.679 IQR)
- **Magnitude:** 138.18 | **LOC:** 223 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9173%), Tech Debt (96.8788%), Safety Score (96.7586%)
- **Heaviest Functions:** `Settlement` (Impact: 40.5), `Settlement` (Impact: 13.4), `mongoSerialise` (Impact: 12.4)

### 4. `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT) -> Cumulative Risk: **630.68**
- **Archetype:** `file_cluster_11` (Distance: 15.226 IQR)
- **Magnitude:** 7672.26 | **LOC:** 19384 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.5178%)
- **Heaviest Functions:** `define` (Impact: 685.5), `escapeHTML` (Impact: 594.4), `define` (Impact: 463.1)

### 5. `Server/src/main/typescript/GameObject.ts` (TYPESCRIPT) -> Cumulative Risk: **629.14**
- **Archetype:** `file_cluster_8` (Distance: 13.159 IQR)
- **Magnitude:** 85.45 | **LOC:** 889 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8247%)
- **Heaviest Functions:** `updateHologram` (Impact: 28.5), `createObject` (Impact: 27.4), `updateObject` (Impact: 25.7)

### 6. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotInventory.java` (JAVA) -> Cumulative Risk: **628.4**
- **Archetype:** `file_cluster_13` (Distance: 10.584 IQR)
- **Magnitude:** 122.52 | **LOC:** 143 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9996%), State Flux (99.7273%), Documentation (97.2249%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 30.8), `toString` (Impact: 9.3), `mongoSerialise` (Impact: 7.6)

### 7. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` (JAVA) -> Cumulative Risk: **626.17**
- **Archetype:** `file_cluster_13` (Distance: 10.055 IQR)
- **Magnitude:** 128.56 | **LOC:** 135 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.3484%), State Flux (97.8888%), Documentation (84.5938%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 95.3), `getId` (Impact: 2.4), `CubotLidar` (Impact: 2.1)

### 8. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotFloppyDrive.java` (JAVA) -> Cumulative Risk: **624.27**
- **Archetype:** `file_cluster_13` (Distance: 10.674 IQR)
- **Magnitude:** 77.28 | **LOC:** 93 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), State Flux (99.9316%), Safety Score (89.3649%)
- **Heaviest Functions:** `handleInterrupt` (Impact: 36.5), `CubotFloppyDrive` (Impact: 5.6), `getId` (Impact: 2.4)

### 9. `Server/src/main/java/net/simon987/server/game/GameUniverse.java` (JAVA) -> Cumulative Risk: **610.96**
- **Archetype:** `file_cluster_13` (Distance: 11.011 IQR)
- **Magnitude:** 179.66 | **LOC:** 293 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9944%), State Flux (97.6344%), Documentation (96.0086%)
- **Heaviest Functions:** `getOrCreateUser` (Impact: 15.4), `getObject` (Impact: 11.9), `getGuestUsername` (Impact: 8.8)

### 10. `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT) -> Cumulative Risk: **603.56**
- **Archetype:** `file_cluster_8` (Distance: 13.71 IQR)
- **Magnitude:** 2404.9 | **LOC:** 1946 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8374%)
- **Heaviest Functions:** `initialiseAnimations` (Impact: 43.3), `MarGame` (Impact: 39.2), `alert` (Impact: 32.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.226 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.727 IQR)
- **Top Global Matches:** file_cluster_11: 15.226, file_cluster_13: 15.434, file_cluster_8: 15.454
- **Magnitude:** 7672.26 | **LOC:** 19384 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (87.1885%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 685.5)
  * `escapeHTML` (Impact: 594.4)
  * `define` (Impact: 463.1)
  * `define` (Impact: 277.6)
  * `define` (Impact: 109.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1516`, `structural_boundaries: 1142`, `args: 539`, `func_start: 571`
* *Risk/State:* `safety_bypasses: 266`, `high_risk_execution: 2`, `state_mutation: 3879`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 50`, `orphaned_logic: 21`
* *Architecture:* `io: 18`, `api: 159`, `concurrency: 85`, `import: 52`
* *Defense:* `safety: 201`, `doc: 5`, `immutability_locks: 7`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fold_handler, tooltip, editor, event_emitter, text, behaviour, dom, placeholder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_15` (Drift: 16.223 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.502 IQR)
- **Top Global Matches:** file_cluster_15: 16.223, file_cluster_11: 16.313, file_cluster_8: 16.441
- **Magnitude:** 2768.06 | **LOC:** 4447 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.9027%), Tech Debt (99.9462%)
**Top Internal Functions/Classes:**
  * `IsoSprite` (Impact: 476.7)
  * `Isometric` (Impact: 457.9)
    * *Intent:* /** * The MIT License (MIT) * Copyright (c) 2015 Lewis Lane
  * `preUpdate` (Impact: 213.0)
  * `separateY` (Impact: 68.8)
  * `computeVelocity` (Impact: 54.7)
    * *Intent:* /** * The axonometric position of the IsoSprite on the z axis. Increasing the z coordinate will move...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 77`, `args: 71`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1038`, `duplicate_logic: 18`, `orphaned_logic: 28`
* *Architecture:* None
* *Defense:* `safety: 72`, `doc: 263`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.71 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.141 IQR)
- **Top Global Matches:** file_cluster_8: 13.71, file_cluster_11: 13.783, file_cluster_15: 13.917
- **Magnitude:** 2404.9 | **LOC:** 1946 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.8374%)
**Top Internal Functions/Classes:**
  * `initialiseAnimations` (Impact: 43.3)
  * `MarGame` (Impact: 39.2)
  * `alert` (Impact: 32.5)
  * `handle` (Impact: 31.9)
  * `updateObject` (Impact: 29.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 265`, `args: 236`, `func_start: 207`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 7`, `state_mutation: 1302`, `duplicate_logic: 64`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `concurrency: 4`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/ace/ext-searchbox.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.563 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.734 IQR)
- **Top Global Matches:** file_cluster_8: 12.563, file_cluster_13: 12.877, file_cluster_15: 12.935
- **Magnitude:** 568.26 | **LOC:** 511 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.5564%), Tech Debt (90.0886%)
**Top Internal Functions/Classes:**
  * `define` (Impact: 111.3)
  * `updateCounter` (Impact: 22.4)
  * `init` (Impact: 19.7)
  * `setSearchRange` (Impact: 7.4)
  * `syncOptions` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 50`, `args: 48`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 321`, `duplicate_logic: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hash_handler, keys, dom, lang, event
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/editor.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.695 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.786 IQR)
- **Top Global Matches:** file_cluster_8: 12.695, file_cluster_17: 12.7, file_cluster_2: 12.88
- **Magnitude:** 437.48 | **LOC:** 572 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.1595%), Tech Debt (77.8775%)
**Top Internal Functions/Classes:**
  * `parseInstruction` (Impact: 56.5)
  * `getOperandType` (Impact: 52.6)
  * `parseDWInstruction` (Impact: 36.8)
  * `checkForORGInstruction` (Impact: 17.6)
  * `checkForEQUInstruction` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 69`, `args: 18`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 154`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 4`, `api: 5`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.466
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002506
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/phaser.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.01 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 13.01, file_cluster_7: 13.578, file_cluster_0: 13.671
- **Magnitude:** 419.6 | **LOC:** 7686 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.692%), Tech Debt (95.0978%)
**Top Internal Functions/Classes:**
  * `updateTexture` (Impact: 540.7)
  * `constructor` (Impact: 330.6)
  * `tween` (Impact: 153.9)
  * `updateBoundsCollisionGroup` (Impact: 146.6)
  * `setType` (Impact: 138.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1711`, `structural_boundaries: 348`, `args: 2072`, `func_start: 2070`, `class_start: 181`
* *Risk/State:* `safety_bypasses: 731`, `state_mutation: 43`, `duplicate_logic: 90`, `orphaned_logic: 54`
* *Architecture:* `io: 8`, `api: 4`
* *Defense:* `safety: 792`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.628 IQR)
- **Top Global Matches:** file_cluster_13: 11.628, file_cluster_0: 11.677, file_cluster_8: 11.795
- **Magnitude:** 383.5 | **LOC:** 606 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5584%), Tech Debt (57.8569%)
**Top Internal Functions/Classes:**
  * `detachHardware` (Impact: 15.3)
  * `jsonSerialise` (Impact: 12.4)
  * `toString` (Impact: 11.7)
  * `mongoSerialise` (Impact: 10.4)
    * *Intent:* /** * No specific client-side action */
  * `sendMessage` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 113`, `args: 51`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 80`, `duplicate_logic: 4`
* *Architecture:* `api: 87`, `import: 16`
* *Defense:* `doc: 20`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.329
  * `Choke Point (Betweenness):` 0.000628 | `Ripple Effect (Closeness):` 0.015038
  * `Imports (Out-Degree: 13):` java.awt.*, net.simon987.server.user.User, java.util.*, net.simon987.cubotplugin.event.CubotWalkEvent, net.simon987.server.assembly.Memory, java.util.List, org.bson.Document, net.simon987.server.game.item.Item...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.221 IQR)
- **Top Global Matches:** file_cluster_0: 12.221, file_cluster_13: 12.254, file_cluster_4: 12.397
- **Magnitude:** 335.3 | **LOC:** 340 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5746%), Tech Debt (99.995%)
**Top Internal Functions/Classes:**
  * `detachHardware` (Impact: 15.3)
  * `jsonSerialise` (Impact: 14.4)
  * `setKeyboardBuffer` (Impact: 10.1)
  * `setParent` (Impact: 10.1)
  * `update` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 85`, `args: 37`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 89`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 30`, `concurrency: 16`, `import: 15`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` net.simon987.server.GameServer, net.simon987.server.logging.LogManager, java.util.HashMap, java.util.List, org.bson.Document, net.simon987.server.user.User, net.simon987.server.game.objects.Direction, net.simon987.server.event.ObjectDeathEvent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/CPU.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.001 IQR)
- **Top Global Matches:** file_cluster_8: 11.001, file_cluster_13: 11.016, file_cluster_7: 11.348
- **Magnitude:** 274.18 | **LOC:** 470 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.9764%), Tech Debt (99.8968%)
**Top Internal Functions/Classes:**
  * `executeInstruction` (Impact: 42.4)
    * *Intent:* /*
  * `executeSourceIsRegister` (Impact: 23.6)
  * `executeImmediateValueMem` (Impact: 23.6)
  * `executeSourceIsRegister` (Impact: 14.7)
  * `execute` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 101`, `args: 22`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 64`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.915
  * `Choke Point (Betweenness):` 0.009451 | `Ripple Effect (Closeness):` 0.127731
  * `Imports (Out-Degree: 9):` net.simon987.server.logging.LogManager, net.simon987.server.event.GameEvent, net.simon987.server.assembly.exception.CancelledException, org.bson.Document, net.simon987.server.assembly.instruction.*, net.simon987.server.io.MongoSerializable, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.event.CpuInitialisationEvent...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/world/World.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.999 IQR)
- **Top Global Matches:** file_cluster_13: 10.999, file_cluster_8: 11.184, file_cluster_16: 11.297
- **Magnitude:** 264.56 | **LOC:** 443 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0635%), Tech Debt (78.6219%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 19.1)
  * `getMapInfo` (Impact: 15.1)
  * `getRandomTileWithAdjacent` (Impact: 13.6)
  * `getNeighbouringLoadedWorlds` (Impact: 13.1)
  * `getRandomPassableTile` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 65`, `args: 31`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 39`, `duplicate_logic: 4`
* *Architecture:* `api: 41`, `import: 15`
* *Defense:* `safety: 2`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.422
  * `Choke Point (Betweenness):` 0.006284 | `Ripple Effect (Closeness):` 0.152129
  * `Imports (Out-Degree: 8):` java.awt.*, net.simon987.server.game.objects.GameObject, net.simon987.server.event.GameEvent, net.simon987.server.game.pathfinding.Pathfinder, java.util.List, org.bson.Document, org.bson.types.ObjectId, java.util.Random...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/Assembler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.357 IQR)
- **Top Global Matches:** file_cluster_8: 11.357, file_cluster_13: 11.459, file_cluster_7: 11.627
- **Magnitude:** 256.72 | **LOC:** 607 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.4777%), Tech Debt (99.4685%)
**Top Internal Functions/Classes:**
  * `parseDWInstruction` (Impact: 58.2)
    * *Intent:* /** * Check for labels in a line and save it * * @param line Line to check * @param result Current a...
  * `parseInstruction` (Impact: 46.0)
  * `encodeInstructions` (Impact: 22.2)
    * *Intent:* /** * Check for and handle the EQU instruction *
  * `parseDUPOperator16` (Impact: 20.1)
  * `checkForEQUInstruction` (Impact: 17.1)
    * *Intent:* //Label value is casted to byte
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 68`, `args: 16`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 15`, `duplicate_logic: 9`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 24`, `doc: 54`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.412
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.005013
  * `Imports (Out-Degree: 2):` java.util.regex.Pattern, net.simon987.server.logging.LogManager, java.util.HashMap, net.simon987.server.assembly.exception.*, java.util.regex.Matcher, java.io.IOException, java.io.ByteArrayOutputStream, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.787 IQR)
- **Top Global Matches:** file_cluster_13: 10.787, file_cluster_8: 10.935, file_cluster_7: 11.061
- **Magnitude:** 242.38 | **LOC:** 342 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.5295%), Tech Debt (76.0053%)
**Top Internal Functions/Classes:**
  * `setcc` (Impact: 73.3)
  * `encode` (Impact: 17.6)
  * `seta` (Impact: 6.3)
    * *Intent:* /** * Encodes the instruction. Writes the result in the outputStream. * Needs one operand of Operand...
  * `setae` (Impact: 6.3)
    * *Intent:* // This will catch the off case that someone uses the mnemonic 'setcc'
  * `setbe` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 53`, `args: 21`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 22`, `import: 12`
* *Defense:* `doc: 21`, `sync_locks: 28`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` net.simon987.server.assembly.Status, java.util.HashMap, net.simon987.server.assembly.exception.AssemblyException, net.simon987.server.assembly.Target, net.simon987.server.assembly.MachineCode, java.io.ByteArrayOutputStream, net.simon987.server.assembly.exception.IllegalOperandException, net.simon987.server.assembly.OperandType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.089 IQR)
- **Top Global Matches:** file_cluster_13: 10.089, file_cluster_8: 10.135, file_cluster_7: 10.467
- **Magnitude:** 231.16 | **LOC:** 276 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4446%), Tech Debt (99.7341%)
**Top Internal Functions/Classes:**
  * `incrementLocation` (Impact: 49.1)
    * *Intent:* /** * Current World of the object */
  * `getAdjacentTile` (Impact: 18.9)
  * `setWorld` (Impact: 17.9)
    * *Intent:* /** * Increment the location of the game object by 1 tile * Collision checks happen here
  * `setY` (Impact: 14.8)
  * `getFrontTile` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 56`, `args: 25`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 40`, `import: 9`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.76
  * `Choke Point (Betweenness):` 0.004298 | `Ripple Effect (Closeness):` 0.133723
  * `Imports (Out-Degree: 5):` java.awt.*, org.bson.Document, org.bson.types.ObjectId, net.simon987.server.io.JSONSerializable, net.simon987.server.game.world.Tile, net.simon987.server.io.MongoSerializable, java.util.ArrayList, net.simon987.server.game.world.World...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/GameServer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.549 IQR)
- **Top Global Matches:** file_cluster_13: 10.549, file_cluster_8: 10.732, file_cluster_0: 11.122
- **Magnitude:** 199.96 | **LOC:** 351 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0078%), Tech Debt (36.3081%)
**Top Internal Functions/Classes:**
  * `save` (Impact: 37.4)
  * `tick` (Impact: 22.1)
  * `load` (Impact: 17.6)
  * `run` (Impact: 12.6)
  * `GameServer` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 82`, `args: 17`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 34`, `duplicate_logic: 2`
* *Architecture:* `api: 28`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.741
  * `Choke Point (Betweenness):` 0.02293 | `Ripple Effect (Closeness):` 0.218379
  * `Imports (Out-Degree: 16):` net.simon987.server.logging.LogManager, net.simon987.server.user.User, net.simon987.server.crypto.CryptoProvider, java.util.ArrayList, net.simon987.server.event.GameEventDispatcher, net.simon987.server.user.UserManager, net.simon987.server.plugin.ServerPlugin, net.simon987.server.game.item.ItemIron...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/GameUniverse.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.011 IQR)
- **Top Global Matches:** file_cluster_13: 11.011, file_cluster_8: 11.394, file_cluster_16: 11.568
- **Magnitude:** 179.66 | **LOC:** 293 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7844%), Tech Debt (99.9944%)
**Top Internal Functions/Classes:**
  * `getOrCreateUser` (Impact: 15.4)
  * `getObject` (Impact: 11.9)
  * `getGuestUsername` (Impact: 8.8)
  * `getWorld` (Impact: 8.7)
  * `loadWorld` (Impact: 6.8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 57`, `args: 24`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 28`, `duplicate_logic: 9`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 4`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.628
  * `Choke Point (Betweenness):` 0.004005 | `Ripple Effect (Closeness):` 0.145195
  * `Imports (Out-Degree: 8):` com.mongodb.client.MongoClient, net.simon987.server.game.objects.GameObject, net.simon987.server.logging.LogManager, net.simon987.server.assembly.exception.CancelledException, java.util.concurrent.ConcurrentHashMap, org.bson.Document, net.simon987.server.user.User, org.bson.types.ObjectId...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/game/objects/GameRegistry.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.328 IQR)
- **Top Global Matches:** file_cluster_13: 11.328, file_cluster_8: 11.563, file_cluster_16: 11.622
- **Magnitude:** 140.72 | **LOC:** 150 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.1179%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deserializeGameObject` (Impact: 21.2)
  * `deserializeItem` (Impact: 21.2)
  * `makeItem` (Impact: 14.2)
    * *Intent:* /**
  * `makeTile` (Impact: 14.2)
  * `deserializeHardware` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 47`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 12`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 12`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.256
  * `Choke Point (Betweenness):` 0.001795 | `Ripple Effect (Closeness):` 0.141775
  * `Imports (Out-Degree: 4):` net.simon987.server.logging.LogManager, java.util.HashMap, org.bson.Document, net.simon987.server.game.world.Tile, net.simon987.server.game.item.Item, net.simon987.server.assembly.HardwareModule, java.lang.reflect.InvocationTargetException
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.679 IQR)
- **Top Global Matches:** file_cluster_13: 10.679, file_cluster_8: 10.811, file_cluster_0: 11.209
- **Magnitude:** 138.18 | **LOC:** 223 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0697%), Tech Debt (96.8788%)
**Top Internal Functions/Classes:**
  * `Settlement` (Impact: 40.5)
  * `Settlement` (Impact: 13.4)
  * `mongoSerialise` (Impact: 12.4)
  * `addNpc` (Impact: 2.4)
  * `DifficultyLevel` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 32`, `args: 11`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 33`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.275
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.003342
  * `Imports (Out-Degree: 5):` java.awt.*, java.util.List, org.bson.Document, org.bson.types.ObjectId, net.simon987.server.io.MongoSerializable, java.util.ArrayList, net.simon987.server.game.world.World, net.simon987.server.GameServer...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/RegisterSet.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.806 IQR)
- **Top Global Matches:** file_cluster_13: 11.806, file_cluster_8: 12.159, file_cluster_0: 12.174
- **Magnitude:** 130.88 | **LOC:** 212 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.6173%), Tech Debt (99.8739%)
**Top Internal Functions/Classes:**
  * `getRegister` (Impact: 9.5)
  * `set` (Impact: 9.2)
  * `getIndex` (Impact: 8.7)
    * *Intent:* /** * Create an empty Register set
  * `deserialize` (Impact: 8.2)
  * `deserialize` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 35`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 29`, `duplicate_logic: 4`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.432
  * `Choke Point (Betweenness):` 0.000482 | `Ripple Effect (Closeness):` 0.065163
  * `Imports (Out-Degree: 2):` net.simon987.server.logging.LogManager, java.util.HashMap, java.util.List, org.bson.Document, net.simon987.server.io.MongoSerializable, java.util.ArrayList, org.json.simple.JSONObject, org.json.simple.JSONArray
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.055 IQR)
- **Top Global Matches:** file_cluster_13: 10.055, file_cluster_8: 10.307, file_cluster_0: 10.569
- **Magnitude:** 128.56 | **LOC:** 135 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.4459%), Tech Debt (99.3484%)
**Top Internal Functions/Classes:**
  * `handleInterrupt` (Impact: 95.3)
  * `getId` (Impact: 2.4)
  * `CubotLidar` (Impact: 2.1)
  * `CubotLidar` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 13`, `args: 4`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 18`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` net.simon987.server.assembly.Memory, net.simon987.server.assembly.Status, net.simon987.server.game.pathfinding.Pathfinder, org.bson.Document, java.util.ArrayList, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.game.pathfinding.Node, net.simon987.server.assembly.HardwareModule
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.288 IQR)
- **Top Global Matches:** file_cluster_13: 11.288, file_cluster_8: 11.642, file_cluster_7: 11.955
- **Magnitude:** 127.1 | **LOC:** 262 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0816%), Tech Debt (46.3301%)
**Top Internal Functions/Classes:**
  * `VaultDimension` (Impact: 52.7)
  * `attachWorld` (Impact: 35.5)
  * `coordinatesOf` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.awt.*, net.simon987.server.logging.LogManager, java.util.HashMap, net.simon987.server.game.world.Location, java.util.Random, org.bson.types.ObjectId, net.simon987.server.game.objects.Direction, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/Operand.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.902 IQR)
- **Top Global Matches:** file_cluster_8: 9.902, file_cluster_7: 10.187, file_cluster_13: 10.327
- **Magnitude:** 126.32 | **LOC:** 277 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.9533%), Tech Debt (98.0358%)
**Top Internal Functions/Classes:**
  * `parseRegExpr` (Impact: 38.3)
    * *Intent:* /**
  * `Operand` (Impact: 26.5)
  * `parseImmediate` (Impact: 14.7)
  * `parseLabel` (Impact: 9.4)
    * *Intent:* /** * Attempt to parse an integer *
  * `parseReg` (Impact: 5.8)
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

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotInventory.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.584 IQR)
- **Top Global Matches:** file_cluster_13: 10.584, file_cluster_8: 10.868, file_cluster_0: 10.886
- **Magnitude:** 122.52 | **LOC:** 143 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.991%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `handleInterrupt` (Impact: 30.8)
  * `toString` (Impact: 9.3)
  * `mongoSerialise` (Impact: 7.6)
  * `CubotInventory` (Impact: 5.8)
  * `super` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 24`, `args: 11`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.007519
  * `Imports (Out-Degree: 5):` net.simon987.server.assembly.Status, java.util.HashMap, org.bson.Document, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.game.item.Item, net.simon987.server.assembly.HardwareModule, net.simon987.server.GameServer, java.util.Map
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.321 IQR)
- **Top Global Matches:** file_cluster_13: 10.321, file_cluster_8: 10.748, file_cluster_16: 10.928
- **Magnitude:** 120.02 | **LOC:** 174 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6058%), Tech Debt (99.4139%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 36.2)
  * `loadInFolder` (Impact: 21.7)
    * *Intent:* /** * Load all plugins in plugins folder, if it doesn't exist, create it * * @return true if all the...
  * `initWithDependencies` (Impact: 14.3)
  * `getPluginByName` (Impact: 7.4)
  * `initPlugin` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 39`, `args: 9`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 17`, `duplicate_logic: 4`
* *Architecture:* `io: 8`, `api: 7`, `import: 14`
* *Defense:* `safety: 5`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.259
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.138158
  * `Imports (Out-Degree: 2):` net.simon987.server.logging.LogManager, java.util.List, java.util.ArrayList, java.net.URLClassLoader, java.util.zip.ZipEntry, java.io.IOException, java.lang.reflect.Constructor, java.net.URL...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/test/java/net/simon987/server/assembly/OperandTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.536 IQR)
- **Top Global Matches:** file_cluster_8: 12.536, file_cluster_13: 12.568, file_cluster_0: 12.768
- **Magnitude:** 119.48 | **LOC:** 154 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5276%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Operand` (Impact: 103.0)
  * `fail` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 48`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 42`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.junit.Test, java.util.HashMap, org.junit.Assert.fail, org.junit.Assert.assertEquals, net.simon987.server.assembly.exception.InvalidOperandException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/websocket/SocketServer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.933 IQR)
- **Top Global Matches:** file_cluster_13: 10.933, file_cluster_0: 11.316, file_cluster_8: 11.346
- **Magnitude:** 117.16 | **LOC:** 187 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.1121%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `onMessage` (Impact: 19.0)
  * `tick` (Impact: 13.3)
    * *Intent:* /**
  * `sendJSONObject` (Impact: 7.4)
  * `charArraysToJSON` (Impact: 7.2)
  * `sendString` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 45`, `args: 12`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 25`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.45
  * `Choke Point (Betweenness):` 0.002266 | `Ripple Effect (Closeness):` 0.138866
  * `Imports (Out-Degree: 5):` net.simon987.server.logging.LogManager, java.util.List, net.simon987.server.user.User, org.eclipse.jetty.websocket.api.annotations.WebSocket, java.util.ArrayList, net.simon987.server.web.GuestPolicy, net.simon987.server.game.objects.ControllableUnit, org.json.simple.JSONArray...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA) | Magnitude: 335.3 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 241, state_mutation: 89, structural_boundaries: 85, branch: 48
- `Plugin NPC/src/main/java/net/simon987/npcplugin/Obstacle.java` (JAVA) | Magnitude: 65.76 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 20, func_start: 16, api: 16
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/ItemBluePrint.java` (JAVA) | Magnitude: 36.12 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 14, func_start: 9, api: 9
- `Server/src/test/java/net/simon987/server/FakeConfiguration.java` (JAVA) | Magnitude: 25.38 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, api: 10, structural_boundaries: 9, args: 5
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/Obstacle.java` (JAVA) | Magnitude: 64.84 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 22, func_start: 18, api: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT) | Magnitude: 7672.26 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5118, state_mutation: 3879, branch: 1516, structural_boundaries: 1142

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Server/src/main/java/net/simon987/server/assembly/instruction/XchgInstruction.java` (JAVA) | Magnitude: 9.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, api: 4, import: 4
- `Server/src/main/java/net/simon987/server/game/objects/ItemsContainer.java` (JAVA) | Magnitude: 41.24 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 18, args: 10, func_start: 9
- `Server/src/main/java/net/simon987/server/event/WorldGenerationEvent.java` (JAVA) | Magnitude: 9.4 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 4, func_start: 3
- `Server/src/main/java/net/simon987/server/assembly/DefaultInstructionSet.java` (JAVA) | Magnitude: 101.22 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 64, state_mutation: 59, doc: 11
- `Server/src/test/java/net/simon987/server/assembly/instruction/SetgInstructionTest.java` (JAVA) | Magnitude: 27.96 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 18, structural_boundaries: 12, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT) | Magnitude: 2768.06 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1038, indent_spaces: 672, doc: 263, branch: 199

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Server/src/main/java/net/simon987/server/user/UserStatsHelper.java` (JAVA) | Magnitude: 43.2 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 25, state_mutation: 19, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Server/src/main/java/net/simon987/server/Main.java` (JAVA) | Magnitude: 12.5 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, concurrency: 6, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `Server/src/main/java/net/simon987/server/assembly/InstructionSet.java` (JAVA) | Magnitude: 25.12 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 3, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Server/src/main/java/net/simon987/server/assembly/AssemblyResult.java` (JAVA) | Magnitude: 40.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 20, doc: 16, branch: 10
- `Server/src/main/java/net/simon987/server/websocket/MessageHandler.java` (JAVA) | Magnitude: 18.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 2, args: 1, func_start: 1
- `Server/src/main/resources/static/js/editor.js` (JAVASCRIPT) | Magnitude: 437.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 372, state_mutation: 154, branch: 113, structural_boundaries: 69
- `Server/src/main/java/net/simon987/server/game/world/Tile.java` (JAVA) | Magnitude: 14.9 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, api: 8, structural_boundaries: 7, doc: 7
- `Server/src/main/java/net/simon987/server/game/world/WorldGenerator.java` (JAVA) | Magnitude: 71.32 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 25, branch: 21, encapsulation: 15

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

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 16.816** (Embedded: 0.2184 * Error Risk: 77.0057%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 15.976** (Embedded: 0.23 * Error Risk: 69.4708%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 13.023** (Embedded: 0.1452 * Error Risk: 89.6928%)
- `Server/src/main/java/net/simon987/server/user/User.java` -> **Severity: 12.967** (Embedded: 0.1574 * Error Risk: 82.3665%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 12.401** (Embedded: 0.1521 * Error Risk: 81.5191%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Server/src/main/java/net/simon987/server/ServerConfiguration.java` -> **Severity: 8844.069** (Blast Radius: 89.271 * Doc Risk: 99.0699%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 7535.905** (Blast Radius: 103.863 * Doc Risk: 72.5562%)
- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 3030.649** (Blast Radius: 34.741 * Doc Risk: 87.2355%)
- `Server/src/main/java/net/simon987/server/assembly/Status.java` -> **Severity: 2820.827** (Blast Radius: 28.231 * Doc Risk: 99.9195%)
- `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` -> **Severity: 1465.881** (Blast Radius: 14.76 * Doc Risk: 99.3144%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
