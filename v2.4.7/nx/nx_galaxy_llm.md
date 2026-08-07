# ARCHITECTURAL_BRIEF: nx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/nx` |
| **Timestamp** | `2026-08-07T04:16:49.782341+00:00` |
| **Scan Duration** | `19.07s` |
| **Git Branch** | `master` |
| **Git Commit** | `557c876e96c1f92f39eb05cb79f0cf06973ee214` |
| **Git Remote** | `https://github.com/nrwl/nx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4684 malicious artifacts.

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
| Total Artifacts | 10631 |
| Analyzed Artifacts (Scanned) | 6132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4499 |
| Total LOC | 644130 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1483 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 510 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 4300 | 541666 | 70.1% |
| JSON | 805 | 56005 | 13.1% |
| MARKDOWN | 210 | 0 | 3.4% |
| PLAINTEXT | 169 | 6 | 2.8% |
| RUST | 137 | 25441 | 2.2% |
| XML | 130 | 505 | 2.1% |
| JAVASCRIPT | 117 | 6471 | 1.9% |
| KOTLIN | 93 | 8136 | 1.5% |
| HTML | 90 | 3038 | 1.5% |
| CSS | 37 | 967 | 0.6% |
| CSHARP | 23 | 893 | 0.4% |
| YAML | 7 | 242 | 0.1% |
| SHELL | 5 | 326 | 0.1% |
| BATCH | 3 | 298 | 0.0% |
| GROOVY | 3 | 66 | 0.0% |
| RUBY | 2 | 31 | 0.0% |
| SWIFT | 1 | 39 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.524`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3895 | 63.5% |
| file_cluster_13 | 1188 | 19.4% |
| file_cluster_4 | 254 | 4.1% |
| file_cluster_0 | 205 | 3.3% |
| file_cluster_2 | 87 | 1.4% |
| file_cluster_17 | 60 | 1.0% |
| file_cluster_16 | 26 | 0.4% |
| Unknown | 6 | 0.1% |
| file_cluster_1 | 4 | 0.1% |
| file_cluster_7 | 4 | 0.1% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 373 | 6.1% |
| Static: Minified & Vendor Opaque Mass | 28 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4499*

