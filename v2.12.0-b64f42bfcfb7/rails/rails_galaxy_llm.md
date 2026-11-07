# ARCHITECTURAL_BRIEF: rails
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rails/rails.git` |
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
- **Scope:** 4389 analyzed artifact(s), 398048 LOC.
- **Load-bearing artifact:** `activesupport/test/abstract_unit.rb` -- 168 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `activerecord/lib/active_record/base.rb` -- pulls in 57 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `actionview/test/template/date_helper_test.rb` at magnitude 2774.98 (structural weight, not risk).
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
| Total Artifacts | 4901 |
| Analyzed Artifacts (Scanned) | 4389 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 512 |
| Total LOC | 398048 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 89.6% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7007 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1419 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 7.207 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 377 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 3453 | 375442 | 78.7% |
| HTML | 468 | 4212 | 10.7% |
| YAML | 189 | 2891 | 4.3% |
| MARKDOWN | 120 | 0 | 2.7% |
| PLAINTEXT | 59 | 0 | 1.3% |
| JAVASCRIPT | 58 | 13225 | 1.3% |
| XML | 20 | 15 | 0.5% |
| CSS | 18 | 2176 | 0.4% |
| JSON | 2 | 16 | 0.0% |
| SQLITE | 1 | 43 | 0.0% |
| DOCKERFILE | 1 | 28 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 4389 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Interface Declarations Files 17%, Large Core Modules (3) 12%, Parameter Forwarders Files 11%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4195 | 95.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 179 | 4.1% |
| Static: Minified & Vendor Opaque Mass | 15 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 512*

**Composition by Extension & Reason:**
- `.tt`: 152x Excluded (Unsupported Extension: '.tt'), 12x Unsupported Format (.tt)
- `.erb`: 86x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `no_extension`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 12x Unsupported Format (.undeterminable), 3x Excluded (Unsupported Extension: 'no_extension')
- `.rb`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC), 1x Excluded (Machine-Generated Source Code Signature: 79 LOC)
- `.png`: 30x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 5x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 54, Signals: 0)
- `.dump`: 16x Excluded (Unsupported Extension: '.dump')
- `.jpg`: 14x Excluded (Explicitly Denied Extension: '.jpg')
- `.rdoc`: 9x Excluded (Unsupported Extension: '.rdoc')
- `.gz`: 8x Excluded (Explicitly Denied Extension: '.gz')
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2830 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 4027 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3335 LOC)
- `.mp4`: 6x Excluded (Explicitly Denied Extension: '.mp4')
- `.ico`: 5x Excluded (Explicitly Denied Extension: '.ico')
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 7 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.2 | 3.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 35.4 | 49.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 99.0 | 8.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.6 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 96.5 | 2.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.0 | 87.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 435 | 190 | 0 | `activesupport/test/core_ext/date_and_time_behavior.rb` |
| cleanup | 95 | 34 | 0 | `guides/assets/javascripts/@hotwired--turbo.js` |
| guards | 6577 | 1716 | 4 | `guides/assets/javascripts/@hotwired--turbo.js` |
| danger | 5935 | 1268 | 3 | `guides/assets/javascripts/@hotwired--turbo.js` |
| concurrency | 1382 | 249 | 0 | `guides/assets/javascripts/@hotwired--turbo.js` |
| connectivity | 11893 | 1744 | 5 | `actionpack/test/dispatch/routing_test.rb` |
| io | 14382 | 1362 | 5 | `activerecord/test/cases/associations/has_many_associations_test.rb` |
| crypto | 2 | 2 | 0 | `activestorage/app/assets/javascripts/activestorage.esm.js` |
| ipc | 111 | 42 | 0 | `Rakefile` |
| time | 719 | 191 | 0 | `activesupport/test/time_travel_test.rb` |
| serialization | 184 | 102 | 0 | `actionpack/test/controller/test_case_test.rb` |
| regex | 965 | 365 | 0 | `activerecord/lib/active_record/connection_adapters/abstract_mysql_adapter.rb` |
| events | 1058 | 218 | 0 | `activesupport/test/notifications_test.rb` |
| tests | 54642 | 1386 | 28 | `actionpack/test/dispatch/routing_test.rb` |
| docs | 2915 | 1104 | 2 | `guides/source/documents.yaml` |
| debt | 3804 | 649 | 1 | `actionview/test/template/tag_helper_test.rb` |
| mutation | 95171 | 2839 | 49 | `actionview/test/template/date_helper_test.rb` |
| dead_code | 19880 | 1575 | 9 | `actionview/test/template/form_helper_test.rb` |
| credential | 55 | 34 | 0 | `actionmailbox/test/controllers/ingresses/mailgun/inbound_emails_controller_test.rb` |
| threat | 24 | 14 | 0 | `activesupport/lib/active_support/core_ext/digest/uuid.rb` |
| ml_ai | 329 | 80 | 0 | `activemodel/test/cases/type/decimal_test.rb` |
| ui | 4287 | 430 | 0 | `actionview/test/template/render_test.rb` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `activerecord/test/cases/associations/has_many_associations_test.rb` (Hits: 380)
- `activerecord/test/cases/associations/belongs_to_associations_test.rb` (Hits: 283)
- `activerecord/test/cases/finder_test.rb` (Hits: 277)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **abstract_unit.rb** (`activesupport/test/abstract_unit.rb`) — 168 inbound connections
2. **fake_record.rb** (`activerecord/test/cases/arel/support/fake_record.rb`) — 137 inbound connections
3. **abstract_unit.rb** (`railties/test/isolation/abstract_unit.rb`) — 99 inbound connections
4. **base.rb** (`actionview/lib/action_view/helpers/tags/base.rb`) — 97 inbound connections
5. **abstract_unit.rb** (`actionpack/test/abstract_unit.rb`) — 80 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **base.rb** (`activerecord/lib/active_record/base.rb`) — 57 outbound dependencies
2. **helpers.rb** (`actionview/lib/action_view/helpers.rb`) — 52 outbound dependencies
3. **has_many_associations_test.rb** (`activerecord/test/cases/associations/has_many_associations_test.rb`) — 51 outbound dependencies
4. **nodes.rb** (`activerecord/lib/arel/nodes.rb`) — 50 outbound dependencies
5. **has_many_through_associations_test.rb** (`activerecord/test/cases/associations/has_many_through_associations_test.rb`) — 47 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `uuid_column_and_sequence_sql` **(Compute Cores)** (@ `activerecord/lib/active_record/connection_adapters/postgresql/schema_statements.rb`) -> Impact: **242.7** | LOC: 865
- `table_options` **(Compute Cores)** (@ `activerecord/lib/active_record/connection_adapters/abstract_mysql_adapter.rb`) -> Impact: **203.1** | LOC: 499
- `verify_request_for_forgery_protection` **(Many-Argument Workhorses)** (@ `actionpack/lib/action_controller/metal/request_forgery_protection.rb`) -> Impact: **149.1** | LOC: 384
  * *Intent:* # The actual before_action that is used to verify the request to protect from forgery. # Don't override this directly. Provide your own forgery protec...
- `derive_fk_query_constraints` **(Compute Cores)** (@ `activerecord/lib/active_record/reflection.rb`) -> Impact: **140.9** | LOC: 471
- `match` **(Many-Argument Workhorses)** (@ `actionpack/lib/action_dispatch/routing/mapper.rb`) -> Impact: **134.6** | LOC: 52
  * *Intent:* # Matches a URL pattern to one or more routes. For more information, see # [match](rdoc-ref:Base#match). # # match 'path', to: 'controller#action', vi...
- `Anonymous_Block_[Truncated]` **(Compute Cores)** (@ `Rakefile`) -> Impact: **133.8** | LOC: 216
- `generate` **(Many-Argument Workhorses)** (@ `activesupport/lib/active_support/delegation.rb`) -> Impact: **129.1** | LOC: 128
- `store_nested_param` **(Many-Argument Workhorses)** (@ `actionpack/lib/action_dispatch/http/param_builder.rb`) -> Impact: **126.7** | LOC: 85
- `load_defaults` **(Many-Argument Workhorses)** (@ `railties/lib/rails/application/configuration.rb`) -> Impact: **108.8** | LOC: 310
  * *Intent:* # Loads default configuration values for a target version. This includes # defaults for versions prior to the target version. See the # {configuration...
- `test_button_to_with_content_exfiltration_prevention` **(Compute Cores)** (@ `actionview/test/template/url_helper_test.rb`) -> Impact: **90.1** | LOC: 982

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `activerecord/test/cases` | 134 | 18532.46 | 12.7% | 0.0% |
| `activerecord/lib/active_record` | 77 | 9318.82 | 36.7% | 40.69% |
| `actionview/test/template` | 41 | 8122.32 | 10.17% | 0.0% |
| `actionpack/test/controller` | 53 | 6420.34 | 6.86% | 0.0% |
| `activesupport/lib/active_support` | 87 | 6036.72 | 31.29% | 13.69% |
| `activerecord/test/cases/associations` | 24 | 5940.9 | 17.87% | 0.0% |
| `activesupport/test` | 80 | 5837.68 | 13.87% | 0.0% |
| `actionpack/test/dispatch` | 38 | 5222.44 | 11.53% | 0.0% |
| `actionview/lib/action_view/helpers` | 25 | 4459.24 | 46.68% | 2.03% |
| `activerecord/lib/active_record/connection_adapters` | 14 | 3843.14 | 45.21% | 45.54% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `actionpack/lib/action_dispatch/http/rack_cache.rb` -> **100.0%** Exposure
- `activemodel/lib/active_model/lint.rb` -> **100.0%** Exposure
- `activerecord/lib/active_record/associations/singular_association.rb` -> **100.0%** Exposure
- `activerecord/lib/active_record/connection_adapters/pool_manager.rb` -> **100.0%** Exposure
- `activerecord/lib/arel/nodes/window.rb` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Rakefile` -> **100.0%** Exposure
- `actioncable/actioncable.gemspec` -> **100.0%** Exposure
- `actioncable/lib/action_cable/connection/stream.rb` -> **100.0%** Exposure
- `actioncable/lib/action_cable/server/base.rb` -> **100.0%** Exposure
- `actioncable/lib/action_cable/test_helper.rb` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `actionview/test/template/form_helper_test.rb` -> **349** Orphaned Functions | **12** Duplicates
- `actionpack/test/dispatch/routing_test.rb` -> **254** Orphaned Functions | **29** Duplicates
- `activerecord/test/cases/associations/has_many_associations_test.rb` -> **273** Orphaned Functions | **0** Duplicates
- `activerecord/test/cases/finder_test.rb` -> **249** Orphaned Functions | **0** Duplicates
- `activerecord/test/cases/relations_test.rb` -> **243** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `actionmailbox/test/controllers/ingresses/mailgun/inbound_emails_controller_test.rb` -> **100.0%** Exposure
- `actionpack/test/controller/http_token_authentication_test.rb` -> **99.9998%** Exposure
- `activesupport/test/env_configuration_test.rb` -> **99.9995%** Exposure
- `activestorage/config/routes.rb` -> **99.5195%** Exposure
- `activerecord/test/cases/secure_token_test.rb` -> **97.2852%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `8359` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `actionview/test/template/date_helper_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.094)
- **Top Global Matches:** file_cluster_10: 7.094, file_cluster_11: 7.513, file_cluster_2: 8.128
- **Magnitude:** 2774.98 | **LOC:** 3711 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (41.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_datetime_select_with_seconds` **(I/O & Config Routines)** (Impact: 8.5)
  * `test_datetime_select_invalid_order` **(I/O & Config Routines)** (Impact: 7.3)
  * `test_datetime_select_with_default_value_as_time` **(I/O & Config Routines)** (Impact: 7.3)
  * `test_datetime_select_with_default_value_as_hash` **(I/O & Config Routines)** (Impact: 7.3)
  * `test_datetime_select_discard_year` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 280 instances
