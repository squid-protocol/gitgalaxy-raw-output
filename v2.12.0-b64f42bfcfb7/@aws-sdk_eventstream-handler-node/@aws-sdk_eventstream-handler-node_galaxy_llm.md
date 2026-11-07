# ARCHITECTURAL_BRIEF: @aws-sdk_eventstream-handler-node
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
- **Scope:** 15 analyzed artifact(s), 317 LOC.
- **Load-bearing artifact:** `package/dist-es/eventStreamPayloadHandlerProvider.js` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/dist-es/EventStreamPayloadHandler.js` -- pulls in 3 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/dist-cjs/index.js` at magnitude 84.36 (structural weight, not risk).
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
| Total Artifacts | 16 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 317 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.22 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8333 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 8 | 89 | 53.3% |
| JAVASCRIPT | 5 | 228 | 33.3% |
| MARKDOWN | 1 | 0 | 6.7% |
| PLAINTEXT | 1 | 0 | 6.7% |

## 4.1 SOURCE ENCODINGS
All 15 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 53%, State Mutators Files 20%, Large Core Modules (2) 13%, Generic / Templated Code Files 7%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 13 | 86.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 13.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 15.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 51.3 | 18.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 81.8 | 27.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.5 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 1.9 | 38.9 | 9.9 | 3.5 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 29.6 | 28.2 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.9 | 22.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 2 | 1 | `package/dist-types/EventStreamPayloadHandler.d.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 48 | 7 | 11 | `package/dist-cjs/index.js` |
| danger | 8 | 4 | 2 | `package/dist-cjs/index.js` |
| concurrency | 22 | 7 | 6 | `package/dist-cjs/index.js` |
| connectivity | 21 | 13 | 3 | `package/dist-es/EventSigningTransformStream.js` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 4 | 2 | 2 | `package/dist-cjs/index.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 2 | 1 | `package/dist-cjs/index.js` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 6 | 4 | 2 | `package/dist-types/EventSigningTransformStream.d.ts` |
| debt | 0 | 0 | 0 | - |
| mutation | 61 | 4 | 17 | `package/dist-cjs/index.js` |
| dead_code | 10 | 5 | 2 | `package/dist-cjs/index.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/README.md` (Hits: 0)
- `package/dist-cjs/index.js` (Hits: 0)
- `package/dist-es/EventSigningTransformStream.js` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **eventStreamPayloadHandlerProvider.js** (`package/dist-es/eventStreamPayloadHandlerProvider.js`) — 3 inbound connections
2. **EventSigningTransformStream.js** (`package/dist-es/EventSigningTransformStream.js`) — 1 inbound connections
3. **EventStreamPayloadHandler.js** (`package/dist-es/EventStreamPayloadHandler.js`) — 1 inbound connections
4. **README.md** (`package/README.md`) — 0 inbound connections
5. **index.js** (`package/dist-cjs/index.js`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **EventStreamPayloadHandler.js** (`package/dist-es/EventStreamPayloadHandler.js`) — 3 outbound dependencies
2. **EventSigningTransformStream.d.ts** (`package/dist-types/EventSigningTransformStream.d.ts`) — 3 outbound dependencies
3. **EventSigningTransformStream.d.ts** (`package/dist-types/ts3.4/EventSigningTransformStream.d.ts`) — 3 outbound dependencies
4. **index.js** (`package/dist-cjs/index.js`) — 2 outbound dependencies
5. **EventSigningTransformStream.js** (`package/dist-es/EventSigningTransformStream.js`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handle` **(Defensive Guards)** (@ `package/dist-cjs/index.js`) -> Impact: **22.1** | LOC: 43
- `handle` **(Defensive Guards)** (@ `package/dist-es/EventStreamPayloadHandler.js`) -> Impact: **22.1** | LOC: 43
- `handle` **(Generic / Templated Code)** (@ `package/dist-types/ts3.4/EventStreamPayloadHandler.d.ts`) -> Impact: **4.2** | LOC: 5
- `handle` **(Generic / Templated Code)** (@ `package/dist-types/EventStreamPayloadHandler.d.ts`) -> Impact: **4.0** | LOC: 1
- `_transform` **(Many-Argument Workhorses)** (@ `package/dist-cjs/index.js`) -> Impact: **3.7** | LOC: 33
- `_transform` **(Many-Argument Workhorses)** (@ `package/dist-es/EventSigningTransformStream.js`) -> Impact: **3.7** | LOC: 33
- `constructor` **(Defensive Guards)** (@ `package/dist-cjs/index.js`) -> Impact: **3.1** | LOC: 5
- `constructor` **(Defensive Guards)** (@ `package/dist-es/EventStreamPayloadHandler.js`) -> Impact: **3.1** | LOC: 5
- `_transform` **(Parameter Forwarders)** (@ `package/dist-types/ts3.4/EventSigningTransformStream.d.ts`) -> Impact: **2.2** | LOC: 5
- `constructor` **(Parameter Forwarders)** (@ `package/dist-cjs/index.js`) -> Impact: **2.0** | LOC: 12

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/dist-es` | 4 | 100.9 | 24.58% | 0.0% |
| `package/dist-cjs` | 1 | 84.36 | 95.52% | 32.52% |
| `package` | 2 | 2.18 | 0.0% | 0.0% |
| `package/dist-types/ts3.4` | 4 | 2.01 | 1.47% | 40.88% |
| `package/dist-types` | 4 | 1.96 | 0.88% | 40.88% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/dist-types/EventSigningTransformStream.d.ts` -> **81.7574%** Exposure
- `package/dist-types/EventStreamPayloadHandler.d.ts` -> **81.7574%** Exposure
- `package/dist-types/ts3.4/EventSigningTransformStream.d.ts` -> **81.7574%** Exposure
- `package/dist-types/ts3.4/EventStreamPayloadHandler.d.ts` -> **81.7574%** Exposure
- `package/dist-cjs/index.js` -> **32.5175%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/dist-es/EventStreamPayloadHandler.js` -> **99.8979%** Exposure
- `package/dist-cjs/index.js` -> **99.0803%** Exposure
- `package/dist-es/EventSigningTransformStream.js` -> **86.8266%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/dist-cjs/index.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/dist-types/EventSigningTransformStream.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/dist-types/EventStreamPayloadHandler.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/dist-types/ts3.4/EventSigningTransformStream.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/dist-types/ts3.4/EventStreamPayloadHandler.d.ts` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `15` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/dist-cjs/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.703)
- **Top Global Matches:** file_cluster_15: 6.703, file_cluster_10: 6.999, file_cluster_13: 8.52
- **Magnitude:** 84.36 | **LOC:** 119 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.1%), Complexity Load (formerly Cognitive Load) (95.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Defensive Guards)** (Impact: 22.1)
  * `_transform` **(Many-Argument Workhorses)** (Impact: 3.7)
  * `constructor` **(Defensive Guards)** (Impact: 3.1)
  * `constructor` **(Parameter Forwarders)** (Impact: 2.0)
  * `systemClockOffsetProvider` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 21`, `args: 10`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eventstream-codec, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-es/EventStreamPayloadHandler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.032)
- **Top Global Matches:** file_cluster_10: 7.032, file_cluster_15: 8.647, file_cluster_13: 8.87
- **Magnitude:** 66.42 | **LOC:** 57 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 167.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (98.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Defensive Guards)** (Impact: 22.1)
  * `constructor` **(Defensive Guards)** (Impact: 3.1)
  * `systemClockOffsetProvider` **(Defensive Guards)** (Impact: 2.0)
  * `resolvePipeline` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 167.518
  * `Choke Point (Betweenness):` 0.021978 | `Ripple Effect (Closeness):` 0.163265
  * `Imports (Out-Degree: 1):` EventSigningTransformStream, eventstream-codec, node:stream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/dist-es/EventSigningTransformStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.527)
