# ARCHITECTURAL_BRIEF: normal_rp2040_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_rp2040_doom` |
| **Timestamp** | `2026-08-07T03:29:41.437846+00:00` |
| **Scan Duration** | `3.24s` |
| **Git Branch** | `rp2` |
| **Git Commit** | `29a453c980918a03e40fc8b69b024e7a3bdb5dc2` |
| **Git Remote** | `https://github.com/kilograham/rp2040-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 628 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 96.4 | 37.1 | 29.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 52.8 | 70.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.7 | 9.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.6 | 2.3 | 80.0 |
| API Exposure | 0.0 | 19.3 | 9.2 | 9.8 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.4 | 99.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.9 | 3.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 65.7 | 83.4 | 11.9 |
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

- `convert_textures` (@ `src/whd_gen/whd_gen.cpp`) -> Impact: **549.0** | LOC: 1246
- `P_InitSwitchList` (@ `src/strife/p_switch.c`) -> Impact: **515.7** | LOC: 838
  * *Intent:* // // P_InitSwitchList // Only called at game initialization. //
- `get_patch_decoder` (@ `src/pd_render.cpp`) -> Impact: **486.5** | LOC: 696
- `P_ExecuteLineSpecial` (@ `src/hexen/p_spec.c`) -> Impact: **477.1** | LOC: 332
- `push_down_x_guts` (@ `src/pd_render.cpp`) -> Impact: **402.3** | LOC: 875
  * *Intent:* // =========================================================== // LETS LOOK AT COLUMNS AGAIN // SORT COL // 19: texture_mid - need markers for fuzzy, ...
- `P_UseSpecialLine` (@ `src/strife/p_switch.c`) -> Impact: **333.1** | LOC: 623
- `P_XYMovement` (@ `src/hexen/p_mobj.c`) -> Impact: **327.2** | LOC: 1024
  * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMovement // //------------------------------------------...
- `P_GiveArtifact` (@ `src/hexen/p_inter.c`) -> Impact: **316.3** | LOC: 806
- `P_InitSwitchList` (@ `src/doom/p_switch.c`) -> Impact: **287.5** | LOC: 460
  * *Intent:* // // P_InitSwitchList // Only called at game initialization. //
- `DrawWuLine` (@ `src/hexen/am_map.c`) -> Impact: **284.4** | LOC: 484

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/hexen` | 59 | 27078.08 | 52.29% | 26.46% |
| `src/strife` | 104 | 26020.88 | 35.87% | 26.5% |
| `src/doom` | 103 | 24419.3 | 36.72% | 24.54% |
| `src/heretic` | 62 | 22268.68 | 46.02% | 27.88% |
| `src` | 145 | 21920.26 | 35.68% | 27.84% |
| `src/whd_gen` | 17 | 7832.68 | 43.01% | 43.43% |
| `opl` | 23 | 6273.68 | 35.85% | 23.95% |
| `textscreen` | 45 | 3496.62 | 26.16% | 22.19% |
| `src/pico` | 16 | 3383.96 | 40.72% | 27.29% |
| `src/setup` | 31 | 1871.44 | 14.37% | 16.04% |

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
- `src/hexen/p_enemy.c` -> **65** Orphaned Functions | **0** Duplicates
- `src/heretic/p_enemy.c` -> **51** Orphaned Functions | **0** Duplicates
- `src/doom/p_enemy.c` -> **46** Orphaned Functions | **0** Duplicates
- `src/heretic/p_pspr.c` -> **45** Orphaned Functions | **0** Duplicates
- `src/hexen/a_action.c` -> **30** Orphaned Functions | **0** Duplicates

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
19. **`src/strife/p_ceilng.c`** -> AI Confidence: **99.48%**
20. **`src/strife/p_doors.c`** -> AI Confidence: **99.48%**
21. **`src/strife/p_floor.c`** -> AI Confidence: **99.48%**
22. **`src/strife/p_inter.c`** -> AI Confidence: **99.48%**
23. **`src/strife/p_plats.c`** -> AI Confidence: **99.48%**
24. **`src/strife/p_setup.c`** -> AI Confidence: **99.48%**
25. **`src/strife/p_switch.c`** -> AI Confidence: **99.48%**
26. **`src/strife/p_user.c`** -> AI Confidence: **99.48%**
27. **`src/strife/r_plane.c`** -> AI Confidence: **99.48%**
28. **`src/strife/r_segs.c`** -> AI Confidence: **99.48%**
29. **`src/strife/r_things.c`** -> AI Confidence: **99.48%**
30. **`src/v_video.c`** -> AI Confidence: **99.48%**
31. **`src/w_file_memory.c`** -> AI Confidence: **99.48%**
32. **`src/pd_render.cpp`** -> AI Confidence: **99.48%**
33. **`pkg/osx/Execute.m`** -> AI Confidence: **99.48%**
34. **`src/doom/f_finale.c`** -> AI Confidence: **99.39%**
35. **`src/doom/p_saveg.c`** -> AI Confidence: **99.39%**
36. **`src/doom/r_draw.c`** -> AI Confidence: **99.39%**
37. **`src/doom/s_sound.c`** -> AI Confidence: **99.39%**
38. **`src/doom/st_stuff.c`** -> AI Confidence: **99.39%**
39. **`src/doom/statdump.c`** -> AI Confidence: **99.39%**
40. **`src/doom/wi_stuff.c`** -> AI Confidence: **99.39%**
41. **`src/heretic/am_map.c`** -> AI Confidence: **99.39%**
42. **`src/heretic/p_setup.c`** -> AI Confidence: **99.39%**
43. **`src/heretic/r_things.c`** -> AI Confidence: **99.39%**
44. **`src/hexen/am_map.c`** -> AI Confidence: **99.39%**
45. **`src/hexen/s_sound.c`** -> AI Confidence: **99.39%**
46. **`src/m_argv.c`** -> AI Confidence: **99.39%**
47. **`src/pico/i_system.c`** -> AI Confidence: **99.39%**
48. **`src/pico/i_video.c`** -> AI Confidence: **99.39%**
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3734` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/doom/r_data_whd.c` (C) -> Cumulative Risk: **718.36**
- **Archetype:** `file_cluster_11` (Distance: 19.082 IQR)
- **Magnitude:** 287.4 | **LOC:** 424 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8879%), Tech Debt (99.3307%)
- **Heaviest Functions:** `R_PrecacheLevel` (Impact: 15.9), `lookup_texture` (Impact: 15.0), `R_InitColormaps` (Impact: 9.8)

