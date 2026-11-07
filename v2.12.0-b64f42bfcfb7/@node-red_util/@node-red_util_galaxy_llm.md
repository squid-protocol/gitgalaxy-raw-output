# ARCHITECTURAL_BRIEF: @node-red_util
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
- **Scope:** 9 analyzed artifact(s), 1567 LOC.
- **Load-bearing artifact:** `package/lib/log.js` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/index.js` -- pulls in 6 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/util.js` at magnitude 927.72 (structural weight, not risk).
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
| Total Artifacts | 10 |
| Analyzed Artifacts (Scanned) | 9 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 1567 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0992 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4651 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 7 | 1567 | 77.8% |
| MARKDOWN | 1 | 0 | 11.1% |
| PLAINTEXT | 1 | 0 | 11.1% |

## 4.1 SOURCE ENCODINGS
All 9 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 33%, Large Core Modules (2) 33%, Data / Markup / Trivial 22%, Many-Argument Workhorses Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7 | 77.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 22.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 67.5 | 40.7 | 45.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 49.6 | 63.8 | 56.5 | 56.5 | 49.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 8.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 24.7 | 2.7 | 80.0 |
| Connectivity (formerly API Exposure) | 3.1 | 31.7 | 21.2 | 20.9 | 3.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 31.6 | 22.2 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 16.8 | 100.0 | 88.0 | 100.0 | 16.8 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 29.8 | 5.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.3 | 35.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7 | 1 | 0 | `package/lib/util.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 194 | 5 | 19 | `package/lib/util.js` |
| danger | 45 | 4 | 4 | `package/lib/util.js` |
| concurrency | 20 | 4 | 4 | `package/lib/i18n.js` |
| connectivity | 13 | 7 | 3 | `package/lib/i18n.js` |
| io | 12 | 2 | 4 | `package/lib/i18n.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `package/lib/exec.js` |
| time | 9 | 3 | 3 | `package/lib/exec.js` |
| serialization | 10 | 3 | 1 | `package/lib/util.js` |
| regex | 18 | 4 | 5 | `package/lib/hooks.js` |
| events | 33 | 3 | 9 | `package/lib/exec.js` |
| tests | 0 | 0 | 0 | - |
| docs | 60 | 7 | 12 | `package/lib/util.js` |
| debt | 5 | 3 | 2 | `package/lib/log.js` |
| mutation | 473 | 7 | 54 | `package/lib/util.js` |
| dead_code | 7 | 3 | 1 | `package/lib/i18n.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/i18n.js` (Hits: 8)
- `package/lib/exec.js` (Hits: 4)
- `package/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **log.js** (`package/lib/log.js`) — 3 inbound connections
2. **events.js** (`package/lib/events.js`) — 2 inbound connections
3. **i18n.js** (`package/lib/i18n.js`) — 2 inbound connections
4. **util.js** (`package/lib/util.js`) — 2 inbound connections
5. **exec.js** (`package/lib/exec.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/index.js`) — 6 outbound dependencies
2. **util.js** (`package/lib/util.js`) — 6 outbound dependencies
3. **log.js** (`package/lib/log.js`) — 4 outbound dependencies
4. **exec.js** (`package/lib/exec.js`) — 3 outbound dependencies
5. **i18n.js** (`package/lib/i18n.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `normalisePropertyExpression` **(Many-Argument Workhorses)** (@ `package/lib/util.js`) -> Impact: **298.6** | LOC: 893
  * *Intent:* * names. * * For example, `a["b"].c` returns `['a','b','c']` * * If `msg` is provided, any internal cross-references will be evaluated against that * ...
- `encodeObject` **(Many-Argument Workhorses)** (@ `package/lib/util.js`) -> Impact: **183.0** | LOC: 266
  * *Intent:* /** * Encode an object to JSON without losing information about non-JSON types * such as Buffer and Function. * * *This function is closely tied to it...
- `compareObjects` **(Defensive Guards)** (@ `package/lib/util.js`) -> Impact: **44.8** | LOC: 65
  * *Intent:* /** * Compares two objects, handling various JavaScript types. * */
