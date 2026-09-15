# ARCHITECTURAL_BRIEF: gutenberg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wordpress/gutenberg.git` |
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
| Total Artifacts | 12229 |
| Analyzed Artifacts (Scanned) | 11103 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1126 |
| Total LOC | 791725 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6599 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2343 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.51 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 517 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4150 | 435845 | 37.4% |
| TYPESCRIPT | 2431 | 227341 | 21.9% |
| JSON | 1101 | 34811 | 9.9% |
| CSS | 836 | 34379 | 7.5% |
| MARKDOWN | 744 | 0 | 6.7% |
| HTML | 675 | 2134 | 6.1% |
| PHP | 469 | 48272 | 4.2% |
| XML | 380 | 1 | 3.4% |
| PLAINTEXT | 224 | 2 | 2.0% |
| JAVA | 29 | 4089 | 0.3% |
| SWIFT | 20 | 2749 | 0.2% |
| SHELL | 10 | 505 | 0.1% |
| KOTLIN | 9 | 782 | 0.1% |
| GROOVY | 8 | 312 | 0.1% |
| OBJECTIVE-C | 6 | 134 | 0.1% |
| RUBY | 4 | 110 | 0.0% |
| YAML | 3 | 40 | 0.0% |
| BATCH | 3 | 211 | 0.0% |
| PYTHON | 1 | 8 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -0.91; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 18%, Callbacks & Closures Files 10%, Defensive Guards Files 8%, Interface Declarations Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10133 | 91.3% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 966 | 8.7% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1126*