### 2. `src/strife/p_pspr.c` (C) -> Cumulative Risk: **684.12**
- **Archetype:** `file_cluster_13` (Distance: 13.869 IQR)
- **Magnitude:** 635.66 | **LOC:** 1006 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.744%), Safety Score (96.3574%)
- **Heaviest Functions:** `A_Lower` (Impact: 62.1), `P_CheckAmmo` (Impact: 37.1), `A_FireSigil` (Impact: 24.7)

### 3. `src/doom/p_enemy.c` (C) -> Cumulative Risk: **681.65**
- **Archetype:** `file_cluster_8` (Distance: 13.513 IQR)
- **Magnitude:** 1551.34 | **LOC:** 2023 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5459%), Tech Debt (94.8571%)
- **Heaviest Functions:** `A_Fire` (Impact: 143.7), `P_NewChaseDir` (Impact: 40.4), `A_Chase` (Impact: 39.2)

### 4. `src/hexen/p_setup.c` (C) -> Cumulative Risk: **679.84**
- **Archetype:** `file_cluster_8` (Distance: 13.56 IQR)
- **Magnitude:** 644.74 | **LOC:** 1232 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8075%), Tech Debt (96.3092%)
- **Heaviest Functions:** `InitMapInfo` (Impact: 57.4), `P_LoadThings` (Impact: 9.7), `P_LoadSegs` (Impact: 8.8)

### 5. `src/doom/p_tick.c` (C) -> Cumulative Risk: **675.03**
- **Archetype:** `file_cluster_13` (Distance: 14.524 IQR)
- **Magnitude:** 268.48 | **LOC:** 363 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5318%), Tech Debt (98.2394%)
- **Heaviest Functions:** `P_RunThinkers` (Impact: 49.4), `P_Ticker` (Impact: 15.3), `Z_ThinkFree` (Impact: 12.9)

### 6. `src/pico/i_system.c` (C) -> Cumulative Risk: **672.64**
- **Archetype:** `file_cluster_13` (Distance: 13.656 IQR)
- **Magnitude:** 730.42 | **LOC:** 664 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.8031%), Safety Score (97.6736%)
- **Heaviest Functions:** `handle_exit_key_down` (Impact: 133.8), `AutoAllocMemory` (Impact: 41.8), `I_GetMemoryValue` (Impact: 37.9)

### 7. `src/doom/st_lib.c` (C) -> Cumulative Risk: **668.22**
- **Archetype:** `file_cluster_13` (Distance: 13.469 IQR)
- **Magnitude:** 304.38 | **LOC:** 330 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9364%), Tech Debt (96.7554%)
- **Heaviest Functions:** `STlib_drawNum` (Impact: 22.4), `STlib_updateBinIcon` (Impact: 16.0), `STlib_updateMultIcon` (Impact: 15.9)

