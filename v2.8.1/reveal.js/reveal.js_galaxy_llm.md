# ARCHITECTURAL_BRIEF: reveal.js
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hakimel/reveal.js.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 228 |
| Analyzed Artifacts (Scanned) | 161 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 67 |
| Total LOC | 19970 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 70.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6202 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3714 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2769 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 47 | 3792 | 29.2% |
| JAVASCRIPT | 39 | 6411 | 24.2% |
| HTML | 32 | 5633 | 19.9% |
| CSS | 26 | 3139 | 16.1% |
| MARKDOWN | 7 | 0 | 4.3% |
| JSON | 6 | 995 | 3.7% |
| PLAINTEXT | 4 | 0 | 2.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z -0.38; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Declarative / Non-Code 29%, Large Core Modules 12%, State Mutators Files 7%, Callbacks & Closures Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 150 | 93.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 6.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 67*

**Composition by Extension & Reason:**
- `.css`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.mjs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 5x Excluded (Explicitly Denied Extension: '.woff')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 1x Excluded (Massive Static Asset Blob: 3895 LOC), 1x Excluded (Massive Static Asset Blob: 3959 LOC)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wav`: 1x Excluded (Explicitly Denied Extension: '.wav')
- `.mp4`: 1x Excluded (Explicitly Denied Extension: '.mp4')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.7 | 15.7 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.4 | 33.0 | 22.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 84.7 | 18.2 | 7.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.7 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 68.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 78.9 | 9.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 70 | 22 | 1 | `react/src/components/deck.test.tsx` |
| cleanup | 101 | 25 | 1 | `js/reveal.js` |
| guards | 762 | 55 | 12 | `js/reveal.js` |
| danger | 198 | 37 | 3 | `test/test-markdown.html` |
| concurrency | 330 | 50 | 5 | `react/src/components/deck.test.tsx` |
| connectivity | 508 | 103 | 8 | `examples/auto-animate.html` |
| io | 342 | 42 | 4 | `demo.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 5 | 0 | `plugin/notes/speaker-view.html` |
| time | 59 | 14 | 0 | `plugin/notes/speaker-view.html` |
| serialization | 21 | 6 | 0 | `plugin/notes/speaker-view.html` |
| regex | 88 | 17 | 1 | `plugin/markdown/plugin.js` |
| events | 321 | 53 | 4 | `test/test.html` |
| tests | 632 | 22 | 8 | `test/test.html` |
| docs | 577 | 87 | 7 | `js/reveal.d.ts` |
| debt | 42 | 18 | 1 | `react/src/components/code.test.tsx` |
| mutation | 3873 | 106 | 66 | `js/reveal.js` |
| dead_code | 78 | 7 | 0 | `js/reveal.d.ts` |
| credential | 47 | 1 | 0 | `react/demo/package-lock.json` |
| threat | 162 | 32 | 2 | `demo.html` |
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

1. **reveal.js** (`js/reveal.js`) — 28 inbound connections
2. **util.ts** (`js/utils/util.ts`) — 12 inbound connections
3. **types.ts** (`react/src/types.ts`) — 9 inbound connections
4. **monokai.css** (`public/plugin/highlight/monokai.css`) — 8 inbound connections
5. **vite-plugin-dts.ts** (`plugin/vite-plugin-dts.ts`) — 8 inbound connections

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
  * *Intent:* /** * Handler for the document level 'keydown' event. * * @param {object} event */
- `slide` **(Many-Argument Workhorses)** (@ `js/reveal.js`) -> Impact: **94.7** | LOC: 194
  * *Intent:* /** * Steps from the current point in the presentation to the * slide which matches the specified horizontal and vertical * indices. * * @param {numbe...
- `autoAnimateElements` **(Many-Argument Workhorses)** (@ `js/controllers/autoanimate.js`) -> Impact: **57.6** | LOC: 123
  * *Intent:* /** * Creates a FLIP animation where the `to` element starts out * in the `from` element position and animates to its original * state. * * @param {HT...
- `load` **(Many-Argument Workhorses)** (@ `js/controllers/slidecontent.js`) -> Impact: **56.0** | LOC: 150
  * *Intent:* /** * Called when the given slide is within the configured view * distance. Shows the slide element and loads any content * that is set to load lazily...
- `onTouchMove` **(Compute Cores)** (@ `js/controllers/touch.js`) -> Impact: **52.6** | LOC: 90
  * *Intent:* /** * Handler for the 'touchmove' event. * * @param {object} event */
