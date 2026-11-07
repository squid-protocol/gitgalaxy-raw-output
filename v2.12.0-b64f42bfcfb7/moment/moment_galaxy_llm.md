# ARCHITECTURAL_BRIEF: moment
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/moment/moment.git` |
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
- **Scope:** 642 analyzed artifact(s), 294553 LOC.
- **Load-bearing artifact:** `src/moment.js` -- 327 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/lib/moment/prototype.js` -- pulls in 32 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `min/tests.js` at magnitude 50583.3 (structural weight, not risk).
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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 642 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 153 |
| Total LOC | 294553 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5693 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4954 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7453 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 621 | 292181 | 96.7% |
| MARKDOWN | 7 | 0 | 1.1% |
| JSON | 6 | 239 | 0.9% |
| TYPESCRIPT | 4 | 2056 | 0.6% |
| YAML | 2 | 40 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.2% |
| SHELL | 1 | 37 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 642 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 22%, Callbacks & Closures Files 22%, Large Core Modules (2) 21%, Declarative / Non-Code 13%, Data / Markup / Trivial 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 634 | 98.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 1.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 153*

**Composition by Extension & Reason:**
- `.js`: 141x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12060 LOC)
- `.nuspec`: 1x Excluded (Unsupported Extension: '.nuspec')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.7 | 14.9 | 10.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.9 | 36.7 | 46.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 91.1 | 6.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 58.5 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 84.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2 | 2 | 0 | `min/tests.js` |
| cleanup | 2 | 1 | 0 | `scripts/npm_prepublish.sh` |
| guards | 8014 | 342 | 12 | `min/tests.js` |
| danger | 2534 | 84 | 1 | `min/tests.js` |
| concurrency | 55 | 19 | 0 | `tasks/transpile.js` |
| connectivity | 595 | 285 | 1 | `moment.d.ts` |
| io | 25 | 5 | 0 | `tasks/transpile.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 2178 | 183 | 1 | `min/tests.js` |
| serialization | 17 | 5 | 0 | `min/tests.js` |
| regex | 4720 | 441 | 7 | `min/moment-with-locales.js` |
| events | 467 | 25 | 0 | `min/tests.js` |
| tests | 45984 | 194 | 110 | `min/tests.js` |
| docs | 75 | 12 | 0 | `moment.d.ts` |
| debt | 3234 | 37 | 0 | `min/tests.js` |
| mutation | 51134 | 548 | 93 | `min/tests.js` |
| dead_code | 907 | 275 | 4 | `min/tests.js` |
| credential | 2 | 1 | 0 | `.travis.yml` |
| threat | 332 | 6 | 0 | `min/tests.js` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7596**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tasks/transpile.js` (Hits: 11)
- `scripts/locales.js` (Hits: 9)
- `.travis.yml` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **moment.js** (`src/moment.js`) — 327 inbound connections
2. **qunit.js** (`src/test/qunit.js`) — 192 inbound connections
3. **moment.js** (`moment.js`) — 155 inbound connections
4. **qunit-locale.js** (`src/test/qunit-locale.js`) — 138 inbound connections
5. **format.js** (`src/lib/format/format.js`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **prototype.js** (`src/lib/moment/prototype.js`) — 32 outbound dependencies
2. **from-anything.js** (`src/lib/create/from-anything.js`) — 17 outbound dependencies
3. **month.js** (`src/lib/units/month.js`) — 15 outbound dependencies
4. **offset.js** (`src/lib/units/offset.js`) — 15 outbound dependencies
5. **prototype.js** (`src/lib/locale/prototype.js`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processRelativeTime` **(Many-Argument Workhorses)** (@ `locale/sl.js`) -> Impact: **225.5** | LOC: 83
  * *Intent:* //! moment.js locale configuration
- `processRelativeTime` **(Many-Argument Workhorses)** (@ `src/locale/sl.js`) -> Impact: **225.5** | LOC: 83
- `translate` **(Many-Argument Workhorses)** (@ `locale/is.js`) -> Impact: **115.6** | LOC: 75
- `translate` **(Many-Argument Workhorses)** (@ `src/locale/is.js`) -> Impact: **115.6** | LOC: 75
- `translate` **(Compute Cores)** (@ `locale/cs.js`) -> Impact: **114.5** | LOC: 53
- `translate` **(Compute Cores)** (@ `locale/sk.js`) -> Impact: **114.5** | LOC: 53
- `translate` **(Compute Cores)** (@ `src/locale/cs.js`) -> Impact: **114.5** | LOC: 53
- `translate` **(Compute Cores)** (@ `src/locale/sk.js`) -> Impact: **114.5** | LOC: 53
- `processRelativeTime$9` **(Defensive Guards)** (@ `min/locales.js`) -> Impact: **103.2** | LOC: 83
  * *Intent:* //! moment.js locale configuration
- `processRelativeTime$9` **(Defensive Guards)** (@ `min/moment-with-locales.js`) -> Impact: **103.2** | LOC: 83
  * *Intent:* //! moment.js locale configuration

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `min` | 3 | 60284.06 | 19.01% | 43.57% |
| `__monolith__` | 15 | 3862.16 | 6.74% | 15.06% |
| `meteor` | 5 | 3747.94 | 15.15% | 1.68% |
| `src/test/moment` | 52 | 2144.74 | 3.62% | 0.0% |
| `src/lib/units` | 21 | 1496.78 | 26.82% | 1.36% |
| `src/lib/moment` | 19 | 991.94 | 40.96% | 3.89% |
| `src/lib/create` | 12 | 875.82 | 55.37% | 21.48% |
| `src/lib/duration` | 13 | 664.14 | 39.27% | 0.0% |
| `src/lib/parse` | 2 | 436.77 | 35.51% | 0.0% |
| `src/lib/utils` | 27 | 348.18 | 20.22% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/query.js` -> **100.0%** Exposure
- `moment.d.ts` -> **100.0%** Exposure
- `ts3.1-typings/moment.d.ts` -> **100.0%** Exposure
- `benchmarks/isObjectEmpty.js` -> **99.9918%** Exposure
- `src/locale/gl.js` -> **99.7697%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `meteor/moment.js` -> **100.0%** Exposure
- `moment.js` -> **100.0%** Exposure
- `src/lib/create/from-anything.js` -> **100.0%** Exposure
- `src/lib/create/from-array.js` -> **100.0%** Exposure
- `src/lib/create/from-string-and-array.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `min/tests.js` -> **1** Orphaned Functions | **3002** Duplicates
- `moment.d.ts` -> **67** Orphaned Functions | **26** Duplicates
- `ts3.1-typings/moment.d.ts` -> **65** Orphaned Functions | **26** Duplicates
- `min/moment-with-locales.js` -> **2** Orphaned Functions | **29** Duplicates
- `min/locales.js` -> **0** Orphaned Functions | **29** Duplicates

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
- **Unknown Dependencies:** `25` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `min/tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.858)
- **Top Global Matches:** file_cluster_4: 8.858, file_cluster_12: 9.32, file_cluster_10: 9.605
- **Magnitude:** 50583.3 | **LOC:** 149293 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.569; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (48.5%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5593 instances
* *State Mutation (weighted view):* 26651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8012`, `structural_boundaries: 6674`, `args: 7871`, `func_start: 3097`
* *Risk/State:* `safety_bypasses: 1115`, `high_risk_execution: 1`, `state_mutation: 15465`, `dead_code: 74`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 3002`, `unreferenced_by_name: 1`
* *Architecture:* `import: 190`
* *Defense:* `safety: 4023`, `test: 26055`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `min/moment-with-locales.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.857)
- **Top Global Matches:** file_cluster_4: 8.857, file_cluster_15: 11.105, file_cluster_12: 11.172
- **Magnitude:** 6696.72 | **LOC:** 18473 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 99.389% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processRelativeTime$9` **(Defensive Guards)** (Impact: 103.2)
    * *Intent:* //! moment.js locale configuration
  * `relativeTimeMr` **(Many-Argument Workhorses)** (Impact: 69.0)
  * `translate$5` **(Compute Cores)** (Impact: 53.8)
  * `translate$9` **(Compute Cores)** (Impact: 52.6)
  * `translate$3` **(Defensive Guards)** (Impact: 47.0)
    * *Intent:* //! moment.js locale configuration
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 637 instances
* *State Mutation (weighted view):* 2490
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2276`, `structural_boundaries: 1815`, `args: 736`, `func_start: 664`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 1216`, `dead_code: 7`, `planned_debt: 12`, `duplicate_logic: 29`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 667`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `meteor/moment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_4: 6.975, file_cluster_12: 8.836, file_cluster_15: 10.493
- **Magnitude:** 3702.84 | **LOC:** 5689 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 96.4971% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createDuration` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `getSetOffset` **(Defensive Guards)** (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `checkOverflow` **(Defensive Guards)** (Impact: 38.9)
  * `configFromArray` **(Defensive Guards)** (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `isValid` **(Defensive Guards)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 501 instances
* *State Mutation (weighted view):* 1971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 923`, `structural_boundaries: 713`, `args: 346`, `func_start: 283`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 969`, `dead_code: 3`, `planned_debt: 10`
* *Architecture:* `api: 4`
* *Defense:* `safety: 222`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `moment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_4: 6.975, file_cluster_12: 8.836, file_cluster_15: 10.493
- **Magnitude:** 3702.84 | **LOC:** 5689 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **155** in-repo importer(s); blast radius 75.513; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 49.8024% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createDuration` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `getSetOffset` **(Defensive Guards)** (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `checkOverflow` **(Defensive Guards)** (Impact: 38.9)
  * `configFromArray` **(Defensive Guards)** (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `isValid` **(Defensive Guards)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 501 instances
* *State Mutation (weighted view):* 1971
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 923`, `structural_boundaries: 713`, `args: 346`, `func_start: 283`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 969`, `dead_code: 3`, `planned_debt: 10`
* *Architecture:* `api: 4`
* *Defense:* `safety: 222`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 75.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.24181
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 155):` (Excluded from Brief to save tokens)

### `min/locales.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.413)
- **Top Global Matches:** file_cluster_4: 9.413, file_cluster_15: 10.249, file_cluster_9: 10.628
- **Magnitude:** 3004.04 | **LOC:** 12801 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.6%), Mutation Surface (formerly State Flux) (32.8%), Debt Markers (formerly Tech Debt) (16.7%)
- **Documentation Coverage:** 99.1701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processRelativeTime$9` **(Defensive Guards)** (Impact: 103.2)
    * *Intent:* //! moment.js locale configuration
  * `relativeTimeMr` **(Many-Argument Workhorses)** (Impact: 69.0)
  * `translate$5` **(Compute Cores)** (Impact: 53.8)
  * `translate$9` **(Compute Cores)** (Impact: 52.6)
  * `translate$3` **(Defensive Guards)** (Impact: 47.0)
    * *Intent:* //! moment.js locale configuration
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1358`, `structural_boundaries: 1103`, `args: 394`, `func_start: 381`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 247`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 29`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 453`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/parse/regex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.086)
- **Top Global Matches:** file_cluster_2: 4.086, file_cluster_10: 4.452, file_cluster_17: 5.207
- **Magnitude:** 399.43 | **LOC:** 85 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **2**; blast radius 2.386; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Connectivity (formerly Api Exposure) (56.6%), Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (28.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.386
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.158649
  * `Imports (Out-Degree: 2):` has-own-prop, is-function
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/lib/units/day-of-week.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.077)
- **Top Global Matches:** file_cluster_6: 8.077, file_cluster_4: 8.206, file_cluster_12: 14.312
- **Magnitude:** 376.58 | **LOC:** 433 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 0.969; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleStrictParse` **(Defensive Guards)** (Impact: 53.6)
  * `localeWeekdaysParse` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `weekdaysRegex` **(Compute Cores)** (Impact: 13.7)
  * `weekdaysShortRegex` **(Compute Cores)** (Impact: 13.7)
  * `weekdaysMinRegex` **(Compute Cores)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 81`, `args: 24`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 65`
* *Architecture:* `api: 11`, `import: 10`
* *Defense:* `safety: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.969
  * `Choke Point (Betweenness):` 0.000476 | `Ripple Effect (Closeness):` 0.146182
  * `Imports (Out-Degree: 10):` parsing-flags, utc, format, get-set, regex, token, has-own-prop, index-of...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/units/month.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.554)
- **Top Global Matches:** file_cluster_4: 6.554, file_cluster_6: 10.776, file_cluster_9: 11.179
- **Magnitude:** 294.74 | **LOC:** 341 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 1.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `localeMonthsParse` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `handleStrictParse` **(Defensive Guards)** (Impact: 32.3)
  * `setMonth` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* // MOMENTS
  * `monthsShortRegex` **(Compute Cores)** (Impact: 13.7)
  * `monthsRegex` **(Compute Cores)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 66`, `args: 19`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `planned_debt: 2`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.57
  * `Choke Point (Betweenness):` 0.002149 | `Ripple Effect (Closeness):` 0.148109
  * `Imports (Out-Degree: 15):` parsing-flags, utc, format, get-set, regex, token, has-own-prop, hooks...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/lib/units/era.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.225)
