# ARCHITECTURAL_BRIEF: cypress
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/cypress` |
| **Timestamp** | `2026-08-07T04:23:48.210994+00:00` |
| **Scan Duration** | `13.1s` |
| **Git Branch** | `develop` |
| **Git Commit** | `58bbebcbcd6d685956dd9bcd3bf58d93bac5f998` |
| **Git Remote** | `https://github.com/cypress-io/cypress.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2837 malicious artifacts.

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
| Total Artifacts | 6958 |
| Analyzed Artifacts (Scanned) | 4611 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2347 |
| Total LOC | 227446 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7479 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.326 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2377 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 154 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1617 | 124882 | 35.1% |
| JAVASCRIPT | 1211 | 43762 | 26.3% |
| HTML | 614 | 37191 | 13.3% |
| JSON | 314 | 15201 | 6.8% |
| MARKDOWN | 277 | 0 | 6.0% |
| XML | 245 | 30 | 5.3% |
| PLAINTEXT | 209 | 5 | 4.5% |
| CSS | 105 | 4936 | 2.3% |
| SHELL | 9 | 268 | 0.2% |
| YAML | 6 | 1160 | 0.1% |
| CSV | 4 | 11 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.901`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3196 | 69.3% |
| file_cluster_13 | 534 | 11.6% |
| file_cluster_4 | 125 | 2.7% |
| file_cluster_2 | 78 | 1.7% |
| file_cluster_0 | 71 | 1.5% |
| file_cluster_17 | 40 | 0.9% |
| file_cluster_11 | 28 | 0.6% |
| file_cluster_9 | 15 | 0.3% |
| file_cluster_16 | 13 | 0.3% |
| file_cluster_1 | 8 | 0.2% |
| Unknown | 5 | 0.1% |
| file_cluster_6 | 3 | 0.1% |
| file_cluster_12 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 481 | 10.4% |
| Static: Minified & Vendor Opaque Mass | 12 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2347*

**Composition by Extension & Reason:**
- `.ts`: 796x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 257 LOC)
- `.js`: 589x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 70 LOC)
- `.ansi`: 156x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 118x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.js"')
- `.lock`: 107x Excluded (Unsupported Extension: '.lock'), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 5877 LOC), 2x Excluded (Massive Static Asset Blob: 3975 LOC)
- `.png`: 80x Excluded (Explicitly Denied Extension: '.png')
- `.html`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 59 exceeds 500 chars), 1x Excluded (Saturation: Line 53 exceeds 500 chars)
- `.vue`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 25 exceeds 500 chars)
- `.jsx`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.tsx`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.patch`: 30x Excluded (Unsupported Extension: '.patch')
- `.md`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 46 LOC), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.yml`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2869 LOC)
- `.coffee`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.coffee')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 16.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.6 | 2.0 | 2.3 |
| API Exposure | 0.0 | 19.4 | 2.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 72.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.4 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 54.0 | 1.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.2 | 17.9 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `system-tests/projects/e2e/elements.html` (Hits: 3500)
- `packages/driver/cypress/e2e/commands/request.cy.js` (Hits: 166)
- `system-tests/project-fixtures/runner-specs/cypress/fixtures/commandsActions.html` (Hits: 111)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vue.svg** (`packages/frontend-shared/src/assets/logos/vue.svg`) — 279 inbound connections
2. **react.svg** (`packages/frontend-shared/src/assets/logos/react.svg`) — 272 inbound connections
3. **lodash.ts** (`packages/driver/src/config/lodash.ts`) — 225 inbound connections
4. **debug.js** (`scripts/debug.js`) — 118 inbound connections
5. **error_utils.ts** (`packages/driver/src/cypress/error_utils.ts`) — 78 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cypress.ts** (`packages/driver/src/cypress.ts`) — 45 outbound dependencies
2. **node_builtins.cy.js** (`system-tests/projects/node-builtins/cypress/e2e/node_builtins.cy.js`) — 36 outbound dependencies
3. **index.ts** (`packages/data-context/graphql/schemaTypes/objectTypes/index.ts`) — 36 outbound dependencies
4. **cy.ts** (`packages/driver/src/cypress/cy.ts`) — 36 outbound dependencies
5. **index.ts** (`packages/driver/src/cy/commands/index.ts`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `describe` (@ `packages/driver/cypress/e2e/commands/waiting.cy.js`) -> Impact: **277.3** | LOC: 1424
- `context` (@ `packages/driver/cypress/e2e/commands/waiting.cy.js`) -> Impact: **277.2** | LOC: 1422
- `describe` (@ `packages/driver/cypress/e2e/e2e/origin/cookie_behavior.cy.ts`) -> Impact: **241.4** | LOC: 1259
- `create` (@ `packages/driver/src/cy/chai/inspect.ts`) -> Impact: **218.8** | LOC: 416
  * *Intent:* // let config = require('../config')
- `describe` (@ `packages/driver/cypress/e2e/commands/actions/click.cy.ts`) -> Impact: **206.7** | LOC: 1710
- `describe` (@ `cli/types/tests/net-stubbing-tests.ts`) -> Impact: **178.3** | LOC: 587
- `describe` (@ `packages/driver/cypress/e2e/commands/actions/type_special_chars.cy.ts`) -> Impact: **174.6** | LOC: 1690
- `getKeyDetails` (@ `packages/driver/src/cy/keyboard.ts`) -> Impact: **167.6** | LOC: 512
- `describe` (@ `packages/driver/cypress/e2e/commands/cookies.cy.js`) -> Impact: **147.7** | LOC: 1638
- `describe` (@ `packages/driver/cypress/e2e/commands/connectors.cy.js`) -> Impact: **144.9** | LOC: 1651

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/driver/cypress/e2e/commands` | 26 | 12050.05 | 62.1% | 100.0% |
| `__monolith__` | 21 | 5213.14 | 3.09% | 0.0% |
| `cli` | 11 | 5099.0 | 2.37% | 7.36% |
| `npm/vue` | 12 | 5082.12 | 3.64% | 0.0% |
| `npm/webpack-preprocessor` | 11 | 5053.33 | 2.54% | 7.13% |
| `npm/svelte` | 9 | 5050.62 | 3.54% | 0.0% |
| `packages/driver/cypress/e2e/cypress` | 23 | 2797.82 | 28.18% | 100.0% |
| `packages/app/src/specs` | 54 | 2679.48 | 3.68% | 0.0% |
| `packages/frontend-shared/src/assets/icons` | 200 | 2084.96 | 4.95% | 0.0% |
| `system-tests/projects/e2e/cypress/e2e` | 120 | 2053.87 | 14.59% | 85.12% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `npm/eslint-plugin-dev/lib/scripts/lint-changed.js` -> **100.0%** Exposure
- `npm/eslint-plugin-dev/lib/scripts/lint-pre-push.js` -> **100.0%** Exposure
- `npm/eslint-plugin-dev/lib/scripts/lint-staged.js` -> **100.0%** Exposure
- `npm/eslint-plugin-dev/lib/scripts/utils.js` -> **100.0%** Exposure
- `npm/react/cypress/component/advanced/app-action-example/counter.cy.jsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `npm/react/cypress/component/basic/counter-set-state/counter.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/error-boundary.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/hello-x.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/toggle-example/toggle.jsx` -> **100.0%** Exposure
- `npm/react/cypress/component/basic/transpiled.jsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/driver/cypress/e2e/commands/actions/type_special_chars.cy.ts` -> **0** Orphaned Functions | **280** Duplicates
- `packages/driver/cypress/e2e/commands/connectors.cy.js` -> **0** Orphaned Functions | **256** Duplicates
- `packages/driver/cypress/e2e/commands/cookies.cy.js` -> **0** Orphaned Functions | **252** Duplicates
- `packages/driver/cypress/e2e/commands/actions/click.cy.ts` -> **2** Orphaned Functions | **240** Duplicates
- `packages/driver/cypress/e2e/commands/actions/type.cy.ts` -> **0** Orphaned Functions | **242** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/server/start-cypress.js`** -> AI Confidence: **99.48%**
2. **`scripts/binary/binary-integrity-check-source.js`** -> AI Confidence: **99.32%**
3. **`system-tests/projects/v8-snapshot/esm/index.js`** -> AI Confidence: **99.32%**
4. **`scripts/get-next-version.js`** -> AI Confidence: **99.31%**
5. **`npm/angular/src/mount.ts`** -> AI Confidence: **99.31%**
6. **`npm/cypress-schematic/src/schematics/ng-add/index.ts`** -> AI Confidence: **99.31%**
7. **`npm/webpack-batteries-included-preprocessor/index.ts`** -> AI Confidence: **99.31%**
8. **`npm/webpack-preprocessor/index.ts`** -> AI Confidence: **99.31%**
9. **`packages/app/src/runner/aut-iframe.ts`** -> AI Confidence: **99.31%**
10. **`packages/data-context/graphql/makeGraphQLServer.ts`** -> AI Confidence: **99.31%**
11. **`packages/data-context/src/actions/WizardActions.ts`** -> AI Confidence: **99.31%**
12. **`packages/data-context/src/data/ProjectLifecycleManager.ts`** -> AI Confidence: **99.31%**
13. **`packages/data-context/src/sources/GitDataSource.ts`** -> AI Confidence: **99.31%**
14. **`packages/data-context/src/sources/RelevantRunsDataSource.ts`** -> AI Confidence: **99.31%**
15. **`packages/data-context/src/sources/RemoteRequestDataSource.ts`** -> AI Confidence: **99.31%**
16. **`packages/driver/src/cy/actionability.ts`** -> AI Confidence: **99.31%**
17. **`packages/driver/src/cy/commands/actions/focus.ts`** -> AI Confidence: **99.31%**
18. **`packages/driver/src/cy/commands/cookies.ts`** -> AI Confidence: **99.31%**
19. **`packages/driver/src/cy/commands/navigation.ts`** -> AI Confidence: **99.31%**
20. **`packages/driver/src/cy/commands/querying/querying.ts`** -> AI Confidence: **99.31%**
21. **`packages/driver/src/cy/keyboard.ts`** -> AI Confidence: **99.31%**
22. **`packages/driver/src/cy/net-stubbing/add-command.ts`** -> AI Confidence: **99.31%**
23. **`packages/electron/src/open.ts`** -> AI Confidence: **99.31%**
24. **`packages/frontend-shared/src/graphql/urqlClient.ts`** -> AI Confidence: **99.31%**
25. **`packages/packherd-require/src/require.ts`** -> AI Confidence: **99.31%**
26. **`packages/reporter/src/attempts/attempt-model.ts`** -> AI Confidence: **99.31%**
27. **`packages/reporter/src/header/controls.tsx`** -> AI Confidence: **99.31%**
28. **`packages/reporter/src/runnables/runnable-popover-options.tsx`** -> AI Confidence: **99.31%**
29. **`packages/v8-snapshot-require/src/snapshot-require.ts`** -> AI Confidence: **99.31%**
30. **`scripts/gulp/utils/childProcessUtils.ts`** -> AI Confidence: **99.31%**
31. **`tooling/electron-mksnapshot/src/mksnapshot-run.ts`** -> AI Confidence: **99.31%**
32. **`tooling/v8-snapshot/src/doctor/process-script.worker.ts`** -> AI Confidence: **99.31%**
33. **`tooling/v8-snapshot/src/doctor/snapshot-doctor.ts`** -> AI Confidence: **99.31%**
34. **`tooling/v8-snapshot/src/generator/create-snapshot-script.ts`** -> AI Confidence: **99.31%**
35. **`tooling/v8-snapshot/src/generator/snapshot-generator.ts`** -> AI Confidence: **99.31%**
36. **`tooling/v8-snapshot/src/utils.ts`** -> AI Confidence: **99.31%**
37. **`cli/bin/cypress`** -> AI Confidence: **99.29%**
38. **`packages/data-context/index.js`** -> AI Confidence: **99.29%**
39. **`packages/driver/cypress/fixtures/issue-6125.js`** -> AI Confidence: **99.29%**
40. **`packages/driver/cypress/fixtures/security.js`** -> AI Confidence: **99.29%**
41. **`packages/frontend-shared/index.js`** -> AI Confidence: **99.29%**
42. **`packages/frontend-shared/script/generate-shiki-theme.js`** -> AI Confidence: **99.29%**
43. **`packages/frontend-shared/script/generate-stub-specs.js`** -> AI Confidence: **99.29%**
44. **`packages/proxy/index.js`** -> AI Confidence: **99.29%**
45. **`packages/rewriter/index.js`** -> AI Confidence: **99.29%**
46. **`packages/rewriter/script/worker-shim.js`** -> AI Confidence: **99.29%**
47. **`packages/server/hook-require.js`** -> AI Confidence: **99.29%**
48. **`scripts/check-node-version.js`** -> AI Confidence: **99.29%**
49. **`scripts/check-terminal.js`** -> AI Confidence: **99.29%**
50. **`scripts/run-postInstall.js`** -> AI Confidence: **99.29%**
51. **`scripts/semantic-commits/change-categories.js`** -> AI Confidence: **99.29%**
52. **`scripts/windows-sign.js`** -> AI Confidence: **99.29%**
53. **`system-tests/projects/config-screenshot-on-failure-enabled/cypress/e2e/issue-5016.cy.js`** -> AI Confidence: **99.29%**
54. **`system-tests/projects/e2e/cypress/e2e/network_error_handling.cy.js`** -> AI Confidence: **99.29%**
55. **`system-tests/projects/e2e/static/obstructive_code.js`** -> AI Confidence: **99.29%**
56. **`system-tests/projects/e2e/static/simple_obstructive_code.js`** -> AI Confidence: **99.29%**
57. **`system-tests/projects/plugin-extension/ext/content.js`** -> AI Confidence: **99.29%**
58. **`system-tests/projects/svelte-webpack-configured/webpack.config.js`** -> AI Confidence: **99.29%**
59. **`system-tests/projects/svelte-webpack-unconfigured/webpack.config.js`** -> AI Confidence: **99.29%**
60. **`tooling/v8-snapshot/scripts/setup-v8-snapshot-in-cypress.js`** -> AI Confidence: **99.29%**
61. **`packages/driver/cypress/e2e/e2e/abort_beforeunload_event.cy.ts`** -> AI Confidence: **99.29%**
62. **`packages/driver/cypress/e2e/e2e/abort_beforeunload_event_child.cy.ts`** -> AI Confidence: **99.29%**
63. **`packages/driver/cypress/e2e/e2e/abort_onbeforeunload.cy.ts`** -> AI Confidence: **99.29%**
64. **`packages/driver/cypress/e2e/e2e/abort_onbeforeunload_child.cy.ts`** -> AI Confidence: **99.29%**
65. **`packages/driver/types/cypress/log.d.ts`** -> AI Confidence: **99.29%**
66. **`packages/driver/types/internal-types.d.ts`** -> AI Confidence: **99.29%**
67. **`system-tests/projects/e2e/cypress/e2e/abort_beforeunload_event.cy.ts`** -> AI Confidence: **99.29%**
68. **`system-tests/projects/e2e/cypress/e2e/abort_beforeunload_event_child.cy.ts`** -> AI Confidence: **99.29%**
69. **`scripts/ensure-dependencies.sh`** -> AI Confidence: **99.29%**
70. **`scripts/ensure-node.sh`** -> AI Confidence: **99.29%**
71. **`scripts/pack-ci.sh`** -> AI Confidence: **99.29%**
72. **`scripts/add-install-comment.js`** -> AI Confidence: **99.24%**
73. **`npm/vite-dev-server/src/resolveConfig.ts`** -> AI Confidence: **99.24%**
74. **`npm/vite-plugin-cypress-esm/src/index.ts`** -> AI Confidence: **99.24%**
75. **`npm/webpack-dev-server/src/helpers/nextHandler.ts`** -> AI Confidence: **99.24%**
76. **`npm/webpack-dev-server/src/makeWebpackConfig.ts`** -> AI Confidence: **99.24%**
77. **`packages/data-context/src/sources/ProjectDataSource.ts`** -> AI Confidence: **99.24%**
78. **`packages/data-context/src/util/config-file-updater.ts`** -> AI Confidence: **99.24%**
79. **`packages/driver/src/cy/commands/actions/select.ts`** -> AI Confidence: **99.24%**
80. **`packages/driver/src/cy/commands/origin/index.ts`** -> AI Confidence: **99.24%**
81. **`packages/driver/src/cy/commands/screenshot.ts`** -> AI Confidence: **99.24%**
82. **`packages/driver/src/cy/commands/task.ts`** -> AI Confidence: **99.24%**
83. **`packages/driver/src/cy/commands/waiting.ts`** -> AI Confidence: **99.24%**
84. **`packages/driver/src/cypress/command_queue.ts`** -> AI Confidence: **99.24%**
85. **`packages/driver/src/cypress/commands.ts`** -> AI Confidence: **99.24%**
86. **`packages/driver/src/cypress/cy.ts`** -> AI Confidence: **99.24%**
87. **`packages/driver/src/cypress/runner.ts`** -> AI Confidence: **99.24%**
88. **`packages/driver/src/dom/visibility.ts`** -> AI Confidence: **99.24%**
89. **`packages/packherd-require/src/transpile-ts.ts`** -> AI Confidence: **99.24%**
90. **`packages/reporter/src/commands/command.tsx`** -> AI Confidence: **99.24%**
91. **`packages/reporter/src/runnables/runnable-and-suite.tsx`** -> AI Confidence: **99.24%**
92. **`packages/reporter/src/test/test-model.ts`** -> AI Confidence: **99.24%**
93. **`scripts/binary/util/packages.ts`** -> AI Confidence: **99.24%**
94. **`scripts/semantic-commits/get-binary-release-data.js`** -> AI Confidence: **99.23%**
95. **`packages/data-context/src/actions/CodegenActions.ts`** -> AI Confidence: **99.23%**
96. **`packages/data-context/src/codegen/spec-options.ts`** -> AI Confidence: **99.23%**
97. **`packages/data-context/src/data/coreDataShape.ts`** -> AI Confidence: **99.23%**
98. **`packages/driver/src/cy/commands/actions/scroll.ts`** -> AI Confidence: **99.23%**
99. **`packages/driver/src/cy/commands/sessions/index.ts`** -> AI Confidence: **99.23%**
100. **`packages/driver/src/cy/net-stubbing/events/before-request.ts`** -> AI Confidence: **99.23%**
101. **`packages/driver/src/cy/net-stubbing/events/response.ts`** -> AI Confidence: **99.23%**
102. **`packages/driver/src/cy/retries.ts`** -> AI Confidence: **99.23%**
103. **`packages/driver/src/cypress/error_utils.ts`** -> AI Confidence: **99.23%**
104. **`packages/driver/src/cypress/stack_utils.ts`** -> AI Confidence: **99.23%**
105. **`packages/driver/src/cypress/utils.ts`** -> AI Confidence: **99.23%**
106. **`packages/server/test/scripts/run.js`** -> AI Confidence: **99.22%**
107. **`system-tests/scripts/run.js`** -> AI Confidence: **99.22%**
108. **`scripts/semantic-commits/parse-changelog.js`** -> AI Confidence: **99.2%**
109. **`npm/grep/src/register.ts`** -> AI Confidence: **99.2%**
110. **`scripts/binary/index.js`** -> AI Confidence: **99.18%**
111. **`scripts/binary/smoke.js`** -> AI Confidence: **99.18%**
112. **`scripts/binary/util/upload.js`** -> AI Confidence: **99.18%**
113. **`scripts/binary/zip.js`** -> AI Confidence: **99.18%**
114. **`scripts/unit/binary/util/packages-spec.js`** -> AI Confidence: **99.18%**
115. **`npm/webpack-dev-server/src/devServer.ts`** -> AI Confidence: **99.18%**
116. **`packages/data-context/src/DataContext.ts`** -> AI Confidence: **99.18%**
117. **`packages/data-context/src/codegen/code-generator.ts`** -> AI Confidence: **99.18%**
118. **`packages/data-context/src/data/ProjectConfigIpc.ts`** -> AI Confidence: **99.18%**
119. **`packages/data-context/src/sources/FileDataSource.ts`** -> AI Confidence: **99.18%**
120. **`packages/driver/src/cross-origin/cypress.ts`** -> AI Confidence: **99.18%**
121. **`packages/driver/src/cy/commands/actions/submit.ts`** -> AI Confidence: **99.18%**
122. **`packages/driver/src/cy/commands/window.ts`** -> AI Confidence: **99.18%**
123. **`packages/driver/src/dom/elements/complexElements.ts`** -> AI Confidence: **99.18%**
124. **`packages/electron/src/install.ts`** -> AI Confidence: **99.18%**
125. **`packages/errors/src/errors.ts`** -> AI Confidence: **99.18%**
126. **`packages/eslint-config/src/baseConfig.ts`** -> AI Confidence: **99.18%**
127. **`packages/frontend-shared/cypress/e2e/e2ePluginSetup.ts`** -> AI Confidence: **99.18%**
128. **`packages/frontend-shared/cypress/support/e2e.ts`** -> AI Confidence: **99.18%**
129. **`packages/reporter/src/header/header.tsx`** -> AI Confidence: **99.18%**
130. **`packages/reporter/src/hooks/hooks.tsx`** -> AI Confidence: **99.18%**
131. **`packages/reporter/src/test/test.tsx`** -> AI Confidence: **99.18%**
132. **`packages/scaffold-config/src/frameworks.ts`** -> AI Confidence: **99.18%**
133. **`packages/telemetry/src/node.ts`** -> AI Confidence: **99.18%**
134. **`scripts/binary/build.ts`** -> AI Confidence: **99.18%**
135. **`scripts/gulp/tasks/gulpCloudDeliveredTypes.ts`** -> AI Confidence: **99.18%**
136. **`scripts/gulp/tasks/gulpCypress.ts`** -> AI Confidence: **99.18%**
137. **`scripts/gulp/tasks/gulpMakePackage.ts`** -> AI Confidence: **99.18%**
138. **`scripts/gulp/utils/nexusTypegenUtil.ts`** -> AI Confidence: **99.18%**
139. **`tooling/v8-snapshot/src/setup/install-snapshot.ts`** -> AI Confidence: **99.18%**
140. **`packages/driver/cypress/fixtures/aut-commands.js`** -> AI Confidence: **99.17%**
141. **`scripts/cypress.js`** -> AI Confidence: **99.17%**
142. **`scripts/verify-accessibility-results.js`** -> AI Confidence: **99.17%**
143. **`system-tests/projects/rename.js`** -> AI Confidence: **99.17%**
144. **`packages/driver/src/config/jquery.scrollto.ts`** -> AI Confidence: **99.17%**
145. **`packages/driver/src/cy/chai.ts`** -> AI Confidence: **99.17%**
146. **`packages/driver/src/cy/net-stubbing/static-response-utils.ts`** -> AI Confidence: **99.17%**
147. **`packages/driver/src/cypress/UsKeyboardLayout.ts`** -> AI Confidence: **99.17%**
148. **`packages/frontend-shared/vite.config.mjs`** -> AI Confidence: **99.16%**
149. **`scripts/circle-cache.js`** -> AI Confidence: **99.16%**
150. **`npm/vue/src/index.ts`** -> AI Confidence: **99.16%**
151. **`packages/app/src/runner/event-manager.ts`** -> AI Confidence: **99.16%**
152. **`packages/app/src/runner/index.ts`** -> AI Confidence: **99.16%**
153. **`packages/app/src/runner/unifiedRunner.ts`** -> AI Confidence: **99.16%**
154. **`packages/config/src/ast-utils/addToCypressConfig.ts`** -> AI Confidence: **99.16%**
155. **`packages/config/src/project/utils.ts`** -> AI Confidence: **99.16%**
156. **`packages/data-context/graphql/plugins/nexusRemoteFieldPlugin.ts`** -> AI Confidence: **99.16%**
157. **`packages/data-context/src/actions/ProjectActions.ts`** -> AI Confidence: **99.16%**
158. **`packages/data-context/src/data/ProjectConfigManager.ts`** -> AI Confidence: **99.16%**
159. **`packages/data-context/src/sources/CloudDataSource.ts`** -> AI Confidence: **99.16%**
160. **`packages/data-context/src/sources/GraphQLDataSource.ts`** -> AI Confidence: **99.16%**
161. **`packages/driver/src/cy/mouse.ts`** -> AI Confidence: **99.16%**
162. **`packages/reporter/src/errors/test-error.tsx`** -> AI Confidence: **99.16%**
163. **`packages/reporter/src/main.tsx`** -> AI Confidence: **99.16%**
164. **`packages/reporter/src/runnables/runnables-store.ts`** -> AI Confidence: **99.16%**
165. **`scripts/gulp/gulpfile.ts`** -> AI Confidence: **99.16%**
166. **`scripts/gulp/tasks/gulpGraphql.ts`** -> AI Confidence: **99.16%**
167. **`scripts/binary/upload-build-artifact.js`** -> AI Confidence: **99.15%**
168. **`scripts/binary/util/testStaticAssets.js`** -> AI Confidence: **99.15%**
169. **`npm/cypress-schematic/src/builders/cypress/index.ts`** -> AI Confidence: **99.15%**
170. **`npm/cypress-schematic/src/schematics/utils/index.ts`** -> AI Confidence: **99.15%**
171. **`npm/vite-dev-server/src/plugins/cypress.ts`** -> AI Confidence: **99.15%**
172. **`npm/webpack-dev-server/src/helpers/angularHandler.ts`** -> AI Confidence: **99.15%**
173. **`npm/webpack-dev-server/src/makeDefaultWebpackConfig.ts`** -> AI Confidence: **99.15%**
174. **`packages/app/src/runner/useRunnerStyle.ts`** -> AI Confidence: **99.15%**
175. **`packages/data-context/graphql/stitching/remoteSchemaWrapped.ts`** -> AI Confidence: **99.15%**
176. **`packages/data-context/src/sources/RelevantRunSpecsDataSource.ts`** -> AI Confidence: **99.15%**
177. **`packages/driver/src/cross-origin/origin_fn.ts`** -> AI Confidence: **99.15%**
178. **`packages/driver/src/cy/commands/actions/click.ts`** -> AI Confidence: **99.15%**
179. **`packages/driver/src/cy/commands/actions/selectFile.ts`** -> AI Confidence: **99.15%**
180. **`packages/driver/src/cy/commands/actions/type.ts`** -> AI Confidence: **99.15%**
181. **`packages/driver/src/cy/net-stubbing/events/index.ts`** -> AI Confidence: **99.15%**
182. **`packages/driver/src/cy/snapshots.ts`** -> AI Confidence: **99.15%**
183. **`packages/driver/src/cypress/log.ts`** -> AI Confidence: **99.15%**
184. **`packages/driver/src/dom/elements/find.ts`** -> AI Confidence: **99.15%**
185. **`packages/errors/src/errTemplate.ts`** -> AI Confidence: **99.15%**
186. **`packages/reporter/src/runnables/runnable-header.tsx`** -> AI Confidence: **99.15%**
187. **`packages/scaffold-config/src/detect.ts`** -> AI Confidence: **99.15%**
188. **`packages/server/test/unit/cloud/api/utils/fake_proxy_server.ts`** -> AI Confidence: **99.15%**
189. **`packages/types/src/protocol.ts`** -> AI Confidence: **99.15%**
190. **`packages/types/src/server.ts`** -> AI Confidence: **99.15%**
191. **`packages/web-config/webpack.config.base.ts`** -> AI Confidence: **99.15%**
192. **`packages/server/index.js`** -> AI Confidence: **99.13%**
193. **`scripts/npm-release.js`** -> AI Confidence: **99.13%**
194. **`scripts/semantic-commits/validate-binary-changelog.js`** -> AI Confidence: **99.13%**
195. **`scripts/type_check.js`** -> AI Confidence: **99.13%**
196. **`scripts/verify-mocha-results.js`** -> AI Confidence: **99.13%**
197. **`system-tests/scripts/projects-yarn-install.js`** -> AI Confidence: **99.13%**
198. **`npm/grep/src/plugin.ts`** -> AI Confidence: **99.13%**
199. **`packages/app/src/composables/useRelevantRun.ts`** -> AI Confidence: **99.13%**
200. **`packages/app/src/specs/banners/index.ts`** -> AI Confidence: **99.13%**
201. **`packages/app/src/store/studio-store.ts`** -> AI Confidence: **99.13%**
202. **`packages/data-context/src/sources/ErrorDataSource.ts`** -> AI Confidence: **99.13%**
203. **`packages/data-context/src/sources/VersionsDataSource.ts`** -> AI Confidence: **99.13%**
204. **`packages/data-context/src/util/files.ts`** -> AI Confidence: **99.13%**
205. **`packages/driver/src/cross-origin/communicator.ts`** -> AI Confidence: **99.13%**
206. **`packages/driver/src/cy/commands/env.ts`** -> AI Confidence: **99.13%**
207. **`packages/driver/src/cy/commands/files.ts`** -> AI Confidence: **99.13%**
208. **`packages/driver/src/cy/commands/request.ts`** -> AI Confidence: **99.13%**
209. **`packages/driver/src/cypress/mocha.ts`** -> AI Confidence: **99.13%**
210. **`packages/driver/src/cypress/state.ts`** -> AI Confidence: **99.13%**
211. **`packages/packherd-require/src/sourcemap-support.ts`** -> AI Confidence: **99.13%**
212. **`packages/reporter/src/collapsible/collapsible.tsx`** -> AI Confidence: **99.13%**
213. **`packages/reporter/src/commands/command-model.ts`** -> AI Confidence: **99.13%**
214. **`tooling/electron-mksnapshot/src/mksnapshot-download.ts`** -> AI Confidence: **99.13%**
215. **`tooling/v8-snapshot/src/doctor/determine-deferred.ts`** -> AI Confidence: **99.13%**
216. **`scripts/debug.js`** -> AI Confidence: **99.11%**
217. **`packages/driver/cypress/e2e/cypress/stack_utils-invocationDetails.cy.ts`** -> AI Confidence: **99.11%**
218. **`packages/electron/src/electron.ts`** -> AI Confidence: **99.11%**
219. **`packages/example/bin/convert.js`** -> AI Confidence: **99.09%**
220. **`scripts/after-sign-hook.js`** -> AI Confidence: **99.09%**
221. **`scripts/binary/binary-entry-point-source.js`** -> AI Confidence: **99.09%**
222. **`scripts/github-actions/semantic-pull-request/index.js`** -> AI Confidence: **99.09%**
223. **`system-tests/projects/module-api/index.js`** -> AI Confidence: **99.09%**
224. **`system-tests/projects/node-builtins/cypress/e2e/node_builtins.cy.js`** -> AI Confidence: **99.09%**
225. **`npm/angular-zoneless/src/mount.ts`** -> AI Confidence: **99.09%**
226. **`packages/app/cypress/support/fixtures.ts`** -> AI Confidence: **99.09%**
227. **`packages/app/src/composables/useTestingType.ts`** -> AI Confidence: **99.09%**
228. **`packages/app/src/main.ts`** -> AI Confidence: **99.09%**
229. **`packages/app/src/runner/iframe-model.ts`** -> AI Confidence: **99.09%**
230. **`packages/app/src/specs/tree/useVirtualListNavigation.ts`** -> AI Confidence: **99.09%**
231. **`packages/data-context/graphql/schemaTypes/enumTypes/index.ts`** -> AI Confidence: **99.09%**
232. **`packages/data-context/graphql/schemaTypes/objectTypes/index.ts`** -> AI Confidence: **99.09%**
233. **`packages/data-context/src/actions/index.ts`** -> AI Confidence: **99.09%**
234. **`packages/data-context/src/polling/poller.ts`** -> AI Confidence: **99.09%**
235. **`packages/data-context/src/sources/index.ts`** -> AI Confidence: **99.09%**
236. **`packages/data-context/src/util/index.ts`** -> AI Confidence: **99.09%**
237. **`packages/driver/src/cy/commands/actions/index.ts`** -> AI Confidence: **99.09%**
238. **`packages/driver/src/cy/commands/clock.ts`** -> AI Confidence: **99.09%**
239. **`packages/driver/src/cy/commands/index.ts`** -> AI Confidence: **99.09%**
240. **`packages/driver/src/cy/net-stubbing/route-matcher-log.ts`** -> AI Confidence: **99.09%**
241. **`packages/driver/src/cypress/screenshot.ts`** -> AI Confidence: **99.09%**
242. **`packages/driver/src/dom/elements/index.ts`** -> AI Confidence: **99.09%**
243. **`packages/driver/src/dom/elements/nativeProps.ts`** -> AI Confidence: **99.09%**
244. **`packages/driver/src/util/serialization/log.ts`** -> AI Confidence: **99.09%**
245. **`packages/frontend-shared/script/generate-stub-specs-ts.ts`** -> AI Confidence: **99.09%**
246. **`packages/types/src/index.ts`** -> AI Confidence: **99.09%**
247. **`tooling/electron-mksnapshot/src/process-args-from-file.ts`** -> AI Confidence: **99.09%**
248. **`packages/driver/cypress/plugins/server.js`** -> AI Confidence: **99.08%**
249. **`scripts/after-pack-hook.js`** -> AI Confidence: **99.08%**
250. **`scripts/unit/binary/move-binaries-spec.js`** -> AI Confidence: **99.08%**
251. **`system-tests/projects/module-api/test/spec.js`** -> AI Confidence: **99.08%**
252. **`npm/vite-dev-server/src/getVite.ts`** -> AI Confidence: **99.08%**
253. **`packages/app/src/store/index.ts`** -> AI Confidence: **99.08%**
254. **`packages/app/src/store/run-all-specs-store.ts`** -> AI Confidence: **99.08%**
255. **`packages/config/src/project/index.ts`** -> AI Confidence: **99.08%**
256. **`packages/data-context/graphql/schemaTypes/objectTypes/gql-Mutation.ts`** -> AI Confidence: **99.08%**
257. **`packages/data-context/graphql/schemaTypes/objectTypes/gql-Query.ts`** -> AI Confidence: **99.08%**
258. **`packages/data-context/src/actions/ElectronActions.ts`** -> AI Confidence: **99.08%**
259. **`packages/frontend-shared/src/components/Alert.cy.tsx`** -> AI Confidence: **99.08%**
260. **`packages/frontend-shared/src/utils/icons.ts`** -> AI Confidence: **99.08%**
261. **`packages/launchpad/src/main.ts`** -> AI Confidence: **99.08%**
262. **`packages/reporter/src/attempts/attempts.tsx`** -> AI Confidence: **99.08%**
263. **`packages/reporter/src/commands/command.cy.tsx`** -> AI Confidence: **99.08%**
264. **`packages/reporter/src/studio/StudioTest.tsx`** -> AI Confidence: **99.08%**
265. **`packages/scaffold-config/src/index.ts`** -> AI Confidence: **99.08%**
266. **`scripts/binary/move-binaries.ts`** -> AI Confidence: **99.08%**
267. **`system-tests/project-fixtures/angular/src/app/mount.cy.ts`** -> AI Confidence: **99.08%**
268. **`system-tests/projects/angular-21/src/app/mount.cy.ts`** -> AI Confidence: **99.08%**
269. **`tooling/v8-snapshot/src/v8-snapshot.ts`** -> AI Confidence: **99.08%**
270. **`npm/eslint-plugin-dev/lib/scripts/utils.js`** -> AI Confidence: **99.07%**
271. **`packages/driver/cypress/plugins/index.js`** -> AI Confidence: **99.07%**
272. **`scripts/binary/upload.js`** -> AI Confidence: **99.07%**
273. **`npm/react/src/mount.ts`** -> AI Confidence: **99.07%**
274. **`npm/vite-plugin-cypress-esm/cypress/component/edgeCases.cy.tsx`** -> AI Confidence: **99.07%**
275. **`packages/app/src/runner/SpecRunnerHeaderOpenMode.cy.tsx`** -> AI Confidence: **99.07%**
276. **`packages/app/src/runner/useEventManager.ts`** -> AI Confidence: **99.07%**
277. **`packages/app/src/specs/SpecsListBanners.cy.tsx`** -> AI Confidence: **99.07%**
278. **`packages/app/src/specs/generators/index.ts`** -> AI Confidence: **99.07%**
279. **`packages/data-context/graphql/schemaTypes/objectTypes/gql-CurrentProject.ts`** -> AI Confidence: **99.07%**
280. **`packages/data-context/graphql/schemaTypes/objectTypes/gql-Wizard.ts`** -> AI Confidence: **99.07%**
281. **`packages/frontend-shared/src/gql-components/modals/LoginModal.cy.tsx`** -> AI Confidence: **99.07%**
282. **`packages/reporter/cypress/e2e/runnables.cy.ts`** -> AI Confidence: **99.07%**
283. **`packages/reporter/cypress/e2e/unit/runnables_store.cy.ts`** -> AI Confidence: **99.07%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3574` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/app/src/runner/event-manager.ts` (TYPESCRIPT) -> Cumulative Risk: **740.95**
- **Archetype:** `file_cluster_4` (Distance: 14.03 IQR)
- **Magnitude:** 46.41 | **LOC:** 1071 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 21.1%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9967%), Cognitive Load (96.7482%)
- **Heaviest Functions:** `_addListeners` (Impact: 109.5), `handleBeforeScreenshot` (Impact: 15.1), `rerunSpec` (Impact: 15.1)

### 2. `packages/data-context/src/sources/EventCollectorSource.ts` (TYPESCRIPT) -> Cumulative Risk: **736.91**
- **Archetype:** `file_cluster_4` (Distance: 12.738 IQR)
- **Magnitude:** 13.11 | **LOC:** 79 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `sendLocalTestCounts` (Impact: 26.4), `debug` (Impact: 11.3), `debug` (Impact: 9.1)

### 3. `packages/data-context/src/actions/WizardActions.ts` (TYPESCRIPT) -> Cumulative Risk: **732.15**
- **Archetype:** `file_cluster_4` (Distance: 13.502 IQR)
- **Magnitude:** 66.66 | **LOC:** 393 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.6999%), Cognitive Load (96.6597%)
- **Heaviest Functions:** `setFramework` (Impact: 50.3), `scaffoldConfig` (Impact: 42.3), `initializeFramework` (Impact: 23.2)

### 4. `packages/data-context/src/data/ProjectConfigManager.ts` (TYPESCRIPT) -> Cumulative Risk: **727.2**
- **Archetype:** `file_cluster_4` (Distance: 13.96 IQR)
- **Magnitude:** 95.94 | **LOC:** 681 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `refreshLifecycle` (Impact: 100.4), `handleSetupTestingTypeReply` (Impact: 33.8), `loadTestingType` (Impact: 32.9)

### 5. `packages/data-context/src/actions/CohortsActions.ts` (TYPESCRIPT) -> Cumulative Risk: **723.82**
- **Archetype:** `file_cluster_4` (Distance: 11.865 IQR)
- **Magnitude:** 10.47 | **LOC:** 55 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9967%), Cognitive Load (99.9877%)
- **Heaviest Functions:** `insertCohort` (Impact: 18.2), `determineCohort` (Impact: 15.2), `debug` (Impact: 10.8)

### 6. `packages/data-context/src/actions/ProjectActions.ts` (TYPESCRIPT) -> Cumulative Risk: **720.22**
- **Archetype:** `file_cluster_4` (Distance: 13.92 IQR)
- **Magnitude:** 96.76 | **LOC:** 664 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (97.7649%), State Flux (95.0%)
- **Heaviest Functions:** `switchTestingTypesAndRelaunch` (Impact: 47.7), `launchProject` (Impact: 30.2), `toArray` (Impact: 20.2)

### 7. `packages/data-context/src/sources/ProjectDataSource.ts` (TYPESCRIPT) -> Cumulative Risk: **706.55**
- **Archetype:** `file_cluster_4` (Distance: 12.336 IQR)
- **Magnitude:** 65.7 | **LOC:** 627 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9512%), Tech Debt (98.4552%)
- **Heaviest Functions:** `debug` (Impact: 40.7), `specPatternsByTestingType` (Impact: 32.1), `defaultSpecFileName` (Impact: 30.1)

### 8. `packages/data-context/src/polling/poller.ts` (TYPESCRIPT) -> Cumulative Risk: **702.69**
- **Archetype:** `file_cluster_4` (Distance: 13.064 IQR)
- **Magnitude:** 17.15 | **LOC:** 94 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `poll` (Impact: 11.2), `debug` (Impact: 8.3), `debug` (Impact: 7.8)

### 9. `packages/data-context/src/sources/VersionsDataSource.ts` (TYPESCRIPT) -> Cumulative Risk: **684.85**
- **Archetype:** `file_cluster_4` (Distance: 12.941 IQR)
- **Magnitude:** 32.0 | **LOC:** 245 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9992%)
- **Heaviest Functions:** `getLatestVersion` (Impact: 63.6), `getVersionMetadata` (Impact: 13.3), `versionData` (Impact: 11.1)

### 10. `packages/data-context/src/data/ProjectConfigIpc.ts` (TYPESCRIPT) -> Cumulative Risk: **678.5**
- **Archetype:** `file_cluster_13` (Distance: 13.898 IQR)
- **Magnitude:** 25.58 | **LOC:** 413 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Concurrency (99.9559%)
- **Heaviest Functions:** `forkConfigProcess` (Impact: 15.9), `constructor` (Impact: 9.6), `loadConfig` (Impact: 9.5)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/svelte/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/vue/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `npm/webpack-preprocessor/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/app/src/specs/RunStatusDots.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.285 IQR)
- **Top Global Matches:** file_cluster_8: 9.285, file_cluster_13: 9.451, file_cluster_0: 9.483
- **Magnitude:** 2019.72 | **LOC:** 240 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8876%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 47`, `args: 14`, `func_start: 1`, `class_start: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 3`, `import: 14`
* *Defense:* `safety: 13`, `test: 4`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/cookies.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.072 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.376 IQR)
- **Top Global Matches:** file_cluster_8: 12.072, file_cluster_4: 12.225, file_cluster_15: 12.41
- **Magnitude:** 1981.8 | **LOC:** 2548 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.4024%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 147.7)
  * `describe` (Impact: 138.9)
  * `context` (Impact: 47.3)
  * `context` (Impact: 40.6)
  * `context` (Impact: 32.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 299`, `args: 374`, `func_start: 594`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 212`, `planned_debt: 4`, `duplicate_logic: 252`
* *Architecture:* `io: 95`, `concurrency: 279`, `import: 2`
* *Defense:* `safety: 34`, `test: 985`, `immutability_locks: 114`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` common-tags, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/connectors.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.598 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.465 IQR)
- **Top Global Matches:** file_cluster_8: 11.598, file_cluster_4: 11.688, file_cluster_1: 11.928
- **Magnitude:** 1618.16 | **LOC:** 1999 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.4536%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 144.9)
  * `describe` (Impact: 144.9)
  * `context` (Impact: 68.2)
  * `context` (Impact: 61.9)
  * `describe` (Impact: 24.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 388`, `args: 397`, `func_start: 503`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 161`, `planned_debt: 2`, `duplicate_logic: 256`
* *Architecture:* `io: 21`, `concurrency: 300`, `import: 1`
* *Defense:* `safety: 19`, `test: 716`, `immutability_locks: 98`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/waiting.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.828 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.565 IQR)
- **Top Global Matches:** file_cluster_0: 11.828, file_cluster_8: 11.885, file_cluster_4: 11.95
- **Magnitude:** 1587.12 | **LOC:** 1446 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.4643%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 277.3)
  * `context` (Impact: 277.2)
  * `describe` (Impact: 143.3)
  * `describe` (Impact: 63.6)
  * `describe` (Impact: 42.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 234`, `args: 222`, `func_start: 301`
* *Risk/State:* `state_mutation: 77`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 157`, `orphaned_logic: 1`
* *Architecture:* `io: 43`, `concurrency: 108`, `import: 1`
* *Defense:* `safety: 38`, `test: 376`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/assertions.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.094 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.141 IQR)
- **Top Global Matches:** file_cluster_8: 12.094, file_cluster_15: 12.501, file_cluster_1: 12.588
- **Magnitude:** 1198.58 | **LOC:** 3121 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.2394%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `context` (Impact: 96.6)
  * `context` (Impact: 19.8)
  * `describe` (Impact: 16.6)
  * `describe` (Impact: 14.1)
  * `context` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 181`, `args: 270`, `func_start: 618`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 293`, `dead_code: 1`, `duplicate_logic: 234`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `concurrency: 40`, `import: 1`
