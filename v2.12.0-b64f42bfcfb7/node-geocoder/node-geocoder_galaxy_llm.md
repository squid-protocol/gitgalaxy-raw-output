# ARCHITECTURAL_BRIEF: node-geocoder
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
- **Scope:** 37 analyzed artifact(s), 3185 LOC.
- **Load-bearing artifact:** `package/lib/geocoder/abstractgeocoder.js` -- 19 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/geocoderfactory.js` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/geocoder/googlegeocoder.js` at magnitude 297.46 (structural weight, not risk).
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
| Total Artifacts | 38 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 3185 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.4% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1664 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7956 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5514 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 32 | 3185 | 86.5% |
| MARKDOWN | 3 | 0 | 8.1% |
| PLAINTEXT | 2 | 0 | 5.4% |

## 4.1 SOURCE ENCODINGS
All 37 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Callbacks & Closures Files 22%, Large Core Modules (3) 22%, Data / Markup / Trivial 19%, Compute Cores Files 16%, Large Core Modules (2) 14%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32 | 86.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 13.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.7 | 47.6 | 49.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 41.7 | 79.0 | 63.3 | 62.7 | 57.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 29.1 | 2.6 | 80.0 |
| Connectivity (formerly API Exposure) | 3.5 | 45.9 | 29.9 | 31.5 | 20.1 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 16.8 | 100.0 | 93.8 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.8 | 14.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4 | 1 | 0 | `package/lib/geocoder/heregeocoder.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 117 | 20 | 8 | `package/lib/geocoderfactory.js` |
| danger | 91 | 23 | 5 | `package/lib/geocoder/agolgeocoder.js` |
| concurrency | 53 | 6 | 3 | `package/lib/geocoder/heregeocoder.js` |
| connectivity | 85 | 32 | 4 | `package/lib/geocoder/heregeocoder.js` |
| io | 12 | 6 | 1 | `package/lib/httpadapter/fetchadapter.js` |
| crypto | 1 | 1 | 0 | `package/lib/geocoder/googlegeocoder.js` |
| ipc | 0 | 0 | 0 | - |
| time | 2 | 1 | 0 | `package/lib/geocoder/agolgeocoder.js` |
| serialization | 5 | 3 | 0 | `package/lib/geocoder/agolgeocoder.js` |
| regex | 21 | 8 | 1 | `package/lib/formatter/stringformatter.js` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 83 | 26 | 4 | `package/lib/geocoder/locationiqgeocoder.js` |
| debt | 0 | 0 | 0 | - |
| mutation | 1040 | 32 | 67 | `package/lib/geocoder/googlegeocoder.js` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/httpadapter/fetchadapter.js` (Hits: 6)
- `package/lib/geocoderfactory.js` (Hits: 2)
- `package/lib/geocoder/abstractgeocoder.js` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **abstractgeocoder.js** (`package/lib/geocoder/abstractgeocoder.js`) — 19 inbound connections
2. **valueerror.js** (`package/lib/error/valueerror.js`) — 3 inbound connections
3. **openstreetmapgeocoder.js** (`package/lib/geocoder/openstreetmapgeocoder.js`) — 3 inbound connections
4. **httperror.js** (`package/lib/error/httperror.js`) — 1 inbound connections
5. **gpxformatter.js** (`package/lib/formatter/gpxformatter.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **geocoderfactory.js** (`package/lib/geocoderfactory.js`) — 27 outbound dependencies
2. **aplacegeocoder.js** (`package/lib/geocoder/aplacegeocoder.js`) — 4 outbound dependencies
3. **googlegeocoder.js** (`package/lib/geocoder/googlegeocoder.js`) — 4 outbound dependencies
4. **datasciencetoolkitgeocoder.js** (`package/lib/geocoder/datasciencetoolkitgeocoder.js`) — 3 outbound dependencies
5. **geocodiogeocoder.js** (`package/lib/geocoder/geocodiogeocoder.js`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_getGeocoder` **(Defensive Guards)** (@ `package/lib/geocoderfactory.js`) -> Impact: **51.5** | LOC: 110
  * *Intent:* /** * Return a geocoder adapter by name */
- `_formatResult` **(Compute Cores)** (@ `package/lib/geocoder/googlegeocoder.js`) -> Impact: **42.1** | LOC: 107
- `_geocode` **(Many-Argument Workhorses)** (@ `package/lib/geocoder/googlegeocoder.js`) -> Impact: **38.7** | LOC: 82
  * *Intent:* /** * Geocode */
- `_geocode` **(Defensive Guards)** (@ `package/lib/geocoder/aplacegeocoder.js`) -> Impact: **36.7** | LOC: 75
- `_formatResult` **(Compute Cores)** (@ `package/lib/geocoder/heregeocoder.js`) -> Impact: **32.2** | LOC: 51
- `_geocode` **(Defensive Guards)** (@ `package/lib/geocoder/heregeocoder.js`) -> Impact: **28.6** | LOC: 53
  * *Intent:* /** * Geocode */
- `_geocode` **(Compute Cores)** (@ `package/lib/geocoder/opendatafrancegeocoder.js`) -> Impact: **28.6** | LOC: 53
  * *Intent:* /** * Geocode */
- `_geocode` **(Compute Cores)** (@ `package/lib/geocoder/opencagegeocoder.js`) -> Impact: **28.3** | LOC: 46
  * *Intent:* /** * Geocode */
- `__pollJobStatusAndFetchResults` **(Defensive Guards)** (@ `package/lib/geocoder/tomtomgeocoder.js`) -> Impact: **26.3** | LOC: 42
- `_geocode` **(Defensive Guards)** (@ `package/lib/geocoder/mapquestgeocoder.js`) -> Impact: **24.7** | LOC: 43
  * *Intent:* /** * Geocode */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib/geocoder` | 23 | 2642.5 | 52.37% | 0.0% |
| `package/lib` | 3 | 199.38 | 24.67% | 0.0% |
| `package/lib/httpadapter` | 1 | 128.92 | 99.74% | 0.0% |
| `package/lib/formatter` | 2 | 46.88 | 47.17% | 0.0% |
| `package/lib/error` | 2 | 29.84 | 25.5% | 0.0% |
| `package` | 6 | 24.66 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/geocoder/aplacegeocoder.js` -> **100.0%** Exposure
- `package/lib/geocoder/datasciencetoolkitgeocoder.js` -> **100.0%** Exposure
- `package/lib/geocoder/googlegeocoder.js` -> **100.0%** Exposure
- `package/lib/geocoder/locationiqgeocoder.js` -> **100.0%** Exposure
- `package/lib/geocoder/mapquestgeocoder.js` -> **100.0%** Exposure

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

### `package/lib/geocoder/googlegeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.12)
- **Top Global Matches:** file_cluster_8: 6.12, file_cluster_6: 12.921, file_cluster_4: 21.523
- **Magnitude:** 297.46 | **LOC:** 356 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formatResult` **(Compute Cores)** (Impact: 42.1)
  * `_geocode` **(Many-Argument Workhorses)** (Impact: 38.7)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Compute Cores)** (Impact: 18.1)
    * *Intent:* /** * Reverse geocoding */
  * `_prepareQueryString` **(I/O & Config Routines)** (Impact: 10.6)
  * `GoogleGeocoder` **(State Mutators)** (Impact: 9.7)
    * *Intent:* /** * Constructor */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 54`, `args: 9`, `func_start: 8`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 10`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, crypto, url, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/heregeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.154)
- **Top Global Matches:** file_cluster_4: 7.154, file_cluster_9: 10.696, file_cluster_10: 11.239
- **Magnitude:** 291.16 | **LOC:** 459 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (96.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.2%)
- **Documentation Coverage:** 64.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formatResult` **(Compute Cores)** (Impact: 32.2)
  * `_geocode` **(Defensive Guards)** (Impact: 28.6)
    * *Intent:* /** * Geocode */
  * `_getJobResults` **(Compute Cores)** (Impact: 22.9)
  * `constructor` **(Compute Cores)** (Impact: 11.0)
  * `_prepareQueryString` **(I/O & Config Routines)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 68`, `args: 27`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`
* *Architecture:* `api: 5`, `concurrency: 18`, `import: 3`
* *Defense:* `safety: 7`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.000877 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 2):` valueerror, abstractgeocoder, readline
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/aplacegeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.712)
- **Top Global Matches:** file_cluster_6: 8.712, file_cluster_4: 9.068, file_cluster_9: 14.586
- **Magnitude:** 252.32 | **LOC:** 313 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.6%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Defensive Guards)** (Impact: 36.7)
  * `_formatResult` **(Compute Cores)** (Impact: 24.6)
  * `APlaceGeocoder` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /** * APlaceGeocoder Constructor */
  * `_reverse` **(Defensive Guards)** (Impact: 17.8)
  * `geocode` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** * Geocode */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 33`, `args: 12`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 48`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 11`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.000877 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 2):` valueerror.js, abstractgeocoder, net, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/agolgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.211)
- **Top Global Matches:** file_cluster_12: 10.211, file_cluster_9: 10.739, file_cluster_7: 10.778
- **Magnitude:** 203.74 | **LOC:** 274 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 13.806; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (71.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AGOLGeocoder` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Compute Cores)** (Impact: 20.5)
  * `geocode` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /** * Geocode */
  * `reverse` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* /** * Reverse geocoding */
  * `execute` **(Defensive Guards)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 43`, `args: 15`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 34`
