# ARCHITECTURAL_BRIEF: normal_rp2040_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/kilograham/rp2040-doom.git` |
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
- **Scope:** 683 analyzed artifact(s), 200435 LOC.
- **Load-bearing artifact:** `src/i_system.h` -- 151 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/strife/d_main.c` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/whd_gen/lodepng.cpp` at magnitude 7894.44 (structural weight, not risk).
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
| Total Artifacts | 780 |
| Analyzed Artifacts (Scanned) | 683 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 97 |
| Total LOC | 200435 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.6% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5026 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1012 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8652 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 578 | 181502 | 84.6% |
| PLAINTEXT | 22 | 0 | 3.2% |
| CPP | 19 | 15549 | 2.8% |
| MARKDOWN | 15 | 0 | 2.2% |
| M4 | 13 | 399 | 1.9% |
| MAKEFILE | 9 | 648 | 1.3% |
| OBJECTIVE-C | 8 | 859 | 1.2% |
| XML | 7 | 0 | 1.0% |
| PYTHON | 5 | 689 | 0.7% |
| SHELL | 4 | 60 | 0.6% |
| ASSEMBLY | 2 | 708 | 0.3% |
| YAML | 1 | 21 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 683 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 35%, Large Core Modules (3) 19%, Data / Markup / Trivial 11%, Compute Cores Files 9%, Encapsulated Accessors Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 646 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 37 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 97*

**Composition by Extension & Reason:**
- `no_extension`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 2452 LOC)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.am`: 12x Excluded (Unsupported Extension: '.am')
- `.template`: 10x Excluded (Unsupported Extension: '.template')
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Embedded Hex Payload: 16384 hex tokens in 2737 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4694 LOC)
- `.h`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1373 LOC), 1x Excluded (Machine-Generated Source Code Signature: 3621 LOC)
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.man`: 2x Excluded (Unsupported Extension: '.man')
- `.icns`: 2x Excluded (Unsupported Extension: '.icns')
- `.nib`: 2x Excluded (Unsupported Extension: '.nib')
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cin`: 1x Excluded (Unsupported Extension: '.cin')
- `.whx`: 1x Excluded (Unsupported Extension: '.whx')
- `.ds_store`: 1x Excluded (Unsupported Extension: '.DS_Store')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.4 | 31.2 | 15.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.8 | 40.4 | 55.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.5 | 9.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 30.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 26.6 | 7.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.7 | 81.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 950 | 155 | 3 | `src/whd_gen/whd_gen.cpp` |
| cleanup | 292 | 89 | 1 | `textscreen/txt_fileselect.c` |
| guards | 6760 | 402 | 26 | `src/whd_gen/whd_gen.cpp` |
| danger | 744 | 198 | 3 | `src/z_zone.c` |
| concurrency | 4 | 2 | 0 | `src/pd_render.cpp` |
| connectivity | 8483 | 556 | 25 | `src/hexen/h2def.h` |
| io | 247 | 74 | 1 | `pkg/osx/GNUmakefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 9 | 0 | `pkg/win32/cp-with-libs` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 30 | 8 | 0 | `man/docgen` |
| events | 550 | 40 | 0 | `opl/slot_render.cpp` |
| tests | 5 | 3 | 0 | `src/midifile.c` |
| docs | 183 | 32 | 0 | `src/whd_gen/lodepng.cpp` |
| debt | 1271 | 219 | 5 | `src/whd_gen/whd_gen.cpp` |
| mutation | 57875 | 409 | 297 | `src/whd_gen/lodepng.cpp` |
| dead_code | 3915 | 324 | 11 | `src/strife/p_saveg.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 68 | 31 | 0 | `src/strife/p_dialog.c` |
| ui | 2 | 1 | 0 | `midiproc/main.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pkg/osx/GNUmakefile` (Hits: 23)
- `src/i_sdlsound.c` (Hits: 19)
- `src/hexen/sv_save.c` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i_system.h** (`src/i_system.h`) — 151 inbound connections
2. **doomtype.h** (`src/doomtype.h`) — 149 inbound connections
3. **m_misc.h** (`src/m_misc.h`) — 112 inbound connections
4. **m_misc.c** (`src/m_misc.c`) — 108 inbound connections
5. **z_zone.h** (`src/z_zone.h`) — 99 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **d_main.c** (`src/strife/d_main.c`) — 47 outbound dependencies
2. **d_main.c** (`src/doom/d_main.c`) — 46 outbound dependencies
3. **g_game.c** (`src/doom/g_game.c`) — 39 outbound dependencies
4. **i_video.c** (`src/pico/i_video.c`) — 38 outbound dependencies
5. **g_game.c** (`src/strife/g_game.c`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `src/strife/p_switch.c`) -> Impact: **473.4** | LOC: 629
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `P_CrossSpecialLine` **(Many-Argument Workhorses)** (@ `src/strife/p_spec.c`) -> Impact: **372.9** | LOC: 818
  * *Intent:* // // P_CrossSpecialLine - TRIGGER // Called every time a thing origin is about // to cross a line with a non 0 special. //
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `src/hexen/p_inter.c`) -> Impact: **318.0** | LOC: 367
  * *Intent:* */
- `P_ExecuteLineSpecial` **(Many-Argument Workhorses)** (@ `src/hexen/p_spec.c`) -> Impact: **276.2** | LOC: 332
  * *Intent:* */ //============================================================================ // // P_ExecuteLineSpecial // // Invoked when crossing a linedef. Th...
- `G_BuildTiccmd` **(Many-Argument Workhorses)** (@ `src/hexen/g_game.c`) -> Impact: **264.4** | LOC: 472
- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `src/doom/p_switch.c`) -> Impact: **262.9** | LOC: 379
  * *Intent:* // // P_UseSpecialLine // Called when a thing uses a special line. // Only the front sides of lines are usable. //
- `MN_Responder` **(Compute Cores)** (@ `src/hexen/mn_menu.c`) -> Impact: **257.6** | LOC: 570
  * *Intent:* //--------------------------------------------------------------------------- // // FUNC MN_Responder // //-------------------------------------------...
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `src/strife/p_inter.c`) -> Impact: **253.9** | LOC: 337
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...
- `M_Responder` **(Compute Cores)** (@ `src/strife/m_menu.c`) -> Impact: **249.0** | LOC: 568
  * *Intent:* // // CONTROL PANEL // // // M_Responder //
- `MN_Responder` **(Compute Cores)** (@ `src/heretic/mn_menu.c`) -> Impact: **244.8** | LOC: 541
  * *Intent:* //--------------------------------------------------------------------------- // // FUNC MN_Responder // //-------------------------------------------...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/hexen` | 61 | 38998.54 | 49.5% | 24.15% |