* *Defense:* `safety: 33`, `test: 622`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/request.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.908 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.812 IQR)
- **Top Global Matches:** file_cluster_8: 10.908, file_cluster_4: 11.022, file_cluster_1: 11.363
- **Magnitude:** 923.48 | **LOC:** 1510 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.947%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 119.0)
  * `describe` (Impact: 39.2)
  * `describe` (Impact: 19.4)
  * `context` (Impact: 14.5)
  * `context` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 137`, `args: 201`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 87`, `planned_debt: 5`, `duplicate_logic: 126`
* *Architecture:* `io: 166`, `concurrency: 283`, `import: 2`
* *Defense:* `safety: 3`, `test: 353`, `immutability_locks: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` common-tags, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/window.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.249 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.472 IQR)
- **Top Global Matches:** file_cluster_8: 11.249, file_cluster_4: 11.467, file_cluster_1: 11.575
- **Magnitude:** 747.12 | **LOC:** 1141 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.8223%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 81.1)
  * `context` (Impact: 43.4)
  * `context` (Impact: 15.4)
  * `context` (Impact: 13.6)
  * `context` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 173`, `args: 216`, `func_start: 288`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 98`, `duplicate_logic: 134`
* *Architecture:* `io: 6`, `concurrency: 139`, `import: 1`
* *Defense:* `safety: 6`, `test: 400`, `immutability_locks: 43`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/cypress/log.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.335 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.804 IQR)
- **Top Global Matches:** file_cluster_2: 13.335, file_cluster_11: 13.372, file_cluster_4: 13.418
- **Magnitude:** 533.62 | **LOC:** 639 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 50.2)
  * `context` (Impact: 15.4)
  * `context` (Impact: 13.5)
  * `context` (Impact: 12.2)
  * `objectDiff` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 50`, `args: 74`, `func_start: 132`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 228`, `planned_debt: 17`, `duplicate_logic: 57`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `concurrency: 42`, `import: 2`