* *State Mutation (weighted view):* 2221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 371`, `args: 1`, `func_start: 238`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1661`, `unreferenced_by_name: 236`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`, `test: 362`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` abstract_unit, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actionpack/lib/action_dispatch/routing/mapper.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.602)
- **Top Global Matches:** file_cluster_15: 7.602, file_cluster_12: 7.956, file_cluster_4: 8.131
- **Magnitude:** 2046.52 | **LOC:** 2547 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 0.309; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 96.8553% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 134.6)
    * *Intent:* # Matches a URL pattern to one or more routes. For more information, see # [match](rdoc-ref:Base#mat...
  * `mount` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* # # mount SomeRackApp, at: "some_route" # # For options, see `match`, as `mount` uses it internally....
  * `map_match` **(Many-Argument Workhorses)** (Impact: 76.5)
  * `scope` **(Many-Argument Workhorses)** (Impact: 58.7)
    * *Intent:* # # route /posts (without the prefix /admin) to Admin::PostsController # scope module: "admin" do # ...
  * `get` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* # Define a route that only recognizes HTTP GET. For supported arguments, see # [match](rdoc-ref:Base...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 150 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 503
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 267`, `args: 111`, `func_start: 152`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 7`, `state_mutation: 203`, `dead_code: 8`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 23`
* *Architecture:* `io: 30`, `api: 10`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 9`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.309
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.002528
  * `Imports (Out-Degree: 10):` Base, Concerns, CustomUrls, Enumerable, HttpHelpers, Module, Redirection, Resources...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `actionpack/test/dispatch/routing_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.505)
- **Top Global Matches:** file_cluster_10: 7.505, file_cluster_11: 9.074, file_cluster_15: 9.543
- **Magnitude:** 1733.52 | **LOC:** 5314 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.1%), Connectivity (formerly Api Exposure) (16.0%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `method_missing` **(Compute Cores)** (Impact: 5.5)
  * `call` **(Compute Cores)** (Impact: 4.6)
  * `test_non_greedy_regexp` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_resource_does_not_modify_passed_options` **(I/O & Config Routines)** (Impact: 3.2)
  * `test_resources_does_not_modify_passed_options` **(I/O & Config Routines)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 434`, `args: 24`, `func_start: 307`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 85`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 29`, `unreferenced_by_name: 254`
* *Architecture:* `io: 118`, `api: 1011`, `import: 4`
* *Defense:* `safety: 4`, `test: 1059`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ActionDispatch::Routing::Redirection, DefaultScopeRoutes, Routes, abstract_unit, rotation_configuration, fake_controllers, erb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/lib/arel/visitors/to_sql.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.919)
- **Top Global Matches:** file_cluster_15: 5.919, file_cluster_10: 7.929, file_cluster_16: 8.156
- **Magnitude:** 1248.48 | **LOC:** 1026 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 0.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.6%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.5305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_Arel_Nodes_BoundSqlLiteral` **(Compute Cores)** (Impact: 37.3)
  * `infix_value_with_paren` **(Compute Cores)** (Impact: 16.5)
  * `prepare_update_statement` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* # The default strategy for an UPDATE with joins is to use a subquery. This doesn't work # on MySQL (...
  * `visit_Arel_Nodes_InsertStatement` **(Compute Cores)** (Impact: 11.5)
  * `visit_Arel_Nodes_HomogeneousIn` **(Compute Cores)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 182 instances
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 166`, `args: 115`, `func_start: 120`, `class_start: 4`
* *Risk/State:* `state_mutation: 263`, `fragile_debt: 1`
* *Architecture:* `api: 92`
* *Defense:* `doc: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.032333
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `actionview/test/template/form_helper_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.402)
- **Top Global Matches:** file_cluster_10: 7.402, file_cluster_11: 8.868, file_cluster_15: 9.555
- **Magnitude:** 1240.72 | **LOC:** 4301 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.9%), Complexity Load (formerly Cognitive Load) (10.7%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `form_text` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `hidden_fields` **(Defensive Guards)** (Impact: 7.8)
  * `url_for` **(Compute Cores)** (Impact: 6.2)
  * `test_label` **(I/O & Config Routines)** (Impact: 5.6)
  * `test_form_for_with_collection_checkboxes_with_custom_builder_block_does_not_leak_the_template` **(Callbacks & Closures)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 433`, `args: 5`, `func_start: 357`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 369`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 349`
