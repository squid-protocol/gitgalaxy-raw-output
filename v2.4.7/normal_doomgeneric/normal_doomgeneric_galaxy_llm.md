# ARCHITECTURAL_BRIEF: normal_doomgeneric
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/DOOM_systems/normal_doomgeneric` |
| **Timestamp** | `2026-08-07T03:29:33.720853+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `3b1d53020373b502035d7d48dede645a7c429feb` |
| **Git Remote** | `https://github.com/ozkl/doomgeneric.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 180 malicious artifacts.

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
| Modularity | 0.3674 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 97.7 | 33.7 | 6.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 46.0 | 60.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 24.1 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.6 | 9.8 | 10.4 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.5 | 32.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 95.6 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.5 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 71.8 | 93.4 | 100.0 |
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

- `DG_DrawFrame` (@ `doomgeneric/doomgeneric_allegro.c`) -> Impact: **240.3** | LOC: 337
- `DG_GetKey` (@ `doomgeneric/doomgeneric_allegro.c`) -> Impact: **224.4** | LOC: 261
- `P_UseSpecialLine` (@ `doomgeneric/p_switch.c`) -> Impact: **194.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `convertToDoomKey` (@ `doomgeneric/doomgeneric_linuxvt.c`) -> Impact: **184.2** | LOC: 324
  * *Intent:* #undef KEY_ENTER #undef KEY_BACKSPACE #undef KEY_MINUS #undef KEY_F1 #undef KEY_F2 #undef KEY_F3 #undef KEY_F4 #undef KEY_F5 #undef KEY_F6 #undef KEY_...
- `M_Responder` (@ `doomgeneric/m_menu.c`) -> Impact: **164.8** | LOC: 476
- `A_Fire` (@ `doomgeneric/p_enemy.c`) -> Impact: **138.9** | LOC: 679
  * *Intent:* // // A_Fire // Keep fire in front of player unless out of sight
- `F_CastTicker` (@ `doomgeneric/f_finale.c`) -> Impact: **119.4** | LOC: 101
  * *Intent:* // // F_CastTicker //
- `convertToDoomKey` (@ `doomgeneric/doomgeneric_emscripten.c`) -> Impact: **108.0** | LOC: 81
- `convertToDoomKey` (@ `doomgeneric/doomgeneric_sdl.c`) -> Impact: **108.0** | LOC: 80
- `convert_to_doom_keyx` (@ `doomgeneric/doomgeneric_sosox.c`) -> Impact: **106.0** | LOC: 42

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `doomgeneric` | 180 | 32892.04 | 33.72% | 28.69% |
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
- `doomgeneric/p_enemy.c` -> **47** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `doomgeneric/p_pspr.c` -> **20** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_video.c` -> **16** Orphaned Functions | **0** Duplicates
- `doomgeneric/p_saveg.c` -> **14** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1018` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `doomgeneric/doomgeneric_linuxvt.c` (C) -> Cumulative Risk: **699.62**
- **Archetype:** `file_cluster_8` (Distance: 13.01 IQR)
- **Magnitude:** 488.34 | **LOC:** 529 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.3438%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 184.2), `isKeyboard` (Impact: 15.8), `checkInputDevs` (Impact: 11.1)

### 2. `doomgeneric/doomgeneric_allegro.c` (C) -> Cumulative Risk: **691.24**
- **Archetype:** `file_cluster_13` (Distance: 13.076 IQR)
- **Magnitude:** 768.18 | **LOC:** 454 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9865%), Cognitive Load (97.7029%)
- **Heaviest Functions:** `DG_DrawFrame` (Impact: 240.3), `DG_GetKey` (Impact: 224.4), `main` (Impact: 4.0)

### 3. `doomgeneric/doomgeneric_sosox.c` (C) -> Cumulative Risk: **688.31**
- **Archetype:** `file_cluster_13` (Distance: 12.821 IQR)
- **Magnitude:** 339.44 | **LOC:** 248 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (97.4973%)
- **Heaviest Functions:** `convert_to_doom_keyx` (Impact: 106.0), `DG_DrawFrame` (Impact: 21.8), `DG_GetKey` (Impact: 6.2)

### 4. `doomgeneric/i_video.c` (C) -> Cumulative Risk: **686.54**
- **Archetype:** `file_cluster_13` (Distance: 13.353 IQR)
- **Magnitude:** 374.1 | **LOC:** 496 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9804%), Documentation (99.0837%)
- **Heaviest Functions:** `I_InitGraphics` (Impact: 23.7), `I_FinishUpdate` (Impact: 16.4), `I_GetPaletteIndex` (Impact: 11.8)

### 5. `doomgeneric/doomgeneric_sdl.c` (C) -> Cumulative Risk: **667.5**
- **Archetype:** `file_cluster_13` (Distance: 12.276 IQR)
- **Magnitude:** 287.46 | **LOC:** 211 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9584%), Cognitive Load (96.4783%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 108.0), `handleKeyInput` (Impact: 7.0), `DG_GetKey` (Impact: 6.1)

### 6. `doomgeneric/p_pspr.c` (C) -> Cumulative Risk: **661.91**
- **Archetype:** `file_cluster_8` (Distance: 12.924 IQR)
- **Magnitude:** 510.12 | **LOC:** 889 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.005%), Safety Score (90.4255%)
- **Heaviest Functions:** `A_Lower` (Impact: 46.9), `P_CheckAmmo` (Impact: 38.0), `A_WeaponReady` (Impact: 14.7)

### 7. `doomgeneric/p_enemy.c` (C) -> Cumulative Risk: **661.65**
- **Archetype:** `file_cluster_8` (Distance: 13.607 IQR)
- **Magnitude:** 1552.3 | **LOC:** 2007 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.5765%), Cognitive Load (92.821%)
- **Heaviest Functions:** `A_Fire` (Impact: 138.9), `P_NewChaseDir` (Impact: 40.4), `A_Chase` (Impact: 39.2)

### 8. `doomgeneric/doomgeneric_emscripten.c` (C) -> Cumulative Risk: **661.6**
- **Archetype:** `file_cluster_13` (Distance: 12.096 IQR)
- **Magnitude:** 280.98 | **LOC:** 220 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9452%), Cognitive Load (96.026%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 108.0), `handleKeyInput` (Impact: 7.1), `DG_GetKey` (Impact: 6.2)

### 9. `doomgeneric/doomgeneric_win.c` (C) -> Cumulative Risk: **661.02**
- **Archetype:** `file_cluster_8` (Distance: 12.254 IQR)
- **Magnitude:** 230.42 | **LOC:** 210 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.2472%), Safety Score (93.3314%)
- **Heaviest Functions:** `convertToDoomKey` (Impact: 45.9), `wndProc` (Impact: 12.1), `DG_Init` (Impact: 6.5)

### 10. `doomgeneric/r_draw.c` (C) -> Cumulative Risk: **660.02**
- **Archetype:** `file_cluster_13` (Distance: 14.217 IQR)
- **Magnitude:** 903.48 | **LOC:** 976 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.6262%), Safety Score (98.8755%)
- **Heaviest Functions:** `R_FillBackScreen` (Impact: 27.6), `R_DrawFuzzColumnLow` (Impact: 20.6), `R_DrawFuzzColumn` (Impact: 20.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `doomgeneric/p_enemy.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.607 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.403 IQR)
- **Top Global Matches:** file_cluster_8: 13.607, file_cluster_13: 13.734, file_cluster_0: 13.849
- **Magnitude:** 1552.3 | **LOC:** 2007 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 302`, `structural_boundaries: 182`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 684`, `dead_code: 6`, `orphaned_logic: 47`
* *Architecture:* `api: 263`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` stdio.h, r_state.h, m_random.h, stdlib.h, i_system.h, sounds.h, g_game.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/i_scale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.959 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.715 IQR)
- **Top Global Matches:** file_cluster_8: 13.959, file_cluster_13: 14.183, file_cluster_7: 14.329
- **Magnitude:** 1454.88 | **LOC:** 1453 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 86`, `structural_boundaries: 87`, `args: 15`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1050`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 121`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` stdio.h, m_argv.h, stdlib.h, z_zone.h, string.h, doomtype.h, i_video.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/wi_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.221 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_8: 13.221, file_cluster_13: 13.441, file_cluster_7: 13.584
- **Magnitude:** 1435.4 | **LOC:** 1830 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.675%), Tech Debt (25.3459%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` (Impact: 78.3)
  * `WI_updateDeathmatchStats` (Impact: 46.0)
  * `WI_updateStats` (Impact: 44.8)
  * `WI_loadUnloadData` (Impact: 30.4)
  * `WI_updateAnimatedBack` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 106`, `args: 35`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 736`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 159`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` v_video.h, stdio.h, m_random.h, i_system.h, sounds.h, z_zone.h, m_misc.h, wi_stuff.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/m_menu.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.204 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.67 IQR)
