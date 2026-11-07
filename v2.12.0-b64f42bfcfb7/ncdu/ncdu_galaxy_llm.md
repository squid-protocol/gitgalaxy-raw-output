# ARCHITECTURAL_BRIEF: ncdu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rofl0r/ncdu.git` |
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
- **Scope:** 33 analyzed artifact(s), 4085 LOC.
- **Load-bearing artifact:** `src/global.h` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/global.h` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/util.c` at magnitude 583.46 (structural weight, not risk).
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
| Total Artifacts | 36 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 4085 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1959 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5914 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 69.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0887 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 28 | 3757 | 84.8% |
| PLAINTEXT | 2 | 0 | 6.1% |
| MARKDOWN | 1 | 0 | 3.0% |
| M4 | 1 | 55 | 3.0% |
| PERL | 1 | 273 | 3.0% |

## 4.1 SOURCE ENCODINGS
All 33 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Large Core Modules (3) 24%, Declarative / Non-Code 21%, Compute Cores Files 12%, Encapsulated Accessors Files 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 30 | 90.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 9.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.am`: 1x Excluded (Unsupported Extension: '.am')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.8 | 43.9 | 62.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.1 | 45.7 | 64.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.7 | 28.3 | 13.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 36.0 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.7 | 22.4 | 5.6 | 40.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 56.9 | 100.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 39 | 9 | 4 | `src/path.c` |
| cleanup | 26 | 9 | 3 | `src/path.c` |
| guards | 223 | 21 | 20 | `src/util.c` |
| danger | 76 | 16 | 8 | `src/main.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 172 | 28 | 15 | `src/util.h` |
| io | 26 | 8 | 2 | `doc/ncdu.pod` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 3 | 0 | `deps/yopt.h` |
| time | 11 | 3 | 0 | `src/browser.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 4 | 2 | 0 | `doc/ncdu.pod` |
| tests | 0 | 0 | 0 | - |
| docs | 8 | 2 | 0 | `deps/khashl.h` |
| debt | 49 | 11 | 2 | `src/main.c` |
| mutation | 1241 | 20 | 106 | `src/dirlist.c` |
| dead_code | 50 | 15 | 4 | `src/util.c` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `src/main.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/ncdu.pod` (Hits: 14)
- `src/exclude.c` (Hits: 3)
- `configure.ac` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **global.h** (`src/global.h`) — 21 inbound connections
2. **util.c** (`src/util.c`) — 14 inbound connections
3. **browser.c** (`src/browser.c`) — 6 inbound connections
4. **util.h** (`src/util.h`) — 6 inbound connections
5. **main.c** (`src/main.c`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **global.h** (`src/global.h`) — 19 outbound dependencies
2. **dir_scan.c** (`src/dir_scan.c`) — 11 outbound dependencies
3. **main.c** (`src/main.c`) — 8 outbound dependencies
4. **shell.c** (`src/shell.c`) — 8 outbound dependencies
5. **path.c** (`src/path.c`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `browse_key` **(Compute Cores)** (@ `src/browser.c`) -> Impact: **149.8** | LOC: 225
- `argv_parse` **(Many-Argument Workhorses)** (@ `src/main.c`) -> Impact: **83.8** | LOC: 151
  * *Intent:* /* parse command line */
- `dir_scan_item` **(C Struct Operations)** (@ `src/dir_scan.c`) -> Impact: **53.4** | LOC: 78
  * *Intent:* /* Scans and adds a single item. Recurses into dir_walk() again if this is a * directory. Assumes we're chdir'ed in the directory in which this item *...
- `yopt_next` **(Compute Cores)** (@ `deps/yopt.h`) -> Impact: **48.0** | LOC: 60
  * *Intent:* /* Return values: * 0 -> Non-option argument, val is its value * -1 -> Last argument has been processed * -2 -> Error, val will contain the error mess...
- `formatsize` **(Compute Cores)** (@ `src/util.c`) -> Impact: **47.9** | LOC: 22
- `iteminfo` **(Compute Cores)** (@ `src/dir_import.c`) -> Impact: **46.5** | LOC: 89
  * *Intent:* /* Reads a JSON object representing a struct dir/dir_ext item. Writes to * ctx->buf_dir, ctx->buf_ext and ctx->buf_name. */
- `delete_key` **(Compute Cores)** (@ `src/delete.c`) -> Impact: **45.2** | LOC: 56
- `path_real_rec` **(Many-Argument Workhorses)** (@ `src/path.c`) -> Impact: **42.0** | LOC: 78
  * *Intent:* /* NOTE: cwd and the memory cur points to are unreliable after calling this * function. * TODO: This code is rather fragile and inefficient. A rewrite...
- `dirlist_cmp` **(Compute Cores)** (@ `src/dirlist.c`) -> Impact: **38.8** | LOC: 48
- `browse_draw_graph` **(Stateful Encapsulated Methods)** (@ `src/browser.c`) -> Impact: **38.2** | LOC: 37

*Function archetypes referenced above:*
  * **C Struct Operations**: operates on C structs and pointers (data-structure logic)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 26 | 4190.02 | 44.84% | 31.81% |
| `deps` | 2 | 282.82 | 66.86% | 5.36% |
| `doc` | 1 | 33.46 | 16.47% | 12.45% |
| `__monolith__` | 4 | 21.88 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/util.c` -> **98.7126%** Exposure
- `src/quit.c` -> **97.0688%** Exposure
- `src/exclude.c` -> **91.5138%** Exposure
- `src/dir_common.c` -> **83.7809%** Exposure
- `src/shell.c` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `deps/yopt.h` -> **100.0%** Exposure
- `src/browser.c` -> **100.0%** Exposure
- `src/delete.c` -> **100.0%** Exposure
- `src/dir_mem.c` -> **100.0%** Exposure
- `src/dir_scan.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/util.c` -> **13** Orphaned Functions | **0** Duplicates
- `src/dir_common.c` -> **7** Orphaned Functions | **0** Duplicates
- `src/delete.c` -> **4** Orphaned Functions | **0** Duplicates
- `src/dirlist.c` -> **4** Orphaned Functions | **0** Duplicates
- `src/exclude.c` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `117` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.301)
- **Top Global Matches:** file_cluster_4: 5.301, file_cluster_6: 9.372, file_cluster_12: 12.142
- **Magnitude:** 583.46 | **LOC:** 435 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **7**; blast radius 56.232; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.7%), Guard Balance (formerly Safety Score) (89.0%), Complexity Load (formerly Cognitive Load) (81.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatsize` **(Compute Cores)** (Impact: 47.9)
  * `fmtmode` **(Stateful Encapsulated Methods)** (Impact: 25.1)
  * `freedir_hlnk` **(C Struct Operations)** (Impact: 20.0)
    * *Intent:* /* removes item from the hlnk circular linked list and size counts of the parents */
  * `getpath` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `freedir` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 115 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 44`, `args: 30`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 118`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 19`, `import: 7`
* *Defense:* `safety: 6`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.232
  * `Choke Point (Betweenness):` 0.100588 | `Ripple Effect (Closeness):` 0.4375
  * `Imports (Out-Degree: 2):` locale.h, ncurses.h, stdarg.h, stdlib.h, string.h, unistd.h, util.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/browser.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.033)