* *Architecture:* `io: 46`, `api: 6`, `import: 3`
* *Defense:* `safety: 12`, `test: 419`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` RenderERBUtils, Routes, abstract_unit, with, fake_models
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/test/cases/associations/has_many_associations_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.669)
- **Top Global Matches:** file_cluster_10: 7.669, file_cluster_11: 8.634, file_cluster_13: 9.515
- **Magnitude:** 1187.2 | **LOC:** 3359 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **51**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.9%), Complexity Load (formerly Cognitive Load) (29.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_async_load_has_many` **(Callbacks & Closures)** (Impact: 3.9)
  * `test_calling_first_nth_or_last_on_existing_record_with_build_should_load_association` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_create_with_bang_on_has_many_when_parent_is_new_raises` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_regular_create_on_has_many_when_parent_is_new_raises` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_create_with_bang_on_habtm_when_parent_is_new_raises` **(Callbacks & Closures)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 54 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 365`, `args: 3`, `func_start: 276`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 619`, `fragile_debt: 1`, `unreferenced_by_name: 273`
* *Architecture:* `io: 380`, `import: 55`
* *Defense:* `safety: 10`, `test: 779`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` DeprecatedAssociationsTestHelpers, WaitForAsyncTestHelper, helper, destroyed = companies(:first_firm).clients_of_firm.destroy_all
    assert_equal clients.sort_by(&:id), destroyed.sort_by(&:id)
    assert destroyed.all?(&:frozen?), author, bulb, car...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/lib/active_record/connection_adapters/postgresql/schema_statements.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.071)
- **Top Global Matches:** file_cluster_15: 8.071, file_cluster_4: 8.344, file_cluster_10: 9.348
- **Magnitude:** 1110.4 | **LOC:** 1346 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.127; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 91.8919% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uuid_column_and_sequence_sql` **(Compute Cores)** (Impact: 242.7)
  * `type_to_sql` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* # Maps logical Rails types to PostgreSQL-specific data types.
  * `indexes` **(Compute Cores)** (Impact: 40.3)
    * *Intent:* # Returns an array of indexes for the given table.
  * `create_database` **(Compute Cores)** (Impact: 22.3)
    * *Intent:* # Create a new PostgreSQL database. Options include <tt>:owner</tt>, <tt>:template</tt>, # <tt>:enco...
  * `new_column_from_field` **(Many-Argument Workhorses)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 164`, `args: 91`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 169`
* *Architecture:* `io: 13`, `api: 28`
* *Defense:* `safety: 6`, `doc: 7`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000227
  * `Imports (Out-Degree: 2):` the
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `activerecord/lib/active_record/relation/query_methods.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.247)
- **Top Global Matches:** file_cluster_15: 7.247, file_cluster_12: 7.911, file_cluster_10: 8.021
- **Magnitude:** 1030.52 | **LOC:** 2291 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 63.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_where_clause` **(Compute Cores)** (Impact: 33.2)
  * `arel_column` **(Compute Cores)** (Impact: 23.6)
  * `build_join_buckets` **(I/O & Config Routines)** (Impact: 21.8)
  * `reverse_sql_order` **(Compute Cores)** (Impact: 20.1)
  * `column_references` **(Compute Cores)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 178`, `args: 112`, `func_start: 130`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 47`, `state_mutation: 148`, `dead_code: 11`, `unreferenced_by_name: 10`
* *Architecture:* `io: 16`, `import: 4`
* *Defense:* `safety: 8`, `doc: 49`, `test: 3`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ActiveModel::ForbiddenAttributesProtection, from_clause, query_attribute, where_clause, wrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/test/cases/relations_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.308)
- **Top Global Matches:** file_cluster_10: 8.308, file_cluster_11: 9.347, file_cluster_15: 10.201
- **Magnitude:** 914.32 | **LOC:** 2785 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (23.8%), Concurrency Surface (formerly Concurrency) (23.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_finding_with_sanitized_order` **(I/O & Config Routines)** (Impact: 6.7)
  * `test_finding_with_arel_sql_order` **(I/O & Config Routines)** (Impact: 6.7)
  * `test_find_all_using_where_with_relation_with_bound_values` **(I/O & Config Routines)** (Impact: 5.0)
  * `test_find_all_using_where_with_relation` **(I/O & Config Routines)** (Impact: 4.8)
  * `test_multivalue_where` **(I/O & Config Routines)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 290`, `args: 3`, `func_start: 247`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 435`, `planned_debt: 2`, `unreferenced_by_name: 243`
