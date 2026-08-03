# ARCHITECTURAL_BRIEF: original_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/original_doom` |
| **Timestamp** | `2026-08-03T19:06:09.532934+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `a77dfb96cb91780ca334d0d4cfd86957558007e0` |
| **Git Remote** | `https://github.com/id-Software/DOOM.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 138 malicious artifacts.

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
| Total Artifacts | 165 |
| Analyzed Artifacts (Scanned) | 146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 24740 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3303 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1173 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6085 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 136 | 24642 | 93.2% |
| PLAINTEXT | 6 | 0 | 4.1% |
| MARKDOWN | 2 | 0 | 1.4% |
| MAKEFILE | 2 | 98 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.522`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_9 | 50 | 34.2% |
| file_cluster_13 | 49 | 33.6% |
| file_cluster_8 | 39 | 26.7% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 93.4 | 33.5 | 9.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 31.8 | 9.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.2 | 0.0 | 0.0 |
| Testing Exposure | 0.9 | 80.0 | 25.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 17.3 | 10.0 | 10.9 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.9 | 30.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 63.7 | 11.7 | 9.2 | 0.0 |
| Specification Exposure | 40.0 | 100.0 | 95.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 4.8 | 100.0 | 82.2 | 99.2 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 0.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `linuxdoom-1.10/w_wad.c` (Hits: 19)
- `linuxdoom-1.10/m_misc.c` (Hits: 18)
- `sndserv/soundsrv.c` (Hits: 10)

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

- `G_DoReborn` (@ `linuxdoom-1.10/g_game.c`) -> Impact: **289.6** | LOC: 711
- `P_UseSpecialLine` (@ `linuxdoom-1.10/p_switch.c`) -> Impact: **194.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `S_StartSoundAtVolume` (@ `linuxdoom-1.10/s_sound.c`) -> Impact: **181.0** | LOC: 140
- `D_DoomMain` (@ `linuxdoom-1.10/d_main.c`) -> Impact: **172.2** | LOC: 361
- `G_Ticker` (@ `linuxdoom-1.10/g_game.c`) -> Impact: **163.1** | LOC: 144
  * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
- `A_Fire` (@ `linuxdoom-1.10/p_enemy.c`) -> Impact: **147.3** | LOC: 666
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `D_Display` (@ `linuxdoom-1.10/d_main.c`) -> Impact: **132.4** | LOC: 153
- `M_Responder` (@ `linuxdoom-1.10/m_menu.c`) -> Impact: **127.4** | LOC: 368
  * *Intent:* // // SAVE GAME MENU
- `TryRunTics` (@ `linuxdoom-1.10/d_net.c`) -> Impact: **124.4** | LOC: 132
  * *Intent:* // check for exiting the game
- `F_CastTicker` (@ `linuxdoom-1.10/f_finale.c`) -> Impact: **119.4** | LOC: 101
  * *Intent:* // // F_CastTicker //

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `GetPacket` (@ `ipx/IPXNET.C`) -> **O(2^N) [Recursive]**
  * *Intent:* // set the length (ipx + time + datalength)
- `SendPacket` (@ `ipx/IPXNET.C`) -> **O(2^N) [Recursive]**
- `ListenForPacket` (@ `ipx/IPXNET.C`) -> **O(2^N) [Recursive]**
- `R_Subsector` (@ `linuxdoom-1.10/r_bsp.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // R_Subsector // Determine floor/ceiling planes. // Add sprites of things in sector. // Draw one or more line segments. //
- `R_InitTextures` (@ `linuxdoom-1.10/r_data.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
- `S_StartSoundAtVolume` (@ `linuxdoom-1.10/s_sound.c`) -> **O(2^N) [Recursive]**
- `V_DrawPatch` (@ `linuxdoom-1.10/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
- `V_DrawPatchFlipped` (@ `linuxdoom-1.10/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e.g. to mirror face. //
- `OpenSocket` (@ `ipx/IPXNET.C`) -> **O(2^N) [Recursive]**
- `TryRunTics` (@ `linuxdoom-1.10/d_net.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // check for exiting the game

### Highest Data Gravity (Database Complexity)
- `G_DoReborn` (@ `linuxdoom-1.10/g_game.c`) -> DB Complexity: **264**
- `A_Fire` (@ `linuxdoom-1.10/p_enemy.c`) -> DB Complexity: **105**
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `I_FinishUpdate` (@ `linuxdoom-1.10/i_video.c`) -> DB Complexity: **92**
  * *Intent:* // // I_FinishUpdate //
- `PIT_StompThing` (@ `linuxdoom-1.10/p_map.c`) -> DB Complexity: **81**
  * *Intent:* // // TELEPORT MOVE //
- `M_Responder` (@ `linuxdoom-1.10/m_menu.c`) -> DB Complexity: **76**
  * *Intent:* // // SAVE GAME MENU
- `EV_DoFloor` (@ `linuxdoom-1.10/p_floor.c`) -> DB Complexity: **76**
  * *Intent:* // // HANDLE FLOOR TYPES //
- `mix` (@ `sndserv/soundsrv.c`) -> DB Complexity: **70**
- `R_InitTextures` (@ `linuxdoom-1.10/r_data.c`) -> DB Complexity: **69**
  * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
- `G_BuildTiccmd` (@ `linuxdoom-1.10/g_game.c`) -> DB Complexity: **65**
  * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo buffer. // If recording a demo, write it out //
- `I_InitGraphics` (@ `linuxdoom-1.10/i_video.c`) -> DB Complexity: **56**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `linuxdoom-1.10` | 119 | 29116.88 | 32.32% | 22.69% |
| `sndserv` | 9 | 1222.08 | 26.73% | 19.47% |
| `sersrc` | 8 | 940.88 | 35.24% | 16.77% |
| `ipx` | 8 | 751.56 | 31.34% | 6.66% |
| `__monolith__` | 2 | 8.46 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `linuxdoom-1.10/p_tick.c` -> **99.9999%** Exposure
- `linuxdoom-1.10/p_setup.h` -> **99.9997%** Exposure
- `linuxdoom-1.10/m_swap.c` -> **99.9955%** Exposure
- `linuxdoom-1.10/i_system.c` -> **99.9897%** Exposure
- `linuxdoom-1.10/m_fixed.c` -> **99.9792%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ipx/IPXNET.C` -> **100.0%** Exposure
- `ipx/IPXSETUP.C` -> **100.0%** Exposure
- `linuxdoom-1.10/d_main.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_net.c` -> **100.0%** Exposure
- `linuxdoom-1.10/f_finale.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `linuxdoom-1.10/p_enemy.c` -> **22** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/i_system.c` -> **12** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/m_menu.c` -> **11** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/r_draw.c` -> **7** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ipx/IPXSETUP.C`** -> AI Confidence: **99.48%**
2. **`linuxdoom-1.10/d_net.c`** -> AI Confidence: **99.48%**
3. **`linuxdoom-1.10/i_video.c`** -> AI Confidence: **99.48%**
4. **`linuxdoom-1.10/p_ceilng.c`** -> AI Confidence: **99.48%**
5. **`linuxdoom-1.10/p_doors.c`** -> AI Confidence: **99.48%**
6. **`linuxdoom-1.10/p_floor.c`** -> AI Confidence: **99.48%**
7. **`linuxdoom-1.10/p_mobj.c`** -> AI Confidence: **99.48%**
8. **`linuxdoom-1.10/p_plats.c`** -> AI Confidence: **99.48%**
9. **`linuxdoom-1.10/p_setup.c`** -> AI Confidence: **99.48%**
10. **`linuxdoom-1.10/p_switch.c`** -> AI Confidence: **99.48%**
11. **`linuxdoom-1.10/r_plane.c`** -> AI Confidence: **99.48%**
12. **`linuxdoom-1.10/v_video.c`** -> AI Confidence: **99.48%**
13. **`sndserv/soundsrv.c`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `ipx/IPXNET.C` -> **20.0%** Exposure
- `sersrc/SERSTR.H` -> **20.0%** Exposure
- `linuxdoom-1.10/d_englsh.h` -> **0.0066%** Exposure
### Weaponizable Injection Vectors
- `sersrc/SERSTR.H` -> **100.0%** Exposure
- `linuxdoom-1.10/d_englsh.h` -> **1.1768%** Exposure
### Raw Memory Manipulation
- `linuxdoom-1.10/d_net.c` -> **0.3848%** Exposure
- `linuxdoom-1.10/i_video.c` -> **0.0078%** Exposure
- `linuxdoom-1.10/r_main.c` -> **0.0005%** Exposure
### Algorithmic DoS Exposure
- `ipx/IPXNET.C` -> **100.0%** Exposure
- `linuxdoom-1.10/d_main.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_net.c` -> **100.0%** Exposure
- `linuxdoom-1.10/g_game.c` -> **100.0%** Exposure
- `linuxdoom-1.10/i_sound.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `645` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `linuxdoom-1.10/i_sound.c` (C) -> Cumulative Risk: **769.22**
- **Archetype:** `file_cluster_13` (Distance: 14.5 IQR)
- **Magnitude:** 665.1 | **LOC:** 986 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7327%)
- **Heaviest Functions:** `addsfx` (Impact: 52.9), `I_UpdateSound` (Impact: 35.8), `I_InitSound` (Impact: 30.4)

### 2. `linuxdoom-1.10/m_menu.c` (C) -> Cumulative Risk: **718.25**
- **Archetype:** `file_cluster_13` (Distance: 13.191 IQR)
- **Magnitude:** 943.8 | **LOC:** 1894 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9999%), Documentation (94.9304%)
- **Heaviest Functions:** `M_Responder` (Impact: 127.4), `M_Drawer` (Impact: 31.9), `M_WriteText` (Impact: 24.1)

### 3. `linuxdoom-1.10/d_main.c` (C) -> Cumulative Risk: **698.88**
- **Archetype:** `file_cluster_13` (Distance: 13.181 IQR)
- **Magnitude:** 1005.98 | **LOC:** 1172 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.5014%)
- **Heaviest Functions:** `D_DoomMain` (Impact: 172.2), `D_Display` (Impact: 132.4), `D_DoAdvanceDemo` (Impact: 48.3)

### 4. `linuxdoom-1.10/s_sound.c` (C) -> Cumulative Risk: **695.34**
- **Archetype:** `file_cluster_13` (Distance: 13.943 IQR)
- **Magnitude:** 794.02 | **LOC:** 880 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.8804%)
- **Heaviest Functions:** `S_StartSoundAtVolume` (Impact: 181.0), `S_UpdateSounds` (Impact: 40.4), `S_StartSound` (Impact: 32.9)

### 5. `linuxdoom-1.10/p_mobj.c` (C) -> Cumulative Risk: **694.87**
- **Archetype:** `file_cluster_13` (Distance: 13.984 IQR)
- **Magnitude:** 477.62 | **LOC:** 989 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (83.1037%)
- **Heaviest Functions:** `P_XYMovement` (Impact: 50.4), `P_ZMovement` (Impact: 47.2), `P_SpawnMissile` (Impact: 8.0)

### 6. `linuxdoom-1.10/i_video.c` (C) -> Cumulative Risk: **689.64**
- **Archetype:** `file_cluster_13` (Distance: 14.177 IQR)
- **Magnitude:** 1335.18 | **LOC:** 1051 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6735%)
- **Heaviest Functions:** `xlatekey` (Impact: 99.5), `I_InitGraphics` (Impact: 87.6), `grabsharedmemory` (Impact: 59.4)

### 7. `sndserv/soundsrv.c` (C) -> Cumulative Risk: **684.85**
- **Archetype:** `file_cluster_13` (Distance: 14.888 IQR)
- **Magnitude:** 877.48 | **LOC:** 741 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.677%)
- **Heaviest Functions:** `main` (Impact: 101.2), `addsfx` (Impact: 51.6), `mix` (Impact: 44.7)

### 8. `linuxdoom-1.10/p_floor.c` (C) -> Cumulative Risk: **682.11**
- **Archetype:** `file_cluster_13` (Distance: 14.496 IQR)
- **Magnitude:** 689.66 | **LOC:** 556 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.1258%)
- **Heaviest Functions:** `EV_DoFloor` (Impact: 76.8), `T_MovePlane` (Impact: 42.8), `EV_BuildStairs` (Impact: 26.1)

### 9. `linuxdoom-1.10/p_plats.c` (C) -> Cumulative Risk: **681.84**
- **Archetype:** `file_cluster_13` (Distance: 13.495 IQR)
- **Magnitude:** 346.24 | **LOC:** 315 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.9317%)
- **Heaviest Functions:** `T_PlatRaise` (Impact: 47.5), `EV_DoPlat` (Impact: 29.9), `P_ActivateInStasis` (Impact: 9.4)

### 10. `linuxdoom-1.10/g_game.c` (C) -> Cumulative Risk: **681.57**
- **Archetype:** `file_cluster_13` (Distance: 14.555 IQR)
- **Magnitude:** 1917.94 | **LOC:** 1691 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7157%)
- **Heaviest Functions:** `G_DoReborn` (Impact: 289.6), `G_Ticker` (Impact: 163.1), `G_BuildTiccmd` (Impact: 71.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `linuxdoom-1.10/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.555 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.641 IQR)
- **Top Global Matches:** file_cluster_13: 14.555, file_cluster_11: 14.725, file_cluster_8: 14.765
- **Magnitude:** 1917.94 | **LOC:** 1691 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 264
- **Risk Profile:** Cognitive Load (74.2028%), Tech Debt (11.7727%)
**Top Internal Functions/Classes:**
  * `G_DoReborn` (Impact: 289.6 | O(N^1) | DB: 264)
  * `G_Ticker` (Impact: 163.1 | O(N^2) | DB: 15)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_BuildTiccmd` (Impact: 71.0 | O(N^1) | DB: 65)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_Responder` (Impact: 43.7 | O(N^1) | DB: 16)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_DoLoadLevel` (Impact: 21.7 | O(N^1) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 159`, `args: 34`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1050`, `dead_code: 10`, `orphaned_logic: 5`
* *Architecture:* `api: 236`, `import: 28`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` m_menu.h, string.h, m_random.h, d_main.h, st_stuff.h, stdlib.h, doomstat.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.446 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.984 IQR)
- **Top Global Matches:** file_cluster_8: 13.446, file_cluster_13: 13.599, file_cluster_0: 13.778
- **Magnitude:** 1561.04 | **LOC:** 1851 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (71.2149%), Tech Debt (22.7657%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` (Impact: 78.3 | O(N^1) | DB: 40)
  * `WI_loadData` (Impact: 55.1 | O(N^2) | DB: 47)
  * `WI_updateDeathmatchStats` (Impact: 46.0 | O(N^1) | DB: 25)
  * `WI_updateStats` (Impact: 44.8 | O(N^1) | DB: 24)
  * `WI_updateAnimatedBack` (Impact: 29.4 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 101`, `args: 33`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 837`, `dead_code: 4`, `fragile_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 159`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` z_zone.h, doomstat.h, s_sound.h, stdio.h, g_game.h, wi_stuff.h, r_local.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.607 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.36 IQR)