- `run` **(Many-Argument Workhorses)** (@ `package/lib/exec.js`) -> Impact: **26.9** | LOC: 47
  * *Intent:* * of the promise is an object of the form: * * { * code: <exit code>, * stdout: <standard output from the command>, * stderr: <standard error from the...
- `add` **(Defensive Guards)** (@ `package/lib/hooks.js`) -> Impact: **26.8** | LOC: 51
  * *Intent:* * - `postDeliver` - passed a `SendEvent`. The message has been dispatched to be delivered asynchronously (unless the sync delivery flag is set, in whi...
- `invokeStack` **(Defensive Guards)** (@ `package/lib/hooks.js`) -> Impact: **24.4** | LOC: 49
- `consoleLogger` **(Defensive Guards)** (@ `package/lib/log.js`) -> Impact: **23.6** | LOC: 20
- `trigger` **(Defensive Guards)** (@ `package/lib/hooks.js`) -> Impact: **21.4** | LOC: 28
- `readFile` **(Defensive Guards)** (@ `package/lib/i18n.js`) -> Impact: **20.5** | LOC: 29
- `evaluateJSONataExpression` **(Callbacks & Closures)** (@ `package/lib/util.js`) -> Impact: **18.1** | LOC: 43
  * *Intent:* /** * Evaluates a JSONata expression. * before passing to this function. * */

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 6 | 1529.38 | 47.45% | 2.99% |
| `package` | 3 | 5.96 | 0.0% | 12.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/index.js` -> **37.7541%** Exposure
- `package/lib/hooks.js` -> **9.579%** Exposure
- `package/lib/util.js` -> **8.3652%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/exec.js` -> **99.9997%** Exposure
- `package/lib/log.js` -> **99.9993%** Exposure
- `package/lib/hooks.js` -> **99.9992%** Exposure
- `package/lib/util.js` -> **99.9974%** Exposure
- `package/lib/i18n.js` -> **99.894%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/index.js` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `14` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.876)
- **Top Global Matches:** file_cluster_6: 8.876, file_cluster_8: 9.97, file_cluster_4: 16.497
- **Magnitude:** 927.72 | **LOC:** 1110 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 100.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (67.5%), Guard Balance (formerly Safety Score) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 10.3448% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalisePropertyExpression` **(Many-Argument Workhorses)** (Impact: 298.6)
    * *Intent:* * names. * * For example, `a["b"].c` returns `['a','b','c']` * * If `msg` is provided, any internal ...
  * `encodeObject` **(Many-Argument Workhorses)** (Impact: 183.0)
    * *Intent:* /** * Encode an object to JSON without losing information about non-JSON types * such as Buffer and ...
  * `compareObjects` **(Defensive Guards)** (Impact: 44.8)
    * *Intent:* /** * Compares two objects, handling various JavaScript types. * */
  * `evaluateJSONataExpression` **(Callbacks & Closures)** (Impact: 18.1)
    * *Intent:* /** * Evaluates a JSONata expression. * before passing to this function. * */
  * `ensureString` **(Defensive Guards)** (Impact: 9.0)
    * *Intent:* /** * Converts the provided argument to a String, using type-dependent * methods. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 78 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 152`, `args: 36`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 149`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 2`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 157`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 100.77
  * `Choke Point (Betweenness):` 0.035714 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 1):` log, json-stringify-safe, jsonata, lodash.clonedeep, moment-timezone, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/hooks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.961)
- **Top Global Matches:** file_cluster_9: 5.961, file_cluster_15: 9.241, file_cluster_16: 9.933
- **Magnitude:** 203.32 | **LOC:** 261 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 70.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (71.0%), Complexity Load (formerly Cognitive Load) (65.8%), Guard Balance (formerly Safety Score) (57.0%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* * - `postDeliver` - passed a `SendEvent`. The message has been dispatched to be delivered asynchrono...
  * `invokeStack` **(Defensive Guards)** (Impact: 24.4)
  * `trigger` **(Defensive Guards)** (Impact: 21.4)
  * `callNextHook` **(Defensive Guards)** (Impact: 14.6)
  * `remove` **(Defensive Guards)** (Impact: 12.5)
    * *Intent:* /** * Remove a handled from a named hook */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 31`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 25`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 19`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 70.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 1):` log.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/i18n.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.587)
- **Top Global Matches:** file_cluster_10: 7.587, file_cluster_15: 8.253, file_cluster_12: 8.322
- **Magnitude:** 168.56 | **LOC:** 257 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 254.724; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.0%)
- **Documentation Coverage:** 53.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readFile` **(Defensive Guards)** (Impact: 20.5)
  * `getCatalog` **(Compute Cores)** (Impact: 11.3)
    * *Intent:* /** * Gets a message catalog. */
  * `mergeCatalog` **(Defensive Guards)** (Impact: 10.9)
  * `registerMessageCatalog` **(Callbacks & Closures)** (Impact: 9.1)
    * *Intent:* /** * Register a message catalog with i18n. */
  * `migrateMessageCatalogV3toV4` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 43`, `args: 26`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `dead_code: 5`
