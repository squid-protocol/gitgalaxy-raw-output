# ARCHITECTURAL_BRIEF: excalidraw
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/excalidraw/excalidraw.git` |
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
- **Scope:** 840 analyzed artifact(s), 193112 LOC.
- **Load-bearing artifact:** `packages/excalidraw/types.ts` -- 122 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/excalidraw/components/App.tsx` -- pulls in 80 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.env.production` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1225 |
| Analyzed Artifacts (Scanned) | 840 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 385 |
| Total LOC | 193112 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 68.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6077 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1927 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 30.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.8507 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 131 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 597 | 140685 | 71.1% |
| CSS | 85 | 7992 | 10.1% |
| JSON | 75 | 41098 | 8.9% |
| JAVASCRIPT | 25 | 2793 | 3.0% |
| MARKDOWN | 15 | 0 | 1.8% |
| YAML | 14 | 280 | 1.7% |
| XML | 13 | 23 | 1.5% |
| PLAINTEXT | 13 | 2 | 1.5% |
| HTML | 2 | 229 | 0.2% |
| DOCKERFILE | 1 | 10 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 838 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 21%, Callbacks & Closures Files 20%, Data / Markup / Trivial 19%, Large Core Modules (3) 9%, Large Core Modules (2) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 806 | 96.0% |
| Unknown | 2 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 385*

**Composition by Extension & Reason:**
- `.woff2`: 237x Excluded (Explicitly Denied Extension: '.woff2')
- `.mdx`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `.snap`: 20x Excluded (Unsupported Extension: '.snap'), 4x Unsupported Format (.snap)
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.excalidrawlib'), 1x Unsupported Format (.undeterminable)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 5x Excluded (Explicitly Denied Extension: '.jpeg')
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 97 LOC), 1x Excluded (Machine-Generated Source Code Signature: 161 LOC), 1x Excluded (Embedded Array/Matrix Payload: 11397 commas in 1325 LOC)
- `.ttf`: 5x Excluded (Explicitly Denied Extension: '.ttf')
- `.ico`: 3x Excluded (Explicitly Denied Extension: '.ico')
- `.lock`: 3x Excluded (Unsupported Extension: '.lock')
- `.rules`: 2x Excluded (Unsupported Extension: '.rules')
- `.tsx`: 1x Excluded (Saturation: Line 43 exceeds 500 chars), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.wasm`: 2x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.5 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 26.6 | 34.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 2.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.0 | 20.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.4 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.2 | 1.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.2 | 5.8 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 998 | 220 | 3 | `packages/excalidraw/wysiwyg/textWysiwyg.test.tsx` |
| cleanup | 117 | 41 | 0 | `packages/excalidraw/components/App.tsx` |
| guards | 4053 | 401 | 12 | `packages/excalidraw/components/App.tsx` |
| danger | 1260 | 244 | 4 | `packages/excalidraw/subset/woff2/woff2-bindings.ts` |
| concurrency | 2281 | 194 | 7 | `packages/excalidraw/tests/flip.test.tsx` |
| connectivity | 3610 | 557 | 8 | `packages/excalidraw/components/icons.tsx` |
| io | 1164 | 102 | 1 | `packages/excalidraw/components/icons.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 26 | 13 | 0 | `packages/excalidraw/components/App.tsx` |
| time | 182 | 57 | 0 | `packages/excalidraw/components/TTDDialog/utils/chat.test.ts` |
| serialization | 103 | 52 | 0 | `packages/excalidraw/components/App.tsx` |
| regex | 203 | 63 | 0 | `packages/element/src/embeddable.ts` |
| events | 483 | 91 | 1 | `packages/excalidraw/components/App.tsx` |
| tests | 6405 | 111 | 10 | `packages/excalidraw/tests/history.test.tsx` |
| docs | 761 | 164 | 2 | `packages/excalidraw/types.ts` |
| debt | 412 | 144 | 1 | `packages/excalidraw/components/App.tsx` |
| mutation | 24550 | 590 | 68 | `packages/excalidraw/components/App.tsx` |
| dead_code | 124 | 36 | 0 | `packages/element/tests/resize.test.tsx` |
| credential | 59 | 13 | 0 | `packages/excalidraw/locales/ja-JP.json` |
| threat | 245 | 19 | 0 | `packages/excalidraw/locales/km-KH.json` |
| ml_ai | 941 | 121 | 2 | `packages/element/src/bounds.ts` |
| ui | 4589 | 385 | 12 | `packages/excalidraw/components/App.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/excalidraw/components/icons.tsx` (Hits: 616)
- `packages/excalidraw/components/TTDDialog/utils/TTDstreamFetch.test.ts` (Hits: 46)
- `packages/excalidraw/data/library.test.ts` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.ts** (`packages/excalidraw/types.ts`) — 122 inbound connections
2. **i18n.ts** (`packages/excalidraw/i18n.ts`) — 91 inbound connections
3. **icons.tsx** (`packages/excalidraw/components/icons.tsx`) — 89 inbound connections
4. **App.tsx** (`packages/excalidraw/components/App.tsx`) — 70 inbound connections
5. **types.ts** (`packages/element/src/types.ts`) — 56 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **App.tsx** (`packages/excalidraw/components/App.tsx`) — 80 outbound dependencies
2. **App.tsx** (`excalidraw-app/App.tsx`) — 51 outbound dependencies
3. **index.ts** (`packages/element/src/index.ts`) — 48 outbound dependencies
4. **LayerUI.tsx** (`packages/excalidraw/components/LayerUI.tsx`) — 46 outbound dependencies
5. **index.tsx** (`packages/excalidraw/index.tsx`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resizeMultipleElements` **(Many-Argument Workhorses)** (@ `packages/element/src/resizeElements.ts`) -> Impact: **255.7** | LOC: 352
- `convertToExcalidrawElements` **(Many-Argument Workhorses)** (@ `packages/element/src/transform.ts`) -> Impact: **195.2** | LOC: 301
- `generateDynamicAABBs` **(Many-Argument Workhorses)** (@ `packages/element/src/elbowArrow.ts`) -> Impact: **188.8** | LOC: 177
  * *Intent:* /** * Create dynamically resizing, always touching * bounding boxes having a minimum extent represented * by the given static bounds. */
