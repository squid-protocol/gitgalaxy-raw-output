# ARCHITECTURAL_BRIEF: loony_ascii_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/loony_ascii_doom` |
| **Timestamp** | `2026-08-07T03:29:31.279883+00:00` |
| **Scan Duration** | `0.69s` |
| **Git Branch** | `master` |
| **Git Commit** | `b5188d7c9c4da6c81264a7803e8725ac3df2cfea` |
| **Git Remote** | `https://github.com/wojciech-graj/doom-ascii.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 179 malicious artifacts.

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
| Modularity | 0.3432 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 95.3 | 31.1 | 6.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 43.7 | 55.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.5 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.6 | 10.0 | 10.5 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.6 | 13.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.0 | 3.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 70.9 | 92.9 | 100.0 |
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

- `P_UseSpecialLine` (@ `src/p_switch.c`) -> Impact: **194.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `M_Responder` (@ `src/m_menu.c`) -> Impact: **164.8** | LOC: 476
- `A_Fire` (@ `src/p_enemy.c`) -> Impact: **138.9** | LOC: 679
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `F_CastTicker` (@ `src/f_finale.c`) -> Impact: **119.4** | LOC: 101
  * *Intent:* // // F_CastTicker //
- `PrintDehackedBanners` (@ `src/d_main.c`) -> Impact: **99.6** | LOC: 522
- `D_Display` (@ `src/d_main.c`) -> Impact: **92.9** | LOC: 161
- `ST_Responder` (@ `src/st_stuff.c`) -> Impact: **82.2** | LOC: 224
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `WI_updateNetgameStats` (@ `src/wi_stuff.c`) -> Impact: **78.3** | LOC: 152
- `P_SpawnSpecials` (@ `src/p_spec.c`) -> Impact: **71.6** | LOC: 116
- `EV_VerticalDoor` (@ `src/p_doors.c`) -> Impact: **66.8** | LOC: 176
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 177 | 31067.7 | 31.27% | 26.49% |
| `__monolith__` | 4 | 623.44 | 23.06% | 0.0% |
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
- `src/p_enemy.c` -> **47** Orphaned Functions | **0** Duplicates
- `src/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `src/p_pspr.c` -> **20** Orphaned Functions | **0** Duplicates
- `src/i_video.c` -> **16** Orphaned Functions | **0** Duplicates
- `src/p_saveg.c` -> **14** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `917` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/i_video.c` (C) -> Cumulative Risk: **684.77**
- **Archetype:** `file_cluster_13` (Distance: 12.727 IQR)
- **Magnitude:** 246.98 | **LOC:** 355 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9724%), Tech Debt (99.548%)
- **Heaviest Functions:** `I_GetPaletteIndex` (Impact: 11.8), `I_FinishUpdate` (Impact: 4.5), `cmap_to_fb` (Impact: 4.2)

### 2. `src/p_enemy.c` (C) -> Cumulative Risk: **664.32**
- **Archetype:** `file_cluster_8` (Distance: 13.598 IQR)
- **Magnitude:** 1552.3 | **LOC:** 2007 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5765%), Cognitive Load (92.821%)
- **Heaviest Functions:** `A_Fire` (Impact: 138.9), `P_NewChaseDir` (Impact: 40.4), `A_Chase` (Impact: 39.2)

### 3. `src/p_pspr.c` (C) -> Cumulative Risk: **664.22**
- **Archetype:** `file_cluster_8` (Distance: 12.919 IQR)
- **Magnitude:** 510.12 | **LOC:** 889 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.005%), Safety Score (90.4255%)
- **Heaviest Functions:** `A_Lower` (Impact: 46.9), `P_CheckAmmo` (Impact: 38.0), `A_WeaponReady` (Impact: 14.7)

### 4. `src/r_draw.c` (C) -> Cumulative Risk: **662.92**
- **Archetype:** `file_cluster_13` (Distance: 14.217 IQR)
- **Magnitude:** 903.48 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6262%), Safety Score (98.8755%)
- **Heaviest Functions:** `R_FillBackScreen` (Impact: 27.6), `R_DrawFuzzColumnLow` (Impact: 20.6), `R_DrawFuzzColumn` (Impact: 20.1)

### 5. `src/p_saveg.c` (C) -> Cumulative Risk: **655.88**
- **Archetype:** `file_cluster_9` (Distance: 21.327 IQR)
- **Magnitude:** 1049.7 | **LOC:** 1892 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Dead Code (97.0116%), Safety Score (95.5238%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 42.3), `P_UnArchiveSpecials` (Impact: 41.3), `P_UnArchiveThinkers` (Impact: 20.0)

### 6. `src/hu_lib.c` (C) -> Cumulative Risk: **646.43**
- **Archetype:** `file_cluster_13` (Distance: 12.889 IQR)
- **Magnitude:** 227.94 | **LOC:** 348 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.788%), Safety Score (93.0017%)
- **Heaviest Functions:** `HUlib_drawTextLine` (Impact: 14.1), `HUlib_eraseTextLine` (Impact: 10.5), `HUlib_drawSText` (Impact: 6.9)

### 7. `src/m_menu.c` (C) -> Cumulative Risk: **645.02**
- **Archetype:** `file_cluster_13` (Distance: 13.198 IQR)
- **Magnitude:** 1065.8 | **LOC:** 2126 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.3528%), Safety Score (93.1884%)
- **Heaviest Functions:** `M_Responder` (Impact: 164.8), `M_Drawer` (Impact: 25.0), `M_WriteText` (Impact: 24.1)

### 8. `src/v_video.c` (C) -> Cumulative Risk: **642.72**
- **Archetype:** `file_cluster_8` (Distance: 13.995 IQR)
- **Magnitude:** 915.06 | **LOC:** 933 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1146%), Documentation (98.6686%)
- **Heaviest Functions:** `V_CopyRect` (Impact: 29.9), `V_DrawPatch` (Impact: 22.9), `V_DrawPatchFlipped` (Impact: 22.9)

### 9. `src/i_cdmus.c` (C) -> Cumulative Risk: **637.54**
- **Archetype:** `file_cluster_8` (Distance: 12.425 IQR)
- **Magnitude:** 172.08 | **LOC:** 244 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.7504%), Safety Score (91.972%)
- **Heaviest Functions:** `I_CDMusInit` (Impact: 11.0), `I_CDMusTrackLength` (Impact: 9.9), `I_CDMusFirstTrack` (Impact: 8.7)

### 10. `src/z_zone.c` (C) -> Cumulative Risk: **636.41**
- **Archetype:** `file_cluster_8` (Distance: 12.98 IQR)
- **Magnitude:** 279.86 | **LOC:** 489 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.2723%), Documentation (96.82%)
- **Heaviest Functions:** `Z_DumpHeap` (Impact: 19.1), `Z_CheckHeap` (Impact: 15.0), `Z_ChangeTag2` (Impact: 12.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.598 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.406 IQR)
- **Top Global Matches:** file_cluster_8: 13.598, file_cluster_13: 13.725, file_cluster_0: 13.84
- **Magnitude:** 1552.3 | **LOC:** 2007 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.821%), Tech Debt (76.7901%)
**Top Internal Functions/Classes:**
  * `A_Fire` (Impact: 138.9)
    * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
  * `P_NewChaseDir` (Impact: 40.4)
  * `A_Chase` (Impact: 39.2)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_BossDeath` (Impact: 37.0)
  * `A_Look` (Impact: 26.1)
    * *Intent:* // // ACTION ROUTINES // // // A_Look // Stay in state until a player is sighted. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 193`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 684`, `dead_code: 6`, `orphaned_logic: 47`
