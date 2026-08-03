# ARCHITECTURAL_BRIEF: normal_rp2040_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_rp2040_doom` |
| **Timestamp** | `2026-08-03T19:06:06.499159+00:00` |
| **Scan Duration** | `3.47s` |
| **Git Branch** | `rp2` |
| **Git Commit** | `29a453c980918a03e40fc8b69b024e7a3bdb5dc2` |
| **Git Remote** | `https://github.com/kilograham/rp2040-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 628 malicious artifacts.

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
| Total Artifacts | 779 |
| Analyzed Artifacts (Scanned) | 669 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 110 |
| Total LOC | 138510 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 85.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4739 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1264 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3146 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 42 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 574 | 127602 | 85.8% |
| CPP | 19 | 8062 | 2.8% |
| PLAINTEXT | 17 | 0 | 2.5% |
| MARKDOWN | 15 | 0 | 2.2% |
| M4 | 13 | 374 | 1.9% |
| OBJECTIVE-C | 8 | 839 | 1.2% |
| MAKEFILE | 8 | 632 | 1.2% |
| XML | 7 | 0 | 1.0% |
| SHELL | 3 | 52 | 0.4% |
| PYTHON | 3 | 241 | 0.4% |
| ASSEMBLY | 2 | 708 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.852`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 416 | 62.2% |
| file_cluster_13 | 209 | 31.2% |
| file_cluster_11 | 5 | 0.7% |
| file_cluster_9 | 4 | 0.6% |
| file_cluster_12 | 2 | 0.3% |
| file_cluster_17 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 4.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 110*

