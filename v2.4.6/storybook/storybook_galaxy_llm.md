# ARCHITECTURAL_BRIEF: storybook
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/storybook` |
| **Timestamp** | `2026-08-03T19:57:09.970971+00:00` |
| **Scan Duration** | `11.02s` |
| **Git Branch** | `next` |
| **Git Commit** | `ce8c743b04264c5e8010df1181c828171a04c33a` |
| **Git Remote** | `https://github.com/storybookjs/storybook.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2629 malicious artifacts.

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
| Total Artifacts | 5516 |
| Analyzed Artifacts (Scanned) | 3101 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2415 |
| Total LOC | 244494 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 56.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.687 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1958 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8697 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 55 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2400 | 231445 | 77.4% |
| JAVASCRIPT | 225 | 6608 | 7.3% |
| JSON | 128 | 2316 | 4.1% |
| HTML | 112 | 3169 | 3.6% |
| MARKDOWN | 107 | 0 | 3.5% |
| PLAINTEXT | 77 | 1 | 2.5% |
| CSS | 32 | 623 | 1.0% |
| YAML | 10 | 279 | 0.3% |
| XML | 6 | 4 | 0.2% |
| SHELL | 4 | 49 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.169`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1767 | 57.0% |
| file_cluster_13 | 813 | 26.2% |
| file_cluster_4 | 131 | 4.2% |
| file_cluster_16 | 51 | 1.6% |
| file_cluster_17 | 50 | 1.6% |
| file_cluster_2 | 47 | 1.5% |
| file_cluster_0 | 46 | 1.5% |
| file_cluster_11 | 2 | 0.1% |
| file_cluster_6 | 2 | 0.1% |
| file_cluster_9 | 2 | 0.1% |
| Unknown | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_5 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 183 | 5.9% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2415*

**Composition by Extension & Reason:**
- `.md`: 733x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5720 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3544 LOC)
- `.ts`: 341x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 55 LOC), 5x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.tsx`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 18 exceeds 500 chars)
- `.png`: 213x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 203x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 18x Excluded (Machine-Generated Source Code Signature: 35 LOC), 10x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.snapshot`: 113x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Unsupported Format (.snapshot)
- `.js`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 30 LOC), 5x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `no_extension`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.pug`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Unsupported Format (.pug)
- `.yml`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp4`: 37x Excluded (Explicitly Denied Extension: '.mp4')
- `.jsx`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 30 LOC), 1x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `.svelte`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Machine-Generated Source Code Signature: 27 LOC)
- `.css`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.3 | 6.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 23.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.7 | 0.8 | 0.0 |
| API Exposure | 0.0 | 19.4 | 4.8 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 94.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.7 | 0.3 | 0.1 | 0.1 |
| Volatility Exposure | 0.0 | 80.3 | 11.6 | 14.4 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 48.3 | 45.6 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `code/core/src/manager/components/sidebar/mockdata.large.ts` (Hits: 941)
- `code/addons/vitest/src/updateVitestFile.config.4.test.ts` (Hits: 160)
- `code/addons/vitest/src/updateVitestFile.config.test.ts` (Hits: 160)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vitest.ts** (`code/addons/vitest/src/node/vitest.ts`) — 376 inbound connections
2. **common.tsx** (`code/core/src/components/components/typography/lib/common.tsx`) — 208 inbound connections
3. **test.sh** (`scripts/ecosystem-ci/test.sh`) — 199 inbound connections
4. **global.ts** (`code/core/src/theming/global.ts`) — 161 inbound connections
5. **core.ts** (`code/core/src/bin/core.ts`) — 88 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`code/core/src/components/index.ts`) — 76 outbound dependencies
2. **index.ts** (`code/core/src/common/index.ts`) — 47 outbound dependencies
3. **getComponentImports.test.ts** (`code/renderers/react/src/componentManifest/getComponentImports.test.ts`) — 32 outbound dependencies
4. **task.ts** (`scripts/task.ts`) — 32 outbound dependencies
5. **sandbox-parts.ts** (`scripts/tasks/sandbox-parts.ts`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `describe` (@ `code/core/src/csf-tools/vitest-plugin/transformer.test.ts`) -> Impact: **1331.2** | LOC: 1337
- `resolveLiteralValue` (@ `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts`) -> Impact: **1191.7** | LOC: 400
- `describe` (@ `code/core/src/csf-tools/ConfigFile.test.ts`) -> Impact: **1186.8** | LOC: 1739
- `describe` (@ `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts`) -> Impact: **1096.6** | LOC: 1494
- `appendToExistingProjectRefs` (@ `code/addons/vitest/src/updateVitestFile.ts`) -> Impact: **1022.2** | LOC: 358
- `getCodeSnippet` (@ `code/renderers/react/src/componentManifest/generateCodeSnippet.ts`) -> Impact: **918.5** | LOC: 569
- `describe` (@ `code/core/src/docs-tools/argTypes/jsdocParser.test.ts`) -> Impact: **781.7** | LOC: 358
- `describe` (@ `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts`) -> Impact: **670.8** | LOC: 598
- `matcherFunction` (@ `code/lib/create-storybook/src/services/ProjectTypeService.ts`) -> Impact: **665.5** | LOC: 349
- `describe` (@ `code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.test.ts`) -> Impact: **633.9** | LOC: 726

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `onDismiss` (@ `code/addons/onboarding/src/features/IntentSurvey/IntentSurvey.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `code/core/src/common/js-package-manager/PNPMProxy.test.ts`) -> **O(2^N) [Recursive]**
- `accept` (@ `code/core/src/manager/components/sidebar/ChecklistWidget.tsx`) -> **O(2^N) [Recursive]**
- `accept` (@ `code/core/src/manager/settings/Checklist/Checklist.tsx`) -> **O(2^N) [Recursive]**
- `ImportDeclaration` (@ `code/frameworks/nextjs/src/babel/plugins/react-loadable-plugin.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `code/core/src/common/js-package-manager/Yarn1Proxy.test.ts`) -> **O(2^N) [Recursive]**
- `useList` (@ `code/core/src/components/components/Tabs/Tabs.hooks.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `code/core/src/csf-tools/getStorySortParameter.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `code/core/src/docs-tools/argTypes/convert/convert.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `code/core/src/shared/universal-store/index.test.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `code/addons/vitest/src/updateVitestFile.config.3.2.test.ts`) -> DB Complexity: **381**
- `describe` (@ `code/addons/vitest/src/updateVitestFile.config.test.ts`) -> DB Complexity: **381**
- `describe` (@ `code/addons/vitest/src/updateVitestFile.config.4.test.ts`) -> DB Complexity: **363**
- `describe` (@ `code/core/src/manager-api/tests/refs.test.ts`) -> DB Complexity: **332**
- `describe` (@ `code/core/src/csf-tools/ConfigFile.test.ts`) -> DB Complexity: **258**
- `describe` (@ `code/core/src/node-logger/wrap-utils.test.ts`) -> DB Complexity: **176**
- `describe` (@ `code/core/src/preview-api/modules/store/autoTitle.test.ts`) -> DB Complexity: **135**
- `constructor` (@ `code/core/src/instrumenter/instrumenter.ts`) -> DB Complexity: **118**
- `setFieldNode` (@ `code/core/src/csf-tools/ConfigFile.ts`) -> DB Complexity: **113**
- `describe` (@ `code/core/src/common/presets.test.ts`) -> DB Complexity: **106**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 16 | 5229.1 | 0.62% | 0.0% |
| `code/core/src/manager-api/tests` | 18 | 784.24 | 19.62% | 0.0% |
| `code/core/src/csf-tools` | 13 | 599.55 | 19.16% | 4.51% |
| `code/renderers/react/src/componentManifest/componentMeta` | 14 | 500.39 | 27.31% | 0.0% |
| `scripts` | 26 | 459.48 | 26.11% | 42.1% |
| `code/lib/cli-storybook/src/automigrate/fixes` | 42 | 424.68 | 32.36% | 3.4% |
| `code/core/src/preview-api/modules/preview-web` | 17 | 420.9 | 39.81% | 9.68% |
| `code/lib/eslint-plugin/src/rules` | 32 | 420.49 | 7.88% | 1.21% |
| `code/core/src/manager/components/sidebar` | 63 | 405.42 | 13.05% | 28.02% |
| `code/addons/vitest/src` | 21 | 404.23 | 10.02% | 18.6% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `code/.storybook/utils/todo.tsx` -> **100.0%** Exposure
- `code/addons/links/scripts/fix-preview-api-reference.ts` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/stories/CSSAtRules.stories.tsx` -> **100.0%** Exposure
- `code/core/src/components/components/Form/Field.stories.tsx` -> **100.0%** Exposure
- `code/core/src/components/components/Form/Input.stories.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `code/addons/a11y/src/postinstall.ts` -> **100.0%** Exposure
- `code/addons/a11y/src/typings.d.ts` -> **100.0%** Exposure
- `code/addons/links/src/react/components/link.tsx` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/preview/splitSelectors.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/components/TestStatusIcon.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/core/src/components/components/Select/Select.stories.tsx` -> **0** Orphaned Functions | **61** Duplicates
- `code/core/src/server-errors.ts` -> **0** Orphaned Functions | **45** Duplicates
- `code/renderers/react/src/componentManifest/generateCodeSnippet.test.tsx` -> **0** Orphaned Functions | **37** Duplicates
- `code/core/src/components/components/Modal/Modal.stories.tsx` -> **0** Orphaned Functions | **35** Duplicates
- `code/renderers/react/src/componentManifest/getComponentImports.test.ts` -> **0** Orphaned Functions | **31** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`code/lib/cli-storybook/src/automigrate/fixes/addon-globals-api.ts`** -> AI Confidence: **99.39%**
2. **`code/lib/cli-storybook/src/codemod/helpers/config-to-csf-factory.ts`** -> AI Confidence: **99.34%**
3. **`code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts`** -> AI Confidence: **99.34%**
4. **`code/addons/a11y/src/a11yRunner.ts`** -> AI Confidence: **99.31%**
5. **`code/addons/a11y/src/components/A11YPanel.tsx`** -> AI Confidence: **99.31%**
6. **`code/addons/a11y/src/preview.tsx`** -> AI Confidence: **99.31%**
7. **`code/addons/vitest/src/components/Description.tsx`** -> AI Confidence: **99.31%**
8. **`code/addons/vitest/src/components/GlobalErrorModal.tsx`** -> AI Confidence: **99.31%**
9. **`code/addons/vitest/src/components/TestProviderRender.tsx`** -> AI Confidence: **99.31%**
10. **`code/addons/vitest/src/node/vitest-manager.ts`** -> AI Confidence: **99.31%**
11. **`code/addons/vitest/src/postinstall.ts`** -> AI Confidence: **99.31%**
12. **`code/addons/vitest/src/vitest-plugin/index.ts`** -> AI Confidence: **99.31%**
13. **`code/builders/builder-vite/src/plugins/vite-mock/plugin.ts`** -> AI Confidence: **99.31%**
14. **`code/builders/builder-webpack5/src/preview/iframe-webpack.config.ts`** -> AI Confidence: **99.31%**
15. **`code/core/src/channels/postmessage/index.ts`** -> AI Confidence: **99.31%**
16. **`code/core/src/cli/AddonVitestService.ts`** -> AI Confidence: **99.31%**
17. **`code/core/src/cli/eslintPlugin.ts`** -> AI Confidence: **99.31%**
18. **`code/core/src/common/js-package-manager/JsPackageManagerFactory.ts`** -> AI Confidence: **99.31%**
19. **`code/core/src/common/utils/get-storybook-info.ts`** -> AI Confidence: **99.31%**
20. **`code/core/src/component-testing/components/Interaction.tsx`** -> AI Confidence: **99.31%**
21. **`code/core/src/components/components/Modal/Modal.tsx`** -> AI Confidence: **99.31%**
22. **`code/core/src/components/components/Select/Select.tsx`** -> AI Confidence: **99.31%**
23. **`code/core/src/components/components/Tabs/TabsView.tsx`** -> AI Confidence: **99.31%**
24. **`code/core/src/components/components/tooltip/WithTooltip.tsx`** -> AI Confidence: **99.31%**
25. **`code/core/src/core-server/build-dev.ts`** -> AI Confidence: **99.31%**
26. **`code/core/src/core-server/change-detection/ChangeDetectionService.ts`** -> AI Confidence: **99.31%**
27. **`code/core/src/core-server/utils/StoryIndexGenerator.ts`** -> AI Confidence: **99.31%**
28. **`code/core/src/core-server/utils/manifests/manifests.ts`** -> AI Confidence: **99.31%**
29. **`code/core/src/core-server/utils/save-story/save-story.ts`** -> AI Confidence: **99.31%**
30. **`code/core/src/csf-tools/ConfigFile.ts`** -> AI Confidence: **99.31%**
31. **`code/core/src/csf-tools/CsfFile.ts`** -> AI Confidence: **99.31%**
32. **`code/core/src/csf-tools/vitest-plugin/transformer.ts`** -> AI Confidence: **99.31%**
33. **`code/core/src/instrumenter/instrumenter.ts`** -> AI Confidence: **99.31%**
34. **`code/core/src/manager-api/modules/layout.ts`** -> AI Confidence: **99.31%**
35. **`code/core/src/manager/components/preview/Viewport.tsx`** -> AI Confidence: **99.31%**
36. **`code/core/src/manager/components/sidebar/FileSearchList.tsx`** -> AI Confidence: **99.31%**
37. **`code/core/src/manager/components/sidebar/TestingWidget.tsx`** -> AI Confidence: **99.31%**
38. **`code/core/src/manager/components/sidebar/useHighlighted.ts`** -> AI Confidence: **99.31%**
39. **`code/core/src/manager/settings/Checklist/Checklist.tsx`** -> AI Confidence: **99.31%**
40. **`code/core/src/preview-api/modules/preview-web/WebView.ts`** -> AI Confidence: **99.31%**
41. **`code/core/src/preview-api/modules/preview-web/render/MdxDocsRender.ts`** -> AI Confidence: **99.31%**
42. **`code/core/src/preview-api/modules/store/csf/prepareStory.ts`** -> AI Confidence: **99.31%**
43. **`code/core/src/telemetry/storybook-metadata.ts`** -> AI Confidence: **99.31%**
44. **`code/core/src/theming/convert.ts`** -> AI Confidence: **99.31%**
45. **`code/core/src/toolbar/components/ToolbarMenuSelect.tsx`** -> AI Confidence: **99.31%**
46. **`code/core/src/types/modules/core-common.ts`** -> AI Confidence: **99.31%**
47. **`code/frameworks/angular/src/server/framework-preset-angular-cli.ts`** -> AI Confidence: **99.31%**
48. **`code/frameworks/nextjs/src/babel/preset.ts`** -> AI Confidence: **99.31%**
49. **`code/frameworks/nextjs/src/preview.tsx`** -> AI Confidence: **99.31%**
50. **`code/frameworks/nextjs/src/swc/loader.ts`** -> AI Confidence: **99.31%**
51. **`code/lib/cli-storybook/src/add.ts`** -> AI Confidence: **99.31%**
52. **`code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.ts`** -> AI Confidence: **99.31%**
53. **`code/lib/cli-storybook/src/automigrate/fixes/fix-faux-esm-require.ts`** -> AI Confidence: **99.31%**
54. **`code/lib/cli-storybook/src/automigrate/index.ts`** -> AI Confidence: **99.31%**
55. **`code/lib/cli-storybook/src/codemod/csf-factories.ts`** -> AI Confidence: **99.31%**
56. **`code/lib/cli-storybook/src/codemod/helpers/story-to-csf-factory.ts`** -> AI Confidence: **99.31%**
57. **`code/lib/cli-storybook/src/sandbox.ts`** -> AI Confidence: **99.31%**
58. **`code/lib/cli-storybook/src/upgrade.ts`** -> AI Confidence: **99.31%**
59. **`code/lib/codemod/src/index.ts`** -> AI Confidence: **99.31%**
60. **`code/lib/codemod/src/transforms/csf-2-to-3.ts`** -> AI Confidence: **99.31%**
61. **`code/lib/create-storybook/src/bin/run.ts`** -> AI Confidence: **99.31%**
62. **`code/lib/create-storybook/src/generators/ANGULAR/index.ts`** -> AI Confidence: **99.31%**
63. **`code/lib/create-storybook/src/services/ProjectTypeService.ts`** -> AI Confidence: **99.31%**
64. **`code/presets/create-react-app/src/index.ts`** -> AI Confidence: **99.31%**
65. **`code/presets/react-webpack/src/loaders/react-docgen-loader.ts`** -> AI Confidence: **99.31%**
66. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaManager.ts`** -> AI Confidence: **99.31%**
67. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.ts`** -> AI Confidence: **99.31%**
68. **`code/renderers/react/src/componentManifest/getComponentImports.ts`** -> AI Confidence: **99.31%**
69. **`scripts/build-package.ts`** -> AI Confidence: **99.31%**
70. **`code/core/src/components/components/ErrorFormatter/ErrorFormatter.stories.tsx`** -> AI Confidence: **99.29%**
71. **`code/core/src/core-server/utils/__search-files-tests__/src/commonjs-module.js`** -> AI Confidence: **99.29%**
72. **`scripts/eslint-plugin-local-rules/no-duplicated-error-codes.js`** -> AI Confidence: **99.29%**
73. **`code/addons/a11y/src/manager.tsx`** -> AI Confidence: **99.24%**
74. **`code/addons/vitest/src/node/test-manager.ts`** -> AI Confidence: **99.24%**
75. **`code/core/src/backgrounds/components/Tool.tsx`** -> AI Confidence: **99.24%**
76. **`code/core/src/bin/core.ts`** -> AI Confidence: **99.24%**
77. **`code/core/src/builder-manager/utils/managerEntries.ts`** -> AI Confidence: **99.24%**
78. **`code/core/src/cli/helpers.ts`** -> AI Confidence: **99.24%**
79. **`code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts`** -> AI Confidence: **99.24%**
80. **`code/core/src/common/js-package-manager/PNPMProxy.ts`** -> AI Confidence: **99.24%**
81. **`code/core/src/common/js-package-manager/Yarn1Proxy.ts`** -> AI Confidence: **99.24%**
82. **`code/core/src/common/js-package-manager/Yarn2Proxy.ts`** -> AI Confidence: **99.24%**
83. **`code/core/src/common/presets.ts`** -> AI Confidence: **99.24%**
84. **`code/core/src/component-testing/components/InteractionsPanel.tsx`** -> AI Confidence: **99.24%**
85. **`code/core/src/controls/components/ControlsPanel.tsx`** -> AI Confidence: **99.24%**
86. **`code/core/src/core-server/build-static.ts`** -> AI Confidence: **99.24%**
87. **`code/core/src/core-server/utils/doTelemetry.ts`** -> AI Confidence: **99.24%**
88. **`code/core/src/core-server/utils/generate-story.ts`** -> AI Confidence: **99.24%**
89. **`code/core/src/core-server/utils/server-statics.ts`** -> AI Confidence: **99.24%**
90. **`code/core/src/csf/core-annotations.ts`** -> AI Confidence: **99.24%**
91. **`code/core/src/manager-api/lib/stories.ts`** -> AI Confidence: **99.24%**
92. **`code/core/src/manager-api/modules/stories.ts`** -> AI Confidence: **99.24%**
93. **`code/core/src/manager/components/layout/Layout.tsx`** -> AI Confidence: **99.24%**
94. **`code/core/src/manager/components/mobile/navigation/MobileNavigation.tsx`** -> AI Confidence: **99.24%**
95. **`code/core/src/manager/components/sidebar/Refs.tsx`** -> AI Confidence: **99.24%**
96. **`code/core/src/manager/components/sidebar/Search.tsx`** -> AI Confidence: **99.24%**
97. **`code/core/src/mocking-utils/extract.ts`** -> AI Confidence: **99.24%**
98. **`code/core/src/preview-api/modules/preview-web/PreviewWithSelection.tsx`** -> AI Confidence: **99.24%**
99. **`code/core/src/preview-api/modules/store/csf/portable-stories.ts`** -> AI Confidence: **99.24%**
100. **`code/frameworks/angular/src/builders/build-storybook/index.ts`** -> AI Confidence: **99.24%**
101. **`code/frameworks/angular/src/client/angular-beta/AbstractRenderer.ts`** -> AI Confidence: **99.24%**
102. **`code/lib/cli-storybook/src/automigrate/codemod.ts`** -> AI Confidence: **99.24%**
103. **`code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-parameters.ts`** -> AI Confidence: **99.24%**
104. **`code/lib/cli-storybook/src/automigrate/fixes/addon-globals-api.test.ts`** -> AI Confidence: **99.24%**
105. **`code/lib/cli-storybook/src/bin/run.ts`** -> AI Confidence: **99.24%**
106. **`code/lib/cli-storybook/src/doctor/index.ts`** -> AI Confidence: **99.24%**
107. **`code/lib/create-storybook/src/commands/UserPreferencesCommand.ts`** -> AI Confidence: **99.24%**
108. **`code/lib/create-storybook/src/generators/NEXTJS/index.ts`** -> AI Confidence: **99.24%**
109. **`code/lib/eslint-plugin/scripts/generate-rule.ts`** -> AI Confidence: **99.24%**
110. **`code/lib/eslint-plugin/src/rules/no-uninstalled-addons.ts`** -> AI Confidence: **99.24%**
111. **`code/renderers/react/src/componentManifest/generator.ts`** -> AI Confidence: **99.24%**
112. **`code/renderers/svelte/src/render.ts`** -> AI Confidence: **99.24%**
113. **`scripts/check-package.ts`** -> AI Confidence: **99.24%**
114. **`scripts/sandbox/generate.ts`** -> AI Confidence: **99.24%**
115. **`code/core/src/components/components/Modal/Modal.styled.tsx`** -> AI Confidence: **99.23%**
116. **`code/core/src/core-server/utils/checklist.ts`** -> AI Confidence: **99.23%**
117. **`code/core/src/core-server/utils/open-browser/opener.ts`** -> AI Confidence: **99.23%**
118. **`code/core/src/csf/csf-factories.ts`** -> AI Confidence: **99.23%**
119. **`code/core/src/manager/components/sidebar/Filter.tsx`** -> AI Confidence: **99.23%**
120. **`code/core/src/preview-api/modules/preview-web/render/StoryRender.ts`** -> AI Confidence: **99.23%**
121. **`code/frameworks/angular/src/client/angular-beta/utils/PropertyExtractor.ts`** -> AI Confidence: **99.23%**
122. **`code/lib/cli-storybook/src/automigrate/fixes/wrap-getAbsolutePath.ts`** -> AI Confidence: **99.23%**
123. **`code/lib/cli-storybook/src/automigrate/helpers/mainConfigFile.ts`** -> AI Confidence: **99.23%**
124. **`code/lib/cli-storybook/src/automigrate/multi-project.ts`** -> AI Confidence: **99.23%**
125. **`scripts/create-nx-sandbox-projects.ts`** -> AI Confidence: **99.2%**
126. **`code/addons/a11y/src/components/Tabs.tsx`** -> AI Confidence: **99.18%**
127. **`code/addons/a11y/src/components/VisionSimulator.tsx`** -> AI Confidence: **99.18%**
128. **`code/addons/vitest/src/components/GlobalErrorModal.stories.tsx`** -> AI Confidence: **99.18%**
129. **`code/addons/vitest/src/node/boot-test-runner.ts`** -> AI Confidence: **99.18%**
130. **`code/addons/vitest/src/updateVitestFile.config.3.2.test.ts`** -> AI Confidence: **99.18%**
131. **`code/addons/vitest/src/updateVitestFile.config.test.ts`** -> AI Confidence: **99.18%**
132. **`code/addons/vitest/src/updateVitestFile.config.workspace.test.ts`** -> AI Confidence: **99.18%**
133. **`code/builders/builder-vite/src/codegen-modern-iframe-script.test.ts`** -> AI Confidence: **99.18%**
134. **`code/builders/builder-vite/src/index.ts`** -> AI Confidence: **99.18%**
135. **`code/builders/builder-vite/src/plugins/code-generator-plugin.ts`** -> AI Confidence: **99.18%**
136. **`code/core/scripts/generate-source-files.ts`** -> AI Confidence: **99.18%**
137. **`code/core/src/cli/AddonVitestService.test.ts`** -> AI Confidence: **99.18%**
138. **`code/core/src/cli/dirs.ts`** -> AI Confidence: **99.18%**
139. **`code/core/src/common/utils/load-main-config.ts`** -> AI Confidence: **99.18%**
140. **`code/core/src/component-testing/components/Toolbar.tsx`** -> AI Confidence: **99.18%**
141. **`code/core/src/components/components/Tabs/TabList.tsx`** -> AI Confidence: **99.18%**
142. **`code/core/src/components/components/Tabs/Tabs.stories.tsx`** -> AI Confidence: **99.18%**
143. **`code/core/src/components/components/Tabs/Tabs.tsx`** -> AI Confidence: **99.18%**
144. **`code/core/src/components/components/syntaxhighlighter/syntaxhighlighter.tsx`** -> AI Confidence: **99.18%**
145. **`code/core/src/core-server/presets/common-preset.ts`** -> AI Confidence: **99.18%**
146. **`code/core/src/core-server/server-channel/create-new-story-channel.test.ts`** -> AI Confidence: **99.18%**
147. **`code/core/src/core-server/server-channel/file-search-channel.test.ts`** -> AI Confidence: **99.18%**
148. **`code/core/src/core-server/utils/watch-story-specifiers.ts`** -> AI Confidence: **99.18%**
149. **`code/core/src/csf-tools/ConfigFile.test.ts`** -> AI Confidence: **99.18%**
150. **`code/core/src/csf-tools/vitest-plugin/transformer.test.ts`** -> AI Confidence: **99.18%**
151. **`code/core/src/manager/components/notifications/NotificationItem.tsx`** -> AI Confidence: **99.18%**
152. **`code/core/src/manager/components/panel/Panel.stories.tsx`** -> AI Confidence: **99.18%**
153. **`code/core/src/manager/components/preview/Toolbar.tsx`** -> AI Confidence: **99.18%**
154. **`code/core/src/manager/components/sidebar/Filter.stories.tsx`** -> AI Confidence: **99.18%**
155. **`code/core/src/manager/components/sidebar/Menu.tsx`** -> AI Confidence: **99.18%**
156. **`code/core/src/manager/components/sidebar/useExpanded.ts`** -> AI Confidence: **99.18%**
157. **`code/core/src/manager/container/Preview.tsx`** -> AI Confidence: **99.18%**
158. **`code/core/src/manager/settings/index.tsx`** -> AI Confidence: **99.18%**
159. **`code/core/src/node-logger/index.ts`** -> AI Confidence: **99.18%**
160. **`code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts`** -> AI Confidence: **99.18%**
161. **`code/core/src/shared/status-store/index.ts`** -> AI Confidence: **99.18%**
162. **`code/core/src/test/testing-library.ts`** -> AI Confidence: **99.18%**
163. **`code/core/src/types/modules/addons.ts`** -> AI Confidence: **99.18%**
164. **`code/frameworks/nextjs-vite/src/portable-stories.ts`** -> AI Confidence: **99.18%**
165. **`code/frameworks/nextjs/src/portable-stories.ts`** -> AI Confidence: **99.18%**
166. **`code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.test.ts`** -> AI Confidence: **99.18%**
167. **`code/lib/cli-storybook/src/automigrate/fixes/migrate-addon-console.test.ts`** -> AI Confidence: **99.18%**
168. **`code/lib/cli-storybook/src/codemod/helpers/config-to-csf-factory.test.ts`** -> AI Confidence: **99.18%**
169. **`code/lib/create-storybook/src/commands/GeneratorExecutionCommand.ts`** -> AI Confidence: **99.18%**
170. **`code/lib/create-storybook/src/generators/REACT_NATIVE/index.ts`** -> AI Confidence: **99.18%**
171. **`code/renderers/react/src/__test__/portable-stories-legacy.test.tsx`** -> AI Confidence: **99.18%**
172. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaManager.test.ts`** -> AI Confidence: **99.18%**
173. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.storyExtraction.test.ts`** -> AI Confidence: **99.18%**
174. **`code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts`** -> AI Confidence: **99.18%**
175. **`code/renderers/react/src/componentManifest/fixtures.ts`** -> AI Confidence: **99.18%**
176. **`code/renderers/react/src/componentManifest/getComponentImports.test.ts`** -> AI Confidence: **99.18%**
177. **`code/renderers/react/src/enrichCsf.test.ts`** -> AI Confidence: **99.18%**
178. **`code/renderers/react/src/extractArgTypes.test.ts`** -> AI Confidence: **99.18%**
179. **`code/renderers/react/src/portable-stories.tsx`** -> AI Confidence: **99.18%**
180. **`code/renderers/svelte/src/__test__/composeStories/portable-stories.test.ts`** -> AI Confidence: **99.18%**
181. **`code/renderers/vue3/src/__tests__/composeStories/portable-stories.test.ts`** -> AI Confidence: **99.18%**
182. **`code/renderers/vue3/src/preview.ts`** -> AI Confidence: **99.18%**
183. **`code/renderers/web-components/src/preview.ts`** -> AI Confidence: **99.18%**
184. **`code/renderers/web-components/src/render.ts`** -> AI Confidence: **99.18%**
185. **`scripts/sandbox/publish.ts`** -> AI Confidence: **99.18%**
186. **`scripts/tasks/build.ts`** -> AI Confidence: **99.18%**
187. **`scripts/tasks/dev.ts`** -> AI Confidence: **99.18%**
188. **`scripts/tasks/serve.ts`** -> AI Confidence: **99.18%**
189. **`code/addons/pseudo-states/src/preview/splitSelectors.ts`** -> AI Confidence: **99.17%**
190. **`code/addons/vitest/src/vitest-plugin/types.ts`** -> AI Confidence: **99.17%**
191. **`code/core/src/controls/types.ts`** -> AI Confidence: **99.17%**
192. **`code/core/src/shared/utils/toHaveLiveRegion.ts`** -> AI Confidence: **99.17%**
193. **`code/frameworks/react-vite/src/plugins/react-docgen.ts`** -> AI Confidence: **99.17%**
194. **`code/lib/cli-storybook/src/autoblock/block-webpack5-frameworks.ts`** -> AI Confidence: **99.17%**
195. **`scripts/dangerfile.js`** -> AI Confidence: **99.17%**
196. **`code/addons/a11y/src/components/A11yContext.tsx`** -> AI Confidence: **99.16%**
197. **`code/addons/onboarding/src/Onboarding.tsx`** -> AI Confidence: **99.16%**
198. **`code/addons/vitest/src/preset.ts`** -> AI Confidence: **99.16%**
199. **`code/builders/builder-vite/src/plugins/storybook-external-globals-plugin.ts`** -> AI Confidence: **99.16%**
200. **`code/builders/builder-webpack5/src/index.ts`** -> AI Confidence: **99.16%**
201. **`code/builders/builder-webpack5/src/presets/custom-webpack-preset.ts`** -> AI Confidence: **99.16%**
202. **`code/core/src/bin/loader.ts`** -> AI Confidence: **99.16%**
203. **`code/core/src/common/js-package-manager/BUNProxy.ts`** -> AI Confidence: **99.16%**
204. **`code/core/src/common/js-package-manager/NPMProxy.ts`** -> AI Confidence: **99.16%**
205. **`code/core/src/component-testing/components/Panel.tsx`** -> AI Confidence: **99.16%**
206. **`code/core/src/controls/manager.tsx`** -> AI Confidence: **99.16%**
207. **`code/core/src/core-server/utils/get-new-story-file.ts`** -> AI Confidence: **99.16%**
208. **`code/core/src/docs-tools/argTypes/docgen/createPropDef.ts`** -> AI Confidence: **99.16%**
209. **`code/core/src/manager/components/preview/Preview.tsx`** -> AI Confidence: **99.16%**
210. **`code/core/src/manager/components/sidebar/SearchResults.tsx`** -> AI Confidence: **99.16%**
211. **`code/core/src/manager/components/sidebar/Sidebar.tsx`** -> AI Confidence: **99.16%**
212. **`code/core/src/manager/components/sidebar/Tree.tsx`** -> AI Confidence: **99.16%**
213. **`code/core/src/preview-api/modules/preview-web/Preview.tsx`** -> AI Confidence: **99.16%**
214. **`code/core/src/preview-api/modules/store/StoryStore.ts`** -> AI Confidence: **99.16%**
215. **`code/core/src/shared/checklist-store/checklistData.tsx`** -> AI Confidence: **99.16%**
216. **`code/core/src/telemetry/telemetry.ts`** -> AI Confidence: **99.16%**
217. **`code/core/src/types/modules/api.ts`** -> AI Confidence: **99.16%**
218. **`code/frameworks/angular/src/builders/start-storybook/index.ts`** -> AI Confidence: **99.16%**
219. **`code/frameworks/nextjs/src/utils.ts`** -> AI Confidence: **99.16%**
220. **`code/lib/cli-storybook/src/automigrate/fixes/addon-storysource-code-panel.ts`** -> AI Confidence: **99.16%**
221. **`code/lib/cli-storybook/src/util.ts`** -> AI Confidence: **99.16%**
222. **`code/lib/create-storybook/src/generators/baseGenerator.ts`** -> AI Confidence: **99.16%**
223. **`code/lib/create-storybook/src/initiate.ts`** -> AI Confidence: **99.16%**
224. **`code/renderers/react/src/componentManifest/generator.test.ts`** -> AI Confidence: **99.16%**
225. **`code/renderers/react/src/componentManifest/reactDocgen.ts`** -> AI Confidence: **99.16%**
226. **`code/renderers/react/src/preset.ts`** -> AI Confidence: **99.16%**
227. **`scripts/bench/bench-packages.ts`** -> AI Confidence: **99.16%**
228. **`scripts/ci/main.ts`** -> AI Confidence: **99.16%**
229. **`scripts/run-registry.ts`** -> AI Confidence: **99.16%**
230. **`scripts/snippets/codemod.ts`** -> AI Confidence: **99.16%**
231. **`scripts/task.ts`** -> AI Confidence: **99.16%**
232. **`scripts/tasks/sandbox-parts.ts`** -> AI Confidence: **99.16%**
233. **`code/addons/onboarding/src/manager.tsx`** -> AI Confidence: **99.15%**
234. **`code/builders/builder-vite/src/build.ts`** -> AI Confidence: **99.15%**
235. **`code/builders/builder-vite/src/codegen-project-annotations.ts`** -> AI Confidence: **99.15%**
236. **`code/builders/builder-vite/src/plugins/storybook-optimize-deps-plugin.ts`** -> AI Confidence: **99.15%**
237. **`code/core/src/actions/containers/ActionLogger/index.tsx`** -> AI Confidence: **99.15%**
238. **`code/core/src/actions/runtime/action.ts`** -> AI Confidence: **99.15%**
239. **`code/core/src/common/utils/get-storybook-refs.ts`** -> AI Confidence: **99.15%**
240. **`code/core/src/common/utils/normalize-stories.ts`** -> AI Confidence: **99.15%**
241. **`code/core/src/common/utils/sync-main-preview-addons.ts`** -> AI Confidence: **99.15%**
242. **`code/core/src/common/utils/validate-configuration-files.ts`** -> AI Confidence: **99.15%**
243. **`code/core/src/component-testing/components/PanelTitle.tsx`** -> AI Confidence: **99.15%**
244. **`code/core/src/component-testing/manager.tsx`** -> AI Confidence: **99.15%**
245. **`code/core/src/components/components/Button/Button.tsx`** -> AI Confidence: **99.15%**
246. **`code/core/src/components/components/Tabs/TabPanel.stories.tsx`** -> AI Confidence: **99.15%**
247. **`code/core/src/components/components/Tabs/TabPanel.tsx`** -> AI Confidence: **99.15%**
248. **`code/core/src/components/components/Tabs/Tabs.hooks.tsx`** -> AI Confidence: **99.15%**
249. **`code/core/src/core-server/change-detection/GitDiffProvider.test.ts`** -> AI Confidence: **99.15%**
250. **`code/core/src/core-server/load.ts`** -> AI Confidence: **99.15%**
251. **`code/core/src/core-server/server-channel/file-search-channel.ts`** -> AI Confidence: **99.15%**
252. **`code/core/src/core-server/utils/get-server-channel.ts`** -> AI Confidence: **99.15%**
253. **`code/core/src/core-server/utils/whats-new.ts`** -> AI Confidence: **99.15%**
254. **`code/core/src/manager/components/TourGuide/TourGuide.tsx`** -> AI Confidence: **99.15%**
255. **`code/core/src/manager/components/preview/tools/zoom.tsx`** -> AI Confidence: **99.15%**
256. **`code/core/src/manager/components/sidebar/ChecklistWidget.tsx`** -> AI Confidence: **99.15%**
257. **`code/core/src/manager/components/sidebar/CreateNewStoryFileModal.tsx`** -> AI Confidence: **99.15%**
258. **`code/core/src/manager/components/sidebar/Filter.story-helpers.tsx`** -> AI Confidence: **99.15%**
259. **`code/core/src/manager/components/sidebar/FilterPanel.tsx`** -> AI Confidence: **99.15%**
260. **`code/core/src/manager/components/sidebar/RefBlocks.tsx`** -> AI Confidence: **99.15%**
261. **`code/core/src/manager/components/sidebar/SidebarBottom.tsx`** -> AI Confidence: **99.15%**
262. **`code/core/src/manager/components/sidebar/StatusButton.tsx`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `code/addons/vitest/src/node/vitest-manager.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/updateVitestFile.config.3.2.test.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/updateVitestFile.config.4.test.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/updateVitestFile.config.test.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/updateVitestFile.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `code/core/src/core-server/utils/server-address.ts` -> **100.0%** Exposure
- `code/core/src/core-server/utils/server-init.ts` -> **100.0%** Exposure
- `code/core/src/preview-api/Errors.stories.tsx` -> **100.0%** Exposure
- `code/lib/cli-storybook/src/postinstallAddon.ts` -> **100.0%** Exposure
- `code/lib/eslint-plugin/scripts/generate-rule.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `code/addons/a11y/src/components/A11yContext.tsx` -> **100.0%** Exposure
- `code/addons/vitest/src/node/test-manager.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/node/vitest-manager.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/postinstall.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/preset.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6178` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `code/core/src/preview-api/modules/preview-web/render/StoryRender.ts` (TYPESCRIPT) -> Cumulative Risk: **897.9**
- **Archetype:** `file_cluster_4` (Distance: 13.753 IQR)
- **Magnitude:** 66.84 | **LOC:** 497 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `mount` (Impact: 21.4), `checkIfAborted` (Impact: 9.6), `rerender` (Impact: 7.3)

### 2. `code/core/src/manager/components/sidebar/Filter.stories.tsx` (TYPESCRIPT) -> Cumulative Risk: **894.77**
- **Archetype:** `file_cluster_17` (Distance: 11.912 IQR)
- **Magnitude:** 25.2 | **LOC:** 413 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `createInitialState` (Impact: 117.3), `getDefaultTagFilters` (Impact: 13.8), `expect` (Impact: 5.9)

### 3. `code/core/src/core-server/utils/get-server-channel.ts` (TYPESCRIPT) -> Cumulative Risk: **881.85**
- **Archetype:** `file_cluster_13` (Distance: 13.049 IQR)
- **Magnitude:** 9.99 | **LOC:** 115 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 51.3), `send` (Impact: 3.8), `getServerChannel` (Impact: 2.2)

