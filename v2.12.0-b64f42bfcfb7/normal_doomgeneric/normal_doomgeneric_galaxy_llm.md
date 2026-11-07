# ARCHITECTURAL_BRIEF: normal_doomgeneric
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ozkl/doomgeneric.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 192 analyzed artifact(s), 41196 LOC.
- **Load-bearing artifact:** `doomgeneric/doomtype.h` -- 55 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `doomgeneric/d_main.c` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `doomgeneric/g_game.c` at magnitude 1851.84 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 211 |
| Analyzed Artifacts (Scanned) | 192 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 41196 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 91.0% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3299 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2098 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4164 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 190 | 41196 | 99.0% |
| PLAINTEXT | 1 | 0 | 0.5% |
| MARKDOWN | 1 | 0 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 192 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 44%, Large Core Modules (3) 17%, Data / Markup / Trivial 10%, Compute Cores Files 9%, Many-Argument Workhorses Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 190 | 99.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
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
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 4663 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1332 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.9 | 27.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.2 | 34.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 28.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.7 | 8.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.9 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 131 | 35 | 2 | `doomgeneric/i_sdlmusic.c` |
| cleanup | 60 | 17 | 0 | `doomgeneric/i_sdlmusic.c` |
| guards | 928 | 75 | 17 | `doomgeneric/i_sdlmusic.c` |
| danger | 205 | 45 | 3 | `doomgeneric/v_video.c` |
| concurrency | 4 | 4 | 0 | `doomgeneric/doomgeneric_linuxvt.c` |
| connectivity | 2204 | 176 | 23 | `doomgeneric/m_controls.h` |
| io | 71 | 14 | 0 | `doomgeneric/i_sdlmusic.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 3 | 0 | `doomgeneric/doomgeneric_linuxvt.c` |
| time | 5 | 4 | 0 | `doomgeneric/doomgeneric_linuxvt.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 55 | 6 | 0 | `doomgeneric/wi_stuff.c` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `doomgeneric/sha1.c` |
| debt | 287 | 61 | 5 | `doomgeneric/statdump.c` |
| mutation | 11982 | 101 | 232 | `doomgeneric/g_game.c` |
| dead_code | 757 | 86 | 10 | `doomgeneric/p_saveg.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 14 | 6 | 0 | `doomgeneric/d_englsh.h` |
| ui | 1 | 1 | 0 | `doomgeneric/doomgeneric_xlib.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doomgeneric/i_sdlmusic.c` (Hits: 15)
- `doomgeneric/i_sdlsound.c` (Hits: 15)
- `doomgeneric/m_misc.c` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomtype.h** (`doomgeneric/doomtype.h`) — 55 inbound connections
2. **i_system.h** (`doomgeneric/i_system.h`) — 45 inbound connections
3. **z_zone.h** (`doomgeneric/z_zone.h`) — 44 inbound connections
4. **doomdef.h** (`doomgeneric/doomdef.h`) — 41 inbound connections
5. **i_system.c** (`doomgeneric/i_system.c`) — 35 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`doomgeneric/d_main.c`) — 42 outbound dependencies
2. **g_game.c** (`doomgeneric/g_game.c`) — 36 outbound dependencies
3. **m_menu.c** (`doomgeneric/m_menu.c`) — 25 outbound dependencies
4. **i_input.c** (`doomgeneric/i_input.c`) — 24 outbound dependencies
5. **st_stuff.c** (`doomgeneric/st_stuff.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `doomgeneric/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `M_Responder` **(Compute Cores)** (@ `doomgeneric/m_menu.c`) -> Impact: **216.2** | LOC: 477
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `P_CrossSpecialLine` **(Many-Argument Workhorses)** (@ `doomgeneric/p_spec.c`) -> Impact: **211.0** | LOC: 460
  * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or by timed thinkers. // // // P_CrossSpecialLine - ...
- `P_TouchSpecialThing` **(Many-Argument Workhorses)** (@ `doomgeneric/p_inter.c`) -> Impact: **180.9** | LOC: 328
  * *Intent:* // // P_TouchSpecialThing //
- `G_BuildTiccmd` **(Many-Argument Workhorses)** (@ `doomgeneric/g_game.c`) -> Impact: **145.4** | LOC: 276
  * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo buffer. // If recording a demo, write it out //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `doomgeneric/r_segs.c`) -> Impact: **136.4** | LOC: 372
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `DG_GetKey` **(Many-Argument Workhorses)** (@ `doomgeneric/doomgeneric_allegro.c`) -> Impact: **123.9** | LOC: 261
- `convertToDoomKey` **(Compute Cores)** (@ `doomgeneric/doomgeneric_linuxvt.c`) -> Impact: **123.6** | LOC: 153
- `ST_Responder` **(Compute Cores)** (@ `doomgeneric/st_stuff.c`) -> Impact: **108.8** | LOC: 224
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `AM_Responder` **(Compute Cores)** (@ `doomgeneric/am_map.c`) -> Impact: **94.8** | LOC: 143
  * *Intent:* // // Handle events (user inputs) in automap mode //

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `doomgeneric` | 190 | 37676.92 | 27.68% | 22.92% |
| `__monolith__` | 2 | 3.14 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `doomgeneric/p_tick.c` -> **99.9998%** Exposure
- `doomgeneric/i_sound.c` -> **99.9857%** Exposure
- `doomgeneric/i_video.c` -> **99.972%** Exposure
- `doomgeneric/m_fixed.c` -> **99.9665%** Exposure
- `doomgeneric/i_timer.c` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doomgeneric/am_map.c` -> **100.0%** Exposure
- `doomgeneric/d_loop.c` -> **100.0%** Exposure
- `doomgeneric/d_main.c` -> **100.0%** Exposure
- `doomgeneric/d_net.c` -> **100.0%** Exposure
- `doomgeneric/doomgeneric_allegro.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `doomgeneric/p_enemy.c` -> **49** Orphaned Functions | **0** Duplicates
- `doomgeneric/p_pspr.c` -> **24** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_sound.c` -> **20** Orphaned Functions | **0** Duplicates
- `doomgeneric/i_video.c` -> **19** Orphaned Functions | **0** Duplicates
- `doomgeneric/v_video.c` -> **17** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1077` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `doomgeneric/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.847)
- **Top Global Matches:** file_cluster_6: 5.847, file_cluster_4: 9.149, file_cluster_8: 16.134
- **Magnitude:** 1851.84 | **LOC:** 2304 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **36**; blast radius 3.281; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.2%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 145.4)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `G_Responder` **(Compute Cores)** (Impact: 65.1)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 55.6)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_DoCompleted` **(I/O & Config Routines)** (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 244`, `args: 54`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 430`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 49`, `import: 36`
* *Defense:* `safety: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.281
  * `Choke Point (Betweenness):` 0.031543 | `Ripple Effect (Closeness):` 0.099283
  * `Imports (Out-Degree: 58):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `doomgeneric/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.346)
- **Top Global Matches:** file_cluster_4: 5.346, file_cluster_6: 8.356, file_cluster_15: 11.846
- **Magnitude:** 1415.82 | **LOC:** 2007 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 2.398; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 288`, `structural_boundaries: 213`, `args: 78`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 281`, `unreferenced_by_name: 49`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.398
  * `Choke Point (Betweenness):` 0.00079 | `Ripple Effect (Closeness):` 0.044308
  * `Imports (Out-Degree: 24):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `doomgeneric/i_scale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.668)
- **Top Global Matches:** file_cluster_12: 6.668, file_cluster_16: 7.61, file_cluster_15: 8.53
- **Magnitude:** 1229.78 | **LOC:** 1453 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 84`, `structural_boundaries: 87`, `args: 35`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 434`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` doomtype.h, i_video.h, m_argv.h, stdio.h, stdlib.h, string.h, z_zone.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.511)
- **Top Global Matches:** file_cluster_15: 6.511, file_cluster_16: 7.706, file_cluster_11: 8.027
- **Magnitude:** 1181.64 | **LOC:** 2126 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 2.38; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 248`, `structural_boundaries: 282`, `args: 176`, `func_start: 56`, `class_start: 11`
* *Risk/State:* `state_mutation: 206`, `dead_code: 6`, `fragile_debt: 7`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 104`, `import: 25`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.38
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.071483
  * `Imports (Out-Degree: 34):` ctype.h, d_main.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `doomgeneric/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.307)
- **Top Global Matches:** file_cluster_6: 7.307, file_cluster_4: 7.771, file_cluster_16: 15.096
- **Magnitude:** 1169.0 | **LOC:** 1830 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 2.38; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(I/O & Config Routines)** (Impact: 52.6)
  * `WI_loadUnloadData` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* // Common load/unload function. Iterates over all the graphics // lumps to be loaded/unloaded into m...
  * `WI_updateDeathmatchStats` **(I/O & Config Routines)** (Impact: 34.0)
  * `WI_updateStats` **(I/O & Config Routines)** (Impact: 33.2)
  * `WI_drawOnLnode` **(Compute Cores)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 122`, `args: 111`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `state_mutation: 244`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `import: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.38
  * `Choke Point (Betweenness):` 0.000182 | `Ripple Effect (Closeness):` 0.071483
  * `Imports (Out-Degree: 21):` deh_main.h, doomstat.h, g_game.h, i_swap.h, i_system.h, m_misc.h, m_random.h, r_local.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `doomgeneric/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.651)