- **Top Global Matches:** file_cluster_15: 5.527, file_cluster_2: 6.561, file_cluster_11: 7.241
- **Magnitude:** 20.42 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 184.092; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.8%), Concurrency Surface (formerly Concurrency) (72.4%), Guard Balance (formerly Safety Score) (51.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_transform` **(Many-Argument Workhorses)** (Impact: 3.7)
  * `constructor` **(Parameter Forwarders)** (Impact: 2.0)
  * `getSignatureBinary` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 3`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 184.092
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.14881
  * `Imports (Out-Degree: 0):` node:stream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/dist-es/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.474)
- **Top Global Matches:** file_cluster_2: 4.474, file_cluster_17: 5.26, file_cluster_13: 5.769
- **Magnitude:** 11.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` eventStreamPayloadHandlerProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-es/eventStreamPayloadHandlerProvider.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.578)
- **Top Global Matches:** file_cluster_15: 5.578, file_cluster_11: 6.759, file_cluster_2: 7.108
- **Magnitude:** 2.54 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 148.024; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `eventStreamPayloadHandlerProvider` **(Parameter Forwarders)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 148.024
  * `Choke Point (Betweenness):` 0.032967 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 1):` EventStreamPayloadHandler
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.18 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/eventStreamPayloadHandlerProvider.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.005)
- **Top Global Matches:** file_cluster_13: 5.005, file_cluster_2: 6.931, file_cluster_17: 7.578
- **Magnitude:** 0.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/ts3.4/eventStreamPayloadHandlerProvider.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.913)
- **Top Global Matches:** file_cluster_13: 4.913, file_cluster_2: 6.797, file_cluster_17: 7.487
- **Magnitude:** 0.6 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.474)
- **Top Global Matches:** file_cluster_2: 4.474, file_cluster_17: 5.26, file_cluster_13: 5.769
- **Magnitude:** 0.58 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` eventStreamPayloadHandlerProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/ts3.4/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.474)
- **Top Global Matches:** file_cluster_2: 4.474, file_cluster_17: 5.26, file_cluster_13: 5.769
- **Magnitude:** 0.58 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` eventStreamPayloadHandlerProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/ts3.4/EventStreamPayloadHandler.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.369)
- **Top Global Matches:** file_cluster_5: 6.369, file_cluster_7: 9.236, file_cluster_12: 9.908
- **Magnitude:** 0.47 | **LOC:** 32 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (50.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (28.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Generic / Templated Code)** (Impact: 4.2)
  * `constructor` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/EventStreamPayloadHandler.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.152)
