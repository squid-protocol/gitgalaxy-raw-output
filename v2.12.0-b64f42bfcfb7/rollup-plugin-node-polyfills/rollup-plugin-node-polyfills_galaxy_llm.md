# ARCHITECTURAL_BRIEF: rollup-plugin-node-polyfills
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
- **Scope:** 54 analyzed artifact(s), 36490 LOC.
- **Load-bearing artifact:** `package/polyfills/readable-stream/duplex.js` -- 4 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/polyfills/stream.js` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/polyfills/browserify-fs.js` at magnitude 16790.42 (structural weight, not risk).
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
| Total Artifacts | 55 |
| Analyzed Artifacts (Scanned) | 54 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 36490 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.658 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1516 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6324 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 47 | 36490 | 87.0% |
| PLAINTEXT | 5 | 0 | 9.3% |
| MARKDOWN | 2 | 0 | 3.7% |

## 4.1 SOURCE ENCODINGS
All 54 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 35%, Data / Markup / Trivial 17%, Large Core Modules (3) 13%, Callbacks & Closures Files 9%, Many-Argument Workhorses Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 47 | 87.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 13.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 4.8 | 100.0 | 68.1 | 86.0 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.1 | 58.6 | 65.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 38.8 | 2.9 | 80.0 |
| Connectivity (formerly API Exposure) | 1.8 | 75.2 | 26.1 | 21.5 | 21.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 85.6 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 83.7 | 7.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 86.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 50 | 8 | 1 | `package/polyfills/browserify-fs.js` |
| cleanup | 26 | 6 | 1 | `package/polyfills/browserify-fs.js` |
| guards | 2919 | 39 | 67 | `package/polyfills/browserify-fs.js` |
| danger | 579 | 24 | 10 | `package/polyfills/browserify-fs.js` |
| concurrency | 89 | 9 | 5 | `package/polyfills/timers.js` |
| connectivity | 763 | 47 | 17 | `package/polyfills/constants.js` |
| io | 74 | 6 | 1 | `package/polyfills/browserify-fs.js` |
| crypto | 1 | 1 | 0 | `package/polyfills/crypto-browserify.js` |
| ipc | 6 | 1 | 0 | `package/polyfills/setimmediate.js` |
| time | 66 | 7 | 1 | `package/polyfills/timers.js` |
| serialization | 10 | 3 | 0 | `package/polyfills/crypto-browserify.js` |
| regex | 75 | 13 | 3 | `package/polyfills/url.js` |
| events | 765 | 15 | 19 | `package/polyfills/browserify-fs.js` |
| tests | 21 | 2 | 0 | `package/polyfills/assert.js` |
| docs | 204 | 8 | 2 | `package/polyfills/browserify-fs.js` |
| debt | 250 | 15 | 2 | `package/polyfills/browserify-fs.js` |
| mutation | 16985 | 42 | 340 | `package/polyfills/crypto-browserify.js` |
| dead_code | 318 | 15 | 17 | `package/polyfills/browserify-fs.js` |
| credential | 2 | 2 | 0 | `package/polyfills/buffer-es6.js` |
| threat | 1 | 1 | 0 | `package/polyfills/punycode.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 23 | 4 | 0 | `package/polyfills/crypto-browserify.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.5956**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/polyfills/browserify-fs.js` (Hits: 63)
- `package/polyfills/http-lib/request.js` (Hits: 5)
- `package/polyfills/http-lib/capability.js` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **duplex.js** (`package/polyfills/readable-stream/duplex.js`) — 4 inbound connections
2. **utils.js** (`package/polyfills/zlib-lib/utils.js`) — 4 inbound connections
3. **capability.js** (`package/polyfills/http-lib/capability.js`) — 2 inbound connections
4. **inherits.js** (`package/polyfills/inherits.js`) — 2 inbound connections
5. **readable.js** (`package/polyfills/readable-stream/readable.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stream.js** (`package/polyfills/stream.js`) — 7 outbound dependencies
2. **readable.js** (`package/polyfills/readable-stream/readable.js`) — 6 outbound dependencies
3. **browserify-fs.js** (`package/polyfills/browserify-fs.js`) — 5 outbound dependencies
4. **crypto-browserify.js** (`package/polyfills/crypto-browserify.js`) — 5 outbound dependencies
5. **request.js** (`package/polyfills/http-lib/request.js`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inflate` **(Many-Argument Workhorses)** (@ `package/polyfills/zlib-lib/inflate.js`) -> Impact: **471.4** | LOC: 1184
- `levelFilesystem` **(Defensive Guards)** (@ `package/polyfills/browserify-fs.js`) -> Impact: **340.7** | LOC: 579
- `deflate` **(Many-Argument Workhorses)** (@ `package/polyfills/zlib-lib/deflate.js`) -> Impact: **217.6** | LOC: 333
- `resolveObject` **(Compute Cores)** (@ `package/polyfills/url.js`) -> Impact: **174.6** | LOC: 268
- `parse` **(Many-Argument Workhorses)** (@ `package/polyfills/url.js`) -> Impact: **171.8** | LOC: 260
- `inflate_table` **(Many-Argument Workhorses)** (@ `package/polyfills/zlib-lib/inftrees.js`) -> Impact: **158.8** | LOC: 297
- `levelBlobs` **(Many-Argument Workhorses)** (@ `package/polyfills/browserify-fs.js`) -> Impact: **134.1** | LOC: 361
- `makeConstructor` **(Many-Argument Workhorses)** (@ `package/polyfills/browserify-fs.js`) -> Impact: **114.4** | LOC: 208
  * *Intent:* // // 5 The Typed Array View Types //
- `inflate_fast` **(Many-Argument Workhorses)** (@ `package/polyfills/zlib-lib/inffast.js`) -> Impact: **107.8** | LOC: 285
  * *Intent:* */
- `decode` **(Defensive Guards)** (@ `package/polyfills/crypto-browserify.js`) -> Impact: **94.6** | LOC: 125
  * *Intent:* // // Decoding //

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/polyfills` | 30 | 37825.34 | 59.72% | 14.82% |
| `package/polyfills/zlib-lib` | 11 | 6082.3 | 61.53% | 1.76% |
| `package/polyfills/readable-stream` | 6 | 1825.28 | 80.2% | 6.22% |
| `package/polyfills/http-lib` | 4 | 511.22 | 62.51% | 21.73% |
| `package` | 3 | 3.98 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/polyfills/browserify-fs.js` -> **100.0%** Exposure
- `package/polyfills/domain.js` -> **100.0%** Exposure
- `package/polyfills/timers.js` -> **72.3987%** Exposure
- `package/polyfills/http-lib/capability.js` -> **71.5828%** Exposure
- `package/polyfills/os.js` -> **61.2774%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/polyfills/browserify-fs.js` -> **100.0%** Exposure
- `package/polyfills/buffer-es6.js` -> **100.0%** Exposure
- `package/polyfills/crypto-browserify.js` -> **100.0%** Exposure
- `package/polyfills/events.js` -> **100.0%** Exposure
- `package/polyfills/http-lib/request.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/polyfills/browserify-fs.js` -> **66** Orphaned Functions | **129** Duplicates
- `package/polyfills/crypto-browserify.js` -> **23** Orphaned Functions | **25** Duplicates
- `package/polyfills/domain.js` -> **7** Orphaned Functions | **0** Duplicates
- `package/polyfills/zlib.js` -> **4** Orphaned Functions | **0** Duplicates
- `package/polyfills/buffer-es6.js` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `41` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/polyfills/browserify-fs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.79)
- **Top Global Matches:** file_cluster_4: 13.79, file_cluster_12: 14.891, file_cluster_15: 16.03
- **Magnitude:** 16790.42 | **LOC:** 19039 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 11.327; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `levelFilesystem` **(Defensive Guards)** (Impact: 340.7)
  * `levelBlobs` **(Many-Argument Workhorses)** (Impact: 134.1)
  * `makeConstructor` **(Many-Argument Workhorses)** (Impact: 114.4)
    * *Intent:* // // 5 The Typed Array View Types //
  * `open` **(Defensive Guards)** (Impact: 69.9)
  * `readableAddChunk` **(Many-Argument Workhorses)** (Impact: 63.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 2495 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 7922
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3497`, `structural_boundaries: 2644`, `args: 1226`, `func_start: 1089`
* *Risk/State:* `safety_bypasses: 176`, `state_mutation: 2932`, `dead_code: 6`, `planned_debt: 22`, `fragile_debt: 28`, `duplicate_logic: 129`, `unreferenced_by_name: 66`
* *Architecture:* `io: 63`, `api: 155`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 1106`, `doc: 110`, `immutability_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, events, path, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/crypto-browserify.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.813)
- **Top Global Matches:** file_cluster_15: 8.813, file_cluster_12: 9.876, file_cluster_4: 10.055
- **Magnitude:** 13303.12 | **LOC:** 16433 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 11.327; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 99.4867% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Defensive Guards)** (Impact: 94.6)
    * *Intent:* // // Decoding //
  * `encode` **(Defensive Guards)** (Impact: 74.8)
  * `_wnafMulAdd` **(Many-Argument Workhorses)** (Impact: 74.7)
  * `decodeGeneric` **(Defensive Guards)** (Impact: 55.5)
  * `divmod` **(Many-Argument Workhorses)** (Impact: 44.7)
    * *Intent:* // NOTE: 1) `mode` can be set to `mod` to request mod only, // to `div` to request div only, or be a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 2142 instances
* *Concurrency (weighted view):* 41
* *State Mutation (weighted view):* 7912
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1913`, `structural_boundaries: 3535`, `args: 944`, `func_start: 1372`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 3628`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 4`, `duplicate_logic: 25`, `unreferenced_by_name: 23`
* *Architecture:* `io: 1`, `api: 101`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 836`, `doc: 9`, `test: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, crypto, stream, string_decoder, vm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/buffer-es6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.777)
- **Top Global Matches:** file_cluster_4: 5.777, file_cluster_6: 10.035, file_cluster_15: 11.335
- **Magnitude:** 2707.08 | **LOC:** 1982 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 94.964% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Many-Argument Workhorses)** (Impact: 77.3)
  * `bidirectionalIndexOf` **(Many-Argument Workhorses)** (Impact: 66.5)
    * *Intent:* // Finds either the first index of `val` in `buffer` at offset >= `byteOffset`, // OR the last index...
  * `arrayIndexOf` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `copy` **(Many-Argument Workhorses)** (Impact: 60.5)
    * *Intent:* // copy(targetBuffer, targetStart=0, sourceStart=0, sourceEnd=buffer.length)
  * `write` **(Many-Argument Workhorses)** (Impact: 58.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 424 instances
* *State Mutation (weighted view):* 1288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 538`, `structural_boundaries: 349`, `args: 119`, `func_start: 172`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 440`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 150`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/zlib-lib/inflate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.064)
- **Top Global Matches:** file_cluster_4: 6.064, file_cluster_15: 10.576, file_cluster_9: 11.095
- **Magnitude:** 2133.8 | **LOC:** 1651 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 15.781; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.9%), Guard Balance (formerly Safety Score) (90.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 471.4)
  * `updatewindow` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* */
  * `inflateReset2` **(Defensive Guards)** (Impact: 20.8)
  * `inflateSetDictionary` **(Defensive Guards)** (Impact: 15.7)
  * `fixedtables` **(Compute Cores)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 477 instances
* *State Mutation (weighted view):* 1520
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 210`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 566`, `dead_code: 49`, `planned_debt: 2`
* *Architecture:* `api: 10`, `import: 6`
* *Defense:* `safety: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.781
  * `Choke Point (Betweenness):` 0.00254 | `Ripple Effect (Closeness):` 0.025157
  * `Imports (Out-Degree: 5):` adler32, crc32, inffast, inftrees, utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/zlib-lib/deflate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.337)
