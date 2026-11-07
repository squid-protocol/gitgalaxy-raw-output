# ARCHITECTURAL_BRIEF: @hapi_hoek
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
- **Scope:** 52 analyzed artifact(s), 1248 LOC.
- **Load-bearing artifact:** `package/lib/assert.js` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/index.js` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/deepEqual.js` at magnitude 275.54 (structural weight, not risk).
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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 0 |
| Total LOC | 1248 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 100.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1914 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4499 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3222 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 26 | 1111 | 50.0% |
| TYPESCRIPT | 23 | 137 | 44.2% |
| MARKDOWN | 2 | 0 | 3.8% |
| PLAINTEXT | 1 | 0 | 1.9% |

## 4.1 SOURCE ENCODINGS
All 52 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 60%, Large Core Modules (2) 25%, Callbacks & Closures Files 6%, Declarative / Non-Code 4%, Large Core Modules (3) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 49 | 94.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 0*


## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.8 | 19.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 65.2 | 48.1 | 50.0 | 50.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 7.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 3.5 | 100.0 | 18.3 | 17.3 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.4 | 16.8 | 16.8 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3 | 3 | 0 | `package/lib/once.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 223 | 18 | 21 | `package/lib/deepEqual.js` |
| danger | 17 | 4 | 0 | `package/lib/index.d.ts` |
| concurrency | 10 | 4 | 0 | `package/lib/wait.js` |
| connectivity | 142 | 49 | 2 | `package/lib/index.d.ts` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 3 | 2 | 0 | `package/lib/wait.js` |
| serialization | 1 | 1 | 0 | `package/lib/stringify.js` |
| regex | 9 | 7 | 1 | `package/lib/contain.js` |
| events | 14 | 4 | 0 | `package/lib/contain.js` |
| tests | 3 | 2 | 0 | `package/lib/index.d.ts` |
| docs | 52 | 1 | 0 | `package/lib/index.d.ts` |
| debt | 0 | 0 | 0 | - |
| mutation | 361 | 47 | 22 | `package/lib/contain.js` |
| dead_code | 15 | 1 | 0 | `package/lib/index.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/LICENSE.md` (Hits: 0)
- `package/README.md` (Hits: 0)
- `package/lib/applyToDefaults.d.ts` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **assert.js** (`package/lib/assert.js`) — 7 inbound connections
2. **reach.js** (`package/lib/reach.js`) — 5 inbound connections
3. **clone.js** (`package/lib/clone.js`) — 4 inbound connections
4. **assertError.js** (`package/lib/assertError.js`) — 3 inbound connections
5. **deepEqual.js** (`package/lib/deepEqual.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`package/lib/index.js`) — 22 outbound dependencies
2. **index.mjs** (`package/lib/index.mjs`) — 22 outbound dependencies
3. **applyToDefaults.js** (`package/lib/applyToDefaults.js`) — 4 outbound dependencies
4. **contain.js** (`package/lib/contain.js`) — 4 outbound dependencies
5. **clone.js** (`package/lib/clone.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isDeepEqualObj` **(Many-Argument Workhorses)** (@ `package/lib/deepEqual.js`) -> Impact: **143.2** | LOC: 170
- `clone` **(Many-Argument Workhorses)** (@ `package/lib/clone.js`) -> Impact: **77.6** | LOC: 112
- `array` **(Many-Argument Workhorses)** (@ `package/lib/contain.js`) -> Impact: **73.5** | LOC: 109
- `exports` **(Defensive Guards)** (@ `package/lib/reach.js`) -> Impact: **58.8** | LOC: 56
- `merge` **(Defensive Guards)** (@ `package/lib/merge.js`) -> Impact: **57.4** | LOC: 68
- `isDeepEqual` **(Defensive Guards)** (@ `package/lib/deepEqual.js`) -> Impact: **49.9** | LOC: 59
- `string` **(Many-Argument Workhorses)** (@ `package/lib/contain.js`) -> Impact: **46.0** | LOC: 80
- `base` **(Defensive Guards)** (@ `package/lib/clone.js`) -> Impact: **34.5** | LOC: 50
- `applyToDefaultsWithShallow` **(Defensive Guards)** (@ `package/lib/applyToDefaults.js`) -> Impact: **27.8** | LOC: 35
- `exports` **(Many-Argument Workhorses)** (@ `package/lib/intersect.js`) -> Impact: **21.3** | LOC: 26

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 49 | 1371.3 | 19.89% | 2.04% |
| `package` | 3 | 3.22 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/index.d.ts` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/escapeHtml.js` -> **100.0%** Exposure
- `package/lib/index.js` -> **100.0%** Exposure
- `package/lib/merge.js` -> **100.0%** Exposure
- `package/lib/reach.js` -> **100.0%** Exposure
- `package/lib/applyToDefaults.js` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/index.d.ts` -> **15** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/deepEqual.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.199)
- **Top Global Matches:** file_cluster_6: 9.199, file_cluster_8: 11.403, file_cluster_4: 15.968
- **Magnitude:** 275.54 | **LOC:** 318 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 19.051; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (98.2%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isDeepEqualObj` **(Many-Argument Workhorses)** (Impact: 143.2)
  * `isDeepEqual` **(Defensive Guards)** (Impact: 49.9)
  * `getSharedType` **(Defensive Guards)** (Impact: 8.8)
  * `isSetSimpleEqual` **(Callbacks & Closures)** (Impact: 5.7)
  * `isSame` **(Defensive Guards)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 54`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.051
  * `Choke Point (Betweenness):` 0.000784 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 1):` types
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/contain.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.938)
- **Top Global Matches:** file_cluster_8: 6.938, file_cluster_6: 17.553, file_cluster_3: 19.848
- **Magnitude:** 242.52 | **LOC:** 308 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 15.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `array` **(Many-Argument Workhorses)** (Impact: 73.5)
  * `string` **(Many-Argument Workhorses)** (Impact: 46.0)
  * `object` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `exports` **(Defensive Guards)** (Impact: 11.6)
  * `compare` **(Defensive Guards)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 41`, `args: 10`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.000261 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 4):` assert, deepEqual, escapeRegex, utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/clone.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.854)
- **Top Global Matches:** file_cluster_3: 6.854, file_cluster_8: 20.537, file_cluster_6: 33.394
- **Magnitude:** 160.42 | **LOC:** 199 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 24.449; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (76.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clone` **(Many-Argument Workhorses)** (Impact: 77.6)
  * `base` **(Defensive Guards)** (Impact: 34.5)
  * `cloneWithShallow` **(Defensive Guards)** (Impact: 7.9)
  * `clone` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.449
  * `Choke Point (Betweenness):` 0.002026 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 3):` reach, types, utils
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/reach.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.622)
- **Top Global Matches:** file_cluster_3: 7.622, file_cluster_8: 20.892, file_cluster_6: 33.653
- **Magnitude:** 95.6 | **LOC:** 77 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 39.333; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 58.8)
  * `iterables` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.333
  * `Choke Point (Betweenness):` 0.002353 | `Ripple Effect (Closeness):` 0.10084
  * `Imports (Out-Degree: 1):` assert
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/applyToDefaults.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.458)
- **Top Global Matches:** file_cluster_9: 6.458, file_cluster_15: 12.62, file_cluster_16: 12.69
- **Magnitude:** 92.72 | **LOC:** 103 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 15.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `applyToDefaultsWithShallow` **(Defensive Guards)** (Impact: 27.8)
  * `exports` **(Defensive Guards)** (Impact: 17.1)
  * `reachCopy` **(Defensive Guards)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 11`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 4):` assert, clone, merge, reach
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/merge.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.697)
- **Top Global Matches:** file_cluster_1: 6.697, file_cluster_3: 48.371, file_cluster_8: 70.158
- **Magnitude:** 86.58 | **LOC:** 79 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 19.051; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge` **(Defensive Guards)** (Impact: 57.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.051
  * `Choke Point (Betweenness):` 0.000458 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 3):` assert, clone, utils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 17.334)
- **Top Global Matches:** file_cluster_17: 17.334, file_cluster_2: 17.565, file_cluster_13: 17.657
- **Magnitude:** 59.46 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 14.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 22`, `import: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` applyToDefaults, assert, assertError, bench, block, clone, contain, deepEqual...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/wait.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.167)
- **Top Global Matches:** file_cluster_10: 9.167, file_cluster_9: 9.569, file_cluster_15: 10.879
- **Magnitude:** 46.32 | **LOC:** 38 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (93.1%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 17.5)
  * `activate` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 4`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `concurrency: 3`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/escapeHtml.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.52)
- **Top Global Matches:** file_cluster_10: 5.52, file_cluster_15: 7.275, file_cluster_2: 7.749
- **Magnitude:** 42.92 | **LOC:** 88 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (58.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Compute Cores)** (Impact: 8.2)
  * `escapeHtmlChar` **(Callbacks & Closures)** (Impact: 4.9)
  * `isSafe` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 10`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/types.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.89)
