# ARCHITECTURAL_BRIEF: @nx_node
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
- **Scope:** 61 analyzed artifact(s), 2111 LOC.
- **Load-bearing artifact:** `package/src/generators/application/lib/normalized-schema.js` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/generators/e2e-project/e2e-project.js` -- pulls in 13 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/generators/application/application.js` at magnitude 181.54 (structural weight, not risk).
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
| Total Artifacts | 108 |
| Analyzed Artifacts (Scanned) | 61 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 47 |
| Total LOC | 2111 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5972 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3565 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8218 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 26 | 195 | 42.6% |
| JAVASCRIPT | 21 | 1313 | 34.4% |
| JSON | 12 | 603 | 19.7% |
| MARKDOWN | 1 | 0 | 1.6% |
| PLAINTEXT | 1 | 0 | 1.6% |

## 4.1 SOURCE ENCODINGS
All 61 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 54%, Declarative / Non-Code 18%, Large Core Modules (2) 15%, Large Core Modules (3) 3%, Callbacks & Closures Files 2%
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
*Total Excluded Artifacts: 47*

**Composition by Extension & Reason:**
- `.map`: 18x Unresolved Ambiguity (No Retainable Structure), 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.ts__tmpl__`: 19x Excluded (Unsupported Extension: '.ts__tmpl__')
- `no_extension`: 3x Excluded (Unsupported Extension: '.json__tmpl__'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.js__tmpl__`: 1x Excluded (Unsupported Extension: '.js__tmpl__')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 14.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 61.2 | 18.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 10.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 5.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 1 | 1 | 0 | `package/src/utils/wait-for-port-open.js` |
| guards | 93 | 13 | 6 | `package/src/generators/e2e-project/e2e-project.js` |
| danger | 10 | 9 | 1 | `package/src/generators/setup-docker/setup-docker.js` |
| concurrency | 74 | 19 | 3 | `package/src/generators/application/application.js` |
| connectivity | 126 | 45 | 4 | `package/src/utils/versions.js` |
| io | 12 | 5 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 2 | 0 | `package/src/utils/kill-port.js` |
| serialization | 5 | 3 | 0 | `package/src/generators/application/lib/add-proxy.js` |
| regex | 8 | 5 | 0 | `package/src/generators/setup-docker/setup-docker.js` |
| events | 13 | 3 | 0 | `package/src/utils/wait-for-port-open.js` |
| tests | 20 | 3 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| docs | 13 | 8 | 1 | `package/src/utils/wait-for-port-open.d.ts` |
| debt | 2 | 1 | 0 | `package/src/generators/e2e-project/e2e-project.js` |
| mutation | 307 | 22 | 13 | `package/src/generators/e2e-project/e2e-project.js` |
| dead_code | 19 | 15 | 1 | `package/src/generators/application/lib/create-targets.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/generators/e2e-project/e2e-project.js` (Hits: 7)
- `package/src/generators/setup-docker/setup-docker.js` (Hits: 2)
- `package/src/generators/application/lib/create-files.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **normalized-schema.js** (`package/src/generators/application/lib/normalized-schema.js`) — 9 inbound connections
2. **versions.js** (`package/src/utils/versions.js`) — 5 inbound connections
3. **init.js** (`package/src/generators/init/init.js`) — 4 inbound connections
4. **create-targets.js** (`package/src/generators/application/lib/create-targets.js`) — 3 inbound connections
5. **application.js** (`package/src/generators/application/application.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **e2e-project.js** (`package/src/generators/e2e-project/e2e-project.js`) — 13 outbound dependencies
2. **application.js** (`package/src/generators/application/application.js`) — 12 outbound dependencies
3. **library.js** (`package/src/generators/library/library.js`) — 11 outbound dependencies
4. **index.js** (`package/src/generators/application/lib/index.js`) — 9 outbound dependencies
5. **index.d.ts** (`package/src/generators/application/lib/index.d.ts`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `e2eProjectGeneratorInternal` **(Many-Argument Workhorses)** (@ `package/src/generators/e2e-project/e2e-project.js`) -> Impact: **78.8** | LOC: 190
- `applicationGeneratorInternal` **(Many-Argument Workhorses)** (@ `package/src/generators/application/application.js`) -> Impact: **50.4** | LOC: 141
- `addProject` **(Many-Argument Workhorses)** (@ `package/src/generators/application/lib/create-project.js`) -> Impact: **32.4** | LOC: 48
- `normalizeOptions` **(Defensive Guards)** (@ `package/src/generators/application/lib/normalize-options.js`) -> Impact: **31.6** | LOC: 44
- `updateProject` **(Defensive Guards)** (@ `package/src/generators/library/library.js`) -> Impact: **26.0** | LOC: 36
- `libraryGeneratorInternal` **(Compute Cores)** (@ `package/src/generators/library/library.js`) -> Impact: **25.2** | LOC: 53
- `addDocker` **(Defensive Guards)** (@ `package/src/generators/setup-docker/setup-docker.js`) -> Impact: **23.1** | LOC: 46
- `addAppFiles` **(Defensive Guards)** (@ `package/src/generators/application/lib/create-files.js`) -> Impact: **19.4** | LOC: 42
- `waitForPortOpen` **(Defensive Guards)** (@ `package/src/utils/wait-for-port-open.js`) -> Impact: **17.4** | LOC: 37
  * *Intent:* /** * Waits for the given port to be open */
- `normalizeOptions` **(Defensive Guards)** (@ `package/src/generators/library/library.js`) -> Impact: **17.3** | LOC: 34

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/generators/application/lib` | 18 | 233.22 | 12.17% | 18.14% |
| `package/src/generators/application` | 4 | 200.61 | 30.58% | 9.44% |
| `package/src/utils` | 10 | 190.09 | 17.99% | 15.1% |
| `package/src/generators/e2e-project` | 4 | 175.88 | 18.33% | 12.24% |
| `package/src/generators/library` | 4 | 167.71 | 23.38% | 9.44% |
| `package/src/generators/setup-docker` | 4 | 115.15 | 19.49% | 9.44% |
| `package` | 9 | 86.92 | 0.0% | 0.0% |
| `package/src/generators/init` | 4 | 48.7 | 24.54% | 0.0% |
| `package/src/generators/application/files/common` | 2 | 29.88 | 0.0% | 0.0% |
| `package/src/generators/library/files/ts-solution` | 1 | 15.4 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/generators/application/lib/create-targets.d.ts` -> **99.9447%** Exposure
- `package/src/generators/application/application.d.ts` -> **37.7541%** Exposure
- `package/src/generators/application/lib/add-dependencies.d.ts` -> **37.7541%** Exposure
- `package/src/generators/application/lib/add-linting.d.ts` -> **37.7541%** Exposure
- `package/src/generators/application/lib/add-proxy.d.ts` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/utils/kill-port.js` -> **100.0%** Exposure
- `package/src/utils/versions.js` -> **100.0%** Exposure
- `package/src/utils/vscode-debug-config.js` -> **100.0%** Exposure
- `package/src/generators/application/lib/create-project.js` -> **99.9866%** Exposure
- `package/src/generators/application/application.js` -> **99.9413%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/generators/application/lib/create-targets.d.ts` -> **5** Orphaned Functions | **0** Duplicates
- `package/src/generators/application/application.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/generators/application/lib/add-dependencies.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/generators/application/lib/add-linting.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/src/generators/application/lib/add-proxy.d.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `73` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/generators/application/application.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.045)
- **Top Global Matches:** file_cluster_8: 7.045, file_cluster_6: 17.275, file_cluster_3: 20.257
- **Magnitude:** 181.54 | **LOC:** 193 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 14.983; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (98.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applicationGeneratorInternal` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `updateTsConfigOptions` **(Compute Cores)** (Impact: 8.3)
  * `applicationGenerator` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 26`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 3`, `concurrency: 18`, `import: 12`
* *Defense:* `safety: 10`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.983
  * `Choke Point (Betweenness):` 0.004551 | `Ripple Effect (Closeness):` 0.025641
  * `Imports (Out-Degree: 5):` versions, e2e-project, init, setup-docker, lib, devkit, log-show-project-command, jest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/e2e-project/e2e-project.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.673)
