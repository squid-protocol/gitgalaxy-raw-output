# ARCHITECTURAL_BRIEF: material-ui
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mui/material-ui.git` |
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
- **Scope:** 34055 analyzed artifact(s), 480715 LOC.
- **Load-bearing artifact:** `packages/mui-icons-material/lib/utils/createSvgIcon.mjs` -- 9816 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/mui-icons-material/lib/index.js` -- pulls in 10751 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/mui-icons-material/lib/index.js` at magnitude 24080.1 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 34055 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6963 |
| Total LOC | 480715 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5636 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3726 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9479 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 379 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 21624 | 411052 | 63.5% |
| XML | 10610 | 1243 | 31.2% |
| TYPESCRIPT | 1527 | 64369 | 4.5% |
| JSON | 96 | 1329 | 0.3% |
| MARKDOWN | 64 | 0 | 0.2% |
| PLAINTEXT | 53 | 1 | 0.2% |
| CSS | 40 | 859 | 0.1% |
| YAML | 29 | 1483 | 0.1% |
| HTML | 12 | 379 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 34054 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 57%, Declarative / Non-Code 38%, Parameter Forwarders Files 1%, Callbacks & Closures Files 1%, Large Core Modules (2) 1%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32695 | 96.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 1243 | 3.6% |
| Static: Literature & Documentation | 116 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6963*

**Composition by Extension & Reason:**
- `.js`: 1395x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 872x Excluded (Saturation: Line 12 exceeds 500 chars), 81x Excluded (Saturation: Line 15 exceeds 500 chars)
- `.tsx`: 988x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.mjs`: 872x Excluded (Saturation: Line 6 exceeds 500 chars), 37x Excluded (Saturation: Line 9 exceeds 500 chars), 7x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.png`: 903x Excluded (Explicitly Denied Extension: '.png')
- `.preview`: 397x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 319x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 53809 LOC)
- `.jpg`: 182x Excluded (Explicitly Denied Extension: '.jpg')
- `.svg`: 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.mp4`: 59x Excluded (Explicitly Denied Extension: '.mp4')
- `.jpeg`: 44x Excluded (Explicitly Denied Extension: '.jpeg')
- `no_extension`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.woff2`: 20x Excluded (Explicitly Denied Extension: '.woff2')
- `.ttf`: 16x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.2 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.8 | 17.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.6 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 74.2 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1151 | 592 | 0 | `packages/mui-material/src/index.d.ts` |
| cleanup | 86 | 54 | 0 | `packages-internal/core-docs/src/CodeCopy/CodeCopy.tsx` |
| guards | 4386 | 628 | 0 | `packages/mui-codemod/src/util/migrateToVariants.js` |
| danger | 11352 | 10214 | 1 | `packages/mui-styled-engine-sc/src/index.d.ts` |
| concurrency | 1914 | 186 | 0 | `packages/mui-material/src/ButtonBase/ButtonBase.test.js` |
| connectivity | 36248 | 22017 | 2 | `packages/mui-material/src/index.js` |
| io | 1117 | 306 | 0 | `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` |
| crypto | 1 | 1 | 0 | `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` |
| ipc | 9 | 8 | 0 | `packages-internal/core-docs/src/DocsApp/serviceWorker.ts` |
| time | 79 | 55 | 0 | `packages-internal/core-docs/src/Ad/Ad.tsx` |
| serialization | 133 | 31 | 0 | `packages/mui-system/src/cssVars/useCurrentColorScheme.test.js` |
| regex | 961 | 252 | 0 | `packages-internal/markdown/parseMarkdown.mjs` |
| events | 778 | 206 | 0 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |
| tests | 13531 | 455 | 0 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |
| docs | 6031 | 982 | 0 | `.circleci/config.yml` |
| debt | 879 | 327 | 0 | `packages/mui-material/src/Slider/Slider.test.js` |
| mutation | 90312 | 12198 | 5 | `packages/mui-icons-material/lib/index.js` |
| dead_code | 923 | 533 | 0 | `test/integration/material-ui/components.spec.tsx` |
| credential | 0 | 0 | 0 | - |
| threat | 13 | 7 | 0 | `packages/mui-material/src/locale/faIR.ts` |
| ml_ai | 41 | 16 | 0 | `packages-internal/core-docs/src/Ad/Ad.tsx` |
| ui | 30966 | 20669 | 1 | `packages/mui-material/src/Autocomplete/Autocomplete.test.js` |

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

1. **createSvgIcon.mjs** (`packages/mui-icons-material/lib/utils/createSvgIcon.mjs`) — 9816 inbound connections
2. **index.js** (`packages/mui-material/src/styles/index.js`) — 227 inbound connections
3. **describeConformance.ts** (`packages/mui-material/test/describeConformance.ts`) — 125 inbound connections
4. **index.tsx** (`packages/mui-material/src/zero-styled/index.tsx`) — 124 inbound connections
5. **readFile.js** (`packages/mui-codemod/src/util/readFile.js`) — 122 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.js** (`packages/mui-icons-material/lib/index.js`) — 10751 outbound dependencies
2. **fixtureTemplateValues.js** (`test/bundling/scripts/fixtureTemplateValues.js`) — 151 outbound dependencies
3. **index.js** (`packages/mui-material/src/index.js`) — 142 outbound dependencies
4. **index.d.ts** (`packages/mui-material/src/index.d.ts`) — 141 outbound dependencies
5. **props.ts** (`packages/mui-material/src/styles/props.ts`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `useAutocomplete` **(Defensive Guards)** (@ `packages/mui-material/src/useAutocomplete/useAutocomplete.js`) -> Impact: **505.0** | LOC: 1248
- `sxV6` **(Many-Argument Workhorses)** (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **316.7** | LOC: 494
  * *Intent:* /** */
- `transformer` **(Many-Argument Workhorses)** (@ `packages/mui-codemod/src/v5.0.0/jss-to-styled.js`) -> Impact: **282.0** | LOC: 640
  * *Intent:* /** */
- `migrateToVariants` **(Defensive Guards)** (@ `packages/mui-codemod/src/util/migrateToVariants.js`) -> Impact: **262.3** | LOC: 500
  * *Intent:* /** * */
- `getThemedComponents` **(I/O & Config Routines)** (@ `packages-internal/core-docs/src/branding/brandingTheme.ts`) -> Impact: **259.5** | LOC: 1170
- `createThemeWithVars` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/styles/createThemeWithVars.js`) -> Impact: **230.4** | LOC: 866
  * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` based on the `defaultColorScheme`. * This is better s...
- `useSlider` **(Compute Cores)** (@ `packages/mui-material/src/Slider/useSlider.ts`) -> Impact: **221.4** | LOC: 638
- `Tabs` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/Tabs/Tabs.js`) -> Impact: **197.7** | LOC: 629
- `SwipeableDrawer` **(Many-Argument Workhorses)** (@ `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js`) -> Impact: **189.7** | LOC: 504
- `recurseObjectExpression` **(Defensive Guards)** (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **167.3** | LOC: 320
  * *Intent:* /** * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/mui-icons-material/lib` | 19507 | 363271.54 | 9.63% | 0.0% |
| `packages/mui-icons-material/material-icons` | 10583 | 99614.04 | 0.0% | 0.0% |
| `__monolith__` | 25 | 5958.78 | 1.22% | 1.27% |
| `packages/mui-codemod/src/v5.0.0` | 142 | 3404.08 | 11.01% | 1.27% |
| `packages/mui-material/src/styles` | 83 | 2215.85 | 8.33% | 12.53% |
| `packages/mui-icons-material/legacy` | 139 | 1881.56 | 5.12% | 0.0% |
| `packages-internal/api-docs-builder/ApiBuilders` | 2 | 1304.36 | 55.14% | 8.29% |
| `packages-internal/api-docs-builder/utils` | 24 | 1230.2 | 25.57% | 7.52% |
| `packages/mui-system/src/cssVars` | 18 | 1215.27 | 13.1% | 6.77% |
| `packages/mui-material/src/useAutocomplete` | 6 | 1208.3 | 11.48% | 21.01% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/expected.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/package.actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/package.expected.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/avatar-props/test-cases/theme.actual.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages-internal/waterfall/Queue.mjs` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/all/deprecations-all.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/movePropIntoSlotProps.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/movePropIntoSlots.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/replaceComponentsWithSlots.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/integration/material-ui/components.spec.tsx` -> **42** Orphaned Functions | **2** Duplicates
- `packages-internal/core-docs/src/HighlightedCodeWithTabs/HighlightedCodeWithTabs.tsx` -> **0** Orphaned Functions | **29** Duplicates
- `packages/mui-system/src/colorManipulator/colorManipulator.d.ts` -> **18** Orphaned Functions | **0** Duplicates
- `packages/mui-material/src/SpeedDial/SpeedDial.test.js` -> **0** Orphaned Functions | **14** Duplicates
- `packages/mui-system/src/cssVars/createCssVarsProvider.test.js` -> **2** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36668` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/mui-icons-material/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.003)
- **Top Global Matches:** file_cluster_10: 6.003, file_cluster_2: 8.814, file_cluster_17: 9.157
- **Magnitude:** 24080.1 | **LOC:** 75263 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10751**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (60.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 61.164% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Callbacks & Closures)** (Impact: 2.1)
  * `get` **(Callbacks & Closures)** (Impact: 2.1)
  * `get` **(Callbacks & Closures)** (Impact: 2.1)
  * `get` **(Callbacks & Closures)** (Impact: 2.1)
  * `get` **(Callbacks & Closures)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10751`, `structural_boundaries: 21501`, `args: 10750`, `func_start: 10750`
* *Risk/State:* None
* *Architecture:* `import: 10751`
* *Defense:* `doc: 1`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 127):` Abc, AbcOutlined, AbcRounded, AbcSharp, AbcTwoTone, AcUnit, AcUnitOutlined, AcUnitRounded...
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/useAutocomplete/useAutocomplete.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.51)
- **Top Global Matches:** file_cluster_4: 7.51, file_cluster_12: 10.627, file_cluster_15: 11.324
- **Magnitude:** 1090.52 | **LOC:** 1331 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 0.105; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Complexity Load (formerly Cognitive Load) (51.0%), Connectivity (formerly Api Exposure) (46.7%), Guard Balance (formerly Safety Score) (46.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useAutocomplete` **(Defensive Guards)** (Impact: 505.0)
  * `handleKeyDown` **(Defensive Guards)** (Impact: 111.3)
  * `selectNewValue` **(Defensive Guards)** (Impact: 40.3)
  * `validOptionIndex` **(Defensive Guards)** (Impact: 26.0)
  * `validItemIndex` **(Defensive Guards)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 173`, `args: 73`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 45`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 113`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003728
  * `Imports (Out-Degree: 0):` setRef, useControlled, useEventCallback, useId, usePreviousProps, react
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.526)
- **Top Global Matches:** file_cluster_8: 9.526, file_cluster_3: 15.934, file_cluster_6: 21.437
- **Magnitude:** 816.58 | **LOC:** 941 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (85.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotateComponentDefinition` **(Many-Argument Workhorses)** (Impact: 100.0)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Icons](ht...
  * `attachPropsTable` **(Defensive Guards)** (Impact: 78.2)
  * `generateComponentApi` **(Many-Argument Workhorses)** (Impact: 76.6)
    * *Intent:* /** * - Build react component (specified filename) api by lookup at its definition (.d.ts or ts) * a...
  * `generateApiPage` **(Many-Argument Workhorses)** (Impact: 52.7)
  * `attachTable` **(Defensive Guards)** (Impact: 41.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 69 instances
* *Concurrency (weighted view):* 37
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 138`, `args: 46`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 88`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 17`, `api: 12`, `concurrency: 17`, `import: 33`
* *Defense:* `safety: 43`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000106
  * `Imports (Out-Degree: 15):` $layoutConfigPath, $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/util/migrateToVariants.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.06)
- **Top Global Matches:** file_cluster_4: 8.06, file_cluster_6: 9.4, file_cluster_15: 13.978
- **Magnitude:** 691.32 | **LOC:** 682 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 0.102; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.9%), Connectivity (formerly Api Exposure) (45.1%), Guard Balance (formerly Safety Score) (40.6%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `migrateToVariants` **(Defensive Guards)** (Impact: 262.3)
    * *Intent:* /** * */
  * `recurseObjectExpression` **(Defensive Guards)** (Impact: 102.9)
  * `buildProps` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /** * */
  * `createBuildStyle` **(Defensive Guards)** (Impact: 17.6)
  * `assignProperties` **(Defensive Guards)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 87`, `args: 53`, `func_start: 26`
* *Risk/State:* `state_mutation: 55`, `duplicate_logic: 3`
* *Architecture:* `api: 9`
* *Defense:* `safety: 129`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000158
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Slider/useSlider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.983)
- **Top Global Matches:** file_cluster_4: 6.983, file_cluster_6: 10.907, file_cluster_12: 11.266
- **Magnitude:** 649.3 | **LOC:** 855 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (68.8%), Guard Balance (formerly Safety Score) (59.4%), Connectivity (formerly Api Exposure) (25.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useSlider` **(Compute Cores)** (Impact: 221.4)
  * `createHandleHiddenInputKeyDown` **(Compute Cores)** (Impact: 46.7)
  * `changeValue` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `getFingerNewValue` **(Compute Cores)** (Impact: 24.5)
  * `createHandleMouseDown` **(Defensive Guards)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 112`, `args: 55`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 22`, `doc: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.045
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.003684
  * `Imports (Out-Degree: 3):` areArraysEqual, types, useSlider.types, clamp, extractEventHandlers, isFocusVisible, ownerDocument, useControlled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.891)
- **Top Global Matches:** file_cluster_6: 7.891, file_cluster_4: 10.502, file_cluster_8: 16.916
- **Magnitude:** 637.62 | **LOC:** 530 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.047; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Complexity Load (formerly Cognitive Load) (74.8%), Guard Balance (formerly Safety Score) (38.4%), Debt Markers (formerly Tech Debt) (18.7%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sxV6` **(Many-Argument Workhorses)** (Impact: 316.7)
    * *Intent:* /** */
  * `recurseObjectExpression` **(Defensive Guards)** (Impact: 167.3)
    * *Intent:* /** * */
  * `rootThemeCallback` **(Defensive Guards)** (Impact: 9.0)
  * `replaceUndefined` **(Defensive Guards)** (Impact: 7.2)
    * *Intent:* /** * */
  * `getCssVarName` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* /** * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 43`, `args: 30`, `func_start: 13`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 110`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.9e-05
  * `Imports (Out-Degree: 2):` getReturnExpression, migrateToVariants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `CHANGELOG.old.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 621.5 | **LOC:** 31075 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.022; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` globals, composition, typescript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-codemod/src/v5.0.0/jss-to-styled.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.403)
- **Top Global Matches:** file_cluster_4: 8.403, file_cluster_9: 10.447, file_cluster_6: 12.243
- **Magnitude:** 607.26 | **LOC:** 647 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.031; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (53.3%), Complexity Load (formerly Cognitive Load) (47.7%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 43.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformer` **(Many-Argument Workhorses)** (Impact: 282.0)
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
* *Structure:* `branch: 125`, `structural_boundaries: 76`, `args: 51`, `func_start: 13`
* *Risk/State:* `state_mutation: 62`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 1`
* *Defense:* `safety: 68`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.9e-05
  * `Imports (Out-Degree: 0):` path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages-internal/core-docs/src/branding/brandingTheme.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.835)
- **Top Global Matches:** file_cluster_6: 6.835, file_cluster_4: 12.6, file_cluster_8: 13.316
- **Magnitude:** 581.16 | **LOC:** 1592 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 0.199; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%), Connectivity (formerly Api Exposure) (44.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.5%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getThemedComponents` **(I/O & Config Routines)** (Impact: 259.5)
  * `root` **(Compute Cores)** (Impact: 80.0)
  * `root` **(I/O & Config Routines)** (Impact: 78.2)
  * `getDesignTokens` **(I/O & Config Routines)** (Impact: 33.9)
  * `root` **(I/O & Config Routines)** (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 68`, `args: 31`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 2`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.199
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000392
  * `Imports (Out-Degree: 0):` ArrowDropDownRounded, styles, themeCssVarsAugmentation, system
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.884)
- **Top Global Matches:** file_cluster_8: 8.884, file_cluster_3: 17.079, file_cluster_6: 20.445
- **Magnitude:** 487.78 | **LOC:** 513 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (88.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.5%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `annotateHookDefinition` **(Many-Argument Workhorses)** (Impact: 107.8)
    * *Intent:* /** * Add demos & API comment block to type definitions, e.g.: * /** * * Demos: * * * * - [Button](h...
  * `attachTable` **(Defensive Guards)** (Impact: 41.0)
  * `attachTranslations` **(Defensive Guards)** (Impact: 39.9)
  * `ExportNamedDeclaration` **(Defensive Guards)** (Impact: 38.5)
  * `generateHookApi` **(Many-Argument Workhorses)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 83`, `args: 31`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 15`, `api: 5`, `concurrency: 11`, `import: 19`
* *Defense:* `safety: 24`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 9.6e-05
  * `Imports (Out-Degree: 9):` $rootImportPath, $subdirectoryImportPath, ProjectSettings, buildApi, buildApiUtils, ApiBuilder.types, utils.types, createTypeScriptProject...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-tss-react.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.298)
- **Top Global Matches:** file_cluster_8: 7.298, file_cluster_6: 13.377, file_cluster_4: 21.682
- **Magnitude:** 471.84 | **LOC:** 491 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.031; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (67.4%), Guard Balance (formerly Safety Score) (58.5%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 46.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transformer` **(Many-Argument Workhorses)** (Impact: 125.0)
    * *Intent:* /** */
  * `transformStylesExpression` **(Many-Argument Workhorses)** (Impact: 91.3)
  * `transformNestedKeys` **(Many-Argument Workhorses)** (Impact: 36.6)
  * `addCommentsToNode` **(State Mutators)** (Impact: 8.5)
  * `addCommentsToDeclaration` **(Defensive Guards)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 59`, `args: 36`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 74`, `planned_debt: 5`
* *Architecture:* `api: 1`
* *Defense:* `safety: 55`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.9e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.819)
- **Top Global Matches:** file_cluster_8: 7.819, file_cluster_6: 14.475, file_cluster_4: 22.918
- **Magnitude:** 435.54 | **LOC:** 532 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.8%), Guard Balance (formerly Safety Score) (59.1%), Connectivity (formerly Api Exposure) (44.7%), Complexity Load (formerly Cognitive Load) (22.4%)
- **Documentation Coverage:** 82.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createBabelPlugin` **(Compute Cores)** (Impact: 110.7)
  * `getUsedProps` **(Compute Cores)** (Impact: 46.7)
    * *Intent:* /** * Gets used props from path */
  * `enter` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `getUsedPropsInternal` **(Compute Cores)** (Impact: 38.3)
  * `VariableDeclarator` **(Compute Cores)** (Impact: 27.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 52`, `args: 29`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 20`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 55`, `api: 9`, `import: 6`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 6.6e-05
  * `Imports (Out-Degree: 2):` generatePropTypes, models, core, types, node:crypto, prop-types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tabs/Tabs.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.703)
