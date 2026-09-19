# ARCHITECTURAL_BRIEF: ncdu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rofl0r/ncdu.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 31 analyzed artifact(s), 3714 LOC.
- **Load-bearing artifact:** `src/global.h` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/global.h` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/util.c` at magnitude 586.96 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 3714 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.8794 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 25.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.898 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 26 | 3386 | 83.9% |
| PLAINTEXT | 2 | 0 | 6.5% |
| MARKDOWN | 1 | 0 | 3.2% |
| M4 | 1 | 55 | 3.2% |
| PERL | 1 | 273 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `3.31`
> **Composition Archetype:** `Small Flat Repo (2)` (z +3.31; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Declarative / Non-Code 23%, Large Core Modules (3) 23%, Compute Cores Files 16%, Encapsulated Accessors Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 28 | 90.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 9.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.am`: 1x Excluded (Unsupported Extension: '.am')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.0 | 43.0 | 60.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 54.2 | 74.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.0 | 34.5 | 15.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 35.6 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.7 | 22.2 | 4.7 | 40.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 54.8 | 84.5 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 981 | 20 | 97 | `src/dir_import.c` |
| cleanup | 25 | 8 | 3 | `src/path.c` |
| guards | 187 | 19 | 18 | `src/util.c` |
| danger | 65 | 14 | 5 | `src/main.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 153 | 26 | 12 | `src/util.h` |
| io | 26 | 8 | 2 | `doc/ncdu.pod` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 2 | 0 | `doc/ncdu.pod` |
| time | 11 | 3 | 0 | `src/browser.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 4 | 2 | 0 | `doc/ncdu.pod` |
| tests | 0 | 0 | 0 | - |
| docs | 73 | 1 | 0 | `doc/ncdu.pod` |
| debt | 47 | 10 | 2 | `src/main.c` |
| mutation | 1099 | 18 | 91 | `src/dirlist.c` |
| dead_code | 50 | 15 | 4 | `src/util.c` |
| credential | 0 | 0 | 0 | - |
| threat | 41 | 8 | 3 | `src/util.h` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `src/main.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `doc/ncdu.pod` (Hits: 14)
- `src/exclude.c` (Hits: 3)
- `configure.ac` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **global.h** (`src/global.h`) — 21 inbound connections
2. **util.h** (`src/util.h`) — 3 inbound connections
3. **dirlist.h** (`src/dirlist.h`) — 2 inbound connections
4. **browser.h** (`src/browser.h`) — 1 inbound connections
5. **delete.h** (`src/delete.h`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **global.h** (`src/global.h`) — 19 outbound dependencies
2. **dir_scan.c** (`src/dir_scan.c`) — 11 outbound dependencies
3. **main.c** (`src/main.c`) — 8 outbound dependencies
4. **shell.c** (`src/shell.c`) — 8 outbound dependencies
5. **path.c** (`src/path.c`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `browse_key` **(Compute Cores)** (@ `src/browser.c`) -> Impact: **154.1** | LOC: 225
- `argv_parse` **(Many-Argument Workhorses)** (@ `src/main.c`) -> Impact: **116.7** | LOC: 151
  * *Intent:* /* parse command line */
- `dir_scan_item` **(Compute Cores)** (@ `src/dir_scan.c`) -> Impact: **61.9** | LOC: 78
  * *Intent:* /* Scans and adds a single item. Recurses into dir_walk() again if this is a * directory. Assumes we're chdir'ed in the directory in which this item *...
- `dirlist_cmp` **(Compute Cores)** (@ `src/dirlist.c`) -> Impact: **49.2** | LOC: 48
- `formatsize` **(Compute Cores)** (@ `src/util.c`) -> Impact: **47.9** | LOC: 22
- `iteminfo` **(Compute Cores)** (@ `src/dir_import.c`) -> Impact: **46.5** | LOC: 89
  * *Intent:* /* Reads a JSON object representing a struct dir/dir_ext item. Writes to * ctx->buf_dir, ctx->buf_ext and ctx->buf_name. */
- `rstring_esc` **(Stateful Encapsulated Methods)** (@ `src/dir_import.c`) -> Impact: **45.3** | LOC: 39
- `delete_key` **(Compute Cores)** (@ `src/delete.c`) -> Impact: **45.2** | LOC: 56
- `path_real_rec` **(Many-Argument Workhorses)** (@ `src/path.c`) -> Impact: **42.0** | LOC: 78
  * *Intent:* /* NOTE: cwd and the memory cur points to are unreliable after calling this * function. * TODO: This code is rather fragile and inefficient. A rewrite...
- `browse_draw_graph` **(Stateful Encapsulated Methods)** (@ `src/browser.c`) -> Impact: **38.2** | LOC: 37

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 26 | 4286.82 | 45.96% | 36.5% |
| `doc` | 1 | 33.46 | 8.55% | 15.76% |
| `__monolith__` | 4 | 21.88 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/util.c` -> **98.9804%** Exposure
- `src/quit.c` -> **98.9013%** Exposure
- `src/exclude.c` -> **95.202%** Exposure
- `src/shell.c` -> **92.4142%** Exposure
- `src/dir_common.c` -> **87.4118%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/browser.c` -> **100.0%** Exposure
- `src/delete.c` -> **100.0%** Exposure
- `src/dir_mem.c` -> **100.0%** Exposure
- `src/dir_scan.c` -> **100.0%** Exposure
- `src/dirlist.c` -> **100.0%** Exposure
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
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/util.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 586.96 | **LOC:** 435 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Debt Markers (formerly Tech Debt) (99.0%), Complexity Load (formerly Cognitive Load) (81.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatsize` **(Compute Cores)** (Impact: 47.9)
  * `fmtmode` **(Stateful Encapsulated Methods)** (Impact: 26.6)
  * `freedir_hlnk` **(C Struct Operations)** (Impact: 20.0)
    * *Intent:* /* removes item from the hlnk circular linked list and size counts of the parents */
  * `getpath` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `freedir` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 44`, `args: 30`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 118`, `fragile_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 2`, `api: 19`, `import: 7`
* *Defense:* `safety: 6`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` locale.h, ncurses.h, stdarg.h, stdlib.h, string.h, unistd.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/browser.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 585.58 | **LOC:** 568 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `browse_key` **(Compute Cores)** (Impact: 154.1)
  * `browse_draw_graph` **(Stateful Encapsulated Methods)** (Impact: 38.2)
  * `browse_draw_flag` **(Stateful Encapsulated Methods)** (Impact: 25.1)
  * `browse_draw_info` **(Compute Cores)** (Impact: 23.4)
  * `browse_draw_items` **(C Struct Operations)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 72`, `args: 39`, `func_start: 9`, `class_start: 10`
* *Risk/State:* `state_mutation: 91`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, ncurses.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dirlist.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 510.98 | **LOC:** 399 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dirlist_cmp` **(Compute Cores)** (Impact: 49.2)
  * `dirlist_sort` **(Compute Cores)** (Impact: 29.2)
  * `dirlist_top` **(Compute Cores)** (Impact: 24.6)
    * *Intent:* * -2 = selected = first item in the list (faster version of '1') * -3 = top should be considered as ...
  * `dirlist_get` **(Compute Cores)** (Impact: 15.9)
  * `dirlist_set_sort` **(Compute Cores)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 51`, `args: 14`, `func_start: 12`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 103`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_import.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 435.54 | **LOC:** 616 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iteminfo` **(Compute Cores)** (Impact: 46.5)
    * *Intent:* /* Reads a JSON object representing a struct dir/dir_ext item. Writes to * ctx->buf_dir, ctx->buf_ex...
  * `rstring_esc` **(Stateful Encapsulated Methods)** (Impact: 45.3)
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
* *Structure:* `branch: 167`, `structural_boundaries: 78`, `args: 23`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 6`
* *Defense:* `safety: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, limits.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_scan.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 336.68 | **LOC:** 406 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (82.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_scan_item` **(Compute Cores)** (Impact: 61.9)
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
* *Structure:* `branch: 116`, `structural_boundaries: 33`, `args: 18`, `func_start: 8`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirent.h, errno.h, global.h, magic.h, stdlib.h, string.h, attr.h, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 323.18 | **LOC:** 360 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (82.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `argv_parse` **(Many-Argument Workhorses)** (Impact: 116.7)
    * *Intent:* /* parse command line */
  * `input_handle` **(Compute Cores)** (Impact: 30.4)
    * *Intent:* /* wait: * -1: non-blocking, always draw screen * 0: blocking wait for input and always draw screen ...
  * `main` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* /* main program */
  * `init_nc` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* /* Initializes ncurses only when not done yet. */
  * `screen_draw` **(Stateful Encapsulated Methods)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 46`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 49`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, stdio.h, stdlib.h, string.h, time.h, unistd.h, yopt.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/path.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 260.46 | **LOC:** 247 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 45`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 56`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `immutability_locks: 3`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, limits.h, stdio.h, stdlib.h, string.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_mem.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 226.26 | **LOC:** 216 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (84.0%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 43`, `structural_boundaries: 25`, `args: 8`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, khashl.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/delete.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 212.06 | **LOC:** 254 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Complexity Load (formerly Cognitive Load) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `delete_key` **(Compute Cores)** (Impact: 45.2)
  * `delete_dir` **(Compute Cores)** (Impact: 27.6)
  * `delete_draw_confirm` **(Stateful Encapsulated Methods)** (Impact: 12.2)
  * `delete_process` **(I/O & Config Routines)** (Impact: 10.6)
  * `delete_draw` **(Compute Cores)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 37`, `args: 20`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, global.h, string.h, unistd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_common.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 152.58 | **LOC:** 233 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.1%), Debt Markers (formerly Tech Debt) (87.4%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, stdarg.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/help.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 128.86 | **LOC:** 213 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `help_key` **(Compute Cores)** (Impact: 35.8)
  * `help_draw` **(I/O & Config Routines)** (Impact: 13.6)
  * `help_init` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 11`, `args: 12`, `func_start: 3`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, ncurses.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_export.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 127.2 | **LOC:** 195 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, stdio.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exclude.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 106.84 | **LOC:** 139 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Debt Markers (formerly Tech Debt) (95.2%), Complexity Load (formerly Cognitive Load) (71.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fnmatch.h, global.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 35.82 | **LOC:** 196 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 52.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (82.2%), Connectivity (formerly Api Exposure) (75.7%), Guard Balance (formerly Safety Score) (57.0%), Debt Markers (formerly Tech Debt) (45.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dir_ext_ptr` **(Encapsulated Accessors)** (Impact: 3.1)
    * *Intent:* /* Macros/functions for managing struct dir and struct dir_ext */ #define dir_memsize(n) (offsetof(s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 29`, `args: 36`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.556
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.393496
  * `Imports (Out-Degree: 1):` global.h, ncurses.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/dir.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 35.6 | **LOC:** 142 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 41.696; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.9%), Debt Markers (formerly Tech Debt) (62.2%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 16`, `args: 11`, `class_start: 1`
* *Risk/State:* `planned_debt: 2`
* *Architecture:* `api: 20`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.383333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `doc/ncdu.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 33.46 | **LOC:** 446 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.582; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.3%), Mutation Surface (formerly State Flux) (37.9%), Debt Markers (formerly Tech Debt) (15.8%), Complexity Load (formerly Cognitive Load) (8.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `import: 7`
* *Defense:* `doc: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` C, cases, effect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shell.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 31.1 | **LOC:** 83 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.4%), Guard Balance (formerly Safety Score) (92.3%), Complexity Load (formerly Cognitive Load) (57.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` config.h, dirlist.h, global.h, ncurses.h, stdlib.h, wait.h, unistd.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/global.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 28.32 | **LOC:** 133 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **19**; blast radius 377.819; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 2`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 19`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 377.819
  * `Choke Point (Betweenness):` 0.241379 | `Ripple Effect (Closeness):` 0.701449
  * `Imports (Out-Degree: 10):` browser.h, config.h, delete.h, dir.h, dirlist.h, exclude.h, help.h, inttypes.h...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/dirlist.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 27.44 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 44.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 7`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.375194
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/exclude.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 19.16 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 41.696; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (51.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 5`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.383333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/quit.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 18.4 | **LOC:** 51 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.582; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (98.9%), Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (66.5%), Complexity Load (formerly Cognitive Load) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quit_key` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* */ #include "global.h" #include <ncurses.h>
  * `quit_draw` **(Interface Declarations)** (Impact: 2.3)
  * `quit_init` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.582
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` global.h, ncurses.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/delete.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 18.16 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 41.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (46.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/browser.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 41.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (40.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/help.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 41.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (40.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/quit.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 16.64 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 41.696; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (40.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 3`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.696
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.366667
  * `Imports (Out-Degree: 1):` global.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/util.h` -> **Severity: 0.308** (Bridge: 0.0115 * Flux: 26.8028%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util.h` -> **Severity: 22.441** (Embedded: 0.3935 * Error Risk: 57.0286%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/util.h` -> **Severity: 5255.6** (Blast Radius: 52.556 * Doc Risk: 100.0%)
- `src/browser.c` -> **Severity: 958.2** (Blast Radius: 9.582 * Doc Risk: 100.0%)
- `src/delete.c` -> **Severity: 958.2** (Blast Radius: 9.582 * Doc Risk: 100.0%)
- `src/dir_common.c` -> **Severity: 958.2** (Blast Radius: 9.582 * Doc Risk: 100.0%)
- `src/dir_export.c` -> **Severity: 958.2** (Blast Radius: 9.582 * Doc Risk: 100.0%)

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
