# ARCHITECTURAL_BRIEF: freeCodeCamp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/freeCodeCamp/freeCodeCamp.git` |
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
- **Scope:** 1386 analyzed artifact(s), 135548 LOC.
- **Load-bearing artifact:** `client/src/redux/prop-types.ts` -- 92 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `api/src/schemas.ts` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 18529 |
| Analyzed Artifacts (Scanned) | 1386 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17143 |
| Total LOC | 135548 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 7.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7168 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0941 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1965 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 224 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 909 | 90292 | 65.6% |
| JAVASCRIPT | 157 | 23682 | 11.3% |
| MARKDOWN | 100 | 0 | 7.2% |
| CSS | 86 | 7655 | 6.2% |
| JSON | 69 | 10210 | 5.0% |
| YAML | 32 | 2571 | 2.3% |
| PLAINTEXT | 18 | 1 | 1.3% |
| XML | 10 | 1006 | 0.7% |
| DOCKERFILE | 2 | 98 | 0.1% |
| SHELL | 2 | 15 | 0.1% |
| HTML | 1 | 18 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1385 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Data / Markup / Trivial 23%, Callbacks & Closures Files 12%, Generic / Templated Code Files 9%, Large Core Modules 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1258 | 90.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 117 | 8.4% |
| Static: Minified & Vendor Opaque Mass | 10 | 0.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17143*

