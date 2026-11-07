# ARCHITECTURAL_BRIEF: reveal.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hakimel/reveal.js.git` |
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
- **Scope:** 164 analyzed artifact(s), 20214 LOC.
- **Load-bearing artifact:** `js/reveal.js` -- 16 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `js/reveal.js` -- pulls in 25 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `js/reveal.js` at magnitude 1432.7 (structural weight, not risk).
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
| Total Artifacts | 228 |
| Analyzed Artifacts (Scanned) | 164 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 64 |
| Total LOC | 20214 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 71.9% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6714 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4056 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8235 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 47 | 3792 | 28.7% |
| JAVASCRIPT | 40 | 6640 | 24.4% |
| HTML | 32 | 5633 | 19.5% |
| CSS | 24 | 3109 | 14.6% |
| MARKDOWN | 8 | 0 | 4.9% |
| JSON | 6 | 995 | 3.7% |
| PLAINTEXT | 4 | 0 | 2.4% |
| YAML | 3 | 45 | 1.8% |

## 4.1 SOURCE ENCODINGS
All 164 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 27%, Callbacks & Closures Files 7%, Large Core Modules (2) 7%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 152 | 92.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 7.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 64*

**Composition by Extension & Reason:**
- `.css`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 5x Excluded (Explicitly Denied Extension: '.woff')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 1x Excluded (Massive Static Asset Blob: 3895 LOC), 1x Excluded (Massive Static Asset Blob: 3959 LOC)
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.mp4`: 1x Excluded (Explicitly Denied Extension: '.mp4')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 15.7 | 4.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 28.7 | 40.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 84.7 | 18.0 | 7.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.7 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 78.9 | 9.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 27.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 72 | 23 | 1 | `react/src/components/deck.test.tsx` |
| cleanup | 102 | 26 | 1 | `js/reveal.js` |
| guards | 792 | 58 | 12 | `js/reveal.js` |
| danger | 200 | 38 | 3 | `test/test-markdown.html` |
| concurrency | 332 | 52 | 5 | `react/src/components/deck.test.tsx` |
| connectivity | 503 | 105 | 8 | `examples/auto-animate.html` |
| io | 338 | 41 | 4 | `demo.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 5 | 0 | `plugin/notes/speaker-view.html` |
| time | 59 | 14 | 0 | `plugin/notes/speaker-view.html` |
| serialization | 21 | 6 | 0 | `plugin/notes/speaker-view.html` |
| regex | 97 | 18 | 1 | `plugin/markdown/plugin.js` |
| events | 327 | 54 | 5 | `test/test.html` |
| tests | 633 | 23 | 8 | `test/test.html` |
| docs | 587 | 90 | 7 | `js/reveal.d.ts` |
| debt | 45 | 18 | 1 | `react/src/components/code.test.tsx` |
| mutation | 3946 | 108 | 67 | `js/reveal.js` |
| dead_code | 74 | 4 | 0 | `js/reveal.d.ts` |
| credential | 47 | 1 | 0 | `react/demo/package-lock.json` |
| threat | 1 | 1 | 0 | `css/theme/blood.scss` |
| ml_ai | 5 | 3 | 0 | `react/demo/src/demo-app.tsx` |
| ui | 469 | 47 | 6 | `react/src/components/deck.test.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `demo.html` (Hits: 100)
- `examples/auto-animate.html` (Hits: 41)
- `examples/layout-helpers.html` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **reveal.js** (`js/reveal.js`) — 16 inbound connections
2. **util.ts** (`js/utils/util.ts`) — 12 inbound connections
3. **types.ts** (`react/src/types.ts`) — 9 inbound connections
4. **reveal-context.ts** (`react/src/reveal-context.ts`) — 8 inbound connections
5. **monokai.css** (`public/plugin/highlight/monokai.css`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reveal.js** (`js/reveal.js`) — 25 outbound dependencies
2. **demo.html** (`demo.html`) — 10 outbound dependencies
3. **index.ts** (`react/src/index.ts`) — 9 outbound dependencies
4. **markdown.html** (`examples/markdown.html`) — 8 outbound dependencies
5. **scroll.html** (`examples/scroll.html`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `onDocumentKeyDown` **(Defensive Guards)** (@ `js/controllers/keyboard.js`) -> Impact: **194.7** | LOC: 273
  * *Intent:* /** * Handler for the document level 'keydown' event. * */
- `slide` **(Many-Argument Workhorses)** (@ `js/reveal.js`) -> Impact: **94.7** | LOC: 194
  * *Intent:* /** * Steps from the current point in the presentation to the * slide which matches the specified horizontal and vertical * indices. * * target slide ...
- `autoAnimateElements` **(Many-Argument Workhorses)** (@ `js/controllers/autoanimate.js`) -> Impact: **57.6** | LOC: 123
  * *Intent:* /** * Creates a FLIP animation where the `to` element starts out * in the `from` element position and animates to its original * state. * * auto-anima...
- `load` **(Many-Argument Workhorses)** (@ `js/controllers/slidecontent.js`) -> Impact: **56.0** | LOC: 150
  * *Intent:* /** * Called when the given slide is within the configured view * distance. Shows the slide element and loads any content * that is set to load lazily...
- `onTouchMove` **(Compute Cores)** (@ `js/controllers/touch.js`) -> Impact: **52.6** | LOC: 90
  * *Intent:* /** * Handler for the 'touchmove' event. * */
- `update` **(Compute Cores)** (@ `js/controllers/backgrounds.js`) -> Impact: **52.1** | LOC: 136
  * *Intent:* /** * Updates the background elements to reflect the current * slide. * * all vertical slides (not just the present) will be updated. */
- `updateSlides` **(Many-Argument Workhorses)** (@ `js/reveal.js`) -> Impact: **50.9** | LOC: 117
  * *Intent:* /** * Updates one dimension of slides by showing the slide * with the specified index. * * the group of slides we are working with * shown * * might d...
- `Code` **(Compute Cores)** (@ `react/src/components/code.tsx`) -> Impact: **47.1** | LOC: 94
- `addAttributes` **(Many-Argument Workhorses)** (@ `react/src/utils/markdown.ts`) -> Impact: **47.1** | LOC: 61
- `addAttributes` **(Defensive Guards)** (@ `plugin/markdown/plugin.js`) -> Impact: **46.0** | LOC: 39
  * *Intent:* /** * Add attributes to the parent element of a text node, * or the element of an attribute node. */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js/controllers` | 19 | 3497.16 | 47.41% | 2.58% |