| `src/strife` | 104 | 30650.72 | 30.79% | 22.7% |
| `src/doom` | 104 | 28697.58 | 31.59% | 21.08% |
| `src/heretic` | 63 | 26982.14 | 43.18% | 22.15% |
| `src` | 146 | 22701.18 | 25.1% | 23.35% |
| `src/whd_gen` | 17 | 14067.62 | 35.3% | 13.76% |
| `textscreen` | 45 | 5435.08 | 22.14% | 21.66% |
| `opl` | 23 | 5285.94 | 28.65% | 17.65% |
| `src/pico` | 16 | 3602.72 | 33.83% | 27.1% |
| `src/setup` | 31 | 2493.9 | 10.72% | 10.59% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/i_cdmus.c` -> **100.0%** Exposure
- `src/strife/p_tick.c` -> **99.9996%** Exposure
- `src/pico/i_timer.c` -> **99.9983%** Exposure
- `src/deh_mapping.c` -> **99.9826%** Exposure
- `src/m_fixed.c` -> **99.9665%** Exposure
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
- **Unknown Dependencies:** `3787` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/whd_gen/lodepng.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.615)
- **Top Global Matches:** file_cluster_4: 5.615, file_cluster_6: 9.258, file_cluster_15: 12.043
- **Magnitude:** 7894.44 | **LOC:** 6256 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.8%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.5764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lodepng_get_color_profile` **(Many-Argument Workhorses)** (Impact: 227.2)
    * *Intent:* /*profile must already have been inited with mode. It's ok to set some parameters of profile to done...
  * `encodeLZ77` **(Many-Argument Workhorses)** (Impact: 223.8)
    * *Intent:* */
  * `decodeGeneric` **(Many-Argument Workhorses)** (Impact: 208.4)
    * *Intent:* #endif /*LODEPNG_COMPILE_ANCILLARY_CHUNKS*/ /*read a PNG, the result will be in the same color type ...
  * `deflateDynamic` **(Many-Argument Workhorses)** (Impact: 183.2)
    * *Intent:* /*Deflate for a block of type "dynamic", that is, with freely, optimally, created huffman trees*/
  * `lodepng_encode` **(Many-Argument Workhorses)** (Impact: 165.7)
    * *Intent:* #endif /*LODEPNG_COMPILE_ANCILLARY_CHUNKS*/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1212 instances
* *State Mutation (weighted view):* 3797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1381`, `structural_boundaries: 476`, `args: 244`, `func_start: 229`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1373`, `dead_code: 9`, `planned_debt: 9`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 5`, `import: 4`
* *Defense:* `safety: 7`, `doc: 50`, `immutability_locks: 237`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039165
  * `Imports (Out-Degree: 1):` limits.h, lodepng.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/whd_gen/whd_gen.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.588)
- **Top Global Matches:** file_cluster_8: 6.588, file_cluster_6: 11.034, file_cluster_4: 19.549
- **Magnitude:** 4484.36 | **LOC:** 5332 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **26**; blast radius 1.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.2%), Guard Balance (formerly Safety Score) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 211.9)
    * *Intent:* #endif
  * `convert_textures` **(Many-Argument Workhorses)** (Impact: 201.8)
  * `convert_vpatch` **(Many-Argument Workhorses)** (Impact: 193.5)
    * *Intent:* // use_runs = true to do runs of pixels, false to use 0 as transparent color
  * `optimize_column` **(Many-Argument Workhorses)** (Impact: 171.1)
  * `convert_sidedefs` **(Many-Argument Workhorses)** (Impact: 151.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 721 instances
* *State Mutation (weighted view):* 2302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 317`, `args: 140`, `func_start: 56`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 860`, `dead_code: 52`, `planned_debt: 23`, `fragile_debt: 6`, `unreferenced_by_name: 4`
* *Architecture:* `import: 26`
* *Defense:* `safety: 121`, `immutability_locks: 133`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.516
  * `Choke Point (Betweenness):` 0.005348 | `Ripple Effect (Closeness):` 0.047364
  * `Imports (Out-Degree: 18):` normal.h, adpcm-lib.h, algorithm, array, cassert, cmath, compress_mus.h, cstdarg...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/hexen/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.106)
- **Top Global Matches:** file_cluster_4: 5.106, file_cluster_15: 9.293, file_cluster_16: 10.422
- **Magnitude:** 4128.88 | **LOC:** 5444 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 0.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DragonSeek` **(Many-Argument Workhorses)** (Impact: 60.1)
    * *Intent:* //============================================================================ // // DragonSeek // /...
  * `A_SorcBallOrbit` **(Compute Cores)** (Impact: 57.6)
    * *Intent:* // // A_SorcBallOrbit() ========================================== //
  * `A_Chase` **(Compute Cores)** (Impact: 57.4)
    * *Intent:* */
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 55.2)
  * `A_FastChase` **(Compute Cores)** (Impact: 50.3)
    * *Intent:* //============================================================================ // Class Bosses //===...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 682 instances