- `update` **(Compute Cores)** (@ `js/controllers/backgrounds.js`) -> Impact: **52.1** | LOC: 136
  * *Intent:* /** * Updates the background elements to reflect the current * slide. * * @param {boolean} includeAll If true, the backgrounds of * all vertical slide...
- `updateSlides` **(Compute Cores)** (@ `js/reveal.js`) -> Impact: **50.9** | LOC: 117
  * *Intent:* /** * Updates one dimension of slides by showing the slide * with the specified index. * * @param {string} selector A CSS selector that will fetch * t...
- `escapeForHTML` **(Compute Cores)** (@ `react/src/utils/markdown.ts`) -> Impact: **48.1** | LOC: 141
- `Code` **(Compute Cores)** (@ `react/src/components/code.tsx`) -> Impact: **47.1** | LOC: 94
- `addAttributes` **(Many-Argument Workhorses)** (@ `react/src/utils/markdown.ts`) -> Impact: **47.1** | LOC: 61

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `js/controllers` | 19 | 3549.36 | 44.87% | 3.69% |
| `test` | 17 | 1957.43 | 6.58% | 0.0% |
| `examples` | 13 | 1540.52 | 0.77% | 0.0% |
| `js` | 4 | 1495.77 | 19.98% | 25.0% |
| `react/src/components` | 12 | 1237.41 | 14.08% | 0.0% |
| `__monolith__` | 9 | 567.16 | 1.58% | 0.0% |
| `plugin/notes` | 4 | 479.52 | 23.59% | 0.0% |
| `plugin/markdown` | 3 | 423.08 | 25.44% | 3.7% |
| `react/src/utils` | 2 | 293.7 | 41.04% | 0.0% |
| `plugin/math` | 7 | 289.22 | 38.02% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `js/reveal.d.ts` -> **100.0%** Exposure
- `scripts/zip.js` -> **46.2676%** Exposure
- `scripts/test.js` -> **41.5929%** Exposure
- `js/controllers/location.js` -> **32.5558%** Exposure
- `js/controllers/touch.js` -> **25.4273%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `js/components/playback.js` -> **100.0%** Exposure
- `js/controllers/autoanimate.js` -> **100.0%** Exposure
- `js/controllers/backgrounds.js` -> **100.0%** Exposure
- `js/controllers/controls.js` -> **100.0%** Exposure
- `js/controllers/fragments.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `js/reveal.d.ts` -> **71** Orphaned Functions | **0** Duplicates
- `scripts/zip.js` -> **2** Orphaned Functions | **0** Duplicates
- `react/src/components/deck.test.tsx` -> **0** Orphaned Functions | **2** Duplicates
- `scripts/test.js` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `162` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `plugin/zoom/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **654.99**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.17)
- **Magnitude:** 206.94 | **LOC:** 265 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (96.3551%), Safety Score (96.1842%)
- **Heaviest Functions:** `magnify` (Many-Argument Workhorses, Impact: 23.7), `to` (Defensive Guards, Impact: 16.4), `init` (Callbacks & Closures, Impact: 9.5)

### 2. `scripts/test.js` (JAVASCRIPT) -> Cumulative Risk: **638.44**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.16)
- **Magnitude:** 85.42 | **LOC:** 98 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9993%)
- **Heaviest Functions:** `runTests` (Defensive Guards, Impact: 13.0), `startServer` (Defensive Guards, Impact: 4.8)

### 3. `plugin/markdown/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **636.72**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.09)
- **Magnitude:** 391.18 | **LOC:** 488 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.0749%), Concurrency (90.0028%)
- **Heaviest Functions:** `addAttributes` (Defensive Guards, Impact: 46.0), `slidify` (Many-Argument Workhorses, Impact: 24.1), `getSlidifyOptions` (Defensive Guards, Impact: 20.4)

### 4. `js/controllers/location.js` (JAVASCRIPT) -> Cumulative Risk: **635.85**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.49)
- **Magnitude:** 173.14 | **LOC:** 249 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (98.682%), Safety Score (88.4183%)
- **Heaviest Functions:** `getIndicesFromHash` (Compute Cores, Impact: 28.8), `getHash` (Compute Cores, Impact: 24.4), `writeURL` (Defensive Guards, Impact: 15.0)

### 5. `plugin/search/plugin.js` (JAVASCRIPT) -> Cumulative Risk: **609.33**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.60)
- **Magnitude:** 210.8 | **LOC:** 245 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.2312%)
- **Heaviest Functions:** `Hilitor` (Compute Cores, Impact: 46.2), `hiliteWords` (Compute Cores, Impact: 26.4), `doSearch` (I/O & Config Routines, Impact: 10.4)

### 6. `plugin/math/mathjax4.js` (JAVASCRIPT) -> Cumulative Risk: **594.41**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.82)
- **Magnitude:** 67.7 | **LOC:** 82 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9983%), Safety Score (94.6038%)
- **Heaviest Functions:** `init` (Callbacks & Closures, Impact: 5.6), `loadScript` (Defensive Guards, Impact: 4.4), `onload` (Callbacks & Closures, Impact: 2.6)

### 7. `plugin/math/mathjax3.js` (JAVASCRIPT) -> Cumulative Risk: **586.57**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.80)
- **Magnitude:** 61.44 | **LOC:** 78 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.4897%), Safety Score (95.1815%)
- **Heaviest Functions:** `init` (Callbacks & Closures, Impact: 5.4), `loadScript` (Defensive Guards, Impact: 4.4), `onload` (Callbacks & Closures, Impact: 2.6)

### 8. `js/components/playback.js` (JAVASCRIPT) -> Cumulative Risk: **570.01**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.44)
- **Magnitude:** 97.86 | **LOC:** 165 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.5688%)
- **Heaviest Functions:** `render` (I/O & Config Routines, Impact: 8.0), `setPlaying` (State Mutators, Impact: 6.4), `animate` (I/O & Config Routines, Impact: 5.0)

### 9. `js/controllers/slidecontent.js` (JAVASCRIPT) -> Cumulative Risk: **569.4**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.06)
- **Magnitude:** 397.62 | **LOC:** 747 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9476%), Concurrency (99.2739%), Verification (80.0%)
- **Heaviest Functions:** `load` (Many-Argument Workhorses, Impact: 56.0), `startEmbeddedContent` (Defensive Guards, Impact: 32.5), `stopEmbeddedContent` (Defensive Guards, Impact: 26.9)

### 10. `js/controllers/scrollview.js` (JAVASCRIPT) -> Cumulative Risk: **546.53**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.53)
- **Magnitude:** 498.88 | **LOC:** 924 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.4666%), Verification (80.0%)
- **Heaviest Functions:** `createPageElement` (Many-Argument Workhorses, Impact: 38.4), `syncPages` (I/O & Config Routines, Impact: 25.9), `activate` (I/O & Config Routines, Impact: 24.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `js/reveal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1438.6 | **LOC:** 2962 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.8878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `slide` **(Many-Argument Workhorses)** (Impact: 94.7)
    * *Intent:* /** * Steps from the current point in the presentation to the * slide which matches the specified ho...
  * `updateSlides` **(Compute Cores)** (Impact: 50.9)
    * *Intent:* /** * Updates one dimension of slides by showing the slide * with the specified index. * * @param {s...
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
* *Structure:* `branch: 413`, `structural_boundaries: 204`, `args: 123`, `func_start: 99`
* *Risk/State:* `state_mutation: 211`, `dead_code: 1`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 25`
* *Defense:* `safety: 136`, `doc: 81`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 101.405
  * `Choke Point (Betweenness):` 0.042571 | `Ripple Effect (Closeness):` 0.190086
  * `Imports (Out-Degree: 24):` package.json, playback, config.ts, autoanimate, backgrounds, controls, focus, fragments...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `test/test-markdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1006.14 | **LOC:** 516 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7977%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 65`, `args: 78`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 4`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `doc: 1`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/scrollview.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 498.88 | **LOC:** 924 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3959%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createPageElement` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* // Creates a new page element and appends the given slide/bg // to it.
  * `syncPages` **(I/O & Config Routines)** (Impact: 25.9)
    * *Intent:* /** * Updates our pages to match the latest configuration and * presentation size. */
  * `activate` **(I/O & Config Routines)** (Impact: 24.4)
    * *Intent:* /** * Activates the scroll view. This rearranges the presentation DOM * by—among other things—wrappi...
  * `deactivate` **(I/O & Config Routines)** (Impact: 19.9)
  * `syncScrollPosition` **(I/O & Config Routines)** (Impact: 17.8)
    * *Intent:* /** * Reads the current scroll position and updates our active * trigger states accordingly. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 59 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 67`, `args: 70`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 110`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 17`, `doc: 24`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `demo.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 448.12 | **LOC:** 701 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 180`, `args: 91`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 100`, `api: 22`, `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` highlight.js, monokai.css, markdown.js, notes.js, search.js, zoom.js, reset.css, reveal.css...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/autoanimate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 413.22 | **LOC:** 627 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `autoAnimateElements` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* /** * Creates a FLIP animation where the `to` element starts out * in the `from` element position an...
  * `getAutoAnimatableProperties` **(Defensive Guards)** (Impact: 39.6)
    * *Intent:* /** * Returns an object containing all of the properties * that can be auto-animated for the given e...
  * `run` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* /** * Runs an auto-animation between the given slides. * * @param {HTMLElement} fromSlide * @param {...
  * `findAutoAnimateMatches` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* /** * Finds matching elements between two slides. * * @param {Array} pairs List of pairs to push mat...
  * `getAutoAnimateOptions` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* /** * Returns the auto-animate options for the given element. * * @param {HTMLElement} element Eleme...
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/slidecontent.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 397.62 | **LOC:** 747 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.6653%), Tech Debt (12.2192%)
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* /** * Called when the given slide is within the configured view * distance. Shows the slide element ...
  * `startEmbeddedContent` **(Defensive Guards)** (Impact: 32.5)
    * *Intent:* /** * Start playback of any embedded content inside of * the given element. * * @param {HTMLElement}...
  * `stopEmbeddedContent` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* /** * Stop playback of any embedded content inside of * the targeted slide. * * @param {HTMLElement}...
  * `playMediaElement` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Plays the given HTMLMediaElement and handles any playback * errors, such as the browser not al...
  * `startEmbeddedIframe` **(Compute Cores)** (Impact: 17.4)
    * *Intent:* /** * "Starts" the content of an embedded iframe using the * postMessage API. * * @param {object} ev...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 64`, `args: 50`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 35`, `doc: 16`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 2):` device, util, fitty
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/markdown/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 391.18 | **LOC:** 488 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.8524%), Tech Debt (11.0865%)
**Top Internal Functions/Classes:**
  * `addAttributes` **(Defensive Guards)** (Impact: 46.0)
    * *Intent:* /** * Add attributes to the parent element of a text node, * or the element of an attribute node. */
  * `slidify` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* /** * Parses a data string into multiple slides based * on the passed in separator arguments. */
  * `getSlidifyOptions` **(Defensive Guards)** (Impact: 20.4)
    * *Intent:* /** * Inspects the given options and fills out default * values for what's not defined. */
  * `addAttributeInElement` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* /** * Check if a node value has the attributes pattern. * If yes, extract it and add that value as o...
  * `escapeForHTML` **(Compute Cores)** (Impact: 16.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 17
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 48`, `args: 28`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 7`, `import: 2`
* *Defense:* `safety: 27`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` marked, marked-smartypants
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `react/src/components/markdown.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 390.26 | **LOC:** 223 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.7355%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 24`, `args: 16`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 1`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 4`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` reveal-context, markdown, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/auto-animate.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 354.22 | **LOC:** 443 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 90`, `args: 75`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 41`, `api: 45`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` highlight.js, monokai.css, reveal.css, reveal.js, black.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `react/src/components/code.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 323.79 | **LOC:** 145 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.9875%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 15`, `args: 12`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`
* *Architecture:* `import: 4`
* *Defense:* `safety: 4`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` reveal-context, code, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/notes/speaker-view.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 314.16 | **LOC:** 911 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.8526%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setupTimer` **(Callbacks & Closures)** (Impact: 21.1)
    * *Intent:* /** * Create the timer and clock and start updating them * at an interval. */
  * `getTimings` **(Callbacks & Closures)** (Impact: 20.9)
  * `_displayTime` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `handleStateMessage` **(State Mutators)** (Impact: 8.6)
    * *Intent:* /** * Called when the main window sends an updated state. */
  * `_updatePacing` **(Callbacks & Closures)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 32
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 98`, `args: 52`, `func_start: 25`, `class_start: 89`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 9`, `state_mutation: 58`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 12`
* *Defense:* `safety: 19`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/markdown.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 296.85 | **LOC:** 176 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.9497%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `args: 17`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `io: 9`, `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` highlight.js, monokai.css, markdown.js, math.js, notes.js, reveal.css, reveal.js, white.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/backgrounds.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 296.7 | **LOC:** 471 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.5369%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* /** * Updates the background elements to reflect the current * slide. * * @param {boolean} includeAl...
  * `sync` **(Compute Cores)** (Impact: 35.5)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.00169 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 2):` color, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/keyboard.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 286.14 | **LOC:** 415 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.8766%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onDocumentKeyDown` **(Defensive Guards)** (Impact: 194.7)
    * *Intent:* /** * Handler for the document level 'keydown' event. * * @param {object} event */
  * `addKeyBinding` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /** * Add a custom key binding with optional description to * be added to the help screen. */
  * `configure` **(State Mutators)** (Impact: 6.3)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `constructor` **(State Mutators)** (Impact: 2.1)
  * `registerKeyboardShortcut` **(State Mutators)** (Impact: 2.0)
    * *Intent:* /** * Registers a new shortcut to include in the help overlay * * @param {String} key * @param {Stri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 25`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 59`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `react/src/utils/markdown.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 264.88 | **LOC:** 339 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.1033%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escapeForHTML` **(Compute Cores)** (Impact: 48.1)
  * `addAttributes` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `addAttributeInElement` **(Compute Cores)** (Impact: 25.4)
  * `normalizeMarkdownSource` **(Defensive Guards)** (Impact: 19.3)
  * `serializeSignatureValue` **(Compute Cores)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 75`, `args: 26`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`
* *Architecture:* `api: 14`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008333
  * `Imports (Out-Degree: 1):` types, marked, marked-smartypants, react
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/overlay.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 220.68 | **LOC:** 391 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onSlidesClicked` **(Compute Cores)** (Impact: 29.2)
  * `previewMedia` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* /** * Opens a lightbox window that provides a larger view of the * given image/video. * * @param {st...
  * `setState` **(Defensive Guards)** (Impact: 12.4)
  * `toggleHelp` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* /** * Open or close help overlay window. * * @param {Boolean} [override] Flag which overrides the * ...
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `plugin/search/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 210.8 | **LOC:** 245 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.8172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Hilitor` **(Compute Cores)** (Impact: 46.2)
    * *Intent:* // Original JavaScript code by Chirp Internet: www.chirp.com.au // Please acknowledge use of this co...
  * `hiliteWords` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* // recursively apply word highlighting
  * `doSearch` **(I/O & Config Routines)** (Impact: 10.4)
  * `init` **(Callbacks & Closures)** (Impact: 8.2)
  * `render` **(I/O & Config Routines)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 40`, `args: 15`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `plugin/zoom/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 206.94 | **LOC:** 265 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (64.7021%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `magnify` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* /** * Applies the CSS required to zoom in, prefers the use of CSS3 * transforms but falls back on zo...
  * `to` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /** * Zooms in on either a rectangle or HTML element. * * @param {Object} options * - element: HTML ...
  * `init` **(Callbacks & Closures)** (Impact: 9.5)
  * `destroy` **(Callbacks & Closures)** (Impact: 8.6)
  * `pan` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* /** * Pan the document when the mouse cursor approaches the edges * of the window. */
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/plugins.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 188.86 | **LOC:** 254 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1134%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* /** * Loads reveal.js dependencies, registers and * initializes plugins. * * Plugins are direct refe...
  * `registerPlugin` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* /** * Registers a new plugin with this reveal.js instance. * * reveal.js waits for all registered pl...
  * `scriptLoadedCallback` **(Defensive Guards)** (Impact: 14.2)
  * `initPlugins` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /** * Initializes our plugins and waits for them to be ready * before proceeding. */
  * `initNextPlugin` **(Defensive Guards)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 28`, `args: 19`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 8`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 26`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.00169 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 1):` loader
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/printview.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 182.06 | **LOC:** 239 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.2244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `activate` **(I/O & Config Routines)** (Impact: 31.5)
    * *Intent:* /** * Configures the presentation for printing to a static * PDF. */
  * `constructor` **(State Mutators)** (Impact: 1.7)
  * `isActive` **(Interface Declarations)** (Impact: 1.2)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 2):` constants, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/utils/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 173.46 | **LOC:** 302 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.0446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deserialize` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /** * Utility for deserializing a value. * * @param {*} value * @return {*} */
  * `enterFullscreen` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* /** * Handling the fullscreen functionality via the fullscreen API * * @see http://fullscreen.spec.w...
  * `getRemainingHeight` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* /** * Returns the remaining height within the parent of the * target element. * * remaining height =...
  * `closest` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Find the closest parent that matches the given * selector. * * @param {HTMLElement} target The...
  * `createSingletonNode` **(Many-Argument Workhorses)** (Impact: 8.4)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.162723
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `js/controllers/location.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 173.14 | **LOC:** 249 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1563%), Tech Debt (32.5558%)
**Top Internal Functions/Classes:**
  * `getIndicesFromHash` **(Compute Cores)** (Impact: 28.8)
    * *Intent:* /** * Returns the slide indices for the given hash link. * * @param {string} [hash] the hash string ...
  * `getHash` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /** * Return a hash URL that will resolve to the given slide location. * * @param {HTMLElement} [sli...
  * `writeURL` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* /** * Updates the page URL (hash) to reflect the current * state. * * @param {number} delay The time...
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
* *Risk/State:* `state_mutation: 25`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 2`
* *Defense:* `safety: 10`, `doc: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `js/controllers/controls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 166.8 | **LOC:** 290 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.5386%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(Callbacks & Closures)** (Impact: 39.1)
    * *Intent:* /** * Updates the state of all control/navigation arrows. */
  * `configure` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `onNavigateLeftClicked` **(State Mutators)** (Impact: 4.9)
    * *Intent:* /** * Event handlers for navigation control buttons. */
  * `onNavigateRightClicked` **(State Mutators)** (Impact: 4.9)
  * `render` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 46`, `args: 43`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 38`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 6`, `doc: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 2):` device, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/scroll.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 154.43 | **LOC:** 167 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 33`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 8`, `api: 15`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.599
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` highlight.js, monokai.css, markdown.js, notes.js, reset.css, reveal.css, reveal.js, black.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `js/controllers/fragments.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 153.1 | **LOC:** 375 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2727%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `goto` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* /** * Navigate to the specified slide fragment. * * @param {?number} index The index of the fragment...
  * `sort` **(Callbacks & Closures)** (Impact: 11.0)
    * *Intent:* * this function, so you can use the index attributes to control the * order of fragment appearance. ...
  * `configure` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* /** * Called when the reveal.js config is updated. */
  * `availableRoutes` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* /** * Returns an object describing the available fragment * directions. * * @return {{prev: boolean,...
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.114418
  * `Imports (Out-Degree: 1):` util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `js/reveal.d.ts` -> Churn: **53.47%** | Cog Load: 8.3195% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `js/reveal.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 1438.6