* *Architecture:* `io: 1`, `api: 2`, `import: 1`
* *Defense:* `safety: 8`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 0):` net
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/opendatafrancegeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.157)
- **Top Global Matches:** file_cluster_9: 7.157, file_cluster_12: 9.403, file_cluster_15: 9.711
- **Magnitude:** 168.8 | **LOC:** 183 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* /** * Geocode */
  * `_formatResult` **(Defensive Guards)** (Impact: 19.1)
  * `_reverse` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* /** * Reverse geocoding */
  * `_getCommonParams` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * Prepare common params * */
  * `OpendataFranceGeocoder` **(State Mutators)** (Impact: 2.0)
    * *Intent:* /** * Constructor */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 26`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 7`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/openstreetmapgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.458)
- **Top Global Matches:** file_cluster_9: 7.458, file_cluster_12: 8.75, file_cluster_10: 8.828
- **Magnitude:** 167.02 | **LOC:** 169 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 37.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (62.5%)
- **Documentation Coverage:** 18.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Defensive Guards)** (Impact: 19.4)
    * *Intent:* /** * Geocode */
  * `_formatResult` **(Compute Cores)** (Impact: 15.7)
  * `_reverse` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Reverse geocoding */
  * `OpenStreetMapGeocoder` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /** * Constructor */
  * `_getCommonParams` **(Callbacks & Closures)** (Impact: 4.8)
    * *Intent:* /** * Prepare common params * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 8`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.276
  * `Choke Point (Betweenness):` 0.003258 | `Ripple Effect (Closeness):` 0.088889
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/tomtomgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.404)
- **Top Global Matches:** file_cluster_10: 8.404, file_cluster_9: 8.519, file_cluster_15: 9.074
- **Magnitude:** 154.72 | **LOC:** 222 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.3%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__pollJobStatusAndFetchResults` **(Defensive Guards)** (Impact: 26.3)
  * `__createJob` **(Compute Cores)** (Impact: 17.1)
  * `_geocode` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* /** * Geocode */
  * `TomTomGeocoder` **(State Mutators)** (Impact: 5.5)
    * *Intent:* /** * Constructor */
  * `__parseBatchResults` **(Callbacks & Closures)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 34`, `args: 15`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 8`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/locationiqgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.027)
- **Top Global Matches:** file_cluster_10: 8.027, file_cluster_12: 8.203, file_cluster_15: 9.029
- **Magnitude:** 137.28 | **LOC:** 175 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 9.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Defensive Guards)** (Impact: 23.1)
    * *Intent:* /** * Geocode * Value to geocode (Adress String or parameters as specified over at * http://location...
  * `_formatResult` **(Compute Cores)** (Impact: 17.2)
  * `_reverse` **(Callbacks & Closures)** (Impact: 8.4)
    * *Intent:* /** * Reverse geocoding */
  * `LocationIQGeocoder` **(State Mutators)** (Impact: 5.7)
    * *Intent:* /** * Constructor * * Geocoder for LocationIQ * http://locationiq.org/#docs * */
  * `_forceParams` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* /** * Adds parameters that are enforced * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 21`, `args: 10`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/opencagegeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.847)
