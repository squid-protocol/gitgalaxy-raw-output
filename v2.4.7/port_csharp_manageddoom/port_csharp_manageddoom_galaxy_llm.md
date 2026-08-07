# ARCHITECTURAL_BRIEF: port_csharp_manageddoom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/port_csharp_manageddoom` |
| **Timestamp** | `2026-08-07T03:29:46.984183+00:00` |
| **Scan Duration** | `0.99s` |
| **Git Branch** | `master` |
| **Git Commit** | `9365696eb44326a3aab72c4bab217f7db8a87c96` |
| **Git Remote** | `https://github.com/sinshu/managed-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 244 malicious artifacts.

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
| Tech Debt Exposure | 0.0 | 100.0 | 33.3 | 20.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.7 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.6 | 5.7 | 5.5 | 4.1 |
| Concurrency Exposure | 0.0 | 73.9 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 58.1 | 83.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 12.8 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 40.0 | 100.0 | 96.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.7 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 4.8 | 100.0 | 48.2 | 43.4 | 11.9 |
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
- `UseSpecialLine` (@ `ManagedDoom/src/Doom/World/MapInteraction.cs`) -> Impact: **370.9** | LOC: 458
- `CrossSpecialLine` (@ `ManagedDoom/src/Doom/World/MapInteraction.cs`) -> Impact: **358.6** | LOC: 452
- `ToString` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **265.2** | LOC: 210
- `Parse` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **265.2** | LOC: 210
- `SilkToDoom` (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **256.2** | LOC: 128
- `DoomToSilk` (@ `ManagedDoom/src/Silk/SilkUserInput.cs`) -> Impact: **247.9** | LOC: 108
- `TouchSpecialThing` (@ `ManagedDoom/src/Doom/World/ItemPickup.cs`) -> Impact: **246.2** | LOC: 421
- `GetChar` (@ `ManagedDoom/src/UserInput/DoomKeyEx.cs`) -> Impact: **175.8** | LOC: 130
- `UpdateCast` (@ `ManagedDoom/src/Doom/Intermission/Finale.cs`) -> Impact: **136.8** | LOC: 177

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `ManagedDoom/src/Doom/World` | 60 | 8800.3 | 20.54% | 22.31% |
| `ManagedDoom/src/Silk` | 8 | 1863.28 | 40.39% | 38.55% |
| `ManagedDoomTest/src/CompatibilityTests` | 11 | 1828.48 | 44.94% | 61.59% |
| `ManagedDoom/src/Video` | 12 | 1825.84 | 22.89% | 42.29% |
| `ManagedDoom/src/Doom/Game` | 16 | 1506.0 | 17.66% | 28.22% |
| `ManagedDoom/src/Doom/Intermission` | 9 | 1430.98 | 26.27% | 24.38% |
| `ManagedDoom/src/Doom` | 3 | 975.32 | 35.66% | 18.57% |
| `ManagedDoom/src/UserInput` | 7 | 917.04 | 13.78% | 42.97% |
| `ManagedDoom/src/Doom/Menu` | 17 | 889.62 | 21.66% | 55.1% |
| `ManagedDoom/src/Doom/Info` | 16 | 887.68 | 5.93% | 1.15% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `ManagedDoom/src/Audio/NullSound.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Math/Trig.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Menu/MenuItem.cs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ManagedDoom/src/Doom/Common/DoomDebug.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Common/DoomString.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Game/GameOptions.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Game/Player.cs` -> **100.0%** Exposure
- `ManagedDoom/src/Doom/Info/DoomInfo.DeHackEdConst.cs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ManagedDoom/src/Doom/World/MonsterBehavior.cs` -> **36** Orphaned Functions | **4** Duplicates
- `ManagedDoom/src/Doom/Math/Fixed.cs` -> **15** Orphaned Functions | **10** Duplicates
- `ManagedDoomTest/src/UnitTests/FixedTest.cs` -> **22** Orphaned Functions | **0** Duplicates
- `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` -> **21** Orphaned Functions | **0** Duplicates
- `ManagedDoom/src/Doom/World/SectorAction.cs` -> **20** Orphaned Functions | **0** Duplicates

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
10. **`ManagedDoom/src/Doom/Intermission/Intermission.cs`** -> AI Confidence: **99.17%**
11. **`ManagedDoom/src/Doom/World/AutoMap.cs`** -> AI Confidence: **99.17%**
12. **`ManagedDoom/src/Doom/World/CeilingMove.cs`** -> AI Confidence: **99.17%**
13. **`ManagedDoom/src/Doom/World/ItemPickup.cs`** -> AI Confidence: **99.17%**
14. **`ManagedDoom/src/Doom/World/StatusBar.cs`** -> AI Confidence: **99.17%**
15. **`ManagedDoom/src/Doom/World/VerticalDoor.cs`** -> AI Confidence: **99.17%**
16. **`ManagedDoom/src/Doom/DeHackEd.cs`** -> AI Confidence: **99.13%**
17. **`ManagedDoom/src/Silk/SilkMusic.cs`** -> AI Confidence: **99.13%**
18. **`ManagedDoom/src/Silk/SilkSound.cs`** -> AI Confidence: **99.13%**
19. **`ManagedDoom/src/Silk/SilkUserInput.cs`** -> AI Confidence: **99.13%**
20. **`ManagedDoom/src/Doom/Graphics/SpriteLookup.cs`** -> AI Confidence: **99.09%**
21. **`ManagedDoom/src/Doom/Graphics/TextureAnimation.cs`** -> AI Confidence: **99.09%**
22. **`ManagedDoom/src/Doom/Intermission/Animation.cs`** -> AI Confidence: **99.09%**
23. **`ManagedDoom/src/Doom/Map/Map.cs`** -> AI Confidence: **99.09%**
24. **`ManagedDoom/src/Doom/Menu/SaveMenu.cs`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `461` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ManagedDoom/src/CommandLineArgs.cs` (CSHARP) -> Cumulative Risk: **619.28**
- **Archetype:** `file_cluster_8` (Distance: 11.161 IQR)
- **Magnitude:** 166.82 | **LOC:** 250 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9865%), Documentation (97.486%), Tech Debt (93.9095%)
- **Heaviest Functions:** `CommandLineArgs` (Impact: 25.6), `Check_warp` (Impact: 9.6), `GetInt` (Impact: 5.9)

