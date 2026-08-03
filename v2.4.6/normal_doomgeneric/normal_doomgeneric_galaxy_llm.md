# ARCHITECTURAL_BRIEF: normal_doomgeneric
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_doomgeneric` |
| **Timestamp** | `2026-08-03T19:05:31.767258+00:00` |
| **Scan Duration** | `0.71s` |
| **Git Branch** | `master` |
| **Git Commit** | `3b1d53020373b502035d7d48dede645a7c429feb` |
| **Git Remote** | `https://github.com/ozkl/doomgeneric.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 180 malicious artifacts.

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
| Total Artifacts | 211 |
| Analyzed Artifacts (Scanned) | 182 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 29 |
| Total LOC | 28177 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 86.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3689 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2081 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7069 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 180 | 28177 | 98.9% |
| PLAINTEXT | 1 | 0 | 0.5% |
| MARKDOWN | 1 | 0 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.2`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 120 | 65.9% |
| file_cluster_13 | 58 | 31.9% |
| file_cluster_9 | 2 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 29*

**Composition by Extension & Reason:**
- `.c`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 64 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4663 LOC)
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1332 LOC), 1x Excluded (Machine-Generated Source Code Signature: 72 LOC)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 25 exceeds 500 chars)
- `.sln`: 1x Excluded (Unsupported Extension: '.sln')
- `.djgpp`: 1x Excluded (Unsupported Extension: '.djgpp')
- `.emscripten`: 1x Excluded (Unsupported Extension: '.emscripten')
- `.freebsd`: 1x Excluded (Unsupported Extension: '.freebsd')
- `.linuxvt`: 1x Excluded (Unsupported Extension: '.linuxvt')
- `.sdl`: 1x Excluded (Unsupported Extension: '.sdl')
- `.soso`: 1x Excluded (Unsupported Extension: '.soso')
- `.sosox`: 1x Excluded (Unsupported Extension: '.sosox')
- `.vcxproj`: 1x Excluded (Unsupported Extension: '.vcxproj')
- `.filters`: 1x Excluded (Unsupported Extension: '.filters')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.5 | 33.6 | 6.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.6 | 26.3 | 7.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 25.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.6 | 9.8 | 10.4 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.5 | 32.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 95.6 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.5 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 76.2 | 98.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 5.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 1.2 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 9.9 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doomgeneric/i_sdlsound.c` (Hits: 16)
- `doomgeneric/doomgeneric_linuxvt.c` (Hits: 12)
- `doomgeneric/g_game.c` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomtype.h** (`doomgeneric/doomtype.h`) — 55 inbound connections
2. **i_system.h** (`doomgeneric/i_system.h`) — 43 inbound connections
3. **z_zone.h** (`doomgeneric/z_zone.h`) — 42 inbound connections
4. **doomdef.h** (`doomgeneric/doomdef.h`) — 38 inbound connections
5. **doomstat.h** (`doomgeneric/doomstat.h`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`doomgeneric/d_main.c`) — 42 outbound dependencies
2. **g_game.c** (`doomgeneric/g_game.c`) — 36 outbound dependencies
3. **m_menu.c** (`doomgeneric/m_menu.c`) — 25 outbound dependencies
4. **i_input.c** (`doomgeneric/i_input.c`) — 24 outbound dependencies
5. **st_stuff.c** (`doomgeneric/st_stuff.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `M_Responder` (@ `doomgeneric/m_menu.c`) -> Impact: **517.3** | LOC: 476
- `PrintDehackedBanners` (@ `doomgeneric/d_main.c`) -> Impact: **467.4** | LOC: 524
- `EV_VerticalDoor` (@ `doomgeneric/p_doors.c`) -> Impact: **414.8** | LOC: 176
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `A_Fire` (@ `doomgeneric/p_enemy.c`) -> Impact: **348.9** | LOC: 679
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `G_CheckSpot` (@ `doomgeneric/g_game.c`) -> Impact: **295.9** | LOC: 99
  * *Intent:* #define SLOWTURNTICS 6 #define NUMKEYS 256 #define MAX_JOY_BUTTONS 20
- `DG_DrawFrame` (@ `doomgeneric/doomgeneric_allegro.c`) -> Impact: **240.3** | LOC: 337
- `mus2mid` (@ `doomgeneric/mus2mid.c`) -> Impact: **212.0** | LOC: 250
- `P_UseSpecialLine` (@ `doomgeneric/p_switch.c`) -> Impact: **194.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `ST_Responder` (@ `doomgeneric/st_stuff.c`) -> Impact: **188.7** | LOC: 224
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `convertToDoomKey` (@ `doomgeneric/doomgeneric_linuxvt.c`) -> Impact: **184.2** | LOC: 324
  * *Intent:* #undef KEY_ENTER #undef KEY_BACKSPACE #undef KEY_MINUS #undef KEY_F1 #undef KEY_F2 #undef KEY_F3 #undef KEY_F4 #undef KEY_F5 #undef KEY_F6 #undef KEY_...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `G_CheckSpot` (@ `doomgeneric/g_game.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #define SLOWTURNTICS 6 #define NUMKEYS 256 #define MAX_JOY_BUTTONS 20
- `I_Error` (@ `doomgeneric/i_system.c`) -> **O(2^N) [Recursive]**
- `AllocateMIDIChannel` (@ `doomgeneric/mus2mid.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Allocate a free MIDI channel.
- `EV_VerticalDoor` (@ `doomgeneric/p_doors.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
- `SpechitOverrun` (@ `doomgeneric/p_map.c`) -> **O(2^N) [Recursive]**
- `saveg_read8` (@ `doomgeneric/p_saveg.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // Endian-safe integer read/write functions
- `PrintDehackedBanners` (@ `doomgeneric/d_main.c`) -> **O(2^N) [Recursive]**
- `V_CopyRect` (@ `doomgeneric/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_CopyRect //
- `V_DrawPatch` (@ `doomgeneric/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
- `V_DrawPatchFlipped` (@ `doomgeneric/v_video.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e.g. to mirror face. //

### Highest Data Gravity (Database Complexity)
- `A_Fire` (@ `doomgeneric/p_enemy.c`) -> DB Complexity: **110**
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `convertToDoomKey` (@ `doomgeneric/doomgeneric_linuxvt.c`) -> DB Complexity: **98**
  * *Intent:* #undef KEY_ENTER #undef KEY_BACKSPACE #undef KEY_MINUS #undef KEY_F1 #undef KEY_F2 #undef KEY_F3 #undef KEY_F4 #undef KEY_F5 #undef KEY_F6 #undef KEY_...
- `M_Responder` (@ `doomgeneric/m_menu.c`) -> DB Complexity: **81**
- `EV_DoFloor` (@ `doomgeneric/p_floor.c`) -> DB Complexity: **76**
  * *Intent:* // // HANDLE FLOOR TYPES //
- `I_Scale5x` (@ `doomgeneric/i_scale.c`) -> DB Complexity: **74**
  * *Intent:* // 5x scale (1600x1000)
- `DG_DrawFrame` (@ `doomgeneric/doomgeneric_allegro.c`) -> DB Complexity: **73**
- `WriteWAV` (@ `doomgeneric/i_sdlsound.c`) -> DB Complexity: **58**
  * *Intent:* // Lock a sound, to indicate that it may not be freed.
- `ST_Responder` (@ `doomgeneric/st_stuff.c`) -> DB Complexity: **55**
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `I_Scale4x` (@ `doomgeneric/i_scale.c`) -> DB Complexity: **53**
  * *Intent:* // 4x scale (1280x800)
- `R_RenderSegLoop` (@ `doomgeneric/r_segs.c`) -> DB Complexity: **53**
  * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for walls. // Can draw or mark the starting pixel of floo...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `doomgeneric` | 180 | 38497.14 | 33.6% | 27.02% |
| `__monolith__` | 2 | 3.14 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `doomgeneric/dummy.c` -> **100.0%** Exposure
- `doomgeneric/m_fixed.c` -> **100.0%** Exposure
- `doomgeneric/p_setup.h` -> **100.0%** Exposure
- `doomgeneric/p_tick.c` -> **99.9999%** Exposure
- `doomgeneric/i_timer.c` -> **99.9997%** Exposure
### Highest State Flux (Mutation/Volatility)
- `doomgeneric/d_loop.c` -> **100.0%** Exposure
- `doomgeneric/d_main.c` -> **100.0%** Exposure
- `doomgeneric/d_net.c` -> **100.0%** Exposure
- `doomgeneric/doomgeneric_allegro.c` -> **100.0%** Exposure
- `doomgeneric/doomgeneric_emscripten.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `doomgeneric/p_enemy.c` -> **22** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_video.c` -> **16** Orphaned Functions | **0** Duplicates
- `doomgeneric/p_saveg.c` -> **14** Orphaned Functions | **0** Duplicates
- `doomgeneric/v_video.c` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`doomgeneric/doomgeneric_allegro.c`** -> AI Confidence: **99.48%**
2. **`doomgeneric/doomgeneric_emscripten.c`** -> AI Confidence: **99.48%**
3. **`doomgeneric/doomgeneric_sdl.c`** -> AI Confidence: **99.48%**
4. **`doomgeneric/doomgeneric_sosox.c`** -> AI Confidence: **99.48%**
5. **`doomgeneric/p_ceilng.c`** -> AI Confidence: **99.48%**
6. **`doomgeneric/p_doors.c`** -> AI Confidence: **99.48%**
7. **`doomgeneric/p_floor.c`** -> AI Confidence: **99.48%**
8. **`doomgeneric/p_inter.c`** -> AI Confidence: **99.48%**
9. **`doomgeneric/p_mobj.c`** -> AI Confidence: **99.48%**
10. **`doomgeneric/p_plats.c`** -> AI Confidence: **99.48%**
11. **`doomgeneric/p_switch.c`** -> AI Confidence: **99.48%**
12. **`doomgeneric/r_plane.c`** -> AI Confidence: **99.48%**
13. **`doomgeneric/r_segs.c`** -> AI Confidence: **99.48%**
14. **`doomgeneric/d_main.c`** -> AI Confidence: **99.39%**
15. **`doomgeneric/doomgeneric_linuxvt.c`** -> AI Confidence: **99.39%**
16. **`doomgeneric/f_finale.c`** -> AI Confidence: **99.39%**
17. **`doomgeneric/i_endoom.c`** -> AI Confidence: **99.39%**
18. **`doomgeneric/r_things.c`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `doomgeneric/d_loop.c` -> **20.0%** Exposure
- `doomgeneric/d_main.c` -> **20.0%** Exposure
- `doomgeneric/d_mode.c` -> **20.0%** Exposure
- `doomgeneric/d_net.c` -> **20.0%** Exposure
- `doomgeneric/doomgeneric_emscripten.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `doomgeneric/d_englsh.h` -> **1.1768%** Exposure
### Raw Memory Manipulation
- `doomgeneric/sha1.c` -> **9.916%** Exposure
- `doomgeneric/i_sound.h` -> **7.169%** Exposure
- `doomgeneric/i_sdlsound.c` -> **1.2967%** Exposure
- `doomgeneric/i_system.c` -> **0.0233%** Exposure
- `doomgeneric/i_sdlmusic.c` -> **0.0212%** Exposure
### Algorithmic DoS Exposure
- `doomgeneric/d_loop.c` -> **100.0%** Exposure
- `doomgeneric/d_main.c` -> **100.0%** Exposure
- `doomgeneric/d_mode.c` -> **100.0%** Exposure
- `doomgeneric/d_net.c` -> **100.0%** Exposure
- `doomgeneric/doomgeneric_emscripten.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1018` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `doomgeneric/i_video.c` (C) -> Cumulative Risk: **800.33**
- **Archetype:** `file_cluster_13` (Distance: 13.361 IQR)
- **Magnitude:** 496.8 | **LOC:** 496 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9804%)
- **Heaviest Functions:** `I_InitGraphics` (Impact: 80.8), `I_FinishUpdate` (Impact: 51.0), `I_GetPaletteIndex` (Impact: 41.8)

### 2. `doomgeneric/doomgeneric_sosox.c` (C) -> Cumulative Risk: **784.0**
- **Archetype:** `file_cluster_13` (Distance: 12.821 IQR)
- **Magnitude:** 438.74 | **LOC:** 248 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `convert_to_doom_keyx` (Impact: 158.0), `DG_DrawFrame` (Impact: 59.8), `DG_GetKey` (Impact: 8.8)

### 3. `doomgeneric/r_draw.c` (C) -> Cumulative Risk: **776.34**
- **Archetype:** `file_cluster_13` (Distance: 14.217 IQR)
- **Magnitude:** 1039.38 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7155%)
- **Heaviest Functions:** `R_FillBackScreen` (Impact: 83.9), `R_DrawSpan` (Impact: 51.0), `R_DrawFuzzColumn` (Impact: 37.4)

### 4. `doomgeneric/v_video.c` (C) -> Cumulative Risk: **760.78**
- **Archetype:** `file_cluster_8` (Distance: 13.995 IQR)
- **Magnitude:** 1521.66 | **LOC:** 933 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.4281%)
- **Heaviest Functions:** `V_CopyRect` (Impact: 143.1), `V_DrawPatch` (Impact: 102.8), `V_DrawPatchFlipped` (Impact: 102.8)

### 5. `doomgeneric/p_saveg.c` (C) -> Cumulative Risk: **759.2**
- **Archetype:** `file_cluster_9` (Distance: 21.332 IQR)
- **Magnitude:** 1248.2 | **LOC:** 1892 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Dead Code (95.6428%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 99.5), `P_UnArchiveSpecials` (Impact: 77.6), `saveg_read8` (Impact: 40.4)

### 6. `doomgeneric/doomgeneric_sdl.c` (C) -> Cumulative Risk: **753.84**
- **Archetype:** `file_cluster_13` (Distance: 12.276 IQR)
- **Magnitude:** 291.66 | **LOC:** 211 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9945%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 108.0), `handleKeyInput` (Impact: 7.0), `DG_GetKey` (Impact: 6.1)

### 7. `doomgeneric/z_zone.c` (C) -> Cumulative Risk: **747.4**
- **Archetype:** `file_cluster_8` (Distance: 12.991 IQR)
- **Magnitude:** 367.86 | **LOC:** 489 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6914%)
- **Heaviest Functions:** `Z_Free` (Impact: 51.4), `Z_CheckHeap` (Impact: 28.8), `Z_ChangeTag2` (Impact: 28.8)

### 8. `doomgeneric/doomgeneric_emscripten.c` (C) -> Cumulative Risk: **741.19**
- **Archetype:** `file_cluster_13` (Distance: 12.096 IQR)
- **Magnitude:** 283.48 | **LOC:** 220 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9916%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 108.0), `handleKeyInput` (Impact: 7.1), `DG_GetKey` (Impact: 6.2)

### 9. `doomgeneric/m_menu.c` (C) -> Cumulative Risk: **737.39**
- **Archetype:** `file_cluster_13` (Distance: 13.204 IQR)
- **Magnitude:** 1495.2 | **LOC:** 2126 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.5172%)
- **Heaviest Functions:** `M_Responder` (Impact: 517.3), `M_Drawer` (Impact: 77.0), `M_WriteText` (Impact: 24.1)

### 10. `doomgeneric/p_mobj.c` (C) -> Cumulative Risk: **734.92**
- **Archetype:** `file_cluster_13` (Distance: 13.796 IQR)
- **Magnitude:** 522.32 | **LOC:** 1050 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (91.8192%)
- **Heaviest Functions:** `P_ZMovement` (Impact: 68.8), `P_XYMovement` (Impact: 50.4), `P_SpawnMissile` (Impact: 8.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `doomgeneric/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.563 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.387 IQR)
- **Top Global Matches:** file_cluster_8: 13.563, file_cluster_13: 13.692, file_cluster_0: 13.812
- **Magnitude:** 1665.6 | **LOC:** 2007 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 302`, `structural_boundaries: 182`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 686`, `dead_code: 6`, `orphaned_logic: 22`
* *Architecture:* `api: 263`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` stdio.h, g_game.h, r_state.h, s_sound.h, sounds.h, doomstat.h, i_system.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/i_scale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.959 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.715 IQR)
- **Top Global Matches:** file_cluster_8: 13.959, file_cluster_13: 14.183, file_cluster_7: 14.329
- **Magnitude:** 1613.28 | **LOC:** 1453 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 86`, `structural_boundaries: 87`, `args: 15`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1050`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 121`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdio.h, doomtype.h, i_video.h, z_zone.h, m_argv.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.221 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_8: 13.221, file_cluster_13: 13.441, file_cluster_7: 13.584
- **Magnitude:** 1567.0 | **LOC:** 1830 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (71.675%), Tech Debt (25.3459%)
**Top Internal Functions/Classes:**
  * `WI_loadUnloadData` (Impact: 88.0 | O(N^6) | DB: 14)
  * `WI_updateNetgameStats` (Impact: 78.3 | O(N^1) | DB: 40)
  * `WI_drawOnLnode` (Impact: 69.8 | O(N^5) | DB: 8)
  * `WI_updateDeathmatchStats` (Impact: 46.0 | O(N^1) | DB: 25)
  * `WI_updateStats` (Impact: 44.8 | O(N^1) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 106`, `args: 35`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 736`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 159`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` stdio.h, g_game.h, i_swap.h, m_misc.h, z_zone.h, s_sound.h, sounds.h, wi_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` stdio.h, i_swap.h, m_misc.h, png.h, doomtype.h, i_video.h, z_zone.h, deh_str.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.204 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.67 IQR)
- **Top Global Matches:** file_cluster_13: 13.204, file_cluster_8: 13.258, file_cluster_11: 13.533
- **Magnitude:** 1495.2 | **LOC:** 2126 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (93.3528%), Tech Debt (65.7778%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 517.3 | O(N^6) | DB: 81)
  * `M_Drawer` (Impact: 77.0 | O(N^6) | DB: 19)
  * `M_WriteText` (Impact: 24.1 | O(N^1) | DB: 11)
  * `M_Init` (Impact: 21.5 | O(N^1) | DB: 15)
  * `M_DrawOPLDev` (Impact: 15.7 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 123`, `args: 25`, `func_start: 28`
* *Risk/State:* `state_mutation: 526`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 158`, `import: 25`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` g_game.h, d_main.h, hu_stuff.h, ctype.h, i_system.h, v_video.h, deh_main.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_9` (Drift: 21.332 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.513 IQR)
- **Top Global Matches:** file_cluster_9: 21.332, file_cluster_0: 21.338, file_cluster_11: 21.351
- **Magnitude:** 1248.2 | **LOC:** 1892 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 109`, `structural_boundaries: 83`, `args: 23`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 642`, `dead_code: 128`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 92`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` stdio.h, g_game.h, r_state.h, m_misc.h, p_saveg.h, z_zone.h, i_system.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/d_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.663 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.996 IQR)
- **Top Global Matches:** file_cluster_13: 12.663, file_cluster_8: 12.928, file_cluster_11: 13.167
- **Magnitude:** 1120.04 | **LOC:** 1846 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (70.5955%), Tech Debt (16.7799%)
**Top Internal Functions/Classes:**
  * `PrintDehackedBanners` (Impact: 467.4 | O(2^N) | DB: 52)
  * `D_Display` (Impact: 177.8 | O(N^3) | DB: 28)
  * `D_SetGameDescription` (Impact: 70.1 | O(N^4) | DB: 12)
  * `D_ProcessEvents` (Impact: 13.7 | O(N^2) | DB: 1)
    * *Intent:* // // D_ProcessEvents // Send all the events of the given timestamp down the responder chain //
  * `D_BindVariables` (Impact: 6.5 | O(N^2) | DB: 6)
    * *Intent:* // // Add configuration file variable bindings. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 50`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 297`, `dead_code: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 70`, `import: 42`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` stdio.h, i_endoom.h, g_game.h, d_main.h, net_dedicated.h, hu_stuff.h, ctype.h, v_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.817 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 13.817, file_cluster_8: 13.886, file_cluster_0: 14.119
- **Magnitude:** 1084.56 | **LOC:** 1417 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 152`, `structural_boundaries: 76`, `args: 20`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 572`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 88`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` stdio.h, g_game.h, i_system.h, v_video.h, deh_main.h, am_map.h, m_misc.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.501 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.306 IQR)
- **Top Global Matches:** file_cluster_13: 14.501, file_cluster_8: 14.573, file_cluster_11: 14.657
- **Magnitude:** 1048.4 | **LOC:** 983 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 133`, `structural_boundaries: 39`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 625`, `dead_code: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` stdio.h, i_swap.h, z_zone.h, r_local.h, doomstat.h, i_system.h, stdlib.h, deh_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_draw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` z_zone.h, r_local.h, doomstat.h, i_system.h, v_video.h, deh_main.h, doomdef.h, w_wad.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` r_state.h, z_zone.h, s_sound.h, sounds.h, doomstat.h, dstrings.h, deh_main.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.253 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.631 IQR)
- **Top Global Matches:** file_cluster_13: 13.253, file_cluster_8: 13.258, file_cluster_11: 13.594
- **Magnitude:** 924.06 | **LOC:** 719 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 149`, `structural_boundaries: 59`, `args: 14`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 394`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` stdio.h, d_main.h, i_swap.h, r_state.h, z_zone.h, s_sound.h, hu_stuff.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.62 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.345 IQR)
- **Top Global Matches:** file_cluster_8: 13.62, file_cluster_13: 13.657, file_cluster_0: 13.835
- **Magnitude:** 778.72 | **LOC:** 892 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 82`, `structural_boundaries: 60`, `args: 8`, `func_start: 17`
* *Risk/State:* `state_mutation: 456`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 143`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` r_sky.h, math.h, m_menu.h, r_local.h, stdlib.h, m_bbox.h, d_loop.h, doomdef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.389 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.297 IQR)
- **Top Global Matches:** file_cluster_13: 13.389, file_cluster_8: 13.457, file_cluster_11: 13.707
- **Magnitude:** 732.0 | **LOC:** 1449 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (69.6916%), Tech Debt (41.1651%)
**Top Internal Functions/Classes:**
  * `SpechitOverrun` (Impact: 114.8 | O(2^N) | DB: 8)
  * `PTR_SlideTraverse` (Impact: 50.9 | O(2^N) | DB: 23)
  * `P_CheckPosition` (Impact: 11.4 | O(N^1) | DB: 31)
  * `P_TryMove` (Impact: 10.7 | O(N^1) | DB: 11)
  * `PIT_RadiusAttack` (Impact: 9.8 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 94`, `func_start: 13`
* *Risk/State:* `state_mutation: 356`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 127`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` stdio.h, r_state.h, m_misc.h, s_sound.h, sounds.h, m_argv.h, deh_misc.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/mus2mid.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.738 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.004 IQR)
- **Top Global Matches:** file_cluster_8: 11.738, file_cluster_13: 12.007, file_cluster_7: 12.188
- **Magnitude:** 711.3 | **LOC:** 738 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (68.6471%), Tech Debt (10.0302%)
**Top Internal Functions/Classes:**
  * `mus2mid` (Impact: 212.0 | O(N^6) | DB: 16)
  * `AllocateMIDIChannel` (Impact: 41.6 | O(2^N) | DB: 6)
    * *Intent:* // Allocate a free MIDI channel.
  * `WriteChangeController_Valued` (Impact: 23.3 | O(N^6) | DB: 5)
    * *Intent:* // Write a valued controller change event
  * `WriteTime` (Impact: 22.4 | O(N^3) | DB: 5)
    * *Intent:* // Write timestamp to a MIDI file.
  * `WritePressKey` (Impact: 19.1 | O(N^6) | DB: 4)
    * *Intent:* // Write a key press event
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 118`, `args: 8`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 185`, `orphaned_logic: 1`
* *Architecture:* `api: 110`, `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdio.h, i_swap.h, m_misc.h, doomtype.h, z_zone.h, mus2mid.h, memio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.362 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.485 IQR)
- **Top Global Matches:** file_cluster_13: 14.362, file_cluster_8: 14.432, file_cluster_11: 14.51
- **Magnitude:** 694.48 | **LOC:** 547 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 111`, `structural_boundaries: 26`, `func_start: 4`
* *Risk/State:* `state_mutation: 454`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 63`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` r_state.h, z_zone.h, s_sound.h, sounds.h, doomstat.h, doomdef.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.702 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.925 IQR)
- **Top Global Matches:** file_cluster_8: 12.702, file_cluster_13: 12.703, file_cluster_7: 13.125
- **Magnitude:** 691.52 | **LOC:** 671 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 86`, `structural_boundaries: 38`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` stdio.h, w_wad.h, m_misc.h, doomfeatures.h, doomtype.h, z_zone.h, s_sound.h, deh_str.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_data.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.858 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_0: 14.375, file_cluster_8: 14.376
- **Magnitude:** 665.1 | **LOC:** 913 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` stdio.h, r_sky.h, i_swap.h, m_misc.h, r_data.h, z_zone.h, p_local.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.26 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.448 IQR)
- **Top Global Matches:** file_cluster_13: 13.26, file_cluster_11: 13.754, file_cluster_0: 13.792
- **Magnitude:** 641.18 | **LOC:** 2304 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 46`, `structural_boundaries: 66`, `args: 15`, `func_start: 8`
* *Risk/State:* `state_mutation: 189`, `dead_code: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 82`, `import: 36`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` g_game.h, d_main.h, r_sky.h, r_data.h, hu_stuff.h, i_system.h, v_video.h, deh_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/i_system.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.747 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.274 IQR)
- **Top Global Matches:** file_cluster_13: 12.747, file_cluster_8: 12.863, file_cluster_7: 13.275
- **Magnitude:** 616.84 | **LOC:** 579 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (65.86%), Tech Debt (34.8236%)
**Top Internal Functions/Classes:**
  * `I_Error` (Impact: 163.3 | O(2^N) | DB: 8)
  * `I_GetMemoryValue` (Impact: 115.8 | O(N^6) | DB: 16)
    * *Intent:* // Read Access Violation emulation. // // From PrBoom+, by entryway. // // C:\>debug // -d 0:0 // //...
  * `AutoAllocMemory` (Impact: 21.9 | O(N^3) | DB: 4)
    * *Intent:* // Zone memory auto-allocation function that allocates the zone size // by trying progressively smal...
  * `I_ZoneBase` (Impact: 13.6 | O(N^2) | DB: 6)
  * `EscapeShellString` (Impact: 12.3 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 36`, `args: 13`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 190`, `orphaned_logic: 6`
* *Architecture:* `api: 48`, `import: 21`
* *Defense:* `safety: 1`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` stdio.h, windows.h, stdarg.h, deh_str.h, i_system.h, m_misc.h, z_zone.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/hu_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.313 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.716 IQR)
- **Top Global Matches:** file_cluster_8: 12.313, file_cluster_13: 12.427, file_cluster_7: 12.743
- **Magnitude:** 541.56 | **LOC:** 642 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (66.589%), Tech Debt (27.3149%)
**Top Internal Functions/Classes:**
  * `HU_Responder` (Impact: 126.5 | O(N^5) | DB: 34)
  * `HU_Ticker` (Impact: 54.5 | O(N^2) | DB: 17)
  * `HU_Start` (Impact: 37.6 | O(N^2) | DB: 16)
  * `HU_queueChatChar` (Impact: 5.8 | O(N^1) | DB: 3)
  * `HU_dequeueChatChar` (Impact: 5.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 48`, `args: 8`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 241`, `orphaned_logic: 7`
* *Architecture:* `api: 51`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` i_swap.h, m_misc.h, i_video.h, z_zone.h, s_sound.h, hu_stuff.h, ctype.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/doomgeneric_allegro.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.031 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.738 IQR)
- **Top Global Matches:** file_cluster_13: 13.031, file_cluster_8: 13.209, file_cluster_11: 13.384
- **Magnitude:** 535.18 | **LOC:** 454 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (87.7579%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `DG_DrawFrame` (Impact: 240.3 | O(N^1) | DB: 73)
  * `back_to_text_mode` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 14`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 217`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 71`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, doomgeneric.h, i_video.h, unistd.h, stdbool.h, m_argv.h, allegro.h, i_system.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.864 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.838 IQR)
- **Top Global Matches:** file_cluster_13: 13.864, file_cluster_8: 13.928, file_cluster_0: 14.119
- **Magnitude:** 530.32 | **LOC:** 744 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 61`, `structural_boundaries: 6`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, r_sky.h, r_local.h, doomstat.h, i_system.h, stdlib.h, doomdef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.796 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_13: 13.796, file_cluster_8: 13.9, file_cluster_11: 14.092
- **Magnitude:** 522.32 | **LOC:** 1050 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 97`, `structural_boundaries: 24`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 293`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 57`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` stdio.h, z_zone.h, s_sound.h, hu_stuff.h, sounds.h, doomstat.h, i_system.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_maputl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.645 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.645, file_cluster_13: 13.806, file_cluster_7: 14.052
- **Magnitude:** 519.02 | **LOC:** 1002 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (68.9525%), Tech Debt (21.1002%)
**Top Internal Functions/Classes:**
  * `P_BoxOnLineSide` (Impact: 15.2 | O(N^1) | DB: 14)
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
* *Risk/State:* `state_mutation: 352`, `orphaned_logic: 4`
* *Architecture:* `api: 88`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` r_state.h, doomstat.h, m_bbox.h, stdlib.h, doomdef.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `doomgeneric/r_bsp.c` (C) | Magnitude: 477.08 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 238, indent_spaces: 174, pointers: 74, indent_tabs: 72
- `doomgeneric/f_finale.c` (C) | Magnitude: 924.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 394, indent_spaces: 275, branch: 149, api: 115
- `doomgeneric/doomgeneric_emscripten.c` (C) | Magnitude: 283.48 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 98, branch: 59, api: 43
- `doomgeneric/doomgeneric_sdl.c` (C) | Magnitude: 291.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 104, branch: 60, api: 42
- `doomgeneric/r_draw.c` (C) | Magnitude: 1039.38 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 567, indent_spaces: 283, indent_tabs: 139, api: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `doomgeneric/s_sound.c` (C) | Magnitude: 691.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 347, state_mutation: 220, branch: 86, pointers: 84
- `doomgeneric/f_wipe.c` (C) | Magnitude: 327.7 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 180, indent_spaces: 92, api: 57, indent_tabs: 45
- `doomgeneric/v_video.c` (C) | Magnitude: 1521.66 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 545, indent_spaces: 430, pointers: 173, api: 104
- `doomgeneric/doomdef.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `doomgeneric/doomgeneric_linuxvt.c` (C) | Magnitude: 426.44 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 225, state_mutation: 186, branch: 84, api: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `doomgeneric/p_saveg.c` (C) | Magnitude: 1248.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 642, indent_spaces: 602, pointers: 486, dead_code: 128
- `doomgeneric/i_system.h` (C) | Magnitude: 29.38 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, api: 14, args: 12, pointers: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `doomgeneric/i_system.c` -> **ozkl** (100.0% isolated ownership) | Magnitude: 616.84
- `doomgeneric/doomgeneric_sosox.c` -> **ozkl** (100.0% isolated ownership) | Magnitude: 438.74
- `doomgeneric/doomgeneric_linuxvt.c` -> **techflashYT** (100.0% isolated ownership) | Magnitude: 426.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `doomgeneric/p_mobj.h` -> **Severity: 0.303** (Bridge: 0.003 * Flux: 99.7778%)
- `doomgeneric/doomdef.h` -> **Severity: 0.133** (Bridge: 0.0034 * Flux: 39.6628%)
- `doomgeneric/d_player.h` -> **Severity: 0.133** (Bridge: 0.0043 * Flux: 30.6489%)
- `doomgeneric/d_event.h` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 99.9999%)
- `doomgeneric/i_sound.h` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 87.553%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `doomgeneric/d_event.h` -> **Severity: 4.834** (Embedded: 0.1678 * Error Risk: 28.8073%)
- `doomgeneric/i_swap.h` -> **Severity: 2.736** (Embedded: 0.0939 * Error Risk: 29.1339%)
- `doomgeneric/z_zone.h` -> **Severity: 1.952** (Embedded: 0.232 * Error Risk: 8.4111%)
- `doomgeneric/p_mobj.h` -> **Severity: 1.63** (Embedded: 0.1107 * Error Risk: 14.728%)
- `doomgeneric/doomdef.h` -> **Severity: 1.534** (Embedded: 0.2112 * Error Risk: 7.2617%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `doomgeneric/doomtype.h` -> **Severity: 2487.979** (Blast Radius: 166.974 * Doc Risk: 14.9004%)
- `doomgeneric/net_defs.h` -> **Severity: 2314.4** (Blast Radius: 23.144 * Doc Risk: 100.0%)
- `doomgeneric/d_mode.h` -> **Severity: 1963.872** (Blast Radius: 19.713 * Doc Risk: 99.6232%)
- `doomgeneric/d_ticcmd.h` -> **Severity: 1899.5** (Blast Radius: 18.995 * Doc Risk: 100.0%)
- `doomgeneric/d_event.h` -> **Severity: 1709.485** (Blast Radius: 19.259 * Doc Risk: 88.7629%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
