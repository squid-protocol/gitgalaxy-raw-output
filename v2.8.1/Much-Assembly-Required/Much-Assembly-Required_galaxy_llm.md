# ARCHITECTURAL_BRIEF: Much-Assembly-Required
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/simon987/Much-Assembly-Required.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 451 |
| Analyzed Artifacts (Scanned) | 401 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 50 |
| Total LOC | 47971 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.525 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2753 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8128 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 324 | 13001 | 80.8% |
| JAVASCRIPT | 43 | 25930 | 10.7% |
| TYPESCRIPT | 10 | 8647 | 2.5% |
| XML | 8 | 0 | 2.0% |
| PLAINTEXT | 7 | 0 | 1.7% |
| MARKDOWN | 2 | 0 | 0.5% |
| JSON | 2 | 82 | 0.5% |
| DOCKERFILE | 1 | 6 | 0.2% |
| CSS | 1 | 261 | 0.2% |
| RUBY | 1 | 5 | 0.2% |
| SHELL | 1 | 12 | 0.2% |
| YAML | 1 | 27 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +1.57; from the repo's file-archetype mix)
> **File Composition:** Annotated Framework Methods Files 24%, Data / Markup / Trivial 20%, Interface Declarations Files 11%, Large Core Modules 10%, Declarative / Non-Code 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 392 | 97.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 50*

**Composition by Extension & Reason:**
- `.java`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 49.5 | 60.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.6 | 7.5 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.1 | 19.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 87.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 60.4 | 76.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 331 | 109 | 2 | `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` |
| cleanup | 67 | 10 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| guards | 1711 | 216 | 7 | `Server/src/main/resources/static/js/ace/ace.js` |
| danger | 2058 | 144 | 3 | `Server/src/main/typescript/phaser.d.ts` |
| concurrency | 171 | 15 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| connectivity | 2340 | 370 | 10 | `Server/src/main/resources/static/js/ace/ace.js` |
| io | 48 | 14 | 0 | `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 2 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| time | 88 | 8 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| serialization | 18 | 2 | 0 | `Server/src/main/resources/static/js/mar.js` |
| regex | 169 | 7 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| events | 426 | 32 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| tests | 288 | 37 | 0 | `Server/src/test/java/net/simon987/server/assembly/OperandTest.java` |
| docs | 806 | 191 | 4 | `Server/src/main/resources/static/js/phaser-plugin-isometric.js` |
| debt | 846 | 55 | 1 | `Server/src/main/typescript/phaser.d.ts` |
| mutation | 13245 | 301 | 26 | `Server/src/main/resources/static/js/ace/ace.js` |
| dead_code | 1675 | 155 | 3 | `Server/src/main/typescript/phaser.d.ts` |
| credential | 19 | 11 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| threat | 544 | 10 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |
| ml_ai | 83 | 26 | 0 | `Server/src/main/typescript/phaser.d.ts` |
| ui | 80 | 16 | 0 | `Server/src/main/resources/static/js/ace/ace.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4444**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Server/src/main/java/net/simon987/server/plugin/PluginManager.java` (Hits: 8)
- `Server/src/main/typescript/phaser.d.ts` (Hits: 8)
- `Server/src/test/java/net/simon987/server/ConfigHelper.java` (Hits: 7)

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

- `escapeHTML` **(Compute Cores)** (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **479.7** | LOC: 1392
- `generateVaultWorld` **(Many-Argument Workhorses)** (@ `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java`) -> Impact: **123.2** | LOC: 227
- `onMouseDown` **(Compute Cores)** (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **97.5** | LOC: 168
- `renderChanges` **(Compute Cores)** (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **83.3** | LOC: 107
- `copy` **(Compute Cores)** (@ `Server/src/main/typescript/phaser.d.ts`) -> Impact: **76.4** | LOC: 1
- `normalizeCommandKeys` **(Defensive Guards)** (@ `Server/src/main/resources/static/js/ace/ace.js`) -> Impact: **74.7** | LOC: 54
- `setcc` **(Compute Cores)** (@ `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java`) -> Impact: **73.3** | LOC: 34
  * *Intent:* * 0x02 SETAE,SETNB,SETNC Above or Equal, Not Below, No Carry CF=0 * 0x03 SETBE, SETNA Below or Equal, Not Above CF=1 OR ZF=1 * 0x04 SETB, SETC,SETNAE ...
- `separateZ` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **68.8** | LOC: 97
  * *Intent:* /** * The core separation function to separate two physics bodies on the z axis. * * @private * @method Phaser.Plugin.Isometric.Arcade#separateZ * @pa...
- `executeInstruction` **(Many-Argument Workhorses)** (@ `Server/src/main/java/net/simon987/server/assembly/CPU.java`) -> Impact: **66.0** | LOC: 81
- `separateX` **(Many-Argument Workhorses)** (@ `Server/src/main/resources/static/js/phaser-plugin-isometric.js`) -> Impact: **64.2** | LOC: 84
  * *Intent:* /** * The core separation function to separate two physics bodies on the x axis. * * @private * @method Phaser.Plugin.Isometric.Arcade#separateX * @pa...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Server/src/main/resources/static/js/ace` | 40 | 14970.48 | 4.81% | 1.9% |