### 2. `ManagedDoom/src/Doom/Intermission/Animation.cs` (CSHARP) -> Cumulative Risk: **606.88**
- **Archetype:** `file_cluster_8` (Distance: 11.51 IQR)
- **Magnitude:** 120.08 | **LOC:** 136 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8968%), Safety Score (92.5265%)
- **Heaviest Functions:** `Update` (Impact: 33.4), `Reset` (Impact: 14.3), `Animation` (Impact: 9.3)

### 3. `ManagedDoom/src/Doom/World/StatusBar.cs` (CSHARP) -> Cumulative Risk: **579.48**
- **Archetype:** `file_cluster_8` (Distance: 11.679 IQR)
- **Magnitude:** 241.4 | **LOC:** 302 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.7312%), Documentation (91.8373%)
- **Heaviest Functions:** `UpdateFace` (Impact: 70.2), `CalcPainOffset` (Impact: 6.8), `StatusBar` (Impact: 3.0)

### 4. `ManagedDoom/src/Silk/SilkMusic.cs` (CSHARP) -> Cumulative Risk: **563.69**
- **Archetype:** `file_cluster_8` (Distance: 10.715 IQR)
- **Magnitude:** 409.92 | **LOC:** 646 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.2351%), Verification (80.0%), Concurrency (73.9202%)
- **Heaviest Functions:** `SendEvents` (Impact: 86.5), `ReadSingleEvent` (Impact: 49.4), `OnGetData` (Impact: 22.1)

