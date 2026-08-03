# ARCHITECTURAL_BRIEF: odoo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/odoo` |
| **Timestamp** | `2026-08-03T21:17:01.116919+00:00` |
| **Scan Duration** | `102.07s` |
| **Git Branch** | `19.0` |
| **Git Commit** | `93095e1e9507fde18aefe91aac8c9cb53cadc2f3` |
| **Git Remote** | `https://github.com/odoo/odoo.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 12941 malicious artifacts.

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
| Total Artifacts | 46696 |
| Analyzed Artifacts (Scanned) | 22180 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24516 |
| Total LOC | 1325985 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 47.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.219 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 426 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 8170 | 831156 | 36.8% |
| XML | 6205 | 495 | 28.0% |
| JAVASCRIPT | 4605 | 376870 | 20.8% |
| MARKDOWN | 1048 | 0 | 4.7% |
| CSS | 1034 | 50229 | 4.7% |
| CSV | 845 | 47959 | 3.8% |
| SQLITE | 74 | 407 | 0.3% |
| TYPESCRIPT | 73 | 2383 | 0.3% |
| JSON | 51 | 14904 | 0.2% |
| PLAINTEXT | 43 | 11 | 0.2% |
| SHELL | 18 | 698 | 0.1% |
| HTML | 13 | 857 | 0.1% |
| MAKEFILE | 1 | 16 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.989`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 15160 | 68.3% |
| file_cluster_13 | 4374 | 19.7% |
| file_cluster_4 | 1024 | 4.6% |
| file_cluster_17 | 215 | 1.0% |
| file_cluster_0 | 141 | 0.6% |
| file_cluster_2 | 54 | 0.2% |
| file_cluster_16 | 15 | 0.1% |
| Unknown | 11 | 0.0% |
| file_cluster_11 | 7 | 0.0% |
| file_cluster_12 | 6 | 0.0% |
| file_cluster_7 | 4 | 0.0% |
| file_cluster_1 | 3 | 0.0% |
| file_cluster_9 | 2 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1080 | 4.9% |
| Static: Minified & Vendor Opaque Mass | 82 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24516*