- **Top Global Matches:** file_cluster_8: 13.607, file_cluster_13: 13.727, file_cluster_0: 13.826
- **Magnitude:** 1453.26 | **LOC:** 2009 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (92.4303%), Tech Debt (32.0145%)
**Top Internal Functions/Classes:**
  * `A_Fire` (Impact: 147.3 | O(N^1) | DB: 105)
    * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
  * `P_NewChaseDir` (Impact: 74.3 | O(2^N) | DB: 27)
  * `A_Chase` (Impact: 39.2 | O(N^1) | DB: 10)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `P_RecursiveSound` (Impact: 28.2 | O(2^N) | DB: 8)
  * `P_CheckMissileRange` (Impact: 27.0 | O(N^2) | DB: 5)
    * *Intent:* // // P_CheckMissileRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 180`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 683`, `dead_code: 7`, `orphaned_logic: 22`
* *Architecture:* `io: 1`, `api: 255`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` stdlib.h, doomstat.h, doomdef.h, s_sound.h, g_game.h, m_random.h, sounds.h, r_state.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/i_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.177 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.899 IQR)
- **Top Global Matches:** file_cluster_13: 14.177, file_cluster_8: 14.318, file_cluster_11: 14.406
- **Magnitude:** 1335.18 | **LOC:** 1051 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (74.9544%), Tech Debt (20.0992%)
**Top Internal Functions/Classes:**
  * `xlatekey` (Impact: 99.5 | O(N^1) | DB: 29)
    * *Intent:* // // Translates the key currently in X_event //
  * `I_InitGraphics` (Impact: 87.6 | O(N^2) | DB: 56)
  * `grabsharedmemory` (Impact: 59.4 | O(N^2) | DB: 20)
    * *Intent:* // // This function is probably redundant, // if XShmDetach works properly. // ddt never detached th...
  * `I_GetEvent` (Impact: 53.8 | O(N^1) | DB: 22)
  * `I_FinishUpdate` (Impact: 51.8 | O(N^1) | DB: 92)
    * *Intent:* // // I_FinishUpdate //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 41`, `args: 13`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 761`, `dead_code: 3`, `orphaned_logic: 8`
* *Architecture:* `io: 4`, `api: 146`, `import: 21`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Xutil.h, socket.h, keysym.h, d_main.h, in.h, stdlib.h, doomstat.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.64 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.37 IQR)
- **Top Global Matches:** file_cluster_13: 14.64, file_cluster_8: 14.735, file_cluster_11: 14.762
- **Magnitude:** 1047.34 | **LOC:** 990 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (70.8812%), Tech Debt (12.7484%)
**Top Internal Functions/Classes:**
  * `R_ProjectSprite` (Impact: 49.6 | O(2^N) | DB: 44)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` (Impact: 49.2 | O(N^1) | DB: 27)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_InstallSpriteLump` (Impact: 47.4 | O(2^N) | DB: 13)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
  * `R_DrawSprite` (Impact: 39.5 | O(N^1) | DB: 31)
    * *Intent:* // // R_DrawSprite //
  * `R_DrawPSprite` (Impact: 21.7 | O(N^1) | DB: 25)
    * *Intent:* // // R_DrawPSprite //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 39`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 626`, `dead_code: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 125`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stdlib.h, z_zone.h, doomstat.h, doomdef.h, stdio.h, r_local.h, w_wad.h, m_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/d_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.181 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.484 IQR)
- **Top Global Matches:** file_cluster_13: 13.181, file_cluster_8: 13.418, file_cluster_11: 13.517
- **Magnitude:** 1005.98 | **LOC:** 1172 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (93.3814%), Tech Debt (36.3875%)
**Top Internal Functions/Classes:**
  * `D_DoomMain` (Impact: 172.2 | O(N^1) | DB: 54)
  * `D_Display` (Impact: 132.4 | O(N^2) | DB: 28)
  * `D_DoAdvanceDemo` (Impact: 48.3 | O(N^1) | DB: 20)
    * *Intent:* // // This cycles through the demo sequences. // FIXME - version dependend demo numbers? //
  * `FindResponseFile` (Impact: 45.0 | O(N^2) | DB: 44)
  * `D_DoomLoop` (Impact: 14.8 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 69`, `args: 18`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 1`, `state_mutation: 448`, `dead_code: 4`, `fragile_debt: 4`, `orphaned_logic: 3`
* *Architecture:* `io: 7`, `api: 104`, `import: 30`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` fcntl.h, m_menu.h, d_main.h, st_stuff.h, stdlib.h, stat.h, doomstat.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.998 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.565 IQR)
- **Top Global Matches:** file_cluster_13: 13.998, file_cluster_8: 14.087, file_cluster_0: 14.232
- **Magnitude:** 1001.88 | **LOC:** 1472 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (88.4749%), Tech Debt (14.2273%)
**Top Internal Functions/Classes:**
  * `ST_updateFaceWidget` (Impact: 80.7 | O(N^2) | DB: 46)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_Responder` (Impact: 75.5 | O(N^1) | DB: 54)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_doPaletteStuff` (Impact: 21.0 | O(N^1) | DB: 13)
  * `ST_updateWidgets` (Impact: 20.1 | O(N^1) | DB: 18)
  * `ST_loadGraphics` (Impact: 12.3 | O(N^1) | DB: 36)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 71`, `args: 18`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 617`, `dead_code: 8`, `orphaned_logic: 6`
