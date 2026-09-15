# ARCHITECTURAL_BRIEF: discourse
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/discourse/discourse` |
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
| Total Artifacts | 21317 |
| Analyzed Artifacts (Scanned) | 19207 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2110 |
| Total LOC | 1427604 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.1% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5181 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1597 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3681 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 615 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 9018 | 762229 | 47.0% |
| JAVASCRIPT | 5227 | 471562 | 27.2% |
| YAML | 3627 | 107612 | 18.9% |
| CSS | 640 | 65023 | 3.3% |
| HTML | 321 | 7134 | 1.7% |
| JSON | 158 | 12714 | 0.8% |
| PLAINTEXT | 75 | 6 | 0.4% |
| MARKDOWN | 60 | 0 | 0.3% |
| SHELL | 26 | 327 | 0.1% |
| SQLITE | 19 | 656 | 0.1% |
| XML | 17 | 1 | 0.1% |
| CSV | 14 | 58 | 0.1% |
| BINARY_THREAT | 3 | 3 | 0.0% |
| TYPESCRIPT | 2 | 279 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.38; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Declarative / Non-Code 22%, Interface Declarations Files 12%, I/O & Config Routines Files 12%, Large Core Modules 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19065 | 99.3% |
| Unknown | 8 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 129 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2110*

**Composition by Extension & Reason:**
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Zero-Density Threshold (LOC: 60, Signals: 0), 15x Zero-Density Threshold (LOC: 476, Signals: 0)
- `.rb`: 278x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 45 LOC), 5x Excluded (Machine-Generated Source Code Signature: 42 LOC)
- `.png`: 244x Excluded (Explicitly Denied Extension: '.png'), 68x Excluded (Explicitly Denied Extension: '.PNG')
- `.md`: 131x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eml`: 131x Excluded (Unsupported Extension: '.eml')
- `.yaml`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 80, Signals: 0), 1x Zero-Density Threshold (LOC: 72, Signals: 0)
- `.response`: 90x Excluded (Unsupported Extension: '.response')
- `no_extension`: 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.production-sample')
- `.jpg`: 38x Excluded (Explicitly Denied Extension: '.jpg')
- `.mustache`: 37x Excluded (Unsupported Extension: '.mustache')
- `.js`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 5 LOC), 2x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.gif`: 11x Excluded (Explicitly Denied Extension: '.gif')
- `.sample`: 6x Excluded (Unsupported Extension: '.sample'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 314 LOC)
- `.scss`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 8 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.3 | 4.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.1 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 58.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 87.2 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 50.6 | 87.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 389 | 230 | 0 | `frontend/discourse/tests/unit/lib/array-tools-test.js` |
| cleanup | 508 | 255 | 0 | `frontend/discourse/app/modifiers/draggable.js` |
| guards | 23205 | 4775 | 3 | `frontend/discourse/app/services/composer.js` |
| danger | 10954 | 3369 | 1 | `spec/lib/topics_filter_spec.rb` |
| concurrency | 18752 | 2145 | 1 | `frontend/discourse/tests/acceptance/composer-test.js` |
| connectivity | 23342 | 5756 | 2 | `config/routes.rb` |
| io | 25763 | 3884 | 3 | `spec/lib/post_creator_spec.rb` |
| crypto | 2 | 2 | 0 | `frontend/asset-processor/shims.js` |
| ipc | 191 | 99 | 0 | `spec/support/helpers.rb` |
| time | 1280 | 546 | 0 | `migrations/db/intermediate_db_schema/100-base-schema.sql` |
| serialization | 990 | 429 | 0 | `spec/models/web_hook_spec.rb` |
| regex | 3950 | 1143 | 0 | `script/import_scripts/vbulletin3.rb` |
| events | 6808 | 1489 | 0 | `plugins/discourse-subscriptions/assets/javascripts/discourse/components/subscribe-country-select.js` |
| tests | 141659 | 3721 | 16 | `spec/requests/users_controller_spec.rb` |
| docs | 9279 | 1669 | 0 | `config/locales/names.yml` |
| debt | 9487 | 1479 | 0 | `spec/lib/pretty_text_spec.rb` |
| mutation | 217076 | 10665 | 28 | `spec/lib/search_spec.rb` |
| dead_code | 16632 | 6568 | 2 | `app/services/staff_action_logger.rb` |
| credential | 4263 | 185 | 0 | `script/import_scripts/socialcast/test/test_data.rb` |
| threat | 1153 | 561 | 0 | `frontend/discourse/tests/unit/models/post-stream-test.js` |
| ml_ai | 65 | 32 | 0 | `app/models/user_auth_token.rb` |
| ui | 14891 | 2954 | 2 | `app/controllers/users_controller.rb` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spec/lib/post_creator_spec.rb` (Hits: 191)
- `spec/requests/topics_controller_spec.rb` (Hits: 187)
- `spec/requests/users_controller_spec.rb` (Hits: 184)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **component.gjs** (`plugins/styleguide/assets/javascripts/discourse/components/styleguide/component.gjs`) — 1523 inbound connections
2. **service.rb** (`lib/service.rb`) — 1199 inbound connections
3. **d-button.gjs** (`frontend/discourse/app/components/d-button.gjs`) — 595 inbound connections
4. **ajax.js** (`frontend/discourse/app/lib/ajax.js`) — 400 inbound connections
5. **qunit-helpers.js** (`frontend/discourse/tests/helpers/qunit-helpers.js`) — 374 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin-api.gjs** (`frontend/discourse/app/lib/plugin-api.gjs`) — 98 outbound dependencies
2. **qunit-helpers.js** (`frontend/discourse/tests/helpers/qunit-helpers.js`) — 84 outbound dependencies
3. **_index.scss** (`app/assets/stylesheets/common/components/_index.scss`) — 79 outbound dependencies
4. **index.scss** (`plugins/chat/assets/stylesheets/common/index.scss`) — 78 outbound dependencies
5. **_index.scss** (`app/assets/stylesheets/common/base/_index.scss`) — 76 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/requests/users_controller_spec.rb`) -> Impact: **1059.7** | LOC: 8133
- `Anonymous_Block` **(Unclassified)** (@ `spec/lib/guardian_spec.rb`) -> Impact: **814.5** | LOC: 3448
  * *Intent:* # frozen_string_literal: true
- `Anonymous_Block` **(Many-Argument Workhorses)** (@ `spec/requests/topics_controller_spec.rb`) -> Impact: **761.8** | LOC: 7084
  * *Intent:* # coding: utf-8 # frozen_string_literal: true
- `Anonymous_Block` **(Compute Cores)** (@ `spec/requests/admin/users_controller_spec.rb`) -> Impact: **534.0** | LOC: 2931
- `Anonymous_Block` **(Unclassified)** (@ `spec/lib/topics_filter_spec.rb`) -> Impact: **528.6** | LOC: 2850
  * *Intent:* # frozen_string_literal: true
- `Anonymous_Block` **(Unclassified)** (@ `spec/requests/posts_controller_spec.rb`) -> Impact: **480.8** | LOC: 3612
- `Anonymous_Block` **(Compute Cores)** (@ `spec/requests/session_controller_spec.rb`) -> Impact: **466.9** | LOC: 3414
- `Anonymous_Block` **(Unclassified)** (@ `spec/lib/guardian/post_guardian_spec.rb`) -> Impact: **361.7** | LOC: 1345
  * *Intent:* # frozen_string_literal: true
- `extract_email_address_and_name` **(Compute Cores)** (@ `lib/email/receiver.rb`) -> Impact: **323.1** | LOC: 918
- `Anonymous_Block` **(Unclassified)** (@ `plugins/discourse-assign/plugin.rb`) -> Impact: **304.6** | LOC: 1029

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Unclassified**: no dominant structural signature (too small or ambiguous)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib` | 235 | 26809.22 | 45.1% | 35.88% |
| `app/models` | 278 | 20896.72 | 27.55% | 53.16% |
| `spec/requests` | 88 | 17112.9 | 7.9% | 0.0% |
| `script/import_scripts` | 63 | 16719.08 | 62.35% | 30.04% |
| `spec/lib` | 170 | 15912.5 | 8.49% | 0.0% |
| `frontend/discourse/app/lib` | 200 | 15152.36 | 35.49% | 61.79% |
| `frontend/discourse/app/components` | 351 | 14580.48 | 20.89% | 16.76% |
| `spec/models` | 173 | 14522.4 | 8.58% | 0.0% |
| `frontend/discourse/tests/acceptance` | 205 | 12626.12 | 16.73% | 0.0% |
| `app/controllers` | 85 | 11785.36 | 47.6% | 55.04% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/services/base_bookmarkable.rb` -> **100.0%** Exposure
- `app/services/registered_bookmarkable.rb` -> **100.0%** Exposure
- `lib/auth/current_user_provider.rb` -> **100.0%** Exposure
- `lib/freedom_patches/cose_rsapkcs1.rb` -> **100.0%** Exposure
- `lib/request_tracker/rate_limiters/stack.rb` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `config/unicorn_launcher` -> **100.0%** Exposure
- `.skills/discourse-upcoming-changes/scripts/optimize_upcoming_change_image.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/about_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/color_palettes_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/customize_controller.rb` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/services/staff_action_logger.rb` -> **93** Orphaned Functions | **0** Duplicates
- `spec/system/page_objects/pages/admin_customize_themes.rb` -> **54** Orphaned Functions | **0** Duplicates
- `spec/system/page_objects/pages/review.rb` -> **54** Orphaned Functions | **0** Duplicates
- `frontend/discourse/admin/controllers/admin-user/index.js` -> **48** Orphaned Functions | **0** Duplicates
- `app/serializers/post_serializer.rb` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `plugins/discourse-hcaptcha/spec/lib/discourse_h_captcha/create_users_controller_patch_spec.rb` -> **100.0%** Exposure
- `script/import_scripts/socialcast/test/test_data.rb` -> **100.0%** Exposure
- `spec/lib/validators/user_password_validator_spec.rb` -> **100.0%** Exposure
- `spec/requests/finish_installation_controller_spec.rb` -> **100.0%** Exposure
- `spec/system/discourse_connect_provider_spec.rb` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `41` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `30185` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `frontend/discourse/admin/controllers/admin-users-list/show.js` (JAVASCRIPT) -> Cumulative Risk: **782.09**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.70)
- **Magnitude:** 129.54 | **LOC:** 243 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9676%), Concurrency (98.5326%)
- **Heaviest Functions:** `bulkSelectItemToggle` (Compute Cores, Impact: 15.8), `_refreshUsers` (Callbacks & Closures, Impact: 4.2), `columnCount` (Interface Declarations, Impact: 3.6)

