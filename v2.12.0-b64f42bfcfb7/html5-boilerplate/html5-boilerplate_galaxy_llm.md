# ARCHITECTURAL_BRIEF: html5-boilerplate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/h5bp/html5-boilerplate.git` |
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
- **Scope:** 34 analyzed artifact(s), 768 LOC.
- **Load-bearing artifact:** `package.json` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `gulpfile.mjs` -- pulls in 12 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 79 |
| Analyzed Artifacts (Scanned) | 34 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 45 |
| Total LOC | 768 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 43.0% |
| Dominant Lang | YAML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.74 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7906 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 12 | 385 | 35.3% |
| JAVASCRIPT | 8 | 308 | 23.5% |
| MARKDOWN | 6 | 0 | 17.6% |
| PLAINTEXT | 5 | 1 | 14.7% |
| HTML | 2 | 74 | 5.9% |
| XML | 1 | 0 | 2.9% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 33 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 79%, Declarative / Non-Code 15%, Large Core Modules (2) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 23 | 67.6% |
| Unknown | 1 | 2.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 29.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 45*

**Composition by Extension & Reason:**
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4596 LOC)
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.webmanifest`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.webmanifest)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 11.9 | 1.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 52.0 | 17.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.2 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.4 | 2.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 21.5 | 2.9 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 16.8 | 2.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 61.3 | 18.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 1 | 1 | 0 | `test/file_content.mjs` |
| guards | 37 | 10 | 4 | `.github/workflows/publish.yml` |
| danger | 2 | 2 | 0 | `gulpfile.mjs` |
| concurrency | 3 | 3 | 0 | `.github/workflows/test.yml` |
| connectivity | 19 | 12 | 1 | `src/index.html` |
| io | 25 | 5 | 4 | `gulpfile.mjs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 24 | 6 | 3 | `src/index.html` |
| tests | 14 | 4 | 1 | `test/file_existence.mjs` |
| docs | 31 | 14 | 3 | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| debt | 9 | 5 | 1 | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| mutation | 67 | 10 | 9 | `src/index.html` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `gulpfile.mjs` (Hits: 9)
- `src/index.html` (Hits: 6)
- `test/file_content.mjs` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **package.json** (`package.json`) — 3 inbound connections
2. **LICENSE.txt** (`LICENSE.txt`) — 2 inbound connections
3. **webpack.common.js** (`src/webpack.common.js`) — 2 inbound connections
4. **CONTRIBUTING.md** (`.github/CONTRIBUTING.md`) — 1 inbound connections
5. **app.js** (`src/js/app.js`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gulpfile.mjs** (`gulpfile.mjs`) — 12 outbound dependencies
2. **file_existence.mjs** (`test/file_existence.mjs`) — 6 outbound dependencies
3. **index.html** (`src/index.html`) — 6 outbound dependencies
4. **file_content.mjs** (`test/file_content.mjs`) — 5 outbound dependencies
5. **ossf-scorecard.yml** (`.github/workflows/ossf-scorecard.yml`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `checkString` **(Defensive Guards)** (@ `test/file_content.mjs`) -> Impact: **13.3** | LOC: 27
  * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- `checkFiles` **(Defensive Guards)** (@ `test/file_existence.mjs`) -> Impact: **11.3** | LOC: 53
  * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- `Check for dist changes` **(I/O & Config Routines)** (@ `.github/workflows/build-dist.yml`) -> Impact: **4.5** | LOC: 11
- `media` **(I/O & Config Routines)** (@ `src/404.html`) -> Impact: **2.6** | LOC: 13
- `runTests` **(Callbacks & Closures)** (@ `test/file_existence.mjs`) -> Impact: **1.6** | LOC: 11
  * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- `runTests` **(Callbacks & Closures)** (@ `test/file_content.mjs`) -> Impact: **1.5** | LOC: 10
  * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
- `publish npm` **(Interface Declarations)** (@ `.github/workflows/publish.yml`) -> Impact: **1.2** | LOC: 4
- `Get npm cache directory` **(I/O & Config Routines)** (@ `.github/workflows/push-to-template.yml`) -> Impact: **1.2** | LOC: 4
- `Get npm cache directory` **(I/O & Config Routines)** (@ `.github/workflows/test.yml`) -> Impact: **1.2** | LOC: 4
- `Install dependencies` **(I/O & Config Routines)** (@ `.github/workflows/build-dist.yml`) -> Impact: **1.1** | LOC: 2

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Interface Declarations**: signature/entry function exposing API with minimal logic

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 7 | 5046.54 | 0.73% | 0.0% |
| `src` | 8 | 111.92 | 0.51% | 0.0% |
| `.github/workflows` | 8 | 93.38 | 1.04% | 0.0% |
| `test` | 2 | 45.14 | 7.81% | 0.0% |
| `.github/ISSUE_TEMPLATE` | 3 | 44.4 | 1.87% | 33.08% |
| `.github` | 5 | 21.76 | 0.0% | 0.0% |
| `src/js` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.2438%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/webpack.common.js` -> **16.7982%** Exposure
- `src/webpack.config.dev.js` -> **16.7982%** Exposure
- `src/webpack.config.prod.js` -> **16.7982%** Exposure
- `.github/workflows/publish.yml` -> **16.1747%** Exposure

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
- **Unknown Dependencies:** `63` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.951)
- **Top Global Matches:** file_cluster_13: 5.951, file_cluster_2: 6.138, file_cluster_17: 6.824
- **Magnitude:** 42.84 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (11.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 4`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 6`, `api: 8`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` favicon.ico, icon.svg, style.css, icon.png, app.js, site.webmanifest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/file_content.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.325)
- **Top Global Matches:** file_cluster_10: 8.325, file_cluster_9: 8.864, file_cluster_15: 10.01
- **Magnitude:** 24.58 | **LOC:** 53 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkString` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  * `runTests` **(Callbacks & Closures)** (Impact: 1.5)
    * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`, `args: 5`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 4`, `import: 5`
* *Defense:* `safety: 4`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, assert, fs, module, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/file_existence.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.263)
- **Top Global Matches:** file_cluster_10: 5.263, file_cluster_15: 8.29, file_cluster_2: 8.341
- **Magnitude:** 20.56 | **LOC:** 117 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.0%), Complexity Load (formerly Cognitive Load) (3.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkFiles` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  * `runTests` **(Callbacks & Closures)** (Impact: 1.6)
    * *Intent:* // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 16`, `args: 10`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 4`, `import: 6`
* *Defense:* `safety: 5`, `doc: 2`, `test: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, assert, fs, glob, module, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webpack.config.prod.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.277)
- **Top Global Matches:** file_cluster_2: 2.277, file_cluster_17: 4.805, file_cluster_13: 6.012
- **Magnitude:** 17.5 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` webpack.common.js, copy-webpack-plugin, html-webpack-plugin, webpack-merge
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webpack.config.dev.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.453)
- **Top Global Matches:** file_cluster_2: 2.453, file_cluster_17: 4.872, file_cluster_13: 6.054
- **Magnitude:** 17.24 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` webpack.common.js, webpack-merge
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/webpack.common.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.263)
- **Top Global Matches:** file_cluster_2: 4.263, file_cluster_17: 6.211, file_cluster_13: 7.044
- **Magnitude:** 17.22 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 65.595; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Connectivity (formerly Api Exposure) (21.5%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 0):` path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `gulpfile.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.419)
- **Top Global Matches:** file_cluster_10: 4.419, file_cluster_2: 5.59, file_cluster_17: 6.591
- **Magnitude:** 17.2 | **LOC:** 144 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 24.295; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 24`, `args: 10`
* *Risk/State:* None
* *Architecture:* `io: 9`, `import: 12`
* *Defense:* `doc: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, archiver, del, fs, glob, gulp, gulp-autoprefixer, gulp-eslint-new...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/codeql-analysis.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.159)
- **Top Global Matches:** file_cluster_17: 4.159, file_cluster_2: 4.204, file_cluster_15: 5.84
- **Magnitude:** 16.62 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.7%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, analyze@3599b3baa15b485a2e49ef411a7a4bb2452e7f93, init@3599b3baa15b485a2e49ef411a7a4bb2452e7f93
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `eslint.config.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.941)
- **Top Global Matches:** file_cluster_2: 3.941, file_cluster_13: 4.483, file_cluster_17: 5.467
- **Magnitude:** 16.56 | **LOC:** 31 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (5.1%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` js, eslint-plugin-mocha, config, globals
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/spellcheck.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.353)
- **Top Global Matches:** file_cluster_17: 4.353, file_cluster_2: 4.651, file_cluster_15: 5.934
- **Magnitude:** 16.4 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 4`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, cspell-action@9cd41bb518a24fefdafd9880cbab8f0ceba04d28
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/bug_report.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.666)
- **Top Global Matches:** file_cluster_2: 2.666, file_cluster_17: 5.187, file_cluster_13: 6.482
- **Magnitude:** 16.22 | **LOC:** 62 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Complexity Load (formerly Cognitive Load) (2.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`
* *Risk/State:* `fragile_debt: 3`
* *Architecture:* None
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/ossf-scorecard.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.684)
- **Top Global Matches:** file_cluster_17: 4.684, file_cluster_2: 4.743, file_cluster_15: 6.162
- **Magnitude:** 15.74 | **LOC:** 44 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.7%), Complexity Load (formerly Cognitive Load) (2.8%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 2`, `args: 8`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02, upload-sarif@3599b3baa15b485a2e49ef411a7a4bb2452e7f93, scorecard-action@4eaacf0543bb3f2c246792bd56e8cdeffafb205a
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/feature_request.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.045)
- **Top Global Matches:** file_cluster_2: 2.045, file_cluster_17: 4.906, file_cluster_13: 6.248
- **Magnitude:** 15.58 | **LOC:** 30 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (2.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/dependabot.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.61)
- **Top Global Matches:** file_cluster_2: 3.61, file_cluster_17: 5.743, file_cluster_13: 6.909
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/dependency-review.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.72)
- **Top Global Matches:** file_cluster_17: 4.72, file_cluster_2: 5.022, file_cluster_15: 6.247
- **Magnitude:** 15.28 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%), Test Surface (formerly Verification) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, dependency-review-action@05fe4576374b728f0c523d6a13d64c25081e0803
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/ISSUE_TEMPLATE/config.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.266)
- **Top Global Matches:** file_cluster_2: 2.266, file_cluster_17: 5.005, file_cluster_13: 6.316
- **Magnitude:** 12.6 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/js/app.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 34.62; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/icon.svg` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 34.62; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `.github/workflows/build-dist.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.117)
- **Top Global Matches:** file_cluster_2: 6.117, file_cluster_17: 6.757, file_cluster_15: 6.782
- **Magnitude:** 8.5 | **LOC:** 48 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%), Complexity Load (formerly Cognitive Load) (5.5%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Check for dist changes` **(I/O & Config Routines)** (Impact: 4.5)
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 1.1)
  * `Build project` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 2`, `args: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, setup-node@2028fbc5c25fe9cf00d9f06a71cc4710d4507903, create-pull-request@v8
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/publish.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.121)
- **Top Global Matches:** file_cluster_11: 6.121, file_cluster_2: 7.297, file_cluster_17: 7.614
- **Magnitude:** 8.46 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.7%), Mutation Surface (formerly State Flux) (16.2%), Connectivity (formerly Api Exposure) (3.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publish npm` **(Interface Declarations)** (Impact: 1.2)
  * `Get tag` **(I/O & Config Routines)** (Impact: 1.1)
  * `Create Zip Folder` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 11`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, create-release@0cb9c9b65d5d1901c1f53e5e66eaf4afd303e70e, setup-node@2028fbc5c25fe9cf00d9f06a71cc4710d4507903, upload-release-asset@e8f9f06c4b078e705bd2ea027f0926603fc9b4d5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 8.08 | **LOC:** 404 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/push-to-template.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.119)
- **Top Global Matches:** file_cluster_2: 6.119, file_cluster_17: 6.626, file_cluster_15: 7.124
- **Magnitude:** 6.24 | **LOC:** 46 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Get npm cache directory` **(I/O & Config Routines)** (Impact: 1.2)
  * `Install dependencies` **(I/O & Config Routines)** (Impact: 1.1)
  * `Build` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 11`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cache@v5, checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, setup-node@2028fbc5c25fe9cf00d9f06a71cc4710d4507903, github-action-push-to-another-repository@main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/test.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.031)
- **Top Global Matches:** file_cluster_2: 7.031, file_cluster_17: 7.368, file_cluster_13: 7.543
- **Magnitude:** 6.14 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 24.295; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.3%), Concurrency Surface (formerly Concurrency) (28.2%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Get npm cache directory` **(I/O & Config Routines)** (Impact: 1.2)
  * `run` **(State Mutators)** (Impact: 1.1)
  * `run` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cache@6f8efc29b200d32929f49075959781ed54ec270c, checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd, setup-node@2028fbc5c25fe9cf00d9f06a71cc4710d4507903
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/404.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.615)
- **Top Global Matches:** file_cluster_12: 6.615, file_cluster_2: 7.64, file_cluster_7: 7.84
- **Magnitude:** 4.6 | **LOC:** 63 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Complexity Load (formerly Cognitive Load) (4.1%), Connectivity (formerly Api Exposure) (3.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `media` **(I/O & Config Routines)** (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/codeql-analysis.yml` (YAML) | Magnitude: 16.62 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 28, args: 3, import: 3, immutability_locks: 3
- `.github/workflows/ossf-scorecard.yml` (YAML) | Magnitude: 15.74 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, args: 8, import: 4, immutability_locks: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/webpack.common.js` -> **Severity: 3.074** (Embedded: 0.0606 * Error Risk: 50.7142%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/file_content.mjs` -> **Severity: 2429.5** (Blast Radius: 24.295 * Doc Risk: 100.0%)
- `test/file_existence.mjs` -> **Severity: 2429.5** (Blast Radius: 24.295 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 23 call pairs -- scoped 8.7%, unique 0.0%, ambiguous 0.0%, external 91.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 23 | 8.7% | 0.0% | 0.0% | 91.3% |

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
