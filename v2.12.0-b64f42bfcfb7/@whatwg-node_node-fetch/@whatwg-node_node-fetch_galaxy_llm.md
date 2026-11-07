# ARCHITECTURAL_BRIEF: @whatwg-node_node-fetch
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
- **Scope:** 94 analyzed artifact(s), 6351 LOC.
- **Load-bearing artifact:** `package/cjs/utils.js` -- 12 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/cjs/index.js` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/cjs/Body.js` at magnitude 405.12 (structural weight, not risk).
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
| Total Artifacts | 94 |
| Analyzed Artifacts (Scanned) | 94 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 6351 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5111 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4532 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5888 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 46 | 5551 | 48.9% |
| TYPESCRIPT | 46 | 800 | 48.9% |
| PLAINTEXT | 2 | 0 | 2.1% |

## 4.1 SOURCE ENCODINGS
All 94 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 21%, Large Core Modules (2) 19%, State Mutators Files 19%, Compute Cores Files 11%, Generic / Templated Code Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 92 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.2 | 27.8 | 10.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 42.4 | 51.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 36.1 | 12.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 9.4 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 1.8 | 91.9 | 28.8 | 14.0 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.1 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 62 | 16 | 1 | `package/typings/index.d.cts` |
| cleanup | 60 | 18 | 3 | `package/cjs/ReadableStream.js` |
| guards | 526 | 48 | 20 | `package/cjs/Body.js` |
| danger | 298 | 63 | 10 | `package/cjs/Blob.js` |
| concurrency | 222 | 40 | 8 | `package/cjs/Headers.js` |
| connectivity | 452 | 92 | 12 | `package/cjs/index.js` |
| io | 15 | 8 | 0 | `package/cjs/index.js` |
| crypto | 4 | 4 | 0 | `package/cjs/URL.js` |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 2 | 0 | `package/cjs/File.js` |
| serialization | 6 | 6 | 0 | `package/cjs/Blob.js` |
| regex | 12 | 10 | 1 | `package/cjs/fetchCurl.js` |
| events | 123 | 12 | 5 | `package/cjs/Body.js` |
| tests | 0 | 0 | 0 | - |
| docs | 12 | 6 | 0 | `package/typings/Blob.d.cts` |
| debt | 26 | 6 | 0 | `package/typings/Blob.d.cts` |
| mutation | 1259 | 55 | 47 | `package/cjs/Body.js` |
| dead_code | 238 | 48 | 11 | `package/typings/Headers.d.cts` |
| credential | 0 | 0 | 0 | - |
| threat | 4 | 4 | 0 | `package/cjs/index.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2857**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/index.js` (Hits: 3)
- `package/esm/index.js` (Hits: 2)
- `package/typings/Request.d.cts` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.js** (`package/cjs/utils.js`) — 12 inbound connections
2. **utils.js** (`package/esm/utils.js`) — 12 inbound connections
3. **ReadableStream.js** (`package/cjs/ReadableStream.js`) — 5 inbound connections
4. **ReadableStream.js** (`package/esm/ReadableStream.js`) — 5 inbound connections
5. **Response.js** (`package/cjs/Response.js`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 18 outbound dependencies
2. **index.js** (`package/esm/index.js`) — 18 outbound dependencies
3. **index.d.cts** (`package/typings/index.d.cts`) — 18 outbound dependencies
4. **index.d.ts** (`package/typings/index.d.ts`) — 18 outbound dependencies
5. **fetchNodeHttp.js** (`package/cjs/fetchNodeHttp.js`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` **(Defensive Guards)** (@ `package/cjs/Request.js`) -> Impact: **95.0** | LOC: 64
- `constructor` **(Defensive Guards)** (@ `package/esm/Request.js`) -> Impact: **95.0** | LOC: 64
- `fetchNodeHttp` **(Compute Cores)** (@ `package/cjs/fetchNodeHttp.js`) -> Impact: **74.5** | LOC: 133
- `fetchNodeHttp` **(Compute Cores)** (@ `package/esm/fetchNodeHttp.js`) -> Impact: **66.0** | LOC: 133
- `fetchCurl` **(Defensive Guards)** (@ `package/cjs/fetchCurl.js`) -> Impact: **56.2** | LOC: 134
- `fetchCurl` **(Defensive Guards)** (@ `package/esm/fetchCurl.js`) -> Impact: **56.2** | LOC: 134
- `json` **(Defensive Guards)** (@ `package/cjs/Response.js`) -> Impact: **47.8** | LOC: 55
- `json` **(Defensive Guards)** (@ `package/esm/Response.js`) -> Impact: **47.8** | LOC: 55
- `constructor` **(Defensive Guards)** (@ `package/cjs/ReadableStream.js`) -> Impact: **31.7** | LOC: 69
- `constructor` **(Defensive Guards)** (@ `package/esm/ReadableStream.js`) -> Impact: **31.7** | LOC: 69

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/cjs` | 24 | 2681.36 | 47.38% | 2.64% |
| `package/esm` | 23 | 2548.06 | 41.92% | 2.77% |
| `package/typings` | 46 | 420.94 | 9.84% | 69.49% |
| `package` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/typings/Blob.d.cts` -> **100.0%** Exposure
- `package/typings/Blob.d.ts` -> **100.0%** Exposure
- `package/typings/Body.d.cts` -> **100.0%** Exposure
- `package/typings/Body.d.ts` -> **100.0%** Exposure
- `package/typings/FormData.d.cts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/cjs/Request.js` -> **100.0%** Exposure
- `package/cjs/Response.js` -> **100.0%** Exposure
- `package/esm/Request.js` -> **100.0%** Exposure
- `package/esm/Response.js` -> **100.0%** Exposure
- `package/cjs/TextEncoderDecoder.js` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/typings/Blob.d.cts` -> **12** Orphaned Functions | **8** Duplicates
- `package/typings/Blob.d.ts` -> **12** Orphaned Functions | **8** Duplicates
- `package/typings/Headers.d.cts` -> **16** Orphaned Functions | **0** Duplicates
- `package/typings/Headers.d.ts` -> **16** Orphaned Functions | **0** Duplicates
- `package/typings/IteratorObject.d.cts` -> **15** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `111` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/cjs/Body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.294)
- **Top Global Matches:** file_cluster_12: 7.294, file_cluster_10: 9.302, file_cluster_4: 9.84
- **Magnitude:** 405.12 | **LOC:** 530 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 14.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.7%), Complexity Load (formerly Cognitive Load) (92.4%), Guard Balance (formerly Safety Score) (60.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formData` **(Defensive Guards)** (Impact: 30.7)
  * `processBodyInit` **(Defensive Guards)** (Impact: 28.2)
  * `handleContentLengthHeader` **(Compute Cores)** (Impact: 15.3)
  * `buffer` **(Callbacks & Closures)** (Impact: 11.2)
  * `get` **(Defensive Guards)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 114`, `args: 61`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 69`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 39`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.99
  * `Choke Point (Betweenness):` 0.002583 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 5):` Blob.js, File.js, FormData.js, ReadableStream.js, utils.js, busboy, promise-helpers, node:buffer...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/Body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.338)
- **Top Global Matches:** file_cluster_12: 7.338, file_cluster_10: 9.116, file_cluster_4: 9.726
- **Magnitude:** 400.04 | **LOC:** 526 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 14.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.7%), Complexity Load (formerly Cognitive Load) (91.9%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formData` **(Defensive Guards)** (Impact: 30.7)
  * `processBodyInit` **(Defensive Guards)** (Impact: 28.2)
  * `handleContentLengthHeader` **(Compute Cores)** (Impact: 15.3)
  * `buffer` **(Callbacks & Closures)** (Impact: 11.2)
  * `get` **(Defensive Guards)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 124`, `args: 61`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 67`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 5`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 39`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.99
  * `Choke Point (Betweenness):` 0.002583 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 5):` Blob.js, File.js, FormData.js, ReadableStream.js, utils.js, busboy, promise-helpers, node:buffer...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/cjs/Blob.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.141)
- **Top Global Matches:** file_cluster_12: 8.141, file_cluster_7: 8.335, file_cluster_5: 9.802
- **Magnitude:** 316.7 | **LOC:** 292 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 17.484; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Connectivity (formerly Api Exposure) (74.7%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buffer` **(Callbacks & Closures)** (Impact: 17.8)
  * `constructor` **(Defensive Guards)** (Impact: 16.0)
  * `stream` **(Callbacks & Closures)** (Impact: 13.1)
  * `getBlobPartAsBuffer` **(Defensive Guards)** (Impact: 10.6)
  * `pull` **(Callbacks & Closures)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 78`, `args: 37`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 41`