* *State Mutation (weighted view):* 2274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 769`, `structural_boundaries: 502`, `args: 231`, `func_start: 172`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 910`, `dead_code: 8`, `unreferenced_by_name: 120`
* *Architecture:* `api: 199`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.827
  * `Choke Point (Betweenness):` 0.000533 | `Ripple Effect (Closeness):` 0.021259
  * `Imports (Out-Degree: 13):` h2def.h, i_swap.h, i_system.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/pd_render.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.937)
- **Top Global Matches:** file_cluster_8: 7.937, file_cluster_6: 10.177, file_cluster_4: 18.323
- **Magnitude:** 2935.86 | **LOC:** 3116 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **30**; blast radius 0.758; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pd_end_frame` **(Many-Argument Workhorses)** (Impact: 179.6)
  * `draw_composite_columns` **(Many-Argument Workhorses)** (Impact: 149.0)
  * `draw_patch_columns` **(Many-Argument Workhorses)** (Impact: 100.7)
  * `push_down_x_guts` **(Many-Argument Workhorses)** (Impact: 80.9)
    * *Intent:* #endif // new_index can be a (non overlapping) linked list (in ascending y order)
  * `push_down_x_fuzzy` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* // new_index can be a (non overlapping) linked list (in ascending y order) // for fuzzy columns we'r...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 512 instances
* *State Mutation (weighted view):* 1654
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 604`, `structural_boundaries: 117`, `args: 52`, `func_start: 51`, `class_start: 4`
* *Risk/State:* `state_mutation: 630`, `dead_code: 75`, `planned_debt: 34`, `fragile_debt: 10`, `unreferenced_by_name: 12`
* *Architecture:* `import: 31`
* *Defense:* `safety: 94`, `sync_locks: 3`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.758
  * `Choke Point (Betweenness):` 0.001955 | `Ripple Effect (Closeness):` 0.011713
  * `Imports (Out-Degree: 37):` statsomizer.h, algorithm, am_map.h, d_main.h, doomstat.h, f_finale.h, f_wipe.h, hu_stuff.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/hexen/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.07)
- **Top Global Matches:** file_cluster_8: 7.07, file_cluster_6: 8.92, file_cluster_4: 17.527
- **Magnitude:** 2196.06 | **LOC:** 2471 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **6**; blast radius 1.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 162.2)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_ZMovement` **(Compute Cores)** (Impact: 118.2)
    * *Intent:* */
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 98.1)
    * *Intent:* //========================================================================== // // P_SpawnMapThing /...
  * `P_FloorBounceMissile` **(Compute Cores)** (Impact: 44.1)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_FloorBou...
  * `P_MobjThinker` **(Compute Cores)** (Impact: 43.5)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_MobjThin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 370 instances
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 486`, `structural_boundaries: 164`, `args: 49`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 460`, `dead_code: 20`, `fragile_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 40`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.261
  * `Choke Point (Betweenness):` 0.00273 | `Ripple Effect (Closeness):` 0.026138
  * `Imports (Out-Degree: 14):` h2def.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/strife/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.257)
- **Top Global Matches:** file_cluster_4: 5.257, file_cluster_15: 8.378, file_cluster_16: 9.593
- **Magnitude:** 2114.12 | **LOC:** 3373 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **18**; blast radius 0.711; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A_BossDeath` **(Compute Cores)** (Impact: 71.0)
    * *Intent:* // // A_BossDeath // // Possibly trigger special effects // if on first boss level // // haleyjd 09/...
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 54.7)
    * *Intent:* // // P_NewChaseDir //
  * `P_LookForPlayers` **(Many-Argument Workhorses)** (Impact: 54.5)
    * *Intent:* // // P_LookForPlayers // // If allaround is false, only look 180 degrees in front. // Returns true ...
  * `A_Chase` **(Compute Cores)** (Impact: 51.0)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible // // haleyjd...
  * `P_DoPunchAlert` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* // // P_DoPunchAlert // // villsa [STRIFE] New function (by Quasar ;) // Wake up buddies nearby when...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 307 instances
