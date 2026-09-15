# ARCHITECTURAL_BRIEF: storybook
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/storybookjs/storybook.git` |
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
| Total Artifacts | 5516 |
| Analyzed Artifacts (Scanned) | 3544 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1972 |
| Total LOC | 292646 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 64.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7302 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1829 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0128 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 277 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2651 | 274926 | 74.8% |
| JAVASCRIPT | 279 | 8375 | 7.9% |
| JSON | 180 | 3282 | 5.1% |
| HTML | 143 | 4515 | 4.0% |
| MARKDOWN | 131 | 0 | 3.7% |
| PLAINTEXT | 78 | 1 | 2.2% |
| CSS | 49 | 1396 | 1.4% |
| XML | 18 | 13 | 0.5% |
| YAML | 11 | 89 | 0.3% |
| SHELL | 4 | 49 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.44; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Declarative / Non-Code 21%, Callbacks & Closures Files 17%, Defensive Guards Files 6%, Large Core Modules 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3321 | 93.7% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 208 | 5.9% |
| Static: Minified & Vendor Opaque Mass | 14 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1972*

**Composition by Extension & Reason:**
- `.md`: 719x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5720 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3544 LOC)
- `.png`: 213x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 190x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.ts`: 160x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 55 LOC), 5x Excluded (Machine-Generated Source Code Signature: 35 LOC)
- `.tsx`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 18 exceeds 500 chars)
- `.snapshot`: 104x Excluded (Unsupported Extension: '.snapshot'), 14x Unsupported Format (.snapshot), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 18x Excluded (Machine-Generated Source Code Signature: 35 LOC), 10x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `no_extension`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.pug`: 37x Excluded (Unsupported Extension: '.pug'), 7x Unsupported Format (.pug)
- `.yml`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp4`: 37x Excluded (Explicitly Denied Extension: '.mp4')
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 30 LOC), 5x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `.lock`: 11x Excluded (Unsupported Extension: '.lock'), 2x Unsupported Format (.lock)
- `.snap`: 8x Unsupported Format (.snap), 4x Excluded (Unsupported Extension: '.snap'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 12x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.7 | 5.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 29.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.2 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.0 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 68.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.7 | 0.3 | 0.1 | 0.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 80.3 | 11.2 | 14.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 48.6 | 46.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2127 | 697 | 1 | `code/core/src/manager-api/tests/stories.test.ts` |
| cleanup | 157 | 78 | 0 | `code/core/src/core-server/change-detection/ChangeDetectionService.test.ts` |
| guards | 6899 | 1216 | 5 | `code/core/src/docs-tools/argTypes/jsdocParser.test.ts` |
| danger | 4612 | 1050 | 3 | `code/core/src/manager-api/tests/stories.test.ts` |
| concurrency | 13516 | 1039 | 10 | `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` |
| connectivity | 11529 | 2587 | 7 | `code/core/src/csf-tools/ConfigFile.test.ts` |
| io | 5915 | 712 | 3 | `code/core/src/manager/components/sidebar/mockdata.large.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 12 | 0 | `code/addons/themes/src/postinstall.ts` |
| time | 356 | 176 | 0 | `code/core/src/highlight/useHighlights.stories.tsx` |
| serialization | 405 | 219 | 0 | `code/core/src/docs-tools/argTypes/convert/convert.test.ts` |
| regex | 779 | 301 | 0 | `code/core/src/csf-tools/vitest-plugin/transformer.test.ts` |
| events | 2420 | 589 | 2 | `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` |
| tests | 15065 | 646 | 7 | `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` |
| docs | 2642 | 732 | 2 | `code/core/src/docs-tools/argTypes/jsdocParser.test.ts` |
| debt | 845 | 335 | 0 | `code/lib/cli-storybook/src/automigrate/fixes/migrate-addon-console.test.ts` |
| mutation | 45918 | 2574 | 30 | `code/core/src/manager/components/sidebar/mockdata.large.ts` |
| dead_code | 793 | 485 | 1 | `code/core/src/csf-tools/ConfigFile.ts` |
| credential | 9 | 6 | 0 | `code/core/src/telemetry/storybook-metadata.test.ts` |
| threat | 525 | 213 | 0 | `test-storybooks/ember-cli/ember-output/assets/ember-example.js` |
| ml_ai | 267 | 80 | 0 | `code/core/src/components/components/Select/Select.tsx` |
| ui | 5402 | 685 | 3 | `code/core/src/components/components/Modal/Modal.stories.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `code/core/src/manager/components/sidebar/mockdata.large.ts` (Hits: 1543)
- `code/addons/vitest/src/updateVitestFile.config.4.test.ts` (Hits: 168)
- `code/addons/vitest/src/updateVitestFile.config.test.ts` (Hits: 160)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vitest.ts** (`code/addons/vitest/src/node/vitest.ts`) — 381 inbound connections
2. **test.sh** (`scripts/ecosystem-ci/test.sh`) — 251 inbound connections
3. **common.tsx** (`code/core/src/components/components/typography/lib/common.tsx`) — 229 inbound connections
4. **global.ts** (`code/core/src/theming/global.ts`) — 173 inbound connections
5. **core.ts** (`code/core/src/bin/core.ts`) — 91 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`code/core/src/components/index.ts`) — 76 outbound dependencies
2. **index.ts** (`code/core/src/common/index.ts`) — 47 outbound dependencies
3. **getComponentImports.test.ts** (`code/renderers/react/src/componentManifest/getComponentImports.test.ts`) — 32 outbound dependencies
4. **task.ts** (`scripts/task.ts`) — 32 outbound dependencies
5. **sandbox-parts.ts** (`scripts/tasks/sandbox-parts.ts`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `transform` **(Many-Argument Workhorses)** (@ `code/core/src/csf-tools/CsfFile.test.ts`) -> Impact: **377.9** | LOC: 3123
- `removeField` **(Many-Argument Workhorses)** (@ `code/core/src/csf-tools/ConfigFile.test.ts`) -> Impact: **352.9** | LOC: 1897
- `parse` **(Compute Cores)** (@ `code/core/src/csf-tools/CsfFile.ts`) -> Impact: **193.3** | LOC: 546
- `storyToCsfFactory` **(Many-Argument Workhorses)** (@ `code/lib/cli-storybook/src/codemod/helpers/story-to-csf-factory.ts`) -> Impact: **184.0** | LOC: 494
- `onModuleGraphChange` **(Compute Cores)** (@ `code/core/src/types/modules/core-common.ts`) -> Impact: **181.8** | LOC: 497
- `getCodeSnippet` **(Many-Argument Workhorses)** (@ `code/renderers/react/src/componentManifest/generateCodeSnippet.ts`) -> Impact: **163.6** | LOC: 272
- `TestProviderRender` **(Compute Cores)** (@ `code/addons/vitest/src/components/TestProviderRender.tsx`) -> Impact: **148.3** | LOC: 393
- `esmWalker` **(Defensive Guards)** (@ `code/core/src/mocking-utils/esmWalker.ts`) -> Impact: **145.8** | LOC: 180
  * *Intent:* /** Same logic from @vue/compiler-core & @vue/compiler-sfc Except this is using acorn AST */
- `configToCsfFactory` **(Many-Argument Workhorses)** (@ `code/lib/cli-storybook/src/codemod/helpers/config-to-csf-factory.ts`) -> Impact: **142.9** | LOC: 259
- `generateDocgen` **(Many-Argument Workhorses)** (@ `code/frameworks/svelte-vite/src/plugins/generateDocgen.ts`) -> Impact: **132.9** | LOC: 268

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `code/renderers/react/src/componentManifest/componentMeta` | 14 | 34944.38 | 31.58% | 0.0% |
| `code/addons/vitest/src` | 21 | 20181.23 | 10.0% | 6.04% |
| `code/core/src/common/js-package-manager` | 18 | 11338.3 | 29.98% | 1.56% |
| `code/core/src/manager/components/sidebar` | 63 | 9943.82 | 15.83% | 10.63% |
| `code/core/src/cli` | 17 | 9474.39 | 28.71% | 4.87% |
| `code/lib/cli-storybook/src/automigrate/fixes` | 42 | 7762.82 | 31.72% | 0.57% |
| `code/core/src/core-server/utils` | 51 | 6179.22 | 30.83% | 0.47% |
| `code/core/src/preview-api/modules/preview-web` | 17 | 5886.65 | 42.83% | 4.3% |
| `code/core/src/csf-tools` | 13 | 5762.08 | 19.21% | 3.44% |
| `code/e2e-tests` | 23 | 5440.67 | 82.74% | 11.24% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `code/frameworks/nextjs-vite/template/stories/Redirect.stories.tsx` -> **99.9842%** Exposure
- `code/frameworks/nextjs/template/stories_nextjs-default-ts/Redirect.stories.tsx` -> **99.9842%** Exposure
- `code/frameworks/nextjs/template/stories_nextjs-prerelease/Redirect.stories.tsx` -> **99.9842%** Exposure
- `code/frameworks/angular/template/stories/basics/component-with-complex-selectors/multiple-selector.component.ts` -> **99.9665%** Exposure
- `code/renderers/vue3/template/stories_vue3-vite-default-ts/component-meta/ts-named-export/component.ts` -> **99.9665%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `code/addons/a11y/src/postinstall.ts` -> **100.0%** Exposure
- `code/addons/links/src/react/components/link.tsx` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/preview/splitSelectors.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/components/Description.tsx` -> **100.0%** Exposure
- `code/addons/vitest/src/components/TestStatusIcon.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/core/src/manager-api/tests/refs.test.ts` -> **0** Orphaned Functions | **17** Duplicates
- `code/core/src/components/components/Modal/Modal.stories.tsx` -> **1** Orphaned Functions | **12** Duplicates
- `code/core/src/components/components/Select/Select.stories.tsx` -> **1** Orphaned Functions | **12** Duplicates
- `code/core/src/manager/components/sidebar/Filter.stories.tsx` -> **9** Orphaned Functions | **2** Duplicates
- `code/core/src/instrumenter/instrumenter.test.ts` -> **4** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6630` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `code/frameworks/nextjs/src/swc/next-swc-loader-patch.ts` (TYPESCRIPT) -> Cumulative Risk: **744.36**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.01)
- **Magnitude:** 130.94 | **LOC:** 206 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9982%), Cognitive Load (94.2449%)
- **Heaviest Functions:** `loaderTransform` (Many-Argument Workhorses, Impact: 58.4), `pitch` (Callbacks & Closures, Impact: 16.0), `swcLoader` (Callbacks & Closures, Impact: 4.7)