### 2. `frontend/discourse/app/models/topic-list.js` (JAVASCRIPT) -> Cumulative Risk: **778.28**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.91)
- **Magnitude:** 222.04 | **LOC:** 251 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9962%)
- **Heaviest Functions:** `topicsFrom` (Many-Argument Workhorses, Impact: 20.0), `loadMore` (I/O & Config Routines, Impact: 11.4), `displayCategoryInList` (Defensive Guards, Impact: 9.5)

### 3. `frontend/discourse/app/controllers/group/index.js` (JAVASCRIPT) -> Cumulative Risk: **772.62**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.23)
- **Magnitude:** 222.74 | **LOC:** 301 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9997%), State Flux (99.929%)
- **Heaviest Functions:** `actOnSelection` (Callbacks & Closures, Impact: 18.2), `actOnGroup` (Callbacks & Closures, Impact: 13.2), `reloadMembers` (Defensive Guards, Impact: 9.4)

### 4. `frontend/discourse/app/lib/ajax.js` (JAVASCRIPT) -> Cumulative Risk: **771.02**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.26)
- **Magnitude:** 361.46 | **LOC:** 258 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8655%), Cognitive Load (94.1438%)
- **Heaviest Functions:** `performAjax` (Many-Argument Workhorses, Impact: 61.4), `ajax` (Defensive Guards, Impact: 52.7), `error` (Defensive Guards, Impact: 48.0)

