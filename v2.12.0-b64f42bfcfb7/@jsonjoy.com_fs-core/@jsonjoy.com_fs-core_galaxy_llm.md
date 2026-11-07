# ARCHITECTURAL_BRIEF: @jsonjoy.com_fs-core
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
- **Scope:** 26 analyzed artifact(s), 1632 LOC.
- **Load-bearing artifact:** `package/lib/Node.js` -- 6 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/index.d.ts` -- pulls in 10 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/Superblock.js` at magnitude 788.56 (structural weight, not risk).
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
| Total Artifacts | 39 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 1632 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1409 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0953 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2407 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 12 | 295 | 46.2% |
| JAVASCRIPT | 12 | 1337 | 46.2% |
| MARKDOWN | 1 | 0 | 3.8% |
| PLAINTEXT | 1 | 0 | 3.8% |

## 4.1 SOURCE ENCODINGS
All 26 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 27%, Data / Markup / Trivial 19%, Declarative / Non-Code 15%, Large Core Modules (2) 12%, Large Core Modules (3) 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 24 | 92.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `.map`: 8x Excluded (Saturation: Line 1 exceeds 500 chars), 4x Unresolved Ambiguity (No Retainable Structure)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.6 | 21.6 | 4.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 70.0 | 29.0 | 23.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 18.6 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 81.3 | 25.2 | 10.7 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 90.9 | 3.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.1 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.0 | 93.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7 | 3 | 0 | `package/lib/Superblock.js` |
| cleanup | 1 | 1 | 0 | `package/lib/Superblock.js` |
| guards | 147 | 12 | 15 | `package/lib/Superblock.js` |
| danger | 65 | 9 | 2 | `package/lib/Superblock.js` |
| concurrency | 2 | 1 | 0 | `package/lib/util.js` |
| connectivity | 147 | 22 | 13 | `package/lib/util.js` |
| io | 32 | 14 | 3 | `package/lib/util.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 15 | 2 | 0 | `package/lib/Node.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 3 | 1 | 0 | `package/lib/util.js` |
| events | 13 | 3 | 0 | `package/lib/Node.js` |
| tests | 0 | 0 | 0 | - |
| docs | 27 | 9 | 4 | `package/lib/Superblock.d.ts` |
| debt | 11 | 6 | 1 | `package/lib/Superblock.js` |
| mutation | 524 | 17 | 33 | `package/lib/Superblock.js` |
| dead_code | 84 | 9 | 12 | `package/lib/Node.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/util.d.ts` (Hits: 7)
- `package/lib/Superblock.js` (Hits: 4)
- `package/lib/util.js` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Node.js** (`package/lib/Node.js`) — 6 inbound connections
2. **Link.js** (`package/lib/Link.js`) — 5 inbound connections
3. **process.js** (`package/lib/process.js`) — 5 inbound connections
4. **File.js** (`package/lib/File.js`) — 4 inbound connections
5. **json.js** (`package/lib/json.js`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.d.ts** (`package/lib/index.d.ts`) — 10 outbound dependencies
2. **Superblock.js** (`package/lib/Superblock.js`) — 10 outbound dependencies
3. **index.js** (`package/lib/index.js`) — 10 outbound dependencies
4. **Superblock.d.ts** (`package/lib/Superblock.d.ts`) — 9 outbound dependencies
5. **util.js** (`package/lib/util.js`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` **(Defensive Guards)** (@ `package/lib/Superblock.js`) -> Impact: **93.0** | LOC: 277
- `walk` **(Many-Argument Workhorses)** (@ `package/lib/Superblock.js`) -> Impact: **71.8** | LOC: 64
- `formatError` **(Many-Argument Workhorses)** (@ `package/lib/util.js`) -> Impact: **44.4** | LOC: 39
- `_toJSON` **(Many-Argument Workhorses)** (@ `package/lib/Superblock.js`) -> Impact: **33.1** | LOC: 35
- `openFile` **(Many-Argument Workhorses)** (@ `package/lib/Superblock.js`) -> Impact: **30.9** | LOC: 36
- `openLink` **(Many-Argument Workhorses)** (@ `package/lib/Superblock.js`) -> Impact: **26.1** | LOC: 42
- `toJSON` **(Many-Argument Workhorses)** (@ `package/lib/Superblock.js`) -> Impact: **21.2** | LOC: 22
- `write` **(Many-Argument Workhorses)** (@ `package/lib/Node.js`) -> Impact: **19.1** | LOC: 25
- `mkdirp` **(Compute Cores)** (@ `package/lib/Superblock.js`) -> Impact: **19.1** | LOC: 35
  * *Intent:* /** * Creates directory tree recursively. */
- `createLink` **(Defensive Guards)** (@ `package/lib/Superblock.js`) -> Impact: **18.7** | LOC: 16

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 24 | 1565.54 | 21.59% | 31.9% |
| `package` | 2 | 2.74 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/File.d.ts` -> **100.0%** Exposure
- `package/lib/Link.d.ts` -> **100.0%** Exposure
- `package/lib/Node.d.ts` -> **100.0%** Exposure
- `package/lib/Superblock.d.ts` -> **100.0%** Exposure
- `package/lib/util.d.ts` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/File.js` -> **100.0%** Exposure
- `package/lib/Link.js` -> **100.0%** Exposure
- `package/lib/Superblock.js` -> **100.0%** Exposure
- `package/lib/Node.js` -> **99.9998%** Exposure
- `package/lib/util.js` -> **99.9967%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/Node.d.ts` -> **23** Orphaned Functions | **0** Duplicates
- `package/lib/Superblock.d.ts` -> **22** Orphaned Functions | **0** Duplicates
- `package/lib/File.d.ts` -> **12** Orphaned Functions | **0** Duplicates
- `package/lib/Link.d.ts` -> **12** Orphaned Functions | **0** Duplicates
- `package/lib/util.d.ts` -> **7** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `31` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/Superblock.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.845)
- **Top Global Matches:** file_cluster_4: 6.845, file_cluster_15: 8.301, file_cluster_12: 9.26
- **Magnitude:** 788.56 | **LOC:** 692 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 40.49; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.0%), Guard Balance (formerly Safety Score) (61.3%)
- **Documentation Coverage:** 92.5926% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 93.0)
  * `walk` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `_toJSON` **(Many-Argument Workhorses)** (Impact: 33.1)
  * `openFile` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `openLink` **(Many-Argument Workhorses)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 253
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 89`, `args: 43`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 101`, `planned_debt: 6`
* *Architecture:* `io: 4`, `api: 13`, `import: 11`
* *Defense:* `safety: 58`, `doc: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.49
  * `Choke Point (Betweenness):` 0.008415 | `Ripple Effect (Closeness):` 0.103448
  * `Imports (Out-Degree: 7):` File, Link, Node, json, process, result, util, buffer...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/Node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.385)
- **Top Global Matches:** file_cluster_15: 6.385, file_cluster_11: 6.444, file_cluster_12: 7.295
- **Magnitude:** 226.72 | **LOC:** 289 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 59.196; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%), Connectivity (formerly Api Exposure) (72.1%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 19.1)
  * `read` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* /** * Read data from the file. * */
  * `truncate` **(Compute Cores)** (Impact: 12.7)
  * `getuid` **(Defensive Guards)** (Impact: 4.0)
  * `getgid` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 40`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 18`, `import: 4`
* *Defense:* `safety: 15`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.196
  * `Choke Point (Betweenness):` 0.002258 | `Ripple Effect (Closeness):` 0.206897
  * `Imports (Out-Degree: 1):` process, buffer, fs-node-utils, fanout
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/lib/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.401)
- **Top Global Matches:** file_cluster_4: 7.401, file_cluster_15: 9.816, file_cluster_12: 9.889
- **Magnitude:** 225.46 | **LOC:** 199 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 34.681; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (90.9%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatError` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `dataToBuffer` **(Defensive Guards)** (Impact: 12.6)
  * `getPathFromURLPosix` **(Defensive Guards)** (Impact: 10.6)
  * `pathToFilename` **(Defensive Guards)** (Impact: 8.0)
  * `isSeparator` **(Defensive Guards)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 48`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`
