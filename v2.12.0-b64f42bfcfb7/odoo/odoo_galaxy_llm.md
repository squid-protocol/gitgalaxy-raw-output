# ARCHITECTURAL_BRIEF: odoo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/odoo/odoo.git` |
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
- **Scope:** 23384 analyzed artifact(s), 1869215 LOC.
- **Load-bearing artifact:** `odoo/tests/common.py` -- 1625 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `addons/web/static/lib/ace/ace.js` -- pulls in 111 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `addons/web/static/lib/ace/ace.js` at magnitude 21112.56 (structural weight, not risk).
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
| Total Artifacts | 46701 |
| Analyzed Artifacts (Scanned) | 23384 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 23317 |
| Total LOC | 1869215 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 50.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6157 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1836 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7717 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1684 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 8238 | 843179 | 35.2% |
| XML | 6237 | 495 | 26.7% |
| JAVASCRIPT | 5704 | 901608 | 24.4% |
| MARKDOWN | 1052 | 0 | 4.5% |
| CSS | 1032 | 56503 | 4.4% |
| CSV | 848 | 47966 | 3.6% |
| TYPESCRIPT | 73 | 2394 | 0.3% |
| SQLITE | 70 | 265 | 0.3% |
| JSON | 51 | 14904 | 0.2% |
| PLAINTEXT | 41 | 10 | 0.2% |
| SHELL | 18 | 712 | 0.1% |
| HTML | 14 | 942 | 0.1% |
| POSTGRESQL | 5 | 220 | 0.0% |
| MAKEFILE | 1 | 17 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 23372 |
| unknown | unknown | 10 |
| utf-8 | bom | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 48%, Declarative / Non-Code 12%, Encapsulated Accessors Files 8%, Large Core Modules 6%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 22209 | 95.0% |
| Unknown | 10 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1083 | 4.6% |
| Static: Minified & Vendor Opaque Mass | 82 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 23317*