- **Top Global Matches:** file_cluster_13: 13.204, file_cluster_8: 13.258, file_cluster_11: 13.533
- **Magnitude:** 1065.8 | **LOC:** 2126 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3528%), Tech Debt (65.7778%)
**Top Internal Functions/Classes:**
  * `M_Responder` (Impact: 164.8)
  * `M_Drawer` (Impact: 25.0)
  * `M_WriteText` (Impact: 24.1)
  * `M_Init` (Impact: 21.5)
  * `M_SizeDisplay` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 123`, `args: 25`, `func_start: 28`
* *Risk/State:* `state_mutation: 526`, `dead_code: 2`, `fragile_debt: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 158`, `import: 25`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ctype.h, sounds.h, m_misc.h, doomdef.h, r_local.h, dstrings.h, p_saveg.h, deh_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_saveg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_9` (Drift: 21.332 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.513 IQR)
- **Top Global Matches:** file_cluster_9: 21.332, file_cluster_0: 21.338, file_cluster_11: 21.351
- **Magnitude:** 1049.7 | **LOC:** 1892 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 109`, `structural_boundaries: 83`, `args: 23`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 642`, `dead_code: 128`, `orphaned_logic: 14`
* *Architecture:* `io: 2`, `api: 92`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` stdio.h, r_state.h, stdlib.h, i_system.h, p_local.h, z_zone.h, m_misc.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_things.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.501 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.306 IQR)
- **Top Global Matches:** file_cluster_13: 14.501, file_cluster_8: 14.573, file_cluster_11: 14.657
- **Magnitude:** 996.3 | **LOC:** 983 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 133`, `structural_boundaries: 39`, `args: 8`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 625`, `dead_code: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 122`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` stdio.h, stdlib.h, i_system.h, z_zone.h, doomstat.h, doomdef.h, w_wad.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/st_stuff.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.817 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.626 IQR)
- **Top Global Matches:** file_cluster_13: 13.817, file_cluster_8: 13.886, file_cluster_0: 14.119
- **Magnitude:** 933.06 | **LOC:** 1417 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 152`, `structural_boundaries: 76`, `args: 20`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 572`, `dead_code: 6`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 88`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` m_cheat.h, m_random.h, sounds.h, am_map.h, st_lib.h, m_misc.h, doomdef.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/v_video.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` deh_str.h, v_video.h, stdio.h, i_video.h, i_system.h, z_zone.h, m_bbox.h, m_misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_draw.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` v_video.h, i_system.h, z_zone.h, doomstat.h, doomdef.h, w_wad.h, r_local.h, deh_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/f_finale.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.253 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.631 IQR)
- **Top Global Matches:** file_cluster_13: 13.253, file_cluster_8: 13.258, file_cluster_11: 13.594
- **Magnitude:** 821.36 | **LOC:** 719 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 149`, `structural_boundaries: 59`, `args: 14`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 394`, `fragile_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ctype.h, v_video.h, stdio.h, r_state.h, i_system.h, sounds.h, hu_stuff.h, z_zone.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.62 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.345 IQR)
- **Top Global Matches:** file_cluster_8: 13.62, file_cluster_13: 13.657, file_cluster_0: 13.835
- **Magnitude:** 776.72 | **LOC:** 892 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 82`, `structural_boundaries: 60`, `args: 8`, `func_start: 17`
* *Risk/State:* `state_mutation: 456`, `dead_code: 3`, `orphaned_logic: 9`
* *Architecture:* `api: 143`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` r_sky.h, stdlib.h, d_loop.h, doomdef.h, r_local.h, m_menu.h, math.h, m_bbox.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/doomgeneric_allegro.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.076 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.754 IQR)
- **Top Global Matches:** file_cluster_13: 13.076, file_cluster_8: 13.255, file_cluster_11: 13.427
- **Magnitude:** 768.18 | **LOC:** 454 | **CtrlFlow:** 90.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.7029%), Tech Debt (96.9702%)
**Top Internal Functions/Classes:**
  * `DG_DrawFrame` (Impact: 240.3)
  * `DG_GetKey` (Impact: 224.4)
  * `main` (Impact: 4.0)
  * `DG_SetWindowTitle` (Impact: 2.2)
  * `back_to_text_mode` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 14`, `args: 4`, `func_start: 7`