| `Server/src/main/resources/static/js` | 3 | 5399.32 | 76.27% | 36.04% |
| `Server/src/main/typescript` | 11 | 2179.1 | 30.76% | 72.87% |
| `Plugin NPC/src/main/java/net/simon987/npcplugin` | 21 | 1706.44 | 42.18% | 65.06% |
| `Server/src/main/java/net/simon987/server/assembly` | 18 | 1508.24 | 20.81% | 5.52% |
| `Server/src/main/java/net/simon987/server/assembly/instruction` | 76 | 1367.44 | 8.89% | 7.03% |
| `Plugin Cubot/src/main/java/net/simon987/cubotplugin` | 17 | 1104.8 | 40.22% | 63.58% |
| `Server/src/main/java/net/simon987/server/game/world` | 13 | 566.6 | 9.61% | 35.37% |
| `Server/src/test/java/net/simon987/server/assembly/instruction` | 31 | 560.02 | 0.63% | 0.0% |
| `Server/src/main/java/net/simon987/server/game/objects` | 15 | 500.82 | 9.94% | 6.66% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotBattery.java` -> **100.0%** Exposure
- `plugin-contruction/src/main/java/net/simon987/constructionplugin/ConstructionSite.java` -> **100.0%** Exposure
- `Server/src/main/typescript/p2.d.ts` -> **100.0%** Exposure
- `Server/src/main/typescript/phaser.d.ts` -> **100.0%** Exposure
- `Server/src/main/typescript/pixi.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/HarvestTask.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` -> **100.0%** Exposure
- `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Server/src/main/typescript/phaser.d.ts` -> **919** Orphaned Functions | **469** Duplicates
- `Server/src/main/typescript/pixi.d.ts` -> **92** Orphaned Functions | **109** Duplicates
- `Server/src/main/typescript/p2.d.ts` -> **132** Orphaned Functions | **23** Duplicates
- `Server/src/main/typescript/phaser.plugin.isometric.d.ts` -> **40** Orphaned Functions | **2** Duplicates
- `Server/src/main/resources/static/js/ace/ace.js` -> **34** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1258` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA) -> Cumulative Risk: **679.41**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.90)
- **Magnitude:** 207.4 | **LOC:** 340 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9984%), State Flux (99.973%)
- **Heaviest Functions:** `detachHardware` (Generic / Templated Code, Impact: 9.1), `jsonSerialise` (Interface Declarations, Impact: 7.0), `spendEnergy` (Type Conversions, Impact: 6.4)

### 2. `Server/src/main/typescript/GameObject.ts` (TYPESCRIPT) -> Cumulative Risk: **668.05**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.85)
- **Magnitude:** 550.46 | **LOC:** 889 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.3069%), Safety Score (92.936%)
- **Heaviest Functions:** `updateObject` (Compute Cores, Impact: 20.1), `createObject` (Compute Cores, Impact: 19.7), `updateHologram` (Many-Argument Workhorses, Impact: 19.6)

### 3. `Server/src/main/java/net/simon987/server/GameServer.java` (JAVA) -> Cumulative Risk: **661.75**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.60)
- **Magnitude:** 172.56 | **LOC:** 351 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9933%), Cognitive Load (90.6484%)
- **Heaviest Functions:** `save` (I/O & Config Routines, Impact: 16.4), `load` (I/O & Config Routines, Impact: 11.1), `tick` (I/O & Config Routines, Impact: 10.1)

### 4. `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT) -> Cumulative Risk: **657.39**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.23)
- **Magnitude:** 2097.7 | **LOC:** 1946 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `initialiseAnimations` (I/O & Config Routines, Impact: 27.2), `handle` (Compute Cores, Impact: 26.5), `createTile` (Compute Cores, Impact: 25.1)