**Composition by Extension & Reason:**
- `no_extension`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 2452 LOC)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.am`: 12x Excluded (Unsupported Extension: '.am')
- `.c`: 2x Excluded (Embedded Hex Payload: 16384 hex tokens in 2737 LOC), 1x Excluded (Embedded Hex Payload: 2055 hex tokens in 957 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4694 LOC)
- `.template`: 10x Excluded (Unsupported Extension: '.template')
- `.cmake`: 7x Excluded (Unsupported Extension: '.cmake')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1073 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3621 LOC)
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.man`: 2x Excluded (Unsupported Extension: '.man')
- `.in`: 1x Excluded (Machine-Generated Source Code Signature: 29 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.icns`: 2x Excluded (Unsupported Extension: '.icns')
- `.nib`: 2x Excluded (Unsupported Extension: '.nib')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cin`: 1x Excluded (Unsupported Extension: '.cin')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 96.9 | 37.2 | 30.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 30.0 | 14.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.4 | 9.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 31.8 | 2.4 | 80.0 |
| API Exposure | 0.0 | 19.3 | 9.2 | 9.8 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.4 | 99.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.9 | 3.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 74.2 | 96.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 48.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.4 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/adpcm-xq/adpcm-xq.c` (Hits: 33)
- `pkg/osx/GNUmakefile` (Hits: 23)
- `src/midifile.c` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i_system.h** (`src/i_system.h`) — 150 inbound connections
2. **doomtype.h** (`src/doomtype.h`) — 125 inbound connections
3. **m_misc.h** (`src/m_misc.h`) — 112 inbound connections
4. **z_zone.h** (`src/z_zone.h`) — 97 inbound connections
5. **deh_main.h** (`src/deh_main.h`) — 71 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`src/strife/d_main.c`) — 47 outbound dependencies
2. **d_main.c** (`src/doom/d_main.c`) — 46 outbound dependencies
3. **g_game.c** (`src/doom/g_game.c`) — 39 outbound dependencies
4. **i_video.c** (`src/pico/i_video.c`) — 38 outbound dependencies
5. **g_game.c** (`src/strife/g_game.c`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convert_textures` (@ `src/whd_gen/whd_gen.cpp`) -> Impact: **6282.5** | LOC: 1246
- `get_patch_decoder` (@ `src/pd_render.cpp`) -> Impact: **3196.6** | LOC: 696
- `push_down_x_guts` (@ `src/pd_render.cpp`) -> Impact: **2553.5** | LOC: 875
  * *Intent:* // =========================================================== // LETS LOOK AT COLUMNS AGAIN // SORT COL // 19: texture_mid - need markers for fuzzy, ...
- `P_XYMovement` (@ `src/hexen/p_mobj.c`) -> Impact: **1983.2** | LOC: 1024
  * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMovement // //------------------------------------------...
- `P_InitSwitchList` (@ `src/strife/p_switch.c`) -> Impact: **1700.1** | LOC: 838
  * *Intent:* // // P_InitSwitchList // Only called at game initialization. //
- `P_ExecuteLineSpecial` (@ `src/hexen/p_spec.c`) -> Impact: **1628.4** | LOC: 332
- `R_DrawVisSprite` (@ `src/strife/r_things.c`) -> Impact: **1329.2** | LOC: 637
  * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. //
- `P_MovePlayer` (@ `src/strife/p_user.c`) -> Impact: **1240.2** | LOC: 723
- `P_LookForPlayers` (@ `src/strife/p_enemy.c`) -> Impact: **1131.5** | LOC: 929
- `P_MobjThinker` (@ `src/strife/p_mobj.c`) -> Impact: **1122.6** | LOC: 629

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `EV_VerticalDoor` (@ `src/doom/p_doors.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `SpechitOverrun` (@ `src/doom/p_map.c`) -> **O(2^N) [Recursive]**
- `saveg_read8` (@ `src/doom/p_saveg.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Endian-safe integer read/write functions
- `R_Subsector` (@ `src/doom/r_bsp.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // R_Subsector // Determine floor/ceiling planes. // Add sprites of things in sector. // Draw one or more line segments. //
- `R_RenderSegLoop` (@ `src/doom/r_segs.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif #define EPSILON 1
- `P_GiveAmmo` (@ `src/heretic/p_inter.c`) -> **O(2^N) [Recursive]**
- `P_XYMovement` (@ `src/heretic/p_mobj.c`) -> **O(2^N) [Recursive]**
  * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMovement // //------------------------------------------...
- `R_Subsector` (@ `src/heretic/r_bsp.c`) -> **O(2^N) [Recursive]**
- `R_DrawPlanes` (@ `src/heretic/r_plane.c`) -> **O(2^N) [Recursive]**
- `R_FindPlane` (@ `src/heretic/r_plane.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `convert_textures` (@ `src/whd_gen/whd_gen.cpp`) -> DB Complexity: **452**
- `push_down_x_guts` (@ `src/pd_render.cpp`) -> DB Complexity: **413**
  * *Intent:* // =========================================================== // LETS LOOK AT COLUMNS AGAIN // SORT COL // 19: texture_mid - need markers for fuzzy, ...
- `get_patch_decoder` (@ `src/pd_render.cpp`) -> DB Complexity: **331**
- `deflateDynamic` (@ `src/whd_gen/lodepng.cpp`) -> DB Complexity: **203**
- `P_XYMovement` (@ `src/hexen/p_mobj.c`) -> DB Complexity: **195**
  * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMovement // //------------------------------------------...
- `draw_vpatch` (@ `src/pico/i_video.c`) -> DB Complexity: **171**
- `R_DrawVisSprite` (@ `src/strife/r_things.c`) -> DB Complexity: **167**
  * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. //
- `V_DrawPatchList` (@ `src/v_video.c`) -> DB Complexity: **147**
  * *Intent:* #pragma GCC push_options #if PICO_ON_DEVICE #pragma GCC optimize("O3") #endif
- `P_MovePlayer` (@ `src/strife/p_user.c`) -> DB Complexity: **144**
- `A_Lower` (@ `src/hexen/p_pspr.c`) -> DB Complexity: **138**
  * *Intent:* //--------------------------------------------------------------------------- // // PROC A_ReFire // // The player can re fire the weapon without lowe...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/hexen` | 59 | 40860.58 | 52.62% | 24.72% |
| `src/strife` | 104 | 36010.58 | 35.69% | 24.68% |
| `src` | 145 | 31212.66 | 35.53% | 26.58% |
| `src/doom` | 103 | 30950.0 | 36.5% | 23.89% |
| `src/heretic` | 62 | 30944.58 | 46.13% | 25.22% |
| `src/whd_gen` | 17 | 15879.58 | 43.29% | 39.29% |
| `opl` | 23 | 7670.08 | 35.15% | 23.95% |
| `src/pico` | 16 | 4898.76 | 40.72% | 27.29% |
| `textscreen` | 45 | 4386.52 | 26.3% | 21.67% |
| `src/adpcm-xq` | 5 | 2878.08 | 16.62% | 8.2% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cup.sh` -> **100.0%** Exposure
- `up.sh` -> **100.0%** Exposure
- `src/i_cdmus.c` -> **100.0%** Exposure
- `src/m_fixed.c` -> **100.0%** Exposure
- `src/pico/i_timer.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `opl/emu8950.c` -> **100.0%** Exposure
- `opl/opl3.c` -> **100.0%** Exposure
- `opl/opl_pico.c` -> **100.0%** Exposure
- `opl/opl_queue.c` -> **100.0%** Exposure
- `opl/opl_sdl.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/hexen/p_enemy.c` -> **59** Orphaned Functions | **0** Duplicates
- `src/heretic/p_enemy.c` -> **48** Orphaned Functions | **0** Duplicates
- `src/heretic/p_pspr.c` -> **45** Orphaned Functions | **0** Duplicates
- `src/hexen/p_setup.c` -> **29** Orphaned Functions | **0** Duplicates
- `src/strife/m_menu.c` -> **26** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`opl/emu8950.c`** -> AI Confidence: **99.48%**
2. **`src/doom/d_main.c`** -> AI Confidence: **99.48%**
3. **`src/doom/p_ceilng.c`** -> AI Confidence: **99.48%**
4. **`src/doom/p_doors.c`** -> AI Confidence: **99.48%**
5. **`src/doom/p_floor.c`** -> AI Confidence: **99.48%**
6. **`src/doom/p_inter.c`** -> AI Confidence: **99.48%**
7. **`src/doom/p_mobj.c`** -> AI Confidence: **99.48%**
8. **`src/doom/p_plats.c`** -> AI Confidence: **99.48%**
9. **`src/doom/p_setup.c`** -> AI Confidence: **99.48%**
10. **`src/doom/p_spec.c`** -> AI Confidence: **99.48%**
11. **`src/doom/p_switch.c`** -> AI Confidence: **99.48%**
12. **`src/doom/r_plane.c`** -> AI Confidence: **99.48%**
13. **`src/doom/r_segs.c`** -> AI Confidence: **99.48%**
14. **`src/doom/r_things.c`** -> AI Confidence: **99.48%**
15. **`src/doom/st_lib.c`** -> AI Confidence: **99.48%**
16. **`src/heretic/p_saveg.c`** -> AI Confidence: **99.48%**
17. **`src/i_main.c`** -> AI Confidence: **99.48%**
18. **`src/pico/i_input.c`** -> AI Confidence: **99.48%**
19. **`src/pico/i_video.c`** -> AI Confidence: **99.48%**
20. **`src/strife/p_ceilng.c`** -> AI Confidence: **99.48%**
21. **`src/strife/p_doors.c`** -> AI Confidence: **99.48%**
22. **`src/strife/p_floor.c`** -> AI Confidence: **99.48%**
23. **`src/strife/p_inter.c`** -> AI Confidence: **99.48%**
24. **`src/strife/p_plats.c`** -> AI Confidence: **99.48%**
25. **`src/strife/p_setup.c`** -> AI Confidence: **99.48%**
26. **`src/strife/p_switch.c`** -> AI Confidence: **99.48%**
27. **`src/strife/p_user.c`** -> AI Confidence: **99.48%**
28. **`src/strife/r_plane.c`** -> AI Confidence: **99.48%**
29. **`src/strife/r_segs.c`** -> AI Confidence: **99.48%**
30. **`src/strife/r_things.c`** -> AI Confidence: **99.48%**
31. **`src/v_video.c`** -> AI Confidence: **99.48%**
32. **`src/w_file_memory.c`** -> AI Confidence: **99.48%**
33. **`src/pd_render.cpp`** -> AI Confidence: **99.48%**
34. **`pkg/osx/Execute.m`** -> AI Confidence: **99.48%**
35. **`src/doom/f_finale.c`** -> AI Confidence: **99.39%**
36. **`src/doom/p_saveg.c`** -> AI Confidence: **99.39%**
37. **`src/doom/r_draw.c`** -> AI Confidence: **99.39%**
38. **`src/doom/s_sound.c`** -> AI Confidence: **99.39%**
39. **`src/doom/st_stuff.c`** -> AI Confidence: **99.39%**
40. **`src/doom/statdump.c`** -> AI Confidence: **99.39%**
41. **`src/doom/wi_stuff.c`** -> AI Confidence: **99.39%**
42. **`src/heretic/am_map.c`** -> AI Confidence: **99.39%**
43. **`src/heretic/p_setup.c`** -> AI Confidence: **99.39%**
44. **`src/heretic/r_things.c`** -> AI Confidence: **99.39%**
45. **`src/hexen/am_map.c`** -> AI Confidence: **99.39%**
46. **`src/hexen/s_sound.c`** -> AI Confidence: **99.39%**
47. **`src/m_argv.c`** -> AI Confidence: **99.39%**
48. **`src/pico/i_system.c`** -> AI Confidence: **99.39%**
49. **`src/pico/piconet.c`** -> AI Confidence: **99.39%**
50. **`src/strife/f_finale.c`** -> AI Confidence: **99.39%**
51. **`src/strife/g_game.c`** -> AI Confidence: **99.39%**
52. **`src/strife/p_dialog.c`** -> AI Confidence: **99.39%**
53. **`src/strife/p_enemy.c`** -> AI Confidence: **99.39%**
54. **`src/strife/p_mobj.c`** -> AI Confidence: **99.39%**
55. **`src/strife/p_pspr.c`** -> AI Confidence: **99.39%**
56. **`src/strife/p_spec.c`** -> AI Confidence: **99.39%**
57. **`src/strife/r_draw.c`** -> AI Confidence: **99.39%**
58. **`src/strife/st_lib.c`** -> AI Confidence: **99.39%**
59. **`src/strife/wi_stuff.c`** -> AI Confidence: **99.39%**
60. **`textscreen/txt_fileselect.c`** -> AI Confidence: **99.39%**
61. **`textscreen/txt_label.c`** -> AI Confidence: **99.39%**
62. **`textscreen/txt_table.c`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `man/simplecpp` -> **100.0%** Exposure
- `pkg/win32/cp-with-libs` -> **100.0%** Exposure
- `opl/emu8950.c` -> **20.0%** Exposure
- `opl/examples/droplay.c` -> **20.0%** Exposure
- `opl/opl3.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `man/simplecpp` -> **100.0%** Exposure
- `pcsound/pcsound_bsd.c` -> **100.0%** Exposure
- `textscreen/txt_window.c` -> **100.0%** Exposure
- `pkg/osx/GNUmakefile` -> **100.0%** Exposure
- `src/setup/execute.c` -> **87.8043%** Exposure
### Raw Memory Manipulation
- `opl/emu8950.c` -> **10.0%** Exposure
- `src/midifile.c` -> **10.0%** Exposure
- `src/strife/p_saveg.c` -> **10.0%** Exposure
- `src/tiny_huff.h` -> **10.0%** Exposure
- `textscreen/txt_spinctrl.c` -> **10.0%** Exposure
### Algorithmic DoS Exposure
- `pkg/osx/cp-with-libs` -> **100.0%** Exposure
- `pkg/win32/cp-with-libs` -> **100.0%** Exposure
- `midiproc/main.c` -> **100.0%** Exposure
- `opl/emu8950.c` -> **100.0%** Exposure
- `opl/examples/droplay.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3734` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/doom/r_data_whd.c` (C) -> Cumulative Risk: **812.21**
- **Archetype:** `file_cluster_11` (Distance: 19.082 IQR)
- **Magnitude:** 339.1 | **LOC:** 424 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9949%)
- **Heaviest Functions:** `lookup_texture` (Impact: 35.8), `R_PrecacheLevel` (Impact: 26.3), `R_InitColormaps` (Impact: 18.5)

### 2. `textscreen/txt_window.c` (C) -> Cumulative Risk: **796.95**
- **Archetype:** `file_cluster_8` (Distance: 12.766 IQR)
- **Magnitude:** 474.42 | **LOC:** 597 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `MouseButtonPress` (Impact: 49.0), `CalcWindowPosition` (Impact: 31.4), `TXT_WindowKeyPress` (Impact: 20.1)

### 3. `src/doom/p_tick.c` (C) -> Cumulative Risk: **787.29**
- **Archetype:** `file_cluster_13` (Distance: 14.524 IQR)
- **Magnitude:** 380.48 | **LOC:** 363 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.941%)
- **Heaviest Functions:** `P_RunThinkers` (Impact: 142.9), `Z_ThinkFree` (Impact: 27.9), `P_Ticker` (Impact: 15.3)

### 4. `src/whd_gen/huffman.h` (CPP) -> Cumulative Risk: **786.03**
- **Archetype:** `file_cluster_11` (Distance: 14.48 IQR)
- **Magnitude:** 1517.56 | **LOC:** 677 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.048%)
- **Heaviest Functions:** `output_min_max` (Impact: 244.3), `huffman_encoding` (Impact: 128.9), `decode_min_max8` (Impact: 118.2)

### 5. `src/pico/i_system.c` (C) -> Cumulative Risk: **784.59**
- **Archetype:** `file_cluster_13` (Distance: 13.656 IQR)
- **Magnitude:** 1142.42 | **LOC:** 664 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.2422%)
- **Heaviest Functions:** `handle_exit_key_down` (Impact: 388.7), `I_GetMemoryValue` (Impact: 122.8), `AutoAllocMemory` (Impact: 79.8)

