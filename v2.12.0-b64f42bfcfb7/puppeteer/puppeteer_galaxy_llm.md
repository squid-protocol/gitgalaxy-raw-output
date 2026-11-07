# ARCHITECTURAL_BRIEF: puppeteer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/puppeteer/puppeteer.git` |
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
- **Scope:** 1345 analyzed artifact(s), 78722 LOC.
- **Load-bearing artifact:** `test/src/mocha-utils.ts` -- 67 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `website/versioned_docs/version-24.40.0/api/index.md` -- pulls in 223 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `test/src/network.spec.ts` at magnitude 5543.71 (structural weight, not risk).
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
| Total Artifacts | 2125 |
| Analyzed Artifacts (Scanned) | 1345 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 780 |
| Total LOC | 78722 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 63.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6854 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2419 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 24.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3282 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 89 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 675 | 0 | 50.2% |
| TYPESCRIPT | 369 | 69375 | 27.4% |
| HTML | 95 | 1256 | 7.1% |
| JAVASCRIPT | 87 | 3597 | 6.5% |
| JSON | 64 | 2698 | 4.8% |
| PLAINTEXT | 21 | 2 | 1.6% |
| YAML | 20 | 1619 | 1.5% |
| CSS | 11 | 146 | 0.8% |
| DOCKERFILE | 1 | 18 | 0.1% |
| SHELL | 1 | 10 | 0.1% |
| XML | 1 | 1 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1343 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 69%, Declarative / Non-Code 11%, Large Core Modules (3) 6%, Callbacks & Closures Files 4%, Large Core Modules (2) 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 648 | 48.2% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 694 | 51.6% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 780*

**Composition by Extension & Reason:**
- `.md`: 659x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3774 LOC)
- `.png`: 67x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.json`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 45039 LOC), 1x Excluded (Static Asset Blob without Intent: 1959 LOC)
- `.ts`: 4x Unsupported Format (.undeterminable), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')
- `.xz`: 1x Excluded (Explicitly Denied Extension: '.xz')
- `.template`: 1x Unsupported Format (.template)
- `.pem`: 1x Excluded (Unsupported Extension: '.pem')
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')
- `.js`: 1x Excluded (Saturation: Line 3 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 26.9 | 40.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 92.4 | 13.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 41.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 93.3 | 4.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 32.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 35.1 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 375 | 137 | 1 | `packages/puppeteer-core/src/api/locators/locators.ts` |
| cleanup | 296 | 103 | 0 | `test/src/launcher.spec.ts` |
| guards | 2375 | 270 | 4 | `test/src/launcher.spec.ts` |
| danger | 1883 | 220 | 2 | `test/src/page.spec.ts` |
| concurrency | 11614 | 321 | 15 | `test/src/page.spec.ts` |
| connectivity | 1954 | 284 | 4 | `packages/puppeteer-core/src/api/Page.ts` |
| io | 1519 | 202 | 2 | `packages/puppeteer-core/src/cdp/NetworkManager.test.ts` |
| crypto | 4 | 4 | 0 | `packages/ng-schematics/tools/projects.mjs` |
| ipc | 38 | 29 | 0 | `test/src/worker.spec.ts` |
| time | 107 | 42 | 0 | `test/src/page.spec.ts` |
| serialization | 89 | 48 | 0 | `tools/mocha-runner/src/utils.ts` |
| regex | 149 | 67 | 0 | `tools/docgen/src/custom_markdown_documenter.ts` |
| events | 1709 | 176 | 1 | `test/src/requestinterception-experimental.spec.ts` |
| tests | 4813 | 169 | 3 | `test/src/page.spec.ts` |
| docs | 2276 | 470 | 3 | `packages/puppeteer-core/src/api/Page.ts` |
| debt | 432 | 133 | 0 | `.github/workflows/ci.yml` |
| mutation | 8825 | 467 | 17 | `test/src/elementhandle.spec.ts` |
| dead_code | 95 | 36 | 0 | `packages/puppeteer-core/src/common/util.ts` |
| credential | 105 | 5 | 0 | `examples/puppeteer-in-browser/package-lock.json` |
| threat | 5 | 3 | 0 | `packages/puppeteer-core/src/cdp/HTTPRequest.test.ts` |
| ml_ai | 67 | 17 | 0 | `packages/puppeteer-core/src/api/ElementHandle.ts` |
| ui | 223 | 54 | 0 | `website/src/theme/SearchPage/index.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/puppeteer-core/src/cdp/NetworkManager.test.ts` (Hits: 68)
- `test/src/page.spec.ts` (Hits: 66)
- `test/src/cookies.spec.ts` (Hits: 55)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mocha-utils.ts** (`test/src/mocha-utils.ts`) — 67 inbound connections
2. **util.ts** (`packages/puppeteer-core/src/common/util.ts`) — 47 inbound connections
3. **EventEmitter.ts** (`packages/puppeteer-core/src/common/EventEmitter.ts`) — 45 inbound connections
4. **puppeteer.elementhandle.md** (`website/versioned_docs/version-24.40.0/api/puppeteer.elementhandle.md`) — 42 inbound connections
5. **Errors.ts** (`packages/puppeteer-core/src/common/Errors.ts`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.md** (`website/versioned_docs/version-24.40.0/api/index.md`) — 223 outbound dependencies
2. **puppeteer.page.md** (`website/versioned_docs/version-24.40.0/api/puppeteer.page.md`) — 138 outbound dependencies
3. **Page.ts** (`packages/puppeteer-core/src/cdp/Page.ts`) — 50 outbound dependencies
4. **puppeteer.browser.md** (`website/versioned_docs/version-24.40.0/api/puppeteer.browser.md`) — 47 outbound dependencies
5. **puppeteer.elementhandle.md** (`website/versioned_docs/version-24.40.0/api/puppeteer.elementhandle.md`) — 46 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getBidiKeyValue` **(Compute Cores)** (@ `packages/puppeteer-core/src/bidi/Input.ts`) -> Impact: **169.5** | LOC: 222
- `resolveBuildIdForBrowserTag` **(Many-Argument Workhorses)** (@ `packages/browsers/src/browser-data/browser-data.ts`) -> Impact: **109.2** | LOC: 105
  * *Intent:* /** */
