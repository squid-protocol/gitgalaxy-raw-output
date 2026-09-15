# ARCHITECTURAL_BRIEF: loony_ascii_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wojciech-graj/doom-ascii.git` |
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
| Total Artifacts | 193 |
| Analyzed Artifacts (Scanned) | 181 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 35379 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.8% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3491 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1897 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0202 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 177 | 35249 | 97.8% |
| MAKEFILE | 2 | 130 | 1.1% |
| MARKDOWN | 1 | 0 | 0.6% |
| XML | 1 | 0 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z -0.52; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 47%, Large Core Modules 20%, Data / Markup / Trivial 10%, Compute Cores Files 8%, Interface Declarations Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 180 | 99.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 86, Signals: 0)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 4663 LOC), 1x Excluded (Embedded Array/Matrix Payload: 17673 commas in 2228 LOC)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Unsupported Format (.cfg)
- `.desktop`: 1x Unsupported Format (.desktop)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1332 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.1 | 25.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 40.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 24.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 33.2 | 10.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.0 | 4.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 62.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 42.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7846 | 122 | 171 | `src/p_enemy.c` |
| cleanup | 35 | 15 | 0 | `src/d_iwad.c` |
| guards | 735 | 61 | 13 | `src/doomgeneric_ascii.c` |
| danger | 173 | 34 | 3 | `src/v_video.c` |
| concurrency | 1 | 1 | 0 | `src/doomgeneric_ascii.c` |
| connectivity | 2151 | 167 | 25 | `src/m_controls.h` |
| io | 44 | 13 | 0 | `src/m_misc.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 2 | 0 | `Makefile` |
| time | 9 | 1 | 0 | `src/doomgeneric_ascii.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `Makefile` |
| events | 53 | 5 | 0 | `src/wi_stuff.c` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `src/sha1.c` |
| debt | 210 | 50 | 4 | `src/statdump.c` |
| mutation | 10853 | 91 | 240 | `src/g_game.c` |
| dead_code | 720 | 86 | 9 | `src/p_saveg.c` |
| credential | 1 | 1 | 0 | `src/doomgeneric_ascii.c` |
| threat | 101 | 19 | 1 | `Makefile` |
| ml_ai | 14 | 6 | 0 | `src/d_englsh.h` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/m_misc.c` (Hits: 11)
- `Makefile` (Hits: 10)
- `src/m_config.c` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomtype.h** (`src/doomtype.h`) — 49 inbound connections
2. **doomdef.h** (`src/doomdef.h`) — 41 inbound connections
3. **i_system.h** (`src/i_system.h`) — 39 inbound connections
4. **z_zone.h** (`src/z_zone.h`) — 39 inbound connections
5. **doomstat.h** (`src/doomstat.h`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`src/d_main.c`) — 42 outbound dependencies
2. **g_game.c** (`src/g_game.c`) — 36 outbound dependencies
3. **m_menu.c** (`src/m_menu.c`) — 25 outbound dependencies
4. **i_input.c** (`src/i_input.c`) — 24 outbound dependencies
5. **st_stuff.c** (`src/st_stuff.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `src/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `M_Responder` **(Compute Cores)** (@ `src/m_menu.c`) -> Impact: **216.2** | LOC: 477
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `P_CrossSpecialLine` **(Many-Argument Workhorses)** (@ `src/p_spec.c`) -> Impact: **211.0** | LOC: 460
  * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or by timed thinkers. // // // P_CrossSpecialLine - ...
- `P_TouchSpecialThing` **(Compute Cores)** (@ `src/p_inter.c`) -> Impact: **180.9** | LOC: 328
  * *Intent:* // // P_TouchSpecialThing //
- `G_BuildTiccmd` **(Many-Argument Workhorses)** (@ `src/g_game.c`) -> Impact: **145.4** | LOC: 276
  * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo buffer. // If recording a demo, write it out //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `src/r_segs.c`) -> Impact: **138.1** | LOC: 372
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `ST_Responder` **(Compute Cores)** (@ `src/st_stuff.c`) -> Impact: **108.8** | LOC: 224
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `D_DoomMain` **(Compute Cores)** (@ `src/d_main.c`) -> Impact: **100.0** | LOC: 680
  * *Intent:* #endif // // D_DoomMain //
- `AM_Responder` **(Compute Cores)** (@ `src/am_map.c`) -> Impact: **94.8** | LOC: 143
  * *Intent:* // // Handle events (user inputs) in automap mode //
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `src/p_inter.c`) -> Impact: **94.4** | LOC: 144
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 177 | 34488.38 | 25.87% | 23.24% |
| `__monolith__` | 3 | 60.74 | 24.93% | 0.0% |
| `src/AppDir/usr/share/metainfo` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/p_tick.c` -> **99.9999%** Exposure
- `src/m_fixed.c` -> **99.9925%** Exposure
- `src/i_timer.c` -> **99.9797%** Exposure
- `src/i_sound.c` -> **99.9496%** Exposure
- `src/i_video.c` -> **99.8259%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/am_map.c` -> **100.0%** Exposure
- `src/d_loop.c` -> **100.0%** Exposure
- `src/d_main.c` -> **100.0%** Exposure
- `src/d_net.c` -> **100.0%** Exposure
- `src/f_finale.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/p_enemy.c` -> **49** Orphaned Functions | **0** Duplicates
- `src/p_pspr.c` -> **24** Orphaned Functions | **0** Duplicates
- `src/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `src/i_video.c` -> **18** Orphaned Functions | **0** Duplicates
- `src/v_video.c` -> **17** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `918` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/p_saveg.c` (C) -> Cumulative Risk: **687.38**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.37)
- **Magnitude:** 901.4 | **LOC:** 1892 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.2296%)
- **Heaviest Functions:** `P_UnArchiveSpecials` (I/O & Config Routines, Impact: 18.9), `P_ArchiveSpecials` (I/O & Config Routines, Impact: 17.2), `saveg_read_player_t` (Compute Cores, Impact: 16.3)

### 2. `src/p_pspr.c` (C) -> Cumulative Risk: **669.37**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.05)
- **Magnitude:** 540.84 | **LOC:** 889 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.4249%)
- **Heaviest Functions:** `P_CheckAmmo` (Compute Cores, Impact: 52.1), `A_WeaponReady` (Compute Cores, Impact: 23.5), `P_SetPsprite` (Many-Argument Workhorses, Impact: 16.2)

### 3. `src/p_enemy.c` (C) -> Cumulative Risk: **663.81**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.83)
- **Magnitude:** 1415.82 | **LOC:** 2007 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.3888%)
- **Heaviest Functions:** `P_NewChaseDir` (Compute Cores, Impact: 54.4), `A_Chase` (Compute Cores, Impact: 50.5), `A_BossDeath` (Compute Cores, Impact: 43.1)

### 4. `src/hu_lib.c` (C) -> Cumulative Risk: **655.0**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.51)
- **Magnitude:** 292.14 | **LOC:** 348 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.473%)
- **Heaviest Functions:** `HUlib_drawTextLine` (Compute Cores, Impact: 19.4), `HUlib_eraseTextLine` (Compute Cores, Impact: 14.2), `HUlib_keyInIText` (Compute Cores, Impact: 13.1)

### 5. `src/st_lib.c` (C) -> Cumulative Risk: **653.68**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.04)
- **Magnitude:** 171.02 | **LOC:** 285 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.1491%)
- **Heaviest Functions:** `STlib_drawNum` (Compute Cores, Impact: 25.5), `STlib_updateBinIcon` (Compute Cores, Impact: 13.6), `STlib_updateMultIcon` (Compute Cores, Impact: 13.5)

### 6. `src/z_zone.c` (C) -> Cumulative Risk: **648.5**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.47)
- **Magnitude:** 340.56 | **LOC:** 489 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4143%)
- **Heaviest Functions:** `Z_Malloc` (Many-Argument Workhorses, Impact: 35.4), `Z_DumpHeap` (Compute Cores, Impact: 17.3), `Z_Free` (Compute Cores, Impact: 13.7)

### 7. `src/v_video.c` (C) -> Cumulative Risk: **642.38**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.22)
- **Magnitude:** 843.24 | **LOC:** 933 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.64%)
- **Heaviest Functions:** `V_CopyRect` (Many-Argument Workhorses, Impact: 29.9), `V_DrawPatch` (Many-Argument Workhorses, Impact: 22.9), `V_DrawPatchFlipped` (Many-Argument Workhorses, Impact: 22.9)

### 8. `src/r_plane.c` (C) -> Cumulative Risk: **637.4**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.15)
- **Magnitude:** 348.86 | **LOC:** 447 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1437%)
- **Heaviest Functions:** `R_MakeSpans` (Many-Argument Workhorses, Impact: 23.5), `R_MapPlane` (Many-Argument Workhorses, Impact: 22.9), `R_CheckPlane` (Many-Argument Workhorses, Impact: 19.0)

### 9. `src/p_mobj.c` (C) -> Cumulative Risk: **636.07**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.64)
- **Magnitude:** 886.08 | **LOC:** 1050 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2313%)
- **Heaviest Functions:** `P_XYMovement` (Compute Cores, Impact: 68.6), `P_ZMovement` (Compute Cores, Impact: 50.6), `P_SpawnMapThing` (Compute Cores, Impact: 43.1)

### 10. `src/m_misc.c` (C) -> Cumulative Risk: **634.25**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.93)
- **Magnitude:** 319.9 | **LOC:** 536 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.6574%)
- **Heaviest Functions:** `M_StringReplace` (Many-Argument Workhorses, Impact: 16.9), `M_StringJoin` (Many-Argument Workhorses, Impact: 12.7), `M_ExtractFileBase` (Compute Cores, Impact: 12.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1855.24 | **LOC:** 2304 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.2817%), Tech Debt (37.8438%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 145.4)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `G_Responder` **(Compute Cores)** (Impact: 66.5)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_Ticker` **(Compute Cores)** (Impact: 55.6)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_DoCompleted` **(Compute Cores)** (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 278`, `args: 54`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 430`, `dead_code: 10`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 49`, `import: 36`
* *Defense:* `safety: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1415.82 | **LOC:** 2007 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.0809%), Tech Debt (76.6969%)
**Top Internal Functions/Classes:**
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 54.4)
  * `A_Chase` **(Compute Cores)** (Impact: 50.5)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_BossDeath` **(Compute Cores)** (Impact: 43.1)
    * *Intent:* // // A_BossDeath // Possibly trigger special effects // if on first boss level //
  * `A_SpawnFly` **(Compute Cores)** (Impact: 35.3)
  * `A_Look` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* // // ACTION ROUTINES // // // A_Look // Stay in state until a player is sighted. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 729
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 224`, `args: 78`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 281`, `dead_code: 6`, `unreferenced_by_name: 49`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/i_scale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1229.78 | **LOC:** 1453 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.5549%), Tech Debt (13.8825%)
**Top Internal Functions/Classes:**
  * `I_Stretch5x` **(Many-Argument Workhorses)** (Impact: 21.1)
    * *Intent:* // 5x stretch (1600x1200)
  * `I_Stretch4x` **(Many-Argument Workhorses)** (Impact: 19.5)
    * *Intent:* // 4x stretch (1280x960)
  * `I_Stretch3x` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* // 3x stretch (960x720)
  * `I_Stretch2x` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* // 2x stretch (640x480)
  * `I_Stretch1x` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* // 1x stretch (320x240)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 236 instances
