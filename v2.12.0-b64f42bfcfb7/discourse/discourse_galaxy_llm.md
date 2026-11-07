# ARCHITECTURAL_BRIEF: discourse
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/discourse/discourse` |
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
- **Scope:** 18937 analyzed artifact(s), 1424276 LOC.
- **Load-bearing artifact:** `lib/discourse.rb` -- 864 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `frontend/discourse/app/lib/plugin-api.gjs` -- pulls in 93 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 21317 |
| Analyzed Artifacts (Scanned) | 18937 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2380 |
| Total LOC | 1424276 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.8% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6789 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1356 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.8599 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1037 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 9012 | 763617 | 47.6% |
| JAVASCRIPT | 5205 | 473145 | 27.5% |
| YAML | 3425 | 103470 | 18.1% |
| CSS | 611 | 61833 | 3.2% |
| HTML | 322 | 8357 | 1.7% |
| JSON | 154 | 12527 | 0.8% |
| PLAINTEXT | 74 | 6 | 0.4% |
| MARKDOWN | 56 | 0 | 0.3% |
| SHELL | 26 | 327 | 0.1% |
| XML | 17 | 1 | 0.1% |
| CSV | 14 | 58 | 0.1% |
| POSTGRESQL | 10 | 173 | 0.1% |
| SQLITE | 9 | 483 | 0.0% |
| TYPESCRIPT | 2 | 279 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 18926 |
| unknown | unknown | 5 |
| utf-8 | bom | 3 |
| cp1252 | cp1252-fallback | 1 |
| utf-16-be | bom | 1 |
| utf-16-le | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, Declarative / Non-Code 23%, Interface Declarations Files 13%, Large Core Modules (2) 7%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18803 | 99.3% |
| Unknown | 5 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 124 | 0.7% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2380*

**Composition by Extension & Reason:**
- `.yml`: 205x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Zero-Density Threshold (LOC: 60, Signals: 0), 15x Zero-Density Threshold (LOC: 476, Signals: 0)
- `.rb`: 292x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 45 LOC), 5x Excluded (Machine-Generated Source Code Signature: 42 LOC)
- `.png`: 244x Excluded (Explicitly Denied Extension: '.png'), 68x Excluded (Explicitly Denied Extension: '.PNG')
- `.md`: 135x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.eml`: 131x Excluded (Unsupported Extension: '.eml')
- `.yaml`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 80, Signals: 0), 1x Zero-Density Threshold (LOC: 72, Signals: 0)
- `.response`: 90x Excluded (Unsupported Extension: '.response')
- `no_extension`: 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.production-sample')
- `.js`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 136 LOC)
- `.jpg`: 38x Excluded (Explicitly Denied Extension: '.jpg')
- `.mustache`: 37x Excluded (Unsupported Extension: '.mustache')
- `.scss`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 8 exceeds 500 chars)
- `.gjs`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 314 LOC)
- `.json`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1002 LOC)
- `.gif`: 11x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.7 | 4.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 24.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 87.2 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 389 | 230 | 0 | `frontend/discourse/tests/unit/lib/array-tools-test.js` |
| cleanup | 511 | 256 | 0 | `frontend/discourse/app/modifiers/draggable.js` |
| guards | 23124 | 4765 | 3 | `frontend/discourse/app/services/composer.js` |
| danger | 10960 | 3363 | 1 | `spec/lib/topics_filter_spec.rb` |
| concurrency | 18784 | 2155 | 1 | `frontend/discourse/tests/acceptance/composer-test.js` |
| connectivity | 23975 | 5912 | 2 | `config/routes.rb` |
| io | 26366 | 3885 | 3 | `spec/fixtures/onebox/meetup.response.html` |
| crypto | 1 | 1 | 0 | `frontend/discourse/ember-cli-build.js` |
| ipc | 194 | 100 | 0 | `spec/support/helpers.rb` |
| time | 1283 | 547 | 0 | `migrations/db/intermediate_db_schema/100-base-schema.sql` |
| serialization | 990 | 430 | 0 | `spec/models/web_hook_spec.rb` |
| regex | 3980 | 1145 | 0 | `script/import_scripts/vbulletin3.rb` |
| events | 6911 | 1491 | 0 | `plugins/discourse-subscriptions/assets/javascripts/discourse/components/subscribe-country-select.js` |
| tests | 141795 | 3723 | 16 | `spec/requests/users_controller_spec.rb` |
| docs | 8822 | 1645 | 0 | `config/locales/names.yml` |
| debt | 9879 | 1525 | 0 | `spec/lib/pretty_text_spec.rb` |
| mutation | 217773 | 10655 | 28 | `spec/lib/search_spec.rb` |
| dead_code | 16487 | 6403 | 2 | `app/services/staff_action_logger.rb` |
| credential | 2093 | 193 | 0 | `script/import_scripts/socialcast/test/test_data.rb` |
| threat | 866 | 124 | 0 | `plugins/chat/config/locales/client.fa_IR.yml` |
| ml_ai | 65 | 32 | 0 | `app/models/user_auth_token.rb` |
| ui | 14723 | 2926 | 2 | `app/controllers/users_controller.rb` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spec/fixtures/onebox/meetup.response.html` (Hits: 567)
- `spec/lib/post_creator_spec.rb` (Hits: 191)
- `spec/requests/topics_controller_spec.rb` (Hits: 187)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **discourse.rb** (`lib/discourse.rb`) — 864 inbound connections
2. **qunit-helpers.js** (`frontend/discourse/tests/helpers/qunit-helpers.js`) — 378 inbound connections
3. **component-test.js** (`frontend/discourse/tests/helpers/component-test.js`) — 366 inbound connections
4. **base.rb** (`app/jobs/base.rb`) — 364 inbound connections
5. **index.js** (`frontend/discourse/truth-helpers/index.js`) — 351 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin-api.gjs** (`frontend/discourse/app/lib/plugin-api.gjs`) — 93 outbound dependencies
2. **qunit-helpers.js** (`frontend/discourse/tests/helpers/qunit-helpers.js`) — 84 outbound dependencies
3. **_index.scss** (`app/assets/stylesheets/common/components/_index.scss`) — 79 outbound dependencies
4. **index.scss** (`plugins/chat/assets/stylesheets/common/index.scss`) — 78 outbound dependencies
5. **_index.scss** (`app/assets/stylesheets/common/base/_index.scss`) — 76 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `extract_from_outlook` **(Compute Cores)** (@ `lib/email/receiver.rb`) -> Impact: **421.8** | LOC: 1139
  * *Intent:* # Outlook properly identifies the signature and any replied/forwarded email # Use their id to remove them and anything that comes after elided = doc.c...
- `handle` **(Many-Argument Workhorses)** (@ `plugins/discourse-ai/lib/automation/llm_triage.rb`) -> Impact: **278.7** | LOC: 259
- `reply_to` **(Many-Argument Workhorses)** (@ `plugins/discourse-ai/lib/ai_bot/playground.rb`) -> Impact: **258.0** | LOC: 280
- `process_raw` **(Compute Cores)** (@ `script/bulk_import/base.rb`) -> Impact: **212.0** | LOC: 366
- `copy_model` **(Many-Argument Workhorses)** (@ `script/bulk_import/discourse_merger.rb`) -> Impact: **208.2** | LOC: 196
- `perform_completion!` **(Many-Argument Workhorses)** (@ `plugins/discourse-ai/lib/completions/endpoints/base.rb`) -> Impact: **204.4** | LOC: 308
- `preprocess_post_raw` **(Compute Cores)** (@ `script/import_scripts/vbulletin3.rb`) -> Impact: **198.3** | LOC: 290
- `list_for` **(Many-Argument Workhorses)** (@ `app/models/reviewable.rb`) -> Impact: **190.1** | LOC: 136
- `message_for_email` **(Many-Argument Workhorses)** (@ `app/jobs/regular/user_email.rb`) -> Impact: **181.4** | LOC: 149
- `validateArgValue` **(Many-Argument Workhorses)** (@ `frontend/discourse/app/lib/blocks/-internals/validation/args.js`) -> Impact: **168.3** | LOC: 280
  * *Intent:* /** * Validates a single argument value against its schema definition. * */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib` | 235 | 28140.86 | 44.81% | 30.87% |