- **Top Global Matches:** file_cluster_15: 6.225, file_cluster_9: 7.354, file_cluster_16: 8.283
- **Magnitude:** 235.06 | **LOC:** 294 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.672; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%), Guard Balance (formerly Safety Score) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `localeErasParse` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `localeEras` **(Defensive Guards)** (Impact: 15.2)
  * `getEraYear` **(I/O & Config Routines)** (Impact: 8.2)
  * `localeErasConvertYear` **(Defensive Guards)** (Impact: 7.3)
  * `getEraName` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 59`, `args: 17`, `func_start: 15`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.672
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.131145
  * `Imports (Out-Degree: 8):` parsing-flags, format, locales, regex, token, has-own-prop, hooks, constants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tasks/transpile.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.089)
- **Top Global Matches:** file_cluster_4: 10.089, file_cluster_6: 12.329, file_cluster_12: 12.357
- **Magnitude:** 220.86 | **LOC:** 363 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.569; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.6%), Concurrency Surface (formerly Concurrency) (85.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Callbacks & Closures)** (Impact: 50.6)
  * `transpile` **(Defensive Guards)** (Impact: 11.2)
  * `rollupBundle` **(Callbacks & Closures)** (Impact: 7.5)
  * `generateLocales` **(Defensive Guards)** (Impact: 7.5)
  * `transpileCode` **(Compute Cores)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 44`, `args: 42`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 23`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 2`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment-with-locales.custom.js, , moment, es6-promise, path, rollup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/units/offset.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.966)
