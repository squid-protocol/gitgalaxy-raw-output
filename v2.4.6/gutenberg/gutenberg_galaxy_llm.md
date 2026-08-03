# ARCHITECTURAL_BRIEF: gutenberg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/gutenberg` |
| **Timestamp** | `2026-08-03T20:05:18.814523+00:00` |
| **Scan Duration** | `21.26s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `4af0efd09488abc25e84933c634230ac884cc2f8` |
| **Git Remote** | `https://github.com/wordpress/gutenberg.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6365 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 12229 |
| Analyzed Artifacts (Scanned) | 8752 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3477 |
| Total LOC | 583130 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2261 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 373 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3667 | 322640 | 41.9% |
| TYPESCRIPT | 2358 | 191350 | 26.9% |
| CSS | 806 | 32387 | 9.2% |
| MARKDOWN | 714 | 0 | 8.2% |
| XML | 373 | 0 | 4.3% |
| JSON | 326 | 15693 | 3.7% |
| PHP | 256 | 13134 | 2.9% |
| PLAINTEXT | 157 | 2 | 1.8% |
| JAVA | 29 | 3226 | 0.3% |
| SWIFT | 20 | 2790 | 0.2% |
| SHELL | 10 | 500 | 0.1% |
| KOTLIN | 9 | 782 | 0.1% |
| HTML | 8 | 93 | 0.1% |
| OBJECTIVE-C | 6 | 134 | 0.1% |
| GROOVY | 4 | 70 | 0.0% |
| YAML | 3 | 40 | 0.0% |
| BATCH | 3 | 214 | 0.0% |
| RUBY | 2 | 67 | 0.0% |
| PYTHON | 1 | 8 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.16`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4982 | 56.9% |
| file_cluster_13 | 2279 | 26.0% |
| file_cluster_2 | 241 | 2.8% |
| file_cluster_16 | 141 | 1.6% |
| file_cluster_4 | 101 | 1.2% |
| file_cluster_17 | 72 | 0.8% |
| file_cluster_0 | 46 | 0.5% |
| file_cluster_7 | 9 | 0.1% |
| file_cluster_12 | 3 | 0.0% |
| file_cluster_15 | 2 | 0.0% |
| file_cluster_9 | 2 | 0.0% |
| Unknown | 2 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 869 | 9.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3477*

**Composition by Extension & Reason:**
- `.html`: 814x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 792x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 24291 LOC), 1x Excluded (Monolithic Amalgamation: 63386 LOC exceeds safe regex boundaries)
- `.js`: 549x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Saturation: Line 8 exceeds 500 chars), 2x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.md`: 268x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 52 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3442 LOC)
- `.php`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 179 LOC), 1x Excluded (Saturation: Line 54 exceeds 500 chars)
- `.png`: 176x Excluded (Explicitly Denied Extension: '.png')
- `.snap`: 121x Unsupported Format (.snap), 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.txt`: 72x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 59269 LOC exceeds safe regex boundaries)
- `.ts`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `no_extension`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable), 4x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.mustache`: 23x Excluded (Unsupported Extension: '.mustache'), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 18x Excluded (Explicitly Denied Extension: '.jpg')
- `.template`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 8.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.6 | 1.4 | 0.0 |
| API Exposure | 0.0 | 20.0 | 3.8 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 57.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.5 | 5.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.4 | 17.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.3 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/url/src/test/index.js` (Hits: 243)
- `packages/block-library/src/navigation-link/shared/test/update-attributes.test.js` (Hits: 99)
- `packages/block-library/src/navigation-link/shared/test/use-link-preview.test.js` (Hits: 75)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **i18n.js** (`packages/eslint-plugin/configs/i18n.js`) — 1346 inbound connections
2. **components.tsx** (`storybook/stories/tokens/components.tsx`) — 1163 inbound connections
3. **blocks.ts** (`packages/e2e-test-utils-playwright/src/request-utils/blocks.ts`) — 466 inbound connections
4. **scss.js** (`packages/stylelint-config/scss.js`) — 204 inbound connections
5. **helpers.ts** (`packages/core-data/src/entity-types/helpers.ts`) — 140 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`packages/block-library/src/index.js`) — 133 outbound dependencies
2. **index.ts** (`packages/components/src/index.ts`) — 130 outbound dependencies
3. **index.js** (`packages/block-editor/src/components/index.js`) — 111 outbound dependencies
4. **index.js** (`packages/editor/src/components/index.js`) — 89 outbound dependencies
5. **index.native.js** (`packages/components/src/index.native.js`) — 79 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inflate` (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> Impact: **3110.5** | LOC: 1761
- `describe` (@ `packages/editor/src/store/test/selectors.js`) -> Impact: **799.8** | LOC: 2486
- `shouldInvalidate` (@ `packages/core-data/src/resolvers.js`) -> Impact: **790.2** | LOC: 804
- `withBlockReset` (@ `packages/block-editor/src/store/reducer.js`) -> Impact: **609.1** | LOC: 778
- `setOnLongClickListener` (@ `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecText.java`) -> Impact: **595.4** | LOC: 419
- `onKeyDown` (@ `packages/block-editor/src/components/list-view/block.js`) -> Impact: **551.7** | LOC: 453
- `render_block_core_search` (@ `packages/block-library/src/search/index.php`) -> Impact: **528.2** | LOC: 547
  * *Intent:* /** * Server-side rendering of the `core/search` block.
- `describe` (@ `packages/dataviews/src/hooks/test/use-form-validity.ts`) -> Impact: **479.9** | LOC: 1976
  * *Intent:* /** * Internal dependencies
- `describe` (@ `packages/block-editor/src/store/test/selectors.js`) -> Impact: **433.6** | LOC: 2333
- `__unstableGetSelectedBlocksWithPartialSe` (@ `packages/block-editor/src/store/selectors.js`) -> Impact: **430.8** | LOC: 902
  * *Intent:* /** * Given a block client ID, returns the list of all its parents from top to bottom. * * @param {Object} state Editor state. * @param {string} clien...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `shouldDeleteEnter` (@ `packages/react-native-aztec/android/src/main/kotlin/org/wordpress/mobile/ReactNativeAztec/EnterPressedWatcher.kt`) -> **O(2^N) [Recursive]**
- `setFontSize` (@ `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecManager.java`) -> **O(2^N) [Recursive]**
- `onCreate` (@ `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergEmbedWebViewActivity.java`) -> **O(2^N) [Recursive]**
- `onCreate` (@ `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergWebViewActivity.java`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/core-data/src/locks/test/selectors.js`) -> **O(2^N) [Recursive]**
- `receiveCommand` (@ `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecManager.java`) -> **O(2^N) [Recursive]**
- `inflate` (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> **O(2^N) [Recursive]**
- `setEditingElement` (@ `packages/components/src/palette-edit/index.tsx`) -> **O(2^N) [Recursive]**
- `render` (@ `storybook/stories/design-system/theme-example-application.story.tsx`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * A mock application page demonstrating how `ThemeProvider` affects multiple
- `onCreate` (@ `packages/react-native-editor/android/app/src/main/java/com/gutenberg/MainActivity.kt`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/block-library/src/navigation-link/shared/test/update-attributes.test.js`) -> DB Complexity: **297**
  * *Intent:* /** * Internal dependencies */
- `describe` (@ `packages/api-fetch/src/test/index.js`) -> DB Complexity: **158**
- `describe` (@ `packages/block-library/src/page-list/test/convert-to-navigation-links.js`) -> DB Complexity: **129**
- `describe` (@ `packages/editor/src/components/post-publish-panel/test/media-util.js`) -> DB Complexity: **120**
  * *Intent:* /** * Internal dependencies */
- `render_block_core_search` (@ `packages/block-library/src/search/index.php`) -> DB Complexity: **108**
  * *Intent:* /** * Server-side rendering of the `core/search` block.
- `describe` (@ `packages/block-library/src/utils/test/waveform-utils.js`) -> DB Complexity: **97**
- `describe` (@ `packages/block-library/src/navigation-link/shared/test/use-link-preview.test.js`) -> DB Complexity: **93**
- `inflate` (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> DB Complexity: **93**
- `describe` (@ `packages/url/src/test/index.js`) -> DB Complexity: **83**
- `describe` (@ `packages/components/src/navigator/test/router.ts`) -> DB Complexity: **81**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/global-styles-ui/src/font-library/lib` | 4 | 7882.18 | 60.63% | 55.32% |
| `__monolith__` | 16 | 5135.88 | 3.85% | 6.25% |
| `packages/vips` | 5 | 5021.44 | 1.0% | 0.0% |
| `packages/icons/src/library` | 331 | 3482.12 | 5.0% | 0.0% |
| `packages/block-editor/src/hooks` | 66 | 2467.11 | 6.97% | 13.07% |
| `packages/block-editor/src/store` | 13 | 2426.3 | 9.44% | 11.36% |
| `packages/block-editor/src/components/global-styles` | 17 | 2183.98 | 13.97% | 16.23% |
| `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec` | 16 | 1995.0 | 17.53% | 79.37% |
| `packages/block-editor/src/store/test` | 9 | 1933.62 | 7.18% | 0.0% |
| `packages/react-native-bridge/ios` | 7 | 1832.9 | 28.99% | 70.64% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/babel-preset-default/polyfill-exclusions.js` -> **100.0%** Exposure
- `packages/block-directory/src/store/resolvers.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-popover/inbetween.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/inserter/tips.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/inserter/utils.native.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/a11y/src/shared/clear.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/filter-message.js` -> **100.0%** Exposure
- `packages/babel-preset-default/polyfill-exclusions.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/audio-player/audio-url-parser.native.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-list/block-crash-boundary.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **0** Orphaned Functions | **170** Duplicates
- `packages/hooks/src/test/index.test.js` -> **1** Orphaned Functions | **61** Duplicates
- `packages/block-library/src/cover/deprecated.js` -> **0** Orphaned Functions | **42** Duplicates
- `packages/react-native-editor/ios/GutenbergDemo/GutenbergViewController.swift` -> **39** Orphaned Functions | **2** Duplicates
- `packages/rich-text/src/test/helpers/index.js` -> **0** Orphaned Functions | **40** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/global-styles-ui/src/font-library/lib/inflate.js`** -> AI Confidence: **99.48%**
2. **`packages/scripts/config/webpack.config.js`** -> AI Confidence: **99.48%**
3. **`packages/block-library/src/term-template/index.php`** -> AI Confidence: **99.48%**
4. **`packages/react-native-aztec/android/src/main/kotlin/org/wordpress/mobile/ReactNativeAztec/EnterPressedWatcher.kt`** -> AI Confidence: **99.48%**
5. **`packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/Media.kt`** -> AI Confidence: **99.48%**
6. **`packages/react-native-editor/android/app/src/main/java/com/gutenberg/MainActivity.kt`** -> AI Confidence: **99.48%**
7. **`packages/react-native-editor/android/app/src/main/java/com/gutenberg/MainApplication.kt`** -> AI Confidence: **99.48%**
8. **`packages/block-editor/src/components/block-list/block.js`** -> AI Confidence: **99.39%**
9. **`packages/block-editor/src/components/global-styles/dimensions-panel.js`** -> AI Confidence: **99.39%**
10. **`packages/block-library/src/button/edit.native.js`** -> AI Confidence: **99.39%**
11. **`packages/components/src/mobile/image/index.native.js`** -> AI Confidence: **99.39%**
12. **`packages/scripts/utils/config.js`** -> AI Confidence: **99.39%**
13. **`packages/components/src/button/index.tsx`** -> AI Confidence: **99.39%**
14. **`packages/block-library/src/cover/deprecated.js`** -> AI Confidence: **99.34%**
15. **`packages/edit-site/src/components/editor/use-resolve-edited-entity.js`** -> AI Confidence: **99.34%**
16. **`packages/scripts/scripts/test-playwright.js`** -> AI Confidence: **99.34%**
17. **`bin/packages/validate-typescript-version.js`** -> AI Confidence: **99.32%**
18. **`bin/plugin/commands/common.js`** -> AI Confidence: **99.32%**
19. **`packages/block-library/src/cover/save.js`** -> AI Confidence: **99.32%**
20. **`packages/block-library/src/embed/variations.js`** -> AI Confidence: **99.32%**
21. **`packages/scripts/scripts/build.js`** -> AI Confidence: **99.32%**
22. **`packages/scripts/scripts/lint-js.js`** -> AI Confidence: **99.32%**
23. **`packages/scripts/scripts/lint-md-docs.js`** -> AI Confidence: **99.32%**
24. **`packages/scripts/scripts/lint-pkg-json.js`** -> AI Confidence: **99.32%**
25. **`packages/scripts/scripts/lint-style.js`** -> AI Confidence: **99.32%**
26. **`packages/scripts/scripts/start.js`** -> AI Confidence: **99.32%**
27. **`packages/global-styles-engine/src/settings/get-palette.ts`** -> AI Confidence: **99.32%**
28. **`packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/GutenbergProps.kt`** -> AI Confidence: **99.32%**
29. **`bin/plugin/commands/performance.js`** -> AI Confidence: **99.31%**
30. **`packages/block-editor/src/components/background-image-control/index.js`** -> AI Confidence: **99.31%**
31. **`packages/block-editor/src/components/block-card/index.js`** -> AI Confidence: **99.31%**
32. **`packages/block-editor/src/components/block-draggable/dropping-insertion-point.native.js`** -> AI Confidence: **99.31%**
33. **`packages/block-editor/src/components/block-draggable/index.js`** -> AI Confidence: **99.31%**
34. **`packages/block-editor/src/components/block-edit/edit.js`** -> AI Confidence: **99.31%**
35. **`packages/block-editor/src/components/block-list/block-list-item.native.js`** -> AI Confidence: **99.31%**
36. **`packages/block-editor/src/components/block-list/index.native.js`** -> AI Confidence: **99.31%**
37. **`packages/block-editor/src/components/block-list/use-block-props/index.js`** -> AI Confidence: **99.31%**
38. **`packages/block-editor/src/components/block-list/use-block-props/use-selected-block-event-handlers.js`** -> AI Confidence: **99.31%**
39. **`packages/block-editor/src/components/block-list/use-in-between-inserter.js`** -> AI Confidence: **99.31%**
40. **`packages/block-editor/src/components/block-list/zoom-out-separator.js`** -> AI Confidence: **99.31%**
41. **`packages/block-editor/src/components/block-lock/modal.js`** -> AI Confidence: **99.31%**
42. **`packages/block-editor/src/components/block-mover/index.js`** -> AI Confidence: **99.31%**
43. **`packages/block-editor/src/components/block-quick-navigation/index.js`** -> AI Confidence: **99.31%**
44. **`packages/block-editor/src/components/block-rename/modal.js`** -> AI Confidence: **99.31%**
45. **`packages/block-editor/src/components/block-settings-menu-controls/index.js`** -> AI Confidence: **99.31%**
46. **`packages/block-editor/src/components/block-settings-menu/block-settings-dropdown.js`** -> AI Confidence: **99.31%**
47. **`packages/block-editor/src/components/block-switcher/index.js`** -> AI Confidence: **99.31%**
48. **`packages/block-editor/src/components/block-toolbar/block-toolbar-icon.js`** -> AI Confidence: **99.31%**
49. **`packages/block-editor/src/components/block-toolbar/block-toolbar-menu.native.js`** -> AI Confidence: **99.31%**
50. **`packages/block-editor/src/components/block-toolbar/index.js`** -> AI Confidence: **99.31%**
51. **`packages/block-editor/src/components/block-tools/index.js`** -> AI Confidence: **99.31%**
52. **`packages/block-editor/src/components/block-visibility/modal.js`** -> AI Confidence: **99.31%**
53. **`packages/block-editor/src/components/border-radius-control/index.js`** -> AI Confidence: **99.31%**
54. **`packages/block-editor/src/components/child-layout-control/index.js`** -> AI Confidence: **99.31%**
55. **`packages/block-editor/src/components/contrast-checker/index.native.js`** -> AI Confidence: **99.31%**
56. **`packages/block-editor/src/components/default-block-appender/index.native.js`** -> AI Confidence: **99.31%**
57. **`packages/block-editor/src/components/global-styles/background-panel.js`** -> AI Confidence: **99.31%**
58. **`packages/block-editor/src/components/global-styles/border-panel.js`** -> AI Confidence: **99.31%**
59. **`packages/block-editor/src/components/global-styles/color-panel.js`** -> AI Confidence: **99.31%**
60. **`packages/block-editor/src/components/global-styles/filters-panel.js`** -> AI Confidence: **99.31%**
61. **`packages/block-editor/src/components/global-styles/index.js`** -> AI Confidence: **99.31%**
62. **`packages/block-editor/src/components/global-styles/typography-panel.js`** -> AI Confidence: **99.31%**
63. **`packages/block-editor/src/components/global-styles/use-global-styles-context.native.js`** -> AI Confidence: **99.31%**
64. **`packages/block-editor/src/components/grid/grid-item-movers.js`** -> AI Confidence: **99.31%**
65. **`packages/block-editor/src/components/grid/grid-visualizer.js`** -> AI Confidence: **99.31%**
66. **`packages/block-editor/src/components/image-link-destinations/index.native.js`** -> AI Confidence: **99.31%**
67. **`packages/block-editor/src/components/inner-blocks/use-nested-settings-update.js`** -> AI Confidence: **99.31%**
68. **`packages/block-editor/src/components/inserter-draggable-blocks/index.js`** -> AI Confidence: **99.31%**
69. **`packages/block-editor/src/components/inserter/hooks/use-insertion-point.js`** -> AI Confidence: **99.31%**
70. **`packages/block-editor/src/components/inserter/index.js`** -> AI Confidence: **99.31%**
71. **`packages/block-editor/src/components/inspector-controls/fill.js`** -> AI Confidence: **99.31%**
72. **`packages/block-editor/src/components/link-control/link-preview.js`** -> AI Confidence: **99.31%**
73. **`packages/block-editor/src/components/list-view/block.js`** -> AI Confidence: **99.31%**
74. **`packages/block-editor/src/components/list-view/branch.js`** -> AI Confidence: **99.31%**
75. **`packages/block-editor/src/components/list-view/drop-indicator.js`** -> AI Confidence: **99.31%**
76. **`packages/block-editor/src/components/list-view/use-block-selection.js`** -> AI Confidence: **99.31%**
77. **`packages/block-editor/src/components/media-placeholder/index.native.js`** -> AI Confidence: **99.31%**
78. **`packages/block-editor/src/components/media-upload-progress/index.native.js`** -> AI Confidence: **99.31%**
79. **`packages/block-editor/src/components/media-upload/index.native.js`** -> AI Confidence: **99.31%**
80. **`packages/block-editor/src/components/preset-input-control/index.js`** -> AI Confidence: **99.31%**
81. **`packages/block-editor/src/components/provider/index.js`** -> AI Confidence: **99.31%**
82. **`packages/block-editor/src/components/rich-text/index.native.js`** -> AI Confidence: **99.31%**
83. **`packages/block-editor/src/components/rich-text/native/index.native.js`** -> AI Confidence: **99.31%**
84. **`packages/block-editor/src/components/spacing-sizes-control/index.js`** -> AI Confidence: **99.31%**
85. **`packages/block-editor/src/components/unsupported-block-details/index.native.js`** -> AI Confidence: **99.31%**
86. **`packages/block-editor/src/components/url-input/index.js`** -> AI Confidence: **99.31%**
87. **`packages/block-editor/src/components/use-block-drop-zone/index.js`** -> AI Confidence: **99.31%**
88. **`packages/block-editor/src/components/use-block-drop-zone/index.native.js`** -> AI Confidence: **99.31%**
89. **`packages/block-editor/src/components/writing-flow/use-clipboard-handler.js`** -> AI Confidence: **99.31%**
90. **`packages/block-editor/src/components/writing-flow/use-tab-nav.js`** -> AI Confidence: **99.31%**
91. **`packages/block-editor/src/hooks/anchor.js`** -> AI Confidence: **99.31%**
92. **`packages/block-editor/src/hooks/background.js`** -> AI Confidence: **99.31%**
93. **`packages/block-editor/src/hooks/block-fields/link/index.js`** -> AI Confidence: **99.31%**
94. **`packages/block-editor/src/hooks/block-fields/media/index.js`** -> AI Confidence: **99.31%**
95. **`packages/block-editor/src/hooks/block-fields/rich-text/index.js`** -> AI Confidence: **99.31%**
96. **`packages/block-editor/src/hooks/block-style-variation.js`** -> AI Confidence: **99.31%**
97. **`packages/block-editor/src/hooks/custom-class-name.js`** -> AI Confidence: **99.31%**
98. **`packages/block-editor/src/hooks/duotone.js`** -> AI Confidence: **99.31%**
99. **`packages/block-editor/src/hooks/grid-visualizer.js`** -> AI Confidence: **99.31%**
100. **`packages/block-editor/src/hooks/layout.js`** -> AI Confidence: **99.31%**
101. **`packages/block-editor/src/hooks/position.js`** -> AI Confidence: **99.31%**
102. **`packages/block-editor/src/layouts/constrained.js`** -> AI Confidence: **99.31%**
103. **`packages/block-editor/src/layouts/flex.js`** -> AI Confidence: **99.31%**
104. **`packages/block-editor/src/layouts/grid.js`** -> AI Confidence: **99.31%**
105. **`packages/block-editor/src/store/reducer.js`** -> AI Confidence: **99.31%**
106. **`packages/block-library/src/breadcrumbs/edit.js`** -> AI Confidence: **99.31%**
107. **`packages/block-library/src/button/edit.js`** -> AI Confidence: **99.31%**
108. **`packages/block-library/src/categories/edit.js`** -> AI Confidence: **99.31%**
109. **`packages/block-library/src/column/edit.native.js`** -> AI Confidence: **99.31%**
110. **`packages/block-library/src/comments-title/edit.js`** -> AI Confidence: **99.31%**
111. **`packages/block-library/src/cover/controls.native.js`** -> AI Confidence: **99.31%**
112. **`packages/block-library/src/cover/edit.native.js`** -> AI Confidence: **99.31%**
113. **`packages/block-library/src/cover/edit/inspector-controls.js`** -> AI Confidence: **99.31%**
114. **`packages/block-library/src/file/edit.native.js`** -> AI Confidence: **99.31%**
115. **`packages/block-library/src/footnotes/format.js`** -> AI Confidence: **99.31%**
116. **`packages/block-library/src/gallery/edit.js`** -> AI Confidence: **99.31%**
117. **`packages/block-library/src/group/edit.js`** -> AI Confidence: **99.31%**
118. **`packages/block-library/src/group/edit.native.js`** -> AI Confidence: **99.31%**
119. **`packages/block-library/src/heading/edit.native.js`** -> AI Confidence: **99.31%**
120. **`packages/block-library/src/image/edit.js`** -> AI Confidence: **99.31%**
121. **`packages/block-library/src/image/edit.native.js`** -> AI Confidence: **99.31%**
122. **`packages/block-library/src/latest-posts/edit.js`** -> AI Confidence: **99.31%**
123. **`packages/block-library/src/media-text/edit.js`** -> AI Confidence: **99.31%**
124. **`packages/block-library/src/media-text/edit.native.js`** -> AI Confidence: **99.31%**
125. **`packages/block-library/src/missing/edit.js`** -> AI Confidence: **99.31%**
126. **`packages/block-library/src/navigation-link/edit.js`** -> AI Confidence: **99.31%**
127. **`packages/block-library/src/navigation/edit/index.js`** -> AI Confidence: **99.31%**
128. **`packages/block-library/src/navigation/edit/navigation-menu-selector.js`** -> AI Confidence: **99.31%**
129. **`packages/block-library/src/page-list/edit.js`** -> AI Confidence: **99.31%**
130. **`packages/block-library/src/paragraph/edit.js`** -> AI Confidence: **99.31%**
131. **`packages/block-library/src/pattern/edit.js`** -> AI Confidence: **99.31%**
132. **`packages/block-library/src/playlist-track/edit.js`** -> AI Confidence: **99.31%**
133. **`packages/block-library/src/post-author/edit.js`** -> AI Confidence: **99.31%**
134. **`packages/block-library/src/post-content/edit.js`** -> AI Confidence: **99.31%**
135. **`packages/block-library/src/post-excerpt/edit.js`** -> AI Confidence: **99.31%**
136. **`packages/block-library/src/post-featured-image/edit.js`** -> AI Confidence: **99.31%**
137. **`packages/block-library/src/post-template/edit.js`** -> AI Confidence: **99.31%**
138. **`packages/block-library/src/post-terms/edit.js`** -> AI Confidence: **99.31%**
139. **`packages/block-library/src/query-title/edit.js`** -> AI Confidence: **99.31%**
140. **`packages/block-library/src/query/edit/inspector-controls/index.js`** -> AI Confidence: **99.31%**
141. **`packages/block-library/src/query/edit/inspector-controls/taxonomy-controls.js`** -> AI Confidence: **99.31%**
142. **`packages/block-library/src/query/edit/query-placeholder.js`** -> AI Confidence: **99.31%**
143. **`packages/block-library/src/search/edit.native.js`** -> AI Confidence: **99.31%**
144. **`packages/block-library/src/spacer/edit.js`** -> AI Confidence: **99.31%**
145. **`packages/block-library/src/template-part/edit/index.js`** -> AI Confidence: **99.31%**
146. **`packages/block-library/src/term-template/edit.js`** -> AI Confidence: **99.31%**
147. **`packages/block-library/src/utils/caption.js`** -> AI Confidence: **99.31%**
148. **`packages/components/src/autocomplete/autocompleter-ui.native.js`** -> AI Confidence: **99.31%**
149. **`packages/components/src/button/index.native.js`** -> AI Confidence: **99.31%**
150. **`packages/components/src/color-palette/index.native.js`** -> AI Confidence: **99.31%**
151. **`packages/components/src/mobile/bottom-sheet/cell.native.js`** -> AI Confidence: **99.31%**
152. **`packages/components/src/mobile/bottom-sheet/range-cell.native.js`** -> AI Confidence: **99.31%**
153. **`packages/components/src/mobile/bottom-sheet/range-text-input.native.js`** -> AI Confidence: **99.31%**
154. **`packages/components/src/mobile/bottom-sheet/stepper-cell/index.native.js`** -> AI Confidence: **99.31%**
155. **`packages/components/src/mobile/color-settings/palette.screen.native.js`** -> AI Confidence: **99.31%**
156. **`packages/components/src/mobile/gradient/index.native.js`** -> AI Confidence: **99.31%**
157. **`packages/components/src/unit-control/index.native.js`** -> AI Confidence: **99.31%**
158. **`packages/compose/src/index.js`** -> AI Confidence: **99.31%**
159. **`packages/compose/src/index.native.js`** -> AI Confidence: **99.31%**
160. **`packages/core-commands/src/site-editor-navigation-commands.js`** -> AI Confidence: **99.31%**
161. **`packages/core-data/src/utils/index.js`** -> AI Confidence: **99.31%**
162. **`packages/dom/src/dom/index.js`** -> AI Confidence: **99.31%**
163. **`packages/dom/src/dom/is-edge.js`** -> AI Confidence: **99.31%**
164. **`packages/edit-post/src/components/back-button/fullscreen-mode-close.js`** -> AI Confidence: **99.31%**
165. **`packages/edit-post/src/components/layout/index.js`** -> AI Confidence: **99.31%**
166. **`packages/edit-site/src/components/add-new-post/index.js`** -> AI Confidence: **99.31%**
167. **`packages/edit-site/src/components/add-new-template-legacy/add-custom-template-modal-content.js`** -> AI Confidence: **99.31%**
168. **`packages/edit-site/src/components/add-new-template/add-custom-template-modal-content.js`** -> AI Confidence: **99.31%**
169. **`packages/edit-site/src/components/editor/index.js`** -> AI Confidence: **99.31%**
170. **`packages/edit-site/src/components/layout/index.js`** -> AI Confidence: **99.31%**
171. **`packages/edit-site/src/components/page-templates/index.js`** -> AI Confidence: **99.31%**
172. **`packages/edit-site/src/components/post-list/index.js`** -> AI Confidence: **99.31%**
173. **`packages/edit-site/src/components/post-list/quick-edit-modal.js`** -> AI Confidence: **99.31%**
174. **`packages/edit-site/src/components/save-button/index.js`** -> AI Confidence: **99.31%**
175. **`packages/edit-site/src/components/sidebar-navigation-item/index.js`** -> AI Confidence: **99.31%**
176. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menu/use-navigation-menu-handlers.js`** -> AI Confidence: **99.31%**
177. **`packages/edit-site/src/components/site-hub/index.js`** -> AI Confidence: **99.31%**
178. **`packages/editor/src/components/collab-sidebar/comment-author-info.js`** -> AI Confidence: **99.31%**
179. **`packages/editor/src/components/collab-sidebar/comment-form.js`** -> AI Confidence: **99.31%**
180. **`packages/editor/src/components/collab-sidebar/comments.js`** -> AI Confidence: **99.31%**
181. **`packages/editor/src/components/document-bar/index.js`** -> AI Confidence: **99.31%**
182. **`packages/editor/src/components/editor/index.js`** -> AI Confidence: **99.31%**
183. **`packages/editor/src/components/entities-saved-states/index.js`** -> AI Confidence: **99.31%**
184. **`packages/editor/src/components/header/index.js`** -> AI Confidence: **99.31%**
185. **`packages/editor/src/components/index.js`** -> AI Confidence: **99.31%**
186. **`packages/editor/src/components/index.native.js`** -> AI Confidence: **99.31%**
187. **`packages/editor/src/components/offline-status/index.native.js`** -> AI Confidence: **99.31%**
188. **`packages/editor/src/components/post-card-panel/index.js`** -> AI Confidence: **99.31%**
189. **`packages/editor/src/components/post-featured-image/index.js`** -> AI Confidence: **99.31%**
190. **`packages/editor/src/components/post-locked-modal/index.js`** -> AI Confidence: **99.31%**
191. **`packages/editor/src/components/post-publish-panel/index.js`** -> AI Confidence: **99.31%**
192. **`packages/editor/src/components/post-publish-panel/maybe-category-panel.js`** -> AI Confidence: **99.31%**
193. **`packages/editor/src/components/post-publish-panel/maybe-tags-panel.js`** -> AI Confidence: **99.31%**
194. **`packages/editor/src/components/post-revisions-preview/block-diff.js`** -> AI Confidence: **99.31%**
195. **`packages/editor/src/components/post-saved-state/index.js`** -> AI Confidence: **99.31%**
196. **`packages/editor/src/components/post-taxonomies/flat-term-selector.js`** -> AI Confidence: **99.31%**
197. **`packages/editor/src/components/post-template/classic-theme.js`** -> AI Confidence: **99.31%**
198. **`packages/editor/src/components/post-url/index.js`** -> AI Confidence: **99.31%**
199. **`packages/editor/src/components/provider/use-block-editor-settings.js`** -> AI Confidence: **99.31%**
200. **`packages/editor/src/components/provider/use-revision-blocks.js`** -> AI Confidence: **99.31%**
201. **`packages/editor/src/components/visual-editor/index.js`** -> AI Confidence: **99.31%**
202. **`packages/editor/src/hooks/pattern-overrides.js`** -> AI Confidence: **99.31%**
203. **`packages/editor/src/store/private-actions.js`** -> AI Confidence: **99.31%**
204. **`packages/format-library/src/link/index.js`** -> AI Confidence: **99.31%**
205. **`packages/format-library/src/link/modal-screens/link-settings-screen.native.js`** -> AI Confidence: **99.31%**
206. **`packages/format-library/src/text-color/index.native.js`** -> AI Confidence: **99.31%**
207. **`packages/global-styles-ui/src/font-library/lib/unbrotli.js`** -> AI Confidence: **99.31%**
208. **`packages/interface/src/components/complementary-area/index.js`** -> AI Confidence: **99.31%**
209. **`packages/patterns/src/components/pattern-convert-button.js`** -> AI Confidence: **99.31%**
210. **`packages/patterns/src/components/rename-pattern-category-modal.js`** -> AI Confidence: **99.31%**
211. **`packages/patterns/src/components/rename-pattern-modal.js`** -> AI Confidence: **99.31%**
212. **`packages/rich-text/src/create.js`** -> AI Confidence: **99.31%**
213. **`packages/scripts/config/jest-environment-puppeteer/config.js`** -> AI Confidence: **99.31%**
214. **`packages/scripts/scripts/format.js`** -> AI Confidence: **99.31%**
215. **`packages/widgets/src/blocks/legacy-widget/edit/index.js`** -> AI Confidence: **99.31%**
216. **`packages/workflow/src/components/workflow-menu.js`** -> AI Confidence: **99.31%**
217. **`platform-docs/src/components/HomepageBlocks/index.js`** -> AI Confidence: **99.31%**
218. **`platform-docs/src/components/HomepageFeatures/index.js`** -> AI Confidence: **99.31%**
219. **`storybook/package-styles/config.js`** -> AI Confidence: **99.31%**
220. **`packages/block-library/src/archives/index.php`** -> AI Confidence: **99.31%**
221. **`packages/block-library/src/latest-comments/index.php`** -> AI Confidence: **99.31%**
222. **`packages/style-engine/src/style-engine.php`** -> AI Confidence: **99.31%**
223. **`packages/boot/src/components/root/index.tsx`** -> AI Confidence: **99.31%**
224. **`packages/components/src/autocomplete/index.tsx`** -> AI Confidence: **99.31%**
225. **`packages/components/src/border-control/border-control/hook.ts`** -> AI Confidence: **99.31%**
226. **`packages/components/src/box-control/index.tsx`** -> AI Confidence: **99.31%**
227. **`packages/components/src/box-control/input-control.tsx`** -> AI Confidence: **99.31%**
228. **`packages/components/src/calendar/date-range-calendar/index.tsx`** -> AI Confidence: **99.31%**
229. **`packages/components/src/custom-gradient-picker/gradient-bar/index.tsx`** -> AI Confidence: **99.31%**
230. **`packages/components/src/date-time/date/index.tsx`** -> AI Confidence: **99.31%**
231. **`packages/components/src/drop-zone/index.tsx`** -> AI Confidence: **99.31%**
232. **`packages/components/src/dropdown/index.tsx`** -> AI Confidence: **99.31%**
233. **`packages/components/src/form-token-field/index.tsx`** -> AI Confidence: **99.31%**
234. **`packages/components/src/input-control/input-base.tsx`** -> AI Confidence: **99.31%**
235. **`packages/components/src/modal/index.tsx`** -> AI Confidence: **99.31%**
236. **`packages/components/src/navigation/item/index.tsx`** -> AI Confidence: **99.31%**
237. **`packages/components/src/notice/index.tsx`** -> AI Confidence: **99.31%**
238. **`packages/components/src/number-control/index.tsx`** -> AI Confidence: **99.31%**
239. **`packages/components/src/palette-edit/index.tsx`** -> AI Confidence: **99.31%**
240. **`packages/components/src/query-controls/index.tsx`** -> AI Confidence: **99.31%**
241. **`packages/components/src/range-control/index.tsx`** -> AI Confidence: **99.31%**
242. **`packages/components/src/tabs/tablist.tsx`** -> AI Confidence: **99.31%**
243. **`packages/components/src/tools-panel/tools-panel-item/hook.ts`** -> AI Confidence: **99.31%**
244. **`packages/components/src/tooltip/index.tsx`** -> AI Confidence: **99.31%**
245. **`packages/components/src/tree-grid/index.tsx`** -> AI Confidence: **99.31%**
246. **`packages/components/src/truncate/hook.ts`** -> AI Confidence: **99.31%**
247. **`packages/components/src/unit-control/index.tsx`** -> AI Confidence: **99.31%**
248. **`packages/core-data/src/selectors.ts`** -> AI Confidence: **99.31%**
249. **`packages/core-data/src/utils/crdt-user-selections.ts`** -> AI Confidence: **99.31%**
250. **`packages/core-data/src/utils/crdt.ts`** -> AI Confidence: **99.31%**
251. **`packages/dataviews/src/components/dataform-controls/date.tsx`** -> AI Confidence: **99.31%**
252. **`packages/dataviews/src/components/dataform-controls/datetime.tsx`** -> AI Confidence: **99.31%**
253. **`packages/dataviews/src/components/dataform-layouts/panel/summary-button.tsx`** -> AI Confidence: **99.31%**
254. **`packages/dataviews/src/components/dataviews-filters/filter.tsx`** -> AI Confidence: **99.31%**
255. **`packages/dataviews/src/components/dataviews-footer/index.tsx`** -> AI Confidence: **99.31%**
256. **`packages/dataviews/src/components/dataviews-layouts/activity/index.tsx`** -> AI Confidence: **99.31%**
257. **`packages/dataviews/src/components/dataviews-layouts/grid/composite-grid.tsx`** -> AI Confidence: **99.31%**
258. **`packages/dataviews/src/components/dataviews-layouts/grid/index.tsx`** -> AI Confidence: **99.31%**
259. **`packages/dataviews/src/components/dataviews-layouts/list/index.tsx`** -> AI Confidence: **99.31%**
260. **`packages/dataviews/src/components/dataviews-layouts/picker-grid/index.tsx`** -> AI Confidence: **99.31%**
261. **`packages/dataviews/src/components/dataviews-layouts/picker-table/index.tsx`** -> AI Confidence: **99.31%**
262. **`packages/dataviews/src/components/dataviews-layouts/table/index.tsx`** -> AI Confidence: **99.31%**
263. **`packages/dataviews/src/dataform/stories/validation.tsx`** -> AI Confidence: **99.31%**
264. **`packages/dataviews/src/field-types/index.tsx`** -> AI Confidence: **99.31%**
265. **`packages/editor/src/components/collaborators-presence/avatar/component.tsx`** -> AI Confidence: **99.31%**
266. **`packages/editor/src/components/collaborators-presence/use-collaborator-notifications.ts`** -> AI Confidence: **99.31%**
267. **`packages/editor/src/components/sync-connection-error-modal/index.tsx`** -> AI Confidence: **99.31%**
268. **`packages/editor/src/dataviews/store/private-actions.ts`** -> AI Confidence: **99.31%**
269. **`packages/fields/src/actions/index.ts`** -> AI Confidence: **99.31%**
270. **`packages/fields/src/actions/permanently-delete-post.tsx`** -> AI Confidence: **99.31%**
271. **`packages/fields/src/actions/rename-post.tsx`** -> AI Confidence: **99.31%**
272. **`packages/fields/src/actions/restore-post.tsx`** -> AI Confidence: **99.31%**
273. **`packages/fields/src/actions/trash-post.tsx`** -> AI Confidence: **99.31%**
274. **`packages/fields/src/components/media-edit/index.tsx`** -> AI Confidence: **99.31%**
275. **`packages/fields/src/fields/author/author-view.tsx`** -> AI Confidence: **99.31%**
276. **`packages/fields/src/fields/index.ts`** -> AI Confidence: **99.31%**
277. **`packages/global-styles-engine/src/core/render.tsx`** -> AI Confidence: **99.31%**
278. **`packages/global-styles-ui/src/color-palette-panel.tsx`** -> AI Confidence: **99.31%**
279. **`packages/global-styles-ui/src/font-families.tsx`** -> AI Confidence: **99.31%**
280. **`packages/global-styles-ui/src/font-library/context.tsx`** -> AI Confidence: **99.31%**
281. **`packages/global-styles-ui/src/font-library/installed-fonts.tsx`** -> AI Confidence: **99.31%**
282. **`packages/global-styles-ui/src/font-library/utils/index.ts`** -> AI Confidence: **99.31%**
283. **`packages/global-styles-ui/src/font-sizes/font-size.tsx`** -> AI Confidence: **99.31%**
284. **`packages/global-styles-ui/src/font-sizes/font-sizes.tsx`** -> AI Confidence: **99.31%**
285. **`packages/global-styles-ui/src/screen-block.tsx`** -> AI Confidence: **99.31%**
286. **`packages/global-styles-ui/src/style-variations-container.tsx`** -> AI Confidence: **99.31%**
287. **`packages/interactivity/src/directives.tsx`** -> AI Confidence: **99.31%**
288. **`packages/media-utils/src/components/media-upload-modal/index.tsx`** -> AI Confidence: **99.31%**
289. **`packages/media-utils/src/utils/upload-media.ts`** -> AI Confidence: **99.31%**
290. **`packages/theme/bin/terrazzo-plugin-ds-token-fallbacks/index.ts`** -> AI Confidence: **99.31%**
291. **`packages/theme/src/color-ramps/lib/index.ts`** -> AI Confidence: **99.31%**
292. **`routes/connectors-home/default-connectors.tsx`** -> AI Confidence: **99.31%**
293. **`routes/pattern-list/use-patterns.ts`** -> AI Confidence: **99.31%**
294. **`bin/validate-package-lock.js`** -> AI Confidence: **99.29%**
295. **`packages/babel-preset-default/polyfill-exclusions.js`** -> AI Confidence: **99.29%**
296. **`packages/babel-preset-default/replace-polyfills.js`** -> AI Confidence: **99.29%**
297. **`packages/block-editor/src/utils/format-font-weight.js`** -> AI Confidence: **99.29%**
298. **`packages/block-library/src/accordion-heading/deprecated.js`** -> AI Confidence: **99.29%**
299. **`packages/block-library/src/gallery/shared.js`** -> AI Confidence: **99.29%**
300. **`packages/block-library/src/playlist/utils.js`** -> AI Confidence: **99.29%**
301. **`packages/block-library/src/post-date/variations.js`** -> AI Confidence: **99.29%**
302. **`packages/blocks/src/api/parser/convert-legacy-block.js`** -> AI Confidence: **99.29%**
303. **`packages/blocks/src/api/raw-handling/normalise-blocks.js`** -> AI Confidence: **99.29%**
304. **`packages/create-block-interactive-template/index.js`** -> AI Confidence: **99.29%**
305. **`packages/docgen/bin/cli.js`** -> AI Confidence: **99.29%**
306. **`packages/e2e-tests/plugins/interactive-blocks/get-server-context/view.js`** -> AI Confidence: **99.29%**
307. **`packages/e2e-tests/plugins/interactive-blocks/get-server-state/view.js`** -> AI Confidence: **99.29%**
308. **`packages/e2e-tests/plugins/interactive-blocks/tovdom/processing-instructions.js`** -> AI Confidence: **99.29%**
309. **`packages/eslint-plugin/rules/__tests__/wp-global-usage.js`** -> AI Confidence: **99.29%**
310. **`packages/eslint-plugin/rules/no-i18n-in-save.js`** -> AI Confidence: **99.29%**
311. **`packages/eslint-plugin/utils/constants.js`** -> AI Confidence: **99.29%**
312. **`packages/jest-preset-default/jest-preset.js`** -> AI Confidence: **99.29%**
313. **`packages/preferences-persistence/src/migrations/legacy-local-storage-data/move-feature-preferences.js`** -> AI Confidence: **99.29%**
314. **`packages/preferences-persistence/src/migrations/legacy-local-storage-data/move-individual-preference.js`** -> AI Confidence: **99.29%**
315. **`packages/react-native-bridge/common/gutenberg-web-single-block/insert-block.js`** -> AI Confidence: **99.29%**
316. **`packages/react-native-editor/jest_ui.config.js`** -> AI Confidence: **99.29%**
317. **`packages/scripts/config/babel-transform.js`** -> AI Confidence: **99.29%**
318. **`packages/scripts/config/jest-e2e.config.js`** -> AI Confidence: **99.29%**
319. **`packages/scripts/config/jest-unit.config.js`** -> AI Confidence: **99.29%**
320. **`packages/scripts/config/playwright.config.js`** -> AI Confidence: **99.29%**
321. **`packages/scripts/config/puppeteer.config.js`** -> AI Confidence: **99.29%**
322. **`packages/scripts/scripts/check-licenses.js`** -> AI Confidence: **99.29%**
323. **`packages/scripts/scripts/test-e2e.js`** -> AI Confidence: **99.29%**
324. **`packages/stylelint-config/scss.js`** -> AI Confidence: **99.29%**
325. **`react-scanner.config.js`** -> AI Confidence: **99.29%**
326. **`test/native/jest.config.js`** -> AI Confidence: **99.29%**
327. **`packages/react-native-editor/bin/test-e2e.sh`** -> AI Confidence: **99.29%**
328. **`packages/block-library/src/breadcrumbs/index.php`** -> AI Confidence: **99.29%**
329. **`packages/block-library/src/cover/index.php`** -> AI Confidence: **99.29%**
330. **`packages/block-library/src/icon/index.php`** -> AI Confidence: **99.29%**
331. **`packages/block-library/src/query-title/index.php`** -> AI Confidence: **99.29%**
332. **`packages/block-library/src/query-total/index.php`** -> AI Confidence: **99.29%**
333. **`packages/block-library/src/term-count/index.php`** -> AI Confidence: **99.29%**
334. **`packages/e2e-tests/mu-plugins/disable-login-autofocus.php`** -> AI Confidence: **99.29%**
335. **`packages/e2e-tests/mu-plugins/disable-remote-patterns.php`** -> AI Confidence: **99.29%**
336. **`packages/e2e-tests/plugins/disable-client-side-media-processing.php`** -> AI Confidence: **99.29%**
337. **`packages/e2e-tests/plugins/interactive-blocks/directive-bind/render.php`** -> AI Confidence: **99.29%**
338. **`packages/e2e-tests/plugins/interactive-blocks/directive-each/render.php`** -> AI Confidence: **99.29%**
339. **`packages/e2e-tests/plugins/interactive-blocks/directive-init/render.php`** -> AI Confidence: **99.29%**
340. **`packages/e2e-tests/plugins/interactive-blocks/directive-key/render.php`** -> AI Confidence: **99.29%**
341. **`packages/e2e-tests/plugins/interactive-blocks/directive-on-document/render.php`** -> AI Confidence: **99.29%**
342. **`packages/e2e-tests/plugins/interactive-blocks/directive-on-window/render.php`** -> AI Confidence: **99.29%**
343. **`packages/e2e-tests/plugins/interactive-blocks/directive-on/render.php`** -> AI Confidence: **99.29%**
344. **`packages/e2e-tests/plugins/interactive-blocks/directive-text/render.php`** -> AI Confidence: **99.29%**
345. **`packages/e2e-tests/plugins/interactive-blocks/directive-watch/render.php`** -> AI Confidence: **99.29%**
346. **`packages/e2e-tests/plugins/interactive-blocks/generator-scope/render.php`** -> AI Confidence: **99.29%**
347. **`packages/e2e-tests/plugins/interactive-blocks/get-server-context/render.php`** -> AI Confidence: **99.29%**
348. **`packages/e2e-tests/plugins/interactive-blocks/get-server-state/render.php`** -> AI Confidence: **99.29%**
349. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing-async/render.php`** -> AI Confidence: **99.29%**
350. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing-slow/render.php`** -> AI Confidence: **99.29%**
351. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing/render.php`** -> AI Confidence: **99.29%**
352. **`packages/e2e-tests/plugins/interactive-blocks/negation-operator/render.php`** -> AI Confidence: **99.29%**
353. **`packages/e2e-tests/plugins/interactive-blocks/router-race-condition/render.php`** -> AI Confidence: **99.29%**
354. **`packages/e2e-tests/plugins/interactive-blocks/router-regions/render.php`** -> AI Confidence: **99.29%**
355. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-alpha/render.php`** -> AI Confidence: **99.29%**
356. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-bravo/render.php`** -> AI Confidence: **99.29%**
357. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-charlie/render.php`** -> AI Confidence: **99.29%**
358. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-wrapper/render.php`** -> AI Confidence: **99.29%**
359. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-blue/render.php`** -> AI Confidence: **99.29%**
360. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-green/render.php`** -> AI Confidence: **99.29%**
361. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-red/render.php`** -> AI Confidence: **99.29%**
362. **`packages/e2e-tests/plugins/interactive-blocks/store-tag/render.php`** -> AI Confidence: **99.29%**
363. **`packages/e2e-tests/plugins/interactive-blocks/store/render.php`** -> AI Confidence: **99.29%**
364. **`packages/e2e-tests/plugins/interactive-blocks/tovdom/render.php`** -> AI Confidence: **99.29%**
365. **`packages/e2e-tests/plugins/interactive-blocks/with-scope/render.php`** -> AI Confidence: **99.29%**
366. **`packages/e2e-tests/plugins/query-block.php`** -> AI Confidence: **99.29%**
367. **`packages/icons/src/manifest.php`** -> AI Confidence: **99.29%**
368. **`packages/dataviews/src/components/dataform-controls/utils/get-custom-validity.ts`** -> AI Confidence: **99.29%**
369. **`packages/dataviews/src/field-types/utils/get-is-valid.ts`** -> AI Confidence: **99.29%**
370. **`packages/editor/src/components/collaborators-overlay/get-avatar-url.ts`** -> AI Confidence: **99.29%**
371. **`packages/interactivity-router/src/assets/dynamic-importmap/resolver.ts`** -> AI Confidence: **99.29%**
372. **`packages/report-flaky-tests/src/strip-ansi.ts`** -> AI Confidence: **99.29%**
373. **`packages/react-native-aztec/android/settings.gradle`** -> AI Confidence: **99.29%**
374. **`packages/react-native-bridge/android/settings.gradle`** -> AI Confidence: **99.29%**
375. **`packages/react-native-editor/android/settings.gradle`** -> AI Confidence: **99.29%**
376. **`packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/AztecReactTextChangedEvent.kt`** -> AI Confidence: **99.29%**
377. **`packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/GutenbergJsException.kt`** -> AI Confidence: **99.29%**
378. **`packages/react-native-bridge/ios/GutenbergBridgeDelegate.swift`** -> AI Confidence: **99.29%**
379. **`packages/react-native-bridge/ios/RNReactNativeGutenbergBridge.swift`** -> AI Confidence: **99.29%**
380. **`packages/react-native-editor/ios/Podfile`** -> AI Confidence: **99.29%**
381. **`bin/api-docs/gen-components-docs/index.mjs`** -> AI Confidence: **99.24%**
382. **`bin/plugin/commands/packages.js`** -> AI Confidence: **99.24%**
383. **`packages/block-directory/src/components/downloadable-block-list-item/index.js`** -> AI Confidence: **99.24%**
384. **`packages/block-editor/src/components/audio-player/index.native.js`** -> AI Confidence: **99.24%**
385. **`packages/block-editor/src/components/block-list/index.js`** -> AI Confidence: **99.24%**
386. **`packages/block-editor/src/components/block-mover/button.js`** -> AI Confidence: **99.24%**
387. **`packages/block-editor/src/components/block-switcher/block-transformations-menu.js`** -> AI Confidence: **99.24%**
388. **`packages/block-editor/src/components/block-tools/insertion-point.js`** -> AI Confidence: **99.24%**
389. **`packages/block-editor/src/components/block-tools/use-block-toolbar-popover-props.js`** -> AI Confidence: **99.24%**
390. **`packages/block-editor/src/components/block-variation-transforms/index.js`** -> AI Confidence: **99.24%**
391. **`packages/block-editor/src/components/floating-toolbar/index.native.js`** -> AI Confidence: **99.24%**
392. **`packages/block-editor/src/components/iframe/index.js`** -> AI Confidence: **99.24%**
393. **`packages/block-editor/src/components/image-editor/use-save-image.js`** -> AI Confidence: **99.24%**
394. **`packages/block-editor/src/components/index.js`** -> AI Confidence: **99.24%**
395. **`packages/block-editor/src/components/index.native.js`** -> AI Confidence: **99.24%**
396. **`packages/block-editor/src/components/inserter/menu.js`** -> AI Confidence: **99.24%**
397. **`packages/block-editor/src/components/inserter/menu.native.js`** -> AI Confidence: **99.24%**
398. **`packages/block-editor/src/components/inspector-controls-tabs/index.js`** -> AI Confidence: **99.24%**
399. **`packages/block-editor/src/components/inspector-controls/slot.js`** -> AI Confidence: **99.24%**
400. **`packages/block-editor/src/components/link-control/search-results.js`** -> AI Confidence: **99.24%**
401. **`packages/block-editor/src/components/list-view/block-select-button.js`** -> AI Confidence: **99.24%**
402. **`packages/block-editor/src/components/list-view/index.js`** -> AI Confidence: **99.24%**
403. **`packages/block-editor/src/components/rich-text/index.js`** -> AI Confidence: **99.24%**
404. **`packages/block-editor/src/hooks/block-fields/index.js`** -> AI Confidence: **99.24%**
405. **`packages/block-editor/src/hooks/custom-css.js`** -> AI Confidence: **99.24%**
406. **`packages/block-editor/src/hooks/fit-text.js`** -> AI Confidence: **99.24%**
407. **`packages/block-editor/src/hooks/style.js`** -> AI Confidence: **99.24%**
408. **`packages/block-editor/src/hooks/typography.js`** -> AI Confidence: **99.24%**
409. **`packages/block-editor/src/hooks/utils.js`** -> AI Confidence: **99.24%**
410. **`packages/block-editor/src/store/actions.js`** -> AI Confidence: **99.24%**
411. **`packages/block-library/src/block/edit-title.native.js`** -> AI Confidence: **99.24%**
412. **`packages/block-library/src/block/edit.js`** -> AI Confidence: **99.24%**
413. **`packages/block-library/src/comment-author-name/edit.js`** -> AI Confidence: **99.24%**
414. **`packages/block-library/src/cover/edit/block-controls.js`** -> AI Confidence: **99.24%**
415. **`packages/block-library/src/cover/edit/index.js`** -> AI Confidence: **99.24%**
416. **`packages/block-library/src/file/edit.js`** -> AI Confidence: **99.24%**
417. **`packages/block-library/src/html/modal.js`** -> AI Confidence: **99.24%**
418. **`packages/block-library/src/icon/edit.js`** -> AI Confidence: **99.24%**
419. **`packages/block-library/src/image/image.js`** -> AI Confidence: **99.24%**
420. **`packages/block-library/src/list-item/edit.native.js`** -> AI Confidence: **99.24%**
421. **`packages/block-library/src/media-text/media-container.js`** -> AI Confidence: **99.24%**
422. **`packages/block-library/src/navigation-link/link-ui/index.js`** -> AI Confidence: **99.24%**
423. **`packages/block-library/src/navigation-link/link-ui/page-creator.js`** -> AI Confidence: **99.24%**
424. **`packages/block-library/src/navigation-link/shared/controls.js`** -> AI Confidence: **99.24%**
425. **`packages/block-library/src/navigation-submenu/edit.js`** -> AI Confidence: **99.24%**
426. **`packages/block-library/src/navigation/edit/overlay-template-part-selector.js`** -> AI Confidence: **99.24%**
427. **`packages/block-library/src/navigation/edit/placeholder/index.js`** -> AI Confidence: **99.24%**
428. **`packages/block-library/src/paragraph/index.js`** -> AI Confidence: **99.24%**
429. **`packages/block-library/src/post-date/edit.js`** -> AI Confidence: **99.24%**
430. **`packages/block-library/src/social-link/edit.native.js`** -> AI Confidence: **99.24%**
431. **`packages/block-library/src/table/edit.js`** -> AI Confidence: **99.24%**
432. **`packages/block-library/src/video/edit.native.js`** -> AI Confidence: **99.24%**
433. **`packages/commands/src/components/command-menu.js`** -> AI Confidence: **99.24%**
434. **`packages/components/src/custom-gradient-picker/index.native.js`** -> AI Confidence: **99.24%**
435. **`packages/components/src/index.native.js`** -> AI Confidence: **99.24%**
436. **`packages/core-data/src/resolvers.js`** -> AI Confidence: **99.24%**
437. **`packages/edit-post/src/components/layout/index.native.js`** -> AI Confidence: **99.24%**
438. **`packages/edit-site/src/components/add-new-pattern/index.js`** -> AI Confidence: **99.24%**
439. **`packages/edit-site/src/components/add-new-template/utils.js`** -> AI Confidence: **99.24%**
440. **`packages/edit-site/src/components/page-patterns/fields.js`** -> AI Confidence: **99.24%**
441. **`packages/edit-site/src/components/page-patterns/index.js`** -> AI Confidence: **99.24%**
442. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menu/index.js`** -> AI Confidence: **99.24%**
443. **`packages/edit-site/src/components/sidebar-navigation-screen/index.js`** -> AI Confidence: **99.24%**
444. **`packages/edit-site/src/components/site-editor-routes/pages.js`** -> AI Confidence: **99.24%**
445. **`packages/edit-site/src/components/site-editor-routes/templates.js`** -> AI Confidence: **99.24%**
446. **`packages/edit-widgets/src/components/layout/interface.js`** -> AI Confidence: **99.24%**
447. **`packages/edit-widgets/src/components/sidebar/index.js`** -> AI Confidence: **99.24%**
448. **`packages/editor/src/components/collab-sidebar/index.js`** -> AI Confidence: **99.24%**
449. **`packages/editor/src/components/commands/index.js`** -> AI Confidence: **99.24%**
450. **`packages/editor/src/components/editor-interface/index.js`** -> AI Confidence: **99.24%**
451. **`packages/editor/src/components/global-styles-sidebar/index.js`** -> AI Confidence: **99.24%**
452. **`packages/editor/src/components/post-publish-panel/postpublish.js`** -> AI Confidence: **99.24%**
453. **`packages/editor/src/components/post-publish-panel/prepublish.js`** -> AI Confidence: **99.24%**
454. **`packages/editor/src/components/post-taxonomies/hierarchical-term-selector.js`** -> AI Confidence: **99.24%**
455. **`packages/editor/src/components/post-title/index.native.js`** -> AI Confidence: **99.24%**
456. **`packages/editor/src/components/provider/index.native.js`** -> AI Confidence: **99.24%**
457. **`packages/editor/src/components/sidebar/dataform-post-summary.js`** -> AI Confidence: **99.24%**
458. **`packages/editor/src/components/style-book/index.js`** -> AI Confidence: **99.24%**
459. **`packages/editor/src/components/template-actions-panel/classic-theme-content.js`** -> AI Confidence: **99.24%**
460. **`packages/patterns/src/components/patterns-manage-button.js`** -> AI Confidence: **99.24%**
461. **`packages/reusable-blocks/src/components/reusable-blocks-menu-items/reusable-block-convert-button.js`** -> AI Confidence: **99.24%**
462. **`packages/rich-text/src/hook/index.js`** -> AI Confidence: **99.24%**
463. **`packages/boot/src/components/root/single-page.tsx`** -> AI Confidence: **99.24%**
464. **`packages/boot/src/components/site-hub/index.tsx`** -> AI Confidence: **99.24%**
465. **`packages/components/src/calendar/test/date-calendar.tsx`** -> AI Confidence: **99.24%**
466. **`packages/components/src/combobox-control/index.tsx`** -> AI Confidence: **99.24%**
467. **`packages/components/src/custom-select-control-v2/styles.ts`** -> AI Confidence: **99.24%**
468. **`packages/components/src/duotone-picker/duotone-picker.tsx`** -> AI Confidence: **99.24%**
469. **`packages/components/src/index.ts`** -> AI Confidence: **99.24%**
470. **`packages/components/src/navigator/navigator/component.tsx`** -> AI Confidence: **99.24%**
471. **`packages/components/src/select-control/styles/select-control-styles.ts`** -> AI Confidence: **99.24%**
472. **`packages/components/src/tab-panel/index.tsx`** -> AI Confidence: **99.24%**
473. **`packages/components/src/text/hook.ts`** -> AI Confidence: **99.24%**
474. **`packages/core-data/src/utils/crdt-selection.ts`** -> AI Confidence: **99.24%**
475. **`packages/dataviews/src/components/dataform-layouts/card/index.tsx`** -> AI Confidence: **99.24%**
476. **`packages/dataviews/src/components/dataform-layouts/details/index.tsx`** -> AI Confidence: **99.24%**
477. **`packages/dataviews/src/components/dataviews-layouts/activity/activity-item.tsx`** -> AI Confidence: **99.24%**
478. **`packages/dataviews/src/components/dataviews-view-config/index.tsx`** -> AI Confidence: **99.24%**
479. **`packages/dataviews/src/components/dataviews-view-config/properties-section.tsx`** -> AI Confidence: **99.24%**
480. **`packages/dataviews/src/field-types/color.tsx`** -> AI Confidence: **99.24%**
481. **`packages/dataviews/src/field-types/number.tsx`** -> AI Confidence: **99.24%**
482. **`packages/editor/src/components/collaborators-overlay/overlay.tsx`** -> AI Confidence: **99.24%**
483. **`packages/editor/src/components/collaborators-overlay/use-render-cursors.ts`** -> AI Confidence: **99.24%**
484. **`packages/fields/src/actions/reset-post.tsx`** -> AI Confidence: **99.24%**
485. **`packages/fields/src/components/create-template-part-modal/index.tsx`** -> AI Confidence: **99.24%**
486. **`packages/global-styles-ui/src/font-library/font-collection.tsx`** -> AI Confidence: **99.24%**
487. **`packages/global-styles-ui/src/shadows-panel.tsx`** -> AI Confidence: **99.24%**
488. **`packages/global-styles-ui/src/variations/variation.tsx`** -> AI Confidence: **99.24%**
489. **`packages/lazy-editor/src/components/editor/index.tsx`** -> AI Confidence: **99.24%**
490. **`packages/lazy-editor/src/components/preview/index.tsx`** -> AI Confidence: **99.24%**
491. **`packages/media-fields/src/index.ts`** -> AI Confidence: **99.24%**
492. **`packages/theme/src/use-theme-provider-styles.ts`** -> AI Confidence: **99.24%**
493. **`packages/upload-media/src/store/actions.ts`** -> AI Confidence: **99.24%**
494. **`packages/upload-media/src/store/private-actions.ts`** -> AI Confidence: **99.24%**
495. **`packages/wordcount/src/index.ts`** -> AI Confidence: **99.24%**
496. **`routes/content-guidelines/components/block-guideline-modal.tsx`** -> AI Confidence: **99.24%**
497. **`routes/content-guidelines/components/revision-history.tsx`** -> AI Confidence: **99.24%**
498. **`routes/post-list/quick-edit-modal.tsx`** -> AI Confidence: **99.24%**
499. **`routes/post-list/stage.tsx`** -> AI Confidence: **99.24%**
500. **`routes/template-list/stage-activation.tsx`** -> AI Confidence: **99.24%**
501. **`routes/template-list/stage-legacy.tsx`** -> AI Confidence: **99.24%**
502. **`bin/plugin/lib/utils.js`** -> AI Confidence: **99.23%**
503. **`packages/block-editor/src/components/block-bindings/source-fields-list.js`** -> AI Confidence: **99.23%**
504. **`packages/block-editor/src/components/block-toolbar/change-design.js`** -> AI Confidence: **99.23%**
505. **`packages/block-editor/src/components/default-block-appender/index.js`** -> AI Confidence: **99.23%**
506. **`packages/block-editor/src/components/editor-styles/index.js`** -> AI Confidence: **99.23%**
507. **`packages/block-editor/src/components/global-styles/hooks.js`** -> AI Confidence: **99.23%**
508. **`packages/block-editor/src/components/inspector-controls-tabs/position-controls-panel.js`** -> AI Confidence: **99.23%**
509. **`packages/block-editor/src/components/link-control/search-input.js`** -> AI Confidence: **99.23%**
510. **`packages/block-editor/src/components/link-control/search-item.js`** -> AI Confidence: **99.23%**
511. **`packages/block-editor/src/components/list-view/use-list-view-drop-zone.js`** -> AI Confidence: **99.23%**
512. **`packages/block-editor/src/components/spacing-sizes-control/input-controls/spacing-input-control.js`** -> AI Confidence: **99.23%**
513. **`packages/block-editor/src/components/url-popover/index.js`** -> AI Confidence: **99.23%**
514. **`packages/block-editor/src/components/use-block-commands/index.js`** -> AI Confidence: **99.23%**
515. **`packages/block-editor/src/components/use-block-display-information/index.js`** -> AI Confidence: **99.23%**
516. **`packages/block-editor/src/components/use-paste-styles/index.js`** -> AI Confidence: **99.23%**
517. **`packages/block-editor/src/components/video-player/index.native.js`** -> AI Confidence: **99.23%**
518. **`packages/block-editor/src/hooks/font-size.js`** -> AI Confidence: **99.23%**
519. **`packages/block-editor/src/hooks/text-align.js`** -> AI Confidence: **99.23%**
520. **`packages/block-library/src/buttons/edit.native.js`** -> AI Confidence: **99.23%**
521. **`packages/block-library/src/comment-template/edit.js`** -> AI Confidence: **99.23%**
522. **`packages/block-library/src/embed/embed-placeholder.native.js`** -> AI Confidence: **99.23%**
523. **`packages/block-library/src/navigation/edit/overlay-panel.js`** -> AI Confidence: **99.23%**
524. **`packages/block-library/src/navigation/edit/unsaved-inner-blocks.js`** -> AI Confidence: **99.23%**
525. **`packages/block-library/src/page-list-item/edit.js`** -> AI Confidence: **99.23%**
526. **`packages/block-library/src/post-author-name/edit.js`** -> AI Confidence: **99.23%**
527. **`packages/block-library/src/post-comments-form/form.js`** -> AI Confidence: **99.23%**
528. **`packages/block-library/src/post-title/edit.js`** -> AI Confidence: **99.23%**
529. **`packages/block-library/src/site-title/edit.js`** -> AI Confidence: **99.23%**
530. **`packages/block-library/src/spacer/edit.native.js`** -> AI Confidence: **99.23%**
531. **`packages/block-library/src/tab/edit.js`** -> AI Confidence: **99.23%**
532. **`packages/block-library/src/template-part/edit/placeholder.js`** -> AI Confidence: **99.23%**
533. **`packages/blocks/src/api/parser/apply-block-deprecated-versions.js`** -> AI Confidence: **99.23%**
534. **`packages/blocks/src/store/process-block-type.js`** -> AI Confidence: **99.23%**
535. **`packages/components/src/font-size-picker/index.native.js`** -> AI Confidence: **99.23%**
536. **`packages/edit-site/src/components/more-menu/site-export.js`** -> AI Confidence: **99.23%**
537. **`packages/edit-site/src/components/page-patterns/use-patterns.js`** -> AI Confidence: **99.23%**
538. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menus/leaf-more-menu.js`** -> AI Confidence: **99.23%**
539. **`packages/editor/src/components/global-styles/index.js`** -> AI Confidence: **99.23%**
540. **`packages/editor/src/components/global-styles/menu.js`** -> AI Confidence: **99.23%**
541. **`packages/editor/src/components/post-actions/set-as-homepage.js`** -> AI Confidence: **99.23%**
542. **`packages/editor/src/components/post-actions/set-as-posts-page.js`** -> AI Confidence: **99.23%**
543. **`packages/editor/src/components/post-publish-button/post-publish-button-or-toggle.js`** -> AI Confidence: **99.23%**
544. **`packages/editor/src/components/post-publish-panel/maybe-upload-media.js`** -> AI Confidence: **99.23%**
545. **`packages/editor/src/components/revision-fields-diff/index.js`** -> AI Confidence: **99.23%**
546. **`packages/editor/src/hooks/navigation-link-view-button.js`** -> AI Confidence: **99.23%**
547. **`storybook/preview.jsx`** -> AI Confidence: **99.23%**
548. **`packages/block-library/src/search/index.php`** -> AI Confidence: **99.23%**
549. **`packages/components/src/border-box-control/border-box-control/hook.ts`** -> AI Confidence: **99.23%**
550. **`packages/components/src/circular-option-picker/circular-option-picker-option.tsx`** -> AI Confidence: **99.23%**
551. **`packages/components/src/dropdown-menu/index.tsx`** -> AI Confidence: **99.23%**
552. **`packages/components/src/flex/flex/hook.ts`** -> AI Confidence: **99.23%**
553. **`packages/components/src/grid/hook.ts`** -> AI Confidence: **99.23%**
554. **`packages/components/src/guide/index.tsx`** -> AI Confidence: **99.23%**
555. **`packages/components/src/input-control/input-field.tsx`** -> AI Confidence: **99.23%**
556. **`packages/components/src/input-control/styles/input-control-styles.tsx`** -> AI Confidence: **99.23%**
557. **`packages/components/src/input-control/types.ts`** -> AI Confidence: **99.23%**
558. **`packages/components/src/menu-item/index.tsx`** -> AI Confidence: **99.23%**
559. **`packages/components/src/navigation/back-button/index.tsx`** -> AI Confidence: **99.23%**
560. **`packages/compose/src/hooks/use-dialog/index.ts`** -> AI Confidence: **99.23%**
561. **`packages/core-data/src/utils/crdt-blocks.ts`** -> AI Confidence: **99.23%**
562. **`packages/data/src/components/use-select/index.ts`** -> AI Confidence: **99.23%**
563. **`packages/dataviews/src/components/dataform-controls/utils/validated-number.tsx`** -> AI Confidence: **99.23%**
564. **`packages/dataviews/src/components/dataform-layouts/regular/index.tsx`** -> AI Confidence: **99.23%**
565. **`packages/dataviews/src/hooks/use-form-validity.ts`** -> AI Confidence: **99.23%**
566. **`packages/editor/src/dataviews/fields/content-preview/content-preview-view.tsx`** -> AI Confidence: **99.23%**
567. **`packages/fields/src/actions/duplicate-post.tsx`** -> AI Confidence: **99.23%**
568. **`packages/global-styles-ui/src/palette.tsx`** -> AI Confidence: **99.23%**
569. **`packages/global-styles-ui/src/screen-revisions/index.tsx`** -> AI Confidence: **99.23%**
570. **`packages/global-styles-ui/src/screen-revisions/revisions-buttons.tsx`** -> AI Confidence: **99.23%**
571. **`packages/global-styles-ui/src/typography-example.tsx`** -> AI Confidence: **99.23%**
572. **`packages/media-fields/src/attached_to/edit.tsx`** -> AI Confidence: **99.23%**
573. **`packages/media-fields/src/author/view.tsx`** -> AI Confidence: **99.23%**
574. **`packages/sync/src/manager.ts`** -> AI Confidence: **99.23%**
575. **`packages/theme/terrazzo.config.ts`** -> AI Confidence: **99.23%**
576. **`packages/ui/src/link/link.tsx`** -> AI Confidence: **99.23%**
577. **`packages/views/src/use-view.ts`** -> AI Confidence: **99.23%**
578. **`routes/content-guidelines/api.ts`** -> AI Confidence: **99.23%**
579. **`routes/template-list/add-new-template/add-custom-template-modal-content.tsx`** -> AI Confidence: **99.23%**
580. **`packages/block-editor/src/components/inspector-controls-tabs/use-inspector-controls-tabs.js`** -> AI Confidence: **99.22%**
581. **`packages/scripts/scripts/build-blocks-manifest.js`** -> AI Confidence: **99.22%**
582. **`packages/scripts/scripts/plugin-zip.js`** -> AI Confidence: **99.22%**
583. **`packages/block-editor/src/components/block-list/block-outline.native.js`** -> AI Confidence: **99.2%**
584. **`packages/block-library/src/file/deprecated.js`** -> AI Confidence: **99.2%**
585. **`packages/block-library/src/image/save.js`** -> AI Confidence: **99.2%**
586. **`packages/block-library/src/navigation/menu-items-to-blocks.js`** -> AI Confidence: **99.2%**
587. **`packages/block-library/src/navigation-link/index.php`** -> AI Confidence: **99.2%**
588. **`packages/components/src/unit-control/utils.ts`** -> AI Confidence: **99.2%**
589. **`packages/block-directory/src/store/actions.js`** -> AI Confidence: **99.18%**
590. **`packages/block-editor/src/autocompleters/block.js`** -> AI Confidence: **99.18%**
591. **`packages/block-editor/src/components/autocomplete/index.js`** -> AI Confidence: **99.18%**
592. **`packages/block-editor/src/components/block-caption/index.native.js`** -> AI Confidence: **99.18%**
593. **`packages/block-editor/src/components/block-parent-selector/index.js`** -> AI Confidence: **99.18%**
594. **`packages/block-editor/src/components/block-pattern-setup/index.js`** -> AI Confidence: **99.18%**
595. **`packages/block-editor/src/components/block-patterns-list/index.js`** -> AI Confidence: **99.18%**
596. **`packages/block-editor/src/components/block-preview/index.js`** -> AI Confidence: **99.18%**
597. **`packages/block-editor/src/components/block-switcher/block-variation-transformations.js`** -> AI Confidence: **99.18%**
598. **`packages/block-editor/src/components/block-tools/block-toolbar-popover.js`** -> AI Confidence: **99.18%**
599. **`packages/block-editor/src/components/button-block-appender/index.native.js`** -> AI Confidence: **99.18%**
600. **`packages/block-editor/src/components/inner-blocks/index.js`** -> AI Confidence: **99.18%**
601. **`packages/block-editor/src/components/inner-blocks/index.native.js`** -> AI Confidence: **99.18%**
602. **`packages/block-editor/src/components/inserter/block-patterns-tab/index.js`** -> AI Confidence: **99.18%**
603. **`packages/block-editor/src/components/inserter/block-types-tab.native.js`** -> AI Confidence: **99.18%**
604. **`packages/block-editor/src/components/inserter/hooks/use-block-types-state.js`** -> AI Confidence: **99.18%**
605. **`packages/block-editor/src/components/inserter/media-tab/media-preview.js`** -> AI Confidence: **99.18%**
606. **`packages/block-editor/src/components/inserter/media-tab/media-tab.js`** -> AI Confidence: **99.18%**
607. **`packages/block-editor/src/components/inserter/search-results.native.js`** -> AI Confidence: **99.18%**
608. **`packages/block-editor/src/components/media-replace-flow/index.js`** -> AI Confidence: **99.18%**
609. **`packages/block-editor/src/store/test/reducer.js`** -> AI Confidence: **99.18%**
610. **`packages/block-library/src/avatar/user-control.js`** -> AI Confidence: **99.18%**
611. **`packages/block-library/src/block/edit.native.js`** -> AI Confidence: **99.18%**
612. **`packages/block-library/src/button/index.js`** -> AI Confidence: **99.18%**
613. **`packages/block-library/src/cover/focal-point-settings-button.native.js`** -> AI Confidence: **99.18%**
614. **`packages/block-library/src/details/index.js`** -> AI Confidence: **99.18%**
615. **`packages/block-library/src/embed/edit.js`** -> AI Confidence: **99.18%**
616. **`packages/block-library/src/embed/embed-preview.js`** -> AI Confidence: **99.18%**
617. **`packages/block-library/src/form/index.js`** -> AI Confidence: **99.18%**
618. **`packages/block-library/src/freeform/edit.js`** -> AI Confidence: **99.18%**
619. **`packages/block-library/src/image/test/edit.native.js`** -> AI Confidence: **99.18%**
620. **`packages/block-library/src/math/edit.js`** -> AI Confidence: **99.18%**
621. **`packages/block-library/src/missing/edit.native.js`** -> AI Confidence: **99.18%**
622. **`packages/block-library/src/navigation-link/index.js`** -> AI Confidence: **99.18%**
623. **`packages/block-library/src/navigation/edit/use-create-overlay.js`** -> AI Confidence: **99.18%**
624. **`packages/block-library/src/pullquote/edit.js`** -> AI Confidence: **99.18%**
625. **`packages/block-library/src/query-pagination/edit.js`** -> AI Confidence: **99.18%**
626. **`packages/block-library/src/query/edit/inspector-controls/parent-control.js`** -> AI Confidence: **99.18%**
627. **`packages/block-library/src/social-link/edit.js`** -> AI Confidence: **99.18%**
628. **`packages/block-library/src/tag-cloud/edit.js`** -> AI Confidence: **99.18%**
629. **`packages/block-library/src/template-part/edit/advanced-controls.js`** -> AI Confidence: **99.18%**
630. **`packages/block-library/src/template-part/edit/selection-modal.js`** -> AI Confidence: **99.18%**
631. **`packages/block-library/src/template-part/edit/utils/hooks.js`** -> AI Confidence: **99.18%**
632. **`packages/block-library/src/term-name/edit.js`** -> AI Confidence: **99.18%**
633. **`packages/components/src/mobile/bottom-sheet-select-control/index.native.js`** -> AI Confidence: **99.18%**
634. **`packages/components/src/mobile/bottom-sheet/index.native.js`** -> AI Confidence: **99.18%**
635. **`packages/components/src/mobile/keyboard-aware-flat-list/index.ios.js`** -> AI Confidence: **99.18%**
636. **`packages/components/src/mobile/picker/index.android.js`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bin/generate-php-sync-issue.mjs` -> **100.0%** Exposure
- `packages/block-library/src/file/edit.native.js` -> **100.0%** Exposure
- `packages/core-data/src/locks/test/selectors.js` -> **100.0%** Exposure
- `packages/edit-post/src/components/welcome-guide/default.js` -> **100.0%** Exposure
- `packages/global-styles-ui/src/font-library/lib/inflate.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bin/generate-php-sync-issue.mjs` -> **100.0%** Exposure
- `bin/packages/check-build-type-declaration-files.js` -> **100.0%** Exposure
- `bin/packages/generate-worker-placeholders.mjs` -> **100.0%** Exposure
- `bin/plugin/commands/packages.js` -> **100.0%** Exposure
- `bin/validate-tsconfig.mjs` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `packages/eslint-plugin/rules/__tests__/no-unknown-ds-tokens.js` -> **99.2872%** Exposure
- `packages/dataviews/src/hooks/test/use-form-validity.ts` -> **12.2948%** Exposure
- `packages/dataviews/src/dataform/stories/validation.tsx` -> **11.6568%** Exposure
- `packages/dataviews/src/field-types/stories/index.story.tsx` -> **9.4885%** Exposure
### Algorithmic DoS Exposure
- `bin/plugin/commands/performance.js` -> **100.0%** Exposure
- `packages/babel-plugin-import-jsx-pragma/index.js` -> **100.0%** Exposure
- `packages/block-library/src/block/test/edit.native.js` -> **100.0%** Exposure
- `packages/block-library/src/file/edit.native.js` -> **100.0%** Exposure
- `packages/block-library/src/media-text/edit.native.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13654` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecManager.java` (JAVA) -> Cumulative Risk: **893.25**
- **Archetype:** `file_cluster_13` (Distance: 11.806 IQR)
- **Magnitude:** 909.12 | **LOC:** 875 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9856%)
- **Heaviest Functions:** `setFontSize` (Impact: 283.3), `receiveCommand` (Impact: 121.6), `getHeadingScale` (Impact: 79.2)

### 2. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergEmbedWebViewActivity.java` (JAVA) -> Cumulative Risk: **870.05**
- **Archetype:** `file_cluster_4` (Distance: 10.912 IQR)
- **Magnitude:** 274.26 | **LOC:** 161 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onCreate` (Impact: 70.4), `onOptionsItemSelected` (Impact: 30.0), `setupWebViewClient` (Impact: 25.6)

### 3. `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecText.java` (JAVA) -> Cumulative Risk: **833.93**
- **Archetype:** `file_cluster_13` (Distance: 11.065 IQR)
- **Magnitude:** 761.64 | **LOC:** 720 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (98.3583%)
- **Heaviest Functions:** `setOnLongClickListener` (Impact: 595.4), `forceCaretAtStartOnTakeFocus` (Impact: 48.3), `onSelectionChanged` (Impact: 4.5)

### 4. `packages/react-native-editor/ios/GutenbergDemo/GutenbergViewController.swift` (SWIFT) -> Cumulative Risk: **828.66**
- **Archetype:** `file_cluster_8` (Distance: 11.374 IQR)
- **Magnitude:** 824.0 | **LOC:** 615 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.7633%)
- **Heaviest Functions:** `gutenbergDidRequestMedia` (Impact: 150.7), `gutenbergDidRequestMediaUploadActionDial` (Impact: 79.9), `getInitialPropsFromArgs` (Impact: 39.7)

### 5. `packages/react-native-bridge/ios/RNReactNativeGutenbergBridge.swift` (SWIFT) -> Cumulative Risk: **803.89**
- **Archetype:** `file_cluster_0` (Distance: 11.366 IQR)
- **Magnitude:** 841.58 | **LOC:** 481 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `requestMediaPickFrom` (Impact: 61.8), `sendEvent` (Impact: 43.8), `postRequest` (Impact: 34.1)

### 6. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergWebViewActivity.java` (JAVA) -> Cumulative Risk: **789.8**
- **Archetype:** `file_cluster_13` (Distance: 10.791 IQR)
- **Magnitude:** 588.22 | **LOC:** 447 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onCreate` (Impact: 70.8), `onOptionsItemSelected` (Impact: 49.8), `run` (Impact: 40.2)

### 7. `packages/react-native-aztec/ios/RNTAztecView/RCTAztecView.swift` (SWIFT) -> Cumulative Risk: **779.4**
- **Archetype:** `file_cluster_0` (Distance: 12.472 IQR)
- **Magnitude:** 1119.26 | **LOC:** 791 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.8635%)
- **Heaviest Functions:** `setContents` (Impact: 68.4), `applyFontConstraints` (Impact: 57.2), `interceptTriggersKeyCodes` (Impact: 51.4)

### 8. `packages/react-native-aztec/ios/RNTAztecView/RCTAztecViewManager.swift` (SWIFT) -> Cumulative Risk: **775.95**
- **Archetype:** `file_cluster_0` (Distance: 11.781 IQR)
- **Magnitude:** 108.72 | **LOC:** 112 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Algorithmic Dos (99.9892%), Logic Bomb (99.9885%)
- **Heaviest Functions:** `executeBlockBeforeOthers` (Impact: 22.1), `executeBlock` (Impact: 22.1), `view` (Impact: 14.8)

### 9. `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecArrowKeyMovementMethod.java` (JAVA) -> Cumulative Risk: **749.78**
- **Archetype:** `file_cluster_13` (Distance: 10.539 IQR)
- **Magnitude:** 28.76 | **LOC:** 22 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9997%)
- **Heaviest Functions:** `onTakeFocus` (Impact: 20.4)

### 10. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/DeferredEventEmitter.java` (JAVA) -> Cumulative Risk: **743.11**
- **Archetype:** `file_cluster_13` (Distance: 10.386 IQR)
- **Magnitude:** 223.54 | **LOC:** 252 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9987%)
- **Heaviest Functions:** `setMediaFileUploadDataInJS` (Impact: 22.0), `setMediaSaveResultDataInJS` (Impact: 14.0), `setMediaSaveResultDataInJS` (Impact: 14.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vips/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.855 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.798 IQR)
- **Top Global Matches:** file_cluster_17: 13.855, file_cluster_4: 13.965, file_cluster_8: 14.067
- **Magnitude:** 3889.62 | **LOC:** 3862 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (99.984%)
**Top Internal Functions/Classes:**
  * `supports` (Impact: 24.8 | O(2^N) | DB: 2)
  * `constructor` (Impact: 21.9 | O(N^1) | DB: 16)
  * `flags` (Impact: 20.6 | O(2^N))
  * `supports` (Impact: 20.6 | O(2^N) | DB: 4)
  * `supports` (Impact: 20.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 1042`, `args: 586`, `func_start: 454`, `class_start: 165`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2368`, `dead_code: 12`, `duplicate_logic: 170`
* *Architecture:* `io: 6`, `api: 38`, `concurrency: 182`, `import: 2`
* *Defense:* `safety: 126`, `doc: 1`, `immutability_locks: 181`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pako, zlib, fs, unbrotli, inflate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/inflate.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.314 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.725 IQR)
- **Top Global Matches:** file_cluster_8: 12.314, file_cluster_13: 12.732, file_cluster_7: 12.781
- **Magnitude:** 3757.5 | **LOC:** 4096 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (55.4422%), Tech Debt (21.3662%)
**Top Internal Functions/Classes:**
  * `inflate` (Impact: 3110.5 | O(2^N) | DB: 93)
  * `string2buf` (Impact: 64.2 | O(N^2) | DB: 1)
  * `buf2string` (Impact: 41.5 | O(N^2) | DB: 3)
  * `fixedtables` (Impact: 26.5 | O(N^2) | DB: 1)
    * *Intent:* // arising from the use of this software. // // Permission is granted to anyone to use this software...
  * `assign` (Impact: 24.9 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 132`, `args: 35`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 283`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 28`, `import: 8`
* *Defense:* `safety: 121`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inffast, pako, adler32, strings, messages, common, inflate, constants...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.514 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.231 IQR)
- **Top Global Matches:** file_cluster_4: 12.514, file_cluster_0: 13.428, file_cluster_8: 13.492
- **Magnitude:** 1714.06 | **LOC:** 1140 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (96.1538%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `waitForKeyboardToBeHidden` (Impact: 25.4 | O(2^N) | DB: 7)
  * `findBlockButton` (Impact: 21.1 | O(N^1) | DB: 14)
  * `swipeToolbarToElement` (Impact: 19.3 | O(N^1) | DB: 6)
  * `dismissKeyboard` (Impact: 9.8 | O(N^1) | DB: 6)
  * `scrollAndReturnElementByAccessibilityId` (Impact: 9.5 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 194`, `args: 57`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 336`
* *Architecture:* `api: 33`, `concurrency: 1087`, `import: 2`
* *Defense:* `safety: 18`, `doc: 3`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webdriverio, utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-native-aztec/ios/RNTAztecView/RCTAztecView.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.472 IQR)
- **Top Global Matches:** file_cluster_0: 12.472, file_cluster_8: 12.512, file_cluster_13: 12.714
- **Magnitude:** 1119.26 | **LOC:** 791 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (39.9717%), Tech Debt (98.6709%)
**Top Internal Functions/Classes:**
  * `setContents` (Impact: 68.4 | O(N^3))
  * `applyFontConstraints` (Impact: 57.2 | O(N^4) | DB: 2)
    * *Intent:* // MARK: - Font Refreshing /// Applies the family, size and weight constraints to the provided font....
  * `interceptTriggersKeyCodes` (Impact: 51.4 | O(N^4) | DB: 1)
  * `packCaretDataForRN` (Impact: 50.4 | O(N^4) | DB: 4)
  * `interceptBackspace` (Impact: 44.3 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 116`, `args: 56`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `state_mutation: 139`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 26`, `import: 4`
* *Defense:* `safety: 49`, `doc: 25`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UIKit, Foundation, Aztec, CoreServices
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core-data/src/resolvers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.073 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.795 IQR)
- **Top Global Matches:** file_cluster_4: 12.073, file_cluster_8: 12.174, file_cluster_0: 12.185
- **Magnitude:** 992.46 | **LOC:** 1339 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 37.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (34.9939%), Tech Debt (25.0525%)
**Top Internal Functions/Classes:**
  * `shouldInvalidate` (Impact: 790.2 | O(2^N) | DB: 75)
  * `restoreUndoMeta` (Impact: 6.0 | O(N^2))
  * `addUndoMeta` (Impact: 5.7 | O(N^2))
  * `onStatusChange` (Impact: 3.8 | O(N^2))
  * `refetchRecord` (Impact: 3.0 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 191`, `args: 82`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 31`, `api: 28`, `concurrency: 99`, `import: 10`
* *Defense:* `safety: 88`, `doc: 43`, `sync_locks: 7`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` url, change-case, api-fetch, crdt-selection, utils, entities, name, sync...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/editor/src/store/test/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.548 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.343 IQR)
- **Top Global Matches:** file_cluster_8: 9.548, file_cluster_7: 10.292, file_cluster_1: 10.469
- **Magnitude:** 946.8 | **LOC:** 2845 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (7.8344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 799.8 | O(2^N) | DB: 32)
  * `select` (Impact: 41.8 | O(N^1) | DB: 4)
    * *Intent:* /** * Internal dependencies */
  * `describe` (Impact: 6.2 | O(N^1))
  * `select` (Impact: 5.5 | O(2^N))
  * `describe` (Impact: 5.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 387`, `args: 268`, `func_start: 429`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 10`, `import: 4`
* *Defense:* `safety: 4`, `doc: 3`, `test: 336`, `immutability_locks: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deep-freeze, blocks, selectors, element
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/reducer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.658 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.239 IQR)
- **Top Global Matches:** file_cluster_8: 12.658, file_cluster_13: 12.844, file_cluster_7: 12.876
- **Magnitude:** 923.22 | **LOC:** 3138 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 38.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (22.89%), Tech Debt (19.6646%)
**Top Internal Functions/Classes:**
  * `withBlockReset` (Impact: 609.1 | O(N^2) | DB: 9)
  * `withPersistentBlockChange` (Impact: 34.4 | O(N^1) | DB: 5)
  * `withInnerBlocksRemoveCascade` (Impact: 31.2 | O(N^1) | DB: 3)
  * `updateParentInnerBlocksInTree` (Impact: 25.6 | O(2^N))
  * `updateBlockTreeForBlocks` (Impact: 15.4 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 169`, `args: 63`, `func_start: 59`
* *Risk/State:* `state_mutation: 94`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 22`, `import: 9`
* *Defense:* `safety: 74`, `doc: 116`, `sync_locks: 1`, `immutability_locks: 77`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` compose, data, index.js, deprecated, defaults, array, blocks, lock-unlock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecManager.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.806 IQR)
- **Top Global Matches:** file_cluster_13: 11.806, file_cluster_0: 12.047, file_cluster_8: 12.279
- **Magnitude:** 909.12 | **LOC:** 875 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (87.1655%), Tech Debt (97.7958%)
**Top Internal Functions/Classes:**
  * `setFontSize` (Impact: 283.3 | O(2^N) | DB: 25)
  * `receiveCommand` (Impact: 121.6 | O(2^N))
  * `getHeadingScale` (Impact: 79.2 | O(N^4))
    * *Intent:* /* .put(
  * `setActiveFormats` (Impact: 35.2 | O(2^N) | DB: 3)
  * `addEventEmitters` (Impact: 32.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 138`, `args: 42`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 137`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 59`
* *Defense:* `test: 1`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.facebook.react.bridge.ReadableMap, android.os.Looper, com.facebook.react.views.text.ReactFontManager, android.graphics.text.LineBreaker, java.util.Arrays, android.view.Gravity, com.facebook.react.uimanager.events.EventDispatcher, com.facebook.react.common.MapBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/ios/RNReactNativeGutenbergBridge.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.366 IQR)
- **Top Global Matches:** file_cluster_0: 11.366, file_cluster_8: 11.653, file_cluster_4: 11.74
- **Magnitude:** 841.58 | **LOC:** 481 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (73.0906%), Tech Debt (99.8999%)
**Top Internal Functions/Classes:**
  * `requestMediaPickFrom` (Impact: 61.8 | O(N^5))
  * `sendEvent` (Impact: 43.8 | O(2^N) | DB: 1)
  * `postRequest` (Impact: 34.1 | O(N^4))
  * `requestMediaEditor` (Impact: 32.4 | O(N^5))
  * `requestMediaImport` (Impact: 32.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 38`, `args: 57`, `func_start: 46`, `class_start: 8`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 38`
* *Architecture:* `api: 43`, `concurrency: 42`, `import: 1`
* *Defense:* `safety: 24`, `doc: 6`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` React
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-editor/ios/GutenbergDemo/GutenbergViewController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.374 IQR)
- **Top Global Matches:** file_cluster_8: 11.374, file_cluster_0: 11.556, file_cluster_13: 11.775
- **Magnitude:** 824.0 | **LOC:** 615 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (53.2072%), Tech Debt (99.7633%)
**Top Internal Functions/Classes:**
  * `gutenbergDidRequestMedia` (Impact: 150.7 | O(N^6))
  * `gutenbergDidRequestMediaUploadActionDial` (Impact: 79.9 | O(N^4) | DB: 1)
  * `getInitialPropsFromArgs` (Impact: 39.7 | O(N^4))
  * `alertWithTextInput` (Impact: 37.5 | O(N^3))
  * `configureNavigationBar` (Impact: 32.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 71`, `args: 75`, `func_start: 65`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 66`, `duplicate_logic: 2`, `orphaned_logic: 39`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 20`, `doc: 2`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` UIKit, Aztec, Gutenberg
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/navigation/index.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.923 IQR)
- **Top Global Matches:** file_cluster_8: 13.923, file_cluster_7: 14.056, file_cluster_13: 14.163
- **Magnitude:** 819.94 | **LOC:** 1812 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (35.5762%), Tech Debt (12.7484%)
**Top Internal Functions/Classes:**
  * `get_responsive_container_classes` (Impact: 98.0 | O(N^2) | DB: 39)
  * `disable_overlay_menu_for_nested_navigati` (Impact: 46.2 | O(2^N) | DB: 1)
  * `block_core_navigation_build_css_colors` (Impact: 42.1 | O(N^1) | DB: 9)
    * *Intent:* /** * Get responsive container classes for the navigation block. * * @since 7.0.0 * * @param bool $i...
  * `has_submenus` (Impact: 41.7 | O(2^N) | DB: 3)
  * `block_core_navigation_block_tree_has_blo` (Impact: 29.0 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 117`, `args: 33`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 340`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 14`
* *Defense:* `safety: 41`, `doc: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` s a null block with '\n\n', static function ( $block ) 
			return isset( $block['blockName']
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/test/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.718 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.348 IQR)
- **Top Global Matches:** file_cluster_8: 9.718, file_cluster_7: 10.417, file_cluster_1: 10.621
- **Magnitude:** 813.74 | **LOC:** 5099 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 433.6 | O(2^N) | DB: 1)
  * `describe` (Impact: 51.3 | O(2^N))
  * `describe` (Impact: 29.5 | O(N^2))
  * `describe` (Impact: 23.1 | O(N^1))
  * `describe` (Impact: 20.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 421`, `args: 285`, `func_start: 554`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 5`, `planned_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `concurrency: 28`, `import: 8`
* *Defense:* `safety: 5`, `doc: 2`, `test: 446`, `sync_locks: 8`, `immutability_locks: 209`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` data, lock-unlock, icons, .., blocks, selectors, private-keys, element
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.562 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.426 IQR)
- **Top Global Matches:** file_cluster_8: 12.562, file_cluster_7: 12.7, file_cluster_13: 12.75
- **Magnitude:** 811.32 | **LOC:** 3363 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 29.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (10.5465%), Tech Debt (14.9167%)
**Top Internal Functions/Classes:**
  * `__unstableGetSelectedBlocksWithPartialSe` (Impact: 430.8 | O(N^2) | DB: 12)
    * *Intent:* /** * Given a block client ID, returns the list of all its parents from top to bottom. * * @param {O...
  * `getAdjacentBlockClientId` (Impact: 18.0 | O(N^1))
  * `__unstableGetClientIdWithClientIdsTree` (Impact: 15.1 | O(N^1) | DB: 3)
    * *Intent:* /** * Returns whether a block is valid or not. * * @param {Object} state Editor state. * @param {str...
  * `getBlocks` (Impact: 12.5 | O(N^1))
    * *Intent:* /** * Returns a block's name given its client ID, or null if no block exists with * the client ID. *...
  * `__unstableIsSelectionCollapsed` (Impact: 11.7 | O(N^1))
    * *Intent:* * let activeBlockClientId = null * * const getActiveBlockData = () => { * const activeBlock = select...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 350`, `args: 154`, `func_start: 111`
* *Risk/State:* `state_mutation: 64`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 100`, `import: 12`
* *Defense:* `safety: 73`, `doc: 301`, `sync_locks: 6`, `immutability_locks: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` block-editor, private-selectors, data, hooks, icons, deprecated, utils, block-editing-mode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/search/index.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.83 IQR)
- **Top Global Matches:** file_cluster_8: 13.83, file_cluster_7: 14.057, file_cluster_13: 14.096
- **Magnitude:** 797.64 | **LOC:** 622 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 108
- **Risk Profile:** Cognitive Load (36.2171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render_block_core_search` (Impact: 528.2 | O(2^N) | DB: 108)
    * *Intent:* /** * Server-side rendering of the `core/search` block.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 33`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 260`, `dead_code: 1`
* *Architecture:* None
* *Defense:* `safety: 47`, `doc: 36`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` d in an HTML style tag.
 * This excludes text-decoration, the button element class.
		$button_classes[] = wp_theme_get_element_class_name( 'button', $inline_styles['input'] ), 
function get_typography_styles_for_block_core_search( $attributes ) 
	$typography_styles = array(, >'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/RNReactNativeGutenbergBridgeModule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.916 IQR)
- **Top Global Matches:** file_cluster_0: 9.916, file_cluster_13: 9.992, file_cluster_8: 10.048
- **Magnitude:** 793.86 | **LOC:** 611 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.9803%), Tech Debt (94.3479%)
**Top Internal Functions/Classes:**
  * `requestMediaPickFrom` (Impact: 63.2 | O(2^N))
  * `getMediaTypeFromFilter` (Impact: 61.2 | O(N^5))
  * `onMediaFileSelected` (Impact: 55.5 | O(N^6))
  * `fetchRequest` (Impact: 35.7 | O(N^6))
  * `postRequest` (Impact: 35.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 145`, `args: 81`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 14`, `dead_code: 1`, `orphaned_logic: 27`
* *Architecture:* `api: 72`, `concurrency: 3`, `import: 38`
* *Defense:* `safety: 2`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.facebook.react.bridge.Callback, com.facebook.react.bridge.ReadableMap, org.wordpress.mobile.ReactNativeGutenbergBridge.GutenbergBridgeJS2Parent.OtherMediaOptionsReceivedCallback, org.wordpress.mobile.WPAndroidGlue.DeferredEventEmitter, android.app.Activity, org.wordpress.mobile.ReactNativeGutenbergBridge.GutenbergBridgeJS2Parent.FocalPointPickerTooltipShownCallback, com.facebook.react.modules.core.DeviceEventManagerModule, com.facebook.react.bridge.WritableMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/components/rich-text/native/index.native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.216 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.276 IQR)
- **Top Global Matches:** file_cluster_17: 14.216, file_cluster_13: 14.266, file_cluster_0: 14.415
- **Magnitude:** 763.84 | **LOC:** 1389 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (71.0217%), Tech Debt (10.4436%)
**Top Internal Functions/Classes:**
  * `handleDelete` (Impact: 62.3 | O(2^N) | DB: 9)
  * `getLineHeight` (Impact: 35.7 | O(N^1) | DB: 7)
  * `onSelectionChange` (Impact: 25.3 | O(2^N) | DB: 11)
  * `onPaste` (Impact: 22.2 | O(2^N) | DB: 7)
  * `onBlur` (Impact: 20.9 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 82`, `args: 45`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 426`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 22`
* *Defense:* `safety: 93`, `doc: 12`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` components, i18n, html-entities, blocks, react-native, block-editor, element, url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecText.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.065 IQR)
- **Top Global Matches:** file_cluster_13: 11.065, file_cluster_8: 11.394, file_cluster_0: 11.442
- **Magnitude:** 761.64 | **LOC:** 720 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (32.4875%), Tech Debt (58.5065%)
**Top Internal Functions/Classes:**
  * `setOnLongClickListener` (Impact: 595.4 | O(N^6) | DB: 30)
  * `forceCaretAtStartOnTakeFocus` (Impact: 48.3 | O(N^6) | DB: 1)
  * `onSelectionChanged` (Impact: 4.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 126`, `args: 47`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 70`, `planned_debt: 1`, `fragile_debt: 3`, `orphaned_logic: 3`
* *Architecture:* `api: 27`, `concurrency: 8`, `import: 43`
* *Defense:* `safety: 3`, `doc: 4`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` android.os.Looper, java.util.HashSet, org.wordpress.aztec.AlignmentRendering, java.util.Set, com.facebook.react.uimanager.events.EventDispatcher, androidx.annotation.NonNull, android.text.Editable, android.text.TextUtils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/ios/Gutenberg.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.313 IQR)
- **Top Global Matches:** file_cluster_8: 11.313, file_cluster_13: 11.489, file_cluster_0: 11.651
- **Magnitude:** 589.08 | **LOC:** 366 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (44.6736%), Tech Debt (99.1561%)
**Top Internal Functions/Classes:**
  * `supportedBlocks` (Impact: 167.3 | O(2^N) | DB: 1)
  * `properties` (Impact: 59.2 | O(N^3) | DB: 1)
  * `mediaUpdate` (Impact: 51.8 | O(N^3) | DB: 1)
  * `sourceURL` (Impact: 32.5 | O(N^3) | DB: 1)
  * `mediaUploadUpdate` (Impact: 20.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 47`, `args: 36`, `func_start: 33`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 44`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 23`, `doc: 3`, `sync_locks: 3`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UIKit, Aztec, Network, RNTAztecView
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergWebViewActivity.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.791 IQR)
- **Top Global Matches:** file_cluster_13: 10.791, file_cluster_8: 10.879, file_cluster_4: 10.91
- **Magnitude:** 588.22 | **LOC:** 447 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (46.0161%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onCreate` (Impact: 70.8 | O(2^N) | DB: 7)
  * `onOptionsItemSelected` (Impact: 49.8 | O(2^N))
  * `run` (Impact: 40.2 | O(N^6) | DB: 1)
  * `setupWebViewClient` (Impact: 30.9 | O(N^6) | DB: 1)
  * `onBackPressed` (Impact: 24.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 90`, `args: 51`, `func_start: 68`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 42`
* *Architecture:* `api: 41`, `concurrency: 42`, `import: 29`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.093
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` android.view.ActionMode, android.webkit.JavascriptInterface, android.graphics.Bitmap, androidx.appcompat.app.ActionBar, java.util.Locale, android.webkit.WebView, android.webkit.WebChromeClient, java.util.concurrent.atomic.AtomicBoolean...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/block-editor/src/components/list-view/block.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.954 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.296 IQR)
- **Top Global Matches:** file_cluster_8: 9.954, file_cluster_13: 10.169, file_cluster_2: 10.26
- **Magnitude:** 580.88 | **LOC:** 723 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 41.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (12.1899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onKeyDown` (Impact: 551.7 | O(2^N) | DB: 7)
  * `getBlocksToUpdate` (Impact: 6.2 | O(N^1))
  * `ListViewBlock` (Impact: 1.5 | O(N^1) | DB: 3)
  * `hasBlockSupport` (Impact: 1.5 | O(N^1))
  * `select` (Impact: 1.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 61`, `args: 21`, `func_start: 36`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 4`, `import: 26`
* *Defense:* `safety: 22`, `doc: 5`, `sync_locks: 2`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` use-paste-styles, lock-unlock, components, i18n, utils, block-visibility, blocks, element...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/rich-text/src/create.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.534 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.338 IQR)
- **Top Global Matches:** file_cluster_8: 11.534, file_cluster_13: 11.768, file_cluster_7: 11.861
- **Magnitude:** 487.4 | **LOC:** 695 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.4602%), Tech Debt (53.1209%)
**Top Internal Functions/Classes:**
  * `accumulateSelection` (Impact: 250.0 | O(2^N) | DB: 1)
  * `collapseWhiteSpace` (Impact: 92.1 | O(2^N) | DB: 1)
    * *Intent:* * { * text: string, * formats: Array, * replacements: Array, * ?start: number, * ?end: number, * } *...
  * `accumulateSelection` (Impact: 60.9 | O(N^1))
  * `filterRange` (Impact: 8.9 | O(N^1) | DB: 1)
    * *Intent:* /** * Create a RichText value from an `Element` tree (DOM), an HTML string or a * plain text string,...
  * `length` (Impact: 3.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 52`, `args: 20`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`, `duplicate_logic: 4`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 45`, `doc: 43`, `immutability_locks: 28`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` data, special-characters, to-html-string, concat, store, create-element, types, get-text-content
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.098 IQR)
- **Top Global Matches:** file_cluster_13: 10.098, file_cluster_8: 10.355, file_cluster_16: 10.749
- **Magnitude:** 479.96 | **LOC:** 1178 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (18.3627%), Tech Debt (97.5736%)
**Top Internal Functions/Classes:**
  * `getPackages` (Impact: 329.0 | O(N^6) | DB: 8)
  * `onCreate` (Impact: 3.5 | O(N^2))
  * `gutenbergDidSendButtonPressedAction` (Impact: 3.4 | O(N^2))
  * `onEditorDidMount` (Impact: 3.3 | O(N^2))
  * `gutenbergDidRequestUnsupportedBlockFallb` (Impact: 3.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 183`, `args: 86`, `func_start: 92`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 14`, `fragile_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 63`, `concurrency: 12`, `import: 70`
* *Defense:* `doc: 1`, `sync_locks: 2`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` com.facebook.react.bridge.ReadableMap, android.os.Looper, com.facebook.hermes.reactexecutor.HermesExecutorFactory, com.facebook.soloader.SoLoader, com.swmansion.gesturehandler.RNGestureHandlerPackage, java.util.Arrays, androidx.core.util.Pair, com.facebook.imagepipeline.core.ImagePipelineConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/media-text/edit.native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.209 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.323 IQR)
- **Top Global Matches:** file_cluster_13: 12.209, file_cluster_8: 12.276, file_cluster_2: 12.363
- **Magnitude:** 475.52 | **LOC:** 418 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (40.8957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyWidthConstraints` (Impact: 366.6 | O(2^N) | DB: 59)
  * `select` (Impact: 2.6 | O(N^1))
  * `withSelect` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 28`, `args: 20`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 97`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 24`, `doc: 3`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` data, compose, i18n, components, icons, media-container, constants, react-native...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/core-data/src/entities.js` (JAVASCRIPT) | Magnitude: 65.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 100, structural_boundaries: 33, doc: 22, branch: 21
- `packages/core-data/src/hooks/use-query-select.ts` (TYPESCRIPT) | Magnitude: 3.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, structural_boundaries: 31, branch: 18, doc: 13
- `packages/core-data/src/footnotes/get-rich-text-values-cached.js` (JAVASCRIPT) | Magnitude: 12.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 5, branch: 3, state_mutation: 3
- `packages/ui/src/lock-unlock.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, branch: 2, structural_boundaries: 2, decorators: 2
- `packages/priority-queue/src/index.ts` (TYPESCRIPT) | Magnitude: 6.63 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 24, doc: 24, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/block-library/src/template-part/edit/utils/create-template-part-id.js` (JAVASCRIPT) | Magnitude: 7.5 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, decorators: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/block-library/src/gallery/index.php` (PHP) | Magnitude: 203.5 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 124, indent_tabs: 83, branch: 32, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/react-native-editor/bin/test-e2e-setup.sh` (SHELL) | Magnitude: 98.62 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 50, safety_bypasses: 43, state_mutation: 39, structural_boundaries: 35
- `packages/i18n/src/default-i18n.ts` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 51, structural_boundaries: 14, api: 11, immutability_locks: 11
- `packages/react-native-editor/bin/build-e2e-wda.sh` (SHELL) | Magnitude: 4.62 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, reflection_metaprogramming: 3, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/blocks/src/api/raw-handling/blockquote-normaliser.js` (JAVASCRIPT) | Magnitude: 7.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 5, branch: 2, args: 2
- `packages/boot/src/components/app/router.tsx` (TYPESCRIPT) | Magnitude: 13.11 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 153, structural_boundaries: 55, concurrency: 42, branch: 26
- `packages/components/src/shortcut/test/index.tsx` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 25, args: 12, func_start: 12, test: 9
- `packages/editor/src/components/post-template/hooks.js` (JAVASCRIPT) | Magnitude: 63.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 92, structural_boundaries: 28, branch: 24, immutability_locks: 16
- `packages/components/src/autocomplete/types.ts` (TYPESCRIPT) | Magnitude: 4.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 20, indent_tabs: 14, doc: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts` (TYPESCRIPT) | Magnitude: 26.3 | Delta: **0.211 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_tabs: 16, args: 15, func_start: 14
- `packages/block-editor/src/utils/get-px-from-css-unit.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.434 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/compose/src/higher-order/if-condition/index.tsx` (TYPESCRIPT) | Magnitude: 1.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 10, doc: 5, args: 3
- `packages/components/src/alignment-matrix-control/types.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 9, doc: 8, branch: 7
- `packages/dataviews/src/field-types/utils/is-valid-required-for-array.ts` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 5, branch: 3, args: 3
- `packages/core-data/src/hooks/use-resource-permissions.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 13, doc: 13, generics: 8
- `packages/global-styles-ui/src/with-global-styles-provider.tsx` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 9, doc: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/sync/src/y-utilities/y-multidoc-undomanager.js` (JAVASCRIPT) | Magnitude: 165.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 134, state_mutation: 83, doc: 43, structural_boundaries: 34
- `packages/global-styles-ui/src/font-library/font-demo.tsx` (TYPESCRIPT) | Magnitude: 5.73 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 86, branch: 24, structural_boundaries: 24, args: 13
- `packages/block-editor/src/components/media-upload/index.native.js` (JAVASCRIPT) | Magnitude: 249.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 284, state_mutation: 91, branch: 47, structural_boundaries: 44
- `packages/block-editor/src/components/preset-input-control/utils.js` (JAVASCRIPT) | Magnitude: 67.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 25, branch: 19, doc: 19
- `packages/editor/src/components/entities-saved-states/entity-type-list.js` (JAVASCRIPT) | Magnitude: 33.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 101, structural_boundaries: 23, branch: 21, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/block-library/src/group/placeholder.js` (JAVASCRIPT) | Magnitude: 37.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 102, branch: 16, structural_boundaries: 15, ui_framework: 14
- `packages/editor/src/components/entities-saved-states/index.js` (JAVASCRIPT) | Magnitude: 29.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 167, doc: 24, branch: 22, structural_boundaries: 22
- `packages/block-library/src/html/edit.js` (JAVASCRIPT) | Magnitude: 4.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 73, ui_framework: 16, structural_boundaries: 15, import: 7
- `packages/components/src/composite/legacy/stories/index.story.tsx` (TYPESCRIPT) | Magnitude: 2.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 167, ui_framework: 38, generics: 38, structural_boundaries: 17
- `packages/block-directory/src/components/downloadable-block-icon/index.js` (JAVASCRIPT) | Magnitude: 2.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 6, branch: 5, structural_boundaries: 3, ui_framework: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/theme/bin/terrazzo-plugin-typescript-types/index.ts` (TYPESCRIPT) | Magnitude: 11.85 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 68, branch: 16, doc: 16, structural_boundaries: 15
- `packages/compose/src/hooks/use-copy-to-clipboard/index.ts` (TYPESCRIPT) | Magnitude: 8.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 66, structural_boundaries: 25, branch: 20, doc: 17
- `packages/components/src/utils/element-rect.ts` (TYPESCRIPT) | Magnitude: 3.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 14, concurrency: 13, doc: 11
- `packages/components/src/popover/test/index.tsx` (TYPESCRIPT) | Magnitude: 32.16 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 450, concurrency: 228, structural_boundaries: 133, args: 120
- `packages/interactivity/src/utils.ts` (TYPESCRIPT) | Magnitude: 24.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 218, structural_boundaries: 98, args: 61, doc: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/block-serialization-default-parser/class-wp-block-parser-block.php` (PHP) | Magnitude: 14.1 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, indent_tabs: 12, api: 6, state_mutation: 5
- `packages/block-serialization-default-parser/class-wp-block-parser-frame.php` (PHP) | Magnitude: 26.5 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, state_mutation: 15, indent_tabs: 12, api: 6
- `packages/annotations/src/store/constants.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1
- `packages/core-data/src/name.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1
- `packages/edit-site/src/store/constants.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/customize-widgets/src/filters/replace-media-upload.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, func_start: 2, decorators: 2
- `packages/edit-widgets/src/filters/replace-media-upload.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, func_start: 2, decorators: 2
- `packages/editor/src/components/post-excerpt/panel.js` (JAVASCRIPT) | Magnitude: 50.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 145, structural_boundaries: 30, ui_framework: 18, immutability_locks: 17
- `packages/patterns/src/components/duplicate-pattern-modal.js` (JAVASCRIPT) | Magnitude: 18.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 18, branch: 9, args: 8
- `packages/components/src/button-group/stories/index.story.tsx` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 6, doc: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/block-library/src/video/index.php` (PHP) | Magnitude: 10.64 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, doc: 5, structural_boundaries: 3
- `packages/rich-text/src/create-element.js` (JAVASCRIPT) | Magnitude: 2.24 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 5, doc: 4, structural_boundaries: 2, branch: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/block-library/src/navigation/edit/index.js` -> Churn: **54.93%** | Cog Load: 8.1913% | Debt: 97.5343%
- `packages/block-editor/src/hooks/fit-text.js` -> Churn: **51.07%** | Cog Load: 8.9267% | Debt: 72.1908%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **Riad Benguella** (100.0% isolated ownership) | Magnitude: 3889.62
- `packages/react-native-editor/__device-tests__/pages/editor-page.js` -> **Ella** (100.0% isolated ownership) | Magnitude: 1714.06
- `packages/editor/src/store/test/selectors.js` -> **Aki Hamano** (100.0% isolated ownership) | Magnitude: 946.8
- `packages/rich-text/src/create.js` -> **Ella** (100.0% isolated ownership) | Magnitude: 487.4
- `packages/url/src/test/index.js` -> **Manuel Camargo** (100.0% isolated ownership) | Magnitude: 416.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/eslint-plugin/configs/i18n.js` -> **Severity: 5148.323** (Blast Radius: 56.505 * Doc Risk: 91.1127%)
- `storybook/stories/tokens/components.tsx` -> **Severity: 2372.494** (Blast Radius: 47.304 * Doc Risk: 50.1542%)
- `packages/e2e-test-utils-playwright/src/request-utils/blocks.ts` -> **Severity: 574.863** (Blast Radius: 26.004 * Doc Risk: 22.1067%)
- `packages/block-library/src/utils/init-block.js` -> **Severity: 379.501** (Blast Radius: 7.169 * Doc Risk: 52.9364%)
- `packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts` -> **Severity: 314.814** (Blast Radius: 4.08 * Doc Risk: 77.1604%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