- `demo.html` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 448.12
- `plugin/markdown/plugin.js` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 391.18
- `react/src/components/markdown.test.tsx` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 390.26
- `react/src/components/code.test.tsx` -> **Hakim El Hattab** (100.0% isolated ownership) | Magnitude: 323.79

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `js/reveal.js` -> **Severity: 4.257** (Bridge: 0.0426 * Flux: 99.9995%)
- `react/src/components/slide.tsx` -> **Severity: 0.205** (Bridge: 0.0021 * Flux: 100.0%)
- `js/controllers/backgrounds.js` -> **Severity: 0.169** (Bridge: 0.0017 * Flux: 100.0%)
- `js/controllers/plugins.js` -> **Severity: 0.169** (Bridge: 0.0017 * Flux: 99.9994%)
- `react/src/components/fragment.tsx` -> **Severity: 0.096** (Bridge: 0.0011 * Flux: 87.3543%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `js/utils/util.ts` -> **Severity: 15.532** (Embedded: 0.1627 * Error Risk: 95.4477%)
- `js/reveal.js` -> **Severity: 14.156** (Embedded: 0.1901 * Error Risk: 74.472%)
- `js/controllers/printview.js` -> **Severity: 11.144** (Embedded: 0.1144 * Error Risk: 97.4005%)
- `js/components/playback.js` -> **Severity: 10.935** (Embedded: 0.1144 * Error Risk: 95.5688%)
- `js/controllers/backgrounds.js` -> **Severity: 10.791** (Embedded: 0.1144 * Error Risk: 94.3129%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `plugin/vite-plugin-dts.ts` -> **Severity: 2807.2** (Blast Radius: 28.072 * Doc Risk: 100.0%)
- `js/reveal.js` -> **Severity: 2558.813** (Blast Radius: 101.405 * Doc Risk: 25.2336%)
- `react/demo/src/demo-app.tsx` -> **Severity: 925.8** (Blast Radius: 9.258 * Doc Risk: 100.0%)
- `react/src/components/fragment.tsx` -> **Severity: 704.0** (Blast Radius: 7.04 * Doc Risk: 100.0%)
- `react/src/components/slide.tsx` -> **Severity: 704.0** (Blast Radius: 7.04 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