- **Top Global Matches:** file_cluster_8: 7.673, file_cluster_6: 17.829, file_cluster_3: 20.151
- **Magnitude:** 158.26 | **LOC:** 243 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 12.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (92.9%), Complexity Load (formerly Cognitive Load) (58.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `e2eProjectGeneratorInternal` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `normalizeOptions` **(Defensive Guards)** (Impact: 11.7)
  * `e2eProjectGenerator` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 21`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 11`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 22`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023077
  * `Imports (Out-Degree: 1):` versions, devkit, project-name-and-root-utils, log-show-project-command, eslint, global-eslint-config, eslint-file, config-file...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/generators/library/library.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.122)
- **Top Global Matches:** file_cluster_15: 7.122, file_cluster_9: 7.415, file_cluster_16: 8.751
- **Magnitude:** 148.74 | **LOC:** 185 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 14.983; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateProject` **(Defensive Guards)** (Impact: 26.0)
  * `libraryGeneratorInternal` **(Compute Cores)** (Impact: 25.2)
  * `normalizeOptions` **(Defensive Guards)** (Impact: 17.3)
  * `createFiles` **(Defensive Guards)** (Impact: 6.0)
  * `updatePackageJson` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 18`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 11`, `import: 11`
* *Defense:* `safety: 12`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.983
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.025641
  * `Imports (Out-Degree: 2):` versions, init, devkit, project-name-and-root-utils, target-defaults-utils, js, sort-fields, add-swc-config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/setup-docker/setup-docker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.176)
