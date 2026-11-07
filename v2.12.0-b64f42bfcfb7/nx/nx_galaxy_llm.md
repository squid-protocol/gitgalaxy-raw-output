# ARCHITECTURAL_BRIEF: nx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nrwl/nx.git` |
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
- **Scope:** 6477 analyzed artifact(s), 786482 LOC.
- **Load-bearing artifact:** `packages/nx/src/generators/tree.ts` -- 133 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `nx-dev/ui-icons/src/index.ts` -- pulls in 142 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/nx/src/ai/set-up-ai-agents/set-up-ai-agents.spec.ts` at magnitude 8545.34 (structural weight, not risk).
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
| Total Artifacts | 10631 |
| Analyzed Artifacts (Scanned) | 6477 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4154 |
| Total LOC | 786482 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8107 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0244 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.2861 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 702 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 4370 | 668532 | 67.5% |
| JSON | 1037 | 61588 | 16.0% |
| MARKDOWN | 225 | 0 | 3.5% |
| PLAINTEXT | 170 | 6 | 2.6% |
| XML | 157 | 727 | 2.4% |
| RUST | 138 | 30721 | 2.1% |
| KOTLIN | 96 | 9381 | 1.5% |
| JAVASCRIPT | 93 | 6811 | 1.4% |
| HTML | 92 | 3422 | 1.4% |
| CSS | 37 | 1252 | 0.6% |
| CSHARP | 25 | 1048 | 0.4% |
| YAML | 24 | 2055 | 0.4% |
| SHELL | 4 | 484 | 0.1% |
| BATCH | 3 | 307 | 0.0% |
| GROOVY | 3 | 78 | 0.0% |
| RUBY | 2 | 31 | 0.0% |
| SWIFT | 1 | 39 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6471 |
| unknown | unknown | 6 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Declarative / Non-Code 22%, Large Core Modules (2) 10%, Many-Argument Workhorses Files 6%, Compute Cores Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6038 | 93.2% |
| Unknown | 6 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 389 | 6.0% |
| Static: Minified & Vendor Opaque Mass | 44 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4154*

**Composition by Extension & Reason:**
- `.avif`: 754x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 132x Excluded (Binary Format Detected), 107x Excluded (Unsupported Extension: '.avif')
- `.mdoc`: 497x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 495x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 377x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webp`: 253x Excluded (Explicitly Denied Extension: '.webp')
- `.snap`: 222x Unsupported Format (.snap)
- `.ts`: 160x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Embedded Array/Matrix Payload: 4689 commas in 1547 LOC)
- `.json`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 6795 LOC), 2x Excluded (Massive Static Asset Blob: 9787 LOC)
- `no_extension`: 122x Unsupported Format (.undeterminable), 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts__tmpl__`: 145x Unsupported Format (.undeterminable)
- `.tsx`: 58x Excluded (Saturation: Line 12 exceeds 500 chars), 34x Excluded (Saturation: Line 15 exceeds 500 chars), 14x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.jpg`: 61x Excluded (Explicitly Denied Extension: '.jpg')
- `.tsx__tmpl__`: 54x Unsupported Format (.undeterminable)
- `.js__tmpl__`: 48x Unsupported Format (.undeterminable)
- `.ts__tpl__`: 38x Unsupported Format (.undeterminable)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.5 | 4.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.8 | 25.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.8 | 9.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 13.7 | 1.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 81.7 | 4.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1263 | 489 | 0 | `packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.spec.ts` |
| cleanup | 233 | 109 | 0 | `.github/workflows/publish.yml` |
| guards | 17859 | 2276 | 7 | `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/.modules.yaml.ts` |
| danger | 6409 | 1457 | 3 | `packages/nx/src/native/tui/components/tasks_list.rs` |
| concurrency | 21703 | 2013 | 8 | `packages/js/src/plugins/typescript/plugin.spec.ts` |
| connectivity | 13557 | 3911 | 5 | `nx-dev/ui-icons/src/index.ts` |
| io | 17272 | 1952 | 4 | `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/large-project.bun.lock.ts` |
| crypto | 16 | 16 | 0 | `packages/angular-rspack-compiler/src/compilation/augments.ts` |
| ipc | 340 | 198 | 0 | `astro-docs/fixlinks` |
| time | 426 | 176 | 0 | `packages/nx/src/native/tests/task_history.spec.ts` |
| serialization | 1869 | 429 | 0 | `packages/eslint-plugin/src/rules/dependency-checks.spec.ts` |
| regex | 1658 | 602 | 0 | `astro-docs/fixlinks` |
| events | 3211 | 778 | 1 | `packages/nx/src/plugins/js/lock-file/__fixtures__/resolutions-and-patches/yarn.lock.ts` |
| tests | 30234 | 1090 | 11 | `packages/angular/src/generators/application/application.spec.ts` |
| docs | 9634 | 1245 | 2 | `packages/nx/src/plugins/js/lock-file/__fixtures__/resolutions-and-patches/yarn.lock.ts` |
| debt | 1882 | 629 | 0 | `graph/migrate/src/lib/migrate.stories.tsx` |
| mutation | 78682 | 3998 | 32 | `packages/nx/src/native/tui/components/tasks_list.rs` |
| dead_code | 556 | 350 | 0 | `packages/dotnet/src/analyzer/analyzer-client.ts` |
| credential | 1452 | 33 | 0 | `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/large-project.bun.lock.ts` |
| threat | 33 | 16 | 0 | `packages/nx/src/plugins/js/lock-file/__fixtures__/resolutions-and-patches/yarn.lock.ts` |
| ml_ai | 683 | 130 | 0 | `packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenHomeDiscovery.kt` |
| ui | 5414 | 388 | 0 | `packages/expo/src/generators/application/files/nx-welcome/not-configured/src/app/App.tsx.template` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/large-project.bun.lock.ts` (Hits: 2494)
- `packages/nx/src/plugins/js/lock-file/__fixtures__/resolutions-and-patches/yarn.lock.ts` (Hits: 787)
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/nextjs-app.bun.lock.ts` (Hits: 619)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tree.ts** (`packages/nx/src/generators/tree.ts`) — 133 inbound connections
2. **project-graph.ts** (`packages/nx/src/config/project-graph.ts`) — 125 inbound connections
3. **package-json.ts** (`packages/nx/src/utils/package-json.ts`) — 123 inbound connections
4. **mock-project-graph.ts** (`packages/nx/src/internal-testing-utils/mock-project-graph.ts`) — 119 inbound connections
5. **nx-json.ts** (`packages/nx/src/config/nx-json.ts`) — 114 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`nx-dev/ui-icons/src/index.ts`) — 142 outbound dependencies
2. **native-bindings.js** (`packages/nx/src/native/native-bindings.js`) — 82 outbound dependencies
3. **app.rs** (`packages/nx/src/native/tui/app.rs`) — 70 outbound dependencies
4. **server.ts** (`packages/nx/src/daemon/server/server.ts`) — 58 outbound dependencies
5. **tasks_list.rs** (`packages/nx/src/native/tui/components/tasks_list.rs`) — 55 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `extractPropertiesFromObjectLiteral` **(Many-Argument Workhorses)** (@ `packages/eslint/src/generators/utils/flat-config/ast-utils.ts`) -> Impact: **485.7** | LOC: 1737
  * *Intent:* /** * Extracts property values from an ObjectLiteralExpression using AST. * Only extracts properties that have simple literal values. * Returns a part...
- `collectFailureDetails` **(Many-Argument Workhorses)** (@ `.github/workflows/nightly/analyze-failures.ts`) -> Impact: **248.7** | LOC: 505
  * *Intent:* /** * Collects detailed failure information for golden projects. * Called by process-result.ts when golden failures exist. * Returns Slack mrkdwn repo...
- `runExecutor` **(Many-Argument Workhorses)** (@ `packages/js/src/executors/release-publish/release-publish.impl.ts`) -> Impact: **222.6** | LOC: 469
- `create` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/enforce-module-boundaries.ts`) -> Impact: **210.9** | LOC: 650
- `render` **(Many-Argument Workhorses)** (@ `packages/nx/src/native/tui/components/terminal_pane.rs`) -> Impact: **210.6** | LOC: 500
- `convertToRspack` **(Many-Argument Workhorses)** (@ `packages/angular/src/generators/convert-to-rspack/convert-to-rspack.ts`) -> Impact: **193.4** | LOC: 404
- `handle_event` **(Many-Argument Workhorses)** (@ `packages/nx/src/native/tui/app.rs`) -> Impact: **185.8** | LOC: 436
- `requireNative` **(Defensive Guards)** (@ `packages/nx/src/native/native-bindings.js`) -> Impact: **171.1** | LOC: 462
- `render_task_table` **(Many-Argument Workhorses)** (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **170.4** | LOC: 392
  * *Intent:* /// Renders the main task table with scrollbar if needed.
- `run` **(Many-Argument Workhorses)** (@ `packages/eslint-plugin/src/rules/enforce-module-boundaries.ts`) -> Impact: **170.3** | LOC: 530

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/nx/src/ai/set-up-ai-agents` | 4 | 8948.54 | 25.67% | 0.0% |
| `packages/nx/src/utils` | 100 | 5872.26 | 20.18% | 2.68% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs` | 4 | 5640.52 | 2.86% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages` | 8 | 5281.96 | 4.83% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package` | 3 | 5140.66 | 2.62% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/optional` | 5 | 5077.54 | 3.3% | 0.0% |
| `e2e/dotnet` | 7 | 5064.6 | 0.0% | 0.0% |
| `packages/nx/src/tasks-runner` | 31 | 5044.8 | 25.54% | 5.34% |
| `packages/react-native/src/generators/application/files/app/android/app` | 2 | 5009.94 | 3.06% | 17.98% |
| `packages/js/src/generators/library` | 4 | 3776.0 | 36.78% | 4.13% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `graph/migrate/src/lib/migrate.stories.tsx` -> **100.0%** Exposure
- `graph/ui-project-details/src/lib/target-configuration-details-group-list/target-configuration-details-group-list.stories.tsx` -> **100.0%** Exposure
- `graph/ui-project-details/src/lib/target-configuration-details-header/target-configuration-details-header.stories.tsx` -> **100.0%** Exposure
- `packages/nx/src/command-line/affected/command-object.ts` -> **99.9983%** Exposure
- `graph/ui-project-details/src/lib/tooltips/atomizer-tooltip.stories.tsx` -> **99.9962%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/workflows/nightly/analyze-failures.ts` -> **100.0%** Exposure
- `astro-docs/src/pages/[...slug].md.ts` -> **100.0%** Exposure
- `astro-docs/src/pages/llms-full.txt.ts` -> **100.0%** Exposure
- `astro-docs/src/pages/llms.txt.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/cnw-generation.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `graph/migrate/src/lib/migrate.stories.tsx` -> **1** Orphaned Functions | **27** Duplicates
- `graph/ui-project-details/src/lib/target-configuration-details-group-list/target-configuration-details-group-list.stories.tsx` -> **0** Orphaned Functions | **12** Duplicates
- `graph/ui-project-details/src/lib/target-configuration-details-header/target-configuration-details-header.stories.tsx` -> **0** Orphaned Functions | **12** Duplicates
- `.github/workflows/e2e-matrix.yml` -> **0** Orphaned Functions | **10** Duplicates
- `packages/nx/src/command-line/affected/command-object.ts` -> **0** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/js/src/plugins/jest/start-local-registry.ts` -> **100.0%** Exposure
- `e2e/utils/global-setup.ts` -> **99.9985%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `216` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11774` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/nx/src/ai/set-up-ai-agents/set-up-ai-agents.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.22)
- **Top Global Matches:** file_cluster_10: 5.22, file_cluster_2: 6.991, file_cluster_13: 7.491
- **Magnitude:** 8545.34 | **LOC:** 1440 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 63.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.2%), Complexity Load (formerly Cognitive Load) (48.9%), Mutation Surface (formerly State Flux) (46.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 193
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 181`, `args: 85`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 38`
* *Architecture:* `io: 49`, `concurrency: 123`, `import: 9`
* *Defense:* `safety: 79`, `test: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` create-tree-with-empty-workspace, tree, json, package-json, clone-ai-config-repo, constants, schema, set-up-ai-agents...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/dotnet/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/optional/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native/src/generators/application/files/app/android/app/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/js/src/generators/library/library.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.373)
- **Top Global Matches:** file_cluster_10: 4.373, file_cluster_13: 6.016, file_cluster_2: 6.242
- **Magnitude:** 2970.91 | **LOC:** 2582 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (59.9%), Guard Balance (formerly Safety Score) (43.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 570
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 375`, `args: 163`, `func_start: 113`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 53`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 14`, `api: 7`, `concurrency: 230`, `import: 11`
* *Defense:* `safety: 33`, `doc: 4`, `test: 317`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` my-ts-lib.js, library, my-ts-lib.js, schema, :, devkit, testing, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/components/tasks_list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.473)
- **Top Global Matches:** file_cluster_12: 8.473, file_cluster_4: 8.868, file_cluster_5: 9.883
- **Magnitude:** 2131.02 | **LOC:** 6606 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **55**; blast radius 0.425; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.0%)
- **Documentation Coverage:** 63.7097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_task_table` **(Many-Argument Workhorses)** (Impact: 170.4)
    * *Intent:* /// Renders the main task table with scrollbar if needed.
  * `draw` **(Many-Argument Workhorses)** (Impact: 142.1)
  * `create_entries_from_display_items` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* /// Creates entries from hierarchical display items for the selection manager. /// Returns typed ent...
  * `render_cloud_message` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /// Renders messages received from Nx Cloud
  * `update_task_status` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /// Updates a task's status and marks the list for deferred sorting.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 442
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 1051`, `args: 239`, `func_start: 153`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 182`, `fragile_debt: 5`
* *Architecture:* `api: 116`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 89`, `doc: 123`, `test: 160`, `sync_locks: 91`, `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.425
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.002413
  * `Imports (Out-Degree: 12):` color_eyre::eyre::Result, crate::native::tasks::types::Task, crate::native::tasks::types::TaskResult, crate::native::tasks::types::TaskTarget, crate::native::tui::action::Action, crate::native::tui::app::Focus, crate::native::tui::components::Component, crate::native::tui::lifecycle::BatchStatus...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `packages/js/src/plugins/typescript/plugin.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.749)
- **Top Global Matches:** file_cluster_9: 7.749, file_cluster_15: 9.144, file_cluster_16: 9.243
- **Magnitude:** 2010.5 | **LOC:** 7016 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 35.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.4%), Mutation Surface (formerly State Flux) (64.6%), Guard Balance (formerly Safety Score) (51.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invokeCreateNodesOnMatchingFiles` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `applyFilesToTempFsAndContext` **(Generic / Templated Code)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 204 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 1329
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 413`, `args: 102`, `func_start: 90`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 501`
* *Architecture:* `io: 61`, `api: 21`, `concurrency: 309`, `import: 7`
* *Defense:* `safety: 23`, `doc: 259`, `test: 213`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` plugin, devkit, internal-testing-utils, node:fs, lock-file, workspace-context, picomatch
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/eslint/src/generators/utils/flat-config/ast-utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.151)
- **Top Global Matches:** file_cluster_6: 7.151, file_cluster_4: 8.461, file_cluster_9: 16.092
- **Magnitude:** 1661.8 | **LOC:** 2017 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 0.32; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Connectivity (formerly Api Exposure) (77.6%), Guard Balance (formerly Safety Score) (53.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.8%)
- **Documentation Coverage:** 67.4419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractPropertiesFromObjectLiteral` **(Many-Argument Workhorses)** (Impact: 485.7)
    * *Intent:* /** * Extracts property values from an ObjectLiteralExpression using AST. * Only extracts properties...
  * `removePlugin` **(Many-Argument Workhorses)** (Impact: 110.1)
  * `addCJSImportToFlatConfig` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `replaceOverride` **(Many-Argument Workhorses)** (Impact: 59.2)
    * *Intent:* /** * Finds an override matching the lookup function and applies the update function to it. * Uses p...
  * `generateFlatOverride` **(Many-Argument Workhorses)** (Impact: 58.0)
    * *Intent:* /** * Generates an AST object or spread element representing a modern flat config entry, * based on ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 282`, `args: 101`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 45`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 25`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001464
  * `Imports (Out-Degree: 1):` $parser, ), path-utils, devkit, [
          ts.factory.createStringLiteral(
            override[, eslint, typescript, undefined
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/angular/src/generators/convert-to-rspack/convert-to-rspack.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.36)
- **Top Global Matches:** file_cluster_10: 4.36, file_cluster_13: 5.01, file_cluster_2: 5.046
- **Magnitude:** 1656.71 | **LOC:** 1381 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.8%), Guard Balance (formerly Safety Score) (48.0%), Mutation Surface (formerly State Flux) (28.9%), Complexity Load (formerly Cognitive Load) (17.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 127`, `args: 50`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`
* *Architecture:* `io: 4`, `api: 10`, `concurrency: 62`, `import: 18`
* *Defense:* `safety: 12`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` convert-to-rspack, module-federation.config, webpack.config, angular-rspack, devkit, config-utils, testing, angular...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/create-nx-workspace/bin/create-nx-workspace.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.706)
- **Top Global Matches:** file_cluster_8: 6.706, file_cluster_6: 12.671, file_cluster_4: 21.131
- **Magnitude:** 1484.36 | **LOC:** 2150 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.114; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (88.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.7%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeArgsMiddleware` **(Many-Argument Workhorses)** (Impact: 93.1)
    * *Intent:* /** * This function is used to normalize the arguments passed to the command. * It would: * - normal...
  * `determineReactOptions` **(Compute Cores)** (Impact: 66.0)
  * `determineAngularOptions` **(Compute Cores)** (Impact: 51.0)
  * `determineStack` **(Compute Cores)** (Impact: 46.2)
  * `determineUnitTestRunner` **(Defensive Guards)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 61 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 441
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 281`, `args: 41`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 138`
* *Architecture:* `io: 45`, `api: 5`, `concurrency: 136`, `import: 22`
* *Defense:* `safety: 48`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 16):` package.json, create-workspace, create-workspace-options, prompts, yargs-options, ai-output, is-ci, error-utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/nest/src/generators/library/library.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.384)
- **Top Global Matches:** file_cluster_10: 4.384, file_cluster_13: 6.219, file_cluster_2: 6.695
- **Magnitude:** 1418.59 | **LOC:** 697 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.8%), Complexity Load (formerly Cognitive Load) (38.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Concurrency (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 112`, `args: 55`, `func_start: 35`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 6`, `concurrency: 71`, `import: 4`
* *Defense:* `safety: 14`, `doc: 4`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` library, :, devkit, testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/nx/src/run.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.288)
- **Top Global Matches:** file_cluster_10: 4.288, file_cluster_13: 6.07, file_cluster_2: 6.509
- **Magnitude:** 1315.78 | **LOC:** 948 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (83.2%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (18.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 124`, `args: 88`, `func_start: 6`
* *Risk/State:* `state_mutation: 167`
* *Architecture:* `io: 10`, `concurrency: 8`, `import: 4`
* *Defense:* `safety: 4`, `test: 151`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $libC, $mylib1, $mylib2, e2e-utils, fs, package-json, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/detox/src/generators/application/application.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.893)
- **Top Global Matches:** file_cluster_10: 3.893, file_cluster_2: 5.559, file_cluster_13: 6.008
- **Magnitude:** 1259.25 | **LOC:** 784 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (45.3%), Mutation Surface (formerly State Flux) (33.0%), Complexity Load (formerly Cognitive Load) (16.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 98`, `args: 44`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 37`, `import: 4`
* *Defense:* `safety: 5`, `doc: 5`, `test: 91`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` application, devkit, testing, fs, mock-project-graph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/command-line/migrate/migrate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.286)
- **Top Global Matches:** file_cluster_4: 6.286, file_cluster_16: 9.13, file_cluster_15: 9.458
- **Magnitude:** 1255.24 | **LOC:** 2280 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **38**; blast radius 0.332; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (78.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.7%), Guard Balance (formerly Safety Score) (50.4%)
- **Documentation Coverage:** 98.8764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runNxOrAngularMigration` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `populatePackageJsonUpdatesAndGetPackagesToCheck` **(Many-Argument Workhorses)** (Impact: 39.9)
  * `runMigrations` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `filterPackageJsonUpdates` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `generateMigrationsJsonAndUpdatePackageJson` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 217
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 325`, `args: 119`, `func_start: 78`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 6`, `state_mutation: 77`, `fragile_debt: 1`
* *Architecture:* `io: 34`, `api: 16`, `concurrency: 112`, `import: 39`
* *Defense:* `safety: 96`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.001602
  * `Imports (Out-Degree: 28):` compat, ngcli-adapter, configuration, misc-interfaces, nx-json, client, format-changed-files-with-prettier-if-available, tree...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/resolutions-and-patches/yarn.lock.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.243)
- **Top Global Matches:** file_cluster_13: 6.243, file_cluster_2: 6.409, file_cluster_17: 7.772
- **Magnitude:** 1126.2 | **LOC:** 54524 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.08; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.8%), Concurrency Surface (formerly Concurrency) (13.0%), Mutation Surface (formerly State Flux) (8.5%), Complexity Load (formerly Cognitive Load) (4.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 595`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 3`, `state_mutation: 28`
* *Architecture:* `io: 787`, `api: 9`, `concurrency: 67`, `import: 19`
* *Defense:* `safety: 27`, `doc: 1258`, `sync_locks: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` :
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/react-native/src/react-native-legacy.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.914)
- **Top Global Matches:** file_cluster_10: 4.914, file_cluster_13: 6.937, file_cluster_2: 7.754
- **Magnitude:** 1051.98 | **LOC:** 324 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.08; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (52.6%), Complexity Load (formerly Cognitive Load) (47.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 113
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 62`, `args: 43`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 53`, `planned_debt: 2`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 33`, `import: 4`
* *Defense:* `safety: 8`, `doc: 1`, `test: 41`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` e2e-utils, async-storage, child_process, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/app.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.976)
- **Top Global Matches:** file_cluster_4: 7.976, file_cluster_15: 8.664, file_cluster_0: 9.244
- **Magnitude:** 1035.68 | **LOC:** 2669 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **70**; blast radius 0.143; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (55.6%), Guard Balance (formerly Safety Score) (49.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.1%), Mutation Surface (formerly State Flux) (42.9%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_event` **(Many-Argument Workhorses)** (Impact: 185.8)
  * `handle_action` **(Many-Argument Workhorses)** (Impact: 115.4)
  * `with_state` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* /// Create a new App with existing shared state (for mode switching) /// /// This constructor is use...
  * `focus_previous` **(Defensive Guards)** (Impact: 30.1)
  * `handle_key_event` **(Defensive Guards)** (Impact: 26.6)
    * *Intent:* /// Forward key events to the currently focused pane, if any.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 415`, `args: 159`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 46`, `concurrency: 2`, `import: 43`
* *Defense:* `safety: 71`, `doc: 56`, `sync_locks: 60`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.143
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.001821
  * `Imports (Out-Degree: 23):` color_eyre::eyre::Result, crate::native::ide::nx_console::messaging::NxConsoleMessageConnection, crate::native::pseudo_terminal::pseudo_terminal::ParserArc, crate::native::pseudo_terminal::pseudo_terminal::WriterArc, crate::native::tasks::types::Task, crate::native::tasks::types::TaskResult, crate::native::tui::graph_utils::get_failed_dependencies, crate::native::tui::lifecycle::BatchInfo...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/nx/src/tasks-runner/task-orchestrator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.334)
- **Top Global Matches:** file_cluster_4: 6.334, file_cluster_16: 11.047, file_cluster_6: 11.154
- **Magnitude:** 1019.54 | **LOC:** 1540 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 52.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **34**; blast radius 0.127; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (91.8%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.3488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTask` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `completeTasks` **(Many-Argument Workhorses)** (Impact: 47.6)
    * *Intent:* /** * Unified task completion handler for a set of tasks. * - Calls endTasks() lifecycle hook (non-s...
  * `postRunSteps` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `runBatch` **(Many-Argument Workhorses)** (Impact: 34.5)
  * `applyFromCacheOrRunBatch` **(Many-Argument Workhorses)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 50 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 302
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 235`, `args: 100`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 59`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 137`, `import: 34`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.000154 | `Ripple Effect (Closeness):` 0.009533
  * `Imports (Out-Degree: 29):` nx-json, project-graph, task-graph, client, run-commands.impl, hash-task, task-hasher, native...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/eslint/src/generators/convert-to-flat-config/generator.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.237)
- **Top Global Matches:** file_cluster_10: 4.237, file_cluster_13: 5.692, file_cluster_2: 5.983
- **Magnitude:** 973.86 | **LOC:** 1216 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.2%), Complexity Load (formerly Cognitive Load) (37.9%), Mutation Surface (formerly State Flux) (33.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 195
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 209`, `args: 69`, `func_start: 35`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 105`, `import: 21`
* *Defense:* `safety: 10`, `doc: 8`, `test: 136`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` eslint.config.cjs, eslint.config.mjs, versions, lint-project, generator, schema, eslintrc, js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/js/src/plugins/typescript/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.597)
- **Top Global Matches:** file_cluster_6: 5.597, file_cluster_4: 9.834, file_cluster_8: 15.284
- **Magnitude:** 942.76 | **LOC:** 1791 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 52.4%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 0.259; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.0%), Guard Balance (formerly Safety Score) (56.4%), Connectivity (formerly Api Exposure) (40.2%)
- **Documentation Coverage:** 86.8421% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getInputs` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `buildTscTargets` **(Many-Argument Workhorses)** (Impact: 67.5)
  * `getOutputs` **(Many-Argument Workhorses)** (Impact: 52.7)
  * `getExternalProjectReferenceTsconfigPatterns` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /** * Collects unique tsconfig paths (relative to their project root) from the * project reference c...
  * `toRelativePaths` **(Many-Argument Workhorses)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 147`, `args: 64`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 126`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 17`, `api: 5`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 55`, `doc: 8`, `sync_locks: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.259
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.000967
  * `Imports (Out-Degree: 4):` util, devkit, get-named-inputs, node:fs, node:path, file-hasher, lock-file, cache-directory...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `e2e/rollup/src/rollup.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.275)
- **Top Global Matches:** file_cluster_10: 4.275, file_cluster_13: 4.744, file_cluster_2: 5.386
- **Magnitude:** 941.09 | **LOC:** 354 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.7%), Mutation Surface (formerly State Flux) (96.5%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (16.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 41`, `args: 16`, `func_start: 5`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `api: 12`, `concurrency: 4`, `import: 12`
* *Defense:* `safety: 8`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.cjs.js, e2e-utils, with-nx, plugin-babel, plugin-commonjs, rollup-plugin-typescript2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react/src/generators/library/library.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.796)
- **Top Global Matches:** file_cluster_10: 4.796, file_cluster_13: 6.079, file_cluster_2: 6.77
- **Magnitude:** 912.46 | **LOC:** 1432 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (42.4%), Mutation Surface (formerly State Flux) (16.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (10.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Concurrency (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 219`, `args: 91`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`
* *Architecture:* `io: 21`, `api: 6`, `concurrency: 129`, `import: 21`
* *Defense:* `safety: 11`, `doc: 16`, `test: 209`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` versions, application, library, schema, :, versions, devkit, testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/angular/src/migrations/update-21-2-0/update-module-resolution.ts` (TYPESCRIPT) | Magnitude: 1.61 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 57, branch: 18, structural_boundaries: 15, core_var_decl: 7
- `packages/nx/src/native/tasks/utils.rs` (RUST) | Magnitude: 26.82 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 8, branch: 7, generics: 6
- `nx-dev/ui-blog/src/lib/filters.tsx` (TYPESCRIPT) | Magnitude: 39.16 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 130, core_var_decl: 34, structural_boundaries: 25, ui_framework: 24
- `packages/angular/src/generators/scam-pipe/schema.d.ts` (TYPESCRIPT) | Magnitude: 0.97 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, branch: 6, api: 4
- `packages/jest/src/generators/init/init.spec.ts` (TYPESCRIPT) | Magnitude: 213.0 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 22, test: 12, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/remix/src/executors/serve/serve.impl.ts` (TYPESCRIPT) | Magnitude: 79.78 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 19, branch: 14, state_mutation: 13
- `packages/next/src/generators/application/application.spec.ts` (TYPESCRIPT) | Magnitude: 327.16 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1241, structural_boundaries: 219, test: 180, core_var_decl: 109
- `nx-dev/ui-common/src/lib/live-stream-notifier.tsx` (TYPESCRIPT) | Magnitude: 13.36 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 99, core_var_decl: 36, ui_framework: 27, design_snake_case: 21
- `packages/next/src/generators/application/lib/add-linting.spec.ts` (TYPESCRIPT) | Magnitude: 64.62 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 14, decorators: 8, import: 7
- `packages/next/babel.ts` (TYPESCRIPT) | Magnitude: 15.48 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 5, branch: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/nx/src/tasks-runner/life-cycles/task-profiling-life-cycle.ts` (TYPESCRIPT) | Magnitude: 50.72 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 12, branch: 9, state_mutation: 8
- `packages/nx/src/nx-cloud/utilities/get-cloud-options.ts` (TYPESCRIPT) | Magnitude: 15.02 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, args: 4, func_start: 4
- `packages/nx/src/tasks-runner/process-metrics-service.ts` (TYPESCRIPT) | Magnitude: 55.2 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 99, safety: 24, structural_boundaries: 23, args: 13
- `packages/nx/src/tasks-runner/task-io-service.ts` (TYPESCRIPT) | Magnitude: 44.02 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 31, api: 14, args: 12
- `e2e/angular/src/projects-setup.ts` (TYPESCRIPT) | Magnitude: 18.78 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 13, core_var_decl: 9, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/angular/src/executors/ng-packagr-lite/ng-packagr-adjustments/ng-package/entry-point/entry-point.ts` (TYPESCRIPT) | Magnitude: 54.86 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 22, api: 9, core_var_decl: 8
- `packages/nx/src/native/tui/tui.rs` (RUST) | Magnitude: 289.24 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 412, structural_boundaries: 93, branch: 71, doc: 63
- `packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/ProcessTaskUtilsTest.kt` (KOTLIN) | Magnitude: 106.7 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 628, core_var_decl: 184, design_camel_case: 140, test: 122
- `packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.spec.ts` (TYPESCRIPT) | Magnitude: 98.92 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 658, branch: 74, safety: 63, structural_boundaries: 59
- `packages/docker/src/utils/interpolate-pattern.ts` (TYPESCRIPT) | Magnitude: 33.88 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 15, branch: 13, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/rspack/src/generators/convert-webpack/convert-webpack.spec.ts` (TYPESCRIPT) | Magnitude: 99.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 462, structural_boundaries: 58, decorators: 29, import: 28
- `examples/angular-rspack/appshell-css/src/main.server.ts` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, indent_spaces: 3, branch: 1
- `examples/angular-rspack/ssg-css/src/main.server.ts` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, indent_spaces: 3, branch: 1
- `examples/angular-rspack/zoneless-ssg-css/src/main.server.ts` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, indent_spaces: 3, branch: 1
- `packages/cypress/src/migrations/update-21-0-0/remove-tsconfig-and-copy-files-options-from-cypress-executor.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 77, branch: 20, structural_boundaries: 13, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `graph/shared/src/lib/use-route-constructor.ts` (TYPESCRIPT) | Magnitude: 23.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 13, branch: 12, core_var_decl: 7
- `packages/remix/src/generators/init/init.ts` (TYPESCRIPT) | Magnitude: 40.06 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 15, branch: 6, decorators: 6
- `packages/nx/src/native/tui/scroll_momentum.rs` (RUST) | Magnitude: 70.5 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 16, structural_boundaries: 14, branch: 11
- `packages/angular/src/migrations/update-21-5-0/utils/karma-config-comparer.ts` (TYPESCRIPT) | Magnitude: 5.1 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 28, branch: 19, core_var_decl: 16
- `packages/detox/src/generators/application/application.ts` (TYPESCRIPT) | Magnitude: 29.24 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 26, import: 13, concurrency: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/dotnet/analyzer/Utilities/PerfLogger.cs` (CSHARP) | Magnitude: 12.6 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, doc: 12, structural_boundaries: 4, encapsulation: 4
- `packages/dotnet/analyzer/Utilities/TargetBuilder.Restore.cs` (CSHARP) | Magnitude: 10.64 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 9, design_pascal_case: 8, state_mutation: 6
- `packages/webpack/src/plugins/nx-typescript-webpack-plugin/nx-tsconfig-paths-webpack-plugin.ts` (TYPESCRIPT) | Magnitude: 39.24 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 17, branch: 11, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `graph/migrate/src/lib/components/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `nx-dev/ui-animations/src/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8
- `packages/angular/src/generators/ng-add/utilities/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/module-federation/src/plugins/utils/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `graph/shared/src/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/angular/src/generators/ngrx/lib/generate-files.ts` (TYPESCRIPT) | Magnitude: 11.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 7, import: 4, state_mutation: 2
- `packages/dotnet/analyzer/Utilities/TargetBuilder.Watch.cs` (CSHARP) | Magnitude: 9.64 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 9, design_pascal_case: 9, state_mutation: 5
- `packages/react/typings/style.d.ts` (TYPESCRIPT) | Magnitude: 0.78 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 2, api: 1, decorators: 1
- `packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock-v9.yaml.ts` (TYPESCRIPT) | Magnitude: 40.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 909, decorators: 365, io: 44, bitwise_ops: 10
- `packages/angular/src/migrations/update-21-5-0/remove-default-karma-configuration-files.ts` (TYPESCRIPT) | Magnitude: 2.01 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, branch: 17, structural_boundaries: 13, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/module-federation/src/utils/share.ts` (TYPESCRIPT) | Magnitude: 260.34 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 303, branch: 62, structural_boundaries: 62, core_var_decl: 33
- `packages/nx/src/executors/run-commands/running-tasks.ts` (TYPESCRIPT) | Magnitude: 446.04 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 568, structural_boundaries: 123, branch: 90, args: 75
- `packages/angular-rspack/src/lib/plugins/i18n-inline-plugin.ts` (TYPESCRIPT) | Magnitude: 126.58 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 34, branch: 33, core_var_decl: 21
- `packages/nx/src/project-graph/utils/project-configuration/project-nodes-manager.ts` (TYPESCRIPT) | Magnitude: 294.6 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 241, branch: 66, state_mutation: 36, structural_boundaries: 27
- `packages/nx/src/command-line/init/implementation/angular/standalone-workspace.ts` (TYPESCRIPT) | Magnitude: 213.6 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 230, branch: 54, structural_boundaries: 27, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/devkit/src/utils/config-utils.ts` (TYPESCRIPT) | Magnitude: 94.94 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 48, concurrency: 27, io: 26
- `packages/next/typings/image.d.ts` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, branch: 2, api: 2
- `packages/nx/src/native/tasks/hashers/hash_tsconfig.rs` (RUST) | Magnitude: 25.48 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 22, args: 11, core_var_decl: 11
- `packages/nx/src/project-graph/affected/locators/workspace-projects.ts` (TYPESCRIPT) | Magnitude: 78.26 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, branch: 21, structural_boundaries: 20, core_var_decl: 10
- `packages/devkit/src/utils/async-iterable/tap-async-iteratable.ts` (TYPESCRIPT) | Magnitude: 5.1 | Delta: **0.215** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, generics: 5, lazy_evaluation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/js/src/executors/verdaccio/verdaccio.impl.ts` (TYPESCRIPT) | Magnitude: 223.24 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 307, branch: 56, structural_boundaries: 34, safety: 33
- `packages/nx/src/command-line/configure-ai-agents/configure-ai-agents.ts` (TYPESCRIPT) | Magnitude: 254.64 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 402, structural_boundaries: 96, branch: 78, core_var_decl: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/CachingResidentMavenInvoker.kt` (KOTLIN) | Magnitude: 12.68 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 17, reflection_metaprogramming: 10, import: 7
- `packages/rspack/src/plugins/utils/loaders/stylesheet-loaders.ts` (TYPESCRIPT) | Magnitude: 46.8 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 19, branch: 11, import: 10
- `nx-dev/ui-markdoc/src/lib/nodes/link.component.tsx` (TYPESCRIPT) | Magnitude: 9.68 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 20, ui_framework: 7, core_var_decl: 5, branch: 4
- `packages/workspace/src/generators/remove/schema.d.ts` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, class_start: 2, api: 2
- `packages/eslint-plugin/src/configs/typescript.ts` (TYPESCRIPT) | Magnitude: 16.7 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, doc: 20, decorators: 18, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/react/src/generators/component/component.ts` (TYPESCRIPT) | Magnitude: 71.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 21, branch: 17, core_var_decl: 13
- `packages/remix/src/generators/library/library.impl.ts` (TYPESCRIPT) | Magnitude: 56.52 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 22, import: 9, branch: 8
- `packages/angular/src/generators/convert-to-with-mf/lib/write-new-webpack-config.ts` (TYPESCRIPT) | Magnitude: 54.12 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 14, core_var_decl: 12, state_mutation: 9
- `packages/playwright/src/generators/init/init.ts` (TYPESCRIPT) | Magnitude: 28.62 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 13, branch: 6, decorators: 5
- `packages/create-nx-workspace/src/utils/package-manager.ts` (TYPESCRIPT) | Magnitude: 155.3 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 195, branch: 48, structural_boundaries: 41, core_var_decl: 26

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/create-nx-workspace/bin/create-nx-workspace.ts` -> Churn: **81.72%** | Cog Load: 88.1422% | Debt: 0.0%
- `packages/create-nx-workspace/src/create-workspace.ts` -> Churn: **68.9%** | Cog Load: 97.1847% | Debt: 0.0%
- `packages/nx/src/tasks-runner/task-orchestrator.ts` -> Churn: **67.19%** | Cog Load: 81.1541% | Debt: 7.866%
- `.github/workflows/ci.yml` -> Churn: **64.12%** | Cog Load: 12.6378% | Debt: 98.288%
- `packages/nx/src/daemon/client/client.ts` -> Churn: **58.91%** | Cog Load: 95.6146% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/angular/src/generators/convert-to-rspack/convert-to-rspack.spec.ts` -> **Leosvel Pérez Espinosa** (100.0% isolated ownership) | Magnitude: 1656.71
- `packages/nest/src/generators/library/library.spec.ts` -> **Colum Ferry** (100.0% isolated ownership) | Magnitude: 1418.59
- `packages/detox/src/generators/application/application.spec.ts` -> **Colum Ferry** (100.0% isolated ownership) | Magnitude: 1259.25
- `e2e/react-native/src/react-native-legacy.test.ts` -> **Colum Ferry** (100.0% isolated ownership) | Magnitude: 1051.98
- `packages/angular/src/generators/setup-mf/setup-mf.spec.ts` -> **Leosvel Pérez Espinosa** (100.0% isolated ownership) | Magnitude: 864.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/nx/src/daemon/client/client.ts` -> **Severity: 0.218** (Bridge: 0.0022 * Flux: 97.336%)
- `packages/nx/src/utils/output.ts` -> **Severity: 0.099** (Bridge: 0.0014 * Flux: 70.1262%)
- `packages/nx/src/generators/tree.ts` -> **Severity: 0.095** (Bridge: 0.0009 * Flux: 99.6271%)
- `packages/nx/src/utils/package-json.ts` -> **Severity: 0.078** (Bridge: 0.0008 * Flux: 100.0%)
- `packages/nx/src/project-graph/project-graph.ts` -> **Severity: 0.073** (Bridge: 0.0011 * Flux: 67.5987%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/nx/src/utils/workspace-root.ts` -> **Severity: 3.964** (Embedded: 0.0784 * Error Risk: 50.5714%)
- `packages/nx/src/utils/fileutils.ts` -> **Severity: 3.733** (Embedded: 0.0772 * Error Risk: 48.3666%)
- `packages/nx/src/config/workspace-json-project-json.ts` -> **Severity: 3.673** (Embedded: 0.0696 * Error Risk: 52.7912%)
- `packages/nx/src/config/nx-json.ts` -> **Severity: 3.536** (Embedded: 0.0768 * Error Risk: 46.0698%)
- `packages/nx/src/generators/tree.ts` -> **Severity: 3.514** (Embedded: 0.0648 * Error Risk: 54.2391%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/nx/src/config/nx-json.ts` -> **Severity: 1472.8** (Blast Radius: 14.728 * Doc Risk: 100.0%)
- `packages/nx/src/utils/workspace-root.ts` -> **Severity: 746.8** (Blast Radius: 14.936 * Doc Risk: 50.0%)
- `packages/nx/src/utils/package-json.ts` -> **Severity: 638.611** (Blast Radius: 9.196 * Doc Risk: 69.4444%)
- `packages/nx/src/config/project-graph.ts` -> **Severity: 616.1** (Blast Radius: 6.161 * Doc Risk: 100.0%)
- `packages/nx/src/utils/fileutils.ts` -> **Severity: 614.94** (Blast Radius: 20.498 * Doc Risk: 30.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1260 literal sites + 54 sites through wrappers = 1314
- **`panics_and_aborts`:** 2079 literal sites + 38 sites through wrappers = 2117

- `log` (function, debug_prints, primitive): 43 call sites in 1 files -- `tools/update-repos/src/update-repo.ts`
- `log` (function, debug_prints, primitive): 9 call sites in 1 files -- `tools/update-repos/src/setup-repos.ts`
- `toRelativePathCached` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateRecorder.kt`
- `getGradleFilesInputs` (function, panics_and_aborts, primitive): 5 call sites in 2 files -- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/TaskUtils.kt`
- `toRelativePathsCached` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateRecorder.kt`
- `buildProjectTags` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/NxProjectAnalyzer.kt`
- `handleTermination` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/js/src/executors/tsc/tsc.batch-impl.ts`
- `toProjectPath` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/utils/PathFormatter.kt`
- `buildProjectMap` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/maven/batch-runner-adapters/maven3/src/main/kotlin/dev/nx/maven/adapter/maven3/NxMaven3.kt`
- `containsEssentialTestAnnotations` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/TestParsingConstants.kt`
- `echo` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/devkit/src/utils/convert-nx-executor.spec.ts`
- `generateExternalEdges` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/NxProjectAnalyzerMojo.kt`
*(+13 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 48817 call pairs -- scoped 24.4%, unique 0.2%, ambiguous 23.0%, external 52.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 36425 | 27.2% | 0.0% | 28.7% | 44.1% |
| rust | 9269 | 16.9% | 0.0% | 6.1% | 76.9% |
| kotlin | 2533 | 13.6% | 4.5% | 5.1% | 76.8% |
| javascript | 272 | 9.9% | 0.0% | 16.9% | 73.2% |
| csharp | 153 | 40.5% | 0.0% | 2.0% | 57.5% |
| html | 83 | 1.2% | 0.0% | 0.0% | 98.8% |
| shell | 56 | 37.5% | 0.0% | 0.0% | 62.5% |
| ruby | 15 | 0.0% | 0.0% | 0.0% | 100.0% |
| swift | 9 | 22.2% | 0.0% | 0.0% | 77.8% |
| groovy | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