### 5. `ManagedDoom/src/Doom/World/World.cs` (CSHARP) -> Cumulative Risk: **560.82**
- **Archetype:** `file_cluster_8` (Distance: 10.935 IQR)
- **Magnitude:** 240.1 | **LOC:** 398 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8685%), Documentation (94.6405%), Verification (80.0%)
- **Heaviest Functions:** `LoadThings` (Impact: 35.8), `Update` (Impact: 22.6), `DoEvent` (Impact: 22.1)

### 6. `ManagedDoom/src/Doom/Game/Player.cs` (CSHARP) -> Cumulative Risk: **556.44**
- **Archetype:** `file_cluster_8` (Distance: 11.795 IQR)
- **Magnitude:** 309.48 | **LOC:** 583 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.0209%), Documentation (91.7518%)
- **Heaviest Functions:** `GetInterpolatedAngle` (Impact: 12.1), `Reborn` (Impact: 9.3), `GetInterpolatedViewZ` (Impact: 7.3)

### 7. `ManagedDoom/src/Doom/Doom.cs` (CSHARP) -> Cumulative Risk: **554.3**
- **Archetype:** `file_cluster_8` (Distance: 11.54 IQR)
- **Magnitude:** 449.16 | **LOC:** 557 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9985%), Safety Score (86.3561%), Cognitive Load (86.1114%)
- **Heaviest Functions:** `CheckFunctionKey` (Impact: 77.6), `Update` (Impact: 52.5), `DoEvents` (Impact: 32.1)

### 8. `ManagedDoom/src/Doom/World/AutoMap.cs` (CSHARP) -> Cumulative Risk: **552.48**
- **Archetype:** `file_cluster_8` (Distance: 11.655 IQR)
- **Magnitude:** 317.44 | **LOC:** 339 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.7105%), Verification (80.0%)
- **Heaviest Functions:** `DoEvent` (Impact: 104.9), `Update` (Impact: 37.3), `AutoMap` (Impact: 14.5)

### 9. `ManagedDoom/src/Video/Renderer.cs` (CSHARP) -> Cumulative Risk: **551.41**
- **Archetype:** `file_cluster_8` (Distance: 10.199 IQR)
- **Magnitude:** 195.5 | **LOC:** 379 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5236%), Churn (85.53%), Verification (80.0%)
- **Heaviest Functions:** `GetPaletteNumber` (Impact: 29.4), `RenderGame` (Impact: 26.6), `Render` (Impact: 15.6)

### 10. `ManagedDoom/src/Doom/Intermission/Finale.cs` (CSHARP) -> Cumulative Risk: **536.27**
- **Archetype:** `file_cluster_8` (Distance: 12.588 IQR)
- **Magnitude:** 633.8 | **LOC:** 567 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4157%), Verification (80.0%)
- **Heaviest Functions:** `UpdateCast` (Impact: 136.8), `Finale` (Impact: 92.3), `Update` (Impact: 29.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ManagedDoom/src/Doom/World/MapInteraction.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.067 IQR)
- **Top Global Matches:** file_cluster_8: 10.067, file_cluster_7: 10.309, file_cluster_1: 10.554
- **Magnitude:** 1638.72 | **LOC:** 1081 | **CtrlFlow:** 93.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5734%), Tech Debt (12.5501%)
**Top Internal Functions/Classes:**
  * `UseTraverse` (Impact: 844.6)
  * `UseSpecialLine` (Impact: 370.9)
  * `CrossSpecialLine` (Impact: 358.6)
  * `ShootSpecialLine` (Impact: 24.8)
  * `UseLines` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 24`, `args: 7`, `func_start: 144`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `doc: 134`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/SectorAction.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.2 IQR)
- **Top Global Matches:** file_cluster_8: 11.2, file_cluster_7: 11.367, file_cluster_1: 11.483
- **Magnitude:** 960.14 | **LOC:** 1774 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.4739%), Tech Debt (27.7283%)
**Top Internal Functions/Classes:**
  * `DoLocalDoor` (Impact: 96.3)
  * `MovePlane` (Impact: 94.6)
  * `DoFloor` (Impact: 88.4)
  * `DoPlatform` (Impact: 53.4)
  * `DoCeiling` (Impact: 43.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 190`, `args: 33`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `state_mutation: 127`, `orphaned_logic: 20`
