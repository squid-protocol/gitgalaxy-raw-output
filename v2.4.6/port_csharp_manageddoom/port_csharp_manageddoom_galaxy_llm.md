# ARCHITECTURAL_BRIEF: port_csharp_manageddoom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/port_csharp_manageddoom` |
| **Timestamp** | `2026-08-03T19:06:12.590645+00:00` |
| **Scan Duration** | `1.08s` |
| **Git Branch** | `master` |
| **Git Commit** | `9365696eb44326a3aab72c4bab217f7db8a87c96` |
| **Git Remote** | `https://github.com/sinshu/managed-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 244 malicious artifacts.

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
| Total Artifacts | 350 |
| Analyzed Artifacts (Scanned) | 245 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 105 |
| Total LOC | 38885 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 243 | 38879 | 99.2% |
| MARKDOWN | 1 | 0 | 0.4% |
| BATCH | 1 | 6 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.676`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 238 | 97.1% |
| file_cluster_13 | 5 | 2.0% |
| file_cluster_0 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 105*

**Composition by Extension & Reason:**
- `.lmp`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wad`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.csproj`: 1x Excluded (Unsupported Extension: '.csproj'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cs`: 1x Excluded (Embedded Array/Matrix Payload: 8705 commas in 999 LOC), 1x Excluded (Embedded Array/Matrix Payload: 16385 commas in 2086 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.slnx`: 1x Excluded (Unsupported Extension: '.slnx')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.9 | 20.0 | 12.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.4 | 46.9 | 58.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.8 | 16.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 29.8 | 2.5 | 80.0 |
| API Exposure | 0.0 | 17.6 | 5.7 | 5.5 | 4.1 |
| Concurrency Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 58.1 | 83.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 12.8 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 40.0 | 100.0 | 96.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.7 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 4.8 | 100.0 | 74.1 | 99.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 67.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 61.2 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ManagedDoom/src/ConfigUtilities.cs` (Hits: 8)
- `ManagedDoom/src/Doom/Wad/Wad.cs` (Hits: 4)
- `ManagedDoom/src/Doom/DeHackEd.cs` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ApplicationInfo.cs** (`ManagedDoom/src/ApplicationInfo.cs`) — 0 inbound connections
2. **Bgm.cs** (`ManagedDoom/src/Audio/Bgm.cs`) — 0 inbound connections
3. **IMusic.cs** (`ManagedDoom/src/Audio/IMusic.cs`) — 0 inbound connections
4. **ISound.cs** (`ManagedDoom/src/Audio/ISound.cs`) — 0 inbound connections
5. **NullMusic.cs** (`ManagedDoom/src/Audio/NullMusic.cs`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **SilkDoom.cs** (`ManagedDoom/src/Silk/SilkDoom.cs`) — 8 outbound dependencies
2. **SilkVideo.cs** (`ManagedDoom/src/Silk/SilkVideo.cs`) — 7 outbound dependencies
3. **DeHackEd.cs** (`ManagedDoom/src/Doom/DeHackEd.cs`) — 6 outbound dependencies
4. **SilkMusic.cs** (`ManagedDoom/src/Silk/SilkMusic.cs`) — 6 outbound dependencies
5. **ConfigUtilities.cs** (`ManagedDoom/src/ConfigUtilities.cs`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `UseTraverse` (@ `ManagedDoom/src/Doom/World/MapInteraction.cs`) -> Impact: **844.6** | LOC: 1016
- `TouchSpecialThing` (@ `ManagedDoom/src/Doom/World/ItemPickup.cs`) -> Impact: **809.1** | LOC: 421
- `Update` (@ `ManagedDoom/src/Doom/Opening/OpeningSequence.cs`) -> Impact: **777.3** | LOC: 146
- `ToString` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **774.7** | LOC: 210
- `Parse` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **774.7** | LOC: 210
- `SilkToDoom` (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **631.0** | LOC: 128
- `DoomToSilk` (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **611.6** | LOC: 108
- `GetChar` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **514.5** | LOC: 130
- `DoEvent` (@ `ManagedDoom/src/Doom/Menu/SelectableMenu.cs`) -> Impact: **417.4** | LOC: 118
- `BossDeath` (@ `ManagedDoom/src/Doom/World/MonsterBehavior.cs`) -> Impact: **407.8** | LOC: 173

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Update` (@ `ManagedDoom/src/Doom/Doom.cs`) -> **O(2^N) [Recursive]**
- `TextureAnimation` (@ `ManagedDoom/src/Doom/Graphics/TextureAnimation.cs`) -> **O(2^N) [Recursive]**
- `Map` (@ `ManagedDoom/src/Doom/Map/Map.cs`) -> **O(2^N) [Recursive]**
- `DoEvent` (@ `ManagedDoom/src/Doom/Menu/DoomMenu.cs`) -> **O(2^N) [Recursive]**
- `DoEvent` (@ `ManagedDoom/src/Doom/Menu/SelectableMenu.cs`) -> **O(2^N) [Recursive]**
- `Update` (@ `ManagedDoom/src/Doom/Opening/OpeningSequence.cs`) -> **O(2^N) [Recursive]**
- `TraverseIntercepts` (@ `ManagedDoom/src/Doom/World/PathTraversal.cs`) -> **O(2^N) [Recursive]**
- `Run` (@ `ManagedDoom/src/Doom/World/Thinkers.cs`) -> **O(2^N) [Recursive]**
- `RecursiveSound` (@ `ManagedDoom/src/Doom/World/WeaponBehavior.cs`) -> **O(2^N) [Recursive]**
- `Run` (@ `ManagedDoom/src/Silk/SilkDoom.Run.cs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Finale` (@ `ManagedDoom/src/Doom/Intermission/Finale.cs`) -> DB Complexity: **46**
- `Clear` (@ `ManagedDoom/src/Doom/Game/Player.cs`) -> DB Complexity: **40**
- `UpdateCast` (@ `ManagedDoom/src/Doom/Intermission/Finale.cs`) -> DB Complexity: **38**
- `Reborn` (@ `ManagedDoom/src/Doom/Game/Player.cs`) -> DB Complexity: **35**
- `UpdateFace` (@ `ManagedDoom/src/Doom/World/StatusBar.cs`) -> DB Complexity: **34**
- `World` (@ `ManagedDoom/src/Doom/World/World.cs`) -> DB Complexity: **33**
- `Config` (@ `ManagedDoom/src/Config.cs`) -> DB Complexity: **30**
- `CommandLineArgs` (@ `ManagedDoom/src/CommandLineArgs.cs`) -> DB Complexity: **29**
- `Config` (@ `ManagedDoom/src/Config.cs`) -> DB Complexity: **27**
  * *Intent:* // Default settings.
- `DoomMenu` (@ `ManagedDoom/src/Doom/Menu/DoomMenu.cs`) -> DB Complexity: **27**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ManagedDoom/src/Doom/World` | 60 | 14286.1 | 20.44% | 19.27% |
| `ManagedDoom/src/Silk` | 8 | 4324.68 | 40.39% | 38.55% |
| `ManagedDoom/src/Video` | 12 | 4020.54 | 22.89% | 40.19% |
| `ManagedDoomTest/src/CompatibilityTests` | 11 | 3590.88 | 44.94% | 61.59% |
| `ManagedDoom/src/Doom/Game` | 16 | 2642.5 | 17.66% | 28.22% |
| `ManagedDoom/src/UserInput` | 7 | 2470.84 | 13.78% | 42.97% |
| `ManagedDoom/src/Doom` | 3 | 2351.32 | 35.66% | 15.21% |
| `ManagedDoom/src/Doom/Intermission` | 9 | 2257.28 | 26.36% | 24.38% |
| `ManagedDoom/src/Doom/Info` | 16 | 2215.15 | 6.26% | 1.15% |
| `ManagedDoom/src/Doom/Menu` | 17 | 2004.42 | 21.66% | 55.1% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ManagedDoom/src/Audio/NullSound.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Math/Trig.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Menu/MenuItem.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/World/BoxEx.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/World/Intercept.cs` -> **99.9999%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ManagedDoom/src/Doom/Common/DoomDebug.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Common/DoomString.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Game/GameOptions.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Game/Player.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Info/DoomInfo.DeHackEdConst.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ManagedDoom/src/Doom/World/MonsterBehavior.cs` -> **36** Orphaned Functions | **0** Duplicates
- `ManagedDoomTest/src/UnitTests/FixedTest.cs` -> **22** Orphaned Functions | **0** Duplicates
- `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` -> **21** Orphaned Functions | **0** Duplicates
- `ManagedDoom/src/Doom/World/SectorAction.cs` -> **20** Orphaned Functions | **0** Duplicates
- `ManagedDoomTest/src/UnitTests/GeometryTest.cs` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ManagedDoom/src/Silk/SilkDoom.cs`** -> AI Confidence: **99.31%**
2. **`ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs`** -> AI Confidence: **99.29%**
3. **`ManagedDoom/src/Doom/Intermission/Finale.cs`** -> AI Confidence: **99.29%**
4. **`ManagedDoom/src/Doom/Opening/OpeningSequence.cs`** -> AI Confidence: **99.29%**
5. **`ManagedDoom/src/Doom/World/MapInteraction.cs`** -> AI Confidence: **99.29%**
6. **`ManagedDoom/src/Doom/World/PlayerBehavior.cs`** -> AI Confidence: **99.29%**
7. **`ManagedDoom/src/Doom/Doom.cs`** -> AI Confidence: **99.23%**
8. **`ManagedDoom/src/Silk/SilkVideo.cs`** -> AI Confidence: **99.18%**
9. **`ManagedDoom/src/Doom/Game/DoomGame.cs`** -> AI Confidence: **99.17%**
10. **`ManagedDoom/src/Doom/Info/DoomInfo.QuitMessages.cs`** -> AI Confidence: **99.17%**
11. **`ManagedDoom/src/Doom/Intermission/Intermission.cs`** -> AI Confidence: **99.17%**
12. **`ManagedDoom/src/Doom/World/AutoMap.cs`** -> AI Confidence: **99.17%**
13. **`ManagedDoom/src/Doom/World/CeilingMove.cs`** -> AI Confidence: **99.17%**
14. **`ManagedDoom/src/Doom/World/ItemPickup.cs`** -> AI Confidence: **99.17%**
15. **`ManagedDoom/src/Doom/World/StatusBar.cs`** -> AI Confidence: **99.17%**
16. **`ManagedDoom/src/Doom/World/VerticalDoor.cs`** -> AI Confidence: **99.17%**
17. **`ManagedDoom/src/Doom/DeHackEd.cs`** -> AI Confidence: **99.13%**
18. **`ManagedDoom/src/Silk/SilkMusic.cs`** -> AI Confidence: **99.13%**
19. **`ManagedDoom/src/Silk/SilkSound.cs`** -> AI Confidence: **99.13%**
20. **`ManagedDoom/src/Silk/SilkUserInput.cs`** -> AI Confidence: **99.13%**
21. **`ManagedDoom/src/Doom/Graphics/SpriteLookup.cs`** -> AI Confidence: **99.09%**
22. **`ManagedDoom/src/Doom/Graphics/TextureAnimation.cs`** -> AI Confidence: **99.09%**
23. **`ManagedDoom/src/Doom/Intermission/Animation.cs`** -> AI Confidence: **99.09%**
24. **`ManagedDoom/src/Doom/Map/Map.cs`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `ManagedDoomTest/src/UnitTests/NodeTest.cs` -> **100.0%** Exposure
- `ManagedDoomTest/src/UnitTests/SegTest.cs` -> **99.9997%** Exposure
- `ManagedDoomTest/src/UnitTests/LineDefTest.cs` -> **99.9899%** Exposure
- `ManagedDoomTest/src/UnitTests/SideDefTest.cs` -> **99.8505%** Exposure
- `ManagedDoomTest/src/UnitTests/SectorTest.cs` -> **98.1232%** Exposure
### Exploit Generation Surface
- `ManagedDoom/src/Audio/NullMusic.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Audio/NullSound.cs` -> **100.0%** Exposure
- `ManagedDoom/src/CommandLineArgs.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Config.cs` -> **100.0%** Exposure
- `ManagedDoom/src/ConfigUtilities.cs` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `ManagedDoom/src/Audio/NullSound.cs` -> **100.0%** Exposure
- `ManagedDoom/src/CommandLineArgs.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Config.cs` -> **100.0%** Exposure
- `ManagedDoom/src/ConfigUtilities.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Common/DoomDebug.cs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `461` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ManagedDoom/src/Silk/SilkMusic.cs` (CSHARP) -> Cumulative Risk: **842.42**
- **Archetype:** `file_cluster_8` (Distance: 10.739 IQR)
- **Magnitude:** 1000.32 | **LOC:** 646 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9962%)
- **Heaviest Functions:** `SendEvents` (Impact: 293.3), `ReadSingleEvent` (Impact: 159.3), `OnGetData` (Impact: 72.4)

### 2. `ManagedDoom/src/CommandLineArgs.cs` (CSHARP) -> Cumulative Risk: **821.8**
- **Archetype:** `file_cluster_8` (Distance: 11.183 IQR)
- **Magnitude:** 304.12 | **LOC:** 250 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `CommandLineArgs` (Impact: 80.7), `Check_warp` (Impact: 45.2), `GetInt` (Impact: 16.3)

### 3. `ManagedDoomTest/src/CompatibilityTests/IwadDemo.cs` (CSHARP) -> Cumulative Risk: **813.41**
- **Archetype:** `file_cluster_8` (Distance: 11.903 IQR)
- **Magnitude:** 732.8 | **LOC:** 591 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9989%)
- **Heaviest Functions:** `Doom1SharewareDemo1` (Impact: 33.1), `Doom1SharewareDemo2` (Impact: 33.1), `Doom1SharewareDemo3` (Impact: 33.1)