**Composition by Extension & Reason:**
- `.avif`: 756x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 132x Excluded (Binary Format Detected), 105x Excluded (Unsupported Extension: '.avif')
- `.mdoc`: 497x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 495x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 392x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 377x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 6795 LOC), 2x Excluded (Massive Static Asset Blob: 9787 LOC)
- `.webp`: 253x Excluded (Explicitly Denied Extension: '.webp')
- `.ts`: 203x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 2x Excluded (Machine-Generated Source Code Signature: 1185 LOC)
- `.snap`: 220x Unsupported Format (.snap), 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 19 exceeds 500 chars)
- `no_extension`: 122x Unsupported Format (.undeterminable), 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 252 LOC)
- `.tsx`: 58x Excluded (Saturation: Line 12 exceeds 500 chars), 34x Excluded (Saturation: Line 15 exceeds 500 chars), 14x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.ts__tmpl__`: 143x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 50 exceeds 500 chars)
- `.jpg`: 61x Excluded (Explicitly Denied Extension: '.jpg')
- `.tsx__tmpl__`: 54x Unsupported Format (.undeterminable)
- `.svg`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js__tmpl__`: 48x Unsupported Format (.undeterminable)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.4 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 21.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.8 | 4.1 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 28.8 | 4.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.6 | 5.8 | 3.2 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.2 | 23.5 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/large-project.bun.lock.ts` (Hits: 2494)
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/nextjs-app.bun.lock.ts` (Hits: 619)
- `packages/js/src/utils/assets/copy-assets-handler.spec.ts` (Hits: 214)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **js.rs** (`packages/nx/src/native/plugins/js.rs`) — 199 inbound connections
2. **child_process.rs** (`packages/nx/src/native/pseudo_terminal/child_process.rs`) — 150 inbound connections
3. **tree.ts** (`packages/nx/src/generators/tree.ts`) — 133 inbound connections
4. **mock-project-graph.ts** (`packages/nx/src/internal-testing-utils/mock-project-graph.ts`) — 119 inbound connections
5. **semver.ts** (`packages/devkit/src/utils/semver.ts`) — 103 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`nx-dev/ui-icons/src/index.ts`) — 143 outbound dependencies
2. **native-bindings.js** (`packages/nx/src/native/native-bindings.js`) — 82 outbound dependencies
3. **app.rs** (`packages/nx/src/native/tui/app.rs`) — 71 outbound dependencies
4. **server.ts** (`packages/nx/src/daemon/server/server.ts`) — 58 outbound dependencies
5. **tasks_list.rs** (`packages/nx/src/native/tui/components/tasks_list.rs`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `from_str` (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **560.0** | LOC: 1559
- `is_loading_state` (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **503.8** | LOC: 1520
- `runPackageJsonUpdatesConfirmationPrompt` (@ `packages/nx/src/command-line/migrate/migrate.ts`) -> Impact: **457.2** | LOC: 1185
- `extractPropertiesFromObjectLiteral` (@ `packages/eslint/src/generators/utils/flat-config/ast-utils.ts`) -> Impact: **373.6** | LOC: 712
- `add_filter_char` (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **365.3** | LOC: 1106
- `getInputs` (@ `packages/js/src/plugins/typescript/plugin.ts`) -> Impact: **336.6** | LOC: 647
- `joinPathFragments` (@ `packages/js/src/generators/library/library.ts`) -> Impact: **307.8** | LOC: 555
- `libraryGeneratorInternal` (@ `packages/js/src/generators/library/library.ts`) -> Impact: **306.8** | LOC: 662
- `addOverrideToLintConfig` (@ `packages/js/src/generators/library/library.ts`) -> Impact: **288.0** | LOC: 520
- `validateProperty` (@ `packages/nx/src/utils/params.ts`) -> Impact: **279.5** | LOC: 312

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs` | 4 | 6296.15 | 3.21% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package` | 3 | 5236.57 | 2.94% | 0.0% |
| `e2e/dotnet` | 6 | 5033.69 | 4.13% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages` | 6 | 5018.79 | 4.63% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/optional` | 5 | 5017.22 | 4.5% | 0.0% |
| `packages/react-native/src/generators/application/files/app/android/app` | 2 | 5009.8 | 7.85% | 47.9% |
| `packages/nx/src/native/tui/components` | 9 | 4666.88 | 15.61% | 65.14% |
| `packages/nx/src/native/tui` | 18 | 2869.58 | 13.97% | 44.69% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/pnpm-regression` | 3 | 1013.84 | 4.89% | 0.0% |
| `packages/nx/src/utils` | 100 | 934.67 | 24.91% | 42.28% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/expo/src/generators/application/files/base/.babelrc.js.template` -> **100.0%** Exposure
- `packages/expo/src/utils/jest/files/jest.resolver.js` -> **100.0%** Exposure
- `packages/nx/src/native/wasi-worker-browser.mjs` -> **100.0%** Exposure
- `scripts/fetch-nx-issues.js` -> **100.0%** Exposure
- `e2e/gradle/src/utils/create-gradle-project.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/nx/src/native/native-bindings.js` -> **100.0%** Exposure
- `astro-docs/src/pages/llms.txt.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/theme.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/toc.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/watch.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/nx/src/utils/params.spec.ts` -> **0** Orphaned Functions | **250** Duplicates
- `packages/angular/src/generators/library/library.spec.ts` -> **0** Orphaned Functions | **139** Duplicates
- `packages/js/src/plugins/typescript/plugin.spec.ts` -> **2** Orphaned Functions | **134** Duplicates
- `packages/angular/src/generators/ng-add/migrators/projects/app.migrator.spec.ts` -> **1** Orphaned Functions | **123** Duplicates
- `packages/devkit/src/utils/package-json.spec.ts` -> **1** Orphaned Functions | **103** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`e2e/utils/create-project-utils.ts`** -> AI Confidence: **99.39%**
2. **`packages/angular/plugins/component-testing.ts`** -> AI Confidence: **99.39%**
3. **`packages/angular/src/generators/ng-add/migrators/projects/app.migrator.ts`** -> AI Confidence: **99.39%**
4. **`packages/cypress/src/utils/start-dev-server.ts`** -> AI Confidence: **99.39%**
5. **`packages/js/src/executors/release-publish/release-publish.impl.ts`** -> AI Confidence: **99.39%**
6. **`packages/js/src/utils/package-json/update-package-json.ts`** -> AI Confidence: **99.39%**
7. **`packages/nx/src/command-line/init/implementation/angular/standalone-workspace.ts`** -> AI Confidence: **99.39%**
8. **`packages/nx/src/command-line/show/target.ts`** -> AI Confidence: **99.39%**
9. **`packages/nx/src/project-graph/utils/project-configuration/project-nodes-manager.ts`** -> AI Confidence: **99.39%**
10. **`packages/nx/src/project-graph/utils/project-configuration/target-normalization.ts`** -> AI Confidence: **99.39%**
11. **`packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.spec.ts`** -> AI Confidence: **99.39%**
12. **`packages/react/plugins/component-testing/index.ts`** -> AI Confidence: **99.39%**
13. **`packages/react/src/generators/application/lib/create-application-files.ts`** -> AI Confidence: **99.39%**
14. **`packages/storybook/src/generators/configuration/lib/util-functions.ts`** -> AI Confidence: **99.39%**
15. **`packages/vite/src/utils/generator-utils.ts`** -> AI Confidence: **99.39%**
16. **`packages/vitest/src/utils/generator-utils.ts`** -> AI Confidence: **99.39%**
17. **`packages/workspace/src/generators/new/generate-workspace-files.ts`** -> AI Confidence: **99.39%**
18. **`packages/workspace/src/generators/new/new.ts`** -> AI Confidence: **99.39%**
19. **`packages/angular/src/generators/convert-to-rspack/convert-to-rspack.ts`** -> AI Confidence: **99.35%**
20. **`packages/cypress/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.35%**
21. **`packages/nx/src/command-line/init/implementation/utils.ts`** -> AI Confidence: **99.35%**
22. **`packages/nx/src/plugins/js/lock-file/pnpm-parser.ts`** -> AI Confidence: **99.35%**
23. **`packages/rollup/src/plugins/package-json/update-package-json.ts`** -> AI Confidence: **99.35%**
24. **`packages/rspack/src/plugins/utils/apply-base-config.ts`** -> AI Confidence: **99.35%**
25. **`packages/nx/src/native/nx.wasi.cjs`** -> AI Confidence: **99.34%**
26. **`packages/angular/src/generators/convert-to-application-executor/convert-to-application-executor.ts`** -> AI Confidence: **99.34%**
27. **`packages/angular/src/generators/setup-ssr/lib/update-project-config.ts`** -> AI Confidence: **99.34%**
28. **`packages/nx/src/executors/run-commands/run-commands.impl.ts`** -> AI Confidence: **99.34%**
29. **`packages/nx/src/project-graph/utils/project-configuration/target-merging.ts`** -> AI Confidence: **99.34%**
30. **`packages/nx/src/tasks-runner/create-task-graph.ts`** -> AI Confidence: **99.34%**
31. **`packages/rspack/src/plugins/utils/plugins/normalize-options.ts`** -> AI Confidence: **99.34%**
32. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/normalize-options.ts`** -> AI Confidence: **99.34%**
33. **`packages/workspace/src/generators/preset/preset.ts`** -> AI Confidence: **99.34%**
34. **`scripts/copy.js`** -> AI Confidence: **99.32%**
35. **`packages/jest/src/executors/jest/summary.ts`** -> AI Confidence: **99.32%**
36. **`packages/jest/src/utils/config/get-jest-projects.ts`** -> AI Confidence: **99.32%**
37. **`packages/js/src/utils/typescript/plugin.ts`** -> AI Confidence: **99.32%**
38. **`packages/nx/src/migrations/update-16-0-0/update-depends-on-to-tokens.ts`** -> AI Confidence: **99.32%**
39. **`packages/nx/src/utils/git-utils.tree-filter.ts`** -> AI Confidence: **99.32%**
40. **`astro-docs/src/plugins/plugin.loader.ts`** -> AI Confidence: **99.31%**
41. **`astro-docs/src/plugins/utils/devkit-generation.ts`** -> AI Confidence: **99.31%**
42. **`e2e/utils/command-utils.ts`** -> AI Confidence: **99.31%**
43. **`e2e/utils/ensure-browser-installation.ts`** -> AI Confidence: **99.31%**
44. **`e2e/utils/global-setup.ts`** -> AI Confidence: **99.31%**
45. **`graph/migrate/src/lib/components/migration-card.tsx`** -> AI Confidence: **99.31%**
46. **`graph/ui-project-details/src/lib/project-details/project-details.tsx`** -> AI Confidence: **99.31%**
47. **`graph/ui-project-details/src/lib/show-all-options/show-options-help.tsx`** -> AI Confidence: **99.31%**
48. **`graph/ui-project-details/src/lib/target-configuration-details-header/target-configuration-details-header.tsx`** -> AI Confidence: **99.31%**
49. **`graph/ui-project-details/src/lib/target-configuration-details/target-configuration-details.tsx`** -> AI Confidence: **99.31%**
50. **`nx-dev/feature-package-schema-viewer/src/lib/parameter-view.tsx`** -> AI Confidence: **99.31%**
51. **`nx-dev/nx-dev/pages/changelog.tsx`** -> AI Confidence: **99.31%**
52. **`nx-dev/ui-common/src/lib/sidebar.tsx`** -> AI Confidence: **99.31%**
53. **`nx-dev/ui-fence/src/lib/fence.tsx`** -> AI Confidence: **99.31%**
54. **`packages/angular-rspack/src/lib/config/config-utils/dev-server-config-utils.ts`** -> AI Confidence: **99.31%**
55. **`packages/angular-rspack/src/lib/config/i18n/create-i18n-options.ts`** -> AI Confidence: **99.31%**
56. **`packages/angular-rspack/src/lib/models/normalize-options.ts`** -> AI Confidence: **99.31%**
57. **`packages/angular-rspack/src/lib/plugins/angular-rspack-plugin.ts`** -> AI Confidence: **99.31%**
58. **`packages/angular-rspack/src/lib/plugins/i18n-inline-plugin.ts`** -> AI Confidence: **99.31%**
59. **`packages/angular-rspack/src/lib/plugins/ng-rspack.ts`** -> AI Confidence: **99.31%**
60. **`packages/angular-rspack/src/lib/plugins/prerender-plugin.ts`** -> AI Confidence: **99.31%**
61. **`packages/angular-rspack/src/lib/utils/stats.ts`** -> AI Confidence: **99.31%**
62. **`packages/angular/src/executors/utilities/ng-packagr/stylesheet-processor.ts`** -> AI Confidence: **99.31%**
63. **`packages/angular/src/generators/application/lib/create-files.ts`** -> AI Confidence: **99.31%**
64. **`packages/angular/src/generators/host/host.ts`** -> AI Confidence: **99.31%**
65. **`packages/angular/src/generators/library/lib/normalize-options.ts`** -> AI Confidence: **99.31%**
66. **`packages/angular/src/generators/ng-add/migrators/projects/e2e.migrator.ts`** -> AI Confidence: **99.31%**
67. **`packages/angular/src/generators/ng-add/utilities/workspace.ts`** -> AI Confidence: **99.31%**
68. **`packages/angular/src/generators/ngrx-feature-store/lib/add-imports.ts`** -> AI Confidence: **99.31%**
69. **`packages/angular/src/generators/ngrx/lib/add-imports-to-module.ts`** -> AI Confidence: **99.31%**
70. **`packages/angular/src/generators/remote/lib/update-ssr-setup.ts`** -> AI Confidence: **99.31%**
71. **`packages/angular/src/generators/remote/remote.ts`** -> AI Confidence: **99.31%**
72. **`packages/angular/src/generators/setup-mf/lib/add-remote-to-host.ts`** -> AI Confidence: **99.31%**
73. **`packages/angular/src/generators/setup-ssr/lib/generate-files.ts`** -> AI Confidence: **99.31%**
74. **`packages/angular/src/migrations/update-17-1-0/replace-nguniversal-engines.ts`** -> AI Confidence: **99.31%**
75. **`packages/angular/src/migrations/update-21-5-0/utils/karma-config-comparer.ts`** -> AI Confidence: **99.31%**
76. **`packages/angular/src/migrations/update-22-3-0/update-ssr-webpack-config.ts`** -> AI Confidence: **99.31%**
77. **`packages/angular/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
78. **`packages/angular/src/utils/nx-devkit/ast-utils.ts`** -> AI Confidence: **99.31%**
79. **`packages/create-nx-workspace/bin/create-nx-workspace.ts`** -> AI Confidence: **99.31%**
80. **`packages/create-nx-workspace/src/create-empty-workspace.ts`** -> AI Confidence: **99.31%**
81. **`packages/create-nx-workspace/src/create-sandbox.ts`** -> AI Confidence: **99.31%**
82. **`packages/create-nx-workspace/src/create-workspace.ts`** -> AI Confidence: **99.31%**
83. **`packages/create-nx-workspace/src/utils/nx/ab-testing.ts`** -> AI Confidence: **99.31%**
84. **`packages/cypress/src/generators/component-configuration/component-configuration.ts`** -> AI Confidence: **99.31%**
85. **`packages/cypress/src/generators/convert-to-inferred/convert-to-inferred.spec.ts`** -> AI Confidence: **99.31%**
86. **`packages/cypress/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
87. **`packages/cypress/src/generators/migrate-to-cypress-11/conversion.util.ts`** -> AI Confidence: **99.31%**
88. **`packages/cypress/src/migrations/update-20-8-0/replace-experimental-just-in-time-compile.ts`** -> AI Confidence: **99.31%**
89. **`packages/cypress/src/migrations/update-22-1-0/update-angular-component-testing-support.ts`** -> AI Confidence: **99.31%**
90. **`packages/cypress/src/plugins/plugin.spec.ts`** -> AI Confidence: **99.31%**
91. **`packages/cypress/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
92. **`packages/detox/src/executors/test/test.impl.ts`** -> AI Confidence: **99.31%**
93. **`packages/detox/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
94. **`packages/devkit/src/utils/catalog/pnpm-manager.ts`** -> AI Confidence: **99.31%**
95. **`packages/devkit/src/utils/catalog/yarn-manager.ts`** -> AI Confidence: **99.31%**
96. **`packages/devkit/src/utils/package-json.ts`** -> AI Confidence: **99.31%**
97. **`packages/esbuild/src/executors/esbuild/lib/build-esbuild-options.ts`** -> AI Confidence: **99.31%**
98. **`packages/esbuild/src/executors/esbuild/lib/normalize.ts`** -> AI Confidence: **99.31%**
99. **`packages/esbuild/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
100. **`packages/eslint-plugin/src/resolve-workspace-rules.ts`** -> AI Confidence: **99.31%**
101. **`packages/eslint-plugin/src/rules/dependency-checks.ts`** -> AI Confidence: **99.31%**
102. **`packages/eslint-plugin/src/rules/nx-plugin-checks.ts`** -> AI Confidence: **99.31%**
103. **`packages/eslint-plugin/src/utils/ast-utils.ts`** -> AI Confidence: **99.31%**
104. **`packages/eslint/src/executors/lint/lint.impl.ts`** -> AI Confidence: **99.31%**
105. **`packages/eslint/src/generators/convert-to-flat-config/generator.ts`** -> AI Confidence: **99.31%**
106. **`packages/eslint/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
107. **`packages/eslint/src/generators/init/init-migration.ts`** -> AI Confidence: **99.31%**
108. **`packages/eslint/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
109. **`packages/eslint/src/generators/lint-project/lint-project.ts`** -> AI Confidence: **99.31%**
110. **`packages/eslint/src/generators/utils/flat-config/ast-utils.ts`** -> AI Confidence: **99.31%**
111. **`packages/expo/plugins/metro-resolver.ts`** -> AI Confidence: **99.31%**
112. **`packages/expo/plugins/plugin.ts`** -> AI Confidence: **99.31%**
113. **`packages/expo/src/executors/run/run.impl.ts`** -> AI Confidence: **99.31%**
114. **`packages/expo/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
115. **`packages/gradle/src/executors/gradle/gradle-batch.impl.ts`** -> AI Confidence: **99.31%**
116. **`packages/gradle/src/plugin-v1/nodes.ts`** -> AI Confidence: **99.31%**
117. **`packages/gradle/src/plugin-v1/utils/get-gradle-report.ts`** -> AI Confidence: **99.31%**
118. **`packages/gradle/src/plugin/nodes.ts`** -> AI Confidence: **99.31%**
119. **`packages/jest/src/executors/jest/jest.impl.ts`** -> AI Confidence: **99.31%**
120. **`packages/jest/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
121. **`packages/jest/src/migrations/update-22-2-0/convert-jest-config-to-cjs.ts`** -> AI Confidence: **99.31%**
122. **`packages/jest/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
123. **`packages/js/src/executors/prune-lockfile/prune-lockfile.ts`** -> AI Confidence: **99.31%**
124. **`packages/js/src/executors/verdaccio/verdaccio.impl.ts`** -> AI Confidence: **99.31%**
125. **`packages/js/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
126. **`packages/js/src/generators/library/library.ts`** -> AI Confidence: **99.31%**
127. **`packages/js/src/generators/setup-build/generator.ts`** -> AI Confidence: **99.31%**
128. **`packages/js/src/plugins/typescript/plugin.ts`** -> AI Confidence: **99.31%**
129. **`packages/js/src/utils/buildable-libs-utils.ts`** -> AI Confidence: **99.31%**
130. **`packages/js/src/utils/generate-globs.ts`** -> AI Confidence: **99.31%**
131. **`packages/js/src/utils/typescript/ts-solution-setup.ts`** -> AI Confidence: **99.31%**
132. **`packages/maven/src/executors/maven/maven-batch.impl.ts`** -> AI Confidence: **99.31%**
133. **`packages/maven/src/plugins/maven-analyzer.ts`** -> AI Confidence: **99.31%**
134. **`packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
135. **`packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-ssr-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
136. **`packages/module-federation/src/plugins/nx-module-federation-plugin/rspack/nx-module-federation-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
137. **`packages/module-federation/src/plugins/nx-module-federation-plugin/rspack/nx-module-federation-ssr-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
138. **`packages/module-federation/src/utils/get-remotes-for-host.ts`** -> AI Confidence: **99.31%**
139. **`packages/module-federation/src/utils/start-remote-proxies.ts`** -> AI Confidence: **99.31%**
140. **`packages/module-federation/src/utils/start-ssr-remote-proxies.ts`** -> AI Confidence: **99.31%**
141. **`packages/next/plugins/component-testing.ts`** -> AI Confidence: **99.31%**
142. **`packages/next/src/executors/server/server.impl.ts`** -> AI Confidence: **99.31%**
143. **`packages/next/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
144. **`packages/next/src/generators/application/lib/create-application-files.ts`** -> AI Confidence: **99.31%**
145. **`packages/next/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
146. **`packages/node/src/generators/library/library.ts`** -> AI Confidence: **99.31%**
147. **`packages/nuxt/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
148. **`packages/nuxt/src/utils/add-linting.ts`** -> AI Confidence: **99.31%**
149. **`packages/nx/bin/init-local.ts`** -> AI Confidence: **99.31%**
150. **`packages/nx/src/adapter/ngcli-adapter.ts`** -> AI Confidence: **99.31%**
151. **`packages/nx/src/ai/set-up-ai-agents/set-up-ai-agents.ts`** -> AI Confidence: **99.31%**
152. **`packages/nx/src/ai/utils.ts`** -> AI Confidence: **99.31%**
153. **`packages/nx/src/analytics/analytics.ts`** -> AI Confidence: **99.31%**
154. **`packages/nx/src/command-line/generate/generate.ts`** -> AI Confidence: **99.31%**
155. **`packages/nx/src/command-line/generate/generator-utils.ts`** -> AI Confidence: **99.31%**
156. **`packages/nx/src/command-line/graph/graph.ts`** -> AI Confidence: **99.31%**
157. **`packages/nx/src/command-line/init/configure-plugins.ts`** -> AI Confidence: **99.31%**
158. **`packages/nx/src/command-line/init/implementation/add-nx-to-monorepo.ts`** -> AI Confidence: **99.31%**
159. **`packages/nx/src/command-line/init/implementation/add-nx-to-npm-repo.ts`** -> AI Confidence: **99.31%**
160. **`packages/nx/src/command-line/init/implementation/angular/index.ts`** -> AI Confidence: **99.31%**
161. **`packages/nx/src/command-line/init/implementation/check-compatible-with-plugins.ts`** -> AI Confidence: **99.31%**
162. **`packages/nx/src/command-line/init/init-v2.ts`** -> AI Confidence: **99.31%**
163. **`packages/nx/src/command-line/migrate/migrate.ts`** -> AI Confidence: **99.31%**
164. **`packages/nx/src/command-line/reset/reset.ts`** -> AI Confidence: **99.31%**
165. **`packages/nx/src/command-line/run/executor-utils.ts`** -> AI Confidence: **99.31%**
166. **`packages/nx/src/command-line/show/project.ts`** -> AI Confidence: **99.31%**
167. **`packages/nx/src/config/nx-json.ts`** -> AI Confidence: **99.31%**
168. **`packages/nx/src/generators/utils/project-configuration.ts`** -> AI Confidence: **99.31%**
169. **`packages/nx/src/hasher/hash-task.ts`** -> AI Confidence: **99.31%**
170. **`packages/nx/src/hasher/native-task-hasher-impl.ts`** -> AI Confidence: **99.31%**
171. **`packages/nx/src/hasher/task-hasher.ts`** -> AI Confidence: **99.31%**
172. **`packages/nx/src/migrations/update-15-0-0/prefix-outputs.ts`** -> AI Confidence: **99.31%**
173. **`packages/nx/src/migrations/update-16-2-0/remove-run-commands-output-path.ts`** -> AI Confidence: **99.31%**
174. **`packages/nx/src/migrations/update-17-0-0/rm-default-collection-npm-scope.ts`** -> AI Confidence: **99.31%**
175. **`packages/nx/src/migrations/update-17-0-0/use-minimal-config-for-tasks-runner-options.ts`** -> AI Confidence: **99.31%**
176. **`packages/nx/src/migrations/update-19-2-4/set-project-name.ts`** -> AI Confidence: **99.31%**
177. **`packages/nx/src/migrations/update-22-0-0/consolidate-release-tag-config.ts`** -> AI Confidence: **99.31%**
178. **`packages/nx/src/nx-cloud/generators/connect-to-nx-cloud/connect-to-nx-cloud.ts`** -> AI Confidence: **99.31%**
179. **`packages/nx/src/plugins/js/lock-file/bun-parser.ts`** -> AI Confidence: **99.31%**
180. **`packages/nx/src/plugins/js/lock-file/npm-parser.ts`** -> AI Confidence: **99.31%**
181. **`packages/nx/src/plugins/js/lock-file/project-graph-pruning.ts`** -> AI Confidence: **99.31%**
182. **`packages/nx/src/plugins/js/lock-file/yarn-parser.ts`** -> AI Confidence: **99.31%**
183. **`packages/nx/src/plugins/js/package-json/create-package-json.ts`** -> AI Confidence: **99.31%**
184. **`packages/nx/src/plugins/js/project-graph/affected/npm-packages.ts`** -> AI Confidence: **99.31%**
185. **`packages/nx/src/plugins/js/project-graph/build-dependencies/explicit-project-dependencies.ts`** -> AI Confidence: **99.31%**
186. **`packages/nx/src/plugins/js/project-graph/build-dependencies/target-project-locator.ts`** -> AI Confidence: **99.31%**
187. **`packages/nx/src/plugins/package-json/create-nodes.ts`** -> AI Confidence: **99.31%**
188. **`packages/nx/src/project-graph/build-project-graph.ts`** -> AI Confidence: **99.31%**
189. **`packages/nx/src/project-graph/nx-deps-cache.ts`** -> AI Confidence: **99.31%**
190. **`packages/nx/src/project-graph/plugins/get-plugins.ts`** -> AI Confidence: **99.31%**
191. **`packages/nx/src/project-graph/plugins/resolve-plugin.ts`** -> AI Confidence: **99.31%**
192. **`packages/nx/src/project-graph/project-graph.ts`** -> AI Confidence: **99.31%**
193. **`packages/nx/src/project-graph/utils/project-configuration-utils.ts`** -> AI Confidence: **99.31%**
194. **`packages/nx/src/tasks-runner/life-cycles/dynamic-run-many-terminal-output-life-cycle.ts`** -> AI Confidence: **99.31%**
195. **`packages/nx/src/tasks-runner/life-cycles/task-history-life-cycle-old.ts`** -> AI Confidence: **99.31%**
196. **`packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.ts`** -> AI Confidence: **99.31%**
197. **`packages/nx/src/tasks-runner/run-command.ts`** -> AI Confidence: **99.31%**
198. **`packages/nx/src/tasks-runner/task-orchestrator.ts`** -> AI Confidence: **99.31%**
199. **`packages/nx/src/utils/analytics-prompt.ts`** -> AI Confidence: **99.31%**
200. **`packages/nx/src/utils/catalog/pnpm-manager.ts`** -> AI Confidence: **99.31%**
201. **`packages/nx/src/utils/catalog/yarn-manager.ts`** -> AI Confidence: **99.31%**
202. **`packages/nx/src/utils/child-process.ts`** -> AI Confidence: **99.31%**
203. **`packages/nx/src/utils/command-line-utils.ts`** -> AI Confidence: **99.31%**
204. **`packages/nx/src/utils/package-json.ts`** -> AI Confidence: **99.31%**
205. **`packages/nx/src/utils/package-manager.ts`** -> AI Confidence: **99.31%**
206. **`packages/nx/src/utils/plugins/local-plugins.ts`** -> AI Confidence: **99.31%**
207. **`packages/nx/src/utils/plugins/output.ts`** -> AI Confidence: **99.31%**
208. **`packages/nx/src/utils/plugins/plugin-capabilities.ts`** -> AI Confidence: **99.31%**
209. **`packages/nx/src/utils/print-help.ts`** -> AI Confidence: **99.31%**
210. **`packages/nx/src/utils/sync-generators.ts`** -> AI Confidence: **99.31%**
211. **`packages/playwright/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
212. **`packages/plugin/src/generators/lint-checks/generator.ts`** -> AI Confidence: **99.31%**
213. **`packages/plugin/src/generators/migration/migration.ts`** -> AI Confidence: **99.31%**
214. **`packages/react-native/plugins/metro-resolver.ts`** -> AI Confidence: **99.31%**
215. **`packages/react-native/plugins/plugin.ts`** -> AI Confidence: **99.31%**
216. **`packages/react/src/executors/module-federation-dev-server/module-federation-dev-server.impl.ts`** -> AI Confidence: **99.31%**
217. **`packages/react/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.31%**
218. **`packages/react/src/executors/module-federation-static-server/module-federation-static-server.impl.ts`** -> AI Confidence: **99.31%**
219. **`packages/react/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
220. **`packages/react/src/generators/component-story/component-story.ts`** -> AI Confidence: **99.31%**
221. **`packages/react/src/generators/library/lib/add-rollup-build-target.ts`** -> AI Confidence: **99.31%**
222. **`packages/react/src/generators/remote/remote.ts`** -> AI Confidence: **99.31%**
223. **`packages/react/src/generators/setup-ssr/setup-ssr.ts`** -> AI Confidence: **99.31%**
224. **`packages/react/src/generators/stories/stories.ts`** -> AI Confidence: **99.31%**
225. **`packages/react/src/plugins/router-plugin.ts`** -> AI Confidence: **99.31%**
226. **`packages/react/src/utils/ast-utils.ts`** -> AI Confidence: **99.31%**
227. **`packages/react/src/utils/ct-utils.ts`** -> AI Confidence: **99.31%**
228. **`packages/remix/generators.ts`** -> AI Confidence: **99.31%**
229. **`packages/remix/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
230. **`packages/rollup/src/executors/rollup/rollup.impl.ts`** -> AI Confidence: **99.31%**
231. **`packages/rollup/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
232. **`packages/rollup/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
233. **`packages/rspack/src/executors/dev-server/lib/get-dev-server-config.ts`** -> AI Confidence: **99.31%**
234. **`packages/rspack/src/executors/module-federation-dev-server/module-federation-dev-server.impl.ts`** -> AI Confidence: **99.31%**
235. **`packages/rspack/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.31%**
236. **`packages/rspack/src/executors/module-federation-static-server/module-federation-static-server.impl.ts`** -> AI Confidence: **99.31%**
237. **`packages/rspack/src/executors/rspack/lib/config.ts`** -> AI Confidence: **99.31%**
238. **`packages/rspack/src/executors/rspack/rspack.impl.ts`** -> AI Confidence: **99.31%**
239. **`packages/rspack/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
240. **`packages/rspack/src/generators/convert-config-to-rspack-plugin/convert-config-to-rspack-plugin.ts`** -> AI Confidence: **99.31%**
241. **`packages/rspack/src/generators/convert-to-inferred/utils/build-post-target-transformer.ts`** -> AI Confidence: **99.31%**
242. **`packages/rspack/src/generators/convert-to-inferred/utils/serve-post-target-transformer.ts`** -> AI Confidence: **99.31%**
243. **`packages/rspack/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
244. **`packages/rspack/src/plugins/utils/apply-web-config.ts`** -> AI Confidence: **99.31%**
245. **`packages/rspack/src/plugins/utils/plugins/nx-tsconfig-paths-rspack-plugin.ts`** -> AI Confidence: **99.31%**
246. **`packages/rspack/src/plugins/write-index-html-plugin.ts`** -> AI Confidence: **99.31%**
247. **`packages/rspack/src/utils/generator-utils.ts`** -> AI Confidence: **99.31%**
248. **`packages/storybook/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
249. **`packages/storybook/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
250. **`packages/storybook/src/utils/utilities.ts`** -> AI Confidence: **99.31%**
251. **`packages/vite/plugins/nx-tsconfig-paths.plugin.ts`** -> AI Confidence: **99.31%**
252. **`packages/vite/src/executors/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.31%**
253. **`packages/vite/src/executors/preview-server/preview-server.impl.ts`** -> AI Confidence: **99.31%**
254. **`packages/vite/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
255. **`packages/vitest/src/executors/test/vitest.impl.ts`** -> AI Confidence: **99.31%**
256. **`packages/vitest/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
257. **`packages/vitest/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
258. **`packages/vue/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
259. **`packages/vue/src/generators/component/lib/utils.ts`** -> AI Confidence: **99.31%**
260. **`packages/vue/src/utils/add-linting.ts`** -> AI Confidence: **99.31%**
261. **`packages/web/src/executors/file-server/file-server.impl.ts`** -> AI Confidence: **99.31%**
262. **`packages/webpack/src/executors/dev-server/lib/get-dev-server-config.ts`** -> AI Confidence: **99.31%**
263. **`packages/webpack/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
264. **`packages/webpack/src/generators/convert-config-to-webpack-plugin/convert-config-to-webpack-plugin.ts`** -> AI Confidence: **99.31%**
265. **`packages/webpack/src/generators/convert-to-inferred/utils/build-post-target-transformer.ts`** -> AI Confidence: **99.31%**
266. **`packages/webpack/src/generators/convert-to-inferred/utils/serve-post-target-transformer.ts`** -> AI Confidence: **99.31%**
267. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/apply-base-config.ts`** -> AI Confidence: **99.31%**
268. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/apply-web-config.ts`** -> AI Confidence: **99.31%**
269. **`packages/webpack/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
270. **`packages/webpack/src/plugins/write-index-html-plugin.ts`** -> AI Confidence: **99.31%**
271. **`packages/workspace/src/generators/move/lib/update-imports.ts`** -> AI Confidence: **99.31%**
272. **`packages/workspace/src/generators/new/generate-preset.ts`** -> AI Confidence: **99.31%**
273. **`scripts/documentation/package-schemas/package-metadata.ts`** -> AI Confidence: **99.31%**
274. **`scripts/issues-scraper/index.ts`** -> AI Confidence: **99.31%**
275. **`tools/documentation/create-embeddings/src/main.mts`** -> AI Confidence: **99.31%**
276. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/runner/GradleRunner.kt`** -> AI Confidence: **99.31%**
277. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/ProjectUtils.kt`** -> AI Confidence: **99.31%**
278. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/TaskUtils.kt`** -> AI Confidence: **99.31%**
279. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/KotlinAstTestParser.kt`** -> AI Confidence: **99.31%**
280. **`packages/maven/batch-runner-adapters/maven3/src/main/kotlin/dev/nx/maven/adapter/maven3/NxMaven3.kt`** -> AI Confidence: **99.31%**
281. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenInvokerRunner.kt`** -> AI Confidence: **99.31%**
282. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/NxTargetFactory.kt`** -> AI Confidence: **99.31%**
283. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/utils/MojoAnalyzer.kt`** -> AI Confidence: **99.31%**
284. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateRecorder.kt`** -> AI Confidence: **99.31%**
285. **`packages/nx/src/native/db/connection.rs`** -> AI Confidence: **99.31%**
286. **`packages/nx/src/native/db/initialize.rs`** -> AI Confidence: **99.31%**
287. **`packages/nx/src/native/ide/install.rs`** -> AI Confidence: **99.31%**
288. **`packages/nx/src/native/pseudo_terminal/command/unix.rs`** -> AI Confidence: **99.31%**
289. **`packages/nx/src/native/tasks/hash_planner.rs`** -> AI Confidence: **99.31%**
290. **`packages/nx/src/native/tui/tui_core.rs`** -> AI Confidence: **99.31%**
291. **`graph/client/src/assets/release-static/environment.js`** -> AI Confidence: **99.29%**
292. **`jest.preset.js`** -> AI Confidence: **99.29%**
293. **`nx-dev/nx-dev/next-sitemap.config.js`** -> AI Confidence: **99.29%**
294. **`scripts/check-lock-files.js`** -> AI Confidence: **99.29%**
295. **`scripts/check-react-native-changes.js`** -> AI Confidence: **99.29%**
296. **`scripts/commitizen.js`** -> AI Confidence: **99.29%**
297. **`scripts/migrate-to-pnpm-version.js`** -> AI Confidence: **99.29%**
298. **`scripts/run-native-target.js`** -> AI Confidence: **99.29%**
299. **`scripts/submit-plugin.js`** -> AI Confidence: **99.29%**
300. **`scripts/validate-pr-title.js`** -> AI Confidence: **99.29%**
301. **`tools/documentation/create-embeddings/jest.preset.js`** -> AI Confidence: **99.29%**
302. **`e2e/remix/src/remix-ts-solution.test.ts`** -> AI Confidence: **99.29%**
303. **`graph/ui-project-details/src/lib/utils/get-display-header-from-target-configuration.ts`** -> AI Confidence: **99.29%**
304. **`packages/angular-rspack-compiler/src/utils/targets-from-browsers.ts`** -> AI Confidence: **99.29%**
305. **`packages/angular/src/builders/dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
306. **`packages/angular/src/executors/module-federation-dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
307. **`packages/angular/src/generators/library/lib/normalized-schema.ts`** -> AI Confidence: **99.29%**
308. **`packages/angular/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
309. **`packages/angular/src/generators/utils/add-mf-env-to-inputs.ts`** -> AI Confidence: **99.29%**
310. **`packages/angular/src/migrations/update-17-1-0/replace-nguniversal-builders.ts`** -> AI Confidence: **99.29%**
311. **`packages/create-nx-workspace/src/utils/ci/is-ci.ts`** -> AI Confidence: **99.29%**
312. **`packages/detox/src/executors/test/schema.d.ts`** -> AI Confidence: **99.29%**
313. **`packages/devkit/src/utils/replace-project-configuration-with-plugin.ts`** -> AI Confidence: **99.29%**
314. **`packages/expo/src/executors/build-list/build-fragment.d.ts`** -> AI Confidence: **99.29%**
315. **`packages/expo/src/executors/build-list/schema.d.ts`** -> AI Confidence: **99.29%**
316. **`packages/expo/src/executors/export/schema.d.ts`** -> AI Confidence: **99.29%**
317. **`packages/expo/src/executors/start/schema.d.ts`** -> AI Confidence: **99.29%**
318. **`packages/expo/src/migrations/update-21-4-0/update-splash-screen-config.ts`** -> AI Confidence: **99.29%**
319. **`packages/expo/src/utils/resolve-eas.ts`** -> AI Confidence: **99.29%**
320. **`packages/jest/src/executors/jest/schema.d.ts`** -> AI Confidence: **99.29%**
321. **`packages/jest/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
322. **`packages/js/src/executors/release-publish/schema.d.ts`** -> AI Confidence: **99.29%**
323. **`packages/js/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
324. **`packages/node/src/generators/application/schema.d.ts`** -> AI Confidence: **99.29%**
325. **`packages/node/src/generators/e2e-project/schema.d.ts`** -> AI Confidence: **99.29%**
326. **`packages/node/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
327. **`packages/nx/src/native/assert-supported-platform.ts`** -> AI Confidence: **99.29%**
328. **`packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
329. **`packages/nx/src/plugins/js/lock-file/__fixtures__/optional/yarn.lock.ts`** -> AI Confidence: **99.29%**
330. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock-v6.yaml.ts`** -> AI Confidence: **99.29%**
331. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock-v9.yaml.ts`** -> AI Confidence: **99.29%**
332. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
333. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock-v6.yaml.ts`** -> AI Confidence: **99.29%**
334. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock-v9.yaml.ts`** -> AI Confidence: **99.29%**
335. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
336. **`packages/nx/src/plugins/js/project-graph/build-dependencies/strip-source-code.ts`** -> AI Confidence: **99.29%**
337. **`packages/nx/src/tasks-runner/life-cycles/pretty-time.ts`** -> AI Confidence: **99.29%**
338. **`packages/nx/src/utils/git-utils.index-filter.ts`** -> AI Confidence: **99.29%**
339. **`packages/playwright/src/executors/playwright/playwright.impl.ts`** -> AI Confidence: **99.29%**
340. **`packages/plugin/src/generators/plugin/schema.d.ts`** -> AI Confidence: **99.29%**
341. **`packages/react-native/src/generators/init/lib/gitignore-entries.ts`** -> AI Confidence: **99.29%**
342. **`packages/react/babel.ts`** -> AI Confidence: **99.29%**
343. **`packages/react/src/rules/update-module-federation-project.ts`** -> AI Confidence: **99.29%**
344. **`packages/react/src/utils/add-mf-env-to-inputs.ts`** -> AI Confidence: **99.29%**
345. **`packages/remix/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
346. **`packages/rollup/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
347. **`packages/storybook/src/generators/convert-to-inferred/lib/serve-post-target-transformer.ts`** -> AI Confidence: **99.29%**
348. **`packages/vite/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
349. **`packages/vite/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
350. **`packages/vite/src/generators/vitest/schema.d.ts`** -> AI Confidence: **99.29%**
351. **`packages/vite/src/utils/e2e-web-server-info-utils.ts`** -> AI Confidence: **99.29%**
352. **`packages/vitest/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
353. **`packages/vitest/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
354. **`packages/web/src/executors/file-server/schema.d.ts`** -> AI Confidence: **99.29%**
355. **`packages/web/src/generators/application/schema.d.ts`** -> AI Confidence: **99.29%**
356. **`packages/webpack/src/executors/dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
357. **`packages/webpack/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
358. **`packages/webpack/src/migrations/update-22-0-0/remove-deprecated-options.ts`** -> AI Confidence: **99.29%**
359. **`packages/workspace/src/generators/move/lib/update-owners-and-conformance.ts`** -> AI Confidence: **99.29%**
360. **`packages/workspace/src/generators/preset/schema.d.ts`** -> AI Confidence: **99.29%**
361. **`scripts/release-docs.ts`** -> AI Confidence: **99.29%**
362. **`tools/eslint-rules/rules/ensure-pnpm-lock-version.ts`** -> AI Confidence: **99.29%**
363. **`mvnw`** -> AI Confidence: **99.29%**
364. **`packages/react-native/src/generators/application/files/app/android/gradlew.template`** -> AI Confidence: **99.29%**
365. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/TestClassParser.kt`** -> AI Confidence: **99.29%**
366. **`packages/nx/src/native/utils/ci.rs`** -> AI Confidence: **99.29%**
367. **`packages/js/src/plugins/typescript/util.ts`** -> AI Confidence: **99.25%**
368. **`packages/nx/src/native/native-bindings.js`** -> AI Confidence: **99.24%**
369. **`e2e/nx/src/graph-ts-solution.test.ts`** -> AI Confidence: **99.24%**
370. **`graph/migrate/src/lib/components/migration-timeline.tsx`** -> AI Confidence: **99.24%**
371. **`nx-dev/feature-ai/src/lib/feed-container.tsx`** -> AI Confidence: **99.24%**
372. **`nx-dev/feature-doc-viewer/src/lib/doc-viewer.tsx`** -> AI Confidence: **99.24%**
373. **`nx-dev/feature-package-schema-viewer/src/lib/content.tsx`** -> AI Confidence: **99.24%**
374. **`nx-dev/feature-search/src/lib/algolia-search.tsx`** -> AI Confidence: **99.24%**
375. **`nx-dev/ui-blog/src/lib/blog-details.tsx`** -> AI Confidence: **99.24%**
376. **`nx-dev/ui-common/src/lib/headers/documentation-header.tsx`** -> AI Confidence: **99.24%**
377. **`nx-dev/ui-common/src/lib/headers/header.tsx`** -> AI Confidence: **99.24%**
378. **`nx-dev/ui-courses/src/lib/course-details.tsx`** -> AI Confidence: **99.24%**
379. **`packages/angular-rspack/src/lib/config/config-utils/common-config.ts`** -> AI Confidence: **99.24%**
380. **`packages/angular-rspack/src/lib/config/config-utils/style-config-utils.ts`** -> AI Confidence: **99.24%**
381. **`packages/angular-rspack/src/lib/plugins/index-html-plugin.ts`** -> AI Confidence: **99.24%**
382. **`packages/angular/src/builders/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.24%**
383. **`packages/angular/src/builders/webpack-browser/webpack-browser.impl.ts`** -> AI Confidence: **99.24%**
384. **`packages/angular/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.24%**
385. **`packages/angular/src/generators/add-linting/add-linting.ts`** -> AI Confidence: **99.24%**
386. **`packages/angular/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
387. **`packages/create-nx-workspace/src/internal-utils/prompts.ts`** -> AI Confidence: **99.24%**
388. **`packages/devkit/src/generators/plugin-migrations/executor-to-plugin-migrator.ts`** -> AI Confidence: **99.24%**
389. **`packages/esbuild/src/executors/esbuild/esbuild.impl.ts`** -> AI Confidence: **99.24%**
390. **`packages/eslint-plugin/src/rules/enforce-module-boundaries.ts`** -> AI Confidence: **99.24%**
391. **`packages/eslint-plugin/src/utils/project-graph-utils.ts`** -> AI Confidence: **99.24%**
392. **`packages/eslint-plugin/src/utils/runtime-lint-utils.ts`** -> AI Confidence: **99.24%**
393. **`packages/eslint/src/generators/utils/eslint-file.ts`** -> AI Confidence: **99.24%**
394. **`packages/eslint/src/generators/workspace-rule/workspace-rule.ts`** -> AI Confidence: **99.24%**
395. **`packages/expo/src/executors/install/install.impl.ts`** -> AI Confidence: **99.24%**
396. **`packages/expo/src/generators/library/library.ts`** -> AI Confidence: **99.24%**
397. **`packages/js/src/executors/node/node.impl.ts`** -> AI Confidence: **99.24%**
398. **`packages/js/src/executors/swc/swc.impl.ts`** -> AI Confidence: **99.24%**
399. **`packages/maven/src/plugins/nodes.ts`** -> AI Confidence: **99.24%**
400. **`packages/next/src/generators/application/lib/add-linting.ts`** -> AI Confidence: **99.24%**
401. **`packages/node/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
402. **`packages/nuxt/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
403. **`packages/nx/src/command-line/format/format.ts`** -> AI Confidence: **99.24%**
404. **`packages/nx/src/command-line/import/import.ts`** -> AI Confidence: **99.24%**
405. **`packages/nx/src/command-line/init/implementation/add-nx-to-nest.ts`** -> AI Confidence: **99.24%**
406. **`packages/nx/src/command-line/init/implementation/angular/legacy-angular-versions.ts`** -> AI Confidence: **99.24%**
407. **`packages/nx/src/command-line/run/run-one.ts`** -> AI Confidence: **99.24%**
408. **`packages/nx/src/config/misc-interfaces.ts`** -> AI Confidence: **99.24%**
409. **`packages/nx/src/daemon/client/client.ts`** -> AI Confidence: **99.24%**
410. **`packages/nx/src/daemon/server/server.ts`** -> AI Confidence: **99.24%**
411. **`packages/nx/src/daemon/socket-utils.ts`** -> AI Confidence: **99.24%**
412. **`packages/nx/src/executors/run-commands/running-tasks.ts`** -> AI Confidence: **99.24%**
413. **`packages/nx/src/nx-cloud/update-manager.ts`** -> AI Confidence: **99.24%**
414. **`packages/nx/src/plugins/js/index.ts`** -> AI Confidence: **99.24%**
415. **`packages/nx/src/plugins/js/lock-file/lock-file.ts`** -> AI Confidence: **99.24%**
416. **`packages/nx/src/plugins/js/utils/register.ts`** -> AI Confidence: **99.24%**
417. **`packages/nx/src/project-graph/plugins/isolation/isolated-plugin.ts`** -> AI Confidence: **99.24%**
418. **`packages/nx/src/project-graph/plugins/loaded-nx-plugin.ts`** -> AI Confidence: **99.24%**
419. **`packages/nx/src/tasks-runner/cache.ts`** -> AI Confidence: **99.24%**
420. **`packages/nx/src/tasks-runner/life-cycles/task-history-life-cycle.ts`** -> AI Confidence: **99.24%**
421. **`packages/nx/src/tasks-runner/pseudo-terminal.ts`** -> AI Confidence: **99.24%**
422. **`packages/nx/src/tasks-runner/running-tasks/node-child-process.ts`** -> AI Confidence: **99.24%**
423. **`packages/plugin/src/generators/e2e-project/e2e.ts`** -> AI Confidence: **99.24%**
424. **`packages/plugin/src/generators/executor/executor.ts`** -> AI Confidence: **99.24%**
425. **`packages/plugin/src/generators/plugin/plugin.ts`** -> AI Confidence: **99.24%**
426. **`packages/react-native/src/generators/library/library.ts`** -> AI Confidence: **99.24%**
427. **`packages/react/plugins/storybook/index.ts`** -> AI Confidence: **99.24%**
428. **`packages/react/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
429. **`packages/react/src/generators/component/component.ts`** -> AI Confidence: **99.24%**
430. **`packages/react/src/generators/cypress-component-configuration/lib/add-files.ts`** -> AI Confidence: **99.24%**
431. **`packages/react/src/generators/host/host.ts`** -> AI Confidence: **99.24%**
432. **`packages/react/src/generators/library/library.ts`** -> AI Confidence: **99.24%**
433. **`packages/react/src/generators/redux/redux.ts`** -> AI Confidence: **99.24%**
434. **`packages/remix/src/generators/application/application.impl.ts`** -> AI Confidence: **99.24%**
435. **`packages/remix/src/generators/route/route.impl.ts`** -> AI Confidence: **99.24%**
436. **`packages/rollup/src/generators/convert-to-inferred/convert-to-inferred.spec.ts`** -> AI Confidence: **99.24%**
437. **`packages/rspack/src/executors/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.24%**
438. **`packages/vite/src/generators/init/init.ts`** -> AI Confidence: **99.24%**
439. **`packages/vue/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
440. **`packages/vue/src/generators/library/library.ts`** -> AI Confidence: **99.24%**
441. **`packages/web/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
442. **`packages/webpack/src/executors/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.24%**
443. **`scripts/copy-built-package/index.ts`** -> AI Confidence: **99.24%**
444. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/Maven4AdapterInvoker.kt`** -> AI Confidence: **99.24%**
445. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/NxProjectAnalyzerMojo.kt`** -> AI Confidence: **99.24%**
446. **`packages/nx/src/native/cache/cache.rs`** -> AI Confidence: **99.24%**
447. **`astro-docs/src/plugins/utils/core-nx-plugin-generation.ts`** -> AI Confidence: **99.23%**
448. **`graph/project-details/src/lib/project-details-wrapper.tsx`** -> AI Confidence: **99.23%**
449. **`nx-dev/nx-dev/pages/whitepaper-fast-ci.tsx`** -> AI Confidence: **99.23%**
450. **`nx-dev/ui-common/src/lib/video-player/video-player.tsx`** -> AI Confidence: **99.23%**
451. **`packages/angular-rspack-compiler/src/compilation/setup-compilation.ts`** -> AI Confidence: **99.23%**
452. **`packages/angular/src/generators/application/lib/update-tsconfig-files.ts`** -> AI Confidence: **99.23%**
453. **`packages/angular/src/generators/component/lib/normalize-options.ts`** -> AI Confidence: **99.23%**
454. **`packages/angular/src/generators/setup-ssr/lib/add-server-file.ts`** -> AI Confidence: **99.23%**
455. **`packages/cypress/src/migrations/update-20-8-0/update-component-testing-mount-imports.ts`** -> AI Confidence: **99.23%**
456. **`packages/devkit/src/utils/replace-package.ts`** -> AI Confidence: **99.23%**
457. **`packages/docker/src/plugins/plugin.ts`** -> AI Confidence: **99.23%**
458. **`packages/dotnet/src/analyzer/analyzer-client.ts`** -> AI Confidence: **99.23%**
459. **`packages/eslint/src/executors/lint/utility/eslint-utils.ts`** -> AI Confidence: **99.23%**
460. **`packages/gradle/src/plugin/dependencies.ts`** -> AI Confidence: **99.23%**
461. **`packages/gradle/src/plugin/utils/get-project-graph-from-gradle-plugin.ts`** -> AI Confidence: **99.23%**
462. **`packages/jest/src/migrations/update-21-3-0/replace-removed-matcher-aliases.ts`** -> AI Confidence: **99.23%**
463. **`packages/js/src/utils/find-npm-dependencies.ts`** -> AI Confidence: **99.23%**
464. **`packages/js/src/utils/swc/compile-swc.ts`** -> AI Confidence: **99.23%**
465. **`packages/next/src/generators/convert-to-inferred/lib/build-post-target-transformer.ts`** -> AI Confidence: **99.23%**
466. **`packages/next/src/generators/custom-server/custom-server.ts`** -> AI Confidence: **99.23%**
467. **`packages/node/src/generators/application/lib/normalize-options.ts`** -> AI Confidence: **99.23%**
468. **`packages/nx/src/config/schema-utils.ts`** -> AI Confidence: **99.23%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `e2e/utils/global-setup.ts` -> **100.0%** Exposure
- `scripts/local-registry/populate-storage.js` -> **99.9999%** Exposure
- `packages/js/src/plugins/jest/start-local-registry.ts` -> **99.999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `210` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11731` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/nx/src/daemon/client/client.ts` (TYPESCRIPT) -> Cumulative Risk: **756.67**
- **Archetype:** `file_cluster_4` (Distance: 13.814 IQR)
- **Magnitude:** 128.86 | **LOC:** 1415 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 52.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `reconnectFileWatcher` (Impact: 47.4), `reconnectProjectGraphListener` (Impact: 45.4), `enabled` (Impact: 32.0)

### 2. `packages/nx/src/tasks-runner/running-tasks/batch-process.ts` (TYPESCRIPT) -> Cumulative Risk: **741.3**
- **Archetype:** `file_cluster_4` (Distance: 13.12 IQR)
- **Magnitude:** 18.06 | **LOC:** 134 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 34.6), `cb` (Impact: 9.2), `cb` (Impact: 6.0)

### 3. `packages/nx/src/tasks-runner/running-tasks/node-child-process.ts` (TYPESCRIPT) -> Cumulative Risk: **737.63**
- **Archetype:** `file_cluster_4` (Distance: 13.909 IQR)
- **Magnitude:** 27.11 | **LOC:** 205 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9112%)
- **Heaviest Functions:** `callback` (Impact: 19.2), `kill` (Impact: 8.3), `constructor` (Impact: 8.0)

### 4. `packages/nx/src/executors/run-commands/running-tasks.ts` (TYPESCRIPT) -> Cumulative Risk: **719.98**
- **Archetype:** `file_cluster_4` (Distance: 12.27 IQR)
- **Magnitude:** 41.6 | **LOC:** 723 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 53.8%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.961%)
- **Heaviest Functions:** `registerTaskProcessStart` (Impact: 51.8), `run` (Impact: 36.8), `processEnv` (Impact: 27.4)

### 5. `packages/rspack/src/plugins/utils/plugins/rspack-nx-build-coordination-plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **717.22**
- **Archetype:** `file_cluster_4` (Distance: 12.553 IQR)
- **Magnitude:** 16.42 | **LOC:** 115 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createFileWatcher` (Impact: 22.4), `constructor` (Impact: 9.5), `buildChangedProjects` (Impact: 8.2)

### 6. `graph/client/src/app/external-api-impl.ts` (TYPESCRIPT) -> Cumulative Risk: **697.38**
- **Archetype:** `file_cluster_4` (Distance: 12.521 IQR)
- **Magnitude:** 13.49 | **LOC:** 118 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.6162%)
- **Heaviest Functions:** `constructor` (Impact: 18.6), `openProjectDetails` (Impact: 5.6), `focusProject` (Impact: 4.1)

### 7. `packages/nx/src/internal-testing-utils/temp-fs.ts` (TYPESCRIPT) -> Cumulative Risk: **696.96**
- **Archetype:** `file_cluster_4` (Distance: 12.234 IQR)
- **Magnitude:** 19.17 | **LOC:** 143 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%), Cognitive Load (99.9975%)
- **Heaviest Functions:** `cleanup` (Impact: 7.7), `reset` (Impact: 7.7), `setWorkspaceRoot` (Impact: 6.1)

### 8. `packages/rspack/src/plugins/utils/plugins/postcss-cli-resources.ts` (TYPESCRIPT) -> Cumulative Risk: **689.5**
- **Archetype:** `file_cluster_4` (Distance: 11.418 IQR)
- **Magnitude:** 21.9 | **LOC:** 217 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5909%), Concurrency (97.7374%)
- **Heaviest Functions:** `resolve` (Impact: 32.6), `Once` (Impact: 32.2), `PostcssCliResources` (Impact: 28.4)

### 9. `packages/webpack/src/utils/webpack/plugins/postcss-cli-resources.ts` (TYPESCRIPT) -> Cumulative Risk: **689.5**
- **Archetype:** `file_cluster_4` (Distance: 11.445 IQR)
- **Magnitude:** 21.9 | **LOC:** 217 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5909%), Concurrency (97.7374%)
- **Heaviest Functions:** `resolve` (Impact: 32.6), `Once` (Impact: 32.2), `PostcssCliResources` (Impact: 28.4)

### 10. `packages/nx/src/executors/run-script/run-script.impl.ts` (TYPESCRIPT) -> Cumulative Risk: **688.57**
- **Archetype:** `file_cluster_4` (Distance: 11.662 IQR)
- **Magnitude:** 11.96 | **LOC:** 114 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (98.6166%)
- **Heaviest Functions:** `nodeProcess` (Impact: 20.1), `exitHandler` (Impact: 14.7), `ptyProcess` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `e2e/dotnet/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/optional/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native/src/generators/application/files/app/android/app/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/nx/src/native/tui/components/tasks_list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.698 IQR)
- **Top Global Matches:** file_cluster_8: 13.698, file_cluster_0: 13.822, file_cluster_17: 13.913
- **Magnitude:** 3339.6 | **LOC:** 6606 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (22.6203%), Tech Debt (62.1474%)
**Top Internal Functions/Classes:**
  * `from_str` (Impact: 560.0)
  * `is_loading_state` (Impact: 503.8)
  * `add_filter_char` (Impact: 365.3)
  * `calculate_column_visibility` (Impact: 266.1)
  * `render_cloud_message` (Impact: 126.2)
    * *Intent:* // Replace the first cell with a new one containing the NX logo and title
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 731`, `args: 184`, `func_start: 121`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 484`, `dead_code: 1`, `fragile_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 59`
* *Architecture:* `api: 36`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 485`, `doc: 123`, `test: 126`, `sync_locks: 58`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parking_lot::Mutex, lifecycle::BatchStatus, Cell, ScrollbarState, Table, Serialize, TaskSection, theme::THEME...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/pnpm-regression/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.419 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.277 IQR)
- **Top Global Matches:** file_cluster_8: 11.419, file_cluster_0: 11.53, file_cluster_7: 11.979
- **Magnitude:** 987.51 | **LOC:** 16458 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9259%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 205`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`
* *Architecture:* `io: 182`, `api: 22`, `concurrency: 62`, `import: 16`
* *Defense:* `safety: 13`, `doc: 347`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.24.5), core@7.24.0):
    resolution: integrity: sha512-OxBdcnF04bpdQdR3i4giHZNZQn7cm8RQKcSwA17wAAqEELo1ZOwp5FFgeptWUQXFyT9kwHo10aqqauYkRZPCAg==
    engines: node:, 2SkOrRk4pNBPg5IPZ+dOxcmkK5IyuBcxiNPyyYowPGUReyBvrvZs7IlQ==
    engines: node:, core@7.24.0), core@7.24.5), core@7.24.0)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.132 IQR)
- **Top Global Matches:** file_cluster_13: 13.132, file_cluster_8: 13.187, file_cluster_17: 13.36
- **Magnitude:** 820.88 | **LOC:** 2669 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (16.4919%), Tech Debt (84.199%)
**Top Internal Functions/Classes:**
  * `handle_event` (Impact: 102.5)
  * `render_batch_terminal_pane_internal` (Impact: 96.0)
  * `handle_key_event` (Impact: 26.6)
  * `init` (Impact: 21.3)
  * `setup_pane_pty` (Impact: 21.2)
    * *Intent:* // TODO: move this to the layout manager?
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 302`, `args: 127`, `func_start: 86`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 137`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 7`, `import: 43`
* *Defense:* `safety: 191`, `doc: 56`, `sync_locks: 43`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parking_lot::Mutex, crate::native::tui::tui_core::AutoExitDecision, super::components::dependency_view::DependencyView, super::pty::PtyInstance, TerminalPaneState, super::components::Component, TerminalPaneData, TasksList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/pnpm-lock-v6.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.88 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.156 IQR)
- **Top Global Matches:** file_cluster_8: 10.88, file_cluster_0: 11.058, file_cluster_7: 11.446
- **Magnitude:** 653.64 | **LOC:** 10421 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.5748%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 168`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 136`, `api: 12`, `concurrency: 24`, `import: 14`
* *Defense:* `safety: 14`, `doc: 288`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.21.3), KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:, core@7.21.3)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.64 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.077 IQR)
- **Top Global Matches:** file_cluster_8: 10.64, file_cluster_0: 11.022, file_cluster_7: 11.233
- **Magnitude:** 632.39 | **LOC:** 10285 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8432%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 171`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 137`, `api: 12`, `concurrency: 24`, `import: 14`
* *Defense:* `safety: 12`, `doc: 245`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` : 7.18.9_@babel+core@7.20.5, KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:, : 7.8.3_@babel+core@7.20.5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/metrics/collector.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.805 IQR)
- **Top Global Matches:** file_cluster_13: 12.805, file_cluster_8: 12.815, file_cluster_0: 12.892
- **Magnitude:** 524.08 | **LOC:** 1583 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (9.5631%), Tech Debt (77.799%)
**Top Internal Functions/Classes:**
  * `run_baseline_if_needed` (Impact: 144.3)
    * *Intent:* /// Establish CPU baselines for all processes when there are processes needing a baseline. /// Uses ...
  * `create_new_group_info` (Impact: 21.6)
    * *Intent:* /// Create only NEW groups based on current registrations
  * `collect_tree_metrics` (Impact: 19.6)
  * `collect_main_cli_subprocess_metrics` (Impact: 15.3)
  * `collect_all_task_metrics` (Impact: 15.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 188`, `args: 66`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 66`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `api: 12`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 140`, `doc: 84`, `test: 54`, `sync_locks: 34`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, tracing::error, GroupType, ThreadsafeFunctionCallMode, ProcessMetadata, crossbeam_channel::Sender, sysinfo::
    CpuRefreshKind, anyhow::Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/dotnet/analyzer/Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.194 IQR)
