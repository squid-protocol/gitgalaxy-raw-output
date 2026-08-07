# ARCHITECTURAL_BRIEF: ant-design
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/ant-design` |
| **Timestamp** | `2026-08-07T04:21:30.788752+00:00` |
| **Scan Duration** | `6.63s` |
| **Git Branch** | `master` |
| **Git Commit** | `a8ae51fe861dc0db2fc581938b38d7bbab5ba8f5` |
| **Git Remote** | `https://github.com/ant-design/ant-design.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2087 malicious artifacts.

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
| Total Artifacts | 4763 |
| Analyzed Artifacts (Scanned) | 3266 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1497 |
| Total LOC | 135905 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.6% |
| Dominant Lang | PLAINTEXT |

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
> **Architectural Drift Z-Score:** `3.214`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1099 | 33.6% |
| file_cluster_13 | 621 | 19.0% |
| file_cluster_2 | 331 | 10.1% |
| file_cluster_17 | 22 | 0.7% |
| file_cluster_4 | 14 | 0.4% |
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
| Error & Exception Exposure | 0.0 | 98.1 | 11.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.8 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.3 | 4.4 | 4.0 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 36.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.0 | 1.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 63.7 | 5.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 17.4 | 14.4 | 11.9 |
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

- `useSelection` (@ `components/table/hooks/useSelection.tsx`) -> Impact: **278.0** | LOC: 680
- `InternalTable` (@ `components/table/InternalTable.tsx`) -> Impact: **232.3** | LOC: 567
- `InternalFormItem` (@ `components/form/FormItem/index.tsx`) -> Impact: **205.2** | LOC: 331
- `FilterDropdown` (@ `components/table/hooks/useFilter/FilterDropdown.tsx`) -> Impact: **160.7** | LOC: 442
- `updatePrevSelectedIndex` (@ `components/table/hooks/useSelection.tsx`) -> Impact: **128.8** | LOC: 370
- `Transfer` (@ `components/transfer/index.tsx`) -> Impact: **126.0** | LOC: 441
- `InternalUpload` (@ `components/upload/Upload.tsx`) -> Impact: **123.5** | LOC: 495
  * *Intent:* /** * Get native element for wrapping upload * @since 5.17.0 */
- `Steps` (@ `components/steps/index.tsx`) -> Impact: **109.4** | LOC: 308
- `ProviderChildren` (@ `components/config-provider/index.tsx`) -> Impact: **109.1** | LOC: 380
- `InternalList` (@ `components/list/index.tsx`) -> Impact: **107.7** | LOC: 248

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 24 | 5291.38 | 7.16% | 2.83% |
| `.dumi/scripts` | 2 | 182.38 | 11.53% | 50.0% |
| `components/table/demo` | 101 | 169.13 | 2.99% | 23.63% |
| `scripts/visual-regression` | 6 | 156.38 | 27.61% | 55.57% |
| `components/table/hooks` | 6 | 149.0 | 23.54% | 66.02% |
| `components/locale` | 75 | 139.36 | 4.39% | 0.88% |
| `components/message` | 7 | 137.21 | 13.65% | 19.3% |
| `scripts` | 18 | 118.83 | 37.89% | 42.6% |
| `components/date-picker/locale` | 69 | 111.65 | 4.54% | 0.0% |
| `components/form/demo` | 79 | 103.11 | 3.11% | 5.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `components/_util/ActionButton.tsx` -> **100.0%** Exposure
- `components/_util/motion.ts` -> **100.0%** Exposure
- `components/_util/warning.ts` -> **100.0%** Exposure
- `components/checkbox/useBubbleLock.ts` -> **100.0%** Exposure
- `components/date-picker/demo/external-panel.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.dumi/theme/utils/index.ts` -> **100.0%** Exposure
- `components/_util/ActionButton.tsx` -> **100.0%** Exposure
- `components/_util/getAllowClear.tsx` -> **100.0%** Exposure
- `components/_util/getScroll.ts` -> **100.0%** Exposure
- `components/_util/hooks/useMultipleSelect.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `components/table/hooks/useSelection.tsx` -> **0** Orphaned Functions | **28** Duplicates
- `scripts/pre-publish.ts` -> **1** Orphaned Functions | **21** Duplicates
- `components/message/index.tsx` -> **0** Orphaned Functions | **21** Duplicates
- `components/date-picker/demo/external-panel.tsx` -> **0** Orphaned Functions | **20** Duplicates
- `.dumi/scripts/mirror-notify.js` -> **4** Orphaned Functions | **14** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4226` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `components/_util/ActionButton.tsx` (TYPESCRIPT) -> Cumulative Risk: **668.46**
- **Archetype:** `file_cluster_13` (Distance: 11.87 IQR)
- **Magnitude:** 15.42 | **LOC:** 137 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `ActionButton` (Impact: 36.5), `onClick` (Impact: 26.0), `handlePromiseOnOk` (Impact: 11.2)

