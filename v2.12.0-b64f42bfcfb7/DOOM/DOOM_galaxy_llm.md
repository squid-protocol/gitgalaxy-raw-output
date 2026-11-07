# ARCHITECTURAL_BRIEF: DOOM
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/id-Software/DOOM.git` |
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
- **Scope:** 154 analyzed artifact(s), 33099 LOC.
- **Load-bearing artifact:** `linuxdoom-1.10/doomdef.h` -- 51 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `linuxdoom-1.10/d_main.c` -- pulls in 30 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `linuxdoom-1.10/g_game.c` at magnitude 1515.0 (structural weight, not risk).
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
| Total Artifacts | 165 |
| Analyzed Artifacts (Scanned) | 154 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 33099 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.315 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.124 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 30.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7816 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 144 | 33001 | 93.5% |
| PLAINTEXT | 6 | 0 | 3.9% |
| MARKDOWN | 2 | 0 | 1.3% |
| MAKEFILE | 2 | 98 | 1.3% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 152 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 48%, Large Core Modules (3) 12%, Compute Cores Files 12%, Data / Markup / Trivial 8%, Large Core Modules 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 146 | 94.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 5.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 222 LOC)
- `.b`: 1x Excluded (Unsupported Extension: '.b')
- `.book`: 1x Excluded (Unsupported Extension: '.book')
- `.gl`: 1x Excluded (Unsupported Extension: '.gl')
- `.sound`: 1x Excluded (Unsupported Extension: '.sound')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 4671 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1341 LOC)
- `.sndserv`: 1x Excluded (Unsupported Extension: '.sndserv')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.4 | 27.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.6 | 38.4 | 50.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 27.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.0 | 10.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.0 | 11.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.7 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 132 | 29 | 2 | `linuxdoom-1.10/m_misc.c` |
| cleanup | 21 | 12 | 0 | `linuxdoom-1.10/m_misc.c` |
| guards | 383 | 68 | 4 | `linuxdoom-1.10/am_map.c` |
| danger | 264 | 43 | 6 | `linuxdoom-1.10/d_main.c` |
| concurrency | 2 | 1 | 0 | `linuxdoom-1.10/i_system.c` |
| connectivity | 1793 | 133 | 26 | `linuxdoom-1.10/m_menu.c` |
| io | 58 | 15 | 0 | `linuxdoom-1.10/m_misc.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 3 | 0 | `linuxdoom-1.10/i_video.c` |
| time | 2 | 2 | 0 | `linuxdoom-1.10/i_system.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 3 | 3 | 0 | `linuxdoom-1.10/i_sound.c` |
| tests | 0 | 0 | 0 | - |
| docs | 1 | 1 | 0 | `linuxdoom-1.10/i_sound.c` |
| debt | 242 | 43 | 5 | `linuxdoom-1.10/d_main.c` |
| mutation | 9984 | 81 | 254 | `linuxdoom-1.10/g_game.c` |
| dead_code | 465 | 63 | 9 | `linuxdoom-1.10/p_enemy.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 31 | 8 | 0 | `linuxdoom-1.10/i_video.c` |
| ui | 1 | 1 | 0 | `linuxdoom-1.10/i_video.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `linuxdoom-1.10/m_misc.c` (Hits: 9)
- `linuxdoom-1.10/w_wad.c` (Hits: 9)
- `sndserv/soundsrv.c` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomdef.h** (`linuxdoom-1.10/doomdef.h`) — 51 inbound connections
2. **doomstat.h** (`linuxdoom-1.10/doomstat.h`) — 36 inbound connections
3. **i_system.h** (`linuxdoom-1.10/i_system.h`) — 35 inbound connections
4. **z_zone.h** (`linuxdoom-1.10/z_zone.h`) — 29 inbound connections
5. **p_local.h** (`linuxdoom-1.10/p_local.h`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`linuxdoom-1.10/d_main.c`) — 30 outbound dependencies
2. **g_game.c** (`linuxdoom-1.10/g_game.c`) — 28 outbound dependencies
3. **m_menu.c** (`linuxdoom-1.10/m_menu.c`) — 23 outbound dependencies
4. **i_video.c** (`linuxdoom-1.10/i_video.c`) — 21 outbound dependencies
5. **i_sound.c** (`linuxdoom-1.10/i_sound.c`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `P_CrossSpecialLine` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_spec.c`) -> Impact: **211.0** | LOC: 460
  * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or by timed thinkers. // // // P_CrossSpecialLine - ...