- `updateElbowArrowPoints` **(Many-Argument Workhorses)** (@ `packages/element/src/elbowArrow.ts`) -> Impact: **176.3** | LOC: 261
  * *Intent:* /** * */
- `handleEndpointDrag` **(Many-Argument Workhorses)** (@ `packages/element/src/elbowArrow.ts`) -> Impact: **174.2** | LOC: 195
- `CommandPaletteInner` **(Compute Cores)** (@ `packages/excalidraw/components/CommandPalette/CommandPalette.tsx`) -> Impact: **171.8** | LOC: 777
- `perform` **(Many-Argument Workhorses)** (@ `packages/excalidraw/actions/actionFinalize.tsx`) -> Impact: **169.0** | LOC: 294
- `handleSegmentMove` **(Many-Argument Workhorses)** (@ `packages/element/src/elbowArrow.ts`) -> Impact: **157.5** | LOC: 240
  * *Intent:* /** * */
- `ExampleApp` **(Many-Argument Workhorses)** (@ `examples/with-script-in-browser/components/ExampleApp.tsx`) -> Impact: **148.0** | LOC: 896
- `renderElement` **(Many-Argument Workhorses)** (@ `packages/element/src/renderElement.ts`) -> Impact: **147.6** | LOC: 293

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/element/src` | 47 | 14928.82 | 24.91% | 7.01% |
| `__monolith__` | 13 | 10128.16 | 7.12% | 2.87% |
| `packages/excalidraw/components` | 134 | 5596.95 | 7.38% | 2.61% |
| `packages/excalidraw/actions` | 47 | 4840.67 | 7.87% | 4.2% |
| `packages/excalidraw/tests` | 33 | 3131.83 | 6.92% | 0.0% |
| `packages/excalidraw/subset/woff2` | 2 | 3009.84 | 62.42% | 13.37% |
| `packages/element/tests` | 22 | 2906.69 | 2.12% | 0.0% |
| `packages/excalidraw` | 37 | 2784.93 | 20.98% | 1.3% |
| `packages/excalidraw/data` | 14 | 1846.88 | 26.27% | 6.89% |
| `packages/common/src` | 21 | 1755.27 | 23.13% | 3.24% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/excalidraw/actions/actionAlign.tsx` -> **99.9006%** Exposure
- `packages/element/src/sortElements.ts` -> **68.9269%** Exposure
- `packages/excalidraw/hooks/useOutsideClick.ts` -> **62.2459%** Exposure
- `packages/excalidraw/components/AppStateObserver.ts` -> **55.4135%** Exposure
- `packages/excalidraw/actions/actionFrame.ts` -> **53.6312%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/common/debug.ts` -> **100.0%** Exposure
- `packages/common/src/appEventBus.ts` -> **100.0%** Exposure
- `packages/common/src/binary-heap.ts` -> **100.0%** Exposure
- `packages/common/src/queue.ts` -> **100.0%** Exposure
- `packages/common/src/url.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `excalidraw-app/tests/collab.test.tsx` -> **7** Orphaned Functions | **0** Duplicates
- `packages/excalidraw/charts.test.ts` -> **0** Orphaned Functions | **7** Duplicates
- `packages/element/src/visualdebug.ts` -> **6** Orphaned Functions | **0** Duplicates
- `packages/excalidraw/actions/actionAlign.tsx` -> **0** Orphaned Functions | **6** Duplicates
- `packages/element/src/delta.ts` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `dev-docs/docusaurus.config.js` -> **99.8599%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `269` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1541` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.env.production` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/subset/woff2/woff2-bindings.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.676)
- **Top Global Matches:** file_cluster_15: 7.676, file_cluster_10: 8.125, file_cluster_11: 9.159
- **Magnitude:** 2985.44 | **LOC:** 4052 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 1.53; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` **(Many-Argument Workhorses)** (Impact: 53.9)
  * `__embind_register_std_string` **(Compute Cores)** (Impact: 51.8)
  * `genericPointerToWireType` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `__embind_register_class` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `stringToUTF8Array` **(Many-Argument Workhorses)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 385 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 1281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 377`, `args: 393`, `func_start: 367`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 511`, `duplicate_logic: 2`
* *Architecture:* `io: 31`, `api: 38`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 40`, `doc: 1`, `test: 90`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.53
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.051327
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/App.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.824)
- **Top Global Matches:** file_cluster_4: 6.824, file_cluster_6: 9.41, file_cluster_12: 13.342
- **Magnitude:** 1925.08 | **LOC:** 12839 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **80**; blast radius 19.337; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (57.5%), Guard Balance (formerly Safety Score) (50.4%), Concurrency Surface (formerly Concurrency) (46.8%)
- **Documentation Coverage:** 92.6829% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleDelayedBindModeChange` **(Many-Argument Workhorses)** (Impact: 133.3)
  * `handleAppOnDrop` **(Defensive Guards)** (Impact: 43.0)
  * `maybeDragNewGenericElement` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `handleIframeLikeCenterClick` **(I/O & Config Routines)** (Impact: 37.5)
  * `isIframeLikeElementCenter` **(Stateful Encapsulated Methods)** (Impact: 32.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 62 instances
* *Concurrency (weighted view):* 235
* *State Mutation (weighted view):* 728
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 1167`, `args: 482`, `func_start: 216`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 604`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 4`
* *Architecture:* `io: 17`, `api: 62`, `concurrency: 85`, `import: 83`
* *Defense:* `safety: 441`, `doc: 32`, `immutability_locks: 18`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.337
  * `Choke Point (Betweenness):` 0.165259 | `Ripple Effect (Closeness):` 0.164298
  * `Imports (Out-Degree: 70):` actions, actionBoundText, actionCanvas, actionClipboard, actionElementLink, actionElementLock, actionFrame, actionHistory...
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `packages/element/tests/binding.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.92)
- **Top Global Matches:** file_cluster_10: 4.92, file_cluster_2: 6.423, file_cluster_13: 6.603
- **Magnitude:** 1801.06 | **LOC:** 698 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.5; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (63.6%), Guard Balance (formerly Safety Score) (36.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 77`, `args: 30`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `concurrency: 18`, `import: 11`
* *Defense:* `safety: 28`, `test: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dom, transformHandles, types, common, excalidraw, actionBoundText, i18n, api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/elbowArrow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.812)
- **Top Global Matches:** file_cluster_8: 7.812, file_cluster_3: 17.631, file_cluster_6: 19.422
- **Magnitude:** 1678.98 | **LOC:** 2310 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 1.369; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Guard Balance (formerly Safety Score) (53.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.0%), Complexity Load (formerly Cognitive Load) (26.8%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateDynamicAABBs` **(Many-Argument Workhorses)** (Impact: 188.8)
    * *Intent:* /** * Create dynamically resizing, always touching * bounding boxes having a minimum extent represen...
  * `updateElbowArrowPoints` **(Many-Argument Workhorses)** (Impact: 176.3)
    * *Intent:* /** * */
  * `handleEndpointDrag` **(Many-Argument Workhorses)** (Impact: 174.2)
  * `handleSegmentMove` **(Many-Argument Workhorses)** (Impact: 157.5)
    * *Intent:* /** * */
  * `estimateSegmentCount` **(Many-Argument Workhorses)** (Impact: 130.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 240`, `args: 87`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 92`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 3`, `import: 13`
* *Defense:* `safety: 69`, `doc: 9`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.369
  * `Choke Point (Betweenness):` 0.000611 | `Ripple Effect (Closeness):` 0.088936
  * `Imports (Out-Degree: 8):` binding, bounds, collision, distance, heading, mutateElement, typeChecks, types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/excalidraw/actions/actionDuplicateSelection.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.333)
- **Top Global Matches:** file_cluster_10: 3.333, file_cluster_2: 5.374, file_cluster_13: 6.257
- **Magnitude:** 1527.31 | **LOC:** 532 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.5; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (27.8%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 79`, `args: 41`, `func_start: 4`
* *Risk/State:* `fragile_debt: 2`
* *Architecture:* `concurrency: 6`, `import: 5`
* *Defense:* `safety: 19`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index, api, test-utils, actionDuplicateSelection, common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/element/src/binding.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.581)
- **Top Global Matches:** file_cluster_6: 6.581, file_cluster_4: 9.412, file_cluster_8: 16.591
- **Magnitude:** 1280.36 | **LOC:** 2941 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 88.2%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **16**; blast radius 2.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.3%), Connectivity (formerly Api Exposure) (71.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Guard Balance (formerly Safety Score) (54.0%)
- **Documentation Coverage:** 85.9155% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateBoundPoint` **(Many-Argument Workhorses)** (Impact: 132.2)
  * `getBindingSideMidPoint` **(Many-Argument Workhorses)** (Impact: 106.4)
  * `bindPointToSnapToElementOutline` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `snapToMid` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `avoidRectangularCorner` **(Many-Argument Workhorses)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 318`, `args: 71`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 110`
* *Architecture:* `api: 39`, `import: 20`
* *Defense:* `safety: 61`, `doc: 9`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.251
  * `Choke Point (Betweenness):` 0.004176 | `Ripple Effect (Closeness):` 0.110749
  * `Imports (Out-Degree: 12):` Scene, bounds, collision, distance, elbowArrow, heading, linearElementEditor, mutateElement...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/element/src/linearElementEditor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.023)
- **Top Global Matches:** file_cluster_6: 8.023, file_cluster_8: 9.394, file_cluster_4: 15.946
- **Magnitude:** 1196.18 | **LOC:** 2508 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **15**; blast radius 4.333; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.8%), Connectivity (formerly Api Exposure) (63.9%), Guard Balance (formerly Safety Score) (53.4%)
- **Documentation Coverage:** 87.7551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handlePointDragging` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `movePoints` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `handlePointerMove` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `handlePointerDown` **(Many-Argument Workhorses)** (Impact: 71.2)
  * `_updatePoints` **(Many-Argument Workhorses)** (Impact: 68.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 150`, `args: 55`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 98`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 30`, `import: 18`
* *Defense:* `safety: 61`, `doc: 9`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.333
  * `Choke Point (Betweenness):` 0.01242 | `Ripple Effect (Closeness):` 0.145786
  * `Imports (Out-Degree: 10):` Scene, binding, bounds, heading, mutateElement, shape, sizeHelpers, textElement...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `packages/element/src/delta.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.593)
- **Top Global Matches:** file_cluster_4: 7.593, file_cluster_0: 9.947, file_cluster_16: 11.039
- **Magnitude:** 1148.3 | **LOC:** 2067 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 1.1; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (40.9%), Connectivity (formerly Api Exposure) (39.5%)
- **Documentation Coverage:** 51.938% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filterInvisibleChanges` **(Many-Argument Workhorses)** (Impact: 79.5)
    * *Intent:* /** * Mutates `nextAppState` be filtering out state related to deleted elements. * */
  * `squash` **(Defensive Guards)** (Impact: 48.8)
  * `distinctKeysIterator` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* /** * Iterator comparing values of object properties based on the passed joining strategy. * * * WAR...
  * `calculate` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * Calculates the `Delta`s between the previous and next set of elements. * * */
  * `applyLatestChanges` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* /** * Update delta/s based on the existing elements. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 207`, `args: 100`, `func_start: 77`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 91`, `planned_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `api: 46`, `import: 16`
* *Defense:* `safety: 54`, `doc: 31`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.1
  * `Choke Point (Betweenness):` 0.000686 | `Ripple Effect (Closeness):` 0.07676
  * `Imports (Out-Degree: 9):` Scene, binding, fractionalIndex, groups, linearElementEditor, mutateElement, store, textElement...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/element/src/resizeElements.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.02)