### 2. `components/spin/usePercent.ts` (TYPESCRIPT) -> Cumulative Risk: **591.57**
- **Archetype:** `file_cluster_4` (Distance: 11.248 IQR)
- **Magnitude:** 4.68 | **LOC:** 50 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9967%)
- **Heaviest Functions:** `usePercent` (Impact: 18.0), `setMockPercent` (Impact: 5.1), `setMockPercent` (Impact: 4.9)

### 3. `components/tree/demo/drag-debug.tsx` (TYPESCRIPT) -> Cumulative Risk: **569.95**
- **Archetype:** `file_cluster_13` (Distance: 11.474 IQR)
- **Magnitude:** 15.61 | **LOC:** 153 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9976%), Safety Score (90.3374%)
- **Heaviest Functions:** `FC` (Impact: 38.9), `onDrop` (Impact: 29.1), `innerSetShowLine` (Impact: 10.6)

### 4. `components/modal/confirm.tsx` (TYPESCRIPT) -> Cumulative Risk: **563.92**
- **Archetype:** `file_cluster_13` (Distance: 10.931 IQR)
- **Magnitude:** 16.16 | **LOC:** 198 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.5225%), Concurrency (92.6582%), Verification (80.0%)
- **Heaviest Functions:** `confirm` (Impact: 30.4), `ConfirmDialogWrapper` (Impact: 20.8), `destroy` (Impact: 14.8)

### 5. `components/spin/demo/percent.tsx` (TYPESCRIPT) -> Cumulative Risk: **562.34**
- **Archetype:** `file_cluster_2` (Distance: 11.282 IQR)
- **Magnitude:** 3.68 | **LOC:** 45 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9997%), Cognitive Load (91.16%)
- **Heaviest Functions:** `FC` (Impact: 8.9), `clearTimeout` (Impact: 3.5), `setPercent` (Impact: 3.0)

### 6. `components/tree/demo/draggable.tsx` (TYPESCRIPT) -> Cumulative Risk: **561.16**
- **Archetype:** `file_cluster_13` (Distance: 11.398 IQR)
- **Magnitude:** 10.97 | **LOC:** 112 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6183%), Safety Score (89.8164%)
- **Heaviest Functions:** `FC` (Impact: 19.4), `onDrop` (Impact: 18.3), `generateData` (Impact: 17.1)

### 7. `components/splitter/hooks/sizeUtil.ts` (TYPESCRIPT) -> Cumulative Risk: **557.87**
- **Archetype:** `file_cluster_8` (Distance: 11.117 IQR)
- **Magnitude:** 7.84 | **LOC:** 85 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (85.0043%)
- **Heaviest Functions:** `autoPtgSizes` (Impact: 51.1)

### 8. `components/message/__tests__/util.ts` (TYPESCRIPT) -> Cumulative Risk: **557.7**
- **Archetype:** `file_cluster_4` (Distance: 11.373 IQR)
- **Magnitude:** 5.1 | **LOC:** 25 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `triggerMotionEnd` (Impact: 5.3), `awaitPromise` (Impact: 3.7), `act` (Impact: 1.6)

