# ARCHITECTURAL_BRIEF: bootstrap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/twbs/bootstrap.git` |
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
- **Scope:** 199 analyzed artifact(s), 26660 LOC.
- **Load-bearing artifact:** `js/src/util/index.js` -- 31 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scss/bootstrap.scss` -- pulls in 40 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `js/tests/unit/dropdown.spec.js` at magnitude 588.58 (structural weight, not risk).
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
| Total Artifacts | 790 |
| Analyzed Artifacts (Scanned) | 199 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 591 |
| Total LOC | 26660 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 25.2% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2767 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3648 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7143 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSS | 95 | 7749 | 47.7% |
| JAVASCRIPT | 63 | 17353 | 31.7% |
| YAML | 22 | 706 | 11.1% |
| MARKDOWN | 8 | 0 | 4.0% |
| HTML | 8 | 820 | 4.0% |
| PLAINTEXT | 2 | 0 | 1.0% |
| JSON | 1 | 32 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 199 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 39%, Data / Markup / Trivial 30%, Callbacks & Closures Files 10%, Large Core Modules (3) 8%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 189 | 95.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 591*

**Composition by Extension & Reason:**
- `.png`: 111x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.astro`: 104x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 63, Signals: 0), 1x Zero-Density Threshold (LOC: 57, Signals: 0)
- `.ts`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 20135 LOC)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (Saturation: Line 41 exceeds 500 chars), 1x Excluded (Saturation: Line 31 exceeds 500 chars), 1x Excluded (Saturation: Line 32 exceeds 500 chars)
- `.svg`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 58.2 | 6.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.4 | 20.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.1 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.4 | 1.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 81.7 | 7.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 8.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 60.5 | 3.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 20 | 14 | 0 | `js/tests/unit/dom/selector-engine.spec.js` |
| cleanup | 62 | 27 | 1 | `js/tests/unit/tooltip.spec.js` |
| guards | 435 | 83 | 5 | `js/src/dropdown.js` |
| danger | 844 | 50 | 6 | `js/tests/unit/dropdown.spec.js` |
| concurrency | 602 | 21 | 2 | `js/tests/unit/dropdown.spec.js` |
| connectivity | 222 | 63 | 4 | `js/tests/visual/modal.html` |
| io | 122 | 12 | 0 | `js/tests/visual/dropdown.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 138 | 21 | 1 | `js/tests/unit/dropdown.spec.js` |
| serialization | 2 | 2 | 0 | `js/src/dom/manipulator.js` |
| regex | 19 | 10 | 0 | `js/src/util/index.js` |
| events | 932 | 52 | 11 | `js/tests/unit/dropdown.spec.js` |
| tests | 2688 | 27 | 37 | `js/tests/unit/dropdown.spec.js` |
| docs | 163 | 56 | 3 | `js/tests/visual/modal.html` |
| debt | 79 | 38 | 2 | `js/tests/visual/modal.html` |
| mutation | 5685 | 79 | 66 | `js/tests/unit/dropdown.spec.js` |
| dead_code | 16 | 14 | 0 | `js/tests/karma.conf.js` |
| credential | 6 | 1 | 0 | `config.yml` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 1 | 0 | `scss/_functions.scss` |
| ui | 283 | 53 | 4 | `js/tests/unit/tooltip.spec.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `js/tests/visual/dropdown.html` (Hits: 62)
- `js/tests/visual/modal.html` (Hits: 22)
- `js/tests/visual/tooltip.html` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`js/src/util/index.js`) — 31 inbound connections
2. **event-handler.js** (`js/src/dom/event-handler.js`) — 28 inbound connections
3. **fixture.js** (`js/tests/helpers/fixture.js`) — 25 inbound connections
4. **base-component.js** (`js/src/base-component.js`) — 13 inbound connections
5. **selector-engine.js** (`js/src/dom/selector-engine.js`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bootstrap.scss** (`scss/bootstrap.scss`) — 40 outbound dependencies
2. **_mixins.scss** (`scss/_mixins.scss`) — 25 outbound dependencies
3. **bootstrap-grid.scss** (`scss/bootstrap-grid.scss`) — 14 outbound dependencies
4. **index.esm.js** (`js/index.esm.js`) — 12 outbound dependencies
5. **index.umd.js** (`js/index.umd.js`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addHandler` **(Many-Argument Workhorses)** (@ `js/src/dom/event-handler.js`) -> Impact: **34.0** | LOC: 44
- `off` **(Defensive Guards)** (@ `js/src/dom/event-handler.js`) -> Impact: **28.6** | LOC: 35
- `clearMenus` **(Defensive Guards)** (@ `js/src/dropdown.js`) -> Impact: **25.9** | LOC: 37
- `sanitizeHtml` **(Many-Argument Workhorses)** (@ `js/src/util/sanitizer.js`) -> Impact: **21.6** | LOC: 33
- `_slide` **(Many-Argument Workhorses)** (@ `js/src/carousel.js`) -> Impact: **20.9** | LOC: 71
- `trigger` **(Many-Argument Workhorses)** (@ `js/src/dom/event-handler.js`) -> Impact: **19.9** | LOC: 39
- `_onInteraction` **(Compute Cores)** (@ `js/src/toast.js`) -> Impact: **18.9** | LOC: 31
- `getSelector` **(Defensive Guards)** (@ `js/src/dom/selector-engine.js`) -> Impact: **16.8** | LOC: 24
- `dataApiKeydownHandler` **(Compute Cores)** (@ `js/src/dropdown.js`) -> Impact: **16.1** | LOC: 40
- `parseSelector` **(Defensive Guards)** (@ `js/src/util/index.js`) -> Impact: **15.5** | LOC: 83
  * *Intent:* /** * Properly escape IDs selectors to handle weird IDs */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js/tests/unit` | 13 | 2888.2 | 15.58% | 0.0% |
| `js/src` | 13 | 1380.02 | 20.27% | 5.22% |
| `js/tests/visual` | 8 | 612.94 | 0.79% | 0.0% |
| `js/src/util` | 9 | 475.66 | 16.78% | 4.05% |
| `js/src/dom` | 4 | 386.5 | 37.55% | 5.53% |
| `js/tests/unit/util` | 9 | 319.72 | 10.43% | 0.0% |
| `js/tests/unit/dom` | 4 | 270.92 | 0.0% | 0.0% |
| `.github/workflows` | 15 | 180.38 | 3.07% | 4.15% |
| `js/tests` | 3 | 89.92 | 7.49% | 0.0% |
| `__monolith__` | 7 | 59.64 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.1491%** Exposure
- `.github/release-drafter.yml` -> **92.9873%** Exposure
- `.github/workflows/issue-labeled.yml` -> **62.2459%** Exposure
- `scss/helpers/_color-bg.scss` -> **62.2459%** Exposure
- `scss/helpers/_colored-links.scss` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `js/src/util/backdrop.js` -> **100.0%** Exposure
- `js/src/util/focustrap.js` -> **100.0%** Exposure
- `js/src/util/index.js` -> **100.0%** Exposure
- `js/src/util/swipe.js` -> **100.0%** Exposure
- `js/src/util/template-factory.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/tests/unit/scrollspy.spec.js` -> **1** Orphaned Functions | **3** Duplicates
- `js/tests/unit/tooltip.spec.js` -> **1** Orphaned Functions | **3** Duplicates
- `js/tests/unit/dom/event-handler.spec.js` -> **1** Orphaned Functions | **2** Duplicates
- `js/tests/unit/modal.spec.js` -> **0** Orphaned Functions | **3** Duplicates
- `js/tests/unit/util/backdrop.spec.js` -> **1** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `config.yml` -> **99.9462%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `169` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `js/tests/unit/dropdown.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_10: 6.747, file_cluster_11: 9.383, file_cluster_12: 9.451
- **Magnitude:** 588.58 | **LOC:** 2437 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (39.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectDropdownToBeOpened` **(Callbacks & Closures)** (Impact: 5.1)
  * `test` **(Callbacks & Closures)** (Impact: 2.1)
  * `onFirstUpdate` **(State Mutators)** (Impact: 1.8)
  * `expectDropdownToBeOpened` **(Callbacks & Closures)** (Impact: 1.8)
  * `expectDropdownToBeOpened` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 65 instances
* *High Risk Execution (weighted view):* 81
* *Concurrency (weighted view):* 412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 704`, `args: 290`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 83`, `state_mutation: 119`, `planned_debt: 1`
* *Architecture:* `concurrency: 87`, `import: 4`
* *Defense:* `safety: 2`, `test: 296`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, dropdown.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/tooltip.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.202)
- **Top Global Matches:** file_cluster_10: 7.202, file_cluster_12: 9.39, file_cluster_11: 10.021
- **Magnitude:** 404.08 | **LOC:** 1586 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (69.3%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onFirstUpdate` **(State Mutators)** (Impact: 1.8)
  * `firstCallback` **(Callbacks & Closures)** (Impact: 1.8)
  * `title` **(Parameter Forwarders)** (Impact: 1.6)
  * `tip` **(Callbacks & Closures)** (Impact: 1.4)
  * `tip` **(Callbacks & Closures)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 80
* *Concurrency (weighted view):* 264
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 313`, `args: 234`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 84`, `state_mutation: 98`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 59`, `import: 4`
* *Defense:* `safety: 4`, `test: 273`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, tooltip.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/modal.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.999)
- **Top Global Matches:** file_cluster_10: 5.999, file_cluster_2: 9.646, file_cluster_13: 9.901
- **Magnitude:** 366.8 | **LOC:** 1330 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (66.9%), Complexity Load (formerly Cognitive Load) (34.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shownCallback` **(Callbacks & Closures)** (Impact: 1.3)
  * `shownCallback` **(Callbacks & Closures)** (Impact: 1.3)
  * `shownCallback` **(Callbacks & Closures)** (Impact: 1.3)
  * `shownCallback` **(Callbacks & Closures)** (Impact: 1.3)
  * `shownCallback` **(Callbacks & Closures)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 250
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 373`, `args: 205`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 57`, `state_mutation: 79`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 55`, `import: 4`
* *Defense:* `test: 184`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` event-handler.js, modal.js, scrollbar.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/carousel.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.267)
- **Top Global Matches:** file_cluster_10: 6.267, file_cluster_12: 8.469, file_cluster_2: 9.447
- **Magnitude:** 314.68 | **LOC:** 1573 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (31.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getActiveId` **(Callbacks & Closures)** (Impact: 5.2)
  * `onSlide` **(Callbacks & Closures)** (Impact: 2.0)
  * `onSlid` **(Callbacks & Closures)** (Impact: 2.0)
  * `onSlide2` **(Callbacks & Closures)** (Impact: 1.6)
  * `onSlid2` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 58
* *Concurrency (weighted view):* 166
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 388`, `args: 143`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 63`, `state_mutation: 100`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 36`, `import: 5`
* *Defense:* `safety: 5`, `test: 215`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` carousel.js, event-handler.js, index.js, swipe.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.519)
- **Top Global Matches:** file_cluster_15: 6.519, file_cluster_11: 6.973, file_cluster_10: 7.321
- **Magnitude:** 286.76 | **LOC:** 634 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 6.975; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (55.5%), Connectivity (formerly Api Exposure) (49.1%), Complexity Load (formerly Cognitive Load) (37.2%)
- **Documentation Coverage:** 98.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `show` **(I/O & Config Routines)** (Impact: 13.8)
  * `_setListeners` **(Defensive Guards)** (Impact: 13.1)
  * `hide` **(I/O & Config Routines)** (Impact: 9.1)
  * `_configAfterMerge` **(Defensive Guards)** (Impact: 8.1)
  * `_getConfig` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 62`, `args: 49`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 28`, `doc: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.975
  * `Choke Point (Betweenness):` 0.000731 | `Ripple Effect (Closeness):` 0.02073
  * `Imports (Out-Degree: 7):` base-component.js, event-handler.js, manipulator.js, index.js, sanitizer.js, template-factory.js, core
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `js/src/dom/event-handler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.066)
- **Top Global Matches:** file_cluster_15: 6.066, file_cluster_11: 8.157, file_cluster_16: 8.317
- **Magnitude:** 234.32 | **LOC:** 318 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **1**; blast radius 36.202; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (53.1%), Connectivity (formerly Api Exposure) (52.0%), Complexity Load (formerly Cognitive Load) (44.6%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addHandler` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `off` **(Defensive Guards)** (Impact: 28.6)
  * `trigger` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `bootstrapDelegationHandler` **(Defensive Guards)** (Impact: 13.1)
  * `handler` **(Defensive Guards)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 35`, `args: 21`, `func_start: 19`
* *Risk/State:* `state_mutation: 19`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 19`, `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.202
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.150192
  * `Imports (Out-Degree: 1):` index.js
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `js/tests/unit/tab.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.024)
- **Top Global Matches:** file_cluster_10: 5.024, file_cluster_2: 8.502, file_cluster_13: 8.715
- **Magnitude:** 220.32 | **LOC:** 1253 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (62.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectDone` **(Callbacks & Closures)** (Impact: 1.3)
  * `expectDone` **(Callbacks & Closures)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Concurrency (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 367`, `args: 123`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 46`, `state_mutation: 69`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 28`, `import: 2`
* *Defense:* `test: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tab.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/offcanvas.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.989)
- **Top Global Matches:** file_cluster_10: 5.989, file_cluster_2: 9.57, file_cluster_13: 9.845
- **Magnitude:** 219.56 | **LOC:** 915 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectEnd` **(Callbacks & Closures)** (Impact: 1.3)
  * `expectEnd` **(Callbacks & Closures)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Concurrency (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 211`, `args: 132`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 47`, `state_mutation: 67`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 26`, `import: 5`
* *Defense:* `test: 165`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` event-handler.js, offcanvas.js, index.js, scrollbar.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/collapse.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.875)
- **Top Global Matches:** file_cluster_10: 5.875, file_cluster_2: 8.985, file_cluster_13: 9.268
- **Magnitude:** 217.34 | **LOC:** 1063 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (60.9%), Complexity Load (formerly Cognitive Load) (18.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `target2Shown` **(Callbacks & Closures)** (Impact: 2.9)
  * `el` **(Callbacks & Closures)** (Impact: 2.7)
  * `handlerNestedCollapseOne` **(Callbacks & Closures)** (Impact: 1.8)
  * `firstTest` **(I/O & Config Routines)** (Impact: 1.4)
  * `secondTest` **(State Mutators)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 39
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 245`, `args: 123`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 40`, `state_mutation: 54`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 22`, `import: 3`
* *Defense:* `safety: 1`, `test: 182`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collapse.js, event-handler.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/carousel.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.713)
- **Top Global Matches:** file_cluster_15: 6.713, file_cluster_10: 6.849, file_cluster_11: 7.334
- **Magnitude:** 183.5 | **LOC:** 475 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 4.668; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.5%), Concurrency Surface (formerly Concurrency) (66.1%), Guard Balance (formerly Safety Score) (50.7%), Connectivity (formerly Api Exposure) (40.3%)
- **Documentation Coverage:** 97.2973% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_slide` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `to` **(Defensive Guards)** (Impact: 9.5)
  * `jQueryInterface` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* // Static
  * `_directionToOrder` **(Defensive Guards)** (Impact: 6.0)
  * `_orderToDirection` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 56`, `args: 43`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 17`, `doc: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.668
  * `Choke Point (Betweenness):` 0.000191 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 6):` base-component.js, event-handler.js, manipulator.js, selector-engine.js, index.js, swipe.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/dropdown.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.618)
- **Top Global Matches:** file_cluster_4: 7.618, file_cluster_15: 8.396, file_cluster_11: 8.662
- **Magnitude:** 172.18 | **LOC:** 456 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 4.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.2%), Guard Balance (formerly Safety Score) (46.6%), Connectivity (formerly Api Exposure) (40.6%), Complexity Load (formerly Cognitive Load) (20.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearMenus` **(Defensive Guards)** (Impact: 25.9)
  * `dataApiKeydownHandler` **(Compute Cores)** (Impact: 16.1)
  * `_getPlacement` **(I/O & Config Routines)** (Impact: 9.4)
  * `show` **(I/O & Config Routines)** (Impact: 8.7)
  * `_completeHide` **(Compute Cores)** (Impact: 8.3)
    * *Intent:* // Private
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 47`, `args: 26`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 31`, `doc: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.82
  * `Choke Point (Betweenness):` 0.000166 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 5):` base-component.js, event-handler.js, manipulator.js, selector-engine.js, index.js, core
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/unit/scrollspy.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.936)
- **Top Global Matches:** file_cluster_10: 5.936, file_cluster_15: 8.549, file_cluster_2: 8.838
- **Magnitude:** 170.9 | **LOC:** 981 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.4%), Guard Balance (formerly Safety Score) (63.8%), Complexity Load (formerly Cognitive Load) (18.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testElementIsActiveAfterScroll` **(Callbacks & Closures)** (Impact: 5.4)
  * `expectToBeCloseToArray` **(Callbacks & Closures)** (Impact: 3.8)
    * *Intent:* // See https://stackoverflow.com/a/45592926
  * `getElementScrollSpy` **(Parameter Forwarders)** (Impact: 3.1)
  * `onScroll` **(Callbacks & Closures)** (Impact: 2.5)
  * `onScrollStop` **(Callbacks & Closures)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 64
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 221`, `args: 94`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 37`, `state_mutation: 55`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 14`, `import: 3`
* *Defense:* `safety: 2`, `test: 122`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, scrollspy.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/visual/dropdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.559)
- **Top Global Matches:** file_cluster_13: 5.559, file_cluster_2: 7.319, file_cluster_17: 8.104
- **Magnitude:** 169.33 | **LOC:** 206 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.559; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 75`, `args: 38`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 62`, `api: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.min.css, bootstrap.bundle.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/dom/event-handler.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.826)
- **Top Global Matches:** file_cluster_10: 6.826, file_cluster_11: 9.523, file_cluster_13: 10.125
- **Magnitude:** 153.34 | **LOC:** 481 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `moveMouse` **(Callbacks & Closures)** (Impact: 2.3)
  * `oneListener` **(State Mutators)** (Impact: 1.1)
  * `oneListener` **(State Mutators)** (Impact: 1.1)
  * `handler` **(Callbacks & Closures)** (Impact: 1.1)
  * `handler` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Concurrency (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 108`, `args: 73`, `func_start: 7`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 32`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 25`, `import: 3`
