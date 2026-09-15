# ARCHITECTURAL_BRIEF: DOOM
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/id-Software/DOOM.git` |
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
| Total Artifacts | 165 |
| Analyzed Artifacts (Scanned) | 146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 29164 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3313 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1173 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.156 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 136 | 29066 | 93.2% |
| PLAINTEXT | 6 | 0 | 4.1% |
| MARKDOWN | 2 | 0 | 1.4% |
| MAKEFILE | 2 | 98 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z -0.33; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 48%, Large Core Modules 19%, Compute Cores Files 10%, Data / Markup / Trivial 9%, Interface Declarations Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 138 | 94.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 5.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4671 LOC), 1x Excluded (Embedded Array/Matrix Payload: 16392 commas in 2131 LOC)
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1341 LOC), 1x Excluded (Machine-Generated Source Code Signature: 83 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 222 LOC)
- `.b`: 1x Excluded (Unsupported Extension: '.b')
- `.book`: 1x Excluded (Unsupported Extension: '.book')
- `.gl`: 1x Excluded (Unsupported Extension: '.gl')
- `.sound`: 1x Excluded (Unsupported Extension: '.sound')
- `.sndserv`: 1x Excluded (Unsupported Extension: '.sndserv')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.4 | 28.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 48.9 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 27.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 30.7 | 10.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.6 | 11.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 63.7 | 11.8 | 9.3 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 65.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 45.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5708 | 79 | 151 | `linuxdoom-1.10/p_enemy.c` |
| cleanup | 21 | 12 | 0 | `linuxdoom-1.10/m_misc.c` |
| guards | 374 | 64 | 4 | `linuxdoom-1.10/am_map.c` |
| danger | 267 | 42 | 6 | `linuxdoom-1.10/d_main.c` |
| concurrency | 2 | 1 | 0 | `linuxdoom-1.10/i_system.c` |
| connectivity | 1621 | 125 | 25 | `linuxdoom-1.10/m_menu.c` |
| io | 60 | 17 | 1 | `linuxdoom-1.10/m_misc.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 3 | 0 | `linuxdoom-1.10/i_video.c` |
| time | 2 | 2 | 0 | `linuxdoom-1.10/i_system.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 3 | 3 | 0 | `linuxdoom-1.10/i_sound.c` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `linuxdoom-1.10/i_sound.c` |
| debt | 240 | 41 | 5 | `linuxdoom-1.10/d_main.c` |
| mutation | 9631 | 77 | 254 | `linuxdoom-1.10/g_game.c` |
| dead_code | 586 | 124 | 9 | `linuxdoom-1.10/p_enemy.c` |
| credential | 0 | 0 | 0 | - |
| threat | 48 | 16 | 1 | `linuxdoom-1.10/p_map.c` |
| ml_ai | 31 | 8 | 0 | `linuxdoom-1.10/i_video.c` |
| ui | 1 | 1 | 0 | `linuxdoom-1.10/i_video.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `linuxdoom-1.10/m_misc.c` (Hits: 9)
- `linuxdoom-1.10/w_wad.c` (Hits: 9)
- `sndserv/soundsrv.c` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomdef.h** (`linuxdoom-1.10/doomdef.h`) — 48 inbound connections
2. **doomstat.h** (`linuxdoom-1.10/doomstat.h`) — 35 inbound connections
3. **i_system.h** (`linuxdoom-1.10/i_system.h`) — 33 inbound connections
4. **z_zone.h** (`linuxdoom-1.10/z_zone.h`) — 27 inbound connections
5. **p_local.h** (`linuxdoom-1.10/p_local.h`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`linuxdoom-1.10/d_main.c`) — 30 outbound dependencies
2. **g_game.c** (`linuxdoom-1.10/g_game.c`) — 28 outbound dependencies
3. **m_menu.c** (`linuxdoom-1.10/m_menu.c`) — 23 outbound dependencies
4. **i_video.c** (`linuxdoom-1.10/i_video.c`) — 21 outbound dependencies
5. **i_sound.c** (`linuxdoom-1.10/i_sound.c`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `P_TouchSpecialThing` **(Compute Cores)** (@ `linuxdoom-1.10/p_inter.c`) -> Impact: **180.7** | LOC: 324
  * *Intent:* // // P_TouchSpecialThing //
- `M_Responder` **(Compute Cores)** (@ `linuxdoom-1.10/m_menu.c`) -> Impact: **164.1** | LOC: 368
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/r_segs.c`) -> Impact: **138.1** | LOC: 372
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `ST_Responder` **(Compute Cores)** (@ `linuxdoom-1.10/st_stuff.c`) -> Impact: **99.5** | LOC: 209
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `D_DoomMain` **(Compute Cores)** (@ `linuxdoom-1.10/d_main.c`) -> Impact: **96.8** | LOC: 376
  * *Intent:* // // D_DoomMain //
- `G_BuildTiccmd` **(Compute Cores)** (@ `linuxdoom-1.10/g_game.c`) -> Impact: **94.9** | LOC: 201
  * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo buffer. // If recording a demo, write it out //
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_inter.c`) -> Impact: **94.4** | LOC: 144
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...
- `EV_VerticalDoor` **(Compute Cores)** (@ `linuxdoom-1.10/p_doors.c`) -> Impact: **83.6** | LOC: 147
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `T_MovePlane` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_floor.c`) -> Impact: **81.9** | LOC: 156
  * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // // // Move a plane (floor or ceiling) and check for ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `linuxdoom-1.10` | 119 | 27398.18 | 28.04% | 22.69% |
| `sndserv` | 9 | 1000.0 | 21.54% | 19.47% |
| `sersrc` | 8 | 845.5 | 26.21% | 9.12% |
| `ipx` | 8 | 626.3 | 21.53% | 2.27% |
| `__monolith__` | 2 | 8.46 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `linuxdoom-1.10/p_tick.c` -> **99.9999%** Exposure
- `linuxdoom-1.10/i_system.c` -> **99.9897%** Exposure
- `linuxdoom-1.10/m_fixed.c` -> **99.8499%** Exposure
- `linuxdoom-1.10/i_sound.c` -> **99.8325%** Exposure
- `sndserv/linux.c` -> **99.8035%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ipx/IPXNET.C` -> **100.0%** Exposure
- `ipx/IPXSETUP.C` -> **100.0%** Exposure
- `linuxdoom-1.10/am_map.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_main.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_net.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `linuxdoom-1.10/p_enemy.c` -> **49** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/p_pspr.c` -> **24** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/i_sound.c` -> **21** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/g_game.c` -> **16** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/i_system.c` -> **12** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `645` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `linuxdoom-1.10/i_sound.c` (C) -> Cumulative Risk: **681.37**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.21)
- **Magnitude:** 495.98 | **LOC:** 986 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8325%)
- **Heaviest Functions:** `addsfx` (Many-Argument Workhorses, Impact: 50.6), `I_UpdateSound` (I/O & Config Routines, Impact: 20.8), `I_InitSound` (I/O & Config Routines, Impact: 17.4)

### 2. `linuxdoom-1.10/p_pspr.c` (C) -> Cumulative Risk: **668.9**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.18)
- **Magnitude:** 536.04 | **LOC:** 880 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.7514%)
- **Heaviest Functions:** `P_CheckAmmo` (Compute Cores, Impact: 52.1), `A_WeaponReady` (Compute Cores, Impact: 23.5), `P_SetPsprite` (Many-Argument Workhorses, Impact: 16.2)

### 3. `linuxdoom-1.10/p_enemy.c` (C) -> Cumulative Risk: **661.6**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.82)
- **Magnitude:** 1415.68 | **LOC:** 2009 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.3326%)
- **Heaviest Functions:** `A_BossDeath` (Compute Cores, Impact: 71.0), `P_NewChaseDir` (Compute Cores, Impact: 54.4), `A_Chase` (Compute Cores, Impact: 50.5)

### 4. `linuxdoom-1.10/m_misc.c` (C) -> Cumulative Risk: **644.89**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.33)
- **Magnitude:** 301.7 | **LOC:** 535 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.4349%)
- **Heaviest Functions:** `M_LoadDefaults` (I/O & Config Routines, Impact: 21.2), `M_DrawText` (Many-Argument Workhorses, Impact: 17.3), `WritePCXfile` (Many-Argument Workhorses, Impact: 15.1)

### 5. `linuxdoom-1.10/z_zone.c` (C) -> Cumulative Risk: **639.79**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.04)
- **Magnitude:** 324.22 | **LOC:** 468 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.593%)
- **Heaviest Functions:** `Z_Malloc` (Many-Argument Workhorses, Impact: 35.4), `Z_DumpHeap` (Compute Cores, Impact: 17.3), `Z_Free` (Compute Cores, Impact: 12.4)

### 6. `linuxdoom-1.10/r_draw.c` (C) -> Cumulative Risk: **639.51**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.60)
- **Magnitude:** 432.86 | **LOC:** 878 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.9871%)
- **Heaviest Functions:** `R_FillBackScreen` (I/O & Config Routines, Impact: 15.1), `R_DrawFuzzColumn` (I/O & Config Routines, Impact: 14.2), `R_DrawTranslatedColumn` (I/O & Config Routines, Impact: 10.2)

### 7. `linuxdoom-1.10/r_plane.c` (C) -> Cumulative Risk: **634.84**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.13)
- **Magnitude:** 346.88 | **LOC:** 454 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.0948%)
- **Heaviest Functions:** `R_MakeSpans` (Many-Argument Workhorses, Impact: 23.5), `R_MapPlane` (Many-Argument Workhorses, Impact: 22.9), `R_CheckPlane` (Many-Argument Workhorses, Impact: 19.0)

### 8. `linuxdoom-1.10/p_lights.c` (C) -> Cumulative Risk: **629.95**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.92)
- **Magnitude:** 256.56 | **LOC:** 358 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.0057%)
- **Heaviest Functions:** `EV_LightTurnOn` (Compute Cores, Impact: 14.0), `EV_TurnTagLightsOff` (Compute Cores, Impact: 9.9), `T_Glow` (Compute Cores, Impact: 9.7)

### 9. `linuxdoom-1.10/s_sound.c` (C) -> Cumulative Risk: **627.16**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.68)
- **Magnitude:** 551.92 | **LOC:** 880 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.5177%)
- **Heaviest Functions:** `S_StartSoundAtVolume` (Many-Argument Workhorses, Impact: 65.1), `S_StartSound` (Compute Cores, Impact: 32.9), `S_AdjustSoundParams` (Many-Argument Workhorses, Impact: 30.3)

### 10. `linuxdoom-1.10/w_wad.c` (C) -> Cumulative Risk: **626.73**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.16)
- **Magnitude:** 356.46 | **LOC:** 578 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5453%)
- **Heaviest Functions:** `W_AddFile` (Compute Cores, Impact: 19.9), `W_ReadLump` (Compute Cores, Impact: 14.0), `W_Profile` (I/O & Config Routines, Impact: 13.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `linuxdoom-1.10/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1516.4 | **LOC:** 1691 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.3767%), Tech Debt (24.4031%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Compute Cores)** (Impact: 94.9)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 78.0)
  * `G_Responder` **(Compute Cores)** (Impact: 54.2)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_Ticker` **(Compute Cores)** (Impact: 51.2)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_DoCompleted` **(Compute Cores)** (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 296 instances
* *State Mutation (weighted view):* 979
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 203`, `args: 49`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 387`, `dead_code: 10`, `unreferenced_by_name: 16`
* *Architecture:* `api: 53`, `import: 28`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` am_map.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, f_finale.h, g_game.h, hu_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1415.68 | **LOC:** 2009 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.4005%), Tech Debt (76.5493%)
**Top Internal Functions/Classes:**
  * `A_BossDeath` **(Compute Cores)** (Impact: 71.0)
    * *Intent:* // // A_BossDeath // Possibly trigger special effects // if on first boss level //
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 54.4)
  * `A_Chase` **(Compute Cores)** (Impact: 50.5)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_SpawnFly` **(Compute Cores)** (Impact: 35.3)
  * `A_Look` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* // // ACTION ROUTINES // // // A_Look // Stay in state until a player is sighted. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 219`, `args: 77`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 279`, `dead_code: 7`, `unreferenced_by_name: 49`
* *Architecture:* `api: 71`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1264.64 | **LOC:** 1851 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0022%), Tech Debt (22.7657%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(Compute Cores)** (Impact: 52.6)
  * `WI_updateDeathmatchStats` **(I/O & Config Routines)** (Impact: 34.0)
  * `WI_updateStats` **(I/O & Config Routines)** (Impact: 33.2)
  * `WI_loadData` **(I/O & Config Routines)** (Impact: 30.5)
  * `WI_drawOnLnode` **(Compute Cores)** (Impact: 23.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 117`, `args: 57`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 286`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 38`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` doomstat.h, g_game.h, i_system.h, m_random.h, m_swap.h, r_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1111.96 | **LOC:** 1350 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.3357%), Tech Debt (12.7541%)
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 72.6)
    * *Intent:* // // Handle events (user inputs) in automap mode //
  * `AM_clipMline` **(Compute Cores)** (Impact: 66.9)
    * *Intent:* // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algorithm but with a sligh...
  * `AM_drawFline` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* #undef DOOUTCODE // // Classic Bresenham w/ whatever optimizations needed for speed //
  * `AM_drawWalls` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* // // Determines visible lines, draws them. // This is LineDef based, not LineSeg based. //
  * `AM_drawLineCharacter` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 123`, `args: 53`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 257`, `dead_code: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 41`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` am_map.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_cheat.h, p_local.h, r_state.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1056.22 | **LOC:** 1894 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0231%), Tech Debt (27.0925%)
**Top Internal Functions/Classes:**
  * `M_Responder` **(Compute Cores)** (Impact: 164.1)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_WriteText` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* // // Write a string using the hu_font //
  * `M_Drawer` **(I/O & Config Routines)** (Impact: 13.3)
    * *Intent:* // // M_Drawer // Called after the view has been rendered, // but before it has been blitted. //
  * `M_SizeDisplay` **(Compute Cores)** (Impact: 9.6)
  * `M_SfxVol` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 282`, `args: 150`, `func_start: 54`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 188`, `dead_code: 3`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 105`, `import: 23`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ctype.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, fcntl.h, g_game.h, hu_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 931.9 | **LOC:** 919 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.2662%), Tech Debt (17.3288%)
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Compute Cores)** (Impact: 180.7)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_GiveAmmo` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* // // GET STUFF // // // P_GiveAmmo // Num is the number of clip loads, // not the individual count ...
  * `P_KillMobj` **(Compute Cores)** (Impact: 44.4)
    * *Intent:* // // KillMobj //
  * `P_GiveWeapon` **(Many-Argument Workhorses)** (Impact: 32.7)
    * *Intent:* // // P_GiveWeapon // The weapon name may have a MF_DROPPED flag ored in. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 469
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 133`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 157`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` am_map.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_random.h, p_inter.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 868.74 | **LOC:** 990 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.7813%), Tech Debt (12.7484%)
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 50.7)
    * *Intent:* // // R_DrawSprite //
  * `R_ProjectSprite` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 30.7)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawPSprite` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // // R_DrawPSprite //
  * `R_InstallSpriteLump` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 45`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 213`, `dead_code: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomdef.h, doomstat.h, i_system.h, m_swap.h, r_local.h, stdio.h, stdlib.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 856.72 | **LOC:** 989 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.3854%), Tech Debt (46.9333%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 68.6)
    * *Intent:* // // P_XYMovement // #define STOPSPEED 0x1000 #define FRICTION 0xe800
  * `P_ZMovement` **(Compute Cores)** (Impact: 44.8)
    * *Intent:* // // P_ZMovement //
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* // // P_SpawnMapThing // The fields of the mapthing should // already be in host byte order. //
  * `P_MobjThinker` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* // // P_MobjThinker //
  * `P_SpawnMobj` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* // // P_SpawnMobj //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 52`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 187`, `dead_code: 3`, `fragile_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` doomdef.h, doomstat.h, hu_stuff.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/i_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 856.48 | **LOC:** 1051 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.3557%), Tech Debt (22.2985%)
**Top Internal Functions/Classes:**
  * `I_InitGraphics` **(Compute Cores)** (Impact: 47.2)
  * `xlatekey` **(Compute Cores)** (Impact: 44.3)
    * *Intent:* // // Translates the key currently in X_event //
  * `I_FinishUpdate` **(Compute Cores)** (Impact: 33.5)
    * *Intent:* // // I_FinishUpdate //
  * `I_GetEvent` **(Compute Cores)** (Impact: 32.3)
  * `grabsharedmemory` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* // // This function is probably redundant, // if XShmDetach works properly. // ddt never detached th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 78`, `args: 45`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `dead_code: 3`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 18`, `import: 21`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Xlib.h, Xutil.h, XShm.h, keysym.h, d_main.h, doomdef.h, doomstat.h, errnos.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 852.14 | **LOC:** 1340 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.2338%), Tech Debt (39.0183%)
**Top Internal Functions/Classes:**
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 32.9)
    * *Intent:* // // PIT_CheckThing //
  * `PTR_ShootTraverse` **(Compute Cores)** (Impact: 32.8)
    * *Intent:* // // PTR_ShootTraverse //
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* // // P_TryMove // Attempt to move to a new position, // crossing special lines unless MF_TELEPORT i...
  * `PTR_AimTraverse` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // // PTR_AimTraverse // Sets linetaget and aimslope when a target is aimed at. //
  * `PIT_CheckLine` **(Compute Cores)** (Impact: 24.2)
    * *Intent:* // // MOVEMENT ITERATOR FUNCTIONS // // // PIT_CheckLine // Adjusts tmfloorz and tmceilingz as lines...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 153`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 212`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 22`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` doomdef.h, doomstat.h, i_system.h, m_bbox.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/st_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 846.64 | **LOC:** 1472 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0474%), Tech Debt (14.1538%)
**Top Internal Functions/Classes:**
  * `ST_Responder` **(Compute Cores)** (Impact: 99.5)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` **(I/O & Config Routines)** (Impact: 42.5)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` **(I/O & Config Routines)** (Impact: 15.7)
  * `ST_updateWidgets` **(I/O & Config Routines)** (Impact: 15.2)
  * `ST_drawWidgets` **(Compute Cores)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 181 instances
* *State Mutation (weighted view):* 568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 73`, `args: 33`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 206`, `dead_code: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 22`, `import: 20`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` am_map.h, doomdef.h, doomstat.h, dstrings.h, g_game.h, i_system.h, i_video.h, m_cheat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 774.68 | **LOC:** 747 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5373%), Tech Debt (29.6693%)
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 138.1)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 35.0)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` doomdef.h, doomstat.h, i_system.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 729.16 | **LOC:** 1172 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.7781%), Tech Debt (39.985%)
**Top Internal Functions/Classes:**
  * `D_DoomMain` **(Compute Cores)** (Impact: 96.8)
    * *Intent:* // // D_DoomMain //
  * `D_Display` **(Compute Cores)** (Impact: 50.6)
  * `IdentifyVersion` **(I/O & Config Routines)** (Impact: 23.8)
    * *Intent:* // // IdentifyVersion // Checks availability of IWAD files by name, // to determine whether register...
  * `D_DoAdvanceDemo` **(I/O & Config Routines)** (Impact: 22.2)
    * *Intent:* // // This cycles through the demo sequences. // FIXME - version dependend demo numbers? //
  * `FindResponseFile` **(I/O & Config Routines)** (Impact: 18.4)
    * *Intent:* // // Find a Response File //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 145 instances
* *Memory Alloc (weighted view):* 8
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 101`, `args: 32`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 160`, `dead_code: 4`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 25`, `import: 30`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` am_map.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, f_finale.h, f_wipe.h, fcntl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 729.04 | **LOC:** 709 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4466%), Tech Debt (12.4232%)
**Top Internal Functions/Classes:**
  * `P_SetupLevel` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* // // P_SetupLevel //
  * `P_LoadLineDefs` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // // P_LoadLineDefs // Also counts secret lines for intermissions. //
  * `P_LoadThings` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* // // P_LoadThings //
  * `P_GroupLines` **(I/O & Config Routines)** (Impact: 17.9)
    * *Intent:* // // P_GroupLines // Builds sector line lists and subsector sector numbers. // Finds block bounding...
  * `P_LoadSegs` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* // // P_LoadSegs //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 20`, `args: 14`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 214`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_bbox.h, m_swap.h, math.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 720.74 | **LOC:** 884 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2669%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `P_PathTraverse` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* // // P_PathTraverse // Traces a line from x1,y1 to x2,y2, // calling the traverser function for eac...
  * `P_UnsetThingPosition` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* // // THING POSITION SETTING // // // P_UnsetThingPosition // Unlinks a thing from block map and sec...
  * `P_PointOnDivlineSide` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* // // P_PointOnDivlineSide // Returns 0 or 1. //
  * `PIT_AddLineIntercepts` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* // // PIT_AddLineIntercepts. // Looks for lines in the given block // that intercept the given trace...
  * `P_BoxOnLineSide` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 70`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 153`, `dead_code: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` doomdef.h, m_bbox.h, p_local.h, r_state.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sndserv/soundsrv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 712.88 | **LOC:** 741 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4579%), Tech Debt (12.2113%)
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `addsfx` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `grabdata` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `mix` **(I/O & Config Routines)** (Impact: 33.9)
  * `outputushort` **(Compute Cores)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 25`, `args: 11`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 167`, `dead_code: 8`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 10`, `import: 13`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fcntl.h, malloc.h, math.h, sounds.h, soundsrv.h, stdio.h, stdlib.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 645.56 | **LOC:** 556 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.6784%), Tech Debt (12.7568%)