### 4. `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` (CSHARP) -> Cumulative Risk: **805.94**
- **Archetype:** `file_cluster_8` (Distance: 12.073 IQR)
- **Magnitude:** 910.58 | **LOC:** 645 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9992%)
- **Heaviest Functions:** `NightmareTest` (Impact: 32.8), `BarrelTest` (Impact: 32.8), `ZombiemanTest` (Impact: 32.8)

### 5. `ManagedDoom/src/Doom/Common/DoomDebug.cs` (CSHARP) -> Cumulative Risk: **799.85**
- **Archetype:** `file_cluster_8` (Distance: 10.858 IQR)
- **Magnitude:** 148.94 | **LOC:** 151 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetMobjHash` (Impact: 44.7), `GetSectorHash` (Impact: 24.9), `DumpMobjCsv` (Impact: 18.9)

### 6. `ManagedDoomTest/src/CompatibilityTests/PlayerWeapon.cs` (CSHARP) -> Cumulative Risk: **799.27**
- **Archetype:** `file_cluster_8` (Distance: 11.73 IQR)
- **Magnitude:** 390.94 | **LOC:** 283 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.999%)
- **Heaviest Functions:** `PunchTest` (Impact: 32.8), `ChainsawTest` (Impact: 32.8), `ShotgunTest` (Impact: 32.8)

### 7. `ManagedDoom/src/Doom/Doom.cs` (CSHARP) -> Cumulative Risk: **793.56**
- **Archetype:** `file_cluster_8` (Distance: 11.561 IQR)
- **Magnitude:** 1147.66 | **LOC:** 557 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9985%)
- **Heaviest Functions:** `Update` (Impact: 340.5), `CheckFunctionKey` (Impact: 256.4), `DoEvents` (Impact: 107.2)

### 8. `ManagedDoom/src/Doom/World/Thinkers.cs` (CSHARP) -> Cumulative Risk: **785.23**
- **Archetype:** `file_cluster_8` (Distance: 9.947 IQR)
- **Magnitude:** 200.28 | **LOC:** 143 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Run` (Impact: 71.0), `MoveNext` (Impact: 35.8), `UpdateFrameInterpolationInfo` (Impact: 20.4)