* *Architecture:* `api: 263`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` r_state.h, g_game.h, sounds.h, i_system.h, stdio.h, doomdef.h, doomstat.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/i_scale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.929 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 13.929, file_cluster_13: 14.15, file_cluster_7: 14.301
- **Magnitude:** 1454.88 | **LOC:** 1453 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.7714%), Tech Debt (11.9854%)
**Top Internal Functions/Classes:**
  * `I_Stretch5x` (Impact: 21.1)
    * *Intent:* // 5x stretch (1600x1200)
  * `I_Stretch4x` (Impact: 19.5)
    * *Intent:* // 4x stretch (1280x960)
  * `I_Stretch3x` (Impact: 18.3)
    * *Intent:* // 3x stretch (960x720)
  * `I_Stretch2x` (Impact: 17.1)
    * *Intent:* // 2x stretch (640x480)
  * `I_Stretch1x` (Impact: 15.9)
    * *Intent:* // 1x stretch (320x240)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 102`, `args: 15`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1050`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 121`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdio.h, m_argv.h, i_video.h, string.h, stdlib.h, z_zone.h, doomtype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.216 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.274 IQR)
- **Top Global Matches:** file_cluster_8: 13.216, file_cluster_13: 13.434, file_cluster_7: 13.579
- **Magnitude:** 1435.4 | **LOC:** 1830 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.675%), Tech Debt (25.3459%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` (Impact: 78.3)
  * `WI_updateDeathmatchStats` (Impact: 46.0)
  * `WI_updateStats` (Impact: 44.8)
  * `WI_loadUnloadData` (Impact: 30.4)
  * `WI_updateAnimatedBack` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 111`, `args: 35`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 736`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 159`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` g_game.h, sounds.h, m_misc.h, i_system.h, wi_stuff.h, stdio.h, i_swap.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.198 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_13: 13.198, file_cluster_8: 13.252, file_cluster_11: 13.527
- **Magnitude:** 1065.8 | **LOC:** 2126 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3528%), Tech Debt (65.7778%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 164.8)
  * `M_Drawer` (Impact: 25.0)
  * `M_WriteText` (Impact: 24.1)
  * `M_Init` (Impact: 21.5)
  * `M_SizeDisplay` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 129`, `args: 25`, `func_start: 28`
* *Risk/State:* `state_mutation: 526`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 158`, `import: 25`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` dstrings.h, ctype.h, doomdef.h, doomkeys.h, i_video.h, w_wad.h, p_saveg.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_9` (Drift: 21.327 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.514 IQR)
- **Top Global Matches:** file_cluster_9: 21.327, file_cluster_0: 21.334, file_cluster_11: 21.347
- **Magnitude:** 1049.7 | **LOC:** 1892 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.851%), Tech Debt (26.6428%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` (Impact: 42.3)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `P_UnArchiveSpecials` (Impact: 41.3)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_UnArchiveThinkers` (Impact: 20.0)
    * *Intent:* // // P_UnArchiveThinkers //
  * `saveg_read_player_t` (Impact: 12.5)
    * *Intent:* // // player_t //
  * `saveg_write_player_t` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 86`, `args: 23`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 642`, `dead_code: 128`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 92`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` r_state.h, p_saveg.h, g_game.h, m_misc.h, i_system.h, stdio.h, dstrings.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.507 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.345 IQR)
- **Top Global Matches:** file_cluster_13: 14.507, file_cluster_8: 14.583, file_cluster_11: 14.662
- **Magnitude:** 1000.3 | **LOC:** 980 | **CtrlFlow:** 74.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.9419%), Tech Debt (12.7696%)
**Top Internal Functions/Classes:**
  * `R_InitSpriteDefs` (Impact: 49.1)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawSprite` (Impact: 39.4)
  * `R_ProjectSprite` (Impact: 28.6)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InstallSpriteLump` (Impact: 25.0)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
  * `R_DrawPSprite` (Impact: 21.7)
    * *Intent:* // // R_DrawPSprite //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 45`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 629`, `dead_code: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` i_system.h, stdio.h, i_swap.h, doomdef.h, doomstat.h, r_local.h, w_wad.h, deh_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.791 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.631 IQR)
- **Top Global Matches:** file_cluster_13: 13.791, file_cluster_8: 13.863, file_cluster_0: 14.092
- **Magnitude:** 933.06 | **LOC:** 1417 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.8813%), Tech Debt (23.6657%)
**Top Internal Functions/Classes:**
  * `ST_Responder` (Impact: 82.2)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` (Impact: 56.6)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` (Impact: 25.8)
  * `ST_updateWidgets` (Impact: 20.1)
  * `ST_loadUnloadGraphics` (Impact: 9.5)
    * *Intent:* // Iterates through all graphics to be loaded or unloaded, along with // the variable they use, invo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 91`, `args: 20`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 572`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 88`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` dstrings.h, doomdef.h, doomkeys.h, i_video.h, w_wad.h, m_misc.h, i_system.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.995 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.475 IQR)
- **Top Global Matches:** file_cluster_8: 13.995, file_cluster_13: 14.014, file_cluster_11: 14.323
- **Magnitude:** 915.06 | **LOC:** 933 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.4507%), Tech Debt (87.3855%)
**Top Internal Functions/Classes:**
  * `V_CopyRect` (Impact: 29.9)
    * *Intent:* // // V_CopyRect //
  * `V_DrawPatch` (Impact: 22.9)
    * *Intent:* // // V_DrawPatch // Masks a column based masked pic to the screen. //
  * `V_DrawPatchFlipped` (Impact: 22.9)
    * *Intent:* // // V_DrawPatchFlipped // Masks a column based masked pic to the screen. // Flips horizontally, e....
  * `WritePNGfile` (Impact: 20.3)
  * `V_DrawShadowedPatch` (Impact: 18.4)
    * *Intent:* // // V_DrawShadowedPatch // // Masks a column based masked pic to the screen. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 39`, `args: 21`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 545`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 104`, `import: 15`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` config.h, m_misc.h, i_system.h, stdio.h, deh_str.h, i_swap.h, png.h, m_bbox.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_draw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.217 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.076 IQR)
- **Top Global Matches:** file_cluster_13: 14.217, file_cluster_8: 14.236, file_cluster_0: 14.371
- **Magnitude:** 903.48 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8789%), Tech Debt (96.0301%)
**Top Internal Functions/Classes:**
  * `R_FillBackScreen` (Impact: 27.6)
    * *Intent:* // // R_FillBackScreen // Fills the back screen with a pattern // for variable screen sizes // Also ...
  * `R_DrawFuzzColumnLow` (Impact: 20.6)
    * *Intent:* // low detail mode version
  * `R_DrawFuzzColumn` (Impact: 20.1)
    * *Intent:* // // Framebuffer postprocessing. // Creates a fuzzy image by copying pixels // from adjacent ones t...
  * `R_DrawTranslatedColumnLow` (Impact: 14.7)
  * `R_DrawSpan` (Impact: 14.6)
    * *Intent:* // // Draws the actual span.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 36`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 567`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 9`
* *Architecture:* `api: 123`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` i_system.h, doomdef.h, doomstat.h, w_wad.h, z_zone.h, deh_main.h, r_local.h, v_video.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.242 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.641 IQR)
- **Top Global Matches:** file_cluster_13: 13.242, file_cluster_8: 13.25, file_cluster_11: 13.582
- **Magnitude:** 821.36 | **LOC:** 719 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.5275%), Tech Debt (40.8706%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` (Impact: 119.4)
    * *Intent:* // // F_CastTicker //
  * `F_TextWrite` (Impact: 29.3)
  * `F_CastPrint` (Impact: 28.4)
  * `F_Ticker` (Impact: 26.4)
    * *Intent:* // // F_Ticker //
  * `F_ArtScreenDrawer` (Impact: 20.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 66`, `args: 14`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 394`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` r_state.h, sounds.h, i_system.h, stdio.h, ctype.h, i_swap.h, dstrings.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.618 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.345 IQR)
- **Top Global Matches:** file_cluster_8: 13.618, file_cluster_13: 13.655, file_cluster_0: 13.832
- **Magnitude:** 776.72 | **LOC:** 892 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.6643%), Tech Debt (31.1875%)
**Top Internal Functions/Classes:**
  * `R_InitTextureMapping` (Impact: 29.0)
    * *Intent:* // // R_InitTextureMapping //
  * `R_ExecuteSetViewSize` (Impact: 25.3)
    * *Intent:* // // R_ExecuteSetViewSize //
  * `R_PointToAngle` (Impact: 21.2)
    * *Intent:* // // R_PointToAngle // To get a global angle from cartesian coordinates, // the coordinates are fli...
  * `R_PointOnSegSide` (Impact: 11.1)
  * `R_AddPointToBox` (Impact: 10.8)
    * *Intent:* // // R_AddPointToBox // Expand a given bbox // so that it encloses a given point. //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 61`, `args: 8`, `func_start: 17`
* *Risk/State:* `state_mutation: 456`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 143`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` d_loop.h, m_menu.h, doomdef.h, m_bbox.h, stdlib.h, r_sky.h, r_local.h, math.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.575 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.431 IQR)
- **Top Global Matches:** file_cluster_8: 13.575, file_cluster_13: 13.616, file_cluster_11: 13.824
- **Magnitude:** 677.82 | **LOC:** 779 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.38%), Tech Debt (21.2567%)
**Top Internal Functions/Classes:**
  * `EV_VerticalDoor` (Impact: 66.8)
    * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //
  * `T_VerticalDoor` (Impact: 63.5)
    * *Intent:* #endif // // VERTICAL DOORS // // // T_VerticalDoor //
  * `T_SlidingDoor` (Impact: 25.2)
  * `EV_DoDoor` (Impact: 25.0)
  * `EV_DoLockedDoor` (Impact: 23.8)
    * *Intent:* // // EV_DoLockedDoor // Move a locked door up/down //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 31`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 373`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 70`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` r_state.h, sounds.h, dstrings.h, doomdef.h, doomstat.h, s_sound.h, deh_main.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.357 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.487 IQR)