* *State Mutation (weighted view):* 1068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 270`, `args: 121`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 454`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 85`
* *Architecture:* `api: 119`, `import: 18`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.711
  * `Choke Point (Betweenness):` 0.00098 | `Ripple Effect (Closeness):` 0.011436
  * `Imports (Out-Degree: 24):` deh_str.h, doomdef.h, doomstat.h, f_finale.h, g_game.h, i_system.h, m_misc.h, m_random.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/doom/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.938)
- **Top Global Matches:** file_cluster_6: 5.938, file_cluster_4: 8.865, file_cluster_8: 16.477
- **Magnitude:** 1984.04 | **LOC:** 2651 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **39**; blast radius 0.62; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 149.3)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 84.3)
  * `G_Responder` **(Compute Cores)** (Impact: 67.0)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 66.8)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_DoCompleted` **(I/O & Config Routines)** (Impact: 53.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 361 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 261`, `args: 68`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 457`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 15`
* *Architecture:* `io: 8`, `api: 48`, `import: 40`
* *Defense:* `safety: 5`, `immutability_locks: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.62
  * `Choke Point (Betweenness):` 0.000488 | `Ripple Effect (Closeness):` 0.004792
  * `Imports (Out-Degree: 51):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `opl/emu8950.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.816)
- **Top Global Matches:** file_cluster_4: 5.816, file_cluster_6: 9.125, file_cluster_16: 11.783
- **Magnitude:** 1881.46 | **LOC:** 2028 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.691; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.4706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OPL_writeReg` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `OPL_calc_buffer_linear` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* // this produces stereo
  * `calc_envelope` **(Stateful Encapsulated Methods)** (Impact: 38.0)
  * `commit_slot_update` **(Stateful Encapsulated Methods)** (Impact: 32.8)
  * `update_output` **(Compute Cores)** (Impact: 29.0)
    * *Intent:* #endif #if !EMU8950_LINEAR
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 383 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 106`, `args: 89`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 434`, `dead_code: 30`, `planned_debt: 17`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 24`, `import: 7`
* *Defense:* `safety: 10`, `doc: 5`, `immutability_locks: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.691
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002928
  * `Imports (Out-Degree: 2):` assert.h, emu8950.h, gpio.h, math.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/hexen/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.101)
- **Top Global Matches:** file_cluster_8: 5.101, file_cluster_6: 12.398, file_cluster_4: 21.214
- **Magnitude:** 1880.6 | **LOC:** 2235 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 0.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.3%), Guard Balance (formerly Safety Score) (68.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 318.0)
    * *Intent:* */
  * `P_TouchSpecialThing` **(Many-Argument Workhorses)** (Impact: 174.9)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC P_TouchSpec...
  * `P_KillMobj` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* //--------------------------------------------------------------------------- // // PROC P_KillMobj ...
  * `TryPickupWeapon` **(Many-Argument Workhorses)** (Impact: 73.8)
    * *Intent:* //========================================================================== // // TryPickupWeapon /...
  * `TryPickupWeaponPiece` **(Many-Argument Workhorses)** (Impact: 57.3)
    * *Intent:* */ //========================================================================== // // TryPickupWeapo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 708
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 495`, `structural_boundaries: 282`, `args: 41`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 256`, `dead_code: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.894
  * `Choke Point (Betweenness):` 0.001997 | `Ripple Effect (Closeness):` 0.021842
  * `Imports (Out-Degree: 15):` h2def.h, i_system.h, m_misc.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/hexen/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.845)
- **Top Global Matches:** file_cluster_4: 5.845, file_cluster_6: 8.953, file_cluster_15: 12.465
- **Magnitude:** 1790.34 | **LOC:** 2192 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **14**; blast radius 0.817; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 264.4)
  * `G_Responder` **(Compute Cores)** (Impact: 68.3)
    * *Intent:* */
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 55.8)
    * *Intent:* //========================================================================== // // G_Ticker // //===...
  * `G_DoReborn` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* //========================================================================== // // G_DoReborn // //=...
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 334 instances
* *State Mutation (weighted view):* 1102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 208`, `args: 66`, `func_start: 38`
* *Risk/State:* `state_mutation: 434`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 58`, `import: 14`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.817
  * `Choke Point (Betweenness):` 0.004474 | `Ripple Effect (Closeness):` 0.018327
  * `Imports (Out-Degree: 27):` doomkeys.h, h2def.h, i_input.h, i_system.h, i_timer.h, i_video.h, m_argv.h, m_controls.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/strife/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.523)
- **Top Global Matches:** file_cluster_4: 5.523, file_cluster_6: 9.308, file_cluster_15: 12.156
- **Magnitude:** 1764.0 | **LOC:** 2468 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **38**; blast radius 0.658; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.9%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 176.0)
    * *Intent:* // // G_BuildTiccmd // Builds a ticcmd from all of the available inputs // or reads it from the demo...
  * `G_Responder` **(Compute Cores)** (Impact: 69.5)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* // // G_InitNew // // haleyjd 20100824: [STRIFE]: // * Added riftdest initialization // * Removed ep...
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 54.2)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_CheckSpot` **(Many-Argument Workhorses)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 326 instances
* *State Mutation (weighted view):* 1082
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 211`, `args: 54`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 430`, `dead_code: 14`, `fragile_debt: 4`, `unreferenced_by_name: 18`
* *Architecture:* `io: 3`, `api: 50`, `import: 39`
* *Defense:* `safety: 2`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.658
  * `Choke Point (Betweenness):` 0.000474 | `Ripple Effect (Closeness):` 0.01085
  * `Imports (Out-Degree: 45):` am_map.h, d_main.h, deh_main.h, deh_misc.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/hexen/sv_save.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.22)
- **Top Global Matches:** file_cluster_16: 6.22, file_cluster_15: 8.493, file_cluster_4: 8.742
- **Magnitude:** 1743.64 | **LOC:** 3458 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (96.3%), Complexity Load (formerly Cognitive Load) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SV_MapTeleport` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* //========================================================================== // // SV_MapTeleport //...
  * `StreamOutMobjSpecials` **(Compute Cores)** (Impact: 34.7)
  * `StreamInMobjSpecials` **(Stateful Encapsulated Methods)** (Impact: 21.8)
    * *Intent:* // // mobj_t //
  * `CopyFile` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* //========================================================================== // // CopyFile // // Th...
  * `StreamIn_player_t` **(I/O & Config Routines)** (Impact: 18.2)
    * *Intent:* // // player_t //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 332 instances
