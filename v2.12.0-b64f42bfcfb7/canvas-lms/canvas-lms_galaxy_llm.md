# ARCHITECTURAL_BRIEF: canvas-lms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/instructure/canvas-lms.git` |
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
- **Scope:** 19989 analyzed artifact(s), 2426753 LOC.
- **Load-bearing artifact:** `spec/selenium/common.rb` -- 514 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ui/featureBundles.ts` -- pulls in 212 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `app/services/rubric_llm_service.rb` at magnitude 9106.34 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 19989 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2530 |
| Total LOC | 2426753 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.8% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8963 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0601 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.304 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2967 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 6586 | 1100774 | 32.9% |
| TYPESCRIPT | 5412 | 638095 | 27.1% |
| JAVASCRIPT | 4400 | 543330 | 22.0% |
| HTML | 901 | 44120 | 4.5% |
| XML | 676 | 385 | 3.4% |
| JSON | 674 | 40967 | 3.4% |
| PLAINTEXT | 509 | 1 | 2.5% |
| CSS | 420 | 45192 | 2.1% |
| MARKDOWN | 155 | 0 | 0.8% |
| YAML | 137 | 10778 | 0.7% |
| SHELL | 80 | 1936 | 0.4% |
| CSV | 26 | 421 | 0.1% |
| LUA | 7 | 93 | 0.0% |
| DOCKERFILE | 5 | 136 | 0.0% |
| GROOVY | 1 | 525 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 19985 |
| utf-8 | bom | 3 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 23%, Data / Markup / Trivial 21%, Callbacks & Closures Files 18%, Large Core Modules (2) 6%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19101 | 95.6% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 663 | 3.3% |
| Static: Minified & Vendor Opaque Mass | 224 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2530*

**Composition by Extension & Reason:**
- `.png`: 630x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 204x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 43x Excluded (Massive Static Asset Blob: 2994 LOC), 9x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.handlebars`: 230x Excluded (Unsupported Extension: '.handlebars')
- `.rb`: 201x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2192 LOC), 1x Excluded (Saturation: Line 32 exceeds 500 chars)
- `.js`: 77x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 56x Excluded (Saturation: Line 21 exceeds 500 chars), 44x Excluded (Saturation: Line 22 exceeds 500 chars)
- `no_extension`: 124x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.package-translations'), 2x Unsupported Format (.undeterminable)
- `.gif`: 101x Excluded (Explicitly Denied Extension: '.gif')
- `.xss`: 94x Excluded (Unsupported Extension: '.xss')
- `.zip`: 92x Excluded (Explicitly Denied Extension: '.zip')
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 41511 LOC), 1x Excluded (Massive Static Asset Blob: 43287 LOC)
- `.lock`: 44x Excluded (Unsupported Extension: '.lock'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.example`: 35x Excluded (Unsupported Extension: '.example')
- `.scss`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Zero-Density Threshold (LOC: 451, Signals: 0)
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.1 | 6.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.4 | 31.3 | 43.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 95.5 | 4.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3949 | 1511 | 0 | `ui/features/assignment_edit/react/hooks/__tests__/usePeerReviewSettings.test.ts` |
| cleanup | 1338 | 1003 | 0 | `ui/features/gradebook/react/default_gradebook/GradebookGrid/editors/AssignmentCellEditor/__tests__/AssignmentCellEditor.test.jsx` |
| guards | 44847 | 7258 | 6 | `doc/api/fulldoc/html/js/swagger-ui.js` |
| danger | 19033 | 4992 | 2 | `spec/controllers/application_controller_spec.rb` |
| concurrency | 38960 | 3323 | 4 | `ui/features/section/react/__tests__/CrosslistForm.test.tsx` |
| connectivity | 60692 | 8471 | 6 | `config/routes.rb` |
| io | 74087 | 6159 | 7 | `spec/models/assignment_spec.rb` |
| crypto | 4 | 4 | 0 | `ui/shared/encrypted-forage/index.js` |
| ipc | 336 | 114 | 0 | `packages/canvas-rce/src/enhance-user-content/__tests__/instructure_helper.test.js` |
| time | 3820 | 1326 | 0 | `packages/jqueryui/datepicker.js` |
| serialization | 1820 | 652 | 0 | `spec/lib/cc/basic_lti_links_spec.rb` |
| regex | 2810 | 1099 | 0 | `lib/swagger_yard/canvas_adapter.rb` |
| events | 9755 | 2692 | 1 | `ui/features/quizzes/jquery/quizzes.jsx` |
| tests | 338749 | 6727 | 42 | `spec/models/assignment_spec.rb` |
| docs | 6557 | 1247 | 0 | `packages/react-dnd-test-backend/index.js` |
| debt | 8078 | 1875 | 0 | `spec/models/accessibility/rules/list_structure_rule_spec.rb` |
| mutation | 504745 | 15508 | 57 | `spec/apis/v1/assignments_api_spec.rb` |
| dead_code | 9724 | 3583 | 1 | `app/models/user.rb` |
| credential | 261 | 145 | 0 | `spec/apis/v1/submissions_api_spec.rb` |
| threat | 1577 | 87 | 0 | `packages/canvas-rce/src/translations/tinymce/he_IL.js` |
| ml_ai | 564 | 216 | 0 | `gems/plugins/account_reports/spec_canvas/grade_reports_spec.rb` |
| ui | 79544 | 6756 | 12 | `ui/features/discussion_topics_post/react/containers/DiscussionThreadContainer/DiscussionThreadContainer.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spec/models/assignment_spec.rb` (Hits: 1061)
- `spec/models/submission_spec.rb` (Hits: 996)
- `spec/models/course_spec.rb` (Hits: 730)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.rb** (`spec/selenium/common.rb`) — 514 inbound connections
2. **selenium_driver_setup.rb** (`spec/selenium/test_setup/selenium_driver_setup.rb`) — 277 inbound connections
3. **application_controller.rb** (`app/controllers/application_controller.rb`) — 252 inbound connections
4. **setting.rb** (`app/models/setting.rb`) — 237 inbound connections
5. **generate_data.rb** (`spec/fixtures/data_generation/generate_data.rb`) — 225 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **featureBundles.ts** (`ui/featureBundles.ts`) — 212 outbound dependencies
2. **loadLocale.ts** (`ui/loadLocale.ts`) — 137 outbound dependencies
3. **Gradebook.tsx** (`ui/features/gradebook/react/default_gradebook/Gradebook.tsx`) — 97 outbound dependencies
4. **getTranslations.js** (`packages/canvas-rce/src/getTranslations.js`) — 77 outbound dependencies
5. **getTranslations.js** (`packages/canvas-media/src/getTranslations.js`) — 76 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `SlickGrid` **(Many-Argument Workhorses)** (@ `packages/slickgrid/slick.grid.js`) -> Impact: **2033.9** | LOC: 4096
  * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // SlickGrid class implementation (available as Slick....
- `in_batches_with_temp_table` **(Many-Argument Workhorses)** (@ `config/initializers/active_record.rb`) -> Impact: **833.5** | LOC: 1324
- `DiscussionTopicForm` **(Many-Argument Workhorses)** (@ `ui/features/discussion_topic_edit_v2/react/components/DiscussionTopicForm/DiscussionTopicForm.tsx`) -> Impact: **623.1** | LOC: 1573
- `add_course` **(Many-Argument Workhorses)** (@ `lib/sis/course_importer.rb`) -> Impact: **485.1** | LOC: 218
- `batch_destroy` **(Compute Cores)** (@ `app/models/attachment.rb`) -> Impact: **436.9** | LOC: 1044
- `load` **(Many-Argument Workhorses)** (@ `app/graphql/graphql_node_loader.rb`) -> Impact: **424.6** | LOC: 333
- `import_from_migration` **(Many-Argument Workhorses)** (@ `app/models/importers/assignment_importer.rb`) -> Impact: **396.4** | LOC: 335
- `concurrent_inserts` **(I/O & Config Routines)** (@ `spec/models/assignment_spec.rb`) -> Impact: **339.5** | LOC: 5179
- `create_completed_assessment_request` **(Many-Argument Workhorses)** (@ `spec/models/assignment_spec.rb`) -> Impact: **316.0** | LOC: 1953
- `assignment_json` **(Many-Argument Workhorses)** (@ `lib/api/v1/assignment.rb`) -> Impact: **276.2** | LOC: 425

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/models` | 289 | 56009.54 | 37.53% | 41.71% |
| `spec/models` | 227 | 53638.3 | 14.68% | 0.0% |
| `app/controllers` | 199 | 42361.72 | 42.63% | 49.6% |
| `spec/controllers` | 138 | 35760.3 | 9.78% | 0.0% |
| `spec/apis/v1` | 103 | 33061.26 | 13.4% | 0.0% |
| `lib` | 160 | 18949.62 | 46.91% | 50.97% |
| `spec/lib` | 128 | 15097.24 | 14.47% | 0.0% |
| `lib/api/v1` | 105 | 13216.16 | 44.94% | 35.79% |
| `app/services` | 15 | 11028.7 | 41.02% | 37.79% |
| `spec/graphql/types` | 87 | 10191.4 | 11.49% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/frontend.yml` -> **100.0%** Exposure
- `packages/canvas-rce/src/rce/plugins/instructure_paste/pasteMenuCommand.js` -> **100.0%** Exposure
- `packages/slickgrid/slick.editors.js` -> **100.0%** Exposure
- `ui/features/discussion_topics_post/react/utils/constants.jsx` -> **100.0%** Exposure
- `ui/shared/add-people/react/components/__tests__/add_people.spec.jsx` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/api/fulldoc/html/js/handlebars-1.0.0.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/pendo.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/swagger-ui.js` -> **100.0%** Exposure
- `doc/api/fulldoc/html/js/swagger.js` -> **100.0%** Exposure
- `packages/canvas-media/src/getTranslations.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/models/user.rb` -> **183** Orphaned Functions | **0** Duplicates
- `app/models/abstract_assignment.rb` -> **138** Orphaned Functions | **0** Duplicates
- `app/helpers/application_helper.rb` -> **78** Orphaned Functions | **0** Duplicates
- `app/models/discussion_topic.rb` -> **55** Orphaned Functions | **0** Duplicates
- `app/controllers/application_controller.rb` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `docker-compose/config/consul.yml` -> **100.0%** Exposure
- `spec/selenium/new_login/otp_page_spec.rb` -> **100.0%** Exposure
- `lib/cc/cc_helper.rb` -> **99.9999%** Exposure
- `ui/features/new_login/pages/register/__tests__/StudentSubmission.test.tsx` -> **99.9999%** Exposure
- `ui/features/new_login/routes/routes.ts` -> **99.9999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `146` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `43835` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `app/services/rubric_llm_service.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.467)
- **Top Global Matches:** file_cluster_2: 4.467, file_cluster_10: 4.516, file_cluster_17: 5.942
- **Magnitude:** 9106.34 | **LOC:** 962 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.025; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (58.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 47`, `args: 33`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `state_mutation: 164`, `planned_debt: 1`
* *Architecture:* `io: 7`
* *Defense:* `safety: 8`, `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HtmlTextHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/slickgrid/slick.grid.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.616)
- **Top Global Matches:** file_cluster_4: 9.616, file_cluster_12: 11.361, file_cluster_15: 13.461
- **Magnitude:** 5169.84 | **LOC:** 4192 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.025; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 86.5079% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SlickGrid` **(Many-Argument Workhorses)** (Impact: 2033.9)
    * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // S...
  * `setupColumnResize` **(I/O & Config Routines)** (Impact: 80.8)
  * `appendRowHtml` **(Many-Argument Workhorses)** (Impact: 58.9)
  * `handleKeyDown` **(Compute Cores)** (Impact: 54.2)
  * `init` **(I/O & Config Routines)** (Impact: 39.7)
    * *Intent:* // //////////////////////////////////////////////////////////////////////////////////////////// // I...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 456 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 1430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 820`, `structural_boundaries: 661`, `args: 215`, `func_start: 188`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 11`, `state_mutation: 518`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 9`, `import: 3`
* *Defense:* `safety: 82`, `doc: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rtlHelper, jquery, normalize-scroll-left
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/submission_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.564)
- **Top Global Matches:** file_cluster_10: 8.564, file_cluster_15: 9.004, file_cluster_11: 9.415
- **Magnitude:** 4622.94 | **LOC:** 11564 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 41.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.9%), Guard Balance (formerly Safety Score) (45.0%), Complexity Load (formerly Cognitive Load) (33.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `submission_spec_model` **(Compute Cores)** (Impact: 13.6)
  * `setup_account_for_turnitin` **(Parameter Forwarders)** (Impact: 1.7)
  * `make_attachment` **(Parameter Forwarders)** (Impact: 1.6)
  * `peer_review_assignment` **(I/O & Config Routines)** (Impact: 1.6)
  * `submission_for_some_user` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 524 instances
* *State Mutation (weighted view):* 2583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 881`, `structural_boundaries: 285`, `args: 4`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 1535`, `fragile_debt: 2`
* *Architecture:* `io: 996`, `import: 2`
* *Defense:* `safety: 95`, `test: 3034`, `immutability_locks: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` validates_as_url, attachment, attachments, do
      attachment = attachment_model(filename:, draft, duplicates, eligible, excused...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/assignment_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.821)
- **Top Global Matches:** file_cluster_8: 9.821, file_cluster_6: 13.281, file_cluster_4: 20.837
- **Magnitude:** 4545.34 | **LOC:** 14538 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.6%), Guard Balance (formerly Safety Score) (43.3%), Complexity Load (formerly Cognitive Load) (26.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `concurrent_inserts` **(I/O & Config Routines)** (Impact: 339.5)
  * `create_completed_assessment_request` **(Many-Argument Workhorses)** (Impact: 316.0)
  * `generate_comments` **(Many-Argument Workhorses)** (Impact: 213.8)
  * `student_unread_count_counts` **(I/O & Config Routines)** (Impact: 204.5)
  * `assignment` **(I/O & Config Routines)** (Impact: 73.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 597 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 2779
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1146`, `structural_boundaries: 303`, `args: 8`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 9`, `state_mutation: 1585`, `planned_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1061`, `import: 6`
* *Defense:* `safety: 27`, `test: 4062`, `sync_locks: 1`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` lti2_spec_helper, groups_common, GroupsCommon, Shard, a, admin, an_object_having_attributes, assignment...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/course.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.677)
- **Top Global Matches:** file_cluster_4: 10.677, file_cluster_15: 10.93, file_cluster_12: 11.131
- **Magnitude:** 4026.3 | **LOC:** 5058 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **21**; blast radius 0.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Connectivity (formerly Api Exposure) (89.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uncached_tabs_available` **(Many-Argument Workhorses)** (Impact: 172.5)
    * *Intent:* # make sure t() is called before we switch to the secondary, in case we update the user's selected l...
  * `enroll_user` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `generate_grade_publishing_csv_output` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `update_account_associations` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `add_setting` **(Compute Cores)** (Impact: 42.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 497 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 588`, `args: 144`, `func_start: 351`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 625`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 316`, `api: 172`
* *Defense:* `safety: 82`, `test: 3`, `sync_locks: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 0.00061 | `Ripple Effect (Closeness):` 0.021982
  * `Imports (Out-Degree: 41):` Accessibility::Scannable, ContentLicenses, ContentNotices, Context, CopiedAssets, Courses::ExportWarnings, Courses::ItemVisibilityHelper, Csp::CourseHelper...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `spec/apis/v1/assignments_api_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.156)