**Composition by Extension & Reason:**
- `.md`: 15846x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1083x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded (Static Asset Blob without Intent: 1531 LOC), 5x Excluded (Massive Static Asset Blob: 10022 LOC)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 30 exceeds 500 chars), 1x Excluded (Saturation: Line 62 exceeds 500 chars)
- `.woff`: 23x Excluded (Explicitly Denied Extension: '.woff')
- `.js`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 17x Unsupported Format (.snap), 1x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Saturation: Line 59 exceeds 500 chars)
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ts`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Packed Payload Guard (Impossible Density: 3.59 hits/line)
- `.mjs`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `.tsx`: 2x Excluded (Saturation: Line 18 exceeds 500 chars), 2x Excluded (Saturation: Line 17 exceeds 500 chars), 1x Excluded (Saturation: Line 21 exceeds 500 chars)
- `.woff2`: 5x Excluded (Explicitly Denied Extension: '.woff2')
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.css`: 1x Excluded (Saturation: Line 74 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 31800 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.2 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.9 | 24.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.8 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.5 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.9 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 69.5 | 6.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.7 | 66.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 281 | 120 | 0 | `client/src/templates/Introduction/components/block.test.tsx` |
| cleanup | 108 | 56 | 0 | `client/src/templates/Challenges/classic/show.tsx` |
| guards | 2259 | 427 | 4 | `api/src/routes/protected/settings.ts` |
| danger | 954 | 242 | 2 | `api/__mocks__/exam-environment-exam.ts` |
| concurrency | 6618 | 383 | 13 | `api/src/routes/protected/challenge.test.ts` |
| connectivity | 2039 | 749 | 3 | `client/src/components/layouts/variables.css` |
| io | 1558 | 344 | 3 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| crypto | 16 | 16 | 0 | `tools/client-plugins/gatsby-source-challenges/create-challenge-nodes.js` |
| ipc | 95 | 43 | 0 | `packages/challenge-builder/src/worker-executor.test.js` |
| time | 286 | 83 | 0 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| serialization | 104 | 46 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| regex | 173 | 84 | 0 | `e2e/donate-page-default.spec.ts` |
| events | 658 | 157 | 1 | `api/src/routes/protected/challenge.ts` |
| tests | 6949 | 300 | 14 | `api/src/routes/protected/challenge.test.ts` |
| docs | 503 | 170 | 1 | `api/src/exam-environment/routes/exam-environment.test.ts` |
| debt | 651 | 212 | 1 | `.github/workflows/deploy-client.yml` |
| mutation | 18410 | 1002 | 37 | `client/src/assets/icons/top-contributor-badge-emblem.tsx` |
| dead_code | 128 | 61 | 0 | `client/src/templates/Introduction/super-block-intro.test.tsx` |
| credential | 22 | 13 | 0 | `api/src/routes/protected/settings.test.ts` |
| threat | 9 | 3 | 0 | `api/src/routes/protected/challenge.test.ts` |
| ml_ai | 87 | 43 | 0 | `api/src/exam-environment/routes/exam-environment.ts` |
| ui | 4400 | 364 | 10 | `client/src/client-only-routes/show-certification.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `client/src/assets/icons/top-contributor-badge-emblem.tsx` (Hits: 80)
- `client/src/assets/icons/supporter-badge-emblem.tsx` (Hits: 74)
- `client/src/components/formHelpers/form-validators.test.ts` (Hits: 48)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **prop-types.ts** (`client/src/redux/prop-types.ts`) — 92 inbound connections
2. **index.ts** (`client/src/components/helpers/index.ts`) — 66 inbound connections
3. **selectors.js** (`client/src/redux/selectors.js`) — 58 inbound connections
4. **env.ts** (`api/src/utils/env.ts`) — 48 inbound connections
5. **actions.js** (`client/src/templates/Challenges/redux/actions.js`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **schemas.ts** (`api/src/schemas.ts`) — 47 outbound dependencies
2. **show.tsx** (`client/src/templates/Challenges/classic/show.tsx`) — 46 outbound dependencies
3. **default.tsx** (`client/src/components/layouts/default.tsx`) — 39 outbound dependencies
4. **show.tsx** (`client/src/templates/Challenges/codeally/show.tsx`) — 36 outbound dependencies
5. **show.tsx** (`client/src/templates/Challenges/generic/show.tsx`) — 35 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Scene` **(Compute Cores)** (@ `client/src/templates/Challenges/components/scene/scene.tsx`) -> Impact: **78.6** | LOC: 413
- `createLanguageBlock` **(Many-Argument Workhorses)** (@ `tools/challenge-helper-scripts/create-language-block.ts`) -> Impact: **68.5** | LOC: 73
- `postExamGeneratedExamHandler` **(Many-Argument Workhorses)** (@ `api/src/exam-environment/routes/exam-environment.ts`) -> Impact: **66.8** | LOC: 336
  * *Intent:* /** * Generates an exam for the user. * * Requires token to be validated and TODO: live longer than the exam attempt. */
- `generateExam` **(Compute Cores)** (@ `api/src/exam-environment/utils/exam-environment.ts`) -> Impact: **66.6** | LOC: 314
  * *Intent:* /** * Generates an exam for the user, based on the exam configuration. */
- `render` **(I/O & Config Routines)** (@ `client/src/templates/Introduction/components/block.tsx`) -> Impact: **61.1** | LOC: 462
- `transformer` **(Many-Argument Workhorses)** (@ `tools/challenge-parser/parser/plugins/add-video-question.js`) -> Impact: **58.6** | LOC: 132
- `handleDownloadLink` **(Compute Cores)** (@ `client/src/templates/Challenges/exam-download/show.tsx`) -> Impact: **51.3** | LOC: 57
- `sourceChallengesSourceNodes` **(Defensive Guards)** (@ `tools/client-plugins/gatsby-source-challenges/gatsby-node.js`) -> Impact: **49.0** | LOC: 217
- `Hotkeys` **(Compute Cores)** (@ `client/src/templates/Challenges/components/hotkeys.tsx`) -> Impact: **47.8** | LOC: 136
- `SearchBar` **(Defensive Guards)** (@ `client/src/components/search/searchBar/search-bar.tsx`) -> Impact: **46.2** | LOC: 161

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `e2e` | 122 | 15810.64 | 29.83% | 0.87% |
| `api/src/routes/protected` | 11 | 6717.7 | 14.66% | 8.05% |
| `__monolith__` | 10 | 5094.12 | 0.0% | 0.0% |
| `client/src/templates/Challenges/components` | 65 | 2198.88 | 10.22% | 0.52% |
| `api/src/plugins` | 28 | 1548.98 | 7.72% | 4.43% |
| `api/src/routes/public` | 21 | 1524.53 | 4.22% | 2.48% |
| `api/src/exam-environment/routes` | 2 | 1418.86 | 6.77% | 5.34% |
| `api/src/exam-environment/utils` | 3 | 1286.2 | 6.35% | 3.61% |
| `client/src/templates/Challenges/classic` | 17 | 1033.74 | 14.86% | 4.64% |
| `client/src/templates/Challenges/redux` | 12 | 1008.04 | 14.46% | 3.06% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/node.js-tests.yml` -> **99.9999%** Exposure
- `api/src/utils/create-user.ts` -> **99.956%** Exposure
- `api/src/utils/error-formatting.ts` -> **99.9498%** Exposure
- `client/gatsby-browser.tsx` -> **99.593%** Exposure
- `api/src/utils/exam-schemas.ts` -> **98.1564%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/challenge-builder/src/worker-executor.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-fill-in-the-blank.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-hooks.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-quizzes.js` -> **100.0%** Exposure
- `tools/challenge-parser/parser/plugins/add-seed.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `client/src/templates/Introduction/super-block-intro.test.tsx` -> **12** Orphaned Functions | **4** Duplicates
- `.github/workflows/node.js-tests.yml` -> **0** Orphaned Functions | **11** Duplicates
- `client/src/components/Intro/intro.test.tsx` -> **2** Orphaned Functions | **4** Duplicates
- `api/src/routes/protected/challenge.ts` -> **0** Orphaned Functions | **5** Duplicates
- `api/src/utils/exam-schemas.ts` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2526` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/settings.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.311)
- **Top Global Matches:** file_cluster_10: 5.311, file_cluster_2: 7.304, file_cluster_13: 7.417
- **Magnitude:** 4720.59 | **LOC:** 1598 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (36.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.1%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 284`, `args: 109`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 5`, `planned_debt: 2`
* *Architecture:* `io: 47`, `concurrency: 201`, `import: 7`
* *Defense:* `safety: 63`, `doc: 3`, `test: 284`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` vitest.utils.js, redirect-with-message.js, create-user.js, env.js, auth-helpers.js, settings.js, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/routes/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.914)
- **Top Global Matches:** file_cluster_12: 6.914, file_cluster_7: 7.753, file_cluster_10: 7.953
- **Magnitude:** 1090.72 | **LOC:** 1470 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.3%), Mutation Surface (formerly State Flux) (36.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 70 instances
* *Concurrency (weighted view):* 532
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 249`, `args: 77`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 182`, `import: 12`
* *Defense:* `safety: 7`, `doc: 27`, `test: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` exam-environment-exam.js, vitest.utils.js, env.js, exam-environment-exam-attempt.js, index.js, exam-environment.js, type-provider-typebox, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/utils/exam-environment.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_12: 6.43, file_cluster_7: 7.049, file_cluster_10: 7.623
- **Magnitude:** 1000.64 | **LOC:** 544 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (63.9%), Guard Balance (formerly Safety Score) (47.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.3%), Mutation Surface (formerly State Flux) (11.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 99`, `args: 66`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`
* *Architecture:* `concurrency: 16`, `import: 8`
* *Defense:* `safety: 5`, `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` exam-environment-exam.js, vitest.utils.js, index.js, exam-environment.js, type-provider-typebox, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/lower-jaw.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.567)
- **Top Global Matches:** file_cluster_10: 4.567, file_cluster_2: 6.045, file_cluster_13: 6.568
- **Magnitude:** 664.07 | **LOC:** 251 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (44.4%), Mutation Surface (formerly State Flux) (33.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 76`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `concurrency: 71`, `import: 3`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` editor, logout, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/header.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.531)
- **Top Global Matches:** file_cluster_10: 4.531, file_cluster_2: 6.625, file_cluster_13: 6.847
- **Magnitude:** 643.67 | **LOC:** 305 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (80.4%), Guard Balance (formerly Safety Score) (43.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 91
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 86`, `args: 20`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 2`
* *Architecture:* `io: 3`, `concurrency: 76`, `import: 5`
* *Defense:* `safety: 3`, `test: 58`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` links.json, translations.json, i18n, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/quiz-challenge.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.109)
- **Top Global Matches:** file_cluster_10: 5.109, file_cluster_2: 6.93, file_cluster_13: 7.267
- **Magnitude:** 602.76 | **LOC:** 335 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.4%), Guard Balance (formerly Safety Score) (42.5%), Mutation Surface (formerly State Flux) (36.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 152
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 101`, `args: 15`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `io: 11`, `concurrency: 92`, `import: 4`
* *Defense:* `test: 50`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` url, test, fs, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/completion-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.753)
- **Top Global Matches:** file_cluster_10: 4.753, file_cluster_2: 7.175, file_cluster_13: 7.331
- **Magnitude:** 567.34 | **LOC:** 196 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Guard Balance (formerly Safety Score) (42.4%), Mutation Surface (formerly State Flux) (12.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 71`, `args: 18`, `func_start: 14`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`
* *Architecture:* `io: 2`, `concurrency: 61`, `import: 5`
* *Defense:* `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, request, url, test, node:child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/email-subscription.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.184)
- **Top Global Matches:** file_cluster_10: 5.184, file_cluster_13: 6.396, file_cluster_2: 6.753
- **Magnitude:** 513.92 | **LOC:** 283 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 41`, `args: 15`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 2`
* *Architecture:* `concurrency: 29`, `import: 5`
* *Defense:* `doc: 1`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` vitest.utils.js, create-user.js, env.js, client, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/classic/editor.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.55)
- **Top Global Matches:** file_cluster_10: 6.55, file_cluster_15: 7.042, file_cluster_11: 8.077
- **Magnitude:** 461.88 | **LOC:** 1462 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **34**; blast radius 0.568; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.9%), Guard Balance (formerly Safety Score) (54.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.3%), Concurrency Surface (formerly Concurrency) (30.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Editor` **(I/O & Config Routines)** (Impact: 18.1)
  * `createDescription` **(Compute Cores)** (Impact: 15.7)
  * `onChange` **(Defensive Guards)** (Impact: 14.2)
  * `editorDidMount` **(Compute Cores)** (Impact: 9.8)
  * `updateEditableRegion` **(Defensive Guards)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 180`, `args: 106`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 5`, `state_mutation: 71`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 3`, `import: 35`
* *Defense:* `safety: 42`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.568
  * `Choke Point (Betweenness):` 0.000208 | `Ripple Effect (Closeness):` 0.005347
  * `Imports (Out-Degree: 18):` env.json, green-pass, helpers, actions, prop-types, selectors, types, curriculum-layout...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `api/src/routes/protected/challenge.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.273)
- **Top Global Matches:** file_cluster_10: 7.273, file_cluster_12: 7.652, file_cluster_15: 9.26
- **Magnitude:** 400.42 | **LOC:** 2556 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (42.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createMSUsernameRecord` **(Parameter Forwarders)** (Impact: 1.9)
  * `submitExam` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 338
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 378`, `args: 155`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 12`, `planned_debt: 4`
* *Architecture:* `io: 33`, `concurrency: 268`, `import: 13`
* *Defense:* `safety: 34`, `doc: 6`, `test: 383`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` exam.js, vitest.utils.js, get-session-user.js, exam-types.js, challenge-helpers.js, type-provider-typebox, challenge-types, client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/portfolio.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.023)
- **Top Global Matches:** file_cluster_10: 5.023, file_cluster_2: 7.079, file_cluster_13: 7.357
- **Magnitude:** 395.68 | **LOC:** 196 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.416; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.3%), Guard Balance (formerly Safety Score) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.8%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.47)
- **Top Global Matches:** file_cluster_10: 5.47, file_cluster_11: 8.121, file_cluster_12: 8.602
- **Magnitude:** 390.72 | **LOC:** 1704 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.0%), Guard Balance (formerly Safety Score) (43.3%), Complexity Load (formerly Cognitive Load) (23.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `json` **(Callbacks & Closures)** (Impact: 1.2)
  * `json` **(Callbacks & Closures)** (Impact: 1.2)
  * `json` **(Callbacks & Closures)** (Impact: 1.2)
  * `json` **(Callbacks & Closures)** (Impact: 1.2)
  * `json` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 320
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 307`, `args: 126`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 23`, `planned_debt: 7`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 36`, `concurrency: 240`, `import: 11`
* *Defense:* `safety: 15`, `doc: 3`, `test: 226`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` exam-environment-exam.js, vitest.utils.js, create-user.js, env.js, user.js, client, jsonwebtoken, lodash-es...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/protected/certificate.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.907)
- **Top Global Matches:** file_cluster_10: 3.907, file_cluster_2: 5.187, file_cluster_13: 6.128
- **Magnitude:** 378.21 | **LOC:** 477 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (45.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.5%), Mutation Surface (formerly State Flux) (11.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 63`, `args: 22`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `planned_debt: 4`
* *Architecture:* `concurrency: 34`, `import: 5`
* *Defense:* `safety: 3`, `doc: 3`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` vitest.utils.js, get-challenges.js, certificate.js, certification-settings, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/settings.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.715)
- **Top Global Matches:** file_cluster_10: 4.715, file_cluster_2: 5.894, file_cluster_13: 6.124
- **Magnitude:** 365.99 | **LOC:** 357 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (58.7%), Guard Balance (formerly Safety Score) (50.4%), Mutation Surface (formerly State Flux) (26.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 70`, `args: 13`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 7`
* *Architecture:* `io: 2`, `concurrency: 59`, `import: 5`
* *Defense:* `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` translations.json, alerts, certification-settings, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/src/templates/Challenges/components/pinyin-to-hanzi-input.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.935)
- **Top Global Matches:** file_cluster_10: 5.935, file_cluster_0: 6.224, file_cluster_13: 7.612
- **Magnitude:** 357.48 | **LOC:** 365 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (40.4%), Complexity Load (formerly Cognitive Load) (22.2%), Mutation Surface (formerly State Flux) (10.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 55`, `args: 21`, `func_start: 8`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 23`, `import: 5`
* *Defense:* `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pinyin-to-hanzi-input, react, user-event, react, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/exam-environment/routes/exam-environment.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.941)
- **Top Global Matches:** file_cluster_4: 6.941, file_cluster_6: 9.416, file_cluster_9: 12.01
- **Magnitude:** 328.14 | **LOC:** 1154 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.506; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (83.1%), Guard Balance (formerly Safety Score) (51.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.0%), Mutation Surface (formerly State Flux) (37.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postExamGeneratedExamHandler` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* /** * Generates an exam for the user. * * Requires token to be validated and TODO: live longer than ...
  * `postExamAttemptHandler` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /** * Handles updates to an exam attempt. * * Requires token to be validated. * * TODO: Consider val...
  * `getExams` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * Get all the public information about all exams. */
  * `getExamAttemptsHandler` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* /** * Gets all exam attempts owned by authz user. * * If an attempt is completed, the result is incl...
  * `getExamChallenge` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* /** * Gets all the relations for a given challenge and exam(s). */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 173`, `args: 20`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 7`
* *Architecture:* `api: 7`, `concurrency: 33`, `import: 11`
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.506
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.007443
  * `Imports (Out-Degree: 6):` env.js, index.js, validation.js, index.js, errors.js, exam-environment.js, type-provider-typebox, client...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `e2e/username-change.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.827)
