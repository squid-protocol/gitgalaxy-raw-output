# ARCHITECTURAL_BRIEF: odoo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/odoo/odoo.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 23557 analyzed artifact(s), 1916861 LOC.
- **Load-bearing artifact:** `setup/odoo` -- 4065 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `addons/web/static/lib/ace/ace.js` -- pulls in 111 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `addons/web/static/lib/ace/ace.js` at magnitude 24005.16 (structural weight, not risk).
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
| Total Artifacts | 46696 |
| Analyzed Artifacts (Scanned) | 23557 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23139 |
| Total LOC | 1916861 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6709 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2469 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5068 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 373 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 8253 | 835038 | 35.0% |
| XML | 6290 | 500 | 26.7% |
| JAVASCRIPT | 5707 | 945122 | 24.2% |
| CSS | 1125 | 68206 | 4.8% |
| MARKDOWN | 1054 | 0 | 4.5% |
| CSV | 848 | 47966 | 3.6% |
| SQLITE | 75 | 485 | 0.3% |
| TYPESCRIPT | 73 | 2394 | 0.3% |
| JSON | 52 | 14905 | 0.2% |
| PLAINTEXT | 46 | 11 | 0.2% |
| SHELL | 18 | 712 | 0.1% |
| HTML | 15 | 1505 | 0.1% |
| MAKEFILE | 1 | 17 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.417`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.42; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 48%, Declarative / Non-Code 12%, Encapsulated Accessors Files 8%, Large Core Modules 6%, Large Core Modules (2) 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22372 | 95.0% |
| Unknown | 11 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1089 | 4.6% |
| Static: Minified & Vendor Opaque Mass | 85 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23139*

**Composition by Extension & Reason:**
- `.po`: 19646x Excluded (Unsupported Extension: '.po')
- `.png`: 1344x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.pot`: 565x Excluded (Unsupported Extension: '.pot')
- `.jpg`: 436x Excluded (Explicitly Denied Extension: '.jpg')
- `.bcmap`: 168x Excluded (Unsupported Extension: '.bcmap')
- `.ftl`: 111x Excluded (Unsupported Extension: '.ftl')
- `.ttf`: 96x Excluded (Explicitly Denied Extension: '.ttf')
- `.webp`: 93x Excluded (Explicitly Denied Extension: '.webp')
- `.xml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 2 exceeds 500 chars), 2x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.py`: 2x Excluded (Machine-Generated Source Code Signature: 19 LOC), 2x Zero-Density Threshold (LOC: 79, Signals: 0), 2x Zero-Density Threshold (LOC: 63, Signals: 0)
- `.js`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 90 exceeds 500 chars)
- `.pdf`: 51x Excluded (Explicitly Denied Extension: '.pdf')
- `no_extension`: 20x Unsupported Format (.undeterminable), 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 5575 LOC), 1x Excluded (Massive Static Asset Blob: 5572 LOC), 1x Excluded (Static Asset Blob without Intent: 1086 LOC)
- `.gif`: 34x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 32.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 15.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10786 | 2399 | 1 | `odoo/addons/base/tests/test_groups.py` |
| cleanup | 1555 | 636 | 0 | `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` |
| guards | 55262 | 6620 | 4 | `addons/web/static/lib/pdfjs/web/viewer.js` |
| danger | 19162 | 3251 | 1 | `addons/web/static/lib/ace/ace.js` |
| concurrency | 83454 | 3080 | 2 | `addons/web/static/tests/views/list/list_view.test.js` |
| connectivity | 50477 | 9394 | 5 | `addons/web/static/lib/pdfjs/web/viewer.css` |
| io | 3474 | 793 | 0 | `odoo/service/server.py` |
| crypto | 171 | 110 | 0 | `odoo/addons/base/models/ir_mail_server.py` |
| ipc | 377 | 133 | 0 | `addons/rpc/controllers/xmlrpc.py` |
| time | 4808 | 962 | 0 | `addons/google_calendar/tests/test_sync_google2odoo.py` |
| serialization | 1051 | 460 | 0 | `addons/html_editor/static/src/others/embedded_component_utils.js` |
| regex | 2873 | 911 | 0 | `addons/web/static/lib/ace/ace.js` |
| events | 12040 | 1729 | 0 | `addons/web/static/lib/ace/ace.js` |
| tests | 69919 | 2854 | 2 | `addons/web/static/tests/views/list/list_view.test.js` |
| docs | 30869 | 5297 | 2 | `addons/web/static/lib/zxing-library/zxing-library.js` |
| debt | 4963 | 1411 | 0 | `addons/web/static/lib/zxing-library/zxing-library.js` |
| mutation | 535737 | 11108 | 45 | `addons/web/static/lib/ace/ace.js` |
| dead_code | 33555 | 7374 | 4 | `odoo/addons/test_orm/tests/test_fields.py` |
| credential | 219 | 110 | 0 | `addons/auth_passkey/tests/test_passkey_demo.py` |
| threat | 8902 | 2825 | 1 | `addons/web/static/lib/ace/ace.js` |
| ml_ai | 3343 | 472 | 0 | `odoo/addons/base/tests/test_mail.py` |
| ui | 19614 | 2315 | 0 | `addons/web/static/lib/pdfjs/web/viewer.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `odoo/service/server.py` (Hits: 106)
- `addons/web/static/tests/core/utils/indexed_db.test.js` (Hits: 67)
- `addons/iot_box_image/overwrite_before_init/etc/init_image.sh` (Hits: 59)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **odoo** (`setup/odoo`) — 4065 inbound connections
2. **owl.js** (`addons/web/static/lib/owl/owl.js`) — 1608 inbound connections
3. **exceptions.py** (`odoo/exceptions.py`) — 1350 inbound connections
4. **hoot.js** (`addons/web/static/lib/hoot/hoot.js`) — 1118 inbound connections
5. **web_test_helpers.js** (`addons/web/static/tests/web_test_helpers.js`) — 1024 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ace.js** (`addons/web/static/lib/ace/ace.js`) — 111 outbound dependencies
2. **plugin_sets.js** (`addons/html_editor/static/src/plugin_sets.js`) — 79 outbound dependencies
3. **common.py** (`odoo/tests/common.py`) — 65 outbound dependencies
4. **http.py** (`odoo/http.py`) — 59 outbound dependencies
5. **mail_test_helpers.js** (`addons/mail/static/tests/mail_test_helpers.js`) — 56 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeActionManager` **(Many-Argument Workhorses)** (@ `addons/web/static/src/webclient/actions/action_service.js`) -> Impact: **668.2** | LOC: 1483
- `findLinkAt` **(Many-Argument Workhorses)** (@ `addons/web/static/lib/ace/ace.js`) -> Impact: **564.2** | LOC: 1238
- `DateTime` **(Many-Argument Workhorses)** (@ `addons/web/static/lib/luxon/luxon.js`) -> Impact: **505.9** | LOC: 2284
  * *Intent:* * * Configuration properties that effect how output strings are formatted, such as `locale`, `numberingSystem`, and `outputCalendar`. * * Here is a br...