### 9. `ManagedDoom/src/Video/Renderer.cs` (CSHARP) -> Cumulative Risk: **783.91**
- **Archetype:** `file_cluster_8` (Distance: 10.28 IQR)
- **Magnitude:** 404.6 | **LOC:** 379 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `RenderGame` (Impact: 87.3), `GetPaletteNumber` (Impact: 83.3), `RenderDoom` (Impact: 50.0)

### 10. `ManagedDoom/src/Doom/World/AutoMap.cs` (CSHARP) -> Cumulative Risk: **781.44**
- **Archetype:** `file_cluster_8` (Distance: 11.775 IQR)
- **Magnitude:** 648.44 | **LOC:** 339 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `DoEvent` (Impact: 350.9), `Update` (Impact: 88.3), `AutoMap` (Impact: 38.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ManagedDoom/src/Doom/World/MonsterBehavior.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.31 IQR)
- **Top Global Matches:** file_cluster_8: 11.31, file_cluster_7: 11.442, file_cluster_1: 11.549
- **Magnitude:** 2247.56 | **LOC:** 2015 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (12.8753%), Tech Debt (58.9448%)
**Top Internal Functions/Classes:**
  * `BossDeath` (Impact: 407.8 | O(N^6))
  * `NewChaseDir` (Impact: 265.6 | O(N^6))
  * `Look` (Impact: 167.7 | O(N^6) | DB: 3)
  * `Chase` (Impact: 167.2 | O(N^5))
  * `SpawnFly` (Impact: 138.5 | O(N^4) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 194`, `args: 83`, `func_start: 161`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 87`, `dead_code: 1`, `orphaned_logic: 36`
* *Architecture:* `api: 46`, `import: 1`
* *Defense:* `safety: 3`, `doc: 320`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/UserInput/DoomKeyEx.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.692 IQR)
- **Top Global Matches:** file_cluster_8: 7.692, file_cluster_7: 8.652, file_cluster_1: 8.848
- **Magnitude:** 2079.06 | **LOC:** 578 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (25.5083%), Tech Debt (12.3211%)
**Top Internal Functions/Classes:**
  * `ToString` (Impact: 774.7 | O(N^5))
  * `Parse` (Impact: 774.7 | O(N^5))
  * `GetChar` (Impact: 514.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 269`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkUserInput.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.489 IQR)
- **Top Global Matches:** file_cluster_8: 10.489, file_cluster_13: 10.941, file_cluster_1: 11.029
- **Magnitude:** 1722.22 | **LOC:** 581 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (84.1479%), Tech Debt (18.0664%)
**Top Internal Functions/Classes:**
  * `SilkToDoom` (Impact: 631.0 | O(N^4))
  * `DoomToSilk` (Impact: 611.6 | O(N^4))
  * `BuildTicCmd` (Impact: 208.6 | O(N^5) | DB: 9)
  * `IsPressed` (Impact: 37.5 | O(N^6))
  * `SilkUserInput` (Impact: 28.5 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 236`, `args: 14`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `orphaned_logic: 5`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Numerics, Silk.NET.Windowing, ManagedDoom.UserInput, System.Runtime.ExceptionServices, Silk.NET.Input
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Intermission/Intermission.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.946 IQR)
- **Top Global Matches:** file_cluster_8: 11.946, file_cluster_7: 12.044, file_cluster_1: 12.116
- **Magnitude:** 1335.4 | **LOC:** 859 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (19.1651%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UpdateNetGameStats` (Impact: 359.6 | O(N^6) | DB: 11)
  * `UpdateDeathmatchStats` (Impact: 194.9 | O(N^6) | DB: 5)
  * `UpdateSinglePlayerStats` (Impact: 194.8 | O(N^6) | DB: 7)
  * `Update` (Impact: 136.1 | O(N^6) | DB: 1)
    * *Intent:* //////////////////////////////////////////////////////////// // Update /////////////////////////////...
  * `CheckForAccelerate` (Impact: 64.8 | O(N^6) | DB: 2)
    * *Intent:* //////////////////////////////////////////////////////////// // Check for button press /////////////...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 49`, `args: 46`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `doc: 160`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/DeHackEd.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.745 IQR)