* *Architecture:* `api: 27`, `import: 1`
* *Defense:* `safety: 1`, `doc: 286`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/MonsterBehavior.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.243 IQR)
- **Top Global Matches:** file_cluster_8: 11.243, file_cluster_7: 11.376, file_cluster_1: 11.484
- **Magnitude:** 912.36 | **LOC:** 2015 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0169%), Tech Debt (76.0714%)
**Top Internal Functions/Classes:**
  * `BossDeath` (Impact: 122.7)
  * `NewChaseDir` (Impact: 81.1)
  * `Chase` (Impact: 59.9)
  * `SpawnFly` (Impact: 58.0)
  * `Look` (Impact: 50.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 194`, `args: 55`, `func_start: 161`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 87`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 36`
* *Architecture:* `api: 46`, `import: 1`
* *Defense:* `safety: 3`, `doc: 320`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkUserInput.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.475 IQR)
- **Top Global Matches:** file_cluster_8: 10.475, file_cluster_13: 10.928, file_cluster_1: 11.016
- **Magnitude:** 749.82 | **LOC:** 581 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.1479%), Tech Debt (18.0664%)
**Top Internal Functions/Classes:**
  * `SilkToDoom` (Impact: 256.2)
  * `DoomToSilk` (Impact: 247.9)
  * `BuildTicCmd` (Impact: 74.5)
  * `IsPressed` (Impact: 11.5)
  * `SilkUserInput` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 236`, `args: 12`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 96`, `orphaned_logic: 5`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Numerics, Silk.NET.Input, System.Runtime.ExceptionServices, Silk.NET.Windowing, ManagedDoom.UserInput
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/UserInput/DoomKeyEx.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.692 IQR)
- **Top Global Matches:** file_cluster_8: 7.692, file_cluster_7: 8.652, file_cluster_1: 8.848
- **Magnitude:** 721.36 | **LOC:** 578 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.5083%), Tech Debt (12.3211%)
**Top Internal Functions/Classes:**
  * `ToString` (Impact: 265.2)
  * `Parse` (Impact: 265.2)
  * `GetChar` (Impact: 175.8)
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

### `ManagedDoom/src/Doom/Intermission/Finale.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.588 IQR)
- **Top Global Matches:** file_cluster_8: 12.588, file_cluster_7: 13.032, file_cluster_13: 13.072
- **Magnitude:** 633.8 | **LOC:** 567 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7968%), Tech Debt (21.0781%)
**Top Internal Functions/Classes:**
  * `UpdateCast` (Impact: 136.8)
  * `Finale` (Impact: 92.3)
  * `Update` (Impact: 29.1)
  * `BunnyScroll` (Impact: 15.8)
  * `DoEvent` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 27`, `args: 18`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 312`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Intermission/Intermission.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.897 IQR)
- **Top Global Matches:** file_cluster_8: 11.897, file_cluster_7: 11.995, file_cluster_1: 12.067
- **Magnitude:** 541.8 | **LOC:** 859 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.1651%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UpdateNetGameStats` (Impact: 109.6)
  * `UpdateSinglePlayerStats` (Impact: 59.9)
  * `UpdateDeathmatchStats` (Impact: 59.9)
  * `Update` (Impact: 41.1)
    * *Intent:* //////////////////////////////////////////////////////////// // Update /////////////////////////////...
  * `CheckForAccelerate` (Impact: 19.8)
    * *Intent:* //////////////////////////////////////////////////////////// // Check for button press /////////////...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 49`, `args: 32`, `func_start: 71`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `doc: 160`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/DeHackEd.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.69 IQR)
