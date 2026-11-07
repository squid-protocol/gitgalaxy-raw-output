# ARCHITECTURAL_BRIEF: jquery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jquery/jquery.git` |
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
- **Scope:** 307 analyzed artifact(s), 34824 LOC.
- **Load-bearing artifact:** `src/core.js` -- 62 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/selector.js` -- pulls in 23 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 351 |
| Analyzed Artifacts (Scanned) | 307 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 44 |
| Total LOC | 34824 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 87.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6167 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3171 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9519 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 214 | 31614 | 69.7% |
| HTML | 61 | 2209 | 19.9% |
| YAML | 11 | 597 | 3.6% |
| MARKDOWN | 7 | 0 | 2.3% |
| PLAINTEXT | 7 | 1 | 2.3% |
| XML | 3 | 0 | 1.0% |
| PHP | 2 | 275 | 0.7% |
| CSS | 2 | 128 | 0.7% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 306 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 57%, Callbacks & Closures Files 14%, Large Core Modules (2) 12%, Declarative / Non-Code 7%, Many-Argument Workhorses Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 293 | 95.4% |
| Unknown | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 44*

**Composition by Extension & Reason:**
- `.js`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11486 LOC)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.1 | 16.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.0 | 31.8 | 47.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 6.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 85.7 | 10.1 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 84.5 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16 | 7 | 0 | `test/unit/css.js` |
| cleanup | 22 | 13 | 0 | `test/unit/selector.js` |
| guards | 1301 | 117 | 10 | `src/selector.js` |
| danger | 890 | 85 | 4 | `test/unit/ajax.js` |
| concurrency | 461 | 58 | 2 | `test/unit/deferred.js` |
| connectivity | 644 | 186 | 1 | `test/data/qunit-fixture.html` |
| io | 310 | 70 | 3 | `test/data/mock.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `test/data/event/onbeforeunload.html` |
| time | 91 | 32 | 1 | `test/unit/effects.js` |
| serialization | 21 | 9 | 0 | `test/middleware-mockserver.cjs` |
| regex | 139 | 50 | 1 | `test/unit/manipulation.js` |
| events | 1978 | 85 | 4 | `test/unit/event.js` |
| tests | 7086 | 37 | 1 | `test/unit/selector.js` |
| docs | 104 | 70 | 1 | `src/selector.js` |
| debt | 284 | 34 | 1 | `test/unit/ajax.js` |
| mutation | 8800 | 254 | 58 | `test/unit/manipulation.js` |
| dead_code | 139 | 53 | 1 | `test/middleware-mockserver.cjs` |
| credential | 5 | 3 | 0 | `.github/workflows/browser-tests.yml` |
| threat | 10 | 2 | 0 | `test/unit/selector.js` |
| ml_ai | 1 | 1 | 0 | `test/data/mock.php` |
| ui | 257 | 34 | 1 | `test/unit/manipulation.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/data/mock.php` (Hits: 65)
- `test/data/qunit-fixture.html` (Hits: 47)
- `test/index.html` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.js** (`src/core.js`) — 62 inbound connections
2. **iframeTest.js** (`test/data/iframeTest.js`) — 44 inbound connections
3. **document.js** (`src/var/document.js`) — 13 inbound connections
4. **whitespace.js** (`src/var/whitespace.js`) — 11 inbound connections
5. **arr.js** (`src/var/arr.js`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **selector.js** (`src/selector.js`) — 23 outbound dependencies
2. **css.js** (`src/css.js`) — 16 outbound dependencies
3. **core.js** (`src/core.js`) — 14 outbound dependencies
4. **manipulation.js** (`src/manipulation.js`) — 14 outbound dependencies
5. **selector-native.js** (`src/selector-native.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ajax` **(Many-Argument Workhorses)** (@ `src/ajax.js`) -> Impact: **201.6** | LOC: 464
  * *Intent:* // Main method
- `trigger` **(Many-Argument Workhorses)** (@ `src/event/trigger.js`) -> Impact: **127.9** | LOC: 144
- `CHILD` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **125.6** | LOC: 111
- `defaultPrefilter` **(Many-Argument Workhorses)** (@ `src/effects.js`) -> Impact: **104.3** | LOC: 167
- `find` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **98.0** | LOC: 126
- `setMatcher` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **94.9** | LOC: 98
- `superMatcher` **(Many-Argument Workhorses)** (@ `src/selector.js`) -> Impact: **91.4** | LOC: 113
- `remove` **(Many-Argument Workhorses)** (@ `src/event.js`) -> Impact: **86.9** | LOC: 72
  * *Intent:* // Detach an event or set of events from an element
- `done` **(Many-Argument Workhorses)** (@ `src/ajax.js`) -> Impact: **80.2** | LOC: 129
  * *Intent:* // Callback for when everything is done
- `add` **(Many-Argument Workhorses)** (@ `src/event.js`) -> Impact: **74.1** | LOC: 110

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/unit` | 24 | 6458.16 | 19.73% | 0.0% |
| `src` | 23 | 6281.22 | 63.14% | 32.2% |
| `__monolith__` | 11 | 5070.86 | 0.42% | 0.79% |
| `test/data` | 38 | 1355.69 | 2.89% | 0.0% |
| `test` | 6 | 470.12 | 8.2% | 0.0% |
| `src/attributes` | 4 | 434.02 | 73.13% | 8.82% |
| `src/core` | 15 | 400.66 | 32.79% | 7.55% |
| `test/data/offset` | 8 | 383.98 | 0.27% | 0.0% |
| `src/css` | 8 | 320.26 | 39.89% | 4.72% |
| `src/manipulation` | 6 | 310.94 | 38.77% | 13.63% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/ajax/script.js` -> **99.8783%** Exposure
- `.github/workflows/browser-tests.yml` -> **99.8388%** Exposure
- `src/traversing.js` -> **97.6035%** Exposure
- `src/data.js` -> **96.5285%** Exposure
- `src/callbacks.js` -> **93.8421%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/ajax.js` -> **100.0%** Exposure
- `src/ajax/jsonp.js` -> **100.0%** Exposure
- `src/ajax/load.js` -> **100.0%** Exposure
- `src/attributes/classes.js` -> **100.0%** Exposure
- `src/attributes/val.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/unit/ajax.js` -> **0** Orphaned Functions | **79** Duplicates
- `test/middleware-mockserver.cjs` -> **23** Orphaned Functions | **0** Duplicates
- `test/unit/effects.js` -> **3** Orphaned Functions | **8** Duplicates
- `test/unit/core.js` -> **0** Orphaned Functions | **10** Duplicates
- `test/unit/event.js` -> **6** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `116` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/selector.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.167)
- **Top Global Matches:** file_cluster_6: 7.167, file_cluster_8: 12.992, file_cluster_4: 13.327
- **Magnitude:** 1361.7 | **LOC:** 1377 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 86.2069% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CHILD` **(Many-Argument Workhorses)** (Impact: 125.6)
  * `find` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `setMatcher` **(Many-Argument Workhorses)** (Impact: 94.9)
  * `superMatcher` **(Many-Argument Workhorses)** (Impact: 91.4)
  * `matcherFromGroupMatchers` **(Many-Argument Workhorses)** (Impact: 68.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 501
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 185`, `args: 77`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 177`, `unreferenced_by_name: 9`
* *Architecture:* `api: 1`, `import: 23`
* *Defense:* `safety: 94`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` core.js, nodeName.js, createCache.js, filterMatchExpr.js, preFilter.js, rbuggyQSA.js, selectorError.js, testContext.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/ajax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.708)
- **Top Global Matches:** file_cluster_10: 8.708, file_cluster_12: 9.04, file_cluster_15: 11.277
- **Magnitude:** 996.78 | **LOC:** 4142 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (74.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.9%), Guard Balance (formerly Safety Score) (45.8%), Connectivity (formerly Api Exposure) (19.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Callbacks & Closures)** (Impact: 6.5)
  * `error` **(Callbacks & Closures)** (Impact: 6.2)
  * `request` **(Callbacks & Closures)** (Impact: 6.2)
  * `beforeSend` **(Defensive Guards)** (Impact: 5.7)
  * `beforeSend` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 338`, `args: 625`, `func_start: 331`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 1`, `state_mutation: 133`, `fragile_debt: 4`, `duplicate_logic: 79`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 62`
* *Defense:* `safety: 60`, `test: 601`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ajax.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.224)
- **Top Global Matches:** file_cluster_6: 7.224, file_cluster_8: 11.115, file_cluster_4: 14.543
- **Magnitude:** 890.7 | **LOC:** 889 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.512; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ajax` **(Many-Argument Workhorses)** (Impact: 201.6)
    * *Intent:* // Main method
  * `done` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* // Callback for when everything is done
  * `ajaxConvert` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* /* Chain conversions given the request and the original response * Also sets the responseXXX fields ...
  * `ajaxHandleResponses` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /* Handles responses to an ajax request: * - finds the right dataType (mediates between content-type...
  * `inspectPrefiltersOrTransports` **(Defensive Guards)** (Impact: 21.4)
    * *Intent:* // Base inspection function for prefilters and transports
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 59`, `args: 24`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 122`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 48`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.512
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.003268
  * `Imports (Out-Degree: 6):` location.js, nonce.js, rquery.js, core.js, createElement.js, rnothtmlwhite.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/event.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.977)
- **Top Global Matches:** file_cluster_4: 7.977, file_cluster_6: 8.302, file_cluster_12: 14.8
- **Magnitude:** 821.04 | **LOC:** 881 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove` **(Many-Argument Workhorses)** (Impact: 86.9)
    * *Intent:* // Detach an event or set of events from an element
  * `add` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `on` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `leverageNative` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* // Ensure the presence of an event listener that handles manually-triggered // synthetic events by i...
  * `dispatch` **(Defensive Guards)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 120 instances
* *State Mutation (weighted view):* 364
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 69`, `args: 38`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 124`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` core.js, nodeName.js, acceptData.js, dataPriv.js, documentElement.js, isIE.js, rcheckableType.js, rnothtmlwhite.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/effects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.587)
- **Top Global Matches:** file_cluster_6: 7.587, file_cluster_4: 9.838, file_cluster_12: 16.393
- **Magnitude:** 759.54 | **LOC:** 688 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defaultPrefilter` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `Animation` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `stop` **(Defensive Guards)** (Impact: 40.6)
  * `speed` **(Defensive Guards)** (Impact: 40.1)
  * `finish` **(Defensive Guards)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 72`, `args: 39`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 127`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` core.js, adjustCSS.js, cssCamelCase.js, showHide.js, cssExpand.js, isHiddenWithinTree.js, dataPriv.js, document.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/event.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.945)