- `createRelatedModels` **(Many-Argument Workhorses)** (@ `addons/point_of_sale/static/src/app/models/related_models/index.js`) -> Impact: **446.5** | LOC: 890
- `TextInput` **(Many-Argument Workhorses)** (@ `addons/web/static/lib/ace/ace.js`) -> Impact: **431.0** | LOC: 688
- `Lame` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **413.4** | LOC: 1827
- `PsyModel` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **380.2** | LOC: 1704
  * *Intent:* */ //package mp3; //import java.util.Arrays;
- `createDOMPurify` **(I/O & Config Routines)** (@ `addons/web/static/lib/dompurify/DOMpurify.js`) -> Impact: **366.9** | LOC: 1259
- `Quantize` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **345.6** | LOC: 1432
  * *Intent:* * * You should have received a copy of the GNU Lesser General Public * License along with this library; if not, write to the * Free Software Foundatio...
- `attachmentThumbnailToLinkImg` **(Many-Argument Workhorses)** (@ `addons/mail/static/src/views/web/fields/html_mail_field/convert_inline.js`) -> Impact: **341.2** | LOC: 941
  * *Intent:* /** * Convert CSS display for attachment link to real image. * Without this post process, the display depends on the CSS and the picture * does not ap...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `addons/account/models` | 52 | 31448.06 | 45.77% | 59.25% |
| `odoo/addons/base/models` | 47 | 25797.48 | 45.19% | 39.69% |
| `addons/web/static/lib/ace` | 6 | 25736.44 | 69.65% | 23.3% |
| `odoo/orm` | 23 | 21058.96 | 47.39% | 13.1% |
| `addons/web/static/tests/views/fields` | 69 | 20062.12 | 58.78% | 0.0% |
| `addons/web/static/lib/zxing-library` | 2 | 19893.7 | 31.38% | 33.99% |
| `addons/mail/models` | 60 | 18241.86 | 43.79% | 61.29% |
| `addons/mail/static/lib/lame` | 1 | 17279.56 | 64.9% | 11.45% |
| `addons/stock/models` | 26 | 16387.98 | 48.46% | 45.44% |
| `addons/l10n_es_edi_tbai/demo/certificates` | 3 | 15000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `addons/hr_holidays_attendance/models/hr_leave.py` -> **100.0%** Exposure
- `addons/l10n_account_withholding_tax/models/account_payment_withholding_line.py` -> **100.0%** Exposure
- `addons/product/report/product_label_report.py` -> **100.0%** Exposure
- `addons/test_mail_sms/models/test_mail_sms_models.py` -> **100.0%** Exposure
- `addons/website_sale/models/product_pricelist.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `addons/account/controllers/download_docs.py` -> **100.0%** Exposure
- `addons/account/controllers/portal.py` -> **100.0%** Exposure
- `addons/account/models/account_account.py` -> **100.0%** Exposure
- `addons/account/models/account_analytic_line.py` -> **100.0%** Exposure
- `addons/account/models/account_analytic_plan.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `odoo/addons/test_orm/tests/test_fields.py` -> **195** Orphaned Functions | **4** Duplicates
- `addons/web/static/lib/zxing-library/zxing-library.js` -> **60** Orphaned Functions | **138** Duplicates
- `addons/stock/tests/test_move.py` -> **160** Orphaned Functions | **0** Duplicates
- `addons/mrp/tests/test_order.py` -> **133** Orphaned Functions | **0** Duplicates
- `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` -> **24** Orphaned Functions | **106** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `addons/auth_passkey/_vendor/webauthn/helpers/known_root_certs.py` -> **100.0%** Exposure
- `addons/payment/views/express_checkout_templates.xml` -> **100.0%** Exposure
- `addons/website_slides/data/website_data.xml` -> **100.0%** Exposure
- `addons/account/tests/test_account_account.py` -> **85.6275%** Exposure
- `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` -> **73.1728%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `524` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `42114` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `addons/web/static/lib/ace/ace.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 24005.16 | **LOC:** 21443 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **111**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.4828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findLinkAt` **(Many-Argument Workhorses)** (Impact: 564.2)
  * `TextInput` **(Many-Argument Workhorses)** (Impact: 431.0)
  * `Folding` **(Compute Cores)** (Impact: 267.4)
  * `escapeHTML` **(Defensive Guards)** (Impact: 196.0)
  * `addTouchListeners` **(Compute Cores)** (Impact: 157.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 51 instances
* *Amplified Cascading Flux:* 3818 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 322
* *State Mutation (weighted view):* 12633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5548`, `structural_boundaries: 4690`, `args: 2048`, `func_start: 1655`
* *Risk/State:* `safety_bypasses: 781`, `high_risk_execution: 5`, `state_mutation: 4997`, `dead_code: 1`, `planned_debt: 20`, `fragile_debt: 1`, `duplicate_logic: 23`, `unreferenced_by_name: 106`
* *Architecture:* `io: 1`, `api: 263`, `concurrency: 67`, `import: 250`
* *Defense:* `safety: 642`, `doc: 74`, `test: 1`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ace-internal, lang, oop, range, token_iterator, ace-internal, behaviour, clipboard...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/zxing-library/zxing-library.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 19892.7 | **LOC:** 27952 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (68.0%)
- **Documentation Coverage:** 58.083% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeRow` **(Many-Argument Workhorses)** (Impact: 193.9)
  * `decodeTextCompaction` **(Many-Argument Workhorses)** (Impact: 131.8)
    * *Intent:* * (i.e. values from 32 to 126) and three ASCII control characters: HT or tab * (9: e), LF or line fe...
  * `guessEncoding` **(Many-Argument Workhorses)** (Impact: 129.2)
    * *Intent:* /** * default encoding if none of these can possibly be correct */
  * `lookAheadTestIntern` **(Many-Argument Workhorses)** (Impact: 101.6)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 98.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2611 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 8984
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4272`, `structural_boundaries: 4134`, `args: 1453`, `func_start: 1376`, `class_start: 202`
* *Risk/State:* `safety_bypasses: 191`, `state_mutation: 3762`, `dead_code: 110`, `planned_debt: 31`, `fragile_debt: 5`, `duplicate_logic: 138`, `unreferenced_by_name: 60`
* *Architecture:* `api: 110`, `concurrency: 9`
* *Defense:* `safety: 1158`, `doc: 744`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Float, Integer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/mail/static/lib/lame/lame.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17279.56 | **LOC:** 15525 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.9%)
- **Documentation Coverage:** 62.1528% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Lame` **(I/O & Config Routines)** (Impact: 413.4)
  * `PsyModel` **(I/O & Config Routines)** (Impact: 380.2)
    * *Intent:* */ //package mp3; //import java.util.Arrays;
  * `Quantize` **(I/O & Config Routines)** (Impact: 345.6)
    * *Intent:* * * You should have received a copy of the GNU Lesser General Public * License along with this libra...
  * `lamejs` **(I/O & Config Routines)** (Impact: 336.4)
    * *Intent:* /** * lamejs, a Javascript mp3 encoder library * V.1.2.1 * https://github.com/zhuker/lamejs/blob/mas...
  * `L3psycho_anal_ns` **(Many-Argument Workhorses)** (Impact: 290.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2494 instances
* *State Mutation (weighted view):* 8973
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1992`, `structural_boundaries: 1756`, `args: 284`, `func_start: 284`
* *Risk/State:* `safety_bypasses: 507`, `state_mutation: 3985`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 8`, `unreferenced_by_name: 15`
* *Architecture:* None
* *Defense:* `doc: 357`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/Chart/Chart.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 13375.44 | **LOC:** 14947 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.6%), Complexity Load (formerly Cognitive Load) (73.2%), Debt Markers (formerly Tech Debt) (17.5%)
- **Documentation Coverage:** 88.7763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawPointLegend` **(Many-Argument Workhorses)** (Impact: 99.5)
    * *Intent:* // eslint-disable-next-line complexity
  * `_computeLabelItems` **(Defensive Guards)** (Impact: 93.1)
  * `updateElements` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `generateTicks$1` **(I/O & Config Routines)** (Impact: 45.0)
  * `_computeGridLineItems` **(Defensive Guards)** (Impact: 42.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1590 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 5402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2871`, `structural_boundaries: 1965`, `args: 1366`, `func_start: 1215`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2222`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 14`, `unreferenced_by_name: 54`
* *Architecture:* `api: 1`, `concurrency: 5`
* *Defense:* `safety: 740`, `doc: 106`, `test: 1`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types, 46011
     * @typedef  import(
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/pdfjs/web/viewer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 12414.3 | **LOC:** 15353 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.034; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.5%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.4197% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onKeyDown` **(Defensive Guards)** (Impact: 191.9)
  * `constructor` **(Defensive Guards)** (Impact: 117.7)
  * `setDocument` **(Defensive Guards)** (Impact: 81.2)
  * `onAfterDraw` **(Defensive Guards)** (Impact: 65.7)
  * `_getPageAdvance` **(Many-Argument Workhorses)** (Impact: 65.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 153 instances
* *Amplified Cascading Flux:* 1239 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 1174
* *State Mutation (weighted view):* 4172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3045`, `structural_boundaries: 1930`, `args: 1139`, `func_start: 892`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1694`, `planned_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `io: 5`, `api: 32`, `concurrency: 409`, `import: 3`
* *Defense:* `safety: 1146`, `doc: 23`, `test: 11`, `immutability_locks: 3`, `cleanup: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 4.2e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9045.4 | **LOC:** 13833 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.031; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Debt Markers (formerly Tech Debt) (81.1%), Complexity Load (formerly Cognitive Load) (79.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 98.6)
  * `getExtendedRtpCapabilities` **(Many-Argument Workhorses)** (Impact: 87.3)
    * *Intent:* /** * Generate extended RTP capabilities for sending and receiving. * * Resulting codecs keep order ...
  * `requireMs` **(Compute Cores)** (Impact: 79.2)
  * `parse` **(Compute Cores)** (Impact: 79.2)
    * *Intent:* /** * Parse the given `str` and return milliseconds. * */
  * `setup` **(Defensive Guards)** (Impact: 62.3)
    * *Intent:* /** * This is the common logic for both the Node.js and web browser * implementations of `debug()`. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 145 instances
* *Amplified Cascading Flux:* 810 instances
* *Concurrency (weighted view):* 1254
* *State Mutation (weighted view):* 2951
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2115`, `structural_boundaries: 1654`, `args: 920`, `func_start: 688`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 1331`, `dead_code: 3`, `planned_debt: 10`, `fragile_debt: 9`, `duplicate_logic: 106`, `unreferenced_by_name: 24`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 529`
* *Defense:* `safety: 917`, `doc: 275`, `immutability_locks: 1`, `cleanup: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000181
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/web/static/tests/views/list/list_view.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 7877.02 | **LOC:** 19560 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.3%)
- **Documentation Coverage:** 99.0196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clickFieldDropdownItem` **(Many-Argument Workhorses)** (Impact: 102.8)
  * `callback` **(I/O & Config Routines)** (Impact: 99.6)
  * `doActionButton` **(Compute Cores)** (Impact: 83.1)
  * `extractProps` **(Compute Cores)** (Impact: 67.7)
  * `getServerValue` **(Compute Cores)** (Impact: 35.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 536 instances
* *Amplified Cascading Flux:* 176 instances
* *Concurrency (weighted view):* 5950
* *State Mutation (weighted view):* 928
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 3678`, `args: 878`, `func_start: 102`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 280`, `high_risk_execution: 2`, `state_mutation: 576`, `planned_debt: 12`, `fragile_debt: 13`, `duplicate_logic: 34`, `unreferenced_by_name: 5`
* *Architecture:* `io: 6`, `api: 4`, `concurrency: 3270`, `import: 19`
* *Defense:* `safety: 36`, `doc: 1`, `test: 3303`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` hoot, owl, view_test_helpers, datetime_test_helpers, web_test_helpers, currency, domain, localization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `odoo/orm/models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7612.12 | **LOC:** 7128 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **48**; blast radius 0.033; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (49.7%)
- **Documentation Coverage:** 35.1759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_export_rows` **(Many-Argument Workhorses)** (Impact: 178.1)
    * *Intent:* """ Export fields of the records in ``self``. :param list fields: list of lists of fields to travers...
  * `read_group` **(Many-Argument Workhorses)** (Impact: 153.9)
    * *Intent:* """Deprecated - Get the list of records in list view grouped by the given ``groupby`` fields. :param...
  * `_read_grouping_sets` **(Many-Argument Workhorses)** (Impact: 152.6)
  * `_read_group_fill_temporal` **(Many-Argument Workhorses)** (Impact: 118.6)
  * `_read_group_format_result_properties` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* """Modify the final read group properties result. Replace the relational properties ids by a tuple w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1085 instances
* *State Mutation (weighted view):* 3377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1618`, `structural_boundaries: 854`, `args: 273`, `func_start: 240`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1207`, `dead_code: 19`, `planned_debt: 21`
* *Architecture:* `io: 15`, `api: 148`, `import: 49`
* *Defense:* `safety: 149`, `doc: 209`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.5e-05
  * `Imports (Out-Degree: 18):` , .commands, .domains, .environments, .fields, .fields_misc, .fields_properties, .fields_relational...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `addons/web/static/lib/luxon/luxon.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 7274.28 | **LOC:** 8607 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); blast radius 0.13; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 43.6519% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DateTime` **(Many-Argument Workhorses)** (Impact: 505.9)
    * *Intent:* * * Configuration properties that effect how output strings are formatted, such as `locale`, `number...
  * `Duration` **(Compute Cores)** (Impact: 210.8)
    * *Intent:* /** * * Here is a brief overview of commonly used methods and getters in Duration: * * * There's are...
  * `Interval` **(Compute Cores)** (Impact: 171.6)
    * *Intent:* /** * * Here is a brief overview of the most commonly used methods and getters in Interval: * */
  * `formatDateTimeFromString` **(Compute Cores)** (Impact: 167.4)
  * `Formatter` **(Compute Cores)** (Impact: 140.5)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 739 instances