### 9. `scripts/print-changelog.ts` (TYPESCRIPT) -> Cumulative Risk: **556.53**
- **Archetype:** `file_cluster_4` (Distance: 10.832 IQR)
- **Magnitude:** 12.97 | **LOC:** 392 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9997%), Tech Debt (98.738%), Cognitive Load (80.8304%)
- **Heaviest Functions:** `printLog` (Impact: 50.6), `getDescription` (Impact: 7.2), `validate` (Impact: 4.3)

### 10. `components/notification/__tests__/util.ts` (TYPESCRIPT) -> Cumulative Risk: **542.97**
- **Archetype:** `file_cluster_4` (Distance: 12.198 IQR)
- **Magnitude:** 5.8 | **LOC:** 31 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `triggerMotionEnd` (Impact: 12.3), `awaitPromise` (Impact: 3.7), `act` (Impact: 1.6)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.dumi/scripts/mirror-notify.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.822 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.322 IQR)
- **Top Global Matches:** file_cluster_8: 8.822, file_cluster_7: 9.546, file_cluster_4: 9.596
- **Magnitude:** 158.14 | **LOC:** 274 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.0592%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `createMirrorModal` (Impact: 44.8)
  * `createNotification` (Impact: 13.0)
  * `checkMirrorAvailable` (Impact: 10.2)
  * `resolve` (Impact: 8.0)
  * `startProgressTimer` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 21`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 8`, `duplicate_logic: 14`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `concurrency: 10`
* *Defense:* `safety: 5`, `immutability_locks: 18`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/visual-regression/upload.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.522 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.014 IQR)
- **Top Global Matches:** file_cluster_4: 11.522, file_cluster_13: 11.776, file_cluster_8: 11.946
- **Magnitude:** 100.78 | **LOC:** 170 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.2127%), Tech Debt (87.3855%)
**Top Internal Functions/Classes:**
  * `boot` (Impact: 20.7)
  * `uploadFile` (Impact: 9.3)
  * `walkDir` (Impact: 9.0)
  * `retry` (Impact: 8.9)
  * `parseArgs` (Impact: 7.7)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 9`, `func_start: 13`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 1`, `concurrency: 18`, `import: 4`