- **Top Global Matches:** file_cluster_8: 9.745, file_cluster_7: 10.479, file_cluster_13: 10.561
- **Magnitude:** 1187.42 | **LOC:** 788 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.8606%), Tech Debt (8.6901%)
**Top Internal Functions/Classes:**
  * `ProcessBlock` (Impact: 198.4 | O(N^6))
  * `GetBlockType` (Impact: 155.8 | O(N^4))
  * `ProcessBexStringsBlock` (Impact: 79.3 | O(N^6) | DB: 4)
  * `ProcessBexParsBlock` (Impact: 79.0 | O(N^6) | DB: 2)
  * `ProcessLines` (Impact: 60.9 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 135`, `args: 45`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `state_mutation: 47`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 6`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Text, System.IO, System.Runtime.ExceptionServices, System, System.Linq
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Doom.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.561 IQR)
- **Top Global Matches:** file_cluster_8: 11.561, file_cluster_13: 11.962, file_cluster_7: 12.09
- **Magnitude:** 1147.66 | **LOC:** 557 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (86.1114%), Tech Debt (36.9367%)
**Top Internal Functions/Classes:**
  * `Update` (Impact: 340.5 | O(2^N) | DB: 12)
  * `CheckFunctionKey` (Impact: 256.4 | O(N^6) | DB: 5)
  * `DoEvents` (Impact: 107.2 | O(N^6) | DB: 2)
  * `CheckGameArgs` (Impact: 68.2 | O(N^4) | DB: 7)
  * `CheckMouseState` (Impact: 55.6 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 40`, `args: 29`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `state_mutation: 155`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, ManagedDoom.Video, ManagedDoom.UserInput, ManagedDoom.Audio, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Game/SaveAndLoad.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.556 IQR)
- **Top Global Matches:** file_cluster_8: 10.556, file_cluster_1: 10.813, file_cluster_7: 10.872
- **Magnitude:** 1099.28 | **LOC:** 1013 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (7.5616%), Tech Debt (52.2281%)
**Top Internal Functions/Classes:**
  * `ArchiveSpecials` (Impact: 188.4 | O(N^6))
  * `UnArchiveSpecials` (Impact: 155.7 | O(N^6) | DB: 7)
  * `ArchivePlayer` (Impact: 115.3 | O(N^6))
  * `UnArchiveThinkers` (Impact: 82.2 | O(N^6) | DB: 1)
  * `UnArchivePlayer` (Impact: 66.3 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 101`, `args: 32`, `func_start: 245`, `class_start: 5`
* *Risk/State:* `state_mutation: 49`, `duplicate_logic: 9`
* *Architecture:* `io: 1`, `api: 8`, `import: 2`
* *Defense:* `safety: 10`, `doc: 83`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.IO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/SectorAction.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.202 IQR)
- **Top Global Matches:** file_cluster_8: 11.202, file_cluster_7: 11.37, file_cluster_1: 11.486
- **Magnitude:** 1094.74 | **LOC:** 1774 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (11.4739%), Tech Debt (27.7283%)
**Top Internal Functions/Classes:**
  * `DoLocalDoor` (Impact: 140.5 | O(N^2) | DB: 1)
  * `MovePlane` (Impact: 138.2 | O(N^2))
  * `DoFloor` (Impact: 128.3 | O(N^2) | DB: 6)
  * `DoPlatform` (Impact: 53.4 | O(N^1) | DB: 2)
  * `DoCeiling` (Impact: 43.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 190`, `args: 34`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `state_mutation: 127`, `orphaned_logic: 20`
* *Architecture:* `api: 27`, `import: 1`
* *Defense:* `safety: 1`, `doc: 286`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkMusic.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.739 IQR)
- **Top Global Matches:** file_cluster_8: 10.739, file_cluster_13: 11.215, file_cluster_7: 11.293
- **Magnitude:** 1000.32 | **LOC:** 646 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (43.8929%), Tech Debt (42.4484%)
**Top Internal Functions/Classes:**
  * `SendEvents` (Impact: 293.3 | O(N^6))
  * `ReadSingleEvent` (Impact: 159.3 | O(N^6) | DB: 1)
  * `OnGetData` (Impact: 72.4 | O(N^6) | DB: 5)
  * `ReadSingleEventGroup` (Impact: 64.5 | O(N^6) | DB: 2)
  * `ProcessMidiEvents` (Impact: 40.3 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 65`, `args: 23`, `func_start: 55`, `class_start: 7`
* *Risk/State:* `state_mutation: 94`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MeltySynth, System.IO, DrippyAL, System.Runtime.ExceptionServices, ManagedDoom.Audio, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ItemPickup.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.18 IQR)
- **Top Global Matches:** file_cluster_8: 10.18, file_cluster_7: 10.537, file_cluster_1: 10.657
- **Magnitude:** 936.24 | **LOC:** 762 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (23.3363%), Tech Debt (9.2897%)
**Top Internal Functions/Classes:**
  * `TouchSpecialThing` (Impact: 809.1 | O(N^6) | DB: 15)
  * `GivePower` (Impact: 32.5 | O(N^4))
  * `GiveHealth` (Impact: 13.8 | O(N^4))
  * `GiveArmor` (Impact: 9.4 | O(N^4))
  * `GiveCard` (Impact: 9.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 57`, `args: 6`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Math/Geometry.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.477 IQR)
- **Top Global Matches:** file_cluster_8: 10.477, file_cluster_7: 10.778, file_cluster_1: 11.037
- **Magnitude:** 931.3 | **LOC:** 626 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (13.9386%), Tech Debt (54.9%)
**Top Internal Functions/Classes:**
  * `PointToAngle` (Impact: 129.3 | O(N^6) | DB: 3)
    * *Intent:* /// <summary> /// Calculate the angle of the line passing through the two points. /// </summary>
  * `BoxOnLineSide` (Impact: 117.7 | O(N^6) | DB: 8)
    * *Intent:* /// <summary> /// Calculate on which side of the line the box is. /// </summary> /// <returns> /// 0...
  * `PointOnSegSide` (Impact: 99.2 | O(N^5))
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnDivLineSide` (Impact: 98.8 | O(N^5))
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnSide` (Impact: 92.8 | O(N^5))
    * *Intent:* /// <summary> /// Calculate on which side of the node the point is. /// </summary> /// <returns> ///...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 108`, `args: 12`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 52`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 54`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Opening/OpeningSequence.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.311 IQR)