### 5. `frontend/discourse/app/routes/topic/from-params.js` (JAVASCRIPT) -> Cumulative Risk: **765.44**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.64)
- **Magnitude:** 89.52 | **LOC:** 154 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7201%), Tech Debt (99.2863%)
- **Heaviest Functions:** `setupController` (Many-Argument Workhorses, Impact: 34.0), `model` (Defensive Guards, Impact: 6.9), `afterModel` (State Mutators, Impact: 4.6)

### 6. `frontend/discourse/app/controllers/login.js` (JAVASCRIPT) -> Cumulative Risk: **761.61**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.64)
- **Magnitude:** 248.6 | **LOC:** 324 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9959%), Tech Debt (97.6525%)
- **Heaviest Functions:** `localLogin` (Defensive Guards, Impact: 41.6), `set` (Defensive Guards, Impact: 31.7), `passkeyLogin` (Defensive Guards, Impact: 11.7)

### 7. `frontend/discourse/app/models/post-stream.js` (JAVASCRIPT) -> Cumulative Risk: **758.31**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.55)
- **Magnitude:** 866.82 | **LOC:** 1355 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9966%), State Flux (99.9813%), Tech Debt (91.7508%)
- **Heaviest Functions:** `triggerNewPostsInStream` (Defensive Guards, Impact: 29.0), `loadIntoIdentityMap` (Defensive Guards, Impact: 19.5), `refresh` (Defensive Guards, Impact: 14.3)

