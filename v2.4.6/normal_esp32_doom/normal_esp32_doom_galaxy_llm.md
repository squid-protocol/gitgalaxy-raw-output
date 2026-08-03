# ARCHITECTURAL_BRIEF: normal_esp32_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_esp32_doom` |
| **Timestamp** | `2026-08-03T19:05:39.965546+00:00` |
| **Scan Duration** | `1.0s` |
| **Git Branch** | `master` |
| **Git Commit** | `085f21b630f11adb69a3894db5a1efa39a7aa31a` |
| **Git Remote** | `https://github.com/espressif/esp32-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 178 malicious artifacts.

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
| Total Artifacts | 203 |
| Analyzed Artifacts (Scanned) | 181 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 22 |
| Total LOC | 29541 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.2% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3311 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1029 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7095 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 164 | 28867 | 90.6% |
| MAKEFILE | 9 | 36 | 5.0% |
| CPP | 4 | 633 | 2.2% |
| PLAINTEXT | 2 | 0 | 1.1% |
| SHELL | 1 | 2 | 0.6% |
| CSV | 1 | 3 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.487`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 94 | 51.9% |
| file_cluster_13 | 72 | 39.8% |
| file_cluster_9 | 13 | 7.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 22*

**Composition by Extension & Reason:**
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 40960 hex tokens in 3418 LOC), 1x Excluded (Embedded Hex Payload: 16384 hex tokens in 1370 LOC)
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1501 LOC), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.dat`: 4x Excluded (Unsupported Extension: '.dat')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 298 LOC)
- `.projbuild`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.disabled`: 1x Excluded (Unsupported Extension: '.disabled')
- `.wad`: 1x Excluded (Unsupported Extension: '.wad')
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 34.0 | 7.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 29.4 | 8.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 25.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.3 | 9.3 | 10.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.9 | 42.8 | 100.0 |
| Commented Logic Exposure | 0.0 | 52.6 | 2.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 66.1 | 92.1 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 32.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 5.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.9 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `components/prboom/m_misc.c` (Hits: 16)
- `components/prboom/include/d_englsh.h` (Hits: 13)
- `components/prboom/mmus2mid.c` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomstat.h** (`components/prboom/include/doomstat.h`) — 58 inbound connections
2. **lprintf.h** (`components/prboom/include/lprintf.h`) — 50 inbound connections
3. **r_main.h** (`components/prboom/include/r_main.h`) — 38 inbound connections
4. **config.h** (`components/prboom/include/config.h`) — 35 inbound connections
5. **doomtype.h** (`components/prboom/include/doomtype.h`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **g_game.c** (`components/prboom/g_game.c`) — 41 outbound dependencies
2. **d_main.c** (`components/prboom/d_main.c`) — 38 outbound dependencies
3. **m_misc.c** (`components/prboom/m_misc.c`) — 29 outbound dependencies
4. **i_system.c** (`components/prboom-esp32-compat/i_system.c`) — 26 outbound dependencies
5. **gl_main.c** (`components/prboom/gl_main.c`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_ChangeSwitchTexture` (@ `components/prboom/p_switch.c`) -> Impact: **1627.6** | LOC: 752
- `D_BuildBEXTables` (@ `components/prboom/d_deh.c`) -> Impact: **958.8** | LOC: 565
- `G_BuildTiccmd` (@ `components/prboom/g_game.c`) -> Impact: **692.7** | LOC: 622
- `AM_Responder` (@ `components/prboom/am_map.c`) -> Impact: **676.9** | LOC: 598
- `R_RenderMaskedSegRange` (@ `components/prboom/r_segs.c`) -> Impact: **654.0** | LOC: 592
- `V_DrawMemPatch` (@ `components/prboom/v_video.c`) -> Impact: **654.0** | LOC: 592
- `createPatch` (@ `components/prboom/r_patch.c`) -> Impact: **602.7** | LOC: 277
- `HU_Start` (@ `components/prboom/hu_stuff.c`) -> Impact: **544.5** | LOC: 567
- `WI_drawTime` (@ `components/prboom/wi_stuff.c`) -> Impact: **531.1** | LOC: 622
- `S_StartSoundAtVolume` (@ `components/prboom/s_sound.c`) -> Impact: **522.8** | LOC: 96
  * *Intent:* // start new music for the level

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `R_InstallSpriteLump` (@ `components/prboom/r_things.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // // Sprite rotation 0 is facing the viewer, // rotation 1 is one angle turn CLOCKWISE around the axis. // This is not the same as the angle, // whic...
- `S_StartSoundAtVolume` (@ `components/prboom/s_sound.c`) -> **O(2^N) [Recursive]**
  * *Intent:* // start new music for the level
- `M_ReadFile` (@ `components/prboom/m_misc.c`) -> **O(2^N) [Recursive]**
  * *Intent:* #include "am_map.h" #include "w_wad.h" #include "i_system.h" #include "i_sound.h" #include "i_video.h" #include "v_video.h" #include "hu_stuff.h" #inc...
- `P_ChangeSwitchTexture` (@ `components/prboom/p_switch.c`) -> **O(2^N) [Recursive]**
- `P_InitSwitchList` (@ `components/prboom/p_switch.c`) -> **O(2^N) [Recursive]**
  * *Intent:* * along with this program; if not, write to the Free Software * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA * 02111-1307, USA. * * DESCR...
- `createPatch` (@ `components/prboom/r_patch.c`) -> **O(2^N) [Recursive]**
- `gld_AddPatchToTexture` (@ `components/prboom/gl_texture.c`) -> **O(2^N) [Recursive]**
- `gld_AddPatchToTexture_UnTranslated` (@ `components/prboom/gl_texture.c`) -> **O(2^N) [Recursive]**
- `T_MoveCeiling` (@ `components/prboom/p_ceilng.c`) -> **O(2^N) [Recursive]**
  * *Intent:* * as published by the Free Software Foundation; either version 2 * of the License, or (at your option) any later version. * * This program is distribu...
- `P_Move` (@ `components/prboom/p_enemy.c`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `V_DrawMemPatch` (@ `components/prboom/v_video.c`) -> DB Complexity: **230**
- `R_RenderMaskedSegRange` (@ `components/prboom/r_segs.c`) -> DB Complexity: **205**
- `HU_Start` (@ `components/prboom/hu_stuff.c`) -> DB Complexity: **172**
- `G_BuildTiccmd` (@ `components/prboom/g_game.c`) -> DB Complexity: **134**
- `R_DRAWCOLUMN_FUNCNAME` (@ `components/prboom/r_drawcolumn.inl`) -> DB Complexity: **127**
  * *Intent:* #define GETCOL16(frac, nextfrac) filter_getFilteredForColumn16(GETCOL8_DEPTH,frac,nextfrac) #define GETCOL32(frac, nextfrac) filter_getFilteredForColu...
- `D_BuildBEXTables` (@ `components/prboom/d_deh.c`) -> DB Complexity: **117**
- `createPatch` (@ `components/prboom/r_patch.c`) -> DB Complexity: **113**
- `gld_PointOnSide` (@ `components/prboom/gl_main.c`) -> DB Complexity: **112**
- `WI_drawTime` (@ `components/prboom/wi_stuff.c`) -> DB Complexity: **104**
- `AM_Responder` (@ `components/prboom/am_map.c`) -> DB Complexity: **83**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `components/prboom` | 74 | 42376.74 | 62.83% | 36.82% |
| `components/prboom/include` | 74 | 2856.8 | 9.05% | 4.0% |
| `components/prboom-esp32-compat` | 10 | 1080.38 | 41.06% | 57.39% |
| `components/prboom/native` | 7 | 699.92 | 39.21% | 75.8% |
| `components/prboom-wad-tables/include` | 4 | 52.16 | 5.0% | 0.0% |
| `components/prboom-esp32-compat/include` | 3 | 43.76 | 5.0% | 0.0% |
| `main` | 3 | 38.52 | 7.78% | 26.45% |
| `components/prboom-wad-tables` | 2 | 31.72 | 2.5% | 0.0% |
| `__monolith__` | 3 | 23.74 | 5.0% | 33.33% |
| `components/prboom/native/include/rom` | 1 | 10.52 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `components/prboom-esp32-compat/i_network.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_sound.c` -> **100.0%** Exposure
- `components/prboom/native/i_network.c` -> **100.0%** Exposure
- `components/prboom/native/i_sound.c` -> **100.0%** Exposure
- `components/prboom/native/i_system.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `components/prboom/Makefile` -> **100.0%** Exposure
- `components/prboom/component.mk` -> **100.0%** Exposure
- `components/prboom-esp32-compat/gamepad.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_main.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_network.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `components/prboom/p_enemy.c` -> **35** Orphaned Functions | **0** Duplicates
- `components/prboom/m_menu.c` -> **23** Orphaned Functions | **0** Duplicates
- `components/prboom-esp32-compat/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates
- `components/prboom/native/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates
- `components/prboom-esp32-compat/i_network.c` -> **16** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`components/prboom/am_map.c`** -> AI Confidence: **99.48%**
2. **`components/prboom/hu_stuff.c`** -> AI Confidence: **99.48%**
3. **`components/prboom/p_doors.c`** -> AI Confidence: **99.48%**
4. **`components/prboom/p_floor.c`** -> AI Confidence: **99.48%**
5. **`components/prboom/p_genlin.c`** -> AI Confidence: **99.48%**
6. **`components/prboom/p_mobj.c`** -> AI Confidence: **99.48%**
7. **`components/prboom/p_plats.c`** -> AI Confidence: **99.48%**
8. **`components/prboom/p_sight.c`** -> AI Confidence: **99.48%**
9. **`components/prboom/p_switch.c`** -> AI Confidence: **99.48%**
10. **`components/prboom/p_user.c`** -> AI Confidence: **99.48%**
11. **`components/prboom/r_bsp.c`** -> AI Confidence: **99.48%**
12. **`components/prboom/r_draw.c`** -> AI Confidence: **99.48%**
13. **`components/prboom/r_patch.c`** -> AI Confidence: **99.48%**
14. **`components/prboom/r_plane.c`** -> AI Confidence: **99.48%**
15. **`components/prboom/r_segs.c`** -> AI Confidence: **99.48%**
16. **`components/prboom/r_things.c`** -> AI Confidence: **99.48%**
17. **`components/prboom-esp32-compat/psxcontroller.c`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `components/prboom/am_map.c` -> **20.0%** Exposure
- `components/prboom/d_client.c` -> **20.0%** Exposure
- `components/prboom/d_deh.c` -> **20.0%** Exposure
- `components/prboom/d_main.c` -> **20.0%** Exposure
- `components/prboom/f_finale.c` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `components/prboom/include/d_englsh.h` -> **0.873%** Exposure
### Raw Memory Manipulation
- `components/prboom/r_patch.c` -> **10.0%** Exposure
- `components/prboom/p_setup.c` -> **9.9997%** Exposure
- `components/prboom/r_data.c` -> **0.8622%** Exposure
- `components/prboom/hu_stuff.c` -> **0.0989%** Exposure
- `components/prboom/r_main.c` -> **0.0292%** Exposure
### Algorithmic DoS Exposure
- `components/prboom/am_map.c` -> **100.0%** Exposure
- `components/prboom/d_client.c` -> **100.0%** Exposure
- `components/prboom/d_deh.c` -> **100.0%** Exposure
- `components/prboom/d_main.c` -> **100.0%** Exposure
- `components/prboom/f_finale.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1076` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `components/prboom/p_enemy.c` (C) -> Cumulative Risk: **772.95**
- **Archetype:** `file_cluster_13` (Distance: 14.191 IQR)
- **Magnitude:** 1666.18 | **LOC:** 2602 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (97.84%)
- **Heaviest Functions:** `A_BossDeath` (Impact: 165.3), `P_Move` (Impact: 104.5), `P_CheckMeleeRange` (Impact: 58.6)

### 2. `components/prboom/r_plane.c` (C) -> Cumulative Risk: **770.77**
- **Archetype:** `file_cluster_13` (Distance: 14.238 IQR)
- **Magnitude:** 680.8 | **LOC:** 471 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9503%)
- **Heaviest Functions:** `R_MapPlane` (Impact: 90.1), `R_MakeSpans` (Impact: 84.0), `R_DoDrawPlane` (Impact: 53.7)

### 3. `components/prboom/r_data.c` (C) -> Cumulative Risk: **754.71**
- **Archetype:** `file_cluster_13` (Distance: 13.652 IQR)
- **Magnitude:** 255.1 | **LOC:** 747 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.854%)
- **Heaviest Functions:** `R_PrecacheLevel` (Impact: 54.7), `R_InitTranMap` (Impact: 11.7), `R_InitTextures` (Impact: 3.8)

### 4. `components/prboom/p_plats.c` (C) -> Cumulative Risk: **745.18**
- **Archetype:** `file_cluster_13` (Distance: 17.147 IQR)
- **Magnitude:** 563.56 | **LOC:** 438 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (95.3634%)
- **Heaviest Functions:** `T_PlatRaise` (Impact: 242.8), `P_ActivateInStasis` (Impact: 19.0), `EV_StopPlat` (Impact: 4.8)

### 5. `components/prboom/r_patch.c` (C) -> Cumulative Risk: **741.74**
- **Archetype:** `file_cluster_13` (Distance: 14.178 IQR)
- **Magnitude:** 1222.08 | **LOC:** 788 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.3121%)
- **Heaviest Functions:** `createPatch` (Impact: 602.7), `R_FlushAllPatches` (Impact: 30.7), `R_CachePatchNum` (Impact: 25.8)