- **Top Global Matches:** file_cluster_4: 6.703, file_cluster_15: 9.711, file_cluster_10: 10.311
- **Magnitude:** 406.9 | **LOC:** 1017 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.9%), Guard Balance (formerly Safety Score) (48.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%), Connectivity (formerly Api Exposure) (32.3%)
- **Documentation Coverage:** 96.875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tabs` **(Many-Argument Workhorses)** (Impact: 197.7)
  * `getTabsMeta` **(I/O & Config Routines)** (Impact: 19.4)
  * `useUtilityClasses` **(Compute Cores)** (Impact: 17.1)
  * `getConditionalElements` **(I/O & Config Routines)** (Impact: 11.6)
  * `overridesResolver` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 100`, `args: 50`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `planned_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 4`, `import: 24`
* *Defense:* `safety: 42`, `doc: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.004383
  * `Imports (Out-Degree: 18):` DefaultPropsProvider, TabScrollButton, animate, debounce, getActiveElement, isLayoutSupported, memoTheme, ownerDocument...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.813)
- **Top Global Matches:** file_cluster_4: 6.813, file_cluster_6: 8.51, file_cluster_15: 13.266
- **Magnitude:** 400.7 | **LOC:** 777 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (44.0%), Connectivity (formerly Api Exposure) (22.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SwipeableDrawer` **(Many-Argument Workhorses)** (Impact: 189.7)
  * `getDomTreeShapes` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* /** */
  * `computeHasNativeHandler` **(Defensive Guards)** (Impact: 14.6)
    * *Intent:* /** */
  * `startMaybeSwiping` **(Compute Cores)** (Impact: 12.9)
  * `getTranslate` **(Parameter Forwarders)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 62`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 15`