- **Top Global Matches:** file_cluster_4: 6.651, file_cluster_6: 8.171, file_cluster_16: 13.489
- **Magnitude:** 1146.8 | **LOC:** 1356 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 2.497; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 94.8)
    * *Intent:* // // Handle events (user inputs) in automap mode //
  * `AM_clipMline` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algorithm but with a sligh...
  * `AM_drawFline` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* #undef DOOUTCODE // // Classic Bresenham w/ whatever optimizations needed for speed //
  * `AM_drawWalls` **(I/O & Config Routines)** (Impact: 24.4)
    * *Intent:* // // Determines visible lines, draws them. // This is LineDef based, not LineSeg based. //
  * `AM_drawLineCharacter` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 105`, `args: 58`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `state_mutation: 264`, `dead_code: 7`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `import: 17`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.497
  * `Choke Point (Betweenness):` 0.001353 | `Ripple Effect (Closeness):` 0.076589
  * `Imports (Out-Degree: 22):` am_map.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, i_system.h, m_cheat.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `doomgeneric/p_spec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.289)
- **Top Global Matches:** file_cluster_6: 6.289, file_cluster_8: 10.761, file_cluster_4: 13.855
- **Magnitude:** 937.96 | **LOC:** 1490 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **16**; blast radius 4.168; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (35.5%), Connectivity (formerly Api Exposure) (7.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 211.0)
    * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or...
  * `P_SpawnSpecials` **(I/O & Config Routines)** (Impact: 30.8)
    * *Intent:* // Parses command line parameters.
  * `P_PlayerInSpecialSector` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* // // P_PlayerInSpecialSector // Called every tic frame // that the player origin is in a special se...
  * `P_UpdateSpecials` **(I/O & Config Routines)** (Impact: 20.6)
  * `P_FindNextHighestFloor` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* // // P_FindNextHighestFloor // FIND NEXT HIGHEST FLOOR IN SURROUNDING SECTORS // Note: this should ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 473
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 175`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 173`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 25`, `import: 16`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.168
  * `Choke Point (Betweenness):` 0.016847 | `Ripple Effect (Closeness):` 0.075511
  * `Imports (Out-Degree: 33):` deh_main.h, doomdef.h, doomstat.h, g_game.h, i_system.h, m_argv.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `doomgeneric/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.15)
