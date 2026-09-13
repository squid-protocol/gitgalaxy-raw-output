# ARCHITECTURAL_BRIEF: normal_rp2040_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kilograham/rp2040-doom.git` |
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
| Total Artifacts | 779 |
| Analyzed Artifacts (Scanned) | 672 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 107 |
| Total LOC | 196203 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4744 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1451 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2972 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 44 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 575 | 177364 | 85.6% |
| CPP | 19 | 15549 | 2.8% |
| PLAINTEXT | 17 | 0 | 2.5% |
| MARKDOWN | 15 | 0 | 2.2% |
| M4 | 13 | 399 | 1.9% |
| OBJECTIVE-C | 8 | 859 | 1.2% |
| MAKEFILE | 8 | 634 | 1.2% |
| XML | 7 | 0 | 1.0% |
| SHELL | 4 | 60 | 0.6% |
| PYTHON | 4 | 630 | 0.6% |
| ASSEMBLY | 2 | 708 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 640 | 95.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 4.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 107*

**Composition by Extension & Reason:**
- `no_extension`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 2452 LOC)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.am`: 12x Excluded (Unsupported Extension: '.am')
- `.template`: 10x Excluded (Unsupported Extension: '.template')
- `.c`: 2x Excluded (Embedded Hex Payload: 16384 hex tokens in 2737 LOC), 1x Excluded (Embedded Hex Payload: 2055 hex tokens in 957 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4694 LOC)
- `.cmake`: 7x Excluded (Unsupported Extension: '.cmake')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1073 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3621 LOC)
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.man`: 2x Excluded (Unsupported Extension: '.man')
- `.in`: 1x Excluded (Machine-Generated Source Code Signature: 29 LOC), 1x Zero-Density Threshold (LOC: 96, Signals: 0)
- `.icns`: 2x Excluded (Unsupported Extension: '.icns')
- `.nib`: 2x Excluded (Unsupported Extension: '.nib')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cin`: 1x Excluded (Unsupported Extension: '.cin')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.8 | 33.3 | 22.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 51.4 | 73.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.9 | 10.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 30.9 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 26.7 | 7.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 52.1 | 88.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 57.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 47140 | 508 | 190 | `src/whd_gen/lodepng.cpp` |
| cleanup | 299 | 90 | 1 | `textscreen/txt_fileselect.c` |
| guards | 6701 | 398 | 26 | `src/whd_gen/whd_gen.cpp` |
| danger | 770 | 194 | 3 | `src/adpcm-xq/adpcm-xq.c` |
| concurrency | 4 | 2 | 0 | `src/pd_render.cpp` |
| connectivity | 8213 | 553 | 25 | `src/hexen/p_enemy.c` |
| io | 265 | 73 | 1 | `pkg/osx/GNUmakefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 9 | 0 | `pkg/win32/cp-with-libs` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 30 | 8 | 0 | `man/docgen` |
| events | 550 | 40 | 0 | `opl/slot_render.cpp` |
| tests | 5 | 3 | 0 | `src/midifile.c` |
| docs | 187 | 33 | 0 | `src/whd_gen/lodepng.cpp` |
| debt | 1313 | 217 | 5 | `src/whd_gen/whd_gen.cpp` |
| mutation | 57090 | 402 | 295 | `src/whd_gen/lodepng.cpp` |
| dead_code | 3500 | 351 | 11 | `src/hexen/sv_save.c` |
| credential | 0 | 0 | 0 | - |
| threat | 690 | 94 | 2 | `src/doom/r_state.h` |
| ml_ai | 66 | 29 | 0 | `src/strife/p_dialog.c` |
| ui | 2 | 1 | 0 | `midiproc/main.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pkg/osx/GNUmakefile` (Hits: 23)
- `src/adpcm-xq/adpcm-xq.c` (Hits: 22)
- `src/i_sdlsound.c` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i_system.h** (`src/i_system.h`) — 150 inbound connections
2. **doomtype.h** (`src/doomtype.h`) — 126 inbound connections
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