* *Defense:* `safety: 27`, `doc: 21`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.004368
  * `Imports (Out-Degree: 15):` DefaultPropsProvider, Drawer, NoSsr, utils, utils, ownerDocument, ownerWindow, useEnhancedEffect...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/styles/createThemeWithVars.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.832)
- **Top Global Matches:** file_cluster_4: 6.832, file_cluster_15: 10.183, file_cluster_10: 10.968
- **Magnitude:** 379.02 | **LOC:** 993 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **12**; blast radius 0.453; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (49.8%), Guard Balance (formerly Safety Score) (49.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.1%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createThemeWithVars` **(Many-Argument Workhorses)** (Impact: 230.4)
    * *Intent:* /** * A default `createThemeWithVars` comes with a single color scheme, either `light` or `dark` bas...
  * `attachColorScheme` **(Defensive Guards)** (Impact: 26.0)
  * `colorMix` **(Defensive Guards)** (Impact: 10.8)
  * `getSpacingVal` **(Defensive Guards)** (Impact: 7.7)
  * `setColor` **(State Mutators)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 52`, `args: 28`, `func_start: 15`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 33`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.453
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.007727
  * `Imports (Out-Degree: 6):` createColorScheme, createGetSelector, createPalette, createThemeNoVars, shouldSkipGeneratingVar, stringifyTheme, system, colorManipulator...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tooltip/Tooltip.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.09)
- **Top Global Matches:** file_cluster_15: 7.09, file_cluster_10: 7.954, file_cluster_4: 8.55
- **Magnitude:** 365.48 | **LOC:** 935 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.082; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Debt Markers (formerly Tech Debt) (92.9%), Guard Balance (formerly Safety Score) (52.9%), Connectivity (formerly Api Exposure) (29.6%)
- **Documentation Coverage:** 97.4359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tooltip` **(Many-Argument Workhorses)** (Impact: 142.8)
  * `handleMouseOver` **(Defensive Guards)** (Impact: 13.8)
  * `handleBlur` **(Defensive Guards)** (Impact: 12.3)
  * `useUtilityClasses` **(Compute Cores)** (Impact: 7.9)
  * `overridesResolver` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 85`, `args: 52`, `func_start: 33`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 4`, `duplicate_logic: 9`
* *Architecture:* `api: 3`, `import: 21`
* *Defense:* `safety: 21`, `doc: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.082
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.004421
  * `Imports (Out-Degree: 14):` DefaultPropsProvider, Grow, Popper, capitalize, memoTheme, useControlled, useEventCallback, useForkRef...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-system/src/createStyled/createStyled.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.535)
- **Top Global Matches:** file_cluster_4: 7.535, file_cluster_15: 8.905, file_cluster_9: 9.933
- **Magnitude:** 324.98 | **LOC:** 351 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 0.115; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.0%), Connectivity (formerly Api Exposure) (50.2%), Guard Balance (formerly Safety Score) (48.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStyled` **(Defensive Guards)** (Impact: 67.5)
  * `processStyleVariants` **(Defensive Guards)** (Impact: 35.3)
  * `styled` **(Defensive Guards)** (Impact: 28.6)
  * `processStyle` **(Defensive Guards)** (Impact: 27.8)
  * `shallowLayer` **(Defensive Guards)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 55`, `args: 23`, `func_start: 19`
* *Risk/State:* `state_mutation: 28`, `planned_debt: 5`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000362
  * `Imports (Out-Degree: 3):` createTheme, preprocessStyles, styleFunctionSx, styled-engine, capitalize, deepmerge, getDisplayName, isObjectEmpty
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages-internal/scripts/typescript-to-proptypes/src/getPropTypesFromFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.455)
- **Top Global Matches:** file_cluster_6: 6.455, file_cluster_4: 10.931, file_cluster_8: 15.196
- **Magnitude:** 309.64 | **LOC:** 751 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.037; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (55.3%), Guard Balance (formerly Safety Score) (53.7%), Connectivity (formerly Api Exposure) (20.2%), Complexity Load (formerly Cognitive Load) (16.0%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkType` **(Compute Cores)** (Impact: 110.8)
  * `checkSymbol` **(Compute Cores)** (Impact: 48.9)
  * `getPropTypesFromFile` **(Compute Cores)** (Impact: 21.0)
  * `getType` **(Compute Cores)** (Impact: 17.6)
  * `getSymbolDocumentation` **(Compute Cores)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 166`, `args: 40`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`, `planned_debt: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 7`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 6.6e-05
  * `Imports (Out-Degree: 2):` createType, models, internal-docs-utils, doctrine, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-utils/src/useRovingTabIndex/useRovingTabIndex.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.991)
