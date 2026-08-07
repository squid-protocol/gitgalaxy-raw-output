# ARCHITECTURAL_BRIEF: normal_esp32_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_esp32_doom` |
| **Timestamp** | `2026-08-07T03:29:36.368310+00:00` |
| **Scan Duration** | `0.89s` |
| **Git Branch** | `master` |
| **Git Commit** | `085f21b630f11adb69a3894db5a1efa39a7aa31a` |
| **Git Remote** | `https://github.com/espressif/esp32-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 178 malicious artifacts.

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
| Modularity | 0.3313 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 34.4 | 7.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 48.9 | 59.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 22.4 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.3 | 9.3 | 10.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.9 | 42.8 | 100.0 |
| Commented Logic Exposure | 0.0 | 52.6 | 2.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 1.6 | 100.0 | 62.2 | 78.7 | 11.9 |
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

- `G_BuildTiccmd` (@ `components/prboom/g_game.c`) -> Impact: **361.9** | LOC: 622
- `P_ChangeSwitchTexture` (@ `components/prboom/p_switch.c`) -> Impact: **355.6** | LOC: 752
- `V_DrawMemPatch` (@ `components/prboom/v_video.c`) -> Impact: **341.8** | LOC: 592
- `D_BuildBEXTables` (@ `components/prboom/d_deh.c`) -> Impact: **294.1** | LOC: 565
- `getConvertedDEHBits` (@ `components/prboom/d_deh.c`) -> Impact: **289.8** | LOC: 396
- `AM_Responder` (@ `components/prboom/am_map.c`) -> Impact: **288.7** | LOC: 598
- `WI_drawTime` (@ `components/prboom/wi_stuff.c`) -> Impact: **281.1** | LOC: 622
- `HU_Start` (@ `components/prboom/hu_stuff.c`) -> Impact: **234.8** | LOC: 567
- `R_RenderMaskedSegRange` (@ `components/prboom/r_segs.c`) -> Impact: **208.0** | LOC: 592
- `gld_PointOnSide` (@ `components/prboom/gl_main.c`) -> Impact: **187.4** | LOC: 439

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `components/prboom` | 74 | 33440.24 | 63.68% | 40.48% |
| `components/prboom/include` | 74 | 2849.4 | 9.04% | 4.0% |
| `components/prboom-esp32-compat` | 10 | 1027.28 | 41.06% | 57.39% |
| `components/prboom/native` | 7 | 635.82 | 39.21% | 75.8% |
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
- `components/prboom/gl_main.c` -> **21** Orphaned Functions | **0** Duplicates
- `components/prboom-esp32-compat/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates
- `components/prboom/native/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1076` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `components/prboom/p_enemy.c` (C) -> Cumulative Risk: **659.78**
- **Archetype:** `file_cluster_13` (Distance: 14.191 IQR)
- **Magnitude:** 1356.88 | **LOC:** 2602 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.9222%), Cognitive Load (96.3846%)
- **Heaviest Functions:** `A_BossDeath` (Impact: 70.8), `P_IsOnLift` (Impact: 39.1), `P_DoNewChaseDir` (Impact: 35.7)

### 2. `components/prboom/r_plane.c` (C) -> Cumulative Risk: **648.3**
- **Archetype:** `file_cluster_13` (Distance: 14.226 IQR)
- **Magnitude:** 508.7 | **LOC:** 471 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5887%), Documentation (96.6077%)
- **Heaviest Functions:** `R_MapPlane` (Impact: 32.0), `R_MakeSpans` (Impact: 24.5), `R_DoDrawPlane` (Impact: 21.7)

### 3. `components/prboom-esp32-compat/i_system.c` (C) -> Cumulative Risk: **644.62**
- **Archetype:** `file_cluster_13` (Distance: 12.782 IQR)
- **Magnitude:** 297.36 | **LOC:** 344 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9418%), Tech Debt (97.3207%)
- **Heaviest Functions:** `I_Mmap` (Impact: 17.5), `I_Lseek` (Impact: 12.5), `I_Munmap` (Impact: 11.0)