- **Top Global Matches:** file_cluster_13: 14.357, file_cluster_8: 14.429, file_cluster_11: 14.505
- **Magnitude:** 664.98 | **LOC:** 547 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.1468%), Tech Debt (12.8169%)
**Top Internal Functions/Classes:**
  * `EV_DoFloor` (Impact: 54.3)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `T_MovePlane` (Impact: 42.8)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_BuildStairs` (Impact: 26.1)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` (Impact: 16.2)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 28`, `func_start: 4`
* *Risk/State:* `state_mutation: 454`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 63`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` r_state.h, sounds.h, doomdef.h, doomstat.h, s_sound.h, z_zone.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doomgeneric_ascii.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.697 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.629 IQR)
- **Top Global Matches:** file_cluster_8: 12.697, file_cluster_13: 12.745, file_cluster_11: 13.074
- **Magnitude:** 647.88 | **LOC:** 734 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.3261%), Tech Debt (12.5257%)
**Top Internal Functions/Classes:**
  * `convertToDoomKey` (Impact: 49.5)
  * `DG_DrawFrame` (Impact: 47.7)
  * `DG_Init` (Impact: 31.5)
  * `DG_ReadInput` (Impact: 23.0)
  * `DG_AtExit` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 142`, `args: 14`, `func_start: 16`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 282`, `orphaned_logic: 3`
* *Architecture:* `io: 2`, `api: 173`, `import: 15`
* *Defense:* `safety: 5`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` i_system.h, unistd.h, stdio.h, ctype.h, doomgeneric.h, windows.h, time.h, m_argv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/d_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.63 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.016 IQR)
- **Top Global Matches:** file_cluster_13: 12.63, file_cluster_8: 12.906, file_cluster_11: 13.135
- **Magnitude:** 647.0 | **LOC:** 1841 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.655%), Tech Debt (19.241%)
**Top Internal Functions/Classes:**
  * `PrintDehackedBanners` (Impact: 99.6)
  * `D_Display` (Impact: 92.9)
  * `D_SetGameDescription` (Impact: 29.8)
    * *Intent:* // frame syncronous IO operations
  * `D_DoomMain` (Impact: 27.1)
  * `D_ProcessEvents` (Impact: 9.4)
    * *Intent:* // // D_ProcessEvents // Send all the events of the given timestamp down the responder chain //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 69`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 297`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 70`, `import: 42`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` config.h, net_dedicated.h, net_client.h, dstrings.h, ctype.h, statdump.h, doomdef.h, f_finale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_data.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.858 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_0: 14.375, file_cluster_8: 14.376