- `P_UseSpecialLine` (@ `src/strife/p_switch.c`) -> Impact: **473.4** | LOC: 629
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `P_CrossSpecialLine` (@ `src/strife/p_spec.c`) -> Impact: **372.9** | LOC: 818
  * *Intent:* // // P_CrossSpecialLine - TRIGGER // Called every time a thing origin is about // to cross a line with a non 0 special. //
- `P_DamageMobj` (@ `src/hexen/p_inter.c`) -> Impact: **318.0** | LOC: 367
  * *Intent:* */
- `P_ExecuteLineSpecial` (@ `src/hexen/p_spec.c`) -> Impact: **276.2** | LOC: 332
  * *Intent:* */ //============================================================================ // // P_ExecuteLineSpecial // // Invoked when crossing a linedef. Th...
- `G_BuildTiccmd` (@ `src/hexen/g_game.c`) -> Impact: **264.4** | LOC: 472
- `P_UseSpecialLine` (@ `src/doom/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `MN_Responder` (@ `src/hexen/mn_menu.c`) -> Impact: **257.6** | LOC: 570
  * *Intent:* //--------------------------------------------------------------------------- // // FUNC MN_Responder // //-------------------------------------------...
- `M_Responder` (@ `src/doom/m_menu.c`) -> Impact: **256.7** | LOC: 551
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `P_DamageMobj` (@ `src/strife/p_inter.c`) -> Impact: **253.9** | LOC: 337
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...
- `M_Responder` (@ `src/strife/m_menu.c`) -> Impact: **249.0** | LOC: 568
  * *Intent:* // // CONTROL PANEL // // // M_Responder //

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/hexen` | 59 | 37066.12 | 50.09% | 26.18% |
| `src/strife` | 104 | 30724.02 | 31.39% | 24.6% |
| `src/doom` | 103 | 29776.48 | 34.31% | 23.19% |
| `src/heretic` | 62 | 26893.8 | 44.15% | 23.98% |
| `src` | 145 | 23587.93 | 29.31% | 25.78% |
| `src/whd_gen` | 17 | 14290.12 | 38.9% | 16.43% |
| `opl` | 23 | 5591.94 | 31.6% | 19.96% |
| `textscreen` | 45 | 5454.28 | 22.73% | 25.31% |
| `src/pico` | 16 | 3822.02 | 36.09% | 29.27% |
| `src/setup` | 31 | 2527.1 | 11.15% | 12.57% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/i_cdmus.c` -> **100.0%** Exposure
- `src/strife/p_tick.c` -> **99.9999%** Exposure
- `src/pico/i_timer.c` -> **99.9996%** Exposure
- `src/m_fixed.c` -> **99.9925%** Exposure
- `src/deh_mapping.c` -> **99.9906%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `man/docgen` -> **100.0%** Exposure
- `man/simplecpp` -> **100.0%** Exposure
- `pkg/win32/cp-with-libs` -> **100.0%** Exposure
- `midiproc/buffer.c` -> **100.0%** Exposure
- `opl/emu8950.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/hexen/p_enemy.c` -> **120** Orphaned Functions | **0** Duplicates
- `src/strife/p_enemy.c` -> **85** Orphaned Functions | **0** Duplicates
- `src/heretic/p_enemy.c` -> **80** Orphaned Functions | **0** Duplicates
- `src/heretic/p_pspr.c` -> **52** Orphaned Functions | **0** Duplicates
- `src/doom/p_enemy.c` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3745` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/heretic/p_saveg.c` (C) -> Cumulative Risk: **706.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 874.5 | **LOC:** 1913 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.6971%)
- **Heaviest Functions:** `saveg_read_mobj_t` (Impact: 24.5), `saveg_read_player_t` (Impact: 18.2), `saveg_write_player_t` (Impact: 18.2)

### 2. `src/strife/p_saveg.c` (C) -> Cumulative Risk: **706.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 981.32 | **LOC:** 2209 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.2046%)
- **Heaviest Functions:** `P_UnArchiveSpecials` (Impact: 20.4), `saveg_read_player_t` (Impact: 20.1), `saveg_write_player_t` (Impact: 20.1)

### 3. `src/doom/r_data_whd.c` (C) -> Cumulative Risk: **699.93**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 140.5 | **LOC:** 424 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9988%), Tech Debt (99.3307%)
- **Heaviest Functions:** `lookup_texture` (Impact: 12.5), `R_InitColormaps` (Impact: 6.2), `R_DrawColumnInCache` (Impact: 4.9)

### 4. `src/strife/p_pspr.c` (C) -> Cumulative Risk: **685.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 699.04 | **LOC:** 1006 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.7441%)
- **Heaviest Functions:** `P_CheckAmmo` (Impact: 51.2), `A_FireSigil` (Impact: 28.9), `A_WeaponReady` (Impact: 23.4)

### 5. `src/doom/p_enemy.c` (C) -> Cumulative Risk: **677.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1250.84 | **LOC:** 2023 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (95.3775%)
- **Heaviest Functions:** `P_NewChaseDir` (Impact: 54.5), `A_Chase` (Impact: 50.5), `A_BossDeath` (Impact: 43.1)

### 6. `src/pico/i_system.c` (C) -> Cumulative Risk: **671.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 551.82 | **LOC:** 664 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.7023%)
- **Heaviest Functions:** `handle_exit_key_down` (Impact: 133.8), `AutoAllocMemory` (Impact: 41.8), `I_GetMemoryValue` (Impact: 35.9)

### 7. `src/doom/p_pspr.c` (C) -> Cumulative Risk: **668.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 528.2 | **LOC:** 893 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (94.587%)
- **Heaviest Functions:** `P_CheckAmmo` (Impact: 52.1), `A_WeaponReady` (Impact: 23.5), `P_SetPsprite` (Impact: 18.4)

### 8. `src/strife/hu_stuff.c` (C) -> Cumulative Risk: **667.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 447.9 | **LOC:** 708 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.8268%)
- **Heaviest Functions:** `HU_Responder` (Impact: 69.2), `HU_addMessage` (Impact: 35.1), `HU_Ticker` (Impact: 24.6)

### 9. `src/strife/p_enemy.c` (C) -> Cumulative Risk: **666.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2114.12 | **LOC:** 3373 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.0303%)
- **Heaviest Functions:** `A_BossDeath` (Impact: 71.0), `P_NewChaseDir` (Impact: 54.7), `P_LookForPlayers` (Impact: 54.5)

### 10. `src/hexen/sv_save.c` (C) -> Cumulative Risk: **664.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1743.64 | **LOC:** 3458 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.5067%)
- **Heaviest Functions:** `SV_MapTeleport` (Impact: 62.3), `StreamOutMobjSpecials` (Impact: 34.7), `StreamInMobjSpecials` (Impact: 21.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/whd_gen/lodepng.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7954.74 | **LOC:** 6256 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.0768%), Tech Debt (15.8822%)
**Top Internal Functions/Classes:**
  * `lodepng_get_color_profile` (Impact: 227.2)
    * *Intent:* /*profile must already have been inited with mode. It's ok to set some parameters of profile to done...
  * `encodeLZ77` (Impact: 223.8)
    * *Intent:* */
  * `decodeGeneric` (Impact: 208.4)
    * *Intent:* #endif /*LODEPNG_COMPILE_ANCILLARY_CHUNKS*/ /*read a PNG, the result will be in the same color type ...
  * `deflateDynamic` (Impact: 183.2)
    * *Intent:* /*Deflate for a block of type "dynamic", that is, with freely, optimally, created huffman trees*/
  * `lodepng_error_text` (Impact: 173.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1215 instances
* *State Mutation (weighted view):* 3803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1433`, `structural_boundaries: 476`, `args: 244`, `func_start: 229`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1373`, `dead_code: 20`, `planned_debt: 9`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 5`, `import: 4`
* *Defense:* `safety: 7`, `doc: 50`, `immutability_locks: 237`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` limits.h, lodepng.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/whd_gen/whd_gen.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4611.36 | **LOC:** 5332 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1722%), Tech Debt (15.2709%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 232.7)
    * *Intent:* #endif
  * `convert_textures` (Impact: 207.4)
  * `optimize_column` (Impact: 197.6)
  * `convert_vpatch` (Impact: 196.4)
    * *Intent:* // use_runs = true to do runs of pixels, false to use 0 as transparent color
  * `convert_sidedefs` (Impact: 151.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 730 instances
* *State Mutation (weighted view):* 2320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 946`, `structural_boundaries: 317`, `args: 140`, `func_start: 56`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 860`, `dead_code: 39`, `planned_debt: 23`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `import: 26`
* *Defense:* `safety: 121`, `immutability_locks: 133`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` normal.h, adpcm-lib.h, algorithm, array, cassert, cmath, compress_mus.h, cstdarg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4128.88 | **LOC:** 5444 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.3505%), Tech Debt (64.0766%)
**Top Internal Functions/Classes:**
  * `DragonSeek` (Impact: 60.1)
    * *Intent:* //============================================================================ // // DragonSeek // /...
  * `A_SorcBallOrbit` (Impact: 57.6)
    * *Intent:* // // A_SorcBallOrbit() ========================================== //
  * `A_Chase` (Impact: 57.4)
    * *Intent:* */
  * `P_NewChaseDir` (Impact: 55.2)
  * `A_FastChase` (Impact: 50.3)
    * *Intent:* //============================================================================ // Class Bosses //===...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 682 instances