* *State Mutation (weighted view):* 2373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1440`, `structural_boundaries: 1525`, `args: 625`, `func_start: 937`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 895`, `dead_code: 12`, `planned_debt: 2`, `duplicate_logic: 31`
* *Architecture:* `api: 16`
* *Defense:* `safety: 408`, `doc: 354`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000303
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `addons/account/models/account_move.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6915.16 | **LOC:** 7257 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.2%)
- **Documentation Coverage:** 76.4831% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_post` **(Many-Argument Workhorses)** (Impact: 157.1)
    * *Intent:* """Post/Validate the documents. Posting the documents will give it a number, and check that the docu...
  * `_sync_tax_lines` **(Many-Argument Workhorses)** (Impact: 115.8)
  * `write` **(Compute Cores)** (Impact: 114.3)
  * `_sync_dynamic_line` **(Many-Argument Workhorses)** (Impact: 105.3)
  * `_prepare_invoice_aggregated_taxes` **(Many-Argument Workhorses)** (Impact: 71.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 935 instances
* *State Mutation (weighted view):* 3108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1642`, `structural_boundaries: 892`, `args: 505`, `func_start: 380`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 1238`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 120`
* *Architecture:* `io: 1`, `api: 87`, `import: 23`
* *Defense:* `safety: 24`, `doc: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` ast, calendar, collections, contextlib, datetime, dateutil.relativedelta, documents, hashlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/tests/views/fields/one2many_field.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 5954.2 | **LOC:** 13723 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (81.2%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `name` **(I/O & Config Routines)** (Impact: 44.4)
  * `p` **(I/O & Config Routines)** (Impact: 40.2)
  * `doActionButton` **(Compute Cores)** (Impact: 35.0)
  * `getServerValue` **(Compute Cores)** (Impact: 31.8)
  * `add` **(Many-Argument Workhorses)** (Impact: 16.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 520 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 4266
* *State Mutation (weighted view):* 1012
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 2028`, `args: 621`, `func_start: 123`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 175`, `state_mutation: 666`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 48`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `concurrency: 1666`, `import: 12`
* *Defense:* `safety: 36`, `test: 1521`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` hoot, hoot-dom, hoot-mock, owl, datetime_test_helpers, web_test_helpers, browser, registry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/qunit/qunit-2.9.1.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5796.56 | **LOC:** 6613 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.1%), Complexity Load (formerly Cognitive Load) (98.4%), Guard Balance (formerly Safety Score) (92.1%)
- **Documentation Coverage:** 87.0482% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diff` **(I/O & Config Routines)** (Impact: 239.1)
    * *Intent:* * https://www.apache.org/licenses/LICENSE-2.0 * * Unless required by applicable law or agreed to in ...
  * `Assert` **(I/O & Config Routines)** (Impact: 87.9)
  * `setUrl` **(Compute Cores)** (Impact: 82.4)
  * `diffBisect` **(Many-Argument Workhorses)** (Impact: 82.0)
    * *Intent:* /** * Find the 'middle snake' of a diff, split the problem in two * and return the recursively const...
  * `rejects` **(Many-Argument Workhorses)** (Impact: 52.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 58 instances
* *Amplified Cascading Flux:* 828 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 435
* *State Mutation (weighted view):* 2669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1131`, `structural_boundaries: 746`, `args: 431`, `func_start: 361`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 25`, `state_mutation: 1013`, `dead_code: 2`, `planned_debt: 52`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 7`
* *Architecture:* `io: 5`, `api: 4`, `concurrency: 145`, `import: 1`
* *Defense:* `safety: 448`, `doc: 45`, `test: 39`, `sync_locks: 15`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vertx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/owl/owl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5780.06 | **LOC:** 6341 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1608** in-repo importer(s); blast radius 30.778; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.9589% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileTDomNode` **(Many-Argument Workhorses)** (Impact: 120.1)
  * `parseDOMNode` **(Many-Argument Workhorses)** (Impact: 80.2)
  * `parseComponent` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `buildTree` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `compileComponent` **(Many-Argument Workhorses)** (Impact: 65.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 648 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 139
* *State Mutation (weighted view):* 2187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1365`, `structural_boundaries: 959`, `args: 476`, `func_start: 398`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 891`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 15`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 34`
* *Defense:* `safety: 346`, `doc: 52`, `test: 7`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.072081
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1608):` (Excluded from Brief to save tokens)

### `addons/mail/models/mail_thread.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5243.08 | **LOC:** 5097 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (51.5%)
- **Documentation Coverage:** 39.3939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `message_post` **(Many-Argument Workhorses)** (Impact: 195.4)
    * *Intent:* # ------------------------------------------------------------ # MESSAGE POST MAIN # ---------------...
  * `message_route` **(Many-Argument Workhorses)** (Impact: 132.2)
    * *Intent:* """ Attempt to figure out the correct target model, thread_id, custom_values and user_id to use for ...
  * `message_notify` **(Many-Argument Workhorses)** (Impact: 115.3)
  * `_process_attachments_for_post` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* """ Preprocess attachments for MailTread.message_post() or MailMail.create(). Purpose is to * transf...
  * `_notify_thread_with_out_of_office` **(Many-Argument Workhorses)** (Impact: 92.3)
    * *Intent:* """ Out-of-office automated answer at posting time. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 686 instances