- **Top Global Matches:** file_cluster_8: 8.033, file_cluster_6: 17.956, file_cluster_3: 20.234
- **Magnitude:** 579.28 | **LOC:** 568 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 26.948; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `browse_key` **(Compute Cores)** (Impact: 149.8)
  * `browse_draw_graph` **(Stateful Encapsulated Methods)** (Impact: 38.2)
  * `browse_draw_flag` **(Stateful Encapsulated Methods)** (Impact: 25.1)
  * `browse_draw_info` **(Compute Cores)** (Impact: 23.4)
  * `browse_draw_items` **(C Struct Operations)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 72`, `args: 39`, `func_start: 9`, `class_start: 10`
* *Risk/State:* `state_mutation: 91`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.948
  * `Choke Point (Betweenness):` 0.042288 | `Ripple Effect (Closeness):` 0.226852
  * `Imports (Out-Degree: 10):` global.h, ncurses.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/dirlist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.137)
- **Top Global Matches:** file_cluster_8: 8.137, file_cluster_6: 10.068, file_cluster_4: 18.354
- **Magnitude:** 496.58 | **LOC:** 399 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 14.891; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.1%), Complexity Load (formerly Cognitive Load) (84.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dirlist_cmp` **(Compute Cores)** (Impact: 38.8)
  * `dirlist_sort` **(Compute Cores)** (Impact: 29.2)
  * `dirlist_top` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* * -2 = selected = first item in the list (faster version of '1') * -3 = top should be considered as ...
  * `dirlist_get` **(Compute Cores)** (Impact: 15.9)
  * `dirlist_set_sort` **(Compute Cores)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 51`, `args: 14`, `func_start: 12`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 103`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.891
  * `Choke Point (Betweenness):` 0.000252 | `Ripple Effect (Closeness):` 0.170139
  * `Imports (Out-Degree: 3):` global.h, stdlib.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/dir_import.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.102)