- **Top Global Matches:** file_cluster_3: 9.15, file_cluster_8: 14.866, file_cluster_6: 27.769
- **Magnitude:** 931.36 | **LOC:** 923 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 2.767; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Many-Argument Workhorses)** (Impact: 180.9)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_GiveAmmo` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* // // GET STUFF // // // P_GiveAmmo // Num is the number of clip loads, // not the individual count ...
  * `P_KillMobj` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* // // KillMobj //
  * `P_GiveWeapon` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* // // P_GiveWeapon // The weapon name may have a MF_DROPPED flag ored in. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 134`, `args: 49`, `func_start: 9`
* *Risk/State:* `state_mutation: 156`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.767
  * `Choke Point (Betweenness):` 0.002142 | `Ripple Effect (Closeness):` 0.073442
  * `Imports (Out-Degree: 20):` am_map.h, deh_main.h, deh_misc.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_random.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `doomgeneric/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.457)
- **Top Global Matches:** file_cluster_6: 5.457, file_cluster_8: 12.325, file_cluster_4: 12.411
- **Magnitude:** 908.46 | **LOC:** 1449 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **14**; blast radius 3.341; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 161`, `structural_boundaries: 159`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 220`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 22`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.341
  * `Choke Point (Betweenness):` 0.003797 | `Ripple Effect (Closeness):` 0.077699
  * `Imports (Out-Degree: 25):` deh_misc.h, doomdef.h, doomstat.h, i_system.h, m_argv.h, m_bbox.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `doomgeneric/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.657)
- **Top Global Matches:** file_cluster_16: 6.657, file_cluster_12: 7.342, file_cluster_15: 8.667
- **Magnitude:** 897.0 | **LOC:** 1892 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 2.439; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (98.9%), Complexity Load (formerly Cognitive Load) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_UnArchiveSpecials` **(I/O & Config Routines)** (Impact: 18.9)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_ArchiveSpecials` **(I/O & Config Routines)** (Impact: 17.2)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `saveg_read_player_t` **(I/O & Config Routines)** (Impact: 16.3)
    * *Intent:* // // player_t //
  * `saveg_write_player_t` **(I/O & Config Routines)** (Impact: 16.3)
  * `P_UnArchiveThinkers` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* // // P_UnArchiveThinkers //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 629
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 105`, `args: 53`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 299`, `dead_code: 158`, `unreferenced_by_name: 14`
* *Architecture:* `io: 2`, `api: 15`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.439
  * `Choke Point (Betweenness):` 0.002244 | `Ripple Effect (Closeness):` 0.072449
  * `Imports (Out-Degree: 19):` deh_main.h, doomstat.h, dstrings.h, g_game.h, i_system.h, m_misc.h, p_local.h, p_saveg.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `doomgeneric/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.758)
