# ARCHITECTURAL_BRIEF: @node-red_editor-api
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 28 analyzed artifact(s), 2749 LOC.
- **Load-bearing artifact:** `package/lib/util.js` -- 16 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/editor/index.js` -- pulls in 13 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/editor/theme.js` at magnitude 384.9 (structural weight, not risk).
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
| Total Artifacts | 29 |
| Analyzed Artifacts (Scanned) | 28 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 2749 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3519 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.567 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4948 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 26 | 2749 | 92.9% |
| MARKDOWN | 1 | 0 | 3.6% |
| PLAINTEXT | 1 | 0 | 3.6% |

## 4.1 SOURCE ENCODINGS
All 28 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 64%, Large Core Modules (2) 14%, Data / Markup / Trivial 7%, Large Core Modules (3) 7%, Interface Declarations Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 26 | 92.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 7.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.9 | 52.9 | 61.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 40.8 | 77.2 | 53.4 | 51.6 | 49.9 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 85.9 | 12.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 14.5 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 2.4 | 71.2 | 35.3 | 40.1 | 40.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 74.7 | 99.8 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 27.5 | 100.0 | 84.1 | 98.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 66.5 | 7.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 94.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 2 | 0 | `package/lib/auth/index.js` |
| cleanup | 6 | 2 | 0 | `package/lib/editor/comms.js` |
| guards | 164 | 24 | 11 | `package/lib/editor/projects.js` |
| danger | 14 | 9 | 2 | `package/lib/editor/comms.js` |
| concurrency | 205 | 22 | 11 | `package/lib/editor/projects.js` |
| connectivity | 130 | 26 | 6 | `package/lib/editor/projects.js` |
| io | 19 | 3 | 0 | `package/lib/editor/ui.js` |
| crypto | 4 | 4 | 1 | `package/lib/auth/index.js` |
| ipc | 0 | 0 | 0 | - |
| time | 15 | 3 | 0 | `package/lib/auth/tokens.js` |
| serialization | 7 | 3 | 0 | `package/lib/editor/comms.js` |
| regex | 6 | 4 | 1 | `package/lib/auth/strategies.js` |
| events | 22 | 1 | 0 | `package/lib/editor/comms.js` |
| tests | 0 | 0 | 0 | - |
| docs | 35 | 24 | 1 | `package/lib/index.js` |
| debt | 22 | 12 | 3 | `package/lib/auth/index.js` |
| mutation | 682 | 26 | 49 | `package/lib/editor/theme.js` |
| dead_code | 19 | 9 | 3 | `package/lib/auth/index.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/editor/ui.js` (Hits: 8)
- `package/lib/editor/theme.js` (Hits: 7)
- `package/lib/editor/index.js` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.js** (`package/lib/util.js`) — 16 inbound connections
2. **index.js** (`package/lib/auth/index.js`) — 4 inbound connections
3. **theme.js** (`package/lib/editor/theme.js`) — 4 inbound connections
4. **permissions.js** (`package/lib/auth/permissions.js`) — 3 inbound connections
5. **tokens.js** (`package/lib/auth/tokens.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/lib/editor/index.js`) — 13 outbound dependencies
2. **index.js** (`package/lib/auth/index.js`) — 11 outbound dependencies
3. **index.js** (`package/lib/admin/index.js`) — 10 outbound dependencies
4. **strategies.js** (`package/lib/auth/strategies.js`) — 9 outbound dependencies
5. **comms.js** (`package/lib/editor/comms.js`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `CommsConnection` **(Many-Argument Workhorses)** (@ `package/lib/editor/comms.js`) -> Impact: **49.0** | LOC: 113
- `loadThemePlugin` **(I/O & Config Routines)** (@ `package/lib/editor/theme.js`) -> Impact: **48.0** | LOC: 121
  * *Intent:* /** * Check if a theme is enabled and load its settings. * This is done lazily as it has to happen after the plugins have been loaded, but before the ...
- `app` **(I/O & Config Routines)** (@ `package/lib/editor/theme.js`) -> Impact: **45.9** | LOC: 158
- `init` **(Defensive Guards)** (@ `package/lib/auth/users.js`) -> Impact: **45.0** | LOC: 52
- `app` **(Callbacks & Closures)** (@ `package/lib/editor/projects.js`) -> Impact: **43.0** | LOC: 460
- `init` **(Many-Argument Workhorses)** (@ `package/lib/index.js`) -> Impact: **36.5** | LOC: 60
  * *Intent:* /** * Initialise the module. */
- `init` **(Many-Argument Workhorses)** (@ `package/lib/admin/index.js`) -> Impact: **34.8** | LOC: 72
- `login` **(Defensive Guards)** (@ `package/lib/auth/index.js`) -> Impact: **31.8** | LOC: 47
- `hasPermission` **(Defensive Guards)** (@ `package/lib/auth/permissions.js`) -> Impact: **29.7** | LOC: 40
- `passwordTokenExchange` **(Many-Argument Workhorses)** (@ `package/lib/auth/strategies.js`) -> Impact: **26.9** | LOC: 48

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib/editor` | 10 | 1128.64 | 44.39% | 15.68% |
| `package/lib/auth` | 6 | 664.12 | 69.77% | 10.84% |
| `package/lib/admin` | 8 | 507.42 | 54.13% | 3.65% |
| `package/lib` | 2 | 126.8 | 40.3% | 40.65% |
| `package` | 2 | 2.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/editor/index.js` -> **85.9404%** Exposure
- `package/lib/util.js` -> **58.1805%** Exposure
- `package/lib/auth/index.js` -> **54.7502%** Exposure
- `package/lib/admin/index.js` -> **29.1709%** Exposure
- `package/lib/index.js` -> **23.1244%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/auth/tokens.js` -> **100.0%** Exposure
- `package/lib/auth/users.js` -> **100.0%** Exposure
- `package/lib/editor/theme.js` -> **100.0%** Exposure
- `package/lib/editor/comms.js` -> **99.9961%** Exposure
- `package/lib/admin/settings.js` -> **99.9932%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/auth/index.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/lib/editor/index.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/lib/admin/index.js` -> **1** Orphaned Functions | **0** Duplicates
- `package/lib/index.js` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `42` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/editor/theme.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.485)
- **Top Global Matches:** file_cluster_8: 8.485, file_cluster_6: 10.163, file_cluster_4: 18.198
- **Magnitude:** 384.9 | **LOC:** 414 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 56.789; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (88.7%), Complexity Load (formerly Cognitive Load) (85.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadThemePlugin` **(I/O & Config Routines)** (Impact: 48.0)
    * *Intent:* /** * Check if a theme is enabled and load its settings. * This is done lazily as it has to happen a...
  * `app` **(I/O & Config Routines)** (Impact: 45.9)
  * `serveFilesFromTheme` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `init` **(Defensive Guards)** (Impact: 9.5)
  * `serveFile` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 39`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 80`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 8`, `import: 5`
* *Defense:* `safety: 11`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.789
  * `Choke Point (Betweenness):` 0.002849 | `Ripple Effect (Closeness):` 0.181481
  * `Imports (Out-Degree: 1):` util, clone, fs, path, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/editor/comms.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.524)