- **Top Global Matches:** file_cluster_12: 8.945, file_cluster_10: 9.154, file_cluster_7: 10.761
- **Magnitude:** 734.68 | **LOC:** 3636 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (73.1%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (24.8%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handler` **(Defensive Guards)** (Impact: 6.0)
  * `handler` **(Defensive Guards)** (Impact: 6.0)
  * `handlerWithData` **(Defensive Guards)** (Impact: 6.0)
  * `addEventListener` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* // Support: Firefox 124+ // In Firefox, alert displayed just before blurring an element // dispatche...
  * `patchAddEventListener` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 101
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 167`, `args: 412`, `func_start: 70`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 340`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 4`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 21`
* *Defense:* `safety: 49`, `test: 663`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/deferred.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.725)
- **Top Global Matches:** file_cluster_10: 6.725, file_cluster_12: 9.332, file_cluster_11: 9.458
- **Magnitude:** 727.78 | **LOC:** 1146 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (47.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onFulfilled` **(Callbacks & Closures)** (Impact: 4.9)
  * `onFulfilled` **(Callbacks & Closures)** (Impact: 4.9)
  * `onRejected` **(Callbacks & Closures)** (Impact: 4.8)
  * `onRejected` **(Callbacks & Closures)** (Impact: 4.8)
  * `createDeferred` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 80 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 498
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 94`, `args: 192`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 155`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 98`
* *Defense:* `safety: 18`, `test: 208`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/manipulation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.968)
- **Top Global Matches:** file_cluster_12: 7.968, file_cluster_10: 9.664, file_cluster_7: 9.833
- **Magnitude:** 679.76 | **LOC:** 3227 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (74.1%), Guard Balance (formerly Safety Score) (46.1%), Complexity Load (formerly Cognitive Load) (25.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAppend` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `testAppendForObject` **(Many-Argument Workhorses)** (Impact: 11.7)
  * `testReplaceWith` **(Many-Argument Workhorses)** (Impact: 6.9)
  * `htmlPrefilter` **(Callbacks & Closures)** (Impact: 4.6)
  * `assertSpecialCharsSupport` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 458
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 239`, `args: 271`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 1`, `state_mutation: 372`, `fragile_debt: 7`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 18`
* *Defense:* `safety: 31`, `test: 784`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/effects.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_10: 6.477, file_cluster_12: 7.903, file_cluster_15: 9.575
- **Magnitude:** 578.62 | **LOC:** 2616 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (51.7%), Guard Balance (formerly Safety Score) (45.6%), Complexity Load (formerly Cognitive Load) (19.9%), Dead Code Surface (formerly Dead Code) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `progress` **(Callbacks & Closures)** (Impact: 7.5)
  * `step` **(Defensive Guards)** (Impact: 7.4)
  * `step` **(Defensive Guards)** (Impact: 7.3)
  * `progress` **(State Mutators)** (Impact: 6.5)
  * `step` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 155`, `args: 311`, `func_start: 79`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 221`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 7`, `duplicate_logic: 8`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 15`
* *Defense:* `safety: 64`, `test: 480`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/css.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.699)
- **Top Global Matches:** file_cluster_10: 7.699, file_cluster_12: 7.982, file_cluster_2: 9.813
- **Magnitude:** 428.7 | **LOC:** 1914 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Complexity Load (formerly Cognitive Load) (26.7%), Concurrency Surface (formerly Concurrency) (17.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add` **(Many-Argument Workhorses)** (Impact: 4.8)
  * `getUnits` **(State Mutators)** (Impact: 2.0)
  * `round` **(Callbacks & Closures)** (Impact: 1.9)
  * `hide` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 160`, `args: 95`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 2`, `state_mutation: 239`, `fragile_debt: 3`
* *Architecture:* `concurrency: 3`
* *Defense:* `safety: 20`, `test: 408`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.892)
- **Top Global Matches:** file_cluster_12: 7.892, file_cluster_10: 8.406, file_cluster_7: 8.971
- **Magnitude:** 403.9 | **LOC:** 1632 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.5%), Concurrency Surface (formerly Concurrency) (33.6%), Complexity Load (formerly Cognitive Load) (33.0%), Connectivity (formerly Api Exposure) (27.2%)
- **Documentation Coverage:** 96.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iframeDone` **(Callbacks & Closures)** (Impact: 3.8)
  * `callback` **(Callbacks & Closures)** (Impact: 3.8)
  * `callback` **(Callbacks & Closures)** (Impact: 3.2)
  * `Two` **(Callbacks & Closures)** (Impact: 1.9)
  * `callback` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 81`, `args: 129`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 1`, `state_mutation: 178`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 9`, `duplicate_logic: 10`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 6`
* *Defense:* `safety: 54`, `doc: 1`, `test: 475`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/selector.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.192)
- **Top Global Matches:** file_cluster_12: 8.192, file_cluster_7: 8.495, file_cluster_5: 10.332
- **Magnitude:** 401.58 | **LOC:** 2555 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.1%), Concurrency Surface (formerly Concurrency) (22.1%), Complexity Load (formerly Cognitive Load) (9.9%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertNoMatch` **(Defensive Guards)** (Impact: 12.7)
  * `testLang` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `mixCase` **(Callbacks & Closures)** (Impact: 4.7)
  * `getUniqueSortFixtures` **(I/O & Config Routines)** (Impact: 4.0)
  * `get` **(Callbacks & Closures)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 102`, `args: 93`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 118`, `high_risk_execution: 4`, `state_mutation: 159`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 4`
* *Defense:* `safety: 27`, `doc: 2`, `test: 882`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.951)
- **Top Global Matches:** file_cluster_6: 7.951, file_cluster_8: 9.959, file_cluster_4: 15.736
- **Magnitude:** 386.76 | **LOC:** 405 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `style` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* // Get and set the style property on a DOM Node
  * `boxModelAdjustment` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `getWidthOrHeight` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `css` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `set` **(Defensive Guards)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 53`, `args: 13`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 16`
* *Defense:* `safety: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` core.js, access.js, nodeName.js, adjustCSS.js, cssCamelCase.js, curCSS.js, finalPropName.js, isAutoPx.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/testinit.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.192)
- **Top Global Matches:** file_cluster_4: 8.192, file_cluster_10: 8.642, file_cluster_15: 9.386
- **Magnitude:** 326.3 | **LOC:** 447 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 2.705; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (62.5%), Connectivity (formerly Api Exposure) (44.7%), Complexity Load (formerly Cognitive Load) (36.8%)
- **Documentation Coverage:** 73.8095% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ajaxTest` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* // Ajax testing helper
  * `loadTests` **(I/O & Config Routines)** (Impact: 17.7)
  * `testIframe` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `callIfDefined` **(Defensive Guards)** (Impact: 11.0)
  * `loadDep` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* // Ensure load order (to preserve test numbers)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 36`, `args: 31`, `func_start: 20`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 53`, `planned_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 13`, `doc: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.705
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003268
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/deferred.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.736)
- **Top Global Matches:** file_cluster_6: 8.736, file_cluster_8: 11.764, file_cluster_4: 15.452
- **Magnitude:** 325.54 | **LOC:** 393 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Concurrency Surface (formerly Concurrency) (74.1%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Deferred` **(Defensive Guards)** (Impact: 60.1)
  * `then` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `resolve` **(Many-Argument Workhorses)** (Impact: 48.7)
  * `adoptValue` **(Defensive Guards)** (Impact: 17.1)
  * `mightThrow` **(I/O & Config Routines)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 29`, `args: 24`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 32`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core.js, slice.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.364)
- **Top Global Matches:** file_cluster_12: 8.364, file_cluster_4: 9.963, file_cluster_10: 10.024
- **Magnitude:** 315.26 | **LOC:** 420 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **14**; blast radius 59.084; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Connectivity (formerly Api Exposure) (85.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extend` **(Defensive Guards)** (Impact: 27.6)
  * `map` **(Many-Argument Workhorses)** (Impact: 15.5)
    * *Intent:* // arg is for internal usage only
  * `each` **(Defensive Guards)** (Impact: 13.1)
  * `text` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* // Retrieve the text value of an array of DOM nodes
  * `contains` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // Note: an element does not contain itself
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 79`, `args: 32`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 45`
* *Architecture:* `api: 16`, `import: 14`
* *Defense:* `safety: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.084
  * `Choke Point (Betweenness):` 0.01145 | `Ripple Effect (Closeness):` 0.200958
  * `Imports (Out-Degree: 14):` DOMEval.js, isArrayLike.js, ObjectFunctionString.js, arr.js, class2type.js, flat.js, fnToString.js, getProto.js...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `test/data/qunit-fixture.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.793)