* *State Mutation (weighted view):* 2274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 769`, `structural_boundaries: 502`, `args: 231`, `func_start: 172`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 910`, `dead_code: 5`, `unreferenced_by_name: 120`
* *Architecture:* `api: 199`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` h2def.h, i_swap.h, i_system.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pd_render.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3156.06 | **LOC:** 3116 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5746%), Tech Debt (53.246%)
**Top Internal Functions/Classes:**
  * `pd_end_frame` (Impact: 200.8)
  * `draw_composite_columns` (Impact: 176.7)
  * `draw_patch_columns` (Impact: 108.0)
  * `get_patch_decoder` (Impact: 85.3)
  * `push_down_x_guts` (Impact: 80.9)
    * *Intent:* #endif // new_index can be a (non overlapping) linked list (in ascending y order)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 548 instances
* *State Mutation (weighted view):* 1726
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 719`, `structural_boundaries: 126`, `args: 52`, `func_start: 51`, `class_start: 4`
* *Risk/State:* `state_mutation: 630`, `dead_code: 37`, `planned_debt: 34`, `fragile_debt: 10`, `unreferenced_by_name: 12`
* *Architecture:* `import: 31`
* *Defense:* `safety: 94`, `sync_locks: 3`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` statsomizer.h, algorithm, am_map.h, d_main.h, doomstat.h, f_finale.h, f_wipe.h, hu_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2196.06 | **LOC:** 2471 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.255%), Tech Debt (28.9402%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 162.2)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_ZMovement` (Impact: 118.2)
    * *Intent:* */
  * `P_SpawnMapThing` (Impact: 98.1)
    * *Intent:* //========================================================================== // // P_SpawnMapThing /...
  * `P_FloorBounceMissile` (Impact: 44.1)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_FloorBou...
  * `P_MobjThinker` (Impact: 43.5)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_MobjThin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 370 instances
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 486`, `structural_boundaries: 164`, `args: 49`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 460`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 40`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` h2def.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2140.44 | **LOC:** 2651 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1363%), Tech Debt (30.6256%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 175.3)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` (Impact: 88.3)
  * `G_Ticker` (Impact: 77.8)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_Responder` (Impact: 72.7)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_DoCompleted` (Impact: 57.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 389 instances
* *State Mutation (weighted view):* 1235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 505`, `structural_boundaries: 261`, `args: 68`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 457`, `dead_code: 10`, `fragile_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `io: 8`, `api: 48`, `import: 40`
* *Defense:* `safety: 5`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2114.12 | **LOC:** 3373 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.5051%), Tech Debt (99.0303%)
**Top Internal Functions/Classes:**
  * `A_BossDeath` (Impact: 71.0)
    * *Intent:* // // A_BossDeath // // Possibly trigger special effects // if on first boss level // // haleyjd 09/...
  * `P_NewChaseDir` (Impact: 54.7)
    * *Intent:* // // P_NewChaseDir //
  * `P_LookForPlayers` (Impact: 54.5)
    * *Intent:* // // P_LookForPlayers // // If allaround is false, only look 180 degrees in front. // Returns true ...
  * `A_Chase` (Impact: 51.0)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible // // haleyjd...
  * `P_DoPunchAlert` (Impact: 31.7)
    * *Intent:* // // P_DoPunchAlert // // villsa [STRIFE] New function (by Quasar ;) // Wake up buddies nearby when...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 1068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 270`, `args: 121`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 454`, `dead_code: 8`, `fragile_debt: 4`, `unreferenced_by_name: 85`