- **Top Global Matches:** file_cluster_8: 7.02, file_cluster_6: 17.745, file_cluster_3: 19.635
- **Magnitude:** 893.26 | **LOC:** 1501 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.598; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Connectivity (formerly Api Exposure) (36.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resizeMultipleElements` **(Many-Argument Workhorses)** (Impact: 255.7)
  * `resizeSingleElement` **(Many-Argument Workhorses)** (Impact: 115.2)
  * `transformElements` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* // Returns true when transform (resizing/rotation) happened
  * `getNextMultipleWidthAndHeightFromPointer` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `rotateMultipleElements` **(Many-Argument Workhorses)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 123`, `args: 26`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`
* *Architecture:* `api: 8`, `import: 18`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.598
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.064755
  * `Imports (Out-Degree: 12):` Scene, binding, bounds, groups, linearElementEditor, mutateElement, textElement, textMeasurements...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/common/src/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.605)
- **Top Global Matches:** file_cluster_5: 7.605, file_cluster_12: 9.299, file_cluster_0: 11.075
- **Magnitude:** 779.88 | **LOC:** 1332 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 2.606; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (69.1%), Guard Balance (formerly Safety Score) (59.4%)
- **Documentation Coverage:** 76.7442% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isShallowEqual` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* /** * Returns whether object/array is shallow equal. * Considers empty object/arrays as equal (wheth...
  * `updateActiveTool` **(Defensive Guards)** (Impact: 17.2)
  * `addEventListener` **(Defensive Guards)** (Impact: 16.9)
    * *Intent:* // implem
  * `isWritableElement` **(Compute Cores)** (Impact: 16.4)
  * `step` **(Type Conversions)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 442`, `args: 126`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 67`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 96`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 37`, `doc: 28`, `immutability_locks: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.606
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.006489
  * `Imports (Out-Degree: 2):` constants, utility-types, types, types, math
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/excalidraw/snapping.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.223)
- **Top Global Matches:** file_cluster_4: 7.223, file_cluster_6: 7.753, file_cluster_9: 13.919
- **Magnitude:** 738.74 | **LOC:** 1415 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 7.804; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.3%), Connectivity (formerly Api Exposure) (58.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `snapResizingElements` **(Many-Argument Workhorses)** (Impact: 75.6)
  * `getGapSnaps` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `createGapSnapLines` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `getElementsCorners` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `getPointSnaps` **(Many-Argument Workhorses)** (Impact: 33.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 195`, `args: 47`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 94`, `planned_debt: 1`
* *Architecture:* `api: 28`, `import: 11`
* *Defense:* `safety: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.804
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.140753
  * `Imports (Out-Degree: 1):` types, common, element, types, math
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/excalidraw/renderer/interactiveScene.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.602)
- **Top Global Matches:** file_cluster_6: 6.602, file_cluster_4: 11.383, file_cluster_8: 14.634
- **Magnitude:** 724.64 | **LOC:** 2091 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 1.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.7%), Guard Balance (formerly Safety Score) (52.2%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderBindingHighlightForBindableElement_simple` **(Many-Argument Workhorses)** (Impact: 139.0)
  * `renderBindingHighlightForBindableElement_complex` **(Many-Argument Workhorses)** (Impact: 118.4)
  * `renderLinearPointHandles` **(Many-Argument Workhorses)** (Impact: 86.7)
  * `renderFocusPointIndicator` **(Defensive Guards)** (Impact: 30.0)
  * `renderSingleLinearPoint` **(Many-Argument Workhorses)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 147`, `args: 63`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 74`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 43`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.03
  * `Choke Point (Betweenness):` 0.0007 | `Ripple Effect (Closeness):` 0.074714
  * `Imports (Out-Degree: 9):` clients, renderSnaps, roundRect, scrollbars, types, textAutoResizeHandle, types, helpers...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/excalidraw/tests/elementLocking.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.809)
- **Top Global Matches:** file_cluster_10: 3.809, file_cluster_2: 5.255, file_cluster_13: 6.019
- **Magnitude:** 689.95 | **LOC:** 391 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.5; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (54.2%), Complexity Load (formerly Cognitive Load) (3.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 59`, `args: 18`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `concurrency: 10`, `import: 8`
* *Defense:* `safety: 14`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` actions, i18n, index, api, ui, test-utils, dom, common
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/excalidraw/actions/actionProperties.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.278)
- **Top Global Matches:** file_cluster_4: 7.278, file_cluster_15: 9.636, file_cluster_10: 9.7
- **Magnitude:** 597.24 | **LOC:** 2044 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.679; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Connectivity (formerly Api Exposure) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.6%), Mutation Surface (formerly State Flux) (29.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `perform` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `perform` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `getFormValue` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `perform` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `changeFontSize` **(Many-Argument Workhorses)** (Impact: 17.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 301`, `args: 141`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 29`
* *Architecture:* `api: 19`, `import: 31`
* *Defense:* `safety: 19`, `doc: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.679
  * `Choke Point (Betweenness):` 0.00554 | `Ripple Effect (Closeness):` 0.092481
  * `Imports (Out-Degree: 16):` analytics, ColorPicker, FontPicker, IconPicker, RadioSelection, Range, icons, fonts...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/element/src/renderElement.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.11)
- **Top Global Matches:** file_cluster_8: 6.11, file_cluster_6: 11.555, file_cluster_4: 20.286
- **Magnitude:** 578.62 | **LOC:** 1129 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.95; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Connectivity (formerly Api Exposure) (36.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderElement` **(Many-Argument Workhorses)** (Impact: 147.6)
  * `drawElementOnCanvas` **(Many-Argument Workhorses)** (Impact: 111.4)
  * `generateElementWithCanvas` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `generateElementCanvas` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `drawElementFromCanvas` **(Many-Argument Workhorses)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 77`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 54`, `planned_debt: 2`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.95
  * `Choke Point (Betweenness):` 0.002815 | `Ripple Effect (Closeness):` 0.10587
  * `Imports (Out-Degree: 10):` bounds, cropElement, frame, linearElementEditor, shape, textElement, textMeasurements, typeChecks...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/element/src/shape.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.01)
- **Top Global Matches:** file_cluster_6: 7.01, file_cluster_8: 11.095, file_cluster_4: 14.294
- **Magnitude:** 544.76 | **LOC:** 1235 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **19**; blast radius 4.096; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%), Connectivity (formerly Api Exposure) (39.7%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getArrowheadShapes` **(Many-Argument Workhorses)** (Impact: 91.4)
  * `_generateElementShape` **(Many-Argument Workhorses)** (Impact: 82.4)
    * *Intent:* /** * Generates the roughjs shape for given element. * * Low-level. Use `ShapeCache.generateElementS...
  * `generateRoughOptions` **(Many-Argument Workhorses)** (Impact: 47.6)
  * `getElementShape` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* /** * get the pure geometric shape of an excalidraw elementw * which is then used for hit detection ...
  * `generateElbowArrowShape` **(Many-Argument Workhorses)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 159`, `args: 31`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 10`, `import: 20`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.096
  * `Choke Point (Betweenness):` 0.008838 | `Ripple Effect (Closeness):` 0.143149
  * `Imports (Out-Degree: 8):` bounds, collision, comparisons, heading, renderElement, typeChecks, types, utils...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `packages/element/src/frame.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.466)
- **Top Global Matches:** file_cluster_4: 6.466, file_cluster_6: 10.395, file_cluster_15: 11.94
- **Magnitude:** 541.52 | **LOC:** 950 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 0.979; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Connectivity (formerly Api Exposure) (69.3%), Guard Balance (formerly Safety Score) (56.2%), Complexity Load (formerly Cognitive Load) (25.1%)
- **Documentation Coverage:** 78.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getElementsInResizingFrame` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `shouldApplyFrameClip` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `addElementsToFrame` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* /** * Retains (or repairs for target frame) the ordering invriant where children * elements come rig...
  * `filterElementsEligibleAsFrameChildren` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* // --------------------------- Frame Operations ------------------------------- /** */
  * `isElementInFrame` **(Defensive Guards)** (Impact: 21.2)
    * *Intent:* // TODO: this a huge bottleneck for large scenes, optimise // given an element, return if the elemen...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 166`, `args: 65`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 39`, `planned_debt: 2`
* *Architecture:* `api: 32`, `import: 13`
* *Defense:* `safety: 12`, `doc: 8`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.979
  * `Choke Point (Betweenness):` 0.001993 | `Ripple Effect (Closeness):` 0.086813
  * `Imports (Out-Degree: 8):` Scene, bounds, groups, mutateElement, selection, textElement, typeChecks, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/element/src/bounds.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.471)