- `P_TouchSpecialThing` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_inter.c`) -> Impact: **180.7** | LOC: 324
  * *Intent:* // // P_TouchSpecialThing //
- `M_Responder` **(Compute Cores)** (@ `linuxdoom-1.10/m_menu.c`) -> Impact: **164.1** | LOC: 368
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/r_segs.c`) -> Impact: **136.4** | LOC: 372
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `ST_Responder` **(Compute Cores)** (@ `linuxdoom-1.10/st_stuff.c`) -> Impact: **99.5** | LOC: 209
  * *Intent:* // Respond to keyboard input events, // intercept cheats.
- `G_BuildTiccmd` **(Compute Cores)** (@ `linuxdoom-1.10/g_game.c`) -> Impact: **94.9** | LOC: 201
  * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo buffer. // If recording a demo, write it out //
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_inter.c`) -> Impact: **94.4** | LOC: 144
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...
- `D_DoomMain` **(I/O & Config Routines)** (@ `linuxdoom-1.10/d_main.c`) -> Impact: **93.8** | LOC: 376
  * *Intent:* // // D_DoomMain //
- `EV_VerticalDoor` **(Many-Argument Workhorses)** (@ `linuxdoom-1.10/p_doors.c`) -> Impact: **83.6** | LOC: 147
  * *Intent:* // // EV_VerticalDoor : open a door manually, no tag value //

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `linuxdoom-1.10` | 127 | 28908.18 | 27.0% | 20.84% |
| `sndserv` | 9 | 1000.0 | 21.47% | 18.42% |
| `sersrc` | 8 | 839.5 | 25.47% | 6.1% |
| `ipx` | 8 | 620.3 | 20.58% | 1.92% |
| `__monolith__` | 2 | 8.46 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `linuxdoom-1.10/p_tick.c` -> **99.9996%** Exposure
- `linuxdoom-1.10/i_system.c` -> **99.9836%** Exposure
- `linuxdoom-1.10/i_sound.c` -> **99.8031%** Exposure
- `sndserv/linux.c` -> **99.5664%** Exposure
- `linuxdoom-1.10/m_fixed.c` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ipx/IPXNET.C` -> **100.0%** Exposure
- `ipx/IPXSETUP.C` -> **100.0%** Exposure
- `linuxdoom-1.10/am_map.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_main.c` -> **100.0%** Exposure
- `linuxdoom-1.10/d_net.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `linuxdoom-1.10/p_enemy.c` -> **49** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/p_pspr.c` -> **24** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/i_sound.c` -> **21** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/g_game.c` -> **16** Orphaned Functions | **0** Duplicates
- `linuxdoom-1.10/p_spec.c` -> **16** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `682` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `linuxdoom-1.10/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.242)
- **Top Global Matches:** file_cluster_6: 6.242, file_cluster_4: 9.408, file_cluster_8: 16.239
- **Magnitude:** 1515.0 | **LOC:** 1691 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **28**; blast radius 5.284; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.3%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Compute Cores)** (Impact: 94.9)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 78.0)
  * `G_Responder` **(Compute Cores)** (Impact: 52.8)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 51.2)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_DoCompleted` **(I/O & Config Routines)** (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 296 instances
* *State Mutation (weighted view):* 979
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 203`, `args: 49`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 387`, `dead_code: 4`, `unreferenced_by_name: 16`
* *Architecture:* `api: 53`, `import: 28`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.284
  * `Choke Point (Betweenness):` 0.070648 | `Ripple Effect (Closeness):` 0.137868
  * `Imports (Out-Degree: 48):` am_map.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, f_finale.h, g_game.h, hu_stuff.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.98)
