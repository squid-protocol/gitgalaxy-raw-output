# ARCHITECTURAL_BRIEF: gutenberg
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/wordpress/gutenberg.git` |
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
- **Scope:** 11176 analyzed artifact(s), 806914 LOC.
- **Load-bearing artifact:** `packages/block-editor/src/store/index.js` -- 230 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/block-library/src/index.js` -- pulls in 131 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 12229 |
| Analyzed Artifacts (Scanned) | 11176 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1053 |
| Total LOC | 806914 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.4% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9054 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1052 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4045 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1240 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4199 | 442378 | 37.6% |
| TYPESCRIPT | 2427 | 225985 | 21.7% |
| JSON | 1101 | 34811 | 9.9% |
| CSS | 814 | 34026 | 7.3% |
| MARKDOWN | 751 | 0 | 6.7% |
| HTML | 675 | 2134 | 6.0% |
| PHP | 477 | 55862 | 4.3% |
| XML | 380 | 1 | 3.4% |
| PLAINTEXT | 225 | 2 | 2.0% |
| YAML | 33 | 2386 | 0.3% |
| JAVA | 29 | 4089 | 0.3% |
| SWIFT | 20 | 2749 | 0.2% |
| SHELL | 13 | 822 | 0.1% |
| GROOVY | 9 | 424 | 0.1% |
| KOTLIN | 9 | 782 | 0.1% |
| OBJECTIVE-C | 6 | 134 | 0.1% |
| RUBY | 4 | 110 | 0.0% |
| BATCH | 3 | 211 | 0.0% |
| PYTHON | 1 | 8 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 11174 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 38%, Declarative / Non-Code 17%, Large Core Modules (2) 12%, Callbacks & Closures Files 11%, Large Core Modules 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 10197 | 91.2% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 974 | 8.7% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1053*

