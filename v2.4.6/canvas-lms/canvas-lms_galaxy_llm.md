# ARCHITECTURAL_BRIEF: canvas-lms
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/canvas-lms` |
| **Timestamp** | `2026-08-03T20:01:39.813742+00:00` |
| **Scan Duration** | `40.32s` |
| **Git Branch** | `master` |
| **Git Commit** | `24ea71c7a99edd7393a4e2ab3572b1c2d6214605` |
| **Git Remote** | `https://github.com/instructure/canvas-lms.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8726 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 22519 |
| Analyzed Artifacts (Scanned) | 11820 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10699 |
| Total LOC | 951084 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 52.5% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1066 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1253 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3909 | 381426 | 33.1% |
| JAVASCRIPT | 2657 | 247137 | 22.5% |
| RUBY | 2113 | 204361 | 17.9% |
| HTML | 857 | 42865 | 7.3% |
| XML | 639 | 370 | 5.4% |
| PLAINTEXT | 510 | 3 | 4.3% |
| CSS | 409 | 43192 | 3.5% |
| JSON | 402 | 20877 | 3.4% |
| MARKDOWN | 161 | 0 | 1.4% |
| YAML | 115 | 8330 | 1.0% |
| SHELL | 38 | 1700 | 0.3% |
| DOCKERFILE | 6 | 143 | 0.1% |
| GROOVY | 2 | 535 | 0.0% |
| LUA | 1 | 26 | 0.0% |
| CSV | 1 | 119 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.317`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7069 | 59.8% |
| file_cluster_13 | 2903 | 24.6% |
| file_cluster_2 | 414 | 3.5% |
| file_cluster_17 | 278 | 2.4% |
| file_cluster_0 | 148 | 1.3% |
| file_cluster_4 | 138 | 1.2% |
| file_cluster_11 | 35 | 0.3% |
| file_cluster_16 | 34 | 0.3% |
| file_cluster_9 | 7 | 0.1% |
| file_cluster_12 | 6 | 0.1% |
| file_cluster_15 | 5 | 0.0% |
| Unknown | 3 | 0.0% |
| file_cluster_6 | 3 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 668 | 5.7% |
| Static: Minified & Vendor Opaque Mass | 108 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10699*

**Composition by Extension & Reason:**
- `.rb`: 4628x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 47 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1423 LOC)
- `.tsx`: 1225x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 24 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 55 LOC)
- `.jsx`: 1063x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 89 exceeds 500 chars), 1x Excluded (Saturation: Line 58 exceeds 500 chars)
- `.js`: 749x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 56x Excluded (Saturation: Line 21 exceeds 500 chars), 44x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.png`: 630x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 539x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3125 LOC), 1x Excluded (Static Asset Blob without Intent: 1583 LOC)
- `.ts`: 279x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 20 exceeds 500 chars)
- `.handlebars`: 230x Excluded (Unsupported Extension: '.handlebars')
- `no_extension`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.package-translations'), 1x Excluded (Unsupported Extension: '.jenkins-cache')
- `.gif`: 101x Excluded (Explicitly Denied Extension: '.gif')
- `.sh`: 94x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xss`: 94x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 92x Excluded (Explicitly Denied Extension: '.zip')
- `.yml`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Monolithic Amalgamation: 41511 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 43287 LOC exceeds safe regex boundaries)
- `.gemspec`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 18.3 | 8.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.9 | 2.3 | 0.0 |
| API Exposure | 0.0 | 18.6 | 2.9 | 2.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 84.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 95.5 | 3.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.6 | 17.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 36.4 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/models/course.rb` (Hits: 312)
- `config/routes.rb` (Hits: 287)
- `app/models/user.rb` (Hits: 276)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AlertManager.tsx** (`ui/shared/alerts/react/AlertManager.tsx`) — 69 inbound connections
2. **globalUtils.ts** (`ui/shared/util/globalUtils.ts`) — 63 inbound connections
3. **InstuiModal.tsx** (`ui/shared/instui-bindings/react/InstuiModal.tsx`) — 62 inbound connections
4. **tinymce.scss** (`app/stylesheets/bundles/tinymce.scss`) — 54 inbound connections
5. **date-functions.js** (`ui/shared/datetime/date-functions.js`) — 54 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **featureBundles.ts** (`ui/featureBundles.ts`) — 212 outbound dependencies
2. **Gradebook.tsx** (`ui/features/gradebook/react/default_gradebook/Gradebook.tsx`) — 97 outbound dependencies
3. **getTranslations.js** (`packages/canvas-rce/src/getTranslations.js`) — 77 outbound dependencies
4. **getTranslations.js** (`packages/canvas-media/src/getTranslations.js`) — 76 outbound dependencies
5. **common.scss** (`app/stylesheets/bundles/common.scss`) — 72 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `AbstractAssignment_[Truncated]` (@ `app/models/abstract_assignment.rb`) -> Impact: **9237.4** | LOC: 4775
- `custom_visibility_option_[Truncated]` (@ `app/models/course.rb`) -> Impact: **9044.4** | LOC: 4115
- `DiscussionTopic_[Truncated]` (@ `app/models/discussion_topic.rb`) -> Impact: **5911.7** | LOC: 2325
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...
- `UsersController_[Truncated]` (@ `app/controllers/users_controller.rb`) -> Impact: **5191.1** | LOC: 3553
  * *Intent:* # "avatar_image_url": { # "description": "A URL to retrieve a generic avatar.", # "example": "https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443...
- `ensure_grader_can_grade` (@ `app/models/submission.rb`) -> Impact: **5068.4** | LOC: 1505
- `infer_namespace` (@ `app/models/attachment.rb`) -> Impact: **4621.3** | LOC: 1978
- `Account` (@ `app/models/account.rb`) -> Impact: **4600.9** | LOC: 1327
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...
- `ContentTag` (@ `app/models/content_tag.rb`) -> Impact: **4445.0** | LOC: 877
  * *Intent:* # This file is part of Canvas. # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Publi...
- `avatar_location_[Truncated]` (@ `app/models/user.rb`) -> Impact: **4194.4** | LOC: 2291
- `accept_enrollment` (@ `app/controllers/courses_controller.rb`) -> Impact: **3945.4** | LOC: 828
  * *Intent:* # Internal: Accept an enrollment invitation and redirect. # # enrollment - An enrollment object to accept. # # Returns nothing.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `create` (@ `app/controllers/assignments_api_controller.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z. # # @argument assignment[peer_review][lock_at] [DateTime] # The day/time the peer revie...
