# ARCHITECTURAL_BRIEF: material-ui
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mui/material-ui.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 33892 analyzed artifact(s), 402153 LOC.
- **Load-bearing artifact:** `packages/mui-icons-material/lib/utils/createSvgIcon.mjs` -- 9689 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/bundling/scripts/fixtureTemplateValues.js` -- pulls in 151 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 41018 |
| Analyzed Artifacts (Scanned) | 33892 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7126 |
| Total LOC | 402153 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 82.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5485 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3771 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.571 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 435 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 21495 | 334306 | 63.4% |
| XML | 10610 | 1243 | 31.3% |
| TYPESCRIPT | 1522 | 63991 | 4.5% |
| JSON | 96 | 1329 | 0.3% |
| MARKDOWN | 62 | 0 | 0.2% |
| PLAINTEXT | 53 | 1 | 0.2% |
| CSS | 40 | 859 | 0.1% |
| HTML | 12 | 379 | 0.0% |
| YAML | 2 | 45 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `9.622`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +9.62; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 57%, Declarative / Non-Code 38%, Parameter Forwarders Files 1%, Large Core Modules (2) 1%, Callbacks & Closures Files 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32534 | 96.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 1243 | 3.7% |
| Static: Literature & Documentation | 114 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7126*

**Composition by Extension & Reason:**
- `.js`: 1395x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 872x Excluded (Saturation: Line 12 exceeds 500 chars), 81x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.mjs`: 873x Excluded (Saturation: Line 6 exceeds 500 chars), 81x Excluded (Saturation: Line 9 exceeds 500 chars), 40x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.tsx`: 988x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 58 exceeds 500 chars)
- `.png`: 903x Excluded (Explicitly Denied Extension: '.png')
- `.preview`: 397x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 320x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31075 LOC exceeds safe regex boundaries)
- `.json`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 53809 LOC exceeds safe regex boundaries)
- `.jpg`: 182x Excluded (Explicitly Denied Extension: '.jpg')
- `.svg`: 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 86 LOC)
- `.mp4`: 59x Excluded (Explicitly Denied Extension: '.mp4')
- `.jpeg`: 44x Excluded (Explicitly Denied Extension: '.jpeg')
- `no_extension`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 20x Excluded (Explicitly Denied Extension: '.woff2')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.2 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 22.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.3 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 55.6 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1150 | 591 | 0 | `packages/mui-material/src/index.d.ts` |
| cleanup | 86 | 54 | 0 | `packages-internal/core-docs/src/CodeCopy/CodeCopy.tsx` |
| guards | 4341 | 610 | 0 | `packages/mui-codemod/src/util/migrateToVariants.js` |
| danger | 11349 | 10212 | 1 | `packages/mui-styled-engine-sc/src/index.d.ts` |
| concurrency | 1888 | 181 | 0 | `packages/mui-material/src/ButtonBase/ButtonBase.test.js` |
| connectivity | 36139 | 21874 | 2 | `packages/mui-material/src/index.js` |
| io | 1091 | 302 | 0 | `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 8 | 0 | `packages-internal/core-docs/src/DocsApp/serviceWorker.ts` |
| time | 79 | 55 | 0 | `packages-internal/core-docs/src/Ad/Ad.tsx` |
| serialization | 132 | 30 | 0 | `packages/mui-system/src/cssVars/useCurrentColorScheme.test.js` |
| regex | 954 | 250 | 0 | `packages-internal/markdown/parseMarkdown.mjs` |
| events | 768 | 201 | 0 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |
| tests | 13530 | 454 | 0 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |
| docs | 5863 | 955 | 0 | `packages/mui-material/src/Autocomplete/Autocomplete.js` |
| debt | 669 | 294 | 0 | `packages/mui-material/src/Slider/Slider.test.js` |
| mutation | 79465 | 12186 | 5 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |
| dead_code | 1012 | 577 | 0 | `test/integration/material-ui/components.spec.tsx` |
| credential | 0 | 0 | 0 | - |
| threat | 9822 | 9744 | 1 | `packages/mui-material/src/Tabs/Tabs.test.js` |
| ml_ai | 41 | 16 | 0 | `packages-internal/core-docs/src/Ad/Ad.tsx` |
| ui | 30837 | 20541 | 1 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` (Hits: 55)
- `packages-internal/markdown/loader.mjs` (Hits: 51)
- `packages-internal/scripts/generate-llms-txt/test/processComponent.test.ts` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **createSvgIcon.mjs** (`packages/mui-icons-material/lib/utils/createSvgIcon.mjs`) — 9689 inbound connections
2. **styles.css** (`packages/mui-material-pigment-css/src/styles.css`) — 401 inbound connections
3. **generateUtilityClass.ts** (`packages/mui-utils/src/generateUtilityClass/generateUtilityClass.ts`) — 145 inbound connections
4. **composeClasses.ts** (`packages/mui-utils/src/composeClasses/composeClasses.ts`) — 137 inbound connections
5. **generateUtilityClasses.ts** (`packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts`) — 137 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fixtureTemplateValues.js** (`test/bundling/scripts/fixtureTemplateValues.js`) — 151 outbound dependencies
2. **index.js** (`packages/mui-material/src/index.js`) — 142 outbound dependencies
3. **index.d.ts** (`packages/mui-material/src/index.d.ts`) — 141 outbound dependencies
4. **props.ts** (`packages/mui-material/src/styles/props.ts`) — 118 outbound dependencies
5. **overrides.ts** (`packages/mui-material/src/styles/overrides.ts`) — 117 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `useAutocomplete` **(Defensive Guards)** (@ `packages/mui-material/src/useAutocomplete/useAutocomplete.js`) -> Impact: **514.9** | LOC: 1248
- `sxV6` **(Many-Argument Workhorses)** (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **316.7** | LOC: 494
  * *Intent:* /** */
- `getThemedComponents` **(I/O & Config Routines)** (@ `packages-internal/core-docs/src/branding/brandingTheme.ts`) -> Impact: **302.5** | LOC: 1170
- `transformer` **(Many-Argument Workhorses)** (@ `packages/mui-codemod/src/v5.0.0/jss-to-styled.js`) -> Impact: **284.0** | LOC: 640
  * *Intent:* /** */
- `migrateToVariants` **(Defensive Guards)** (@ `packages/mui-codemod/src/util/migrateToVariants.js`) -> Impact: **265.8** | LOC: 500
  * *Intent:* /** * */
- `createThemeWithVars` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/styles/createThemeWithVars.js`) -> Impact: **235.6** | LOC: 866
  * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` based on the `defaultColorScheme`. * This is better s...
- `useSlider` **(Compute Cores)** (@ `packages/mui-material/src/Slider/useSlider.ts`) -> Impact: **227.1** | LOC: 638
- `SelectInput` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/Select/SelectInput.js`) -> Impact: **217.4** | LOC: 676
  * *Intent:* /** */