* *Architecture:* `api: 98`, `import: 20`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` p_inter.h, m_random.h, st_stuff.h, st_lib.h, doomstat.h, doomdef.h, stdio.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.191 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.598 IQR)
- **Top Global Matches:** file_cluster_13: 13.191, file_cluster_8: 13.3, file_cluster_11: 13.534
- **Magnitude:** 943.8 | **LOC:** 1894 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (92.9894%), Tech Debt (61.7618%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 127.4 | O(N^1) | DB: 76)
    * *Intent:* // // SAVE GAME MENU
  * `M_Drawer` (Impact: 31.9 | O(N^2) | DB: 15)
  * `M_WriteText` (Impact: 24.1 | O(N^1) | DB: 11)
  * `M_Init` (Impact: 19.6 | O(N^1) | DB: 19)
  * `M_SizeDisplay` (Impact: 15.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 113`, `args: 21`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 472`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 11`
* *Architecture:* `io: 1`, `api: 147`, `import: 23`
* *Defense:* `safety: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` fcntl.h, m_menu.h, d_main.h, stdlib.h, stat.h, doomstat.h, doomdef.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.421 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.72 IQR)
- **Top Global Matches:** file_cluster_13: 13.421, file_cluster_8: 13.463, file_cluster_11: 13.669
- **Magnitude:** 937.88 | **LOC:** 739 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (78.8106%), Tech Debt (39.8241%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` (Impact: 119.4 | O(N^1) | DB: 38)
    * *Intent:* // // F_CastTicker //
  * `F_StartFinale` (Impact: 67.2 | O(N^1) | DB: 28)
    * *Intent:* // // F_StartFinale //
  * `F_TextWrite` (Impact: 29.3 | O(N^1) | DB: 22)
  * `F_CastPrint` (Impact: 28.4 | O(N^1) | DB: 16)
  * `F_Drawer` (Impact: 27.8 | O(N^1))
    * *Intent:* // // F_Drawer //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 55`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 453`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 132`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` z_zone.h, doomstat.h, r_state.h, s_sound.h, ctype.h, hu_stuff.h, sounds.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_setup.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.049 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.547 IQR)
- **Top Global Matches:** file_cluster_13: 15.049, file_cluster_11: 15.226, file_cluster_0: 15.248
- **Magnitude:** 919.44 | **LOC:** 709 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (64.6557%), Tech Debt (12.4232%)
**Top Internal Functions/Classes:**
  * `P_GroupLines` (Impact: 52.4 | O(2^N) | DB: 41)
    * *Intent:* // // P_GroupLines // Builds sector line lists and subsector sector numbers. // Finds block bounding...
  * `P_LoadThings` (Impact: 36.5 | O(N^1) | DB: 13)
    * *Intent:* // // P_LoadThings //
  * `P_LoadLineDefs` (Impact: 35.8 | O(N^1) | DB: 36)
    * *Intent:* // // P_LoadLineDefs // Also counts secret lines for intermissions. //
  * `P_SetupLevel` (Impact: 34.6 | O(N^1) | DB: 26)
    * *Intent:* // // P_SetupLevel //
  * `P_LoadSegs` (Impact: 9.9 | O(N^1) | DB: 21)
    * *Intent:* // // P_LoadSegs //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 18`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 601`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 102`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` z_zone.h, doomstat.h, doomdef.h, s_sound.h, m_bbox.h, g_game.h, math.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_data.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.405 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.22 IQR)
- **Top Global Matches:** file_cluster_13: 14.405, file_cluster_0: 14.575, file_cluster_11: 14.587
- **Magnitude:** 902.64 | **LOC:** 850 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (62.0622%), Tech Debt (13.9866%)
**Top Internal Functions/Classes:**
  * `R_InitTextures` (Impact: 91.3 | O(2^N) | DB: 69)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `R_GenerateLookup` (Impact: 44.0 | O(2^N) | DB: 26)
    * *Intent:* // // R_GenerateLookup //
  * `R_PrecacheLevel` (Impact: 34.6 | O(N^1) | DB: 39)
  * `R_GenerateComposite` (Impact: 27.1 | O(N^2) | DB: 17)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_FlatNumForName` (Impact: 8.8 | O(2^N) | DB: 2)
    * *Intent:* // // R_FlatNumForName // Retrieval, get a flat number for a flat name. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 12`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 499`, `dead_code: 6`, `orphaned_logic: 3`
* *Architecture:* `api: 142`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` z_zone.h, doomstat.h, doomdef.h, r_sky.h, r_local.h, r_data.h, w_wad.h, m_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sndserv/soundsrv.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.888 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.969 IQR)
- **Top Global Matches:** file_cluster_13: 14.888, file_cluster_11: 15.026, file_cluster_0: 15.071
- **Magnitude:** 877.48 | **LOC:** 741 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (71.6724%), Tech Debt (12.2113%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 101.2 | O(N^2) | DB: 56)
  * `addsfx` (Impact: 51.6 | O(N^1) | DB: 29)
  * `mix` (Impact: 44.7 | O(N^1) | DB: 70)
  * `grabdata` (Impact: 38.0 | O(N^1) | DB: 23)
  * `outputushort` (Impact: 13.3 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 20`, `args: 10`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 515`, `dead_code: 8`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 90`, `import: 13`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types.h, stdlib.h, soundsrv.h, stat.h, fcntl.h, time.h, stdio.h, wadread.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.576 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.102 IQR)