### 4. `components/prboom/p_plats.c` (C) -> Cumulative Risk: **625.21**
- **Archetype:** `file_cluster_13` (Distance: 17.147 IQR)
- **Magnitude:** 383.46 | **LOC:** 438 | **CtrlFlow:** 86.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.9205%), Cognitive Load (93.8899%)
- **Heaviest Functions:** `T_PlatRaise` (Impact: 68.8), `P_ActivateInStasis` (Impact: 12.9), `EV_StopPlat` (Impact: 4.8)

### 5. `components/prboom/r_fps.c` (C) -> Cumulative Risk: **624.05**
- **Archetype:** `file_cluster_8` (Distance: 13.329 IQR)
- **Magnitude:** 558.06 | **LOC:** 451 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4888%), Documentation (99.2514%)
- **Heaviest Functions:** `R_DoAnInterpolation` (Impact: 31.8), `R_CopyInterpToOld` (Impact: 29.4), `R_CopyBakToInterp` (Impact: 29.4)

### 6. `components/prboom/p_pspr.c` (C) -> Cumulative Risk: **623.73**
- **Archetype:** `file_cluster_13` (Distance: 13.375 IQR)
- **Magnitude:** 352.86 | **LOC:** 830 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.7502%), Safety Score (95.9469%)
- **Heaviest Functions:** `A_Lower` (Impact: 50.5), `P_SetPsprite` (Impact: 10.9), `A_BFGSpray` (Impact: 8.4)

### 7. `components/prboom/p_mobj.c` (C) -> Cumulative Risk: **621.41**
- **Archetype:** `file_cluster_13` (Distance: 14.68 IQR)
- **Magnitude:** 758.1 | **LOC:** 1533 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3383%), Cognitive Load (82.7452%)
- **Heaviest Functions:** `P_XYMovement` (Impact: 77.7), `P_IsDoomnumAllowed` (Impact: 23.6), `P_SpawnMapThing` (Impact: 22.2)

### 8. `components/prboom/p_saveg.c` (C) -> Cumulative Risk: **619.57**
- **Archetype:** `file_cluster_8` (Distance: 14.294 IQR)
- **Magnitude:** 1238.14 | **LOC:** 1030 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4673%), Documentation (95.9516%)
- **Heaviest Functions:** `P_ArchiveSpecials` (Impact: 115.9), `P_UnArchiveSpecials` (Impact: 61.7), `P_UnArchiveThinkers` (Impact: 30.6)

### 9. `components/prboom/native/i_system.c` (C) -> Cumulative Risk: **615.45**
- **Archetype:** `file_cluster_13` (Distance: 11.712 IQR)
- **Magnitude:** 123.48 | **LOC:** 209 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.9002%)
- **Heaviest Functions:** `I_Lseek` (Impact: 12.5), `I_Open` (Impact: 7.6), `I_Read` (Impact: 4.4)

### 10. `components/prboom/r_patch.c` (C) -> Cumulative Risk: **612.41**
- **Archetype:** `file_cluster_13` (Distance: 14.178 IQR)
- **Magnitude:** 712.18 | **LOC:** 788 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3926%), Documentation (98.4873%)
- **Heaviest Functions:** `createPatch` (Impact: 131.6), `getPatchIsNotTileable` (Impact: 20.4), `R_CachePatchNum` (Impact: 13.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `components/prboom/gl_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.283 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.721 IQR)
- **Top Global Matches:** file_cluster_8: 14.283, file_cluster_13: 14.309, file_cluster_11: 14.466
- **Magnitude:** 2116.94 | **LOC:** 2721 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.8559%), Tech Debt (20.8177%)
**Top Internal Functions/Classes:**
  * `gld_PointOnSide` (Impact: 187.4)
  * `gld_AddWall` (Impact: 69.1)
  * `gld_Init` (Impact: 68.4)
  * `gld_InitExtensions` (Impact: 42.6)
  * `gld_DrawScene` (Impact: 40.2)
    * *Intent:* // e6y // Sky textures with a zero index should be forced // See third episode of requiem.wad #defin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 135`, `args: 25`, `func_start: 37`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1209`, `dead_code: 9`, `orphaned_logic: 21`
* *Architecture:* `io: 3`, `api: 237`, `import: 26`
* *Defense:* `safety: 1`, `doc: 6`, `immutability_locks: 14`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` windows.h, r_fps.h, d_event.h, gl_struct.h, r_plane.h, r_main.h, r_draw.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_deh.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.553 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.406 IQR)
- **Top Global Matches:** file_cluster_8: 13.553, file_cluster_13: 13.657, file_cluster_0: 13.773
- **Magnitude:** 2042.86 | **LOC:** 3096 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.3444%), Tech Debt (24.6642%)
**Top Internal Functions/Classes:**
  * `D_BuildBEXTables` (Impact: 294.1)
  * `getConvertedDEHBits` (Impact: 289.8)
  * `setMobjInfoValue` (Impact: 59.7)
    * *Intent:* // to hold startup code pointers from INFO.C // CPhipps - static
  * `deh_procThing` (Impact: 40.3)
  * `deh_procStrings` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 88`, `args: 15`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 789`, `dead_code: 4`, `fragile_debt: 5`, `orphaned_logic: 6`