### 5. `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT) -> Cumulative Risk: **637.01**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.06)
- **Magnitude:** 13787.44 | **LOC:** 19384 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.0859%)
- **Heaviest Functions:** `escapeHTML` (Compute Cores, Impact: 479.7), `onMouseDown` (Compute Cores, Impact: 97.5), `renderChanges` (Compute Cores, Impact: 83.3)

### 6. `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` (JAVA) -> Cumulative Risk: **623.44**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.37)
- **Magnitude:** 166.64 | **LOC:** 262 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.2825%), Tech Debt (96.2039%)
- **Heaviest Functions:** `VaultDimension` (Compute Cores, Impact: 43.0), `attachWorld` (Compute Cores, Impact: 18.5), `worldExists` (Callbacks & Closures, Impact: 2.0)

### 7. `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA) -> Cumulative Risk: **622.59**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.63)
- **Magnitude:** 170.46 | **LOC:** 223 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.5548%)
- **Heaviest Functions:** `Settlement` (Compute Cores, Impact: 26.3), `Settlement` (Type Conversions, Impact: 9.9), `mongoSerialise` (I/O & Config Routines, Impact: 6.2)

### 8. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotLidar.java` (JAVA) -> Cumulative Risk: **614.37**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.59)
- **Magnitude:** 105.66 | **LOC:** 135 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.3289%)
- **Heaviest Functions:** `handleInterrupt` (Compute Cores, Impact: 47.1), `CubotLidar` (State Mutators, Impact: 1.9), `CubotLidar` (State Mutators, Impact: 1.6)

### 9. `Server/src/main/typescript/MarGame.ts` (TYPESCRIPT) -> Cumulative Risk: **598.85**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.92)
- **Magnitude:** 367.6 | **LOC:** 346 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.7505%), Documentation (92.3077%)
- **Heaviest Functions:** `initialiseAnimations` (I/O & Config Routines, Impact: 28.0), `constructor` (I/O & Config Routines, Impact: 26.7), `update` (I/O & Config Routines, Impact: 17.9)