* *Defense:* `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, index.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/tests/unit/toast.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_10: 7.431, file_cluster_12: 9.089, file_cluster_7: 10.427
- **Magnitude:** 151.68 | **LOC:** 673 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expected` **(Callbacks & Closures)** (Impact: 1.6)
  * `assertDone` **(Callbacks & Closures)** (Impact: 1.3)
  * `assertDone` **(Callbacks & Closures)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Concurrency (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 154`, `args: 97`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 28`, `state_mutation: 39`
* *Architecture:* `concurrency: 23`, `import: 2`
* *Defense:* `test: 94`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` toast.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/scrollspy.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.091)
- **Top Global Matches:** file_cluster_15: 6.091, file_cluster_11: 6.542, file_cluster_10: 7.295
- **Magnitude:** 137.98 | **LOC:** 297 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 5.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.0%), Connectivity (formerly Api Exposure) (36.1%), Complexity Load (formerly Cognitive Load) (31.9%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_observerCallback` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* // The logic of selection
  * `jQueryInterface` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* // Static
  * `_activateParents` **(Compute Cores)** (Impact: 6.5)
  * `_configAfterMerge` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* // Private
  * `_maybeEnableSmoothScroll` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 30`, `args: 22`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `planned_debt: 4`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 8`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.072
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/modal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.562)
- **Top Global Matches:** file_cluster_15: 6.562, file_cluster_10: 6.843, file_cluster_11: 7.106
- **Magnitude:** 131.66 | **LOC:** 379 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 4.82; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (55.5%), Connectivity (formerly Api Exposure) (38.5%), Complexity Load (formerly Cognitive Load) (34.2%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_addEventListeners` **(Defensive Guards)** (Impact: 10.9)
  * `_adjustDialog` **(I/O & Config Routines)** (Impact: 7.8)
    * *Intent:* /** * The following methods are used to handle overflowing modals */
  * `_showElement` **(Compute Cores)** (Impact: 7.4)
  * `show` **(Compute Cores)** (Impact: 6.9)
  * `_triggerBackdropTransition` **(Callbacks & Closures)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 45`, `args: 33`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 9`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.82
  * `Choke Point (Betweenness):` 0.000282 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 8):` base-component.js, event-handler.js, selector-engine.js, backdrop.js, component-functions.js, focustrap.js, index.js, scrollbar.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/unit/popover.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.748)