* *Defense:* `safety: 8`, `doc: 6`, `test: 4`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ali-oss, node:assert, node:path, node:fs
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/table/hooks/useSelection.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.77 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.535 IQR)
- **Top Global Matches:** file_cluster_17: 11.77, file_cluster_13: 12.024, file_cluster_2: 12.161
- **Magnitude:** 87.37 | **LOC:** 757 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (33.5645%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `useSelection` (Impact: 278.0)
  * `updatePrevSelectedIndex` (Impact: 128.8)
  * `triggerSingleSelection` (Impact: 61.1)
  * `renderCell` (Impact: 48.6)
  * `updatePrevSelectedIndex` (Impact: 36.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 128`, `args: 85`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 72`, `planned_debt: 1`, `duplicate_logic: 28`
* *Architecture:* `api: 6`, `import: 19`
* *Defense:* `safety: 34`, `immutability_locks: 94`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` interface, dropdown, conductUtil, clsx, hooks, checkbox, util, treeUtil...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/message/interface.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.238 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.319 IQR)
- **Top Global Matches:** file_cluster_8: 10.238, file_cluster_16: 10.302, file_cluster_13: 10.346
- **Magnitude:** 86.34 | **LOC:** 110 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 66.7%
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

### `components/table/InternalTable.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.064 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.327 IQR)
- **Top Global Matches:** file_cluster_13: 11.064, file_cluster_2: 11.207, file_cluster_17: 11.314
- **Magnitude:** 44.24 | **LOC:** 772 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 44.0%
- **Risk Profile:** Cognitive Load (19.3554%), Tech Debt (56.15%)
**Top Internal Functions/Classes:**
  * `InternalTable` (Impact: 232.3)
  * `resetPagination` (Impact: 40.3)
  * `transformSelectionColumns` (Impact: 32.6)
  * `triggerOnChange` (Impact: 28.8)
  * `warning` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 144`, `args: 45`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 13`, `duplicate_logic: 7`
* *Architecture:* `api: 13`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 31`, `doc: 2`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.977
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` useTitleColumns, warning, spin, context, usePagination, clsx, pagination, useFilter...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `components/table/hooks/useSorter.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.045 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.259 IQR)
- **Top Global Matches:** file_cluster_2: 11.045, file_cluster_17: 11.096, file_cluster_13: 11.247
- **Magnitude:** 43.32 | **LOC:** 524 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.2121%), Tech Debt (96.8917%)
**Top Internal Functions/Classes:**
  * `triggerSorter` (Impact: 84.3)
  * `finalColumns` (Impact: 56.0)
  * `useFilterSorter` (Impact: 41.1)
  * `collectSortStates` (Impact: 27.0)
  * `onHeaderCell` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 96`, `args: 47`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 46`, `duplicate_logic: 11`
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `safety: 11`, `immutability_locks: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.299
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` interface, locale, util, clsx, KeyCode, CaretDownOutlined, tooltip, react...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `webpack.config.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.819 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.562 IQR)
- **Top Global Matches:** file_cluster_13: 10.819, file_cluster_0: 10.931, file_cluster_17: 11.096
- **Magnitude:** 42.02 | **LOC:** 94 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.3895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addPluginsForProduction` (Impact: 10.4)
  * `externalCssinjs` (Impact: 5.5)
  * `addLocales` (Impact: 4.0)
  * `externalDayjs` (Impact: 2.2)
  * `codecovWebpackPlugin` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`
* *Architecture:* `io: 3`, `api: 1`, `import: 6`
* *Defense:* `safety: 4`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` webpack-plugin, tools, circular-dependency-plugin, webpack-bundle-analyzer, node:path, duplicate-package-checker-webpack-plugin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/form/FormItem/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.508 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.407 IQR)
- **Top Global Matches:** file_cluster_13: 10.508, file_cluster_17: 10.793, file_cluster_2: 10.794
- **Magnitude:** 38.87 | **LOC:** 459 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (30.8399%), Tech Debt (97.3766%)
**Top Internal Functions/Classes:**
  * `InternalFormItem` (Impact: 205.2)
  * `isSimilarControl` (Impact: 32.4)
  * `setMeta` (Impact: 18.9)
    * *Intent:* // Destroy will reset all the meta
  * `warning` (Impact: 16.6)
  * `renderLayout` (Impact: 13.2)
    * *Intent:* // ======================== Render ========================
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 79`, `args: 31`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 24`, `duplicate_logic: 9`
* *Architecture:* `io: 2`, `api: 4`, `import: 26`
* *Defense:* `safety: 9`, `immutability_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ItemHolder, isNonNullable, Form, clsx, util, warning, useState, reactNode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/table/hooks/useFilter/FilterDropdown.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.457 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.378 IQR)
- **Top Global Matches:** file_cluster_13: 10.457, file_cluster_8: 10.489, file_cluster_2: 10.634
- **Magnitude:** 38.8 | **LOC:** 592 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (16.3671%), Tech Debt (99.0716%)
**Top Internal Functions/Classes:**
  * `FilterDropdown` (Impact: 160.7)
  * `getFilterComponent` (Impact: 35.0)
  * `internalTriggerFilter` (Impact: 18.8)
    * *Intent:* // ======================= Submit ========================
  * `onVisibleChange` (Impact: 12.8)
  * `getDropdownTrigger` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 106`, `args: 62`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `duplicate_logic: 15`
* *Architecture:* `api: 7`, `import: 27`
* *Defense:* `safety: 18`, `immutability_locks: 45`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` clsx, FilterSearch, OverrideContext, tree, react, menu, , dropdown...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/transfer/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.674 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.056 IQR)
- **Top Global Matches:** file_cluster_13: 10.674, file_cluster_8: 10.827, file_cluster_2: 10.829
- **Magnitude:** 32.69 | **LOC:** 617 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (11.9796%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `Transfer` (Impact: 126.0)
  * `onItemSelect` (Impact: 20.8)
  * `data` (Impact: 13.7)
  * `onItemSelectAll` (Impact: 12.3)
  * `getStatusClassNames` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 125`, `args: 70`, `func_start: 47`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`, `duplicate_logic: 4`
* *Architecture:* `api: 20`, `import: 27`
* *Defense:* `safety: 22`, `doc: 6`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` warning, context, clsx, locale, interface, en_US, Section, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/upload/Upload.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.573 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.176 IQR)
- **Top Global Matches:** file_cluster_13: 10.573, file_cluster_8: 10.575, file_cluster_17: 10.672
- **Magnitude:** 29.01 | **LOC:** 548 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (25.334%), Tech Debt (81.2375%)
**Top Internal Functions/Classes:**
  * `InternalUpload` (Impact: 123.5)
    * *Intent:* /** * Get native element for wrapping upload * @since 5.17.0 */
  * `warning` (Impact: 21.8)
  * `handleRemove` (Impact: 19.2)
  * `onBatchStart` (Impact: 13.0)
  * `mergedBeforeUpload` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 74`, `args: 35`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `concurrency: 18`, `import: 16`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 54`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` warning, utils, context, clsx, hooks, DisabledContext, util, locale...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/visual-regression/build.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.011 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.23 IQR)
