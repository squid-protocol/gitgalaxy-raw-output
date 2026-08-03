# ARCHITECTURAL_BRIEF: discourse
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/discourse` |
| **Timestamp** | `2026-08-03T20:10:34.866884+00:00` |
| **Scan Duration** | `24.74s` |
| **Git Branch** | `main` |
| **Git Commit** | `544e36f477511818b9df96ec37e44af5e4bab7d9` |
| **Git Remote** | `https://github.com/discourse/discourse` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6904 malicious artifacts.

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
| Total Artifacts | 21317 |
| Analyzed Artifacts (Scanned) | 11501 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9816 |
| Total LOC | 608768 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.0% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2041 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 197 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 4384 | 188503 | 38.1% |
| YAML | 4072 | 206585 | 35.4% |
| JAVASCRIPT | 2486 | 200753 | 21.6% |
| HTML | 313 | 6988 | 2.7% |
| PLAINTEXT | 65 | 5 | 0.6% |
| MARKDOWN | 56 | 0 | 0.5% |
| JSON | 53 | 1431 | 0.5% |
| CSS | 31 | 4101 | 0.3% |
| SHELL | 26 | 321 | 0.2% |
| XML | 7 | 1 | 0.1% |
| SQLITE | 4 | 36 | 0.0% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| TYPESCRIPT | 1 | 41 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.163`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 9451 | 82.2% |
| file_cluster_13 | 979 | 8.5% |
| file_cluster_0 | 646 | 5.6% |
| file_cluster_4 | 252 | 2.2% |
| file_cluster_17 | 33 | 0.3% |
| Unknown | 8 | 0.1% |
| file_cluster_9 | 7 | 0.1% |
| file_cluster_2 | 6 | 0.1% |
| file_cluster_12 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 116 | 1.0% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9816*

**Composition by Extension & Reason:**
- `.rb`: 4899x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2574 LOC), 1x Excluded (Machine-Generated Source Code Signature: 204 LOC)
- `.js`: 1542x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.gjs`: 1224x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 314 LOC)
- `.scss`: 614x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 244x Excluded (Explicitly Denied Extension: '.png'), 68x Excluded (Explicitly Denied Extension: '.PNG')
- `.yml`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 35 exceeds 500 chars), 3x Excluded (Saturation: Line 32 exceeds 500 chars)
- `.md`: 135x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eml`: 131x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 98x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.response`: 90x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rake`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.production-sample')
- `.jpg`: 38x Excluded (Explicitly Denied Extension: '.jpg')
- `.mustache`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 35.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.3 | 2.3 | 2.3 |
| API Exposure | 0.0 | 19.4 | 0.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 98.5 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 73.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.9 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 87.2 | 4.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 44.0 | 40.0 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/models/user.rb` (Hits: 176)
- `frontend/discourse/admin/routes/admin-route-map.js` (Hits: 120)
- `app/models/topic.rb` (Hits: 119)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **object.gjs** (`frontend/discourse/app/form-kit/components/fk/object.gjs`) — 842 inbound connections
2. **helper.rb** (`plugins/discourse-chat-integration/app/helpers/helper.rb`) — 396 inbound connections
3. **d-button.gjs** (`frontend/discourse/app/components/d-button.gjs`) — 362 inbound connections
4. **d-icon.js** (`frontend/discourse/app/helpers/d-icon.js`) — 279 inbound connections
5. **plugin-outlet.gjs** (`frontend/discourse/app/components/plugin-outlet.gjs`) — 200 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **qunit-helpers.js** (`frontend/discourse/tests/helpers/qunit-helpers.js`) — 84 outbound dependencies
2. **topic.gjs** (`frontend/discourse/app/templates/topic.gjs`) — 49 outbound dependencies
3. **report.rb** (`app/models/report.rb`) — 48 outbound dependencies
4. **topic.js** (`frontend/discourse/app/controllers/topic.js`) — 46 outbound dependencies
5. **d-editor.gjs** (`frontend/discourse/app/components/d-editor.gjs`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `TopicsController` (@ `app/controllers/topics_controller.rb`) -> Impact: **5571.7** | LOC: 1587
  * *Intent:* # frozen_string_literal: true
- `BulkImport::Generic_[Truncated]` (@ `script/bulk_import/generic_bulk.rb`) -> Impact: **4104.0** | LOC: 3514
- `UsersController` (@ `app/controllers/users_controller.rb`) -> Impact: **3361.6** | LOC: 1952
  * *Intent:* # frozen_string_literal: true
- `User_[Truncated]` (@ `app/models/user.rb`) -> Impact: **2632.3** | LOC: 2356
  * *Intent:* # frozen_string_literal: true
- `RemapToFa6IconNames` (@ `db/migrate/20241204085540_remap_to_fa6_icon_names.rb`) -> Impact: **2440.2** | LOC: 792
  * *Intent:* # frozen_string_literal: true
- `Topic` (@ `app/models/topic.rb`) -> Impact: **2229.4** | LOC: 733
  * *Intent:* # frozen_string_literal: true
- `BulkImport::Base_[Truncated]` (@ `script/bulk_import/base.rb`) -> Impact: **2005.8** | LOC: 2357
- `PostMover` (@ `app/models/post_mover.rb`) -> Impact: **1944.5** | LOC: 825
  * *Intent:* # frozen_string_literal: true
- `members` (@ `app/controllers/groups_controller.rb`) -> Impact: **1876.9** | LOC: 818
- `PostAlerter_[Truncated]` (@ `app/services/post_alerter.rb`) -> Impact: **1831.7** | LOC: 1109
  * *Intent:* # frozen_string_literal: true

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `TopicsController` (@ `app/controllers/topics_controller.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `Jobs` (@ `app/jobs/regular/create_linked_topic.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `Jobs` (@ `app/jobs/regular/merge_user.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `Jobs` (@ `app/jobs/regular/update_username.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `Notification` (@ `app/models/notification.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `PostMover` (@ `app/models/post_mover.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `PostTiming` (@ `app/models/post_timing.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `Tag` (@ `app/models/tag.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `TagUser` (@ `app/models/tag_user.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true
- `TopTopic` (@ `app/models/top_topic.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # frozen_string_literal: true

### Highest Data Gravity (Database Complexity)
- `User_[Truncated]` (@ `app/models/user.rb`) -> DB Complexity: **580**
  * *Intent:* # frozen_string_literal: true
- `UsersController` (@ `app/controllers/users_controller.rb`) -> DB Complexity: **258**
  * *Intent:* # frozen_string_literal: true
- `BulkImport::Generic_[Truncated]` (@ `script/bulk_import/generic_bulk.rb`) -> DB Complexity: **248**
- `log_badge_creation_[Truncated]` (@ `app/services/staff_action_logger.rb`) -> DB Complexity: **191**
- `BulkImport::Base_[Truncated]` (@ `script/bulk_import/base.rb`) -> DB Complexity: **181**
- `Anonymous_Block` (@ `plugins/discourse-assign/plugin.rb`) -> DB Complexity: **165**
- `UserMerger` (@ `app/services/user_merger.rb`) -> DB Complexity: **159**
  * *Intent:* # frozen_string_literal: true
- `TopicsController` (@ `app/controllers/topics_controller.rb`) -> DB Complexity: **151**
  * *Intent:* # frozen_string_literal: true
- `members` (@ `app/controllers/groups_controller.rb`) -> DB Complexity: **148**
- `DiscourseAi` (@ `plugins/discourse-ai/lib/utils/research/filter.rb`) -> DB Complexity: **147**
  * *Intent:* # frozen_string_literal: true

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `app/models` | 278 | 47538.9 | 18.16% | 62.18% |
| `frontend/discourse/app/components` | 345 | 32486.68 | 56.28% | 15.57% |
| `app/controllers` | 85 | 29002.38 | 25.77% | 61.37% |
| `frontend/discourse/admin/components` | 126 | 12755.92 | 54.87% | 5.72% |
| `script/bulk_import` | 9 | 12018.56 | 39.17% | 15.76% |
| `frontend/discourse/app/models` | 56 | 11695.52 | 51.82% | 68.31% |
| `app/services` | 60 | 10960.02 | 28.11% | 42.8% |
| `frontend/discourse/app/components/modal` | 66 | 10254.42 | 73.25% | 7.56% |
| `app/jobs/regular` | 90 | 7678.16 | 20.09% | 19.46% |
| `app/serializers` | 218 | 7342.96 | 11.51% | 86.02% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.devcontainer/scripts/chrome_wrapper` -> **100.0%** Exposure
- `bin/dev` -> **100.0%** Exposure
- `bin/docker/bundle` -> **100.0%** Exposure
- `bin/docker/cleanup` -> **100.0%** Exposure
- `bin/docker/ember-cli` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.devcontainer/scripts/chrome_wrapper` -> **100.0%** Exposure
- `bin/docker/reset_db` -> **100.0%** Exposure
- `bin/notify_file_change` -> **100.0%** Exposure
- `config/unicorn_launcher` -> **100.0%** Exposure
- `script/silence_successful_output` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `db/fixtures/007_web_hook_event_types.rb` -> **0** Orphaned Functions | **50** Duplicates
- `db/fixtures/006_badges.rb` -> **1** Orphaned Functions | **33** Duplicates
- `frontend/discourse/admin/controllers/admin-customize-themes/show/index.js` -> **32** Orphaned Functions | **0** Duplicates
- `app/models/group.rb` -> **29** Orphaned Functions | **2** Duplicates
- `frontend/discourse/app/static/wizard/models/wizard.js` -> **9** Orphaned Functions | **22** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`app/controllers/application_controller.rb`** -> AI Confidence: **99.39%**
2. **`app/models/topic.rb`** -> AI Confidence: **99.39%**
3. **`plugins/discourse-calendar/plugin.rb`** -> AI Confidence: **99.39%**
4. **`plugins/poll/plugin.rb`** -> AI Confidence: **99.39%**
5. **`script/bench.rb`** -> AI Confidence: **99.39%**
6. **`frontend/discourse/app/blocks/conditions/route.js`** -> AI Confidence: **99.39%**
7. **`app/helpers/application_helper.rb`** -> AI Confidence: **99.34%**
8. **`bin/qunit`** -> AI Confidence: **99.34%**
9. **`app/controllers/categories_controller.rb`** -> AI Confidence: **99.32%**
10. **`config/environments/development.rb`** -> AI Confidence: **99.32%**
11. **`config/initializers/006-mini_profiler.rb`** -> AI Confidence: **99.32%**
12. **`config/initializers/101-lograge.rb`** -> AI Confidence: **99.32%**
13. **`config/pitchfork.conf.rb`** -> AI Confidence: **99.32%**
14. **`config/unicorn.conf.rb`** -> AI Confidence: **99.32%**
15. **`plugins/chat/app/queries/chat/tracking_state_report_query.rb`** -> AI Confidence: **99.32%**
16. **`plugins/discourse-ai/spec/lib/agents/tools/github_diff_spec.rb`** -> AI Confidence: **99.32%**
17. **`plugins/discourse-openid-connect/plugin.rb`** -> AI Confidence: **99.32%**
18. **`script/bulk_import/generic_bulk.rb`** -> AI Confidence: **99.32%**
19. **`app/models/category.rb`** -> AI Confidence: **99.31%**
20. **`app/models/post.rb`** -> AI Confidence: **99.31%**
21. **`app/models/report.rb`** -> AI Confidence: **99.31%**
22. **`config/application.rb`** -> AI Confidence: **99.31%**
23. **`migrations/migrations.rb`** -> AI Confidence: **99.31%**
24. **`plugins/discourse-adplugin/plugin.rb`** -> AI Confidence: **99.31%**
25. **`plugins/discourse-ai/evals/run`** -> AI Confidence: **99.31%**
26. **`plugins/discourse-cakeday/plugin.rb`** -> AI Confidence: **99.31%**
27. **`plugins/discourse-patreon/plugin.rb`** -> AI Confidence: **99.31%**
28. **`plugins/discourse-policy/plugin.rb`** -> AI Confidence: **99.31%**
29. **`plugins/discourse-post-voting/plugin.rb`** -> AI Confidence: **99.31%**
30. **`script/cache_critical_dns`** -> AI Confidence: **99.31%**
31. **`frontend/custom-proxy/index.js`** -> AI Confidence: **99.31%**
32. **`frontend/discourse/admin/components/admin-config-areas/api-keys-show.gjs`** -> AI Confidence: **99.31%**
33. **`frontend/discourse/admin/components/admin-filter-controls.gjs`** -> AI Confidence: **99.31%**
34. **`frontend/discourse/admin/components/admin-permalink-form.gjs`** -> AI Confidence: **99.31%**
35. **`frontend/discourse/admin/components/admin-report-legacy.gjs`** -> AI Confidence: **99.31%**
36. **`frontend/discourse/admin/components/admin-report-new.gjs`** -> AI Confidence: **99.31%**
37. **`frontend/discourse/admin/components/admin-report-table.gjs`** -> AI Confidence: **99.31%**
38. **`frontend/discourse/admin/components/admin-report.gjs`** -> AI Confidence: **99.31%**
39. **`frontend/discourse/admin/components/admin-welcome-banner-form.gjs`** -> AI Confidence: **99.31%**
40. **`frontend/discourse/admin/components/color-input.gjs`** -> AI Confidence: **99.31%**
41. **`frontend/discourse/admin/components/color-palette-list-item.gjs`** -> AI Confidence: **99.31%**
42. **`frontend/discourse/admin/components/email-logs-list.gjs`** -> AI Confidence: **99.31%**
43. **`frontend/discourse/admin/components/file-size-input.gjs`** -> AI Confidence: **99.31%**
44. **`frontend/discourse/admin/components/ip-lookup.gjs`** -> AI Confidence: **99.31%**
45. **`frontend/discourse/admin/components/modal/install-theme.gjs`** -> AI Confidence: **99.31%**
46. **`frontend/discourse/admin/components/modal/penalize-user.gjs`** -> AI Confidence: **99.31%**
47. **`frontend/discourse/admin/components/schema-setting/number-field.gjs`** -> AI Confidence: **99.31%**
48. **`frontend/discourse/admin/components/simple-list.gjs`** -> AI Confidence: **99.31%**
49. **`frontend/discourse/admin/components/site-settings/upload.gjs`** -> AI Confidence: **99.31%**
50. **`frontend/discourse/admin/components/themes-grid-card.gjs`** -> AI Confidence: **99.31%**
51. **`frontend/discourse/admin/components/themes-list-item.gjs`** -> AI Confidence: **99.31%**
52. **`frontend/discourse/admin/components/upsert-category/appearance.gjs`** -> AI Confidence: **99.31%**
53. **`frontend/discourse/admin/components/upsert-category/general.gjs`** -> AI Confidence: **99.31%**
54. **`frontend/discourse/admin/components/watched-word-form.gjs`** -> AI Confidence: **99.31%**
55. **`frontend/discourse/admin/controllers/admin-customize-themes/show.js`** -> AI Confidence: **99.31%**
56. **`frontend/discourse/admin/controllers/admin-customize-themes/show/index.js`** -> AI Confidence: **99.31%**
57. **`frontend/discourse/admin/controllers/admin-email-templates/edit.js`** -> AI Confidence: **99.31%**
58. **`frontend/discourse/admin/controllers/admin-logs/staff-action-logs.js`** -> AI Confidence: **99.31%**
59. **`frontend/discourse/admin/controllers/admin-site-text/index.js`** -> AI Confidence: **99.31%**
60. **`frontend/discourse/admin/controllers/edit-category/tabs.js`** -> AI Confidence: **99.31%**
61. **`frontend/discourse/admin/models/report.js`** -> AI Confidence: **99.31%**
62. **`frontend/discourse/admin/services/admin-search-data-source.js`** -> AI Confidence: **99.31%**
63. **`frontend/discourse/admin/templates/admin-customize-themes/show.gjs`** -> AI Confidence: **99.31%**
64. **`frontend/discourse/admin/templates/admin-logs/staff-action-logs.gjs`** -> AI Confidence: **99.31%**
65. **`frontend/discourse/admin/templates/edit-category/tabs-horizontal.gjs`** -> AI Confidence: **99.31%**
66. **`frontend/discourse/app/app.js`** -> AI Confidence: **99.31%**
67. **`frontend/discourse/app/blocks/block-outlet.gjs`** -> AI Confidence: **99.31%**
68. **`frontend/discourse/app/components/admin-post-menu.gjs`** -> AI Confidence: **99.31%**
69. **`frontend/discourse/app/components/async-content.gjs`** -> AI Confidence: **99.31%**
70. **`frontend/discourse/app/components/bulk-select-topics-dropdown.gjs`** -> AI Confidence: **99.31%**
71. **`frontend/discourse/app/components/categories-only.gjs`** -> AI Confidence: **99.31%**
72. **`frontend/discourse/app/components/category-topic-template-editor.gjs`** -> AI Confidence: **99.31%**
73. **`frontend/discourse/app/components/composer-body.js`** -> AI Confidence: **99.31%**
74. **`frontend/discourse/app/components/composer-container.gjs`** -> AI Confidence: **99.31%**
75. **`frontend/discourse/app/components/composer-messages.gjs`** -> AI Confidence: **99.31%**
76. **`frontend/discourse/app/components/composer-title.gjs`** -> AI Confidence: **99.31%**
77. **`frontend/discourse/app/components/d-button.gjs`** -> AI Confidence: **99.31%**
78. **`frontend/discourse/app/components/d-editor-original-translation-preview.gjs`** -> AI Confidence: **99.31%**
79. **`frontend/discourse/app/components/d-navigation.gjs`** -> AI Confidence: **99.31%**
80. **`frontend/discourse/app/components/date-input.gjs`** -> AI Confidence: **99.31%**
81. **`frontend/discourse/app/components/discovery/filter-navigation-menu.gjs`** -> AI Confidence: **99.31%**
82. **`frontend/discourse/app/components/discovery/topics.gjs`** -> AI Confidence: **99.31%**
83. **`frontend/discourse/app/components/emoji-picker/content.gjs`** -> AI Confidence: **99.31%**
84. **`frontend/discourse/app/components/form-template-field/upload.gjs`** -> AI Confidence: **99.31%**
85. **`frontend/discourse/app/components/glimmer-site-header.gjs`** -> AI Confidence: **99.31%**
86. **`frontend/discourse/app/components/global-notice.gjs`** -> AI Confidence: **99.31%**
87. **`frontend/discourse/app/components/group-membership-button.gjs`** -> AI Confidence: **99.31%**
88. **`frontend/discourse/app/components/header.gjs`** -> AI Confidence: **99.31%**
89. **`frontend/discourse/app/components/header/icons.gjs`** -> AI Confidence: **99.31%**
90. **`frontend/discourse/app/components/invite-panel.gjs`** -> AI Confidence: **99.31%**
91. **`frontend/discourse/app/components/mobile-nav.gjs`** -> AI Confidence: **99.31%**
92. **`frontend/discourse/app/components/modal/avatar-selector.gjs`** -> AI Confidence: **99.31%**
93. **`frontend/discourse/app/components/modal/bulk-topic-actions.gjs`** -> AI Confidence: **99.31%**
94. **`frontend/discourse/app/components/modal/create-invite.gjs`** -> AI Confidence: **99.31%**
95. **`frontend/discourse/app/components/modal/forgot-password.gjs`** -> AI Confidence: **99.31%**
96. **`frontend/discourse/app/components/modal/history.gjs`** -> AI Confidence: **99.31%**
97. **`frontend/discourse/app/components/modal/history/revision.gjs`** -> AI Confidence: **99.31%**
98. **`frontend/discourse/app/components/modal/move-to-topic.gjs`** -> AI Confidence: **99.31%**
99. **`frontend/discourse/app/components/modal/reorder-categories.gjs`** -> AI Confidence: **99.31%**
100. **`frontend/discourse/app/components/modal/share-topic.gjs`** -> AI Confidence: **99.31%**
101. **`frontend/discourse/app/components/modal/upsert-hyperlink.gjs`** -> AI Confidence: **99.31%**
102. **`frontend/discourse/app/components/more-topics/browse-more.gjs`** -> AI Confidence: **99.31%**
103. **`frontend/discourse/app/components/nav-item.gjs`** -> AI Confidence: **99.31%**
104. **`frontend/discourse/app/components/post-text-selection.gjs`** -> AI Confidence: **99.31%**
105. **`frontend/discourse/app/components/post.gjs`** -> AI Confidence: **99.31%**
106. **`frontend/discourse/app/components/post/meta-data/poster-name.gjs`** -> AI Confidence: **99.31%**
107. **`frontend/discourse/app/components/post/quoted-content.gjs`** -> AI Confidence: **99.31%**
108. **`frontend/discourse/app/components/relative-time-picker.gjs`** -> AI Confidence: **99.31%**
109. **`frontend/discourse/app/components/reviewable/ip-lookup.gjs`** -> AI Confidence: **99.31%**
110. **`frontend/discourse/app/components/reviewable/item.gjs`** -> AI Confidence: **99.31%**
111. **`frontend/discourse/app/components/search-advanced-options.gjs`** -> AI Confidence: **99.31%**
112. **`frontend/discourse/app/components/search-menu.gjs`** -> AI Confidence: **99.31%**
113. **`frontend/discourse/app/components/search-menu/results/assistant-item.gjs`** -> AI Confidence: **99.31%**
114. **`frontend/discourse/app/components/search-menu/results/assistant.gjs`** -> AI Confidence: **99.31%**
115. **`frontend/discourse/app/components/search-menu/results/initial-options.gjs`** -> AI Confidence: **99.31%**
116. **`frontend/discourse/app/components/search-menu/search-term.gjs`** -> AI Confidence: **99.31%**
117. **`frontend/discourse/app/components/second-factor-form.gjs`** -> AI Confidence: **99.31%**
118. **`frontend/discourse/app/components/sidebar/section-link-prefix.gjs`** -> AI Confidence: **99.31%**
119. **`frontend/discourse/app/components/sidebar/section-link.gjs`** -> AI Confidence: **99.31%**
120. **`frontend/discourse/app/components/tag-info-button.gjs`** -> AI Confidence: **99.31%**
121. **`frontend/discourse/app/components/tag-info.gjs`** -> AI Confidence: **99.31%**
122. **`frontend/discourse/app/components/time-input.gjs`** -> AI Confidence: **99.31%**
123. **`frontend/discourse/app/components/topic-admin-menu.gjs`** -> AI Confidence: **99.31%**
124. **`frontend/discourse/app/components/topic-list/header/sortable-column.gjs`** -> AI Confidence: **99.31%**
125. **`frontend/discourse/app/components/topic-list/item.gjs`** -> AI Confidence: **99.31%**
126. **`frontend/discourse/app/components/topic-navigation.gjs`** -> AI Confidence: **99.31%**
127. **`frontend/discourse/app/components/topic-progress.gjs`** -> AI Confidence: **99.31%**
128. **`frontend/discourse/app/components/topic-skip-links.gjs`** -> AI Confidence: **99.31%**
129. **`frontend/discourse/app/components/topic-status.gjs`** -> AI Confidence: **99.31%**
130. **`frontend/discourse/app/components/topic-timer-info.gjs`** -> AI Confidence: **99.31%**
131. **`frontend/discourse/app/components/user-card-contents.gjs`** -> AI Confidence: **99.31%**
132. **`frontend/discourse/app/controllers/discovery/list.js`** -> AI Confidence: **99.31%**
133. **`frontend/discourse/app/controllers/exception.js`** -> AI Confidence: **99.31%**
134. **`frontend/discourse/app/controllers/full-page-search.js`** -> AI Confidence: **99.31%**
135. **`frontend/discourse/app/controllers/group/index.js`** -> AI Confidence: **99.31%**
136. **`frontend/discourse/app/controllers/invites/show.js`** -> AI Confidence: **99.31%**
137. **`frontend/discourse/app/controllers/login.js`** -> AI Confidence: **99.31%**
138. **`frontend/discourse/app/controllers/password-reset.js`** -> AI Confidence: **99.31%**
139. **`frontend/discourse/app/controllers/preferences/interface.js`** -> AI Confidence: **99.31%**
140. **`frontend/discourse/app/controllers/preferences/security.js`** -> AI Confidence: **99.31%**
141. **`frontend/discourse/app/controllers/second-factor-auth.js`** -> AI Confidence: **99.31%**
142. **`frontend/discourse/app/controllers/signup.js`** -> AI Confidence: **99.31%**
143. **`frontend/discourse/app/controllers/topic.js`** -> AI Confidence: **99.31%**
144. **`frontend/discourse/app/controllers/user-topics-list.js`** -> AI Confidence: **99.31%**
145. **`frontend/discourse/app/controllers/user.js`** -> AI Confidence: **99.31%**
146. **`frontend/discourse/app/helpers/category-link.js`** -> AI Confidence: **99.31%**
147. **`frontend/discourse/app/initializers/discourse-bootstrap.js`** -> AI Confidence: **99.31%**
148. **`frontend/discourse/app/initializers/freeze-block-registry.js`** -> AI Confidence: **99.31%**
149. **`frontend/discourse/app/instance-initializers/subscribe-user-notifications.js`** -> AI Confidence: **99.31%**
150. **`frontend/discourse/app/models/composer.js`** -> AI Confidence: **99.31%**
151. **`frontend/discourse/app/models/nav-item.js`** -> AI Confidence: **99.31%**
152. **`frontend/discourse/app/models/post-stream.js`** -> AI Confidence: **99.31%**
153. **`frontend/discourse/app/models/topic-tracking-state.js`** -> AI Confidence: **99.31%**
154. **`frontend/discourse/app/models/user-action.js`** -> AI Confidence: **99.31%**
155. **`frontend/discourse/app/modifiers/d-autocomplete.js`** -> AI Confidence: **99.31%**
156. **`frontend/discourse/app/modifiers/post-stream-viewport-tracker.js`** -> AI Confidence: **99.31%**
157. **`frontend/discourse/app/routes/login.js`** -> AI Confidence: **99.31%**
158. **`frontend/discourse/app/routes/signup.js`** -> AI Confidence: **99.31%**
159. **`frontend/discourse/app/routes/tag/show.js`** -> AI Confidence: **99.31%**
160. **`frontend/discourse/app/routes/topic/from-params.js`** -> AI Confidence: **99.31%**
161. **`frontend/discourse/app/services/composer.js`** -> AI Confidence: **99.31%**
162. **`frontend/discourse/app/services/keyboard-shortcuts.js`** -> AI Confidence: **99.31%**
163. **`frontend/discourse/app/services/pm-topic-tracking-state.js`** -> AI Confidence: **99.31%**
164. **`frontend/discourse/app/services/presence.js`** -> AI Confidence: **99.31%**
165. **`frontend/discourse/app/services/screen-track.js`** -> AI Confidence: **99.31%**
166. **`frontend/discourse/app/static/dev-tools/block-debug/patch.js`** -> AI Confidence: **99.31%**
167. **`frontend/discourse/app/static/dev-tools/shared/args-table.gjs`** -> AI Confidence: **99.31%**
168. **`frontend/discourse/app/static/prosemirror/components/image-node-view.gjs`** -> AI Confidence: **99.31%**
169. **`frontend/discourse/app/static/prosemirror/extensions/image.js`** -> AI Confidence: **99.31%**
170. **`frontend/discourse/app/static/wizard/components/fields/dropdown.gjs`** -> AI Confidence: **99.31%**
171. **`frontend/discourse/app/templates/discovery/list.gjs`** -> AI Confidence: **99.31%**
172. **`frontend/discourse/app/templates/full-page-search.gjs`** -> AI Confidence: **99.31%**
173. **`frontend/discourse/app/templates/user.gjs`** -> AI Confidence: **99.31%**
174. **`frontend/discourse/app/templates/user/notifications-index.gjs`** -> AI Confidence: **99.31%**
175. **`frontend/discourse/float-kit/components/d-default-toast.gjs`** -> AI Confidence: **99.31%**
176. **`frontend/discourse/float-kit/components/d-inline-float.gjs`** -> AI Confidence: **99.31%**
177. **`frontend/discourse/float-kit/components/d-tooltip.gjs`** -> AI Confidence: **99.31%**
178. **`frontend/discourse/select-kit/components/category-chooser.js`** -> AI Confidence: **99.31%**
179. **`frontend/discourse/select-kit/components/category-drop.js`** -> AI Confidence: **99.31%**
180. **`frontend/discourse/select-kit/components/category-row.gjs`** -> AI Confidence: **99.31%**
181. **`frontend/discourse/select-kit/components/composer-actions.js`** -> AI Confidence: **99.31%**
182. **`frontend/discourse/select-kit/components/select-kit.js`** -> AI Confidence: **99.31%**
183. **`frontend/discourse/select-kit/components/select-kit/select-kit-filter.gjs`** -> AI Confidence: **99.31%**
184. **`frontend/discourse/select-kit/components/tag-drop.js`** -> AI Confidence: **99.31%**
185. **`frontend/discourse/select-kit/components/topic-notifications-button.gjs`** -> AI Confidence: **99.31%**
186. **`frontend/discourse/truth-helpers/index.js`** -> AI Confidence: **99.31%**
187. **`.devcontainer/scripts/chrome_wrapper`** -> AI Confidence: **99.29%**
188. **`bin/docker/cleanup`** -> AI Confidence: **99.29%**
189. **`bin/system_rspec`** -> AI Confidence: **99.29%**
190. **`config/unicorn_launcher`** -> AI Confidence: **99.29%**
191. **`.devcontainer/scripts/start.rb`** -> AI Confidence: **99.29%**
192. **`.skills/discourse-upcoming-changes/scripts/optimize_upcoming_change_image.rb`** -> AI Confidence: **99.29%**
193. **`app/controllers/admin/config/color_palettes_controller.rb`** -> AI Confidence: **99.29%**
194. **`app/controllers/admin/config/site_settings_controller.rb`** -> AI Confidence: **99.29%**
195. **`app/controllers/admin/reports_controller.rb`** -> AI Confidence: **99.29%**
196. **`app/controllers/composer_controller.rb`** -> AI Confidence: **99.29%**
197. **`app/controllers/directory_items_controller.rb`** -> AI Confidence: **99.29%**
198. **`app/controllers/drafts_controller.rb`** -> AI Confidence: **99.29%**
199. **`app/controllers/email_controller.rb`** -> AI Confidence: **99.29%**
200. **`app/controllers/embed_controller.rb`** -> AI Confidence: **99.29%**
201. **`app/controllers/groups_controller.rb`** -> AI Confidence: **99.29%**
202. **`app/controllers/invites_controller.rb`** -> AI Confidence: **99.29%**
203. **`app/controllers/list_controller.rb`** -> AI Confidence: **99.29%**
204. **`app/controllers/permalinks_controller.rb`** -> AI Confidence: **99.29%**
205. **`app/controllers/presence_controller.rb`** -> AI Confidence: **99.29%**
206. **`app/controllers/reviewables_controller.rb`** -> AI Confidence: **99.29%**
207. **`app/controllers/search_controller.rb`** -> AI Confidence: **99.29%**
208. **`app/controllers/tags_controller.rb`** -> AI Confidence: **99.29%**
209. **`app/controllers/topics_controller.rb`** -> AI Confidence: **99.29%**
210. **`app/controllers/users/omniauth_callbacks_controller.rb`** -> AI Confidence: **99.29%**
211. **`app/controllers/users_controller.rb`** -> AI Confidence: **99.29%**
212. **`app/jobs/regular/bulk_invite.rb`** -> AI Confidence: **99.29%**
213. **`app/jobs/regular/notify_mailing_list_subscribers.rb`** -> AI Confidence: **99.29%**
214. **`app/jobs/regular/process_post.rb`** -> AI Confidence: **99.29%**
215. **`app/jobs/scheduled/call_discourse_hub.rb`** -> AI Confidence: **99.29%**
216. **`app/jobs/scheduled/check_new_features.rb`** -> AI Confidence: **99.29%**
217. **`app/jobs/scheduled/tl3_promotions.rb`** -> AI Confidence: **99.29%**
218. **`app/mailers/invite_mailer.rb`** -> AI Confidence: **99.29%**
219. **`app/models/color_scheme.rb`** -> AI Confidence: **99.29%**
220. **`app/models/concerns/category_hashtag.rb`** -> AI Confidence: **99.29%**
221. **`app/models/concerns/has_post_upload_references.rb`** -> AI Confidence: **99.29%**
222. **`app/models/concerns/reports/associated_accounts_by_provider.rb`** -> AI Confidence: **99.29%**
223. **`app/models/concerns/reports/post_edits.rb`** -> AI Confidence: **99.29%**
224. **`app/models/discourse_connect.rb`** -> AI Confidence: **99.29%**
225. **`app/models/embeddable_host.rb`** -> AI Confidence: **99.29%**
226. **`app/models/invite_redeemer.rb`** -> AI Confidence: **99.29%**
227. **`app/models/post_timing.rb`** -> AI Confidence: **99.29%**
228. **`app/models/quoted_post.rb`** -> AI Confidence: **99.29%**
229. **`app/models/remote_theme.rb`** -> AI Confidence: **99.29%**
230. **`app/models/tag_user.rb`** -> AI Confidence: **99.29%**
231. **`app/models/theme_field.rb`** -> AI Confidence: **99.29%**
232. **`app/models/theme_modifier_set.rb`** -> AI Confidence: **99.29%**
233. **`app/models/theme_setting.rb`** -> AI Confidence: **99.29%**
234. **`app/models/topic_tag.rb`** -> AI Confidence: **99.29%**
235. **`app/models/topic_view_item.rb`** -> AI Confidence: **99.29%**
236. **`app/models/user_avatar.rb`** -> AI Confidence: **99.29%**
237. **`app/models/user_search.rb`** -> AI Confidence: **99.29%**
238. **`app/models/watched_word.rb`** -> AI Confidence: **99.29%**
239. **`app/models/web_hook_event_type.rb`** -> AI Confidence: **99.29%**
240. **`app/serializers/upload_serializer.rb`** -> AI Confidence: **99.29%**
241. **`app/services/color_scheme_revisor.rb`** -> AI Confidence: **99.29%**
242. **`app/services/email_settings_validator.rb`** -> AI Confidence: **99.29%**
243. **`app/services/inline_uploads.rb`** -> AI Confidence: **99.29%**
244. **`app/services/post_owner_changer.rb`** -> AI Confidence: **99.29%**
245. **`app/services/site_setting_update_existing_users.rb`** -> AI Confidence: **99.29%**
246. **`app/services/topic_status_updater.rb`** -> AI Confidence: **99.29%**
247. **`app/services/user_destroyer.rb`** -> AI Confidence: **99.29%**
248. **`app/services/user_updater.rb`** -> AI Confidence: **99.29%**
249. **`bin/rails`** -> AI Confidence: **99.29%**
250. **`bin/turbo_rspec`** -> AI Confidence: **99.29%**
251. **`bin/unicorn`** -> AI Confidence: **99.29%**
252. **`config/environment.rb`** -> AI Confidence: **99.29%**
253. **`config/environments/production.rb`** -> AI Confidence: **99.29%**
254. **`config/environments/profile.rb`** -> AI Confidence: **99.29%**
255. **`config/initializers/000-development_reload_warnings.rb`** -> AI Confidence: **99.29%**
256. **`config/initializers/000-mini_racer.rb`** -> AI Confidence: **99.29%**
257. **`config/initializers/000-post_migration.rb`** -> AI Confidence: **99.29%**
258. **`config/initializers/000-zeitwerk.rb`** -> AI Confidence: **99.29%**
259. **`config/initializers/001-redis.rb`** -> AI Confidence: **99.29%**
260. **`config/initializers/002-rails_failover.rb`** -> AI Confidence: **99.29%**
261. **`config/initializers/004-message_bus.rb`** -> AI Confidence: **99.29%**
262. **`config/initializers/006-ensure_login_hint.rb`** -> AI Confidence: **99.29%**
263. **`config/initializers/009-omniauth.rb`** -> AI Confidence: **99.29%**
264. **`config/initializers/012-web_hook_events.rb`** -> AI Confidence: **99.29%**
265. **`config/initializers/014-track-setting-changes.rb`** -> AI Confidence: **99.29%**
266. **`config/initializers/099-anon-cache.rb`** -> AI Confidence: **99.29%**
267. **`config/initializers/100-flags.rb`** -> AI Confidence: **99.29%**
268. **`config/initializers/100-logster.rb`** -> AI Confidence: **99.29%**
269. **`config/initializers/100-onebox_options.rb`** -> AI Confidence: **99.29%**
270. **`config/initializers/100-push-notifications.rb`** -> AI Confidence: **99.29%**
271. **`config/initializers/100-session_store.rb`** -> AI Confidence: **99.29%**
272. **`config/initializers/100-verify_config.rb`** -> AI Confidence: **99.29%**
273. **`config/initializers/300-perf.rb`** -> AI Confidence: **99.29%**
274. **`config/initializers/400-deprecations.rb`** -> AI Confidence: **99.29%**
275. **`config/routes.rb`** -> AI Confidence: **99.29%**
276. **`db/fixtures/002_groups.rb`** -> AI Confidence: **99.29%**
277. **`db/fixtures/009_users.rb`** -> AI Confidence: **99.29%**
278. **`db/fixtures/010_uploads.rb`** -> AI Confidence: **99.29%**
279. **`db/fixtures/600_themes.rb`** -> AI Confidence: **99.29%**
280. **`db/fixtures/990_settings.rb`** -> AI Confidence: **99.29%**
281. **`db/migrate/20140211230222_move_cas_settings.rb`** -> AI Confidence: **99.29%**
282. **`db/migrate/20150818190757_create_embeddable_hosts.rb`** -> AI Confidence: **99.29%**
283. **`db/migrate/20190313134642_migrate_default_user_email_options.rb`** -> AI Confidence: **99.29%**
284. **`db/migrate/20201117212328_set_category_slug_to_lower.rb`** -> AI Confidence: **99.29%**
285. **`db/migrate/20241204085540_remap_to_fa6_icon_names.rb`** -> AI Confidence: **99.29%**
286. **`db/migrate/20250818063631_migrate_color_schemes_base_scheme_id_from_string_to_int.rb`** -> AI Confidence: **99.29%**
287. **`migrations/config/schema/intermediate_db/tables/categories.rb`** -> AI Confidence: **99.29%**
288. **`migrations/config/schema/intermediate_db/tables/groups.rb`** -> AI Confidence: **99.29%**
289. **`migrations/config/schema/intermediate_db/tables/tags.rb`** -> AI Confidence: **99.29%**
290. **`migrations/config/schema/intermediate_db/tables/users.rb`** -> AI Confidence: **99.29%**
291. **`plugins/automation/app/models/discourse_automation/field.rb`** -> AI Confidence: **99.29%**
292. **`plugins/automation/config/routes.rb`** -> AI Confidence: **99.29%**
293. **`plugins/automation/lib/discourse_automation/scripts/add_user_to_group_through_custom_field.rb`** -> AI Confidence: **99.29%**
294. **`plugins/automation/lib/discourse_automation/scripts/append_last_checked_by.rb`** -> AI Confidence: **99.29%**
295. **`plugins/automation/lib/discourse_automation/scripts/append_last_edited_by.rb`** -> AI Confidence: **99.29%**
296. **`plugins/automation/lib/discourse_automation/scripts/auto_responder.rb`** -> AI Confidence: **99.29%**
297. **`plugins/automation/lib/discourse_automation/scripts/auto_tag_topic.rb`** -> AI Confidence: **99.29%**
298. **`plugins/automation/lib/discourse_automation/scripts/banner_topic.rb`** -> AI Confidence: **99.29%**
299. **`plugins/automation/lib/discourse_automation/scripts/close_topic.rb`** -> AI Confidence: **99.29%**
300. **`plugins/automation/lib/discourse_automation/scripts/email_on_flagged_post.rb`** -> AI Confidence: **99.29%**
301. **`plugins/automation/lib/discourse_automation/scripts/flag_post_on_words.rb`** -> AI Confidence: **99.29%**
302. **`plugins/automation/lib/discourse_automation/scripts/gift_exchange.rb`** -> AI Confidence: **99.29%**
303. **`plugins/automation/lib/discourse_automation/scripts/group_category_notification_default.rb`** -> AI Confidence: **99.29%**
304. **`plugins/automation/lib/discourse_automation/scripts/pin_topic.rb`** -> AI Confidence: **99.29%**
305. **`plugins/automation/lib/discourse_automation/scripts/post.rb`** -> AI Confidence: **99.29%**
306. **`plugins/automation/lib/discourse_automation/scripts/remove_upload_markup_from_deleted_posts.rb`** -> AI Confidence: **99.29%**
307. **`plugins/automation/lib/discourse_automation/scripts/send_pms.rb`** -> AI Confidence: **99.29%**
308. **`plugins/automation/lib/discourse_automation/scripts/set_topic_timer.rb`** -> AI Confidence: **99.29%**
309. **`plugins/automation/lib/discourse_automation/scripts/suspend_user_by_email.rb`** -> AI Confidence: **99.29%**
310. **`plugins/automation/lib/discourse_automation/scripts/topic.rb`** -> AI Confidence: **99.29%**
311. **`plugins/automation/lib/discourse_automation/scripts/user_global_notice.rb`** -> AI Confidence: **99.29%**
312. **`plugins/automation/lib/discourse_automation/scripts/user_group_membership_through_badge.rb`** -> AI Confidence: **99.29%**
313. **`plugins/automation/lib/discourse_automation/scripts/zapier_webhook.rb`** -> AI Confidence: **99.29%**
314. **`plugins/automation/spec/scripts/add_user_to_group_through_custom_field_spec.rb`** -> AI Confidence: **99.29%**
315. **`plugins/automation/spec/scripts/auto_responder_spec.rb`** -> AI Confidence: **99.29%**
316. **`plugins/automation/spec/scripts/auto_tag_topic_spec.rb`** -> AI Confidence: **99.29%**
317. **`plugins/automation/spec/scripts/banner_topic_spec.rb`** -> AI Confidence: **99.29%**
318. **`plugins/automation/spec/scripts/flag_post_on_words_spec.rb`** -> AI Confidence: **99.29%**
319. **`plugins/automation/spec/scripts/gift_exchange_spec.rb`** -> AI Confidence: **99.29%**
320. **`plugins/automation/spec/scripts/group_category_notification_default_spec.rb`** -> AI Confidence: **99.29%**
321. **`plugins/automation/spec/scripts/pin_topic_spec.rb`** -> AI Confidence: **99.29%**
322. **`plugins/automation/spec/scripts/post_spec.rb`** -> AI Confidence: **99.29%**
323. **`plugins/automation/spec/scripts/remove_upload_markup_from_deleted_posts_spec.rb`** -> AI Confidence: **99.29%**
324. **`plugins/automation/spec/scripts/send_pms_spec.rb`** -> AI Confidence: **99.29%**
325. **`plugins/automation/spec/scripts/set_topic_timer_spec.rb`** -> AI Confidence: **99.29%**
326. **`plugins/automation/spec/scripts/suspend_user_by_email_spec.rb`** -> AI Confidence: **99.29%**
327. **`plugins/automation/spec/scripts/topic_required_words_spec.rb`** -> AI Confidence: **99.29%**
328. **`plugins/automation/spec/scripts/topic_spec.rb`** -> AI Confidence: **99.29%**
329. **`plugins/automation/spec/scripts/user_global_notice_spec.rb`** -> AI Confidence: **99.29%**
330. **`plugins/automation/spec/scripts/user_group_membership_through_badge_spec.rb`** -> AI Confidence: **99.29%**
331. **`plugins/chat/app/queries/chat/channel_memberships_query.rb`** -> AI Confidence: **99.29%**
332. **`plugins/chat/app/queries/chat/messages_query.rb`** -> AI Confidence: **99.29%**
333. **`plugins/chat/config/routes.rb`** -> AI Confidence: **99.29%**
334. **`plugins/chat/db/fixtures/600_chat_channels.rb`** -> AI Confidence: **99.29%**
335. **`plugins/chat/plugin.rb`** -> AI Confidence: **99.29%**
336. **`plugins/discourse-ai/app/controllers/discourse_ai/admin/ai_spam_controller.rb`** -> AI Confidence: **99.29%**
337. **`plugins/discourse-ai/app/controllers/discourse_ai/ai_helper/assistant_controller.rb`** -> AI Confidence: **99.29%**
338. **`plugins/discourse-ai/app/controllers/discourse_ai/embeddings/embeddings_controller.rb`** -> AI Confidence: **99.29%**
339. **`plugins/discourse-ai/app/jobs/regular/detect_translate_topic.rb`** -> AI Confidence: **99.29%**
340. **`plugins/discourse-ai/app/models/ai_agent.rb`** -> AI Confidence: **99.29%**
341. **`plugins/discourse-ai/app/models/ai_secret.rb`** -> AI Confidence: **99.29%**
342. **`plugins/discourse-ai/app/services/discourse_ai/agent_importer.rb`** -> AI Confidence: **99.29%**
343. **`plugins/discourse-ai/db/fixtures/agents/603_ai_agents.rb`** -> AI Confidence: **99.29%**
344. **`plugins/discourse-ai/db/migrate/20240603143158_seed_oss_models.rb`** -> AI Confidence: **99.29%**
345. **`plugins/discourse-ai/db/post_migrate/20260206013737_migrate_existing_secrets_to_ai_secrets.rb`** -> AI Confidence: **99.29%**
346. **`plugins/discourse-ai/db/post_migrate/20260306000002_finalize_ai_agents_schema.rb`** -> AI Confidence: **99.29%**
347. **`plugins/discourse-ai/discourse_automation/ai_tool_action.rb`** -> AI Confidence: **99.29%**
348. **`plugins/discourse-ai/discourse_automation/llm_agent_triage.rb`** -> AI Confidence: **99.29%**
349. **`plugins/discourse-ai/discourse_automation/llm_report.rb`** -> AI Confidence: **99.29%**
350. **`plugins/discourse-ai/discourse_automation/llm_tagger.rb`** -> AI Confidence: **99.29%**
351. **`plugins/discourse-ai/discourse_automation/llm_triage.rb`** -> AI Confidence: **99.29%**
352. **`plugins/discourse-ai/lib/utils/ai_staff_action_logger.rb`** -> AI Confidence: **99.29%**
353. **`plugins/discourse-ai/lib/utils/research/filter.rb`** -> AI Confidence: **99.29%**
354. **`plugins/discourse-ai/lib/utils/search.rb`** -> AI Confidence: **99.29%**
355. **`plugins/discourse-ai/spec/lib/agents/tools/close_topic_spec.rb`** -> AI Confidence: **99.29%**
356. **`plugins/discourse-ai/spec/lib/agents/tools/discourse_meta_search_spec.rb`** -> AI Confidence: **99.29%**
357. **`plugins/discourse-ai/spec/lib/agents/tools/github_search_files_spec.rb`** -> AI Confidence: **99.29%**
358. **`plugins/discourse-ai/spec/lib/agents/tools/mcp_spec.rb`** -> AI Confidence: **99.29%**
359. **`plugins/discourse-ai/spec/lib/agents/tools/read_artifact_spec.rb`** -> AI Confidence: **99.29%**
360. **`plugins/discourse-ai/spec/lib/agents/tools/search_spec.rb`** -> AI Confidence: **99.29%**
361. **`plugins/discourse-ai/spec/lib/agents/tools/unlist_topic_spec.rb`** -> AI Confidence: **99.29%**
362. **`plugins/discourse-ai/spec/lib/utils/ai_staff_action_logger_spec.rb`** -> AI Confidence: **99.29%**
363. **`plugins/discourse-ai/spec/lib/utils/best_effort_json_parser_spec.rb`** -> AI Confidence: **99.29%**
364. **`plugins/discourse-ai/spec/lib/utils/diff_utils/safety_checker_spec.rb`** -> AI Confidence: **99.29%**
365. **`plugins/discourse-ai/spec/lib/utils/pdf_to_text_spec.rb`** -> AI Confidence: **99.29%**
366. **`plugins/discourse-assign/config/routes.rb`** -> AI Confidence: **99.29%**
367. **`plugins/discourse-assign/plugin.rb`** -> AI Confidence: **99.29%**
368. **`plugins/discourse-cakeday/app/controllers/discourse_cakeday/cakeday_controller.rb`** -> AI Confidence: **99.29%**
369. **`plugins/discourse-cakeday/config/routes.rb`** -> AI Confidence: **99.29%**
370. **`plugins/discourse-calendar/config/routes.rb`** -> AI Confidence: **99.29%**
371. **`plugins/discourse-calendar/db/migrate/20251017115448_migrate_deprecated_holiday_region_codes.rb`** -> AI Confidence: **99.29%**
372. **`plugins/discourse-calendar/jobs/regular/discourse_post_event/send_reminder.rb`** -> AI Confidence: **99.29%**
373. **`plugins/discourse-chat-integration/app/jobs/onceoff/migrate_from_slack_official.rb`** -> AI Confidence: **99.29%**
374. **`plugins/discourse-chat-integration/app/routes/discourse.rb`** -> AI Confidence: **99.29%**
375. **`plugins/discourse-chat-integration/app/routes/discourse_chat_integration.rb`** -> AI Confidence: **99.29%**
376. **`plugins/discourse-chat-integration/app/services/manager.rb`** -> AI Confidence: **99.29%**
377. **`plugins/discourse-chat-integration/db/migrate/20240903184807_migrate_tag_added_filter_to_all_providers.rb`** -> AI Confidence: **99.29%**
378. **`plugins/discourse-chat-integration/plugin.rb`** -> AI Confidence: **99.29%**
379. **`plugins/discourse-data-explorer/config/routes.rb`** -> AI Confidence: **99.29%**
380. **`plugins/discourse-data-explorer/db/migrate/20200810053843_create_data_explorer_queries.rb`** -> AI Confidence: **99.29%**
381. **`plugins/discourse-data-explorer/plugin.rb`** -> AI Confidence: **99.29%**
382. **`plugins/discourse-details/plugin.rb`** -> AI Confidence: **99.29%**
383. **`plugins/discourse-gamification/config/routes.rb`** -> AI Confidence: **99.29%**
384. **`plugins/discourse-gamification/db/fixtures/001_gamification_leaderboards.rb`** -> AI Confidence: **99.29%**
385. **`plugins/discourse-hcaptcha/config/routes.rb`** -> AI Confidence: **99.29%**
386. **`plugins/discourse-local-dates/plugin.rb`** -> AI Confidence: **99.29%**
387. **`plugins/discourse-lti/plugin.rb`** -> AI Confidence: **99.29%**
388. **`plugins/discourse-math/plugin.rb`** -> AI Confidence: **99.29%**
389. **`plugins/discourse-narrative-bot/config/routes.rb`** -> AI Confidence: **99.29%**
390. **`plugins/discourse-narrative-bot/db/fixtures/001_discobot.rb`** -> AI Confidence: **99.29%**
391. **`plugins/discourse-narrative-bot/db/fixtures/002_badges.rb`** -> AI Confidence: **99.29%**
392. **`plugins/discourse-narrative-bot/plugin.rb`** -> AI Confidence: **99.29%**
393. **`plugins/discourse-patreon/config/routes.rb`** -> AI Confidence: **99.29%**
394. **`plugins/discourse-policy/config/routes.rb`** -> AI Confidence: **99.29%**
395. **`plugins/discourse-post-voting/config/routes.rb`** -> AI Confidence: **99.29%**
396. **`plugins/discourse-presence/plugin.rb`** -> AI Confidence: **99.29%**
397. **`plugins/discourse-reactions/config/routes.rb`** -> AI Confidence: **99.29%**
398. **`plugins/discourse-reactions/db/migrate/20221122010538_rename_badge.rb`** -> AI Confidence: **99.29%**
399. **`plugins/discourse-rewind/app/services/discourse_rewind/action/reactions.rb`** -> AI Confidence: **99.29%**
400. **`plugins/discourse-rewind/app/services/discourse_rewind/action/reading_time.rb`** -> AI Confidence: **99.29%**
401. **`plugins/discourse-rewind/app/services/discourse_rewind/action/time_of_day_activity.rb`** -> AI Confidence: **99.29%**
402. **`plugins/discourse-rewind/config/routes.rb`** -> AI Confidence: **99.29%**
403. **`plugins/discourse-solved/config/routes.rb`** -> AI Confidence: **99.29%**
404. **`plugins/discourse-solved/db/migrate/20221121223417_rename_badges.rb`** -> AI Confidence: **99.29%**
405. **`plugins/discourse-subscriptions/config/routes.rb`** -> AI Confidence: **99.29%**
406. **`plugins/discourse-topic-voting/config/routes.rb`** -> AI Confidence: **99.29%**
407. **`plugins/discourse-topic-voting/plugin.rb`** -> AI Confidence: **99.29%**
408. **`plugins/discourse-user-notes/app/controllers/discourse_user_notes/user_notes_controller.rb`** -> AI Confidence: **99.29%**
409. **`plugins/discourse-user-notes/config/routes.rb`** -> AI Confidence: **99.29%**
410. **`plugins/footnote/plugin.rb`** -> AI Confidence: **99.29%**
411. **`plugins/poll/config/routes.rb`** -> AI Confidence: **99.29%**
412. **`plugins/poll/db/migrate/20180820080623_migrate_polls_data.rb`** -> AI Confidence: **99.29%**
413. **`plugins/styleguide/config/routes.rb`** -> AI Confidence: **99.29%**
414. **`script/analyse_message_bus.rb`** -> AI Confidence: **99.29%**
415. **`script/backport.rb`** -> AI Confidence: **99.29%**
416. **`script/benchmarks/cache/bench.rb`** -> AI Confidence: **99.29%**
417. **`script/bulk_import/uploads_importer.rb`** -> AI Confidence: **99.29%**
418. **`script/bulk_import/vanilla.rb`** -> AI Confidence: **99.29%**
419. **`script/diff_heaps.rb`** -> AI Confidence: **99.29%**
420. **`script/promote_migrations`** -> AI Confidence: **99.29%**
421. **`script/redis_memory.rb`** -> AI Confidence: **99.29%**
422. **`script/start_test_db.rb`** -> AI Confidence: **99.29%**
423. **`script/test_email_settings.rb`** -> AI Confidence: **99.29%**
424. **`frontend/discourse-types/process-package-json.js`** -> AI Confidence: **99.29%**
425. **`frontend/discourse/app/components/conditional-in-element.gjs`** -> AI Confidence: **99.29%**
426. **`frontend/discourse/app/components/password-field.js`** -> AI Confidence: **99.29%**
427. **`frontend/discourse/app/instance-initializers/sniff-capabilities.js`** -> AI Confidence: **99.29%**
428. **`frontend/discourse/app/resolver-shims.js`** -> AI Confidence: **99.29%**
429. **`frontend/discourse/config/environment.js`** -> AI Confidence: **99.29%**
430. **`frontend/discourse/config/optional-features.json.js`** -> AI Confidence: **99.29%**
431. **`frontend/discourse/config/targets.js`** -> AI Confidence: **99.29%**
432. **`frontend/discourse/public/assets/scripts/discourse-test-load-dynamic-js.js`** -> AI Confidence: **99.29%**
433. **`frontend/discourse/scripts/browser-detect.js`** -> AI Confidence: **99.29%**
434. **`frontend/discourse/scripts/google-universal-analytics-v3.js`** -> AI Confidence: **99.29%**
435. **`frontend/discourse/scripts/onpopstate-handler.js`** -> AI Confidence: **99.29%**
436. **`frontend/discourse/scripts/pageview.js`** -> AI Confidence: **99.29%**
437. **`frontend/discourse/tests/fixtures/badges-fixture.js`** -> AI Confidence: **99.29%**
438. **`frontend/discourse/tests/fixtures/discovery-fixtures.js`** -> AI Confidence: **99.29%**
439. **`frontend/discourse/tests/fixtures/drafts.js`** -> AI Confidence: **99.29%**
440. **`frontend/discourse/tests/fixtures/group-fixtures.js`** -> AI Confidence: **99.29%**
441. **`frontend/discourse/tests/fixtures/groups-fixtures.js`** -> AI Confidence: **99.29%**
442. **`frontend/discourse/tests/fixtures/post.js`** -> AI Confidence: **99.29%**
443. **`frontend/discourse/tests/fixtures/site-fixtures.js`** -> AI Confidence: **99.29%**
444. **`frontend/discourse/tests/fixtures/site-settings.js`** -> AI Confidence: **99.29%**
445. **`frontend/discourse/tests/fixtures/top-fixtures.js`** -> AI Confidence: **99.29%**
446. **`frontend/discourse/tests/fixtures/user-fixtures.js`** -> AI Confidence: **99.29%**
447. **`frontend/discourse/tests/fixtures/watched-words-fixtures.js`** -> AI Confidence: **99.29%**
448. **`frontend/discourse/tests/helpers/site.js`** -> AI Confidence: **99.29%**
449. **`frontend/ember-cli-progress-ci/index.js`** -> AI Confidence: **99.29%**
450. **`frontend/pretty-text/addon/text-replace.js`** -> AI Confidence: **99.29%**
451. **`frontend/discourse-plugins/index.js`** -> AI Confidence: **99.24%**
452. **`frontend/discourse/admin/components/admin-badges-award.gjs`** -> AI Confidence: **99.24%**
453. **`frontend/discourse/admin/components/admin-badges-show.gjs`** -> AI Confidence: **99.24%**
454. **`frontend/discourse/admin/components/admin-config-areas/components.gjs`** -> AI Confidence: **99.24%**
455. **`frontend/discourse/admin/components/admin-plugins-list-item.gjs`** -> AI Confidence: **99.24%**
456. **`frontend/discourse/admin/components/admin-report-storage-stats.gjs`** -> AI Confidence: **99.24%**
457. **`frontend/discourse/admin/components/admin-search.gjs`** -> AI Confidence: **99.24%**
458. **`frontend/discourse/admin/components/admin-section-landing-item.gjs`** -> AI Confidence: **99.24%**
459. **`frontend/discourse/admin/components/admin-theme-editor.gjs`** -> AI Confidence: **99.24%**
460. **`frontend/discourse/admin/components/edit-category-general.gjs`** -> AI Confidence: **99.24%**
461. **`frontend/discourse/admin/components/edit-category-tab.gjs`** -> AI Confidence: **99.24%**
462. **`frontend/discourse/admin/components/modal/merge-users-progress.gjs`** -> AI Confidence: **99.24%**
463. **`frontend/discourse/admin/components/schema-setting/editor.gjs`** -> AI Confidence: **99.24%**
464. **`frontend/discourse/admin/components/schema-setting/editor/tree-node.gjs`** -> AI Confidence: **99.24%**
465. **`frontend/discourse/admin/components/schema-setting/types/datetime.gjs`** -> AI Confidence: **99.24%**
466. **`frontend/discourse/admin/components/site-setting.gjs`** -> AI Confidence: **99.24%**
467. **`frontend/discourse/admin/components/site-settings/file-types-list.gjs`** -> AI Confidence: **99.24%**
468. **`frontend/discourse/admin/components/theme-upload-add.gjs`** -> AI Confidence: **99.24%**
469. **`frontend/discourse/admin/components/upsert-category/permission-row.gjs`** -> AI Confidence: **99.24%**
470. **`frontend/discourse/admin/components/upsert-category/security.gjs`** -> AI Confidence: **99.24%**
471. **`frontend/discourse/admin/components/upsert-category/settings.gjs`** -> AI Confidence: **99.24%**
472. **`frontend/discourse/admin/components/value-list.gjs`** -> AI Confidence: **99.24%**
473. **`frontend/discourse/admin/controllers/admin-api-keys/new.js`** -> AI Confidence: **99.24%**
474. **`frontend/discourse/admin/controllers/admin-logs/screened-ip-addresses.js`** -> AI Confidence: **99.24%**
475. **`frontend/discourse/admin/controllers/admin-watched-words/action.js`** -> AI Confidence: **99.24%**
476. **`frontend/discourse/admin/models/theme.js`** -> AI Confidence: **99.24%**
477. **`frontend/discourse/admin/services/site-setting-change-tracker.js`** -> AI Confidence: **99.24%**
478. **`frontend/discourse/admin/templates/admin-customize-themes/show/index.gjs`** -> AI Confidence: **99.24%**
479. **`frontend/discourse/admin/templates/admin-email-logs/sent.gjs`** -> AI Confidence: **99.24%**
480. **`frontend/discourse/admin/templates/admin-email/preview-digest.gjs`** -> AI Confidence: **99.24%**
481. **`frontend/discourse/admin/templates/admin-logs/screened-ip-addresses.gjs`** -> AI Confidence: **99.24%**
482. **`frontend/discourse/admin/templates/admin-permalinks/index.gjs`** -> AI Confidence: **99.24%**
483. **`frontend/discourse/admin/templates/admin-user/index.gjs`** -> AI Confidence: **99.24%**
484. **`frontend/discourse/admin/templates/edit-category/tabs.gjs`** -> AI Confidence: **99.24%**
485. **`frontend/discourse/app/components/ace-editor.gjs`** -> AI Confidence: **99.24%**
486. **`frontend/discourse/app/components/badge-card.gjs`** -> AI Confidence: **99.24%**
487. **`frontend/discourse/app/components/bookmark-menu.gjs`** -> AI Confidence: **99.24%**
488. **`frontend/discourse/app/components/bread-crumbs.gjs`** -> AI Confidence: **99.24%**
489. **`frontend/discourse/app/components/card-contents-base.js`** -> AI Confidence: **99.24%**
490. **`frontend/discourse/app/components/composer-editor.gjs`** -> AI Confidence: **99.24%**
491. **`frontend/discourse/app/components/d-modal.gjs`** -> AI Confidence: **99.24%**
492. **`frontend/discourse/app/components/d-otp/index.gjs`** -> AI Confidence: **99.24%**
493. **`frontend/discourse/app/components/d-page-header.gjs`** -> AI Confidence: **99.24%**
494. **`frontend/discourse/app/components/d-select.gjs`** -> AI Confidence: **99.24%**
495. **`frontend/discourse/app/components/date-picker.gjs`** -> AI Confidence: **99.24%**
496. **`frontend/discourse/app/components/dialog-messages/confirm-session.gjs`** -> AI Confidence: **99.24%**
497. **`frontend/discourse/app/components/discourse-banner.gjs`** -> AI Confidence: **99.24%**
498. **`frontend/discourse/app/components/edit-topic-timer-form.gjs`** -> AI Confidence: **99.24%**
499. **`frontend/discourse/app/components/flag-action-type.gjs`** -> AI Confidence: **99.24%**
500. **`frontend/discourse/app/components/future-date-input.gjs`** -> AI Confidence: **99.24%**
501. **`frontend/discourse/app/components/group-card.gjs`** -> AI Confidence: **99.24%**
502. **`frontend/discourse/app/components/group-flair-inputs.gjs`** -> AI Confidence: **99.24%**
503. **`frontend/discourse/app/components/group-manage-save-button.gjs`** -> AI Confidence: **99.24%**
504. **`frontend/discourse/app/components/groups-form-interaction-fields.gjs`** -> AI Confidence: **99.24%**
505. **`frontend/discourse/app/components/groups-form-profile-fields.gjs`** -> AI Confidence: **99.24%**
506. **`frontend/discourse/app/components/header/contents.gjs`** -> AI Confidence: **99.24%**
507. **`frontend/discourse/app/components/header/topic/info.gjs`** -> AI Confidence: **99.24%**
508. **`frontend/discourse/app/components/header/user-dropdown/notifications.gjs`** -> AI Confidence: **99.24%**
509. **`frontend/discourse/app/components/local-login-form.gjs`** -> AI Confidence: **99.24%**
510. **`frontend/discourse/app/components/login-buttons.gjs`** -> AI Confidence: **99.24%**
511. **`frontend/discourse/app/components/modal/associate-account-confirm.gjs`** -> AI Confidence: **99.24%**
512. **`frontend/discourse/app/components/modal/edit-topic-timer.gjs`** -> AI Confidence: **99.24%**
513. **`frontend/discourse/app/components/modal/edit-user-directory-columns.gjs`** -> AI Confidence: **99.24%**
514. **`frontend/discourse/app/components/modal/feature-topic.gjs`** -> AI Confidence: **99.24%**
515. **`frontend/discourse/app/components/modal/flag.gjs`** -> AI Confidence: **99.24%**
516. **`frontend/discourse/app/components/modal/history/revisions.gjs`** -> AI Confidence: **99.24%**
517. **`frontend/discourse/app/components/modal/raw-email.gjs`** -> AI Confidence: **99.24%**
518. **`frontend/discourse/app/components/modal/second-factor-backup-edit.gjs`** -> AI Confidence: **99.24%**
519. **`frontend/discourse/app/components/notification-consent-banner.gjs`** -> AI Confidence: **99.24%**
520. **`frontend/discourse/app/components/page-loading-slider.gjs`** -> AI Confidence: **99.24%**
521. **`frontend/discourse/app/components/parent-category-row.gjs`** -> AI Confidence: **99.24%**
522. **`frontend/discourse/app/components/pinned-options.gjs`** -> AI Confidence: **99.24%**
523. **`frontend/discourse/app/components/plugin-outlet.gjs`** -> AI Confidence: **99.24%**
524. **`frontend/discourse/app/components/post-list/index.gjs`** -> AI Confidence: **99.24%**
525. **`frontend/discourse/app/components/post-list/item/details.gjs`** -> AI Confidence: **99.24%**
526. **`frontend/discourse/app/components/post-stream.gjs`** -> AI Confidence: **99.24%**
527. **`frontend/discourse/app/components/post-translation-editor.gjs`** -> AI Confidence: **99.24%**
528. **`frontend/discourse/app/components/post/cooked-html.gjs`** -> AI Confidence: **99.24%**
529. **`frontend/discourse/app/components/search-menu/results.gjs`** -> AI Confidence: **99.24%**
530. **`frontend/discourse/app/components/search-menu/results/recent-searches.gjs`** -> AI Confidence: **99.24%**
531. **`frontend/discourse/app/components/sidebar/common/custom-section.gjs`** -> AI Confidence: **99.24%**
532. **`frontend/discourse/app/components/sidebar/edit-navigation-menu/tags-modal.gjs`** -> AI Confidence: **99.24%**
533. **`frontend/discourse/app/components/sidebar/footer.gjs`** -> AI Confidence: **99.24%**
534. **`frontend/discourse/app/components/sidebar/section.gjs`** -> AI Confidence: **99.24%**
535. **`frontend/discourse/app/components/tag-list.gjs`** -> AI Confidence: **99.24%**
536. **`frontend/discourse/app/components/tag-settings.gjs`** -> AI Confidence: **99.24%**
537. **`frontend/discourse/app/components/time-shortcut-picker.gjs`** -> AI Confidence: **99.24%**
538. **`frontend/discourse/app/components/toolbar-popup-menu-options.gjs`** -> AI Confidence: **99.24%**
539. **`frontend/discourse/app/components/topic-footer-buttons.gjs`** -> AI Confidence: **99.24%**
540. **`frontend/discourse/app/components/topic-list/list.gjs`** -> AI Confidence: **99.24%**
541. **`frontend/discourse/app/components/topic-map/topic-map-summary.gjs`** -> AI Confidence: **99.24%**
542. **`frontend/discourse/app/components/topic-title.gjs`** -> AI Confidence: **99.24%**
543. **`frontend/discourse/app/components/uppy-image-uploader.gjs`** -> AI Confidence: **99.24%**
544. **`frontend/discourse/app/components/user-autocomplete-results.gjs`** -> AI Confidence: **99.24%**
545. **`frontend/discourse/app/components/user-info.gjs`** -> AI Confidence: **99.24%**
546. **`frontend/discourse/app/components/user-menu/items-list.gjs`** -> AI Confidence: **99.24%**
547. **`frontend/discourse/app/controllers/application.js`** -> AI Confidence: **99.24%**
548. **`frontend/discourse/app/controllers/tags/index.js`** -> AI Confidence: **99.24%**
549. **`frontend/discourse/app/form-kit/components/fk/control/color.gjs`** -> AI Confidence: **99.24%**
550. **`frontend/discourse/app/models/category-list.js`** -> AI Confidence: **99.24%**
551. **`frontend/discourse/app/models/category.js`** -> AI Confidence: **99.24%**
552. **`frontend/discourse/app/models/post.js`** -> AI Confidence: **99.24%**
553. **`frontend/discourse/app/models/topic-list.js`** -> AI Confidence: **99.24%**
554. **`frontend/discourse/app/models/topic.js`** -> AI Confidence: **99.24%**
555. **`frontend/discourse/app/routes/application.js`** -> AI Confidence: **99.24%**
556. **`frontend/discourse/app/services/deprecation-warning-handler.js`** -> AI Confidence: **99.24%**
557. **`frontend/discourse/app/static/dev-tools/plugin-outlet-debug/outlet-info.gjs`** -> AI Confidence: **99.24%**
558. **`frontend/discourse/app/static/prosemirror/components/image-alt-text-input.gjs`** -> AI Confidence: **99.24%**
559. **`frontend/discourse/app/static/prosemirror/extensions/link-toolbar.js`** -> AI Confidence: **99.24%**
560. **`frontend/discourse/app/templates/activate-account.gjs`** -> AI Confidence: **99.24%**
561. **`frontend/discourse/app/templates/badges/show.gjs`** -> AI Confidence: **99.24%**
562. **`frontend/discourse/app/templates/group/index.gjs`** -> AI Confidence: **99.24%**
563. **`frontend/discourse/app/templates/invites/show.gjs`** -> AI Confidence: **99.24%**
564. **`frontend/discourse/app/templates/login.gjs`** -> AI Confidence: **99.24%**
565. **`frontend/discourse/app/templates/password-reset.gjs`** -> AI Confidence: **99.24%**
566. **`frontend/discourse/app/templates/preferences/account.gjs`** -> AI Confidence: **99.24%**
567. **`frontend/discourse/app/templates/preferences/interface.gjs`** -> AI Confidence: **99.24%**
568. **`frontend/discourse/app/templates/preferences/second-factor.gjs`** -> AI Confidence: **99.24%**
569. **`frontend/discourse/app/templates/signup.gjs`** -> AI Confidence: **99.24%**
570. **`frontend/discourse/app/templates/topic.gjs`** -> AI Confidence: **99.24%**
571. **`frontend/discourse/app/templates/user-invited/show.gjs`** -> AI Confidence: **99.24%**
572. **`frontend/discourse/app/templates/user-topics-list.gjs`** -> AI Confidence: **99.24%**
573. **`frontend/discourse/app/templates/user/bookmarks.gjs`** -> AI Confidence: **99.24%**
574. **`frontend/discourse/app/templates/user/collapsed-info.gjs`** -> AI Confidence: **99.24%**
575. **`frontend/discourse/dialog-holder/components/dialog-holder.gjs`** -> AI Confidence: **99.24%**
576. **`frontend/discourse/float-kit/components/d-menu.gjs`** -> AI Confidence: **99.24%**
577. **`frontend/discourse/select-kit/components/icon-picker.js`** -> AI Confidence: **99.24%**
578. **`frontend/discourse/select-kit/components/mini-tag-chooser.js`** -> AI Confidence: **99.24%**
579. **`frontend/discourse/select-kit/components/multi-select.gjs`** -> AI Confidence: **99.24%**
580. **`frontend/discourse/select-kit/components/select-kit/select-kit-row.gjs`** -> AI Confidence: **99.24%**
581. **`frontend/discourse/select-kit/components/selected-name.gjs`** -> AI Confidence: **99.24%**
582. **`frontend/discourse/select-kit/components/tag-chooser.js`** -> AI Confidence: **99.24%**
583. **`frontend/discourse/select-kit/components/user-chooser.js`** -> AI Confidence: **99.24%**
584. **`app/models/group.rb`** -> AI Confidence: **99.23%**
585. **`frontend/discourse/admin/components/admin-backups-actions.gjs`** -> AI Confidence: **99.23%**
586. **`frontend/discourse/admin/components/admin-config-area-card.gjs`** -> AI Confidence: **99.23%**
587. **`frontend/discourse/admin/components/schema-setting/types/string.gjs`** -> AI Confidence: **99.23%**
588. **`frontend/discourse/admin/controllers/admin-config/color-palettes/index.js`** -> AI Confidence: **99.23%**
589. **`frontend/discourse/admin/controllers/admin-site-text/edit.js`** -> AI Confidence: **99.23%**
590. **`frontend/discourse/admin/models/web-hook.js`** -> AI Confidence: **99.23%**
591. **`frontend/discourse/app/blocks/conditions/index.js`** -> AI Confidence: **99.23%**
592. **`frontend/discourse/app/components/d-page-subheader.gjs`** -> AI Confidence: **99.23%**
593. **`frontend/discourse/app/components/emoji-picker/index.gjs`** -> AI Confidence: **99.23%**
594. **`frontend/discourse/app/components/empty-topic-filter.gjs`** -> AI Confidence: **99.23%**
595. **`frontend/discourse/app/components/footer-nav.gjs`** -> AI Confidence: **99.23%**
596. **`frontend/discourse/app/components/form-template-field/textarea.gjs`** -> AI Confidence: **99.23%**
597. **`frontend/discourse/app/components/group-manage-logs-row.gjs`** -> AI Confidence: **99.23%**
598. **`frontend/discourse/app/components/selected-posts.gjs`** -> AI Confidence: **99.23%**
599. **`frontend/discourse/app/components/sidebar.gjs`** -> AI Confidence: **99.23%**
600. **`frontend/discourse/app/components/small-user-list.gjs`** -> AI Confidence: **99.23%**
601. **`frontend/discourse/app/components/user-nav.gjs`** -> AI Confidence: **99.23%**
602. **`frontend/discourse/app/controllers/badges/show.js`** -> AI Confidence: **99.23%**
603. **`frontend/discourse/app/controllers/preferences/tracking.js`** -> AI Confidence: **99.23%**
604. **`frontend/discourse/app/form-kit/components/fk/field-data.gjs`** -> AI Confidence: **99.23%**
605. **`frontend/discourse/app/models/user-badge.js`** -> AI Confidence: **99.23%**
606. **`frontend/discourse/app/services/client-error-handler.js`** -> AI Confidence: **99.23%**
607. **`frontend/discourse/app/services/history-store.js`** -> AI Confidence: **99.23%**
608. **`frontend/discourse/app/services/network-connectivity.js`** -> AI Confidence: **99.23%**
609. **`frontend/discourse/app/templates/email-login.gjs`** -> AI Confidence: **99.23%**
610. **`frontend/discourse/app/templates/second-factor-auth.gjs`** -> AI Confidence: **99.23%**
611. **`frontend/discourse/float-kit/services/toasts.js`** -> AI Confidence: **99.23%**
612. **`app/controllers/admin/themes_controller.rb`** -> AI Confidence: **99.2%**
613. **`app/controllers/uploads_controller.rb`** -> AI Confidence: **99.2%**
614. **`app/mailers/user_notifications.rb`** -> AI Confidence: **99.2%**
615. **`plugins/discourse-reactions/plugin.rb`** -> AI Confidence: **99.2%**
616. **`plugins/discourse-user-notes/plugin.rb`** -> AI Confidence: **99.2%**
617. **`plugins/discourse-zendesk-plugin/plugin.rb`** -> AI Confidence: **99.18%**
618. **`frontend/asset-processor/postcss.js`** -> AI Confidence: **99.18%**
619. **`frontend/discourse/admin/components/admin-config-areas/user-fields-list.gjs`** -> AI Confidence: **99.18%**
620. **`frontend/discourse/admin/components/admin-config-areas/webhooks-list.gjs`** -> AI Confidence: **99.18%**
621. **`frontend/discourse/admin/components/admin-embedding-host-form.gjs`** -> AI Confidence: **99.18%**
622. **`frontend/discourse/admin/components/admin-filtered-site-settings.gjs`** -> AI Confidence: **99.18%**
623. **`frontend/discourse/admin/components/admin-flag-item.gjs`** -> AI Confidence: **99.18%**
624. **`frontend/discourse/admin/components/admin-penalty-post-action.gjs`** -> AI Confidence: **99.18%**
625. **`frontend/discourse/admin/components/admin-penalty-similar-users.gjs`** -> AI Confidence: **99.18%**
626. **`frontend/discourse/admin/components/admin-site-settings-filter-controls.gjs`** -> AI Confidence: **99.18%**
627. **`frontend/discourse/admin/components/bulk-user-delete-confirmation.gjs`** -> AI Confidence: **99.18%**
628. **`frontend/discourse/admin/components/dashboard-problems.gjs`** -> AI Confidence: **99.18%**
629. **`frontend/discourse/admin/components/edit-category-tags.gjs`** -> AI Confidence: **99.18%**
630. **`frontend/discourse/admin/components/emoji-uploader.gjs`** -> AI Confidence: **99.18%**
631. **`frontend/discourse/admin/components/images-uploader.gjs`** -> AI Confidence: **99.18%**
632. **`frontend/discourse/admin/components/modal/edit-badge-groupings.gjs`** -> AI Confidence: **99.18%**
633. **`frontend/discourse/admin/components/modal/start-backup.gjs`** -> AI Confidence: **99.18%**
634. **`frontend/discourse/admin/components/permalink-form.gjs`** -> AI Confidence: **99.18%**
635. **`frontend/discourse/admin/components/schema-setting/editor/child-tree.gjs`** -> AI Confidence: **99.18%**
636. **`frontend/discourse/admin/components/screened-ip-address-form.gjs`** -> AI Confidence: **99.18%**
637. **`frontend/discourse/admin/components/site-settings/compact-list.gjs`** -> AI Confidence: **99.18%**
638. **`frontend/discourse/admin/components/site-text-summary.gjs`** -> AI Confidence: **99.18%**
639. **`frontend/discourse/admin/components/tags-admin-dropdown.js`** -> AI Confidence: **99.18%**
640. **`frontend/discourse/admin/components/themes-grid.gjs`** -> AI Confidence: **99.18%**
641. **`frontend/discourse/admin/controllers/admin-permalinks/index.js`** -> AI Confidence: **99.18%**
642. **`frontend/discourse/admin/controllers/admin-user/badges.js`** -> AI Confidence: **99.18%**
643. **`frontend/discourse/admin/models/admin-user.js`** -> AI Confidence: **99.18%**
644. **`frontend/discourse/admin/routes/admin/backups.js`** -> AI Confidence: **99.18%**
645. **`frontend/discourse/admin/services/admin-badges.js`** -> AI Confidence: **99.18%**
646. **`frontend/discourse/admin/services/admin-emojis.js`** -> AI Confidence: **99.18%**
647. **`frontend/discourse/admin/services/admin-tools.js`** -> AI Confidence: **99.18%**
648. **`frontend/discourse/admin/templates/admin-site-text/edit.gjs`** -> AI Confidence: **99.18%**
649. **`frontend/discourse/admin/templates/admin-site-text/index.gjs`** -> AI Confidence: **99.18%**
650. **`frontend/discourse/admin/templates/admin/backups/index.gjs`** -> AI Confidence: **99.18%**
651. **`frontend/discourse/admin/templates/admin/dashboard/general.gjs`** -> AI Confidence: **99.18%**
652. **`frontend/discourse/app/components/avatar-uploader.gjs`** -> AI Confidence: **99.18%**
653. **`frontend/discourse/app/components/calendar-subscription-url.gjs`** -> AI Confidence: **99.18%**
654. **`frontend/discourse/app/components/categories-boxes-with-topics.gjs`** -> AI Confidence: **99.18%**
655. **`frontend/discourse/app/components/categories-boxes.gjs`** -> AI Confidence: **99.18%**
656. **`frontend/discourse/app/components/choose-message.gjs`** -> AI Confidence: **99.18%**
657. **`frontend/discourse/app/components/composer-message.gjs`** -> AI Confidence: **99.18%**
658. **`frontend/discourse/app/components/cook-text.gjs`** -> AI Confidence: **99.18%**
659. **`frontend/discourse/app/components/d-document.js`** -> AI Confidence: **99.18%**
660. **`frontend/discourse/app/components/d-segmented-control.gjs`** -> AI Confidence: **99.18%**
661. **`frontend/discourse/app/components/dialog-messages/second-factor-confirm-phrase.gjs`** -> AI Confidence: **99.18%**
662. **`frontend/discourse/app/components/directory-item.gjs`** -> AI Confidence: **99.18%**
663. **`frontend/discourse/app/components/directory-table.gjs`** -> AI Confidence: **99.18%**
664. **`frontend/discourse/app/components/discovery/filter-navigation.gjs`** -> AI Confidence: **99.18%**
665. **`frontend/discourse/app/components/group-list.gjs`** -> AI Confidence: **99.18%**
666. **`frontend/discourse/app/components/group-smtp-email-settings.gjs`** -> AI Confidence: **99.18%**
667. **`frontend/discourse/app/components/hashtag-autocomplete-results.gjs`** -> AI Confidence: **99.18%**
668. **`frontend/discourse/app/components/header/dropdown.gjs`** -> AI Confidence: **99.18%**
669. **`frontend/discourse/app/components/header/header-search.gjs`** -> AI Confidence: **99.18%**
670. **`frontend/discourse/app/components/header/home-logo.gjs`** -> AI Confidence: **99.18%**
671. **`frontend/discourse/app/components/header/topic/participant.gjs`** -> AI Confidence: **99.18%**
672. **`frontend/discourse/app/components/ignored-user-list.gjs`** -> AI Confidence: **99.18%**
673. **`frontend/discourse/app/components/interface-color-selector.gjs`** -> AI Confidence: **99.18%**
674. **`frontend/discourse/app/components/mobile-category-topic.gjs`** -> AI Confidence: **99.18%**
675. **`frontend/discourse/app/components/modal/activation-edit.gjs`** -> AI Confidence: **99.18%**
676. **`frontend/discourse/app/components/modal/change-owner.gjs`** -> AI Confidence: **99.18%**
677. **`frontend/discourse/app/components/modal/change-timestamp.gjs`** -> AI Confidence: **99.18%**
678. **`frontend/discourse/app/components/modal/download-calendar.gjs`** -> AI Confidence: **99.18%**
679. **`frontend/discourse/app/components/modal/ignore-duration-with-username.gjs`** -> AI Confidence: **99.18%**
680. **`frontend/discourse/app/components/modal/revise-and-reject-post-reviewable.gjs`** -> AI Confidence: **99.18%**
681. **`frontend/discourse/app/components/modal/second-factor-add-security-key.gjs`** -> AI Confidence: **99.18%**
682. **`frontend/discourse/app/components/modal/second-factor-add-totp.gjs`** -> AI Confidence: **99.18%**
683. **`frontend/discourse/app/components/modal/second-factor-edit-security-key.gjs`** -> AI Confidence: **99.18%**
684. **`frontend/discourse/app/components/modal/second-factor-edit.gjs`** -> AI Confidence: **99.18%**
685. **`frontend/discourse/app/components/modal/user-status.gjs`** -> AI Confidence: **99.18%**
686. **`frontend/discourse/app/components/post/avatar.gjs`** -> AI Confidence: **99.18%**
687. **`frontend/discourse/app/components/post/filtered-notice.gjs`** -> AI Confidence: **99.18%**
688. **`frontend/discourse/app/components/post/meta-data.gjs`** -> AI Confidence: **99.18%**
689. **`frontend/discourse/app/components/post/notice/custom.gjs`** -> AI Confidence: **99.18%**
690. **`frontend/discourse/app/components/reviewable-post-edits.gjs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `app/services/word_watcher.rb` -> **0.0001%** Exposure
### Exploit Generation Surface
- `config/unicorn_launcher` -> **100.0%** Exposure
- `.skills/discourse-upcoming-changes/scripts/optimize_upcoming_change_image.rb` -> **100.0%** Exposure
- `app/controllers/admin/backups_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/badges_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/themes_controller.rb` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `config/unicorn_launcher` -> **100.0%** Exposure
- `.skills/discourse-upcoming-changes/scripts/optimize_upcoming_change_image.rb` -> **100.0%** Exposure
- `app/controllers/admin/badges_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/web_hooks_controller.rb` -> **100.0%** Exposure
- `app/controllers/tags_controller.rb` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `script/profile_db_generator.rb` -> **99.9751%** Exposure
### Algorithmic DoS Exposure
- `bin/docker/boot_dev` -> **100.0%** Exposure
- `app/controllers/admin/api_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/backups_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/badges_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/themes_controller.rb` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `50` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14794` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `frontend/discourse/admin/controllers/admin-logs/screened-ip-addresses.js` (JAVASCRIPT) -> Cumulative Risk: **1012.75**
- **Archetype:** `file_cluster_4` (Distance: 12.369 IQR)
- **Magnitude:** 165.84 | **LOC:** 127 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `save` (Impact: 35.0), `destroyRecord` (Impact: 18.5), `debouncedShow` (Impact: 5.6)

### 2. `frontend/discourse/app/models/user.js` (JAVASCRIPT) -> Cumulative Risk: **958.46**
- **Archetype:** `file_cluster_4` (Distance: 13.506 IQR)
- **Magnitude:** 1325.44 | **LOC:** 1599 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 44.4%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `findDetails` (Impact: 49.0), `save` (Impact: 46.2), `summary` (Impact: 25.0)

### 3. `frontend/discourse/admin/controllers/edit-category/tabs.js` (JAVASCRIPT) -> Cumulative Risk: **954.95**
- **Archetype:** `file_cluster_0` (Distance: 13.979 IQR)
- **Magnitude:** 468.36 | **LOC:** 430 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 26.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `initFormData` (Impact: 61.6), `saveCategory` (Impact: 31.7), `toggleAdvancedTabs` (Impact: 29.7)

### 4. `frontend/discourse/admin/controllers/admin/dashboard.js` (JAVASCRIPT) -> Cumulative Risk: **948.17**
- **Archetype:** `file_cluster_4` (Distance: 12.797 IQR)
- **Magnitude:** 138.08 | **LOC:** 121 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `fetchDashboard` (Impact: 24.3), `fetchProblems` (Impact: 9.1), `_loadProblems` (Impact: 5.8)

### 5. `frontend/discourse/app/controllers/preferences/email.js` (JAVASCRIPT) -> Cumulative Risk: **940.5**
- **Archetype:** `file_cluster_0` (Distance: 12.466 IQR)
- **Magnitude:** 124.16 | **LOC:** 106 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `saveEmail` (Impact: 30.2), `emailValidation` (Impact: 10.8), `saveButtonText` (Impact: 5.6)

### 6. `frontend/discourse/app/services/pm-topic-tracking-state.js` (JAVASCRIPT) -> Cumulative Risk: **931.55**
- **Archetype:** `file_cluster_17` (Distance: 14.118 IQR)
- **Magnitude:** 396.42 | **LOC:** 286 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_processMessage` (Impact: 56.2), `_shouldDisplayMessageForInbox` (Impact: 11.8), `_isNew` (Impact: 11.0)

### 7. `frontend/discourse/app/controllers/password-reset.js` (JAVASCRIPT) -> Cumulative Risk: **928.55**
- **Archetype:** `file_cluster_0` (Distance: 13.377 IQR)
- **Magnitude:** 265.5 | **LOC:** 180 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `submit` (Impact: 86.3), `initSelectedSecondFactorMethod` (Impact: 13.3), `done` (Impact: 4.7)

### 8. `frontend/discourse/admin/controllers/admin-user/index.js` (JAVASCRIPT) -> Cumulative Risk: **926.0**
- **Archetype:** `file_cluster_4` (Distance: 13.66 IQR)
- **Magnitude:** 1020.76 | **LOC:** 672 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `anonymize` (Impact: 51.5), `grantAdmin` (Impact: 34.9), `saveTrustLevel` (Impact: 29.1)

### 9. `frontend/discourse/app/models/bookmark.js` (JAVASCRIPT) -> Cumulative Risk: **921.86**
- **Archetype:** `file_cluster_0` (Distance: 13.299 IQR)
- **Magnitude:** 262.66 | **LOC:** 221 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `reminderTitle` (Impact: 18.9), `bumpedAtTitle` (Impact: 14.5), `visibleListTags` (Impact: 11.2)

### 10. `frontend/discourse/app/components/date-input.gjs` (JAVASCRIPT) -> Cumulative Risk: **921.35**
- **Archetype:** `file_cluster_4` (Distance: 13.555 IQR)
- **Magnitude:** 334.12 | **LOC:** 203 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `didInsertElement` (Impact: 52.3), `didUpdateAttrs` (Impact: 39.3), `_loadPikadayPicker` (Impact: 11.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `app/controllers/topics_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.935 IQR)
- **Top Global Matches:** file_cluster_8: 10.935, file_cluster_13: 11.374, file_cluster_17: 11.392
- **Magnitude:** 5686.58 | **LOC:** 1590 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (25.9923%), Tech Debt (8.1456%)
**Top Internal Functions/Classes:**
  * `TopicsController` (Impact: 5571.7 | O(2^N) | DB: 151)
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 126`, `args: 25`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `state_mutation: 89`, `planned_debt: 1`
* *Architecture:* `io: 40`, `import: 14`
* *Defense:* `safety: 37`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/custom-proxy/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/pretty-text/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/generic_bulk.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.452 IQR)
- **Top Global Matches:** file_cluster_8: 11.452, file_cluster_7: 12.006, file_cluster_11: 12.141
- **Magnitude:** 4465.1 | **LOC:** 3533 | **CtrlFlow:** 79.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 248
- **Risk Profile:** Cognitive Load (25.211%), Tech Debt (10.65%)
**Top Internal Functions/Classes:**
  * `BulkImport::Generic_[Truncated]` (Impact: 4104.0 | O(N^6) | DB: 248)
  * `Anonymous_Block` (Impact: 10.8 | O(N^3))
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 651`, `structural_boundaries: 167`, `args: 120`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 21`, `state_mutation: 294`, `dead_code: 1`, `planned_debt: 11`, `orphaned_logic: 1`
* *Architecture:* `io: 26`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base, sqlite3, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `config/routes.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.89 IQR)
- **Top Global Matches:** file_cluster_8: 10.89, file_cluster_7: 11.359, file_cluster_15: 11.453
- **Magnitude:** 4352.48 | **LOC:** 1926 | **CtrlFlow:** 99.6% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(N^4) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (29.868%), Tech Debt (11.705%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 1680.5 | O(N^4) | DB: 43)
  * `Anonymous_Block` (Impact: 1049.1 | O(N^4) | DB: 29)
  * `__global_context__` (Impact: 464.1 | O(N^4))
  * `Anonymous_Block` (Impact: 139.7 | O(N^4) | DB: 6)
  * `Anonymous_Block` (Impact: 1.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 840`, `structural_boundaries: 3`, `args: 14`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 141`, `duplicate_logic: 3`
* *Architecture:* `io: 13`, `api: 843`, `import: 2`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/users_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.435 IQR)
- **Top Global Matches:** file_cluster_8: 11.435, file_cluster_2: 11.61, file_cluster_17: 11.657
- **Magnitude:** 3914.44 | **LOC:** 2318 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 258
- **Risk Profile:** Cognitive Load (54.0204%), Tech Debt (12.6414%)
**Top Internal Functions/Classes:**
  * `UsersController` (Impact: 3361.6 | O(N^5) | DB: 258)
    * *Intent:* # frozen_string_literal: true
  * `user_menu_messages` (Impact: 84.0 | O(N^3) | DB: 9)
  * `user_params` (Impact: 63.1 | O(N^2) | DB: 7)
  * `clashing_with_existing_route?_[Truncated` (Impact: 58.5 | O(N^2))
  * `user_menu_bookmarks` (Impact: 40.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 650`, `structural_boundaries: 176`, `args: 42`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 184`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 74`, `import: 15`
* *Defense:* `safety: 54`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rotp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/topic.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.93 IQR)
- **Top Global Matches:** file_cluster_8: 10.93, file_cluster_0: 11.176, file_cluster_7: 11.505
- **Magnitude:** 3642.38 | **LOC:** 2339 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 138
- **Risk Profile:** Cognitive Load (33.1384%), Tech Debt (17.0037%)
**Top Internal Functions/Classes:**
  * `Topic` (Impact: 2229.4 | O(2^N) | DB: 138)
    * *Intent:* # frozen_string_literal: true
  * `self.reset_highest` (Impact: 219.7 | O(N^4) | DB: 27)
    * *Intent:* # If a post is deleted we have to update our highest post counters and last post information
  * `set_or_create_timer` (Impact: 219.5 | O(N^3) | DB: 6)
    * *Intent:* # Valid arguments for the time: # * An integer, which is the number of hours from now to update the ...
  * `update_category_topic_count_by` (Impact: 96.2 | O(N^2) | DB: 31)
  * `self.time_to_first_response` (Impact: 64.5 | O(N^2) | DB: 74)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 191`, `args: 98`, `func_start: 124`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 94`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 119`, `api: 35`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LimitedEdit, HasCustomFields, Forwardable, RateLimiter::OnCreateRecord, Searchable, Trashable, topics, test1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/user.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.963 IQR)
- **Top Global Matches:** file_cluster_8: 10.963, file_cluster_0: 11.2, file_cluster_7: 11.563
- **Magnitude:** 2789.76 | **LOC:** 2360 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 580
- **Risk Profile:** Cognitive Load (21.0213%), Tech Debt (8.1832%)
**Top Internal Functions/Classes:**
  * `User_[Truncated]` (Impact: 2632.3 | O(N^6) | DB: 580)
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 304`, `args: 109`, `func_start: 236`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 120`, `planned_debt: 2`
* *Architecture:* `io: 176`, `api: 1`
* *Defense:* `safety: 18`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasCustomFields, SecondFactorManager, HasDestroyedWebHook, Roleable, HasDeprecatedColumns, Searchable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/base.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.755 IQR)
- **Top Global Matches:** file_cluster_8: 11.755, file_cluster_7: 12.293, file_cluster_13: 12.336
- **Magnitude:** 2426.7 | **LOC:** 2384 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 181
- **Risk Profile:** Cognitive Load (69.2063%), Tech Debt (9.3907%)
**Top Internal Functions/Classes:**
  * `BulkImport::Base_[Truncated]` (Impact: 2005.8 | O(N^4) | DB: 181)
  * `Anonymous_Block` (Impact: 3.6 | O(N^1))
    * *Intent:* # frozen_string_literal: true # Replace (most) bbcode with markdown before creating posts. # This wi...
  * `__global_context__` (Impact: 1.6 | O(N^1))
  * `BulkImport` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 208`, `args: 175`, `func_start: 171`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 29`, `state_mutation: 368`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 6`, `import: 6`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` htmlentities, redcarpet, pg, uploader, environment, ruby-bbcode-to-md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/groups_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.672 IQR)
- **Top Global Matches:** file_cluster_8: 10.672, file_cluster_13: 11.197, file_cluster_2: 11.222
- **Magnitude:** 2265.9 | **LOC:** 1093 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 148
- **Risk Profile:** Cognitive Load (49.7287%), Tech Debt (10.8658%)
**Top Internal Functions/Classes:**
  * `members` (Impact: 1876.9 | O(2^N) | DB: 148)
  * `GroupsController` (Impact: 154.4 | O(N^4) | DB: 32)
    * *Intent:* # frozen_string_literal: true
  * `update` (Impact: 80.1 | O(2^N) | DB: 9)
  * `posts_feed` (Impact: 20.9 | O(N^2) | DB: 8)
  * `posts` (Impact: 11.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 62`, `args: 35`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `orphaned_logic: 3`
* *Architecture:* `io: 52`, `import: 7`
* *Defense:* `safety: 10`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/post_mover.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.306 IQR)
- **Top Global Matches:** file_cluster_8: 10.306, file_cluster_7: 10.94, file_cluster_17: 11.105
- **Magnitude:** 2048.54 | **LOC:** 829 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (29.9869%), Tech Debt (9.239%)
**Top Internal Functions/Classes:**
  * `PostMover` (Impact: 1944.5 | O(2^N) | DB: 112)
    * *Intent:* # frozen_string_literal: true
  * `__global_context__` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 53`, `args: 27`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 17`, `state_mutation: 89`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 23`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/group.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.438 IQR)
- **Top Global Matches:** file_cluster_8: 10.438, file_cluster_0: 10.835, file_cluster_7: 11.093
- **Magnitude:** 1997.92 | **LOC:** 1439 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 134
- **Risk Profile:** Cognitive Load (38.5965%), Tech Debt (90.4954%)
**Top Internal Functions/Classes:**
  * `Group` (Impact: 1276.3 | O(2^N) | DB: 134)
    * *Intent:* # frozen_string_literal: true # NOTE (martin): Remove after 2026.02.0 # and drop columns. self.ignor...
  * `full_url` (Impact: 145.8 | O(N^3) | DB: 31)
  * `bulk_add` (Impact: 60.3 | O(N^4) | DB: 17)
  * `__global_context__` (Impact: 50.8 | O(N^2))
  * `bulk_remove` (Impact: 50.4 | O(N^4) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 115`, `args: 69`, `func_start: 80`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 10`, `state_mutation: 82`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `io: 77`
* *Defense:* `safety: 11`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasCustomFields, HasDestroyedWebHook, non, AnonCacheInvalidator, GlobalPath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/services/post_alerter.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.725 IQR)
- **Top Global Matches:** file_cluster_8: 9.725, file_cluster_7: 10.436, file_cluster_17: 10.532
- **Magnitude:** 1886.98 | **LOC:** 1112 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 137
- **Risk Profile:** Cognitive Load (21.6355%), Tech Debt (13.0975%)
**Top Internal Functions/Classes:**
  * `PostAlerter_[Truncated]` (Impact: 1831.7 | O(N^6) | DB: 137)
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 112`, `args: 79`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `planned_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 41`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` all
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/app/components/reviewable/item.gjs` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.548 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.789 IQR)
- **Top Global Matches:** file_cluster_4: 14.548, file_cluster_0: 14.579, file_cluster_13: 14.654
- **Magnitude:** 1870.28 | **LOC:** 925 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 121
- **Risk Profile:** Cognitive Load (99.1679%), Tech Debt (15.5001%)
**Top Internal Functions/Classes:**
  * `reviewableTypeLabel` (Impact: 1042.6 | O(2^N) | DB: 121)
  * `claimHelp` (Impact: 45.1 | O(N^2) | DB: 7)
  * `reviewableComponent` (Impact: 32.4 | O(N^2) | DB: 5)
  * `displayContextQuestion` (Impact: 23.8 | O(N^2) | DB: 6)
  * `claimEnabled` (Impact: 21.2 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 147`, `args: 42`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `state_mutation: 476`, `dead_code: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 6`, `concurrency: 96`, `import: 42`
* *Defense:* `safety: 89`, `doc: 3`, `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` service, dasherize, horizontal-overflow-nav, get-url, computed, explain-reviewable, ajax-error, concat-class...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/application_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.834 IQR)
- **Top Global Matches:** file_cluster_8: 10.834, file_cluster_0: 11.125, file_cluster_11: 11.41
- **Magnitude:** 1817.44 | **LOC:** 1114 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (38.2241%), Tech Debt (81.621%)
**Top Internal Functions/Classes:**
  * `ApplicationController` (Impact: 807.0 | O(N^6) | DB: 2)
  * `__global_context__` (Impact: 259.2 | O(N^5))
  * `add_early_hint_header` (Impact: 126.1 | O(N^2) | DB: 2)
    * *Intent:* # We don't actually send 103 Early Hint responses from Discourse. However, upstream proxies can be c...
  * `fetch_user_from_params` (Impact: 71.0 | O(N^3) | DB: 3)
  * `redirect_to_login` (Impact: 47.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 141`, `args: 45`, `func_start: 81`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 56`, `dead_code: 1`, `duplicate_logic: 3`, `orphaned_logic: 27`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* `safety: 21`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` current_user, ThemeResolver, Hijack, JsonError, CanonicalURL::ControllerExtensions, ReadOnlyMixin, VaryHeader, CurrentUser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/serializers/post_serializer.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.591 IQR)
- **Top Global Matches:** file_cluster_8: 10.591, file_cluster_7: 11.297, file_cluster_17: 11.298
- **Magnitude:** 1808.32 | **LOC:** 738 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (27.3705%), Tech Debt (8.884%)
**Top Internal Functions/Classes:**
  * `PostSerializer` (Impact: 1775.7 | O(2^N) | DB: 19)
    * *Intent:* # frozen_string_literal: true # To pass in additional information we might need INSTANCE_VARS = %i[ ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 142`, `args: 11`, `func_start: 117`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `io: 4`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` it
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/post.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.326 IQR)
- **Top Global Matches:** file_cluster_8: 10.326, file_cluster_0: 10.761, file_cluster_7: 10.98
- **Magnitude:** 1757.22 | **LOC:** 1308 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (34.6882%), Tech Debt (9.6466%)
**Top Internal Functions/Classes:**
  * `Post` (Impact: 1151.1 | O(2^N) | DB: 97)
  * `self.rebake_old_[Truncated]` (Impact: 458.1 | O(N^3) | DB: 71)
  * `url` (Impact: 18.3 | O(2^N))
  * `unhide!` (Impact: 18.1 | O(N^2) | DB: 4)
  * `self.urls` (Impact: 11.1 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 135`, `args: 67`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 54`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 52`, `api: 7`, `import: 2`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LimitedEdit, HasCustomFields, sha1, RateLimiter::OnCreateRecord, Searchable, Trashable, HasPostUploadReferences, Localizable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/select-kit/components/select-kit.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.241 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.583 IQR)
- **Top Global Matches:** file_cluster_13: 14.241, file_cluster_0: 14.251, file_cluster_8: 14.275
- **Magnitude:** 1755.48 | **LOC:** 1316 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (92.4968%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_searchWrapper` (Impact: 85.7 | O(N^4) | DB: 43)
  * `didReceiveAttrs` (Impact: 62.4 | O(2^N) | DB: 25)
  * `_onChangeWrapper` (Impact: 61.5 | O(N^3) | DB: 18)
  * `updateFloatingUiPosition` (Impact: 59.0 | O(N^4) | DB: 15)
  * `_focusFilter` (Impact: 31.4 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 155`, `args: 111`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `state_mutation: 942`
* *Architecture:* `api: 14`, `concurrency: 36`, `import: 26`
* *Defense:* `safety: 36`, `doc: 3`, `immutability_locks: 49`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.24
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` service, plugin-api, selected-name, component, tracked-tools, selected-choice, select-kit-filter, deprecated...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `app/controllers/session_controller.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.631 IQR)
- **Top Global Matches:** file_cluster_8: 10.631, file_cluster_2: 10.932, file_cluster_13: 11.096
- **Magnitude:** 1606.84 | **LOC:** 939 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (29.9276%), Tech Debt (9.1416%)
**Top Internal Functions/Classes:**
  * `SessionController_[Truncated]` (Impact: 1538.1 | O(N^5) | DB: 53)
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 91`, `args: 20`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `import: 6`
* *Defense:* `safety: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/reviewable.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.715 IQR)
- **Top Global Matches:** file_cluster_8: 9.715, file_cluster_0: 10.37, file_cluster_7: 10.428
- **Magnitude:** 1557.44 | **LOC:** 923 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 127
- **Risk Profile:** Cognitive Load (16.9247%), Tech Debt (9.2653%)
**Top Internal Functions/Classes:**
  * `Reviewable` (Impact: 1507.7 | O(2^N) | DB: 127)
    * *Intent:* # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 89`, `args: 53`, `func_start: 61`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `planned_debt: 2`