### 2. `code/core/src/core-server/build-dev.ts` (TYPESCRIPT) -> Cumulative Risk: **724.28**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.42)
- **Magnitude:** 283.72 | **LOC:** 339 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), State Flux (99.4202%), Documentation (89.953%)
- **Heaviest Functions:** `buildDevStandalone` (Compute Cores, Impact: 110.9), `send` (Compute Cores, Impact: 52.1), `setHandler` (Callbacks & Closures, Impact: 1.1)

### 3. `code/builders/builder-webpack5/src/presets/custom-webpack-preset.ts` (TYPESCRIPT) -> Cumulative Risk: **706.91**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.15)
- **Magnitude:** 77.64 | **LOC:** 93 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `swc` (Defensive Guards, Impact: 17.9), `webpack` (Defensive Guards, Impact: 9.9), `webpackFinal` (Compute Cores, Impact: 8.5)

### 4. `code/core/src/manager-api/root.tsx` (TYPESCRIPT) -> Cumulative Risk: **705.4**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.36)
- **Magnitude:** 224.02 | **LOC:** 516 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.1093%), Api Exposure (92.4191%)
- **Heaviest Functions:** `useSharedState` (Compute Cores, Impact: 32.0), `useArgs` (Defensive Guards, Impact: 7.9), `[SET_STORIES]` (Callbacks & Closures, Impact: 6.8)

