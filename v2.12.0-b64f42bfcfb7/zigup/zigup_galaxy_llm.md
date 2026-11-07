# ARCHITECTURAL_BRIEF: zigup
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/marler8997/zigup.git` |
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
- **Scope:** 10 analyzed artifact(s), 2772 LOC.
- **Load-bearing artifact:** `fixdeletetree.zig` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `.github/workflows/artifact.yml` -- pulls in 3 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `zigup.zig` at magnitude 605.96 (structural weight, not risk).
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 2772 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.9% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 8 | 2740 | 80.0% |
| YAML | 1 | 32 | 10.0% |
| MARKDOWN | 1 | 0 | 10.0% |

## 4.1 SOURCE ENCODINGS
All 10 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 50%, Data / Markup / Trivial 20%, Large Core Modules (3) 20%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 90.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 56.0 | 15.7 | 14.4 | 3.8 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 58.9 | 29.4 | 31.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 51.4 | 16.3 | 15.5 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.0 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 34.1 | 8.1 | 4.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.5 | 39.7 | 34.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.4 | 1.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.8 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 87 | 6 | 19 | `zigup.zig` |
| cleanup | 54 | 3 | 5 | `zigup.zig` |
| guards | 475 | 7 | 84 | `zigup.zig` |
| danger | 91 | 6 | 30 | `zigup.zig` |
| concurrency | 2 | 2 | 1 | `.github/workflows/artifact.yml` |
| connectivity | 55 | 7 | 13 | `zigup.zig` |
| io | 163 | 6 | 42 | `zigup.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 3 | 2 | `zigup.zig` |
| time | 2 | 2 | 1 | `fixdeletetree.zig` |
| serialization | 1 | 1 | 0 | `zigup.zig` |
| regex | 3 | 2 | 1 | `zigup.zig` |
| events | 49 | 6 | 6 | `zigup.zig` |
| tests | 3 | 2 | 1 | `build.zig` |
| docs | 5 | 2 | 2 | `zigup.zig` |
| debt | 16 | 4 | 3 | `zigup.zig` |
| mutation | 513 | 7 | 77 | `zigup.zig` |
| dead_code | 12 | 6 | 4 | `runtest.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 7 | 2 | 1 | `zigup.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5834**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `zigup.zig` (Hits: 92)
- `runtest.zig` (Hits: 42)
- `zip.zig` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fixdeletetree.zig** (`fixdeletetree.zig`) — 2 inbound connections
2. **artifact.yml** (`.github/workflows/artifact.yml`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **build.zig** (`build.zig`) — 0 inbound connections
5. **build.zig.zon** (`build.zig.zon`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **artifact.yml** (`.github/workflows/artifact.yml`) — 3 outbound dependencies
2. **runtest.zig** (`runtest.zig`) — 3 outbound dependencies
3. **zigup.zig** (`zigup.zig`) — 3 outbound dependencies
4. **build.zig** (`build.zig`) — 2 outbound dependencies
5. **fixdeletetree.zig** (`fixdeletetree.zig`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main2` **(Defensive Guards)** (@ `zigup.zig`) -> Impact: **56.9** | LOC: 177
- `copyEnvDir` **(Many-Argument Workhorses)** (@ `runtest.zig`) -> Impact: **46.0** | LOC: 71
- `main` **(Defensive Guards)** (@ `runtest.zig`) -> Impact: **41.2** | LOC: 184
- `verifyPathLink` **(Defensive Guards)** (@ `zigup.zig`) -> Impact: **35.4** | LOC: 84
  * *Intent:* /// Verify that path_link will work. It verifies that `path_link` is /// in PATH and there is no zig executable in an earlier directory in PATH.
- `cleanCompilers` **(Defensive Guards)** (@ `zigup.zig`) -> Impact: **28.3** | LOC: 47
- `addCommon` **(Many-Argument Workhorses)** (@ `build.zig`) -> Impact: **23.9** | LOC: 37
- `byteSwapAllFields` **(Many-Argument Workhorses)** (@ `zip.zig`) -> Impact: **20.9** | LOC: 36
- `installCompiler` **(Defensive Guards)** (@ `zigup.zig`) -> Impact: **19.9** | LOC: 79
- `saveInstallDir` **(Defensive Guards)** (@ `zigup.zig`) -> Impact: **17.3** | LOC: 34
- `writeZip` **(Many-Argument Workhorses)** (@ `zip.zig`) -> Impact: **17.3** | LOC: 66

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 9 | 1126.98 | 15.22% | 16.33% |
| `.github/workflows` | 1 | 2.74 | 3.85% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `win32exelink.zig` -> **51.4201%** Exposure
- `unzip.zig` -> **23.1244%** Exposure
- `zip.zig` -> **19.526%** Exposure
- `fixdeletetree.zig` -> **18.2426%** Exposure
- `zigup.zig` -> **15.453%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `unzip.zig` -> **99.5469%** Exposure
- `win32exelink.zig` -> **84.4344%** Exposure
- `zip.zig` -> **80.4558%** Exposure
- `zigup.zig` -> **48.2929%** Exposure
- `runtest.zig` -> **34.0544%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `zigup.zig` -> **2** Orphaned Functions | **0** Duplicates
- `build.zig` -> **1** Orphaned Functions | **0** Duplicates
- `runtest.zig` -> **1** Orphaned Functions | **0** Duplicates
- `unzip.zig` -> **1** Orphaned Functions | **0** Duplicates
- `win32exelink.zig` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `19` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `zigup.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.237)
- **Top Global Matches:** file_cluster_12: 8.237, file_cluster_4: 9.102, file_cluster_15: 9.466
- **Magnitude:** 605.96 | **LOC:** 1389 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 85.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (48.3%), Guard Balance (formerly Safety Score) (31.2%), Debt Markers (formerly Tech Debt) (15.5%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 48.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main2` **(Defensive Guards)** (Impact: 56.9)
  * `verifyPathLink` **(Defensive Guards)** (Impact: 35.4)
    * *Intent:* /// Verify that path_link will work. It verifies that `path_link` is /// in PATH and there is no zig...
  * `cleanCompilers` **(Defensive Guards)** (Impact: 28.3)
  * `installCompiler` **(Defensive Guards)** (Impact: 19.9)
  * `saveInstallDir` **(Defensive Guards)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 43 instances
* *Amplified Cascading Flux:* 23 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 310`, `args: 59`, `func_start: 59`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 7`, `state_mutation: 25`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 92`, `api: 24`, `import: 5`
* *Defense:* `safety: 314`, `doc: 3`, `cleanup: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` builtin, fixdeletetree.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zip.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.577)
- **Top Global Matches:** file_cluster_5: 7.577, file_cluster_12: 8.026, file_cluster_7: 9.016
- **Magnitude:** 160.92 | **LOC:** 391 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.5%), Guard Balance (formerly Safety Score) (58.9%), Complexity Load (formerly Cognitive Load) (22.2%), Debt Markers (formerly Tech Debt) (19.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `byteSwapAllFields` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `writeZip` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `main` **(I/O & Config Routines)** (Impact: 15.6)
  * `Zipper` **(Type Conversions)** (Impact: 8.7)
  * `isBadFilename` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 35`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 7`, `state_mutation: 13`, `planned_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `api: 13`, `import: 3`
* *Defense:* `safety: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtest.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.723)
- **Top Global Matches:** file_cluster_6: 6.723, file_cluster_4: 11.273, file_cluster_8: 15.181
- **Magnitude:** 135.62 | **LOC:** 317 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 85.47; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (34.1%), Guard Balance (formerly Safety Score) (26.5%), Complexity Load (formerly Cognitive Load) (14.4%), Debt Markers (formerly Tech Debt) (10.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyEnvDir` **(Many-Argument Workhorses)** (Impact: 46.0)
  * `main` **(Defensive Guards)** (Impact: 41.2)
  * `isCompilerFilesEntry` **(Defensive Guards)** (Impact: 12.0)
  * `parseInstallDir` **(Defensive Guards)** (Impact: 8.0)
  * `containsCompiler` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 60`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 4`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 42`, `api: 1`, `import: 3`
* *Defense:* `safety: 84`, `test: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` builtin, fixdeletetree.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.916)
- **Top Global Matches:** file_cluster_15: 5.916, file_cluster_2: 7.548, file_cluster_16: 7.876
- **Magnitude:** 104.78 | **LOC:** 762 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.7%), Mutation Surface (formerly State Flux) (10.3%), Debt Markers (formerly Tech Debt) (8.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addCommon` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `ci` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `addTests` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `addZigupExe` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `makeCiArchiveStep` **(Many-Argument Workhorses)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 10`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `unzip.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.314)
- **Top Global Matches:** file_cluster_15: 8.314, file_cluster_0: 8.489, file_cluster_2: 8.94
- **Magnitude:** 42.54 | **LOC:** 87 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Complexity Load (formerly Cognitive Load) (56.0%), Guard Balance (formerly Safety Score) (50.5%), Debt Markers (formerly Tech Debt) (23.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 14.5)
  * `cmdlineArgs` **(Defensive Guards)** (Impact: 4.8)
  * `fatal` **(Generic / Templated Code)** (Impact: 1.9)
  * `oom` **(State Mutators)** (Impact: 1.6)
  * `usage` **(Defensive Guards)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 2`, `import: 2`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win32exelink.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.332)