- `syllabus` (@ `app/controllers/assignments_controller.rb`) -> **O(2^N) [Recursive]**
- `render_a2_student_view` (@ `app/controllers/assignments_controller.rb`) -> **O(2^N) [Recursive]**
- `create` (@ `app/controllers/conferences_controller.rb`) -> **O(2^N) [Recursive]**
- `update` (@ `app/controllers/conferences_controller.rb`) -> **O(2^N) [Recursive]**
- `close` (@ `app/controllers/conferences_controller.rb`) -> **O(2^N) [Recursive]**
- `accept_enrollment` (@ `app/controllers/courses_controller.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Internal: Accept an enrollment invitation and redirect. # # enrollment - An enrollment object to accept. # # Returns nothing.
- `settings` (@ `app/controllers/courses_controller.rb`) -> **O(2^N) [Recursive]**
- `user` (@ `app/controllers/courses_controller.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # @API Get single user # Return information on a single user. # # Accepts the same include[] parameters as the :users: action, and returns a # single ...
- `speed_grader` (@ `app/controllers/gradebooks_controller.rb`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `InitCanvasDb_[Truncated]` (@ `db/migrate/20101210192618_init_canvas_db.rb`) -> DB Complexity: **799**
  * *Intent:* # # Canvas is distributed in the hope that it will be useful, but WITHOUT ANY # WARRANTY; without even the implied warranty of MERCHANTABILITY or FITN...
- `AbstractAssignment_[Truncated]` (@ `app/models/abstract_assignment.rb`) -> DB Complexity: **660**
- `custom_visibility_option_[Truncated]` (@ `app/models/course.rb`) -> DB Complexity: **643**
- `bindGridEvents` (@ `ui/features/gradebook/react/default_gradebook/Gradebook.tsx`) -> DB Complexity: **445**
- `Datepicker` (@ `packages/jqueryui/datepicker.js`) -> DB Complexity: **434**
- `avatar_location_[Truncated]` (@ `app/models/user.rb`) -> DB Complexity: **411**
- `DiscussionTopic_[Truncated]` (@ `app/models/discussion_topic.rb`) -> DB Complexity: **393**
  * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Public License as published by the F...
- `_setOption` (@ `packages/jqueryui/sortable.js`) -> DB Complexity: **390**
- `infer_namespace` (@ `app/models/attachment.rb`) -> DB Complexity: **375**
- `SplitUsers_[Truncated]` (@ `app/models/split_users.rb`) -> DB Complexity: **346**
  * *Intent:* # This file is part of Canvas. # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Affero General Publi...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `app/models` | 288 | 176468.94 | 23.31% | 58.16% |
| `app/controllers` | 195 | 107772.8 | 29.05% | 48.19% |
| `app/helpers` | 71 | 17082.54 | 24.4% | 68.83% |
| `app/models/importers` | 32 | 15231.3 | 30.4% | 45.38% |
| `app/graphql/types` | 182 | 15165.16 | 10.66% | 39.24% |
| `packages/jqueryui` | 18 | 13701.28 | 64.91% | 46.0% |
| `config/initializers` | 84 | 13632.9 | 10.75% | 41.68% |
| `config/saml` | 2 | 10000.0 | 0.0% | 0.0% |
| `app/models/quizzes` | 28 | 8078.64 | 22.69% | 64.38% |
| `app/graphql/mutations` | 108 | 7874.56 | 23.43% | 82.06% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Gemfile.d/i18n_tools_and_rake_tasks.rb` -> **100.0%** Exposure
- `Rakefile` -> **100.0%** Exposure
- `app/controllers/account_grading_settings_controller.rb` -> **100.0%** Exposure
- `app/controllers/anonymous_provisional_grades_controller.rb` -> **100.0%** Exposure
- `app/controllers/concerns/student_enrollment_helper.rb` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `app/controllers/anonymous_submissions_controller.rb` -> **100.0%** Exposure
- `app/controllers/concerns/k5_mode.rb` -> **100.0%** Exposure
- `app/controllers/course_pacing/section_paces_api_controller.rb` -> **100.0%** Exposure
- `app/controllers/course_pacing/student_enrollment_paces_api_controller.rb` -> **100.0%** Exposure
- `app/controllers/eportfolio_entries_controller.rb` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `config/routes.rb` -> **0** Orphaned Functions | **84** Duplicates
- `doc/api/fulldoc/html/js/swagger-ui.js` -> **0** Orphaned Functions | **81** Duplicates
- `packages/canvas-media/src/closedCaptionLanguages.js` -> **0** Orphaned Functions | **63** Duplicates
- `ui/features/quizzes/jquery/calcCmd.js` -> **0** Orphaned Functions | **41** Duplicates
- `app/models/content_migration.rb` -> **28** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`app/controllers/accounts_controller.rb`** -> AI Confidence: **99.48%**
2. **`app/controllers/application_controller.rb`** -> AI Confidence: **99.48%**
3. **`app/controllers/assignments_controller.rb`** -> AI Confidence: **99.48%**
4. **`app/controllers/courses_controller.rb`** -> AI Confidence: **99.48%**
5. **`app/controllers/discussion_topics_controller.rb`** -> AI Confidence: **99.48%**
6. **`app/controllers/gradebooks_controller.rb`** -> AI Confidence: **99.48%**
7. **`app/controllers/learning_object_dates_controller.rb`** -> AI Confidence: **99.48%**
8. **`app/controllers/profile_controller.rb`** -> AI Confidence: **99.48%**
9. **`app/controllers/quizzes/quizzes_controller.rb`** -> AI Confidence: **99.48%**
10. **`app/controllers/submissions_api_controller.rb`** -> AI Confidence: **99.48%**
11. **`app/controllers/users_controller.rb`** -> AI Confidence: **99.48%**
12. **`app/models/calendar_event.rb`** -> AI Confidence: **99.48%**
13. **`app/controllers/assignments_api_controller.rb`** -> AI Confidence: **99.39%**
14. **`app/controllers/context_modules_controller.rb`** -> AI Confidence: **99.39%**
15. **`app/controllers/conversations_controller.rb`** -> AI Confidence: **99.39%**
16. **`app/controllers/group_categories_controller.rb`** -> AI Confidence: **99.39%**
17. **`app/graphql/types/user_type.rb`** -> AI Confidence: **99.39%**
18. **`app/models/abstract_assignment.rb`** -> AI Confidence: **99.39%**
19. **`app/models/attachment.rb`** -> AI Confidence: **99.39%**
20. **`app/models/course.rb`** -> AI Confidence: **99.39%**
21. **`app/models/discussion_topic.rb`** -> AI Confidence: **99.39%**
22. **`app/models/quizzes/quiz.rb`** -> AI Confidence: **99.39%**
23. **`app/models/submission.rb`** -> AI Confidence: **99.39%**
24. **`app/models/wiki_page.rb`** -> AI Confidence: **99.39%**
25. **`ui/features/inbox/react/containers/AddressBookContainer/AddressBookContainer.jsx`** -> AI Confidence: **99.39%**
26. **`ui/features/inbox/react/containers/ComposeModalContainer/ComposeModalManager.jsx`** -> AI Confidence: **99.39%**
27. **`ui/shared/calendar/jquery/CommonEvent/index.js`** -> AI Confidence: **99.39%**
28. **`ui/features/discussion_topic_edit_v2/react/components/DiscussionTopicForm/DiscussionTopicForm.tsx`** -> AI Confidence: **99.39%**
29. **`ui/features/discussion_topics_post/react/components/AssignmentAvailabilityContainer/AssignmentAvailabilityContainer.tsx`** -> AI Confidence: **99.39%**
30. **`ui/features/discussion_topics_post/react/components/AuthorInfo/NameLink.tsx`** -> AI Confidence: **99.39%**
31. **`ui/features/discussion_topics_post/react/components/DiscussionTopicAlertManager/DiscussionTopicAlertManager.tsx`** -> AI Confidence: **99.39%**
32. **`app/controllers/outcome_results_controller.rb`** -> AI Confidence: **99.35%**
33. **`app/helpers/application_helper.rb`** -> AI Confidence: **99.35%**
34. **`app/models/account.rb`** -> AI Confidence: **99.35%**
35. **`app/models/user.rb`** -> AI Confidence: **99.35%**
36. **`ui/features/user/index.tsx`** -> AI Confidence: **99.35%**
37. **`app/controllers/calendar_events_api_controller.rb`** -> AI Confidence: **99.34%**
38. **`app/controllers/context_controller.rb`** -> AI Confidence: **99.34%**
39. **`app/controllers/enrollments_api_controller.rb`** -> AI Confidence: **99.34%**
40. **`app/controllers/files_controller.rb`** -> AI Confidence: **99.34%**
41. **`app/controllers/submissions_base_controller.rb`** -> AI Confidence: **99.34%**
42. **`app/models/conversation.rb`** -> AI Confidence: **99.34%**
43. **`app/models/speed_grader/assignment.rb`** -> AI Confidence: **99.34%**
44. **`app/controllers/calendars_controller.rb`** -> AI Confidence: **99.32%**
45. **`app/controllers/canvadoc_sessions_controller.rb`** -> AI Confidence: **99.32%**
46. **`app/controllers/media_objects_controller.rb`** -> AI Confidence: **99.32%**
47. **`app/controllers/sections_controller.rb`** -> AI Confidence: **99.32%**
48. **`app/controllers/submissions/previews_base_controller.rb`** -> AI Confidence: **99.32%**
49. **`app/graphql/mutations/create_discussion_topic.rb`** -> AI Confidence: **99.32%**
50. **`app/graphql/mutations/update_discussion_topic.rb`** -> AI Confidence: **99.32%**
51. **`script/bundle_update`** -> AI Confidence: **99.32%**
52. **`packages/canvas-rce/webpack.shared.config.js`** -> AI Confidence: **99.32%**
53. **`ui/features/new_user_tutorial/react/trays/ZoomTray.jsx`** -> AI Confidence: **99.32%**
54. **`ui/shared/util/templateData.js`** -> AI Confidence: **99.32%**
55. **`app/graphql/types/query_type.rb`** -> AI Confidence: **99.31%**
56. **`app/models/conversation_message.rb`** -> AI Confidence: **99.31%**
57. **`app/models/message.rb`** -> AI Confidence: **99.31%**
58. **`config/application.rb`** -> AI Confidence: **99.31%**
59. **`config/initializers/active_record.rb`** -> AI Confidence: **99.31%**
60. **`config/initializers/i18n.rb`** -> AI Confidence: **99.31%**
61. **`doc/api/fulldoc/html/setup.rb`** -> AI Confidence: **99.31%**
62. **`doc/api/fulldoc/markdown/setup.rb`** -> AI Confidence: **99.31%**
63. **`packages/canvas-media/src/getTranslations.js`** -> AI Confidence: **99.31%**
64. **`packages/canvas-media/src/shared/CanvasSelect.jsx`** -> AI Confidence: **99.31%**
65. **`packages/canvas-rce/src/enhance-user-content/enhance_user_content.js`** -> AI Confidence: **99.31%**
66. **`packages/canvas-rce/src/getTranslations.js`** -> AI Confidence: **99.31%**
67. **`packages/canvas-rce/src/rce/plugins/instructure_icon_maker/svg/settings.js`** -> AI Confidence: **99.31%**
68. **`packages/canvas-rce/src/rce/plugins/instructure_image/ImageOptionsTray/index.jsx`** -> AI Confidence: **99.31%**
69. **`packages/canvas-rce/src/rce/plugins/instructure_links/components/Link.jsx`** -> AI Confidence: **99.31%**
70. **`packages/canvas-rce/src/rce/plugins/instructure_links/components/LinksPanel.jsx`** -> AI Confidence: **99.31%**
71. **`packages/canvas-rce/src/rce/plugins/instructure_record/AudioOptionsTray/TrayController.jsx`** -> AI Confidence: **99.31%**
72. **`packages/canvas-rce/src/rce/plugins/instructure_record/VideoOptionsTray/index.jsx`** -> AI Confidence: **99.31%**
73. **`packages/canvas-rce/src/rce/plugins/shared/ColorInput.jsx`** -> AI Confidence: **99.31%**
74. **`packages/canvas-rce/src/rce/plugins/shared/Filter.jsx`** -> AI Confidence: **99.31%**
75. **`ui/features/account_course_user_search/react/components/SearchMessage.jsx`** -> AI Confidence: **99.31%**
76. **`ui/features/account_course_user_search/react/components/SearchableSelect.jsx`** -> AI Confidence: **99.31%**
77. **`ui/features/account_course_user_search/react/components/UsersListHeader.jsx`** -> AI Confidence: **99.31%**
78. **`ui/features/account_settings/jquery/index.jsx`** -> AI Confidence: **99.31%**
79. **`ui/features/assignment_edit/backbone/views/EditView.jsx`** -> AI Confidence: **99.31%**
80. **`ui/features/assignment_edit/index.js`** -> AI Confidence: **99.31%**
81. **`ui/features/assignment_grade_summary/react/components/FlashMessageHolder.js`** -> AI Confidence: **99.31%**
82. **`ui/features/assignment_index/backbone/views/CreateAssignmentViewAdapter.jsx`** -> AI Confidence: **99.31%**
83. **`ui/features/assignment_index/backbone/views/CreateGroupView.jsx`** -> AI Confidence: **99.31%**
84. **`ui/features/assignments_show_student/react/components/AssignmentDetails.jsx`** -> AI Confidence: **99.31%**
85. **`ui/features/assignments_show_student/react/components/AttemptType/FileUpload.jsx`** -> AI Confidence: **99.31%**
86. **`ui/features/assignments_show_student/react/components/AttemptType/UrlEntry.jsx`** -> AI Confidence: **99.31%**
87. **`ui/features/assignments_show_student/react/components/GradeDisplay.jsx`** -> AI Confidence: **99.31%**
88. **`ui/features/assignments_show_student/react/components/Header.jsx`** -> AI Confidence: **99.31%**
89. **`ui/features/assignments_show_student/react/components/StepContainer.jsx`** -> AI Confidence: **99.31%**
90. **`ui/features/calendar/backbone/views/EditAssignmentDetails.js`** -> AI Confidence: **99.31%**
91. **`ui/features/calendar/jquery/EditAppointmentGroupDetails.js`** -> AI Confidence: **99.31%**
92. **`ui/features/calendar/jquery/EditEventDetailsDialog.js`** -> AI Confidence: **99.31%**
93. **`ui/features/calendar/jquery/index.js`** -> AI Confidence: **99.31%**
94. **`ui/features/content_migrations/backbone/views/ContentCheckboxView.js`** -> AI Confidence: **99.31%**
95. **`ui/features/dashboard/react/DashboardHeader.jsx`** -> AI Confidence: **99.31%**
96. **`ui/features/developer_keys_v2/react/ActionButtons.jsx`** -> AI Confidence: **99.31%**
97. **`ui/features/developer_keys_v2/react/InheritanceStateControl.jsx`** -> AI Confidence: **99.31%**
98. **`ui/features/developer_keys_v2/react/ManualConfigurationForm/RequiredValues.jsx`** -> AI Confidence: **99.31%**
99. **`ui/features/discussion_topics_post/graphql/Mocks.js`** -> AI Confidence: **99.31%**
100. **`ui/features/discussion_topics_post/react/utils/index.js`** -> AI Confidence: **99.31%**
101. **`ui/features/external_apps/react/components/ExternalToolsTableRow.jsx`** -> AI Confidence: **99.31%**
102. **`ui/features/files/MasterCourseLock.jsx`** -> AI Confidence: **99.31%**
103. **`ui/features/files/react/components/Breadcrumbs.jsx`** -> AI Confidence: **99.31%**
104. **`ui/features/files/react/legacy/components/ShowFolder.js`** -> AI Confidence: **99.31%**
105. **`ui/features/grade_summary/index.js`** -> AI Confidence: **99.31%**
106. **`ui/features/grade_summary/jquery/index.jsx`** -> AI Confidence: **99.31%**
107. **`ui/features/gradebook_uploads/jquery/index.js`** -> AI Confidence: **99.31%**
108. **`ui/features/k5_course/react/GradeRow.jsx`** -> AI Confidence: **99.31%**
109. **`ui/features/k5_course/react/GradesPage.jsx`** -> AI Confidence: **99.31%**
110. **`ui/features/k5_course/react/K5Course.jsx`** -> AI Confidence: **99.31%**
111. **`ui/features/k5_dashboard/react/K5DashboardCard.jsx`** -> AI Confidence: **99.31%**
112. **`ui/features/new_user_tutorial/react/util/getProperTray.js`** -> AI Confidence: **99.31%**
113. **`ui/features/outcome_management/react/Alignments/AlignmentItem.jsx`** -> AI Confidence: **99.31%**
114. **`ui/features/outcome_management/react/Alignments/AlignmentOutcomeItem.jsx`** -> AI Confidence: **99.31%**
115. **`ui/features/outcome_management/react/Alignments/AlignmentStatItem.jsx`** -> AI Confidence: **99.31%**
116. **`ui/features/outcome_management/react/Alignments/AlignmentSummaryHeader.jsx`** -> AI Confidence: **99.31%**
117. **`ui/features/outcome_management/react/FindOutcomeItem.jsx`** -> AI Confidence: **99.31%**
118. **`ui/features/outcome_management/react/FindOutcomesModal.jsx`** -> AI Confidence: **99.31%**
119. **`ui/features/outcome_management/react/FindOutcomesView.jsx`** -> AI Confidence: **99.31%**
120. **`ui/features/outcome_management/react/Management/GroupEditModal.jsx`** -> AI Confidence: **99.31%**
121. **`ui/features/outcome_management/react/Management/GroupRemoveModal.jsx`** -> AI Confidence: **99.31%**
122. **`ui/features/outcome_management/react/Management/ManageOutcomesFooter.jsx`** -> AI Confidence: **99.31%**
123. **`ui/features/outcome_management/react/Management/ManageOutcomesView.jsx`** -> AI Confidence: **99.31%**
124. **`ui/features/outcome_management/react/Management/OutcomeEditModal.jsx`** -> AI Confidence: **99.31%**
125. **`ui/features/outcome_management/react/Management/OutcomeKebabMenu.jsx`** -> AI Confidence: **99.31%**
126. **`ui/features/outcome_management/react/Management/OutcomeMoveModal.jsx`** -> AI Confidence: **99.31%**
127. **`ui/features/outcome_management/react/MasteryCalculation/ProficiencyCalculation.jsx`** -> AI Confidence: **99.31%**
128. **`ui/features/outcome_management/react/MasteryScale/index.jsx`** -> AI Confidence: **99.31%**
129. **`ui/features/outcome_management/react/shared/GroupActionDrillDown.jsx`** -> AI Confidence: **99.31%**
130. **`ui/features/question_bank/jquery/index.js`** -> AI Confidence: **99.31%**
131. **`ui/features/section/jquery/index.jsx`** -> AI Confidence: **99.31%**
132. **`ui/features/submit_assignment/jquery/index.jsx`** -> AI Confidence: **99.31%**
133. **`ui/features/wiki_page_index/backbone/views/WikiPageIndexItemView.js`** -> AI Confidence: **99.31%**
134. **`ui/shared/add-people/react/components/add_people.jsx`** -> AI Confidence: **99.31%**
135. **`ui/shared/add-people/react/components/duplicate_section.jsx`** -> AI Confidence: **99.31%**
136. **`ui/shared/assignments/backbone/models/Assignment.js`** -> AI Confidence: **99.31%**
137. **`ui/shared/assignments/backbone/views/GradingTypeSelector.jsx`** -> AI Confidence: **99.31%**
138. **`ui/shared/assignments/react/CommentsTray/CommentContent.jsx`** -> AI Confidence: **99.31%**
139. **`ui/shared/canvas-media-player/react/CanvasMediaPlayer.jsx`** -> AI Confidence: **99.31%**
140. **`ui/shared/context-modules/jquery/index.jsx`** -> AI Confidence: **99.31%**
141. **`ui/shared/context-modules/jquery/utils.jsx`** -> AI Confidence: **99.31%**
142. **`ui/shared/datetime/jquery/DatetimeField.js`** -> AI Confidence: **99.31%**
143. **`ui/shared/datetime/react/components/DateTimeInput.jsx`** -> AI Confidence: **99.31%**
144. **`ui/shared/direct-sharing/react/components/DirectShareCoursePanel.jsx`** -> AI Confidence: **99.31%**
145. **`ui/shared/due-dates/backbone/views/DueDateOverride.jsx`** -> AI Confidence: **99.31%**
146. **`ui/shared/due-dates/util/differentiatedModulesUtil.jsx`** -> AI Confidence: **99.31%**
147. **`ui/shared/enhanced-user-content/react/showFilePreview.jsx`** -> AI Confidence: **99.31%**
148. **`ui/shared/files/backbone/models/Folder.js`** -> AI Confidence: **99.31%**
149. **`ui/shared/files/react/components/FilePreview.jsx`** -> AI Confidence: **99.31%**
150. **`ui/shared/files/react/components/PublishCloud.jsx`** -> AI Confidence: **99.31%**
151. **`ui/shared/group-modal/react/index.jsx`** -> AI Confidence: **99.31%**
152. **`ui/shared/groups/backbone/views/GroupCategorySelector.js`** -> AI Confidence: **99.31%**
153. **`ui/shared/handlebars-helpers/index.js`** -> AI Confidence: **99.31%**
154. **`ui/shared/integrations/react/courses/IntegrationRow.jsx`** -> AI Confidence: **99.31%**
155. **`ui/shared/k5/react/ResourcesPage.jsx`** -> AI Confidence: **99.31%**
156. **`ui/shared/mastery-path-toggle/react/MasteryPathToggle.jsx`** -> AI Confidence: **99.31%**
157. **`ui/shared/media-comments/jquery/index.js`** -> AI Confidence: **99.31%**
158. **`ui/shared/module-sequence-footer/jquery/index.jsx`** -> AI Confidence: **99.31%**
159. **`ui/shared/outcomes/content-view/backbone/views/OutcomeGroupView.js`** -> AI Confidence: **99.31%**
160. **`ui/shared/planner/dynamic-ui/animations/scroll-to-today.js`** -> AI Confidence: **99.31%**
161. **`ui/shared/rce/plugins/canvas_mentions/components/MentionAutoComplete/MentionDropdown.jsx`** -> AI Confidence: **99.31%**
162. **`ui/shared/rce/plugins/canvas_mentions/events.jsx`** -> AI Confidence: **99.31%**
163. **`ui/shared/rce/serviceRCELoader.js`** -> AI Confidence: **99.31%**
164. **`ui/shared/rubrics/jquery/edit_rubric.jsx`** -> AI Confidence: **99.31%**
165. **`ui/shared/tree-browser-view/backbone/views/TreeBrowserView.js`** -> AI Confidence: **99.31%**
166. **`ui/shared/wiki/backbone/views/WikiPageEditView.jsx`** -> AI Confidence: **99.31%**
167. **`packages/canvas-media/src/ClosedCaptionCreatorV2/CaptionRow.tsx`** -> AI Confidence: **99.31%**
168. **`packages/canvas-media/src/ClosedCaptionCreatorV2/ManualCaptionCreator.tsx`** -> AI Confidence: **99.31%**
169. **`packages/canvas-rce/src/rce/RCE.tsx`** -> AI Confidence: **99.31%**
170. **`packages/canvas-rce/src/rce/RCEWrapper.tsx`** -> AI Confidence: **99.31%**
171. **`packages/canvas-rce/src/rce/plugins/instructure_color/components/ColorPicker.tsx`** -> AI Confidence: **99.31%**
172. **`packages/canvas-rce/src/rce/plugins/instructure_links/plugin.ts`** -> AI Confidence: **99.31%**
173. **`packages/canvas-rce/src/rce/plugins/instructure_rce_external_tools/components/ExternalToolDialog/ExternalToolDialog.tsx`** -> AI Confidence: **99.31%**
174. **`packages/canvas-rce/src/rce/plugins/shared/Upload/UploadFile.tsx`** -> AI Confidence: **99.31%**
175. **`ui/features/accessibility/accessibility_course_statistics/react/components/CoursesTableRow.tsx`** -> AI Confidence: **99.31%**
176. **`ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/Form/TextInputForm.tsx`** -> AI Confidence: **99.31%**
177. **`ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/Preview.tsx`** -> AI Confidence: **99.31%**
178. **`ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/index.tsx`** -> AI Confidence: **99.31%**
179. **`ui/features/accessibility/shared/react/hooks/useAccessibilityScansFetchUtils.ts`** -> AI Confidence: **99.31%**
180. **`ui/features/account_admin_tools/react/CourseActivityDetails.tsx`** -> AI Confidence: **99.31%**
181. **`ui/features/account_course_user_search/react/components/CreateOrUpdateUserModal.tsx`** -> AI Confidence: **99.31%**
182. **`ui/features/account_grading_settings/hooks/useAccountGradingStatuses.tsx`** -> AI Confidence: **99.31%**
183. **`ui/features/account_settings/react/AccountSettingsRoute.tsx`** -> AI Confidence: **99.31%**
184. **`ui/features/account_settings/react/components/SecurityPanel.tsx`** -> AI Confidence: **99.31%**
185. **`ui/features/ai_experiences_edit/react/AIExperienceManager.tsx`** -> AI Confidence: **99.31%**
186. **`ui/features/ai_experiences_edit/react/components/AIExperienceForm/AIExperienceForm.tsx`** -> AI Confidence: **99.31%**
187. **`ui/features/ai_experiences_index/react/components/AIExperienceRow.tsx`** -> AI Confidence: **99.31%**
188. **`ui/features/ai_experiences_show/react/components/AIExperiencePublishButton.tsx`** -> AI Confidence: **99.31%**
189. **`ui/features/ai_experiences_show/react/components/AIExperienceShow.tsx`** -> AI Confidence: **99.31%**
190. **`ui/features/assignment_edit/backbone/views/EditHeaderView.tsx`** -> AI Confidence: **99.31%**
191. **`ui/features/assignment_edit/react/PeerReviewDetails.tsx`** -> AI Confidence: **99.31%**
192. **`ui/features/assignment_grade_summary/react/components/GradesGrid/GradeSelect.tsx`** -> AI Confidence: **99.31%**
193. **`ui/features/assignment_index/react/bulk_edit/BulkDateInput.tsx`** -> AI Confidence: **99.31%**
194. **`ui/features/assignments_peer_reviews_student/react/components/RubricPanel.tsx`** -> AI Confidence: **99.31%**
195. **`ui/features/assignments_show_student/react/components/AttemptInformation.tsx`** -> AI Confidence: **99.31%**
196. **`ui/features/assignments_show_student/react/components/AttemptSelect.tsx`** -> AI Confidence: **99.31%**
197. **`ui/features/brand_configs/react/CollectionView.tsx`** -> AI Confidence: **99.31%**
198. **`ui/features/conferences/react/components/VideoConferenceModal/VideoConferenceModal.tsx`** -> AI Confidence: **99.31%**
199. **`ui/features/content_migrations/react/components/migrator_forms/course_copy.tsx`** -> AI Confidence: **99.31%**
200. **`ui/features/context_modules_v2/index.tsx`** -> AI Confidence: **99.31%**
201. **`ui/features/context_modules_v2/react/components/ModuleItemSupplementalInfo.tsx`** -> AI Confidence: **99.31%**
202. **`ui/features/context_modules_v2/react/componentsStudents/ModuleHeaderStudent.tsx`** -> AI Confidence: **99.31%**
203. **`ui/features/context_modules_v2/react/componentsStudents/ModuleItemStudent.tsx`** -> AI Confidence: **99.31%**
204. **`ui/features/context_modules_v2/react/componentsStudents/ModuleItemSupplementalInfoStudent.tsx`** -> AI Confidence: **99.31%**
205. **`ui/features/context_modules_v2/react/componentsStudents/ModulePageActionHeaderStudent.tsx`** -> AI Confidence: **99.31%**
206. **`ui/features/context_modules_v2/react/componentsTeacher/AddItemModalComponents/ExternalItemForm.tsx`** -> AI Confidence: **99.31%**
207. **`ui/features/context_modules_v2/react/componentsTeacher/ManageModuleContent/ManageModuleContentTray.tsx`** -> AI Confidence: **99.31%**
208. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleActionMenu.tsx`** -> AI Confidence: **99.31%**
209. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleHeader.tsx`** -> AI Confidence: **99.31%**
210. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleHeaderActionPanel.tsx`** -> AI Confidence: **99.31%**
211. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleItem.tsx`** -> AI Confidence: **99.31%**
212. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleItemActionMenu.tsx`** -> AI Confidence: **99.31%**
213. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleItemActionPanel.tsx`** -> AI Confidence: **99.31%**
214. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleItemTitle.tsx`** -> AI Confidence: **99.31%**
215. **`ui/features/context_modules_v2/react/handlers/moduleItemActionHandlers.ts`** -> AI Confidence: **99.31%**
216. **`ui/features/context_modules_v2/react/handlers/modulePageCommandEventHandlers.ts`** -> AI Confidence: **99.31%**
217. **`ui/features/context_modules_v2/react/hooks/queries/useModules.ts`** -> AI Confidence: **99.31%**
218. **`ui/features/context_modules_v2/react/utils/utils.tsx`** -> AI Confidence: **99.31%**
219. **`ui/features/copy_course/react/components/form/CopyCourseForm.tsx`** -> AI Confidence: **99.31%**
220. **`ui/features/course_paces/react/components/errors.tsx`** -> AI Confidence: **99.31%**
221. **`ui/features/course_paces/react/components/footer.tsx`** -> AI Confidence: **99.31%**
222. **`ui/features/course_paces/react/shared/components/course_pace_date_input.tsx`** -> AI Confidence: **99.31%**
223. **`ui/features/course_people_new/react/components/PageHeader/CoursePeopleOptionsMenu.tsx`** -> AI Confidence: **99.31%**
224. **`ui/features/course_settings/react/components/LicenseHelpIcon.tsx`** -> AI Confidence: **99.31%**
225. **`ui/features/developer_keys_v2/react/NewKeyModal.tsx`** -> AI Confidence: **99.31%**
226. **`ui/features/discovery_page/react/components/AuthProvider.tsx`** -> AI Confidence: **99.31%**
227. **`ui/features/discussion_topic_edit_v2/react/components/DiscussionOptions/GradedDiscussionOptions.tsx`** -> AI Confidence: **99.31%**
228. **`ui/features/discussion_topic_edit_v2/react/components/DiscussionOptions/UsageRights.tsx`** -> AI Confidence: **99.31%**
229. **`ui/features/discussion_topic_edit_v2/react/containers/DiscussionTopicFormContainer/DiscussionTopicFormContainer.tsx`** -> AI Confidence: **99.31%**
230. **`ui/features/discussion_topic_insights/react/components/DiscussionInsights/DiscussionInsights.tsx`** -> AI Confidence: **99.31%**
231. **`ui/features/discussion_topic_insights/react/components/DiscussionInsights/Placeholder.tsx`** -> AI Confidence: **99.31%**
232. **`ui/features/discussion_topics_index/react/components/DiscussionRow.tsx`** -> AI Confidence: **99.31%**
233. **`ui/features/discussion_topics_post/react/DiscussionTopicManager.tsx`** -> AI Confidence: **99.31%**
234. **`ui/features/discussion_topics_post/react/components/AssignmentAvailabilityWindow/AssignmentAvailabilityWindow.tsx`** -> AI Confidence: **99.31%**
235. **`ui/features/discussion_topics_post/react/components/AssignmentSingleAvailabilityWindow/AssignmentSingleAvailabilityWindow.tsx`** -> AI Confidence: **99.31%**
236. **`ui/features/discussion_topics_post/react/components/AuthorInfo/AuthorInfo.tsx`** -> AI Confidence: **99.31%**
237. **`ui/features/discussion_topics_post/react/components/AuthorInfo/Timestamps.tsx`** -> AI Confidence: **99.31%**
238. **`ui/features/discussion_topics_post/react/components/DiscussionAvailabilityContainer/DiscussionAvailabilityContainer.tsx`** -> AI Confidence: **99.31%**
239. **`ui/features/discussion_topics_post/react/components/DiscussionPostToolbar/DiscussionPostToolbar.tsx`** -> AI Confidence: **99.31%**
240. **`ui/features/discussion_topics_post/react/components/DiscussionSummary/DiscussionSummary.tsx`** -> AI Confidence: **99.31%**
241. **`ui/features/discussion_topics_post/react/components/DiscussionSummary/DiscussionSummaryRatings.tsx`** -> AI Confidence: **99.31%**
242. **`ui/features/discussion_topics_post/react/components/PostMessage/PostMessage.tsx`** -> AI Confidence: **99.31%**
243. **`ui/features/discussion_topics_post/react/components/PostMessage/Translation/Translation.tsx`** -> AI Confidence: **99.31%**
244. **`ui/features/discussion_topics_post/react/components/PostToolbar/PostToolbar.tsx`** -> AI Confidence: **99.31%**
245. **`ui/features/discussion_topics_post/react/components/ThreadActions/ThreadActions.tsx`** -> AI Confidence: **99.31%**
246. **`ui/features/discussion_topics_post/react/containers/DiscussionThreadContainer/DiscussionThreadContainer.tsx`** -> AI Confidence: **99.31%**
247. **`ui/features/discussion_topics_post/react/containers/DiscussionTopicContainer/DiscussionTopicContainer.tsx`** -> AI Confidence: **99.31%**
248. **`ui/features/discussion_topics_post/react/containers/DiscussionTopicToolbarContainer/DiscussionTopicToolbarContainer.tsx`** -> AI Confidence: **99.31%**
249. **`ui/features/discussion_topics_post/react/containers/SplitScreenThreadsContainer/SplitScreenThreadsContainer.tsx`** -> AI Confidence: **99.31%**
250. **`ui/features/discussion_topics_post/react/containers/SplitScreenViewContainer/SplitScreenParent.tsx`** -> AI Confidence: **99.31%**
251. **`ui/features/discussion_topics_post/react/containers/SplitScreenViewContainer/SplitScreenViewContainer.tsx`** -> AI Confidence: **99.31%**
252. **`ui/features/discussion_topics_post/react/hooks/useTranslation.ts`** -> AI Confidence: **99.31%**
253. **`ui/features/enhanced_individual_gradebook/react/components/ContentSelection/index.tsx`** -> AI Confidence: **99.31%**
254. **`ui/features/enhanced_individual_gradebook/react/components/ContentSelectionLearningMastery/index.tsx`** -> AI Confidence: **99.31%**
255. **`ui/features/enhanced_individual_gradebook/react/components/GradingResults/index.tsx`** -> AI Confidence: **99.31%**
256. **`ui/features/enhanced_individual_gradebook/react/components/StudentInformation/index.tsx`** -> AI Confidence: **99.31%**
257. **`ui/features/enhanced_individual_gradebook/react/hooks/useComments.tsx`** -> AI Confidence: **99.31%**
258. **`ui/features/enhanced_individual_gradebook/react/hooks/useSubmitScore.tsx`** -> AI Confidence: **99.31%**
259. **`ui/features/enhanced_individual_gradebook/utils/gradebookUtils.ts`** -> AI Confidence: **99.31%**
260. **`ui/features/external_apps/react/components/configuration_forms/ConfigurationFormManual.tsx`** -> AI Confidence: **99.31%**
261. **`ui/features/files_v2/react/hooks/useGetFolders.ts`** -> AI Confidence: **99.31%**
262. **`ui/features/grade_summary/react/GradeSummary/AssignmentTable.tsx`** -> AI Confidence: **99.31%**
263. **`ui/features/grade_summary/react/GradeSummary/AssignmentTableRows/AssignmentGroupRow.tsx`** -> AI Confidence: **99.31%**
264. **`ui/features/grade_summary/react/GradeSummary/AssignmentTableRows/AssignmentRow.tsx`** -> AI Confidence: **99.31%**
265. **`ui/features/grade_summary/react/GradeSummary/AssignmentTableRows/GradingPeriodRow.tsx`** -> AI Confidence: **99.31%**
266. **`ui/features/grade_summary/react/GradeSummary/AssignmentTableRows/RubricRow.tsx`** -> AI Confidence: **99.31%**
267. **`ui/features/grade_summary/react/GradeSummary/GradeSummaryContainer.tsx`** -> AI Confidence: **99.31%**
268. **`ui/features/grade_summary/react/GradeSummary/WhatIfGrade.tsx`** -> AI Confidence: **99.31%**
269. **`ui/features/grade_summary/react/GradeSummary/utils.tsx`** -> AI Confidence: **99.31%**
270. **`ui/features/gradebook/react/SISGradePassback/AssignmentCorrectionRow.tsx`** -> AI Confidence: **99.31%**
271. **`ui/features/gradebook/react/default_gradebook/Gradebook.tsx`** -> AI Confidence: **99.31%**
272. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/editors/AssignmentCellEditor/AssignmentRowCell.tsx`** -> AI Confidence: **99.31%**
273. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/formatters/AssignmentCellFormatter.ts`** -> AI Confidence: **99.31%**
274. **`ui/features/gradebook/react/default_gradebook/components/GradeInput.tsx`** -> AI Confidence: **99.31%**
275. **`ui/features/inbox/react/components/AddressBook/AddressBook.tsx`** -> AI Confidence: **99.31%**
276. **`ui/features/inbox/react/components/AddressBook/AddressBookItem.tsx`** -> AI Confidence: **99.31%**
277. **`ui/features/inbox/react/components/MessageActionButtons/MessageActionButtons.tsx`** -> AI Confidence: **99.31%**
278. **`ui/features/inbox/react/components/MessageDetailActions/MessageDetailActions.tsx`** -> AI Confidence: **99.31%**
279. **`ui/features/inbox/react/components/MessageDetailHeader/MessageDetailHeader.tsx`** -> AI Confidence: **99.31%**
280. **`ui/features/inbox/react/components/MessageDetailItem/MessageDetailItem.tsx`** -> AI Confidence: **99.31%**
281. **`ui/features/inbox/react/containers/CanvasInbox.tsx`** -> AI Confidence: **99.31%**
282. **`ui/features/inbox/react/containers/ComposeModalContainer/ComposeModalContainer.tsx`** -> AI Confidence: **99.31%**
283. **`ui/features/inbox/react/containers/ComposeModalContainer/HeaderInputs.tsx`** -> AI Confidence: **99.31%**
284. **`ui/features/inbox/react/containers/ConversationListContainer.tsx`** -> AI Confidence: **99.31%**
285. **`ui/features/inbox/react/containers/MessageDetailContainer/MessageDetailContainer.tsx`** -> AI Confidence: **99.31%**
286. **`ui/features/jobs/jquery/index.tsx`** -> AI Confidence: **99.31%**
287. **`ui/features/k5_dashboard/react/TodosPage.tsx`** -> AI Confidence: **99.31%**
288. **`ui/features/learning_mastery_v2/react/components/charts/MasteryDistributionChart.tsx`** -> AI Confidence: **99.31%**
289. **`ui/features/learning_mastery_v2/react/components/modals/OutcomeDescriptionModal.tsx`** -> AI Confidence: **99.31%**
290. **`ui/features/learning_mastery_v2/react/components/trays/StudentAssignmentDetailTray/CommentsSection.tsx`** -> AI Confidence: **99.31%**
291. **`ui/features/lti_registrations/manage/dynamic_registration_wizard/components/ReviewScreenWrapper.tsx`** -> AI Confidence: **99.31%**
292. **`ui/features/lti_registrations/manage/lti_1p3_registration_form/components/ReviewScreenWrapper.tsx`** -> AI Confidence: **99.31%**
293. **`ui/features/lti_registrations/manage/pages/tool_details/availability/ContextCard.tsx`** -> AI Confidence: **99.31%**
294. **`ui/features/lti_registrations/manage/pages/tool_details/availability/exception_modal/ContextOption.tsx`** -> AI Confidence: **99.31%**
295. **`ui/features/lti_registrations/manage/pages/tool_details/history/differ.ts`** -> AI Confidence: **99.31%**
296. **`ui/features/lti_registrations/manage/pages/tool_details/tii_migration/MigrationRow.tsx`** -> AI Confidence: **99.31%**
297. **`ui/features/lti_registrations/manage/pages/tool_details/tii_migration/TurnitinAPMigrationModal.tsx`** -> AI Confidence: **99.31%**
298. **`ui/features/lti_registrations/manage/registration_overlay/Lti1p3RegistrationOverlayStateHelpers.ts`** -> AI Confidence: **99.31%**
299. **`ui/features/lti_registrations/manage/registration_wizard_forms/NamingConfirmation.tsx`** -> AI Confidence: **99.31%**
300. **`ui/features/nav_tourpoints/react/tour.tsx`** -> AI Confidence: **99.31%**
301. **`ui/features/nav_tourpoints/react/tours/studentTour.tsx`** -> AI Confidence: **99.31%**
302. **`ui/features/navigation_header/react/NavigationBadges.tsx`** -> AI Confidence: **99.31%**
303. **`ui/features/navigation_header/react/trays/HighContrastModeToggle.tsx`** -> AI Confidence: **99.31%**
304. **`ui/features/navigation_header/react/trays/UseDyslexicFontToggle.tsx`** -> AI Confidence: **99.31%**
305. **`ui/features/navigation_header/react/trays/WidgetDashboardToggle.tsx`** -> AI Confidence: **99.31%**
306. **`ui/features/new_login/pages/OtpForm.tsx`** -> AI Confidence: **99.31%**
307. **`ui/features/new_login/pages/SignIn.tsx`** -> AI Confidence: **99.31%**
308. **`ui/features/new_login/pages/register/Parent.tsx`** -> AI Confidence: **99.31%**
309. **`ui/features/new_login/pages/register/Student.tsx`** -> AI Confidence: **99.31%**
310. **`ui/features/new_login/pages/register/Teacher.tsx`** -> AI Confidence: **99.31%**
311. **`ui/features/new_login/shared/index.ts`** -> AI Confidence: **99.31%**
312. **`ui/features/profile/react/AccessTokenDetails.tsx`** -> AI Confidence: **99.31%**
313. **`ui/features/quiz_log_auditing/react/components/event_stream/event.tsx`** -> AI Confidence: **99.31%**
314. **`ui/features/quiz_statistics/react/components/summary/index.tsx`** -> AI Confidence: **99.31%**
315. **`ui/features/roster/backbone/views/RosterUserView.tsx`** -> AI Confidence: **99.31%**
316. **`ui/features/roster/backbone/views/RosterView.tsx`** -> AI Confidence: **99.31%**
317. **`ui/features/rubrics/queries/ViewRubricQueries.ts`** -> AI Confidence: **99.31%**
318. **`ui/features/sis_import/jquery/index.tsx`** -> AI Confidence: **99.31%**
319. **`ui/features/sis_import/react/FullBatchDropdown.tsx`** -> AI Confidence: **99.31%**
320. **`ui/features/speed_grader/jquery/speed_grader.tsx`** -> AI Confidence: **99.31%**
321. **`ui/features/speed_grader/react/RubricAssessmentWrapper/index.tsx`** -> AI Confidence: **99.31%**
322. **`ui/features/speed_grader/react/SpeedGraderCheckpoints/AssessmentGradeInput.tsx`** -> AI Confidence: **99.31%**
323. **`ui/features/speed_grader/react/SpeedGraderStatusMenu.tsx`** -> AI Confidence: **99.31%**
324. **`ui/features/submissions/jquery/index.tsx`** -> AI Confidence: **99.31%**
325. **`ui/features/syllabus_revisions/react/SyllabusRevisionsTray.tsx`** -> AI Confidence: **99.31%**
326. **`ui/features/terms_of_service_modal/react/TermsOfServiceModal.tsx`** -> AI Confidence: **99.31%**
327. **`ui/features/top_navigation_tools/index.tsx`** -> AI Confidence: **99.31%**
328. **`ui/features/user_logins/react/AddEditPseudonym.tsx`** -> AI Confidence: **99.31%**
329. **`ui/features/users_admin_merge/react/PreviewUserMerge.tsx`** -> AI Confidence: **99.31%**
330. **`ui/features/widget_dashboard/react/components/EnrollmentInvitation.tsx`** -> AI Confidence: **99.31%**
331. **`ui/features/widget_dashboard/react/components/widgets/AnnouncementsWidget/AnnouncementItem.tsx`** -> AI Confidence: **99.31%**
332. **`ui/features/widget_dashboard/react/components/widgets/CourseGradesWidget/CourseGradeCard.tsx`** -> AI Confidence: **99.31%**
333. **`ui/features/widget_dashboard/react/components/widgets/CourseWorkCombinedWidget/CourseWorkCombinedWidget.tsx`** -> AI Confidence: **99.31%**
334. **`ui/features/widget_dashboard/react/components/widgets/CourseWorkWidget/CourseWorkWidget.tsx`** -> AI Confidence: **99.31%**
335. **`ui/features/widget_dashboard/react/components/widgets/PeopleWidget/PeopleWidget.tsx`** -> AI Confidence: **99.31%**
336. **`ui/features/widget_dashboard/react/components/widgets/RecentGradesWidget/ExpandedGradeView.tsx`** -> AI Confidence: **99.31%**
337. **`ui/features/widget_dashboard/react/components/widgets/TodoListWidget/CreateTodoModal.tsx`** -> AI Confidence: **99.31%**
338. **`ui/features/widget_dashboard/react/components/widgets/TodoListWidget/TodoItem.tsx`** -> AI Confidence: **99.31%**
339. **`ui/features/widget_dashboard/react/hooks/useCourseInstructors.ts`** -> AI Confidence: **99.31%**
340. **`ui/features/widget_dashboard/react/hooks/useCourseWork.ts`** -> AI Confidence: **99.31%**
341. **`ui/features/widget_dashboard/react/hooks/useUserCourses.ts`** -> AI Confidence: **99.31%**
342. **`ui/shared/add-people/react/components/people_search.tsx`** -> AI Confidence: **99.31%**
343. **`ui/shared/ai-experiences/react/components/LLMConversationView.tsx`** -> AI Confidence: **99.31%**
344. **`ui/shared/ai-experiences/react/components/MessageFeedback.tsx`** -> AI Confidence: **99.31%**
345. **`ui/shared/ai-experiences/react/components/MessageThread.tsx`** -> AI Confidence: **99.31%**
346. **`ui/shared/announcements/react/components/AnnouncementRow.tsx`** -> AI Confidence: **99.31%**
347. **`ui/shared/announcements/react/components/CourseItemRow.tsx`** -> AI Confidence: **99.31%**
348. **`ui/shared/assignments/react/AssignmentHeader.tsx`** -> AI Confidence: **99.31%**
349. **`ui/shared/assignments/react/AssignmentPublishButton.tsx`** -> AI Confidence: **99.31%**
350. **`ui/shared/assignments/react/CreateEditAllocationRuleModal.tsx`** -> AI Confidence: **99.31%**
351. **`ui/shared/assignments/react/DateAvailable.tsx`** -> AI Confidence: **99.31%**
352. **`ui/shared/assignments/react/OptionsMenu.tsx`** -> AI Confidence: **99.31%**
353. **`ui/shared/assignments/react/PeerReviewAllocationRulesTray.tsx`** -> AI Confidence: **99.31%**
354. **`ui/shared/assignments/react/PeerReviewInfo.tsx`** -> AI Confidence: **99.31%**
355. **`ui/shared/assignments/react/StudentSelect.tsx`** -> AI Confidence: **99.31%**
356. **`ui/shared/avatar-dialog-view/react/AvatarModal.tsx`** -> AI Confidence: **99.31%**
357. **`ui/shared/block-editor/react/components/editor/BlockToolbar.tsx`** -> AI Confidence: **99.31%**
358. **`ui/shared/block-editor/react/components/user/blocks/MediaBlock/BlockEditorVideoOptionsTray.tsx`** -> AI Confidence: **99.31%**
359. **`ui/shared/block-editor/react/utils/buildPageContent.tsx`** -> AI Confidence: **99.31%**
360. **`ui/shared/calendar-conferences/react/Conference.tsx`** -> AI Confidence: **99.31%**
361. **`ui/shared/calendar/react/RecurringEvents/DeleteCalendarEventDialog.tsx`** -> AI Confidence: **99.31%**
362. **`ui/shared/calendar/react/RecurringEvents/FrequencyPicker/utils.ts`** -> AI Confidence: **99.31%**
363. **`ui/shared/content-migrations/react/CommonMigratorControls/CommonMigratorControls.tsx`** -> AI Confidence: **99.31%**
364. **`ui/shared/context-cards/react/StudentContextTray.tsx`** -> AI Confidence: **99.31%**
365. **`ui/shared/context-modules/differentiated-modules/react/AssigneeSelector.tsx`** -> AI Confidence: **99.31%**
366. **`ui/shared/context-modules/differentiated-modules/react/DifferentiatedModulesTray.tsx`** -> AI Confidence: **99.31%**
367. **`ui/shared/context-modules/differentiated-modules/react/Item/ItemAssignToCard.tsx`** -> AI Confidence: **99.31%**
368. **`ui/shared/context-modules/differentiated-modules/react/Item/ItemAssignToTrayContent.tsx`** -> AI Confidence: **99.31%**
369. **`ui/shared/context-modules/differentiated-modules/utils/hooks/useFetchAssignees.tsx`** -> AI Confidence: **99.31%**
370. **`ui/shared/context-modules/differentiated-modules/utils/hooks/useGetAssigneeOptions.ts`** -> AI Confidence: **99.31%**
371. **`ui/shared/context-modules/react/ContextModulesHeader.tsx`** -> AI Confidence: **99.31%**
372. **`ui/shared/context-modules/utils/ModuleItemsLazyLoader.tsx`** -> AI Confidence: **99.31%**
373. **`ui/shared/courses/react/CoursePublishButton.tsx`** -> AI Confidence: **99.31%**
374. **`ui/shared/create-course-modal/react/CreateCourseModal.tsx`** -> AI Confidence: **99.31%**
375. **`ui/shared/dashboard-card/loadCardDashboard.tsx`** -> AI Confidence: **99.31%**
376. **`ui/shared/datetime/react/components/DateInput.tsx`** -> AI Confidence: **99.31%**
377. **`ui/shared/datetime/react/components/DateInput2.tsx`** -> AI Confidence: **99.31%**
378. **`ui/shared/differentiation-tags/react/DifferentiationTagModalForm/DifferentiationTagModalForm.tsx`** -> AI Confidence: **99.31%**
379. **`ui/shared/differentiation-tags/react/PeopleFilter/PeopleFilter.tsx`** -> AI Confidence: **99.31%**
380. **`ui/shared/differentiation-tags/react/TagAsModal/TagAsModal.tsx`** -> AI Confidence: **99.31%**
381. **`ui/shared/differentiation-tags/react/UserDifferentiationTagManager/UserDifferentiationTagManager.tsx`** -> AI Confidence: **99.31%**
382. **`ui/shared/due-dates/react/AssignToContent.tsx`** -> AI Confidence: **99.31%**
383. **`ui/shared/external-tools/react/components/ExternalToolModalLauncher.tsx`** -> AI Confidence: **99.31%**
384. **`ui/shared/feature-flags/react/EarlyAccessModal.tsx`** -> AI Confidence: **99.31%**
385. **`ui/shared/final-grade-override/react/index.tsx`** -> AI Confidence: **99.31%**
386. **`ui/shared/gradebook-menu/react/GradebookMenu.tsx`** -> AI Confidence: **99.31%**
387. **`ui/shared/grading-scheme/react/components/GradingSchemesSelector.tsx`** -> AI Confidence: **99.31%**
388. **`ui/shared/grading-scheme/react/components/form/GradingSchemeDataRowInput.tsx`** -> AI Confidence: **99.31%**
389. **`ui/shared/grading/GradeEntry/GradeOverrideEntry.ts`** -> AI Confidence: **99.31%**
390. **`ui/shared/grading/GradeInputHelper.ts`** -> AI Confidence: **99.31%**
391. **`ui/shared/groups/react/CreateOrEditSetModal/index.tsx`** -> AI Confidence: **99.31%**
392. **`ui/shared/instui-bindings/react/Select.tsx`** -> AI Confidence: **99.31%**
393. **`ui/shared/lti-apps/components/ProductDetail/ExternalLinks.tsx`** -> AI Confidence: **99.31%**
394. **`ui/shared/lti-apps/components/ProductDetail/ProductDetail.tsx`** -> AI Confidence: **99.31%**
395. **`ui/shared/lti-asset-processor/react/hooks/useCourseAssignmentsAssetReports.ts`** -> AI Confidence: **99.31%**
396. **`ui/shared/lti-asset-processor/shared-with-sg/replicated/components/LtiAssetReportsCard.tsx`** -> AI Confidence: **99.31%**
397. **`ui/shared/message-students-dialog/react/MessageStudentsWhoDialog.tsx`** -> AI Confidence: **99.31%**
398. **`ui/shared/outcome-context-tag/OutcomeContextTag.tsx`** -> AI Confidence: **99.31%**
399. **`ui/shared/planner/components/PlannerApp/index.tsx`** -> AI Confidence: **99.31%**
400. **`ui/shared/planner/components/PlannerItem/index.tsx`** -> AI Confidence: **99.31%**
401. **`ui/shared/rubrics/react/Comments.tsx`** -> AI Confidence: **99.31%**
402. **`ui/shared/rubrics/react/RubricAssessment/HorizontalButtonDisplay.tsx`** -> AI Confidence: **99.31%**
403. **`ui/shared/rubrics/react/RubricAssessment/ModernView.tsx`** -> AI Confidence: **99.31%**
404. **`ui/shared/rubrics/react/RubricAssessment/OutcomePopover/OutcomePopoverDisplay.tsx`** -> AI Confidence: **99.31%**
405. **`ui/shared/rubrics/react/RubricAssessment/RubricAssessmentContainer.tsx`** -> AI Confidence: **99.31%**
406. **`ui/shared/rubrics/react/RubricAssessment/RubricAssessmentTray.tsx`** -> AI Confidence: **99.31%**
407. **`ui/shared/rubrics/react/RubricAssessment/TraditionalViewCriterionRow.tsx`** -> AI Confidence: **99.31%**
408. **`ui/shared/rubrics/react/RubricAssessment/VerticalButtonDisplay.tsx`** -> AI Confidence: **99.31%**
409. **`ui/shared/rubrics/react/RubricAssignment/components/RubricAssignmentContainer.tsx`** -> AI Confidence: **99.31%**
410. **`ui/shared/rubrics/react/RubricForm/components/CriterionModal/CriterionModal.tsx`** -> AI Confidence: **99.31%**
411. **`ui/shared/rubrics/react/RubricForm/components/RubricCriteriaRow.tsx`** -> AI Confidence: **99.31%**
412. **`ui/shared/rubrics/react/RubricForm/components/RubricFormFooter.tsx`** -> AI Confidence: **99.31%**
413. **`ui/shared/rubrics/react/RubricForm/index.tsx`** -> AI Confidence: **99.31%**
414. **`ui/shared/rubrics/react/RubricForm/queries/RubricFormQueries.ts`** -> AI Confidence: **99.31%**
415. **`ui/shared/select-content-dialog/jquery/select_content_dialog.tsx`** -> AI Confidence: **99.31%**
416. **`ui/shared/student_view_peer_reviews/react/StudentViewPeerReviews.tsx`** -> AI Confidence: **99.31%**
417. **`ui/shared/submission-sticker/react/helpers/assetFactory.ts`** -> AI Confidence: **99.31%**
418. **`ui/shared/temporary-enrollment/react/TempEnrollAssign.tsx`** -> AI Confidence: **99.31%**
419. **`ui/shared/temporary-enrollment/react/TempEnrollUsersListRow.tsx`** -> AI Confidence: **99.31%**
420. **`ui/shared/top-navigation/react/TopNavPortalWithDefaults.tsx`** -> AI Confidence: **99.31%**
421. **`Dockerfile`** -> AI Confidence: **99.29%**
422. **`Dockerfile.jenkins.js`** -> AI Confidence: **99.29%**
423. **`docker-compose/karma/Dockerfile`** -> AI Confidence: **99.29%**
424. **`docker-compose/postgres/Dockerfile`** -> AI Confidence: **99.29%**
425. **`Gemfile.d/_before.rb`** -> AI Confidence: **99.29%**
426. **`Gemfile.d/plugins.rb`** -> AI Confidence: **99.29%**
427. **`Gemfile.d/~after.rb`** -> AI Confidence: **99.29%**
428. **`app/controllers/assignment_extensions_controller.rb`** -> AI Confidence: **99.29%**
429. **`app/controllers/block_editor_templates_api_controller.rb`** -> AI Confidence: **99.29%**
430. **`app/controllers/communication_channels_controller.rb`** -> AI Confidence: **99.29%**
431. **`app/controllers/concerns/k5_mode.rb`** -> AI Confidence: **99.29%**
432. **`app/controllers/concerns/observer_module_info.rb`** -> AI Confidence: **99.29%**
433. **`app/controllers/errors_controller.rb`** -> AI Confidence: **99.29%**
434. **`app/controllers/feature_flags_controller.rb`** -> AI Confidence: **99.29%**
435. **`app/controllers/gradebook_csvs_controller.rb`** -> AI Confidence: **99.29%**
436. **`app/controllers/login/canvas_controller.rb`** -> AI Confidence: **99.29%**
437. **`app/controllers/login/saml_controller.rb`** -> AI Confidence: **99.29%**
438. **`app/controllers/permissions_help_controller.rb`** -> AI Confidence: **99.29%**
439. **`app/controllers/quizzes/quiz_submissions_controller.rb`** -> AI Confidence: **99.29%**
440. **`app/controllers/role_overrides_controller.rb`** -> AI Confidence: **99.29%**
441. **`app/controllers/search_controller.rb`** -> AI Confidence: **99.29%**
442. **`app/graphql/canvas_schema.rb`** -> AI Confidence: **99.29%**
443. **`app/graphql/graphql_node_loader.rb`** -> AI Confidence: **99.29%**
444. **`app/graphql/loaders/activity_stream_summary_loader.rb`** -> AI Confidence: **99.29%**
445. **`app/graphql/loaders/discussion_entry_loader.rb`** -> AI Confidence: **99.29%**
446. **`app/graphql/mutations/accept_enrollment_invitation.rb`** -> AI Confidence: **99.29%**
447. **`app/graphql/mutations/auto_grade_submission.rb`** -> AI Confidence: **99.29%**
448. **`app/graphql/mutations/create_assignment.rb`** -> AI Confidence: **99.29%**
449. **`app/graphql/mutations/create_conversation.rb`** -> AI Confidence: **99.29%**
450. **`app/graphql/mutations/create_discussion_entry.rb`** -> AI Confidence: **99.29%**
451. **`app/graphql/mutations/create_group_in_set.rb`** -> AI Confidence: **99.29%**
452. **`app/graphql/mutations/create_institutional_tag.rb`** -> AI Confidence: **99.29%**
453. **`app/graphql/mutations/create_submission_comment.rb`** -> AI Confidence: **99.29%**
454. **`app/graphql/mutations/delete_conversations.rb`** -> AI Confidence: **99.29%**
455. **`app/graphql/mutations/hide_assignment_grades.rb`** -> AI Confidence: **99.29%**
456. **`app/graphql/mutations/hide_assignment_grades_for_sections.rb`** -> AI Confidence: **99.29%**
457. **`app/graphql/mutations/post_assignment_grades.rb`** -> AI Confidence: **99.29%**
458. **`app/graphql/mutations/post_assignment_grades_for_sections.rb`** -> AI Confidence: **99.29%**
459. **`app/graphql/mutations/reject_enrollment_invitation.rb`** -> AI Confidence: **99.29%**
460. **`app/graphql/mutations/remove_institutional_tag.rb`** -> AI Confidence: **99.29%**
461. **`app/graphql/mutations/save_rubric_assessment.rb`** -> AI Confidence: **99.29%**
462. **`app/graphql/mutations/set_assignment_post_policy.rb`** -> AI Confidence: **99.29%**
463. **`app/graphql/mutations/set_rubric_self_assessment.rb`** -> AI Confidence: **99.29%**
464. **`app/graphql/mutations/update_assignment.rb`** -> AI Confidence: **99.29%**
465. **`app/graphql/mutations/update_conversation_participants.rb`** -> AI Confidence: **99.29%**
466. **`app/graphql/mutations/update_discussion_entry.rb`** -> AI Confidence: **99.29%**
467. **`app/graphql/mutations/update_gradebook_group_filter.rb`** -> AI Confidence: **99.29%**
468. **`app/graphql/mutations/update_institutional_tag.rb`** -> AI Confidence: **99.29%**
469. **`app/graphql/mutations/update_institutional_tag_category.rb`** -> AI Confidence: **99.29%**
470. **`app/graphql/mutations/update_submission_grade.rb`** -> AI Confidence: **99.29%**
471. **`app/graphql/mutations/update_submission_grade_status.rb`** -> AI Confidence: **99.29%**
472. **`app/graphql/mutations/update_submission_sticker.rb`** -> AI Confidence: **99.29%**
473. **`app/graphql/mutations/update_submission_student_entered_score.rb`** -> AI Confidence: **99.29%**
474. **`app/graphql/mutations/update_submissions_read_state.rb`** -> AI Confidence: **99.29%**
475. **`app/graphql/mutations/update_widget_dashboard_config.rb`** -> AI Confidence: **99.29%**
476. **`app/graphql/mutations/upsert_custom_grade_status.rb`** -> AI Confidence: **99.29%**
477. **`app/graphql/types/string_map_type.rb`** -> AI Confidence: **99.29%**
478. **`app/helpers/account_notification_helper.rb`** -> AI Confidence: **99.29%**
479. **`app/helpers/canvas_outcomes_helper.rb`** -> AI Confidence: **99.29%**
480. **`app/helpers/content_export_api_helper.rb`** -> AI Confidence: **99.29%**
481. **`app/helpers/conversations_helper.rb`** -> AI Confidence: **99.29%**
482. **`app/helpers/courses_helper.rb`** -> AI Confidence: **99.29%**
483. **`app/helpers/cyoe_helper.rb`** -> AI Confidence: **99.29%**
484. **`app/helpers/kaltura_helper.rb`** -> AI Confidence: **99.29%**
485. **`app/helpers/search_helper.rb`** -> AI Confidence: **99.29%**
486. **`app/models/access_verifier.rb`** -> AI Confidence: **99.29%**
487. **`app/models/account/bulk_update.rb`** -> AI Confidence: **99.29%**
488. **`app/models/account/help_links.rb`** -> AI Confidence: **99.29%**
489. **`app/models/account_notification.rb`** -> AI Confidence: **99.29%**
490. **`app/models/alert.rb`** -> AI Confidence: **99.29%**
491. **`app/models/appointment_group_sub_context.rb`** -> AI Confidence: **99.29%**
492. **`app/models/assignment/bulk_update.rb`** -> AI Confidence: **99.29%**
493. **`app/models/attachments/storage.rb`** -> AI Confidence: **99.29%**
494. **`app/models/broadcast_policies/submission_policy.rb`** -> AI Confidence: **99.29%**
495. **`app/models/canvadocs_annotation_context.rb`** -> AI Confidence: **99.29%**
496. **`app/models/collaborator.rb`** -> AI Confidence: **99.29%**
497. **`app/models/conditional_release/override_handler.rb`** -> AI Confidence: **99.29%**
498. **`app/models/context.rb`** -> AI Confidence: **99.29%**
499. **`app/models/course_pace.rb`** -> AI Confidence: **99.29%**
500. **`app/models/courses/timetable_event_builder.rb`** -> AI Confidence: **99.29%**
501. **`app/models/discussion_topic_insight.rb`** -> AI Confidence: **99.29%**
502. **`app/models/enrollment/query_builder.rb`** -> AI Confidence: **99.29%**
503. **`app/models/eportfolio.rb`** -> AI Confidence: **99.29%**
504. **`app/models/eportfolio_category.rb`** -> AI Confidence: **99.29%**
505. **`app/models/eportfolio_entry.rb`** -> AI Confidence: **99.29%**
506. **`app/models/grading_period_group.rb`** -> AI Confidence: **99.29%**
507. **`app/models/importers/assessment_question_bank_importer.rb`** -> AI Confidence: **99.29%**
508. **`app/models/importers/assessment_question_importer.rb`** -> AI Confidence: **99.29%**
509. **`app/models/importers/assignment_group_importer.rb`** -> AI Confidence: **99.29%**
510. **`app/models/importers/assignment_importer.rb`** -> AI Confidence: **99.29%**
511. **`app/models/importers/context_external_tool_importer.rb`** -> AI Confidence: **99.29%**
512. **`app/models/importers/context_module_importer.rb`** -> AI Confidence: **99.29%**
513. **`app/models/importers/course_content_importer.rb`** -> AI Confidence: **99.29%**
514. **`app/models/importers/learning_outcome_group_importer.rb`** -> AI Confidence: **99.29%**
515. **`app/models/importers/learning_outcome_importer.rb`** -> AI Confidence: **99.29%**
516. **`app/models/importers/quiz_group_importer.rb`** -> AI Confidence: **99.29%**
517. **`app/models/importers/quiz_importer.rb`** -> AI Confidence: **99.29%**
518. **`app/models/importers/quiz_question_importer.rb`** -> AI Confidence: **99.29%**
519. **`app/models/importers/rubric_importer.rb`** -> AI Confidence: **99.29%**
520. **`app/models/importers/wiki_page_importer.rb`** -> AI Confidence: **99.29%**
521. **`app/models/llm_config.rb`** -> AI Confidence: **99.29%**
522. **`app/models/lti/registration_history_entry.rb`** -> AI Confidence: **99.29%**
523. **`app/models/notification.rb`** -> AI Confidence: **99.29%**
524. **`app/models/notification_policy.rb`** -> AI Confidence: **99.29%**
525. **`app/models/notifier.rb`** -> AI Confidence: **99.29%**
526. **`app/models/polling/poll.rb`** -> AI Confidence: **99.29%**
527. **`app/models/quizzes/quiz_statistics/student_analysis.rb`** -> AI Confidence: **99.29%**
528. **`app/models/quizzes/quiz_submission_service.rb`** -> AI Confidence: **99.29%**
529. **`app/models/root_account_resolver.rb`** -> AI Confidence: **99.29%**
530. **`app/models/rubric_association.rb`** -> AI Confidence: **99.29%**
531. **`app/models/sis_pseudonym.rb`** -> AI Confidence: **99.29%**
532. **`app/models/stream_item.rb`** -> AI Confidence: **99.29%**
533. **`app/services/checkpoints/discussion_checkpoint_updater_service.rb`** -> AI Confidence: **99.29%**
534. **`app/services/course_pacing/pace_contexts_service.rb`** -> AI Confidence: **99.29%**
535. **`app/services/peer_review/validations.rb`** -> AI Confidence: **99.29%**
536. **`app/services/rubric_llm_service.rb`** -> AI Confidence: **99.29%**
537. **`config/canvas_rails_switcher.rb`** -> AI Confidence: **99.29%**
538. **`config/initializers/api_scope_mapper_initializer.rb`** -> AI Confidence: **99.29%**
539. **`config/initializers/cache_store.rb`** -> AI Confidence: **99.29%**
540. **`config/initializers/code_statistics.rb`** -> AI Confidence: **99.29%**
541. **`config/initializers/datadog_apm.rb`** -> AI Confidence: **99.29%**
542. **`config/initializers/diigo.rb`** -> AI Confidence: **99.29%**
543. **`config/initializers/errors.rb`** -> AI Confidence: **99.29%**
544. **`config/initializers/google_drive.rb`** -> AI Confidence: **99.29%**
545. **`config/initializers/guard_rail.rb`** -> AI Confidence: **99.29%**
546. **`config/initializers/incoming_mail.rb`** -> AI Confidence: **99.29%**
547. **`config/initializers/inst_statsd.rb`** -> AI Confidence: **99.29%**
548. **`config/initializers/jwt_workflow.rb`** -> AI Confidence: **99.29%**
549. **`config/initializers/mime_types.rb`** -> AI Confidence: **99.29%**
550. **`config/initializers/no_timeouts_debugging.rb`** -> AI Confidence: **99.29%**
551. **`config/initializers/outgoing_mail.rb`** -> AI Confidence: **99.29%**
552. **`config/initializers/periodic_jobs.rb`** -> AI Confidence: **99.29%**
553. **`config/initializers/permissions_groups.rb`** -> AI Confidence: **99.29%**
554. **`config/initializers/permissions_registry.rb`** -> AI Confidence: **99.29%**
555. **`config/initializers/ruby_version_compat.rb`** -> AI Confidence: **99.29%**
556. **`config/initializers/sentry.rb`** -> AI Confidence: **99.29%**
557. **`config/initializers/zeitwerk.rb`** -> AI Confidence: **99.29%**
558. **`config/locales/ca.rb`** -> AI Confidence: **99.29%**
559. **`config/locales/cy.rb`** -> AI Confidence: **99.29%**
560. **`config/locales/ga.rb`** -> AI Confidence: **99.29%**
561. **`config/locales/hi.rb`** -> AI Confidence: **99.29%**
562. **`config/locales/ht.rb`** -> AI Confidence: **99.29%**
563. **`config/locales/hy.rb`** -> AI Confidence: **99.29%**
564. **`config/locales/id.rb`** -> AI Confidence: **99.29%**
565. **`config/locales/ms.rb`** -> AI Confidence: **99.29%**
566. **`config/locales/pl.rb`** -> AI Confidence: **99.29%**
567. **`config/locales/sv.rb`** -> AI Confidence: **99.29%**
568. **`config/puma.rb`** -> AI Confidence: **99.29%**
569. **`config/routes.rb`** -> AI Confidence: **99.29%**
570. **`db/migrate/20101216224513_create_delayed_jobs.rb`** -> AI Confidence: **99.29%**
571. **`db/migrate/20111111214312_load_initial_data.rb`** -> AI Confidence: **99.29%**
572. **`doc/api/data_services/data_services_events_loader.rb`** -> AI Confidence: **99.29%**
573. **`doc/yard_plugins/lti_variable_expansion_plugin.rb`** -> AI Confidence: **99.29%**
574. **`gems/plugins/account_reports/spec_canvas/improved_outcome_reports/shared/improved_outcome_reports_spec_helpers.rb`** -> AI Confidence: **99.29%**
575. **`gems/plugins/account_reports/spec_canvas/improved_outcome_reports/shared/shared_examples.rb`** -> AI Confidence: **99.29%**
576. **`gems/plugins/account_reports/spec_canvas/report_spec_helper.rb`** -> AI Confidence: **99.29%**
577. **`script/lint_commit_message`** -> AI Confidence: **99.29%**
578. **`script/render_json_lint`** -> AI Confidence: **99.29%**
579. **`spec/lib/utils/date_presenter_spec.rb`** -> AI Confidence: **99.29%**
580. **`spec/lib/utils/datetime_range_presenter_spec.rb`** -> AI Confidence: **99.29%**
581. **`spec/lib/utils/hash_utils_spec.rb`** -> AI Confidence: **99.29%**
582. **`spec/lib/utils/inst_statsd_utils/timing_spec.rb`** -> AI Confidence: **99.29%**
583. **`spec/lib/utils/relative_date_spec.rb`** -> AI Confidence: **99.29%**
584. **`Jenkinsfile`** -> AI Confidence: **99.29%**
585. **`docker-compose/postgres/create-dbs.sh`** -> AI Confidence: **99.29%**
586. **`packages/canvas-rce/scripts/demo.sh`** -> AI Confidence: **99.29%**
587. **`packages/canvas-rce/scripts/npm_localpublish.sh`** -> AI Confidence: **99.29%**
588. **`script/canvas_update`** -> AI Confidence: **99.29%**
589. **`script/webpack_watch_es_packages.sh`** -> AI Confidence: **99.29%**
590. **`packages/canvas-rce/jest.config.js`** -> AI Confidence: **99.29%**
591. **`packages/canvas-rce/src/canvasFileBrowser/en-US.js`** -> AI Confidence: **99.29%**
592. **`packages/canvas-rce/src/rce/plugins/shared/Upload/videoValidationUtils.js`** -> AI Confidence: **99.29%**
593. **`packages/canvas-rce/src/rce/plugins/tinymce-a11y-checker/utils/rgb-hex.js`** -> AI Confidence: **99.29%**
594. **`packages/canvas-rce/src/translations/tinymce/ar_SA.js`** -> AI Confidence: **99.29%**
595. **`packages/canvas-rce/src/translations/tinymce/ca.js`** -> AI Confidence: **99.29%**
596. **`packages/canvas-rce/src/translations/tinymce/cs.js`** -> AI Confidence: **99.29%**
597. **`packages/canvas-rce/src/translations/tinymce/cy.js`** -> AI Confidence: **99.29%**
598. **`packages/canvas-rce/src/translations/tinymce/da.js`** -> AI Confidence: **99.29%**
599. **`packages/canvas-rce/src/translations/tinymce/de.js`** -> AI Confidence: **99.29%**
600. **`packages/canvas-rce/src/translations/tinymce/en_GB.js`** -> AI Confidence: **99.29%**
601. **`packages/canvas-rce/src/translations/tinymce/es.js`** -> AI Confidence: **99.29%**
602. **`packages/canvas-rce/src/translations/tinymce/fr_FR.js`** -> AI Confidence: **99.29%**
603. **`packages/canvas-rce/src/translations/tinymce/ga.js`** -> AI Confidence: **99.29%**
604. **`packages/canvas-rce/src/translations/tinymce/he_IL.js`** -> AI Confidence: **99.29%**
605. **`packages/canvas-rce/src/translations/tinymce/hu_HU.js`** -> AI Confidence: **99.29%**
606. **`packages/canvas-rce/src/translations/tinymce/id.js`** -> AI Confidence: **99.29%**
607. **`packages/canvas-rce/src/translations/tinymce/ja.js`** -> AI Confidence: **99.29%**
608. **`packages/canvas-rce/src/translations/tinymce/ko_KR.js`** -> AI Confidence: **99.29%**
609. **`packages/canvas-rce/src/translations/tinymce/nb_NO.js`** -> AI Confidence: **99.29%**
610. **`packages/canvas-rce/src/translations/tinymce/nl.js`** -> AI Confidence: **99.29%**
611. **`packages/canvas-rce/src/translations/tinymce/pl.js`** -> AI Confidence: **99.29%**
612. **`packages/canvas-rce/src/translations/tinymce/pt_BR.js`** -> AI Confidence: **99.29%**
613. **`packages/canvas-rce/src/translations/tinymce/pt_PT.js`** -> AI Confidence: **99.29%**
614. **`packages/canvas-rce/src/translations/tinymce/ro.js`** -> AI Confidence: **99.29%**
615. **`packages/canvas-rce/src/translations/tinymce/sl.js`** -> AI Confidence: **99.29%**
616. **`packages/canvas-rce/src/translations/tinymce/sr.js`** -> AI Confidence: **99.29%**
617. **`packages/canvas-rce/src/translations/tinymce/sv_SE.js`** -> AI Confidence: **99.29%**
618. **`packages/canvas-rce/src/translations/tinymce/tr_TR.js`** -> AI Confidence: **99.29%**
619. **`packages/canvas-rce/src/translations/tinymce/vi_VN.js`** -> AI Confidence: **99.29%**
620. **`packages/canvas-rce/src/translations/tinymce/zh_CN.js`** -> AI Confidence: **99.29%**
621. **`packages/canvas-rce/src/translations/tinymce/zh_TW.js`** -> AI Confidence: **99.29%**
622. **`packages/jquery-kyle-menu/monkey-patches.js`** -> AI Confidence: **99.29%**
623. **`packages/jquery-kyle-menu/popup.js`** -> AI Confidence: **99.29%**
624. **`packages/jqueryui/draggable.js`** -> AI Confidence: **99.29%**
625. **`packages/jqueryui/position.js`** -> AI Confidence: **99.29%**
626. **`packages/k5uploader/src/upload_result.js`** -> AI Confidence: **99.29%**
627. **`ui/boot/initializers/setWebpackCdnHost.js`** -> AI Confidence: **99.29%**
628. **`ui/features/calendar/CalendarEventFilter.js`** -> AI Confidence: **99.29%**
629. **`ui/features/calendar/backbone/views/__tests__/calendarEvents.js`** -> AI Confidence: **99.29%**
630. **`ui/features/developer_keys_v2/react/__tests__/fixtures/responses.js`** -> AI Confidence: **99.29%**
631. **`ui/features/not_found_index/react/space_invaders/input.js`** -> AI Confidence: **99.29%**
632. **`ui/features/quiz_statistics/stores/util/populate_collection.js`** -> AI Confidence: **99.29%**
633. **`ui/shared/groups/react/mixins/BackboneState.js`** -> AI Confidence: **99.29%**
634. **`ui/shared/loading-image/jquery/index.js`** -> AI Confidence: **99.29%**
635. **`ui/shared/media-comments/jquery/MediaElementKeyActionHandler.js`** -> AI Confidence: **99.29%**
636. **`ui/shared/outcomes/react/hooks/useCanvasContext.js`** -> AI Confidence: **99.29%**
637. **`ui/shared/util/rgb2hex.js`** -> AI Confidence: **99.29%**
638. **`ui/features/ai_experiences_index/react/types.ts`** -> AI Confidence: **99.29%**
639. **`ui/features/assignments_show_student/react/components/RubricsQuery.types.d.ts`** -> AI Confidence: **99.29%**
640. **`ui/features/gradebook/jquery/slickgrid.long_text_editor.ts`** -> AI Confidence: **99.29%**
641. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/formatters/CellStyles.ts`** -> AI Confidence: **99.29%**
642. **`ui/features/gradebook/react/default_gradebook/stores/graphql/assignments/transformAssignments.ts`** -> AI Confidence: **99.29%**
643. **`ui/features/gradebook/react/default_gradebook/stores/graphql/enrollments/transformEnrollment.ts`** -> AI Confidence: **99.29%**
644. **`ui/features/gradebook/react/default_gradebook/stores/graphql/submissions/transformSubmission.ts`** -> AI Confidence: **99.29%**
645. **`ui/features/gradebook/react/default_gradebook/utils/urlHelpers.ts`** -> AI Confidence: **99.29%**
646. **`ui/features/quiz_log_auditing/backbone/models/question_answered_event_decorator.ts`** -> AI Confidence: **99.29%**
647. **`ui/shared/instui-bindings/react/AiInformation.tsx`** -> AI Confidence: **99.29%**
648. **`ui/shared/normalize-registration-errors/obj-flatten.ts`** -> AI Confidence: **99.29%**
649. **`ui/features/quizzes/jquery/quizzes.jsx`** -> AI Confidence: **99.25%**
650. **`packages/canvas-media/src/UploadMedia.jsx`** -> AI Confidence: **99.24%**
651. **`packages/canvas-rce/src/canvasFileBrowser/FileBrowser.jsx`** -> AI Confidence: **99.24%**
652. **`packages/canvas-rce/src/rce/contentRendering.jsx`** -> AI Confidence: **99.24%**
653. **`packages/canvas-rce/src/rce/plugins/instructure_documents/components/Link.jsx`** -> AI Confidence: **99.24%**
654. **`packages/canvas-rce/src/rce/plugins/instructure_icon_maker/components/CreateIconMakerForm/Footer.jsx`** -> AI Confidence: **99.24%**
655. **`packages/canvas-rce/src/rce/plugins/instructure_links/components/LinkOptionsDialog/index.jsx`** -> AI Confidence: **99.24%**
656. **`packages/canvas-rce/src/rce/plugins/instructure_links/components/LinkSet.jsx`** -> AI Confidence: **99.24%**
657. **`packages/canvas-rce/src/rce/plugins/instructure_record/MediaPanel/index.jsx`** -> AI Confidence: **99.24%**
658. **`packages/canvas-rce/src/rce/plugins/shared/DimensionsInput/index.jsx`** -> AI Confidence: **99.24%**
659. **`packages/canvas-rce/src/rce/plugins/shared/Upload/ComputerPanel.jsx`** -> AI Confidence: **99.24%**
660. **`ui/features/account_course_user_search/react/components/CoursesListRow.jsx`** -> AI Confidence: **99.24%**
661. **`ui/features/account_course_user_search/react/components/UsersListRow.jsx`** -> AI Confidence: **99.24%**
662. **`ui/features/assignment_index/backbone/views/CreateAssignmentView.js`** -> AI Confidence: **99.24%**
663. **`ui/features/assignment_index/backbone/views/DeleteGroupView.jsx`** -> AI Confidence: **99.24%**
664. **`ui/features/assignments_show_student/react/components/AttemptType/MediaAttempt.jsx`** -> AI Confidence: **99.24%**
665. **`ui/features/assignments_show_student/react/components/AttemptType/MoreOptions/CanvasFiles/index.jsx`** -> AI Confidence: **99.24%**
666. **`ui/features/assignments_show_student/react/components/AttemptType/TextEntry.jsx`** -> AI Confidence: **99.24%**
667. **`ui/features/assignments_show_student/react/components/RubricTab.jsx`** -> AI Confidence: **99.24%**
668. **`ui/features/assignments_show_student/react/components/StudentContent.jsx`** -> AI Confidence: **99.24%**
669. **`ui/features/assignments_show_student/react/components/SubmissionManager.jsx`** -> AI Confidence: **99.24%**
670. **`ui/features/assignments_show_student/react/components/SubmissionWorkflowTracker.jsx`** -> AI Confidence: **99.24%**
671. **`ui/features/calendar/backbone/views/CalendarHeader.jsx`** -> AI Confidence: **99.24%**
672. **`ui/features/calendar/backbone/views/CalendarNavigator.jsx`** -> AI Confidence: **99.24%**
673. **`ui/features/calendar/backbone/views/EditPlannerNoteDetails.js`** -> AI Confidence: **99.24%**
674. **`ui/features/calendar/backbone/views/EditToDoItemDetails.js`** -> AI Confidence: **99.24%**
675. **`ui/features/conferences/index.jsx`** -> AI Confidence: **99.24%**
676. **`ui/features/course_settings/react/components/CourseAvailabilityOptions.jsx`** -> AI Confidence: **99.24%**
677. **`ui/features/developer_keys_v2/react/ManualConfigurationForm/Placement.jsx`** -> AI Confidence: **99.24%**
678. **`ui/features/developer_keys_v2/react/ToolConfigurationForm.jsx`** -> AI Confidence: **99.24%**
679. **`ui/features/external_apps/react/components/ExternalToolsTable.jsx`** -> AI Confidence: **99.24%**
680. **`ui/features/files/react/components/FilesApp.jsx`** -> AI Confidence: **99.24%**
681. **`ui/features/files/react/components/FolderChild.jsx`** -> AI Confidence: **99.24%**
682. **`ui/features/files/react/components/ItemCog.jsx`** -> AI Confidence: **99.24%**
683. **`ui/features/files/react/legacy/components/FolderChild.jsx`** -> AI Confidence: **99.24%**
684. **`ui/features/jobs_v2/react/components/OrphanedStrandIndicator.jsx`** -> AI Confidence: **99.24%**
685. **`ui/features/k5_dashboard/react/GradesPage.jsx`** -> AI Confidence: **99.24%**
686. **`ui/features/k5_dashboard/react/GradesSummary.jsx`** -> AI Confidence: **99.24%**
687. **`ui/features/not_found_index/react/space_invaders/SpaceInvaders.jsx`** -> AI Confidence: **99.24%**
688. **`ui/features/outcome_management/react/CreateOutcomeModal.jsx`** -> AI Confidence: **99.24%**
689. **`ui/features/outcome_management/react/FindOutcomesBillboard.jsx`** -> AI Confidence: **99.24%**
690. **`ui/features/outcome_management/react/Management/GroupMoveModal.jsx`** -> AI Confidence: **99.24%**
691. **`ui/features/outcome_management/react/Management/ManageOutcomeItem.jsx`** -> AI Confidence: **99.24%**
692. **`ui/features/outcome_management/react/shared/TargetGroupSelector.jsx`** -> AI Confidence: **99.24%**
693. **`ui/features/profile/jquery/communication_channels.jsx`** -> AI Confidence: **99.24%**
694. **`ui/features/profile/jquery/index.jsx`** -> AI Confidence: **99.24%**
695. **`ui/features/quizzes_index/backbone/views/QuizItemView.jsx`** -> AI Confidence: **99.24%**
696. **`ui/features/registration/jquery/index.js`** -> AI Confidence: **99.24%**
697. **`ui/features/submit_assignment/backbone/views/ExternalContentFileSubmissionView.jsx`** -> AI Confidence: **99.24%**
698. **`ui/shared/add-people/react/components/missing_people_section.jsx`** -> AI Confidence: **99.24%**
699. **`ui/shared/assignments/react/CommentsTray/CommentTextArea.jsx`** -> AI Confidence: **99.24%**
700. **`ui/shared/blueprint-courses/react/components/LockManager/LockToggle.jsx`** -> AI Confidence: **99.24%**
701. **`ui/shared/direct-sharing/react/components/CourseAndModulePicker.jsx`** -> AI Confidence: **99.24%**
702. **`ui/shared/enhanced-user-content/jquery/index.js`** -> AI Confidence: **99.24%**
703. **`ui/shared/feature-flags/react/FeatureFlagButton.jsx`** -> AI Confidence: **99.24%**
704. **`ui/shared/feature-flags/react/FeatureFlagTable.jsx`** -> AI Confidence: **99.24%**
705. **`ui/shared/files/react/components/FilePreviewInfoPanel.jsx`** -> AI Confidence: **99.24%**
706. **`ui/shared/files/react/components/RestrictedRadioButtons.jsx`** -> AI Confidence: **99.24%**
707. **`ui/shared/generic-error-page/react/index.jsx`** -> AI Confidence: **99.24%**
708. **`ui/shared/groups/backbone/views/GroupCategoryEditView.jsx`** -> AI Confidence: **99.24%**
709. **`ui/shared/k5/react/K5Announcement.jsx`** -> AI Confidence: **99.24%**
710. **`ui/shared/k5/react/utils.js`** -> AI Confidence: **99.24%**
711. **`ui/shared/media-comments/jquery/mediaComment.jsx`** -> AI Confidence: **99.24%**
712. **`ui/shared/move-item-tray/react/MoveSelect.jsx`** -> AI Confidence: **99.24%**
713. **`ui/shared/observer-picker/react/ObserverOptions.jsx`** -> AI Confidence: **99.24%**
714. **`ui/shared/outcomes/content-view/backbone/views/CalculationMethodFormView.js`** -> AI Confidence: **99.24%**
715. **`ui/shared/outcomes/react/hooks/useCourseAlignments.js`** -> AI Confidence: **99.24%**
716. **`ui/shared/outcomes/react/treeBrowser.js`** -> AI Confidence: **99.24%**
717. **`ui/shared/planner/actions/loading-actions.js`** -> AI Confidence: **99.24%**
718. **`ui/shared/post-assignment-grades-tray/react/index.jsx`** -> AI Confidence: **99.24%**
719. **`ui/shared/publish-button-view/backbone/views/index.jsx`** -> AI Confidence: **99.24%**
720. **`ui/shared/publish-button-view/react/components/DelayedPublishDialog.jsx`** -> AI Confidence: **99.24%**
721. **`ui/shared/quizzes/backbone/models/Quiz.js`** -> AI Confidence: **99.24%**
722. **`ui/shared/rubrics/react/Criterion.jsx`** -> AI Confidence: **99.24%**
723. **`packages/canvas-media/src/ClosedCaptionCreatorV2/ClosedCaptionPanelV2.tsx`** -> AI Confidence: **99.24%**
724. **`packages/canvas-rce/src/rce/plugins/instructure_links/components/NoResults.tsx`** -> AI Confidence: **99.24%**
725. **`packages/canvas-rce/src/rce/plugins/instructure_search_and_replace/components/FindReplaceTray.tsx`** -> AI Confidence: **99.24%**
726. **`packages/canvas-rce/src/util/loadingPlaceholder.ts`** -> AI Confidence: **99.24%**
727. **`ui/engine/capabilities/IntlPolyfills/index.ts`** -> AI Confidence: **99.24%**
728. **`ui/features/accessibility/accessibility_checker/react/components/AccessibilityCourseScan/AccessibilityCourseScan.tsx`** -> AI Confidence: **99.24%**
729. **`ui/features/accessibility/accessibility_checker/react/components/AccessibilityIssuesSummary/AccessibilityIssuesSummary.tsx`** -> AI Confidence: **99.24%**
730. **`ui/features/accessibility/accessibility_checker/react/components/AccessibilityIssuesTable/AccessibilityIssuesTable.tsx`** -> AI Confidence: **99.24%**
731. **`ui/features/accessibility/shared/react/components/AccessibilityIssuesContent/Form/CheckboxTextInput.tsx`** -> AI Confidence: **99.24%**
732. **`ui/features/account_admin_tools/react/CommMessages/CommMessageList.tsx`** -> AI Confidence: **99.24%**
733. **`ui/features/account_grading_settings/components/account_grading_status/EditStatusPopover.tsx`** -> AI Confidence: **99.24%**
734. **`ui/features/account_grading_standards/react/GradingPeriodSet.tsx`** -> AI Confidence: **99.24%**
735. **`ui/features/account_reports/react/components/ReportProgress.tsx`** -> AI Confidence: **99.24%**
736. **`ui/features/account_reports/react/components/ReportRun.tsx`** -> AI Confidence: **99.24%**
737. **`ui/features/account_reports/react/components/ReportsTable.tsx`** -> AI Confidence: **99.24%**
738. **`ui/features/account_settings/react/components/Whitelist.tsx`** -> AI Confidence: **99.24%**
739. **`ui/features/account_settings/react/internal_settings/InternalSettingsManager.tsx`** -> AI Confidence: **99.24%**
740. **`ui/features/account_settings/react/notification_settings/index.tsx`** -> AI Confidence: **99.24%**
741. **`ui/features/ai_experiences_edit/index.tsx`** -> AI Confidence: **99.24%**
742. **`ui/features/ai_experiences_index/react/AiExperiencesIndex.tsx`** -> AI Confidence: **99.24%**
743. **`ui/features/announcements/react/components/IndexHeader.tsx`** -> AI Confidence: **99.24%**
744. **`ui/features/assignment_edit/react/DefaultToolForm.tsx`** -> AI Confidence: **99.24%**
745. **`ui/features/assignment_edit/react/TurnitinSettingsModal.tsx`** -> AI Confidence: **99.24%**
746. **`ui/features/assignment_index/backbone/views/IndexView.tsx`** -> AI Confidence: **99.24%**
747. **`ui/features/assignment_index/react/bulk_edit/BulkEditHeader.tsx`** -> AI Confidence: **99.24%**
748. **`ui/features/assignments_peer_reviews/index.tsx`** -> AI Confidence: **99.24%**
749. **`ui/features/assignments_peer_reviews_student/react/components/AssignmentSubmission.tsx`** -> AI Confidence: **99.24%**
750. **`ui/features/assignments_peer_reviews_student/react/hooks/useRubricAssessment.ts`** -> AI Confidence: **99.24%**
751. **`ui/features/assignments_show_student/react/components/LoginActionPrompt.tsx`** -> AI Confidence: **99.24%**
752. **`ui/features/authentication_providers/jquery/account_authorization_configs.tsx`** -> AI Confidence: **99.24%**
753. **`ui/features/blueprint_course_master/react/components/CourseFilter.tsx`** -> AI Confidence: **99.24%**
754. **`ui/features/change_password/react/ConfirmChangePassword.tsx`** -> AI Confidence: **99.24%**
755. **`ui/features/conferences/react/components/BBBModalOptions/BBBModalOptions.tsx`** -> AI Confidence: **99.24%**
756. **`ui/features/content_migrations/react/components/MissingPolicyWarningModal.tsx`** -> AI Confidence: **99.24%**
757. **`ui/features/content_migrations/react/components/content_selection_modal.tsx`** -> AI Confidence: **99.24%**
758. **`ui/features/content_migrations/react/components/migration_row.tsx`** -> AI Confidence: **99.24%**
759. **`ui/features/content_migrations/react/components/migrator_forms/question_bank_selector.tsx`** -> AI Confidence: **99.24%**
760. **`ui/features/content_migrations/react/components/migrator_forms/zip_file.tsx`** -> AI Confidence: **99.24%**
761. **`ui/features/content_shares/react/CourseImportPanel.tsx`** -> AI Confidence: **99.24%**
762. **`ui/features/content_shares/react/ReceivedTable.tsx`** -> AI Confidence: **99.24%**
763. **`ui/features/context_modules_v2/react/componentsStudents/ModuleStudent.tsx`** -> AI Confidence: **99.24%**
764. **`ui/features/context_modules_v2/react/componentsTeacher/AddItemModalComponents/AddItemModal.tsx`** -> AI Confidence: **99.24%**
765. **`ui/features/context_modules_v2/react/componentsTeacher/AddItemModalComponents/CreateLearningObjectForm.tsx`** -> AI Confidence: **99.24%**
766. **`ui/features/context_modules_v2/react/componentsTeacher/ModuleItemList.tsx`** -> AI Confidence: **99.24%**
767. **`ui/features/context_modules_v2/react/componentsTeacher/ModulesList.tsx`** -> AI Confidence: **99.24%**
768. **`ui/features/context_modules_v2/react/hooks/mutations/useAddModuleItem.ts`** -> AI Confidence: **99.24%**
769. **`ui/features/copy_course/react/components/form/formComponents/ConfiguredDateInput.tsx`** -> AI Confidence: **99.24%**
770. **`ui/features/course_paces/react/components/course_pace_table/assignment_row.tsx`** -> AI Confidence: **99.24%**
771. **`ui/features/course_paces/react/components/pace_contexts_table.tsx`** -> AI Confidence: **99.24%**
772. **`ui/features/course_settings/react/components/CourseNavigationSettings.tsx`** -> AI Confidence: **99.24%**
773. **`ui/features/developer_keys_v2/react/ManualConfigurationForm/AdditionalSettings.tsx`** -> AI Confidence: **99.24%**
774. **`ui/features/developer_keys_v2/react/NewKeyForm.tsx`** -> AI Confidence: **99.24%**
775. **`ui/features/developer_keys_v2/react/Scopes.tsx`** -> AI Confidence: **99.24%**
776. **`ui/features/discussion_topics_index/react/components/DiscussionsIndex.tsx`** -> AI Confidence: **99.24%**
777. **`ui/features/discussion_topics_post/react/components/DiscussionDetails/DiscussionDetails.tsx`** -> AI Confidence: **99.24%**
778. **`ui/features/discussion_topics_post/react/components/DiscussionEdit/DiscussionEdit.tsx`** -> AI Confidence: **99.24%**
779. **`ui/features/discussion_topics_post/react/components/DiscussionPostToolbar/DiscussionPostButtonsToolbar.tsx`** -> AI Confidence: **99.24%**
780. **`ui/features/discussion_topics_post/react/containers/DiscussionTopicRepliesContainer/DiscussionTopicRepliesContainer.tsx`** -> AI Confidence: **99.24%**
781. **`ui/features/discussion_topics_post/react/containers/DiscussionTranslationModuleContainer/DiscussionTranslationModuleContainer.tsx`** -> AI Confidence: **99.24%**
782. **`ui/features/enhanced_individual_gradebook/react/components/AssignmentInformation/DefaultGradeModal.tsx`** -> AI Confidence: **99.24%**
783. **`ui/features/enhanced_individual_gradebook/react/components/EnhancedIndividualGradebook.tsx`** -> AI Confidence: **99.24%**
784. **`ui/features/enhanced_individual_gradebook/react/components/GlobalSettings/GradebookScoreExport.tsx`** -> AI Confidence: **99.24%**
785. **`ui/features/enhanced_individual_gradebook/react/components/GradingResults/DefaultGradeInput.tsx`** -> AI Confidence: **99.24%**
786. **`ui/features/enhanced_individual_gradebook/react/components/LearningMasteryTabsView.tsx`** -> AI Confidence: **99.24%**
787. **`ui/features/enhanced_individual_gradebook/react/components/StudentInformation/FinalGradeOverrideContainer.tsx`** -> AI Confidence: **99.24%**
788. **`ui/features/eportfolio/react/PageEditModal.tsx`** -> AI Confidence: **99.24%**
789. **`ui/features/eportfolio/react/SectionEditModal.tsx`** -> AI Confidence: **99.24%**
790. **`ui/features/eportfolio/react/SubmissionModal.tsx`** -> AI Confidence: **99.24%**
791. **`ui/features/external_apps/react/components/configuration_forms/ConfigurationFormXml.tsx`** -> AI Confidence: **99.24%**
792. **`ui/features/files_v2/react/components/FileFolderTable/Breadcrumbs.tsx`** -> AI Confidence: **99.24%**
793. **`ui/features/files_v2/react/components/FileFolderTable/BulkActionButtons.tsx`** -> AI Confidence: **99.24%**
794. **`ui/features/files_v2/react/components/FileFolderTable/DeleteModal/DeleteModal.tsx`** -> AI Confidence: **99.24%**
795. **`ui/features/files_v2/react/components/FileFolderTable/FileFolderTable.tsx`** -> AI Confidence: **99.24%**
796. **`ui/features/files_v2/react/components/FileFolderTable/FilePreviewTray/CommonFileInfo.tsx`** -> AI Confidence: **99.24%**
797. **`ui/features/files_v2/react/components/FileFolderTable/MoveModal/utils.tsx`** -> AI Confidence: **99.24%**
798. **`ui/features/files_v2/react/components/FileFolderTable/PermissionsModal/PermissionsModal.tsx`** -> AI Confidence: **99.24%**
799. **`ui/features/files_v2/react/components/FilesApp.tsx`** -> AI Confidence: **99.24%**
800. **`ui/features/files_v2/react/components/RenameModal.tsx`** -> AI Confidence: **99.24%**
801. **`ui/features/files_v2/utils/downloadUtils.ts`** -> AI Confidence: **99.24%**
802. **`ui/features/grade_summary/react/OutcomeDetailModal.tsx`** -> AI Confidence: **99.24%**
803. **`ui/features/gradebook/react/AssignmentPostingPolicyTray/index.tsx`** -> AI Confidence: **99.24%**
804. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/editors/AssignmentGradeInput/GradingSchemeGradeInput.tsx`** -> AI Confidence: **99.24%**
805. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/formatters/TotalGradeCellFormatter.ts`** -> AI Confidence: **99.24%**
806. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/headers/AssignmentGroupColumnHeader.tsx`** -> AI Confidence: **99.24%**
807. **`ui/features/gradebook/react/default_gradebook/GradebookGrid/headers/TotalGradeColumnHeader.tsx`** -> AI Confidence: **99.24%**
808. **`ui/features/gradebook/react/default_gradebook/components/ActionMenu.tsx`** -> AI Confidence: **99.24%**
809. **`ui/features/gradebook/react/default_gradebook/components/SubmissionCommentForm.tsx`** -> AI Confidence: **99.24%**
810. **`ui/features/gradebook/react/default_gradebook/components/SubmissionCommentListItem.tsx`** -> AI Confidence: **99.24%**
811. **`ui/features/gradebook/react/default_gradebook/components/SubmissionTray.tsx`** -> AI Confidence: **99.24%**
812. **`ui/features/gradebook_history/react/SearchResultsRow.tsx`** -> AI Confidence: **99.24%**
813. **`ui/features/inbox/react/components/ConversationListHolder/ConversationListHolder.tsx`** -> AI Confidence: **99.24%**
814. **`ui/features/inbox/react/components/MessageDetailParticipants/MessageDetailParticipants.tsx`** -> AI Confidence: **99.24%**
815. **`ui/features/inbox/react/containers/InboxSettingsModalContainer/InboxSettingsModalContainer.tsx`** -> AI Confidence: **99.24%**
816. **`ui/features/inbox/react/containers/MessageListActionContainer.tsx`** -> AI Confidence: **99.24%**
817. **`ui/features/job_stats/react/components/JobStats.tsx`** -> AI Confidence: **99.24%**
818. **`ui/features/job_stats/react/components/JobStatsTable.tsx`** -> AI Confidence: **99.24%**
819. **`ui/features/learning_mastery_v2/react/components/grid/BarChartRow.tsx`** -> AI Confidence: **99.24%**
820. **`ui/features/learning_mastery_v2/react/components/grid/StudentCellPopover.tsx`** -> AI Confidence: **99.24%**
821. **`ui/features/learning_mastery_v2/react/components/popovers/OutcomeDistributionPopover.tsx`** -> AI Confidence: **99.24%**
822. **`ui/features/learning_mastery_v2/react/index.tsx`** -> AI Confidence: **99.24%**
823. **`ui/features/lti_registrations/discover/ProductConfigureButton.tsx`** -> AI Confidence: **99.24%**
824. **`ui/features/lti_registrations/manage/dynamic_registration_wizard/DynamicRegistrationWizard.tsx`** -> AI Confidence: **99.24%**
825. **`ui/features/lti_registrations/manage/inherited_key_registration_wizard/InheritedKeyRegistrationReview.tsx`** -> AI Confidence: **99.24%**
826. **`ui/features/lti_registrations/manage/registration_wizard/RegistrationWizardInitialization.tsx`** -> AI Confidence: **99.24%**
827. **`ui/features/lti_registrations/manage/registration_wizard/RegistrationWizardModal.tsx`** -> AI Confidence: **99.24%**
828. **`ui/features/lti_registrations/manage/registration_wizard_forms/IconConfirmation.tsx`** -> AI Confidence: **99.24%**
829. **`ui/features/lti_registrations/manage/registration_wizard_forms/LaunchSettingsConfirmation.tsx`** -> AI Confidence: **99.24%**
830. **`ui/features/lti_registrations/manage/registration_wizard_forms/PermissionConfirmation.tsx`** -> AI Confidence: **99.24%**
831. **`ui/features/lti_registrations/manage/registration_wizard_forms/ReviewScreen.tsx`** -> AI Confidence: **99.24%**
832. **`ui/features/navigation_header/index.tsx`** -> AI Confidence: **99.24%**
833. **`ui/features/navigation_header/react/SideNav.tsx`** -> AI Confidence: **99.24%**
834. **`ui/features/new_login/pages/ForgotPassword.tsx`** -> AI Confidence: **99.24%**
835. **`ui/features/outcome_management/react/Management/OutcomeRemoveModal.tsx`** -> AI Confidence: **99.24%**
836. **`ui/features/password_complexity_configuration/react/CustomForbiddenWordsSection.tsx`** -> AI Confidence: **99.24%**
837. **`ui/features/qr_mobile_login/react/components/QRMobileLogin.tsx`** -> AI Confidence: **99.24%**
838. **`ui/features/rate_limiting_settings/react/EditRateLimitModal.tsx`** -> AI Confidence: **99.24%**
839. **`ui/features/rate_limiting_settings/react/RateLimitingSettingsApp.tsx`** -> AI Confidence: **99.24%**
840. **`ui/features/release_notes_edit/react/CreateEditModal.tsx`** -> AI Confidence: **99.24%**
841. **`ui/features/rubrics/components/ViewRubrics/RubricTable.tsx`** -> AI Confidence: **99.24%**
842. **`ui/features/section/react/UncrosslistForm.tsx`** -> AI Confidence: **99.24%**
843. **`ui/features/speed_grader/jquery/speed_grader.utils.tsx`** -> AI Confidence: **99.24%**
844. **`ui/features/speed_grader/react/AssessmentAuditTray/components/AssessmentSummary.tsx`** -> AI Confidence: **99.24%**
845. **`ui/features/speed_grader/react/CommentArea.tsx`** -> AI Confidence: **99.24%**
846. **`ui/features/sub_accounts/react/SubaccountNameForm.tsx`** -> AI Confidence: **99.24%**
847. **`ui/features/theme_editor/react/SaveThemeButton.tsx`** -> AI Confidence: **99.24%**
848. **`ui/features/widget_dashboard/react/WidgetDashboardContainer.tsx`** -> AI Confidence: **99.24%**
849. **`ui/features/widget_dashboard/react/components/DashboardNotifications.tsx`** -> AI Confidence: **99.24%**
850. **`ui/features/widget_dashboard/react/components/widgets/RecentGradesWidget/GradeItem.tsx`** -> AI Confidence: **99.24%**
851. **`ui/features/widget_dashboard/react/components/widgets/RecentGradesWidget/RecentGradesWidget.tsx`** -> AI Confidence: **99.24%**
852. **`ui/features/widget_dashboard/react/hooks/useAnnouncements.ts`** -> AI Confidence: **99.24%**
853. **`ui/features/youtube_migration/react/App.tsx`** -> AI Confidence: **99.24%**
854. **`ui/shared/account_reports/react/RunReportForm.tsx`** -> AI Confidence: **99.24%**
855. **`ui/shared/assignments/react/CommentsTray/CommentsTrayBody.tsx`** -> AI Confidence: **99.24%**
856. **`ui/shared/assignments/react/CreateEditAssignmentModal.tsx`** -> AI Confidence: **99.24%**
857. **`ui/shared/assignments/react/DateDue.tsx`** -> AI Confidence: **99.24%**
858. **`ui/shared/block-content-editor/react/Blocks/BlockItems/SettingsImageInfos/SettingsImageInfos.tsx`** -> AI Confidence: **99.24%**
859. **`ui/shared/block-content-editor/react/accessibilityChecker/AccessibilityCheckerPopover.tsx`** -> AI Confidence: **99.24%**
860. **`ui/shared/block-editor/react/components/user/blocks/GroupBlock/GroupBlock.tsx`** -> AI Confidence: **99.24%**
861. **`ui/shared/block-editor/react/components/user/blocks/HeadingBlock/HeadingBlock.tsx`** -> AI Confidence: **99.24%**
862. **`ui/shared/block-editor/react/components/user/blocks/ImageBlock/ImageBlock.tsx`** -> AI Confidence: **99.24%**
863. **`ui/shared/block-editor/react/components/user/blocks/RCETextBlock/RCETextBlock.tsx`** -> AI Confidence: **99.24%**
864. **`ui/shared/block-editor/react/components/user/blocks/RCETextBlock/RCETextBlockPopup.tsx`** -> AI Confidence: **99.24%**
865. **`ui/shared/block-editor/react/components/user/blocks/TabsBlock/TabsBlock.tsx`** -> AI Confidence: **99.24%**
866. **`ui/shared/block-editor/react/components/user/blocks/TextBlock/TextBlock.tsx`** -> AI Confidence: **99.24%**
867. **`ui/shared/calendar/react/RecurringEvents/RepeatPicker/RepeatPicker.tsx`** -> AI Confidence: **99.24%**
868. **`ui/shared/canvas-studio-player/react/CanvasStudioPlayer.tsx`** -> AI Confidence: **99.24%**
869. **`ui/shared/color-picker/react/index.tsx`** -> AI Confidence: **99.24%**
870. **`ui/shared/content-migrations/react/CommonMigratorControls/DateAdjustments.tsx`** -> AI Confidence: **99.24%**
871. **`ui/shared/context-modules/differentiated-modules/react/Item/ItemAssignToTray.tsx`** -> AI Confidence: **99.24%**
872. **`ui/shared/context-modules/differentiated-modules/react/RequirementForm.tsx`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/canvas-rce/src/translations/tinymce/ca.js` -> **100.0%** Exposure
- `packages/canvas-rce/src/translations/tinymce/cs.js` -> **100.0%** Exposure
- `packages/canvas-rce/src/translations/tinymce/da.js` -> **100.0%** Exposure
- `packages/canvas-rce/src/translations/tinymce/de.js` -> **100.0%** Exposure
- `packages/canvas-rce/src/translations/tinymce/fr_FR.js` -> **100.0%** Exposure
### Exploit Generation Surface
- `app/controllers/account_calendars_api_controller.rb` -> **100.0%** Exposure
- `app/controllers/account_notifications_controller.rb` -> **100.0%** Exposure
- `app/controllers/accounts_controller.rb` -> **100.0%** Exposure
- `app/controllers/ai_experiences_controller.rb` -> **100.0%** Exposure
- `app/controllers/announcements_api_controller.rb` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `app/controllers/account_reports_controller.rb` -> **100.0%** Exposure
- `app/controllers/jobs_v2_controller.rb` -> **100.0%** Exposure
- `app/controllers/quizzes/quiz_reports_controller.rb` -> **100.0%** Exposure
- `app/models/account_report_runner.rb` -> **100.0%** Exposure
- `app/models/course_section.rb` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `ui/features/quizzes/jquery/calcCmd.js` -> **36.4011%** Exposure
- `ui/features/developer_keys_v2/react/__tests__/fixtures/responses.js` -> **26.1301%** Exposure
### Algorithmic DoS Exposure
- `Gemfile` -> **100.0%** Exposure
- `app/controllers/account_notifications_controller.rb` -> **100.0%** Exposure
- `app/controllers/accounts_controller.rb` -> **100.0%** Exposure
- `app/controllers/announcements_api_controller.rb` -> **100.0%** Exposure
- `app/controllers/application_controller.rb` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `123` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28679` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ui/features/blueprint_course_master/react/components/CourseFilter.tsx` (TYPESCRIPT) -> Cumulative Risk: **928.33**
- **Archetype:** `file_cluster_13` (Distance: 12.951 IQR)
- **Magnitude:** 14.55 | **LOC:** 190 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `handleBlur` (Impact: 25.0), `getSearchText` (Impact: 10.1), `componentDidUpdate` (Impact: 9.1)

### 2. `ui/features/gradebook/react/shared/GradebookExportManager.ts` (TYPESCRIPT) -> Cumulative Risk: **885.03**
- **Archetype:** `file_cluster_4` (Distance: 12.958 IQR)
- **Magnitude:** 31.43 | **LOC:** 256 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `monitorExport` (Impact: 79.7), `constructor` (Impact: 29.2), `setExportState` (Impact: 12.3)

### 3. `ui/features/manage_groups/backbone/views/GroupUserView.tsx` (TYPESCRIPT) -> Cumulative Risk: **877.03**
- **Archetype:** `file_cluster_4` (Distance: 12.405 IQR)
- **Magnitude:** 13.09 | **LOC:** 189 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `renderGroupUserMenu` (Impact: 12.9), `toJSON` (Impact: 9.2), `isLeader` (Impact: 4.4)

### 4. `ui/features/files/react/legacy/components/FolderChild.jsx` (JAVASCRIPT) -> Cumulative Risk: **875.27**
- **Archetype:** `file_cluster_13` (Distance: 13.441 IQR)
- **Magnitude:** 208.58 | **LOC:** 186 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `getAttributesForRootNode` (Impact: 28.1), `focusNameInput` (Impact: 9.3), `saveNameEdit` (Impact: 8.1)

### 5. `ui/features/course_link_validator/react/LinkValidator.tsx` (TYPESCRIPT) -> Cumulative Risk: **873.85**
- **Archetype:** `file_cluster_13` (Distance: 12.03 IQR)
- **Magnitude:** 19.45 | **LOC:** 189 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getResults` (Impact: 98.0), `render` (Impact: 12.8), `startValidation` (Impact: 4.0)

### 6. `ui/shared/confetti/javascript/ConfettiGenerator.ts` (TYPESCRIPT) -> Cumulative Risk: **871.39**
- **Archetype:** `file_cluster_4` (Distance: 13.847 IQR)
- **Magnitude:** 28.37 | **LOC:** 154 | **CtrlFlow:** 73.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `drawParticle` (Impact: 56.8), `render` (Impact: 44.5), `constructor` (Impact: 15.5)

### 7. `ui/features/files/react/legacy/components/ShowFolder.js` (JAVASCRIPT) -> Cumulative Risk: **866.46**
- **Archetype:** `file_cluster_17` (Distance: 13.775 IQR)
- **Magnitude:** 188.2 | **LOC:** 152 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `redirectToCourseFiles` (Impact: 22.4), `updateAPIQuerySortParams` (Impact: 18.3), `componentDidUpdate` (Impact: 6.1)

### 8. `ui/shared/files/react/modules/ZipUploader.js` (JAVASCRIPT) -> Cumulative Risk: **854.56**
- **Archetype:** `file_cluster_4` (Distance: 12.714 IQR)
- **Magnitude:** 239.7 | **LOC:** 156 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `pullMigrationProgress` (Impact: 42.4), `getContentMigration` (Impact: 28.6), `createPreFlightParams` (Impact: 7.1)

### 9. `ui/features/files/MasterCourseLock.jsx` (JAVASCRIPT) -> Cumulative Risk: **849.02**
- **Archetype:** `file_cluster_13` (Distance: 12.639 IQR)
- **Magnitude:** 141.16 | **LOC:** 136 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `render` (Impact: 24.3), `toggleLockedState` (Impact: 16.4), `setLocked` (Impact: 3.1)

### 10. `ui/features/gradebook/react/default_gradebook/Gradebook.tsx` (TYPESCRIPT) -> Cumulative Risk: **847.38**
- **Archetype:** `file_cluster_13` (Distance: 14.792 IQR)
- **Magnitude:** 474.06 | **LOC:** 5644 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `bindGridEvents` (Impact: 3249.6), `constructor` (Impact: 58.5), `updateColumnOrder` (Impact: 8.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/models/course.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.457 IQR)
- **Top Global Matches:** file_cluster_8: 12.457, file_cluster_0: 12.531, file_cluster_11: 12.779
- **Magnitude:** 11293.88 | **LOC:** 5058 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 643
- **Risk Profile:** Cognitive Load (52.703%), Tech Debt (7.8477%)
**Top Internal Functions/Classes:**
  * `custom_visibility_option_[Truncated]` (Impact: 9044.4 | O(N^6) | DB: 643)
  * `__global_context__` (Impact: 1204.6 | O(N^6))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
  * `Course` (Impact: 551.7 | O(2^N) | DB: 314)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
  * `Anonymous_Block` (Impact: 55.4 | O(N^6))
  * `build_role_map` (Impact: 35.7 | O(N^3) | DB: 7)
    * *Intent:* # returns a mapping from (existing role id => role id in the new account), matching by role name and...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1719`, `structural_boundaries: 574`, `args: 311`, `func_start: 353`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 239`, `dead_code: 6`, `planned_debt: 2`
* *Architecture:* `io: 312`, `api: 4`
* *Defense:* `safety: 78`, `test: 127`, `sync_locks: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` FeatureFlags, LearningOutcomeContext, OutcomeImportContext, MaterialChanges, Accessibility::Scannable, the, ContentNotices, Courses::ItemVisibilityHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/submission.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.846 IQR)
- **Top Global Matches:** file_cluster_8: 11.846, file_cluster_0: 12.108, file_cluster_11: 12.231
- **Magnitude:** 11049.4 | **LOC:** 3892 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 189
- **Risk Profile:** Cognitive Load (65.9652%), Tech Debt (49.2793%)
**Top Internal Functions/Classes:**
  * `ensure_grader_can_grade` (Impact: 5068.4 | O(N^6) | DB: 178)
  * `Submission` (Impact: 2696.2 | O(2^N) | DB: 189)
  * `lti_attempt_id` (Impact: 990.7 | O(N^6) | DB: 15)
  * `view_report_url` (Impact: 637.1 | O(2^N) | DB: 21)
  * `infer_values` (Impact: 170.8 | O(N^5) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1585`, `structural_boundaries: 475`, `args: 219`, `func_start: 277`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 210`, `dead_code: 7`, `planned_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 28`
* *Architecture:* `io: 134`, `import: 1`
* *Defense:* `safety: 71`, `doc: 3`, `test: 71`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HtmlTextHelper, CustomValidations, SendToStream, the, Tardiness, Workflow, LinkedAttachmentHandler, anonymity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/courses_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.302 IQR)
- **Top Global Matches:** file_cluster_8: 13.302, file_cluster_17: 13.45, file_cluster_2: 13.511
- **Magnitude:** 9784.88 | **LOC:** 4757 | **CtrlFlow:** 81.4% | **Authorship Centralization:** 29.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 137
- **Risk Profile:** Cognitive Load (69.2795%), Tech Debt (59.5977%)
**Top Internal Functions/Classes:**
  * `accept_enrollment` (Impact: 3945.4 | O(2^N) | DB: 137)
    * *Intent:* # Internal: Accept an enrollment invitation and redirect. # # enrollment - An enrollment object to a...
  * `Anonymous_Block` (Impact: 1434.2 | O(N^6) | DB: 73)
  * `CoursesController` (Impact: 1206.2 | O(N^6) | DB: 74)
    * *Intent:* # # @model CalendarLink # { # "id": "CalendarLink", # "description": "", # "properties": { # "ics": ...
  * `settings` (Impact: 552.1 | O(2^N) | DB: 16)
  * `courses_for_user` (Impact: 487.3 | O(N^6) | DB: 47)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1223`, `structural_boundaries: 280`, `args: 101`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 575`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 12`, `orphaned_logic: 22`
* *Architecture:* `io: 95`, `import: 5`
* *Defense:* `safety: 61`, `doc: 62`, `test: 445`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CustomSidebarLinksHelper, courses, each, the, Api::V1::Progress, ObserverEnrollmentsHelper, Api::V1::Course, Api::V1::PreviewHtml...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/application_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.278 IQR)
- **Top Global Matches:** file_cluster_8: 13.278, file_cluster_0: 13.458, file_cluster_17: 13.468
- **Magnitude:** 9577.98 | **LOC:** 3694 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 21.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (83.688%), Tech Debt (14.3929%)
**Top Internal Functions/Classes:**
  * `rescue_action_in_public_[Truncated]` (Impact: 3829.8 | O(N^6) | DB: 125)
    * *Intent:* # Custom error catching and message rendering.
  * `ApplicationController` (Impact: 1856.5 | O(N^6) | DB: 22)
    * *Intent:* # Software Foundation, version 3 of the License. # # Canvas is distributed in the hope that it will ...
  * `get_feed_context` (Impact: 1030.1 | O(N^6) | DB: 54)
    * *Intent:* # Used to retrieve the context from a :feed_code parameter. These # :feed_code attributes are keyed ...
  * `require_context_type` (Impact: 863.5 | O(N^6) | DB: 52)
  * `authorized_action` (Impact: 453.8 | O(2^N) | DB: 10)
    * *Intent:* # checks the authorization policy for the given object using # the vendor/plugins/adheres_to_policy ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1408`, `structural_boundaries: 387`, `args: 154`, `func_start: 229`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 488`, `dead_code: 8`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 39`, `concurrency: 1`
* *Defense:* `safety: 129`, `doc: 4`, `test: 385`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LocaleSelection, Api::V1::WikiPage, Api::V1::User, AuthenticationMethods, Api::V1::Group, Api, one, ObserverEnrollmentsHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/abstract_assignment.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.879 IQR)
- **Top Global Matches:** file_cluster_8: 11.879, file_cluster_0: 12.251, file_cluster_11: 12.382
- **Magnitude:** 9484.38 | **LOC:** 4798 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 660
- **Risk Profile:** Cognitive Load (34.2081%), Tech Debt (9.1582%)
**Top Internal Functions/Classes:**
  * `AbstractAssignment_[Truncated]` (Impact: 9237.4 | O(N^6) | DB: 660)
  * `__global_context__` (Impact: 2.0 | O(N^1))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1817`, `structural_boundaries: 590`, `args: 284`, `func_start: 352`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 172`, `dead_code: 4`, `planned_debt: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 198`, `import: 2`
