# ARCHITECTURAL_BRIEF: material-ui
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/material-ui` |
| **Timestamp** | `2026-08-07T04:26:46.848224+00:00` |
| **Scan Duration** | `19.79s` |
| **Git Branch** | `master` |
| **Git Commit** | `d7d328cf02ac669419a181ea1c357618cb753322` |
| **Git Remote** | `https://github.com/mui/material-ui.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3433 malicious artifacts.

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
| Total Artifacts | 41018 |
| Analyzed Artifacts (Scanned) | 14241 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 26777 |
| Total LOC | 171321 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 34.7% |
| Dominant Lang | XML |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1622 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 405 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 10610 | 1243 | 74.5% |
| JAVASCRIPT | 2013 | 113972 | 14.1% |
| TYPESCRIPT | 1420 | 53980 | 10.0% |
| PLAINTEXT | 53 | 1 | 0.4% |
| MARKDOWN | 51 | 0 | 0.4% |
| JSON | 45 | 907 | 0.3% |
| CSS | 40 | 859 | 0.3% |
| HTML | 7 | 314 | 0.0% |
| YAML | 2 | 45 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.746`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 11109 | 78.0% |
| file_cluster_13 | 1447 | 10.2% |
| file_cluster_2 | 175 | 1.2% |
| file_cluster_17 | 85 | 0.6% |
| file_cluster_16 | 45 | 0.3% |
| file_cluster_0 | 19 | 0.1% |
| file_cluster_4 | 10 | 0.1% |
| file_cluster_1 | 2 | 0.0% |
| file_cluster_9 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 1243 | 8.7% |
| Static: Literature & Documentation | 103 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 26777*

**Composition by Extension & Reason:**
- `.js`: 12256x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded (Saturation: Line 4 exceeds 500 chars), 4x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.mjs`: 10761x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 97 exceeds 500 chars)
- `.tsx`: 1030x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 58 exceeds 500 chars)
- `.png`: 899x Excluded (Explicitly Denied Extension: '.png')
- `.preview`: 397x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 352x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 53809 LOC exceeds safe regex boundaries)
- `.md`: 330x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31075 LOC exceeds safe regex boundaries)
- `.jpg`: 182x Excluded (Explicitly Denied Extension: '.jpg')
- `.svg`: 130x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.mp4`: 59x Excluded (Explicitly Denied Extension: '.mp4')
- `.jpeg`: 44x Excluded (Explicitly Denied Extension: '.jpeg')
- `no_extension`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 5.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.2 | 2.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 0.4 | 0.2 | 0.2 |
| API Exposure | 0.0 | 19.9 | 1.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 22.3 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 55.6 | 1.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 9.6 | 6.2 | 6.2 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/bundling/scripts/fixtureTemplateValues.js` (Hits: 145)
- `packages/mui-codemod/src/v5.0.0/jss-to-styled.js` (Hits: 69)
- `packages/mui-codemod/src/v5.0.0/jss-to-tss-react.js` (Hits: 48)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **styles.css** (`packages/mui-material-pigment-css/src/styles.css`) — 351 inbound connections
2. **generateUtilityClass.ts** (`packages/mui-utils/src/generateUtilityClass/generateUtilityClass.ts`) — 144 inbound connections
3. **composeClasses.ts** (`packages/mui-utils/src/composeClasses/composeClasses.ts`) — 137 inbound connections
4. **generateUtilityClasses.ts** (`packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts`) — 137 inbound connections
5. **readFile.js** (`packages/mui-codemod/src/util/readFile.js`) — 122 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fixtureTemplateValues.js** (`test/bundling/scripts/fixtureTemplateValues.js`) — 151 outbound dependencies
2. **index.js** (`packages/mui-material/src/index.js`) — 142 outbound dependencies
3. **index.d.ts** (`packages/mui-material/src/index.d.ts`) — 141 outbound dependencies
4. **props.ts** (`packages/mui-material/src/styles/props.ts`) — 118 outbound dependencies
5. **overrides.ts** (`packages/mui-material/src/styles/overrides.ts`) — 117 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getThemedComponents` (@ `packages-internal/core-docs/src/branding/brandingTheme.ts`) -> Impact: **481.1** | LOC: 1170
  * *Intent:* /** * This utility exists to help transitioning to CSS variables page by page (prevent dark mode flicker). * It will use the proper styling method bas...
- `sxV6` (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **295.4** | LOC: 469
- `transformer` (@ `packages/mui-codemod/src/v5.0.0/jss-to-styled.js`) -> Impact: **281.8** | LOC: 596
  * *Intent:* /**
- `migrateToVariants` (@ `packages/mui-codemod/src/util/migrateToVariants.js`) -> Impact: **267.1** | LOC: 492
- `validOptionIndex` (@ `packages/mui-material/src/useAutocomplete/useAutocomplete.js`) -> Impact: **233.9** | LOC: 347
- `recurseObjectExpression` (@ `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`) -> Impact: **201.3** | LOC: 320
- `removeSystemProps` (@ `packages/mui-codemod/src/v9.0.0/system-props/removeSystemProps.js`) -> Impact: **138.6** | LOC: 172
  * *Intent:* /**
- `describe` (@ `packages/mui-material/src/styles/createTheme.test.js`) -> Impact: **127.6** | LOC: 820
- `transformer` (@ `packages/mui-codemod/src/v5.0.0/joy-text-field-to-input.js`) -> Impact: **126.3** | LOC: 206
  * *Intent:* /**
- `SelectInput` (@ `packages/mui-material/src/Select/SelectInput.js`) -> Impact: **126.1** | LOC: 339
  * *Intent:* /**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/mui-icons-material/material-icons` | 10583 | 99614.04 | 4.42% | 0.0% |
