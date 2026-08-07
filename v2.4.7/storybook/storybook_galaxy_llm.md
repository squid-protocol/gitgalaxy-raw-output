# ARCHITECTURAL_BRIEF: storybook
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/storybook` |
| **Timestamp** | `2026-08-07T04:17:53.464727+00:00` |
| **Scan Duration** | `10.83s` |
| **Git Branch** | `next` |
| **Git Commit** | `ce8c743b04264c5e8010df1181c828171a04c33a` |
| **Git Remote** | `https://github.com/storybookjs/storybook.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2629 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.144`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1750 | 56.4% |
| file_cluster_13 | 829 | 26.7% |
| file_cluster_4 | 131 | 4.2% |
| file_cluster_16 | 51 | 1.6% |
| file_cluster_17 | 50 | 1.6% |
| file_cluster_2 | 47 | 1.5% |
| file_cluster_0 | 47 | 1.5% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 17.4 | 6.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 24.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.8 | 0.8 | 0.0 |
| API Exposure | 0.0 | 19.4 | 4.9 | 5.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 94.2 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.7 | 0.3 | 0.1 | 0.1 |
| Volatility Exposure | 0.0 | 80.3 | 11.6 | 14.4 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.5 | 28.9 | 0.0 |
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

- `getCodeSnippet` (@ `code/renderers/react/src/componentManifest/generateCodeSnippet.ts`) -> Impact: **384.4** | LOC: 569
- `getRenderPath` (@ `code/renderers/react/src/componentManifest/generateCodeSnippet.ts`) -> Impact: **380.6** | LOC: 502
- `describe` (@ `code/core/src/csf-tools/vitest-plugin/transformer.test.ts`) -> Impact: **319.7** | LOC: 1337
- `resolveLiteralValue` (@ `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts`) -> Impact: **312.9** | LOC: 400
- `describe` (@ `code/core/src/csf-tools/ConfigFile.test.ts`) -> Impact: **306.9** | LOC: 1739
- `describe` (@ `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts`) -> Impact: **279.1** | LOC: 1494
- `describe` (@ `code/core/src/docs-tools/argTypes/jsdocParser.test.ts`) -> Impact: **272.5** | LOC: 358
- `describe` (@ `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts`) -> Impact: **244.4** | LOC: 1494
- `matcherFunction` (@ `code/lib/create-storybook/src/services/ProjectTypeService.ts`) -> Impact: **233.4** | LOC: 349
- `describe` (@ `code/core/src/csf-tools/CsfFile.test.ts`) -> Impact: **231.8** | LOC: 1968

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 16 | 5229.1 | 0.62% | 0.0% |
| `code/core/src/manager-api/tests` | 18 | 1190.69 | 22.24% | 0.0% |
| `code/core/src/csf-tools` | 13 | 589.06 | 19.07% | 15.23% |
| `code/core/src/preview-api/modules/preview-web` | 17 | 519.82 | 36.6% | 16.87% |
| `code/renderers/react/src/componentManifest/componentMeta` | 14 | 470.0 | 28.26% | 10.23% |
| `code/lib/eslint-plugin/src/rules` | 32 | 435.45 | 7.81% | 15.66% |
| `code/lib/cli-storybook/src/automigrate/fixes` | 42 | 420.46 | 34.14% | 4.71% |
| `scripts` | 26 | 391.5 | 27.36% | 49.35% |
| `code/core/src/core-server/utils` | 51 | 372.04 | 34.27% | 15.04% |
| `code/renderers/react/src/componentManifest` | 16 | 349.67 | 19.12% | 15.48% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `code/.storybook/utils/todo.tsx` -> **100.0%** Exposure
- `code/addons/links/scripts/fix-preview-api-reference.ts` -> **100.0%** Exposure
- `code/addons/onboarding/src/preset.ts` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/stories/CSSAtRules.stories.tsx` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/types.test-d.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `code/addons/a11y/src/postinstall.ts` -> **100.0%** Exposure
- `code/addons/a11y/src/typings.d.ts` -> **100.0%** Exposure
- `code/addons/links/src/react/components/link.tsx` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/preview/splitSelectors.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/components/TestStatusIcon.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` -> **0** Orphaned Functions | **321** Duplicates
- `code/core/src/csf-tools/ConfigFile.test.ts` -> **0** Orphaned Functions | **163** Duplicates
- `code/core/src/preview-api/modules/preview-web/parseArgsParam.test.ts` -> **0** Orphaned Functions | **145** Duplicates
- `code/core/src/instrumenter/instrumenter.test.ts` -> **3** Orphaned Functions | **140** Duplicates
- `code/core/src/preview-api/modules/store/hooks.test.ts` -> **0** Orphaned Functions | **120** Duplicates

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
73. **`scripts/ecosystem-ci/build.sh`** -> AI Confidence: **99.29%**
74. **`code/addons/a11y/src/manager.tsx`** -> AI Confidence: **99.24%**
75. **`code/addons/vitest/src/node/test-manager.ts`** -> AI Confidence: **99.24%**
76. **`code/core/src/backgrounds/components/Tool.tsx`** -> AI Confidence: **99.24%**
77. **`code/core/src/bin/core.ts`** -> AI Confidence: **99.24%**
78. **`code/core/src/builder-manager/utils/managerEntries.ts`** -> AI Confidence: **99.24%**
79. **`code/core/src/cli/helpers.ts`** -> AI Confidence: **99.24%**
80. **`code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts`** -> AI Confidence: **99.24%**
81. **`code/core/src/common/js-package-manager/PNPMProxy.ts`** -> AI Confidence: **99.24%**
82. **`code/core/src/common/js-package-manager/Yarn1Proxy.ts`** -> AI Confidence: **99.24%**
83. **`code/core/src/common/js-package-manager/Yarn2Proxy.ts`** -> AI Confidence: **99.24%**
84. **`code/core/src/common/presets.ts`** -> AI Confidence: **99.24%**
85. **`code/core/src/component-testing/components/InteractionsPanel.tsx`** -> AI Confidence: **99.24%**
86. **`code/core/src/controls/components/ControlsPanel.tsx`** -> AI Confidence: **99.24%**
87. **`code/core/src/core-server/build-static.ts`** -> AI Confidence: **99.24%**
88. **`code/core/src/core-server/utils/doTelemetry.ts`** -> AI Confidence: **99.24%**
89. **`code/core/src/core-server/utils/generate-story.ts`** -> AI Confidence: **99.24%**
90. **`code/core/src/core-server/utils/server-statics.ts`** -> AI Confidence: **99.24%**
91. **`code/core/src/csf/core-annotations.ts`** -> AI Confidence: **99.24%**
92. **`code/core/src/manager-api/lib/stories.ts`** -> AI Confidence: **99.24%**
93. **`code/core/src/manager-api/modules/stories.ts`** -> AI Confidence: **99.24%**
94. **`code/core/src/manager/components/layout/Layout.tsx`** -> AI Confidence: **99.24%**
95. **`code/core/src/manager/components/mobile/navigation/MobileNavigation.tsx`** -> AI Confidence: **99.24%**
96. **`code/core/src/manager/components/sidebar/Refs.tsx`** -> AI Confidence: **99.24%**
97. **`code/core/src/manager/components/sidebar/Search.tsx`** -> AI Confidence: **99.24%**
98. **`code/core/src/mocking-utils/extract.ts`** -> AI Confidence: **99.24%**
99. **`code/core/src/preview-api/modules/preview-web/PreviewWithSelection.tsx`** -> AI Confidence: **99.24%**
100. **`code/core/src/preview-api/modules/store/csf/portable-stories.ts`** -> AI Confidence: **99.24%**
101. **`code/frameworks/angular/src/builders/build-storybook/index.ts`** -> AI Confidence: **99.24%**
102. **`code/frameworks/angular/src/client/angular-beta/AbstractRenderer.ts`** -> AI Confidence: **99.24%**
103. **`code/lib/cli-storybook/src/automigrate/codemod.ts`** -> AI Confidence: **99.24%**
104. **`code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-parameters.ts`** -> AI Confidence: **99.24%**
105. **`code/lib/cli-storybook/src/automigrate/fixes/addon-globals-api.test.ts`** -> AI Confidence: **99.24%**
106. **`code/lib/cli-storybook/src/bin/run.ts`** -> AI Confidence: **99.24%**
107. **`code/lib/cli-storybook/src/doctor/index.ts`** -> AI Confidence: **99.24%**
108. **`code/lib/create-storybook/src/commands/UserPreferencesCommand.ts`** -> AI Confidence: **99.24%**
109. **`code/lib/create-storybook/src/generators/NEXTJS/index.ts`** -> AI Confidence: **99.24%**
110. **`code/lib/eslint-plugin/scripts/generate-rule.ts`** -> AI Confidence: **99.24%**
111. **`code/lib/eslint-plugin/src/rules/no-uninstalled-addons.ts`** -> AI Confidence: **99.24%**
112. **`code/renderers/react/src/componentManifest/generator.ts`** -> AI Confidence: **99.24%**
113. **`code/renderers/svelte/src/render.ts`** -> AI Confidence: **99.24%**
114. **`scripts/check-package.ts`** -> AI Confidence: **99.24%**
115. **`scripts/sandbox/generate.ts`** -> AI Confidence: **99.24%**
116. **`code/core/src/components/components/Modal/Modal.styled.tsx`** -> AI Confidence: **99.23%**
117. **`code/core/src/core-server/utils/checklist.ts`** -> AI Confidence: **99.23%**
118. **`code/core/src/core-server/utils/open-browser/opener.ts`** -> AI Confidence: **99.23%**
119. **`code/core/src/csf/csf-factories.ts`** -> AI Confidence: **99.23%**
120. **`code/core/src/manager/components/sidebar/Filter.tsx`** -> AI Confidence: **99.23%**
121. **`code/core/src/preview-api/modules/preview-web/render/StoryRender.ts`** -> AI Confidence: **99.23%**
122. **`code/frameworks/angular/src/client/angular-beta/utils/PropertyExtractor.ts`** -> AI Confidence: **99.23%**
123. **`code/lib/cli-storybook/src/automigrate/fixes/wrap-getAbsolutePath.ts`** -> AI Confidence: **99.23%**
124. **`code/lib/cli-storybook/src/automigrate/helpers/mainConfigFile.ts`** -> AI Confidence: **99.23%**
125. **`code/lib/cli-storybook/src/automigrate/multi-project.ts`** -> AI Confidence: **99.23%**
126. **`scripts/create-nx-sandbox-projects.ts`** -> AI Confidence: **99.2%**
127. **`code/addons/a11y/src/components/Tabs.tsx`** -> AI Confidence: **99.18%**
128. **`code/addons/a11y/src/components/VisionSimulator.tsx`** -> AI Confidence: **99.18%**
129. **`code/addons/vitest/src/components/GlobalErrorModal.stories.tsx`** -> AI Confidence: **99.18%**
130. **`code/addons/vitest/src/node/boot-test-runner.ts`** -> AI Confidence: **99.18%**
131. **`code/addons/vitest/src/updateVitestFile.config.3.2.test.ts`** -> AI Confidence: **99.18%**
132. **`code/addons/vitest/src/updateVitestFile.config.test.ts`** -> AI Confidence: **99.18%**
133. **`code/addons/vitest/src/updateVitestFile.config.workspace.test.ts`** -> AI Confidence: **99.18%**
134. **`code/builders/builder-vite/src/codegen-modern-iframe-script.test.ts`** -> AI Confidence: **99.18%**
135. **`code/builders/builder-vite/src/index.ts`** -> AI Confidence: **99.18%**
136. **`code/builders/builder-vite/src/plugins/code-generator-plugin.ts`** -> AI Confidence: **99.18%**
137. **`code/core/scripts/generate-source-files.ts`** -> AI Confidence: **99.18%**
138. **`code/core/src/cli/AddonVitestService.test.ts`** -> AI Confidence: **99.18%**
139. **`code/core/src/cli/dirs.ts`** -> AI Confidence: **99.18%**
140. **`code/core/src/common/utils/load-main-config.ts`** -> AI Confidence: **99.18%**
141. **`code/core/src/component-testing/components/Toolbar.tsx`** -> AI Confidence: **99.18%**
142. **`code/core/src/components/components/Tabs/TabList.tsx`** -> AI Confidence: **99.18%**
143. **`code/core/src/components/components/Tabs/Tabs.stories.tsx`** -> AI Confidence: **99.18%**
144. **`code/core/src/components/components/Tabs/Tabs.tsx`** -> AI Confidence: **99.18%**
145. **`code/core/src/components/components/syntaxhighlighter/syntaxhighlighter.tsx`** -> AI Confidence: **99.18%**
146. **`code/core/src/core-server/presets/common-preset.ts`** -> AI Confidence: **99.18%**
147. **`code/core/src/core-server/server-channel/create-new-story-channel.test.ts`** -> AI Confidence: **99.18%**
148. **`code/core/src/core-server/server-channel/file-search-channel.test.ts`** -> AI Confidence: **99.18%**
149. **`code/core/src/core-server/utils/watch-story-specifiers.ts`** -> AI Confidence: **99.18%**
150. **`code/core/src/csf-tools/ConfigFile.test.ts`** -> AI Confidence: **99.18%**
151. **`code/core/src/csf-tools/vitest-plugin/transformer.test.ts`** -> AI Confidence: **99.18%**
152. **`code/core/src/manager/components/notifications/NotificationItem.tsx`** -> AI Confidence: **99.18%**
153. **`code/core/src/manager/components/panel/Panel.stories.tsx`** -> AI Confidence: **99.18%**
154. **`code/core/src/manager/components/preview/Toolbar.tsx`** -> AI Confidence: **99.18%**
155. **`code/core/src/manager/components/sidebar/Filter.stories.tsx`** -> AI Confidence: **99.18%**
156. **`code/core/src/manager/components/sidebar/Menu.tsx`** -> AI Confidence: **99.18%**
157. **`code/core/src/manager/components/sidebar/useExpanded.ts`** -> AI Confidence: **99.18%**
158. **`code/core/src/manager/container/Preview.tsx`** -> AI Confidence: **99.18%**
159. **`code/core/src/manager/settings/index.tsx`** -> AI Confidence: **99.18%**
160. **`code/core/src/node-logger/index.ts`** -> AI Confidence: **99.18%**
161. **`code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts`** -> AI Confidence: **99.18%**
162. **`code/core/src/shared/status-store/index.ts`** -> AI Confidence: **99.18%**
163. **`code/core/src/test/testing-library.ts`** -> AI Confidence: **99.18%**
164. **`code/core/src/types/modules/addons.ts`** -> AI Confidence: **99.18%**
165. **`code/frameworks/nextjs-vite/src/portable-stories.ts`** -> AI Confidence: **99.18%**
166. **`code/frameworks/nextjs/src/portable-stories.ts`** -> AI Confidence: **99.18%**
167. **`code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.test.ts`** -> AI Confidence: **99.18%**
168. **`code/lib/cli-storybook/src/automigrate/fixes/migrate-addon-console.test.ts`** -> AI Confidence: **99.18%**
169. **`code/lib/cli-storybook/src/codemod/helpers/config-to-csf-factory.test.ts`** -> AI Confidence: **99.18%**
170. **`code/lib/create-storybook/src/commands/GeneratorExecutionCommand.ts`** -> AI Confidence: **99.18%**
171. **`code/lib/create-storybook/src/generators/REACT_NATIVE/index.ts`** -> AI Confidence: **99.18%**
172. **`code/renderers/react/src/__test__/portable-stories-legacy.test.tsx`** -> AI Confidence: **99.18%**
173. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaManager.test.ts`** -> AI Confidence: **99.18%**
174. **`code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.storyExtraction.test.ts`** -> AI Confidence: **99.18%**
175. **`code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts`** -> AI Confidence: **99.18%**
176. **`code/renderers/react/src/componentManifest/fixtures.ts`** -> AI Confidence: **99.18%**
177. **`code/renderers/react/src/componentManifest/getComponentImports.test.ts`** -> AI Confidence: **99.18%**
178. **`code/renderers/react/src/enrichCsf.test.ts`** -> AI Confidence: **99.18%**
179. **`code/renderers/react/src/extractArgTypes.test.ts`** -> AI Confidence: **99.18%**
180. **`code/renderers/react/src/portable-stories.tsx`** -> AI Confidence: **99.18%**
181. **`code/renderers/svelte/src/__test__/composeStories/portable-stories.test.ts`** -> AI Confidence: **99.18%**
182. **`code/renderers/vue3/src/__tests__/composeStories/portable-stories.test.ts`** -> AI Confidence: **99.18%**
183. **`code/renderers/vue3/src/preview.ts`** -> AI Confidence: **99.18%**
184. **`code/renderers/web-components/src/preview.ts`** -> AI Confidence: **99.18%**
185. **`code/renderers/web-components/src/render.ts`** -> AI Confidence: **99.18%**
186. **`scripts/sandbox/publish.ts`** -> AI Confidence: **99.18%**
187. **`scripts/tasks/build.ts`** -> AI Confidence: **99.18%**
188. **`scripts/tasks/dev.ts`** -> AI Confidence: **99.18%**
189. **`scripts/tasks/serve.ts`** -> AI Confidence: **99.18%**
190. **`code/addons/pseudo-states/src/preview/splitSelectors.ts`** -> AI Confidence: **99.17%**
191. **`code/addons/vitest/src/vitest-plugin/types.ts`** -> AI Confidence: **99.17%**
192. **`code/core/src/controls/types.ts`** -> AI Confidence: **99.17%**
193. **`code/core/src/shared/utils/toHaveLiveRegion.ts`** -> AI Confidence: **99.17%**
194. **`code/frameworks/react-vite/src/plugins/react-docgen.ts`** -> AI Confidence: **99.17%**
195. **`code/lib/cli-storybook/src/autoblock/block-webpack5-frameworks.ts`** -> AI Confidence: **99.17%**
196. **`scripts/dangerfile.js`** -> AI Confidence: **99.17%**
197. **`code/addons/a11y/src/components/A11yContext.tsx`** -> AI Confidence: **99.16%**
198. **`code/addons/onboarding/src/Onboarding.tsx`** -> AI Confidence: **99.16%**
199. **`code/addons/vitest/src/preset.ts`** -> AI Confidence: **99.16%**
200. **`code/builders/builder-vite/src/plugins/storybook-external-globals-plugin.ts`** -> AI Confidence: **99.16%**
201. **`code/builders/builder-webpack5/src/index.ts`** -> AI Confidence: **99.16%**
202. **`code/builders/builder-webpack5/src/presets/custom-webpack-preset.ts`** -> AI Confidence: **99.16%**
203. **`code/core/src/bin/loader.ts`** -> AI Confidence: **99.16%**
204. **`code/core/src/common/js-package-manager/BUNProxy.ts`** -> AI Confidence: **99.16%**
205. **`code/core/src/common/js-package-manager/NPMProxy.ts`** -> AI Confidence: **99.16%**
206. **`code/core/src/component-testing/components/Panel.tsx`** -> AI Confidence: **99.16%**
207. **`code/core/src/controls/manager.tsx`** -> AI Confidence: **99.16%**
208. **`code/core/src/core-server/utils/get-new-story-file.ts`** -> AI Confidence: **99.16%**
209. **`code/core/src/docs-tools/argTypes/docgen/createPropDef.ts`** -> AI Confidence: **99.16%**
210. **`code/core/src/manager/components/preview/Preview.tsx`** -> AI Confidence: **99.16%**
211. **`code/core/src/manager/components/sidebar/SearchResults.tsx`** -> AI Confidence: **99.16%**
212. **`code/core/src/manager/components/sidebar/Sidebar.tsx`** -> AI Confidence: **99.16%**
213. **`code/core/src/manager/components/sidebar/Tree.tsx`** -> AI Confidence: **99.16%**
214. **`code/core/src/preview-api/modules/preview-web/Preview.tsx`** -> AI Confidence: **99.16%**
215. **`code/core/src/preview-api/modules/store/StoryStore.ts`** -> AI Confidence: **99.16%**
216. **`code/core/src/shared/checklist-store/checklistData.tsx`** -> AI Confidence: **99.16%**
217. **`code/core/src/telemetry/telemetry.ts`** -> AI Confidence: **99.16%**
218. **`code/core/src/types/modules/api.ts`** -> AI Confidence: **99.16%**
219. **`code/frameworks/angular/src/builders/start-storybook/index.ts`** -> AI Confidence: **99.16%**
220. **`code/frameworks/nextjs/src/utils.ts`** -> AI Confidence: **99.16%**
221. **`code/lib/cli-storybook/src/automigrate/fixes/addon-storysource-code-panel.ts`** -> AI Confidence: **99.16%**
222. **`code/lib/cli-storybook/src/util.ts`** -> AI Confidence: **99.16%**
223. **`code/lib/create-storybook/src/generators/baseGenerator.ts`** -> AI Confidence: **99.16%**
224. **`code/lib/create-storybook/src/initiate.ts`** -> AI Confidence: **99.16%**
225. **`code/renderers/react/src/componentManifest/generator.test.ts`** -> AI Confidence: **99.16%**
226. **`code/renderers/react/src/componentManifest/reactDocgen.ts`** -> AI Confidence: **99.16%**
227. **`code/renderers/react/src/preset.ts`** -> AI Confidence: **99.16%**
228. **`scripts/bench/bench-packages.ts`** -> AI Confidence: **99.16%**
229. **`scripts/ci/main.ts`** -> AI Confidence: **99.16%**
230. **`scripts/run-registry.ts`** -> AI Confidence: **99.16%**
231. **`scripts/snippets/codemod.ts`** -> AI Confidence: **99.16%**
232. **`scripts/task.ts`** -> AI Confidence: **99.16%**
233. **`scripts/tasks/sandbox-parts.ts`** -> AI Confidence: **99.16%**
234. **`code/addons/onboarding/src/manager.tsx`** -> AI Confidence: **99.15%**
235. **`code/builders/builder-vite/src/build.ts`** -> AI Confidence: **99.15%**
236. **`code/builders/builder-vite/src/codegen-project-annotations.ts`** -> AI Confidence: **99.15%**
237. **`code/builders/builder-vite/src/plugins/storybook-optimize-deps-plugin.ts`** -> AI Confidence: **99.15%**
238. **`code/core/src/actions/containers/ActionLogger/index.tsx`** -> AI Confidence: **99.15%**
239. **`code/core/src/actions/runtime/action.ts`** -> AI Confidence: **99.15%**
240. **`code/core/src/common/utils/get-storybook-refs.ts`** -> AI Confidence: **99.15%**
241. **`code/core/src/common/utils/normalize-stories.ts`** -> AI Confidence: **99.15%**
242. **`code/core/src/common/utils/sync-main-preview-addons.ts`** -> AI Confidence: **99.15%**
243. **`code/core/src/common/utils/validate-configuration-files.ts`** -> AI Confidence: **99.15%**
244. **`code/core/src/component-testing/components/PanelTitle.tsx`** -> AI Confidence: **99.15%**
245. **`code/core/src/component-testing/manager.tsx`** -> AI Confidence: **99.15%**
246. **`code/core/src/components/components/Button/Button.tsx`** -> AI Confidence: **99.15%**
247. **`code/core/src/components/components/Tabs/TabPanel.stories.tsx`** -> AI Confidence: **99.15%**
248. **`code/core/src/components/components/Tabs/TabPanel.tsx`** -> AI Confidence: **99.15%**
249. **`code/core/src/components/components/Tabs/Tabs.hooks.tsx`** -> AI Confidence: **99.15%**
250. **`code/core/src/core-server/change-detection/GitDiffProvider.test.ts`** -> AI Confidence: **99.15%**
251. **`code/core/src/core-server/load.ts`** -> AI Confidence: **99.15%**
252. **`code/core/src/core-server/server-channel/file-search-channel.ts`** -> AI Confidence: **99.15%**
253. **`code/core/src/core-server/utils/get-server-channel.ts`** -> AI Confidence: **99.15%**
254. **`code/core/src/core-server/utils/whats-new.ts`** -> AI Confidence: **99.15%**
255. **`code/core/src/manager/components/TourGuide/TourGuide.tsx`** -> AI Confidence: **99.15%**
256. **`code/core/src/manager/components/preview/tools/zoom.tsx`** -> AI Confidence: **99.15%**
257. **`code/core/src/manager/components/sidebar/ChecklistWidget.tsx`** -> AI Confidence: **99.15%**
258. **`code/core/src/manager/components/sidebar/CreateNewStoryFileModal.tsx`** -> AI Confidence: **99.15%**
259. **`code/core/src/manager/components/sidebar/Filter.story-helpers.tsx`** -> AI Confidence: **99.15%**
260. **`code/core/src/manager/components/sidebar/FilterPanel.tsx`** -> AI Confidence: **99.15%**
261. **`code/core/src/manager/components/sidebar/RefBlocks.tsx`** -> AI Confidence: **99.15%**
262. **`code/core/src/manager/components/sidebar/SidebarBottom.tsx`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6178` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `code/core/src/common/utils/file-cache.ts` (TYPESCRIPT) -> Cumulative Risk: **768.47**
- **Archetype:** `file_cluster_4` (Distance: 13.757 IQR)
- **Magnitude:** 31.97 | **LOC:** 163 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `get` (Impact: 7.3), `getSync` (Impact: 7.3), `setMany` (Impact: 7.1)