**Composition by Extension & Reason:**
- `.md`: 239x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3442 LOC)
- `.png`: 176x Excluded (Explicitly Denied Extension: '.png')
- `.html`: 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 33x Excluded (Saturation: Line 2 exceeds 500 chars), 15x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.snap`: 121x Unsupported Format (.snap), 17x Excluded (Unsupported Extension: '.snap'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Saturation: Line 8 exceeds 500 chars), 2x Excluded (Saturation: Line 17 exceeds 500 chars)
- `no_extension`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable), 4x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.mustache`: 38x Excluded (Unsupported Extension: '.mustache'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 24291 LOC), 1x Excluded (Monolithic Amalgamation: 63386 LOC exceeds safe regex boundaries)
- `.jpg`: 18x Excluded (Explicitly Denied Extension: '.jpg')
- `.template`: 14x Excluded (Unsupported Extension: '.template')
- `.woff2`: 11x Excluded (Explicitly Denied Extension: '.woff2')
- `.ttf`: 10x Excluded (Explicitly Denied Extension: '.ttf')
- `.php`: 2x Excluded (Saturation: Line 54 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 464 LOC), 1x Excluded (Machine-Generated Source Code Signature: 93 LOC)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 59269 LOC exceeds safe regex boundaries)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.8 | 3.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 20.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.2 | 4.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 57.3 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 60.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.1 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 74.5 | 4.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3102 | 978 | 0 | `packages/core-data/src/utils/test/crdt-blocks.ts` |
| cleanup | 484 | 245 | 0 | `lib/class-wp-theme-json-gutenberg.php` |
| guards | 23717 | 3445 | 6 | `lib/class-wp-theme-json-gutenberg.php` |
| danger | 4508 | 1389 | 1 | `packages/react-native-editor/bin/generate-pot-files.sh` |
| concurrency | 30148 | 1717 | 2 | `test/e2e/specs/editor/blocks/navigation.spec.js` |
| connectivity | 16789 | 5670 | 3 | `packages/theme/src/prebuilt/css/design-tokens.css` |
| io | 2913 | 671 | 0 | `packages/wp-build/lib/build.mjs` |
| crypto | 3 | 3 | 0 | `packages/react-native-editor/__device-tests__/helpers/utils.js` |
| ipc | 68 | 40 | 0 | `packages/upload-media/src/test/feature-detection.ts` |
| time | 763 | 238 | 0 | `packages/components/src/calendar/stories/date-range-calendar.story.tsx` |
| serialization | 333 | 178 | 0 | `packages/element/src/test/create-interpolate-element.tsx` |
| regex | 1091 | 491 | 0 | `packages/autop/src/index.ts` |
| events | 2920 | 694 | 0 | `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` |
| tests | 38258 | 1339 | 5 | `packages/block-editor/src/store/test/reducer.js` |
| docs | 21851 | 6553 | 4 | `packages/editor/src/store/selectors.js` |
| debt | 1689 | 601 | 0 | `bin/cherry-pick.mjs` |
| mutation | 123857 | 6793 | 29 | `packages/global-styles-ui/src/font-library/lib/inflate.js` |
| dead_code | 2559 | 804 | 0 | `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` |
| credential | 57 | 26 | 0 | `packages/dataviews/src/dataviews-picker/stories/fixtures.tsx` |
| threat | 1156 | 393 | 0 | `test/integration/fixtures/documents/ms-word-in.html` |
| ml_ai | 254 | 89 | 0 | `test/integration/fixtures/blocks/core__math.html` |
| ui | 28878 | 3787 | 8 | `packages/components/src/menu/stories/index.story.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/wp-build/lib/build.mjs` (Hits: 97)
- `packages/components/src/navigator/test/index.tsx` (Hits: 46)
- `packages/global-styles-ui/src/global-styles-ui.tsx` (Hits: 42)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i18n.js** (`packages/eslint-plugin/configs/i18n.js`) — 1348 inbound connections
2. **components.tsx** (`storybook/stories/tokens/components.tsx`) — 1165 inbound connections
3. **init-block.js** (`packages/block-library/src/utils/init-block.js`) — 121 inbound connections
4. **test.ts** (`packages/e2e-test-utils-playwright/src/test.ts`) — 106 inbound connections
5. **keycodes.ts** (`packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts`) — 97 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`packages/block-library/src/index.js`) — 133 outbound dependencies
2. **index.ts** (`packages/components/src/index.ts`) — 130 outbound dependencies
3. **index.js** (`packages/block-editor/src/components/index.js`) — 111 outbound dependencies
4. **index.js** (`packages/editor/src/components/index.js`) — 89 outbound dependencies
5. **index.native.js** (`packages/components/src/index.native.js`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inflate` **(Many-Argument Workhorses)** (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> Impact: **483.5** | LOC: 1426
- `Image` **(Compute Cores)** (@ `packages/block-library/src/image/image.js`) -> Impact: **351.4** | LOC: 1032
- `gutenberg_get_layout_style` **(Many-Argument Workhorses)** (@ `lib/block-supports/layout.php`) -> Impact: **284.0** | LOC: 363
  * *Intent:* /** * Generates the CSS corresponding to the provided layout. * * @param string $selector CSS selector. * @param array $layout Layout object. The one ...
- `save` **(Compute Cores)** (@ `packages/block-editor/src/store/test/selectors.js`) -> Impact: **283.6** | LOC: 3551
- `Navigation` **(Compute Cores)** (@ `packages/block-library/src/navigation/edit/index.js`) -> Impact: **227.5** | LOC: 929
- `FontLibraryProvider` **(Defensive Guards)** (@ `packages/global-styles-ui/src/font-library/context.tsx`) -> Impact: **220.0** | LOC: 525
- `gutenberg_render_layout_support_flag` **(Many-Argument Workhorses)** (@ `lib/block-supports/layout.php`) -> Impact: **218.9** | LOC: 429
  * *Intent:* /** * Renders the layout config to the block wrapper. * * @param string $block_content Rendered block content. * @param array $block Block object. * @...
- `CoverEdit` **(Compute Cores)** (@ `packages/block-library/src/cover/edit/index.js`) -> Impact: **204.8** | LOC: 645
- `TypographyPanel` **(Defensive Guards)** (@ `packages/block-editor/src/components/global-styles/typography-panel.js`) -> Impact: **202.3** | LOC: 539
- `GalleryEdit` **(Compute Cores)** (@ `packages/block-library/src/gallery/edit.js`) -> Impact: **197.9** | LOC: 875

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/e2e/specs/editor/various` | 100 | 15471.7 | 56.4% | 0.0% |
| `test/e2e/specs/editor/blocks` | 39 | 9787.86 | 62.64% | 0.0% |
| `test/e2e/specs/interactivity` | 31 | 8732.48 | 18.44% | 0.0% |
| `packages/global-styles-ui/src/font-library/lib` | 4 | 8076.48 | 66.69% | 30.11% |
| `lib` | 23 | 6511.52 | 20.43% | 22.96% |
| `__monolith__` | 16 | 5132.18 | 1.31% | 4.57% |
| `packages/vips` | 5 | 5021.44 | 0.0% | 0.0% |
| `test/e2e/specs/editor/collaboration` | 16 | 4428.83 | 56.55% | 0.0% |
| `test/e2e/specs/site-editor` | 48 | 4205.72 | 24.77% | 0.0% |
| `packages/block-editor/src/hooks` | 66 | 3972.94 | 7.95% | 3.14% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/block-library/src/navigation-submenu/transforms.js` -> **100.0%** Exposure
- `lib/experimental/class--wp-editors.php` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-gutenberg-fonts-api-bc-layer.php` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-wp-fonts-provider.php` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-wp-fonts-resolver.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/api-docs/gen-block-lib-list.js` -> **100.0%** Exposure
- `bin/api-docs/gen-theme-reference.mjs` -> **100.0%** Exposure
- `packages/a11y/src/shared/clear.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/filter-message.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/index.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` -> **79** Orphaned Functions | **0** Duplicates
- `phpunit/tests/collaboration/wpHttpPollingSyncServer.php` -> **60** Orphaned Functions | **0** Duplicates
- `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/RNReactNativeGutenbergBridgeModule.java` -> **57** Orphaned Functions | **0** Duplicates
- `packages/block-editor/src/store/test/actions.js` -> **0** Orphaned Functions | **43** Duplicates
- `packages/react-native-editor/android/app/src/main/java/com/gutenberg/MainApplication.kt` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/e2e/specs/editor/blocks/avatar.spec.js` -> **99.8994%** Exposure
- `packages/eslint-plugin/rules/__tests__/no-unknown-ds-tokens.js` -> **99.2872%** Exposure
- `test/e2e/specs/editor/various/autocomplete-and-mentions.spec.js` -> **98.6603%** Exposure
- `packages/dataviews/src/hooks/test/use-form-validity.ts` -> **12.2948%** Exposure
- `packages/dataviews/src/dataform/stories/validation.tsx` -> **11.6568%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `19` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14948` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergEmbedWebViewActivity.java` (JAVA) -> Cumulative Risk: **741.78**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.45)
- **Magnitude:** 112.16 | **LOC:** 161 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7618%), Concurrency (99.7109%)
- **Heaviest Functions:** `onPageStarted` (Compute Cores, Impact: 10.4), `onProgressChanged` (Compute Cores, Impact: 7.6), `onCreate` (Compute Cores, Impact: 7.5)

### 2. `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` (JAVASCRIPT) -> Cumulative Risk: **717.12**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.07)
- **Magnitude:** 2549.12 | **LOC:** 3862 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9965%), Cognitive Load (96.6361%)
- **Heaviest Functions:** `constructor` (Many-Argument Workhorses, Impact: 21.9), `createSubTable` (Defensive Guards, Impact: 20.6), `constructor` (Many-Argument Workhorses, Impact: 18.2)

### 3. `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT) -> Cumulative Risk: **713.45**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.33)
- **Magnitude:** 907.52 | **LOC:** 1140 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (98.3871%), Cognitive Load (96.558%)
- **Heaviest Functions:** `getBlockAtPosition` (Many-Argument Workhorses, Impact: 30.6), `swipeToolbarToElement` (Compute Cores, Impact: 17.5), `findBlockButton` (Compute Cores, Impact: 14.5)