| `__monolith__` | 22 | 5250.52 | 3.3% | 2.22% |
| `packages/mui-codemod/src/v5.0.0` | 142 | 4604.6 | 8.84% | 4.42% |
| `packages/mui-material/src/styles` | 83 | 3350.59 | 7.33% | 18.23% |
| `packages-internal/markdown` | 12 | 3075.41 | 10.73% | 12.11% |
| `packages/mui-icons-material/legacy` | 139 | 1881.56 | 5.0% | 0.0% |
| `packages/mui-system/src/cssVars` | 18 | 1474.38 | 14.25% | 21.44% |
| `packages/mui-material/src/Tabs` | 9 | 1036.47 | 5.97% | 35.4% |
| `packages/mui-material/src/Autocomplete` | 7 | 983.5 | 4.0% | 23.48% |
| `packages/mui-material/src/Select` | 9 | 978.09 | 8.85% | 22.21% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/mui-codemod/src/deprecations/accordion-props/test-cases/theme.actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/accordion-props/test-cases/theme.expected.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/accordion-summary-classes/test-cases/actual.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/accordion-summary-classes/test-cases/expected.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/accordion-summary-classes/test-cases/package.actual.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages-internal/waterfall/Queue.mjs` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/table-sort-label-classes/index.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/deprecations/utils/movePropIntoSlots.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/util/assignObject.js` -> **100.0%** Exposure
- `packages/mui-codemod/src/util/findComponentJSX.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/mui-material/src/Autocomplete/Autocomplete.test.js` -> **1** Orphaned Functions | **276** Duplicates
- `packages/mui-material/src/Select/Select.test.js` -> **0** Orphaned Functions | **171** Duplicates
- `packages/mui-material/src/Tabs/Tabs.test.js` -> **2** Orphaned Functions | **166** Duplicates
- `packages/mui-system/src/spacing/spacing.test.js` -> **0** Orphaned Functions | **130** Duplicates
- `packages/mui-system/src/cssVars/useCurrentColorScheme.test.js` -> **6** Orphaned Functions | **122** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js`** -> AI Confidence: **99.32%**
2. **`test/e2e/webpack.config.js`** -> AI Confidence: **99.32%**
3. **`packages/mui-material/src/styles/components.ts`** -> AI Confidence: **99.32%**
4. **`packages/mui-codemod/src/deprecations/autocomplete-props/autocomplete-props.js`** -> AI Confidence: **99.31%**
5. **`packages/mui-lab/src/Masonry/Masonry.js`** -> AI Confidence: **99.31%**
6. **`packages/mui-lab/src/TimelineDot/TimelineDot.js`** -> AI Confidence: **99.31%**
7. **`packages/mui-material/src/Autocomplete/Autocomplete.js`** -> AI Confidence: **99.31%**
8. **`packages/mui-material/src/Badge/Badge.js`** -> AI Confidence: **99.31%**
9. **`packages/mui-material/src/ButtonBase/ButtonBase.js`** -> AI Confidence: **99.31%**
10. **`packages/mui-material/src/CardMedia/CardMedia.js`** -> AI Confidence: **99.31%**
11. **`packages/mui-material/src/Chip/Chip.js`** -> AI Confidence: **99.31%**
12. **`packages/mui-material/src/Collapse/Collapse.js`** -> AI Confidence: **99.31%**
13. **`packages/mui-material/src/Divider/Divider.js`** -> AI Confidence: **99.31%**
14. **`packages/mui-material/src/FormControlLabel/FormControlLabel.js`** -> AI Confidence: **99.31%**
15. **`packages/mui-material/src/Grow/Grow.js`** -> AI Confidence: **99.31%**
16. **`packages/mui-material/src/InputAdornment/InputAdornment.js`** -> AI Confidence: **99.31%**
17. **`packages/mui-material/src/InputBase/InputBase.js`** -> AI Confidence: **99.31%**
18. **`packages/mui-material/src/ListItemButton/ListItemButton.js`** -> AI Confidence: **99.31%**
19. **`packages/mui-material/src/ListItemText/ListItemText.js`** -> AI Confidence: **99.31%**
20. **`packages/mui-material/src/PaginationItem/PaginationItem.js`** -> AI Confidence: **99.31%**
21. **`packages/mui-material/src/Select/SelectInput.js`** -> AI Confidence: **99.31%**
22. **`packages/mui-material/src/Skeleton/Skeleton.js`** -> AI Confidence: **99.31%**
23. **`packages/mui-material/src/Slide/Slide.js`** -> AI Confidence: **99.31%**
24. **`packages/mui-material/src/SpeedDial/SpeedDial.js`** -> AI Confidence: **99.31%**
25. **`packages/mui-material/src/Step/Step.js`** -> AI Confidence: **99.31%**
26. **`packages/mui-material/src/StepLabel/StepLabel.js`** -> AI Confidence: **99.31%**
27. **`packages/mui-material/src/SvgIcon/SvgIcon.js`** -> AI Confidence: **99.31%**
28. **`packages/mui-material/src/SwipeableDrawer/SwipeableDrawer.js`** -> AI Confidence: **99.31%**
29. **`packages/mui-material/src/Tab/Tab.js`** -> AI Confidence: **99.31%**
30. **`packages/mui-material/src/TableCell/TableCell.js`** -> AI Confidence: **99.31%**
31. **`packages/mui-material/src/TablePaginationActions/TablePaginationActions.js`** -> AI Confidence: **99.31%**
32. **`packages/mui-material/src/TableRow/TableRow.js`** -> AI Confidence: **99.31%**
33. **`packages/mui-material/src/Tabs/Tabs.js`** -> AI Confidence: **99.31%**
34. **`packages/mui-material/src/ToggleButton/ToggleButton.js`** -> AI Confidence: **99.31%**
35. **`packages/mui-material/src/Tooltip/Tooltip.js`** -> AI Confidence: **99.31%**
36. **`packages/mui-material/src/colors/index.js`** -> AI Confidence: **99.31%**
37. **`packages/mui-material/src/internal/SwitchBase.js`** -> AI Confidence: **99.31%**
38. **`packages/mui-material/src/styles/createPalette.js`** -> AI Confidence: **99.31%**
39. **`packages/mui-material/src/styles/createThemeWithVars.js`** -> AI Confidence: **99.31%**
40. **`packages/mui-system/src/ThemeProvider/ThemeProvider.js`** -> AI Confidence: **99.31%**
41. **`packages/mui-system/src/breakpoints/breakpoints.js`** -> AI Confidence: **99.31%**
42. **`packages/mui-system/src/createStyled/createStyled.js`** -> AI Confidence: **99.31%**
43. **`packages/mui-system/src/cssVars/createCssVarsProvider.js`** -> AI Confidence: **99.31%**
44. **`packages-internal/api-docs-builder/utils/parseSlotsAndClasses.ts`** -> AI Confidence: **99.31%**
45. **`packages-internal/core-docs/src/Ad/Ad.tsx`** -> AI Confidence: **99.31%**
46. **`packages-internal/core-docs/src/ApiPage/sections/ClassesSection.tsx`** -> AI Confidence: **99.31%**
47. **`packages-internal/core-docs/src/Document/Document.tsx`** -> AI Confidence: **99.31%**
48. **`packages-internal/core-docs/src/HighlightedCodeWithTabs/HighlightedCodeWithTabs.tsx`** -> AI Confidence: **99.31%**
49. **`packages-internal/core-docs/src/Link/Link.tsx`** -> AI Confidence: **99.31%**
50. **`packages/mui-material/src/Chip/Chip.d.ts`** -> AI Confidence: **99.31%**
51. **`packages/mui-material/src/Dialog/Dialog.d.ts`** -> AI Confidence: **99.31%**
52. **`packages/mui-material/src/Modal/Modal.d.ts`** -> AI Confidence: **99.31%**
53. **`packages/mui-material/src/Popper/BasePopper.tsx`** -> AI Confidence: **99.31%**
54. **`packages/mui-material/src/Slider/useSlider.ts`** -> AI Confidence: **99.31%**
55. **`packages/mui-material/src/Unstable_TrapFocus/FocusTrap.tsx`** -> AI Confidence: **99.31%**
56. **`packages/mui-material/src/colors/index.d.ts`** -> AI Confidence: **99.31%**
57. **`packages/mui-material/src/styles/ThemeProvider.tsx`** -> AI Confidence: **99.31%**
58. **`packages/mui-material/src/styles/adaptV4Theme.d.ts`** -> AI Confidence: **99.31%**
59. **`packages/mui-material/src/utils/index.d.ts`** -> AI Confidence: **99.31%**
60. **`packages/mui-system/src/Grid/createGrid.tsx`** -> AI Confidence: **99.31%**
61. **`packages/mui-utils/src/index.ts`** -> AI Confidence: **99.31%**
62. **`packages/mui-utils/src/useRovingTabIndex/useRovingTabIndex.ts`** -> AI Confidence: **99.31%**
63. **`scripts/buildLlmsDocs/index.ts`** -> AI Confidence: **99.31%**
64. **`examples/material-ui-express-ssr/webpack.config.js`** -> AI Confidence: **99.29%**
65. **`packages/mui-codemod/src/util/assignObject.js`** -> AI Confidence: **99.29%**
66. **`packages/mui-codemod/src/v5.0.0/badge-overlap-value.js`** -> AI Confidence: **99.29%**
67. **`packages/mui-codemod/src/v5.0.0/button-color-prop.test/actual.js`** -> AI Confidence: **99.29%**
68. **`packages/mui-codemod/src/v5.0.0/chip-variant-prop.test/actual.js`** -> AI Confidence: **99.29%**
69. **`packages/mui-codemod/src/v5.0.0/circularprogress-variant.test/actual.js`** -> AI Confidence: **99.29%**
70. **`packages/mui-codemod/src/v5.0.0/circularprogress-variant.test/expected.js`** -> AI Confidence: **99.29%**
71. **`packages/mui-codemod/src/v5.0.0/theme-palette-mode.test/actual.js`** -> AI Confidence: **99.29%**
72. **`packages/mui-codemod/src/v5.0.0/theme-palette-mode.test/expected.js`** -> AI Confidence: **99.29%**
73. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/BasicStyled.actual.js`** -> AI Confidence: **99.29%**
74. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/ObjectMap.actual.js`** -> AI Confidence: **99.29%**
75. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/ObjectMap.expected.js`** -> AI Confidence: **99.29%**
76. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-applyStyles.actual.js`** -> AI Confidence: **99.29%**
77. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-condition.actual.js`** -> AI Confidence: **99.29%**
78. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-condition.expected.js`** -> AI Confidence: **99.29%**
79. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-dynamic2.actual.js`** -> AI Confidence: **99.29%**
80. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-dynamic2.expected.js`** -> AI Confidence: **99.29%**
81. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-inheritance.actual.js`** -> AI Confidence: **99.29%**
82. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-inheritance.expected.js`** -> AI Confidence: **99.29%**
83. **`packages/mui-codemod/src/v9.0.0/system-props/removeSystemProps.js`** -> AI Confidence: **99.29%**
84. **`packages/mui-private-theming/src/ThemeProvider/nested.js`** -> AI Confidence: **99.29%**
85. **`packages-internal/core-docs/src/branding/brandingTheme.ts`** -> AI Confidence: **99.29%**
86. **`packages/mui-lab/src/themeAugmentation/components.ts`** -> AI Confidence: **99.29%**
87. **`packages/mui-material/src/utils/mergeSlotProps.ts`** -> AI Confidence: **99.29%**
88. **`packages/mui-system/src/InitColorSchemeScript/InitColorSchemeScript.tsx`** -> AI Confidence: **99.29%**
89. **`packages/mui-system/src/styleFunctionSx/AliasesCSSProperties.ts`** -> AI Confidence: **99.29%**
90. **`packages/mui-utils/src/resolveProps/resolveProps.ts`** -> AI Confidence: **99.29%**
91. **`packages/mui-codemod/src/v9.0.0/system-props/test-cases/system-props.expected.js`** -> AI Confidence: **99.24%**
92. **`packages/mui-material/src/Alert/Alert.js`** -> AI Confidence: **99.24%**
93. **`packages/mui-material/src/Avatar/Avatar.js`** -> AI Confidence: **99.24%**
94. **`packages/mui-material/src/BottomNavigationAction/BottomNavigationAction.js`** -> AI Confidence: **99.24%**
95. **`packages/mui-material/src/ButtonGroup/ButtonGroup.js`** -> AI Confidence: **99.24%**
96. **`packages/mui-material/src/CardHeader/CardHeader.js`** -> AI Confidence: **99.24%**
97. **`packages/mui-material/src/Fab/Fab.js`** -> AI Confidence: **99.24%**
98. **`packages/mui-material/src/FilledInput/FilledInput.js`** -> AI Confidence: **99.24%**
99. **`packages/mui-material/src/FormControl/FormControl.js`** -> AI Confidence: **99.24%**
100. **`packages/mui-material/src/FormHelperText/FormHelperText.js`** -> AI Confidence: **99.24%**
101. **`packages/mui-material/src/FormLabel/FormLabel.js`** -> AI Confidence: **99.24%**
102. **`packages/mui-material/src/Link/Link.js`** -> AI Confidence: **99.24%**
103. **`packages/mui-material/src/MenuItem/MenuItem.js`** -> AI Confidence: **99.24%**
104. **`packages/mui-material/src/MenuList/MenuList.js`** -> AI Confidence: **99.24%**
105. **`packages/mui-material/src/Paper/Paper.js`** -> AI Confidence: **99.24%**
106. **`packages/mui-material/src/Slider/Slider.js`** -> AI Confidence: **99.24%**
107. **`packages/mui-material/src/SpeedDialAction/SpeedDialAction.js`** -> AI Confidence: **99.24%**
108. **`packages/mui-material/src/SpeedDialIcon/SpeedDialIcon.js`** -> AI Confidence: **99.24%**
109. **`packages/mui-material/src/StepContent/StepContent.js`** -> AI Confidence: **99.24%**
110. **`packages/mui-material/src/Switch/Switch.js`** -> AI Confidence: **99.24%**
111. **`packages/mui-material/src/TablePagination/TablePagination.js`** -> AI Confidence: **99.24%**
112. **`packages/mui-material/src/styles/createThemeNoVars.js`** -> AI Confidence: **99.24%**
113. **`packages/mui-material/src/styles/index.js`** -> AI Confidence: **99.24%**
114. **`packages/mui-material/src/utils/index.js`** -> AI Confidence: **99.24%**
115. **`packages/mui-system/src/index.js`** -> AI Confidence: **99.24%**
116. **`packages-internal/core-docs/src/ApiPage/sections/PropertiesSection.tsx`** -> AI Confidence: **99.24%**
117. **`packages-internal/core-docs/src/ApiPage/sections/SlotsSection.tsx`** -> AI Confidence: **99.24%**
118. **`packages-internal/core-docs/src/ComponentLinkHeader/ComponentLinkHeader.tsx`** -> AI Confidence: **99.24%**
119. **`packages-internal/core-docs/src/DocsApp/GoogleAnalytics.tsx`** -> AI Confidence: **99.24%**
120. **`packages/mui-material/src/Button/Button.d.ts`** -> AI Confidence: **99.24%**
121. **`packages/mui-material/src/InputLabel/InputLabel.d.ts`** -> AI Confidence: **99.24%**
122. **`packages/mui-material/src/ListItemText/ListItemText.d.ts`** -> AI Confidence: **99.24%**
123. **`packages/mui-material/src/Portal/Portal.tsx`** -> AI Confidence: **99.24%**
124. **`packages/mui-material/src/TextField/TextField.d.ts`** -> AI Confidence: **99.24%**
125. **`scripts/canaryRelease.mts`** -> AI Confidence: **99.24%**
126. **`packages/mui-material/src/ListSubheader/ListSubheader.js`** -> AI Confidence: **99.23%**
127. **`examples/material-ui-remix-ts/app/root.tsx`** -> AI Confidence: **99.23%**
128. **`packages/mui-material/src/FormControlLabel/FormControlLabel.d.ts`** -> AI Confidence: **99.23%**
129. **`packages/mui-material/src/Modal/useModal.ts`** -> AI Confidence: **99.23%**
130. **`packages/mui-material/src/NativeSelect/NativeSelect.d.ts`** -> AI Confidence: **99.23%**
131. **`packages/mui-material/src/Rating/Rating.d.ts`** -> AI Confidence: **99.23%**
132. **`packages/mui-system/src/createTheme/createTheme.d.ts`** -> AI Confidence: **99.23%**
133. **`packages/mui-codemod/src/codemod.js`** -> AI Confidence: **99.22%**
134. **`packages/mui-codemod/src/v5.0.0/base-use-named-exports.test/actual.js`** -> AI Confidence: **99.18%**
135. **`packages/mui-codemod/src/v5.0.0/jss-to-styled.test/first.actual.js`** -> AI Confidence: **99.18%**
136. **`packages/mui-codemod/src/v5.0.0/jss-to-styled.test/sixth.expected.js`** -> AI Confidence: **99.18%**
137. **`packages/mui-codemod/src/v5.0.0/theme-spacing.test/large-actual.js`** -> AI Confidence: **99.18%**
138. **`packages/mui-codemod/src/v5.0.0/theme-spacing.test/large-expected.js`** -> AI Confidence: **99.18%**
139. **`packages/mui-material/src/Breadcrumbs/Breadcrumbs.js`** -> AI Confidence: **99.18%**
140. **`packages/mui-material/src/ButtonBase/TouchRipple.js`** -> AI Confidence: **99.18%**
141. **`packages/mui-material/src/DialogContent/DialogContent.js`** -> AI Confidence: **99.18%**
142. **`packages/mui-material/src/Fade/Fade.test.js`** -> AI Confidence: **99.18%**
143. **`packages/mui-material/src/FormGroup/FormGroup.js`** -> AI Confidence: **99.18%**
144. **`packages/mui-material/src/Grow/Grow.test.js`** -> AI Confidence: **99.18%**
145. **`packages/mui-material/src/Input/Input.js`** -> AI Confidence: **99.18%**
146. **`packages/mui-material/src/LinearProgress/LinearProgress.js`** -> AI Confidence: **99.18%**
147. **`packages/mui-material/src/Modal/Modal.js`** -> AI Confidence: **99.18%**
148. **`packages/mui-material/src/RadioGroup/RadioGroup.js`** -> AI Confidence: **99.18%**
149. **`packages/mui-material/src/Snackbar/Snackbar.js`** -> AI Confidence: **99.18%**
150. **`packages/mui-material/src/Stepper/Stepper.js`** -> AI Confidence: **99.18%**
151. **`packages/mui-material/src/Table/Table.js`** -> AI Confidence: **99.18%**
152. **`packages/mui-material/src/Zoom/Zoom.test.js`** -> AI Confidence: **99.18%**
153. **`packages/mui-system/src/cssVars/createCssVarsProvider.test.js`** -> AI Confidence: **99.18%**
154. **`examples/material-ui-pigment-css-nextjs-ts/src/app/page.tsx`** -> AI Confidence: **99.18%**
155. **`examples/material-ui-react-router-ts/app/entry.server.tsx`** -> AI Confidence: **99.18%**
156. **`packages-internal/core-docs/src/ApiPage/list/ClassesList.tsx`** -> AI Confidence: **99.18%**
157. **`packages-internal/core-docs/src/ApiPage/list/ExpandableApiItem.tsx`** -> AI Confidence: **99.18%**
158. **`packages/mui-material/src/Accordion/Accordion.d.ts`** -> AI Confidence: **99.18%**
159. **`packages/mui-material/src/Alert/Alert.d.ts`** -> AI Confidence: **99.18%**
160. **`packages/mui-material/src/Avatar/Avatar.d.ts`** -> AI Confidence: **99.18%**
161. **`packages/mui-material/src/AvatarGroup/AvatarGroup.d.ts`** -> AI Confidence: **99.18%**
162. **`packages/mui-material/src/CardHeader/CardHeader.d.ts`** -> AI Confidence: **99.18%**
163. **`packages/mui-material/src/Drawer/Drawer.d.ts`** -> AI Confidence: **99.18%**
164. **`packages/mui-material/src/OutlinedInput/OutlinedInput.d.ts`** -> AI Confidence: **99.18%**
165. **`packages/mui-material/src/Pagination/Pagination.d.ts`** -> AI Confidence: **99.18%**
166. **`packages/mui-material/src/PaginationItem/PaginationItem.d.ts`** -> AI Confidence: **99.18%**
167. **`packages/mui-material/src/PigmentStack/PigmentStack.tsx`** -> AI Confidence: **99.18%**
168. **`packages/mui-material/src/Select/Select.d.ts`** -> AI Confidence: **99.18%**
169. **`packages/mui-material/src/SpeedDialAction/SpeedDialAction.d.ts`** -> AI Confidence: **99.18%**
170. **`packages/mui-material/src/StepContent/StepContent.d.ts`** -> AI Confidence: **99.18%**
171. **`packages/mui-material/src/StepLabel/StepLabel.d.ts`** -> AI Confidence: **99.18%**
172. **`packages/mui-material/src/TableSortLabel/TableSortLabel.d.ts`** -> AI Confidence: **99.18%**
173. **`packages/mui-material/src/Tooltip/Tooltip.d.ts`** -> AI Confidence: **99.18%**
174. **`packages/mui-material/src/styles/createThemeFoundation.ts`** -> AI Confidence: **99.18%**
175. **`packages/mui-system/src/Container/createContainer.tsx`** -> AI Confidence: **99.18%**
176. **`packages/mui-codemod/src/v5.0.0/avatar-circle-circular.js`** -> AI Confidence: **99.17%**
177. **`packages/mui-codemod/src/v5.0.0/circularprogress-variant.js`** -> AI Confidence: **99.17%**
178. **`packages/mui-codemod/src/v5.0.0/date-pickers-moved-to-x.js`** -> AI Confidence: **99.17%**
179. **`packages/mui-codemod/src/v5.0.0/fab-variant.js`** -> AI Confidence: **99.17%**
180. **`packages/mui-codemod/src/v5.0.0/joy-text-field-to-input.js`** -> AI Confidence: **99.17%**
181. **`packages/mui-codemod/src/v5.0.0/moved-lab-modules.js`** -> AI Confidence: **99.17%**
182. **`packages/mui-codemod/src/v5.0.0/skeleton-variant.js`** -> AI Confidence: **99.17%**
183. **`packages/mui-codemod/src/v5.0.0/table-props.js`** -> AI Confidence: **99.17%**
184. **`packages/mui-codemod/src/v5.0.0/tabs-scroll-buttons.js`** -> AI Confidence: **99.17%**
185. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/NestedSpread.actual.js`** -> AI Confidence: **99.17%**
186. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/ThemePaletteMode.actual.js`** -> AI Confidence: **99.17%**
187. **`packages/mui-codemod/src/v6.0.0/styled/test-cases/VariantAndModeStyled.actual.js`** -> AI Confidence: **99.17%**
188. **`packages/mui-codemod/src/v6.0.0/sx-prop/test-cases/sx-dynamic.actual.js`** -> AI Confidence: **99.17%**
189. **`packages/mui-codemod/src/v6.0.0/system-props/removeSystemProps.js`** -> AI Confidence: **99.17%**
190. **`packages/mui-codemod/src/v7.0.0/theme-color-functions/test-cases/opacity-var.expected.js`** -> AI Confidence: **99.17%**
191. **`packages-internal/core-docs/src/ApiPage/definitions/types.ts`** -> AI Confidence: **99.17%**
192. **`packages/mui-material-nextjs/src/v13-pagesRouter/createCache.ts`** -> AI Confidence: **99.17%**
193. **`packages/mui-material/src/Slider/SliderValueLabel.types.ts`** -> AI Confidence: **99.17%**
194. **`packages/mui-material/src/styles/shouldSkipGeneratingVar.ts`** -> AI Confidence: **99.17%**
195. **`packages/mui-utils/src/ponyfillGlobal/ponyfillGlobal.ts`** -> AI Confidence: **99.17%**
196. **`packages/mui-utils/src/useEnhancedEffect/useEnhancedEffect.ts`** -> AI Confidence: **99.17%**
197. **`eslint.config.mjs`** -> AI Confidence: **99.16%**
198. **`packages/mui-codemod/src/v5.0.0/jss-to-styled.test/sixth.actual.js`** -> AI Confidence: **99.16%**
199. **`packages/mui-icons-material/builder.mjs`** -> AI Confidence: **99.16%**
200. **`packages/mui-lab/src/TimelineItem/TimelineItem.js`** -> AI Confidence: **99.16%**
201. **`packages/mui-lab/src/index.js`** -> AI Confidence: **99.16%**
202. **`packages/mui-material/src/Accordion/Accordion.js`** -> AI Confidence: **99.16%**
203. **`packages/mui-material/src/AccordionSummary/AccordionSummary.js`** -> AI Confidence: **99.16%**
204. **`packages/mui-material/src/AppBar/AppBar.js`** -> AI Confidence: **99.16%**
205. **`packages/mui-material/src/AvatarGroup/AvatarGroup.js`** -> AI Confidence: **99.16%**
206. **`packages/mui-material/src/BottomNavigation/BottomNavigation.js`** -> AI Confidence: **99.16%**
207. **`packages/mui-material/src/Button/Button.js`** -> AI Confidence: **99.16%**
208. **`packages/mui-material/src/Checkbox/Checkbox.js`** -> AI Confidence: **99.16%**
209. **`packages/mui-material/src/CircularProgress/CircularProgress.js`** -> AI Confidence: **99.16%**
210. **`packages/mui-material/src/Drawer/Drawer.js`** -> AI Confidence: **99.16%**
211. **`packages/mui-material/src/IconButton/IconButton.js`** -> AI Confidence: **99.16%**
212. **`packages/mui-material/src/ImageListItem/ImageListItem.js`** -> AI Confidence: **99.16%**
213. **`packages/mui-material/src/InputLabel/InputLabel.js`** -> AI Confidence: **99.16%**
214. **`packages/mui-material/src/List/List.js`** -> AI Confidence: **99.16%**
215. **`packages/mui-material/src/ListItem/ListItem.js`** -> AI Confidence: **99.16%**
216. **`packages/mui-material/src/Menu/Menu.js`** -> AI Confidence: **99.16%**
217. **`packages/mui-material/src/MobileStepper/MobileStepper.js`** -> AI Confidence: **99.16%**
218. **`packages/mui-material/src/Popover/Popover.js`** -> AI Confidence: **99.16%**
219. **`packages/mui-material/src/Radio/Radio.js`** -> AI Confidence: **99.16%**
220. **`packages/mui-material/src/Rating/Rating.js`** -> AI Confidence: **99.16%**
221. **`packages/mui-material/src/StepIcon/StepIcon.js`** -> AI Confidence: **99.16%**
222. **`packages/mui-material/src/TabScrollButton/TabScrollButton.js`** -> AI Confidence: **99.16%**
223. **`packages/mui-material/src/TableSortLabel/TableSortLabel.js`** -> AI Confidence: **99.16%**
224. **`packages/mui-material/src/ToggleButtonGroup/ToggleButtonGroup.js`** -> AI Confidence: **99.16%**
225. **`packages/mui-material/src/index.js`** -> AI Confidence: **99.16%**
226. **`examples/material-ui-nextjs-ts-v4-v5-migration/pages/_app.tsx`** -> AI Confidence: **99.16%**
227. **`packages-internal/core-docs/src/DocsApp/AnalyticsProvider.tsx`** -> AI Confidence: **99.16%**
228. **`packages-internal/core-docs/src/branding/BrandingCssVarsProvider.tsx`** -> AI Confidence: **99.16%**
229. **`packages-internal/scripts/typescript-to-proptypes/test/typescript-to-proptypes.test.ts`** -> AI Confidence: **99.16%**
230. **`packages/mui-lab/src/index.d.ts`** -> AI Confidence: **99.16%**
231. **`packages/mui-material/src/Autocomplete/Autocomplete.d.ts`** -> AI Confidence: **99.16%**
232. **`packages/mui-material/src/PigmentContainer/PigmentContainer.tsx`** -> AI Confidence: **99.16%**
233. **`packages/mui-material/src/index.d.ts`** -> AI Confidence: **99.16%**
234. **`packages/mui-material/src/styles/index.d.ts`** -> AI Confidence: **99.16%**
235. **`packages/mui-system/src/Stack/createStack.tsx`** -> AI Confidence: **99.16%**
236. **`packages/mui-system/src/index.d.ts`** -> AI Confidence: **99.16%**
237. **`scripts/generateProptypes.ts`** -> AI Confidence: **99.16%**
238. **`packages/mui-lab/src/TabPanel/TabPanel.js`** -> AI Confidence: **99.15%**
239. **`packages/mui-material/src/Fade/Fade.js`** -> AI Confidence: **99.15%**
240. **`packages/mui-material/src/Icon/Icon.js`** -> AI Confidence: **99.15%**
241. **`packages/mui-material/src/NativeSelect/NativeSelectInput.js`** -> AI Confidence: **99.15%**
242. **`packages/mui-material/src/ScopedCssBaseline/ScopedCssBaseline.js`** -> AI Confidence: **99.15%**
243. **`packages/mui-material/src/SnackbarContent/SnackbarContent.js`** -> AI Confidence: **99.15%**
244. **`packages/mui-material/src/StepConnector/StepConnector.js`** -> AI Confidence: **99.15%**
245. **`packages/mui-material/src/Typography/Typography.js`** -> AI Confidence: **99.15%**
246. **`packages/mui-material/src/Zoom/Zoom.js`** -> AI Confidence: **99.15%**
247. **`packages/mui-material/src/styles/createTheme.test.js`** -> AI Confidence: **99.15%**
248. **`examples/material-ui-react-router-ts/app/root.tsx`** -> AI Confidence: **99.15%**
249. **`packages-internal/api-docs-builder/utils/generatePropDescription.ts`** -> AI Confidence: **99.15%**
250. **`packages-internal/core-docs/src/ApiPage/list/PropertiesList.tsx`** -> AI Confidence: **99.15%**
251. **`packages-internal/core-docs/src/ApiPage/sections/ToggleDisplayOption.tsx`** -> AI Confidence: **99.15%**
252. **`packages-internal/core-docs/src/ThemeContext/ThemeContext.tsx`** -> AI Confidence: **99.15%**
253. **`packages/mui-material/src/AppBar/AppBar.d.ts`** -> AI Confidence: **99.15%**
254. **`packages/mui-material/src/Badge/Badge.d.ts`** -> AI Confidence: **99.15%**
255. **`packages/mui-material/src/BottomNavigationAction/BottomNavigationAction.d.ts`** -> AI Confidence: **99.15%**
256. **`packages/mui-material/src/Breadcrumbs/Breadcrumbs.d.ts`** -> AI Confidence: **99.15%**
257. **`packages/mui-material/src/Collapse/Collapse.d.ts`** -> AI Confidence: **99.15%**
258. **`packages/mui-material/src/Fab/Fab.d.ts`** -> AI Confidence: **99.15%**
259. **`packages/mui-material/src/Grid/Grid.tsx`** -> AI Confidence: **99.15%**
260. **`packages/mui-material/src/IconButton/IconButton.d.ts`** -> AI Confidence: **99.15%**
261. **`packages/mui-material/src/Link/Link.d.ts`** -> AI Confidence: **99.15%**
262. **`packages/mui-material/src/PigmentGrid/PigmentGrid.tsx`** -> AI Confidence: **99.15%**
263. **`packages/mui-material/src/Snackbar/Snackbar.d.ts`** -> AI Confidence: **99.15%**
264. **`packages/mui-material/src/SpeedDial/SpeedDial.d.ts`** -> AI Confidence: **99.15%**
265. **`packages/mui-material/src/StepContent/StepContent.spec.tsx`** -> AI Confidence: **99.15%**
266. **`packages/mui-material/src/TabScrollButton/TabScrollButton.d.ts`** -> AI Confidence: **99.15%**
267. **`packages/mui-material/src/TextareaAutosize/TextareaAutosize.tsx`** -> AI Confidence: **99.15%**
268. **`packages/mui-material/src/ToggleButton/ToggleButton.d.ts`** -> AI Confidence: **99.15%**
269. **`packages/mui-material/src/Typography/Typography.d.ts`** -> AI Confidence: **99.15%**
270. **`packages/mui-material/src/styles/createThemeNoVars.d.ts`** -> AI Confidence: **99.15%**
271. **`packages/mui-material/src/utils/useSlot.test.tsx`** -> AI Confidence: **99.15%**
272. **`packages/mui-codemod/src/deprecations/tabs-props/tabs-props.js`** -> AI Confidence: **99.13%**
273. **`packages/mui-codemod/src/deprecations/utils/movePropIntoSlotProps.js`** -> AI Confidence: **99.13%**
274. **`packages/mui-codemod/src/deprecations/utils/movePropIntoSlots.js`** -> AI Confidence: **99.13%**
275. **`packages/mui-material/src/useAutocomplete/useAutocomplete.js`** -> AI Confidence: **99.13%**
276. **`packages/mui-system/src/styleFunctionSx/styleFunctionSx.js`** -> AI Confidence: **99.13%**
277. **`scripts/useReactVersion.mjs`** -> AI Confidence: **99.13%**
278. **`packages-internal/core-docs/src/IconImage/IconImage.tsx`** -> AI Confidence: **99.13%**
279. **`packages-internal/core-docs/src/InfoCard/InfoCard.tsx`** -> AI Confidence: **99.13%**
280. **`packages/mui-material/src/ImageListItemBar/ImageListItemBar.d.ts`** -> AI Confidence: **99.13%**
281. **`packages/mui-material/src/InputBase/InputBase.d.ts`** -> AI Confidence: **99.13%**
282. **`packages/mui-material/src/Tab/Tab.d.ts`** -> AI Confidence: **99.13%**
283. **`packages/mui-material/src/internal/SwitchBase.d.ts`** -> AI Confidence: **99.13%**
284. **`packages/mui-utils/src/mergeSlotProps/mergeSlotProps.ts`** -> AI Confidence: **99.13%**
285. **`packages-internal/api-docs-builder/utils/defaultPropsHandler.ts`** -> AI Confidence: **99.11%**
286. **`packages/mui-material/src/styles/stringifyTheme.ts`** -> AI Confidence: **99.11%**
287. **`examples/material-ui-express-ssr/server.js`** -> AI Confidence: **99.09%**
288. **`packages-internal/markdown/parseMarkdown.mjs`** -> AI Confidence: **99.09%**
289. **`packages/mui-codemod/src/deprecations/all/deprecations-all.js`** -> AI Confidence: **99.09%**
290. **`packages/mui-codemod/src/deprecations/all/postcss.config.js`** -> AI Confidence: **99.09%**
291. **`packages/mui-codemod/src/v1.0.0/import-path.test/actual.js`** -> AI Confidence: **99.09%**
292. **`packages/mui-codemod/src/v1.0.0/import-path.test/expected.js`** -> AI Confidence: **99.09%**
293. **`packages/mui-codemod/src/v4.0.0/optimal-imports.js`** -> AI Confidence: **99.09%**
294. **`packages/mui-codemod/src/v4.0.0/optimal-imports.test/actual.js`** -> AI Confidence: **99.09%**
295. **`packages/mui-codemod/src/v4.0.0/optimal-imports.test/expected.js`** -> AI Confidence: **99.09%**
296. **`packages/mui-codemod/src/v4.0.0/top-level-imports.test/actual.js`** -> AI Confidence: **99.09%**
297. **`packages/mui-codemod/src/v5.0.0/base-use-named-exports.test/expected.js`** -> AI Confidence: **99.09%**
298. **`packages/mui-codemod/src/v5.0.0/date-pickers-moved-to-x.test/actual-sub-module.js`** -> AI Confidence: **99.09%**
299. **`packages/mui-codemod/src/v5.0.0/date-pickers-moved-to-x.test/expected-sub-module.js`** -> AI Confidence: **99.09%**
300. **`packages/mui-codemod/src/v5.0.0/jss-to-styled.test/eighth.actual.js`** -> AI Confidence: **99.09%**
301. **`packages/mui-codemod/src/v5.0.0/jss-to-styled.test/eighth.expected.js`** -> AI Confidence: **99.09%**
302. **`packages/mui-codemod/src/v5.0.0/material-ui-styles.test/core-import.expected.js`** -> AI Confidence: **99.09%**
303. **`packages/mui-codemod/src/v5.0.0/material-ui-styles.test/expected.js`** -> AI Confidence: **99.09%**
304. **`packages/mui-codemod/src/v5.0.0/mui-replace.test/actual.js`** -> AI Confidence: **99.09%**
305. **`packages/mui-codemod/src/v5.0.0/mui-replace.test/expected.js`** -> AI Confidence: **99.09%**
306. **`packages/mui-codemod/src/v5.0.0/optimal-imports.js`** -> AI Confidence: **99.09%**
307. **`packages/mui-codemod/src/v5.0.0/optimal-imports.test/actual.js`** -> AI Confidence: **99.09%**
308. **`packages/mui-codemod/src/v5.0.0/path-imports.test/expected.js`** -> AI Confidence: **99.09%**
309. **`packages/mui-codemod/src/v5.0.0/preset-safe.js`** -> AI Confidence: **99.09%**
310. **`packages/mui-codemod/src/v5.0.0/top-level-imports.js`** -> AI Confidence: **99.09%**
311. **`packages/mui-codemod/src/v5.0.0/top-level-imports.test/actual.js`** -> AI Confidence: **99.09%**
312. **`packages/mui-codemod/src/v6.0.0/system-props/test-cases/system-props.expected.js`** -> AI Confidence: **99.09%**
313. **`packages/mui-codemod/src/v6.0.0/theme-v6/theme-v6.js`** -> AI Confidence: **99.09%**
314. **`packages/mui-codemod/src/v7.0.0/lab-removed-components/test-cases/component-file-actual.js`** -> AI Confidence: **99.09%**
315. **`packages/mui-codemod/src/v7.0.0/lab-removed-components/test-cases/component-file-expected.js`** -> AI Confidence: **99.09%**
316. **`packages/mui-material/src/Accordion/Accordion.test.js`** -> AI Confidence: **99.09%**
317. **`packages/mui-material/src/Checkbox/Checkbox.test.js`** -> AI Confidence: **99.09%**
318. **`packages/mui-material/src/Chip/Chip.test.js`** -> AI Confidence: **99.09%**
319. **`packages/mui-material/src/IconButton/IconButton.test.js`** -> AI Confidence: **99.09%**
320. **`packages/mui-material/src/InputBase/InputBase.test.js`** -> AI Confidence: **99.09%**
321. **`packages/mui-material/src/InputLabel/InputLabel.test.js`** -> AI Confidence: **99.09%**
322. **`packages/mui-material/src/Menu/Menu.test.js`** -> AI Confidence: **99.09%**
323. **`packages/mui-material/src/MenuItem/MenuItem.test.js`** -> AI Confidence: **99.09%**
324. **`packages/mui-material/src/MenuList/MenuList.test.js`** -> AI Confidence: **99.09%**
325. **`packages/mui-material/src/Modal/Modal.test.js`** -> AI Confidence: **99.09%**
326. **`packages/mui-material/src/Popover/Popover.test.js`** -> AI Confidence: **99.09%**
327. **`packages/mui-material/src/StepButton/StepButton.test.js`** -> AI Confidence: **99.09%**
328. **`packages/mui-material/src/TablePagination/TablePagination.test.js`** -> AI Confidence: **99.09%**
329. **`packages/mui-material/src/TextField/TextField.js`** -> AI Confidence: **99.09%**
330. **`packages/mui-system/src/createTheme/index.js`** -> AI Confidence: **99.09%**
331. **`packages/mui-system/src/spacing/spacing.js`** -> AI Confidence: **99.09%**
332. **`scripts/generateCodeowners.mjs`** -> AI Confidence: **99.09%**
333. **`test/bundling/scripts/fixtureTemplateValues.js`** -> AI Confidence: **99.09%**
334. **`examples/material-ui-remix-ts/app/entry.server.tsx`** -> AI Confidence: **99.09%**
335. **`netlify/functions/feedback-management.mts`** -> AI Confidence: **99.09%**
336. **`packages-internal/api-docs-builder/utils/resolveExportSpecifier.ts`** -> AI Confidence: **99.09%**
337. **`packages-internal/core-docs/src/Link/MarkdownLinks.ts`** -> AI Confidence: **99.09%**
338. **`packages-internal/core-docs/src/Link/SkipLink.tsx`** -> AI Confidence: **99.09%**
339. **`packages-internal/core-docs/src/SectionHeadline/SectionHeadline.tsx`** -> AI Confidence: **99.09%**
340. **`packages-internal/scripts/typescript-to-proptypes/src/generatePropTypes.ts`** -> AI Confidence: **99.09%**
341. **`packages/mui-lab/src/themeAugmentation/overrides.ts`** -> AI Confidence: **99.09%**
342. **`packages/mui-lab/src/themeAugmentation/props.ts`** -> AI Confidence: **99.09%**
343. **`packages/mui-material/src/Badge/useBadge.ts`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6461` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/mui-utils/src/debounce/debounce.ts` (TYPESCRIPT) -> Cumulative Risk: **631.16**
- **Archetype:** `file_cluster_4` (Distance: 12.597 IQR)
- **Magnitude:** 2.24 | **LOC:** 24 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9988%), Cognitive Load (99.9537%)
- **Heaviest Functions:** `clear` (Impact: 3.9), `debounced` (Impact: 2.4), `later` (Impact: 1.9)

### 2. `packages-internal/waterfall/Queue.mjs` (JAVASCRIPT) -> Cumulative Risk: **624.08**
- **Archetype:** `file_cluster_4` (Distance: 14.257 IQR)
- **Magnitude:** 100.26 | **LOC:** 59 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9988%)
- **Heaviest Functions:** `process` (Impact: 9.5), `waitUntil` (Impact: 8.7), `push` (Impact: 1.9)

### 3. `packages-internal/core-docs/src/Ad/Ad.tsx` (TYPESCRIPT) -> Cumulative Risk: **574.98**
- **Archetype:** `file_cluster_13` (Distance: 10.143 IQR)
- **Magnitude:** 12.24 | **LOC:** 235 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9878%), Documentation (81.1624%), Verification (80.0%)
- **Heaviest Functions:** `Ad` (Impact: 54.6), `clearTimeout` (Impact: 5.3), `checkAdblock` (Impact: 4.3)

### 4. `packages-internal/waterfall/retry.mjs` (JAVASCRIPT) -> Cumulative Risk: **553.67**
- **Archetype:** `file_cluster_4` (Distance: 11.818 IQR)
- **Magnitude:** 20.5 | **LOC:** 35 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9973%), Concurrency (99.9914%), Cognitive Load (99.0806%)
- **Heaviest Functions:** `bail` (Impact: 1.9), `retry` (Impact: 1.1)

### 5. `packages/mui-utils/src/useTimeout/useTimeout.ts` (TYPESCRIPT) -> Cumulative Risk: **528.95**
- **Archetype:** `file_cluster_4` (Distance: 12.513 IQR)
- **Magnitude:** 4.14 | **LOC:** 42 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Safety Score (82.2882%)
- **Heaviest Functions:** `clear` (Impact: 3.8), `start` (Impact: 2.1), `useTimeout` (Impact: 2.1)

### 6. `packages-internal/core-docs/src/DocsApp/serviceWorker.ts` (TYPESCRIPT) -> Cumulative Risk: **522.26**
- **Archetype:** `file_cluster_4` (Distance: 9.639 IQR)
- **Magnitude:** 6.29 | **LOC:** 67 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9996%), Tech Debt (99.9918%), Cognitive Load (84.1131%)
- **Heaviest Functions:** `forcePageReload` (Impact: 17.9), `listenInstalledStateChange` (Impact: 9.3), `registerServiceWorker` (Impact: 8.6)

### 7. `packages-internal/core-docs/src/CodeCopy/CodeCopy.tsx` (TYPESCRIPT) -> Cumulative Risk: **518.92**
- **Archetype:** `file_cluster_17` (Distance: 12.871 IQR)
- **Magnitude:** 17.84 | **LOC:** 200 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9566%), Verification (80.0%), Safety Score (67.5902%)
- **Heaviest Functions:** `InitCodeCopy` (Impact: 42.8), `handleClick` (Impact: 20.9), `hasNativeSelection` (Impact: 14.7)

### 8. `packages-internal/markdown/loader.mjs` (JAVASCRIPT) -> Cumulative Risk: **514.05**
- **Archetype:** `file_cluster_17` (Distance: 11.786 IQR)
- **Magnitude:** 163.78 | **LOC:** 720 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.4039%), Tech Debt (84.5153%), Verification (80.0%)
- **Heaviest Functions:** `demoLoader` (Impact: 62.8), `findComponents` (Impact: 13.4), `extractImports` (Impact: 4.3)

### 9. `packages-internal/api-docs-builder/utils/extractInfoFromEnum.ts` (TYPESCRIPT) -> Cumulative Risk: **504.06**
- **Archetype:** `file_cluster_17` (Distance: 11.681 IQR)
- **Magnitude:** 6.99 | **LOC:** 71 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (93.3201%)
- **Heaviest Functions:** `extractInfoFromEnum` (Impact: 27.1), `parseProperty` (Impact: 7.3), `forEachChild` (Impact: 5.4)

### 10. `packages/mui-material/src/internal/animate.js` (JAVASCRIPT) -> Cumulative Risk: **491.13**
- **Archetype:** `file_cluster_8` (Distance: 10.199 IQR)
- **Magnitude:** 31.18 | **LOC:** 50 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (87.1019%), Cognitive Load (58.755%)
- **Heaviest Functions:** `step` (Impact: 8.0), `cb` (Impact: 2.4), `requestAnimationFrame` (Impact: 2.4)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages-internal/markdown/parseMarkdown.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.197 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 10.197, file_cluster_17: 10.513, file_cluster_13: 10.707
- **Magnitude:** 2636.83 | **LOC:** 504 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.3267%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 43`, `args: 20`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `io: 7`, `api: 1`, `import: 3`
* *Defense:* `safety: 12`, `doc: 7`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` prism.mjs, marked, textToHash.mjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/Autocomplete/Autocomplete.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.811 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.911 IQR)
- **Top Global Matches:** file_cluster_8: 9.811, file_cluster_2: 9.993, file_cluster_1: 10.509
- **Magnitude:** 923.98 | **LOC:** 3969 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (3.0873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 116.0)
  * `describe` (Impact: 25.1)
  * `describe` (Impact: 24.9)
  * `describe` (Impact: 17.5)
  * `describe` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 300`, `args: 269`, `func_start: 441`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 2`, `planned_debt: 1`, `duplicate_logic: 276`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 15`, `import: 13`