### 4. `code/addons/vitest/src/node/vitest-manager.ts` (TYPESCRIPT) -> Cumulative Risk: **844.6**
- **Archetype:** `file_cluster_4` (Distance: 13.531 IQR)
- **Magnitude:** 51.62 | **LOC:** 594 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `runAffectedTestsAfterChange` (Impact: 65.4), `filterTestSpecifications` (Impact: 65.2), `runTests` (Impact: 56.4)

### 5. `code/e2e-tests/util.ts` (TYPESCRIPT) -> Cumulative Risk: **820.16**
- **Archetype:** `file_cluster_4` (Distance: 12.407 IQR)
- **Magnitude:** 66.9 | **LOC:** 302 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `navigateToStory` (Impact: 21.6), `waitForStoryLoaded` (Impact: 14.0), `deepLinkToStory` (Impact: 11.7)

### 6. `code/core/src/preview-api/modules/preview-web/WebView.ts` (TYPESCRIPT) -> Cumulative Risk: **815.94**
- **Archetype:** `file_cluster_13` (Distance: 12.313 IQR)
- **Magnitude:** 17.73 | **LOC:** 209 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (98.9723%)
- **Heaviest Functions:** `constructor` (Impact: 17.9), `showMode` (Impact: 8.3), `checkIfLayoutExists` (Impact: 7.2)