- **Top Global Matches:** file_cluster_9: 7.847, file_cluster_12: 8.088, file_cluster_10: 8.387
- **Magnitude:** 136.74 | **LOC:** 159 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%), Complexity Load (formerly Cognitive Load) (55.4%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Defensive Guards)** (Impact: 11.7)
    * *Intent:* /** * Reverse geocoding */
  * `OpenCageGeocoder` **(Many-Argument Workhorses)** (Impact: 6.7)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 5.2)
  * `_getCommonParams` **(Callbacks & Closures)** (Impact: 2.5)
    * *Intent:* /** * Prepare common params * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 18`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/httpadapter/fetchadapter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.031)
- **Top Global Matches:** file_cluster_9: 8.031, file_cluster_15: 8.339, file_cluster_11: 9.041
- **Magnitude:** 128.92 | **LOC:** 104 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.7%), Guard Balance (formerly Safety Score) (59.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `post` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `constructor` **(Parameter Forwarders)** (Impact: 3.1)
  * `supportsHttps` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 20`, `args: 8`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 6`, `api: 5`, `concurrency: 9`, `import: 3`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.001587 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` httperror.js, bluebird, node-fetch
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoderfactory.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.375)
- **Top Global Matches:** file_cluster_8: 10.375, file_cluster_6: 12.048, file_cluster_4: 19.384
- **Magnitude:** 102.26 | **LOC:** 219 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 24.135; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.7%), Connectivity (formerly Api Exposure) (23.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getGeocoder` **(Defensive Guards)** (Impact: 51.5)
    * *Intent:* /** * Return a geocoder adapter by name */
  * `getGeocoder` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* /** * Return a geocoder */
  * `_getFormatter` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* /** * Return an formatter adapter by name */
  * `_getHttpAdapter` **(Defensive Guards)** (Impact: 3.7)
    * *Intent:* /** * Return an http adapter by name */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 29`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 2`, `api: 2`, `import: 27`