* *State Mutation (weighted view):* 1188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 228`, `args: 183`, `func_start: 89`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 524`, `dead_code: 225`, `unreferenced_by_name: 7`
* *Architecture:* `io: 13`, `api: 15`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.013628
  * `Imports (Out-Degree: 15):` h2def.h, i_swap.h, i_system.h, m_misc.h, p_local.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/hexen/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.63)
- **Top Global Matches:** file_cluster_6: 7.63, file_cluster_8: 9.351, file_cluster_4: 15.698
- **Magnitude:** 1734.8 | **LOC:** 2314 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 0.796; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 190.3)
    * *Intent:* //--------------------------------------------------------------------------- // // FUNC PIT_CheckTh...
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 99.8)
    * *Intent:* */
  * `P_FakeZMovement` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* //============================================================================= // // P_FakeZMovemen...
  * `PTR_ShootTraverse` **(Compute Cores)** (Impact: 40.4)
    * *Intent:* */
  * `PTR_UseTraverse` **(Compute Cores)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 267`, `args: 34`, `func_start: 31`
* *Risk/State:* `state_mutation: 374`, `dead_code: 5`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 32`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.018119
  * `Imports (Out-Degree: 11):` h2def.h, i_system.h, m_bbox.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/hexen/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.745)
- **Top Global Matches:** file_cluster_4: 5.745, file_cluster_15: 7.304, file_cluster_16: 8.209
- **Magnitude:** 1703.54 | **LOC:** 2482 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.765; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (65.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CHolySeekerMissile` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* //============================================================================ // // CHolySeekerMiss...
  * `P_CheckMana` **(Compute Cores)** (Impact: 29.4)
    * *Intent:* //--------------------------------------------------------------------------- // // FUNC P_CheckMana...
  * `A_ShedShard` **(Compute Cores)** (Impact: 29.3)
  * `A_FAxeAttack` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* //============================================================================ // // A_FAxeAttack //...
  * `A_LightningClip` **(Compute Cores)** (Impact: 22.5)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.765
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.017915
  * `Imports (Out-Degree: 9):` h2def.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/heretic/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.18)
- **Top Global Matches:** file_cluster_4: 5.18, file_cluster_6: 10.296, file_cluster_15: 11.135
- **Magnitude:** 1693.56 | **LOC:** 2075 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.4%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Many-Argument Workhorses)** (Impact: 200.5)
  * `G_Responder` **(Compute Cores)** (Impact: 68.3)
    * *Intent:* */
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 52.2)
    * *Intent:* */
  * `G_InitNew` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `G_RecordDemo` **(Many-Argument Workhorses)** (Impact: 18.6)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 327 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 194`, `args: 54`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 414`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 50`, `import: 16`
* *Defense:* `doc: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` deh_str.h, doomdef.h, doomkeys.h, i_input.h, i_system.h, i_timer.h, m_argv.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_15: 6.134, file_cluster_4: 7.05, file_cluster_16: 7.578
- **Magnitude:** 1693.14 | **LOC:** 2716 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.713; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_NewChaseDir` **(Compute Cores)** (Impact: 55.2)
  * `A_Chase` **(Compute Cores)** (Impact: 54.3)
    * *Intent:* */
  * `P_LookForPlayers` **(Compute Cores)** (Impact: 32.4)
    * *Intent:* */
  * `A_NoBlocking` **(Compute Cores)** (Impact: 23.3)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC A_NoBlocki...
  * `P_RecursiveSound` **(Compute Cores)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 251 instances
* *State Mutation (weighted view):* 866
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 261`, `args: 108`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 364`, `dead_code: 6`, `unreferenced_by_name: 80`
* *Architecture:* `api: 99`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.713
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.004685
  * `Imports (Out-Degree: 8):` doomdef.h, i_system.h, i_timer.h, m_random.h, p_local.h, s_sound.h, stdlib.h, v_video.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/hexen/po_man.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.411)
- **Top Global Matches:** file_cluster_6: 8.411, file_cluster_8: 9.523, file_cluster_4: 16.432
- **Magnitude:** 1592.7 | **LOC:** 1503 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 0.789; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SpawnPolyobj` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* //========================================================================== // // SpawnPolyobj // /...
  * `EV_RotatePoly` **(Many-Argument Workhorses)** (Impact: 46.9)
    * *Intent:* //========================================================================== // // EV_RotatePoly // ...
  * `T_PolyDoor` **(Compute Cores)** (Impact: 42.7)
    * *Intent:* //========================================================================== // // T_PolyDoor // //=...
  * `CheckMobjBlocking` **(Many-Argument Workhorses)** (Impact: 35.9)
    * *Intent:* //========================================================================== // // CheckMobjBlocking...
  * `PO_MovePolyobj` **(Many-Argument Workhorses)** (Impact: 34.8)
    * *Intent:* //========================================================================== // // PO_MovePolyobj //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 332 instances
* *State Mutation (weighted view):* 1061
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 87`, `args: 42`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 397`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.789
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.020707
  * `Imports (Out-Degree: 12):` h2def.h, i_swap.h, i_system.h, m_bbox.h, p_local.h, r_local.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/hexen/p_user.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.611)