- **Top Global Matches:** file_cluster_4: 4.98, file_cluster_6: 9.592, file_cluster_15: 10.678
- **Magnitude:** 1415.68 | **LOC:** 2009 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.369; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (75.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A_BossDeath` **(Compute Cores)** (Impact: 71.0)
    * *Intent:* // // A_BossDeath // Possibly trigger special effects // if on first boss level //
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 54.4)
  * `A_Chase` **(Compute Cores)** (Impact: 50.5)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_SpawnFly` **(Compute Cores)** (Impact: 35.3)
  * `A_Look` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* // // ACTION ROUTINES // // // A_Look // Stay in state until a player is sighted. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 219`, `args: 77`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 279`, `unreferenced_by_name: 49`
* *Architecture:* `api: 71`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.369
  * `Choke Point (Betweenness):` 0.000838 | `Ripple Effect (Closeness):` 0.065847
  * `Imports (Out-Degree: 23):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.411)
- **Top Global Matches:** file_cluster_6: 6.411, file_cluster_4: 8.519, file_cluster_9: 16.285
- **Magnitude:** 1264.64 | **LOC:** 1851 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 3.339; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (70.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(I/O & Config Routines)** (Impact: 52.6)
  * `WI_updateDeathmatchStats` **(I/O & Config Routines)** (Impact: 34.0)
  * `WI_updateStats` **(I/O & Config Routines)** (Impact: 33.2)
  * `WI_loadData` **(I/O & Config Routines)** (Impact: 30.5)
  * `WI_drawOnLnode` **(Compute Cores)** (Impact: 23.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 117`, `args: 57`, `func_start: 35`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 286`, `dead_code: 5`, `fragile_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 38`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.339
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.098039
  * `Imports (Out-Degree: 18):` doomstat.h, g_game.h, i_system.h, m_random.h, m_swap.h, r_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.461)
- **Top Global Matches:** file_cluster_4: 6.461, file_cluster_6: 7.975, file_cluster_16: 13.452
- **Magnitude:** 1101.56 | **LOC:** 1350 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 3.527; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 72.6)
    * *Intent:* // // Handle events (user inputs) in automap mode //
  * `AM_clipMline` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algorithm but with a sligh...
  * `AM_drawFline` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* #undef DOOUTCODE // // Classic Bresenham w/ whatever optimizations needed for speed //
  * `AM_drawWalls` **(I/O & Config Routines)** (Impact: 24.4)
    * *Intent:* // // Determines visible lines, draws them. // This is LineDef based, not LineSeg based. //
  * `AM_drawLineCharacter` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 123`, `args: 53`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 257`, `dead_code: 7`, `unreferenced_by_name: 5`
* *Architecture:* `api: 41`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.527
  * `Choke Point (Betweenness):` 0.002584 | `Ripple Effect (Closeness):` 0.10181
  * `Imports (Out-Degree: 18):` am_map.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_cheat.h, p_local.h, r_state.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.147)
- **Top Global Matches:** file_cluster_15: 7.147, file_cluster_12: 7.435, file_cluster_4: 8.599
- **Magnitude:** 1056.22 | **LOC:** 1894 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **23**; blast radius 3.613; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M_Responder` **(Compute Cores)** (Impact: 164.1)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_WriteText` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* // // Write a string using the hu_font //
  * `M_Drawer` **(I/O & Config Routines)** (Impact: 13.3)
    * *Intent:* // // M_Drawer // Called after the view has been rendered, // but before it has been blitted. //
  * `M_SizeDisplay` **(Compute Cores)** (Impact: 9.6)
  * `M_SfxVol` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 282`, `args: 150`, `func_start: 54`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 188`, `dead_code: 3`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 105`, `import: 23`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.613
  * `Choke Point (Betweenness):` 0.001594 | `Ripple Effect (Closeness):` 0.104215
  * `Imports (Out-Degree: 26):` ctype.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, fcntl.h, g_game.h, hu_stuff.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.113)
- **Top Global Matches:** file_cluster_3: 9.113, file_cluster_8: 14.847, file_cluster_6: 27.76
- **Magnitude:** 931.9 | **LOC:** 919 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 3.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Many-Argument Workhorses)** (Impact: 180.7)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_GiveAmmo` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* // // GET STUFF // // // P_GiveAmmo // Num is the number of clip loads, // not the individual count ...
  * `P_KillMobj` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* // // KillMobj //
  * `P_GiveWeapon` **(Many-Argument Workhorses)** (Impact: 32.7)
    * *Intent:* // // P_GiveWeapon // The weapon name may have a MF_DROPPED flag ored in. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 469
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 133`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 157`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.99
  * `Choke Point (Betweenness):` 0.003418 | `Ripple Effect (Closeness):` 0.091278
  * `Imports (Out-Degree: 18):` am_map.h, doomdef.h, doomstat.h, dstrings.h, i_system.h, m_random.h, p_inter.h, p_local.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_spec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.267)
- **Top Global Matches:** file_cluster_6: 7.267, file_cluster_8: 9.819, file_cluster_4: 15.073
- **Magnitude:** 907.6 | **LOC:** 1363 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **14**; blast radius 6.028; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (35.9%), Connectivity (formerly Api Exposure) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 211.0)
    * *Intent:* // // EVENTS // Events are operations triggered by using, crossing, // or shooting special lines, or...
  * `P_SpawnSpecials` **(I/O & Config Routines)** (Impact: 32.2)
    * *Intent:* // Parses command line parameters.
  * `P_PlayerInSpecialSector` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* // // P_PlayerInSpecialSector // Called every tic frame // that the player origin is in a special se...
  * `P_UpdateSpecials` **(I/O & Config Routines)** (Impact: 20.7)
  * `P_ShootSpecialLine` **(Compute Cores)** (Impact: 17.7)
    * *Intent:* // // P_ShootSpecialLine - IMPACT SPECIALS // Called when a thing shoots a special line. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 175`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `state_mutation: 169`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `api: 24`, `import: 14`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.028
  * `Choke Point (Betweenness):` 0.019856 | `Ripple Effect (Closeness):` 0.092555
  * `Imports (Out-Degree: 29):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_argv.h, m_random.h, p_local.h, r_local.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.912)
- **Top Global Matches:** file_cluster_8: 5.912, file_cluster_6: 12.866, file_cluster_4: 21.614
- **Magnitude:** 867.34 | **LOC:** 990 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 4.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 50.7)
    * *Intent:* // // R_DrawSprite //
  * `R_ProjectSprite` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing // if it might be visible. //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* // R_InitSpriteDefs // Pass a null terminated list of sprite names // (4 chars exactly) to be used. ...
  * `R_DrawPSprite` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // // R_DrawPSprite //
  * `R_InstallSpriteLump` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* // // R_InstallSpriteLump // Local function for R_InitSprites. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 45`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 213`, `dead_code: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.256
  * `Choke Point (Betweenness):` 0.001806 | `Ripple Effect (Closeness):` 0.098771
  * `Imports (Out-Degree: 12):` doomdef.h, doomstat.h, i_system.h, m_swap.h, r_local.h, stdio.h, stdlib.h, w_wad.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.973)
