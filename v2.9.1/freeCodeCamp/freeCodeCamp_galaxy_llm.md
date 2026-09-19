# ARCHITECTURAL_BRIEF: freeCodeCamp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/freeCodeCamp/freeCodeCamp.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 18305 analyzed artifact(s), 207114 LOC.
- **Load-bearing artifact:** `curriculum/structure/blocks/react.json` -- 344 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `api/src/schemas.ts` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `api/src/routes/protected/settings.test.ts` at magnitude 9230.47 (structural weight, not risk).
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
| Total Artifacts | 18528 |
| Analyzed Artifacts (Scanned) | 18305 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 223 |
| Total LOC | 207114 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5231 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1963 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9939 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 162 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 15918 | 0 | 87.0% |
| JSON | 1149 | 80157 | 6.3% |
| TYPESCRIPT | 898 | 90652 | 4.9% |
| JAVASCRIPT | 183 | 26671 | 1.0% |
| CSS | 86 | 7655 | 0.5% |
| YAML | 37 | 838 | 0.2% |
| PLAINTEXT | 18 | 1 | 0.1% |
| XML | 10 | 1006 | 0.1% |
| HTML | 2 | 21 | 0.0% |
| DOCKERFILE | 2 | 98 | 0.0% |
| SHELL | 2 | 15 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `7.676`
> **Composition Archetype:** `Flat Modular Platform` (z +7.68; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 94%, Declarative / Non-Code 2%, Callbacks & Closures Files 1%, Generic / Templated Code Files 1%, Large Core Modules (2) 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2359 | 12.9% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 15935 | 87.1% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 223*

**Composition by Extension & Reason:**
- `.tsx`: 8x Excluded (Saturation: Line 13 exceeds 500 chars), 7x Excluded (Saturation: Line 18 exceeds 500 chars), 3x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 53 LOC), 2x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 11x Excluded (Static Asset Blob without Intent: 1531 LOC), 5x Excluded (Massive Static Asset Blob: 10022 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff`: 23x Excluded (Explicitly Denied Extension: '.woff')
- `.snap`: 17x Unsupported Format (.snap), 1x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 59 exceeds 500 chars)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.woff2`: 5x Excluded (Explicitly Denied Extension: '.woff2')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 31800 LOC exceeds safe regex boundaries)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.js`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (Saturation: Line 74 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.ts`: 1x Unsupported Format (.undeterminable), 1x Packed Payload Guard (Impossible Density: 3.59 hits/line)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 13.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 80.2 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.5 | 0.4 | 0.4 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 87.1 | 10.0 | 12.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 293 | 125 | 0 | `client/src/templates/Introduction/components/block.test.tsx` |
| cleanup | 109 | 56 | 0 | `client/src/templates/Challenges/classic/show.tsx` |
| guards | 2218 | 427 | 0 | `api/src/routes/protected/settings.ts` |
| danger | 1016 | 250 | 0 | `api/__mocks__/exam-environment-exam.ts` |
| concurrency | 6730 | 388 | 0 | `api/src/routes/protected/challenge.test.ts` |
| connectivity | 2145 | 727 | 0 | `client/src/components/layouts/variables.css` |
| io | 1457 | 331 | 0 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| crypto | 1 | 1 | 0 | `tools/client-plugins/gatsby-source-challenges/create-challenge-nodes.js` |
| ipc | 100 | 45 | 0 | `packages/challenge-builder/src/worker-executor.test.js` |
| time | 286 | 83 | 0 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| serialization | 115 | 51 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| regex | 180 | 90 | 0 | `e2e/donate-page-default.spec.ts` |
| events | 655 | 155 | 0 | `api/src/routes/protected/challenge.ts` |
| tests | 7208 | 316 | 0 | `api/src/routes/protected/challenge.test.ts` |
| docs | 424 | 154 | 0 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| debt | 511 | 204 | 0 | `curriculum/src/test/test-challenges.js` |
| mutation | 18271 | 1004 | 0 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| dead_code | 198 | 122 | 0 | `client/src/templates/Introduction/super-block-intro.test.tsx` |
| credential | 20 | 12 | 0 | `api/src/routes/protected/settings.test.ts` |
| threat | 68 | 32 | 0 | `client/i18n/schema-validation.ts` |
| ml_ai | 88 | 44 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| ui | 4399 | 363 | 0 | `client/src/client-only-routes/show-certification.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `client/src/assets/icons/top-contributor-badge-emblem.tsx` (Hits: 80)
- `client/src/components/formHelpers/form-validators.test.ts` (Hits: 48)
- `api/src/routes/protected/settings.test.ts` (Hits: 47)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.json** (`curriculum/structure/blocks/react.json`) — 344 inbound connections
2. **react-i18next.js** (`client/__mocks__/react-i18next.js`) — 186 inbound connections
3. **prop-types.ts** (`client/src/redux/prop-types.ts`) — 92 inbound connections
4. **redux.json** (`curriculum/structure/blocks/redux.json`) — 59 inbound connections
5. **gatsby.ts** (`client/__mocks__/gatsby.ts`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **schemas.ts** (`api/src/schemas.ts`) — 47 outbound dependencies
2. **show.tsx** (`client/src/templates/Challenges/classic/show.tsx`) — 46 outbound dependencies
3. **default.tsx** (`client/src/components/layouts/default.tsx`) — 39 outbound dependencies
4. **show.tsx** (`client/src/templates/Challenges/codeally/show.tsx`) — 36 outbound dependencies
5. **show.tsx** (`client/src/templates/Challenges/generic/show.tsx`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `togglePane` **(Compute Cores)** (@ `client/src/templates/Challenges/classic/desktop-layout.tsx`) -> Impact: **98.7** | LOC: 221
- `Scene` **(Compute Cores)** (@ `client/src/templates/Challenges/components/scene/scene.tsx`) -> Impact: **84.3** | LOC: 413
- `generateExam` **(Compute Cores)** (@ `api/src/exam-environment/utils/exam-environment.ts`) -> Impact: **76.5** | LOC: 314
  * *Intent:* /** * Generates an exam for the user, based on the exam configuration. */
- `createLanguageBlock` **(Many-Argument Workhorses)** (@ `tools/challenge-helper-scripts/create-language-block.ts`) -> Impact: **68.5** | LOC: 73
- `render` **(I/O & Config Routines)** (@ `client/src/templates/Introduction/components/block.tsx`) -> Impact: **68.1** | LOC: 462
- `postExamGeneratedExamHandler` **(Many-Argument Workhorses)** (@ `api/src/exam-environment/routes/exam-environment.ts`) -> Impact: **66.8** | LOC: 336
  * *Intent:* /** * Generates an exam for the user. * * Requires token to be validated and TODO: live longer than the exam attempt. */
- `handleSubmit` **(Many-Argument Workhorses)** (@ `client/src/components/profile/components/experience.tsx`) -> Impact: **63.7** | LOC: 201
- `courseCompletionStatus` **(I/O & Config Routines)** (@ `client/src/templates/Introduction/components/block.tsx`) -> Impact: **61.5** | LOC: 411
- `sourceChallengesSourceNodes` **(Defensive Guards)** (@ `tools/client-plugins/gatsby-source-challenges/gatsby-node.js`) -> Impact: **61.1** | LOC: 217
- `transformer` **(Many-Argument Workhorses)** (@ `tools/challenge-parser/parser/plugins/add-video-question.js`) -> Impact: **58.6** | LOC: 132

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `e2e` | 122 | 20715.62 | 52.79% | 1.51% |
| `curriculum/structure/blocks` | 970 | 15887.02 | 0.0% | 0.0% |
| `api/src/routes/protected` | 11 | 11815.97 | 16.74% | 8.36% |
| `api/src/routes/public` | 21 | 5717.79 | 8.24% | 3.05% |
| `api/src/exam-environment/routes` | 2 | 5176.06 | 25.3% | 5.47% |
| `__monolith__` | 10 | 5094.12 | 0.0% | 0.0% |
| `client/src/templates/Challenges/components` | 65 | 3151.04 | 10.96% | 0.63% |
| `api/src/plugins` | 28 | 1912.48 | 22.79% | 5.96% |
| `client/src/components/profile/components` | 30 | 1830.4 | 6.71% | 0.0% |
| `api/src/exam-environment/utils` | 3 | 1789.22 | 6.67% | 3.72% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `api/src/utils/error-formatting.ts` -> **99.9756%** Exposure
- `api/src/utils/create-user.ts` -> **99.9712%** Exposure
- `client/gatsby-browser.tsx` -> **99.7527%** Exposure
- `client/gatsby-ssr.tsx` -> **99.2058%** Exposure
- `api/src/routes/helpers/user-utils.ts` -> **98.5936%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `curriculum/src/test/utils/challenge-titles.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/mongo-ids.js` -> **100.0%** Exposure
- `curriculum/src/test/utils/pseudo-worker.js` -> **100.0%** Exposure
- `packages/challenge-builder/src/worker-executor.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-fill-in-the-blank.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `client/src/templates/Introduction/super-block-intro.test.tsx` -> **14** Orphaned Functions | **0** Duplicates
- `api/src/routes/protected/challenge.ts` -> **0** Orphaned Functions | **5** Duplicates
- `api/src/utils/exam-schemas.ts` -> **5** Orphaned Functions | **0** Duplicates
- `api/src/utils/logger.ts` -> **5** Orphaned Functions | **0** Duplicates
- `client/src/components/growth-book/growth-book-wrapper.test.tsx` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `62` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2633` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `api/src/routes/protected/settings.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 9230.47 | **LOC:** 1598 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (24.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.1%), Guard Balance (formerly Safety Score) (16.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 284`, `args: 109`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 47`, `concurrency: 201`, `import: 7`
* *Defense:* `safety: 63`, `doc: 3`, `test: 284`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, redirect-with-message.js, create-user.js, env.js, auth-helpers.js, settings.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/routes/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4833.42 | **LOC:** 1470 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.2%), Mutation Surface (formerly State Flux) (44.1%), Complexity Load (formerly Cognitive Load) (36.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 70 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 532
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 249`, `args: 77`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 182`, `import: 12`
* *Defense:* `safety: 7`, `doc: 27`, `test: 170`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, env.js, exam-environment-exam-attempt.js, index.js, exam-environment.js, type-provider-typebox, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3274.49 | **LOC:** 648 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.0%), Guard Balance (formerly Safety Score) (26.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.4%), Mutation Surface (formerly State Flux) (10.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 69`, `args: 36`, `func_start: 12`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 8`
* *Architecture:* `io: 11`, `concurrency: 35`, `import: 7`
* *Defense:* `safety: 21`, `test: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, create-user.js, user.js, client, lodash-es, mongodb, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/utils/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1491.76 | **LOC:** 544 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (63.9%), Guard Balance (formerly Safety Score) (42.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.3%), Mutation Surface (formerly State Flux) (11.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 99`, `args: 66`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`
* *Architecture:* `concurrency: 16`, `import: 8`
* *Defense:* `safety: 5`, `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, index.js, exam-environment.js, type-provider-typebox, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/email-subscription.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1036.92 | **LOC:** 283 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (33.1%), Complexity Load (formerly Cognitive Load) (10.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 41`, `args: 15`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`
* *Architecture:* `concurrency: 29`, `import: 5`
* *Defense:* `doc: 1`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, create-user.js, env.js, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/certificate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 909.8 | **LOC:** 477 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (36.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.5%), Mutation Surface (formerly State Flux) (13.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 63`, `args: 22`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `concurrency: 34`, `import: 5`
* *Defense:* `safety: 3`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest.utils.js, get-challenges.js, certificate.js, certification-settings, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/certificate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 883.22 | **LOC:** 360 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Complexity Load (formerly Cognitive Load) (8.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 67`, `args: 22`, `func_start: 11`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `concurrency: 35`, `import: 3`
* *Defense:* `safety: 7`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest.utils.js, certificate-utils.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/components/profile/components/profile-completeness.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 876.02 | **LOC:** 221 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (34.9%), Guard Balance (formerly Safety Score) (16.9%), Complexity Load (formerly Cognitive Load) (8.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 45`, `args: 26`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 14`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 3`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` profile-completeness, react, user-event, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/help-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 860.12 | **LOC:** 250 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.3%), Guard Balance (formerly Safety Score) (31.0%), Mutation Surface (formerly State Flux) (27.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 120
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 69`, `args: 10`, `func_start: 8`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `concurrency: 65`, `import: 2`
* *Defense:* `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/header.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 828.97 | **LOC:** 305 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (82.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%), Guard Balance (formerly Safety Score) (33.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 86`, `args: 20`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2`
* *Architecture:* `io: 3`, `concurrency: 76`, `import: 5`
* *Defense:* `safety: 3`, `test: 58`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` links.json, translations.json, i18n, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/lower-jaw.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 698.23 | **LOC:** 251 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (35.0%), Mutation Surface (formerly State Flux) (33.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 76`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `concurrency: 71`, `import: 3`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` editor, logout, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/completion-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 654.52 | **LOC:** 196 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Guard Balance (formerly Safety Score) (29.9%), Mutation Surface (formerly State Flux) (12.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 71`, `args: 18`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 61`, `import: 5`
* *Defense:* `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, request, url, test, node:child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/quiz-challenge.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 646.76 | **LOC:** 335 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Mutation Surface (formerly State Flux) (36.6%), Guard Balance (formerly Safety Score) (29.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 152
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 101`, `args: 15`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 11`, `concurrency: 92`, `import: 4`
* *Defense:* `test: 50`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` url, test, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/classic/editor.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 513.68 | **LOC:** 1462 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Guard Balance (formerly Safety Score) (64.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.3%), Connectivity (formerly Api Exposure) (34.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setTabTrapped` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `Editor` **(I/O & Config Routines)** (Impact: 21.0)
  * `handleSubmitAndGoButtonBoolean` **(I/O & Config Routines)** (Impact: 17.1)
  * `createDescription` **(Compute Cores)** (Impact: 15.7)
  * `onChange` **(Defensive Guards)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 180`, `args: 106`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 3`, `import: 35`
* *Defense:* `safety: 42`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` env.json, green-pass, helpers, actions, prop-types, selectors, types, curriculum-layout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/components/pinyin-to-hanzi-input.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 513.19 | **LOC:** 365 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (24.4%), Complexity Load (formerly Cognitive Load) (22.9%), Mutation Surface (formerly State Flux) (10.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 55`, `args: 21`, `func_start: 8`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 23`, `import: 5`
* *Defense:* `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pinyin-to-hanzi-input, react, user-event, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/profile.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 501.41 | **LOC:** 209 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%), Complexity Load (formerly Cognitive Load) (29.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 37`, `args: 13`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `concurrency: 30`, `import: 2`
* *Defense:* `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/settings.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 497.24 | **LOC:** 357 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (59.9%), Guard Balance (formerly Safety Score) (54.0%), Mutation Surface (formerly State Flux) (37.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 70`, `args: 13`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 7`
* *Architecture:* `io: 2`, `concurrency: 59`, `import: 5`
* *Defense:* `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, alerts, certification-settings, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/daily-coding-challenge.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 478.78 | **LOC:** 301 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (73.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.6%), Dead Code Surface (formerly Dead Code) (6.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 77`, `args: 17`, `func_start: 10`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 2`, `concurrency: 70`, `import: 2`
* *Defense:* `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` helpers, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/mobile-app-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 456.87 | **LOC:** 160 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (67.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 51`, `args: 18`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 7`, `concurrency: 39`, `import: 2`
* *Defense:* `safety: 1`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/help-button.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 426.49 | **LOC:** 172 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (75.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 50`, `args: 11`, `func_start: 7`
* *Risk/State:* None
* *Architecture:* `concurrency: 44`, `import: 2`
* *Defense:* `safety: 5`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/components/completion-modal.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 417.34 | **LOC:** 242 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (56.8%), Guard Balance (formerly Safety Score) (31.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.5%), Mutation Surface (formerly State Flux) (10.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 39`, `args: 17`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `concurrency: 6`, `import: 16`
* *Defense:* `safety: 4`, `doc: 3`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` test-utils, create-store, prop-types, selectors, curriculum-data, fire-confetti, get-completion-percentage, execute-challenge-saga...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 404.42 | **LOC:** 1704 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.0%), Complexity Load (formerly Cognitive Load) (38.5%), Guard Balance (formerly Safety Score) (31.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(I/O & Config Routines)** (Impact: 3.6)
  * `json` **(I/O & Config Routines)** (Impact: 2.5)
  * `json` **(I/O & Config Routines)** (Impact: 2.3)
  * `json` **(Callbacks & Closures)** (Impact: 1.9)
  * `json` **(Callbacks & Closures)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 320
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 307`, `args: 126`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 23`, `planned_debt: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 36`, `concurrency: 240`, `import: 11`
* *Defense:* `safety: 15`, `doc: 3`, `test: 226`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exam-environment-exam.js, vitest.utils.js, create-user.js, env.js, user.js, client, jsonwebtoken, lodash-es...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/challenge.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 402.52 | **LOC:** 2556 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%), Guard Balance (formerly Safety Score) (28.6%), Complexity Load (formerly Cognitive Load) (13.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `submitExam` **(Callbacks & Closures)** (Impact: 2.0)
  * `createMSUsernameRecord` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 338
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 378`, `args: 155`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `io: 33`, `concurrency: 268`, `import: 13`
* *Defense:* `safety: 34`, `doc: 6`, `test: 383`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` exam.js, vitest.utils.js, get-session-user.js, exam-types.js, challenge-helpers.js, type-provider-typebox, challenge-types, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/portfolio.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 395.68 | **LOC:** 196 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.3%), Guard Balance (formerly Safety Score) (51.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Concurrency (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 66`, `args: 13`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 22`, `planned_debt: 1`
* *Architecture:* `io: 9`, `concurrency: 58`, `import: 3`
* *Defense:* `safety: 8`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/challenge-helper-scripts/create-language-block.ts` -> Churn: **51.69%** | Cog Load: 94.3124% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `api/src/exam-environment/routes/exam-environment.test.ts` -> **Shaun Hamilton** (100.0% isolated ownership) | Magnitude: 4833.42
- `client/src/components/profile/components/profile-completeness.test.tsx` -> **Mrugesh Mohapatra** (100.0% isolated ownership) | Magnitude: 876.02
- `e2e/help-modal.spec.ts` -> **Ahmad Abdolsaheb** (100.0% isolated ownership) | Magnitude: 860.12
- `e2e/lower-jaw.spec.ts` -> **Ahmad Abdolsaheb** (100.0% isolated ownership) | Magnitude: 698.23
- `e2e/completion-modal.spec.ts` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 654.52

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `client/__mocks__/react-i18next.js` -> **Severity: 0.428** (Embedded: 0.0103 * Error Risk: 41.5116%)
- `packages/shared/src/config/chapters.ts` -> **Severity: 0.28** (Embedded: 0.0041 * Error Risk: 68.383%)
- `packages/shared/src/config/blocks.ts` -> **Severity: 0.245** (Embedded: 0.0043 * Error Risk: 56.3934%)
- `packages/shared/src/config/certification-settings.ts` -> **Severity: 0.231** (Embedded: 0.0046 * Error Risk: 50.285%)
- `packages/shared/src/config/donation-settings.ts` -> **Severity: 0.118** (Embedded: 0.0021 * Error Risk: 55.7075%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `client/__mocks__/react-i18next.js` -> **Severity: 278.6** (Blast Radius: 2.786 * Doc Risk: 100.0%)
- `packages/shared/src/config/certification-settings.ts` -> **Severity: 110.5** (Blast Radius: 1.105 * Doc Risk: 100.0%)
- `packages/shared/src/config/challenge-types.ts` -> **Severity: 100.4** (Blast Radius: 1.004 * Doc Risk: 100.0%)
- `e2e/utils/editor.ts` -> **Severity: 61.6** (Blast Radius: 0.616 * Doc Risk: 100.0%)
- `packages/shared/src/utils/polyvinyl.ts` -> **Severity: 53.6** (Blast Radius: 0.536 * Doc Risk: 100.0%)

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