### 2. `code/core/src/preview-api/modules/preview-web/WebView.ts` (TYPESCRIPT) -> Cumulative Risk: **735.8**
- **Archetype:** `file_cluster_13` (Distance: 12.31 IQR)
- **Magnitude:** 17.15 | **LOC:** 209 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (97.3179%)
- **Heaviest Functions:** `constructor` (Impact: 12.3), `showNoPreview` (Impact: 6.2), `showMode` (Impact: 5.7)

### 3. `code/frameworks/nextjs/src/swc/next-swc-loader-patch.ts` (TYPESCRIPT) -> Cumulative Risk: **720.57**
- **Archetype:** `file_cluster_4` (Distance: 12.236 IQR)
- **Magnitude:** 20.52 | **LOC:** 206 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.9864%)
- **Heaviest Functions:** `loaderTransform` (Impact: 85.4), `pitch` (Impact: 21.9), `swcLoader` (Impact: 4.7)

### 4. `code/frameworks/angular/src/client/angular-beta/RendererFactory.ts` (TYPESCRIPT) -> Cumulative Risk: **717.85**
- **Archetype:** `file_cluster_4` (Distance: 11.84 IQR)
- **Magnitude:** 8.2 | **LOC:** 61 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `clearRootHTMLElement` (Impact: 16.6), `getRendererInstance` (Impact: 12.4), `getRenderType` (Impact: 4.6)