### 6. `components/prboom/p_saveg.c` (C) -> Cumulative Risk: **741.48**
- **Archetype:** `file_cluster_8` (Distance: 14.345 IQR)
- **Magnitude:** 1511.04 | **LOC:** 1030 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.1246%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 221.5), `P_UnArchiveSpecials` (Impact: 115.4), `P_UnArchiveThinkers` (Impact: 79.1)

### 7. `components/prboom/p_mobj.c` (C) -> Cumulative Risk: **739.89**
- **Archetype:** `file_cluster_13` (Distance: 14.68 IQR)
- **Magnitude:** 859.0 | **LOC:** 1533 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (91.9884%)
- **Heaviest Functions:** `P_XYMovement` (Impact: 145.7), `P_IsDoomnumAllowed` (Impact: 34.8), `P_SpawnMapThing` (Impact: 31.8)

### 8. `components/prboom/r_fps.c` (C) -> Cumulative Risk: **723.05**
- **Archetype:** `file_cluster_8` (Distance: 13.329 IQR)
- **Magnitude:** 568.16 | **LOC:** 451 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.4893%)
- **Heaviest Functions:** `R_InterpolationGetData` (Impact: 33.0), `R_DoAnInterpolation` (Impact: 31.8), `R_CopyInterpToOld` (Impact: 29.4)