* *Architecture:* `api: 14`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 30`, `doc: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.484
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 2):` ReadableStream.js, utils.js, node:buffer
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/Blob.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.161)
- **Top Global Matches:** file_cluster_12: 8.161, file_cluster_7: 8.413, file_cluster_5: 9.826
- **Magnitude:** 305.46 | **LOC:** 280 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 17.484; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.1%), Connectivity (formerly Api Exposure) (73.3%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buffer` **(Callbacks & Closures)** (Impact: 17.8)
  * `constructor` **(Defensive Guards)** (Impact: 16.0)
  * `stream` **(Callbacks & Closures)** (Impact: 13.1)
  * `getBlobPartAsBuffer` **(Defensive Guards)** (Impact: 10.6)
  * `pull` **(Callbacks & Closures)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 90`, `args: 37`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 31`
* *Architecture:* `api: 13`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 30`, `doc: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.484
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 2):` ReadableStream.js, utils.js, node:buffer
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/cjs/Headers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.803)
- **Top Global Matches:** file_cluster_4: 9.803, file_cluster_6: 10.487, file_cluster_12: 13.607
- **Magnitude:** 251.98 | **LOC:** 310 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 14.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (69.9%), Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMap` **(Defensive Guards)** (Impact: 27.1)
    * *Intent:* // perf: Build the map of headers lazily, only when we need to access all headers or write to it. //...
  * `_get` **(Defensive Guards)** (Impact: 26.3)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `set` **(Defensive Guards)** (Impact: 18.7)
  * `forEach` **(Callbacks & Closures)** (Impact: 11.3)
  * `_keys` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 76`, `args: 31`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 37`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.99
  * `Choke Point (Betweenness):` 0.000584 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 1):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/Headers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.618)