* *Architecture:* `api: 119`, `import: 18`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` deh_str.h, doomdef.h, doomstat.h, f_finale.h, g_game.h, i_system.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/emu8950.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2053.36 | **LOC:** 2028 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.0926%), Tech Debt (33.2304%)
**Top Internal Functions/Classes:**
  * `OPL_writeReg` (Impact: 114.8)
  * `OPL_calc_buffer_linear` (Impact: 88.2)
    * *Intent:* // this produces stereo
  * `commit_slot_update` (Impact: 43.2)
  * `calc_envelope` (Impact: 38.0)
  * `update_output` (Impact: 33.2)
    * *Intent:* #endif #if !EMU8950_LINEAR
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 405 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 106`, `args: 89`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 434`, `dead_code: 7`, `planned_debt: 17`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, emu8950.h, gpio.h, math.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1880.6 | **LOC:** 2235 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3152%), Tech Debt (11.7003%)
**Top Internal Functions/Classes:**
  * `P_DamageMobj` (Impact: 318.0)
    * *Intent:* */
  * `P_TouchSpecialThing` (Impact: 174.9)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC P_TouchSpec...
  * `P_KillMobj` (Impact: 142.7)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC P_KillMobj ...
  * `TryPickupWeapon` (Impact: 73.8)
    * *Intent:* //========================================================================== // // TryPickupWeapon /...
  * `TryPickupWeaponPiece` (Impact: 57.3)
    * *Intent:* */ //========================================================================== // // TryPickupWeapo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 708
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 495`, `structural_boundaries: 282`, `args: 41`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 256`, `dead_code: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` h2def.h, i_system.h, m_misc.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1790.34 | **LOC:** 2192 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.0571%), Tech Debt (33.0812%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 264.4)
  * `G_Responder` (Impact: 68.3)
    * *Intent:* */
  * `G_Ticker` (Impact: 55.8)
    * *Intent:* //========================================================================== // // G_Ticker // //===...
  * `G_DoReborn` (Impact: 28.7)
    * *Intent:* //========================================================================== // // G_DoReborn // //=...
  * `G_InitNew` (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 334 instances
* *State Mutation (weighted view):* 1102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 208`, `args: 66`, `func_start: 38`
* *Risk/State:* `state_mutation: 434`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 58`, `import: 14`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` doomkeys.h, h2def.h, i_input.h, i_system.h, i_timer.h, i_video.h, m_argv.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1765.5 | **LOC:** 2468 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.9534%), Tech Debt (51.5239%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 176.0)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_Responder` (Impact: 71.0)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_InitNew` (Impact: 62.8)
    * *Intent:* // // G_InitNew // // haleyjd 20100824: [STRIFE]: // * Added riftdest initialization // * Removed ep...
  * `G_Ticker` (Impact: 54.2)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_CheckSpot` (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 326 instances
* *State Mutation (weighted view):* 1082
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 211`, `args: 54`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 430`, `dead_code: 12`, `fragile_debt: 4`, `unreferenced_by_name: 18`
* *Architecture:* `io: 3`, `api: 50`, `import: 39`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/sv_save.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1743.64 | **LOC:** 3458 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.1142%), Tech Debt (10.7573%)
**Top Internal Functions/Classes:**
  * `SV_MapTeleport` (Impact: 62.3)
    * *Intent:* //========================================================================== // // SV_MapTeleport //...
  * `StreamOutMobjSpecials` (Impact: 34.7)
  * `StreamInMobjSpecials` (Impact: 21.8)
    * *Intent:* // // mobj_t //
  * `CopyFile` (Impact: 18.7)
    * *Intent:* //========================================================================== // // CopyFile // // Th...
  * `StreamIn_player_t` (Impact: 18.2)
    * *Intent:* // // player_t //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 332 instances
* *State Mutation (weighted view):* 1188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 228`, `args: 183`, `func_start: 89`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 524`, `dead_code: 189`, `unreferenced_by_name: 7`
* *Architecture:* `io: 13`, `api: 15`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` h2def.h, i_swap.h, i_system.h, m_misc.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1706.86 | **LOC:** 2825 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.5906%), Tech Debt (26.9261%)
**Top Internal Functions/Classes:**
  * `saveg_write_mobj_t` (Impact: 97.3)
  * `saveg_read_mobj_t` (Impact: 77.9)
    * *Intent:* // // mobj_t //
  * `P_SaveGameWriteFlashSlot` (Impact: 33.2)
  * `P_UnArchiveWorld` (Impact: 31.8)
    * *Intent:* // // P_UnArchiveWorld //
  * `P_ArchiveWorld` (Impact: 26.6)
    * *Intent:* // // P_ArchiveWorld //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 303 instances