- **Top Global Matches:** file_cluster_13: 5.793, file_cluster_2: 7.145, file_cluster_17: 7.333
- **Magnitude:** 282.68 | **LOC:** 310 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (19.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 105`, `args: 167`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 47`, `api: 262`
* *Defense:* `safety: 69`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/unit/attributes.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.383)
- **Top Global Matches:** file_cluster_12: 8.383, file_cluster_7: 8.922, file_cluster_5: 10.507
- **Magnitude:** 274.52 | **LOC:** 1901 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (42.4%), Concurrency Surface (formerly Concurrency) (13.1%), Complexity Load (formerly Cognitive Load) (7.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testToggleClass` **(Compute Cores)** (Impact: 8.4)
  * `testAddClass` **(Compute Cores)** (Impact: 7.4)
  * `testFalseSetter` **(Callbacks & Closures)** (Impact: 6.0)
  * `expectClasses` **(Parameter Forwarders)** (Impact: 4.3)
  * `testRemoveClass` **(Compute Cores)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 207`, `args: 122`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 136`, `fragile_debt: 13`
* *Architecture:* `concurrency: 2`
* *Defense:* `safety: 34`, `test: 549`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/manipulation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.551)
- **Top Global Matches:** file_cluster_12: 7.551, file_cluster_10: 8.75, file_cluster_15: 9.504
- **Magnitude:** 270.68 | **LOC:** 336 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clone` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `html` **(Defensive Guards)** (Impact: 18.9)
  * `remove` **(Defensive Guards)** (Impact: 17.0)
  * `cleanData` **(Compute Cores)** (Impact: 14.4)
  * `cloneCopyEvent` **(Compute Cores)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 57`, `args: 28`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 39`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` core.js, access.js, isAttached.js, nodeName.js, acceptData.js, dataPriv.js, dataUser.js, domManip.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/middleware-mockserver.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.601)
- **Top Global Matches:** file_cluster_10: 6.601, file_cluster_15: 7.867, file_cluster_2: 9.191
- **Magnitude:** 255.12 | **LOC:** 426 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.899; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Guard Balance (formerly Safety Score) (51.5%), Complexity Load (formerly Cognitive Load) (30.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.7%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonp` **(Defensive Guards)** (Impact: 21.2)
  * `script` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `json` **(State Mutators)** (Impact: 9.6)
  * `errorWithScript` **(Compute Cores)** (Impact: 9.3)
  * `xml` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 18`, `args: 51`, `func_start: 36`
* *Risk/State:* `state_mutation: 17`, `dead_code: 1`, `unreferenced_by_name: 23`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 14`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` multiparty, node:fs, node:url, raw-body
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/event/trigger.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.969)
- **Top Global Matches:** file_cluster_6: 7.969, file_cluster_8: 12.907, file_cluster_4: 14.049
- **Magnitude:** 249.56 | **LOC:** 193 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `trigger` **(Many-Argument Workhorses)** (Impact: 127.9)
  * `triggerHandler` **(Callbacks & Closures)** (Impact: 3.8)
  * `simulate` **(Callbacks & Closures)** (Impact: 2.6)
    * *Intent:* // Piggyback on a donor event to simulate a different one // Used only for `focus(in | out)` events
  * `trigger` **(Callbacks & Closures)** (Impact: 2.0)
  * `stopPropagationCallback` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 37`, `unreferenced_by_name: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` core.js, acceptData.js, dataPriv.js, document.js, hasOwn.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/data/mock.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.476)