### 5. `code/core/src/channels/websocket/index.ts` (TYPESCRIPT) -> Cumulative Risk: **708.45**
- **Archetype:** `file_cluster_13` (Distance: 12.469 IQR)
- **Magnitude:** 11.28 | **LOC:** 109 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `send` (Impact: 7.4), `onclose` (Impact: 4.0), `invariant` (Impact: 3.8)

### 6. `code/addons/links/src/react/components/link.tsx` (TYPESCRIPT) -> Cumulative Risk: **669.87**
- **Archetype:** `file_cluster_4` (Distance: 11.54 IQR)
- **Magnitude:** 7.38 | **LOC:** 88 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `componentDidUpdate` (Impact: 9.3), `cb` (Impact: 7.6), `updateHref` (Impact: 5.5)

### 7. `code/core/src/core-server/change-detection/GitDiffProvider.ts` (TYPESCRIPT) -> Cumulative Risk: **669.49**
- **Archetype:** `file_cluster_4` (Distance: 13.998 IQR)
- **Magnitude:** 46.81 | **LOC:** 288 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `onChange` (Impact: 21.2), `getGitDir` (Impact: 15.3), `configureBranchWatcher` (Impact: 12.4)

### 8. `code/core/src/preview-api/modules/preview-web/render/StoryRender.ts` (TYPESCRIPT) -> Cumulative Risk: **666.15**
- **Archetype:** `file_cluster_4` (Distance: 13.753 IQR)
- **Magnitude:** 63.36 | **LOC:** 497 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `rerender` (Impact: 7.3), `runPhase` (Impact: 6.6), `checkIfAborted` (Impact: 6.5)