- **Top Global Matches:** file_cluster_8: 7.611, file_cluster_3: 16.545, file_cluster_6: 19.855
- **Magnitude:** 1541.72 | **LOC:** 1646 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.743; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_PlayerThink` **(Compute Cores)** (Impact: 166.4)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_PlayerTh...
  * `P_UseArtifact` **(Many-Argument Workhorses)** (Impact: 109.7)
    * *Intent:* //========================================================================== // // P_UseArtifact // ...
  * `P_MovePlayer` **(Compute Cores)** (Impact: 55.3)
    * *Intent:* */
  * `P_DeathThink` **(Compute Cores)** (Impact: 52.6)
    * *Intent:* //========================================================================== // // P_DeathThink // /...
  * `P_BlastMobj` **(Many-Argument Workhorses)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 834
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 123`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 300`, `dead_code: 7`, `unreferenced_by_name: 4`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.743
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.018327
  * `Imports (Out-Degree: 14):` h2def.h, i_system.h, m_random.h, p_local.h, s_sound.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/hexen/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.966)
- **Top Global Matches:** file_cluster_6: 5.966, file_cluster_4: 12.53, file_cluster_8: 12.533
- **Magnitude:** 1501.18 | **LOC:** 1552 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 97.3)
  * `AM_clipMline` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* // Based on Cohen-Sutherland clipping algorithm but with a slightly // faster reject and precalculat...
  * `DrawWuLine` **(Many-Argument Workhorses)** (Impact: 54.8)
  * `AM_drawFline` **(Compute Cores)** (Impact: 49.1)
    * *Intent:* #undef DOOUTCODE // Classic Bresenham w/ whatever optimizations I need for speed
  * `PUTDOT` **(Stateful Encapsulated Methods)** (Impact: 37.9)
    * *Intent:* /* Wu antialiased line drawer. * (X0,Y0),(X1,Y1) = line to draw * BaseColor = color # of first color...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 297 instances
* *State Mutation (weighted view):* 946
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 113`, `args: 62`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 352`, `dead_code: 20`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 33`, `import: 12`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` am_data.h, am_map.h, doomkeys.h, h2def.h, i_swap.h, i_timer.h, i_video.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.067)
- **Top Global Matches:** file_cluster_6: 5.067, file_cluster_4: 11.772, file_cluster_8: 12.789
- **Magnitude:** 1461.9 | **LOC:** 1628 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 110.0)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_XYMoveme...
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 73.6)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_SpawnMap...
  * `P_ZMovement` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* */
  * `P_MobjThinker` **(Compute Cores)** (Impact: 47.5)
    * *Intent:* //---------------------------------------------------------------------------- // // PROC P_MobjThin...
  * `P_SpawnMobj` **(Many-Argument Workhorses)** (Impact: 35.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 255 instances
* *State Mutation (weighted view):* 825
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 113`, `args: 35`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 315`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 11`
* *Architecture:* `api: 31`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` doomdef.h, i_system.h, m_random.h, p_local.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/heretic/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.799)
- **Top Global Matches:** file_cluster_6: 5.799, file_cluster_4: 12.451, file_cluster_8: 12.471
- **Magnitude:** 1458.14 | **LOC:** 1543 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 96.5)
  * `AM_clipMline` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* // Based on Cohen-Sutherland clipping algorithm but with a slightly // faster reject and precalculat...
  * `DrawWuLine` **(Many-Argument Workhorses)** (Impact: 54.8)
  * `AM_drawFline` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* #undef DOOUTCODE // Classic Bresenham w/ whatever optimizations I need for speed
  * `PUTDOT` **(Stateful Encapsulated Methods)** (Impact: 37.9)
    * *Intent:* /* Wu antialiased line drawer. * (X0,Y0),(X1,Y1) = line to draw * BaseColor = color # of first color...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 286 instances
* *State Mutation (weighted view):* 904
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 106`, `args: 61`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 332`, `dead_code: 21`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` am_data.h, am_map.h, deh_str.h, doomdef.h, doomkeys.h, i_timer.h, i_video.h, m_controls.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.644)
- **Top Global Matches:** file_cluster_4: 6.644, file_cluster_15: 8.41, file_cluster_16: 8.631
- **Magnitude:** 1368.46 | **LOC:** 2634 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M_Responder` **(Compute Cores)** (Impact: 236.9)
    * *Intent:* // // CONTROL PANEL // // // M_Responder //
  * `M_Drawer` **(I/O & Config Routines)** (Impact: 25.5)
    * *Intent:* // // M_Drawer // Called after the view has been rendered, // but before it has been blitted. //
  * `M_DrawNetFoyer` **(I/O & Config Routines)** (Impact: 19.2)
  * `M_WriteText` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* // // Write a string using the hu_font //
  * `M_Init` **(I/O & Config Routines)** (Impact: 11.2)
    * *Intent:* // // M_Init //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 217 instances
* *State Mutation (weighted view):* 690
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 319`, `args: 203`, `func_start: 67`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 256`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 69`, `import: 29`
* *Defense:* `safety: 4`, `doc: 1`, `test: 1`, `immutability_locks: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` ctype.h, d_main.h, deh_main.h, doomdef.h, doomkeys.h, doomstat.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/doom/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.61)
- **Top Global Matches:** file_cluster_4: 6.61, file_cluster_16: 8.36, file_cluster_12: 9.82
- **Magnitude:** 1357.26 | **LOC:** 2825 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **18**; blast radius 0.672; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (95.8%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveg_write_mobj_t` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `saveg_read_mobj_t` **(I/O & Config Routines)** (Impact: 35.5)
    * *Intent:* // // mobj_t //
  * `P_SaveGameWriteFlashSlot` **(Many-Argument Workhorses)** (Impact: 33.2)
  * `P_UnArchiveWorld` **(I/O & Config Routines)** (Impact: 24.8)
    * *Intent:* // // P_UnArchiveWorld //
  * `P_SaveGameGetExistingFlashSlotAddresses` **(Compute Cores)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 240 instances
* *State Mutation (weighted view):* 843
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 161`, `args: 70`, `func_start: 68`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 363`, `dead_code: 180`, `planned_debt: 6`, `unreferenced_by_name: 15`
* *Architecture:* `io: 2`, `api: 23`, `import: 18`
* *Defense:* `safety: 9`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.672
  * `Choke Point (Betweenness):` 0.001283 | `Ripple Effect (Closeness):` 0.006589
  * `Imports (Out-Degree: 26):` deh_main.h, doomstat.h, dstrings.h, g_game.h, address_mapped.h, sync.h, timer.h, i_system.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `opl/opl3.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.239)
