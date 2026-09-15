# ARCHITECTURAL_BRIEF: angular
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/angular/angular.git` |
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
| Total Artifacts | 9855 |
| Analyzed Artifacts (Scanned) | 8871 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 984 |
| Total LOC | 860399 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8549 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1711 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.6323 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 633 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 5421 | 728889 | 61.1% |
| JAVASCRIPT | 880 | 43173 | 9.9% |
| MARKDOWN | 602 | 0 | 6.8% |
| JSON | 458 | 36223 | 5.2% |
| CSS | 448 | 26698 | 5.1% |
| HTML | 447 | 21701 | 5.0% |
| PLAINTEXT | 437 | 1 | 4.9% |
| XML | 88 | 169 | 1.0% |
| PYTHON | 40 | 2313 | 0.5% |
| YAML | 28 | 307 | 0.3% |
| SHELL | 15 | 743 | 0.2% |
| NIX | 7 | 182 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z -0.09; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 34%, Declarative / Non-Code 23%, State Mutators Files 10%, Large Core Modules 8%, Interface Declarations Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7801 | 87.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1038 | 11.7% |
| Static: Minified & Vendor Opaque Mass | 31 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 984*

**Composition by Extension & Reason:**
- `.bazel`: 330x Excluded (Unsupported Extension: '.bazel'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 180x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 28 LOC), 2x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 20x Unsupported Format (.undeterminable)
- `.ts`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 13 exceeds 500 chars)
- `.gif`: 36x Excluded (Explicitly Denied Extension: '.gif')
- `.ico`: 33x Excluded (Explicitly Denied Extension: '.ico')
- `.yaml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Zero-Density Threshold (LOC: 82, Signals: 0), 2x Excluded (Massive Static Asset Blob: 8745 LOC)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Massive Static Asset Blob: 7696 LOC), 1x Excluded (Static Asset Blob without Intent: 1290 LOC)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 78 exceeds 500 chars), 2x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.yml`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 16x Excluded (Explicitly Denied Extension: '.jpg')
- `.scss`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.snap`: 8x Excluded (Unsupported Extension: '.snap')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.9 | 2.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 30.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.9 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 46.4 | 1.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 68.7 | 4.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 35.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4274 | 1039 | 1 | `packages/language-service/test/legacy/template_target_spec.ts` |
| cleanup | 710 | 272 | 0 | `packages/zone.js/test/browser/browser.spec.ts` |
| guards | 24396 | 2872 | 6 | `packages/forms/signals/test/web/form_field.spec.ts` |
| danger | 20857 | 2334 | 5 | `packages/compiler-cli/src/ngtsc/typecheck/test/type_checker__get_symbol_of_template_node_spec.ts` |
| concurrency | 17349 | 1167 | 2 | `packages/service-worker/worker/test/happy_spec.ts` |
| connectivity | 28391 | 5119 | 7 | `packages/compiler-cli/test/ngtsc/ngtsc_spec.ts` |
| io | 8790 | 1101 | 1 | `adev/src/app/routing/navigation-entries/index.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 158 | 62 | 0 | `devtools/projects/ng-devtools/src/lib/shared/signal-graph/devtools-signal-graph.ts` |
| time | 1138 | 291 | 0 | `packages/zone.js/test/zone-spec/fake-async-test.spec.ts` |
| serialization | 374 | 185 | 0 | `packages/compiler-cli/src/ngtsc/sourcemaps/test/source_file_loader_spec.ts` |
| regex | 1385 | 472 | 0 | `packages/core/schematics/test/inject_migration_spec.ts` |
| events | 7885 | 1211 | 1 | `packages/zone.js/test/browser/browser.spec.ts` |
| tests | 63778 | 1222 | 8 | `packages/compiler-cli/test/ngtsc/ngtsc_spec.ts` |
| docs | 18945 | 4214 | 4 | `packages/compiler/src/template/pipeline/ir/src/ops/create.ts` |
| debt | 4664 | 1006 | 1 | `packages/core/test/acceptance/inherit_definition_feature_spec.ts` |
| mutation | 126987 | 4933 | 31 | `packages/platform-server/test/full_app_hydration_spec.ts` |
| dead_code | 2034 | 1203 | 1 | `packages/core/schematics/utils/template_ast_visitor.ts` |
| credential | 69 | 39 | 0 | `packages/platform-server/test/integration_spec.ts` |
| threat | 1246 | 334 | 0 | `packages/compiler/test/render3/view/binding_spec.ts` |
| ml_ai | 778 | 124 | 0 | `integration/cli-hello-world-lazy/src/app/app.component.html` |
| ui | 15024 | 2305 | 2 | `packages/compiler-cli/test/ngtsc/ngtsc_spec.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `adev/src/app/routing/navigation-entries/index.ts` (Hits: 314)
- `packages/router/test/apply_redirects.spec.ts` (Hits: 250)
- `packages/common/test/image_loaders/image_loader_spec.ts` (Hits: 223)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **platform-browser.ts** (`packages/platform-browser/src/platform-browser.ts`) — 342 inbound connections
2. **rxjs.ts** (`packages/zone.js/lib/rxjs/rxjs.ts`) — 250 inbound connections
3. **router.ts** (`packages/router/src/router.ts`) — 193 inbound connections
4. **path.ts** (`packages/compiler-cli/src/ngtsc/util/src/path.ts`) — 126 inbound connections
5. **view.ts** (`packages/core/src/render3/interfaces/view.ts`) — 125 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **emit.ts** (`packages/compiler/src/template/pipeline/src/emit.ts`) — 73 outbound dependencies
2. **standalone_migration_spec.ts** (`packages/core/schematics/test/standalone_migration_spec.ts`) — 71 outbound dependencies
3. **ngtsc_spec.ts** (`packages/compiler-cli/test/ngtsc/ngtsc_spec.ts`) — 67 outbound dependencies
4. **core_private_export.ts** (`packages/core/src/core_private_export.ts`) — 60 outbound dependencies
5. **compiler.ts** (`packages/compiler/src/compiler.ts`) — 59 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getInlayHintsForTemplate` **(Many-Argument Workhorses)** (@ `packages/language-service/src/inlay_hints.ts`) -> Impact: **829.3** | LOC: 1738
  * *Intent:* /** * Get Angular-specific inlay hints for a template. */
- `patchEventTarget` **(Many-Argument Workhorses)** (@ `packages/zone.js/lib/common/events.ts`) -> Impact: **413.4** | LOC: 710
- `assertValueSpan` **(Many-Argument Workhorses)** (@ `packages/compiler/test/render3/r3_ast_spans_spec.ts`) -> Impact: **403.9** | LOC: 638
- `patchEventTargetMethods` **(Many-Argument Workhorses)** (@ `packages/zone.js/lib/common/events.ts`) -> Impact: **265.2** | LOC: 593
- `_scopeLocalKeyframeDeclarations` **(Many-Argument Workhorses)** (@ `packages/compiler/src/shadow_css.ts`) -> Impact: **260.8** | LOC: 775
  * *Intent:* * to { * background-color: green; * } * } * ``` * and as a side effect it adds "box-animation" to the `unscopedKeyframesSet` set * * @param cssRule th...