- **Top Global Matches:** file_cluster_8: 6.973, file_cluster_6: 9.144, file_cluster_4: 17.804
- **Magnitude:** 856.72 | **LOC:** 989 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **10**; blast radius 5.702; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 68.6)
    * *Intent:* // // P_XYMovement // #define STOPSPEED 0x1000 #define FRICTION 0xe800
  * `P_ZMovement` **(Compute Cores)** (Impact: 44.8)
    * *Intent:* // // P_ZMovement //
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 41.3)
    * *Intent:* // // P_SpawnMapThing // The fields of the mapthing should // already be in host byte order. //
  * `P_MobjThinker` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* // // P_MobjThinker //
  * `P_SpawnMobj` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* // // P_SpawnMobj //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 521
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 52`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 187`, `fragile_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 19`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.702
  * `Choke Point (Betweenness):` 0.015305 | `Ripple Effect (Closeness):` 0.111221
  * `Imports (Out-Degree: 22):` doomdef.h, doomstat.h, hu_stuff.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.396)
- **Top Global Matches:** file_cluster_4: 6.396, file_cluster_6: 9.012, file_cluster_9: 11.611
- **Magnitude:** 850.74 | **LOC:** 1340 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 4.794; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 32.9)
    * *Intent:* // // PIT_CheckThing //
  * `PTR_ShootTraverse` **(Compute Cores)** (Impact: 32.8)
    * *Intent:* // // PTR_ShootTraverse //
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* // // P_TryMove // Attempt to move to a new position, // crossing special lines unless MF_TELEPORT i...
  * `PTR_AimTraverse` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // // PTR_AimTraverse // Sets linetaget and aimslope when a target is aimed at. //
  * `PIT_CheckLine` **(Compute Cores)** (Impact: 24.2)
    * *Intent:* // // MOVEMENT ITERATOR FUNCTIONS // // // PIT_CheckLine // Adjusts tmfloorz and tmceilingz as lines...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 153`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 212`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 22`, `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.794
  * `Choke Point (Betweenness):` 0.00793 | `Ripple Effect (Closeness):` 0.107604
  * `Imports (Out-Degree: 19):` doomdef.h, doomstat.h, i_system.h, m_bbox.h, m_random.h, p_local.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/st_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.229)