**Top Internal Functions/Classes:**
  * `T_MovePlane` **(Many-Argument Workhorses)** (Impact: 81.9)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_DoFloor` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `EV_BuildStairs` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 54`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 149`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` doomdef.h, doomstat.h, p_local.h, r_state.h, s_sound.h, sounds.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/d_net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 642.8 | **LOC:** 768 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5833%), Tech Debt (25.2579%)
**Top Internal Functions/Classes:**
  * `TryRunTics` **(I/O & Config Routines)** (Impact: 39.6)
  * `D_ArbitrateNetStart` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* // // D_ArbitrateNetStart //
  * `GetPackets` **(I/O & Config Routines)** (Impact: 21.9)
  * `HGetPacket` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* // // HGetPacket // Returns false if no packet is waiting //
  * `NetUpdate` **(I/O & Config Routines)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 72`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 149`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 17`, `import: 7`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomdef.h, doomstat.h, g_game.h, i_net.h, i_system.h, i_video.h, m_menu.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_data.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 634.34 | **LOC:** 850 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.1382%), Tech Debt (19.3757%)
**Top Internal Functions/Classes:**
  * `R_InitTextures` **(I/O & Config Routines)** (Impact: 24.2)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `R_PrecacheLevel` **(I/O & Config Routines)** (Impact: 20.1)
  * `R_GenerateLookup` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* // // R_GenerateLookup //
  * `R_GenerateComposite` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_DrawColumnInCache` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* // for a column directory and any new columns. // The directory will simply point inside other patch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 36`, `args: 15`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 185`, `dead_code: 6`, `unreferenced_by_name: 5`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` alloca.h, doomdef.h, doomstat.h, i_system.h, m_swap.h, p_local.h, r_data.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 598.3 | **LOC:** 587 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6229%), Tech Debt (38.8931%)