- **Top Global Matches:** file_cluster_12: 8.966, file_cluster_4: 9.121, file_cluster_7: 11.155
- **Magnitude:** 203.3 | **LOC:** 250 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 4.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSetOffset` **(Defensive Guards)** (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `offsetFromString` **(Defensive Guards)** (Impact: 12.9)
  * `cloneWithOffset` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* // Return a moment from input, that is local/utc/zone equivalent to model.
  * `getSetZone` **(Defensive Guards)** (Impact: 7.6)
  * `isDaylightSavingTimeShifted` **(I/O & Config Routines)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 57`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 26`
* *Architecture:* `api: 12`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.165
  * `Choke Point (Betweenness):` 0.008023 | `Ripple Effect (Closeness):` 0.182907
  * `Imports (Out-Degree: 15):` from-anything, local, utc, create, format, add-subtract, constructor, regex...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib/create/from-string.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.166)
- **Top Global Matches:** file_cluster_4: 7.166, file_cluster_6: 7.408, file_cluster_12: 13.842
- **Magnitude:** 186.74 | **LOC:** 259 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 1.263; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configFromISO` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* // date from iso format
  * `configFromString` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* // date from 1) ASP.NET, 2) ISO, 3) RFC 2822 formats, or 4) optional fallback if parsing isn't stric...
  * `calculateOffset` **(Compute Cores)** (Impact: 10.7)
  * `configFromRFC2822` **(Compute Cores)** (Impact: 7.0)
    * *Intent:* // date and time from ref 2822 format
  * `checkWeekday` **(Defensive Guards)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 40`, `args: 9`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 34`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.263
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.118982
  * `Imports (Out-Degree: 7):` day-of-week, month, deprecate, hooks, date-from-array, from-string-and-format, parsing-flags
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/test/moment/create.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.415)
- **Top Global Matches:** file_cluster_12: 7.415, file_cluster_7: 7.557, file_cluster_10: 9.417
- **Magnitude:** 180.42 | **LOC:** 2920 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.8%), Dead Code Surface (formerly Dead Code) (7.5%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `offStr` **(Callbacks & Closures)** (Impact: 4.7)
  * `extend` **(Callbacks & Closures)** (Impact: 3.8)
  * `getVerifier` **(Callbacks & Closures)** (Impact: 3.4)
  * `pad` **(Callbacks & Closures)** (Impact: 3.1)
  * `parseTwoDigitYear` **(Callbacks & Closures)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 52`, `args: 92`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 56`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 25`, `test: 490`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` moment, each-own-prop, has-own-prop, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/create/from-array.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 18.57)