### 8. `src/doom/r_draw.c` (C) -> Cumulative Risk: **667.63**
- **Archetype:** `file_cluster_13` (Distance: 14.455 IQR)
- **Magnitude:** 928.9 | **LOC:** 988 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.8071%), Safety Score (98.9583%)
- **Heaviest Functions:** `R_FillBackScreen` (Impact: 23.1), `R_DrawFuzzColumnLow` (Impact: 17.2), `R_DrawFuzzColumn` (Impact: 16.8)

### 9. `src/doom/p_pspr.c` (C) -> Cumulative Risk: **664.2**
- **Archetype:** `file_cluster_8` (Distance: 12.934 IQR)
- **Magnitude:** 515.48 | **LOC:** 893 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.1247%), Safety Score (90.5433%)
- **Heaviest Functions:** `A_Lower` (Impact: 47.0), `P_CheckAmmo` (Impact: 38.0), `A_WeaponReady` (Impact: 14.7)

### 10. `src/strife/hu_lib.c` (C) -> Cumulative Risk: **663.86**
- **Archetype:** `file_cluster_13` (Distance: 13.109 IQR)
- **Magnitude:** 313.4 | **LOC:** 475 | **CtrlFlow:** 62.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.3228%), Tech Debt (96.674%)
- **Heaviest Functions:** `HUlib_drawYellowText` (Impact: 32.5), `HUlib_drawTextLine` (Impact: 13.9), `HUlib_eraseTextLine` (Impact: 10.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/pd_render.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.58 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.877 IQR)
- **Top Global Matches:** file_cluster_11: 16.58, file_cluster_6: 16.807, file_cluster_0: 16.808
- **Magnitude:** 4274.16 | **LOC:** 3116 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3692%), Tech Debt (53.1765%)
**Top Internal Functions/Classes:**
  * `get_patch_decoder` (Impact: 486.5)
  * `push_down_x_guts` (Impact: 402.3)
    * *Intent:* // =========================================================== // LETS LOOK AT COLUMNS AGAIN // SORT...
  * `draw_splash` (Impact: 277.4)
  * `draw_composite_columns` (Impact: 272.3)
  * `draw_fullscreen_background` (Impact: 183.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 89`, `args: 33`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 2208`, `dead_code: 27`, `planned_debt: 23`, `fragile_debt: 3`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 56`, `sync_locks: 2`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` f_finale.h, z_zone.h, sem.h, hu_stuff.h, w_wad.h, r_things.h, r_data.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/whd_gen/whd_gen.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.7 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.151 IQR)
- **Top Global Matches:** file_cluster_8: 14.7, file_cluster_11: 14.711, file_cluster_13: 14.788
- **Magnitude:** 3549.94 | **LOC:** 5332 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3543%), Tech Debt (23.8799%)
**Top Internal Functions/Classes:**
  * `convert_textures` (Impact: 549.0)
  * `main` (Impact: 234.1)
  * `output_min_max_best_c3` (Impact: 159.6)
  * `convert_sprites` (Impact: 75.7)
  * `output_min_max_c3` (Impact: 69.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 169`, `args: 87`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 2164`, `dead_code: 19`, `planned_debt: 12`, `fragile_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 6`
* *Architecture:* `import: 26`
* *Defense:* `safety: 34`, `immutability_locks: 71`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` iostream, utility, lodepng.h, adpcm-lib.h, algorithm, musx_decoder.h, image_decoder.h, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.833 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.415 IQR)
- **Top Global Matches:** file_cluster_8: 13.833, file_cluster_13: 14.158, file_cluster_7: 14.205
- **Magnitude:** 2367.88 | **LOC:** 5444 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3147%), Tech Debt (63.2011%)
**Top Internal Functions/Classes:**
  * `A_Explode` (Impact: 84.8)
  * `A_Scream` (Impact: 42.0)
  * `P_NewChaseDir` (Impact: 41.8)
  * `A_MinotaurLook` (Impact: 41.8)
    * *Intent:* //---------------------------------------------------------------------------- //
  * `P_InitCreatureCorpseQueue` (Impact: 38.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 533`, `structural_boundaries: 214`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1282`, `dead_code: 4`, `orphaned_logic: 65`
* *Architecture:* `api: 298`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` p_local.h, s_sound.h, i_swap.h, m_random.h, h2def.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/emu8950.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.943 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.679 IQR)
- **Top Global Matches:** file_cluster_11: 14.943, file_cluster_8: 14.964, file_cluster_13: 15.059
- **Magnitude:** 2342.86 | **LOC:** 2028 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.2299%), Tech Debt (33.2304%)
**Top Internal Functions/Classes:**
  * `OPL_writeReg` (Impact: 60.8)
    * *Intent:* #if DUMPO
  * `OPL_calc_buffer_linear` (Impact: 48.2)
  * `makeSinTable` (Impact: 30.4)
  * `commit_slot_update` (Impact: 26.4)
  * `update_output` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 489`, `structural_boundaries: 107`, `args: 7`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1567`, `dead_code: 7`, `planned_debt: 17`, `fragile_debt: 1`, `orphaned_logic: 9`