- `fill` **(Many-Argument Workhorses)** (@ `packages/puppeteer-core/src/api/locators/locators.ts`) -> Impact: **67.7** | LOC: 153
- `evaluate` **(Many-Argument Workhorses)** (@ `packages/puppeteer-core/src/cdp/ExecutionContext.ts`) -> Impact: **61.7** | LOC: 154
- `getEscapedText` **(Stateful Encapsulated Methods)** (@ `tools/docgen/src/custom_markdown_documenter.ts`) -> Impact: **57.4** | LOC: 1538
- `build` **(Compute Cores)** (@ `packages/browsers/src/CLI.ts`) -> Impact: **53.5** | LOC: 306
- `SearchPageContent` **(I/O & Config Routines)** (@ `website/src/theme/SearchPage/index.js`) -> Impact: **52.5** | LOC: 390
- `getExpectationUpdates` **(Many-Argument Workhorses)** (@ `tools/mocha-runner/src/utils.ts`) -> Impact: **46.6** | LOC: 128
- `launch` **(Compute Cores)** (@ `packages/puppeteer-core/src/node/BrowserLauncher.ts`) -> Impact: **46.4** | LOC: 193
- `constructor` **(Many-Argument Workhorses)** (@ `packages/puppeteer-core/src/node/ScreenRecorder.ts`) -> Impact: **46.2** | LOC: 163
  * *Intent:* #page: Page; #process: ChildProcessWithoutNullStreams; #controller = new AbortController(); #lastFrame: Promise<readonly [Buffer, number]>; #fps: numb...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/src` | 56 | 28318.99 | 28.45% | 0.0% |