- **Top Global Matches:** file_cluster_6: 7.758, file_cluster_8: 8.129, file_cluster_4: 16.296
- **Magnitude:** 886.08 | **LOC:** 1050 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **11**; blast radius 3.847; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 166`, `structural_boundaries: 55`, `args: 19`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `fragile_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `api: 20`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.847
  * `Choke Point (Betweenness):` 0.010059 | `Ripple Effect (Closeness):` 0.082481
  * `Imports (Out-Degree: 23):` doomdef.h, doomstat.h, hu_stuff.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `doomgeneric/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.974)
- **Top Global Matches:** file_cluster_6: 8.974, file_cluster_8: 10.573, file_cluster_4: 16.219
- **Magnitude:** 878.48 | **LOC:** 1846 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **42**; blast radius 6.139; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `D_DoomMain` **(I/O & Config Routines)** (Impact: 94.1)
    * *Intent:* #endif // // D_DoomMain //
  * `D_Display` **(Stateful Encapsulated Methods)** (Impact: 52.0)
  * `InitGameVersion` **(I/O & Config Routines)** (Impact: 30.1)
    * *Intent:* // Initialize the game version
  * `D_DoAdvanceDemo` **(I/O & Config Routines)** (Impact: 27.1)
    * *Intent:* // // This cycles through the demo sequences. // FIXME - version dependend demo numbers? //
  * `D_SetGameDescription` **(I/O & Config Routines)** (Impact: 21.9)
    * *Intent:* // Set the gamedescription string
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 162 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 118`, `args: 48`, `func_start: 22`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 182`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 25`, `import: 42`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.139
  * `Choke Point (Betweenness):` 0.049538 | `Ripple Effect (Closeness):` 0.082481
  * `Imports (Out-Degree: 69):` am_map.h, config.h, ctype.h, d_iwad.h, d_main.h, deh_main.h, doomdef.h, doomfeatures.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `doomgeneric/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.825)
- **Top Global Matches:** file_cluster_8: 5.825, file_cluster_6: 12.846, file_cluster_4: 21.588
- **Magnitude:** 866.2 | **LOC:** 983 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 2.948; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 50.6)
  * `R_ProjectSprite` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawPSprite` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // // R_DrawPSprite //
  * `R_InstallSpriteLump` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 45`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 212`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.948
  * `Choke Point (Betweenness):` 0.001528 | `Ripple Effect (Closeness):` 0.082127
  * `Imports (Out-Degree: 14):` deh_main.h, doomdef.h, doomstat.h, i_swap.h, i_system.h, r_local.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `doomgeneric/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.764)
- **Top Global Matches:** file_cluster_12: 6.764, file_cluster_7: 9.218, file_cluster_15: 9.666
- **Magnitude:** 843.24 | **LOC:** 933 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **15**; blast radius 3.598; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.3%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.598
  * `Choke Point (Betweenness):` 0.00329 | `Ripple Effect (Closeness):` 0.111601
  * `Imports (Out-Degree: 17):` config.h, deh_str.h, doomtype.h, i_swap.h, i_system.h, i_video.h, m_bbox.h, m_misc.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `doomgeneric/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.016)