- **Top Global Matches:** file_cluster_8: 9.69, file_cluster_7: 10.427, file_cluster_13: 10.506
- **Magnitude:** 509.92 | **LOC:** 788 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8606%), Tech Debt (18.778%)
**Top Internal Functions/Classes:**
  * `GetBlockType` (Impact: 64.0)
  * `ProcessBlock` (Impact: 58.5)
  * `ProcessBexStringsBlock` (Impact: 24.1)
  * `ProcessBexParsBlock` (Impact: 23.9)
  * `ProcessLines` (Impact: 21.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 135`, `args: 35`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `state_mutation: 47`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 2`, `import: 6`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Text, System, System.IO, System.Runtime.ExceptionServices, System.Linq
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Doom.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.54 IQR)
- **Top Global Matches:** file_cluster_8: 11.54, file_cluster_13: 11.941, file_cluster_7: 12.07
- **Magnitude:** 449.16 | **LOC:** 557 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.1114%), Tech Debt (36.9367%)
**Top Internal Functions/Classes:**
  * `CheckFunctionKey` (Impact: 77.6)
  * `Update` (Impact: 52.5)
  * `DoEvents` (Impact: 32.1)
  * `CheckGameArgs` (Impact: 29.2)
  * `CheckMouseState` (Impact: 19.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 40`, `args: 25`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `state_mutation: 155`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System, ManagedDoom.UserInput, ManagedDoom.Video, ManagedDoom.Audio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoomTest/src/CompatibilityTests/Monsters.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.073 IQR)
- **Top Global Matches:** file_cluster_8: 12.073, file_cluster_17: 12.17, file_cluster_0: 12.26
- **Magnitude:** 440.18 | **LOC:** 645 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.7762%), Tech Debt (80.1565%)
**Top Internal Functions/Classes:**
  * `NightmareTest` (Impact: 10.4)
  * `BarrelTest` (Impact: 10.4)
  * `ZombiemanTest` (Impact: 10.4)
  * `ZombiemanTest2` (Impact: 10.4)
  * `ShotgunguyTest` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 175`, `args: 42`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `state_mutation: 189`, `orphaned_logic: 21`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Linq, Microsoft.VisualStudio.TestTools.UnitTesting, ManagedDoom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Game/SaveAndLoad.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.552 IQR)
- **Top Global Matches:** file_cluster_8: 10.552, file_cluster_1: 10.81, file_cluster_7: 10.868
- **Magnitude:** 411.78 | **LOC:** 1013 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5616%), Tech Debt (52.2281%)
**Top Internal Functions/Classes:**
  * `ArchiveSpecials` (Impact: 59.8)
  * `UnArchiveSpecials` (Impact: 49.5)
  * `ArchivePlayer` (Impact: 35.4)
  * `UnArchiveThinkers` (Impact: 26.3)
  * `UnArchivePlayer` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 101`, `args: 31`, `func_start: 245`, `class_start: 5`
* *Risk/State:* `state_mutation: 49`, `duplicate_logic: 9`
* *Architecture:* `io: 1`, `api: 8`, `import: 2`
* *Defense:* `safety: 10`, `doc: 83`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.IO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Game/DoomGame.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.786 IQR)
- **Top Global Matches:** file_cluster_8: 11.786, file_cluster_7: 11.885, file_cluster_1: 12.166
- **Magnitude:** 411.0 | **LOC:** 621 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8287%), Tech Debt (19.7642%)
**Top Internal Functions/Classes:**
  * `Update` (Impact: 130.8)
    * *Intent:* /// <summary> /// Advance the game one frame. /// </summary>
  * `DoCompleted` (Impact: 93.0)
  * `DoReborn` (Impact: 18.2)
  * `InitNew` (Impact: 17.8)
  * `DoEvent` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 44`, `args: 23`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 16`, `import: 2`
* *Defense:* `safety: 1`, `doc: 139`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.IO
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Silk/SilkMusic.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.715 IQR)
- **Top Global Matches:** file_cluster_8: 10.715, file_cluster_13: 11.192, file_cluster_7: 11.27
- **Magnitude:** 409.92 | **LOC:** 646 | **CtrlFlow:** 59.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8929%), Tech Debt (42.4484%)
**Top Internal Functions/Classes:**
  * `SendEvents` (Impact: 86.5)
  * `ReadSingleEvent` (Impact: 49.4)
  * `OnGetData` (Impact: 22.1)
  * `ReadSingleEventGroup` (Impact: 19.4)
  * `ReadData` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 65`, `args: 19`, `func_start: 55`, `class_start: 7`