### 6. `src/doom/r_draw.c` (C) -> Cumulative Risk: **784.34**
- **Archetype:** `file_cluster_13` (Distance: 14.455 IQR)
- **Magnitude:** 1206.1 | **LOC:** 988 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9055%)
- **Heaviest Functions:** `R_DrawFuzzColumn` (Impact: 73.4), `R_FillBackScreen` (Impact: 69.0), `R_DrawSpan` (Impact: 59.1)

### 7. `src/strife/p_saveg.c` (C) -> Cumulative Risk: **783.61**
- **Archetype:** `file_cluster_9` (Distance: 22.373 IQR)
- **Magnitude:** 1180.1 | **LOC:** 2209 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Dead Code (97.8723%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 129.3), `P_UnArchiveSpecials` (Impact: 124.9), `saveg_read8` (Impact: 40.4)

### 8. `src/hexen/p_setup.c` (C) -> Cumulative Risk: **778.11**
- **Archetype:** `file_cluster_8` (Distance: 13.56 IQR)
- **Magnitude:** 819.14 | **LOC:** 1232 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9874%)
- **Heaviest Functions:** `InitMapInfo` (Impact: 184.7), `P_LoadNodes` (Impact: 18.7), `P_LoadSegs` (Impact: 15.7)

### 9. `src/z_zone.c` (C) -> Cumulative Risk: **775.63**
- **Archetype:** `file_cluster_13` (Distance: 14.183 IQR)
- **Magnitude:** 585.66 | **LOC:** 648 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.8752%)
- **Heaviest Functions:** `Z_Free` (Impact: 71.5), `Z_DumpHeap` (Impact: 64.4), `ScanForBlock` (Impact: 50.2)