**Composition by Extension & Reason:**
- `.po`: 19646x Excluded (Unsupported Extension: '.po')
- `.png`: 1344x Excluded (Explicitly Denied Extension: '.png'), 1x Excluded (Explicitly Denied Extension: '.PNG')
- `.pot`: 565x Excluded (Unsupported Extension: '.pot')
- `.jpg`: 436x Excluded (Explicitly Denied Extension: '.jpg')
- `.bcmap`: 168x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ftl`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 17 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 54, Signals: 0)
- `.ttf`: 96x Excluded (Explicitly Denied Extension: '.ttf')
- `.py`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 19 LOC), 2x Zero-Density Threshold (LOC: 79, Signals: 0)
- `.webp`: 93x Excluded (Explicitly Denied Extension: '.webp')
- `.xml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Saturation: Line 2 exceeds 500 chars), 2x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.js`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 17 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 89291 LOC)
- `.svg`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 6122 commas in 663 LOC), 1x Excluded (Static Asset Blob without Intent: 2008 LOC)
- `.pdf`: 51x Excluded (Explicitly Denied Extension: '.pdf')
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable), 5x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.0 | 26.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 93.4 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 15.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10864 | 2409 | 1 | `odoo/addons/base/tests/test_groups.py` |
| cleanup | 1467 | 633 | 0 | `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` |
| guards | 52631 | 6590 | 5 | `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` |
| danger | 18398 | 3231 | 1 | `addons/web/static/lib/ace/ace.js` |
| concurrency | 83108 | 3084 | 2 | `addons/web/static/tests/views/list/list_view.test.js` |
| connectivity | 56457 | 9370 | 6 | `addons/website_sale/static/src/scss/product_tile.scss` |
| io | 3426 | 795 | 0 | `odoo/service/server.py` |
| crypto | 173 | 93 | 0 | `odoo/addons/base/models/ir_mail_server.py` |
| ipc | 330 | 97 | 0 | `addons/rpc/controllers/xmlrpc.py` |
| time | 4764 | 960 | 0 | `addons/google_calendar/tests/test_sync_google2odoo.py` |
| serialization | 1019 | 456 | 0 | `addons/html_editor/static/src/others/embedded_component_utils.js` |
| regex | 2852 | 909 | 0 | `addons/web/static/lib/ace/ace.js` |
| events | 11813 | 1733 | 0 | `addons/web/static/lib/ace/ace.js` |
| tests | 70017 | 2863 | 2 | `addons/web/static/tests/views/list/list_view.test.js` |
| docs | 30200 | 5281 | 2 | `addons/mail/static/lib/lame/lame.js` |
| debt | 5920 | 1486 | 0 | `addons/html_editor/static/tests/paste.test.js` |
| mutation | 526463 | 11098 | 46 | `addons/web/static/lib/ace/ace.js` |
| dead_code | 8593 | 3035 | 1 | `addons/web/static/lib/ace/ace.js` |
| credential | 252 | 135 | 0 | `addons/auth_passkey/tests/test_passkey_demo.py` |
| threat | 451 | 55 | 0 | `addons/web/static/src/core/emoji_picker/emoji_data.js` |
| ml_ai | 119 | 24 | 0 | `addons/web/static/src/views/fields/statusbar/statusbar_field.scss` |
| ui | 18682 | 2271 | 0 | `addons/mail/static/src/discuss/call/common/rtc_service.js` |

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

1. **common.py** (`odoo/tests/common.py`) — 1625 inbound connections
2. **exceptions.py** (`odoo/exceptions.py`) — 1369 inbound connections
3. **__init__.py** (`odoo/tests/__init__.py`) — 1282 inbound connections
4. **__init__.py** (`odoo/tools/__init__.py`) — 913 inbound connections
5. **commands.py** (`odoo/orm/commands.py`) — 888 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ace.js** (`addons/web/static/lib/ace/ace.js`) — 111 outbound dependencies
2. **__init__.py** (`odoo/addons/base/tests/__init__.py`) — 82 outbound dependencies
3. **plugin_sets.js** (`addons/html_editor/static/src/plugin_sets.js`) — 79 outbound dependencies
4. **__init__.py** (`addons/account/tests/__init__.py`) — 69 outbound dependencies
5. **common.py** (`odoo/tests/common.py`) — 66 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `lamejs` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **2768.8** | LOC: 15516
  * *Intent:* /** * lamejs, a Javascript mp3 encoder library * V.1.2.1 * https://github.com/zhuker/lamejs/blob/master/LICENSE */
- `makeActionManager` **(Many-Argument Workhorses)** (@ `addons/web/static/src/webclient/actions/action_service.js`) -> Impact: **616.3** | LOC: 1483
- `PsyModel` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **594.0** | LOC: 2661
  * *Intent:* */ //package mp3; //import java.util.Arrays;
- `DateTime` **(Many-Argument Workhorses)** (@ `addons/web/static/lib/luxon/luxon.js`) -> Impact: **504.5** | LOC: 2284
  * *Intent:* * * Configuration properties that effect how output strings are formatted, such as `locale`, `numberingSystem`, and `outputCalendar`. * * Here is a br...
- `createRelatedModels` **(Many-Argument Workhorses)** (@ `addons/point_of_sale/static/src/app/models/related_models/index.js`) -> Impact: **444.5** | LOC: 890
- `TextInput` **(Many-Argument Workhorses)** (@ `addons/web/static/lib/ace/ace.js`) -> Impact: **431.0** | LOC: 688
- `Lame` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **413.4** | LOC: 1827
- `createDOMPurify` **(I/O & Config Routines)** (@ `addons/web/static/lib/dompurify/DOMpurify.js`) -> Impact: **365.9** | LOC: 1259
- `Quantize` **(I/O & Config Routines)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **345.6** | LOC: 1432
  * *Intent:* * * You should have received a copy of the GNU Lesser General Public * License along with this library; if not, write to the * Free Software Foundatio...
- `L3psycho_anal_ns` **(Many-Argument Workhorses)** (@ `addons/mail/static/lib/lame/lame.js`) -> Impact: **290.8** | LOC: 376

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `addons/account/models` | 55 | 33182.86 | 45.74% | 2.44% |
| `odoo/addons/base/models` | 48 | 29299.28 | 45.31% | 6.04% |
| `addons/web/static/lib/ace` | 6 | 22637.44 | 66.58% | 19.41% |
| `odoo/orm` | 23 | 21256.26 | 47.39% | 11.29% |
| `addons/mail/static/lib/lame` | 1 | 19925.76 | 65.55% | 11.34% |
| `addons/web/static/tests/views/fields` | 69 | 18933.92 | 47.94% | 0.0% |
| `addons/mail/models` | 62 | 18776.24 | 44.21% | 5.6% |
| `addons/stock/models` | 26 | 16519.28 | 48.46% | 3.09% |
| `addons/l10n_es_edi_tbai/demo/certificates` | 3 | 15000.0 | 0.0% | 0.0% |
| `addons/account/tests` | 70 | 14628.04 | 10.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `addons/product/report/product_label_report.py` -> **100.0%** Exposure
- `addons/test_mail_sms/models/test_mail_sms_models.py` -> **100.0%** Exposure
- `odoo/tools/pdf/_pypdf.py` -> **100.0%** Exposure
- `addons/im_livechat/static/src/core/common/thread_actions_patch.js` -> **100.0%** Exposure
- `addons/mail/static/src/discuss/call/common/thread_actions.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `addons/account/controllers/download_docs.py` -> **100.0%** Exposure
- `addons/account/controllers/portal.py` -> **100.0%** Exposure
- `addons/account/models/account_account.py` -> **100.0%** Exposure
- `addons/account/models/account_account_tag.py` -> **100.0%** Exposure
- `addons/account/models/account_analytic_line.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `addons/html_editor/static/tests/paste.test.js` -> **0** Orphaned Functions | **192** Duplicates
- `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` -> **24** Orphaned Functions | **106** Duplicates
- `addons/web/static/lib/ace/ace.js` -> **106** Orphaned Functions | **23** Duplicates
- `addons/html_editor/static/tests/format/remove_format.test.js` -> **0** Orphaned Functions | **123** Duplicates
- `addons/html_editor/static/tests/list/delete_backward.test.js` -> **0** Orphaned Functions | **109** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `addons/payment_flutterwave/tests/common.py` -> **100.0%** Exposure
- `addons/website_crm/tests/test_crm_lead_merge.py` -> **100.0%** Exposure
- `addons/payment/views/express_checkout_templates.xml` -> **100.0%** Exposure
- `addons/website_slides/data/website_data.xml` -> **100.0%** Exposure
- `addons/web/static/tests/core/file_model.test.js` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `514` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `41308` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `addons/web/static/lib/ace/ace.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.729)
- **Top Global Matches:** file_cluster_4: 12.729, file_cluster_12: 13.187, file_cluster_7: 14.874
- **Magnitude:** 21112.56 | **LOC:** 21443 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **111**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%)
- **Documentation Coverage:** 94.3951% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TextInput` **(Many-Argument Workhorses)** (Impact: 431.0)
  * `Folding` **(Compute Cores)** (Impact: 267.4)
  * `addTouchListeners` **(Compute Cores)** (Impact: 157.2)
  * `escapeHTML` **(Defensive Guards)** (Impact: 147.9)
  * `BracketMatch` **(Defensive Guards)** (Impact: 143.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 51 instances
* *Amplified Cascading Flux:* 2664 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 322
* *State Mutation (weighted view):* 10325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3972`, `structural_boundaries: 4690`, `args: 2048`, `func_start: 1655`
* *Risk/State:* `safety_bypasses: 781`, `high_risk_execution: 5`, `state_mutation: 4997`, `planned_debt: 20`, `fragile_debt: 1`, `duplicate_logic: 23`, `unreferenced_by_name: 106`
* *Architecture:* `io: 1`, `api: 263`, `concurrency: 67`, `import: 250`
* *Defense:* `safety: 642`, `doc: 74`, `test: 1`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ace-internal, lang, oop, range, token_iterator, ace-internal, behaviour, clipboard...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/mail/static/lib/lame/lame.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.058)
- **Top Global Matches:** file_cluster_6: 12.058, file_cluster_4: 16.12, file_cluster_8: 16.87
- **Magnitude:** 19925.76 | **LOC:** 15525 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 61.7241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lamejs` **(I/O & Config Routines)** (Impact: 2768.8)
    * *Intent:* /** * lamejs, a Javascript mp3 encoder library * V.1.2.1 * https://github.com/zhuker/lamejs/blob/mas...
  * `PsyModel` **(I/O & Config Routines)** (Impact: 594.0)
    * *Intent:* */ //package mp3; //import java.util.Arrays;
  * `Lame` **(I/O & Config Routines)** (Impact: 413.4)
  * `Quantize` **(I/O & Config Routines)** (Impact: 345.6)
    * *Intent:* * * You should have received a copy of the GNU Lesser General Public * License along with this libra...
  * `L3psycho_anal_ns` **(Many-Argument Workhorses)** (Impact: 290.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2494 instances
* *State Mutation (weighted view):* 8973
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1992`, `structural_boundaries: 1756`, `args: 284`, `func_start: 284`
* *Risk/State:* `safety_bypasses: 507`, `state_mutation: 3985`, `dead_code: 59`, `planned_debt: 6`, `fragile_debt: 8`, `unreferenced_by_name: 15`
* *Architecture:* None
* *Defense:* `doc: 357`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/Chart/Chart.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 9.926)
- **Top Global Matches:** file_cluster_15: 9.926, file_cluster_4: 11.305, file_cluster_16: 11.346
- **Magnitude:** 13235.54 | **LOC:** 14947 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.066; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (73.3%), Guard Balance (formerly Safety Score) (63.2%), Debt Markers (formerly Tech Debt) (17.9%)
- **Documentation Coverage:** 88.785% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawPointLegend` **(Many-Argument Workhorses)** (Impact: 99.5)
    * *Intent:* // eslint-disable-next-line complexity
  * `_computeLabelItems` **(Defensive Guards)** (Impact: 93.1)
  * `updateElements` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `generateTicks$1` **(I/O & Config Routines)** (Impact: 45.0)
  * `_computeGridLineItems` **(Defensive Guards)** (Impact: 42.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1588 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 5398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2862`, `structural_boundaries: 1965`, `args: 1366`, `func_start: 1215`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 2222`, `planned_debt: 3`, `duplicate_logic: 20`, `unreferenced_by_name: 42`
* *Architecture:* `api: 1`, `concurrency: 5`
* *Defense:* `safety: 740`, `doc: 106`, `test: 1`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 8.5e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `addons/mail/static/lib/odoo_sfu/odoo_sfu.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.632)
- **Top Global Matches:** file_cluster_4: 8.632, file_cluster_12: 9.923, file_cluster_15: 10.649
- **Magnitude:** 8768.1 | **LOC:** 13833 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.039; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Credential Material (formerly Secrets Risk) (83.2%), Debt Markers (formerly Tech Debt) (80.9%)
- **Documentation Coverage:** 66.5301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 91.6)
  * `requireMs` **(Compute Cores)** (Impact: 79.2)
  * `parse` **(Compute Cores)** (Impact: 79.2)
    * *Intent:* /** * Parse the given `str` and return milliseconds. * */
  * `getExtendedRtpCapabilities` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* /** * Generate extended RTP capabilities for sending and receiving. * * Resulting codecs keep order ...
  * `setup` **(Defensive Guards)** (Impact: 62.3)
    * *Intent:* /** * This is the common logic for both the Node.js and web browser * implementations of `debug()`. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 145 instances
* *Amplified Cascading Flux:* 796 instances
* *Concurrency (weighted view):* 1254
* *State Mutation (weighted view):* 2923
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1943`, `structural_boundaries: 1654`, `args: 920`, `func_start: 688`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 1331`, `dead_code: 10`, `planned_debt: 10`, `fragile_debt: 9`, `duplicate_logic: 106`, `unreferenced_by_name: 24`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 529`
* *Defense:* `safety: 917`, `doc: 275`, `immutability_locks: 1`, `cleanup: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000336
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `odoo/orm/models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.978)
- **Top Global Matches:** file_cluster_6: 7.978, file_cluster_4: 11.317, file_cluster_8: 16.557
- **Magnitude:** 7785.22 | **LOC:** 7128 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **83** in-repo importer(s); it depends on **46**; blast radius 9.099; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.5%)
- **Documentation Coverage:** 35.1759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_export_rows` **(Many-Argument Workhorses)** (Impact: 178.1)
    * *Intent:* """ Export fields of the records in ``self``. :param list fields: list of lists of fields to travers...
  * `read_group` **(Many-Argument Workhorses)** (Impact: 153.9)
    * *Intent:* """Deprecated - Get the list of records in list view grouped by the given ``groupby`` fields. :param...
  * `_read_grouping_sets` **(Many-Argument Workhorses)** (Impact: 152.6)
  * `_update_field_translations` **(Many-Argument Workhorses)** (Impact: 123.1)
  * `_read_group_fill_temporal` **(Many-Argument Workhorses)** (Impact: 118.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1086 instances
* *State Mutation (weighted view):* 3379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1618`, `structural_boundaries: 854`, `args: 273`, `func_start: 240`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1207`, `planned_debt: 21`
* *Architecture:* `io: 15`, `api: 148`, `import: 49`
* *Defense:* `safety: 149`, `doc: 209`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.099
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.077284
  * `Imports (Out-Degree: 27):` .commands, .decorators, .domains, .environments, .fields, .fields_misc, .fields_properties, .fields_relational...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `addons/web/static/tests/views/list/list_view.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.787)
- **Top Global Matches:** file_cluster_12: 7.787, file_cluster_10: 8.937, file_cluster_15: 9.762
- **Magnitude:** 7367.62 | **LOC:** 19560 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.024; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (46.3%), Guard Balance (formerly Safety Score) (45.1%)
- **Documentation Coverage:** 99.0196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clickFieldDropdownItem` **(Defensive Guards)** (Impact: 10.8)
  * `selectMany2xItem` **(Compute Cores)** (Impact: 5.6)
  * `getItem` **(Compute Cores)** (Impact: 4.7)
  * `clickControlPanelAction` **(Compute Cores)** (Impact: 4.6)
  * `toggleMultiCurrencyPopover` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 537 instances
* *Amplified Cascading Flux:* 146 instances
* *Concurrency (weighted view):* 5955
* *State Mutation (weighted view):* 868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 3678`, `args: 878`, `func_start: 102`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 280`, `high_risk_execution: 2`, `state_mutation: 576`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 13`, `duplicate_logic: 38`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 4`, `concurrency: 3270`, `import: 19`
* *Defense:* `safety: 36`, `doc: 1`, `test: 3303`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hoot, owl, view_test_helpers, datetime_test_helpers, web_test_helpers, currency, domain, localization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/luxon/luxon.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 11.338)
- **Top Global Matches:** file_cluster_12: 11.338, file_cluster_4: 12.076, file_cluster_15: 13.588
- **Magnitude:** 7254.78 | **LOC:** 8607 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (52.3%)
- **Documentation Coverage:** 43.9716% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DateTime` **(Many-Argument Workhorses)** (Impact: 504.5)
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
* *Structure:* `branch: 1419`, `structural_boundaries: 1525`, `args: 625`, `func_start: 937`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 895`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 31`
* *Architecture:* `api: 16`
* *Defense:* `safety: 408`, `doc: 354`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account/models/account_move.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.694)
- **Top Global Matches:** file_cluster_4: 6.694, file_cluster_16: 10.361, file_cluster_12: 10.861
- **Magnitude:** 7115.96 | **LOC:** 7257 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.8%)
- **Documentation Coverage:** 73.9209% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 1238`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 172`, `import: 23`
* *Defense:* `safety: 24`, `doc: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000152
  * `Imports (Out-Degree: 20):` ast, calendar, collections, contextlib, datetime, dateutil.relativedelta, hashlib, json...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `addons/web/static/tests/views/fields/one2many_field.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.658)
- **Top Global Matches:** file_cluster_12: 7.658, file_cluster_10: 7.924, file_cluster_15: 9.531
- **Magnitude:** 5699.5 | **LOC:** 13723 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.024; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (76.7%), Guard Balance (formerly Safety Score) (49.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `turtles` **(State Mutators)** (Impact: 7.7)
  * `turtles` **(I/O & Config Routines)** (Impact: 7.4)
  * `product_id` **(Defensive Guards)** (Impact: 6.0)
  * `partnerOnchange` **(I/O & Config Routines)** (Impact: 5.7)
  * `validationHandler` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 523 instances
* *Amplified Cascading Flux:* 143 instances
* *Concurrency (weighted view):* 4281
* *State Mutation (weighted view):* 952
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 2028`, `args: 621`, `func_start: 123`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 175`, `state_mutation: 666`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 50`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `concurrency: 1666`, `import: 12`
* *Defense:* `safety: 36`, `test: 1521`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hoot, hoot-dom, hoot-mock, owl, datetime_test_helpers, web_test_helpers, browser, registry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/web/static/lib/owl/owl.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.629)
- **Top Global Matches:** file_cluster_4: 7.629, file_cluster_15: 9.039, file_cluster_12: 9.522
- **Magnitude:** 5635.76 | **LOC:** 6341 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); blast radius 1.478; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.5%)
- **Documentation Coverage:** 85.9619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileTDomNode` **(Many-Argument Workhorses)** (Impact: 116.6)
  * `parseDOMNode` **(Many-Argument Workhorses)** (Impact: 80.2)
  * `parseComponent` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `buildTree` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `compileComponent` **(Many-Argument Workhorses)** (Impact: 62.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 640 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 139
* *State Mutation (weighted view):* 2171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1314`, `structural_boundaries: 959`, `args: 476`, `func_start: 398`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 891`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 15`
* *Architecture:* `io: 1`, `api: 41`, `concurrency: 34`
* *Defense:* `safety: 346`, `doc: 52`, `test: 7`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004553
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `addons/web/static/lib/qunit/qunit-2.9.1.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.015)
- **Top Global Matches:** file_cluster_4: 9.015, file_cluster_12: 12.08, file_cluster_15: 12.751
- **Magnitude:** 5573.56 | **LOC:** 6613 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.039; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.1%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 86.9822% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diff` **(I/O & Config Routines)** (Impact: 239.1)
    * *Intent:* * https://www.apache.org/licenses/LICENSE-2.0 * * Unless required by applicable law or agreed to in ...
  * `Assert` **(I/O & Config Routines)** (Impact: 83.9)
  * `diffBisect` **(Many-Argument Workhorses)** (Impact: 82.0)
    * *Intent:* /** * Find the 'middle snake' of a diff, split the problem in two * and return the recursively const...
  * `diffCleanupMerge` **(Defensive Guards)** (Impact: 51.0)
    * *Intent:* /** * Reorder and merge like edit sections. Merge equalities. * Any edit section can move as long as...
  * `rejects` **(Many-Argument Workhorses)** (Impact: 48.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 58 instances
* *Amplified Cascading Flux:* 779 instances
* *High Risk Execution (weighted view):* 19
* *Concurrency (weighted view):* 435
* *State Mutation (weighted view):* 2571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1011`, `structural_boundaries: 746`, `args: 431`, `func_start: 361`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 25`, `state_mutation: 1013`, `dead_code: 4`, `planned_debt: 52`, `fragile_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 7`
* *Architecture:* `io: 5`, `api: 4`, `concurrency: 145`, `import: 1`
* *Defense:* `safety: 448`, `doc: 45`, `test: 39`, `sync_locks: 15`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000316
  * `Imports (Out-Degree: 1):` vertx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/mail/models/mail_thread.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.49)
- **Top Global Matches:** file_cluster_6: 5.49, file_cluster_4: 11.99, file_cluster_8: 13.071
- **Magnitude:** 5269.88 | **LOC:** 5097 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **28**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (51.5%)
- **Documentation Coverage:** 40.113% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 800`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 35`, `import: 30`
* *Defense:* `safety: 52`, `doc: 109`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.7e-05
  * `Imports (Out-Degree: 17):` ast, base64, collections, collections.abc, datetime, dateutil, email, email.message...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/spreadsheet/static/lib/chartjs-chart-geo/chartjs-chart-geo.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.504)
- **Top Global Matches:** file_cluster_12: 8.504, file_cluster_4: 9.485, file_cluster_15: 9.811
- **Magnitude:** 5077.94 | **LOC:** 5323 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.024; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%)
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
* *Amplified Cascading Flux:* 554 instances
* *State Mutation (weighted view):* 2017
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 879`, `structural_boundaries: 935`, `args: 604`, `func_start: 528`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 909`, `planned_debt: 8`, `duplicate_logic: 24`, `unreferenced_by_name: 10`
* *Architecture:* `api: 27`, `import: 2`
* *Defense:* `safety: 167`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chart.js, helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account_peppol/tools/private_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/iot_box_image/overwrite_after_init/etc/ssl/private/nginx-cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_facturae/demo/certificate_demo.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_sii/demo/certificates/aeat_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/Bizkaia-IZDesa2025.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/araba_1234.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_tbai/demo/certificates/gipuzkoa_Iz3np32024.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_verifactu/demo/certificates/Certificado_PF_99999910G_CERTIFICADO_FISICA_PRUEBAS_5_Pre.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_es_edi_verifactu/demo/certificates/Certificado_RPJ_A39200019_CERTIFICADO_ENTIDAD_PRUEBAS_5_Pre.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/l10n_it_edi/data/pkey.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `addons/account/models/account_tax.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.864)
- **Top Global Matches:** file_cluster_6: 5.864, file_cluster_4: 8.722, file_cluster_12: 16.535
- **Magnitude:** 4883.86 | **LOC:** 5075 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.0%)
- **Documentation Coverage:** 60.0962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_reduce_base_lines_to_target_amount` **(Many-Argument Workhorses)** (Impact: 140.3)
  * `_get_tax_totals_summary` **(Many-Argument Workhorses)** (Impact: 131.6)
    * *Intent:* # ------------------------------------------------------------------------- # TAX TOTALS SUMMARY # -...
  * `_get_tax_details` **(Many-Argument Workhorses)** (Impact: 126.0)
  * `_add_and_round_raw_gross_total_excluded_and_discount` **(Many-Argument Workhorses)** (Impact: 85.1)
  * `_add_accounting_data_to_base_line_tax_details` **(Many-Argument Workhorses)** (Impact: 73.8)
    * *Intent:* """ Add all informations about repartition lines to base_line['tax_details']['taxes_data']. Consider...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 706 instances
* *State Mutation (weighted view):* 2327
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 864`, `structural_boundaries: 341`, `args: 180`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 915`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 71`, `import: 14`
* *Defense:* `safety: 8`, `doc: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.7e-05
  * `Imports (Out-Degree: 14):` ast, collections, collections.abc, copy, markupsafe, math, odoo, odoo.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `addons/web/static/tests/views/form/form_view.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.083)
- **Top Global Matches:** file_cluster_12: 8.083, file_cluster_10: 8.275, file_cluster_11: 9.419
- **Magnitude:** 4793.38 | **LOC:** 13391 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.024; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.2%), Mutation Surface (formerly State Flux) (41.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `int_field` **(Defensive Guards)** (Impact: 6.8)
  * `doAction` **(Defensive Guards)** (Impact: 5.5)
  * `doActionButton` **(Defensive Guards)** (Impact: 4.7)
  * `setItem` **(Parameter Forwarders)** (Impact: 3.8)
  * `setItem` **(Parameter Forwarders)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 382 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 3644
* *State Mutation (weighted view):* 635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 2340`, `args: 796`, `func_start: 165`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 137`, `state_mutation: 493`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 71`, `unreferenced_by_name: 7`
* *Architecture:* `io: 3`, `concurrency: 1734`, `import: 23`
* *Defense:* `safety: 25`, `test: 1654`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.024
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hoot, hoot-dom, hoot-mock, owl, web_test_helpers, browser, rpc, registry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `addons/l10n_ro_edi_stock/models/etransport_api.py` (PYTHON) | Magnitude: 80.48 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 23, core_var_decl: 22, design_snake_case: 20
- `addons/project/models/project_tags.py` (PYTHON) | Magnitude: 94.34 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 27, core_var_decl: 23, design_snake_case: 23
- `addons/purchase/report/purchase_report.py` (PYTHON) | Magnitude: 59.7 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 62, core_var_decl: 36, design_snake_case: 36, state_mutation: 31
- `odoo/modules/db.py` (PYTHON) | Magnitude: 112.94 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 32, state_mutation: 26, core_var_decl: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `addons/website/static/src/interactions/popup/popup.js` (JAVASCRIPT) | Magnitude: 104.62 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 167, branch: 31, structural_boundaries: 27, args: 20
- `addons/html_builder/static/src/core/anchor/anchor_plugin.js` (JAVASCRIPT) | Magnitude: 64.48 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 27, core_var_decl: 19, args: 14
- `addons/website/static/tests/builder/website_builder/image_snippet_option.test.js` (JAVASCRIPT) | Magnitude: 42.78 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 41, concurrency: 32, test: 28
- `addons/mrp/tests/test_byproduct.py` (PYTHON) | Magnitude: 200.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 452, state_mutation: 120, core_var_decl: 60, design_snake_case: 60
- `addons/web/static/src/core/l10n/localization_service.js` (JAVASCRIPT) | Magnitude: 67.72 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 23, core_var_decl: 18, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `addons/web/static/src/views/calendar/calendar_filter_section/calendar_filter_section.js` (JAVASCRIPT) | Magnitude: 69.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 34, args: 22, func_start: 17
- `addons/spreadsheet/static/tests/helpers/data.js` (JAVASCRIPT) | Magnitude: 197.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 519, core_var_decl: 94, design_snake_case: 80, structural_boundaries: 75
- `addons/mail/static/src/discuss/typing/common/typing.scss` (CSS) | Magnitude: 0.11 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, class_start: 10, closures: 5, thread_sleeps: 2
- `addons/spreadsheet/static/src/actions/spreadsheet_component.js` (JAVASCRIPT) | Magnitude: 3.52 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, decorators: 3, import: 3
- `addons/web/static/lib/hoot/ui/hoot_style.css` (CSS) | Magnitude: 2.49 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 600, class_start: 476, ui_framework: 62, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `addons/spreadsheet/static/tests/pivots/model/pivot_custom_groups_model.test.js` (JAVASCRIPT) | Magnitude: 120.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 365, structural_boundaries: 48, concurrency: 46, test: 37
- `addons/web/static/tests/views/fields/percent_pie_field.test.js` (JAVASCRIPT) | Magnitude: 45.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 24, test: 18, core_var_decl: 14
- `addons/web/static/tests/core/expression_editor/expression_editor_dialog.test.js` (JAVASCRIPT) | Magnitude: 38.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 22, concurrency: 11, args: 10
- `addons/point_of_sale/models/pos_config.py` (PYTHON) | Magnitude: 1288.56 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1029, core_var_decl: 304, state_mutation: 299, design_snake_case: 299
- `addons/mail/static/tests/mail_utils.test.js` (JAVASCRIPT) | Magnitude: 87.28 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 66, concurrency: 54, core_var_decl: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `addons/stock_dropshipping/tests/test_lifo_price.py` (PYTHON) | Magnitude: 43.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 34, structural_boundaries: 16, core_var_decl: 10
- `addons/web/static/src/core/emoji_picker/frequent_emoji_service.js` (JAVASCRIPT) | Magnitude: 35.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 9, branch: 7, args: 6
- `addons/payment_mollie/tests/test_mollie.py` (PYTHON) | Magnitude: 11.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, import: 6, core_var_decl: 6
- `addons/html_editor/static/src/others/embedded_components/core/file/readonly_file.js` (JAVASCRIPT) | Magnitude: 29.36 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 16, decorators: 9, import: 9
- `addons/hr_holidays/tests/test_holidays_mail.py` (PYTHON) | Magnitude: 13.8 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 20, import: 8, state_mutation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `addons/point_of_sale/tests/test_performances.py` (PYTHON) | Magnitude: 18.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, import: 5, core_var_decl: 5
- `addons/website/static/src/snippets/s_announcement_scroll/announcement_scroll.edit.js` (JAVASCRIPT) | Magnitude: 8.54 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 8, args: 3, func_start: 3
- `addons/account_edi/tests/test_import_vendor_bill.py` (PYTHON) | Magnitude: 7.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, api: 3, args: 2
- `addons/l10n_ke_edi_tremol/tests/test_account_move_send.py` (PYTHON) | Magnitude: 19.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 16, state_mutation: 6, core_var_decl: 6
- `addons/website_crm_livechat/models/crm_lead.py` (PYTHON) | Magnitude: 14.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, state_mutation: 6, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `addons/l10n_dk/models/account_journal.py` (PYTHON) | Magnitude: 21.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, state_mutation: 4, branch: 3
- `addons/event_product/models/product_product.py` (PYTHON) | Magnitude: 13.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, core_var_decl: 5, design_snake_case: 5
- `addons/link_tracker/models/link_tracker.py` (PYTHON) | Magnitude: 419.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 254, state_mutation: 94, core_var_decl: 82, branch: 80
- `addons/sale_loyalty_delivery/tests/test_loyalty_delivery.py` (PYTHON) | Magnitude: 76.96 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 26, core_var_decl: 22, design_snake_case: 22
- `addons/website_hr_recruitment/models/hr_recruitment_source.py` (PYTHON) | Magnitude: 12.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, branch: 3, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `addons/google_calendar/models/__init__.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8, time_date_logic: 1
- `addons/microsoft_calendar/models/__init__.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8, time_date_logic: 1
- `addons/account/models/__init__.py` (PYTHON) | Magnitude: 16.06 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 106, import: 53
- `addons/point_of_sale/models/__init__.py` (PYTHON) | Magnitude: 16.02 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 102, import: 51
- `addons/mail/models/__init__.py` (PYTHON) | Magnitude: 16.22 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 122, import: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `addons/web/static/lib/hoot/tests/index.html` (HTML) | Magnitude: 27.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, test_skip: 20, decorators: 8, core_var_decl: 8
- `addons/account/tests/test_account_merge_wizard.py` (PYTHON) | Magnitude: 73.28 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 234, state_mutation: 23, core_var_decl: 17, design_snake_case: 17
- `addons/pos_self_order/static/src/app/pages/stand_number_page/stand_number_page.scss` (CSS) | Magnitude: 0.77 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, closures: 2, class_start: 1, immutability_locks: 1
- `addons/mass_mailing/static/src/builder/plugins/move_plugin.js` (JAVASCRIPT) | Magnitude: 17.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 4, core_var_decl: 3, design_snake_case: 3
- `addons/website/tests/test_import_files.py` (PYTHON) | Magnitude: 26.46 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 10, state_mutation: 7, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `odoo/orm/fields_properties.py` (PYTHON) | Magnitude: 1296.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 608, branch: 285, state_mutation: 196, structural_boundaries: 171
- `odoo/addons/test_lint/tests/test_override_signatures.py` (PYTHON) | Magnitude: 239.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 137, core_var_decl: 56, branch: 53, state_mutation: 47
- `odoo/orm/fields_temporal.py` (PYTHON) | Magnitude: 260.96 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 100, branch: 48, state_mutation: 41
- `addons/website_slides/controllers/main.py` (PYTHON) | Magnitude: 1727.8 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1134, core_var_decl: 311, design_snake_case: 307, branch: 299
- `addons/html_editor/models/diff_utils.py` (PYTHON) | Magnitude: 309.58 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 75, core_var_decl: 73, branch: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `addons/html_builder/static/src/core/building_blocks/builder_number_input.js` (JAVASCRIPT) | Magnitude: 123.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 154, branch: 44, structural_boundaries: 33, ui_framework: 21
- `odoo/cli/i18n.py` (PYTHON) | Magnitude: 225.14 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 182, core_var_decl: 61, design_snake_case: 58, structural_boundaries: 50
- `addons/website/models/ir_module_module.py` (PYTHON) | Magnitude: 729.18 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 430, branch: 141, state_mutation: 132, core_var_decl: 119
- `addons/pos_loyalty/static/src/app/services/pos_store.js` (JAVASCRIPT) | Magnitude: 688.58 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 737, branch: 186, structural_boundaries: 164, core_var_decl: 103
- `addons/mail/static/src/views/web/fields/html_mail_field/convert_inline.js` (JAVASCRIPT) | Magnitude: 916.98 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1655, core_var_decl: 308, branch: 250, structural_boundaries: 235

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `addons/website_livechat/static/tests/thread_patch.test.js` (JAVASCRIPT) | Magnitude: 24.72 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, concurrency: 9, import: 4
- `addons/spreadsheet_account/models/res_company.py` (PYTHON) | Magnitude: 26.18 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, core_var_decl: 7, design_snake_case: 7
- `addons/pos_discount/static/tests/unit/models/pos_order_line.test.js` (JAVASCRIPT) | Magnitude: 51.72 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, concurrency: 10, core_var_decl: 9
- `addons/pos_glory_cash/static/tests/glory_xml.test.js` (JAVASCRIPT) | Magnitude: 20.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, test: 31, structural_boundaries: 16, args: 12
- `addons/pos_restaurant/static/src/app/components/popup/edit_order_name_popup/edit_order_name_popup.js` (JAVASCRIPT) | Magnitude: 9.84 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 13, args: 6, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `addons/point_of_sale/static/tests/unit/data/get_model_definitions.js` (JAVASCRIPT) | Magnitude: 23.9 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, core_var_decl: 12, design_camel_case: 7
- `addons/website_sale_collect/utils.py` (PYTHON) | Magnitude: 32.66 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 25, core_var_decl: 11, design_snake_case: 10, state_mutation: 8
- `addons/l10n_ar/models/account_move_line.py` (PYTHON) | Magnitude: 64.74 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 19, state_mutation: 18, design_snake_case: 18
- `addons/website_event_track/static/src/interactions/event_track_reminder.js` (JAVASCRIPT) | Magnitude: 125.04 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 141, branch: 29, state_mutation: 24, structural_boundaries: 19
- `addons/website/static/src/js/http_cookie.js` (JAVASCRIPT) | Magnitude: 20.68 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 9, branch: 6, safety: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `addons/account_edi_ubl_cii/models/account_edi_common.py` -> Churn: **100.0%** | Cog Load: 63.3323% | Debt: 8.0458%
- `addons/stock_account/models/product.py` -> Churn: **97.19%** | Cog Load: 65.9341% | Debt: 9.5385%
- `addons/point_of_sale/models/pos_order.py` -> Churn: **91.76%** | Cog Load: 68.1293% | Debt: 9.8475%
- `addons/mrp/models/mrp_production.py` -> Churn: **78.79%** | Cog Load: 71.6994% | Debt: 9.012%
- `addons/stock/models/stock_move.py` -> Churn: **76.05%** | Cog Load: 69.2968% | Debt: 8.8236%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `addons/web/static/tests/views/fields/one2many_field.test.js` -> **Aaron Bohy** (100.0% isolated ownership) | Magnitude: 5699.5
- `addons/web/static/tests/views/form/form_view.test.js` -> **Corentin Heinix (cohe)** (100.0% isolated ownership) | Magnitude: 4793.38
- `odoo/addons/base/models/ir_ui_view.py` -> **sagu-odoo** (100.0% isolated ownership) | Magnitude: 4202.82
- `odoo/addons/base/models/ir_qweb.py` -> **Pierre Paridans** (100.0% isolated ownership) | Magnitude: 3254.9
- `addons/web/static/tests/_framework/mock_server/mock_model.js` -> **Florian Charlier** (100.0% isolated ownership) | Magnitude: 2946.62

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `odoo/http.py` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 100.0%)
- `odoo/orm/registry.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)
- `odoo/orm/domains.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)
- `odoo/service/server.py` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `odoo/tools/date_utils.py` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `odoo/tools/misc.py` -> **Severity: 6.762** (Embedded: 0.0887 * Error Risk: 76.2702%)
- `odoo/orm/models.py` -> **Severity: 6.429** (Embedded: 0.0773 * Error Risk: 83.191%)
- `odoo/tools/mail.py` -> **Severity: 6.007** (Embedded: 0.0739 * Error Risk: 81.3002%)
- `odoo/tools/convert.py` -> **Severity: 5.924** (Embedded: 0.0675 * Error Risk: 87.7539%)
- `odoo/orm/fields_relational.py` -> **Severity: 5.823** (Embedded: 0.0736 * Error Risk: 79.0998%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `odoo/exceptions.py` -> **Severity: 1184.0** (Blast Radius: 23.68 * Doc Risk: 50.0%)
- `odoo/tests/common.py` -> **Severity: 1179.27** (Blast Radius: 16.617 * Doc Risk: 70.9677%)
- `odoo/tools/misc.py` -> **Severity: 1154.569** (Blast Radius: 17.743 * Doc Risk: 65.0718%)
- `odoo/tests/form.py` -> **Severity: 620.894** (Blast Radius: 9.276 * Doc Risk: 66.9355%)
- `odoo/http.py` -> **Severity: 582.129** (Blast Radius: 8.991 * Doc Risk: 64.7458%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 646 literal sites + 14 sites through wrappers = 660
- **`panics_and_aborts`:** 6303 literal sites + 35 sites through wrappers = 6338

- `abstract` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `addons/web/static/lib/Chart/Chart.js`
- `log_and_raise_error` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `addons/l10n_ro_edi/controllers/main.py`
- `throwDeltaError` (function, debug_prints, primitive): 6 call sites in 1 files -- `addons/web/static/lib/ace/ace.js`
- `throwDeltaError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `addons/web/static/lib/ace/ace.js`
- `dragEffectDelay` (function, debug_prints, primitive): 4 call sites in 1 files -- `addons/pos_restaurant/static/tests/tours/utils/floor_screen_util.js`
- `warnOnBrokenImplementation` (function, debug_prints, primitive): 3 call sites in 1 files -- `addons/auth_passkey/static/lib/simplewebauthn.js`
- `assertSomething` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `odoo/addons/base/tests/test_test_suite.py`
- `binary_to_image` (function, panics_and_aborts, primitive): 2 call sites in 2 files -- `odoo/tools/image.py`
- `func` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `odoo/addons/base/tests/test_test_suite.py`
- `get_action_triples_` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `addons/web/controllers/json.py`
- `throwNotImplemented` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `addons/web/static/lib/hoot/mock/navigator.js`
- `fail` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `addons/stock/static/tests/tours/tour_helper.js`
*(+5 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 313482 call pairs -- scoped 24.0%, unique 0.0%, ambiguous 38.5%, external 37.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 213522 | 25.4% | 0.0% | 34.3% | 40.3% |
| javascript | 99799 | 21.2% | 0.0% | 47.5% | 31.3% |
| shell | 158 | 10.8% | 3.2% | 0.0% | 86.1% |
| postgresql | 3 | 66.7% | 0.0% | 0.0% | 33.3% |

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