* *Risk/State:* `state_mutation: 94`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 20`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.IO, System.Runtime.ExceptionServices, DrippyAL, MeltySynth, ManagedDoom.Audio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ThingMovement.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.724 IQR)
- **Top Global Matches:** file_cluster_8: 10.724, file_cluster_7: 10.914, file_cluster_1: 11.023
- **Magnitude:** 396.7 | **LOC:** 1179 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.6748%), Tech Debt (34.0655%)
**Top Internal Functions/Classes:**
  * `ZMovement` (Impact: 80.4)
  * `XYMovement` (Impact: 69.8)
  * `SlideTraverse` (Impact: 40.9)
  * `CheckPosition` (Impact: 19.9)
  * `TryMove` (Impact: 18.6)
    * *Intent:* // Missiles can hit other things.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 84`, `args: 13`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 77`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 92`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoomTest/src/CompatibilityTests/IwadDemo.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_17: 12.076, file_cluster_0: 12.168
- **Magnitude:** 374.4 | **LOC:** 591 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.426%), Tech Debt (65.4133%)
**Top Internal Functions/Classes:**
  * `Doom1SharewareDemo1` (Impact: 10.7)
  * `Doom1SharewareDemo2` (Impact: 10.7)
  * `Doom1SharewareDemo3` (Impact: 10.7)
  * `Doom1Demo1` (Impact: 10.7)
  * `Doom1Demo2` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 167`, `args: 32`, `func_start: 112`, `class_start: 1`
* *Risk/State:* `state_mutation: 176`, `orphaned_logic: 16`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Linq, Microsoft.VisualStudio.TestTools.UnitTesting, ManagedDoom
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Math/Geometry.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.477 IQR)
- **Top Global Matches:** file_cluster_8: 10.477, file_cluster_7: 10.778, file_cluster_1: 11.037
- **Magnitude:** 369.4 | **LOC:** 626 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9386%), Tech Debt (54.9%)
**Top Internal Functions/Classes:**
  * `PointToAngle` (Impact: 39.8)
    * *Intent:* /// <summary> /// Calculate the angle of the line passing through the two points. /// </summary>
  * `BoxOnLineSide` (Impact: 35.4)
    * *Intent:* /// <summary> /// Calculate on which side of the line the box is. /// </summary> /// <returns> /// 0...
  * `PointOnSegSide` (Impact: 35.1)
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnDivLineSide` (Impact: 34.9)
    * *Intent:* /// <summary> /// Calculate on which side of the line the point is. /// </summary> /// <returns> ///...
  * `PointOnSide` (Impact: 32.8)
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

### `ManagedDoom/src/Silk/SilkSound.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.786 IQR)
- **Top Global Matches:** file_cluster_8: 10.786, file_cluster_13: 11.288, file_cluster_7: 11.37
- **Magnitude:** 361.7 | **LOC:** 586 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7061%), Tech Debt (51.2752%)
**Top Internal Functions/Classes:**
  * `Update` (Impact: 29.4)
  * `StartSound` (Impact: 28.0)
  * `SilkSound` (Impact: 21.1)
  * `ContainsDmxPadding` (Impact: 18.6)
    * *Intent:* // Check if the data contains pad bytes. // If the first and last 16 samples are the same, // the da...
  * `Dispose` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 74`, `args: 18`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `duplicate_logic: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Numerics, System, System.Runtime.ExceptionServices, DrippyAL, ManagedDoom.Audio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Video/DrawScreen.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.342 IQR)