### 9. `components/prboom/p_sight.c` (C) -> Cumulative Risk: **716.74**
- **Archetype:** `file_cluster_13` (Distance: 14.842 IQR)
- **Magnitude:** 582.42 | **LOC:** 339 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9884%)
- **Heaviest Functions:** `P_CrossSubsector` (Impact: 247.2), `P_CheckSight` (Impact: 94.7), `P_CrossBSPNode_LxDoom` (Impact: 19.1)

### 10. `components/prboom/r_main.c` (C) -> Cumulative Risk: **712.46**
- **Archetype:** `file_cluster_13` (Distance: 13.523 IQR)
- **Magnitude:** 699.76 | **LOC:** 651 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.7269%)
- **Heaviest Functions:** `R_PointToAngle` (Impact: 61.5), `R_InitTextureMapping` (Impact: 54.8), `R_PointToAngle2` (Impact: 35.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `components/prboom/gl_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.29 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 14.29, file_cluster_13: 14.316, file_cluster_11: 14.472
- **Magnitude:** 2358.64 | **LOC:** 2721 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (87.7591%), Tech Debt (16.7053%)
**Top Internal Functions/Classes:**
  * `gld_PointOnSide` (Impact: 270.2 | O(N^2) | DB: 112)
  * `gld_AddWall` (Impact: 126.1 | O(N^3) | DB: 56)
  * `gld_Init` (Impact: 98.7 | O(N^2) | DB: 40)
  * `gld_DrawScene` (Impact: 75.2 | O(N^3) | DB: 31)
    * *Intent:* // e6y // Sky textures with a zero index should be forced // See third episode of requiem.wad #defin...
  * `gld_SetPalette` (Impact: 69.6 | O(N^3) | DB: 39)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 135`, `args: 27`, `func_start: 37`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1215`, `dead_code: 9`, `orphaned_logic: 16`
* *Architecture:* `io: 3`, `api: 237`, `import: 26`
* *Defense:* `safety: 1`, `doc: 6`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` stdio.h, windows.h, math.h, r_draw.h, r_plane.h, gl_struct.h, SDL_opengl.h, d_event.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_deh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.558 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.406 IQR)
- **Top Global Matches:** file_cluster_8: 13.558, file_cluster_13: 13.664, file_cluster_0: 13.78
- **Magnitude:** 2307.66 | **LOC:** 3096 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 117
- **Risk Profile:** Cognitive Load (88.5791%), Tech Debt (21.178%)
**Top Internal Functions/Classes:**
  * `D_BuildBEXTables` (Impact: 958.8 | O(N^6) | DB: 117)
  * `dehfgets` (Impact: 44.9 | O(N^3) | DB: 10)
    * *Intent:* * Author: Ty Halderman, TeamTNT * *-----------------------------------------------------------------...
  * `deh_GetData` (Impact: 31.1 | O(N^2) | DB: 17)
  * `deh_procHelperThing` (Impact: 19.4 | O(N^2) | DB: 6)
  * `StrToInt` (Impact: 7.4 | O(N^1) | DB: 12)
    * *Intent:* // ==================================================================== // deh_procFrame // Purpose:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 88`, `args: 15`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 789`, `dead_code: 4`, `fragile_debt: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 400`, `import: 14`