* *Risk/State:* `state_mutation: 217`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 71`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdint.h, stdio.h, m_argv.h, i_system.h, unistd.h, stdbool.h, doomgeneric.h, doomkeys.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_doors.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` r_state.h, sounds.h, deh_main.h, z_zone.h, doomstat.h, doomdef.h, s_sound.h, dstrings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_floor.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.362 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.485 IQR)
- **Top Global Matches:** file_cluster_13: 14.362, file_cluster_8: 14.432, file_cluster_11: 14.51
- **Magnitude:** 664.98 | **LOC:** 547 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 111`, `structural_boundaries: 26`, `func_start: 4`
* *Risk/State:* `state_mutation: 454`, `dead_code: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 63`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` r_state.h, sounds.h, z_zone.h, doomstat.h, doomdef.h, s_sound.h, p_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/d_main.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.668 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 2.996 IQR)
- **Top Global Matches:** file_cluster_13: 12.668, file_cluster_8: 12.934, file_cluster_11: 13.172
- **Magnitude:** 647.14 | **LOC:** 1846 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.5955%), Tech Debt (19.1869%)
**Top Internal Functions/Classes:**
  * `PrintDehackedBanners` (Impact: 99.7)
  * `D_Display` (Impact: 92.9)
  * `D_SetGameDescription` (Impact: 29.8)
  * `D_DoomMain` (Impact: 27.1)
  * `D_ProcessEvents` (Impact: 9.4)
    * *Intent:* // // D_ProcessEvents // Send all the events of the given timestamp down the responder chain //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 50`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 297`, `dead_code: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 70`, `import: 42`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` ctype.h, sounds.h, am_map.h, m_misc.h, p_setup.h, string.h, doomdef.h, r_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_data.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.858 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_0: 14.375, file_cluster_8: 14.376