- **Top Global Matches:** file_cluster_4: 10.011, file_cluster_8: 10.032, file_cluster_13: 10.152
- **Magnitude:** 28.24 | **LOC:** 566 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (37.6833%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `generateReport` (Impact: 51.0)
  * `boot` (Impact: 43.3)
  * `generateLineReport` (Impact: 37.6)
  * `compareScreenshots` (Impact: 11.6)
  * `parseArgs` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 100`, `args: 32`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 37`, `api: 1`, `concurrency: 59`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 3`, `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.602
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` promises, pngjs, filter, node:os, node:fs, reportAdapter, p-all, difference...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/transfer/Section.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.714 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.65 IQR)
- **Top Global Matches:** file_cluster_17: 10.714, file_cluster_13: 10.852, file_cluster_2: 10.873
- **Magnitude:** 26.82 | **LOC:** 449 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (14.5201%), Tech Debt (64.9583%)
**Top Internal Functions/Classes:**
  * `TransferSection` (Impact: 102.9)
  * `renderListBody` (Impact: 12.8)
  * `handleClear` (Impact: 10.9)
  * `onScroll` (Impact: 10.4)
  * `getShowSearchOption` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 90`, `args: 51`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `duplicate_logic: 5`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 16`, `doc: 1`, `immutability_locks: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.642
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` dropdown, checkbox, menu, clsx, transKeys, util, , ListBody...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `eslint.config.mjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_1` (Drift: 8.658 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.78 IQR)
- **Top Global Matches:** file_cluster_1: 8.658, file_cluster_8: 8.994, file_cluster_7: 9.471
- **Magnitude:** 26.38 | **LOC:** 181 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 78.9%
- **Risk Profile:** Cognitive Load (3.5416%), Tech Debt (68.0145%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 10`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 4`, `import: 6`
* *Defense:* `doc: 13`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` eslint-config, eslint-plugin-compat, eslint-plugin-react-hooks, eslint-plugin-jest, eslint-plugin-jsx-a11y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/anchor/Anchor.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.855 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.722 IQR)
- **Top Global Matches:** file_cluster_13: 10.855, file_cluster_17: 11.053, file_cluster_2: 11.066
- **Magnitude:** 25.72 | **LOC:** 433 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 43.8%
- **Risk Profile:** Cognitive Load (20.5164%), Tech Debt (97.9214%)
**Top Internal Functions/Classes:**
  * `Anchor` (Impact: 104.8)
  * `updateInk` (Impact: 18.1)
  * `getInternalCurrentAnchor` (Impact: 15.2)
  * `setCurrentActiveLink` (Impact: 13.1)
  * `getOffsetTop` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 95`, `args: 42`, `func_start: 21`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `fragile_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 14`, `import: 17`
* *Defense:* `safety: 21`, `doc: 5`, `immutability_locks: 54`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` warning, context, AnchorLink, useCSSVarCls, context, affix, clsx, hooks...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `.dumi/scripts/clarity.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.519 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.514 IQR)
- **Top Global Matches:** file_cluster_8: 10.519, file_cluster_4: 10.533, file_cluster_15: 11.016
- **Magnitude:** 24.24 | **LOC:** 15 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `args: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `concurrency: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/calendar/generateCalendar.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.022 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.567 IQR)
- **Top Global Matches:** file_cluster_8: 10.022, file_cluster_2: 10.081, file_cluster_13: 10.081
- **Magnitude:** 23.91 | **LOC:** 417 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.0954%), Tech Debt (72.9408%)
**Top Internal Functions/Classes:**
  * `generateCalendar` (Impact: 81.5)
  * `Calendar` (Impact: 70.5)
  * `triggerChange` (Impact: 14.8)
  * `setMergedValue` (Impact: 10.5)
  * `mergedCellRender` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 98`, `args: 38`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 10`, `import: 16`
* *Defense:* `safety: 14`, `doc: 8`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.687
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` warning, context, generate, clsx, Header, hooks, locale, util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/pre-publish.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.665 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.6 IQR)
- **Top Global Matches:** file_cluster_4: 10.665, file_cluster_13: 10.915, file_cluster_8: 10.974
- **Magnitude:** 21.34 | **LOC:** 285 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.4989%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `runPrePublish` (Impact: 38.5)
  * `showMessage` (Impact: 31.0)
  * `showMessage` (Impact: 11.0)
  * `showMessage` (Impact: 10.7)
  * `downloadArtifact` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 41`, `args: 52`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 17`, `fragile_debt: 3`, `duplicate_logic: 21`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `concurrency: 37`, `import: 11`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` axios, rest, simple-git, check-repo, node:fs, dotenv, adm-zip, chalk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.dumi/theme/utils/index.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.902 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.985 IQR)
- **Top Global Matches:** file_cluster_17: 10.902, file_cluster_8: 11.076, file_cluster_13: 11.12
- **Magnitude:** 21.32 | **LOC:** 217 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (51.6641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getMenuItems` (Impact: 65.8)
  * `sortFn` (Impact: 44.9)
  * `getMetaDescription` (Impact: 18.4)
  * `matchDeprecated` (Impact: 6.5)
  * `getLocalizedPathname` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 80`, `args: 23`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 39`
