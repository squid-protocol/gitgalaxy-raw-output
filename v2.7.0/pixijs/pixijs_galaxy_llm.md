# ARCHITECTURAL_BRIEF: pixijs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pixijs/pixijs.git` |
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
| Avg Path Length | 3.5547 | Hops between files. Lower = Tighter coupling. |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 47.2 | 58.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.2 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 79.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 67.0 | 8.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 44.5 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `isDataUrl` (@ `src/utils/path.ts`) -> Impact: **217.2** | LOC: 639
  * *Intent:* /** * Checks if the path is a URL e.g. http://, https:// * @param path - The path to check * @example * ```ts * // Check if a path is a URL * path.isU...
- `wordWrapTaggedLines` (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **168.6** | LOC: 303
  * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining style information. * @param runsByLine - Array of...
- `getBitmapTextLayout` (@ `src/scene/text-bitmap/utils/getBitmapTextLayout.ts`) -> Impact: **152.8** | LOC: 284
  * *Intent:* /** * @param chars * @param style * @param font * @param trimEnd * @internal */
- `renderChildren` (@ `src/scene/graphics/shared/svg/SVGParser.ts`) -> Impact: **143.7** | LOC: 236
  * *Intent:* /** * Recursively renders SVG elements and their children. * Handles styling inheritance and different SVG shape types. * @param svg - The SVG element...
- `buildLine` (@ `src/scene/graphics/shared/buildCommands/buildLine.ts`) -> Impact: **130.7** | LOC: 391
  * *Intent:* /** * Builds a line to draw using the polygon method. * @param points * @param lineStyle * @param flipAlignment * @param closed * @param vertices * @p...
- `execute` (@ `src/scene/graphics/canvas/CanvasGraphicsAdaptor.ts`) -> Impact: **128.2** | LOC: 244
- `recursive` (@ `src/scene/graphics/shared/buildCommands/buildAdaptiveBezier.ts`) -> Impact: **116.7** | LOC: 187
  * *Intent:* // eslint-disable-next-line max-params
- `_renderTaggedTextToCanvas` (@ `src/scene/text/canvas/CanvasTextGenerator.ts`) -> Impact: **108.7** | LOC: 264
  * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. * @param measured - The measured text metrics containing runsByLine * @param style - The ba...
- `measureTaggedText` (@ `src/scene/text/canvas/utils/measureTaggedText.ts`) -> Impact: **105.3** | LOC: 186
  * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line metrics. * @param text - The tagged text to measure *...
- `execute` (@ `src/rendering/batcher/canvas/CanvasBatchAdaptor.ts`) -> Impact: **99.9** | LOC: 196

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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `transcoders/basis/basis_transcoder.js` (JAVASCRIPT) -> Cumulative Risk: **639.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2349.88 | **LOC:** 1265 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6448%)
- **Heaviest Functions:** `craftInvokerFunction` (Impact: 65.0), `__embind_register_std_string` (Impact: 51.4), `genericPointerToWireType` (Impact: 41.5)

### 2. `src/scene/text-html/utils/loadSVGImage.ts` (TYPESCRIPT) -> Cumulative Risk: **630.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 34.84 | **LOC:** 36 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.2014%)
- **Heaviest Functions:** `loadSVGImage` (Impact: 5.1), `onload` (Impact: 1.4)

### 3. `scripts/jest/jest-global-setup.ts` (TYPESCRIPT) -> Cumulative Risk: **622.53**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 42.52 | **LOC:** 43 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.6316%)
- **Heaviest Functions:** `exports` (Impact: 5.9)

### 4. `src/assets/loader/parsers/textures/loadVideoTextures.ts` (TYPESCRIPT) -> Cumulative Risk: **617.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 16.6 | **LOC:** 301 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4669%), Concurrency (93.9849%), Verification (80.0%)
- **Heaviest Functions:** `load` (Impact: 53.4), `crossOrigin` (Impact: 14.6), `determineCrossOrigin` (Impact: 11.4)

### 5. `.stackblitz/bunny-mark/src/index.js` (JAVASCRIPT) -> Cumulative Risk: **602.17**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 109.48 | **LOC:** 195 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Concurrency (99.4491%)
- **Heaviest Functions:** `renderUpdate` (Impact: 9.6), `onclick` (Impact: 3.9), `addBunnies` (Impact: 3.6)

### 6. `src/rendering/renderers/gpu/GpuEncoderSystem.ts` (TYPESCRIPT) -> Cumulative Risk: **600.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 168.46 | **LOC:** 318 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.4255%), Verification (80.0%)
- **Heaviest Functions:** `draw` (Impact: 25.5), `_setShaderBindGroups` (Impact: 7.7), `setGeometry` (Impact: 6.2)

### 7. `playground/src/scenes/sceneRunner.ts` (TYPESCRIPT) -> Cumulative Risk: **600.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 54.76 | **LOC:** 97 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (93.8671%)
- **Heaviest Functions:** `getEnabledRenderers` (Impact: 8.4), `runScene` (Impact: 6.8)

### 8. `src/rendering/renderers/canvas/utils/canvasUtils.ts` (TYPESCRIPT) -> Cumulative Risk: **599.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 330.7 | **LOC:** 507 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.9596%)
- **Heaviest Functions:** `getCanvasSource` (Impact: 59.4), `tintWithPerPixel` (Impact: 23.4), `tintWithMultiply` (Impact: 21.4)

### 9. `src/scene/text-bitmap/utils/getBitmapTextLayout.ts` (TYPESCRIPT) -> Cumulative Risk: **593.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 401.02 | **LOC:** 388 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.8431%), Verification (80.0%)
- **Heaviest Functions:** `getBitmapTextLayout` (Impact: 152.8), `checkIsOverflow` (Impact: 61.6), `alignJustify` (Impact: 7.3)

### 10. `src/math-extras/pointExtras.ts` (TYPESCRIPT) -> Cumulative Risk: **593.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 125.24 | **LOC:** 132 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.36%), Documentation (91.3043%)
- **Heaviest Functions:** `rotate` (Impact: 7.5), `reflect` (Impact: 6.0), `project` (Impact: 5.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2349.88 | **LOC:** 1265 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7349%), Tech Debt (20.2109%)
**Top Internal Functions/Classes:**
  * `craftInvokerFunction` (Impact: 65.0)
  * `__embind_register_std_string` (Impact: 51.4)
  * `genericPointerToWireType` (Impact: 41.5)
  * `__embind_register_class` (Impact: 34.9)
  * `stringToUTF8Array` (Impact: 34.6)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1133.5 | **LOC:** 479 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.3533%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 854.42 | **LOC:** 1487 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5291%), Tech Debt (9.2328%)
**Top Internal Functions/Classes:**
  * `hitTestMoveRecursive` (Impact: 70.4)
  * `mapPointerMove` (Impact: 59.0)
    * *Intent:* /** * Maps the upstream `pointermove` to downstream `pointerout`, `pointerover`, and `pointermove` e...
  * `hitTestRecursive` (Impact: 45.1)
    * *Intent:* /** * Recursive implementation for {@link EventBoundary.hitTest hitTest}. * @param currentTarget - T...
  * `mapPointerUp` (Impact: 41.2)
    * *Intent:* /** * Maps the upstream `pointerup` event to downstream `pointerup`, `pointerupoutside`, * and `clic...
  * `propagate` (Impact: 21.2)
    * *Intent:* /** * Propagate the passed event from from {@link EventBoundary.rootTarget this.rootTarget} to its *...
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
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Point, Renderable, Container, warn, EventBoundaryTypes, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/container/__tests__/getLocalBounds.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 739.42 | **LOC:** 509 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.4866%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 695.39 | **LOC:** 477 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9108%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 634.62 | **LOC:** 389 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1222%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 631.38 | **LOC:** 940 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.7927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isDataUrl` (Impact: 217.2)
    * *Intent:* /** * Checks if the path is a URL e.g. http://, https:// * @param path - The path to check * @exampl...
  * `normalizeStringPosix` (Impact: 62.3)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `parse` (Impact: 47.7)
    * *Intent:* * // ext: '.png', * // name: 'baz' * // } * // Parse a file path * const parsedFile = path.parse('C:...
  * `parse` (Impact: 10.3)
    * *Intent:* /** * Parses a path into an object containing the 'root', `dir`, `base`, `ext`, and `name` propertie...
  * `assertPath` (Impact: 3.2)
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
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` adapter, pixi.js
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/scene/graphics/__tests__/Graphics.Drawing.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 623.8 | **LOC:** 482 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.5773%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 607.53 | **LOC:** 393 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1903%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 579.68 | **LOC:** 1285 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.1097%), Tech Debt (11.8488%)
**Top Internal Functions/Classes:**
  * `texture` (Impact: 32.9)
  * `containsPoint` (Impact: 27.4)
    * *Intent:* /** * Check to see if a point is contained within this geometry. * @param point - Point to check if ...
  * `fill` (Impact: 21.3)
  * `destroy` (Impact: 20.5)
    * *Intent:* /** * Destroys the GraphicsData object. * @param options - Options parameter. A boolean will act as ...
  * `setTransform` (Impact: 19.2)
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
  * `Choke Point (Betweenness):` 0.004869 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Color, Matrix, Point, PointData, GCSystem, Shader, Texture, uid...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/utils/measureTaggedText.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 567.86 | **LOC:** 633 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.5995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wordWrapTaggedLines` (Impact: 168.6)
    * *Intent:* /** * Applies word wrapping to tagged text lines. * Breaks runs at word boundaries while maintaining...
  * `measureTaggedText` (Impact: 105.3)
    * *Intent:* /** * Measures tagged text with multiple styles. * Handles per-run font measurement and per-line met...
  * `startNewLine` (Impact: 57.4)
  * `getWordGroupWidth` (Impact: 12.0)
    * *Intent:* // Helper to calculate the total width of a word group starting at index // A word group is a sequen...
  * `tokenizeTaggedRuns` (Impact: 10.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ICanvasRenderingContext2D, TextStyle, parseTaggedText, textTokenization, types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/path/GraphicsPath.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 557.0 | **LOC:** 863 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3781%), Tech Debt (9.9223%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 28.6)
    * *Intent:* /** * Applies a transformation matrix to all drawing instructions within the `GraphicsPath`. * This ...
  * `star` (Impact: 21.0)
    * *Intent:* * @param x - The x-coordinate of the center of the star. * @param y - The y-coordinate of the center...
  * `getLastPoint` (Impact: 19.8)
    * *Intent:* /** * Retrieves the last point from the current drawing instructions in the `GraphicsPath`. * This m...
  * `bezierCurveToShort` (Impact: 13.8)
    * *Intent:* /** * Adds a cubic Bezier curve to the path. * It requires two points: the second control point and ...
  * `constructor` (Impact: 12.8)
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
  * `Choke Point (Betweenness):` 0.002846 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Matrix, Point, PointData, uid, warn, Bounds, parseSVGPath, ShapePath...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/container/Container.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 546.2 | **LOC:** 2142 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.6418%), Tech Debt (11.6547%)
**Top Internal Functions/Classes:**
  * `updateTransform` (Impact: 21.1)
    * *Intent:* * @param opts - Transform options to update * @param opts.x - The x position * @param opts.y - The y...
  * `addChild` (Impact: 19.1)
    * *Intent:* * container.addChild(sprite); * * // Add multiple children * container.addChild(background, player, ...
  * `setSize` (Impact: 18.2)
    * *Intent:* /** * Sets the size of the container to the specified width and height. * This is more efficient tha...
  * `destroy` (Impact: 14.9)
    * *Intent:* /** * Removes all internal references and listeners as well as removes children from the display lis...
  * `removeChild` (Impact: 13.6)
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
  * `Choke Point (Betweenness):` 0.013797 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` Color, cullingMixin, Extensions, Matrix, Size, const, ObservablePoint, PointData...
  * `Imported By (In-Degree: 105):` (Excluded from Brief to save tokens)

### `src/events/EventSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 498.12 | **LOC:** 1168 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.2546%), Tech Debt (8.7162%)
**Top Internal Functions/Classes:**
  * `_normalizeToPointerData` (Impact: 70.2)
    * *Intent:* /** * Ensures that the original event object contains all data that a regular pointer event would ha...
  * `setCursor` (Impact: 26.6)
    * *Intent:* * * // Using callback-based cursor * app.renderer.events.cursorStyles.dynamic = (mode) => { * docume...
  * `_addEvents` (Impact: 13.2)
    * *Intent:* /** Register event listeners on {@link Renderer#domElement this.domElement}. */
  * `_removeEvents` (Impact: 12.8)
    * *Intent:* /** Unregister event listeners on {@link EventSystem#domElement this.domElement}. */
  * `_onPointerDown` (Impact: 11.6)
    * *Intent:* /** * Event handler for pointer down events on {@link EventSystem#domElement this.domElement}. * @pa...
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
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Extensions, PointData, System, types, EventBoundary, EventTicker, FederatedEvent, FederatedEventTarget...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/scene/text/canvas/CanvasTextGenerator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 484.64 | **LOC:** 785 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.5109%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_renderTaggedTextToCanvas` (Impact: 108.7)
    * *Intent:* /** * Renders tagged text (with per-run styles) to canvas. * @param measured - The measured text met...
  * `_renderTextToCanvas` (Impact: 91.9)
    * *Intent:* /** * Renders text to its canvas, and updates its texture. * @param style - The style of the text * ...
  * `_drawLetterSpacing` (Impact: 61.5)
    * *Intent:* * 1. Native letter spacing if supported by the browser * 2. Manual letter spacing calculation if not...
  * `_setFillAndStrokeStyles` (Impact: 12.5)
    * *Intent:* /** * Sets fill and stroke styles on the canvas context for text rendering. * @param context - The c...
  * `_getAlignmentOffset` (Impact: 8.7)
    * *Intent:* /** * Calculates the X offset for text alignment. * @param lineWidth - The width of the current line...
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
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Color, Rectangle, CanvasPool, getCanvasBoundingBox, TextStyle, CanvasTextMetrics, fontStringFromTextStyle, getCanvasFillStyle...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/container/bounds/Bounds.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 474.56 | **LOC:** 1017 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.5774%), Tech Debt (9.4791%)
**Top Internal Functions/Classes:**
  * `addFrame` (Impact: 49.2)
    * *Intent:* * // Add transformed frame * const matrix = new Matrix() * .translate(50, 50) * .rotate(Math.PI / 4)...
  * `applyMatrix` (Impact: 20.3)
    * *Intent:* * Applies a transformation matrix to the bounds, updating its coordinates. * Transforms all corners ...
  * `addVertexData` (Impact: 19.6)
    * *Intent:* * .translate(50, 50) * .rotate(Math.PI / 4); * bounds.addVertexData(vertices, 0, 6, matrix); * * // ...
  * `fitBounds` (Impact: 11.7)
    * *Intent:* * ```ts * const bounds = new Bounds(0, 0, 200, 200); * // Fit to specific coordinates * bounds.fitBo...
  * `containsPoint` (Impact: 9.1)
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
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Matrix, Rectangle
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/buildCommands/buildLine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 458.6 | **LOC:** 555 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.7431%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `buildLine` (Impact: 130.7)
    * *Intent:* /** * Builds a line to draw using the polygon method. * @param points * @param lineStyle * @param fl...
  * `round` (Impact: 33.5)
    * *Intent:* * * Ignored from docs since it is not directly exposed. * @ignore * @private * @param {number} cx - ...
  * `square` (Impact: 11.2)
    * *Intent:* * * Ignored from docs since it is not directly exposed. * @ignore * @private * @param {number} x - X...
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
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Point, FillTypes, const, getOrientationOfPoints
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/scene/graphics/shared/Graphics.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 448.9 | **LOC:** 2048 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9398%), Tech Debt (9.0905%)
**Top Internal Functions/Classes:**
  * `texture` (Impact: 15.9)
  * `setTransform` (Impact: 15.9)
  * `transform` (Impact: 15.9)
  * `lineStyle` (Impact: 14.8)
    * *Intent:* // -------- v7 deprecations --------- /** * @param width * @param color * @param alpha * @deprecated...
  * `constructor` (Impact: 12.8)
    * *Intent:* /** * Creates a new Graphics object. * @param options - Options for the Graphics. */
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
  * `Choke Point (Betweenness):` 0.001239 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` Color, Matrix, PointData, Instruction, Texture, deprecation, Bounds, destroyTypes...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/filters/FilterSystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 446.74 | **LOC:** 1093 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.4901%), Tech Debt (9.8496%)
**Top Internal Functions/Classes:**
  * `_calculateFilterBounds` (Impact: 55.6)
  * `_updateFilterUniforms` (Impact: 25.0)
    * *Intent:* /** * Updates the filter uniforms with the current filter state. * @param input - The input texture ...
  * `_calculateFilterArea` (Impact: 16.0)
    * *Intent:* /** * Calculates the filter area bounds based on the instruction type. * @param instruction - The fi...
  * `_applyFiltersToTexture` (Impact: 11.5)
  * `_setupBindGroupsAndRender` (Impact: 9.8)
    * *Intent:* /** * Sets up the bind groups and renders the filter. * @param filter - The filter to apply * @param...
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
  * `Choke Point (Betweenness):` 0.008887 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` Extensions, PassthroughFilter, Matrix, Rectangle, WebGLRenderer, WebGPURenderer, BindGroup, Renderable...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/scene/text/TextStyle.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 415.48 | **LOC:** 1549 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.6365%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertV7Tov8Style` (Impact: 53.0)
  * `destroy` (Impact: 21.6)
    * *Intent:* /** * Destroys this text style. * @param options - Options parameter. A boolean will act as if all o...
  * `dropShadow` (Impact: 9.2)
  * `_isFillStyle` (Impact: 8.7)
  * `constructor` (Impact: 8.6)
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
  * `Choke Point (Betweenness):` 0.000145 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Color, Filter, uid, deprecation, warn, destroyTypes, FillTypes, GraphicsContext...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `src/spritesheet/__tests__/spritesheetAsset.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 413.07 | **LOC:** 239 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.7155%), Tech Debt (0.0%)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 408.04 | **LOC:** 708 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.2965%), Tech Debt (10.2621%)