- **Top Global Matches:** file_cluster_6: 6.102, file_cluster_4: 10.8, file_cluster_8: 15.026
- **Magnitude:** 423.34 | **LOC:** 616 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 11.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iteminfo` **(Compute Cores)** (Impact: 46.5)
    * *Intent:* /* Reads a JSON object representing a struct dir/dir_ext item. Writes to * ctx->buf_dir, ctx->buf_ex...
  * `rstring_esc` **(Stateful Encapsulated Methods)** (Impact: 33.1)
  * `rval` **(Compute Cores)** (Impact: 21.5)
    * *Intent:* /* (Recursively) parse and consume any JSON value. The result is discarded. */
  * `fill` **(Stateful Encapsulated Methods)** (Impact: 20.3)
    * *Intent:* /* Fills readbuf with data from the stream. *buf will have at least n (< * READ_BUF_SIZE) bytes avai...
  * `item` **(Stateful Encapsulated Methods)** (Impact: 17.8)
    * *Intent:* /* Recursively reads a file or directory item */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 58 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 78`, `args: 23`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165541
  * `Imports (Out-Degree: 4):` errno.h, global.h, limits.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/dir_scan.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.444)
- **Top Global Matches:** file_cluster_8: 8.444, file_cluster_6: 10.275, file_cluster_4: 18.451
- **Magnitude:** 328.18 | **LOC:** 406 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_scan_item` **(C Struct Operations)** (Impact: 53.4)
    * *Intent:* /* Scans and adds a single item. Recurses into dir_walk() again if this is a * directory. Assumes we...
  * `process` **(Compute Cores)** (Impact: 22.5)
  * `dir_scan_recurse` **(Compute Cores)** (Impact: 22.3)
    * *Intent:* /* Tries to recurse into the current directory item (buf_dir is assumed to be the current dir) */
  * `is_kernfs` **(Stateful Encapsulated Methods)** (Impact: 22.0)
    * *Intent:* #if HAVE_LINUX_MAGIC_H && HAVE_SYS_STATFS_H && HAVE_STATFS int exclude_kernfs; /* Exclude Linux pseu...
  * `dir_read` **(Stateful Encapsulated Methods)** (Impact: 17.3)
    * *Intent:* /* Reads all filenames in the currently chdir'ed directory and stores it as a * nul-separated list o...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 33`, `args: 18`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.012937 | `Ripple Effect (Closeness):` 0.197581
  * `Imports (Out-Degree: 6):` dirent.h, errno.h, global.h, magic.h, stdlib.h, string.h, attr.h, stat.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.799)