- **Top Global Matches:** file_cluster_4: 8.524, file_cluster_12: 10.262, file_cluster_10: 10.654
- **Magnitude:** 245.24 | **LOC:** 293 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 21.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (87.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CommsConnection` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `start` **(Callbacks & Closures)** (Impact: 13.8)
  * `completeConnection` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `handleAuthPacket` **(Callbacks & Closures)** (Impact: 11.2)
  * `upgrade` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 33`, `args: 30`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 8`, `import: 8`
* *Defense:* `safety: 11`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.003561 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 4):` permissions, strategies, tokens, users, util, crypto, url, ws
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/editor/projects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.649)
- **Top Global Matches:** file_cluster_6: 9.649, file_cluster_4: 12.577, file_cluster_8: 16.941
- **Magnitude:** 224.62 | **LOC:** 545 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 21.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (79.7%), Connectivity (formerly Api Exposure) (63.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `app` **(Callbacks & Closures)** (Impact: 43.0)
  * `getProject` **(Defensive Guards)** (Impact: 6.0)
  * `getProjectStatus` **(Defensive Guards)** (Impact: 6.0)
  * `listProjects` **(Callbacks & Closures)** (Impact: 2.3)
  * `getProjectRemotes` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 105
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 45`, `args: 98`, `func_start: 6`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 32`, `concurrency: 65`, `import: 2`
* *Defense:* `safety: 32`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 2):` auth, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/auth/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.697)
- **Top Global Matches:** file_cluster_4: 6.697, file_cluster_15: 9.464, file_cluster_10: 10.182
- **Magnitude:** 184.56 | **LOC:** 286 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 37.885; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (94.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.9%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `login` **(Defensive Guards)** (Impact: 31.8)
  * `genericStrategy` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `needsPermission` **(Callbacks & Closures)** (Impact: 9.4)
    * *Intent:* /** * Returns an Express middleware function that ensures the user making a request * has the necess...
  * `revoke` **(Compute Cores)** (Impact: 9.3)
  * `completeVerify` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 38`, `args: 19`, `func_start: 14`