* *Architecture:* `io: 7`, `api: 400`, `import: 14`
* *Defense:* `safety: 13`, `immutability_locks: 333`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` p_enemy.h, d_deh.h, g_game.h, doomdef.h, sounds.h, lprintf.h, d_think.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.437 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.639 IQR)
- **Top Global Matches:** file_cluster_8: 14.437, file_cluster_13: 14.44, file_cluster_11: 14.677
- **Magnitude:** 1469.24 | **LOC:** 1042 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.2196%), Tech Debt (24.9802%)
**Top Internal Functions/Classes:**
  * `V_DrawMemPatch` (Impact: 341.8)
  * `FUNC_V_DrawBackground` (Impact: 37.8)
    * *Intent:* // // V_CopyRect // // Copies a source rectangle in a screen buffer to a destination
  * `FUNC_V_CopyRect` (Impact: 36.7)
    * *Intent:* /* * V_InitColorTranslation * * Loads the color translation tables from predefined lumps at game sta...
  * `WRAP_V_DrawLine` (Impact: 24.8)
  * `V_InitMode` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 72`, `args: 34`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 771`, `orphaned_logic: 8`
* *Architecture:* `api: 113`, `import: 10`
* *Defense:* `immutability_locks: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` i_video.h, doomdef.h, v_video.h, GAMMATBL.h, r_filter.h, esp_attr.h, r_draw.h, m_bbox.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.191 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.186 IQR)
- **Top Global Matches:** file_cluster_13: 14.191, file_cluster_8: 14.272, file_cluster_11: 14.334
- **Magnitude:** 1356.88 | **LOC:** 2602 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3846%), Tech Debt (77.9128%)
**Top Internal Functions/Classes:**
  * `A_BossDeath` (Impact: 70.8)
  * `P_IsOnLift` (Impact: 39.1)
  * `P_DoNewChaseDir` (Impact: 35.7)
  * `P_Move` (Impact: 29.4)
  * `P_NewChaseDir` (Impact: 28.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 166`, `args: 1`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 702`, `dead_code: 6`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `api: 183`, `import: 15`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` p_enemy.h, p_setup.h, g_game.h, p_spec.h, sounds.h, p_tick.h, s_sound.h, p_inter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.015 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.474 IQR)