- **Top Global Matches:** file_cluster_4: 9.618, file_cluster_6: 10.324, file_cluster_12: 13.588
- **Magnitude:** 245.88 | **LOC:** 305 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 14.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (66.9%), Guard Balance (formerly Safety Score) (58.5%), Connectivity (formerly Api Exposure) (55.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMap` **(Defensive Guards)** (Impact: 27.1)
    * *Intent:* // perf: Build the map of headers lazily, only when we need to access all headers or write to it. //...
  * `_get` **(Defensive Guards)** (Impact: 26.3)
    * *Intent:* // perf: we don't need to build `this.map` for Requests, as we can access the headers directly
  * `set` **(Defensive Guards)** (Impact: 18.7)
  * `forEach` **(Callbacks & Closures)** (Impact: 11.3)
  * `_keys` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 80`, `args: 31`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 34`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.99
  * `Choke Point (Betweenness):` 0.000584 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 1):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/cjs/ReadableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.555)
- **Top Global Matches:** file_cluster_12: 7.555, file_cluster_10: 10.026, file_cluster_7: 10.173
- **Magnitude:** 242.78 | **LOC:** 246 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 25.347; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (98.9%), Complexity Load (formerly Cognitive Load) (68.7%), Connectivity (formerly Api Exposure) (63.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 31.7)
  * `createController` **(Defensive Guards)** (Impact: 15.9)
  * `destroy` **(Defensive Guards)** (Impact: 9.6)
  * `getReader` **(Callbacks & Closures)** (Impact: 9.1)
  * `handleStart` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 22
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 71`, `args: 44`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 20`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.347
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.081059
  * `Imports (Out-Degree: 1):` utils.js, promise-helpers, node:buffer, node:events, node:stream, promises
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/esm/ReadableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.611)
- **Top Global Matches:** file_cluster_12: 7.611, file_cluster_10: 9.689, file_cluster_15: 10.08
- **Magnitude:** 237.7 | **LOC:** 242 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 25.347; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.0%), Complexity Load (formerly Cognitive Load) (65.3%), Connectivity (formerly Api Exposure) (60.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 31.7)
  * `createController` **(Defensive Guards)** (Impact: 15.9)
  * `destroy` **(Defensive Guards)** (Impact: 9.6)
  * `getReader` **(Callbacks & Closures)** (Impact: 9.1)
  * `handleStart` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 22
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 78`, `args: 44`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 20`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.347
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.081059
  * `Imports (Out-Degree: 1):` utils.js, promise-helpers, node:buffer, node:events, node:stream, promises
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/cjs/Request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.002)
- **Top Global Matches:** file_cluster_6: 12.002, file_cluster_4: 13.185, file_cluster_12: 16.495
- **Magnitude:** 215.46 | **LOC:** 129 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 9.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (71.2%), Connectivity (formerly Api Exposure) (61.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 95.0)
  * `url` **(I/O & Config Routines)** (Impact: 4.5)
  * `parsedUrl` **(I/O & Config Routines)** (Impact: 4.5)
  * `isURL` **(Defensive Guards)** (Impact: 3.0)
  * `signal` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 13`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 33`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.488
  * `Choke Point (Betweenness):` 0.000818 | `Ripple Effect (Closeness):` 0.032258
  * `Imports (Out-Degree: 3):` Body.js, Headers.js, URL.js, node:http, node:https
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/Request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.708)
- **Top Global Matches:** file_cluster_6: 11.708, file_cluster_4: 12.907, file_cluster_12: 16.39
- **Magnitude:** 212.38 | **LOC:** 125 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 9.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.9%), Guard Balance (formerly Safety Score) (70.3%), Connectivity (formerly Api Exposure) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 95.0)
  * `url` **(I/O & Config Routines)** (Impact: 4.5)
  * `parsedUrl` **(I/O & Config Routines)** (Impact: 4.5)
  * `isURL` **(Defensive Guards)** (Impact: 3.0)
  * `signal` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.488
  * `Choke Point (Betweenness):` 0.000818 | `Ripple Effect (Closeness):` 0.032258
  * `Imports (Out-Degree: 3):` Body.js, Headers.js, URL.js, node:http, node:https
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/cjs/FormData.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.669)
- **Top Global Matches:** file_cluster_12: 7.669, file_cluster_4: 7.744, file_cluster_15: 8.846
- **Magnitude:** 165.78 | **LOC:** 151 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 9.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.2%), Concurrency Surface (formerly Concurrency) (68.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` **(Defensive Guards)** (Impact: 30.9)
  * `handleNextEntry` **(Defensive Guards)** (Impact: 11.3)
  * `pull` **(Callbacks & Closures)** (Impact: 9.5)
  * `cancel` **(Defensive Guards)** (Impact: 7.3)
  * `append` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 34`, `args: 21`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`
* *Architecture:* `api: 11`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.451
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.035125
  * `Imports (Out-Degree: 2):` IteratorObject.js, ReadableStream.js, node:buffer
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/esm/FormData.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.36)
- **Top Global Matches:** file_cluster_4: 7.36, file_cluster_15: 8.158, file_cluster_12: 8.238
- **Magnitude:** 159.68 | **LOC:** 146 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 9.451; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (69.9%), Connectivity (formerly Api Exposure) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` **(Defensive Guards)** (Impact: 30.9)
  * `handleNextEntry` **(Defensive Guards)** (Impact: 11.3)
  * `pull` **(Callbacks & Closures)** (Impact: 9.5)
  * `cancel` **(Defensive Guards)** (Impact: 7.3)
  * `append` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 39`, `args: 21`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.451
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.035125
  * `Imports (Out-Degree: 2):` IteratorObject.js, ReadableStream.js, node:buffer
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/cjs/Response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.004)
- **Top Global Matches:** file_cluster_8: 9.004, file_cluster_6: 18.074, file_cluster_3: 21.025
- **Magnitude:** 150.26 | **LOC:** 109 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 12.705; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(Defensive Guards)** (Impact: 47.8)
  * `constructor` **(Defensive Guards)** (Impact: 30.1)
  * `redirect` **(Compute Cores)** (Impact: 5.7)
  * `ok` **(Interface Declarations)** (Impact: 2.1)
  * `error` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.705
  * `Choke Point (Betweenness):` 0.001636 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 2):` Body.js, Headers.js, node:http
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/esm/Response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.343)
- **Top Global Matches:** file_cluster_8: 8.343, file_cluster_6: 17.771, file_cluster_3: 20.743
- **Magnitude:** 147.18 | **LOC:** 105 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 12.705; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(Defensive Guards)** (Impact: 47.8)
  * `constructor` **(Defensive Guards)** (Impact: 30.1)
  * `redirect` **(Compute Cores)** (Impact: 5.7)
  * `ok` **(Interface Declarations)** (Impact: 2.1)
  * `error` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 15`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.705
  * `Choke Point (Betweenness):` 0.001636 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 2):` Body.js, Headers.js, node:http
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/cjs/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.208)
- **Top Global Matches:** file_cluster_8: 10.208, file_cluster_6: 18.735, file_cluster_3: 21.551
- **Magnitude:** 138.38 | **LOC:** 156 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 7.569; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (75.6%), Complexity Load (formerly Cognitive Load) (75.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` **(Compute Cores)** (Impact: 74.5)
  * `getRequestFnForProtocol` **(Compute Cores)** (Impact: 6.1)
  * `onError` **(Callbacks & Closures)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 23`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 15`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014337
  * `Imports (Out-Degree: 4):` Request.js, Response.js, URL.js, utils.js, promise-helpers, node:http, node:https, node:stream...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/esm/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.285)