* *State Mutation (weighted view):* 2172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1052`, `structural_boundaries: 462`, `args: 153`, `func_start: 139`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 800`, `dead_code: 16`, `planned_debt: 4`, `unreferenced_by_name: 19`
* *Architecture:* `io: 1`, `api: 23`, `import: 30`
* *Defense:* `safety: 52`, `doc: 109`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` XML, ast, base64, collections, collections.abc, datetime, dateutil, email...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/spreadsheet/static/lib/chartjs-chart-geo/chartjs-chart-geo.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 5130.64 | **LOC:** 5323 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.027; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clipRectangle` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* // TODO Use d3-polygon’s polygonContains here for the ring check? // TODO Eliminate duplicate buffer...
  * `clipLine` **(Many-Argument Workhorses)** (Impact: 106.1)
  * `clipCircle` **(Compute Cores)** (Impact: 77.8)
  * `clipRejoin` **(Many-Argument Workhorses)** (Impact: 55.1)
    * *Intent:* // A generalized polygon clipping algorithm: given a polygon that has been cut // into its visible l...
  * `point` **(Compute Cores)** (Impact: 45.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 559 instances
* *State Mutation (weighted view):* 2027
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 905`, `structural_boundaries: 935`, `args: 604`, `func_start: 528`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 909`, `dead_code: 1`, `planned_debt: 8`, `duplicate_logic: 22`, `unreferenced_by_name: 12`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `safety: 167`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chart.js, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/tests/views/kanban/kanban_view.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 5103.24 | **LOC:** 15026 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (42.2%), Guard Balance (formerly Safety Score) (38.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectRecord` **(Many-Argument Workhorses)** (Impact: 127.5)
  * `selectRecord` **(Many-Argument Workhorses)** (Impact: 67.7)
  * `createRecord` **(I/O & Config Routines)** (Impact: 63.5)
  * `createRecord` **(I/O & Config Routines)** (Impact: 55.9)
  * `createRecord` **(I/O & Config Routines)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 386 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 3670
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 2179`, `args: 605`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 157`, `state_mutation: 425`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 4`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `concurrency: 1740`, `import: 21`
* *Defense:* `safety: 8`, `doc: 1`, `test: 2052`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` hoot, hoot-dom, hoot-mock, owl, condition_tree_editor_test_helpers, web_test_helpers, browser, currency...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account_peppol/tools/private_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/iot_box_image/overwrite_after_init/etc/ssl/certs/nginx-cert.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/iot_box_image/overwrite_after_init/etc/ssl/private/nginx-cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_facturae/demo/certificate_demo.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_sii/demo/certificates/aeat_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/Bizkaia-IZDesa2025.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/araba_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/gipuzkoa_Iz3np32024.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_verifactu/demo/certificates/Certificado_PF_99999910G_CERTIFICADO_FISICA_PRUEBAS_5_Pre.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `addons/account_edi_ubl_cii/models/account_edi_common.py` -> Churn: **100.0%** | Cog Load: 63.3323% | Debt: 87.0584%
- `addons/stock_account/models/product.py` -> Churn: **97.19%** | Cog Load: 65.9341% | Debt: 43.8748%
- `addons/point_of_sale/models/pos_order.py` -> Churn: **91.76%** | Cog Load: 68.1293% | Debt: 65.5399%
- `addons/mrp/models/mrp_production.py` -> Churn: **78.79%** | Cog Load: 71.6994% | Debt: 54.4025%
- `addons/stock/models/stock_move.py` -> Churn: **76.05%** | Cog Load: 69.2968% | Debt: 45.7184%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `addons/web/static/tests/views/fields/one2many_field.test.js` -> **Aaron Bohy** (100.0% isolated ownership) | Magnitude: 5954.2
- `addons/web/static/tests/views/form/form_view.test.js` -> **Corentin Heinix (cohe)** (100.0% isolated ownership) | Magnitude: 4970.08
- `odoo/addons/base/models/ir_ui_view.py` -> **sagu-odoo** (100.0% isolated ownership) | Magnitude: 4195.72
- `addons/web/static/tests/_framework/mock_server/mock_model.js` -> **Florian Charlier** (100.0% isolated ownership) | Magnitude: 3139.82
- `addons/web/models/models.py` -> **Amr Elkhatieb** (100.0% isolated ownership) | Magnitude: 2865.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `odoo/http.py` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)
- `addons/web/static/lib/hoot/hoot_utils.js` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.9359%)
- `odoo/tools/misc.py` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)
- `addons/web/static/lib/hoot/mock/math.js` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 83.2018%)
- `addons/web/static/lib/hoot/core/runner.js` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9983%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `addons/web/static/lib/owl/owl.js` -> **Severity: 6.084** (Embedded: 0.0721 * Error Risk: 84.4033%)
- `addons/payment/logging.py` -> **Severity: 3.964** (Embedded: 0.0416 * Error Risk: 95.2574%)
- `odoo/exceptions.py` -> **Severity: 3.91** (Embedded: 0.0563 * Error Risk: 69.4842%)
- `addons/web/static/lib/hoot/mock/math.js` -> **Severity: 2.898** (Embedded: 0.0413 * Error Risk: 70.2063%)
- `addons/web/static/tests/web_test_helpers.js` -> **Severity: 2.667** (Embedded: 0.0438 * Error Risk: 60.8907%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `addons/web/static/lib/owl/owl.js` -> **Severity: 2645.643** (Blast Radius: 30.778 * Doc Risk: 85.9589%)
- `odoo/exceptions.py` -> **Severity: 716.1** (Blast Radius: 14.322 * Doc Risk: 50.0%)
- `addons/web/static/tests/web_test_helpers.js` -> **Severity: 599.772** (Blast Radius: 10.496 * Doc Risk: 57.1429%)
- `odoo/tests/common.py` -> **Severity: 514.516** (Blast Radius: 7.25 * Doc Risk: 70.9677%)
- `odoo/http.py` -> **Severity: 328.196** (Blast Radius: 5.069 * Doc Risk: 64.7458%)

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