- **Top Global Matches:** file_cluster_9: 6.89, file_cluster_15: 12.783, file_cluster_16: 12.804
- **Magnitude:** 42.48 | **LOC:** 58 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 37.706; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (99.8%), Concurrency Surface (formerly Concurrency) (99.6%), Mutation Surface (formerly State Flux) (96.1%), Connectivity (formerly Api Exposure) (82.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getInternalProto` **(Defensive Guards)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 15`, `concurrency: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.706
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.080065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/intersect.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.102)
- **Top Global Matches:** file_cluster_9: 7.102, file_cluster_15: 9.016, file_cluster_10: 9.127
- **Magnitude:** 38.76 | **LOC:** 42 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `has` **(Defensive Guards)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 5`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/index.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 18.027)
- **Top Global Matches:** file_cluster_17: 18.027, file_cluster_15: 18.064, file_cluster_13: 18.072
- **Magnitude:** 37.44 | **LOC:** 44 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 14.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 22`
* *Risk/State:* None
* *Architecture:* `api: 22`, `import: 22`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` applyToDefaults.js, assert.js, assertError.js, bench.js, block.js, clone.js, contain.js, deepEqual.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/once.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.073)
- **Top Global Matches:** file_cluster_10: 5.073, file_cluster_2: 7.893, file_cluster_15: 8.34
- **Magnitude:** 18.66 | **LOC:** 26 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Callbacks & Closures)** (Impact: 5.1)
  * `wrappedFn` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/flatten.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.467)