| `test` | 17 | 1670.03 | 3.24% | 0.0% |
| `js` | 4 | 1490.17 | 21.82% | 25.0% |
| `examples` | 13 | 1362.82 | 0.0% | 0.0% |
| `react/src/components` | 12 | 1066.45 | 13.79% | 0.0% |
| `__monolith__` | 9 | 561.56 | 1.58% | 0.0% |
| `plugin/notes` | 4 | 473.32 | 23.79% | 0.0% |
| `plugin/markdown` | 3 | 384.08 | 25.19% | 2.95% |
| `plugin/highlight` | 3 | 287.84 | 25.04% | 0.0% |
| `plugin/math` | 7 | 282.32 | 41.8% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `js/reveal.d.ts` -> **100.0%** Exposure
- `js/controllers/location.js` -> **21.1002%** Exposure
- `js/controllers/touch.js` -> **17.4995%** Exposure
- `scripts/zip.js` -> **16.1745%** Exposure
- `js/controllers/slidecontent.js` -> **10.4529%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `js/components/playback.js` -> **100.0%** Exposure
- `js/controllers/autoanimate.js` -> **100.0%** Exposure
- `js/controllers/backgrounds.js` -> **100.0%** Exposure
- `js/controllers/fragments.js` -> **100.0%** Exposure
- `js/controllers/location.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/reveal.d.ts` -> **71** Orphaned Functions | **0** Duplicates
- `react/src/components/deck.test.tsx` -> **0** Orphaned Functions | **5** Duplicates
- `scripts/zip.js` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `167` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `js/reveal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.613)
- **Top Global Matches:** file_cluster_4: 7.613, file_cluster_15: 9.491, file_cluster_10: 9.948
- **Magnitude:** 1432.7 | **LOC:** 2962 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **25**; blast radius 44.302; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Connectivity (formerly Api Exposure) (46.2%)
- **Documentation Coverage:** 23.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `slide` **(Many-Argument Workhorses)** (Impact: 94.7)
    * *Intent:* /** * Steps from the current point in the presentation to the * slide which matches the specified ho...
  * `updateSlides` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* /** * Updates one dimension of slides by showing the slide * with the specified index. * * the group...
  * `updateSlidesVisibility` **(I/O & Config Routines)** (Impact: 31.5)
    * *Intent:* /** * Optimization method; hide all slides that are far away * from the present slide. */
  * `cueAutoSlide` **(Defensive Guards)** (Impact: 28.6)
    * *Intent:* /** * Cues a new automated slide if enabled in the config. */
  * `layout` **(I/O & Config Routines)** (Impact: 24.7)
    * *Intent:* /** * Applies JavaScript-controlled layout rules to the * presentation. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 557
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 204`, `args: 123`, `func_start: 99`
* *Risk/State:* `state_mutation: 211`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 25`
* *Defense:* `safety: 136`, `doc: 81`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.302
  * `Choke Point (Betweenness):` 0.016171 | `Ripple Effect (Closeness):` 0.09816
  * `Imports (Out-Degree: 25):` package.json, playback, config.ts, autoanimate, backgrounds, controls, focus, fragments...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `test/test-markdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.013)