* *Architecture:* `api: 218`, `import: 7`
* *Defense:* `safety: 10`, `doc: 5`, `test: 7`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` emu8950.h, assert.h, stdlib.h, gpio.h, stdio.h, string.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/whd_gen/lodepng.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 16.007 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.17 IQR)
- **Top Global Matches:** file_cluster_13: 16.007, file_cluster_7: 16.025, file_cluster_8: 16.028
- **Magnitude:** 1826.12 | **LOC:** 6256 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8443%), Tech Debt (99.9353%)
**Top Internal Functions/Classes:**
  * `deflateDynamic` (Impact: 130.3)
  * `lodepng_huffman_code_lengths` (Impact: 109.5)
  * `encodeLZ77` (Impact: 76.7)
    * *Intent:* #endif /*LODEPNG_COMPILE_DECODER*/ /* //////////////////////////////////////////////////////////////...
  * `hash_init` (Impact: 22.1)
    * *Intent:* *outsize = (size_t)size;
  * `color_tree_get` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 71`, `args: 54`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1260`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 17`, `orphaned_logic: 13`
* *Architecture:* `io: 3`, `import: 4`
* *Defense:* `safety: 2`, `doc: 289`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, lodepng.h, stdio.h, limits.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.004 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.35 IQR)
- **Top Global Matches:** file_cluster_8: 14.004, file_cluster_13: 14.056, file_cluster_11: 14.221
- **Magnitude:** 1678.38 | **LOC:** 1552 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9521%), Tech Debt (14.9102%)
**Top Internal Functions/Classes:**
  * `DrawWuLine` (Impact: 284.4)
  * `AM_Responder` (Impact: 71.2)
  * `AM_drawWalls` (Impact: 45.6)
  * `AM_clipMline` (Impact: 40.0)
  * `AM_drawFline` (Impact: 33.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 90`, `args: 23`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 867`, `dead_code: 5`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 127`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` p_local.h, doomkeys.h, am_map.h, m_controls.h, i_timer.h, i_video.h, stdio.h, i_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.438 IQR)
- **Top Global Matches:** file_cluster_8: 14.15, file_cluster_13: 14.171, file_cluster_11: 14.304
- **Magnitude:** 1612.66 | **LOC:** 1543 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.8463%), Tech Debt (17.2181%)
**Top Internal Functions/Classes:**
  * `DrawWuLine` (Impact: 268.6)
    * *Intent:* // memcpy(I_VideoBuffer, maplump, finit_width*finit_height); // memset(fb, color, f_w*f_h);
  * `AM_Responder` (Impact: 70.0)
  * `AM_drawWalls` (Impact: 57.5)
  * `AM_clipMline` (Impact: 40.0)
  * `AM_drawFline` (Impact: 33.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 83`, `args: 21`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 827`, `dead_code: 7`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 119`, `import: 11`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` deh_str.h, p_local.h, doomkeys.h, doomdef.h, am_map.h, m_controls.h, i_timer.h, i_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.513 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.235 IQR)
- **Top Global Matches:** file_cluster_8: 13.513, file_cluster_13: 13.625, file_cluster_0: 13.729
- **Magnitude:** 1551.34 | **LOC:** 2023 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.7974%), Tech Debt (94.8571%)
**Top Internal Functions/Classes:**
  * `A_Fire` (Impact: 143.7)
    * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
  * `P_NewChaseDir` (Impact: 40.4)
  * `A_Chase` (Impact: 39.2)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_BossDeath` (Impact: 37.0)
  * `A_Look` (Impact: 26.1)
    * *Intent:* // // ACTION ROUTINES // // // A_Look // Stay in state until a player is sighted. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 182`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 672`, `dead_code: 7`, `planned_debt: 1`, `orphaned_logic: 46`
* *Architecture:* `api: 264`, `import: 11`
* *Defense:* `safety: 1`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` p_local.h, doomdef.h, stdlib.h, doomstat.h, sounds.h, s_sound.h, g_game.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.464 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.526 IQR)
- **Top Global Matches:** file_cluster_8: 13.464, file_cluster_13: 13.71, file_cluster_7: 13.814
- **Magnitude:** 1547.14 | **LOC:** 2471 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3439%), Tech Debt (21.3807%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 327.2)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_ZMovement` (Impact: 203.4)
  * `P_SpawnMapThing` (Impact: 48.7)
  * `P_FloorBounceMissile` (Impact: 38.1)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_FloorBou...
  * `P_MobjThinker` (Impact: 31.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 337`, `structural_boundaries: 79`, `args: 1`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 634`, `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 131`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` p_local.h, sounds.h, s_sound.h, m_random.h, h2def.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.22 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.268 IQR)