* *State Mutation (weighted view):* 906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 102`, `args: 35`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 434`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` doomtype.h, i_video.h, m_argv.h, stdio.h, stdlib.h, string.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1181.64 | **LOC:** 2126 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3399%), Tech Debt (26.8549%)
**Top Internal Functions/Classes:**
  * `M_Responder` **(Compute Cores)** (Impact: 216.2)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_DrawReadThis1` **(I/O & Config Routines)** (Impact: 17.6)
    * *Intent:* // // Read This Menus // Had a "quick hack to fix romero bug" //
  * `M_WriteText` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* // // Write a string using the hu_font //
  * `M_Drawer` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* #endif // // M_Drawer // Called after the view has been rendered, // but before it has been blitted....
  * `M_Init` **(I/O & Config Routines)** (Impact: 10.4)
    * *Intent:* // // M_Init //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 182 instances
* *State Mutation (weighted view):* 570
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 292`, `args: 176`, `func_start: 56`, `class_start: 11`
* *Risk/State:* `state_mutation: 206`, `dead_code: 3`, `fragile_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 104`, `import: 25`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ctype.h, d_main.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1169.0 | **LOC:** 1830 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4566%), Tech Debt (25.3459%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(Compute Cores)** (Impact: 52.6)
  * `WI_loadUnloadData` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* // Common load/unload function. Iterates over all the graphics // lumps to be loaded/unloaded into m...
  * `WI_updateDeathmatchStats` **(I/O & Config Routines)** (Impact: 34.0)
  * `WI_updateStats` **(I/O & Config Routines)** (Impact: 33.2)
  * `WI_drawOnLnode` **(Compute Cores)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 127`, `args: 111`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 244`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` deh_main.h, doomstat.h, g_game.h, i_swap.h, i_system.h, m_misc.h, m_random.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1157.2 | **LOC:** 1356 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.0832%), Tech Debt (12.642%)
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 94.8)
    * *Intent:* // // Handle events (user inputs) in automap mode //
  * `AM_clipMline` **(Compute Cores)** (Impact: 68.9)
    * *Intent:* // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algorithm but with a sligh...
  * `AM_drawFline` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* #undef DOOUTCODE // // Classic Bresenham w/ whatever optimizations needed for speed //
  * `AM_drawWalls` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* // // Determines visible lines, draws them. // This is LineDef based, not LineSeg based. //
  * `AM_drawLineCharacter` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 109`, `args: 58`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `state_mutation: 264`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `import: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` am_map.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, i_system.h, m_cheat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_spec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 946.76 | **LOC:** 1490 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6243%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 211.0)
    * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or...
  * `P_SpawnSpecials` **(I/O & Config Routines)** (Impact: 30.8)
    * *Intent:* // Parses command line parameters.
  * `P_PlayerInSpecialSector` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* // // P_PlayerInSpecialSector // Called every tic frame // that the player origin is in a special se...
  * `P_UpdateSpecials` **(I/O & Config Routines)** (Impact: 20.6)
  * `P_FindNextHighestFloor` **(Compute Cores)** (Impact: 20.2)
    * *Intent:* // // P_FindNextHighestFloor // FIND NEXT HIGHEST FLOOR IN SURROUNDING SECTORS // Note: this should ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 177`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 173`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 25`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` deh_main.h, doomdef.h, doomstat.h, g_game.h, i_system.h, m_argv.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 931.36 | **LOC:** 923 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1644%), Tech Debt (17.2662%)
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Compute Cores)** (Impact: 180.9)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_GiveAmmo` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* // // GET STUFF // // // P_GiveAmmo // Num is the number of clip loads, // not the individual count ...
  * `P_KillMobj` **(Compute Cores)** (Impact: 46.5)
    * *Intent:* // // KillMobj //
  * `P_GiveWeapon` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* // // P_GiveWeapon // The weapon name may have a MF_DROPPED flag ored in. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 142`, `args: 49`, `func_start: 9`