- **Top Global Matches:** file_cluster_6: 7.016, file_cluster_4: 8.033, file_cluster_12: 15.07
- **Magnitude:** 826.94 | **LOC:** 856 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 2.38; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 75`, `structural_boundaries: 26`, `args: 17`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 239`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 14`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.38
  * `Choke Point (Betweenness):` 0.003415 | `Ripple Effect (Closeness):` 0.071483
  * `Imports (Out-Degree: 26):` deh_main.h, doomdef.h, doomstat.h, g_game.h, i_swap.h, i_system.h, m_argv.h, m_bbox.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `doomgeneric/st_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.417)
- **Top Global Matches:** file_cluster_4: 8.417, file_cluster_6: 8.44, file_cluster_16: 14.756
- **Magnitude:** 821.16 | **LOC:** 1417 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 2.619; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ST_Responder` **(Compute Cores)** (Impact: 108.8)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` **(I/O & Config Routines)** (Impact: 42.5)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` **(I/O & Config Routines)** (Impact: 19.2)
  * `ST_updateWidgets` **(I/O & Config Routines)** (Impact: 15.2)
  * `ST_loadUnloadGraphics` **(I/O & Config Routines)** (Impact: 12.5)
    * *Intent:* // Iterates through all graphics to be loaded or unloaded, along with // the variable they use, invo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 168 instances
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 78`, `args: 57`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 192`, `dead_code: 7`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 22`, `import: 24`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.619
  * `Choke Point (Betweenness):` 0.00725 | `Ripple Effect (Closeness):` 0.081231
  * `Imports (Out-Degree: 35):` am_map.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `doomgeneric/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.272)
- **Top Global Matches:** file_cluster_1: 5.272, file_cluster_3: 48.155, file_cluster_8: 69.995
- **Magnitude:** 776.14 | **LOC:** 744 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.599; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 136.4)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 36.1)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 552
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.599
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.059835
  * `Imports (Out-Degree: 11):` doomdef.h, doomstat.h, i_system.h, r_local.h, r_sky.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `doomgeneric/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.678)