- **Top Global Matches:** file_cluster_8: 10.285, file_cluster_6: 18.77, file_cluster_3: 21.593
- **Magnitude:** 128.8 | **LOC:** 152 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 7.569; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (76.9%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` **(Compute Cores)** (Impact: 66.0)
  * `getRequestFnForProtocol` **(Compute Cores)** (Impact: 6.1)
  * `onError` **(Callbacks & Closures)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 33`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014337
  * `Imports (Out-Degree: 4):` Request.js, Response.js, URL.js, utils.js, promise-helpers, node:http, node:https, node:stream...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/cjs/fetchCurl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.169)
- **Top Global Matches:** file_cluster_6: 8.169, file_cluster_8: 12.703, file_cluster_4: 14.558
- **Magnitude:** 118.94 | **LOC:** 143 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 7.569; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.4%), Concurrency Surface (formerly Concurrency) (70.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchCurl` **(Defensive Guards)** (Impact: 56.2)
  * `streamListener` **(Defensive Guards)** (Impact: 21.6)
  * `errorListener` **(Defensive Guards)** (Impact: 9.3)
  * `onAbort` **(Defensive Guards)** (Impact: 2.5)
  * `endListener` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 11`, `args: 10`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014337
  * `Imports (Out-Degree: 2):` Response.js, utils.js, promise-helpers, node:stream, node:tls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/esm/fetchCurl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.203)