**Top Internal Functions/Classes:**
  * `destroyGpuRenderTarget` (Impact: 89.0)
    * *Intent:* /** * destroys the gpu render target * @param {RendererRenderTarget} gpuRenderTarget - the gpu rende...
  * `bind` (Impact: 42.5)
    * *Intent:* * - When `renderSurface` is a {@link Texture}, `renderer.render({ container, target: texture, mipLev...
  * `clear` (Impact: 15.9)
  * `renderStart` (Impact: 14.4)
    * *Intent:* /** * called when the renderer starts to render a scene. * @param options * @param options.target - ...
  * `clear` (Impact: 13.8)
    * *Intent:* /** * clears the current render target to the specified color * @param {RenderTarget} renderTarget -...
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
  * `Choke Point (Betweenness):` 0.001947 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Color, ICanvas, Matrix, Rectangle, CanvasRenderTargetAdaptor, GlRenderTarget, const, GpuRenderTarget...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/accessibility/AccessibilitySystem.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 402.66 | **LOC:** 913 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.5533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_addChild` (Impact: 35.9)
    * *Intent:* /** * Creates or reuses a div element for a Container and adds it to the accessibility layer. * Sets...
  * `postrender` (Impact: 25.1)
    * *Intent:* /** * Updates the accessibility layer during rendering. * - Removes divs for containers no longer in...
  * `_deactivate` (Impact: 13.7)
    * *Intent:* /** * Deactivates the accessibility system. Removes listeners and accessibility elements. * @private...
  * `_updateAccessibleObjects` (Impact: 11.3)
    * *Intent:* /** * This recursive function will run through the scene graph and add any new accessible objects to...
  * `_activate` (Impact: 11.2)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` CanvasObserver, FederatedEvent, Extensions, Rectangle, System, types, Container, isMobile...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/scene/text-bitmap/utils/getBitmapTextLayout.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 401.02 | **LOC:** 388 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (70.2114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBitmapTextLayout` (Impact: 152.8)
    * *Intent:* /** * @param chars * @param style * @param font * @param trimEnd * @internal */
  * `checkIsOverflow` (Impact: 61.6)
  * `alignJustify` (Impact: 7.3)
  * `nextWord` (Impact: 7.1)
  * `alignCenter` (Impact: 4.9)
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
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` TextStyle, textTokenization, AbstractBitmapFont
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
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

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/rendering/renderers/shared/texture/sources/TextureSource.ts` -> **Severity: 2.069** (Bridge: 0.0207 * Flux: 100.0%)
- `src/scene/container/Container.ts` -> **Severity: 1.38** (Bridge: 0.0138 * Flux: 99.9971%)
- `src/assets/loader/Loader.ts` -> **Severity: 0.981** (Bridge: 0.0098 * Flux: 99.9131%)
- `src/rendering/renderers/shared/system/AbstractRenderer.ts` -> **Severity: 0.966** (Bridge: 0.0097 * Flux: 100.0%)
- `src/assets/Assets.ts` -> **Severity: 0.961** (Bridge: 0.0096 * Flux: 99.7144%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/extensions/Extensions.ts` -> **Severity: 1337.717** (Blast Radius: 18.951 * Doc Risk: 70.5882%)
- `src/utils/logging/deprecation.ts` -> **Severity: 940.4** (Blast Radius: 9.404 * Doc Risk: 100.0%)
- `src/environment/canvas/ICanvasRenderingContext2D.ts` -> **Severity: 564.16** (Blast Radius: 14.104 * Doc Risk: 40.0%)
- `src/scene/container/Container.ts` -> **Severity: 324.198** (Blast Radius: 13.54 * Doc Risk: 23.9437%)
- `src/rendering/renderers/gl/WebGLRenderer.ts` -> **Severity: 318.2** (Blast Radius: 3.182 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
