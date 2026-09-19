# ARCHITECTURAL_BRIEF: diff-so-fancy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/so-fancy/diff-so-fancy.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 14 analyzed artifact(s), 1791 LOC.
- **Load-bearing artifact:** `lib/DiffHighlight.pm` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `diff-so-fancy` -- pulls in 23 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `diff-so-fancy` at magnitude 1116.94 (structural weight, not risk).
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
| Total Artifacts | 66 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 52 |
| Total LOC | 1791 |
| Volatility Index | 0.071 |
| % Scanned of codebase = | 21.2% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SHELL | 6 | 457 | 42.9% |
| PERL | 3 | 1313 | 21.4% |
| MARKDOWN | 2 | 0 | 14.3% |
| YAML | 1 | 6 | 7.1% |
| JSON | 1 | 15 | 7.1% |
| PLAINTEXT | 1 | 0 | 7.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Large Core Modules 21%, Compute Cores Files 7%, Declarative / Non-Code 7%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 11 | 78.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 21.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 52*

**Composition by Extension & Reason:**
- `.diff`: 32x Excluded (Unsupported Extension: '.diff')
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.1`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.1 | 24.5 | 9.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 66.7 | 91.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 9.5 | 0.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 50.4 | 7.5 | 2.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.5 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.3 | 0.4 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 26.6 | 19.5 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.8 | 88.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10 | 1 | 0 | `diff-so-fancy` |
| cleanup | 2 | 2 | 1 | `test/diff-so-fancy.bats` |
| guards | 9 | 3 | 3 | `test/git_ansi_color.pl` |
| danger | 98 | 7 | 18 | `test/diff-so-fancy.bats` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 68 | 6 | 12 | `diff-so-fancy` |
| io | 86 | 6 | 18 | `test/diff-so-fancy.bats` |
| crypto | 0 | 0 | 0 | - |
| ipc | 6 | 2 | 1 | `diff-so-fancy` |
| time | 3 | 1 | 0 | `diff-so-fancy` |
| serialization | 0 | 0 | 0 | - |
| regex | 132 | 4 | 22 | `diff-so-fancy` |
| events | 0 | 0 | 0 | - |
| tests | 96 | 3 | 27 | `test/diff-so-fancy.bats` |
| docs | 11 | 1 | 0 | `diff-so-fancy` |
| debt | 69 | 7 | 21 | `diff-so-fancy` |
| mutation | 478 | 8 | 82 | `diff-so-fancy` |
| dead_code | 26 | 6 | 4 | `diff-so-fancy` |
| credential | 0 | 0 | 0 | - |
| threat | 3 | 3 | 1 | `diff-so-fancy` |
| ml_ai | 15 | 2 | 7 | `diff-so-fancy` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/diff-so-fancy.bats` (Hits: 41)
- `test/bugs.bats` (Hits: 18)
- `test/test_helper/util.bash` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DiffHighlight.pm** (`lib/DiffHighlight.pm`) — 1 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **README.md** (`test/README.md`) — 0 inbound connections
4. **appveyor.yml** (`appveyor.yml`) — 0 inbound connections
5. **diff-so-fancy** (`diff-so-fancy`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **diff-so-fancy** (`diff-so-fancy`) — 23 outbound dependencies
2. **DiffHighlight.pm** (`lib/DiffHighlight.pm`) — 6 outbound dependencies
3. **README.md** (`README.md`) — 5 outbound dependencies
4. **git_ansi_color.pl** (`test/git_ansi_color.pl`) — 5 outbound dependencies
5. **README.md** (`test/README.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `do_dsf_stuff` **(I/O & Config Routines)** (@ `diff-so-fancy`) -> Impact: **118.6** | LOC: 312
  * *Intent:* ################################################################################# ####################################################################...
- `highlight_pair` **(Compute Cores)** (@ `lib/DiffHighlight.pm`) -> Impact: **37.5** | LOC: 57
- `handle_line` **(Compute Cores)** (@ `lib/DiffHighlight.pm`) -> Impact: **31.0** | LOC: 54
- `git_ansi_color` **(I/O & Config Routines)** (@ `test/git_ansi_color.pl`) -> Impact: **25.1** | LOC: 83
  * *Intent:* # https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_colors_in_git
- `color` **(Compute Cores)** (@ `diff-so-fancy`) -> Impact: **22.2** | LOC: 29
  * *Intent:* # String format: '115', '165_bold', '10_on_140', 'reset', 'on_173', 'red', 'white_on_blue'
- `show_debug_info` **(Compute Cores)** (@ `diff-so-fancy`) -> Impact: **19.6** | LOC: 32
- `is_pair_interesting` **(Many-Argument Workhorses)** (@ `lib/DiffHighlight.pm`) -> Impact: **17.1** | LOC: 24
  * *Intent:* # Pairs are interesting to highlight only if we are going to end up # highlighting a subset (i.e., not the whole line). Otherwise, the highlighting # ...
- `git_ansi_color` **(I/O & Config Routines)** (@ `diff-so-fancy`) -> Impact: **17.0** | LOC: 60
  * *Intent:* # https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_colors_in_git
- `set_ansi_color` **(Many-Argument Workhorses)** (@ `diff-so-fancy`) -> Impact: **16.9** | LOC: 25
- `get_diff_chunks` **(Compute Cores)** (@ `diff-so-fancy`) -> Impact: **16.6** | LOC: 49
  * *Intent:* # This function divides Git/Diff strings into smaller chunks that d-s-f can # process. The special sauce is not splitting on the Git headers, or any o...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 7 | 1157.78 | 12.32% | 1.36% |
| `test` | 5 | 371.24 | 17.76% | 0.0% |
| `lib` | 1 | 287.1 | 80.08% | 0.0% |
| `test/test_helper` | 1 | 27.36 | 14.25% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `diff-so-fancy` -> **9.5066%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `diff-so-fancy` -> **100.0%** Exposure
- `lib/DiffHighlight.pm` -> **100.0%** Exposure
- `diff-so-fancy.plugin.zsh` -> **50.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/test_helper/util.bash` -> **4** Orphaned Functions | **0** Duplicates
- `test/git_ansi_color.pl` -> **3** Orphaned Functions | **0** Duplicates
- `test/bugs.bats` -> **3** Orphaned Functions | **0** Duplicates
- `test/git-config.bats` -> **3** Orphaned Functions | **0** Duplicates
- `test/diff-so-fancy.bats` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `39` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `diff-so-fancy` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1116.94 | **LOC:** 1442 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 67.34; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_dsf_stuff` **(I/O & Config Routines)** (Impact: 118.6)
    * *Intent:* ################################################################################# ##################...
  * `color` **(Compute Cores)** (Impact: 22.2)
    * *Intent:* # String format: '115', '165_bold', '10_on_140', 'reset', 'on_173', 'red', 'white_on_blue'
  * `show_debug_info` **(Compute Cores)** (Impact: 19.6)
  * `git_ansi_color` **(I/O & Config Routines)** (Impact: 17.0)
    * *Intent:* # https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_colors_in_git
  * `set_ansi_color` **(Many-Argument Workhorses)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 594
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 355`, `args: 12`, `func_start: 42`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 210`, `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 42`, `import: 12`
* *Defense:* `safety: 3`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ANSI, ASCII, C, Cwd, DiffHighlight, Dump::Krumo, Encode, File::Basename...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/DiffHighlight.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 287.1 | **LOC:** 327 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 124.579; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `highlight_pair` **(Compute Cores)** (Impact: 37.5)
  * `handle_line` **(Compute Cores)** (Impact: 31.0)
  * `is_pair_interesting` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* # Pairs are interesting to highlight only if we are going to end up # highlighting a subset (i.e., n...
  * `color_config` **(Compute Cores)** (Impact: 16.4)
    * *Intent:* # Ideally we would feed the default as a human-readable color to # git-config as the fallback value....
  * `split_line` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* # we split either by $COLOR or by character. This has the side effect of # leaving in graph cruft. I...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 75`, `args: 10`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`
* *Architecture:* `io: 1`, `api: 12`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 124.579
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 0):` File::Spec, optimal, strict, trailing, v5, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/git_ansi_color.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 158.22 | **LOC:** 254 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 67.34; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.7%), Complexity Load (formerly Cognitive Load) (38.8%), Connectivity (formerly Api Exposure) (7.9%), Dead Code Surface (formerly Dead Code) (6.6%)
- **Documentation Coverage:** 88.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `git_ansi_color` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* # https://www.git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_colors_in_git
  * `color` **(I/O & Config Routines)** (Impact: 12.4)
    * *Intent:* # String format: '115', '165_bold', '10_on_140', 'reset', 'on_173', 'red', 'white_on_blue'
  * `git_ansi_color2` **(I/O & Config Routines)** (Impact: 12.2)
    * *Intent:* # Alternate (unused) method to parse git config colors
  * `compare_color` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* ############################################################################### ####################...
  * `trim` **(Compute Cores)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 57`, `args: 1`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 28`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dump::Color, Data::Dumper, strict, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/diff-so-fancy.bats` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 92.72 | **LOC:** 257 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%), Complexity Load (formerly Cognitive Load) (9.8%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 88.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* # see https://git.io/vrOF4
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.5)
  * `setup_file` **(Interface Declarations)** (Impact: 1.4)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.4)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 48`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 34`, `unreferenced_by_name: 2`
* *Architecture:* `io: 41`, `api: 1`
* *Defense:* `test: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/git-config.bats` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 83.28 | **LOC:** 172 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.3%), Complexity Load (formerly Cognitive Load) (40.2%), Connectivity (formerly Api Exposure) (4.3%)
- **Documentation Coverage:** 88.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_dsf_git_config` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* # build config using passed in values
  * `ansi_color` **(Parameter Forwarders)** (Impact: 4.2)
    * *Intent:* # get a foreground or background color code
  * `rgb_color` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* # get rgb color codes from hex
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 2.0)
    * *Intent:* # General description of how colors are applied # meta = header # frag = @ filenames # func = functi...
  * `__global_context__` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 10`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 35`, `unreferenced_by_name: 3`