- **Top Global Matches:** file_cluster_8: 11.311, file_cluster_7: 11.836, file_cluster_13: 11.895
- **Magnitude:** 916.9 | **LOC:** 263 | **CtrlFlow:** 86.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (93.9364%), Tech Debt (11.6726%)
**Top Internal Functions/Classes:**
  * `Update` (Impact: 777.3 | O(2^N) | DB: 17)
  * `StartTitleScreen` (Impact: 15.7 | O(N^4) | DB: 4)
  * `OpeningSequence` (Impact: 9.6 | O(N^4) | DB: 6)
  * `StartDemo` (Impact: 5.2 | O(N^3) | DB: 3)
  * `Reset` (Impact: 4.6 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 9`, `args: 8`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `orphaned_logic: 1`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.073 IQR)
- **Top Global Matches:** file_cluster_8: 12.073, file_cluster_17: 12.17, file_cluster_0: 12.26
- **Magnitude:** 910.58 | **LOC:** 645 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (56.7762%), Tech Debt (80.1565%)
**Top Internal Functions/Classes:**
  * `NightmareTest` (Impact: 32.8 | O(N^6) | DB: 3)
  * `BarrelTest` (Impact: 32.8 | O(N^6) | DB: 3)
  * `ZombiemanTest` (Impact: 32.8 | O(N^6) | DB: 3)
  * `ZombiemanTest2` (Impact: 32.8 | O(N^6) | DB: 3)
  * `ShotgunguyTest` (Impact: 32.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 175`, `args: 42`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `state_mutation: 189`, `orphaned_logic: 21`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, Microsoft.VisualStudio.TestTools.UnitTesting, System.Linq, ManagedDoom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/MapInteraction.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.066 IQR)