### 4. `packages/react-native-editor/ios/GutenbergDemo/GutenbergViewController.swift` (SWIFT) -> Cumulative Risk: **711.67**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.65)
- **Magnitude:** 372.9 | **LOC:** 615 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.659%), Tech Debt (99.5769%), Documentation (98.6667%)
- **Heaviest Functions:** `gutenbergDidRequestMedia` (Many-Argument Workhorses, Impact: 42.2), `gutenbergDidRequestMediaUploadActionDialog` (Defensive Guards, Impact: 18.6), `gutenbergDidEmitLog` (Compute Cores, Impact: 12.8)

### 5. `packages/react-native-bridge/common/gutenberg-web-single-block/content-functions.js` (JAVASCRIPT) -> Cumulative Risk: **684.46**
- **Archetype:** `file_cluster_17` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.16)
- **Magnitude:** 61.44 | **LOC:** 72 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `startObservingGutenberg` (Callbacks & Closures, Impact: 7.0), `getHTMLPostContent` (Callbacks & Closures, Impact: 3.8), `getBlockEditorStore` (Callbacks & Closures, Impact: 3.6)

### 6. `packages/react-native-bridge/ios/RNReactNativeGutenbergBridge.swift` (SWIFT) -> Cumulative Risk: **682.27**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.91)
- **Magnitude:** 396.18 | **LOC:** 481 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.993%), Tech Debt (99.939%), Documentation (98.3333%)
- **Heaviest Functions:** `requestMediaPickFrom` (Many-Argument Workhorses, Impact: 19.3), `postRequest` (Annotated Framework Methods, Impact: 14.0), `requestImageFullscreenPreview` (Defensive Guards, Impact: 13.3)