### 8. `frontend/discourse/app/models/category.js` (JAVASCRIPT) -> Cumulative Risk: **751.39**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.99)
- **Magnitude:** 640.8 | **LOC:** 992 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7025%), Documentation (98.6301%), Concurrency (94.8975%)
- **Heaviest Functions:** `search` (Defensive Guards, Impact: 48.7), `validCategoryParent` (Defensive Guards, Impact: 30.2), `findBySlug` (Defensive Guards, Impact: 24.5)

### 9. `frontend/discourse/app/services/user-tips.js` (JAVASCRIPT) -> Cumulative Risk: **746.99**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.37)
- **Magnitude:** 124.2 | **LOC:** 155 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9931%), State Flux (99.9868%)
- **Heaviest Functions:** `canSeeUserTip` (Defensive Guards, Impact: 16.8), `markAsSeen` (Defensive Guards, Impact: 15.5), `hideUserTipForever` (Defensive Guards, Impact: 9.5)

### 10. `frontend/discourse/app/adapters/rest.js` (JAVASCRIPT) -> Cumulative Risk: **744.97**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.98)
- **Magnitude:** 110.04 | **LOC:** 143 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8482%), Concurrency (99.7233%)
- **Heaviest Functions:** `appendQueryParams` (Defensive Guards, Impact: 21.1), `storageKey` (Compute Cores, Impact: 6.3), `cacheFind` (State Mutators, Impact: 5.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/custom-proxy/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/pretty-text/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/users_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2439.04 | **LOC:** 8138 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (10.0644%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 1059.7)
  * `create_totp` **(Callbacks & Closures)** (Impact: 3.2)
  * `enabled?` **(Callbacks & Closures)** (Impact: 3.1)
  * `create_and_like_post` **(State Mutators)** (Impact: 2.0)
  * `revoke` **(Tests & Verification)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 113 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 121`, `args: 6`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 21`, `state_mutation: 433`, `unreferenced_by_name: 2`
* *Architecture:* `io: 184`, `api: 558`, `import: 2`
* *Defense:* `safety: 3`, `test: 2161`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ApplicationHelper, I18n, hidden, links, mentionable, other_user, private_group, privileged_user...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/topics_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1962.82 | **LOC:** 7088 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 21.1%
- **Risk Profile:** Cognitive Load (6.9174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 761.8)
    * *Intent:* # coding: utf-8 # frozen_string_literal: true
  * `fabricate_topic` **(Callbacks & Closures)** (Impact: 3.7)
  * `topic_user_post_timings_count` **(Tests & Verification)** (Impact: 3.6)
  * `invite_group` **(State Mutators)** (Impact: 1.9)
  * `extract_post_stream` **(Tests & Verification)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 116 instances
* *Api Near Db Sink:* 1 instances
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 637
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 87`, `args: 5`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 405`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 187`, `api: 440`
* *Defense:* `safety: 4`, `test: 1687`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` I18n, category, ja_category, ja_subcategory, ja_topic, p2, post, pt_category...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/base.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1785.2 | **LOC:** 2384 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (92.7328%), Tech Debt (9.3856%)
**Top Internal Functions/Classes:**
  * `create_records` **(Many-Argument Workhorses)** (Impact: 161.5)
  * `pre_cook` **(Compute Cores)** (Impact: 63.9)
    * *Intent:* # TODO Check if this is still up-to-date # Convert YouTube URLs to lazyYT DOMs before being transfor...
  * `process_raw` **(Compute Cores)** (Impact: 41.3)
  * `process_post` **(Compute Cores)** (Impact: 24.7)
  * `process_chat_channel` **(Compute Cores)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 243 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 215`, `args: 158`, `func_start: 171`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 30`, `state_mutation: 317`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 135`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` environment, uploader, htmlentities, pg, redcarpet, ruby-bbcode-to-md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/email/receiver.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1646.86 | **LOC:** 1683 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.9957%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extract_email_address_and_name` **(Compute Cores)** (Impact: 323.1)
  * `process_internal` **(Compute Cores)** (Impact: 45.5)
  * `forwarded_email_create_topic` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `create_post` **(Compute Cores)** (Impact: 42.3)
  * `create_group_post` **(Many-Argument Workhorses)** (Impact: 41.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 190 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 215`, `args: 61`, `func_start: 90`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 240`
* *Architecture:* `io: 19`, `api: 12`, `import: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 0):` digest
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `script/bulk_import/generic_bulk.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1615.7 | **LOC:** 3533 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (63.8812%), Tech Debt (11.6987%)
**Top Internal Functions/Classes:**
  * `raw_with_placeholders_interpolated` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `import_bookmarks` **(I/O & Config Routines)** (Impact: 20.9)
  * `update_topic_users` **(I/O & Config Routines)** (Impact: 13.5)
  * `import_post_events` **(I/O & Config Routines)** (Impact: 12.7)
  * `import_user_stats` **(I/O & Config Routines)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 294 instances