### 9. `code/core/src/manager-api/root.tsx` (TYPESCRIPT) -> Cumulative Risk: **662.67**
- **Archetype:** `file_cluster_13` (Distance: 11.132 IQR)
- **Magnitude:** 31.18 | **LOC:** 516 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (98.3621%), Verification (80.0%)
- **Heaviest Functions:** `initModules` (Impact: 67.1), `useSharedState` (Impact: 32.0), `useArgs` (Impact: 13.0)

### 10. `code/renderers/web-components/template/components/Form.js` (JAVASCRIPT) -> Cumulative Risk: **660.06**
- **Archetype:** `file_cluster_4` (Distance: 11.292 IQR)
- **Magnitude:** 59.44 | **LOC:** 82 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8292%)
- **Heaviest Functions:** `render` (Impact: 3.9), `onSubmit` (Impact: 3.8), `properties` (Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `code/core/src/manager-api/tests/url.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.035 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.084 IQR)
- **Top Global Matches:** file_cluster_8: 11.035, file_cluster_13: 11.379, file_cluster_1: 11.401
- **Magnitude:** 372.34 | **LOC:** 567 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (41.2859%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 65.9)
  * `describe` (Impact: 16.6)
  * `describe` (Impact: 16.5)
  * `it` (Impact: 7.8)
  * `it` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 70`, `args: 63`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 56`, `duplicate_logic: 60`
* *Architecture:* `io: 24`, `concurrency: 18`, `import: 5`
* *Defense:* `test: 99`, `immutability_locks: 74`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` vitest, url, core-events, global, events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.875 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.713 IQR)
- **Top Global Matches:** file_cluster_8: 10.875, file_cluster_4: 11.181, file_cluster_1: 11.207
- **Magnitude:** 351.46 | **LOC:** 4120 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.1953%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 279.1)
  * `describe` (Impact: 244.4)
  * `describe` (Impact: 194.3)
  * `describe` (Impact: 133.0)
  * `describe` (Impact: 118.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 731`, `args: 563`, `func_start: 488`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 24`, `duplicate_logic: 321`
* *Architecture:* `io: 38`, `api: 1`, `concurrency: 649`, `import: 12`
* *Defense:* `safety: 26`, `doc: 2`, `test: 463`, `immutability_locks: 171`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WebView.ts, vitest, index.ts, core-events, PreviewWeb.mockdata.ts, global, client-logger, PreviewWeb.tsx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager-api/tests/shortcuts.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.048 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_4: 10.048, file_cluster_8: 10.313, file_cluster_7: 11.052
- **Magnitude:** 273.48 | **LOC:** 292 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 18.9)
  * `it` (Impact: 5.7)
  * `it` (Impact: 4.7)
  * `it` (Impact: 4.1)
  * `createMockStore` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 20`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `duplicate_logic: 19`
* *Architecture:* `concurrency: 172`, `import: 2`
* *Defense:* `safety: 2`, `test: 43`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, shortcuts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager-api/tests/versions.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.399 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.579 IQR)
- **Top Global Matches:** file_cluster_8: 9.399, file_cluster_4: 9.552, file_cluster_7: 10.143
- **Magnitude:** 243.88 | **LOC:** 362 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 32.8)
  * `describe` (Impact: 25.5)
  * `it` (Impact: 5.8)
  * `describe` (Impact: 5.6)
  * `it` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 57`, `args: 33`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`, `duplicate_logic: 42`
* *Architecture:* `io: 12`, `concurrency: 73`, `import: 3`
* *Defense:* `test: 54`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` versions, vitest, global
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/ConfigFile.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.357 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.675 IQR)
- **Top Global Matches:** file_cluster_8: 10.357, file_cluster_13: 10.632, file_cluster_0: 10.827
- **Magnitude:** 173.78 | **LOC:** 1928 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.7624%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 306.9)
  * `describe` (Impact: 79.5)
  * `describe` (Impact: 50.1)
  * `describe` (Impact: 40.7)
  * `describe` (Impact: 38.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 547`, `args: 302`, `func_start: 365`
* *Risk/State:* `safety_bypasses: 7`, `planned_debt: 4`, `duplicate_logic: 163`
* *Architecture:* `io: 104`, `api: 243`, `concurrency: 1`, `import: 78`
* *Defense:* `safety: 31`, `test: 292`, `immutability_locks: 335`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ts-dedent, vitest, baz, fs, react-vite, react-webpack5, ConfigFile.ts, babel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/vitest-plugin/transformer.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.091 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.33 IQR)
- **Top Global Matches:** file_cluster_8: 10.091, file_cluster_13: 10.263, file_cluster_0: 10.603
- **Magnitude:** 166.1 | **LOC:** 1388 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.9996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 319.7)
  * `describe` (Impact: 194.3)
  * `describe` (Impact: 119.8)
  * `describe` (Impact: 94.6)
  * `describe` (Impact: 68.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 390`, `args: 173`, `func_start: 146`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 54`
* *Architecture:* `api: 138`, `concurrency: 77`, `import: 92`
* *Defense:* `safety: 32`, `test: 101`, `immutability_locks: 259`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vitest, transformer.ts, source-map, preview, Button.stories, tags.ts, node-logger, test-utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/CsfFile.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.976 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.16 IQR)
- **Top Global Matches:** file_cluster_8: 9.976, file_cluster_13: 10.626, file_cluster_7: 10.64
- **Magnitude:** 159.34 | **LOC:** 3155 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.9311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 231.8)
  * `describe` (Impact: 128.3)
  * `describe` (Impact: 92.3)
  * `describe` (Impact: 48.0)
  * `describe` (Impact: 45.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 564`, `args: 308`, `func_start: 406`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 118`
* *Architecture:* `io: 9`, `api: 238`, `concurrency: 5`, `import: 51`
* *Defense:* `safety: 21`, `test: 235`, `immutability_locks: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` #bar.mock, A, node-logger, some-library, bad-preview, CsfFile.ts, Check, schemas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MIGRATION.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 147.8 | **LOC:** 7390 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `scripts/dangerfile.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.512 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.881 IQR)
- **Top Global Matches:** file_cluster_8: 10.512, file_cluster_7: 11.024, file_cluster_13: 11.104
- **Magnitude:** 129.88 | **LOC:** 195 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (7.7385%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `checkRequiredLabels` (Impact: 38.7)
  * `checkManualTestingSection` (Impact: 19.5)
  * `checkTargetBranch` (Impact: 18.5)
    * *Intent:* // Extract content after the manual testing section
  * `fail` (Impact: 12.1)
  * `fail` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 14`, `args: 9`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 9`
* *Architecture:* `import: 2`
* *Defense:* `safety: 16`, `doc: 12`, `test: 1`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` package.json, danger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/eslint-plugin/src/rules/await-interactions.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.209 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.169 IQR)
- **Top Global Matches:** file_cluster_8: 8.209, file_cluster_4: 9.044, file_cluster_7: 9.173
- **Magnitude:** 123.05 | **LOC:** 812 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.7662%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 181`, `args: 88`, `func_start: 108`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 24`, `concurrency: 139`, `import: 12`
* *Defense:* `safety: 6`, `doc: 1`, `test: 23`, `immutability_locks: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ts-dedent, jest, testing-library, test-utils.ts, test, await-interactions.ts, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/CsfFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.523 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.999 IQR)
- **Top Global Matches:** file_cluster_17: 12.523, file_cluster_11: 12.598, file_cluster_13: 12.752
- **Magnitude:** 106.68 | **LOC:** 1113 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (61.4438%), Tech Debt (98.0563%)
**Top Internal Functions/Classes:**
  * `traverse` (Impact: 222.9)
  * `parse` (Impact: 185.6)
  * `enter` (Impact: 107.7)
  * `enter` (Impact: 43.9)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-this-alias
  * `_parseMeta` (Impact: 42.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 141`, `args: 68`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 132`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 13`
* *Architecture:* `io: 23`, `api: 32`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 92`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts-dedent, promises, csf, findVarInitialization.ts, node-logger, PrintResultType.ts, path-to-component, babel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/generateCodeSnippet.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.014 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.46 IQR)
- **Top Global Matches:** file_cluster_8: 10.014, file_cluster_17: 10.273, file_cluster_7: 10.576
- **Magnitude:** 100.47 | **LOC:** 651 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.4357%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCodeSnippet` (Impact: 384.4)
  * `getRenderPath` (Impact: 380.6)
  * `resolveIdentifierInit` (Impact: 36.9)
  * `getArgsMemberKey` (Impact: 33.4)
    * *Intent:* /** Find `StoryName.args = { ... }` assignment and return the right-hand ObjectExpression if present...
  * `storyArgsAssignmentPath` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 114`, `args: 64`, `func_start: 26`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 5`, `api: 8`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 13`, `doc: 6`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils.ts, csf-tools, babel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/docs-tools/argTypes/jsdocParser.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.997 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.928 IQR)