- **Top Global Matches:** file_cluster_15: 8.471, file_cluster_0: 8.477, file_cluster_4: 8.887
- **Magnitude:** 537.58 | **LOC:** 1315 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **15**; blast radius 5.676; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.7%), Connectivity (formerly Api Exposure) (71.5%), Guard Balance (formerly Safety Score) (55.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.6%)
- **Documentation Coverage:** 80.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getElementLineSegments` **(Many-Argument Workhorses)** (Impact: 45.7)
    * *Intent:* /* * for a given element, `getElementLineSegments` returns line segments * that can be used for visu...
  * `getMinMaxXYFromCurvePathOps` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `getArrowheadPoints` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `getBounds` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `calculateBounds` **(Many-Argument Workhorses)** (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 196`, `args: 51`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `state_mutation: 51`, `planned_debt: 6`
* *Architecture:* `api: 29`, `import: 19`
* *Defense:* `safety: 7`, `doc: 6`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.676
  * `Choke Point (Betweenness):` 0.006348 | `Ripple Effect (Closeness):` 0.115107
  * `Imports (Out-Degree: 6):` linearElementEditor, shape, textElement, typeChecks, types, utils, common, utility-types...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/library.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.939)
- **Top Global Matches:** file_cluster_12: 7.939, file_cluster_10: 9.213, file_cluster_5: 9.435
- **Magnitude:** 464.18 | **LOC:** 1002 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 8.149; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.1%), Complexity Load (formerly Cognitive Load) (58.0%), Guard Balance (formerly Safety Score) (54.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateLibrary` **(Compute Cores)** (Impact: 25.8)
    * *Intent:* // NOTE this is a high-level public API (exposed on ExcalidrawAPI) with // a slight overhead (always...
  * `createLibraryUpdate` **(Compute Cores)** (Impact: 13.7)
    * *Intent:* /** * Returns { deletedItems, addedItems } maps of all added and deleted items * since last onLibrar...
  * `importLibraryFromURL` **(Defensive Guards)** (Impact: 11.6)
  * `useHandleLibrary` **(Callbacks & Closures)** (Impact: 9.2)
  * `getLibraryItems` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 156
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 154`, `args: 64`, `func_start: 35`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 60`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 15`, `concurrency: 46`, `import: 14`
* *Defense:* `safety: 32`, `doc: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.149
  * `Choke Point (Betweenness):` 0.001893 | `Ripple Effect (Closeness):` 0.1469
  * `Imports (Out-Degree: 8):` App, editor-jotai, errors, useLibraryItemSvg, i18n, types, blob, restore...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `excalidraw-app/collab/Collab.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.883)