- **Top Global Matches:** file_cluster_6: 8.203, file_cluster_8: 12.728, file_cluster_4: 14.578
- **Magnitude:** 117.88 | **LOC:** 140 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 7.569; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (79.3%), Concurrency Surface (formerly Concurrency) (71.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchCurl` **(Defensive Guards)** (Impact: 56.2)
  * `streamListener` **(Defensive Guards)** (Impact: 21.6)
  * `errorListener` **(Defensive Guards)** (Impact: 9.3)
  * `onAbort` **(Defensive Guards)** (Impact: 2.5)
  * `endListener` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 17`, `args: 10`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014337
  * `Imports (Out-Degree: 2):` Response.js, utils.js, promise-helpers, node:stream, node:tls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/cjs/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.001)
- **Top Global Matches:** file_cluster_7: 8.001, file_cluster_12: 9.201, file_cluster_5: 10.201
- **Magnitude:** 112.1 | **LOC:** 126 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **4**; blast radius 92.36; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Connectivity (formerly Api Exposure) (91.9%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (53.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeThrough` **(Defensive Guards)** (Impact: 14.9)
  * `getHeadersObj` **(Compute Cores)** (Impact: 9.0)
  * `getSupportedFormats` **(Defensive Guards)** (Impact: 7.5)
  * `shouldRedirect` **(Defensive Guards)** (Impact: 7.2)
  * `isArrayBufferView` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 20`, `args: 18`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 16`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 92.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.149297
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:zlib, tslib
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `package/cjs/IteratorObject.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.661)
- **Top Global Matches:** file_cluster_15: 5.661, file_cluster_12: 6.556, file_cluster_10: 7.358
- **Magnitude:** 109.28 | **LOC:** 135 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 23.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.3%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flatMap` **(Compute Cores)** (Impact: 9.4)
  * `take` **(Compute Cores)** (Impact: 4.8)
  * `filter` **(Compute Cores)** (Impact: 4.7)
  * `drop` **(Compute Cores)** (Impact: 4.7)
  * `some` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 39`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.662
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.048387
  * `Imports (Out-Degree: 1):` utils.js, disposablestack, node:util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/IteratorObject.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.964)