- **Top Global Matches:** file_cluster_8: 10.342, file_cluster_1: 10.749, file_cluster_7: 10.917
- **Magnitude:** 351.26 | **LOC:** 535 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.3915%), Tech Debt (72.3963%)
**Top Internal Functions/Classes:**
  * `DrawLine` (Impact: 50.0)
  * `Bresenham` (Impact: 34.8)
  * `DrawText` (Impact: 21.8)
  * `DrawText` (Impact: 21.8)
  * `MeasureText` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 102`, `args: 17`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 80`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/ItemPickup.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.18 IQR)
- **Top Global Matches:** file_cluster_8: 10.18, file_cluster_7: 10.537, file_cluster_1: 10.657
- **Magnitude:** 334.94 | **LOC:** 762 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3363%), Tech Debt (9.2897%)
**Top Internal Functions/Classes:**
  * `TouchSpecialThing` (Impact: 246.2)
  * `GivePower` (Impact: 14.3)
  * `GiveHealth` (Impact: 6.0)
  * `GiveArmor` (Impact: 4.2)
  * `GiveCard` (Impact: 4.0)
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

### `ManagedDoom/src/Doom/World/AutoMap.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.655 IQR)
- **Top Global Matches:** file_cluster_8: 11.655, file_cluster_13: 12.038, file_cluster_7: 12.121
- **Magnitude:** 317.44 | **LOC:** 339 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.5447%), Tech Debt (32.5864%)
**Top Internal Functions/Classes:**
  * `DoEvent` (Impact: 104.9)
  * `Update` (Impact: 37.3)
  * `AutoMap` (Impact: 14.5)
  * `ToggleCheat` (Impact: 4.4)
  * `Close` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 27`, `args: 17`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `orphaned_logic: 5`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Game/Player.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.795 IQR)
- **Top Global Matches:** file_cluster_8: 11.795, file_cluster_15: 12.207, file_cluster_7: 12.317
- **Magnitude:** 309.48 | **LOC:** 583 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.6869%), Tech Debt (31.2489%)
**Top Internal Functions/Classes:**
  * `GetInterpolatedAngle` (Impact: 12.1)
  * `Reborn` (Impact: 9.3)
  * `GetInterpolatedViewZ` (Impact: 7.3)
  * `Clear` (Impact: 7.0)
  * `Player` (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 83`, `args: 77`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `orphaned_logic: 7`