- **Top Global Matches:** file_cluster_4: 8.229, file_cluster_6: 10.869, file_cluster_12: 12.238
- **Magnitude:** 846.64 | **LOC:** 1472 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **20**; blast radius 3.726; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ST_Responder` **(Compute Cores)** (Impact: 99.5)
    * *Intent:* // Respond to keyboard input events, // intercept cheats.
  * `ST_updateFaceWidget` **(I/O & Config Routines)** (Impact: 42.5)
    * *Intent:* // // This is a not-very-pretty routine which handles // the face states and their timing. // the pr...
  * `ST_doPaletteStuff` **(I/O & Config Routines)** (Impact: 15.7)
  * `ST_updateWidgets` **(I/O & Config Routines)** (Impact: 15.2)
  * `ST_drawWidgets` **(Compute Cores)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 181 instances
* *State Mutation (weighted view):* 568
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 73`, `args: 33`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 206`, `dead_code: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 22`, `import: 20`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.726
  * `Choke Point (Betweenness):` 0.012546 | `Ripple Effect (Closeness):` 0.105882
  * `Imports (Out-Degree: 30):` am_map.h, doomdef.h, doomstat.h, dstrings.h, g_game.h, i_system.h, i_video.h, m_cheat.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/i_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_8: 5.695, file_cluster_6: 14.958, file_cluster_3: 22.021
- **Magnitude:** 827.28 | **LOC:** 1051 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **21**; blast radius 4.755; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `I_InitGraphics` **(I/O & Config Routines)** (Impact: 47.2)
  * `xlatekey` **(Compute Cores)** (Impact: 44.3)
    * *Intent:* // // Translates the key currently in X_event //
  * `I_GetEvent` **(I/O & Config Routines)** (Impact: 32.3)
  * `I_FinishUpdate` **(I/O & Config Routines)** (Impact: 31.5)
    * *Intent:* // // I_FinishUpdate //
  * `grabsharedmemory` **(Compute Cores)** (Impact: 28.8)
    * *Intent:* // // This function is probably redundant, // if XShmDetach works properly. // ddt never detached th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 555
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 78`, `args: 45`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 237`, `dead_code: 10`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 18`, `import: 21`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.755
  * `Choke Point (Betweenness):` 0.007489 | `Ripple Effect (Closeness):` 0.116099
  * `Imports (Out-Degree: 9):` Xlib.h, Xutil.h, XShm.h, keysym.h, d_main.h, doomdef.h, doomstat.h, errnos.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.256)
- **Top Global Matches:** file_cluster_1: 5.256, file_cluster_3: 48.151, file_cluster_8: 69.991
- **Magnitude:** 772.98 | **LOC:** 747 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 3.709; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 136.4)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 35.0)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked // texture) for wal...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 178 instances
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 194`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.709
  * `Choke Point (Betweenness):` 0.000241 | `Ripple Effect (Closeness):` 0.074776
  * `Imports (Out-Degree: 10):` doomdef.h, doomstat.h, i_system.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.123)
- **Top Global Matches:** file_cluster_4: 7.123, file_cluster_12: 10.63, file_cluster_6: 11.233
- **Magnitude:** 726.84 | **LOC:** 709 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 3.339; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_SetupLevel` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* // // P_SetupLevel //
  * `P_LoadLineDefs` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // // P_LoadLineDefs // Also counts secret lines for intermissions. //
  * `P_LoadThings` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* // // P_LoadThings //
  * `P_GroupLines` **(I/O & Config Routines)** (Impact: 17.9)
    * *Intent:* // // P_GroupLines // Builds sector line lists and subsector sector numbers. // Finds block bounding...
  * `P_LoadSegs` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* // // P_LoadSegs //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 20`, `args: 14`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 214`, `unreferenced_by_name: 2`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.339
  * `Choke Point (Betweenness):` 0.006429 | `Ripple Effect (Closeness):` 0.098039
  * `Imports (Out-Degree: 22):` doomdef.h, doomstat.h, g_game.h, i_system.h, m_bbox.h, m_swap.h, math.h, p_local.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.236)
- **Top Global Matches:** file_cluster_6: 10.236, file_cluster_8: 11.406, file_cluster_4: 17.275
- **Magnitude:** 723.16 | **LOC:** 1172 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **30**; blast radius 4.761; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `D_DoomMain` **(I/O & Config Routines)** (Impact: 93.8)
    * *Intent:* // // D_DoomMain //
  * `D_Display` **(Stateful Encapsulated Methods)** (Impact: 50.6)
  * `D_DoAdvanceDemo` **(I/O & Config Routines)** (Impact: 22.2)
    * *Intent:* // // This cycles through the demo sequences. // FIXME - version dependend demo numbers? //
  * `IdentifyVersion` **(I/O & Config Routines)** (Impact: 20.8)
    * *Intent:* // // IdentifyVersion // Checks availability of IWAD files by name, // to determine whether register...
  * `FindResponseFile` **(I/O & Config Routines)** (Impact: 18.4)
    * *Intent:* // // Find a Response File //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 145 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 101`, `args: 32`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 160`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `api: 25`, `import: 30`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.761
  * `Choke Point (Betweenness):` 0.022643 | `Ripple Effect (Closeness):` 0.107604
  * `Imports (Out-Degree: 45):` am_map.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, f_finale.h, f_wipe.h, fcntl.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.109)