* *Architecture:* `io: 37`
* *Defense:* `safety: 7`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` scores
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/discourse_merger.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.44 IQR)
- **Top Global Matches:** file_cluster_8: 10.44, file_cluster_7: 11.07, file_cluster_11: 11.145
- **Magnitude:** 1540.28 | **LOC:** 1233 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (49.2226%), Tech Debt (22.4009%)
**Top Internal Functions/Classes:**
  * `copy_model` (Impact: 825.4 | O(N^4) | DB: 4)
  * `Anonymous_Block` (Impact: 232.0 | O(N^2) | DB: 25)
  * `BulkImport::DiscourseMerger` (Impact: 111.2 | O(N^3) | DB: 43)
  * `fix_user_columns` (Impact: 47.4 | O(N^2) | DB: 14)
  * `copy_uploads` (Impact: 43.1 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 102`, `args: 81`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 13`, `state_mutation: 85`, `dead_code: 2`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 27`, `import: 1`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/app/controllers/topic.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.136 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.66 IQR)
- **Top Global Matches:** file_cluster_4: 14.136, file_cluster_0: 14.276, file_cluster_13: 14.411
- **Magnitude:** 1531.6 | **LOC:** 2067 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (99.447%), Tech Debt (8.3173%)
**Top Internal Functions/Classes:**
  * `onMessage` (Impact: 122.4 | O(N^3) | DB: 18)
  * `retryOnRateLimit` (Impact: 114.4 | O(2^N) | DB: 10)
  * `finishedEditingTopic` (Impact: 29.5 | O(N^3) | DB: 9)
  * `readPosts` (Impact: 24.6 | O(N^2) | DB: 4)
  * `showBottomTopicMap` (Impact: 19.7 | O(N^2) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 178`, `args: 133`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `state_mutation: 591`, `planned_debt: 1`
* *Architecture:* `api: 52`, `concurrency: 188`, `import: 46`
* *Defense:* `safety: 52`, `immutability_locks: 54`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` service, transformer, change-post-notice, computed, proxy, delete-topic-confirm, post, ajax-error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `frontend/discourse/admin/components/admin-backups-logs.gjs` (JAVASCRIPT) | Magnitude: 89.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 60, branch: 14, structural_boundaries: 13
- `frontend/discourse/app/models/site.js` (JAVASCRIPT) | Magnitude: 304.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 251, structural_boundaries: 83, state_mutation: 79, branch: 39
- `frontend/discourse/app/static/dev-tools/block-debug/ghost-block.gjs` (JAVASCRIPT) | Magnitude: 109.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, state_mutation: 71, structural_boundaries: 44, branch: 23
- `frontend/discourse/admin/components/edit-category-panel.gjs` (JAVASCRIPT) | Magnitude: 12.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, decorators: 9, state_mutation: 5
- `frontend/discourse/app/components/modal-container.gjs` (JAVASCRIPT) | Magnitude: 16.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 13, structural_boundaries: 9, decorators: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `bin/docker/reset_db` (SHELL) | Magnitude: 12.66 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, structural_boundaries: 5, safety_bypasses: 3, reflection_metaprogramming: 3
- `script/list_bundled_plugins` (SHELL) | Magnitude: 3.28 | Delta: **0.213 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, io: 4, safety: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frontend/discourse/admin/templates/admin-config/login.gjs` (JAVASCRIPT) | Magnitude: 18.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, decorators: 21, structural_boundaries: 11, ui_framework: 8
- `frontend/discourse/app/helpers/i18n-yes-no.js` (JAVASCRIPT) | Magnitude: 4.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 2, args: 1, func_start: 1
- `frontend/discourse/admin/routes/admin-customize/index.js` (JAVASCRIPT) | Magnitude: 14.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 8, structural_boundaries: 5, branch: 3
- `frontend/discourse/admin/components/site-settings/simple-list.gjs` (JAVASCRIPT) | Magnitude: 19.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 15, decorators: 10, structural_boundaries: 7
- `frontend/discourse/app/components/color-picker.gjs` (JAVASCRIPT) | Magnitude: 28.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 19, structural_boundaries: 11, decorators: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frontend/discourse/app/components/form-template-field/tag-chooser.gjs` (JAVASCRIPT) | Magnitude: 163.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 156, state_mutation: 94, structural_boundaries: 50, branch: 29
- `frontend/discourse/admin/components/admin-reports.gjs` (JAVASCRIPT) | Magnitude: 94.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 35, structural_boundaries: 32, decorators: 20
- `frontend/discourse/app/static/prosemirror/extensions/code-block.js` (JAVASCRIPT) | Magnitude: 101.84 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, structural_boundaries: 34, state_mutation: 30, immutability_locks: 26
- `frontend/discourse/select-kit/components/tag-chooser.js` (JAVASCRIPT) | Magnitude: 241.24 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 154, state_mutation: 119, structural_boundaries: 44, branch: 29
- `frontend/pretty-text/addon/text-replace.js` (JAVASCRIPT) | Magnitude: 98.76 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 46, branch: 21, safety: 11, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `app/controllers/sitemap_controller.rb` (RUBY) | Magnitude: 73.38 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 22, structural_boundaries: 9, branch: 8
- `frontend/discourse/app/instance-initializers/meta-tag-updater.js` (JAVASCRIPT) | Magnitude: 15.44 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, immutability_locks: 7, branch: 6, ui_framework: 5
- `frontend/discourse/scripts/pageview.js` (JAVASCRIPT) | Magnitude: 4.72 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, branch: 6, globals: 6, safety: 4
- `frontend/discourse/scripts/embed-application.js` (JAVASCRIPT) | Magnitude: 57.02 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 27, structural_boundaries: 10, branch: 9
- `frontend/discourse/scripts/print-page.js` (JAVASCRIPT) | Magnitude: 11.56 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 2, args: 1, ui_framework: 1, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `frontend/discourse/app/components/modal/second-factor-edit.gjs` (JAVASCRIPT) | Magnitude: 49.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 26, structural_boundaries: 17, decorators: 14
- `frontend/discourse/admin/components/form-template/form.gjs` (JAVASCRIPT) | Magnitude: 202.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 198, state_mutation: 121, decorators: 47, structural_boundaries: 40
- `frontend/discourse/app/components/modal/flag.gjs` (JAVASCRIPT) | Magnitude: 399.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 259, state_mutation: 205, decorators: 66, structural_boundaries: 55
- `frontend/discourse/admin/components/modal/staff-action-log-change.gjs` (JAVASCRIPT) | Magnitude: 22.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, decorators: 13, concurrency: 12
- `frontend/discourse/app/models/pending-post.js` (JAVASCRIPT) | Magnitude: 18.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, concurrency: 6, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `frontend/discourse/admin/templates/admin-reports/index.gjs` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, branch: 1, api: 1
- `frontend/discourse/app/instance-initializers/localization.js` (JAVASCRIPT) | Magnitude: 15.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, branch: 6, structural_boundaries: 5, state_mutation: 3
- `frontend/discourse/admin/templates/admin-config/color-palettes/index.gjs` (JAVASCRIPT) | Magnitude: 17.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 75, decorators: 42, structural_boundaries: 14, import: 10
- `frontend/discourse/app/templates/account-created/resent.gjs` (JAVASCRIPT) | Magnitude: 16.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, branch: 4, decorators: 4
- `frontend/discourse/app/templates/user-invited.gjs` (JAVASCRIPT) | Magnitude: 16.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, decorators: 14, structural_boundaries: 6, ui_framework: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `script/test_pretty_text.rb` (RUBY) | Magnitude: 4.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: dead_code: 2, indent_spaces: 2, structural_boundaries: 1, args: 1
- `db/migrate/20200428014005_correct_topic_user_bookmarked_boolean.rb` (RUBY) | Magnitude: 0.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 3, func_start: 2, high_risk_execution: 2
- `plugins/discourse-cakeday/db/migrate/20251127125226_delete_old_default_values.rb` (RUBY) | Magnitude: 0.1 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 4, structural_boundaries: 1, class_start: 1, orphaned_logic: 1
- `plugins/discourse-cakeday/db/migrate/20250717093505_persist_cakeday_enabled.rb` (RUBY) | Magnitude: 0.09 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2, structural_boundaries: 1, class_start: 1, orphaned_logic: 1
- `plugins/discourse-cakeday/db/migrate/20250811132217_persist_cakeday_birthday_enabled.rb` (RUBY) | Magnitude: 0.09 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 2, structural_boundaries: 1, class_start: 1, orphaned_logic: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `frontend/discourse/admin/controllers/edit-category/tabs.js` -> Churn: **87.24%** | Cog Load: 94.6383% | Debt: 96.3915%
- `frontend/discourse/app/models/category.js` -> Churn: **74.69%** | Cog Load: 90.7637% | Debt: 13.8325%
- `frontend/discourse/app/models/user.js` -> Churn: **67.05%** | Cog Load: 95.4154% | Debt: 88.3807%
- `frontend/discourse/app/services/composer.js` -> Churn: **63.98%** | Cog Load: 78.2044% | Debt: 71.7853%
- `frontend/discourse/admin/components/upsert-category/general.gjs` -> Churn: **62.34%** | Cog Load: 62.7956% | Debt: 16.059%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `app/services/post_alerter.rb` -> **Jake Goldsborough** (100.0% isolated ownership) | Magnitude: 1886.98
- `app/controllers/session_controller.rb` -> **Penar Musaraj** (100.0% isolated ownership) | Magnitude: 1606.84
- `script/bulk_import/discourse_merger.rb` -> **Alan Guo Xiang Tan** (100.0% isolated ownership) | Magnitude: 1540.28
- `script/bulk_import/uploads_importer.rb` -> **Jarek Radosz** (100.0% isolated ownership) | Magnitude: 1433.4
- `app/models/notification.rb` -> **Jarek Radosz** (100.0% isolated ownership) | Magnitude: 1425.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `frontend/discourse/admin/components/admin-area-settings.gjs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/admin/components/admin-embedding-host-form.gjs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/app/form-kit/components/fk/object.gjs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/admin/components/admin-filtered-site-settings.gjs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/admin/components/site-setting.gjs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/discourse/app/form-kit/components/fk/object.gjs` -> **Severity: 1570.768** (Blast Radius: 46.302 * Doc Risk: 33.9244%)
- `frontend/discourse/app/form-kit/components/fk/collection.gjs` -> **Severity: 828.16** (Blast Radius: 19.561 * Doc Risk: 42.3373%)
- `plugins/discourse-chat-integration/app/helpers/helper.rb` -> **Severity: 477.892** (Blast Radius: 34.317 * Doc Risk: 13.9258%)
- `frontend/discourse/app/helpers/d-icon.js` -> **Severity: 347.033** (Blast Radius: 10.411 * Doc Risk: 33.3333%)
- `frontend/discourse/app/helpers/get-url.js` -> **Severity: 305.765** (Blast Radius: 3.858 * Doc Risk: 79.2547%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