* *Defense:* `safety: 14`, `test: 301`, `immutability_locks: 169`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` styles, InputAdornment, Box, Chip, describeConformance, Tooltip, sinon, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-codemod/src/util/migrateToVariants.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.162 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.935 IQR)
- **Top Global Matches:** file_cluster_17: 13.162, file_cluster_8: 13.269, file_cluster_7: 13.581
- **Magnitude:** 814.62 | **LOC:** 682 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.4405%), Tech Debt (99.9982%)
**Top Internal Functions/Classes:**
  * `migrateToVariants` (Impact: 267.1)
  * `recurseObjectExpression` (Impact: 123.2)
  * `appendPaletteModeStyles` (Impact: 35.8)
  * `removeProperty` (Impact: 35.7)
  * `buildProps` (Impact: 34.0)
    * *Intent:* /** *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 86`, `args: 53`, `func_start: 49`
* *Risk/State:* `state_mutation: 87`, `duplicate_logic: 31`
* *Architecture:* `api: 10`
* *Defense:* `safety: 129`, `doc: 35`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v6.0.0/sx-prop/sx-v6.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.606 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.922 IQR)
- **Top Global Matches:** file_cluster_17: 12.606, file_cluster_8: 12.672, file_cluster_13: 12.997
- **Magnitude:** 805.74 | **LOC:** 530 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.5907%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `sxV6` (Impact: 295.4)
  * `recurseObjectExpression` (Impact: 201.3)
  * `appendPaletteModeStyles` (Impact: 62.9)
  * `removeProperty` (Impact: 28.5)
  * `getCssVarName` (Impact: 16.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 39`, `args: 29`, `func_start: 45`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`, `duplicate_logic: 37`
* *Architecture:* `io: 7`, `api: 2`, `import: 2`
* *Defense:* `safety: 106`, `doc: 11`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` getReturnExpression, jscodeshift, migrateToVariants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Tabs/Tabs.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.885 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.106 IQR)
- **Top Global Matches:** file_cluster_8: 9.885, file_cluster_2: 9.959, file_cluster_7: 10.654
- **Magnitude:** 792.62 | **LOC:** 1753 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (12.0039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 43.1)
  * `describe` (Impact: 32.1)
  * `describe` (Impact: 20.9)
  * `describe` (Impact: 16.9)
  * `describe` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 258`, `args: 173`, `func_start: 387`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `duplicate_logic: 166`, `orphaned_logic: 2`
* *Architecture:* `io: 2`, `concurrency: 112`, `import: 11`
* *Defense:* `safety: 4`, `test: 303`, `immutability_locks: 144`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Tab, styles, utils, Tabs, describeConformance, sinon, react, SvgIcon...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/useAutocomplete/useAutocomplete.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.769 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.632 IQR)
- **Top Global Matches:** file_cluster_8: 11.769, file_cluster_17: 11.834, file_cluster_13: 12.006
- **Magnitude:** 777.92 | **LOC:** 1331 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (37.0971%), Tech Debt (99.9989%)
**Top Internal Functions/Classes:**
  * `validOptionIndex` (Impact: 233.9)
  * `selectNewValue` (Impact: 40.3)
  * `useAutocomplete` (Impact: 29.1)
  * `handleBlur` (Impact: 28.9)
  * `validItemIndex` (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 114`, `args: 58`, `func_start: 96`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 49`, `dead_code: 1`, `duplicate_logic: 41`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 77`, `doc: 2`, `immutability_locks: 73`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` usePreviousProps, useControlled, react, useEventCallback, useId, setRef
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `packages/mui-material/src/Select/Select.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_2` (Drift: 9.968 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.22 IQR)
- **Top Global Matches:** file_cluster_2: 9.968, file_cluster_8: 10.104, file_cluster_13: 10.66
- **Magnitude:** 640.54 | **LOC:** 1987 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (6.1081%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 103.1)
  * `describe` (Impact: 33.4)
  * `describe` (Impact: 12.4)
  * `describe` (Impact: 11.3)
  * `describe` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 175`, `args: 141`, `func_start: 297`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 5`, `planned_debt: 6`, `duplicate_logic: 171`
* *Architecture:* `concurrency: 49`, `import: 17`
* *Defense:* `safety: 1`, `test: 222`, `immutability_locks: 72`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` InputBase, styles, MenuItem, OutlinedInput, describeConformance, NativeSelect, selectClasses, sinon...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-system/src/cssVars/createCssVarsProvider.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.649 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.709 IQR)
- **Top Global Matches:** file_cluster_8: 9.649, file_cluster_2: 9.872, file_cluster_13: 10.211
- **Magnitude:** 549.92 | **LOC:** 931 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 107.8)
  * `describe` (Impact: 52.3)
  * `describe` (Impact: 30.3)
  * `describe` (Impact: 22.8)
  * `describe` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 118`, `args: 96`, `func_start: 158`
* *Risk/State:* `state_mutation: 15`, `dead_code: 2`, `duplicate_logic: 88`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `import: 8`
* *Defense:* `safety: 14`, `doc: 2`, `test: 96`, `immutability_locks: 63`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` createCssVarsProvider, useTheme, system, sinon, InitColorSchemeScript, internal-test-utils, chai, createCssVarsTheme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/styles/extendTheme.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.902 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.491 IQR)
- **Top Global Matches:** file_cluster_8: 9.902, file_cluster_7: 10.63, file_cluster_0: 10.668
- **Magnitude:** 523.8 | **LOC:** 875 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8485%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 112.6)
  * `describe` (Impact: 22.4)
  * `describe` (Impact: 12.5)
  * `describe` (Impact: 11.4)
  * `describe` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 142`, `args: 108`, `func_start: 237`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`, `duplicate_logic: 100`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 4`, `test: 227`, `immutability_locks: 67`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` styles, Button, sinon, colors, internal-test-utils, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-codemod/src/v5.0.0/jss-to-styled.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.849 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.103 IQR)
- **Top Global Matches:** file_cluster_17: 11.849, file_cluster_8: 12.123, file_cluster_0: 12.422
- **Magnitude:** 512.46 | **LOC:** 647 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.566%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 281.8)
    * *Intent:* /**
  * `getRootClassKeys` (Impact: 28.6)
    * *Intent:* // Self closing tag
  * `convertToStyledArg` (Impact: 26.9)
  * `getPrefix` (Impact: 19.1)
    * *Intent:* /** * @param {string} filePath * @example computePrefixFromPath('/a/b/c/Anonymous.tsx') === 'Anonymo...
  * `getReturnStatement` (Impact: 19.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 76`, `args: 51`, `func_start: 15`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 69`, `api: 2`, `import: 1`
* *Defense:* `safety: 68`, `doc: 26`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` path, jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-codemod/src/v5.0.0/jss-to-tss-react.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.65 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.264 IQR)
- **Top Global Matches:** file_cluster_17: 12.65, file_cluster_8: 12.936, file_cluster_0: 12.942
- **Magnitude:** 503.94 | **LOC:** 491 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.7897%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 124.5)
    * *Intent:* /**
  * `transformStylesExpression` (Impact: 96.2)
  * `transformNestedKeys` (Impact: 36.6)
  * `addCommentsToClosestDeclaration` (Impact: 28.0)
  * `transformNestedKeys` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 59`, `args: 36`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`, `planned_debt: 5`, `duplicate_logic: 21`
* *Architecture:* `io: 48`, `api: 2`
* *Defense:* `safety: 55`, `doc: 7`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/mui-system/src/cssVars/useCurrentColorScheme.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.147 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.882 IQR)
- **Top Global Matches:** file_cluster_8: 9.147, file_cluster_2: 9.68, file_cluster_13: 9.945
- **Magnitude:** 489.48 | **LOC:** 941 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.3598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 75.9)
  * `describe` (Impact: 28.2)
  * `describe` (Impact: 21.5)
  * `describe` (Impact: 12.5)
  * `it` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 138`, `args: 126`, `func_start: 162`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 122`, `orphaned_logic: 6`
* *Architecture:* `io: 11`, `import: 6`
* *Defense:* `safety: 7`, `test: 87`, `immutability_locks: 59`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sinon, react, InitColorSchemeScript, internal-test-utils, useCurrentColorScheme, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/styles/styled.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.379 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.001 IQR)
- **Top Global Matches:** file_cluster_8: 10.379, file_cluster_2: 10.414, file_cluster_17: 10.78
- **Magnitude:** 481.86 | **LOC:** 671 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.882%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 105.6)
  * `describe` (Impact: 92.7)
  * `it` (Impact: 16.2)
  * `beforeAll` (Impact: 13.1)
    * *Intent:* /** * @type {ReturnType<typeof styled>} */
  * `it` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 78`, `args: 64`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 9`, `duplicate_logic: 75`, `orphaned_logic: 1`