**Top Internal Functions/Classes:**
  * `P_UnArchiveSpecials` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_ArchiveSpecials` **(I/O & Config Routines)** (Impact: 18.8)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `P_UnArchiveThinkers` **(I/O & Config Routines)** (Impact: 12.9)
    * *Intent:* // // P_UnArchiveThinkers //
  * `P_ArchiveWorld` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* // // P_ArchiveWorld //
  * `P_UnArchiveWorld` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* // // P_UnArchiveWorld //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 43`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 183`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` doomstat.h, i_system.h, p_local.h, r_state.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 592.72 | **LOC:** 899 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6217%), Tech Debt (31.5212%)
**Top Internal Functions/Classes:**
  * `R_PointToAngle` **(Compute Cores)** (Impact: 33.6)
    * *Intent:* // // R_PointToAngle // To get a global angle from cartesian coordinates, // the coordinates are fli...
  * `R_PointOnSegSide` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `R_PointOnSide` **(Many-Argument Workhorses)** (Impact: 18.6)
    * *Intent:* // // R_PointOnSide // Traverse BSP (sub) tree, // check point against partition plane. // Returns s...
  * `R_InitTextureMapping` **(I/O & Config Routines)** (Impact: 18.0)
    * *Intent:* // // R_InitTextureMapping //
  * `R_ExecuteSetViewSize` **(I/O & Config Routines)** (Impact: 16.6)
    * *Intent:* // // R_ExecuteSetViewSize //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 59`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 141`, `dead_code: 4`, `unreferenced_by_name: 9`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` d_net.h, doomdef.h, m_bbox.h, math.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/f_finale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 577.78 | **LOC:** 739 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1097%), Tech Debt (39.8241%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` **(Compute Cores)** (Impact: 52.0)
    * *Intent:* // // F_CastTicker //
  * `F_StartFinale` **(I/O & Config Routines)** (Impact: 25.8)
    * *Intent:* // // F_StartFinale //
  * `F_Ticker` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* // // F_Ticker //
  * `F_CastPrint` **(Compute Cores)** (Impact: 15.2)
  * `F_TextWrite` **(I/O & Config Routines)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 101`, `args: 21`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 134`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 20`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` ctype.h, doomstat.h, dstrings.h, hu_stuff.h, i_system.h, m_swap.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/s_sound.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 551.92 | **LOC:** 880 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.1244%), Tech Debt (64.1572%)