- **Top Global Matches:** file_cluster_8: 14.576, file_cluster_13: 14.64, file_cluster_11: 14.809
- **Magnitude:** 829.1 | **LOC:** 587 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (68.7909%), Tech Debt (38.8931%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` (Impact: 43.9 | O(N^1) | DB: 46)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `P_UnArchiveSpecials` (Impact: 41.9 | O(N^1) | DB: 34)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_UnArchiveThinkers` (Impact: 22.0 | O(N^1) | DB: 15)
    * *Intent:* // // P_UnArchiveThinkers //
  * `P_ArchiveWorld` (Impact: 12.7 | O(N^1) | DB: 43)
    * *Intent:* // // P_ArchiveWorld //
  * `P_UnArchiveWorld` (Impact: 12.6 | O(N^1) | DB: 45)
    * *Intent:* // // P_UnArchiveWorld //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 593`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 61`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` z_zone.h, doomstat.h, r_state.h, p_local.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_draw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.332 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.985 IQR)
- **Top Global Matches:** file_cluster_13: 14.332, file_cluster_8: 14.428, file_cluster_0: 14.451
- **Magnitude:** 798.46 | **LOC:** 878 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (63.9374%), Tech Debt (98.9557%)
**Top Internal Functions/Classes:**
  * `R_DrawFuzzColumn` (Impact: 37.8 | O(2^N) | DB: 12)
    * *Intent:* // // Framebuffer postprocessing. // Creates a fuzzy image by copying pixels // from adjacent ones t...
  * `R_DrawColumn` (Impact: 26.4 | O(2^N) | DB: 8)
    * *Intent:* // // A column is a vertical slice/span from a wall texture that, // given the DOOM style restrictio...
  * `R_DrawSpan` (Impact: 26.4 | O(2^N) | DB: 10)
  * `R_FillBackScreen` (Impact: 23.1 | O(N^1) | DB: 24)
  * `R_DrawTranslatedColumn` (Impact: 14.5 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 31`, `args: 14`, `func_start: 13`
* *Risk/State:* `state_mutation: 475`, `dead_code: 5`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 7`
* *Architecture:* `api: 112`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` z_zone.h, doomstat.h, doomdef.h, r_local.h, w_wad.h, v_video.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.943 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.157 IQR)
- **Top Global Matches:** file_cluster_13: 13.943, file_cluster_0: 14.131, file_cluster_8: 14.135
- **Magnitude:** 794.02 | **LOC:** 880 | **CtrlFlow:** 73.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (71.4196%), Tech Debt (57.1666%)
**Top Internal Functions/Classes:**
  * `S_StartSoundAtVolume` (Impact: 181.0 | O(2^N) | DB: 22)
  * `S_UpdateSounds` (Impact: 40.4 | O(N^2) | DB: 12)
    * *Intent:* //
  * `S_StartSound` (Impact: 32.9 | O(N^1) | DB: 17)
  * `S_getChannel` (Impact: 26.7 | O(N^1) | DB: 7)
  * `S_StopChannel` (Impact: 15.6 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 41`, `args: 17`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 307`, `dead_code: 7`, `fragile_debt: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 89`, `import: 12`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` stdlib.h, z_zone.h, doomstat.h, doomdef.h, s_sound.h, stdio.h, i_sound.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.757 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.428 IQR)
- **Top Global Matches:** file_cluster_8: 13.757, file_cluster_13: 13.764, file_cluster_0: 13.899
- **Magnitude:** 770.02 | **LOC:** 899 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (64.4576%), Tech Debt (31.5212%)
**Top Internal Functions/Classes:**
  * `R_InitTextureMapping` (Impact: 29.0 | O(N^1) | DB: 22)
    * *Intent:* // // R_InitTextureMapping //
  * `R_ExecuteSetViewSize` (Impact: 25.3 | O(N^1) | DB: 45)
    * *Intent:* // // R_ExecuteSetViewSize //
  * `R_PointToAngle` (Impact: 21.2 | O(N^1) | DB: 5)
    * *Intent:* // // R_PointToAngle // To get a global angle from cartesian coordinates, // the coordinates are fli...
  * `R_PointOnSegSide` (Impact: 11.1 | O(N^1) | DB: 8)
  * `R_AddPointToBox` (Impact: 10.8 | O(N^1) | DB: 4)
    * *Intent:* // // R_AddPointToBox // Expand a given bbox // so that it encloses a given point. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 60`, `args: 8`, `func_start: 17`
* *Risk/State:* `state_mutation: 450`, `dead_code: 4`, `orphaned_logic: 9`
* *Architecture:* `api: 145`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdlib.h, doomdef.h, r_sky.h, m_bbox.h, r_local.h, d_net.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.674 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.43 IQR)
- **Top Global Matches:** file_cluster_8: 13.674, file_cluster_13: 13.679, file_cluster_11: 13.843
- **Magnitude:** 706.0 | **LOC:** 765 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (78.9365%), Tech Debt (24.5297%)
**Top Internal Functions/Classes:**
  * `T_VerticalDoor` (Impact: 92.3 | O(N^2) | DB: 26)
    * *Intent:* #endif // // VERTICAL DOORS // // // T_VerticalDoor //
  * `EV_VerticalDoor` (Impact: 61.4 | O(N^1) | DB: 30)
    * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
  * `EV_DoDoor` (Impact: 35.8 | O(N^2) | DB: 34)
  * `T_SlidingDoor` (Impact: 25.2 | O(N^1) | DB: 22)
  * `EV_DoLockedDoor` (Impact: 23.8 | O(N^1) | DB: 4)
    * *Intent:* // // EV_DoLockedDoor // Move a locked door up/down //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 31`, `args: 1`, `func_start: 10`