### 10. `src/pico/i_picosound.c` (C) -> Cumulative Risk: **768.59**
- **Archetype:** `file_cluster_13` (Distance: 13.987 IQR)
- **Magnitude:** 580.2 | **LOC:** 492 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8902%)
- **Heaviest Functions:** `I_Pico_UpdateSound` (Impact: 122.7), `adpcm_decode_block_s8` (Impact: 39.2), `I_Pico_InitSound` (Impact: 7.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/whd_gen/whd_gen.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.793 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.148 IQR)
- **Top Global Matches:** file_cluster_8: 14.793, file_cluster_11: 14.798, file_cluster_13: 14.877
- **Magnitude:** 9750.34 | **LOC:** 5332 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 452
- **Risk Profile:** Cognitive Load (94.2305%), Tech Debt (21.0791%)
**Top Internal Functions/Classes:**
  * `convert_textures` (Impact: 6282.5 | O(2^N) | DB: 452)
  * `output_min_max_best_c3` (Impact: 659.4 | O(N^6) | DB: 130)
  * `output_min_max_c3` (Impact: 272.7 | O(N^6) | DB: 40)
  * `to_merged_posts` (Impact: 119.8 | O(N^5) | DB: 28)
  * `image_to_patch` (Impact: 66.9 | O(N^4) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 169`, `args: 135`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 2178`, `dead_code: 19`, `planned_debt: 12`, `fragile_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `import: 26`
* *Defense:* `safety: 34`, `immutability_locks: 71`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` statsomizer.h, vector, image_decoder.h, normal.h, functional, memory, compress_mus.h, huff_sink.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pd_render.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.603 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_11: 16.603, file_cluster_6: 16.828, file_cluster_0: 16.833
- **Magnitude:** 8055.36 | **LOC:** 3116 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 413
- **Risk Profile:** Cognitive Load (96.9411%), Tech Debt (19.6321%)
**Top Internal Functions/Classes:**
  * `get_patch_decoder` (Impact: 3196.6 | O(2^N) | DB: 331)
  * `push_down_x_guts` (Impact: 2553.5 | O(2^N) | DB: 413)
    * *Intent:* // =========================================================== // LETS LOOK AT COLUMNS AGAIN // SORT...
  * `dump_column_list` (Impact: 20.8 | O(N^3) | DB: 7)
    * *Intent:* #define UP_SHIFT(x) ((x) << SHIFT) // only used for texturemid
  * `alloc_pd_column` (Impact: 14.6 | O(N^3) | DB: 10)
    * *Intent:* #if PICO_ON_DEVICE //extern fixed_t FastFixedMul(fixed_t a, fixed_t b); #define FastFixedMul FixedMu...
  * `patch_offset_or_inverse_slot` (Impact: 8.3 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 89`, `args: 50`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 2218`, `dead_code: 27`, `planned_debt: 23`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 56`, `sync_locks: 2`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` gpio.h, r_local.h, image_decoder.h, i_picosound.h, doomstat.h, interp.h, divider.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.831 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.411 IQR)
- **Top Global Matches:** file_cluster_8: 13.831, file_cluster_13: 14.156, file_cluster_7: 14.203
- **Magnitude:** 3259.48 | **LOC:** 5444 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (92.2988%), Tech Debt (56.5202%)
**Top Internal Functions/Classes:**
  * `P_NewChaseDir` (Impact: 221.8 | O(2^N) | DB: 27)
  * `A_Explode` (Impact: 192.8 | O(N^4) | DB: 40)
  * `A_Scream` (Impact: 137.1 | O(N^6) | DB: 14)
  * `A_MinotaurLook` (Impact: 98.8 | O(N^4) | DB: 17)
    * *Intent:* //---------------------------------------------------------------------------- //
  * `P_LookForPlayers` (Impact: 73.2 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 214`, `args: 1`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1286`, `dead_code: 4`, `orphaned_logic: 59`
* *Architecture:* `api: 298`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` s_sound.h, m_random.h, i_system.h, i_swap.h, h2def.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_spec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.094 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.588 IQR)
- **Top Global Matches:** file_cluster_8: 13.094, file_cluster_13: 13.403, file_cluster_7: 13.481
- **Magnitude:** 3147.66 | **LOC:** 1205 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (48.4137%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_ExecuteLineSpecial` (Impact: 1628.4 | O(N^6) | DB: 82)
  * `P_PlayerInSpecialSector` (Impact: 352.6 | O(2^N) | DB: 4)
    * *Intent:* //============================================================================ // // P_ActivateLine ...
  * `P_SpawnSpecials` (Impact: 231.4 | O(2^N) | DB: 22)
  * `P_UpdateSpecials` (Impact: 56.1 | O(N^6) | DB: 6)
  * `EV_LineSearchForPuzzleItem` (Impact: 40.8 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 80`, `args: 8`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 549`, `orphaned_logic: 11`
* *Architecture:* `api: 103`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` s_sound.h, i_system.h, h2def.h, p_local.h, m_misc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.458 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.531 IQR)
- **Top Global Matches:** file_cluster_8: 13.458, file_cluster_13: 13.705, file_cluster_7: 13.808
- **Magnitude:** 2966.74 | **LOC:** 2471 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 195
- **Risk Profile:** Cognitive Load (94.7988%), Tech Debt (12.2645%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 1983.2 | O(2^N) | DB: 195)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_FloorBounceMissile` (Impact: 108.1 | O(N^5) | DB: 5)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_FloorBou...
  * `P_SeekerMissile` (Impact: 32.6 | O(N^5) | DB: 13)
    * *Intent:* //---------------------------------------------------------------------------- // // // The missile ...
  * `P_ExplodeMissile` (Impact: 28.8 | O(N^4) | DB: 4)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_ExplodeM...
  * `P_FaceMobj` (Impact: 15.8 | O(N^3) | DB: 8)
    * *Intent:* //---------------------------------------------------------------------------- // // FUNC P_FaceMobj...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 79`, `args: 1`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 634`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 131`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sounds.h, s_sound.h, m_random.h, i_system.h, h2def.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/emu8950.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.944 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.679 IQR)
- **Top Global Matches:** file_cluster_11: 14.944, file_cluster_8: 14.965, file_cluster_13: 15.06
- **Magnitude:** 2911.86 | **LOC:** 2028 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (78.2299%), Tech Debt (33.2304%)
**Top Internal Functions/Classes:**
  * `OPL_writeReg` (Impact: 195.8 | O(N^6) | DB: 35)
    * *Intent:* #if DUMPO
  * `OPL_calc_buffer_linear` (Impact: 153.2 | O(N^6) | DB: 36)
  * `commit_slot_update` (Impact: 60.9 | O(N^4) | DB: 21)
  * `makeSinTable` (Impact: 58.7 | O(N^3) | DB: 19)
  * `calc_envelope` (Impact: 54.5 | O(N^4) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 107`, `args: 8`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1567`, `dead_code: 7`, `planned_debt: 17`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 218`, `import: 7`
* *Defense:* `safety: 10`, `doc: 5`, `test: 7`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, stdio.h, gpio.h, emu8950.h, string.h, math.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.012 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.352 IQR)
- **Top Global Matches:** file_cluster_8: 14.012, file_cluster_13: 14.064, file_cluster_11: 14.228
- **Magnitude:** 2516.18 | **LOC:** 1552 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 111
- **Risk Profile:** Cognitive Load (92.7321%), Tech Debt (13.0866%)
**Top Internal Functions/Classes:**
  * `DrawWuLine` (Impact: 935.0 | O(N^6) | DB: 111)
  * `AM_Responder` (Impact: 228.7 | O(N^6) | DB: 45)
  * `AM_drawFline` (Impact: 105.5 | O(N^6) | DB: 19)
  * `AM_clipMline` (Impact: 75.0 | O(N^3) | DB: 44)
  * `AM_initVariables` (Impact: 34.7 | O(N^4) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 90`, `args: 23`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 869`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 127`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stdio.h, i_timer.h, m_controls.h, am_map.h, v_video.h, i_swap.h, am_data.h, h2def.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.159 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.441 IQR)
- **Top Global Matches:** file_cluster_8: 14.159, file_cluster_13: 14.18, file_cluster_11: 14.313
- **Magnitude:** 2440.66 | **LOC:** 1543 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (75.3958%), Tech Debt (13.237%)
**Top Internal Functions/Classes:**
  * `DrawWuLine` (Impact: 890.9 | O(N^6) | DB: 86)
    * *Intent:* // memcpy(I_VideoBuffer, maplump, finit_width*finit_height); // memset(fb, color, f_w*f_h);
  * `AM_Responder` (Impact: 224.9 | O(N^6) | DB: 41)
  * `AM_drawFline` (Impact: 105.6 | O(N^6) | DB: 21)
  * `AM_clipMline` (Impact: 75.0 | O(N^3) | DB: 44)
  * `AM_initVariables` (Impact: 53.2 | O(N^4) | DB: 32)
    * *Intent:* // Calculates the slope and slope according to the x-axis of a line // segment in map coordinates (w...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 83`, `args: 21`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 831`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 119`, `import: 11`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` i_timer.h, stdio.h, m_controls.h, am_map.h, v_video.h, deh_str.h, am_data.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/whd_gen/lodepng.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.989 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.232 IQR)
- **Top Global Matches:** file_cluster_13: 15.989, file_cluster_7: 15.999, file_cluster_8: 15.999
- **Magnitude:** 2419.82 | **LOC:** 6256 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 203
- **Risk Profile:** Cognitive Load (47.7827%), Tech Debt (35.8099%)
**Top Internal Functions/Classes:**
  * `deflateDynamic` (Impact: 407.4 | O(N^6) | DB: 203)
  * `lodepng_huffman_code_lengths` (Impact: 366.7 | O(N^6) | DB: 59)
  * `encodeLZ77` (Impact: 246.7 | O(N^6) | DB: 80)
    * *Intent:* #endif /*LODEPNG_COMPILE_DECODER*/ /* //////////////////////////////////////////////////////////////...
  * `hash_init` (Impact: 22.1 | O(N^1) | DB: 21)
    * *Intent:* *outsize = (size_t)size;
  * `writeLZ77data` (Impact: 11.8 | O(N^6) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 71`, `args: 48`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1282`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 3`, `import: 4`
* *Defense:* `safety: 2`, `doc: 289`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lodepng.h, limits.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.805 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.368 IQR)
- **Top Global Matches:** file_cluster_13: 14.805, file_cluster_11: 14.933, file_cluster_8: 14.949
- **Magnitude:** 2233.5 | **LOC:** 1068 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 167
- **Risk Profile:** Cognitive Load (91.2369%), Tech Debt (9.4167%)
**Top Internal Functions/Classes:**
  * `R_DrawVisSprite` (Impact: 1329.2 | O(2^N) | DB: 167)
    * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. //
  * `R_InitSpriteDefs` (Impact: 49.1 | O(N^1) | DB: 26)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_InstallSpriteLump` (Impact: 47.4 | O(2^N) | DB: 13)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
  * `R_DrawMaskedColumn` (Impact: 19.8 | O(N^4) | DB: 12)
    * *Intent:* // // R_DrawMaskedColumn // // villsa [STRIFE] new baseclip argument //
  * `R_InitSprites` (Impact: 4.5 | O(N^1) | DB: 3)
    * *Intent:* // // R_InitSprites // Called at program start. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 39`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 637`, `dead_code: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 128`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, i_system.h, deh_main.h, i_swap.h, doomstat.h, r_local.h, stdlib.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.264 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_13: 15.264, file_cluster_11: 15.279, file_cluster_0: 15.363
- **Magnitude:** 2002.92 | **LOC:** 1175 | **CtrlFlow:** 84.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (77.0486%), Tech Debt (17.3964%)
**Top Internal Functions/Classes:**
  * `R_InitSpriteDefs` (Impact: 173.3 | O(N^6) | DB: 33)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawMaskedColumn` (Impact: 162.6 | O(N^6) | DB: 60)
  * `R_ProjectSprite` (Impact: 152.8 | O(2^N) | DB: 47)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_DrawSprite` (Impact: 116.1 | O(N^5) | DB: 33)
    * *Intent:* #endif // // R_DrawSprite //
  * `R_InstallSpriteLump` (Impact: 99.0 | O(2^N) | DB: 15)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 44`, `args: 8`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 871`, `dead_code: 9`, `planned_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 144`, `import: 13`
* *Defense:* `safety: 8`, `test: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` stdio.h, picodoom.h, i_system.h, deh_main.h, v_patch.h, i_swap.h, doomstat.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/sb_bar.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.93 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.44 IQR)
- **Top Global Matches:** file_cluster_8: 12.93, file_cluster_13: 13.304, file_cluster_7: 13.33
- **Magnitude:** 1954.12 | **LOC:** 2007 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (64.9707%), Tech Debt (12.1758%)
**Top Internal Functions/Classes:**
  * `DrawMainBar` (Impact: 222.9 | O(N^6) | DB: 66)
    * *Intent:* //========================================================================== //
  * `DrawAnimatedIcons` (Impact: 118.2 | O(N^6) | DB: 15)
  * `DrawFullScreenStuff` (Impact: 92.8 | O(N^6) | DB: 8)
    * *Intent:* //========================================================================== // // DrawWeaponPieces ...
  * `DrawKeyBar` (Impact: 67.3 | O(N^6) | DB: 11)
  * `SB_Drawer` (Impact: 58.3 | O(N^5) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 163`, `args: 30`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 835`, `orphaned_logic: 7`
* *Architecture:* `api: 125`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` m_cheat.h, m_bbox.h, s_sound.h, v_video.h, i_swap.h, h2def.h, p_local.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_switch.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.665 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.797 IQR)
- **Top Global Matches:** file_cluster_8: 11.665, file_cluster_13: 11.928, file_cluster_11: 12.136
- **Magnitude:** 1897.98 | **LOC:** 1080 | **CtrlFlow:** 94.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (67.5873%), Tech Debt (72.2764%)
**Top Internal Functions/Classes:**
  * `P_InitSwitchList` (Impact: 1700.1 | O(N^6) | DB: 53)
    * *Intent:* // // P_InitSwitchList // Only called at game initialization. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 20`, `args: 1`, `func_start: 4`
* *Risk/State:* `state_mutation: 156`, `planned_debt: 20`, `fragile_debt: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 28`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stdio.h, sounds.h, m_bbox.h, s_sound.h, m_random.h, i_system.h, deh_main.h, r_state.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.247 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.834 IQR)
- **Top Global Matches:** file_cluster_13: 14.247, file_cluster_8: 14.347, file_cluster_11: 14.438
- **Magnitude:** 1886.04 | **LOC:** 1362 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 133
- **Risk Profile:** Cognitive Load (74.3251%), Tech Debt (24.9478%)
**Top Internal Functions/Classes:**
  * `P_MobjThinker` (Impact: 1122.6 | O(2^N) | DB: 133)
  * `P_XYMovement` (Impact: 154.8 | O(N^5) | DB: 27)
    * *Intent:* // // P_XYMovement // // [STRIFE] Modifications for: // * No SKULLFLY logic (replaced by BOUNCE flag...
  * `P_SetMobjState` (Impact: 6.6 | O(N^1) | DB: 7)
  * `P_ExplodeMissile` (Impact: 3.6 | O(N^2) | DB: 4)
    * *Intent:* // // P_ExplodeMissile // // [STRIFE] Removed randomization of deathstate tics //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 47`, `args: 2`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 497`, `dead_code: 4`, `fragile_debt: 5`
* *Architecture:* `api: 90`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stdio.h, sounds.h, s_sound.h, m_random.h, i_system.h, d_main.h, hu_stuff.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.902 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.675 IQR)
- **Top Global Matches:** file_cluster_8: 13.902, file_cluster_13: 13.915, file_cluster_11: 14.079
- **Magnitude:** 1885.06 | **LOC:** 2825 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (74.9401%), Tech Debt (70.3402%)
**Top Internal Functions/Classes:**
  * `P_UnArchiveWorld` (Impact: 130.4 | O(N^4) | DB: 40)
  * `P_SaveGameWriteFlashSlot` (Impact: 105.8 | O(N^6) | DB: 35)
  * `P_ArchiveWorld` (Impact: 105.2 | O(N^4) | DB: 30)
    * *Intent:* #endif #endif #if !LOAD_COMPRESSED // int tics;
  * `P_ArchiveSpecials` (Impact: 99.5 | O(N^4) | DB: 4)
    * *Intent:* // struct mobj_s* tracer;
  * `saveg_read8` (Impact: 80.4 | O(2^N) | DB: 5)
    * *Intent:* // Endian-safe integer read/write functions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 104`, `args: 23`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 721`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 2`, `api: 154`, `import: 18`
* *Defense:* `safety: 8`, `test: 3`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` stdio.h, timer.h, i_system.h, deh_main.h, w_wad.h, r_state.h, p_saveg.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_user.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.905 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.656 IQR)
- **Top Global Matches:** file_cluster_13: 13.905, file_cluster_8: 13.981, file_cluster_11: 14.189
- **Magnitude:** 1872.0 | **LOC:** 922 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 144
- **Risk Profile:** Cognitive Load (77.8702%), Tech Debt (19.9585%)
**Top Internal Functions/Classes:**
  * `P_MovePlayer` (Impact: 1240.2 | O(2^N) | DB: 144)
  * `P_CalcHeight` (Impact: 33.5 | O(N^4) | DB: 16)
    * *Intent:* // // P_CalcHeight // Calculate the walking / running height adjustment // // [STRIFE] Some odd adju...
  * `P_Thrust` (Impact: 1.6 | O(N^1) | DB: 2)
    * *Intent:* // // P_Thrust // Moves the given origin along a given angle. // // [STRIFE] Verified unmodified //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 47`, `func_start: 11`
* *Risk/State:* `state_mutation: 470`, `dead_code: 2`, `fragile_debt: 4`
* *Architecture:* `api: 115`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` sounds.h, p_pspr.h, s_sound.h, m_random.h, p_inter.h, w_wad.h, deh_str.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/adpcm-xq/adpcm-xq.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.708 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.327 IQR)
- **Top Global Matches:** file_cluster_13: 14.708, file_cluster_0: 14.782, file_cluster_11: 14.793
- **Magnitude:** 1864.62 | **LOC:** 790 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 90
- **Risk Profile:** Cognitive Load (40.323%), Tech Debt (9.4962%)
**Top Internal Functions/Classes:**
  * `adpcm_converter` (Impact: 793.0 | O(N^6) | DB: 90)
  * `main` (Impact: 236.4 | O(N^6) | DB: 35)
  * `adpcm_encode_data` (Impact: 65.2 | O(N^5) | DB: 43)
  * `native_to_little_endian` (Impact: 53.5 | O(N^5) | DB: 17)
  * `little_endian_to_native` (Impact: 53.4 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 63`, `args: 6`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 494`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 33`, `api: 99`, `import: 5`
* *Defense:* `safety: 24`, `doc: 50`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdio.h, adpcm-lib.h, string.h, stdlib.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.417 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.662 IQR)
- **Top Global Matches:** file_cluster_8: 13.417, file_cluster_13: 13.51, file_cluster_7: 13.776
- **Magnitude:** 1844.28 | **LOC:** 3373 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 128
- **Risk Profile:** Cognitive Load (75.6785%), Tech Debt (14.6428%)
**Top Internal Functions/Classes:**
  * `P_LookForPlayers` (Impact: 1131.5 | O(2^N) | DB: 128)
  * `P_NewRandomDir` (Impact: 70.4 | O(N^6) | DB: 14)
  * `P_RecursiveSound` (Impact: 28.2 | O(2^N) | DB: 8)
  * `P_WakeUpThing` (Impact: 6.5 | O(N^3) | DB: 1)
    * *Intent:* // // P_WakeUpThing // // villsa [STRIFE] New function // Wakes up an mobj.nearby when somebody has ...
  * `P_NoiseAlert` (Impact: 1.4 | O(N^1) | DB: 2)
    * *Intent:* // // P_NoiseAlert // If a monster yells at a player, // it will alert other monsters to the player....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 81`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 466`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 124`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdio.h, sounds.h, s_sound.h, m_random.h, i_system.h, p_inter.h, w_wad.h, r_state.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/opl3.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.168 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_7: 14.182, file_cluster_13: 14.213
- **Magnitude:** 1795.7 | **LOC:** 1378 | **CtrlFlow:** 84.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (70.6618%), Tech Debt (9.8684%)
**Top Internal Functions/Classes:**
  * `OPL3_EnvelopeCalc` (Impact: 184.3 | O(N^5) | DB: 38)
  * `OPL3_WriteReg` (Impact: 124.9 | O(N^4) | DB: 6)
  * `OPL3_PhaseGenerate` (Impact: 81.5 | O(N^6) | DB: 27)
    * *Intent:* // // Phase Generator //
  * `OPL3_Generate` (Impact: 81.5 | O(N^5) | DB: 44)
  * `OPL3_ChannelSetupAlg` (Impact: 57.0 | O(N^3) | DB: 54)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 48`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 907`, `orphaned_logic: 3`
* *Architecture:* `api: 84`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, stdio.h, opl3.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.476 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.219 IQR)
- **Top Global Matches:** file_cluster_8: 13.476, file_cluster_13: 13.589, file_cluster_11: 13.696
- **Magnitude:** 1781.84 | **LOC:** 2023 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (92.1164%), Tech Debt (53.7373%)
**Top Internal Functions/Classes:**
  * `A_Fire` (Impact: 361.6 | O(N^5) | DB: 110)
    * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
  * `P_NewChaseDir` (Impact: 74.4 | O(2^N) | DB: 28)
  * `P_CheckMissileRange` (Impact: 59.0 | O(N^6) | DB: 6)
    * *Intent:* // // P_CheckMissileRange //
  * `P_LookForPlayers` (Impact: 55.4 | O(N^6) | DB: 8)
    * *Intent:* // // P_LookForPlayers // If allaround is false, only look 180 degrees in front. // Returns true if ...
  * `A_Tracer` (Impact: 49.0 | O(N^6) | DB: 20)
    * *Intent:* //int TRACEANGLE = 0xc000000; #define TRACEANGLE 0xc000000
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 182`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 676`, `dead_code: 7`, `planned_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 264`, `import: 11`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdio.h, sounds.h, s_sound.h, m_random.h, i_system.h, r_state.h, p_local.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_user.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.443 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.529 IQR)
- **Top Global Matches:** file_cluster_8: 13.443, file_cluster_13: 13.745, file_cluster_7: 13.825
- **Magnitude:** 1771.48 | **LOC:** 1646 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (77.7573%), Tech Debt (11.8778%)
**Top Internal Functions/Classes:**
  * `P_UseArtifact` (Impact: 268.2 | O(N^6) | DB: 22)
  * `P_DeathThink` (Impact: 151.3 | O(N^6) | DB: 47)
  * `P_MovePlayer` (Impact: 110.8 | O(N^5) | DB: 21)
  * `P_HealRadius` (Impact: 84.2 | O(N^5) | DB: 11)
    * *Intent:* // Colormaps // if(player->powers[pw_invulnerability]) // { // if(player->powers[pw_invulnerability]...
  * `P_BlastRadius` (Impact: 83.0 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 59`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 651`, `dead_code: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 132`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` s_sound.h, m_random.h, i_system.h, h2def.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.599 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.637 IQR)
- **Top Global Matches:** file_cluster_8: 13.599, file_cluster_13: 13.869, file_cluster_7: 13.97
- **Magnitude:** 1744.14 | **LOC:** 1628 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (91.5226%), Tech Debt (44.0824%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 768.9 | O(2^N) | DB: 76)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_SpawnMissileAngle` (Impact: 47.4 | O(N^6) | DB: 11)
  * `P_SpawnMissile` (Impact: 38.7 | O(N^3) | DB: 17)
    * *Intent:* // Set the state, but do not use P_SetMobjState, because action
  * `P_SpawnPlayerMissile` (Impact: 34.6 | O(N^6) | DB: 24)
  * `P_SeekerMissile` (Impact: 22.6 | O(N^3) | DB: 13)
    * *Intent:* //---------------------------------------------------------------------------- // // FUNC P_SeekerMi...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 67`, `args: 1`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 609`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 11`
* *Architecture:* `api: 93`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sounds.h, s_sound.h, m_random.h, i_system.h, p_local.h, doomdef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.669 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.684 IQR)
- **Top Global Matches:** file_cluster_13: 13.669, file_cluster_8: 13.738, file_cluster_11: 13.968
- **Magnitude:** 1734.46 | **LOC:** 1613 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (91.9351%), Tech Debt (41.0068%)
**Top Internal Functions/Classes:**
  * `ST_Responder` (Impact: 426.9 | O(N^6) | DB: 105)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_doRefresh` (Impact: 115.6 | O(N^6) | DB: 31)
  * `ST_drawKeysPopup` (Impact: 86.7 | O(N^5) | DB: 40)
  * `ST_DrawExternal` (Impact: 72.2 | O(N^4) | DB: 7)
  * `ST_doPaletteStuff` (Impact: 39.6 | O(N^3) | DB: 13)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 136`, `args: 23`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 716`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 128`, `import: 31`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` m_cheat.h, m_controls.h, am_map.h, m_random.h, deh_main.h, dstrings.h, p_dialog.h, hu_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.327 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.919 IQR)
- **Top Global Matches:** file_cluster_13: 14.327, file_cluster_8: 14.448, file_cluster_11: 14.505
- **Magnitude:** 1722.58 | **LOC:** 2075 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (84.9375%), Tech Debt (52.9796%)
**Top Internal Functions/Classes:**
  * `G_NextWeapon` (Impact: 426.1 | O(2^N) | DB: 57)
  * `G_Responder` (Impact: 50.0 | O(N^5) | DB: 25)
  * `SetJoyButtons` (Impact: 36.4 | O(N^4) | DB: 6)
  * `SetMouseButtons` (Impact: 36.2 | O(N^4) | DB: 6)
  * `G_InitNew` (Impact: 36.1 | O(N^3) | DB: 35)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 113`, `args: 32`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 778`, `dead_code: 8`, `planned_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 152`, `import: 16`
* *Defense:* `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` stdio.h, i_timer.h, m_argv.h, m_controls.h, s_sound.h, m_random.h, i_system.h, v_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.803 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.777 IQR)
- **Top Global Matches:** file_cluster_13: 13.803, file_cluster_8: 13.878, file_cluster_11: 13.955
- **Magnitude:** 1704.78 | **LOC:** 2192 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 99
- **Risk Profile:** Cognitive Load (93.7441%), Tech Debt (30.9694%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 507.6 | O(N^6) | DB: 99)
  * `G_Ticker` (Impact: 335.5 | O(N^6) | DB: 19)
  * `G_DoReborn` (Impact: 41.2 | O(N^4) | DB: 11)
  * `G_PlayerExitMap` (Impact: 33.5 | O(N^4) | DB: 21)
  * `G_CheckDemoStatus` (Impact: 19.5 | O(N^4) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 111`, `args: 23`, `func_start: 10`
