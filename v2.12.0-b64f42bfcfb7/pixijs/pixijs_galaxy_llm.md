# ARCHITECTURAL_BRIEF: pixijs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pixijs/pixijs.git` |
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
- **Scope:** 1575 analyzed artifact(s), 114566 LOC.
- **Load-bearing artifact:** `tests/visual/types.ts` -- 354 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/rendering/index.ts` -- pulls in 236 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 3149 |
| Analyzed Artifacts (Scanned) | 1575 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1574 |
| Total LOC | 114566 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 50.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5454 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1913 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.0785 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 94 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1394 | 108470 | 88.5% |
| MARKDOWN | 57 | 0 | 3.6% |
| GLSL | 41 | 888 | 2.6% |
| JSON | 26 | 1325 | 1.7% |
| YAML | 19 | 455 | 1.2% |
| JAVASCRIPT | 16 | 2738 | 1.0% |
| XML | 11 | 1 | 0.7% |
| PLAINTEXT | 8 | 1 | 0.5% |
| HTML | 2 | 21 | 0.1% |
| CSS | 1 | 667 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1574 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 21%, Large Core Modules 18%, Data / Markup / Trivial 13%, Many-Argument Workhorses Files 11%, Large Core Modules (3) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1508 | 95.7% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 64 | 4.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1574*

**Composition by Extension & Reason:**
- `.png`: 1438x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 17x Excluded (Explicitly Denied Extension: '.jpg')
- `.wgsl`: 10x Unsupported Format (.wgsl), 5x Excluded (Unsupported Extension: '.wgsl')
- `.dds`: 13x Excluded (Binary Format Detected), 2x Excluded (Unsupported Extension: '.dds')
- `.fnt`: 10x Unsupported Format (.fnt), 3x Excluded (Unsupported Extension: '.fnt')
- `.ktx`: 9x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.ktx')
- `.webp`: 9x Excluded (Explicitly Denied Extension: '.webp')
- `.ts`: 2x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 88 exceeds 500 chars)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 32765 LOC), 1x Excluded (Static Asset Blob without Intent: 2084 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 7x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff2`: 4x Excluded (Explicitly Denied Extension: '.woff2')
- `.mp4`: 3x Excluded (Explicitly Denied Extension: '.mp4')
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 39.1 | 51.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.9 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.0 | 8.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.6 | 20.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 864 | 271 | 1 | `src/color/Color.ts` |
| cleanup | 532 | 161 | 1 | `src/rendering/renderers/shared/texture/__tests__/ExternalSource.test.ts` |
| guards | 2856 | 463 | 5 | `transcoders/basis/basis_transcoder.js` |
| danger | 1180 | 277 | 1 | `src/unsafe-eval/uniforms/uniformSyncFunctions.ts` |
| concurrency | 2631 | 636 | 4 | `src/assets/__tests__/Assets.test.ts` |
| connectivity | 5476 | 1110 | 9 | `src/rendering/index.ts` |
| io | 1270 | 179 | 1 | `src/utils/__tests__/path.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 27 | 13 | 0 | `src/assets/loader/workers/WorkerManager.ts` |
| time | 115 | 75 | 0 | `src/rendering/renderers/shared/__tests__/GCSystem.test.ts` |
| serialization | 11 | 5 | 0 | `scripts/plugins/typedoc-plugin-stackblitz.mjs` |
| regex | 178 | 73 | 0 | `scripts/plugins/typedoc-plugin-stackblitz.mjs` |
| events | 846 | 183 | 1 | `src/events/__tests__/EventSystem.test.ts` |
| tests | 7565 | 196 | 5 | `src/scene/container/__tests__/Container.test.ts` |
| docs | 5210 | 708 | 10 | `src/scene/container/Container.ts` |
| debt | 278 | 137 | 0 | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| mutation | 28518 | 1340 | 43 | `transcoders/basis/basis_transcoder.js` |
| dead_code | 714 | 424 | 1 | `src/scene/container/__tests__/Container.Culling.test.ts` |
| credential | 7 | 4 | 0 | `src/utils/__tests__/path.test.ts` |
| threat | 101 | 84 | 0 | `src/assets/__tests__/Assets.test.ts` |
| ml_ai | 962 | 197 | 1 | `examples/graphics_dynamic.ts` |
| ui | 112 | 20 | 0 | `scripts/plugins/typedoc-custom.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/utils/__tests__/path.test.ts` (Hits: 401)
- `src/utils/path.ts` (Hits: 228)
- `src/scene/graphics/shared/__tests__/SVGParser.test.ts` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.ts** (`tests/visual/types.ts`) — 354 inbound connections
2. **Extensions.ts** (`src/extensions/Extensions.ts`) — 193 inbound connections
3. **Container.ts** (`src/scene/container/Container.ts`) — 107 inbound connections
4. **Texture.ts** (`src/rendering/renderers/shared/texture/Texture.ts`) — 96 inbound connections
5. **types.ts** (`src/rendering/renderers/types.ts`) — 80 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/rendering/index.ts`) — 236 outbound dependencies
2. **index.ts** (`src/scene/index.ts`) — 192 outbound dependencies
3. **index.ts** (`src/filters/index.ts`) — 40 outbound dependencies
4. **index.ts** (`src/assets/index.ts`) — 37 outbound dependencies
5. **Container.ts** (`src/scene/container/Container.ts`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `wordWrapTaggedLines` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **163.3** | LOC: 303
  * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining style information. */
- `getBitmapTextLayout` **(Many-Argument Workhorses)** (@ `src/scene/text-bitmap/utils/getBitmapTextLayout.ts`) -> Impact: **152.8** | LOC: 284
  * *Intent:* /** */
- `renderChildren` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/svg/SVGParser.ts`) -> Impact: **143.7** | LOC: 236
  * *Intent:* /** * Recursively renders SVG elements and their children. * Handles styling inheritance and different SVG shape types. */
- `buildLine` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> Impact: **130.7** | LOC: 391
  * *Intent:* /** * Builds a line to draw using the polygon method. */
- `execute` **(Many-Argument Workhorses)** (@ `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`) -> Impact: **119.6** | LOC: 244
- `recursive` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> Impact: **116.7** | LOC: 187
  * *Intent:* // eslint-disable-next-line max-params
- `measureTaggedText` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **105.3** | LOC: 186
  * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line metrics. */
- `_renderTaggedTextToCanvas` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/CanvasTextGenerator.ts`) -> Impact: **103.8** | LOC: 264
  * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. */