- **Magnitude:** 623.7 | **LOC:** 913 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` stdio.h, r_sky.h, i_system.h, p_local.h, z_zone.h, m_misc.h, r_data.h, doomstat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_map.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.393 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_13: 13.393, file_cluster_8: 13.462, file_cluster_11: 13.711
- **Magnitude:** 616.1 | **LOC:** 1449 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6916%), Tech Debt (48.7248%)
**Top Internal Functions/Classes:**
  * `PTR_SlideTraverse` (Impact: 28.9)
  * `SpechitOverrun` (Impact: 18.9)
  * `P_CheckPosition` (Impact: 11.4)
  * `P_TryMove` (Impact: 10.7)
  * `PIT_RadiusAttack` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 94`, `func_start: 13`
* *Risk/State:* `state_mutation: 356`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 127`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` stdio.h, r_state.h, m_random.h, stdlib.h, i_system.h, m_argv.h, deh_misc.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_maputl.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.645 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.645, file_cluster_13: 13.806, file_cluster_7: 14.052
- **Magnitude:** 519.02 | **LOC:** 1002 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 74`, `structural_boundaries: 44`, `func_start: 9`
* *Risk/State:* `state_mutation: 352`, `orphaned_logic: 4`
* *Architecture:* `api: 88`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` r_state.h, stdlib.h, doomstat.h, doomdef.h, p_local.h, m_bbox.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_pspr.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.924 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.415 IQR)
- **Top Global Matches:** file_cluster_8: 12.924, file_cluster_13: 13.062, file_cluster_7: 13.342
- **Magnitude:** 510.12 | **LOC:** 889 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 87`, `structural_boundaries: 39`, `func_start: 27`
* *Risk/State:* `state_mutation: 241`, `dead_code: 1`, `orphaned_logic: 20`
* *Architecture:* `api: 83`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` m_random.h, sounds.h, d_event.h, deh_misc.h, doomstat.h, doomdef.h, s_sound.h, p_local.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/doomgeneric_linuxvt.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.01 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.448 IQR)
- **Top Global Matches:** file_cluster_8: 13.01, file_cluster_13: 13.042, file_cluster_0: 13.262
- **Magnitude:** 488.34 | **LOC:** 529 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.7016%), Tech Debt (98.3438%)
**Top Internal Functions/Classes:**
  * `convertToDoomKey` (Impact: 184.2)
    * *Intent:* #undef KEY_ENTER #undef KEY_BACKSPACE #undef KEY_MINUS #undef KEY_F1 #undef KEY_F2 #undef KEY_F3 #un...
  * `isKeyboard` (Impact: 15.8)
  * `checkInputDevs` (Impact: 11.1)
  * `DG_Init` (Impact: 10.8)
  * `checkKeys` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 31`, `args: 5`, `func_start: 11`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 186`, `fragile_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 12`, `api: 51`, `import: 4`