* *Defense:* `safety: 65`, `doc: 7`, `test: 130`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HasContentTags, Canvas::DraftStateValidations, SearchTermHelper, that, Workflow, draft_state_validations, CopyAuthorizedLinks, TextHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/account.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.375 IQR)
- **Top Global Matches:** file_cluster_0: 12.375, file_cluster_8: 12.409, file_cluster_11: 12.606
- **Magnitude:** 8191.4 | **LOC:** 3073 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 28.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 211
- **Risk Profile:** Cognitive Load (64.3859%), Tech Debt (29.2817%)
**Top Internal Functions/Classes:**
  * `Account` (Impact: 4600.9 | O(2^N) | DB: 211)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
  * `tabs_available` (Impact: 1816.4 | O(N^6) | DB: 140)
  * `self.sub_accounts_recursive_sql` (Impact: 801.2 | O(N^6) | DB: 67)
    * *Intent:* # the default ordering will have each tier in a group, followed by the next tier, etc. # if an order...
  * `validate_url_setting` (Impact: 121.0 | O(N^2) | DB: 13)
  * `update_account_associations` (Impact: 84.8 | O(2^N) | DB: 6)
    * *Intent:* # Updates account associations for all the courses and users associated with this account
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1002`, `structural_boundaries: 435`, `args: 230`, `func_start: 281`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 253`, `dead_code: 5`, `planned_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 121`, `api: 38`, `import: 3`
* *Defense:* `safety: 44`, `doc: 6`, `test: 60`, `sync_locks: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Context, BrandConfigHelpers, FeatureFlags, LearningOutcomeContext, OutcomeImportContext, RubricContext, Canvas::Security::PasswordPolicyAccountSettingValidator, StickySisFields...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/models/user.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.208 IQR)
- **Top Global Matches:** file_cluster_8: 12.208, file_cluster_0: 12.234, file_cluster_11: 12.48
- **Magnitude:** 7948.76 | **LOC:** 4120 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 411
- **Risk Profile:** Cognitive Load (46.664%), Tech Debt (25.9417%)
**Top Internal Functions/Classes:**
  * `avatar_location_[Truncated]` (Impact: 4194.4 | O(N^6) | DB: 411)
  * `__global_context__` (Impact: 1270.0 | O(N^6))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
  * `associate_with_shard` (Impact: 957.1 | O(N^6) | DB: 31)
  * `User` (Impact: 554.1 | O(2^N) | DB: 297)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
  * `gravatar_url` (Impact: 243.3 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1163`, `structural_boundaries: 501`, `args: 334`, `func_start: 339`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 194`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 14`
