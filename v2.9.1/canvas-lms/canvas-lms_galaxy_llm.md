# ARCHITECTURAL_BRIEF: canvas-lms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/instructure/canvas-lms.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 20349 analyzed artifact(s), 2476076 LOC.
- **Load-bearing artifact:** `ui/shared/test-utils/fakeENV.js` -- 510 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ui/features/gradebook/react/default_gradebook/Gradebook.tsx` -- pulls in 97 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `app/services/rubric_llm_service.rb` at magnitude 9048.03 (structural weight, not risk).
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
| Total Artifacts | 22519 |
| Analyzed Artifacts (Scanned) | 20349 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2170 |
| Total LOC | 2476076 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 90.4% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8888 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0582 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2893 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2609 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 6777 | 1104923 | 33.3% |
| TYPESCRIPT | 5341 | 635724 | 26.2% |
| JAVASCRIPT | 4419 | 544678 | 21.7% |
| HTML | 902 | 44133 | 4.4% |
| JSON | 866 | 87788 | 4.3% |
| XML | 676 | 385 | 3.3% |
| PLAINTEXT | 527 | 3 | 2.6% |
| CSS | 417 | 44900 | 2.0% |
| MARKDOWN | 166 | 0 | 0.8% |
| YAML | 129 | 10389 | 0.6% |
| SHELL | 90 | 1978 | 0.4% |
| CSV | 26 | 421 | 0.1% |
| LUA | 7 | 93 | 0.0% |
| DOCKERFILE | 5 | 136 | 0.0% |
| GROOVY | 1 | 525 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.64`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.64; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 23%, Data / Markup / Trivial 22%, Callbacks & Closures Files 18%, Large Core Modules 7%, Large Core Modules (2) 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19432 | 95.5% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 690 | 3.4% |
| Static: Minified & Vendor Opaque Mass | 224 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2170*