* *Defense:* `safety: 7`, `test: 150`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` log, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/cypress/location.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.242 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.214 IQR)
- **Top Global Matches:** file_cluster_8: 12.242, file_cluster_15: 12.406, file_cluster_11: 12.696
- **Magnitude:** 528.7 | **LOC:** 518 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.1099%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 76.7)
  * `context` (Impact: 25.7)
  * `context` (Impact: 17.6)
  * `context` (Impact: 11.4)
  * `describe` (Impact: 11.3)
    * *Intent:* // https://github.com/cypress-io/cypress/issues/2101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 44`, `args: 104`, `func_start: 157`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 110`, `duplicate_logic: 100`
* *Architecture:* `io: 93`
* *Defense:* `test: 135`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/files.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.978 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.358 IQR)
- **Top Global Matches:** file_cluster_8: 10.978, file_cluster_4: 11.269, file_cluster_1: 11.372
- **Magnitude:** 473.34 | **LOC:** 833 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.9762%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 70.6)
  * `describe` (Impact: 39.6)
  * `describe` (Impact: 32.4)
  * `describe` (Impact: 8.3)
  * `describe` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 91`, `args: 114`, `func_start: 185`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 55`, `planned_debt: 1`, `duplicate_logic: 67`
* *Architecture:* `io: 31`, `concurrency: 68`, `import: 2`
* *Defense:* `safety: 10`, `test: 250`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` common-tags, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/app/src/specs/flaky-badge/FlakyInformation.vue` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.099 IQR)
- **Top Global Matches:** file_cluster_8: 9.099, file_cluster_13: 9.274, file_cluster_0: 9.338
- **Magnitude:** 395.39 | **LOC:** 106 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.078%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 6`, `func_start: 2`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/misc.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.516 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.711 IQR)
- **Top Global Matches:** file_cluster_4: 11.516, file_cluster_8: 11.521, file_cluster_15: 11.894
- **Magnitude:** 384.14 | **LOC:** 552 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 37.1)
  * `context` (Impact: 30.9)
  * `describe` (Impact: 9.8)
  * `describe` (Impact: 9.0)
  * `context` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 91`, `args: 108`, `func_start: 137`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `planned_debt: 7`, `duplicate_logic: 60`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 87`, `import: 1`