* *Risk/State:* `state_mutation: 156`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` am_map.h, deh_main.h, deh_misc.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 909.86 | **LOC:** 1449 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5065%), Tech Debt (35.4841%)
**Top Internal Functions/Classes:**
  * `PTR_ShootTraverse` **(Compute Cores)** (Impact: 39.2)
    * *Intent:* // // PTR_ShootTraverse //
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 34.5)
    * *Intent:* // // PIT_CheckThing //
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* // // P_TryMove // Attempt to move to a new position, // crossing special lines unless MF_TELEPORT i...
  * `PTR_AimTraverse` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* // // PTR_AimTraverse // Sets linetaget and aimslope when a target is aimed at. //
  * `PIT_CheckLine` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* // // PIT_CheckLine // Adjusts tmfloorz and tmceilingz as lines are contacted //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 179`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 220`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 22`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` deh_misc.h, doomdef.h, doomstat.h, i_system.h, m_argv.h, m_bbox.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 901.4 | **LOC:** 1892 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.5235%), Tech Debt (26.6428%)
**Top Internal Functions/Classes:**
  * `P_UnArchiveSpecials` **(I/O & Config Routines)** (Impact: 18.9)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_ArchiveSpecials` **(I/O & Config Routines)** (Impact: 17.2)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `saveg_read_player_t` **(Compute Cores)** (Impact: 16.3)
    * *Intent:* // // player_t //
  * `saveg_write_player_t` **(Compute Cores)** (Impact: 16.3)
  * `P_UnArchiveThinkers` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* // // P_UnArchiveThinkers //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 108`, `args: 53`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 299`, `dead_code: 128`, `unreferenced_by_name: 14`