**Composition by Extension & Reason:**
- `.png`: 630x Excluded (Explicitly Denied Extension: '.png')
- `.handlebars`: 230x Excluded (Unsupported Extension: '.handlebars')
- `.js`: 56x Excluded (Saturation: Line 21 exceeds 500 chars), 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 44x Excluded (Saturation: Line 22 exceeds 500 chars)
- `no_extension`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.package-translations'), 2x Unsupported Format (.undeterminable)
- `.gif`: 101x Excluded (Explicitly Denied Extension: '.gif')
- `.xss`: 94x Excluded (Unsupported Extension: '.xss')
- `.zip`: 92x Excluded (Explicitly Denied Extension: '.zip')
- `.json`: 43x Excluded (Massive Static Asset Blob: 2994 LOC), 9x Excluded: Neighborhood Micro-Mass Limit Exceeded, 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Monolithic Amalgamation: 41511 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 43287 LOC exceeds safe regex boundaries)
- `.lock`: 54x Excluded (Unsupported Extension: '.lock')
- `.rb`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 47 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1423 LOC)
- `.ts`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.sh`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 451, Signals: 0), 1x Excluded (Machine-Generated Source Code Signature: 96 LOC)
- `.example`: 35x Excluded (Unsupported Extension: '.example')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.6 | 7.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 34.5 | 35.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 95.5 | 4.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3943 | 1507 | 0 | `ui/features/assignment_edit/react/hooks/__tests__/usePeerReviewSettings.test.ts` |
| cleanup | 1337 | 1002 | 0 | `ui/features/gradebook/react/default_gradebook/GradebookGrid/editors/AssignmentCellEditor/__tests__/AssignmentCellEditor.test.jsx` |
| guards | 44987 | 7307 | 6 | `doc/api/fulldoc/html/js/swagger-ui.js` |
| danger | 19114 | 5009 | 2 | `spec/controllers/application_controller_spec.rb` |
| concurrency | 38866 | 3314 | 3 | `ui/features/section/react/__tests__/CrosslistForm.test.tsx` |
| connectivity | 61490 | 8500 | 6 | `config/routes.rb` |
| io | 74086 | 6175 | 6 | `spec/models/assignment_spec.rb` |
| crypto | 1 | 1 | 0 | `ui/shared/encrypted-forage/index.js` |
| ipc | 337 | 115 | 0 | `packages/canvas-rce/src/enhance-user-content/__tests__/instructure_helper.test.js` |
| time | 3831 | 1326 | 0 | `packages/jqueryui/datepicker.js` |
| serialization | 1816 | 650 | 0 | `spec/lib/cc/basic_lti_links_spec.rb` |
| regex | 2833 | 1108 | 0 | `lib/swagger_yard/canvas_adapter.rb` |
| events | 9755 | 2689 | 1 | `ui/features/quizzes/jquery/quizzes.jsx` |
| tests | 339772 | 6786 | 41 | `spec/models/assignment_spec.rb` |
| docs | 6467 | 1244 | 0 | `packages/react-dnd-test-backend/index.js` |
| debt | 7585 | 1806 | 0 | `spec/models/accessibility/rules/list_structure_rule_spec.rb` |
| mutation | 505900 | 15599 | 56 | `spec/apis/v1/assignments_api_spec.rb` |
| dead_code | 11476 | 4539 | 2 | `app/models/user.rb` |
| credential | 225 | 126 | 0 | `spec/apis/v1/submissions_api_spec.rb` |
| threat | 7710 | 1741 | 0 | `ui/shared/assignments/backbone/models/Assignment.js` |
| ml_ai | 563 | 215 | 0 | `gems/plugins/account_reports/spec_canvas/grade_reports_spec.rb` |
| ui | 79322 | 6710 | 12 | `ui/features/discussion_topics_post/react/containers/DiscussionThreadContainer/DiscussionThreadContainer.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spec/models/assignment_spec.rb` (Hits: 1061)
- `spec/models/submission_spec.rb` (Hits: 996)
- `spec/models/course_spec.rb` (Hits: 724)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **fakeENV.js** (`ui/shared/test-utils/fakeENV.js`) — 510 inbound connections
2. **graphql_spec_helper.rb** (`spec/graphql/graphql_spec_helper.rb`) — 193 inbound connections
3. **AlertManager.tsx** (`ui/shared/alerts/react/AlertManager.tsx`) — 125 inbound connections
4. **globalUtils.ts** (`ui/shared/util/globalUtils.ts`) — 111 inbound connections
5. **views_helper.rb** (`spec/views/views_helper.rb`) — 104 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Gradebook.tsx** (`ui/features/gradebook/react/default_gradebook/Gradebook.tsx`) — 97 outbound dependencies
2. **getTranslations.js** (`packages/canvas-rce/src/getTranslations.js`) — 77 outbound dependencies
3. **getTranslations.js** (`packages/canvas-media/src/getTranslations.js`) — 76 outbound dependencies
4. **common.scss** (`app/stylesheets/bundles/common.scss`) — 72 outbound dependencies
5. **speed_grader.tsx** (`ui/features/speed_grader/jquery/speed_grader.tsx`) — 71 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/models/submission_spec.rb`) -> Impact: **1824.4** | LOC: 11541
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/apis/v1/assignments_api_spec.rb`) -> Impact: **1129.4** | LOC: 12102
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/models/user_spec.rb`) -> Impact: **820.0** | LOC: 6241
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/controllers/gradebooks_controller_spec.rb`) -> Impact: **756.1** | LOC: 5051
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/controllers/assignments_controller_spec.rb`) -> Impact: **747.8** | LOC: 3896
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/models/account_spec.rb`) -> Impact: **739.3** | LOC: 4124
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...
- `SlickGrid` **(Many-Argument Workhorses)** (@ `packages/slickgrid/slick.grid.js`) -> Impact: **712.4** | LOC: 1592
  * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // SlickGrid class implementation (available as Slick....
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/controllers/users_controller_spec.rb`) -> Impact: **700.4** | LOC: 4594
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/controllers/courses_controller_spec.rb`) -> Impact: **699.6** | LOC: 6857
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/controllers/application_controller_spec.rb`) -> Impact: **631.6** | LOC: 3691
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/models` | 288 | 54148.8 | 36.99% | 48.92% |
| `spec/models` | 228 | 53753.76 | 14.78% | 0.0% |
| `app/controllers` | 195 | 44338.82 | 43.1% | 54.42% |
| `spec/controllers` | 139 | 36095.02 | 9.67% | 0.0% |
| `spec/apis/v1` | 103 | 32700.46 | 13.58% | 0.0% |
| `lib` | 160 | 18062.48 | 46.21% | 59.83% |
| `spec/lib` | 128 | 15518.82 | 14.32% | 0.0% |
| `lib/api/v1` | 105 | 12533.86 | 43.95% | 51.75% |
| `app/services` | 15 | 10838.69 | 39.53% | 46.07% |
| `config/saml` | 2 | 10000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/slickgrid/slick.editors.js` -> **100.0%** Exposure
- `ui/shared/add-people/react/components/__tests__/add_people.spec.jsx` -> **100.0%** Exposure
- `ui/shared/grading/content-filters/ContentFilterDriver.js` -> **100.0%** Exposure
- `ui/shared/jquery/FakeXHR.js` -> **100.0%** Exposure
- `ui/shared/test-utils/I18nStubber.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/api/fulldoc/html/js/handlebars-1.0.0.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/pendo.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/swagger-ui.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/swagger.js` -> **100.0%** Exposure
- `packages/canvas-media/src/getTranslations.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/models/user.rb` -> **182** Orphaned Functions | **0** Duplicates
- `app/models/abstract_assignment.rb` -> **137** Orphaned Functions | **0** Duplicates
- `app/helpers/application_helper.rb` -> **68** Orphaned Functions | **0** Duplicates
- `app/models/discussion_topic.rb` -> **54** Orphaned Functions | **0** Duplicates
- `app/models/content_migration.rb` -> **50** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `spec/models/pseudonym_spec.rb` -> **100.0%** Exposure
- `spec/selenium/new_login/otp_page_spec.rb` -> **100.0%** Exposure
- `spec/lib/enhanced_cookie_store_spec.rb` -> **99.9995%** Exposure
- `spec/selenium/new_login/sign_in_page_spec.rb` -> **99.9986%** Exposure
- `spec/models/attachments/s3_storage_spec.rb` -> **99.9979%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `92` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `44172` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `app/services/rubric_llm_service.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 9048.03 | **LOC:** 962 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.032; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 47`, `args: 33`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 164`, `planned_debt: 1`
* *Architecture:* `io: 7`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HtmlTextHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/context_modules_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 5162.24 | **LOC:** 1348 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.032; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 432.1)
  * `content_tag_assignment_data` **(Many-Argument Workhorses)** (Impact: 397.6)
  * `items_html` **(Compute Cores)** (Impact: 364.6)
  * `bulk_items_html` **(Compute Cores)** (Impact: 362.1)
  * `module_html` **(Compute Cores)** (Impact: 344.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 682
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 164`, `args: 9`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 270`, `dead_code: 4`, `unreferenced_by_name: 15`
* *Architecture:* `io: 50`
* *Defense:* `safety: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Api::V1::ContextModule, ContextExternalToolsHelper, ContextModulesHelper, HorizonMode, K5Mode, ModuleIndexHelper, ObserverModuleInfo, WebZipExportHelper
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/saml/inc-md-cert-mdq.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/saml/ukfederation.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/submission_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4620.84 | **LOC:** 11564 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 41.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.9%), Guard Balance (formerly Safety Score) (35.3%), Complexity Load (formerly Cognitive Load) (20.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 1824.4)
  * `submission_spec_model` **(Callbacks & Closures)** (Impact: 5.1)
  * `peer_review_assignment` **(Callbacks & Closures)** (Impact: 3.6)
  * `submission_for_some_user` **(I/O & Config Routines)** (Impact: 3.3)
  * `setup_account_for_turnitin` **(I/O & Config Routines)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 524 instances