| `app/models` | 278 | 22569.46 | 27.29% | 46.52% |
| `script/import_scripts` | 63 | 18326.02 | 63.48% | 23.38% |
| `spec/requests` | 88 | 17017.44 | 7.83% | 0.0% |
| `spec/lib` | 170 | 15880.06 | 8.44% | 0.0% |
| `spec/models` | 174 | 14491.28 | 8.58% | 0.0% |
| `frontend/discourse/app/components` | 351 | 14099.38 | 20.77% | 12.25% |
| `frontend/discourse/app/lib` | 200 | 13800.54 | 34.85% | 50.65% |
| `frontend/discourse/tests/acceptance` | 205 | 12555.02 | 5.66% | 0.0% |
| `app/controllers` | 85 | 12237.48 | 47.81% | 46.85% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/services/base_bookmarkable.rb` -> **100.0%** Exposure
- `app/services/registered_bookmarkable.rb` -> **100.0%** Exposure
- `app/services/video_conversion/base_adapter.rb` -> **100.0%** Exposure
- `lib/auth/current_user_provider.rb` -> **100.0%** Exposure
- `lib/service/base/steps_helpers.rb` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `config/unicorn_launcher` -> **100.0%** Exposure
- `.skills/discourse-upcoming-changes/scripts/optimize_upcoming_change_image.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/about_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/color_palettes_controller.rb` -> **100.0%** Exposure
- `app/controllers/admin/config/customize_controller.rb` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/services/staff_action_logger.rb` -> **93** Orphaned Functions | **0** Duplicates
- `frontend/discourse/app/lib/plugin-api.gjs` -> **85** Orphaned Functions | **0** Duplicates
- `spec/system/page_objects/pages/admin_customize_themes.rb` -> **54** Orphaned Functions | **0** Duplicates
- `spec/system/page_objects/pages/review.rb` -> **54** Orphaned Functions | **0** Duplicates
- `frontend/discourse/admin/controllers/admin-user/index.js` -> **48** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `config/routes.rb` -> **100.0%** Exposure
- `plugins/discourse-hcaptcha/spec/lib/discourse_h_captcha/create_users_controller_patch_spec.rb` -> **100.0%** Exposure
- `script/import_scripts/socialcast/test/test_data.rb` -> **100.0%** Exposure
- `spec/lib/validators/user_password_validator_spec.rb` -> **100.0%** Exposure
- `spec/mailers/group_smtp_mailer_spec.rb` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `164` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `29955` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/custom-proxy/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/pretty-text/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/users_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.087)
- **Top Global Matches:** file_cluster_10: 7.087, file_cluster_11: 8.23, file_cluster_15: 8.859
- **Magnitude:** 2433.04 | **LOC:** 8138 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (71.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.8%), Guard Balance (formerly Safety Score) (40.1%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_and_like_post` **(Parameter Forwarders)** (Impact: 2.0)
  * `revoke` **(Parameter Forwarders)** (Impact: 1.9)
  * `honeypot_magic` **(Parameter Forwarders)** (Impact: 1.8)
  * `post_user` **(Parameter Forwarders)** (Impact: 1.6)
  * `description_for_user` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 657
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 521`, `structural_boundaries: 121`, `args: 6`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 21`, `state_mutation: 433`, `duplicate_logic: 8`, `unreferenced_by_name: 2`
* *Architecture:* `io: 184`, `api: 558`, `import: 2`
* *Defense:* `safety: 3`, `test: 2161`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` ApplicationHelper, I18n, hidden, links, mentionable, other_user, private_group, privileged_user...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/requests/topics_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.835)
- **Top Global Matches:** file_cluster_10: 6.835, file_cluster_15: 8.964, file_cluster_2: 9.119
- **Magnitude:** 1959.42 | **LOC:** 7088 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 21.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (87.2%), Guard Balance (formerly Safety Score) (41.4%), Connectivity (formerly Api Exposure) (12.7%), Complexity Load (formerly Cognitive Load) (6.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fabricate_topic` **(Parameter Forwarders)** (Impact: 2.0)
  * `topic_user_post_timings_count` **(Callbacks & Closures)** (Impact: 1.9)
  * `invite_group` **(Parameter Forwarders)** (Impact: 1.9)
  * `extract_post_stream` **(Callbacks & Closures)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 637
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 87`, `args: 5`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 405`, `planned_debt: 1`
* *Architecture:* `io: 187`, `api: 440`
* *Defense:* `safety: 4`, `test: 1687`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` I18n, category, ja_category, ja_subcategory, ja_topic, p2, post, pt_category...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/generic_bulk.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.984)
- **Top Global Matches:** file_cluster_4: 7.984, file_cluster_15: 8.665, file_cluster_16: 9.697
- **Magnitude:** 1861.8 | **LOC:** 3533 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (63.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `raw_with_placeholders_interpolated` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `poll_bbcode` **(Compute Cores)** (Impact: 25.8)
  * `import_post_events` **(I/O & Config Routines)** (Impact: 20.6)
  * `event_bbcode` **(Compute Cores)** (Impact: 19.6)
  * `import_permalinks` **(I/O & Config Routines)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 297 instances
* *High Risk Execution (weighted view):* 22
* *State Mutation (weighted view):* 1079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 168`, `args: 18`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 25`, `state_mutation: 485`, `planned_debt: 11`, `unreferenced_by_name: 3`
* *Architecture:* `io: 26`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` base, json, sqlite3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/base.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.511)
- **Top Global Matches:** file_cluster_4: 8.511, file_cluster_15: 8.628, file_cluster_16: 10.321
- **Magnitude:** 1836.56 | **LOC:** 2384 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **6**; blast radius 0.109; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_raw` **(Compute Cores)** (Impact: 212.0)
  * `pre_cook` **(Compute Cores)** (Impact: 69.6)
    * *Intent:* # TODO Check if this is still up-to-date # Convert YouTube URLs to lazyYT DOMs before being transfor...
  * `process_user` **(Compute Cores)** (Impact: 39.8)
  * `process_category` **(Compute Cores)** (Impact: 35.3)
  * `process_group` **(Compute Cores)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 242 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 215`, `args: 158`, `func_start: 171`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 30`, `state_mutation: 317`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 116`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.109
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.00048
  * `Imports (Out-Degree: 7):` environment, uploader, htmlentities, pg, redcarpet, ruby-bbcode-to-md
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/email/receiver.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.443)
- **Top Global Matches:** file_cluster_4: 6.443, file_cluster_6: 11.375, file_cluster_15: 11.522
- **Magnitude:** 1734.22 | **LOC:** 1683 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **1**; blast radius 0.262; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_from_outlook` **(Compute Cores)** (Impact: 421.8)
    * *Intent:* # Outlook properly identifies the signature and any replied/forwarded email # Use their id to remove...
  * `process_destination` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `add_attachments` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `process_internal` **(I/O & Config Routines)** (Impact: 44.5)
  * `select_body` **(I/O & Config Routines)** (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 215`, `args: 61`, `func_start: 90`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 240`
* *Architecture:* `io: 19`, `api: 3`, `import: 1`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.00408
  * `Imports (Out-Degree: 20):` digest
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `app/models/topic.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.52)
- **Top Global Matches:** file_cluster_15: 7.52, file_cluster_4: 8.098, file_cluster_11: 8.688
- **Magnitude:** 1545.46 | **LOC:** 2339 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **7**; blast radius 1.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (87.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_or_create_timer` **(Many-Argument Workhorses)** (Impact: 86.6)
    * *Intent:* # Valid arguments for the time: # * An integer, which is the number of hours from now to update the ...
  * `for_digest` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* # Returns hot topics since a date for display in email digest.
  * `similar_to` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `changed_to_category` **(Compute Cores)** (Impact: 38.1)
  * `invite` **(Many-Argument Workhorses)** (Impact: 27.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 191 instances
* *State Mutation (weighted view):* 619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 194`, `args: 76`, `func_start: 124`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 237`, `planned_debt: 1`
* *Architecture:* `io: 119`, `api: 66`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.139
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.041513
  * `Imports (Out-Degree: 35):` Forwardable, HasCustomFields, LimitedEdit, Localizable, RateLimiter::OnCreateRecord, Searchable, Trashable
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `script/import_scripts/vbulletin3.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.806)
- **Top Global Matches:** file_cluster_4: 7.806, file_cluster_6: 9.746, file_cluster_9: 13.93
- **Magnitude:** 1519.52 | **LOC:** 1699 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (71.3%), Debt Markers (formerly Tech Debt) (11.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `preprocess_post_raw` **(Compute Cores)** (Impact: 198.3)
  * `apply_special_category_permissions` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `apply_category_permissions` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `import_attachments` **(I/O & Config Routines)** (Impact: 29.0)
  * `import_profile_picture` **(Many-Argument Workhorses)** (Impact: 18.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 283 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 929
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 90`, `args: 22`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 363`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 25`, `import: 4`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.1e-05
  * `Imports (Out-Degree: 7):` base, htmlentities, mysql2, php_serialize
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/controllers/users_controller.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.1)
- **Top Global Matches:** file_cluster_4: 7.1, file_cluster_6: 11.169, file_cluster_15: 11.8
- **Magnitude:** 1499.36 | **LOC:** 2318 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.4%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(I/O & Config Routines)** (Impact: 50.6)
  * `search_users` **(I/O & Config Routines)** (Impact: 28.1)
    * *Intent:* # the search can specify the parameter term or usernames, term will perform the classic user search ...
  * `password_reset_update` **(I/O & Config Routines)** (Impact: 26.4)
  * `show` **(Defensive Guards)** (Impact: 21.7)
  * `user_menu_messages` **(I/O & Config Routines)** (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 823
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 178`, `args: 12`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 311`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 77`, `import: 15`
* *Defense:* `safety: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` rotp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/lib/search_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_10: 6.975, file_cluster_15: 8.616, file_cluster_2: 8.698
- **Magnitude:** 1426.78 | **LOC:** 3684 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.4%), Complexity Load (formerly Cognitive Load) (21.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_post` **(Parameter Forwarders)** (Impact: 4.5)
  * `create_pm` **(Callbacks & Closures)** (Impact: 4.1)
  * `search_with_bookmarks` **(Interface Declarations)** (Impact: 2.1)
  * `result` **(Parameter Forwarders)** (Impact: 1.6)
  * `search` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 878
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 60`, `args: 6`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 510`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 82`, `import: 1`
* *Defense:* `safety: 6`, `test: 961`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` PMs, custom, post, post4, post_in_accented, post_in_topic_with_synonym_target_tag, reply, superfluous...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/search.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.543)
- **Top Global Matches:** file_cluster_4: 6.543, file_cluster_6: 11.068, file_cluster_15: 11.578
- **Magnitude:** 1415.26 | **LOC:** 1682 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **1**; blast radius 1.84; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `posts_query` **(Many-Argument Workhorses)** (Impact: 104.0)
  * `apply_order` **(Many-Argument Workhorses)** (Impact: 66.1)
  * `process_advanced_search!` **(Compute Cores)** (Impact: 46.6)
  * `execute` **(Compute Cores)** (Impact: 32.1)
    * *Intent:* # Query a term
  * `sort_by_relevance` **(Many-Argument Workhorses)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 637
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 108`, `args: 40`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 231`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `io: 104`, `api: 8`, `import: 1`
* *Defense:* `safety: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.84
  * `Choke Point (Betweenness):` 0.000165 | `Ripple Effect (Closeness):` 0.0493
  * `Imports (Out-Degree: 8):` cppjieba_rb
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `spec/requests/session_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.69)
- **Top Global Matches:** file_cluster_10: 7.69, file_cluster_11: 8.685, file_cluster_2: 8.756
- **Magnitude:** 1286.22 | **LOC:** 3419 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (42.1%), Connectivity (formerly Api Exposure) (13.6%), Complexity Load (formerly Cognitive Load) (11.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_sso` **(I/O & Config Routines)** (Impact: 2.0)
  * `login_with_sso_and_invite` **(Parameter Forwarders)** (Impact: 1.9)
  * `sso_for_ip_specs` **(I/O & Config Routines)** (Impact: 1.4)
  * `post_login` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 508
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 38`, `args: 4`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 352`
* *Architecture:* `io: 36`, `api: 248`, `import: 1`
* *Defense:* `safety: 2`, `test: 999`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` I18n, correct_params, rotp
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/lib/guardian_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.921)
- **Top Global Matches:** file_cluster_10: 5.921, file_cluster_2: 7.572, file_cluster_17: 8.926
- **Magnitude:** 1265.86 | **LOC:** 3451 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.2%), Guard Balance (formerly Safety Score) (33.4%), Complexity Load (formerly Cognitive Load) (11.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 10`, `args: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 193`
* *Architecture:* `io: 64`
* *Defense:* `safety: 3`, `test: 1397`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/topic_query.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.415)
- **Top Global Matches:** file_cluster_4: 6.415, file_cluster_15: 9.75, file_cluster_16: 10.965
- **Magnitude:** 1256.7 | **LOC:** 1401 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **1**; blast radius 0.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_results` **(Compute Cores)** (Impact: 104.0)
    * *Intent:* # Create results based on a bunch of default options
  * `list_suggested_for` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* # Return a list of suggested topics for a topic # The include_random param was added so plugins can ...
  * `remove_muted_categories` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `create_list` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `remove_muted_tags` **(Many-Argument Workhorses)** (Impact: 31.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 95`, `args: 47`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `state_mutation: 234`, `planned_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `io: 76`
* *Defense:* `safety: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.031698
  * `Imports (Out-Degree: 11):` PrivateMessageLists
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `app/models/user.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.61)
- **Top Global Matches:** file_cluster_15: 6.61, file_cluster_11: 6.829, file_cluster_10: 7.586
- **Magnitude:** 1255.02 | **LOC:** 2360 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **109** in-repo importer(s); it depends on **6**; blast radius 2.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.6%), Guard Balance (formerly Safety Score) (59.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_posts_read!` **(Defensive Guards)** (Impact: 14.9)
  * `count_by_signup_date` **(Compute Cores)** (Impact: 14.8)
  * `update_ip_address!` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `username_available?` **(Compute Cores)** (Impact: 10.8)
  * `posted_too_much_in_topic?` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* # Does not apply to staff and non-new members... return false if staff? || (trust_level != TrustLeve...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 312`, `structural_boundaries: 312`, `args: 74`, `func_start: 236`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 175`, `planned_debt: 1`
* *Architecture:* `io: 176`, `api: 110`
* *Defense:* `safety: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.77
  * `Choke Point (Betweenness):` 0.000282 | `Ripple Effect (Closeness):` 0.043274
  * `Imports (Out-Degree: 34):` HasCustomFields, HasDeprecatedColumns, HasDestroyedWebHook, Roleable, Searchable, SecondFactorManager
  * `Imported By (In-Degree: 109):` (Excluded from Brief to save tokens)

### `frontend/discourse/app/controllers/topic.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.032)
- **Top Global Matches:** file_cluster_15: 8.032, file_cluster_10: 8.264, file_cluster_11: 8.905
- **Magnitude:** 1217.64 | **LOC:** 2067 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **46**; blast radius 0.126; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.4%), Mutation Surface (formerly State Flux) (97.1%), Complexity Load (formerly Cognitive Load) (73.6%), Connectivity (formerly Api Exposure) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onMessage` **(Compute Cores)** (Impact: 46.0)
  * `deletePost` **(Defensive Guards)** (Impact: 35.6)
  * `replyToPost` **(Defensive Guards)** (Impact: 31.5)
    * *Intent:* // Post related methods
  * `retryOnRateLimit` **(Defensive Guards)** (Impact: 26.4)
  * `_openComposerForEdit` **(Defensive Guards)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 66 instances
* *Concurrency (weighted view):* 157
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 294`, `args: 227`, `func_start: 161`, `class_start: 1`
* *Risk/State:* `state_mutation: 127`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 93`, `concurrency: 72`, `import: 46`
* *Defense:* `safety: 127`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.126
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.010697
  * `Imports (Out-Degree: 27):` object, controller, object, compat, computed, runloop, service, utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `frontend/discourse/app/services/composer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_4: 7.912, file_cluster_15: 9.0, file_cluster_10: 9.935