- `execute` **(Many-Argument Workhorses)** (@ `src/rendering/batcher/canvas/CanvasBatchAdaptor.ts`) -> Impact: **89.5** | LOC: 196
- `canvasTaggedTextSplitFromRuns` **(Many-Argument Workhorses)** (@ `src/scene/text/utils/canvasTextSplit.ts`) -> Impact: **87.6** | LOC: 187

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 5 | 5048.44 | 0.48% | 0.0% |
| `examples` | 87 | 3110.56 | 34.12% | 0.0% |
| `transcoders/basis` | 1 | 2308.08 | 95.98% | 18.97% |
| `src/scene/container/__tests__` | 32 | 2000.36 | 3.54% | 0.0% |
| `src/events` | 14 | 1776.18 | 11.26% | 1.24% |
| `src/scene/graphics/shared` | 7 | 1362.42 | 18.06% | 5.62% |
| `src/scene/graphics/shared/buildCommands` | 12 | 1318.58 | 36.22% | 0.83% |
| `src/scene/container` | 8 | 1078.2 | 18.87% | 4.62% |
| `src/scene/graphics/shared/path` | 3 | 1033.76 | 38.33% | 7.08% |
| `src/scene/text/canvas/utils` | 7 | 1003.99 | 31.07% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **100.0%** Exposure
- `src/math-extras/MathExtraMixins.d.ts` -> **100.0%** Exposure
- `types/Temp.d.ts` -> **100.0%** Exposure
- `src/app/ApplicationMixins.d.ts` -> **99.9447%** Exposure
- `scripts/jest/jest-snapshot-resolver.js` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure
- `scripts/utils/autoGenerateUnsafeEvalFunctions.ts` -> **100.0%** Exposure
- `scripts/utils/bump.mts` -> **100.0%** Exposure
- `src/app/ResizePlugin.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/math-extras/MathExtraMixins.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `transcoders/basis/basis_transcoder.js` -> **10** Orphaned Functions | **0** Duplicates
- `src/scene/sprite-animated/__tests__/AnimatedSprite.test.ts` -> **0** Orphaned Functions | **8** Duplicates
- `src/events/__tests__/EventSystem.test.ts` -> **3** Orphaned Functions | **3** Duplicates
- `src/app/ApplicationMixins.d.ts` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1160` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `transcoders/basis/basis_transcoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.531)
- **Top Global Matches:** file_cluster_12: 7.531, file_cluster_7: 10.33, file_cluster_15: 10.335
- **Magnitude:** 2308.08 | **LOC:** 1265 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.264; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.0%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` **(Defensive Guards)** (Impact: 50.3)
  * `__embind_register_std_string` **(Defensive Guards)** (Impact: 49.7)
  * `genericPointerToWireType` **(Defensive Guards)** (Impact: 38.0)
  * `__embind_register_class` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `stringToUTF8Array` **(Compute Cores)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 360 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 1189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 484`, `structural_boundaries: 394`, `args: 220`, `func_start: 194`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 4`, `state_mutation: 469`, `unreferenced_by_name: 10`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 198`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/events/EventBoundary.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.332)
- **Top Global Matches:** file_cluster_4: 6.332, file_cluster_6: 7.411, file_cluster_16: 13.616
- **Magnitude:** 844.22 | **LOC:** 1487 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 0.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.0%), Complexity Load (formerly Cognitive Load) (39.3%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 5.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hitTestMoveRecursive` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `mapPointerMove` **(Compute Cores)** (Impact: 57.6)
    * *Intent:* /** * Maps the upstream `pointermove` to downstream `pointerout`, `pointerover`, and `pointermove` e...
  * `hitTestRecursive` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* /** * can assume that `pruneFn` failed to prune the container. * cannot pass the hit test. It is use...
  * `mapPointerUp` **(Compute Cores)** (Impact: 41.2)
    * *Intent:* /** * Maps the upstream `pointerup` event to downstream `pointerup`, `pointerupoutside`, * and `clic...
  * `propagate` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /** * target `e.target`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 142`, `args: 37`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 144`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 13`, `import: 12`
* *Defense:* `safety: 12`, `doc: 43`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.727
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.007706
  * `Imports (Out-Degree: 11):` Point, Renderable, Container, warn, EventBoundaryTypes, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/rendering/renderers/__tests__/Extract.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.101)
- **Top Global Matches:** file_cluster_10: 5.101, file_cluster_2: 6.865, file_cluster_13: 7.359
- **Magnitude:** 636.54 | **LOC:** 477 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.264; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.0%), Mutation Surface (formerly State Flux) (19.0%), Complexity Load (formerly Cognitive Load) (17.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 73`, `args: 28`, `func_start: 23`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `concurrency: 58`, `import: 7`
* *Defense:* `safety: 7`, `test: 84`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` init, WebGLRenderer, ExtractSystem, RenderTexture, Texture, @test-utils, maths, scene...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/graphics/shared/GraphicsContext.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.815)
- **Top Global Matches:** file_cluster_15: 5.815, file_cluster_16: 7.498, file_cluster_11: 7.546
- **Magnitude:** 579.68 | **LOC:** 1285 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **19**; blast radius 2.148; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (83.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 3.7383% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `texture` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `containsPoint` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* /** * Check to see if a point is contained within this geometry. */
  * `fill` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `destroy` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * Destroys the GraphicsData object. * have been set to that value * context.destroy(); * context...
  * `setTransform` **(Many-Argument Workhorses)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 100`, `args: 57`, `func_start: 57`, `class_start: 4`
* *Risk/State:* `state_mutation: 89`, `planned_debt: 6`
* *Architecture:* `io: 26`, `api: 68`, `import: 19`
* *Defense:* `safety: 8`, `doc: 85`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.148
  * `Choke Point (Betweenness):` 0.007967 | `Ripple Effect (Closeness):` 0.090692
  * `Imports (Out-Degree: 18):` Color, Matrix, Point, PointData, GCSystem, Shader, Texture, uid...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/path/GraphicsPath.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.404)
- **Top Global Matches:** file_cluster_15: 5.404, file_cluster_12: 7.192, file_cluster_11: 7.574
- **Magnitude:** 555.2 | **LOC:** 863 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **9**; blast radius 1.383; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 6.8966% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transform` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* /** * Applies a transformation matrix to all drawing instructions within the `GraphicsPath`. * This ...
  * `star` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* * (distance from the center to the inner points between the outer points). * If not provided, defaul...
  * `getLastPoint` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /** * Retrieves the last point from the current drawing instructions in the `GraphicsPath`. * This m...
  * `bezierCurveToShort` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /** * Adds a cubic Bezier curve to the path. * It requires two points: the second control point and ...
  * `quadraticCurveToShort` **(Many-Argument Workhorses)** (Impact: 11.7)
    * *Intent:* /** * Adds a quadratic curve to the path. It uses the previous point as the control point. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 67`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 47`, `import: 9`
* *Defense:* `safety: 2`, `doc: 31`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.383
  * `Choke Point (Betweenness):` 0.001282 | `Ripple Effect (Closeness):` 0.085852
  * `Imports (Out-Degree: 9):` Matrix, Point, PointData, uid, warn, Bounds, parseSVGPath, ShapePath...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/container/Container.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.74)
- **Top Global Matches:** file_cluster_15: 6.74, file_cluster_11: 7.056, file_cluster_12: 7.708
- **Magnitude:** 538.5 | **LOC:** 2142 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **107** in-repo importer(s); it depends on **31**; blast radius 16.097; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (28.3%)
- **Documentation Coverage:** 23.9437% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateTransform` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* */
  * `addChild` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* * container.addChild(sprite); * * // Add multiple children * container.addChild(background, player, ...
  * `destroy` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* /** * Removes all internal references and listeners as well as removes children from the display lis...
  * `setSize` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /** * Sets the size of the container to the specified width and height. * This is more efficient tha...
  * `removeChild` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* * const removed = container.removeChild(sprite); * * // Remove multiple children * const bg = contai...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 117`, `args: 56`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 68`, `import: 32`
* *Defense:* `safety: 14`, `doc: 115`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.097
  * `Choke Point (Betweenness):` 0.022641 | `Ripple Effect (Closeness):` 0.150077
  * `Imports (Out-Degree: 30):` Color, cullingMixin, Extensions, Matrix, Size, const, ObservablePoint, PointData...
  * `Imported By (In-Degree: 107):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/utils/measureTaggedText.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.6)
- **Top Global Matches:** file_cluster_8: 5.6, file_cluster_6: 12.546, file_cluster_4: 21.209
- **Magnitude:** 492.06 | **LOC:** 633 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.366; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (40.4%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wordWrapTaggedLines` **(Many-Argument Workhorses)** (Impact: 163.3)
    * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining...
  * `measureTaggedText` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line met...
  * `tokenizeTaggedRuns` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Tokenizes an array of TextStyleRuns into individual styled tokens. * Each token is a word, spa...
  * `getWordGroupWidth` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* // Helper to calculate the total width of a word group starting at index // A word group is a sequen...
  * `measureTokenWidth` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 33`, `args: 9`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 6`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.366
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02198
  * `Imports (Out-Degree: 5):` ICanvasRenderingContext2D, TextStyle, parseTaggedText, textTokenization, types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/events/EventSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.053)
- **Top Global Matches:** file_cluster_4: 6.053, file_cluster_6: 9.927, file_cluster_12: 11.59
- **Magnitude:** 487.82 | **LOC:** 1168 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 0.745; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (47.0%), Connectivity (formerly Api Exposure) (38.0%)
- **Documentation Coverage:** 4.878% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_normalizeToPointerData` **(Compute Cores)** (Impact: 64.6)
    * *Intent:* /** * Ensures that the original event object contains all data that a regular pointer event would ha...
  * `setCursor` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* * * // Using callback-based cursor * app.renderer.events.cursorStyles.dynamic = (mode) => { * docume...
  * `_addEvents` **(I/O & Config Routines)** (Impact: 13.2)
  * `_removeEvents` **(I/O & Config Routines)** (Impact: 12.8)
  * `_onPointerDown` **(Stateful Encapsulated Methods)** (Impact: 11.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 83`, `args: 22`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 124`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 6`, `doc: 44`, `immutability_locks: 6`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.745
  * `Choke Point (Betweenness):` 0.000911 | `Ripple Effect (Closeness):` 0.007206
  * `Imports (Out-Degree: 11):` Extensions, PointData, System, types, EventBoundary, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/scene/container/bounds/Bounds.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.264)
- **Top Global Matches:** file_cluster_15: 6.264, file_cluster_11: 6.78, file_cluster_16: 8.169
- **Magnitude:** 474.56 | **LOC:** 1017 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **2**; blast radius 7.886; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.0%), Guard Balance (formerly Safety Score) (82.5%), Complexity Load (formerly Cognitive Load) (45.6%)
- **Documentation Coverage:** 5.3571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addFrame` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* * // Add transformed frame * const matrix = new Matrix() * .translate(50, 50) * .rotate(Math.PI / 4)...
  * `applyMatrix` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* * Applies a transformation matrix to the bounds, updating its coordinates. * Transforms all corners ...
  * `addVertexData` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* * .translate(50, 50) * .rotate(Math.PI / 4); * bounds.addVertexData(vertices, 0, 6, matrix); * * // ...
  * `fitBounds` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* * ```ts * const bounds = new Bounds(0, 0, 200, 200); * // Fit to specific coordinates * bounds.fitBo...
  * `containsPoint` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* * // Basic point check * console.log(bounds.containsPoint(50, 50)); // true * console.log(bounds.con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `api: 29`, `import: 2`
* *Defense:* `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.886
  * `Choke Point (Betweenness):` 0.000115 | `Ripple Effect (Closeness):` 0.15906
  * `Imports (Out-Degree: 2):` Matrix, Rectangle
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/CanvasTextGenerator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.12)
- **Top Global Matches:** file_cluster_8: 6.12, file_cluster_6: 16.849, file_cluster_3: 20.019
- **Magnitude:** 472.34 | **LOC:** 785 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.0%), Guard Balance (formerly Safety Score) (63.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_renderTaggedTextToCanvas` **(Many-Argument Workhorses)** (Impact: 103.8)
    * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. */
  * `_renderTextToCanvas` **(Many-Argument Workhorses)** (Impact: 84.5)
    * *Intent:* /** * Renders text to its canvas, and updates its texture. */
  * `_drawLetterSpacing` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* * 1. Native letter spacing if supported by the browser * 2. Manual letter spacing calculation if not...
  * `_setFillAndStrokeStyles` **(Stateful Encapsulated Methods)** (Impact: 12.5)
    * *Intent:* /** * Sets fill and stroke styles on the canvas context for text rendering. */
  * `_getAlignmentOffset` **(Stateful Encapsulated Methods)** (Impact: 8.7)
    * *Intent:* /** * Calculates the X offset for text alignment. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 14`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.619
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.021134
  * `Imports (Out-Degree: 8):` Color, Rectangle, CanvasPool, getCanvasBoundingBox, TextStyle, CanvasTextMetrics, fontStringFromTextStyle, getCanvasFillStyle
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/buildCommands/buildLine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.508)
- **Top Global Matches:** file_cluster_8: 6.508, file_cluster_6: 17.448, file_cluster_3: 19.632
- **Magnitude:** 458.6 | **LOC:** 555 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.315; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (60.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildLine` **(Many-Argument Workhorses)** (Impact: 130.7)
    * *Intent:* /** * Builds a line to draw using the polygon method. */
  * `round` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* * * Ignored from docs since it is not directly exposed. */
  * `square` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* * * Ignored from docs since it is not directly exposed. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 122`, `dead_code: 4`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.083632
  * `Imports (Out-Degree: 4):` Point, FillTypes, const, getOrientationOfPoints
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/Graphics.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.408)
- **Top Global Matches:** file_cluster_0: 6.408, file_cluster_5: 9.476, file_cluster_15: 9.564
- **Magnitude:** 447.4 | **LOC:** 2048 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **15**; blast radius 1.026; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.1%), Guard Balance (formerly Safety Score) (53.3%), Complexity Load (formerly Cognitive Load) (17.7%)
- **Documentation Coverage:** 1.0989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `texture` **(Compute Cores)** (Impact: 15.9)
  * `setTransform` **(Compute Cores)** (Impact: 15.9)
  * `transform` **(Compute Cores)** (Impact: 15.9)
  * `lineStyle` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* // -------- v7 deprecations --------- /** */
  * `destroy` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* * then the context will still be destroyed. * * If you want to explicitly not destroy this context t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 96`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 92`, `import: 14`
* *Defense:* `safety: 5`, `doc: 67`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.026
  * `Choke Point (Betweenness):` 0.003076 | `Ripple Effect (Closeness):` 0.091014
  * `Imports (Out-Degree: 15):` Color, Matrix, PointData, Instruction, Texture, deprecation, Bounds, destroyTypes...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/filters/FilterSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_4: 6.66, file_cluster_16: 7.085, file_cluster_15: 8.205
- **Magnitude:** 443.24 | **LOC:** 1093 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **24**; blast radius 0.992; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.2%), Connectivity (formerly Api Exposure) (40.7%)
- **Documentation Coverage:** 36.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_calculateFilterBounds` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `_updateFilterUniforms` **(Many-Argument Workhorses)** (Impact: 25.0)
    * *Intent:* /** * Updates the filter uniforms with the current filter state. */
  * `_calculateFilterArea` **(Stateful Encapsulated Methods)** (Impact: 16.0)
    * *Intent:* /** * Calculates the filter area bounds based on the instruction type. */
  * `_applyFiltersToTexture` **(Many-Argument Workhorses)** (Impact: 11.5)
  * `_setupBindGroupsAndRender` **(Stateful Encapsulated Methods)** (Impact: 9.8)
    * *Intent:* /** * Sets up the bind groups and renders the filter. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 83`, `args: 24`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 95`, `planned_debt: 3`
* *Architecture:* `api: 26`, `import: 24`
* *Defense:* `safety: 6`, `doc: 31`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 0.009318 | `Ripple Effect (Closeness):` 0.099143
  * `Imports (Out-Degree: 24):` Extensions, PassthroughFilter, Matrix, Rectangle, WebGLRenderer, WebGPURenderer, BindGroup, Renderable...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/text/TextStyle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.446)
- **Top Global Matches:** file_cluster_12: 7.446, file_cluster_15: 7.847, file_cluster_0: 8.041
- **Magnitude:** 402.68 | **LOC:** 1549 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **13**; blast radius 5.571; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.3%), Connectivity (formerly Api Exposure) (45.5%), Complexity Load (formerly Cognitive Load) (36.6%)
- **Documentation Coverage:** 18.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertV7Tov8Style` **(Defensive Guards)** (Impact: 44.5)
  * `destroy` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* /** * Destroys this text style. * have been set to that value * // Destroy the text style and its te...
  * `dropShadow` **(Compute Cores)** (Impact: 9.2)
  * `_createProxy` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `_toObject` **(Stateful Encapsulated Methods)** (Impact: 7.3)
    * *Intent:* * Returns an object with the same values as this TextStyle instance. * ```ts * const style = new Tex...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 100`, `args: 60`, `func_start: 56`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 52`
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 19`, `doc: 75`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.571
  * `Choke Point (Betweenness):` 0.007696 | `Ripple Effect (Closeness):` 0.037239
  * `Imports (Out-Degree: 12):` Color, Filter, uid, deprecation, warn, destroyTypes, FillTypes, GraphicsContext...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/utils/path.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.535)
- **Top Global Matches:** file_cluster_8: 6.535, file_cluster_6: 14.236, file_cluster_4: 22.774
- **Magnitude:** 400.18 | **LOC:** 940 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **1**; blast radius 1.683; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (60.6%), Connectivity (formerly Api Exposure) (26.7%), Complexity Load (formerly Cognitive Load) (20.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isDataUrl` **(Many-Argument Workhorses)** (Impact: 77.2)
    * *Intent:* /** * Checks if the path is a data URL * ```ts * // Check if a path is a data URL * path.isDataUrl('...
  * `normalizeStringPosix` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `parse` **(Compute Cores)** (Impact: 47.7)
    * *Intent:* * // ext: '.png', * // name: 'baz' * // } * // Parse a file path * const parsedFile = path.parse('C:...
  * `parse` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* /** * Parses a path into an object containing the 'root', `dir`, `base`, `ext`, and `name` propertie...
  * `assertPath` **(State Mutators)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 69`, `args: 35`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 89`
* *Architecture:* `io: 228`, `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 12`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.683
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.01977
  * `Imports (Out-Degree: 1):` adapter
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/rendering/renderers/shared/renderTarget/RenderTargetSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.518)
- **Top Global Matches:** file_cluster_4: 6.518, file_cluster_15: 8.12, file_cluster_16: 8.591
- **Magnitude:** 399.54 | **LOC:** 708 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 1.008; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (67.9%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (41.9%)
- **Documentation Coverage:** 25.5814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `destroyGpuRenderTarget` **(Many-Argument Workhorses)** (Impact: 84.8)
    * *Intent:* /** * destroys the gpu render target */
  * `bind` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* * render into * texture's frame to define the region (in mip 0 space). * 3D textures, or cubemaps, t...
  * `clear` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `clear` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /** * clears the current render target to the specified color */
  * `init` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* /** * Initializes the adaptor. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 60`, `args: 26`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 53`, `planned_debt: 2`
* *Architecture:* `api: 32`, `import: 20`
* *Defense:* `safety: 6`, `doc: 50`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.008
  * `Choke Point (Betweenness):` 0.002329 | `Ripple Effect (Closeness):` 0.11194
  * `Imports (Out-Degree: 18):` Color, ICanvas, Matrix, Rectangle, CanvasRenderTargetAdaptor, GlRenderTarget, const, GpuRenderTarget...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/accessibility/AccessibilitySystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.118)
- **Top Global Matches:** file_cluster_4: 6.118, file_cluster_16: 9.519, file_cluster_15: 10.858
- **Magnitude:** 395.66 | **LOC:** 913 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 0.859; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (35.5%), Connectivity (formerly Api Exposure) (14.9%)
- **Documentation Coverage:** 5.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_addChild` **(Compute Cores)** (Impact: 35.9)
    * *Intent:* /** * Creates or reuses a div element for a Container and adds it to the accessibility layer. * Sets...
  * `postrender` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* /** * Updates the accessibility layer during rendering. * - Removes divs for containers no longer in...
  * `_deactivate` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* /** * Deactivates the accessibility system. Removes listeners and accessibility elements. */
  * `_updateAccessibleObjects` **(Stateful Encapsulated Methods)** (Impact: 11.3)
    * *Intent:* /** * This recursive function will run through the scene graph and add any new accessible objects to...
  * `_activate` **(I/O & Config Routines)** (Impact: 11.2)
    * *Intent:* /** * Activating will cause the Accessibility layer to be shown. * This is called when a user presse...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 74`, `args: 31`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 88`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `safety: 4`, `doc: 53`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.859
  * `Choke Point (Betweenness):` 0.000718 | `Ripple Effect (Closeness):` 0.005294
  * `Imports (Out-Degree: 10):` CanvasObserver, FederatedEvent, Extensions, Rectangle, System, types, Container, isMobile...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/color/Color.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.039)
- **Top Global Matches:** file_cluster_4: 7.039, file_cluster_6: 10.223, file_cluster_15: 12.646
- **Magnitude:** 381.98 | **LOC:** 1195 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **2**; blast radius 3.815; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.4%), Connectivity (formerly Api Exposure) (53.2%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 2.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isColorLike` **(Type Conversions)** (Impact: 42.7)
    * *Intent:* * ``` * Checks for the following formats: * - Numbers (0x000000 to 0xffffff) * - CSS color strings *...
  * `_normalize` **(Compute Cores)** (Impact: 36.9)
    * *Intent:* /** * Normalize the input value into rgba */
  * `_isSourceEqual` **(Stateful Encapsulated Methods)** (Impact: 30.0)
    * *Intent:* /** * Equality check for color sources. */
  * `_cloneSource` **(Stateful Encapsulated Methods)** (Impact: 16.4)
    * *Intent:* /** * Copy a color source internally. */
  * `value` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* * * // Copying from another color * const red = new Color('red'); * color.value = red; // Copies red...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 58`, `args: 32`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `safety: 1`, `doc: 39`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.815
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.143699
  * `Imports (Out-Degree: 0):` colord, names
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `src/scene/sprite/__tests__/Sprite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.335)
- **Top Global Matches:** file_cluster_10: 4.335, file_cluster_2: 6.754, file_cluster_13: 7.218
- **Magnitude:** 374.49 | **LOC:** 389 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.264; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.9%), Guard Balance (formerly Safety Score) (39.4%), Concurrency Surface (formerly Concurrency) (26.9%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 54`, `args: 40`, `func_start: 2`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `concurrency: 4`, `import: 6`
* *Defense:* `test: 93`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Container, NineSliceSprite, Sprite, @test-utils, maths, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/graphics/__tests__/Graphics.Drawing.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.435)
- **Top Global Matches:** file_cluster_10: 4.435, file_cluster_2: 6.405, file_cluster_13: 7.163
- **Magnitude:** 356.57 | **LOC:** 482 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.264; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.0%), Guard Balance (formerly Safety Score) (44.2%), Concurrency Surface (formerly Concurrency) (32.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 60`, `args: 41`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 1`, `test: 84`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Bounds, getLocalBounds, Graphics, GraphicsContext, maths, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/rendering/batcher/shared/Batcher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.512)
- **Top Global Matches:** file_cluster_15: 5.512, file_cluster_16: 7.051, file_cluster_11: 7.271
- **Magnitude:** 350.64 | **LOC:** 827 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **17**; blast radius 1.397; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (79.2%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (30.8%)
- **Documentation Coverage:** 61.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `break` **(I/O & Config Routines)** (Impact: 30.3)
    * *Intent:* /** * breaks the batcher. This happens when a batch gets too big, * or we need to switch to a differ...
  * `destroy` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* /** * Destroys the batch and its resources. */
  * `_resizeIndexBuffer` **(Stateful Encapsulated Methods)** (Impact: 8.5)
  * `_finishBatch` **(Many-Argument Workhorses)** (Impact: 7.8)
  * `checkAndUpdateTexture` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 56`, `args: 21`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `state_mutation: 96`, `planned_debt: 2`
* *Architecture:* `api: 49`, `import: 17`
* *Defense:* `safety: 2`, `doc: 56`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.397
  * `Choke Point (Betweenness):` 0.002357 | `Ripple Effect (Closeness):` 0.106295
  * `Imports (Out-Degree: 17):` Bounds, ViewableBuffer, uid, deprecation, GlobalResourceRegistry, BindGroup, fastCopy, Geometry...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/culling/__tests__/Culler.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.151)
- **Top Global Matches:** file_cluster_10: 4.151, file_cluster_2: 5.763, file_cluster_13: 6.617
- **Magnitude:** 350.04 | **LOC:** 479 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.264; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 42`, `args: 26`, `func_start: 3`
* *Risk/State:* `state_mutation: 106`
* *Architecture:* `concurrency: 10`, `import: 10`
* *Defense:* `safety: 6`, `test: 73`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Culler, CullerPlugin, @test-utils, app, assets, extensions, filters, maths...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/text/utils/canvasTextSplit.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.135)
- **Top Global Matches:** file_cluster_8: 11.135, file_cluster_3: 13.141, file_cluster_6: 23.724
- **Magnitude:** 349.94 | **LOC:** 492 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 1.208; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%), Complexity Load (formerly Cognitive Load) (69.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canvasTaggedTextSplitFromRuns` **(Many-Argument Workhorses)** (Impact: 87.6)
  * `canvasTextSplit` **(Compute Cores)** (Impact: 52.7)
    * *Intent:* /** * Splits a Text object into segments based on the text's layout and style, * and adds these segm...
  * `groupTextSegments` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* /** * Groups text segments into lines based on measured text metrics */
  * `getAlignmentOffset` **(Compute Cores)** (Impact: 12.7)
  * `isNewlineCharacter` **(Compute Cores)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 35`, `args: 11`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.208
  * `Choke Point (Betweenness):` 0.000247 | `Ripple Effect (Closeness):` 0.020893
  * `Imports (Out-Degree: 10):` Matrix, Container, FillGradient, SplitText, types, Text, TextStyle, CanvasTextGenerator...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/rendering/renderers/gl/renderTarget/GlRenderTargetAdaptor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.924)
