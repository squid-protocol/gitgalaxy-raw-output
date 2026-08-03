# ARCHITECTURAL_BRIEF: loony_ascii_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/loony_ascii_doom` |
| **Timestamp** | `2026-08-03T19:05:24.009457+00:00` |
| **Scan Duration** | `0.79s` |
| **Git Branch** | `master` |
| **Git Commit** | `b5188d7c9c4da6c81264a7803e8725ac3df2cfea` |
| **Git Remote** | `https://github.com/wojciech-graj/doom-ascii.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 179 malicious artifacts.

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
| Total Artifacts | 193 |
| Analyzed Artifacts (Scanned) | 182 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 27545 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 94.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3491 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1897 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7269 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 177 | 27331 | 97.3% |
| MAKEFILE | 2 | 128 | 1.1% |
| YAML | 1 | 86 | 0.5% |
| MARKDOWN | 1 | 0 | 0.5% |
| XML | 1 | 0 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.298`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 123 | 67.6% |
| file_cluster_13 | 56 | 30.8% |
| file_cluster_9 | 2 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 4663 LOC), 1x Excluded (Embedded Array/Matrix Payload: 17673 commas in 2228 LOC)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Unsupported Format (.cfg)
- `.desktop`: 1x Unsupported Format (.desktop)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1332 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 95.3 | 31.3 | 6.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.6 | 24.9 | 6.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.6 | 10.0 | 10.5 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.6 | 13.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.0 | 3.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 75.3 | 98.5 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 28.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 4.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 9.9 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Makefile` (Hits: 10)
- `src/g_game.c` (Hits: 7)
- `src/m_argv.c` (Hits: 4)

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

- `M_Responder` (@ `src/m_menu.c`) -> Impact: **517.3** | LOC: 476
- `PrintDehackedBanners` (@ `src/d_main.c`) -> Impact: **467.3** | LOC: 522
- `EV_VerticalDoor` (@ `src/p_doors.c`) -> Impact: **414.8** | LOC: 176
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `A_Fire` (@ `src/p_enemy.c`) -> Impact: **348.9** | LOC: 679
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `G_CheckSpot` (@ `src/g_game.c`) -> Impact: **295.9** | LOC: 99
  * *Intent:* #define SLOWTURNTICS 6 #define NUMKEYS 256 #define MAX_JOY_BUTTONS 20
- `P_SpawnSpecials` (@ `src/p_spec.c`) -> Impact: **236.2** | LOC: 116
- `P_CrossSpecialLine` (@ `src/p_spec.c`) -> Impact: **215.8** | LOC: 115
  * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or by timed thinkers. // // // P_CrossSpecialLine - ...
- `P_UseSpecialLine` (@ `src/p_switch.c`) -> Impact: **194.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `ST_Responder` (@ `src/st_stuff.c`) -> Impact: **188.7** | LOC: 224
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `P_CrossSubsector` (@ `src/p_sight.c`) -> Impact: **181.5** | LOC: 110
  * *Intent:* // // P_CrossSubsector // Returns true // if strace crosses the given subsector successfully. //

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `G_CheckSpot` (@ `src/g_game.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #define SLOWTURNTICS 6 #define NUMKEYS 256 #define MAX_JOY_BUTTONS 20
- `I_Error` (@ `src/i_system.c`) -> **O(2^N) [Recursive]**
- `EV_VerticalDoor` (@ `src/p_doors.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `SpechitOverrun` (@ `src/p_map.c`) -> **O(2^N) [Recursive]**
- `saveg_read8` (@ `src/p_saveg.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Endian-safe integer read/write functions
- `PrintDehackedBanners` (@ `src/d_main.c`) -> **O(2^N) [Recursive]**
- `V_CopyRect` (@ `src/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_CopyRect //
- `V_DrawPatch` (@ `src/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
- `V_DrawPatchFlipped` (@ `src/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e.g. to mirror face. //
- `V_DrawShadowedPatch` (@ `src/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawShadowedPatch // // Masks a column based masked pic to the screen. //

### Highest Data Gravity (Database Complexity)
- `A_Fire` (@ `src/p_enemy.c`) -> DB Complexity: **110**
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `M_Responder` (@ `src/m_menu.c`) -> DB Complexity: **81**
- `EV_DoFloor` (@ `src/p_floor.c`) -> DB Complexity: **76**
  * *Intent:* // // HANDLE FLOOR TYPES //
- `I_Scale5x` (@ `src/i_scale.c`) -> DB Complexity: **74**
  * *Intent:* // 5x scale (1600x1000)
- `ST_Responder` (@ `src/st_stuff.c`) -> DB Complexity: **55**
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `I_Scale4x` (@ `src/i_scale.c`) -> DB Complexity: **53**
  * *Intent:* // 4x scale (1280x800)
- `R_RenderSegLoop` (@ `src/r_segs.c`) -> DB Complexity: **53**
  * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for walls. // Can draw or mark the starting pixel of floo...
- `PrintDehackedBanners` (@ `src/d_main.c`) -> DB Complexity: **52**
- `A_Lower` (@ `src/p_pspr.c`) -> DB Complexity: **49**
  * *Intent:* // // A_Lower // Lowers current weapon, // and changes weapon at bottom. //
- `saveg_read_player_t` (@ `src/p_saveg.c`) -> DB Complexity: **47**
  * *Intent:* // // player_t //

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 177 | 36808.9 | 31.27% | 25.24% |
| `__monolith__` | 4 | 623.44 | 30.39% | 0.0% |
| `src/AppDir/usr/share/metainfo` | 1 | 10.52 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/dummy.c` -> **100.0%** Exposure
- `src/m_fixed.c` -> **100.0%** Exposure
- `src/p_setup.h` -> **100.0%** Exposure
- `src/p_tick.c` -> **99.9999%** Exposure
- `src/i_timer.c` -> **99.9997%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/d_loop.c` -> **100.0%** Exposure
- `src/d_main.c` -> **100.0%** Exposure
- `src/d_net.c` -> **100.0%** Exposure
- `src/doomgeneric.c` -> **100.0%** Exposure
- `src/doomstat.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/p_enemy.c` -> **22** Orphaned Functions | **0** Duplicates
- `src/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `src/i_video.c` -> **16** Orphaned Functions | **0** Duplicates
- `src/p_saveg.c` -> **14** Orphaned Functions | **0** Duplicates
- `src/v_video.c` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/p_ceilng.c`** -> AI Confidence: **99.48%**
2. **`src/p_doors.c`** -> AI Confidence: **99.48%**
3. **`src/p_floor.c`** -> AI Confidence: **99.48%**
4. **`src/p_inter.c`** -> AI Confidence: **99.48%**
5. **`src/p_mobj.c`** -> AI Confidence: **99.48%**
6. **`src/p_plats.c`** -> AI Confidence: **99.48%**
7. **`src/p_switch.c`** -> AI Confidence: **99.48%**
8. **`src/r_plane.c`** -> AI Confidence: **99.48%**
9. **`src/r_segs.c`** -> AI Confidence: **99.48%**
10. **`src/r_things.c`** -> AI Confidence: **99.39%**
11. **`src/statdump.c`** -> AI Confidence: **99.39%**
12. **`src/wi_stuff.c`** -> AI Confidence: **99.39%**
13. **`src/f_finale.c`** -> AI Confidence: **99.35%**
14. **`src/r_draw.c`** -> AI Confidence: **99.34%**
15. **`src/d_iwad.c`** -> AI Confidence: **99.31%**
16. **`src/d_loop.c`** -> AI Confidence: **99.31%**
17. **`src/d_main.c`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/d_loop.c` -> **20.0%** Exposure
- `src/d_main.c` -> **20.0%** Exposure
- `src/d_mode.c` -> **20.0%** Exposure
- `src/d_net.c` -> **20.0%** Exposure
- `src/f_finale.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `target.mk` -> **100.0%** Exposure
- `src/d_englsh.h` -> **1.1768%** Exposure
### Raw Memory Manipulation
- `src/sha1.c` -> **9.916%** Exposure
- `src/i_sound.h` -> **7.582%** Exposure
- `src/p_spec.c` -> **2.0461%** Exposure
- `src/doomgeneric_ascii.c` -> **0.2595%** Exposure
- `src/i_system.c` -> **0.0247%** Exposure
### Algorithmic DoS Exposure
- `src/d_loop.c` -> **100.0%** Exposure
- `src/d_main.c` -> **100.0%** Exposure
- `src/d_mode.c` -> **100.0%** Exposure
- `src/d_net.c` -> **100.0%** Exposure
- `src/f_finale.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `917` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/r_draw.c` (C) -> Cumulative Risk: **779.25**
- **Archetype:** `file_cluster_13` (Distance: 14.217 IQR)
- **Magnitude:** 1039.38 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7155%)
- **Heaviest Functions:** `R_FillBackScreen` (Impact: 83.9), `R_DrawSpan` (Impact: 51.0), `R_DrawFuzzColumn` (Impact: 37.4)

### 2. `src/i_video.c` (C) -> Cumulative Risk: **777.85**
- **Archetype:** `file_cluster_13` (Distance: 12.737 IQR)
- **Magnitude:** 286.38 | **LOC:** 355 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9954%)
- **Heaviest Functions:** `I_GetPaletteIndex` (Impact: 41.8), `I_InitGraphics` (Impact: 8.9), `I_FinishUpdate` (Impact: 6.2)

### 3. `src/v_video.c` (C) -> Cumulative Risk: **760.78**
- **Archetype:** `file_cluster_8` (Distance: 13.995 IQR)
- **Magnitude:** 1521.66 | **LOC:** 933 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.4281%)
- **Heaviest Functions:** `V_CopyRect` (Impact: 143.1), `V_DrawPatch` (Impact: 102.8), `V_DrawPatchFlipped` (Impact: 102.8)