- **Top Global Matches:** file_cluster_8: 13.015, file_cluster_13: 13.077, file_cluster_0: 13.295
- **Magnitude:** 1333.8 | **LOC:** 1969 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.1552%), Tech Debt (42.154%)
**Top Internal Functions/Classes:**
  * `WI_drawTime` (Impact: 281.1)
  * `WI_updateDeathmatchStats` (Impact: 159.9)
  * `WI_updateStats` (Impact: 56.7)
    * *Intent:* // ====================================================================
  * `WI_updateAnimatedBack` (Impact: 29.3)
  * `WI_drawOnLnode` (Impact: 23.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 78`, `args: 27`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 441`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 115`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 24`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` g_game.h, sounds.h, v_video.h, wi_stuff.h, s_sound.h, r_main.h, r_draw.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.294 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.635 IQR)
- **Top Global Matches:** file_cluster_8: 14.294, file_cluster_13: 14.344, file_cluster_11: 14.499
- **Magnitude:** 1238.14 | **LOC:** 1030 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.0204%), Tech Debt (60.2168%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` (Impact: 115.9)
  * `P_UnArchiveSpecials` (Impact: 61.7)
  * `P_UnArchiveThinkers` (Impact: 30.6)
  * `P_ArchiveThinkers` (Impact: 28.2)
  * `P_ArchiveWorld` (Impact: 17.6)
    * *Intent:* // // P_UnArchivePlayers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 55`, `args: 14`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 810`, `fragile_debt: 3`, `orphaned_logic: 10`
* *Architecture:* `io: 4`, `api: 100`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` p_saveg.h, p_enemy.h, p_tick.h, p_spec.h, r_main.h, doomstat.h, am_map.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.554 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.127 IQR)
- **Top Global Matches:** file_cluster_13: 14.554, file_cluster_8: 14.645, file_cluster_11: 14.667
- **Magnitude:** 1192.88 | **LOC:** 1079 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.5179%), Tech Debt (12.0436%)
**Top Internal Functions/Classes:**
  * `R_InitSpriteDefs` (Impact: 68.9)
  * `R_DrawSprite` (Impact: 62.1)
  * `R_ProjectSprite` (Impact: 46.0)
  * `R_DrawPSprite` (Impact: 31.2)
  * `R_InstallSpriteLump` (Impact: 19.4)
    * *Intent:* // // Sprite rotation 0 is facing the viewer, // rotation 1 is one angle turn CLOCKWISE around the a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 43`, `args: 8`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `state_mutation: 752`, `dead_code: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 125`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` r_fps.h, r_segs.h, v_video.h, r_bsp.h, r_things.h, r_main.h, r_draw.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_setup.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.998 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 14.998, file_cluster_11: 15.281, file_cluster_0: 15.32
- **Magnitude:** 1116.72 | **LOC:** 1689 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.1576%), Tech Debt (39.1247%)
**Top Internal Functions/Classes:**
  * `P_CreateBlockMap` (Impact: 51.6)
  * `P_LoadReject` (Impact: 43.7)
    * *Intent:* // // jff 10/6/98 // New code added to speed up calculation of internal blockmap // Algorithm is ord...
  * `P_RemoveSlimeTrails` (Impact: 29.7)
  * `P_GetNodesVersion` (Impact: 20.8)
  * `P_LoadSegs` (Impact: 20.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 41`, `args: 16`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `state_mutation: 704`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 125`, `import: 20`
* *Defense:* `safety: 2`, `doc: 63`, `immutability_locks: 33`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` r_fps.h, g_game.h, r_demo.h, r_main.h, w_wad.h, p_setup.h, lprintf.h, p_maputl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/g_game.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.878 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.384 IQR)
- **Top Global Matches:** file_cluster_13: 13.878, file_cluster_11: 14.233, file_cluster_0: 14.266
- **Magnitude:** 1109.96 | **LOC:** 2923 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.0258%), Tech Debt (45.3836%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` (Impact: 361.9)
  * `G_Ticker` (Impact: 111.7)
  * `G_SetFastParms` (Impact: 13.6)
  * `G_ReloadDefaults` (Impact: 13.1)
  * `fudgef` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 57`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 382`, `dead_code: 8`, `fragile_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 173`, `import: 41`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` hu_stuff.h, g_game.h, r_fps.h, r_demo.h, i_main.h, p_inter.h, r_main.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/hu_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.466 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.292 IQR)
- **Top Global Matches:** file_cluster_8: 13.466, file_cluster_13: 13.589, file_cluster_7: 13.801
- **Magnitude:** 1101.7 | **LOC:** 1594 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4828%), Tech Debt (12.1161%)
**Top Internal Functions/Classes:**
  * `HU_Start` (Impact: 234.8)
  * `HU_Drawer` (Impact: 162.0)
  * `HU_Init` (Impact: 38.0)
  * `HU_MoveHud` (Impact: 23.8)
  * `HU_Stop` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 29`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 549`, `orphaned_logic: 3`