- **Top Global Matches:** file_cluster_4: 6.678, file_cluster_9: 8.169, file_cluster_16: 10.693
- **Magnitude:** 753.52 | **LOC:** 1002 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 2.706; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 106`, `structural_boundaries: 102`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 160`, `unreferenced_by_name: 6`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.706
  * `Choke Point (Betweenness):` 0.000206 | `Ripple Effect (Closeness):` 0.068694
  * `Imports (Out-Degree: 7):` doomdef.h, doomstat.h, m_bbox.h, p_local.h, r_state.h, stdlib.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `doomgeneric/i_sdlmusic.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.681)
- **Top Global Matches:** file_cluster_16: 5.681, file_cluster_4: 7.822, file_cluster_15: 8.135
- **Magnitude:** 698.14 | **LOC:** 1317 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 2.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseSubstituteLine` **(Many-Argument Workhorses)** (Impact: 44.1)
    * *Intent:* // Parse a line from substitute music configuration file; returns error // message or NULL for no er...
  * `I_SDL_RegisterSong` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `ParseVorbisComments` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* // Parse a vorbis comments structure, reading from the given file.
  * `ParseFlacFile` **(Stateful Encapsulated Methods)** (Impact: 18.0)
  * `ParseOggFile` **(Stateful Encapsulated Methods)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 136`, `args: 42`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 122`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 15`, `api: 4`, `import: 21`
* *Defense:* `safety: 5`, `immutability_locks: 2`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` SDL.h, SDL_mixer.h, config.h, ctype.h, deh_str.h, doomtype.h, gusconf.h, i_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doomgeneric/r_data.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.551)
- **Top Global Matches:** file_cluster_4: 6.551, file_cluster_12: 9.655, file_cluster_15: 10.73
- **Magnitude:** 656.96 | **LOC:** 913 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **13**; blast radius 3.279; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_InitTextures` **(I/O & Config Routines)** (Impact: 25.8)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 190`, `unreferenced_by_name: 5`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.279
  * `Choke Point (Betweenness):` 0.001673 | `Ripple Effect (Closeness):` 0.10149
  * `Imports (Out-Degree: 16):` deh_main.h, doomdef.h, doomstat.h, i_swap.h, i_system.h, m_misc.h, p_local.h, r_data.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `doomgeneric/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.008)
- **Top Global Matches:** file_cluster_3: 6.008, file_cluster_8: 20.775, file_cluster_6: 33.755
- **Magnitude:** 641.68 | **LOC:** 547 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 3.044; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `T_MovePlane` **(Many-Argument Workhorses)** (Impact: 79.2)
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
* *Structure:* `branch: 79`, `structural_boundaries: 54`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 148`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.044
  * `Choke Point (Betweenness):` 0.000404 | `Ripple Effect (Closeness):` 0.058275
  * `Imports (Out-Degree: 12):` doomdef.h, doomstat.h, p_local.h, r_state.h, s_sound.h, sounds.h, z_zone.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `doomgeneric/r_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.173)
- **Top Global Matches:** file_cluster_4: 6.173, file_cluster_15: 8.517, file_cluster_16: 9.605
- **Magnitude:** 597.32 | **LOC:** 892 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **8**; blast radius 4.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.9%), Complexity Load (formerly Cognitive Load) (63.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_PointToAngle` **(Many-Argument Workhorses)** (Impact: 33.6)
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
* *Structure:* `branch: 76`, `structural_boundaries: 59`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 143`, `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.393
  * `Choke Point (Betweenness):` 0.016952 | `Ripple Effect (Closeness):` 0.125029
  * `Imports (Out-Degree: 15):` d_loop.h, doomdef.h, m_bbox.h, m_menu.h, math.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `doomgeneric/r_draw.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.104)
- **Top Global Matches:** file_cluster_9: 6.104, file_cluster_15: 8.726, file_cluster_16: 9.439
- **Magnitude:** 549.48 | **LOC:** 976 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 2.853; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 77`, `structural_boundaries: 32`, `args: 24`, `func_start: 13`
* *Risk/State:* `state_mutation: 136`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.853
  * `Choke Point (Betweenness):` 0.001281 | `Ripple Effect (Closeness):` 0.102618
  * `Imports (Out-Degree: 12):` deh_main.h, doomdef.h, doomstat.h, i_system.h, r_local.h, v_video.h, w_wad.h, z_zone.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `doomgeneric/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.928)
- **Top Global Matches:** file_cluster_15: 5.928, file_cluster_4: 7.295, file_cluster_16: 7.513
- **Magnitude:** 539.14 | **LOC:** 889 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 2.83; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.0%), Debt Markers (formerly Tech Debt) (87.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CheckAmmo` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* #include "p_pspr.h" #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM...
  * `A_Saw` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* // // A_Saw //
  * `A_ReFire` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* // // A_ReFire // The player can re-fire the weapon // without lowering it entirely. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 49`, `args: 31`, `func_start: 31`