* *Architecture:* `io: 4`, `api: 21`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.681
  * `Choke Point (Betweenness):` 0.005337 | `Ripple Effect (Closeness):` 0.110345
  * `Imports (Out-Degree: 2):` encoding, process, buffer, errors, path, fs-node-utils, url
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/Link.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.328)
- **Top Global Matches:** file_cluster_12: 6.328, file_cluster_11: 6.845, file_cluster_15: 6.873
- **Magnitude:** 87.84 | **LOC:** 105 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 48.471; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (69.4%), Connectivity (formerly Api Exposure) (64.0%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `steps` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* // Recursively sync children steps, e.g. in case of dir rename
  * `deleteChild` **(Compute Cores)** (Impact: 3.4)
  * `constructor` **(State Mutators)** (Impact: 2.7)
  * `getParentPath` **(Interface Declarations)** (Impact: 2.2)
  * `syncSteps` **(State Mutators)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 13`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`
* *Architecture:* `io: 1`, `api: 8`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.17734
  * `Imports (Out-Degree: 0):` fs-node-utils, fanout
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/File.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.051)
- **Top Global Matches:** file_cluster_12: 6.051, file_cluster_11: 7.817, file_cluster_15: 8.031
- **Magnitude:** 75.36 | **LOC:** 72 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 37.746; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.3%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (56.9%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(State Mutators)** (Impact: 4.9)
    * *Intent:* /** * Open a Link-Node pair. `node` is provided separately as that might be a different node * rathe...
  * `write` **(Defensive Guards)** (Impact: 4.8)
  * `read` **(Defensive Guards)** (Impact: 4.8)
  * `chown` **(State Mutators)** (Impact: 1.9)
  * `getString` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `import: 1`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.143678
  * `Imports (Out-Degree: 0):` fs-node-utils
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/json.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.078)
- **Top Global Matches:** file_cluster_12: 9.078, file_cluster_7: 10.159, file_cluster_9: 10.685
- **Magnitude:** 30.5 | **LOC:** 35 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 37.746; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flatten` **(Defensive Guards)** (Impact: 18.4)
  * `flattenJSON` **(Callbacks & Closures)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 2`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.143678
  * `Imports (Out-Degree: 0):` buffer, path
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.58)
- **Top Global Matches:** file_cluster_10: 5.58, file_cluster_15: 8.295, file_cluster_2: 8.53
- **Magnitude:** 28.74 | **LOC:** 40 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 100.419; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (54.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.6%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createProcess` **(Callbacks & Closures)** (Impact: 5.7)
  * `maybeReturnProcess` **(Defensive Guards)** (Impact: 2.5)
    * *Intent:* /** * Looks to return a `process` object, if one is available. * * The global `process` is returned ...
  * `emitWarning` **(Callbacks & Closures)** (Impact: 1.9)
  * `cwd` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 7`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.419
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.200627
  * `Imports (Out-Degree: 0):` process
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.356)
- **Top Global Matches:** file_cluster_7: 11.356, file_cluster_12: 11.613, file_cluster_5: 12.276
- **Magnitude:** 28.5 | **LOC:** 26 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `args: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` File, Link, Node, Superblock, constants, json, result, types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/encoding.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_7: 7.431, file_cluster_12: 8.215, file_cluster_5: 9.627
- **Magnitude:** 23.08 | **LOC:** 20 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 50.701; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Connectivity (formerly Api Exposure) (55.6%), Guard Balance (formerly Safety Score) (53.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `strToEncoding` **(Defensive Guards)** (Impact: 7.3)
  * `assertEncoding` **(State Mutators)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `io: 2`, `api: 5`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.701
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.112853
  * `Imports (Out-Degree: 0):` buffer, errors
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/constants.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.586)
- **Top Global Matches:** file_cluster_2: 4.586, file_cluster_17: 5.797, file_cluster_13: 7.381
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 29.765; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.765
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.068966
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/types.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.586)
- **Top Global Matches:** file_cluster_2: 4.586, file_cluster_17: 5.797, file_cluster_13: 7.381
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 43.554; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 43.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.137931
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/result.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.307)
- **Top Global Matches:** file_cluster_15: 5.307, file_cluster_2: 6.18, file_cluster_17: 6.588
- **Magnitude:** 7.4 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 37.746; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (36.9%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Ok` **(Parameter Forwarders)** (Impact: 1.6)
  * `Err` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.143678
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/Superblock.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.41)
- **Top Global Matches:** file_cluster_0: 8.41, file_cluster_15: 9.358, file_cluster_16: 10.155
- **Magnitude:** 6.8 | **LOC:** 102 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.2%)
- **Documentation Coverage:** 60.6061% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_toJSON` **(Compute Cores)** (Impact: 11.2)
  * `toJSON` **(Compute Cores)** (Impact: 11.2)
  * `write` **(Compute Cores)** (Impact: 9.8)
  * `fromJSON` **(Compute Cores)** (Impact: 8.2)
  * `fromNestedJSON` **(Compute Cores)** (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 41`, `args: 46`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `planned_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `io: 3`, `api: 1`, `import: 9`
* *Defense:* `doc: 6`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` File, Link, Node, json, process, result, types, buffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/Node.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.214)
- **Top Global Matches:** file_cluster_15: 6.214, file_cluster_11: 7.021, file_cluster_13: 7.65
- **Magnitude:** 4.44 | **LOC:** 86 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 25.236; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 86.4865% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 9.0)
  * `write` **(Compute Cores)** (Impact: 9.0)
  * `read` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* /** * Read data from the file. * */
  * `canRead` **(Compute Cores)** (Impact: 5.2)
  * `canWrite` **(Compute Cores)** (Impact: 5.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 22`, `args: 30`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 23`
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, fanout
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/util.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 9.782)
- **Top Global Matches:** file_cluster_14: 9.782, file_cluster_7: 10.561, file_cluster_5: 12.865
- **Magnitude:** 2.21 | **LOC:** 19 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (70.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createError` **(Compute Cores)** (Impact: 12.3)
  * `createStatError` **(Compute Cores)** (Impact: 9.0)
  * `dataToBuffer` **(Compute Cores)** (Impact: 3.5)
  * `nullCheck` **(Compute Cores)** (Impact: 3.5)
  * `isFd` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 34`, `args: 10`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `unreferenced_by_name: 7`
* *Architecture:* `io: 7`, `api: 11`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` encoding, types, buffer, misc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/File.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.742)
- **Top Global Matches:** file_cluster_15: 6.742, file_cluster_13: 8.21, file_cluster_11: 8.652
- **Magnitude:** 1.88 | **LOC:** 40 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.6%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Compute Cores)** (Impact: 9.0)
  * `read` **(Compute Cores)** (Impact: 9.0)
  * `getString` **(Compute Cores)** (Impact: 2.9)
  * `truncate` **(Compute Cores)** (Impact: 2.9)
  * `constructor` **(State Mutators)** (Impact: 2.3)
    * *Intent:* /** * Open a Link-Node pair. `node` is provided separately as that might be a different node * rathe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Link, Node, buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.74 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/Link.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.361)
- **Top Global Matches:** file_cluster_15: 6.361, file_cluster_11: 6.874, file_cluster_0: 7.351
- **Magnitude:** 1.36 | **LOC:** 39 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (6.5%), Complexity Load (formerly Cognitive Load) (4.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createChild` **(Compute Cores)** (Impact: 3.5)
  * `setChild` **(Compute Cores)** (Impact: 3.5)
  * `constructor` **(State Mutators)** (Impact: 2.0)
  * `setNode` **(Parameter Forwarders)** (Impact: 1.5)
  * `deleteChild` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 19`, `args: 13`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 12`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Node, Superblock, fanout
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 9.517)
- **Top Global Matches:** file_cluster_17: 9.517, file_cluster_2: 9.739, file_cluster_13: 9.739
- **Magnitude:** 1.26 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 25.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` File, Link, Node, Superblock, constants, json, process, result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 35 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/json.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.83)
- **Top Global Matches:** file_cluster_0: 5.83, file_cluster_13: 8.309, file_cluster_2: 9.726
- **Magnitude:** 0.93 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 25.236; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (8.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 4`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/constants.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.584)
- **Top Global Matches:** file_cluster_2: 2.584, file_cluster_17: 4.539, file_cluster_13: 5.36
- **Magnitude:** 0.87 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/encoding.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.091)
- **Top Global Matches:** file_cluster_15: 7.091, file_cluster_13: 7.66, file_cluster_11: 8.669
- **Magnitude:** 0.51 | **LOC:** 7 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 25.236; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (9.1%), Complexity Load (formerly Cognitive Load) (4.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `strToEncoding` **(Compute Cores)** (Impact: 3.5)
  * `assertEncoding` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 5`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/process.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.9)
- **Top Global Matches:** file_cluster_0: 6.9, file_cluster_13: 8.8, file_cluster_15: 9.074
- **Magnitude:** 0.47 | **LOC:** 12 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (7.1%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getuid` **(I/O & Config Routines)** (Impact: 2.0)
  * `getgid` **(I/O & Config Routines)** (Impact: 2.0)
  * `cwd` **(State Mutators)** (Impact: 1.1)
  * `createProcess` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 3`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `unreferenced_by_name: 4`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/result.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.376)
- **Top Global Matches:** file_cluster_0: 6.376, file_cluster_13: 12.205, file_cluster_5: 12.335
- **Magnitude:** 0.41 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (9.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Ok` **(Generic / Templated Code)** (Impact: 1.5)
  * `Err` **(Generic / Templated Code)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 25.236
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/lib/Node.js` (JAVASCRIPT) | Magnitude: 226.72 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 257, state_mutation: 61, branch: 41, structural_boundaries: 40

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/Superblock.js` -> **Severity: 0.842** (Bridge: 0.0084 * Flux: 100.0%)
- `package/lib/util.js` -> **Severity: 0.534** (Bridge: 0.0053 * Flux: 99.9967%)
- `package/lib/Node.js` -> **Severity: 0.226** (Bridge: 0.0023 * Flux: 99.9998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/Node.js` -> **Severity: 13.027** (Embedded: 0.2069 * Error Risk: 62.9619%)
- `package/lib/Link.js` -> **Severity: 12.301** (Embedded: 0.1773 * Error Risk: 69.3619%)
- `package/lib/process.js` -> **Severity: 11.003** (Embedded: 0.2006 * Error Risk: 54.8419%)
- `package/lib/File.js` -> **Severity: 9.625** (Embedded: 0.1437 * Error Risk: 66.9891%)
- `package/lib/result.js` -> **Severity: 7.389** (Embedded: 0.1437 * Error Risk: 51.4282%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/process.js` -> **Severity: 7531.425** (Blast Radius: 100.419 * Doc Risk: 75.0%)
- `package/lib/Node.js` -> **Severity: 5691.92** (Blast Radius: 59.196 * Doc Risk: 96.1538%)
- `package/lib/encoding.js` -> **Severity: 5070.1** (Blast Radius: 50.701 * Doc Risk: 100.0%)
- `package/lib/Link.js` -> **Severity: 4577.815** (Blast Radius: 48.471 * Doc Risk: 94.4444%)
- `package/lib/json.js` -> **Severity: 3774.6** (Blast Radius: 37.746 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 247 call pairs -- scoped 50.2%, unique 0.0%, ambiguous 2.0%, external 47.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 247 | 50.2% | 0.0% | 2.0% | 47.8% |

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