**Composition by Extension & Reason:**
- `.md`: 236x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3442 LOC)
- `.png`: 176x Excluded (Explicitly Denied Extension: '.png')
- `.html`: 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 33x Excluded (Saturation: Line 2 exceeds 500 chars), 15x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.snap`: 121x Unsupported Format (.snap), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.snap')
- `.js`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 34x Excluded (Saturation: Line 8 exceeds 500 chars), 2x Excluded (Saturation: Line 14 exceeds 500 chars)
- `no_extension`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable), 4x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.mustache`: 38x Excluded (Unsupported Extension: '.mustache'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 24291 LOC), 1x Excluded (Massive Static Asset Blob: 63386 LOC)
- `.jpg`: 18x Excluded (Explicitly Denied Extension: '.jpg')
- `.css`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.template`: 14x Excluded (Unsupported Extension: '.template')
- `.woff2`: 11x Excluded (Explicitly Denied Extension: '.woff2')
- `.ttf`: 10x Excluded (Explicitly Denied Extension: '.ttf')
- `.scss`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 70 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 78, Signals: 0)
- `.ts`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.8 | 3.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.0 | 18.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 67.4 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 72.7 | 4.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3229 | 977 | 0 | `packages/core-data/src/utils/test/crdt-blocks.ts` |
| cleanup | 494 | 252 | 0 | `lib/class-wp-theme-json-gutenberg.php` |
| guards | 24176 | 3516 | 6 | `lib/class-wp-theme-json-gutenberg.php` |
| danger | 4737 | 1417 | 1 | `packages/react-native-editor/bin/generate-pot-files.sh` |
| concurrency | 30691 | 1763 | 2 | `test/e2e/specs/editor/blocks/navigation.spec.js` |
| connectivity | 16329 | 5617 | 3 | `packages/theme/src/prebuilt/css/design-tokens.css` |
| io | 3123 | 708 | 0 | `packages/wp-build/lib/build.mjs` |
| crypto | 5 | 5 | 0 | `packages/env/lib/md5.js` |
| ipc | 79 | 44 | 0 | `packages/upload-media/src/test/feature-detection.ts` |
| time | 772 | 242 | 0 | `packages/components/src/calendar/stories/date-range-calendar.story.tsx` |
| serialization | 335 | 180 | 0 | `packages/element/src/test/create-interpolate-element.tsx` |
| regex | 1089 | 502 | 0 | `packages/autop/src/index.ts` |
| events | 2994 | 713 | 0 | `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` |
| tests | 38633 | 1348 | 5 | `packages/block-editor/src/store/test/reducer.js` |
| docs | 22263 | 6629 | 4 | `packages/editor/src/store/selectors.js` |
| debt | 2230 | 672 | 0 | `packages/block-editor/src/store/test/actions.js` |
| mutation | 125723 | 6865 | 29 | `packages/global-styles-ui/src/font-library/lib/inflate.js` |
| dead_code | 2309 | 527 | 0 | `phpunit/class-wp-theme-json-test.php` |
| credential | 65 | 32 | 0 | `packages/dataviews/src/dataviews-picker/stories/fixtures.tsx` |
| threat | 60 | 21 | 0 | `platform-docs/src/components/HomepageBlocks/index.js` |
| ml_ai | 247 | 88 | 0 | `test/integration/fixtures/blocks/core__math.html` |
| ui | 28946 | 3793 | 8 | `packages/components/src/menu/stories/index.story.tsx` |

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

1. **index.js** (`packages/block-editor/src/store/index.js`) — 230 inbound connections
2. **index.ts** (`packages/components/src/context/index.ts`) — 181 inbound connections
3. **index.js** (`packages/editor/src/store/index.js`) — 164 inbound connections
4. **index.ts** (`packages/dataviews/src/types/index.ts`) — 145 inbound connections
5. **selectors.js** (`packages/block-editor/src/store/selectors.js`) — 138 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`packages/block-library/src/index.js`) — 131 outbound dependencies
2. **index.ts** (`packages/components/src/index.ts`) — 130 outbound dependencies
3. **load.php** (`lib/load.php`) — 115 outbound dependencies
4. **index.js** (`packages/block-editor/src/components/index.js`) — 111 outbound dependencies
5. **index.js** (`packages/editor/src/components/index.js`) — 89 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inflate` **(Many-Argument Workhorses)** (@ `packages/global-styles-ui/src/font-library/lib/inflate.js`) -> Impact: **483.5** | LOC: 1426
- `Image` **(Many-Argument Workhorses)** (@ `packages/block-library/src/image/image.js`) -> Impact: **342.9** | LOC: 1032
- `gutenberg_get_layout_style` **(Many-Argument Workhorses)** (@ `lib/block-supports/layout.php`) -> Impact: **278.4** | LOC: 363
  * *Intent:* /** * Generates the CSS corresponding to the provided layout. * * @param string $selector CSS selector. * @param array $layout Layout object. The one ...
- `Navigation` **(Many-Argument Workhorses)** (@ `packages/block-library/src/navigation/edit/index.js`) -> Impact: **217.6** | LOC: 929
- `gutenberg_render_layout_support_flag` **(Many-Argument Workhorses)** (@ `lib/block-supports/layout.php`) -> Impact: **213.7** | LOC: 429
  * *Intent:* /** * Renders the layout config to the block wrapper. * * @param string $block_content Rendered block content. * @param array $block Block object. * @...
- `CoverEdit` **(Defensive Guards)** (@ `packages/block-library/src/cover/edit/index.js`) -> Impact: **202.0** | LOC: 645
- `TypographyPanel` **(Defensive Guards)** (@ `packages/block-editor/src/components/global-styles/typography-panel.js`) -> Impact: **196.7** | LOC: 539
- `transformToStyles` **(Many-Argument Workhorses)** (@ `packages/global-styles-engine/src/core/render.tsx`) -> Impact: **192.6** | LOC: 345
- `GalleryEdit` **(Many-Argument Workhorses)** (@ `packages/block-library/src/gallery/edit.js`) -> Impact: **189.4** | LOC: 875
- `FontLibraryProvider` **(Defensive Guards)** (@ `packages/global-styles-ui/src/font-library/context.tsx`) -> Impact: **188.9** | LOC: 525

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/e2e/specs/editor/various` | 100 | 14582.5 | 33.63% | 0.0% |
| `test/e2e/specs/editor/blocks` | 39 | 9386.46 | 35.08% | 0.0% |
| `packages/global-styles-ui/src/font-library/lib` | 4 | 8047.68 | 66.94% | 30.0% |
| `test/e2e/specs/interactivity` | 31 | 7108.23 | 9.91% | 0.0% |
| `lib` | 26 | 6690.02 | 20.43% | 17.26% |
| `__monolith__` | 17 | 6310.16 | 0.25% | 2.22% |
| `packages/vips` | 5 | 5021.44 | 0.0% | 0.0% |
| `test/e2e/specs/editor/collaboration` | 16 | 4193.87 | 51.42% | 0.0% |
| `test/e2e/specs/site-editor` | 48 | 4026.02 | 10.88% | 0.0% |
| `packages/block-editor/src/store` | 13 | 3694.82 | 10.49% | 3.43% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/Bug_report.yml` -> **100.0%** Exposure
- `packages/block-library/src/navigation-submenu/transforms.js` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-wp-fonts-provider.php` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-wp-fonts-resolver.php` -> **100.0%** Exposure
- `lib/experimental/font-face/bc-layer/class-wp-fonts-utils.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/api-docs/gen-block-lib-list.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/clear.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/filter-message.js` -> **100.0%** Exposure
- `packages/a11y/src/shared/index.js` -> **100.0%** Exposure
- `packages/block-editor/src/components/audio-player/audio-url-parser.native.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `phpunit/class-wp-theme-json-test.php` -> **142** Orphaned Functions | **0** Duplicates
- `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` -> **79** Orphaned Functions | **0** Duplicates
- `packages/block-editor/src/store/test/actions.js` -> **0** Orphaned Functions | **60** Duplicates
- `phpunit/tests/collaboration/wpHttpPollingSyncServer.php` -> **60** Orphaned Functions | **0** Duplicates
- `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/ReactNativeGutenbergBridge/RNReactNativeGutenbergBridgeModule.java` -> **57** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/e2e/specs/editor/blocks/avatar.spec.js` -> **99.8994%** Exposure
- `packages/eslint-plugin/rules/__tests__/no-unknown-ds-tokens.js` -> **99.2872%** Exposure
- `packages/e2e-tests/plugins/connectors-test-provider.php` -> **99.1938%** Exposure
- `test/e2e/specs/editor/various/autocomplete-and-mentions.spec.js` -> **98.6603%** Exposure
- `test/e2e/specs/admin/connectors.spec.js` -> **26.8157%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14265` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vips/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/inflate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.798)
- **Top Global Matches:** file_cluster_6: 6.798, file_cluster_4: 8.585, file_cluster_15: 16.255
- **Magnitude:** 3877.3 | **LOC:** 4096 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.4%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inflate` **(Many-Argument Workhorses)** (Impact: 483.5)
  * `inflate_table` **(Many-Argument Workhorses)** (Impact: 159.9)
  * `inflate_fast` **(Many-Argument Workhorses)** (Impact: 110.9)
    * *Intent:* */
  * `push` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* * We strongly recommend to use `Uint8Array` on input for best speed (output * format is detected aut...
  * `Inflate` **(Defensive Guards)** (Impact: 34.4)
    * *Intent:* * var pako = require('pako') * , chunk1 = Uint8Array([1,2,3,4,5,6,7,8,9]) * , chunk2 = Uint8Array([1...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 815 instances
* *State Mutation (weighted view):* 2606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 372`, `args: 57`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 976`, `dead_code: 80`, `planned_debt: 2`
* *Architecture:* `api: 40`, `import: 14`
* *Defense:* `safety: 156`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000213
  * `Imports (Out-Degree: 3):` common, adler32, common, crc32, inffast, inftrees, common, strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/class-wp-theme-json-gutenberg.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.081)
- **Top Global Matches:** file_cluster_6: 6.081, file_cluster_8: 11.573, file_cluster_4: 13.292
- **Magnitude:** 3683.36 | **LOC:** 5073 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 29.2%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 1.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_layout_styles` **(Many-Argument Workhorses)** (Impact: 125.5)
    * *Intent:* /** * Gets the CSS layout rules for a particular block from theme.json layout definitions. * * @sinc...
  * `compute_style_properties` **(Many-Argument Workhorses)** (Impact: 100.8)
    * *Intent:* * @since 5.9.0 Added the `$settings` and `$properties` parameters. * @since 6.1.0 Added `$theme_json...
  * `get_block_nodes` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* * An internal method to get the block nodes from a theme.json file. * * @since 6.1.0 * * @param arra...
  * `get_styles_for_block` **(Many-Argument Workhorses)** (Impact: 79.6)
    * *Intent:* /** * Gets the CSS rules for a particular block from theme.json. * * @since 6.1.0 * @since 6.6.0 Set...
  * `sanitize` **(Many-Argument Workhorses)** (Impact: 79.4)
    * *Intent:* /** * Sanitizes the input according to the schemas. * * @since 5.8.0 * @since 5.9.0 Added the `$vali...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 641 instances
* *State Mutation (weighted view):* 2068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 740`, `structural_boundaries: 361`, `args: 84`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 786`, `unreferenced_by_name: 15`
* *Architecture:* `api: 24`
* *Defense:* `safety: 259`, `doc: 101`, `immutability_locks: 18`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.039
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001433
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.587)
- **Top Global Matches:** file_cluster_15: 6.587, file_cluster_10: 7.435, file_cluster_11: 7.777
- **Magnitude:** 2520.32 | **LOC:** 3862 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.7%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (74.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 21.9)
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
* *Structure:* `branch: 244`, `structural_boundaries: 1048`, `args: 586`, `func_start: 324`, `class_start: 165`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 800`, `dead_code: 17`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 48`, `concurrency: 97`, `import: 2`
* *Defense:* `safety: 126`, `doc: 1`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000229
  * `Imports (Out-Degree: 2):` inflate, unbrotli
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/e2e/specs/editor/blocks/list.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_10: 6.465, file_cluster_12: 6.692, file_cluster_2: 7.233
- **Magnitude:** 2271.9 | **LOC:** 1743 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (68.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 242 instances
* *Concurrency (weighted view):* 1644
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 517`, `args: 61`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 583`
* *Architecture:* `concurrency: 434`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-ui/src/font-library/lib/unbrotli.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.842)
- **Top Global Matches:** file_cluster_4: 5.842, file_cluster_15: 8.931, file_cluster_12: 10.153
- **Magnitude:** 1649.16 | **LOC:** 2689 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.081; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 96.3636% of unit weight undocumented
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
* *Structure:* `branch: 218`, `structural_boundaries: 341`, `args: 64`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 404`, `dead_code: 1`
* *Architecture:* `api: 31`, `import: 15`
* *Defense:* `safety: 56`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000213
  * `Imports (Out-Degree: 0):` bit_reader, context, decode, decode, dictionary, dictionary-browser, dictionary.bin.js, huffman...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/block-editor/src/store/reducer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.252)
- **Top Global Matches:** file_cluster_4: 6.252, file_cluster_6: 10.262, file_cluster_15: 11.914
- **Magnitude:** 1444.06 | **LOC:** 3138 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **9**; blast radius 0.843; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.7%), Connectivity (formerly Api Exposure) (79.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.9%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 12.1212% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withDerivedBlockEditingModes` **(Defensive Guards)** (Impact: 151.8)
    * *Intent:* /** * Higher-order reducer that adds derived block editing modes to the state. * * This function wra...
  * `getDerivedBlockEditingModesForTree` **(Many-Argument Workhorses)** (Impact: 90.7)
    * *Intent:* /** * Computes and returns derived block editing modes for a given block tree. * * This function cal...
  * `withBlockTree` **(Compute Cores)** (Impact: 47.1)
    * *Intent:* /** * Higher-order reducer intended to compute full block objects key for each block in the post. * ...
  * `selection` **(Defensive Guards)** (Impact: 44.4)
    * *Intent:* /** * Reducer returning the selection state. * * */
  * `selectionHelper` **(Defensive Guards)** (Impact: 35.7)
    * *Intent:* /** * Internal helper reducer for selectionStart and selectionEnd. Can hold a block * selection, rep...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 137 instances
* *State Mutation (weighted view):* 426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 535`, `structural_boundaries: 443`, `args: 134`, `func_start: 65`
* *Risk/State:* `state_mutation: 152`, `planned_debt: 1`
* *Architecture:* `api: 34`, `import: 9`
* *Defense:* `safety: 192`, `doc: 60`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.843
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.015197
  * `Imports (Out-Degree: 4):` lock-unlock, array, defaults, private-keys, blocks, compose, data, deprecated...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `phpunit/class-wp-theme-json-test.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_15: 7.346, file_cluster_11: 7.41, file_cluster_2: 7.69
- **Magnitude:** 1420.08 | **LOC:** 7442 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 26.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.3%), Guard Balance (formerly Safety Score) (55.5%)
- **Documentation Coverage:** 52.8814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_merge_incoming_data` **(I/O & Config Routines)** (Impact: 6.0)
  * `test_opt_in_to_block_style_variations` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* /** * Block style variations styles aren't generated by default. This test ensures * variations are ...
  * `test_sanitize_removes_non_boolean_values_when_schema_expects_boolean` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /** * @covers WP_Theme_JSON_Gutenberg::sanitize * @covers WP_Theme_JSON_Gutenberg::remove_keys_not_i...
  * `test_get_block_background_image_styles` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_opt_out_of_block_style_variations_by_default` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* /** * Block style variations styles aren't generated by default. This test covers * the `get_block_n...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 291`, `args: 144`, `func_start: 144`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 772`, `unreferenced_by_name: 142`
* *Architecture:* `io: 4`, `api: 142`
* *Defense:* `safety: 11`, `doc: 69`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/interactivity/directive-each.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.059)
- **Top Global Matches:** file_cluster_10: 5.059, file_cluster_2: 7.14, file_cluster_13: 7.659
- **Magnitude:** 1412.37 | **LOC:** 705 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.0%), Guard Balance (formerly Safety Score) (38.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 296
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 235`, `args: 53`, `func_start: 29`
* *Risk/State:* `state_mutation: 7`, `planned_debt: 1`
* *Architecture:* `concurrency: 216`, `import: 1`
* *Defense:* `doc: 1`, `test: 159`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fixtures
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/various/writing-flow.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.515)
- **Top Global Matches:** file_cluster_10: 6.515, file_cluster_12: 8.54, file_cluster_2: 8.996
- **Magnitude:** 1334.0 | **LOC:** 1255 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addDemoContent` **(I/O & Config Routines)** (Impact: 3.0)
  * `getActiveBlockName` **(Callbacks & Closures)** (Impact: 2.4)
  * `writingFlowUtils` **(Callbacks & Closures)** (Impact: 1.9)
  * `constructor` **(State Mutators)** (Impact: 1.7)
  * `getHeight` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 145 instances
* *Concurrency (weighted view):* 1189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 488`, `args: 62`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 112`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 464`, `import: 1`
* *Defense:* `safety: 5`, `doc: 1`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/interactivity/router-regions.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.395)
- **Top Global Matches:** file_cluster_10: 5.395, file_cluster_2: 6.968, file_cluster_13: 7.337
- **Magnitude:** 1248.26 | **LOC:** 769 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (47.2%), Guard Balance (formerly Safety Score) (36.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fixtures, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/global-styles-engine/src/core/render.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.246)
- **Top Global Matches:** file_cluster_8: 9.246, file_cluster_3: 19.326, file_cluster_6: 19.428
- **Magnitude:** 1228.74 | **LOC:** 1982 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 0.094; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (44.3%), Connectivity (formerly Api Exposure) (43.1%)
- **Documentation Coverage:** 57.5758% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformToStyles` **(Many-Argument Workhorses)** (Impact: 192.6)
  * `getNodesWithStyles` **(Many-Argument Workhorses)** (Impact: 116.1)
  * `getStylesDeclarations` **(Many-Argument Workhorses)** (Impact: 83.7)
    * *Intent:* /** * Transform given style tree into a set of style declarations. * */
  * `getLayoutStyles` **(Defensive Guards)** (Impact: 62.0)
    * *Intent:* /** * Get generated CSS for layout styles by looking up layout definitions provided * in theme.json,...
  * `generateGlobalStyles` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /** * Returns the global styles output based on the current state of global styles config loaded in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 117 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 174`, `args: 76`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 150`
* *Architecture:* `io: 11`, `api: 12`, `import: 14`
* *Defense:* `safety: 117`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.094
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000268
  * `Imports (Out-Degree: 11):` get-setting, types, background, common, duotone, gap, layout, object...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/e2e/specs/editor/blocks/navigation.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.732)
- **Top Global Matches:** file_cluster_12: 7.732, file_cluster_10: 7.825, file_cluster_11: 8.661
- **Magnitude:** 1195.94 | **LOC:** 2403 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 73.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.6%), Guard Balance (formerly Safety Score) (45.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.6%)
- **Documentation Coverage:** 60.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `arrowToLabel` **(Defensive Guards)** (Impact: 7.6)
  * `addPage` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* /** * Adds a page via the link control and closes it. * Usage: * - Open the new link control however...
  * `previewIsOpenAndCloses` **(Callbacks & Closures)** (Impact: 4.4)
    * *Intent:* /** * Checks: * - the preview is open * - has focus within it * - closes with Escape * - The popover...
  * `useLinkControlSearch` **(Parameter Forwarders)** (Impact: 2.3)
  * `useToolbarButton` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* /** * Moves focus to the toolbar and arrows to the button and activates it. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 1071
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 733`, `args: 134`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 40`, `planned_debt: 4`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 711`, `import: 1`
* *Defense:* `safety: 13`, `doc: 17`, `test: 234`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `changelog.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1185.38 | **LOC:** 59269 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/block-supports/layout.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.614)
- **Top Global Matches:** file_cluster_6: 7.614, file_cluster_8: 9.807, file_cluster_4: 15.478
- **Magnitude:** 1183.28 | **LOC:** 1259 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.31; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gutenberg_get_layout_style` **(Many-Argument Workhorses)** (Impact: 278.4)
    * *Intent:* /** * Generates the CSS corresponding to the provided layout. * * @param string $selector CSS select...
  * `gutenberg_render_layout_support_flag` **(Many-Argument Workhorses)** (Impact: 213.7)
    * *Intent:* /** * Renders the layout config to the block wrapper. * * @param string $block_content Rendered bloc...
  * `gutenberg_restore_group_inner_container` **(Many-Argument Workhorses)** (Impact: 25.3)
    * *Intent:* /** * For themes without theme.json file, make sure * to restore the inner div for the group block *...
  * `gutenberg_restore_image_outer_container` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /** * For themes without theme.json file, make sure * to restore the outer div for the aligned image...
  * `gutenberg_get_block_style_variation_name_from_registered_style` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* /** * Layout block support flag. * * @package gutenberg */ /** * Get the first style variation name ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 188 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 51`, `args: 14`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 224`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `safety: 75`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/e2e/specs/editor/collaboration/collaboration-refresh.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_12: 6.66, file_cluster_7: 7.257, file_cluster_5: 7.847
- **Magnitude:** 1131.72 | **LOC:** 182 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (86.2%), Guard Balance (formerly Safety Score) (45.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 111
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 60`, `args: 12`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `io: 1`, `concurrency: 41`, `import: 4`
* *Defense:* `safety: 17`, `doc: 3`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fixtures, collaboration-utils, test, e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-library/src/navigation/index.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.489)
- **Top Global Matches:** file_cluster_4: 6.489, file_cluster_16: 7.57, file_cluster_15: 8.172
- **Magnitude:** 1106.08 | **LOC:** 1812 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 26.7%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.8%), Complexity Load (formerly Cognitive Load) (35.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_responsive_container_markup` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /** * Get the responsive container markup * * @since 6.5.0 * * @param array $attributes The block at...
  * `block_core_navigation_build_css_colors` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* /** * Build an array with CSS classes and inline styles defining the colors * which will be applied ...
  * `block_core_navigation_parse_blocks_from_menu_items` **(Defensive Guards)** (Impact: 22.9)
    * *Intent:* * Turns menu item data into a nested array of parsed blocks * * @since 5.9.0 * * @deprecated 6.3.0 U...
  * `get_overlay_blocks_from_template_part` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /** * Gets the inner blocks for the navigation block from an overlay template part. * * @since 6.5.0...
  * `get_inner_blocks` **(Stateful Encapsulated Methods)** (Impact: 19.8)
    * *Intent:* /** * Gets the inner blocks for the navigation block. * * @since 6.5.0 * * @param array $attributes ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 176`, `args: 51`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 260`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 60`, `doc: 59`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/block-editor/src/store/selectors.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.694)
- **Top Global Matches:** file_cluster_15: 6.694, file_cluster_10: 8.463, file_cluster_11: 8.628
- **Magnitude:** 907.44 | **LOC:** 3363 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 21.4%
- **Blast Radius:** changing it is visible to **138** in-repo importer(s); it depends on **12**; blast radius 3.287; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (63.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.4%), Guard Balance (formerly Safety Score) (46.3%)
- **Documentation Coverage:** 7.2626% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canInsertBlockTypeUnmemoized` **(Many-Argument Workhorses)** (Impact: 81.4)
    * *Intent:* /** * Determines if the given block type is allowed to be inserted into the block list. * This funct...
  * `canRemoveBlock` **(Defensive Guards)** (Impact: 38.6)
    * *Intent:* /** * Determines if the given block is allowed to be deleted. * * */
  * `isBlockVisibleInTheInserter` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* * Determines if the given block type is visible in the inserter. * Note that this is different than ...
  * `__unstableIsSelectionMergeable` **(Defensive Guards)** (Impact: 28.0)
    * *Intent:* /** * Check whether the selection is mergeable. * * */
  * `__unstableHasActiveBlockOverlayActive` **(Compute Cores)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 502`, `args: 209`, `func_start: 95`
* *Risk/State:* `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `api: 112`, `import: 12`
* *Defense:* `safety: 133`, `doc: 120`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.287
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.018722
  * `Imports (Out-Degree: 5):` lock-unlock, sorting, constants, private-selectors, utils, blocks, data, deprecated...
  * `Imported By (In-Degree: 138):` (Excluded from Brief to save tokens)

### `packages/react-native-editor/__device-tests__/pages/editor-page.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.349)
- **Top Global Matches:** file_cluster_12: 7.349, file_cluster_15: 7.832, file_cluster_11: 8.496
- **Magnitude:** 900.62 | **LOC:** 1140 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 0.157; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (96.5%), Mutation Surface (formerly State Flux) (89.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.3871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBlockAtPosition` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* // Finds the wd element for new block that was added and sets the element attribute // and accessibi...
  * `swipeToolbarToElement` **(Compute Cores)** (Impact: 17.5)
  * `findBlockButton` **(Compute Cores)** (Impact: 14.5)
    * *Intent:* // Attempts to find the given block button in the block inserter control.
  * `getTitleElement` **(Defensive Guards)** (Impact: 11.1)
  * `pasteClipboardToTextBlock` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 438
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 262`, `args: 76`, `func_start: 76`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 32`
* *Architecture:* `api: 49`, `concurrency: 258`, `import: 1`
* *Defense:* `safety: 20`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000626
  * `Imports (Out-Degree: 1):` utils
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/wp-build/lib/build.mjs` (JAVASCRIPT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.785)
- **Top Global Matches:** file_cluster_4: 6.785, file_cluster_6: 9.871, file_cluster_15: 12.415
- **Magnitude:** 810.66 | **LOC:** 2181 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 19.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (62.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.0%)
- **Documentation Coverage:** 28.2051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bundlePackage` **(Many-Argument Workhorses)** (Impact: 73.7)
    * *Intent:* /** * Bundle a package for WordPress using esbuild. * */
  * `buildAll` **(Compute Cores)** (Impact: 35.1)
    * *Intent:* /** * Main build function. * */
  * `transpilePackage` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* /** * Transpile a single package's source files and copy JSON files. * */
  * `watchMode` **(I/O & Config Routines)** (Impact: 30.1)
    * *Intent:* /** * Watch mode for development. */
  * `transformPhpContent` **(Many-Argument Workhorses)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 261
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 264`, `args: 93`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 50`, `unreferenced_by_name: 2`
* *Architecture:* `io: 97`, `api: 2`, `concurrency: 131`, `import: 27`
* *Defense:* `safety: 63`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` , dependency-graph.mjs, package-utils.mjs, php-generator.mjs, route-utils.mjs, wordpress-externals-plugin.mjs, worker-build.mjs, esbuild-ds-token-fallbacks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/e2e/specs/editor/various/pattern-overrides.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.082)
- **Top Global Matches:** file_cluster_10: 6.082, file_cluster_2: 6.515, file_cluster_12: 6.861
- **Magnitude:** 781.5 | **LOC:** 1487 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 67 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 668
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 362`, `args: 33`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 72`, `fragile_debt: 1`
* *Architecture:* `concurrency: 333`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native-bridge/android/react-native-bridge/src/main/java/org/wordpress/mobile/WPAndroidGlue/WPAndroidGlueCode.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.104)
- **Top Global Matches:** file_cluster_5: 8.104, file_cluster_12: 8.879, file_cluster_7: 10.635
- **Magnitude:** 781.18 | **LOC:** 1178 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **70**; blast radius 0.104; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.5%)
- **Documentation Coverage:** 99.1453% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPackages` **(Annotated & Test Methods)** (Impact: 47.5)
  * `attachToContainer` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `requestMediaPickFromMediaLibrary` **(Compute Cores)** (Impact: 17.2)
  * `requestMediaPickFromDeviceLibrary` **(Compute Cores)** (Impact: 12.7)
  * `appendMediaFiles` **(Compute Cores)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 291`, `args: 144`, `func_start: 145`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 100`, `fragile_debt: 1`, `unreferenced_by_name: 79`
* *Architecture:* `api: 113`, `concurrency: 8`, `import: 70`
* *Defense:* `safety: 6`, `doc: 2`, `sync_locks: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.9e-05
  * `Imports (Out-Degree: 8):` android.app.Activity, android.app.Application, android.content.Context, android.content.MutableContextWrapper, android.os.Build, android.os.Bundle, android.os.Handler, android.os.Looper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/performance/specs/post-editor.spec.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.867)