- **Top Global Matches:** file_cluster_4: 8.991, file_cluster_6: 11.693, file_cluster_0: 12.314
- **Magnitude:** 306.26 | **LOC:** 816 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.1%), Guard Balance (formerly Safety Score) (51.2%), Connectivity (formerly Api Exposure) (41.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.1%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `useRovingTabIndexRoot` **(Compute Cores)** (Impact: 60.1)
    * *Intent:* /** * Provides roving tab index behavior for a composite container and its focusable children. * Thi...
  * `onKeyDown` **(Compute Cores)** (Impact: 28.4)
  * `getNextActiveItem` **(Many-Argument Workhorses)** (Impact: 21.3)
    * *Intent:* * Walks the item snapshot to find the next focusable item in the requested direction. * * This is th...
  * `useRovingTabIndexItem` **(Defensive Guards)** (Impact: 15.3)
  * `getNextIndex` **(Many-Argument Workhorses)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 145`, `args: 62`, `func_start: 21`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 17`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.8e-05
  * `Imports (Out-Degree: 13):` fastObjectShallowCompare, getActiveElement, ownerDocument, setRef, useEnhancedEffect, useEventCallback, useForkRef, RovingTabIndexContext...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages-internal/markdown/loader.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.678)
- **Top Global Matches:** file_cluster_6: 7.678, file_cluster_4: 11.628, file_cluster_8: 15.684
- **Magnitude:** 304.64 | **LOC:** 720 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (50.7%), Complexity Load (formerly Cognitive Load) (34.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `demoLoader` **(I/O & Config Routines)** (Impact: 54.0)
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
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 100`, `args: 38`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 51`, `api: 5`, `concurrency: 27`, `import: 11`
* *Defense:* `safety: 33`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` $moduleID, extractImports.mjs, prepareMarkdown.mjs, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/Select/SelectInput.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.966)
- **Top Global Matches:** file_cluster_4: 6.966, file_cluster_10: 10.235, file_cluster_12: 10.385
- **Magnitude:** 298.12 | **LOC:** 759 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (71.7%), Guard Balance (formerly Safety Score) (48.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.2%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SelectInput` **(Many-Argument Workhorses)** (Impact: 158.5)
    * *Intent:* /** */
  * `handleItemClick` **(Defensive Guards)** (Impact: 19.3)
  * `update` **(Compute Cores)** (Impact: 13.1)
  * `useUtilityClasses` **(Compute Cores)** (Impact: 9.0)
  * `handleKeyDown` **(Defensive Guards)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 76`, `args: 33`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `safety: 32`, `doc: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003711
  * `Imports (Out-Degree: 13):` utils, Menu, NativeSelectInput, slotShouldForwardProp, ownerDocument, useControlled, useForkRef, zero-styled...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 19.536)
