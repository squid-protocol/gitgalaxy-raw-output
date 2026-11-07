# ARCHITECTURAL_BRIEF: @node-red_runtime
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
- **Scope:** 61 analyzed artifact(s), 11965 LOC.
- **Load-bearing artifact:** `package/lib/storage/localfilesystem/util.js` -- 6 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/index.js` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/storage/localfilesystem/projects/Project.js` at magnitude 1395.12 (structural weight, not risk).
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
| Total Artifacts | 62 |
| Analyzed Artifacts (Scanned) | 61 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 11965 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.4% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6219 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3985 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8408 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 47 | 10119 | 77.0% |
| JSON | 10 | 1842 | 16.4% |
| SHELL | 2 | 4 | 3.3% |
| MARKDOWN | 1 | 0 | 1.6% |
| PLAINTEXT | 1 | 0 | 1.6% |

## 4.1 SOURCE ENCODINGS
All 61 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 28%, Data / Markup / Trivial 26%, Large Core Modules (2) 26%, Large Core Modules (3) 7%, State Mutators Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 59 | 96.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 3.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 44.3 | 48.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 73.9 | 45.5 | 55.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 13.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 24.8 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 68.8 | 21.2 | 16.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 56.7 | 86.3 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 66.5 | 99.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 96.0 | 11.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.2 | 60.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7 | 4 | 0 | `package/lib/nodes/context/index.js` |
| cleanup | 18 | 7 | 1 | `package/lib/storage/localfilesystem/projects/git/authServer.js` |
| guards | 775 | 38 | 38 | `package/lib/flows/util.js` |
| danger | 199 | 26 | 13 | `package/lib/api/nodes.js` |
| concurrency | 527 | 39 | 30 | `package/lib/storage/localfilesystem/projects/Project.js` |
| connectivity | 221 | 46 | 9 | `package/lib/api/projects.js` |
| io | 188 | 20 | 8 | `package/lib/nodes/context/localfilesystem.js` |
| crypto | 5 | 5 | 0 | `package/lib/index.js` |
| ipc | 4 | 2 | 0 | `package/lib/storage/localfilesystem/projects/ssh/keygen.js` |
| time | 18 | 6 | 0 | `package/lib/flows/Flow.js` |
| serialization | 42 | 16 | 2 | `package/lib/nodes/credentials.js` |
| regex | 34 | 13 | 1 | `package/lib/storage/localfilesystem/projects/git/index.js` |
| events | 129 | 17 | 8 | `package/lib/flows/index.js` |
| tests | 2 | 1 | 0 | `package/lib/settings.js` |
| docs | 233 | 42 | 13 | `package/lib/api/projects.js` |
| debt | 64 | 22 | 4 | `package/lib/storage/localfilesystem/projects/Project.js` |
| mutation | 3415 | 47 | 192 | `package/lib/storage/localfilesystem/projects/Project.js` |
| dead_code | 150 | 27 | 6 | `package/lib/storage/localfilesystem/projects/git/index.js` |
| credential | 3 | 3 | 0 | `package/locales/ja/runtime.json` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `package/lib/api/settings.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/nodes/context/localfilesystem.js` (Hits: 34)
- `package/lib/storage/localfilesystem/projects/Project.js` (Hits: 32)
- `package/lib/storage/localfilesystem/projects/ssh/index.js` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.js** (`package/lib/storage/localfilesystem/util.js`) — 6 inbound connections
2. **Flow.js** (`package/lib/flows/Flow.js`) — 5 inbound connections
3. **util.js** (`package/lib/flows/util.js`) — 5 inbound connections
4. **index.js** (`package/lib/nodes/context/index.js`) — 5 inbound connections
5. **memory.js** (`package/lib/nodes/context/memory.js`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/lib/index.js`) — 15 outbound dependencies
2. **index.js** (`package/lib/storage/localfilesystem/projects/index.js`) — 10 outbound dependencies
3. **index.js** (`package/lib/api/index.js`) — 9 outbound dependencies
4. **Subflow.js** (`package/lib/flows/Subflow.js`) — 9 outbound dependencies
5. **index.js** (`package/lib/nodes/index.js`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `diffConfigs` **(Many-Argument Workhorses)** (@ `package/lib/flows/util.js`) -> Impact: **205.3** | LOC: 330
- `createContext` **(Many-Argument Workhorses)** (@ `package/lib/nodes/context/index.js`) -> Impact: **142.7** | LOC: 213
- `start` **(Compute Cores)** (@ `package/lib/flows/Flow.js`) -> Impact: **111.8** | LOC: 200
  * *Intent:* /** * Start this flow. * The `diff` argument helps define what needs to be started in the case * of a modified-nodes/flows type deploy. */
- `update` **(Many-Argument Workhorses)** (@ `package/lib/storage/localfilesystem/projects/Project.js`) -> Impact: **100.4** | LOC: 207
- `start` **(Many-Argument Workhorses)** (@ `package/lib/flows/index.js`) -> Impact: **97.5** | LOC: 161
- `runGitCommand` **(Many-Argument Workhorses)** (@ `package/lib/storage/localfilesystem/projects/git/index.js`) -> Impact: **90.0** | LOC: 56
- `handleError` **(Many-Argument Workhorses)** (@ `package/lib/flows/Flow.js`) -> Impact: **83.3** | LOC: 100
  * *Intent:* /** * Handle an error event from a node within this flow. If there are no Catch * nodes within this flow, pass the event to the parent flow. */
- `parseConfig` **(Defensive Guards)** (@ `package/lib/flows/util.js`) -> Impact: **78.0** | LOC: 118
- `start` **(Defensive Guards)** (@ `package/lib/flows/Subflow.js`) -> Impact: **73.4** | LOC: 167
  * *Intent:* /** * Start the subflow. * This creates a subflow instance node to handle the inbound messages. It also * rewires an subflow internal node that is con...
- `stop` **(Many-Argument Workhorses)** (@ `package/lib/flows/index.js`) -> Impact: **64.4** | LOC: 81

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib/flows` | 5 | 3006.2 | 71.5% | 6.52% |
| `package/lib/storage/localfilesystem/projects` | 3 | 2044.42 | 77.06% | 10.54% |
| `package/lib/api` | 10 | 1551.84 | 40.53% | 14.93% |
| `package/lib/nodes/context` | 3 | 1430.86 | 98.08% | 2.75% |
| `package/lib/nodes` | 3 | 1175.08 | 62.2% | 15.08% |
| `package/lib/storage/localfilesystem/projects/git` | 6 | 640.2 | 34.83% | 3.76% |
| `package/lib/storage/localfilesystem` | 5 | 419.38 | 59.83% | 18.98% |
| `package/lib` | 3 | 409.04 | 33.29% | 35.4% |
| `package/lib/storage/localfilesystem/projects/ssh` | 2 | 235.2 | 84.2% | 0.0% |
| `package/lib/storage` | 1 | 233.58 | 94.12% | 95.5% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/api/index.js` -> **97.0688%** Exposure
- `package/lib/index.js` -> **96.0573%** Exposure
- `package/lib/storage/index.js` -> **95.5022%** Exposure
- `package/lib/storage/localfilesystem/index.js` -> **76.6477%** Exposure
- `package/lib/telemetry/index.js` -> **38.07%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/api/settings.js` -> **100.0%** Exposure
- `package/lib/flows/Flow.js` -> **100.0%** Exposure
- `package/lib/flows/Subflow.js` -> **100.0%** Exposure
- `package/lib/flows/index.js` -> **100.0%** Exposure
- `package/lib/flows/util.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/index.js` -> **6** Orphaned Functions | **2** Duplicates
- `package/lib/storage/index.js` -> **6** Orphaned Functions | **0** Duplicates
- `package/lib/flows/index.js` -> **5** Orphaned Functions | **0** Duplicates
- `package/lib/api/index.js` -> **3** Orphaned Functions | **0** Duplicates
- `package/lib/telemetry/index.js` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `96` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/storage/localfilesystem/projects/Project.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.759)
- **Top Global Matches:** file_cluster_4: 7.759, file_cluster_10: 9.907, file_cluster_15: 10.325
- **Magnitude:** 1395.12 | **LOC:** 1081 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 13.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `status` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `createProject` **(Compute Cores)** (Impact: 34.8)
  * `createDefaultProject` **(Compute Cores)** (Impact: 29.1)
  * `resolveMerge` **(Defensive Guards)** (Impact: 28.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 55 instances
* *Amplified Cascading Flux:* 163 instances
* *Concurrency (weighted view):* 352
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 251`, `args: 119`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 214`, `dead_code: 19`, `planned_debt: 9`
* *Architecture:* `io: 32`, `api: 23`, `concurrency: 77`, `import: 10`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 13.55
  * `Choke Point (Betweenness):` 0.00226 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 5):` util, defaultFileSet, git, authCache, ssh, util, fs-extra, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/flows/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.467)
- **Top Global Matches:** file_cluster_8: 7.467, file_cluster_6: 13.444, file_cluster_4: 21.858
- **Magnitude:** 858.92 | **LOC:** 740 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 32.846; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Concurrency Surface (formerly Concurrency) (87.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diffConfigs` **(Many-Argument Workhorses)** (Impact: 205.3)
  * `parseConfig` **(Defensive Guards)** (Impact: 78.0)
  * `evaluateEnvProperties` **(Defensive Guards)** (Impact: 43.3)
  * `createNode` **(Defensive Guards)** (Impact: 35.0)
    * *Intent:* /** * Create a new instance of a node */
  * `mapEnvVarProperties` **(Defensive Guards)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 118 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 105`, `args: 26`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 131`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 70`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.846
  * `Choke Point (Betweenness):` 0.002119 | `Ripple Effect (Closeness):` 0.090741
  * `Imports (Out-Degree: 1):` Subflow, registry, util, rfdc
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/flows/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.625)
- **Top Global Matches:** file_cluster_6: 8.625, file_cluster_8: 10.142, file_cluster_4: 16.111
- **Magnitude:** 823.54 | **LOC:** 877 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 17.697; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Many-Argument Workhorses)** (Impact: 97.5)
  * `stop` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `setFlows` **(Many-Argument Workhorses)** (Impact: 61.8)
    * *Intent:* /* * _config - new node array configuration * _credentials - new credentials configuration (optional...
  * `updateFlow` **(Defensive Guards)** (Impact: 43.4)
  * `getFlow` **(Defensive Guards)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 99 instances
* *Concurrency (weighted view):* 90
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 156`, `args: 55`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 109`, `planned_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 2`, `concurrency: 25`, `import: 8`
* *Defense:* `safety: 51`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.697
  * `Choke Point (Betweenness):` 0.000565 | `Ripple Effect (Closeness):` 0.054444
  * `Imports (Out-Degree: 4):` context, credentials, Flow, util, registry, util, rfdc
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/flows/Flow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.911)
- **Top Global Matches:** file_cluster_6: 6.911, file_cluster_4: 9.667, file_cluster_8: 16.585
- **Magnitude:** 795.76 | **LOC:** 868 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 27.531; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.9%)
- **Documentation Coverage:** 36.5854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Compute Cores)** (Impact: 111.8)
    * *Intent:* /** * Start this flow. * The `diff` argument helps define what needs to be started in the case * of ...
  * `handleError` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* /** * Handle an error event from a node within this flow. If there are no Catch * nodes within this ...
  * `handleStatus` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* /** * Handle a status event from a node within this flow. * This could be a subflow instance node wh...
  * `getNode` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* /** * Get a node instance from this flow. If the node is not known to this * flow, pass the request ...
  * `stop` **(Defensive Guards)** (Impact: 18.0)
    * *Intent:* /** * Stop this flow. * The `stopList` argument helps define what needs to be stopped in the case * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 70
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 114`, `args: 48`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 105`, `dead_code: 6`
* *Architecture:* `api: 15`, `concurrency: 15`, `import: 9`
* *Defense:* `safety: 66`, `doc: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.531
  * `Choke Point (Betweenness):` 0.003766 | `Ripple Effect (Closeness):` 0.081667
  * `Imports (Out-Degree: 6):` context, credentials, Group, Subflow, util, util, clone
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/nodes/context/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.302)
- **Top Global Matches:** file_cluster_6: 6.302, file_cluster_4: 10.714, file_cluster_8: 15.115
- **Magnitude:** 743.24 | **LOC:** 656 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 30.491; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (60.1%)
- **Documentation Coverage:** 88.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContext` **(Many-Argument Workhorses)** (Impact: 142.7)
  * `value` **(Defensive Guards)** (Impact: 62.3)
  * `value` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `load` **(Defensive Guards)** (Impact: 37.7)
  * `value` **(Defensive Guards)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 112`, `args: 34`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 89`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 61`, `doc: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.491
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.088889
  * `Imports (Out-Degree: 1):` , memory, util, clone
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/storage/localfilesystem/projects/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.77)
- **Top Global Matches:** file_cluster_4: 7.77, file_cluster_15: 8.127, file_cluster_10: 8.549
- **Magnitude:** 619.68 | **LOC:** 717 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 14.67; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `saveFlows` **(Defensive Guards)** (Impact: 27.9)
  * `updateProject` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `getFlows` **(I/O & Config Routines)** (Impact: 19.2)
  * `createProject` **(Compute Cores)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 90
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 144`, `args: 78`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`, `dead_code: 2`, `planned_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 2`, `concurrency: 40`, `import: 11`
* *Defense:* `safety: 26`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.67
  * `Choke Point (Betweenness):` 0.005932 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 5):` settings, util, Project, git, ssh, util, crypto, fs-extra...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/nodes/Node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.601)