**Top Internal Functions/Classes:**
  * `S_StartSoundAtVolume` **(Many-Argument Workhorses)** (Impact: 65.1)
  * `S_StartSound` **(Compute Cores)** (Impact: 32.9)
  * `S_AdjustSoundParams` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* // // Changes volume, stereo-separation, and pitch variables // from the norm of a sound effect to b...
  * `S_UpdateSounds` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* // // Updates music & sounds //
  * `S_getChannel` **(Compute Cores)** (Impact: 21.5)
    * *Intent:* // // S_getChannel : // If none available, return -1. Otherwise channel #. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 47`, `args: 20`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 95`, `dead_code: 7`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` doomdef.h, doomstat.h, i_sound.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 536.04 | **LOC:** 880 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0303%), Tech Debt (89.5571%)
**Top Internal Functions/Classes:**
  * `P_CheckAmmo` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM 128*FRACUNIT #defin...
  * `A_Saw` **(Compute Cores)** (Impact: 16.0)
    * *Intent:* // // A_Saw //
  * `A_ReFire` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* // // A_ReFire // The player can re-fire the weapon // without lowering it entirely. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 48`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 106`, `dead_code: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` d_event.h, doomdef.h, doomstat.h, m_random.h, p_local.h, p_pspr.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/i_sound.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 495.98 | **LOC:** 986 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.0777%), Tech Debt (99.8325%)