* *Risk/State:* `state_mutation: 102`, `unreferenced_by_name: 24`
* *Architecture:* `api: 30`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.83
  * `Choke Point (Betweenness):` 0.001467 | `Ripple Effect (Closeness):` 0.05957
  * `Imports (Out-Degree: 17):` d_event.h, deh_misc.h, doomdef.h, doomstat.h, m_random.h, p_local.h, p_pspr.h, s_sound.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `doomgeneric/f_finale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.895)
- **Top Global Matches:** file_cluster_4: 5.895, file_cluster_9: 10.336, file_cluster_6: 10.967
- **Magnitude:** 530.06 | **LOC:** 719 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 2.38; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (71.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Structure:* `branch: 115`, `structural_boundaries: 92`, `args: 26`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 123`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.38
  * `Choke Point (Betweenness):` 0.000146 | `Ripple Effect (Closeness):` 0.074046
  * `Imports (Out-Degree: 16):` ctype.h, d_main.h, deh_main.h, doomstat.h, dstrings.h, hu_stuff.h, i_swap.h, i_system.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `doomgeneric/z_zone.c` (C) | Magnitude: 334.56 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 171, pointers: 158, state_mutation: 81, branch: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `doomgeneric/f_wipe.h` (C) | Magnitude: 18.58 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, args: 3, api: 3, macros: 2
- `doomgeneric/doomstat.h` (C) | Magnitude: 81.54 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 65, globals: 65, import: 5, macros: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `doomgeneric/st_stuff.c` (C) | Magnitude: 821.16 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 294, pointers: 221, state_mutation: 192, indent_tabs: 154

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `doomgeneric/d_main.c` -> **Severity: 4.954** (Bridge: 0.0495 * Flux: 100.0%)
- `doomgeneric/g_game.c` -> **Severity: 3.154** (Bridge: 0.0315 * Flux: 100.0%)
- `doomgeneric/r_main.c` -> **Severity: 1.695** (Bridge: 0.017 * Flux: 100.0%)
- `doomgeneric/p_spec.c` -> **Severity: 1.685** (Bridge: 0.0168 * Flux: 100.0%)
- `doomgeneric/w_wad.c` -> **Severity: 1.154** (Bridge: 0.0115 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `doomgeneric/doomtype.h` -> **Severity: 22.589** (Embedded: 0.4454 * Error Risk: 50.7142%)
- `doomgeneric/z_zone.c` -> **Severity: 18.979** (Embedded: 0.225 * Error Risk: 84.3508%)
- `doomgeneric/i_system.c` -> **Severity: 18.528** (Embedded: 0.2469 * Error Risk: 75.0413%)
- `doomgeneric/m_misc.c` -> **Severity: 16.02** (Embedded: 0.2306 * Error Risk: 69.4774%)
- `doomgeneric/m_argv.c` -> **Severity: 15.988** (Embedded: 0.2007 * Error Risk: 79.6523%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `doomgeneric/i_system.c` -> **Severity: 1091.0** (Blast Radius: 10.91 * Doc Risk: 100.0%)
- `doomgeneric/z_zone.c` -> **Severity: 873.9** (Blast Radius: 8.739 * Doc Risk: 100.0%)
- `doomgeneric/m_misc.c` -> **Severity: 810.3** (Blast Radius: 8.103 * Doc Risk: 100.0%)
- `doomgeneric/m_argv.c` -> **Severity: 718.5** (Blast Radius: 7.185 * Doc Risk: 100.0%)
- `doomgeneric/i_swap.h` -> **Severity: 671.1** (Blast Radius: 6.711 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 219 literal sites + 2 sites through wrappers = 221
- **`memory_alloc`:** 58 literal sites + 13 sites through wrappers = 71

- `I_AtExit` (function, memory_alloc, primitive): 9 call sites in 5 files -- `doomgeneric/i_system.c`
- `PrintBanner` (function, debug_prints, primitive): 2 call sites in 1 files -- `doomgeneric/statdump.c`
- `AddSubstituteMusic` (function, memory_alloc, primitive): 1 call sites in 1 files -- `doomgeneric/i_sdlmusic.c`
- `FreeDMXConfig` (function, memory_alloc, primitive): 1 call sites in 1 files -- `doomgeneric/gusconf.c`
- `GetDefaultConfigDir` (function, memory_alloc, primitive): 1 call sites in 1 files -- `doomgeneric/m_config.c`
- `RemoveTimidityConfig` (function, memory_alloc, primitive): 1 call sites in 1 files -- `doomgeneric/i_sdlmusic.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3207 call pairs -- scoped 26.2%, unique 41.1%, ambiguous 0.2%, external 32.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 3207 | 26.2% | 41.1% | 0.2% | 32.5% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
