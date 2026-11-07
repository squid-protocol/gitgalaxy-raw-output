# ARCHITECTURAL_BRIEF: @ledgerhq_hw-transport-node-hid
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
- **Scope:** 16 analyzed artifact(s), 572 LOC.
- **Load-bearing artifact:** `package/src/listenDevices.ts` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/TransportNodeHid.ts` -- pulls in 6 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/TransportNodeHid.js` at magnitude 74.02 (structural weight, not risk).
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
| Total Artifacts | 26 |
| Analyzed Artifacts (Scanned) | 16 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 572 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 61.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 7 | 199 | 43.8% |
| JAVASCRIPT | 4 | 348 | 25.0% |
| PLAINTEXT | 2 | 0 | 12.5% |
| JSON | 2 | 25 | 12.5% |
| MARKDOWN | 1 | 0 | 6.2% |

## 4.1 SOURCE ENCODINGS
All 16 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Callbacks & Closures Files 38%, Generic / Templated Code Files 12%, Declarative / Non-Code 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 13 | 81.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 18.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `.map`: 6x Excluded (Saturation: Line 1 exceeds 500 chars), 2x Unresolved Ambiguity (No Retainable Structure)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 80 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 69.7 | 19.0 | 6.5 | 6.5 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 58.9 | 33.1 | 49.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.3 | 27.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.6 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 32.8 | 9.8 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 96.6 | 30.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.9 | 35.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 4 | 2 | 1 | `package/lib/TransportNodeHid.js` |
| danger | 6 | 5 | 1 | `package/lib/TransportNodeHid.js` |
| concurrency | 38 | 10 | 6 | `package/lib-es/TransportNodeHid.d.ts` |
| connectivity | 13 | 11 | 2 | `package/lib-es/listenDevices.js` |
| io | 11 | 5 | 1 | `package/src/TransportNodeHid.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 3 | 1 | `package/src/listenDevices.ts` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 39 | 8 | 8 | `package/src/listenDevices.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 40 | 5 | 8 | `package/lib-es/TransportNodeHid.d.ts` |
| debt | 3 | 3 | 1 | `package/src/TransportNodeHid.ts` |
| mutation | 171 | 7 | 31 | `package/lib/TransportNodeHid.js` |
| dead_code | 17 | 5 | 5 | `package/src/TransportNodeHid.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/TransportNodeHid.ts` (Hits: 7)
- `package/jest.config.ts` (Hits: 1)
- `package/lib-es/TransportNodeHid.d.ts` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **listenDevices.ts** (`package/src/listenDevices.ts`) — 1 inbound connections
2. **listenDevices.js** (`package/lib-es/listenDevices.js`) — 1 inbound connections
3. **listenDevices.js** (`package/lib/listenDevices.js`) — 1 inbound connections
4. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 inbound connections
5. **LICENSE.txt** (`package/LICENSE.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TransportNodeHid.ts** (`package/src/TransportNodeHid.ts`) — 6 outbound dependencies
2. **listenDevices.ts** (`package/src/listenDevices.ts`) — 5 outbound dependencies
3. **TransportNodeHid.js** (`package/lib-es/TransportNodeHid.js`) — 5 outbound dependencies
4. **listenDevices.js** (`package/lib-es/listenDevices.js`) — 5 outbound dependencies
5. **TransportNodeHid.js** (`package/lib/TransportNodeHid.js`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `poll` **(I/O & Config Routines)** (@ `package/src/listenDevices.ts`) -> Impact: **9.8** | LOC: 35
- `poll` **(I/O & Config Routines)** (@ `package/lib-es/listenDevices.js`) -> Impact: **9.7** | LOC: 34
- `poll` **(I/O & Config Routines)** (@ `package/lib/listenDevices.js`) -> Impact: **9.7** | LOC: 34
- `open` **(Callbacks & Closures)** (@ `package/lib/TransportNodeHid.js`) -> Impact: **7.6** | LOC: 11
  * *Intent:* /** * if path="" is not provided, the library will take the first device */
- `listen` **(Callbacks & Closures)** (@ `package/lib/TransportNodeHid.js`) -> Impact: **6.6** | LOC: 19
  * *Intent:* /** */
- `ownKeys` **(Callbacks & Closures)** (@ `package/lib/TransportNodeHid.js`) -> Impact: **6.1** | LOC: 8
- `default` **(Callbacks & Closures)** (@ `package/lib/listenDevices.js`) -> Impact: **5.4** | LOC: 5
- `listen` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **5.3** | LOC: 22
  * *Intent:* /** */
- `listen` **(Callbacks & Closures)** (@ `package/lib-es/TransportNodeHid.js`) -> Impact: **5.2** | LOC: 19
  * *Intent:* /** */
- `open` **(Callbacks & Closures)** (@ `package/src/TransportNodeHid.ts`) -> Impact: **4.8** | LOC: 11
  * *Intent:* /** * if path="" is not provided, the library will take the first device */

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 4 | 118.32 | 30.47% | 30.35% |
| `package/lib-es` | 4 | 71.74 | 15.76% | 33.77% |
| `package/src` | 2 | 70.74 | 28.19% | 48.47% |
| `package` | 6 | 67.76 | 0.85% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib-es/TransportNodeHid.js` -> **97.334%** Exposure
- `package/src/TransportNodeHid.ts` -> **96.9302%** Exposure
- `package/lib/TransportNodeHid.js` -> **83.6475%** Exposure
- `package/lib-es/TransportNodeHid.d.ts` -> **37.7541%** Exposure
- `package/lib/TransportNodeHid.d.ts` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/TransportNodeHid.js` -> **99.9457%** Exposure
- `package/lib/listenDevices.js` -> **99.7835%** Exposure
- `package/src/listenDevices.ts` -> **99.7039%** Exposure
- `package/lib-es/listenDevices.js` -> **99.3494%** Exposure
- `package/lib-es/TransportNodeHid.js` -> **28.1591%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/TransportNodeHid.ts` -> **5** Orphaned Functions | **0** Duplicates
- `package/lib-es/TransportNodeHid.js` -> **5** Orphaned Functions | **0** Duplicates
- `package/lib/TransportNodeHid.js` -> **5** Orphaned Functions | **0** Duplicates
- `package/lib-es/TransportNodeHid.d.ts` -> **1** Orphaned Functions | **0** Duplicates
- `package/lib/TransportNodeHid.d.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `36` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/TransportNodeHid.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.017)
- **Top Global Matches:** file_cluster_10: 6.017, file_cluster_12: 8.421, file_cluster_13: 8.781
- **Magnitude:** 74.02 | **LOC:** 150 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 48.662; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (83.6%), Guard Balance (formerly Safety Score) (58.9%), Concurrency Surface (formerly Concurrency) (54.8%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Callbacks & Closures)** (Impact: 7.6)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
  * `listen` **(Callbacks & Closures)** (Impact: 6.6)
    * *Intent:* /** */
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
  * `onAdd` **(Callbacks & Closures)** (Impact: 4.8)
  * `onRemove` **(Callbacks & Closures)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 37`, `args: 21`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` listenDevices, devices, errors, hw-transport-node-hid-noevents, node-hid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/listenDevices.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.323)
- **Top Global Matches:** file_cluster_10: 6.323, file_cluster_15: 7.859, file_cluster_13: 8.756
- **Magnitude:** 43.2 | **LOC:** 76 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 90.024; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (69.7%), Guard Balance (formerly Safety Score) (58.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(I/O & Config Routines)** (Impact: 9.7)
  * `default` **(Callbacks & Closures)** (Impact: 5.4)
  * `attachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `detachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `flatDevice` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 19`, `args: 14`, `func_start: 8`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 90.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` hw-transport-node-hid-noevents, logs, events, debounce, usb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/TransportNodeHid.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.342)
- **Top Global Matches:** file_cluster_10: 6.342, file_cluster_13: 7.821, file_cluster_0: 8.494
- **Magnitude:** 35.98 | **LOC:** 127 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 48.662; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.9%), Concurrency Surface (formerly Concurrency) (71.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.7%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen` **(Callbacks & Closures)** (Impact: 5.3)
    * *Intent:* /** */
  * `open` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
  * `onAdd` **(Callbacks & Closures)** (Impact: 4.7)
  * `onRemove` **(Callbacks & Closures)** (Impact: 4.7)
  * `setListenDevicesDebounce` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` listenDevices, devices, errors, hw-transport, hw-transport-node-hid-noevents, node-hid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib-es/TransportNodeHid.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.073)
- **Top Global Matches:** file_cluster_10: 5.073, file_cluster_13: 7.546, file_cluster_2: 8.503
- **Magnitude:** 35.94 | **LOC:** 111 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 48.662; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.3%), Concurrency Surface (formerly Concurrency) (72.9%), Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 44.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* /** */
  * `onAdd` **(Callbacks & Closures)** (Impact: 4.8)
  * `onRemove` **(Callbacks & Closures)** (Impact: 4.8)
  * `open` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
  * `setListenDevicesDebounce` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 5`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` listenDevices, devices, errors, hw-transport-node-hid-noevents, node-hid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/listenDevices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.648)
- **Top Global Matches:** file_cluster_10: 6.648, file_cluster_15: 8.149, file_cluster_13: 9.066
- **Magnitude:** 34.76 | **LOC:** 89 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 90.024; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (58.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(I/O & Config Routines)** (Impact: 9.8)
  * `attachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `detachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `flatDevice` **(Parameter Forwarders)** (Impact: 1.5)
  * `getDeviceByPaths` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 23`, `args: 14`, `func_start: 6`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 90.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` hw-transport-node-hid-noevents, logs, events, debounce, usb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib-es/listenDevices.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.523)
- **Top Global Matches:** file_cluster_10: 6.523, file_cluster_15: 7.924, file_cluster_13: 8.787
- **Magnitude:** 34.7 | **LOC:** 71 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 90.024; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (57.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(I/O & Config Routines)** (Impact: 9.7)
  * `attachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `detachDetected` **(Callbacks & Closures)** (Impact: 1.6)
  * `flatDevice` **(Parameter Forwarders)** (Impact: 1.5)
  * `getDeviceByPaths` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 23`, `args: 13`, `func_start: 7`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 90.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` hw-transport-node-hid-noevents, logs, events, debounce, usb
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 20.98 | **LOC:** 1049 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.build.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.046)
- **Top Global Matches:** file_cluster_2: 2.046, file_cluster_17: 4.905, file_cluster_13: 6.247
- **Magnitude:** 15.36 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/jest.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.217)
- **Top Global Matches:** file_cluster_2: 4.217, file_cluster_17: 5.496, file_cluster_13: 5.927
- **Magnitude:** 15.16 | **LOC:** 11 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 48.662; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jest.config.ts, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.197)
- **Top Global Matches:** file_cluster_2: 2.197, file_cluster_17: 4.973, file_cluster_13: 6.293
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.62 | **LOC:** 81 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib-es/listenDevices.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.789)
- **Top Global Matches:** file_cluster_10: 6.789, file_cluster_2: 9.398, file_cluster_13: 9.616
- **Magnitude:** 0.71 | **LOC:** 7 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 48.662; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.3%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/listenDevices.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.789)
- **Top Global Matches:** file_cluster_10: 6.789, file_cluster_2: 9.398, file_cluster_13: 9.616
- **Magnitude:** 0.71 | **LOC:** 7 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 48.662; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.3%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib-es/TransportNodeHid.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.955)
- **Top Global Matches:** file_cluster_5: 9.955, file_cluster_7: 12.788, file_cluster_12: 14.088
- **Magnitude:** 0.39 | **LOC:** 39 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 48.662; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 16`, `args: 7`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hw-transport, hw-transport-node-hid-noevents
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/TransportNodeHid.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.955)
- **Top Global Matches:** file_cluster_5: 9.955, file_cluster_7: 12.788, file_cluster_12: 14.088
- **Magnitude:** 0.39 | **LOC:** 39 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 48.662; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Generic / Templated Code)** (Impact: 1.5)
    * *Intent:* /** * if path="" is not provided, the library will take the first device */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 16`, `args: 7`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 48.662
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hw-transport, hw-transport-node-hid-noevents
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/listenDevices.js` -> **Severity: 3.432** (Embedded: 0.0588 * Error Risk: 58.3423%)
- `package/src/listenDevices.ts` -> **Severity: 3.412** (Embedded: 0.0588 * Error Risk: 57.9953%)
- `package/lib-es/listenDevices.js` -> **Severity: 3.363** (Embedded: 0.0588 * Error Risk: 57.1724%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/listenDevices.ts` -> **Severity: 9002.4** (Blast Radius: 90.024 * Doc Risk: 100.0%)
- `package/lib-es/listenDevices.js` -> **Severity: 9002.4** (Blast Radius: 90.024 * Doc Risk: 100.0%)
- `package/lib/listenDevices.js` -> **Severity: 9002.4** (Blast Radius: 90.024 * Doc Risk: 100.0%)
- `package/lib/TransportNodeHid.js` -> **Severity: 2838.615** (Blast Radius: 48.662 * Doc Risk: 58.3333%)
- `package/src/TransportNodeHid.ts` -> **Severity: 2162.753** (Blast Radius: 48.662 * Doc Risk: 44.4444%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 115 call pairs -- scoped 13.9%, unique 0.0%, ambiguous 3.5%, external 82.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 76 | 15.8% | 0.0% | 2.6% | 81.6% |
| typescript | 39 | 10.3% | 0.0% | 5.1% | 84.6% |

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
