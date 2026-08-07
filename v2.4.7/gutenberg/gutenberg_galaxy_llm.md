# ARCHITECTURAL_BRIEF: gutenberg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/gutenberg` |
| **Timestamp** | `2026-08-07T04:26:07.622513+00:00` |
| **Scan Duration** | `20.84s` |
| **Git Branch** | `trunk` |
| **Git Commit** | `4af0efd09488abc25e84933c634230ac884cc2f8` |
| **Git Remote** | `https://github.com/wordpress/gutenberg.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6365 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `5.15`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4956 | 56.6% |
| file_cluster_13 | 2310 | 26.4% |
| file_cluster_2 | 239 | 2.7% |
| file_cluster_16 | 141 | 1.6% |
| file_cluster_4 | 99 | 1.1% |
| file_cluster_17 | 71 | 0.8% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 9.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 15.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 1.4 | 0.0 |
| API Exposure | 0.0 | 20.0 | 4.0 | 4.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 57.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.5 | 5.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.3 | 17.0 | 0.0 |
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

- `inflate` (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> Impact: **692.5** | LOC: 1761
- `withBlockReset` (@ `packages/block-editor/src/store/reducer.js`) -> Impact: **419.0** | LOC: 778
- `describe` (@ `packages/editor/src/store/test/selectors.js`) -> Impact: **349.5** | LOC: 2486
- `__unstableGetSelectedBlocksWithPartialSe` (@ `packages/block-editor/src/store/selectors.js`) -> Impact: **302.2** | LOC: 902
  * *Intent:* /** * Given a block client ID, returns the list of all its parents from top to bottom. * * @param {Object} state Editor state. * @param {string} clien...
- `shouldInvalidate` (@ `packages/core-data/src/resolvers.js`) -> Impact: **290.2** | LOC: 804
- `render_block_core_search` (@ `packages/block-library/src/search/index.php`) -> Impact: **277.8** | LOC: 547
  * *Intent:* /** * Server-side rendering of the `core/search` block.
- `isBlockVisibleInTheInserter` (@ `packages/block-editor/src/store/selectors.js`) -> Impact: **264.0** | LOC: 840
- `attributes` (@ `packages/block-editor/src/store/reducer.js`) -> Impact: **257.4** | LOC: 680
- `getEntityRecordNonTransientEdits` (@ `packages/core-data/src/selectors.ts`) -> Impact: **255.9** | LOC: 466
- `describe` (@ `packages/block-editor/src/store/test/selectors.js`) -> Impact: **222.3** | LOC: 2333

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/global-styles-ui/src/font-library/lib` | 4 | 6051.78 | 60.35% | 84.4% |
| `__monolith__` | 16 | 5135.88 | 3.85% | 6.25% |
| `packages/vips` | 5 | 5021.44 | 1.0% | 0.0% |
| `packages/block-editor/src/store/test` | 9 | 4378.12 | 8.61% | 0.0% |
| `packages/block-editor/src/store` | 13 | 3583.8 | 9.49% | 24.74% |
| `packages/icons/src/library` | 331 | 3482.12 | 5.0% | 0.0% |
| `packages/block-editor/src/hooks` | 66 | 2574.01 | 6.9% | 21.67% |
| `packages/block-editor/src/components/global-styles` | 17 | 2433.68 | 14.16% | 45.39% |
| `packages/core-data/src/test` | 9 | 2333.76 | 7.17% | 0.0% |
| `packages/editor/src/store/test` | 7 | 2296.88 | 9.8% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/babel-preset-default/polyfill-exclusions.js` -> **100.0%** Exposure
- `packages/block-directory/src/store/resolvers.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-list/block-crash-boundary.native.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-list/use-block-props/use-firefox-draggable-compatibility.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-mover/mover-description.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/a11y/src/shared/clear.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/filter-message.js` -> **100.0%** Exposure
- `packages/babel-preset-default/polyfill-exclusions.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/audio-player/audio-url-parser.native.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/block-list/block-crash-boundary.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **0** Orphaned Functions | **314** Duplicates
- `packages/block-editor/src/store/test/selectors.js` -> **0** Orphaned Functions | **304** Duplicates
- `packages/editor/src/store/test/selectors.js` -> **0** Orphaned Functions | **255** Duplicates
- `packages/block-editor/src/store/test/actions.js` -> **0** Orphaned Functions | **203** Duplicates
- `packages/block-editor/src/store/test/reducer.js` -> **0** Orphaned Functions | **165** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/global-styles-ui/src/font-library/lib/inflate.js`** -> AI Confidence: **99.48%**
2. **`packages/scripts/config/webpack.config.js`** -> AI Confidence: **99.48%**
3. **`packages/block-library/src/term-template/index.php`** -> AI Confidence: **99.48%**
4. **`packages/block-editor/src/components/block-list/block.js`** -> AI Confidence: **99.39%**
5. **`packages/block-editor/src/components/global-styles/dimensions-panel.js`** -> AI Confidence: **99.39%**
6. **`packages/block-library/src/button/edit.native.js`** -> AI Confidence: **99.39%**
7. **`packages/components/src/mobile/image/index.native.js`** -> AI Confidence: **99.39%**
8. **`packages/scripts/utils/config.js`** -> AI Confidence: **99.39%**
9. **`packages/components/src/button/index.tsx`** -> AI Confidence: **99.39%**
10. **`packages/block-library/src/cover/deprecated.js`** -> AI Confidence: **99.34%**
11. **`packages/edit-site/src/components/editor/use-resolve-edited-entity.js`** -> AI Confidence: **99.34%**
12. **`packages/scripts/scripts/test-playwright.js`** -> AI Confidence: **99.34%**
13. **`bin/packages/validate-typescript-version.js`** -> AI Confidence: **99.32%**
14. **`bin/plugin/commands/common.js`** -> AI Confidence: **99.32%**
15. **`packages/block-library/src/cover/save.js`** -> AI Confidence: **99.32%**
16. **`packages/block-library/src/embed/variations.js`** -> AI Confidence: **99.32%**
17. **`packages/scripts/scripts/build.js`** -> AI Confidence: **99.32%**
18. **`packages/scripts/scripts/lint-js.js`** -> AI Confidence: **99.32%**
19. **`packages/scripts/scripts/lint-md-docs.js`** -> AI Confidence: **99.32%**
20. **`packages/scripts/scripts/lint-pkg-json.js`** -> AI Confidence: **99.32%**
21. **`packages/scripts/scripts/lint-style.js`** -> AI Confidence: **99.32%**
22. **`packages/scripts/scripts/start.js`** -> AI Confidence: **99.32%**
23. **`packages/global-styles-engine/src/settings/get-palette.ts`** -> AI Confidence: **99.32%**
24. **`bin/plugin/commands/performance.js`** -> AI Confidence: **99.31%**
25. **`packages/block-editor/src/components/background-image-control/index.js`** -> AI Confidence: **99.31%**
26. **`packages/block-editor/src/components/block-card/index.js`** -> AI Confidence: **99.31%**
27. **`packages/block-editor/src/components/block-draggable/dropping-insertion-point.native.js`** -> AI Confidence: **99.31%**
28. **`packages/block-editor/src/components/block-draggable/index.js`** -> AI Confidence: **99.31%**
29. **`packages/block-editor/src/components/block-edit/edit.js`** -> AI Confidence: **99.31%**
30. **`packages/block-editor/src/components/block-list/block-list-item.native.js`** -> AI Confidence: **99.31%**
31. **`packages/block-editor/src/components/block-list/index.native.js`** -> AI Confidence: **99.31%**
32. **`packages/block-editor/src/components/block-list/use-block-props/index.js`** -> AI Confidence: **99.31%**
33. **`packages/block-editor/src/components/block-list/use-block-props/use-selected-block-event-handlers.js`** -> AI Confidence: **99.31%**
34. **`packages/block-editor/src/components/block-list/use-in-between-inserter.js`** -> AI Confidence: **99.31%**
35. **`packages/block-editor/src/components/block-list/zoom-out-separator.js`** -> AI Confidence: **99.31%**
36. **`packages/block-editor/src/components/block-lock/modal.js`** -> AI Confidence: **99.31%**
37. **`packages/block-editor/src/components/block-mover/index.js`** -> AI Confidence: **99.31%**
38. **`packages/block-editor/src/components/block-quick-navigation/index.js`** -> AI Confidence: **99.31%**
39. **`packages/block-editor/src/components/block-rename/modal.js`** -> AI Confidence: **99.31%**
40. **`packages/block-editor/src/components/block-settings-menu-controls/index.js`** -> AI Confidence: **99.31%**
41. **`packages/block-editor/src/components/block-settings-menu/block-settings-dropdown.js`** -> AI Confidence: **99.31%**
42. **`packages/block-editor/src/components/block-switcher/index.js`** -> AI Confidence: **99.31%**
43. **`packages/block-editor/src/components/block-toolbar/block-toolbar-icon.js`** -> AI Confidence: **99.31%**
44. **`packages/block-editor/src/components/block-toolbar/block-toolbar-menu.native.js`** -> AI Confidence: **99.31%**
45. **`packages/block-editor/src/components/block-toolbar/index.js`** -> AI Confidence: **99.31%**
46. **`packages/block-editor/src/components/block-tools/index.js`** -> AI Confidence: **99.31%**
47. **`packages/block-editor/src/components/block-visibility/modal.js`** -> AI Confidence: **99.31%**
48. **`packages/block-editor/src/components/border-radius-control/index.js`** -> AI Confidence: **99.31%**
49. **`packages/block-editor/src/components/child-layout-control/index.js`** -> AI Confidence: **99.31%**
50. **`packages/block-editor/src/components/contrast-checker/index.native.js`** -> AI Confidence: **99.31%**
51. **`packages/block-editor/src/components/default-block-appender/index.native.js`** -> AI Confidence: **99.31%**
52. **`packages/block-editor/src/components/global-styles/background-panel.js`** -> AI Confidence: **99.31%**
53. **`packages/block-editor/src/components/global-styles/border-panel.js`** -> AI Confidence: **99.31%**
54. **`packages/block-editor/src/components/global-styles/color-panel.js`** -> AI Confidence: **99.31%**
55. **`packages/block-editor/src/components/global-styles/filters-panel.js`** -> AI Confidence: **99.31%**
56. **`packages/block-editor/src/components/global-styles/index.js`** -> AI Confidence: **99.31%**
57. **`packages/block-editor/src/components/global-styles/typography-panel.js`** -> AI Confidence: **99.31%**
58. **`packages/block-editor/src/components/global-styles/use-global-styles-context.native.js`** -> AI Confidence: **99.31%**
59. **`packages/block-editor/src/components/grid/grid-item-movers.js`** -> AI Confidence: **99.31%**
60. **`packages/block-editor/src/components/grid/grid-visualizer.js`** -> AI Confidence: **99.31%**
61. **`packages/block-editor/src/components/image-link-destinations/index.native.js`** -> AI Confidence: **99.31%**
62. **`packages/block-editor/src/components/inner-blocks/use-nested-settings-update.js`** -> AI Confidence: **99.31%**
63. **`packages/block-editor/src/components/inserter-draggable-blocks/index.js`** -> AI Confidence: **99.31%**
64. **`packages/block-editor/src/components/inserter/hooks/use-insertion-point.js`** -> AI Confidence: **99.31%**
65. **`packages/block-editor/src/components/inserter/index.js`** -> AI Confidence: **99.31%**
66. **`packages/block-editor/src/components/inspector-controls/fill.js`** -> AI Confidence: **99.31%**
67. **`packages/block-editor/src/components/link-control/link-preview.js`** -> AI Confidence: **99.31%**
68. **`packages/block-editor/src/components/list-view/block.js`** -> AI Confidence: **99.31%**
69. **`packages/block-editor/src/components/list-view/branch.js`** -> AI Confidence: **99.31%**
70. **`packages/block-editor/src/components/list-view/drop-indicator.js`** -> AI Confidence: **99.31%**
71. **`packages/block-editor/src/components/list-view/use-block-selection.js`** -> AI Confidence: **99.31%**
72. **`packages/block-editor/src/components/media-placeholder/index.native.js`** -> AI Confidence: **99.31%**
73. **`packages/block-editor/src/components/media-upload-progress/index.native.js`** -> AI Confidence: **99.31%**
74. **`packages/block-editor/src/components/media-upload/index.native.js`** -> AI Confidence: **99.31%**
75. **`packages/block-editor/src/components/preset-input-control/index.js`** -> AI Confidence: **99.31%**
76. **`packages/block-editor/src/components/provider/index.js`** -> AI Confidence: **99.31%**
77. **`packages/block-editor/src/components/rich-text/index.native.js`** -> AI Confidence: **99.31%**
78. **`packages/block-editor/src/components/rich-text/native/index.native.js`** -> AI Confidence: **99.31%**
79. **`packages/block-editor/src/components/spacing-sizes-control/index.js`** -> AI Confidence: **99.31%**
80. **`packages/block-editor/src/components/unsupported-block-details/index.native.js`** -> AI Confidence: **99.31%**
81. **`packages/block-editor/src/components/url-input/index.js`** -> AI Confidence: **99.31%**
82. **`packages/block-editor/src/components/use-block-drop-zone/index.js`** -> AI Confidence: **99.31%**
83. **`packages/block-editor/src/components/use-block-drop-zone/index.native.js`** -> AI Confidence: **99.31%**
84. **`packages/block-editor/src/components/writing-flow/use-clipboard-handler.js`** -> AI Confidence: **99.31%**
85. **`packages/block-editor/src/components/writing-flow/use-tab-nav.js`** -> AI Confidence: **99.31%**
86. **`packages/block-editor/src/hooks/anchor.js`** -> AI Confidence: **99.31%**
87. **`packages/block-editor/src/hooks/background.js`** -> AI Confidence: **99.31%**
88. **`packages/block-editor/src/hooks/block-fields/link/index.js`** -> AI Confidence: **99.31%**
89. **`packages/block-editor/src/hooks/block-fields/media/index.js`** -> AI Confidence: **99.31%**
90. **`packages/block-editor/src/hooks/block-fields/rich-text/index.js`** -> AI Confidence: **99.31%**
91. **`packages/block-editor/src/hooks/block-style-variation.js`** -> AI Confidence: **99.31%**
92. **`packages/block-editor/src/hooks/custom-class-name.js`** -> AI Confidence: **99.31%**
93. **`packages/block-editor/src/hooks/duotone.js`** -> AI Confidence: **99.31%**
94. **`packages/block-editor/src/hooks/grid-visualizer.js`** -> AI Confidence: **99.31%**
95. **`packages/block-editor/src/hooks/layout.js`** -> AI Confidence: **99.31%**
96. **`packages/block-editor/src/hooks/position.js`** -> AI Confidence: **99.31%**
97. **`packages/block-editor/src/layouts/constrained.js`** -> AI Confidence: **99.31%**
98. **`packages/block-editor/src/layouts/flex.js`** -> AI Confidence: **99.31%**
99. **`packages/block-editor/src/layouts/grid.js`** -> AI Confidence: **99.31%**
100. **`packages/block-editor/src/store/reducer.js`** -> AI Confidence: **99.31%**
101. **`packages/block-library/src/breadcrumbs/edit.js`** -> AI Confidence: **99.31%**
102. **`packages/block-library/src/button/edit.js`** -> AI Confidence: **99.31%**
103. **`packages/block-library/src/categories/edit.js`** -> AI Confidence: **99.31%**
104. **`packages/block-library/src/column/edit.native.js`** -> AI Confidence: **99.31%**
105. **`packages/block-library/src/comments-title/edit.js`** -> AI Confidence: **99.31%**
106. **`packages/block-library/src/cover/controls.native.js`** -> AI Confidence: **99.31%**
107. **`packages/block-library/src/cover/edit.native.js`** -> AI Confidence: **99.31%**
108. **`packages/block-library/src/cover/edit/inspector-controls.js`** -> AI Confidence: **99.31%**
109. **`packages/block-library/src/file/edit.native.js`** -> AI Confidence: **99.31%**
110. **`packages/block-library/src/footnotes/format.js`** -> AI Confidence: **99.31%**
111. **`packages/block-library/src/gallery/edit.js`** -> AI Confidence: **99.31%**
112. **`packages/block-library/src/group/edit.js`** -> AI Confidence: **99.31%**
113. **`packages/block-library/src/group/edit.native.js`** -> AI Confidence: **99.31%**
114. **`packages/block-library/src/heading/edit.native.js`** -> AI Confidence: **99.31%**
115. **`packages/block-library/src/image/edit.js`** -> AI Confidence: **99.31%**
116. **`packages/block-library/src/image/edit.native.js`** -> AI Confidence: **99.31%**
117. **`packages/block-library/src/latest-posts/edit.js`** -> AI Confidence: **99.31%**
118. **`packages/block-library/src/media-text/edit.js`** -> AI Confidence: **99.31%**
119. **`packages/block-library/src/media-text/edit.native.js`** -> AI Confidence: **99.31%**
120. **`packages/block-library/src/missing/edit.js`** -> AI Confidence: **99.31%**
121. **`packages/block-library/src/navigation-link/edit.js`** -> AI Confidence: **99.31%**
122. **`packages/block-library/src/navigation/edit/index.js`** -> AI Confidence: **99.31%**
123. **`packages/block-library/src/navigation/edit/navigation-menu-selector.js`** -> AI Confidence: **99.31%**
124. **`packages/block-library/src/page-list/edit.js`** -> AI Confidence: **99.31%**
125. **`packages/block-library/src/paragraph/edit.js`** -> AI Confidence: **99.31%**
126. **`packages/block-library/src/pattern/edit.js`** -> AI Confidence: **99.31%**
127. **`packages/block-library/src/playlist-track/edit.js`** -> AI Confidence: **99.31%**
128. **`packages/block-library/src/post-author/edit.js`** -> AI Confidence: **99.31%**
129. **`packages/block-library/src/post-content/edit.js`** -> AI Confidence: **99.31%**
130. **`packages/block-library/src/post-excerpt/edit.js`** -> AI Confidence: **99.31%**
131. **`packages/block-library/src/post-featured-image/edit.js`** -> AI Confidence: **99.31%**
132. **`packages/block-library/src/post-template/edit.js`** -> AI Confidence: **99.31%**
133. **`packages/block-library/src/post-terms/edit.js`** -> AI Confidence: **99.31%**
134. **`packages/block-library/src/query-title/edit.js`** -> AI Confidence: **99.31%**
135. **`packages/block-library/src/query/edit/inspector-controls/index.js`** -> AI Confidence: **99.31%**
136. **`packages/block-library/src/query/edit/inspector-controls/taxonomy-controls.js`** -> AI Confidence: **99.31%**
137. **`packages/block-library/src/query/edit/query-placeholder.js`** -> AI Confidence: **99.31%**
138. **`packages/block-library/src/search/edit.native.js`** -> AI Confidence: **99.31%**
139. **`packages/block-library/src/spacer/edit.js`** -> AI Confidence: **99.31%**
140. **`packages/block-library/src/template-part/edit/index.js`** -> AI Confidence: **99.31%**
141. **`packages/block-library/src/term-template/edit.js`** -> AI Confidence: **99.31%**
142. **`packages/block-library/src/utils/caption.js`** -> AI Confidence: **99.31%**
143. **`packages/components/src/autocomplete/autocompleter-ui.native.js`** -> AI Confidence: **99.31%**
144. **`packages/components/src/button/index.native.js`** -> AI Confidence: **99.31%**
145. **`packages/components/src/color-palette/index.native.js`** -> AI Confidence: **99.31%**
146. **`packages/components/src/mobile/bottom-sheet/cell.native.js`** -> AI Confidence: **99.31%**
147. **`packages/components/src/mobile/bottom-sheet/range-cell.native.js`** -> AI Confidence: **99.31%**
148. **`packages/components/src/mobile/bottom-sheet/range-text-input.native.js`** -> AI Confidence: **99.31%**
149. **`packages/components/src/mobile/bottom-sheet/stepper-cell/index.native.js`** -> AI Confidence: **99.31%**
150. **`packages/components/src/mobile/color-settings/palette.screen.native.js`** -> AI Confidence: **99.31%**
151. **`packages/components/src/mobile/gradient/index.native.js`** -> AI Confidence: **99.31%**
152. **`packages/components/src/unit-control/index.native.js`** -> AI Confidence: **99.31%**
153. **`packages/compose/src/index.js`** -> AI Confidence: **99.31%**
154. **`packages/compose/src/index.native.js`** -> AI Confidence: **99.31%**
155. **`packages/core-commands/src/site-editor-navigation-commands.js`** -> AI Confidence: **99.31%**
156. **`packages/core-data/src/utils/index.js`** -> AI Confidence: **99.31%**
157. **`packages/dom/src/dom/index.js`** -> AI Confidence: **99.31%**
158. **`packages/dom/src/dom/is-edge.js`** -> AI Confidence: **99.31%**
159. **`packages/edit-post/src/components/back-button/fullscreen-mode-close.js`** -> AI Confidence: **99.31%**
160. **`packages/edit-post/src/components/layout/index.js`** -> AI Confidence: **99.31%**
161. **`packages/edit-site/src/components/add-new-post/index.js`** -> AI Confidence: **99.31%**
162. **`packages/edit-site/src/components/add-new-template-legacy/add-custom-template-modal-content.js`** -> AI Confidence: **99.31%**
163. **`packages/edit-site/src/components/add-new-template/add-custom-template-modal-content.js`** -> AI Confidence: **99.31%**
164. **`packages/edit-site/src/components/editor/index.js`** -> AI Confidence: **99.31%**
165. **`packages/edit-site/src/components/layout/index.js`** -> AI Confidence: **99.31%**
166. **`packages/edit-site/src/components/page-templates/index.js`** -> AI Confidence: **99.31%**
167. **`packages/edit-site/src/components/post-list/index.js`** -> AI Confidence: **99.31%**
168. **`packages/edit-site/src/components/post-list/quick-edit-modal.js`** -> AI Confidence: **99.31%**
169. **`packages/edit-site/src/components/save-button/index.js`** -> AI Confidence: **99.31%**
170. **`packages/edit-site/src/components/sidebar-navigation-item/index.js`** -> AI Confidence: **99.31%**
171. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menu/use-navigation-menu-handlers.js`** -> AI Confidence: **99.31%**
172. **`packages/edit-site/src/components/site-hub/index.js`** -> AI Confidence: **99.31%**
173. **`packages/editor/src/components/collab-sidebar/comment-author-info.js`** -> AI Confidence: **99.31%**
174. **`packages/editor/src/components/collab-sidebar/comment-form.js`** -> AI Confidence: **99.31%**
175. **`packages/editor/src/components/collab-sidebar/comments.js`** -> AI Confidence: **99.31%**
176. **`packages/editor/src/components/document-bar/index.js`** -> AI Confidence: **99.31%**
177. **`packages/editor/src/components/editor/index.js`** -> AI Confidence: **99.31%**
178. **`packages/editor/src/components/entities-saved-states/index.js`** -> AI Confidence: **99.31%**
179. **`packages/editor/src/components/header/index.js`** -> AI Confidence: **99.31%**
180. **`packages/editor/src/components/index.js`** -> AI Confidence: **99.31%**
181. **`packages/editor/src/components/index.native.js`** -> AI Confidence: **99.31%**
182. **`packages/editor/src/components/offline-status/index.native.js`** -> AI Confidence: **99.31%**
183. **`packages/editor/src/components/post-card-panel/index.js`** -> AI Confidence: **99.31%**
184. **`packages/editor/src/components/post-featured-image/index.js`** -> AI Confidence: **99.31%**
185. **`packages/editor/src/components/post-locked-modal/index.js`** -> AI Confidence: **99.31%**
186. **`packages/editor/src/components/post-publish-panel/index.js`** -> AI Confidence: **99.31%**
187. **`packages/editor/src/components/post-publish-panel/maybe-category-panel.js`** -> AI Confidence: **99.31%**
188. **`packages/editor/src/components/post-publish-panel/maybe-tags-panel.js`** -> AI Confidence: **99.31%**
189. **`packages/editor/src/components/post-revisions-preview/block-diff.js`** -> AI Confidence: **99.31%**
190. **`packages/editor/src/components/post-saved-state/index.js`** -> AI Confidence: **99.31%**
191. **`packages/editor/src/components/post-taxonomies/flat-term-selector.js`** -> AI Confidence: **99.31%**
192. **`packages/editor/src/components/post-template/classic-theme.js`** -> AI Confidence: **99.31%**
193. **`packages/editor/src/components/post-url/index.js`** -> AI Confidence: **99.31%**
194. **`packages/editor/src/components/provider/use-block-editor-settings.js`** -> AI Confidence: **99.31%**
195. **`packages/editor/src/components/provider/use-revision-blocks.js`** -> AI Confidence: **99.31%**
196. **`packages/editor/src/components/visual-editor/index.js`** -> AI Confidence: **99.31%**
197. **`packages/editor/src/hooks/pattern-overrides.js`** -> AI Confidence: **99.31%**
198. **`packages/editor/src/store/private-actions.js`** -> AI Confidence: **99.31%**
199. **`packages/format-library/src/link/index.js`** -> AI Confidence: **99.31%**
200. **`packages/format-library/src/link/modal-screens/link-settings-screen.native.js`** -> AI Confidence: **99.31%**
201. **`packages/format-library/src/text-color/index.native.js`** -> AI Confidence: **99.31%**
202. **`packages/global-styles-ui/src/font-library/lib/unbrotli.js`** -> AI Confidence: **99.31%**
203. **`packages/interface/src/components/complementary-area/index.js`** -> AI Confidence: **99.31%**
204. **`packages/patterns/src/components/pattern-convert-button.js`** -> AI Confidence: **99.31%**
205. **`packages/patterns/src/components/rename-pattern-category-modal.js`** -> AI Confidence: **99.31%**
206. **`packages/patterns/src/components/rename-pattern-modal.js`** -> AI Confidence: **99.31%**
207. **`packages/rich-text/src/create.js`** -> AI Confidence: **99.31%**
208. **`packages/scripts/config/jest-environment-puppeteer/config.js`** -> AI Confidence: **99.31%**
209. **`packages/scripts/scripts/format.js`** -> AI Confidence: **99.31%**
210. **`packages/widgets/src/blocks/legacy-widget/edit/index.js`** -> AI Confidence: **99.31%**
211. **`packages/workflow/src/components/workflow-menu.js`** -> AI Confidence: **99.31%**
212. **`platform-docs/src/components/HomepageBlocks/index.js`** -> AI Confidence: **99.31%**
213. **`platform-docs/src/components/HomepageFeatures/index.js`** -> AI Confidence: **99.31%**
214. **`storybook/package-styles/config.js`** -> AI Confidence: **99.31%**
215. **`packages/block-library/src/archives/index.php`** -> AI Confidence: **99.31%**
216. **`packages/block-library/src/latest-comments/index.php`** -> AI Confidence: **99.31%**
217. **`packages/style-engine/src/style-engine.php`** -> AI Confidence: **99.31%**
218. **`packages/boot/src/components/root/index.tsx`** -> AI Confidence: **99.31%**
219. **`packages/components/src/autocomplete/index.tsx`** -> AI Confidence: **99.31%**
220. **`packages/components/src/border-control/border-control/hook.ts`** -> AI Confidence: **99.31%**
221. **`packages/components/src/box-control/index.tsx`** -> AI Confidence: **99.31%**
222. **`packages/components/src/box-control/input-control.tsx`** -> AI Confidence: **99.31%**
223. **`packages/components/src/calendar/date-range-calendar/index.tsx`** -> AI Confidence: **99.31%**
224. **`packages/components/src/custom-gradient-picker/gradient-bar/index.tsx`** -> AI Confidence: **99.31%**
225. **`packages/components/src/date-time/date/index.tsx`** -> AI Confidence: **99.31%**
226. **`packages/components/src/drop-zone/index.tsx`** -> AI Confidence: **99.31%**
227. **`packages/components/src/dropdown/index.tsx`** -> AI Confidence: **99.31%**
228. **`packages/components/src/form-token-field/index.tsx`** -> AI Confidence: **99.31%**
229. **`packages/components/src/input-control/input-base.tsx`** -> AI Confidence: **99.31%**
230. **`packages/components/src/modal/index.tsx`** -> AI Confidence: **99.31%**
231. **`packages/components/src/navigation/item/index.tsx`** -> AI Confidence: **99.31%**
232. **`packages/components/src/notice/index.tsx`** -> AI Confidence: **99.31%**
233. **`packages/components/src/number-control/index.tsx`** -> AI Confidence: **99.31%**
234. **`packages/components/src/palette-edit/index.tsx`** -> AI Confidence: **99.31%**
235. **`packages/components/src/query-controls/index.tsx`** -> AI Confidence: **99.31%**
236. **`packages/components/src/range-control/index.tsx`** -> AI Confidence: **99.31%**
237. **`packages/components/src/tabs/tablist.tsx`** -> AI Confidence: **99.31%**
238. **`packages/components/src/tools-panel/tools-panel-item/hook.ts`** -> AI Confidence: **99.31%**
239. **`packages/components/src/tooltip/index.tsx`** -> AI Confidence: **99.31%**
240. **`packages/components/src/tree-grid/index.tsx`** -> AI Confidence: **99.31%**
241. **`packages/components/src/truncate/hook.ts`** -> AI Confidence: **99.31%**
242. **`packages/components/src/unit-control/index.tsx`** -> AI Confidence: **99.31%**
243. **`packages/core-data/src/selectors.ts`** -> AI Confidence: **99.31%**
244. **`packages/core-data/src/utils/crdt-user-selections.ts`** -> AI Confidence: **99.31%**
245. **`packages/core-data/src/utils/crdt.ts`** -> AI Confidence: **99.31%**
246. **`packages/dataviews/src/components/dataform-controls/date.tsx`** -> AI Confidence: **99.31%**
247. **`packages/dataviews/src/components/dataform-controls/datetime.tsx`** -> AI Confidence: **99.31%**
248. **`packages/dataviews/src/components/dataform-layouts/panel/summary-button.tsx`** -> AI Confidence: **99.31%**
249. **`packages/dataviews/src/components/dataviews-filters/filter.tsx`** -> AI Confidence: **99.31%**
250. **`packages/dataviews/src/components/dataviews-footer/index.tsx`** -> AI Confidence: **99.31%**
251. **`packages/dataviews/src/components/dataviews-layouts/activity/index.tsx`** -> AI Confidence: **99.31%**
252. **`packages/dataviews/src/components/dataviews-layouts/grid/composite-grid.tsx`** -> AI Confidence: **99.31%**
253. **`packages/dataviews/src/components/dataviews-layouts/grid/index.tsx`** -> AI Confidence: **99.31%**
254. **`packages/dataviews/src/components/dataviews-layouts/list/index.tsx`** -> AI Confidence: **99.31%**
255. **`packages/dataviews/src/components/dataviews-layouts/picker-grid/index.tsx`** -> AI Confidence: **99.31%**
256. **`packages/dataviews/src/components/dataviews-layouts/picker-table/index.tsx`** -> AI Confidence: **99.31%**
257. **`packages/dataviews/src/components/dataviews-layouts/table/index.tsx`** -> AI Confidence: **99.31%**
258. **`packages/dataviews/src/dataform/stories/validation.tsx`** -> AI Confidence: **99.31%**
259. **`packages/dataviews/src/field-types/index.tsx`** -> AI Confidence: **99.31%**
260. **`packages/editor/src/components/collaborators-presence/avatar/component.tsx`** -> AI Confidence: **99.31%**
261. **`packages/editor/src/components/collaborators-presence/use-collaborator-notifications.ts`** -> AI Confidence: **99.31%**
262. **`packages/editor/src/components/sync-connection-error-modal/index.tsx`** -> AI Confidence: **99.31%**
263. **`packages/editor/src/dataviews/store/private-actions.ts`** -> AI Confidence: **99.31%**
264. **`packages/fields/src/actions/index.ts`** -> AI Confidence: **99.31%**
265. **`packages/fields/src/actions/permanently-delete-post.tsx`** -> AI Confidence: **99.31%**
266. **`packages/fields/src/actions/rename-post.tsx`** -> AI Confidence: **99.31%**
267. **`packages/fields/src/actions/restore-post.tsx`** -> AI Confidence: **99.31%**
268. **`packages/fields/src/actions/trash-post.tsx`** -> AI Confidence: **99.31%**
269. **`packages/fields/src/components/media-edit/index.tsx`** -> AI Confidence: **99.31%**
270. **`packages/fields/src/fields/author/author-view.tsx`** -> AI Confidence: **99.31%**
271. **`packages/fields/src/fields/index.ts`** -> AI Confidence: **99.31%**
272. **`packages/global-styles-engine/src/core/render.tsx`** -> AI Confidence: **99.31%**
273. **`packages/global-styles-ui/src/color-palette-panel.tsx`** -> AI Confidence: **99.31%**
274. **`packages/global-styles-ui/src/font-families.tsx`** -> AI Confidence: **99.31%**
275. **`packages/global-styles-ui/src/font-library/context.tsx`** -> AI Confidence: **99.31%**
276. **`packages/global-styles-ui/src/font-library/installed-fonts.tsx`** -> AI Confidence: **99.31%**
277. **`packages/global-styles-ui/src/font-library/utils/index.ts`** -> AI Confidence: **99.31%**
278. **`packages/global-styles-ui/src/font-sizes/font-size.tsx`** -> AI Confidence: **99.31%**
279. **`packages/global-styles-ui/src/font-sizes/font-sizes.tsx`** -> AI Confidence: **99.31%**
280. **`packages/global-styles-ui/src/screen-block.tsx`** -> AI Confidence: **99.31%**
281. **`packages/global-styles-ui/src/style-variations-container.tsx`** -> AI Confidence: **99.31%**
282. **`packages/interactivity/src/directives.tsx`** -> AI Confidence: **99.31%**
283. **`packages/media-utils/src/components/media-upload-modal/index.tsx`** -> AI Confidence: **99.31%**
284. **`packages/media-utils/src/utils/upload-media.ts`** -> AI Confidence: **99.31%**
285. **`packages/theme/bin/terrazzo-plugin-ds-token-fallbacks/index.ts`** -> AI Confidence: **99.31%**
286. **`packages/theme/src/color-ramps/lib/index.ts`** -> AI Confidence: **99.31%**
287. **`routes/connectors-home/default-connectors.tsx`** -> AI Confidence: **99.31%**
288. **`routes/pattern-list/use-patterns.ts`** -> AI Confidence: **99.31%**
289. **`bin/validate-package-lock.js`** -> AI Confidence: **99.29%**
290. **`packages/babel-preset-default/polyfill-exclusions.js`** -> AI Confidence: **99.29%**
291. **`packages/babel-preset-default/replace-polyfills.js`** -> AI Confidence: **99.29%**
292. **`packages/block-editor/src/utils/format-font-weight.js`** -> AI Confidence: **99.29%**
293. **`packages/block-library/src/accordion-heading/deprecated.js`** -> AI Confidence: **99.29%**
294. **`packages/block-library/src/gallery/shared.js`** -> AI Confidence: **99.29%**
295. **`packages/block-library/src/playlist/utils.js`** -> AI Confidence: **99.29%**
296. **`packages/block-library/src/post-date/variations.js`** -> AI Confidence: **99.29%**
297. **`packages/blocks/src/api/parser/convert-legacy-block.js`** -> AI Confidence: **99.29%**
298. **`packages/blocks/src/api/raw-handling/normalise-blocks.js`** -> AI Confidence: **99.29%**
299. **`packages/create-block-interactive-template/index.js`** -> AI Confidence: **99.29%**
300. **`packages/docgen/bin/cli.js`** -> AI Confidence: **99.29%**
301. **`packages/e2e-tests/plugins/interactive-blocks/tovdom/processing-instructions.js`** -> AI Confidence: **99.29%**
302. **`packages/eslint-plugin/rules/__tests__/wp-global-usage.js`** -> AI Confidence: **99.29%**
303. **`packages/eslint-plugin/rules/no-i18n-in-save.js`** -> AI Confidence: **99.29%**
304. **`packages/eslint-plugin/utils/constants.js`** -> AI Confidence: **99.29%**
305. **`packages/jest-preset-default/jest-preset.js`** -> AI Confidence: **99.29%**
306. **`packages/preferences-persistence/src/migrations/legacy-local-storage-data/move-feature-preferences.js`** -> AI Confidence: **99.29%**
307. **`packages/preferences-persistence/src/migrations/legacy-local-storage-data/move-individual-preference.js`** -> AI Confidence: **99.29%**
308. **`packages/react-native-bridge/common/gutenberg-web-single-block/insert-block.js`** -> AI Confidence: **99.29%**
309. **`packages/react-native-editor/jest_ui.config.js`** -> AI Confidence: **99.29%**
310. **`packages/scripts/config/babel-transform.js`** -> AI Confidence: **99.29%**
311. **`packages/scripts/config/jest-e2e.config.js`** -> AI Confidence: **99.29%**
312. **`packages/scripts/config/jest-unit.config.js`** -> AI Confidence: **99.29%**
313. **`packages/scripts/config/playwright.config.js`** -> AI Confidence: **99.29%**
314. **`packages/scripts/config/puppeteer.config.js`** -> AI Confidence: **99.29%**
315. **`packages/scripts/scripts/check-licenses.js`** -> AI Confidence: **99.29%**
316. **`packages/scripts/scripts/test-e2e.js`** -> AI Confidence: **99.29%**
317. **`packages/stylelint-config/scss.js`** -> AI Confidence: **99.29%**
318. **`react-scanner.config.js`** -> AI Confidence: **99.29%**
319. **`test/native/jest.config.js`** -> AI Confidence: **99.29%**
320. **`bin/unit-test-date.sh`** -> AI Confidence: **99.29%**
321. **`packages/react-native-editor/bin/test-e2e.sh`** -> AI Confidence: **99.29%**
322. **`packages/block-library/src/breadcrumbs/index.php`** -> AI Confidence: **99.29%**
323. **`packages/block-library/src/cover/index.php`** -> AI Confidence: **99.29%**
324. **`packages/block-library/src/icon/index.php`** -> AI Confidence: **99.29%**
325. **`packages/block-library/src/query-title/index.php`** -> AI Confidence: **99.29%**
326. **`packages/block-library/src/query-total/index.php`** -> AI Confidence: **99.29%**
327. **`packages/block-library/src/term-count/index.php`** -> AI Confidence: **99.29%**
328. **`packages/e2e-tests/mu-plugins/disable-login-autofocus.php`** -> AI Confidence: **99.29%**
329. **`packages/e2e-tests/mu-plugins/disable-remote-patterns.php`** -> AI Confidence: **99.29%**
330. **`packages/e2e-tests/plugins/disable-client-side-media-processing.php`** -> AI Confidence: **99.29%**
331. **`packages/e2e-tests/plugins/interactive-blocks/directive-bind/render.php`** -> AI Confidence: **99.29%**
332. **`packages/e2e-tests/plugins/interactive-blocks/directive-each/render.php`** -> AI Confidence: **99.29%**
333. **`packages/e2e-tests/plugins/interactive-blocks/directive-init/render.php`** -> AI Confidence: **99.29%**
334. **`packages/e2e-tests/plugins/interactive-blocks/directive-key/render.php`** -> AI Confidence: **99.29%**
335. **`packages/e2e-tests/plugins/interactive-blocks/directive-on-document/render.php`** -> AI Confidence: **99.29%**
336. **`packages/e2e-tests/plugins/interactive-blocks/directive-on-window/render.php`** -> AI Confidence: **99.29%**
337. **`packages/e2e-tests/plugins/interactive-blocks/directive-on/render.php`** -> AI Confidence: **99.29%**
338. **`packages/e2e-tests/plugins/interactive-blocks/directive-text/render.php`** -> AI Confidence: **99.29%**
339. **`packages/e2e-tests/plugins/interactive-blocks/directive-watch/render.php`** -> AI Confidence: **99.29%**
340. **`packages/e2e-tests/plugins/interactive-blocks/generator-scope/render.php`** -> AI Confidence: **99.29%**
341. **`packages/e2e-tests/plugins/interactive-blocks/get-server-context/render.php`** -> AI Confidence: **99.29%**
342. **`packages/e2e-tests/plugins/interactive-blocks/get-server-state/render.php`** -> AI Confidence: **99.29%**
343. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing-async/render.php`** -> AI Confidence: **99.29%**
344. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing-slow/render.php`** -> AI Confidence: **99.29%**
345. **`packages/e2e-tests/plugins/interactive-blocks/hydration-timing/render.php`** -> AI Confidence: **99.29%**
346. **`packages/e2e-tests/plugins/interactive-blocks/negation-operator/render.php`** -> AI Confidence: **99.29%**
347. **`packages/e2e-tests/plugins/interactive-blocks/router-race-condition/render.php`** -> AI Confidence: **99.29%**
348. **`packages/e2e-tests/plugins/interactive-blocks/router-regions/render.php`** -> AI Confidence: **99.29%**
349. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-alpha/render.php`** -> AI Confidence: **99.29%**
350. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-bravo/render.php`** -> AI Confidence: **99.29%**
351. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-charlie/render.php`** -> AI Confidence: **99.29%**
352. **`packages/e2e-tests/plugins/interactive-blocks/router-script-modules-wrapper/render.php`** -> AI Confidence: **99.29%**
353. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-blue/render.php`** -> AI Confidence: **99.29%**
354. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-green/render.php`** -> AI Confidence: **99.29%**
355. **`packages/e2e-tests/plugins/interactive-blocks/router-styles-red/render.php`** -> AI Confidence: **99.29%**
356. **`packages/e2e-tests/plugins/interactive-blocks/store-tag/render.php`** -> AI Confidence: **99.29%**
357. **`packages/e2e-tests/plugins/interactive-blocks/store/render.php`** -> AI Confidence: **99.29%**
358. **`packages/e2e-tests/plugins/interactive-blocks/tovdom/render.php`** -> AI Confidence: **99.29%**
359. **`packages/e2e-tests/plugins/interactive-blocks/with-scope/render.php`** -> AI Confidence: **99.29%**
360. **`packages/e2e-tests/plugins/query-block.php`** -> AI Confidence: **99.29%**
361. **`packages/icons/src/manifest.php`** -> AI Confidence: **99.29%**
362. **`packages/dataviews/src/components/dataform-controls/utils/get-custom-validity.ts`** -> AI Confidence: **99.29%**
363. **`packages/dataviews/src/field-types/utils/get-is-valid.ts`** -> AI Confidence: **99.29%**
364. **`packages/editor/src/components/collaborators-overlay/get-avatar-url.ts`** -> AI Confidence: **99.29%**
365. **`packages/interactivity-router/src/assets/dynamic-importmap/resolver.ts`** -> AI Confidence: **99.29%**
366. **`packages/report-flaky-tests/src/strip-ansi.ts`** -> AI Confidence: **99.29%**
367. **`packages/react-native-bridge/android/settings.gradle`** -> AI Confidence: **99.29%**
368. **`packages/react-native-editor/ios/Podfile`** -> AI Confidence: **99.29%**
369. **`bin/api-docs/gen-components-docs/index.mjs`** -> AI Confidence: **99.24%**
370. **`bin/plugin/commands/packages.js`** -> AI Confidence: **99.24%**
371. **`packages/block-directory/src/components/downloadable-block-list-item/index.js`** -> AI Confidence: **99.24%**
372. **`packages/block-editor/src/components/audio-player/index.native.js`** -> AI Confidence: **99.24%**
373. **`packages/block-editor/src/components/block-list/index.js`** -> AI Confidence: **99.24%**
374. **`packages/block-editor/src/components/block-mover/button.js`** -> AI Confidence: **99.24%**
375. **`packages/block-editor/src/components/block-switcher/block-transformations-menu.js`** -> AI Confidence: **99.24%**
376. **`packages/block-editor/src/components/block-tools/insertion-point.js`** -> AI Confidence: **99.24%**
377. **`packages/block-editor/src/components/block-tools/use-block-toolbar-popover-props.js`** -> AI Confidence: **99.24%**
378. **`packages/block-editor/src/components/block-variation-transforms/index.js`** -> AI Confidence: **99.24%**
379. **`packages/block-editor/src/components/floating-toolbar/index.native.js`** -> AI Confidence: **99.24%**
380. **`packages/block-editor/src/components/iframe/index.js`** -> AI Confidence: **99.24%**
381. **`packages/block-editor/src/components/image-editor/use-save-image.js`** -> AI Confidence: **99.24%**
382. **`packages/block-editor/src/components/index.js`** -> AI Confidence: **99.24%**
383. **`packages/block-editor/src/components/index.native.js`** -> AI Confidence: **99.24%**
384. **`packages/block-editor/src/components/inserter/menu.js`** -> AI Confidence: **99.24%**
385. **`packages/block-editor/src/components/inserter/menu.native.js`** -> AI Confidence: **99.24%**
386. **`packages/block-editor/src/components/inspector-controls-tabs/index.js`** -> AI Confidence: **99.24%**
387. **`packages/block-editor/src/components/inspector-controls/slot.js`** -> AI Confidence: **99.24%**
388. **`packages/block-editor/src/components/link-control/search-results.js`** -> AI Confidence: **99.24%**
389. **`packages/block-editor/src/components/list-view/block-select-button.js`** -> AI Confidence: **99.24%**
390. **`packages/block-editor/src/components/list-view/index.js`** -> AI Confidence: **99.24%**
391. **`packages/block-editor/src/components/rich-text/index.js`** -> AI Confidence: **99.24%**
392. **`packages/block-editor/src/hooks/block-fields/index.js`** -> AI Confidence: **99.24%**
393. **`packages/block-editor/src/hooks/custom-css.js`** -> AI Confidence: **99.24%**
394. **`packages/block-editor/src/hooks/fit-text.js`** -> AI Confidence: **99.24%**
395. **`packages/block-editor/src/hooks/style.js`** -> AI Confidence: **99.24%**
396. **`packages/block-editor/src/hooks/typography.js`** -> AI Confidence: **99.24%**
397. **`packages/block-editor/src/hooks/utils.js`** -> AI Confidence: **99.24%**
398. **`packages/block-editor/src/store/actions.js`** -> AI Confidence: **99.24%**
399. **`packages/block-library/src/block/edit-title.native.js`** -> AI Confidence: **99.24%**
400. **`packages/block-library/src/block/edit.js`** -> AI Confidence: **99.24%**
401. **`packages/block-library/src/comment-author-name/edit.js`** -> AI Confidence: **99.24%**
402. **`packages/block-library/src/cover/edit/block-controls.js`** -> AI Confidence: **99.24%**
403. **`packages/block-library/src/cover/edit/index.js`** -> AI Confidence: **99.24%**
404. **`packages/block-library/src/file/edit.js`** -> AI Confidence: **99.24%**
405. **`packages/block-library/src/html/modal.js`** -> AI Confidence: **99.24%**
406. **`packages/block-library/src/icon/edit.js`** -> AI Confidence: **99.24%**
407. **`packages/block-library/src/image/image.js`** -> AI Confidence: **99.24%**
408. **`packages/block-library/src/list-item/edit.native.js`** -> AI Confidence: **99.24%**
409. **`packages/block-library/src/media-text/media-container.js`** -> AI Confidence: **99.24%**
410. **`packages/block-library/src/navigation-link/link-ui/index.js`** -> AI Confidence: **99.24%**
411. **`packages/block-library/src/navigation-link/link-ui/page-creator.js`** -> AI Confidence: **99.24%**
412. **`packages/block-library/src/navigation-link/shared/controls.js`** -> AI Confidence: **99.24%**
413. **`packages/block-library/src/navigation-submenu/edit.js`** -> AI Confidence: **99.24%**
414. **`packages/block-library/src/navigation/edit/overlay-template-part-selector.js`** -> AI Confidence: **99.24%**
415. **`packages/block-library/src/navigation/edit/placeholder/index.js`** -> AI Confidence: **99.24%**
416. **`packages/block-library/src/paragraph/index.js`** -> AI Confidence: **99.24%**
417. **`packages/block-library/src/post-date/edit.js`** -> AI Confidence: **99.24%**
418. **`packages/block-library/src/social-link/edit.native.js`** -> AI Confidence: **99.24%**
419. **`packages/block-library/src/table/edit.js`** -> AI Confidence: **99.24%**
420. **`packages/block-library/src/video/edit.native.js`** -> AI Confidence: **99.24%**
421. **`packages/commands/src/components/command-menu.js`** -> AI Confidence: **99.24%**
422. **`packages/components/src/custom-gradient-picker/index.native.js`** -> AI Confidence: **99.24%**
423. **`packages/components/src/index.native.js`** -> AI Confidence: **99.24%**
424. **`packages/core-data/src/resolvers.js`** -> AI Confidence: **99.24%**
425. **`packages/edit-post/src/components/layout/index.native.js`** -> AI Confidence: **99.24%**
426. **`packages/edit-site/src/components/add-new-pattern/index.js`** -> AI Confidence: **99.24%**
427. **`packages/edit-site/src/components/add-new-template/utils.js`** -> AI Confidence: **99.24%**
428. **`packages/edit-site/src/components/page-patterns/fields.js`** -> AI Confidence: **99.24%**
429. **`packages/edit-site/src/components/page-patterns/index.js`** -> AI Confidence: **99.24%**
430. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menu/index.js`** -> AI Confidence: **99.24%**
431. **`packages/edit-site/src/components/sidebar-navigation-screen/index.js`** -> AI Confidence: **99.24%**
432. **`packages/edit-site/src/components/site-editor-routes/pages.js`** -> AI Confidence: **99.24%**
433. **`packages/edit-site/src/components/site-editor-routes/templates.js`** -> AI Confidence: **99.24%**
434. **`packages/edit-widgets/src/components/layout/interface.js`** -> AI Confidence: **99.24%**
435. **`packages/edit-widgets/src/components/sidebar/index.js`** -> AI Confidence: **99.24%**
436. **`packages/editor/src/components/collab-sidebar/index.js`** -> AI Confidence: **99.24%**
437. **`packages/editor/src/components/commands/index.js`** -> AI Confidence: **99.24%**
438. **`packages/editor/src/components/editor-interface/index.js`** -> AI Confidence: **99.24%**
439. **`packages/editor/src/components/global-styles-sidebar/index.js`** -> AI Confidence: **99.24%**
440. **`packages/editor/src/components/post-publish-panel/postpublish.js`** -> AI Confidence: **99.24%**
441. **`packages/editor/src/components/post-publish-panel/prepublish.js`** -> AI Confidence: **99.24%**
442. **`packages/editor/src/components/post-taxonomies/hierarchical-term-selector.js`** -> AI Confidence: **99.24%**
443. **`packages/editor/src/components/post-title/index.native.js`** -> AI Confidence: **99.24%**
444. **`packages/editor/src/components/provider/index.native.js`** -> AI Confidence: **99.24%**
445. **`packages/editor/src/components/sidebar/dataform-post-summary.js`** -> AI Confidence: **99.24%**
446. **`packages/editor/src/components/style-book/index.js`** -> AI Confidence: **99.24%**
447. **`packages/editor/src/components/template-actions-panel/classic-theme-content.js`** -> AI Confidence: **99.24%**
448. **`packages/patterns/src/components/patterns-manage-button.js`** -> AI Confidence: **99.24%**
449. **`packages/reusable-blocks/src/components/reusable-blocks-menu-items/reusable-block-convert-button.js`** -> AI Confidence: **99.24%**
450. **`packages/rich-text/src/hook/index.js`** -> AI Confidence: **99.24%**
451. **`packages/boot/src/components/root/single-page.tsx`** -> AI Confidence: **99.24%**
452. **`packages/boot/src/components/site-hub/index.tsx`** -> AI Confidence: **99.24%**
453. **`packages/components/src/calendar/test/date-calendar.tsx`** -> AI Confidence: **99.24%**
454. **`packages/components/src/combobox-control/index.tsx`** -> AI Confidence: **99.24%**
455. **`packages/components/src/custom-select-control-v2/styles.ts`** -> AI Confidence: **99.24%**
456. **`packages/components/src/duotone-picker/duotone-picker.tsx`** -> AI Confidence: **99.24%**
457. **`packages/components/src/index.ts`** -> AI Confidence: **99.24%**
458. **`packages/components/src/navigator/navigator/component.tsx`** -> AI Confidence: **99.24%**
459. **`packages/components/src/select-control/styles/select-control-styles.ts`** -> AI Confidence: **99.24%**
460. **`packages/components/src/tab-panel/index.tsx`** -> AI Confidence: **99.24%**
461. **`packages/components/src/text/hook.ts`** -> AI Confidence: **99.24%**
462. **`packages/core-data/src/utils/crdt-selection.ts`** -> AI Confidence: **99.24%**
463. **`packages/dataviews/src/components/dataform-layouts/card/index.tsx`** -> AI Confidence: **99.24%**
464. **`packages/dataviews/src/components/dataform-layouts/details/index.tsx`** -> AI Confidence: **99.24%**
465. **`packages/dataviews/src/components/dataviews-layouts/activity/activity-item.tsx`** -> AI Confidence: **99.24%**
466. **`packages/dataviews/src/components/dataviews-view-config/index.tsx`** -> AI Confidence: **99.24%**
467. **`packages/dataviews/src/components/dataviews-view-config/properties-section.tsx`** -> AI Confidence: **99.24%**
468. **`packages/dataviews/src/field-types/color.tsx`** -> AI Confidence: **99.24%**
469. **`packages/dataviews/src/field-types/number.tsx`** -> AI Confidence: **99.24%**
470. **`packages/editor/src/components/collaborators-overlay/overlay.tsx`** -> AI Confidence: **99.24%**
471. **`packages/editor/src/components/collaborators-overlay/use-render-cursors.ts`** -> AI Confidence: **99.24%**
472. **`packages/fields/src/actions/reset-post.tsx`** -> AI Confidence: **99.24%**
473. **`packages/fields/src/components/create-template-part-modal/index.tsx`** -> AI Confidence: **99.24%**
474. **`packages/global-styles-ui/src/font-library/font-collection.tsx`** -> AI Confidence: **99.24%**
475. **`packages/global-styles-ui/src/shadows-panel.tsx`** -> AI Confidence: **99.24%**
476. **`packages/global-styles-ui/src/variations/variation.tsx`** -> AI Confidence: **99.24%**
477. **`packages/lazy-editor/src/components/editor/index.tsx`** -> AI Confidence: **99.24%**
478. **`packages/lazy-editor/src/components/preview/index.tsx`** -> AI Confidence: **99.24%**
479. **`packages/media-fields/src/index.ts`** -> AI Confidence: **99.24%**
480. **`packages/theme/src/use-theme-provider-styles.ts`** -> AI Confidence: **99.24%**
481. **`packages/upload-media/src/store/actions.ts`** -> AI Confidence: **99.24%**
482. **`packages/upload-media/src/store/private-actions.ts`** -> AI Confidence: **99.24%**
483. **`packages/wordcount/src/index.ts`** -> AI Confidence: **99.24%**
484. **`routes/content-guidelines/components/block-guideline-modal.tsx`** -> AI Confidence: **99.24%**
485. **`routes/content-guidelines/components/revision-history.tsx`** -> AI Confidence: **99.24%**
486. **`routes/post-list/quick-edit-modal.tsx`** -> AI Confidence: **99.24%**
487. **`routes/post-list/stage.tsx`** -> AI Confidence: **99.24%**
488. **`routes/template-list/stage-activation.tsx`** -> AI Confidence: **99.24%**
489. **`routes/template-list/stage-legacy.tsx`** -> AI Confidence: **99.24%**
490. **`packages/react-native-editor/android/app/src/main/java/com/gutenberg/MainActivity.kt`** -> AI Confidence: **99.24%**
491. **`bin/plugin/lib/utils.js`** -> AI Confidence: **99.23%**
492. **`packages/block-editor/src/components/block-bindings/source-fields-list.js`** -> AI Confidence: **99.23%**
493. **`packages/block-editor/src/components/block-toolbar/change-design.js`** -> AI Confidence: **99.23%**
494. **`packages/block-editor/src/components/default-block-appender/index.js`** -> AI Confidence: **99.23%**
495. **`packages/block-editor/src/components/editor-styles/index.js`** -> AI Confidence: **99.23%**
496. **`packages/block-editor/src/components/global-styles/hooks.js`** -> AI Confidence: **99.23%**
497. **`packages/block-editor/src/components/inspector-controls-tabs/position-controls-panel.js`** -> AI Confidence: **99.23%**
498. **`packages/block-editor/src/components/link-control/search-input.js`** -> AI Confidence: **99.23%**
499. **`packages/block-editor/src/components/link-control/search-item.js`** -> AI Confidence: **99.23%**
500. **`packages/block-editor/src/components/list-view/use-list-view-drop-zone.js`** -> AI Confidence: **99.23%**
501. **`packages/block-editor/src/components/spacing-sizes-control/input-controls/spacing-input-control.js`** -> AI Confidence: **99.23%**
502. **`packages/block-editor/src/components/url-popover/index.js`** -> AI Confidence: **99.23%**
503. **`packages/block-editor/src/components/use-block-commands/index.js`** -> AI Confidence: **99.23%**
504. **`packages/block-editor/src/components/use-block-display-information/index.js`** -> AI Confidence: **99.23%**
505. **`packages/block-editor/src/components/use-paste-styles/index.js`** -> AI Confidence: **99.23%**
506. **`packages/block-editor/src/components/video-player/index.native.js`** -> AI Confidence: **99.23%**
507. **`packages/block-editor/src/hooks/font-size.js`** -> AI Confidence: **99.23%**
508. **`packages/block-editor/src/hooks/text-align.js`** -> AI Confidence: **99.23%**
509. **`packages/block-library/src/buttons/edit.native.js`** -> AI Confidence: **99.23%**
510. **`packages/block-library/src/comment-template/edit.js`** -> AI Confidence: **99.23%**
511. **`packages/block-library/src/embed/embed-placeholder.native.js`** -> AI Confidence: **99.23%**
512. **`packages/block-library/src/navigation/edit/overlay-panel.js`** -> AI Confidence: **99.23%**
513. **`packages/block-library/src/navigation/edit/unsaved-inner-blocks.js`** -> AI Confidence: **99.23%**
514. **`packages/block-library/src/page-list-item/edit.js`** -> AI Confidence: **99.23%**
515. **`packages/block-library/src/post-author-name/edit.js`** -> AI Confidence: **99.23%**
516. **`packages/block-library/src/post-comments-form/form.js`** -> AI Confidence: **99.23%**
517. **`packages/block-library/src/post-title/edit.js`** -> AI Confidence: **99.23%**
518. **`packages/block-library/src/site-title/edit.js`** -> AI Confidence: **99.23%**
519. **`packages/block-library/src/spacer/edit.native.js`** -> AI Confidence: **99.23%**
520. **`packages/block-library/src/tab/edit.js`** -> AI Confidence: **99.23%**
521. **`packages/block-library/src/template-part/edit/placeholder.js`** -> AI Confidence: **99.23%**
522. **`packages/blocks/src/api/parser/apply-block-deprecated-versions.js`** -> AI Confidence: **99.23%**
523. **`packages/blocks/src/store/process-block-type.js`** -> AI Confidence: **99.23%**
524. **`packages/components/src/font-size-picker/index.native.js`** -> AI Confidence: **99.23%**
525. **`packages/edit-site/src/components/more-menu/site-export.js`** -> AI Confidence: **99.23%**
526. **`packages/edit-site/src/components/page-patterns/use-patterns.js`** -> AI Confidence: **99.23%**
527. **`packages/edit-site/src/components/sidebar-navigation-screen-navigation-menus/leaf-more-menu.js`** -> AI Confidence: **99.23%**
528. **`packages/editor/src/components/global-styles/index.js`** -> AI Confidence: **99.23%**
529. **`packages/editor/src/components/global-styles/menu.js`** -> AI Confidence: **99.23%**
530. **`packages/editor/src/components/post-actions/set-as-homepage.js`** -> AI Confidence: **99.23%**
531. **`packages/editor/src/components/post-actions/set-as-posts-page.js`** -> AI Confidence: **99.23%**
532. **`packages/editor/src/components/post-publish-button/post-publish-button-or-toggle.js`** -> AI Confidence: **99.23%**
533. **`packages/editor/src/components/post-publish-panel/maybe-upload-media.js`** -> AI Confidence: **99.23%**
534. **`packages/editor/src/components/revision-fields-diff/index.js`** -> AI Confidence: **99.23%**
535. **`packages/editor/src/hooks/navigation-link-view-button.js`** -> AI Confidence: **99.23%**
536. **`storybook/preview.jsx`** -> AI Confidence: **99.23%**
537. **`packages/block-library/src/search/index.php`** -> AI Confidence: **99.23%**
538. **`packages/components/src/border-box-control/border-box-control/hook.ts`** -> AI Confidence: **99.23%**
539. **`packages/components/src/circular-option-picker/circular-option-picker-option.tsx`** -> AI Confidence: **99.23%**
540. **`packages/components/src/dropdown-menu/index.tsx`** -> AI Confidence: **99.23%**
541. **`packages/components/src/flex/flex/hook.ts`** -> AI Confidence: **99.23%**
542. **`packages/components/src/grid/hook.ts`** -> AI Confidence: **99.23%**
543. **`packages/components/src/guide/index.tsx`** -> AI Confidence: **99.23%**
544. **`packages/components/src/input-control/input-field.tsx`** -> AI Confidence: **99.23%**
545. **`packages/components/src/input-control/styles/input-control-styles.tsx`** -> AI Confidence: **99.23%**
546. **`packages/components/src/input-control/types.ts`** -> AI Confidence: **99.23%**
547. **`packages/components/src/menu-item/index.tsx`** -> AI Confidence: **99.23%**
548. **`packages/components/src/navigation/back-button/index.tsx`** -> AI Confidence: **99.23%**
549. **`packages/compose/src/hooks/use-dialog/index.ts`** -> AI Confidence: **99.23%**
550. **`packages/core-data/src/utils/crdt-blocks.ts`** -> AI Confidence: **99.23%**
551. **`packages/data/src/components/use-select/index.ts`** -> AI Confidence: **99.23%**
552. **`packages/dataviews/src/components/dataform-controls/utils/validated-number.tsx`** -> AI Confidence: **99.23%**
553. **`packages/dataviews/src/components/dataform-layouts/regular/index.tsx`** -> AI Confidence: **99.23%**
554. **`packages/dataviews/src/hooks/use-form-validity.ts`** -> AI Confidence: **99.23%**
555. **`packages/editor/src/dataviews/fields/content-preview/content-preview-view.tsx`** -> AI Confidence: **99.23%**
556. **`packages/fields/src/actions/duplicate-post.tsx`** -> AI Confidence: **99.23%**
557. **`packages/global-styles-ui/src/palette.tsx`** -> AI Confidence: **99.23%**
558. **`packages/global-styles-ui/src/screen-revisions/index.tsx`** -> AI Confidence: **99.23%**
559. **`packages/global-styles-ui/src/screen-revisions/revisions-buttons.tsx`** -> AI Confidence: **99.23%**
560. **`packages/global-styles-ui/src/typography-example.tsx`** -> AI Confidence: **99.23%**
561. **`packages/media-fields/src/attached_to/edit.tsx`** -> AI Confidence: **99.23%**
562. **`packages/media-fields/src/author/view.tsx`** -> AI Confidence: **99.23%**
563. **`packages/sync/src/manager.ts`** -> AI Confidence: **99.23%**
564. **`packages/theme/terrazzo.config.ts`** -> AI Confidence: **99.23%**
565. **`packages/ui/src/link/link.tsx`** -> AI Confidence: **99.23%**
566. **`packages/views/src/use-view.ts`** -> AI Confidence: **99.23%**
567. **`routes/content-guidelines/api.ts`** -> AI Confidence: **99.23%**
568. **`routes/template-list/add-new-template/add-custom-template-modal-content.tsx`** -> AI Confidence: **99.23%**
569. **`packages/react-native-aztec/android/src/main/kotlin/org/wordpress/mobile/ReactNativeAztec/EnterPressedWatcher.kt`** -> AI Confidence: **99.23%**
570. **`packages/block-editor/src/components/inspector-controls-tabs/use-inspector-controls-tabs.js`** -> AI Confidence: **99.22%**
571. **`packages/scripts/scripts/build-blocks-manifest.js`** -> AI Confidence: **99.22%**
572. **`packages/scripts/scripts/plugin-zip.js`** -> AI Confidence: **99.22%**
573. **`packages/block-editor/src/components/block-list/block-outline.native.js`** -> AI Confidence: **99.2%**
574. **`packages/block-library/src/file/deprecated.js`** -> AI Confidence: **99.2%**
575. **`packages/block-library/src/image/save.js`** -> AI Confidence: **99.2%**
576. **`packages/block-library/src/navigation/menu-items-to-blocks.js`** -> AI Confidence: **99.2%**
577. **`packages/block-library/src/navigation-link/index.php`** -> AI Confidence: **99.2%**
578. **`packages/components/src/unit-control/utils.ts`** -> AI Confidence: **99.2%**
579. **`packages/block-directory/src/store/actions.js`** -> AI Confidence: **99.18%**
580. **`packages/block-editor/src/autocompleters/block.js`** -> AI Confidence: **99.18%**
581. **`packages/block-editor/src/components/autocomplete/index.js`** -> AI Confidence: **99.18%**
582. **`packages/block-editor/src/components/block-caption/index.native.js`** -> AI Confidence: **99.18%**
583. **`packages/block-editor/src/components/block-parent-selector/index.js`** -> AI Confidence: **99.18%**
584. **`packages/block-editor/src/components/block-pattern-setup/index.js`** -> AI Confidence: **99.18%**
585. **`packages/block-editor/src/components/block-patterns-list/index.js`** -> AI Confidence: **99.18%**
586. **`packages/block-editor/src/components/block-preview/index.js`** -> AI Confidence: **99.18%**
587. **`packages/block-editor/src/components/block-switcher/block-variation-transformations.js`** -> AI Confidence: **99.18%**
588. **`packages/block-editor/src/components/block-tools/block-toolbar-popover.js`** -> AI Confidence: **99.18%**
589. **`packages/block-editor/src/components/button-block-appender/index.native.js`** -> AI Confidence: **99.18%**
590. **`packages/block-editor/src/components/inner-blocks/index.js`** -> AI Confidence: **99.18%**
591. **`packages/block-editor/src/components/inner-blocks/index.native.js`** -> AI Confidence: **99.18%**
592. **`packages/block-editor/src/components/inserter/block-patterns-tab/index.js`** -> AI Confidence: **99.18%**
593. **`packages/block-editor/src/components/inserter/block-types-tab.native.js`** -> AI Confidence: **99.18%**
594. **`packages/block-editor/src/components/inserter/hooks/use-block-types-state.js`** -> AI Confidence: **99.18%**
595. **`packages/block-editor/src/components/inserter/media-tab/media-preview.js`** -> AI Confidence: **99.18%**
596. **`packages/block-editor/src/components/inserter/media-tab/media-tab.js`** -> AI Confidence: **99.18%**
597. **`packages/block-editor/src/components/inserter/search-results.native.js`** -> AI Confidence: **99.18%**
598. **`packages/block-editor/src/components/media-replace-flow/index.js`** -> AI Confidence: **99.18%**
599. **`packages/block-editor/src/store/test/reducer.js`** -> AI Confidence: **99.18%**
600. **`packages/block-library/src/avatar/user-control.js`** -> AI Confidence: **99.18%**
601. **`packages/block-library/src/block/edit.native.js`** -> AI Confidence: **99.18%**
602. **`packages/block-library/src/button/index.js`** -> AI Confidence: **99.18%**
603. **`packages/block-library/src/cover/focal-point-settings-button.native.js`** -> AI Confidence: **99.18%**
604. **`packages/block-library/src/details/index.js`** -> AI Confidence: **99.18%**
605. **`packages/block-library/src/embed/edit.js`** -> AI Confidence: **99.18%**
606. **`packages/block-library/src/embed/embed-preview.js`** -> AI Confidence: **99.18%**
607. **`packages/block-library/src/form/index.js`** -> AI Confidence: **99.18%**
608. **`packages/block-library/src/freeform/edit.js`** -> AI Confidence: **99.18%**
609. **`packages/block-library/src/image/test/edit.native.js`** -> AI Confidence: **99.18%**
610. **`packages/block-library/src/math/edit.js`** -> AI Confidence: **99.18%**
611. **`packages/block-library/src/missing/edit.native.js`** -> AI Confidence: **99.18%**
612. **`packages/block-library/src/navigation-link/index.js`** -> AI Confidence: **99.18%**
613. **`packages/block-library/src/navigation/edit/use-create-overlay.js`** -> AI Confidence: **99.18%**
614. **`packages/block-library/src/pullquote/edit.js`** -> AI Confidence: **99.18%**
615. **`packages/block-library/src/query-pagination/edit.js`** -> AI Confidence: **99.18%**
616. **`packages/block-library/src/query/edit/inspector-controls/parent-control.js`** -> AI Confidence: **99.18%**
617. **`packages/block-library/src/social-link/edit.js`** -> AI Confidence: **99.18%**
618. **`packages/block-library/src/tag-cloud/edit.js`** -> AI Confidence: **99.18%**
619. **`packages/block-library/src/template-part/edit/advanced-controls.js`** -> AI Confidence: **99.18%**
620. **`packages/block-library/src/template-part/edit/selection-modal.js`** -> AI Confidence: **99.18%**
621. **`packages/block-library/src/template-part/edit/utils/hooks.js`** -> AI Confidence: **99.18%**
622. **`packages/block-library/src/term-name/edit.js`** -> AI Confidence: **99.18%**
623. **`packages/components/src/mobile/bottom-sheet-select-control/index.native.js`** -> AI Confidence: **99.18%**
624. **`packages/components/src/mobile/bottom-sheet/index.native.js`** -> AI Confidence: **99.18%**
625. **`packages/components/src/mobile/keyboard-aware-flat-list/index.ios.js`** -> AI Confidence: **99.18%**
626. **`packages/components/src/mobile/picker/index.android.js`** -> AI Confidence: **99.18%**
627. **`packages/components/src/mobile/picker/index.ios.js`** -> AI Confidence: **99.18%**
628. **`packages/core-data/src/actions.js`** -> AI Confidence: **99.18%**
629. **`packages/customize-widgets/src/components/customize-widgets/index.js`** -> AI Confidence: **99.18%**
630. **`packages/customize-widgets/src/components/header/index.js`** -> AI Confidence: **99.18%**
631. **`packages/customize-widgets/src/components/sidebar-block-editor/index.js`** -> AI Confidence: **99.18%**
632. **`packages/customize-widgets/src/filters/move-to-sidebar.js`** -> AI Confidence: **99.18%**
633. **`packages/edit-post/src/components/preferences-modal/enable-custom-fields.js`** -> AI Confidence: **99.18%**
634. **`packages/edit-site/src/components/add-new-template-legacy/index.js`** -> AI Confidence: **99.18%**
635. **`packages/edit-site/src/components/add-new-template/index.js`** -> AI Confidence: **99.18%**
636. **`packages/edit-site/src/components/dataviews-actions/index.js`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `packages/eslint-plugin/rules/__tests__/no-unknown-ds-tokens.js` -> **99.2872%** Exposure
- `packages/dataviews/src/hooks/test/use-form-validity.ts` -> **12.2948%** Exposure
- `packages/dataviews/src/dataform/stories/validation.tsx` -> **11.6568%** Exposure
- `packages/dataviews/src/field-types/stories/index.story.tsx` -> **9.4885%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `24` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13654` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergEmbedWebViewActivity.java` (JAVA) -> Cumulative Risk: **749.65**
- **Archetype:** `file_cluster_4` (Distance: 10.884 IQR)
- **Magnitude:** 167.46 | **LOC:** 161 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.6747%), Cognitive Load (97.5925%)
- **Heaviest Functions:** `onCreate` (Impact: 12.4), `setupWebViewClient` (Impact: 10.6), `onPageStarted` (Impact: 10.4)