- **Top Global Matches:** file_cluster_10: 6.883, file_cluster_12: 7.69, file_cluster_15: 8.454
- **Magnitude:** 420.42 | **LOC:** 1052 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **29**; blast radius 0.972; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.0%), Mutation Surface (formerly State Flux) (97.3%), Guard Balance (formerly Safety Score) (56.7%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initializeRoom` **(Defensive Guards)** (Impact: 15.0)
  * `constructor` **(Callbacks & Closures)** (Impact: 14.4)
  * `stopCollaboration` **(Compute Cores)** (Impact: 13.7)
  * `saveCollabRoomToFirebase` **(Defensive Guards)** (Impact: 13.4)
  * `fetchImageFilesFromFirebase` **(Callbacks & Closures)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 67
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 160`, `args: 64`, `func_start: 44`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 68`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 16`, `concurrency: 27`, `import: 33`
* *Defense:* `safety: 16`, `doc: 3`, `immutability_locks: 8`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.972
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.006273
  * `Imports (Out-Degree: 11):` app-jotai, app_constants, data, FileManager, LocalData, fileStatusStore, firebase, localStorage...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/blob.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.504)
- **Top Global Matches:** file_cluster_12: 7.504, file_cluster_5: 8.93, file_cluster_10: 10.162
- **Magnitude:** 420.42 | **LOC:** 508 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **17**; blast radius 9.929; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (91.3%), Connectivity (formerly Api Exposure) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadSceneOrLibraryFromBlob` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `getMimeType` **(Compute Cores)** (Impact: 22.4)
  * `normalizeFile` **(Defensive Guards)** (Impact: 22.4)
    * *Intent:* /** attempts to detect correct mimeType if none is set, or if an image * has an incorrect extension....
  * `resizeImageFile` **(Compute Cores)** (Impact: 11.8)
  * `ImageURLToFile` **(Defensive Guards)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 134
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 184`, `args: 37`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 19`
* *Architecture:* `io: 3`, `api: 27`, `concurrency: 44`, `import: 17`
* *Defense:* `safety: 28`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.929
  * `Choke Point (Betweenness):` 0.004936 | `Ripple Effect (Closeness):` 0.126944
  * `Imports (Out-Degree: 11):` appState, errors, scene, export, types, encode, filesystem, image...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `packages/excalidraw/components/ConvertElementTypePopup.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_6: 6.609, file_cluster_4: 9.847, file_cluster_8: 16.11