### 4. `src/p_saveg.c` (C) -> Cumulative Risk: **760.57**
- **Archetype:** `file_cluster_9` (Distance: 21.327 IQR)
- **Magnitude:** 1248.2 | **LOC:** 1892 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Dead Code (97.0116%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 99.5), `P_UnArchiveSpecials` (Impact: 77.6), `saveg_read8` (Impact: 40.4)

### 5. `src/z_zone.c` (C) -> Cumulative Risk: **747.4**
- **Archetype:** `file_cluster_8` (Distance: 12.991 IQR)
- **Magnitude:** 367.86 | **LOC:** 489 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6914%)
- **Heaviest Functions:** `Z_Free` (Impact: 51.4), `Z_CheckHeap` (Impact: 28.8), `Z_ChangeTag2` (Impact: 28.8)

### 6. `src/m_menu.c` (C) -> Cumulative Risk: **739.67**
- **Archetype:** `file_cluster_13` (Distance: 13.198 IQR)
- **Magnitude:** 1495.2 | **LOC:** 2126 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.5172%)
- **Heaviest Functions:** `M_Responder` (Impact: 517.3), `M_Drawer` (Impact: 77.0), `M_WriteText` (Impact: 24.1)

### 7. `src/p_mobj.c` (C) -> Cumulative Risk: **737.37**
- **Archetype:** `file_cluster_13` (Distance: 13.792 IQR)
- **Magnitude:** 522.32 | **LOC:** 1050 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (91.8192%)
- **Heaviest Functions:** `P_ZMovement` (Impact: 68.8), `P_XYMovement` (Impact: 50.4), `P_SpawnMissile` (Impact: 8.0)