- **Top Global Matches:** file_cluster_4: 5.924, file_cluster_12: 9.147, file_cluster_16: 9.901
- **Magnitude:** 343.18 | **LOC:** 676 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.8%), Complexity Load (formerly Cognitive Load) (32.4%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `startRenderPass` **(Many-Argument Workhorses)** (Impact: 87.1)
  * `clear` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_initColor` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `_setDrawBuffers` **(Stateful Encapsulated Methods)** (Impact: 9.9)
  * `_resizeColor` **(Many-Argument Workhorses)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 43`, `args: 24`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.336
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.081583
  * `Imports (Out-Degree: 11):` Color, Rectangle, warn, RenderTarget, RenderTargetSystem, Texture, CanvasSource, GlRenderTarget...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/assets/loader/parsers/loadWebFont.ts` (TYPESCRIPT) | Magnitude: 4.98 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 37, core_var_decl: 27, doc: 15
- `src/rendering/renderers/shared/texture/RenderTexture.ts` (TYPESCRIPT) | Magnitude: 10.98 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, api: 3, doc: 3
- `src/scene/text-bitmap/asset/loadBitmapFont.ts` (TYPESCRIPT) | Magnitude: 6.14 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 40, concurrency: 14, import: 14
- `src/spritesheet/__tests__/spritesheetAsset.test.ts` (TYPESCRIPT) | Magnitude: 244.14 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 174, test: 51, structural_boundaries: 48, core_var_decl: 39
- `src/math-extras/pointExtras.ts` (TYPESCRIPT) | Magnitude: 123.54 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 24, state_mutation: 24, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `examples/graphics_mask_animation.ts` (TYPESCRIPT) | Magnitude: 65.46 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 70, state_mutation: 28, io: 10, scientific: 10
- `src/rendering/renderers/gl/shader/program/__tests__/glEnsureAttributes.test.ts` (TYPESCRIPT) | Magnitude: 48.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 94, core_var_decl: 13, structural_boundaries: 11, test: 9
- `examples/graphics_svg_string-parsing.ts` (TYPESCRIPT) | Magnitude: 21.52 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 11, design_snake_case: 11, design_short_vars: 7
- `tests/visual/scenes/text/text-invisible-value-update.scene.ts` (TYPESCRIPT) | Magnitude: 41.14 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 15, concurrency: 8, core_var_decl: 8
- `src/spritesheet/__tests__/Spritesheet.test.ts` (TYPESCRIPT) | Magnitude: 50.1 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 75, test: 66, core_var_decl: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/filters/FilterPipe.ts` (TYPESCRIPT) | Magnitude: 32.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 22, api: 7, import: 7
- `src/rendering/renderers/shared/renderTarget/GlobalUniformSystem.ts` (TYPESCRIPT) | Magnitude: 115.76 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 47, state_mutation: 30, branch: 18
- `src/rendering/renderers/shared/texture/TextureMatrix.ts` (TYPESCRIPT) | Magnitude: 99.0 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 24, core_var_decl: 14, branch: 12
- `src/rendering/renderers/shared/view/ViewSystem.ts` (TYPESCRIPT) | Magnitude: 63.86 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 31, doc: 28, branch: 15
- `src/assets/resolver/__tests__/Resolver.test.ts` (TYPESCRIPT) | Magnitude: 9.43 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 719, test: 89, decorators: 54, structural_boundaries: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/filters/defaults/blur/BlurFilterPass.ts` (TYPESCRIPT) | Magnitude: 132.24 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 32, state_mutation: 28, core_var_decl: 24
- `src/rendering/renderers/shared/texture/__tests__/ExternalSource.test.ts` (TYPESCRIPT) | Magnitude: 52.72 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 205, core_var_decl: 48, test: 41, structural_boundaries: 37
- `src/utils/pool/Pool.ts` (TYPESCRIPT) | Magnitude: 78.0 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 22, branch: 15, state_mutation: 13
- `src/gif/GifSource.ts` (TYPESCRIPT) | Magnitude: 100.26 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 124, core_var_decl: 23, state_mutation: 21, branch: 18
- `examples/graphics_dynamic.ts` (TYPESCRIPT) | Magnitude: 35.34 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, scientific: 30, state_mutation: 12, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/visual/scenes/sprite/tiling-sprite.scene.ts` (TYPESCRIPT) | Magnitude: 7.02 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 10, import: 5, core_var_decl: 4
- `tests/visual/scenes/mesh/fully-custom-mesh.scene.ts` (TYPESCRIPT) | Magnitude: 11.02 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 14, core_var_decl: 9, decorators: 7
- `src/rendering/batcher/shared/DefaultShader.ts` (TYPESCRIPT) | Magnitude: 7.14 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 9, import: 6, api: 3
- `tests/visual/scenes/textures/mrt-render-to-mip-level.scene.ts` (TYPESCRIPT) | Magnitude: 39.48 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 181, state_mutation: 24, structural_boundaries: 23, core_var_decl: 23
- `tests/visual/scenes/textures/render-to-array-layer.scene.ts` (TYPESCRIPT) | Magnitude: 23.4 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 178, core_var_decl: 28, structural_boundaries: 24, design_camel_case: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/rendering/renderers/canvas/texture/CanvasTextureSystem.ts` (TYPESCRIPT) | Magnitude: 26.54 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 26, core_var_decl: 13, design_snake_case: 12
- `src/dom/CanvasObserver.ts` (TYPESCRIPT) | Magnitude: 75.54 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 101, branch: 17, core_var_decl: 17, state_mutation: 16
- `src/scene/graphics/shared/fill/FillPattern.ts` (TYPESCRIPT) | Magnitude: 46.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 16, api: 12, doc: 10
- `src/scene/mesh/shared/MeshPipe.ts` (TYPESCRIPT) | Magnitude: 119.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 43, state_mutation: 25, branch: 19
- `src/utils/browser/isWebGPUSupported.ts` (TYPESCRIPT) | Magnitude: 37.2 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, concurrency: 7, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/rendering/renderers/gl/state/GlStateSystem.ts` (TYPESCRIPT) | Magnitude: 194.64 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 205, state_mutation: 47, structural_boundaries: 40, branch: 31
- `src/scene/text-html/HTMLTextPipe.ts` (TYPESCRIPT) | Magnitude: 113.04 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 27, state_mutation: 23, branch: 17
- `src/rendering/renderers/gpu/shader/GpuProgram.ts` (TYPESCRIPT) | Magnitude: 78.14 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, doc: 26, structural_boundaries: 23, api: 20
- `src/rendering/renderers/gpu/texture/utils/GpuMipmapGenerator.ts` (TYPESCRIPT) | Magnitude: 66.64 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 154, core_var_decl: 20, state_mutation: 16, design_camel_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/unsafe-eval/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `src/scene/index.ts` (TYPESCRIPT) | Magnitude: 210.84 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 192, api: 192, import: 192, branch: 3
- `src/rendering/renderers/shared/system/SharedSystems.ts` (TYPESCRIPT) | Magnitude: 19.0 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 22, import: 21, doc: 5
- `src/rendering/index.ts` (TYPESCRIPT) | Magnitude: 255.72 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 236, api: 236, import: 236
- `src/filters/index.ts` (TYPESCRIPT) | Magnitude: 55.8 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 40, api: 40, import: 40, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/scene/particle-container/gl/GlParticleContainerAdaptor.ts` (TYPESCRIPT) | Magnitude: 15.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, core_var_decl: 7, design_snake_case: 5
- `tests/visual/scenes/mask/nested-mask.scene.ts` (TYPESCRIPT) | Magnitude: 27.1 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 8, core_var_decl: 8, state_mutation: 5
- `.github/workflows/issue-close.yaml` (YAML) | Magnitude: 15.38 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 16, args: 4, structural_boundaries: 2, events: 2
- `.github/workflows/issue-labelled.yaml` (YAML) | Magnitude: 16.44 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, args: 5, branch: 3, structural_boundaries: 2
- `src/utils/data/updateQuadBounds.ts` (TYPESCRIPT) | Magnitude: 31.26 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, state_mutation: 8, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/assets/cache/Cache.ts` (TYPESCRIPT) | Magnitude: 5.42 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 19, core_var_decl: 12, args: 11
- `src/rendering/renderers/canvas/CanvasRenderer.ts` (TYPESCRIPT) | Magnitude: 10.16 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 45, indent_spaces: 34, import: 23, core_var_decl: 8
- `src/rendering/mask/MaskEffectManager.ts` (TYPESCRIPT) | Magnitude: 31.44 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 20, api: 8, args: 7
- `src/rendering/renderers/gpu/WebGPURenderer.ts` (TYPESCRIPT) | Magnitude: 11.22 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 49, indent_spaces: 33, import: 26, core_var_decl: 8
- `src/rendering/renderers/gl/WebGLRenderer.ts` (TYPESCRIPT) | Magnitude: 11.22 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 50, indent_spaces: 35, import: 27, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/visual/scenes/text-bitmap/bitmap-text-break-all.scene.ts` (TYPESCRIPT) | Magnitude: 6.38 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, import: 4, core_var_decl: 4
- `tests/visual/scenes/text/text-break-all.scene.ts` (TYPESCRIPT) | Magnitude: 6.28 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, import: 4, core_var_decl: 4
- `tests/visual/scenes/text-split/bitmap-text-break-all-split.scene.ts` (TYPESCRIPT) | Magnitude: 6.26 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, import: 4, core_var_decl: 4
- `tests/visual/scenes/text-split/text-break-all-split.scene.ts` (TYPESCRIPT) | Magnitude: 6.26 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, import: 4, core_var_decl: 4
- `src/environment/ImageLike.ts` (TYPESCRIPT) | Magnitude: 6.46 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 10, doc: 9, structural_boundaries: 7, args: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/scene/text/utils/canvasTextSplit.ts` -> Churn: **66.96%** | Cog Load: 69.0978% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/scene/graphics/shared/GraphicsContext.ts` -> **Mat Groves** (100.0% isolated ownership) | Magnitude: 579.68
- `src/scene/container/Container.ts` -> **Bjorn Stromberg** (100.0% isolated ownership) | Magnitude: 538.5
- `src/scene/text/canvas/utils/measureTaggedText.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 492.06
- `src/events/EventSystem.ts` -> **Kai Gritun** (100.0% isolated ownership) | Magnitude: 487.82
- `src/scene/text/canvas/CanvasTextGenerator.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 472.34

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/scene/container/Container.ts` -> **Severity: 2.264** (Bridge: 0.0226 * Flux: 99.9971%)
- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 2.097** (Bridge: 0.021 * Flux: 100.0%)
- `src/rendering/renderers/shared/texture/Texture.ts` -> **Severity: 1.036** (Bridge: 0.0104 * Flux: 100.0%)
- `src/filters/Filter.ts` -> **Severity: 0.995** (Bridge: 0.01 * Flux: 99.9887%)
- `src/filters/FilterSystem.ts` -> **Severity: 0.932** (Bridge: 0.0093 * Flux: 99.9978%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/scene/container/bounds/Bounds.ts` -> **Severity: 13.115** (Embedded: 0.1591 * Error Risk: 82.4561%)
- `src/maths/matrix/Matrix.ts` -> **Severity: 12.786** (Embedded: 0.1732 * Error Risk: 73.8094%)
- `src/extensions/Extensions.ts` -> **Severity: 11.949** (Embedded: 0.1983 * Error Risk: 60.2475%)
- `src/rendering/renderers/shared/texture/Texture.ts` -> **Severity: 10.708** (Embedded: 0.1606 * Error Risk: 66.6904%)
- `src/maths/shapes/Rectangle.ts` -> **Severity: 10.091** (Embedded: 0.1731 * Error Risk: 58.2865%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/utils/logging/deprecation.ts` -> **Severity: 1237.4** (Blast Radius: 12.374 * Doc Risk: 100.0%)
- `src/scene/text-split/SplitText.ts` -> **Severity: 443.334** (Blast Radius: 6.65 * Doc Risk: 66.6667%)
- `src/rendering/renderers/gl/WebGLRenderer.ts` -> **Severity: 398.0** (Blast Radius: 3.98 * Doc Risk: 100.0%)
- `src/scene/container/Container.ts` -> **Severity: 385.422** (Blast Radius: 16.097 * Doc Risk: 23.9437%)
- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 280.209** (Blast Radius: 8.056 * Doc Risk: 34.7826%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 249 literal sites + 36 sites through wrappers = 285

- `throwBindingError` (function, panics_and_aborts, primitive): 30 call sites in 1 files -- `transcoders/basis/basis_transcoder.js`
- `throwInternalError` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `transcoders/basis/basis_transcoder.js`
- `instantiateArrayBuffer` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `transcoders/basis/basis_transcoder.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 8889 call pairs -- scoped 31.8%, unique 0.0%, ambiguous 35.7%, external 32.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 8233 | 31.5% | 0.0% | 37.7% | 30.8% |
| javascript | 656 | 35.2% | 0.0% | 10.1% | 54.7% |

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