- **Top Global Matches:** file_cluster_4: 8.601, file_cluster_9: 9.115, file_cluster_10: 9.787
- **Magnitude:** 589.18 | **LOC:** 689 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 18.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (86.8%), Guard Balance (formerly Safety Score) (68.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 10.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Defensive Guards)** (Impact: 42.4)
    * *Intent:* /** * Send a message to the nodes wired. * * */
  * `removeListener` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* /** * Remove a listener for an event */
  * `logUnexpectedError` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `close` **(Defensive Guards)** (Impact: 21.4)
    * *Intent:* /** * Called when the node is being stopped */
  * `log_helper` **(Many-Argument Workhorses)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 93 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 70`, `args: 36`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 105`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 7`
* *Defense:* `safety: 53`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.829
  * `Choke Point (Betweenness):` 0.001224 | `Ripple Effect (Closeness):` 0.058333
  * `Imports (Out-Degree: 4):` flows, context, util, events, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/nodes/context/localfilesystem.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.04)
- **Top Global Matches:** file_cluster_4: 9.04, file_cluster_10: 9.642, file_cluster_15: 10.814
- **Magnitude:** 509.04 | **LOC:** 428 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 11.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Defensive Guards)** (Impact: 47.6)
  * `get` **(Defensive Guards)** (Impact: 22.2)
  * `getBasePath` **(Defensive Guards)** (Impact: 18.4)
  * `open` **(Callbacks & Closures)** (Impact: 17.4)
  * `clean` **(Callbacks & Closures)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 60 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 95`, `args: 50`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 67`
* *Architecture:* `io: 34`, `api: 5`, `concurrency: 34`, `import: 6`
* *Defense:* `safety: 38`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` memory, util, fs-extra, json-stringify-safe, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/storage/localfilesystem/projects/git/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.548)
- **Top Global Matches:** file_cluster_6: 8.548, file_cluster_8: 13.351, file_cluster_4: 14.264
- **Magnitude:** 506.8 | **LOC:** 663 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 15.854; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (79.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runGitCommand` **(Many-Argument Workhorses)** (Impact: 90.0)
  * `parseFilenames` **(Defensive Guards)** (Impact: 31.6)
  * `runGitCommandWithSSHCommand` **(Callbacks & Closures)** (Impact: 3.4)
  * `runGitCommandWithAuth` **(Callbacks & Closures)** (Impact: 3.1)
  * `cleanFilename` **(Defensive Guards)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 151`, `args: 69`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 136`, `dead_code: 29`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `api: 1`, `concurrency: 32`, `import: 5`
* *Defense:* `safety: 37`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.854
  * `Choke Point (Betweenness):` 0.001412 | `Ripple Effect (Closeness):` 0.037879
  * `Imports (Out-Degree: 1):` authServer, util, clone, path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/flows/Subflow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.319)
- **Top Global Matches:** file_cluster_6: 6.319, file_cluster_4: 10.425, file_cluster_8: 15.295
- **Magnitude:** 472.98 | **LOC:** 569 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 42.874; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (57.0%)
- **Documentation Coverage:** 21.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Defensive Guards)** (Impact: 73.4)
    * *Intent:* /** * Start the subflow. * This creates a subflow instance node to handle the inbound messages. It a...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* /** * Create a Subflow object. * This takes a subflow definition and instance node, creates a clone ...
  * `remapSubflowNodes` **(Defensive Guards)** (Impact: 32.8)
    * *Intent:* /** * Given an object of {id:nodes} and a map of {old-id:node}, modifiy all * properties in the node...
  * `getSetting` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* /** * Get environment variable of subflow */
  * `updateWires` **(Compute Cores)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 80`, `args: 29`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`, `dead_code: 6`
* *Architecture:* `api: 9`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 32`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.874
  * `Choke Point (Betweenness):` 0.004237 | `Ripple Effect (Closeness):` 0.068056
  * `Imports (Out-Degree: 6):` Node, context, credentials, Flow, util, util, clone, rfdc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/nodes/credentials.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.687)
