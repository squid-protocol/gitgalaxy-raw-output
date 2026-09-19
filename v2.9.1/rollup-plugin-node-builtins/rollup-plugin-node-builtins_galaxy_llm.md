# ARCHITECTURAL_BRIEF: rollup-plugin-node-builtins
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
- **Scope:** 31 analyzed artifact(s), 4730 LOC.
- **Load-bearing artifact:** `package/src/es6/util.js` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/src/es6/stream.js` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/src/es6/url.js` at magnitude 1052.04 (structural weight, not risk).
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
| Total Artifacts | 33 |
| Analyzed Artifacts (Scanned) | 31 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 4730 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 93.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3574 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6716 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 28 | 4702 | 90.3% |
| JSON | 1 | 28 | 3.2% |
| PLAINTEXT | 1 | 0 | 3.2% |
| MARKDOWN | 1 | 0 | 3.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.655`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.66; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 45%, Data / Markup / Trivial 16%, Large Core Modules (3) 13%, Callbacks & Closures Files 10%, State Mutators Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 29 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 67.7 | 89.0 | 5.1 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 68.0 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 37.2 | 2.7 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 72.6 | 21.7 | 12.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 80.4 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 5.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 82.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 9 | 4 | 1 | `package/src/es6/util.js` |
| cleanup | 12 | 3 | 0 | `package/src/es6/timers.js` |
| guards | 440 | 23 | 45 | `package/src/es6/readable-stream/readable.js` |
| danger | 81 | 16 | 8 | `package/src/es6/zlib.js` |
| concurrency | 44 | 4 | 1 | `package/src/es6/timers.js` |
| connectivity | 184 | 28 | 16 | `package/src/es6/zlib.js` |
| io | 6 | 2 | 0 | `package/src/index.js` |
| crypto | 1 | 1 | 0 | `package/src/index.js` |
| ipc | 8 | 2 | 0 | `package/src/es6/setimmediate.js` |
| time | 32 | 3 | 0 | `package/src/es6/timers.js` |
| serialization | 3 | 1 | 0 | `package/src/es6/util.js` |
| regex | 43 | 8 | 3 | `package/src/es6/url.js` |
| events | 145 | 10 | 12 | `package/src/es6/readable-stream/readable.js` |
| tests | 14 | 1 | 0 | `package/src/es6/assert.js` |
| docs | 23 | 2 | 0 | `package/src/es6/punycode.js` |
| debt | 19 | 8 | 2 | `package/src/es6/readable-stream/readable.js` |
| mutation | 1842 | 25 | 157 | `package/src/es6/url.js` |
| dead_code | 52 | 14 | 5 | `package/src/es6/readable-stream/readable.js` |
| credential | 0 | 0 | 0 | - |
| threat | 190 | 21 | 15 | `package/src/es6/events.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/index.js` (Hits: 4)
- `package/src/es6/path.js` (Hits: 2)
- `package/.eslintrc` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.js** (`package/src/es6/util.js`) — 9 inbound connections
2. **events.js** (`package/src/es6/events.js`) — 4 inbound connections
3. **duplex.js** (`package/src/es6/readable-stream/duplex.js`) — 4 inbound connections
4. **inherits.js** (`package/src/es6/inherits.js`) — 2 inbound connections
5. **readable.js** (`package/src/es6/readable-stream/readable.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **stream.js** (`package/src/es6/stream.js`) — 7 outbound dependencies
2. **readable.js** (`package/src/es6/readable-stream/readable.js`) — 6 outbound dependencies
3. **writable.js** (`package/src/es6/readable-stream/writable.js`) — 5 outbound dependencies
4. **duplex.js** (`package/src/es6/readable-stream/duplex.js`) — 4 outbound dependencies
5. **url.js** (`package/src/es6/url.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` **(Many-Argument Workhorses)** (@ `package/src/es6/url.js`) -> Impact: **178.5** | LOC: 260
- `resolveObject` **(Compute Cores)** (@ `package/src/es6/url.js`) -> Impact: **174.6** | LOC: 268
- `_deepEqual` **(Defensive Guards)** (@ `package/src/es6/assert.js`) -> Impact: **77.0** | LOC: 65
- `readableAddChunk` **(Many-Argument Workhorses)** (@ `package/src/es6/readable-stream/readable.js`) -> Impact: **75.8** | LOC: 47
- `formatValue` **(Many-Argument Workhorses)** (@ `package/src/es6/util.js`) -> Impact: **71.5** | LOC: 111
- `Zlib` **(Defensive Guards)** (@ `package/src/es6/zlib.js`) -> Impact: **65.5** | LOC: 98
  * *Intent:* // the Zlib class they all inherit from // This thing manages the queue of requests, and returns // true or false if there is anything in the queue wh...
- `formatProperty` **(Many-Argument Workhorses)** (@ `package/src/es6/util.js`) -> Impact: **58.4** | LOC: 57
- `format` **(Defensive Guards)** (@ `package/src/es6/url.js`) -> Impact: **53.7** | LOC: 55
- `_throws` **(Defensive Guards)** (@ `package/src/es6/assert.js`) -> Impact: **48.8** | LOC: 37
- `read` **(Defensive Guards)** (@ `package/src/es6/readable-stream/readable.js`) -> Impact: **47.4** | LOC: 99
  * *Intent:* // you can override either this method, or the async _read(n) below.

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/es6` | 20 | 4576.0 | 70.75% | 17.36% |
| `package/src/es6/readable-stream` | 6 | 1826.68 | 80.16% | 6.18% |
| `package/src` | 1 | 70.32 | 63.31% | 0.0% |
| `package` | 4 | 33.24 | 1.28% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/es6/domain.js` -> **99.9811%** Exposure
- `package/src/es6/timers.js` -> **84.1131%** Exposure
- `package/src/es6/os.js` -> **75.3696%** Exposure
- `package/src/es6/zlib.js` -> **37.2349%** Exposure
- `package/src/es6/string-decoder.js` -> **25.4029%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/es6/events.js` -> **100.0%** Exposure
- `package/src/es6/path.js` -> **100.0%** Exposure
- `package/src/es6/punycode.js` -> **100.0%** Exposure
- `package/src/es6/qs.js` -> **100.0%** Exposure
- `package/src/es6/readable-stream/buffer-list.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/es6/domain.js` -> **7** Orphaned Functions | **0** Duplicates
- `package/src/es6/zlib.js` -> **4** Orphaned Functions | **0** Duplicates
- `package/src/es6/os.js` -> **2** Orphaned Functions | **0** Duplicates
- `package/src/es6/timers.js` -> **2** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `29` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/src/es6/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1052.04 | **LOC:** 746 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 34.729; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (98.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `resolveObject` **(Compute Cores)** (Impact: 174.6)
  * `format` **(Defensive Guards)** (Impact: 53.7)
  * `urlParse` **(Defensive Guards)** (Impact: 8.3)
  * `parseHost` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 81`, `args: 14`, `func_start: 13`
* *Risk/State:* `state_mutation: 211`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.003448 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 2):` punycode, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/readable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 997.26 | **LOC:** 897 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 37.275; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.2%), Complexity Load (formerly Cognitive Load) (89.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readableAddChunk` **(Many-Argument Workhorses)** (Impact: 75.8)
  * `read` **(Defensive Guards)** (Impact: 47.4)
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
* *Structure:* `branch: 223`, `structural_boundaries: 117`, `args: 54`, `func_start: 49`
* *Risk/State:* `state_mutation: 163`, `dead_code: 12`, `fragile_debt: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.275
  * `Choke Point (Betweenness):` 0.008621 | `Ripple Effect (Closeness):` 0.109091
  * `Imports (Out-Degree: 4):` buffer-list, duplex, events, process, string_decoder, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/writable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 565.22 | **LOC:** 484 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 37.275; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (87.1%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `state_mutation: 116`, `dead_code: 5`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.275
  * `Choke Point (Betweenness):` 0.001724 | `Ripple Effect (Closeness):` 0.109091
  * `Imports (Out-Degree: 3):` duplex, buffer, events, process, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/zlib.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 561.98 | **LOC:** 636 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.7%), Concurrency Surface (formerly Concurrency) (94.3%), Guard Balance (formerly Safety Score) (84.7%)
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
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 78`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 31`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 45`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` binding, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/events.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 560.96 | **LOC:** 476 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 48.482; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`, `dead_code: 1`
* *Architecture:* `api: 2`
* *Defense:* `safety: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.482
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.142222
  * `Imports (Out-Degree: 0):` events
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/es6/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 507.34 | **LOC:** 599 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 117.149; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%)
- **Documentation Coverage:** 92.7711% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 117.149
  * `Choke Point (Betweenness):` 0.011494 | `Ripple Effect (Closeness):` 0.30303
  * `Imports (Out-Degree: 1):` inherits, process
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `package/src/es6/assert.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 447.4 | **LOC:** 489 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%)
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
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 43`, `dead_code: 1`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 59`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` buffer, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/punycode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 309.28 | **LOC:** 476 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 33.533; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
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
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 71`, `dead_code: 2`
* *Architecture:* `api: 7`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.533
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044444
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/path.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 198.16 | **LOC:** 235 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 34.729; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.4%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `state_mutation: 32`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 1`
* *Defense:* `safety: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/string-decoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 168.66 | **LOC:** 221 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 18.772; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (87.9%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/setimmediate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 150.06 | **LOC:** 186 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 34.729; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (69.8%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.729
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/qs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 149.04 | **LOC:** 148 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/vm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 134.14 | **LOC:** 203 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runInContext` **(Defensive Guards)** (Impact: 16.8)
  * `forEach` **(Compute Cores)** (Impact: 7.3)
  * `indexOf` **(Defensive Guards)** (Impact: 7.3)
  * `Object_keys` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* */
  * `createContext` **(Defensive Guards)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 52`, `args: 25`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 20`
* *Architecture:* `api: 8`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/readable-stream/transform.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 125.8 | **LOC:** 175 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 31.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `afterTransform` **(Defensive Guards)** (Impact: 13.1)
  * `Transform` **(Defensive Guards)** (Impact: 11.4)
  * `_write` **(Compute Cores)** (Impact: 10.5)
  * `_read` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* // Doesn't matter what the args are here. // _transform does all the work. // That we got here means...
  * `done` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 20`, `args: 11`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.38
  * `Choke Point (Betweenness):` 0.005747 | `Ripple Effect (Closeness):` 0.075
  * `Imports (Out-Degree: 2):` duplex, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/src/es6/readable-stream/buffer-list.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 89.22 | **LOC:** 60 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 26.694; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Complexity Load (formerly Cognitive Load) (96.4%), Connectivity (formerly Api Exposure) (57.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `concat` **(Defensive Guards)** (Impact: 6.3)
  * `join` **(Defensive Guards)** (Impact: 4.6)
  * `push` **(Callbacks & Closures)** (Impact: 4.5)
  * `shift` **(Defensive Guards)** (Impact: 4.3)
  * `unshift` **(Defensive Guards)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090741
  * `Imports (Out-Degree: 0):` buffer
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/stream.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 76.6 | **LOC:** 111 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 26.751; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (71.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipe` **(Defensive Guards)** (Impact: 26.6)
  * `ondata` **(Defensive Guards)** (Impact: 6.0)
  * `onclose` **(Defensive Guards)** (Impact: 3.3)
  * `ondrain` **(State Mutators)** (Impact: 3.2)
  * `onerror` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* // don't leave dangling pipes when there are errors.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 14`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 26.751
  * `Choke Point (Betweenness):` 0.008046 | `Ripple Effect (Closeness):` 0.033333
  * `Imports (Out-Degree: 7):` duplex.js, passthrough.js, readable.js, transform.js, writable.js, events, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/src/es6/timers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 70.32 | **LOC:** 77 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.7%), Mutation Surface (formerly State Flux) (92.0%), Debt Markers (formerly Tech Debt) (84.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearInterval` **(Defensive Guards)** (Impact: 6.0)
  * `clearTimeout` **(Defensive Guards)** (Impact: 6.0)
  * `active` **(Compute Cores)** (Impact: 4.8)
  * `clearFn` **(Defensive Guards)** (Impact: 4.5)
  * `onTimeout` **(State Mutators)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 2`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 10`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` setimmediate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 70.32 | **LOC:** 74 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Complexity Load (formerly Cognitive Load) (63.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 8`, `args: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/os.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 54.92 | **LOC:** 114 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Debt Markers (formerly Tech Debt) (75.4%), Guard Balance (formerly Safety Score) (53.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `endianness` **(Defensive Guards)** (Impact: 6.8)
  * `hostname` **(Defensive Guards)** (Impact: 3.2)
  * `release` **(Defensive Guards)** (Impact: 2.3)
  * `loadavg` **(Interface Declarations)** (Impact: 1.1)
  * `uptime` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 37`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/http.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 53.3 | **LOC:** 168 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Guard Balance (formerly Safety Score) (64.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (24.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Defensive Guards)** (Impact: 25.8)
  * `get` **(Parameter Forwarders)** (Impact: 2.0)
  * `Agent` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` request, url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/readable-stream/duplex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 37.76 | **LOC:** 46 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 53.84; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Guard Balance (formerly Safety Score) (79.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Duplex` **(Defensive Guards)** (Impact: 12.1)
  * `onend` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* // the no-half-open enforcer
  * `onEndNT` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 53.84
  * `Choke Point (Betweenness):` 0.012644 | `Ripple Effect (Closeness):` 0.15
  * `Imports (Out-Degree: 3):` readable, writable, process, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/src/es6/domain.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 35.4 | **LOC:** 101 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Mutation Surface (formerly State Flux) (96.5%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intercept` **(Defensive Guards)** (Impact: 5.0)
  * `bind` **(Callbacks & Closures)** (Impact: 2.0)
  * `run` **(Defensive Guards)** (Impact: 1.9)
  * `createEmitError` **(Parameter Forwarders)** (Impact: 1.7)
  * `emitError` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 19`, `args: 13`, `func_start: 11`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inherits, events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/es6/inherits.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 24.96 | **LOC:** 26 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 126.327; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Guard Balance (formerly Safety Score) (84.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inherits` **(State Mutators)** (Impact: 2.3)
  * `inherits` **(Callbacks & Closures)** (Impact: 2.1)
  * `TempCtor` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 3`, `func_start: 5`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 126.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.208696
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/.eslintrc` (JSON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.56 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/rollup.config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 14.64 | **LOC:** 9 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 18.772; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, rollup-plugin-babel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/src/es6/readable-stream/duplex.js` -> **Severity: 1.264** (Bridge: 0.0126 * Flux: 99.9994%)
- `package/src/es6/util.js` -> **Severity: 1.149** (Bridge: 0.0115 * Flux: 99.9997%)
- `package/src/es6/readable-stream/readable.js` -> **Severity: 0.862** (Bridge: 0.0086 * Flux: 100.0%)
- `package/src/es6/stream.js` -> **Severity: 0.805** (Bridge: 0.008 * Flux: 99.9982%)
- `package/src/es6/readable-stream/transform.js` -> **Severity: 0.575** (Bridge: 0.0057 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/src/es6/util.js` -> **Severity: 24.042** (Embedded: 0.303 * Error Risk: 79.3386%)
- `package/src/es6/inherits.js` -> **Severity: 17.685** (Embedded: 0.2087 * Error Risk: 84.7391%)
- `package/src/es6/events.js` -> **Severity: 13.603** (Embedded: 0.1422 * Error Risk: 95.6497%)
- `package/src/es6/readable-stream/duplex.js` -> **Severity: 11.964** (Embedded: 0.15 * Error Risk: 79.7611%)
- `package/src/es6/readable-stream/writable.js` -> **Severity: 10.766** (Embedded: 0.1091 * Error Risk: 98.6893%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/es6/inherits.js` -> **Severity: 12632.7** (Blast Radius: 126.327 * Doc Risk: 100.0%)
- `package/src/es6/util.js` -> **Severity: 10868.042** (Blast Radius: 117.149 * Doc Risk: 92.7711%)
- `package/src/es6/readable-stream/duplex.js` -> **Severity: 5384.0** (Blast Radius: 53.84 * Doc Risk: 100.0%)
- `package/src/es6/events.js` -> **Severity: 4848.2** (Blast Radius: 48.482 * Doc Risk: 100.0%)
- `package/src/es6/readable-stream/readable.js` -> **Severity: 3727.5** (Blast Radius: 37.275 * Doc Risk: 100.0%)

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