### 8. `src/i_cdmus.c` (C) -> Cumulative Risk: **729.44**
- **Archetype:** `file_cluster_8` (Distance: 12.425 IQR)
- **Magnitude:** 198.88 | **LOC:** 244 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.7504%)
- **Heaviest Functions:** `I_CDMusInit` (Impact: 19.5), `I_CDMusFirstTrack` (Impact: 15.7), `I_CDMusTrackLength` (Impact: 14.2)

### 9. `src/d_net.c` (C) -> Cumulative Risk: **718.88**
- **Archetype:** `file_cluster_13` (Distance: 12.594 IQR)
- **Magnitude:** 224.76 | **LOC:** 282 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (91.5138%)
- **Heaviest Functions:** `D_CheckNetGame` (Impact: 50.5), `InitConnectData` (Impact: 20.2), `RunTic` (Impact: 13.2)

### 10. `src/f_finale.c` (C) -> Cumulative Risk: **711.9**
- **Archetype:** `file_cluster_13` (Distance: 13.242 IQR)
- **Magnitude:** 924.06 | **LOC:** 719 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9045%)
- **Heaviest Functions:** `F_CastTicker` (Impact: 119.4), `F_ArtScreenDrawer` (Impact: 57.0), `F_BunnyScroll` (Impact: 54.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.554 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.39 IQR)
- **Top Global Matches:** file_cluster_8: 13.554, file_cluster_13: 13.682, file_cluster_0: 13.802
- **Magnitude:** 1665.6 | **LOC:** 2007 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (92.0777%), Tech Debt (32.1033%)
**Top Internal Functions/Classes:**
  * `A_Fire` (Impact: 348.9 | O(N^5) | DB: 110)
    * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
  * `P_NewChaseDir` (Impact: 74.3 | O(2^N) | DB: 27)
  * `A_Chase` (Impact: 39.2 | O(N^1) | DB: 10)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `P_RecursiveSound` (Impact: 28.2 | O(2^N) | DB: 8)
  * `P_CheckMissileRange` (Impact: 27.0 | O(N^2) | DB: 5)
    * *Intent:* // // P_CheckMissileRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 193`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 686`, `dead_code: 6`, `orphaned_logic: 22`