* *Architecture:* `io: 8`, `api: 3`, `concurrency: 12`, `import: 3`
* *Defense:* `safety: 9`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 254.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.347222
  * `Imports (Out-Degree: 0):` fs, i18next, path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/log.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.03)
- **Top Global Matches:** file_cluster_4: 9.03, file_cluster_12: 9.869, file_cluster_10: 11.309
- **Magnitude:** 160.3 | **LOC:** 266 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 216.479; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 35.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consoleLogger` **(Defensive Guards)** (Impact: 23.6)
  * `LogHandler` **(Compute Cores)** (Impact: 16.3)
  * `init` **(Defensive Guards)** (Impact: 13.8)
  * `audit` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* /** * Log an audit event. */
  * `shouldReportMessage` **(Callbacks & Closures)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 20`, `args: 17`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 216.479
  * `Choke Point (Betweenness):` 0.053571 | `Ripple Effect (Closeness):` 0.4
  * `Imports (Out-Degree: 1):` i18n, chalk, events, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/exec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 9.468)
- **Top Global Matches:** file_cluster_9: 9.468, file_cluster_10: 10.112, file_cluster_15: 10.654
- **Magnitude:** 52.0 | **LOC:** 100 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 70.716; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.3%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* * of the promise is an object of the form: * * { * code: <exit code>, * stdout: <standard output fro...
  * `logLines` **(State Mutators)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 10`, `args: 7`, `func_start: 2`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 70.716
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.125
  * `Imports (Out-Degree: 2):` events, util, child_process
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/events.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.434)
- **Top Global Matches:** file_cluster_10: 6.434, file_cluster_13: 8.145, file_cluster_2: 8.26
- **Magnitude:** 17.48 | **LOC:** 80 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 100.77; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (56.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapEventFunction` **(Callbacks & Closures)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 3`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 100.77
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` util, events
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.955)
- **Top Global Matches:** file_cluster_10: 6.955, file_cluster_2: 8.191, file_cluster_17: 8.774
- **Magnitude:** 3.96 | **LOC:** 82 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 61.941; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.6%), Debt Markers (formerly Tech Debt) (37.8%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * Initialise the module with the runtime settings */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 61.941
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` events, exec, hooks, i18n, log, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 61.941
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 61.941
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

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/log.js` -> **Severity: 5.357** (Bridge: 0.0536 * Flux: 99.9993%)
- `package/lib/util.js` -> **Severity: 3.571** (Bridge: 0.0357 * Flux: 99.9974%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/log.js` -> **Severity: 25.538** (Embedded: 0.4 * Error Risk: 63.8451%)
- `package/lib/i18n.js` -> **Severity: 19.438** (Embedded: 0.3472 * Error Risk: 55.9816%)
- `package/lib/events.js` -> **Severity: 14.133** (Embedded: 0.25 * Error Risk: 56.5339%)
- `package/lib/util.js` -> **Severity: 12.716** (Embedded: 0.25 * Error Risk: 50.8636%)
- `package/lib/exec.js` -> **Severity: 7.705** (Embedded: 0.125 * Error Risk: 61.6398%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/i18n.js` -> **Severity: 13585.272** (Blast Radius: 254.724 * Doc Risk: 53.3333%)
- `package/lib/events.js` -> **Severity: 10077.0** (Blast Radius: 100.77 * Doc Risk: 100.0%)
- `package/lib/log.js` -> **Severity: 7640.431** (Blast Radius: 216.479 * Doc Risk: 35.2941%)
- `package/lib/hooks.js` -> **Severity: 5500.135** (Blast Radius: 70.716 * Doc Risk: 77.7778%)
- `package/lib/exec.js` -> **Severity: 2357.198** (Blast Radius: 70.716 * Doc Risk: 33.3333%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 208 call pairs -- scoped 8.7%, unique 0.0%, ambiguous 0.0%, external 91.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 208 | 8.7% | 0.0% | 0.0% | 91.3% |

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