### 2. `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` (JAVASCRIPT) -> Cumulative Risk: **713.28**
- **Archetype:** `file_cluster_17` (Distance: 13.851 IQR)
- **Magnitude:** 4254.42 | **LOC:** 3862 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getBaseGlyphRecord` (Impact: 23.3), `constructor` (Impact: 21.9), `createSubTable` (Impact: 20.6)

### 3. `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/GutenbergWebViewActivity.java` (JAVA) -> Cumulative Risk: **680.47**
- **Archetype:** `file_cluster_13` (Distance: 10.74 IQR)
- **Magnitude:** 345.42 | **LOC:** 447 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.8776%), Tech Debt (98.817%), Documentation (91.6305%)
- **Heaviest Functions:** `onOptionsItemSelected` (Impact: 14.1), `onCreate` (Impact: 12.9), `run` (Impact: 12.2)

### 4. `packages/components/src/mobile/bottom-sheet/stepper-cell/index.native.js` (JAVASCRIPT) -> Cumulative Risk: **659.49**
- **Archetype:** `file_cluster_13` (Distance: 12.126 IQR)
- **Magnitude:** 202.74 | **LOC:** 265 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.3362%)
- **Heaviest Functions:** `render` (Impact: 29.0), `constructor` (Impact: 7.0), `onIncrementValue` (Impact: 6.3)

### 5. `bin/unit-test-date.sh` (SHELL) -> Cumulative Risk: **658.87**
- **Archetype:** `file_cluster_4` (Distance: 14.8 IQR)
- **Magnitude:** 61.98 | **LOC:** 30 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 7.5), `Anonymous_Block` (Impact: 4.5), `__global_context__` (Impact: 1.5)

### 6. `packages/block-library/src/latest-posts/edit.native.js` (JAVASCRIPT) -> Cumulative Risk: **658.27**
- **Archetype:** `file_cluster_13` (Distance: 11.998 IQR)
- **Magnitude:** 200.6 | **LOC:** 295 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Tech Debt (99.9793%), Concurrency (83.0415%)
- **Heaviest Functions:** `getInspectorControls` (Impact: 14.4), `componentDidMount` (Impact: 6.5), `render` (Impact: 4.8)

### 7. `packages/customize-widgets/src/controls/inspector-section.js` (JAVASCRIPT) -> Cumulative Risk: **642.13**
- **Archetype:** `file_cluster_8` (Distance: 11.519 IQR)
- **Magnitude:** 98.82 | **LOC:** 99 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.4762%), Safety Score (87.847%)
- **Heaviest Functions:** `getInspectorSection` (Impact: 17.0), `onChangeExpanded` (Impact: 13.4), `completeCallback` (Impact: 5.7)

### 8. `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT) -> Cumulative Risk: **631.24**
- **Archetype:** `file_cluster_4` (Distance: 12.495 IQR)
- **Magnitude:** 1699.06 | **LOC:** 1140 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (96.1538%)
- **Heaviest Functions:** `findBlockButton` (Impact: 21.1), `swipeToolbarToElement` (Impact: 19.3), `waitForKeyboardToBeHidden` (Impact: 13.3)