- **Top Global Matches:** file_cluster_0: 14.997, file_cluster_8: 15.35, file_cluster_15: 15.48
- **Magnitude:** 98.84 | **LOC:** 363 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.8909%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 272.5)
  * `describe` (Impact: 157.8)
  * `describe` (Impact: 81.2)
  * `describe` (Impact: 44.9)
  * `describe` (Impact: 35.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 107`, `args: 151`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 55`
* *Architecture:* `import: 2`
* *Defense:* `safety: 155`, `doc: 68`, `test: 149`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jsdocParser.ts, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/ConfigFile.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.415 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_17: 12.415, file_cluster_11: 12.588, file_cluster_8: 12.609
- **Magnitude:** 88.47 | **LOC:** 1203 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (71.1948%), Tech Debt (99.9705%)
**Top Internal Functions/Classes:**
  * `setFieldNode` (Impact: 140.5)
  * `traverse` (Impact: 79.3)
  * `parse` (Impact: 66.2)
  * `setRequireImport` (Impact: 33.2)
  * `_findVarDeclarator` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 147`, `args: 89`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 237`, `dead_code: 4`, `fragile_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `io: 44`, `api: 19`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 9`, `doc: 16`, `immutability_locks: 93`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts-dedent, promises, baz, foo, node-logger, bar, PrintResultType.ts, babel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.props.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.464 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.666 IQR)
