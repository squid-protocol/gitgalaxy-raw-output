# ARCHITECTURAL_BRIEF: @workos-inc_node
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
- **Scope:** 12 analyzed artifact(s), 24488 LOC.
- **Load-bearing artifact:** `package/lib/factory-BraleEZU.cjs` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/factory-BraleEZU.cjs` -- pulls in 2 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/webapi-N7c2LUJd.cjs` at magnitude 3970.5 (structural weight, not risk).
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
| Total Artifacts | 25 |
| Analyzed Artifacts (Scanned) | 12 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 24488 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 48.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 8 | 16246 | 66.7% |
| TYPESCRIPT | 2 | 8242 | 16.7% |
| MARKDOWN | 1 | 0 | 8.3% |
| PLAINTEXT | 1 | 0 | 8.3% |

## 4.1 SOURCE ENCODINGS
All 12 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 33%, Data / Markup / Trivial 17%, Generic / Templated Code Files 17%, Large Core Modules (2) 17%, Parameter Forwarders Files 17%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10 | 83.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 16.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `.map`: 8x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.cts`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.mts`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 12.5 | 99.3 | 52.6 | 47.3 | 14.3 |
| Guard Balance (formerly Error & Exception Exposure) | 44.5 | 66.6 | 53.7 | 51.7 | 51.7 |
| Debt Markers (formerly Tech Debt Exposure) | 16.8 | 99.9 | 77.8 | 96.5 | 96.5 |
| Test Surface (formerly Testing Exposure) | 2.4 | 80.0 | 33.5 | 2.8 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 68.9 | 20.6 | 9.9 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 57.1 | 85.4 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 73.4 | 96.3 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.7 | 79.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 25.0 | 4.9 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 22 | 6 | 7 | `package/lib/factory-BraleEZU.cjs` |
| cleanup | 14 | 4 | 5 | `package/lib/factory-BraleEZU.cjs` |
| guards | 2144 | 10 | 590 | `package/lib/webapi-CxKOxXjo.mjs` |
| danger | 1188 | 6 | 332 | `package/lib/webapi-CxKOxXjo.mjs` |
| concurrency | 1706 | 6 | 483 | `package/lib/factory-BraleEZU.cjs` |
| connectivity | 356 | 8 | 124 | `package/lib/factory-IqQiyE5J.mjs` |
| io | 60 | 6 | 24 | `package/lib/workos-COj1yMhR.d.cts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 66 | 4 | 23 | `package/lib/factory-BraleEZU.cjs` |
| serialization | 40 | 4 | 13 | `package/lib/webapi-CxKOxXjo.mjs` |
| regex | 48 | 4 | 12 | `package/lib/factory-BraleEZU.cjs` |
| events | 55 | 6 | 24 | `package/lib/factory-IqQiyE5J.mjs` |
| tests | 0 | 0 | 0 | - |
| docs | 362 | 8 | 134 | `package/lib/workos-COj1yMhR.d.cts` |
| debt | 194 | 8 | 46 | `package/lib/webapi-CxKOxXjo.mjs` |
| mutation | 3923 | 10 | 913 | `package/lib/factory-BraleEZU.cjs` |
| dead_code | 342 | 6 | 162 | `package/lib/workos-COj1yMhR.d.cts` |
| credential | 4 | 2 | 2 | `package/lib/webapi-CxKOxXjo.mjs` |
| threat | 18 | 4 | 7 | `package/lib/factory-BraleEZU.cjs` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.3859**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/workos-COj1yMhR.d.cts` (Hits: 24)
- `package/lib/workos-DluXltJr.d.mts` (Hits: 24)
- `package/lib/factory-BraleEZU.cjs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **factory-BraleEZU.cjs** (`package/lib/factory-BraleEZU.cjs`) — 2 inbound connections
2. **factory-IqQiyE5J.mjs** (`package/lib/factory-IqQiyE5J.mjs`) — 2 inbound connections
3. **webapi-CxKOxXjo.mjs** (`package/lib/webapi-CxKOxXjo.mjs`) — 1 inbound connections
4. **webapi-N7c2LUJd.cjs** (`package/lib/webapi-N7c2LUJd.cjs`) — 1 inbound connections
5. **README.md** (`package/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **factory-BraleEZU.cjs** (`package/lib/factory-BraleEZU.cjs`) — 2 outbound dependencies
2. **factory-IqQiyE5J.mjs** (`package/lib/factory-IqQiyE5J.mjs`) — 2 outbound dependencies
3. **index.cjs** (`package/lib/index.cjs`) — 1 outbound dependencies
4. **index.mjs** (`package/lib/index.mjs`) — 1 outbound dependencies
5. **index.worker.cjs** (`package/lib/index.worker.cjs`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `flattenedDecrypt` **(Defensive Guards)** (@ `package/lib/webapi-CxKOxXjo.mjs`) -> Impact: **132.0** | LOC: 80
  * *Intent:* //#endregion //#region node_modules/jose/dist/webapi/jwe/flattened/decrypt.js
- `flattenedDecrypt` **(Defensive Guards)** (@ `package/lib/webapi-N7c2LUJd.cjs`) -> Impact: **132.0** | LOC: 80
  * *Intent:* //#endregion //#region node_modules/jose/dist/webapi/jwe/flattened/decrypt.js
- `deserializeEvent` **(Compute Cores)** (@ `package/lib/factory-BraleEZU.cjs`) -> Impact: **118.4** | LOC: 219
  * *Intent:* //#endregion //#region src/common/serializers/event.serializer.ts
- `deserializeEvent` **(Compute Cores)** (@ `package/lib/factory-IqQiyE5J.mjs`) -> Impact: **118.4** | LOC: 219
  * *Intent:* //#endregion //#region src/common/serializers/event.serializer.ts
- `decryptKeyManagement` **(Defensive Guards)** (@ `package/lib/webapi-CxKOxXjo.mjs`) -> Impact: **98.9** | LOC: 68
- `decryptKeyManagement` **(Defensive Guards)** (@ `package/lib/webapi-N7c2LUJd.cjs`) -> Impact: **98.9** | LOC: 68
- `handleKeyObject` **(Defensive Guards)** (@ `package/lib/webapi-CxKOxXjo.mjs`) -> Impact: **92.6** | LOC: 86
- `handleKeyObject` **(Defensive Guards)** (@ `package/lib/webapi-N7c2LUJd.cjs`) -> Impact: **92.6** | LOC: 86
- `encryptKeyManagement` **(Many-Argument Workhorses)** (@ `package/lib/webapi-CxKOxXjo.mjs`) -> Impact: **89.4** | LOC: 74
- `encryptKeyManagement` **(Many-Argument Workhorses)** (@ `package/lib/webapi-N7c2LUJd.cjs`) -> Impact: **89.4** | LOC: 74

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 10 | 16899.96 | 52.63% | 77.79% |
| `package` | 2 | 4.36 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/index.worker.mjs` -> **99.9447%** Exposure
- `package/lib/index.worker.cjs` -> **99.9188%** Exposure
- `package/lib/index.mjs` -> **99.593%** Exposure
- `package/lib/index.cjs` -> **98.6342%** Exposure
- `package/lib/workos-COj1yMhR.d.cts` -> **96.4828%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/index.cjs` -> **100.0%** Exposure
- `package/lib/index.worker.cjs` -> **100.0%** Exposure
- `package/lib/webapi-N7c2LUJd.cjs` -> **99.9913%** Exposure
- `package/lib/webapi-CxKOxXjo.mjs` -> **99.9875%** Exposure
- `package/lib/factory-IqQiyE5J.mjs` -> **96.6852%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/workos-COj1yMhR.d.cts` -> **162** Orphaned Functions | **31** Duplicates
- `package/lib/workos-DluXltJr.d.mts` -> **162** Orphaned Functions | **31** Duplicates
- `package/lib/webapi-CxKOxXjo.mjs` -> **0** Orphaned Functions | **46** Duplicates
- `package/lib/webapi-N7c2LUJd.cjs` -> **0** Orphaned Functions | **46** Duplicates
- `package/lib/factory-BraleEZU.cjs` -> **0** Orphaned Functions | **18** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `package/lib/webapi-CxKOxXjo.mjs` -> **24.9728%** Exposure
- `package/lib/webapi-N7c2LUJd.cjs` -> **24.4544%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/webapi-N7c2LUJd.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.604)
- **Top Global Matches:** file_cluster_4: 8.604, file_cluster_12: 10.371, file_cluster_15: 12.533
- **Magnitude:** 3970.5 | **LOC:** 3267 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 164.833; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.3%), Debt Markers (formerly Tech Debt) (75.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flattenedDecrypt` **(Defensive Guards)** (Impact: 132.0)
    * *Intent:* //#endregion //#region node_modules/jose/dist/webapi/jwe/flattened/decrypt.js
  * `decryptKeyManagement` **(Defensive Guards)** (Impact: 98.9)
  * `handleKeyObject` **(Defensive Guards)** (Impact: 92.6)
  * `encryptKeyManagement` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `validateClaimsSet` **(Defensive Guards)** (Impact: 78.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 57 instances
* *Amplified Cascading Flux:* 286 instances
* *Concurrency (weighted view):* 457
* *State Mutation (weighted view):* 927
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1127`, `structural_boundaries: 729`, `args: 297`, `func_start: 294`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 355`, `duplicate_logic: 46`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 172`
* *Defense:* `safety: 543`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 164.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163636
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/webapi-CxKOxXjo.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.638)
- **Top Global Matches:** file_cluster_4: 8.638, file_cluster_12: 10.426, file_cluster_15: 12.604
- **Magnitude:** 3890.36 | **LOC:** 3220 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 164.833; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Debt Markers (formerly Tech Debt) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flattenedDecrypt` **(Defensive Guards)** (Impact: 132.0)
    * *Intent:* //#endregion //#region node_modules/jose/dist/webapi/jwe/flattened/decrypt.js
  * `decryptKeyManagement` **(Defensive Guards)** (Impact: 98.9)
  * `handleKeyObject` **(Defensive Guards)** (Impact: 92.6)
  * `encryptKeyManagement` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `validateClaimsSet` **(Defensive Guards)** (Impact: 78.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 57 instances
* *Amplified Cascading Flux:* 283 instances
* *Concurrency (weighted view):* 457
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1127`, `structural_boundaries: 728`, `args: 295`, `func_start: 292`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 319`, `duplicate_logic: 46`
* *Architecture:* `io: 1`, `api: 7`, `concurrency: 172`
* *Defense:* `safety: 543`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 164.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.163636
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/factory-BraleEZU.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.584)
- **Top Global Matches:** file_cluster_12: 10.584, file_cluster_15: 12.395, file_cluster_4: 13.066
- **Magnitude:** 3605.76 | **LOC:** 5254 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 135.068; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.9%), Complexity Load (formerly Cognitive Load) (85.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.8486% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserializeEvent` **(Compute Cores)** (Impact: 118.4)
    * *Intent:* //#endregion //#region src/common/serializers/event.serializer.ts
  * `constructor` **(Defensive Guards)** (Impact: 60.8)
    * *Intent:* * * // Server-side with API key (string) * const workos = new WorkOS('sk_...'); * * // Server-side w...
  * `fetchRequest` **(Defensive Guards)** (Impact: 47.7)
  * `unseal` **(Defensive Guards)** (Impact: 33.4)
  * `isJson` **(Defensive Guards)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 80 instances
* *Amplified Cascading Flux:* 168 instances
* *Concurrency (weighted view):* 872
* *State Mutation (weighted view):* 698
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 1139`, `args: 605`, `func_start: 543`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 362`, `duplicate_logic: 18`
* *Architecture:* `io: 5`, `api: 122`, `concurrency: 472`, `import: 5`
* *Defense:* `safety: 297`, `doc: 39`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 135.068
  * `Choke Point (Betweenness):` 0.018182 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 1):` webapi-N7c2LUJd.cjs, eventemitter3
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/factory-IqQiyE5J.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.251)
- **Top Global Matches:** file_cluster_12: 10.251, file_cluster_15: 12.123, file_cluster_4: 12.776
- **Magnitude:** 3565.74 | **LOC:** 5063 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 135.068; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.7%), Complexity Load (formerly Cognitive Load) (85.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.5216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserializeEvent` **(Compute Cores)** (Impact: 118.4)
    * *Intent:* //#endregion //#region src/common/serializers/event.serializer.ts
  * `constructor` **(Defensive Guards)** (Impact: 60.8)
    * *Intent:* * * // Server-side with API key (string) * const workos = new WorkOS('sk_...'); * * // Server-side w...
  * `fetchRequest` **(Defensive Guards)** (Impact: 47.7)
  * `unseal` **(Defensive Guards)** (Impact: 33.4)
  * `isJson` **(Defensive Guards)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 80 instances
* *Amplified Cascading Flux:* 168 instances
* *Concurrency (weighted view):* 870
* *State Mutation (weighted view):* 698
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 1108`, `args: 572`, `func_start: 511`
* *Risk/State:* `safety_bypasses: 113`, `state_mutation: 362`, `duplicate_logic: 18`
* *Architecture:* `io: 5`, `api: 123`, `concurrency: 470`, `import: 5`
* *Defense:* `safety: 297`, `doc: 39`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 135.068
  * `Choke Point (Betweenness):` 0.018182 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 1):` webapi-CxKOxXjo.mjs, eventemitter3
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/workos-COj1yMhR.d.cts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.293)
- **Top Global Matches:** file_cluster_0: 7.293, file_cluster_5: 8.353, file_cluster_12: 8.951
- **Magnitude:** 831.12 | **LOC:** 5202 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.5%), Concurrency Surface (formerly Concurrency) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 79.927% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createRemoteJWKSet` **(Callbacks & Closures)** (Impact: 7.3)
    * *Intent:* * Only a single public key must match the selection process. As shown in the example below when * mu...
  * `encrypt` **(State Mutators)** (Impact: 7.0)
    * *Intent:* /** * Encrypts data using AES-256-GCM algorithm. * */
  * `constructor` **(Compute Cores)** (Impact: 6.2)
  * `constructor` **(State Mutators)** (Impact: 6.2)
  * `isEnabled` **(Compute Cores)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 608`, `structural_boundaries: 1147`, `args: 287`, `func_start: 274`, `class_start: 608`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 10`, `duplicate_logic: 31`, `unreferenced_by_name: 162`
