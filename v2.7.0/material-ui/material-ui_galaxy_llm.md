# ARCHITECTURAL_BRIEF: material-ui
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mui/material-ui.git` |
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
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3771 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 22.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.3 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 55.6 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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
| threat | 9821 | 9743 | 1 | `packages/mui-material/src/Tabs/Tabs.test.js` |
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

- `useAutocomplete` (@ `packages/mui-material/src/useAutocomplete/useAutocomplete.js`) -> Impact: **514.9** | LOC: 1248
- `sxV6` (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **316.7** | LOC: 494
  * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
- `getThemedComponents` (@ `packages-internal/core-docs/src/branding/brandingTheme.ts`) -> Impact: **302.5** | LOC: 1170
- `transformer` (@ `packages/mui-codemod/src/v5.0.0/jss-to-styled.js`) -> Impact: **284.0** | LOC: 640
  * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
- `migrateToVariants` (@ `packages/mui-codemod/src/util/migrateToVariants.js`) -> Impact: **265.8** | LOC: 500
  * *Intent:* /** * * @param {import('jscodeshift').API['j']} j * @param {any[]} styles */
- `createThemeWithVars` (@ `packages/mui-material/src/styles/createThemeWithVars.js`) -> Impact: **235.6** | LOC: 866
  * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` based on the `defaultColorScheme`. * This is better s...
- `useSlider` (@ `packages/mui-material/src/Slider/useSlider.ts`) -> Impact: **227.1** | LOC: 638
- `SelectInput` (@ `packages/mui-material/src/Select/SelectInput.js`) -> Impact: **217.4** | LOC: 676
  * *Intent:* /** * @ignore - internal component. */
- `Tabs` (@ `packages/mui-material/src/Tabs/Tabs.js`) -> Impact: **199.5** | LOC: 629
- `SwipeableDrawer` (@ `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js`) -> Impact: **189.7** | LOC: 504

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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/mui-codemod/src/codemod.js` (JAVASCRIPT) -> Cumulative Risk: **677.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 165.4 | **LOC:** 216 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Concurrency (99.946%)
- **Heaviest Functions:** `runJscodeshiftTransform` (Impact: 30.5), `runPostcssTransform` (Impact: 16.4), `builder` (Impact: 14.9)

### 2. `packages-internal/api-docs-builder/buildApi.ts` (TYPESCRIPT) -> Cumulative Risk: **676.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 170.04 | **LOC:** 233 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (91.8439%)
- **Heaviest Functions:** `buildSingleProject` (Impact: 32.9), `buildApi` (Impact: 12.2), `removeOutdatedApiDocsTranslations` (Impact: 7.6)

### 3. `packages-internal/waterfall/Queue.mjs` (JAVASCRIPT) -> Cumulative Risk: **652.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 63.26 | **LOC:** 59 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.998%)
- **Heaviest Functions:** `wait` (Impact: 8.1), `constructor` (Impact: 3.7), `process` (Impact: 2.9)

### 4. `packages-internal/core-docs/src/CodeCopy/CodeCopy.tsx` (TYPESCRIPT) -> Cumulative Risk: **651.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 155.62 | **LOC:** 200 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9917%), Concurrency (82.287%), Verification (80.0%)
- **Heaviest Functions:** `InitCodeCopy` (Impact: 24.7), `CodeCopyProvider` (Impact: 16.2), `handleClick` (Impact: 12.3)

### 5. `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **649.91**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 862.08 | **LOC:** 941 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (99.994%), Spec Match (94.4444%), Concurrency (85.5142%), Safety Score (81.4701%)
- **Heaviest Functions:** `annotateComponentDefinition` (Impact: 114.0), `generateComponentApi` (Impact: 90.6), `attachPropsTable` (Impact: 78.6)

### 6. `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **649.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 511.78 | **LOC:** 513 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (99.9958%), Spec Match (90.9091%), Concurrency (88.1796%), Safety Score (80.8989%)
- **Heaviest Functions:** `annotateHookDefinition` (Impact: 119.8), `attachTranslations` (Impact: 43.5), `attachTable` (Impact: 43.0)