- **Top Global Matches:** file_cluster_15: 6.176, file_cluster_10: 7.615, file_cluster_16: 8.423
- **Magnitude:** 98.24 | **LOC:** 104 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 12.111; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (66.6%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addDocker` **(Defensive Guards)** (Impact: 23.1)
  * `normalizeOptions` **(Defensive Guards)** (Impact: 9.1)
  * `updateProjectConfig` **(Compute Cores)** (Impact: 6.2)
  * `setupDockerGenerator` **(Parameter Forwarders)** (Impact: 4.0)
  * `sanitizeProjectName` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 5`, `import: 4`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023077
  * `Imports (Out-Degree: 0):` devkit, generators, fs, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/utils/vscode-debug-config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.73)
- **Top Global Matches:** file_cluster_9: 6.73, file_cluster_12: 11.762, file_cluster_16: 12.87
- **Magnitude:** 54.58 | **LOC:** 83 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 14.607; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (56.8%), Guard Balance (formerly Safety Score) (56.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addVSCodeDebugConfiguration` **(Defensive Guards)** (Impact: 16.5)
  * `findFreeDebugPort` **(Defensive Guards)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 5`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.607
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028846
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/utils/versions.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.034)
- **Top Global Matches:** file_cluster_7: 5.034, file_cluster_12: 8.031, file_cluster_5: 9.205
- **Magnitude:** 52.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 59.175; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`
* *Architecture:* `api: 24`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.175
  * `Choke Point (Betweenness):` 0.001499 | `Ripple Effect (Closeness):` 0.079882
  * `Imports (Out-Degree: 1):` package.json
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/src/generators/application/lib/create-project.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.455)
- **Top Global Matches:** file_cluster_9: 6.455, file_cluster_16: 12.71, file_cluster_15: 12.829
- **Magnitude:** 49.46 | **LOC:** 56 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 11.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (73.5%), Guard Balance (formerly Safety Score) (53.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addProject` **(Many-Argument Workhorses)** (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.866
  * `Choke Point (Betweenness):` 0.000416 | `Ripple Effect (Closeness):` 0.032051
  * `Imports (Out-Degree: 2):` has-webpack-plugin, create-targets, devkit, target-defaults-utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/utils/kill-port.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.006)