* *Defense:* `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` fcntl.h, stdio.h, m_argv.h, i_system.h, unistd.h, time.h, string.h, dirent.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/p_mobj.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.796 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_13: 13.796, file_cluster_8: 13.9, file_cluster_11: 14.092
- **Magnitude:** 488.32 | **LOC:** 1050 | **CtrlFlow:** 80.2% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 97`, `structural_boundaries: 24`, `args: 1`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 293`, `dead_code: 2`, `fragile_debt: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 57`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` stdio.h, m_random.h, i_system.h, sounds.h, hu_stuff.h, z_zone.h, st_stuff.h, doomdef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_segs.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.864 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.838 IQR)
- **Top Global Matches:** file_cluster_13: 13.864, file_cluster_8: 13.928, file_cluster_0: 14.119
- **Magnitude:** 481.82 | **LOC:** 744 | **CtrlFlow:** 91.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4985%), Tech Debt (15.6698%)
**Top Internal Functions/Classes:**
  * `R_RenderSegLoop` (Impact: 56.6)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
  * `R_StoreWallRange` (Impact: 37.7)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` (Impact: 21.4)
    * *Intent:* // // R_RenderMaskedSegRange //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 6`, `args: 2`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 299`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 61`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` stdio.h, r_sky.h, stdlib.h, i_system.h, doomstat.h, doomdef.h, r_local.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/s_sound.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.702 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.925 IQR)
- **Top Global Matches:** file_cluster_8: 12.702, file_cluster_13: 12.703, file_cluster_7: 13.125
- **Magnitude:** 449.22 | **LOC:** 671 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 86`, `structural_boundaries: 38`, `args: 13`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 220`, `dead_code: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` deh_str.h, stdio.h, i_sound.h, m_random.h, stdlib.h, i_system.h, sounds.h, doomfeatures.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/mus2mid.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.706 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.004 IQR)
- **Top Global Matches:** file_cluster_8: 11.706, file_cluster_13: 11.976, file_cluster_7: 12.157
- **Magnitude:** 447.9 | **LOC:** 738 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.6471%), Tech Debt (10.0302%)
**Top Internal Functions/Classes:**
  * `mus2mid` (Impact: 69.5)
  * `WriteTime` (Impact: 12.0)
    * *Intent:* // Write timestamp to a MIDI file.
  * `WriteChangeController_Valued` (Impact: 8.3)
    * *Intent:* // Write a valued controller change event
  * `ReadMusHeader` (Impact: 8.1)
    * *Intent:* // Find the MIDI channel to use for this MUS channel. // MUS channel 15 is the percusssion channel.
  * `AllocateMIDIChannel` (Impact: 7.7)
    * *Intent:* // Allocate a free MIDI channel.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 118`, `args: 3`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 185`, `orphaned_logic: 1`