- **Top Global Matches:** file_cluster_3: 18.57, file_cluster_1: 35.334, file_cluster_8: 38.081
- **Magnitude:** 178.8 | **LOC:** 188 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 1.581; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configFromArray` **(Defensive Guards)** (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `dayOfYearFromWeekInfo` **(Compute Cores)** (Impact: 31.3)
  * `currentDateArray` **(Parameter Forwarders)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 15`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 34`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.581
  * `Choke Point (Betweenness):` 0.001308 | `Ripple Effect (Closeness):` 0.119248
  * `Imports (Out-Degree: 8):` constants, week-calendar-utils, year, defaults, hooks, date-from-array, local, parsing-flags
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib/duration/humanize.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.435)
- **Top Global Matches:** file_cluster_6: 8.435, file_cluster_8: 13.173, file_cluster_4: 14.549
- **Magnitude:** 165.16 | **LOC:** 115 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 5.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `relativeTime` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `humanize` **(Defensive Guards)** (Impact: 15.5)
  * `getSetRelativeTimeThreshold` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* // This function allows you to set a threshold for relative time strings
  * `substituteTimeAgo` **(Parameter Forwarders)** (Impact: 5.0)
    * *Intent:* // helper function for moment.fn.from, moment.fn.fromNow, and moment.duration.fn.humanize
  * `getSetRelativeTimeRounding` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* // This function allows you to set the rounding function for relative time strings
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 25`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.059
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.17386
  * `Imports (Out-Degree: 1):` create
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/lib/moment/start-end-of.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.152)
- **Top Global Matches:** file_cluster_8: 11.152, file_cluster_3: 13.818, file_cluster_6: 23.445
- **Magnitude:** 163.14 | **LOC:** 165 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.635; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.8%), Guard Balance (formerly Safety Score) (71.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `endOf` **(Compute Cores)** (Impact: 27.4)
  * `startOf` **(Compute Cores)** (Impact: 27.1)
  * `localStartOfDate` **(Compute Cores)** (Impact: 8.4)
  * `utcStartOfDate` **(Compute Cores)** (Impact: 8.4)
  * `mod` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* // actual modulo - handles negative numbers (for dates before 1970):
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 29`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.635
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.130461
  * `Imports (Out-Degree: 2):` aliases, hooks
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/test/moment/add_subtract.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.825)
- **Top Global Matches:** file_cluster_10: 4.825, file_cluster_2: 4.894, file_cluster_17: 6.407
- **Magnitude:** 156.94 | **LOC:** 546 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.9%), Complexity Load (formerly Cognitive Load) (15.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 18`, `args: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`, `fragile_debt: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `test: 175`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` moment, qunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/duration/create.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.418)
- **Top Global Matches:** file_cluster_8: 8.418, file_cluster_6: 9.97, file_cluster_4: 18.08
- **Magnitude:** 152.72 | **LOC:** 134 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 11.815; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createDuration` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `momentsDifference` **(Compute Cores)** (Impact: 9.5)
  * `parseIso` **(Compute Cores)** (Impact: 5.6)
  * `positiveMomentsDifference` **(Compute Cores)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.815
  * `Choke Point (Betweenness):` 0.004403 | `Ripple Effect (Closeness):` 0.183982
  * `Imports (Out-Degree: 9):` local, constants, offset, abs-round, has-own-prop, is-number, to-int, constructor...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/test/helpers/common-locale.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.894)
- **Top Global Matches:** file_cluster_8: 7.894, file_cluster_6: 17.688, file_cluster_3: 20.512
- **Magnitude:** 139.94 | **LOC:** 266 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (53.0%), Complexity Load (formerly Cognitive Load) (48.8%), Connectivity (formerly Api Exposure) (14.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defineCommonLocaleTests` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `tester` **(I/O & Config Routines)** (Impact: 6.2)
  * `tester` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 22`, `args: 14`, `func_start: 3`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 10`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.414
  * `Choke Point (Betweenness):` 0.001016 | `Ripple Effect (Closeness):` 0.108816
  * `Imports (Out-Degree: 3):` moment, qunit, each-own-prop
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib/moment/get-set.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 14.42)
- **Top Global Matches:** file_cluster_8: 14.42, file_cluster_3: 16.664, file_cluster_6: 25.091
- **Magnitude:** 139.5 | **LOC:** 118 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **5**; blast radius 1.55; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `get` **(Compute Cores)** (Impact: 36.1)
  * `stringSet` **(Defensive Guards)** (Impact: 9.5)
  * `makeGetSet` **(Callbacks & Closures)** (Impact: 5.7)
  * `stringGet` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* // MOMENTS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 38`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `dead_code: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.55
  * `Choke Point (Betweenness):` 0.001085 | `Ripple Effect (Closeness):` 0.153039
  * `Imports (Out-Degree: 5):` aliases, priorities, year, hooks, is-function
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/lib/create/from-anything.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.483)
- **Top Global Matches:** file_cluster_9: 8.483, file_cluster_15: 12.052, file_cluster_16: 12.57
- **Magnitude:** 133.04 | **LOC:** 118 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 11.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createLocalOrUTC` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `prepareConfig` **(Defensive Guards)** (Impact: 22.8)
  * `configFromInput` **(Defensive Guards)** (Impact: 19.5)
  * `createFromConfig` **(Compute Cores)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 5`, `func_start: 4`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 18`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.128
  * `Choke Point (Betweenness):` 0.0088 | `Ripple Effect (Closeness):` 0.149039
  * `Imports (Out-Degree: 17):` locales, constructor, hooks, is-array, is-date, is-number, is-object, is-object-empty...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ts3.1-typing-tests/moment-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.538)
- **Top Global Matches:** file_cluster_10: 6.538, file_cluster_15: 6.831, file_cluster_2: 7.663
- **Magnitude:** 122.78 | **LOC:** 550 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.569; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (60.8%), Guard Balance (formerly Safety Score) (52.4%), Complexity Load (formerly Cognitive Load) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `meridiem` **(Defensive Guards)** (Impact: 22.6)
  * `meridiem` **(Compute Cores)** (Impact: 22.6)
  * `ordinal` **(Compute Cores)** (Impact: 7.5)
  * `ordinal` **(Compute Cores)** (Impact: 7.4)
  * `months` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 77`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 28`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing-tests/moment-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.578)
- **Top Global Matches:** file_cluster_10: 6.578, file_cluster_15: 6.854, file_cluster_2: 7.696
- **Magnitude:** 120.82 | **LOC:** 558 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.569; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (56.5%), Guard Balance (formerly Safety Score) (52.2%), Complexity Load (formerly Cognitive Load) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `meridiem` **(Defensive Guards)** (Impact: 22.6)
  * `meridiem` **(Compute Cores)** (Impact: 22.6)
  * `ordinal` **(Compute Cores)** (Impact: 7.5)
  * `ordinal` **(Compute Cores)** (Impact: 7.4)
  * `months` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 77`, `args: 10`, `func_start: 11`