* *State Mutation (weighted view):* 969
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 161`, `args: 70`, `func_start: 68`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 363`, `dead_code: 132`, `planned_debt: 6`, `unreferenced_by_name: 15`
* *Architecture:* `io: 2`, `api: 23`, `import: 18`
* *Defense:* `safety: 9`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` deh_main.h, doomstat.h, dstrings.h, g_game.h, address_mapped.h, sync.h, timer.h, i_system.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1703.54 | **LOC:** 2482 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.7612%), Tech Debt (60.0948%)
**Top Internal Functions/Classes:**
  * `CHolySeekerMissile` (Impact: 35.6)
    * *Intent:* //============================================================================ // // CHolySeekerMiss...
  * `P_CheckMana` (Impact: 29.4)
    * *Intent:* //--------------------------------------------------------------------------- // // FUNC P_CheckMana...
  * `A_ShedShard` (Impact: 29.3)
  * `A_FAxeAttack` (Impact: 22.8)
    * *Intent:* //============================================================================ // // A_FAxeAttack //...
  * `A_LightningClip` (Impact: 22.5)
    * *Intent:* //============================================================================ // // A_LightningClip...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 1052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 111`, `args: 90`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 410`, `unreferenced_by_name: 48`
* *Architecture:* `api: 63`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` h2def.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1695.56 | **LOC:** 2075 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.4061%), Tech Debt (35.6825%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 200.5)
  * `G_Responder` (Impact: 68.3)
    * *Intent:* */
  * `G_Ticker` (Impact: 52.2)
    * *Intent:* */
  * `G_InitNew` (Impact: 34.1)
  * `G_RecordDemo` (Impact: 18.6)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 327 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 194`, `args: 54`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 414`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 50`, `import: 16`
* *Defense:* `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` deh_str.h, doomdef.h, doomkeys.h, i_input.h, i_system.h, i_timer.h, m_argv.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1693.14 | **LOC:** 2716 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.6962%), Tech Debt (87.194%)
**Top Internal Functions/Classes:**
  * `P_NewChaseDir` (Impact: 55.2)
  * `A_Chase` (Impact: 54.3)
    * *Intent:* */
  * `P_LookForPlayers` (Impact: 32.4)
    * *Intent:* */
  * `A_NoBlocking` (Impact: 23.3)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC A_NoBlocki...
  * `P_RecursiveSound` (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 866
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 261`, `args: 108`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 364`, `dead_code: 2`, `unreferenced_by_name: 80`
* *Architecture:* `api: 99`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` doomdef.h, i_system.h, i_timer.h, m_random.h, p_local.h, s_sound.h, stdlib.h, v_video.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/po_man.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1594.7 | **LOC:** 1503 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7927%), Tech Debt (11.4135%)
**Top Internal Functions/Classes:**
  * `SpawnPolyobj` (Impact: 58.0)
    * *Intent:* //========================================================================== // // SpawnPolyobj // /...
  * `EV_RotatePoly` (Impact: 46.9)
    * *Intent:* //========================================================================== // // EV_RotatePoly // ...
  * `T_PolyDoor` (Impact: 42.7)
    * *Intent:* //========================================================================== // // T_PolyDoor // //=...
  * `CheckMobjBlocking` (Impact: 35.9)
    * *Intent:* //========================================================================== // // CheckMobjBlocking...
  * `PO_MovePolyobj` (Impact: 34.8)
    * *Intent:* //========================================================================== // // PO_MovePolyobj //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 332 instances