* *Architecture:* `io: 246`, `concurrency: 4`, `import: 49`
* *Defense:* `safety: 1`, `test: 757`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` DeprecatedAssociationsTestHelpers, helper, do
    Post.cache do
      assert_queries_count(1) do
        Post.eager_load(:comments).load
        Post.eager_load(:comments).load
      end

      assert_queries_count(2) do
        Post.eager_load(:comments).skip_query_cache!.load
        Post.eager_load(:comments).skip_query_cache!.load
      end
    end
  end

  test, do
    relation = Post.all
    assert_queries_count(1) do
      assert_equal relation, author, bird, car, categorization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/test/cases/autosave_association_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.466)
- **Top Global Matches:** file_cluster_12: 7.466, file_cluster_10: 8.36, file_cluster_11: 8.965
- **Magnitude:** 864.66 | **LOC:** 2501 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.8%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_autosave_has_one_association_callbacks_get_called_once` **(Callbacks & Closures)** (Impact: 5.2)
    * *Intent:* # a bidirectional autosave is required to trigger multiple calls to # save_has_one_association asser...
  * `test_autosave_collection_association_callbacks_get_called_once` **(Callbacks & Closures)** (Impact: 4.9)
  * `test_autosave_belongs_to_association_callbacks_get_called_once` **(Callbacks & Closures)** (Impact: 4.9)
  * `save_collection_association` **(Compute Cores)** (Impact: 4.5)
  * `save_has_one_association` **(Compute Cores)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 326`, `args: 11`, `func_start: 199`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 384`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 26`, `unreferenced_by_name: 133`
* *Architecture:* `io: 133`, `import: 43`
* *Defense:* `safety: 7`, `test: 501`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 43):` AutosaveAssociationOnACollectionAssociationTests, helper, attachment, author, bird, book, cake_designer, category...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/lib/active_record/connection_adapters/abstract/schema_statements.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.98)
- **Top Global Matches:** file_cluster_15: 6.98, file_cluster_10: 8.037, file_cluster_12: 8.117
- **Magnitude:** 863.26 | **LOC:** 1967 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%)
- **Documentation Coverage:** 76.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `type_to_sql` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `create_table` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* # supplier_id bigint # ) # # ====== Create a temporary table based on a query # # create_table(:long...
  * `index_name_for_remove` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `foreign_key_options` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `remove_reference` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* # Removes the reference(s). Also removes a +type+ column if one exists. # # ====== Remove the refere...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 167`, `args: 98`, `func_start: 120`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 117`, `unreferenced_by_name: 41`
* *Architecture:* `io: 8`, `import: 3`
* *Defense:* `safety: 12`, `doc: 26`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000682
  * `Imports (Out-Degree: 4):` ActiveRecord::Migration::JoinTable, access, filters, openssl
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `activerecord/lib/active_record/migration.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.843)
- **Top Global Matches:** file_cluster_15: 6.843, file_cluster_12: 7.309, file_cluster_11: 7.538
- **Magnitude:** 834.52 | **LOC:** 1650 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **6**; blast radius 2.052; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%), Complexity Load (formerly Cognitive Load) (38.9%)
- **Documentation Coverage:** 68.4564% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `method_missing` **(Compute Cores)** (Impact: 16.8)
  * `initialize` **(Compute Cores)** (Impact: 14.5)
  * `migrate` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* # Runs the migrations in the +migrations_path+. # # If +target_version+ is +nil+, +migrate+ will run...
  * `migrate` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* # Execute this migration in the named direction
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 232`, `args: 56`, `func_start: 129`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 138`, `dead_code: 25`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 18`, `api: 16`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 6`, `doc: 40`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.052
  * `Choke Point (Betweenness):` 0.000309 | `Ripple Effect (Closeness):` 0.005259
  * `Imports (Out-Degree: 10):` ActiveSupport::ActionableError, pending_migration_connection, actionable_error, access, enumerable, attribute_accessors
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `activerecord/lib/active_record/reflection.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.589)
- **Top Global Matches:** file_cluster_15: 7.589, file_cluster_12: 8.355, file_cluster_11: 8.597
- **Magnitude:** 827.42 | **LOC:** 1326 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 1.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%), Guard Balance (formerly Safety Score) (67.1%)
- **Documentation Coverage:** 81.4159% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `derive_fk_query_constraints` **(Compute Cores)** (Impact: 140.9)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `foreign_key` **(Defensive Guards)** (Impact: 15.3)
  * `compute_class` **(Defensive Guards)** (Impact: 13.9)
  * `active_record_primary_key` **(Defensive Guards)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 217`, `args: 52`, `func_start: 134`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 12`, `state_mutation: 132`, `dead_code: 6`, `fragile_debt: 2`
* *Architecture:* `io: 13`, `api: 21`, `import: 1`
* *Defense:* `safety: 28`, `doc: 18`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.249
  * `Choke Point (Betweenness):` 0.006176 | `Ripple Effect (Closeness):` 0.047519
  * `Imports (Out-Degree: 3):` ActiveSupport::Concern, filters, the
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `actionview/test/template/form_helper/form_with_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.685)
- **Top Global Matches:** file_cluster_10: 6.685, file_cluster_11: 8.736, file_cluster_15: 8.967
- **Magnitude:** 810.38 | **LOC:** 2554 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.121; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.5%), Complexity Load (formerly Cognitive Load) (15.8%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `form_text` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `form_text` **(Compute Cores)** (Impact: 14.6)
  * `hidden_fields` **(Defensive Guards)** (Impact: 7.8)
  * `hidden_fields` **(Defensive Guards)** (Impact: 6.4)
  * `url_for` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 235`, `args: 13`, `func_start: 169`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 244`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 10`, `unreferenced_by_name: 147`