* *Architecture:* `io: 5`, `api: 14`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BUG_VERSIONS.json, flattenDeep, flatten, semver
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/config-provider/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.969 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.7 IQR)
- **Top Global Matches:** file_cluster_8: 9.969, file_cluster_13: 10.09, file_cluster_2: 10.329
- **Magnitude:** 20.76 | **LOC:** 777 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (11.5323%), Tech Debt (14.6883%)
**Top Internal Functions/Classes:**
  * `ProviderChildren` (Impact: 109.1)
  * `globalConfig` (Impact: 11.4)
  * `setGlobalConfig` (Impact: 10.8)
  * `getPrefixCls` (Impact: 9.0)
  * `warning` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 91`, `args: 31`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 27`
* *Defense:* `safety: 11`, `doc: 13`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` warning, validateMessagesContext, locale, util, en_US, react, context, seed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/check-site.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.337 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 7.085 IQR)
- **Top Global Matches:** file_cluster_4: 10.337, file_cluster_8: 10.415, file_cluster_13: 10.532
- **Magnitude:** 20.05 | **LOC:** 192 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.5685%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 46.5)
  * `render` (Impact: 27.2)
  * `expectComponent` (Impact: 17.4)
  * `getTextContent` (Impact: 12.9)
  * `first` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 59`, `args: 41`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 7`, `duplicate_logic: 10`, `orphaned_logic: 3`
* *Architecture:* `io: 17`, `concurrency: 30`, `import: 9`
* *Defense:* `safety: 1`, `doc: 1`, `test: 26`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:https, node:http, uniq, http-server, isomorphic-fetch, glob, domparser-rs, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/message/index.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.297 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.779 IQR)
- **Top Global Matches:** file_cluster_13: 11.297, file_cluster_17: 11.358, file_cluster_8: 11.433
- **Magnitude:** 19.62 | **LOC:** 346 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (18.5784%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `flushMessageQueue` (Impact: 31.8)
  * `typeOpen` (Impact: 10.5)
  * `render` (Impact: 8.7)
  * `setCloseFn` (Impact: 8.2)
  * `open` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 87`, `args: 52`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 23`, `duplicate_logic: 21`
* *Architecture:* `api: 4`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 36`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` useMessage, context, PurePanel, util, interface, config-provider, render, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/message/useMessage.tsx` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.748 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.994 IQR)
- **Top Global Matches:** file_cluster_13: 10.748, file_cluster_8: 10.895, file_cluster_17: 11.156
- **Magnitude:** 19.45 | **LOC:** 329 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (13.0322%), Tech Debt (35.1328%)
**Top Internal Functions/Classes:**
  * `useInternalMessage` (Impact: 52.0)
  * `open` (Impact: 34.1)
    * *Intent:* // >>> Open
  * `TypeOpen` (Impact: 15.4)
  * `destroy` (Impact: 10.3)
    * *Intent:* // >>> destroy
  * `getContainer` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 60`, `args: 26`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 15`