- **Magnitude:** 623.7 | **LOC:** 910 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.3643%), Tech Debt (19.5342%)
**Top Internal Functions/Classes:**
  * `R_PrecacheLevel` (Impact: 34.9)
  * `R_GenerateLookup` (Impact: 24.1)
    * *Intent:* // // R_GenerateLookup //
  * `R_GenerateComposite` (Impact: 19.1)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_InitTextures` (Impact: 15.6)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `R_DrawColumnInCache` (Impact: 6.6)
    * *Intent:* // for a column directory and any new columns. // The directory will simply point inside other patch...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 26`, `args: 7`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 364`, `dead_code: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 134`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` m_misc.h, i_system.h, r_data.h, stdio.h, i_swap.h, doomdef.h, doomstat.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_spec.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.127 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.9 IQR)
- **Top Global Matches:** file_cluster_13: 13.127, file_cluster_8: 13.2, file_cluster_11: 13.502
- **Magnitude:** 617.42 | **LOC:** 1490 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_SpawnSpecials` (Impact: 71.6)
  * `P_CrossSpecialLine` (Impact: 65.8)
    * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or...
  * `P_InitPicAnims` (Impact: 17.8)
  * `P_FindNextHighestFloor` (Impact: 13.9)
    * *Intent:* // // P_FindNextHighestFloor // FIND NEXT HIGHEST FLOOR IN SURROUNDING SECTORS // Note: this should ...
  * `P_FindMinSurroundingLight` (Impact: 6.2)
    * *Intent:* // // Find minimum light from an adjacent sector //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 54`, `args: 6`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 295`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 100`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` r_state.h, g_game.h, sounds.h, m_misc.h, i_system.h, m_random.h, doomdef.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.373 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.306 IQR)
- **Top Global Matches:** file_cluster_13: 13.373, file_cluster_8: 13.444, file_cluster_11: 13.692
- **Magnitude:** 616.1 | **LOC:** 1449 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6916%), Tech Debt (48.7248%)
**Top Internal Functions/Classes:**
  * `PTR_SlideTraverse` (Impact: 28.9)
  * `SpechitOverrun` (Impact: 18.9)
  * `P_CheckPosition` (Impact: 11.4)
  * `P_TryMove` (Impact: 10.7)
  * `PIT_RadiusAttack` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 105`, `func_start: 13`