- **Top Global Matches:** file_cluster_8: 13.22, file_cluster_13: 13.451, file_cluster_7: 13.583
- **Magnitude:** 1443.9 | **LOC:** 1837 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6643%), Tech Debt (25.236%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` (Impact: 78.3)
  * `WI_updateDeathmatchStats` (Impact: 46.0)
  * `WI_updateStats` (Impact: 44.8)
  * `WI_loadUnloadData` (Impact: 30.6)
  * `WI_updateAnimatedBack` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 106`, `args: 35`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 743`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 160`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` deh_main.h, v_video.h, doomstat.h, z_zone.h, sounds.h, wi_stuff.h, s_sound.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/sb_bar.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.93 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.44 IQR)
- **Top Global Matches:** file_cluster_8: 12.93, file_cluster_13: 13.304, file_cluster_7: 13.33
- **Magnitude:** 1396.72 | **LOC:** 2007 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9707%), Tech Debt (12.1758%)
**Top Internal Functions/Classes:**
  * `DrawMainBar` (Impact: 70.9)
    * *Intent:* //========================================================================== //
  * `DrawAnimatedIcons` (Impact: 36.9)
  * `DrawFullScreenStuff` (Impact: 29.2)
    * *Intent:* //========================================================================== // // DrawWeaponPieces ...
  * `SB_Drawer` (Impact: 21.5)
  * `DrawKeyBar` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 163`, `args: 30`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 835`, `orphaned_logic: 7`
* *Architecture:* `api: 125`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` p_local.h, m_cheat.h, i_video.h, i_cdmus.h, m_bbox.h, m_misc.h, i_swap.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/opl3.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.168 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_7: 14.182, file_cluster_13: 14.213
- **Magnitude:** 1372.9 | **LOC:** 1378 | **CtrlFlow:** 84.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6618%), Tech Debt (9.8684%)
**Top Internal Functions/Classes:**
  * `OPL3_EnvelopeCalc` (Impact: 66.3)
  * `OPL3_WriteReg` (Impact: 52.9)
  * `OPL3_Generate` (Impact: 31.6)
  * `OPL3_ChannelSetupAlg` (Impact: 31.0)
  * `OPL3_PhaseGenerate` (Impact: 26.4)
    * *Intent:* // // Phase Generator //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 48`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 907`, `orphaned_logic: 3`
* *Architecture:* `api: 84`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, stdio.h, string.h, opl3.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.902 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.675 IQR)
- **Top Global Matches:** file_cluster_8: 13.902, file_cluster_13: 13.915, file_cluster_11: 14.079
- **Magnitude:** 1369.26 | **LOC:** 2825 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9401%), Tech Debt (70.3402%)
**Top Internal Functions/Classes:**
  * `P_UnArchiveWorld` (Impact: 55.0)
  * `P_ArchiveWorld` (Impact: 45.4)
    * *Intent:* #endif #endif #if !LOAD_COMPRESSED // int tics;
  * `P_ArchiveSpecials` (Impact: 42.3)
    * *Intent:* // struct mobj_s* tracer;
  * `P_UnArchiveSpecials` (Impact: 41.3)
  * `P_SaveGameWriteFlashSlot` (Impact: 33.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 104`, `args: 23`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 721`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 2`, `api: 154`, `import: 18`
* *Defense:* `safety: 8`, `test: 3`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` deh_main.h, p_local.h, sync.h, stdlib.h, doomstat.h, z_zone.h, picoflash.h, timer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_spec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.091 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.589 IQR)
- **Top Global Matches:** file_cluster_8: 13.091, file_cluster_13: 13.4, file_cluster_7: 13.478
- **Magnitude:** 1359.96 | **LOC:** 1205 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.4137%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_ExecuteLineSpecial` (Impact: 477.1)
  * `P_PlayerInSpecialSector` (Impact: 62.6)
    * *Intent:* //============================================================================ // // P_ActivateLine ...
  * `P_SpawnSpecials` (Impact: 36.2)
  * `P_UpdateSpecials` (Impact: 17.2)
  * `EV_LineSearchForPuzzleItem` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 80`, `args: 7`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 549`, `orphaned_logic: 11`
* *Architecture:* `api: 103`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` p_local.h, m_misc.h, s_sound.h, h2def.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.264 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.028 IQR)
- **Top Global Matches:** file_cluster_13: 15.264, file_cluster_11: 15.279, file_cluster_0: 15.363
- **Magnitude:** 1354.22 | **LOC:** 1175 | **CtrlFlow:** 84.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0486%), Tech Debt (17.3964%)
**Top Internal Functions/Classes:**
  * `R_InitSpriteDefs` (Impact: 53.4)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawMaskedColumn` (Impact: 52.6)
  * `R_DrawSprite` (Impact: 42.1)
    * *Intent:* #endif // // R_DrawSprite //
  * `R_ProjectSprite` (Impact: 36.8)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_DrawVisSprite` (Impact: 29.0)
    * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 44`, `args: 8`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 871`, `dead_code: 9`, `planned_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 144`, `import: 13`