* *Risk/State:* `state_mutation: 19`, `dead_code: 2`, `planned_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 11`
* *Defense:* `safety: 7`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.885
  * `Choke Point (Betweenness):` 0.027778 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 5):` theme, permissions, strategies, tokens, users, util, crypto, express-session...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/auth/users.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.583)
- **Top Global Matches:** file_cluster_4: 8.583, file_cluster_12: 11.542, file_cluster_6: 12.008
- **Magnitude:** 155.32 | **LOC:** 135 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 37.833; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.4%), Complexity Load (formerly Cognitive Load) (90.6%), Guard Balance (formerly Safety Score) (59.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Defensive Guards)** (Impact: 45.0)
  * `authenticate` **(Defensive Guards)** (Impact: 9.3)
  * `cleanUser` **(Compute Cores)** (Impact: 4.6)
  * `default` **(Callbacks & Closures)** (Impact: 3.3)
  * `default` **(Callbacks & Closures)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 29`, `args: 14`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`
* *Architecture:* `api: 1`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 17`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164983
  * `Imports (Out-Degree: 0):` bcrypt, bcryptjs, clone, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/admin/nodes.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.628)
- **Top Global Matches:** file_cluster_10: 5.628, file_cluster_12: 8.69, file_cluster_15: 8.932
- **Magnitude:** 141.34 | **LOC:** 208 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 24.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (94.3%), Complexity Load (formerly Cognitive Load) (81.1%), Connectivity (formerly Api Exposure) (58.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `post` **(Defensive Guards)** (Impact: 9.9)
  * `getSet` **(Defensive Guards)** (Impact: 8.1)
  * `getAll` **(Callbacks & Closures)** (Impact: 7.9)
  * `putModule` **(Callbacks & Closures)** (Impact: 4.5)
  * `putSet` **(Callbacks & Closures)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 18`, `args: 32`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `dead_code: 2`
* *Architecture:* `api: 12`, `concurrency: 21`, `import: 1`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/auth/strategies.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.009)
- **Top Global Matches:** file_cluster_12: 8.009, file_cluster_10: 8.061, file_cluster_15: 9.775
- **Magnitude:** 134.28 | **LOC:** 188 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 31.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `passwordTokenExchange` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `authenticateUserToken` **(Defensive Guards)** (Impact: 17.0)
  * `bearerStrategy` **(Callbacks & Closures)** (Impact: 9.6)
  * `clientPasswordStrategy` **(Callbacks & Closures)** (Impact: 8.5)
  * `authenticate` **(Callbacks & Closures)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 27`, `args: 21`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 11`, `import: 9`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.202
  * `Choke Point (Betweenness):` 0.008547 | `Ripple Effect (Closeness):` 0.133333
  * `Imports (Out-Degree: 4):` clients, permissions, tokens, users, util, passport, passport-http-bearer, passport-oauth2-client-password...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/auth/tokens.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.909)
- **Top Global Matches:** file_cluster_10: 6.909, file_cluster_15: 8.71, file_cluster_16: 9.436
- **Magnitude:** 124.58 | **LOC:** 145 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 37.833; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (88.7%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expireSessions` **(Compute Cores)** (Impact: 12.6)
  * `get` **(Callbacks & Closures)** (Impact: 9.3)
  * `init` **(Defensive Guards)** (Impact: 6.3)
  * `create` **(Callbacks & Closures)** (Impact: 5.3)
  * `loadSessions` **(Callbacks & Closures)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 35`, `args: 15`, `func_start: 7`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164983
  * `Imports (Out-Degree: 0):` crypto
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/admin/plugins.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.562)
- **Top Global Matches:** file_cluster_10: 6.562, file_cluster_12: 8.03, file_cluster_15: 9.621
- **Magnitude:** 83.86 | **LOC:** 83 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (98.9%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getConfig` **(Defensive Guards)** (Impact: 8.2)
  * `getAll` **(Callbacks & Closures)** (Impact: 7.9)
  * `getCatalogs` **(Callbacks & Closures)** (Impact: 4.3)
  * `getModule` **(Callbacks & Closures)** (Impact: 2.3)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 15`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `api: 6`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/editor/ui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.855)
- **Top Global Matches:** file_cluster_10: 6.855, file_cluster_12: 7.949, file_cluster_15: 8.957
- **Magnitude:** 82.42 | **LOC:** 118 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 21.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (82.5%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `icon` **(Callbacks & Closures)** (Impact: 8.0)
  * `editor` **(Compute Cores)** (Impact: 7.9)
  * `ensureSlash` **(Callbacks & Closures)** (Impact: 6.5)
  * `moduleResource` **(Callbacks & Closures)** (Impact: 6.2)
  * `init` **(State Mutators)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 27`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `io: 8`, `api: 5`, `concurrency: 6`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 2):` util, theme, crypto, express, fs, mime, mustache, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/flows.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.139)
- **Top Global Matches:** file_cluster_10: 7.139, file_cluster_9: 9.077, file_cluster_15: 9.377
- **Magnitude:** 76.82 | **LOC:** 96 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.7%), Complexity Load (formerly Cognitive Load) (80.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `post` **(Defensive Guards)** (Impact: 17.0)
  * `get` **(Defensive Guards)** (Impact: 11.3)
  * `postState` **(Callbacks & Closures)** (Impact: 4.1)
  * `getState` **(Callbacks & Closures)** (Impact: 2.3)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 8`, `args: 13`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 5`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/settings.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.016)
- **Top Global Matches:** file_cluster_10: 7.016, file_cluster_15: 8.552, file_cluster_9: 8.736
- **Magnitude:** 68.58 | **LOC:** 72 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (55.6%), Guard Balance (formerly Safety Score) (52.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extend` **(Defensive Guards)** (Impact: 21.9)
  * `runtimeSettings` **(Callbacks & Closures)** (Impact: 7.8)
  * `init` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 13`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.000712 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` theme, util, clone
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.74)
- **Top Global Matches:** file_cluster_10: 6.74, file_cluster_15: 8.124, file_cluster_16: 9.014
- **Magnitude:** 65.26 | **LOC:** 80 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **2**; blast radius 283.015; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (71.2%), Complexity Load (formerly Cognitive Load) (59.3%), Guard Balance (formerly Safety Score) (58.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rejectHandler` **(Compute Cores)** (Impact: 16.9)
  * `errorHandler` **(Defensive Guards)** (Impact: 9.5)
  * `getRequestLogObject` **(Callbacks & Closures)** (Impact: 7.4)
  * `createExpressApp` **(Callbacks & Closures)** (Impact: 4.8)
  * `determineLangFromHeaders` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 6`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 3`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 283.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.6
  * `Imports (Out-Degree: 0):` util, express
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.798)
- **Top Global Matches:** file_cluster_11: 6.798, file_cluster_15: 7.236, file_cluster_16: 8.083
- **Magnitude:** 61.54 | **LOC:** 147 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 20.092; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (50.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (39.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* /** * Initialise the module. */
  * `start` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* /** * Start the module. */
  * `stop` **(State Mutators)** (Impact: 2.2)
    * *Intent:* /** * Stop the module. */
  * `httpAdmin` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** * The Express app used to serve the Node-RED Editor */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 6`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` admin, auth, editor, util, body-parser, cors, passport
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/editor/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.42)
- **Top Global Matches:** file_cluster_10: 8.42, file_cluster_15: 9.567, file_cluster_13: 9.802
- **Magnitude:** 50.64 | **LOC:** 133 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 24.362; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Debt Markers (formerly Tech Debt) (85.9%), Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `ensureRuntimeStarted` **(Callbacks & Closures)** (Impact: 6.5)
  * `start` **(Callbacks & Closures)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 24`, `args: 6`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.362
  * `Choke Point (Betweenness):` 0.012821 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 11):` nodes, auth, util, comms, credentials, library, locales, projects...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/editor/library.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_10: 7.059, file_cluster_15: 9.066, file_cluster_9: 9.438
- **Magnitude:** 49.12 | **LOC:** 82 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 21.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (70.3%), Dead Code Surface (formerly Dead Code) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEntry` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* // getLibraryConfig: function(req,res) { // var opts = { // user: req.user, // library: req.params.i...
  * `saveEntry` **(Defensive Guards)** (Impact: 8.0)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 7.04)