* *Architecture:* `io: 2`, `api: 15`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` deh_main.h, doomstat.h, dstrings.h, g_game.h, i_system.h, m_misc.h, p_local.h, p_saveg.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 888.22 | **LOC:** 1841 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.3053%), Tech Debt (16.7673%)
**Top Internal Functions/Classes:**
  * `D_DoomMain` **(Compute Cores)** (Impact: 100.0)
    * *Intent:* #endif // // D_DoomMain //
  * `D_Display` **(Compute Cores)** (Impact: 52.0)
  * `InitGameVersion` **(I/O & Config Routines)** (Impact: 30.1)
    * *Intent:* // Initialize the game version
  * `D_DoAdvanceDemo` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* // // This cycles through the demo sequences. // FIXME - version dependend demo numbers? //
  * `D_SetGameDescription` **(I/O & Config Routines)** (Impact: 21.9)
    * *Intent:* // Set the gamedescription string
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 164 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 136`, `args: 48`, `func_start: 21`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 182`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 24`, `import: 42`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` am_map.h, config.h, ctype.h, d_iwad.h, d_main.h, deh_main.h, doomdef.h, doomfeatures.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 886.08 | **LOC:** 1050 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4054%), Tech Debt (67.0624%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 68.6)
    * *Intent:* // // P_XYMovement // #define STOPSPEED 0x1000 #define FRICTION 0xe800
  * `P_ZMovement` **(Compute Cores)** (Impact: 50.6)
    * *Intent:* // // P_ZMovement //
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 43.1)
    * *Intent:* // // P_SpawnMapThing // The fields of the mapthing should // already be in host byte order. //
  * `P_MobjThinker` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* // // P_MobjThinker //
  * `P_SpawnMobj` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* // // P_SpawnMobj //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 56`, `args: 19`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `dead_code: 2`, `fragile_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 20`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` doomdef.h, doomstat.h, hu_stuff.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 867.6 | **LOC:** 980 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.8396%), Tech Debt (12.7696%)
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 50.6)
  * `R_ProjectSprite` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 30.6)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawPSprite` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // // R_DrawPSprite //
  * `R_InstallSpriteLump` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 51`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 212`, `dead_code: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` deh_main.h, doomdef.h, doomstat.h, i_swap.h, i_system.h, r_local.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 843.24 | **LOC:** 933 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.7382%), Tech Debt (90.3844%)