- **Top Global Matches:** file_cluster_8: 10.066, file_cluster_7: 10.309, file_cluster_1: 10.557
- **Magnitude:** 881.42 | **LOC:** 1081 | **CtrlFlow:** 93.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.5734%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UseTraverse` (Impact: 844.6 | O(N^1) | DB: 4)
  * `MapInteraction` (Impact: 2.3 | O(N^1) | DB: 1)
  * `InitUse` (Impact: 2.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 24`, `args: 7`, `func_start: 144`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 134`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Info/DoomInfo.MobjInfos.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.24 IQR)
- **Top Global Matches:** file_cluster_8: 5.24, file_cluster_7: 6.827, file_cluster_1: 6.896
- **Magnitude:** 878.19 | **LOC:** 3591 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 137`, `func_start: 264`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/PlayerBehavior.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.689 IQR)
- **Top Global Matches:** file_cluster_8: 10.689, file_cluster_7: 10.813, file_cluster_1: 10.865
- **Magnitude:** 844.62 | **LOC:** 660 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.6722%), Tech Debt (14.339%)
**Top Internal Functions/Classes:**
  * `PlayerThink` (Impact: 275.1 | O(N^6) | DB: 3)
    * *Intent:* //////////////////////////////////////////////////////////// // Player movement ////////////////////...
  * `PlayerInSpecialSector` (Impact: 183.7 | O(N^6))
    * *Intent:* /// <summary> /// Called every tic frame that the player origin is in a special sector. /// </summar...
  * `DeathThink` (Impact: 96.7 | O(N^6) | DB: 1)
    * *Intent:* /// <summary> /// Fall on your face when dying. /// Decrease POV height to floor height. /// </summa...
  * `CalcHeight` (Impact: 89.5 | O(N^6))
    * *Intent:* /// <summary> /// Calculate the walking / running height adjustment. /// </summary>
  * `SetPlayerSprite` (Impact: 65.0 | O(N^6) | DB: 1)
    * *Intent:* //////////////////////////////////////////////////////////// // Player's weapon sprites ////////////...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 20`, `args: 14`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `orphaned_logic: 3`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `doc: 129`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkSound.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.793 IQR)