- **Top Global Matches:** file_cluster_10: 8.156, file_cluster_12: 8.314, file_cluster_15: 8.623
- **Magnitude:** 3980.86 | **LOC:** 12270 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.4%), Guard Balance (formerly Safety Score) (53.0%), Complexity Load (formerly Cognitive Load) (25.5%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adhoc_override_api_call` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `mock_and_call_create_api_assignment` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `call_update_assignment_api` **(Compute Cores)** (Impact: 6.4)
  * `api_bulk_update` **(Many-Argument Workhorses)** (Impact: 5.5)
  * `build_peer_review_assignment` **(Defensive Guards)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 490 instances
* *State Mutation (weighted view):* 2497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 171`, `args: 30`, `func_start: 37`
* *Risk/State:* `safety_bypasses: 89`, `high_risk_execution: 1`, `state_mutation: 1517`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 623`, `api: 27`, `import: 4`
* *Defense:* `safety: 12`, `test: 2121`, `sync_locks: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` lti2_spec_helper, lti_spec_helper, api_spec_helper, locked_examples, Api, Api::V1::Assignment, Api::V1::Submission, LtiSpecHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/course_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.819)
- **Top Global Matches:** file_cluster_10: 7.819, file_cluster_15: 8.665, file_cluster_11: 9.346
- **Magnitude:** 3813.1 | **LOC:** 10427 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 23.5%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **55**; blast radius 0.546; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.0%), Guard Balance (formerly Safety Score) (43.7%), Complexity Load (formerly Cognitive Load) (29.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expect_active_now` **(Many-Argument Workhorses)** (Impact: 7.4)
  * `quick_sanity_check` **(Compute Cores)** (Impact: 6.7)
  * `create_temp_enrollment` **(Compute Cores)** (Impact: 4.7)
  * `sample_grade_publishing_request` **(Callbacks & Closures)** (Impact: 2.9)
  * `add_pseudonym` **(Parameter Forwarders)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 431 instances
* *State Mutation (weighted view):* 2203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 647`, `structural_boundaries: 280`, `args: 17`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1341`, `planned_debt: 9`, `duplicate_logic: 3`
* *Architecture:* `io: 730`, `import: 4`
* *Defense:* `safety: 23`, `test: 2950`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.546
  * `Choke Point (Betweenness):` 0.000239 | `Ripple Effect (Closeness):` 0.017714
  * `Imports (Out-Degree: 21):` k5_common, AI, Announcements, Course::TAB_ANNOUNCEMENTS, Course::TAB_COURSE_PACES, Course::TAB_DISCUSSIONS, Course::TAB_GRADES, Course::TAB_GROUPS...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `app/models/abstract_assignment.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.4)
- **Top Global Matches:** file_cluster_15: 8.4, file_cluster_10: 9.169, file_cluster_11: 9.341
- **Magnitude:** 3683.16 | **LOC:** 4798 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **19**; blast radius 0.494; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 98.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_grade_to_submission` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `submit_homework` **(Many-Argument Workhorses)** (Impact: 50.3)
    * *Intent:* %w[comment group_comment attachments require_submission_type_is_valid resource_link_lookup_uuid stud...
  * `grade_student` **(Compute Cores)** (Impact: 47.7)
  * `representatives` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* # for group assignments, returns a single "student" for each # group's submission. the students name...
  * `score_to_grade` **(Many-Argument Workhorses)** (Impact: 42.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 477 instances
* *State Mutation (weighted view):* 1549
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 602`, `args: 152`, `func_start: 352`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 595`, `planned_debt: 5`, `unreferenced_by_name: 138`
* *Architecture:* `io: 198`, `import: 2`
* *Defense:* `safety: 73`, `doc: 7`, `test: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.494
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.015612
  * `Imports (Out-Degree: 39):` ApplicationHelper, Assignments::GraderIdentities, Canvas::DraftStateValidations, ContextModuleItem, CopyAuthorizedLinks, DatesOverridable, DuplicatingObjects, HasContentTags...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `ui/features/gradebook/react/default_gradebook/Gradebook.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.92)
- **Top Global Matches:** file_cluster_10: 9.92, file_cluster_4: 10.086, file_cluster_15: 10.389
- **Magnitude:** 3515.92 | **LOC:** 5644 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **97**; blast radius 0.695; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.3%), Connectivity (formerly Api Exposure) (81.5%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `componentDidUpdate` **(Many-Argument Workhorses)** (Impact: 140.4)
  * `render` **(I/O & Config Routines)** (Impact: 51.3)
  * `handleViewOptionsUpdated` **(Compute Cores)** (Impact: 46.6)
  * `compareAssignmentModulePositions` **(Defensive Guards)** (Impact: 43.0)
  * `gradeSubmission` **(Many-Argument Workhorses)** (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 368 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 1404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 923`, `structural_boundaries: 983`, `args: 521`, `func_start: 347`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 668`, `planned_debt: 8`
* *Architecture:* `io: 3`, `api: 65`, `concurrency: 19`, `import: 100`
* *Defense:* `safety: 165`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.695
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.002881
  * `Imports (Out-Degree: 56):` api.d, GradeDisplayWarningDialog, GradebookKeyboardNav, PostGradesFrameDialog, NumberCompare, LatePolicyApplicator, PostGradesStore, EnterGradesAsSetting...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `app/controllers/application_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.691)
- **Top Global Matches:** file_cluster_4: 7.691, file_cluster_15: 8.999, file_cluster_12: 9.916
- **Magnitude:** 3372.8 | **LOC:** 3694 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 21.4%
- **Blast Radius:** changing it is visible to **252** in-repo importer(s); it depends on **11**; blast radius 2.524; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%)
- **Documentation Coverage:** 99.5652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `js_env` **(Many-Argument Workhorses)** (Impact: 142.0)
    * *Intent:* # Also, please don't name it stuff from JavaScript's Object.prototype # like `hasOwnProperty`, `cons...
  * `content_tag_redirect` **(Many-Argument Workhorses)** (Impact: 139.5)
  * `get_context` **(Compute Cores)** (Impact: 72.1)
    * *Intent:* # Can be used as a before_action, or just called from controller code. # Assigns the variable @conte...
  * `get_feed_context` **(Stateful Encapsulated Methods)** (Impact: 65.3)
    * *Intent:* # Used to retrieve the context from a :feed_code parameter. These # :feed_code attributes are keyed ...
  * `safe_domain_file_url` **(Many-Argument Workhorses)** (Impact: 56.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 491 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1545
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 886`, `structural_boundaries: 397`, `args: 94`, `func_start: 229`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 563`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `io: 41`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 134`, `doc: 4`, `test: 5`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.524
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.011874
  * `Imports (Out-Degree: 52):` Api, Api::V1::Course, Api::V1::Group, Api::V1::User, Api::V1::UserProfile, Api::V1::WikiPage, AuthenticationMethods, Canvas::RequestForgeryProtection...
  * `Imported By (In-Degree: 252):` (Excluded from Brief to save tokens)

### `packages/jquery-qtip/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.672)
- **Top Global Matches:** file_cluster_6: 7.672, file_cluster_4: 9.896, file_cluster_8: 17.236
- **Magnitude:** 3110.28 | **LOC:** 2926 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.025; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.5%), Guard Balance (formerly Safety Score) (70.1%), Connectivity (formerly Api Exposure) (34.7%)
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
* *Structure:* `branch: 782`, `structural_boundaries: 212`, `args: 162`, `func_start: 94`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 477`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `concurrency: 7`, `import: 1`
* *Defense:* `safety: 242`, `test: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/submission.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.758)
- **Top Global Matches:** file_cluster_15: 8.758, file_cluster_4: 8.787, file_cluster_12: 9.514
- **Magnitude:** 3103.02 | **LOC:** 3892 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **8**; blast radius 0.2; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (65.2%), Connectivity (formerly Api Exposure) (62.4%)
- **Documentation Coverage:** 99.4872% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 475`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 136`, `api: 83`, `import: 1`
* *Defense:* `safety: 72`, `doc: 3`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.2
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.00086
  * `Imports (Out-Degree: 27):` Canvas::GradeValidations, CustomValidations, HtmlTextHelper, LinkedAttachmentHandler, SendToStream, Tardiness, Workflow, anonymity
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `app/models/user.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.556)
- **Top Global Matches:** file_cluster_10: 8.556, file_cluster_15: 8.623, file_cluster_11: 9.296
- **Magnitude:** 3069.9 | **LOC:** 4120 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **12**; blast radius 0.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Complexity Load (formerly Cognitive Load) (90.7%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 696`, `structural_boundaries: 516`, `args: 155`, `func_start: 339`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 562`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 183`
* *Architecture:* `io: 277`
* *Defense:* `safety: 53`, `test: 3`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.556
  * `Choke Point (Betweenness):` 0.000268 | `Ripple Effect (Closeness):` 0.021917
  * `Imports (Out-Degree: 25):` Context, FeatureFlags, ManyRootAccounts, ModelCache, PermissionsHelper, Pronouns, StickySisFields, TimeZoneHelper...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `doc/api/fulldoc/html/js/swagger-ui.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.513)
- **Top Global Matches:** file_cluster_12: 7.513, file_cluster_10: 9.543, file_cluster_15: 9.706
- **Magnitude:** 2967.18 | **LOC:** 2120 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.027; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `program1` **(Defensive Guards)** (Impact: 37.4)
  * `submitOperation` **(Compute Cores)** (Impact: 25.7)
  * `handleFileUpload` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `showStatus` **(Defensive Guards)** (Impact: 20.8)
  * `formatXml` **(Compute Cores)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 677 instances
* *State Mutation (weighted view):* 2204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 373`, `args: 199`, `func_start: 148`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 850`, `dead_code: 6`, `duplicate_logic: 26`
* *Architecture:* `api: 5`, `concurrency: 1`
* *Defense:* `safety: 273`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.9e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `config/initializers/active_record.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.078)
- **Top Global Matches:** file_cluster_12: 9.078, file_cluster_15: 10.926, file_cluster_4: 11.337
- **Magnitude:** 2831.76 | **LOC:** 2342 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **87** in-repo importer(s); it depends on **14**; blast radius 3.943; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.5%), Guard Balance (formerly Safety Score) (77.4%)
- **Documentation Coverage:** 97.8355% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `in_batches_with_temp_table` **(Many-Argument Workhorses)** (Impact: 833.5)
  * `in_batches_with_copy` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `as_json` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* # Example: # obj.to_json(:permissions => {:user => u, :policies => [:read, :write, :update]})
  * `wait_for_replication` **(Compute Cores)** (Impact: 25.2)
  * `update_many` **(Compute Cores)** (Impact: 23.1)
    * *Intent:* # Update many rows at once with unique values per row # # @param updates [Hash] A hash where the key...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 341 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 445`, `args: 118`, `func_start: 175`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 2`, `state_mutation: 432`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 82`, `api: 76`, `import: 10`