* *Defense:* `safety: 13`, `immutability_locks: 333`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` w_wad.h, dstrings.h, doomdef.h, doomstat.h, p_enemy.h, info.h, ctype.h, lprintf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_switch.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.64 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.904 IQR)
- **Top Global Matches:** file_cluster_8: 10.64, file_cluster_13: 10.977, file_cluster_7: 11.15
- **Magnitude:** 1852.66 | **LOC:** 1151 | **CtrlFlow:** 96.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (55.6575%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_ChangeSwitchTexture` (Impact: 1627.6 | O(2^N) | DB: 17)
  * `P_InitSwitchList` (Impact: 101.2 | O(2^N) | DB: 16)
    * *Intent:* * along with this program; if not, write to the Free Software * Foundation, Inc., 59 Temple Place - ...
  * `P_StartButton` (Impact: 13.3 | O(2^N) | DB: 9)
    * *Intent:* // Ignore switches referencing unknown texture names, instead of exiting.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 12`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 80`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 20`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` w_wad.h, s_sound.h, p_spec.h, doomstat.h, lprintf.h, g_game.h, sounds.h, r_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.558 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.127 IQR)
- **Top Global Matches:** file_cluster_13: 14.558, file_cluster_8: 14.649, file_cluster_11: 14.67
- **Magnitude:** 1782.98 | **LOC:** 1079 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (76.5179%), Tech Debt (12.0436%)
**Top Internal Functions/Classes:**
  * `R_InitSpriteDefs` (Impact: 227.6 | O(N^6) | DB: 28)
  * `R_DrawSprite` (Impact: 174.2 | O(N^5) | DB: 42)
  * `R_ProjectSprite` (Impact: 153.9 | O(2^N) | DB: 59)
  * `R_InstallSpriteLump` (Impact: 126.8 | O(2^N) | DB: 10)
    * *Intent:* // // Sprite rotation 0 is facing the viewer, // rotation 1 is one angle turn CLOCKWISE around the a...
  * `R_DrawPSprite` (Impact: 81.2 | O(N^5) | DB: 33)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 43`, `args: 9`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `state_mutation: 752`, `dead_code: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 125`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` w_wad.h, r_fps.h, doomstat.h, lprintf.h, v_video.h, r_segs.h, r_draw.h, r_bsp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.436 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.635 IQR)