* *Architecture:* `api: 79`, `import: 11`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` hu_stuff.h, st_stuff.h, d_deh.h, sounds.h, g_game.h, hu_lib.h, s_sound.h, r_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.245 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.317 IQR)
- **Top Global Matches:** file_cluster_13: 15.245, file_cluster_11: 15.377, file_cluster_0: 15.404
- **Magnitude:** 1016.4 | **LOC:** 857 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9737%), Tech Debt (12.1994%)
**Top Internal Functions/Classes:**
  * `R_RenderMaskedSegRange` (Impact: 208.0)
  * `R_StoreWallRange` (Impact: 107.3)
  * `R_RenderSegLoop` (Impact: 61.3)
    * *Intent:* // killough 1/25/98: here's where Medusa came in, because // it implicitly assumed that the column w...
  * `R_ScaleFromGlobalAngle` (Impact: 4.5)
  * `R_PointToDist` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 12`, `args: 2`, `func_start: 5`
* *Risk/State:* `state_mutation: 572`, `dead_code: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 51`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` r_segs.h, v_video.h, r_bsp.h, esp_attr.h, r_things.h, r_plane.h, r_main.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/gl_texture.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.788 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.545 IQR)
- **Top Global Matches:** file_cluster_13: 13.788, file_cluster_8: 13.879, file_cluster_11: 14.074
- **Magnitude:** 1004.68 | **LOC:** 960 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.2174%), Tech Debt (11.0057%)
**Top Internal Functions/Classes:**
  * `gld_AddPatchToTexture` (Impact: 30.6)
  * `gld_Precache` (Impact: 27.6)
  * `gld_AddPatchToTexture_UnTranslated` (Impact: 26.1)
  * `gld_RegisterTexture` (Impact: 24.6)
  * `gld_BindTexture` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 78`, `args: 11`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 614`, `dead_code: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 99`, `import: 25`
* *Defense:* `safety: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` windows.h, d_event.h, gl_struct.h, r_plane.h, r_main.h, r_draw.h, w_wad.h, lprintf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.28 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_8: 13.28, file_cluster_7: 13.341, file_cluster_13: 13.358
- **Magnitude:** 921.84 | **LOC:** 5565 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.4063%), Tech Debt (58.3033%)
**Top Internal Functions/Classes:**
  * `M_DrawInstructions` (Impact: 48.1)
  * `M_DrawSetting` (Impact: 34.5)
  * `M_Init` (Impact: 16.9)
    * *Intent:* // Note that the Y values are ascending. If you need to add something to // this table, (well, this ...
  * `M_DrawScreenItems` (Impact: 11.3)
  * `M_Episode` (Impact: 9.6)
    * *Intent:* // // MainMenu is the definition of what the main menu Screen should look // like. Each entry shows ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 150`, `args: 37`, `func_start: 41`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 503`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 23`
* *Architecture:* `api: 143`, `import: 24`
* *Defense:* `doc: 277`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` hu_stuff.h, g_game.h, r_fps.h, r_demo.h, i_main.h, r_main.h, w_wad.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_genlin.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.094 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.175 IQR)
- **Top Global Matches:** file_cluster_13: 15.094, file_cluster_11: 15.138, file_cluster_0: 15.264
- **Magnitude:** 902.94 | **LOC:** 1165 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9002%), Tech Debt (29.4676%)
**Top Internal Functions/Classes:**
  * `EV_DoGenFloor` (Impact: 80.8)
    * *Intent:* * This program is free software; you can redistribute it and/or * modify it under the terms of the G...
  * `EV_DoGenDoor` (Impact: 66.0)
  * `EV_DoGenLift` (Impact: 60.0)
  * `EV_DoGenCrusher` (Impact: 34.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 26`, `func_start: 4`