- **Top Global Matches:** file_cluster_5: 9.152, file_cluster_7: 11.816, file_cluster_14: 12.705
- **Magnitude:** 0.44 | **LOC:** 21 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.9%), Concurrency Surface (formerly Concurrency) (28.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle` **(Generic / Templated Code)** (Impact: 4.0)
  * `constructor` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/ts3.4/EventSigningTransformStream.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.137)
- **Top Global Matches:** file_cluster_0: 7.137, file_cluster_13: 8.317, file_cluster_15: 8.986
- **Magnitude:** 0.36 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (28.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_transform` **(Parameter Forwarders)** (Impact: 2.2)
  * `constructor` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 3`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eventstream-codec, types, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/dist-types/EventSigningTransformStream.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.47)
- **Top Global Matches:** file_cluster_0: 7.47, file_cluster_13: 8.853, file_cluster_15: 9.619
- **Magnitude:** 0.34 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 41.697; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (28.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_transform` **(Parameter Forwarders)** (Impact: 2.0)
  * `constructor` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 3`
* *Defense:* `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 41.697
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eventstream-codec, types, node:stream
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

- `package/dist-es/EventStreamPayloadHandler.js` -> **Severity: 2.196** (Bridge: 0.022 * Flux: 99.8979%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/dist-es/EventSigningTransformStream.js` -> **Severity: 7.636** (Embedded: 0.1488 * Error Risk: 51.3155%)
- `package/dist-es/EventStreamPayloadHandler.js` -> **Severity: 7.201** (Embedded: 0.1633 * Error Risk: 44.1065%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/dist-es/EventSigningTransformStream.js` -> **Severity: 18409.2** (Blast Radius: 184.092 * Doc Risk: 100.0%)
- `package/dist-es/EventStreamPayloadHandler.js` -> **Severity: 16751.8** (Blast Radius: 167.518 * Doc Risk: 100.0%)
- `package/dist-es/eventStreamPayloadHandlerProvider.js` -> **Severity: 14802.4** (Blast Radius: 148.024 * Doc Risk: 100.0%)
- `package/dist-cjs/index.js` -> **Severity: 4169.7** (Blast Radius: 41.697 * Doc Risk: 100.0%)
- `package/dist-types/EventSigningTransformStream.d.ts` -> **Severity: 4169.7** (Blast Radius: 41.697 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 52 call pairs -- scoped 17.3%, unique 0.0%, ambiguous 1.9%, external 80.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 52 | 17.3% | 0.0% | 1.9% | 80.8% |

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