### 7. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergWebViewActivity.java` (JAVA) -> Cumulative Risk: **674.01**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.75)
- **Magnitude:** 241.72 | **LOC:** 447 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.1498%), Tech Debt (87.3485%)
- **Heaviest Functions:** `onCreate` (Compute Cores, Impact: 8.0), `onOptionsItemSelected` (Compute Cores, Impact: 7.9), `onProgressChanged` (Compute Cores, Impact: 7.6)

### 8. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` (JAVA) -> Cumulative Risk: **670.5**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.26)
- **Magnitude:** 842.48 | **LOC:** 1178 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9961%), Documentation (99.1525%), State Flux (98.5281%)
- **Heaviest Functions:** `getPackages` (Annotated Framework Methods, Impact: 62.5), `requestMediaPickFromMediaLibrary` (Compute Cores, Impact: 29.2), `attachToContainer` (Many-Argument Workhorses, Impact: 18.6)

### 9. `bin/generate-php-sync-issue.mjs` (JAVASCRIPT) -> Cumulative Risk: **665.05**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.39)
- **Magnitude:** 350.06 | **LOC:** 456 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9969%), Concurrency (99.9903%)
- **Heaviest Functions:** `main` (I/O & Config Routines, Impact: 25.6), `processCommits` (Compute Cores, Impact: 21.3), `reduceNesting` (Defensive Guards, Impact: 14.4)