- **Top Global Matches:** file_cluster_1: 7.04, file_cluster_3: 48.432, file_cluster_8: 70.203
- **Magnitude:** 44.04 | **LOC:** 102 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 24.362; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.2%), Guard Balance (formerly Safety Score) (50.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Dead Code Surface (formerly Dead Code) (30.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.362
  * `Choke Point (Betweenness):` 0.009259 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 9):` auth, util, context, diagnostics, flow, flows, nodes, plugins...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/context.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.195)
- **Top Global Matches:** file_cluster_10: 5.195, file_cluster_15: 8.59, file_cluster_2: 8.666
- **Magnitude:** 43.3 | **LOC:** 62 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (78.2%), Mutation Surface (formerly State Flux) (77.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Defensive Guards)** (Impact: 4.4)
  * `delete` **(Callbacks & Closures)** (Impact: 2.5)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/auth/permissions.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.159)
- **Top Global Matches:** file_cluster_1: 6.159, file_cluster_3: 48.3, file_cluster_8: 70.106
- **Magnitude:** 40.5 | **LOC:** 66 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 37.833; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (36.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hasPermission` **(Defensive Guards)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 14`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.164983
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/editor/sshkeys.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.554)
- **Top Global Matches:** file_cluster_10: 4.554, file_cluster_2: 8.319, file_cluster_13: 8.857
- **Magnitude:** 39.62 | **LOC:** 95 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 29.432; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (92.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `app` **(Callbacks & Closures)** (Impact: 4.4)
  * `init` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 14`, `func_start: 2`
* *Risk/State:* `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/flow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.614)
- **Top Global Matches:** file_cluster_10: 4.614, file_cluster_2: 8.516, file_cluster_13: 8.93
- **Magnitude:** 28.02 | **LOC:** 74 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Connectivity (formerly Api Exposure) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `put` **(Callbacks & Closures)** (Impact: 2.4)
  * `get` **(Callbacks & Closures)** (Impact: 2.3)
  * `post` **(Callbacks & Closures)** (Impact: 2.3)
  * `delete` **(Callbacks & Closures)** (Impact: 2.3)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 13`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/auth/clients.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.144)
