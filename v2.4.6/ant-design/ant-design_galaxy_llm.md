# ARCHITECTURAL_BRIEF: ant-design
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/ant-design` |
| **Timestamp** | `2026-08-03T20:00:50.520975+00:00` |
| **Scan Duration** | `6.63s` |
| **Git Branch** | `master` |
| **Git Commit** | `a8ae51fe861dc0db2fc581938b38d7bbab5ba8f5` |
| **Git Remote** | `https://github.com/ant-design/ant-design.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2087 malicious artifacts.

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
| Total Artifacts | 4763 |
| Analyzed Artifacts (Scanned) | 3266 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1497 |
| Total LOC | 135905 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6609 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3178 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.008 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 86 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2075 | 134336 | 63.5% |
| MARKDOWN | 1163 | 0 | 35.6% |
| JAVASCRIPT | 10 | 673 | 0.3% |
| JSON | 9 | 402 | 0.3% |
| HTML | 3 | 143 | 0.1% |
| PLAINTEXT | 2 | 1 | 0.1% |
| SHELL | 2 | 100 | 0.1% |
| YAML | 1 | 6 | 0.0% |
| CSS | 1 | 244 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.221`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1104 | 33.8% |
| file_cluster_13 | 619 | 19.0% |
| file_cluster_2 | 329 | 10.1% |
| file_cluster_17 | 22 | 0.7% |
| file_cluster_4 | 13 | 0.4% |
| file_cluster_16 | 10 | 0.3% |
| file_cluster_0 | 2 | 0.1% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1164 | 35.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1497*

**Composition by Extension & Reason:**
- `.tsx`: 542x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 10 exceeds 500 chars), 1x Excluded (Saturation: Line 38 exceeds 500 chars)
- `.ts`: 335x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 307x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.snap)
- `.md`: 241x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 137 LOC)
- `.yml`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1836 LOC)
- `.less`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.2 | 5.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.1 | 11.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.3 | 4.4 | 4.0 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.0 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 63.6 | 5.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.9 | 14.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `components/result/serverError.tsx` (Hits: 59)
- `components/result/unauthorized.tsx` (Hits: 52)
- `components/result/noFound.tsx` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **internal.ts** (`components/theme/internal.ts`) — 175 inbound connections
2. **cssinjs.js** (`alias/cssinjs.js`) — 167 inbound connections
3. **genStyleUtils.ts** (`components/theme/util/genStyleUtils.ts`) — 45 inbound connections
4. **useCSSVarCls.ts** (`components/config-provider/hooks/useCSSVarCls.ts`) — 41 inbound connections
5. **SizeContext.tsx** (`components/config-provider/SizeContext.tsx`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`components/index.ts`) — 83 outbound dependencies
2. **context.ts** (`components/config-provider/context.ts`) — 70 outbound dependencies
3. **components.ts** (`components/theme/interface/components.ts`) — 67 outbound dependencies
4. **InternalTable.tsx** (`components/table/InternalTable.tsx`) — 36 outbound dependencies
5. **index.tsx** (`components/tree-select/index.tsx`) — 32 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `useSelection` (@ `components/table/hooks/useSelection.tsx`) -> Impact: **988.8** | LOC: 680
- `InternalTable` (@ `components/table/InternalTable.tsx`) -> Impact: **538.4** | LOC: 567
- `FilterDropdown` (@ `components/table/hooks/useFilter/FilterDropdown.tsx`) -> Impact: **507.1** | LOC: 442
- `InternalFormItem` (@ `components/form/FormItem/index.tsx`) -> Impact: **488.1** | LOC: 331
- `Steps` (@ `components/steps/index.tsx`) -> Impact: **485.4** | LOC: 308
- `triggerSorter` (@ `components/table/hooks/useSorter.tsx`) -> Impact: **464.4** | LOC: 167
- `Anchor` (@ `components/anchor/Anchor.tsx`) -> Impact: **375.0** | LOC: 294
- `Splitter` (@ `components/splitter/Splitter.tsx`) -> Impact: **335.3** | LOC: 262
- `Transfer` (@ `components/transfer/index.tsx`) -> Impact: **333.8** | LOC: 441
- `updateSizes` (@ `components/splitter/hooks/useResize.ts`) -> Impact: **311.8** | LOC: 156

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Splitter` (@ `components/splitter/Splitter.tsx`) -> **O(2^N) [Recursive]**
- `triggerSorter` (@ `components/table/hooks/useSorter.tsx`) -> **O(2^N) [Recursive]**
- `AutoComplete` (@ `components/auto-complete/AutoComplete.tsx`) -> **O(2^N) [Recursive]**
- `Breadcrumb` (@ `components/breadcrumb/Breadcrumb.tsx`) -> **O(2^N) [Recursive]**
- `setMode` (@ `components/menu/demo/_semantic.tsx`) -> **O(2^N) [Recursive]**
- `flushMessageQueue` (@ `components/message/index.tsx`) -> **O(2^N) [Recursive]**
- `flushNotificationQueue` (@ `components/notification/index.tsx`) -> **O(2^N) [Recursive]**
- `Steps` (@ `components/steps/index.tsx`) -> **O(2^N) [Recursive]**
- `getFilterData` (@ `components/table/hooks/useFilter/index.tsx`) -> **O(2^N) [Recursive]**
- `onItemSelect` (@ `components/transfer/demo/tree-transfer.tsx`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `boot` (@ `scripts/visual-regression/build.ts`) -> DB Complexity: **73**
- `run` (@ `scripts/visual-regression/local.ts`) -> DB Complexity: **46**
- `useSelection` (@ `components/table/hooks/useSelection.tsx`) -> DB Complexity: **25**
- `describe` (@ `scripts/check-site.ts`) -> DB Complexity: **24**
- `runPrePublish` (@ `scripts/pre-publish.ts`) -> DB Complexity: **24**
- `convertReport` (@ `scripts/visual-regression/reportAdapter.ts`) -> DB Complexity: **21**
  * *Intent:* /**
- `FC` (@ `components/empty/empty.tsx`) -> DB Complexity: **18**
- `FC` (@ `components/upload/demo/picture-card.tsx`) -> DB Complexity: **18**
- `downloadVisualSnapshots` (@ `scripts/visual-regression/local.ts`) -> DB Complexity: **18**
- `process` (@ `scripts/post-publish.ts`) -> DB Complexity: **16**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 24 | 5294.38 | 7.16% | 2.83% |
| `components/table/hooks` | 6 | 214.89 | 22.71% | 1.36% |
| `scripts/visual-regression` | 6 | 172.7 | 27.78% | 18.6% |
| `components/table/demo` | 101 | 153.79 | 2.94% | 15.12% |
| `components/message` | 7 | 141.61 | 15.28% | 12.88% |
| `components/locale` | 75 | 139.38 | 4.39% | 0.88% |
| `scripts` | 18 | 132.6 | 37.78% | 30.46% |
| `components/date-picker/locale` | 69 | 111.65 | 4.54% | 0.0% |
| `.dumi/scripts` | 2 | 107.38 | 10.0% | 6.69% |
| `components/form/demo` | 79 | 104.26 | 3.1% | 1.58% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `components/_util/motion.ts` -> **100.0%** Exposure
- `components/upload/__tests__/requests.ts` -> **100.0%** Exposure
- `scripts/ci-mock-project-build.sh` -> **100.0%** Exposure
- `scripts/test-all.sh` -> **100.0%** Exposure
- `components/upload/demo/defaultFileList.tsx` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.dumi/theme/utils/index.ts` -> **100.0%** Exposure
- `components/_util/ActionButton.tsx` -> **100.0%** Exposure
- `components/_util/getAllowClear.tsx` -> **100.0%** Exposure
- `components/_util/getScroll.ts` -> **100.0%** Exposure
- `components/_util/hooks/useMultipleSelect.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/test-all.sh` -> **1** Orphaned Functions | **10** Duplicates
- `components/message/index.tsx` -> **0** Orphaned Functions | **5** Duplicates
- `components/table/demo/ellipsis-custom-tooltip.tsx` -> **0** Orphaned Functions | **5** Duplicates
- `components/_util/warning.ts` -> **0** Orphaned Functions | **4** Duplicates
- `components/color-picker/demo/format.tsx` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`.dumi/hooks/useMenu.tsx`** -> AI Confidence: **99.31%**
2. **`components/affix/index.tsx`** -> AI Confidence: **99.31%**
3. **`components/alert/Alert.tsx`** -> AI Confidence: **99.31%**
4. **`components/anchor/Anchor.tsx`** -> AI Confidence: **99.31%**
5. **`components/auto-complete/AutoComplete.tsx`** -> AI Confidence: **99.31%**
6. **`components/avatar/Avatar.tsx`** -> AI Confidence: **99.31%**
7. **`components/avatar/AvatarGroup.tsx`** -> AI Confidence: **99.31%**
8. **`components/badge/Badge.tsx`** -> AI Confidence: **99.31%**
9. **`components/breadcrumb/BreadcrumbItem.tsx`** -> AI Confidence: **99.31%**
10. **`components/button/Button.tsx`** -> AI Confidence: **99.31%**
11. **`components/card/Card.tsx`** -> AI Confidence: **99.31%**
12. **`components/carousel/index.tsx`** -> AI Confidence: **99.31%**
13. **`components/checkbox/Checkbox.tsx`** -> AI Confidence: **99.31%**
14. **`components/collapse/Collapse.tsx`** -> AI Confidence: **99.31%**
15. **`components/color-picker/ColorPicker.tsx`** -> AI Confidence: **99.31%**
16. **`components/config-provider/hooks/useTheme.ts`** -> AI Confidence: **99.31%**
17. **`components/config-provider/index.tsx`** -> AI Confidence: **99.31%**
18. **`components/divider/index.tsx`** -> AI Confidence: **99.31%**
19. **`components/drawer/DrawerPanel.tsx`** -> AI Confidence: **99.31%**
20. **`components/dropdown/dropdown.tsx`** -> AI Confidence: **99.31%**
21. **`components/empty/index.tsx`** -> AI Confidence: **99.31%**
22. **`components/float-button/FloatButtonGroup.tsx`** -> AI Confidence: **99.31%**
23. **`components/form/FormItem/StatusProvider.tsx`** -> AI Confidence: **99.31%**
24. **`components/form/FormItem/index.tsx`** -> AI Confidence: **99.31%**
25. **`components/form/FormItemInput.tsx`** -> AI Confidence: **99.31%**
26. **`components/form/FormItemLabel.tsx`** -> AI Confidence: **99.31%**
27. **`components/grid/col.tsx`** -> AI Confidence: **99.31%**
28. **`components/input/OTP/index.tsx`** -> AI Confidence: **99.31%**
29. **`components/input/Search.tsx`** -> AI Confidence: **99.31%**
30. **`components/list/Item.tsx`** -> AI Confidence: **99.31%**
31. **`components/list/index.tsx`** -> AI Confidence: **99.31%**
32. **`components/menu/MenuItem.tsx`** -> AI Confidence: **99.31%**
33. **`components/menu/SubMenu.tsx`** -> AI Confidence: **99.31%**
34. **`components/menu/menu.tsx`** -> AI Confidence: **99.31%**
35. **`components/modal/ConfirmDialog.tsx`** -> AI Confidence: **99.31%**
36. **`components/modal/interface.ts`** -> AI Confidence: **99.31%**
37. **`components/progress/Line.tsx`** -> AI Confidence: **99.31%**
38. **`components/progress/progress.tsx`** -> AI Confidence: **99.31%**
39. **`components/qr-code/index.tsx`** -> AI Confidence: **99.31%**
40. **`components/select/index.tsx`** -> AI Confidence: **99.31%**
41. **`components/select/useIcons.tsx`** -> AI Confidence: **99.31%**
42. **`components/skeleton/Skeleton.tsx`** -> AI Confidence: **99.31%**
43. **`components/slider/index.tsx`** -> AI Confidence: **99.31%**
44. **`components/spin/index.tsx`** -> AI Confidence: **99.31%**
45. **`components/statistic/Statistic.tsx`** -> AI Confidence: **99.31%**
46. **`components/steps/index.tsx`** -> AI Confidence: **99.31%**
47. **`components/switch/index.tsx`** -> AI Confidence: **99.31%**
48. **`components/table/InternalTable.tsx`** -> AI Confidence: **99.31%**
49. **`components/table/hooks/useFilter/FilterDropdown.tsx`** -> AI Confidence: **99.31%**
50. **`components/table/hooks/useSelection.tsx`** -> AI Confidence: **99.31%**
51. **`components/table/hooks/useSorter.tsx`** -> AI Confidence: **99.31%**
52. **`components/tabs/index.tsx`** -> AI Confidence: **99.31%**
53. **`components/tag/index.tsx`** -> AI Confidence: **99.31%**
54. **`components/tooltip/index.tsx`** -> AI Confidence: **99.31%**
55. **`components/tour/panelRender.tsx`** -> AI Confidence: **99.31%**
56. **`components/transfer/index.tsx`** -> AI Confidence: **99.31%**
57. **`components/tree-select/index.tsx`** -> AI Confidence: **99.31%**
58. **`components/tree/Tree.tsx`** -> AI Confidence: **99.31%**
59. **`components/tree/utils/iconUtil.tsx`** -> AI Confidence: **99.31%**
60. **`components/typography/Base/index.tsx`** -> AI Confidence: **99.31%**
61. **`components/upload/UploadList/ListItem.tsx`** -> AI Confidence: **99.31%**
62. **`components/watermark/index.tsx`** -> AI Confidence: **99.31%**
63. **`scripts/post-publish.ts`** -> AI Confidence: **99.31%**
64. **`components/_util/placements.ts`** -> AI Confidence: **99.29%**
65. **`components/theme/themes/shared/genRadius.ts`** -> AI Confidence: **99.29%**
66. **`.dumi/scripts/clarity.js`** -> AI Confidence: **99.29%**
67. **`alias/cssinjs.js`** -> AI Confidence: **99.29%**
68. **`scripts/test-all.sh`** -> AI Confidence: **99.29%**
69. **`components/_util/wave/WaveEffect.tsx`** -> AI Confidence: **99.24%**
70. **`components/back-top/index.tsx`** -> AI Confidence: **99.24%**
71. **`components/badge/Ribbon.tsx`** -> AI Confidence: **99.24%**
72. **`components/breadcrumb/Breadcrumb.tsx`** -> AI Confidence: **99.24%**
73. **`components/calendar/generateCalendar.tsx`** -> AI Confidence: **99.24%**
74. **`components/cascader/index.tsx`** -> AI Confidence: **99.24%**
75. **`components/color-picker/components/PanelPicker/index.tsx`** -> AI Confidence: **99.24%**
76. **`components/descriptions/index.tsx`** -> AI Confidence: **99.24%**
77. **`components/drawer/Drawer.tsx`** -> AI Confidence: **99.24%**
78. **`components/dropdown/dropdown-button.tsx`** -> AI Confidence: **99.24%**
79. **`components/float-button/BackTop.tsx`** -> AI Confidence: **99.24%**
80. **`components/form/FormItem/ItemHolder.tsx`** -> AI Confidence: **99.24%**
81. **`components/grid/row.tsx`** -> AI Confidence: **99.24%**
82. **`components/image/index.tsx`** -> AI Confidence: **99.24%**
83. **`components/input-number/index.tsx`** -> AI Confidence: **99.24%**
84. **`components/input/Input.tsx`** -> AI Confidence: **99.24%**
85. **`components/input/Password.tsx`** -> AI Confidence: **99.24%**
86. **`components/input/TextArea.tsx`** -> AI Confidence: **99.24%**
87. **`components/locale/index.tsx`** -> AI Confidence: **99.24%**
88. **`components/message/useMessage.tsx`** -> AI Confidence: **99.24%**
89. **`components/notification/useNotification.tsx`** -> AI Confidence: **99.24%**
90. **`components/popconfirm/PurePanel.tsx`** -> AI Confidence: **99.24%**
91. **`components/popover/index.tsx`** -> AI Confidence: **99.24%**
92. **`components/result/index.tsx`** -> AI Confidence: **99.24%**
93. **`components/space/Compact.tsx`** -> AI Confidence: **99.24%**
94. **`components/space/index.tsx`** -> AI Confidence: **99.24%**
95. **`components/splitter/SplitBar.tsx`** -> AI Confidence: **99.24%**
96. **`components/splitter/Splitter.tsx`** -> AI Confidence: **99.24%**
97. **`components/timeline/Timeline.tsx`** -> AI Confidence: **99.24%**
98. **`components/transfer/Section.tsx`** -> AI Confidence: **99.24%**
99. **`components/tree/DirectoryTree.tsx`** -> AI Confidence: **99.24%**
100. **`components/upload/Upload.tsx`** -> AI Confidence: **99.24%**
101. **`scripts/pre-publish.ts`** -> AI Confidence: **99.24%**
102. **`scripts/print-changelog.ts`** -> AI Confidence: **99.24%**
103. **`scripts/visual-regression/local.ts`** -> AI Confidence: **99.24%**
104. **`components/_util/hooks/useClosable.tsx`** -> AI Confidence: **99.23%**
105. **`components/_util/wave/index.ts`** -> AI Confidence: **99.23%**
106. **`components/calendar/Header.tsx`** -> AI Confidence: **99.23%**
107. **`components/color-picker/components/ColorTrigger.tsx`** -> AI Confidence: **99.23%**
108. **`components/color-picker/interface.ts`** -> AI Confidence: **99.23%**
109. **`components/date-picker/generatePicker/interface.ts`** -> AI Confidence: **99.23%**
110. **`components/input/Group.tsx`** -> AI Confidence: **99.23%**
111. **`components/progress/Circle.tsx`** -> AI Confidence: **99.23%**
112. **`components/select/style/select-input.ts`** -> AI Confidence: **99.23%**
113. **`components/theme/context.ts`** -> AI Confidence: **99.23%**
114. **`components/theme/useToken.ts`** -> AI Confidence: **99.23%**
115. **`components/transfer/ListItem.tsx`** -> AI Confidence: **99.23%**
116. **`components/typography/Editable.tsx`** -> AI Confidence: **99.23%**
117. **`components/color-picker/components/ColorPresets.tsx`** -> AI Confidence: **99.18%**
118. **`components/image/PreviewGroup.tsx`** -> AI Confidence: **99.18%**
119. **`components/index.ts`** -> AI Confidence: **99.18%**
120. **`components/radio/group.tsx`** -> AI Confidence: **99.18%**
121. **`components/steps/style/index.ts`** -> AI Confidence: **99.18%**
122. **`components/tour/index.tsx`** -> AI Confidence: **99.18%**
123. **`components/transfer/ListBody.tsx`** -> AI Confidence: **99.18%**
124. **`scripts/check-site.ts`** -> AI Confidence: **99.18%**
125. **`components/_util/wave/util.ts`** -> AI Confidence: **99.17%**
126. **`components/typography/demo/ellipsis.tsx`** -> AI Confidence: **99.17%**
127. **`index-style-only.js`** -> AI Confidence: **99.17%**
128. **`index-with-locales.js`** -> AI Confidence: **99.17%**
129. **`components/_util/wave/useWave.ts`** -> AI Confidence: **99.16%**
130. **`components/color-picker/components/ColorSlider.tsx`** -> AI Confidence: **99.16%**
131. **`components/config-provider/context.ts`** -> AI Confidence: **99.16%**
132. **`components/date-picker/generatePicker/generateRangePicker.tsx`** -> AI Confidence: **99.16%**
133. **`components/date-picker/generatePicker/generateSinglePicker.tsx`** -> AI Confidence: **99.16%**
134. **`components/float-button/FloatButton.tsx`** -> AI Confidence: **99.16%**
135. **`components/form/Form.tsx`** -> AI Confidence: **99.16%**
136. **`components/form/context.tsx`** -> AI Confidence: **99.16%**
137. **`components/masonry/Masonry.tsx`** -> AI Confidence: **99.16%**
138. **`components/mentions/index.tsx`** -> AI Confidence: **99.16%**
139. **`components/message/PurePanel.tsx`** -> AI Confidence: **99.16%**
140. **`components/modal/Modal.tsx`** -> AI Confidence: **99.16%**
141. **`components/modal/PurePanel.tsx`** -> AI Confidence: **99.16%**
142. **`components/notification/PurePanel.tsx`** -> AI Confidence: **99.16%**
143. **`components/notification/index.tsx`** -> AI Confidence: **99.16%**
144. **`components/pagination/Pagination.tsx`** -> AI Confidence: **99.16%**
145. **`components/popconfirm/index.tsx`** -> AI Confidence: **99.16%**
146. **`components/radio/radio.tsx`** -> AI Confidence: **99.16%**
147. **`components/rate/index.tsx`** -> AI Confidence: **99.16%**
148. **`components/table/interface.ts`** -> AI Confidence: **99.16%**
149. **`components/theme/interface/components.ts`** -> AI Confidence: **99.16%**
150. **`components/time-picker/index.tsx`** -> AI Confidence: **99.16%**
151. **`components/upload/UploadList/index.tsx`** -> AI Confidence: **99.16%**
152. **`scripts/visual-regression/build.ts`** -> AI Confidence: **99.16%**
153. **`components/app/App.tsx`** -> AI Confidence: **99.15%**
154. **`components/button/style/token.ts`** -> AI Confidence: **99.15%**
155. **`components/checkbox/Group.tsx`** -> AI Confidence: **99.15%**
156. **`components/color-picker/components/ColorInput.tsx`** -> AI Confidence: **99.15%**
157. **`components/flex/index.tsx`** -> AI Confidence: **99.15%**
158. **`components/form/ErrorList.tsx`** -> AI Confidence: **99.15%**
159. **`components/message/index.tsx`** -> AI Confidence: **99.15%**
160. **`components/modal/confirm.tsx`** -> AI Confidence: **99.15%**
161. **`components/modal/shared.tsx`** -> AI Confidence: **99.15%**
162. **`components/modal/useModal/HookModal.tsx`** -> AI Confidence: **99.15%**
163. **`components/popover/PurePanel.tsx`** -> AI Confidence: **99.15%**
164. **`components/segmented/index.tsx`** -> AI Confidence: **99.15%**
165. **`components/skeleton/Button.tsx`** -> AI Confidence: **99.15%**
166. **`components/skeleton/Input.tsx`** -> AI Confidence: **99.15%**
167. **`components/tag/CheckableTagGroup.tsx`** -> AI Confidence: **99.15%**
168. **`components/typography/Base/CopyBtn.tsx`** -> AI Confidence: **99.15%**
169. **`scripts/build-style.tsx`** -> AI Confidence: **99.15%**
170. **`components/anchor/AnchorLink.tsx`** -> AI Confidence: **99.13%**
171. **`components/badge/ScrollNumber.tsx`** -> AI Confidence: **99.13%**
172. **`components/collapse/CollapsePanel.tsx`** -> AI Confidence: **99.13%**
173. **`components/descriptions/Cell.tsx`** -> AI Confidence: **99.13%**
174. **`components/image/hooks/useMergedPreviewConfig.ts`** -> AI Confidence: **99.13%**
175. **`components/image/hooks/usePreviewConfig.ts`** -> AI Confidence: **99.13%**
176. **`components/input/OTP/OTPInput.tsx`** -> AI Confidence: **99.13%**
177. **`components/tag/CheckableTag.tsx`** -> AI Confidence: **99.13%**
178. **`components/timeline/useItems.tsx`** -> AI Confidence: **99.13%**
179. **`components/transfer/Actions.tsx`** -> AI Confidence: **99.13%**
180. **`scripts/check-version-md.ts`** -> AI Confidence: **99.13%**
181. **`scripts/prepare-examples.ts`** -> AI Confidence: **99.13%**
182. **`webpack.config.js`** -> AI Confidence: **99.13%**
183. **`.dumi/hooks/useLocation.ts`** -> AI Confidence: **99.09%**
184. **`components/_util/hooks/index.ts`** -> AI Confidence: **99.09%**
185. **`components/_util/scrollTo.ts`** -> AI Confidence: **99.09%**
186. **`components/alert/ErrorBoundary.tsx`** -> AI Confidence: **99.09%**
187. **`components/button/demo/color-variant.tsx`** -> AI Confidence: **99.09%**
188. **`components/descriptions/Item.ts`** -> AI Confidence: **99.09%**
189. **`components/form/demo/register.tsx`** -> AI Confidence: **99.09%**
190. **`components/form/hooks/useVariants.ts`** -> AI Confidence: **99.09%**
191. **`components/form/util.ts`** -> AI Confidence: **99.09%**
192. **`components/menu/style/index.ts`** -> AI Confidence: **99.09%**
193. **`components/progress/utils.ts`** -> AI Confidence: **99.09%**
194. **`components/splitter/hooks/useResizable.ts`** -> AI Confidence: **99.09%**
195. **`components/table/hooks/useLazyKVMap.ts`** -> AI Confidence: **99.09%**
196. **`components/table/style/index.ts`** -> AI Confidence: **99.09%**
197. **`components/tooltip/hook/useMergedArrow.ts`** -> AI Confidence: **99.09%**
198. **`components/tour/interface.ts`** -> AI Confidence: **99.09%**
199. **`components/transfer/search.tsx`** -> AI Confidence: **99.09%**
200. **`components/tree/demo/drag-debug.tsx`** -> AI Confidence: **99.09%**
201. **`scripts/generate-component-changelog.ts`** -> AI Confidence: **99.09%**
202. **`components/button/style/index.ts`** -> AI Confidence: **99.08%**
203. **`components/cascader/Panel.tsx`** -> AI Confidence: **99.08%**
204. **`components/color-picker/style/index.ts`** -> AI Confidence: **99.08%**
205. **`components/dropdown/style/index.ts`** -> AI Confidence: **99.08%**
206. **`components/form/index.tsx`** -> AI Confidence: **99.08%**
207. **`components/form/style/index.ts`** -> AI Confidence: **99.08%**
208. **`components/input-number/style/index.ts`** -> AI Confidence: **99.08%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `components/form/FormItem/index.tsx` -> **100.0%** Exposure
- `components/form/demo/advanced-search.tsx` -> **100.0%** Exposure
- `components/message/index.tsx` -> **100.0%** Exposure
- `components/modal/style/index.ts` -> **100.0%** Exposure
- `components/space/demo/compact-debug.tsx` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `components/upload/demo/crop-image.tsx` -> **100.0%** Exposure
- `scripts/check-version-md.ts` -> **100.0%** Exposure
- `scripts/pre-publish.ts` -> **100.0%** Exposure
- `scripts/visual-regression/upload.js` -> **100.0%** Exposure
- `scripts/visual-regression/build.ts` -> **36.5486%** Exposure
### Algorithmic DoS Exposure
- `components/_util/responsiveObserver.ts` -> **100.0%** Exposure
- `components/anchor/Anchor.tsx` -> **100.0%** Exposure
- `components/breadcrumb/Breadcrumb.tsx` -> **100.0%** Exposure
- `components/button/demo/debug-icon.tsx` -> **100.0%** Exposure
- `components/calendar/Header.tsx` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4226` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `components/spin/usePercent.ts` (TYPESCRIPT) -> Cumulative Risk: **683.92**
- **Archetype:** `file_cluster_4` (Distance: 11.332 IQR)
- **Magnitude:** 5.28 | **LOC:** 50 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Logic Bomb (98.8861%)
- **Heaviest Functions:** `usePercent` (Impact: 34.0)

### 2. `components/_util/ActionButton.tsx` (TYPESCRIPT) -> Cumulative Risk: **665.85**
- **Archetype:** `file_cluster_13` (Distance: 11.948 IQR)
- **Magnitude:** 10.35 | **LOC:** 137 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (97.3924%)
- **Heaviest Functions:** `ActionButton` (Impact: 52.1), `isThenable` (Impact: 8.1)

### 3. `components/upload/demo/crop-image.tsx` (TYPESCRIPT) -> Cumulative Risk: **660.7**
- **Archetype:** `file_cluster_4` (Distance: 10.169 IQR)
- **Magnitude:** 3.54 | **LOC:** 53 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `FC` (Impact: 12.5)

### 4. `scripts/pre-publish.ts` (TYPESCRIPT) -> Cumulative Risk: **650.43**
- **Archetype:** `file_cluster_4` (Distance: 10.737 IQR)
- **Magnitude:** 16.85 | **LOC:** 285 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `runPrePublish` (Impact: 53.2), `showMessage` (Impact: 45.6), `downloadArtifact` (Impact: 11.3)

### 5. `components/splitter/hooks/useResizable.ts` (TYPESCRIPT) -> Cumulative Risk: **622.31**
- **Archetype:** `file_cluster_8` (Distance: 10.006 IQR)
- **Magnitude:** 10.29 | **LOC:** 107 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9999%), Documentation (97.9478%)
- **Heaviest Functions:** `useResizable` (Impact: 60.6), `getShowCollapsibleIcon` (Impact: 16.5)

### 6. `components/message/index.tsx` (TYPESCRIPT) -> Cumulative Risk: **614.66**
- **Archetype:** `file_cluster_13` (Distance: 11.395 IQR)
- **Magnitude:** 27.26 | **LOC:** 346 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (90.1764%)
- **Heaviest Functions:** `flushMessageQueue` (Impact: 142.6), `open` (Impact: 19.4), `typeOpen` (Impact: 14.8)

### 7. `components/_util/responsiveObserver.ts` (TYPESCRIPT) -> Cumulative Risk: **612.19**
- **Archetype:** `file_cluster_17` (Distance: 11.791 IQR)
- **Magnitude:** 10.49 | **LOC:** 155 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (98.1618%), State Flux (94.9559%)
- **Heaviest Functions:** `useResponsiveObserver` (Impact: 34.1), `validateBreakpoints` (Impact: 16.8), `matchScreen` (Impact: 12.6)

### 8. `scripts/check-version-md.ts` (TYPESCRIPT) -> Cumulative Risk: **606.31**
- **Archetype:** `file_cluster_13` (Distance: 10.829 IQR)
- **Magnitude:** 3.1 | **LOC:** 65 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), State Flux (99.022%), Logic Bomb (98.1564%)
- **Heaviest Functions:** `getChangelogByVersion` (Impact: 14.9)

### 9. `components/table/hooks/useSorter.tsx` (TYPESCRIPT) -> Cumulative Risk: **596.42**
- **Archetype:** `file_cluster_2` (Distance: 11.077 IQR)
- **Magnitude:** 81.74 | **LOC:** 524 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (92.8345%)
- **Heaviest Functions:** `triggerSorter` (Impact: 464.4), `useFilterSorter` (Impact: 104.5), `getSortData` (Impact: 83.1)

### 10. `components/color-picker/color.ts` (TYPESCRIPT) -> Cumulative Risk: **593.14**
- **Archetype:** `file_cluster_17` (Distance: 12.55 IQR)
- **Magnitude:** 18.5 | **LOC:** 115 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (98.1127%)
- **Heaviest Functions:** `equals` (Impact: 41.1), `constructor` (Impact: 35.0), `getHex` (Impact: 7.2)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/visual-regression/upload.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.595 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.933 IQR)
- **Top Global Matches:** file_cluster_4: 11.595, file_cluster_13: 11.834, file_cluster_8: 11.959
- **Magnitude:** 113.08 | **LOC:** 170 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (33.2127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `boot` (Impact: 29.7 | O(N^2) | DB: 12)
  * `walkDir` (Impact: 17.0 | O(2^N) | DB: 11)
  * `retry` (Impact: 16.9 | O(N^3))
  * `uploadFile` (Impact: 9.3 | O(N^1) | DB: 6)
  * `parseArgs` (Impact: 7.7 | O(N^1) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 9`, `func_start: 13`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 13`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`, `test: 4`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, node:fs, ali-oss, node:path
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/table/hooks/useSelection.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.857 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.523 IQR)
- **Top Global Matches:** file_cluster_17: 11.857, file_cluster_13: 12.096, file_cluster_2: 12.221
- **Magnitude:** 110.72 | **LOC:** 757 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (21.1955%), Tech Debt (8.1474%)
**Top Internal Functions/Classes:**
  * `useSelection` (Impact: 988.8 | O(N^6) | DB: 25)
  * `flattenData` (Impact: 27.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 128`, `args: 84`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 72`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 34`, `immutability_locks: 94`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` type, clsx, interface, DownOutlined, treeUtil, util, hooks, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/message/interface.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.238 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.319 IQR)
- **Top Global Matches:** file_cluster_8: 10.238, file_cluster_16: 10.302, file_cluster_13: 10.346
- **Magnitude:** 86.34 | **LOC:** 110 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 36`, `args: 6`, `func_start: 2`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 4`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` react, hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.dumi/scripts/mirror-notify.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.772 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.572 IQR)
- **Top Global Matches:** file_cluster_8: 8.772, file_cluster_7: 9.517, file_cluster_4: 9.616
- **Magnitude:** 83.14 | **LOC:** 274 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (15.0054%), Tech Debt (13.3879%)
**Top Internal Functions/Classes:**
  * `createMirrorModal` (Impact: 60.4 | O(N^2) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 21`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `concurrency: 10`
* *Defense:* `safety: 5`, `immutability_locks: 18`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useSorter.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.077 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.254 IQR)
- **Top Global Matches:** file_cluster_2: 11.077, file_cluster_17: 11.148, file_cluster_13: 11.289
- **Magnitude:** 81.74 | **LOC:** 524 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (19.2121%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `triggerSorter` (Impact: 464.4 | O(2^N) | DB: 5)
  * `useFilterSorter` (Impact: 104.5 | O(N^3) | DB: 7)
  * `getSortData` (Impact: 83.1 | O(2^N) | DB: 3)
  * `collectSortStates` (Impact: 76.2 | O(2^N) | DB: 3)
  * `generateSorterInfo` (Impact: 10.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 96`, `args: 47`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 46`
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `safety: 11`, `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.299
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` KeyCode, type, clsx, interface, locale, util, react, CaretUpOutlined...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/table/InternalTable.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.069 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.339 IQR)
- **Top Global Matches:** file_cluster_13: 11.069, file_cluster_2: 11.203, file_cluster_8: 11.312
- **Magnitude:** 61.74 | **LOC:** 772 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 44.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (13.0088%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `InternalTable` (Impact: 538.4 | O(N^4) | DB: 5)
  * `resetPagination` (Impact: 40.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 144`, `args: 46`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 13`
* *Architecture:* `api: 12`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 31`, `doc: 2`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.977
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` clsx, useSorter, defaultRenderEmpty, useColumns, useFilter, useLazyKVMap, useBreakpoint, ExpandIcon...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `components/form/FormItem/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.531 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.461 IQR)
- **Top Global Matches:** file_cluster_13: 10.531, file_cluster_2: 10.809, file_cluster_17: 10.821
- **Magnitude:** 56.94 | **LOC:** 459 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (19.92%), Tech Debt (24.2081%)
**Top Internal Functions/Classes:**
  * `InternalFormItem` (Impact: 488.1 | O(N^4) | DB: 14)
  * `isSimilarControl` (Impact: 32.4 | O(N^1))
  * `isSimilarControl` (Impact: 11.3 | O(N^2))
    * *Intent:* // https://github.com/ant-design/ant-design/issues/46417 // `getValueProps` may modify the value pro...
  * `genEmptyMeta` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 79`, `args: 34`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 24`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 4`, `import: 26`
* *Defense:* `safety: 9`, `immutability_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` clsx, form, warning, reactNode, Field, ItemHolder, react, isNonNullable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useFilter/FilterDropdown.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.522 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.384 IQR)
- **Top Global Matches:** file_cluster_8: 10.522, file_cluster_13: 10.526, file_cluster_2: 10.675
- **Magnitude:** 56.7 | **LOC:** 592 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.2294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FilterDropdown` (Impact: 507.1 | O(N^6) | DB: 2)
  * `flattenKeys` (Impact: 16.5 | O(2^N) | DB: 2)
  * `searchValueMatched` (Impact: 7.2 | O(N^1))
  * `wrapStringListType` (Impact: 6.2 | O(N^1))
  * `hasSubMenu` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 106`, `args: 68`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `api: 4`, `import: 27`
* *Defense:* `safety: 18`, `immutability_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` clsx, FilterWrapper, , isEqual, dropdown, context, OverrideContext, react...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/steps/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.155 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.436 IQR)
- **Top Global Matches:** file_cluster_13: 10.155, file_cluster_2: 10.37, file_cluster_8: 10.402
- **Magnitude:** 52.34 | **LOC:** 458 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (13.9791%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Steps` (Impact: 485.4 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 87`, `args: 17`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 10`, `import: 22`
* *Defense:* `safety: 1`, `doc: 12`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` interface, clsx, wave, ProgressIcon, tooltip, useBreakpoint, context, steps...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `webpack.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.831 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.562 IQR)
- **Top Global Matches:** file_cluster_13: 10.831, file_cluster_0: 10.943, file_cluster_17: 11.108
- **Magnitude:** 45.02 | **LOC:** 94 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (29.3895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addPluginsForProduction` (Impact: 14.7 | O(N^2) | DB: 3)
  * `externalCssinjs` (Impact: 5.5 | O(N^1) | DB: 3)
  * `addLocales` (Impact: 4.0 | O(N^1) | DB: 1)
  * `externalDayjs` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`
* *Architecture:* `io: 3`, `api: 1`, `import: 6`
* *Defense:* `safety: 4`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` duplicate-package-checker-webpack-plugin, webpack-bundle-analyzer, node:path, webpack-plugin, circular-dependency-plugin, tools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/anchor/Anchor.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.002 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.753 IQR)
- **Top Global Matches:** file_cluster_13: 11.002, file_cluster_17: 11.196, file_cluster_2: 11.213
- **Magnitude:** 43.55 | **LOC:** 433 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 43.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (15.025%), Tech Debt (15.7052%)
**Top Internal Functions/Classes:**
  * `Anchor` (Impact: 375.0 | O(2^N) | DB: 12)
  * `getOffsetTop` (Impact: 9.5 | O(N^1))
  * `getContainer` (Impact: 7.8 | O(N^1))
  * `getDefaultContainer` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 95`, `args: 43`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 13`, `import: 17`
* *Defense:* `safety: 21`, `doc: 5`, `immutability_locks: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` clsx, hooks, AnchorLink, scroll-into-view-if-needed, context, util, react, affix...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/transfer/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.65 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.069 IQR)
- **Top Global Matches:** file_cluster_13: 10.65, file_cluster_8: 10.793, file_cluster_2: 10.799
- **Magnitude:** 37.32 | **LOC:** 617 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 63.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.9796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Transfer` (Impact: 333.8 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 125`, `args: 71`, `func_start: 47`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `api: 20`, `import: 27`
* *Defense:* `safety: 22`, `doc: 6`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` clsx, defaultRenderEmpty, statusUtils, Section, useData, context, react, interface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useFilter/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.237 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.263 IQR)
- **Top Global Matches:** file_cluster_17: 10.237, file_cluster_2: 10.359, file_cluster_8: 10.469
- **Magnitude:** 36.69 | **LOC:** 333 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.0853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `collectFilterStates` (Impact: 136.4 | O(2^N) | DB: 4)
  * `getFilterData` (Impact: 69.0 | O(2^N))
  * `triggerFilter` (Impact: 59.2 | O(2^N) | DB: 1)
  * `useFilter` (Impact: 42.0 | O(N^3) | DB: 3)
  * `generateFilterInfo` (Impact: 16.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 68`, `args: 36`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 4`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` type, util, react, FilterDropdown, warning, interface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/splitter/Splitter.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.551 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.832 IQR)
- **Top Global Matches:** file_cluster_13: 10.551, file_cluster_8: 10.721, file_cluster_17: 10.808
- **Magnitude:** 36.61 | **LOC:** 294 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (16.495%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Splitter` (Impact: 335.3 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 40`, `args: 19`, `func_start: 8`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 8`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` clsx, hooks, useResize, useItems, util, react, SplitBar, style...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/breadcrumb/Breadcrumb.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.823 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.264 IQR)
- **Top Global Matches:** file_cluster_13: 9.823, file_cluster_16: 10.194, file_cluster_8: 10.25
- **Magnitude:** 34.5 | **LOC:** 310 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (11.6859%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Breadcrumb` (Impact: 309.6 | O(2^N) | DB: 9)
  * `getPath` (Impact: 7.4 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 76`, `args: 12`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`
* *Architecture:* `io: 7`, `api: 11`, `import: 20`
* *Defense:* `safety: 5`, `doc: 8`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.009
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` clsx, hooks, DownOutlined, dropdown, BreadcrumbSeparator, util, useItems, pickAttrs...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `components/splitter/hooks/useResize.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.794 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.802 IQR)
- **Top Global Matches:** file_cluster_8: 10.794, file_cluster_13: 10.89, file_cluster_17: 10.985
- **Magnitude:** 33.03 | **LOC:** 174 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (25.3447%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateSizes` (Impact: 311.8 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 6`, `doc: 2`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` react, useResizable, useSizes, useItems
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/transfer/Section.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.771 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.663 IQR)
- **Top Global Matches:** file_cluster_17: 10.771, file_cluster_13: 10.902, file_cluster_2: 10.917
- **Magnitude:** 32.07 | **LOC:** 449 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (20.852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TransferSection` (Impact: 232.8 | O(N^4) | DB: 7)
  * `onScroll` (Impact: 12.7 | O(N^1))
  * `handleClear` (Impact: 10.9 | O(N^1))
  * `getShowSearchOption` (Impact: 10.4 | O(N^1))
  * `getTextFromRenderResult` (Impact: 8.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 90`, `args: 54`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.642
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` transKeys, clsx, DownOutlined, dropdown, util, menu, react, ...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `components/auto-complete/AutoComplete.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.192 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.45 IQR)
- **Top Global Matches:** file_cluster_13: 10.192, file_cluster_8: 10.307, file_cluster_16: 10.469
- **Magnitude:** 29.75 | **LOC:** 299 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 53.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.3658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AutoComplete` (Impact: 269.2 | O(2^N) | DB: 2)
  * `isSelectOptionOrSelectOptGroup` (Impact: 8.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 58`, `args: 16`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`
* *Architecture:* `api: 9`, `import: 12`
* *Defense:* `safety: 11`, `doc: 14`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` clsx, hooks, util, select, statusUtils, react, select, warning...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/visual-regression/build.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.078 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_8: 10.078, file_cluster_4: 10.082, file_cluster_13: 10.209
- **Magnitude:** 29.57 | **LOC:** 566 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^2) | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (38.7248%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `boot` (Impact: 59.8 | O(N^2) | DB: 73)
  * `generateLineReport` (Impact: 54.8 | O(N^2) | DB: 1)
  * `generateReport` (Impact: 51.0 | O(N^1) | DB: 6)
  * `compareScreenshots` (Impact: 11.6 | O(N^1) | DB: 4)
  * `parseArgs` (Impact: 7.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 100`, `args: 32`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `dead_code: 1`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 59`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 3`, `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` node:stream, node:console, node:fs, sharp, difference, pngjs, reportAdapter, filter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/modal/ConfirmDialog.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.082 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.973 IQR)
- **Top Global Matches:** file_cluster_13: 10.082, file_cluster_2: 10.269, file_cluster_8: 10.451
- **Magnitude:** 28.83 | **LOC:** 299 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.1687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `confirmPrefixCls` (Impact: 241.8 | O(2^N) | DB: 4)
    * *Intent:* /** @private Internal Usage. Do not override this */
  * `ConfirmDialog` (Impact: 33.5 | O(N^2))
  * `ConfirmDialogWrapper` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 57`, `args: 18`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 22`
* *Defense:* `safety: 13`, `doc: 4`, `immutability_locks: 31`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` clsx, isNonNullable, InfoCircleFilled, Modal, context, CheckCircleFilled, motion, react...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `components/upload/Upload.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.562 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.19 IQR)
- **Top Global Matches:** file_cluster_8: 10.562, file_cluster_13: 10.572, file_cluster_17: 10.676
- **Magnitude:** 27.3 | **LOC:** 548 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (16.7602%), Tech Debt (10.3849%)
**Top Internal Functions/Classes:**
  * `InternalUpload` (Impact: 222.2 | O(N^3) | DB: 9)
    * *Intent:* /** * Get native element for wrapping upload * @since 5.17.0 */
  * `onProgress` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 74`, `args: 39`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 18`, `import: 16`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 54`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` upload, clsx, hooks, locale, util, react, style, react-dom...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `components/message/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.395 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.747 IQR)
- **Top Global Matches:** file_cluster_13: 11.395, file_cluster_17: 11.462, file_cluster_8: 11.526
- **Magnitude:** 27.26 | **LOC:** 346 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (29.9602%), Tech Debt (90.1764%)
**Top Internal Functions/Classes:**
  * `flushMessageQueue` (Impact: 142.6 | O(2^N))
  * `open` (Impact: 19.4 | O(2^N) | DB: 2)
  * `typeOpen` (Impact: 14.8 | O(N^2) | DB: 2)
  * `setCloseFn` (Impact: 12.6 | O(2^N))
  * `setMessageGlobalConfig` (Impact: 6.5 | O(N^1))
    * *Intent:* // ============================================================================== // == Export == //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 87`, `args: 54`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 25`, `duplicate_logic: 5`
* *Architecture:* `api: 4`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 36`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` useMessage, PurePanel, react, context, render, interface, config-provider, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/menu/MenuItem.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.244 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.292 IQR)
- **Top Global Matches:** file_cluster_13: 11.244, file_cluster_16: 11.606, file_cluster_8: 11.611
- **Magnitude:** 26.47 | **LOC:** 176 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GenericComponent` (Impact: 253.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 42`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 25`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.574
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` clsx, MenuContext, util, menu, react, tooltip, reactNode, Sider
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `eslint.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_1` (Drift: 8.658 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.78 IQR)
- **Top Global Matches:** file_cluster_1: 8.658, file_cluster_8: 8.994, file_cluster_7: 9.471
- **Magnitude:** 26.38 | **LOC:** 181 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 78.9%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.5416%), Tech Debt (68.0145%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 10`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 4`, `import: 6`
* *Defense:* `doc: 13`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint-plugin-jsx-a11y, eslint-plugin-compat, eslint-config, eslint-plugin-react-hooks, eslint-plugin-jest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `components/_util/throttleByAnimationFrame.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, args: 6, func_start: 5
- `alias/cssinjs.js` (JAVASCRIPT) | Magnitude: 18.68 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 6, safety: 4, globals: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 26.38 | Delta: **0.336 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 162, events: 91, doc: 13, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `components/modal/Modal.tsx` (TYPESCRIPT) | Magnitude: 21.73 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 227, structural_boundaries: 46, immutability_locks: 30, branch: 29
- `components/segmented/index.tsx` (TYPESCRIPT) | Magnitude: 2.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 52, generics: 36, branch: 30
- `components/steps/style/util.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, state_mutation: 5, immutability_locks: 4
- `components/typography/hooks/useTooltipProps.ts` (TYPESCRIPT) | Magnitude: 1.33 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, branch: 8, args: 2
- `.dumi/theme/utils/renderReactToHTML.tsx` (TYPESCRIPT) | Magnitude: 0.38 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, immutability_locks: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `components/table/interface.ts` (TYPESCRIPT) | Magnitude: 4.97 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 134, branch: 85, generics: 50
- `components/splitter/interface.ts` (TYPESCRIPT) | Magnitude: 4.12 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 54, branch: 50, api: 19
- `components/theme/interface/cssinjs-utils.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 15, generics: 9, api: 6
- `components/_util/reactNode.ts` (TYPESCRIPT) | Magnitude: 2.6 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 12, branch: 7, generics: 6
- `components/_util/capitalize.ts` (TYPESCRIPT) | Magnitude: 0.74 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, generics: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `components/input/hooks/useRemovePasswordTimeout.ts` (TYPESCRIPT) | Magnitude: 5.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, concurrency: 12, branch: 11
- `components/date-picker/__tests__/utils.ts` (TYPESCRIPT) | Magnitude: 3.94 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, branch: 10, structural_boundaries: 10, api: 8
- `index-style-only.js` (JAVASCRIPT) | Magnitude: 6.28 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 11, structural_boundaries: 4, safety: 4
- `scripts/visual-regression/reportAdapter.ts` (TYPESCRIPT) | Magnitude: 8.34 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 37, immutability_locks: 35, io: 27
- `components/form/hooks/useFrameState.ts` (TYPESCRIPT) | Magnitude: 3.43 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 19, structural_boundaries: 15, ui_framework: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `components/mentions/demo/async.tsx` (TYPESCRIPT) | Magnitude: 1.95 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 13, args: 13, func_start: 11
- `components/tooltip/demo/colorful.tsx` (TYPESCRIPT) | Magnitude: 0.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, ui_framework: 8, generics: 8, structural_boundaries: 6
- `components/table/ColumnGroup.ts` (TYPESCRIPT) | Magnitude: 3.65 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, ui_framework: 9, generics: 8, import: 4
- `components/list/demo/component-token.tsx` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, ui_framework: 23, generics: 21, structural_boundaries: 9
- `components/transfer/demo/search.tsx` (TYPESCRIPT) | Magnitude: 2.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, args: 11, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `components/upload/__tests__/requests.ts` (TYPESCRIPT) | Magnitude: 1.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, args: 4, func_start: 4
- `components/upload/demo/crop-image.tsx` (TYPESCRIPT) | Magnitude: 3.54 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, concurrency: 18, structural_boundaries: 14, args: 7
- `scripts/check-site.ts` (TYPESCRIPT) | Magnitude: 13.12 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 59, args: 41, func_start: 36
- `components/spin/usePercent.ts` (TYPESCRIPT) | Magnitude: 5.28 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 10, state_mutation: 9, branch: 8
- `scripts/generate-cssinjs.ts` (TYPESCRIPT) | Magnitude: 3.35 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, args: 13, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `components/config-provider/hooks/useCSSVarCls.ts` (TYPESCRIPT) | Magnitude: 3.33 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, doc: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `components/theme/index.tsx` (TYPESCRIPT) | Magnitude: 0.45 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, import: 6, doc: 4
- `components/badge/ScrollNumber.tsx` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, branch: 17, structural_boundaries: 15, ui_framework: 6
- `components/form/demo/label-debug.tsx` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, ui_framework: 7, generics: 5, structural_boundaries: 4
- `components/result/demo/success.tsx` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, ui_framework: 3, func_start: 2
- `components/form/demo/col-24-debug.tsx` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 101, ui_framework: 20, generics: 20, structural_boundaries: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `eslint.config.mjs` -> Churn: **63.65%** | Cog Load: 3.5416% | Debt: 68.0145%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/visual-regression/upload.js` -> **thinkasany** (100.0% isolated ownership) | Magnitude: 113.08
- `.dumi/scripts/mirror-notify.js` -> **lijianan** (100.0% isolated ownership) | Magnitude: 83.14
- `components/table/hooks/useSorter.tsx` -> **lijianan** (100.0% isolated ownership) | Magnitude: 81.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `components/color-picker/components/PanelPicker/GradientColorBar.tsx` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 84.6082%)
- `components/_util/responsiveObserver.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 94.9559%)
- `components/calendar/Header.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 87.3543%)
- `components/grid/col.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `components/theme/useToken.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 17.7499%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `components/theme/internal.ts` -> **Severity: 2670.7** (Blast Radius: 26.707 * Doc Risk: 100.0%)
- `alias/cssinjs.js` -> **Severity: 1681.879** (Blast Radius: 28.377 * Doc Risk: 59.2691%)
- `components/theme/util/genStyleUtils.ts` -> **Severity: 836.8** (Blast Radius: 8.368 * Doc Risk: 100.0%)
- `components/theme/interface/cssinjs-utils.ts` -> **Severity: 709.4** (Blast Radius: 7.094 * Doc Risk: 100.0%)
- `components/theme/themes/shared/genFontSizes.ts` -> **Severity: 374.488** (Blast Radius: 3.768 * Doc Risk: 99.3864%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