* *Risk/State:* `state_mutation: 551`, `dead_code: 6`, `planned_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 101`, `import: 7`
* *Defense:* `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` p_tick.h, p_spec.h, sounds.h, s_sound.h, r_main.h, doomstat.h, m_random.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/am_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.295 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.28 IQR)
- **Top Global Matches:** file_cluster_13: 13.295, file_cluster_8: 13.419, file_cluster_11: 13.52
- **Magnitude:** 898.12 | **LOC:** 1586 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.9217%), Tech Debt (30.234%)
**Top Internal Functions/Classes:**
  * `AM_Responder` (Impact: 288.7)
  * `AM_drawWalls` (Impact: 122.2)
  * `AM_drawThings` (Impact: 40.8)
  * `AM_drawPlayers` (Impact: 19.4)
    * *Intent:* // // AM_minOutWindowScale()
  * `AM_drawMarks` (Impact: 17.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 39`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 274`, `dead_code: 5`, `fragile_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 87`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` st_stuff.h, d_deh.h, p_spec.h, g_game.h, v_video.h, r_main.h, doomstat.h, am_map.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.68 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.987 IQR)
- **Top Global Matches:** file_cluster_13: 14.68, file_cluster_11: 14.781, file_cluster_0: 14.914
- **Magnitude:** 758.1 | **LOC:** 1533 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.7452%), Tech Debt (72.8069%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` (Impact: 77.7)
  * `P_IsDoomnumAllowed` (Impact: 23.6)
  * `P_SpawnMapThing` (Impact: 22.2)
  * `P_SetMobjState` (Impact: 15.9)
    * *Intent:* * Copyright 2005, 2006 by * Florian Schulze, Colin Phipps, Neil Stevens, Andrey Budko * * This progr...
  * `P_SpawnPlayer` (Impact: 15.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 41`, `args: 4`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 460`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 82`, `import: 16`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` st_stuff.h, hu_stuff.h, doomdef.h, p_tick.h, sounds.h, g_game.h, lprintf.h, r_demo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_patch.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.178 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.94 IQR)
- **Top Global Matches:** file_cluster_13: 14.178, file_cluster_11: 14.449, file_cluster_8: 14.478
- **Magnitude:** 712.18 | **LOC:** 788 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.6278%), Tech Debt (22.6389%)
**Top Internal Functions/Classes:**
  * `createPatch` (Impact: 131.6)
  * `getPatchIsNotTileable` (Impact: 20.4)
  * `R_CachePatchNum` (Impact: 13.7)
  * `R_FlushAllPatches` (Impact: 10.9)
    * *Intent:* // // Patches. // A patch holds one or more columns. // Patches are used for sprites and all masked ...
  * `R_UnlockTextureCompositePatchNum` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 28`, `args: 7`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 419`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 74`, `import: 13`
* *Defense:* `safety: 4`, `test: 2`, `immutability_locks: 53`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` p_tick.h, r_bsp.h, r_sky.h, r_things.h, z_zone.h, assert.h, r_main.h, r_draw.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.857 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_13: 13.857, file_cluster_8: 13.943, file_cluster_0: 14.059
- **Magnitude:** 674.16 | **LOC:** 1161 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.1612%), Tech Debt (17.2392%)
**Top Internal Functions/Classes:**
  * `ST_updateFaceWidget` (Impact: 56.8)
  * `ST_doPaletteStuff` (Impact: 26.4)
    * *Intent:* // used by the w_armsbg widget
  * `ST_drawWidgets` (Impact: 25.0)
  * `ST_updateWidgets` (Impact: 23.1)
  * `ST_Responder` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 55`, `args: 16`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 402`, `dead_code: 8`, `orphaned_logic: 6`
* *Architecture:* `api: 56`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` i_video.h, st_stuff.h, doomdef.h, sounds.h, m_cheat.h, s_sound.h, r_main.h, st_lib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_client.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.688 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.343 IQR)
- **Top Global Matches:** file_cluster_13: 13.688, file_cluster_11: 13.987, file_cluster_8: 14.035
- **Magnitude:** 644.16 | **LOC:** 543 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.5736%), Tech Debt (25.6433%)
**Top Internal Functions/Classes:**
  * `NetUpdate` (Impact: 54.5)
  * `TryRunTics` (Impact: 34.4)
  * `CheckQueuedPackets` (Impact: 29.4)
  * `D_InitNetGame` (Impact: 27.8)
    * *Intent:* #include <sys/wait.h> #endif #ifdef USE_SDL_NET #include "SDL.h" #endif #include "doomtype.h" #inclu...
  * `D_NetGetWad` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 49`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 384`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 70`, `import: 21`