- **Top Global Matches:** file_cluster_8: 14.436, file_cluster_13: 14.442, file_cluster_11: 14.68
- **Magnitude:** 1701.44 | **LOC:** 1042 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 230
- **Risk Profile:** Cognitive Load (73.5248%), Tech Debt (12.7484%)
**Top Internal Functions/Classes:**
  * `V_DrawMemPatch` (Impact: 654.0 | O(N^3) | DB: 230)
  * `FUNC_V_CopyRect` (Impact: 88.9 | O(N^4) | DB: 11)
    * *Intent:* /* * V_InitColorTranslation * * Loads the color translation tables from predefined lumps at game sta...
  * `FUNC_V_DrawBackground` (Impact: 55.1 | O(N^2) | DB: 33)
    * *Intent:* // // V_CopyRect // // Copies a source rectangle in a screen buffer to a destination
  * `V_Init` (Impact: 4.2 | O(N^1) | DB: 9)
  * `V_InitColorTranslation` (Impact: 3.1 | O(N^1) | DB: 3)
    * *Intent:* * Functions to draw patches (by post) directly to screen. * Functions to blit a block to the screen....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 72`, `args: 36`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 771`, `orphaned_logic: 3`
* *Architecture:* `api: 113`, `import: 10`
* *Defense:* `immutability_locks: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` w_wad.h, doomdef.h, GAMMATBL.h, lprintf.h, v_video.h, esp_attr.h, m_bbox.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.191 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.186 IQR)
- **Top Global Matches:** file_cluster_13: 14.191, file_cluster_8: 14.272, file_cluster_11: 14.334
- **Magnitude:** 1666.18 | **LOC:** 2602 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (96.3846%), Tech Debt (77.9128%)
**Top Internal Functions/Classes:**
  * `A_BossDeath` (Impact: 165.3 | O(N^4) | DB: 10)
  * `P_Move` (Impact: 104.5 | O(2^N) | DB: 27)
  * `P_CheckMeleeRange` (Impact: 58.6 | O(N^6) | DB: 5)
  * `P_DoNewChaseDir` (Impact: 52.2 | O(N^2) | DB: 22)
  * `P_NewChaseDir` (Impact: 40.8 | O(N^2) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 166`, `args: 1`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 702`, `dead_code: 6`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `api: 183`, `import: 15`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` s_sound.h, p_spec.h, p_inter.h, p_enemy.h, doomstat.h, p_tick.h, lprintf.h, p_maputl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.345 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.644 IQR)
- **Top Global Matches:** file_cluster_8: 14.345, file_cluster_13: 14.394, file_cluster_11: 14.549
- **Magnitude:** 1511.04 | **LOC:** 1030 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (71.0204%), Tech Debt (60.2168%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` (Impact: 221.5 | O(N^3) | DB: 71)
  * `P_UnArchiveSpecials` (Impact: 115.4 | O(N^3) | DB: 55)
  * `P_UnArchiveThinkers` (Impact: 79.1 | O(2^N) | DB: 44)
  * `P_ArchiveThinkers` (Impact: 52.4 | O(N^3) | DB: 20)
  * `P_ArchiveWorld` (Impact: 24.5 | O(N^2) | DB: 44)
    * *Intent:* // // P_UnArchivePlayers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 55`, `args: 30`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 810`, `fragile_debt: 3`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 100`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` p_spec.h, doomstat.h, p_tick.h, lprintf.h, p_maputl.h, am_map.h, p_saveg.h, p_enemy.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_setup.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.997 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.351 IQR)
- **Top Global Matches:** file_cluster_13: 14.997, file_cluster_11: 15.281, file_cluster_0: 15.32
- **Magnitude:** 1332.82 | **LOC:** 1689 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (34.1576%), Tech Debt (28.9176%)
**Top Internal Functions/Classes:**
  * `P_CreateBlockMap` (Impact: 98.3 | O(N^3) | DB: 27)
  * `P_LoadNodes` (Impact: 66.0 | O(2^N) | DB: 17)
  * `P_LoadReject` (Impact: 61.9 | O(N^2) | DB: 29)
    * *Intent:* // // jff 10/6/98 // New code added to speed up calculation of internal blockmap // Algorithm is ord...
  * `P_GetNodesVersion` (Impact: 58.9 | O(2^N) | DB: 7)
  * `P_LoadSegs` (Impact: 56.7 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 41`, `args: 17`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `state_mutation: 704`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 125`, `import: 20`
* *Defense:* `safety: 2`, `doc: 63`, `immutability_locks: 33`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` i_system.h, math.h, g_game.h, p_map.h, p_setup.h, lprintf.h, m_bbox.h, r_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/gl_texture.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.788 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.545 IQR)
- **Top Global Matches:** file_cluster_13: 13.788, file_cluster_8: 13.879, file_cluster_11: 14.074
- **Magnitude:** 1327.38 | **LOC:** 960 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (69.2174%), Tech Debt (11.0057%)
**Top Internal Functions/Classes:**
  * `gld_AddPatchToTexture` (Impact: 108.7 | O(2^N) | DB: 32)
  * `gld_AddPatchToTexture_UnTranslated` (Impact: 92.2 | O(2^N) | DB: 30)
  * `gld_BindTexture` (Impact: 71.8 | O(N^6) | DB: 9)
  * `gld_BindFlat` (Impact: 62.0 | O(N^5) | DB: 7)
  * `gld_BindPatch` (Impact: 55.1 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 78`, `args: 11`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 614`, `dead_code: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 99`, `import: 25`
* *Defense:* `safety: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` stdio.h, windows.h, math.h, r_draw.h, r_plane.h, gl_struct.h, SDL_opengl.h, d_event.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.061 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.443 IQR)
- **Top Global Matches:** file_cluster_8: 13.061, file_cluster_13: 13.136, file_cluster_0: 13.352
- **Magnitude:** 1293.6 | **LOC:** 1969 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 104
- **Risk Profile:** Cognitive Load (91.8697%), Tech Debt (29.192%)
**Top Internal Functions/Classes:**
  * `WI_drawTime` (Impact: 531.1 | O(N^3) | DB: 104)
  * `WI_updateAnimatedBack` (Impact: 69.6 | O(N^4) | DB: 13)
  * `WI_drawNum` (Impact: 32.7 | O(N^2) | DB: 12)
  * `WI_drawOnLnode` (Impact: 23.2 | O(N^1) | DB: 9)
  * `WI_initAnimatedBack` (Impact: 20.5 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 78`, `args: 27`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 453`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 115`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 24`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` w_wad.h, s_sound.h, wi_stuff.h, doomstat.h, lprintf.h, g_game.h, v_video.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.253 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.317 IQR)
- **Top Global Matches:** file_cluster_13: 15.253, file_cluster_11: 15.384, file_cluster_0: 15.413
- **Magnitude:** 1293.0 | **LOC:** 857 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 205
- **Risk Profile:** Cognitive Load (71.9737%), Tech Debt (10.1177%)
**Top Internal Functions/Classes:**
  * `R_RenderMaskedSegRange` (Impact: 654.0 | O(N^6) | DB: 205)
  * `R_ScaleFromGlobalAngle` (Impact: 4.5 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 12`, `args: 4`, `func_start: 5`
* *Risk/State:* `state_mutation: 574`, `dead_code: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 51`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` w_wad.h, doomstat.h, lprintf.h, v_video.h, r_segs.h, r_draw.h, r_bsp.h, esp_attr.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.891 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.386 IQR)
- **Top Global Matches:** file_cluster_13: 13.891, file_cluster_11: 14.245, file_cluster_0: 14.282
- **Magnitude:** 1287.36 | **LOC:** 2923 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 134
- **Risk Profile:** Cognitive Load (77.6765%), Tech Debt (20.7084%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 692.7 | O(N^3) | DB: 134)
  * `fudgef` (Impact: 12.4 | O(N^1) | DB: 3)
  * `fudgea` (Impact: 10.3 | O(N^1) | DB: 2)
    * *Intent:* // joystick values are repeated
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 57`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 386`, `dead_code: 8`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 173`, `import: 41`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` stdio.h, f_finale.h, i_system.h, d_main.h, stdarg.h, g_game.h, m_menu.h, io.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.35 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.542 IQR)
- **Top Global Matches:** file_cluster_13: 13.35, file_cluster_8: 13.49, file_cluster_11: 13.602
- **Magnitude:** 1284.54 | **LOC:** 689 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (80.1076%), Tech Debt (34.653%)
**Top Internal Functions/Classes:**
  * `S_StartSoundAtVolume` (Impact: 522.8 | O(2^N) | DB: 25)
    * *Intent:* // start new music for the level
  * `S_UpdateSounds` (Impact: 99.7 | O(N^6) | DB: 11)
    * *Intent:* // // Stop and resume music, during game PAUSE. //
  * `S_ChangeMusic` (Impact: 54.9 | O(2^N) | DB: 8)
  * `S_getChannel` (Impact: 46.9 | O(N^2) | DB: 8)
  * `S_AdjustSoundParams` (Impact: 38.2 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 59`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 273`, `dead_code: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 67`, `import: 10`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` s_sound.h, w_wad.h, i_sound.h, i_system.h, doomstat.h, d_main.h, config.h, lprintf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/hu_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.464 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.294 IQR)
- **Top Global Matches:** file_cluster_8: 13.464, file_cluster_13: 13.587, file_cluster_7: 13.799
- **Magnitude:** 1225.6 | **LOC:** 1594 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 172
- **Risk Profile:** Cognitive Load (73.4828%), Tech Debt (10.625%)
**Top Internal Functions/Classes:**
  * `HU_Start` (Impact: 544.5 | O(N^4) | DB: 172)
  * `HU_Init` (Impact: 38.0 | O(N^1) | DB: 10)
  * `HU_Stop` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 29`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 549`, `orphaned_logic: 2`
* *Architecture:* `api: 79`, `import: 11`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` w_wad.h, hu_stuff.h, s_sound.h, doomstat.h, st_stuff.h, g_game.h, d_deh.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_patch.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.178 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.94 IQR)
- **Top Global Matches:** file_cluster_13: 14.178, file_cluster_11: 14.449, file_cluster_8: 14.478
- **Magnitude:** 1222.08 | **LOC:** 788 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (94.6278%), Tech Debt (22.6389%)
**Top Internal Functions/Classes:**
  * `createPatch` (Impact: 602.7 | O(2^N) | DB: 113)
  * `R_FlushAllPatches` (Impact: 30.7 | O(2^N) | DB: 6)
    * *Intent:* // // Patches. // A patch holds one or more columns. // Patches are used for sprites and all masked ...
  * `R_CachePatchNum` (Impact: 25.8 | O(2^N) | DB: 3)
  * `getPatchIsNotTileable` (Impact: 20.4 | O(N^1) | DB: 17)
  * `R_UnlockTextureCompositePatchNum` (Impact: 14.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 28`, `args: 7`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 419`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 74`, `import: 13`
* *Defense:* `safety: 4`, `test: 2`, `immutability_locks: 53`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` r_patch.h, assert.h, w_wad.h, i_system.h, doomstat.h, p_tick.h, z_zone.h, lprintf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.351 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.284 IQR)
- **Top Global Matches:** file_cluster_13: 13.351, file_cluster_8: 13.479, file_cluster_11: 13.573
- **Magnitude:** 1077.22 | **LOC:** 1586 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (96.2369%), Tech Debt (25.1214%)
**Top Internal Functions/Classes:**
  * `AM_Responder` (Impact: 676.9 | O(N^4) | DB: 83)
  * `AM_Start` (Impact: 6.5 | O(N^1) | DB: 5)
  * `AM_LevelInit` (Impact: 3.5 | O(N^1) | DB: 8)
    * *Intent:* #define F_PANINC 4 // how much zoom-in per tic // goes to 2x in 1 second #define M_ZOOMIN ((int) (1....
  * `AM_Stop` (Impact: 2.2 | O(N^1) | DB: 3)
  * `AM_minOutWindowScale` (Impact: 1.7 | O(N^1) | DB: 2)
    * *Intent:* #undef R
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 39`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 286`, `dead_code: 5`, `fragile_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 87`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` w_wad.h, p_spec.h, doomstat.h, st_stuff.h, config.h, p_maputl.h, am_map.h, v_video.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_genlin.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.094 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.175 IQR)
- **Top Global Matches:** file_cluster_13: 15.094, file_cluster_11: 15.138, file_cluster_0: 15.264
- **Magnitude:** 1072.44 | **LOC:** 1165 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (42.9002%), Tech Debt (29.4676%)
**Top Internal Functions/Classes:**
  * `EV_DoGenFloor` (Impact: 151.8 | O(N^3) | DB: 62)
    * *Intent:* * This program is free software; you can redistribute it and/or * modify it under the terms of the G...
  * `EV_DoGenDoor` (Impact: 95.5 | O(N^2) | DB: 44)
  * `EV_DoGenLift` (Impact: 85.5 | O(N^2) | DB: 65)
  * `EV_DoGenCrusher` (Impact: 77.5 | O(N^4) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 26`, `func_start: 4`
* *Risk/State:* `state_mutation: 551`, `dead_code: 6`, `planned_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 101`, `import: 7`
* *Defense:* `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` s_sound.h, p_spec.h, doomstat.h, p_tick.h, sounds.h, r_main.h, m_random.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.28 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_8: 13.28, file_cluster_7: 13.341, file_cluster_13: 13.358
- **Magnitude:** 1028.24 | **LOC:** 5565 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (40.4063%), Tech Debt (58.3033%)
**Top Internal Functions/Classes:**
  * `M_DrawSetting` (Impact: 104.5 | O(N^6) | DB: 18)
  * `M_DrawInstructions` (Impact: 70.7 | O(N^2) | DB: 1)
  * `M_Episode` (Impact: 18.3 | O(2^N) | DB: 2)
    * *Intent:* // // MainMenu is the definition of what the main menu Screen should look // like. Each entry shows ...
  * `M_Init` (Impact: 16.9 | O(N^1) | DB: 20)
    * *Intent:* // Note that the Y values are ascending. If you need to add something to // this table, (well, this ...
  * `M_DrawScreenItems` (Impact: 16.4 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 150`, `args: 37`, `func_start: 41`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 503`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 23`
* *Architecture:* `api: 143`, `import: 24`
* *Defense:* `doc: 277`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` stdio.h, i_system.h, d_main.h, g_game.h, m_menu.h, i_main.h, hu_stuff.h, i_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.68 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.987 IQR)
- **Top Global Matches:** file_cluster_13: 14.68, file_cluster_11: 14.781, file_cluster_0: 14.914
- **Magnitude:** 859.0 | **LOC:** 1533 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (82.7452%), Tech Debt (72.8069%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 145.7 | O(N^3) | DB: 33)
  * `P_IsDoomnumAllowed` (Impact: 34.8 | O(N^2))
  * `P_SpawnMapThing` (Impact: 31.8 | O(N^2) | DB: 9)
  * `P_SpawnPlayer` (Impact: 27.5 | O(2^N) | DB: 23)
  * `P_SetMobjState` (Impact: 15.9 | O(N^1) | DB: 21)
    * *Intent:* * Copyright 2005, 2006 by * Florian Schulze, Colin Phipps, Neil Stevens, Andrey Budko * * This progr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 41`, `args: 4`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 460`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 82`, `import: 16`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` hu_stuff.h, s_sound.h, r_demo.h, doomdef.h, doomstat.h, st_stuff.h, p_tick.h, info.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.857 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_13: 13.857, file_cluster_8: 13.943, file_cluster_0: 14.059
- **Magnitude:** 847.36 | **LOC:** 1161 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (66.1612%), Tech Debt (17.2392%)
**Top Internal Functions/Classes:**
  * `ST_updateFaceWidget` (Impact: 177.0 | O(N^6) | DB: 46)
  * `ST_doPaletteStuff` (Impact: 38.4 | O(N^2) | DB: 13)
    * *Intent:* // used by the w_armsbg widget
  * `ST_drawWidgets` (Impact: 36.0 | O(N^2) | DB: 8)
  * `ST_updateWidgets` (Impact: 33.0 | O(N^2) | DB: 18)
  * `ST_Responder` (Impact: 16.1 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 55`, `args: 16`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 402`, `dead_code: 8`, `orphaned_logic: 6`
* *Architecture:* `api: 56`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` w_wad.h, s_sound.h, st_lib.h, doomdef.h, doomstat.h, st_stuff.h, am_map.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_client.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.697 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.344 IQR)
- **Top Global Matches:** file_cluster_13: 13.697, file_cluster_11: 13.995, file_cluster_8: 14.044
- **Magnitude:** 780.26 | **LOC:** 543 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (73.5736%), Tech Debt (25.6433%)
**Top Internal Functions/Classes:**
  * `NetUpdate` (Impact: 104.0 | O(N^3) | DB: 42)
  * `TryRunTics` (Impact: 65.6 | O(N^3) | DB: 9)
  * `D_InitNetGame` (Impact: 52.0 | O(2^N) | DB: 32)
    * *Intent:* #include <sys/wait.h> #endif #ifdef USE_SDL_NET #include "SDL.h" #endif #include "doomtype.h" #inclu...
  * `CheckQueuedPackets` (Impact: 42.8 | O(N^2) | DB: 16)
  * `D_CheckNetGame` (Impact: 26.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 49`, `args: 11`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 384`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 70`, `import: 21`
* *Defense:* `safety: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` i_network.h, i_system.h, d_main.h, types.h, protocol.h, g_game.h, m_menu.h, i_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.851 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.721 IQR)
- **Top Global Matches:** file_cluster_13: 13.851, file_cluster_7: 14.014, file_cluster_8: 14.026
- **Magnitude:** 710.4 | **LOC:** 712 | **CtrlFlow:** 92.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (42.8395%), Tech Debt (18.8722%)
**Top Internal Functions/Classes:**
  * `T_VerticalDoor` (Impact: 339.8 | O(N^6) | DB: 30)
    * *Intent:* * modify it under the terms of the GNU General Public License * as published by the Free Software Fo...
  * `EV_DoDoor` (Impact: 85.0 | O(N^2) | DB: 61)
  * `EV_DoLockedDoor` (Impact: 29.4 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 13`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 193`, `dead_code: 1`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 56`, `import: 9`
* *Defense:* `doc: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` s_sound.h, p_spec.h, doomstat.h, p_tick.h, lprintf.h, d_deh.h, dstrings.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_inter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.412 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.758 IQR)
- **Top Global Matches:** file_cluster_13: 13.412, file_cluster_8: 13.503, file_cluster_11: 13.76
- **Magnitude:** 707.44 | **LOC:** 914 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (84.6242%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` (Impact: 284.9 | O(N^3) | DB: 82)
  * `P_GivePower` (Impact: 16.4 | O(N^2) | DB: 3)
  * `P_GiveCard` (Impact: 2.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 58`, `func_start: 3`
* *Risk/State:* `state_mutation: 324`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 72`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` s_sound.h, p_inter.h, p_enemy.h, doomstat.h, p_tick.h, lprintf.h, am_map.h, d_deh.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.523 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.158 IQR)
- **Top Global Matches:** file_cluster_13: 13.523, file_cluster_8: 13.759, file_cluster_11: 13.949
- **Magnitude:** 699.76 | **LOC:** 651 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (72.0424%), Tech Debt (35.6267%)
**Top Internal Functions/Classes:**
  * `R_PointToAngle` (Impact: 61.5 | O(N^6) | DB: 9)
  * `R_InitTextureMapping` (Impact: 54.8 | O(N^3) | DB: 20)
    * *Intent:* // R_PointToAngleEx merged into R_PointToAngle
  * `R_PointToAngle2` (Impact: 35.8 | O(N^6) | DB: 6)
    * *Intent:* if ( /* !render_precise && */
  * `R_ShowStats` (Impact: 26.5 | O(N^4) | DB: 9)
    * *Intent:* // killough 3/20/98, 4/4/98: select colormap based on player status
  * `R_InitLightTables` (Impact: 25.8 | O(N^3) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 28`, `args: 6`, `func_start: 13`
* *Risk/State:* `state_mutation: 338`, `dead_code: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 74`, `import: 22`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` i_system.h, math.h, g_game.h, r_draw.h, r_plane.h, i_main.h, ets_sys.h, lprintf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.382 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.268 IQR)
- **Top Global Matches:** file_cluster_13: 15.382, file_cluster_11: 15.509, file_cluster_0: 15.567
- **Magnitude:** 686.72 | **LOC:** 1043 | **CtrlFlow:** 89.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (38.3989%), Tech Debt (90.8495%)
**Top Internal Functions/Classes:**
  * `EV_BuildStairs` (Impact: 86.8 | O(N^2) | DB: 48)
    * *Intent:* // moving a ceiling up
  * `T_MovePlane` (Impact: 64.9 | O(N^4) | DB: 29)
    * *Intent:* * This program is distributed in the hope that it will be useful, * but WITHOUT ANY WARRANTY; withou...
  * `EV_DoDonut` (Impact: 33.5 | O(N^3) | DB: 29)
  * `EV_DoElevator` (Impact: 26.1 | O(N^2) | DB: 25)
  * `EV_DoChange` (Impact: 17.1 | O(N^2) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 14`, `func_start: 6`
* *Risk/State:* `state_mutation: 386`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 60`, `import: 7`
* *Defense:* `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` s_sound.h, p_spec.h, doomstat.h, p_tick.h, p_map.h, sounds.h, r_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `components/prboom/f_finale.c` (C) | Magnitude: 663.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 287, state_mutation: 266, branch: 120, api: 77
- `components/prboom/include/wi_stuff.h` (C) | Magnitude: 21.28 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, args: 3, ownership: 3
- `components/prboom/p_plats.c` (C) | Magnitude: 563.56 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 250, indent_spaces: 207, pointers: 173, branch: 69
- `components/prboom/p_user.c` (C) | Magnitude: 405.3 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 235, state_mutation: 192, pointers: 192, branch: 89
- `components/prboom/p_genlin.c` (C) | Magnitude: 1072.44 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 551, indent_spaces: 480, branch: 206, pointers: 201

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `components/prboom/v_video.c` (C) | Magnitude: 1701.44 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 771, indent_spaces: 482, branch: 148, api: 113
- `components/prboom/include/r_demo.h` (C) | Magnitude: 20.16 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 6, structural_boundaries: 3, ownership: 3, pointers: 2
- `components/prboom/gl_main.c` (C) | Magnitude: 2358.64 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1506, state_mutation: 1215, pointers: 517, branch: 314
- `components/prboom-esp32-compat/Makefile` (MAKEFILE) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `components/prboom-esp32-compat/component.mk` (MAKEFILE) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `components/prboom/include/f_wipe.h` (C) | Magnitude: 16.12 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, api: 3, ownership: 3, structural_boundaries: 2
- `components/prboom/dstrings.c` (C) | Magnitude: 27.48 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 10, branch: 6, ownership: 3
- `components/prboom/include/i_main.h` (C) | Magnitude: 16.12 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, ownership: 3, args: 2
- `components/prboom/include/r_defs.h` (C) | Magnitude: 145.44 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 122, indent_spaces: 114, structural_boundaries: 40, pointers: 27
- `components/prboom/include/p_checksum.h` (C) | Magnitude: 14.56 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 4, api: 3, args: 2, pointers: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `components/prboom/include/doomdef.h` -> **Severity: 0.35** (Bridge: 0.0082 * Flux: 42.7923%)
- `components/prboom/include/d_player.h` -> **Severity: 0.331** (Bridge: 0.0122 * Flux: 27.1182%)
- `components/prboom/include/doomstat.h` -> **Severity: 0.316** (Bridge: 0.0079 * Flux: 40.1588%)
- `components/prboom/include/r_defs.h` -> **Severity: 0.157** (Bridge: 0.0063 * Flux: 24.8129%)
- `components/prboom/include/m_fixed.h` -> **Severity: 0.139** (Bridge: 0.0014 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `components/prboom/include/lprintf.h` -> **Severity: 4.803** (Embedded: 0.2778 * Error Risk: 17.2899%)
- `components/prboom/include/d_event.h` -> **Severity: 2.629** (Embedded: 0.1415 * Error Risk: 18.5788%)
- `components/prboom/include/doomtype.h` -> **Severity: 2.539** (Embedded: 0.2983 * Error Risk: 8.5099%)
- `components/prboom/include/doomstat.h` -> **Severity: 2.057** (Embedded: 0.3226 * Error Risk: 6.3757%)
- `components/prboom/include/m_fixed.h` -> **Severity: 1.944** (Embedded: 0.1897 * Error Risk: 10.2494%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `components/prboom/include/doomtype.h` -> **Severity: 5707.527** (Blast Radius: 70.672 * Doc Risk: 80.7608%)
- `components/prboom/include/d_player.h` -> **Severity: 3949.3** (Blast Radius: 39.493 * Doc Risk: 100.0%)
- `components/prboom/include/m_fixed.h` -> **Severity: 3310.897** (Blast Radius: 33.489 * Doc Risk: 98.8652%)
- `components/prboom/include/doomstat.h` -> **Severity: 2512.2** (Blast Radius: 25.122 * Doc Risk: 100.0%)
- `components/prboom/include/p_mobj.h` -> **Severity: 2502.7** (Blast Radius: 25.027 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