* *Risk/State:* `state_mutation: 356`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 127`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` r_state.h, sounds.h, m_misc.h, i_system.h, stdio.h, doomdef.h, m_argv.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.058 IQR)
- **Top Global Matches:** file_cluster_8: 10.058, file_cluster_12: 10.3, file_cluster_17: 10.561
- **Magnitude:** 552.96 | **LOC:** 144 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
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

### `src/p_maputl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.64 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.527 IQR)
- **Top Global Matches:** file_cluster_8: 13.64, file_cluster_13: 13.8, file_cluster_7: 14.048
- **Magnitude:** 519.02 | **LOC:** 1002 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9525%), Tech Debt (21.1002%)
**Top Internal Functions/Classes:**
  * `P_BoxOnLineSide` (Impact: 15.2)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
  * `P_UnsetThingPosition` (Impact: 10.3)
    * *Intent:* // // THING POSITION SETTING // // // P_UnsetThingPosition // Unlinks a thing from block map and sec...
  * `P_PointOnDivlineSide` (Impact: 10.2)
    * *Intent:* // // P_PointOnDivlineSide // Returns 0 or 1. //
  * `PIT_AddThingIntercepts` (Impact: 8.4)
  * `P_PointOnLineSide` (Impact: 7.8)
    * *Intent:* // // P_PointOnLineSide // Returns 0 or 1 //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 46`, `func_start: 9`