* *Architecture:* `io: 276`
* *Defense:* `safety: 52`, `test: 69`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` FeatureFlags, after, the, ModelCache, UserLearningObjectScopes, it, TimeZoneHelper, ManyRootAccounts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/initializers/active_record.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.817 IQR)
- **Top Global Matches:** file_cluster_8: 11.817, file_cluster_11: 12.133, file_cluster_17: 12.176
- **Magnitude:** 7675.1 | **LOC:** 2342 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 222
- **Risk Profile:** Cognitive Load (23.8376%), Tech Debt (14.2869%)
**Top Internal Functions/Classes:**
  * `in_batches_with_temp_table_[Truncated]` (Impact: 3761.0 | O(N^6) | DB: 222)
  * `ActiveRecord::Base` (Impact: 3674.7 | O(2^N) | DB: 84)
  * `in_batches_with_pluck_ids` (Impact: 2.9 | O(N^1) | DB: 3)
    * *Intent:* # in some cases we're doing a lot of work inside # the yielded block, and holding open a transaction...
  * `__global_context__` (Impact: 2.5 | O(N^1))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 656`, `structural_boundaries: 436`, `args: 195`, `func_start: 179`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 198`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 77`, `import: 10`
* *Defense:* `safety: 33`, `doc: 5`, `test: 6`, `sync_locks: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` a, UpdateAndDeleteWithJoins, VersionAgnosticPreloader, ClassMethods, UserContentSerialization, UpdateAndDeleteAllWithLimit, WithMigrationAdvisoryLock, ActiveSupport::Callbacks::Suspension...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/attachment.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.816 IQR)
- **Top Global Matches:** file_cluster_8: 11.816, file_cluster_0: 11.981, file_cluster_11: 12.126
- **Magnitude:** 7074.82 | **LOC:** 2830 | **CtrlFlow:** 76.6% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 375
- **Risk Profile:** Cognitive Load (59.3542%), Tech Debt (15.7549%)
**Top Internal Functions/Classes:**
  * `infer_namespace` (Impact: 4621.3 | O(N^6) | DB: 375)
  * `Attachment` (Impact: 812.0 | O(2^N) | DB: 26)
    * *Intent:* # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Aff...
  * `infer_encoding` (Impact: 688.2 | O(N^5) | DB: 53)
  * `ingest_to_pine` (Impact: 580.0 | O(2^N) | DB: 6)
  * `delete_from_pine` (Impact: 60.4 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 323`, `args: 140`, `func_start: 203`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 119`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 141`, `api: 5`, `import: 2`
* *Defense:* `safety: 74`, `test: 151`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HasContentTags, ContextModuleItem, MasterCourses::Restrictor, Workflow, amazon_s3, SearchTermHelper, file_store, DatesOverridable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/discussion_topic.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.476 IQR)
- **Top Global Matches:** file_cluster_8: 11.476, file_cluster_0: 11.732, file_cluster_11: 11.893
- **Magnitude:** 6014.06 | **LOC:** 2345 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 393
- **Risk Profile:** Cognitive Load (33.0667%), Tech Debt (9.1644%)
**Top Internal Functions/Classes:**
  * `DiscussionTopic_[Truncated]` (Impact: 5911.7 | O(N^6) | DB: 393)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 955`, `structural_boundaries: 290`, `args: 185`, `func_start: 169`, `class_start: 6`
* *Risk/State:* `state_mutation: 66`, `dead_code: 7`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 123`, `import: 1`
* *Defense:* `safety: 39`, `test: 124`, `sync_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HasContentTags, Accessibility::Scannable, SearchTermHelper, SendToStream, media, Workflow, TextHelper, CopyAuthorizedLinks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/users_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.256 IQR)
- **Top Global Matches:** file_cluster_8: 13.256, file_cluster_17: 13.256, file_cluster_2: 13.368
- **Magnitude:** 5658.48 | **LOC:** 3635 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(N^6) | **DB Complexity:** 344
- **Risk Profile:** Cognitive Load (39.7839%), Tech Debt (10.8975%)
**Top Internal Functions/Classes:**
  * `UsersController_[Truncated]` (Impact: 5191.1 | O(N^6) | DB: 344)
    * *Intent:* # "avatar_image_url": { # "description": "A URL to retrieve a generic avatar.", # "example": "https:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 826`, `structural_boundaries: 206`, `args: 91`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 426`, `dead_code: 4`, `planned_debt: 8`, `orphaned_logic: 1`