### 5. `code/core/src/manager/components/preview/tools/share.stories.tsx` (TYPESCRIPT) -> Cumulative Risk: **703.05**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -1.36)
- **Magnitude:** 0.04 | **LOC:** 78 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `getStoryHrefs` (Callbacks & Closures, Impact: 5.4), `ManagerDecorator` (Interface Declarations, Impact: 3.8), `play` (Callbacks & Closures, Impact: 1.9)

### 6. `code/core/src/core-server/build-static.ts` (TYPESCRIPT) -> Cumulative Risk: **702.53**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.22)
- **Magnitude:** 169.02 | **LOC:** 233 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.2824%), Cognitive Load (98.1921%)
- **Heaviest Functions:** `buildStaticStandalone` (Compute Cores, Impact: 62.2)

### 7. `code/core/src/node-logger/prompts/prompt-functions.ts` (TYPESCRIPT) -> Cumulative Risk: **701.4**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -0.02)
- **Magnitude:** 170.9 | **LOC:** 256 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.4178%), State Flux (95.218%)
- **Heaviest Functions:** `log` (Compute Cores, Impact: 12.4), `multiselect` (Generic / Templated Code, Impact: 7.9), `message` (Callbacks & Closures, Impact: 6.3)

### 8. `code/core/src/common/utils/file-cache.ts` (TYPESCRIPT) -> Cumulative Risk: **695.97**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.43)
- **Magnitude:** 153.7 | **LOC:** 163 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `constructor` (Compute Cores, Impact: 8.9), `parseSetData` (Defensive Guards, Impact: 8.2), `setMany` (Defensive Guards, Impact: 7.1)