### 7. `code/core/src/csf/csf-factories.ts` (TYPESCRIPT) -> Cumulative Risk: **807.06**
- **Archetype:** `file_cluster_2` (Distance: 13.472 IQR)
- **Magnitude:** 48.36 | **LOC:** 286 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `defineStory` (Impact: 289.1), `composed` (Impact: 21.3), `isStory` (Impact: 12.4)

### 8. `code/core/src/manager/components/panel/Panel.stories.tsx` (TYPESCRIPT) -> Cumulative Risk: **803.05**
- **Archetype:** `file_cluster_13` (Distance: 9.699 IQR)
- **Magnitude:** 8.51 | **LOC:** 156 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `JSXTitles` (Impact: 56.9), `Default` (Impact: 2.3), `NoPanels` (Impact: 1.9)

### 9. `code/frameworks/angular/src/client/angular-beta/utils/PropertyExtractor.ts` (TYPESCRIPT) -> Cumulative Risk: **800.61**
- **Archetype:** `file_cluster_4` (Distance: 12.024 IQR)
- **Magnitude:** 23.36 | **LOC:** 219 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `analyzeDecorators` (Impact: 37.3), `analyzeRestricted` (Impact: 37.2), `analyzeMetadata` (Impact: 27.9)

### 10. `code/core/src/common/utils/file-cache.ts` (TYPESCRIPT) -> Cumulative Risk: **790.84**
- **Archetype:** `file_cluster_4` (Distance: 13.709 IQR)
- **Magnitude:** 31.23 | **LOC:** 163 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setMany` (Impact: 7.1), `setManySync` (Impact: 7.1), `getAll` (Impact: 6.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.883 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.59 IQR)
- **Top Global Matches:** file_cluster_8: 10.883, file_cluster_1: 11.214, file_cluster_4: 11.223
- **Magnitude:** 275.69 | **LOC:** 4120 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (84.2801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1096.6 | O(2^N) | DB: 44)
  * `describe` (Impact: 464.5 | O(2^N) | DB: 58)
  * `describe` (Impact: 91.7 | O(2^N))
  * `describe` (Impact: 90.8 | O(N^4))
  * `describe` (Impact: 41.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 731`, `args: 564`, `func_start: 489`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 26`, `duplicate_logic: 18`
* *Architecture:* `io: 38`, `api: 1`, `concurrency: 659`, `import: 12`
* *Defense:* `safety: 26`, `doc: 2`, `test: 463`, `immutability_locks: 171`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` PreviewWeb.mockdata.ts, core-events, index.ts, index.ts, WebView.ts, PreviewWeb.tsx, types, vitest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager-api/tests/url.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.077 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.669 IQR)
- **Top Global Matches:** file_cluster_8: 11.077, file_cluster_1: 11.441, file_cluster_13: 11.441
- **Magnitude:** 236.14 | **LOC:** 567 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (40.3057%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 91.8 | O(N^2) | DB: 76)
  * `describe` (Impact: 40.8 | O(2^N) | DB: 4)
  * `describe` (Impact: 8.2 | O(N^2) | DB: 7)
  * `describe` (Impact: 7.7 | O(N^2) | DB: 7)
  * `storyState` (Impact: 2.0 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 70`, `args: 63`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 58`, `duplicate_logic: 4`
* *Architecture:* `io: 24`, `concurrency: 18`, `import: 5`
* *Defense:* `test: 99`, `immutability_locks: 74`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` events, core-events, url, vitest, global
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager-api/tests/shortcuts.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.159 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 4.953 IQR)
- **Top Global Matches:** file_cluster_4: 10.159, file_cluster_8: 10.401, file_cluster_7: 11.135
- **Magnitude:** 235.68 | **LOC:** 292 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 22.3 | O(N^2) | DB: 15)
  * `createMockStore` (Impact: 4.0 | O(N^1) | DB: 2)
  * `action` (Impact: 1.9 | O(N^1))
  * `action` (Impact: 1.9 | O(N^1))
  * `action` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 20`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 172`, `import: 2`
* *Defense:* `safety: 2`, `test: 43`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, shortcuts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager-api/tests/versions.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.422 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.299 IQR)
- **Top Global Matches:** file_cluster_8: 9.422, file_cluster_4: 9.649, file_cluster_7: 10.167
- **Magnitude:** 162.78 | **LOC:** 362 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (74.5278%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 70.9 | O(2^N) | DB: 41)
  * `createMockStore` (Impact: 3.5 | O(N^2) | DB: 2)
  * `setVersions` (Impact: 2.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 57`, `args: 33`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `io: 12`, `concurrency: 73`, `import: 3`
* *Defense:* `test: 54`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` versions, vitest, global
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/vitest-plugin/transformer.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.059 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.295 IQR)
- **Top Global Matches:** file_cluster_8: 10.059, file_cluster_13: 10.259, file_cluster_0: 10.604
- **Magnitude:** 157.23 | **LOC:** 1388 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.9996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1331.2 | O(2^N))
  * `transform` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 390`, `args: 173`, `func_start: 146`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 138`, `concurrency: 77`, `import: 92`
* *Defense:* `safety: 32`, `test: 101`, `immutability_locks: 259`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Button, test-utils, common, transformer.ts, Button.stories, vitest, preview, tags.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/ConfigFile.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.358 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.57 IQR)
- **Top Global Matches:** file_cluster_8: 10.358, file_cluster_13: 10.662, file_cluster_0: 10.862
- **Magnitude:** 155.6 | **LOC:** 1928 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 258
- **Risk Profile:** Cognitive Load (3.7816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 1186.8 | O(2^N) | DB: 258)
  * `describe` (Impact: 47.8 | O(N^3) | DB: 15)
  * `describe` (Impact: 21.6 | O(N^2))
  * `it` (Impact: 11.3 | O(N^2) | DB: 12)
  * `removeField` (Impact: 3.7 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 547`, `args: 302`, `func_start: 365`
* *Risk/State:* `safety_bypasses: 7`, `planned_debt: 4`, `duplicate_logic: 3`
* *Architecture:* `io: 104`, `api: 243`, `concurrency: 1`, `import: 78`
* *Defense:* `safety: 31`, `test: 292`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` react-vite, fs, path, vitest, ts-dedent, another-file, react-webpack5, ConfigFile.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MIGRATION.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 147.8 | **LOC:** 7390 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/CsfFile.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.974 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.112 IQR)
- **Top Global Matches:** file_cluster_8: 9.974, file_cluster_7: 10.64, file_cluster_13: 10.641
- **Magnitude:** 141.72 | **LOC:** 3155 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (3.1866%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 631.9 | O(2^N) | DB: 4)
  * `describe` (Impact: 348.7 | O(2^N) | DB: 18)
  * `describe` (Impact: 29.6 | O(N^3))
  * `describe` (Impact: 25.1 | O(N^3))
  * `describe` (Impact: 13.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 564`, `args: 308`, `func_start: 406`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 11`
* *Architecture:* `io: 9`, `api: 238`, `concurrency: 5`, `import: 51`
* *Defense:* `safety: 21`, `test: 235`, `immutability_locks: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` B, #bar.mock, Check, bad-preview, react, Button, node-logger, ts-dedent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.202 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.2 IQR)
- **Top Global Matches:** file_cluster_8: 10.202, file_cluster_7: 10.645, file_cluster_13: 10.684
- **Magnitude:** 141.55 | **LOC:** 1728 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (28.9502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveLiteralValue` (Impact: 1191.7 | O(2^N) | DB: 3)
  * `unwrapToFunction` (Impact: 137.0 | O(2^N))
  * `resolvePropsFromComponentType` (Impact: 22.9 | O(N^2))
    * *Intent:* // --------------------------------------------------------------------------- // Constants // -----...
  * `isWrappedExpression` (Impact: 12.7 | O(N^1))
    * *Intent:* // ---------------------------------------------------------------------------
  * `getSymbolContextNode` (Impact: 8.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 74`, `args: 26`, `func_start: 23`
* *Risk/State:* `state_mutation: 9`, `dead_code: 3`
* *Architecture:* `api: 8`, `import: 3`
* *Defense:* `safety: 15`, `doc: 13`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Button, types.ts, ..., ..., utils.ts, typescript, m
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `code/lib/eslint-plugin/src/rules/await-interactions.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.209 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.169 IQR)
- **Top Global Matches:** file_cluster_8: 8.209, file_cluster_4: 9.044, file_cluster_7: 9.173
- **Magnitude:** 123.05 | **LOC:** 812 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.7662%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 181`, `args: 88`, `func_start: 108`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 24`, `concurrency: 139`, `import: 12`
* *Defense:* `safety: 6`, `doc: 1`, `test: 23`, `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jest, testing-library, await-interactions.ts, test-utils.ts, ts-dedent, test, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/CsfFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.545 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.995 IQR)
- **Top Global Matches:** file_cluster_17: 12.545, file_cluster_11: 12.613, file_cluster_13: 12.77
- **Magnitude:** 122.47 | **LOC:** 1113 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (61.4333%), Tech Debt (47.6978%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 602.8 | O(N^6) | DB: 57)
  * `_parseMeta` (Impact: 102.5 | O(N^4) | DB: 10)
  * `isArgsStory` (Impact: 43.6 | O(N^2) | DB: 1)
  * `hasMount` (Impact: 40.2 | O(N^3))
  * `getStoryExport` (Impact: 39.2 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 141`, `args: 69`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 132`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 23`, `api: 32`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 92`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` findVarInitialization.ts, tags.ts, types, ts-dedent, babel, promises, csf, path-to-component...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.823 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.061 IQR)