- **Top Global Matches:** file_cluster_17: 19.536, file_cluster_13: 19.579, file_cluster_15: 19.614
- **Magnitude:** 295.52 | **LOC:** 421 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **142**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Complexity Load (formerly Cognitive Load) (26.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.2%), Debt Markers (formerly Tech Debt) (9.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 276`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 275`, `import: 275`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.00044
  * `Imports (Out-Degree: 141):` Accordion, AccordionActions, AccordionDetails, AccordionSummary, Alert, AlertTitle, AppBar, Autocomplete...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `packages/mui-system/src/cssVars/createCssVarsProvider.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.375)
- **Top Global Matches:** file_cluster_8: 8.375, file_cluster_6: 17.862, file_cluster_3: 20.762
- **Magnitude:** 274.3 | **LOC:** 413 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.042; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Guard Balance (formerly Safety Score) (44.6%), Concurrency Surface (formerly Concurrency) (35.7%), Connectivity (formerly Api Exposure) (29.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createCssVarsProvider` **(Defensive Guards)** (Impact: 108.9)
  * `CssVarsProvider` **(Defensive Guards)** (Impact: 104.1)
  * `useColorScheme` **(Callbacks & Closures)** (Impact: 2.0)
  * `getInitColorSchemeScript` **(Parameter Forwarders)** (Impact: 1.8)
  * `setColorScheme` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 46`, `args: 22`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 38`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000361
  * `Imports (Out-Degree: 3):` InitColorSchemeScript, ThemeProvider, useCurrentColorScheme, private-theming, styled-engine, useEnhancedEffect, prop-types, react
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tabs/Tabs.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.172)
- **Top Global Matches:** file_cluster_10: 6.172, file_cluster_15: 8.582, file_cluster_12: 9.241
- **Magnitude:** 272.82 | **LOC:** 1753 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.022; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%), Guard Balance (formerly Safety Score) (41.3%), Complexity Load (formerly Cognitive Load) (15.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test` **(I/O & Config Routines)** (Impact: 4.3)
  * `test` **(Callbacks & Closures)** (Impact: 3.9)
    * *Intent:* // https://github.com/mui/material-ui/issues/31936
  * `hasLeftScrollButton` **(Parameter Forwarders)** (Impact: 3.3)
  * `hasRightScrollButton` **(Parameter Forwarders)** (Impact: 3.3)
  * `root` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Concurrency (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 258`, `args: 173`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 26`, `duplicate_logic: 5`
* *Architecture:* `concurrency: 112`, `import: 11`
* *Defense:* `safety: 4`, `test: 300`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.022
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` describeConformance, capitalize, internal-test-utils, SvgIcon, Tab, Tabs, styles, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/mui-material/src/Collapse/collapseClasses.ts` (TYPESCRIPT) | Magnitude: 6.08 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, doc: 6, api: 4
- `packages/mui-material/test/typescript/moduleAugmentation/buttonCustomProps.spec.tsx` (TYPESCRIPT) | Magnitude: 15.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 8, class_start: 3, decorators: 3
- `packages/mui-utils/src/setRef/setRef.spec.tsx` (TYPESCRIPT) | Magnitude: 1.58 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, core_var_decl: 3, args: 2
- `packages-internal/core-docs/src/branding/BrandingProvider.tsx` (TYPESCRIPT) | Magnitude: 8.28 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, branch: 4, core_var_decl: 4
- `packages-internal/core-docs/src/Ad/AdGuest.tsx` (TYPESCRIPT) | Magnitude: 17.14 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, branch: 6, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/mui-material/src/SpeedDialAction/SpeedDialAction.js` (JAVASCRIPT) | Magnitude: 60.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 233, structural_boundaries: 32, branch: 22, core_var_decl: 21
- `test/e2e/fixtures/FocusTrap/DefaultOpenLazyFocusTrap.tsx` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, core_var_decl: 4, args: 3
- `packages/mui-codemod/src/v5.0.0/jss-to-styled.test/first.actual.js` (JAVASCRIPT) | Magnitude: 38.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 28, ui_framework: 21, core_var_decl: 21
- `packages/mui-codemod/src/deprecations/linear-progress-classes/postcss-plugin.js` (JAVASCRIPT) | Magnitude: 12.64 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 3, args: 3, state_mutation: 3
- `packages-internal/api-docs-builder/utils/findHooks.ts` (TYPESCRIPT) | Magnitude: 11.12 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, io: 7, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/mui-material/src/DialogContent/DialogContent.js` (JAVASCRIPT) | Magnitude: 17.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 18, core_var_decl: 11, import: 9
- `packages/mui-styled-engine/src/GlobalStyles/GlobalStyles.test.js` (JAVASCRIPT) | Magnitude: 9.18 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 72, test: 13, structural_boundaries: 10, args: 10
- `packages/mui-styled-engine-sc/src/GlobalStyles/GlobalStyles.test.js` (JAVASCRIPT) | Magnitude: 9.18 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 72, test: 13, structural_boundaries: 10, args: 10
- `packages/mui-system/src/index.spec.tsx` (TYPESCRIPT) | Magnitude: 17.96 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 39, args: 9, func_start: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/mui-material/src/InputLabel/InputLabel.test.js` (JAVASCRIPT) | Magnitude: 12.18 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 53, test: 32, ui_framework: 27
- `packages/mui-codemod/src/deprecations/circular-progress-classes/postcss-plugin.js` (JAVASCRIPT) | Magnitude: 12.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 3, args: 3, state_mutation: 3
- `packages/mui-codemod/src/deprecations/dialog-classes/postcss-plugin.js` (JAVASCRIPT) | Magnitude: 12.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 3, args: 3, state_mutation: 3
- `packages/mui-codemod/src/deprecations/step-connector-classes/postcss-plugin.js` (JAVASCRIPT) | Magnitude: 12.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 3, args: 3, state_mutation: 3
- `packages/mui-codemod/src/deprecations/table-sort-label-classes/postcss-plugin.js` (JAVASCRIPT) | Magnitude: 12.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 3, args: 3, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages-internal/core-docs/src/ApiPage/definitions/slots.ts` (TYPESCRIPT) | Magnitude: 17.2 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, branch: 6, args: 4
- `packages/mui-material/src/Skeleton/skeletonClasses.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, doc: 10, structural_boundaries: 9, api: 4
- `packages/mui-material/src/SvgIcon/svgIconClasses.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, doc: 10, structural_boundaries: 9, api: 4
- `packages/mui-material/src/Tab/tabClasses.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, doc: 10, structural_boundaries: 9, api: 4
- `packages/mui-material/src/ToggleButton/toggleButtonClasses.ts` (TYPESCRIPT) | Magnitude: 6.22 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, doc: 10, structural_boundaries: 9, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/mui-system/src/propsToClassKey/propsToClassKey.d.ts` (TYPESCRIPT) | Magnitude: 0.13 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `packages-internal/api-docs-builder/utils/findComponents.ts` (TYPESCRIPT) | Magnitude: 11.12 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, io: 7, branch: 5
- `packages/mui-material/src/CircularProgress/circularProgressClasses.ts` (TYPESCRIPT) | Magnitude: 6.24 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 9, doc: 9, api: 4
- `packages/mui-material/src/FormControlLabel/formControlLabelClasses.ts` (TYPESCRIPT) | Magnitude: 6.24 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 9, doc: 9, api: 4
- `packages/mui-utils/src/index.ts` (TYPESCRIPT) | Magnitude: 71.1 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 56, api: 55, import: 55, branch: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/mui-material/src/index.d.ts` (TYPESCRIPT) | Magnitude: 14.78 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 276, api: 275, import: 275, branch: 137
- `packages/mui-codemod/src/deprecations/all/postcss.config.js` (JAVASCRIPT) | Magnitude: 17.96 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, import: 16, api: 1, state_mutation: 1
- `packages/mui-lab/src/index.d.ts` (TYPESCRIPT) | Magnitude: 4.73 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 78, api: 78, import: 78, branch: 39
- `packages/mui-material/src/index.js` (JAVASCRIPT) | Magnitude: 295.52 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 276, api: 275, import: 275, branch: 138
- `packages/mui-material/src/locale/index.ts` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 60, api: 60, import: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/mark-duplicate.yml` (YAML) | Magnitude: 15.42 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, args: 5, branch: 2, structural_boundaries: 2
- `packages/mui-material/src/Box/Box.js` (JAVASCRIPT) | Magnitude: 17.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, import: 6, doc: 3
- `packages/mui-codemod/src/util/readFile.js` (JAVASCRIPT) | Magnitude: 4.38 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, io: 3, branch: 2
- `packages/mui-codemod/src/v5.0.0/material-ui-styles.test/core-import.actual.js` (JAVASCRIPT) | Magnitude: 15.3 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 2, decorators: 2, import: 2
- `packages/mui-codemod/src/deprecations/form-control-label-props/test-cases/expected.js` (JAVASCRIPT) | Magnitude: 14.16 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, core_var_decl: 3, ui_framework: 2, design_camel_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/mui-system/src/breakpoints/breakpoints.d.ts` (TYPESCRIPT) | Magnitude: 1.22 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 12, safety_bypasses: 10, generics: 10
- `packages/mui-system/src/styleFunctionSx/extendSxProp.d.ts` (TYPESCRIPT) | Magnitude: 0.2 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 2, args: 1, func_start: 1
- `packages-internal/core-docs/src/DocsApp/DocsApp.tsx` (TYPESCRIPT) | Magnitude: 13.1 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 35, import: 20, ui_framework: 17
- `packages/mui-material/src/Slider/SliderValueLabel.tsx` (TYPESCRIPT) | Magnitude: 8.96 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, ui_framework: 7, core_var_decl: 6
- `packages/mui-utils/src/unsupportedProp/unsupportedProp.test.ts` (TYPESCRIPT) | Magnitude: 15.4 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, core_var_decl: 6, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages-internal/scripts/typescript-to-proptypes/src/generatePropTypes.ts` (TYPESCRIPT) | Magnitude: 185.9 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 128, branch: 68, core_var_decl: 36
- `scripts/generateProptypes.ts` (TYPESCRIPT) | Magnitude: 185.68 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 288, structural_boundaries: 57, branch: 37, core_var_decl: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/regressions/fixtures/Grid/Issue43707.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 63, ui_framework: 30, core_var_decl: 18, design_snake_case: 17
- `packages/mui-material/src/MobileStepper/MobileStepper.test.js` (JAVASCRIPT) | Magnitude: 6.36 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 148, test: 39, structural_boundaries: 35, ui_framework: 28
- `packages/mui-icons-material/lib/BathroomTwoTone.js` (JAVASCRIPT) | Magnitude: 20.82 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, branch: 4, structural_boundaries: 4, core_var_decl: 4
- `packages/mui-material/src/AppBar/AppBar.test.js` (JAVASCRIPT) | Magnitude: 4.72 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 29, test: 23, ui_framework: 11
- `packages/mui-utils/src/createChainedFunction/createChainedFunction.ts` (TYPESCRIPT) | Magnitude: 7.22 | Delta: **0.173** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, args: 5, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/mui-utils/src/elementTypeAcceptingRef/elementTypeAcceptingRef.ts` (TYPESCRIPT) | Magnitude: 32.58 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 10, branch: 8, core_var_decl: 5
- `packages-internal/core-docs/src/Link/MarkdownLinks.ts` (TYPESCRIPT) | Magnitude: 48.4 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 62, branch: 19, structural_boundaries: 19, core_var_decl: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages-internal/api-docs-builder/ApiBuilders/ComponentApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 816.58
- `packages/mui-material/src/Slider/useSlider.ts` -> **Albert Yu** (100.0% isolated ownership) | Magnitude: 649.3
- `packages-internal/core-docs/src/branding/brandingTheme.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 581.16
- `packages-internal/api-docs-builder/ApiBuilders/HookApiBuilder.ts` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 487.78
- `packages-internal/scripts/typescript-to-proptypes/src/injectPropTypesInFile.ts` -> **Jose C Quintas Jr** (100.0% isolated ownership) | Magnitude: 435.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/mui-material/src/DefaultPropsProvider/DefaultPropsProvider.tsx` -> **Severity: 0.014** (Bridge: 0.0003 * Flux: 50.0%)
- `packages/mui-material/src/SvgIcon/createSvgIcon.js` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 91.6827%)
- `packages/mui-material/src/styles/createTheme.ts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.5526%)
- `packages/mui-material/src/ButtonBase/ButtonBase.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 54.9987%)
- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 42.6845%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/mui-material/src/styles/createTheme.ts` -> **Severity: 0.578** (Embedded: 0.0092 * Error Risk: 62.9173%)
- `packages/mui-material/src/DefaultPropsProvider/DefaultPropsProvider.tsx` -> **Severity: 0.482** (Embedded: 0.0086 * Error Risk: 56.1121%)
- `packages/mui-material/src/zero-styled/index.tsx` -> **Severity: 0.448** (Embedded: 0.0086 * Error Risk: 51.9989%)
- `packages/mui-material/src/styles/stringifyTheme.ts` -> **Severity: 0.421** (Embedded: 0.006 * Error Risk: 70.0%)
- `packages/mui-material/src/styles/createThemeWithVars.js` -> **Severity: 0.382** (Embedded: 0.0077 * Error Risk: 49.4665%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/mui-material/src/DefaultPropsProvider/DefaultPropsProvider.tsx` -> **Severity: 178.6** (Blast Radius: 1.786 * Doc Risk: 100.0%)
- `packages/mui-codemod/src/util/readFile.js` -> **Severity: 142.5** (Blast Radius: 1.425 * Doc Risk: 100.0%)
- `packages/mui-material/test/describeConformance.ts` -> **Severity: 70.3** (Blast Radius: 0.703 * Doc Risk: 100.0%)
- `packages/mui-material/src/zero-styled/index.tsx` -> **Severity: 61.6** (Blast Radius: 0.924 * Doc Risk: 66.6667%)
- `packages/mui-material/src/SvgIcon/SvgIcon.js` -> **Severity: 55.5** (Blast Radius: 0.555 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 244 literal sites + 1 sites through wrappers = 245

- `onEntered` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/mui-material/src/Modal/Modal.spec.tsx`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 11121 call pairs -- scoped 18.1%, unique 0.0%, ambiguous 10.4%, external 71.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 7504 | 17.9% | 0.0% | 10.5% | 71.6% |
| typescript | 3613 | 18.7% | 0.0% | 10.3% | 71.0% |
| html | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