* *Risk/State:* `state_mutation: 352`, `orphaned_logic: 4`
* *Architecture:* `api: 88`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` r_state.h, doomdef.h, doomstat.h, m_bbox.h, stdlib.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_pspr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.919 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.416 IQR)
- **Top Global Matches:** file_cluster_8: 12.919, file_cluster_13: 13.056, file_cluster_7: 13.337
- **Magnitude:** 510.12 | **LOC:** 889 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.9199%), Tech Debt (86.4414%)
**Top Internal Functions/Classes:**
  * `A_Lower` (Impact: 46.9)
    * *Intent:* // // A_Lower // Lowers current weapon, // and changes weapon at bottom. //
  * `P_CheckAmmo` (Impact: 38.0)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` (Impact: 14.7)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` (Impact: 11.2)
    * *Intent:* #include "p_pspr.h" #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM...
  * `A_BFGSpray` (Impact: 6.5)
    * *Intent:* // // A_FireShotgun
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 41`, `func_start: 27`
* *Risk/State:* `state_mutation: 241`, `dead_code: 1`, `orphaned_logic: 20`
* *Architecture:* `api: 83`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` sounds.h, doomdef.h, doomstat.h, p_pspr.h, s_sound.h, m_random.h, deh_misc.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.792 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.794 IQR)
- **Top Global Matches:** file_cluster_13: 13.792, file_cluster_8: 13.896, file_cluster_11: 14.088
- **Magnitude:** 488.32 | **LOC:** 1050 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.6866%), Tech Debt (91.8192%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 50.4)
    * *Intent:* // // P_XYMovement // #define STOPSPEED 0x1000 #define FRICTION 0xe800
  * `P_ZMovement` (Impact: 37.8)
    * *Intent:* // // P_ZMovement //
  * `P_SpawnPlayerMissile` (Impact: 7.7)
  * `P_SpawnBlood` (Impact: 7.1)
  * `P_SetMobjState` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 25`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 293`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 57`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` sounds.h, i_system.h, stdio.h, doomdef.h, doomstat.h, st_stuff.h, hu_stuff.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.836 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.829 IQR)
- **Top Global Matches:** file_cluster_13: 13.836, file_cluster_8: 13.911, file_cluster_11: 14.087
- **Magnitude:** 481.82 | **LOC:** 744 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4985%), Tech Debt (15.6698%)
**Top Internal Functions/Classes:**
  * `R_RenderSegLoop` (Impact: 56.6)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
  * `R_StoreWallRange` (Impact: 37.7)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` (Impact: 21.4)
    * *Intent:* // // R_RenderMaskedSegRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 10`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` i_system.h, stdio.h, doomdef.h, doomstat.h, stdlib.h, r_sky.h, r_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.696 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.927 IQR)