* *Architecture:* `api: 51`, `import: 2`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Numerics, System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/WeaponBehavior.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.663 IQR)
- **Top Global Matches:** file_cluster_8: 9.663, file_cluster_1: 10.3, file_cluster_7: 10.302
- **Magnitude:** 308.2 | **LOC:** 698 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.2935%), Tech Debt (86.0348%)
**Top Internal Functions/Classes:**
  * `CheckAmmo` (Impact: 58.1)
  * `Lower` (Impact: 55.1)
  * `RecursiveSound` (Impact: 29.5)
  * `WeaponReady` (Impact: 14.7)
  * `BFGSpray` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 39`, `args: 27`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `orphaned_logic: 19`
* *Architecture:* `api: 26`, `import: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.295 IQR)
- **Top Global Matches:** file_cluster_8: 9.295, file_cluster_7: 9.902, file_cluster_0: 10.16
- **Magnitude:** 302.02 | **LOC:** 546 | **CtrlFlow:** 92.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.2003%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 258`, `import: 1`
* *Defense:* `safety: 12`, `immutability_locks: 256`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Doom/World/PlayerBehavior.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.645 IQR)
- **Top Global Matches:** file_cluster_8: 10.645, file_cluster_7: 10.769, file_cluster_1: 10.821
- **Magnitude:** 301.42 | **LOC:** 660 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6722%), Tech Debt (35.4398%)
**Top Internal Functions/Classes:**
  * `PlayerThink` (Impact: 85.0)
    * *Intent:* //////////////////////////////////////////////////////////// // Player movement ////////////////////...
  * `PlayerInSpecialSector` (Impact: 55.1)
    * *Intent:* /// <summary> /// Called every tic frame that the player origin is in a special sector. /// </summar...
  * `DeathThink` (Impact: 29.6)
    * *Intent:* /// <summary> /// Fall on your face when dying. /// Decrease POV height to floor height. /// </summa...
  * `CalcHeight` (Impact: 28.0)
    * *Intent:* /// <summary> /// Calculate the walking / running height adjustment. /// </summary>
  * `SetPlayerSprite` (Impact: 20.0)
    * *Intent:* //////////////////////////////////////////////////////////// // Player's weapon sprites ////////////...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 20`, `args: 11`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `doc: 129`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.082
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ManagedDoom/src/Video/IntermissionRenderer.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.53 IQR)
- **Top Global Matches:** file_cluster_8: 9.53, file_cluster_1: 10.164, file_cluster_7: 10.214
- **Magnitude:** 297.28 | **LOC:** 720 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.9525%), Tech Debt (38.2738%)
**Top Internal Functions/Classes:**
  * `Render` (Impact: 28.2)
  * `DrawDeathmatchStats` (Impact: 24.9)
  * `DrawNumber` (Impact: 22.7)
  * `DrawNetGameStats` (Impact: 22.1)
  * `DrawShowNextLoc` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 57`, `args: 20`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `state_mutation: 55`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `immutability_locks: 21`
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
- `ManagedDoom/src/Silk/SilkDoom.cs` (CSHARP) | Magnitude: 152.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 67, func_start: 33, branch: 22
- `ManagedDoom/src/UserInput/KeyBinding.cs` (CSHARP) | Magnitude: 51.1 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 24, state_mutation: 12, args: 10
- `ManagedDoomTest/src/CompatibilityTests/FireOnce.cs` (CSHARP) | Magnitude: 19.68 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 17, state_mutation: 6, func_start: 5
- `ManagedDoom/src/Silk/SilkVideo.cs` (CSHARP) | Magnitude: 94.4 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 44, structural_boundaries: 27, func_start: 26
- `ManagedDoomTest/src/CompatibilityTests/Miscellaneous.cs` (CSHARP) | Magnitude: 22.14 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 15, state_mutation: 9, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ManagedDoom/src/Doom/Graphics/TextureAnimation.cs` (CSHARP) | Magnitude: 44.22 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 18, branch: 10, structural_boundaries: 9
- `ManagedDoom/src/Silk/SilkConfigUtilities.cs` (CSHARP) | Magnitude: 35.24 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 21, branch: 7, state_mutation: 6
- `ManagedDoom/src/Video/ThreeDRenderer.cs` (CSHARP) | Magnitude: 261.36 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 397, doc: 160, state_mutation: 84, encapsulation: 65
- `ManagedDoom/src/Doom/World/PathTraverseFlags.cs` (CSHARP) | Magnitude: 19.24 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, state_mutation: 3, class_start: 1
- `ManagedDoom/src/Doom/Map/ThingFlags.cs` (CSHARP) | Magnitude: 20.26 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 4, structural_boundaries: 3, class_start: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ManagedDoom/src/Doom/Math/Angle.cs` -> Churn: **85.53%** | Cog Load: 6.5546% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ManagedDoom/src/Video/ThreeDRenderer.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 261.36
- `ManagedDoom/src/Video/Renderer.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 195.5
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Nobuaki Tanaka** (100.0% isolated ownership) | Magnitude: 91.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ManagedDoom/src/Doom/Info/DoomInfo.Strings.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Math/Angle.cs` -> **Severity: 408.2** (Blast Radius: 4.082 * Doc Risk: 100.0%)
- `ManagedDoom/src/Doom/Info/DoomInfo.DeHackEdConst.cs` -> **Severity: 408.198** (Blast Radius: 4.082 * Doc Risk: 99.9996%)
- `ManagedDoom/src/Audio/ISound.cs` -> **Severity: 408.159** (Blast Radius: 4.082 * Doc Risk: 99.99%)
- `ManagedDoom/src/Video/IVideo.cs` -> **Severity: 408.113** (Blast Radius: 4.082 * Doc Risk: 99.9786%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