- **Top Global Matches:** file_cluster_13: 11.464, file_cluster_8: 11.478, file_cluster_4: 11.764
- **Magnitude:** 84.67 | **LOC:** 756 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.276%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 174.3)
  * `describe` (Impact: 53.0)
  * `describe` (Impact: 50.6)
  * `describe` (Impact: 33.1)
  * `describe` (Impact: 22.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 344`, `args: 134`, `func_start: 133`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 80`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 74`, `import: 43`
* *Defense:* `safety: 59`, `doc: 4`, `test: 83`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ts-dedent, vitest, Accordion, componentMetaExtractor.test-helpers.ts, Panel, Widget, Button, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/core-server/utils/StoryIndexGenerator.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.373 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.874 IQR)
- **Top Global Matches:** file_cluster_8: 8.373, file_cluster_7: 9.163, file_cluster_1: 9.302
- **Magnitude:** 83.02 | **LOC:** 2425 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (16.2376%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 90.3)
  * `describe` (Impact: 89.8)
  * `describe` (Impact: 60.7)
  * `describe` (Impact: 32.9)
  * `describe` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 287`, `args: 142`, `func_start: 134`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `duplicate_logic: 69`
* *Architecture:* `io: 1`, `concurrency: 175`, `import: 13`
* *Defense:* `safety: 1`, `doc: 14`, `test: 133`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vitest, csf, tags.ts, StoryIndexGenerator.ts, async () => 
        const csfSpecifier: NormalizedStoriesSpecifier = normalizeStoriesEntry(, csf-tools, node-logger, common-preset.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/theming/tests/create.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.498 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.75 IQR)
- **Top Global Matches:** file_cluster_8: 8.498, file_cluster_13: 9.449, file_cluster_7: 9.457
- **Magnitude:** 77.02 | **LOC:** 172 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.5733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 5.6)
  * `describe` (Impact: 4.7)
  * `it` (Impact: 3.9)
  * `it` (Impact: 3.7)
  * `describe` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 33`, `args: 26`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 28`