* *Defense:* `safety: 27`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.135
  * `Choke Point (Betweenness):` 0.02381 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 27):` gpxformatter.js, stringformatter.js, geocoder.js, agolgeocoder.js, aplacegeocoder.js, datasciencetoolkitgeocoder.js, freegeoipgeocoder.js, geocodiogeocoder.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/mapboxgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.01)
- **Top Global Matches:** file_cluster_10: 6.01, file_cluster_15: 6.678, file_cluster_2: 7.621
- **Magnitude:** 91.22 | **LOC:** 171 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formatResult` **(Compute Cores)** (Impact: 14.8)
  * `_geocode` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Reverse geocoding */
  * `constructor` **(Compute Cores)** (Impact: 5.6)
  * `_prepareQueryString` **(Callbacks & Closures)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 19`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/mapquestgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.394)
- **Top Global Matches:** file_cluster_12: 7.394, file_cluster_10: 7.595, file_cluster_15: 8.913
- **Magnitude:** 90.26 | **LOC:** 118 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (56.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Defensive Guards)** (Impact: 24.7)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Callbacks & Closures)** (Impact: 8.1)
    * *Intent:* /** * Reverse geocoding */
  * `MapQuestGeocoder` **(State Mutators)** (Impact: 5.7)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 3`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.713)