- **Top Global Matches:** file_cluster_16: 6.476, file_cluster_15: 8.392, file_cluster_11: 8.626
- **Magnitude:** 220.8 | **LOC:** 328 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.899; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.2%), Connectivity (formerly Api Exposure) (30.6%), Complexity Load (formerly Cognitive Load) (21.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.7%)
- **Documentation Coverage:** 98.3051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `script` **(Stateful Encapsulated Methods)** (Impact: 12.7)
  * `json` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `jsonp` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `etag` **(Stateful Encapsulated Methods)** (Impact: 6.5)
  * `ims` **(Stateful Encapsulated Methods)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 49`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`
* *Architecture:* `io: 65`, `api: 25`, `import: 5`
* *Defense:* `safety: 20`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` -trusted-types-for 'script'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/callbacks.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.047)
- **Top Global Matches:** file_cluster_4: 8.047, file_cluster_10: 9.261, file_cluster_15: 10.212
- **Magnitude:** 216.28 | **LOC:** 231 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.8%), Complexity Load (formerly Cognitive Load) (93.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Callbacks` **(Compute Cores)** (Impact: 56.3)
    * *Intent:* * * Possible options: * * once: will ensure the callback list can only be fired once (like a Deferre...
  * `add` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* // Add a callback or a collection of callbacks to the list
  * `fire` **(I/O & Config Routines)** (Impact: 12.2)
    * *Intent:* // Fire callbacks
  * `add` **(Defensive Guards)** (Impact: 12.0)
  * `fireWith` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* // Call all callbacks with the given context and arguments
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 21`, `args: 18`, `func_start: 16`
* *Risk/State:* `state_mutation: 30`, `unreferenced_by_name: 7`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` core.js, toType.js, rnothtmlwhite.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/offset.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.654)
- **Top Global Matches:** file_cluster_9: 7.654, file_cluster_12: 9.142, file_cluster_10: 10.616
- **Magnitude:** 173.96 | **LOC:** 202 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.899; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.9%), Guard Balance (formerly Safety Score) (71.9%), Debt Markers (formerly Tech Debt) (14.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setOffset` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `fn[ method ]` **(Defensive Guards)** (Impact: 15.4)
  * `position` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* // position() relates an element's margin box to its offset parent's padding box // This corresponds...
  * `offset` **(Compute Cores)** (Impact: 8.8)
    * *Intent:* // offset() relates an element's border box to the document origin
  * `offsetParent` **(Callbacks & Closures)** (Impact: 4.5)
    * *Intent:* // This method will return documentElement in the following cases: // 1) For the element inside the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 25`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` core.js, access.js, documentElement.js, isWindow.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/data/trusted-html.html` (HTML) | Magnitude: 28.18 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 52, core_var_decl: 16, design_snake_case: 16, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/traversing.js` (JAVASCRIPT) | Magnitude: 133.1 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 126, structural_boundaries: 46, branch: 35, args: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/data/support/getComputedSupport.js` (JAVASCRIPT) | Magnitude: 16.64 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 10, branch: 3, state_mutation: 3, structural_boundaries: 2
- `test/bundler_smoke_tests/rollup-pure-esm.config.js` (JAVASCRIPT) | Magnitude: 16.3 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 9, structural_boundaries: 5, import: 3, dependency_injection: 3
- `src/var/ObjectFunctionString.js` (JAVASCRIPT) | Magnitude: 12.04 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 3, api: 1, reflection_metaprogramming: 1, import: 1
- `src/selector/selectorError.js` (JAVASCRIPT) | Magnitude: 2.68 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/browser-tests-beta.yml` -> Churn: **84.47%** | Cog Load: 5.6208% | Debt: 81.9164%
- `.github/workflows/browser-tests.yml` -> Churn: **77.77%** | Cog Load: 3.6275% | Debt: 99.8388%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/unit/css.js` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 428.7
- `test/unit/selector.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 401.58
- `test/middleware-mockserver.cjs` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 255.12
- `test/data/mock.php` -> **Apoorv Darshan** (100.0% isolated ownership) | Magnitude: 220.8
- `test/unit/data.js` -> **Michał Gołębiowski-Owczarek** (100.0% isolated ownership) | Magnitude: 119.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/core.js` -> **Severity: 1.145** (Bridge: 0.0115 * Flux: 100.0%)
- `src/data/Data.js` -> **Severity: 0.092** (Bridge: 0.0009 * Flux: 100.0%)
- `src/core/isArrayLike.js` -> **Severity: 0.064** (Bridge: 0.0013 * Flux: 50.0%)
- `src/core/DOMEval.js` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 99.9254%)
- `src/ajax.js` -> **Severity: 0.025** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/core.js` -> **Severity: 12.947** (Embedded: 0.201 * Error Risk: 64.425%)
- `test/data/iframeTest.js` -> **Severity: 7.364** (Embedded: 0.1438 * Error Risk: 51.214%)
- `src/core/DOMEval.js` -> **Severity: 6.313** (Embedded: 0.1079 * Error Risk: 58.4884%)
- `src/core/isArrayLike.js` -> **Severity: 4.707** (Embedded: 0.1079 * Error Risk: 43.6066%)
- `src/var/isWindow.js` -> **Severity: 3.887** (Embedded: 0.0766 * Error Risk: 50.7142%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/data/iframeTest.js` -> **Severity: 6617.2** (Blast Radius: 66.172 * Doc Risk: 100.0%)
- `src/core.js` -> **Severity: 5908.4** (Blast Radius: 59.084 * Doc Risk: 100.0%)
- `src/data/Data.js` -> **Severity: 939.1** (Blast Radius: 9.391 * Doc Risk: 100.0%)
- `src/core/toType.js` -> **Severity: 741.6** (Blast Radius: 7.416 * Doc Risk: 100.0%)
- `test/node_smoke_tests/module/lib/ensure_jquery.js` -> **Severity: 649.8** (Blast Radius: 6.498 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2634 call pairs -- scoped 9.6%, unique 0.0%, ambiguous 2.1%, external 88.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 2534 | 9.8% | 0.0% | 2.1% | 88.0% |
| php | 55 | 7.3% | 0.0% | 0.0% | 92.7% |
| html | 45 | 0.0% | 0.0% | 0.0% | 100.0% |

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