* *High Risk Execution (weighted view):* 24
* *State Mutation (weighted view):* 1073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 168`, `args: 18`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 25`, `state_mutation: 485`, `dead_code: 1`, `planned_debt: 11`, `unreferenced_by_name: 3`
* *Architecture:* `io: 26`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base, json, sqlite3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/search.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1570.72 | **LOC:** 1682 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.087%), Tech Debt (10.9353%)
**Top Internal Functions/Classes:**
  * `process_advanced_search!` **(Compute Cores)** (Impact: 255.7)
  * `posts_query` **(Many-Argument Workhorses)** (Impact: 70.0)
  * `apply_order` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `execute` **(Compute Cores)** (Impact: 30.7)
    * *Intent:* # Query a term
  * `sort_by_relevance` **(Many-Argument Workhorses)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 643
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 107`, `args: 40`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 231`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 103`, `api: 9`, `import: 1`
* *Defense:* `safety: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cppjieba_rb, that
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/controllers/users_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1440.86 | **LOC:** 2318 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (71.3637%), Tech Debt (13.5591%)
**Top Internal Functions/Classes:**
  * `create` **(I/O & Config Routines)** (Impact: 39.6)
  * `password_reset_update` **(I/O & Config Routines)** (Impact: 26.4)
  * `user_menu_messages` **(I/O & Config Routines)** (Impact: 25.3)
  * `search_users` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* # the search can specify the parameter term or usernames, term will perform the classic user search ...
  * `notification_level` **(I/O & Config Routines)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 258 instances