- `reifyCreateOperations` **(Many-Argument Workhorses)** (@ `packages/compiler/src/template/pipeline/src/phases/reify.ts`) -> Impact: **234.1** | LOC: 525
- `initZone` **(Compute Cores)** (@ `packages/zone.js/lib/zone-impl.ts`) -> Impact: **222.1** | LOC: 841
- `analyze` **(Many-Argument Workhorses)** (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> Impact: **206.7** | LOC: 565
- `extractDirectiveMetadata` **(Many-Argument Workhorses)** (@ `packages/compiler-cli/src/ngtsc/annotations/directive/src/shared.ts`) -> Impact: **195.8** | LOC: 352
  * *Intent:* /** * Helper function to extract metadata from a `Directive` or `Component`. `Directive`s without a * selector are allowed to be used for abstract bas...
- `patchPromise` **(Compute Cores)** (@ `packages/zone.js/lib/common/promise.ts`) -> Impact: **187.1** | LOC: 631

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/language-service/test` | 21 | 47741.22 | 3.8% | 0.0% |
| `packages/core/test/acceptance` | 65 | 11586.56 | 7.78% | 0.0% |
| `packages/compiler-cli/src/ngtsc/typecheck/test` | 14 | 10389.86 | 5.85% | 0.0% |
| `packages/compiler-cli/test/ngtsc` | 33 | 8131.16 | 3.56% | 0.0% |
| `packages/common/http/src` | 19 | 7063.11 | 19.67% | 8.11% |
| `packages/compiler-cli/src/ngtsc/partial_evaluator/test` | 4 | 6283.57 | 4.6% | 0.0% |
| `packages/language-service/src` | 19 | 6179.22 | 18.6% | 6.65% |
| `packages/core/src/render3` | 50 | 5428.14 | 16.26% | 6.97% |
| `__monolith__` | 19 | 5256.15 | 4.8% | 6.04% |
| `packages/forms/test` | 12 | 5216.24 | 19.48% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `devtools/src/app/demo-app/todo/home/todos.service.ts` -> **100.0%** Exposure
- `modules/playground/src/todo/main.ts` -> **100.0%** Exposure
- `packages/compiler/src/template/pipeline/ir/src/expression.ts` -> **100.0%** Exposure
- `packages/core/schematics/utils/template_ast_visitor.ts` -> **100.0%** Exposure
- `packages/core/src/render/api.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.agent/skills/pr_review/scripts/submit_pr_review.sh` -> **100.0%** Exposure
- `scripts/ci/publish-snapshot-build-artifacts.sh` -> **100.0%** Exposure
- `adev/shared-docs/components/breadcrumb/breadcrumb.component.ts` -> **100.0%** Exposure
- `adev/shared-docs/components/cookie-popup/cookie-popup.component.ts` -> **100.0%** Exposure
- `adev/shared-docs/components/copy-source-code-button/copy-source-code-button.component.spec.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/upgrade/static/test/integration/upgrade_component_spec.ts` -> **5** Orphaned Functions | **174** Duplicates
- `packages/core/test/acceptance/inherit_definition_feature_spec.ts` -> **3** Orphaned Functions | **157** Duplicates
- `packages/core/test/acceptance/lifecycle_spec.ts` -> **0** Orphaned Functions | **113** Duplicates
- `packages/zone.js/test/browser/browser.spec.ts` -> **0** Orphaned Functions | **113** Duplicates
- `packages/core/test/render3/providers_spec.ts` -> **1** Orphaned Functions | **85** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `adev/src/app/environment.ts` -> **99.9997%** Exposure
- `packages/core/src/application/application_init.ts` -> **98.9806%** Exposure
- `packages/forms/signals/test/node/api/validators/validation_errors.spec.ts` -> **90.5779%** Exposure
- `packages/core/src/application/application_ref.ts` -> **83.6119%** Exposure
- `packages/core/test/application_init_spec.ts` -> **72.1632%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8666` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/benchpress/src/webdriver/ios_driver_extension.ts` (TYPESCRIPT) -> Cumulative Risk: **722.65**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.06)
- **Magnitude:** 111.66 | **LOC:** 145 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9907%), Safety Score (97.1552%), Documentation (95.0%)
- **Heaviest Functions:** `_convertPerfRecordsToEvents` (Compute Cores, Impact: 33.1), `createEvent` (Many-Argument Workhorses, Impact: 5.5), `timeEnd` (Parameter Forwarders, Impact: 3.8)

### 2. `packages/compiler/src/template/pipeline/ir/src/expression.ts` (TYPESCRIPT) -> Cumulative Risk: **722.5**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.05)
- **Magnitude:** 961.7 | **LOC:** 1448 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 58.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.2657%), Api Exposure (88.4819%)
- **Heaviest Functions:** `transformExpressionsInOp` (Many-Argument Workhorses, Impact: 174.0), `transformExpressionsInExpression` (Many-Argument Workhorses, Impact: 114.7), `transformExpressionsInStatement` (Compute Cores, Impact: 25.2)

### 3. `packages/zone.js/lib/jasmine/jasmine.ts` (TYPESCRIPT) -> Cumulative Risk: **718.21**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.14)
- **Magnitude:** 323.08 | **LOC:** 354 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9971%), Safety Score (97.6238%), Documentation (97.5%)
- **Heaviest Functions:** `patchJasmine` (Compute Cores, Impact: 97.5), `ZoneQueueRunner` (Many-Argument Workhorses, Impact: 27.2), `runInTestZone` (Many-Argument Workhorses, Impact: 19.0)

### 4. `packages/benchpress/src/webdriver/chrome_driver_extension.ts` (TYPESCRIPT) -> Cumulative Risk: **692.22**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.71)
- **Magnitude:** 236.32 | **LOC:** 289 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7705%), Concurrency (99.6539%)
- **Heaviest Functions:** `_convertEvent` (Compute Cores, Impact: 67.5), `normalizeEvent` (Compute Cores, Impact: 24.4), `normalizeGCEvent` (Compute Cores, Impact: 11.6)

### 5. `vscode-ng-language-service/client/src/client.ts` (TYPESCRIPT) -> Cumulative Risk: **691.71**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.36)
- **Magnitude:** 575.36 | **LOC:** 812 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 35.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9949%), State Flux (99.8738%), Verification (80.0%)
- **Heaviest Functions:** `constructor` (Compute Cores, Impact: 56.4), `provideCompletionItem` (Many-Argument Workhorses, Impact: 24.0), `constructArgs` (I/O & Config Routines, Impact: 22.1)

### 6. `packages/common/src/pipes/async_pipe.ts` (TYPESCRIPT) -> Cumulative Risk: **687.24**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.78)
- **Magnitude:** 103.98 | **LOC:** 244 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `createSubscription` (Many-Argument Workhorses, Impact: 8.0), `_updateLatestValue` (Defensive Guards, Impact: 7.3), `transform` (Defensive Guards, Impact: 6.8)

### 7. `adev/src/app/features/home/components/hydration-example/hydration-example.ts` (TYPESCRIPT) -> Cumulative Risk: **685.02**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.76)
- **Magnitude:** 161.06 | **LOC:** 243 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `handleCardClick` (Compute Cores, Impact: 12.7), `getCardSignal` (Compute Cores, Impact: 10.6), `startLifecycle` (I/O & Config Routines, Impact: 10.1)

### 8. `packages/zone.js/lib/zone-spec/wtf.ts` (TYPESCRIPT) -> Cumulative Risk: **684.8**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.88)
- **Magnitude:** 176.96 | **LOC:** 198 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5752%), Tech Debt (99.177%)
- **Heaviest Functions:** `patchWtf` (Compute Cores, Impact: 50.0), `shallowObj` (Compute Cores, Impact: 21.8), `onInvoke` (Many-Argument Workhorses, Impact: 15.2)

### 9. `devtools/projects/ng-devtools-backend/src/lib/hooks/profiler/native.ts` (TYPESCRIPT) -> Cumulative Risk: **676.9**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -1.71)
- **Magnitude:** 123.38 | **LOC:** 253 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9893%), Safety Score (99.4592%)
- **Heaviest Functions:** `ProfilerEvent.TemplateUpdateStart]` (Compute Cores, Impact: 12.0), `ProfilerEvent.TemplateUpdateEnd]` (Compute Cores, Impact: 7.7), `constructor` (Generic / Templated Code, Impact: 3.4)

### 10. `packages/compiler-cli/src/perform_watch.ts` (TYPESCRIPT) -> Cumulative Risk: **673.1**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.57)
- **Magnitude:** 305.12 | **LOC:** 337 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9707%), Documentation (88.3721%), Safety Score (87.9254%)
- **Heaviest Functions:** `performWatchCompilation` (Compute Cores, Impact: 51.3), `createPerformWatchHost` (Many-Argument Workhorses, Impact: 36.3), `doCompilation` (I/O & Config Routines, Impact: 20.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/language-service/test/inlay_hints_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 41124.67 | **LOC:** 3728 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.1169%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 896`, `args: 419`, `func_start: 92`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 193`, `dead_code: 2`
* *Architecture:* `api: 154`, `concurrency: 3`, `import: 147`
* *Defense:* `safety: 40`, `doc: 1`, `test: 350`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` testing, signal-input.directive, user-display.directive, animations, common, testing, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/typecheck/test/diagnostics_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 9777.02 | **LOC:** 1544 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.825%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 356`, `args: 112`, `func_start: 32`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 6`
* *Architecture:* `api: 21`, `import: 6`
* *Defense:* `safety: 56`, `doc: 1`, `test: 156`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` testing, diagnostics, testing, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/partial_evaluator/test/evaluator_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 6238.79 | **LOC:** 947 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.0376%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 277`, `args: 105`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 5`
* *Architecture:* `api: 31`, `import: 37`
* *Defense:* `safety: 6`, `doc: 1`, `test: 245`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` file_system, testing, imports, api, testing, dynamic, result, const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/common/http/src/client.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 4894.2 | **LOC:** 5025 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.5271%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 116.2)
    * *Intent:* * * The `responseType` value determines how a successful response body is parsed. * * If `responseTy...
  * `request` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* /** * Constructs a request which interprets the body as a JavaScript object and returns the full * `...
  * `request` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* /** * Constructs a request which interprets the body as a JavaScript object * with the response body...
  * `request` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* /** * Constructs a request where response type and requested observable are not known statically. * ...
  * `post` **(Compute Cores)** (Impact: 43.3)
    * *Intent:* /** * Constructs a `POST` request that interprets the body as JSON * and returns the response body a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 142
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2270`, `structural_boundaries: 37`, `args: 141`, `func_start: 135`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 6`
* *Architecture:* `api: 2`, `concurrency: 137`, `import: 10`
* *Defense:* `safety: 3`, `doc: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` backend, context, errors, headers, params, request, response, core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/app/features/update/recommendations.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4150.88 | **LOC:** 2916 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (7.4589%), Tech Debt (9.3914%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 162`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 84`, `api: 5`, `concurrency: 16`, `import: 15`
* *Defense:* `safety: 72`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000225
  * `Imports (Out-Degree: 1):` core, platform-browser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/linker/babel/test/ast/babel_ast_factory_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3084.17 | **LOC:** 567 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (8.3215%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 152`, `args: 100`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`
* *Architecture:* `io: 1`, `import: 6`
* *Defense:* `safety: 7`, `doc: 1`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $url, babel_ast_factory, , compiler, core, generator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/language-service/test/signal_queries_refactoring_action_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2834.82 | **LOC:** 526 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (6.3242%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 98`, `args: 33`, `func_start: 17`, `class_start: 14`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 14`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 36`, `doc: 1`, `test: 97`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` testing, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/nullish_coalescing_not_nullable/nullish_coalescing_not_nullable_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2295.73 | **LOC:** 355 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9642%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 65`, `args: 21`, `func_start: 3`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 12`, `import: 9`
* *Defense:* `safety: 23`, `doc: 1`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api, diagnostics, file_system, testing, testing, testing, nullish_coalescing_not_nullable, extended_template_checker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/service-worker/config/test/generator_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2226.87 | **LOC:** 591 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.6053%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 29`, `args: 17`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `io: 32`, `concurrency: 21`, `import: 3`
* *Defense:* `safety: 22`, `doc: 7`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` generator, in, mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/language-service/test/signal_input_refactoring_action_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2028.36 | **LOC:** 467 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (6.8955%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 93`, `args: 30`, `func_start: 15`, `class_start: 13`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 13`, `concurrency: 16`, `import: 14`
* *Defense:* `safety: 31`, `doc: 1`, `test: 86`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` testing, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/language-service/src/inlay_hints.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1816.1 | **LOC:** 2054 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (32.073%), Tech Debt (8.1808%)
**Top Internal Functions/Classes:**
  * `getInlayHintsForTemplate` **(Many-Argument Workhorses)** (Impact: 829.3)
    * *Intent:* /** * Get Angular-specific inlay hints for a template. */
  * `isHostBindingInSpan` **(Compute Cores)** (Impact: 109.9)
    * *Intent:* // For host bindings, check if the position is within the requested span. // Host binding keySpan po...
  * `processCallArguments` **(Many-Argument Workhorses)** (Impact: 73.5)
  * `isRequiredInput` **(Compute Cores)** (Impact: 52.6)
    * *Intent:* /** * Check if an input is required (input.required() or @Input with required: true). * * For signal...
  * `visitPipe` **(Many-Argument Workhorses)** (Impact: 48.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 220`, `args: 50`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 61`, `planned_debt: 2`
* *Architecture:* `api: 19`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 22`, `doc: 29`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` api, utils, compiler, core, api, checker, symbols, comments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/test/compliance/test_helpers/expect_emit.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1705.98 | **LOC:** 229 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8059%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 8`, `args: 6`, `func_start: 5`
* *Risk/State:* `state_mutation: 27`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000307
  * `Imports (Out-Degree: 0):` compiler
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/forms/test/template_integration_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1602.06 | **LOC:** 3127 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (49.7138%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `verifyFormState` **(Tests & Verification)** (Impact: 6.4)
  * `getValues` **(Tests & Verification)** (Impact: 5.3)
  * `verifyFormState` **(Tests & Verification)** (Impact: 5.1)
  * `onNgModelChange` **(Annotated Framework Methods)** (Impact: 4.8)
  * `add` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 177 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 1133
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 369`, `args: 151`, `func_start: 113`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 291`, `duplicate_logic: 8`, `unreferenced_by_name: 3`
* *Architecture:* `api: 2`, `concurrency: 248`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `test: 502`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index, value_accessor_integration_spec, common, core, testing, platform-browser, testing, rxjs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1543.24 | **LOC:** 2643 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (37.9678%), Tech Debt (7.8338%)
**Top Internal Functions/Classes:**
  * `analyze` **(Many-Argument Workhorses)** (Impact: 206.7)
  * `resolveComponentDependencies` **(Many-Argument Workhorses)** (Impact: 116.9)
    * *Intent:* /** * Determines the dependencies of a component and * categorizes them based on how they were intro...
  * `handleDependencyCycles` **(Many-Argument Workhorses)** (Impact: 101.8)
    * *Intent:* /** Handles any cycles in the dependencies of a component. */
  * `resolveDeferBlocks` **(Many-Argument Workhorses)** (Impact: 58.9)
    * *Intent:* /** * Resolves information about defer blocks dependencies to make it * available for the final `com...
  * `resolve` **(Many-Argument Workhorses)** (Impact: 58.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 183`, `args: 57`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 146`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 16`, `concurrency: 9`, `import: 37`
* *Defense:* `safety: 43`, `doc: 18`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` cycles, diagnostics, file_system, hmr, imports, api, semantic_graph, indexer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/annotations/directive/src/shared.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1506.52 | **LOC:** 2234 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.4398%), Tech Debt (7.8772%)
**Top Internal Functions/Classes:**
  * `extractDirectiveMetadata` **(Many-Argument Workhorses)** (Impact: 195.8)
    * *Intent:* /** * Helper function to extract metadata from a `Directive` or `Component`. `Directive`s without a ...
  * `extractHostBindings` **(Many-Argument Workhorses)** (Impact: 117.7)
  * `parseOutputFields` **(Many-Argument Workhorses)** (Impact: 97.2)
    * *Intent:* /** Parses the class members that are outputs. */
  * `tryParseInputFieldMapping` **(Many-Argument Workhorses)** (Impact: 90.9)
  * `extractDecoratorQueryMetadata` **(Many-Argument Workhorses)** (Impact: 69.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 176`, `args: 65`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 77`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 11`, `import: 19`
* *Defense:* `safety: 51`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` +, diagnostics, imports, metadata, partial_evaluator, reflection, transform, host_bindings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/platform-server/test/full_app_hydration_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1499.02 | **LOC:** 7855 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (27.1688%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadComponent` **(Tests & Verification)** (Impact: 4.5)
  * `ngAfterViewInit` **(I/O & Config Routines)** (Impact: 4.0)
  * `loadComponent` **(Tests & Verification)** (Impact: 3.5)
  * `ngAfterViewInit` **(Defensive Guards)** (Impact: 3.4)
  * `ngAfterViewInit` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 72 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 937
* *State Mutation (weighted view):* 339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 1036`, `args: 326`, `func_start: 233`, `class_start: 312`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 4`, `state_mutation: 253`, `duplicate_logic: 17`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `concurrency: 577`, `import: 10`
* *Defense:* `safety: 244`, `doc: 1`, `test: 661`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` dom_utils, hydration_utils, common, testing, compiler, core, testing, localize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/test/ngtsc/doc_extraction/class_doc_extraction_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1374.24 | **LOC:** 768 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.6619%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 159`, `args: 72`, `func_start: 49`, `class_start: 34`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 33`, `import: 5`
* *Defense:* `doc: 3`, `test: 221`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` docs, entities, testing, testing, env
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/primitives/dom-navigation/testing/test/fake_platform_navigation.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1317.4 | **LOC:** 2176 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `popStateListener` **(Callbacks & Closures)** (Impact: 6.6)
  * `precommitHandler` **(Callbacks & Closures)** (Impact: 4.9)
  * `setUpEntries` **(Callbacks & Closures)** (Impact: 3.9)
  * `setUpEntriesWithHistory` **(Callbacks & Closures)** (Impact: 3.6)
  * `precommitHandler` **(Tests & Verification)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 123 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 993
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 475`, `args: 208`, `func_start: 138`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 135`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 46`, `concurrency: 378`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`, `test: 619`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fake_navigation, testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zone.js/lib/common/events.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1285.9 | **LOC:** 955 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.2172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `patchEventTarget` **(Many-Argument Workhorses)** (Impact: 413.4)
  * `patchEventTargetMethods` **(Many-Argument Workhorses)** (Impact: 265.2)
  * `makeAddListener` **(Many-Argument Workhorses)** (Impact: 131.6)
  * `globalCallback` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `findEventTasks` **(Compute Cores)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 76`, `args: 32`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 80`, `dead_code: 11`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 5`, `doc: 19`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.151
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00093
  * `Imports (Out-Degree: 0):` utils
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/interpolated_signal_not_invoked/interpolated_signal_not_invoked_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1267.64 | **LOC:** 1049 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.1312%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 150`, `args: 40`, `func_start: 1`, `class_start: 33`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `api: 33`, `import: 39`
* *Defense:* `safety: 26`, `doc: 1`, `test: 120`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` diagnostics, file_system, testing, testing, testing, interpolated_signal_not_invoked, extended_template_checker, core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/output/output_ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1261.3 | **LOC:** 2091 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (15.3262%), Tech Debt (59.9298%)
**Top Internal Functions/Classes:**
  * `escapeForTemplateLiteral` **(Compute Cores)** (Impact: 183.8)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 605`, `args: 359`, `func_start: 338`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 228`, `state_mutation: 23`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 13`
* *Architecture:* `api: 205`, `import: 4`
* *Defense:* `safety: 11`, `doc: 12`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.771
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.009131
  * `Imports (Out-Degree: 4):` digest, i18n_ast, parse_util, meta
  * `Imported By (In-Degree: 85):` (Excluded from Brief to save tokens)

### `packages/animations/browser/src/render/transition_animation_engine.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1204.8 | **LOC:** 1944 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.5914%), Tech Debt (8.4393%)
**Top Internal Functions/Classes:**
  * `_flushAnimations` **(Many-Argument Workhorses)** (Impact: 123.7)
  * `trigger` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `_getPreviousPlayers` **(Many-Argument Workhorses)** (Impact: 45.7)
  * `removeNode` **(Compute Cores)** (Impact: 27.0)
  * `_buildAnimation` **(Many-Argument Workhorses)** (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 245`, `args: 198`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 142`, `state_mutation: 160`, `dead_code: 8`, `fragile_debt: 1`
* *Architecture:* `api: 42`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 9`, `doc: 3`, `immutability_locks: 3`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.097
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000451
  * `Imports (Out-Degree: 8):` animations, animation_timeline_instruction, animation_transition_factory, animation_transition_instruction, animation_trigger, element_instruction_map, animation_style_normalizer, error_helpers...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/compiler/src/template/pipeline/src/ingest.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1198.12 | **LOC:** 1939 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (31.7125%), Tech Debt (12.9484%)
**Top Internal Functions/Classes:**
  * `convertAst` **(Many-Argument Workhorses)** (Impact: 140.4)
    * *Intent:* /** * Convert a template AST expression into an output AST expression. */
  * `ingestDeferBlock` **(Defensive Guards)** (Impact: 71.6)
  * `createTemplateBinding` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* * @param value The bindings's value, which will either be an input AST expression, or a string * lit...
  * `ingestTemplateBindings` **(Many-Argument Workhorses)** (Impact: 47.7)
    * *Intent:* /** * Process all of the bindings on a template in the template AST and convert them to their IR * r...
  * `ingestNodes` **(Compute Cores)** (Impact: 46.6)
    * *Intent:* /** * Ingest the nodes of a template AST into the given `ViewCompilation`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 179`, `args: 67`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 110`, `planned_debt: 18`
* *Architecture:* `api: 8`, `import: 15`
* *Defense:* `safety: 64`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000593
  * `Imports (Out-Degree: 11):` constant_pool, core, ast, i18n_ast, tags, output_ast, parse_util, r3_ast...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/test/ngtsc/standalone_spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1179.39 | **LOC:** 1196 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (2.4758%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 348`, `args: 62`, `func_start: 6`, `class_start: 87`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 3`
* *Architecture:* `api: 87`, `import: 67`
* *Defense:* `safety: 12`, `doc: 1`, `test: 134`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` diagnostics, testing, testing, component, dep, env, lib, module...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/language-service/test/inlay_hints_spec.ts` -> **kbrilla** (100.0% isolated ownership) | Magnitude: 41124.67
- `packages/compiler-cli/src/ngtsc/partial_evaluator/test/evaluator_spec.ts` -> **JoostK** (100.0% isolated ownership) | Magnitude: 6238.79
- `packages/common/http/src/client.ts` -> **SkyZeroZx** (100.0% isolated ownership) | Magnitude: 4894.2
- `packages/compiler-cli/test/ngtsc/doc_extraction/class_doc_extraction_spec.ts` -> **Angular Robot** (100.0% isolated ownership) | Magnitude: 1374.24
- `packages/compiler-cli/test/ngtsc/standalone_spec.ts` -> **Kristiyan Kostadinov** (100.0% isolated ownership) | Magnitude: 1179.39

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/core/src/render3/component_ref.ts` -> **Severity: 0.047** (Bridge: 0.0005 * Flux: 96.7204%)
- `packages/core/src/di/provider_collection.ts` -> **Severity: 0.035** (Bridge: 0.0003 * Flux: 99.0611%)
- `packages/core/src/render3/ng_module_ref.ts` -> **Severity: 0.03** (Bridge: 0.0005 * Flux: 66.3052%)
- `packages/core/src/hydration/utils.ts` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 98.4778%)
- `packages/core/src/hydration/annotate.ts` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 99.9323%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/zone.js/lib/zone-impl.ts` -> **Severity: 2.813** (Embedded: 0.0284 * Error Risk: 98.977%)
- `packages/zone.js/lib/rxjs/rxjs.ts` -> **Severity: 2.615** (Embedded: 0.0263 * Error Risk: 99.3267%)
- `packages/router/src/router.ts` -> **Severity: 1.673** (Embedded: 0.0217 * Error Risk: 77.2452%)
- `packages/platform-browser/src/dom/dom_renderer.ts` -> **Severity: 1.665** (Embedded: 0.0181 * Error Risk: 91.9179%)
- `packages/core/src/util/array_utils.ts` -> **Severity: 1.492** (Embedded: 0.015 * Error Risk: 99.4431%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/zone.js/lib/zone-impl.ts` -> **Severity: 1542.568** (Blast Radius: 18.217 * Doc Risk: 84.6774%)
- `packages/zone.js/lib/rxjs/rxjs.ts` -> **Severity: 1277.2** (Blast Radius: 12.772 * Doc Risk: 100.0%)
- `packages/compiler/src/chars.ts` -> **Severity: 522.6** (Blast Radius: 5.226 * Doc Risk: 100.0%)
- `packages/compiler/src/parse_util.ts` -> **Severity: 446.129** (Blast Radius: 5.511 * Doc Risk: 80.9524%)
- `packages/platform-browser/src/dom/events/dom_events.ts` -> **Severity: 402.5** (Blast Radius: 4.025 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