- **Top Global Matches:** file_cluster_15: 4.964, file_cluster_10: 6.869, file_cluster_13: 7.658
- **Magnitude:** 106.2 | **LOC:** 131 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 23.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.6%), Guard Balance (formerly Safety Score) (61.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flatMap` **(Compute Cores)** (Impact: 9.4)
  * `take` **(Compute Cores)** (Impact: 4.8)
  * `filter` **(Compute Cores)** (Impact: 4.7)
  * `drop` **(Compute Cores)** (Impact: 4.7)
  * `some` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 43`, `args: 16`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.662
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.048387
  * `Imports (Out-Degree: 1):` utils.js, disposablestack, node:util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/esm/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.21)
- **Top Global Matches:** file_cluster_7: 8.21, file_cluster_12: 9.465, file_cluster_5: 10.329
- **Magnitude:** 97.8 | **LOC:** 111 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **3**; blast radius 92.36; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Mutation Surface (formerly State Flux) (85.9%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeThrough` **(Defensive Guards)** (Impact: 14.9)
  * `getHeadersObj` **(Compute Cores)** (Impact: 9.0)
  * `shouldRedirect` **(Defensive Guards)** (Impact: 7.2)
  * `getSupportedFormats` **(Defensive Guards)** (Impact: 6.5)
  * `isArrayBufferView` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 32`, `args: 17`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 92.36
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.149297
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:zlib
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `package/cjs/WritableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_12: 6.997, file_cluster_10: 8.445, file_cluster_15: 9.252
- **Magnitude:** 90.88 | **LOC:** 116 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 11.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.4%), Mutation Surface (formerly State Flux) (85.9%), Connectivity (formerly Api Exposure) (66.4%), Guard Balance (formerly Safety Score) (51.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 18.2)
  * `write` **(Defensive Guards)** (Impact: 8.9)
  * `getWriter` **(Callbacks & Closures)** (Impact: 6.8)
  * `final` **(Defensive Guards)** (Impact: 6.3)
  * `close` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 23`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 8`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.351
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.033602
  * `Imports (Out-Degree: 1):` utils.js, promise-helpers, node:events, node:stream
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/esm/WritableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.515)
- **Top Global Matches:** file_cluster_10: 7.515, file_cluster_12: 7.594, file_cluster_15: 8.416
- **Magnitude:** 87.8 | **LOC:** 112 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 11.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.5%), Mutation Surface (formerly State Flux) (77.5%), Connectivity (formerly Api Exposure) (63.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 18.2)
  * `write` **(Defensive Guards)** (Impact: 8.9)
  * `getWriter` **(Callbacks & Closures)** (Impact: 6.8)
  * `final` **(Defensive Guards)** (Impact: 6.3)
  * `close` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 29`, `args: 23`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 7`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.351
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.033602
  * `Imports (Out-Degree: 1):` utils.js, promise-helpers, node:events, node:stream
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/cjs/TransformStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_12: 6.755, file_cluster_10: 8.203, file_cluster_11: 8.434
- **Magnitude:** 72.48 | **LOC:** 80 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 15.702; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Connectivity (formerly Api Exposure) (85.5%), Complexity Load (formerly Cognitive Load) (74.7%), Concurrency Surface (formerly Concurrency) (74.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 18.9)
  * `write` **(Defensive Guards)** (Impact: 8.9)
  * `final` **(Defensive Guards)** (Impact: 6.6)
  * `enqueue` **(State Mutators)** (Impact: 1.6)
  * `error` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 6`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`
* *Architecture:* `api: 10`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.702
  * `Choke Point (Betweenness):` 0.000771 | `Ripple Effect (Closeness):` 0.043011
  * `Imports (Out-Degree: 3):` ReadableStream.js, WritableStream.js, utils.js, node:stream
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `package/typings/URL.d.cts` (TYPESCRIPT) | Magnitude: 15.82 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, globals: 9, structural_boundaries: 8, args: 7
- `package/typings/URL.d.ts` (TYPESCRIPT) | Magnitude: 0.79 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, globals: 9, structural_boundaries: 8, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `package/esm/WritableStream.js` (JAVASCRIPT) | Magnitude: 87.8 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 29, args: 23, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/cjs/FormData.js` (JAVASCRIPT) | Magnitude: 165.78 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 34, branch: 28, core_var_decl: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/esm/index.js` (JAVASCRIPT) | Magnitude: 33.36 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, api: 18, import: 18, io: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `package/typings/Blob.d.cts` (TYPESCRIPT) | Magnitude: 56.64 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 23, func_start: 23
- `package/typings/Blob.d.ts` (TYPESCRIPT) | Magnitude: 2.83 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 27, args: 23, func_start: 23

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/cjs/Body.js` -> **Severity: 0.258** (Bridge: 0.0026 * Flux: 99.996%)
- `package/esm/Body.js` -> **Severity: 0.258** (Bridge: 0.0026 * Flux: 99.995%)
- `package/cjs/Response.js` -> **Severity: 0.164** (Bridge: 0.0016 * Flux: 100.0%)
- `package/esm/Response.js` -> **Severity: 0.164** (Bridge: 0.0016 * Flux: 100.0%)
- `package/cjs/Request.js` -> **Severity: 0.082** (Bridge: 0.0008 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/cjs/utils.js` -> **Severity: 11.944** (Embedded: 0.1493 * Error Risk: 80.0%)
- `package/esm/utils.js` -> **Severity: 11.944** (Embedded: 0.1493 * Error Risk: 80.0%)
- `package/cjs/ReadableStream.js` -> **Severity: 4.602** (Embedded: 0.0811 * Error Risk: 56.7762%)
- `package/esm/ReadableStream.js` -> **Severity: 4.503** (Embedded: 0.0811 * Error Risk: 55.5539%)
- `package/cjs/IteratorObject.js` -> **Severity: 3.049** (Embedded: 0.0484 * Error Risk: 63.0058%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/utils.js` -> **Severity: 9236.0** (Blast Radius: 92.36 * Doc Risk: 100.0%)
- `package/esm/utils.js` -> **Severity: 9236.0** (Blast Radius: 92.36 * Doc Risk: 100.0%)
- `package/cjs/ReadableStream.js` -> **Severity: 2534.7** (Blast Radius: 25.347 * Doc Risk: 100.0%)
- `package/esm/ReadableStream.js` -> **Severity: 2534.7** (Blast Radius: 25.347 * Doc Risk: 100.0%)
- `package/cjs/IteratorObject.js` -> **Severity: 2366.2** (Blast Radius: 23.662 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1004 call pairs -- scoped 34.7%, unique 0.0%, ambiguous 14.3%, external 51.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1004 | 34.7% | 0.0% | 14.3% | 51.0% |

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