* *State Mutation (weighted view):* 827
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 178`, `args: 12`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 311`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 77`, `import: 15`
* *Defense:* `safety: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` rotp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/lib/search_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1439.78 | **LOC:** 3684 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (34.8932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 188.0)
    * *Intent:* # frozen_string_literal: true
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 77.3)
  * `Anonymous_Block` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 18.9)
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 870
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 59`, `args: 6`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 510`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 81`, `import: 1`
* *Defense:* `safety: 3`, `test: 961`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` PMs, bot, custom, post, post4, post_in_accented, post_in_topic_with_synonym_target_tag, reply...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/topic.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1407.18 | **LOC:** 2339 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (63.6165%), Tech Debt (7.9837%)
**Top Internal Functions/Classes:**
  * `set_or_create_timer` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* # Valid arguments for the time: # * An integer, which is the number of hours from now to update the ...
  * `similar_to` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `for_digest` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* # Returns hot topics since a date for display in email digest.
  * `changed_to_category` **(Compute Cores)** (Impact: 29.5)
  * `publish_stats_to_clients!` **(Defensive Guards)** (Impact: 27.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 190 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 617
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 194`, `args: 76`, `func_start: 124`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 237`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 119`, `api: 59`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Forwardable, HasCustomFields, LimitedEdit, Localizable, RateLimiter::OnCreateRecord, Searchable, Trashable, test1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/import_scripts/vbulletin3.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1295.7 | **LOC:** 1699 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.9984%), Tech Debt (12.3631%)
**Top Internal Functions/Classes:**
  * `bbcode_list_to_md` **(Compute Cores)** (Impact: 41.9)
  * `postprocess_post_raw` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* # [QUOTE=<username>;<post_id>] raw.gsub!(/\[quote=([^;]+);(\d+)\]/im) do old_username, post_id = $1,...
  * `setup_category_moderator_groups` **(I/O & Config Routines)** (Impact: 21.9)
  * `import_users` **(I/O & Config Routines)** (Impact: 21.5)
  * `import_topics` **(I/O & Config Routines)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 280 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 921
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 90`, `args: 22`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 361`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 25`, `import: 4`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base, bcc, htmlentities, mysql2, php_serialize
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/session_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1294.22 | **LOC:** 3419 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.7187%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 466.9)
  * `get_sso` **(State Mutators)** (Impact: 2.0)
  * `login_with_sso_and_invite` **(Tests & Verification)** (Impact: 1.9)
  * `sso_for_ip_specs` **(Tests & Verification)** (Impact: 1.4)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 38`, `args: 4`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 352`
* *Architecture:* `io: 36`, `api: 248`, `import: 1`
* *Defense:* `safety: 2`, `test: 999`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` I18n, correct_params, rotp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/lib/guardian_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1265.86 | **LOC:** 3451 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (11.8896%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 814.5)
    * *Intent:* # frozen_string_literal: true
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 102 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 10`, `args: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 193`
* *Architecture:* `io: 64`
* *Defense:* `safety: 3`, `test: 1397`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/app/controllers/topic.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1247.64 | **LOC:** 2067 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (75.4407%), Tech Debt (8.0999%)
**Top Internal Functions/Classes:**
  * `onMessage` **(Compute Cores)** (Impact: 46.0)
  * `deletePost` **(Defensive Guards)** (Impact: 35.6)
  * `replyToPost` **(Defensive Guards)** (Impact: 31.5)
    * *Intent:* // Post related methods
  * `retryOnRateLimit` **(Defensive Guards)** (Impact: 26.4)
  * `_openComposerForEdit` **(Defensive Guards)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 67 instances
* *Concurrency (weighted view):* 167
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 294`, `args: 227`, `func_start: 161`, `class_start: 1`
* *Risk/State:* `state_mutation: 127`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 95`, `concurrency: 72`, `import: 46`
* *Defense:* `safety: 127`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` object, controller, object, compat, computed, runloop, service, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/app/services/composer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1244.36 | **LOC:** 1914 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (61.7987%), Tech Debt (8.4117%)
**Top Internal Functions/Classes:**
  * `save` **(Many-Argument Workhorses)** (Impact: 88.6)
  * `open` **(Defensive Guards)** (Impact: 48.3)
    * *Intent:* **/
  * `_setModel` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* // Given a potential instance and options, set the model for this composer.
  * `afterRefresh` **(Defensive Guards)** (Impact: 30.7)
  * `toggleWrap` **(Defensive Guards)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 74 instances