**Top Internal Functions/Classes:**
  * `V_CopyRect` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* // // V_CopyRect //
  * `V_DrawPatch` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
  * `V_DrawPatchFlipped` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e....
  * `WritePNGfile` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `V_DrawShadowedPatch` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* // // V_DrawShadowedPatch // // Masks a column based masked pic to the screen. //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 170 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 42`, `args: 30`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 196`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 28`, `import: 15`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` config.h, deh_str.h, doomtype.h, i_swap.h, i_system.h, i_video.h, m_bbox.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 826.94 | **LOC:** 853 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.3775%), Tech Debt (19.7323%)
**Top Internal Functions/Classes:**
  * `P_SetupLevel` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* // // P_SetupLevel //
  * `P_LoadLineDefs` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // // P_LoadLineDefs // Also counts secret lines for intermissions. //
  * `P_LoadThings` **(Compute Cores)** (Impact: 23.8)
    * *Intent:* // // P_LoadThings //
  * `P_GroupLines` **(I/O & Config Routines)** (Impact: 21.6)
    * *Intent:* // // P_GroupLines // Builds sector line lists and subsector sector numbers. // Finds block bounding...
  * `PadRejectArray` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* // Pad the REJECT lump with extra data when the lump is too small, // to simulate a REJECT buffer ov...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 639
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 28`, `args: 17`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 239`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 14`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` deh_main.h, doomdef.h, doomstat.h, g_game.h, i_swap.h, i_system.h, m_argv.h, m_bbox.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/st_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 821.16 | **LOC:** 1417 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.6202%), Tech Debt (23.6657%)
**Top Internal Functions/Classes:**
  * `ST_Responder` **(Compute Cores)** (Impact: 108.8)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` **(I/O & Config Routines)** (Impact: 42.5)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` **(I/O & Config Routines)** (Impact: 19.2)
  * `ST_updateWidgets` **(I/O & Config Routines)** (Impact: 15.2)
  * `ST_loadUnloadGraphics` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* // Iterates through all graphics to be loaded or unloaded, along with // the variable they use, invo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 93`, `args: 57`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `dead_code: 6`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 22`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` am_map.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 777.84 | **LOC:** 744 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5939%), Tech Debt (29.4676%)
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 138.1)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 36.1)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 552
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 18`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` doomdef.h, doomstat.h, i_system.h, r_local.h, r_sky.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 758.72 | **LOC:** 1002 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1445%), Tech Debt (18.2197%)
**Top Internal Functions/Classes:**
  * `P_PathTraverse` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* // // P_PathTraverse // Traces a line from x1,y1 to x2,y2, // calling the traverser function for eac...
  * `P_UnsetThingPosition` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* // // THING POSITION SETTING // // // P_UnsetThingPosition // Unlinks a thing from block map and sec...
  * `P_PointOnDivlineSide` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* // // P_PointOnDivlineSide // Returns 0 or 1. //
  * `PIT_AddLineIntercepts` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* // // PIT_AddLineIntercepts. // Looks for lines in the given block // that intercept the given trace...
  * `P_BoxOnLineSide` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 460
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 114`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 160`, `dead_code: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` doomdef.h, doomstat.h, m_bbox.h, p_local.h, r_state.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_data.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 657.06 | **LOC:** 910 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.0486%), Tech Debt (18.4356%)
**Top Internal Functions/Classes:**
  * `R_InitTextures` **(Compute Cores)** (Impact: 25.8)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `R_PrecacheLevel` **(I/O & Config Routines)** (Impact: 20.4)
  * `R_GenerateLookup` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* // // R_GenerateLookup //
  * `R_GenerateComposite` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_DrawColumnInCache` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* // for a column directory and any new columns. // The directory will simply point inside other patch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 38`, `args: 37`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 190`, `dead_code: 5`, `unreferenced_by_name: 5`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` deh_main.h, doomdef.h, doomstat.h, i_swap.h, i_system.h, m_misc.h, p_local.h, r_data.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 644.38 | **LOC:** 547 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.8289%), Tech Debt (12.8169%)