- **Top Global Matches:** file_cluster_8: 11.194, file_cluster_13: 11.359, file_cluster_17: 11.448
- **Magnitude:** 478.08 | **LOC:** 164 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2997%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 29`, `args: 3`, `func_start: 27`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `import: 6`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MsbuildAnalyzer.Utilities, MsbuildAnalyzer, Microsoft.Build.Locator, System.Text.Json, MsbuildAnalyzer.Models, System.Text.Json.Serialization
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/inline_app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.716 IQR)
- **Top Global Matches:** file_cluster_13: 12.716, file_cluster_8: 12.804, file_cluster_0: 12.961
- **Magnitude:** 463.88 | **LOC:** 1775 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (14.6146%), Tech Debt (73.0723%)
**Top Internal Functions/Classes:**
  * `handle_event` (Impact: 85.9)
  * `render_inline_status` (Impact: 53.0)
  * `handle_interactive_key` (Impact: 32.7)
  * `render_scrollback_above_tui` (Impact: 17.7)
  * `handle_action` (Impact: 14.9)
    * *Intent:* // Show status message in bottom chrome
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 228`, `args: 65`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 65`, `planned_debt: 1`, `orphaned_logic: 20`
* *Architecture:* `api: 3`, `concurrency: 25`, `import: 39`
* *Defense:* `safety: 128`, `doc: 73`, `test: 34`, `sync_locks: 26`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, crate::native::tui::utils::
    calculate_actual_duration_ms, crate::native::tui::theme::THEME, super::utils::get_task_status_icon, super::pty::PtyInstance, ratatui::style::Style, hashbrown::HashSet, super::lifecycle::BatchStatus...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/NxTargetFactory.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.374 IQR)
- **Top Global Matches:** file_cluster_8: 12.374, file_cluster_17: 12.419, file_cluster_13: 12.432
- **Magnitude:** 430.64 | **LOC:** 734 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (44.0959%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createCiPhaseTarget` (Impact: 37.8)
  * `createSimpleGoalTarget` (Impact: 29.2)
  * `createRegularPhaseTarget` (Impact: 26.2)
  * `createPhaseBatchTarget` (Impact: 22.5)
  * `createIndividualGoalTargets` (Impact: 20.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 67`, `args: 52`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 146`
* *Architecture:* `io: 2`, `api: 2`, `import: 16`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` dev.nx.maven.utils.PathFormatter, dev.nx.maven.utils.MojoAnalyzer, com.google.gson.JsonArray, org.slf4j.LoggerFactory, org.apache.maven.plugin.descriptor.PluginDescriptor, org.slf4j.Logger, java.io.File, org.apache.maven.plugin.descriptor.MojoDescriptor...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/app/pnpm-lock-v6.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.545 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.234 IQR)
- **Top Global Matches:** file_cluster_8: 10.545, file_cluster_0: 10.745, file_cluster_7: 11.167
- **Magnitude:** 415.48 | **LOC:** 7407 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0262%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 95`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 97`, `api: 12`, `concurrency: 19`, `import: 10`
* *Defense:* `safety: 10`, `doc: 133`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.21.3), core@7.21.3), KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/app/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.381 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.175 IQR)
- **Top Global Matches:** file_cluster_8: 10.381, file_cluster_0: 10.735, file_cluster_7: 11.024
- **Magnitude:** 414.16 | **LOC:** 7450 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1593%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 97`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 98`, `api: 13`, `concurrency: 19`, `import: 10`
* *Defense:* `safety: 10`, `doc: 119`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:, : 7.18.9_@babel+core@7.20.5, : 7.8.3_@babel+core@7.20.5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/plugins/js/ts_import_locators.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.905 IQR)
- **Top Global Matches:** file_cluster_8: 10.905, file_cluster_16: 11.08, file_cluster_13: 11.212
- **Magnitude:** 376.28 | **LOC:** 1740 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (13.3897%), Tech Debt (23.1961%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 83.5)
  * `find_specifier_in_import` (Impact: 62.0)
  * `find_specifier_in_export` (Impact: 60.9)
  * `find_imports_with_ast` (Impact: 24.8)
  * `should_find_imports` (Impact: 10.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 250`, `args: 41`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 36`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 11`, `concurrency: 20`, `import: 28`
* *Defense:* `safety: 94`, `test: 48`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` swc_ecma_parser::token::BinOpToken, tracing::trace, Tokens, swc_common::BytePos, swc_ecma_ast::EsVersion::EsNext, crate::native::walker::nx_walker, std::env, Class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/telemetry/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.003 IQR)
- **Top Global Matches:** file_cluster_8: 13.003, file_cluster_16: 13.012, file_cluster_13: 13.043
- **Magnitude:** 370.3 | **LOC:** 669 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (16.7293%), Tech Debt (17.0432%)
**Top Internal Functions/Classes:**
  * `background_sender` (Impact: 43.0)
  * `send_batches` (Impact: 27.4)
  * `log_page_view` (Impact: 21.4)
  * `sanitize_params` (Impact: 19.3)
  * `new` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 134`, `args: 31`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 95`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 34`, `concurrency: 14`, `import: 7`
* *Defense:* `safety: 94`, `doc: 29`, `sync_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, reqwest::Client, crossbeam_channel::self, std::collections::HashMap, ClientBuilder, Sender, napi::bindgen_prelude::*, std::time::Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/tui_state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.003 IQR)
- **Top Global Matches:** file_cluster_0: 13.003, file_cluster_13: 13.041, file_cluster_16: 13.132
- **Magnitude:** 368.5 | **LOC:** 1002 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.4615%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 9.1)
    * *Intent:* /// Create a new TuiState with the given tasks and configuration
  * `call_done_callback` (Impact: 7.6)
    * *Intent:* /// Call the done callback if it exists /// Can be called multiple times safely /// If is_forced_shu...
  * `get_focused_item_id` (Impact: 7.6)
    * *Intent:* /// Get the item ID (task or batch) that should be shown in inline mode /// Priority: focused pane i...
  * `test_task_timing` (Impact: 7.0)
    * *Intent:* // === Task Timing Tests ===
  * `complete_batch_metadata` (Impact: 6.0)
    * *Intent:* /// Update batch as completed
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 136`, `args: 94`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 44`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 47`
* *Architecture:* `api: 72`, `concurrency: 27`, `import: 25`
* *Defense:* `safety: 122`, `doc: 82`, `test: 62`, `sync_locks: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, crate::native::tasks::types::Task, super::pty::PtyInstance, TuiState timing

use super::components::task_selection_manager::SelectionEntry, crate::native::ide::nx_console::messaging::NxConsoleMessageConnection, ThreadsafeFunctionCallMode, Instant, RunMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/ide/nx_console/ipc_transport.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.016 IQR)
- **Top Global Matches:** file_cluster_4: 12.016, file_cluster_13: 12.566, file_cluster_0: 12.688
- **Magnitude:** 324.68 | **LOC:** 321 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `receive` (Impact: 17.2)
  * `send` (Impact: 9.3)
  * `test_transport_receiver_receive` (Impact: 7.3)
  * `new` (Impact: 6.4)
  * `test_transport_sender_send` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 166`, `args: 24`, `func_start: 24`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 31`, `duplicate_logic: 17`
* *Architecture:* `io: 9`, `api: 11`, `concurrency: 202`, `import: 23`
* *Defense:* `safety: 30`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncWriteExt, jsonrpsee::core::client::ReceivedMessage, tokio::net::windows::named_pipe::ServerOptions, ToFsName, super::test_utils::*, std::pin::Pin, RefTokioAsyncWrite, interprocess::
    bound_util::RefTokioAsyncRead...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vitest/src/generators/configuration/configuration.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.071 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.738 IQR)
- **Top Global Matches:** file_cluster_8: 11.071, file_cluster_13: 11.114, file_cluster_0: 11.121
- **Magnitude:** 320.23 | **LOC:** 527 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.9132%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 38`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 4`, `import: 12`
* *Defense:* `safety: 19`, `doc: 10`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` $zoneless ?, versions, testing, setup-testbed, semver, init, ts-solution-setup, version-utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mvnw` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.752 IQR)
- **Top Global Matches:** file_cluster_11: 13.752, file_cluster_8: 13.756, file_cluster_17: 13.806
- **Magnitude:** 319.26 | **LOC:** 296 | **CtrlFlow:** 88.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.3942%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `native_path_[Truncated]` (Impact: 222.3)
    * *Intent:* # OS specific support.
  * `__global_context__` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 19`, `args: 5`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 87`, `orphaned_logic: 2`
* *Architecture:* `io: 86`
* *Defense:* `safety: 31`, `sync_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/components/task_selection_manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.16 IQR)
- **Top Global Matches:** file_cluster_8: 13.16, file_cluster_0: 13.26, file_cluster_7: 13.409
- **Magnitude:** 294.8 | **LOC:** 931 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (11.2495%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `handle_in_progress_task_finished` (Impact: 43.6)
  * `previous` (Impact: 13.4)
  * `get_selected_task_index` (Impact: 13.3)
  * `next` (Impact: 13.1)
  * `ensure_selected_visible` (Impact: 12.9)
    * *Intent:* /// Scroll up by the specified number of lines
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 101`, `args: 56`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `state_mutation: 47`, `orphaned_logic: 12`
* *Architecture:* `api: 38`
* *Defense:* `safety: 124`, `doc: 75`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/pnpm-semver-range-specifier/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.473 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.344 IQR)
- **Top Global Matches:** file_cluster_8: 10.473, file_cluster_0: 10.545, file_cluster_7: 11.101
- **Magnitude:** 292.78 | **LOC:** 7423 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.8526%), Tech Debt (7.7679%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 90`, `func_start: 1`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 101`, `api: 4`, `concurrency: 17`, `import: 9`
* *Defense:* `safety: 3`, `doc: 118`, `immutability_locks: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.27.4)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/devkit/src/generators/format-files.spec.ts` (TYPESCRIPT) | Magnitude: 3.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 13, concurrency: 10, args: 9
- `packages/remix/src/utils/get-default-export-name.ts` (TYPESCRIPT) | Magnitude: 1.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 4, api: 3, safety: 2
- `packages/angular/src/builders/utilities/buildable-libs.ts` (TYPESCRIPT) | Magnitude: 1.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, branch: 9, structural_boundaries: 6, safety: 4
- `packages/react/src/migrations/update-21-0-0/update-babel-loose.ts` (TYPESCRIPT) | Magnitude: 3.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 12, branch: 10, args: 4
- `packages/nx/src/native/tasks/running_tasks_service.rs` (RUST) | Magnitude: 75.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 41, safety: 32, branch: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/eslint-plugin/src/configs/typescript.ts` (TYPESCRIPT) | Magnitude: 0.92 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 30, doc: 21, decorators: 18, structural_boundaries: 10
- `graph/client-e2e/src/plugins/index.js` (JAVASCRIPT) | Magnitude: 4.04 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 2, structural_boundaries: 1, args: 1, func_start: 1
- `packages/eslint-plugin/src/flat-configs/typescript.ts` (TYPESCRIPT) | Magnitude: 0.51 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, doc: 19, decorators: 16, structural_boundaries: 13
- `packages/eslint-plugin/src/configs/react-typescript.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, doc: 7, decorators: 6, events: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `mvnw` (SHELL) | Magnitude: 319.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 150, indent_spaces: 118, state_mutation: 87, io: 86

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/angular/src/generators/setup-ssr/setup-ssr.spec.ts` (TYPESCRIPT) | Magnitude: 49.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 924, structural_boundaries: 290, func_start: 151, args: 146
- `packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-plugin.ts` (TYPESCRIPT) | Magnitude: 10.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 80, state_mutation: 39, branch: 31, structural_boundaries: 20
- `packages/vite/src/generators/configuration/configuration.ts` (TYPESCRIPT) | Magnitude: 16.81 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 187, branch: 36, structural_boundaries: 29, state_mutation: 19
- `packages/eslint-plugin/angular.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, import: 3, api: 2
- `packages/eslint-plugin/typescript.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, import: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/nx/src/native/utils/git.rs` (RUST) | Magnitude: 38.26 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, safety: 11, branch: 9
- `packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildState.kt` (KOTLIN) | Magnitude: 15.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 18, indent_spaces: 18, generics: 7, structural_boundaries: 3
- `packages/js/src/utils/typescript/configuration.ts` (TYPESCRIPT) | Magnitude: 3.77 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 21, generics: 15, branch: 9
- `packages/create-nx-workspace/src/internal-utils/yargs-options.ts` (TYPESCRIPT) | Magnitude: 5.81 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 33, generics: 16, api: 14
- `packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/data/MavenBatchOptions.kt` (KOTLIN) | Magnitude: 16.06 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 38, indent_spaces: 38, doc: 27, generics: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `graph/ui-code-block/src/lib/json-code-block.tsx` (TYPESCRIPT) | Magnitude: 3.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 21, ui_framework: 15, branch: 10
- `packages/react-native/src/utils/find-all-npm-dependencies.ts` (TYPESCRIPT) | Magnitude: 1.21 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, args: 3, state_mutation: 3
- `packages/devkit/src/generators/executor-options-utils.ts` (TYPESCRIPT) | Magnitude: 3.51 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, branch: 10, args: 10, generics: 8
- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/JavaAstTestParser.kt` (KOTLIN) | Magnitude: 54.56 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, branch: 18, structural_boundaries: 17, immutability_locks: 11
- `packages/eslint/src/generators/convert-to-flat-config/converters/json-converter.ts` (TYPESCRIPT) | Magnitude: 18.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 348, state_mutation: 100, branch: 63, structural_boundaries: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/expo/src/generators/application/files/nx-welcome/unclaimed/src/app/App.tsx.template` (TYPESCRIPT) | Magnitude: 57.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 716, ui_framework: 148, generics: 145, structural_boundaries: 18
- `nx-dev/ui-markdoc/src/lib/tags/stackblitz-button.component.tsx` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, ui_framework: 10, structural_boundaries: 5, io: 3
- `nx-dev/ui-markdoc/src/lib/tags/graph.component.tsx` (TYPESCRIPT) | Magnitude: 4.08 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 33, ui_framework: 20, branch: 19
- `graph/migrate/src/lib/components/migration-list.tsx` (TYPESCRIPT) | Magnitude: 5.02 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 45, ui_framework: 37, args: 28
- `packages/react-native/src/generators/application/files/nx-welcome/not-configured/src/app/App.tsx.template` (TYPESCRIPT) | Magnitude: 59.92 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 707, ui_framework: 149, generics: 146, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/rollup/src/plugins/postcss/loaders/stylus-loader.ts` (TYPESCRIPT) | Magnitude: 5.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 19, structural_boundaries: 13, args: 9
- `nx-dev/ui-common/src/lib/hubspot-form.tsx` (TYPESCRIPT) | Magnitude: 19.49 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 105, branch: 36, ui_framework: 27
- `packages/plugin/src/generators/e2e-project/e2e.ts` (TYPESCRIPT) | Magnitude: 17.72 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 212, concurrency: 43, structural_boundaries: 42, branch: 27
- `packages/react/src/generators/init/init.ts` (TYPESCRIPT) | Magnitude: 3.55 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 15, concurrency: 10, branch: 8
- `packages/storybook/src/generators/init/init.spec.ts` (TYPESCRIPT) | Magnitude: 7.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 18, concurrency: 14, args: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/nx/src/utils/call-sites.ts` (TYPESCRIPT) | Magnitude: 0.75 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, immutability_locks: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/dotnet/analyzer/Models/NxJsonConfig.cs` (CSHARP) | Magnitude: 15.6 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, class_start: 1
- `packages/dotnet/analyzer/Models/ProjectNode.cs` (CSHARP) | Magnitude: 19.16 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, structural_boundaries: 6, api: 5, immutability_locks: 4
- `packages/dotnet/analyzer/Models/Target.cs` (CSHARP) | Magnitude: 25.26 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, structural_boundaries: 11, api: 10, immutability_locks: 9
- `packages/dotnet/analyzer/Models/PluginOptions.cs` (CSHARP) | Magnitude: 32.24 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, api: 9, state_mutation: 8, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/angular/src/migrations/update-21-5-0/remove-default-karma-configuration-files.ts` (TYPESCRIPT) | Magnitude: 21.49 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, branch: 21, state_mutation: 12, immutability_locks: 9
- `packages/nx/src/plugins/js/project-graph/build-dependencies/explicit-project-dependencies.ts` (TYPESCRIPT) | Magnitude: 6.43 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, branch: 18, structural_boundaries: 17, immutability_locks: 14
- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/NxTracing.kt` (KOTLIN) | Magnitude: 18.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 16, import: 11, immutability_locks: 10
- `packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/PathUtils.kt` (KOTLIN) | Magnitude: 30.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, branch: 10, io: 9
- `packages/angular/src/generators/setup-ssr/lib/add-dependencies.ts` (TYPESCRIPT) | Magnitude: 3.03 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, branch: 7, decorators: 7, immutability_locks: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/js/src/plugins/typescript/plugin.ts` -> Churn: **67.09%** | Cog Load: 29.5869% | Debt: 82.3685%
- `packages/js/src/plugins/typescript/plugin.spec.ts` -> Churn: **63.82%** | Cog Load: 5.881% | Debt: 99.0815%
- `packages/nx/src/tasks-runner/task-orchestrator.ts` -> Churn: **63.82%** | Cog Load: 99.9971% | Debt: 8.05%
- `packages/create-nx-workspace/src/create-workspace.ts` -> Churn: **62.92%** | Cog Load: 58.0905% | Debt: 96.8082%
- `packages/nx/src/command-line/migrate/migrate.ts` -> Churn: **62.92%** | Cog Load: 96.7951% | Debt: 99.7887%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/dotnet/analyzer/Program.cs` -> **Craigory Coppola** (100.0% isolated ownership) | Magnitude: 478.08
- `mvnw` -> **Jason Jean** (100.0% isolated ownership) | Magnitude: 319.26
- `packages/nx/src/plugins/js/lock-file/__fixtures__/pnpm-semver-range-specifier/pnpm-lock.yaml.ts` -> **Nicholas Cunningham** (100.0% isolated ownership) | Magnitude: 292.78
- `packages/nx/src/native/tui/components/layout_manager.rs` -> **Craigory Coppola** (100.0% isolated ownership) | Magnitude: 263.78
- `packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenHomeDiscovery.kt` -> **Jason Jean** (100.0% isolated ownership) | Magnitude: 226.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/nx/src/project-graph/plugins/loaded-nx-plugin.ts` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `packages/nx/src/project-graph/build-project-graph.ts` -> **Severity: 0.021** (Bridge: 0.0003 * Flux: 63.7138%)
- `packages/nx/src/project-graph/project-graph-builder.ts` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9999%)
- `packages/nx/src/command-line/graph/graph.ts` -> **Severity: 0.016** (Bridge: 0.0003 * Flux: 55.7463%)
- `packages/nx/src/tasks-runner/pseudo-terminal.ts` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.998%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/nx/src/devkit-exports.ts` -> **Severity: 1810.3** (Blast Radius: 18.103 * Doc Risk: 100.0%)
- `packages/nx/src/native/pseudo_terminal/child_process.rs` -> **Severity: 1395.3** (Blast Radius: 13.953 * Doc Risk: 100.0%)
- `packages/nx/src/utils/workspace-root.ts` -> **Severity: 1152.083** (Blast Radius: 17.317 * Doc Risk: 66.529%)
- `packages/devkit/src/utils/semver.ts` -> **Severity: 425.238** (Blast Radius: 7.421 * Doc Risk: 57.302%)
- `packages/nx/src/devkit-internals.ts` -> **Severity: 410.0** (Blast Radius: 4.1 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