- **Magnitude:** 1208.36 | **LOC:** 1914 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **38**; blast radius 0.035; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Mutation Surface (formerly State Flux) (99.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.0%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 97.6048% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save` **(Many-Argument Workhorses)** (Impact: 88.6)
  * `open` **(Defensive Guards)** (Impact: 46.9)
    * *Intent:* **/
  * `_setModel` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* // Given a potential instance and options, set the model for this composer.
  * `afterRefresh` **(Defensive Guards)** (Impact: 30.7)
  * `toggleWrap` **(Defensive Guards)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 150
* *State Mutation (weighted view):* 272
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 233`, `args: 134`, `func_start: 108`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`, `planned_debt: 2`
* *Architecture:* `api: 58`, `concurrency: 45`, `import: 38`
* *Defense:* `safety: 176`, `doc: 3`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000102
  * `Imports (Out-Degree: 23):` object, object, computed, owner, runloop, service, utils, tracking...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spec/requests/posts_controller_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.37)
- **Top Global Matches:** file_cluster_10: 5.37, file_cluster_2: 6.73, file_cluster_17: 8.088
- **Magnitude:** 1195.38 | **LOC:** 3695 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.9%), Guard Balance (formerly Safety Score) (43.9%), Connectivity (formerly Api Exposure) (12.8%), Complexity Load (formerly Cognitive Load) (8.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 61`, `args: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 13`, `state_mutation: 238`
* *Architecture:* `io: 98`, `api: 247`
* *Defense:* `safety: 1`, `test: 890`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` I18n, array_arg, hash_arg, links, posts, private_post, public_post, regular_post...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `script/bulk_import/discourse_merger.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.222)
- **Top Global Matches:** file_cluster_15: 8.222, file_cluster_4: 8.722, file_cluster_10: 9.072
- **Magnitude:** 1186.78 | **LOC:** 1233 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.9%), Guard Balance (formerly Safety Score) (80.3%), Debt Markers (formerly Tech Debt) (56.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_model` **(Many-Argument Workhorses)** (Impact: 208.2)
  * `copy_model_user_search_data` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `process_raw` **(Compute Cores)** (Impact: 16.5)
  * `copy_categories_first_child` **(I/O & Config Routines)** (Impact: 13.8)
    * *Intent:* # Only for categories with one parent, no granparent puts "merging categories..." columns = Category...
  * `copy_categories_with_no_parent` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* # Categories with no parent are copied first so child categories can reference the parent puts "merg...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 191 instances
* *High Risk Execution (weighted view):* 15
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 102`, `args: 42`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 16`, `state_mutation: 230`, `unreferenced_by_name: 28`
* *Architecture:* `io: 28`, `import: 1`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/discourse/tests/integration/components/d-editor-test.gjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.719)
- **Top Global Matches:** file_cluster_12: 7.719, file_cluster_10: 8.866, file_cluster_7: 9.164
- **Magnitude:** 1159.08 | **LOC:** 1511 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jumpEnd` **(Defensive Guards)** (Impact: 3.3)
  * `testCase` **(Callbacks & Closures)** (Impact: 2.8)
  * `composerTestCase` **(Annotated & Test Methods)** (Impact: 2.4)
  * `indentSelection` **(Parameter Forwarders)** (Impact: 2.0)
  * `triggerEnter` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* // Smart list functionality relies on beforeinput, which QUnit does not send with // `typeIn` synthe...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 150 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 964
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 189`, `args: 99`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 139`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 214`, `import: 15`
* *Defense:* `safety: 4`, `test: 223`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` runloop, test-helpers, discourse-i18n, d-editor, d-menus, toolbar, plugin-api, utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spec/models/topic_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.463)
- **Top Global Matches:** file_cluster_10: 6.463, file_cluster_2: 8.364, file_cluster_15: 9.105
- **Magnitude:** 1099.64 | **LOC:** 3899 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.2%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (9.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expect_the_right_notification_to_be_created` **(Parameter Forwarders)** (Impact: 2.4)
  * `set_state!` **(Parameter Forwarders)** (Impact: 2.3)
  * `build_topic_with_title` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 504
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 95`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 304`
* *Architecture:* `io: 94`
* *Defense:* `safety: 2`, `test: 1051`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` I18n, Time, UserAction::GOT_PRIVATE_MESSAGE, UserAction::NEW_PRIVATE_MESSAGE, UserAction::NEW_TOPIC, a, allowed_group_user, allowed_user...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `plugins/discourse-topic-voting/assets/javascripts/discourse/components/vote-box.gjs` (JAVASCRIPT) | Magnitude: 46.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, decorators: 21, structural_boundaries: 20, state_mutation: 14
- `spec/integration/remote_theme_color_schemes_spec.rb` (RUBY) | Magnitude: 26.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 166, test: 26, state_mutation: 13, core_var_decl: 13
- `app/assets/stylesheets/common/base/topic-admin-menu.scss` (CSS) | Magnitude: 0.81 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 53, class_start: 7, closures: 7, branch: 3
- `spec/models/topic_featured_users_spec.rb` (RUBY) | Magnitude: 7.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 29, test: 10, state_mutation: 5, core_var_decl: 5
- `plugins/chat/app/services/chat/add_users_to_channel.rb` (RUBY) | Magnitude: 46.56 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 16, closures: 11, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `plugins/discourse-adplugin/admin/assets/javascripts/admin/components/house-ads-setting.gjs` (JAVASCRIPT) | Magnitude: 23.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 20, decorators: 15, core_var_decl: 10
- `plugins/discourse-ai/app/models/llm_quota.rb` (RUBY) | Magnitude: 35.28 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 12, decorators: 8, branch: 6
- `app/jobs/onceoff/onceoff.rb` (RUBY) | Magnitude: 32.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 14, branch: 6, func_start: 6
- `frontend/discourse/admin/components/admin-reports.gjs` (JAVASCRIPT) | Magnitude: 54.84 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 32, decorators: 20, core_var_decl: 17
- `plugins/discourse-assign/assets/javascripts/discourse/initializers/extend-for-assigns.js` (JAVASCRIPT) | Magnitude: 45.79 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 599, structural_boundaries: 138, branch: 105, args: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `frontend/discourse/app/lib/blocks/-internals/decorator.js` (JAVASCRIPT) | Magnitude: 75.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, branch: 26, core_var_decl: 25, structural_boundaries: 22
- `app/models/base_timer.rb` (RUBY) | Magnitude: 37.16 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 17, func_start: 11, branch: 8
- `frontend/discourse/tests/acceptance/topic-admin-menu-test.js` (JAVASCRIPT) | Magnitude: 25.4 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 18, test: 15, concurrency: 11
- `plugins/chat/app/services/chat/update_channel_status.rb` (RUBY) | Magnitude: 8.4 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, doc: 4, args: 3
- `frontend/discourse/tests/integration/components/admin-config-area-card-section-test.gjs` (JAVASCRIPT) | Magnitude: 24.44 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 66, test: 16, structural_boundaries: 9, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frontend/discourse/admin/routes/admin/dashboard-reports.js` (JAVASCRIPT) | Magnitude: 9.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, branch: 4, args: 3
- `frontend/discourse/app/routes/discovery.js` (JAVASCRIPT) | Magnitude: 30.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 45, branch: 14, structural_boundaries: 9, decorators: 8
- `frontend/discourse/app/components/user-avatar.gjs` (JAVASCRIPT) | Magnitude: 20.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 35, decorators: 17, structural_boundaries: 13, branch: 7
- `plugins/chat/assets/javascripts/discourse/components/chat-side-panel.gjs` (JAVASCRIPT) | Magnitude: 23.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 16, branch: 10, decorators: 9
- `frontend/discourse/app/components/sidebar/section-link.gjs` (JAVASCRIPT) | Magnitude: 92.42 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 261, decorators: 89, structural_boundaries: 63, branch: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `script/silence_successful_output` (SHELL) | Magnitude: 12.96 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: io: 6, structural_boundaries: 4, args: 4, debug_prints: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `frontend/discourse/app/components/bookmark-menu.gjs` (JAVASCRIPT) | Magnitude: 176.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 59, decorators: 41, branch: 36
- `spec/system/page_objects/pages/topic.rb` (RUBY) | Magnitude: 257.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 344, structural_boundaries: 92, func_start: 85, api: 68
- `frontend/discourse/admin/components/edit-category-settings.gjs` (JAVASCRIPT) | Magnitude: 60.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 525, decorators: 96, structural_boundaries: 94, core_var_decl: 90
- `plugins/chat/spec/plugin_helper.rb` (RUBY) | Magnitude: 79.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 16, state_mutation: 13, func_start: 11
- `plugins/discourse-ai/admin/assets/javascripts/discourse/components/ai-embedding-editor.gjs` (JAVASCRIPT) | Magnitude: 197.72 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 525, decorators: 125, structural_boundaries: 96, branch: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `frontend/discourse/app/lib/uppy/composer-upload.js` (JAVASCRIPT) | Magnitude: 234.86 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 496, structural_boundaries: 72, branch: 60, args: 50
- `frontend/discourse/app/static/prosemirror/extensions/link-toolbar.js` (JAVASCRIPT) | Magnitude: 122.58 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 300, structural_boundaries: 49, args: 35, func_start: 34
- `frontend/discourse/app/lib/dag.js` (JAVASCRIPT) | Magnitude: 113.8 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 135, branch: 30, structural_boundaries: 24, args: 15
- `plugins/discourse-ai/assets/javascripts/discourse/lib/smooth-streamer.gjs` (JAVASCRIPT) | Magnitude: 89.9 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, state_mutation: 17, branch: 10, doc: 10
- `frontend/discourse/app/lib/uppy/uppy-upload.js` (JAVASCRIPT) | Magnitude: 221.34 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 450, structural_boundaries: 69, branch: 58, args: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frontend/discourse/app/blocks/conditions/index.js` (JAVASCRIPT) | Magnitude: 20.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, branch: 5
- `plugins/chat/assets/stylesheets/common/index.scss` (CSS) | Magnitude: 0.83 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 78
- `frontend/discourse/app/static/prosemirror/extensions/register-default.js` (JAVASCRIPT) | Magnitude: 17.14 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 29, import: 27, indent_spaces: 26, branch: 1
- `frontend/discourse/truth-helpers/index.js` (JAVASCRIPT) | Magnitude: 26.22 | Delta: **0.167** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 11, structural_boundaries: 11, api: 11, import: 11
- `lib/auth.rb` (RUBY) | Magnitude: 2.0 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, import: 11, indent_spaces: 2, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `plugins/discourse-ai/spec/system/ai_bot/tool_spec.rb` (RUBY) | Magnitude: 15.06 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 51, test: 15, state_mutation: 10, io: 7
- `app/assets/stylesheets/common/base/dialog.scss` (CSS) | Magnitude: 0.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, class_start: 14, ui_framework: 6, branch: 3
- `plugins/discourse-ai/spec/fabricators/ai_tool_fabricator.rb` (RUBY) | Magnitude: 3.56 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 6, branch: 2, closures: 1, debug_prints: 1
- `app/views/dev_mode/index.html.erb` (HTML) | Magnitude: 15.28 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, ssr_boundaries: 6, structural_boundaries: 4, args: 1
- `plugins/discourse-calendar/lib/tasks/javascript.rake` (RUBY) | Magnitude: 34.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, core_var_decl: 10, state_mutation: 9, design_snake_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/models/reviewable_flagged_post.rb` (RUBY) | Magnitude: 212.54 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 290, branch: 46, state_mutation: 34, structural_boundaries: 33
- `app/services/user_updater.rb` (RUBY) | Magnitude: 293.44 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 315, branch: 94, state_mutation: 48, core_var_decl: 26
- `plugins/chat/assets/javascripts/discourse/lib/fabricators.js` (JAVASCRIPT) | Magnitude: 9.43 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 117, branch: 45, structural_boundaries: 19, safety: 16
- `frontend/discourse/admin/services/site-setting-change-tracker.js` (JAVASCRIPT) | Magnitude: 140.92 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 49, args: 30, branch: 27
- `script/bulk_import/base.rb` (RUBY) | Magnitude: 1836.56 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1931, branch: 398, state_mutation: 317, structural_boundaries: 215

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `plugins/discourse-ai/lib/guardian_extensions.rb` (RUBY) | Magnitude: 86.24 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 46, branch: 40, func_start: 8
- `plugins/discourse-ai/lib/completions/prompt_messages_builder.rb` (RUBY) | Magnitude: 822.82 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 444, state_mutation: 170, branch: 142, core_var_decl: 77

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `frontend/discourse/tests/integration/components/post/menu/buttons/flag-test.gjs` (JAVASCRIPT) | Magnitude: 34.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 19, args: 14, closures: 14
- `app/serializers/sidebar_tag_serializer.rb` (RUBY) | Magnitude: 19.34 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, branch: 5, structural_boundaries: 5, func_start: 4
- `spec/lib/service_spec.rb` (RUBY) | Magnitude: 43.8 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 153, test: 50, closures: 46, structural_boundaries: 15
- `frontend/discourse/app/components/topic-list/featured-topic.gjs` (JAVASCRIPT) | Magnitude: 9.34 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, decorators: 16, structural_boundaries: 10, import: 6
- `lib/service/base/steps_helpers.rb` (RUBY) | Magnitude: 35.44 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 12, state_mutation: 11, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `plugins/discourse-ai/lib/agents/artifact_update_strategies/full.rb` (RUBY) | Magnitude: 83.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 121, branch: 18, state_mutation: 15, core_var_decl: 14
- `app/jobs/onceoff/migrate_custom_emojis.rb` (RUBY) | Magnitude: 20.62 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 29, io: 8, branch: 6, structural_boundaries: 5
- `frontend/discourse/app/lib/handle-descriptor.js` (JAVASCRIPT) | Magnitude: 77.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 20, branch: 14, state_mutation: 12
- `plugins/discourse-rewind/app/services/discourse_rewind/action/favorite_gifs.rb` (RUBY) | Magnitude: 61.88 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 132, branch: 29, core_var_decl: 14, structural_boundaries: 13
- `plugins/discourse-narrative-bot/app/controllers/discourse_narrative_bot/certificates_controller.rb` (RUBY) | Magnitude: 25.42 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 29, branch: 6, state_mutation: 5, core_var_decl: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `frontend/discourse/admin/controllers/edit-category/tabs.js` -> Churn: **87.24%** | Cog Load: 59.7608% | Debt: 83.6475%
- `app/controllers/topics_controller.rb` -> Churn: **78.86%** | Cog Load: 71.2123% | Debt: 25.9032%
- `app/controllers/categories_controller.rb` -> Churn: **74.69%** | Cog Load: 67.9265% | Debt: 17.565%
- `frontend/discourse/app/lib/plugin-api.gjs` -> Churn: **74.69%** | Cog Load: 6.4687% | Debt: 99.9986%
- `frontend/discourse/app/models/category.js` -> Churn: **74.69%** | Cog Load: 67.2276% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/email/receiver.rb` -> **Loïc Guitaut** (100.0% isolated ownership) | Magnitude: 1734.22
- `script/import_scripts/vbulletin3.rb` -> **Loïc Guitaut** (100.0% isolated ownership) | Magnitude: 1519.52
- `lib/search.rb` -> **Alan Guo Xiang Tan** (100.0% isolated ownership) | Magnitude: 1415.26
- `spec/requests/session_controller_spec.rb` -> **Penar Musaraj** (100.0% isolated ownership) | Magnitude: 1286.22
- `script/bulk_import/discourse_merger.rb` -> **Alan Guo Xiang Tan** (100.0% isolated ownership) | Magnitude: 1186.78

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/discourse.rb` -> **Severity: 0.21** (Bridge: 0.0021 * Flux: 99.9997%)
- `lib/plugin/instance.rb` -> **Severity: 0.103** (Bridge: 0.001 * Flux: 99.9919%)
- `lib/onebox/helpers.rb` -> **Severity: 0.073** (Bridge: 0.0007 * Flux: 100.0%)
- `lib/file_helper.rb` -> **Severity: 0.07** (Bridge: 0.0007 * Flux: 100.0%)
- `lib/final_destination.rb` -> **Severity: 0.07** (Bridge: 0.0007 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/discourse.rb` -> **Severity: 4.908** (Embedded: 0.0731 * Error Risk: 67.1536%)
- `frontend/discourse/app/lib/get-url.js` -> **Severity: 4.894** (Embedded: 0.0751 * Error Risk: 65.1836%)
- `frontend/discourse/app/lib/avatar-utils.js` -> **Severity: 4.089** (Embedded: 0.0667 * Error Risk: 61.2619%)
- `lib/pretty_text.rb` -> **Severity: 4.036** (Embedded: 0.0526 * Error Risk: 76.6639%)
- `app/models/global_setting.rb` -> **Severity: 3.803** (Embedded: 0.0508 * Error Risk: 74.8398%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/discourse.rb` -> **Severity: 3196.805** (Blast Radius: 32.155 * Doc Risk: 99.4186%)
- `frontend/discourse/app/lib/environment.js` -> **Severity: 1069.334** (Blast Radius: 16.04 * Doc Risk: 66.6667%)
- `frontend/discourse/app/lib/source-identifier.js` -> **Severity: 823.1** (Blast Radius: 8.231 * Doc Risk: 100.0%)
- `frontend/discourse/app/lib/get-url.js` -> **Severity: 735.1** (Blast Radius: 7.351 * Doc Risk: 100.0%)
- `frontend/discourse/tests/helpers/qunit-helpers.js` -> **Severity: 697.4** (Blast Radius: 6.974 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 8152 literal sites + 56 sites through wrappers = 8208
- **`panics_and_aborts`:** 4032 literal sites + 72 sites through wrappers = 4104

- `print_warning` (function, debug_prints, primitive): 15 call sites in 1 files -- `script/import_scripts/mylittleforum.rb`
- `raise_error` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `app/services/theme_settings_migrations_runner.rb`
- `log_error` (function, debug_prints, primitive): 7 call sites in 1 files -- `script/import_scripts/phpbb3/importer.rb`
- `validate_error` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `lib/site_settings/validations.rb`
- `output_row` (function, debug_prints, primitive): 6 call sites in 1 files -- `lib/turbo_tests/json_rows_formatter.rb`
- `raise_error` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `plugins/discourse-post-voting/app/controllers/post_voting/votes_controller.rb`
- `raise_error` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `plugins/discourse-assign/lib/random_assign_utils.rb`
- `cleanup` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `frontend/discourse/app/lib/uppy-chunked-upload.js`
- `load_json` (function, debug_prints, primitive): 4 call sites in 1 files -- `lib/onebox/engine/github_pull_request_onebox.rb`
- `load_json` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `lib/onebox/engine/github_pull_request_onebox.rb`
- `notImplemented` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `frontend/discourse/app/lib/sidebar/base-custom-sidebar-panel.js`
- `print_warning` (function, debug_prints, primitive): 4 call sites in 1 files -- `script/import_scripts/ipboard.rb`
*(+32 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 232575 call pairs -- scoped 13.4%, unique 0.4%, ambiguous 43.3%, external 43.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| ruby | 195221 | 11.1% | 0.5% | 44.6% | 43.8% |
| javascript | 37216 | 25.2% | 0.1% | 36.2% | 38.6% |
| typescript | 63 | 23.8% | 0.0% | 19.0% | 57.1% |
| shell | 56 | 16.1% | 0.0% | 0.0% | 83.9% |
| html | 14 | 0.0% | 0.0% | 0.0% | 100.0% |
| postgresql | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