- **Top Global Matches:** file_cluster_7: 6.013, file_cluster_14: 9.16, file_cluster_5: 9.793
- **Magnitude:** 828.37 | **LOC:** 516 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (3.7%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 65`, `args: 78`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 1`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/scrollview.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.305)
- **Top Global Matches:** file_cluster_10: 8.305, file_cluster_4: 8.575, file_cluster_15: 9.06
- **Magnitude:** 468.28 | **LOC:** 924 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (47.7%)
- **Documentation Coverage:** 36.1702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPageElement` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* // Creates a new page element and appends the given slide/bg // to it.
  * `syncPages` **(I/O & Config Routines)** (Impact: 25.9)
    * *Intent:* /** * Updates our pages to match the latest configuration and * presentation size. */
  * `activate` **(I/O & Config Routines)** (Impact: 24.4)
    * *Intent:* /** * Activates the scroll view. This rearranges the presentation DOM * by—among other things—wrappi...
  * `syncScrollPosition` **(I/O & Config Routines)** (Impact: 17.8)
    * *Intent:* /** * Reads the current scroll position and updates our active * trigger states accordingly. */
  * `toggle` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 67`, `args: 70`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 110`
* *Architecture:* `io: 4`, `api: 6`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 17`, `doc: 24`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `demo.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.138)
- **Top Global Matches:** file_cluster_13: 5.138, file_cluster_2: 5.875, file_cluster_17: 6.498
- **Magnitude:** 448.12 | **LOC:** 701 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 4.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.5%), Connectivity (formerly Api Exposure) (9.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 180`, `args: 91`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 100`, `api: 22`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` highlight.js, monokai.css, markdown.js, notes.js, search.js, zoom.js, reset.css, reveal.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/autoanimate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.506)
- **Top Global Matches:** file_cluster_8: 7.506, file_cluster_6: 12.139, file_cluster_4: 20.358
- **Magnitude:** 413.22 | **LOC:** 627 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%), Complexity Load (formerly Cognitive Load) (54.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `autoAnimateElements` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* /** * Creates a FLIP animation where the `to` element starts out * in the `from` element position an...
  * `getAutoAnimatableProperties` **(Defensive Guards)** (Impact: 39.6)
    * *Intent:* /** * Returns an object containing all of the properties * that can be auto-animated for the given e...
  * `run` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* /** * Runs an auto-animation between the given slides. * */
  * `findAutoAnimateMatches` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* /** * Finds matching elements between two slides. * * a stringified ID based on its contents */...
  * `getAutoAnimateOptions` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* /** * Returns the auto-animate options for the given element. * * from, either a slide or an animati...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 78`, `args: 30`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 73`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 42`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/slidecontent.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.528)
- **Top Global Matches:** file_cluster_4: 7.528, file_cluster_10: 11.426, file_cluster_15: 11.77
- **Magnitude:** 391.82 | **LOC:** 747 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.7%)
- **Documentation Coverage:** 22.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* /** * Called when the given slide is within the configured view * distance. Shows the slide element ...
  * `startEmbeddedContent` **(Defensive Guards)** (Impact: 32.5)
    * *Intent:* /** * Start playback of any embedded content inside of * the given element. * */
  * `stopEmbeddedContent` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* /** * Stop playback of any embedded content inside of * the targeted slide. * */
  * `playMediaElement` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Plays the given HTMLMediaElement and handles any playback * errors, such as the browser not al...
  * `startEmbeddedIframe` **(Defensive Guards)** (Impact: 17.4)
    * *Intent:* /** * "Starts" the content of an embedded iframe using the * postMessage API. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 64`, `args: 50`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 35`, `doc: 16`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 2):` device, util, fitty
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/auto-animate.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.783)
- **Top Global Matches:** file_cluster_13: 4.783, file_cluster_2: 5.379, file_cluster_17: 5.964
- **Magnitude:** 354.22 | **LOC:** 443 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 90`, `args: 75`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 41`, `api: 45`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` highlight.js, monokai.css, reveal.css, reveal.js, black.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/markdown/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.221)
- **Top Global Matches:** file_cluster_4: 7.221, file_cluster_9: 10.211, file_cluster_15: 11.075
- **Magnitude:** 352.18 | **LOC:** 488 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 7.759; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (90.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%)
- **Documentation Coverage:** 47.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAttributes` **(Defensive Guards)** (Impact: 46.0)
    * *Intent:* /** * Add attributes to the parent element of a text node, * or the element of an attribute node. */
  * `slidify` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** * Parses a data string into multiple slides based * on the passed in separator arguments. */
  * `getSlidifyOptions` **(Defensive Guards)** (Impact: 20.4)
    * *Intent:* /** * Inspects the given options and fills out default * values for what's not defined. */
  * `loadExternalMarkdown` **(Defensive Guards)** (Impact: 13.5)
  * `getMarkdownFromSlide` **(Compute Cores)** (Impact: 12.5)
    * *Intent:* /** * Retrieves the markdown contents of a slide section * element. Normalizes leading tabs/whitespa...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 48`, `args: 28`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 27`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 0):` marked, marked-smartypants
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/notes/speaker-view.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.661)
- **Top Global Matches:** file_cluster_12: 6.661, file_cluster_7: 9.315, file_cluster_15: 9.608
- **Magnitude:** 307.96 | **LOC:** 911 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (40.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupTimer` **(I/O & Config Routines)** (Impact: 21.1)
    * *Intent:* /** * Create the timer and clock and start updating them * at an interval. */
  * `getTimings` **(Callbacks & Closures)** (Impact: 18.1)
  * `_displayTime` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `handleStateMessage` **(I/O & Config Routines)** (Impact: 8.6)
    * *Intent:* /** * Called when the main window sends an updated state. */
  * `_updatePacing` **(Callbacks & Closures)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 34 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 98`, `args: 52`, `func_start: 25`, `class_start: 89`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 9`, `state_mutation: 58`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 12`
* *Defense:* `safety: 19`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/backgrounds.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.498)
- **Top Global Matches:** file_cluster_6: 7.498, file_cluster_8: 12.625, file_cluster_4: 13.697
- **Magnitude:** 296.7 | **LOC:** 471 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.0%), Complexity Load (formerly Cognitive Load) (56.5%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* /** * Updates the background elements to reflect the current * slide. * * all vertical slides (not j...
  * `sync` **(I/O & Config Routines)** (Impact: 35.5)
    * *Intent:* /** * Renders all of the visual properties of a slide background * based on the various background a...
  * `getContrastClass` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* /** * Returns a class name that can be applied to a slide to indicate * if it has a light or dark ba...
  * `updateParallax` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* /** * Updates the position of the parallax background based * on the current slide index. */
  * `bubbleSlideContrastClassToElement` **(Callbacks & Closures)** (Impact: 5.8)
    * *Intent:* /** * Bubble the 'has-light-background'/'has-dark-background' classes. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 34`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 59`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 15`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.000644 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 2):` color, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `react/src/components/code.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.261)