- **Top Global Matches:** file_cluster_10: 6.467, file_cluster_2: 7.342, file_cluster_15: 7.376
- **Magnitude:** 16.68 | **LOC:** 21 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flatten` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/assertError.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.497)
- **Top Global Matches:** file_cluster_15: 6.497, file_cluster_2: 6.504, file_cluster_11: 7.262
- **Magnitude:** 13.82 | **LOC:** 19 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 47.409; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (35.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.103199
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/escapeJson.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.192)
- **Top Global Matches:** file_cluster_10: 4.192, file_cluster_2: 7.237, file_cluster_15: 7.919
- **Magnitude:** 13.16 | **LOC:** 29 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (55.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Callbacks & Closures)** (Impact: 3.2)
  * `escape` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/assert.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_9: 7.625, file_cluster_10: 13.165, file_cluster_15: 13.247
- **Magnitude:** 12.78 | **LOC:** 31 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **2**; blast radius 74.576; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (25.0%), Complexity Load (formerly Cognitive Load) (6.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 3`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 74.576
  * `Choke Point (Betweenness):` 0.00549 | `Ripple Effect (Closeness):` 0.144385
  * `Imports (Out-Degree: 2):` assertError, stringify
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `package/lib/bench.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 4.63)
- **Top Global Matches:** file_cluster_11: 4.63, file_cluster_2: 6.27, file_cluster_13: 6.88
- **Magnitude:** 11.16 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(State Mutators)** (Impact: 1.2)
  * `reset` **(State Mutators)** (Impact: 1.2)
  * `elapsed` **(Interface Declarations)** (Impact: 1.2)
  * `now` **(Interface Declarations)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.005)
- **Top Global Matches:** file_cluster_10: 7.005, file_cluster_15: 8.829, file_cluster_2: 8.947
- **Magnitude:** 7.8 | **LOC:** 10 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 30.249; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keys` **(Defensive Guards)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/escapeRegex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.312)
- **Top Global Matches:** file_cluster_10: 5.312, file_cluster_2: 8.564, file_cluster_15: 9.009
- **Magnitude:** 7.2 | **LOC:** 12 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 19.051; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (22.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.058824
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/isPromise.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.801)
- **Top Global Matches:** file_cluster_10: 6.801, file_cluster_15: 8.691, file_cluster_2: 8.76
- **Magnitude:** 7.1 | **LOC:** 10 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 15.712; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/reachTemplate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_10: 6.608, file_cluster_15: 8.538, file_cluster_2: 8.805
- **Magnitude:** 6.58 | **LOC:** 17 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 15.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.3%), Connectivity (formerly Api Exposure) (21.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 1):` reach
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/index.d.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.782)
- **Top Global Matches:** file_cluster_5: 9.782, file_cluster_7: 12.689, file_cluster_14: 13.315
- **Magnitude:** 5.78 | **LOC:** 481 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stringify` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* /** * Converts a JavaScript value to a JavaScript Object Notation (JSON) string with protection agai...
  * `wait` **(Generic / Templated Code)** (Impact: 5.2)
    * *Intent:* /** * Returns a Promise that resolves after the requested timeout. * * */
  * `deepEqual` **(Compute Cores)** (Impact: 4.0)
    * *Intent:* /// <reference types="node" /> /** * Performs a deep comparison of the two values including support ...
  * `merge` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /** * Merge all the properties of source into target. * * */
  * `applyToDefaults` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /** * Apply source to a copy of the defaults. * * */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 66`, `args: 28`, `func_start: 28`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `unreferenced_by_name: 15`
* *Architecture:* `api: 34`, `concurrency: 2`
* *Defense:* `safety: 2`, `doc: 52`, `test: 2`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/block.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.59)
- **Top Global Matches:** file_cluster_10: 4.59, file_cluster_2: 8.114, file_cluster_13: 8.588
- **Magnitude:** 4.32 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 15.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (28.2%), Connectivity (formerly Api Exposure) (21.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Callbacks & Closures)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039216
  * `Imports (Out-Degree: 1):` ignore
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/stringify.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.474)
- **Top Global Matches:** file_cluster_10: 6.474, file_cluster_2: 7.671, file_cluster_15: 8.074
- **Magnitude:** 4.1 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 47.409; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.9%), Connectivity (formerly Api Exposure) (22.5%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Defensive Guards)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.409
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.103199
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/lib/assertError.js` (JAVASCRIPT) | Magnitude: 13.82 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, branch: 2, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/lib/index.mjs` (JAVASCRIPT) | Magnitude: 37.44 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 22, structural_boundaries: 22, api: 22, import: 22
- `package/lib/index.js` (JAVASCRIPT) | Magnitude: 59.46 | Delta: **0.231** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 22, state_mutation: 22, import: 22, events: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/reach.js` -> **Severity: 0.235** (Bridge: 0.0024 * Flux: 100.0%)
- `package/lib/clone.js` -> **Severity: 0.202** (Bridge: 0.002 * Flux: 99.9246%)
- `package/lib/deepEqual.js` -> **Severity: 0.078** (Bridge: 0.0008 * Flux: 99.7667%)
- `package/lib/merge.js` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 100.0%)
- `package/lib/contain.js` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/assertError.js` -> **Severity: 5.307** (Embedded: 0.1032 * Error Risk: 51.4282%)
- `package/lib/stringify.js` -> **Severity: 4.939** (Embedded: 0.1032 * Error Risk: 47.8585%)
- `package/lib/reach.js` -> **Severity: 4.242** (Embedded: 0.1008 * Error Risk: 42.0676%)
- `package/lib/utils.js` -> **Severity: 3.978** (Embedded: 0.0784 * Error Risk: 50.7142%)
- `package/lib/types.js` -> **Severity: 3.832** (Embedded: 0.0801 * Error Risk: 47.8585%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/assert.js` -> **Severity: 7457.6** (Blast Radius: 74.576 * Doc Risk: 100.0%)
- `package/lib/assertError.js` -> **Severity: 4740.9** (Blast Radius: 47.409 * Doc Risk: 100.0%)
- `package/lib/stringify.js` -> **Severity: 4740.9** (Blast Radius: 47.409 * Doc Risk: 100.0%)
- `package/lib/reach.js` -> **Severity: 3933.3** (Blast Radius: 39.333 * Doc Risk: 100.0%)
- `package/lib/types.js` -> **Severity: 3770.6** (Blast Radius: 37.706 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 162 call pairs -- scoped 3.7%, unique 0.0%, ambiguous 0.6%, external 95.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 162 | 3.7% | 0.0% | 0.6% | 95.7% |

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