- **Top Global Matches:** file_cluster_8: 7.799, file_cluster_6: 17.953, file_cluster_3: 20.081
- **Magnitude:** 278.28 | **LOC:** 360 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 38.869; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `argv_parse` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /* parse command line */
  * `input_handle` **(Compute Cores)** (Impact: 30.4)
    * *Intent:* /* wait: * -1: non-blocking, always draw screen * 0: blocking wait for input and always draw screen ...
  * `main` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* /* main program */
  * `init_nc` **(I/O & Config Routines)** (Impact: 11.2)
    * *Intent:* /* Initializes ncurses only when not done yet. */
  * `screen_draw` **(Stateful Encapsulated Methods)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 46`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 49`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.869
  * `Choke Point (Betweenness):` 0.140289 | `Ripple Effect (Closeness):` 0.255208
  * `Imports (Out-Degree: 14):` errno.h, global.h, stdio.h, stdlib.h, string.h, time.h, unistd.h, yopt.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/path.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.072)
- **Top Global Matches:** file_cluster_6: 10.072, file_cluster_8: 14.241, file_cluster_4: 15.833
- **Magnitude:** 260.46 | **LOC:** 247 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 12.601; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.9%), Complexity Load (formerly Cognitive Load) (86.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `path_real_rec` **(Many-Argument Workhorses)** (Impact: 42.0)
    * *Intent:* /* NOTE: cwd and the memory cur points to are unreliable after calling this * function. * TODO: This...
  * `path_split` **(Stateful Encapsulated Methods)** (Impact: 22.7)
    * *Intent:* cur is modified, and res has to be free()d after use */
  * `path_absolute` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* /* copies path and prepends cwd if needed, to ensure an absolute path return value has to be free()'...
  * `path_chdir` **(Compute Cores)** (Impact: 8.1)
  * `path_real` **(Compute Cores)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 55 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 56`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `immutability_locks: 3`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153125
  * `Imports (Out-Degree: 2):` errno.h, global.h, limits.h, stdio.h, stdlib.h, string.h, unistd.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/dir_mem.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.774)
- **Top Global Matches:** file_cluster_6: 5.774, file_cluster_4: 10.626, file_cluster_8: 14.959
- **Magnitude:** 226.26 | **LOC:** 216 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `item` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `hlink_check` **(C Struct Operations)** (Impact: 18.5)
    * *Intent:* /* checks an individual file for hard links and updates its cicrular linked * list, also updates the...
  * `final` **(Stateful Encapsulated Methods)** (Impact: 14.3)
  * `item_add` **(Stateful Encapsulated Methods)** (Impact: 7.9)
    * *Intent:* /* Add item to the correct place in the memory structure */
  * `hlink_init` **(C Struct Operations)** (Impact: 4.8)
    * *Intent:* /* recursively checks a dir structure for hard links and fills the lookup array */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 25`, `args: 8`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.016835 | `Ripple Effect (Closeness):` 0.197581
  * `Imports (Out-Degree: 6):` global.h, khashl.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/delete.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.285)
- **Top Global Matches:** file_cluster_8: 8.285, file_cluster_6: 9.817, file_cluster_4: 17.932
- **Magnitude:** 210.06 | **LOC:** 254 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `delete_key` **(Compute Cores)** (Impact: 45.2)
  * `delete_dir` **(Compute Cores)** (Impact: 27.6)
  * `delete_process` **(I/O & Config Routines)** (Impact: 10.6)
  * `delete_draw_confirm` **(Stateful Encapsulated Methods)** (Impact: 10.2)
  * `delete_draw` **(Compute Cores)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 37`, `args: 20`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.009913 | `Ripple Effect (Closeness):` 0.197581
  * `Imports (Out-Degree: 6):` errno.h, global.h, string.h, unistd.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `deps/yopt.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.838)
- **Top Global Matches:** file_cluster_8: 8.838, file_cluster_6: 10.344, file_cluster_4: 18.278
- **Magnitude:** 174.46 | **LOC:** 199 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 11.152; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yopt_next` **(Compute Cores)** (Impact: 48.0)
    * *Intent:* /* Return values: * 0 -> Non-option argument, val is its value * -1 -> Last argument has been proces...
  * `_yopt_find` **(Stateful Encapsulated Methods)** (Impact: 27.1)
  * `yopt_init` **(Encapsulated Accessors)** (Impact: 2.6)
    * *Intent:* /* opts must be an array of options, terminated with an option with val=0 */
  * `_yopt_err` **(Encapsulated Accessors)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.180288
  * `Imports (Out-Degree: 0):` stdarg.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/dir_common.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.313)