* *Defense:* `safety: 8`, `test: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` deh_main.h, stdlib.h, doomdef.h, doomstat.h, z_zone.h, tiny_huff.h, stdio.h, i_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.792 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.364 IQR)
- **Top Global Matches:** file_cluster_13: 14.792, file_cluster_11: 14.92, file_cluster_8: 14.936
- **Magnitude:** 1229.3 | **LOC:** 1068 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.4978%), Tech Debt (12.4682%)
**Top Internal Functions/Classes:**
  * `R_DrawVisSprite` (Impact: 217.2)
    * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. //
  * `R_InitSpriteDefs` (Impact: 49.1)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawSprite` (Impact: 39.5)
  * `R_ProjectSprite` (Impact: 27.8)
  * `R_DrawPSprite` (Impact: 26.7)
    * *Intent:* // BSP is traversed by subsector. // A sector might have been split into several // subsectors durin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 39`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 637`, `dead_code: 7`, `orphaned_logic: 3`
* *Architecture:* `api: 128`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` deh_main.h, p_local.h, stdlib.h, doomdef.h, doomstat.h, z_zone.h, stdio.h, i_swap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.33 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.919 IQR)
- **Top Global Matches:** file_cluster_13: 14.33, file_cluster_8: 14.452, file_cluster_11: 14.508
- **Magnitude:** 1223.88 | **LOC:** 2075 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.893%), Tech Debt (57.2962%)
**Top Internal Functions/Classes:**
  * `G_NextWeapon` (Impact: 93.6)
  * `G_InitNew` (Impact: 20.1)
  * `G_Responder` (Impact: 18.8)
  * `G_DoCompleted` (Impact: 17.6)
  * `SetJoyButtons` (Impact: 15.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 113`, `args: 32`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 778`, `dead_code: 8`, `planned_debt: 1`, `orphaned_logic: 15`
* *Architecture:* `api: 152`, `import: 16`
* *Defense:* `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` deh_str.h, p_local.h, doomkeys.h, doomdef.h, stdlib.h, m_argv.h, m_controls.h, i_timer.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.669 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.684 IQR)
- **Top Global Matches:** file_cluster_13: 13.669, file_cluster_8: 13.738, file_cluster_11: 13.968
- **Magnitude:** 1207.36 | **LOC:** 1613 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.9351%), Tech Debt (41.0068%)
**Top Internal Functions/Classes:**
  * `ST_Responder` (Impact: 136.9)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_doRefresh` (Impact: 37.8)
  * `ST_drawKeysPopup` (Impact: 32.9)
  * `ST_DrawExternal` (Impact: 31.9)
  * `ST_doPaletteStuff` (Impact: 21.2)
    * *Intent:* */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 136`, `args: 23`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 716`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 128`, `import: 31`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` deh_main.h, doomstat.h, z_zone.h, w_wad.h, s_sound.h, am_map.h, sounds.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_pspr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.276 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.368 IQR)
- **Top Global Matches:** file_cluster_8: 13.276, file_cluster_7: 13.684, file_cluster_13: 13.703
- **Magnitude:** 1190.66 | **LOC:** 2482 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.2148%), Tech Debt (51.9538%)
**Top Internal Functions/Classes:**
  * `A_Lower` (Impact: 118.8)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC A_ReFire //...
  * `A_FireConePL1` (Impact: 24.6)
  * `P_CheckMana` (Impact: 21.5)
  * `A_FPunchAttack` (Impact: 17.6)
    * *Intent:* //============================================================================ // // A_ZapMimic // /...
  * `A_LightningClip` (Impact: 16.8)
    * *Intent:* //============================================================================ // // A_FHammerAttack
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 71`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 682`, `orphaned_logic: 30`
* *Architecture:* `api: 120`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` m_random.h, s_sound.h, h2def.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.458 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.668 IQR)
- **Top Global Matches:** file_cluster_8: 13.458, file_cluster_13: 13.549, file_cluster_7: 13.815
- **Magnitude:** 1182.58 | **LOC:** 3373 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.036%), Tech Debt (93.4607%)
**Top Internal Functions/Classes:**
  * `P_LookForPlayers` (Impact: 201.4)
  * `A_FireSigilWeapon` (Impact: 107.5)
  * `A_PeasantCrash` (Impact: 55.4)
  * `A_Chase` (Impact: 39.7)
  * `P_NewRandomDir` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 81`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 458`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 25`
* *Architecture:* `api: 124`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` deh_str.h, p_local.h, doomdef.h, stdlib.h, doomstat.h, z_zone.h, sounds.h, f_finale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_user.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.443 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.529 IQR)
- **Top Global Matches:** file_cluster_8: 13.443, file_cluster_13: 13.745, file_cluster_7: 13.825
- **Magnitude:** 1158.18 | **LOC:** 1646 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.7573%), Tech Debt (11.8778%)
**Top Internal Functions/Classes:**
  * `P_UseArtifact` (Impact: 83.2)
  * `P_DeathThink` (Impact: 48.9)
  * `P_MovePlayer` (Impact: 40.9)
  * `P_BlastRadius` (Impact: 35.0)
  * `P_HealRadius` (Impact: 30.1)
    * *Intent:* // Colormaps // if(player->powers[pw_invulnerability]) // { // if(player->powers[pw_invulnerability]...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 59`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 651`, `dead_code: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 132`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` p_local.h, s_sound.h, m_random.h, h2def.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_inter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.208 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.213 IQR)