- **Top Global Matches:** file_cluster_8: 10.793, file_cluster_13: 11.294, file_cluster_7: 11.376
- **Magnitude:** 842.2 | **LOC:** 586 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (37.7061%), Tech Debt (51.2752%)
**Top Internal Functions/Classes:**
  * `Dispose` (Impact: 113.8 | O(2^N) | DB: 3)
  * `Update` (Impact: 94.5 | O(N^6) | DB: 3)
  * `StartSound` (Impact: 77.2 | O(N^5) | DB: 4)
  * `SilkSound` (Impact: 66.0 | O(N^6) | DB: 12)
  * `ContainsDmxPadding` (Impact: 61.5 | O(N^6))
    * *Intent:* // Check if the data contains pad bytes. // If the first and last 16 samples are the same, // the da...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 74`, `args: 19`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `duplicate_logic: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Numerics, DrippyAL, ManagedDoom.Audio, System.Runtime.ExceptionServices, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ThingMovement.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.749 IQR)
- **Top Global Matches:** file_cluster_8: 10.749, file_cluster_7: 10.937, file_cluster_1: 11.049
- **Magnitude:** 816.3 | **LOC:** 1179 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (12.7899%), Tech Debt (18.1023%)
**Top Internal Functions/Classes:**
  * `ZMovement` (Impact: 256.0 | O(N^6) | DB: 22)
  * `XYMovement` (Impact: 226.3 | O(N^6) | DB: 5)
  * `CheckPosition` (Impact: 59.9 | O(N^6) | DB: 8)
  * `TryMove` (Impact: 58.6 | O(N^6) | DB: 1)
    * *Intent:* // Missiles can hit other things.
  * `UnsetThingPosition` (Impact: 48.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 84`, `args: 17`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 77`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 92`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Video/DrawScreen.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.383 IQR)
- **Top Global Matches:** file_cluster_8: 10.383, file_cluster_1: 10.789, file_cluster_7: 10.956
- **Magnitude:** 814.36 | **LOC:** 535 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (33.3915%), Tech Debt (72.3963%)
**Top Internal Functions/Classes:**
  * `DrawLine` (Impact: 166.4 | O(N^6) | DB: 15)
  * `Bresenham` (Impact: 114.4 | O(N^6))
  * `DrawText` (Impact: 62.1 | O(N^5) | DB: 1)
  * `DrawText` (Impact: 62.1 | O(N^5) | DB: 1)
  * `MeasureText` (Impact: 48.5 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 102`, `args: 23`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 80`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Video/IntermissionRenderer.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.536 IQR)
- **Top Global Matches:** file_cluster_8: 9.536, file_cluster_1: 10.17, file_cluster_7: 10.22
- **Magnitude:** 739.18 | **LOC:** 720 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (15.9525%), Tech Debt (38.2738%)
**Top Internal Functions/Classes:**
  * `Render` (Impact: 95.3 | O(N^6))
  * `DrawDeathmatchStats` (Impact: 75.2 | O(N^6) | DB: 2)
  * `DrawNumber` (Impact: 73.0 | O(N^6) | DB: 3)
  * `DrawNetGameStats` (Impact: 66.8 | O(N^6))
  * `DrawShowNextLoc` (Impact: 56.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 57`, `args: 21`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoomTest/src/CompatibilityTests/IwadDemo.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_17: 12.076, file_cluster_0: 12.168
- **Magnitude:** 732.8 | **LOC:** 591 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (53.426%), Tech Debt (65.4133%)
**Top Internal Functions/Classes:**
  * `Doom1SharewareDemo1` (Impact: 33.1 | O(N^6) | DB: 5)
  * `Doom1SharewareDemo2` (Impact: 33.1 | O(N^6) | DB: 5)
  * `Doom1SharewareDemo3` (Impact: 33.1 | O(N^6) | DB: 5)
  * `Doom1Demo1` (Impact: 33.1 | O(N^6) | DB: 5)
  * `Doom1Demo2` (Impact: 33.1 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 167`, `args: 32`, `func_start: 112`, `class_start: 1`
* *Risk/State:* `state_mutation: 176`, `orphaned_logic: 16`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, Microsoft.VisualStudio.TestTools.UnitTesting, System.Linq, ManagedDoom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Game/DoomGame.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.802 IQR)
- **Top Global Matches:** file_cluster_8: 11.802, file_cluster_7: 11.901, file_cluster_1: 12.182
- **Magnitude:** 669.9 | **LOC:** 621 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (31.8287%), Tech Debt (19.7642%)
**Top Internal Functions/Classes:**
  * `Update` (Impact: 376.8 | O(2^N) | DB: 13)
    * *Intent:* /// <summary> /// Advance the game one frame. /// </summary>
  * `DoCompleted` (Impact: 93.0 | O(N^1) | DB: 5)
  * `DoEvent` (Impact: 18.5 | O(2^N))
  * `DoReborn` (Impact: 18.2 | O(N^1) | DB: 1)
  * `InitNew` (Impact: 17.8 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 44`, `args: 26`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 16`, `import: 2`
* *Defense:* `safety: 1`, `doc: 139`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.IO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/AutoMap.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.775 IQR)
- **Top Global Matches:** file_cluster_8: 11.775, file_cluster_13: 12.154, file_cluster_7: 12.236
- **Magnitude:** 648.44 | **LOC:** 339 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (71.5447%), Tech Debt (32.5864%)
**Top Internal Functions/Classes:**
  * `DoEvent` (Impact: 350.9 | O(N^6) | DB: 17)
  * `Update` (Impact: 88.3 | O(N^4) | DB: 9)
  * `AutoMap` (Impact: 38.5 | O(N^5) | DB: 23)
  * `ToggleCheat` (Impact: 10.4 | O(N^4) | DB: 1)
  * `Close` (Impact: 4.5 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 27`, `args: 34`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `orphaned_logic: 5`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Intermission/Finale.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.673 IQR)
- **Top Global Matches:** file_cluster_8: 12.673, file_cluster_7: 13.114, file_cluster_13: 13.153
- **Magnitude:** 636.1 | **LOC:** 567 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (76.6118%), Tech Debt (21.0781%)
**Top Internal Functions/Classes:**
  * `UpdateCast` (Impact: 136.8 | O(N^1) | DB: 38)
  * `Finale` (Impact: 92.3 | O(N^1) | DB: 46)
  * `Update` (Impact: 29.1 | O(N^1) | DB: 5)
  * `BunnyScroll` (Impact: 15.8 | O(N^1) | DB: 7)
  * `DoEvent` (Impact: 12.7 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 27`, `args: 35`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 312`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ThingAllocation.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.554 IQR)
- **Top Global Matches:** file_cluster_8: 11.554, file_cluster_7: 11.623, file_cluster_1: 11.699
- **Magnitude:** 631.84 | **LOC:** 727 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.7008%), Tech Debt (41.51%)
**Top Internal Functions/Classes:**
  * `SpawnMapThing` (Impact: 167.4 | O(N^5) | DB: 6)
    * *Intent:* /// <summary> /// Spawn a mobj at the mapthing. /// </summary>
  * `GetMissileSpeed` (Impact: 63.6 | O(N^6))
    * *Intent:* // Free block.
  * `RespawnSpecials` (Impact: 56.9 | O(N^5) | DB: 4)
    * *Intent:* /// <summary> /// Spawns a player at one of the random death match spots. /// Called at level load a...
  * `SpawnPlayer` (Impact: 50.1 | O(N^5))
  * `CheckSpot` (Impact: 38.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 71`, `args: 19`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `state_mutation: 62`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 1`, `doc: 199`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ManagedDoom/src/Doom/World/MobjFlags.cs` (CSHARP) | Magnitude: 29.44 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, state_mutation: 13, structural_boundaries: 3, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ManagedDoom/src/Silk/SilkDoom.cs` (CSHARP) | Magnitude: 286.9 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 67, func_start: 33, branch: 22
- `ManagedDoom/src/UserInput/KeyBinding.cs` (CSHARP) | Magnitude: 156.8 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 24, state_mutation: 12, args: 10
- `ManagedDoomTest/src/CompatibilityTests/FireOnce.cs` (CSHARP) | Magnitude: 42.08 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 17, state_mutation: 6, func_start: 5
- `ManagedDoom/src/Silk/SilkVideo.cs` (CSHARP) | Magnitude: 171.6 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 44, structural_boundaries: 27, func_start: 26
- `ManagedDoomTest/src/CompatibilityTests/Miscellaneous.cs` (CSHARP) | Magnitude: 44.54 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 15, state_mutation: 9, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ManagedDoom/src/Doom/Graphics/TextureAnimation.cs` (CSHARP) | Magnitude: 158.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 18, branch: 10, structural_boundaries: 9
- `ManagedDoom/src/Silk/SilkConfigUtilities.cs` (CSHARP) | Magnitude: 71.74 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 21, branch: 7, state_mutation: 6
- `ManagedDoom/src/Video/ThreeDRenderer.cs` (CSHARP) | Magnitude: 485.16 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 397, doc: 160, state_mutation: 84, encapsulation: 65
- `ManagedDoom/src/Doom/World/PathTraverseFlags.cs` (CSHARP) | Magnitude: 19.24 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, state_mutation: 3, class_start: 1
- `ManagedDoom/src/Doom/Map/ThingFlags.cs` (CSHARP) | Magnitude: 20.26 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 4, structural_boundaries: 3, class_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ManagedDoom/src/Doom/Math/Angle.cs` -> Churn: **85.53%** | Cog Load: 6.5145% | Debt: 98.2394%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ManagedDoom/src/Video/ThreeDRenderer.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 485.16
- `ManagedDoom/src/Video/Renderer.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 404.6
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 107.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ManagedDoom/src/Audio/ISound.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 100.0%)
- `ManagedDoom/src/CommandLineArgs.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 100.0%)
- `ManagedDoom/src/ConfigUtilities.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 99.9999%)
- `ManagedDoom/src/Doom/Common/DoomDebug.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 99.9999%)
- `ManagedDoom/src/Doom/Common/DoomRandom.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