* *Architecture:* `api: 263`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` p_local.h, i_system.h, doomstat.h, s_sound.h, m_random.h, stdlib.h, doomdef.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/i_scale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.929 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 13.929, file_cluster_13: 14.15, file_cluster_7: 14.301
- **Magnitude:** 1613.28 | **LOC:** 1453 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 74
- **Risk Profile:** Cognitive Load (59.7714%), Tech Debt (11.9854%)
**Top Internal Functions/Classes:**
  * `I_Stretch5x` (Impact: 39.0 | O(N^3) | DB: 15)
    * *Intent:* // 5x stretch (1600x1200)
  * `I_Stretch4x` (Impact: 26.2 | O(N^2) | DB: 33)
    * *Intent:* // 4x stretch (1280x960)
  * `I_Stretch3x` (Impact: 25.0 | O(N^2) | DB: 27)
    * *Intent:* // 3x stretch (960x720)
  * `I_Stretch2x` (Impact: 23.8 | O(N^2) | DB: 21)
    * *Intent:* // 2x stretch (640x480)
  * `I_Stretch1x` (Impact: 22.6 | O(N^2) | DB: 15)
    * *Intent:* // 1x stretch (320x240)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 102`, `args: 15`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1050`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 121`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` string.h, i_video.h, doomtype.h, m_argv.h, stdlib.h, stdio.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.216 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.274 IQR)
- **Top Global Matches:** file_cluster_8: 13.216, file_cluster_13: 13.434, file_cluster_7: 13.579
- **Magnitude:** 1567.0 | **LOC:** 1830 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (71.675%), Tech Debt (25.3459%)
**Top Internal Functions/Classes:**
  * `WI_loadUnloadData` (Impact: 88.0 | O(N^6) | DB: 14)
  * `WI_updateNetgameStats` (Impact: 78.3 | O(N^1) | DB: 40)
  * `WI_drawOnLnode` (Impact: 69.8 | O(N^5) | DB: 8)
  * `WI_updateDeathmatchStats` (Impact: 46.0 | O(N^1) | DB: 25)
  * `WI_updateStats` (Impact: 44.8 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 111`, `args: 35`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 736`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 159`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` i_system.h, i_swap.h, w_wad.h, s_sound.h, m_random.h, doomstat.h, v_video.h, wi_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.995 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.475 IQR)
- **Top Global Matches:** file_cluster_8: 13.995, file_cluster_13: 14.014, file_cluster_11: 14.323
- **Magnitude:** 1521.66 | **LOC:** 933 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (64.4507%), Tech Debt (87.3855%)
**Top Internal Functions/Classes:**
  * `V_CopyRect` (Impact: 143.1 | O(2^N) | DB: 5)
    * *Intent:* // // V_CopyRect //
  * `V_DrawPatch` (Impact: 102.8 | O(2^N) | DB: 23)
    * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
  * `V_DrawPatchFlipped` (Impact: 102.8 | O(2^N) | DB: 17)
    * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e....
  * `V_DrawShadowedPatch` (Impact: 82.5 | O(2^N) | DB: 22)
    * *Intent:* // // V_DrawShadowedPatch // // Masks a column based masked pic to the screen. //
  * `V_DrawTLPatch` (Impact: 82.2 | O(2^N) | DB: 17)
    * *Intent:* // // V_DrawTLPatch // // Masks a column based translucent masked pic to the screen. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 39`, `args: 21`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 545`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 104`, `import: 15`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` string.h, i_video.h, doomtype.h, config.h, png.h, i_system.h, i_swap.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.198 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_13: 13.198, file_cluster_8: 13.252, file_cluster_11: 13.527
- **Magnitude:** 1495.2 | **LOC:** 2126 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (93.3528%), Tech Debt (65.7778%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 517.3 | O(N^6) | DB: 81)
  * `M_Drawer` (Impact: 77.0 | O(N^6) | DB: 19)
  * `M_WriteText` (Impact: 24.1 | O(N^1) | DB: 11)
  * `M_Init` (Impact: 21.5 | O(N^1) | DB: 15)
  * `M_DrawOPLDev` (Impact: 15.7 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 129`, `args: 25`, `func_start: 28`