### 7. `packages-internal/waterfall/retry.mjs` (JAVASCRIPT) -> Cumulative Risk: **618.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 43.2 | **LOC:** 35 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.998%), State Flux (99.9254%)
- **Heaviest Functions:** `retry` (Impact: 8.4), `bail` (Impact: 8.3)

### 8. `packages-internal/api-docs-builder/utils/extractInfoFromEnum.ts` (TYPESCRIPT) -> Cumulative Risk: **609.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 68.44 | **LOC:** 71 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `extractInfoFromEnum` (Impact: 22.6), `parseProperty` (Impact: 6.7)

### 9. `packages-internal/api-docs-builder/utils/parseTest.ts` (TYPESCRIPT) -> Cumulative Risk: **594.78**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 106.82 | **LOC:** 194 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `parseTest` (Impact: 21.7), `getRefInstance` (Impact: 17.2), `findConformanceDescriptor` (Impact: 10.1)

### 10. `packages-internal/core-docs/src/Ad/Ad.tsx` (TYPESCRIPT) -> Cumulative Risk: **583.41**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 95.34 | **LOC:** 235 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.4244%), Safety Score (70.555%)
- **Heaviest Functions:** `Ad` (Impact: 34.1), `render` (Impact: 2.5), `PleaseDisableAdblock` (Impact: 2.0)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/useAutocomplete/useAutocomplete.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1270.72 | **LOC:** 1331 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (51.3807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `useAutocomplete` (Impact: 514.9)
  * `handleKeyDown` (Impact: 111.4)
  * `isSameValue` (Impact: 75.3)
  * `getOptionLabel` (Impact: 65.6)
  * `selectNewValue` (Impact: 40.3)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` setRef, useControlled, useEventCallback, useId, usePreviousProps, react
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 862.08 | **LOC:** 941 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.6824%), Tech Debt (8.3082%)
**Top Internal Functions/Classes:**
  * `annotateComponentDefinition` (Impact: 114.0)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Icons](ht...
  * `generateComponentApi` (Impact: 90.6)
    * *Intent:* /** * - Build react component (specified filename) api by lookup at its definition (.d.ts or ts) * a...
  * `attachPropsTable` (Impact: 78.6)
  * `generateApiPage` (Impact: 60.7)
  * `attachTable` (Impact: 46.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` $layoutConfigPath, $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/util/migrateToVariants.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 829.52 | **LOC:** 682 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.0594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `migrateToVariants` (Impact: 265.8)
    * *Intent:* /** * * @param {import('jscodeshift').API['j']} j * @param {any[]} styles */
  * `recurseObjectExpression` (Impact: 102.9)
  * `replaceValue` (Impact: 57.8)
  * `replaceValue` (Impact: 37.5)
  * `buildProps` (Impact: 26.8)
    * *Intent:* /** * * @param {import('jscodeshift').LogicalExpression | import('jscodeshift').BinaryExpression | i...
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages-internal/core-docs/src/branding/brandingTheme.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 809.36 | **LOC:** 1592 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.7056%), Tech Debt (8.1919%)
**Top Internal Functions/Classes:**
  * `getThemedComponents` (Impact: 302.5)
  * `root` (Impact: 119.4)
  * `root` (Impact: 96.9)
  * `root` (Impact: 58.5)
  * `root` (Impact: 35.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 68`, `args: 31`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ArrowDropDownRounded, styles, themeCssVarsAugmentation, system
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 802.72 | **LOC:** 530 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.4431%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sxV6` (Impact: 316.7)
    * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
  * `recurseObjectExpression` (Impact: 167.3)
    * *Intent:* /** * * @param {{ node: import('jscodeshift').Expression }} data */
  * `buildStyle` (Impact: 52.4)
  * `replaceValue` (Impact: 34.5)
  * `replaceRoot` (Impact: 31.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` getReturnExpression, migrateToVariants, jscodeshift
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Slider/useSlider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 715.3 | **LOC:** 855 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.42%), Tech Debt (8.3838%)
**Top Internal Functions/Classes:**
  * `useSlider` (Impact: 227.1)
  * `createHandleHiddenInputKeyDown` (Impact: 57.5)
  * `getFingerNewValue` (Impact: 57.4)
  * `changeValue` (Impact: 33.9)
  * `createHandleMouseDown` (Impact: 22.5)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` areArraysEqual, types, useSlider.types, clamp, extractEventHandlers, isFocusVisible, ownerDocument, useControlled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-styled.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 611.26 | **LOC:** 647 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8253%), Tech Debt (9.4804%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 284.0)
    * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
  * `convertToStyledArg` (Impact: 26.9)
    * *Intent:* /** * * @param {import('jscodeshift').ObjectExpression | import('jscodeshift').ArrowFunctionExpressi...
  * `getRootClassKeys` (Impact: 17.6)
  * `getPrefix` (Impact: 15.9)
    * *Intent:* /** * * @param {import('jscodeshift').CallExpression} withStylesCall */
  * `getReturnStatement` (Impact: 15.8)
    * *Intent:* /** * * @param {import('jscodeshift').ArrowFunctionExpression | import('jscodeshift').FunctionDeclar...
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift, path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 521.9 | **LOC:** 777 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.7954%), Tech Debt (9.3764%)
**Top Internal Functions/Classes:**
  * `SwipeableDrawer` (Impact: 189.7)
  * `startMaybeSwiping` (Impact: 131.1)
  * `getDomTreeShapes` (Impact: 18.7)
    * *Intent:* /** * @param {Element | null} element * @param {Element} rootNode */
  * `computeHasNativeHandler` (Impact: 14.6)
    * *Intent:* /** * @param {object} param0 * @param {ReturnType<getDomTreeShapes>} param0.domTreeShapes */
  * `getTranslate` (Impact: 4.9)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` DefaultPropsProvider, Drawer, NoSsr, utils, utils, ownerDocument, ownerWindow, useEnhancedEffect...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 511.78 | **LOC:** 513 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.2945%), Tech Debt (9.0327%)
**Top Internal Functions/Classes:**
  * `annotateHookDefinition` (Impact: 119.8)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Button](h...
  * `attachTranslations` (Impact: 43.5)
  * `attachTable` (Impact: 43.0)
  * `ExportNamedDeclaration` (Impact: 38.5)
  * `generateHookApi` (Impact: 33.4)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types, createTypeScriptProject...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Select/SelectInput.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 495.92 | **LOC:** 759 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.5234%), Tech Debt (10.1878%)
**Top Internal Functions/Classes:**
  * `SelectInput` (Impact: 217.4)
    * *Intent:* /** * @ignore - internal component. */
  * `onKeyUp` (Impact: 82.3)
  * `handleBlur` (Impact: 30.4)
  * `handleItemClick` (Impact: 19.4)
  * `focus` (Impact: 16.8)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` utils, Menu, NativeSelectInput, slotShouldForwardProp, ownerDocument, useControlled, useForkRef, zero-styled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tabs/Tabs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 493.8 | **LOC:** 1017 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (15.2094%), Tech Debt (22.8226%)
**Top Internal Functions/Classes:**
  * `Tabs` (Impact: 199.5)
  * `getTabsMeta` (Impact: 35.5)
  * `getConditionalElements` (Impact: 21.8)
  * `handleScrollButtonEnd` (Impact: 21.7)
  * `handleMutation` (Impact: 18.7)
    * *Intent:* /** * @type {MutationCallback} */
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` DefaultPropsProvider, TabScrollButton, animate, debounce, getActiveElement, isLayoutSupported, memoTheme, ownerDocument...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-tss-react.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 480.74 | **LOC:** 491 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.6424%), Tech Debt (14.1357%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 125.0)
    * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
  * `transformStylesExpression` (Impact: 96.2)
  * `transformNestedKeys` (Impact: 36.6)
  * `addCommentsToNode` (Impact: 8.5)
  * `addCommentsToDeclaration` (Impact: 3.8)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 460.64 | **LOC:** 532 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.6831%), Tech Debt (8.9829%)
**Top Internal Functions/Classes:**
  * `createBabelPlugin` (Impact: 113.6)
  * `getUsedProps` (Impact: 46.7)
    * *Intent:* /** * Gets used props from path * @param rootPath The path to search for uses of rootNode * @param r...
  * `enter` (Impact: 44.4)
  * `getUsedPropsInternal` (Impact: 38.3)
  * `VariableDeclarator` (Impact: 27.1)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` generatePropTypes, models, core, types, node:crypto, prop-types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tooltip/Tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 450.18 | **LOC:** 935 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.9976%), Tech Debt (10.7152%)