- **Top Global Matches:** file_cluster_10: 8.748, file_cluster_12: 8.938, file_cluster_7: 10.453
- **Magnitude:** 131.36 | **LOC:** 512 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.559; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (30.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `title` **(Parameter Forwarders)** (Impact: 1.6)
  * `content` **(Parameter Forwarders)** (Impact: 1.6)
  * `title` **(Callbacks & Closures)** (Impact: 1.1)
  * `content` **(Callbacks & Closures)** (Impact: 1.1)
  * `title` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 116`, `args: 80`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 25`, `state_mutation: 38`
* *Architecture:* `concurrency: 12`, `import: 3`
* *Defense:* `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` event-handler.js, popover.js, fixture.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/util/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.092)
- **Top Global Matches:** file_cluster_10: 7.092, file_cluster_15: 8.872, file_cluster_9: 9.151
- **Magnitude:** 127.14 | **LOC:** 307 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); blast radius 93.624; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (43.1%), Connectivity (formerly Api Exposure) (32.5%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 68.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseSelector` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* /** * Properly escape IDs selectors to handle weird IDs */
  * `getNextActiveElement` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* /** * Return the previous/next element of a list. * */
  * `isVisible` **(Defensive Guards)** (Impact: 12.6)
  * `findShadowRoot` **(Defensive Guards)** (Impact: 9.6)
  * `isDisabled` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 63`, `args: 25`, `func_start: 21`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 2`, `concurrency: 1`
* *Defense:* `safety: 29`, `doc: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.177683
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `js/src/collapse.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.206)
- **Top Global Matches:** file_cluster_15: 6.206, file_cluster_11: 6.92, file_cluster_10: 7.451
- **Magnitude:** 112.64 | **LOC:** 298 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 5.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Guard Balance (formerly Safety Score) (53.4%), Connectivity (formerly Api Exposure) (36.1%), Complexity Load (formerly Cognitive Load) (23.3%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 11.8)
  * `show` **(I/O & Config Routines)** (Impact: 10.7)
  * `hide` **(I/O & Config Routines)** (Impact: 9.0)
  * `jQueryInterface` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* // Static
  * `_addAriaAndCollapsedClass` **(Compute Cores)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`, `args: 22`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 11`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.072
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/tab.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_15: 6.022, file_cluster_10: 6.78, file_cluster_11: 6.935
- **Magnitude:** 108.08 | **LOC:** 316 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 5.576; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.4%), Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (24.4%), Debt Markers (formerly Tech Debt) (11.6%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_keydown` **(Defensive Guards)** (Impact: 9.6)
  * `jQueryInterface` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* // Static
  * `show` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* // Public
  * `_activate` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* // Private
  * `_deactivate` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 35`, `args: 26`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.576
  * `Choke Point (Betweenness):` 0.000199 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, selector-engine.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/src/toast.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.473)
- **Top Global Matches:** file_cluster_15: 6.473, file_cluster_11: 6.497, file_cluster_10: 6.774
- **Magnitude:** 86.86 | **LOC:** 225 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 5.576; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Concurrency Surface (formerly Concurrency) (66.7%), Guard Balance (formerly Safety Score) (53.3%), Connectivity (formerly Api Exposure) (37.9%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_onInteraction` **(Compute Cores)** (Impact: 18.9)
  * `jQueryInterface` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* // Static
  * `_maybeScheduleHide` **(Callbacks & Closures)** (Impact: 4.7)
    * *Intent:* // Private
  * `show` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* // Public
  * `hide` **(Callbacks & Closures)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 31`, `args: 21`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.576
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 4):` base-component.js, event-handler.js, component-functions.js, index.js
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `js/tests/visual/carousel.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.851)
- **Top Global Matches:** file_cluster_13: 5.851, file_cluster_10: 6.771, file_cluster_2: 7.478
- **Magnitude:** 84.68 | **LOC:** 66 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.559; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.8%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `args: 24`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 8`, `api: 2`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.min.css, bootstrap.bundle.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/src/dom/selector-engine.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.171)
- **Top Global Matches:** file_cluster_15: 5.171, file_cluster_16: 7.861, file_cluster_10: 7.989
- **Magnitude:** 81.18 | **LOC:** 127 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **1**; blast radius 19.711; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Connectivity (formerly Api Exposure) (72.5%), Complexity Load (formerly Cognitive Load) (58.2%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSelector` **(Defensive Guards)** (Impact: 16.8)
  * `prev` **(Compute Cores)** (Impact: 5.8)
  * `next` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* // TODO: this is now unused; remove later along with prev()
  * `getSelectorFromElement` **(Compute Cores)** (Impact: 4.7)
  * `parents` **(Parameter Forwarders)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 27`, `args: 15`, `func_start: 11`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.711
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.095227
  * `Imports (Out-Degree: 1):` index.js
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `js/tests/visual/toast.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.678)
- **Top Global Matches:** file_cluster_13: 6.678, file_cluster_10: 7.283, file_cluster_2: 8.218
- **Magnitude:** 80.67 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.559; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (9.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 22`, `args: 17`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.559
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bootstrap.min.css, bootstrap.bundle.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `scss/mixins/_clearfix.scss` (CSS) | Magnitude: 0.68 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `js/src/util/template-factory.js` (JAVASCRIPT) | Magnitude: 67.54 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 25, args: 15, func_start: 14
- `js/src/util/config.js` (JAVASCRIPT) | Magnitude: 28.16 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 9, branch: 8, args: 7
- `js/tests/unit/util/component-functions.spec.js` (JAVASCRIPT) | Magnitude: 9.96 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 76, core_var_decl: 25, structural_boundaries: 22, design_snake_case: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `js/tests/visual/tooltip.html` (HTML) | Magnitude: 13.68 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 116, core_var_decl: 37, design_snake_case: 33, args: 28
- `js/tests/visual/modal.html` (HTML) | Magnitude: 58.98 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 236, core_var_decl: 90, decorators: 88, structural_boundaries: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `js/src/offcanvas.js` (JAVASCRIPT) | Magnitude: 73.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 38, core_var_decl: 33, branch: 26
- `js/src/toast.js` (JAVASCRIPT) | Magnitude: 86.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 31, core_var_decl: 27, args: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/codeql.yml` (YAML) | Magnitude: 16.76 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 5, import: 4, immutability_locks: 4
- `.github/workflows/cspell.yml` (YAML) | Magnitude: 17.58 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, args: 5, structural_boundaries: 3, import: 2
- `.github/workflows/calibreapp-image-actions.yml` (YAML) | Magnitude: 16.52 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 2, args: 2, doc: 2
- `.github/workflows/scorecard.yml` (YAML) | Magnitude: 15.74 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, args: 8, import: 4, immutability_locks: 4
- `js/index.esm.js` (JAVASCRIPT) | Magnitude: 27.24 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 12, structural_boundaries: 12, api: 12, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/issue-labeled.yml` (YAML) | Magnitude: 16.44 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 18, branch: 3, args: 3, structural_boundaries: 2
- `scss/helpers/_color-bg.scss` (CSS) | Magnitude: 0.66 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, immutability_locks: 2, class_start: 1, safety: 1
- `.github/workflows/js.yml` (YAML) | Magnitude: 12.72 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, args: 5, func_start: 4, structural_boundaries: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/issue-labeled.yml` -> Churn: **55.66%** | Cog Load: 4.7619% | Debt: 62.2459%

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/src/base-component.js` -> **Severity: 0.158** (Bridge: 0.0016 * Flux: 99.9977%)
- `js/src/tooltip.js` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 99.9077%)
- `js/src/offcanvas.js` -> **Severity: 0.057** (Bridge: 0.0008 * Flux: 69.3404%)
- `js/src/modal.js` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 99.4578%)
- `js/src/util/config.js` -> **Severity: 0.023** (Bridge: 0.0007 * Flux: 35.6529%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/src/dom/event-handler.js` -> **Severity: 7.981** (Embedded: 0.1502 * Error Risk: 53.1376%)
- `js/tests/helpers/fixture.js` -> **Severity: 7.867** (Embedded: 0.1244 * Error Risk: 63.2477%)
- `js/src/util/index.js` -> **Severity: 7.666** (Embedded: 0.1777 * Error Risk: 43.1469%)
- `js/src/dom/selector-engine.js` -> **Severity: 5.389** (Embedded: 0.0952 * Error Risk: 56.5959%)
- `js/src/base-component.js` -> **Severity: 5.348** (Embedded: 0.0914 * Error Risk: 58.527%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `js/src/util/index.js` -> **Severity: 6405.857** (Blast Radius: 93.624 * Doc Risk: 68.4211%)
- `js/src/dom/event-handler.js` -> **Severity: 3499.528** (Blast Radius: 36.202 * Doc Risk: 96.6667%)
- `js/tests/helpers/fixture.js` -> **Severity: 3098.7** (Blast Radius: 30.987 * Doc Risk: 100.0%)
- `js/src/dom/selector-engine.js` -> **Severity: 1885.401** (Blast Radius: 19.711 * Doc Risk: 95.6522%)
- `js/src/dom/manipulator.js` -> **Severity: 1581.3** (Blast Radius: 17.57 * Doc Risk: 90.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1393 call pairs -- scoped 31.8%, unique 0.0%, ambiguous 1.5%, external 66.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1377 | 32.2% | 0.0% | 1.5% | 66.3% |
| html | 16 | 0.0% | 0.0% | 0.0% | 100.0% |

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