- **Top Global Matches:** file_cluster_7: 7.144, file_cluster_12: 9.077, file_cluster_5: 9.885
- **Magnitude:** 24.88 | **LOC:** 32 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 26.723; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (91.7%), Complexity Load (formerly Cognitive Load) (58.5%), Guard Balance (formerly Safety Score) (55.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 2`, `concurrency: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.723
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.106754
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/editor/locales.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.724)
- **Top Global Matches:** file_cluster_12: 7.724, file_cluster_7: 8.527, file_cluster_10: 8.983
- **Magnitude:** 23.78 | **LOC:** 55 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 21.975; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (55.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (39.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Callbacks & Closures)** (Impact: 7.8)
  * `loadResource` **(Compute Cores)** (Impact: 5.7)
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/admin/diagnostics.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.887)
- **Top Global Matches:** file_cluster_10: 7.887, file_cluster_9: 8.328, file_cluster_15: 9.645
- **Magnitude:** 21.46 | **LOC:** 24 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 22.393; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getReport` **(Defensive Guards)** (Impact: 11.1)
  * `init` **(Callbacks & Closures)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.393
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/editor/settings.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.521)
- **Top Global Matches:** file_cluster_10: 4.521, file_cluster_2: 8.445, file_cluster_13: 8.739
- **Magnitude:** 17.02 | **LOC:** 48 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 21.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.9%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateUserSettings` **(Callbacks & Closures)** (Impact: 2.3)
  * `userSettings` **(Callbacks & Closures)** (Impact: 2.1)
  * `init` **(Callbacks & Closures)** (Impact: 1.9)
  * `sshkeys` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.975
  * `Choke Point (Betweenness):` 0.002849 | `Ripple Effect (Closeness):` 0.049383
  * `Imports (Out-Degree: 2):` util, sshkeys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/lib/auth/strategies.js` (JAVASCRIPT) | Magnitude: 134.28 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 116, branch: 31, structural_boundaries: 27, core_var_decl: 24

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/auth/index.js` -> **Severity: 2.776** (Bridge: 0.0278 * Flux: 99.9181%)
- `package/lib/editor/index.js` -> **Severity: 1.228** (Bridge: 0.0128 * Flux: 95.7598%)
- `package/lib/auth/strategies.js` -> **Severity: 0.854** (Bridge: 0.0085 * Flux: 99.8804%)
- `package/lib/admin/index.js` -> **Severity: 0.826** (Bridge: 0.0093 * Flux: 89.2461%)
- `package/lib/editor/comms.js` -> **Severity: 0.356** (Bridge: 0.0036 * Flux: 99.9961%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/util.js` -> **Severity: 35.207** (Embedded: 0.6 * Error Risk: 58.6784%)
- `package/lib/editor/theme.js` -> **Severity: 14.006** (Embedded: 0.1815 * Error Risk: 77.1762%)
- `package/lib/auth/tokens.js` -> **Severity: 10.356** (Embedded: 0.165 * Error Risk: 62.7706%)
- `package/lib/auth/users.js` -> **Severity: 9.756** (Embedded: 0.165 * Error Risk: 59.133%)
- `package/lib/auth/index.js` -> **Severity: 8.251** (Embedded: 0.1481 * Error Risk: 55.6953%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/util.js` -> **Severity: 28301.5** (Blast Radius: 283.015 * Doc Risk: 100.0%)
- `package/lib/editor/theme.js` -> **Severity: 4056.359** (Blast Radius: 56.789 * Doc Risk: 71.4286%)
- `package/lib/auth/permissions.js` -> **Severity: 3783.3** (Blast Radius: 37.833 * Doc Risk: 100.0%)
- `package/lib/auth/tokens.js` -> **Severity: 3783.3** (Blast Radius: 37.833 * Doc Risk: 100.0%)
- `package/lib/auth/users.js` -> **Severity: 3783.3** (Blast Radius: 37.833 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 605 call pairs -- scoped 20.7%, unique 0.0%, ambiguous 0.7%, external 78.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 605 | 20.7% | 0.0% | 0.7% | 78.7% |

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