* *Defense:* `safety: 33`, `doc: 4`, `test: 1`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.943
  * `Choke Point (Betweenness):` 0.000458 | `Ripple Effect (Closeness):` 0.036168
  * `Imports (Out-Degree: 9):` ActiveSupport::Callbacks::Suspension, AdditionalIgnoredColumns, ClassMethods, DefineAttributeMethods, Extensions::ActiveRecord::ConnectionHandling, Extensions::ActiveRecord::DatabaseConfigurations, SkipTouchCallbacks::Base, UpdateAndDeleteAllWithLimit...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `app/controllers/courses_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.321)
- **Top Global Matches:** file_cluster_4: 7.321, file_cluster_6: 9.608, file_cluster_15: 13.645
- **Magnitude:** 2827.9 | **LOC:** 4757 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 29.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%)
- **Documentation Coverage:** 81.5126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(I/O & Config Routines)** (Impact: 159.5)
    * *Intent:* # curl https://<canvas>/api/v1/courses/<course_id> \ # -X PUT \ # -H 'Authorization: Bearer <token>'...
  * `show` **(I/O & Config Routines)** (Impact: 119.9)
    * *Intent:* # - "banner_image": Include course banner image url if the course is a Canvas for # Elementary subje...
  * `courses_for_user` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `create` **(I/O & Config Routines)** (Impact: 48.2)
    * *Intent:* # Optional. The grade_passback_setting for the course. Only 'nightly_sync', 'disabled', and '' are a...
  * `sort_enrollments` **(Compute Cores)** (Impact: 43.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 505 instances
* *State Mutation (weighted view):* 1597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 796`, `structural_boundaries: 288`, `args: 25`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 587`, `planned_debt: 3`, `unreferenced_by_name: 33`
* *Architecture:* `io: 95`, `import: 5`
* *Defense:* `safety: 61`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` AnnouncementsController::AnnouncementsIndexHelper, Api::V1::ContextModule, Api::V1::Course, Api::V1::PreviewHtml, Api::V1::Progress, Api::V1::StreamItem, Api::V1::TodoItem, Api::V1::User...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/attachment.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.62)
- **Top Global Matches:** file_cluster_4: 9.62, file_cluster_15: 10.909, file_cluster_16: 11.734
- **Magnitude:** 2810.68 | **LOC:** 2830 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **8**; blast radius 1.331; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.3%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `batch_destroy` **(Compute Cores)** (Impact: 436.9)
  * `clone_for` **(Many-Argument Workhorses)** (Impact: 68.7)
  * `clone_url` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `streaming_download` **(Defensive Guards)** (Impact: 40.3)
    * *Intent:* # GETs this attachment's public_url and streams the response to the # passed block; this is a helper...
  * `handle_duplicates` **(Many-Argument Workhorses)** (Impact: 36.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 316 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 997
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 694`, `structural_boundaries: 345`, `args: 87`, `func_start: 202`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 365`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 149`, `api: 62`, `import: 2`
* *Defense:* `safety: 81`, `test: 8`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.331
  * `Choke Point (Betweenness):` 0.000212 | `Ripple Effect (Closeness):` 0.031153
  * `Imports (Out-Degree: 20):` ContextModuleItem, DatesOverridable, HasContentTags, MasterCourses::Restrictor, SearchTermHelper, Workflow, amazon_s3, file_store
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `ui/features/speed_grader/jquery/speed_grader.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.876)
- **Top Global Matches:** file_cluster_4: 6.876, file_cluster_6: 9.532, file_cluster_15: 13.525
- **Magnitude:** 2765.22 | **LOC:** 5130 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **71**; blast radius 0.334; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%), Connectivity (formerly Api Exposure) (50.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleSubmissionSelectionChange` **(I/O & Config Routines)** (Impact: 83.4)
  * `loadSubmissionPreview` **(Defensive Guards)** (Impact: 61.6)
  * `populateVeriCite` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `handleGradeSubmit` **(Many-Argument Workhorses)** (Impact: 55.6)
    * *Intent:* // If the second argument is passed as true, the grade used will // be the existing score from the p...
  * `populateTurnitin` **(Many-Argument Workhorses)** (Impact: 50.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 234 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 891`, `structural_boundaries: 420`, `args: 320`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 4`, `state_mutation: 356`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 14`, `concurrency: 4`, `import: 73`
* *Defense:* `safety: 97`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.334
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00087
  * `Imports (Out-Degree: 20):` JQuerySelectorCache, QuizzesNextSpeedGrading, SpeedGraderStatusMenuHelpers, _turnitinInfo.handlebars, _vericiteInfo.handlebars, speech_recognition.handlebars, student_viewed_at.handlebars, submissions_dropdown.handlebars...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `ui/features/quizzes/jquery/quizzes.jsx` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.948)