### 10. `Plugin Cubot/src/main/java/net/simon987/cubotplugin/CubotComPort.java` (JAVA) -> Cumulative Risk: **594.79**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.59)
- **Magnitude:** 86.06 | **LOC:** 131 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.996%)
- **Heaviest Functions:** `handleInterrupt` (Compute Cores, Impact: 42.7), `CubotComPort` (State Mutators, Impact: 1.9), `CubotComPort` (State Mutators, Impact: 1.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Server/src/main/resources/static/js/ace/ace.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 13787.44 | **LOC:** 19384 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (12.6797%)
**Top Internal Functions/Classes:**
  * `escapeHTML` **(Compute Cores)** (Impact: 479.7)
  * `onMouseDown` **(Compute Cores)** (Impact: 97.5)
  * `renderChanges` **(Compute Cores)** (Impact: 83.3)
  * `normalizeCommandKeys` **(Defensive Guards)** (Impact: 74.7)
  * `addMultiMouseDownListener` **(Many-Argument Workhorses)** (Impact: 47.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 2963 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 239
* *State Mutation (weighted view):* 9863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4156`, `structural_boundaries: 3518`, `args: 1668`, `func_start: 1408`
* *Risk/State:* `safety_bypasses: 675`, `high_risk_execution: 11`, `state_mutation: 3937`, `dead_code: 2`, `planned_debt: 19`, `fragile_debt: 2`, `duplicate_logic: 7`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 222`, `concurrency: 49`, `import: 202`
* *Defense:* `safety: 426`, `doc: 3`, `immutability_locks: 7`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lang, oop, range, token_iterator, behaviour, config, hash_handler, dom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/phaser-plugin-isometric.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2908.14 | **LOC:** 4447 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.2314%), Tech Debt (35.5406%)
**Top Internal Functions/Classes:**
  * `separateZ` **(Many-Argument Workhorses)** (Impact: 68.8)
    * *Intent:* /** * The core separation function to separate two physics bodies on the z axis. * * @private * @met...
  * `separateX` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * The core separation function to separate two physics bodies on the x axis. * * @private * @met...
  * `separateY` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* /** * The core separation function to separate two physics bodies on the x axis. * * @private * @met...
  * `computeVelocity` **(Many-Argument Workhorses)** (Impact: 54.7)
    * *Intent:* /** * A tween-like function that takes a starting velocity and some other factors and returns an alt...
  * `topologicalSort` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /** * Perform a volume-based topological sort on all IsoSprites in the passed group or array. Will u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 432 instances
* *State Mutation (weighted view):* 1580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 504`, `structural_boundaries: 213`, `args: 178`, `func_start: 159`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 716`, `dead_code: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 22`
* *Architecture:* None
* *Defense:* `safety: 131`, `doc: 256`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/mar.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2097.7 | **LOC:** 1946 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (62.728%)
**Top Internal Functions/Classes:**
  * `initialiseAnimations` **(I/O & Config Routines)** (Impact: 27.2)
  * `handle` **(Compute Cores)** (Impact: 26.5)
  * `createTile` **(Compute Cores)** (Impact: 25.1)
  * `MarGame` **(Callbacks & Closures)** (Impact: 24.6)
  * `handleObjectsUpdate` **(Defensive Guards)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 333 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 1298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 291`, `args: 236`, `func_start: 174`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 2`, `state_mutation: 632`, `duplicate_logic: 12`, `unreferenced_by_name: 28`
* *Architecture:* `io: 1`, `concurrency: 4`
* *Defense:* `safety: 32`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/GameObject.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 550.46 | **LOC:** 889 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7119%), Tech Debt (99.3069%)
**Top Internal Functions/Classes:**
  * `updateObject` **(Compute Cores)** (Impact: 20.1)
  * `createObject` **(Compute Cores)** (Impact: 19.7)
    * *Intent:* /** * Factory method for GameObjects */
  * `updateHologram` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `walkAnimation` **(Compute Cores)** (Impact: 11.9)
  * `walk` **(I/O & Config Routines)** (Impact: 11.8)
    * *Intent:* /** * Initiate the walk animation. Handles multiple calls of this function even if the previous anim...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 78`, `args: 56`, `func_start: 54`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 162`, `planned_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 34`, `concurrency: 2`
* *Defense:* `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/editor.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 393.48 | **LOC:** 572 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5867%), Tech Debt (9.8388%)
**Top Internal Functions/Classes:**
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `getOperandType` **(Defensive Guards)** (Impact: 52.6)
  * `parseDWInstruction` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `checkForORGInstruction` **(Defensive Guards)** (Impact: 17.6)
  * `checkForEQUInstruction` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 69`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 59`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 5`
* *Defense:* `safety: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.465
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0025
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/CPU.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 378.22 | **LOC:** 470 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0304%), Tech Debt (15.497%)
**Top Internal Functions/Classes:**
  * `executeInstruction` **(Many-Argument Workhorses)** (Impact: 66.0)
  * `executeImmediateValue` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `executeSourceIsRegister` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `executeImmediateValueMem` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `execute` **(Compute Cores)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 102`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 108`, `planned_debt: 5`
* *Architecture:* `api: 21`, `import: 10`
* *Defense:* `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.901
  * `Choke Point (Betweenness):` 0.009403 | `Ripple Effect (Closeness):` 0.127412
  * `Imports (Out-Degree: 9):` net.simon987.server.GameServer, net.simon987.server.IServerConfiguration, net.simon987.server.assembly.exception.CancelledException, net.simon987.server.assembly.instruction.*, net.simon987.server.event.CpuInitialisationEvent, net.simon987.server.event.GameEvent, net.simon987.server.game.objects.ControllableUnit, net.simon987.server.game.objects.HardwareHost...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/phaser.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 373.68 | **LOC:** 7686 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.5206%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `copy` **(Compute Cores)** (Impact: 76.4)
  * `button` **(Compute Cores)** (Impact: 36.5)
  * `constructor` **(Compute Cores)** (Impact: 33.2)
  * `button` **(Compute Cores)** (Impact: 31.7)
  * `setSounds` **(Compute Cores)** (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1711`, `structural_boundaries: 1140`, `args: 2072`, `func_start: 2044`, `class_start: 181`
* *Risk/State:* `safety_bypasses: 731`, `state_mutation: 2`, `duplicate_logic: 469`, `unreferenced_by_name: 919`
* *Architecture:* `io: 8`, `api: 4`
* *Defense:* `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/MarGame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 367.6 | **LOC:** 346 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.737%), Tech Debt (60.0647%)
**Top Internal Functions/Classes:**
  * `initialiseAnimations` **(I/O & Config Routines)** (Impact: 28.0)
  * `constructor` **(I/O & Config Routines)** (Impact: 26.7)
  * `update` **(I/O & Config Routines)** (Impact: 17.9)
  * `preload` **(I/O & Config Routines)** (Impact: 6.0)
  * `getMessage` **(Interface Declarations)** (Impact: 3.6)
    * *Intent:* /** * Indicates current World */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 10`, `args: 17`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 110`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin Cubot/src/main/java/net/simon987/cubotplugin/Cubot.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 337.58 | **LOC:** 606 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9783%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(I/O & Config Routines)** (Impact: 10.0)
  * `detachHardware` **(Generic / Templated Code)** (Impact: 9.1)
  * `jsonSerialise` **(I/O & Config Routines)** (Impact: 6.2)
  * `hardwareInterrupt` **(Annotated Framework Methods)** (Impact: 5.7)
  * `Cubot` **(Type Conversions)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 117`, `args: 55`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 69`
* *Architecture:* `api: 57`, `import: 16`
* *Defense:* `safety: 2`, `doc: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.326
  * `Choke Point (Betweenness):` 0.000624 | `Ripple Effect (Closeness):` 0.015
  * `Imports (Out-Degree: 13):` java.awt.*, java.util.*, java.util.List, net.simon987.cubotplugin.event.CubotWalkEvent, net.simon987.cubotplugin.event.DeathEvent, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration, net.simon987.server.assembly.CPU...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultWorldGenerator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 293.14 | **LOC:** 266 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.7193%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `generateVaultWorld` **(Many-Argument Workhorses)** (Impact: 123.2)
  * `hasTileAdjacent` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `compare` **(Annotated Framework Methods)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 39`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.awt.*, java.util.ArrayList, java.util.Comparator, java.util.Random, net.simon987.server.game.objects.Direction, net.simon987.server.game.world.TileMap, net.simon987.server.game.world.TileVoid, net.simon987.server.game.world.World
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/Assembler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 289.62 | **LOC:** 607 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5406%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseDWInstruction` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* /** * Parse the DW instruction (Define word). Handles DUP operator * * @param line Current line. ass...
  * `parseInstruction` **(Many-Argument Workhorses)** (Impact: 41.1)
    * *Intent:* /** * Parse an instruction and encode it * * @param line Line to parse * @param currentLine Current ...
  * `parseDUPOperator16` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /** * Parse the dup operator * * @param valueTokens Value tokens e.g. {"8", "DUP(12)"} * @param labe...
  * `parse` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /** * Parses a text and assembles it. The assembler splits the text in * lines and parses them one b...
  * `checkForEQUInstruction` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* /** * Check for and handle the EQU instruction * * @param line Current line. The method is assuming ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 77`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 36`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 32`, `doc: 15`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.41
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.005
  * `Imports (Out-Degree: 2):` java.io.ByteArrayOutputStream, java.io.DataOutputStream, java.io.IOException, java.nio.charset.StandardCharsets, java.util.HashMap, java.util.regex.Matcher, java.util.regex.Pattern, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/World.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 274.24 | **LOC:** 484 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.6639%), Tech Debt (23.8793%)