- **Top Global Matches:** file_cluster_6: 6.239, file_cluster_4: 7.544, file_cluster_16: 14.712
- **Magnitude:** 1356.4 | **LOC:** 1378 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.691; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.4%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OPL3_WriteReg` **(Many-Argument Workhorses)** (Impact: 76.9)
  * `OPL3_EnvelopeCalc` **(Compute Cores)** (Impact: 75.2)
  * `OPL3_Generate` **(Many-Argument Workhorses)** (Impact: 48.1)
  * `OPL3_ChannelUpdateRhythm` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `OPL3_ChannelSetupAlg` **(Compute Cores)** (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 84`, `args: 37`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 321`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.691
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002928
  * `Imports (Out-Degree: 1):` opl3.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.675)
- **Top Global Matches:** file_cluster_12: 7.675, file_cluster_4: 8.298, file_cluster_15: 9.56
- **Magnitude:** 1352.48 | **LOC:** 1290 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **41** in-repo importer(s); it depends on **18**; blast radius 1.81; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.6%), Guard Balance (formerly Safety Score) (87.5%), Debt Markers (formerly Tech Debt) (82.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `V_DrawPatchList` **(Compute Cores)** (Impact: 93.8)
    * *Intent:* #pragma GCC push_options #if PICO_ON_DEVICE #pragma GCC optimize("O3") #endif
  * `WritePNGfile` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `V_DrawPatchN` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `V_CopyRect` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* #endif // // V_CopyRect //
  * `V_DrawMouseSpeedBox` **(Compute Cores)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 286 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 895
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 63`, `args: 37`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 323`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `io: 1`, `api: 33`, `import: 18`
* *Defense:* `safety: 13`, `immutability_locks: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.81
  * `Choke Point (Betweenness):` 0.010162 | `Ripple Effect (Closeness):` 0.06702
  * `Imports (Out-Degree: 20):` config.h, deh_str.h, r_data.h, doomtype.h, i_input.h, i_swap.h, i_system.h, i_video.h...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/whd_gen/huff_sink.h` (CPP) | Magnitude: 64.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 90, structural_boundaries: 52, args: 19, pointers: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/hexen/st_start.c` (C) | Magnitude: 59.9 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 22, args: 16, core_var_decl: 15