- **Top Global Matches:** file_cluster_4: 8.687, file_cluster_6: 9.151, file_cluster_10: 14.503
- **Magnitude:** 435.08 | **LOC:** 496 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 32.846; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.9%), Complexity Load (formerly Cognitive Load) (74.2%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Defensive Guards)** (Impact: 59.4)
    * *Intent:* /** * Sets the credentials from storage. */
  * `extract` **(Defensive Guards)** (Impact: 57.0)
    * *Intent:* /** * Extracts and stores any credential updates in the provided node. * The provided node may have ...
  * `clean` **(Callbacks & Closures)** (Impact: 9.5)
    * *Intent:* /** * Deletes any credentials for nodes that no longer exist */
  * `export` **(Callbacks & Closures)** (Impact: 7.3)
  * `add` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /** * Adds a set of credentials for the given node id. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 75`, `args: 21`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `planned_debt: 4`
* *Architecture:* `api: 13`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 38`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.09697
  * `Imports (Out-Degree: 0):` crypto
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/api/nodes.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.537)
- **Top Global Matches:** file_cluster_4: 8.537, file_cluster_10: 9.18, file_cluster_15: 10.456
- **Magnitude:** 324.08 | **LOC:** 493 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 10.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addModule` **(Defensive Guards)** (Impact: 36.2)
    * *Intent:* /** * Install a new module into the runtime */
  * `putNode` **(Defensive Guards)** (Impact: 11.1)
  * `setNodeSetState` **(Defensive Guards)** (Impact: 10.3)
    * *Intent:* /** * Enables or disables a n individual node-set in the runtime */
  * `setModuleState` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* /** * Enables or disables a module in the runtime */
  * `removeModule` **(Defensive Guards)** (Impact: 8.6)
    * *Intent:* /** * Removes a module from the runtime */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 79`, `args: 33`, `func_start: 16`
* *Risk/State:* `state_mutation: 48`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 13`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 19`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` fs-extra
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/api/settings.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.39)
- **Top Global Matches:** file_cluster_6: 8.39, file_cluster_8: 13.149, file_cluster_4: 14.213
- **Magnitude:** 313.84 | **LOC:** 330 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.0%), Connectivity (formerly Api Exposure) (50.1%)
- **Documentation Coverage:** 17.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRuntimeSettings` **(Defensive Guards)** (Impact: 60.5)
    * *Intent:* /** * Gets the runtime settings object */
  * `extend` **(Defensive Guards)** (Impact: 29.3)
  * `updateUserSettings` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* /** * Updates an individual user's settings object. */
  * `getUserSettings` **(Callbacks & Closures)** (Impact: 7.5)
    * *Intent:* /** * Gets an individual user's settings object */
  * `getUserKey` **(Callbacks & Closures)** (Impact: 6.6)
    * *Intent:* /** * Gets a user's ssh public key */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 35`, `args: 18`, `func_start: 10`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 8`, `concurrency: 14`, `import: 1`
* *Defense:* `safety: 28`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.794)
- **Top Global Matches:** file_cluster_4: 8.794, file_cluster_12: 9.243, file_cluster_10: 9.357
- **Magnitude:** 261.06 | **LOC:** 452 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 11.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Defensive Guards)** (Impact: 45.8)
    * *Intent:* /** * Start the runtime. * flows will be running as they are started asynchronously. */
  * `init` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* /** * Initialise the runtime module. * better abstracted. */
  * `reinstallModules` **(Callbacks & Closures)** (Impact: 11.5)
  * `stop` **(Callbacks & Closures)** (Impact: 3.6)
    * *Intent:* /** * Stops the runtime. * * Once called, Node-RED should not be restarted until the Node.JS process...
  * `getVersion` **(Defensive Guards)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 68`, `args: 42`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 18`, `import: 17`
* *Defense:* `safety: 16`, `doc: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` api, flows, library, multiplayer, nodes, plugins, settings, storage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/storage/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.921)
- **Top Global Matches:** file_cluster_10: 6.921, file_cluster_12: 7.653, file_cluster_15: 8.507
- **Magnitude:** 233.58 | **LOC:** 233 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 11.996; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.5%), Complexity Load (formerly Cognitive Load) (94.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listFlows` **(Callbacks & Closures)** (Impact: 13.0)
  * `init` **(Defensive Guards)** (Impact: 12.4)
  * `moduleSelector` **(Defensive Guards)** (Impact: 7.8)
  * `saveFlow` **(Compute Cores)** (Impact: 7.6)
  * `getFlow` **(Callbacks & Closures)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 54`, `args: 26`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 22`, `import: 6`