- **Top Global Matches:** file_cluster_10: 5.713, file_cluster_15: 9.236, file_cluster_2: 9.379
- **Magnitude:** 88.98 | **LOC:** 123 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 13.806; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.9%), Complexity Load (formerly Cognitive Load) (52.4%)
- **Documentation Coverage:** 23.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_filter` **(Callbacks & Closures)** (Impact: 11.1)
  * `_format` **(Callbacks & Closures)** (Impact: 7.2)
  * `geocode` **(Callbacks & Closures)** (Impact: 2.5)
    * *Intent:* /** * Geocode a value (address or ip) */
  * `reverse` **(Callbacks & Closures)** (Impact: 2.4)
    * *Intent:* /** * Reverse geocoding */
  * `batchGeocode` **(Callbacks & Closures)** (Impact: 2.2)
    * *Intent:* /** * Batch geocode * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 22`, `args: 19`, `func_start: 6`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 4`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 0):` bluebird
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/yandexgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.745)
- **Top Global Matches:** file_cluster_10: 6.745, file_cluster_15: 6.962, file_cluster_16: 8.606
- **Magnitude:** 88.84 | **LOC:** 146 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.7%), Complexity Load (formerly Cognitive Load) (54.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_processOptionsToParams` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `_findKey` **(Defensive Guards)** (Impact: 7.9)
  * `_geocode` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* /** * Geocode */
  * `_formatResult` **(Parameter Forwarders)** (Impact: 2.2)
  * `_reverse` **(Callbacks & Closures)** (Impact: 2.1)
    * *Intent:* /** * Reverse geocoding */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 16`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 5`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/abstractgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.036)
- **Top Global Matches:** file_cluster_7: 9.036, file_cluster_12: 9.37, file_cluster_5: 10.696
- **Magnitude:** 86.74 | **LOC:** 124 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **2**; blast radius 244.226; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%), Concurrency Surface (formerly Concurrency) (53.6%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `geocode` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* /** * Geocode */
  * `AbstractGeocoder` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* /** * AbstractGeocoder Constructor */
  * `batchGeocode` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Batch Geocode */
  * `reverse` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* /** * Reverse geocoding */
  * `formatGeocoderName` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 11`, `args: 8`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 7`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 244.226
  * `Choke Point (Betweenness):` 0.015079 | `Ripple Effect (Closeness):` 0.524802
  * `Imports (Out-Degree: 1):` valueerror.js, net
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/teleportgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.285)
- **Top Global Matches:** file_cluster_9: 6.285, file_cluster_15: 7.844, file_cluster_16: 9.176
- **Magnitude:** 81.94 | **LOC:** 136 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_formatResult` **(Compute Cores)** (Impact: 17.5)
  * `_reverse` **(Compute Cores)** (Impact: 11.9)
    * *Intent:* /** * Reverse geocoding * */
  * `_geocode` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* /** * Geocode * */
  * `getEmbeddedPath` **(Compute Cores)** (Impact: 7.7)
  * `TeleportGeocoder` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* /** * Constructor */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 36`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/openmapquestgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.097)
- **Top Global Matches:** file_cluster_12: 7.097, file_cluster_15: 8.079, file_cluster_10: 8.382
- **Magnitude:** 72.78 | **LOC:** 124 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (53.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_reverse` **(Compute Cores)** (Impact: 11.9)
    * *Intent:* /** * Reverse geocoding */
  * `_geocode` **(Defensive Guards)** (Impact: 10.0)
    * *Intent:* /** * Geocode */
  * `OpenMapQuestGeocoder` **(State Mutators)** (Impact: 5.8)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 18`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/geocodiogeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.046)
- **Top Global Matches:** file_cluster_10: 7.046, file_cluster_12: 7.182, file_cluster_15: 8.146
- **Magnitude:** 64.54 | **LOC:** 113 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.1%), Complexity Load (formerly Cognitive Load) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Compute Cores)** (Impact: 6.6)
    * *Intent:* /** * Reverse geocoding */
  * `GeocodioGeocoder` **(State Mutators)** (Impact: 5.7)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/mapzengeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.117)
- **Top Global Matches:** file_cluster_10: 7.117, file_cluster_12: 7.231, file_cluster_15: 8.576
- **Magnitude:** 64.04 | **LOC:** 106 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (48.6%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Geocode */
  * `_reverse` **(Callbacks & Closures)** (Impact: 6.5)
    * *Intent:* /** * Reverse geocoding */
  * `MapzenGeocoder` **(State Mutators)** (Impact: 5.8)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, querystring, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/virtualearth.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.32)
- **Top Global Matches:** file_cluster_12: 7.32, file_cluster_10: 7.496, file_cluster_15: 9.025
- **Magnitude:** 47.12 | **LOC:** 98 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_reverse` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Reverse geocoding */
  * `_geocode` **(Callbacks & Closures)** (Impact: 8.1)
    * *Intent:* /** * Geocode */
  * `VirtualEarthGeocoder` **(State Mutators)** (Impact: 5.6)
    * *Intent:* /** * Constructor */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/smartystreetsgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.339)
