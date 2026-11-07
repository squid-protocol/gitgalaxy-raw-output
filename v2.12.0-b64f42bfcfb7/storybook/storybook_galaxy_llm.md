# ARCHITECTURAL_BRIEF: storybook
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/storybookjs/storybook.git` |
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
- **Scope:** 3613 analyzed artifact(s), 329464 LOC.
- **Load-bearing artifact:** `code/core/src/types/index.ts` -- 300 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `code/core/src/components/index.ts` -- pulls in 76 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts` at magnitude 7021.58 (structural weight, not risk).
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
| Total Artifacts | 5516 |
| Analyzed Artifacts (Scanned) | 3613 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1903 |
| Total LOC | 329464 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 65.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7669 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0827 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.508 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 503 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2618 | 271237 | 72.5% |
| JAVASCRIPT | 301 | 45696 | 8.3% |
| JSON | 226 | 4827 | 6.3% |
| HTML | 149 | 4635 | 4.1% |
| MARKDOWN | 136 | 0 | 3.8% |
| PLAINTEXT | 78 | 1 | 2.2% |
| CSS | 49 | 1396 | 1.4% |
| YAML | 34 | 1610 | 0.9% |
| XML | 18 | 13 | 0.5% |
| SHELL | 4 | 49 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3612 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Declarative / Non-Code 20%, Callbacks & Closures Files 16%, Large Core Modules (2) 8%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3385 | 93.7% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 213 | 5.9% |
| Static: Minified & Vendor Opaque Mass | 14 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1903*