- **Top Global Matches:** file_cluster_8: 12.696, file_cluster_13: 12.696, file_cluster_7: 13.12
- **Magnitude:** 449.22 | **LOC:** 671 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.3537%), Tech Debt (37.102%)
**Top Internal Functions/Classes:**
  * `S_StartSound` (Impact: 30.3)
  * `S_ChangeMusic` (Impact: 17.9)
  * `S_UpdateSounds` (Impact: 17.3)
    * *Intent:* // // Updates music & sounds //
  * `S_GetChannel` (Impact: 16.6)
    * *Intent:* // // S_GetChannel : // If none available, return -1. Otherwise channel #. //
  * `S_AdjustSoundParams` (Impact: 14.3)
    * *Intent:* // // Changes volume and stereo-separation variables // from the norm of a sound effect to be played...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 40`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` sounds.h, m_misc.h, i_system.h, stdio.h, deh_str.h, doomstat.h, m_argv.h, i_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/r_bsp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.134 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.932 IQR)
- **Top Global Matches:** file_cluster_13: 13.134, file_cluster_8: 13.139, file_cluster_11: 13.405
- **Magnitude:** 434.98 | **LOC:** 574 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.7581%), Tech Debt (14.9297%)
**Top Internal Functions/Classes:**
  * `R_CheckBBox` (Impact: 24.4)
  * `R_AddLine` (Impact: 23.9)
    * *Intent:* // // R_AddLine // Clips the given segment // and adds any visible pieces to the line list. //
  * `R_ClipSolidWallSegment` (Impact: 23.2)
    * *Intent:* // // R_ClipSolidWallSegment // Does handle solid walls, // e.g. single sided LineDefs (middle textu...
  * `R_Subsector` (Impact: 18.3)
    * *Intent:* // // R_Subsector // Determine floor/ceiling planes. // Add sprites of things in sector. // Draw one...
  * `R_ClipPassWallSegment` (Impact: 14.3)
    * *Intent:* // // R_ClipPassWallSegment // Clips the given range of columns, // but does not includes it in the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 40`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 238`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 71`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` r_state.h, i_system.h, r_things.h, doomdef.h, doomstat.h, r_plane.h, m_bbox.h, r_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/r_bsp.c` (C) | Magnitude: 434.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 238, indent_spaces: 174, pointers: 74, indent_tabs: 72