- **Top Global Matches:** file_cluster_12: 8.006, file_cluster_7: 8.548, file_cluster_5: 10.072
- **Magnitude:** 47.52 | **LOC:** 37 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 17.693; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.5%), Guard Balance (formerly Safety Score) (53.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `killPort` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /** * Kills the process on the given port */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 4`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025641
  * `Imports (Out-Degree: 0):` devkit, kill-port, tcp-port-used
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/application/lib/normalize-options.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 7.115)
- **Top Global Matches:** file_cluster_1: 7.115, file_cluster_3: 48.423, file_cluster_8: 70.191
- **Magnitude:** 46.6 | **LOC:** 51 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 11.866; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (80.4%), Concurrency Surface (formerly Concurrency) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeOptions` **(Defensive Guards)** (Impact: 31.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 4`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 12`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032051
  * `Imports (Out-Degree: 0):` devkit, project-name-and-root-utils, ts-solution-setup
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/application/lib/create-targets.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.095)
- **Top Global Matches:** file_cluster_15: 6.095, file_cluster_2: 7.099, file_cluster_13: 7.292
- **Magnitude:** 45.4 | **LOC:** 143 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 16.91; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (46.0%), Mutation Surface (formerly State Flux) (41.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEsBuildConfig` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `getWebpackBuildConfig` **(Many-Argument Workhorses)** (Impact: 9.3)
  * `getPruneTargets` **(Defensive Guards)** (Impact: 6.8)
  * `getServeConfig` **(I/O & Config Routines)** (Impact: 2.6)
  * `getNestWebpackBuildConfig` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 5`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041958
  * `Imports (Out-Degree: 0):` devkit, js, ts-solution-setup
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/src/generators/init/init.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.272)
- **Top Global Matches:** file_cluster_10: 6.272, file_cluster_13: 6.517, file_cluster_2: 8.539
- **Magnitude:** 32.24 | **LOC:** 23 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 23.898; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Complexity Load (formerly Cognitive Load) (87.7%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initGenerator` **(Callbacks & Closures)** (Impact: 5.7)
  * `updateDependencies` **(Annotated & Test Methods)** (Impact: 2.0)
  * `installTask` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.898
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.051282
  * `Imports (Out-Degree: 1):` versions, devkit
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/utils/wait-for-port-open.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.086)
- **Top Global Matches:** file_cluster_10: 8.086, file_cluster_15: 10.139, file_cluster_9: 10.383
- **Magnitude:** 26.64 | **LOC:** 48 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 17.693; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.1%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `waitForPortOpen` **(Defensive Guards)** (Impact: 17.4)
    * *Intent:* /** * Waits for the given port to be open */
  * `checkPort` **(Defensive Guards)** (Impact: 3.0)
  * `cleanupClient` **(Callbacks & Closures)** (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 7`, `args: 7`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 6`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.693
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025641
  * `Imports (Out-Degree: 0):` devkit, net
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/application/lib/create-files.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.07)
- **Top Global Matches:** file_cluster_9: 6.07, file_cluster_15: 12.319, file_cluster_16: 12.405
- **Magnitude:** 25.38 | **LOC:** 51 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 11.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (24.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAppFiles` **(Defensive Guards)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.866
  * `Choke Point (Betweenness):` 0.001249 | `Ripple Effect (Closeness):` 0.032051
  * `Imports (Out-Degree: 2):` has-webpack-plugin, vscode-debug-config, devkit, js, path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/generators/application/lib/add-proxy.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.858)
- **Top Global Matches:** file_cluster_9: 5.858, file_cluster_15: 12.018, file_cluster_16: 12.249
- **Magnitude:** 22.96 | **LOC:** 45 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 11.866; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (53.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (29.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addProxy` **(Compute Cores)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.866
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032051
  * `Imports (Out-Degree: 0):` devkit
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.736)
- **Top Global Matches:** file_cluster_7: 7.736, file_cluster_14: 10.487, file_cluster_5: 10.683
- **Magnitude:** 18.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` application, init, library
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/application/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.083)
- **Top Global Matches:** file_cluster_2: 2.083, file_cluster_17: 4.914, file_cluster_13: 6.27
- **Magnitude:** 17.76 | **LOC:** 139 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/library/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.077)
- **Top Global Matches:** file_cluster_2: 2.077, file_cluster_17: 4.912, file_cluster_13: 6.268
- **Magnitude:** 17.66 | **LOC:** 134 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_7: 7.67, file_cluster_14: 9.39, file_cluster_5: 10.984
- **Magnitude:** 16.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` kill-port, wait-for-port-open
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/e2e-project/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.007)
- **Top Global Matches:** file_cluster_2: 2.007, file_cluster_17: 4.885, file_cluster_13: 6.242
- **Magnitude:** 16.38 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/migrations.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.998)
- **Top Global Matches:** file_cluster_2: 1.998, file_cluster_17: 4.882, file_cluster_13: 6.238
- **Magnitude:** 16.14 | **LOC:** 58 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/project.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.995)
- **Top Global Matches:** file_cluster_2: 1.995, file_cluster_17: 4.881, file_cluster_13: 6.236
- **Magnitude:** 16.04 | **LOC:** 53 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/setup-docker/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.995)
- **Top Global Matches:** file_cluster_2: 1.995, file_cluster_17: 4.882, file_cluster_13: 6.234
- **Magnitude:** 15.76 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/generators.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 1.998)
- **Top Global Matches:** file_cluster_2: 1.998, file_cluster_17: 4.883, file_cluster_13: 6.235
- **Magnitude:** 15.68 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/init/schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.009)
- **Top Global Matches:** file_cluster_2: 2.009, file_cluster_17: 4.889, file_cluster_13: 6.237
- **Magnitude:** 15.54 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/generators/library/files/ts-solution/tsconfig.lib.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.034)
- **Top Global Matches:** file_cluster_2: 2.034, file_cluster_17: 4.9, file_cluster_13: 6.244
- **Magnitude:** 15.4 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/src/generators/application/lib/index.d.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/generators/application/application.js` -> **Severity: 0.455** (Bridge: 0.0046 * Flux: 99.9413%)
- `package/src/utils/versions.js` -> **Severity: 0.15** (Bridge: 0.0015 * Flux: 100.0%)
- `package/src/generators/application/lib/create-files.js` -> **Severity: 0.086** (Bridge: 0.0012 * Flux: 68.9974%)
- `package/src/generators/application/lib/create-project.js` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 99.9866%)
- `package/src/generators/init/init.js` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 99.1837%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/utils/versions.js` -> **Severity: 4.891** (Embedded: 0.0799 * Error Risk: 61.2336%)
- `package/src/generators/init/init.js` -> **Severity: 2.892** (Embedded: 0.0513 * Error Risk: 56.3934%)
- `package/src/generators/application/lib/create-targets.js` -> **Severity: 2.138** (Embedded: 0.042 * Error Risk: 50.9676%)
- `package/src/generators/application/lib/add-proxy.js` -> **Severity: 1.717** (Embedded: 0.0321 * Error Risk: 53.5654%)
- `package/src/generators/application/lib/create-project.js` -> **Severity: 1.712** (Embedded: 0.0321 * Error Risk: 53.4193%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/generators/init/init.js` -> **Severity: 2389.8** (Blast Radius: 23.898 * Doc Risk: 100.0%)
- `package/src/utils/has-webpack-plugin.js` -> **Severity: 1965.0** (Blast Radius: 19.65 * Doc Risk: 100.0%)
- `package/src/generators/application/lib/create-targets.js` -> **Severity: 1691.0** (Blast Radius: 16.91 * Doc Risk: 100.0%)
- `package/src/generators/application/application.js` -> **Severity: 1498.3** (Blast Radius: 14.983 * Doc Risk: 100.0%)
- `package/src/utils/vscode-debug-config.js` -> **Severity: 1460.7** (Blast Radius: 14.607 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 88 call pairs -- scoped 22.7%, unique 0.0%, ambiguous 1.1%, external 76.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 88 | 22.7% | 0.0% | 1.1% | 76.1% |

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