* *State Mutation (weighted view):* 1061
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 87`, `args: 42`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 397`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` h2def.h, i_swap.h, i_system.h, m_bbox.h, p_local.h, r_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/p_user.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1541.72 | **LOC:** 1646 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2156%), Tech Debt (10.2096%)
**Top Internal Functions/Classes:**
  * `P_PlayerThink` (Impact: 166.4)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_PlayerTh...
  * `P_UseArtifact` (Impact: 109.7)
    * *Intent:* //========================================================================== // // P_UseArtifact // ...
  * `P_MovePlayer` (Impact: 55.3)
    * *Intent:* */
  * `P_DeathThink` (Impact: 52.6)
    * *Intent:* //========================================================================== // // P_DeathThink // /...
  * `P_BlastMobj` (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 834
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 123`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 300`, `dead_code: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` h2def.h, i_system.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hexen/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1513.58 | **LOC:** 1552 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.5818%), Tech Debt (13.8989%)
**Top Internal Functions/Classes:**
  * `AM_Responder` (Impact: 97.3)
  * `AM_clipMline` (Impact: 65.7)
    * *Intent:* // Based on Cohen-Sutherland clipping algorithm but with a slightly // faster reject and precalculat...
  * `DrawWuLine` (Impact: 54.8)
  * `AM_drawFline` (Impact: 49.1)
    * *Intent:* #undef DOOUTCODE // Classic Bresenham w/ whatever optimizations I need for speed
  * `PUTDOT` (Impact: 37.9)
    * *Intent:* /* Wu antialiased line drawer. * (X0,Y0),(X1,Y1) = line to draw * BaseColor = color # of first color...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 298 instances
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 113`, `args: 62`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 352`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 33`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` am_data.h, am_map.h, doomkeys.h, h2def.h, i_swap.h, i_timer.h, i_video.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1470.54 | **LOC:** 1543 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7991%), Tech Debt (15.7151%)
**Top Internal Functions/Classes:**
  * `AM_Responder` (Impact: 96.5)
  * `AM_clipMline` (Impact: 65.7)
    * *Intent:* // Based on Cohen-Sutherland clipping algorithm but with a slightly // faster reject and precalculat...
  * `DrawWuLine` (Impact: 54.8)
  * `AM_drawFline` (Impact: 49.1)
    * *Intent:* #undef DOOUTCODE // Classic Bresenham w/ whatever optimizations I need for speed
  * `PUTDOT` (Impact: 37.9)
    * *Intent:* /* Wu antialiased line drawer. * (X0,Y0),(X1,Y1) = line to draw * BaseColor = color # of first color...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 287 instances
* *State Mutation (weighted view):* 906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 106`, `args: 61`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 332`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` am_data.h, am_map.h, deh_str.h, doomdef.h, doomkeys.h, i_timer.h, i_video.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1465.96 | **LOC:** 2634 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.3097%), Tech Debt (17.41%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 256.7)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_Drawer` (Impact: 30.5)
    * *Intent:* // // M_Drawer // Called after the view has been rendered, // but before it has been blitted. //
  * `M_DrawNetFoyer` (Impact: 19.2)
  * `M_WriteText` (Impact: 16.1)
    * *Intent:* // // Write a string using the hu_font //
  * `M_Init` (Impact: 14.2)
    * *Intent:* // // M_Init //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 229 instances
* *State Mutation (weighted view):* 714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 319`, `args: 203`, `func_start: 67`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 256`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 69`, `import: 29`
* *Defense:* `safety: 4`, `doc: 1`, `test: 1`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ctype.h, d_main.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1461.9 | **LOC:** 1628 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.912%), Tech Debt (28.8714%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 110.0)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_SpawnMapThing` (Impact: 73.6)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_SpawnMap...
  * `P_ZMovement` (Impact: 70.1)
    * *Intent:* */
  * `P_MobjThinker` (Impact: 47.5)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_MobjThin...
  * `P_SpawnMobj` (Impact: 35.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 255 instances
* *State Mutation (weighted view):* 825
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 113`, `args: 35`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 315`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 31`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` doomdef.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1375.88 | **LOC:** 1290 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.0434%), Tech Debt (83.9344%)
**Top Internal Functions/Classes:**
  * `V_DrawPatchList` (Impact: 93.8)
    * *Intent:* #pragma GCC push_options #if PICO_ON_DEVICE #pragma GCC optimize("O3") #endif
  * `V_DrawPatchN` (Impact: 46.1)
  * `WritePNGfile` (Impact: 34.4)
  * `V_DrawPatchFlipped` (Impact: 31.1)
    * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e....
  * `V_CopyRect` (Impact: 29.8)
    * *Intent:* #endif // // V_CopyRect //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 287 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 897
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 63`, `args: 37`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 323`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `io: 1`, `api: 33`, `import: 18`
* *Defense:* `safety: 13`, `immutability_locks: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` config.h, deh_str.h, r_data.h, doomtype.h, i_input.h, i_swap.h, i_system.h, i_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `opl/opl3.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1356.4 | **LOC:** 1378 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.003%), Tech Debt (9.8684%)
**Top Internal Functions/Classes:**
  * `OPL3_WriteReg` (Impact: 76.9)
  * `OPL3_EnvelopeCalc` (Impact: 75.2)
  * `OPL3_Generate` (Impact: 48.1)
  * `OPL3_ChannelUpdateRhythm` (Impact: 30.5)
  * `OPL3_ChannelSetupAlg` (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 84`, `args: 37`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 321`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` opl3.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/strife/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1313.42 | **LOC:** 2441 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3175%), Tech Debt (33.6244%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 249.0)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_DialogDimMsg` (Impact: 48.4)
    * *Intent:* // // M_DialogDimMsg // // [STRIFE] New function // haleyjd 09/04/10: Painstakingly transformed from...
  * `M_WriteText` (Impact: 22.9)
    * *Intent:* // // M_WriteText // // Write a string using the hu_font // haleyjd 09/04/10: [STRIFE] // * Rogue ma...
  * `M_Drawer` (Impact: 15.2)
    * *Intent:* // // M_Drawer // Called after the view has been rendered, // but before it has been blitted. //
  * `M_SaveGame` (Impact: 10.1)
    * *Intent:* // // Selected from DOOM menu //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 287`, `args: 176`, `func_start: 57`, `class_start: 8`
* *Risk/State:* `state_mutation: 237`, `dead_code: 5`, `fragile_debt: 9`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 103`, `import: 28`
* *Defense:* `safety: 2`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ctype.h, d_main.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
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

- `src/d_event.h` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 31.0026%)
- `src/musx_decoder.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/doomtype.h` -> **Severity: 15.09** (Embedded: 0.297 * Error Risk: 50.8151%)
- `src/d_event.h` -> **Severity: 8.49** (Embedded: 0.1357 * Error Risk: 62.5811%)
- `src/v_video.h` -> **Severity: 4.456** (Embedded: 0.0863 * Error Risk: 51.6299%)
- `textscreen/txt_widget.h` -> **Severity: 2.961** (Embedded: 0.0506 * Error Risk: 58.5327%)
- `src/tiny_huff.h` -> **Severity: 1.399** (Embedded: 0.0147 * Error Risk: 95.4556%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/doomtype.h` -> **Severity: 12352.6** (Blast Radius: 123.526 * Doc Risk: 100.0%)
- `src/m_fixed.h` -> **Severity: 1179.6** (Blast Radius: 11.796 * Doc Risk: 100.0%)
- `src/w_wad.h` -> **Severity: 635.5** (Blast Radius: 6.355 * Doc Risk: 100.0%)
- `src/v_patch.h` -> **Severity: 546.7** (Blast Radius: 5.467 * Doc Risk: 100.0%)
- `src/tiny_huff.h` -> **Severity: 537.9** (Blast Radius: 5.379 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