* *Architecture:* `io: 4`, `concurrency: 4`, `import: 5`
* *Defense:* `test: 50`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vitest, create, create, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/instrumenter/instrumenter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.524 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.592 IQR)
- **Top Global Matches:** file_cluster_17: 13.524, file_cluster_11: 13.759, file_cluster_13: 13.847
- **Magnitude:** 74.45 | **LOC:** 842 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.4472%), Tech Debt (92.8291%)
**Top Internal Functions/Classes:**
  * `constructor` (Impact: 189.0)
  * `instrument` (Impact: 101.5)
  * `sync` (Impact: 17.8)
  * `synchronize` (Impact: 17.4)
  * `handleException` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 119`, `args: 74`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 251`, `dead_code: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 20`, `import: 10`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 61`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.178
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` EVENTS.ts, core-events, channels, global, client-logger, typings.d.ts, preview-api.ts, types.ts...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `code/lib/create-storybook/src/bin/run.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.353 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.603 IQR)
- **Top Global Matches:** file_cluster_8: 8.353, file_cluster_13: 8.803, file_cluster_7: 9.207
- **Magnitude:** 72.73 | **LOC:** 129 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.982%), Tech Debt (11.1784%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 25`, `args: 6`, `func_start: 2`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `io: 3`, `concurrency: 5`, `import: 9`
* *Defense:* `safety: 6`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` types.ts, node-logger, telemetry, package.json, cli, commander, initiate.ts, common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.4.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.555 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.933 IQR)
- **Top Global Matches:** file_cluster_8: 9.555, file_cluster_13: 9.709, file_cluster_0: 10.151
- **Magnitude:** 72.11 | **LOC:** 2217 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (3.8698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 207.4)
  * `it` (Impact: 22.2)
  * `it` (Impact: 22.2)
  * `it` (Impact: 21.0)
  * `it` (Impact: 20.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 397`, `args: 122`, `func_start: 111`
* *Risk/State:* `duplicate_logic: 25`
* *Architecture:* `io: 160`, `api: 55`, `concurrency: 50`, `import: 206`
* *Defense:* `safety: 4`, `test: 126`, `immutability_locks: 167`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, vitest-plugin, url, node:url, config, getDiff.ts, browser-playwright, vite.config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.425 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.857 IQR)
- **Top Global Matches:** file_cluster_8: 9.425, file_cluster_13: 9.628, file_cluster_7: 10.139
- **Magnitude:** 71.99 | **LOC:** 2061 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (3.9467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 212.2)
  * `it` (Impact: 22.1)
  * `it` (Impact: 22.1)
  * `it` (Impact: 20.9)
  * `it` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 370`, `args: 122`, `func_start: 111`
* *Risk/State:* `duplicate_logic: 25`
* *Architecture:* `io: 160`, `api: 55`, `concurrency: 50`, `import: 180`
* *Defense:* `safety: 4`, `test: 99`, `immutability_locks: 163`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, vitest-plugin, url, node:url, config, getDiff.ts, vite.config, updateVitestFile.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.3.2.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.353 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.856 IQR)
- **Top Global Matches:** file_cluster_8: 9.353, file_cluster_13: 9.561, file_cluster_7: 10.075
- **Magnitude:** 68.04 | **LOC:** 1898 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (3.9435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 212.0)
  * `it` (Impact: 22.7)
  * `it` (Impact: 22.1)
  * `it` (Impact: 22.0)
  * `it` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 336`, `args: 113`, `func_start: 102`
* *Risk/State:* `duplicate_logic: 23`
* *Architecture:* `io: 148`, `api: 46`, `concurrency: 46`, `import: 165`
* *Defense:* `safety: 4`, `test: 91`, `immutability_locks: 146`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, vitest-plugin, url, node:url, config, getDiff.ts, vite.config, updateVitestFile.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/eslint-plugin/src/rules/default-exports.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.298 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.712 IQR)
- **Top Global Matches:** file_cluster_8: 8.298, file_cluster_13: 8.532, file_cluster_7: 9.124
- **Magnitude:** 67.75 | **LOC:** 130 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.7733%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 45`, `args: 13`, `func_start: 19`
* *Risk/State:* None
* *Architecture:* `api: 19`, `import: 14`
* *Defense:* `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts-dedent, MyComponent, preview, default-exports.ts, test-utils.ts, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/preview-api/modules/addons/hooks.test.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.976 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.685 IQR)
- **Top Global Matches:** file_cluster_8: 8.976, file_cluster_13: 9.79, file_cluster_7: 9.851
- **Magnitude:** 66.74 | **LOC:** 58 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6408%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 16.5)
  * `describe` (Impact: 15.6)
  * `it` (Impact: 5.3)
  * `it` (Impact: 5.3)
  * `it` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `args: 13`, `func_start: 18`