**Top Internal Functions/Classes:**
  * `T_MovePlane` **(Many-Argument Workhorses)** (Impact: 81.9)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_DoFloor` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `EV_BuildStairs` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 56`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 148`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomdef.h, doomstat.h, p_local.h, r_state.h, s_sound.h, sounds.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 600.72 | **LOC:** 892 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8381%), Tech Debt (31.1875%)
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
* *Amplified Cascading Flux:* 127 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 60`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 143`, `dead_code: 3`, `unreferenced_by_name: 9`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` d_loop.h, doomdef.h, m_bbox.h, m_menu.h, math.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_draw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 549.48 | **LOC:** 976 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.8855%), Tech Debt (61.7356%)
**Top Internal Functions/Classes:**
  * `R_FillBackScreen` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* // // R_FillBackScreen // Fills the back screen with a pattern // for variable screen sizes // Also ...
  * `R_DrawFuzzColumnLow` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* // low detail mode version
  * `R_DrawFuzzColumn` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* // // Framebuffer postprocessing. // Creates a fuzzy image by copying pixels // from adjacent ones t...
  * `R_InitBuffer` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* // // R_InitBuffer // Creats lookup tables that avoid // multiplies and other hazzles // for getting...
  * `R_DrawTranslatedColumnLow` **(I/O & Config Routines)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 32`, `args: 24`, `func_start: 13`
* *Risk/State:* `state_mutation: 136`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` deh_main.h, doomdef.h, doomstat.h, i_system.h, r_local.h, v_video.h, w_wad.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 540.84 | **LOC:** 889 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.901%), Tech Debt (88.7193%)
**Top Internal Functions/Classes:**
  * `P_CheckAmmo` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* #include "p_pspr.h" #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM...
  * `A_Saw` **(Compute Cores)** (Impact: 16.0)
    * *Intent:* // // A_Saw //
  * `A_ReFire` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* // // A_ReFire // The player can re-fire the weapon // without lowering it entirely. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 51`, `args: 31`, `func_start: 31`