* *Architecture:* `api: 110`, `import: 7`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` stdio.h, z_zone.h, m_misc.h, memio.h, mus2mid.h, doomtype.h, i_swap.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_bsp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.138 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.931 IQR)
- **Top Global Matches:** file_cluster_13: 13.138, file_cluster_8: 13.142, file_cluster_11: 13.409
- **Magnitude:** 434.98 | **LOC:** 574 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
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
* *Structure:* `branch: 63`, `structural_boundaries: 39`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 238`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 71`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` r_state.h, r_plane.h, i_system.h, r_things.h, doomstat.h, doomdef.h, r_main.h, m_bbox.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `doomgeneric/r_bsp.c` (C) | Magnitude: 434.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 238, indent_spaces: 174, pointers: 74, indent_tabs: 72
- `doomgeneric/f_finale.c` (C) | Magnitude: 821.36 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 394, indent_spaces: 275, branch: 149, api: 115
- `doomgeneric/doomgeneric_emscripten.c` (C) | Magnitude: 280.98 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 98, branch: 59, api: 43
- `doomgeneric/doomgeneric_sdl.c` (C) | Magnitude: 287.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 133, state_mutation: 104, branch: 60, api: 42
- `doomgeneric/r_draw.c` (C) | Magnitude: 903.48 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 567, indent_spaces: 283, indent_tabs: 139, api: 123

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `doomgeneric/s_sound.c` (C) | Magnitude: 449.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 347, state_mutation: 220, branch: 86, pointers: 84
- `doomgeneric/v_video.c` (C) | Magnitude: 915.06 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 545, indent_spaces: 430, pointers: 173, api: 104
- `doomgeneric/f_wipe.c` (C) | Magnitude: 327.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 180, indent_spaces: 92, api: 57, indent_tabs: 45
- `doomgeneric/doomdef.c` (C) | Magnitude: 10.52 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 1
- `doomgeneric/doomgeneric_linuxvt.c` (C) | Magnitude: 488.34 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 225, state_mutation: 186, branch: 84, api: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `doomgeneric/p_saveg.c` (C) | Magnitude: 1049.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 642, indent_spaces: 602, pointers: 486, dead_code: 128
- `doomgeneric/i_system.h` (C) | Magnitude: 29.38 | Delta: **0.163 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, api: 14, args: 12, pointers: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `doomgeneric/doomgeneric_linuxvt.c` -> **techflashYT** (100.0% isolated ownership) | Magnitude: 488.34
- `doomgeneric/i_system.c` -> **ozkl** (100.0% isolated ownership) | Magnitude: 373.34
- `doomgeneric/doomgeneric_sosox.c` -> **ozkl** (100.0% isolated ownership) | Magnitude: 339.44

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

- `doomgeneric/z_zone.h` -> **Severity: 14.22** (Embedded: 0.232 * Error Risk: 61.2821%)
- `doomgeneric/d_event.h` -> **Severity: 13.895** (Embedded: 0.1678 * Error Risk: 82.7987%)
- `doomgeneric/doomdef.h` -> **Severity: 12.335** (Embedded: 0.2112 * Error Risk: 58.4099%)
- `doomgeneric/d_mode.h` -> **Severity: 11.24** (Embedded: 0.1915 * Error Risk: 58.6996%)
- `doomgeneric/p_mobj.h` -> **Severity: 7.944** (Embedded: 0.1107 * Error Risk: 71.7669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `doomgeneric/doomtype.h` -> **Severity: 2487.979** (Blast Radius: 166.974 * Doc Risk: 14.9004%)
- `doomgeneric/net_defs.h` -> **Severity: 2314.4** (Blast Radius: 23.144 * Doc Risk: 100.0%)
- `doomgeneric/d_ticcmd.h` -> **Severity: 1899.266** (Blast Radius: 18.995 * Doc Risk: 99.9877%)
- `doomgeneric/d_mode.h` -> **Severity: 1894.796** (Blast Radius: 19.713 * Doc Risk: 96.1191%)
- `doomgeneric/z_zone.h` -> **Severity: 1462.635** (Blast Radius: 14.658 * Doc Risk: 99.7841%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