* *Defense:* `safety: 5`, `doc: 1`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.996
  * `Choke Point (Betweenness):` 0.003672 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 1):` , localfilesystem, util, async-mutex, crypto, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/api/context.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.023)
- **Top Global Matches:** file_cluster_3: 8.023, file_cluster_8: 21.187, file_cluster_6: 33.889
- **Magnitude:** 227.46 | **LOC:** 311 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (96.0%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.0%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getValue` **(Defensive Guards)** (Impact: 63.2)
    * *Intent:* /** * Gets the info of an individual node set */
  * `exportContextStore` **(Defensive Guards)** (Impact: 30.9)
  * `delete` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* /** * Gets the info of an individual node set */
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 51`, `args: 16`, `func_start: 4`
* *Risk/State:* `state_mutation: 37`, `dead_code: 20`, `planned_debt: 4`
* *Architecture:* `api: 4`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 22`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/api/flows.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.808)
- **Top Global Matches:** file_cluster_4: 9.808, file_cluster_12: 11.602, file_cluster_10: 12.657
- **Magnitude:** 223.78 | **LOC:** 337 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (55.5%), Connectivity (formerly Api Exposure) (52.3%)
- **Documentation Coverage:** 15.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setState` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* /** * Sets running state of runtime flows */
  * `getNodeCredentials` **(Defensive Guards)** (Impact: 22.8)
    * *Intent:* /** * Gets the safe credentials for a node */
  * `makeError` **(Defensive Guards)** (Impact: 20.6)
  * `setFlows` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* /** * Sets the current flow configuration */
  * `updateFlow` **(Callbacks & Closures)** (Impact: 6.9)
    * *Intent:* /** * Updates an existing flow configuration */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 46`, `args: 24`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`, `planned_debt: 3`
* *Architecture:* `api: 9`, `concurrency: 23`, `import: 1`
* *Defense:* `safety: 24`, `doc: 13`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` async-mutex
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/nodes/context/memory.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.127)
- **Top Global Matches:** file_cluster_10: 7.127, file_cluster_15: 8.735, file_cluster_16: 9.319
- **Magnitude:** 178.58 | **LOC:** 174 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 60.345; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (60.7%), Concurrency Surface (formerly Concurrency) (56.8%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Defensive Guards)** (Impact: 23.9)
  * `keys` **(Defensive Guards)** (Impact: 22.3)
  * `get` **(Defensive Guards)** (Impact: 21.9)
  * `clean` **(Defensive Guards)** (Impact: 7.6)
  * `_getOne` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 29`, `args: 12`, `func_start: 11`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `api: 6`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 20`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.104167
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/storage/localfilesystem/library.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.975)
- **Top Global Matches:** file_cluster_12: 7.975, file_cluster_9: 9.78, file_cluster_15: 10.014
- **Magnitude:** 167.6 | **LOC:** 176 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 14.67; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLibraryEntry` **(Defensive Guards)** (Impact: 21.9)
  * `saveLibraryEntry` **(Defensive Guards)** (Impact: 18.9)
  * `getFileMeta` **(Compute Cores)** (Impact: 13.7)
  * `getFileBody` **(Compute Cores)** (Impact: 9.4)
  * `init` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 54`, `args: 14`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 20`
* *Architecture:* `io: 14`, `api: 3`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 1):` util, fs-extra, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/storage/localfilesystem/projects/ssh/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.253)
- **Top Global Matches:** file_cluster_10: 7.253, file_cluster_15: 8.37, file_cluster_12: 8.642
- **Magnitude:** 152.7 | **LOC:** 213 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 15.854; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listSSHKeysInDir` **(Defensive Guards)** (Impact: 19.4)
  * `generateSSHKey` **(Compute Cores)** (Impact: 16.8)
  * `getPrivateKeyPath` **(Defensive Guards)** (Impact: 7.8)
  * `checkFilePairExist` **(Compute Cores)** (Impact: 5.5)
  * `init` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 67`, `args: 34`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 1`, `concurrency: 19`, `import: 4`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.854
  * `Choke Point (Betweenness):` 0.001412 | `Ripple Effect (Closeness):` 0.037879
  * `Imports (Out-Degree: 1):` keygen, util, fs-extra, path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/nodes/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.732)
- **Top Global Matches:** file_cluster_15: 7.732, file_cluster_10: 7.926, file_cluster_9: 8.248
- **Magnitude:** 150.82 | **LOC:** 272 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 11.996; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (77.9%), Complexity Load (formerly Cognitive Load) (64.2%)
- **Documentation Coverage:** 38.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `registerType` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /** * Registers a node constructor */
  * `reportNodeStateChange` **(Defensive Guards)** (Impact: 16.2)
  * `createNode` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* /** * Called from a Node's constructor function, invokes the super-class * constructor and attaches ...
  * `installModule` **(Compute Cores)** (Impact: 10.8)
  * `registerSubflow` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 32`, `args: 15`, `func_start: 9`