- **Top Global Matches:** file_cluster_4: 7.109, file_cluster_9: 8.521, file_cluster_15: 11.058
- **Magnitude:** 715.54 | **LOC:** 884 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 3.966; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_PathTraverse` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* // // P_PathTraverse // Traces a line from x1,y1 to x2,y2, // calling the traverser function for eac...
  * `P_UnsetThingPosition` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* // // THING POSITION SETTING // // // P_UnsetThingPosition // Unlinks a thing from block map and sec...
  * `P_PointOnDivlineSide` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* // // P_PointOnDivlineSide // Returns 0 or 1. //
  * `PIT_AddLineIntercepts` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* // // PIT_AddLineIntercepts. // Looks for lines in the given block // that intercept the given trace...
  * `P_BoxOnLineSide` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 145 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 70`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 153`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.966
  * `Choke Point (Betweenness):` 0.000399 | `Ripple Effect (Closeness):` 0.084842
  * `Imports (Out-Degree: 6):` doomdef.h, m_bbox.h, p_local.h, r_state.h, stdlib.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `sndserv/soundsrv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.394)
- **Top Global Matches:** file_cluster_3: 10.394, file_cluster_8: 15.427, file_cluster_6: 27.936
- **Magnitude:** 712.88 | **LOC:** 741 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 3.155; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `addsfx` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `grabdata` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `mix` **(I/O & Config Routines)** (Impact: 33.9)
  * `outputushort` **(Stateful Encapsulated Methods)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 25`, `args: 11`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 167`, `dead_code: 18`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 10`, `import: 13`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fcntl.h, malloc.h, math.h, sounds.h, soundsrv.h, stdio.h, stdlib.h, ioctl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `linuxdoom-1.10/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.967)
- **Top Global Matches:** file_cluster_3: 5.967, file_cluster_8: 20.76, file_cluster_6: 33.743
- **Magnitude:** 642.86 | **LOC:** 556 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 4.366; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `T_MovePlane` **(Many-Argument Workhorses)** (Impact: 79.2)
    * *Intent:* // State. #include "doomstat.h" #include "r_state.h" // Data. #include "sounds.h" // // FLOORS // //...
  * `EV_DoFloor` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* // // HANDLE FLOOR TYPES //
  * `EV_BuildStairs` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* // // BUILD A STAIRCASE! //
  * `T_MoveFloor` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* // // MOVE A FLOOR TO IT'S DESTINATION (UP OR DOWN) //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 54`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 149`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.366
  * `Choke Point (Betweenness):` 0.000592 | `Ripple Effect (Closeness):` 0.074356
  * `Imports (Out-Degree: 12):` doomdef.h, doomstat.h, p_local.h, r_state.h, s_sound.h, sounds.h, z_zone.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/d_net.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.272)
- **Top Global Matches:** file_cluster_8: 8.272, file_cluster_6: 10.211, file_cluster_4: 18.393
- **Magnitude:** 639.8 | **LOC:** 768 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 4.192; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TryRunTics` **(I/O & Config Routines)** (Impact: 39.6)
  * `GetPackets` **(I/O & Config Routines)** (Impact: 21.9)
  * `D_ArbitrateNetStart` **(I/O & Config Routines)** (Impact: 21.6)
    * *Intent:* // // D_ArbitrateNetStart //
  * `HGetPacket` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* // // HGetPacket // Returns false if no packet is waiting //
  * `NetUpdate` **(I/O & Config Routines)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 72`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 149`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 17`, `import: 7`
* *Defense:* `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.192
  * `Choke Point (Betweenness):` 0.020312 | `Ripple Effect (Closeness):` 0.119237
  * `Imports (Out-Degree: 13):` doomdef.h, doomstat.h, g_game.h, i_net.h, i_system.h, i_video.h, m_menu.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/r_data.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.635)
- **Top Global Matches:** file_cluster_4: 7.635, file_cluster_12: 10.025, file_cluster_7: 11.844
- **Magnitude:** 634.34 | **LOC:** 850 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 4.783; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_InitTextures` **(I/O & Config Routines)** (Impact: 24.2)
    * *Intent:* // // R_InitTextures // Initializes the texture list // with the textures from the world map. //
  * `R_PrecacheLevel` **(I/O & Config Routines)** (Impact: 20.1)
  * `R_GenerateLookup` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* // // R_GenerateLookup //
  * `R_GenerateComposite` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* // // R_GenerateComposite // Using the texture definition, // the composite texture is created from ...
  * `R_DrawColumnInCache` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* // for a column directory and any new columns. // The directory will simply point inside other patch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 36`, `args: 15`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 185`, `unreferenced_by_name: 5`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.783
  * `Choke Point (Betweenness):` 0.001869 | `Ripple Effect (Closeness):` 0.124861
  * `Imports (Out-Degree: 12):` alloca.h, doomdef.h, doomstat.h, i_system.h, m_swap.h, p_local.h, r_data.h, r_local.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.236)