* *Defense:* `safety: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` r_fps.h, g_game.h, i_main.h, p_checksum.h, lprintf.h, d_net.h, protocol.h, i_network.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.35 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.542 IQR)
- **Top Global Matches:** file_cluster_13: 13.35, file_cluster_8: 13.49, file_cluster_11: 13.602
- **Magnitude:** 639.44 | **LOC:** 689 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.1076%), Tech Debt (34.653%)
**Top Internal Functions/Classes:**
  * `S_StartSoundAtVolume` (Impact: 78.8)
    * *Intent:* // start new music for the level
  * `S_getChannel` (Impact: 31.9)
  * `S_UpdateSounds` (Impact: 30.5)
    * *Intent:* // // Stop and resume music, during game PAUSE. //
  * `S_ChangeMusic` (Impact: 20.2)
  * `S_StopChannel` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 59`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 273`, `dead_code: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 67`, `import: 10`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` i_sound.h, s_sound.h, d_main.h, r_main.h, doomstat.h, config.h, m_random.h, i_system.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.382 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.268 IQR)
- **Top Global Matches:** file_cluster_13: 15.382, file_cluster_11: 15.509, file_cluster_0: 15.567
- **Magnitude:** 596.92 | **LOC:** 1043 | **CtrlFlow:** 89.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.3989%), Tech Debt (90.8495%)
**Top Internal Functions/Classes:**
  * `EV_BuildStairs` (Impact: 60.4)
    * *Intent:* // moving a ceiling up
  * `T_MovePlane` (Impact: 28.9)
    * *Intent:* * This program is distributed in the hope that it will be useful, * but WITHOUT ANY WARRANTY; withou...
  * `EV_DoDonut` (Impact: 18.6)
  * `EV_DoElevator` (Impact: 18.6)
  * `EV_DoChange` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 14`, `func_start: 6`
* *Risk/State:* `state_mutation: 386`, `dead_code: 7`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 60`, `import: 7`
* *Defense:* `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` p_tick.h, p_spec.h, sounds.h, s_sound.h, r_main.h, doomstat.h, p_map.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.015 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.082 IQR)
- **Top Global Matches:** file_cluster_13: 13.015, file_cluster_8: 13.026, file_cluster_11: 13.363
- **Magnitude:** 580.82 | **LOC:** 669 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.9582%), Tech Debt (22.8298%)
**Top Internal Functions/Classes:**
  * `F_CastTicker` (Impact: 119.4)
  * `F_CastPrint` (Impact: 31.5)
  * `F_Drawer` (Impact: 27.6)
  * `F_TextWrite` (Impact: 22.7)
    * *Intent:* // // F_StartFinale
  * `F_BunnyScroll` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 41`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 266`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 77`, `import: 9`
* *Defense:* `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` d_deh.h, hu_stuff.h, d_event.h, sounds.h, v_video.h, s_sound.h, doomstat.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.523 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.158 IQR)
- **Top Global Matches:** file_cluster_13: 13.523, file_cluster_8: 13.759, file_cluster_11: 13.949
- **Magnitude:** 572.36 | **LOC:** 651 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.0424%), Tech Debt (35.6267%)
**Top Internal Functions/Classes:**
  * `R_InitTextureMapping` (Impact: 28.8)
    * *Intent:* // R_PointToAngleEx merged into R_PointToAngle
  * `R_PointToAngle` (Impact: 19.0)
  * `R_ExecuteSetViewSize` (Impact: 17.1)
  * `R_SetupFrame` (Impact: 16.5)
  * `R_InitLightTables` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 28`, `args: 6`, `func_start: 13`
* *Risk/State:* `state_mutation: 338`, `dead_code: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 74`, `import: 22`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` r_fps.h, g_game.h, r_demo.h, i_main.h, r_plane.h, r_main.h, r_draw.h, w_wad.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_inter.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.412 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.758 IQR)
- **Top Global Matches:** file_cluster_13: 13.412, file_cluster_8: 13.503, file_cluster_11: 13.76
- **Magnitude:** 568.24 | **LOC:** 914 | **CtrlFlow:** 73.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.6242%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` (Impact: 150.8)
  * `P_GivePower` (Impact: 11.3)
  * `P_GiveCard` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 58`, `func_start: 3`