* *Risk/State:* `state_mutation: 368`, `dead_code: 4`, `orphaned_logic: 7`
* *Architecture:* `io: 6`, `api: 69`, `import: 8`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` z_zone.h, doomstat.h, doomdef.h, s_sound.h, sounds.h, r_state.h, dstrings.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.496 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.465 IQR)
- **Top Global Matches:** file_cluster_13: 14.496, file_cluster_8: 14.604, file_cluster_11: 14.63
- **Magnitude:** 689.66 | **LOC:** 556 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (73.9598%), Tech Debt (12.7568%)
**Top Internal Functions/Classes:**
  * `EV_DoFloor` (Impact: 76.8 | O(N^2) | DB: 76)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `T_MovePlane` (Impact: 42.8 | O(N^1) | DB: 32)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_BuildStairs` (Impact: 26.1 | O(N^1) | DB: 36)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` (Impact: 23.3 | O(N^2) | DB: 6)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 26`, `func_start: 4`
* *Risk/State:* `state_mutation: 449`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `api: 63`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` z_zone.h, doomstat.h, doomdef.h, s_sound.h, sounds.h, r_state.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/i_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.5 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.036 IQR)
- **Top Global Matches:** file_cluster_13: 14.5, file_cluster_11: 14.735, file_cluster_0: 14.74
- **Magnitude:** 665.1 | **LOC:** 986 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (87.5852%), Tech Debt (99.7027%)
**Top Internal Functions/Classes:**
  * `addsfx` (Impact: 52.9 | O(N^1) | DB: 29)
    * *Intent:* // // This function adds a sound to the // list of currently active sounds, // which is maintained a...
  * `I_UpdateSound` (Impact: 35.8 | O(N^1) | DB: 28)
    * *Intent:* // // This function loops all active (internal) sound // channels, retrieves a given number of sampl...
  * `I_InitSound` (Impact: 30.4 | O(2^N) | DB: 20)
  * `I_ShutdownSound` (Impact: 18.9 | O(2^N) | DB: 7)
  * `getsfx` (Impact: 13.7 | O(N^2) | DB: 10)
    * *Intent:* // // This function loads the sound data from the WAD lump, // for single sound. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 46`, `args: 24`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 323`, `dead_code: 8`, `fragile_debt: 4`, `orphaned_logic: 19`
* *Architecture:* `io: 6`, `api: 113`, `import: 20`
* *Defense:* `doc: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` fcntl.h, stdlib.h, doomdef.h, time.h, stdio.h, stdarg.h, signal.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/d_net.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.801 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.969 IQR)
- **Top Global Matches:** file_cluster_13: 13.801, file_cluster_8: 13.926, file_cluster_11: 14.039
- **Magnitude:** 536.7 | **LOC:** 768 | **CtrlFlow:** 79.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (76.2224%), Tech Debt (16.4818%)
**Top Internal Functions/Classes:**
  * `TryRunTics` (Impact: 124.4 | O(2^N) | DB: 35)
    * *Intent:* // check for exiting the game
  * `D_ArbitrateNetStart` (Impact: 45.2 | O(N^1) | DB: 22)
  * `D_CheckNetGame` (Impact: 20.2 | O(N^2) | DB: 18)
  * `D_QuitNetGame` (Impact: 16.6 | O(N^1) | DB: 9)
  * `CheckAbort` (Impact: 9.6 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 21`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 284`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 31`, `import: 7`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` i_net.h, doomstat.h, doomdef.h, i_video.h, m_menu.h, g_game.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_maputl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.652 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.51 IQR)
- **Top Global Matches:** file_cluster_8: 13.652, file_cluster_13: 13.759, file_cluster_0: 13.955
- **Magnitude:** 514.02 | **LOC:** 884 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (68.9525%), Tech Debt (21.1002%)
**Top Internal Functions/Classes:**
  * `P_BoxOnLineSide` (Impact: 15.2 | O(N^1) | DB: 12)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
  * `P_UnsetThingPosition` (Impact: 10.3 | O(N^1) | DB: 5)
    * *Intent:* // // THING POSITION SETTING // // // P_UnsetThingPosition // Unlinks a thing from block map and sec...
  * `P_PointOnDivlineSide` (Impact: 10.2 | O(N^1) | DB: 4)
    * *Intent:* // // P_PointOnDivlineSide // Returns 0 or 1. //
  * `PIT_AddThingIntercepts` (Impact: 8.4 | O(N^1) | DB: 18)
  * `P_PointOnLineSide` (Impact: 7.8 | O(N^1) | DB: 4)
    * *Intent:* // // P_PointOnLineSide // Returns 0 or 1 //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 44`, `func_start: 9`