* *Architecture:* `io: 26`, `api: 5`, `import: 2`
* *Defense:* `safety: 7`, `test: 159`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RenderERBUtils, Routes, abstract_unit, fake_models
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/lib/active_record/connection_adapters/abstract_adapter.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.933)
- **Top Global Matches:** file_cluster_15: 6.933, file_cluster_11: 7.361, file_cluster_10: 8.229
- **Magnitude:** 804.22 | **LOC:** 1347 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 0.343; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.2%), Guard Balance (formerly Safety Score) (62.3%)
- **Documentation Coverage:** 67.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `with_raw_connection` **(Many-Argument Workhorses)** (Impact: 39.7)
    * *Intent:* # methods, and internal transaction-agnostic queries. # ### # # It's not the primary use case, so no...
  * `initialize` **(Many-Argument Workhorses)** (Impact: 31.8)
  * `log` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `find_cmd_and_exec` **(Defensive Guards)** (Impact: 11.7)
  * `reconnect!` **(Compute Cores)** (Impact: 10.3)
    * *Intent:* # Disconnects from the database if already connected, and establishes a new # connection with the da...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 223`, `args: 55`, `func_start: 158`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 7`, `state_mutation: 101`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 94`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 16`, `doc: 45`, `sync_locks: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.343
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.008444
  * `Imports (Out-Degree: 12):` ActiveSupport::Callbacks, Comparable, DatabaseLimits, QueryCache, Quoting, Savepoints, schema_creation, schema_dumper...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `activerecord/lib/active_record/relation.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.262)
- **Top Global Matches:** file_cluster_15: 6.262, file_cluster_10: 7.514, file_cluster_11: 7.571
- **Magnitude:** 785.88 | **LOC:** 1539 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **3**; blast radius 0.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 75.4902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_all` **(Compute Cores)** (Impact: 23.3)
    * *Intent:* # # Update all customers with the given attributes # Customer.update_all wants_email: true # # # Upd...
  * `compute_cache_version` **(Compute Cores)** (Impact: 20.6)
  * `exec_queries` **(Compute Cores)** (Impact: 15.3)
  * `exec_main_query` **(Defensive Guards)** (Impact: 14.3)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 109 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 145`, `args: 59`, `func_start: 100`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 135`, `planned_debt: 4`, `unreferenced_by_name: 37`
* *Architecture:* `io: 31`, `import: 2`
* *Defense:* `safety: 13`, `doc: 22`, `sync_locks: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.621
  * `Choke Point (Betweenness):` 0.006122 | `Ripple Effect (Closeness):` 0.040919
  * `Imports (Out-Degree: 6):` Enumerable, FinderMethods, SignedId::RelationMethods
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `activerecord/lib/active_record/connection_adapters/abstract_mysql_adapter.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.915)
- **Top Global Matches:** file_cluster_15: 6.915, file_cluster_11: 7.851, file_cluster_10: 8.701
- **Magnitude:** 783.02 | **LOC:** 1076 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (62.8%)
- **Documentation Coverage:** 41.5929% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `table_options` **(Compute Cores)** (Impact: 203.1)
  * `check_constraints` **(Compute Cores)** (Impact: 11.8)
  * `dbconsole` **(Compute Cores)** (Impact: 11.7)
  * `build_change_column_definition` **(Compute Cores)** (Impact: 11.7)
    * *Intent:* # Builds a ChangeColumnDefinition object. # # This definition object contains information about the ...
  * `create_database` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* # Create a new MySQL database with optional <tt>:charset</tt> and <tt>:collation</tt>. # Charset def...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 95 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 148`, `args: 56`, `func_start: 97`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 9`, `state_mutation: 118`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 48`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 7`, `doc: 34`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000454
  * `Imports (Out-Degree: 11):` MySQL::DatabaseStatements, MySQL::Quoting, MySQL::SchemaStatements, abstract_adapter, column, database_statements, explain_pretty_printer, quoting...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `activerecord/test/cases/associations/eager_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.068)
- **Top Global Matches:** file_cluster_10: 8.068, file_cluster_11: 9.374, file_cluster_12: 9.967
- **Magnitude:** 751.76 | **LOC:** 1765 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.4%), Complexity Load (formerly Cognitive Load) (36.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_eager_with_invalid_association_reference` **(I/O & Config Routines)** (Impact: 6.0)
  * `assert_equal_after_sort` **(Callbacks & Closures)** (Impact: 4.2)
    * *Intent:* # Eager includes of has many and habtm associations aren't necessarily sorted in the same way
  * `test_eager_with_multiple_associations_with_same_table_belongs_to` **(I/O & Config Routines)** (Impact: 3.8)
  * `test_eager_with_multiple_associations_with_same_table_has_one` **(I/O & Config Routines)** (Impact: 3.6)
  * `test_eager_with_has_many_and_limit_and_conditions_array_on_the_eagers` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 203`, `args: 4`, `func_start: 159`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 427`, `unreferenced_by_name: 157`
* *Architecture:* `io: 235`, `import: 37`
* *Defense:* `test: 426`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` helper, author, book, categorization, category, citation, club, comment...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actionpack/lib/action_dispatch/routing/route_set.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.331)
- **Top Global Matches:** file_cluster_15: 6.331, file_cluster_12: 6.605, file_cluster_11: 7.373
- **Magnitude:** 743.92 | **LOC:** 956 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.528; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `url_for` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* # The `options` argument must be a hash whose keys are **symbols**.
  * `add_route` **(Compute Cores)** (Impact: 24.0)
  * `handle_positional_args` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `call` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `recognize_path_with_request` **(Many-Argument Workhorses)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 170`, `args: 63`, `func_start: 92`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 168`
* *Architecture:* `io: 3`, `api: 19`, `import: 7`
* *Defense:* `safety: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.528
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.011587
  * `Imports (Out-Degree: 9):` ActiveSupport::Concern, Enumerable, UrlFor, exceptions, journey, endpoint, extract_options, redefine_method...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `activerecord/test/cases/associations/belongs_to_associations_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.571)
- **Top Global Matches:** file_cluster_10: 8.571, file_cluster_11: 9.349, file_cluster_12: 9.369
- **Magnitude:** 731.66 | **LOC:** 2092 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.1%), Complexity Load (formerly Cognitive Load) (30.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_raises_type_mismatch_with_namespaced_class` **(I/O & Config Routines)** (Impact: 5.2)
  * `test_async_load_belongs_to` **(Callbacks & Closures)** (Impact: 4.0)
  * `test_belongs_to_without_counter_cache_option` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* # Ship has a conventionally named `treasures_count` column, but the counter_cache # option is not gi...
  * `test_belongs_to_with_primary_key_joins_on_correct_column` **(I/O & Config Routines)** (Impact: 3.5)
  * `polymorphic_class_for` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 217`, `args: 4`, `func_start: 149`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 5`, `state_mutation: 407`, `duplicate_logic: 7`, `unreferenced_by_name: 140`