- **Top Global Matches:** file_cluster_12: 7.339, file_cluster_10: 7.649, file_cluster_7: 9.432
- **Magnitude:** 47.04 | **LOC:** 91 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SmartyStreets` **(State Mutators)** (Impact: 6.5)
    * *Intent:* /** * SmartyStreets Constructor */
  * `geocode` **(Callbacks & Closures)** (Impact: 6.4)
    * *Intent:* /** * Geocode */
  * `reverse` **(Defensive Guards)** (Impact: 4.3)
    * *Intent:* /** * Reverse geocoding */
  * `_formatResult` **(Callbacks & Closures)** (Impact: 3.7)
    * *Intent:* /** * Format Result **/
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 8`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/geocoder/datasciencetoolkitgeocoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.94)
- **Top Global Matches:** file_cluster_10: 6.94, file_cluster_15: 7.842, file_cluster_16: 8.705
- **Magnitude:** 46.84 | **LOC:** 75 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 13.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_geocode` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* /** * Geocode */
  * `_endpoint` **(Callbacks & Closures)** (Impact: 4.9)
    * *Intent:* /** * Build DSTK endpoint, allows for local DSTK installs */
  * `DataScienceToolkitGeocoder` **(State Mutators)** (Impact: 2.0)
    * *Intent:* /** * Constructor */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 1`, `api: 2`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` abstractgeocoder, net, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/formatter/gpxformatter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.343)
- **Top Global Matches:** file_cluster_10: 4.343, file_cluster_2: 7.576, file_cluster_15: 8.091
- **Magnitude:** 25.02 | **LOC:** 23 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 13.806; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.6%), Complexity Load (formerly Cognitive Load) (58.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Callbacks & Closures)** (Impact: 3.6)
  * `GpxFormatter` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.806
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/error/httperror.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.533)
- **Top Global Matches:** file_cluster_10: 6.533, file_cluster_15: 6.887, file_cluster_2: 7.575
- **Magnitude:** 23.86 | **LOC:** 20 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 24.781; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HttpError` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.781
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `package/lib/geocoder/mapzengeocoder.js` (JAVASCRIPT) | Magnitude: 64.04 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 17, core_var_decl: 15, state_mutation: 14
- `package/lib/geocoder/tomtomgeocoder.js` (JAVASCRIPT) | Magnitude: 154.72 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 34, branch: 31, core_var_decl: 25
- `package/lib/geocoder/geocodiogeocoder.js` (JAVASCRIPT) | Magnitude: 64.54 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 17, core_var_decl: 15, state_mutation: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/geocoderfactory.js` -> **Severity: 2.208** (Bridge: 0.0238 * Flux: 92.7157%)
- `package/lib/geocoder/abstractgeocoder.js` -> **Severity: 1.508** (Bridge: 0.0151 * Flux: 99.9972%)
- `package/lib/geocoder/openstreetmapgeocoder.js` -> **Severity: 0.326** (Bridge: 0.0033 * Flux: 100.0%)
- `package/lib/httpadapter/fetchadapter.js` -> **Severity: 0.159** (Bridge: 0.0016 * Flux: 99.9992%)
- `package/lib/geocoder/aplacegeocoder.js` -> **Severity: 0.088** (Bridge: 0.0009 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/geocoder/abstractgeocoder.js` -> **Severity: 36.857** (Embedded: 0.5248 * Error Risk: 70.2299%)
- `package/lib/error/valueerror.js` -> **Severity: 17.38** (Embedded: 0.3333 * Error Risk: 52.1415%)
- `package/lib/geocoder/openstreetmapgeocoder.js` -> **Severity: 7.018** (Embedded: 0.0889 * Error Risk: 78.9512%)
- `package/lib/geocoder/locationiqgeocoder.js` -> **Severity: 2.831** (Embedded: 0.037 * Error Risk: 76.4483%)
- `package/lib/geocoder/opendatafrancegeocoder.js` -> **Severity: 2.785** (Embedded: 0.037 * Error Risk: 75.2005%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/error/valueerror.js` -> **Severity: 23236.0** (Blast Radius: 232.36 * Doc Risk: 100.0%)
- `package/lib/geocoder/abstractgeocoder.js` -> **Severity: 3488.939** (Blast Radius: 244.226 * Doc Risk: 14.2857%)
- `package/lib/error/httperror.js` -> **Severity: 2478.1** (Blast Radius: 24.781 * Doc Risk: 100.0%)
- `package/lib/formatter/gpxformatter.js` -> **Severity: 1380.6** (Blast Radius: 13.806 * Doc Risk: 100.0%)
- `package/lib/formatter/stringformatter.js` -> **Severity: 1380.6** (Blast Radius: 13.806 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 454 call pairs -- scoped 11.9%, unique 0.0%, ambiguous 18.3%, external 69.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 454 | 11.9% | 0.0% | 18.3% | 69.8% |

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