**Composition by Extension & Reason:**
- `.po`: 19537x Excluded (Unsupported Extension: '.po'), 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1344x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.js`: 1163x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 393 LOC), 1x Excluded (Monolithic Amalgamation: 89291 LOC exceeds safe regex boundaries)
- `.pot`: 563x Excluded (Unsupported Extension: '.pot'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 436x Excluded (Explicitly Denied Extension: '.jpg')
- `.bcmap`: 168x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 117x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 141 LOC), 1x Excluded (Machine-Generated Source Code Signature: 843 LOC)
- `.ftl`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 2 exceeds 500 chars), 2x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.scss`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 17 exceeds 500 chars)
- `.ttf`: 96x Excluded (Explicitly Denied Extension: '.ttf')
- `.webp`: 93x Excluded (Explicitly Denied Extension: '.webp')
- `.svg`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Machine-Generated Source Code Signature: 311 LOC), 5x Excluded (Machine-Generated Source Code Signature: 295 LOC)
- `.pdf`: 51x Excluded (Explicitly Denied Extension: '.pdf')
- `no_extension`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 14.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.3 | 0.3 | 0.2 |
| API Exposure | 0.0 | 16.2 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 58.0 | 73.3 | 100.0 |
| Instability Exposure | 0.0 | 15.4 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.4 | 6.7 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 30.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 12.4 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `odoo/service/server.py` (Hits: 122)
- `addons/web/static/tests/core/utils/indexed_db.test.js` (Hits: 67)
- `odoo/tools/appdirs.py` (Hits: 58)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **odoo** (`setup/odoo`) — 4028 inbound connections
2. **exceptions.py** (`odoo/exceptions.py`) — 1344 inbound connections
3. **patch.js** (`addons/web/static/src/core/utils/patch.js`) — 662 inbound connections
4. **logging.py** (`addons/payment/logging.py`) — 527 inbound connections
5. **common.py** (`odoo/tests/common.py`) — 471 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin_sets.js** (`addons/html_editor/static/src/plugin_sets.js`) — 79 outbound dependencies
2. **common.py** (`odoo/tests/common.py`) — 65 outbound dependencies
3. **http.py** (`odoo/http.py`) — 59 outbound dependencies
4. **mail_test_helpers.js** (`addons/mail/static/tests/mail_test_helpers.js`) — 56 outbound dependencies
5. **generate_model_definitions.js** (`addons/point_of_sale/static/tests/unit/data/generate_model_definitions.js`) — 52 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format_and_process` (@ `addons/mail/tests/common.py`) -> Impact: **10556.0** | LOC: 1282
- `_check_constrains_account_id_journal_id` (@ `addons/account/models/account_move_line.py`) -> Impact: **5729.1** | LOC: 1584
- `_unaccent` (@ `odoo/orm/registry.py`) -> Impact: **5361.3** | LOC: 1104
- `_recompute_cash_rounding_lines` (@ `addons/account/models/account_move.py`) -> Impact: **5178.6** | LOC: 1242
- `_get_bom_data` (@ `addons/mrp/report/mrp_report_bom_structure.py`) -> Impact: **4954.1** | LOC: 602
- `split_lots` (@ `addons/stock/models/stock_move.py`) -> Impact: **4462.4** | LOC: 1225
- `onchange_amount` (@ `addons/account/models/account_tax.py`) -> Impact: **4395.1** | LOC: 3395
- `_get_search_order` (@ `addons/website_sale/controllers/main.py`) -> Impact: **4338.7** | LOC: 1661
- `__get__` (@ `odoo/orm/fields_relational.py`) -> Impact: **4159.6** | LOC: 871
- `setUpClass` (@ `addons/test_mail/tests/test_mail_composer.py`) -> Impact: **3967.4** | LOC: 2238
  * *Intent:* # force 'now' to ease test about schedulers cls.reference_now = FieldDatetime.from_string('2022-12-24 12:00:00') cls.user_employee_2 = mail_new_test_u...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `create` (@ `addons/account/models/account_account.py`) -> **O(2^N) [Recursive]**
- `extract_pdf_embedded_files` (@ `addons/account/models/account_document_import_mixin.py`) -> **O(2^N) [Recursive]**
- `write` (@ `addons/account/models/account_journal.py`) -> **O(2^N) [Recursive]**
- `_recompute_cash_rounding_lines` (@ `addons/account/models/account_move.py`) -> **O(2^N) [Recursive]**
- `_inverse_partner_id` (@ `addons/account/models/account_move.py`) -> **O(2^N) [Recursive]**
- `_check_constrains_account_id_journal_id` (@ `addons/account/models/account_move_line.py`) -> **O(2^N) [Recursive]**
- `_validate_analytic_distribution` (@ `addons/account/models/account_move_line.py`) -> **O(2^N) [Recursive]**
- `install_l10n_modules` (@ `addons/account/models/company.py`) -> **O(2^N) [Recursive]**
- `_render_qweb_pdf_prepare_streams` (@ `addons/account/models/ir_actions_report.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Custom behavior for 'account.report_original_vendor_bill'. if self._get_report(report_ref).report_name != 'account.report_original_vendor_bill': ret...
- `write` (@ `addons/account/models/partner.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `cron_thread` (@ `odoo/service/server.py`) -> DB Complexity: **286**
  * *Intent:* # Clean-up threads that are no longer alive # e.g. threads that exceeded their real time,
- `MarkerClusterer` (@ `addons/website_google_map/static/src/lib/markerclusterer.js`) -> DB Complexity: **186**
  * *Intent:* // ==ClosureCompiler== // @compilation_level ADVANCED_OPTIMIZATIONS // @externs_url https://raw.githubusercontent.com/google/closure-compiler/master/c...
- `afterEach` (@ `addons/mail/static/tests/mail_test_helpers_contains.js`) -> DB Complexity: **179**
  * *Intent:* /** * Waits until exactly one element matching the given `selector` is present in * `options.target` and then pastes `files` on it. *
- `patch` (@ `addons/mail/static/src/discuss/core/common/thread_model_patch.js`) -> DB Complexity: **170**
- `patch` (@ `addons/mail/static/src/chatter/web/chatter_patch.js`) -> DB Complexity: **155**
  * *Intent:* /**
- `sequence` (@ `addons/html_editor/static/src/main/media/media_dialog/media_dialog.js`) -> DB Complexity: **136**
- `content_disposition` (@ `odoo/http.py`) -> DB Complexity: **134**
- `onChoiceImageClick` (@ `addons/survey/static/src/interactions/survey_form.js`) -> DB Complexity: **131**
- `test_20_monetary_opw_2223134` (@ `odoo/addons/test_orm/tests/test_fields.py`) -> DB Complexity: **124**
  * *Intent:* # delete and add a line: the deletion of the line clears the cache, then # the recomputation of 'total' must prefetch record.currency_id without # scr...
- `convertObjectValuesToInt` (@ `addons/pos_glory_cash/static/src/glory_service.js`) -> DB Complexity: **118**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `addons/account/models` | 52 | 66918.68 | 12.94% | 36.94% |
| `odoo/orm` | 23 | 47596.5 | 25.21% | 37.88% |
| `odoo/addons/base/models` | 46 | 44359.56 | 14.49% | 35.95% |
| `addons/stock/models` | 26 | 32301.48 | 16.11% | 28.76% |
| `addons/mail/models` | 60 | 29459.7 | 13.18% | 32.51% |
| `addons/test_mail/tests` | 32 | 19271.34 | 3.89% | 0.0% |
| `addons/mail/static/src/core/common` | 152 | 18280.15 | 24.48% | 36.32% |
| `addons/account/tests` | 69 | 18120.82 | 3.27% | 0.0% |
| `odoo/addons/base/tests` | 87 | 17232.24 | 4.49% | 0.0% |
| `addons/mail/tests` | 29 | 15652.62 | 4.93% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `addons/account/controllers/tests_shared_js_python.py` -> **100.0%** Exposure
- `addons/account/wizard/account_autopost_bills_wizard.py` -> **100.0%** Exposure
- `addons/account_check_printing/__init__.py` -> **100.0%** Exposure
- `addons/account_edi_proxy_client/__init__.py` -> **100.0%** Exposure
- `addons/account_payment/__init__.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `addons/account_edi_proxy_client/models/account_edi_proxy_auth.py` -> **100.0%** Exposure
- `addons/account_peppol/controllers/portal.py` -> **100.0%** Exposure
- `addons/account_peppol/wizard/account_move_send_batch_wizard.py` -> **100.0%** Exposure
- `addons/base_address_extended/models/res_partner.py` -> **100.0%** Exposure
- `addons/base_import/models/odf_ods_reader.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `addons/stock/tests/test_move2.py` -> **79** Orphaned Functions | **5** Duplicates
- `addons/mrp/tests/test_order.py` -> **83** Orphaned Functions | **0** Duplicates
- `addons/stock_account/tests/test_stockvaluation.py` -> **80** Orphaned Functions | **3** Duplicates
- `addons/html_editor/static/tests/utils/regex.test.js` -> **0** Orphaned Functions | **81** Duplicates
- `addons/stock_account/tests/test_stockvaluationlayer.py` -> **34** Orphaned Functions | **40** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`odoo/tools/template_inheritance.py`** -> AI Confidence: **99.48%**
2. **`addons/account/models/account_move_line.py`** -> AI Confidence: **99.39%**
3. **`addons/account/models/account_tax.py`** -> AI Confidence: **99.39%**
4. **`addons/account/models/chart_template.py`** -> AI Confidence: **99.39%**
5. **`addons/account/wizard/account_payment_register.py`** -> AI Confidence: **99.39%**
6. **`addons/hr_holidays/models/hr_leave.py`** -> AI Confidence: **99.39%**
7. **`addons/l10n_es_edi_sii/models/account_edi_format.py`** -> AI Confidence: **99.39%**
8. **`addons/l10n_tw_edi_ecpay/models/account_move.py`** -> AI Confidence: **99.39%**
9. **`addons/mail/models/mail_thread.py`** -> AI Confidence: **99.39%**
10. **`addons/mail/wizard/mail_compose_message.py`** -> AI Confidence: **99.39%**
11. **`addons/microsoft_calendar/models/calendar.py`** -> AI Confidence: **99.39%**
12. **`addons/stock/models/stock_move_line.py`** -> AI Confidence: **99.39%**
13. **`addons/test_mail/tests/test_mail_composer.py`** -> AI Confidence: **99.39%**
14. **`addons/test_mail/tests/test_mail_message_security.py`** -> AI Confidence: **99.39%**
15. **`addons/survey/static/src/interactions/survey_form.js`** -> AI Confidence: **99.39%**
16. **`addons/web/static/tests/_framework/mock_server/mock_model.js`** -> AI Confidence: **99.39%**
17. **`addons/stock/models/stock_move.py`** -> AI Confidence: **99.35%**
18. **`odoo/modules/loading.py`** -> AI Confidence: **99.35%**
19. **`addons/html_editor/static/src/core/dom_plugin.js`** -> AI Confidence: **99.35%**
20. **`addons/html_editor/static/src/main/link/link_plugin.js`** -> AI Confidence: **99.35%**
21. **`addons/hr_holidays/models/hr_leave_allocation.py`** -> AI Confidence: **99.34%**
22. **`addons/point_of_sale/models/report_sale_details.py`** -> AI Confidence: **99.34%**
23. **`addons/stock_account/models/product.py`** -> AI Confidence: **99.34%**
24. **`odoo/addons/test_orm/tests/test_performance.py`** -> AI Confidence: **99.34%**
25. **`addons/html_editor/static/src/main/table/table_resize_plugin.js`** -> AI Confidence: **99.34%**
26. **`addons/survey/static/src/interactions/survey_session_manage.js`** -> AI Confidence: **99.34%**
27. **`addons/web/static/src/search/search_arch_parser.js`** -> AI Confidence: **99.34%**
28. **`odoo/tools/arabic_reshaper/__init__.py`** -> AI Confidence: **99.32%**
29. **`addons/account/models/account_account.py`** -> AI Confidence: **99.31%**
30. **`addons/account/models/account_journal.py`** -> AI Confidence: **99.31%**
31. **`addons/account/models/account_journal_dashboard.py`** -> AI Confidence: **99.31%**
32. **`addons/account/models/account_move.py`** -> AI Confidence: **99.31%**
33. **`addons/account/models/company.py`** -> AI Confidence: **99.31%**
34. **`addons/account/models/partner.py`** -> AI Confidence: **99.31%**
35. **`addons/account/models/res_partner_bank.py`** -> AI Confidence: **99.31%**
36. **`addons/account/models/sequence_mixin.py`** -> AI Confidence: **99.31%**
37. **`addons/account/tests/common.py`** -> AI Confidence: **99.31%**
38. **`addons/account/tests/test_account_all_l10n.py`** -> AI Confidence: **99.31%**
39. **`addons/account/tests/test_account_inalterable_hash.py`** -> AI Confidence: **99.31%**
40. **`addons/account/tests/test_account_lock_exception.py`** -> AI Confidence: **99.31%**
41. **`addons/account/wizard/account_automatic_entry_wizard.py`** -> AI Confidence: **99.31%**
42. **`addons/account/wizard/accrued_orders.py`** -> AI Confidence: **99.31%**
43. **`addons/account_edi_ubl_cii/models/account_edi_common.py`** -> AI Confidence: **99.31%**
44. **`addons/account_edi_ubl_cii/models/account_edi_xml_ubl_20.py`** -> AI Confidence: **99.31%**
45. **`addons/account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py`** -> AI Confidence: **99.31%**
46. **`addons/account_edi_ubl_cii/models/account_move_send.py`** -> AI Confidence: **99.31%**
47. **`addons/account_peppol/models/account_edi_proxy_user.py`** -> AI Confidence: **99.31%**
48. **`addons/account_peppol/models/account_move_send.py`** -> AI Confidence: **99.31%**
49. **`addons/account_peppol/models/res_company.py`** -> AI Confidence: **99.31%**
50. **`addons/account_peppol/models/res_partner.py`** -> AI Confidence: **99.31%**
51. **`addons/account_peppol/wizard/peppol_registration.py`** -> AI Confidence: **99.31%**
52. **`addons/analytic/models/analytic_mixin.py`** -> AI Confidence: **99.31%**
53. **`addons/attachment_indexation/models/ir_attachment.py`** -> AI Confidence: **99.31%**
54. **`addons/auth_signup/models/res_users.py`** -> AI Confidence: **99.31%**
55. **`addons/auth_totp/models/res_users.py`** -> AI Confidence: **99.31%**
56. **`addons/barcodes_gs1_nomenclature/models/barcode_nomenclature.py`** -> AI Confidence: **99.31%**
57. **`addons/base_automation/models/base_automation.py`** -> AI Confidence: **99.31%**
58. **`addons/base_import_module/models/ir_module.py`** -> AI Confidence: **99.31%**
59. **`addons/base_vat/models/res_partner.py`** -> AI Confidence: **99.31%**
60. **`addons/calendar/models/calendar_attendee.py`** -> AI Confidence: **99.31%**
61. **`addons/calendar/models/calendar_event.py`** -> AI Confidence: **99.31%**
62. **`addons/calendar/models/calendar_recurrence.py`** -> AI Confidence: **99.31%**
63. **`addons/calendar/tests/test_event_notifications.py`** -> AI Confidence: **99.31%**
64. **`addons/certificate/models/certificate.py`** -> AI Confidence: **99.31%**
65. **`addons/certificate/models/key.py`** -> AI Confidence: **99.31%**
66. **`addons/cloud_storage_migration/models/ir_attachment.py`** -> AI Confidence: **99.31%**
67. **`addons/crm/models/crm_lead.py`** -> AI Confidence: **99.31%**
68. **`addons/crm/models/crm_team.py`** -> AI Confidence: **99.31%**
69. **`addons/crm/tests/common.py`** -> AI Confidence: **99.31%**
70. **`addons/data_recycle/models/data_recycle_model.py`** -> AI Confidence: **99.31%**
71. **`addons/digest/models/digest.py`** -> AI Confidence: **99.31%**
72. **`addons/event/models/event_event.py`** -> AI Confidence: **99.31%**
73. **`addons/event/models/event_mail.py`** -> AI Confidence: **99.31%**
74. **`addons/event/models/event_registration.py`** -> AI Confidence: **99.31%**
75. **`addons/event/tests/test_event_mail_schedule.py`** -> AI Confidence: **99.31%**
76. **`addons/fleet/models/fleet_vehicle.py`** -> AI Confidence: **99.31%**
77. **`addons/gamification/models/gamification_challenge.py`** -> AI Confidence: **99.31%**
78. **`addons/google_calendar/models/calendar.py`** -> AI Confidence: **99.31%**
79. **`addons/google_calendar/models/google_sync.py`** -> AI Confidence: **99.31%**
80. **`addons/hr/models/hr_employee.py`** -> AI Confidence: **99.31%**
81. **`addons/hr/models/hr_version.py`** -> AI Confidence: **99.31%**
82. **`addons/hr/tests/test_hr_version.py`** -> AI Confidence: **99.31%**
83. **`addons/hr/tests/test_self_user_access.py`** -> AI Confidence: **99.31%**
84. **`addons/hr_attendance/models/hr_attendance.py`** -> AI Confidence: **99.31%**
85. **`addons/hr_attendance/models/hr_attendance_overtime_rule.py`** -> AI Confidence: **99.31%**
86. **`addons/hr_expense/models/hr_expense.py`** -> AI Confidence: **99.31%**
87. **`addons/hr_holidays/models/hr_employee.py`** -> AI Confidence: **99.31%**
88. **`addons/hr_holidays/models/hr_leave_type.py`** -> AI Confidence: **99.31%**
89. **`addons/hr_holidays/models/resource.py`** -> AI Confidence: **99.31%**
90. **`addons/hr_holidays/tests/test_accrual_allocations.py`** -> AI Confidence: **99.31%**
91. **`addons/hr_recruitment/models/hr_applicant.py`** -> AI Confidence: **99.31%**
92. **`addons/hr_skills/models/hr_employee.py`** -> AI Confidence: **99.31%**
93. **`addons/hr_timesheet/models/hr_timesheet.py`** -> AI Confidence: **99.31%**
94. **`addons/hr_work_entry/models/hr_version.py`** -> AI Confidence: **99.31%**
95. **`addons/hr_work_entry/models/hr_work_entry.py`** -> AI Confidence: **99.31%**
96. **`addons/html_editor/models/ir_ui_view.py`** -> AI Confidence: **99.31%**
97. **`addons/html_editor/tools.py`** -> AI Confidence: **99.31%**
98. **`addons/http_routing/models/ir_http.py`** -> AI Confidence: **99.31%**
99. **`addons/http_routing/tests/common.py`** -> AI Confidence: **99.31%**
100. **`addons/im_livechat/models/chatbot_script_step.py`** -> AI Confidence: **99.31%**
101. **`addons/im_livechat/models/discuss_channel.py`** -> AI Confidence: **99.31%**
102. **`addons/im_livechat/models/im_livechat_channel.py`** -> AI Confidence: **99.31%**
103. **`addons/iot_drivers/iot_handlers/drivers/keyboard_usb_driver_L.py`** -> AI Confidence: **99.31%**
104. **`addons/iot_drivers/iot_handlers/drivers/printer_driver_L.py`** -> AI Confidence: **99.31%**
105. **`addons/iot_drivers/iot_handlers/drivers/printer_driver_W.py`** -> AI Confidence: **99.31%**
106. **`addons/iot_drivers/iot_handlers/interfaces/printer_interface_L.py`** -> AI Confidence: **99.31%**
107. **`addons/iot_drivers/main.py`** -> AI Confidence: **99.31%**
108. **`addons/iot_drivers/websocket_client.py`** -> AI Confidence: **99.31%**
109. **`addons/l10n_ar/models/account_move.py`** -> AI Confidence: **99.31%**
110. **`addons/l10n_ch/models/res_bank.py`** -> AI Confidence: **99.31%**
111. **`addons/l10n_dk_nemhandel/models/res_partner.py`** -> AI Confidence: **99.31%**
112. **`addons/l10n_eg_edi_eta/models/account_edi_format.py`** -> AI Confidence: **99.31%**
113. **`addons/l10n_es_edi_facturae/models/account_move.py`** -> AI Confidence: **99.31%**
114. **`addons/l10n_es_edi_tbai/models/l10n_es_edi_tbai_document.py`** -> AI Confidence: **99.31%**
115. **`addons/l10n_es_edi_verifactu/models/verifactu_document.py`** -> AI Confidence: **99.31%**
116. **`addons/l10n_es_edi_verifactu/tests/test_document.py`** -> AI Confidence: **99.31%**
117. **`addons/l10n_eu_oss/models/res_company.py`** -> AI Confidence: **99.31%**
118. **`addons/l10n_fr_account/wizard/account_fr_fec_export_wizard.py`** -> AI Confidence: **99.31%**
119. **`addons/l10n_gr_edi/models/account_move.py`** -> AI Confidence: **99.31%**
120. **`addons/l10n_hr_edi/models/account_move.py`** -> AI Confidence: **99.31%**
121. **`addons/l10n_hu_edi/models/account_move.py`** -> AI Confidence: **99.31%**
122. **`addons/l10n_hu_edi/models/res_company.py`** -> AI Confidence: **99.31%**
123. **`addons/l10n_hu_edi/tests/test_flows_live.py`** -> AI Confidence: **99.31%**
124. **`addons/l10n_hu_edi/tests/test_flows_mocked.py`** -> AI Confidence: **99.31%**
125. **`addons/l10n_in/models/account_invoice.py`** -> AI Confidence: **99.31%**
126. **`addons/l10n_in/models/res_partner.py`** -> AI Confidence: **99.31%**
127. **`addons/l10n_in_edi/models/account_move.py`** -> AI Confidence: **99.31%**
128. **`addons/l10n_in_ewaybill/models/l10n_in_ewaybill.py`** -> AI Confidence: **99.31%**
129. **`addons/l10n_in_hr_holidays/models/hr_leave.py`** -> AI Confidence: **99.31%**
130. **`addons/l10n_it_edi/models/account_move.py`** -> AI Confidence: **99.31%**
131. **`addons/l10n_jo_edi_pos/models/pos_edi_ubl_21_jo.py`** -> AI Confidence: **99.31%**
132. **`addons/l10n_my_edi/models/myinvois_document.py`** -> AI Confidence: **99.31%**
133. **`addons/l10n_my_edi/tests/test_submissions.py`** -> AI Confidence: **99.31%**
134. **`addons/l10n_my_edi_pos/tests/test_myinvois_pos.py`** -> AI Confidence: **99.31%**
135. **`addons/l10n_pl_edi/models/account_move.py`** -> AI Confidence: **99.31%**
136. **`addons/l10n_ro_edi/models/account_move.py`** -> AI Confidence: **99.31%**
137. **`addons/l10n_ro_edi_stock/models/stock_picking.py`** -> AI Confidence: **99.31%**
138. **`addons/l10n_ro_edi_stock_batch/models/stock_picking_batch.py`** -> AI Confidence: **99.31%**
139. **`addons/l10n_sa_edi/models/account_edi_format.py`** -> AI Confidence: **99.31%**
140. **`addons/l10n_sa_edi/models/account_move.py`** -> AI Confidence: **99.31%**
141. **`addons/l10n_sa_edi/models/certificate.py`** -> AI Confidence: **99.31%**
142. **`addons/l10n_tr_nilvera_edispatch/models/stock_picking.py`** -> AI Confidence: **99.31%**
143. **`addons/l10n_tr_nilvera_einvoice/models/account_move.py`** -> AI Confidence: **99.31%**
144. **`addons/l10n_tw_edi_ecpay_website_sale/controllers/main.py`** -> AI Confidence: **99.31%**
145. **`addons/l10n_vn_edi_viettel/models/account_move.py`** -> AI Confidence: **99.31%**
146. **`addons/link_tracker/models/link_tracker.py`** -> AI Confidence: **99.31%**
147. **`addons/lunch/models/lunch_alert.py`** -> AI Confidence: **99.31%**
148. **`addons/lunch/models/lunch_supplier.py`** -> AI Confidence: **99.31%**
149. **`addons/mail/controllers/mail.py`** -> AI Confidence: **99.31%**
150. **`addons/mail/models/discuss/discuss_channel_member.py`** -> AI Confidence: **99.31%**
151. **`addons/mail/models/ir_websocket.py`** -> AI Confidence: **99.31%**
152. **`addons/mail/models/mail_activity.py`** -> AI Confidence: **99.31%**
153. **`addons/mail/models/mail_alias.py`** -> AI Confidence: **99.31%**
154. **`addons/mail/models/mail_mail.py`** -> AI Confidence: **99.31%**
155. **`addons/mail/models/mail_message.py`** -> AI Confidence: **99.31%**
156. **`addons/mail/models/mail_render_mixin.py`** -> AI Confidence: **99.31%**
157. **`addons/mail/models/mail_template.py`** -> AI Confidence: **99.31%**
158. **`addons/mail/models/models.py`** -> AI Confidence: **99.31%**
159. **`addons/mail/models/res_users.py`** -> AI Confidence: **99.31%**
160. **`addons/mail/tests/common.py`** -> AI Confidence: **99.31%**
161. **`addons/mail/tests/common_controllers.py`** -> AI Confidence: **99.31%**
162. **`addons/mail/tests/test_ir_mail_server.py`** -> AI Confidence: **99.31%**
163. **`addons/mail/tests/test_res_partner.py`** -> AI Confidence: **99.31%**
164. **`addons/mail/tools/discuss.py`** -> AI Confidence: **99.31%**
165. **`addons/mail/wizard/mail_activity_schedule.py`** -> AI Confidence: **99.31%**
166. **`addons/mail_group/models/mail_group.py`** -> AI Confidence: **99.31%**
167. **`addons/mail_plugin/controllers/mail_plugin.py`** -> AI Confidence: **99.31%**
168. **`addons/mass_mailing/models/mailing.py`** -> AI Confidence: **99.31%**
169. **`addons/mass_mailing/tests/common.py`** -> AI Confidence: **99.31%**
170. **`addons/mass_mailing_sms/tests/common.py`** -> AI Confidence: **99.31%**
171. **`addons/microsoft_calendar/models/microsoft_sync.py`** -> AI Confidence: **99.31%**
172. **`addons/microsoft_calendar/tests/test_sync_odoo2microsoft_mail.py`** -> AI Confidence: **99.31%**
173. **`addons/mrp/models/mrp_production.py`** -> AI Confidence: **99.31%**
174. **`addons/mrp/models/mrp_workcenter.py`** -> AI Confidence: **99.31%**
175. **`addons/mrp/models/mrp_workorder.py`** -> AI Confidence: **99.31%**
176. **`addons/mrp/report/mrp_report_mo_overview.py`** -> AI Confidence: **99.31%**
177. **`addons/mrp_subcontracting/models/stock_picking.py`** -> AI Confidence: **99.31%**
178. **`addons/payment/models/payment_provider.py`** -> AI Confidence: **99.31%**
179. **`addons/payment_nuvei/models/payment_transaction.py`** -> AI Confidence: **99.31%**
180. **`addons/payment_razorpay/models/payment_transaction.py`** -> AI Confidence: **99.31%**
181. **`addons/payment_stripe/models/payment_transaction.py`** -> AI Confidence: **99.31%**
182. **`addons/payment_worldline/models/payment_transaction.py`** -> AI Confidence: **99.31%**
183. **`addons/point_of_sale/controllers/main.py`** -> AI Confidence: **99.31%**
184. **`addons/point_of_sale/models/pos_config.py`** -> AI Confidence: **99.31%**
185. **`addons/point_of_sale/models/pos_order.py`** -> AI Confidence: **99.31%**
186. **`addons/point_of_sale/models/product_template.py`** -> AI Confidence: **99.31%**
187. **`addons/point_of_sale/tests/common.py`** -> AI Confidence: **99.31%**
188. **`addons/portal/controllers/portal.py`** -> AI Confidence: **99.31%**
189. **`addons/pos_adyen/models/pos_payment_method.py`** -> AI Confidence: **99.31%**
190. **`addons/pos_self_order/models/res_config_settings.py`** -> AI Confidence: **99.31%**
191. **`addons/product/models/product_product.py`** -> AI Confidence: **99.31%**
192. **`addons/product/models/product_template.py`** -> AI Confidence: **99.31%**
193. **`addons/project/controllers/portal.py`** -> AI Confidence: **99.31%**
194. **`addons/project/models/project_project.py`** -> AI Confidence: **99.31%**
195. **`addons/project/models/project_task.py`** -> AI Confidence: **99.31%**
196. **`addons/project/tests/test_multicompany.py`** -> AI Confidence: **99.31%**
197. **`addons/project/tests/test_project_sharing_portal_access.py`** -> AI Confidence: **99.31%**
198. **`addons/purchase/models/purchase_order.py`** -> AI Confidence: **99.31%**
199. **`addons/purchase/models/purchase_order_line.py`** -> AI Confidence: **99.31%**
200. **`addons/purchase_stock/models/product.py`** -> AI Confidence: **99.31%**
201. **`addons/purchase_stock/models/purchase_order.py`** -> AI Confidence: **99.31%**
202. **`addons/purchase_stock/models/stock_rule.py`** -> AI Confidence: **99.31%**
203. **`addons/repair/models/repair.py`** -> AI Confidence: **99.31%**
204. **`addons/resource/models/resource_calendar.py`** -> AI Confidence: **99.31%**
205. **`addons/resource/models/resource_resource.py`** -> AI Confidence: **99.31%**
206. **`addons/sale/controllers/portal.py`** -> AI Confidence: **99.31%**
207. **`addons/sale/models/sale_order.py`** -> AI Confidence: **99.31%**
208. **`addons/sale/models/sale_order_line.py`** -> AI Confidence: **99.31%**
209. **`addons/sale_loyalty/models/sale_order.py`** -> AI Confidence: **99.31%**
210. **`addons/sale_mrp/tests/test_sale_mrp_flow.py`** -> AI Confidence: **99.31%**
211. **`addons/sale_project/models/project_project.py`** -> AI Confidence: **99.31%**
212. **`addons/sms/tests/common.py`** -> AI Confidence: **99.31%**
213. **`addons/snailmail/models/snailmail_letter.py`** -> AI Confidence: **99.31%**
214. **`addons/spreadsheet/models/spreadsheet_mixin.py`** -> AI Confidence: **99.31%**
215. **`addons/stock/models/product.py`** -> AI Confidence: **99.31%**
216. **`addons/stock/models/stock_lot.py`** -> AI Confidence: **99.31%**
217. **`addons/stock/models/stock_orderpoint.py`** -> AI Confidence: **99.31%**
218. **`addons/stock/models/stock_package.py`** -> AI Confidence: **99.31%**
219. **`addons/stock/models/stock_picking.py`** -> AI Confidence: **99.31%**
220. **`addons/stock/models/stock_quant.py`** -> AI Confidence: **99.31%**
221. **`addons/stock/models/stock_rule.py`** -> AI Confidence: **99.31%**
222. **`addons/stock/wizard/stock_replenishment_info.py`** -> AI Confidence: **99.31%**
223. **`addons/survey/controllers/main.py`** -> AI Confidence: **99.31%**
224. **`addons/survey/models/survey_question.py`** -> AI Confidence: **99.31%**
225. **`addons/survey/models/survey_survey.py`** -> AI Confidence: **99.31%**
226. **`addons/survey/models/survey_user_input.py`** -> AI Confidence: **99.31%**
227. **`addons/test_mail/tests/test_mail_activity.py`** -> AI Confidence: **99.31%**
228. **`addons/test_mail/tests/test_mail_activity_plan.py`** -> AI Confidence: **99.31%**
229. **`addons/test_mail/tests/test_mail_alias.py`** -> AI Confidence: **99.31%**
230. **`addons/test_mail/tests/test_mail_followers.py`** -> AI Confidence: **99.31%**
231. **`addons/test_mail/tests/test_mail_mail.py`** -> AI Confidence: **99.31%**
232. **`addons/test_mail/tests/test_mail_template.py`** -> AI Confidence: **99.31%**
233. **`addons/test_mail/tests/test_mail_thread_internals.py`** -> AI Confidence: **99.31%**
234. **`addons/test_mail/tests/test_message_post.py`** -> AI Confidence: **99.31%**
235. **`addons/test_mail/tests/test_performance.py`** -> AI Confidence: **99.31%**
236. **`addons/test_mail_full/tests/test_mail_performance.py`** -> AI Confidence: **99.31%**
237. **`addons/test_mail_full/tests/test_portal.py`** -> AI Confidence: **99.31%**
238. **`addons/test_mail_full/tests/test_rating.py`** -> AI Confidence: **99.31%**
239. **`addons/test_mass_mailing/tests/test_mailing_sms.py`** -> AI Confidence: **99.31%**
240. **`addons/web/controllers/binary.py`** -> AI Confidence: **99.31%**
241. **`addons/web/controllers/export.py`** -> AI Confidence: **99.31%**
242. **`addons/web/controllers/json.py`** -> AI Confidence: **99.31%**
243. **`addons/web/controllers/pivot.py`** -> AI Confidence: **99.31%**
244. **`addons/web/controllers/report.py`** -> AI Confidence: **99.31%**
245. **`addons/web/controllers/utils.py`** -> AI Confidence: **99.31%**
246. **`addons/web/models/models.py`** -> AI Confidence: **99.31%**
247. **`addons/website/controllers/form.py`** -> AI Confidence: **99.31%**
248. **`addons/website/controllers/main.py`** -> AI Confidence: **99.31%**
249. **`addons/website/models/ir_http.py`** -> AI Confidence: **99.31%**
250. **`addons/website/models/ir_module_module.py`** -> AI Confidence: **99.31%**
251. **`addons/website/models/ir_qweb.py`** -> AI Confidence: **99.31%**
252. **`addons/website/models/ir_ui_view.py`** -> AI Confidence: **99.31%**
253. **`addons/website/models/website.py`** -> AI Confidence: **99.31%**
254. **`addons/website/models/website_menu.py`** -> AI Confidence: **99.31%**
255. **`addons/website/models/website_page.py`** -> AI Confidence: **99.31%**
256. **`addons/website/models/website_snippet_filter.py`** -> AI Confidence: **99.31%**
257. **`addons/website/tests/test_crawl.py`** -> AI Confidence: **99.31%**
258. **`addons/website/tests/test_fuzzy.py`** -> AI Confidence: **99.31%**
259. **`addons/website_blog/controllers/main.py`** -> AI Confidence: **99.31%**
260. **`addons/website_blog/models/website_blog.py`** -> AI Confidence: **99.31%**
261. **`addons/website_crm_iap_reveal/models/crm_reveal_rule.py`** -> AI Confidence: **99.31%**
262. **`addons/website_crm_partner_assign/controllers/main.py`** -> AI Confidence: **99.31%**
263. **`addons/website_event/controllers/main.py`** -> AI Confidence: **99.31%**
264. **`addons/website_event/models/event_event.py`** -> AI Confidence: **99.31%**
265. **`addons/website_event_track/controllers/event_track.py`** -> AI Confidence: **99.31%**
266. **`addons/website_event_track/models/event_track.py`** -> AI Confidence: **99.31%**
267. **`addons/website_forum/models/forum_post.py`** -> AI Confidence: **99.31%**
268. **`addons/website_sale/controllers/cart.py`** -> AI Confidence: **99.31%**
269. **`addons/website_sale/controllers/main.py`** -> AI Confidence: **99.31%**
270. **`addons/website_sale/models/product_feed.py`** -> AI Confidence: **99.31%**
271. **`addons/website_sale/models/product_template.py`** -> AI Confidence: **99.31%**
272. **`addons/website_sale/models/sale_order.py`** -> AI Confidence: **99.31%**
273. **`addons/website_sale/models/website.py`** -> AI Confidence: **99.31%**
274. **`addons/website_slides/controllers/main.py`** -> AI Confidence: **99.31%**
275. **`addons/website_slides/models/slide_channel.py`** -> AI Confidence: **99.31%**
276. **`addons/website_slides/models/slide_slide.py`** -> AI Confidence: **99.31%**
277. **`addons/website_slides/tests/test_security.py`** -> AI Confidence: **99.31%**
278. **`odoo/addons/base/models/assetsbundle.py`** -> AI Confidence: **99.31%**
279. **`odoo/addons/base/models/ir_actions.py`** -> AI Confidence: **99.31%**
280. **`odoo/addons/base/models/ir_actions_report.py`** -> AI Confidence: **99.31%**
281. **`odoo/addons/base/models/ir_asset.py`** -> AI Confidence: **99.31%**
282. **`odoo/addons/base/models/ir_attachment.py`** -> AI Confidence: **99.31%**
283. **`odoo/addons/base/models/ir_binary.py`** -> AI Confidence: **99.31%**
284. **`odoo/addons/base/models/ir_fields.py`** -> AI Confidence: **99.31%**
285. **`odoo/addons/base/models/ir_mail_server.py`** -> AI Confidence: **99.31%**
286. **`odoo/addons/base/models/ir_model.py`** -> AI Confidence: **99.31%**
287. **`odoo/addons/base/models/ir_module.py`** -> AI Confidence: **99.31%**
288. **`odoo/addons/base/models/ir_profile.py`** -> AI Confidence: **99.31%**
289. **`odoo/addons/base/models/ir_ui_menu.py`** -> AI Confidence: **99.31%**
290. **`odoo/addons/base/models/ir_ui_view.py`** -> AI Confidence: **99.31%**
291. **`odoo/addons/base/models/res_company.py`** -> AI Confidence: **99.31%**
292. **`odoo/addons/base/models/res_currency.py`** -> AI Confidence: **99.31%**
293. **`odoo/addons/base/models/res_lang.py`** -> AI Confidence: **99.31%**
294. **`odoo/addons/base/models/res_partner.py`** -> AI Confidence: **99.31%**
295. **`odoo/addons/base/models/res_users.py`** -> AI Confidence: **99.31%**
296. **`odoo/addons/base/tests/test_expression.py`** -> AI Confidence: **99.31%**
297. **`odoo/addons/base/tests/test_ir_mail_server.py`** -> AI Confidence: **99.31%**
298. **`odoo/addons/base/tests/test_mail.py`** -> AI Confidence: **99.31%**
299. **`odoo/addons/base/tests/test_qweb.py`** -> AI Confidence: **99.31%**
300. **`odoo/addons/base/tests/test_res_partner.py`** -> AI Confidence: **99.31%**
301. **`odoo/addons/base/tests/test_res_users.py`** -> AI Confidence: **99.31%**
302. **`odoo/addons/base/wizard/base_partner_merge.py`** -> AI Confidence: **99.31%**
303. **`odoo/addons/test_lint/tests/_odoo_checker_sql_injection.py`** -> AI Confidence: **99.31%**
304. **`odoo/addons/test_lint/tests/test_checkers.py`** -> AI Confidence: **99.31%**
305. **`odoo/addons/test_lint/tests/test_docstring.py`** -> AI Confidence: **99.31%**
306. **`odoo/cli/command.py`** -> AI Confidence: **99.31%**
307. **`odoo/cli/db.py`** -> AI Confidence: **99.31%**
308. **`odoo/cli/i18n.py`** -> AI Confidence: **99.31%**
309. **`odoo/cli/obfuscate.py`** -> AI Confidence: **99.31%**
310. **`odoo/netsvc.py`** -> AI Confidence: **99.31%**
311. **`odoo/orm/domains.py`** -> AI Confidence: **99.31%**
312. **`odoo/orm/fields.py`** -> AI Confidence: **99.31%**
313. **`odoo/orm/fields_binary.py`** -> AI Confidence: **99.31%**
314. **`odoo/orm/fields_properties.py`** -> AI Confidence: **99.31%**
315. **`odoo/orm/fields_relational.py`** -> AI Confidence: **99.31%**
316. **`odoo/orm/fields_selection.py`** -> AI Confidence: **99.31%**
317. **`odoo/orm/fields_textual.py`** -> AI Confidence: **99.31%**
318. **`odoo/orm/model_classes.py`** -> AI Confidence: **99.31%**
319. **`odoo/orm/models.py`** -> AI Confidence: **99.31%**
320. **`odoo/orm/registry.py`** -> AI Confidence: **99.31%**
321. **`odoo/osv/expression.py`** -> AI Confidence: **99.31%**
322. **`odoo/service/model.py`** -> AI Confidence: **99.31%**
323. **`odoo/service/server.py`** -> AI Confidence: **99.31%**
324. **`odoo/tests/form.py`** -> AI Confidence: **99.31%**
325. **`odoo/tests/result.py`** -> AI Confidence: **99.31%**
326. **`odoo/tests/test_module_operations.py`** -> AI Confidence: **99.31%**
327. **`odoo/tools/_vendor/send_file.py`** -> AI Confidence: **99.31%**
328. **`odoo/tools/appdirs.py`** -> AI Confidence: **99.31%**
329. **`odoo/tools/babel/javascript_extractor.py`** -> AI Confidence: **99.31%**
330. **`odoo/tools/cloc.py`** -> AI Confidence: **99.31%**
331. **`odoo/tools/config.py`** -> AI Confidence: **99.31%**
332. **`odoo/tools/convert.py`** -> AI Confidence: **99.31%**
333. **`odoo/tools/date_utils.py`** -> AI Confidence: **99.31%**
334. **`odoo/tools/image.py`** -> AI Confidence: **99.31%**
335. **`odoo/tools/mail.py`** -> AI Confidence: **99.31%**
336. **`odoo/tools/mimetypes.py`** -> AI Confidence: **99.31%**
337. **`odoo/tools/osutil.py`** -> AI Confidence: **99.31%**
338. **`odoo/tools/profiler.py`** -> AI Confidence: **99.31%**
339. **`odoo/tools/test_reports.py`** -> AI Confidence: **99.31%**
340. **`odoo/tools/translate.py`** -> AI Confidence: **99.31%**
341. **`odoo/tools/view_validation.py`** -> AI Confidence: **99.31%**
342. **`odoo/tools/xml_utils.py`** -> AI Confidence: **99.31%**
343. **`odoo/upgrade_code/18.1-00-sql-constraint.py`** -> AI Confidence: **99.31%**
344. **`odoo/upgrade_code/18.2-00-l10n-translate.py`** -> AI Confidence: **99.31%**
345. **`odoo/upgrade_code/18.5-00-domain-dynamic-dates.py`** -> AI Confidence: **99.31%**
346. **`odoo/upgrade_code/18.5-00-no-tax-tag-invert.py`** -> AI Confidence: **99.31%**
347. **`setup/requirements-check.py`** -> AI Confidence: **99.31%**
348. **`addons/analytic/static/src/components/analytic_distribution/analytic_distribution.js`** -> AI Confidence: **99.31%**
349. **`addons/api_doc/static/src/components/doc_model.js`** -> AI Confidence: **99.31%**
350. **`addons/auth_totp_portal/static/src/interactions/totp_enable.js`** -> AI Confidence: **99.31%**
351. **`addons/base_import/static/src/import_action/import_action.js`** -> AI Confidence: **99.31%**
352. **`addons/base_import/static/src/import_model.js`** -> AI Confidence: **99.31%**
353. **`addons/hr_attendance/static/src/public_kiosk/public_kiosk_app.js`** -> AI Confidence: **99.31%**
354. **`addons/html_builder/static/src/core/builder_options_plugin.js`** -> AI Confidence: **99.31%**
355. **`addons/html_builder/static/src/core/building_blocks/builder_number_input.js`** -> AI Confidence: **99.31%**
356. **`addons/html_builder/static/src/core/building_blocks/builder_row.js`** -> AI Confidence: **99.31%**
357. **`addons/html_builder/static/src/core/drag_and_drop_plugin.js`** -> AI Confidence: **99.31%**
358. **`addons/html_builder/static/src/core/grid_layout/grid_layout_plugin.js`** -> AI Confidence: **99.31%**
359. **`addons/html_builder/static/src/core/move_plugin.js`** -> AI Confidence: **99.31%**
360. **`addons/html_builder/static/src/plugins/image/image_format_option_plugin.js`** -> AI Confidence: **99.31%**
361. **`addons/html_builder/static/src/plugins/image/image_shape_option_plugin.js`** -> AI Confidence: **99.31%**
362. **`addons/html_builder/static/src/plugins/layout_column_option_plugin.js`** -> AI Confidence: **99.31%**
363. **`addons/html_editor/static/src/components/html_viewer/html_viewer.js`** -> AI Confidence: **99.31%**
364. **`addons/html_editor/static/src/core/base_container_plugin.js`** -> AI Confidence: **99.31%**
365. **`addons/html_editor/static/src/core/clipboard_plugin.js`** -> AI Confidence: **99.31%**
366. **`addons/html_editor/static/src/core/delete_plugin.js`** -> AI Confidence: **99.31%**
367. **`addons/html_editor/static/src/core/format_plugin.js`** -> AI Confidence: **99.31%**
368. **`addons/html_editor/static/src/core/history_plugin.js`** -> AI Confidence: **99.31%**
369. **`addons/html_editor/static/src/core/line_break_plugin.js`** -> AI Confidence: **99.31%**
370. **`addons/html_editor/static/src/core/selection_plugin.js`** -> AI Confidence: **99.31%**
371. **`addons/html_editor/static/src/core/split_plugin.js`** -> AI Confidence: **99.31%**
372. **`addons/html_editor/static/src/editor.js`** -> AI Confidence: **99.31%**
373. **`addons/html_editor/static/src/fields/html_field.js`** -> AI Confidence: **99.31%**
374. **`addons/html_editor/static/src/main/font/color_plugin.js`** -> AI Confidence: **99.31%**
375. **`addons/html_editor/static/src/main/font/font_plugin.js`** -> AI Confidence: **99.31%**
376. **`addons/html_editor/static/src/main/font/font_size_selector.js`** -> AI Confidence: **99.31%**
377. **`addons/html_editor/static/src/main/hint_plugin.js`** -> AI Confidence: **99.31%**
378. **`addons/html_editor/static/src/main/inline_code.js`** -> AI Confidence: **99.31%**
379. **`addons/html_editor/static/src/main/link/link_popover.js`** -> AI Confidence: **99.31%**
380. **`addons/html_editor/static/src/main/list/list_plugin.js`** -> AI Confidence: **99.31%**
381. **`addons/html_editor/static/src/main/media/file_plugin.js`** -> AI Confidence: **99.31%**
382. **`addons/html_editor/static/src/main/media/media_dialog/media_dialog.js`** -> AI Confidence: **99.31%**
383. **`addons/html_editor/static/src/main/media/media_plugin.js`** -> AI Confidence: **99.31%**
384. **`addons/html_editor/static/src/main/movenode_plugin.js`** -> AI Confidence: **99.31%**
385. **`addons/html_editor/static/src/main/table/table_plugin.js`** -> AI Confidence: **99.31%**
386. **`addons/html_editor/static/src/main/tabulation_plugin.js`** -> AI Confidence: **99.31%**
387. **`addons/html_editor/static/src/main/text_direction_plugin.js`** -> AI Confidence: **99.31%**
388. **`addons/html_editor/static/src/others/collaboration/collaboration_odoo_plugin.js`** -> AI Confidence: **99.31%**
389. **`addons/html_editor/static/src/others/collaboration/collaboration_selection_avatar_plugin.js`** -> AI Confidence: **99.31%**
390. **`addons/html_editor/static/src/others/collaboration/collaboration_selection_plugin.js`** -> AI Confidence: **99.31%**
391. **`addons/html_editor/static/src/others/embedded_component_plugin.js`** -> AI Confidence: **99.31%**
392. **`addons/html_editor/static/src/others/embedded_components/plugins/caption_plugin/caption_plugin.js`** -> AI Confidence: **99.31%**
393. **`addons/html_editor/static/src/others/embedded_components/plugins/toggle_block_plugin/toggle_block_plugin.js`** -> AI Confidence: **99.31%**
394. **`addons/html_editor/static/src/others/qweb_plugin.js`** -> AI Confidence: **99.31%**
395. **`addons/html_editor/static/src/utils/dom.js`** -> AI Confidence: **99.31%**
396. **`addons/html_editor/static/src/utils/selection.js`** -> AI Confidence: **99.31%**
397. **`addons/html_editor/static/tests/_helpers/collaboration.js`** -> AI Confidence: **99.31%**
398. **`addons/im_livechat/static/src/embed/common/thread_model_patch.js`** -> AI Confidence: **99.31%**
399. **`addons/im_livechat/static/src/embed/cors/boot.js`** -> AI Confidence: **99.31%**
400. **`addons/mail/static/src/chatter/web/chatter_patch.js`** -> AI Confidence: **99.31%**
401. **`addons/mail/static/src/chatter/web_portal/chatter.js`** -> AI Confidence: **99.31%**
402. **`addons/mail/static/src/core/common/action.js`** -> AI Confidence: **99.31%**
403. **`addons/mail/static/src/core/common/composer.js`** -> AI Confidence: **99.31%**
404. **`addons/mail/static/src/core/common/message.js`** -> AI Confidence: **99.31%**
405. **`addons/mail/static/src/core/common/message_card_list.js`** -> AI Confidence: **99.31%**
406. **`addons/mail/static/src/core/common/message_model.js`** -> AI Confidence: **99.31%**
407. **`addons/mail/static/src/core/common/navigable_list.js`** -> AI Confidence: **99.31%**
408. **`addons/mail/static/src/core/common/notification_permission_service.js`** -> AI Confidence: **99.31%**
409. **`addons/mail/static/src/core/common/settings_model.js`** -> AI Confidence: **99.31%**
410. **`addons/mail/static/src/core/common/store_service.js`** -> AI Confidence: **99.31%**
411. **`addons/mail/static/src/core/common/suggestion_hook.js`** -> AI Confidence: **99.31%**
412. **`addons/mail/static/src/core/common/suggestion_service.js`** -> AI Confidence: **99.31%**
413. **`addons/mail/static/src/core/common/thread.js`** -> AI Confidence: **99.31%**
414. **`addons/mail/static/src/core/public_web/messaging_menu.js`** -> AI Confidence: **99.31%**
415. **`addons/mail/static/src/core/web/messaging_menu_patch.js`** -> AI Confidence: **99.31%**
416. **`addons/mail/static/src/discuss/call/common/call_actions.js`** -> AI Confidence: **99.31%**
417. **`addons/mail/static/src/discuss/call/common/call_participant_card.js`** -> AI Confidence: **99.31%**
418. **`addons/mail/static/src/discuss/call/common/call_preview.js`** -> AI Confidence: **99.31%**
419. **`addons/mail/static/src/discuss/call/common/rtc_service.js`** -> AI Confidence: **99.31%**
420. **`addons/mail/static/src/discuss/core/common/channel_invitation.js`** -> AI Confidence: **99.31%**
421. **`addons/mail/static/src/discuss/core/common/thread_actions.js`** -> AI Confidence: **99.31%**
422. **`addons/mail/static/src/discuss/core/common/thread_model_patch.js`** -> AI Confidence: **99.31%**
423. **`addons/mail/static/src/discuss/core/public_web/discuss_command_palette.js`** -> AI Confidence: **99.31%**
424. **`addons/mail/static/src/discuss/core/public_web/discuss_core_public_web_service.js`** -> AI Confidence: **99.31%**
425. **`addons/mail/static/src/discuss/core/public_web/thread_actions.js`** -> AI Confidence: **99.31%**
426. **`addons/mail/static/src/discuss/gif_picker/common/gif_picker.js`** -> AI Confidence: **99.31%**
427. **`addons/mail/static/src/model/make_store.js`** -> AI Confidence: **99.31%**
428. **`addons/mail/static/src/model/record.js`** -> AI Confidence: **99.31%**
429. **`addons/mail/static/src/views/web/activity/activity_cell.js`** -> AI Confidence: **99.31%**
430. **`addons/mail/static/tests/mock_server/mail_mock_server.js`** -> AI Confidence: **99.31%**
431. **`addons/mail/static/tests/mock_server/mock_models/discuss_channel.js`** -> AI Confidence: **99.31%**
432. **`addons/mass_mailing/static/src/builder/plugins/customize_mailing_plugin.js`** -> AI Confidence: **99.31%**
433. **`addons/mass_mailing/static/src/js/mailing_m2o_filter.js`** -> AI Confidence: **99.31%**
434. **`addons/payment/static/src/interactions/payment_form.js`** -> AI Confidence: **99.31%**
435. **`addons/point_of_sale/static/src/app/components/navbar/navbar.js`** -> AI Confidence: **99.31%**
436. **`addons/point_of_sale/static/src/app/models/related_models/index.js`** -> AI Confidence: **99.31%**
437. **`addons/point_of_sale/static/src/app/screens/partner_list/partner_list.js`** -> AI Confidence: **99.31%**
438. **`addons/point_of_sale/static/src/app/screens/payment_screen/payment_screen.js`** -> AI Confidence: **99.31%**
439. **`addons/point_of_sale/static/src/app/screens/product_screen/order_summary/order_summary.js`** -> AI Confidence: **99.31%**
440. **`addons/point_of_sale/static/src/app/screens/ticket_screen/ticket_screen.js`** -> AI Confidence: **99.31%**
441. **`addons/point_of_sale/static/src/app/services/barcode_reader_service.js`** -> AI Confidence: **99.31%**
442. **`addons/point_of_sale/static/src/app/services/data_service.js`** -> AI Confidence: **99.31%**
443. **`addons/point_of_sale/static/src/app/services/pos_store.js`** -> AI Confidence: **99.31%**
444. **`addons/pos_dpopay/static/src/app/utils/payment/payment_dpopay.js`** -> AI Confidence: **99.31%**
445. **`addons/pos_event/static/src/app/components/popup/event_configurator_popup/event_configurator_popup.js`** -> AI Confidence: **99.31%**
446. **`addons/pos_hr/static/src/app/utils/select_cashier_mixin.js`** -> AI Confidence: **99.31%**
447. **`addons/pos_loyalty/static/src/app/screens/product_screen/order_summary/order_summary.js`** -> AI Confidence: **99.31%**
448. **`addons/pos_loyalty/static/src/app/services/pos_store.js`** -> AI Confidence: **99.31%**
449. **`addons/pos_online_payment/static/src/app/utils/order_payment_validation.js`** -> AI Confidence: **99.31%**
450. **`addons/pos_pine_labs/static/src/app/utils/payment/payment_pine_labs.js`** -> AI Confidence: **99.31%**
451. **`addons/pos_restaurant/static/src/app/services/pos_store.js`** -> AI Confidence: **99.31%**
452. **`addons/pos_sale/static/src/app/services/pos_store.js`** -> AI Confidence: **99.31%**
453. **`addons/pos_self_order/static/src/app/pages/cart_page/cart_page.js`** -> AI Confidence: **99.31%**
454. **`addons/pos_self_order/static/src/app/pages/combo_page/combo_page.js`** -> AI Confidence: **99.31%**
455. **`addons/pos_self_order/static/src/app/pages/confirmation_page/confirmation_page.js`** -> AI Confidence: **99.31%**
456. **`addons/pos_self_order/static/src/app/pages/product_list_page/product_list_page.js`** -> AI Confidence: **99.31%**
457. **`addons/pos_self_order/static/src/app/services/self_order_service.js`** -> AI Confidence: **99.31%**
458. **`addons/spreadsheet/static/src/global_filters/components/filter_value/filter_value.js`** -> AI Confidence: **99.31%**
459. **`addons/spreadsheet/static/src/global_filters/helpers.js`** -> AI Confidence: **99.31%**
460. **`addons/spreadsheet/static/src/global_filters/plugins/global_filters_core_view_plugin.js`** -> AI Confidence: **99.31%**
461. **`addons/spreadsheet/static/src/list/list_data_source.js`** -> AI Confidence: **99.31%**
462. **`addons/spreadsheet/static/src/list/plugins/list_core_view_plugin.js`** -> AI Confidence: **99.31%**
463. **`addons/spreadsheet/static/src/pivot/pivot_model.js`** -> AI Confidence: **99.31%**
464. **`addons/spreadsheet_dashboard/static/src/bundle/dashboard_action/dashboard_search_bar/dashboard_search_bar.js`** -> AI Confidence: **99.31%**
465. **`addons/stock/static/src/client_actions/stock_traceability_report_backend.js`** -> AI Confidence: **99.31%**
466. **`addons/web/static/src/core/autocomplete/autocomplete.js`** -> AI Confidence: **99.31%**
467. **`addons/web/static/src/core/barcode/barcode_video_scanner.js`** -> AI Confidence: **99.31%**
468. **`addons/web/static/src/core/bottom_sheet/bottom_sheet.js`** -> AI Confidence: **99.31%**
469. **`addons/web/static/src/core/browser/router.js`** -> AI Confidence: **99.31%**
470. **`addons/web/static/src/core/color_picker/color_picker.js`** -> AI Confidence: **99.31%**
471. **`addons/web/static/src/core/color_picker/custom_color_picker/custom_color_picker.js`** -> AI Confidence: **99.31%**
472. **`addons/web/static/src/core/commands/command_palette.js`** -> AI Confidence: **99.31%**
473. **`addons/web/static/src/core/datetime/datetimepicker_service.js`** -> AI Confidence: **99.31%**
474. **`addons/web/static/src/core/dropdown/dropdown.js`** -> AI Confidence: **99.31%**
475. **`addons/web/static/src/core/emoji_picker/emoji_picker.js`** -> AI Confidence: **99.31%**
476. **`addons/web/static/src/core/errors/error_handlers.js`** -> AI Confidence: **99.31%**
477. **`addons/web/static/src/core/expression_editor_dialog/expression_editor_dialog.js`** -> AI Confidence: **99.31%**
478. **`addons/web/static/src/core/model_field_selector/model_field_selector_popover.js`** -> AI Confidence: **99.31%**
479. **`addons/web/static/src/core/navigation/navigation.js`** -> AI Confidence: **99.31%**
480. **`addons/web/static/src/core/popover/popover.js`** -> AI Confidence: **99.31%**
481. **`addons/web/static/src/core/select_menu/select_menu.js`** -> AI Confidence: **99.31%**
482. **`addons/web/static/src/core/time_picker/time_picker.js`** -> AI Confidence: **99.31%**
483. **`addons/web/static/src/core/tree_editor/tree_editor_value_editors.js`** -> AI Confidence: **99.31%**
484. **`addons/web/static/src/core/tree_editor/tree_processor.js`** -> AI Confidence: **99.31%**
485. **`addons/web/static/src/core/utils/draggable_hook_builder.js`** -> AI Confidence: **99.31%**
486. **`addons/web/static/src/model/relational_model/record.js`** -> AI Confidence: **99.31%**
487. **`addons/web/static/src/model/relational_model/relational_model.js`** -> AI Confidence: **99.31%**
488. **`addons/web/static/src/model/relational_model/static_list.js`** -> AI Confidence: **99.31%**
489. **`addons/web/static/src/model/relational_model/utils.js`** -> AI Confidence: **99.31%**
490. **`addons/web/static/src/search/control_panel/control_panel.js`** -> AI Confidence: **99.31%**
491. **`addons/web/static/src/search/search_bar/search_bar.js`** -> AI Confidence: **99.31%**
492. **`addons/web/static/src/search/search_model.js`** -> AI Confidence: **99.31%**
493. **`addons/web/static/src/views/calendar/calendar_common/calendar_common_renderer.js`** -> AI Confidence: **99.31%**
494. **`addons/web/static/src/views/calendar/calendar_model.js`** -> AI Confidence: **99.31%**
495. **`addons/web/static/src/views/fields/datetime/datetime_field.js`** -> AI Confidence: **99.31%**
496. **`addons/web/static/src/views/fields/field.js`** -> AI Confidence: **99.31%**
497. **`addons/web/static/src/views/fields/image/image_field.js`** -> AI Confidence: **99.31%**
498. **`addons/web/static/src/views/fields/properties/properties_field.js`** -> AI Confidence: **99.31%**
499. **`addons/web/static/src/views/fields/properties/property_definition.js`** -> AI Confidence: **99.31%**
500. **`addons/web/static/src/views/fields/properties/property_value.js`** -> AI Confidence: **99.31%**
501. **`addons/web/static/src/views/fields/signature/signature_field.js`** -> AI Confidence: **99.31%**
502. **`addons/web/static/src/views/form/form_compiler.js`** -> AI Confidence: **99.31%**
503. **`addons/web/static/src/views/graph/graph_model.js`** -> AI Confidence: **99.31%**
504. **`addons/web/static/src/views/graph/graph_renderer.js`** -> AI Confidence: **99.31%**
505. **`addons/web/static/src/views/kanban/kanban_record.js`** -> AI Confidence: **99.31%**
506. **`addons/web/static/src/views/list/list_arch_parser.js`** -> AI Confidence: **99.31%**
507. **`addons/web/static/src/views/pivot/pivot_model.js`** -> AI Confidence: **99.31%**
508. **`addons/web/static/src/views/pivot/pivot_renderer.js`** -> AI Confidence: **99.31%**
509. **`addons/web/static/src/views/view.js`** -> AI Confidence: **99.31%**
510. **`addons/web/static/src/webclient/actions/action_service.js`** -> AI Confidence: **99.31%**
511. **`addons/web/static/src/webclient/webclient.js`** -> AI Confidence: **99.31%**
512. **`addons/web/static/tests/_framework/mock_server/mock_server.js`** -> AI Confidence: **99.31%**
513. **`addons/web/static/tests/legacy/helpers/mock_server.js`** -> AI Confidence: **99.31%**
514. **`addons/web/static/tests/legacy/helpers/utils.js`** -> AI Confidence: **99.31%**
515. **`addons/web_hierarchy/static/src/hierarchy_model.js`** -> AI Confidence: **99.31%**
516. **`addons/web_tour/static/src/js/tour_automatic/tour_step_automatic.js`** -> AI Confidence: **99.31%**
517. **`addons/web_tour/static/src/js/tour_interactive/tour_interactive.js`** -> AI Confidence: **99.31%**
518. **`addons/web_tour/static/src/js/tour_service.js`** -> AI Confidence: **99.31%**
519. **`addons/website/static/src/builder/plugins/options/cover_properties_option_plugin.js`** -> AI Confidence: **99.31%**
520. **`addons/website/static/src/builder/plugins/options/facebook_option_plugin.js`** -> AI Confidence: **99.31%**
521. **`addons/website/static/src/builder/plugins/options/gallery_element_option_plugin.js`** -> AI Confidence: **99.31%**
522. **`addons/website/static/src/builder/plugins/options/navtabs_style_option_plugin.js`** -> AI Confidence: **99.31%**
523. **`addons/website/static/src/builder/plugins/options/parallax_option_plugin.js`** -> AI Confidence: **99.31%**
524. **`addons/website/static/src/builder/plugins/translation_plugin.js`** -> AI Confidence: **99.31%**
525. **`addons/website/static/src/builder/plugins/translation_tab/customize_translation_tab_plugin.js`** -> AI Confidence: **99.31%**
526. **`addons/website/static/src/client_actions/website_preview/edit_website_systray_item.js`** -> AI Confidence: **99.31%**
527. **`addons/website/static/src/components/dialog/add_page_dialog.js`** -> AI Confidence: **99.31%**
528. **`addons/website/static/src/components/dialog/edit_menu.js`** -> AI Confidence: **99.31%**
529. **`addons/website/static/src/components/resource_editor/resource_editor.js`** -> AI Confidence: **99.31%**
530. **`addons/website/static/src/interactions/popup/popup.js`** -> AI Confidence: **99.31%**
531. **`addons/website/static/src/snippets/s_website_form/form.js`** -> AI Confidence: **99.31%**
532. **`addons/website_event_track/static/src/interactions/event_track_reminder.js`** -> AI Confidence: **99.31%**
533. **`addons/website_forum/static/src/interactions/website_forum.js`** -> AI Confidence: **99.31%**
534. **`addons/website_links/static/src/interactions/website_links.js`** -> AI Confidence: **99.31%**
535. **`addons/website_sale/static/src/interactions/website_sale.js`** -> AI Confidence: **99.31%**
536. **`addons/website_sale/static/src/js/variant_mixin.js`** -> AI Confidence: **99.31%**
537. **`addons/website_slides/static/src/js/public/components/slide_upload_dialog/slide_upload_category.js`** -> AI Confidence: **99.31%**
538. **`addons/website_slides/static/src/js/slides_course_fullscreen_player.js`** -> AI Confidence: **99.31%**
539. **`addons/website_slides/static/src/js/slides_course_quiz.js`** -> AI Confidence: **99.31%**
540. **`addons/account_add_gln/__manifest__.py`** -> AI Confidence: **99.29%**
541. **`addons/account_edi_proxy_client/__manifest__.py`** -> AI Confidence: **99.29%**
542. **`addons/account_edi_ubl_cii/__manifest__.py`** -> AI Confidence: **99.29%**
543. **`addons/account_fleet/__manifest__.py`** -> AI Confidence: **99.29%**
544. **`addons/account_payment/__manifest__.py`** -> AI Confidence: **99.29%**
545. **`addons/account_peppol/__manifest__.py`** -> AI Confidence: **99.29%**
546. **`addons/attachment_indexation/__manifest__.py`** -> AI Confidence: **99.29%**
547. **`addons/auth_passkey/__manifest__.py`** -> AI Confidence: **99.29%**
548. **`addons/auth_passkey_portal/__manifest__.py`** -> AI Confidence: **99.29%**
549. **`addons/auth_password_policy_portal/__manifest__.py`** -> AI Confidence: **99.29%**
550. **`addons/auth_password_policy_signup/__manifest__.py`** -> AI Confidence: **99.29%**
551. **`addons/barcodes/__manifest__.py`** -> AI Confidence: **99.29%**
552. **`addons/crm/__manifest__.py`** -> AI Confidence: **99.29%**
553. **`addons/data_recycle/__manifest__.py`** -> AI Confidence: **99.29%**
554. **`addons/event_crm_sale/__manifest__.py`** -> AI Confidence: **99.29%**
555. **`addons/fleet/__manifest__.py`** -> AI Confidence: **99.29%**
556. **`addons/google_address_autocomplete/__manifest__.py`** -> AI Confidence: **99.29%**
557. **`addons/google_gmail/__manifest__.py`** -> AI Confidence: **99.29%**
558. **`addons/hr_expense/__manifest__.py`** -> AI Confidence: **99.29%**
559. **`addons/hr_holidays/__manifest__.py`** -> AI Confidence: **99.29%**
560. **`addons/hr_holidays_homeworking/__manifest__.py`** -> AI Confidence: **99.29%**
561. **`addons/hr_homeworking_calendar/__manifest__.py`** -> AI Confidence: **99.29%**
562. **`addons/hr_skills/__manifest__.py`** -> AI Confidence: **99.29%**
563. **`addons/iap/__manifest__.py`** -> AI Confidence: **99.29%**
564. **`addons/im_livechat/__manifest__.py`** -> AI Confidence: **99.29%**
565. **`addons/iot_box_image/__manifest__.py`** -> AI Confidence: **99.29%**
566. **`addons/l10n_account_edi_ubl_cii_tests/__manifest__.py`** -> AI Confidence: **99.29%**
567. **`addons/l10n_ar_pos/__manifest__.py`** -> AI Confidence: **99.29%**
568. **`addons/l10n_be_pos_sale/__manifest__.py`** -> AI Confidence: **99.29%**
569. **`addons/l10n_br_sales/__manifest__.py`** -> AI Confidence: **99.29%**
570. **`addons/l10n_br_website_sale/__manifest__.py`** -> AI Confidence: **99.29%**
571. **`addons/l10n_dk_nemhandel/__manifest__.py`** -> AI Confidence: **99.29%**
572. **`addons/l10n_es_edi_verifactu/__manifest__.py`** -> AI Confidence: **99.29%**
573. **`addons/l10n_es_edi_verifactu_pos/__manifest__.py`** -> AI Confidence: **99.29%**
574. **`addons/l10n_fr_facturx_chorus_pro/__manifest__.py`** -> AI Confidence: **99.29%**
575. **`addons/l10n_fr_hr_holidays/__manifest__.py`** -> AI Confidence: **99.29%**
576. **`addons/l10n_fr_hr_work_entry_holidays/__manifest__.py`** -> AI Confidence: **99.29%**
577. **`addons/l10n_fr_pos_cert/__manifest__.py`** -> AI Confidence: **99.29%**
578. **`addons/l10n_gr_edi/models/preferred_classification.py`** -> AI Confidence: **99.29%**
579. **`addons/l10n_hk/__manifest__.py`** -> AI Confidence: **99.29%**
580. **`addons/l10n_id/migrations/1.3/end-migrate_update_taxes.py`** -> AI Confidence: **99.29%**
581. **`addons/l10n_id_efaktur_coretax/models/account_move.py`** -> AI Confidence: **99.29%**
582. **`addons/l10n_in_edi/tests/test_edi_json.py`** -> AI Confidence: **99.29%**
583. **`addons/l10n_it_edi_sale/__manifest__.py`** -> AI Confidence: **99.29%**
584. **`addons/l10n_jo_edi/__manifest__.py`** -> AI Confidence: **99.29%**
585. **`addons/l10n_jo_edi_pos/__manifest__.py`** -> AI Confidence: **99.29%**
586. **`addons/l10n_latam_check/__manifest__.py`** -> AI Confidence: **99.29%**
587. **`addons/l10n_lk/__manifest__.py`** -> AI Confidence: **99.29%**
588. **`addons/l10n_my_edi/models/product_template.py`** -> AI Confidence: **99.29%**
589. **`addons/l10n_pe_pos/__manifest__.py`** -> AI Confidence: **99.29%**
590. **`addons/l10n_ph/__manifest__.py`** -> AI Confidence: **99.29%**
591. **`addons/l10n_pl_edi/__manifest__.py`** -> AI Confidence: **99.29%**
592. **`addons/l10n_ro/migrations/1.1/pre-migrate.py`** -> AI Confidence: **99.29%**
593. **`addons/l10n_ro_edi/__manifest__.py`** -> AI Confidence: **99.29%**
594. **`addons/l10n_rs_edi/__manifest__.py`** -> AI Confidence: **99.29%**
595. **`addons/l10n_tr/__manifest__.py`** -> AI Confidence: **99.29%**
596. **`addons/l10n_tr_nilvera_base_vat/__manifest__.py`** -> AI Confidence: **99.29%**
597. **`addons/loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
598. **`addons/mail/__manifest__.py`** -> AI Confidence: **99.29%**
599. **`addons/maintenance/__manifest__.py`** -> AI Confidence: **99.29%**
600. **`addons/mass_mailing/__manifest__.py`** -> AI Confidence: **99.29%**
601. **`addons/mass_mailing_sms/__manifest__.py`** -> AI Confidence: **99.29%**
602. **`addons/microsoft_outlook/__manifest__.py`** -> AI Confidence: **99.29%**
603. **`addons/mrp_subcontracting_account/__manifest__.py`** -> AI Confidence: **99.29%**
604. **`addons/mrp_subcontracting_dropshipping/__manifest__.py`** -> AI Confidence: **99.29%**
605. **`addons/mrp_subcontracting_landed_costs/__manifest__.py`** -> AI Confidence: **99.29%**
606. **`addons/mrp_subcontracting_purchase/__manifest__.py`** -> AI Confidence: **99.29%**
607. **`addons/payment_adyen/__manifest__.py`** -> AI Confidence: **99.29%**
608. **`addons/payment_authorize/__manifest__.py`** -> AI Confidence: **99.29%**
609. **`addons/payment_custom/__manifest__.py`** -> AI Confidence: **99.29%**
610. **`addons/payment_demo/__manifest__.py`** -> AI Confidence: **99.29%**
611. **`addons/payment_paymob/__manifest__.py`** -> AI Confidence: **99.29%**
612. **`addons/payment_paypal/__manifest__.py`** -> AI Confidence: **99.29%**
613. **`addons/payment_redsys/const.py`** -> AI Confidence: **99.29%**
614. **`addons/payment_stripe/__manifest__.py`** -> AI Confidence: **99.29%**
615. **`addons/payment_xendit/__manifest__.py`** -> AI Confidence: **99.29%**
616. **`addons/payment_xendit/const.py`** -> AI Confidence: **99.29%**
617. **`addons/phone_validation/__manifest__.py`** -> AI Confidence: **99.29%**
618. **`addons/point_of_sale/__manifest__.py`** -> AI Confidence: **99.29%**
619. **`addons/pos_adyen/__manifest__.py`** -> AI Confidence: **99.29%**
620. **`addons/pos_cashdro/__manifest__.py`** -> AI Confidence: **99.29%**
621. **`addons/pos_dpopay/__manifest__.py`** -> AI Confidence: **99.29%**
622. **`addons/pos_event/__manifest__.py`** -> AI Confidence: **99.29%**
623. **`addons/pos_event_sale/__manifest__.py`** -> AI Confidence: **99.29%**
624. **`addons/pos_glory_cash/__manifest__.py`** -> AI Confidence: **99.29%**
625. **`addons/pos_hr/__manifest__.py`** -> AI Confidence: **99.29%**
626. **`addons/pos_hr_restaurant/__manifest__.py`** -> AI Confidence: **99.29%**
627. **`addons/pos_loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
628. **`addons/pos_mercado_pago/__manifest__.py`** -> AI Confidence: **99.29%**
629. **`addons/pos_mollie/__manifest__.py`** -> AI Confidence: **99.29%**
630. **`addons/pos_mrp/__manifest__.py`** -> AI Confidence: **99.29%**
631. **`addons/pos_pine_labs/__manifest__.py`** -> AI Confidence: **99.29%**
632. **`addons/pos_qfpay/__manifest__.py`** -> AI Confidence: **99.29%**
633. **`addons/pos_razorpay/__manifest__.py`** -> AI Confidence: **99.29%**
634. **`addons/pos_repair/__manifest__.py`** -> AI Confidence: **99.29%**
635. **`addons/pos_restaurant/__manifest__.py`** -> AI Confidence: **99.29%**
636. **`addons/pos_restaurant_loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
637. **`addons/pos_safaricom/__manifest__.py`** -> AI Confidence: **99.29%**
638. **`addons/pos_sale/__manifest__.py`** -> AI Confidence: **99.29%**
639. **`addons/pos_sale_loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
640. **`addons/pos_sale_margin/__manifest__.py`** -> AI Confidence: **99.29%**
641. **`addons/pos_self_order/__manifest__.py`** -> AI Confidence: **99.29%**
642. **`addons/pos_self_order_adyen/__manifest__.py`** -> AI Confidence: **99.29%**
643. **`addons/pos_self_order_pine_labs/__manifest__.py`** -> AI Confidence: **99.29%**
644. **`addons/pos_self_order_qfpay/__manifest__.py`** -> AI Confidence: **99.29%**
645. **`addons/pos_self_order_razorpay/__manifest__.py`** -> AI Confidence: **99.29%**
646. **`addons/pos_self_order_stripe/__manifest__.py`** -> AI Confidence: **99.29%**
647. **`addons/pos_sms/__manifest__.py`** -> AI Confidence: **99.29%**
648. **`addons/pos_stripe/__manifest__.py`** -> AI Confidence: **99.29%**
649. **`addons/pos_viva_com/__manifest__.py`** -> AI Confidence: **99.29%**
650. **`addons/product_expiry/models/production_lot.py`** -> AI Confidence: **99.29%**
651. **`addons/project/__manifest__.py`** -> AI Confidence: **99.29%**
652. **`addons/project_purchase_stock/__manifest__.py`** -> AI Confidence: **99.29%**
653. **`addons/project_stock_account/__manifest__.py`** -> AI Confidence: **99.29%**
654. **`addons/project_todo/__manifest__.py`** -> AI Confidence: **99.29%**
655. **`addons/purchase/__manifest__.py`** -> AI Confidence: **99.29%**
656. **`addons/purchase_edi_ubl_bis3/__manifest__.py`** -> AI Confidence: **99.29%**
657. **`addons/purchase_mrp/__manifest__.py`** -> AI Confidence: **99.29%**
658. **`addons/purchase_repair/__manifest__.py`** -> AI Confidence: **99.29%**
659. **`addons/purchase_requisition_sale/__manifest__.py`** -> AI Confidence: **99.29%**
660. **`addons/purchase_stock/__manifest__.py`** -> AI Confidence: **99.29%**
661. **`addons/sale_edi_ubl/__manifest__.py`** -> AI Confidence: **99.29%**
662. **`addons/sale_loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
663. **`addons/sale_mrp/__manifest__.py`** -> AI Confidence: **99.29%**
664. **`addons/sale_purchase_stock/__manifest__.py`** -> AI Confidence: **99.29%**
665. **`addons/sale_service/__manifest__.py`** -> AI Confidence: **99.29%**
666. **`addons/sale_sms/__manifest__.py`** -> AI Confidence: **99.29%**
667. **`addons/sale_stock/__manifest__.py`** -> AI Confidence: **99.29%**
668. **`addons/sale_timesheet_margin/__manifest__.py`** -> AI Confidence: **99.29%**
669. **`addons/snailmail/country_utils.py`** -> AI Confidence: **99.29%**
670. **`addons/social_media/__manifest__.py`** -> AI Confidence: **99.29%**
671. **`addons/spreadsheet_dashboard_account/__manifest__.py`** -> AI Confidence: **99.29%**
672. **`addons/spreadsheet_dashboard_event_sale/__manifest__.py`** -> AI Confidence: **99.29%**
673. **`addons/spreadsheet_dashboard_hr_expense/__manifest__.py`** -> AI Confidence: **99.29%**
674. **`addons/spreadsheet_dashboard_hr_timesheet/__manifest__.py`** -> AI Confidence: **99.29%**
675. **`addons/spreadsheet_dashboard_im_livechat/__manifest__.py`** -> AI Confidence: **99.29%**
676. **`addons/spreadsheet_dashboard_pos_hr/__manifest__.py`** -> AI Confidence: **99.29%**
677. **`addons/spreadsheet_dashboard_pos_restaurant/__manifest__.py`** -> AI Confidence: **99.29%**
678. **`addons/spreadsheet_dashboard_sale/__manifest__.py`** -> AI Confidence: **99.29%**
679. **`addons/spreadsheet_dashboard_sale_timesheet/__manifest__.py`** -> AI Confidence: **99.29%**
680. **`addons/spreadsheet_dashboard_stock_account/__manifest__.py`** -> AI Confidence: **99.29%**
681. **`addons/spreadsheet_dashboard_website_sale/__manifest__.py`** -> AI Confidence: **99.29%**
682. **`addons/spreadsheet_dashboard_website_sale_slides/__manifest__.py`** -> AI Confidence: **99.29%**
683. **`addons/stock/__manifest__.py`** -> AI Confidence: **99.29%**
684. **`addons/stock_fleet/__manifest__.py`** -> AI Confidence: **99.29%**
685. **`addons/survey/__manifest__.py`** -> AI Confidence: **99.29%**
686. **`addons/test_discuss_full/__manifest__.py`** -> AI Confidence: **99.29%**
687. **`addons/test_mail/__manifest__.py`** -> AI Confidence: **99.29%**
688. **`addons/test_mail_full/__manifest__.py`** -> AI Confidence: **99.29%**
689. **`addons/test_mail_sms/__manifest__.py`** -> AI Confidence: **99.29%**
690. **`addons/test_mass_mailing/__manifest__.py`** -> AI Confidence: **99.29%**
691. **`addons/test_sale_product_configurators/__manifest__.py`** -> AI Confidence: **99.29%**
692. **`addons/test_website/__manifest__.py`** -> AI Confidence: **99.29%**
693. **`addons/website_crm_livechat/__manifest__.py`** -> AI Confidence: **99.29%**
694. **`addons/website_crm_partner_assign/__manifest__.py`** -> AI Confidence: **99.29%**
695. **`addons/website_crm_sms/__manifest__.py`** -> AI Confidence: **99.29%**
696. **`addons/website_event_booth_sale_exhibitor/__manifest__.py`** -> AI Confidence: **99.29%**
697. **`addons/website_event_exhibitor/__manifest__.py`** -> AI Confidence: **99.29%**
698. **`addons/website_forum/__manifest__.py`** -> AI Confidence: **99.29%**
699. **`addons/website_hr_recruitment/__manifest__.py`** -> AI Confidence: **99.29%**
700. **`addons/website_hr_recruitment_livechat/__manifest__.py`** -> AI Confidence: **99.29%**
701. **`addons/website_livechat/__manifest__.py`** -> AI Confidence: **99.29%**
702. **`addons/website_mail/__manifest__.py`** -> AI Confidence: **99.29%**
703. **`addons/website_mail_group/__manifest__.py`** -> AI Confidence: **99.29%**
704. **`addons/website_partner/__manifest__.py`** -> AI Confidence: **99.29%**
705. **`addons/website_payment/__manifest__.py`** -> AI Confidence: **99.29%**
706. **`addons/website_profile/__manifest__.py`** -> AI Confidence: **99.29%**
707. **`addons/website_sale_autocomplete/__manifest__.py`** -> AI Confidence: **99.29%**
708. **`addons/website_sale_collect_wishlist/__manifest__.py`** -> AI Confidence: **99.29%**
709. **`addons/website_sale_comparison_wishlist/__manifest__.py`** -> AI Confidence: **99.29%**
710. **`addons/website_sale_loyalty/__manifest__.py`** -> AI Confidence: **99.29%**
711. **`addons/website_sale_mass_mailing/__manifest__.py`** -> AI Confidence: **99.29%**
712. **`addons/website_slides/__manifest__.py`** -> AI Confidence: **99.29%**
713. **`odoo/addons/test_access_rights/__manifest__.py`** -> AI Confidence: **99.29%**
714. **`odoo/addons/test_convert/__manifest__.py`** -> AI Confidence: **99.29%**
715. **`odoo/addons/test_read_group/__manifest__.py`** -> AI Confidence: **99.29%**
716. **`odoo/addons/test_search_panel/__manifest__.py`** -> AI Confidence: **99.29%**
717. **`odoo/release.py`** -> AI Confidence: **99.29%**
718. **`odoo/upgrade_code/18.3-00-l10n-fiscal-position-taxes.py`** -> AI Confidence: **99.29%**
719. **`addons/html_editor/static/src/utils/regex.js`** -> AI Confidence: **99.29%**
720. **`addons/html_editor/static/tests/utils/regex.test.js`** -> AI Confidence: **99.29%**
721. **`addons/mail/push-to-talk-extension/content.js`** -> AI Confidence: **99.29%**
722. **`addons/mail/static/src/model/model_internal.js`** -> AI Confidence: **99.29%**
723. **`addons/mrp/static/src/components/mo_overview_line/mo_overview_colors.js`** -> AI Confidence: **99.29%**
724. **`addons/point_of_sale/static/src/app/models/related_models/model_defs.js`** -> AI Confidence: **99.29%**
725. **`addons/point_of_sale/static/src/app/models/related_models/serialization.js`** -> AI Confidence: **99.29%**
726. **`addons/sale_timesheet/static/tests/tours/sale_timesheet_tour.js`** -> AI Confidence: **99.29%**
727. **`addons/survey/static/tests/tours/survey.js`** -> AI Confidence: **99.29%**
728. **`addons/survey/static/tests/tours/survey_prefill.js`** -> AI Confidence: **99.29%**
729. **`addons/test_website/static/tests/tours/error_views.js`** -> AI Confidence: **99.29%**
730. **`addons/web/static/src/public/database_manager.js`** -> AI Confidence: **99.29%**
731. **`addons/account_edi_proxy_client/data/neutralize.sql`** -> AI Confidence: **99.29%**
732. **`addons/base_vat/data/neutralize.sql`** -> AI Confidence: **99.29%**
733. **`addons/delivery/data/neutralize.sql`** -> AI Confidence: **99.29%**
734. **`addons/google_address_autocomplete/data/neutralize.sql`** -> AI Confidence: **99.29%**
735. **`addons/google_recaptcha/data/neutralize.sql`** -> AI Confidence: **99.29%**
736. **`addons/iap/data/neutralize.sql`** -> AI Confidence: **99.29%**
737. **`addons/l10n_dk_nemhandel/data/neutralize.sql`** -> AI Confidence: **99.29%**
738. **`addons/l10n_hu_edi/data/neutralize.sql`** -> AI Confidence: **99.29%**
739. **`addons/l10n_my_edi/data/neutralize.sql`** -> AI Confidence: **99.29%**
740. **`addons/payment/data/neutralize.sql`** -> AI Confidence: **99.29%**
741. **`addons/pos_mercado_pago/data/neutralize.sql`** -> AI Confidence: **99.29%**
742. **`addons/web/data/neutralize.sql`** -> AI Confidence: **99.29%**
743. **`addons/website/data/neutralize.sql`** -> AI Confidence: **99.29%**
744. **`addons/website_cf_turnstile/data/neutralize.sql`** -> AI Confidence: **99.29%**
745. **`addons/iot_box_image/configuration/led_manager.sh`** -> AI Confidence: **99.29%**
746. **`addons/iot_box_image/configuration/setup_ramdisks.sh`** -> AI Confidence: **99.29%**
747. **`setup/debinstall.sh`** -> AI Confidence: **99.29%**
748. **`debian/rules`** -> AI Confidence: **99.29%**
749. **`odoo/_monkeypatches/num2words.py`** -> AI Confidence: **99.25%**
750. **`addons/account/models/account_document_import_mixin.py`** -> AI Confidence: **99.24%**
751. **`addons/account/tests/test_account_payment.py`** -> AI Confidence: **99.24%**
752. **`addons/account_edi_proxy_client/models/account_edi_proxy_user.py`** -> AI Confidence: **99.24%**
753. **`addons/account_edi_ubl_cii/models/account_move.py`** -> AI Confidence: **99.24%**
754. **`addons/api_doc/controllers/api_doc.py`** -> AI Confidence: **99.24%**
755. **`addons/auth_signup/controllers/main.py`** -> AI Confidence: **99.24%**
756. **`addons/base_vat/tests/test_vat_numbers.py`** -> AI Confidence: **99.24%**
757. **`addons/bus/websocket.py`** -> AI Confidence: **99.24%**
758. **`addons/cloud_storage_azure/tests/test_cloud_storage_azure.py`** -> AI Confidence: **99.24%**
759. **`addons/cloud_storage_azure/utils/cleanup_cloud_storage_azure.py`** -> AI Confidence: **99.24%**
760. **`addons/cloud_storage_azure/utils/cloud_storage_azure_utils.py`** -> AI Confidence: **99.24%**
761. **`addons/google_calendar/models/res_users.py`** -> AI Confidence: **99.24%**
762. **`addons/html_editor/controllers/main.py`** -> AI Confidence: **99.24%**
763. **`addons/html_editor/models/ir_qweb_fields.py`** -> AI Confidence: **99.24%**
764. **`addons/iap/models/iap_account.py`** -> AI Confidence: **99.24%**
765. **`addons/iot_drivers/iot_handlers/drivers/l10n_ke_edi_serial_driver.py`** -> AI Confidence: **99.24%**
766. **`addons/iot_drivers/iot_handlers/drivers/printer_driver_base.py`** -> AI Confidence: **99.24%**
767. **`addons/iot_drivers/server_logger.py`** -> AI Confidence: **99.24%**
768. **`addons/iot_drivers/tools/helpers.py`** -> AI Confidence: **99.24%**
769. **`addons/iot_drivers/tools/wifi.py`** -> AI Confidence: **99.24%**
770. **`addons/l10n_hu_edi/tests/test_invoice_xml.py`** -> AI Confidence: **99.24%**
771. **`addons/link_tracker/models/mail_render_mixin.py`** -> AI Confidence: **99.24%**
772. **`addons/mail/models/fetchmail.py`** -> AI Confidence: **99.24%**
773. **`addons/marketing_card/tests/test_campaign.py`** -> AI Confidence: **99.24%**
774. **`addons/microsoft_calendar/tests/test_update_events.py`** -> AI Confidence: **99.24%**
775. **`addons/microsoft_outlook/models/microsoft_outlook_mixin.py`** -> AI Confidence: **99.24%**
776. **`addons/mrp_subcontracting/tests/test_subcontracting.py`** -> AI Confidence: **99.24%**
777. **`addons/payment/models/payment_transaction.py`** -> AI Confidence: **99.24%**
778. **`addons/payment_adyen/controllers/main.py`** -> AI Confidence: **99.24%**
779. **`addons/pos_self_order/models/pos_config.py`** -> AI Confidence: **99.24%**
780. **`addons/product/tests/test_import_files.py`** -> AI Confidence: **99.24%**
781. **`addons/sale_stock/tests/test_sale_stock.py`** -> AI Confidence: **99.24%**
782. **`addons/sms_twilio/tests/common.py`** -> AI Confidence: **99.24%**
783. **`addons/test_event_full/tests/test_event_security.py`** -> AI Confidence: **99.24%**
784. **`addons/test_mail/tests/test_mail_gateway.py`** -> AI Confidence: **99.24%**
785. **`addons/test_mail/tests/test_mail_multicompany.py`** -> AI Confidence: **99.24%**
786. **`addons/test_mail/tests/test_mail_push.py`** -> AI Confidence: **99.24%**
787. **`addons/test_mail/tests/test_mail_scheduled_message.py`** -> AI Confidence: **99.24%**
788. **`addons/website/models/mixins.py`** -> AI Confidence: **99.24%**
789. **`addons/website/models/website_visitor.py`** -> AI Confidence: **99.24%**
790. **`addons/website/tests/test_menu.py`** -> AI Confidence: **99.24%**
791. **`addons/website_forum/controllers/website_forum.py`** -> AI Confidence: **99.24%**
792. **`addons/website_hr_recruitment/controllers/main.py`** -> AI Confidence: **99.24%**
793. **`addons/website_profile/controllers/main.py`** -> AI Confidence: **99.24%**
794. **`addons/website_sale/tests/test_website_sale_pricelist.py`** -> AI Confidence: **99.24%**
795. **`odoo/_monkeypatches/site.py`** -> AI Confidence: **99.24%**
796. **`odoo/_monkeypatches/werkzeug.py`** -> AI Confidence: **99.24%**
797. **`odoo/addons/base/models/ir_autovacuum.py`** -> AI Confidence: **99.24%**
798. **`odoo/addons/base/models/ir_cron.py`** -> AI Confidence: **99.24%**
799. **`odoo/addons/base/models/ir_qweb_fields.py`** -> AI Confidence: **99.24%**
800. **`odoo/addons/base/tests/test_ir_mail_server_smtpd.py`** -> AI Confidence: **99.24%**
801. **`odoo/addons/base/tests/test_translate.py`** -> AI Confidence: **99.24%**
802. **`odoo/addons/test_orm/tests/test_fields.py`** -> AI Confidence: **99.24%**
803. **`odoo/cli/module.py`** -> AI Confidence: **99.24%**
804. **`odoo/cli/start.py`** -> AI Confidence: **99.24%**
805. **`odoo/http.py`** -> AI Confidence: **99.24%**
806. **`odoo/modules/db.py`** -> AI Confidence: **99.24%**
807. **`odoo/modules/migration.py`** -> AI Confidence: **99.24%**
808. **`odoo/modules/module.py`** -> AI Confidence: **99.24%**
809. **`odoo/orm/environments.py`** -> AI Confidence: **99.24%**
810. **`odoo/orm/fields_numeric.py`** -> AI Confidence: **99.24%**
811. **`odoo/orm/fields_reference.py`** -> AI Confidence: **99.24%**
812. **`odoo/service/db.py`** -> AI Confidence: **99.24%**
813. **`odoo/sql_db.py`** -> AI Confidence: **99.24%**
814. **`odoo/tests/common.py`** -> AI Confidence: **99.24%**
815. **`odoo/tests/suite.py`** -> AI Confidence: **99.24%**
816. **`odoo/tools/cache.py`** -> AI Confidence: **99.24%**
817. **`odoo/tools/misc.py`** -> AI Confidence: **99.24%**
818. **`odoo/tools/pdf/__init__.py`** -> AI Confidence: **99.24%**
819. **`odoo/tools/populate.py`** -> AI Confidence: **99.24%**
820. **`odoo/tools/safe_eval.py`** -> AI Confidence: **99.24%**
821. **`odoo/tools/sql.py`** -> AI Confidence: **99.24%**
822. **`setup/package.py`** -> AI Confidence: **99.24%**
823. **`addons/account/static/src/components/section_and_note_fields_backend/section_and_note_fields_backend.js`** -> AI Confidence: **99.24%**
824. **`addons/api_doc/static/src/doc_client.js`** -> AI Confidence: **99.24%**
825. **`addons/base_automation/static/src/base_automation_trigger_selection_field.js`** -> AI Confidence: **99.24%**
826. **`addons/board/static/src/board_controller.js`** -> AI Confidence: **99.24%**
827. **`addons/bus/static/tests/bus_test_helpers.js`** -> AI Confidence: **99.24%**
828. **`addons/event/static/src/client_action/event_barcode.js`** -> AI Confidence: **99.24%**
829. **`addons/google_address_autocomplete/static/src/address_autocomplete/google_address_autocomplete.js`** -> AI Confidence: **99.24%**
830. **`addons/hr_attendance/static/src/components/attendance_menu/attendance_menu.js`** -> AI Confidence: **99.24%**
831. **`addons/hr_holidays/static/src/leave_stats/leave_stats.js`** -> AI Confidence: **99.24%**
832. **`addons/html_builder/static/src/core/remove_plugin.js`** -> AI Confidence: **99.24%**
833. **`addons/html_builder/static/src/plugins/shape/shape_selector.js`** -> AI Confidence: **99.24%**
834. **`addons/html_builder/static/src/snippets/add_snippet_dialog.js`** -> AI Confidence: **99.24%**
835. **`addons/html_editor/static/src/main/separator_plugin.js`** -> AI Confidence: **99.24%**
836. **`addons/html_editor/static/src/main/table/table_ui_plugin.js`** -> AI Confidence: **99.24%**
837. **`addons/html_editor/static/src/main/toolbar/toolbar_plugin.js`** -> AI Confidence: **99.24%**
838. **`addons/im_livechat/static/src/core/public_web/discuss_app_model_patch.js`** -> AI Confidence: **99.24%**
839. **`addons/im_livechat/static/src/embed/common/livechat_service.js`** -> AI Confidence: **99.24%**
840. **`addons/iot_drivers/static/src/app/Homepage.js`** -> AI Confidence: **99.24%**
841. **`addons/mail/static/src/core/common/chat_window.js`** -> AI Confidence: **99.24%**
842. **`addons/mail/static/src/core/common/composer_actions.js`** -> AI Confidence: **99.24%**
843. **`addons/mail/static/src/core/common/search_message_input.js`** -> AI Confidence: **99.24%**
844. **`addons/mail/static/src/core/web/message_patch.js`** -> AI Confidence: **99.24%**
845. **`addons/mail/static/src/core/web/recipients_input.js`** -> AI Confidence: **99.24%**
846. **`addons/mail/static/src/discuss/call/common/call.js`** -> AI Confidence: **99.24%**
847. **`addons/mail/static/src/discuss/call/public_web/discuss_sidebar_call_participants.js`** -> AI Confidence: **99.24%**
848. **`addons/mail/static/src/discuss/core/public_web/sub_channel_list.js`** -> AI Confidence: **99.24%**
849. **`addons/mass_mailing/static/src/fields/html_field/mass_mailing_html_field.js`** -> AI Confidence: **99.24%**
850. **`addons/mass_mailing/static/src/iframe/mass_mailing_iframe.js`** -> AI Confidence: **99.24%**
851. **`addons/point_of_sale/static/src/app/components/popups/closing_popup/closing_popup.js`** -> AI Confidence: **99.24%**
852. **`addons/pos_loyalty/static/src/app/components/popups/manage_giftcard_popup/manage_giftcard_popup.js`** -> AI Confidence: **99.24%**
853. **`addons/pos_self_order/static/src/app/pages/product_page/product_page.js`** -> AI Confidence: **99.24%**
854. **`addons/product/static/src/js/pricelist_report/product_pricelist_report.js`** -> AI Confidence: **99.24%**
855. **`addons/spreadsheet/static/src/data_sources/data_source.js`** -> AI Confidence: **99.24%**
856. **`addons/spreadsheet/static/src/pivot/odoo_pivot.js`** -> AI Confidence: **99.24%**
857. **`addons/web/static/src/core/l10n/localization_service.js`** -> AI Confidence: **99.24%**
858. **`addons/web/static/src/legacy/js/public/public_root.js`** -> AI Confidence: **99.24%**
859. **`addons/web/static/src/model/model.js`** -> AI Confidence: **99.24%**
860. **`addons/web/static/src/search/search_bar_menu/search_bar_menu.js`** -> AI Confidence: **99.24%**
861. **`addons/web/static/src/views/fields/domain/domain_field.js`** -> AI Confidence: **99.24%**
862. **`addons/web/static/src/views/fields/float/float_field.js`** -> AI Confidence: **99.24%**
863. **`addons/web/static/src/views/fields/formatters.js`** -> AI Confidence: **99.24%**
864. **`addons/web/static/src/views/fields/progress_bar/progress_bar_field.js`** -> AI Confidence: **99.24%**
865. **`addons/web/static/src/views/fields/relational_utils.js`** -> AI Confidence: **99.24%**
866. **`addons/web/static/src/views/kanban/kanban_controller.js`** -> AI Confidence: **99.24%**
867. **`addons/web/static/src/views/kanban/kanban_renderer.js`** -> AI Confidence: **99.24%**
868. **`addons/web/static/src/views/list/list_renderer.js`** -> AI Confidence: **99.24%**
869. **`addons/web/static/src/views/view_dialogs/select_create_dialog.js`** -> AI Confidence: **99.24%**
870. **`addons/web/static/src/views/view_hook.js`** -> AI Confidence: **99.24%**
871. **`addons/web/static/src/webclient/res_user_group_ids_field/res_user_group_ids_field.js`** -> AI Confidence: **99.24%**
872. **`addons/web/static/src/webclient/switch_company_menu/switch_company_menu.js`** -> AI Confidence: **99.24%**
873. **`addons/website/static/src/builder/plugins/customize_website_plugin.js`** -> AI Confidence: **99.24%**
874. **`addons/website/static/src/builder/plugins/layout_option/add_element_option_plugin.js`** -> AI Confidence: **99.24%**
875. **`addons/website/static/src/builder/plugins/options/animate_option_plugin.js`** -> AI Confidence: **99.24%**
876. **`addons/website/static/src/builder/plugins/options/image_gallery_option_plugin.js`** -> AI Confidence: **99.24%**
877. **`addons/website/static/src/builder/plugins/options/instagram_option_plugin.js`** -> AI Confidence: **99.24%**
878. **`addons/website/static/src/client_actions/configurator/configurator.js`** -> AI Confidence: **99.24%**
879. **`addons/website/static/src/components/dialog/seo.js`** -> AI Confidence: **99.24%**
880. **`addons/website/static/src/js/editor/html_editor.js`** -> AI Confidence: **99.24%**
881. **`addons/website/static/src/services/website_service.js`** -> AI Confidence: **99.24%**
882. **`addons/website/static/src/snippets/s_dynamic_snippet/dynamic_snippet.js`** -> AI Confidence: **99.24%**
883. **`addons/website_profile/static/src/components/profile_dialog/profile_dialog.js`** -> AI Confidence: **99.24%**
884. **`addons/website_slides/static/src/js/public/components/course_tag_add_dialog/course_tag_add_dialog.js`** -> AI Confidence: **99.24%**
885. **`addons/account/controllers/portal.py`** -> AI Confidence: **99.23%**
886. **`addons/account/tests/test_account_move_entry.py`** -> AI Confidence: **99.23%**
887. **`addons/account/tests/test_account_move_in_invoice.py`** -> AI Confidence: **99.23%**
888. **`addons/account/tests/test_account_move_send.py`** -> AI Confidence: **99.23%**
889. **`addons/account/tests/test_chart_template.py`** -> AI Confidence: **99.23%**
890. **`addons/account_peppol/tests/test_peppol_participant.py`** -> AI Confidence: **99.23%**
891. **`addons/auth_totp_mail/models/res_users.py`** -> AI Confidence: **99.23%**
892. **`addons/crm/tests/test_crm_pls.py`** -> AI Confidence: **99.23%**
893. **`addons/gamification/tests/test_karma_tracking.py`** -> AI Confidence: **99.23%**
894. **`addons/google_address_autocomplete/controllers/google_address_autocomplete.py`** -> AI Confidence: **99.23%**
895. **`addons/google_calendar/tests/test_sync_odoo2google_mail.py`** -> AI Confidence: **99.23%**
896. **`addons/google_calendar/utils/google_event.py`** -> AI Confidence: **99.23%**
897. **`addons/google_gmail/models/google_gmail_mixin.py`** -> AI Confidence: **99.23%**
898. **`addons/hr/models/res_users.py`** -> AI Confidence: **99.23%**
899. **`addons/hr_calendar/models/res_partner.py`** -> AI Confidence: **99.23%**
900. **`addons/hr_holidays/report/holidays_summary_report.py`** -> AI Confidence: **99.23%**
901. **`addons/iot_drivers/connection_manager.py`** -> AI Confidence: **99.23%**
902. **`addons/iot_drivers/tools/certificate.py`** -> AI Confidence: **99.23%**
903. **`addons/l10n_eg_edi_eta/models/account_move.py`** -> AI Confidence: **99.23%**
904. **`addons/l10n_es_edi_verifactu_pos/tests/test_pos_order.py`** -> AI Confidence: **99.23%**
905. **`addons/l10n_tr_nilvera_einvoice/tests/test_tr_nilvera_mocked_requests.py`** -> AI Confidence: **99.23%**
906. **`addons/l10n_tw_edi_ecpay/tests/test_edi.py`** -> AI Confidence: **99.23%**
907. **`addons/mail/controllers/thread.py`** -> AI Confidence: **99.23%**
908. **`addons/mail/models/template_reset_mixin.py`** -> AI Confidence: **99.23%**
909. **`addons/mail/tests/discuss/test_discuss_mail_presence.py`** -> AI Confidence: **99.23%**
910. **`addons/mail_group/tests/test_mail_group_moderation.py`** -> AI Confidence: **99.23%**
911. **`addons/mass_mailing/controllers/main.py`** -> AI Confidence: **99.23%**
912. **`addons/mrp/tests/test_bom.py`** -> AI Confidence: **99.23%**
913. **`addons/mrp/tests/test_order.py`** -> AI Confidence: **99.23%**
914. **`addons/payment/controllers/portal.py`** -> AI Confidence: **99.23%**
915. **`addons/payment_paymob/models/payment_provider.py`** -> AI Confidence: **99.23%**
916. **`addons/test_discuss_full/tests/test_performance.py`** -> AI Confidence: **99.23%**
917. **`addons/test_mail/tests/test_mail_thread_mixins.py`** -> AI Confidence: **99.23%**
918. **`addons/test_mail/tests/test_message_track.py`** -> AI Confidence: **99.23%**
919. **`addons/uom/models/uom_uom.py`** -> AI Confidence: **99.23%**
920. **`addons/web/tests/test_image.py`** -> AI Confidence: **99.23%**
921. **`addons/website_sale/tests/test_website_sale_product_filters.py`** -> AI Confidence: **99.23%**
922. **`odoo/addons/base/models/ir_default.py`** -> AI Confidence: **99.23%**
923. **`odoo/addons/base/tests/test_init.py`** -> AI Confidence: **99.23%**
924. **`odoo/addons/test_orm/models/test_orm.py`** -> AI Confidence: **99.23%**
925. **`odoo/addons/test_orm/tests/test_domain.py`** -> AI Confidence: **99.23%**
926. **`odoo/addons/test_testing_utilities/tests/test_methods.py`** -> AI Confidence: **99.23%**
927. **`odoo/cli/neutralize.py`** -> AI Confidence: **99.23%**
928. **`odoo/cli/populate.py`** -> AI Confidence: **99.23%**
929. **`odoo/modules/module_graph.py`** -> AI Confidence: **99.23%**
930. **`odoo/tests/shell.py`** -> AI Confidence: **99.23%**
931. **`odoo/tools/i18n.py`** -> AI Confidence: **99.23%**
932. **`addons/hr_attendance/static/src/components/manual_selection/manual_selection.js`** -> AI Confidence: **99.23%**
933. **`addons/html_builder/static/src/core/utils.js`** -> AI Confidence: **99.23%**
934. **`addons/html_builder/static/src/snippets/snippet_viewer.js`** -> AI Confidence: **99.23%**
935. **`addons/html_editor/static/src/main/chatgpt/chatgpt_translate_plugin.js`** -> AI Confidence: **99.23%**
936. **`addons/html_editor/static/src/main/column_plugin.js`** -> AI Confidence: **99.23%**
937. **`addons/html_editor/static/src/main/media/media_dialog/upload_progress_toast/upload_service.js`** -> AI Confidence: **99.23%**
938. **`addons/html_editor/static/src/main/powerbox/search_powerbox_plugin.js`** -> AI Confidence: **99.23%**
939. **`addons/html_editor/static/src/main/selection_placeholder_plugin.js`** -> AI Confidence: **99.23%**
940. **`addons/html_editor/static/src/utils/dom_state.js`** -> AI Confidence: **99.23%**
941. **`addons/mail/static/src/core/common/attachment_model.js`** -> AI Confidence: **99.23%**
942. **`addons/mail/static/src/core/common/message_reaction_list.js`** -> AI Confidence: **99.23%**
943. **`addons/mail/static/src/core/common/thread_actions.js`** -> AI Confidence: **99.23%**
944. **`addons/mail/static/src/core/public_web/discuss.js`** -> AI Confidence: **99.23%**
945. **`addons/mail/static/src/core/web/activity_list_popover_item.js`** -> AI Confidence: **99.23%**
946. **`addons/mail/static/src/discuss/typing/common/composer_patch.js`** -> AI Confidence: **99.23%**
947. **`addons/mail/static/src/discuss/voice_message/common/voice_recorder.js`** -> AI Confidence: **99.23%**
948. **`addons/mail/static/src/model/store_internal.js`** -> AI Confidence: **99.23%**
949. **`addons/mail/static/src/utils/common/format.js`** -> AI Confidence: **99.23%**
950. **`addons/mail/static/src/views/web/activity/activity_renderer.js`** -> AI Confidence: **99.23%**
951. **`addons/mail/static/src/views/web/fields/assign_user_command_hook.js`** -> AI Confidence: **99.23%**
952. **`addons/mass_mailing/static/src/themes/theme_service.js`** -> AI Confidence: **99.23%**
953. **`addons/mrp/static/src/components/mo_overview/mrp_mo_overview.js`** -> AI Confidence: **99.23%**
954. **`addons/point_of_sale/static/src/app/models/pos_order_line.js`** -> AI Confidence: **99.23%**
955. **`addons/point_of_sale/static/src/app/services/hardware_proxy_service.js`** -> AI Confidence: **99.23%**
956. **`addons/point_of_sale/static/src/app/services/number_buffer_service.js`** -> AI Confidence: **99.23%**
957. **`addons/pos_loyalty/static/src/app/screens/product_screen/control_buttons/control_buttons.js`** -> AI Confidence: **99.23%**
958. **`addons/pos_restaurant/static/src/app/screens/split_bill_screen/split_bill_screen.js`** -> AI Confidence: **99.23%**
959. **`addons/pos_safaricom/static/src/app/payment_safaricom.js`** -> AI Confidence: **99.23%**
960. **`addons/spreadsheet/static/src/global_filters/components/filter_values_list/filter_values_list.js`** -> AI Confidence: **99.23%**
961. **`addons/spreadsheet/static/src/pivot/odoo_pivot_loader.js`** -> AI Confidence: **99.23%**
962. **`addons/spreadsheet/static/src/pivot/plugins/pivot_core_view_global_filter_plugin.js`** -> AI Confidence: **99.23%**
963. **`addons/spreadsheet/static/tests/helpers/model.js`** -> AI Confidence: **99.23%**
964. **`addons/spreadsheet/static/tests/helpers/pivot.js`** -> AI Confidence: **99.23%**
965. **`addons/spreadsheet_account/static/src/plugins/accounting_plugin.js`** -> AI Confidence: **99.23%**
966. **`addons/web/static/src/core/commands/default_providers.js`** -> AI Confidence: **99.23%**
967. **`addons/web/static/src/core/datetime/datetime_picker.js`** -> AI Confidence: **99.23%**
968. **`addons/web/static/src/core/ui/ui_service.js`** -> AI Confidence: **99.23%**
969. **`addons/web/static/src/env.js`** -> AI Confidence: **99.23%**
970. **`addons/web/static/src/model/relational_model/dynamic_list.js`** -> AI Confidence: **99.23%**
971. **`addons/web/static/src/views/calendar/calendar_common/calendar_common_popover.js`** -> AI Confidence: **99.23%**
972. **`addons/web/static/src/views/fields/selection/selection_field.js`** -> AI Confidence: **99.23%**
973. **`addons/web/static/src/views/graph/graph_view.js`** -> AI Confidence: **99.23%**
974. **`addons/web/static/src/webclient/actions/client_actions.js`** -> AI Confidence: **99.23%**
975. **`addons/web/static/src/webclient/res_user_group_ids_field/res_user_group_ids_privilege_field.js`** -> AI Confidence: **99.23%**
976. **`addons/web/static/tests/_framework/module_set.hoot.js`** -> AI Confidence: **99.23%**
977. **`addons/web_tour/static/src/js/tour_automatic/tour_automatic.js`** -> AI Confidence: **99.23%**
978. **`addons/web_tour/static/src/js/tour_recorder/tour_recorder.js`** -> AI Confidence: **99.23%**
979. **`addons/website/static/src/builder/plugins/font/add_font_dialog.js`** -> AI Confidence: **99.23%**
980. **`addons/website/static/src/builder/plugins/options/dynamic_snippet_option_plugin.js`** -> AI Confidence: **99.23%**
981. **`addons/website/static/src/core/website_edit_service.js`** -> AI Confidence: **99.23%**
982. **`addons/website/static/src/js/backend/view_hierarchy/view_hierarchy.js`** -> AI Confidence: **99.23%**
983. **`addons/website/static/src/js/utils.js`** -> AI Confidence: **99.23%**
984. **`addons/survey/tests/test_survey_security.py`** -> AI Confidence: **99.22%**
985. **`addons/mail/static/src/core/public_web/thread_model_patch.js`** -> AI Confidence: **99.22%**
986. **`addons/website/static/src/snippets/s_searchbar/search_bar.js`** -> AI Confidence: **99.22%**
987. **`addons/l10n_gr_edi/models/account_move_line.py`** -> AI Confidence: **99.2%**
988. **`addons/l10n_latam_check/models/account_payment.py`** -> AI Confidence: **99.2%**
989. **`addons/pos_self_order/models/pos_order.py`** -> AI Confidence: **99.2%**
990. **`addons/product/models/product_pricelist_item.py`** -> AI Confidence: **99.2%**
991. **`odoo/addons/test_assetsbundle/tests/test_js_transpiler_regex.py`** -> AI Confidence: **99.2%**
992. **`addons/web/static/src/core/file_viewer/file_viewer.js`** -> AI Confidence: **99.2%**
993. **`addons/web/static/src/views/graph/graph_arch_parser.js`** -> AI Confidence: **99.2%**
994. **`addons/web/static/src/views/pivot/pivot_arch_parser.js`** -> AI Confidence: **99.2%**
995. **`addons/website/static/tests/tours/website_form_editor.js`** -> AI Confidence: **99.2%**
996. **`addons/account/demo/account_demo.py`** -> AI Confidence: **99.18%**
997. **`addons/account/tests/test_account_journal.py`** -> AI Confidence: **99.18%**
998. **`addons/account/tests/test_account_move_reconcile.py`** -> AI Confidence: **99.18%**
999. **`addons/account_check_printing/tests/test_print_check.py`** -> AI Confidence: **99.18%**
1000. **`addons/api_doc/tests/test_doc.py`** -> AI Confidence: **99.18%**
1001. **`addons/auth_passkey/models/auth_passkey_key.py`** -> AI Confidence: **99.18%**
1002. **`addons/base_import_module/tests/test_import_module.py`** -> AI Confidence: **99.18%**
1003. **`addons/certificate/tests/test_keys_certificates.py`** -> AI Confidence: **99.18%**
1004. **`addons/cloud_storage_google/models/ir_attachment.py`** -> AI Confidence: **99.18%**
1005. **`addons/crm_iap_mine/tests/common.py`** -> AI Confidence: **99.18%**
1006. **`addons/event/tests/test_event_internals.py`** -> AI Confidence: **99.18%**
1007. **`addons/event_booth_sale/tests/test_event_booth_sale.py`** -> AI Confidence: **99.18%**
1008. **`addons/hr_attendance/tests/test_performance.py`** -> AI Confidence: **99.18%**
1009. **`addons/hr_holidays/tests/test_access_rights.py`** -> AI Confidence: **99.18%**
1010. **`addons/hr_holidays/tests/test_allocations.py`** -> AI Confidence: **99.18%**
1011. **`addons/im_livechat/tests/test_chatbot_internals.py`** -> AI Confidence: **99.18%**
1012. **`addons/iot_drivers/iot_handlers/drivers/display_driver_L.py`** -> AI Confidence: **99.18%**
1013. **`addons/iot_drivers/webrtc_client.py`** -> AI Confidence: **99.18%**
1014. **`addons/l10n_dk_nemhandel/tests/test_xml_oioubl_21.py`** -> AI Confidence: **99.18%**
1015. **`addons/l10n_eg_edi_eta/tests/test_edi_json.py`** -> AI Confidence: **99.18%**
1016. **`addons/l10n_in/tests/test_check_status.py`** -> AI Confidence: **99.18%**
1017. **`addons/l10n_my_edi/tests/test_file_generation.py`** -> AI Confidence: **99.18%**
1018. **`addons/l10n_pl_edi/tests/test_l10n_pl_edi.py`** -> AI Confidence: **99.18%**
1019. **`addons/l10n_ro_edi/controllers/main.py`** -> AI Confidence: **99.18%**
1020. **`addons/lunch/tests/test_supplier.py`** -> AI Confidence: **99.18%**
1021. **`addons/mail/tests/discuss/test_message_controller.py`** -> AI Confidence: **99.18%**
1022. **`addons/mail/tests/discuss/test_rtc.py`** -> AI Confidence: **99.18%**
1023. **`addons/mail/tests/test_link_preview.py`** -> AI Confidence: **99.18%**
1024. **`addons/mail/tests/test_mail_message_translate.py`** -> AI Confidence: **99.18%**
1025. **`addons/mail/tests/test_res_users.py`** -> AI Confidence: **99.18%**
1026. **`addons/mail_plugin/controllers/authenticate.py`** -> AI Confidence: **99.18%**
1027. **`addons/mass_mailing/tests/test_mailing_controllers.py`** -> AI Confidence: **99.18%**
1028. **`addons/microsoft_calendar/utils/microsoft_calendar.py`** -> AI Confidence: **99.18%**
1029. **`addons/mrp/tests/test_procurement.py`** -> AI Confidence: **99.18%**
1030. **`addons/mrp_subcontracting_purchase/tests/test_mrp_subcontracting_purchase.py`** -> AI Confidence: **99.18%**
1031. **`addons/onboarding/tests/test_onboarding.py`** -> AI Confidence: **99.18%**
1032. **`addons/payment/tests/test_payment_provider.py`** -> AI Confidence: **99.18%**
1033. **`addons/payment_authorize/models/payment_provider.py`** -> AI Confidence: **99.18%**
1034. **`addons/payment_iyzico/models/payment_provider.py`** -> AI Confidence: **99.18%**
1035. **`addons/payment_mercado_pago/controllers/onboarding.py`** -> AI Confidence: **99.18%**
1036. **`addons/payment_mercado_pago/controllers/payment.py`** -> AI Confidence: **99.18%**
1037. **`addons/payment_paymob/controllers/main.py`** -> AI Confidence: **99.18%**
1038. **`addons/payment_paypal/controllers/main.py`** -> AI Confidence: **99.18%**
1039. **`addons/payment_razorpay/controllers/onboarding.py`** -> AI Confidence: **99.18%**
1040. **`addons/payment_razorpay/tests/test_payment_transaction.py`** -> AI Confidence: **99.18%**
1041. **`addons/payment_redsys/controllers/main.py`** -> AI Confidence: **99.18%**
1042. **`addons/payment_redsys/models/payment_transaction.py`** -> AI Confidence: **99.18%**
1043. **`addons/payment_stripe/tests/test_stripe.py`** -> AI Confidence: **99.18%**
1044. **`addons/payment_worldline/models/payment_provider.py`** -> AI Confidence: **99.18%**
1045. **`addons/payment_xendit/controllers/main.py`** -> AI Confidence: **99.18%**
1046. **`addons/pos_online_payment/tests/test_frontend.py`** -> AI Confidence: **99.18%**
1047. **`addons/pos_sale/tests/test_pos_sale_flow.py`** -> AI Confidence: **99.18%**
1048. **`addons/product/tests/test_product_pricelist.py`** -> AI Confidence: **99.18%**
1049. **`addons/product/tests/test_variants.py`** -> AI Confidence: **99.18%**
1050. **`addons/rpc/controllers/json2.py`** -> AI Confidence: **99.18%**
1051. **`addons/sale/tests/test_sale_order.py`** -> AI Confidence: **99.18%**
1052. **`addons/sale_loyalty/tests/test_program_rules.py`** -> AI Confidence: **99.18%**
1053. **`addons/sale_pdf_quote_builder/controllers/quotation_document.py`** -> AI Confidence: **99.18%**
1054. **`addons/sale_pdf_quote_builder/tests/test_pdf_quote_builder.py`** -> AI Confidence: **99.18%**
1055. **`addons/sale_stock/tests/test_sale_stock_accrued_entries.py`** -> AI Confidence: **99.18%**
1056. **`addons/sale_timesheet/controllers/portal.py`** -> AI Confidence: **99.18%**
1057. **`addons/stock/tests/test_move.py`** -> AI Confidence: **99.18%**
1058. **`addons/stock_account/tests/test_stockvaluation.py`** -> AI Confidence: **99.18%**
1059. **`addons/test_base_automation/tests/test_flow.py`** -> AI Confidence: **99.18%**
1060. **`addons/test_event_full/tests/common.py`** -> AI Confidence: **99.18%**
1061. **`addons/test_mass_mailing/tests/test_mailing_statistics.py`** -> AI Confidence: **99.18%**
1062. **`addons/test_website_modules/tests/test_performance.py`** -> AI Confidence: **99.18%**
1063. **`addons/web/controllers/webmanifest.py`** -> AI Confidence: **99.18%**
1064. **`addons/web/tests/test_partner.py`** -> AI Confidence: **99.18%**
1065. **`addons/web/tests/test_reports.py`** -> AI Confidence: **99.18%**
1066. **`addons/website/tests/test_res_users.py`** -> AI Confidence: **99.18%**
1067. **`addons/website/tests/test_website_visitor.py`** -> AI Confidence: **99.18%**
1068. **`addons/website_sale/controllers/payment.py`** -> AI Confidence: **99.18%**
1069. **`addons/website_sale/controllers/website.py`** -> AI Confidence: **99.18%**
1070. **`addons/website_sale/tests/test_address.py`** -> AI Confidence: **99.18%**
1071. **`addons/website_sale/tests/test_express_checkout_flows.py`** -> AI Confidence: **99.18%**
1072. **`addons/website_sale/tests/test_website_sale_gmc.py`** -> AI Confidence: **99.18%**
1073. **`addons/website_sale/tests/test_website_sequence.py`** -> AI Confidence: **99.18%**
1074. **`addons/website_slides/tests/test_attendee.py`** -> AI Confidence: **99.18%**
1075. **`odoo/_monkeypatches/__init__.py`** -> AI Confidence: **99.18%**
1076. **`odoo/addons/base/tests/test_cache.py`** -> AI Confidence: **99.18%**
1077. **`odoo/addons/base/tests/test_misc.py`** -> AI Confidence: **99.18%**
1078. **`odoo/addons/base/tests/test_test_suite.py`** -> AI Confidence: **99.18%**
1079. **`odoo/addons/base/tests/test_views.py`** -> AI Confidence: **99.18%**
1080. **`odoo/addons/test_assetsbundle/tests/test_assetsbundle.py`** -> AI Confidence: **99.18%**
1081. **`odoo/addons/test_http/tests/test_captcha.py`** -> AI Confidence: **99.18%**
1082. **`odoo/addons/test_http/tests/test_misc.py`** -> AI Confidence: **99.18%**
1083. **`odoo/addons/test_http/tests/test_webjson.py`** -> AI Confidence: **99.18%**
1084. **`odoo/modules/neutralize.py`** -> AI Confidence: **99.18%**
1085. **`odoo/orm/fields_misc.py`** -> AI Confidence: **99.18%**
1086. **`addons/account/static/src/components/tax_totals/tax_totals.js`** -> AI Confidence: **99.18%**
1087. **`addons/auth_timeout/static/src/services/check_identity/check_identity.js`** -> AI Confidence: **99.18%**
1088. **`addons/base_automation/static/src/group_config_menu_patch.js`** -> AI Confidence: **99.18%**
1089. **`addons/calendar/static/src/views/attendee_calendar/common/attendee_calendar_common_popover.js`** -> AI Confidence: **99.18%**
1090. **`addons/hr/static/src/views/fields/many2one_avatar_employee_field/kanban_many2one_avatar_employee_field.js`** -> AI Confidence: **99.18%**
1091. **`addons/hr_holidays/static/src/components/accrual_level/accrual_levels.js`** -> AI Confidence: **99.18%**
1092. **`addons/hr_holidays/static/src/views/calendar/calendar_controller.js`** -> AI Confidence: **99.18%**
1093. **`addons/hr_recruitment_skills/static/src/fields/skill_match_gauge_field/skill_match_gauge_field.js`** -> AI Confidence: **99.18%**
1094. **`addons/html_builder/static/src/core/building_blocks/builder_list.js`** -> AI Confidence: **99.18%**
1095. **`addons/html_builder/static/src/core/building_blocks/builder_select.js`** -> AI Confidence: **99.18%**
1096. **`addons/html_builder/static/src/core/clone_plugin.js`** -> AI Confidence: **99.18%**
1097. **`addons/html_builder/static/src/core/overlay_buttons/overlay_buttons_plugin.js`** -> AI Confidence: **99.18%**
1098. **`addons/html_builder/static/src/plugins/image/image_filter_option_plugin.js`** -> AI Confidence: **99.18%**
1099. **`addons/html_builder/static/src/sidebar/option_container.js`** -> AI Confidence: **99.18%**
1100. **`addons/html_editor/static/src/main/font/color_selector.js`** -> AI Confidence: **99.18%**
1101. **`addons/html_editor/static/src/main/font/font_family_plugin.js`** -> AI Confidence: **99.18%**
1102. **`addons/html_editor/static/src/main/media/media_dialog/file_selector.js`** -> AI Confidence: **99.18%**
1103. **`addons/html_editor/static/tests/_helpers/syntax_highlighting.js`** -> AI Confidence: **99.18%**
1104. **`addons/im_livechat/static/src/core/web/livechat_channel_info_list.js`** -> AI Confidence: **99.18%**
1105. **`addons/im_livechat/static/src/core/web/livechat_conversation_tag_edit.js`** -> AI Confidence: **99.18%**
1106. **`addons/mail/static/src/chatter/web/mail_composer_form.js`** -> AI Confidence: **99.18%**
1107. **`addons/mail/static/src/core/common/chat_bubble.js`** -> AI Confidence: **99.18%**
1108. **`addons/mail/static/src/core/common/chat_hub.js`** -> AI Confidence: **99.18%**
1109. **`addons/mail/static/src/core/common/search_messages_panel.js`** -> AI Confidence: **99.18%**
1110. **`addons/mail/static/src/core/public_web/discuss_content.js`** -> AI Confidence: **99.18%**
1111. **`addons/mail/static/src/core/web/activity_model_patch.js`** -> AI Confidence: **99.18%**
1112. **`addons/mail/static/src/discuss/core/common/attachment_panel.js`** -> AI Confidence: **99.18%**
1113. **`addons/mail/static/src/views/web/fields/html_composer_message_field/html_composer_message_field.js`** -> AI Confidence: **99.18%**
1114. **`addons/mail/static/tests/mail_test_helpers.js`** -> AI Confidence: **99.18%**
1115. **`addons/partner_autocomplete/static/src/js/partner_autocomplete_many2one.js`** -> AI Confidence: **99.18%**
1116. **`addons/payment_demo/static/src/interactions/express_checkout.js`** -> AI Confidence: **99.18%**
1117. **`addons/point_of_sale/static/src/app/pos_app.js`** -> AI Confidence: **99.18%**
1118. **`addons/point_of_sale/static/src/app/screens/product_screen/product_screen.js`** -> AI Confidence: **99.18%**
1119. **`addons/point_of_sale/static/src/backend/pos_kanban_view/pos_kanban_view.js`** -> AI Confidence: **99.18%**
1120. **`addons/point_of_sale/static/src/customer_display/customer_display.js`** -> AI Confidence: **99.18%**
1121. **`addons/portal/static/src/chatter/frontend/portal_chatter_service.js`** -> AI Confidence: **99.18%**
1122. **`addons/pos_event/static/src/app/components/popup/event_slot_selection_popup/event_slot_selection_popup.js`** -> AI Confidence: **99.18%**
1123. **`addons/pos_loyalty/static/tests/tours/utils/pos_loyalty_util.js`** -> AI Confidence: **99.18%**
1124. **`addons/pos_restaurant/static/tests/tours/fake_tours.js`** -> AI Confidence: **99.18%**
1125. **`addons/project/static/src/components/project_right_side_panel/project_right_side_panel.js`** -> AI Confidence: **99.18%**
1126. **`addons/project/static/src/components/subtask_kanban_list/subtask_kanban_list.js`** -> AI Confidence: **99.18%**
1127. **`addons/project/static/src/views/project_task_form/project_task_form_controller.js`** -> AI Confidence: **99.18%**
1128. **`addons/project_todo/static/src/views/todo_form/todo_form_controller.js`** -> AI Confidence: **99.18%**
1129. **`addons/purchase/static/src/components/purchase_file_uploader/purchase_file_uploader.js`** -> AI Confidence: **99.18%**
1130. **`addons/sale_stock/static/src/widgets/qty_at_date_widget.js`** -> AI Confidence: **99.18%**
1131. **`addons/spreadsheet_dashboard/static/src/bundle/dashboard_action/dashboard_loader_service.js`** -> AI Confidence: **99.18%**
1132. **`addons/stock/static/src/widgets/stock_package_m2o.js`** -> AI Confidence: **99.18%**
1133. **`addons/web/static/src/core/tree_editor/tree_editor_autocomplete.js`** -> AI Confidence: **99.18%**
1134. **`addons/web/static/src/views/calendar/calendar_filter_section/calendar_filter_section.js`** -> AI Confidence: **99.18%**
1135. **`addons/web/static/src/views/fields/ace/ace_field.js`** -> AI Confidence: **99.18%**
1136. **`addons/web/static/src/views/fields/many2many_checkboxes/many2many_checkboxes_field.js`** -> AI Confidence: **99.18%**
1137. **`addons/web/static/src/views/fields/many2many_tags/many2many_tags_field.js`** -> AI Confidence: **99.18%**
1138. **`addons/web/static/src/views/fields/many2one/many2one_field.js`** -> AI Confidence: **99.18%**
1139. **`addons/web/static/src/views/pivot/pivot_controller.js`** -> AI Confidence: **99.18%**
1140. **`addons/web/static/src/views/view_components/multi_create_popover.js`** -> AI Confidence: **99.18%**
1141. **`addons/web/static/src/webclient/settings_form_view/settings_form_controller.js`** -> AI Confidence: **99.18%**
1142. **`addons/web/static/src/webclient/user_menu/user_menu_items.js`** -> AI Confidence: **99.18%**
1143. **`addons/web/static/tests/legacy/helpers/mock_services.js`** -> AI Confidence: **99.18%**
1144. **`addons/web_hierarchy/static/src/hierarchy_card.js`** -> AI Confidence: **99.18%**
1145. **`addons/website/static/src/builder/plugins/form/form_option_plugin.js`** -> AI Confidence: **99.18%**
1146. **`addons/website/static/src/builder/plugins/options/carousel_slides_option_plugin.js`** -> AI Confidence: **99.18%**
1147. **`addons/website/static/src/builder/plugins/options/dynamic_snippet_carousel_option_plugin.js`** -> AI Confidence: **99.18%**
1148. **`addons/website/static/src/builder/plugins/options/scroll_button_option_plugin.js`** -> AI Confidence: **99.18%**
1149. **`addons/website/static/src/builder/plugins/options/social_media_option_plugin.js`** -> AI Confidence: **99.18%**
1150. **`addons/website/static/src/builder/plugins/options/visibility_option_plugin.js`** -> AI Confidence: **99.18%**
1151. **`addons/website/static/src/builder/plugins/options/website_page_config_option_plugin.js`** -> AI Confidence: **99.18%**
1152. **`addons/website/static/src/builder/website_builder.js`** -> AI Confidence: **99.18%**
1153. **`addons/website/static/src/client_actions/website_preview/website_systray_item.js`** -> AI Confidence: **99.18%**
1154. **`addons/website/static/src/components/fields/fields.js`** -> AI Confidence: **99.18%**
1155. **`addons/website_sale/static/src/website_builder/dynamic_snippet_category_option_plugin.js`** -> AI Confidence: **99.18%**
1156. **`addons/website_slides/static/src/js/public/components/slide_upload_dialog/slide_upload_dialog.js`** -> AI Confidence: **99.18%**
1157. **`addons/account/models/account_report.py`** -> AI Confidence: **99.17%**
1158. **`addons/account/tests/test_taxes_global_discount.py`** -> AI Confidence: **99.17%**
1159. **`addons/account/tools/dict_to_xml.py`** -> AI Confidence: **99.17%**
1160. **`addons/account_peppol/exceptions.py`** -> AI Confidence: **99.17%**
1161. **`addons/account_tax_python/tests/test_taxes_computation.py`** -> AI Confidence: **99.17%**
1162. **`addons/cloud_storage_migration/models/cloud_storage_migration_report.py`** -> AI Confidence: **99.17%**
1163. **`addons/hr/tests/test_payroll_fields_access.py`** -> AI Confidence: **99.17%**
1164. **`addons/l10n_ar_withholding/models/account_tax.py`** -> AI Confidence: **99.17%**
1165. **`addons/l10n_cl/models/account_move_line.py`** -> AI Confidence: **99.17%**
1166. **`addons/l10n_de/migrations/3.0/pre-migrate.py`** -> AI Confidence: **99.17%**
1167. **`addons/l10n_es_edi_facturae/models/account_tax.py`** -> AI Confidence: **99.17%**
1168. **`addons/l10n_fr_hr_holidays/models/hr_leave.py`** -> AI Confidence: **99.17%**
1169. **`addons/l10n_hr_edi/models/account_move_send.py`** -> AI Confidence: **99.17%**
1170. **`addons/l10n_in_edi/models/res_partner.py`** -> AI Confidence: **99.17%**
1171. **`addons/l10n_it_edi/models/account_tax.py`** -> AI Confidence: **99.17%**
1172. **`addons/l10n_ke_edi_tremol/models/account_move.py`** -> AI Confidence: **99.17%**
1173. **`addons/l10n_my_edi/models/account_edi_xml_ubl_my.py`** -> AI Confidence: **99.17%**
1174. **`addons/l10n_pl/models/product.py`** -> AI Confidence: **99.17%**
1175. **`addons/l10n_tr_nilvera/const.py`** -> AI Confidence: **99.17%**
1176. **`addons/l10n_tr_nilvera_edispatch/models/res_partner.py`** -> AI Confidence: **99.17%**
1177. **`addons/mail/models/ir_model.py`** -> AI Confidence: **99.17%**
1178. **`addons/mail/models/mail_composer_mixin.py`** -> AI Confidence: **99.17%**
1179. **`addons/mail/models/mail_followers.py`** -> AI Confidence: **99.17%**
1180. **`addons/mrp/models/res_config_settings.py`** -> AI Confidence: **99.17%**
1181. **`addons/payment_paypal/utils.py`** -> AI Confidence: **99.17%**
1182. **`addons/point_of_sale/wizard/pos_make_invoice.py`** -> AI Confidence: **99.17%**
1183. **`addons/portal/tests/test_pager.py`** -> AI Confidence: **99.17%**
1184. **`addons/pos_loyalty/models/pos_config.py`** -> AI Confidence: **99.17%**
1185. **`addons/pos_loyalty/models/pos_order.py`** -> AI Confidence: **99.17%**
1186. **`addons/product_margin/models/product_product.py`** -> AI Confidence: **99.17%**
1187. **`addons/project_timesheet_holidays/__init__.py`** -> AI Confidence: **99.17%**
1188. **`addons/sale_mrp/models/account_move.py`** -> AI Confidence: **99.17%**
1189. **`addons/sale_mrp/models/sale_order_line.py`** -> AI Confidence: **99.17%**
1190. **`addons/sale_pdf_quote_builder/models/ir_actions_report.py`** -> AI Confidence: **99.17%**
1191. **`addons/sale_timesheet_margin/models/sale_order_line.py`** -> AI Confidence: **99.17%**
1192. **`addons/sales_team/models/crm_team_member.py`** -> AI Confidence: **99.17%**
1193. **`addons/sms/models/mail_followers.py`** -> AI Confidence: **99.17%**
1194. **`addons/sms/models/mail_thread.py`** -> AI Confidence: **99.17%**
1195. **`addons/sms/models/models.py`** -> AI Confidence: **99.17%**
1196. **`addons/stock/tests/test_packing_neg.py`** -> AI Confidence: **99.17%**
1197. **`addons/survey_crm/models/survey_user_input.py`** -> AI Confidence: **99.17%**
1198. **`addons/web/models/ir_ui_menu.py`** -> AI Confidence: **99.17%**
1199. **`addons/website_crm_partner_assign/wizard/crm_forward_to_partner.py`** -> AI Confidence: **99.17%**
1200. **`addons/website_event_track_live/models/event_track.py`** -> AI Confidence: **99.17%**
1201. **`odoo/addons/test_read_group/tests/test_read_grouping_sets.py`** -> AI Confidence: **99.17%**
1202. **`odoo/tools/babel/python_extractor.py`** -> AI Confidence: **99.17%**
1203. **`odoo/tools/parse_version.py`** -> AI Confidence: **99.17%**
1204. **`addons/bus/static/src/workers/election_worker.js`** -> AI Confidence: **99.17%**
1205. **`addons/html_builder/static/src/core/builder_action.js`** -> AI Confidence: **99.17%**
1206. **`addons/html_editor/static/src/main/media/image_transformation.js`** -> AI Confidence: **99.17%**
1207. **`addons/html_editor/static/src/main/table/table_picker.js`** -> AI Confidence: **99.17%**
1208. **`addons/html_editor/static/src/utils/clipboard.js`** -> AI Confidence: **99.17%**
1209. **`addons/mail/static/src/views/web/fields/html_mail_field/convert_inline.js`** -> AI Confidence: **99.17%**
1210. **`addons/point_of_sale/static/src/app/models/utils/order_change.js`** -> AI Confidence: **99.17%**
1211. **`addons/point_of_sale/static/src/app/utils/debug.js`** -> AI Confidence: **99.17%**
1212. **`addons/spreadsheet/static/src/chart/plugins/odoo_chart_core_view_plugin.js`** -> AI Confidence: **99.17%**
1213. **`addons/spreadsheet/static/src/o_spreadsheet/migration.js`** -> AI Confidence: **99.17%**
1214. **`addons/survey/static/tests/tours/certification_success.js`** -> AI Confidence: **99.17%**
1215. **`addons/survey/static/tests/tours/survey_roaming_mandatory_questions.js`** -> AI Confidence: **99.17%**
1216. **`addons/web/static/src/core/position/utils.js`** -> AI Confidence: **99.17%**
1217. **`addons/web/static/src/core/py_js/py_parser.js`** -> AI Confidence: **99.17%**
1218. **`addons/web/static/src/core/template_inheritance.js`** -> AI Confidence: **99.17%**
1219. **`addons/web/static/src/core/utils/sortable.js`** -> AI Confidence: **99.17%**
1220. **`addons/web/static/src/public/colibri.js`** -> AI Confidence: **99.17%**
1221. **`addons/web/static/src/views/calendar/calendar_common/calendar_common_week_column.js`** -> AI Confidence: **99.17%**
1222. **`addons/web/static/tests/legacy/legacy_tests/helpers/test_utils_dom.js`** -> AI Confidence: **99.17%**
1223. **`addons/web/static/tests/tours/test_user_group_settings_tour.js`** -> AI Confidence: **99.17%**
1224. **`addons/web_tour/static/src/js/tour_pointer/tour_pointer_state.js`** -> AI Confidence: **99.17%**
1225. **`addons/website/static/src/builder/option_sequence.js`** -> AI Confidence: **99.17%**
1226. **`addons/website/static/src/interactions/header/base_header_special.js`** -> AI Confidence: **99.17%**
1227. **`addons/website/static/src/js/content/generate_video_iframe.js`** -> AI Confidence: **99.17%**
1228. **`addons/website/static/src/js/content/snippets.animation.js`** -> AI Confidence: **99.17%**
1229. **`addons/website/static/src/snippets/s_countdown/countdown.js`** -> AI Confidence: **99.17%**
1230. **`addons/website/static/tests/tours/snippet_background_edition.js`** -> AI Confidence: **99.17%**
1231. **`addons/website_blog/static/tests/tours/blog_sidebar_with_date_and_tag.js`** -> AI Confidence: **99.17%**
1232. **`addons/website_livechat/static/tests/tours/website_livechat_chatbot_redirect.js`** -> AI Confidence: **99.17%**
1233. **`addons/website_sale_slides/static/src/js/slides_course_join.js`** -> AI Confidence: **99.17%**
1234. **`addons/account/tests/test_account_payment_register.py`** -> AI Confidence: **99.16%**
1235. **`addons/account/tests/test_sequence_mixin.py`** -> AI Confidence: **99.16%**
1236. **`addons/account_peppol/tests/test_peppol_messages.py`** -> AI Confidence: **99.16%**
1237. **`addons/auth_oauth/controllers/main.py`** -> AI Confidence: **99.16%**
1238. **`addons/bus/models/bus.py`** -> AI Confidence: **99.16%**
1239. **`addons/bus/tests/common.py`** -> AI Confidence: **99.16%**
1240. **`addons/crm/tests/test_crm_lead.py`** -> AI Confidence: **99.16%**
1241. **`addons/digest/tests/test_digest.py`** -> AI Confidence: **99.16%**
1242. **`addons/google_calendar/tests/test_sync_common.py`** -> AI Confidence: **99.16%**
1243. **`addons/google_calendar/utils/google_calendar.py`** -> AI Confidence: **99.16%**
1244. **`addons/hr_timesheet/controllers/portal.py`** -> AI Confidence: **99.16%**
1245. **`addons/iot_drivers/controllers/driver.py`** -> AI Confidence: **99.16%**
1246. **`addons/iot_drivers/controllers/homepage.py`** -> AI Confidence: **99.16%**
1247. **`addons/l10n_dk_nemhandel/tests/test_nemhandel_messages.py`** -> AI Confidence: **99.16%**
1248. **`addons/l10n_es_edi_facturae/tests/test_edi_xml.py`** -> AI Confidence: **99.16%**
1249. **`addons/l10n_hr_edi/tests/test_flows.py`** -> AI Confidence: **99.16%**
1250. **`addons/l10n_hu_edi/models/l10n_hu_edi_connection.py`** -> AI Confidence: **99.16%**
1251. **`addons/l10n_pl_edi/tools/ksef_api_service.py`** -> AI Confidence: **99.16%**
1252. **`addons/mail/controllers/attachment.py`** -> AI Confidence: **99.16%**
1253. **`addons/mail/models/discuss/mail_guest.py`** -> AI Confidence: **99.16%**
1254. **`addons/mail/tests/discuss/test_discuss_channel.py`** -> AI Confidence: **99.16%**
1255. **`addons/mass_mailing/tests/test_mailing_internals.py`** -> AI Confidence: **99.16%**
1256. **`addons/microsoft_calendar/tests/test_create_events.py`** -> AI Confidence: **99.16%**
1257. **`addons/payment_mercado_pago/models/payment_provider.py`** -> AI Confidence: **99.16%**
1258. **`addons/payment_paypal/models/payment_provider.py`** -> AI Confidence: **99.16%**
1259. **`addons/payment_razorpay/models/payment_provider.py`** -> AI Confidence: **99.16%**
1260. **`addons/payment_stripe/controllers/main.py`** -> AI Confidence: **99.16%**
1261. **`addons/point_of_sale/tests/test_frontend.py`** -> AI Confidence: **99.16%**
1262. **`addons/purchase_stock/tests/test_purchase_order.py`** -> AI Confidence: **99.16%**
1263. **`addons/purchase_stock/tests/test_stockvaluation.py`** -> AI Confidence: **99.16%**
1264. **`addons/rating/controllers/main.py`** -> AI Confidence: **99.16%**
1265. **`addons/test_import_export/tests/test_load.py`** -> AI Confidence: **99.16%**
1266. **`addons/test_mail/tests/test_mail_activity_mixin.py`** -> AI Confidence: **99.16%**
1267. **`addons/web/controllers/database.py`** -> AI Confidence: **99.16%**
1268. **`addons/web/controllers/home.py`** -> AI Confidence: **99.16%**
1269. **`addons/web/tests/test_db_manager.py`** -> AI Confidence: **99.16%**
1270. **`addons/website_event_exhibitor/controllers/exhibitor.py`** -> AI Confidence: **99.16%**
1271. **`addons/website_sale/tests/test_website_sale_cart.py`** -> AI Confidence: **99.16%**
1272. **`odoo/addons/base/models/ir_http.py`** -> AI Confidence: **99.16%**
1273. **`odoo/addons/base/tests/test_db_cursor.py`** -> AI Confidence: **99.16%**
1274. **`odoo/addons/base/tests/test_ir_attachment.py`** -> AI Confidence: **99.16%**
1275. **`odoo/addons/base/tests/test_ir_cron.py`** -> AI Confidence: **99.16%**
1276. **`odoo/addons/base/tests/test_ir_sequence.py`** -> AI Confidence: **99.16%**
1277. **`odoo/addons/base/tests/test_reports.py`** -> AI Confidence: **99.16%**
1278. **`odoo/addons/base/wizard/base_import_language.py`** -> AI Confidence: **99.16%**
1279. **`odoo/addons/test_http/tests/test_registry.py`** -> AI Confidence: **99.16%**
1280. **`odoo/addons/test_http/tests/test_session.py`** -> AI Confidence: **99.16%**
1281. **`odoo/addons/test_http/tests/test_static.py`** -> AI Confidence: **99.16%**
1282. **`odoo/addons/test_lint/tests/test_pylint.py`** -> AI Confidence: **99.16%**
1283. **`odoo/addons/test_orm/tests/test_properties.py`** -> AI Confidence: **99.16%**
1284. **`odoo/addons/test_translation_import/tests/test_term_count.py`** -> AI Confidence: **99.16%**
1285. **`odoo/cli/server.py`** -> AI Confidence: **99.16%**
1286. **`odoo/cli/shell.py`** -> AI Confidence: **99.16%**
1287. **`odoo/cli/upgrade_code.py`** -> AI Confidence: **99.16%**
1288. **`odoo/tests/loader.py`** -> AI Confidence: **99.16%**
1289. **`odoo/tools/pdf/signature.py`** -> AI Confidence: **99.16%**
1290. **`addons/html_builder/static/src/builder.js`** -> AI Confidence: **99.16%**
1291. **`addons/html_builder/static/src/core/anchor/anchor_plugin.js`** -> AI Confidence: **99.16%**
1292. **`addons/html_builder/static/src/core/media_website_plugin.js`** -> AI Confidence: **99.16%**
1293. **`addons/html_builder/static/src/plugins/background_option/background_image_option_plugin.js`** -> AI Confidence: **99.16%**
1294. **`addons/html_builder/static/src/plugins/background_option/background_position_option_plugin.js`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `odoo/tools/arabic_reshaper/letters.py` -> **12.3659%** Exposure
- `odoo/tools/urls.py` -> **0.0331%** Exposure
- `odoo/addons/base/tests/test_misc.py` -> **0.0095%** Exposure
- `addons/web/static/src/core/network/download.js` -> **0.0003%** Exposure
### Exploit Generation Surface
- `addons/account/models/account_account.py` -> **100.0%** Exposure
- `addons/account/models/account_document_import_mixin.py` -> **100.0%** Exposure
- `addons/account/models/account_journal.py` -> **100.0%** Exposure
- `addons/account/models/account_journal_dashboard.py` -> **100.0%** Exposure
- `addons/account/models/account_lock_exception.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `addons/account/models/account_account.py` -> **100.0%** Exposure
- `addons/account/models/account_reconcile_model.py` -> **100.0%** Exposure
- `addons/account/models/chart_template.py` -> **100.0%** Exposure
- `addons/account/tests/test_sequence_mixin.py` -> **100.0%** Exposure
- `addons/account/wizard/account_merge_wizard.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `addons/payment/views/express_checkout_templates.xml` -> **100.0%** Exposure
- `addons/website_slides/data/website_data.xml` -> **100.0%** Exposure
- `addons/account/tests/test_account_account.py` -> **85.6275%** Exposure
### Algorithmic DoS Exposure
- `addons/account/controllers/portal.py` -> **100.0%** Exposure
- `addons/account/models/account_account.py` -> **100.0%** Exposure
- `addons/account/models/account_analytic_line.py` -> **100.0%** Exposure
- `addons/account/models/account_bank_statement.py` -> **100.0%** Exposure
- `addons/account/models/account_document_import_mixin.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `763` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36620` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `addons/html_editor/static/src/fields/html_field.js` (JAVASCRIPT) -> Cumulative Risk: **998.61**
- **Archetype:** `file_cluster_4` (Distance: 13.616 IQR)
- **Magnitude:** 640.16 | **LOC:** 442 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getConfig` (Impact: 83.1), `setup` (Impact: 40.6), `value` (Impact: 35.3)

### 2. `addons/point_of_sale/static/src/app/services/pos_store.js` (JAVASCRIPT) -> Cumulative Risk: **995.54**
- **Archetype:** `file_cluster_4` (Distance: 14.042 IQR)
- **Magnitude:** 2494.58 | **LOC:** 2977 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `printChanges` (Impact: 143.3), `deleteOrders` (Impact: 107.5), `processProductAttributes` (Impact: 95.8)

### 3. `addons/api_doc/static/src/components/doc_table.js` (JAVASCRIPT) -> Cumulative Risk: **985.14**
- **Archetype:** `file_cluster_17` (Distance: 14.64 IQR)
- **Magnitude:** 357.3 | **LOC:** 175 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `scheduleHide` (Impact: 30.7), `showDynamicTooltip` (Impact: 22.9), `computeItems` (Impact: 22.1)

### 4. `addons/web/static/src/core/errors/error_dialogs.js` (JAVASCRIPT) -> Cumulative Risk: **983.31**
- **Archetype:** `file_cluster_13` (Distance: 12.941 IQR)
- **Magnitude:** 315.08 | **LOC:** 241 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `inferTitle` (Impact: 40.0), `setup` (Impact: 17.4), `setup` (Impact: 14.6)

### 5. `addons/mrp/static/src/widgets/timer.js` (JAVASCRIPT) -> Cumulative Risk: **976.55**
- **Archetype:** `file_cluster_4` (Distance: 13.558 IQR)
- **Magnitude:** 241.96 | **LOC:** 130 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `setup` (Impact: 18.1), `setup` (Impact: 15.3), `_runSleepTimer` (Impact: 14.6)

### 6. `addons/mail/static/src/discuss/core/common/channel_invitation.js` (JAVASCRIPT) -> Cumulative Risk: **976.06**
- **Archetype:** `file_cluster_17` (Distance: 14.861 IQR)
- **Magnitude:** 728.52 | **LOC:** 254 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `invitationButtonText` (Impact: 92.4), `onClickInvite` (Impact: 48.3), `fetchPartnersToInvite` (Impact: 31.9)

### 7. `addons/pos_self_order/static/src/app/components/preset_info_popup/preset_info_popup.js` (JAVASCRIPT) -> Cumulative Risk: **976.0**
- **Archetype:** `file_cluster_4` (Distance: 14.668 IQR)
- **Magnitude:** 292.78 | **LOC:** 143 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `setup` (Impact: 69.1), `setInformations` (Impact: 54.2), `states` (Impact: 8.0)

### 8. `addons/point_of_sale/static/src/app/screens/scale_screen/scale_service.js` (JAVASCRIPT) -> Cumulative Risk: **974.7**
- **Archetype:** `file_cluster_4` (Distance: 13.959 IQR)
- **Magnitude:** 353.66 | **LOC:** 172 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `setProduct` (Impact: 20.4), `readWeight` (Impact: 14.5), `_readWeightContinuously` (Impact: 14.2)

### 9. `addons/web/static/src/core/autocomplete/autocomplete.js` (JAVASCRIPT) -> Cumulative Risk: **973.71**
- **Archetype:** `file_cluster_4` (Distance: 14.185 IQR)
- **Magnitude:** 1114.44 | **LOC:** 502 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `onInputKeydown` (Impact: 143.3), `navigate` (Impact: 106.3), `setup` (Impact: 50.0)

### 10. `addons/iot_drivers/static/src/app/components/dialog/UpdateDialog.js` (JAVASCRIPT) -> Cumulative Risk: **973.47**
- **Archetype:** `file_cluster_4` (Distance: 12.223 IQR)
- **Magnitude:** 178.68 | **LOC:** 158 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getVersionInfo` (Impact: 22.6), `updateGitTree` (Impact: 22.5), `forceUpdateIotHandlers` (Impact: 17.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `addons/account/models/account_payment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.488 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.223 IQR)
- **Top Global Matches:** file_cluster_8: 10.488, file_cluster_7: 10.834, file_cluster_0: 10.96
- **Magnitude:** 21417.84 | **LOC:** 1246 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.2517%), Tech Debt (12.5569%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 120`, `args: 77`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 91`, `dead_code: 1`, `fragile_debt: 3`
* *Architecture:* `api: 19`, `import: 4`
* *Defense:* `safety: 1`, `doc: 65`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` itertools, odoo.tools, odoo, odoo.exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/orm/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.473 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.28 IQR)
- **Top Global Matches:** file_cluster_0: 13.473, file_cluster_13: 13.527, file_cluster_11: 13.535
- **Magnitude:** 15437.1 | **LOC:** 7128 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (33.706%), Tech Debt (20.3515%)
**Top Internal Functions/Classes:**
  * `_read_group_groupby` (Impact: 3833.9 | O(2^N) | DB: 15)
    * *Intent:* # The following logic is a recursive decomposition strategy. It's complex # but necessary to prevent...
  * `_check_field_access` (Impact: 2940.1 | O(2^N) | DB: 19)
  * `_parent_store_update_prepare` (Impact: 1177.4 | O(N^6) | DB: 23)
  * `name_create` (Impact: 997.0 | O(2^N) | DB: 8)
    * *Intent:* """ defaults = {} parent_fields = defaultdict(list) ir_defaults = self.env['ir.default']._get_model_...
  * `_extract_records` (Impact: 605.6 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1642`, `structural_boundaries: 840`, `args: 273`, `func_start: 240`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 490`, `dead_code: 19`, `planned_debt: 21`, `duplicate_logic: 8`
* *Architecture:* `io: 15`, `api: 131`, `import: 50`
* *Defense:* `safety: 179`, `doc: 585`, `test: 21`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` babel, .table_objects, .fields_properties, .environments, typing, .types, babel.dates, pytz...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `addons/mail/tests/common.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.706 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.299 IQR)
- **Top Global Matches:** file_cluster_8: 11.706, file_cluster_13: 11.707, file_cluster_7: 11.773
- **Magnitude:** 11245.9 | **LOC:** 2082 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (12.3598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format_and_process` (Impact: 10556.0 | O(2^N) | DB: 22)
  * `_activate_multi_lang` (Impact: 182.5 | O(N^5) | DB: 7)
  * `assertBusNotifications` (Impact: 115.7 | O(N^5))
    * *Intent:* # find message if messages: message = messages.filtered(lambda message: ( mbody in message.body and ...
  * `format` (Impact: 31.5 | O(2^N))
    * *Intent:* # ------------------------------------------------------------ # GATEWAY TOOLS # -------------------...
  * `assertBusNotificationType` (Impact: 31.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 444`, `structural_boundaries: 237`, `args: 89`, `func_start: 83`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 50`, `import: 33`
* *Defense:* `safety: 18`, `doc: 151`, `test: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` base64, time, email.policy, odoo.addons.mail.models.mail_mail, odoo, odoo.addons.mail.models.res_users, odoo.addons.base.tests.common, odoo.addons.bus.tests.common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account/models/account_move.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.935 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.293 IQR)
- **Top Global Matches:** file_cluster_8: 11.935, file_cluster_7: 12.107, file_cluster_0: 12.275
- **Magnitude:** 10827.56 | **LOC:** 7257 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (18.3808%), Tech Debt (13.9531%)
**Top Internal Functions/Classes:**
  * `_recompute_cash_rounding_lines` (Impact: 5178.6 | O(2^N) | DB: 27)
  * `_calculate_hashes` (Impact: 3488.2 | O(N^6) | DB: 54)
    * *Intent:* """ Returns a dictionnary containing the suggested values when creating a new line with the quick_ed...
  * `_onchange_name_warning` (Impact: 167.0 | O(N^6) | DB: 4)
  * `_get_chains_to_hash` (Impact: 112.8 | O(N^6) | DB: 1)
    * *Intent:* *self.env['account.move.line']._check_company_domain(company_id),
  * `_onchange_invoice_cash_rounding_id` (Impact: 106.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1668`, `structural_boundaries: 863`, `args: 500`, `func_start: 380`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 297`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `io: 1`, `api: 87`, `import: 23`
* *Defense:* `safety: 27`, `doc: 333`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` odoo, ast, odoo.tools, odoo.exceptions, odoo.tools.mail, dateutil.relativedelta, odoo.tools.safe_eval, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account/models/account_move_line.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.323 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.268 IQR)
- **Top Global Matches:** file_cluster_8: 11.323, file_cluster_7: 11.575, file_cluster_0: 11.731
- **Magnitude:** 8636.82 | **LOC:** 3713 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (25.3402%), Tech Debt (8.2381%)
**Top Internal Functions/Classes:**
  * `_check_constrains_account_id_journal_id` (Impact: 5729.1 | O(2^N) | DB: 42)
  * `_validate_analytic_distribution` (Impact: 1689.2 | O(2^N) | DB: 18)
  * `_compute_epd_needed` (Impact: 539.3 | O(N^6) | DB: 6)
  * `_compute_discount_allocation_needed` (Impact: 93.4 | O(N^6) | DB: 2)
  * `_get_computed_taxes` (Impact: 49.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 906`, `structural_boundaries: 362`, `args: 221`, `func_start: 163`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 196`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 47`, `import: 11`
* *Defense:* `safety: 19`, `doc: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` odoo.fields, collections, odoo.tools, re, odoo.exceptions, odoo.addons.web.controllers.utils, datetime, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/mail/models/mail_thread.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.384 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.308 IQR)
- **Top Global Matches:** file_cluster_8: 12.384, file_cluster_7: 12.501, file_cluster_13: 12.542
- **Magnitude:** 7945.78 | **LOC:** 5097 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (22.0107%), Tech Debt (13.2868%)
**Top Internal Functions/Classes:**
  * `_search_has_message` (Impact: 2599.1 | O(N^6) | DB: 31)
  * `message_notify` (Impact: 1062.1 | O(N^6) | DB: 3)
  * `message_parse` (Impact: 988.7 | O(N^6) | DB: 15)
    * *Intent:* # update document-dependant values msg_dict.update(**self._message_parse_post_process(message, msg_d...
  * `_web_push_send_notification` (Impact: 706.3 | O(N^6) | DB: 2)
  * `_process_attachments_for_post` (Impact: 357.7 | O(N^6) | DB: 3)
    * *Intent:* """ in_reply_to = msg_dict['in_reply_to'] if in_reply_to: parent = self.env['mail.message'].search( ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1061`, `structural_boundaries: 438`, `args: 153`, `func_start: 139`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 192`, `dead_code: 16`, `planned_debt: 4`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 23`, `import: 30`
* *Defense:* `safety: 60`, `doc: 440`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` werkzeug, base64, time, email.message, email.policy, odoo, pytz, odoo.tools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/addons/base/models/ir_ui_view.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.697 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.5 IQR)
- **Top Global Matches:** file_cluster_0: 12.697, file_cluster_8: 12.744, file_cluster_13: 12.749
- **Magnitude:** 7743.32 | **LOC:** 3621 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (32.0868%), Tech Debt (8.3657%)
**Top Internal Functions/Classes:**
  * `_valid_inheritance` (Impact: 1607.4 | O(2^N) | DB: 5)
  * `_validate_tag_filter` (Impact: 1381.6 | O(N^6) | DB: 2)
  * `_compute_arch_diff` (Impact: 1086.5 | O(N^6) | DB: 44)
  * `_log_view_warning` (Impact: 584.7 | O(N^6) | DB: 11)
  * `_postprocess_view` (Impact: 377.3 | O(N^6) | DB: 6)
    * *Intent:* #------------------------------------------------------ # Postprocessing: translation, groups and mo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 496`, `args: 176`, `func_start: 171`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 283`, `dead_code: 12`, `planned_debt: 4`
* *Architecture:* `api: 73`, `import: 25`
* *Defense:* `safety: 76`, `doc: 251`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` odoo, odoo.tools.template_inheritance, odoo.tools, lxml.builder, odoo.exceptions, functools, pprint, odoo.tools.view_validation...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/web/static/tests/_framework/mock_server/mock_model.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.727 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.493 IQR)
- **Top Global Matches:** file_cluster_8: 13.727, file_cluster_17: 13.886, file_cluster_7: 13.915
- **Magnitude:** 7494.34 | **LOC:** 3798 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (44.784%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `orderByField` (Impact: 748.2 | O(2^N) | DB: 7)
  * `formatted_read_group` (Impact: 583.8 | O(N^6) | DB: 22)
  * `parseView` (Impact: 576.9 | O(2^N) | DB: 2)
  * `_openGroups` (Impact: 574.5 | O(2^N) | DB: 12)
    * *Intent:* /** * @type {KwArgs<{
  * `_write` (Impact: 389.0 | O(N^6) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 853`, `structural_boundaries: 353`, `args: 210`, `func_start: 177`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 668`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 26`
* *Architecture:* `api: 19`, `import: 8`
* *Defense:* `safety: 190`, `doc: 392`, `immutability_locks: 443`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.72
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` objects, mock_server_utils, fields, hoot, view, domain, arrays, mock_fields...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `addons/stock/models/stock_move.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.201 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.463 IQR)
- **Top Global Matches:** file_cluster_8: 11.201, file_cluster_7: 11.493, file_cluster_0: 11.687
- **Magnitude:** 7223.22 | **LOC:** 2676 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (30.6207%), Tech Debt (33.949%)
**Top Internal Functions/Classes:**
  * `split_lots` (Impact: 4462.4 | O(2^N) | DB: 28)
  * `_compute_display_name` (Impact: 381.6 | O(N^6) | DB: 2)
    * *Intent:* # We override the default_get to make stock moves created after the picking was confirmed # directly...
  * `_compute_forecast_information` (Impact: 159.5 | O(N^5) | DB: 2)
  * `_match_searched_availability` (Impact: 147.3 | O(N^4))
  * `_set_quantity_done_prepare_vals` (Impact: 131.4 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 789`, `structural_boundaries: 348`, `args: 199`, `func_start: 140`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 139`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 15`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 3`, `doc: 80`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` itertools, operator, odoo.tools.misc, collections, re, odoo.exceptions, odoo.tools.float_utils, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/mrp/models/mrp_production.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.907 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.523 IQR)
- **Top Global Matches:** file_cluster_8: 11.907, file_cluster_7: 12.196, file_cluster_0: 12.256
- **Magnitude:** 6240.54 | **LOC:** 3189 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (47.4176%), Tech Debt (13.5639%)
**Top Internal Functions/Classes:**
  * `action_view_mrp_production_sources` (Impact: 2645.7 | O(N^6) | DB: 87)
  * `_compute_components_availability` (Impact: 2099.7 | O(N^6) | DB: 15)
  * `_get_moves_finished_values` (Impact: 751.1 | O(2^N) | DB: 10)
  * `_compute_picking_type_id` (Impact: 57.5 | O(N^4))
  * `_compute_locations` (Impact: 39.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 893`, `structural_boundaries: 427`, `args: 274`, `func_start: 169`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 326`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 2`, `orphaned_logic: 6`
* *Architecture:* `api: 43`, `import: 14`
* *Defense:* `safety: 3`, `doc: 59`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` odoo.tools.misc, collections, odoo.tools, re, odoo.exceptions, math, odoo.addons.web.controllers.utils, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/orm/fields_relational.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.006 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_17: 13.006, file_cluster_13: 13.071, file_cluster_8: 13.185
- **Magnitude:** 6225.94 | **LOC:** 1773 | **CtrlFlow:** 66.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (38.587%), Tech Debt (71.7746%)
**Top Internal Functions/Classes:**
  * `__get__` (Impact: 4159.6 | O(2^N) | DB: 24)
  * `write_real` (Impact: 429.1 | O(N^6) | DB: 2)
  * `write_real` (Impact: 299.4 | O(N^6) | DB: 7)
  * `write_new` (Impact: 284.3 | O(N^6) | DB: 1)
    * *Intent:* # determine the corecords for which the relation has changed modified_corecord_ids = set() # process...
  * `setup_nonrelated` (Impact: 269.4 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 536`, `structural_boundaries: 270`, `args: 104`, `func_start: 92`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 145`, `dead_code: 10`, `planned_debt: 2`, `duplicate_logic: 11`
* *Architecture:* `api: 67`, `import: 21`
* *Defense:* `safety: 110`, `doc: 62`, `test: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .fields_reference, .models, typing, .types, operator, odoo.tools, odoo.exceptions, .commands...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `addons/mrp/report/mrp_report_bom_structure.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.859 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.096 IQR)
- **Top Global Matches:** file_cluster_8: 9.859, file_cluster_7: 10.336, file_cluster_0: 10.4
- **Magnitude:** 5635.52 | **LOC:** 858 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (39.0389%), Tech Debt (10.3158%)
**Top Internal Functions/Classes:**
  * `_get_bom_data` (Impact: 4954.1 | O(2^N) | DB: 14)
  * `_simulate_operation_planning` (Impact: 172.1 | O(2^N) | DB: 1)
  * `_get_components_closest_forecasted` (Impact: 151.0 | O(N^6) | DB: 3)
    * *Intent:* """ Returns a dict mapping products to a dict of their corresponding BoM lines, which are mapped to ...
  * `_get_report_data` (Impact: 89.0 | O(N^5))
  * `_simulate_bom_planning` (Impact: 88.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 115`, `args: 33`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 56`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` collections, odoo.tools, odoo.exceptions, datetime, odoo, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/orm/registry.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.279 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.828 IQR)
- **Top Global Matches:** file_cluster_13: 13.279, file_cluster_16: 13.464, file_cluster_11: 13.468
- **Magnitude:** 5583.58 | **LOC:** 1255 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 86
- **Risk Profile:** Cognitive Load (28.5086%), Tech Debt (10.0392%)
**Top Internal Functions/Classes:**
  * `_unaccent` (Impact: 5361.3 | O(2^N) | DB: 86)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 212`, `args: 59`, `func_start: 57`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 150`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `io: 9`, `api: 45`, `concurrency: 11`, `import: 36`
* *Defense:* `safety: 84`, `doc: 105`, `test: 7`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` time, odoo.modules.loading, psycopg2.sql, odoo, .environments, typing, operator, odoo.tools...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `addons/test_mail/tests/test_mail_composer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.02 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.319 IQR)
- **Top Global Matches:** file_cluster_8: 10.02, file_cluster_7: 10.328, file_cluster_1: 10.594
- **Magnitude:** 5056.42 | **LOC:** 3780 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (4.3398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setUpClass` (Impact: 3967.4 | O(2^N) | DB: 12)
    * *Intent:* # force 'now' to ease test about schedulers cls.reference_now = FieldDatetime.from_string('2022-12-2...
  * `test_mail_composer_wtpl_mc` (Impact: 269.0 | O(N^6))
  * `test_mail_composer_wtpl_complete` (Impact: 209.7 | O(N^6))
  * `test_mail_composer_duplicates` (Impact: 178.5 | O(N^6) | DB: 8)
  * `test_mail_composer_wtpl_recipients_email` (Impact: 76.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 444`, `structural_boundaries: 141`, `args: 58`, `func_start: 58`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 8`, `fragile_debt: 11`, `duplicate_logic: 6`, `orphaned_logic: 7`
* *Architecture:* `api: 63`, `import: 16`
* *Defense:* `safety: 3`, `doc: 103`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` itertools, base64, odoo.fields, odoo.tests, odoo.tools, odoo.exceptions, odoo.addons.mail.tests.common, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account/models/account_tax.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.674 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.993 IQR)
- **Top Global Matches:** file_cluster_8: 11.674, file_cluster_7: 11.797, file_cluster_1: 12.08
- **Magnitude:** 5035.46 | **LOC:** 5075 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (15.7097%), Tech Debt (9.3477%)
**Top Internal Functions/Classes:**
  * `onchange_amount` (Impact: 4395.1 | O(N^6) | DB: 51)
  * `copy_data` (Impact: 147.0 | O(2^N) | DB: 3)
  * `_sanitize_vals` (Impact: 74.2 | O(N^6) | DB: 5)
  * `_check_company_consistency` (Impact: 22.1 | O(N^4))
  * `_compute_use_in_tax_closing` (Impact: 17.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 864`, `structural_boundaries: 339`, `args: 173`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 195`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 39`, `import: 14`
* *Defense:* `safety: 8`, `doc: 412`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` markupsafe, odoo.tools.misc, odoo.tools.translate, collections, odoo.tools, odoo.exceptions, re, math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/addons/base/models/ir_model.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.816 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_8: 11.816, file_cluster_0: 11.823, file_cluster_13: 11.955
- **Magnitude:** 5027.5 | **LOC:** 2702 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (18.734%), Tech Debt (8.347%)
**Top Internal Functions/Classes:**
  * `_prepare_update` (Impact: 2689.5 | O(2^N) | DB: 9)
  * `_update_selection` (Impact: 448.8 | O(N^6) | DB: 3)
    * *Intent:* """ cr.execute(query, [tuple(model_names)]) existing = {row[:2]: row[2:] for row in cr.fetchall()} #...
  * `_module_data_uninstall` (Impact: 408.2 | O(2^N) | DB: 9)
  * `_unlink_if_manual` (Impact: 271.4 | O(N^6) | DB: 1)
  * `_compute_reference` (Impact: 226.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 638`, `structural_boundaries: 345`, `args: 130`, `func_start: 122`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 1`, `state_mutation: 110`, `dead_code: 7`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 59`, `import: 20`
* *Defense:* `safety: 60`, `doc: 174`, `test: 6`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` itertools, operator, odoo.fields, collections, odoo.tools, odoo.tools.translate, re, odoo.exceptions...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `addons/account_peppol/tools/private_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/iot_box_image/overwrite_after_init/etc/ssl/certs/nginx-cert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/iot_box_image/overwrite_after_init/etc/ssl/private/nginx-cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_facturae/demo/certificate_demo.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_sii/demo/certificates/aeat_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/Bizkaia-IZDesa2025.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/araba_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/gipuzkoa_Iz3np32024.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_verifactu/demo/certificates/Certificado_PF_99999910G_CERTIFICADO_FISICA_PRUEBAS_5_Pre.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `addons/partner_autocomplete/models/res_partner.py` (PYTHON) | Magnitude: 476.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, branch: 53, state_mutation: 44, structural_boundaries: 36
- `addons/im_livechat/static/src/core/common/chat_bubble_patch.js` (JAVASCRIPT) | Magnitude: 17.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, branch: 3, safety: 3
- `addons/im_livechat/static/src/core/common/chatbot_step_model.js` (JAVASCRIPT) | Magnitude: 72.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, state_mutation: 16, structural_boundaries: 11, branch: 10
- `addons/test_event_full/tests/test_performance.py` (PYTHON) | Magnitude: 481.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 339, structural_boundaries: 57, branch: 55, decorators: 52
- `addons/point_of_sale/static/src/app/services/alert_service.js` (JAVASCRIPT) | Magnitude: 9.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, args: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `addons/website/static/src/utils/images.js` (JAVASCRIPT) | Magnitude: 15.26 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, args: 3, branch: 2
- `addons/l10n_my_edi/models/account_move_send.py` (PYTHON) | Magnitude: 8.48 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, encapsulation: 4, doc: 2
- `addons/im_livechat/static/src/js/ajax_external.js` (JAVASCRIPT) | Magnitude: 1.98 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `addons/html_editor/static/src/core/delete_plugin.js` (JAVASCRIPT) | Magnitude: 2208.76 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 775, state_mutation: 333, branch: 191, structural_boundaries: 175
- `addons/sale_product_matrix/models/sale_order.py` (PYTHON) | Magnitude: 233.7 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 101, branch: 30, state_mutation: 22, structural_boundaries: 15
- `addons/html_editor/static/src/others/collaboration/collaboration_plugin.js` (JAVASCRIPT) | Magnitude: 353.08 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 189, state_mutation: 136, doc: 37, branch: 36
- `addons/html_editor/static/src/core/line_break_plugin.js` (JAVASCRIPT) | Magnitude: 86.92 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 86, state_mutation: 43, branch: 22, structural_boundaries: 18
- `odoo/orm/fields_temporal.py` (PYTHON) | Magnitude: 391.46 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 100, branch: 48, doc: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `addons/iot_box_image/build_image.sh` (SHELL) | Magnitude: 41.22 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: reflection_metaprogramming: 40, io: 30, structural_boundaries: 27, safety: 24
- `addons/iot_box_image/configuration/setup_ramdisks.sh` (SHELL) | Magnitude: 14.18 | Delta: **0.092 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 11, state_mutation: 9, safety: 7, indent_spaces: 7
- `addons/website_google_map/static/src/lib/markerclusterer.js` (JAVASCRIPT) | Magnitude: 790.04 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 470, indent_spaces: 221, reflection_metaprogramming: 87, sec_state_mutation: 65
- `setup/debinstall.sh` (SHELL) | Magnitude: 42.82 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, indent_spaces: 11, branch: 8, reflection_metaprogramming: 5
- `addons/iot_box_image/build_utils/download_requirements.sh` (SHELL) | Magnitude: 30.82 | Delta: **0.256 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 19, state_mutation: 17, indent_spaces: 12, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `addons/point_of_sale/static/src/app/components/navbar/proxy_status/proxy_status.js` (JAVASCRIPT) | Magnitude: 92.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 13, structural_boundaries: 12, branch: 6
- `addons/pos_self_order/static/src/app/pages/landing_page/landing_page.js` (JAVASCRIPT) | Magnitude: 189.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 87, structural_boundaries: 25, args: 17
- `addons/l10n_dk_nemhandel/tests/test_nemhandel_participant.py` (PYTHON) | Magnitude: 101.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 26, encapsulation: 15, args: 9
- `odoo/addons/base/models/ir_default.py` (PYTHON) | Magnitude: 242.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 39, branch: 31, doc: 27
- `addons/mail/static/src/core/public_web/discuss_app_model.js` (JAVASCRIPT) | Magnitude: 78.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 25, structural_boundaries: 17, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `addons/account_peppol/exceptions.py` (PYTHON) | Magnitude: 17.0 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 108, encapsulation: 82, branch: 76, closures: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `addons/im_livechat/static/tests/mock_server/mock_models/@types/mock_models.d.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 7, class_start: 3, api: 3
- `addons/web/static/src/@types/registries/fields_registry.d.ts` (TYPESCRIPT) | Magnitude: 2.04 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 33, branch: 23, generics: 21
- `odoo/tools/intervals.py` (PYTHON) | Magnitude: 0.32 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 36, branch: 34, encapsulation: 34
- `odoo/tools/float_utils.py` (PYTHON) | Magnitude: 0.24 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 45, doc: 41, branch: 39
- `odoo/orm/decorators.py` (PYTHON) | Magnitude: 114.98 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 55, api: 28, doc: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `addons/website_sale/static/src/js/product_template_attribute_line/product_template_attribute_line.js` (JAVASCRIPT) | Magnitude: 22.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 14, structural_boundaries: 8, args: 4
- `addons/mail/models/models.py` (PYTHON) | Magnitude: 1933.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 537, branch: 260, structural_boundaries: 128, encapsulation: 119
- `addons/html_builder/static/src/core/drop_zone_plugin.js` (JAVASCRIPT) | Magnitude: 615.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 356, state_mutation: 123, branch: 80, structural_boundaries: 66
- `addons/mail/static/src/discuss/core/common/channel_invitation.js` (JAVASCRIPT) | Magnitude: 728.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 262, indent_spaces: 222, branch: 64, ui_framework: 49
- `addons/html_builder/static/src/core/building_blocks/select_many2x.js` (JAVASCRIPT) | Magnitude: 368.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 171, indent_spaces: 171, concurrency: 54, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `addons/maintenance/static/src/views/calendar_with_recurrence/calendar_with_recurrence_common_popover.js` (JAVASCRIPT) | Magnitude: 14.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, state_mutation: 4, ui_framework: 4
- `addons/web/static/src/views/fields/datetime/datetime_field.js` (JAVASCRIPT) | Magnitude: 687.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 458, state_mutation: 288, branch: 88, structural_boundaries: 69
- `addons/mrp/static/src/components/bom_overview_extra_block/mrp_bom_overview_extra_block.js` (JAVASCRIPT) | Magnitude: 63.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 40, ui_framework: 18, structural_boundaries: 12
- `addons/mass_mailing/static/src/js/mailing_m2o_filter.js` (JAVASCRIPT) | Magnitude: 212.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 174, state_mutation: 76, ui_framework: 35, branch: 30
- `addons/web/static/src/core/color_picker/color_picker.js` (JAVASCRIPT) | Magnitude: 497.48 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 280, state_mutation: 193, structural_boundaries: 55, branch: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `addons/account/static/src/views/file_upload_kanban/file_upload_kanban_renderer.js` (JAVASCRIPT) | Magnitude: 40.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 10, concurrency: 6
- `addons/account/static/src/views/file_upload_list/file_upload_list_renderer.js` (JAVASCRIPT) | Magnitude: 40.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 11, state_mutation: 10, concurrency: 6
- `addons/mail/static/src/chatter/web/mail_composer_form.js` (JAVASCRIPT) | Magnitude: 214.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 121, state_mutation: 39, structural_boundaries: 34, concurrency: 30
- `addons/stock/static/src/widgets/stock_package_m2o.js` (JAVASCRIPT) | Magnitude: 108.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 34, structural_boundaries: 25, concurrency: 12
- `addons/website_event_track/static/src/interactions/website_event_track_proposal_form.js` (JAVASCRIPT) | Magnitude: 191.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 103, indent_spaces: 92, structural_boundaries: 21, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `addons/project_todo/tests/test_todo_quick_create.py` (PYTHON) | Magnitude: 24.26 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, planned_debt: 32, structural_boundaries: 8, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `addons/html_editor/static/src/utils/dom_traversal.js` (JAVASCRIPT) | Magnitude: 325.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 152, state_mutation: 69, doc: 63, structural_boundaries: 61
- `odoo/tools/js_transpiler.py` (PYTHON) | Magnitude: 0.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, doc: 142, structural_boundaries: 91, branch: 50
- `odoo/exceptions.py` (PYTHON) | Magnitude: 40.86 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 29, indent_spaces: 19, structural_boundaries: 14, api: 10
- `addons/payment_aps/utils.py` (PYTHON) | Magnitude: 7.44 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, branch: 2, structural_boundaries: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `addons/payment/utils.py` (PYTHON) | Magnitude: 133.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 53, indent_spaces: 53, structural_boundaries: 37, branch: 25
- `addons/payment_razorpay/controllers/onboarding.py` (PYTHON) | Magnitude: 45.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 22, branch: 8, import: 7
- `addons/point_of_sale/models/account_cash_rounding.py` (PYTHON) | Magnitude: 8.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, import: 2, encapsulation: 2
- `addons/website_sale_loyalty/tests/test_shop_loyalty_payment.py` (PYTHON) | Magnitude: 52.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 17, import: 7, state_mutation: 6
- `addons/im_livechat/static/src/embed/external/boot.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, decorators: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `addons/html_editor/static/src/main/table/table_selection.scss` (CSS) | Magnitude: 0.77 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, class_start: 4, args: 2, dead_code: 2
- `addons/l10n_pl_edi/data/neutralize.sql` (SQLITE) | Magnitude: 1.14 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1, indent_spaces: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `addons/account_edi_ubl_cii/models/account_edi_common.py` -> Churn: **100.0%** | Cog Load: 28.1983% | Debt: 54.5373%
- `addons/spreadsheet/static/src/o_spreadsheet/o_spreadsheet.scss` -> Churn: **67.89%** | Cog Load: 6.6015% | Debt: 53.0725%
- `addons/html_builder/static/src/core/utils.js` -> Churn: **65.88%** | Cog Load: 45.2954% | Debt: 80.0833%
- `addons/point_of_sale/static/src/app/services/pos_store.js` -> Churn: **65.67%** | Cog Load: 100.0% | Debt: 86.1939%
- `addons/pos_sale/static/src/app/services/pos_store.js` -> Churn: **57.82%** | Cog Load: 100.0% | Debt: 9.5404%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `addons/mail/tests/common.py` -> **Renaud Thiry** (100.0% isolated ownership) | Magnitude: 11245.9
- `odoo/addons/base/models/ir_ui_view.py` -> **sagu-odoo** (100.0% isolated ownership) | Magnitude: 7743.32
- `addons/web/static/tests/_framework/mock_server/mock_model.js` -> **Florian Charlier** (100.0% isolated ownership) | Magnitude: 7494.34
- `odoo/orm/registry.py` -> **Alvaro Fuentes** (100.0% isolated ownership) | Magnitude: 5583.58
- `addons/sale_loyalty/models/sale_order.py` -> **Merlin Guillaume** (100.0% isolated ownership) | Magnitude: 4477.52

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `odoo/http.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 81.9235%)
- `odoo/service/server.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9217%)
- `odoo/tools/misc.py` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 98.1183%)
- `odoo/orm/environments.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 93.327%)
- `addons/bus/models/bus.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.2444%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `setup/odoo` -> **Severity: 2116.142** (Blast Radius: 79.382 * Doc Risk: 26.6577%)
- `addons/payment/logging.py` -> **Severity: 851.198** (Blast Radius: 8.512 * Doc Risk: 99.9998%)
- `addons/web/static/src/core/network/rpc.js` -> **Severity: 555.2** (Blast Radius: 5.552 * Doc Risk: 100.0%)
- `addons/web/static/src/core/utils/patch.js` -> **Severity: 517.885** (Blast Radius: 14.56 * Doc Risk: 35.569%)
- `odoo/http.py` -> **Severity: 399.145** (Blast Radius: 5.648 * Doc Risk: 70.6701%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