* *Risk/State:* `state_mutation: 18`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 9`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.996
  * `Choke Point (Betweenness):` 0.000565 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 6):` flows, util, Node, context, credentials, registry, util, rfdc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/telemetry/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.036)
- **Top Global Matches:** file_cluster_10: 7.036, file_cluster_15: 8.496, file_cluster_2: 9.106
- **Magnitude:** 150.68 | **LOC:** 213 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 11.996; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (65.4%), Guard Balance (formerly Safety Score) (55.3%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(I/O & Config Routines)** (Impact: 14.5)
  * `gather` **(Defensive Guards)** (Impact: 10.6)
  * `isTelemetryEnabled` **(Defensive Guards)** (Impact: 8.0)
  * `init` **(Callbacks & Closures)** (Impact: 3.2)
  * `startTelemetry` **(Callbacks & Closures)** (Impact: 2.9)
    * *Intent:* /** * Start the telemetry schedule */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 33`, `args: 15`, `func_start: 10`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 8`, `import: 6`
* *Defense:* `safety: 17`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 0):` cronosjs, promises, got, path, semver
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/settings.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.929)
- **Top Global Matches:** file_cluster_10: 6.929, file_cluster_12: 8.368, file_cluster_15: 8.721
- **Magnitude:** 143.64 | **LOC:** 191 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 11.996; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (53.3%), Complexity Load (formerly Cognitive Load) (50.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exportNodeSettings` **(Compute Cores)** (Impact: 18.1)
  * `init` **(Defensive Guards)** (Impact: 12.2)
  * `set` **(Defensive Guards)** (Impact: 7.9)
  * `registerNodeSettings` **(Compute Cores)** (Impact: 7.5)
  * `load` **(Callbacks & Closures)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 38`, `args: 19`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 16`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.996
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016667
  * `Imports (Out-Degree: 0):` util, assert, clone
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/api/projects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.442)
- **Top Global Matches:** file_cluster_10: 5.442, file_cluster_15: 9.251, file_cluster_2: 9.319
- **Magnitude:** 139.9 | **LOC:** 491 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 3.1746% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setActiveProject` **(Defensive Guards)** (Impact: 4.6)
    * *Intent:* /** * */
  * `listProjects` **(Callbacks & Closures)** (Impact: 3.6)
    * *Intent:* /** * List projects known to the runtime */
  * `getCommits` **(Callbacks & Closures)** (Impact: 3.1)
    * *Intent:* /** * Gets the commit history of the project */
  * `createProject` **(Callbacks & Closures)** (Impact: 3.0)
    * *Intent:* /** * Create a new project */
  * `initialiseProject` **(Callbacks & Closures)** (Impact: 1.7)
    * *Intent:* /** * Initialises an empty project */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 40`, `args: 34`, `func_start: 32`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 32`, `concurrency: 33`
* *Defense:* `safety: 2`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/api/diagnostics.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.97)
- **Top Global Matches:** file_cluster_4: 7.97, file_cluster_6: 9.73, file_cluster_10: 13.191
- **Magnitude:** 123.06 | **LOC:** 213 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 12.19; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.7%), Mutation Surface (formerly State Flux) (88.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.2%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildDiagnosticReport` **(Many-Argument Workhorses)** (Impact: 60.0)
  * `hasDockerCGroup` **(Defensive Guards)** (Impact: 6.7)
  * `getIsInWSL` **(Defensive Guards)** (Impact: 5.8)
  * `get` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* /** * Gets the node-red diagnostics report */
  * `isInContainer` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 24`, `args: 12`, `func_start: 9`
* *Risk/State:* `state_mutation: 8`, `dead_code: 7`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 11`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 0):` fs, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/storage/localfilesystem/index.js` -> **Severity: 0.677** (Bridge: 0.0068 * Flux: 99.7816%)
- `package/lib/storage/localfilesystem/projects/index.js` -> **Severity: 0.593** (Bridge: 0.0059 * Flux: 99.9996%)
- `package/lib/flows/Subflow.js` -> **Severity: 0.424** (Bridge: 0.0042 * Flux: 100.0%)
- `package/lib/flows/Flow.js` -> **Severity: 0.377** (Bridge: 0.0038 * Flux: 100.0%)
- `package/lib/storage/index.js` -> **Severity: 0.367** (Bridge: 0.0037 * Flux: 99.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/nodes/credentials.js` -> **Severity: 6.644** (Embedded: 0.097 * Error Risk: 68.5115%)
- `package/lib/flows/util.js` -> **Severity: 6.341** (Embedded: 0.0907 * Error Risk: 69.8852%)
- `package/lib/nodes/context/memory.js` -> **Severity: 6.328** (Embedded: 0.1042 * Error Risk: 60.7445%)
- `package/lib/nodes/context/index.js` -> **Severity: 5.341** (Embedded: 0.0889 * Error Risk: 60.0909%)
- `package/lib/flows/Flow.js` -> **Severity: 4.972** (Embedded: 0.0817 * Error Risk: 60.8799%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/nodes/context/memory.js` -> **Severity: 5699.247** (Blast Radius: 60.345 * Doc Risk: 94.4444%)
- `package/lib/storage/localfilesystem/util.js` -> **Severity: 2949.8** (Blast Radius: 58.996 * Doc Risk: 50.0%)
- `package/lib/nodes/context/index.js` -> **Severity: 2700.631** (Blast Radius: 30.491 * Doc Risk: 88.5714%)
- `package/lib/flows/util.js` -> **Severity: 2554.69** (Blast Radius: 32.846 * Doc Risk: 77.7778%)
- `package/lib/storage/localfilesystem/projects/git/authServer.js` -> **Severity: 2453.3** (Blast Radius: 24.533 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1920 call pairs -- scoped 16.4%, unique 0.0%, ambiguous 3.2%, external 80.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1919 | 16.4% | 0.0% | 3.2% | 80.5% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