### 10. `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecManager.java` (JAVA) -> Cumulative Risk: **662.15**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.22)
- **Magnitude:** 538.58 | **LOC:** 875 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9594%), Tech Debt (99.915%), Documentation (93.0%)
- **Heaviest Functions:** `setTextAlign` (Compute Cores, Impact: 33.1), `receiveCommand` (Many-Argument Workhorses, Impact: 21.6), `getHeadingScale` (Compute Cores, Impact: 20.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vips/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/inflate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3877.3 | **LOC:** 4096 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (95.6225%), Tech Debt (8.0366%)
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 483.5)
  * `inflate_table` **(Many-Argument Workhorses)** (Impact: 159.9)
  * `inflate_fast` **(Many-Argument Workhorses)** (Impact: 110.9)
    * *Intent:* */
  * `push` **(Defensive Guards)** (Impact: 64.8)
    * *Intent:* * We strongly recommend to use `Uint8Array` on input for best speed (output * format is detected aut...
  * `Inflate` **(Compute Cores)** (Impact: 34.4)
    * *Intent:* * var pako = require('pako') * , chunk1 = Uint8Array([1,2,3,4,5,6,7,8,9]) * , chunk2 = Uint8Array([1...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 815 instances
* *State Mutation (weighted view):* 2606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 372`, `args: 57`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 976`, `dead_code: 20`, `planned_debt: 2`
* *Architecture:* `api: 40`, `import: 14`
* *Defense:* `safety: 156`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000263
  * `Imports (Out-Degree: 3):` common, adler32, common, crc32, inffast, inftrees, common, strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/class-wp-theme-json-gutenberg.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3704.36 | **LOC:** 5073 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 32.0%
- **Risk Profile:** Cognitive Load (47.8002%), Tech Debt (12.5204%)
**Top Internal Functions/Classes:**
  * `get_layout_styles` **(Many-Argument Workhorses)** (Impact: 127.2)
    * *Intent:* /** * Gets the CSS layout rules for a particular block from theme.json layout definitions. * * @sinc...
  * `compute_style_properties` **(Many-Argument Workhorses)** (Impact: 100.8)
    * *Intent:* * @since 5.9.0 Added the `$settings` and `$properties` parameters. * @since 6.1.0 Added `$theme_json...
  * `get_block_nodes` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* * An internal method to get the block nodes from a theme.json file. * * @since 6.1.0 * * @param arra...
  * `get_styles_for_block` **(Compute Cores)** (Impact: 81.0)
    * *Intent:* /** * Gets the CSS rules for a particular block from theme.json. * * @since 6.1.0 * @since 6.6.0 Set...
  * `sanitize` **(Many-Argument Workhorses)** (Impact: 79.4)
    * *Intent:* /** * Sanitizes the input according to the schemas. * * @since 5.8.0 * @since 5.9.0 Added the `$vali...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 641 instances
* *State Mutation (weighted view):* 2068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 754`, `structural_boundaries: 361`, `args: 84`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 786`, `dead_code: 3`, `unreferenced_by_name: 15`
* *Architecture:* `api: 24`
* *Defense:* `safety: 259`, `doc: 101`, `immutability_locks: 18`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $class_name, $name, $nested_selector, $nested_selector )
					: static::append_to_selector( $selector, $node ) 
		$node['selector'] = static::scope_selector( $scope, $node['selector'], $options = array() ) 
		$nodes = array(, $options = array() ) 
		if ( null === $origins ) 
			$origins = static::VALID_ORIGINS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2549.12 | **LOC:** 3862 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.6361%), Tech Debt (12.4343%)
**Top Internal Functions/Classes:**
  * `constructor` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `createSubTable` **(Defensive Guards)** (Impact: 20.6)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `constructor` **(Defensive Guards)** (Impact: 17.9)
  * `buildWoffLazyLookups` **(Many-Argument Workhorses)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 210 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 1220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 1048`, `args: 586`, `func_start: 324`, `class_start: 165`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 800`, `dead_code: 12`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 49`, `concurrency: 97`, `import: 2`
* *Defense:* `safety: 126`, `doc: 1`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.097
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000285
  * `Imports (Out-Degree: 2):` inflate, unbrotli, fs, pako, zlib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/e2e/specs/editor/blocks/list.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2275.9 | **LOC:** 1743 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 242 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 1644
* *State Mutation (weighted view):* 587
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 517`, `args: 61`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 583`
* *Architecture:* `concurrency: 434`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/interactivity/directive-each.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2000.25 | **LOC:** 705 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0907%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 296
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 235`, `args: 53`, `func_start: 29`
* *Risk/State:* `state_mutation: 7`, `planned_debt: 1`
* *Architecture:* `concurrency: 216`, `import: 1`
* *Defense:* `doc: 1`, `test: 159`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fixtures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/unbrotli.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1649.16 | **LOC:** 2689 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (67.1662%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BrotliDecompress` **(Many-Argument Workhorses)** (Impact: 102.3)
  * `ReadHuffmanCode` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `CopyUncompressedBlockToOutput` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `ReadHuffmanCodeLengths` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `BrotliBuildHuffmanTable` **(Many-Argument Workhorses)** (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 286 instances
* *State Mutation (weighted view):* 976
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 341`, `args: 64`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 404`, `dead_code: 3`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 56`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.113
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000263
  * `Imports (Out-Degree: 0):` bit_reader, context, decode, decode, dictionary, dictionary-browser, dictionary.bin.js, huffman...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/block-editor/src/store/reducer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1625.56 | **LOC:** 3138 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (34.4456%), Tech Debt (8.002%)
**Top Internal Functions/Classes:**
  * `withDerivedBlockEditingModes` **(Defensive Guards)** (Impact: 164.5)
    * *Intent:* /** * Higher-order reducer that adds derived block editing modes to the state. * * This function wra...
  * `withResetControlledBlocks` **(Compute Cores)** (Impact: 124.6)
    * *Intent:* /** * Higher-order reducer which removes blocks from state when switching parent block controlled st...
  * `getDerivedBlockEditingModesForTree` **(Many-Argument Workhorses)** (Impact: 92.4)
    * *Intent:* /** * Computes and returns derived block editing modes for a given block tree. * * This function cal...
  * `withBlockTree` **(Compute Cores)** (Impact: 49.9)
    * *Intent:* /** * Higher-order reducer intended to compute full block objects key for each block in the post. * ...
  * `selection` **(Defensive Guards)** (Impact: 44.4)
    * *Intent:* /** * Reducer returning the selection state. * * @param {boolean} state Current state. * @param {Obj...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 140 instances
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 559`, `structural_boundaries: 443`, `args: 134`, `func_start: 65`
* *Risk/State:* `state_mutation: 152`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 192`, `doc: 60`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lock-unlock, array, defaults, private-keys, blocks, compose, data, deprecated...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/various/writing-flow.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1395.1 | **LOC:** 1255 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writingFlowUtils` **(Many-Argument Workhorses)** (Impact: 59.0)
  * `addDemoContent` **(Interface Declarations)** (Impact: 3.0)
  * `getActiveBlockName` **(Callbacks & Closures)** (Impact: 2.4)
  * `constructor` **(State Mutators)** (Impact: 1.7)
  * `getHeight` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 145 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 1189
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 488`, `args: 62`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 112`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 464`, `import: 1`
* *Defense:* `safety: 5`, `doc: 1`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-engine/src/core/render.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1300.94 | **LOC:** 1982 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.0402%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transformToStyles` **(Many-Argument Workhorses)** (Impact: 192.7)
  * `getNodesWithStyles` **(Defensive Guards)** (Impact: 128.3)
  * `getStylesDeclarations` **(Many-Argument Workhorses)** (Impact: 83.7)
    * *Intent:* /** * Transform given style tree into a set of style declarations. * * @param blockStyles Block styl...
  * `getLayoutStyles` **(Compute Cores)** (Impact: 77.6)
    * *Intent:* /** * Get generated CSS for layout styles by looking up layout definitions provided * in theme.json,...
  * `generateGlobalStyles` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* /** * Returns the global styles output based on the current state of global styles config loaded in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 174`, `args: 76`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 150`, `dead_code: 1`
* *Architecture:* `io: 11`, `api: 13`, `import: 14`
* *Defense:* `safety: 117`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.169
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00027
  * `Imports (Out-Degree: 9):` get-setting, types, background, common, duotone, gap, layout, object...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/e2e/specs/interactivity/router-regions.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1248.26 | **LOC:** 769 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (47.2101%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 301
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 258`, `args: 26`, `func_start: 15`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `concurrency: 241`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`, `test: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fixtures, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/blocks/navigation.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1236.84 | **LOC:** 2403 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 76.5%
- **Risk Profile:** Cognitive Load (98.5621%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `navigation` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `arrowToLabel` **(Defensive Guards)** (Impact: 7.6)
  * `addPage` **(Tests & Verification)** (Impact: 6.1)
    * *Intent:* /** * Adds a page via the link control and closes it. * Usage: * - Open the new link control however...
  * `previewIsOpenAndCloses` **(Callbacks & Closures)** (Impact: 5.4)
    * *Intent:* /** * Checks: * - the preview is open * - has focus within it * - closes with Escape * - The popover...
  * `useLinkControlSearch` **(Interface Declarations)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 1071
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 733`, `args: 134`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 40`, `planned_debt: 4`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 711`, `import: 1`
* *Defense:* `safety: 13`, `doc: 17`, `test: 234`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/collaboration/collaboration-refresh.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1205.83 | **LOC:** 182 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.233%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 111
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 60`, `args: 12`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `io: 1`, `concurrency: 41`, `import: 4`
* *Defense:* `safety: 17`, `doc: 3`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fixtures, collaboration-utils, test, e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/block-supports/layout.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1200.78 | **LOC:** 1259 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (66.0539%), Tech Debt (10.3886%)
**Top Internal Functions/Classes:**
  * `gutenberg_get_layout_style` **(Many-Argument Workhorses)** (Impact: 284.0)
    * *Intent:* /** * Generates the CSS corresponding to the provided layout. * * @param string $selector CSS select...
  * `gutenberg_render_layout_support_flag` **(Many-Argument Workhorses)** (Impact: 218.9)
    * *Intent:* /** * Renders the layout config to the block wrapper. * * @param string $block_content Rendered bloc...
  * `gutenberg_restore_group_inner_container` **(Compute Cores)** (Impact: 25.3)
    * *Intent:* /** * For themes without theme.json file, make sure * to restore the inner div for the group block *...
  * `gutenberg_restore_image_outer_container` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /** * For themes without theme.json file, make sure * to restore the outer div for the aligned image...
  * `gutenberg_get_block_style_variation_name_from_registered_style` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* /** * Layout block support flag. * * @package gutenberg */ /** * Get the first style variation name ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 602
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 51`, `args: 14`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 224`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 75`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $block_spacing, $fallback_gap_value, $gap_value, $has_block_gap_support, $should_skip_gap_serialization, 'wp-container-' . sanitize_title( $block['blockName'] ) . '-is-layout-', ), d to obtain the
		 * corresponding layout style. This way...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/navigation/index.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1110.08 | **LOC:** 1812 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (35.1519%), Tech Debt (16.7662%)
**Top Internal Functions/Classes:**
  * `get_responsive_container_markup` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /** * Get the responsive container markup * * @since 6.5.0 * * @param array $attributes The block at...
  * `block_core_navigation_build_css_colors` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* /** * Build an array with CSS classes and inline styles defining the colors * which will be applied ...
  * `block_core_navigation_parse_blocks_from_menu_items` **(Defensive Guards)** (Impact: 22.9)
    * *Intent:* /** * Turns menu item data into a nested array of parsed blocks * * @since 5.9.0 * * @deprecated 6.3...
  * `get_overlay_blocks_from_template_part` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /** * Gets the inner blocks for the navigation block from an overlay template part. * * @since 6.5.0...
  * `get_inner_blocks` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /** * Gets the inner blocks for the navigation block. * * @since 6.5.0 * * @param array $attributes ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 176`, `args: 51`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 260`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 60`, `doc: 59`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` s a null block with '\n\n', static function ( $block ) 
			return isset( $block['blockName']
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sync/src/providers/http-polling/test/utils.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1050.28 | **LOC:** 664 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.0615%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 86`, `args: 65`, `func_start: 4`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 4`, `concurrency: 8`, `import: 4`
* *Defense:* `doc: 3`, `test: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types, utils, globals, api-fetch
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/selectors.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 963.64 | **LOC:** 3363 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 29.4%
- **Risk Profile:** Cognitive Load (14.2309%), Tech Debt (8.091%)
**Top Internal Functions/Classes:**
  * `canInsertBlockTypeUnmemoized` **(Many-Argument Workhorses)** (Impact: 84.8)
    * *Intent:* /** * Determines if the given block type is allowed to be inserted into the block list. * This funct...
  * `canRemoveBlock` **(Defensive Guards)** (Impact: 38.6)
    * *Intent:* /** * Determines if the given block is allowed to be deleted. * * @param {Object} state Editor state...
  * `isBlockVisibleInTheInserter` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* * Determines if the given block type is visible in the inserter. * Note that this is different than ...
  * `__unstableIsSelectionMergeable` **(Defensive Guards)** (Impact: 28.0)
    * *Intent:* /** * Check whether the selection is mergeable. * * @param {Object} state Editor state. * @param {bo...
  * `__unstableHasActiveBlockOverlayActive` **(Compute Cores)** (Impact: 26.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 502`, `args: 209`, `func_start: 95`
* *Risk/State:* `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `api: 113`, `import: 12`
* *Defense:* `safety: 133`, `doc: 120`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` block-editing-mode, lock-unlock, sorting, constants, private-selectors, utils, block-editor, blocks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 907.52 | **LOC:** 1140 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBlockAtPosition` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* // Finds the wd element for new block that was added and sets the element attribute // and accessibi...
  * `swipeToolbarToElement` **(Compute Cores)** (Impact: 17.5)
  * `findBlockButton` **(Compute Cores)** (Impact: 14.5)
    * *Intent:* // Attempts to find the given block button in the block inserter control.
  * `getTitleElement` **(Compute Cores)** (Impact: 12.6)
  * `pasteClipboardToTextBlock` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 443
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 262`, `args: 76`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 32`
* *Architecture:* `api: 49`, `concurrency: 258`, `import: 1`
* *Defense:* `safety: 20`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00063
  * `Imports (Out-Degree: 1):` utils, webdriverio
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/wp-build/lib/build.mjs` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 895.46 | **LOC:** 2181 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 19.0%
- **Risk Profile:** Cognitive Load (37.1775%), Tech Debt (9.8621%)
**Top Internal Functions/Classes:**
  * `bundlePackage` **(Many-Argument Workhorses)** (Impact: 84.1)
    * *Intent:* /** * Bundle a package for WordPress using esbuild. * * @param {string} packageName Package name. * ...
  * `transformPhpContent` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `buildAll` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* /** * Main build function. * * @param {string?} baseUrlExpression */
  * `transpilePackage` **(Compute Cores)** (Impact: 36.1)
    * *Intent:* /** * Transpile a single package's source files and copy JSON files. * * @param {string} packageName...
  * `watchMode` **(I/O & Config Routines)** (Impact: 30.1)
    * *Intent:* /** * Watch mode for development. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 261
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 264`, `args: 93`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 50`, `unreferenced_by_name: 4`
* *Architecture:* `io: 97`, `api: 2`, `concurrency: 131`, `import: 27`
* *Defense:* `safety: 63`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` , dependency-graph.mjs, package-utils.mjs, php-generator.mjs, route-utils.mjs, wordpress-externals-plugin.mjs, worker-build.mjs, autoprefixer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/create-block/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 860.86 | **LOC:** 228 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.6361%), Tech Debt (12.9892%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 12`, `args: 4`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `concurrency: 9`, `import: 9`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` package.json, check-system-requirements, cli-error, log, scaffold, templates, prompts, change-case...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 842.48 | **LOC:** 1178 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.6975%), Tech Debt (99.9961%)
**Top Internal Functions/Classes:**
  * `getPackages` **(Annotated Framework Methods)** (Impact: 62.5)
  * `requestMediaPickFromMediaLibrary` **(Compute Cores)** (Impact: 29.2)
  * `attachToContainer` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `getOtherMediaPickerOptions` **(Generic / Templated Code)** (Impact: 18.3)
  * `editorDidEmitLog` **(Compute Cores)** (Impact: 18.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 291`, `args: 144`, `func_start: 147`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 100`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 79`
* *Architecture:* `api: 113`, `concurrency: 8`, `import: 70`
* *Defense:* `safety: 6`, `doc: 2`, `sync_locks: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` android.app.Activity, android.app.Application, android.content.Context, android.content.MutableContextWrapper, android.os.Build, android.os.Bundle, android.os.Handler, android.os.Looper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/abilities/src/tests/api.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 802.97 | **LOC:** 610 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.8576%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 91`, `args: 31`, `func_start: 11`
* *Risk/State:* None
* *Architecture:* `concurrency: 22`, `import: 4`
* *Defense:* `safety: 4`, `doc: 3`, `test: 73`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` api, store, types, data
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/various/pattern-overrides.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 797.5 | **LOC:** 1487 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 67 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 668
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 362`, `args: 33`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 72`, `fragile_debt: 1`
* *Architecture:* `concurrency: 333`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/blocks/links.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 771.28 | **LOC:** 1349 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `LinkUtils` **(Many-Argument Workhorses)** (Impact: 75.7)
  * `toggleFixedToolbar` **(Callbacks & Closures)** (Impact: 3.4)
  * `createLink` **(Interface Declarations)** (Impact: 2.5)
  * `constructor` **(State Mutators)** (Impact: 1.7)
  * `getLinkPopover` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* /** * This method is used as a temporary workaround for retriveing the * LinkControl component. This...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 66 instances
* *Concurrency (weighted view):* 651
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 325`, `args: 38`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 321`, `import: 1`
* *Defense:* `safety: 1`, `doc: 2`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/core-data/src/resolvers.js` -> Churn: **65.99%** | Cog Load: 61.8064% | Debt: 8.5237%
- `lib/experimental/connectors/default-connectors.php` -> Churn: **58.31%** | Cog Load: 51.8198% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **Riad Benguella** (100.0% isolated ownership) | Magnitude: 2549.12
- `test/e2e/specs/editor/collaboration/collaboration-refresh.spec.ts` -> **Max Schmeling** (100.0% isolated ownership) | Magnitude: 1205.83
- `lib/block-supports/layout.php` -> **tellthemachines** (83.3% isolated ownership) | Magnitude: 1200.78
- `packages/react-native-editor/__device-tests__/pages/editor-page.js` -> **Ella** (100.0% isolated ownership) | Magnitude: 907.52
- `packages/create-block/lib/index.js` -> **Brian Coords** (100.0% isolated ownership) | Magnitude: 860.86

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/eslint-plugin/configs/i18n.js` -> **Severity: 7.881** (Embedded: 0.1221 * Error Risk: 64.5656%)
- `packages/e2e-test-utils-playwright/src/test.ts` -> **Severity: 0.454** (Embedded: 0.0092 * Error Risk: 49.1488%)
- `test/unit/__mocks__/@wordpress/block-library.js` -> **Severity: 0.374** (Embedded: 0.0051 * Error Risk: 73.6639%)
- `packages/core-data/src/sync.ts` -> **Severity: 0.182** (Embedded: 0.003 * Error Risk: 59.7314%)
- `packages/components/src/utils/hooks/use-cx.ts` -> **Severity: 0.137** (Embedded: 0.0024 * Error Risk: 56.5337%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `storybook/stories/tokens/components.tsx` -> **Severity: 4099.1** (Blast Radius: 40.991 * Doc Risk: 100.0%)
- `packages/e2e-test-utils-playwright/src/test.ts` -> **Severity: 540.6** (Blast Radius: 6.307 * Doc Risk: 85.7143%)
- `packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts` -> **Severity: 219.24** (Blast Radius: 3.654 * Doc Risk: 60.0%)
- `packages/core-data/src/sync.ts` -> **Severity: 170.3** (Blast Radius: 1.703 * Doc Risk: 100.0%)
- `packages/dom/src/utils/assert-is-defined.ts` -> **Severity: 121.8** (Blast Radius: 1.218 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