### 9. `packages/e2e-test-utils-playwright/src/request-utils/rest.ts` (TYPESCRIPT) -> Cumulative Risk: **620.24**
- **Archetype:** `file_cluster_4` (Distance: 12.253 IQR)
- **Magnitude:** 29.33 | **LOC:** 223 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%), Safety Score (90.4304%)
- **Heaviest Functions:** `rest` (Impact: 28.5), `setupRest` (Impact: 14.7), `batchRest` (Impact: 8.7)

### 10. `packages/e2e-test-utils-playwright/src/page-utils/press-keys.ts` (TYPESCRIPT) -> Cumulative Risk: **618.34**
- **Archetype:** `file_cluster_4` (Distance: 11.271 IQR)
- **Magnitude:** 15.5 | **LOC:** 197 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (98.0358%), State Flux (93.8671%)
- **Heaviest Functions:** `emulateClipboard` (Impact: 26.2), `command` (Impact: 13.0), `command` (Impact: 10.9)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vips/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_17` (Drift: 13.851 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_17: 13.851, file_cluster_4: 13.95, file_cluster_8: 14.074
- **Magnitude:** 4254.42 | **LOC:** 3862 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getBaseGlyphRecord` (Impact: 23.3)
  * `constructor` (Impact: 21.9)
  * `createSubTable` (Impact: 20.6)
  * `constructor` (Impact: 18.2)
  * `constructor` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 1042`, `args: 586`, `func_start: 454`, `class_start: 165`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2358`, `dead_code: 12`, `duplicate_logic: 314`