* *Architecture:* `import: 6`
* *Defense:* `safety: 35`, `doc: 6`, `test: 73`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, internal-test-utils, createTheme, ThemeProvider, styled, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-system/src/styled/styled.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.225 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.906 IQR)
- **Top Global Matches:** file_cluster_8: 10.225, file_cluster_2: 10.289, file_cluster_17: 10.681
- **Magnitude:** 481.6 | **LOC:** 694 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 103.3)
  * `describe` (Impact: 90.4)
  * `it` (Impact: 16.2)
  * `beforeAll` (Impact: 13.4)
    * *Intent:* /** * @type {ReturnType<typeof styled>} */
  * `it` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 79`, `args: 70`, `func_start: 93`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `duplicate_logic: 85`, `orphaned_logic: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 35`, `doc: 6`, `test: 74`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chai, internal-test-utils, system, createTheme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/styles/createTheme.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.257 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.335 IQR)
- **Top Global Matches:** file_cluster_8: 10.257, file_cluster_13: 10.795, file_cluster_2: 10.924
- **Magnitude:** 477.1 | **LOC:** 841 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.7838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 127.6)
  * `describe` (Impact: 22.5)
  * `describe` (Impact: 21.5)
  * `it` (Impact: 11.9)
  * `it` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 110`, `args: 70`, `func_start: 196`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 39`, `duplicate_logic: 72`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `import: 10`
* *Defense:* `safety: 14`, `test: 187`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` GlobalStyles, styles, createPalette, Button, colorManipulator, Alert, colors, internal-test-utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-system/src/spacing/spacing.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.648 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.964 IQR)
- **Top Global Matches:** file_cluster_8: 9.648, file_cluster_0: 10.374, file_cluster_7: 10.405
- **Magnitude:** 462.0 | **LOC:** 708 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9528%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 61.2)
  * `describe` (Impact: 26.6)
  * `describe` (Impact: 17.8)
  * `describe` (Impact: 17.8)
  * `describe` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 102`, `args: 70`, `func_start: 133`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 48`, `duplicate_logic: 130`