* *Architecture:* `io: 64`
* *Defense:* `safety: 49`, `doc: 71`, `test: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the, ObserverEnrollmentsHelper, Api::V1::CalendarEvent, lti_context_id, on, Pronouns, Api::V1::Account, Api::V1::User...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/saml/inc-md-cert-mdq.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/saml/ukfederation.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/assignments_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.979 IQR)
- **Top Global Matches:** file_cluster_8: 11.979, file_cluster_17: 12.236, file_cluster_0: 12.374
- **Magnitude:** 4665.86 | **LOC:** 1391 | **CtrlFlow:** 82.5% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 134
- **Risk Profile:** Cognitive Load (49.0947%), Tech Debt (13.7631%)
**Top Internal Functions/Classes:**
  * `syllabus` (Impact: 1885.2 | O(2^N) | DB: 44)
  * `show` (Impact: 1261.1 | O(N^6) | DB: 134)
  * `render_a2_student_view` (Impact: 732.7 | O(2^N))
  * `unpublish_quizzes` (Impact: 466.1 | O(N^6) | DB: 7)
    * *Intent:* # unpulish a N.Q assignment from Quizzes Page
  * `AssignmentsController` (Impact: 81.1 | O(N^3) | DB: 2)
    * *Intent:* # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU Aff...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 116`, `args: 31`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 152`, `dead_code: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 47`, `import: 1`
* *Defense:* `safety: 28`, `doc: 4`, `test: 238`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SyllabusHelper, Api::V1::AssignmentOverride, Api::V1::Rubric, Api::V1::Outcome, Api::V1::ModerationGrader, K5Mode, HorizonMode, Api::V1::RubricAssociation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/jqueryui/datepicker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.243 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.885 IQR)
- **Top Global Matches:** file_cluster_8: 14.243, file_cluster_11: 14.243, file_cluster_15: 14.29
- **Magnitude:** 4595.28 | **LOC:** 1853 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 434
- **Risk Profile:** Cognitive Load (75.8565%), Tech Debt (8.4608%)
**Top Internal Functions/Classes:**
  * `Datepicker` (Impact: 3141.0 | O(N^6) | DB: 434)
  * `datepicker` (Impact: 48.1 | O(2^N) | DB: 3)
  * `bindHover` (Impact: 19.0 | O(N^2) | DB: 5)
  * `_adjustInstDate` (Impact: 18.6 | O(N^2) | DB: 8)
  * `_formatDate` (Impact: 14.0 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 333`, `args: 86`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 1261`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 6`, `import: 1`