* *Architecture:* `io: 24`, `concurrency: 195`, `import: 1`
* *Defense:* `doc: 134`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eventemitter3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/workos-DluXltJr.d.mts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.293)
- **Top Global Matches:** file_cluster_0: 7.293, file_cluster_5: 8.353, file_cluster_12: 8.951
- **Magnitude:** 831.12 | **LOC:** 5202 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.5%), Concurrency Surface (formerly Concurrency) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 79.927% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createRemoteJWKSet` **(Callbacks & Closures)** (Impact: 7.3)
    * *Intent:* * Only a single public key must match the selection process. As shown in the example below when * mu...
  * `encrypt` **(State Mutators)** (Impact: 7.0)
    * *Intent:* /** * Encrypts data using AES-256-GCM algorithm. * */
  * `constructor` **(Compute Cores)** (Impact: 6.2)
  * `constructor` **(State Mutators)** (Impact: 6.2)
  * `isEnabled` **(Compute Cores)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 608`, `structural_boundaries: 1147`, `args: 287`, `func_start: 274`, `class_start: 608`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 10`, `duplicate_logic: 31`, `unreferenced_by_name: 162`
* *Architecture:* `io: 24`, `concurrency: 195`, `import: 1`
* *Defense:* `doc: 134`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eventemitter3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/index.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.519)
- **Top Global Matches:** file_cluster_11: 5.519, file_cluster_15: 5.861, file_cluster_16: 7.893
- **Magnitude:** 82.68 | **LOC:** 67 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.6%), Guard Balance (formerly Safety Score) (66.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createHttpClient` **(Defensive Guards)** (Impact: 14.6)
  * `emitWarning` **(Parameter Forwarders)** (Impact: 1.6)
  * `createWebhookClient` **(Interface Declarations)** (Impact: 1.1)
  * `getCryptoProvider` **(Interface Declarations)** (Impact: 1.1)
  * `createActionsClient` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 10`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 30`, `unreferenced_by_name: 4`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` factory-BraleEZU.cjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/index.worker.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.576)
- **Top Global Matches:** file_cluster_11: 5.576, file_cluster_15: 5.947, file_cluster_16: 7.979
- **Magnitude:** 73.54 | **LOC:** 60 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (62.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createHttpClient` **(Defensive Guards)** (Impact: 12.6)
  * `emitWarning` **(Parameter Forwarders)** (Impact: 1.6)
  * `createWebhookClient` **(Interface Declarations)** (Impact: 1.1)
  * `getCryptoProvider` **(Interface Declarations)** (Impact: 1.1)
  * `createActionsClient` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 5`
* *Architecture:* `api: 26`, `import: 1`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` factory-BraleEZU.cjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/index.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.822)
- **Top Global Matches:** file_cluster_11: 5.822, file_cluster_15: 6.157, file_cluster_16: 8.169
- **Magnitude:** 27.12 | **LOC:** 39 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createHttpClient` **(Defensive Guards)** (Impact: 14.6)
  * `emitWarning` **(Parameter Forwarders)** (Impact: 1.6)
  * `createWebhookClient` **(Interface Declarations)** (Impact: 1.1)
  * `getCryptoProvider` **(Interface Declarations)** (Impact: 1.1)
  * `createActionsClient` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 12`, `args: 7`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` factory-IqQiyE5J.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/index.worker.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.93)
- **Top Global Matches:** file_cluster_11: 5.93, file_cluster_15: 6.307, file_cluster_16: 8.309
- **Magnitude:** 22.02 | **LOC:** 34 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 50.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createHttpClient` **(Defensive Guards)** (Impact: 12.6)
  * `emitWarning` **(Parameter Forwarders)** (Impact: 1.6)
  * `createWebhookClient` **(Interface Declarations)** (Impact: 1.1)
  * `getCryptoProvider` **(Interface Declarations)** (Impact: 1.1)
  * `createActionsClient` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 5`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` factory-IqQiyE5J.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.36 | **LOC:** 118 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/package.json` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 2.0 | **LOC:** 100 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.025
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

- `package/lib/factory-IqQiyE5J.mjs` -> **Severity: 1.758** (Bridge: 0.0182 * Flux: 96.6852%)
- `package/lib/factory-BraleEZU.cjs` -> **Severity: 1.744** (Bridge: 0.0182 * Flux: 95.9014%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/factory-IqQiyE5J.mjs` -> **Severity: 9.907** (Embedded: 0.1818 * Error Risk: 54.4912%)
- `package/lib/factory-BraleEZU.cjs` -> **Severity: 9.877** (Embedded: 0.1818 * Error Risk: 54.3213%)
- `package/lib/webapi-N7c2LUJd.cjs` -> **Severity: 8.398** (Embedded: 0.1636 * Error Risk: 51.3225%)
- `package/lib/webapi-CxKOxXjo.mjs` -> **Severity: 8.292** (Embedded: 0.1636 * Error Risk: 50.6713%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/webapi-CxKOxXjo.mjs` -> **Severity: 16483.3** (Blast Radius: 164.833 * Doc Risk: 100.0%)
- `package/lib/webapi-N7c2LUJd.cjs` -> **Severity: 16483.3** (Blast Radius: 164.833 * Doc Risk: 100.0%)
- `package/lib/factory-BraleEZU.cjs` -> **Severity: 12675.943** (Blast Radius: 135.068 * Doc Risk: 93.8486%)
- `package/lib/factory-IqQiyE5J.mjs` -> **Severity: 12631.775** (Blast Radius: 135.068 * Doc Risk: 93.5216%)
- `package/lib/workos-COj1yMhR.d.cts` -> **Severity: 3998.348** (Blast Radius: 50.025 * Doc Risk: 79.927%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 696 literal sites + 26 sites through wrappers = 722

- `decodeBase64url` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `package/lib/webapi-CxKOxXjo.mjs`
- `decodeBase64url` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `package/lib/webapi-N7c2LUJd.cjs`
- `unreachable` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `package/lib/factory-BraleEZU.cjs`
- `unreachable` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `package/lib/factory-IqQiyE5J.mjs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3250 call pairs -- scoped 36.4%, unique 0.0%, ambiguous 2.3%, external 61.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 3250 | 36.4% | 0.0% | 2.3% | 61.2% |

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