* *Risk/State:* `state_mutation: 324`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 72`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` p_enemy.h, d_deh.h, p_tick.h, sounds.h, s_sound.h, p_inter.h, r_main.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_fps.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.329 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.312 IQR)
- **Top Global Matches:** file_cluster_8: 13.329, file_cluster_13: 13.361, file_cluster_0: 13.63
- **Magnitude:** 558.06 | **LOC:** 451 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9471%), Tech Debt (60.658%)
**Top Internal Functions/Classes:**
  * `R_DoAnInterpolation` (Impact: 31.8)
  * `R_CopyInterpToOld` (Impact: 29.4)
  * `R_CopyBakToInterp` (Impact: 29.4)
  * `R_InterpolationGetData` (Impact: 22.9)
  * `R_SetInterpolation` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 52`, `args: 6`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 313`, `orphaned_logic: 10`
* *Architecture:* `api: 67`, `import: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` r_defs.h, r_fps.h, p_spec.h, r_demo.h, r_state.h, doomstat.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `components/prboom/f_finale.c` (C) | Magnitude: 580.82 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 287, state_mutation: 266, branch: 120, api: 77
- `components/prboom/include/wi_stuff.h` (C) | Magnitude: 21.28 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, api: 5, args: 3, ownership: 3
- `components/prboom/p_plats.c` (C) | Magnitude: 383.46 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 250, indent_spaces: 207, pointers: 173, branch: 69
- `components/prboom/p_user.c` (C) | Magnitude: 331.8 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 235, state_mutation: 192, pointers: 192, branch: 89
- `components/prboom/p_genlin.c` (C) | Magnitude: 902.94 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 551, indent_spaces: 480, branch: 206, pointers: 201

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `components/prboom/v_video.c` (C) | Magnitude: 1469.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 771, indent_spaces: 482, branch: 148, api: 113
- `components/prboom/include/r_demo.h` (C) | Magnitude: 20.16 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: api: 6, structural_boundaries: 3, ownership: 3, pointers: 2
- `components/prboom/gl_main.c` (C) | Magnitude: 2116.94 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1506, state_mutation: 1209, pointers: 517, branch: 314
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

- `components/prboom/include/lprintf.h` -> **Severity: 20.715** (Embedded: 0.2778 * Error Risk: 74.5753%)
- `components/prboom/include/doomtype.h` -> **Severity: 18.351** (Embedded: 0.2983 * Error Risk: 61.5088%)
- `components/prboom/include/doomstat.h` -> **Severity: 17.887** (Embedded: 0.3226 * Error Risk: 55.45%)
- `components/prboom/include/m_fixed.h` -> **Severity: 12.345** (Embedded: 0.1897 * Error Risk: 65.0819%)
- `components/prboom/include/doomdef.h` -> **Severity: 11.953** (Embedded: 0.2102 * Error Risk: 56.8792%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `components/prboom/include/doomtype.h` -> **Severity: 4751.908** (Blast Radius: 70.672 * Doc Risk: 67.2389%)
- `components/prboom/include/d_player.h` -> **Severity: 3949.3** (Blast Radius: 39.493 * Doc Risk: 100.0%)
- `components/prboom/include/m_fixed.h` -> **Severity: 3264.374** (Blast Radius: 33.489 * Doc Risk: 97.476%)
- `components/prboom/include/doomstat.h` -> **Severity: 2512.2** (Blast Radius: 25.122 * Doc Risk: 100.0%)
- `components/prboom/include/p_mobj.h` -> **Severity: 2502.697** (Blast Radius: 25.027 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