- **Top Global Matches:** file_cluster_8: 12.208, file_cluster_13: 12.555, file_cluster_7: 12.622
- **Magnitude:** 1130.5 | **LOC:** 2235 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8638%), Tech Debt (15.3638%)
**Top Internal Functions/Classes:**
  * `P_GiveArtifact` (Impact: 316.3)
  * `P_KillMobj` (Impact: 226.3)
  * `P_TouchSpecialThing` (Impact: 58.5)
  * `P_PoisonDamage` (Impact: 27.3)
  * `ActiveMinotaur` (Impact: 16.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 115`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 280`, `dead_code: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `api: 117`, `import: 6`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` p_local.h, s_sound.h, m_misc.h, m_random.h, h2def.h, i_system.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/i_oplmusic.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.761 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.413 IQR)
- **Top Global Matches:** file_cluster_8: 12.761, file_cluster_13: 13.003, file_cluster_7: 13.178
- **Magnitude:** 1093.96 | **LOC:** 1988 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.153%), Tech Debt (24.2339%)
**Top Internal Functions/Classes:**
  * `KeyOnEvent` (Impact: 28.4)
  * `I_OPL_DevMessages` (Impact: 23.7)
  * `I_OPL_RegisterSong` (Impact: 22.5)
    * *Intent:* // printf("DELTA TICK %d\n", nticks);
  * `MetaEvent` (Impact: 21.1)
  * `ProcessEvent` (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 124`, `args: 17`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 559`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 184`, `import: 14`
* *Defense:* `safety: 5`, `test: 2`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` deh_main.h, assert.h, stdlib.h, i_sound.h, z_zone.h, memio.h, stdio.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_switch.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.648 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.794 IQR)
- **Top Global Matches:** file_cluster_8: 11.648, file_cluster_13: 11.914, file_cluster_11: 12.124
- **Magnitude:** 1091.28 | **LOC:** 1080 | **CtrlFlow:** 94.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.5873%), Tech Debt (76.3931%)
**Top Internal Functions/Classes:**
  * `P_InitSwitchList` (Impact: 515.7)
    * *Intent:* // // P_InitSwitchList // Only called at game initialization. //
  * `P_UseSpecialLine` (Impact: 333.1)
  * `P_ChangeSwitchTexture` (Impact: 30.4)
    * *Intent:* // Note that this is called "episode" here but it's actually something // quite different. As we pro...
  * `P_MoveWall` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 20`, `args: 1`, `func_start: 4`
* *Risk/State:* `state_mutation: 156`, `planned_debt: 20`, `fragile_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 28`, `import: 18`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` deh_main.h, p_local.h, doomdef.h, sounds.h, z_zone.h, doomstat.h, r_state.h, p_dialog.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/sb_bar.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.902 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.343 IQR)
- **Top Global Matches:** file_cluster_8: 12.902, file_cluster_13: 13.211, file_cluster_7: 13.304
- **Magnitude:** 1084.38 | **LOC:** 1287 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1782%), Tech Debt (11.3207%)
**Top Internal Functions/Classes:**
  * `SB_Drawer` (Impact: 48.7)
  * `DrawMainBar` (Impact: 39.6)
  * `DrawFullScreenStuff` (Impact: 26.0)
  * `CheatArtifact3Func` (Impact: 21.4)
  * `SB_Ticker` (Impact: 19.0)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC SB_Ticker /...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 131`, `args: 23`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 635`, `orphaned_logic: 4`