* *Risk/State:* `state_mutation: 102`, `dead_code: 1`, `unreferenced_by_name: 24`
* *Architecture:* `api: 30`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` d_event.h, deh_misc.h, doomdef.h, doomstat.h, m_random.h, p_local.h, p_pspr.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/f_finale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 530.06 | **LOC:** 719 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.2814%), Tech Debt (40.8706%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` **(Compute Cores)** (Impact: 52.0)
    * *Intent:* // // F_CastTicker //
  * `F_Ticker` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* // // F_Ticker //
  * `F_CastPrint` **(Compute Cores)** (Impact: 15.2)
  * `F_TextWrite` **(I/O & Config Routines)** (Impact: 14.3)
  * `F_BunnyScroll` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* // // F_BunnyScroll //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 99`, `args: 26`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ctype.h, d_main.h, deh_main.h, doomstat.h, dstrings.h, hu_stuff.h, i_swap.h, i_system.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_doors.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 488.82 | **LOC:** 779 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2665%), Tech Debt (15.2916%)
**Top Internal Functions/Classes:**
  * `EV_VerticalDoor` **(Compute Cores)** (Impact: 92.0)
    * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
  * `T_VerticalDoor` **(Compute Cores)** (Impact: 60.2)
    * *Intent:* #endif // // VERTICAL DOORS // // // T_VerticalDoor //
  * `EV_DoLockedDoor` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* // // EV_DoLockedDoor // Move a locked door up/down //
  * `EV_DoDoor` **(Compute Cores)** (Impact: 28.2)
  * `P_SpawnDoorRaiseIn5Mins` **(State Mutators)** (Impact: 2.9)
    * *Intent:* // // Spawn a door that opens after 5 minutes //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 62`, `args: 18`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `dead_code: 3`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` deh_main.h, doomdef.h, doomstat.h, dstrings.h, p_local.h, r_state.h, s_sound.h, sounds.h...
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

- `src/doomdef.h` -> **Severity: 0.136** (Bridge: 0.0037 * Flux: 36.8296%)
- `src/d_player.h` -> **Severity: 0.078** (Bridge: 0.006 * Flux: 12.8734%)
- `src/p_mobj.h` -> **Severity: 0.039** (Bridge: 0.0029 * Flux: 13.2329%)
- `src/d_event.h` -> **Severity: 0.006** (Bridge: 0.0002 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/doomtype.h` -> **Severity: 27.316** (Embedded: 0.4231 * Error Risk: 64.5656%)
- `src/doomdef.h` -> **Severity: 14.112** (Embedded: 0.2308 * Error Risk: 61.1312%)
- `src/d_event.h` -> **Severity: 10.274** (Embedded: 0.1642 * Error Risk: 62.5811%)
- `src/d_player.h` -> **Severity: 7.443** (Embedded: 0.1299 * Error Risk: 57.3004%)
- `src/p_mobj.h` -> **Severity: 7.047** (Embedded: 0.1222 * Error Risk: 57.6709%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/am_map.c` -> **Severity: 249.1** (Blast Radius: 2.491 * Doc Risk: 100.0%)
- `src/d_event.c` -> **Severity: 249.1** (Blast Radius: 2.491 * Doc Risk: 100.0%)
- `src/d_iwad.c` -> **Severity: 249.1** (Blast Radius: 2.491 * Doc Risk: 100.0%)
- `src/d_loop.c` -> **Severity: 249.1** (Blast Radius: 2.491 * Doc Risk: 100.0%)
- `src/d_main.c` -> **Severity: 249.1** (Blast Radius: 2.491 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