- **Top Global Matches:** file_cluster_8: 7.337, file_cluster_6: 11.64, file_cluster_4: 19.912
- **Magnitude:** 1597.16 | **LOC:** 1863 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 15.781; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.3%), Dead Code Surface (formerly Dead Code) (60.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deflate` **(Many-Argument Workhorses)** (Impact: 217.6)
  * `deflate_slow` **(Many-Argument Workhorses)** (Impact: 63.3)
    * *Intent:* /* =========================================================================== * Same as above, but ...
  * `deflate_rle` **(Defensive Guards)** (Impact: 56.6)
    * *Intent:* /* =========================================================================== * For Z_RLE, simply l...
  * `longest_match` **(Defensive Guards)** (Impact: 46.7)
    * *Intent:* /* =========================================================================== * Set match_start to ...
  * `deflateInit2` **(Many-Argument Workhorses)** (Impact: 46.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 263 instances
* *State Mutation (weighted view):* 899
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 186`, `args: 26`, `func_start: 26`
* *Risk/State:* `state_mutation: 373`, `dead_code: 71`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 143`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 15.781
  * `Choke Point (Betweenness):` 0.001814 | `Ripple Effect (Closeness):` 0.025157
  * `Imports (Out-Degree: 5):` adler32, crc32, messages, trees, utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.934)
- **Top Global Matches:** file_cluster_6: 8.934, file_cluster_8: 10.235, file_cluster_4: 16.272
- **Magnitude:** 1035.04 | **LOC:** 746 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 11.327; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.1%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveObject` **(Compute Cores)** (Impact: 174.6)
  * `parse` **(Many-Argument Workhorses)** (Impact: 171.8)
  * `format` **(Defensive Guards)** (Impact: 49.4)
  * `urlParse` **(Defensive Guards)** (Impact: 8.3)
  * `parseHost` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 81`, `args: 14`, `func_start: 13`
* *Risk/State:* `state_mutation: 211`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode, querystring, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/readable-stream/readable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.903)
- **Top Global Matches:** file_cluster_4: 6.903, file_cluster_15: 11.307, file_cluster_6: 11.484
- **Magnitude:** 995.86 | **LOC:** 897 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 60.545; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readableAddChunk` **(Many-Argument Workhorses)** (Impact: 75.8)
  * `read` **(Defensive Guards)** (Impact: 46.0)
    * *Intent:* // you can override either this method, or the async _read(n) below.
  * `pipe` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `wrap` **(Defensive Guards)** (Impact: 28.4)
    * *Intent:* // wrap an old-style stream as the async data source. // This is *not* part of the readable stream i...
  * `howMuchToRead` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* // This function is designed to be inlinable, so please take care when making // changes to the func...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 149 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 117`, `args: 54`, `func_start: 49`
* *Risk/State:* `state_mutation: 163`, `fragile_debt: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.545
  * `Choke Point (Betweenness):` 0.001814 | `Ripple Effect (Closeness):` 0.052411
  * `Imports (Out-Degree: 2):` buffer-list, duplex, events, process, string_decoder, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/polyfills/zlib-lib/trees.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.018)
- **Top Global Matches:** file_cluster_4: 6.018, file_cluster_15: 9.34, file_cluster_16: 10.561
- **Magnitude:** 960.98 | **LOC:** 1221 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 14.01; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send_tree` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* /* =========================================================================== * Send a literal or d...
  * `scan_tree` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* /* =========================================================================== * Scan a literal or d...
  * `_tr_flush_block` **(Many-Argument Workhorses)** (Impact: 35.5)
    * *Intent:* /* =========================================================================== * Determine the best ...
  * `gen_bitlen` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* /* =========================================================================== * Compute the optimal...
  * `build_tree` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* /* =========================================================================== * Construct one Huffm...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 123`, `args: 29`, `func_start: 29`
* *Risk/State:* `state_mutation: 214`, `dead_code: 44`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 38`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 1):` utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/readable-stream/writable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.352)
- **Top Global Matches:** file_cluster_15: 7.352, file_cluster_10: 8.125, file_cluster_16: 8.796
- **Magnitude:** 565.22 | **LOC:** 484 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 60.545; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.1%), Guard Balance (formerly Safety Score) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearBuffer` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* // if there's something in the buffer waiting, then process it
  * `writeOrBuffer` **(Many-Argument Workhorses)** (Impact: 23.4)
    * *Intent:* // if we're already writing something, then just put this // in the queue, and wait our turn. Otherw...
  * `end` **(Defensive Guards)** (Impact: 19.1)
  * `write` **(Defensive Guards)** (Impact: 19.0)
  * `validChunk` **(Defensive Guards)** (Impact: 18.8)
    * *Intent:* // If we get something that is not a buffer, string, null, or undefined, // and we're not in objectM...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 51`, `args: 31`, `func_start: 32`
* *Risk/State:* `state_mutation: 116`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.545
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052411
  * `Imports (Out-Degree: 1):` duplex, buffer, events, process, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/polyfills/zlib.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.718)
- **Top Global Matches:** file_cluster_12: 7.718, file_cluster_4: 8.858, file_cluster_15: 10.128
- **Magnitude:** 561.98 | **LOC:** 636 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 11.327; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.7%), Concurrency Surface (formerly Concurrency) (94.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Zlib` **(Defensive Guards)** (Impact: 65.5)
    * *Intent:* // the Zlib class they all inherit from // This thing manages the queue of requests, and returns // ...
  * `_processChunk` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `params` **(Defensive Guards)** (Impact: 27.4)
  * `flush` **(Defensive Guards)** (Impact: 22.0)
  * `_transform` **(Defensive Guards)** (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 104`, `args: 50`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 78`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 31`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 45`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` binding, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/events.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.628)
- **Top Global Matches:** file_cluster_6: 7.628, file_cluster_4: 8.453, file_cluster_15: 15.336
- **Magnitude:** 560.96 | **LOC:** 476 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `removeListener` **(Defensive Guards)** (Impact: 44.3)
  * `_addListener` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `emit` **(Defensive Guards)** (Impact: 31.7)
  * `removeAllListeners` **(Defensive Guards)** (Impact: 25.0)
  * `listeners` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 82`, `args: 28`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`
* *Architecture:* `api: 2`
* *Defense:* `safety: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.636)
- **Top Global Matches:** file_cluster_4: 6.636, file_cluster_15: 8.978, file_cluster_12: 9.099
- **Magnitude:** 507.34 | **LOC:** 599 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.327; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.2%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatValue` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `formatProperty` **(Many-Argument Workhorses)** (Impact: 58.4)
  * `format` **(Defensive Guards)** (Impact: 21.6)
  * `inspect` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* /** * Echos the value of a value. Trys to print the value out * in the best way possible given the d...
  * `deprecate` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* // Mark that a method should not be used. // Returns a modified function which warns once by default...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 127`, `args: 45`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 59`
* *Architecture:* `api: 23`, `import: 2`
* *Defense:* `safety: 40`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inherits, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/zlib-lib/inffast.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.213)
- **Top Global Matches:** file_cluster_1: 4.213, file_cluster_3: 48.11, file_cluster_8: 69.985
- **Magnitude:** 494.42 | **LOC:** 326 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 14.01; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate_fast` **(Many-Argument Workhorses)** (Impact: 107.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 37`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 137`, `dead_code: 11`
* *Architecture:* `api: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/assert.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.636)
- **Top Global Matches:** file_cluster_4: 8.636, file_cluster_6: 11.23, file_cluster_12: 12.001
- **Magnitude:** 447.4 | **LOC:** 489 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 11.327; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_deepEqual` **(Defensive Guards)** (Impact: 77.0)
  * `_throws` **(Defensive Guards)** (Impact: 48.8)
  * `objEquiv` **(Defensive Guards)** (Impact: 44.5)
  * `AssertionError` **(Compute Cores)** (Impact: 13.1)
  * `isView` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 99`, `args: 34`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 43`, `dead_code: 7`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 59`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/zlib-lib/inftrees.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.749)
- **Top Global Matches:** file_cluster_1: 4.749, file_cluster_3: 48.162, file_cluster_8: 70.021
- **Magnitude:** 383.68 | **LOC:** 330 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 14.01; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Dead Code Surface (formerly Dead Code) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate_table` **(Many-Argument Workhorses)** (Impact: 158.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 46`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 74`, `dead_code: 17`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 1):` utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/zlib-lib/binding.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.941)
- **Top Global Matches:** file_cluster_6: 6.941, file_cluster_4: 12.209, file_cluster_8: 14.086
- **Magnitude:** 315.9 | **LOC:** 270 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 20.956; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_write` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `init` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `reset` **(Defensive Guards)** (Impact: 7.8)
  * `close` **(Defensive Guards)** (Impact: 6.8)
  * `write` **(Many-Argument Workhorses)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 41`, `args: 12`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `dead_code: 1`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.956
  * `Choke Point (Betweenness):` 0.003628 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 4):` deflate, inflate, messages, zstream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/punycode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.158)
- **Top Global Matches:** file_cluster_4: 7.158, file_cluster_12: 10.312, file_cluster_15: 11.448
- **Magnitude:** 309.28 | **LOC:** 476 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* /** * Converts a string of Unicode symbols (e.g. a domain name label) to a * Punycode string of ASCI...
  * `decode` **(Compute Cores)** (Impact: 25.9)
    * *Intent:* /** * Converts a Punycode string of ASCII-only symbols to a string of Unicode * symbols. */
  * `ucs2decode` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* /** * Creates an array containing the numeric code points of each Unicode * character in the string....
  * `adapt` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** * Bias adaptation function as per section 3.4 of RFC 3492. * https://tools.ietf.org/html/rfc3492...
  * `basicToDigit` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* /** * Converts a basic code point into a digit/integer. * representing integers) in the range `0` to...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 55`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`
* *Architecture:* `api: 7`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/constants.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.843)
- **Top Global Matches:** file_cluster_2: 3.843, file_cluster_17: 5.108, file_cluster_13: 5.698
- **Magnitude:** 268.76 | **LOC:** 489 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (17.8%), Complexity Load (formerly Cognitive Load) (4.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 487`
* *Risk/State:* None
* *Architecture:* `api: 244`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/http-lib/request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.445)
- **Top Global Matches:** file_cluster_10: 8.445, file_cluster_4: 8.889, file_cluster_15: 9.881
- **Magnitude:** 239.26 | **LOC:** 279 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 20.956; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_onFinish` **(Defensive Guards)** (Impact: 25.9)
  * `decideMode` **(Compute Cores)** (Impact: 25.0)
  * `ClientRequest` **(Defensive Guards)** (Impact: 18.9)
  * `_onXHRProgress` **(Callbacks & Closures)** (Impact: 4.5)
  * `end` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 46`, `args: 28`, `func_start: 19`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 5`, `api: 13`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 22`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.956
  * `Choke Point (Betweenness):` 0.001089 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 3):` capability, response, to-arraybuffer, stream, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/http-lib/response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.827)
- **Top Global Matches:** file_cluster_8: 7.827, file_cluster_6: 17.673, file_cluster_3: 20.497
- **Magnitude:** 221.58 | **LOC:** 186 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 17.265; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.0%), Guard Balance (formerly Safety Score) (76.0%), Concurrency Surface (formerly Concurrency) (64.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IncomingMessage` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `_onXHRProgress` **(Defensive Guards)** (Impact: 24.9)
  * `read` **(Callbacks & Closures)** (Impact: 3.6)
  * `onprogress` **(Callbacks & Closures)** (Impact: 2.3)
  * `_read` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 34`, `args: 10`, `func_start: 6`
* *Risk/State:* `state_mutation: 49`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.265
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025157
  * `Imports (Out-Degree: 1):` capability, stream, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/path.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.632)
- **Top Global Matches:** file_cluster_15: 7.632, file_cluster_9: 7.87, file_cluster_10: 8.362
- **Magnitude:** 198.16 | **LOC:** 235 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `relative` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* // path.relative(from, to) // posix version
  * `normalizeArray` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
  * `resolve` **(Defensive Guards)** (Impact: 10.4)
    * *Intent:* // path.resolve([from ...], to) // posix version
  * `normalize` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* // path.normalize(path) // posix version
  * `trim` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 61`, `args: 17`, `func_start: 12`
* *Risk/State:* `state_mutation: 32`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 1`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/string-decoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.358)
- **Top Global Matches:** file_cluster_12: 7.358, file_cluster_7: 8.89, file_cluster_15: 10.235
- **Magnitude:** 168.66 | **LOC:** 221 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 11.327; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Compute Cores)** (Impact: 17.5)
    * *Intent:* // write decodes the given buffer and returns it as JS string that is // guaranteed to not contain a...
  * `detectIncompleteChar` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* // detectIncompleteChar determines if there is an incomplete UTF-8 character at // the end of the gi...
  * `StringDecoder` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* // StringDecoder provides an interface for efficiently splitting a series of // buffers into a serie...
  * `end` **(Callbacks & Closures)** (Impact: 6.4)
  * `assertEncoding` **(State Mutators)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 33`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/process-es6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.93)
- **Top Global Matches:** file_cluster_11: 7.93, file_cluster_15: 8.084, file_cluster_10: 8.347
- **Magnitude:** 165.86 | **LOC:** 225 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 54`, `args: 17`, `func_start: 16`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 2`, `concurrency: 8`
* *Defense:* `safety: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/polyfills/setimmediate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.432)
- **Top Global Matches:** file_cluster_10: 6.432, file_cluster_15: 7.768, file_cluster_2: 9.102
- **Magnitude:** 150.06 | **LOC:** 186 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 20.956; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (55.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 10.9)
  * `installPostMessageImplementation` **(Defensive Guards)** (Impact: 7.2)
  * `runIfPresent` **(Defensive Guards)** (Impact: 6.7)
  * `onGlobalMessage` **(Defensive Guards)** (Impact: 6.0)
  * `setImmediate` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 31`, `args: 20`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 20`
* *Architecture:* `api: 3`, `concurrency: 11`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.956
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/polyfills/qs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.303)
- **Top Global Matches:** file_cluster_6: 7.303, file_cluster_8: 12.196, file_cluster_4: 13.94
- **Magnitude:** 149.04 | **LOC:** 148 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `stringify` **(Defensive Guards)** (Impact: 19.1)
  * `stringifyPrimitive` **(Defensive Guards)** (Impact: 12.1)
  * `map` **(Compute Cores)** (Impact: 5.6)
  * `hasOwnProperty` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 34`, `args: 9`, `func_start: 5`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 4`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `package/polyfills/stream.js` (JAVASCRIPT) | Magnitude: 76.6 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 14, branch: 13, events: 10
- `package/polyfills/process-es6.js` (JAVASCRIPT) | Magnitude: 165.86 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 54, core_var_decl: 49, branch: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/polyfills/zlib-lib/crc32.js` (JAVASCRIPT) | Magnitude: 38.24 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, core_var_decl: 10, structural_boundaries: 9, state_mutation: 9
- `package/polyfills/zlib-lib/adler32.js` (JAVASCRIPT) | Magnitude: 43.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 10, core_var_decl: 6, design_snake_case: 6
- `package/polyfills/vm.js` (JAVASCRIPT) | Magnitude: 134.14 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 52, args: 25, branch: 24

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/polyfills/zlib-lib/binding.js` -> **Severity: 0.363** (Bridge: 0.0036 * Flux: 100.0%)
- `package/polyfills/readable-stream/duplex.js` -> **Severity: 0.327** (Bridge: 0.0033 * Flux: 99.9994%)
- `package/polyfills/zlib-lib/inflate.js` -> **Severity: 0.254** (Bridge: 0.0025 * Flux: 100.0%)
- `package/polyfills/readable-stream/readable.js` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 100.0%)
- `package/polyfills/zlib-lib/deflate.js` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/polyfills/zlib-lib/utils.js` -> **Severity: 5.109** (Embedded: 0.0755 * Error Risk: 67.6936%)
- `package/polyfills/readable-stream/duplex.js` -> **Severity: 4.489** (Embedded: 0.0786 * Error Risk: 57.0947%)
- `package/polyfills/readable-stream/writable.js` -> **Severity: 4.208** (Embedded: 0.0524 * Error Risk: 80.2938%)
- `package/polyfills/readable-stream/readable.js` -> **Severity: 3.891** (Embedded: 0.0524 * Error Risk: 74.2356%)
- `package/polyfills/readable-stream/buffer-list.js` -> **Severity: 3.512** (Embedded: 0.0453 * Error Risk: 77.5466%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/polyfills/readable-stream/duplex.js` -> **Severity: 11127.3** (Blast Radius: 111.273 * Doc Risk: 100.0%)
- `package/polyfills/readable-stream/readable.js` -> **Severity: 6054.5** (Blast Radius: 60.545 * Doc Risk: 100.0%)
- `package/polyfills/readable-stream/writable.js` -> **Severity: 6054.5** (Blast Radius: 60.545 * Doc Risk: 100.0%)
- `package/polyfills/zlib-lib/utils.js` -> **Severity: 4051.1** (Blast Radius: 40.511 * Doc Risk: 100.0%)
- `package/polyfills/readable-stream/buffer-list.js` -> **Severity: 3705.4** (Blast Radius: 37.054 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 12 literal sites + 1 sites through wrappers = 13
- **`panics_and_aborts`:** 321 literal sites + 7 sites through wrappers = 328

- `error` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `package/polyfills/punycode.js`
- `log` (function, debug_prints, primitive): 1 call sites in 1 files -- `package/polyfills/util.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5912 call pairs -- scoped 18.3%, unique 0.0%, ambiguous 3.0%, external 78.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 5912 | 18.3% | 0.0% | 3.0% | 78.7% |

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