* *Defense:* `safety: 24`, `doc: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jquery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/content_tag.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.922 IQR)
- **Top Global Matches:** file_cluster_8: 10.922, file_cluster_0: 11.144, file_cluster_11: 11.378
- **Magnitude:** 4483.98 | **LOC:** 898 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 173
- **Risk Profile:** Cognitive Load (29.7685%), Tech Debt (11.3559%)
**Top Internal Functions/Classes:**
  * `ContentTag` (Impact: 4445.0 | O(2^N) | DB: 173)
    * *Intent:* # This file is part of Canvas. # # Canvas is free software: you can redistribute it and/or modify it...
  * `__global_context__` (Impact: 1.5 | O(N^1))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 145`, `args: 50`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 55`
* *Defense:* `safety: 37`, `doc: 8`, `test: 29`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CustomValidations, Lti::Migratable, MasterCourses::Restrictor, Workflow, SearchTermHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/discussion_topics_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.618 IQR)
- **Top Global Matches:** file_cluster_8: 11.618, file_cluster_17: 11.9, file_cluster_11: 11.997
- **Magnitude:** 4456.42 | **LOC:** 2000 | **CtrlFlow:** 85.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 102
- **Risk Profile:** Cognitive Load (42.7316%), Tech Debt (16.2458%)
**Top Internal Functions/Classes:**
  * `DiscussionTopicsController` (Impact: 2151.5 | O(N^6) | DB: 95)
    * *Intent:* # }, # "expand": { # "description": "Threaded replies should be expanded by default.", # "example": ...
  * `public_feed_[Truncated]` (Impact: 2148.0 | O(N^6) | DB: 102)
  * `__global_context__` (Impact: 1.5 | O(N^1))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 693`, `structural_boundaries: 121`, `args: 35`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 131`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 50`