* *Defense:* `safety: 10`, `test: 181`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/traversals_shadow_dom.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.307 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.334 IQR)
- **Top Global Matches:** file_cluster_8: 8.307, file_cluster_7: 9.298, file_cluster_1: 9.312
- **Magnitude:** 381.58 | **LOC:** 836 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6929%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 45.2)
  * `context` (Impact: 23.6)
  * `context` (Impact: 8.9)
  * `context` (Impact: 6.8)
  * `context` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 189`, `args: 153`, `func_start: 278`
* *Risk/State:* `duplicate_logic: 82`
* *Architecture:* `concurrency: 70`
* *Defense:* `test: 279`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/location.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.806 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.62 IQR)
- **Top Global Matches:** file_cluster_8: 10.806, file_cluster_4: 11.089, file_cluster_1: 11.2
- **Magnitude:** 379.96 | **LOC:** 638 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9419%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 40.4)
  * `context` (Impact: 16.2)
  * `context` (Impact: 15.0)
  * `context` (Impact: 12.3)
  * `describe` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 87`, `args: 125`, `func_start: 160`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 47`, `planned_debt: 2`, `duplicate_logic: 65`
* *Architecture:* `io: 9`, `concurrency: 78`, `import: 1`
* *Defense:* `safety: 6`, `test: 240`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/screenshot.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.168 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.394 IQR)
- **Top Global Matches:** file_cluster_8: 12.168, file_cluster_4: 12.234, file_cluster_15: 12.433
- **Magnitude:** 349.98 | **LOC:** 1213 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8256%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 13.3)
  * `describe` (Impact: 11.3)
  * `it` (Impact: 5.9)
  * `it` (Impact: 4.9)
  * `beforeEach` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 60`, `args: 91`, `func_start: 127`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 93`, `planned_debt: 1`, `duplicate_logic: 61`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `concurrency: 53`, `import: 2`
* *Defense:* `safety: 6`, `test: 203`, `immutability_locks: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/navigation.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.951 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.677 IQR)
- **Top Global Matches:** file_cluster_8: 10.951, file_cluster_4: 11.039, file_cluster_11: 11.257
- **Magnitude:** 334.74 | **LOC:** 2808 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.695%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 47.0)
  * `context` (Impact: 26.4)
  * `context` (Impact: 22.3)
  * `describe` (Impact: 8.5)
  * `it` (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 81`, `args: 98`, `func_start: 134`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 60`
* *Architecture:* `io: 31`, `concurrency: 58`, `import: 3`
* *Defense:* `safety: 4`, `test: 203`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` common-tags, js-cookie, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/cypress/cy.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.993 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.283 IQR)
- **Top Global Matches:** file_cluster_8: 9.993, file_cluster_1: 10.518, file_cluster_15: 10.557
- **Magnitude:** 323.48 | **LOC:** 619 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.6576%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 48.1)
  * `context` (Impact: 17.4)
  * `context` (Impact: 12.9)
  * `describe` (Impact: 8.0)
  * `context` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 165`, `args: 148`, `func_start: 142`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 17`, `planned_debt: 4`, `duplicate_logic: 76`
* *Architecture:* `io: 3`, `concurrency: 33`
* *Defense:* `safety: 3`, `test: 219`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/cypress/stack_utils.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.977 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_8: 8.977, file_cluster_7: 9.715, file_cluster_1: 9.849
- **Magnitude:** 321.98 | **LOC:** 597 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.8659%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 76.4)
  * `context` (Impact: 25.0)
  * `context` (Impact: 19.4)
  * `it` (Impact: 16.5)
  * `context` (Impact: 16.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 57`, `args: 50`, `func_start: 93`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 10`, `state_mutation: 4`, `planned_debt: 6`, `duplicate_logic: 49`, `orphaned_logic: 2`
* *Architecture:* `io: 70`, `concurrency: 4`, `import: 2`
* *Defense:* `test: 111`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` source_map_utils, stack_utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/cypress/screenshot.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.714 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.335 IQR)
- **Top Global Matches:** file_cluster_8: 9.714, file_cluster_1: 10.251, file_cluster_15: 10.345
- **Magnitude:** 321.52 | **LOC:** 333 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7261%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 62.8)
  * `context` (Impact: 61.4)
  * `describe` (Impact: 37.2)
  * `it` (Impact: 6.1)
  * `it` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 54`, `args: 53`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 4`, `planned_debt: 2`, `duplicate_logic: 53`, `orphaned_logic: 1`
