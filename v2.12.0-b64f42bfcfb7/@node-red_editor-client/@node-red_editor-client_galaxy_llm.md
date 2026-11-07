# ARCHITECTURAL_BRIEF: @node-red_editor-client
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
- **Scope:** 109 analyzed artifact(s), 68877 LOC.
- **Load-bearing artifact:** none identifiable. No file in this repository is imported by another that GitGalaxy could resolve, so there is no dependency hierarchy to report. That is itself a finding: either this is a collection of independent scripts/documents rather than a coupled system, or the import style is one the engine does not resolve for these languages.
- **Top orchestrator:** `package/public/types/node/worker_threads.d.ts` -- pulls in 9 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/public/red/red.js` at magnitude 37448.46 (structural weight, not risk).
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
| Total Artifacts | 141 |
| Analyzed Artifacts (Scanned) | 109 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 32 |
| Total LOC | 68877 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 50 | 12838 | 45.9% |
| XML | 27 | 2 | 24.8% |
| JSON | 21 | 3042 | 19.3% |
| JAVASCRIPT | 8 | 52587 | 7.3% |
| MARKDOWN | 1 | 0 | 0.9% |
| PLAINTEXT | 1 | 0 | 0.9% |
| LIVECODE | 1 | 408 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 109 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, State Mutators Files 17%, Large Core Modules (3) 13%, Generic / Templated Code Files 6%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 106 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 32*

**Composition by Extension & Reason:**
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 2x Excluded (Static Asset Blob without Intent: 1302 LOC), 1x Excluded (Static Asset Blob without Intent: 1199 LOC), 1x Excluded (Static Asset Blob without Intent: 1444 LOC)
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 201 LOC)
- `.mst`: 1x Excluded (Unsupported Extension: '.mst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 76.3 | 6.1 | 2.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 27.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 44.2 | 14.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 13.9 | 2.0 | 1.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.8 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 50.0 | 49.5 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 27 | 12 | 1 | `package/public/red/red.js` |
| cleanup | 242 | 11 | 0 | `package/public/red/red.js` |
| guards | 3814 | 39 | 11 | `package/public/red/red.js` |
| danger | 1103 | 44 | 20 | `package/public/red/red.js` |
| concurrency | 1088 | 36 | 15 | `package/public/red/red.js` |
| connectivity | 745 | 55 | 4 | `package/public/types/node/fs.d.ts` |
| io | 378 | 19 | 2 | `package/public/types/node/fs.d.ts` |
| crypto | 9 | 7 | 0 | `package/public/types/node/crypto.d.ts` |
| ipc | 76 | 7 | 0 | `package/public/types/node/cluster.d.ts` |
| time | 352 | 10 | 0 | `package/public/red/red.js` |
| serialization | 151 | 1 | 0 | `package/public/red/red.js` |
| regex | 175 | 1 | 0 | `package/public/red/red.js` |
| events | 1997 | 26 | 14 | `package/public/red/red.js` |
| tests | 22 | 4 | 0 | `package/public/types/node/test.d.ts` |
| docs | 2904 | 50 | 80 | `package/public/types/node/fs.d.ts` |
| debt | 1329 | 30 | 14 | `package/public/red/red.js` |
| mutation | 16541 | 44 | 9 | `package/public/red/red.js` |
| dead_code | 1436 | 50 | 23 | `package/public/red/red.js` |
| credential | 42 | 7 | 0 | `package/locales/zh-TW/jsonata.json` |
| threat | 8 | 2 | 0 | `package/public/types/node/buffer.d.ts` |
| ml_ai | 2 | 2 | 0 | `package/public/types/node/test.d.ts` |
| ui | 76 | 2 | 0 | `package/public/red/red.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/public/types/node/fs.d.ts` (Hits: 163)
- `package/public/types/node/https.d.ts` (Hits: 57)
- `package/public/types/node/fs/promises.d.ts` (Hits: 44)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **worker_threads.d.ts** (`package/public/types/node/worker_threads.d.ts`) — 9 outbound dependencies
2. **http2.d.ts** (`package/public/types/node/http2.d.ts`) — 8 outbound dependencies
3. **child_process.d.ts** (`package/public/types/node/child_process.d.ts`) — 7 outbound dependencies
4. **promises.d.ts** (`package/public/types/node/fs/promises.d.ts`) — 6 outbound dependencies
5. **http.d.ts** (`package/public/types/node/http.d.ts`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `setLabel` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **3230.5** | LOC: 10811
- `importNodes` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **582.9** | LOC: 954
  * *Intent:* * Options: * - generateIds - whether to replace all node ids * - addFlow - whether to import nodes to a new tab * - markChanged - whether to set chang...
- `normalisePropertyExpression` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **343.1** | LOC: 5372
- `undoEvent` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **336.6** | LOC: 792
- `_redraw` **(I/O & Config Routines)** (@ `package/public/red/red.js`) -> Impact: **314.5** | LOC: 1210
- `createNodePropertiesTable` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **284.8** | LOC: 285
- `createObjectElement` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **236.7** | LOC: 370
  * *Intent:* /** * Create a DOM element representation of obj - as used by Debug sidebar etc * * * - If you want the Copy Value button, then set `sourceId` * - If ...
- `portMouseUp` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **231.4** | LOC: 290
- `showEditConfigNodeDialog` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **220.9** | LOC: 449
  * *Intent:* /** * name - name of the property that holds this config node * type - type of config node * id - id of config node to edit. _ADD_ for a new one * pre...
- `buildEnvEditRow` **(Many-Argument Workhorses)** (@ `package/public/red/red.js`) -> Impact: **212.0** | LOC: 438
  * *Intent:* /** * Create UI edit interface for environment variable */

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/public/red` | 4 | 37664.78 | 29.95% | 7.39% |
| `package/public/types/node` | 40 | 476.43 | 9.09% | 94.91% |
| `package/public/red/images` | 17 | 169.32 | 0.0% | 0.0% |
| `package/public/red/images/typedInput` | 9 | 94.68 | 0.0% | 0.0% |
| `package/public/red/tours` | 2 | 40.36 | 6.58% | 10.71% |
| `package/public/red/tours/2.1` | 1 | 37.28 | 9.51% | 42.15% |
| `package/public/red/tours/3.1` | 1 | 20.58 | 5.3% | 23.33% |
| `package/public/types/node/fs` | 1 | 18.0 | 26.55% | 99.97% |
| `package` | 3 | 14.52 | 0.0% | 0.0% |
| `package/public/red/tours/2.2` | 1 | 14.08 | 6.67% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/public/types/node-red/func.d.ts` -> **100.0%** Exposure
- `package/public/types/node-red/util.d.ts` -> **100.0%** Exposure
- `package/public/types/node/async_hooks.d.ts` -> **100.0%** Exposure
- `package/public/types/node/buffer.d.ts` -> **100.0%** Exposure
- `package/public/types/node/cluster.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/public/red/red.js` -> **99.9898%** Exposure
- `package/public/red/about` -> **98.1522%** Exposure
- `package/public/types/node/path.d.ts` -> **60.0373%** Exposure
- `package/public/types/node/console.d.ts` -> **58.5428%** Exposure
- `package/public/red/main.js` -> **50.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/public/types/node/http2.d.ts` -> **30** Orphaned Functions | **262** Duplicates
- `package/public/types/node/stream.d.ts` -> **33** Orphaned Functions | **214** Duplicates
- `package/public/types/node/fs.d.ts` -> **33** Orphaned Functions | **96** Duplicates
- `package/public/red/red.js` -> **31** Orphaned Functions | **73** Duplicates
- `package/public/types/node/buffer.d.ts` -> **92** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `148` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/public/red/red.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 17.085)
- **Top Global Matches:** file_cluster_6: 17.085, file_cluster_4: 17.127, file_cluster_12: 22.363
- **Magnitude:** 37448.46 | **LOC:** 59554 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (58.9%)
- **Documentation Coverage:** 91.4862% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLabel` **(Many-Argument Workhorses)** (Impact: 3230.5)
  * `importNodes` **(Many-Argument Workhorses)** (Impact: 582.9)
    * *Intent:* * Options: * - generateIds - whether to replace all node ids * - addFlow - whether to import nodes t...
  * `normalisePropertyExpression` **(Many-Argument Workhorses)** (Impact: 343.1)
  * `undoEvent` **(Many-Argument Workhorses)** (Impact: 336.6)
  * `_redraw` **(I/O & Config Routines)** (Impact: 314.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 92 instances
* *Amplified Cascading Flux:* 3934 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 674
* *State Mutation (weighted view):* 14985
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7546`, `structural_boundaries: 9800`, `args: 4062`, `func_start: 1957`
* *Risk/State:* `safety_bypasses: 354`, `high_risk_execution: 7`, `state_mutation: 7117`, `dead_code: 588`, `planned_debt: 80`, `fragile_debt: 6`, `duplicate_logic: 73`, `unreferenced_by_name: 31`
* *Architecture:* `io: 41`, `api: 132`, `concurrency: 214`, `import: 8`
* *Defense:* `safety: 3326`, `doc: 203`, `test: 1`, `sync_locks: 19`, `immutability_locks: 1`, `cleanup: 226`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` language_tools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/about` (LIVECODE | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.763)
- **Top Global Matches:** file_cluster_2: 3.763, file_cluster_17: 5.131, file_cluster_15: 6.055
- **Magnitude:** 182.16 | **LOC:** 562 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 99`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 27`, `fragile_debt: 2`
* *Architecture:* None
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/fs.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.204)
- **Top Global Matches:** file_cluster_12: 8.204, file_cluster_5: 9.038, file_cluster_0: 9.485
- **Magnitude:** 67.62 | **LOC:** 4321 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 28.4936% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__promisify__` **(Generic / Templated Code)** (Impact: 12.7)
    * *Intent:* /** * Asynchronously writes `buffer` to the file referenced by the supplied file descriptor. */
  * `writeSync` **(Many-Argument Workhorses)** (Impact: 10.1)
    * *Intent:* /** * For detailed information, see the documentation of the asynchronous version of */
  * `__promisify__` **(State Mutators)** (Impact: 7.5)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. */
  * `readdirSync` **(State Mutators)** (Impact: 7.5)
    * *Intent:* /** * Reads the contents of the directory. * * See the POSIX [`readdir(3)`](http://man7.org/linux/ma...
  * `__promisify__` **(State Mutators)** (Impact: 7.4)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 940`, `args: 391`, `func_start: 384`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 25`, `duplicate_logic: 96`, `unreferenced_by_name: 33`
* *Architecture:* `io: 163`, `api: 261`, `concurrency: 69`, `import: 5`
* *Defense:* `doc: 314`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, node:events, promises, node:stream, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/http2.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.094)
- **Top Global Matches:** file_cluster_12: 9.094, file_cluster_5: 9.704, file_cluster_7: 9.968
- **Magnitude:** 48.79 | **LOC:** 2422 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 82.0128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goaway` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Transmits a `GOAWAY` frame to the connected peer _without_ shutting down the`Http2Session`. */
  * `pushStream` **(Compute Cores)** (Impact: 6.2)
  * `respondWithFD` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* * 'last-modified': stat.mtime.toUTCString(), * 'content-type': 'text/plain; charset=utf-8', * }; * s...
  * `respondWithFile` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* * ```js * const http2 = require('node:http2'); * const server = http2.createServer(); * server.on('s...
  * `connect` **(Compute Cores)** (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 846`, `args: 455`, `func_start: 462`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 54`, `duplicate_logic: 262`, `unreferenced_by_name: 30`
* *Architecture:* `io: 10`, `api: 43`, `concurrency: 5`, `import: 9`
* *Defense:* `doc: 101`, `immutability_locks: 52`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http2, node:events, node:fs, node:http, node:net, node:stream, node:tls, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/crypto.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.071)
- **Top Global Matches:** file_cluster_0: 7.071, file_cluster_15: 8.174, file_cluster_16: 9.454
- **Magnitude:** 40.77 | **LOC:** 4527 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (67.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 43.8066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertKey` **(Many-Argument Workhorses)** (Impact: 10.1)
    * *Intent:* * const uncompressedKey = ECDH.convertKey(compressedKey, * 'secp256k1', * 'hex', * 'hex', * 'uncompr...
  * `computeSecret` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* /** * Computes the shared secret using `otherPublicKey` as the other * party's public key and return...
  * `randomFillSync` **(Generic / Templated Code)** (Impact: 6.0)
    * *Intent:* * * const b = new DataView(new ArrayBuffer(10)); * console.log(Buffer.from(randomFillSync(b).buffer,...
  * `getPublicKey` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * The `format` argument specifies point encoding and can be `'compressed'` or `'uncompressed'`. ...
  * `createCipheriv` **(State Mutators)** (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 549`, `args: 328`, `func_start: 328`, `class_start: 99`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 45`, `unreferenced_by_name: 42`
* *Architecture:* `api: 4`, `concurrency: 57`, `import: 3`
* *Defense:* `doc: 243`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crypto, node:stream, node:tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/stream.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.263)
- **Top Global Matches:** file_cluster_5: 11.263, file_cluster_14: 13.029, file_cluster_7: 13.364
- **Magnitude:** 38.85 | **LOC:** 1711 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (59.3%)
- **Documentation Coverage:** 75.7282% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reduce` **(Generic / Templated Code)** (Impact: 8.2)
    * *Intent:* /** * This method calls *fn* on each chunk of the stream in order, passing it the result from the ca...
  * `pipeline` **(Generic / Templated Code)** (Impact: 6.5)
  * `__promisify__` **(Generic / Templated Code)** (Impact: 6.5)
  * `reduce` **(Generic / Templated Code)** (Impact: 6.2)
  * `write` **(Compute Cores)** (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 606`, `args: 314`, `func_start: 310`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 135`, `state_mutation: 2`, `planned_debt: 5`, `duplicate_logic: 214`, `unreferenced_by_name: 33`
* *Architecture:* `api: 2`, `concurrency: 21`, `import: 6`
* *Defense:* `safety: 1`, `doc: 80`, `immutability_locks: 30`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer, node:events, consumers, promises, web, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/tours/2.1/welcome.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.355)
- **Top Global Matches:** file_cluster_2: 7.355, file_cluster_12: 7.376, file_cluster_15: 7.437
- **Magnitude:** 37.28 | **LOC:** 230 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (55.1%), Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (42.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `complete` **(State Mutators)** (Impact: 2.2)
  * `prepare` **(State Mutators)** (Impact: 1.7)
  * `prepare` **(Parameter Forwarders)** (Impact: 1.7)
  * `prepare` **(State Mutators)** (Impact: 1.6)
  * `complete` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 17`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/test.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.233)
- **Top Global Matches:** file_cluster_5: 8.233, file_cluster_12: 9.18, file_cluster_0: 10.589
- **Magnitude:** 33.84 | **LOC:** 1722 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 42.1965% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn` **(Generic / Templated Code)** (Impact: 8.2)
  * `test` **(Compute Cores)** (Impact: 8.1)
  * `suite` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * The `suite()` function is imported from the `node:test` module. */
  * `skip` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Shorthand for skipping a suite. This is the same as [`suite([name], { skip: true }[, fn])`](ht...
  * `todo` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Shorthand for marking a suite as `TODO`. This is the same as [`suite([name], { todo: true }[, ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 356`, `args: 188`, `func_start: 173`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2`, `planned_debt: 42`, `duplicate_logic: 50`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 70`, `import: 3`
* *Defense:* `doc: 173`, `test: 14`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:async_hooks, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/tours/first-flow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.161)
- **Top Global Matches:** file_cluster_10: 5.161, file_cluster_2: 7.027, file_cluster_15: 7.557
- **Magnitude:** 21.86 | **LOC:** 109 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (45.6%), Complexity Load (formerly Cognitive Load) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Defensive Guards)** (Impact: 3.2)
  * `filter` **(Defensive Guards)** (Impact: 3.2)
  * `filter` **(Defensive Guards)** (Impact: 3.0)
  * `complete` **(Callbacks & Closures)** (Impact: 1.1)
  * `complete` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/net.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.231)