* *Architecture:* `import: 2`
* *Defense:* `test: 131`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chai, spacing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/ButtonBase/ButtonBase.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.426 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.07 IQR)
- **Top Global Matches:** file_cluster_8: 9.426, file_cluster_2: 9.768, file_cluster_7: 10.101
- **Magnitude:** 456.42 | **LOC:** 1602 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (12.2034%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 74.8)
  * `expect` (Impact: 24.3)
  * `describe` (Impact: 24.0)
  * `describe` (Impact: 14.5)
  * `describe` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 123`, `args: 62`, `func_start: 170`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 3`, `duplicate_logic: 69`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `concurrency: 71`, `import: 9`
* *Defense:* `safety: 3`, `doc: 6`, `test: 129`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` styles, ButtonBase, describeConformance, sinon, react, ButtonBase, internal-test-utils, prop-types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/Chip/Chip.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_2` (Drift: 9.642 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.96 IQR)
- **Top Global Matches:** file_cluster_2: 9.642, file_cluster_8: 9.643, file_cluster_13: 10.247
- **Magnitude:** 427.96 | **LOC:** 839 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (2.5207%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 64.8)
  * `describe` (Impact: 20.3)
  * `describe` (Impact: 14.5)
  * `describe` (Impact: 14.4)
  * `describe` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 246`, `args: 136`, `func_start: 252`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 1`, `planned_debt: 2`, `duplicate_logic: 115`