* *Architecture:* `api: 116`, `import: 10`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` deh_str.h, p_local.h, doomdef.h, m_cheat.h, s_sound.h, i_video.h, i_swap.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `opl/emu8950.c` (C) | Magnitude: 2342.86 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1567, indent_spaces: 1226, pointers: 879, branch: 489
- `src/doom/r_data_whd.c` (C) | Magnitude: 287.4 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 117, api: 59, branch: 26
- `src/whd_gen/huffman.h` (CPP) | Magnitude: 999.66 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 662, indent_spaces: 567, structural_boundaries: 168, branch: 124
- `src/pd_render.cpp` (CPP) | Magnitude: 4274.16 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 2208, indent_spaces: 1255, branch: 440, pointers: 252
- `opl/slot_render.cpp` (CPP) | Magnitude: 730.56 | Delta: **0.262 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 468, indent_spaces: 364, pointers: 257, events: 222

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/doom/r_state.h` (C) | Magnitude: 309.02 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 228, pointers: 153, reflection_metaprogramming: 149, indent_spaces: 134
- `cup.sh` (SHELL) | Magnitude: 1.52 | Delta: **0.667 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 3, structural_boundaries: 2, args: 2, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/doom/r_plane.c` (C) | Magnitude: 560.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 326, indent_spaces: 250, branch: 105, macros: 81
- `src/i_system.h` (C) | Magnitude: 35.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 22, api: 20, args: 14, macros: 12
- `src/net_common.c` (C) | Magnitude: 249.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 214, state_mutation: 122, pointers: 118, api: 48
- `src/m_config.c` (C) | Magnitude: 336.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 313, state_mutation: 125, pointers: 104, branch: 61
- `opl/opl_queue.c` (C) | Magnitude: 190.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 141, state_mutation: 99, pointers: 66, api: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/whd_gen/huff_sink.h` (CPP) | Magnitude: 103.06 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 56, structural_boundaries: 52, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/heretic/p_map.c` (C) | Magnitude: 449.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 263, state_mutation: 233, pointers: 121, api: 84
- `textscreen/txt_radiobutton.c` (C) | Magnitude: 34.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, pointers: 30, state_mutation: 20, api: 9
- `src/heretic/s_sound.c` (C) | Magnitude: 825.08 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 414, state_mutation: 358, branch: 103, api: 58
- `pkg/osx/Execute.m` (OBJECTIVE-C) | Magnitude: 76.38 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 32, args: 30, branch: 13
- `src/image_decoder.h` (C) | Magnitude: 19.24 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: pointers: 12, api: 4, macros: 3, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/hexen/sv_save.c` (C) | Magnitude: 487.42 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 340, indent_spaces: 339, pointers: 207, structural_boundaries: 95
- `src/strife/p_saveg.c` (C) | Magnitude: 923.4 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
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

- `src/doomtype.h` -> **Severity: 15.23** (Embedded: 0.296 * Error Risk: 51.4437%)
- `src/d_event.h` -> **Severity: 11.3** (Embedded: 0.1365 * Error Risk: 82.7987%)
- `src/z_zone.h` -> **Severity: 7.392** (Embedded: 0.1452 * Error Risk: 50.9051%)
- `src/v_video.h` -> **Severity: 4.603** (Embedded: 0.0868 * Error Risk: 53.0127%)
- `src/doomkeys.h` -> **Severity: 3.567** (Embedded: 0.0659 * Error Risk: 54.157%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/doomtype.h` -> **Severity: 11246.766** (Blast Radius: 123.185 * Doc Risk: 91.2998%)
- `src/i_system.h` -> **Severity: 2638.742** (Blast Radius: 26.388 * Doc Risk: 99.9978%)
- `src/d_ticcmd.h` -> **Severity: 1614.338** (Blast Radius: 16.151 * Doc Risk: 99.9528%)
- `textscreen/txt_widget.h` -> **Severity: 1599.6** (Blast Radius: 15.996 * Doc Risk: 100.0%)
- `src/z_zone.h` -> **Severity: 1443.383** (Blast Radius: 14.463 * Doc Risk: 99.7983%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