- `Tabs` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/Tabs/Tabs.js`) -> Impact: **199.5** | LOC: 629
- `SwipeableDrawer` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js`) -> Impact: **189.7** | LOC: 504

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/mui-icons-material/lib` | 19379 | 337188.16 | 9.66% | 0.0% |
| `packages/mui-icons-material/material-icons` | 10583 | 99614.04 | 0.0% | 0.0% |
| `__monolith__` | 24 | 5341.78 | 1.32% | 2.22% |
| `packages/mui-codemod/src/v5.0.0` | 142 | 3518.78 | 11.24% | 1.49% |
| `packages/mui-material/src/styles` | 83 | 2503.57 | 9.19% | 15.46% |
| `packages/mui-icons-material/legacy` | 139 | 1881.56 | 5.12% | 0.0% |
| `packages/mui-material/src/useAutocomplete` | 6 | 1409.13 | 11.53% | 21.64% |
| `packages-internal/api-docs-builder/ApiBuilders` | 2 | 1373.86 | 56.99% | 8.67% |
| `packages/mui-system/src/cssVars` | 18 | 1366.57 | 15.18% | 7.62% |
| `packages-internal/api-docs-builder/utils` | 24 | 1348.4 | 27.2% | 8.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/package.actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/v4.0.0/theme-spacing-api.test/actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/v4.0.0/theme-spacing-api.test/actual_destructured.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/v4.0.0/theme-spacing-api.test/expected.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages-internal/waterfall/Queue.mjs` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/all/deprecations-all.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/movePropIntoSlotProps.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/movePropIntoSlots.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/replaceComponentsWithSlots.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/integration/material-ui/components.spec.tsx` -> **42** Orphaned Functions | **0** Duplicates
- `packages/mui-system/src/colorManipulator/colorManipulator.d.ts` -> **18** Orphaned Functions | **0** Duplicates
- `packages/mui-material/src/styles/ThemeProviderWithVars.test.js` -> **7** Orphaned Functions | **6** Duplicates
- `packages/mui-system/src/cssVars/createCssVarsProvider.test.js` -> **2** Orphaned Functions | **10** Duplicates
- `packages/mui-codemod/src/v4.0.0/theme-spacing-api.test/actual.js` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36673` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/useAutocomplete/useAutocomplete.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1270.72 | **LOC:** 1331 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **6**; blast radius 0.152; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Connectivity (formerly Api Exposure) (52.1%), Complexity Load (formerly Cognitive Load) (51.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useAutocomplete` **(Defensive Guards)** (Impact: 514.9)
  * `handleKeyDown` **(Compute Cores)** (Impact: 111.4)
  * `isSameValue` **(Defensive Guards)** (Impact: 75.3)
  * `getOptionLabel` **(Defensive Guards)** (Impact: 65.6)
  * `selectNewValue` **(Defensive Guards)** (Impact: 40.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 338`, `structural_boundaries: 173`, `args: 73`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 113`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001098
  * `Imports (Out-Degree: 1):` setRef, useControlled, useEventCallback, useId, usePreviousProps, react
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 862.08 | **LOC:** 941 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.021; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotateComponentDefinition` **(Many-Argument Workhorses)** (Impact: 114.0)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Icons](ht...
  * `generateComponentApi` **(Many-Argument Workhorses)** (Impact: 90.6)
    * *Intent:* /** * - Build react component (specified filename) api by lookup at its definition (.d.ts or ts) * a...
  * `attachPropsTable` **(Defensive Guards)** (Impact: 78.6)
  * `generateApiPage` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `attachTable` **(Defensive Guards)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 138`, `args: 46`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 88`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 17`, `api: 12`, `concurrency: 17`, `import: 33`
* *Defense:* `safety: 43`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.021
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000106
  * `Imports (Out-Degree: 15):` $layoutConfigPath, $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/util/migrateToVariants.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 829.52 | **LOC:** 682 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.073; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.1%), Connectivity (formerly Api Exposure) (45.1%), Guard Balance (formerly Safety Score) (27.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `migrateToVariants` **(Defensive Guards)** (Impact: 265.8)
    * *Intent:* /** * */
  * `recurseObjectExpression` **(Defensive Guards)** (Impact: 102.9)
  * `replaceValue` **(Defensive Guards)** (Impact: 57.8)
  * `replaceValue` **(Defensive Guards)** (Impact: 37.5)
  * `buildProps` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* /** * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 87`, `args: 53`, `func_start: 26`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `api: 9`
* *Defense:* `safety: 129`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000159
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages-internal/core-docs/src/branding/brandingTheme.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 809.36 | **LOC:** 1592 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Connectivity (formerly Api Exposure) (44.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getThemedComponents` **(I/O & Config Routines)** (Impact: 302.5)
  * `root` **(Compute Cores)** (Impact: 119.4)
  * `root` **(Compute Cores)** (Impact: 96.9)
  * `root` **(Compute Cores)** (Impact: 58.5)
  * `root` **(I/O & Config Routines)** (Impact: 35.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 68`, `args: 31`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.8e-05
  * `Imports (Out-Degree: 1):` ArrowDropDownRounded, styles, themeCssVarsAugmentation, system
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 802.72 | **LOC:** 530 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.035; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (49.4%), Guard Balance (formerly Safety Score) (20.9%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 58.8235% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sxV6` **(Many-Argument Workhorses)** (Impact: 316.7)
    * *Intent:* /** */
  * `recurseObjectExpression` **(Defensive Guards)** (Impact: 167.3)
    * *Intent:* /** * */
  * `buildStyle` **(Defensive Guards)** (Impact: 52.4)
  * `replaceValue` **(Defensive Guards)** (Impact: 34.5)
  * `replaceRoot` **(Defensive Guards)** (Impact: 31.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 43`, `args: 30`, `func_start: 13`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 110`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.9e-05
  * `Imports (Out-Degree: 2):` getReturnExpression, migrateToVariants, jscodeshift
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Slider/useSlider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 715.3 | **LOC:** 855 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.043; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (69.4%), Connectivity (formerly Api Exposure) (29.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useSlider` **(Compute Cores)** (Impact: 227.1)
  * `createHandleHiddenInputKeyDown` **(Compute Cores)** (Impact: 57.5)
  * `getFingerNewValue` **(Compute Cores)** (Impact: 57.4)
  * `changeValue` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `createHandleMouseDown` **(Defensive Guards)** (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 112`, `args: 55`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 22`, `doc: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000796
  * `Imports (Out-Degree: 7):` areArraysEqual, types, useSlider.types, clamp, extractEventHandlers, isFocusVisible, ownerDocument, useControlled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-styled.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 611.26 | **LOC:** 647 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.022; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.3%), Complexity Load (formerly Cognitive Load) (47.8%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 43.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformer` **(Many-Argument Workhorses)** (Impact: 284.0)
    * *Intent:* /** */
  * `convertToStyledArg` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* /** * */
  * `getRootClassKeys` **(Defensive Guards)** (Impact: 17.6)
  * `getPrefix` **(Defensive Guards)** (Impact: 15.9)
    * *Intent:* /** * */
  * `getReturnStatement` **(Defensive Guards)** (Impact: 15.8)
    * *Intent:* /** * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 76`, `args: 51`, `func_start: 13`
* *Risk/State:* `state_mutation: 62`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 1`
* *Defense:* `safety: 68`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.9e-05
  * `Imports (Out-Degree: 0):` jscodeshift, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 521.9 | **LOC:** 777 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **15**; blast radius 0.073; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (43.8%), Connectivity (formerly Api Exposure) (28.3%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SwipeableDrawer` **(Many-Argument Workhorses)** (Impact: 189.7)
  * `startMaybeSwiping` **(Many-Argument Workhorses)** (Impact: 131.1)
  * `getDomTreeShapes` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /** */
  * `computeHasNativeHandler` **(Defensive Guards)** (Impact: 14.6)
    * *Intent:* /** */
  * `getTranslate` **(Parameter Forwarders)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 62`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 15`
* *Defense:* `safety: 27`, `doc: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000806
  * `Imports (Out-Degree: 9):` DefaultPropsProvider, Drawer, NoSsr, utils, utils, ownerDocument, ownerWindow, useEnhancedEffect...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 511.78 | **LOC:** 513 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotateHookDefinition` **(Many-Argument Workhorses)** (Impact: 119.8)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Button](h...
  * `attachTranslations` **(Defensive Guards)** (Impact: 43.5)
  * `attachTable` **(Defensive Guards)** (Impact: 43.0)
  * `ExportNamedDeclaration` **(Defensive Guards)** (Impact: 38.5)
  * `generateHookApi` **(Many-Argument Workhorses)** (Impact: 33.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 83`, `args: 31`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 15`, `api: 5`, `concurrency: 11`, `import: 19`
* *Defense:* `safety: 24`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 9.7e-05
  * `Imports (Out-Degree: 8):` $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types, createTypeScriptProject...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Select/SelectInput.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 495.92 | **LOC:** 759 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.2%)
- **Documentation Coverage:** 86.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SelectInput` **(Many-Argument Workhorses)** (Impact: 217.4)
    * *Intent:* /** */
  * `onKeyUp` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `handleBlur` **(Compute Cores)** (Impact: 30.4)
  * `handleItemClick` **(Defensive Guards)** (Impact: 19.4)
  * `focus` **(Callbacks & Closures)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 76`, `args: 33`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 18`
* *Defense:* `safety: 32`, `doc: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001345
  * `Imports (Out-Degree: 11):` utils, Menu, NativeSelectInput, slotShouldForwardProp, ownerDocument, useControlled, useForkRef, zero-styled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tabs/Tabs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 493.8 | **LOC:** 1017 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **24**; blast radius 0.209; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%), Guard Balance (formerly Safety Score) (47.8%), Connectivity (formerly Api Exposure) (41.7%)
- **Documentation Coverage:** 94.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tabs` **(Many-Argument Workhorses)** (Impact: 199.5)
  * `getTabsMeta` **(I/O & Config Routines)** (Impact: 35.5)
  * `getConditionalElements` **(I/O & Config Routines)** (Impact: 21.8)
  * `handleScrollButtonEnd` **(Defensive Guards)** (Impact: 21.7)
  * `handleMutation` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 100`, `args: 50`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `import: 24`
* *Defense:* `safety: 42`, `doc: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.209
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001343
  * `Imports (Out-Degree: 17):` DefaultPropsProvider, TabScrollButton, animate, debounce, getActiveElement, isLayoutSupported, memoTheme, ownerDocument...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-tss-react.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 480.74 | **LOC:** 491 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.022; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.1%), Complexity Load (formerly Cognitive Load) (67.6%), Debt Markers (formerly Tech Debt) (14.1%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformer` **(Many-Argument Workhorses)** (Impact: 125.0)
    * *Intent:* /** */
  * `transformStylesExpression` **(Many-Argument Workhorses)** (Impact: 96.2)
  * `transformNestedKeys` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `addCommentsToNode` **(State Mutators)** (Impact: 8.5)
  * `addCommentsToDeclaration` **(Defensive Guards)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 59`, `args: 36`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 74`, `planned_debt: 5`
* *Architecture:* `api: 1`
* *Defense:* `safety: 55`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.9e-05
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 460.64 | **LOC:** 532 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.8%), Guard Balance (formerly Safety Score) (75.7%), Connectivity (formerly Api Exposure) (44.7%), Complexity Load (formerly Cognitive Load) (22.7%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createBabelPlugin` **(Compute Cores)** (Impact: 113.6)
  * `getUsedProps` **(Compute Cores)** (Impact: 46.7)
    * *Intent:* /** * Gets used props from path */
  * `enter` **(Compute Cores)** (Impact: 44.4)
  * `getUsedPropsInternal` **(Compute Cores)** (Impact: 38.3)
  * `VariableDeclarator` **(Compute Cores)** (Impact: 27.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 52`, `args: 29`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 20`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `io: 55`, `api: 9`, `import: 6`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.9e-05
  * `Imports (Out-Degree: 2):` generatePropTypes, models, core, types, node:crypto, prop-types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tooltip/Tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 450.18 | **LOC:** 935 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **21**; blast radius 0.198; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (34.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.9%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tooltip` **(Many-Argument Workhorses)** (Impact: 146.2)
  * `handleMouseMove` **(Compute Cores)** (Impact: 50.9)
  * `handleBlur` **(Defensive Guards)** (Impact: 15.2)
  * `handleMouseOver` **(Defensive Guards)** (Impact: 13.9)
  * `overridesResolver` **(Compute Cores)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 85`, `args: 52`, `func_start: 33`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 4`
* *Architecture:* `api: 4`, `import: 21`
* *Defense:* `safety: 21`, `doc: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.198
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001355
  * `Imports (Out-Degree: 16):` DefaultPropsProvider, Grow, Popper, capitalize, memoTheme, useControlled, useEventCallback, useForkRef...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/styles/createThemeWithVars.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 391.02 | **LOC:** 993 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **12**; blast radius 4.158; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.8%), Guard Balance (formerly Safety Score) (49.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.1%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createThemeWithVars` **(Many-Argument Workhorses)** (Impact: 235.6)
    * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` bas...
  * `attachColorScheme` **(Defensive Guards)** (Impact: 26.0)
  * `colorMix` **(Defensive Guards)** (Impact: 10.8)
  * `getSpacingVal` **(Defensive Guards)** (Impact: 7.7)
  * `setColorChannel` **(State Mutators)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 52`, `args: 28`, `func_start: 15`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.158
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.06438
  * `Imports (Out-Degree: 10):` createColorScheme, createGetSelector, createPalette, createThemeNoVars, shouldSkipGeneratingVar, stringifyTheme, system, colorManipulator...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/getPropTypesFromFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 352.24 | **LOC:** 751 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.5%), Mutation Surface (formerly State Flux) (55.3%), Connectivity (formerly Api Exposure) (25.5%), Complexity Load (formerly Cognitive Load) (16.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkType` **(Compute Cores)** (Impact: 110.8)
  * `checkSymbol` **(Compute Cores)** (Impact: 48.9)
  * `getElementTypeName` **(Compute Cores)** (Impact: 40.6)
    * *Intent:* // Helper to check if a type node is a React element type reference
  * `getPropTypesFromFile` **(Compute Cores)** (Impact: 21.0)
  * `getType` **(Compute Cores)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 166`, `args: 40`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 7`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.023
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.9e-05
  * `Imports (Out-Degree: 2):` createType, models, internal-docs-utils, doctrine, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages-internal/markdown/loader.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 347.64 | **LOC:** 720 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (59.8%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `demoLoader` **(I/O & Config Routines)** (Impact: 75.0)
    * *Intent:* */ /** */
  * `detectRelativeImports` **(Many-Argument Workhorses)** (Impact: 29.3)
    * *Intent:* /** */
  * `findComponents` **(Callbacks & Closures)** (Impact: 11.2)
    * *Intent:* /** */ /** */
  * `updateRelativeModules` **(Defensive Guards)** (Impact: 8.7)
    * *Intent:* /** * Inserts the moduleData into the relativeModules object */
  * `moduleIDToJSIdentifier` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 100`, `args: 38`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 51`, `api: 5`, `concurrency: 27`, `import: 11`
* *Defense:* `safety: 33`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` $moduleID, extractImports.mjs, prepareMarkdown.mjs, fs, path, webpack
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-utils/src/useRovingTabIndex/useRovingTabIndex.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 342.36 | **LOC:** 816 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.1%), Guard Balance (formerly Safety Score) (54.2%), Connectivity (formerly Api Exposure) (41.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useRovingTabIndexRoot` **(Compute Cores)** (Impact: 64.4)
    * *Intent:* /** * Provides roving tab index behavior for a composite container and its focusable children. * Thi...
  * `onKeyDown` **(Compute Cores)** (Impact: 38.1)
  * `getNextActiveItem` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* * Walks the item snapshot to find the next focusable item in the requested direction. * * This is th...
  * `useRovingTabIndexItem` **(Defensive Guards)** (Impact: 19.6)
  * `getNextIndex` **(Many-Argument Workhorses)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 145`, `args: 62`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 17`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fastObjectShallowCompare, getActiveElement, ownerDocument, setRef, useEnhancedEffect, useEventCallback, useForkRef, RovingTabIndexContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/Tabs/Tabs.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 335.82 | **LOC:** 1753 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%), Guard Balance (formerly Safety Score) (26.3%), Complexity Load (formerly Cognitive Load) (16.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrapper` **(Callbacks & Closures)** (Impact: 39.8)
  * `root` **(Callbacks & Closures)** (Impact: 6.9)
  * `startScrollButtonIcon` **(Callbacks & Closures)** (Impact: 6.8)
  * `handleChange` **(Callbacks & Closures)** (Impact: 5.6)
  * `getBoundingClientRect` **(Callbacks & Closures)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Concurrency (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 258`, `args: 173`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 26`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 112`, `import: 11`
* *Defense:* `safety: 4`, `test: 300`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` describeConformance, capitalize, internal-test-utils, SvgIcon, Tab, Tabs, styles, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-system/src/createStyled/createStyled.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 333.28 | **LOC:** 351 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **8**; blast radius 0.078; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (65.4%), Connectivity (formerly Api Exposure) (50.2%), Guard Balance (formerly Safety Score) (48.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStyled` **(Defensive Guards)** (Impact: 67.5)
  * `processStyleVariants` **(Defensive Guards)** (Impact: 39.8)
  * `styled` **(Defensive Guards)** (Impact: 28.6)
  * `processStyle` **(Defensive Guards)** (Impact: 27.8)
  * `shallowLayer` **(Defensive Guards)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 55`, `args: 23`, `func_start: 19`
* *Risk/State:* `state_mutation: 28`, `dead_code: 3`, `planned_debt: 5`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000354
  * `Imports (Out-Degree: 5):` createTheme, preprocessStyles, styleFunctionSx, styled-engine, capitalize, deepmerge, getDisplayName, isObjectEmpty
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/buildLlmsDocs/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 330.64 | **LOC:** 622 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (75.4%), Concurrency Surface (formerly Concurrency) (68.4%), Complexity Load (formerly Cognitive Load) (48.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findNonComponentMarkdownFiles` **(Many-Argument Workhorses)** (Impact: 151.8)
    * *Intent:* /** * Find all non-component markdown files from specified folders */
  * `findComponentsToProcess` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* /** * Find all components using the API docs builder infrastructure */
  * `extractMarkdownInfo` **(Defensive Guards)** (Impact: 17.1)
    * *Intent:* /** * Extract title and description from markdown content */
  * `builder` **(Defensive Guards)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 59`, `args: 16`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`
* *Architecture:* `io: 39`, `api: 1`, `concurrency: 6`, `import: 12`
* *Defense:* `safety: 13`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` api-docs-builder, findComponents, findPagesMarkdown, internal-markdown, generate-llms-txt, string, fs, node:url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/Autocomplete/Autocomplete.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 313.38 | **LOC:** 1210 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **23**; blast radius 0.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.9%), Connectivity (formerly Api Exposure) (38.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%), Mutation Surface (formerly State Flux) (19.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Autocomplete` **(Many-Argument Workhorses)** (Impact: 90.7)
  * `onMouseDown` **(I/O & Config Routines)** (Impact: 47.2)
  * `overridesResolver` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `getCustomizedItemProps` **(Compute Cores)** (Impact: 19.1)
  * `useUtilityClasses` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 63`, `args: 24`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 23`
* *Defense:* `safety: 14`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.001206
  * `Imports (Out-Degree: 18):` Chip, DefaultPropsProvider, filledInputClasses, IconButton, inputClasses, inputBaseClasses, ListSubheader, outlinedInputClasses...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/InputBase/InputBase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 307.06 | **LOC:** 806 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **19**; blast radius 0.278; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.4%), Connectivity (formerly Api Exposure) (46.5%), Mutation Surface (formerly State Flux) (23.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.7%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InputBase` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* /** * `InputBase` contains as few styles as possible. * It aims to be a simple building block for cr...
  * `useUtilityClasses` **(Compute Cores)** (Impact: 30.1)
  * `handleAutoFill` **(I/O & Config Routines)** (Impact: 27.4)
  * `rootOverridesResolver` **(Defensive Guards)** (Impact: 18.2)
  * `handleClick` **(Defensive Guards)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 55`, `args: 23`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 15`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002322
  * `Imports (Out-Degree: 12):` DefaultPropsProvider, FormControlContext, formControlState, useFormControl, TextareaAutosize, capitalize, memoTheme, useEnhancedEffect...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v9.0.0/system-props/removeSystemProps.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 301.66 | **LOC:** 320 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.015; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (38.2%), Complexity Load (formerly Cognitive Load) (37.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.2%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `removeSystemProps` **(Defensive Guards)** (Impact: 138.6)
    * *Intent:* /** */
  * `name` **(Defensive Guards)** (Impact: 61.9)
  * `matcher` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* // Same as Typography but keep color="inherit" as a Link component prop (controls underline behavior...
  * `matcher` **(Defensive Guards)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 18`, `args: 12`, `func_start: 4`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1`
* *Defense:* `safety: 41`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 862.08
- `packages-internal/core-docs/src/branding/brandingTheme.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 809.36
- `packages/mui-material/src/Slider/useSlider.ts` -> **Albert Yu** (100.0% isolated ownership) | Magnitude: 715.3
- `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js` -> **Silviu Alexandru Avram** (100.0% isolated ownership) | Magnitude: 521.9
- `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 511.78

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/mui-material/src/styles/createTheme.ts` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 99.5526%)
- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 0.018** (Bridge: 0.0004 * Flux: 42.6845%)
- `packages/mui-system/src/styleFunctionSx/styleFunctionSx.js` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 99.9897%)
- `packages/mui-material/src/styles/createThemeNoVars.js` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 98.67%)
- `packages/mui-material/src/styles/createPalette.js` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 91.2597%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/mui-utils/src/composeClasses/composeClasses.ts` -> **Severity: 9.377** (Embedded: 0.111 * Error Risk: 84.5161%)
- `packages/mui-material/src/styles/createTheme.ts` -> **Severity: 6.793** (Embedded: 0.0807 * Error Risk: 84.1566%)
- `packages/mui-utils/src/deepmerge/deepmerge.ts` -> **Severity: 4.834** (Embedded: 0.0555 * Error Risk: 87.0344%)
- `packages/mui-material/src/styles/stringifyTheme.ts` -> **Severity: 4.825** (Embedded: 0.0535 * Error Risk: 90.1271%)
- `packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts` -> **Severity: 4.82** (Embedded: 0.0855 * Error Risk: 56.3934%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 10396.2** (Blast Radius: 103.962 * Doc Risk: 100.0%)
- `packages/mui-utils/src/generateUtilityClass/generateUtilityClass.ts` -> **Severity: 2223.3** (Blast Radius: 22.233 * Doc Risk: 100.0%)
- `packages/mui-material/src/SvgIcon/svgIconClasses.ts` -> **Severity: 2218.1** (Blast Radius: 22.181 * Doc Risk: 100.0%)
- `packages/mui-utils/src/ClassNameGenerator/ClassNameGenerator.ts` -> **Severity: 1953.6** (Blast Radius: 19.536 * Doc Risk: 100.0%)
- `packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts` -> **Severity: 1206.2** (Blast Radius: 12.062 * Doc Risk: 100.0%)

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