* *Architecture:* `io: 283`, `import: 39`
* *Defense:* `safety: 7`, `test: 433`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` DeprecatedAssociationsTestHelpers, WaitForAsyncTestHelper, helper, admin, user, attachment, author, book...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/test/cases/migration_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.29)
- **Top Global Matches:** file_cluster_10: 8.29, file_cluster_12: 8.62, file_cluster_11: 9.074
- **Magnitude:** 705.34 | **LOC:** 2056 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.4%), Concurrency Surface (formerly Concurrency) (17.2%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_remove_column_with_if_not_exists_not_set` **(Compute Cores)** (Impact: 12.5)
  * `with_temp_migration_files` **(Callbacks & Closures)** (Impact: 8.1)
  * `test_add_column_with_casted_type_if_not_exists_set_to_true` **(Defensive Guards)** (Impact: 7.1)
  * `test_add_table_with_decimals` **(I/O & Config Routines)** (Impact: 6.5)
  * `test_default_functions_on_columns` **(I/O & Config Routines)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 227`, `args: 33`, `func_start: 145`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 245`, `duplicate_logic: 39`, `unreferenced_by_name: 93`
* *Architecture:* `io: 120`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 73`, `test: 261`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ActiveSupport::Testing::Stream, util, helper, helper, count_down_latch, computer, developer, person...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activesupport/lib/active_support/cache.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.328)
- **Top Global Matches:** file_cluster_15: 6.328, file_cluster_10: 7.441, file_cluster_11: 8.156
- **Magnitude:** 702.3 | **LOC:** 1171 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **12**; blast radius 1.045; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (71.9%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Defensive Guards)** (Impact: 27.9)
    * *Intent:* # p cache.fetch("foo") # => nil # # ==== Dynamic Options # # In some cases it may be necessary to dy...
  * `_instrument` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `read` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* # +nil+ is returned. # # Note, if data was written with the <tt>:expires_in</tt> or # <tt>:version</...
  * `retrieve_pool_options` **(Compute Cores)** (Impact: 16.7)
  * `merged_options` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* # Merges the default options with ones specific to a method call.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 102`, `args: 52`, `func_start: 61`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 119`, `dead_code: 4`, `planned_debt: 6`
* *Architecture:* `io: 1`, `api: 23`, `import: 19`
* *Defense:* `safety: 16`, `doc: 2`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.045
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.003905
  * `Imports (Out-Degree: 10):` #store, extract_options, enumerable, attribute_accessors, bytes, to_param, try, inflections...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `actionpack/test/dispatch/cookies_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.909)