- **Top Global Matches:** file_cluster_5: 7.261, file_cluster_12: 8.524, file_cluster_7: 8.829
- **Magnitude:** 287.73 | **LOC:** 145 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (71.0%), Guard Balance (formerly Safety Score) (46.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.5%), Complexity Load (formerly Cognitive Load) (4.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 12`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`
* *Architecture:* `import: 4`
* *Defense:* `safety: 4`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` reveal-context, code, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/keyboard.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.036)
- **Top Global Matches:** file_cluster_4: 8.036, file_cluster_15: 11.786, file_cluster_6: 11.849
- **Magnitude:** 286.14 | **LOC:** 415 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (60.5%), Connectivity (formerly Api Exposure) (45.3%), Guard Balance (formerly Safety Score) (37.4%)
- **Documentation Coverage:** 16.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onDocumentKeyDown` **(Defensive Guards)** (Impact: 194.7)
    * *Intent:* /** * Handler for the document level 'keydown' event. * */
  * `addKeyBinding` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /** * Add a custom key binding with optional description to * be added to the help screen. */
  * `configure` **(State Mutators)** (Impact: 6.3)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `constructor` **(State Mutators)** (Impact: 2.1)
  * `registerKeyboardShortcut` **(State Mutators)** (Impact: 2.0)
    * *Intent:* /** * Registers a new shortcut to include in the help overlay * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 25`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 59`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `react/src/components/markdown.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_0: 7.912, file_cluster_5: 8.187, file_cluster_10: 8.25
- **Magnitude:** 264.56 | **LOC:** 223 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.0%), Concurrency Surface (formerly Concurrency) (26.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.5%), Mutation Surface (formerly State Flux) (16.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 24`, `args: 16`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 1`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 4`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` reveal-context, markdown, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/highlight/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.453)
- **Top Global Matches:** file_cluster_10: 8.453, file_cluster_9: 8.614, file_cluster_15: 9.061
- **Magnitude:** 227.48 | **LOC:** 440 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 7.759; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (58.5%), Guard Balance (formerly Safety Score) (56.1%), Concurrency Surface (formerly Concurrency) (47.2%)
- **Documentation Coverage:** 31.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scrollHighlightedLineIntoView` **(Many-Argument Workhorses)** (Impact: 18.9)
    * *Intent:* /** * Animates scrolling to the first highlighted line * in the given code block. */
  * `init` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* /** * Highlights code blocks within the given deck. * * Note that this can be called multiple times ...
  * `highlightBlock` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Highlights a code block. If the <code> node has the * 'data-line-numbers' attribute we also ge...
  * `betterTrim` **(Defensive Guards)** (Impact: 16.3)
    * *Intent:* // Function to perform a better "data-trim" on code snippets // Will slice an indentation amount on ...
  * `highlightLines` **(Defensive Guards)** (Impact: 13.7)
    * *Intent:* /** * Visually emphasize specific lines within a code block. * This only works on blocks with line n...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 57`, `args: 29`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 32`
* *Architecture:* `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 28`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 0):` highlight.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/overlay.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.616)
- **Top Global Matches:** file_cluster_4: 7.616, file_cluster_15: 10.786, file_cluster_9: 10.967
- **Magnitude:** 220.68 | **LOC:** 391 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 5.7; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Complexity Load (formerly Cognitive Load) (54.4%)
- **Documentation Coverage:** 60.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onSlidesClicked` **(Compute Cores)** (Impact: 29.2)
  * `previewMedia` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* /** * Opens a lightbox window that provides a larger view of the * given image/video. * */
  * `setState` **(Defensive Guards)** (Impact: 12.4)
  * `toggleHelp` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* /** * Open or close help overlay window. * * toggle logic and forcibly sets the desired state. True ...
  * `showHelp` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* /** * Opens an overlay window with help material. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 50`, `args: 26`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 47`
* *Architecture:* `api: 8`
* *Defense:* `safety: 13`, `doc: 6`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/search/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.227)
- **Top Global Matches:** file_cluster_6: 9.227, file_cluster_4: 11.508, file_cluster_12: 16.663
- **Magnitude:** 207.1 | **LOC:** 245 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 7.759; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Hilitor` **(Compute Cores)** (Impact: 44.4)
    * *Intent:* // Original JavaScript code by Chirp Internet: www.chirp.com.au // Please acknowledge use of this co...
  * `hiliteWords` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // recursively apply word highlighting
  * `doSearch` **(I/O & Config Routines)** (Impact: 10.4)
  * `render` **(I/O & Config Routines)** (Impact: 6.3)
  * `init` **(Callbacks & Closures)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 40`, `args: 15`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `react/src/utils/markdown.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.799)
- **Top Global Matches:** file_cluster_6: 7.799, file_cluster_4: 8.34, file_cluster_9: 14.009
- **Magnitude:** 206.88 | **LOC:** 339 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 5.639; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.4%), Connectivity (formerly Api Exposure) (56.7%), Complexity Load (formerly Cognitive Load) (43.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addAttributes` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `escapeForHTML` **(Defensive Guards)** (Impact: 19.8)
  * `addAttributeInElement` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `normalizeMarkdownSource` **(Defensive Guards)** (Impact: 13.6)
  * `serializeSignatureValue` **(Compute Cores)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 75`, `args: 26`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`
* *Architecture:* `api: 14`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.639
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01227
  * `Imports (Out-Degree: 1):` types, marked, marked-smartypants, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/zoom/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.171)
- **Top Global Matches:** file_cluster_10: 8.171, file_cluster_9: 9.029, file_cluster_15: 9.455
- **Magnitude:** 199.54 | **LOC:** 265 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 7.759; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (96.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `magnify` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* /** * Applies the CSS required to zoom in, prefers the use of CSS3 * transforms but falls back on zo...
  * `to` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /** * Zooms in on either a rectangle or HTML element. * * - element: HTML element to zoom in on * OR...
  * `init` **(Callbacks & Closures)** (Impact: 9.5)
  * `pan` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* /** * Pan the document when the mouse cursor approaches the edges * of the window. */
  * `getScrollOffset` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 19`, `args: 16`, `func_start: 10`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `api: 3`, `concurrency: 2`
* *Defense:* `safety: 12`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006135
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/printview.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.1)
- **Top Global Matches:** file_cluster_8: 9.1, file_cluster_6: 18.205, file_cluster_3: 21.039
- **Magnitude:** 182.06 | **LOC:** 239 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.2%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `activate` **(I/O & Config Routines)** (Impact: 31.5)
    * *Intent:* /** * Configures the presentation for printing to a static * PDF. */
  * `constructor` **(State Mutators)** (Impact: 1.7)
  * `isActive` **(Defensive Guards)** (Impact: 1.2)
    * *Intent:* /** * Checks if the print mode is/should be activated. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 17`, `args: 12`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 33`
* *Architecture:* `api: 4`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/plugins.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.003)
- **Top Global Matches:** file_cluster_10: 8.003, file_cluster_15: 8.392, file_cluster_11: 9.223
- **Magnitude:** 179.06 | **LOC:** 254 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (49.2%), Guard Balance (formerly Safety Score) (48.9%)
- **Documentation Coverage:** 35.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* /** * Loads reveal.js dependencies, registers and * initializes plugins. * * Plugins are direct refe...
  * `registerPlugin` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* /** * Registers a new plugin with this reveal.js instance. * * reveal.js waits for all registered pl...
  * `initPlugins` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /** * Initializes our plugins and waits for them to be ready * before proceeding. */
  * `initNextPlugin` **(Defensive Guards)** (Impact: 7.0)
    * *Intent:* // Initialize plugins serially
  * `scriptLoadedCallback` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 28`, `args: 19`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 7`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 26`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.000644 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 1):` loader
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/location.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.769)
- **Top Global Matches:** file_cluster_4: 7.769, file_cluster_6: 10.335, file_cluster_9: 13.049
- **Magnitude:** 173.14 | **LOC:** 249 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 5.7; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.5%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getIndicesFromHash` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /** * Returns the slide indices for the given hash link. * * find the indices for * */
  * `getHash` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /** * Return a hash URL that will resolve to the given slide location. * */
  * `writeURL` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* /** * Updates the page URL (hash) to reflect the current * state. * * writing the hash */
  * `readURL` **(Defensive Guards)** (Impact: 8.8)
    * *Intent:* /** * Reads the current URL (hash) and navigates accordingly. */
  * `debouncedReplaceState` **(Callbacks & Closures)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 21`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 2`