- **Top Global Matches:** file_cluster_12: 7.313, file_cluster_7: 9.375, file_cluster_16: 9.814
- **Magnitude:** 152.58 | **LOC:** 233 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 15.426; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_key` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /* This function can't be called unless dir_ui == 2 * (Doesn't really matter either way). */
  * `draw_progress` **(Stateful Encapsulated Methods)** (Impact: 15.8)
  * `dir_draw` **(I/O & Config Routines)** (Impact: 13.4)
  * `curpath_resize` **(Encapsulated Accessors)** (Impact: 6.0)
    * *Intent:* char *dir_fatalerr; /* Error message on a fatal error. (NULL if there was no fatal error) */ int dir...
  * `dir_curpath_leave` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* /* removes last component from dir_curpath */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 24`, `args: 20`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 23`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.426
  * `Choke Point (Betweenness):` 0.001512 | `Ripple Effect (Closeness):` 0.185606
  * `Imports (Out-Degree: 3):` global.h, stdarg.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/help.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.158)
- **Top Global Matches:** file_cluster_8: 7.158, file_cluster_6: 17.53, file_cluster_3: 19.981
- **Magnitude:** 128.86 | **LOC:** 213 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (68.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `help_key` **(Compute Cores)** (Impact: 35.8)
  * `help_draw` **(I/O & Config Routines)** (Impact: 13.6)
  * `help_init` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 11`, `args: 12`, `func_start: 3`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.197581
  * `Imports (Out-Degree: 3):` global.h, ncurses.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/dir_export.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.569)
- **Top Global Matches:** file_cluster_6: 5.569, file_cluster_4: 10.42, file_cluster_8: 14.845
- **Magnitude:** 127.2 | **LOC:** 195 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 11.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.2%), Guard Balance (formerly Safety Score) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `output_info` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `output_string` **(Stateful Encapsulated Methods)** (Impact: 20.7)
  * `item` **(Stateful Encapsulated Methods)** (Impact: 15.6)
    * *Intent:* /* Note on error handling: For convenience, we just keep writing to *stream * without checking the r...
  * `dir_export_init` **(Compute Cores)** (Impact: 6.4)
  * `output_int` **(Stateful Encapsulated Methods)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 25`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 13`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.170139
  * `Imports (Out-Degree: 2):` global.h, stdio.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `deps/khashl.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_12: 7.466, file_cluster_7: 8.605, file_cluster_16: 8.677
- **Magnitude:** 108.36 | **LOC:** 350 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.696; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (60.6%), Connectivity (formerly Api Exposure) (32.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kh_hash_str` **(Encapsulated Accessors)** (Impact: 4.5)
  * `kh_hash_uint32` **(Encapsulated Accessors)** (Impact: 1.9)
    * *Intent:* #define kh_capacity(h) ((h)->keys? 1U<<(h)->bits : 0U) #define kh_end(h) kh_capacity(h) #define kh_k...
  * `kh_hash_uint64` **(Encapsulated Accessors)** (Impact: 1.9)
  * `__kh_h2b` **(Encapsulated Accessors)** (Impact: 1.8)
    * *Intent:* #ifndef kfree #define kfree(P) free(P) #endif /**************************** * Simple private functio...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 78`, `args: 79`, `func_start: 4`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 72`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 1`, `doc: 7`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.152853
  * `Imports (Out-Degree: 0):` limits.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/exclude.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.079)
- **Top Global Matches:** file_cluster_12: 9.079, file_cluster_9: 9.122, file_cluster_16: 10.7
- **Magnitude:** 106.84 | **LOC:** 139 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 13.056; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.5%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exclude_addfile` **(Compute Cores)** (Impact: 10.9)
  * `exclude_match` **(Compute Cores)** (Impact: 10.5)
  * `has_cachedir_tag` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* /* * Exclusion of directories that contain only cached information. * See http://www.brynosaurus.com...
  * `exclude_add` **(Type Conversions)** (Impact: 3.4)
  * `exclude_clear` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 21 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 16`, `args: 4`, `func_start: 5`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 21`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 5`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.180147
  * `Imports (Out-Degree: 2):` fnmatch.h, global.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/dir.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.694)
- **Top Global Matches:** file_cluster_17: 5.694, file_cluster_2: 7.915, file_cluster_15: 8.017
- **Magnitude:** 35.6 | **LOC:** 142 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 33.017; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.9%), Debt Markers (formerly Tech Debt) (37.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 11`, `class_start: 1`
* *Risk/State:* `planned_debt: 2`
* *Architecture:* `api: 20`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.359375
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `doc/ncdu.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.249)
- **Top Global Matches:** file_cluster_2: 4.249, file_cluster_13: 5.629, file_cluster_17: 6.085
- **Magnitude:** 33.46 | **LOC:** 446 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.5%), Mutation Surface (formerly State Flux) (37.9%), Complexity Load (formerly Cognitive Load) (16.5%), Debt Markers (formerly Tech Debt) (12.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.792
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 7.535)
- **Top Global Matches:** file_cluster_17: 7.535, file_cluster_16: 7.735, file_cluster_12: 8.453
- **Magnitude:** 31.82 | **LOC:** 196 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 68.186; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.7%), Complexity Load (formerly Cognitive Load) (73.8%), Guard Balance (formerly Safety Score) (48.6%), Debt Markers (formerly Tech Debt) (32.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_ext_ptr` **(Encapsulated Accessors)** (Impact: 3.1)
    * *Intent:* /* Macros/functions for managing struct dir and struct dir_ext */ #define dir_memsize(n) (offsetof(s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 29`, `args: 36`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 68.186
  * `Choke Point (Betweenness):` 0.004872 | `Ripple Effect (Closeness):` 0.398026
  * `Imports (Out-Degree: 1):` global.h, ncurses.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/shell.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.034)