* *Defense:* `safety: 24`, `doc: 12`, `test: 232`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Api::V1::AssignmentOverride, Api::V1::Rubric, posts, K5Mode, HorizonMode, DiscussionTopicsHelper, Api::V1::DiscussionTopics, Api::V1::Assignment...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/files_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.499 IQR)
- **Top Global Matches:** file_cluster_8: 12.499, file_cluster_17: 12.562, file_cluster_2: 12.633
- **Magnitude:** 4179.76 | **LOC:** 1856 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 207
- **Risk Profile:** Cognitive Load (49.9763%), Tech Debt (11.4592%)
**Top Internal Functions/Classes:**
  * `FilesController` (Impact: 3917.7 | O(N^6) | DB: 207)
    * *Intent:* # "lock_info": { # "$ref": "LockInfo" # }, # "lock_explanation": { # "example": "This assignment is ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 143`, `args: 28`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `state_mutation: 239`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 40`, `import: 1`
* *Defense:* `safety: 31`, `doc: 33`, `test: 155`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` K5Mode, Api::V1::Avatar, HorizonMode, Api::V1::Attachment, AttachmentHelper, authenticator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/gradebooks_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.763 IQR)
- **Top Global Matches:** file_cluster_8: 11.763, file_cluster_17: 12.128, file_cluster_2: 12.257
- **Magnitude:** 4148.52 | **LOC:** 2013 | **CtrlFlow:** 79.1% | **Authorship Centralization:** 18.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (53.1951%), Tech Debt (28.7564%)
**Top Internal Functions/Classes:**
  * `GradebooksController` (Impact: 1811.6 | O(N^6) | DB: 57)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
  * `speed_grader` (Impact: 1467.7 | O(2^N) | DB: 11)
  * `speed_grader_settings` (Impact: 174.1 | O(N^6) | DB: 11)
  * `gradebook_group_categories_json` (Impact: 109.2 | O(N^2))
  * `submissions_json` (Impact: 50.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 167`, `args: 60`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `state_mutation: 139`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 21`, `import: 6`
* *Defense:* `safety: 40`, `doc: 6`, `test: 347`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Api::V1::Submission, ActionView::Helpers::NumberHelper, Api::V1::Rubric, Api::V1::RubricAssessment, K5Mode, HorizonMode, )
    elsif feature_enabled
      InstStatsd::Statsd.distributed_increment(, Api::V1::Group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/enrollment.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.721 IQR)
- **Top Global Matches:** file_cluster_8: 10.721, file_cluster_0: 11.176, file_cluster_7: 11.372
- **Magnitude:** 4086.5 | **LOC:** 1720 | **CtrlFlow:** 72.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 156
- **Risk Profile:** Cognitive Load (53.814%), Tech Debt (39.0375%)
**Top Internal Functions/Classes:**
  * `self.workflow_readable_type_[Truncated]` (Impact: 1415.2 | O(N^6) | DB: 156)
  * `Enrollment` (Impact: 1310.4 | O(2^N) | DB: 69)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
  * `self.pending_temporary_enrollment_exclus` (Impact: 962.4 | O(N^6) | DB: 53)
    * *Intent:* # SQL condition that excludes temporary enrollments that are not currently # active by date. Course ...
  * `can_be_concluded_by` (Impact: 45.3 | O(N^4))
    * *Intent:* # Determine if a user has permissions to conclude this enrollment. # # user - The user requesting pe...
  * `long_name` (Impact: 28.9 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 241`, `args: 95`, `func_start: 181`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 41`, `dead_code: 2`, `orphaned_logic: 26`
* *Architecture:* `io: 110`
* *Defense:* `safety: 33`, `test: 25`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StickySisFields, Role::AssociationHelper, Workflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/accounts_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.68 IQR)
- **Top Global Matches:** file_cluster_8: 12.68, file_cluster_17: 12.828, file_cluster_2: 12.908
- **Magnitude:** 4010.92 | **LOC:** 2575 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 23.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 126
- **Risk Profile:** Cognitive Load (44.912%), Tech Debt (25.4509%)
**Top Internal Functions/Classes:**
  * `AccountsController` (Impact: 1537.1 | O(N^6) | DB: 126)
    * *Intent:* # "text": "Report a Problem", # "subtext": "If Canvas misbehaves, tell us about it", # "url": "#crea...
  * `__global_context__` (Impact: 976.9 | O(N^6))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
  * `statistics_graph_[Truncated]` (Impact: 755.0 | O(N^6) | DB: 52)
  * `remove_user` (Impact: 219.6 | O(N^6) | DB: 41)
    * *Intent:* # Delete a user record from a Canvas root account. If a user is associated # with multiple root acco...
  * `admin_tools` (Impact: 79.0 | O(N^6))
    * *Intent:* # Admin Tools page controls # => Log Auditing # => Add/Change Quota # = Restoring Content
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 592`, `structural_boundaries: 122`, `args: 54`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 363`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 53`, `import: 1`
* *Defense:* `safety: 48`, `doc: 48`, `test: 21`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Api::V1::Account, DefaultDueTimeHelper, CustomSidebarLinksHelper, Api::V1::QuizIpFilter, HorizonMode, only, default, Api::V1::Progress...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/submission_comment.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.136 IQR)
- **Top Global Matches:** file_cluster_8: 10.136, file_cluster_0: 10.541, file_cluster_7: 10.837
- **Magnitude:** 3806.52 | **LOC:** 629 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (32.7548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SubmissionComment` (Impact: 3782.4 | O(2^N) | DB: 107)
    * *Intent:* # # Canvas is free software: you can redistribute it and/or modify it under # the terms of the GNU A...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 101`, `args: 39`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 34`
* *Defense:* `safety: 12`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HtmlTextHelper, Workflow, SendToStream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/routes.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.845 IQR)
- **Top Global Matches:** file_cluster_8: 11.845, file_cluster_15: 12.005, file_cluster_7: 12.26
- **Magnitude:** 3772.44 | **LOC:** 3303 | **CtrlFlow:** 99.8% | **Authorship Centralization:** 19.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 318
- **Risk Profile:** Cognitive Load (17.4697%), Tech Debt (99.993%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 1081.3 | O(N^6))
    * *Intent:* # # Copyright (C) 2011 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
  * `Anonymous_Block` (Impact: 171.2 | O(N^2) | DB: 27)
  * `Anonymous_Block` (Impact: 82.5 | O(N^3) | DB: 180)
  * `Anonymous_Block` (Impact: 37.8 | O(N^2) | DB: 4)
  * `Anonymous_Block` (Impact: 31.9 | O(N^1) | DB: 9)
    * *Intent:* # Test-only routes for Selenium tests with mock LTI tool if Rails.env.test? post "/test/mock_lti/ui"...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 1`, `args: 5`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 219`, `planned_debt: 9`, `fragile_debt: 1`, `duplicate_logic: 84`
* *Architecture:* `io: 287`, `api: 1911`, `import: 1`
* *Defense:* `test: 14`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/calendar_events_api_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.957 IQR)
- **Top Global Matches:** file_cluster_17: 11.957, file_cluster_8: 11.995, file_cluster_2: 12.238
- **Magnitude:** 3658.54 | **LOC:** 2225 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 269
- **Risk Profile:** Cognitive Load (40.2442%), Tech Debt (9.0966%)
**Top Internal Functions/Classes:**
  * `CalendarEventsApiController` (Impact: 3453.3 | O(N^6) | DB: 269)
    * *Intent:* # "example": "FREQ=DAILY;INTERVAL=1;COUNT=5" # }, # "series_head": { # "description": "Trueif this i...
  * `calendar_events_for_user` (Impact: 2.0 | O(N^1))
  * `__global_context__` (Impact: 2.0 | O(N^1))
    * *Intent:* # # Copyright (C) 2012 - present Instructure, Inc. # # This file is part of Canvas. # # Canvas is fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 122`, `args: 96`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 176`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 69`, `import: 2`
* *Defense:* `safety: 23`, `doc: 21`, `test: 97`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` manageable, rrule, Api::V1::CalendarEvent, all, CalendarConferencesHelper
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ui/features/speed_grader/sg_uploader.js` (JAVASCRIPT) | Magnitude: 138.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 47, structural_boundaries: 22, branch: 15
- `ui/shared/common/activateTooltips.js` (JAVASCRIPT) | Magnitude: 31.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, branch: 8, structural_boundaries: 8, immutability_locks: 6
- `ui/features/question_bank/jquery/moveMultipleQuestionBanks.js` (JAVASCRIPT) | Magnitude: 91.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 66, indent_spaces: 66, structural_boundaries: 17, func_start: 9
- `app/models/session_persistence_token.rb` (RUBY) | Magnitude: 31.8 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 15, branch: 14, func_start: 8
- `app/views/rubrics/index.html.erb` (HTML) | Magnitude: 27.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, ssr_boundaries: 56, decorators: 28, io: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ui/shared/forms/backbone/views/DialogFormView.js` (JAVASCRIPT) | Magnitude: 201.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 108, indent_spaces: 104, structural_boundaries: 41, branch: 24
- `ui/shared/tour-pubsub/pubsub.ts` (TYPESCRIPT) | Magnitude: 3.25 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 15, structural_boundaries: 10, branch: 5
- `ui/features/assignment_index/backbone/collections/UniqueDropdownCollection.js` (JAVASCRIPT) | Magnitude: 144.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 90, indent_spaces: 84, structural_boundaries: 16, branch: 12
- `ui/shared/assignments/backbone/collections/AssignmentOverrideCollection.js` (JAVASCRIPT) | Magnitude: 79.54 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 42, indent_spaces: 35, structural_boundaries: 24, reflection_metaprogramming: 23
- `ui/features/roster/backbone/collections/RolesCollection.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 17, state_mutation: 12, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ui/shared/lock-icon/backbone/views/index.js` (JAVASCRIPT) | Magnitude: 10.72 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: reflection_metaprogramming: 10, sec_state_mutation: 7, structural_boundaries: 5, sync_locks: 5
- `packages/canvas-rce/scripts/npm_localpublish.sh` (SHELL) | Magnitude: 3.35 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 16, indent_spaces: 14, reflection_metaprogramming: 13, branch: 10
- `ui/shared/util/legacyCoffeesScriptHelpers.js` (JAVASCRIPT) | Magnitude: 13.46 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, reflection_metaprogramming: 6, structural_boundaries: 5, args: 4
- `packages/canvas-rce/scripts/npm_localpush.sh` (SHELL) | Magnitude: 7.24 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: reflection_metaprogramming: 45, indent_spaces: 41, state_mutation: 28, branch: 12
- `packages/canvas-rce/scripts/npm_localrev.sh` (SHELL) | Magnitude: 5.58 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 25, reflection_metaprogramming: 21, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ui/features/assignment_index/cache.js` (JAVASCRIPT) | Magnitude: 29.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 12, structural_boundaries: 8, args: 6
- `ui/features/enhanced_individual_gradebook/react/components/LearningMasteryTabsView.tsx` (TYPESCRIPT) | Magnitude: 20.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 247, structural_boundaries: 58, immutability_locks: 45, ui_framework: 42
- `ui/features/lti_registrations/manage/api/PaginatedList.ts` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 3, doc: 3
- `ui/shared/conditional-release-editor/react/components/assignment-card.jsx` (JAVASCRIPT) | Magnitude: 123.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 65, ui_framework: 32, structural_boundaries: 18
- `ui/shared/assignments/react/AssignmentHeader.tsx` (TYPESCRIPT) | Magnitude: 1.13 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 141, ui_framework: 35, structural_boundaries: 32, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/k5uploader/src/messenger.js` (JAVASCRIPT) | Magnitude: 78.98 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 41, args: 13, closures: 12
- `packages/slickgrid/slick.core.js` (JAVASCRIPT) | Magnitude: 298.52 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 160, doc: 80, branch: 30
- `packages/canvas-rce/src/rce/alertHandler.js` (JAVASCRIPT) | Magnitude: 16.64 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, state_mutation: 7, structural_boundaries: 4, api: 4
- `packages/date-js/core.js` (JAVASCRIPT) | Magnitude: 1229.04 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 369, state_mutation: 196, branch: 129, doc: 110
- `config/initializers/permissions_groups.rb` (RUBY) | Magnitude: 510.74 | Delta: **0.345 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 740, closures: 581, state_mutation: 188, branch: 178

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `ui/features/course_paces/react/shared/types.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 36, indent_spaces: 32, immutability_locks: 20, branch: 18
- `ui/shared/network/RequestDispatch/index.ts` (TYPESCRIPT) | Magnitude: 11.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 103, state_mutation: 39, structural_boundaries: 35, args: 25
- `ui/shared/backbone/createStore.ts` (TYPESCRIPT) | Magnitude: 2.1 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, func_start: 13, args: 12, state_mutation: 11
- `packages/canvas-rce/src/util/TypedDict.ts` (TYPESCRIPT) | Magnitude: 0.37 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, generics: 11, ui_framework: 8, structural_boundaries: 4
- `ui/shared/canvas-file-upload/react/components/CanvasFilesBrowser/utils/folderHelpers.ts` (TYPESCRIPT) | Magnitude: 5.25 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 15, state_mutation: 12, immutability_locks: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `ui/features/lti_collaborations/react/NewCollaborationsDropDown.jsx` (JAVASCRIPT) | Magnitude: 48.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 9, state_mutation: 9, branch: 8
- `app/models/discussion_entry_participant.rb` (RUBY) | Magnitude: 303.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 31, branch: 27, structural_boundaries: 16
- `app/controllers/question_banks_controller.rb` (RUBY) | Magnitude: 182.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 57, branch: 31, io: 21
- `ui/features/permissions/react/components/AddTray.jsx` (JAVASCRIPT) | Magnitude: 189.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 204, state_mutation: 111, structural_boundaries: 45, ui_framework: 44
- `ui/features/gradebook/react/default_gradebook/GradebookGrid/headers/__tests__/ColumnHeaderSpecHelpers.js` (JAVASCRIPT) | Magnitude: 23.1 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, args: 11, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `ui/features/context_modules_v2/react/componentsStudents/ModuleItemSupplementalInfoStudent.tsx` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 110, branch: 26, ui_framework: 25, generics: 23
- `ui/features/discussion_topics_post/react/components/TranslationTriggerModal/TranslationTriggerModal.tsx` (TYPESCRIPT) | Magnitude: 0.39 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, ui_framework: 14, generics: 14, structural_boundaries: 13
- `ui/features/discussion_topics_post/react/containers/SplitScreenViewContainer/SplitScreenViewContainer.tsx` (TYPESCRIPT) | Magnitude: 104.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 439, branch: 95, structural_boundaries: 77, ui_framework: 76
- `ui/features/syllabus_revisions/react/SyllabusRevisionsTray.tsx` (TYPESCRIPT) | Magnitude: 15.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 287, branch: 59, ui_framework: 50, args: 49
- `app/controllers/wiki_pages_api_controller.rb` (RUBY) | Magnitude: 904.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 472, branch: 261, state_mutation: 93, structural_boundaries: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/jqueryui/button.js` (JAVASCRIPT) | Magnitude: 174.66 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 122, indent_tabs: 105, branch: 22, structural_boundaries: 12
- `ui/features/quiz_log_auditing/stores/events.ts` (TYPESCRIPT) | Magnitude: 16.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 70, structural_boundaries: 33, concurrency: 30
- `ui/features/quiz_statistics/services/poll_progress.js` (JAVASCRIPT) | Magnitude: 39.06 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 11, concurrency: 9, branch: 8
- `ui/shared/avatar-dialog-view/backbone/views/GravatarView.js` (JAVASCRIPT) | Magnitude: 59.32 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 20, state_mutation: 19, args: 13
- `script/techdebt_stats.js` (JAVASCRIPT) | Magnitude: 202.98 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 274, branch: 71, immutability_locks: 55, concurrency: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `app/models/accessibility/rule.rb` (RUBY) | Magnitude: 11.76 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 14, doc: 14, func_start: 10
- `ui/shared/external-tools/messages.ts` (TYPESCRIPT) | Magnitude: 1.61 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, api: 9, args: 2
- `config/initializers/stubs.rb` (RUBY) | Magnitude: 2.52 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 1, planned_debt: 1, orphaned_logic: 1, sec_dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/canvas-rce/src/common/getCookie.js` (JAVASCRIPT) | Magnitude: 8.78 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3, doc: 3, bitwise_ops: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `app/controllers/users_controller.rb` (RUBY) | Magnitude: 5658.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 2067, branch: 826, state_mutation: 426, structural_boundaries: 206
- `packages/jqueryui/datepicker.js` (JAVASCRIPT) | Magnitude: 4595.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1261, indent_spaces: 1259, branch: 555, structural_boundaries: 333
- `ui/features/grade_summary/backbone/views/GroupView.js` (JAVASCRIPT) | Magnitude: 50.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 20, branch: 13, import: 6
- `ui/features/rubrics/components/ViewRubrics/DuplicateRubricModal.tsx` (TYPESCRIPT) | Magnitude: 2.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 28, import: 14, branch: 12
- `app/controllers/microsoft_sync/groups_controller.rb` (RUBY) | Magnitude: 200.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 99, branch: 33, structural_boundaries: 25, func_start: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `script/canvas_init` (SHELL) | Magnitude: 11.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 4, structural_boundaries: 4, reflection_metaprogramming: 3, indent_spaces: 3
- `ui/shared/temporary-enrollment/react/util/analytics.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 11, doc: 7, api: 6
- `app/middleware/enhanced_cookie_store.rb` (RUBY) | Magnitude: 15.2 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, branch: 7, structural_boundaries: 4, args: 1
- `config/initializers/dropped_columns.rb` (RUBY) | Magnitude: 10.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_dead_code: 2, dead_code: 1
- `app/helpers/group_permission_helper.rb` (RUBY) | Magnitude: 12.18 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 4, test: 4, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `app/controllers/application_controller.rb` -> Churn: **95.49%** | Cog Load: 83.688% | Debt: 14.3929%
- `app/controllers/courses_controller.rb` -> Churn: **89.13%** | Cog Load: 69.2795% | Debt: 59.5977%
- `app/models/account.rb` -> Churn: **88.82%** | Cog Load: 64.3859% | Debt: 29.2817%
- `config/routes.rb` -> Churn: **87.66%** | Cog Load: 17.4697% | Debt: 99.993%
- `app/models/course.rb` -> Churn: **83.5%** | Cog Load: 52.703% | Debt: 7.8477%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `config/initializers/active_record.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 7675.1
- `app/models/calendar_event.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 3557.96
- `app/models/content_migration.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 3556.6
- `app/helpers/application_helper.rb` -> **Cody Cutrer** (100.0% isolated ownership) | Magnitude: 3224.32
- `app/controllers/quizzes/quizzes_controller.rb` -> **Cody Cutrer** (83.3% isolated ownership) | Magnitude: 3209.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/canvas-rce/src/rce/RCEWrapper.tsx` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/canvas-rce/src/rce/plugins/instructure_rce_external_tools/RceToolWrapper.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9929%)
- `packages/canvas-rce/src/rce/plugins/instructure_rce_external_tools/components/ExternalToolDialog/ExternalToolDialog.tsx` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ui/shared/datetime/date-functions.js` -> **Severity: 479.183** (Blast Radius: 4.889 * Doc Risk: 98.0124%)
- `ui/shared/util/globalUtils.ts` -> **Severity: 237.934** (Blast Radius: 2.383 * Doc Risk: 99.8466%)
- `ui/shared/alerts/react/AlertManager.tsx` -> **Severity: 165.823** (Blast Radius: 2.365 * Doc Risk: 70.1154%)
- `ui/features/lti_registrations/manage/model/LtiMessageType.ts` -> **Severity: 158.387** (Blast Radius: 1.697 * Doc Risk: 93.3333%)
- `ui/shared/planner/dynamic-ui/middleware.js` -> **Severity: 149.473** (Blast Radius: 1.8 * Doc Risk: 83.0405%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