* *Defense:* `safety: 10`, `doc: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/utils/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.399)
- **Top Global Matches:** file_cluster_5: 8.399, file_cluster_12: 9.043, file_cluster_7: 9.336
- **Magnitude:** 167.06 | **LOC:** 302 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); blast radius 42.042; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.4%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deserialize` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* /** * Utility for deserializing a value. * */
  * `enterFullscreen` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* /** * Handling the fullscreen functionality via the fullscreen API * */
  * `getRemainingHeight` **(Compute Cores)** (Impact: 11.9)
    * *Intent:* /** * Returns the remaining height within the parent of the * target element. * * remaining height =...
  * `closest` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Find the closest parent that matches the given * selector. * * the parents against * * if no m...
  * `createSingletonNode` **(Many-Argument Workhorses)** (Impact: 8.0)
    * *Intent:* /** * Creates an HTML element and returns a reference to it. * If the element already exists the exi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 54`, `args: 17`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 19`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 1`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109314
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `js/controllers/controls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.156)
- **Top Global Matches:** file_cluster_4: 9.156, file_cluster_10: 10.275, file_cluster_15: 11.29
- **Magnitude:** 160.8 | **LOC:** 290 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Callbacks & Closures)** (Impact: 39.1)
    * *Intent:* /** * Updates the state of all control/navigation arrows. */
  * `configure` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `onNavigateLeftClicked` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* /** * Event handlers for navigation control buttons. */
  * `onNavigateRightClicked` **(Defensive Guards)** (Impact: 4.9)
  * `bind` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 46`, `args: 43`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 38`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 6`, `doc: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 2):` device, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/scroll.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.365)
- **Top Global Matches:** file_cluster_13: 4.365, file_cluster_2: 5.618, file_cluster_17: 6.032
- **Magnitude:** 154.43 | **LOC:** 167 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.194; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 33`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 8`, `api: 15`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` highlight.js, monokai.css, markdown.js, notes.js, reset.css, reveal.css, reveal.js, black.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/fragments.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.824)
- **Top Global Matches:** file_cluster_10: 6.824, file_cluster_15: 7.286, file_cluster_11: 7.416
- **Magnitude:** 153.1 | **LOC:** 375 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 5.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.6%), Connectivity (formerly Api Exposure) (34.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goto` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* /** * Navigate to the specified slide fragment. * * should be shown, -1 means all are invisible * fr...
  * `sort` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* * this function, so you can use the index attributes to control the * order of fragment appearance. ...
  * `configure` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `availableRoutes` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * Returns an object describing the available fragment * directions. * */
  * `sortAll` **(Callbacks & Closures)** (Impact: 2.8)
    * *Intent:* /** * Sorts and formats all of fragments in the * presentation. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 36`, `args: 18`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 11`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053727
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `react/src/components/deck.test.tsx` (TYPESCRIPT) | Magnitude: 123.14 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 392, structural_boundaries: 112, concurrency: 89, generics: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/test-dependencies.html` (HTML) | Magnitude: 39.08 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 35, structural_boundaries: 13, core_var_decl: 8, design_snake_case: 8
- `test/test-destroy.html` (HTML) | Magnitude: 80.4 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 23, core_var_decl: 19, design_snake_case: 13
- `test/test-multiple-instances.html` (HTML) | Magnitude: 59.01 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 73, structural_boundaries: 24, core_var_decl: 14, design_snake_case: 14
- `plugin/highlight/plugin.js` (JAVASCRIPT) | Magnitude: 227.48 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 222, structural_boundaries: 57, branch: 53, core_var_decl: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `js/controllers/notes.js` (JAVASCRIPT) | Magnitude: 44.54 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 55, branch: 16, structural_boundaries: 10, args: 9
- `js/controllers/focus.js` (JAVASCRIPT) | Magnitude: 39.04 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 52, args: 10, func_start: 10, branch: 8
- `plugin/notes/plugin.js` (JAVASCRIPT) | Magnitude: 144.74 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 151, branch: 34, safety: 23, structural_boundaries: 21

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/reveal.d.ts` -> Churn: **53.47%** | Cog Load: 8.3195% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/reveal.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 1432.7
- `demo.html` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 448.12
- `plugin/markdown/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 352.18
- `react/src/components/code.test.tsx` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 287.73
- `react/src/components/markdown.test.tsx` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 264.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/reveal.js` -> **Severity: 1.617** (Bridge: 0.0162 * Flux: 99.9995%)
- `js/controllers/backgrounds.js` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 100.0%)
- `js/controllers/plugins.js` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 99.9994%)
- `react/src/components/slide.tsx` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `react/src/components/code.tsx` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 94.5368%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/utils/util.ts` -> **Severity: 7.952** (Embedded: 0.1093 * Error Risk: 72.7425%)
- `js/reveal.js` -> **Severity: 5.756** (Embedded: 0.0982 * Error Risk: 58.6397%)
- `js/controllers/printview.js` -> **Severity: 4.06** (Embedded: 0.0537 * Error Risk: 75.573%)
- `js/components/playback.js` -> **Severity: 3.844** (Embedded: 0.0537 * Error Risk: 71.5456%)
- `js/controllers/backgrounds.js` -> **Severity: 3.813** (Embedded: 0.0537 * Error Risk: 70.9722%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `plugin/vite-plugin-dts.ts` -> **Severity: 1489.0** (Blast Radius: 14.89 * Doc Risk: 100.0%)
- `react/demo/src/demo-app.tsx` -> **Severity: 1078.9** (Blast Radius: 10.789 * Doc Risk: 100.0%)
- `js/reveal.js` -> **Severity: 1049.257** (Blast Radius: 44.302 * Doc Risk: 23.6842%)
- `vite.config.ts` -> **Severity: 974.282** (Blast Radius: 14.89 * Doc Risk: 65.432%)
- `react/src/components/fragment.tsx` -> **Severity: 858.4** (Blast Radius: 8.584 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2053 call pairs -- scoped 23.4%, unique 0.0%, ambiguous 5.1%, external 71.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1674 | 25.9% | 0.0% | 5.3% | 68.9% |
| typescript | 231 | 10.8% | 0.0% | 6.1% | 83.1% |
| html | 148 | 15.5% | 0.0% | 1.4% | 83.1% |

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