* *Risk/State:* `state_mutation: 572`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 157`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` i_timer.h, m_argv.h, m_controls.h, s_sound.h, m_random.h, i_system.h, v_video.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `opl/emu8950.c` (C) | Magnitude: 2911.86 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1567, indent_spaces: 1226, pointers: 879, branch: 489
- `src/doom/r_data_whd.c` (C) | Magnitude: 339.1 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 117, api: 59, branch: 26
- `src/whd_gen/huffman.h` (CPP) | Magnitude: 1517.56 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 662, indent_spaces: 567, structural_boundaries: 168, branch: 124
- `src/pd_render.cpp` (CPP) | Magnitude: 8055.36 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 2218, indent_spaces: 1255, branch: 440, pointers: 252
- `opl/slot_render.cpp` (CPP) | Magnitude: 659.46 | Delta: **0.259 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 474, indent_spaces: 364, pointers: 257, events: 222

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/doom/r_state.h` (C) | Magnitude: 320.02 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 228, pointers: 153, reflection_metaprogramming: 149, indent_spaces: 134
- `cup.sh` (SHELL) | Magnitude: 1.52 | Delta: **0.667 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 3, structural_boundaries: 2, args: 2, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/i_system.h` (C) | Magnitude: 35.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 22, api: 20, args: 14, macros: 12
- `src/net_common.c` (C) | Magnitude: 325.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 122, pointers: 118, api: 48
- `src/m_config.c` (C) | Magnitude: 439.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 313, state_mutation: 125, pointers: 104, branch: 61
- `opl/opl_queue.c` (C) | Magnitude: 251.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 99, pointers: 66, api: 41
- `src/adpcm-xq/adpcm-lib.h` (C) | Magnitude: 27.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 50, structural_boundaries: 12, api: 12, pointers: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/whd_gen/huff_sink.h` (CPP) | Magnitude: 192.26 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 56, structural_boundaries: 52, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/doom/r_plane.c` (C) | Magnitude: 957.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 326, indent_spaces: 250, branch: 105, macros: 81
- `src/heretic/p_map.c` (C) | Magnitude: 510.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 263, state_mutation: 233, pointers: 121, api: 84
- `textscreen/txt_radiobutton.c` (C) | Magnitude: 34.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, pointers: 30, state_mutation: 20, api: 9
- `src/whd_gen/whd_gen.cpp` (CPP) | Magnitude: 9750.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2491, state_mutation: 2178, branch: 463, pointers: 174
- `pkg/osx/Execute.m` (OBJECTIVE-C) | Magnitude: 105.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 32, args: 30, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/hexen/sv_save.c` (C) | Magnitude: 531.12 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 340, indent_spaces: 339, pointers: 207, structural_boundaries: 95
- `src/strife/p_saveg.c` (C) | Magnitude: 1180.1 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 761, state_mutation: 567, pointers: 506, dead_code: 158
- `src/i_videohr.h` (C) | Magnitude: 26.28 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 15, api: 11, args: 8, pointers: 5
- `src/strife/r_draw.h` (C) | Magnitude: 51.86 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: api: 36, structural_boundaries: 26, args: 14, dead_code: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/d_event.h` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.9999%)
- `src/v_video.h` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 19.0515%)
- `src/i_sound.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 63.1091%)
- `src/musx_decoder.h` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `src/deh_mapping.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 13.5349%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/d_event.h` -> **Severity: 3.932** (Embedded: 0.1365 * Error Risk: 28.8073%)
- `src/doomtype.h` -> **Severity: 1.62** (Embedded: 0.296 * Error Risk: 5.4729%)
- `src/tiny_huff.h` -> **Severity: 1.193** (Embedded: 0.014 * Error Risk: 85.0427%)
- `src/z_zone.h` -> **Severity: 0.806** (Embedded: 0.1452 * Error Risk: 5.5489%)
- `src/v_video.h` -> **Severity: 0.514** (Embedded: 0.0868 * Error Risk: 5.9233%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/doomtype.h` -> **Severity: 11716.187** (Blast Radius: 123.185 * Doc Risk: 95.1105%)
- `src/i_system.h` -> **Severity: 2638.8** (Blast Radius: 26.388 * Doc Risk: 100.0%)
- `src/d_ticcmd.h` -> **Severity: 1615.1** (Blast Radius: 16.151 * Doc Risk: 100.0%)
- `textscreen/txt_widget.h` -> **Severity: 1599.6** (Blast Radius: 15.996 * Doc Risk: 100.0%)
- `src/d_event.h` -> **Severity: 1555.01** (Blast Radius: 18.658 * Doc Risk: 83.3428%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