- **Top Global Matches:** file_cluster_12: 6.909, file_cluster_7: 8.393, file_cluster_11: 9.626
- **Magnitude:** 701.14 | **LOC:** 1676 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.0%), Complexity Load (formerly Cognitive Load) (18.9%), Credential Material (formerly Secrets Risk) (18.0%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_setting_cookie_with_same_site_protection_proc_normal_user_agent` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_setting_cookie_with_same_site_protection_proc_special_user_agent` **(Callbacks & Closures)** (Impact: 2.5)
  * `test_setting_cookie_with_misspelled_same_site_protection_raises` **(Callbacks & Closures)** (Impact: 2.4)
  * `set_cookie_if_not_present` **(Interface Declarations)** (Impact: 2.2)
  * `symbol_key_mock` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 205`, `args: 5`, `func_start: 191`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 258`, `unreferenced_by_name: 142`
* *Architecture:* `api: 136`, `import: 5`
* *Defense:* `safety: 6`, `test: 297`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CookieAssertions, abstract_unit, key_generator, rotation_configuration, openssl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/test/cases/base_test.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_10: 7.155, file_cluster_11: 7.987, file_cluster_12: 8.833
- **Magnitude:** 697.86 | **LOC:** 2087 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.121; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.0%), Concurrency Surface (formerly Concurrency) (35.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.5%), Complexity Load (formerly Cognitive Load) (25.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_readonly_attributes_on_a_new_record` **(I/O & Config Routines)** (Impact: 4.6)
  * `test_marshal_between_processes` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* # Define a new model to ensure there are no caches if self.class.const_defined?("Post", false) flunk...
  * `test_clear_cache_when_setting_table_name` **(I/O & Config Routines)** (Impact: 3.8)
  * `test_dont_clear_sequence_name_when_setting_explicitly` **(I/O & Config Routines)** (Impact: 3.5)
  * `test_dont_clear_inheritance_column_when_setting_explicitly` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 31 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 239`, `args: 3`, `func_start: 162`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 6`, `state_mutation: 308`, `planned_debt: 1`, `unreferenced_by_name: 159`
* *Architecture:* `io: 210`, `concurrency: 5`, `import: 36`
* *Defense:* `safety: 20`, `test: 473`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` ActiveModel::Lint::Tests, ActiveRecord::Base, enumerable, reporting, helper, count_down_latch, author, auto_id...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `activerecord/lib/active_record/connection_adapters/sqlite3_adapter.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.833)
- **Top Global Matches:** file_cluster_15: 6.833, file_cluster_10: 7.207, file_cluster_11: 7.551
- **Magnitude:** 665.96 | **LOC:** 898 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 0.466; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 77.6% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_table` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `translate_exception` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* # SQLite 3.8.2 returns a newly formatted error message: # UNIQUE constraint failed: *table_name*.*co...
  * `copy_table_indexes` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `table_structure_with_collation` **(Compute Cores)** (Impact: 19.2)
  * `extract_value_from_default` **(Compute Cores)** (Impact: 18.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 129`, `args: 32`, `func_start: 75`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 106`
* *Architecture:* `io: 10`, `api: 50`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 12`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.466
  * `Choke Point (Betweenness):` 0.000104 | `Ripple Effect (Closeness):` 0.011759
  * `Imports (Out-Degree: 3):` SQLite3::DatabaseStatements, SQLite3::Quoting, SQLite3::SchemaStatements, abstract_adapter, column, database_statements, explain_pretty_printer, quoting...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `activesupport/test/notifications/instrumenter_test.rb` (RUBY) | Magnitude: 35.74 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 83, test: 24, structural_boundaries: 22, state_mutation: 15
- `actionview/lib/action_view.rb` (RUBY) | Magnitude: 9.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 10, import: 10, closures: 7
- `activerecord/test/activejob/job_runtime_test.rb` (RUBY) | Magnitude: 2.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, test: 3, class_start: 2
- `actionview/test/template/render_test.rb` (RUBY) | Magnitude: 366.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 809, ui_framework: 256, test: 224, structural_boundaries: 184
- `actionmailbox/app/controllers/rails/conductor/action_mailbox/inbound_emails_controller.rb` (RUBY) | Magnitude: 12.22 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 9, func_start: 7, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `actionpack/test/controller/streaming_test.rb` (RUBY) | Magnitude: 6.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, func_start: 3, class_start: 3
- `actionmailbox/app/models/action_mailbox/inbound_email/incineratable.rb` (RUBY) | Magnitude: 2.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, branch: 3, func_start: 2
- `actionview/lib/action_view/buffers.rb` (RUBY) | Magnitude: 93.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 43, func_start: 24, state_mutation: 23
- `activerecord/test/cases/adapters/abstract_mysql_adapter/quoting_test.rb` (RUBY) | Magnitude: 12.46 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 14, test: 12, func_start: 9
- `activesupport/lib/active_support/reloader.rb` (RUBY) | Magnitude: 46.34 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 29, func_start: 15, doc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `railties/lib/rails/commands/app/update_command.rb` (RUBY) | Magnitude: 26.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 19, func_start: 10, io: 8
- `activesupport/test/cache/stores/file_store_test.rb` (RUBY) | Magnitude: 68.2 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 35, io: 32, state_mutation: 27
- `activesupport/test/core_ext/array/wrap_test.rb` (RUBY) | Magnitude: 28.44 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 23, func_start: 16, unreferenced_by_name: 13
- `activerecord/lib/active_record/fixtures.rb` (RUBY) | Magnitude: 191.48 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 241, structural_boundaries: 57, state_mutation: 34, branch: 32
- `actioncable/test/connection/multiple_identifiers_test.rb` (RUBY) | Magnitude: 9.42 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, state_mutation: 5, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `actionpack/lib/action_dispatch/middleware/templates/rescues/_message_and_suggestions.html.erb` (HTML) | Magnitude: 15.44 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, ssr_boundaries: 11, structural_boundaries: 4, core_var_decl: 4
- `actionpack/lib/action_dispatch/middleware/templates/rescues/missing_exact_template.html.erb` (HTML) | Magnitude: 17.44 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, ssr_boundaries: 7, args: 4
- `activerecord/test/cases/adapters/abstract_mysql_adapter/sql_types_test.rb` (RUBY) | Magnitude: 4.64 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, test: 4, func_start: 2
- `activestorage/app/javascript/activestorage/index.js` (JAVASCRIPT) | Magnitude: 4.44 | Delta: **0.166** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, import: 5, indent_spaces: 3, events: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `activerecord/lib/active_record/associations/has_one_through_association.rb` (RUBY) | Magnitude: 37.82 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 34, branch: 11, structural_boundaries: 6, state_mutation: 5
- `activerecord/lib/active_record/connection_adapters/postgresql/schema_dumper.rb` (RUBY) | Magnitude: 170.78 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 137, branch: 34, structural_boundaries: 28, state_mutation: 28
- `activerecord/lib/arel/nodes/casted.rb` (RUBY) | Magnitude: 35.12 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 21, branch: 11, func_start: 6
- `activesupport/lib/active_support/testing/parallelization/server.rb` (RUBY) | Magnitude: 79.48 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 18, state_mutation: 14, func_start: 11
- `activerecord/lib/active_record/attributes.rb` (RUBY) | Magnitude: 45.12 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 17, dead_code: 15, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `activesupport/lib/active_support/core_ext/module/delegation.rb` (RUBY) | Magnitude: 7.54 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: dead_code: 24, indent_spaces: 20, structural_boundaries: 4, encapsulation: 3
- `railties/test/application/middleware/cache_test.rb` (RUBY) | Magnitude: 51.46 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 125, test: 33, structural_boundaries: 23, func_start: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `actionpack/lib/abstract_controller/asset_paths.rb` (RUBY) | Magnitude: 15.22 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 3, class_start: 2, doc: 1
- `activerecord/lib/active_record/base.rb` (RUBY) | Magnitude: 3.96 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 60, indent_spaces: 50, dead_code: 12, import: 11
- `actionpack/lib/abstract_controller/logger.rb` (RUBY) | Magnitude: 1.52 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 5, class_start: 2, doc: 1
- `activerecord/lib/arel/nodes.rb` (RUBY) | Magnitude: 7.7 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 50, import: 50, branch: 2
- `activerecord/lib/active_record/connection_adapters/postgresql/oid.rb` (RUBY) | Magnitude: 3.18 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 30, import: 26, indent_spaces: 6, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `activesupport/lib/active_support/core_ext/hash.rb` (RUBY) | Magnitude: 1.66 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, import: 8
- `guides/source/epub/toc.ncx.erb` (HTML) | Magnitude: 26.08 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, core_var_decl: 19, design_snake_case: 18, ssr_boundaries: 14
- `activesupport/lib/active_support/time.rb` (RUBY) | Magnitude: 2.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 12, structural_boundaries: 10, indent_spaces: 3, class_start: 1
- `activerecord/test/cases/binary_test.rb` (RUBY) | Magnitude: 16.58 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 40, test: 16, core_var_decl: 7, structural_boundaries: 6
- `actionpack/lib/action_dispatch/journey/nfa/dot.rb` (RUBY) | Magnitude: 10.24 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 5, class_start: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `actionview/lib/action_view/template/resolver.rb` (RUBY) | Magnitude: 164.84 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 45, branch: 35, state_mutation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `activemodel/lib/active_model/serialization.rb` (RUBY) | Magnitude: 39.8 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, dead_code: 14, structural_boundaries: 12, branch: 9
- `activesupport/test/messages/message_codec_tests.rb` (RUBY) | Magnitude: 3.58 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, closures: 6, structural_boundaries: 5, test: 5
- `activesupport/test/constantize_test_helpers.rb` (RUBY) | Magnitude: 9.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 5, func_start: 3, closures: 2
- `activesupport/lib/active_support/core_ext/range/compare_range.rb` (RUBY) | Magnitude: 61.74 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: branch: 24, indent_spaces: 24, structural_boundaries: 16, state_mutation: 7
- `actioncable/test/connection/client_socket_test.rb` (RUBY) | Magnitude: 30.92 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 13, state_mutation: 11, closures: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `activerecord/lib/active_record/sanitization.rb` (RUBY) | Magnitude: 148.04 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 130, branch: 51, structural_boundaries: 22, func_start: 12
- `actionpack/lib/abstract_controller/translation.rb` (RUBY) | Magnitude: 32.9 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 7, state_mutation: 6, branch: 5
- `activerecord/lib/active_record/connection_adapters.rb` (RUBY) | Magnitude: 19.34 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 10, import: 9, branch: 7
- `actionview/lib/action_view/helpers/tags/check_box.rb` (RUBY) | Magnitude: 66.72 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 58, branch: 15, state_mutation: 14, structural_boundaries: 13
- `tools/rail_inspector/lib/rail_inspector/configuring/check/framework_defaults.rb` (RUBY) | Magnitude: 0.04 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 14, structural_boundaries: 8, branch: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `railties/lib/rails/application/configuration.rb` -> Churn: **96.48%** | Cog Load: 86.0364% | Debt: 94.4674%
- `activerecord/lib/active_record/connection_adapters/abstract/database_statements.rb` -> Churn: **95.93%** | Cog Load: 47.9915% | Debt: 99.9839%
- `actiontext/lib/action_text/attachment.rb` -> Churn: **64.96%** | Cog Load: 23.1076% | Debt: 99.5345%
- `actionpack/lib/action_controller/metal/request_forgery_protection.rb` -> Churn: **63.45%** | Cog Load: 62.6011% | Debt: 81.8397%
- `activerecord/lib/active_record/connection_adapters/postgresql_adapter.rb` -> Churn: **62.19%** | Cog Load: 51.1617% | Debt: 99.9953%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `activerecord/lib/arel/visitors/to_sql.rb` -> **Said Kaldybaev** (100.0% isolated ownership) | Magnitude: 1248.48
- `activerecord/test/cases/associations/has_many_associations_test.rb` -> **Abdelkader Boudih** (100.0% isolated ownership) | Magnitude: 1187.2
- `activerecord/lib/active_record/reflection.rb` -> **Felix Descoteaux** (100.0% isolated ownership) | Magnitude: 827.42
- `activerecord/lib/active_record/connection_adapters/abstract_mysql_adapter.rb` -> **Matthew Draper** (83.3% isolated ownership) | Magnitude: 783.02
- `activerecord/test/cases/associations/eager_test.rb` -> **Abdelkader Boudih** (100.0% isolated ownership) | Magnitude: 751.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `activesupport/lib/active_support/values/time_zone.rb` -> **Severity: 0.688** (Bridge: 0.0069 * Flux: 99.9355%)
- `activerecord/lib/active_record/reflection.rb` -> **Severity: 0.618** (Bridge: 0.0062 * Flux: 99.9978%)
- `activerecord/lib/active_record/relation.rb` -> **Severity: 0.612** (Bridge: 0.0061 * Flux: 100.0%)
- `activesupport/lib/active_support/delegation.rb` -> **Severity: 0.335** (Bridge: 0.0034 * Flux: 100.0%)
- `activesupport/lib/active_support/core_ext/time/calculations.rb` -> **Severity: 0.209** (Bridge: 0.0021 * Flux: 99.6772%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `activesupport/lib/active_support/core_ext/module/attribute_accessors.rb` -> **Severity: 4.889** (Embedded: 0.0691 * Error Risk: 70.8005%)
- `activesupport/lib/active_support/inflector/methods.rb` -> **Severity: 4.77** (Embedded: 0.0723 * Error Risk: 65.9944%)
- `activesupport/lib/active_support/inflector/inflections.rb` -> **Severity: 4.405** (Embedded: 0.0592 * Error Risk: 74.3808%)
- `activesupport/lib/active_support.rb` -> **Severity: 4.388** (Embedded: 0.0755 * Error Risk: 58.1165%)
- `activesupport/lib/active_support/delegation.rb` -> **Severity: 4.141** (Embedded: 0.0502 * Error Risk: 82.5202%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `activerecord/test/cases/arel/support/fake_record.rb` -> **Severity: 945.1** (Blast Radius: 9.451 * Doc Risk: 100.0%)
- `activesupport/lib/active_support/core_ext/enumerable.rb` -> **Severity: 904.275** (Blast Radius: 11.213 * Doc Risk: 80.6452%)
- `railties/test/isolation/abstract_unit.rb` -> **Severity: 644.2** (Blast Radius: 6.442 * Doc Risk: 100.0%)
- `activesupport/lib/active_support.rb` -> **Severity: 612.727** (Blast Radius: 6.74 * Doc Risk: 90.9091%)
- `activesupport/lib/active_support/inflector/methods.rb` -> **Severity: 588.3** (Blast Radius: 5.883 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1931 literal sites + 14 sites through wrappers = 1945
- **`panics_and_aborts`:** 2326 literal sites + 62 sites through wrappers = 2388

- `assert_nothing_raised` (function, panics_and_aborts, primitive): 6 call sites in 3 files -- `activesupport/lib/active_support/testing/assertions.rb`
- `delete_entry` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `activesupport/lib/active_support/cache.rb`
- `cached_statement` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `activerecord/test/cases/bind_parameter_test.rb`
- `indexes` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `activerecord/lib/active_record/connection_adapters/abstract/schema_statements.rb`
- `format_datetime` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `actionview/lib/action_view/helpers/tags/datetime_field.rb`
- `read_entry` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `activesupport/lib/active_support/cache.rb`
- `checkout_and_verify` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `activerecord/lib/active_record/connection_adapters/abstract/connection_pool.rb`
- `data_source_sql` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `activerecord/lib/active_record/connection_adapters/abstract/schema_statements.rb`
- `enhance_prepare_task_with_output` (function, debug_prints, primitive): 2 call sites in 1 files -- `railties/test/commands/test_test.rb`
- `hash_to_message` (function, debug_prints, primitive): 2 call sites in 1 files -- `activerecord/lib/active_record/encryption/message_pack_message_serializer.rb`
- `marshal_load` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `activesupport/lib/active_support/cache/serializer_with_fallback.rb`
- `message_to_hash` (function, debug_prints, primitive): 2 call sites in 1 files -- `activerecord/lib/active_record/encryption/message_pack_message_serializer.rb`
*(+35 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 127565 call pairs -- scoped 14.6%, unique 0.1%, ambiguous 48.0%, external 37.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| ruby | 124421 | 13.8% | 0.1% | 49.1% | 37.0% |
| javascript | 3084 | 45.1% | 0.0% | 6.8% | 48.1% |
| html | 60 | 18.3% | 0.0% | 0.0% | 81.7% |

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