- **Top Global Matches:** file_cluster_10: 5.867, file_cluster_12: 8.584, file_cluster_2: 8.646
- **Magnitude:** 735.22 | **LOC:** 723 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (48.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (4.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `type` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `perfUtils` **(Callbacks & Closures)** (Impact: 1.9)
  * `metrics` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 87 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 584
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 199`, `args: 41`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 89`
* *Architecture:* `concurrency: 149`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fixtures, utils.js, e2e-test-utils-playwright
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sync/src/providers/http-polling/test/utils.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.806)
- **Top Global Matches:** file_cluster_10: 3.806, file_cluster_2: 6.186, file_cluster_13: 6.751
- **Magnitude:** 723.32 | **LOC:** 664 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.0%), Concurrency Surface (formerly Concurrency) (30.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.4%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 86`, `args: 65`, `func_start: 4`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 4`, `concurrency: 8`, `import: 4`
* *Defense:* `doc: 3`, `test: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` types, utils, globals, api-fetch
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/fields/src/stories/index.story.tsx` (TYPESCRIPT) | Magnitude: 14.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 145, structural_boundaries: 30, core_var_decl: 22, args: 8
- `packages/preferences/src/components/preference-toggle-control/index.tsx` (TYPESCRIPT) | Magnitude: 7.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 14, core_var_decl: 6, args: 5
- `packages/components/src/toolbar/toolbar-button/index.tsx` (TYPESCRIPT) | Magnitude: 18.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 77, structural_boundaries: 19, core_var_decl: 16, ui_framework: 9
- `packages/ui/src/icon-button/test/index.test.tsx` (TYPESCRIPT) | Magnitude: 91.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 87, core_var_decl: 25, design_snake_case: 24, structural_boundaries: 20
- `packages/components/src/validated-form-controls/test/select-control.tsx` (TYPESCRIPT) | Magnitude: 55.46 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 12, core_var_decl: 12, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/block-library/src/navigation-link/shared/use-enable-link-status-validation.js` (JAVASCRIPT) | Magnitude: 5.46 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 6, args: 2, doc: 2
- `packages/block-editor/src/components/block-list/block-invalid-warning.js` (JAVASCRIPT) | Magnitude: 22.68 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 108, core_var_decl: 22, structural_boundaries: 21, design_camel_case: 15
- `packages/editor/src/components/posts-per-page/index.js` (JAVASCRIPT) | Magnitude: 14.74 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 80, core_var_decl: 22, structural_boundaries: 18, design_camel_case: 11
- `packages/react-native-aztec/RNTAztecView.podspec` (RUBY) | Magnitude: 32.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 13, structural_boundaries: 2, io: 2
- `packages/editor/src/store/utils/test/notice-builder.js` (JAVASCRIPT) | Magnitude: 24.86 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 185, structural_boundaries: 10, args: 9, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/block-editor/src/layouts/flow.js` (JAVASCRIPT) | Magnitude: 60.32 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 69, branch: 16, structural_boundaries: 15, func_start: 8
- `packages/components/src/mobile/html-text-input/index.native.js` (JAVASCRIPT) | Magnitude: 43.74 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 128, core_var_decl: 28, structural_boundaries: 22, design_camel_case: 18
- `phpunit/block-supports/anchor-test.php` (PHP) | Magnitude: 30.48 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 151, structural_boundaries: 10, state_mutation: 8, doc: 6
- `packages/editor/src/components/error-boundary/index.native.js` (JAVASCRIPT) | Magnitude: 38.06 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 137, core_var_decl: 31, structural_boundaries: 22, design_camel_case: 17
- `packages/env/lib/runtime/index.js` (JAVASCRIPT) | Magnitude: 21.94 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 7, doc: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/components/src/mobile/link-settings/test/edit.native.js` (JAVASCRIPT) | Magnitude: 41.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 225, structural_boundaries: 53, concurrency: 27, args: 21
- `packages/notices/src/store/test/reducer.ts` (TYPESCRIPT) | Magnitude: 28.02 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 243, core_var_decl: 54, design_snake_case: 51, structural_boundaries: 29
- `packages/block-library/src/separator/edit.js` (JAVASCRIPT) | Magnitude: 20.02 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 59, core_var_decl: 16, structural_boundaries: 10, branch: 9
- `packages/core-data/src/hooks/use-query-select.ts` (TYPESCRIPT) | Magnitude: 29.8 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 62, structural_boundaries: 25, branch: 10, core_var_decl: 10
- `packages/components/src/color-picker/test/index.tsx` (TYPESCRIPT) | Magnitude: 137.12 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 382, test: 104, core_var_decl: 88, structural_boundaries: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/block-library/src/preformatted/save.js` (JAVASCRIPT) | Magnitude: 3.08 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 3, branch: 1, args: 1
- `packages/block-library/src/verse/save.js` (JAVASCRIPT) | Magnitude: 3.08 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 3, branch: 1, args: 1
- `packages/block-editor/src/components/block-controls/slot.native.js` (JAVASCRIPT) | Magnitude: 12.66 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 10, branch: 5, ui_framework: 3
- `test/unit/scripts/babel-transformer.js` (JAVASCRIPT) | Magnitude: 11.72 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 19, core_var_decl: 7, design_camel_case: 6, branch: 4
- `packages/customize-widgets/src/components/sidebar-block-editor/sidebar-editor-provider.js` (JAVASCRIPT) | Magnitude: 3.98 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 6, core_var_decl: 5, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/block-editor/src/hooks/layout.native.js` (JAVASCRIPT) | Magnitude: 15.2 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 4, structural_boundaries: 2, safety_bypasses: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/edit-widgets/src/blocks/widget-area/index.js` (JAVASCRIPT) | Magnitude: 4.72 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 4, api: 3, import: 3
- `packages/media-utils/src/utils/validate-mime-type-for-user.ts` (TYPESCRIPT) | Magnitude: 11.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 8, branch: 4, doc: 3
- `packages/upload-media/src/validate-mime-type-for-user.ts` (TYPESCRIPT) | Magnitude: 11.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 8, branch: 4, doc: 3
- `packages/editor/src/components/index.js` (JAVASCRIPT) | Magnitude: 107.96 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 92, api: 91, import: 89, branch: 83
- `packages/rich-text/src/hook/use-anchor.ts` (TYPESCRIPT) | Magnitude: 108.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 136, branch: 36, structural_boundaries: 30, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/react-native-bridge/ios/GutenbergWebFallback/GutenbergWebSingleBlockViewController.swift` (SWIFT) | Magnitude: 129.72 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 42, args: 31, func_start: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/e2e-tests/plugins/iframed-enqueue-block-assets/style.css` (CSS) | Magnitude: 0.63 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 3, indent_tabs: 3, doc: 1, globals: 1
- `packages/element/src/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, branch: 4
- `packages/editor/src/components/index.native.js` (JAVASCRIPT) | Magnitude: 23.68 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9, branch: 8
- `packages/dataviews/src/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7, import: 7, branch: 4
- `packages/dom/src/dom/index.js` (JAVASCRIPT) | Magnitude: 42.54 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 27, structural_boundaries: 27, api: 27, import: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib/experimental/kses-allowed-html.php` (PHP) | Magnitude: 9.74 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 6, state_mutation: 3, doc: 2
- `packages/viewport/src/store/selectors.js` (JAVASCRIPT) | Magnitude: 8.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 4, structural_boundaries: 2, branch: 1, args: 1
- `packages/block-library/src/pullquote/edit.js` (JAVASCRIPT) | Magnitude: 11.98 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 71, core_var_decl: 21, structural_boundaries: 13, design_camel_case: 11
- `packages/block-editor/src/components/list-view/style.scss` (CSS) | Magnitude: 1.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 405, class_start: 128, closures: 58, branch: 18
- `packages/block-library/src/post-featured-image/editor.scss` (CSS) | Magnitude: 0.86 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 101, class_start: 18, closures: 13, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/block-editor/src/hooks/duotone.js` (JAVASCRIPT) | Magnitude: 123.76 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 245, branch: 59, core_var_decl: 52, structural_boundaries: 48
- `lib/experimental/navigation-theme-opt-in.php` (PHP) | Magnitude: 193.18 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 134, branch: 37, state_mutation: 35, structural_boundaries: 24
- `bin/generate-php-sync-issue.mjs` (JAVASCRIPT) | Magnitude: 348.96 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 284, branch: 66, structural_boundaries: 66, core_var_decl: 61
- `packages/block-editor/src/components/use-block-commands/index.js` (JAVASCRIPT) | Magnitude: 105.22 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 277, structural_boundaries: 43, branch: 34, core_var_decl: 29
- `packages/components/src/box-control/input-control.tsx` (TYPESCRIPT) | Magnitude: 170.66 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 252, core_var_decl: 71, branch: 61, design_camel_case: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/components/src/gradient-picker/index.tsx` (TYPESCRIPT) | Magnitude: 41.7 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 157, core_var_decl: 45, structural_boundaries: 27, design_camel_case: 22
- `packages/components/src/radio-group/radio.tsx` (TYPESCRIPT) | Magnitude: 14.66 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 12, core_var_decl: 9, import: 7
- `routes/styles/canvas.tsx` (TYPESCRIPT) | Magnitude: 8.36 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 9, core_var_decl: 7, design_snake_case: 6
- `packages/components/src/angle-picker-control/index.tsx` (TYPESCRIPT) | Magnitude: 25.12 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 20, core_var_decl: 18, import: 12
- `packages/components/src/navigator/stories/index.story.tsx` (TYPESCRIPT) | Magnitude: 13.16 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 150, core_var_decl: 23, ui_framework: 22, generics: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/env/lib/runtime/docker/wordpress.js` (JAVASCRIPT) | Magnitude: 211.4 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 152, branch: 39, structural_boundaries: 27, state_mutation: 23
- `packages/env/lib/config/parse-config.js` (JAVASCRIPT) | Magnitude: 322.22 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 361, branch: 62, state_mutation: 41, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/data/src/controls.ts` (TYPESCRIPT) | Magnitude: 20.88 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 66, structural_boundaries: 27, args: 11, core_var_decl: 9
- `packages/eslint-plugin/rules/__tests__/no-base-control-with-label-without-id.js` (JAVASCRIPT) | Magnitude: 16.5 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 69, core_var_decl: 12, design_snake_case: 11, ui_framework: 7
- `packages/interactivity/src/proxies/test/store-proxy.ts` (TYPESCRIPT) | Magnitude: 16.78 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 94, core_var_decl: 24, structural_boundaries: 22, design_snake_case: 17
- `packages/block-editor/src/components/inserter/test/fixtures/index.js` (JAVASCRIPT) | Magnitude: 0.03 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 116, structural_boundaries: 13, api: 13, core_var_decl: 12
- `packages/interactivity/src/proxies/signals.ts` (TYPESCRIPT) | Magnitude: 56.96 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 69, structural_boundaries: 21, branch: 18, doc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/components/src/mobile/color-settings/utils.native.js` (JAVASCRIPT) | Magnitude: 11.98 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 7, branch: 5, core_var_decl: 4
- `packages/block-editor/src/components/block-switcher/block-transformations-menu.js` (JAVASCRIPT) | Magnitude: 43.4 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 135, core_var_decl: 33, structural_boundaries: 26, design_camel_case: 21
- `packages/block-editor/src/components/rich-text/format-edit.js` (JAVASCRIPT) | Magnitude: 18.98 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 48, core_var_decl: 20, design_camel_case: 14, structural_boundaries: 12
- `packages/components/src/mobile/picker/index.ios.js` (JAVASCRIPT) | Magnitude: 16.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 64, structural_boundaries: 18, core_var_decl: 12, design_camel_case: 8
- `packages/block-editor/src/components/inserter/quick-inserter.js` (JAVASCRIPT) | Magnitude: 19.9 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 95, core_var_decl: 27, design_camel_case: 19, structural_boundaries: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/core-data/src/resolvers.js` -> Churn: **64.5%** | Cog Load: 60.8533% | Debt: 7.949%
- `packages/sync/src/providers/http-polling/polling-manager.ts` -> Churn: **60.8%** | Cog Load: 55.254% | Debt: 0.0%
- `lib/experimental/connectors/default-connectors.php` -> Churn: **59.76%** | Cog Load: 51.0867% | Debt: 0.0%
- `routes/connectors-home/default-connectors.tsx` -> Churn: **57.5%** | Cog Load: 63.13% | Debt: 0.0%
- `.github/workflows/end2end-test.yml` -> Churn: **50.43%** | Cog Load: 4.3307% | Debt: 70.1762%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/global-styles-ui/src/font-library/lib/lib-font.browser.js` -> **Riad Benguella** (100.0% isolated ownership) | Magnitude: 2520.32
- `lib/block-supports/layout.php` -> **tellthemachines** (83.3% isolated ownership) | Magnitude: 1183.28
- `test/e2e/specs/editor/collaboration/collaboration-refresh.spec.ts` -> **Max Schmeling** (100.0% isolated ownership) | Magnitude: 1131.72
- `packages/react-native-editor/__device-tests__/pages/editor-page.js` -> **Ella** (100.0% isolated ownership) | Magnitude: 900.62
- `test/performance/specs/post-editor.spec.js` -> **Jorge Costa** (100.0% isolated ownership) | Magnitude: 735.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/block-library/src/index.js` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 87.8897%)
- `packages/block-editor/src/components/rich-text/native/index.native.js` -> **Severity: 0.019** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/block-editor/src/components/block-preview/index.js` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 74.8986%)
- `packages/editor/src/store/private-actions.js` -> **Severity: 0.013** (Bridge: 0.0002 * Flux: 74.6003%)
- `packages/block-editor/src/hooks/utils.js` -> **Severity: 0.011** (Bridge: 0.0003 * Flux: 37.4442%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/components/src/context/context-connect.ts` -> **Severity: 1.118** (Embedded: 0.0167 * Error Risk: 66.8421%)
- `packages/components/src/context/wordpress-component.ts` -> **Severity: 0.931** (Embedded: 0.0181 * Error Risk: 51.2854%)
- `packages/components/src/context/use-context-system.js` -> **Severity: 0.916** (Embedded: 0.0186 * Error Risk: 49.2858%)
- `packages/block-editor/src/store/actions.js` -> **Severity: 0.871** (Embedded: 0.0176 * Error Risk: 49.4478%)
- `packages/block-editor/src/store/selectors.js` -> **Severity: 0.867** (Embedded: 0.0187 * Error Risk: 46.299%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/rich-text/src/test/helpers/index.js` -> **Severity: 369.575** (Blast Radius: 3.86 * Doc Risk: 95.7447%)
- `packages/e2e-test-utils-playwright/src/editor/index.ts` -> **Severity: 242.1** (Blast Radius: 2.421 * Doc Risk: 100.0%)
- `packages/e2e-test-utils-playwright/src/request-utils/index.ts` -> **Severity: 161.1** (Blast Radius: 1.611 * Doc Risk: 100.0%)
- `packages/block-library/src/utils/hooks.js` -> **Severity: 150.309** (Blast Radius: 2.362 * Doc Risk: 63.6364%)
- `packages/block-editor/src/components/rich-text/native/index.native.js` -> **Severity: 146.197** (Blast Radius: 1.541 * Doc Risk: 94.8718%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 721 literal sites + 57 sites through wrappers = 778
- **`panics_and_aborts`:** 802 literal sites + 8 sites through wrappers = 810

- `info` (function, debug_prints, primitive): 46 call sites in 6 files -- `packages/create-block/lib/log.js`
- `code` (function, debug_prints, primitive): 10 call sites in 1 files -- `packages/create-block/lib/log.js`
- `throwNotInScope` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/interactivity/src/scopes.ts`
- `throwSpxModeError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/env/lib/parse-spx-mode.js`
- `throwXdebugModeError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/env/lib/parse-xdebug-mode.js`
- `reportSuccessManual` (function, debug_prints, primitive): 1 call sites in 1 files -- `bin/cherry-pick.mjs`
- `throwsError` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/block-editor/src/components/link-control/test/index.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 57045 call pairs -- scoped 18.2%, unique 0.8%, ambiguous 27.0%, external 54.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 32555 | 20.0% | 0.0% | 34.0% | 46.0% |
| typescript | 13433 | 17.8% | 0.0% | 25.8% | 56.3% |
| php | 8989 | 11.0% | 4.5% | 7.8% | 76.7% |
| java | 1139 | 22.7% | 1.6% | 4.2% | 71.6% |
| swift | 517 | 28.4% | 3.7% | 14.7% | 53.2% |
| kotlin | 168 | 14.3% | 0.0% | 8.3% | 77.4% |
| shell | 127 | 33.9% | 0.0% | 0.0% | 66.1% |
| ruby | 81 | 0.0% | 0.0% | 0.0% | 100.0% |
| objective-c | 15 | 6.7% | 0.0% | 0.0% | 93.3% |
| groovy | 11 | 27.3% | 0.0% | 0.0% | 72.7% |

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