* *Risk/State:* `duplicate_logic: 11`
* *Architecture:* `import: 2`
* *Defense:* `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `code/renderers/preact/src/preset.ts` (TYPESCRIPT) | Magnitude: 1.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, immutability_locks: 5, api: 4
- `code/frameworks/sveltekit/src/preview.ts` (TYPESCRIPT) | Magnitude: 2.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 12, structural_boundaries: 11, safety: 10
- `code/lib/create-storybook/src/generators/ANGULAR/index.ts` (TYPESCRIPT) | Magnitude: 9.95 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 112, branch: 33, structural_boundaries: 22, immutability_locks: 17
- `code/core/src/core-server/presets/common-override-preset.ts` (TYPESCRIPT) | Magnitude: 5.2 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, branch: 18, structural_boundaries: 18, safety: 10
- `code/builders/builder-webpack5/src/plugins/webpack-mock-plugin.ts` (TYPESCRIPT) | Magnitude: 15.38 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, state_mutation: 56, branch: 35, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `code/core/src/test/preview.ts` (TYPESCRIPT) | Magnitude: 12.74 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, branch: 44, structural_boundaries: 30, func_start: 17
- `code/core/src/client-logger/index.ts` (TYPESCRIPT) | Magnitude: 6.54 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 25, state_mutation: 21, safety_bypasses: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `code/addons/pseudo-states/src/stories/Button.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, ui_framework: 2, args: 1
- `code/addons/pseudo-states/src/stories/CSSAtRules.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, ui_framework: 2, args: 1
- `code/addons/themes/src/decorators/class-name.decorator.tsx` (TYPESCRIPT) | Magnitude: 3.05 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 18, immutability_locks: 9, branch: 8
- `code/core/src/csf/csf-factories.ts` (TYPESCRIPT) | Magnitude: 33.57 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 84, generics: 66, branch: 64
- `code/lib/cli-storybook/src/automigrate/helpers/mainConfigFile.ts` (TYPESCRIPT) | Magnitude: 12.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 56, branch: 47, immutability_locks: 27

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
- `code/core/src/core-server/utils/IndexingError.ts` (TYPESCRIPT) | Magnitude: 8.33 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 50, indent_spaces: 38, structural_boundaries: 13, args: 8
- `code/core/src/preview-api/modules/store/csf/composeConfigs.ts` (TYPESCRIPT) | Magnitude: 3.66 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 25, branch: 9, args: 9
- `code/lib/codemod/src/transforms/upgrade-hierarchy-separators.js` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 10, args: 9, comprehensions: 9
- `code/core/src/preview-api/modules/store/csf/processCSFFile.ts` (TYPESCRIPT) | Magnitude: 5.01 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 22, args: 16, immutability_locks: 16
- `code/core/src/test/spy.ts` (TYPESCRIPT) | Magnitude: 5.68 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 51, indent_spaces: 37, args: 30, generics: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `code/renderers/svelte/src/portable-stories.ts` (TYPESCRIPT) | Magnitude: 3.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 28, generics: 23, ui_framework: 20
- `code/renderers/react/template/stories/decorators.stories.tsx` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 24, args: 10, ui_framework: 9
- `code/addons/pseudo-states/src/stories/Input.stories.tsx` (TYPESCRIPT) | Magnitude: 1.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, ui_framework: 9, api: 5
- `code/core/src/components/components/Tabs/StatelessTabList.tsx` (TYPESCRIPT) | Magnitude: 3.37 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, immutability_locks: 28, structural_boundaries: 24, ui_framework: 24
- `code/core/src/manager/components/Focus/Focus.tsx` (TYPESCRIPT) | Magnitude: 5.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 18, concurrency: 14, ui_framework: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `code/lib/create-storybook/src/commands/PreflightCheckCommand.ts` (TYPESCRIPT) | Magnitude: 8.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, concurrency: 22, structural_boundaries: 18, branch: 8
- `code/addons/links/src/react/components/link.tsx` (TYPESCRIPT) | Magnitude: 7.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 22, structural_boundaries: 19, branch: 18
- `code/frameworks/angular/src/client/angular-beta/RendererFactory.test.ts` (TYPESCRIPT) | Magnitude: 21.43 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 57, concurrency: 47, globals: 47
- `code/frameworks/nextjs-vite/template/stories/RSC.tsx` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, api: 2
- `code/frameworks/nextjs/template/stories/RSC.tsx` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 2, func_start: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `code/renderers/preact/template/components/Pre.jsx` (JAVASCRIPT) | Magnitude: 2.2 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, indent_spaces: 3, structural_boundaries: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `code/core/template/stories/loader-enhancements.stories.ts` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, immutability_locks: 3, api: 2
- `code/core/src/node-logger/logger/console.ts` (TYPESCRIPT) | Magnitude: 9.6 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 35, args: 23, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `code/addons/vitest/src/node/boot-test-runner.test.ts` (TYPESCRIPT) | Magnitude: 9.07 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 74, args: 44, func_start: 28
- `code/frameworks/nextjs-vite/template/stories/DynamicImport.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1
- `code/frameworks/nextjs/template/stories/dynamic-component.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, branch: 1, args: 1
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

- `code/renderers/react/src/componentManifest/generator.ts` -> Churn: **76.53%** | Cog Load: 21.9417% | Debt: 67.8471%
- `code/core/src/manager/components/preview/tools/zoom.tsx` -> Churn: **69.13%** | Cog Load: 10.0421% | Debt: 99.9997%
- `code/core/src/types/modules/core-common.ts` -> Churn: **68.37%** | Cog Load: 45.2915% | Debt: 99.9628%
- `code/renderers/react/src/componentManifest/getComponentImports.ts` -> Churn: **66.78%** | Cog Load: 32.5145% | Debt: 98.2694%
- `code/addons/vitest/src/updateVitestFile.ts` -> Churn: **63.16%** | Cog Load: 30.9556% | Debt: 80.1565%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 351.46
- `code/core/src/manager-api/tests/shortcuts.test.js` -> **Gert Hengeveld** (100.0% isolated ownership) | Magnitude: 273.48
- `code/core/src/csf-tools/CsfFile.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 159.34
- `code/lib/eslint-plugin/src/rules/await-interactions.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 123.05
- `code/renderers/react/src/componentManifest/generateCodeSnippet.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 100.47

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/core/src/shared/universal-store/mock.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `code/core/src/components/components/typography/lib/common.tsx` -> **Severity: 2888.486** (Blast Radius: 45.047 * Doc Risk: 64.1216%)
- `code/addons/vitest/src/node/vitest.ts` -> **Severity: 1681.198** (Blast Radius: 63.363 * Doc Risk: 26.5328%)
- `scripts/ecosystem-ci/test.sh` -> **Severity: 864.954** (Blast Radius: 33.198 * Doc Risk: 26.0544%)
- `code/core/src/highlight/icons.ts` -> **Severity: 827.918** (Blast Radius: 15.319 * Doc Risk: 54.0452%)
- `code/core/src/theming/global.ts` -> **Severity: 594.439** (Blast Radius: 26.968 * Doc Risk: 22.0424%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