**Top Internal Functions/Classes:**
  * `Tooltip` (Impact: 146.2)
  * `handleMouseMove` (Impact: 50.9)
  * `handleBlur` (Impact: 15.2)
  * `handleMouseOver` (Impact: 13.9)
  * `overridesResolver` (Impact: 12.4)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` DefaultPropsProvider, Grow, Popper, capitalize, memoTheme, useControlled, useEventCallback, useForkRef...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/styles/createThemeWithVars.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 391.02 | **LOC:** 993 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (17.6705%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createThemeWithVars` (Impact: 235.6)
    * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` bas...
  * `attachColorScheme` (Impact: 26.0)
  * `colorMix` (Impact: 10.8)
  * `getSpacingVal` (Impact: 7.7)
  * `setColorChannel` (Impact: 7.5)
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
  * `Choke Point (Betweenness):` 0.000183 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` createColorScheme, createGetSelector, createPalette, createThemeNoVars, shouldSkipGeneratingVar, stringifyTheme, system, colorManipulator...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/getPropTypesFromFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 352.24 | **LOC:** 751 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.0297%), Tech Debt (8.5148%)
**Top Internal Functions/Classes:**
  * `checkType` (Impact: 110.8)
  * `checkSymbol` (Impact: 48.9)
  * `getElementTypeName` (Impact: 40.6)
    * *Intent:* // Helper to check if a type node is a React element type reference
  * `getPropTypesFromFile` (Impact: 21.0)
  * `getType` (Impact: 17.6)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` createType, models, internal-docs-utils, doctrine, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages-internal/markdown/loader.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 347.64 | **LOC:** 720 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.194%), Tech Debt (13.4752%)
**Top Internal Functions/Classes:**
  * `demoLoader` (Impact: 75.0)
    * *Intent:* * @property {string} [rawTailwind] * @property {string} [rawTailwindTS] * @property {string} [rawCSS...
  * `detectRelativeImports` (Impact: 29.3)
    * *Intent:* /** * @param {*} demoName * @param {*} moduleFilepath * @param {*} variant * @param {*} importModule...
  * `findComponents` (Impact: 11.2)
    * *Intent:* /** * @typedef {Object} Package * @property {string[]} paths * @property {string} productId */ /** *...
  * `updateRelativeModules` (Impact: 8.7)
    * *Intent:* /** * Inserts the moduleData into the relativeModules object * @param {string} demoName * @param {Mo...
  * `moduleIDToJSIdentifier` (Impact: 3.3)
    * *Intent:* /** * @param {string} moduleID * @example moduleIDToJSIdentifier('./Box.js') === '$$IndexJs' * @exam...
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 342.36 | **LOC:** 816 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.1126%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `useRovingTabIndexRoot` (Impact: 64.4)
    * *Intent:* /** * Provides roving tab index behavior for a composite container and its focusable children. * Thi...
  * `onKeyDown` (Impact: 38.1)
  * `getNextActiveItem` (Impact: 21.3)
    * *Intent:* * Walks the item snapshot to find the next focusable item in the requested direction. * * This is th...
  * `useRovingTabIndexItem` (Impact: 19.6)
  * `getNextIndex` (Impact: 14.4)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 335.82 | **LOC:** 1753 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (16.4472%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wrapper` (Impact: 39.8)
  * `root` (Impact: 6.9)
  * `startScrollButtonIcon` (Impact: 6.8)
  * `handleChange` (Impact: 5.6)
  * `getBoundingClientRect` (Impact: 5.1)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 333.28 | **LOC:** 351 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.4255%), Tech Debt (22.7853%)