- `opl/examples/droplay.c` (C) | Magnitude: 102.34 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 105, branch: 19, structural_boundaries: 18, state_mutation: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/doom/d_think.h` (C) | Magnitude: 17.3 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 24, macros: 13, pointers: 12
- `src/heretic/deh_ammo.c` (C) | Magnitude: 54.14 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 51, pointers: 13, branch: 11, structural_boundaries: 9
- `src/doom/p_mobj.h` (C) | Magnitude: 37.48 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 85, macros: 78, pointers: 43, reflection_metaprogramming: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/v_diskicon.h` (C) | Magnitude: 10.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, args: 8, macros: 7, func_start: 4
- `src/i_input.c` (C) | Magnitude: 237.54 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 246, branch: 61, structural_boundaries: 47, state_mutation: 37
- `src/doom/deh_bexstr.c` (C) | Magnitude: 28.38 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 311, pointers: 12, structural_boundaries: 7, import: 6
- `textscreen/txt_gui.c` (C) | Magnitude: 396.36 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 278, state_mutation: 76, pointers: 66, branch: 56
- `src/pico/i_glob.c` (C) | Magnitude: 253.2 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 218, pointers: 93, state_mutation: 53, structural_boundaries: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/m_controls.h` (C) | Magnitude: 136.48 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 119, globals: 110, structural_boundaries: 17, args: 9
- `src/strife/f_wipe.h` (C) | Magnitude: 18.58 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, args: 3, api: 3, macros: 2
- `src/m_argv.h` (C) | Magnitude: 12.56 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 7, api: 7, structural_boundaries: 6, immutability_locks: 6
- `src/strife/doomstat.h` (C) | Magnitude: 86.6 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 70, globals: 70, import: 5, macros: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/strife/wi_stuff.h` (C) | Magnitude: 15.32 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 4, core_var_decl: 1, design_pascal_case: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `textscreen/txt_sdl.c` (C) | Magnitude: 558.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 522, pointers: 129, branch: 124, state_mutation: 98
- `textscreen/txt_scrollpane.c` (C) | Magnitude: 397.68 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 360, pointers: 178, branch: 89, state_mutation: 67
- `src/m_config.c` (C) | Magnitude: 419.26 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 607, pointers: 152, state_mutation: 82, branch: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/pico/i_video.c` (C) | Magnitude: 1179.0 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 825, pointers: 320, state_mutation: 297, branch: 164

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pkg/osx/GNUmakefile` (MAKEFILE) | Magnitude: 14.8 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 46, io: 23, core_var_decl: 14, design_upper_case: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/d_loop.c` -> **Severity: 1.979** (Bridge: 0.0198 * Flux: 100.0%)
- `src/doom/r_main.c` -> **Severity: 1.439** (Bridge: 0.0144 * Flux: 99.9999%)
- `src/net_gui.c` -> **Severity: 1.26** (Bridge: 0.0127 * Flux: 99.4218%)
- `src/v_video.c` -> **Severity: 1.016** (Bridge: 0.0102 * Flux: 100.0%)
- `src/doom/r_state.h` -> **Severity: 0.812** (Bridge: 0.0128 * Flux: 63.2637%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/doomtype.h` -> **Severity: 17.241** (Embedded: 0.3505 * Error Risk: 49.1849%)
- `src/z_zone.c` -> **Severity: 15.388** (Embedded: 0.2018 * Error Risk: 76.2407%)
- `src/z_native.c` -> **Severity: 14.494** (Embedded: 0.201 * Error Risk: 72.1149%)
- `src/m_misc.c` -> **Severity: 11.992** (Embedded: 0.1718 * Error Risk: 69.7855%)
- `src/d_event.h` -> **Severity: 9.58** (Embedded: 0.1863 * Error Risk: 51.4282%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/doomtype.h` -> **Severity: 11043.5** (Blast Radius: 110.435 * Doc Risk: 100.0%)
- `src/m_fixed.h` -> **Severity: 932.0** (Blast Radius: 9.32 * Doc Risk: 100.0%)
- `src/z_zone.c` -> **Severity: 623.2** (Blast Radius: 6.232 * Doc Risk: 100.0%)
- `src/z_native.c` -> **Severity: 620.8** (Blast Radius: 6.208 * Doc Risk: 100.0%)
- `src/m_misc.c` -> **Severity: 579.6** (Blast Radius: 5.796 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 747 literal sites + 39 sites through wrappers = 786
- **`memory_alloc`:** 336 literal sites + 408 sites through wrappers = 744
- **`panics_and_aborts`:** 127 literal sites + 6 sites through wrappers = 133

- `AddKeyControl` (function, memory_alloc, via TXT_NewKeyInput): 95 call sites in 1 files -- `src/setup/keyboard.c`
- `lodepng_malloc` (function, memory_alloc, primitive): 43 call sites in 1 files -- `src/whd_gen/lodepng.cpp`
- `TXT_NewStrut` (function, memory_alloc, primitive): 28 call sites in 12 files -- `textscreen/txt_strut.c`
- `TXT_NewButton2` (function, memory_alloc, via TXT_NewButton): 27 call sites in 7 files -- `textscreen/txt_button.c`
- `ST_Message` (function, debug_prints, primitive): 23 call sites in 3 files -- `src/hexen/st_start.c`
- `TXT_NewButton` (function, memory_alloc, primitive): 18 call sites in 5 files -- `textscreen/txt_button.c`
- `TXT_NewWindowAction` (function, memory_alloc, primitive): 17 call sites in 8 files -- `textscreen/txt_window_action.c`
- `TXT_NewTable` (function, memory_alloc, primitive): 16 call sites in 8 files -- `textscreen/txt_table.c`
- `lodepng_realloc` (function, memory_alloc, primitive): 13 call sites in 1 files -- `src/whd_gen/lodepng.cpp`
- `TXT_Shutdown` (function, memory_alloc, primitive): 12 call sites in 8 files -- `textscreen/txt_sdl.c`
- `AddMouseControl` (function, memory_alloc, via TXT_NewMouseInput): 10 call sites in 1 files -- `src/setup/mouse.c`
- `AddNumberButton` (function, memory_alloc, primitive): 10 call sites in 1 files -- `textscreen/examples/calculator.c`
*(+52 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 19967 call pairs -- scoped 27.3%, unique 24.5%, ambiguous 19.4%, external 28.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 17747 | 25.0% | 27.1% | 21.2% | 26.7% |
| cpp | 1843 | 50.6% | 4.0% | 5.4% | 40.0% |
| python | 184 | 23.9% | 0.0% | 0.0% | 76.1% |
| objective-c | 178 | 18.0% | 7.9% | 6.2% | 68.0% |
| shell | 14 | 21.4% | 0.0% | 0.0% | 78.6% |
| m4 | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