**Top Internal Functions/Classes:**
  * `createTile` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* /** * Factory method to create a Tile */
  * `handleObjectsUpdate` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* /** * Update, create or delete the current objects based on a list received from the server * @param...
  * `setTerrain` **(State Mutators)** (Impact: 8.5)
    * *Intent:* /** * Load terrain data from array and create Tiles * @param terrain * @param size Size of a side of...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 6.2)
  * `updateTerrain` **(State Mutators)** (Impact: 5.9)
    * *Intent:* /** * Delete current ojects and tiles and replace them with provided terrain * @param terrain * @par...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 40`, `args: 28`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 100`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`
* *Defense:* `doc: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/typescript/GameClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 267.92 | **LOC:** 499 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.3907%), Tech Debt (80.8285%)
**Top Internal Functions/Classes:**
  * `handle` **(Compute Cores)** (Impact: 27.5)
  * `onDownCallback` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* //Handle keypresses
  * `connectToGameServer` **(State Mutators)** (Impact: 11.9)
    * *Intent:* /** * Connect to the game server * @param info JSON fetched from /getServerInfo.php */
  * `handle` **(State Mutators)** (Impact: 10.7)
  * `initGame` **(I/O & Config Routines)** (Impact: 10.5)
    * *Intent:* /** * Called after the connection has been made to the server */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 46`, `args: 39`, `func_start: 38`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 1`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/world/World.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 247.82 | **LOC:** 443 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.5633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRandomTileWithAdjacent` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* /** * Get a random tile with N adjacent non-blocked tile * * @param n Number of adjacent tiles of ty...
  * `update` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /** * Update this World and its GameObjects * <br> * The update is handled by plugins first */
  * `getMapInfo` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* /** * Get a binary representation of the map as an array of 16-bit bit fields, one word for each * t...
  * `getGameObjectsBlockingAt` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* /** * Get the list of game objects that are blocking a tile at a set of coordinates * * @param x X c...
  * `getGameObjectsAt` **(Generic / Templated Code)** (Impact: 7.5)
    * *Intent:* /** * Get the list of game objects that are exactly at a given location * <br> * Note: Objects like ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 66`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 47`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 2`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.404
  * `Choke Point (Betweenness):` 0.006253 | `Ripple Effect (Closeness):` 0.151749
  * `Imports (Out-Degree: 8):` java.awt.*, java.util.ArrayList, java.util.Collection, java.util.List, java.util.Random, java.util.concurrent.ConcurrentHashMap, net.simon987.server.GameServer, net.simon987.server.event.GameEvent...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/assembly/instruction/SetccInstruction.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 240.08 | **LOC:** 342 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.5295%), Tech Debt (24.4136%)