* *Architecture:* `io: 6`, `api: 46`, `concurrency: 187`, `import: 2`
* *Defense:* `safety: 126`, `doc: 1`, `immutability_locks: 181`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inflate, pako, fs, zlib, unbrotli
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.495 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.233 IQR)
- **Top Global Matches:** file_cluster_4: 12.495, file_cluster_0: 13.413, file_cluster_8: 13.479
- **Magnitude:** 1699.06 | **LOC:** 1140 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.1538%), Tech Debt (15.8366%)
**Top Internal Functions/Classes:**
  * `findBlockButton` (Impact: 21.1)
  * `swipeToolbarToElement` (Impact: 19.3)
  * `waitForKeyboardToBeHidden` (Impact: 13.3)
  * `dismissKeyboard` (Impact: 9.8)
  * `getTextBlockAtPosition` (Impact: 8.9)
    * *Intent:* // =============================== // Text blocks functions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 194`, `args: 57`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 334`, `duplicate_logic: 2`
* *Architecture:* `api: 33`, `concurrency: 1087`, `import: 2`
* *Defense:* `safety: 18`, `doc: 3`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils, webdriverio
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/block-editor/src/store/test/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.718 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.034 IQR)
- **Top Global Matches:** file_cluster_8: 9.718, file_cluster_7: 10.414, file_cluster_1: 10.621
- **Magnitude:** 1686.04 | **LOC:** 5099 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.5153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 222.3)
  * `describe` (Impact: 28.8)
  * `describe` (Impact: 25.2)
  * `describe` (Impact: 23.1)
  * `describe` (Impact: 18.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 421`, `args: 285`, `func_start: 554`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 5`, `planned_debt: 1`, `duplicate_logic: 304`
* *Architecture:* `concurrency: 28`, `import: 8`
* *Defense:* `safety: 5`, `doc: 2`, `test: 446`, `sync_locks: 8`, `immutability_locks: 209`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` element, .., lock-unlock, private-keys, selectors, blocks, icons, data
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/editor/src/store/test/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.54 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.64 IQR)
- **Top Global Matches:** file_cluster_8: 9.54, file_cluster_7: 10.272, file_cluster_1: 10.461
- **Magnitude:** 1680.9 | **LOC:** 2845 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.6399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 349.5)
  * `select` (Impact: 41.8)
    * *Intent:* /** * Internal dependencies */
  * `describe` (Impact: 34.0)
  * `describe` (Impact: 31.0)
  * `describe` (Impact: 30.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 387`, `args: 268`, `func_start: 429`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `planned_debt: 1`, `duplicate_logic: 255`
* *Architecture:* `io: 10`, `api: 9`, `import: 4`
* *Defense:* `safety: 4`, `doc: 3`, `test: 336`, `immutability_locks: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deep-freeze, selectors, element, blocks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/inflate.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.265 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.764 IQR)
- **Top Global Matches:** file_cluster_8: 12.265, file_cluster_13: 12.686, file_cluster_0: 12.735
- **Magnitude:** 1523.0 | **LOC:** 4096 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (54.3289%), Tech Debt (54.8167%)
**Top Internal Functions/Classes:**
  * `inflate` (Impact: 692.5)
  * `o` (Impact: 167.3)
  * `push` (Impact: 64.8)
  * `string2buf` (Impact: 44.1)
  * `buf2string` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 132`, `args: 35`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 275`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `api: 28`, `import: 8`
* *Defense:* `safety: 121`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inffast, constants, common, gzheader, pako, strings, zstream, inflate...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/block-editor/src/store/reducer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.636 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.299 IQR)
- **Top Global Matches:** file_cluster_8: 12.636, file_cluster_13: 12.806, file_cluster_17: 12.848
- **Magnitude:** 1418.72 | **LOC:** 3138 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (23.1328%), Tech Debt (95.3251%)
**Top Internal Functions/Classes:**
  * `withBlockReset` (Impact: 419.0)
  * `attributes` (Impact: 257.4)
  * `withDerivedBlockEditingModes` (Impact: 192.8)
  * `updateParentInnerBlocksInTree` (Impact: 63.2)
  * `withPersistentBlockChange` (Impact: 34.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 169`, `args: 63`, `func_start: 59`
* *Risk/State:* `state_mutation: 94`, `dead_code: 1`, `duplicate_logic: 21`
* *Architecture:* `api: 24`, `import: 9`
* *Defense:* `safety: 74`, `doc: 116`, `sync_locks: 1`, `immutability_locks: 77`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` defaults, deprecated, index.js, blocks, compose, private-keys, array, data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.553 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.479 IQR)
- **Top Global Matches:** file_cluster_8: 12.553, file_cluster_7: 12.687, file_cluster_0: 12.723
- **Magnitude:** 1393.72 | **LOC:** 3363 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 29.4%
- **Risk Profile:** Cognitive Load (10.6254%), Tech Debt (99.977%)
**Top Internal Functions/Classes:**
  * `__unstableGetSelectedBlocksWithPartialSe` (Impact: 302.2)
    * *Intent:* /** * Given a block client ID, returns the list of all its parents from top to bottom. * * @param {O...
  * `isBlockVisibleInTheInserter` (Impact: 264.0)
  * `createSelector` (Impact: 101.6)
  * `createSelector` (Impact: 37.7)
  * `getBlockType` (Impact: 28.3)
    * *Intent:* /** * Returns whether a parent/ancestor of the block is being dragged. * * @param {Object} state Glo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 350`, `args: 154`, `func_start: 111`
* *Risk/State:* `state_mutation: 64`, `planned_debt: 1`, `duplicate_logic: 34`
* *Architecture:* `io: 1`, `api: 113`, `import: 12`
* *Defense:* `safety: 73`, `doc: 301`, `sync_locks: 6`, `immutability_locks: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` element, sorting, hooks, deprecated, utils, blocks, constants, block-editing-mode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/test/actions.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.236 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.827 IQR)
- **Top Global Matches:** file_cluster_8: 9.236, file_cluster_7: 10.004, file_cluster_1: 10.169
- **Magnitude:** 891.54 | **LOC:** 1450 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.7441%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 154.3)
  * `describe` (Impact: 38.6)
  * `describe` (Impact: 27.4)
  * `describe` (Impact: 17.7)
  * `describe` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 233`, `args: 181`, `func_start: 299`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 1`, `duplicate_logic: 203`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 10`, `import: 7`
* *Defense:* `safety: 6`, `doc: 3`, `test: 219`, `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` reducer, selectors, deep-freeze, blocks, constants, data, actions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/url/src/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.534 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.953 IQR)
- **Top Global Matches:** file_cluster_8: 10.534, file_cluster_0: 11.014, file_cluster_7: 11.191
- **Magnitude:** 882.84 | **LOC:** 1252 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 28.3)
  * `describe` (Impact: 27.7)
  * `describe` (Impact: 26.7)
  * `describe` (Impact: 23.5)
  * `it` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 177`, `args: 156`, `func_start: 463`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 43`, `duplicate_logic: 158`
* *Architecture:* `io: 243`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 427`, `immutability_locks: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` wpt-data, .., get-path-and-query-string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/test/reducer.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.232 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.373 IQR)
- **Top Global Matches:** file_cluster_8: 9.232, file_cluster_7: 10.017, file_cluster_1: 10.199
- **Magnitude:** 843.62 | **LOC:** 5739 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 38.9%
- **Risk Profile:** Cognitive Load (5.5637%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 76.7)
  * `describe` (Impact: 68.6)
  * `describe` (Impact: 56.2)
  * `describe` (Impact: 51.9)
  * `it` (Impact: 39.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 118`, `args: 95`, `func_start: 258`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 3`, `duplicate_logic: 165`
* *Architecture:* `import: 7`
* *Defense:* `doc: 3`, `test: 232`, `sync_locks: 1`, `immutability_locks: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` reducer, lock-unlock, selectors, deep-freeze, blocks, private-keys, data
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/navigation/index.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.916 IQR)
- **Top Global Matches:** file_cluster_8: 13.916, file_cluster_7: 14.049, file_cluster_13: 14.158
- **Magnitude:** 787.84 | **LOC:** 1812 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (35.5762%), Tech Debt (12.7484%)
**Top Internal Functions/Classes:**
  * `get_responsive_container_classes` (Impact: 69.0)
  * `block_core_navigation_build_css_colors` (Impact: 42.1)
    * *Intent:* /** * Get responsive container classes for the navigation block. * * @since 7.0.0 * * @param bool $i...
  * `disable_overlay_menu_for_nested_navigati` (Impact: 23.8)
  * `has_submenus` (Impact: 21.6)
  * `get_overlay_blocks_from_template_part` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 113`, `args: 33`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 338`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 14`
* *Defense:* `safety: 41`, `doc: 123`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` static function ( $block ) 
			return isset( $block['blockName'], s a null block with '\n\n'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/search/index.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.837 IQR)
- **Top Global Matches:** file_cluster_8: 13.837, file_cluster_7: 14.05, file_cluster_13: 14.079
- **Magnitude:** 764.64 | **LOC:** 622 | **CtrlFlow:** 77.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.6966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render_block_core_search` (Impact: 277.8)
    * *Intent:* /** * Server-side rendering of the `core/search` block.
  * `styles_for_block_core_search` (Impact: 96.1)
    * *Intent:* /** * This generates a CSS rule for the given border property and side if provided. * Based on wheth...
  * `apply_block_core_search_border_style` (Impact: 28.1)
    * *Intent:* /** * Registers the `core/search` block on the server.
  * `classnames_for_block_core_search` (Impact: 26.2)
  * `get_color_classes_for_block_core_search` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 33`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 260`, `dead_code: 1`
* *Architecture:* `api: 3`
* *Defense:* `safety: 47`, `doc: 36`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 
function get_typography_styles_for_block_core_search( $attributes ) 
	$typography_styles = array(, the button element class.
		$button_classes[] = wp_theme_get_element_class_name( 'button', $inline_styles['input'] ), d in an HTML style tag.
 * This excludes text-decoration, >'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/blocks/src/api/test/factory.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.818 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.343 IQR)
- **Top Global Matches:** file_cluster_8: 8.818, file_cluster_7: 9.656, file_cluster_1: 9.833
- **Magnitude:** 760.84 | **LOC:** 2357 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.0385%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 141.7)
  * `describe` (Impact: 59.9)
  * `describe` (Impact: 37.9)
  * `describe` (Impact: 22.9)
  * `describe` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 98`, `args: 79`, `func_start: 261`
* *Risk/State:* `safety_bypasses: 11`, `duplicate_logic: 161`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 4`, `doc: 2`, `test: 151`, `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deep-freeze, factory, registration, store
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/components/rich-text/native/index.native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.199 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.278 IQR)
- **Top Global Matches:** file_cluster_17: 14.199, file_cluster_13: 14.251, file_cluster_0: 14.4
- **Magnitude:** 707.64 | **LOC:** 1389 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0411%), Tech Debt (53.3307%)
**Top Internal Functions/Classes:**
  * `getLineHeight` (Impact: 35.7)
  * `handleDelete` (Impact: 32.3)
  * `handleTriggerKeyCodes` (Impact: 17.2)
  * `shouldFocusTextInputAfterMerge` (Impact: 15.3)
  * `select` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 82`, `args: 45`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 426`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `concurrency: 12`, `import: 22`
* *Defense:* `safety: 93`, `doc: 12`, `immutability_locks: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` compose, blocks, components, element, get-format-colors, react-native-aztec, i18n, rich-text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/components/link-control/test/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.162 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.929 IQR)
- **Top Global Matches:** file_cluster_8: 9.162, file_cluster_2: 9.694, file_cluster_4: 9.875
- **Magnitude:** 638.86 | **LOC:** 3741 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (25.996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 56.1)
  * `describe` (Impact: 20.1)
  * `describe` (Impact: 19.6)
  * `describe` (Impact: 15.7)
    * *Intent:* // Simulate searching for a term.
  * `describe` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 177`, `args: 92`, `func_start: 235`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 11`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 133`
* *Architecture:* `io: 37`, `api: 4`, `concurrency: 119`, `import: 7`
* *Defense:* `safety: 2`, `doc: 7`, `test: 187`, `immutability_locks: 158`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` element, user-event, .., react, fixtures, data, components
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-aztec/ios/RNTAztecView/RCTAztecView.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.406 IQR)
- **Top Global Matches:** file_cluster_0: 12.406, file_cluster_8: 12.457, file_cluster_13: 12.651
- **Magnitude:** 603.46 | **LOC:** 791 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.9717%), Tech Debt (98.6709%)
**Top Internal Functions/Classes:**
  * `setContents` (Impact: 34.9)
  * `applyFontConstraints` (Impact: 23.6)
    * *Intent:* // MARK: - Font Refreshing /// Applies the family, size and weight constraints to the provided font....
  * `interceptTriggersKeyCodes` (Impact: 21.2)
  * `packCaretDataForRN` (Impact: 21.0)
  * `interceptBackspace` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 171`, `args: 56`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `state_mutation: 139`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 12`
* *Architecture:* `io: 1`, `api: 26`, `import: 4`
* *Defense:* `safety: 49`, `doc: 25`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Aztec, CoreServices, UIKit, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/test/private-selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.003 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.217 IQR)
- **Top Global Matches:** file_cluster_8: 9.003, file_cluster_7: 9.738, file_cluster_1: 9.892
- **Magnitude:** 602.88 | **LOC:** 1690 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 46.2%
- **Risk Profile:** Cognitive Load (5.9827%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 136.9)
  * `describe` (Impact: 31.4)
  * `describe` (Impact: 15.7)
  * `describe` (Impact: 15.2)
  * `describe` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 144`, `args: 107`, `func_start: 199`
* *Risk/State:* `safety_bypasses: 12`, `duplicate_logic: 113`
* *Architecture:* `import: 4`
* *Defense:* `safety: 1`, `doc: 2`, `test: 167`, `sync_locks: 23`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` private-keys, private-selectors, selectors, blocks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core-data/src/test/selectors.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.802 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.562 IQR)
- **Top Global Matches:** file_cluster_8: 8.802, file_cluster_7: 9.644, file_cluster_1: 9.793
- **Magnitude:** 585.86 | **LOC:** 1368 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (3.099%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 42.1)
  * `describe` (Impact: 23.0)
  * `describe` (Impact: 22.7)
  * `describe` (Impact: 20.2)
  * `describe` (Impact: 17.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 88`, `args: 68`, `func_start: 151`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`, `duplicate_logic: 98`
* *Architecture:* `io: 7`, `concurrency: 2`, `import: 2`
* *Defense:* `doc: 2`, `test: 128`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` deep-freeze, selectors
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-aztec/android/src/main/java/org/wordpress/mobile/ReactNativeAztec/ReactAztecText.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.052 IQR)
- **Top Global Matches:** file_cluster_13: 11.052, file_cluster_8: 11.385, file_cluster_0: 11.415
- **Magnitude:** 585.44 | **LOC:** 720 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.1485%), Tech Debt (99.9931%)
**Top Internal Functions/Classes:**
  * `setOnLongClickListener` (Impact: 185.1)
  * `setActiveFormats` (Impact: 43.9)
  * `updateToolbarButtons` (Impact: 26.7)
  * `setCursorColor` (Impact: 16.9)
  * `forceCaretAtStartOnTakeFocus` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 126`, `args: 40`, `func_start: 57`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 66`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 19`
* *Architecture:* `api: 27`, `concurrency: 8`, `import: 43`
* *Defense:* `safety: 3`, `doc: 4`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.facebook.react.views.textinput.ContentSizeWatcher, java.util.HashSet, org.wordpress.aztec.ITextFormat, android.content.res.TypedArray, android.view.inputmethod.InputMethodManager, android.graphics.Rect, android.text.Spannable, com.facebook.react.bridge.ReactContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core-data/src/resolvers.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.043 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.192 IQR)
- **Top Global Matches:** file_cluster_4: 12.043, file_cluster_0: 12.149, file_cluster_8: 12.16
- **Magnitude:** 560.16 | **LOC:** 1339 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 37.0%
- **Risk Profile:** Cognitive Load (34.5045%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `shouldInvalidate` (Impact: 290.2)
  * `shouldInvalidate` (Impact: 9.3)
    * *Intent:* /** * Requests theme supports data from the index.
  * `shouldInvalidate` (Impact: 7.1)
  * `normalizeQueryForResolution` (Impact: 5.9)
  * `getSyncManager` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 191`, `args: 82`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 31`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 36`
* *Architecture:* `io: 31`, `api: 30`, `concurrency: 94`, `import: 10`
* *Defense:* `safety: 88`, `doc: 43`, `sync_locks: 7`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` entities, crdt-selection, html-entities, url, utils, fetch, api-fetch, change-case...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/embed/test/index.native.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.519 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.482 IQR)
- **Top Global Matches:** file_cluster_8: 9.519, file_cluster_4: 9.647, file_cluster_13: 10.156
- **Magnitude:** 547.84 | **LOC:** 1126 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.2182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 85.0)
  * `describe` (Impact: 23.6)
  * `describe` (Impact: 18.7)
  * `describe` (Impact: 12.1)
  * `it` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 212`, `args: 71`, `func_start: 159`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 48`
* *Architecture:* `io: 41`, `api: 3`, `concurrency: 167`, `import: 12`
* *Defense:* `safety: 5`, `doc: 3`, `test: 99`, `immutability_locks: 129`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .., react-native-webview, paragraph, react-native, helpers, core-data, react-native-bridge, blocks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/components/block-list/block.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.311 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 4.255 IQR)
- **Top Global Matches:** file_cluster_8: 10.311, file_cluster_13: 10.764, file_cluster_2: 10.916
- **Magnitude:** 516.06 | **LOC:** 908 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (11.2477%), Tech Debt (98.4311%)
**Top Internal Functions/Classes:**
  * `BlockListBlockProvider` (Impact: 115.6)
  * `onMerge` (Impact: 88.8)
  * `moveFirstItemUp` (Impact: 27.5)
  * `switchToDefaultOrRemove` (Impact: 27.5)
  * `removeBlock` (Impact: 24.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 48`, `args: 25`, `func_start: 75`
* *Risk/State:* `state_mutation: 6`, `duplicate_logic: 19`
* *Architecture:* `api: 2`, `import: 19`
* *Defense:* `safety: 43`, `doc: 10`, `sync_locks: 1`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` block-crash-warning, use-block-props, block-html, lock-unlock, blocks, compose, clsx, data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/navigation-link/shared/test/update-attributes.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.448 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.11 IQR)
- **Top Global Matches:** file_cluster_8: 8.448, file_cluster_7: 9.306, file_cluster_1: 9.488
- **Magnitude:** 499.42 | **LOC:** 1316 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.0938%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 84.0)
    * *Intent:* /** * Internal dependencies */
  * `describe` (Impact: 62.6)
  * `describe` (Impact: 41.5)
  * `describe` (Impact: 19.4)
  * `describe` (Impact: 12.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 51`, `args: 50`, `func_start: 148`
* *Risk/State:* `safety_bypasses: 3`, `duplicate_logic: 107`
* *Architecture:* `io: 99`, `import: 1`
* *Defense:* `doc: 1`, `test: 181`, `immutability_locks: 107`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` update-attributes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/core-data/src/entities.js` (JAVASCRIPT) | Magnitude: 65.16 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 100, structural_boundaries: 33, doc: 22, branch: 21
- `packages/core-data/src/footnotes/get-rich-text-values-cached.js` (JAVASCRIPT) | Magnitude: 12.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 5, branch: 3, state_mutation: 3
- `packages/core-data/src/hooks/use-query-select.ts` (TYPESCRIPT) | Magnitude: 3.49 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 62, structural_boundaries: 31, branch: 18, doc: 13
- `packages/ui/src/lock-unlock.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 4, branch: 2, structural_boundaries: 2, decorators: 2
- `packages/priority-queue/src/index.ts` (TYPESCRIPT) | Magnitude: 10.55 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 24, doc: 24, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/block-library/src/template-part/edit/utils/create-template-part-id.js` (JAVASCRIPT) | Magnitude: 7.5 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, decorators: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/block-library/src/gallery/index.php` (PHP) | Magnitude: 203.5 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 124, indent_tabs: 83, branch: 32, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/react-native-editor/bin/test-e2e-setup.sh` (SHELL) | Magnitude: 106.62 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 50, safety_bypasses: 43, branch: 41, state_mutation: 39
- `packages/i18n/src/default-i18n.ts` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 51, structural_boundaries: 14, api: 11, immutability_locks: 11
- `packages/react-native-editor/bin/build-e2e-wda.sh` (SHELL) | Magnitude: 4.62 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, reflection_metaprogramming: 3, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/block-editor/src/components/media-upload/index.native.js` (JAVASCRIPT) | Magnitude: 223.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 284, state_mutation: 87, branch: 47, structural_boundaries: 44
- `packages/blocks/src/api/raw-handling/blockquote-normaliser.js` (JAVASCRIPT) | Magnitude: 7.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 5, branch: 2, args: 2
- `packages/ui/src/icon-button/icon-button.tsx` (TYPESCRIPT) | Magnitude: 0.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 54, structural_boundaries: 11, ui_framework: 8, import: 7
- `packages/ui/src/form/primitives/select/trigger.tsx` (TYPESCRIPT) | Magnitude: 0.71 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 46, structural_boundaries: 15, import: 9, ui_framework: 6
- `packages/components/src/autocomplete/types.ts` (TYPESCRIPT) | Magnitude: 4.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 20, indent_tabs: 14, doc: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts` (TYPESCRIPT) | Magnitude: 26.3 | Delta: **0.211 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_tabs: 16, args: 15, func_start: 14
- `packages/block-editor/src/utils/get-px-from-css-unit.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.434 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/compose/src/higher-order/if-condition/index.tsx` (TYPESCRIPT) | Magnitude: 0.79 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_tabs: 10, doc: 5, args: 3
- `packages/components/src/alignment-matrix-control/types.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 9, doc: 8, branch: 7
- `packages/core-data/src/hooks/use-resource-permissions.ts` (TYPESCRIPT) | Magnitude: 0.47 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 13, doc: 13, generics: 8
- `packages/dataviews/src/field-types/utils/is-valid-required-for-array.ts` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 10, structural_boundaries: 5, branch: 3, args: 2
- `packages/ui/src/visually-hidden/types.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 1, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/sync/src/y-utilities/y-multidoc-undomanager.js` (JAVASCRIPT) | Magnitude: 143.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 134, state_mutation: 83, doc: 43, structural_boundaries: 34
- `packages/edit-site/src/components/page-templates/index.js` (JAVASCRIPT) | Magnitude: 110.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 294, structural_boundaries: 57, branch: 55, immutability_locks: 41
- `packages/editor/src/components/entities-saved-states/entity-type-list.js` (JAVASCRIPT) | Magnitude: 33.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 101, structural_boundaries: 23, branch: 21, safety: 13
- `packages/global-styles-ui/src/font-library/font-demo.tsx` (TYPESCRIPT) | Magnitude: 6.84 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 86, branch: 24, structural_boundaries: 24, ui_framework: 13
- `packages/block-editor/src/components/preset-input-control/utils.js` (JAVASCRIPT) | Magnitude: 72.26 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 25, branch: 19, doc: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/edit-site/src/components/layout/index.js` (JAVASCRIPT) | Magnitude: 85.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 221, ui_framework: 41, branch: 31, structural_boundaries: 27
- `packages/components/src/composite/legacy/stories/index.story.tsx` (TYPESCRIPT) | Magnitude: 2.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 167, ui_framework: 38, generics: 38, structural_boundaries: 17
- `packages/block-library/src/html/edit.js` (JAVASCRIPT) | Magnitude: 4.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 73, ui_framework: 16, structural_boundaries: 15, import: 7
- `packages/block-directory/src/components/downloadable-block-icon/index.js` (JAVASCRIPT) | Magnitude: 2.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 6, branch: 5, structural_boundaries: 3, ui_framework: 3
- `packages/components/src/mobile/keyboard-aware-flat-list/use-scroll-to-element.native.js` (JAVASCRIPT) | Magnitude: 13.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, doc: 9, structural_boundaries: 7, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/compose/src/hooks/use-copy-to-clipboard/index.ts` (TYPESCRIPT) | Magnitude: 10.61 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 66, structural_boundaries: 25, branch: 20, doc: 17
- `packages/core-data/src/hooks/test/use-entity-record.js` (JAVASCRIPT) | Magnitude: 92.8 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 122, structural_boundaries: 41, concurrency: 31, test: 25
- `packages/components/src/utils/element-rect.ts` (TYPESCRIPT) | Magnitude: 7.41 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 14, concurrency: 13, args: 11
- `packages/scripts/config/jest-environment-puppeteer/global.js` (JAVASCRIPT) | Magnitude: 27.5 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 57, concurrency: 15, branch: 14, structural_boundaries: 12
- `packages/block-directory/src/store/load-assets.js` (JAVASCRIPT) | Magnitude: 39.14 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 13, branch: 7, args: 7

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
- `packages/block-editor/src/components/global-styles/background-panel.js` (JAVASCRIPT) | Magnitude: 108.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 189, branch: 63, safety: 46, structural_boundaries: 44
- `packages/customize-widgets/src/filters/replace-media-upload.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, func_start: 2, decorators: 2
- `packages/edit-widgets/src/filters/replace-media-upload.js` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_tabs: 3, func_start: 2, decorators: 2
- `packages/editor/src/components/post-last-revision/test/check.js` (JAVASCRIPT) | Magnitude: 29.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 27, func_start: 19, structural_boundaries: 14, args: 12
- `packages/patterns/src/components/duplicate-pattern-modal.js` (JAVASCRIPT) | Magnitude: 18.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 18, branch: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/block-library/src/video/index.php` (PHP) | Magnitude: 10.64 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, branch: 5, doc: 5, structural_boundaries: 3
- `packages/rich-text/src/create-element.js` (JAVASCRIPT) | Magnitude: 2.24 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 5, doc: 4, structural_boundaries: 2, branch: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/core-data/src/resolvers.js` -> Churn: **65.99%** | Cog Load: 34.5045% | Debt: 99.9996%
- `packages/block-editor/src/store/reducer.js` -> Churn: **64.84%** | Cog Load: 23.1328% | Debt: 95.3251%
- `packages/sync/src/providers/http-polling/polling-manager.ts` -> Churn: **59.32%** | Cog Load: 8.6168% | Debt: 79.931%
- `packages/block-editor/src/store/selectors.js` -> Churn: **55.7%** | Cog Load: 10.6254% | Debt: 99.977%
- `packages/block-library/src/navigation/edit/index.js` -> Churn: **54.93%** | Cog Load: 8.1452% | Debt: 99.832%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **Riad Benguella** (100.0% isolated ownership) | Magnitude: 4254.42
- `packages/react-native-editor/__device-tests__/pages/editor-page.js` -> **Ella** (100.0% isolated ownership) | Magnitude: 1699.06
- `packages/editor/src/store/test/selectors.js` -> **Aki Hamano** (100.0% isolated ownership) | Magnitude: 1680.9
- `packages/block-editor/src/store/test/actions.js` -> **Aki Hamano** (100.0% isolated ownership) | Magnitude: 891.54
- `packages/url/src/test/index.js` -> **Manuel Camargo** (100.0% isolated ownership) | Magnitude: 882.84

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/eslint-plugin/configs/i18n.js` -> **Severity: 3097.463** (Blast Radius: 56.505 * Doc Risk: 54.8175%)
- `storybook/stories/tokens/components.tsx` -> **Severity: 1891.129** (Blast Radius: 47.304 * Doc Risk: 39.9782%)
- `packages/e2e-test-utils-playwright/src/request-utils/blocks.ts` -> **Severity: 466.941** (Blast Radius: 26.004 * Doc Risk: 17.9565%)
- `packages/block-library/src/utils/init-block.js` -> **Severity: 188.255** (Blast Radius: 7.169 * Doc Risk: 26.2596%)
- `packages/e2e-test-utils-playwright/src/page-utils/keycodes.ts` -> **Severity: 175.718** (Blast Radius: 4.08 * Doc Risk: 43.0682%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