### 9. `code/core/src/channels/main.ts` (TYPESCRIPT) -> Cumulative Risk: **692.94**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.91)
- **Magnitude:** 118.24 | **LOC:** 148 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8482%), Concurrency (87.4754%), Cognitive Load (83.9512%)
- **Heaviest Functions:** `emit` (Callbacks & Closures, Impact: 11.4), `constructor` (Callbacks & Closures, Impact: 9.3), `removeAllListeners` (State Mutators, Impact: 7.4)

### 10. `code/builders/builder-vite/src/index.ts` (TYPESCRIPT) -> Cumulative Risk: **690.31**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z -1.10)
- **Magnitude:** 154.18 | **LOC:** 208 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 90.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (98.6166%)
- **Heaviest Functions:** `startChangeDetection` (Callbacks & Closures, Impact: 15.6), `bail` (Defensive Guards, Impact: 5.8), `watcherChangeHandler` (Callbacks & Closures, Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.props.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 8183.09 | **LOC:** 756 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.8413%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 357`, `args: 94`, `func_start: 72`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 74`, `import: 43`
* *Defense:* `safety: 46`, `doc: 4`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Accordion, Button, Panel, Widget, componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 7090.13 | **LOC:** 361 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.5037%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 104`, `args: 46`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `io: 1`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 43`, `test: 46`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` command.ts, BUNProxy.ts, JsPackageManagerFactory.ts, NPMProxy.ts, PNPMProxy.ts, Yarn1Proxy.ts, Yarn2Proxy.ts, index.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.4.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6706.69 | **LOC:** 2217 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (3.877%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 410`, `args: 31`, `func_start: 26`
* *Risk/State:* None
* *Architecture:* `io: 168`, `api: 57`, `concurrency: 52`, `import: 213`
* *Defense:* `safety: 4`, `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` getDiff.ts, updateVitestFile.ts, vite.config, vitest-plugin, plugin-react, browser-playwright, node:path, node:url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6359.44 | **LOC:** 2061 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (3.9467%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 370`, `args: 30`, `func_start: 25`
* *Risk/State:* None
* *Architecture:* `io: 160`, `api: 55`, `concurrency: 50`, `import: 180`
* *Defense:* `safety: 4`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` getDiff.ts, updateVitestFile.ts, vite.config, vitest-plugin, plugin-react, node:path, node:url, babel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager/components/sidebar/mockdata.large.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6318.32 | **LOC:** 26727 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.6489%), Tech Debt (7.6055%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 610 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 5762
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 1991`
* *Risk/State:* `state_mutation: 4542`, `planned_debt: 1`
* *Architecture:* `io: 1543`, `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.212
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000564
  * `Imports (Out-Degree: 0):` types.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 5969.07 | **LOC:** 605 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.8799%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 193`, `args: 57`, `func_start: 27`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 7`
* *Architecture:* `api: 22`, `concurrency: 28`, `import: 20`
* *Defense:* `safety: 24`, `doc: 28`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Button, componentMetaExtractor.test-helpers.ts, index, override, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/addons/vitest/src/updateVitestFile.config.3.2.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5621.14 | **LOC:** 1898 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (3.9435%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 336`, `args: 28`, `func_start: 23`
* *Risk/State:* None
* *Architecture:* `io: 148`, `api: 46`, `concurrency: 46`, `import: 165`
* *Defense:* `safety: 4`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` getDiff.ts, updateVitestFile.ts, vite.config, vitest-plugin, plugin-react, node:path, node:url, babel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/cli/AddonVitestService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 5199.28 | **LOC:** 896 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (31.6629%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 230`, `args: 99`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 16`
* *Architecture:* `io: 22`, `api: 20`, `concurrency: 122`, `import: 26`
* *Defense:* `safety: 12`, `test: 175`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index.ts, AddonVitestService.ts, vite.config, find, execa, promises, node:os, common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 4590.4 | **LOC:** 4120 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gatedImportFn` **(I/O & Config Routines)** (Impact: 8.9)
  * `createAndRenderPreview` **(Callbacks & Closures)** (Impact: 4.9)
  * `play` **(Tests & Verification)** (Impact: 4.3)
  * `text` **(Tests & Verification)** (Impact: 4.2)
  * `serializeError` **(Callbacks & Closures)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 500 instances
* *Amplified Cascading Flux:* 397 instances
* *Concurrency (weighted view):* 3136
* *State Mutation (weighted view):* 1344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 820`, `args: 326`, `func_start: 189`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 550`, `unreferenced_by_name: 2`
* *Architecture:* `io: 38`, `api: 1`, `concurrency: 636`, `import: 12`
* *Defense:* `safety: 29`, `doc: 2`, `test: 522`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` index.ts, index.ts, PreviewWeb.mockdata.ts, PreviewWeb.tsx, WebView.ts, global, object, client-logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.defaultValue.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4367.28 | **LOC:** 399 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.911%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 137`, `args: 43`, `func_start: 39`, `class_start: 22`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 21`, `concurrency: 40`, `import: 23`
* *Defense:* `safety: 22`, `doc: 3`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4319.81 | **LOC:** 420 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.7162%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 126`, `args: 36`, `func_start: 31`, `class_start: 16`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 4`, `api: 27`, `concurrency: 14`, `import: 35`
* *Defense:* `safety: 29`, `doc: 18`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` getComponentImports.ts, accordion, button, componentMetaExtractor.test-helpers.ts, dialog, accordion, override, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.detection.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4097.18 | **LOC:** 338 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (64.5453%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 176`, `args: 60`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 39`, `concurrency: 58`, `import: 24`
* *Defense:* `safety: 33`, `test: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Lazy, Target, componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/babel/vitest-config-helpers.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3730.85 | **LOC:** 337 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (5.115%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 106`, `args: 34`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 33`, `import: 31`
* *Defense:* `safety: 8`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vite.config, vitest-config-helpers.ts, vitest, config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/reactDocgen/extractReactDocgenInfo.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3326.0 | **LOC:** 747 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (7.1489%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 115`, `args: 34`, `func_start: 7`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 19`, `doc: 6`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fixtures.ts, extractReactDocgenInfo.ts, memfs, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/cli/eslintPlugin.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2978.62 | **LOC:** 654 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (9.1493%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 175`, `args: 42`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 4`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 41`, `import: 51`
* *Defense:* `safety: 30`, `test: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index.ts, JsPackageManager.ts, eslintPlugin.ts, compat, eslintrc, js, find, core-web-vitals...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/core-server/utils/StoryIndexGenerator.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2932.97 | **LOC:** 2425 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (43.8735%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 330
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 287`, `args: 74`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 256`
* *Architecture:* `io: 1`, `concurrency: 155`, `import: 13`
* *Defense:* `safety: 1`, `doc: 6`, `test: 133`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` tags.ts, common-preset.ts, StoryIndexGenerator.ts, async () => 
        const csfSpecifier: NormalizedStoriesSpecifier = normalizeStoriesEntry(, node:path, common, csf, csf-tools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/cli-storybook/src/automigrate/fixes/migrate-addon-console.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2432.4 | **LOC:** 513 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.2962%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 122`, `args: 41`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 13`
* *Architecture:* `io: 3`, `api: 26`, `concurrency: 40`, `import: 18`
* *Defense:* `safety: 6`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` types.ts, migrate-addon-console.ts, addon-console, async () => 
    const source = dedent`
      import, node:fs, common, node-logger, test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.storyExtraction.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2323.88 | **LOC:** 415 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.8429%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 131`, `args: 32`, `func_start: 26`, `class_start: 11`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 28`, `concurrency: 16`, `import: 27`
* *Defense:* `safety: 10`, `doc: 13`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AttachedMember, Button, Compound, DefaultExport, ForwardRefButton, GenericList, MemoButton, NamespaceCompound...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/getStorySortParameter.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1672.02 | **LOC:** 537 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.9027%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 87`, `args: 38`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 14`
* *Architecture:* `api: 32`, `import: 3`
* *Defense:* `safety: 7`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` getStorySortParameter.ts, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/create-storybook/src/services/FrameworkDetectionService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1482.81 | **LOC:** 326 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.0374%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 86`, `args: 38`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 2`
* *Architecture:* `concurrency: 28`, `import: 7`
* *Defense:* `safety: 2`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` FrameworkDetectionService.ts, find, common, node-logger, types, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/eslint-plugin/src/rules/await-interactions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1425.38 | **LOC:** 812 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 44 instances
* *Concurrency (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 181`, `args: 74`, `func_start: 56`
* *Risk/State:* `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `api: 24`, `concurrency: 139`, `import: 12`
* *Defense:* `safety: 6`, `doc: 1`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` await-interactions.ts, test-utils.ts, utils, jest, test, testing-library, ts-dedent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/shared/universal-store/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1348.23 | **LOC:** 1226 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.6574%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 182`, `args: 71`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 15`
* *Architecture:* `concurrency: 40`, `import: 6`
* *Defense:* `safety: 13`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` instances.ts, index.ts, mock.ts, types.ts, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/cli-storybook/src/automigrate/fixes/fix-faux-esm-require.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1343.89 | **LOC:** 437 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.9788%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 107`, `args: 29`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1`
* *Architecture:* `io: 26`, `api: 14`, `concurrency: 28`, `import: 45`
* *Defense:* `safety: 11`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` mainConfigFile.ts, config, fix-faux-esm-require.ts, some-config, addon-essentials, promises, node:module, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaManager.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1330.45 | **LOC:** 388 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.6632%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 71`, `args: 31`, `func_start: 12`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 27`, `api: 14`, `import: 23`
* *Defense:* `safety: 8`, `test: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.154
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` getComponentImports.ts, Button, Card, ComponentMetaManager.ts, Tag, test-helpers.ts, node:fs, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `code/renderers/react/src/componentManifest/generator.ts` -> Churn: **76.53%** | Cog Load: 54.0408% | Debt: 0.0%
- `scripts/utils/yarn.ts` -> Churn: **63.16%** | Cog Load: 87.7023% | Debt: 15.5998%
- `code/addons/vitest/src/vitest-plugin/index.ts` -> Churn: **62.15%** | Cog Load: 87.037% | Debt: 9.9474%
- `code/core/src/manager-api/modules/stories.ts` -> Churn: **59.96%** | Cog Load: 57.0558% | Debt: 30.0753%
- `code/core/src/core-server/presets/common-preset.ts` -> Churn: **58.78%** | Cog Load: 71.5865% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.props.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 8183.09
- `code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 7090.13
- `code/addons/vitest/src/updateVitestFile.config.4.test.ts` -> **Valentin Palkovic** (83.3% isolated ownership) | Magnitude: 6706.69
- `code/core/src/manager/components/sidebar/mockdata.large.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 6318.32
- `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 5969.07

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `scripts/task.ts` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 92.7441%)
- `scripts/tasks/sandbox-parts.ts` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 86.2458%)
- `code/addons/vitest/src/node/test-manager.ts` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 99.486%)
- `scripts/tasks/sandbox.ts` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 72.9865%)
- `code/core/src/manager-api/root.tsx` -> **Severity: 0.024** (Bridge: 0.0003 * Flux: 72.4199%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `code/addons/vitest/src/node/vitest.ts` -> **Severity: 4.396** (Embedded: 0.0879 * Error Risk: 49.9994%)
- `code/addons/vitest/src/node/test-manager.ts` -> **Severity: 3.511** (Embedded: 0.0521 * Error Risk: 67.3863%)
- `code/core/src/preview-api/modules/addons/main.ts` -> **Severity: 3.411** (Embedded: 0.0403 * Error Risk: 84.7391%)
- `scripts/ecosystem-ci/test.sh` -> **Severity: 3.248** (Embedded: 0.0519 * Error Risk: 62.5811%)
- `code/core/src/bin/core.ts` -> **Severity: 2.379** (Embedded: 0.0248 * Error Risk: 95.9367%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `code/core/src/components/components/typography/lib/common.tsx` -> **Severity: 2993.2** (Blast Radius: 29.932 * Doc Risk: 100.0%)
- `code/addons/vitest/src/node/test-manager.ts` -> **Severity: 2602.2** (Blast Radius: 26.022 * Doc Risk: 100.0%)
- `code/addons/vitest/src/node/vitest.ts` -> **Severity: 2527.8** (Blast Radius: 25.278 * Doc Risk: 100.0%)
- `code/core/src/preview-api/modules/addons/main.ts` -> **Severity: 1599.8** (Blast Radius: 15.998 * Doc Risk: 100.0%)
- `code/addons/vitest/src/node/vitest-manager.ts` -> **Severity: 1021.809** (Blast Radius: 11.147 * Doc Risk: 91.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