**Composition by Extension & Reason:**
- `.md`: 714x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5720 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3544 LOC)
- `.ts`: 222x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.png`: 213x Excluded (Explicitly Denied Extension: '.png')
- `.mdx`: 190x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.tsx`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 18 exceeds 500 chars)
- `.snapshot`: 104x Excluded (Unsupported Extension: '.snapshot'), 14x Unsupported Format (.snapshot), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.pug`: 37x Excluded (Unsupported Extension: '.pug'), 7x Unsupported Format (.pug)
- `.json`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mp4`: 37x Excluded (Explicitly Denied Extension: '.mp4')
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1242 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1159 LOC)
- `.lock`: 11x Excluded (Unsupported Extension: '.lock'), 2x Unsupported Format (.lock)
- `.snap`: 8x Unsupported Format (.snap), 4x Excluded (Unsupported Extension: '.snap'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 12x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.1 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.0 | 24.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 22.8 | 19.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 23.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.7 | 0.4 | 0.1 | 0.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 80.3 | 11.1 | 14.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.8 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2224 | 679 | 1 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| cleanup | 192 | 79 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| guards | 10471 | 1213 | 5 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| danger | 5317 | 1048 | 3 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| concurrency | 13484 | 1030 | 9 | `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` |
| connectivity | 11283 | 2593 | 7 | `code/core/src/csf-tools/ConfigFile.test.ts` |
| io | 5874 | 708 | 3 | `code/core/src/manager/components/sidebar/mockdata.large.ts` |
| crypto | 6 | 5 | 0 | `code/core/src/telemetry/one-way-hash.ts` |
| ipc | 14 | 12 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| time | 391 | 177 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| serialization | 420 | 218 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| regex | 903 | 294 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| events | 2803 | 594 | 2 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| tests | 15076 | 647 | 7 | `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` |
| docs | 3822 | 715 | 2 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| debt | 1477 | 382 | 1 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| mutation | 59061 | 2592 | 30 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| dead_code | 679 | 355 | 0 | `test-storybooks/ember-cli/ember-output/assets/vendor.js` |
| credential | 10 | 7 | 0 | `code/core/src/telemetry/storybook-metadata.test.ts` |
| threat | 21 | 12 | 0 | `code/core/src/manager-api/tests/shortcut.test.js` |
| ml_ai | 267 | 80 | 0 | `code/core/src/components/components/Select/Select.tsx` |
| ui | 5532 | 690 | 3 | `code/core/src/components/components/Modal/Modal.stories.tsx` |

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

1. **index.ts** (`code/core/src/types/index.ts`) — 300 inbound connections
2. **index.ts** (`code/core/src/theming/index.ts`) — 197 inbound connections
3. **index.ts** (`code/core/src/manager-api/index.ts`) — 107 inbound connections
4. **index.ts** (`code/core/src/test/index.ts`) — 100 inbound connections
5. **index.ts** (`code/core/src/components/index.ts`) — 92 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`code/core/src/components/index.ts`) — 76 outbound dependencies
2. **index.ts** (`code/core/src/common/index.ts`) — 47 outbound dependencies
3. **getComponentImports.test.ts** (`code/renderers/react/src/componentManifest/getComponentImports.test.ts`) — 32 outbound dependencies
4. **task.ts** (`scripts/task.ts`) — 32 outbound dependencies
5. **sandbox-parts.ts** (`scripts/tasks/sandbox-parts.ts`) — 30 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EmberRouter` **(Compute Cores)** (@ `test-storybooks/ember-cli/ember-output/assets/vendor.js`) -> Impact: **286.7** | LOC: 869
  * *Intent:* */
- `parse` **(I/O & Config Routines)** (@ `code/core/src/csf-tools/CsfFile.ts`) -> Impact: **187.3** | LOC: 546
- `storyToCsfFactory` **(Many-Argument Workhorses)** (@ `code/lib/cli-storybook/src/codemod/helpers/story-to-csf-factory.ts`) -> Impact: **177.1** | LOC: 494
- `Route` **(Many-Argument Workhorses)** (@ `test-storybooks/ember-cli/ember-output/assets/vendor.js`) -> Impact: **171.2** | LOC: 1387
  * *Intent:* */
- `getCodeSnippet` **(Many-Argument Workhorses)** (@ `code/renderers/react/src/componentManifest/generateCodeSnippet.ts`) -> Impact: **159.6** | LOC: 272
- `Router` **(I/O & Config Routines)** (@ `test-storybooks/ember-cli/ember-output/assets/vendor.js`) -> Impact: **156.8** | LOC: 717
- `RehydrateBuilder` **(Defensive Guards)** (@ `test-storybooks/ember-cli/ember-output/assets/vendor.js`) -> Impact: **148.2** | LOC: 362
- `esmWalker` **(Defensive Guards)** (@ `code/core/src/mocking-utils/esmWalker.ts`) -> Impact: **145.8** | LOC: 180
- `configToCsfFactory` **(Many-Argument Workhorses)** (@ `code/lib/cli-storybook/src/codemod/helpers/config-to-csf-factory.ts`) -> Impact: **140.9** | LOC: 259
- `generateDocgen` **(Many-Argument Workhorses)** (@ `code/frameworks/svelte-vite/src/plugins/generateDocgen.ts`) -> Impact: **131.2** | LOC: 268

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `code/renderers/react/src/componentManifest/componentMeta` | 14 | 17269.29 | 28.68% | 0.0% |
| `code/core/src/common/js-package-manager` | 18 | 9982.34 | 27.88% | 1.46% |
| `code/core/src/manager/components/sidebar` | 63 | 7976.12 | 15.03% | 12.17% |
| `__monolith__` | 17 | 5248.86 | 0.32% | 0.0% |
| `code/core/src/preview-api/modules/preview-web` | 17 | 5043.97 | 38.46% | 3.66% |
| `code/e2e-tests` | 23 | 4572.25 | 81.87% | 9.39% |
| `test-storybooks/ember-cli/ember-output/assets` | 4 | 3920.74 | 34.86% | 12.31% |
| `code/core/src/core-server/utils` | 51 | 3689.58 | 26.92% | 2.36% |
| `code/lib/cli-storybook/src/automigrate/fixes` | 42 | 3682.53 | 25.49% | 0.52% |
| `code/core/src/cli` | 17 | 3507.82 | 25.49% | 3.78% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/generate-sandboxes.yml` -> **100.0%** Exposure
- `code/core/src/components/components/ToggleButton/ToggleButton.stories.tsx` -> **100.0%** Exposure
- `code/core/src/core-server/utils/save-story/mocks/csf-variances.stories.tsx` -> **100.0%** Exposure
- `code/frameworks/react-native-web-vite/template/cli/ts/Header.stories.tsx` -> **100.0%** Exposure
- `code/frameworks/react-native-web-vite/template/cli/js/Header.stories.jsx` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `code/addons/a11y/src/postinstall.ts` -> **100.0%** Exposure
- `code/addons/links/src/react/components/link.tsx` -> **100.0%** Exposure
- `code/addons/pseudo-states/src/preview/splitSelectors.ts` -> **100.0%** Exposure
- `code/addons/vitest/src/components/Description.tsx` -> **100.0%** Exposure
- `code/addons/vitest/src/components/TestStatusIcon.tsx` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test-storybooks/ember-cli/ember-output/assets/vendor.js` -> **59** Orphaned Functions | **181** Duplicates
- `code/core/src/manager-api/tests/refs.test.ts` -> **0** Orphaned Functions | **33** Duplicates
- `code/core/src/instrumenter/instrumenter.test.ts` -> **3** Orphaned Functions | **24** Duplicates
- `.github/workflows/generate-sandboxes.yml` -> **0** Orphaned Functions | **16** Duplicates
- `code/lib/create-storybook/src/services/ProjectTypeService.ts` -> **0** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `16` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6589` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.893)
- **Top Global Matches:** file_cluster_10: 5.893, file_cluster_2: 8.437, file_cluster_13: 8.53
- **Magnitude:** 7021.58 | **LOC:** 361 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Guard Balance (formerly Safety Score) (43.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 104`, `args: 46`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `io: 1`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 43`, `test: 46`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` command.ts, BUNProxy.ts, JsPackageManagerFactory.ts, NPMProxy.ts, PNPMProxy.ts, Yarn1Proxy.ts, Yarn2Proxy.ts, index.ts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/manager/components/sidebar/mockdata.large.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.169)
- **Top Global Matches:** file_cluster_2: 4.169, file_cluster_17: 5.888, file_cluster_15: 6.731
- **Magnitude:** 5098.32 | **LOC:** 26727 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.153; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (58.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.4%), Concurrency Surface (formerly Concurrency) (13.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1991`
* *Risk/State:* `state_mutation: 4542`, `planned_debt: 1`
* *Architecture:* `io: 1543`, `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000554
  * `Imports (Out-Degree: 1):` types.ts
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.props.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.166)
- **Top Global Matches:** file_cluster_10: 6.166, file_cluster_0: 6.317, file_cluster_13: 7.977
- **Magnitude:** 4674.24 | **LOC:** 756 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.8%), Guard Balance (formerly Safety Score) (38.2%), Complexity Load (formerly Cognitive Load) (22.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 357`, `args: 94`, `func_start: 72`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 74`, `import: 43`
* *Defense:* `safety: 46`, `doc: 4`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Accordion, Button, Panel, Widget, componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test-storybooks/ember-cli/ember-output/assets/vendor.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 15.214)
- **Top Global Matches:** file_cluster_12: 15.214, file_cluster_4: 15.472, file_cluster_15: 16.231
- **Magnitude:** 3907.22 | **LOC:** 61094 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 1.333; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (65.9%), Guard Balance (formerly Safety Score) (63.3%), Debt Markers (formerly Tech Debt) (49.2%)
- **Documentation Coverage:** 73.7689% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EmberRouter` **(Compute Cores)** (Impact: 286.7)
    * *Intent:* */
  * `Route` **(Many-Argument Workhorses)** (Impact: 171.2)
    * *Intent:* */
  * `Router` **(I/O & Config Routines)** (Impact: 156.8)
  * `RehydrateBuilder` **(Defensive Guards)** (Impact: 148.2)
  * `Meta` **(Defensive Guards)** (Impact: 128.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 74 instances
* *Amplified Cascading Flux:* 4462 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 531
* *State Mutation (weighted view):* 15914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7591`, `structural_boundaries: 9266`, `args: 4466`, `func_start: 5591`
* *Risk/State:* `safety_bypasses: 511`, `high_risk_execution: 4`, `state_mutation: 6990`, `dead_code: 15`, `planned_debt: 92`, `fragile_debt: 31`, `duplicate_logic: 181`, `unreferenced_by_name: 59`
* *Architecture:* `io: 4`, `api: 18`, `concurrency: 161`, `import: 20`
* *Defense:* `safety: 3610`, `doc: 1189`, `test: 5`, `immutability_locks: 31`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044934
  * `Imports (Out-Degree: 0):` ) +, component, helper, modifier, string, ember, bar, exports...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.301)
- **Top Global Matches:** file_cluster_10: 7.301, file_cluster_12: 7.919, file_cluster_15: 9.856
- **Magnitude:** 3849.6 | **LOC:** 4120 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.3%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createAndRenderPreview` **(Callbacks & Closures)** (Impact: 4.9)
  * `openGate` **(Callbacks & Closures)** (Impact: 2.9)
  * `serializeError` **(Callbacks & Closures)** (Impact: 1.6)
  * `gatedImportFn` **(Callbacks & Closures)** (Impact: 1.6)
  * `play` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 500 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 3136
* *State Mutation (weighted view):* 622
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 820`, `args: 326`, `func_start: 189`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 550`, `duplicate_logic: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 38`, `api: 1`, `concurrency: 636`, `import: 12`
* *Defense:* `safety: 29`, `doc: 2`, `test: 522`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` index.ts, index.ts, PreviewWeb.mockdata.ts, PreviewWeb.tsx, WebView.ts, global, object, client-logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.detection.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.174)
- **Top Global Matches:** file_cluster_10: 5.174, file_cluster_13: 7.726, file_cluster_0: 7.898
- **Magnitude:** 2769.44 | **LOC:** 338 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (58.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Guard Balance (formerly Safety Score) (31.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 68
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 176`, `args: 60`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 39`, `concurrency: 58`, `import: 24`
* *Defense:* `safety: 33`, `test: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Lazy, Target, componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.419)
- **Top Global Matches:** file_cluster_10: 5.419, file_cluster_0: 5.907, file_cluster_13: 6.062
- **Magnitude:** 2063.19 | **LOC:** 420 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (70.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.4%), Guard Balance (formerly Safety Score) (39.9%), Mutation Surface (formerly State Flux) (14.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 126`, `args: 36`, `func_start: 31`, `class_start: 16`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 4`, `api: 27`, `concurrency: 14`, `import: 35`
* *Defense:* `safety: 29`, `doc: 18`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` getComponentImports.ts, accordion, button, componentMetaExtractor.test-helpers.ts, dialog, accordion, override, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/cli/AddonVitestService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.401)
- **Top Global Matches:** file_cluster_7: 6.401, file_cluster_12: 8.283, file_cluster_5: 8.828
- **Magnitude:** 1999.28 | **LOC:** 896 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.8%), Mutation Surface (formerly State Flux) (39.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 172
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 230`, `args: 99`, `func_start: 63`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 16`
* *Architecture:* `io: 22`, `api: 20`, `concurrency: 122`, `import: 26`
* *Defense:* `safety: 12`, `test: 175`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index.ts, AddonVitestService.ts, vite.config, find, execa, promises, node:os, common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.defaultValue.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.394)
- **Top Global Matches:** file_cluster_10: 4.394, file_cluster_13: 6.102, file_cluster_2: 6.635
- **Magnitude:** 1711.98 | **LOC:** 399 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.3%), Complexity Load (formerly Cognitive Load) (49.2%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 137`, `args: 43`, `func_start: 39`, `class_start: 22`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 21`, `concurrency: 40`, `import: 23`
* *Defense:* `safety: 22`, `doc: 3`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` componentMetaExtractor.test-helpers.ts, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.qa.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.099)
- **Top Global Matches:** file_cluster_5: 7.099, file_cluster_0: 7.821, file_cluster_12: 7.931
- **Magnitude:** 1547.92 | **LOC:** 605 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.2%), Guard Balance (formerly Safety Score) (45.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Mutation Surface (formerly State Flux) (15.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 193`, `args: 57`, `func_start: 27`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 7`
* *Architecture:* `api: 22`, `concurrency: 28`, `import: 20`
* *Defense:* `safety: 24`, `doc: 28`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Button, componentMetaExtractor.test-helpers.ts, index, override, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/reactDocgen/extractReactDocgenInfo.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.319)
- **Top Global Matches:** file_cluster_10: 4.319, file_cluster_2: 5.263, file_cluster_0: 6.113
- **Magnitude:** 1484.68 | **LOC:** 747 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.8%), Concurrency Surface (formerly Concurrency) (25.3%), Connectivity (formerly Api Exposure) (7.2%), Complexity Load (formerly Cognitive Load) (6.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 115`, `args: 34`, `func_start: 7`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 19`, `doc: 6`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fixtures.ts, extractReactDocgenInfo.ts, memfs, react, ts-dedent, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 4.997)
- **Top Global Matches:** file_cluster_8: 4.997, file_cluster_6: 13.653, file_cluster_4: 22.487
- **Magnitude:** 1215.92 | **LOC:** 1728 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 0.478; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolvePropsFromStoryFile` **(Many-Argument Workhorses)** (Impact: 115.3)
    * *Intent:* /** * Resolves the selected component symbol and props type by finding JSX usage of the target * com...
  * `serializeComponentDoc` **(Many-Argument Workhorses)** (Impact: 92.7)
    * *Intent:* // --------------------------------------------------------------------------- // Props type → Compo...
  * `resolveComponentSymbol` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* * Normalizes the symbol we get from JSX/member resolution to the declaration symbol that owns the * ...
  * `resolveLiteralValue` **(Many-Argument Workhorses)** (Impact: 75.3)
    * *Intent:* /** * Resolves an expression to its literal string representation. * * For identifiers like `DEFAULT...
  * `extractStaticDefaultProps` **(Many-Argument Workhorses)** (Impact: 70.8)
    * *Intent:* /** * Extracts default values from `Component.defaultProps = {...}` and `static defaultProps = {...}...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 195`, `args: 49`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `state_mutation: 47`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 7`, `import: 3`
* *Defense:* `safety: 45`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.478
  * `Choke Point (Betweenness):` 0.000597 | `Ripple Effect (Closeness):` 0.02991
  * `Imports (Out-Degree: 2):` types.ts, utils.ts, typescript
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `code/renderers/react/src/__test__/portable-stories-legacy.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.053)
- **Top Global Matches:** file_cluster_0: 8.053, file_cluster_10: 8.128, file_cluster_12: 9.119
- **Magnitude:** 1213.51 | **LOC:** 218 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (53.3%), Guard Balance (formerly Safety Score) (38.9%), Mutation Surface (formerly State Flux) (27.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 53`, `args: 26`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `concurrency: 15`, `import: 9`
* *Defense:* `safety: 5`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index.ts, Button.stories.tsx, Button.tsx, react, react, expect-type, react, preview-api...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/__test__/portable-stories.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.123)
- **Top Global Matches:** file_cluster_10: 7.123, file_cluster_0: 7.511, file_cluster_13: 9.039
- **Magnitude:** 1113.79 | **LOC:** 216 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Guard Balance (formerly Safety Score) (37.4%), Complexity Load (formerly Cognitive Load) (26.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 56`, `args: 27`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `concurrency: 20`, `import: 10`
* *Defense:* `safety: 4`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` index.ts, Button.stories.tsx, Button.tsx, ComponentWithError.stories.tsx, react, react, expect-type, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/core-server/utils/StoryIndexGenerator.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.419)
- **Top Global Matches:** file_cluster_10: 4.419, file_cluster_2: 4.616, file_cluster_17: 6.012
- **Magnitude:** 1092.92 | **LOC:** 2425 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Concurrency (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 287`, `args: 74`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 256`
* *Architecture:* `io: 1`, `concurrency: 155`, `import: 13`
* *Defense:* `safety: 1`, `doc: 6`, `test: 133`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` tags.ts, common-preset.ts, StoryIndexGenerator.ts, async () => 
        const csfSpecifier: NormalizedStoriesSpecifier = normalizeStoriesEntry(, node:path, common, csf, csf-tools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/e2e-tests/addon-docs.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.137)
- **Top Global Matches:** file_cluster_10: 5.137, file_cluster_2: 6.936, file_cluster_13: 7.299
- **Magnitude:** 1087.36 | **LOC:** 292 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.8%), Mutation Surface (formerly State Flux) (92.8%), Guard Balance (formerly Safety Score) (46.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 74`, `args: 15`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `concurrency: 67`, `import: 4`
* *Defense:* `safety: 3`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util.ts, test, process, ts-dedent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/lib/create-storybook/src/services/FrameworkDetectionService.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.288)
- **Top Global Matches:** file_cluster_7: 6.288, file_cluster_12: 7.865, file_cluster_5: 9.1
- **Magnitude:** 1043.66 | **LOC:** 326 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Guard Balance (formerly Safety Score) (47.9%), Complexity Load (formerly Cognitive Load) (20.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 86`, `args: 38`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 2`
* *Architecture:* `concurrency: 28`, `import: 7`
* *Defense:* `safety: 2`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` FrameworkDetectionService.ts, find, common, node-logger, types, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/core/src/csf-tools/CsfFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.741)
- **Top Global Matches:** file_cluster_6: 6.741, file_cluster_4: 12.013, file_cluster_8: 14.167
- **Magnitude:** 926.1 | **LOC:** 1113 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **9**; blast radius 0.547; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.0%), Connectivity (formerly Api Exposure) (67.3%), Guard Balance (formerly Safety Score) (62.2%)
- **Documentation Coverage:** 79.2212% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(I/O & Config Routines)** (Impact: 187.3)
  * `enter` **(Compute Cores)** (Impact: 104.9)
  * `enter` **(Compute Cores)** (Impact: 43.0)
  * `_parseMeta` **(Compute Cores)** (Impact: 42.8)
  * `enter` **(Compute Cores)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 145`, `args: 66`, `func_start: 33`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 94`, `dead_code: 10`, `planned_debt: 3`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 28`, `api: 29`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 20`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.000385 | `Ripple Effect (Closeness):` 0.047302
  * `Imports (Out-Degree: 9):` tags.ts, PrintResultType.ts, findVarInitialization.ts, promises, babel, csf, node-logger, types...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `code/core/src/shared/universal-store/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.354)
- **Top Global Matches:** file_cluster_10: 5.354, file_cluster_12: 6.543, file_cluster_2: 6.654
- **Magnitude:** 898.96 | **LOC:** 1226 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.184; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.6%), Guard Balance (formerly Safety Score) (45.8%), Mutation Surface (formerly State Flux) (18.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 55
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 182`, `args: 71`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 15`
* *Architecture:* `concurrency: 40`, `import: 6`
* *Defense:* `safety: 13`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.000277
  * `Imports (Out-Degree: 4):` instances.ts, index.ts, mock.ts, types.ts, ts-dedent, vitest
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `code/core/src/csf-tools/ConfigFile.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.974)
- **Top Global Matches:** file_cluster_6: 6.974, file_cluster_4: 8.914, file_cluster_12: 16.265
- **Magnitude:** 854.86 | **LOC:** 1203 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **5**; blast radius 0.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (60.0%), Connectivity (formerly Api Exposure) (55.7%), Complexity Load (formerly Cognitive Load) (38.4%)
- **Documentation Coverage:** 67.7549% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setImport` **(Compute Cores)** (Impact: 52.5)
    * *Intent:* * // import foo from 'bar'; * setImport('foo', 'bar'); * * // import * as foo from 'bar'; * setImpor...
  * `setRequireImport` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* * * ```ts * // const { foo } = require('bar'); * setRequireImport(['foo'], 'bar'); * * // const foo ...
  * `parse` **(I/O & Config Routines)** (Impact: 46.9)
  * `_removeRequireImport` **(Compute Cores)** (Impact: 41.6)
  * `_removeImport` **(Compute Cores)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 168`, `args: 91`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 64`, `dead_code: 15`, `fragile_debt: 2`
* *Architecture:* `io: 50`, `api: 21`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 11`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.553
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.049234
  * `Imports (Out-Degree: 5):` PrintResultType.ts, promises, babel, node-logger, ts-dedent
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `code/core/src/core-server/utils/__tests__/index-extraction.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.635)
- **Top Global Matches:** file_cluster_2: 3.635, file_cluster_10: 4.244, file_cluster_17: 5.225
- **Magnitude:** 838.67 | **LOC:** 491 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.1%), Guard Balance (formerly Safety Score) (50.4%), Mutation Surface (formerly State Flux) (39.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 60`, `args: 16`, `func_start: 7`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 1`, `concurrency: 21`, `import: 7`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tags.ts, StoryIndexGenerator.ts, node:path, common, types, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/vue3/src/__tests__/composeStories/portable-stories.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.795)
- **Top Global Matches:** file_cluster_10: 5.795, file_cluster_13: 7.962, file_cluster_12: 8.027
- **Magnitude:** 778.0 | **LOC:** 156 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.2%), Guard Balance (formerly Safety Score) (38.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.8%), Complexity Load (formerly Cognitive Load) (20.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 42`, `args: 21`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `concurrency: 11`, `import: 8`
* *Defense:* `safety: 3`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` portable-stories.ts, Button.stories.ts, Button.vue, vue3, vue, expect-type, preview-api, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaProject.storyExtraction.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.92)
- **Top Global Matches:** file_cluster_10: 4.92, file_cluster_0: 5.581, file_cluster_13: 6.165
- **Magnitude:** 768.85 | **LOC:** 415 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (74.5%), Guard Balance (formerly Safety Score) (45.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.8%), Mutation Surface (formerly State Flux) (12.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 131`, `args: 32`, `func_start: 26`, `class_start: 11`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 28`, `concurrency: 16`, `import: 27`
* *Defense:* `safety: 10`, `doc: 13`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AttachedMember, Button, Compound, DefaultExport, ForwardRefButton, GenericList, MemoButton, NamespaceCompound...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/renderers/react/src/componentManifest/componentMeta/ComponentMetaManager.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.972)
- **Top Global Matches:** file_cluster_10: 3.972, file_cluster_2: 5.678, file_cluster_13: 6.343
- **Magnitude:** 758.77 | **LOC:** 388 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (59.0%), Guard Balance (formerly Safety Score) (44.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.2%), Complexity Load (formerly Cognitive Load) (9.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 71`, `args: 31`, `func_start: 12`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 27`, `api: 14`, `import: 23`
* *Defense:* `safety: 8`, `test: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` getComponentImports.ts, Button, Card, ComponentMetaManager.ts, Tag, test-helpers.ts, node:fs, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `code/core/src/manager/utils/tree.ts` (TYPESCRIPT) | Magnitude: 109.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 68, branch: 42, core_var_decl: 22
- `code/core/src/manager/components/sidebar/SidebarBottom.tsx` (TYPESCRIPT) | Magnitude: 76.38 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 49, core_var_decl: 32, args: 21
- `code/core/src/toolbar/components/ToolbarManager.tsx` (TYPESCRIPT) | Magnitude: 5.42 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 14, import: 5, core_var_decl: 5
- `code/core/src/common/utils/framework.ts` (TYPESCRIPT) | Magnitude: 18.16 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 52, generics: 4, structural_boundaries: 3, api: 2
- `code/core/src/manager/components/layout/Drag.tsx` (TYPESCRIPT) | Magnitude: 15.0 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 101, branch: 17, structural_boundaries: 12, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `code/renderers/react/src/componentManifest/fixtures.ts` (TYPESCRIPT) | Magnitude: 96.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 56, core_var_decl: 24, state_mutation: 17
- `code/frameworks/angular/template/cli/page.stories.ts` (TYPESCRIPT) | Magnitude: 10.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, core_var_decl: 6, concurrency: 5
- `code/lib/cli-storybook/src/automigrate/fixes/addon-storysource-code-panel.ts` (TYPESCRIPT) | Magnitude: 35.04 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 25, branch: 8, decorators: 7
- `code/renderers/vue3/template/stories_vue3-vite-default-ts/OverrideArgs.stories.js` (JAVASCRIPT) | Magnitude: 9.96 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 6, core_var_decl: 4, design_snake_case: 3
- `scripts/utils/filterExistsInCodeDir.ts` (TYPESCRIPT) | Magnitude: 14.08 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, concurrency: 7, io: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `code/frameworks/angular/template/components/html.component.ts` (TYPESCRIPT) | Magnitude: 7.9 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, decorators: 4, args: 2
- `scripts/tasks/run-registry.ts` (TYPESCRIPT) | Magnitude: 24.44 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 16, concurrency: 6, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `code/lib/cli-storybook/src/automigrate/fixes/wrap-getAbsolutePath.test.ts` (TYPESCRIPT) | Magnitude: 22.58 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 42, args: 15, concurrency: 15
- `code/core/src/csf/csf-factories.test.ts` (TYPESCRIPT) | Magnitude: 6.28 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 16, core_var_decl: 14, args: 9
- `code/lib/cli-storybook/src/automigrate/fixes/addon-mdx-gfm-remove.test.ts` (TYPESCRIPT) | Magnitude: 168.32 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 52, args: 19, concurrency: 17
- `code/core/src/instrumenter/types.ts` (TYPESCRIPT) | Magnitude: 1.39 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 30, branch: 20, api: 10
- `code/core/src/telemetry/index.ts` (TYPESCRIPT) | Magnitude: 80.56 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 23, branch: 15, import: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `code/core/src/components/components/syntaxhighlighter/clipboard.ts` (TYPESCRIPT) | Magnitude: 14.74 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, globals: 7, structural_boundaries: 5, safety: 4
- `code/lib/create-storybook/src/generators/NUXT/index.ts` (TYPESCRIPT) | Magnitude: 24.4 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 9, import: 4, state_mutation: 3
- `code/core/src/manager/settings/whats_new_footer.stories.tsx` (TYPESCRIPT) | Magnitude: 17.36 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, core_var_decl: 3, api: 2
- `test-storybooks/portable-stories-kitchen-sink/nextjs/jest.config.js` (JAVASCRIPT) | Magnitude: 18.5 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, test: 4, decorators: 3, core_var_decl: 3
- `code/core/template/stories/controls/disable.stories.ts` (TYPESCRIPT) | Magnitude: 18.42 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, api: 3, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `code/core/src/manager-api/initial-state.ts` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 8, args: 2, safety_bypasses: 2, import: 2
- `code/core/src/test/utils.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.212** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: generics: 16, structural_boundaries: 8, branch: 4, concurrency: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `code/core/src/components/components/Select/helpers.tsx` (TYPESCRIPT) | Magnitude: 35.96 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 36, branch: 14, api: 13
- `scripts/ci/init-empty.ts` (TYPESCRIPT) | Magnitude: 44.34 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 20, state_mutation: 15, args: 7
- `test-storybooks/portable-stories-kitchen-sink/react-vitest-3/stories/UnhandledErrors.stories.tsx` (TYPESCRIPT) | Magnitude: 19.2 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 9, branch: 6, core_var_decl: 5
- `test-storybooks/portable-stories-kitchen-sink/react/stories/UnhandledErrors.stories.tsx` (TYPESCRIPT) | Magnitude: 19.2 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 9, branch: 6, core_var_decl: 5
- `code/core/template/stories/mount-in-play.stories.ts` (TYPESCRIPT) | Magnitude: 26.78 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, safety: 3, concurrency: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `code/lib/create-storybook/src/commands/PreflightCheckCommand.ts` (TYPESCRIPT) | Magnitude: 53.9 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 27, branch: 13, concurrency: 11
- `code/builders/builder-webpack5/src/plugins/webpack-inject-mocker-runtime-plugin.ts` (TYPESCRIPT) | Magnitude: 19.62 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 15, safety: 9, branch: 7
- `code/frameworks/angular/src/client/angular-beta/RendererFactory.ts` (TYPESCRIPT) | Magnitude: 44.02 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, branch: 10, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `code/core/src/components/index.ts` (TYPESCRIPT) | Magnitude: 109.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 115, import: 92, api: 91, indent_spaces: 7
- `code/core/src/csf-tools/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `code/frameworks/angular/src/client/index.ts` (TYPESCRIPT) | Magnitude: 19.64 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 6, import: 6, explicit_casts: 1
- `code/core/src/common/index.ts` (TYPESCRIPT) | Magnitude: 62.96 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 50, api: 47, import: 47, safety: 1
- `code/lib/create-storybook/src/commands/index.ts` (TYPESCRIPT) | Magnitude: 26.3 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 14, api: 11, import: 11, indent_spaces: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `code/core/src/manager/provider.ts` (TYPESCRIPT) | Magnitude: 8.66 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, api: 4, args: 3
- `code/renderers/vue3/template/stories_vue3-vite-default-ts/SourceCode.stories.ts` (TYPESCRIPT) | Magnitude: 17.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, import: 3, branch: 2
- `code/core/src/theming/modules/syntax.ts` (TYPESCRIPT) | Magnitude: 11.8 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 12, core_var_decl: 5, design_camel_case: 4
- `code/core/src/core-server/utils/__search-files-tests__/src/commonjs-module.js` (JAVASCRIPT) | Magnitude: 36.26 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: api: 6, state_mutation: 5, indent_spaces: 3, branch: 2
- `.github/workflows/nx.yml` (YAML) | Magnitude: 45.3 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 135, branch: 25, core_var_decl: 17, globals: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.ts` (TYPESCRIPT) | Magnitude: 125.5 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 50, branch: 39, core_var_decl: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `code/core/src/components/components/Form/Textarea.tsx` (TYPESCRIPT) | Magnitude: 5.96 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 19, branch: 14, generics: 11
- `code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-parameters.test.ts` (TYPESCRIPT) | Magnitude: 78.96 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 31, args: 11, closures: 11
- `code/renderers/react/src/csf-factories.test.tsx` (TYPESCRIPT) | Magnitude: 59.74 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 287, structural_boundaries: 113, core_var_decl: 66, args: 65
- `code/core/src/actions/runtime/action.ts` (TYPESCRIPT) | Magnitude: 76.4 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 29, branch: 23, core_var_decl: 21
- `code/core/src/node-logger/tasks.test.ts` (TYPESCRIPT) | Magnitude: 22.08 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 19, safety: 12, safety_bypasses: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `code/core/src/preview-api/modules/store/args.ts` (TYPESCRIPT) | Magnitude: 144.9 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 87, branch: 60, core_var_decl: 25
- `code/builders/builder-vite/src/plugins/vite-mock/plugin.ts` (TYPESCRIPT) | Magnitude: 101.2 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 29, branch: 19, core_var_decl: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `code/frameworks/vue3-vite/template/cli/ts/Page.stories.ts` (TYPESCRIPT) | Magnitude: 11.68 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 15, core_var_decl: 7, concurrency: 5
- `code/renderers/vue3/template/cli/ts/Page.stories.ts` (TYPESCRIPT) | Magnitude: 11.68 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 15, core_var_decl: 7, concurrency: 5
- `code/lib/cli-storybook/src/automigrate/fixes/addon-a11y-addon-test.test.ts` (TYPESCRIPT) | Magnitude: 96.14 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 641, structural_boundaries: 182, core_var_decl: 63, test: 61
- `code/frameworks/angular/src/client/angular-beta/utils/NgComponentAnalyzer.ts` (TYPESCRIPT) | Magnitude: 65.22 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 42, branch: 25, core_var_decl: 20
- `code/addons/vitest/src/manager-store.ts` (TYPESCRIPT) | Magnitude: 19.38 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, api: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `code/lib/cli-storybook/src/sandbox-templates.ts` (TYPESCRIPT) | Magnitude: 151.6 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 909, decorators: 157, state_mutation: 104, structural_boundaries: 63
- `code/core/src/docs-tools/argTypes/enhanceArgTypes.test.ts` (TYPESCRIPT) | Magnitude: 21.14 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 246, structural_boundaries: 58, test: 32, args: 24
- `code/frameworks/angular/src/builders/start-storybook/index.ts` (TYPESCRIPT) | Magnitude: 94.38 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 195, structural_boundaries: 46, branch: 25, import: 19
- `code/frameworks/angular/src/client/decorators.ts` (TYPESCRIPT) | Magnitude: 51.16 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 58, branch: 24, structural_boundaries: 23, core_var_decl: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `scripts/utils/yarn.ts` -> Churn: **63.16%** | Cog Load: 84.0557% | Debt: 13.5797%
- `code/addons/vitest/src/vitest-plugin/index.ts` -> Churn: **62.15%** | Cog Load: 85.093% | Debt: 9.4279%
- `code/core/src/manager-api/modules/stories.ts` -> Churn: **59.96%** | Cog Load: 55.847% | Debt: 29.1898%
- `code/core/src/core-server/presets/common-preset.ts` -> Churn: **58.78%** | Cog Load: 70.7507% | Debt: 0.0%
- `code/lib/create-storybook/src/initiate.ts` -> Churn: **58.78%** | Cog Load: 67.6015% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/core/src/common/js-package-manager/JsPackageManagerFactory.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 7021.58
- `code/core/src/manager/components/sidebar/mockdata.large.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 5098.32
- `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.props.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 4674.24
- `code/core/src/preview-api/modules/preview-web/PreviewWeb.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 3849.6
- `code/renderers/react/src/componentManifest/componentMeta/componentMetaExtractor.detection.test.ts` -> **Kasper Peulen** (100.0% isolated ownership) | Magnitude: 2769.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/core/src/csf/index.ts` -> **Severity: 1.102** (Bridge: 0.0117 * Flux: 94.3608%)
- `code/core/src/manager-api/root.tsx` -> **Severity: 0.35** (Bridge: 0.0044 * Flux: 79.413%)
- `code/core/src/core-server/utils/StoryIndexGenerator.ts` -> **Severity: 0.297** (Bridge: 0.003 * Flux: 100.0%)
- `code/core/src/core-server/build-dev.ts` -> **Severity: 0.226** (Bridge: 0.0023 * Flux: 99.4202%)
- `code/core/src/core-server/build-static.ts` -> **Severity: 0.205** (Bridge: 0.0021 * Flux: 99.2824%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `code/core/src/client-logger/index.ts` -> **Severity: 5.997** (Embedded: 0.0722 * Error Risk: 83.046%)
- `code/core/src/shared/universal-store/mock.ts` -> **Severity: 4.87** (Embedded: 0.0609 * Error Risk: 80.0%)
- `code/core/src/types/modules/core-common.ts` -> **Severity: 4.534** (Embedded: 0.0696 * Error Risk: 65.109%)
- `code/core/src/node-logger/logger/console.ts` -> **Severity: 4.357** (Embedded: 0.0547 * Error Risk: 79.6689%)
- `code/core/src/shared/universal-store/use-universal-store-manager.ts` -> **Severity: 4.357** (Embedded: 0.0545 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `code/core/src/client-logger/index.ts` -> **Severity: 953.893** (Blast Radius: 10.299 * Doc Risk: 92.62%)
- `code/core/src/shared/universal-store/index.ts` -> **Severity: 708.251** (Blast Radius: 14.172 * Doc Risk: 49.9754%)
- `code/core/src/theming/utils.ts` -> **Severity: 384.69** (Blast Radius: 3.983 * Doc Risk: 96.583%)
- `code/core/src/test/index.ts` -> **Severity: 348.508** (Blast Radius: 4.542 * Doc Risk: 76.73%)
- `code/lib/cli-storybook/src/sandbox-templates.ts` -> **Severity: 325.4** (Blast Radius: 3.254 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 354 literal sites + 3 sites through wrappers = 357
- **`panics_and_aborts`:** 923 literal sites + 15 sites through wrappers = 938

- `runGitCommand` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `code/core/src/core-server/change-detection/GitDiffProvider.ts`
- `logConfig` (function, debug_prints, primitive): 2 call sites in 2 files -- `code/core/src/common/utils/log-config.ts`
- `throwError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `test-storybooks/portable-stories-kitchen-sink/react-vitest-3/stories/UnhandledErrors.stories.tsx`
- `throwError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `test-storybooks/portable-stories-kitchen-sink/react/stories/UnhandledErrors.stories.tsx`
- `CustomError` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `code/core/src/manager/components/error-boundary/ManagerErrorBoundary.stories.tsx`
- `handleCommandFailure` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `code/lib/create-storybook/src/initiate.ts`
- `logAbort` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test-storybooks/ember-cli/ember-output/assets/vendor.js`
- `myTimer` (function, debug_prints, primitive): 1 call sites in 1 files -- `code/frameworks/angular/template/stories/basics/component-with-ng-on-destroy/component-with-on-destroy.stories.ts`
- `needsNew` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test-storybooks/ember-cli/ember-output/assets/vendor.js`
- `needsResolver` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test-storybooks/ember-cli/ember-output/assets/vendor.js`
- `unsupportedModule` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test-storybooks/ember-cli/ember-output/assets/vendor.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24266 call pairs -- scoped 22.8%, unique 0.0%, ambiguous 19.4%, external 57.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 18374 | 21.7% | 0.0% | 21.2% | 57.0% |
| javascript | 5816 | 26.5% | 0.0% | 13.7% | 59.8% |
| html | 63 | 0.0% | 0.0% | 14.3% | 85.7% |
| shell | 13 | 0.0% | 0.0% | 0.0% | 100.0% |

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