- **Top Global Matches:** file_cluster_12: 9.231, file_cluster_5: 9.851, file_cluster_7: 10.303
- **Magnitude:** 21.69 | **LOC:** 1003 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 61.0169% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* * after a certain amount of time: * * ```js * server.on('error', (e) => { * if (e.code === 'EADDRINU...
  * `write` **(Compute Cores)** (Impact: 8.1)
  * `listen` **(Compute Cores)** (Impact: 8.1)
  * `listen` **(Compute Cores)** (Impact: 8.1)
  * `end` **(Compute Cores)** (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 308`, `args: 179`, `func_start: 177`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 14`, `duplicate_logic: 28`, `unreferenced_by_name: 17`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 2`, `import: 4`
* *Defense:* `doc: 78`, `immutability_locks: 21`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net, node:dns, node:events, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/tours/3.1/welcome.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.207)
- **Top Global Matches:** file_cluster_12: 6.207, file_cluster_2: 6.367, file_cluster_7: 6.917
- **Magnitude:** 20.58 | **LOC:** 232 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (23.3%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`
* *Risk/State:* `safety_bypasses: 5`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/http.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.737)
- **Top Global Matches:** file_cluster_5: 8.737, file_cluster_0: 9.329, file_cluster_12: 9.634
- **Magnitude:** 19.88 | **LOC:** 1912 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 66.8394% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeHead` **(State Mutators)** (Impact: 6.2)
    * *Intent:* * res.setHeader('X-Foo', 'bar'); * res.writeHead(200, { 'Content-Type': 'text/plain' }); * res.end('...
  * `setTimeout` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* /** * Sets the timeout value for sockets, and emits a `'timeout'` event on * the Server object, pass...
  * `setSocketKeepAlive` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Once a socket is assigned to this request and is connected `socket.setKeepAlive()` will be cal...
  * `request` **(Parameter Forwarders)** (Impact: 4.2)
  * `get` **(Compute Cores)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 341`, `args: 195`, `func_start: 193`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 11`, `duplicate_logic: 22`, `unreferenced_by_name: 23`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 5`, `import: 6`
* *Defense:* `doc: 107`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, node:dns, node:events, node:net, node:stream, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/tours/welcome.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.082)
- **Top Global Matches:** file_cluster_12: 6.082, file_cluster_7: 6.506, file_cluster_2: 6.675
- **Magnitude:** 18.5 | **LOC:** 127 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (21.4%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/buffer.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.7)
- **Top Global Matches:** file_cluster_12: 7.7, file_cluster_5: 8.032, file_cluster_0: 9.208
- **Magnitude:** 18.38 | **LOC:** 2367 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.6%)
- **Documentation Coverage:** 0.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* * console.log(buf1.compare(buf2, 0, 6, 4)); * // Prints: -1 * console.log(buf1.compare(buf2, 5, 6, 5...
  * `copy` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * } * * buf.copy(buf, 0, 4, 10); * * console.log(buf.toString()); * // Prints: efghijghijklmnopqrstu...
  * `fill` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * console.log(buf.fill('a')); * // Prints: <Buffer 61 61 61 61 61> * console.log(buf.fill('aazz', 'h...
  * `slice` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* /** * Creates and returns a new `Blob` containing a subset of this `Blob` objects * data. The origin...
  * `toString` **(Compute Cores)** (Impact: 8.1)
    * *Intent:* * const buf2 = Buffer.from('tést'); * * console.log(buf2.toString('hex')); * // Prints: 74c3a97374 *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 52`, `args: 110`, `func_start: 111`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `dead_code: 1`, `unreferenced_by_name: 92`
* *Architecture:* `api: 19`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 2`, `doc: 127`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, node:crypto, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/fs/promises.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.931)
- **Top Global Matches:** file_cluster_0: 6.931, file_cluster_15: 8.807, file_cluster_11: 9.736
- **Magnitude:** 18.0 | **LOC:** 1249 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 12.987% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeFile` **(Many-Argument Workhorses)** (Impact: 11.1)
    * *Intent:* * * await promise; * } catch (err) { * // When a request is aborted - err is an AbortError * console...
  * `write` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* * * It is unsafe to use `filehandle.write()` multiple times on the same file * without waiting for t...
  * `read` **(Generic / Templated Code)** (Impact: 9.2)
    * *Intent:* /** * Reads data from the file and stores that in the given buffer. * * If the file is not modified ...
  * `readdir` **(State Mutators)** (Impact: 7.4)
    * *Intent:* * ```js * import { readdir } from 'node:fs/promises'; * * try { * const files = await readdir(path);...
  * `readdir` **(State Mutators)** (Impact: 7.4)
    * *Intent:* /** * Asynchronous readdir(3) - read a directory. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 55`, `args: 77`, `func_start: 77`, `class_start: 8`
* *Risk/State:* `planned_debt: 1`, `unreferenced_by_name: 24`
* *Architecture:* `io: 44`, `api: 1`, `concurrency: 70`, `import: 6`
* *Defense:* `doc: 74`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:events, node:fs, node:readline, node:stream, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/util.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.42)
- **Top Global Matches:** file_cluster_5: 7.42, file_cluster_12: 10.415, file_cluster_7: 11.191
- **Magnitude:** 17.43 | **LOC:** 2296 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (92.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.2%)
- **Documentation Coverage:** 25.1397% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* * // 1_000_000 * console.log(inspect(bigNumber, { numericSeparator: true })); * // 123_456_789n * co...
  * `constructor` **(Compute Cores)** (Impact: 9.0)
  * `decode` **(State Mutators)** (Impact: 7.2)
    * *Intent:* /** * Decodes the `input` and returns a string. If `options.stream` is `true`, any * incomplete byte...
  * `isMap` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* /** * Returns `true` if the value is a built-in [`Map`](https://developer.mozilla.org/en-US/docs/Web...
  * `isSet` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* /** * Returns `true` if the value is a built-in [`Set`](https://developer.mozilla.org/en-US/docs/Web...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 409`, `args: 146`, `func_start: 117`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 28`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 74`
* *Architecture:* `api: 83`, `concurrency: 28`, `import: 5`
* *Defense:* `safety: 47`, `doc: 130`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:crypto, types, util, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/main.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.817)
- **Top Global Matches:** file_cluster_10: 6.817, file_cluster_2: 7.402, file_cluster_17: 8.314
- **Magnitude:** 17.16 | **LOC:** 25 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `args: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* None
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/keymap.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.04)
- **Top Global Matches:** file_cluster_2: 2.04, file_cluster_17: 4.897, file_cluster_13: 6.254
- **Magnitude:** 17.0 | **LOC:** 101 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/child_process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.577)
- **Top Global Matches:** file_cluster_0: 7.577, file_cluster_12: 9.017, file_cluster_5: 9.241
- **Magnitude:** 16.15 | **LOC:** 1548 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (19.5%)
- **Documentation Coverage:** 74.0458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Compute Cores)** (Impact: 9.2)
  * `spawn` **(State Mutators)** (Impact: 6.2)
    * *Intent:* // overloads of spawn with 'args'
  * `spawnSync` **(State Mutators)** (Impact: 6.2)
  * `send` **(Compute Cores)** (Impact: 6.0)
  * `fork` **(Compute Cores)** (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 207`, `args: 131`, `func_start: 131`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 1`, `import: 7`
* *Defense:* `doc: 36`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` child_process, node:dgram, node:events, node:fs, node:net, node:stream, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/dns.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.738)
- **Top Global Matches:** file_cluster_0: 6.738, file_cluster_15: 7.889, file_cluster_11: 9.023
- **Magnitude:** 14.47 | **LOC:** 868 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (96.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 55.8559% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setLocalAddress` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* * The resolver instance will send its requests from the specified IP address. * This allows programs...
  * `__promisify__` **(Generic / Templated Code)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
  * `__promisify__` **(Compute Cores)** (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 287`, `args: 71`, `func_start: 71`, `class_start: 24`
* *Risk/State:* `fragile_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 5`
* *Architecture:* `api: 110`, `concurrency: 28`, `import: 2`
* *Defense:* `doc: 37`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dns, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/red/tours/2.2/welcome.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.276)
- **Top Global Matches:** file_cluster_2: 7.276, file_cluster_12: 7.366, file_cluster_10: 7.519
- **Magnitude:** 14.08 | **LOC:** 157 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (34.1%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare` **(State Mutators)** (Impact: 1.6)
  * `prepare` **(State Mutators)** (Impact: 1.6)
  * `complete` **(State Mutators)** (Impact: 1.6)
  * `complete` **(State Mutators)** (Impact: 1.1)
  * `element` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 1`, `concurrency: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.371)
- **Top Global Matches:** file_cluster_12: 7.371, file_cluster_15: 8.571, file_cluster_11: 9.448
- **Magnitude:** 13.06 | **LOC:** 1758 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 69.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitWarning` **(Compute Cores)** (Impact: 9.0)
  * `send` **(Compute Cores)** (Impact: 8.9)
    * *Intent:* /** * If Node.js is spawned with an IPC channel, the `process.send()` method can be * used to send m...
  * `emitWarning` **(Compute Cores)** (Impact: 6.0)
  * `writeReport` **(Compute Cores)** (Impact: 5.2)
  * `dlopen` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* * The example below shows how to load a C++ Addon, named `local.node`, that exports a `foo` function...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 131`, `args: 141`, `func_start: 120`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `unreferenced_by_name: 22`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 8`, `import: 5`
* *Defense:* `doc: 84`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:net, node:os, node:tty, node:worker_threads, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/cluster.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 10.654)
- **Top Global Matches:** file_cluster_7: 10.654, file_cluster_5: 11.369, file_cluster_14: 11.398
- **Magnitude:** 12.54 | **LOC:** 582 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 80.3922% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Compute Cores)** (Impact: 7.0)
  * `send` **(Parameter Forwarders)** (Impact: 4.2)
  * `prependListener` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* // the handle is a net.Socket or net.Server object, or undefined.
  * `send` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* * ```js * if (cluster.isPrimary) { * const worker = cluster.fork(); * worker.send('hi there'); * * }...
  * `kill` **(Compute Cores)** (Impact: 2.9)
    * *Intent:* /** * This function will kill the worker. In the primary worker, it does this by * disconnecting the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 186`, `args: 103`, `func_start: 102`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `planned_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 40`, `import: 5`
* *Defense:* `doc: 34`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cluster, node:child_process, node:events, node:net
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.438)
- **Top Global Matches:** file_cluster_2: 3.438, file_cluster_17: 5.555, file_cluster_13: 6.664
- **Magnitude:** 12.52 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/public/types/node/tls.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.551)
- **Top Global Matches:** file_cluster_12: 7.551, file_cluster_5: 8.824, file_cluster_7: 8.965
- **Magnitude:** 11.77 | **LOC:** 1221 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 9.174; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createSecurePair` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* * can be replaced by: * * ```js * secureSocket = tls.TLSSocket(socket, options); * ``` * * where `se...
  * `connect` **(Compute Cores)** (Impact: 9.2)
  * `connect` **(Compute Cores)** (Impact: 6.0)
  * `renegotiate` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* * that is either an `Error` (if the request failed) or `null`. * * This method can be used to reques...
  * `constructor` **(Compute Cores)** (Impact: 3.5)
    * *Intent:* /** * Construct a new tls.TLSSocket object from an existing TCP socket. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 215`, `args: 110`, `func_start: 110`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 13`, `planned_debt: 3`, `duplicate_logic: 12`, `unreferenced_by_name: 23`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `doc: 117`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:crypto, node:net, stream, tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/public/types/node/readline/promises.d.ts` (TYPESCRIPT) | Magnitude: 1.71 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, doc: 12, structural_boundaries: 11, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/public/types/node/wasi.d.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, doc: 14, branch: 8, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/public/red/tours/2.1/welcome.js` (JAVASCRIPT) | Magnitude: 37.28 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 227, args: 17, func_start: 17, structural_boundaries: 7
- `package/public/red/tours/2.2/welcome.js` (JAVASCRIPT) | Magnitude: 14.08 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 5, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `package/public/red/red.js` (JAVASCRIPT) | Magnitude: 37448.46 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 51460, structural_boundaries: 9800, core_var_decl: 9156, branch: 7546

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `package/public/types/node/dgram.d.ts` (TYPESCRIPT) | Magnitude: 9.27 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 129, args: 73, func_start: 72
- `package/public/types/node/tty.d.ts` (TYPESCRIPT) | Magnitude: 3.13 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 38, args: 26, func_start: 26
- `package/public/types/node/v8.d.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 59, doc: 55, args: 44

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/public/red/tours/2.1/welcome.js` -> **Severity: 917.4** (Blast Radius: 9.174 * Doc Risk: 100.0%)
- `package/public/red/tours/2.2/welcome.js` -> **Severity: 917.4** (Blast Radius: 9.174 * Doc Risk: 100.0%)
- `package/public/red/tours/first-flow.js` -> **Severity: 917.4** (Blast Radius: 9.174 * Doc Risk: 100.0%)
- `package/public/types/node/stream/consumers.d.ts` -> **Severity: 917.4** (Blast Radius: 9.174 * Doc Risk: 100.0%)
- `package/public/types/node/stream/promises.d.ts` -> **Severity: 917.4** (Blast Radius: 9.174 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6725 call pairs -- scoped 10.3%, unique 0.0%, ambiguous 0.1%, external 89.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 6713 | 10.3% | 0.0% | 0.1% | 89.6% |
| livecode | 8 | 0.0% | 0.0% | 0.0% | 100.0% |
| typescript | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
