# ARCHITECTURAL_BRIEF: @whatwg-node_node-fetch
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 94 analyzed artifact(s), 6351 LOC.
- **Load-bearing artifact:** none identifiable. No file in this repository is imported by another that GitGalaxy could resolve, so there is no dependency hierarchy to report. That is itself a finding: either this is a collection of independent scripts/documents rather than a coupled system, or the import style is one the engine does not resolve for these languages.
- **Top orchestrator:** `package/cjs/index.js` -- pulls in 18 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/cjs/Body.js` at magnitude 441.42 (structural weight, not risk).
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
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 46 | 5551 | 48.9% |
| TYPESCRIPT | 46 | 800 | 48.9% |
| PLAINTEXT | 2 | 0 | 2.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `1.479`
> **Composition Archetype:** `Small Flat Repo` (z +1.48; from the repo's file-archetype mix)
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.3 | 27.8 | 10.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.4 | 51.0 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 39.1 | 14.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.1 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 1.8 | 91.9 | 28.9 | 14.0 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 38.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.1 | 0.4 | 0.0 | 0.0 |
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
| connectivity | 456 | 92 | 12 | `package/cjs/index.js` |
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
| dead_code | 238 | 46 | 11 | `package/typings/Headers.d.cts` |
| credential | 0 | 0 | 0 | - |
| threat | 59 | 31 | 1 | `package/cjs/index.js` |
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
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/cjs/index.js`) — 18 outbound dependencies
2. **index.js** (`package/esm/index.js`) — 18 outbound dependencies
3. **index.d.cts** (`package/typings/index.d.cts`) — 18 outbound dependencies
4. **index.d.ts** (`package/typings/index.d.ts`) — 18 outbound dependencies
5. **fetchNodeHttp.js** (`package/cjs/fetchNodeHttp.js`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `constructor` **(Defensive Guards)** (@ `package/cjs/Request.js`) -> Impact: **96.7** | LOC: 64
- `constructor` **(Defensive Guards)** (@ `package/esm/Request.js`) -> Impact: **96.7** | LOC: 64
- `fetchNodeHttp` **(Compute Cores)** (@ `package/cjs/fetchNodeHttp.js`) -> Impact: **74.5** | LOC: 133
- `fetchNodeHttp` **(Compute Cores)** (@ `package/esm/fetchNodeHttp.js`) -> Impact: **66.0** | LOC: 133
- `fetchCurl` **(Defensive Guards)** (@ `package/cjs/fetchCurl.js`) -> Impact: **56.2** | LOC: 134
- `fetchCurl` **(Defensive Guards)** (@ `package/esm/fetchCurl.js`) -> Impact: **56.2** | LOC: 134
- `json` **(Defensive Guards)** (@ `package/cjs/Response.js`) -> Impact: **47.8** | LOC: 55
- `json` **(Defensive Guards)** (@ `package/esm/Response.js`) -> Impact: **47.8** | LOC: 55
- `formData` **(Defensive Guards)** (@ `package/cjs/Body.js`) -> Impact: **40.6** | LOC: 105
- `formData` **(Defensive Guards)** (@ `package/esm/Body.js`) -> Impact: **40.6** | LOC: 105

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/cjs` | 24 | 2747.26 | 47.5% | 4.24% |
| `package/esm` | 23 | 2613.96 | 42.07% | 4.43% |
| `package/typings` | 46 | 420.94 | 9.84% | 73.81% |
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
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/cjs/Body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 441.42 | **LOC:** 530 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.7%), Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formData` **(Defensive Guards)** (Impact: 40.6)
  * `processBodyInit` **(Defensive Guards)** (Impact: 28.2)
  * `complete` **(Defensive Guards)** (Impact: 24.5)
  * `handleContentLengthHeader` **(Compute Cores)** (Impact: 15.3)
  * `buffer` **(Callbacks & Closures)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 114`, `args: 61`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 69`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 39`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Blob.js, File.js, FormData.js, ReadableStream.js, utils.js, busboy, promise-helpers, node:buffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Body.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 436.34 | **LOC:** 526 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.7%), Complexity Load (formerly Cognitive Load) (92.6%), Guard Balance (formerly Safety Score) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formData` **(Defensive Guards)** (Impact: 40.6)
  * `processBodyInit` **(Defensive Guards)** (Impact: 28.2)
  * `complete` **(Defensive Guards)** (Impact: 24.5)
  * `handleContentLengthHeader` **(Compute Cores)** (Impact: 15.3)
  * `buffer` **(Callbacks & Closures)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 124`, `args: 61`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 67`, `duplicate_logic: 3`
* *Architecture:* `api: 7`, `concurrency: 8`, `import: 9`
* *Defense:* `safety: 39`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Blob.js, File.js, FormData.js, ReadableStream.js, utils.js, busboy, promise-helpers, node:buffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Blob.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 318.6 | **LOC:** 292 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.7%), Guard Balance (formerly Safety Score) (87.0%)
- **Documentation Coverage:** 96.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buffer` **(Callbacks & Closures)** (Impact: 17.8)
  * `constructor` **(Defensive Guards)** (Impact: 16.0)
  * `stream` **(Callbacks & Closures)** (Impact: 13.1)
  * `getBlobPartAsBuffer` **(Defensive Guards)** (Impact: 10.6)
  * `pull` **(Callbacks & Closures)** (Impact: 10.0)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, utils.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Blob.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 307.36 | **LOC:** 280 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.1%), Guard Balance (formerly Safety Score) (84.7%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buffer` **(Callbacks & Closures)** (Impact: 17.8)
  * `constructor` **(Defensive Guards)** (Impact: 16.0)
  * `stream` **(Callbacks & Closures)** (Impact: 13.1)
  * `getBlobPartAsBuffer` **(Defensive Guards)** (Impact: 10.6)
  * `pull` **(Callbacks & Closures)** (Impact: 10.0)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, utils.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Headers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 251.98 | **LOC:** 310 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (69.9%), Connectivity (formerly Api Exposure) (57.9%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Headers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 245.88 | **LOC:** 305 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (66.9%), Connectivity (formerly Api Exposure) (55.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/ReadableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 240.88 | **LOC:** 246 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%)
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
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 71`, `args: 44`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`
* *Architecture:* `api: 8`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 20`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, node:buffer, node:events, node:stream, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/ReadableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 235.8 | **LOC:** 242 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 31.7)
  * `createController` **(Defensive Guards)** (Impact: 15.9)
  * `destroy` **(Defensive Guards)** (Impact: 9.6)
  * `getReader` **(Callbacks & Closures)** (Impact: 9.1)
  * `handleStart` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 22
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 78`, `args: 44`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 20`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, node:buffer, node:events, node:stream, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 217.16 | **LOC:** 129 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.3%), Guard Balance (formerly Safety Score) (95.1%), Connectivity (formerly Api Exposure) (61.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 96.7)
  * `url` **(I/O & Config Routines)** (Impact: 4.5)
  * `parsedUrl` **(I/O & Config Routines)** (Impact: 4.5)
  * `isURL` **(Defensive Guards)** (Impact: 3.0)
  * `signal` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 13`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 33`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, Headers.js, URL.js, node:http, node:https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 214.08 | **LOC:** 125 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Guard Balance (formerly Safety Score) (94.4%), Connectivity (formerly Api Exposure) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 96.7)
  * `url` **(I/O & Config Routines)** (Impact: 4.5)
  * `parsedUrl` **(I/O & Config Routines)** (Impact: 4.5)
  * `isURL` **(Defensive Guards)** (Impact: 3.0)
  * `signal` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, Headers.js, URL.js, node:http, node:https
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/FormData.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 171.08 | **LOC:** 151 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` **(Defensive Guards)** (Impact: 32.6)
  * `handleNextEntry` **(Defensive Guards)** (Impact: 12.8)
  * `pull` **(Callbacks & Closures)** (Impact: 9.5)
  * `cancel` **(Defensive Guards)** (Impact: 7.4)
  * `append` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 34`, `args: 21`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`
* *Architecture:* `api: 11`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, ReadableStream.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/FormData.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 164.98 | **LOC:** 146 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Concurrency Surface (formerly Concurrency) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getStreamFromFormData` **(Defensive Guards)** (Impact: 32.6)
  * `handleNextEntry` **(Defensive Guards)** (Impact: 12.8)
  * `pull` **(Callbacks & Closures)** (Impact: 9.5)
  * `cancel` **(Defensive Guards)** (Impact: 7.4)
  * `append` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 39`, `args: 21`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IteratorObject.js, ReadableStream.js, node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 158.78 | **LOC:** 156 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` **(Compute Cores)** (Impact: 74.5)
  * `onError` **(Defensive Guards)** (Impact: 23.7)
  * `getRequestFnForProtocol` **(Compute Cores)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 23`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 15`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Request.js, Response.js, URL.js, utils.js, promise-helpers, node:http, node:https, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/Response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 151.96 | **LOC:** 109 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Complexity Load (formerly Cognitive Load) (86.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(Defensive Guards)** (Impact: 47.8)
  * `constructor` **(Defensive Guards)** (Impact: 31.8)
  * `redirect` **(Compute Cores)** (Impact: 5.7)
  * `ok` **(Interface Declarations)** (Impact: 2.1)
  * `error` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, Headers.js, node:http
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchNodeHttp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 149.2 | **LOC:** 152 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchNodeHttp` **(Compute Cores)** (Impact: 66.0)
  * `onError` **(Defensive Guards)** (Impact: 23.7)
  * `getRequestFnForProtocol` **(Compute Cores)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 33`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Request.js, Response.js, URL.js, utils.js, promise-helpers, node:http, node:https, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/Response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 148.88 | **LOC:** 105 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(Defensive Guards)** (Impact: 47.8)
  * `constructor` **(Defensive Guards)** (Impact: 31.8)
  * `redirect` **(Compute Cores)** (Impact: 5.7)
  * `ok` **(Interface Declarations)** (Impact: 2.1)
  * `error` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 15`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 17`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Body.js, Headers.js, node:http
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/fetchCurl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 118.94 | **LOC:** 143 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.4%), Concurrency Surface (formerly Concurrency) (70.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.5%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Response.js, utils.js, promise-helpers, node:stream, node:tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/fetchCurl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 117.88 | **LOC:** 140 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (79.3%), Concurrency Surface (formerly Concurrency) (71.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Response.js, utils.js, promise-helpers, node:stream, node:tls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 112.1 | **LOC:** 126 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.638; role: Isolated/Orphan
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
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 16`, `dead_code: 2`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:signal, node:zlib, tslib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/IteratorObject.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 109.58 | **LOC:** 135 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.3%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, disposablestack, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/IteratorObject.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 106.5 | **LOC:** 131 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.6%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, disposablestack, node:util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 97.8 | **LOC:** 111 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.638; role: Isolated/Orphan
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
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 4`, `dead_code: 2`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promise-helpers, node:events, node:signal, node:zlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/WritableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 90.88 | **LOC:** 116 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.4%), Mutation Surface (formerly State Flux) (85.9%), Connectivity (formerly Api Exposure) (66.4%), Guard Balance (formerly Safety Score) (61.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, node:events, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/WritableStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 87.8 | **LOC:** 112 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.638; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.5%), Mutation Surface (formerly State Flux) (77.5%), Connectivity (formerly Api Exposure) (63.3%), Guard Balance (formerly Safety Score) (55.7%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promise-helpers, node:events, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/TransformStream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 72.48 | **LOC:** 80 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.638; role: Isolated/Orphan
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReadableStream.js, WritableStream.js, utils.js, node:stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/AbortError.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/Body.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/CompressionStream.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/DecompressionStream.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)
- `package/cjs/File.js` -> **Severity: 1063.8** (Blast Radius: 10.638 * Doc Risk: 100.0%)

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