* *Architecture:* `io: 11`
* *Defense:* `test: 76`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/driver/cypress/e2e/commands/traversals.cy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.783 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 7.123 IQR)
- **Top Global Matches:** file_cluster_8: 10.783, file_cluster_1: 11.115, file_cluster_4: 11.143
- **Magnitude:** 288.24 | **LOC:** 391 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.9319%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 54.0)
  * `context` (Impact: 39.9)
  * `it` (Impact: 19.0)
  * `describe` (Impact: 15.4)
  * `done` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 64`, `args: 68`, `func_start: 81`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `duplicate_logic: 35`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 35`, `import: 1`
* *Defense:* `safety: 4`, `test: 115`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/app/src/runs/RunsError.vue` (HTML) | Magnitude: 16.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, decorators: 10, structural_boundaries: 5, branch: 3
- `packages/driver/cypress/e2e/commands/aliasing.cy.ts` (TYPESCRIPT) | Magnitude: 38.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 391, args: 162, func_start: 128, structural_boundaries: 114
- `packages/frontend-shared/src/components/Input.vue` (HTML) | Magnitude: 22.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, decorators: 24, branch: 18, structural_boundaries: 17
- `packages/driver/src/cross-origin/events/cookies.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, branch: 2, import: 2
- `packages/app/src/specs/SpecRunSummary.vue` (HTML) | Magnitude: 12.46 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, branch: 68, structural_boundaries: 50, safety: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `system-tests/projects/e2e/cypress/e2e/nested-1/nested-2/screenshot_nested_file.cy.js` (JAVASCRIPT) | Magnitude: 1.98 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: test: 4, io: 2, events: 2, listeners: 2
- `system-tests/projects/coffee-react-interop/cypress.config.js` (JAVASCRIPT) | Magnitude: 3.98 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 6, api: 2, args: 1, func_start: 1
- `npm/webpack-preprocessor/cypress.config.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, args: 2, func_start: 2
- `packages/runner/injection/main.js` (JAVASCRIPT) | Magnitude: 27.8 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, events: 2, immutability_locks: 2
- `packages/driver/src/cross-origin/events/test.ts` (TYPESCRIPT) | Magnitude: 0.88 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, events: 6, structural_boundaries: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/config/src/validation.ts` (TYPESCRIPT) | Magnitude: 17.25 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 73, branch: 50, immutability_locks: 31
- `packages/driver/src/cypress/stack_utils.ts` (TYPESCRIPT) | Magnitude: 18.84 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 66, branch: 49, immutability_locks: 43
- `packages/driver/src/dom/selection.ts` (TYPESCRIPT) | Magnitude: 14.86 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 44, branch: 41, immutability_locks: 38
- `packages/driver/src/dom/visibility.ts` (TYPESCRIPT) | Magnitude: 17.03 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 78, branch: 54, immutability_locks: 53
- `packages/driver/src/cypress/runner.ts` (TYPESCRIPT) | Magnitude: 84.99 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 718, structural_boundaries: 224, branch: 176, immutability_locks: 147

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/runner/injection/patches/xmlHttpRequest.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, state_mutation: 3, reflection_metaprogramming: 3
- `scripts/ensure-node.sh` (SHELL) | Magnitude: 2.6 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 18, indent_spaces: 9, reflection_metaprogramming: 8, io: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/data-context/src/actions/DataEmitterActions.ts` (TYPESCRIPT) | Magnitude: 21.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 184, state_mutation: 65, branch: 45, structural_boundaries: 34
- `packages/frontend-shared/src/composables/index.ts` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, func_start: 5, args: 4
- `system-tests/projects/v8-snapshot/require-full-path-var/entry.js` (JAVASCRIPT) | Magnitude: 4.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 5, io: 4, func_start: 2, api: 2
- `packages/launchpad/src/Main.vue` (HTML) | Magnitude: 68.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 173, branch: 41, structural_boundaries: 33, decorators: 26
- `tooling/electron-mksnapshot/src/mksnapshot.ts` (TYPESCRIPT) | Magnitude: 4.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, args: 8, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/types/src/video.ts` (TYPESCRIPT) | Magnitude: 3.5 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 20, branch: 9, func_start: 9
- `packages/data-context/graphql/utils/graphqlTypeUtils.ts` (TYPESCRIPT) | Magnitude: 1.82 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, generics: 9, safety: 5, indent_spaces: 5
- `packages/data-context/graphql/plugins/nexusNodePlugin.ts` (TYPESCRIPT) | Magnitude: 2.84 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 10, branch: 9, args: 6
- `packages/ts/typedefs/cypress-request-promise.d.ts` (TYPESCRIPT) | Magnitude: 3.27 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 41, generics: 17, safety_bypasses: 16
- `packages/app/src/specs/tree/useCollapsibleTree.ts` (TYPESCRIPT) | Magnitude: 12.21 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 48, branch: 36, generics: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `npm/webpack-dev-server/src/helpers/nextHandler.ts` (TYPESCRIPT) | Magnitude: 9.23 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 37, branch: 26, immutability_locks: 18
- `packages/driver/src/dom/elements/find.ts` (TYPESCRIPT) | Magnitude: 16.95 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 97, branch: 51, immutability_locks: 37
- `packages/config/src/browser.ts` (TYPESCRIPT) | Magnitude: 16.1 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 83, immutability_locks: 35, api: 33
- `packages/driver/src/cy/snapshots_css.ts` (TYPESCRIPT) | Magnitude: 6.09 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 51, immutability_locks: 37, args: 20
- `npm/eslint-plugin-dev/lib/scripts/utils.js` (JAVASCRIPT) | Magnitude: 47.3 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 20, immutability_locks: 17, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/app/src/navigation/SidebarNavigationRow.cy.tsx` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, ui_framework: 5, generics: 5
- `system-tests/projects/vite-simple/src/main.jsx` (JAVASCRIPT) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 3, import: 3, indent_spaces: 3
- `npm/react/cypress/component/basic/network/1-users.jsx` (JAVASCRIPT) | Magnitude: 17.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, func_start: 5, args: 4
- `packages/frontend-shared/src/components/NoInternetConnection.cy.tsx` (TYPESCRIPT) | Magnitude: 0.39 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 4, closures: 4
- `packages/driver/cypress/e2e/e2e/origin/commands/connectors.cy.ts` (TYPESCRIPT) | Magnitude: 4.37 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, func_start: 35, args: 34, test: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/unit/verify-mocha-results-spec.js` (JAVASCRIPT) | Magnitude: 41.04 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 14, test: 14, concurrency: 10
- `packages/driver/cypress/e2e/commands/misc.cy.js` (JAVASCRIPT) | Magnitude: 384.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 393, test: 181, func_start: 137, args: 108
- `npm/webpack-preprocessor/scripts/test-webpack-5.ts` (TYPESCRIPT) | Magnitude: 2.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, concurrency: 10, immutability_locks: 8
- `scripts/gulp/utils/makePathMap.ts` (TYPESCRIPT) | Magnitude: 1.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, io: 17, structural_boundaries: 16, concurrency: 7
- `system-tests/project-fixtures/svelte/src/lib/Errors.svelte` (HTML) | Magnitude: 17.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, api: 4, concurrency: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `system-tests/projects/e2e/obstructive_code.html` (HTML) | Magnitude: 3.48 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 54, branch: 38, globals: 21, safety_bypasses: 20
- `system-tests/projects/e2e/static/obstructive_code.js` (JAVASCRIPT) | Magnitude: 3.14 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 40, branch: 35, globals: 20, safety_bypasses: 17
- `scripts/gulp/tasks/gulpTypeHelpers.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.391 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 8, doc: 1, planned_debt: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/app/src/store/run-all-specs-store.ts` (TYPESCRIPT) | Magnitude: 0.65 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, import: 8, immutability_locks: 6
- `packages/app/src/specs/generators/component/VueComponentGeneratorStepOne.vue` (HTML) | Magnitude: 36.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 28, decorators: 21, branch: 20
- `tooling/v8-snapshot/src/setup/v8-snapshot-entry-cy-in-cy.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2
- `packages/app/src/specs/banners/ConnectProjectBanner.cy.tsx` (TYPESCRIPT) | Magnitude: 2.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, args: 11, closures: 10
- `packages/app/src/specs/banners/LoginBanner.cy.tsx` (TYPESCRIPT) | Magnitude: 2.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, args: 11, closures: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `system-tests/projects/experimental-retries/cypress-legacy-retries.config.js` (JAVASCRIPT) | Magnitude: 3.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, args: 1, func_start: 1, api: 1
- `packages/reporter/src/lib/util.ts` (TYPESCRIPT) | Magnitude: 3.42 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 21, branch: 13, immutability_locks: 10
- `system-tests/project-fixtures/angular/src/polyfills.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 7, dead_code: 2, structural_boundaries: 1
- `system-tests/projects/angular-signals/src/polyfills.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 7, dead_code: 2, structural_boundaries: 1
- `packages/driver/src/dom/elements/nativeProps.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 7, state_mutation: 3, dead_code: 2, reflection_metaprogramming: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/app/src/runner/event-manager.ts` -> Churn: **54.01%** | Cog Load: 96.7482% | Debt: 92.944%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/driver/cypress/e2e/commands/cookies.cy.js` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 1981.8
- `packages/driver/cypress/e2e/commands/waiting.cy.js` -> **Adam Alston** (100.0% isolated ownership) | Magnitude: 1587.12
- `packages/driver/cypress/e2e/commands/assertions.cy.js` -> **Ryan Manuel** (100.0% isolated ownership) | Magnitude: 1198.58
- `packages/driver/cypress/e2e/commands/window.cy.js` -> **Bill Glesias** (100.0% isolated ownership) | Magnitude: 747.12
- `packages/driver/cypress/e2e/cypress/log.cy.js` -> **Cacie Prins** (100.0% isolated ownership) | Magnitude: 533.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/driver/src/cypress/cy.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.9997%)
- `packages/driver/src/cypress/error_utils.ts` -> **Severity: 0.012** (Bridge: 0.0003 * Flux: 36.3661%)
- `packages/app/src/store/studio-store.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 85.0%)
- `packages/driver/src/cy/keyboard.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 90.3117%)
- `packages/app/src/runner/event-manager.ts` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.9999%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/driver/src/config/lodash.ts` -> **Severity: 696.367** (Blast Radius: 26.047 * Doc Risk: 26.735%)
- `packages/frontend-shared/src/locales/i18n.ts` -> **Severity: 401.385** (Blast Radius: 4.633 * Doc Risk: 86.636%)
- `packages/driver/src/cypress/assertions/assert.ts` -> **Severity: 269.267** (Blast Radius: 2.874 * Doc Risk: 93.6906%)
- `scripts/debug.js` -> **Severity: 202.419** (Blast Radius: 16.981 * Doc Risk: 11.9203%)
- `packages/reporter/src/instruments/instrument-model.ts` -> **Severity: 159.044** (Blast Radius: 2.01 * Doc Risk: 79.1265%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