- **Top Global Matches:** file_cluster_4: 6.948, file_cluster_6: 11.105, file_cluster_12: 12.069
- **Magnitude:** 2733.5 | **LOC:** 5724 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (70.6%), Guard Balance (formerly Safety Score) (59.0%), Connectivity (formerly Api Exposure) (33.8%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateDisplayQuestion` **(Many-Argument Workhorses)** (Impact: 108.2)
  * `updateFormAnswer` **(Many-Argument Workhorses)** (Impact: 96.3)
    * *Intent:* // Updates answer when the question's type changes
  * `updateFormQuestion` **(Defensive Guards)** (Impact: 75.6)
    * *Intent:* // Updates the question's form when the type changes
  * `formulaQuestion` **(I/O & Config Routines)** (Impact: 67.5)
  * `processData` **(Defensive Guards)** (Impact: 57.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 395 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 1289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 855`, `structural_boundaries: 455`, `args: 359`, `func_start: 136`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 499`, `planned_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 12`, `concurrency: 9`, `import: 37`
* *Defense:* `safety: 226`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5e-05
  * `Imports (Out-Degree: 7):` quiz_formula_solution, QuizRegradeModal, QuizRegradeModal.utils, MultipleChoiceToggle, calcCmd, quiz_labels, changeMultiFunc, AssignmentExternalTools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/react-dnd-test-backend/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.345)
- **Top Global Matches:** file_cluster_12: 7.345, file_cluster_15: 8.744, file_cluster_10: 9.352
- **Magnitude:** 2688.82 | **LOC:** 5069 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (78.8%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 61.0294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dirtyHandlerIds` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `baseIntersection` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /** * The base implementation of methods like `_.intersection`, without support * for iteratee short...
  * `createStore` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* * to hydrate the state from the server in universal apps, or to restore a * previously serialized us...
  * `baseUniq` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /** * The base implementation of `_.uniqBy` without support for iteratee shorthands. * */
  * `baseDifference` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /** * The base implementation of methods like `_.difference` without support * for excluding multipl...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 351 instances
* *Concurrency (weighted view):* 41
* *State Mutation (weighted view):* 1310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 745`, `args: 388`, `func_start: 280`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 608`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 169`, `concurrency: 11`
* *Defense:* `safety: 209`, `doc: 433`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/account.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.525)
- **Top Global Matches:** file_cluster_15: 10.525, file_cluster_10: 10.9, file_cluster_12: 10.923
- **Magnitude:** 2343.96 | **LOC:** 3073 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 28.0%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **13**; blast radius 0.638; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.0521% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tabs_available` **(Compute Cores)** (Impact: 139.7)
  * `settings=` **(Compute Cores)** (Impact: 35.6)
  * `get_special_account` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `set_service_availability` **(Compute Cores)** (Impact: 23.8)
  * `account_chain` **(Defensive Guards)** (Impact: 14.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 273 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 881
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 624`, `structural_boundaries: 440`, `args: 129`, `func_start: 280`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 335`, `planned_debt: 1`
* *Architecture:* `io: 122`, `api: 141`, `import: 3`
* *Defense:* `safety: 45`, `doc: 6`, `sync_locks: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.638
  * `Choke Point (Betweenness):` 0.000215 | `Ripple Effect (Closeness):` 0.020752
  * `Imports (Out-Degree: 32):` BrandConfigHelpers, Canvas::Security::PasswordPolicyAccountSettingValidator, Context, FeatureFlags, LearningOutcomeContext, OutcomeImportContext, Pronouns, RubricContext...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `spec/models/user_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_10: 7.308, file_cluster_2: 9.338, file_cluster_15: 9.452
- **Magnitude:** 2331.58 | **LOC:** 6266 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.8%), Guard Balance (formerly Safety Score) (43.9%), Complexity Load (formerly Cognitive Load) (19.0%), Dead Code Surface (formerly Dead Code) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_up_course_with_users` **(I/O & Config Routines)** (Impact: 2.0)
  * `assert_has_courses` **(Callbacks & Closures)** (Impact: 1.8)
  * `search_messageable_users` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* # convenience to search and then get the first page. none of these specs # should be putting more th...
  * `create_course_with_student_and_assignment` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 1401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 149`, `args: 4`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 861`, `dead_code: 1`
* *Architecture:* `io: 493`, `import: 3`
* *Defense:* `safety: 8`, `test: 1817`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` k5_common, Account, K5Common, account1, active_token, admin, assignment, assignments...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/users_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.203)
- **Top Global Matches:** file_cluster_4: 7.203, file_cluster_15: 11.696, file_cluster_6: 11.843
- **Magnitude:** 2220.3 | **LOC:** 3635 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 30.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 81.6092% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_user` **(I/O & Config Routines)** (Impact: 107.8)
  * `update` **(I/O & Config Routines)** (Impact: 75.1)
    * *Intent:* # Default is true. If false, any fields containing “sticky” changes will not be updated. # See SIS C...
  * `user_dashboard` **(I/O & Config Routines)** (Impact: 44.7)
  * `fetch_courses_with_grades` **(Compute Cores)** (Impact: 36.6)
  * `api_index` **(I/O & Config Routines)** (Impact: 23.6)
    * *Intent:* # @argument include_deleted_users [Boolean] # When set to true and used with an account context, ret...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 432 instances
* *State Mutation (weighted view):* 1391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 212`, `args: 14`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 527`, `planned_debt: 8`, `unreferenced_by_name: 44`
* *Architecture:* `io: 65`
* *Defense:* `safety: 49`, `doc: 71`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 40):` Api::V1::Account, Api::V1::Assignment, Api::V1::Avatar, Api::V1::CalendarEvent, Api::V1::StreamItem, Api::V1::Submission, Api::V1::TodoItem, Api::V1::User...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/apis/v1/submissions_api_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.942)
- **Top Global Matches:** file_cluster_15: 7.942, file_cluster_10: 8.051, file_cluster_2: 8.929
- **Magnitude:** 2168.84 | **LOC:** 8467 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.1%), Complexity Load (formerly Cognitive Load) (16.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `submit_homework` **(Compute Cores)** (Impact: 8.8)
  * `call_to_for_students` **(Compute Cores)** (Impact: 6.5)
  * `call_to_submissions_show` **(Compute Cores)** (Impact: 5.0)
  * `preflight` **(Many-Argument Workhorses)** (Impact: 4.8)
    * *Intent:* # preflight_params has to be first and nameless to keep backwards compat with the include_examples
  * `submit_with_grade` **(Many-Argument Workhorses)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 1411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 153`, `args: 9`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 1007`, `unreferenced_by_name: 1`
* *Architecture:* `io: 390`, `import: 2`
* *Defense:* `safety: 15`, `test: 1322`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` api_spec_helper, file_uploads_spec_helper, Api::V1::User, Services::SubmitHomeworkService::CopyWorker, Services::SubmitHomeworkService::SubmitWorker, action, capture_params, field...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ui/features/navigation_header/react/MobileNavigation.tsx` (TYPESCRIPT) | Magnitude: 28.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 33, ui_framework: 23, core_var_decl: 23
- `ui/features/widget_dashboard/react/components/widgets/InboxWidget/__tests__/InboxWidget.test.tsx` (TYPESCRIPT) | Magnitude: 15.88 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 203, test: 50, structural_boundaries: 46, generics: 24
- `ui/shared/rubrics/react/RubricForm/components/CriterionModal/CriterionName.tsx` (TYPESCRIPT) | Magnitude: 6.78 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, core_var_decl: 10, design_snake_case: 5
- `ui/features/assignment_index/react/NeverDrop.tsx` (TYPESCRIPT) | Magnitude: 23.34 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 20, core_var_decl: 17, branch: 12
- `ui/shared/assignments/react/__tests__/DateDue.test.tsx` (TYPESCRIPT) | Magnitude: 10.8 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 23, test: 22, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `ui/features/jobs_v2/react/components/GroupsTable.jsx` (JAVASCRIPT) | Magnitude: 9.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, core_var_decl: 19, ui_framework: 17, structural_boundaries: 16
- `ui/features/assignment_index/react/__tests__/NoAssignmentsSearch.test.tsx` (TYPESCRIPT) | Magnitude: 15.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, test: 4, import: 3
- `ui/shared/assignments/react/__tests__/PeerReviewConfigurationTray.test.tsx` (TYPESCRIPT) | Magnitude: 10.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 240, test: 68, structural_boundaries: 36, args: 27
- `gems/plugins/qti_exporter/lib/qti/respondus_settings.rb` (RUBY) | Magnitude: 63.3 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, branch: 20, structural_boundaries: 17, state_mutation: 10
- `ui/features/new_login/pages/register/__tests__/StudentValidation.test.tsx` (TYPESCRIPT) | Magnitude: 98.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 124, concurrency: 72, test: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/canvas/cross_region_query_metrics.rb` (RUBY) | Magnitude: 25.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, state_mutation: 7, branch: 5
- `ui/features/gradebook/react/default_gradebook/GradebookGrid/editors/CellEditorComponent.ts` (TYPESCRIPT) | Magnitude: 12.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, args: 5, func_start: 5
- `ui/shared/conditional-release-editor/react/components/assignment-set.jsx` (JAVASCRIPT) | Magnitude: 58.32 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 122, ui_framework: 32, core_var_decl: 28, structural_boundaries: 25
- `ui/shared/dashboard-card/react/DraggableDashboardCard.jsx` (JAVASCRIPT) | Magnitude: 20.5 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 11, args: 8, ui_framework: 8
- `ui/shared/planner/dynamic-ui/animations/__tests__/continue-initial-load.test.js` (JAVASCRIPT) | Magnitude: 4.5 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 11, test: 8, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ui/features/assignments_show_teacher_deprecated/react/components/__tests__/integration/AssignmentModules.test.jsx` (JAVASCRIPT) | Magnitude: 19.06 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 12, core_var_decl: 7, import: 6
- `ui/features/users_admin_merge/react/MergeUsers.tsx` (TYPESCRIPT) | Magnitude: 10.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 14, core_var_decl: 10, design_camel_case: 8
- `spec/services/peer_review/allocation_service_spec.rb` (RUBY) | Magnitude: 858.36 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1881, test: 606, state_mutation: 351, closures: 273
- `lib/brand_config_regenerator.rb` (RUBY) | Magnitude: 108.72 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 25, branch: 20, structural_boundaries: 15
- `packages/canvas-rce/src/rce/plugins/shared/ImageCropper/__tests__/imageCropUtils.test.js` (JAVASCRIPT) | Magnitude: 62.28 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 500, core_var_decl: 197, design_snake_case: 197, design_short_vars: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ui/features/media_immersive_view/index.tsx` (TYPESCRIPT) | Magnitude: 15.38 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, branch: 4, import: 4
- `ui/features/change_password/index.jsx` (JAVASCRIPT) | Magnitude: 15.3 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, core_var_decl: 5, structural_boundaries: 4, import: 3
- `lib/cc/exporter/epub/templates/content_sorting_template.html.erb` (HTML) | Magnitude: 16.5 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, ssr_boundaries: 15, structural_boundaries: 10, io: 8
- `ui/features/course_show_secondary/index.tsx` (TYPESCRIPT) | Magnitude: 15.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, branch: 4, import: 4
- `public/partials/_custom_search.html` (HTML) | Magnitude: 29.28 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 7, core_var_decl: 6, design_snake_case: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `ui/features/wiki_page_index/backbone/collections/__tests__/WikiPageCollection.spec.ts` (TYPESCRIPT) | Magnitude: 29.96 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 80, test: 36, structural_boundaries: 20, args: 18
- `packages/canvas-rce/src/rce/plugins/instructure_equation/EquationEditorModal/mathjax.override.css` (CSS) | Magnitude: 0.63 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 3, class_start: 1, safety_bypasses: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `ui/features/permissions/react/components/RoleTrayTable.jsx` (JAVASCRIPT) | Magnitude: 4.84 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, ui_framework: 6, import: 6
- `spec/selenium/helpers/differentiated_assignments.rb` (RUBY) | Magnitude: 49.62 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 18, structural_boundaries: 16, io: 11
- `gems/bookmarked_collection/lib/bookmarked_collection/filter_proxy.rb` (RUBY) | Magnitude: 47.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 13, branch: 8, core_var_decl: 5
- `app/graphql/loaders/module_item_master_course_restrictions_loader.rb` (RUBY) | Magnitude: 40.54 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 10, core_var_decl: 9, design_snake_case: 9
- `ui/shared/groups/react/mixins/BackboneState.js` (JAVASCRIPT) | Magnitude: 37.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, branch: 9, args: 8, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ui/features/new_login/shared/index.ts` (TYPESCRIPT) | Magnitude: 34.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 19, structural_boundaries: 19, api: 19, import: 19
- `ui/features/quiz_log_auditing/config.ts` (TYPESCRIPT) | Magnitude: 14.64 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, import: 3, branch: 2, api: 1
- `ui/features/context_modules_v2/react/dnd/types.ts` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, api: 2, class_start: 1
- `app/serializers/live_events/event_serializer_provider.rb` (RUBY) | Magnitude: 3.26 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, class_start: 3, safety: 3
- `ui/shared/block-editor/react/assets/internal-icons/index.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, import: 10, indent_spaces: 10, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/stylesheets/components/_publish-state.scss` (CSS) | Magnitude: 0.85 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 72, class_start: 33, closures: 13
- `ui/shared/block-content-editor/react/AddBlock/block-data.tsx` (TYPESCRIPT) | Magnitude: 16.86 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 10, import: 9, api: 1
- `spec/models/content_migration/course_copy_outcomes_spec.rb` (RUBY) | Magnitude: 167.14 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 324, state_mutation: 105, test: 74, core_var_decl: 72
- `app/controllers/quizzes/quiz_submission_files_controller.rb` (RUBY) | Magnitude: 10.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 3, io: 3, state_mutation: 3
- `config/initializers/prosopite.rb` (RUBY) | Magnitude: 4.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 2, branch: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `ui/shared/canvas-media-player/react/CanvasMediaPlayer.jsx` (JAVASCRIPT) | Magnitude: 191.7 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 273, ui_framework: 65, core_var_decl: 57, branch: 55
- `ui/shared/temporary-enrollment/react/TempEnrollView.tsx` (TYPESCRIPT) | Magnitude: 153.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 273, structural_boundaries: 72, core_var_decl: 67, ui_framework: 57
- `lib/plannable.rb` (RUBY) | Magnitude: 401.26 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 336, branch: 95, state_mutation: 71, core_var_decl: 57
- `ui/features/new_login/pages/register/Teacher.tsx` (TYPESCRIPT) | Magnitude: 128.42 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 226, core_var_decl: 81, branch: 53, design_camel_case: 52
- `lib/gradebook_exporter.rb` (RUBY) | Magnitude: 590.54 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 395, state_mutation: 150, branch: 104, core_var_decl: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ui/shared/dashboard-card/react/DashboardCardMenu.tsx` (TYPESCRIPT) | Magnitude: 36.8 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 171, core_var_decl: 63, design_camel_case: 50, structural_boundaries: 31
- `ui/boot/initializers/__tests__/router.test.tsx` (TYPESCRIPT) | Magnitude: 19.62 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, test: 12, args: 11
- `ui/shared/canvas-file-upload/react/components/CanvasFilesBrowser/TableFiles.tsx` (TYPESCRIPT) | Magnitude: 68.68 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 45, core_var_decl: 41, ui_framework: 31
- `ui/features/blueprint_course_master/react/components/__tests__/CourseSidebar.test.tsx` (TYPESCRIPT) | Magnitude: 83.94 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 196, core_var_decl: 62, structural_boundaries: 59, design_snake_case: 59
- `ui/features/lti_registrations/manage/lti_1p3_registration_form/__tests__/Lti1p3RegistrationWizardEulaNavigation.test.tsx` (TYPESCRIPT) | Magnitude: 8.0 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 15, test: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `ui/shared/assignments/react/CreateEditAllocationRuleModal.tsx` (TYPESCRIPT) | Magnitude: 431.08 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 779, branch: 202, core_var_decl: 182, structural_boundaries: 135
- `ui/features/content_shares/react/ReceivedTable.tsx` (TYPESCRIPT) | Magnitude: 113.5 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 46, core_var_decl: 45, generics: 43
- `lib/data_fixup/add_attachment_associations_to_all_assets.rb` (RUBY) | Magnitude: 144.38 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 141, branch: 37, core_var_decl: 29, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `ui/features/account_admin_tools/backbone/views/UserSearchResultsView.js` (JAVASCRIPT) | Magnitude: 46.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, branch: 12, state_mutation: 9
- `ui/shared/backbone/Model/computedAttributes.js` (JAVASCRIPT) | Magnitude: 15.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, args: 6, branch: 4
- `ui/shared/due-dates/backbone/views/__tests__/DueDateOverrideView.test.js` (JAVASCRIPT) | Magnitude: 27.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 118, test: 41, structural_boundaries: 25, args: 20
- `spec/models/conditional_release/assignment_set_action_spec.rb` (RUBY) | Magnitude: 50.92 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 33, test: 31, core_var_decl: 22
- `ui/features/quiz_log_auditing/react/components/answer_matrix/inverted_table.tsx` (TYPESCRIPT) | Magnitude: 21.28 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 62, core_var_decl: 18, structural_boundaries: 14, safety_bypasses: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `config/initializers/inst_access_support.rb` (RUBY) | Magnitude: 32.34 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 34, branch: 7, state_mutation: 6, structural_boundaries: 5
- `lib/cc/importer/canvas/quiz_metadata_converter.rb` (RUBY) | Magnitude: 64.98 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 77, state_mutation: 21, branch: 8, closures: 8
- `app/models/accessibility/css_attributes_helper.rb` (RUBY) | Magnitude: 85.54 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, branch: 21, structural_boundaries: 21, core_var_decl: 14
- `ui/shared/block-editor/react/utils/buildPageContent.tsx` (TYPESCRIPT) | Magnitude: 60.52 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 19, branch: 11, state_mutation: 9
- `ui/shared/block-editor/react/utils/renderNodeHelpers.ts` (TYPESCRIPT) | Magnitude: 76.2 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 41, branch: 28, core_var_decl: 19, structural_boundaries: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/controllers/application_controller.rb` -> Churn: **95.49%** | Cog Load: 76.514% | Debt: 50.8532%
- `app/controllers/users_controller.rb` -> Churn: **93.46%** | Cog Load: 48.5869% | Debt: 72.6763%
- `app/controllers/courses_controller.rb` -> Churn: **89.13%** | Cog Load: 72.6015% | Debt: 34.1846%
- `app/models/account.rb` -> Churn: **88.82%** | Cog Load: 70.5882% | Debt: 7.7321%
- `app/models/course.rb` -> Churn: **83.5%** | Cog Load: 91.9861% | Debt: 7.7592%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/services/rubric_llm_service.rb` -> **Laszlo Sipula** (100.0% isolated ownership) | Magnitude: 9106.34
- `config/initializers/active_record.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 2831.76
- `ui/features/quizzes/jquery/quizzes.jsx` -> **Adrian Gruber** (100.0% isolated ownership) | Magnitude: 2733.5
- `ui/features/syllabus_revisions/react/__tests__/SyllabusRevisionsTray.test.tsx` -> **Eric Saupe** (100.0% isolated ownership) | Magnitude: 1932.56
- `ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/__tests__/Preview.test.tsx` -> **viktor.szpisjak** (100.0% isolated ownership) | Magnitude: 1725.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/sis/csv/import_refactored.rb` -> **Severity: 0.064** (Bridge: 0.0006 * Flux: 100.0%)
- `app/models/sis_batch.rb` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 100.0%)
- `app/models/course.rb` -> **Severity: 0.061** (Bridge: 0.0006 * Flux: 99.9998%)
- `config/initializers/active_record.rb` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 100.0%)
- `gems/event_stream/lib/event_stream/index_strategy/active_record.rb` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `spec/selenium/test_setup/selenium_driver_setup.rb` -> **Severity: 2.932** (Embedded: 0.0476 * Error Risk: 61.5669%)
- `config/initializers/active_record.rb` -> **Severity: 2.8** (Embedded: 0.0362 * Error Risk: 77.4048%)
- `app/models/setting.rb` -> **Severity: 2.309** (Embedded: 0.0398 * Error Risk: 57.9599%)
- `gems/canvas_ext/lib/canvas_ext/array.rb` -> **Severity: 2.307** (Embedded: 0.0425 * Error Risk: 54.2752%)
- `lib/user_content.rb` -> **Severity: 2.306** (Embedded: 0.029 * Error Risk: 79.391%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `spec/selenium/test_setup/selenium_driver_setup.rb` -> **Severity: 952.3** (Blast Radius: 9.523 * Doc Risk: 100.0%)
- `gems/adheres_to_policy/spec/spec_helper.rb` -> **Severity: 586.8** (Blast Radius: 5.868 * Doc Risk: 100.0%)
- `gems/canvas_ext/lib/canvas_ext/array.rb` -> **Severity: 493.2** (Blast Radius: 4.932 * Doc Risk: 100.0%)
- `app/models/plugin_setting.rb` -> **Severity: 473.6** (Blast Radius: 4.736 * Doc Risk: 100.0%)
- `app/models/setting.rb` -> **Severity: 473.2** (Blast Radius: 4.732 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 5464 literal sites + 41 sites through wrappers = 5505
- **`panics_and_aborts`:** 4070 literal sites + 70 sites through wrappers = 4140

- `docx_replace` (function, debug_prints, primitive): 20 call sites in 1 files -- `app/presenters/course_pace_presenter.rb`
- `element_value_for_attr` (function, panics_and_aborts, primitive): 12 call sites in 9 files -- `spec/selenium/test_setup/common_helper_methods/custom_selenium_actions.rb`
- `raise_and_disable_group` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `lib/microsoft_sync/syncer_steps.rb`
- `execute` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `config/initializers/postgresql_adapter.rb`
- `fail_import` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `app/models/group_and_membership_importer.rb`
- `pace_in_context` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `app/services/course_pacing/pace_service.rb`
- `raise_context_error` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `lib/user_search.rb`
- `course_for` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `app/services/course_pacing/pace_service.rb`
- `setAdaState` (function, debug_prints, primitive): 3 call sites in 1 files -- `ui/shared/help-dialog/react/AdaChatbot.tsx`
- `template_pace_for` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `app/services/course_pacing/pace_service.rb`
- `attachment_with_rows` (function, debug_prints, primitive): 2 call sites in 1 files -- `spec/lib/gradebook_importer_spec.rb`
- `batch_aborted` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `app/models/sis_batch.rb`
*(+33 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 355216 call pairs -- scoped 12.1%, unique 0.7%, ambiguous 42.8%, external 44.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| ruby | 258701 | 10.2% | 0.9% | 47.5% | 41.4% |
| javascript | 51727 | 15.3% | 0.0% | 33.6% | 51.0% |
| typescript | 44115 | 19.4% | 0.0% | 26.4% | 54.2% |
| shell | 477 | 32.7% | 10.3% | 1.5% | 55.6% |
| groovy | 137 | 0.7% | 0.0% | 0.0% | 99.3% |
| html | 41 | 2.4% | 0.0% | 0.0% | 97.6% |
| lua | 18 | 0.0% | 0.0% | 0.0% | 100.0% |

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