* *Concurrency (weighted view):* 150
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 233`, `args: 134`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 58`, `concurrency: 45`, `import: 38`
* *Defense:* `safety: 176`, `doc: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` object, object, computed, owner, runloop, service, utils, tracking...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/posts_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1195.38 | **LOC:** 3695 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (8.4501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 480.8)
  * `Anonymous_Block` **(Unclassified)** (Impact: 6.3)
  * `Anonymous_Block` **(Unclassified)** (Impact: 4.5)
    * *Intent:* # frozen_string_literal: true
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 80 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 61`, `args: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 13`, `state_mutation: 238`
* *Architecture:* `io: 98`, `api: 247`
* *Defense:* `safety: 1`, `test: 890`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` I18n, array_arg, hash_arg, links, posts, private_post, public_post, regular_post...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/tests/integration/components/d-editor-test.gjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1188.98 | **LOC:** 1511 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `condition` **(Tests & Verification)** (Impact: 6.1)
  * `condition` **(Tests & Verification)** (Impact: 5.0)
  * `condition` **(Tests & Verification)** (Impact: 4.3)
  * `jumpEnd` **(Defensive Guards)** (Impact: 3.3)
  * `testCase` **(Callbacks & Closures)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 150 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 964
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 189`, `args: 99`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 139`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 214`, `import: 15`
* *Defense:* `safety: 4`, `test: 223`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` runloop, test-helpers, discourse-i18n, d-editor, d-menus, toolbar, plugin-api, utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/discourse_merger.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1159.08 | **LOC:** 1233 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.6728%), Tech Debt (63.4844%)
**Top Internal Functions/Classes:**
  * `copy_model` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `copy_solved` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `process_user_action` **(Compute Cores)** (Impact: 20.1)
  * `fix_user_columns` **(I/O & Config Routines)** (Impact: 17.6)
  * `process_raw` **(Many-Argument Workhorses)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 4 instances
* *Amplified Cascading Flux:* 184 instances
* *High Risk Execution (weighted view):* 14
* *Sec Tainted Injection (weighted view):* 4
* *State Mutation (weighted view):* 598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 102`, `args: 42`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 15`, `state_mutation: 230`, `dead_code: 2`, `unreferenced_by_name: 30`
* *Architecture:* `io: 28`, `import: 1`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/models/user.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1153.3 | **LOC:** 2360 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (34.7355%), Tech Debt (7.979%)
**Top Internal Functions/Classes:**
  * `system_avatar_template` **(Compute Cores)** (Impact: 12.2)
  * `update_ip_address!` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `count_by_signup_date` **(Compute Cores)** (Impact: 10.8)
  * `user_fields` **(Compute Cores)** (Impact: 9.5)
  * `letter_avatar_color` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 105 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 312`, `args: 74`, `func_start: 236`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 175`, `planned_debt: 1`