- **Top Global Matches:** file_cluster_12: 7.236, file_cluster_7: 7.964, file_cluster_5: 9.833
- **Magnitude:** 598.3 | **LOC:** 587 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.249; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_UnArchiveSpecials` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_ArchiveSpecials` **(I/O & Config Routines)** (Impact: 18.8)
    * *Intent:* // // Things to handle: // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_Ver...
  * `P_UnArchiveThinkers` **(I/O & Config Routines)** (Impact: 12.9)
    * *Intent:* // // P_UnArchiveThinkers //
  * `P_ArchiveWorld` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* // // P_ArchiveWorld //
  * `P_UnArchiveWorld` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* // // P_UnArchiveWorld //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 157 instances
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 43`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 183`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.249
  * `Choke Point (Betweenness):` 0.003057 | `Ripple Effect (Closeness):` 0.095218
  * `Imports (Out-Degree: 11):` doomstat.h, i_system.h, p_local.h, r_state.h, z_zone.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/r_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.143)
- **Top Global Matches:** file_cluster_4: 6.143, file_cluster_15: 8.481, file_cluster_16: 9.566
- **Magnitude:** 589.32 | **LOC:** 899 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **7**; blast radius 6.65; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (63.1%)
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
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 59`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 141`, `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.65
  * `Choke Point (Betweenness):` 0.031592 | `Ripple Effect (Closeness):` 0.140801
  * `Imports (Out-Degree: 14):` d_net.h, doomdef.h, m_bbox.h, math.h, r_local.h, r_sky.h, stdlib.h
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/f_finale.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.605)
- **Top Global Matches:** file_cluster_6: 5.605, file_cluster_4: 10.535, file_cluster_8: 14.788
- **Magnitude:** 577.78 | **LOC:** 739 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 3.339; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `F_CastTicker` **(Compute Cores)** (Impact: 52.0)
    * *Intent:* // // F_CastTicker //
  * `F_StartFinale` **(I/O & Config Routines)** (Impact: 25.8)
    * *Intent:* // // F_StartFinale //
  * `F_Ticker` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* // // F_Ticker //
  * `F_CastPrint` **(Compute Cores)** (Impact: 15.2)
  * `F_TextWrite` **(I/O & Config Routines)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 101`, `args: 21`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 134`, `fragile_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 20`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.339
  * `Choke Point (Betweenness):` 0.000198 | `Ripple Effect (Closeness):` 0.099513
  * `Imports (Out-Degree: 14):` ctype.h, doomstat.h, dstrings.h, hu_stuff.h, i_system.h, m_swap.h, r_state.h, s_sound.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/s_sound.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.844)
- **Top Global Matches:** file_cluster_6: 6.844, file_cluster_4: 6.934, file_cluster_9: 14.539
- **Magnitude:** 546.52 | **LOC:** 880 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **12**; blast radius 6.995; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `S_StartSoundAtVolume` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `S_StartSound` **(Stateful Encapsulated Methods)** (Impact: 31.2)
  * `S_AdjustSoundParams` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* // // Changes volume, stereo-separation, and pitch variables // from the norm of a sound effect to b...
  * `S_UpdateSounds` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* // // Updates music & sounds //
  * `S_getChannel` **(Compute Cores)** (Impact: 21.5)
    * *Intent:* // // S_getChannel : // If none available, return -1. Otherwise channel #. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 47`, `args: 20`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 95`, `dead_code: 7`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.995
  * `Choke Point (Betweenness):` 0.009678 | `Ripple Effect (Closeness):` 0.136446
  * `Imports (Out-Degree: 16):` doomdef.h, doomstat.h, i_sound.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `linuxdoom-1.10/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.837)