| `packages/puppeteer-core/src/cdp` | 43 | 6457.2 | 30.85% | 3.57% |
| `__monolith__` | 12 | 5303.34 | 6.95% | 0.0% |
| `packages/testserver` | 6 | 5033.52 | 0.0% | 0.0% |
| `packages/puppeteer-core/src/bidi` | 25 | 3210.32 | 33.42% | 10.77% |
| `packages/puppeteer-core/src/api` | 22 | 3120.27 | 21.63% | 5.63% |
| `test/src/cdp` | 16 | 2047.93 | 16.74% | 0.0% |
| `packages/puppeteer-core/src/common` | 42 | 1605.93 | 12.26% | 6.09% |
| `packages/puppeteer-core/src/node` | 14 | 1391.32 | 29.41% | 0.7% |
| `packages/browsers/src` | 14 | 1225.32 | 12.45% | 9.4% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/puppeteer-core/src/bidi/Target.ts` -> **100.0%** Exposure
- `.github/workflows/update-browser-pins.yml` -> **99.9972%** Exposure
- `.github/workflows/deflake.yml` -> **99.9938%** Exposure
- `.github/ISSUE_TEMPLATE/03-issue-browsers.yml` -> **99.9925%** Exposure
- `.github/ISSUE_TEMPLATE/04-issue-ng-schematics.yml` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/ng-schematics/src/schematics/ng-add/files/common/e2e/tests/utils.ts.template` -> **100.0%** Exposure
- `packages/ng-schematics/src/schematics/utils/packages.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/CallbackRegistry.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/CustomQueryHandler.ts` -> **100.0%** Exposure
- `packages/puppeteer-core/src/common/Debug.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `.github/workflows/ci.yml` -> **0** Orphaned Functions | **25** Duplicates
- `packages/puppeteer-core/src/cdp/NetworkManager.test.ts` -> **0** Orphaned Functions | **18** Duplicates
- `packages/puppeteer-core/src/common/util.ts` -> **17** Orphaned Functions | **0** Duplicates
- `packages/puppeteer-core/src/bidi/Target.ts` -> **0** Orphaned Functions | **11** Duplicates
- `packages/testserver/src/index.ts` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `website/docusaurus.config.js` -> **35.1292%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `882` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `test/src/network.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.37)
- **Top Global Matches:** file_cluster_7: 7.37, file_cluster_12: 8.61, file_cluster_5: 9.096
- **Magnitude:** 5543.71 | **LOC:** 1096 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (49.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 585
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 395`, `args: 147`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 45`
* *Architecture:* `io: 25`, `concurrency: 245`, `import: 8`
* *Defense:* `safety: 16`, `doc: 1`, `test: 224`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:fs, node:http, node:path, HTTPRequest.js, HTTPResponse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/locator.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.146)
- **Top Global Matches:** file_cluster_10: 5.146, file_cluster_2: 7.848, file_cluster_13: 8.211
- **Magnitude:** 5167.71 | **LOC:** 867 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.4%), Guard Balance (formerly Safety Score) (42.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 85 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 661
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 366`, `args: 117`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 32`
* *Architecture:* `concurrency: 236`, `import: 6`
* *Defense:* `safety: 48`, `doc: 1`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, puppeteer-core, locators.js, sinon
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/testserver/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/keyboard.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.153)
- **Top Global Matches:** file_cluster_7: 7.153, file_cluster_14: 9.838, file_cluster_12: 10.322
- **Magnitude:** 1192.67 | **LOC:** 603 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (38.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 326`, `args: 81`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 6`
* *Architecture:* `concurrency: 189`, `import: 4`
* *Defense:* `safety: 2`, `doc: 1`, `test: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/page.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.876)
- **Top Global Matches:** file_cluster_12: 8.876, file_cluster_10: 9.541, file_cluster_7: 9.877
- **Magnitude:** 1166.5 | **LOC:** 2567 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.3%), Guard Balance (formerly Safety Score) (45.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkMetrics` **(I/O & Config Routines)** (Impact: 4.0)
  * `default` **(Callbacks & Closures)** (Impact: 3.6)
  * `onResponse` **(Callbacks & Closures)** (Impact: 3.1)
  * `onResponse` **(Callbacks & Closures)** (Impact: 3.1)
  * `task` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 8 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 1068
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 1239`, `args: 404`, `func_start: 152`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 8`, `state_mutation: 20`, `duplicate_logic: 2`
* *Architecture:* `io: 66`, `api: 1`, `concurrency: 853`, `import: 15`
* *Defense:* `safety: 55`, `doc: 1`, `test: 407`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` mocha-utils.js, utils.js, es6module.js, expect, node:assert, node:fs, node:http, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/cookies.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.034)
- **Top Global Matches:** file_cluster_12: 7.034, file_cluster_10: 7.078, file_cluster_7: 8.46
- **Magnitude:** 1136.75 | **LOC:** 883 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (46.8%), Guard Balance (formerly Safety Score) (46.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Concurrency (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 270`, `args: 60`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 18`
* *Architecture:* `io: 55`, `concurrency: 232`, `import: 2`
* *Defense:* `safety: 13`, `doc: 1`, `test: 94`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mocha-utils.js, expect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/input.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.745)
- **Top Global Matches:** file_cluster_7: 7.745, file_cluster_12: 7.995, file_cluster_10: 9.376
- **Magnitude:** 984.44 | **LOC:** 446 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (45.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 8 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 228`, `args: 72`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 11`, `state_mutation: 7`
* *Architecture:* `io: 7`, `concurrency: 135`, `import: 5`
* *Defense:* `safety: 18`, `doc: 1`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:path, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/screenshot.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.073)
- **Top Global Matches:** file_cluster_12: 7.073, file_cluster_10: 7.774, file_cluster_7: 7.943
- **Magnitude:** 834.72 | **LOC:** 541 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.3%), Guard Balance (formerly Safety Score) (47.5%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 281
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 219`, `args: 48`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 10`
* *Architecture:* `api: 1`, `concurrency: 176`, `import: 4`
* *Defense:* `safety: 6`, `doc: 1`, `test: 69`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/frame.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.766)
- **Top Global Matches:** file_cluster_7: 7.766, file_cluster_12: 8.74, file_cluster_5: 8.771
- **Magnitude:** 829.8 | **LOC:** 365 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.1%), Guard Balance (formerly Safety Score) (47.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 194
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 161`, `args: 55`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 21`
* *Architecture:* `io: 5`, `concurrency: 99`, `import: 6`
* *Defense:* `safety: 7`, `doc: 1`, `test: 75`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, CDPSession.js, Frame.js, assert.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/api/ElementHandle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.6)
- **Top Global Matches:** file_cluster_0: 6.6, file_cluster_12: 8.967, file_cluster_10: 9.298
- **Magnitude:** 812.4 | **LOC:** 1667 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **15**; blast radius 4.521; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.3%), Connectivity (formerly Api Exposure) (71.8%), Guard Balance (formerly Safety Score) (54.6%)
- **Documentation Coverage:** 11.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindIsolatedHandle` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /** * A given method will have it's `this` replaced with an isolated version of * `this` when decora...
  * `select` **(Compute Cores)** (Impact: 16.3)
    * *Intent:* * * * ```ts * handle.select('blue'); // single selection * handle.select('red', 'green', 'blue'); //...
  * `clickableBox` **(Callbacks & Closures)** (Impact: 15.1)
  * `drag` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /** * Drags an element over the given element or point. * * returned. */
  * `boxModel` **(I/O & Config Routines)** (Impact: 11.7)
    * *Intent:* /** * This method returns boxes of the element, * (example: `display: none`). * * * Boxes are repres...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 399
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 326`, `args: 93`, `func_start: 65`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 5`, `state_mutation: 39`
* *Architecture:* `api: 39`, `concurrency: 224`, `import: 16`
* *Defense:* `safety: 19`, `doc: 76`, `test: 5`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.521
  * `Choke Point (Betweenness):` 0.001742 | `Ripple Effect (Closeness):` 0.043487
  * `Imports (Out-Degree: 15):` Frame.js, GetQueryHandler.js, LazyArg.js, USKeyboardLayout.js, types.js, util.js, AsyncIterableUtil.js, assert.js...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `packages/puppeteer-core/src/bidi/Page.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.091)
- **Top Global Matches:** file_cluster_4: 8.091, file_cluster_15: 8.851, file_cluster_0: 8.972
- **Magnitude:** 771.64 | **LOC:** 1213 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **38**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (86.7%), Complexity Load (formerly Cognitive Load) (80.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.5%)
- **Documentation Coverage:** 90.0709% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setViewport` **(Defensive Guards)** (Impact: 34.9)
  * `emulateNetworkConditions` **(Defensive Guards)** (Impact: 34.5)
  * `_screenshot` **(Compute Cores)** (Impact: 26.8)
  * `setUserAgent` **(Defensive Guards)** (Impact: 26.5)
    * *Intent:* /** */
  * `setCookie` **(Compute Cores)** (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 208
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 295`, `args: 100`, `func_start: 82`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`, `planned_debt: 6`
* *Architecture:* `io: 12`, `api: 58`, `concurrency: 148`, `import: 40`
* *Defense:* `safety: 44`, `doc: 11`, `test: 10`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.000265 | `Ripple Effect (Closeness):` 0.009371
  * `Imports (Out-Degree: 35):` rxjs.js, BluetoothEmulation.js, Browser.js, CDPSession.js, DeviceRequestPrompt.js, ElementHandle.js, Frame.js, HTTPResponse.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/src/cdp/prerender.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.259)
- **Top Global Matches:** file_cluster_10: 5.259, file_cluster_2: 8.001, file_cluster_13: 8.204
- **Magnitude:** 723.81 | **LOC:** 182 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (45.8%), Guard Balance (formerly Safety Score) (36.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 99`, `args: 21`, `func_start: 7`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `concurrency: 63`, `import: 4`
* *Defense:* `safety: 11`, `doc: 1`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/api/Page.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.762)
- **Top Global Matches:** file_cluster_0: 7.762, file_cluster_15: 9.624, file_cluster_10: 10.19
- **Magnitude:** 720.26 | **LOC:** 3291 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **37**; blast radius 3.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (88.8%), Guard Balance (formerly Safety Score) (52.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.5%)
- **Documentation Coverage:** 3.0612% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `screenshot` **(Compute Cores)** (Impact: 39.1)
  * `screencast` **(Compute Cores)** (Impact: 21.8)
    * *Intent:* * browser.close(); * ``` * * * * * */
  * `setDefaultScreenshotOptions` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /** */
  * `on` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* /** * Listen to page events. * * This method exists to define event typings and handle proper wireup...
  * `off` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 225
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 362`, `args: 147`, `func_start: 116`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `io: 13`, `api: 100`, `concurrency: 145`, `import: 37`
* *Defense:* `safety: 13`, `doc: 194`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.402
  * `Choke Point (Betweenness):` 0.002563 | `Ripple Effect (Closeness):` 0.044919
  * `Imports (Out-Degree: 35):` rxjs.js, HTTPRequest.js, HTTPResponse.js, Accessibility.js, Coverage.js, NetworkManager.js, Tracing.js, ConsoleMessage.js...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `packages/puppeteer-core/src/cdp/Page.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.708)
- **Top Global Matches:** file_cluster_12: 7.708, file_cluster_15: 8.03, file_cluster_0: 8.29
- **Magnitude:** 705.54 | **LOC:** 1370 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **50**; blast radius 0.537; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (80.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.0%), Connectivity (formerly Api Exposure) (64.0%)
- **Documentation Coverage:** 89.5425% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onConsoleAPI` **(Stateful Encapsulated Methods)** (Impact: 17.7)
  * `_screenshot` **(Defensive Guards)** (Impact: 15.3)
  * `setUserAgent` **(Defensive Guards)** (Impact: 15.1)
  * `exposeFunction` **(Compute Cores)** (Impact: 13.9)
  * `_create` **(Defensive Guards)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 253
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 354`, `args: 119`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `planned_debt: 3`
* *Architecture:* `io: 7`, `api: 52`, `concurrency: 188`, `import: 51`
* *Defense:* `safety: 29`, `doc: 8`, `test: 14`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.537
  * `Choke Point (Betweenness):` 0.000843 | `Ripple Effect (Closeness):` 0.024121
  * `Imports (Out-Degree: 48):` rxjs.js, BluetoothEmulation.js, Browser.js, BrowserContext.js, CDPSession.js, DeviceRequestPrompt.js, ElementHandle.js, Frame.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/src/accessibility.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.231)
- **Top Global Matches:** file_cluster_12: 6.231, file_cluster_7: 6.796, file_cluster_10: 7.907
- **Magnitude:** 676.81 | **LOC:** 1014 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.3%), Complexity Load (formerly Cognitive Load) (18.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 190
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 190`, `args: 47`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 6`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `concurrency: 150`, `import: 5`
* *Defense:* `safety: 21`, `doc: 1`, `test: 99`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:assert, Accessibility.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/browsercontext-cookies.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.932)
- **Top Global Matches:** file_cluster_10: 4.932, file_cluster_2: 6.699, file_cluster_13: 7.467
- **Magnitude:** 611.35 | **LOC:** 305 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.2%), Complexity Load (formerly Cognitive Load) (29.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Concurrency (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 67`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`
* *Architecture:* `io: 18`, `concurrency: 43`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mocha-utils.js, expect, puppeteer-core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/click.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.103)
- **Top Global Matches:** file_cluster_7: 7.103, file_cluster_14: 9.801, file_cluster_5: 10.277
- **Magnitude:** 607.82 | **LOC:** 554 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Concurrency (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 282`, `args: 75`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* `io: 3`, `concurrency: 192`, `import: 4`
* *Defense:* `safety: 6`, `doc: 1`, `test: 70`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, puppeteer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/elementhandle.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.96)
- **Top Global Matches:** file_cluster_12: 8.96, file_cluster_7: 9.021, file_cluster_5: 9.848
- **Magnitude:** 593.36 | **LOC:** 1250 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeQuad` **(Parameter Forwarders)** (Impact: 2.7)
  * `queryOne` **(Callbacks & Closures)** (Impact: 1.9)
  * `queryAll` **(Callbacks & Closures)** (Impact: 1.9)
  * `queryAll` **(Callbacks & Closures)** (Impact: 1.9)
  * `queryOne` **(Type Conversions)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 495
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 517`, `args: 135`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 15`, `state_mutation: 42`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `concurrency: 320`, `import: 9`
* *Defense:* `safety: 23`, `doc: 1`, `test: 155`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` mocha-utils.js, touch-event-utils.js, utils.js, expect, puppeteer, ElementHandle.js, disposable.js, sinon
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.557)
- **Top Global Matches:** file_cluster_12: 8.557, file_cluster_7: 8.916, file_cluster_5: 10.348
- **Magnitude:** 540.86 | **LOC:** 1156 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.6%), Complexity Load (formerly Cognitive Load) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pathToFileURL` **(Compute Cores)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 456
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 515`, `args: 155`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 3`, `state_mutation: 29`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `concurrency: 281`, `import: 7`
* *Defense:* `safety: 27`, `doc: 1`, `test: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:fs, node:path, HTTPRequest.js, ConsoleMessage.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/puppeteer-core/src/cdp/Input.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.461)
- **Top Global Matches:** file_cluster_0: 7.461, file_cluster_15: 7.973, file_cluster_10: 8.696
- **Magnitude:** 536.68 | **LOC:** 654 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.379; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.4%), Complexity Load (formerly Cognitive Load) (82.1%), Guard Balance (formerly Safety Score) (55.8%)
- **Documentation Coverage:** 93.617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keyDescriptionForString` **(Compute Cores)** (Impact: 22.4)
  * `getButtonFromPressedButtons` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* /** * This should match * https://source.chromium.org/chromium/chromium/src/+/refs/heads/main:conten...
  * `click` **(Many-Argument Workhorses)** (Impact: 11.4)
  * `type` **(Compute Cores)** (Impact: 11.3)
  * `getFlag` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 269
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 162`, `args: 52`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `state_mutation: 32`, `duplicate_logic: 5`
* *Architecture:* `api: 9`, `concurrency: 89`, `import: 7`
* *Defense:* `safety: 5`, `doc: 10`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.379
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.019898
  * `Imports (Out-Degree: 6):` CDPSession.js, ElementHandle.js, Input.js, Errors.js, USKeyboardLayout.js, assert.js, devtools-protocol
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/src/navigation.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.988)
- **Top Global Matches:** file_cluster_7: 8.988, file_cluster_12: 9.085, file_cluster_5: 10.578
- **Magnitude:** 528.6 | **LOC:** 1033 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.1%), Guard Balance (formerly Safety Score) (45.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `warningHandler` **(Callbacks & Closures)** (Impact: 1.6)
  * `warningHandler` **(Callbacks & Closures)** (Impact: 1.6)
  * `warningHandler` **(Callbacks & Closures)** (Impact: 1.6)
  * `getResponse` **(Parameter Forwarders)** (Impact: 1.6)
  * `pushState` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 447
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 373`, `args: 147`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 2`, `state_mutation: 29`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 12`, `concurrency: 257`, `import: 8`
* *Defense:* `safety: 38`, `doc: 1`, `test: 183`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:http, puppeteer, HTTPRequest.js, HTTPResponse.js, Deferred.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/launcher.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.496)
- **Top Global Matches:** file_cluster_10: 7.496, file_cluster_12: 8.46, file_cluster_7: 10.019
- **Magnitude:** 496.14 | **LOC:** 1004 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.4%), Guard Balance (formerly Safety Score) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `warningHandler` **(Callbacks & Closures)** (Impact: 1.6)
  * `targetFilter` **(Callbacks & Closures)** (Impact: 1.6)
  * `targetFilter` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 401
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 351`, `args: 101`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 34`, `planned_debt: 1`
* *Architecture:* `io: 40`, `concurrency: 256`, `import: 13`
* *Defense:* `safety: 92`, `doc: 1`, `test: 134`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:assert, node:fs, promises, node:os, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/requestinterception-experimental.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.561)
- **Top Global Matches:** file_cluster_7: 8.561, file_cluster_12: 9.003, file_cluster_5: 10.284
- **Magnitude:** 482.5 | **LOC:** 1069 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (57.5%), Complexity Load (formerly Cognitive Load) (46.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pathToFileURL` **(Compute Cores)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 395
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 477`, `args: 142`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 3`, `state_mutation: 31`
* *Architecture:* `io: 22`, `concurrency: 240`, `import: 7`
* *Defense:* `safety: 29`, `doc: 1`, `test: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, node:fs, node:path, HTTPRequest.js, ConsoleMessage.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/src/console.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.155)
- **Top Global Matches:** file_cluster_5: 8.155, file_cluster_7: 8.452, file_cluster_12: 8.771
- **Magnitude:** 474.06 | **LOC:** 330 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.8%), Complexity Load (formerly Cognitive Load) (45.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 127`, `args: 41`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `io: 7`, `concurrency: 90`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`, `test: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mocha-utils.js, utils.js, expect, ConsoleMessage.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/puppeteer-core/src/bidi/Browser.ts` (TYPESCRIPT) | Magnitude: 146.56 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 278, structural_boundaries: 97, args: 40, concurrency: 36
- `packages/puppeteer-core/src/common/PDFOptions.ts` (TYPESCRIPT) | Magnitude: 25.16 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 93, doc: 27, branch: 22, structural_boundaries: 15
- `packages/puppeteer-core/src/common/TextQueryHandler.ts` (TYPESCRIPT) | Magnitude: 4.6 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, api: 2, doc: 2
- `packages/puppeteer-core/src/bidi/HTTPRequest.ts` (TYPESCRIPT) | Magnitude: 201.72 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 278, structural_boundaries: 80, args: 35, branch: 34
- `packages/puppeteer-core/src/bidi/Dialog.ts` (TYPESCRIPT) | Magnitude: 14.04 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/assets/input/keyboard.html` (HTML) | Magnitude: 21.84 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 11, core_var_decl: 7, design_snake_case: 7
- `packages/testserver/src/index.ts` (TYPESCRIPT) | Magnitude: 251.2 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 94, args: 39, branch: 37
- `packages/puppeteer-core/src/common/BrowserConnector.ts` (TYPESCRIPT) | Magnitude: 75.88 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 48, concurrency: 25, core_var_decl: 20
- `test/src/queryhandler.spec.ts` (TYPESCRIPT) | Magnitude: 375.34 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 604, structural_boundaries: 387, concurrency: 231, test: 131
- `test/src/headful.spec.ts` (TYPESCRIPT) | Magnitude: 104.18 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 35, concurrency: 21, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/puppeteer-core/src/bidi/core/Navigation.ts` (TYPESCRIPT) | Magnitude: 39.4 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 32, args: 16, branch: 15
- `packages/puppeteer-core/src/api/BluetoothEmulation.ts` (TYPESCRIPT) | Magnitude: 16.56 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, doc: 10, api: 7
- `packages/puppeteer-core/src/common/ConnectionTransport.ts` (TYPESCRIPT) | Magnitude: 5.72 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 8, args: 4, indent_spaces: 4, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/src/cookies.spec.ts` (TYPESCRIPT) | Magnitude: 1136.75 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 807, structural_boundaries: 270, concurrency: 232, test: 94
- `test/src/bluetooth-emulation.spec.ts` (TYPESCRIPT) | Magnitude: 25.52 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 16, concurrency: 16, core_var_decl: 10
- `test/src/elementhandle.spec.ts` (TYPESCRIPT) | Magnitude: 593.36 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1085, structural_boundaries: 517, concurrency: 320, core_var_decl: 174

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `website/babel.config.js` (JAVASCRIPT) | Magnitude: 13.56 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 1, state_mutation: 1, doc: 1, decorators: 1
- `test/assets/pdf.html` (HTML) | Magnitude: 16.34 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/puppeteer-core/src/cdp/BrowserConnector.ts` (TYPESCRIPT) | Magnitude: 11.44 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 14, core_var_decl: 7, import: 6
- `test/assets/input/mouse-helper.js` (JAVASCRIPT) | Magnitude: 1.24 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 70, globals: 7, state_mutation: 6, args: 5
- `packages/browsers/src/browser-data/chromedriver.ts` (TYPESCRIPT) | Magnitude: 36.14 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, branch: 14, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tools/docgen/src/custom_markdown_documenter.ts` (TYPESCRIPT) | Magnitude: 0.13 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1409, structural_boundaries: 146, core_var_decl: 110, design_camel_case: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/puppeteer-core/src/util/util.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, doc: 1
- `packages/puppeteer-core/src/revisions.ts` (TYPESCRIPT) | Magnitude: 13.6 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 3, doc: 2, structural_boundaries: 1, safety: 1
- `packages/puppeteer-core/src/node/node.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7, import: 7, doc: 1
- `packages/puppeteer-core/src/common/common.ts` (TYPESCRIPT) | Magnitude: 52.74 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 45, api: 37, import: 37, doc: 1
- `packages/puppeteer-core/src/cdp/cdp.ts` (TYPESCRIPT) | Magnitude: 52.74 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 37, api: 37, import: 37, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/browsers/src/main.ts` (TYPESCRIPT) | Magnitude: 28.04 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 19, api: 12, import: 12
- `test/assets/detect-touch.html` (HTML) | Magnitude: 29.24 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 3, func_start: 2, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/puppeteer-core/src/bidi/Input.ts` (TYPESCRIPT) | Magnitude: 421.34 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 640, structural_boundaries: 224, branch: 139, concurrency: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/puppeteer-core/src/util/Function.ts` (TYPESCRIPT) | Magnitude: 60.08 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 31, core_var_decl: 13, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/src/proxy.spec.ts` (TYPESCRIPT) | Magnitude: 132.46 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 173, structural_boundaries: 61, concurrency: 43, core_var_decl: 33
- `test/src/evaluation.spec.ts` (TYPESCRIPT) | Magnitude: 250.5 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 575, structural_boundaries: 347, concurrency: 205, args: 132
- `packages/puppeteer-core/src/util/encoding.ts` (TYPESCRIPT) | Magnitude: 37.86 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 14, core_var_decl: 10, design_snake_case: 7
- `test/src/navigation.spec.ts` (TYPESCRIPT) | Magnitude: 528.6 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 877, structural_boundaries: 373, concurrency: 257, test: 183
- `test/src/cdp/interventionHeaders.spec.ts` (TYPESCRIPT) | Magnitude: 50.09 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 14, args: 5, closures: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tools/compare-trials.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, branch: 10, core_var_decl: 6, design_snake_case: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/puppeteer-core/src/cdp/Page.ts` -> Churn: **69.95%** | Cog Load: 80.3287% | Debt: 8.5289%
- `packages/puppeteer-core/Herebyfile.mjs` -> Churn: **67.83%** | Cog Load: 82.6202% | Debt: 0.0%
- `.github/workflows/ci.yml` -> Churn: **60.38%** | Cog Load: 8.9011% | Debt: 99.9908%
- `packages/puppeteer-core/src/bidi/Page.ts` -> Churn: **57.55%** | Cog Load: 80.207% | Debt: 9.9301%
- `.github/workflows/daily.yml` -> Churn: **55.75%** | Cog Load: 6.5401% | Debt: 99.9888%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/src/network.spec.ts` -> **Nikolay Vitkov** (100.0% isolated ownership) | Magnitude: 5543.71
- `test/src/locator.spec.ts` -> **Alex Rudenko** (100.0% isolated ownership) | Magnitude: 5167.71
- `test/src/keyboard.spec.ts` -> **Alex Rudenko** (100.0% isolated ownership) | Magnitude: 1192.67
- `test/src/cookies.spec.ts` -> **Alex Rudenko** (100.0% isolated ownership) | Magnitude: 1136.75
- `packages/puppeteer-core/src/api/ElementHandle.ts` -> **dependabot[bot]** (100.0% isolated ownership) | Magnitude: 812.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/puppeteer-core/src/api/ElementHandle.ts` -> **Severity: 0.149** (Bridge: 0.0017 * Flux: 85.331%)
- `packages/puppeteer-core/src/api/Frame.ts` -> **Severity: 0.143** (Bridge: 0.0016 * Flux: 91.7889%)
- `packages/puppeteer-core/src/cdp/Frame.ts` -> **Severity: 0.121** (Bridge: 0.0014 * Flux: 89.1293%)
- `packages/puppeteer-core/src/api/Page.ts` -> **Severity: 0.118** (Bridge: 0.0026 * Flux: 46.1815%)
- `packages/puppeteer-core/src/bidi/Frame.ts` -> **Severity: 0.094** (Bridge: 0.0011 * Flux: 82.7829%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/puppeteer-core/src/common/Errors.ts` -> **Severity: 3.478** (Embedded: 0.069 * Error Risk: 50.4286%)
- `packages/puppeteer-core/src/util/decorators.ts` -> **Severity: 3.371** (Embedded: 0.0421 * Error Risk: 80.0%)
- `packages/puppeteer-core/src/util/Deferred.ts` -> **Severity: 3.195** (Embedded: 0.0631 * Error Risk: 50.6306%)
- `packages/puppeteer-core/src/util/disposable.ts` -> **Severity: 2.922** (Embedded: 0.0513 * Error Risk: 56.9686%)
- `packages/puppeteer-core/src/common/EventEmitter.ts` -> **Severity: 2.906** (Embedded: 0.0532 * Error Risk: 54.6149%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/src/mocha-utils.ts` -> **Severity: 1461.442** (Blast Radius: 15.199 * Doc Risk: 96.1538%)
- `test/src/utils.ts` -> **Severity: 1005.5** (Blast Radius: 10.055 * Doc Risk: 100.0%)
- `test/src/golden-utils.ts` -> **Severity: 891.1** (Blast Radius: 8.911 * Doc Risk: 100.0%)
- `packages/puppeteer-core/src/util/Deferred.ts` -> **Severity: 600.86** (Blast Radius: 6.933 * Doc Risk: 86.6667%)
- `packages/testserver/src/index.ts` -> **Severity: 579.3** (Blast Radius: 5.793 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 206 literal sites + 2 sites through wrappers = 208
- **`panics_and_aborts`:** 560 literal sites + 6 sites through wrappers = 566

- `getJSON` (function, panics_and_aborts, primitive): 4 call sites in 2 files -- `packages/browsers/src/httpUtil.ts`
- `prettyPrintJSON` (function, debug_prints, primitive): 2 call sites in 1 files -- `tools/mocha-runner/src/utils.ts`
- `ScreenRecorder` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/puppeteer-core/src/environment.ts`
- `a` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test/src/stacktrace.spec.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5638 call pairs -- scoped 32.2%, unique 0.0%, ambiguous 24.7%, external 43.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 5265 | 33.8% | 0.0% | 25.5% | 40.7% |
| javascript | 322 | 8.7% | 0.0% | 14.0% | 77.3% |
| html | 48 | 14.6% | 0.0% | 0.0% | 85.4% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