- **Top Global Matches:** file_cluster_10: 4.827, file_cluster_2: 6.832, file_cluster_13: 7.201
- **Magnitude:** 318.62 | **LOC:** 183 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.416; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (58.7%), Guard Balance (formerly Safety Score) (50.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Concurrency (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 47`, `args: 13`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 11`
* *Architecture:* `io: 1`, `concurrency: 42`, `import: 3`
* *Defense:* `safety: 2`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `api/src/routes/public/user.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.927)
- **Top Global Matches:** file_cluster_10: 3.927, file_cluster_2: 5.4, file_cluster_13: 6.136
- **Magnitude:** 304.59 | **LOC:** 648 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.0%), Guard Balance (formerly Safety Score) (41.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.4%), Mutation Surface (formerly State Flux) (9.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 69`, `args: 36`, `func_start: 12`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 8`
* *Architecture:* `io: 11`, `concurrency: 35`, `import: 7`
* *Defense:* `safety: 21`, `test: 70`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` vitest.utils.js, create-user.js, user.js, client, lodash-es, mongodb, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/independent-lower-jaw.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.597)
- **Top Global Matches:** file_cluster_10: 4.597, file_cluster_2: 6.645, file_cluster_13: 6.848
- **Magnitude:** 297.41 | **LOC:** 158 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (42.9%), Mutation Surface (formerly State Flux) (37.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 134
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 54`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `concurrency: 49`, `import: 2`
* *Defense:* `safety: 2`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` editor, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `e2e/challenge-reset-modal.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.814)
- **Top Global Matches:** file_cluster_10: 4.814, file_cluster_2: 7.829, file_cluster_13: 8.07
- **Magnitude:** 295.64 | **LOC:** 344 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.416; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (49.1%), Mutation Surface (formerly State Flux) (32.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectToRenderResetModal` **(Callbacks & Closures)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 277
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 107`, `args: 18`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 9`
* *Architecture:* `io: 2`, `concurrency: 92`, `import: 5`
* *Defense:* `safety: 1`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` translations.json, alerts, editor, test, child_process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/challenge-builder/src/transformers.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.208)
- **Top Global Matches:** file_cluster_4: 8.208, file_cluster_10: 10.162, file_cluster_15: 10.573
- **Magnitude:** 280.42 | **LOC:** 418 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.988; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Mutation Surface (formerly State Flux) (83.8%), Guard Balance (formerly Safety Score) (50.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `embedFilesInHtml` **(Defensive Guards)** (Impact: 40.8)
    * *Intent:* // This does the final transformations of the files needed to embed them into // HTML.
  * `embedStylesAndScript` **(Defensive Guards)** (Impact: 25.5)
  * `transformScript` **(Compute Cores)** (Impact: 15.7)
  * `getBabelOptions` **(Compute Cores)** (Impact: 7.7)
  * `embedScript` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 94
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 97`, `args: 47`, `func_start: 28`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 13`, `planned_debt: 3`
* *Architecture:* `api: 5`, `concurrency: 39`, `import: 10`
* *Defense:* `safety: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001623
  * `Imports (Out-Degree: 2):` typescript-worker-handler, worker-executor, preset-env, preset-react, standalone, package.json, loop-protect, polyvinyl...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `api/src/exam-environment/utils/exam-environment.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.687)
- **Top Global Matches:** file_cluster_4: 6.687, file_cluster_9: 11.119, file_cluster_15: 11.366
- **Magnitude:** 280.36 | **LOC:** 969 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.812; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (73.9%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (41.1%), Concurrency Surface (formerly Concurrency) (16.9%)
- **Documentation Coverage:** 8.6957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateExam` **(Compute Cores)** (Impact: 66.6)
    * *Intent:* /** * Generates an exam for the user, based on the exam configuration. */
  * `constructEnvExamAttempt` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* /* eslint-enable jsdoc/require-description-complete-sentence */ /** * From an exam attempt, construc...
  * `calculateScore` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* /** * Calculates the number of correct questions over the number of the total questions given for an...
  * `validateAttempt` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /** * Ensures all questions and answers in the attempt are from the generated exam. */
  * `checkAttemptAgainstGeneratedExam` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /** * Checks all question sets and questions in the generated exam are in the attempt. * * TODO: Con...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 168`, `args: 87`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `planned_debt: 6`
* *Architecture:* `api: 11`, `concurrency: 4`, `import: 8`
* *Defense:* `safety: 5`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.812
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.006494
  * `Imports (Out-Degree: 4):` index.js, exam-environment-exam-attempt.js, index.js, errors.js, type-provider-typebox, client, fastify, lodash-es
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `api/src/routes/protected/challenge.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.007)
- **Top Global Matches:** file_cluster_15: 7.007, file_cluster_10: 7.655, file_cluster_16: 7.896
- **Magnitude:** 269.72 | **LOC:** 1268 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.496; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (92.2%), Guard Balance (formerly Safety Score) (47.9%), Debt Markers (formerly Tech Debt) (41.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.0%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `postCoderoadChallengeCompleted` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `postDailyCodingChallengeCompleted` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `postModernChallengeCompleted` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `postSaveChallenge` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `errorHandler` **(Many-Argument Workhorses)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 198`, `args: 39`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`, `planned_debt: 6`, `duplicate_logic: 5`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 47`, `import: 18`
* *Defense:* `safety: 39`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.496
  * `Choke Point (Betweenness):` 0.000147 | `Ripple Effect (Closeness):` 0.005208
  * `Imports (Out-Degree: 11):` schemas.js, common-challenge-functions.js, env.js, error-formatting.js, exam-schemas.js, exam.js, get-challenges.js, index.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `e2e/profile.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.136)
- **Top Global Matches:** file_cluster_10: 4.136, file_cluster_2: 5.981, file_cluster_13: 6.113
- **Magnitude:** 268.41 | **LOC:** 209 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.416; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%), Complexity Load (formerly Cognitive Load) (26.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 37`, `args: 13`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 1`, `concurrency: 30`, `import: 2`
* *Defense:* `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` translations.json, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `client/src/components/OfflineWarning/offline-warning.test.tsx` (TYPESCRIPT) | Magnitude: 16.24 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 20, core_var_decl: 13, design_camel_case: 13
- `client/src/templates/Challenges/components/pinyin-tone-input.test.tsx` (TYPESCRIPT) | Magnitude: 246.15 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 216, core_var_decl: 73, test: 59, structural_boundaries: 54
- `client/src/templates/Challenges/fill-in-the-blank/show.tsx` (TYPESCRIPT) | Magnitude: 50.22 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 81, core_var_decl: 69, design_camel_case: 41
- `client/src/components/profile/components/heat-map.tsx` (TYPESCRIPT) | Magnitude: 64.18 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 40, core_var_decl: 37, ui_framework: 22
- `client/src/components/helpers/form/block-save-button.tsx` (TYPESCRIPT) | Magnitude: 12.82 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, branch: 5, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `client/src/redux/failed-updates-epic.js` (JAVASCRIPT) | Magnitude: 54.28 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 33, args: 16, core_var_decl: 14
- `client/src/templates/Challenges/exam/show.tsx` (TYPESCRIPT) | Magnitude: 100.92 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 455, structural_boundaries: 96, core_var_decl: 94, ui_framework: 66
- `api/src/routes/public/user.ts` (TYPESCRIPT) | Magnitude: 42.2 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 42, branch: 26, core_var_decl: 17
- `client/src/components/Donation/security-lock-icon.tsx` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, import: 3, decorators: 2
- `tools/challenge-helper-scripts/delete-task.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 16, import: 7, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `e2e/update-about-me.spec.ts` (TYPESCRIPT) | Magnitude: 189.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 30, concurrency: 27, state_mutation: 11
- `client/src/components/Header/components/universal-nav.css` (CSS) | Magnitude: 1.4 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 220, class_start: 106, ui_framework: 21, doc: 19
- `client/src/components/helpers/use-claimable-certs-notification.tsx` (TYPESCRIPT) | Magnitude: 9.88 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 11, import: 5, ui_framework: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tools/challenge-helper-scripts/helpers/get-input-type.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, branch: 3, concurrency: 3
- `tools/challenge-helper-scripts/insert-task.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 18, core_var_decl: 13, design_camel_case: 9
- `api/src/schemas/user/delete-user-token.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, import: 2, branch: 1
- `packages/eslint-config/base.js` (JAVASCRIPT) | Magnitude: 23.64 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 35, import: 16, decorators: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/shared/src/config/challenge-types.ts` (TYPESCRIPT) | Magnitude: 15.34 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 124, core_var_decl: 43, design_camel_case: 26, design_snake_case: 17
- `api/src/routes/public/sentry.ts` (TYPESCRIPT) | Magnitude: 6.7 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, import: 4, args: 2
- `tools/challenge-parser/parser/plugins/utils/get-paragraph-content.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, structural_boundaries: 1, args: 1, func_start: 1
- `client/utils/gatsby/challenge-page-creator.js` (JAVASCRIPT) | Magnitude: 32.02 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 118, core_var_decl: 22, structural_boundaries: 12, args: 12
- `tools/challenge-parser/parser/plugins/utils/before-heading.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, core_var_decl: 3, structural_boundaries: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `client/src/components/helpers/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, import: 8, branch: 6
- `api/src/schemas.ts` (TYPESCRIPT) | Magnitude: 63.06 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 47, api: 47, import: 47, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `api/src/schemas/sentry/event.ts` (TYPESCRIPT) | Magnitude: 16.24 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, api: 1, decorators: 1
- `.github/workflows/github-labeler.yaml` (YAML) | Magnitude: 16.38 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, branch: 2, structural_boundaries: 2, args: 2
- `api/src/exam-environment/schemas/token-meta.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, import: 2, api: 1
- `api/tools/exam-environment/test/index.ts` (TYPESCRIPT) | Magnitude: 0.01 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 8, debug_prints: 6, concurrency: 5
- `client/src/assets/icons/green-not-completed.tsx` (TYPESCRIPT) | Magnitude: 1.43 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, core_var_decl: 13, structural_boundaries: 8, design_snake_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/shared/src/utils/shuffle-array.ts` (TYPESCRIPT) | Magnitude: 7.66 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 6, core_var_decl: 4, structural_boundaries: 3, scientific: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tools/challenge-parser/parser/plugins/add-solution.test.js` (JAVASCRIPT) | Magnitude: 0.05 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, test: 32, structural_boundaries: 29, args: 18
- `packages/challenge-builder/src/build.test.ts` (TYPESCRIPT) | Magnitude: 15.6 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 10, test: 7, args: 5
- `e2e/iframe-script.spec.ts` (TYPESCRIPT) | Magnitude: 63.64 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, concurrency: 7, test: 4
- `client/src/templates/Challenges/components/tool-panel.css` (CSS) | Magnitude: 0.14 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, class_start: 9, ui_framework: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `client/src/templates/Introduction/components/super-block-accordion.tsx` (TYPESCRIPT) | Magnitude: 81.86 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 338, structural_boundaries: 114, core_var_decl: 90, design_camel_case: 65
- `.github/workflows/deploy-client.yml` (YAML) | Magnitude: 76.68 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 320, globals: 69, debug_prints: 49, branch: 35

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/node.js-tests.yml` -> Churn: **69.54%** | Cog Load: 6.5024% | Debt: 99.9999%
- `tools/challenge-helper-scripts/create-language-block.ts` -> Churn: **51.69%** | Cog Load: 92.8881% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `api/src/exam-environment/routes/exam-environment.test.ts` -> **Shaun Hamilton** (100.0% isolated ownership) | Magnitude: 1090.72
- `e2e/lower-jaw.spec.ts` -> **Ahmad Abdolsaheb** (100.0% isolated ownership) | Magnitude: 664.07
- `e2e/completion-modal.spec.ts` -> **Oliver Eyton-Williams** (100.0% isolated ownership) | Magnitude: 567.34
- `client/src/templates/Challenges/components/pinyin-to-hanzi-input.test.tsx` -> **Diem-Trang Pham** (100.0% isolated ownership) | Magnitude: 357.48
- `api/src/exam-environment/utils/exam-environment.ts` -> **Shaun Hamilton** (100.0% isolated ownership) | Magnitude: 280.36

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `api/vitest.utils.ts` -> **Severity: 0.101** (Bridge: 0.0013 * Flux: 77.6271%)
- `tools/challenge-parser/parser/index.js` -> **Severity: 0.023** (Bridge: 0.0003 * Flux: 88.5385%)
- `client/src/templates/Challenges/classic/editor.tsx` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 94.9143%)
- `api/src/app.ts` -> **Severity: 0.018** (Bridge: 0.0014 * Flux: 13.2485%)
- `client/src/templates/Challenges/redux/selectors.js` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 61.3282%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `client/src/redux/types.ts` -> **Severity: 3.263** (Embedded: 0.0637 * Error Risk: 51.2046%)
- `client/src/components/Flash/redux/flash-messages.ts` -> **Severity: 2.545** (Embedded: 0.0504 * Error Risk: 50.5%)
- `client/src/redux/selectors.js` -> **Severity: 2.272** (Embedded: 0.0565 * Error Risk: 40.2219%)
- `client/src/components/helpers/avatar-renderer.tsx` -> **Severity: 2.044** (Embedded: 0.0349 * Error Risk: 58.4884%)
- `client/src/components/helpers/button-link.tsx` -> **Severity: 2.026** (Embedded: 0.0351 * Error Risk: 57.8024%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `api/src/utils/env.ts` -> **Severity: 1328.3** (Blast Radius: 13.283 * Doc Risk: 100.0%)
- `client/src/redux/selectors.js` -> **Severity: 672.5** (Blast Radius: 6.725 * Doc Risk: 100.0%)
- `tools/challenge-helper-scripts/helpers/get-project-info.ts` -> **Severity: 575.1** (Blast Radius: 5.751 * Doc Risk: 100.0%)
- `e2e/utils/editor.ts` -> **Severity: 483.7** (Blast Radius: 4.837 * Doc Risk: 100.0%)
- `client/src/templates/Challenges/redux/selectors.js` -> **Severity: 431.2** (Blast Radius: 4.312 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 321 literal sites + 1 sites through wrappers = 322
- **`panics_and_aborts`:** 286 literal sites + 10 sites through wrappers = 296

- `withTrace` (function, panics_and_aborts, primitive): 5 call sites in 5 files -- `tools/challenge-helper-scripts/helpers/utils.ts`
- `buildChallengeData` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `client/src/templates/Challenges/redux/execute-challenge-saga.js`
- `init` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/challenge-builder/src/worker-executor.test.js`
- `reportClientSideError` (function, debug_prints, primitive): 1 call sites in 1 files -- `client/src/utils/report-error.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5947 call pairs -- scoped 19.5%, unique 0.0%, ambiguous 6.4%, external 74.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 4711 | 17.5% | 0.0% | 7.2% | 75.2% |
| javascript | 1233 | 27.3% | 0.0% | 3.3% | 69.3% |
| shell | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