* *Risk/State:* `state_mutation: 347`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 88`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdlib.h, doomdef.h, m_bbox.h, r_state.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.441 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.562 IQR)
- **Top Global Matches:** file_cluster_8: 12.441, file_cluster_13: 12.523, file_cluster_0: 12.823
- **Magnitude:** 504.76 | **LOC:** 494 | **CtrlFlow:** 80.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (63.6985%), Tech Debt (20.0722%)
**Top Internal Functions/Classes:**
  * `V_CopyRect` (Impact: 74.0 | O(2^N) | DB: 5)
    * *Intent:* // // V_CopyRect //
  * `V_DrawPatch` (Impact: 70.1 | O(2^N) | DB: 17)
    * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
  * `V_DrawPatchFlipped` (Impact: 70.0 | O(2^N) | DB: 17)
    * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e....
  * `V_DrawBlock` (Impact: 38.7 | O(2^N) | DB: 4)
  * `V_GetBlock` (Impact: 20.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 10`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 155`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomdef.h, m_bbox.h, r_local.h, m_swap.h, doomdata.h, v_video.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.102 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.894 IQR)
- **Top Global Matches:** file_cluster_13: 14.102, file_cluster_8: 14.214, file_cluster_0: 14.293
- **Magnitude:** 501.26 | **LOC:** 747 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (69.3914%), Tech Debt (15.777%)
**Top Internal Functions/Classes:**
  * `R_RenderSegLoop` (Impact: 78.1 | O(N^2) | DB: 52)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
  * `R_StoreWallRange` (Impact: 37.7 | O(N^1) | DB: 21)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` (Impact: 21.4 | O(N^1) | DB: 31)
    * *Intent:* // // R_RenderMaskedSegRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 6`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 297`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 61`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdlib.h, doomstat.h, doomdef.h, r_sky.h, r_local.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/w_wad.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.455 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.612 IQR)