* *State Mutation (weighted view):* 2583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 881`, `structural_boundaries: 285`, `args: 4`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 1535`, `fragile_debt: 2`
* *Architecture:* `io: 996`, `import: 2`
* *Defense:* `safety: 95`, `test: 3034`, `immutability_locks: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` validates_as_url, attachment, attachments, do
      attachment = attachment_model(filename:, draft, duplicates, eligible, excused...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/assignment_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4560.2 | **LOC:** 14538 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.6%), Guard Balance (formerly Safety Score) (30.9%), Complexity Load (formerly Cognitive Load) (26.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `concurrent_inserts` **(I/O & Config Routines)** (Impact: 336.5)
  * `create_completed_assessment_request` **(Many-Argument Workhorses)** (Impact: 316.0)
  * `generate_comments` **(Many-Argument Workhorses)** (Impact: 213.8)
  * `student_unread_count_counts` **(I/O & Config Routines)** (Impact: 204.5)
  * `assignment` **(I/O & Config Routines)** (Impact: 73.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 596 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 2777
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1144`, `structural_boundaries: 303`, `args: 8`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 9`, `state_mutation: 1585`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1061`, `import: 6`
* *Defense:* `safety: 27`, `test: 4062`, `sync_locks: 1`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` lti2_spec_helper, groups_common, GroupsCommon, Shard, a, admin, an_object_having_attributes, assignment...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/apis/v1/assignments_api_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3957.16 | **LOC:** 12270 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.4%), Guard Balance (formerly Safety Score) (58.8%), Complexity Load (formerly Cognitive Load) (24.5%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 1129.4)
  * `adhoc_override_api_call` **(Many-Argument Workhorses)** (Impact: 8.1)
  * `api_bulk_update` **(Many-Argument Workhorses)** (Impact: 5.5)
  * `mock_and_call_create_api_assignment` **(Many-Argument Workhorses)** (Impact: 5.0)
  * `create_assignment_json` **(I/O & Config Routines)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 486 instances
* *State Mutation (weighted view):* 2489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 171`, `args: 30`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 1`, `state_mutation: 1517`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 623`, `api: 27`, `import: 4`
* *Defense:* `safety: 12`, `test: 2121`, `sync_locks: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` lti2_spec_helper, lti_spec_helper, api_spec_helper, locked_examples, Api, Api::V1::Assignment, Api::V1::Submission, LtiSpecHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/course.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3950.38 | **LOC:** 5058 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Connectivity (formerly Api Exposure) (90.6%), Guard Balance (formerly Safety Score) (86.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uncached_tabs_available` **(Many-Argument Workhorses)** (Impact: 172.5)
    * *Intent:* # make sure t() is called before we switch to the secondary, in case we update the user's selected l...
  * `enroll_user` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 93.8)
  * `generate_grade_publishing_csv_output` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `update_account_associations` **(Many-Argument Workhorses)** (Impact: 43.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 495 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1024`, `structural_boundaries: 588`, `args: 144`, `func_start: 353`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 624`, `dead_code: 6`, `planned_debt: 2`
* *Architecture:* `io: 316`, `api: 171`
* *Defense:* `safety: 82`, `test: 3`, `sync_locks: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Accessibility::Scannable, ContentLicenses, ContentNotices, Context, CopiedAssets, Courses::ExportWarnings, Courses::ItemVisibilityHelper, Csp::CourseHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/slickgrid/slick.grid.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3877.54 | **LOC:** 4192 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Complexity Load (formerly Cognitive Load) (92.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.9305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SlickGrid` **(Many-Argument Workhorses)** (Impact: 712.4)
    * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // S...
  * `setupColumnResize` **(I/O & Config Routines)** (Impact: 80.8)
  * `appendRowHtml` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `handleKeyDown` **(Compute Cores)** (Impact: 54.2)
  * `init` **(I/O & Config Routines)** (Impact: 45.7)
    * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // I...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 466 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 1450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 831`, `structural_boundaries: 661`, `args: 215`, `func_start: 188`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 11`, `state_mutation: 518`, `dead_code: 11`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 9`, `import: 3`
* *Defense:* `safety: 82`, `doc: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` rtlHelper, jquery, normalize-scroll-left
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/application_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3737.8 | **LOC:** 3694 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 21.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.5%), Guard Balance (formerly Safety Score) (93.3%), Complexity Load (formerly Cognitive Load) (93.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tool_dimensions` **(Many-Argument Workhorses)** (Impact: 356.0)
  * `content_tag_redirect` **(Many-Argument Workhorses)** (Impact: 207.1)
  * `js_env` **(Many-Argument Workhorses)** (Impact: 140.2)
    * *Intent:* # Also, please don't name it stuff from JavaScript's Object.prototype # like `hasOwnProperty`, `cons...
  * `get_feed_context` **(Stateful Encapsulated Methods)** (Impact: 65.3)
    * *Intent:* # Used to retrieve the context from a :feed_code parameter. These # :feed_code attributes are keyed ...
  * `safe_domain_file_url` **(Many-Argument Workhorses)** (Impact: 56.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 489 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 886`, `structural_boundaries: 397`, `args: 94`, `func_start: 229`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 563`, `dead_code: 8`, `planned_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `io: 41`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 134`, `doc: 4`, `test: 5`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Api, Api::V1::Course, Api::V1::Group, Api::V1::User, Api::V1::UserProfile, Api::V1::WikiPage, AuthenticationMethods, Canvas::RequestForgeryProtection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/abstract_assignment.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3692.76 | **LOC:** 4798 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.2%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_grade_to_submission` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 52.8)
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
  * `submit_homework` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* %w[comment group_comment attachments require_submission_type_is_valid resource_link_lookup_uuid stud...
  * `grade_student` **(Compute Cores)** (Impact: 47.7)
  * `representatives` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* # for group assignments, returns a single "student" for each # group's submission. the students name...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 478 instances
* *State Mutation (weighted view):* 1551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 602`, `args: 152`, `func_start: 352`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 595`, `dead_code: 4`, `planned_debt: 5`, `unreferenced_by_name: 137`
* *Architecture:* `io: 198`, `import: 2`
* *Defense:* `safety: 73`, `doc: 7`, `test: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ApplicationHelper, Assignments::GraderIdentities, Canvas::DraftStateValidations, ContextModuleItem, CopyAuthorizedLinks, DatesOverridable, DuplicatingObjects, HasContentTags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/course_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3632.32 | **LOC:** 10427 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 23.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.0%), Guard Balance (formerly Safety Score) (31.6%), Complexity Load (formerly Cognitive Load) (29.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_external_tool` **(Many-Argument Workhorses)** (Impact: 281.3)
  * `cached_account_users` **(I/O & Config Routines)** (Impact: 174.0)
  * `setup_DA` **(I/O & Config Routines)** (Impact: 160.5)
  * `default_scheme` **(I/O & Config Routines)** (Impact: 101.6)
  * `calculated_value` **(I/O & Config Routines)** (Impact: 99.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 425 instances
* *State Mutation (weighted view):* 2191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 647`, `structural_boundaries: 280`, `args: 17`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1341`, `planned_debt: 9`, `unreferenced_by_name: 3`
* *Architecture:* `io: 724`, `import: 4`
* *Defense:* `safety: 23`, `test: 2950`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` k5_common, AI, Announcements, Course::TAB_ANNOUNCEMENTS, Course::TAB_COURSE_PACES, Course::TAB_DISCUSSIONS, Course::TAB_GRADES, Course::TAB_GROUPS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/features/gradebook/react/default_gradebook/Gradebook.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3535.62 | **LOC:** 5644 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **97**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.6%), Connectivity (formerly Api Exposure) (82.6%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 99.5192% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `componentDidUpdate` **(Many-Argument Workhorses)** (Impact: 140.4)
  * `render` **(I/O & Config Routines)** (Impact: 51.3)
  * `handleViewOptionsUpdated` **(Compute Cores)** (Impact: 46.6)
  * `gradeSubmission` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `compareAssignmentModulePositions` **(Defensive Guards)** (Impact: 43.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 374 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 1416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 983`, `args: 521`, `func_start: 347`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 668`, `dead_code: 2`, `planned_debt: 8`
* *Architecture:* `io: 3`, `api: 69`, `concurrency: 19`, `import: 100`
* *Defense:* `safety: 165`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 66):` api.d, GradeDisplayWarningDialog, GradebookKeyboardNav, PostGradesFrameDialog, NumberCompare, LatePolicyApplicator, PostGradesStore, EnterGradesAsSetting...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/api/fulldoc/html/js/swagger-ui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3119.38 | **LOC:** 2120 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.037; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `program1` **(Defensive Guards)** (Impact: 42.6)
  * `submitOperation` **(Compute Cores)** (Impact: 27.1)
  * `buildUrl` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `handleFileUpload` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `showStatus` **(Defensive Guards)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 727 instances
* *State Mutation (weighted view):* 2304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 373`, `args: 199`, `func_start: 148`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 850`, `dead_code: 1`, `duplicate_logic: 26`
* *Architecture:* `api: 5`, `concurrency: 1`
* *Defense:* `safety: 273`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.8e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/jquery-qtip/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3112.28 | **LOC:** 2926 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.032; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.0%), Complexity Load (formerly Cognitive Load) (87.6%), Connectivity (formerly Api Exposure) (34.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reposition` **(Many-Argument Workhorses)** (Impact: 188.4)
  * `viewport` **(Many-Argument Workhorses)** (Impact: 132.8)
  * `reposition` **(Defensive Guards)** (Impact: 102.5)
  * `toggle` **(Many-Argument Workhorses)** (Impact: 97.8)
  * `calculate` **(Many-Argument Workhorses)** (Impact: 91.5)
    * *Intent:* // Generic calculation method
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 427 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 1331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 785`, `structural_boundaries: 212`, `args: 162`, `func_start: 94`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 477`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 242`, `test: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/submission.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3078.72 | **LOC:** 3892 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Complexity Load (formerly Cognitive Load) (78.6%), Connectivity (formerly Api Exposure) (62.4%)
- **Documentation Coverage:** 99.4859% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_bulk_update` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `visible_rubric_assessments_for` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `infer_values` **(I/O & Config Routines)** (Impact: 42.9)
  * `check_vericite_status` **(Compute Cores)** (Impact: 40.5)
  * `can_view_plagiarism_report` **(Compute Cores)** (Impact: 35.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 400 instances
* *State Mutation (weighted view):* 1275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 969`, `structural_boundaries: 485`, `args: 116`, `func_start: 277`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 475`, `dead_code: 7`, `planned_debt: 3`
* *Architecture:* `io: 136`, `api: 83`, `import: 1`
* *Defense:* `safety: 72`, `doc: 3`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Canvas::GradeValidations, CustomValidations, HtmlTextHelper, LinkedAttachmentHandler, SendToStream, Tardiness, Workflow, anonymity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/user.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3070.22 | **LOC:** 4120 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Complexity Load (formerly Cognitive Load) (90.7%), Guard Balance (formerly Safety Score) (89.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_account_associations` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `name_parts` **(Compute Cores)** (Impact: 45.9)
    * *Intent:* # see also user_sortable_name.js
  * `upcoming_events` **(Compute Cores)** (Impact: 43.7)
  * `create_courses_right` **(Compute Cores)** (Impact: 43.0)
  * `avatar_url` **(Compute Cores)** (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 437 instances
* *State Mutation (weighted view):* 1436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 516`, `args: 155`, `func_start: 339`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 562`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 182`
* *Architecture:* `io: 277`
* *Defense:* `safety: 53`, `test: 3`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Context, FeatureFlags, ManyRootAccounts, ModelCache, PermissionsHelper, Pronouns, StickySisFields, TimeZoneHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-dnd-test-backend/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2934.02 | **LOC:** 5069 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Debt Markers (formerly Tech Debt) (79.5%)
- **Documentation Coverage:** 60.9665% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStore` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* * to hydrate the state from the server in universal apps, or to restore a * previously serialized us...
  * `dirtyHandlerIds` **(Many-Argument Workhorses)** (Impact: 46.7)
  * `baseIntersection` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /** * The base implementation of methods like `_.intersection`, without support * for iteratee short...
  * `baseUniq` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /** * The base implementation of `_.uniqBy` without support for iteratee shorthands. * */
  * `baseDifference` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /** * The base implementation of methods like `_.difference` without support * for excluding multipl...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 406 instances
* *Concurrency (weighted view):* 41
* *State Mutation (weighted view):* 1420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 745`, `args: 388`, `func_start: 280`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 608`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 169`, `concurrency: 11`
* *Defense:* `safety: 209`, `doc: 433`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/features/speed_grader/jquery/speed_grader.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2880.82 | **LOC:** 5130 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **71**; blast radius 0.036; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%), Connectivity (formerly Api Exposure) (59.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleSubmissionSelectionChange` **(I/O & Config Routines)** (Impact: 83.4)
  * `loadSubmissionPreview` **(Defensive Guards)** (Impact: 66.8)
  * `populateVeriCite` **(Many-Argument Workhorses)** (Impact: 58.4)
  * `populateTurnitin` **(Many-Argument Workhorses)** (Impact: 58.2)
  * `handleGradeSubmit` **(Many-Argument Workhorses)** (Impact: 55.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 237 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 934`, `structural_boundaries: 420`, `args: 320`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 356`, `dead_code: 14`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 23`, `concurrency: 4`, `import: 73`
* *Defense:* `safety: 97`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 7.4e-05
  * `Imports (Out-Degree: 40):` JQuerySelectorCache, QuizzesNextSpeedGrading, SpeedGraderStatusMenuHelpers, _turnitinInfo.handlebars, _vericiteInfo.handlebars, speech_recognition.handlebars, student_viewed_at.handlebars, submissions_dropdown.handlebars...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/controllers/courses_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2794.6 | **LOC:** 4757 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 29.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.032; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.5126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(I/O & Config Routines)** (Impact: 159.5)
    * *Intent:* # curl https://<canvas>/api/v1/courses/<course_id> \ # -X PUT \ # -H 'Authorization: Bearer <token>'...
  * `show` **(I/O & Config Routines)** (Impact: 119.9)
    * *Intent:* # - "banner_image": Include course banner image url if the course is a Canvas for # Elementary subje...
  * `courses_for_user` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `create` **(I/O & Config Routines)** (Impact: 51.2)
    * *Intent:* # Optional. The grade_passback_setting for the course. Only 'nightly_sync', 'disabled', and '' are a...
  * `users` **(I/O & Config Routines)** (Impact: 31.9)
    * *Intent:* # @argument user_id [String] # If this parameter is given and it corresponds to a user in the course...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 502 instances
* *State Mutation (weighted view):* 1591
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 796`, `structural_boundaries: 288`, `args: 25`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 587`, `dead_code: 4`, `planned_debt: 3`, `unreferenced_by_name: 35`
* *Architecture:* `io: 95`, `import: 5`
* *Defense:* `safety: 61`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnnouncementsController::AnnouncementsIndexHelper, Api::V1::ContextModule, Api::V1::Course, Api::V1::PreviewHtml, Api::V1::Progress, Api::V1::StreamItem, Api::V1::TodoItem, Api::V1::User...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/features/quizzes/jquery/quizzes.jsx` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2787.6 | **LOC:** 5724 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.1%), Complexity Load (formerly Cognitive Load) (70.4%), Connectivity (formerly Api Exposure) (35.6%)
- **Documentation Coverage:** 95.5128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateFormAnswer` **(Many-Argument Workhorses)** (Impact: 110.3)
    * *Intent:* // Updates answer when the question's type changes
  * `updateDisplayQuestion` **(Many-Argument Workhorses)** (Impact: 108.2)
  * `updateFormQuestion` **(Defensive Guards)** (Impact: 75.6)
    * *Intent:* // Updates the question's form when the type changes
  * `formulaQuestion` **(I/O & Config Routines)** (Impact: 70.5)
  * `processData` **(Defensive Guards)** (Impact: 57.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 396 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 1291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 455`, `args: 359`, `func_start: 136`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 499`, `dead_code: 7`, `planned_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 14`, `concurrency: 9`, `import: 37`
* *Defense:* `safety: 226`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` quiz_formula_solution, QuizRegradeModal, QuizRegradeModal.utils, MultipleChoiceToggle, calcCmd, quiz_labels, changeMultiFunc, AssignmentExternalTools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/shared/do-fetch-api-effect/__tests__/index.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2570.95 | **LOC:** 543 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.032; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (73.7%), Guard Balance (formerly Safety Score) (71.8%), Mutation Surface (formerly State Flux) (46.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 133`, `args: 59`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 12`
* *Architecture:* `io: 106`, `concurrency: 54`, `import: 4`
* *Defense:* `safety: 15`, `test: 77`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index, msw, node, zod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/attachment.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2551.82 | **LOC:** 2830 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Guard Balance (formerly Safety Score) (85.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `batch_destroy` **(Compute Cores)** (Impact: 360.5)
  * `ajax_upload_params` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* # Build the data that will be needed for the user to upload to s3 # without us being the middle-man ...
  * `migrate_attachments` **(Stateful Encapsulated Methods)** (Impact: 47.0)
  * `handle_duplicates` **(Compute Cores)** (Impact: 36.5)
  * `process_s3_details!` **(Defensive Guards)** (Impact: 31.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 299 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 962
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 638`, `structural_boundaries: 341`, `args: 87`, `func_start: 202`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 364`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 142`, `api: 58`, `import: 2`
* *Defense:* `safety: 79`, `test: 8`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ContextModuleItem, DatesOverridable, HasContentTags, MasterCourses::Restrictor, SearchTermHelper, Workflow, amazon_s3, file_store
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ui/shared/grading-scheme/react/components/form/__tests__/GradingSchemeInput.test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2426.55 | **LOC:** 739 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (15.8%), Mutation Surface (formerly State Flux) (11.8%), Guard Balance (formerly Safety Score) (9.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 81`, `args: 52`, `func_start: 10`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `concurrency: 23`, `import: 5`
* *Defense:* `safety: 57`, `test: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GradingSchemeInput, fixtures, react, user-event, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/controllers/application_controller.rb` -> Churn: **95.49%** | Cog Load: 93.0848% | Debt: 51.4927%
- `app/controllers/users_controller.rb` -> Churn: **93.46%** | Cog Load: 48.5869% | Debt: 64.1001%
- `app/controllers/courses_controller.rb` -> Churn: **89.13%** | Cog Load: 72.5307% | Debt: 37.2527%
- `app/models/account.rb` -> Churn: **88.82%** | Cog Load: 70.1319% | Debt: 7.8811%
- `app/models/course.rb` -> Churn: **83.5%** | Cog Load: 91.9635% | Debt: 7.8473%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/services/rubric_llm_service.rb` -> **Laszlo Sipula** (100.0% isolated ownership) | Magnitude: 9048.03
- `ui/features/quizzes/jquery/quizzes.jsx` -> **Adrian Gruber** (100.0% isolated ownership) | Magnitude: 2787.6
- `config/initializers/active_record.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 2327.64
- `ui/features/syllabus_revisions/react/__tests__/SyllabusRevisionsTray.test.tsx` -> **Eric Saupe** (100.0% isolated ownership) | Magnitude: 2024.21
- `ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/__tests__/Preview.test.tsx` -> **viktor.szpisjak** (100.0% isolated ownership) | Magnitude: 1831.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/canvas-rce/src/rce/RCEWrapper.tsx` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.9202%)
- `ui/features/gradebook/react/default_gradebook/components/SubmissionCommentForm.tsx` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 88.2207%)
- `ui/features/gradebook/react/default_gradebook/components/SubmissionTray.tsx` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 81.064%)
- `ui/features/gradebook/react/default_gradebook/GradebookGrid/headers/AssignmentColumnHeader.tsx` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 52.4979%)
- `ui/features/gradebook/react/default_gradebook/components/SubmissionCommentCreateForm.tsx` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 55.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ui/shared/test-utils/fakeENV.js` -> **Severity: 1.887** (Embedded: 0.0251 * Error Risk: 75.2927%)
- `ui/shared/datetime/date-functions.js` -> **Severity: 1.054** (Embedded: 0.0113 * Error Risk: 93.5031%)
- `ui/shared/instui-bindings/react/InstuiModal.tsx` -> **Severity: 0.57** (Embedded: 0.0074 * Error Risk: 76.5504%)
- `ui/shared/instui-bindings/react/liveRegion.ts` -> **Severity: 0.557** (Embedded: 0.0084 * Error Risk: 66.5013%)
- `ui/shared/i18n/i18nObj.js` -> **Severity: 0.516** (Embedded: 0.006 * Error Risk: 86.2625%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ui/shared/test-utils/fakeENV.js` -> **Severity: 651.6** (Blast Radius: 6.516 * Doc Risk: 100.0%)
- `spec/graphql/graphql_spec_helper.rb` -> **Severity: 512.9** (Blast Radius: 5.129 * Doc Risk: 100.0%)
- `spec/helpers/graphql_type_tester.rb` -> **Severity: 436.9** (Blast Radius: 4.369 * Doc Risk: 100.0%)
- `ui/shared/datetime/date-functions.js` -> **Severity: 354.1** (Blast Radius: 3.541 * Doc Risk: 100.0%)
- `ui/shared/instui-bindings/react/liveRegion.ts` -> **Severity: 297.2** (Blast Radius: 2.972 * Doc Risk: 100.0%)

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
