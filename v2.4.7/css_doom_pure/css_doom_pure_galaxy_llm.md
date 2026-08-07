# ARCHITECTURAL_BRIEF: css_doom_pure
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/css_doom_pure` |
| **Timestamp** | `2026-08-07T03:29:26.845490+00:00` |
| **Scan Duration** | `0.48s` |
| **Git Branch** | `main` |
| **Git Commit** | `8563252232822cb8aa825dd09bc594c13689494e` |
| **Git Remote** | `https://github.com/NielsLeenheer/cssDOOM.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 54 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 63.9 | 15.3 | 8.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 92.5 | 36.5 | 47.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.3 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.4 | 6.0 | 6.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 100.0 | 14.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 44.8 | 34.8 | 100.0 |
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

- `initKeyboardInput` (@ `src/input/keyboard.js`) -> Impact: **152.3** | LOC: 102
  * *Intent:* * ArrowRight = turn right (strafe if Z held) * A / , = strafe left * D / . = strafe right * Modifiers: Shift = run (2x speed) * Z = strafe modifier (a...
- `behindSkyWall` (@ `src/renderer/scene/culling.js`) -> Impact: **120.7** | LOC: 94
  * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from the player to the element and checks if it crosses ...
- `checkPickups` (@ `src/game/player/pickups.js`) -> Impact: **82.9** | LOC: 99
  * *Intent:* /** * Item collection logic and powerup duration management. * * Pickup collection logic: * - Each frame, all map things are checked against the playe...
- `pickMoveDirection` (@ `src/game/entities/ai.js`) -> Impact: **79.8** | LOC: 75
- `registerInputProvider` (@ `src/input/keyboard.js`) -> Impact: **79.1** | LOC: 58
  * *Intent:* * A / , = strafe left * D / . = strafe right * Modifiers: Shift = run (2x speed) * Z = strafe modifier (arrows strafe instead of turn) * Actions: Spac...
- `buildSkyWalls` (@ `src/renderer/scene/surfaces/walls.js`) -> Impact: **69.6** | LOC: 110
- `moveEnemyToward` (@ `src/game/entities/ai.js`) -> Impact: **68.9** | LOC: 82
  * *Intent:* // Determine horizontal and vertical preferences (DOOM uses 10*FRACUNIT dead zone)
- `hasLineOfSight` (@ `src/game/line-of-sight.js`) -> Impact: **66.8** | LOC: 83
- `buildHorizontalSurface` (@ `src/renderer/scene/surfaces/horizontal.js`) -> Impact: **62.9** | LOC: 95
- `updateProjectiles` (@ `src/game/entities/projectiles.js`) -> Impact: **53.3** | LOC: 166

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/game` | 9 | 640.98 | 24.47% | 10.8% |
| `src/game/entities` | 5 | 584.14 | 14.69% | 56.21% |
| `src/input` | 5 | 534.4 | 22.98% | 33.35% |
| `src/ui` | 10 | 394.44 | 11.45% | 45.18% |
| `src/renderer/scene` | 9 | 386.74 | 15.5% | 16.11% |
| `src/game/mechanics` | 5 | 349.82 | 26.78% | 0.0% |
| `src/renderer/scene/surfaces` | 7 | 283.69 | 21.68% | 0.0% |
| `src/game/player` | 2 | 280.24 | 23.89% | 99.19% |
| `src/renderer/scene/entities` | 9 | 190.4 | 9.42% | 30.94% |
| `src/renderer` | 5 | 137.12 | 16.03% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/renderer/scene/entities/sprites.css` -> **100.0%** Exposure
- `src/renderer/scene/mechanics/lighting.css` -> **100.0%** Exposure
- `src/ui/menu.js` -> **100.0%** Exposure
- `src/ui/spectator.js` -> **100.0%** Exposure
- `src/renderer/scene/entities/projectiles.css` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/game/spatial-grid.js` -> **99.9959%** Exposure
- `src/game/sound-propagation.js` -> **99.9358%** Exposure
- `src/renderer/scene/surfaces/floors.js` -> **99.7902%** Exposure
- `src/renderer/scene/surfaces/walls.js` -> **96.8759%** Exposure
- `src/input/index.js` -> **94.9738%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui/spectator.js` -> **0** Orphaned Functions | **18** Duplicates
- `src/game/entities/ai.js` -> **0** Orphaned Functions | **8** Duplicates
- `src/renderer/scene/entities/projectiles.css` -> **0** Orphaned Functions | **5** Duplicates
- `src/renderer/scene/mechanics/lighting.css` -> **0** Orphaned Functions | **5** Duplicates
- `src/input/gamepad.js` -> **0** Orphaned Functions | **5** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `30` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/shared/maps.js` (JAVASCRIPT) -> Cumulative Risk: **653.55**
- **Archetype:** `file_cluster_13` (Distance: 10.017 IQR)
- **Magnitude:** 69.24 | **LOC:** 98 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.7493%), Tech Debt (99.6695%)
- **Heaviest Functions:** `loadMap` (Impact: 15.8), `applyPlayerStart` (Impact: 5.6), `getNextMap` (Impact: 5.4)

### 2. `src/game/player/damage.js` (JAVASCRIPT) -> Cumulative Risk: **586.47**
- **Archetype:** `file_cluster_13` (Distance: 10.54 IQR)
- **Magnitude:** 118.74 | **LOC:** 197 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8968%), State Flux (93.8197%), Verification (80.0%)
- **Heaviest Functions:** `getSectorDamageAt` (Impact: 22.2), `forEachSectorAt` (Impact: 21.9), `checkSectorDamage` (Impact: 16.5)

### 3. `src/game/physics.js` (JAVASCRIPT) -> Cumulative Risk: **573.99**
- **Archetype:** `file_cluster_13` (Distance: 11.393 IQR)
- **Magnitude:** 192.32 | **LOC:** 270 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.1913%), State Flux (94.1307%), Verification (80.0%)
- **Heaviest Functions:** `rayHitPoint` (Impact: 49.0), `forEachWallInAABB` (Impact: 33.1), `getFloorHeightAt` (Impact: 22.0)

### 4. `src/renderer/scene/sectors.js` (JAVASCRIPT) -> Cumulative Risk: **562.94**
- **Archetype:** `file_cluster_13` (Distance: 10.844 IQR)
- **Magnitude:** 44.5 | **LOC:** 81 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Documentation (100.0%), Tech Debt (99.9797%), Spec Match (85.7143%), State Flux (84.8129%)
- **Heaviest Functions:** `buildSectorContainers` (Impact: 7.9), `appendToSector` (Impact: 7.3), `getSectorLight` (Impact: 5.4)

### 5. `src/audio/audio.js` (JAVASCRIPT) -> Cumulative Risk: **538.26**
- **Archetype:** `file_cluster_4` (Distance: 10.575 IQR)
- **Magnitude:** 68.08 | **LOC:** 88 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.9541%), State Flux (80.5918%)
- **Heaviest Functions:** `setupUnlock` (Impact: 11.9), `unlock` (Impact: 9.9), `loadBuffer` (Impact: 7.9)

### 6. `src/game/entities/ai.js` (JAVASCRIPT) -> Cumulative Risk: **520.22**
- **Archetype:** `file_cluster_13` (Distance: 11.499 IQR)
- **Magnitude:** 247.92 | **LOC:** 491 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9985%), Churn (94.64%), Verification (80.0%)
- **Heaviest Functions:** `pickMoveDirection` (Impact: 79.8), `moveEnemyToward` (Impact: 68.9), `updateAllEnemies` (Impact: 24.0)

### 7. `src/game/entities/projectiles.js` (JAVASCRIPT) -> Cumulative Risk: **510.96**
- **Archetype:** `file_cluster_13` (Distance: 10.37 IQR)
- **Magnitude:** 113.78 | **LOC:** 227 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (81.1048%), Verification (80.0%), Safety Score (59.8914%)
- **Heaviest Functions:** `updateProjectiles` (Impact: 53.3), `playSound` (Impact: 14.9), `spawnProjectile` (Impact: 10.2)

### 8. `src/renderer/scene/entities/sprites.js` (JAVASCRIPT) -> Cumulative Risk: **492.55**
- **Archetype:** `file_cluster_8` (Distance: 10.939 IQR)
- **Magnitude:** 119.0 | **LOC:** 248 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Tech Debt (78.4672%)
- **Heaviest Functions:** `updateEnemyRotation` (Impact: 15.5), `resetEnemy` (Impact: 13.0), `setEnemyState` (Impact: 12.7)

### 9. `src/renderer/effects.js` (JAVASCRIPT) -> Cumulative Risk: **488.53**
- **Archetype:** `file_cluster_4` (Distance: 10.776 IQR)
- **Magnitude:** 23.02 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9948%), Documentation (99.8829%), Safety Score (71.9772%)
- **Heaviest Functions:** `triggerFlash` (Impact: 2.0), `showPowerup` (Impact: 1.9), `hidePowerup` (Impact: 1.9)

### 10. `src/game/entities/combat.js` (JAVASCRIPT) -> Cumulative Risk: **476.48**
- **Archetype:** `file_cluster_13` (Distance: 10.856 IQR)
- **Magnitude:** 54.4 | **LOC:** 281 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9447%), State Flux (72.9626%), Safety Score (54.6614%)
- **Heaviest Functions:** `enemyHitscanAttackEnemy` (Impact: 15.3), `damageEnemy` (Impact: 10.6), `checkBossDeath` (Impact: 7.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/input/keyboard.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.702 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.165 IQR)
- **Top Global Matches:** file_cluster_13: 8.702, file_cluster_8: 9.049, file_cluster_7: 9.564
- **Magnitude:** 265.86 | **LOC:** 159 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.8953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initKeyboardInput` (Impact: 152.3)
    * *Intent:* * ArrowRight = turn right (strafe if Z held) * A / , = strafe left * D / . = strafe right * Modifier...
  * `registerInputProvider` (Impact: 79.1)
    * *Intent:* * A / , = strafe left * D / . = strafe right * Modifiers: Shift = run (2x speed) * Z = strafe modifi...
  * `getInput` (Impact: 23.2)
  * `toggleMenu` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 21`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, lifts.js, switches.js, menu.js, constants.js, state.js, maps.js, weapons.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/entities/ai.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.499 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.355 IQR)
- **Top Global Matches:** file_cluster_13: 11.499, file_cluster_8: 11.672, file_cluster_7: 12.075
- **Magnitude:** 247.92 | **LOC:** 491 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.2098%), Tech Debt (99.9985%)
**Top Internal Functions/Classes:**
  * `pickMoveDirection` (Impact: 79.8)
  * `moveEnemyToward` (Impact: 68.9)
    * *Intent:* // Determine horizontal and vertical preferences (DOOM uses 10*FRACUNIT dead zone)
  * `updateAllEnemies` (Impact: 24.0)
  * `rollMeleeDamage` (Impact: 12.6)
    * *Intent:* // ============================================================================ // Enemy AI // =====...
  * `commitDirection` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 35`, `args: 6`, `func_start: 17`
* *Risk/State:* `state_mutation: 14`, `duplicate_logic: 8`
* *Architecture:* `api: 5`, `import: 11`
* *Defense:* `safety: 18`, `doc: 7`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` enemies.js, line-of-sight.js, physics.js, damage.js, audio.js, state.js, projectiles.js, index.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/culling.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.163 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.277 IQR)
- **Top Global Matches:** file_cluster_8: 10.163, file_cluster_13: 10.547, file_cluster_7: 10.647
- **Magnitude:** 245.88 | **LOC:** 450 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.2073%), Tech Debt (45.0477%)
**Top Internal Functions/Classes:**
  * `behindSkyWall` (Impact: 120.7)
    * *Intent:* /** * Tests whether a sky wall segment lies between the player and the element. * Casts a ray from t...
  * `surfaceInFrustum` (Impact: 33.3)
    * *Intent:* /** * Tests whether a surface bounding box is within the frustum. * Checks corners, center, and whet...
  * `rayIntersectsAABB` (Impact: 28.2)
    * *Intent:* /** * Tests whether a ray from (ox,oy) in direction (dx,dy) intersects an AABB. * Uses the slab meth...
  * `wallInFrustum` (Impact: 14.3)
  * `pointInFrustum` (Impact: 5.5)
    * *Intent:* /** * Tests whether a point (relative to the player) is within the camera's * horizontal view frustu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 25`, `args: 8`, `func_start: 18`
* *Risk/State:* `state_mutation: 21`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 9`, `doc: 7`, `immutability_locks: 47`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spectator.js, dom.js, constants.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/physics.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.393 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.892 IQR)
- **Top Global Matches:** file_cluster_13: 11.393, file_cluster_8: 11.583, file_cluster_11: 11.912
- **Magnitude:** 192.32 | **LOC:** 270 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.3163%), Tech Debt (97.1913%)
**Top Internal Functions/Classes:**
  * `rayHitPoint` (Impact: 49.0)
  * `forEachWallInAABB` (Impact: 33.1)
    * *Intent:* // ============================================================================ // Linedef Crossing ...
  * `getFloorHeightAt` (Impact: 22.0)
  * `forEachSectorAt` (Impact: 20.1)
    * *Intent:* // Upper wall: block if opening is too small for the player. // Skip if the wall doesn't overlap the...
  * `getSectorAt` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 30`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 5`, `doc: 6`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spatial-grid.js, state.js, doors.js, constants.js, geometry.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/spectator.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.859 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.461 IQR)
- **Top Global Matches:** file_cluster_8: 10.859, file_cluster_2: 10.884, file_cluster_17: 11.059
- **Magnitude:** 177.08 | **LOC:** 346 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1094%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `spectatorLoop` (Impact: 27.4)
  * `updatePlayerSprite` (Impact: 15.5)
  * `transitionCeilings` (Impact: 13.2)
  * `spectate` (Impact: 10.9)
  * `spectatorLoop` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 36`, `args: 29`, `func_start: 31`
* *Risk/State:* `state_mutation: 20`, `duplicate_logic: 18`
* *Architecture:* `api: 3`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 23`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui/debug.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.356 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.063 IQR)
- **Top Global Matches:** file_cluster_8: 10.356, file_cluster_13: 10.561, file_cluster_7: 10.81
- **Magnitude:** 161.88 | **LOC:** 372 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `nearby` (Impact: 38.3)
  * `initDebugMenu` (Impact: 27.2)
  * `updateDebugStats` (Impact: 16.5)
  * `load` (Impact: 8.1)
  * `dump` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 32`, `args: 19`, `func_start: 11`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 2`, `api: 8`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` culling.js, physics.js, constants.js, dom.js, constants.js, camera.js, state.js, maps.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/player/pickups.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.19 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_8: 11.19, file_cluster_13: 11.195, file_cluster_7: 11.581
- **Magnitude:** 161.5 | **LOC:** 199 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.3946%), Tech Debt (98.4733%)
**Top Internal Functions/Classes:**
  * `checkPickups` (Impact: 82.9)
    * *Intent:* /** * Item collection logic and powerup duration management. * * Pickup collection logic: * - Each f...
  * `triggerPickupFlash` (Impact: 29.1)
  * `updatePowerups` (Impact: 13.0)
    * *Intent:* // ============================================================================ // Powerups // =====...
  * `triggerPickupFlash` (Impact: 6.8)
  * `equipWeapon` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 12`, `args: 5`, `func_start: 12`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio.js, state.js, index.js, constants.js, weapons.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/doors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.002 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.331 IQR)
- **Top Global Matches:** file_cluster_13: 12.002, file_cluster_8: 12.277, file_cluster_17: 12.465
- **Magnitude:** 160.06 | **LOC:** 203 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.2895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `initDoors` (Impact: 50.5)
  * `toggleDoor` (Impact: 38.1)
  * `tryOpenDoor` (Impact: 28.1)
    * *Intent:* /** * Toggle a door open. If already open, reset the auto-close timer. * The renderer handles the op...
  * `closeDoor` (Impact: 9.6)
  * `getDoorEntry` (Impact: 7.1)
    * *Intent:* /** * Doors * * Handles door initialization, toggling, and player interaction. * * How doors work: *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 23`, `args: 8`, `func_start: 9`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 17`, `doc: 6`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, audio.js, maps.js, state.js, index.js, constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/entities/weapons.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.286 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.027 IQR)
- **Top Global Matches:** file_cluster_13: 9.286, file_cluster_8: 9.345, file_cluster_7: 9.744
- **Magnitude:** 159.58 | **LOC:** 402 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.1075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkWeaponHit` (Impact: 39.2)
  * `spawnPlayerRocket` (Impact: 35.3)
    * *Intent:* // Continuous-fire weapons (chaingun): set up an auto-fire interval that
  * `rocketExplosion` (Impact: 24.1)
    * *Intent:* // ============================================================================ // Weapon Damage Rol...
  * `rollWeaponDamage` (Impact: 12.9)
    * *Intent:* /** * Fires the currently equipped weapon. This is the main entry point for all * weapon firing logi...
  * `damagePlayer` (Impact: 12.0)
    * *Intent:* // Based on: linuxdoom-1.10/p_map.c:P_LineAttack() — Berserk multiplies by 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 23`, `args: 8`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* `safety: 3`, `doc: 9`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` enemies.js, damage.js, physics.js, line-of-sight.js, audio.js, state.js, index.js, constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/line-of-sight.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.59 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.548 IQR)
- **Top Global Matches:** file_cluster_13: 9.59, file_cluster_8: 9.651, file_cluster_7: 10.185
- **Magnitude:** 131.88 | **LOC:** 104 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.6184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasLineOfSight` (Impact: 66.8)
  * `forEachSightLineInAABB` (Impact: 36.9)
  * `forEachWallInAABB` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `doc: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, spatial-grid.js, state.js, doors.js, constants.js, geometry.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/touch.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.765 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 10.765, file_cluster_8: 10.877, file_cluster_11: 11.295
- **Magnitude:** 125.44 | **LOC:** 262 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.02%), Tech Debt (66.7672%)
**Top Internal Functions/Classes:**
  * `setupPointerHandlers` (Impact: 44.9)
  * `stopAutoFire` (Impact: 5.9)
  * `releaseJoystick` (Impact: 5.6)
  * `releaseFire` (Impact: 5.6)
  * `initTouchInput` (Impact: 5.5)
    * *Intent:* // Track active pointers by ID so multi-touch works (joystick + look + fire)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 48`, `args: 18`, `func_start: 20`
* *Risk/State:* `state_mutation: 28`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 30`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, lifts.js, switches.js, menu.js, state.js, maps.js, weapons.js, doors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/entities/sprites.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.939 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.602 IQR)
- **Top Global Matches:** file_cluster_8: 10.939, file_cluster_13: 11.191, file_cluster_7: 11.268
- **Magnitude:** 119.0 | **LOC:** 248 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.4474%), Tech Debt (78.4672%)
**Top Internal Functions/Classes:**
  * `updateEnemyRotation` (Impact: 15.5)
  * `resetEnemy` (Impact: 13.0)
  * `setEnemyState` (Impact: 12.7)
  * `reparentThingToSector` (Impact: 10.9)
  * `setSpriteFrame` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 26`, `args: 15`, `func_start: 17`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 2`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `safety: 12`, `doc: 11`, `immutability_locks: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/player/damage.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.54 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_13: 10.54, file_cluster_8: 10.689, file_cluster_7: 11.151
- **Magnitude:** 118.74 | **LOC:** 197 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.3825%), Tech Debt (99.8968%)
**Top Internal Functions/Classes:**
  * `getSectorDamageAt` (Impact: 22.2)
    * *Intent:* // ============================================================================ // Sector Damage // ...
  * `forEachSectorAt` (Impact: 21.9)
    * *Intent:* // ============================================================================ // Sector Damage // ...
  * `checkSectorDamage` (Impact: 16.5)
  * `damagePlayer` (Impact: 15.6)
    * *Intent:* // ============================================================================ // Player Damage // ...
  * `clearSceneState` (Impact: 5.9)
    * *Intent:* // ============================================================================ // Game State Reset ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 24`, `args: 7`, `func_start: 15`
* *Risk/State:* `state_mutation: 17`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 4`, `doc: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` spatial-grid.js, audio.js, hud.js, state.js, geometry.js, index.js, constants.js, weapons.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/spatial-grid.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.002 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.489 IQR)
- **Top Global Matches:** file_cluster_8: 13.002, file_cluster_0: 13.27, file_cluster_13: 13.306
- **Magnitude:** 117.26 | **LOC:** 192 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.1844%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `forEachSightLineInAABB` (Impact: 30.6)
  * `forEachSectorAt` (Impact: 26.8)
  * `forEachWallInAABB` (Impact: 25.6)
    * *Intent:* /**
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

### `src/game/entities/projectiles.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.37 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.913 IQR)
- **Top Global Matches:** file_cluster_13: 10.37, file_cluster_8: 10.433, file_cluster_7: 10.854
- **Magnitude:** 113.78 | **LOC:** 227 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.2662%), Tech Debt (81.1048%)
**Top Internal Functions/Classes:**
  * `updateProjectiles` (Impact: 53.3)
  * `playSound` (Impact: 14.9)
  * `spawnProjectile` (Impact: 10.2)
  * `playSound` (Impact: 2.3)
  * `rocketExplosion` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 15`, `args: 3`, `func_start: 12`
* *Risk/State:* `state_mutation: 22`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 3`, `doc: 5`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` weapons.js, damage.js, physics.js, line-of-sight.js, audio.js, state.js, index.js, constants.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.259 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.925 IQR)
- **Top Global Matches:** file_cluster_13: 11.259, file_cluster_8: 11.303, file_cluster_7: 11.674
- **Magnitude:** 112.64 | **LOC:** 230 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildSkyWalls` (Impact: 69.6)
  * `createWallElement` (Impact: 5.3)
    * *Intent:* /** * Wall element creation and scene wall construction. * * Provides both: * - createWallElement():...
  * `appendToSector` (Impact: 1.5)
    * *Intent:* // Extend sky walls above the ceiling to occlude distant geometry.
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
- **Magnitude:** 97.58 | **LOC:** 131 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.4485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildHorizontalSurface` (Impact: 62.9)
  * `isRectangular` (Impact: 17.6)
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

### `index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 8.332 IQR)
- **Top Global Matches:** file_cluster_0: 8.332, file_cluster_8: 8.548, file_cluster_7: 9.092
- **Magnitude:** 84.1 | **LOC:** 230 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.451%), Tech Debt (57.5635%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 61`, `args: 78`, `class_start: 3`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* `io: 43`, `api: 65`, `import: 1`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` favicon.svg, icon.png, index.css, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/gamepad.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.921 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.131 IQR)
- **Top Global Matches:** file_cluster_13: 9.921, file_cluster_8: 10.106, file_cluster_1: 10.332
- **Magnitude:** 81.9 | **LOC:** 170 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9442%), Tech Debt (99.9972%)
**Top Internal Functions/Classes:**
  * `setupGamepad` (Impact: 29.5)
  * `tryUseLift` (Impact: 5.7)
  * `handleDeadRestart` (Impact: 5.5)
  * `initGamepadInput` (Impact: 4.3)
  * `stopAutoFire` (Impact: 3.9)
    * *Intent:* // ============================================================================ // Gamepad Binding /...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 44`, `args: 24`, `func_start: 18`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 5`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `doc: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, lifts.js, switches.js, menu.js, state.js, maps.js, weapons.js, doors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/game/mechanics/lifts.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.494 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.831 IQR)
- **Top Global Matches:** file_cluster_8: 11.494, file_cluster_7: 11.883, file_cluster_0: 11.972
- **Magnitude:** 75.1 | **LOC:** 212 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3568%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tryUseLift` (Impact: 20.7)
  * `checkWalkOverTriggers` (Impact: 19.2)
  * `updatePlayerFromLift` (Impact: 9.8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 12`, `args: 3`, `func_start: 5`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 6`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` audio.js, maps.js, state.js, index.js, constants.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shared/maps.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.017 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_13: 10.017, file_cluster_4: 10.149, file_cluster_8: 10.386
- **Magnitude:** 69.24 | **LOC:** 98 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.62%), Tech Debt (99.6695%)
**Top Internal Functions/Classes:**
  * `loadMap` (Impact: 15.8)
  * `applyPlayerStart` (Impact: 5.6)
    * *Intent:* // Drop camera from intro height to eye level after scene is ready
  * `getNextMap` (Impact: 5.4)
    * *Intent:* /** * Sets player position and angle from the current map's start data.
  * `transitionToLevel` (Impact: 3.9)
  * `applyPlayerStart` (Impact: 3.4)
    * *Intent:* /** * Fetches a map JSON and applies it to game state: sets player position, * resets game/level sta...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 25`, `args: 7`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 9`, `import: 6`
* *Defense:* `doc: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` damage.js, scene.js, constants.js, overlay.js, sound-propagation.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/audio/audio.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.575 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.404 IQR)
- **Top Global Matches:** file_cluster_4: 10.575, file_cluster_8: 11.008, file_cluster_15: 11.383
- **Magnitude:** 68.08 | **LOC:** 88 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9103%), Tech Debt (99.9541%)
**Top Internal Functions/Classes:**
  * `setupUnlock` (Impact: 11.9)
    * *Intent:* /** * Audio playback using the Web Audio API. * * Sounds are fetched and decoded into AudioBuffers o...
  * `unlock` (Impact: 9.9)
    * *Intent:* /** * Audio playback using the Web Audio API. * * Sounds are fetched and decoded into AudioBuffers o...
  * `loadBuffer` (Impact: 7.9)
  * `playSound` (Impact: 7.5)
  * `loadBuffer` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 2`
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
- **Magnitude:** 66.28 | **LOC:** 167 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.9449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildSectorAdjacency` (Impact: 18.9)
    * *Intent:* /**
  * `getLineOpening` (Impact: 13.4)
  * `clearSoundAlert` (Impact: 2.0)
    * *Intent:* /** * Computes the vertical opening of a two-sided linedef, accounting for door state. * Based on: l...
  * `isSectorAlerted` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 8`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 3`, `api: 7`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` physics.js, maps.js, state.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/scene.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.488 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.666 IQR)
- **Top Global Matches:** file_cluster_13: 10.488, file_cluster_4: 10.745, file_cluster_8: 11.044
- **Magnitude:** 63.56 | **LOC:** 119 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.5192%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `preloadTextures` (Impact: 22.7)
  * `teardownScene` (Impact: 4.5)
  * `onComplete` (Impact: 3.6)
  * `buildScene` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 20`, `args: 5`, `func_start: 18`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 4`, `concurrency: 15`, `import: 13`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` camera.js, floors.js, player.js, spatial-grid.js, sectors.js, lifts.js, things.js, dom.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/scene/surfaces/floors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.437 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.033 IQR)
- **Top Global Matches:** file_cluster_13: 12.437, file_cluster_8: 12.813, file_cluster_0: 13.065
- **Magnitude:** 60.5 | **LOC:** 69 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.9619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lowerTaggedFloor` (Impact: 35.1)
  * `buildFloors` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 12`, `args: 2`, `func_start: 4`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dom.js, maps.js, horizontal.js, audio.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `index.html` (HTML) | Magnitude: 84.1 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 196, args: 78, api: 65, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/ui/menu.js` (JAVASCRIPT) | Magnitude: 32.22 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 18, func_start: 12, args: 10
- `src/renderer/scene/surfaces/walls.js` (JAVASCRIPT) | Magnitude: 112.64 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, branch: 37, state_mutation: 31, immutability_locks: 30
- `src/game/entities/weapons.js` (JAVASCRIPT) | Magnitude: 159.58 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 100, branch: 27, immutability_locks: 27, structural_boundaries: 23
- `src/game/line-of-sight.js` (JAVASCRIPT) | Magnitude: 131.88 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, branch: 27, structural_boundaries: 26, immutability_locks: 20
- `src/game/entities/projectiles.js` (JAVASCRIPT) | Magnitude: 113.78 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 113, immutability_locks: 38, branch: 25, state_mutation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/renderer/scene/mechanics/switches.js` (JAVASCRIPT) | Magnitude: 7.48 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: events: 3, branch: 2, api: 2, listeners: 2
- `src/ui/overlay.js` (JAVASCRIPT) | Magnitude: 16.5 | Delta: **0.363 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, api: 6, args: 5
- `src/renderer/dom.js` (JAVASCRIPT) | Magnitude: 17.5 | Delta: **0.555 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, ui_framework: 8, globals: 8, memory_alloc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/renderer/effects.js` (JAVASCRIPT) | Magnitude: 23.02 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 8, indent_spaces: 7, structural_boundaries: 6, concurrency: 6
- `src/audio/audio.js` (JAVASCRIPT) | Magnitude: 68.08 | Delta: **0.433 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 18, concurrency: 15, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `index.css` (CSS) | Magnitude: 0.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 26, import: 26
- `src/game/player/pickups.js` (JAVASCRIPT) | Magnitude: 161.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, branch: 51, listeners: 17, safety: 16
- `src/ui/spectator.js` (JAVASCRIPT) | Magnitude: 177.08 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 162, branch: 48, structural_boundaries: 36, func_start: 31
- `src/renderer/hud.js` (JAVASCRIPT) | Magnitude: 37.82 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, branch: 13, immutability_locks: 12, structural_boundaries: 7
- `src/input/index.js` (JAVASCRIPT) | Magnitude: 27.32 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 7, branch: 6, structural_boundaries: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/game/entities/ai.js` -> Churn: **94.64%** | Cog Load: 26.2098% | Debt: 99.9985%
- `src/renderer/scene/entities/sprites.js` -> Churn: **63.09%** | Cog Load: 8.4474% | Debt: 78.4672%
- `index.html` -> Churn: **62.13%** | Cog Load: 4.451% | Debt: 57.5635%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/game/entities/ai.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 247.92
- `src/game/physics.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 192.32
- `src/game/player/pickups.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 161.5
- `src/game/entities/weapons.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 159.58
- `src/renderer/scene/entities/sprites.js` -> **Niels Leenheer** (100.0% isolated ownership) | Magnitude: 119.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/game/constants.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/renderer/index.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/renderer/scene/entities/sprites.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/renderer/scene/sectors.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)
- `src/shared/maps.js` -> **Severity: 1030.3** (Blast Radius: 10.303 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