- **Top Global Matches:** file_cluster_13: 13.455, file_cluster_0: 13.725, file_cluster_11: 13.728
- **Magnitude:** 483.36 | **LOC:** 578 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (65.8439%), Tech Debt (57.1109%)
**Top Internal Functions/Classes:**
  * `W_AddFile` (Impact: 26.3 | O(N^1) | DB: 39)
  * `W_ReadLump` (Impact: 26.1 | O(2^N) | DB: 19)
    * *Intent:* // // W_ReadLump // Loads the lump into the given buffer, // which must be >= W_LumpLength(). //
  * `W_Profile` (Impact: 25.2 | O(N^1) | DB: 25)
  * `W_Reload` (Impact: 19.3 | O(2^N) | DB: 27)
    * *Intent:* // // W_Reload // Flushes any of the reloadable lumps in memory // and reloads the directory. //
  * `W_CacheLumpNum` (Impact: 15.2 | O(2^N) | DB: 1)
    * *Intent:* // // W_CacheLumpNum //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 28`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 227`, `dead_code: 3`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 19`, `api: 73`, `import: 13`
* *Defense:* `safety: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` types.h, stat.h, z_zone.h, fcntl.h, string.h, doomtype.h, ctype.h, m_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_pspr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.073 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_8: 13.073, file_cluster_13: 13.15, file_cluster_0: 13.39
- **Magnitude:** 480.82 | **LOC:** 880 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (68.0241%), Tech Debt (25.1614%)
**Top Internal Functions/Classes:**
  * `A_Lower` (Impact: 56.5 | O(N^2) | DB: 54)
    * *Intent:* // // A_Lower // Lowers current weapon, // and changes weapon at bottom. //
  * `P_CheckAmmo` (Impact: 38.0 | O(N^1) | DB: 13)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` (Impact: 14.7 | O(N^1) | DB: 7)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` (Impact: 11.2 | O(N^1) | DB: 8)
    * *Intent:* #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM 128*FRACUNIT #defin...
  * `A_ReFire` (Impact: 6.0 | O(N^1) | DB: 2)
    * *Intent:* // // A_ReFire // The player can re-fire the weapon // without lowering it entirely. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 38`, `func_start: 26`