**Top Internal Functions/Classes:**
  * `setcc` **(Compute Cores)** (Impact: 73.3)
    * *Intent:* * 0x02 SETAE,SETNB,SETNC Above or Equal, Not Below, No Carry CF=0 * 0x03 SETBE, SETNA Below or Equal...
  * `encode` **(Many-Argument Workhorses)** (Impact: 17.6)
    * *Intent:* /** * Encodes the instruction. Writes the result in the outputStream. * Needs one operand of Operand...
  * `seta` **(Encapsulated Accessors)** (Impact: 6.3)
    * *Intent:* /** * SETA, SETNBE Above, Not Below or Equal CF=0 AND ZF=0 */
  * `setae` **(Encapsulated Accessors)** (Impact: 6.3)
    * *Intent:* /** * SETAE,SETNB,SETNC Above or Equal, Not Below, No Carry CF=0 */
  * `setbe` **(Encapsulated Accessors)** (Impact: 6.3)
    * *Intent:* /** * SETBE, SETNA Below or Equal, Not Above CF=1 OR ZF=1 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 53`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 26`, `unreferenced_by_name: 3`
* *Architecture:* `api: 22`, `import: 12`
* *Defense:* `doc: 20`, `sync_locks: 28`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.io.ByteArrayOutputStream, java.util.HashMap, java.util.Map, net.simon987.server.assembly.Instruction, net.simon987.server.assembly.MachineCode, net.simon987.server.assembly.Operand, net.simon987.server.assembly.OperandType, net.simon987.server.assembly.Status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/resources/static/js/ace/ext-searchbox.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 230.06 | **LOC:** 511 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8838%), Tech Debt (10.5846%)
**Top Internal Functions/Classes:**
  * `init` **(Callbacks & Closures)** (Impact: 12.3)
  * `updateCounter` **(I/O & Config Routines)** (Impact: 11.6)
  * `setSearchRange` **(State Mutators)** (Impact: 6.1)
  * `find` **(Callbacks & Closures)** (Impact: 4.8)
  * `syncOptions` **(State Mutators)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 52`, `args: 48`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 66`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hash_handler, dom, event, keys, lang
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/HackedNPC.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 207.4 | **LOC:** 340 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.4778%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `detachHardware` **(Generic / Templated Code)** (Impact: 9.1)
  * `jsonSerialise` **(Interface Declarations)** (Impact: 7.0)
  * `spendEnergy` **(Type Conversions)** (Impact: 6.4)
  * `hardwareInterrupt` **(Annotated Framework Methods)** (Impact: 5.7)
  * `HackedNPC` **(Type Conversions)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 85`, `args: 37`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 38`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 30`, `concurrency: 6`, `import: 15`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.util.ArrayList, java.util.HashMap, java.util.List, java.util.Map, net.simon987.server.GameServer, net.simon987.server.assembly.*, net.simon987.server.event.ObjectDeathEvent, net.simon987.server.game.item.Item...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/assembly/Operand.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 207.32 | **LOC:** 277 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3267%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseRegExpr` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /** * Attempt to parse a register followed by an expression. * The expression has to follow this for...
  * `Operand` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /** * Creates an Operand from text. If labels is not null, it will be used to parse the * operand. *...
  * `parseLabel` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /** * Attempt to parse a user-defined label * * @param text Text to parse * @param labels Map of lab...
  * `parseReg` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* /** * Attempt to parse a register * * @param text Text to parse * @return true if successful */
  * `parseImmediate` **(Defensive Guards)** (Impact: 4.1)
    * *Intent:* /** * Attempt to parse an integer * * @param text Text to parse, can be a label or immediate value (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 30`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 41`
* *Architecture:* `api: 10`, `import: 2`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.734
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.005
  * `Imports (Out-Degree: 1):` java.util.HashMap, net.simon987.server.assembly.exception.InvalidOperandException
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/java/net/simon987/server/GameServer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 172.56 | **LOC:** 351 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.6484%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `save` **(I/O & Config Routines)** (Impact: 16.4)
  * `load` **(I/O & Config Routines)** (Impact: 11.1)
  * `tick` **(I/O & Config Routines)** (Impact: 10.1)
  * `GameServer` **(I/O & Config Routines)** (Impact: 8.2)
  * `run` **(I/O & Config Routines)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 82`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 44`
* *Architecture:* `api: 18`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.702
  * `Choke Point (Betweenness):` 0.022816 | `Ripple Effect (Closeness):` 0.217833
  * `Imports (Out-Degree: 16):` com.mongodb.MongoClientException, com.mongodb.client.*, com.mongodb.client.model.ReplaceOptions, java.util.ArrayList, net.simon987.server.crypto.CryptoProvider, net.simon987.server.crypto.SecretKeyGenerator, net.simon987.server.event.GameEvent, net.simon987.server.event.GameEventDispatcher...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/Settlement.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 170.46 | **LOC:** 223 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.9045%), Tech Debt (10.0358%)
**Top Internal Functions/Classes:**
  * `Settlement` **(Compute Cores)** (Impact: 26.3)
  * `Settlement` **(Type Conversions)** (Impact: 9.9)
  * `mongoSerialise` **(I/O & Config Routines)** (Impact: 6.2)
  * `addNpc` **(Interface Declarations)** (Impact: 1.6)
  * `DifficultyLevel` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 38`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.273
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.003333
  * `Imports (Out-Degree: 5):` java.awt.*, java.util.ArrayList, java.util.List, net.simon987.server.GameServer, net.simon987.server.game.world.TilePlain, net.simon987.server.game.world.World, net.simon987.server.game.world.WorldGenerationException, net.simon987.server.io.MongoSerializable...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/VaultDimension.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 166.64 | **LOC:** 262 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.6458%), Tech Debt (96.2039%)
**Top Internal Functions/Classes:**
  * `VaultDimension` **(Compute Cores)** (Impact: 43.0)
  * `attachWorld` **(Compute Cores)** (Impact: 18.5)
    * *Intent:* /** * Update the blueprint's openings to allow traveling to the newly attached world * * @param dire...
  * `worldExists` **(Callbacks & Closures)** (Impact: 2.0)
  * `coordinatesOf` **(Interface Declarations)** (Impact: 1.7)
    * *Intent:* /** * Get the coordinates of a world that would be attached to this world * * @param direction direc...
  * `getHomeWorld` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 43`, `args: 9`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.awt.*, java.util.ArrayList, java.util.Collection, java.util.HashMap, java.util.Random, net.simon987.npcplugin.world.TileVaultFloor, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/GameUniverse.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 161.56 | **LOC:** 293 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.3905%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getWorld` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* /** * Get a world by coordinates, attempts to load from mongoDB if not found. * * @param x the x coo...
  * `getOrCreateUser` **(Defensive Guards)** (Impact: 11.9)
  * `getObject` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* /** * Get an object by id * <br> * ConcurrentModificationException risk when inside game loop * * @p...
  * `loadWorld` **(Generic / Templated Code)** (Impact: 6.8)
    * *Intent:* /** * Attempts loading a world from mongoDB by coordinates * * @param x the x coordinate of the worl...
  * `removeWorld` **(Parameter Forwarders)** (Impact: 4.3)
    * *Intent:* /** * Removes the world with given coordinates from the universe. * * @param x the x coordinate of t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 58`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 26`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 4`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.622
  * `Choke Point (Betweenness):` 0.003985 | `Ripple Effect (Closeness):` 0.144832
  * `Imports (Out-Degree: 8):` com.mongodb.client.MongoClient, com.mongodb.client.MongoCollection, com.mongodb.client.MongoCursor, com.mongodb.client.MongoDatabase, java.util.Collection, java.util.concurrent.ConcurrentHashMap, net.simon987.server.GameServer, net.simon987.server.IServerConfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Server/src/main/typescript/Console.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 145.24 | **LOC:** 209 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.128%), Tech Debt (37.4874%)
**Top Internal Functions/Classes:**
  * `handleConsoleBufferUpdate` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* /** * Handles a consoleBuffer update * @param {string[]} consoleBuffer A Cubot's internal buffer, as...
  * `toggleColor` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* /** * Toggle dark/light theme */
  * `toggleScrolling` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /** * Toggle auto scrolling. Also initially scrolls to bottom on click */
  * `constructor` **(State Mutators)** (Impact: 3.8)
  * `constructor` **(State Mutators)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 13`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 45`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 131.56 | **LOC:** 276 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9459%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `incrementLocation` **(I/O & Config Routines)** (Impact: 21.1)
    * *Intent:* /** * Increment the location of the game object by 1 tile * Collision checks happen here */
  * `getAdjacentTile` **(Interface Declarations)** (Impact: 9.8)
    * *Intent:* /** * Get the first directly adjacent tile (starting east, going clockwise) */
  * `getAdjacentTileCount` **(Compute Cores)** (Impact: 8.1)
  * `getFrontTile` **(Interface Declarations)** (Impact: 7.6)
  * `isAt` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 61`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`