- **Top Global Matches:** file_cluster_12: 7.332, file_cluster_7: 9.483, file_cluster_15: 9.918
- **Magnitude:** 39.66 | **LOC:** 110 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.4%), Debt Markers (formerly Tech Debt) (51.4%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 9.0)
  * `consoleCtrlHandler` **(Defensive Guards)** (Impact: 7.0)
  * `SetConsoleCtrlHandler` **(State Mutators)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 5`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 3`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 11`, `import: 6`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixdeletetree.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.589)
- **Top Global Matches:** file_cluster_9: 7.589, file_cluster_15: 8.92, file_cluster_16: 9.349
- **Magnitude:** 20.8 | **LOC:** 37 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 230.77; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (34.1%), Debt Markers (formerly Tech Debt) (18.2%), Complexity Load (formerly Cognitive Load) (8.6%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deleteTree` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* // // TODO: we should fix std library to address these issues //
  * `deleteTreeAbsolute` **(Defensive Guards)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 2`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 230.77
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.222222
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `build.zig.zon` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.06)
- **Top Global Matches:** file_cluster_2: 2.06, file_cluster_17: 4.911, file_cluster_13: 6.251
- **Magnitude:** 15.32 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/artifact.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.681)
- **Top Global Matches:** file_cluster_2: 4.681, file_cluster_17: 6.236, file_cluster_11: 6.554
- **Magnitude:** 2.74 | **LOC:** 33 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 85.47; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (28.2%), Complexity Load (formerly Cognitive Load) (3.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `concurrency: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@v4, upload-artifact@v4, setup-zig@v2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.38 | **LOC:** 69 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 85.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `fixdeletetree.zig` -> **Severity: 11538.5** (Blast Radius: 230.77 * Doc Risk: 50.0%)
- `build.zig` -> **Severity: 4273.5** (Blast Radius: 85.47 * Doc Risk: 50.0%)
- `runtest.zig` -> **Severity: 4273.5** (Blast Radius: 85.47 * Doc Risk: 50.0%)
- `unzip.zig` -> **Severity: 4273.5** (Blast Radius: 85.47 * Doc Risk: 50.0%)
- `win32exelink.zig` -> **Severity: 4273.5** (Blast Radius: 85.47 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 19 literal sites + 25 sites through wrappers = 44

- `oom` (function, panics_and_aborts, primitive): 19 call sites in 1 files -- `zigup.zig`
- `oom` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `unzip.zig`
- `oom` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `zip.zig`
- `usage` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `unzip.zig`
- `usage` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `zip.zig`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 627 call pairs -- scoped 22.2%, unique 0.0%, ambiguous 2.2%, external 75.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 627 | 22.2% | 0.0% | 2.2% | 75.6% |

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