- **Top Global Matches:** file_cluster_15: 5.837, file_cluster_4: 7.356, file_cluster_16: 7.842
- **Magnitude:** 534.34 | **LOC:** 880 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 4.013; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.6%), Complexity Load (formerly Cognitive Load) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CheckAmmo` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* // // P_CheckAmmo // Returns true if there is enough ammo to shoot. // If not, selects the next weap...
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.5)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `P_SetPsprite` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* #define LOWERSPEED FRACUNIT*6 #define RAISESPEED FRACUNIT*6 #define WEAPONBOTTOM 128*FRACUNIT #defin...
  * `A_Saw` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* // // A_Saw //
  * `A_ReFire` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* // // A_ReFire // The player can re-fire the weapon // without lowering it entirely. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 48`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 106`, `unreferenced_by_name: 24`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.013
  * `Choke Point (Betweenness):` 0.002774 | `Ripple Effect (Closeness):` 0.084301
  * `Imports (Out-Degree: 16):` d_event.h, doomdef.h, doomstat.h, m_random.h, p_local.h, p_pspr.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `linuxdoom-1.10/i_sound.c` (C) | Magnitude: 489.58 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 232, state_mutation: 113, core_var_decl: 66, design_snake_case: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `linuxdoom-1.10/f_wipe.h` (C) | Magnitude: 18.58 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, args: 3, api: 3, macros: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `linuxdoom-1.10/d_player.h` (C) | Magnitude: 22.68 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 10, class_start: 5, api: 5
- `linuxdoom-1.10/r_state.h` (C) | Magnitude: 60.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 44, globals: 44, macros: 4, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `linuxdoom-1.10/s_sound.c` (C) | Magnitude: 546.52 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 227, branch: 106, state_mutation: 95, indent_tabs: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `linuxdoom-1.10/z_zone.c` (C) | Magnitude: 316.52 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 147, indent_spaces: 105, state_mutation: 79, indent_tabs: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `sersrc/PORT.C` (C) | Magnitude: 233.26 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 196, state_mutation: 51, branch: 47, structural_boundaries: 42

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `linuxdoom-1.10/g_game.c` -> **Severity: 7.065** (Bridge: 0.0706 * Flux: 100.0%)
- `linuxdoom-1.10/i_system.c` -> **Severity: 3.319** (Bridge: 0.0437 * Flux: 75.9767%)
- `linuxdoom-1.10/r_main.c` -> **Severity: 3.159** (Bridge: 0.0316 * Flux: 100.0%)
- `linuxdoom-1.10/d_main.c` -> **Severity: 2.264** (Bridge: 0.0226 * Flux: 100.0%)
- `linuxdoom-1.10/z_zone.c` -> **Severity: 2.259** (Bridge: 0.0226 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `linuxdoom-1.10/doomdef.h` -> **Severity: 17.356** (Embedded: 0.3362 * Error Risk: 51.6228%)
- `linuxdoom-1.10/z_zone.c` -> **Severity: 16.644** (Embedded: 0.1946 * Error Risk: 85.5123%)
- `linuxdoom-1.10/w_wad.c` -> **Severity: 13.739** (Embedded: 0.1719 * Error Risk: 79.93%)
- `linuxdoom-1.10/g_game.c` -> **Severity: 11.57** (Embedded: 0.1379 * Error Risk: 83.9194%)
- `linuxdoom-1.10/r_main.c` -> **Severity: 11.226** (Embedded: 0.1408 * Error Risk: 79.7304%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `linuxdoom-1.10/z_zone.c` -> **Severity: 1005.8** (Blast Radius: 10.058 * Doc Risk: 100.0%)
- `linuxdoom-1.10/m_fixed.c` -> **Severity: 760.3** (Blast Radius: 7.603 * Doc Risk: 100.0%)
- `linuxdoom-1.10/w_wad.c` -> **Severity: 709.5** (Blast Radius: 7.095 * Doc Risk: 100.0%)
- `linuxdoom-1.10/i_system.c` -> **Severity: 701.9** (Blast Radius: 7.019 * Doc Risk: 100.0%)
- `linuxdoom-1.10/s_sound.c` -> **Severity: 699.5** (Blast Radius: 6.995 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 192 literal sites + 5 sites through wrappers = 197
- **`memory_alloc`:** 38 literal sites + 3 sites through wrappers = 41
- **`panics_and_aborts`:** 25 literal sites + 7 sites through wrappers = 32

- `derror` (function, debug_prints, primitive): 2 call sites in 1 files -- `sndserv/soundsrv.c`
- `derror` (function, debug_prints, primitive): 2 call sites in 1 files -- `sndserv/wadread.c`
- `derror` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `sndserv/soundsrv.c`
- `derror` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `sndserv/wadread.c`
- `quit` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `sndserv/soundsrv.c`
- `I_AllocLow` (function, memory_alloc, primitive): 1 call sites in 1 files -- `linuxdoom-1.10/i_system.c`
- `I_Error` (function, debug_prints, primitive): 1 call sites in 1 files -- `sersrc/SERSETUP.C`
- `I_Error` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `sersrc/SERSETUP.C`
- `I_ZoneBase` (function, memory_alloc, primitive): 1 call sites in 1 files -- `linuxdoom-1.10/i_system.c`
- `V_Init` (function, memory_alloc, via I_AllocLow): 1 call sites in 1 files -- `linuxdoom-1.10/v_video.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2221 call pairs -- scoped 24.4%, unique 42.8%, ambiguous 5.2%, external 27.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 2221 | 24.4% | 42.8% | 5.2% | 27.6% |

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