* *Risk/State:* `state_mutation: 526`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 158`, `import: 25`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ctype.h, doomstat.h, d_main.h, stdlib.h, doomkeys.h, i_video.h, i_swap.h, m_menu.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_9` (Drift: 21.327 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.514 IQR)
- **Top Global Matches:** file_cluster_9: 21.327, file_cluster_0: 21.334, file_cluster_11: 21.347
- **Magnitude:** 1248.2 | **LOC:** 1892 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (85.851%), Tech Debt (26.6428%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` (Impact: 99.5 | O(N^4) | DB: 4)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `P_UnArchiveSpecials` (Impact: 77.6 | O(N^3) | DB: 19)
    * *Intent:* // // P_UnArchiveSpecials //
  * `saveg_read8` (Impact: 40.4 | O(2^N) | DB: 4)
    * *Intent:* // Endian-safe integer read/write functions
  * `P_UnArchiveThinkers` (Impact: 37.3 | O(N^3) | DB: 11)
    * *Intent:* // // P_UnArchiveThinkers //
  * `saveg_write8` (Impact: 16.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 86`, `args: 23`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 642`, `dead_code: 128`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 92`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` p_local.h, i_system.h, dstrings.h, doomstat.h, p_saveg.h, r_state.h, stdlib.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/d_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.625 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.016 IQR)
- **Top Global Matches:** file_cluster_13: 12.625, file_cluster_8: 12.9, file_cluster_11: 13.13
- **Magnitude:** 1119.9 | **LOC:** 1841 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (70.655%), Tech Debt (16.8211%)
**Top Internal Functions/Classes:**
  * `PrintDehackedBanners` (Impact: 467.3 | O(2^N) | DB: 52)
  * `D_Display` (Impact: 177.8 | O(N^3) | DB: 28)
  * `D_SetGameDescription` (Impact: 70.1 | O(N^4) | DB: 12)
    * *Intent:* // frame syncronous IO operations
  * `D_ProcessEvents` (Impact: 13.7 | O(N^2) | DB: 1)
    * *Intent:* // // D_ProcessEvents // Send all the events of the given timestamp down the responder chain //
  * `D_BindVariables` (Impact: 6.5 | O(N^2) | DB: 6)
    * *Intent:* // // Add configuration file variable bindings. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 69`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 297`, `dead_code: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 70`, `import: 42`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` ctype.h, net_client.h, doomstat.h, p_setup.h, d_main.h, stdlib.h, st_stuff.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.791 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_13: 13.791, file_cluster_8: 13.863, file_cluster_0: 14.092
- **Magnitude:** 1084.56 | **LOC:** 1417 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (89.8813%), Tech Debt (23.6657%)
**Top Internal Functions/Classes:**
  * `ST_Responder` (Impact: 188.7 | O(N^4) | DB: 55)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` (Impact: 80.7 | O(N^2) | DB: 46)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` (Impact: 37.1 | O(N^2) | DB: 14)
  * `ST_updateWidgets` (Impact: 20.1 | O(N^1) | DB: 18)
  * `ST_loadUnloadGraphics` (Impact: 15.5 | O(N^3) | DB: 20)
    * *Intent:* // Iterates through all graphics to be loaded or unloaded, along with // the variable they use, invo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 91`, `args: 20`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 572`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 88`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` doomstat.h, st_stuff.h, stdio.h, i_video.h, doomkeys.h, w_wad.h, s_sound.h, v_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.507 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.345 IQR)
- **Top Global Matches:** file_cluster_13: 14.507, file_cluster_8: 14.583, file_cluster_11: 14.662
- **Magnitude:** 1052.4 | **LOC:** 980 | **CtrlFlow:** 74.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (70.9419%), Tech Debt (12.7696%)
**Top Internal Functions/Classes:**
  * `R_ProjectSprite` (Impact: 49.6 | O(2^N) | DB: 44)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` (Impact: 49.1 | O(N^1) | DB: 26)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_InstallSpriteLump` (Impact: 47.4 | O(2^N) | DB: 13)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
  * `R_DrawSprite` (Impact: 39.4 | O(N^1) | DB: 31)
  * `R_DrawPSprite` (Impact: 21.7 | O(N^1) | DB: 25)
    * *Intent:* // // R_DrawPSprite //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 45`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 629`, `dead_code: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` i_system.h, i_swap.h, w_wad.h, doomstat.h, stdlib.h, doomdef.h, stdio.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_draw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.217 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.076 IQR)
- **Top Global Matches:** file_cluster_13: 14.217, file_cluster_8: 14.236, file_cluster_0: 14.371
- **Magnitude:** 1039.38 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (64.8789%), Tech Debt (96.0301%)
**Top Internal Functions/Classes:**
  * `R_FillBackScreen` (Impact: 83.9 | O(N^6) | DB: 26)
    * *Intent:* // // R_FillBackScreen // Fills the back screen with a pattern // for variable screen sizes // Also ...
  * `R_DrawSpan` (Impact: 51.0 | O(2^N) | DB: 11)
    * *Intent:* // // Draws the actual span.
  * `R_DrawFuzzColumn` (Impact: 37.4 | O(2^N) | DB: 12)
    * *Intent:* // // Framebuffer postprocessing. // Creates a fuzzy image by copying pixels // from adjacent ones t...
  * `R_DrawSpanLow` (Impact: 26.7 | O(N^3) | DB: 13)
    * *Intent:* #endif // // Again.. //
  * `R_DrawColumn` (Impact: 26.4 | O(2^N) | DB: 8)
    * *Intent:* // // A column is a vertical slice/span from a wall texture that, // given the DOOM style restrictio...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 36`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 567`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 9`
* *Architecture:* `api: 123`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` i_system.h, w_wad.h, v_video.h, doomstat.h, doomdef.h, r_local.h, z_zone.h, deh_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.575 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.431 IQR)
- **Top Global Matches:** file_cluster_8: 13.575, file_cluster_13: 13.616, file_cluster_11: 13.824
- **Magnitude:** 1025.82 | **LOC:** 779 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (79.38%), Tech Debt (21.2567%)
**Top Internal Functions/Classes:**
  * `EV_VerticalDoor` (Impact: 414.8 | O(2^N) | DB: 32)
    * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
  * `T_VerticalDoor` (Impact: 63.5 | O(N^1) | DB: 17)
    * *Intent:* #endif // // VERTICAL DOORS // // // T_VerticalDoor //
  * `T_SlidingDoor` (Impact: 25.2 | O(N^1) | DB: 22)
  * `EV_DoDoor` (Impact: 25.0 | O(N^1) | DB: 28)
  * `EV_DoLockedDoor` (Impact: 23.8 | O(N^1) | DB: 4)
    * *Intent:* // // EV_DoLockedDoor // Move a locked door up/down //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 31`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 373`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 70`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` p_local.h, dstrings.h, doomstat.h, s_sound.h, doomdef.h, sounds.h, r_state.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_spec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.127 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.9 IQR)
- **Top Global Matches:** file_cluster_13: 13.127, file_cluster_8: 13.2, file_cluster_11: 13.502
- **Magnitude:** 990.72 | **LOC:** 1490 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (36.3118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_SpawnSpecials` (Impact: 236.2 | O(N^6) | DB: 22)
  * `P_CrossSpecialLine` (Impact: 215.8 | O(N^6) | DB: 28)
    * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or...
  * `P_InitPicAnims` (Impact: 49.0 | O(2^N) | DB: 13)
  * `P_FindNextHighestFloor` (Impact: 41.4 | O(N^6) | DB: 13)
    * *Intent:* // // P_FindNextHighestFloor // FIND NEXT HIGHEST FLOOR IN SURROUNDING SECTORS // Note: this should ...
  * `P_FindMinSurroundingLight` (Impact: 6.2 | O(N^1) | DB: 6)
    * *Intent:* // // Find minimum light from an adjacent sector //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 54`, `args: 6`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 295`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 100`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` p_local.h, i_system.h, doomstat.h, m_argv.h, m_random.h, w_wad.h, stdlib.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.242 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.641 IQR)
- **Top Global Matches:** file_cluster_13: 13.242, file_cluster_8: 13.25, file_cluster_11: 13.582
- **Magnitude:** 924.06 | **LOC:** 719 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (76.5275%), Tech Debt (40.8706%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` (Impact: 119.4 | O(N^1) | DB: 38)
    * *Intent:* // // F_CastTicker //
  * `F_ArtScreenDrawer` (Impact: 57.0 | O(N^5) | DB: 5)
  * `F_BunnyScroll` (Impact: 54.7 | O(N^5) | DB: 11)
    * *Intent:* // // F_BunnyScroll //
  * `F_StartFinale` (Impact: 37.1 | O(N^3) | DB: 14)
    * *Intent:* // // F_StartFinale //
  * `F_TextWrite` (Impact: 29.3 | O(N^1) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 66`, `args: 14`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 394`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ctype.h, i_system.h, dstrings.h, i_swap.h, w_wad.h, v_video.h, s_sound.h, d_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.618 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.345 IQR)
- **Top Global Matches:** file_cluster_8: 13.618, file_cluster_13: 13.655, file_cluster_0: 13.832
- **Magnitude:** 778.72 | **LOC:** 892 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (64.6643%), Tech Debt (31.1875%)
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
* *Structure:* `branch: 82`, `structural_boundaries: 61`, `args: 8`, `func_start: 17`
* *Risk/State:* `state_mutation: 456`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 143`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` m_menu.h, stdlib.h, doomdef.h, math.h, r_sky.h, m_bbox.h, d_loop.h, r_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doomgeneric_ascii.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.715 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.633 IQR)
- **Top Global Matches:** file_cluster_8: 12.715, file_cluster_13: 12.763, file_cluster_11: 13.092
- **Magnitude:** 739.38 | **LOC:** 734 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (95.3261%), Tech Debt (12.5257%)
**Top Internal Functions/Classes:**
  * `DG_DrawFrame` (Impact: 90.2 | O(2^N) | DB: 20)
  * `DG_Init` (Impact: 59.8 | O(2^N) | DB: 18)
  * `convertToDoomKey` (Impact: 49.5 | O(N^1))
  * `DG_ReadInput` (Impact: 41.4 | O(2^N) | DB: 33)
  * `DG_AtExit` (Impact: 11.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 142`, `args: 18`, `func_start: 16`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 282`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 173`, `import: 15`
* *Defense:* `safety: 5`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` unistd.h, time.h, ctype.h, doomkeys.h, string.h, i_system.h, stdint.h, m_argv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.369 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.305 IQR)
- **Top Global Matches:** file_cluster_13: 13.369, file_cluster_8: 13.439, file_cluster_11: 13.687
- **Magnitude:** 732.0 | **LOC:** 1449 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (69.6916%), Tech Debt (41.1651%)
**Top Internal Functions/Classes:**
  * `SpechitOverrun` (Impact: 114.8 | O(2^N) | DB: 8)
  * `PTR_SlideTraverse` (Impact: 50.9 | O(2^N) | DB: 23)
  * `P_CheckPosition` (Impact: 11.4 | O(N^1) | DB: 31)
  * `P_TryMove` (Impact: 10.7 | O(N^1) | DB: 11)
  * `PIT_RadiusAttack` (Impact: 9.8 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 105`, `func_start: 13`
* *Risk/State:* `state_mutation: 356`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 127`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` p_local.h, deh_misc.h, i_system.h, doomstat.h, m_argv.h, m_random.h, s_sound.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.357 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_13: 14.357, file_cluster_8: 14.429, file_cluster_11: 14.505
- **Magnitude:** 694.48 | **LOC:** 547 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (74.1468%), Tech Debt (12.8169%)
**Top Internal Functions/Classes:**
  * `EV_DoFloor` (Impact: 76.8 | O(N^2) | DB: 76)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `T_MovePlane` (Impact: 42.8 | O(N^1) | DB: 32)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_BuildStairs` (Impact: 26.1 | O(N^1) | DB: 38)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` (Impact: 23.2 | O(N^2) | DB: 6)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 28`, `func_start: 4`
* *Risk/State:* `state_mutation: 454`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 63`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` p_local.h, doomstat.h, s_sound.h, doomdef.h, sounds.h, r_state.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.696 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.927 IQR)
- **Top Global Matches:** file_cluster_8: 12.696, file_cluster_13: 12.696, file_cluster_7: 13.12
- **Magnitude:** 691.52 | **LOC:** 671 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (69.3537%), Tech Debt (37.102%)
**Top Internal Functions/Classes:**
  * `S_StartSound` (Impact: 95.2 | O(N^6) | DB: 13)
  * `S_ChangeMusic` (Impact: 56.9 | O(N^6) | DB: 8)
  * `S_UpdateSounds` (Impact: 52.3 | O(N^6) | DB: 9)
    * *Intent:* // // Updates music & sounds //
  * `S_AdjustSoundParams` (Impact: 41.9 | O(N^6) | DB: 11)
    * *Intent:* // // Changes volume and stereo-separation variables // from the norm of a sound effect to be played...
  * `S_GetChannel` (Impact: 37.6 | O(N^4) | DB: 7)
    * *Intent:* // // S_GetChannel : // If none available, return -1. Otherwise channel #. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 40`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` p_local.h, doomtype.h, i_system.h, i_sound.h, doomstat.h, s_sound.h, doomfeatures.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_data.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.858 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_0: 14.375, file_cluster_8: 14.376
- **Magnitude:** 665.1 | **LOC:** 910 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (61.3643%), Tech Debt (19.5342%)
**Top Internal Functions/Classes:**
  * `R_GenerateLookup` (Impact: 44.0 | O(2^N) | DB: 26)
    * *Intent:* // // R_GenerateLookup //
  * `R_PrecacheLevel` (Impact: 34.9 | O(N^1) | DB: 39)
  * `R_GenerateComposite` (Impact: 27.1 | O(N^2) | DB: 17)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_InitTextures` (Impact: 20.8 | O(N^2) | DB: 34)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `GenerateTextureHashTable` (Impact: 10.5 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 26`, `args: 7`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 364`, `dead_code: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 134`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` p_local.h, i_system.h, i_swap.h, w_wad.h, doomstat.h, r_data.h, doomdef.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.221 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.469 IQR)
- **Top Global Matches:** file_cluster_13: 13.221, file_cluster_11: 13.718, file_cluster_0: 13.754
- **Magnitude:** 641.18 | **LOC:** 2304 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (86.4845%), Tech Debt (24.3752%)
**Top Internal Functions/Classes:**
  * `G_CheckSpot` (Impact: 295.9 | O(2^N) | DB: 21)
    * *Intent:* #define SLOWTURNTICS 6 #define NUMKEYS 256 #define MAX_JOY_BUTTONS 20
  * `G_InitNew` (Impact: 33.8 | O(N^4) | DB: 20)
  * `G_NextWeapon` (Impact: 26.0 | O(N^3) | DB: 14)
  * `G_DoNewGame` (Impact: 2.4 | O(N^1) | DB: 12)
  * `G_ExitLevel` (Impact: 2.0 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 82`, `args: 15`, `func_start: 8`
* *Risk/State:* `state_mutation: 189`, `dead_code: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 82`, `import: 36`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` doomstat.h, p_setup.h, d_main.h, stdlib.h, st_stuff.h, r_sky.h, f_finale.h, doomkeys.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/i_system.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.699 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.245 IQR)
- **Top Global Matches:** file_cluster_13: 12.699, file_cluster_8: 12.823, file_cluster_7: 13.238
- **Magnitude:** 628.68 | **LOC:** 575 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (65.9887%), Tech Debt (35.1953%)
**Top Internal Functions/Classes:**
  * `I_Error` (Impact: 175.2 | O(2^N) | DB: 8)
  * `I_GetMemoryValue` (Impact: 115.8 | O(N^6) | DB: 16)
    * *Intent:* // Read Access Violation emulation. // // From PrBoom+, by entryway. // // C:\>debug // -d 0:0 // //...
  * `AutoAllocMemory` (Impact: 21.9 | O(N^3) | DB: 4)
    * *Intent:* // Zone memory auto-allocation function that allocates the zone size // by trying progressively smal...
  * `I_ZoneBase` (Impact: 13.6 | O(N^2) | DB: 6)
  * `EscapeShellString` (Impact: 12.3 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 44`, `args: 13`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 190`, `orphaned_logic: 6`
* *Architecture:* `api: 48`, `import: 21`
* *Defense:* `safety: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` CFUserNotification.h, SDL.h, stdlib.h, stdio.h, i_joystick.h, i_video.h, doomtype.h, i_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.058 IQR)
- **Top Global Matches:** file_cluster_8: 10.058, file_cluster_12: 10.3, file_cluster_17: 10.561
- **Magnitude:** 552.96 | **LOC:** 144 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (65.3499%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 23`, `args: 12`, `func_start: 7`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 10`, `api: 8`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` target.mk
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hu_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.288 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.724 IQR)
- **Top Global Matches:** file_cluster_8: 12.288, file_cluster_13: 12.398, file_cluster_7: 12.72
- **Magnitude:** 541.56 | **LOC:** 642 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (66.589%), Tech Debt (27.3149%)
**Top Internal Functions/Classes:**
  * `HU_Responder` (Impact: 126.5 | O(N^5) | DB: 34)
  * `HU_Ticker` (Impact: 54.5 | O(N^2) | DB: 17)
  * `HU_Start` (Impact: 37.6 | O(N^2) | DB: 16)
  * `HU_queueChatChar` (Impact: 5.8 | O(N^1) | DB: 3)
  * `HU_dequeueChatChar` (Impact: 5.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 57`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 241`, `orphaned_logic: 7`
* *Architecture:* `api: 51`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ctype.h, doomkeys.h, i_video.h, m_controls.h, dstrings.h, i_swap.h, hu_lib.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.836 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.829 IQR)
- **Top Global Matches:** file_cluster_13: 13.836, file_cluster_8: 13.911, file_cluster_11: 14.087
- **Magnitude:** 530.32 | **LOC:** 744 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (69.4985%), Tech Debt (15.6698%)
**Top Internal Functions/Classes:**
  * `R_RenderSegLoop` (Impact: 105.1 | O(N^3) | DB: 53)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
  * `R_StoreWallRange` (Impact: 37.7 | O(N^1) | DB: 21)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` (Impact: 21.4 | O(N^1) | DB: 31)
    * *Intent:* // // R_RenderMaskedSegRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 10`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` i_system.h, doomstat.h, stdlib.h, doomdef.h, stdio.h, r_sky.h, r_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.792 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.794 IQR)
- **Top Global Matches:** file_cluster_13: 13.792, file_cluster_8: 13.896, file_cluster_11: 14.088
- **Magnitude:** 522.32 | **LOC:** 1050 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (74.6866%), Tech Debt (91.8192%)
**Top Internal Functions/Classes:**
  * `P_ZMovement` (Impact: 68.8 | O(N^3) | DB: 18)
    * *Intent:* // // P_ZMovement //
  * `P_XYMovement` (Impact: 50.4 | O(N^1) | DB: 25)
    * *Intent:* // // P_XYMovement // #define STOPSPEED 0x1000 #define FRICTION 0xe800
  * `P_SpawnMissile` (Impact: 8.0 | O(N^2) | DB: 11)
  * `P_SpawnPlayerMissile` (Impact: 7.7 | O(N^1) | DB: 17)
  * `P_SpawnBlood` (Impact: 7.1 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 25`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 293`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 57`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` p_local.h, i_system.h, doomstat.h, s_sound.h, m_random.h, st_stuff.h, doomdef.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/r_bsp.c` (C) | Magnitude: 477.08 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 238, indent_spaces: 174, pointers: 74, indent_tabs: 72
- `src/f_finale.c` (C) | Magnitude: 924.06 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 394, indent_spaces: 275, branch: 149, api: 115
- `src/r_draw.c` (C) | Magnitude: 1039.38 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 567, indent_spaces: 283, indent_tabs: 139, api: 123
- `src/m_bbox.c` (C) | Magnitude: 31.42 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 8, branch: 6, api: 6
- `src/doomstat.h` (C) | Magnitude: 80.52 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 64, structural_boundaries: 22, import: 5, macros: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/s_sound.c` (C) | Magnitude: 691.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 347, state_mutation: 220, branch: 86, pointers: 84
- `src/f_wipe.c` (C) | Magnitude: 327.7 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 180, indent_spaces: 92, api: 57, indent_tabs: 45
- `src/v_video.c` (C) | Magnitude: 1521.66 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 545, indent_spaces: 430, pointers: 173, api: 104
- `src/doomdef.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/d_player.h` (C) | Magnitude: 77.64 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, api: 58, structural_boundaries: 16, class_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/p_saveg.c` (C) | Magnitude: 1248.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 642, indent_spaces: 602, pointers: 486, dead_code: 128
- `src/i_system.h` (C) | Magnitude: 29.38 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, api: 14, args: 12, pointers: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/p_mobj.h` -> **Severity: 0.292** (Bridge: 0.0029 * Flux: 99.7778%)
- `src/d_player.h` -> **Severity: 0.185** (Bridge: 0.006 * Flux: 30.6489%)
- `src/doomdef.h` -> **Severity: 0.146** (Bridge: 0.0037 * Flux: 39.6628%)
- `src/d_event.h` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9999%)
- `src/i_sound.h` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 91.306%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/d_event.h` -> **Severity: 4.729** (Embedded: 0.1642 * Error Risk: 28.8073%)
- `src/i_swap.h` -> **Severity: 3.094** (Embedded: 0.0773 * Error Risk: 40.0014%)
- `src/z_zone.h` -> **Severity: 1.812** (Embedded: 0.2155 * Error Risk: 8.4111%)
- `src/p_mobj.h` -> **Severity: 1.8** (Embedded: 0.1222 * Error Risk: 14.728%)
- `src/doomdef.h` -> **Severity: 1.676** (Embedded: 0.2308 * Error Risk: 7.2617%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/net_defs.h` -> **Severity: 2275.3** (Blast Radius: 22.753 * Doc Risk: 100.0%)
- `src/d_mode.h` -> **Severity: 1982.701** (Blast Radius: 19.902 * Doc Risk: 99.6232%)
- `src/doomtype.h` -> **Severity: 1958.028** (Blast Radius: 164.26 * Doc Risk: 11.9203%)
- `src/d_event.h` -> **Severity: 1877.513** (Blast Radius: 21.152 * Doc Risk: 88.7629%)
- `src/d_ticcmd.h` -> **Severity: 1802.7** (Blast Radius: 18.027 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