* *Architecture:* `io: 176`, `api: 105`
* *Defense:* `safety: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HasCustomFields, HasDeprecatedColumns, HasDestroyedWebHook, Roleable, Searchable, SecondFactorManager
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/topic_query.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1139.66 | **LOC:** 1401 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9494%), Tech Debt (61.7469%)
**Top Internal Functions/Classes:**
  * `default_results` **(Compute Cores)** (Impact: 53.0)
    * *Intent:* # Create results based on a bunch of default options
  * `remove_muted_categories` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `list_suggested_for` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* # Return a list of suggested topics for a topic # The include_random param was added so plugins can ...
  * `remove_muted_tags` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `filter_by_tags` **(Compute Cores)** (Impact: 26.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 185 instances
* *State Mutation (weighted view):* 604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 95`, `args: 47`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `state_mutation: 234`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `io: 76`
* *Defense:* `safety: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PrivateMessageLists, the, unlisted
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/topic_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1101.64 | **LOC:** 3899 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (9.9851%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 105.9)
    * *Intent:* # frozen_string_literal: true
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 58.6)
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 50.3)
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 40.1)
  * `Anonymous_Block` **(Tests & Verification)** (Impact: 32.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 101 instances
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 95`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 304`
* *Architecture:* `io: 94`
* *Defense:* `safety: 2`, `test: 1051`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` I18n, Time, UserAction::GOT_PRIVATE_MESSAGE, UserAction::NEW_PRIVATE_MESSAGE, UserAction::NEW_TOPIC, a, allowed_group_user, allowed_user...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `frontend/discourse/admin/controllers/edit-category/tabs.js` -> Churn: **87.24%** | Cog Load: 61.8581% | Debt: 86.2812%
- `app/controllers/topics_controller.rb` -> Churn: **78.86%** | Cog Load: 71.2123% | Debt: 17.184%
- `app/controllers/categories_controller.rb` -> Churn: **74.69%** | Cog Load: 67.9265% | Debt: 16.4435%
- `frontend/discourse/app/models/category.js` -> Churn: **74.69%** | Cog Load: 67.7321% | Debt: 0.0%
- `lib/asset_processor.rb` -> Churn: **72.36%** | Cog Load: 82.5327% | Debt: 81.0535%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/email/receiver.rb` -> **Loïc Guitaut** (100.0% isolated ownership) | Magnitude: 1646.86
- `lib/search.rb` -> **Alan Guo Xiang Tan** (100.0% isolated ownership) | Magnitude: 1570.72
- `script/import_scripts/vbulletin3.rb` -> **Loïc Guitaut** (100.0% isolated ownership) | Magnitude: 1295.7
- `spec/requests/session_controller_spec.rb` -> **Penar Musaraj** (100.0% isolated ownership) | Magnitude: 1294.22
- `frontend/discourse/tests/integration/components/d-editor-test.gjs` -> **Renato Atilio** (100.0% isolated ownership) | Magnitude: 1188.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `frontend/discourse/tests/helpers/qunit-helpers.js` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 100.0%)
- `frontend/discourse/app/components/composer-editor.gjs` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/app/components/d-modal.gjs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/discourse/float-kit/components/d-menu.gjs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 96.273%)
- `frontend/discourse/select-kit/components/select-kit.js` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `frontend/discourse/app/lib/computed.js` -> **Severity: 3.326** (Embedded: 0.0483 * Error Risk: 68.9273%)
- `frontend/discourse/app/lib/deprecated.js` -> **Severity: 3.023** (Embedded: 0.054 * Error Risk: 56.0172%)
- `frontend/discourse/app/lib/ajax.js` -> **Severity: 2.866** (Embedded: 0.0305 * Error Risk: 93.9732%)
- `frontend/discourse/app/lib/preload-store.js` -> **Severity: 2.576** (Embedded: 0.0369 * Error Risk: 69.8465%)
- `frontend/discourse/app/lib/source-identifier.js` -> **Severity: 2.508** (Embedded: 0.041 * Error Risk: 61.1312%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/discourse/tests/helpers/qunit-helpers.js` -> **Severity: 893.0** (Blast Radius: 8.93 * Doc Risk: 100.0%)
- `frontend/discourse/app/lib/source-identifier.js` -> **Severity: 669.8** (Blast Radius: 6.698 * Doc Risk: 100.0%)
- `frontend/discourse/app/components/d-button.gjs` -> **Severity: 636.8** (Blast Radius: 6.368 * Doc Risk: 100.0%)
- `frontend/discourse/tests/helpers/component-test.js` -> **Severity: 577.6** (Blast Radius: 5.776 * Doc Risk: 100.0%)
- `frontend/discourse/app/helpers/concat-class.js` -> **Severity: 523.5** (Blast Radius: 5.235 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