* *Architecture:* `import: 10`
* *Defense:* `doc: 6`, `test: 203`, `immutability_locks: 110`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` styles, Chip, describeConformance, CheckBox, Avatar, sinon, react, defaultTheme...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-system/src/colorManipulator/colorManipulator.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.547 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.787 IQR)
- **Top Global Matches:** file_cluster_8: 9.547, file_cluster_7: 10.316, file_cluster_15: 10.368
- **Magnitude:** 386.46 | **LOC:** 486 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.539%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 61.5)
  * `describe` (Impact: 16.5)
  * `describe` (Impact: 11.4)
  * `describe` (Impact: 10.1)
  * `describe` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 117`, `args: 113`, `func_start: 223`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 3`, `duplicate_logic: 118`
* *Architecture:* `import: 3`
* *Defense:* `test: 214`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chai, system, colorManipulator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/styles/ThemeProviderWithVars.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.051 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_8: 11.051, file_cluster_2: 11.074, file_cluster_13: 11.301
- **Magnitude:** 378.64 | **LOC:** 551 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.2189%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 56.3)
  * `describe` (Impact: 15.3)
  * `it` (Impact: 12.8)
  * `describe` (Impact: 10.3)
  * `it` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 155`, `args: 64`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 98`, `duplicate_logic: 61`, `orphaned_logic: 7`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 6`, `test: 56`, `immutability_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` styles, react, internal-test-utils, Box, chai
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-material/src/TablePagination/TablePagination.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.809 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.804 IQR)
- **Top Global Matches:** file_cluster_8: 8.809, file_cluster_2: 9.069, file_cluster_13: 9.558
- **Magnitude:** 339.46 | **LOC:** 845 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (2.676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 58.1)
  * `describe` (Impact: 13.1)
  * `expect` (Impact: 12.1)
  * `it` (Impact: 11.8)
  * `describe` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 96`, `args: 63`, `func_start: 131`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `duplicate_logic: 79`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `import: 16`
* *Defense:* `safety: 3`, `test: 103`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` utils, OutlinedInput, Input, TableFooter, TableRow, describeConformance, sinon, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/mui-codemod/src/deprecations/autocomplete-props/autocomplete-props.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.118 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.009 IQR)
- **Top Global Matches:** file_cluster_17: 12.118, file_cluster_8: 12.277, file_cluster_13: 12.505
- **Magnitude:** 334.64 | **LOC:** 507 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.0332%), Tech Debt (99.984%)
**Top Internal Functions/Classes:**
  * `transformer` (Impact: 55.5)
    * *Intent:* /**
  * `transformRenderInput` (Impact: 29.4)
  * `renameRenderTagsCallback` (Impact: 22.8)
  * `ensureParamsSlotPropsSpread` (Impact: 21.5)
  * `renameUseAutocompleteReturnMembers` (Impact: 21.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 58`, `args: 43`, `func_start: 44`
* *Risk/State:* `state_mutation: 43`, `duplicate_logic: 19`
* *Architecture:* `io: 29`, `api: 2`, `import: 7`
* *Defense:* `safety: 73`, `doc: 3`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` movePropIntoSlots, movePropIntoSlotProps, replaceComponentsWithSlots, appendAttribute, findComponentDefaultProps, assignObject, jscodeshift, findComponentJSX
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-system/src/cssVars/createCssVarsProvider.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.404 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.889 IQR)
- **Top Global Matches:** file_cluster_17: 11.404, file_cluster_13: 11.422, file_cluster_8: 11.546
- **Magnitude:** 323.26 | **LOC:** 413 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createCssVarsProvider` (Impact: 120.6)
  * `CssVarsProvider` (Impact: 115.4)
  * `useEnhancedEffect` (Impact: 51.3)
  * `useColorScheme` (Impact: 3.6)
  * `setColorScheme` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 43`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 34`, `doc: 9`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` private-theming, useEnhancedEffect, ThemeProvider, react, InitColorSchemeScript, useCurrentColorScheme, prop-types, styled-engine
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/mui-system/src/breakpoints/breakpoints.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.896 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.107 IQR)
- **Top Global Matches:** file_cluster_8: 8.896, file_cluster_7: 9.707, file_cluster_0: 9.844
- **Magnitude:** 321.96 | **LOC:** 279 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.3611%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 61.7)
  * `describe` (Impact: 44.3)
  * `describe` (Impact: 23.3)
  * `describe` (Impact: 22.7)
  * `describe` (Impact: 15.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 43`, `args: 35`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 58`
* *Architecture:* `import: 3`
* *Defense:* `test: 64`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.056
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` breakpoints, chai, style
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `packages/mui-codemod/src/v5.0.0/fade-rename-alpha.test/unmodified.js` (JAVASCRIPT) | **Drift Ratio: 1.77x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.732 IQR)
  * **Local Reality:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 6.606 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/mui-system/src/ThemeProvider/useLayerOrder.test.tsx` (TYPESCRIPT) | Magnitude: 5.13 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, args: 20, func_start: 19, structural_boundaries: 13
- `examples/material-ui-react-router-ts/app/createCache.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, branch: 3, decorators: 3
- `packages-internal/scripts/generate-llms-txt/src/processComponent.ts` (TYPESCRIPT) | Magnitude: 4.62 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 18, branch: 16, io: 16
- `packages/mui-material/src/styles/createStyles.js` (JAVASCRIPT) | Magnitude: 8.36 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 3, state_mutation: 3, branch: 2
- `packages/mui-lab/src/AdapterDateFns/AdapterDateFns.ts` (TYPESCRIPT) | Magnitude: 1.12 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, args: 3, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 13.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, events: 25, doc: 23, structural_boundaries: 22
- `packages/mui-material/src/Slider/SliderValueLabel.types.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.272 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, branch: 6, doc: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/material-ui-nextjs-pages-router-ts/src/Link.tsx` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, generics: 14, ui_framework: 12
- `examples/material-ui-nextjs-ts-v4-v5-migration/src/Link.tsx` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, generics: 14, ui_framework: 12
- `packages/mui-material/src/Tabs/Tabs.js` (JAVASCRIPT) | Magnitude: 175.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 325, branch: 50, structural_boundaries: 48, immutability_locks: 45
- `packages/mui-system/src/styleFunctionSx/styleFunctionSx.spec.tsx` (TYPESCRIPT) | Magnitude: 0.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: ui_framework: 6, generics: 6, structural_boundaries: 5, args: 3
- `scripts/testBuiltTypes.mjs` (JAVASCRIPT) | Magnitude: 17.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, concurrency: 8, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/mui-material/src/Popper/BasePopper.types.ts` (TYPESCRIPT) | Magnitude: 1.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 37, branch: 16, api: 14
- `packages/mui-material/src/OverridableComponent/index.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 18, generics: 16, ui_framework: 14
- `packages-internal/core-docs/src/Ad/AdInHouse.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, generics: 3, api: 2, ui_framework: 2
- `packages/mui-system/src/useThemeProps/getThemeProps.d.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, generics: 6, indent_spaces: 6, ui_framework: 4
- `packages/mui-material/src/styles/createTypography.d.ts` (TYPESCRIPT) | Magnitude: 1.21 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 26, generics: 10, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/mui-codemod/src/deprecations/linear-progress-classes/linear-progress-classes.js` (JAVASCRIPT) | Magnitude: 46.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 12, structural_boundaries: 12, state_mutation: 12
- `packages/mui-codemod/src/deprecations/button-group-classes/button-group-classes.js` (JAVASCRIPT) | Magnitude: 46.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 12, structural_boundaries: 12, state_mutation: 12
- `packages/mui-codemod/src/deprecations/image-list-item-bar-classes/image-list-item-bar-classes.js` (JAVASCRIPT) | Magnitude: 46.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 12, structural_boundaries: 12, state_mutation: 12
- `packages/mui-codemod/src/deprecations/step-connector-classes/step-connector-classes.js` (JAVASCRIPT) | Magnitude: 46.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 12, structural_boundaries: 12, state_mutation: 12
- `packages/mui-codemod/src/deprecations/table-sort-label-classes/table-sort-label-classes.js` (JAVASCRIPT) | Magnitude: 46.6 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, branch: 12, structural_boundaries: 12, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/material-ui-preact/src/index.js` (JAVASCRIPT) | Magnitude: 14.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 3, import: 3, indent_spaces: 3
- `packages/mui-material/src/Stepper/Stepper.spec.tsx` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, ui_framework: 2, generics: 2, args: 1
- `packages/mui-material/src/Chip/Chip.test.js` (JAVASCRIPT) | Magnitude: 427.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 660, func_start: 252, structural_boundaries: 246, test: 203
- `packages/mui-material/src/Slider/SliderValueLabel.tsx` (TYPESCRIPT) | Magnitude: 0.97 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, ui_framework: 7, import: 5
- `packages/mui-material/src/MenuItem/MenuItem.test.js` (JAVASCRIPT) | Magnitude: 80.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 173, func_start: 50, structural_boundaries: 43, test: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages-internal/api-docs-builder/utils/extractInfoFromType.ts` (TYPESCRIPT) | Magnitude: 5.11 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 31, concurrency: 19, structural_boundaries: 18, branch: 10
- `packages-internal/core-docs/src/DocsApp/serviceWorker.ts` (TYPESCRIPT) | Magnitude: 6.29 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, concurrency: 12, branch: 11, args: 10
- `scripts/canaryRelease.mts` (TYPESCRIPT) | Magnitude: 16.51 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, concurrency: 58, structural_boundaries: 54, branch: 35
- `packages/mui-utils/src/useTimeout/useTimeout.ts` (TYPESCRIPT) | Magnitude: 4.14 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 13, concurrency: 12, structural_boundaries: 11
- `packages/mui-icons-material/builder.mjs` (JAVASCRIPT) | Magnitude: 102.78 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, structural_boundaries: 58, concurrency: 43, io: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/mui-codemod/src/v5.0.0/jss-to-styled.test/sixth.actual.js` (JAVASCRIPT) | Magnitude: 23.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 16, import: 11, branch: 8
- `packages/mui-material/src/CardContent/CardContent.test.js` (JAVASCRIPT) | Magnitude: 4.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, import: 3, args: 2
- `packages/mui-material/src/ListItemAvatar/ListItemAvatar.js` (JAVASCRIPT) | Magnitude: 13.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 14, immutability_locks: 11, import: 8
- `packages/mui-material/src/TableContainer/TableContainer.test.js` (JAVASCRIPT) | Magnitude: 4.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, import: 3, args: 2
- `packages-internal/docs-utils/src/createTypeScriptProject.ts` (TYPESCRIPT) | Magnitude: 26.91 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 19, branch: 9, immutability_locks: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/mui-material/src/locale/idID.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 26, dead_code: 18, structural_boundaries: 4, api: 2
- `packages/mui-material/src/locale/hyAM.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 27, dead_code: 18, structural_boundaries: 4, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages-internal/markdown/parseMarkdown.mjs` -> **Brijesh Bittu** (100.0% isolated ownership) | Magnitude: 2636.83
- `packages/mui-material/src/styles/createTheme.test.js` -> **Zeeshan Tamboli** (100.0% isolated ownership) | Magnitude: 477.1
- `packages/mui-codemod/src/deprecations/autocomplete-props/autocomplete-props.js` -> **Zeeshan Tamboli** (100.0% isolated ownership) | Magnitude: 334.64
- `packages/mui-system/src/breakpoints/breakpoints.test.js` -> **Rom Grk** (100.0% isolated ownership) | Magnitude: 321.96
- `packages/mui-material/src/Slide/Slide.test.js` -> **Zeeshan Tamboli** (100.0% isolated ownership) | Magnitude: 316.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/mui-utils/src/generateUtilityClass/generateUtilityClass.ts` -> **Severity: 1840.236** (Blast Radius: 19.417 * Doc Risk: 94.7745%)
- `packages/mui-utils/src/ClassNameGenerator/ClassNameGenerator.ts` -> **Severity: 1342.158** (Blast Radius: 17.293 * Doc Risk: 77.6128%)
- `packages/mui-utils/src/generateUtilityClasses/generateUtilityClasses.ts` -> **Severity: 513.952** (Blast Radius: 10.321 * Doc Risk: 49.7967%)
- `packages/mui-codemod/src/util/readFile.js` -> **Severity: 172.395** (Blast Radius: 3.212 * Doc Risk: 53.6721%)
- `packages/mui-utils/src/chainPropTypes/chainPropTypes.ts` -> **Severity: 140.265** (Blast Radius: 2.058 * Doc Risk: 68.1562%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
