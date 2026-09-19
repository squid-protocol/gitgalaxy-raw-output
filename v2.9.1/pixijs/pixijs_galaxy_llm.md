# ARCHITECTURAL_BRIEF: pixijs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pixijs/pixijs.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1549 analyzed artifact(s), 113831 LOC.
- **Load-bearing artifact:** `src/scene/__docs__/scene.md` -- 377 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Analyzed Artifacts (Scanned) | 1549 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1600 |
| Total LOC | 113831 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 49.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.564 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2099 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 17.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.0358 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 87 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1394 | 108470 | 90.0% |
| MARKDOWN | 53 | 0 | 3.4% |
| GLSL | 41 | 888 | 2.6% |
| JSON | 26 | 1325 | 1.7% |
| JAVASCRIPT | 14 | 2458 | 0.9% |
| XML | 11 | 1 | 0.7% |
| PLAINTEXT | 7 | 1 | 0.5% |
| HTML | 2 | 21 | 0.1% |
| CSS | 1 | 667 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `2.236`
> **Composition Archetype:** `Hub-Coupled App` (z +2.24; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 21%, Large Core Modules 16%, Data / Markup / Trivial 12%, Large Core Modules (3) 10%, Many-Argument Workhorses Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1488 | 96.1% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 3.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1600*

**Composition by Extension & Reason:**
- `.png`: 1438x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 17x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wgsl`: 10x Unsupported Format (.wgsl), 5x Excluded (Unsupported Extension: '.wgsl')
- `.dds`: 13x Excluded (Binary Format Detected), 2x Excluded (Unsupported Extension: '.dds')
- `.fnt`: 10x Unsupported Format (.fnt), 3x Excluded (Unsupported Extension: '.fnt')
- `.ktx`: 9x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.ktx')
- `.webp`: 9x Excluded (Explicitly Denied Extension: '.webp')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 2x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 88 exceeds 500 chars)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 32765 LOC exceeds safe regex boundaries), 1x Excluded (Static Asset Blob without Intent: 2084 LOC)
- `.ttf`: 7x Excluded (Explicitly Denied Extension: '.ttf')
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 4x Excluded (Explicitly Denied Extension: '.woff2')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 14.4 | 4.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 46.9 | 58.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.2 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.0 | 8.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.5 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 864 | 271 | 1 | `src/color/Color.ts` |
| cleanup | 532 | 161 | 1 | `src/rendering/renderers/shared/texture/__tests__/ExternalSource.test.ts` |
| guards | 2840 | 460 | 6 | `transcoders/basis/basis_transcoder.js` |
| danger | 1179 | 276 | 1 | `src/unsafe-eval/uniforms/uniformSyncFunctions.ts` |
| concurrency | 2614 | 631 | 4 | `src/assets/__tests__/Assets.test.ts` |
| connectivity | 5485 | 1104 | 9 | `src/rendering/index.ts` |
| io | 1263 | 177 | 1 | `src/utils/__tests__/path.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 27 | 13 | 0 | `src/assets/loader/workers/WorkerManager.ts` |
| time | 113 | 74 | 0 | `src/rendering/renderers/shared/__tests__/GCSystem.test.ts` |
| serialization | 10 | 4 | 0 | `scripts/plugins/typedoc-plugin-stackblitz.mjs` |
| regex | 178 | 73 | 0 | `scripts/plugins/typedoc-plugin-stackblitz.mjs` |
| events | 837 | 181 | 1 | `src/events/__tests__/EventSystem.test.ts` |
| tests | 7565 | 196 | 5 | `src/scene/container/__tests__/Container.test.ts` |
| docs | 5181 | 693 | 10 | `src/scene/container/Container.ts` |
| debt | 235 | 129 | 0 | `src/rendering/renderers/shared/system/__tests__/SystemRunner.test.ts` |
| mutation | 28432 | 1335 | 43 | `transcoders/basis/basis_transcoder.js` |
| dead_code | 530 | 447 | 1 | `src/math-extras/MathExtraMixins.d.ts` |
| credential | 7 | 4 | 0 | `src/utils/__tests__/path.test.ts` |
| threat | 315 | 133 | 0 | `transcoders/basis/basis_transcoder.js` |
| ml_ai | 962 | 197 | 1 | `examples/graphics_dynamic.ts` |
| ui | 106 | 19 | 0 | `scripts/plugins/typedoc-custom.css` |

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

1. **scene.md** (`src/scene/__docs__/scene.md`) — 377 inbound connections
2. **assets.md** (`src/assets/__docs__/assets.md`) — 206 inbound connections
3. **Extensions.ts** (`src/extensions/Extensions.ts`) — 193 inbound connections
4. **rendering.md** (`src/rendering/__docs__/rendering.md`) — 107 inbound connections
5. **Container.ts** (`src/scene/container/Container.ts`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/rendering/index.ts`) — 236 outbound dependencies
2. **index.ts** (`src/scene/index.ts`) — 192 outbound dependencies
3. **index.ts** (`src/filters/index.ts`) — 40 outbound dependencies
4. **index.ts** (`src/assets/index.ts`) — 37 outbound dependencies
5. **Container.ts** (`src/scene/container/Container.ts`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isDataUrl` **(Compute Cores)** (@ `src/utils/path.ts`) -> Impact: **217.2** | LOC: 639
  * *Intent:* /** * Checks if the path is a URL e.g. http://, https:// * ```ts * // Check if a path is a URL * path.isUrl('http://www.example.com'); * // -> true * ...
- `wordWrapTaggedLines` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **168.6** | LOC: 303
  * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining style information. */
- `getBitmapTextLayout` **(Many-Argument Workhorses)** (@ `src/scene/text-bitmap/utils/getBitmapTextLayout.ts`) -> Impact: **152.8** | LOC: 284
  * *Intent:* /** */
- `renderChildren` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/svg/SVGParser.ts`) -> Impact: **143.7** | LOC: 236
  * *Intent:* /** * Recursively renders SVG elements and their children. * Handles styling inheritance and different SVG shape types. */
- `buildLine` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> Impact: **130.7** | LOC: 391
  * *Intent:* /** * Builds a line to draw using the polygon method. */
- `execute` **(Many-Argument Workhorses)** (@ `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`) -> Impact: **128.2** | LOC: 244
- `recursive` **(Many-Argument Workhorses)** (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> Impact: **116.7** | LOC: 187
  * *Intent:* // eslint-disable-next-line max-params
- `_renderTaggedTextToCanvas` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/CanvasTextGenerator.ts`) -> Impact: **108.7** | LOC: 264
  * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. */
- `measureTaggedText` **(Many-Argument Workhorses)** (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **105.3** | LOC: 186
  * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line metrics. */
- `execute` **(Many-Argument Workhorses)** (@ `src/rendering/batcher/canvas/CanvasBatchAdaptor.ts`) -> Impact: **99.9** | LOC: 196

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 5 | 5048.44 | 0.48% | 0.0% |
| `examples` | 87 | 3118.86 | 35.68% | 0.0% |
| `src/scene/container/__tests__` | 32 | 3055.37 | 12.81% | 0.0% |
| `transcoders/basis` | 1 | 2349.88 | 95.73% | 20.21% |
| `src/events` | 14 | 1797.68 | 11.32% | 1.28% |
| `src/scene/graphics/shared` | 7 | 1365.32 | 18.3% | 6.1% |
| `src/scene/graphics/shared/buildCommands` | 12 | 1325.78 | 36.35% | 0.94% |
| `src/rendering/renderers/__tests__` | 10 | 1151.94 | 8.19% | 0.0% |
| `src/culling/__tests__` | 1 | 1133.5 | 41.35% | 0.0% |
| `src/scene/graphics/shared/path` | 3 | 1100.66 | 38.69% | 7.47% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/math-extras/MathExtraMixins.d.ts` -> **100.0%** Exposure
- `types/Temp.d.ts` -> **100.0%** Exposure
- `src/app/ApplicationMixins.d.ts` -> **99.9665%** Exposure
- `scripts/jest/jest-snapshot-resolver.js` -> **99.929%** Exposure
- `src/scene/text-html/utils/loadSVGImage.ts` -> **98.2014%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.stackblitz/bunny-mark/src/Bunny.js` -> **100.0%** Exposure
- `transcoders/basis/basis_transcoder.js` -> **100.0%** Exposure
- `scripts/utils/autoGenerateUnsafeEvalFunctions.ts` -> **100.0%** Exposure
- `scripts/utils/bump.mts` -> **100.0%** Exposure
- `src/assets/detections/utils/testImageFormat.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/math-extras/MathExtraMixins.d.ts` -> **15** Orphaned Functions | **0** Duplicates
- `transcoders/basis/basis_transcoder.js` -> **10** Orphaned Functions | **0** Duplicates
- `src/app/ApplicationMixins.d.ts` -> **5** Orphaned Functions | **0** Duplicates
- `types/Temp.d.ts` -> **0** Orphaned Functions | **4** Duplicates
- `src/events/__tests__/EventSystem.test.ts` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1256` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `transcoders/basis/basis_transcoder.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2349.88 | **LOC:** 1265 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Complexity Load (formerly Cognitive Load) (95.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` **(Defensive Guards)** (Impact: 65.0)
  * `__embind_register_std_string` **(Defensive Guards)** (Impact: 51.4)
  * `genericPointerToWireType` **(Defensive Guards)** (Impact: 41.5)
  * `__embind_register_class` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `stringToUTF8Array` **(Compute Cores)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 363 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 1195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 394`, `args: 220`, `func_start: 194`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 4`, `state_mutation: 469`, `unreferenced_by_name: 10`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 198`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/culling/__tests__/Culler.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1133.5 | **LOC:** 479 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 42`, `args: 26`, `func_start: 3`
* *Risk/State:* `state_mutation: 106`
* *Architecture:* `concurrency: 10`, `import: 10`
* *Defense:* `safety: 6`, `test: 73`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Culler, CullerPlugin, @test-utils, app, assets, extensions, filters, maths...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/events/EventBoundary.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 854.42 | **LOC:** 1487 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 0.662; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Complexity Load (formerly Cognitive Load) (39.5%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 5.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hitTestMoveRecursive` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `mapPointerMove` **(Compute Cores)** (Impact: 59.0)
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
* *Structure:* `branch: 216`, `structural_boundaries: 142`, `args: 37`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 144`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 13`, `import: 12`
* *Defense:* `safety: 12`, `doc: 43`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.662
  * `Choke Point (Betweenness):` 0.00024 | `Ripple Effect (Closeness):` 0.00726
  * `Imports (Out-Degree: 11):` Point, Renderable, Container, warn, EventBoundaryTypes, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/container/__tests__/getLocalBounds.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 739.42 | **LOC:** 509 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (86.9%), Guard Balance (formerly Safety Score) (33.3%), Complexity Load (formerly Cognitive Load) (28.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 32`, `args: 22`, `func_start: 21`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `concurrency: 21`, `import: 9`
* *Defense:* `safety: 1`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Graphics, Sprite, Container, Bounds, getLocalBounds, DummyEffect, DummyView, maths...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/rendering/renderers/__tests__/Extract.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 695.39 | **LOC:** 477 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (21.3%), Mutation Surface (formerly State Flux) (19.0%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 73`, `args: 28`, `func_start: 23`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `concurrency: 58`, `import: 7`
* *Defense:* `safety: 7`, `test: 84`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` init, WebGLRenderer, ExtractSystem, RenderTexture, Texture, @test-utils, maths, scene...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/sprite/__tests__/Sprite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 634.62 | **LOC:** 389 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.2%), Concurrency Surface (formerly Concurrency) (26.9%), Guard Balance (formerly Safety Score) (23.5%), Dead Code Surface (formerly Dead Code) (8.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 54`, `args: 40`, `func_start: 2`
* *Risk/State:* `state_mutation: 25`, `dead_code: 1`
* *Architecture:* `concurrency: 4`, `import: 6`
* *Defense:* `test: 93`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Container, NineSliceSprite, Sprite, @test-utils, maths, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils/path.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 631.38 | **LOC:** 940 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **2**; blast radius 5.127; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Complexity Load (formerly Cognitive Load) (52.8%), Connectivity (formerly Api Exposure) (26.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isDataUrl` **(Compute Cores)** (Impact: 217.2)
    * *Intent:* /** * Checks if the path is a URL e.g. http://, https:// * ```ts * // Check if a path is a URL * pat...
  * `normalizeStringPosix` **(Many-Argument Workhorses)** (Impact: 62.3)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `parse` **(Compute Cores)** (Impact: 47.7)
    * *Intent:* * // ext: '.png', * // name: 'baz' * // } * // Parse a file path * const parsedFile = path.parse('C:...
  * `parse` **(Compute Cores)** (Impact: 10.3)
    * *Intent:* /** * Parses a path into an object containing the 'root', `dir`, `base`, `ext`, and `name` propertie...
  * `assertPath` **(State Mutators)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 69`, `args: 35`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 89`, `dead_code: 1`
* *Architecture:* `io: 228`, `api: 2`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 12`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.127
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.027769
  * `Imports (Out-Degree: 1):` adapter, pixi.js
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/scene/graphics/__tests__/Graphics.Drawing.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 623.8 | **LOC:** 482 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Guard Balance (formerly Safety Score) (36.9%), Concurrency Surface (formerly Concurrency) (32.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 60`, `args: 41`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 1`, `test: 84`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Bounds, getLocalBounds, Graphics, GraphicsContext, maths, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/text-bitmap/__tests__/BitmapFontLoader.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 607.53 | **LOC:** 393 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (24.7%), Complexity Load (formerly Cognitive Load) (16.2%), Guard Balance (formerly Safety Score) (4.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 43`, `args: 16`, `func_start: 13`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `concurrency: 34`, `import: 6`
* *Defense:* `safety: 2`, `test: 178`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Sprite, BitmapFont, loadBitmapFont, @test-utils, assets, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scene/graphics/shared/GraphicsContext.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 579.68 | **LOC:** 1285 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **19**; blast radius 1.999; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (83.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.999
  * `Choke Point (Betweenness):` 0.006759 | `Ripple Effect (Closeness):` 0.077405
  * `Imports (Out-Degree: 18):` Color, Matrix, Point, PointData, GCSystem, Shader, Texture, uid...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/utils/measureTaggedText.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 567.86 | **LOC:** 633 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.344; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.6%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wordWrapTaggedLines` **(Many-Argument Workhorses)** (Impact: 168.6)
    * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining...
  * `measureTaggedText` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line met...
  * `startNewLine` **(I/O & Config Routines)** (Impact: 57.4)
  * `getWordGroupWidth` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* // Helper to calculate the total width of a word group starting at index // A word group is a sequen...
  * `tokenizeTaggedRuns` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* /** * Tokenizes an array of TextStyleRuns into individual styled tokens. * Each token is a word, spa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 33`, `args: 9`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 6`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.344
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011812
  * `Imports (Out-Degree: 4):` ICanvasRenderingContext2D, TextStyle, parseTaggedText, textTokenization, types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/path/GraphicsPath.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 557.0 | **LOC:** 863 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **9**; blast radius 1.349; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.8%), Connectivity (formerly Api Exposure) (82.2%), Test Surface (formerly Verification) (80.0%)
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
  * `constructor` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /** * Creates a `GraphicsPath` instance optionally from an SVG path string or an array of `PathInstr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 67`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 47`, `import: 9`
* *Defense:* `safety: 2`, `doc: 31`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.349
  * `Choke Point (Betweenness):` 0.00121 | `Ripple Effect (Closeness):` 0.074284
  * `Imports (Out-Degree: 9):` Matrix, Point, PointData, uid, warn, Bounds, parseSVGPath, ShapePath...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/container/Container.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 546.2 | **LOC:** 2142 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **105** in-repo importer(s); it depends on **32**; blast radius 13.54; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Complexity Load (formerly Cognitive Load) (28.6%)
- **Documentation Coverage:** 23.9437% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateTransform` **(Compute Cores)** (Impact: 21.1)
    * *Intent:* */
  * `addChild` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* * container.addChild(sprite); * * // Add multiple children * container.addChild(background, player, ...
  * `setSize` **(Defensive Guards)** (Impact: 18.2)
    * *Intent:* /** * Sets the size of the container to the specified width and height. * This is more efficient tha...
  * `destroy` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* /** * Removes all internal references and listeners as well as removes children from the display lis...
  * `removeChild` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* * const removed = container.removeChild(sprite); * * // Remove multiple children * const bg = contai...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 117`, `args: 56`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 93`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 68`, `import: 32`
* *Defense:* `safety: 14`, `doc: 115`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.54
  * `Choke Point (Betweenness):` 0.016586 | `Ripple Effect (Closeness):` 0.127574
  * `Imports (Out-Degree: 29):` Color, cullingMixin, Extensions, Matrix, Size, const, ObservablePoint, PointData...
  * `Imported By (In-Degree: 105):` (Excluded from Brief to save tokens)

### `src/events/EventSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 498.12 | **LOC:** 1168 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.725; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.5%), Complexity Load (formerly Cognitive Load) (47.3%), Connectivity (formerly Api Exposure) (38.0%)
- **Documentation Coverage:** 15.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_normalizeToPointerData` **(Compute Cores)** (Impact: 70.2)
    * *Intent:* /** * Ensures that the original event object contains all data that a regular pointer event would ha...
  * `setCursor` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* * * // Using callback-based cursor * app.renderer.events.cursorStyles.dynamic = (mode) => { * docume...
  * `_addEvents` **(I/O & Config Routines)** (Impact: 13.2)
  * `_removeEvents` **(I/O & Config Routines)** (Impact: 12.8)
  * `_onPointerDown` **(Stateful Encapsulated Methods)** (Impact: 11.6)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 83`, `args: 22`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 124`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 6`, `doc: 44`, `immutability_locks: 6`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.725
  * `Choke Point (Betweenness):` 0.001027 | `Ripple Effect (Closeness):` 0.007003
  * `Imports (Out-Degree: 11):` Extensions, PointData, System, types, EventBoundary, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/CanvasTextGenerator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 484.64 | **LOC:** 785 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 0.413; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_renderTaggedTextToCanvas` **(Many-Argument Workhorses)** (Impact: 108.7)
    * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. */
  * `_renderTextToCanvas` **(Many-Argument Workhorses)** (Impact: 91.9)
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
* *Structure:* `branch: 102`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 14`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.413
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.007792
  * `Imports (Out-Degree: 8):` Color, Rectangle, CanvasPool, getCanvasBoundingBox, TextStyle, CanvasTextMetrics, fontStringFromTextStyle, getCanvasFillStyle...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/container/bounds/Bounds.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 474.56 | **LOC:** 1017 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **2**; blast radius 7.232; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Connectivity (formerly Api Exposure) (84.0%), Complexity Load (formerly Cognitive Load) (45.6%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.232
  * `Choke Point (Betweenness):` 0.000118 | `Ripple Effect (Closeness):` 0.141545
  * `Imports (Out-Degree: 2):` Matrix, Rectangle
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/buildCommands/buildLine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 458.6 | **LOC:** 555 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.303; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.7%)
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
* *Risk/State:* `state_mutation: 122`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.303
  * `Choke Point (Betweenness):` 0.000262 | `Ripple Effect (Closeness):` 0.072284
  * `Imports (Out-Degree: 3):` Point, FillTypes, const, getOrientationOfPoints
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/Graphics.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 448.9 | **LOC:** 2048 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **15**; blast radius 1.101; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.7%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 1.0989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `texture` **(Compute Cores)** (Impact: 15.9)
  * `setTransform` **(Compute Cores)** (Impact: 15.9)
  * `transform` **(Compute Cores)** (Impact: 15.9)
  * `lineStyle` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* // -------- v7 deprecations --------- /** */
  * `constructor` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* /** * Creates a new Graphics object. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 96`, `args: 95`, `func_start: 95`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 92`, `import: 14`
* *Defense:* `safety: 5`, `doc: 67`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.101
  * `Choke Point (Betweenness):` 0.002356 | `Ripple Effect (Closeness):` 0.080338
  * `Imports (Out-Degree: 14):` Color, Matrix, PointData, Instruction, Texture, deprecation, Bounds, destroyTypes...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/filters/FilterSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 446.74 | **LOC:** 1093 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **24**; blast radius 0.928; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (40.7%)
- **Documentation Coverage:** 36.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_calculateFilterBounds` **(Many-Argument Workhorses)** (Impact: 55.6)
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
* *Structure:* `branch: 71`, `structural_boundaries: 83`, `args: 24`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 95`, `dead_code: 10`, `planned_debt: 3`
* *Architecture:* `api: 26`, `import: 24`
* *Defense:* `safety: 6`, `doc: 31`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.928
  * `Choke Point (Betweenness):` 0.008688 | `Ripple Effect (Closeness):` 0.085279
  * `Imports (Out-Degree: 24):` Extensions, PassthroughFilter, Matrix, Rectangle, WebGLRenderer, WebGPURenderer, BindGroup, Renderable...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/text/TextStyle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 415.48 | **LOC:** 1549 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **14**; blast radius 3.888; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (73.6%), Connectivity (formerly Api Exposure) (45.5%), Complexity Load (formerly Cognitive Load) (37.6%)
- **Documentation Coverage:** 18.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertV7Tov8Style` **(Defensive Guards)** (Impact: 53.0)
  * `destroy` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* /** * Destroys this text style. * have been set to that value * // Destroy the text style and its te...
  * `dropShadow` **(Compute Cores)** (Impact: 9.2)
  * `_isFillStyle` **(Stateful Encapsulated Methods)** (Impact: 8.7)
  * `constructor` **(I/O & Config Routines)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 100`, `args: 60`, `func_start: 56`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 52`
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 19`, `doc: 75`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.888
  * `Choke Point (Betweenness):` 0.004406 | `Ripple Effect (Closeness):` 0.02044
  * `Imports (Out-Degree: 12):` Color, Filter, uid, deprecation, warn, destroyTypes, FillTypes, GraphicsContext...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/spritesheet/__tests__/spritesheetAsset.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 413.07 | **LOC:** 239 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (40.7%), Mutation Surface (formerly State Flux) (39.1%), Guard Balance (formerly Safety Score) (20.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 48`, `args: 16`, `func_start: 11`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `concurrency: 31`, `import: 7`
* *Defense:* `safety: 3`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Spritesheet, spritesheetAsset, @test-utils, assets, rendering
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/rendering/renderers/shared/renderTarget/RenderTargetSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 408.04 | **LOC:** 708 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 1.028; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Connectivity (formerly Api Exposure) (67.9%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 25.5814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `destroyGpuRenderTarget` **(Many-Argument Workhorses)** (Impact: 89.0)
    * *Intent:* /** * destroys the gpu render target */
  * `bind` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* * render into * texture's frame to define the region (in mip 0 space). * 3D textures, or cubemaps, t...
  * `clear` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `renderStart` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* /** * called when the renderer starts to render a scene. * to a specific layer of a layered render t...
  * `clear` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /** * clears the current render target to the specified color */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 60`, `args: 26`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 53`, `planned_debt: 2`
* *Architecture:* `api: 32`, `import: 20`
* *Defense:* `safety: 6`, `doc: 50`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.028
  * `Choke Point (Betweenness):` 0.002342 | `Ripple Effect (Closeness):` 0.099858
  * `Imports (Out-Degree: 17):` Color, ICanvas, Matrix, Rectangle, CanvasRenderTargetAdaptor, GlRenderTarget, const, GpuRenderTarget...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/accessibility/AccessibilitySystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 402.66 | **LOC:** 913 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 0.778; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Complexity Load (formerly Cognitive Load) (35.6%), Connectivity (formerly Api Exposure) (14.9%)
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
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 74`, `args: 31`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 88`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `safety: 4`, `doc: 53`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.778
  * `Choke Point (Betweenness):` 0.000782 | `Ripple Effect (Closeness):` 0.004875
  * `Imports (Out-Degree: 10):` CanvasObserver, FederatedEvent, Extensions, Rectangle, System, types, Container, isMobile...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/scene/text-bitmap/utils/getBitmapTextLayout.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 401.02 | **LOC:** 388 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 0.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBitmapTextLayout` **(Many-Argument Workhorses)** (Impact: 152.8)
    * *Intent:* /** */
  * `checkIsOverflow` **(Compute Cores)** (Impact: 61.6)
  * `alignJustify` **(I/O & Config Routines)** (Impact: 7.3)
  * `nextWord` **(Compute Cores)** (Impact: 7.1)
  * `alignCenter` **(State Mutators)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.402
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.010035
  * `Imports (Out-Degree: 3):` TextStyle, textTokenization, AbstractBitmapFont
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/scene/text/utils/canvasTextSplit.ts` -> Churn: **66.96%** | Cog Load: 69.3262% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/culling/__tests__/Culler.test.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 1133.5
- `src/scene/container/__tests__/getLocalBounds.test.ts` -> **Mat Groves** (100.0% isolated ownership) | Magnitude: 739.42
- `src/scene/graphics/__tests__/Graphics.Drawing.test.ts` -> **Mat Groves** (100.0% isolated ownership) | Magnitude: 623.8
- `src/scene/graphics/shared/GraphicsContext.ts` -> **Mat Groves** (100.0% isolated ownership) | Magnitude: 579.68
- `src/scene/text/canvas/utils/measureTaggedText.ts` -> **Zyie** (100.0% isolated ownership) | Magnitude: 567.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 2.155** (Bridge: 0.0215 * Flux: 100.0%)
- `src/scene/container/Container.ts` -> **Severity: 1.659** (Bridge: 0.0166 * Flux: 99.9971%)
- `src/rendering/renderers/shared/texture/Texture.ts` -> **Severity: 1.1** (Bridge: 0.011 * Flux: 100.0%)
- `src/rendering/renderers/shared/system/AbstractRenderer.ts` -> **Severity: 0.925** (Bridge: 0.0092 * Flux: 100.0%)
- `src/filters/FilterSystem.ts` -> **Severity: 0.869** (Bridge: 0.0087 * Flux: 99.9978%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/maths/matrix/Matrix.ts` -> **Severity: 14.657** (Embedded: 0.1529 * Error Risk: 95.8709%)
- `src/extensions/Extensions.ts` -> **Severity: 14.59** (Embedded: 0.1857 * Error Risk: 78.5835%)
- `src/scene/container/bounds/Bounds.ts` -> **Severity: 14.024** (Embedded: 0.1415 * Error Risk: 99.08%)
- `src/rendering/renderers/shared/texture/Texture.ts` -> **Severity: 13.468** (Embedded: 0.1507 * Error Risk: 89.3997%)
- `src/color/Color.ts` -> **Severity: 11.268** (Embedded: 0.1269 * Error Risk: 88.8092%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/extensions/Extensions.ts` -> **Severity: 1337.717** (Blast Radius: 18.951 * Doc Risk: 70.5882%)
- `src/utils/logging/deprecation.ts` -> **Severity: 940.4** (Blast Radius: 9.404 * Doc Risk: 100.0%)
- `src/environment/canvas/ICanvasRenderingContext2D.ts` -> **Severity: 564.16** (Blast Radius: 14.104 * Doc Risk: 40.0%)
- `src/scene/container/Container.ts` -> **Severity: 324.198** (Blast Radius: 13.54 * Doc Risk: 23.9437%)
- `src/rendering/renderers/gl/WebGLRenderer.ts` -> **Severity: 318.2** (Blast Radius: 3.182 * Doc Risk: 100.0%)

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
