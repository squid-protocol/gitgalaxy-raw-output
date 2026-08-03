# ARCHITECTURAL_BRIEF: css_doom_pure
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/css_doom_pure` |
| **Timestamp** | `2026-08-03T19:05:08.771198+00:00` |
| **Scan Duration** | `0.53s` |
| **Git Branch** | `main` |
| **Git Commit** | `8563252232822cb8aa825dd09bc594c13689494e` |
| **Git Remote** | `https://github.com/NielsLeenheer/cssDOOM.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 54 malicious artifacts.

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
| Total Artifacts | 1047 |
| Analyzed Artifacts (Scanned) | 95 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 952 |
| Total LOC | 5857 |
| Volatility Index | 0.021 |
| % Scanned of codebase = | 9.1% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0657 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | inf | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9951 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 54 | 3891 | 56.8% |
| CSS | 27 | 1752 | 28.4% |
| JSON | 9 | 9 | 9.5% |
| PLAINTEXT | 2 | 0 | 2.1% |
| MARKDOWN | 1 | 0 | 1.1% |
| HTML | 1 | 205 | 1.1% |
| XML | 1 | 0 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.835`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 47 | 49.5% |
| file_cluster_13 | 30 | 31.6% |
| file_cluster_2 | 3 | 3.2% |
| file_cluster_4 | 2 | 2.1% |
| file_cluster_0 | 1 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 9 | 9.5% |
| Static: Literature & Documentation | 3 | 3.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 952*

**Composition by Extension & Reason:**
- `.png`: 874x Excluded (Explicitly Denied Extension: '.png')
- `.wav`: 55x Excluded (Explicitly Denied Extension: '.wav')
- `.svg`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 63.9 | 15.4 | 8.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 12.8 | 4.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.6 | 2.6 | 80.0 |
| API Exposure | 0.0 | 17.4 | 5.9 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 63.7 | 83.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 34.0 | 1.4 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 20.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `index.html` (Hits: 43)
- `src/renderer/scene/surfaces/horizontal.js` (Hits: 5)
- `src/game/sound-propagation.js` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.css** (`index.css`) — 1 inbound connections
2. **camera.css** (`src/renderer/scene/camera.css`) — 1 inbound connections
3. **culling.css** (`src/renderer/scene/culling.css`) — 1 inbound connections
4. **decorations.css** (`src/renderer/scene/entities/decorations.css`) — 1 inbound connections
5. **enemies.css** (`src/renderer/scene/entities/enemies.css`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.css** (`index.css`) — 26 outbound dependencies
2. **index.js** (`index.js`) — 13 outbound dependencies
3. **scene.js** (`src/renderer/scene/scene.js`) — 13 outbound dependencies
4. **weapons.js** (`src/game/entities/weapons.js`) — 12 outbound dependencies
5. **ai.js** (`src/game/entities/ai.js`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `behindSkyWall` (@ `src/renderer/scene/culling.js`) -> Impact: **584.5** | LOC: 94
  * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from the player to the element and checks if it crosses ...
- `initKeyboardInput` (@ `src/input/keyboard.js`) -> Impact: **373.2** | LOC: 102
  * *Intent:* * ArrowRight = turn right (strafe if Z held) * A / , = strafe left * D / . = strafe right * Modifiers: Shift = run (2x speed) * Z = strafe modifier (a...
- `checkPickups` (@ `src/game/player/pickups.js`) -> Impact: **277.7** | LOC: 99
  * *Intent:* /** * Item collection logic and powerup duration management. * * Pickup collection logic: * - Each frame, all map things are checked against the playe...
- `moveEnemyToward` (@ `src/game/entities/ai.js`) -> Impact: **198.6** | LOC: 82
  * *Intent:* // Determine horizontal and vertical preferences (DOOM uses 10*FRACUNIT dead zone)
- `pickMoveDirection` (@ `src/game/entities/ai.js`) -> Impact: **193.8** | LOC: 75
- `buildSkyWalls` (@ `src/renderer/scene/surfaces/walls.js`) -> Impact: **165.7** | LOC: 110
- `rayHitPoint` (@ `src/game/physics.js`) -> Impact: **165.3** | LOC: 49
- `buildHorizontalSurface` (@ `src/renderer/scene/surfaces/horizontal.js`) -> Impact: **150.1** | LOC: 95
- `updateProjectiles` (@ `src/game/entities/projectiles.js`) -> Impact: **143.4** | LOC: 166
- `toggleDoor` (@ `src/game/mechanics/doors.js`) -> Impact: **142.1** | LOC: 70

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `behindSkyWall` (@ `src/renderer/scene/culling.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from the player to the element and checks if it crosses ...
- `spectate` (@ `src/ui/spectator.js`) -> **O(2^N) [Recursive]**
- `loadBuffer` (@ `src/audio/audio.js`) -> **O(2^N) [Recursive]**
- `toggleDoor` (@ `src/game/mechanics/doors.js`) -> **O(2^N) [Recursive]**
- `nearby` (@ `src/ui/debug.js`) -> **O(2^N) [Recursive]**
- `gameLoop` (@ `index.js`) -> **O(2^N) [Recursive]**
- `cullingLoop` (@ `src/renderer/scene/culling.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Run culling checks on all scene elements. Called each frame from the game loop.
- `save` (@ `src/ui/debug.js`) -> **O(2^N) [Recursive]**
- `toggleMenu` (@ `src/ui/menu.js`) -> **O(2^N) [Recursive]**
- `spectatorLoop` (@ `src/ui/spectator.js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `getLineOpening` (@ `src/game/sound-propagation.js`) -> DB Complexity: **11**
- `buildHorizontalSurface` (@ `src/renderer/scene/surfaces/horizontal.js`) -> DB Complexity: **11**
- `buildSkyWalls` (@ `src/renderer/scene/surfaces/walls.js`) -> DB Complexity: **11**
- `loadBuffer` (@ `src/audio/audio.js`) -> DB Complexity: **9**
- `updateProjectiles` (@ `src/game/entities/projectiles.js`) -> DB Complexity: **8**
- `nearby` (@ `src/ui/debug.js`) -> DB Complexity: **7**
- `hasLineOfSight` (@ `src/game/line-of-sight.js`) -> DB Complexity: **6**
- `buildSectorAdjacency` (@ `src/game/sound-propagation.js`) -> DB Complexity: **6**
  * *Intent:* /**
- `setupPointerHandlers` (@ `src/input/touch.js`) -> DB Complexity: **6**
- `getSectorDamageAt` (@ `src/game/player/damage.js`) -> DB Complexity: **5**
  * *Intent:* // ============================================================================ // Sector Damage // ==================================================...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/game` | 9 | 959.38 | 24.47% | 0.0% |
| `src/renderer/scene` | 9 | 918.44 | 13.98% | 0.0% |
| `src/game/entities` | 5 | 805.54 | 14.69% | 0.0% |
| `src/game/mechanics` | 5 | 726.12 | 26.78% | 0.0% |
| `src/input` | 5 | 673.6 | 25.76% | 0.0% |
| `src/ui` | 10 | 663.45 | 11.45% | 44.35% |
| `src/renderer/scene/surfaces` | 7 | 534.79 | 21.68% | 0.0% |
| `src/game/player` | 2 | 494.24 | 30.76% | 0.0% |
| `src/renderer/scene/entities` | 9 | 280.7 | 9.42% | 22.22% |
| `src/renderer` | 5 | 172.32 | 16.08% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/renderer/scene/entities/sprites.css` -> **100.0%** Exposure
- `src/renderer/scene/mechanics/lighting.css` -> **100.0%** Exposure
- `src/renderer/scene/entities/projectiles.css` -> **99.9996%** Exposure
- `src/ui/weapons.css` -> **99.9987%** Exposure
- `src/ui/menu.js` -> **99.9934%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/game/spatial-grid.js` -> **99.9959%** Exposure
- `src/game/sound-propagation.js` -> **99.9358%** Exposure
- `src/renderer/scene/surfaces/floors.js` -> **99.7902%** Exposure
- `src/renderer/scene/surfaces/walls.js` -> **96.8759%** Exposure
- `src/input/index.js` -> **94.9738%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/renderer/scene/entities/projectiles.css` -> **0** Orphaned Functions | **5** Duplicates
- `src/renderer/scene/mechanics/lighting.css` -> **0** Orphaned Functions | **5** Duplicates
- `src/ui/hud.css` -> **0** Orphaned Functions | **4** Duplicates
- `src/ui/weapons.css` -> **0** Orphaned Functions | **4** Duplicates
- `src/ui/spectator.js` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/input/keyboard.js`** -> AI Confidence: **99.48%**
2. **`src/game/player/pickups.js`** -> AI Confidence: **99.34%**
3. **`src/game/entities/ai.js`** -> AI Confidence: **99.31%**
4. **`src/game/entities/projectiles.js`** -> AI Confidence: **99.31%**
5. **`src/game/entities/weapons.js`** -> AI Confidence: **99.31%**
6. **`src/game/mechanics/switches.js`** -> AI Confidence: **99.31%**
7. **`src/game/mechanics/teleporters.js`** -> AI Confidence: **99.31%**
8. **`src/game/movement.js`** -> AI Confidence: **99.31%**
9. **`src/game/player/damage.js`** -> AI Confidence: **99.31%**
10. **`src/renderer/scene/entities/things.js`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/game/mechanics/lifts.js` -> **100.0%** Exposure
- `src/game/physics.js` -> **100.0%** Exposure
- `src/game/player/damage.js` -> **100.0%** Exposure
- `src/game/player/pickups.js` -> **100.0%** Exposure
- `src/ui/debug.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/audio/audio.js` -> **100.0%** Exposure
- `src/game/entities/ai.js` -> **100.0%** Exposure
- `src/game/entities/projectiles.js` -> **100.0%** Exposure
- `src/game/line-of-sight.js` -> **100.0%** Exposure
- `src/game/mechanics/lifts.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `30` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ui/spectator.js` (JAVASCRIPT) -> Cumulative Risk: **720.67**
- **Archetype:** `file_cluster_8` (Distance: 10.842 IQR)
- **Magnitude:** 266.98 | **LOC:** 346 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (96.5433%)
- **Heaviest Functions:** `spectatorLoop` (Impact: 79.4), `spectate` (Impact: 44.9), `transitionCeilings` (Impact: 37.2)

### 2. `src/game/physics.js` (JAVASCRIPT) -> Cumulative Risk: **707.98**
- **Archetype:** `file_cluster_13` (Distance: 11.421 IQR)
- **Magnitude:** 311.72 | **LOC:** 270 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `rayHitPoint` (Impact: 165.3), `getFloorHeightAt` (Impact: 63.6), `getSectorAt` (Impact: 47.9)

### 3. `src/game/player/damage.js` (JAVASCRIPT) -> Cumulative Risk: **701.23**
- **Archetype:** `file_cluster_13` (Distance: 10.584 IQR)
- **Magnitude:** 164.54 | **LOC:** 197 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getSectorDamageAt` (Impact: 63.8), `checkSectorDamage` (Impact: 32.1), `damagePlayer` (Impact: 29.4)

### 4. `src/audio/audio.js` (JAVASCRIPT) -> Cumulative Risk: **698.02**
- **Archetype:** `file_cluster_4` (Distance: 10.616 IQR)
- **Magnitude:** 94.18 | **LOC:** 88 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (93.4397%)
- **Heaviest Functions:** `loadBuffer` (Impact: 28.7), `setupUnlock` (Impact: 27.5), `playSound` (Impact: 10.9)

### 5. `src/game/spatial-grid.js` (JAVASCRIPT) -> Cumulative Risk: **651.44**
- **Archetype:** `file_cluster_8` (Distance: 13.002 IQR)
- **Magnitude:** 224.16 | **LOC:** 192 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9959%), Logic Bomb (99.9939%)
- **Heaviest Functions:** `forEachSightLineInAABB` (Impact: 74.7), `forEachWallInAABB` (Impact: 62.4), `forEachSectorAt` (Impact: 52.8)

### 6. `src/renderer/scene/entities/things.js` (JAVASCRIPT) -> Cumulative Risk: **633.39**
- **Archetype:** `file_cluster_13` (Distance: 10.249 IQR)
- **Magnitude:** 103.06 | **LOC:** 127 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `buildThings` (Impact: 91.0)

### 7. `src/game/entities/projectiles.js` (JAVASCRIPT) -> Cumulative Risk: **614.95**
- **Archetype:** `file_cluster_13` (Distance: 10.413 IQR)
- **Magnitude:** 171.18 | **LOC:** 227 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9916%), Verification (80.0%)
- **Heaviest Functions:** `updateProjectiles` (Impact: 143.4)

### 8. `src/game/sound-propagation.js` (JAVASCRIPT) -> Cumulative Risk: **612.0**
- **Archetype:** `file_cluster_8` (Distance: 12.733 IQR)
- **Magnitude:** 89.68 | **LOC:** 167 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9358%), Verification (80.0%)
- **Heaviest Functions:** `buildSectorAdjacency` (Impact: 36.2), `getLineOpening` (Impact: 19.5), `clearSoundAlert` (Impact: 2.0)

### 9. `src/game/entities/ai.js` (JAVASCRIPT) -> Cumulative Risk: **588.73**
- **Archetype:** `file_cluster_13` (Distance: 11.567 IQR)
- **Magnitude:** 436.62 | **LOC:** 491 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9962%), Churn (94.64%)
- **Heaviest Functions:** `moveEnemyToward` (Impact: 198.6), `pickMoveDirection` (Impact: 193.8), `rollMeleeDamage` (Impact: 18.6)

### 10. `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT) -> Cumulative Risk: **588.55**
- **Archetype:** `file_cluster_13` (Distance: 11.284 IQR)
- **Magnitude:** 207.24 | **LOC:** 230 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9442%), State Flux (96.8759%)
- **Heaviest Functions:** `buildSkyWalls` (Impact: 165.7), `createWallElement` (Impact: 5.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/renderer/scene/culling.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.184 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.222 IQR)
- **Top Global Matches:** file_cluster_8: 10.184, file_cluster_13: 10.576, file_cluster_7: 10.669
- **Magnitude:** 751.48 | **LOC:** 450 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (20.0754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `behindSkyWall` (Impact: 584.5 | O(2^N) | DB: 4)
    * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from t...
  * `surfaceInFrustum` (Impact: 49.2 | O(N^2))
    * *Intent:* /** * Tests whether a surface bounding box is within the frustum. * Checks corners, center, and whet...
  * `rayIntersectsAABB` (Impact: 41.7 | O(N^2) | DB: 2)
    * *Intent:* /** * Tests whether a ray from (ox,oy) in direction (dx,dy) intersects an AABB. * Uses the slab meth...
  * `wallInFrustum` (Impact: 20.9 | O(N^2))
  * `cullingLoop` (Impact: 10.8 | O(2^N))
    * *Intent:* /** * Run culling checks on all scene elements. Called each frame from the game loop.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 25`, `args: 8`, `func_start: 18`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 9`, `doc: 7`, `immutability_locks: 47`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spectator.js, dom.js, state.js, constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/entities/ai.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.567 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.826 IQR)
- **Top Global Matches:** file_cluster_13: 11.567, file_cluster_8: 11.698, file_cluster_7: 12.113
- **Magnitude:** 436.62 | **LOC:** 491 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (26.2098%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `moveEnemyToward` (Impact: 198.6 | O(N^5) | DB: 3)
    * *Intent:* // Determine horizontal and vertical preferences (DOOM uses 10*FRACUNIT dead zone)
  * `pickMoveDirection` (Impact: 193.8 | O(N^4) | DB: 3)
  * `rollMeleeDamage` (Impact: 18.6 | O(N^2))
    * *Intent:* // ============================================================================ // Enemy AI // =====...
  * `canWalkDir` (Impact: 5.6 | O(N^1))
    * *Intent:* // ============================================================================ // DOOM-style 8-dire...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 35`, `args: 6`, `func_start: 17`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `safety: 18`, `doc: 7`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` projectiles.js, enemies.js, physics.js, combat.js, audio.js, sound-propagation.js, constants.js, state.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/keyboard.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.721 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.165 IQR)
- **Top Global Matches:** file_cluster_13: 8.721, file_cluster_8: 9.069, file_cluster_7: 9.582
- **Magnitude:** 379.76 | **LOC:** 159 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (27.8953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initKeyboardInput` (Impact: 373.2 | O(N^4) | DB: 1)
    * *Intent:* * ArrowRight = turn right (strafe if Z held) * A / , = strafe left * D / . = strafe right * Modifier...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weapons.js, switches.js, index.js, lifts.js, menu.js, doors.js, state.js, constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.359 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.063 IQR)
- **Top Global Matches:** file_cluster_8: 10.359, file_cluster_13: 10.564, file_cluster_7: 10.813
- **Magnitude:** 330.88 | **LOC:** 372 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `nearby` (Impact: 139.0 | O(2^N) | DB: 7)
  * `initDebugMenu` (Impact: 68.8 | O(N^5) | DB: 3)
  * `updateDebugStats` (Impact: 32.1 | O(N^3) | DB: 1)
  * `load` (Impact: 11.8 | O(N^2) | DB: 5)
  * `dump` (Impact: 11.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 32`, `args: 19`, `func_start: 11`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spatial-grid.js, culling.js, dom.js, camera.js, physics.js, constants.js, maps.js, constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/player/pickups.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.218 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.245 IQR)
- **Top Global Matches:** file_cluster_8: 11.218, file_cluster_13: 11.237, file_cluster_7: 11.609
- **Magnitude:** 329.7 | **LOC:** 199 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.1336%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkPickups` (Impact: 277.7 | O(N^6) | DB: 3)
    * *Intent:* /** * Item collection logic and powerup duration management. * * Pickup collection logic: * - Each f...
  * `updatePowerups` (Impact: 25.1 | O(N^3))
    * *Intent:* // ============================================================================ // Powerups // =====...
  * `activatePowerup` (Impact: 5.7 | O(N^2))
    * *Intent:* // ============================================================================
  * `triggerPickupFlash` (Impact: 1.9 | O(N^1))
  * `hasPowerup` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 12`, `args: 5`, `func_start: 12`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weapons.js, audio.js, constants.js, state.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/physics.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.421 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.818 IQR)
- **Top Global Matches:** file_cluster_13: 11.421, file_cluster_8: 11.597, file_cluster_11: 11.933
- **Magnitude:** 311.72 | **LOC:** 270 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (31.3163%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rayHitPoint` (Impact: 165.3 | O(N^6) | DB: 1)
  * `getFloorHeightAt` (Impact: 63.6 | O(N^5) | DB: 3)
  * `getSectorAt` (Impact: 47.9 | O(N^5) | DB: 3)
  * `getSectorLightAt` (Impact: 7.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 30`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 5`, `doc: 6`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` geometry.js, state.js, constants.js, doors.js, spatial-grid.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/doors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.996 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.329 IQR)
- **Top Global Matches:** file_cluster_13: 11.996, file_cluster_8: 12.265, file_cluster_17: 12.455
- **Magnitude:** 298.16 | **LOC:** 203 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (27.2895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `toggleDoor` (Impact: 142.1 | O(2^N) | DB: 1)
  * `initDoors` (Impact: 123.3 | O(N^4) | DB: 3)
  * `getDoorEntry` (Impact: 7.1 | O(N^1))
    * *Intent:* /** * Doors * * Handles door initialization, toggling, and player interaction. * * How doors work: *...
  * `isDoorClosed` (Impact: 3.7 | O(N^1))
    * *Intent:* * How doors work: * - Visual animation: The renderer smoothly animates the door's face walls and * c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 23`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 17`, `doc: 6`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, audio.js, constants.js, state.js, maps.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/spectator.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.842 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.454 IQR)
- **Top Global Matches:** file_cluster_8: 10.842, file_cluster_2: 10.875, file_cluster_17: 11.071
- **Magnitude:** 266.98 | **LOC:** 346 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.1094%), Tech Debt (91.7325%)
**Top Internal Functions/Classes:**
  * `spectatorLoop` (Impact: 79.4 | O(2^N))
  * `spectate` (Impact: 44.9 | O(2^N))
  * `transitionCeilings` (Impact: 37.2 | O(N^5))
  * `updatePlayerSprite` (Impact: 29.4 | O(N^3) | DB: 2)
  * `spectatorDragStart` (Impact: 16.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 29`, `func_start: 31`
* *Risk/State:* `state_mutation: 20`, `duplicate_logic: 4`
* *Architecture:* `api: 2`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 23`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/spatial-grid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.002 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.489 IQR)
- **Top Global Matches:** file_cluster_8: 13.002, file_cluster_0: 13.27, file_cluster_13: 13.306
- **Magnitude:** 224.16 | **LOC:** 192 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (53.1844%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `forEachSightLineInAABB` (Impact: 74.7 | O(N^4) | DB: 4)
  * `forEachWallInAABB` (Impact: 62.4 | O(N^4) | DB: 4)
    * *Intent:* /**
  * `forEachSectorAt` (Impact: 52.8 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 6`
* *Defense:* `safety: 10`, `doc: 3`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` maps.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.284 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.925 IQR)
- **Top Global Matches:** file_cluster_13: 11.284, file_cluster_8: 11.329, file_cluster_7: 11.699
- **Magnitude:** 207.24 | **LOC:** 230 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (49.9915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildSkyWalls` (Impact: 165.7 | O(N^4) | DB: 11)
  * `createWallElement` (Impact: 5.3 | O(N^1))
    * *Intent:* /** * Wall element creation and scene wall construction. * * Provides both: * - createWallElement():...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 13`, `args: 2`, `func_start: 3`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants.js, dom.js, maps.js, sectors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/surfaces/horizontal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.005 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.301 IQR)
- **Top Global Matches:** file_cluster_8: 11.005, file_cluster_17: 11.341, file_cluster_7: 11.417
- **Magnitude:** 193.38 | **LOC:** 131 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (22.4485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildHorizontalSurface` (Impact: 150.1 | O(N^4) | DB: 11)
  * `isRectangular` (Impact: 26.2 | O(N^2))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 10`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 13`
* *Architecture:* `io: 5`, `api: 2`
* *Defense:* `safety: 11`, `doc: 4`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants.js, dom.js, sectors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/entities/projectiles.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.413 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.789 IQR)
- **Top Global Matches:** file_cluster_13: 10.413, file_cluster_8: 10.453, file_cluster_7: 10.881
- **Magnitude:** 171.18 | **LOC:** 227 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (19.2662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateProjectiles` (Impact: 143.4 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 3`, `func_start: 12`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, combat.js, audio.js, weapons.js, constants.js, state.js, damage.js, line-of-sight.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/player/damage.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.584 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.888 IQR)
- **Top Global Matches:** file_cluster_13: 10.584, file_cluster_8: 10.713, file_cluster_7: 11.175
- **Magnitude:** 164.54 | **LOC:** 197 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (25.3825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSectorDamageAt` (Impact: 63.8 | O(N^5) | DB: 5)
    * *Intent:* // ============================================================================ // Sector Damage // ...
  * `checkSectorDamage` (Impact: 32.1 | O(N^3))
  * `damagePlayer` (Impact: 29.4 | O(N^3) | DB: 1)
    * *Intent:* // ============================================================================ // Player Damage // ...
  * `clearSceneState` (Impact: 8.5 | O(N^2) | DB: 1)
    * *Intent:* // ============================================================================ // Game State Reset ...
  * `resetGameState` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 24`, `args: 7`, `func_start: 15`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spatial-grid.js, weapons.js, geometry.js, audio.js, constants.js, state.js, index.js, hud.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/lifts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.494 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.831 IQR)
- **Top Global Matches:** file_cluster_8: 11.494, file_cluster_7: 11.883, file_cluster_0: 11.972
- **Magnitude:** 156.5 | **LOC:** 212 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (39.3568%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tryUseLift` (Impact: 58.8 | O(N^5) | DB: 2)
  * `checkWalkOverTriggers` (Impact: 53.9 | O(N^5) | DB: 3)
  * `updatePlayerFromLift` (Impact: 18.4 | O(N^3) | DB: 1)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 12`, `args: 3`, `func_start: 5`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 6`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio.js, constants.js, state.js, maps.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/entities/sprites.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.95 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.69 IQR)
- **Top Global Matches:** file_cluster_8: 10.95, file_cluster_13: 11.213, file_cluster_7: 11.28
- **Magnitude:** 150.3 | **LOC:** 248 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.4474%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resetEnemy` (Impact: 25.2 | O(N^3))
  * `updateEnemyRotation` (Impact: 22.4 | O(N^2) | DB: 2)
  * `setEnemyState` (Impact: 18.6 | O(N^2))
  * `reparentThingToSector` (Impact: 16.1 | O(N^2))
  * `setSpriteFrame` (Impact: 9.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 26`, `args: 15`, `func_start: 17`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `safety: 12`, `doc: 11`, `immutability_locks: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/line-of-sight.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.634 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.548 IQR)
- **Top Global Matches:** file_cluster_13: 9.634, file_cluster_8: 9.697, file_cluster_7: 10.228
- **Magnitude:** 144.98 | **LOC:** 104 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.6184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasLineOfSight` (Impact: 129.4 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `doc: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` geometry.js, state.js, constants.js, doors.js, physics.js, spatial-grid.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/touch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.78 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.2 IQR)
- **Top Global Matches:** file_cluster_13: 10.78, file_cluster_8: 10.882, file_cluster_11: 11.305
- **Magnitude:** 137.24 | **LOC:** 262 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.4118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupPointerHandlers` (Impact: 83.0 | O(N^3) | DB: 6)
  * `handleDeadRestart` (Impact: 8.1 | O(N^2))
  * `initTouchInput` (Impact: 5.5 | O(N^1))
    * *Intent:* // Track active pointers by ID so multi-touch works (joystick + look + fire)
  * `createTouchUI` (Impact: 3.2 | O(N^1))
  * `getInput` (Impact: 2.0 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 48`, `args: 18`, `func_start: 20`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weapons.js, switches.js, index.js, menu.js, lifts.js, doors.js, state.js, maps.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/switches.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.96 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.425 IQR)
- **Top Global Matches:** file_cluster_13: 11.96, file_cluster_11: 12.539, file_cluster_4: 12.551
- **Magnitude:** 131.3 | **LOC:** 107 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (25.8836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tryUseSwitch` (Impact: 124.2 | O(N^6) | DB: 1)
    * *Intent:* * Switch interaction and action triggering. * * How switch interaction works: * 1. When the player p...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 12`, `args: 2`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` constants.js, state.js, maps.js, crushers.js, doors.js, lifts.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/teleporters.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.111 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.079 IQR)
- **Top Global Matches:** file_cluster_13: 10.111, file_cluster_8: 10.445, file_cluster_7: 10.901
- **Magnitude:** 124.6 | **LOC:** 100 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (32.9763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkTeleporters` (Impact: 112.5 | O(N^5) | DB: 3)
    * *Intent:* /** * Teleporters * * Walk-over teleporter linedefs that instantly move the player to a destination ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 12`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, audio.js, constants.js, state.js, maps.js, combat.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/surfaces/floors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.437 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.033 IQR)
- **Top Global Matches:** file_cluster_13: 12.437, file_cluster_8: 12.813, file_cluster_0: 13.065
- **Magnitude:** 112.5 | **LOC:** 69 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (51.9619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lowerTaggedFloor` (Impact: 84.5 | O(N^4) | DB: 5)
  * `buildFloors` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 12`, `args: 2`, `func_start: 4`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` maps.js, dom.js, horizontal.js, audio.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/entities/weapons.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.281 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.024 IQR)
- **Top Global Matches:** file_cluster_13: 9.281, file_cluster_8: 9.325, file_cluster_7: 9.732
- **Magnitude:** 107.68 | **LOC:** 402 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.1075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkWeaponHit` (Impact: 55.7 | O(N^2) | DB: 2)
  * `rollWeaponDamage` (Impact: 25.0 | O(N^3))
    * *Intent:* /** * Fires the currently equipped weapon. This is the main entry point for all * weapon firing logi...
  * `equipWeapon` (Impact: 5.6 | O(N^1))
    * *Intent:* // ============================================================================ // Weapon Loading & ...
  * `stopAutoFire` (Impact: 5.6 | O(N^2))
  * `alertNearbyEnemies` (Impact: 1.9 | O(N^1))
    * *Intent:* /** * Fires the currently equipped weapon. This is the main entry point for all
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 23`, `args: 8`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* `safety: 3`, `doc: 9`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` enemies.js, physics.js, combat.js, audio.js, index.js, sound-propagation.js, state.js, constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/entities/things.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.249 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.775 IQR)
- **Top Global Matches:** file_cluster_13: 10.249, file_cluster_8: 10.603, file_cluster_7: 11.09
- **Magnitude:** 103.06 | **LOC:** 127 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (37.6402%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildThings` (Impact: 91.0 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` state.js, physics.js, constants.js, maps.js, constants.js, sectors.js, dom.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/audio/audio.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.616 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.998 IQR)
- **Top Global Matches:** file_cluster_4: 10.616, file_cluster_8: 11.011, file_cluster_15: 11.386
- **Magnitude:** 94.18 | **LOC:** 88 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (63.9103%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadBuffer` (Impact: 28.7 | O(2^N) | DB: 9)
  * `setupUnlock` (Impact: 27.5 | O(N^4))
    * *Intent:* /** * Audio playback using the Web Audio API. * * Sounds are fetched and decoded into AudioBuffers o...
  * `playSound` (Impact: 10.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 15`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/sound-propagation.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.733 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 5.185 IQR)
- **Top Global Matches:** file_cluster_8: 12.733, file_cluster_0: 12.954, file_cluster_7: 12.955
- **Magnitude:** 89.68 | **LOC:** 167 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (38.9449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildSectorAdjacency` (Impact: 36.2 | O(N^3) | DB: 6)
    * *Intent:* /**
  * `getLineOpening` (Impact: 19.5 | O(N^2) | DB: 11)
  * `clearSoundAlert` (Impact: 2.0 | O(N^1))
    * *Intent:* /** * Computes the vertical opening of a two-sided linedef, accounting for door state. * Based on: l...
  * `isSectorAlerted` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 8`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 3`, `api: 7`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, state.js, maps.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/gamepad.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.949 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.639 IQR)
- **Top Global Matches:** file_cluster_13: 9.949, file_cluster_8: 10.107, file_cluster_1: 10.333
- **Magnitude:** 88.4 | **LOC:** 170 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (17.4878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupGamepad` (Impact: 55.5 | O(N^3))
  * `handleDeadRestart` (Impact: 8.1 | O(N^2))
  * `initGamepadInput` (Impact: 6.0 | O(N^2))
  * `cycleWeapon` (Impact: 2.0 | O(N^1) | DB: 1)
    * *Intent:* // --- Analog stick polling: read raw axes each frame ---
  * `isGamepadConnected` (Impact: 1.9 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 44`, `args: 24`, `func_start: 18`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `doc: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weapons.js, switches.js, index.js, menu.js, lifts.js, doors.js, state.js, maps.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `index.html` (HTML) | Magnitude: 84.1 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 196, args: 78, api: 65, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/game/entities/projectiles.js` (JAVASCRIPT) | Magnitude: 171.18 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 113, immutability_locks: 38, branch: 25, state_mutation: 22
- `src/ui/menu.js` (JAVASCRIPT) | Magnitude: 41.22 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 18, func_start: 12, args: 10
- `src/game/entities/weapons.js` (JAVASCRIPT) | Magnitude: 107.68 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 100, branch: 27, immutability_locks: 27, structural_boundaries: 23
- `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT) | Magnitude: 207.24 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, branch: 37, state_mutation: 31, immutability_locks: 30
- `src/game/line-of-sight.js` (JAVASCRIPT) | Magnitude: 144.98 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, branch: 27, structural_boundaries: 26, immutability_locks: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/renderer/scene/mechanics/switches.js` (JAVASCRIPT) | Magnitude: 7.48 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: events: 3, branch: 2, api: 2, listeners: 2
- `src/ui/overlay.js` (JAVASCRIPT) | Magnitude: 17.3 | Delta: **0.363 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, api: 6, args: 5
- `src/renderer/dom.js` (JAVASCRIPT) | Magnitude: 17.5 | Delta: **0.555 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, ui_framework: 8, globals: 8, memory_alloc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/renderer/effects.js` (JAVASCRIPT) | Magnitude: 23.02 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 8, indent_spaces: 7, structural_boundaries: 6, concurrency: 6
- `src/audio/audio.js` (JAVASCRIPT) | Magnitude: 94.18 | Delta: **0.395 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 18, concurrency: 15, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `index.css` (CSS) | Magnitude: 0.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 26, import: 26
- `src/game/player/pickups.js` (JAVASCRIPT) | Magnitude: 329.7 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, branch: 51, listeners: 17, safety: 16
- `src/ui/spectator.js` (JAVASCRIPT) | Magnitude: 266.98 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 162, branch: 48, structural_boundaries: 36, func_start: 31
- `src/renderer/hud.js` (JAVASCRIPT) | Magnitude: 62.92 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, branch: 13, immutability_locks: 12, structural_boundaries: 7
- `src/input/index.js` (JAVASCRIPT) | Magnitude: 33.42 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 7, branch: 6, structural_boundaries: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `index.html` -> Churn: **62.13%** | Cog Load: 4.451% | Debt: 57.5635%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/game/entities/ai.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 436.62
- `src/game/player/pickups.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 329.7
- `src/game/physics.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 311.72
- `src/game/entities/projectiles.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 171.18
- `src/game/player/damage.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 164.54

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/game/constants.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/game/physics.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/game/player/damage.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/renderer/effects.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/renderer/index.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