- **Top Global Matches:** file_cluster_8: 10.823, file_cluster_17: 11.037, file_cluster_13: 11.041
- **Magnitude:** 120.11 | **LOC:** 541 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (30.9556%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `appendToExistingProjectRefs` (Impact: 1022.2 | O(2^N) | DB: 10)
  * `mergeProperties` (Impact: 79.6 | O(2^N) | DB: 2)
  * `getTemplatePath` (Impact: 22.7 | O(N^1))
    * *Intent:* /**
  * `resolveTestPropValue` (Impact: 7.4 | O(N^1))
  * `loadTemplate` (Impact: 4.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 115`, `args: 40`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`
* *Architecture:* `api: 5`, `concurrency: 13`, `import: 9`
* *Defense:* `safety: 6`, `doc: 8`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` babel, vitest.workspace.template.ts?raw, vitest.config.4.template.ts?raw, vitest.config.3.2.template.ts?raw, pathe, vitest.config.template.ts?raw
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/ConfigFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.434 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.824 IQR)
- **Top Global Matches:** file_cluster_17: 12.434, file_cluster_8: 12.599, file_cluster_11: 12.605
- **Magnitude:** 117.88 | **LOC:** 1203 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 113
- **Risk Profile:** Cognitive Load (71.923%), Tech Debt (10.9201%)
**Top Internal Functions/Classes:**
  * `setFieldNode` (Impact: 525.0 | O(2^N) | DB: 113)
  * `parse` (Impact: 185.0 | O(N^5) | DB: 3)
  * `_getPathProperties` (Impact: 32.2 | O(2^N) | DB: 9)
  * `_findVarDeclarator` (Impact: 24.9 | O(N^2) | DB: 2)
  * `_updateExportNode` (Impact: 24.8 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 147`, `args: 90`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 237`, `dead_code: 4`, `fragile_debt: 2`
* *Architecture:* `io: 44`, `api: 12`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 9`, `doc: 16`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foo, ts-dedent, babel, promises, bar, PrintResultType.ts, baz, node-logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/dangerfile.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.523 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.56 IQR)
- **Top Global Matches:** file_cluster_8: 10.523, file_cluster_7: 11.036, file_cluster_13: 11.129
- **Magnitude:** 107.38 | **LOC:** 195 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^2) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (7.7385%), Tech Debt (85.3656%)
**Top Internal Functions/Classes:**
  * `checkRequiredLabels` (Impact: 56.9 | O(N^2) | DB: 8)
  * `checkManualTestingSection` (Impact: 19.5 | O(N^1))
  * `checkTargetBranch` (Impact: 18.5 | O(N^1))
    * *Intent:* // Extract content after the manual testing section
  * `checkPrTitle` (Impact: 4.2 | O(N^1))
  * `checkTargetBranch` (Impact: 3.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 14`, `args: 9`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 2`
* *Architecture:* `import: 2`
* *Defense:* `safety: 16`, `doc: 12`, `test: 1`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` package.json, danger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/generateCodeSnippet.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.064 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.488 IQR)
- **Top Global Matches:** file_cluster_8: 10.064, file_cluster_17: 10.312, file_cluster_7: 10.634
- **Magnitude:** 95.53 | **LOC:** 651 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (23.9343%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCodeSnippet` (Impact: 918.5 | O(N^4) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 114`, `args: 64`, `func_start: 26`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 5`, `api: 4`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 13`, `doc: 6`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` csf-tools, utils.ts, babel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/frameworks/angular/src/server/angular-cli-webpack.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.094 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 6.785 IQR)
- **Top Global Matches:** file_cluster_13: 10.094, file_cluster_8: 10.314, file_cluster_0: 10.362
- **Magnitude:** 90.98 | **LOC:** 212 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (7.1264%), Tech Debt (47.0273%)
**Top Internal Functions/Classes:**
  * `getCustomStylesConfig` (Impact: 82.2 | O(N^5) | DB: 9)
    * *Intent:* /** * Extract webpack config from angular-cli 13.x.x ⚠️ This file is in JavaScript to not use * Type...
  * `getWebpackConfig` (Impact: 1.1 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 23`, `args: 9`, `func_start: 4`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 7`, `doc: 8`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` storybook-normalize-angular-entry-plugin, filter-out-styling-rules, configs, tsconfig-paths-webpack-plugin, promises, webpack-browser-config, node:module
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/core-server/utils/StoryIndexGenerator.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.146 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.382 IQR)
- **Top Global Matches:** file_cluster_17: 13.146, file_cluster_4: 13.257, file_cluster_13: 13.259
- **Magnitude:** 80.54 | **LOC:** 909 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (90.6794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractDocs` (Impact: 171.0 | O(N^4) | DB: 16)
  * `extractStories` (Impact: 158.1 | O(N^3) | DB: 24)
  * `chooseDuplicate` (Impact: 102.8 | O(N^2) | DB: 2)
  * `invalidate` (Impact: 33.7 | O(N^3) | DB: 13)
  * `getProjectTags` (Impact: 29.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 132`, `args: 61`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 171`
* *Architecture:* `io: 12`, `api: 10`, `concurrency: 56`, `import: 24`
* *Defense:* `safety: 55`, `doc: 6`, `immutability_locks: 71`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` csf-tools, sortStories.ts, types, tiny-invariant, slash, autoTitle.ts, node-logger, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/docs-tools/argTypes/jsdocParser.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.019 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.758 IQR)
- **Top Global Matches:** file_cluster_0: 15.019, file_cluster_8: 15.337, file_cluster_15: 15.466
- **Magnitude:** 78.7 | **LOC:** 363 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.7918%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 781.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 107`, `args: 151`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `import: 2`
* *Defense:* `safety: 155`, `doc: 68`, `test: 149`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, jsdocParser.ts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/create-storybook/src/services/ProjectTypeService.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.61 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.034 IQR)
- **Top Global Matches:** file_cluster_17: 12.61, file_cluster_4: 12.69, file_cluster_13: 12.864
- **Magnitude:** 77.19 | **LOC:** 378 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (77.242%), Tech Debt (8.7525%)
**Top Internal Functions/Classes:**
  * `matcherFunction` (Impact: 665.5 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 101`, `args: 53`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 41`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 58`, `import: 12`
* *Defense:* `safety: 48`, `doc: 5`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` node:path, common, server-errors, types, ts-dedent, node:fs, semver, find...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/instrumenter/instrumenter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.616 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.651 IQR)
- **Top Global Matches:** file_cluster_17: 13.616, file_cluster_11: 13.842, file_cluster_13: 13.936
- **Magnitude:** 75.55 | **LOC:** 842 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 118
- **Risk Profile:** Cognitive Load (94.3302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 433.0 | O(N^4) | DB: 118)
  * `isInstrumentable` (Impact: 10.8 | O(N^1))
  * `construct` (Impact: 6.3 | O(N^1))
  * `getRetainedState` (Impact: 5.7 | O(N^1))
  * `getInitialState` (Impact: 2.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 119`, `args: 72`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 259`, `dead_code: 2`
* *Architecture:* `io: 7`, `api: 3`, `concurrency: 25`, `import: 10`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 61`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.178
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types.ts, core-events, types, channels, error, EVENTS.ts, global, typings.d.ts...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `code/lib/cli-storybook/src/upgrade.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.187 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_8: 10.187, file_cluster_17: 10.38, file_cluster_13: 10.396
- **Magnitude:** 75.21 | **LOC:** 538 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (22.8639%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `upgrade` (Impact: 550.9 | O(2^N) | DB: 10)
  * `getUpgradeResults` (Impact: 52.6 | O(N^3) | DB: 3)
  * `logUpgradeResults` (Impact: 51.1 | O(N^2) | DB: 3)
    * *Intent:* /** Logs the results of the upgrade process, including project categorization and diagnostic message...
  * `checkVersionConsistency` (Impact: 17.5 | O(N^2) | DB: 1)
  * `getStorybookVersion` (Impact: 8.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 87`, `args: 38`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 27`, `import: 16`
* *Defense:* `safety: 13`, `doc: 1`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` common, server-errors, cross-spawn, picocolors, utils.ts, ts-dedent, index.ts, types.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/mocking-utils/esmWalker.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.708 IQR)
- **Top Global Matches:** file_cluster_17: 11.97, file_cluster_13: 12.298, file_cluster_11: 12.301
- **Magnitude:** 73.34 | **LOC:** 344 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (58.7304%), Tech Debt (71.2814%)
**Top Internal Functions/Classes:**
  * `eswalk` (Impact: 494.6 | O(2^N) | DB: 8)
  * `handlePattern` (Impact: 74.0 | O(2^N))
  * `isRefIdentifier` (Impact: 42.9 | O(N^1))
    * *Intent:* // emit the identifier events in BFS so the hoisted declarations
  * `isStaticProperty` (Impact: 22.1 | O(N^2))
  * `setScope` (Impact: 7.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 105`, `args: 40`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 34`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `safety: 20`, `doc: 5`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` estree-walker, ) 
        onImportMeta?.(node, estree
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.288 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.587 IQR)
- **Top Global Matches:** file_cluster_8: 11.288, file_cluster_13: 11.298, file_cluster_16: 11.301
- **Magnitude:** 73.12 | **LOC:** 605 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.239%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 670.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 183`, `args: 79`, `func_start: 51`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 11`
* *Architecture:* `api: 22`, `concurrency: 28`, `import: 20`
* *Defense:* `safety: 34`, `doc: 28`, `test: 36`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Button, index, react, componentMetaExtractor.test-helpers.ts, vitest, ts-dedent, override
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/create-storybook/src/bin/run.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.353 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.603 IQR)
- **Top Global Matches:** file_cluster_8: 8.353, file_cluster_13: 8.803, file_cluster_7: 9.207
- **Magnitude:** 72.73 | **LOC:** 129 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.982%), Tech Debt (11.1784%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 25`, `args: 6`, `func_start: 2`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 3`, `concurrency: 5`, `import: 9`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` common, types, initiate.ts, telemetry, commander, cli, types.ts, package.json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `code/renderers/preact/src/preset.ts` (TYPESCRIPT) | Magnitude: 2.53 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, immutability_locks: 5, api: 4
- `code/frameworks/sveltekit/src/preview.ts` (TYPESCRIPT) | Magnitude: 4.59 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 12, structural_boundaries: 11, safety: 10
- `code/lib/create-storybook/src/generators/ANGULAR/index.ts` (TYPESCRIPT) | Magnitude: 10.2 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 112, branch: 33, structural_boundaries: 22, immutability_locks: 17
- `code/core/src/core-server/presets/common-override-preset.ts` (TYPESCRIPT) | Magnitude: 9.35 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, branch: 18, structural_boundaries: 18, safety: 10
- `code/builders/builder-webpack5/src/plugins/webpack-mock-plugin.ts` (TYPESCRIPT) | Magnitude: 23.29 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 56, branch: 35, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `code/core/src/test/preview.ts` (TYPESCRIPT) | Magnitude: 20.94 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, branch: 44, structural_boundaries: 30, func_start: 17
- `code/core/src/client-logger/index.ts` (TYPESCRIPT) | Magnitude: 9.13 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 25, state_mutation: 21, safety_bypasses: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `code/addons/pseudo-states/src/stories/Button.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, ui_framework: 2, args: 1
- `code/addons/pseudo-states/src/stories/CSSAtRules.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, ui_framework: 2, args: 1
- `code/lib/create-storybook/src/commands/PreflightCheckCommand.ts` (TYPESCRIPT) | Magnitude: 9.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 47, concurrency: 22, structural_boundaries: 18, branch: 8
- `code/builders/builder-webpack5/templates/virtualModuleModernEntry.js` (JAVASCRIPT) | Magnitude: 8.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 16, branch: 6, import: 6
- `code/core/src/actions/decorator.ts` (TYPESCRIPT) | Magnitude: 4.81 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 27, args: 13, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `code/frameworks/angular/src/client/angular-beta/utils/StoryUID.ts` (TYPESCRIPT) | Magnitude: 2.97 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 9, doc: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `code/renderers/react/src/componentManifest/__testfixtures__/DtsComponent.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, generics: 2, indent_spaces: 2, branch: 1
- `code/renderers/html/src/public-types.ts` (TYPESCRIPT) | Magnitude: 2.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, generics: 14, ui_framework: 13, api: 9
- `code/renderers/server/src/public-types.ts` (TYPESCRIPT) | Magnitude: 2.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, generics: 14, ui_framework: 13, api: 9
- `code/renderers/web-components/src/public-types.ts` (TYPESCRIPT) | Magnitude: 2.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, generics: 14, ui_framework: 13, api: 9
- `code/core/src/preview-api/modules/store/csf/stepRunners.ts` (TYPESCRIPT) | Magnitude: 1.06 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 8, args: 6, concurrency: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `code/addons/themes/src/decorators/class-name.decorator.tsx` (TYPESCRIPT) | Magnitude: 3.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 18, immutability_locks: 9, branch: 8
- `code/core/src/preview-api/modules/store/csf/processCSFFile.ts` (TYPESCRIPT) | Magnitude: 5.31 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 22, immutability_locks: 16, args: 15
- `code/core/src/core-server/utils/IndexingError.ts` (TYPESCRIPT) | Magnitude: 8.11 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 50, indent_spaces: 38, structural_boundaries: 13, args: 8
- `code/lib/codemod/src/transforms/upgrade-hierarchy-separators.js` (JAVASCRIPT) | Magnitude: 25.24 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, args: 9, comprehensions: 9
- `code/core/src/preview-api/modules/store/csf/composeConfigs.ts` (TYPESCRIPT) | Magnitude: 3.59 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 25, branch: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `code/core/src/manager/components/sidebar/useDynamicFavicon.ts` (TYPESCRIPT) | Magnitude: 7.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, branch: 16, structural_boundaries: 14, args: 10
- `code/core/src/components/components/Tabs/StatelessTabList.tsx` (TYPESCRIPT) | Magnitude: 2.8 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, immutability_locks: 28, structural_boundaries: 24, ui_framework: 24
- `code/core/src/csf/csf-factories.ts` (TYPESCRIPT) | Magnitude: 48.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 84, generics: 66, branch: 64
- `code/renderers/react/template/stories/decorators.stories.tsx` (TYPESCRIPT) | Magnitude: 2.33 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 24, args: 10, ui_framework: 9
- `code/lib/cli-storybook/src/automigrate/types.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 34, branch: 28, generics: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `code/core/src/preview-api/modules/preview-web/render/CsfDocsRender.ts` (TYPESCRIPT) | Magnitude: 19.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 76, concurrency: 41, structural_boundaries: 40
- `code/addons/links/src/react/components/link.tsx` (TYPESCRIPT) | Magnitude: 7.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 22, structural_boundaries: 19, branch: 18
- `code/frameworks/nextjs-vite/template/stories/RSC.tsx` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, api: 2
- `code/frameworks/nextjs/src/config/webpack.ts` (TYPESCRIPT) | Magnitude: 5.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 18, branch: 16, concurrency: 12
- `code/frameworks/nextjs/template/stories/RSC.tsx` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `code/renderers/preact/template/components/Pre.jsx` (JAVASCRIPT) | Magnitude: 2.2 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, indent_spaces: 3, structural_boundaries: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `code/core/template/stories/loader-enhancements.stories.ts` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, immutability_locks: 3, api: 2
- `code/core/src/node-logger/logger/console.ts` (TYPESCRIPT) | Magnitude: 11.3 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 35, args: 23, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `code/frameworks/nextjs-vite/template/stories/DynamicImport.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1
- `code/frameworks/nextjs/template/stories/dynamic-component.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1
- `code/frameworks/sveltekit/static/MockProvider.svelte` (HTML) | Magnitude: 6.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, safety: 10, branch: 9, structural_boundaries: 9
- `code/core/src/common/js-package-manager/types.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 2, api: 2
- `code/core/template/stories/shortcuts.stories.ts` (TYPESCRIPT) | Magnitude: 0.75 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, concurrency: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `code/frameworks/nextjs-vite/template/next-env.d.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1
- `code/frameworks/nextjs/template/next-env.d.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `code/core/src/manager/components/preview/tools/zoom.tsx` -> Churn: **69.13%** | Cog Load: 10.0421% | Debt: 93.0993%
- `code/core/src/types/modules/core-common.ts` -> Churn: **68.37%** | Cog Load: 45.5009% | Debt: 99.9628%
- `code/renderers/react/src/componentManifest/getComponentImports.ts` -> Churn: **66.78%** | Cog Load: 32.5145% | Debt: 82.1148%
- `scripts/utils/yarn.ts` -> Churn: **63.16%** | Cog Load: 54.4013% | Debt: 25.9086%
- `code/core/src/manager-api/modules/stories.ts` -> Churn: **59.96%** | Cog Load: 9.1112% | Debt: 99.0364%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 275.69
- `code/core/src/manager-api/tests/shortcuts.test.js` -> **Gert Hengeveld** (100.0% isolated ownership) | Magnitude: 235.68
- `code/core/src/csf-tools/CsfFile.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 141.72
- `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 141.55
- `code/lib/eslint-plugin/src/rules/await-interactions.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 123.05

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/core/src/shared/universal-store/mock.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `code/core/src/components/components/typography/lib/common.tsx` -> **Severity: 3870.907** (Blast Radius: 45.047 * Doc Risk: 85.9304%)
- `code/addons/vitest/src/node/vitest.ts` -> **Severity: 1930.246** (Blast Radius: 63.363 * Doc Risk: 30.4633%)
- `code/core/src/highlight/icons.ts` -> **Severity: 1435.962** (Blast Radius: 15.319 * Doc Risk: 93.7373%)
- `scripts/ecosystem-ci/test.sh` -> **Severity: 885.281** (Blast Radius: 33.198 * Doc Risk: 26.6667%)
- `code/core/src/common/utils/cli.ts` -> **Severity: 634.7** (Blast Radius: 6.347 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