* *Architecture:* `api: 26`, `import: 9`
* *Defense:* `safety: 1`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.743
  * `Choke Point (Betweenness):` 0.004277 | `Ripple Effect (Closeness):` 0.133389
  * `Imports (Out-Degree: 5):` java.awt.*, java.util.ArrayList, net.simon987.server.GameServer, net.simon987.server.game.world.Tile, net.simon987.server.game.world.World, net.simon987.server.io.JSONSerializable, net.simon987.server.io.MongoSerializable, org.bson.Document...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `Plugin NPC/src/main/java/net/simon987/npcplugin/NonPlayerCharacter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 124.84 | **LOC:** 256 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.052%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `gotoWorld` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* /** * Go to the next World in the specified Direction. * * @return true if the World in the specifie...
  * `moveTo` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* /** * Attempt to move the NPC to the specified coordinates * * @param range distance to the desired ...
  * `heal` **(Annotated Framework Methods)** (Impact: 3.3)
  * `damage` **(Annotated Framework Methods)** (Impact: 3.3)
  * `update` **(Annotated Framework Methods)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 38`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `doc: 11`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.util.ArrayList, net.simon987.server.GameServer, net.simon987.server.assembly.Util, net.simon987.server.game.objects.*, net.simon987.server.game.pathfinding.Node, net.simon987.server.game.pathfinding.Pathfinder, net.simon987.server.logging.LogManager, org.bson.Document
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 2.281** (Bridge: 0.0228 * Flux: 99.9933%)
- `Server/src/main/java/net/simon987/server/assembly/CPU.java` -> **Severity: 0.94** (Bridge: 0.0094 * Flux: 100.0%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 0.625** (Bridge: 0.0063 * Flux: 99.9993%)
- `Server/src/main/java/net/simon987/server/game/objects/GameObject.java` -> **Severity: 0.417** (Bridge: 0.0043 * Flux: 97.5094%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 0.398** (Bridge: 0.004 * Flux: 99.9947%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 19.527** (Embedded: 0.2178 * Error Risk: 89.6439%)
- `Server/src/main/java/net/simon987/server/game/world/World.java` -> **Severity: 14.202** (Embedded: 0.1517 * Error Risk: 93.5903%)
- `Server/src/main/java/net/simon987/server/user/User.java` -> **Severity: 13.844** (Embedded: 0.157 * Error Risk: 88.1519%)
- `Server/src/main/java/net/simon987/server/game/GameUniverse.java` -> **Severity: 13.839** (Embedded: 0.1448 * Error Risk: 95.5552%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 13.129** (Embedded: 0.2294 * Error Risk: 57.2346%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Server/src/main/java/net/simon987/server/ServerConfiguration.java` -> **Severity: 8916.9** (Blast Radius: 89.169 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/logging/LogManager.java` -> **Severity: 5187.2** (Blast Radius: 103.744 * Doc Risk: 50.0%)
- `Server/src/main/java/net/simon987/server/GameServer.java` -> **Severity: 3470.2** (Blast Radius: 34.702 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/io/MongoSerializable.java` -> **Severity: 2279.1** (Blast Radius: 22.791 * Doc Risk: 100.0%)
- `Server/src/main/java/net/simon987/server/game/objects/ControllableUnit.java` -> **Severity: 1720.1** (Blast Radius: 17.201 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
