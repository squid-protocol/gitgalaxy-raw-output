# ARCHITECTURAL_BRIEF: content
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mdn/content.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 14343 analyzed artifact(s), 6457 LOC.
- **Load-bearing artifact:** `scripts/filecheck/fixtures/html/script.svg` -- 44 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `files/en-us/web/html/reference/global_attributes/index.md` -- pulls in 165 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 15935 |
| Analyzed Artifacts (Scanned) | 14343 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1592 |
| Total LOC | 6457 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9276 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3088 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0096 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 39 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 14126 | 0 | 98.5% |
| XML | 175 | 451 | 1.2% |
| JAVASCRIPT | 18 | 1945 | 0.1% |
| YAML | 14 | 1865 | 0.1% |
| JSON | 7 | 2192 | 0.0% |
| PLAINTEXT | 2 | 1 | 0.0% |
| HTML | 1 | 3 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `5.809`
> **Composition Archetype:** `Mid Flat Project` (z +5.81; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 100%, Declarative / Non-Code 0%, Large Core Modules (2) 0%, Large Core Modules (3) 0%, Compute Cores Files 0%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 100 | 0.7% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14127 | 98.5% |
| Static: Minified & Vendor Opaque Mass | 115 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1592*

**Composition by Extension & Reason:**
- `.png`: 1165x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Machine-Generated Source Code Signature: 147 LOC), 3x Excluded (Machine-Generated Source Code Signature: 46 LOC)
- `.jpg`: 126x Excluded (Explicitly Denied Extension: '.jpg')
- `.gif`: 63x Excluded (Explicitly Denied Extension: '.gif')
- `.yml`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Zero-Density Threshold (LOC: 56, Signals: 0), 1x Zero-Density Threshold (LOC: 233, Signals: 0), 1x Zero-Density Threshold (LOC: 85, Signals: 0)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 126708 LOC exceeds safe regex boundaries), 1x Excluded (Massive Static Asset Blob: 2678 LOC)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 17495 LOC)
- `.jpeg`: 5x Excluded (Explicitly Denied Extension: '.jpeg')
- `.jsonc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1797 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 3.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 84.4 | 4.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 65.1 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.3 | 0.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 64.1 | 1.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.8 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.6 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 25.2 | 1.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5 | 3 | 0 | `scripts/analyze-pr-build.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 88 | 12 | 0 | `scripts/analyze-pr-build.js` |
| danger | 64 | 13 | 0 | `scripts/filecheck/checker.js` |
| concurrency | 136 | 12 | 0 | `scripts/filecheck/checker.js` |
| connectivity | 27 | 7 | 0 | `scripts/utils.js` |
| io | 97 | 15 | 0 | `scripts/filecheck/checker.js` |
| crypto | 1 | 1 | 0 | `scripts/analyze-pr-build.js` |
| ipc | 1 | 1 | 0 | `scripts/utils.js` |
| time | 3 | 2 | 0 | `scripts/analyze-pr-build.js` |
| serialization | 7 | 5 | 0 | `scripts/update-interface-data.js` |
| regex | 43 | 9 | 0 | `scripts/content/release-firefox.js` |
| events | 6 | 2 | 0 | `scripts/content/release-firefox.js` |
| tests | 22 | 2 | 0 | `scripts/filecheck/checker.test.js` |
| docs | 42 | 5 | 0 | `scripts/filecheck/checker.js` |
| debt | 72 | 13 | 0 | `scripts/content/release-firefox.js` |
| mutation | 568 | 20 | 0 | `scripts/analyze-pr-build.js` |
| dead_code | 2 | 2 | 0 | `scripts/front-matter_utils.js` |
| credential | 6 | 1 | 0 | `files/jsondata/L10n-Template.json` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/filecheck/checker.js` (Hits: 23)
- `scripts/content/release-firefox.js` (Hits: 18)
- `scripts/filecheck/checker.test.js` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **script.svg** (`scripts/filecheck/fixtures/html/script.svg`) — 44 inbound connections
2. **step.svg** (`files/en-us/web/css/reference/values/easing-function/step.svg`) — 13 inbound connections
3. **values.md** (`tests/front-matter_test_files/values.md`) — 9 inbound connections
4. **env.js** (`scripts/filecheck/env.js`) — 9 inbound connections
5. **margin-bottom.svg** (`files/en-us/web/css/reference/properties/margin-bottom/margin-bottom.svg`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.md** (`files/en-us/web/html/reference/global_attributes/index.md`) — 165 outbound dependencies
2. **index.md** (`files/en-us/web/accessibility/aria/guides/techniques/index.md`) — 115 outbound dependencies
3. **index.md** (`files/en-us/mdn/writing_guidelines/page_structures/page_types/page_type_key/index.md`) — 106 outbound dependencies
4. **index.md** (`files/en-us/web/accessibility/aria/reference/roles/index.md`) — 84 outbound dependencies
5. **index.md** (`files/en-us/web/javascript/guide/language_overview/index.md`) — 81 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `postAboutDangerousContent` **(Many-Argument Workhorses)** (@ `scripts/analyze-pr-build.js`) -> Impact: **77.0** | LOC: 100
  * *Intent:* /** * Constructs a comment reporting any dangerous external URLs. */
- `postAboutFlaws` **(Many-Argument Workhorses)** (@ `scripts/analyze-pr-build.js`) -> Impact: **51.2** | LOC: 88
  * *Intent:* /** * Constructs a comment reporting document flaws. */
- `checkFile` **(Many-Argument Workhorses)** (@ `scripts/filecheck/checker.js`) -> Impact: **48.1** | LOC: 131
  * *Intent:* /** * Check a single file for naming, type, reference, and compression rules. */
- `analyzePR` **(Many-Argument Workhorses)** (@ `scripts/analyze-pr-build.js`) -> Impact: **41.3** | LOC: 99
  * *Intent:* /** */ /** * Main function to analyze a PR build directory and post (or print) a comment. */
- `checkFrontMatter` **(Many-Argument Workhorses)** (@ `scripts/front-matter_utils.js`) -> Impact: **40.1** | LOC: 74
- `checkCompression` **(Defensive Guards)** (@ `scripts/filecheck/checker.js`) -> Impact: **35.4** | LOC: 85
  * *Intent:* /** * Compresses an image (if supported) and optionally saves the result, * enforcing size and compression delta constraints. */
- `equalsIgnoreCase` **(Defensive Guards)** (@ `scripts/sort_and_unique_file_lines.js`) -> Impact: **26.0** | LOC: 35
- `updateReleaseNotes` **(Many-Argument Workhorses)** (@ `scripts/content/release-firefox.js`) -> Impact: **25.5** | LOC: 70
  * *Intent:* /** * Update a release notes file with new status and date */
- `coerce` **(Compute Cores)** (@ `scripts/analyze-pr-build.js`) -> Impact: **19.4** | LOC: 48
- `movedFiles` **(Many-Argument Workhorses)** (@ `scripts/update-moved-file-links.js`) -> Impact: **18.2** | LOC: 22

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 8 | 5041.4 | 0.0% | 0.0% |
| `scripts` | 10 | 1106.04 | 63.14% | 7.64% |
| `scripts/filecheck` | 6 | 309.66 | 12.19% | 0.0% |
| `files/sidebars` | 14 | 243.8 | 1.04% | 0.0% |
| `scripts/content` | 2 | 148.54 | 28.09% | 0.0% |
| `tests` | 1 | 113.14 | 0.0% | 0.0% |
| `files/jsondata` | 5 | 104.74 | 0.0% | 0.0% |
| `files/en-us/web/api/ui_events/keyboard_event_key_values` | 1 | 93.34 | 0.0% | 0.0% |
| `files/en-us/web/css/guides/flexible_box_layout/basic_concepts` | 8 | 82.5 | 0.0% | 0.0% |
| `files/en-us/web/api/ui_events/keyboard_event_code_values` | 1 | 67.08 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scripts/sort_and_unique_file_lines.js` -> **65.1355%** Exposure
- `scripts/analyze-pr-build.js` -> **11.2905%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/sort_and_unique_file_lines.js` -> **100.0%** Exposure
- `scripts/front-matter_utils.js` -> **99.9998%** Exposure
- `scripts/update-moved-file-links.js` -> **99.999%** Exposure
- `scripts/analyze-pr-build.js` -> **99.9933%** Exposure
- `scripts/log-url-issues.js` -> **99.9929%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/sort_and_unique_file_lines.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `43` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `38570` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/analyze-pr-build.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 513.66 | **LOC:** 620 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postAboutDangerousContent` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* /** * Constructs a comment reporting any dangerous external URLs. */
  * `postAboutFlaws` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* /** * Constructs a comment reporting document flaws. */
  * `analyzePR` **(Many-Argument Workhorses)** (Impact: 41.3)
    * *Intent:* /** */ /** * Main function to analyze a PR build directory and post (or print) a comment. */
  * `coerce` **(Compute Cores)** (Impact: 19.4)
  * `getPatchLines` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* /** * Extracts added (new) lines from patch objects. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 81
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 82`, `args: 21`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 56`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `concurrency: 21`, `import: 9`
* *Defense:* `safety: 24`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rari, rest, node-html-parser, node:crypto, node:fs, promises, node:path, parse-diff...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/filecheck/checker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 198.74 | **LOC:** 399 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (82.8%), Guard Balance (formerly Safety Score) (52.3%), Complexity Load (formerly Cognitive Load) (30.2%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkFile` **(Many-Argument Workhorses)** (Impact: 48.1)
    * *Intent:* /** * Check a single file for naming, type, reference, and compression rules. */
  * `checkCompression` **(Defensive Guards)** (Impact: 35.4)
    * *Intent:* /** * Compresses an image (if supported) and optionally saves the result, * enforcing size and compr...
  * `resolveDirectory` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /** * Resolve a path to a list of files that should be checked. */
  * `runChecker` **(Defensive Guards)** (Impact: 7.1)
    * *Intent:* /** * Run the checker across a set of files or directories. */
  * `formatSize` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 57`, `args: 16`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `io: 23`, `api: 3`, `concurrency: 22`, `import: 19`
* *Defense:* `safety: 15`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000139
  * `Imports (Out-Degree: 2):` constants.js, env.js, utils.js, async, cheerio, cli-progress, fdir, file-type...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/content/release-firefox.js` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 146.86 | **LOC:** 282 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (56.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateReleaseNotes` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* /** * Update a release notes file with new status and date */
  * `main` **(I/O & Config Routines)** (Impact: 16.3)
    * *Intent:* /** * Main function */
  * `deactivatePreviousStable` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* /** * Remove active status from a previous stable release */
  * `createNightlyPage` **(Compute Cores)** (Impact: 4.3)
    * *Intent:* /** * Create a new Nightly release notes page */
  * `formatDate` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /** * Format date for front matter */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 16`
* *Architecture:* `io: 18`, `concurrency: 21`, `import: 3`
* *Defense:* `safety: 6`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/update-moved-file-links.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 121.16 | **LOC:** 146 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.3%), Guard Balance (formerly Safety Score) (84.4%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `movedFiles` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `getImageSlug` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* /** * Try to get slug for an image from file path */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 29`, `args: 7`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 17`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, promises, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/front-matter_linter.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 113.14 | **LOC:** 117 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPath` **(Parameter Forwarders)** (Impact: 1.6)
  * `getContent` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Concurrency (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 31`, `args: 9`, `func_start: 4`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 4`, `concurrency: 21`, `import: 5`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` front-matter_utils.js, strict, node:fs, node:test, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/log-url-issues.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 98.08 | **LOC:** 219 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Complexity Load (formerly Cognitive Load) (56.5%), Concurrency Surface (formerly Concurrency) (16.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDeletedSlugs` **(Compute Cores)** (Impact: 17.7)
  * `getFragmentDetails` **(Compute Cores)** (Impact: 12.6)
  * `getFileAnchors` **(Compute Cores)** (Impact: 4.8)
  * `getFileContent` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 36`, `args: 25`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 19`
* *Architecture:* `io: 5`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.js, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/front-matter_utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 93.54 | **LOC:** 101 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.187; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Concurrency Surface (formerly Concurrency) (97.6%), Guard Balance (formerly Safety Score) (81.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkFrontMatter` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `getAjvValidator` **(Parameter Forwarders)** (Impact: 3.1)
  * `areAttributesInOrder` **(Defensive Guards)** (Impact: 2.0)
  * `getRelativePath` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 24`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000139
  * `Imports (Out-Degree: 0):` better-ajv-errors, ajv, ajv-formats, gray-matter, promises, node:path, prettier, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `files/en-us/web/api/ui_events/keyboard_event_key_values/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 93.34 | **LOC:** 4667 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` key
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/front-matter_linter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 86.16 | **LOC:** 125 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.3%), Complexity Load (formerly Cognitive Load) (94.9%), Guard Balance (formerly Safety Score) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveDirectory` **(Defensive Guards)** (Impact: 16.7)
  * `lintFrontMatter` **(Defensive Guards)** (Impact: 14.3)
    * *Intent:* // lint front matter
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 30`, `args: 10`, `func_start: 3`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 1`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` front-matter_utils.js, async, cli-progress, fdir, promises, node:os, node:path, yargs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/ui_events/keyboard_event_code_values/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 67.08 | **LOC:** 3354 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/keyboardevent/keycode/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 66.06 | **LOC:** 3303 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 58.22 | **LOC:** 92 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.9%), Guard Balance (formerly Safety Score) (65.1%), Connectivity (formerly Api Exposure) (64.1%), Concurrency Surface (formerly Concurrency) (39.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execGit` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `getLocations` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /* * Returns locations (line and column numbers) of 'searchValue' in the given 'content'. */
  * `walkSync` **(Compute Cores)** (Impact: 6.2)
  * `stringToFragment` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* /* * Convert Markdown header into URL slug. */
  * `isImagePath` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 24`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 6`, `api: 8`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:child_process, promises, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/sort_and_unique_file_lines.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 54.12 | **LOC:** 64 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Complexity Load (formerly Cognitive Load) (78.3%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `equalsIgnoreCase` **(Defensive Guards)** (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 10`, `args: 5`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `import: 1`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/update-interface-data.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 50.6 | **LOC:** 36 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.6%), Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (62.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* `io: 8`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/learn_web_development/extensions/forms/how_to_build_custom_form_controls/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 41.22 | **LOC:** 2061 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Advanced_form_styling, Example_1, Example_2, Example_3, Example_4, Example_5, tabIndex, ARIA...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/video_codecs/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 38.66 | **LOC:** 1933 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MediaStream_Recording_API, WebRTC_API, Audio_codecs, Containers, Support_issues, WebRTC_codecs, contouring-effect.jpg, mosquito-effect-sm.png...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/api/webgl_api/webgl_model_view_projection/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 34.06 | **LOC:** 1703 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` WebGL_API, Matrix_math_for_the_web, camera_view_frustum.svg, clip_space_graph.svg, fullcamerafov.svg, part4.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/learn_web_development/extensions/forms/ui_pseudo-classes/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.76 | **LOC:** 1488 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Handling_conflicts, Advanced_form_styling, Form_validation, change_event, Generated_content, Selectors, appearance, Constraint_validation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/mozilla/add-ons/webextensions/manifest.json/theme/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.52 | **LOC:** 1476 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` color_value, theme.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/html/reference/attributes/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 29.36 | **LOC:** 1468 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Events, click_event, Elements, Functions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/html/reference/elements/input/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.76 | **LOC:** 1438 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **50**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Color_space, Attribute_selectors, Advanced_form_styling, Basic_native_form_controls, Form_validation, How_to_structure_a_web_form, Sending_and_retrieving_form_data, Styling_web_forms...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/audio_codecs/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.6 | **LOC:** 1430 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WebRTC_API, Audio_concepts, Containers, Video_codecs, WebRTC_codecs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files/en-us/web/media/guides/formats/image_types/index.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 28.24 | **LOC:** 1412 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.069; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` XML, Webpage_metadata, @media, link, picture, Media, Formats, Video_codecs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/filecheck/checker.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 27.96 | **LOC:** 57 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.069; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 13`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 8`, `concurrency: 12`, `import: 5`
* *Defense:* `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.069
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` checker.js, strict, node:fs, node:test, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/analyze-pr-build.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 513.66
- `scripts/filecheck/checker.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 198.74
- `scripts/content/release-firefox.js` -> **Vadim Makeev** (100.0% isolated ownership) | Magnitude: 146.86
- `scripts/front-matter_linter.js` -> **Claas Augner** (100.0% isolated ownership) | Magnitude: 86.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/front-matter_utils.js` -> **Severity: 0.011** (Embedded: 0.0001 * Error Risk: 81.1218%)
- `scripts/filecheck/checker.js` -> **Severity: 0.007** (Embedded: 0.0001 * Error Risk: 52.3061%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/front-matter_utils.js` -> **Severity: 18.7** (Blast Radius: 0.187 * Doc Risk: 100.0%)
- `scripts/filecheck/utils.js` -> **Severity: 6.9** (Blast Radius: 0.069 * Doc Risk: 100.0%)
- `scripts/front-matter_linter.js` -> **Severity: 6.9** (Blast Radius: 0.069 * Doc Risk: 100.0%)
- `scripts/log-url-issues.js` -> **Severity: 6.9** (Blast Radius: 0.069 * Doc Risk: 100.0%)
- `scripts/sort_and_unique_file_lines.js` -> **Severity: 6.9** (Blast Radius: 0.069 * Doc Risk: 100.0%)

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