* *Architecture:* `io: 11`, `api: 2`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/bugs.bats` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 36.02 | **LOC:** 116 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (91.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 88.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.6)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.5)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* # https://github.com/paulirish/dotfiles/commit/6743b907ff586c28cd36e08d1e1c634e2968893e#commitcommen...
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.4)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `io: 18`
* *Defense:* `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/test_helper/util.bash` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 27.36 | **LOC:** 48 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.1%), Complexity Load (formerly Cognitive Load) (14.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.0%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_default_dsf_git_config` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* # applying colors so ANSI color values will match # FIXME: not everyone will have these set, so we n...
  * `teardown_default_dsf_git_config` **(Interface Declarations)** (Impact: 3.3)
  * `load_fixture` **(Parameter Forwarders)** (Impact: 1.6)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.5)
  * `set_env` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 1`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 13`, `api: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package-lock.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.7%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `appveyor.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 13.12 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.5%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `diff-so-fancy.plugin.zsh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 6.62 | **LOC:** 13 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.4%), Mutation Surface (formerly State Flux) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.3%), Complexity Load (formerly Cognitive Load) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.1)
  * `__global_context__` **(Unclassified)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.56 | **LOC:** 128 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 67.34; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` diff-so-fancy.png, hacking-and-testing.md, history.md, pro-tips.md, reporting-bugs.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `update-deps.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2.24 | **LOC:** 5 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `diff-so-fancy` -> Churn: **100.0%** | Cog Load: 73.1234% | Debt: 9.5066%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `diff-so-fancy` -> **Scott Baker** (100.0% isolated ownership) | Magnitude: 1116.94
- `lib/DiffHighlight.pm` -> **Scott Baker** (100.0% isolated ownership) | Magnitude: 287.1
- `test/diff-so-fancy.bats` -> **Scott Baker** (100.0% isolated ownership) | Magnitude: 92.72

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/DiffHighlight.pm` -> **Severity: 7.234** (Embedded: 0.0769 * Error Risk: 94.0476%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/DiffHighlight.pm` -> **Severity: 12457.9** (Blast Radius: 124.579 * Doc Risk: 100.0%)
- `test/test_helper/util.bash` -> **Severity: 6734.0** (Blast Radius: 67.34 * Doc Risk: 100.0%)
- `test/git_ansi_color.pl` -> **Severity: 5937.806** (Blast Radius: 67.34 * Doc Risk: 88.1765%)
- `test/bugs.bats` -> **Severity: 5937.806** (Blast Radius: 67.34 * Doc Risk: 88.1765%)
- `test/diff-so-fancy.bats` -> **Severity: 5937.806** (Blast Radius: 67.34 * Doc Risk: 88.1765%)

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