**Top Internal Functions/Classes:**
  * `createStyled` (Impact: 67.5)
  * `processStyleVariants` (Impact: 39.8)
  * `styled` (Impact: 28.6)
  * `processStyle` (Impact: 27.8)
  * `shallowLayer` (Impact: 11.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` createTheme, preprocessStyles, styleFunctionSx, styled-engine, capitalize, deepmerge, getDisplayName, isObjectEmpty
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/buildLlmsDocs/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 330.64 | **LOC:** 622 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.9831%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findNonComponentMarkdownFiles` (Impact: 151.8)
    * *Intent:* /** * Find all non-component markdown files from specified folders */
  * `findComponentsToProcess` (Impact: 24.1)
    * *Intent:* /** * Find all components using the API docs builder infrastructure */
  * `extractMarkdownInfo` (Impact: 17.1)
    * *Intent:* /** * Extract title and description from markdown content */
  * `builder` (Impact: 6.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 313.38 | **LOC:** 1210 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (4.0562%), Tech Debt (8.7201%)
**Top Internal Functions/Classes:**
  * `Autocomplete` (Impact: 90.7)
  * `onMouseDown` (Impact: 47.2)
  * `overridesResolver` (Impact: 38.4)
  * `getCustomizedItemProps` (Impact: 19.1)
  * `useUtilityClasses` (Impact: 15.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Chip, DefaultPropsProvider, filledInputClasses, IconButton, inputClasses, inputBaseClasses, ListSubheader, outlinedInputClasses...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/InputBase/InputBase.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 307.06 | **LOC:** 806 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.3499%), Tech Debt (14.5417%)
**Top Internal Functions/Classes:**
  * `InputBase` (Impact: 117.3)
    * *Intent:* /** * `InputBase` contains as few styles as possible. * It aims to be a simple building block for cr...
  * `useUtilityClasses` (Impact: 30.1)
  * `handleAutoFill` (Impact: 27.4)
  * `rootOverridesResolver` (Impact: 18.2)
  * `handleClick` (Impact: 17.6)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` DefaultPropsProvider, FormControlContext, formControlState, useFormControl, TextareaAutosize, capitalize, memoTheme, useEnhancedEffect...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v9.0.0/system-props/removeSystemProps.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 301.66 | **LOC:** 320 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.3264%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `removeSystemProps` (Impact: 138.6)
    * *Intent:* /** * @param {import('jscodeshift').FileInfo} file * @param {import('jscodeshift').API} api */
  * `name` (Impact: 61.9)
  * `matcher` (Impact: 26.2)
    * *Intent:* // Same as Typography but keep color="inherit" as a Link component prop (controls underline behavior...
  * `matcher` (Impact: 16.3)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 862.08
- `packages-internal/core-docs/src/branding/brandingTheme.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 809.36
- `packages/mui-material/src/Slider/useSlider.ts` -> **Albert Yu** (100.0% isolated ownership) | Magnitude: 715.3
- `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js` -> **Silviu Alexandru Avram** (100.0% isolated ownership) | Magnitude: 521.9
- `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 511.78

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/mui-material/src/styles/createTheme.ts` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 99.5526%)
- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 0.023** (Bridge: 0.0005 * Flux: 42.6845%)
- `packages/mui-system/src/styleFunctionSx/styleFunctionSx.js` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.9897%)
- `packages/mui-material/src/styles/createThemeNoVars.js` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 98.67%)
- `packages/mui-material/src/styles/createPalette.js` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 91.2597%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 10396.2** (Blast Radius: 103.962 * Doc Risk: 100.0%)
- `packages/mui-utils/src/generateUtilityClass/generateUtilityClass.ts` -> **Severity: 2223.3** (Blast Radius: 22.233 * Doc Risk: 100.0%)
- `packages/mui-material/src/SvgIcon/svgIconClasses.ts` -> **Severity: 2218.1** (Blast Radius: 22.181 * Doc Risk: 100.0%)
- `packages/mui-utils/src/ClassNameGenerator/ClassNameGenerator.ts` -> **Severity: 1953.6** (Blast Radius: 19.536 * Doc Risk: 100.0%)
- `packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts` -> **Severity: 1206.2** (Blast Radius: 12.062 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