- **Top Global Matches:** file_cluster_9: 8.034, file_cluster_11: 8.133, file_cluster_15: 8.599
- **Magnitude:** 31.1 | **LOC:** 83 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (67.1%), Complexity Load (formerly Cognitive Load) (57.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shell_draw` **(I/O & Config Routines)** (Impact: 10.1)
    * *Intent:* */ #include "config.h" #include "global.h" #include "dirlist.h" #include "util.h" #include <ncurses....
  * `shell_init` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 4`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.001546 | `Ripple Effect (Closeness):` 0.204167
  * `Imports (Out-Degree: 4):` config.h, dirlist.h, global.h, ncurses.h, stdlib.h, wait.h, unistd.h, util.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/global.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 6.592)
- **Top Global Matches:** file_cluster_17: 6.592, file_cluster_2: 8.144, file_cluster_15: 8.724
- **Magnitude:** 28.32 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **19**; blast radius 285.015; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 285.015
  * `Choke Point (Betweenness):` 0.201226 | `Ripple Effect (Closeness):` 0.657609
  * `Imports (Out-Degree: 10):` browser.h, config.h, delete.h, dir.h, dirlist.h, exclude.h, help.h, inttypes.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/dirlist.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.399)
- **Top Global Matches:** file_cluster_17: 4.399, file_cluster_2: 6.526, file_cluster_11: 7.124
- **Magnitude:** 27.44 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 35.873; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 7`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.873
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.351744
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/exclude.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.945)
- **Top Global Matches:** file_cluster_17: 3.945, file_cluster_2: 6.533, file_cluster_15: 6.942
- **Magnitude:** 19.16 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 33.017; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (51.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.359375
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/delete.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.763)
- **Top Global Matches:** file_cluster_17: 3.763, file_cluster_2: 5.502, file_cluster_13: 6.228
- **Magnitude:** 18.16 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 33.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (46.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.34375
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/quit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.07)
- **Top Global Matches:** file_cluster_11: 5.07, file_cluster_15: 6.092, file_cluster_2: 7.266
- **Magnitude:** 17.4 | **LOC:** 51 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 13.442; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quit_key` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* */ #include "global.h" #include <ncurses.h>
  * `quit_draw` **(Interface Declarations)** (Impact: 1.3)
  * `quit_init` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 4`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.442
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.197581
  * `Imports (Out-Degree: 3):` global.h, ncurses.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/browser.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 3.552)
- **Top Global Matches:** file_cluster_17: 3.552, file_cluster_2: 5.34, file_cluster_13: 6.218
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 33.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (40.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.34375
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/exclude.c` (C) | Magnitude: 106.84 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 63, pointers: 30, state_mutation: 21, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/shell.c` (C) | Magnitude: 31.1 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 33, import: 8, branch: 7, state_mutation: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/main.c` -> **Severity: 14.029** (Bridge: 0.1403 * Flux: 99.9999%)
- `src/util.c` -> **Severity: 10.059** (Bridge: 0.1006 * Flux: 100.0%)
- `src/browser.c` -> **Severity: 4.229** (Bridge: 0.0423 * Flux: 100.0%)
- `src/dir_mem.c` -> **Severity: 1.683** (Bridge: 0.0168 * Flux: 100.0%)
- `src/dir_scan.c` -> **Severity: 1.294** (Bridge: 0.0129 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util.c` -> **Severity: 38.929** (Embedded: 0.4375 * Error Risk: 88.9806%)
- `src/main.c` -> **Severity: 20.625** (Embedded: 0.2552 * Error Risk: 80.8164%)
- `src/util.h` -> **Severity: 19.338** (Embedded: 0.398 * Error Risk: 48.5853%)
- `src/dir_mem.c` -> **Severity: 17.169** (Embedded: 0.1976 * Error Risk: 86.8971%)
- `src/browser.c` -> **Severity: 16.881** (Embedded: 0.2269 * Error Risk: 74.4123%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/util.h` -> **Severity: 6818.6** (Blast Radius: 68.186 * Doc Risk: 100.0%)
- `src/util.c` -> **Severity: 5623.2** (Blast Radius: 56.232 * Doc Risk: 100.0%)
- `src/main.c` -> **Severity: 3886.9** (Blast Radius: 38.869 * Doc Risk: 100.0%)
- `src/browser.c` -> **Severity: 2694.8** (Blast Radius: 26.948 * Doc Risk: 100.0%)
- `src/dir_common.c` -> **Severity: 1542.6** (Blast Radius: 15.426 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 28 literal sites + 44 sites through wrappers = 72
- **`panics_and_aborts`:** 27 literal sites + 1 sites through wrappers = 28

- `xmalloc` (function, memory_alloc, primitive): 16 call sites in 7 files -- `src/util.c`
- `xrealloc` (function, memory_alloc, primitive): 9 call sites in 4 files -- `src/util.c`
- `dir_curpath_set` (function, memory_alloc, via curpath_resize): 4 call sites in 2 files -- `src/dir_common.c`
- `curpath_resize` (function, memory_alloc, via xrealloc): 2 call sites in 1 files -- `src/dir_common.c`
- `dir_curpath_enter` (function, memory_alloc, via curpath_resize): 2 call sites in 2 files -- `src/dir_common.c`
- `dir_scan_init` (function, memory_alloc, via dir_curpath_set): 2 call sites in 2 files -- `src/dir_scan.c`
- `exclude_add` (function, memory_alloc, via xcalloc): 2 call sites in 2 files -- `src/exclude.c`
- `xcalloc` (function, memory_alloc, primitive): 2 call sites in 2 files -- `src/util.c`
- `delete_draw_progress` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/delete.c`
- `exclude_clear` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/exclude.c`
- `freedir_rec` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/util.c`
- `nstack_free` (macro, memory_alloc, primitive): 1 call sites in 1 files -- `src/util.h`
*(+2 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 646 call pairs -- scoped 17.8%, unique 26.3%, ambiguous 0.0%, external 55.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 646 | 17.8% | 26.3% | 0.0% | 55.9% |

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