* *Defense:* `safety: 15`, `immutability_locks: 43`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.607
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` warning, context, useCSSVarCls, PurePanel, clsx, notification, hooks, util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `alias/cssinjs.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.115 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_0: 13.115, file_cluster_13: 13.246, file_cluster_8: 13.666
- **Magnitude:** 18.68 | **LOC:** 20 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.377
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cssinjs
  * `Imported By (In-Degree: 167):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `components/_util/throttleByAnimationFrame.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, args: 6, func_start: 5
- `alias/cssinjs.js` (JAVASCRIPT) | Magnitude: 18.68 | Delta: **0.131 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 6, safety: 4, globals: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 26.38 | Delta: **0.336 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 162, events: 91, doc: 13, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `.dumi/theme/utils/renderReactToHTML.tsx` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, immutability_locks: 4, import: 3
- `components/segmented/index.tsx` (TYPESCRIPT) | Magnitude: 2.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 52, generics: 36, branch: 30
- `components/steps/style/util.ts` (TYPESCRIPT) | Magnitude: 1.83 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, state_mutation: 5, immutability_locks: 4
- `components/upload/Upload.tsx` (TYPESCRIPT) | Magnitude: 29.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 408, structural_boundaries: 74, branch: 58, immutability_locks: 54
- `components/typography/hooks/useTooltipProps.ts` (TYPESCRIPT) | Magnitude: 1.33 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, branch: 8, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `components/table/interface.ts` (TYPESCRIPT) | Magnitude: 4.97 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 134, branch: 85, generics: 50
- `components/splitter/interface.ts` (TYPESCRIPT) | Magnitude: 3.72 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 54, branch: 50, api: 19
- `components/theme/interface/cssinjs-utils.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 15, generics: 9, api: 6
- `components/_util/reactNode.ts` (TYPESCRIPT) | Magnitude: 2.6 | Delta: **0.16 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 12, branch: 7, generics: 6
- `components/_util/capitalize.ts` (TYPESCRIPT) | Magnitude: 0.74 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, generics: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `components/date-picker/__tests__/utils.ts` (TYPESCRIPT) | Magnitude: 3.94 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, branch: 10, structural_boundaries: 10, api: 8
- `index-style-only.js` (JAVASCRIPT) | Magnitude: 6.28 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, branch: 11, structural_boundaries: 4, safety: 4
- `scripts/visual-regression/reportAdapter.ts` (TYPESCRIPT) | Magnitude: 7.64 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, structural_boundaries: 37, immutability_locks: 35, io: 27
- `components/form/hooks/useFrameState.ts` (TYPESCRIPT) | Magnitude: 3.82 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 19, structural_boundaries: 15, ui_framework: 11
- `components/descriptions/hooks/useRow.ts` (TYPESCRIPT) | Magnitude: 5.8 | Delta: **0.108 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 27, structural_boundaries: 16, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `components/tooltip/demo/colorful.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, ui_framework: 8, generics: 8, structural_boundaries: 6
- `components/table/ColumnGroup.ts` (TYPESCRIPT) | Magnitude: 3.65 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 16, ui_framework: 9, generics: 8, import: 4
- `components/list/demo/component-token.tsx` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 96, ui_framework: 23, generics: 21, structural_boundaries: 9
- `components/transfer/demo/search.tsx` (TYPESCRIPT) | Magnitude: 3.03 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, args: 11, func_start: 11
- `components/progress/design/demo/info.tsx` (TYPESCRIPT) | Magnitude: 0.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 8, ui_framework: 5, generics: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `components/upload/__tests__/requests.ts` (TYPESCRIPT) | Magnitude: 1.24 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, args: 4, func_start: 4
- `scripts/visual-regression/build.ts` (TYPESCRIPT) | Magnitude: 28.24 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 384, structural_boundaries: 100, immutability_locks: 87, concurrency: 59
- `components/upload/demo/crop-image.tsx` (TYPESCRIPT) | Magnitude: 4.4 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, concurrency: 18, structural_boundaries: 14, ui_framework: 7
- `scripts/check-site.ts` (TYPESCRIPT) | Magnitude: 20.05 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 59, args: 41, func_start: 36
- `scripts/generate-cssinjs.ts` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, args: 13, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `components/config-provider/hooks/useCSSVarCls.ts` (TYPESCRIPT) | Magnitude: 3.33 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, state_mutation: 3, doc: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `components/theme/index.tsx` (TYPESCRIPT) | Magnitude: 0.45 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, import: 6, doc: 4
- `components/form/demo/col-24-debug.tsx` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 101, ui_framework: 20, generics: 20, structural_boundaries: 9
- `components/avatar/demo/dynamic.tsx` (TYPESCRIPT) | Magnitude: 2.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 29, immutability_locks: 11, structural_boundaries: 7, func_start: 7
- `components/form/demo/label-debug.tsx` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, ui_framework: 7, generics: 5, structural_boundaries: 4
- `components/result/demo/success.tsx` (TYPESCRIPT) | Magnitude: 0.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, ui_framework: 3, func_start: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `eslint.config.mjs` -> Churn: **63.69%** | Cog Load: 3.5416% | Debt: 68.0145%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `.dumi/scripts/mirror-notify.js` -> **lijianan** (100.0% isolated ownership) | Magnitude: 158.14
- `scripts/visual-regression/upload.js` -> **thinkasany** (100.0% isolated ownership) | Magnitude: 100.78

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

- `components/theme/internal.ts` -> **Severity: 2070.706** (Blast Radius: 26.707 * Doc Risk: 77.5342%)
- `alias/cssinjs.js` -> **Severity: 844.851** (Blast Radius: 28.377 * Doc Risk: 29.7724%)
- `components/theme/util/genStyleUtils.ts` -> **Severity: 836.8** (Blast Radius: 8.368 * Doc Risk: 100.0%)
- `components/theme/interface/cssinjs-utils.ts` -> **Severity: 709.4** (Blast Radius: 7.094 * Doc Risk: 100.0%)
- `components/theme/useToken.ts` -> **Severity: 322.35** (Blast Radius: 8.977 * Doc Risk: 35.9084%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