* *Risk/State:* `state_mutation: 249`, `dead_code: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 83`, `import: 8`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` p_pspr.h, doomstat.h, doomdef.h, s_sound.h, m_random.h, sounds.h, d_event.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `linuxdoom-1.10/z_zone.c` (C) | Magnitude: 281.34 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 137, pointers: 115, indent_spaces: 78, indent_tabs: 51
- `linuxdoom-1.10/f_finale.c` (C) | Magnitude: 937.88 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 453, indent_spaces: 190, branch: 170, api: 132
- `linuxdoom-1.10/r_sky.c` (C) | Magnitude: 8.3 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 4, import: 3, structural_boundaries: 2, state_mutation: 2
- `linuxdoom-1.10/i_main.c` (C) | Magnitude: 7.6 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 5, state_mutation: 3, import: 3, api: 2
- `linuxdoom-1.10/m_cheat.c` (C) | Magnitude: 101.94 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 70, pointers: 24, indent_spaces: 24, branch: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `linuxdoom-1.10/p_doors.c` (C) | Magnitude: 706.0 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 368, pointers: 231, indent_tabs: 190, branch: 178
- `linuxdoom-1.10/r_main.c` (C) | Magnitude: 770.02 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 450, indent_spaces: 256, api: 145, indent_tabs: 114
- `linuxdoom-1.10/d_net.h` (C) | Magnitude: 47.96 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 30, indent_spaces: 26, structural_boundaries: 12, macros: 7
- `linuxdoom-1.10/am_map.c` (C) | Magnitude: 64.1 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 68, indent_spaces: 48, encapsulation: 43, state_mutation: 28
- `linuxdoom-1.10/r_plane.h` (C) | Magnitude: 40.8 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 25, structural_boundaries: 10, indent_spaces: 10, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sndserv/soundst.h` (C) | Magnitude: 32.7 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 17, macros: 14, indent_spaces: 11, structural_boundaries: 7
- `linuxdoom-1.10/d_event.h` (C) | Magnitude: 39.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, api: 12, state_mutation: 11, structural_boundaries: 8
- `linuxdoom-1.10/w_wad.h` (C) | Magnitude: 39.72 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 24, structural_boundaries: 14, indent_spaces: 10, args: 8
- `linuxdoom-1.10/g_game.h` (C) | Magnitude: 33.46 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, api: 18, args: 15, import: 2
- `linuxdoom-1.10/st_stuff.h` (C) | Magnitude: 23.5 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, api: 8, macros: 5, indent_spaces: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `linuxdoom-1.10/p_mobj.h` -> **Severity: 0.446** (Bridge: 0.0045 * Flux: 99.6731%)
- `linuxdoom-1.10/d_player.h` -> **Severity: 0.3** (Bridge: 0.01 * Flux: 29.9133%)
- `linuxdoom-1.10/d_event.h` -> **Severity: 0.06** (Bridge: 0.0006 * Flux: 99.8528%)
- `linuxdoom-1.10/d_net.h` -> **Severity: 0.026** (Bridge: 0.0007 * Flux: 35.1299%)
- `linuxdoom-1.10/wi_stuff.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 68.9316%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `linuxdoom-1.10/d_event.h` -> **Severity: 2.612** (Embedded: 0.1712 * Error Risk: 15.2609%)
- `linuxdoom-1.10/doomdef.h` -> **Severity: 2.114** (Embedded: 0.3202 * Error Risk: 6.6029%)
- `linuxdoom-1.10/p_mobj.h` -> **Severity: 1.882** (Embedded: 0.1327 * Error Risk: 14.1851%)
- `linuxdoom-1.10/d_player.h` -> **Severity: 1.246** (Embedded: 0.1796 * Error Risk: 6.9386%)
- `linuxdoom-1.10/d_net.h` -> **Severity: 1.09** (Embedded: 0.1399 * Error Risk: 7.7946%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `linuxdoom-1.10/doomtype.h` -> **Severity: 5856.503** (Blast Radius: 80.472 * Doc Risk: 72.7769%)
- `linuxdoom-1.10/d_event.h` -> **Severity: 3116.925** (Blast Radius: 31.27 * Doc Risk: 99.6778%)
- `linuxdoom-1.10/d_player.h` -> **Severity: 3048.1** (Blast Radius: 30.481 * Doc Risk: 100.0%)
- `linuxdoom-1.10/r_data.h` -> **Severity: 2503.062** (Blast Radius: 25.031 * Doc Risk: 99.9985%)
- `linuxdoom-1.10/doomstat.h` -> **Severity: 2147.8** (Blast Radius: 21.478 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