- `src/f_finale.c` (C) | Magnitude: 821.36 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 394, indent_spaces: 275, branch: 149, api: 115
- `src/r_draw.c` (C) | Magnitude: 903.48 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 567, indent_spaces: 283, indent_tabs: 139, api: 123
- `src/m_bbox.c` (C) | Magnitude: 31.42 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 8, branch: 6, api: 6
- `src/doomstat.h` (C) | Magnitude: 80.52 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 64, structural_boundaries: 22, import: 5, macros: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/s_sound.c` (C) | Magnitude: 449.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 347, state_mutation: 220, branch: 86, pointers: 84
- `src/f_wipe.c` (C) | Magnitude: 327.7 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 180, indent_spaces: 92, api: 57, indent_tabs: 45
- `src/v_video.c` (C) | Magnitude: 915.06 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 545, indent_spaces: 430, pointers: 173, api: 104
- `src/doomdef.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `src/d_player.h` (C) | Magnitude: 77.64 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, api: 58, structural_boundaries: 16, class_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/p_saveg.c` (C) | Magnitude: 1049.7 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
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

- `src/d_event.h` -> **Severity: 13.593** (Embedded: 0.1642 * Error Risk: 82.7987%)
- `src/doomdef.h` -> **Severity: 13.484** (Embedded: 0.2308 * Error Risk: 58.4099%)
- `src/z_zone.h` -> **Severity: 13.204** (Embedded: 0.2155 * Error Risk: 61.2821%)
- `src/d_mode.h` -> **Severity: 11.261** (Embedded: 0.1918 * Error Risk: 58.6996%)
- `src/p_mobj.h` -> **Severity: 8.77** (Embedded: 0.1222 * Error Risk: 71.7669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/net_defs.h` -> **Severity: 2275.3** (Blast Radius: 22.753 * Doc Risk: 100.0%)
- `src/doomtype.h` -> **Severity: 1958.028** (Blast Radius: 164.26 * Doc Risk: 11.9203%)
- `src/d_mode.h` -> **Severity: 1912.962** (Blast Radius: 19.902 * Doc Risk: 96.1191%)
- `src/d_ticcmd.h` -> **Severity: 1802.478** (Blast Radius: 18.027 * Doc Risk: 99.9877%)
- `src/d_event.h` -> **Severity: 1448.396** (Blast Radius: 21.152 * Doc Risk: 68.4756%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