* *Risk/State:* `state_mutation: 28`, `dead_code: 5`, `planned_debt: 3`
* *Architecture:* `import: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.569
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` moment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib/create/from-string-and-format.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.535)
- **Top Global Matches:** file_cluster_8: 9.535, file_cluster_6: 11.149, file_cluster_4: 18.978
- **Magnitude:** 118.9 | **LOC:** 136 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 1.468; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `configFromStringAndFormat` **(Compute Cores)** (Impact: 31.3)
    * *Intent:* // date from string and format string
  * `meridiemFixWrap` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `ISO_8601` **(Callbacks & Closures)** (Impact: 1.1)
    * *Intent:* // constant that refers to the ISO standard
  * `RFC_2822` **(Callbacks & Closures)** (Impact: 1.1)
    * *Intent:* // constant that refers to the RFC 2822 form
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.468
  * `Choke Point (Betweenness):` 0.000171 | `Ripple Effect (Closeness):` 0.119048
  * `Imports (Out-Degree: 9):` format, regex, token, constants, hooks, check-overflow, from-array, from-string...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/lib/moment/prototype.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.795)
- **Top Global Matches:** file_cluster_10: 9.795, file_cluster_2: 10.081, file_cluster_17: 10.103
- **Magnitude:** 105.4 | **LOC:** 198 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 2.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.1%), Complexity Load (formerly Cognitive Load) (56.0%), Connectivity (formerly Api Exposure) (23.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `proto[Symbol.for` **(Callbacks & Closures)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 35`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`
* *Architecture:* `api: 2`, `import: 32`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.026287 | `Ripple Effect (Closeness):` 0.172994
  * `Imports (Out-Degree: 32):` day-of-month, day-of-week, day-of-year, era, hour, millisecond, minute, month...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/test/locale/sk.js` (JAVASCRIPT) | Magnitude: 0.15 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 575, test: 140, state_mutation: 79, core_var_decl: 57
- `src/test/locale/cs.js` (JAVASCRIPT) | Magnitude: 0.15 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 601, test: 143, state_mutation: 80, core_var_decl: 58
- `src/test/locale/fr.js` (JAVASCRIPT) | Magnitude: 0.09 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 419, test: 112, state_mutation: 55, core_var_decl: 42
- `src/test/moment/add_subtract.js` (JAVASCRIPT) | Magnitude: 156.94 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 460, test: 175, state_mutation: 132, core_var_decl: 24
- `src/test/locale/dv.js` (JAVASCRIPT) | Magnitude: 0.08 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 368, test: 70, state_mutation: 51, core_var_decl: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/test/moment/from_to.js` (JAVASCRIPT) | Magnitude: 29.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 128, test: 28, core_var_decl: 28, design_snake_case: 28
- `src/test/moment/format.js` (JAVASCRIPT) | Magnitude: 87.2 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 770, test: 206, core_var_decl: 58, state_mutation: 51
- `src/test/moment/days_in_month.js` (JAVASCRIPT) | Magnitude: 11.2 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 98, test: 26, structural_boundaries: 11, args: 8
- `src/test/moment/creation-data.js` (JAVASCRIPT) | Magnitude: 18.64 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, test: 13, core_var_decl: 6, design_snake_case: 6
- `Gruntfile.js` (JAVASCRIPT) | Magnitude: 22.94 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 235, structural_boundaries: 6, branch: 3, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/lib/locale/en.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 5, branch: 4, safety: 4
- `src/lib/utils/is-array.js` (JAVASCRIPT) | Magnitude: 4.22 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, branch: 2, structural_boundaries: 2, safety: 2
- `src/lib/utils/is-date.js` (JAVASCRIPT) | Magnitude: 4.22 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, branch: 2, structural_boundaries: 2, safety: 2
- `src/lib/utils/is-number.js` (JAVASCRIPT) | Magnitude: 4.22 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, safety: 3, branch: 2, structural_boundaries: 2
- `src/test/locale/mk.js` (JAVASCRIPT) | Magnitude: 0.1 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 405, test: 104, state_mutation: 49, core_var_decl: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tasks/nuget.js` (JAVASCRIPT) | Magnitude: 5.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 30, args: 3, closures: 3, func_start: 1
- `src/test/locale/et.js` (JAVASCRIPT) | Magnitude: 0.09 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 472, test: 120, state_mutation: 56, core_var_decl: 41
- `src/test/locale/br.js` (JAVASCRIPT) | Magnitude: 0.1 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 479, test: 116, state_mutation: 63, core_var_decl: 43
- `src/test/locale/mn.js` (JAVASCRIPT) | Magnitude: 0.1 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 494, test: 103, state_mutation: 60, core_var_decl: 41
- `src/lib/locale/base-config.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, import: 9, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/lib/units/day-of-week.js` (JAVASCRIPT) | Magnitude: 376.58 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 308, branch: 100, structural_boundaries: 81, state_mutation: 65

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/moment.js` -> **Severity: 7.736** (Bridge: 0.0774 * Flux: 99.9998%)
- `src/lib/moment/prototype.js` -> **Severity: 2.629** (Bridge: 0.0263 * Flux: 100.0%)
- `src/lib/moment/calendar.js` -> **Severity: 1.596** (Bridge: 0.016 * Flux: 100.0%)
- `src/lib/locale/locales.js` -> **Severity: 0.931** (Bridge: 0.0093 * Flux: 100.0%)
- `src/lib/create/from-anything.js` -> **Severity: 0.88** (Bridge: 0.0088 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/moment.js` -> **Severity: 33.065** (Embedded: 0.5102 * Error Risk: 64.8061%)
- `src/lib/moment/calendar.js` -> **Severity: 17.438** (Embedded: 0.2598 * Error Risk: 67.1347%)
- `moment.js` -> **Severity: 16.501** (Embedded: 0.2418 * Error Risk: 68.2408%)
- `src/lib/moment/constructor.js` -> **Severity: 15.671** (Embedded: 0.1941 * Error Risk: 80.7184%)
- `src/lib/utils/hooks.js` -> **Severity: 15.369** (Embedded: 0.303 * Error Risk: 50.7142%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/test/qunit.js` -> **Severity: 4107.8** (Blast Radius: 41.078 * Doc Risk: 100.0%)
- `moment.js` -> **Severity: 3760.729** (Blast Radius: 75.513 * Doc Risk: 49.8024%)
- `src/lib/utils/has-own-prop.js` -> **Severity: 2957.6** (Blast Radius: 29.576 * Doc Risk: 100.0%)
- `src/lib/utils/hooks.js` -> **Severity: 2690.0** (Blast Radius: 26.9 * Doc Risk: 100.0%)
- `src/test/helpers/deprecation-handler.js` -> **Severity: 2287.0** (Blast Radius: 22.87 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 38 literal sites + 5 sites through wrappers = 43

- `handleBody` (function, debug_prints, primitive): 3 call sites in 1 files -- `scripts/locales.js`
- `handleCommenters` (function, debug_prints, primitive): 2 call sites in 1 files -- `scripts/locales.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14620 call pairs -- scoped 18.5%, unique 0.0%, ambiguous 0.7%, external 80.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 14599 | 18.6% | 0.0% | 0.7% | 80.7% |
| typescript | 16 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