**Top Internal Functions/Classes:**
  * `addsfx` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* // // This function adds a sound to the // list of currently active sounds, // which is maintained a...
  * `I_UpdateSound` **(I/O & Config Routines)** (Impact: 20.8)
    * *Intent:* // // This function loops all active (internal) sound // channels, retrieves a given number of sampl...
  * `I_InitSound` **(I/O & Config Routines)** (Impact: 17.4)
  * `getsfx` **(Many-Argument Workhorses)** (Impact: 10.3)
    * *Intent:* // // This function loads the sound data from the WAD lump, // for single sound. //
  * `I_StartSound` **(Many-Argument Workhorses)** (Impact: 8.9)
    * *Intent:* // // Starting a sound means adding it // to the current list of active sounds // in the internal ch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 48`, `args: 29`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 113`, `dead_code: 8`, `fragile_debt: 4`, `unreferenced_by_name: 21`
* *Architecture:* `io: 3`, `api: 30`, `import: 20`
* *Defense:* `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomdef.h, fcntl.h, i_sound.h, i_system.h, soundcard.h, m_argv.h, m_misc.h, math.h...
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

- `linuxdoom-1.10/d_player.h` -> **Severity: 0.128** (Bridge: 0.01 * Flux: 12.7437%)
- `linuxdoom-1.10/p_mobj.h` -> **Severity: 0.058** (Bridge: 0.0045 * Flux: 13.0108%)
- `linuxdoom-1.10/d_event.h` -> **Severity: 0.019** (Bridge: 0.0006 * Flux: 31.0026%)
- `linuxdoom-1.10/d_net.h` -> **Severity: 0.012** (Bridge: 0.0007 * Flux: 16.7982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `linuxdoom-1.10/doomdef.h` -> **Severity: 18.788** (Embedded: 0.3202 * Error Risk: 58.6775%)
- `linuxdoom-1.10/d_event.h` -> **Severity: 10.712** (Embedded: 0.1712 * Error Risk: 62.5811%)
- `linuxdoom-1.10/d_player.h` -> **Severity: 10.264** (Embedded: 0.1796 * Error Risk: 57.1619%)
- `linuxdoom-1.10/d_net.h` -> **Severity: 8.469** (Embedded: 0.1399 * Error Risk: 60.5532%)
- `linuxdoom-1.10/p_mobj.h` -> **Severity: 7.622** (Embedded: 0.1327 * Error Risk: 57.4443%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ipx/DOOMNET.C` -> **Severity: 348.1** (Blast Radius: 3.481 * Doc Risk: 100.0%)
- `ipx/IPXNET.C` -> **Severity: 348.1** (Blast Radius: 3.481 * Doc Risk: 100.0%)
- `ipx/IPXSETUP.C` -> **Severity: 348.1** (Blast Radius: 3.481 * Doc Risk: 100.0%)
- `linuxdoom-1.10/am_map.c` -> **Severity: 348.1** (Blast Radius: 3.481 * Doc Risk: 100.0%)
- `linuxdoom-1.10/d_main.c` -> **Severity: 348.1** (Blast Radius: 3.481 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