- **Magnitude:** 413.46 | **LOC:** 938 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%), Connectivity (formerly Api Exposure) (31.9%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertElementTypes` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `convertLineToElbow` **(Compute Cores)** (Impact: 42.7)
  * `Panel` **(Compute Cores)** (Impact: 38.4)
  * `convertElementType` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* /** * Converts an element to a new type, adding or removing properties as needed * so that the eleme...
  * `ConvertElementTypePopup` **(Callbacks & Closures)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 149`, `args: 40`, `func_start: 19`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 5`, `import: 21`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.882
  * `Choke Point (Betweenness):` 0.001253 | `Ripple Effect (Closeness):` 0.116806
  * `Imports (Out-Degree: 8):` analytics, editor-jotai, types, App, ConvertElementTypePopup.scss, ToolButton, icons, common...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/excalidraw/data/restore.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.652)
- **Top Global Matches:** file_cluster_6: 8.652, file_cluster_8: 11.626, file_cluster_4: 15.582
- **Magnitude:** 411.3 | **LOC:** 1029 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 2.596; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.8%), Guard Balance (formerly Safety Score) (48.8%), Connectivity (formerly Api Exposure) (43.0%)
- **Documentation Coverage:** 76.1905% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `restoreElements` **(Many-Argument Workhorses)** (Impact: 101.0)
  * `repairBinding` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `restoreAppState` **(Defensive Guards)** (Impact: 49.3)
  * `restoreElement` **(Many-Argument Workhorses)** (Impact: 24.3)
  * `repairBoundElement` **(Defensive Guards)** (Impact: 19.0)
    * *Intent:* /** * Repairs target bound element's container's boundElements array, * or removes contaienrId if co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 119`, `args: 23`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 8`, `import: 21`
* *Defense:* `safety: 49`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.596
  * `Choke Point (Betweenness):` 0.000675 | `Ripple Effect (Closeness):` 0.123563
  * `Imports (Out-Degree: 6):` appState, scene, types, types, common, utility-types, element, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/excalidraw/components/dropdownMenu/DropdownMenu.tsx` (TYPESCRIPT) | Magnitude: 27.6 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 17, import: 13, state_mutation: 10
- `packages/utils/tests/geometry.test.ts` (TYPESCRIPT) | Magnitude: 17.66 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 120, test: 43, structural_boundaries: 17, args: 12
- `packages/excalidraw/components/ColorPicker/ColorPicker.tsx` (TYPESCRIPT) | Magnitude: 55.7 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 282, structural_boundaries: 86, core_var_decl: 75, branch: 42
- `packages/common/src/colors.ts` (TYPESCRIPT) | Magnitude: 87.4 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 69, core_var_decl: 59, api: 24
- `packages/excalidraw/components/TTDDialog/common.test.ts` (TYPESCRIPT) | Magnitude: 9.48 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 15, test: 12, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/excalidraw/components/InlineIcon.tsx` (TYPESCRIPT) | Magnitude: 7.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 4, structural_boundaries: 3, branch: 2
- `packages/excalidraw/components/Section.tsx` (TYPESCRIPT) | Magnitude: 16.54 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, branch: 3, import: 3
- `packages/excalidraw/components/TTDDialog/TTDDialogInput.tsx` (TYPESCRIPT) | Magnitude: 31.68 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 45, core_var_decl: 23, branch: 15
- `packages/excalidraw/actions/actionLinearEditor.tsx` (TYPESCRIPT) | Magnitude: 73.92 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 46, core_var_decl: 27, branch: 23
- `packages/excalidraw/components/main-menu/DefaultItems.tsx` (TYPESCRIPT) | Magnitude: 150.62 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 489, core_var_decl: 132, structural_boundaries: 121, design_camel_case: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/excalidraw/components/Modal.scss` (CSS) | Magnitude: 0.26 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 112, class_start: 13, ui_framework: 10, closures: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev-docs/babel.config.js` (JAVASCRIPT) | Magnitude: 13.56 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: api: 1, state_mutation: 1, decorators: 1, dependency_injection: 1
- `packages/excalidraw/charts/index.ts` (TYPESCRIPT) | Magnitude: 15.16 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 19, import: 8, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/element/src/bounds.ts` (TYPESCRIPT) | Magnitude: 537.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 972, core_var_decl: 241, structural_boundaries: 196, branch: 149
- `packages/element/src/textElement.ts` (TYPESCRIPT) | Magnitude: 290.98 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 398, structural_boundaries: 111, branch: 76, core_var_decl: 76
- `scripts/locales-coverage-description.js` (JAVASCRIPT) | Magnitude: 38.54 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 176, core_var_decl: 16, structural_boundaries: 11, design_snake_case: 9
- `packages/excalidraw/actions/actionFrame.ts` (TYPESCRIPT) | Magnitude: 65.58 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 50, core_var_decl: 19, import: 16
- `packages/excalidraw/components/ToolButton.tsx` (TYPESCRIPT) | Magnitude: 55.74 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 176, ui_framework: 52, branch: 51, structural_boundaries: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/common/src/index.ts` (TYPESCRIPT) | Magnitude: 32.34 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, api: 17, import: 17, scientific: 1
- `packages/excalidraw/actions/index.ts` (TYPESCRIPT) | Magnitude: 47.56 | Delta: **0.215** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 31, api: 31, import: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/excalidraw/components/FilledButton.scss` (CSS) | Magnitude: 3.99 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 256, api: 73, class_start: 37, closures: 35
- `packages/excalidraw/components/Stack.tsx` (TYPESCRIPT) | Magnitude: 19.14 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 9, core_var_decl: 9, branch: 6
- `packages/excalidraw/scene/zoom.ts` (TYPESCRIPT) | Magnitude: 4.96 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 8, design_camel_case: 8, structural_boundaries: 5
- `packages/excalidraw/components/LibraryMenuControlButtons.tsx` (TYPESCRIPT) | Magnitude: 7.34 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, core_var_decl: 6, import: 3
- `packages/excalidraw/mermaid.ts` (TYPESCRIPT) | Magnitude: 6.0 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 4, core_var_decl: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/excalidraw/renderer/animation.ts` (TYPESCRIPT) | Magnitude: 63.12 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 66, branch: 13, structural_boundaries: 10, state_mutation: 7
- `packages/excalidraw/data/json.ts` (TYPESCRIPT) | Magnitude: 72.34 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 51, branch: 21, core_var_decl: 19
- `packages/excalidraw/tests/shortcuts.test.tsx` (TYPESCRIPT) | Magnitude: 38.88 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, import: 6, test: 5
- `packages/excalidraw/errors.ts` (TYPESCRIPT) | Magnitude: 67.44 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 26, api: 14, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/excalidraw/clipboard.ts` (TYPESCRIPT) | Magnitude: 404.8 | Delta: **0.174** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 468, structural_boundaries: 178, branch: 122, core_var_decl: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/excalidraw/tests/data/restore.test.ts` (TYPESCRIPT) | Magnitude: 0.05 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 873, structural_boundaries: 148, test: 134, core_var_decl: 133

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/element/tests/binding.test.tsx` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1801.06
- `packages/element/src/elbowArrow.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1678.98
- `packages/element/src/binding.ts` -> **Márk Tolmács** (88.2% isolated ownership) | Magnitude: 1280.36
- `packages/element/src/linearElementEditor.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 1196.18
- `packages/element/src/resizeElements.ts` -> **Márk Tolmács** (100.0% isolated ownership) | Magnitude: 893.26

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/excalidraw/components/App.tsx` -> **Severity: 9.494** (Bridge: 0.1653 * Flux: 57.4509%)
- `packages/element/src/Scene.ts` -> **Severity: 3.377** (Bridge: 0.0342 * Flux: 98.5907%)
- `packages/element/src/textElement.ts` -> **Severity: 1.19** (Bridge: 0.0123 * Flux: 96.8292%)
- `packages/excalidraw/components/LayerUI.tsx` -> **Severity: 1.117** (Bridge: 0.0608 * Flux: 18.3613%)
- `packages/excalidraw/fonts/Fonts.ts` -> **Severity: 1.11** (Bridge: 0.0125 * Flux: 88.9533%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/excalidraw/i18n.ts` -> **Severity: 10.596** (Embedded: 0.1767 * Error Risk: 59.9838%)
- `packages/excalidraw/types.ts` -> **Severity: 9.842** (Embedded: 0.1985 * Error Risk: 49.5926%)
- `packages/excalidraw/snapping.ts` -> **Severity: 8.341** (Embedded: 0.1408 * Error Risk: 59.2567%)
- `packages/excalidraw/components/App.tsx` -> **Severity: 8.274** (Embedded: 0.1643 * Error Risk: 50.3568%)
- `packages/excalidraw/errors.ts` -> **Severity: 8.223** (Embedded: 0.1315 * Error Risk: 62.5121%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/excalidraw/components/App.tsx` -> **Severity: 1792.209** (Blast Radius: 19.337 * Doc Risk: 92.6829%)
- `packages/excalidraw/i18n.ts` -> **Severity: 1157.1** (Blast Radius: 23.142 * Doc Risk: 50.0%)
- `packages/excalidraw/components/icons.tsx` -> **Severity: 1095.0** (Blast Radius: 10.95 * Doc Risk: 100.0%)
- `packages/excalidraw/charts/index.ts` -> **Severity: 846.8** (Blast Radius: 8.468 * Doc Risk: 100.0%)
- `packages/excalidraw/data/blob.ts` -> **Severity: 845.804** (Blast Radius: 9.929 * Doc Risk: 85.1852%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 330 literal sites + 52 sites through wrappers = 382

- `throwBindingError` (function, panics_and_aborts, primitive): 30 call sites in 1 files -- `packages/excalidraw/subset/woff2/woff2-bindings.ts`
- `abortFnPtrError` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `packages/excalidraw/subset/woff2/woff2-bindings.ts`
- `setValue` (function, panics_and_aborts, primitive): 4 call sites in 2 files -- `packages/excalidraw/subset/woff2/woff2-bindings.ts`
- `throwInternalError` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `packages/excalidraw/subset/woff2/woff2-bindings.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 10748 call pairs -- scoped 29.7%, unique 0.0%, ambiguous 26.6%, external 43.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 10577 | 30.0% | 0.0% | 27.0% | 43.0% |
| javascript | 164 | 12.2% | 0.0% | 6.7% | 81.1% |
| html | 7 | 0.0% | 0.0% | 0.0% | 100.0% |

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
