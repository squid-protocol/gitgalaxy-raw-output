# ARCHITECTURAL_BRIEF: django
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/django/django.git` |
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
- **Scope:** 3511 analyzed artifact(s), 397164 LOC.
- **Load-bearing artifact:** `django/test/__init__.py` -- 783 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/admin_views/tests.py` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/admin_views/tests.py` at magnitude 3755.26 (structural weight, not risk).
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
| Total Artifacts | 7028 |
| Analyzed Artifacts (Scanned) | 3511 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3517 |
| Total LOC | 397164 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 50.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4602 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1767 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7152 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 64 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 2877 | 380583 | 81.9% |
| HTML | 361 | 4770 | 10.3% |
| JSON | 56 | 1931 | 1.6% |
| PLAINTEXT | 51 | 177 | 1.5% |
| XML | 49 | 0 | 1.4% |
| JAVASCRIPT | 47 | 4828 | 1.3% |
| CSS | 39 | 3635 | 1.1% |
| YAML | 19 | 1137 | 0.5% |
| MARKDOWN | 7 | 0 | 0.2% |
| SHELL | 3 | 95 | 0.1% |
| M4 | 1 | 4 | 0.0% |
| CSV | 1 | 4 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3510 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 42%, Parameter Forwarders Files 30%, Declarative / Non-Code 11%, Large Core Modules (3) 6%, Large Core Modules (2) 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3453 | 98.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 56 | 1.6% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3517*

**Composition by Extension & Reason:**
- `.po`: 1273x Excluded (Unsupported Extension: '.po')
- `.mo`: 1262x Excluded (Unsupported Extension: '.mo')
- `.txt`: 662x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.js`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 45x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Unsupported Format (.undeterminable), 1x Excluded (Binary Format Detected)
- `.py`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 381 LOC), 1x Excluded (Machine-Generated Source Code Signature: 256 LOC)
- `.py-tpl`: 14x Excluded (Unsupported Extension: '.py-tpl')
- `.html`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 20 exceeds 500 chars), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.css`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dbf`: 9x Excluded (Unsupported Extension: '.dbf')
- `.shp`: 8x Excluded (Unsupported Extension: '.shp')
- `.shx`: 8x Excluded (Unsupported Extension: '.shx')
- `.gz`: 7x Excluded (Explicitly Denied Extension: '.gz')
- `.egg`: 7x Excluded (Unsupported Extension: '.egg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.7 | 37.2 | 51.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.5 | 6.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4731 | 696 | 2 | `tests/queries/tests.py` |
| cleanup | 233 | 87 | 0 | `tests/file_storage/tests.py` |
| guards | 7808 | 795 | 5 | `django/db/models/query.py` |
| danger | 6310 | 1012 | 5 | `django/db/models/query.py` |
| concurrency | 3153 | 286 | 0 | `tests/sessions_tests/tests.py` |
| connectivity | 44157 | 2351 | 33 | `tests/admin_views/tests.py` |
| io | 3110 | 383 | 1 | `tests/utils_tests/files/strip_tags1.html` |
| crypto | 19 | 16 | 0 | `tests/auth_tests/test_hashers.py` |
| ipc | 121 | 36 | 0 | `tests/test_runner/tests.py` |
| time | 1366 | 161 | 0 | `tests/timezones/tests.py` |
| serialization | 91 | 31 | 0 | `tests/queryset_pickle/tests.py` |
| regex | 177 | 86 | 0 | `tests/admin_views/tests.py` |
| events | 1098 | 152 | 0 | `django/utils/feedgenerator.py` |
| tests | 20994 | 872 | 14 | `tests/admin_views/tests.py` |
| docs | 8578 | 1112 | 6 | `tests/admin_views/tests.py` |
| debt | 1515 | 330 | 0 | `tests/admin_scripts/tests.py` |
| mutation | 162691 | 2334 | 110 | `tests/admin_views/tests.py` |
| dead_code | 8698 | 706 | 6 | `tests/migrations/test_autodetector.py` |
| credential | 38 | 19 | 0 | `tests/utils_tests/files/strip_tags1.html` |
| threat | 66 | 32 | 0 | `tests/i18n/tests.py` |
| ml_ai | 67 | 12 | 0 | `django/views/templates/default_urlconf.html` |
| ui | 1098 | 195 | 0 | `tests/utils_tests/files/strip_tags1.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/utils_tests/files/strip_tags1.html` (Hits: 348)
- `tests/admin_scripts/tests.py` (Hits: 175)
- `tests/i18n/test_extraction.py` (Hits: 106)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`django/test/__init__.py`) — 783 inbound connections
2. **__init__.py** (`django/db/__init__.py`) — 769 inbound connections
3. **testcases.py** (`django/test/testcases.py`) — 529 inbound connections
4. **utils.py** (`django/test/utils.py`) — 361 inbound connections
5. **exceptions.py** (`django/core/exceptions.py`) — 348 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tests.py** (`tests/admin_views/tests.py`) — 44 outbound dependencies
2. **testcases.py** (`django/test/testcases.py`) — 41 outbound dependencies
3. **options.py** (`django/contrib/admin/options.py`) — 40 outbound dependencies
4. **tests.py** (`tests/cache/tests.py`) — 37 outbound dependencies
5. **tests.py** (`tests/mail/tests.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_alter_field` **(Many-Argument Workhorses)** (@ `django/db/backends/base/schema.py`) -> Impact: **328.4** | LOC: 370
- `__new__` **(Many-Argument Workhorses)** (@ `django/db/models/base.py`) -> Impact: **220.4** | LOC: 293
- `create_forward_many_to_many_manager` **(Many-Argument Workhorses)** (@ `django/db/models/fields/related_descriptors.py`) -> Impact: **180.0** | LOC: 640
  * *Intent:* """ Create a manager for the either side of a many-to-many relation. This manager subclasses another manager, generally the default manager of the rel...
- `handle` **(Many-Argument Workhorses)** (@ `django/core/management/commands/migrate.py`) -> Impact: **162.6** | LOC: 292
- `fields_for_model` **(Many-Argument Workhorses)** (@ `django/forms/models.py`) -> Impact: **153.7** | LOC: 117
- `_save_table` **(Many-Argument Workhorses)** (@ `django/db/models/base.py`) -> Impact: **151.0** | LOC: 136
- `get_related_selections` **(Many-Argument Workhorses)** (@ `django/db/models/sql/compiler.py`) -> Impact: **140.6** | LOC: 232
- `templatize` **(Many-Argument Workhorses)** (@ `django/utils/translation/template.py`) -> Impact: **136.8** | LOC: 208
  * *Intent:* """ Turn a Django template into something that is understood by xgettext. It does so by translating the Django translation tags into standard gettext ...
- `reduce` **(Many-Argument Workhorses)** (@ `django/db/migrations/operations/models.py`) -> Impact: **133.4** | LOC: 229
- `_ogrinspect` **(Many-Argument Workhorses)** (@ `django/contrib/gis/utils/ogrinspect.py`) -> Impact: **131.7** | LOC: 140

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `django/db/models` | 17 | 13007.18 | 56.84% | 10.53% |
| `django/db/models/fields` | 12 | 8304.42 | 64.46% | 10.38% |
| `tests/auth_tests` | 30 | 7185.72 | 17.36% | 0.0% |
| `django/utils` | 42 | 7108.28 | 41.17% | 6.66% |
| `django/db/models/sql` | 7 | 6461.64 | 40.5% | 12.86% |
| `tests/admin_views` | 21 | 6399.1 | 12.46% | 0.0% |
| `django/forms` | 9 | 6054.52 | 37.85% | 19.79% |
| `django/test` | 8 | 5583.42 | 26.87% | 0.0% |
| `django/template` | 15 | 5021.12 | 43.78% | 4.41% |
| `django/core/management/commands` | 26 | 4661.48 | 49.28% | 29.49% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `django/utils/translation/trans_null.py` -> **100.0%** Exposure
- `django/core/cache/backends/dummy.py` -> **99.9999%** Exposure
- `.github/workflows/schedule_tests.yml` -> **99.9993%** Exposure
- `.github/workflows/selenium.yml` -> **99.9967%** Exposure
- `django/template/loaders/cached.py` -> **99.9905%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `django/contrib/admin/static/admin/js/SelectBox.js` -> **100.0%** Exposure
- `django/contrib/admin/static/admin/js/calendar.js` -> **100.0%** Exposure
- `django/contrib/admin/static/admin/js/core.js` -> **100.0%** Exposure
- `django/contrib/admin/static/admin/js/nav_sidebar.js` -> **100.0%** Exposure
- `django/views/templates/i18n_catalog.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/migrations/test_autodetector.py` -> **176** Orphaned Functions | **0** Duplicates
- `tests/migrations/test_operations.py` -> **174** Orphaned Functions | **2** Duplicates
- `tests/migrations/test_commands.py` -> **159** Orphaned Functions | **2** Duplicates
- `tests/forms_tests/tests/test_forms.py` -> **154** Orphaned Functions | **4** Duplicates
- `tests/postgres_tests/test_array.py` -> **137** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/auth_tests/fixtures/regular.json` -> **99.9925%** Exposure
- `tests/auth_tests/fixtures/natural.json` -> **99.9898%** Exposure
- `tests/decorators/test_csrf.py` -> **88.8563%** Exposure
- `tests/view_tests/tests/test_debug.py` -> **61.591%** Exposure
- `tests/auth_tests/test_auth_backends.py` -> **23.4429%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `10225` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/admin_views/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.454)
- **Top Global Matches:** file_cluster_15: 8.454, file_cluster_16: 9.987, file_cluster_11: 10.208
- **Magnitude:** 3755.26 | **LOC:** 9674 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **44**; blast radius 0.119; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (95.5%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (17.4%)
- **Documentation Coverage:** 66.3708% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_prepopulated_fields` **(Compute Cores)** (Impact: 31.1)
    * *Intent:* """ The JavaScript-automated prepopulated fields work with the main form and with stacked and tabula...
  * `test_relation_spanning_filters` **(Callbacks & Closures)** (Impact: 18.5)
  * `test_updating_related_objects_updates_fk_selects_except_autocompletes` **(I/O & Config Routines)** (Impact: 9.8)
  * `test_related_field` **(Compute Cores)** (Impact: 9.4)
  * `test_change_view` **(I/O & Config Routines)** (Impact: 9.2)
    * *Intent:* """Change view should restrict access and allow users to edit items."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 1718
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 1004`, `args: 530`, `func_start: 509`, `class_start: 51`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1522`, `fragile_debt: 2`, `duplicate_logic: 52`
* *Architecture:* `io: 6`, `api: 557`, `import: 89`
* *Defense:* `safety: 4`, `doc: 193`, `test: 445`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.119
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.00064
  * `Imports (Out-Degree: 39):` .admin, .customadmin, .models, datetime, django, django.contrib, django.contrib.admin, django.contrib.admin.helpers...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `django/db/models/sql/query.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.195)
- **Top Global Matches:** file_cluster_4: 6.195, file_cluster_12: 9.872, file_cluster_15: 11.292
- **Magnitude:** 3171.88 | **LOC:** 2882 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **26**; blast radius 0.954; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.4%), Connectivity (formerly Api Exposure) (76.2%)
- **Documentation Coverage:** 46.2882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_filter` **(Many-Argument Workhorses)** (Impact: 120.8)
  * `get_aggregation` **(Many-Argument Workhorses)** (Impact: 103.7)
    * *Intent:* """ Return the dictionary with the values of the existing aggregations. """
  * `names_to_path` **(Many-Argument Workhorses)** (Impact: 79.2)
    * *Intent:* """ Walk the list of names and turns them into PathInfo tuples. A single name in 'names' can generat...
  * `setup_joins` **(Many-Argument Workhorses)** (Impact: 56.1)
  * `combine` **(Many-Argument Workhorses)** (Impact: 55.8)
    * *Intent:* """ Merge the 'rhs' query into the current one (with any 'rhs' effects being applied *after* (that i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 444 instances
* *State Mutation (weighted view):* 1455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 315`, `args: 115`, `func_start: 115`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 567`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 104`, `import: 26`
* *Defense:* `safety: 70`, `doc: 64`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.954
  * `Choke Point (Betweenness):` 0.000276 | `Ripple Effect (Closeness):` 0.105336
  * `Imports (Out-Degree: 18):` collections, collections.abc, copy, difflib, django.core.exceptions, django.db, django.db.models.aggregates, django.db.models.constants...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `django/db/models/query.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.868)
- **Top Global Matches:** file_cluster_4: 5.868, file_cluster_12: 9.382, file_cluster_16: 10.511
- **Magnitude:** 3113.94 | **LOC:** 3025 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **165** in-repo importer(s); it depends on **25**; blast radius 3.149; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Concurrency Surface (formerly Concurrency) (68.6%)
- **Documentation Coverage:** 54.8589% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bulk_create` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `in_bulk` **(Many-Argument Workhorses)** (Impact: 60.8)
    * *Intent:* """ Return a dictionary mapping each of the given IDs to the object with that ID. If `id_list` isn't...
  * `bulk_update` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* """ Update the given fields in each of the given objects in the database. """
  * `prefetch_related_objects` **(Many-Argument Workhorses)** (Impact: 56.2)
    * *Intent:* """ Populate prefetched object caches for an iterable of model instances based on the lookups/Prefet...
  * `_check_bulk_create_options` **(Many-Argument Workhorses)** (Impact: 51.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 411 instances
* *Concurrency (weighted view):* 74
* *State Mutation (weighted view):* 1350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 494`, `args: 172`, `func_start: 172`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 528`, `duplicate_logic: 12`
* *Architecture:* `api: 127`, `concurrency: 49`, `import: 25`
* *Defense:* `safety: 82`, `doc: 85`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.149
  * `Choke Point (Betweenness):` 0.0013 | `Ripple Effect (Closeness):` 0.121389
  * `Imports (Out-Degree: 26):` asgiref.sync, contextlib, copy, django, django.conf, django.core, django.db, django.db.models...
  * `Imported By (In-Degree: 165):` (Excluded from Brief to save tokens)

### `django/db/models/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.689)
- **Top Global Matches:** file_cluster_6: 7.689, file_cluster_4: 8.447, file_cluster_12: 15.178
- **Magnitude:** 2810.48 | **LOC:** 2567 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **111** in-repo importer(s); it depends on **30**; blast radius 2.014; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 76.4045% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Many-Argument Workhorses)** (Impact: 220.4)
  * `_save_table` **(Many-Argument Workhorses)** (Impact: 151.0)
  * `refresh_from_db` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* """ Reload field values from the database. By default, the reloading happens from the database this ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 69.7)
    * *Intent:* # Alias some things as locals to avoid repeat global lookups cls = self.__class__ opts = self._meta ...
  * `_get_unique_checks` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* """ Return a list of checks to perform. Since validate_unique() could be called from a ModelForm, so...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 396 instances
* *State Mutation (weighted view):* 1229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 328`, `args: 83`, `func_start: 83`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 437`, `planned_debt: 1`
* *Architecture:* `api: 41`, `concurrency: 6`, `import: 31`
* *Defense:* `safety: 81`, `doc: 29`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.014
  * `Choke Point (Betweenness):` 0.001638 | `Ripple Effect (Closeness):` 0.124018
  * `Imports (Out-Degree: 30):` asgiref.sync, collections, copy, django, django.apps, django.conf, django.core, django.core.exceptions...
  * `Imported By (In-Degree: 111):` (Excluded from Brief to save tokens)

### `django/db/models/sql/compiler.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.17)
- **Top Global Matches:** file_cluster_6: 9.17, file_cluster_8: 10.182, file_cluster_4: 16.838
- **Magnitude:** 2539.04 | **LOC:** 2276 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 0.271; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 58.6777% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_related_selections` **(Many-Argument Workhorses)** (Impact: 140.6)
  * `as_sql` **(Many-Argument Workhorses)** (Impact: 121.3)
    * *Intent:* """ Create the SQL for this query. Return the SQL string and list of parameters. If 'with_limits' is...
  * `_order_by_pairs` **(Compute Cores)** (Impact: 72.2)
  * `as_sql` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* # We don't need quote_name_unless_alias() here, since these are all # going to be column names (so w...
  * `get_group_by` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* """ Return a list of 2-tuples of form (sql, params). The logic of what exactly the GROUP BY clause c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 404 instances
* *Api Near Db Sink:* 5 instances
* *State Mutation (weighted view):* 1277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 495`, `structural_boundaries: 214`, `args: 62`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 469`, `fragile_debt: 1`
* *Architecture:* `api: 55`, `import: 20`
* *Defense:* `safety: 67`, `doc: 29`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.271
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.001468
  * `Imports (Out-Degree: 17):` collections, django.core.exceptions, django.db, django.db.models.constants, django.db.models.expressions, django.db.models.fields, django.db.models.functions, django.db.models.lookups...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `django/db/models/fields/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.745)
- **Top Global Matches:** file_cluster_12: 6.745, file_cluster_15: 7.418, file_cluster_16: 7.981
- **Magnitude:** 2433.72 | **LOC:** 2964 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **87** in-repo importer(s); it depends on **29**; blast radius 3.14; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (90.8%), Debt Markers (formerly Tech Debt) (86.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 82.8633% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deconstruct` **(Compute Cores)** (Impact: 43.2)
    * *Intent:* """ Return enough information to recreate the field as a 4-tuple: * The name of the field on the mod...
  * `_check_choices` **(Defensive Guards)** (Impact: 36.2)
  * `formfield` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* """Return a django.forms.Field instance for this field."""
  * `validate` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* """ Validate value and raise ValidationError if necessary. Subclasses should override this to provid...
  * `get_choices` **(Many-Argument Workhorses)** (Impact: 25.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 255 instances
* *State Mutation (weighted view):* 887
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 721`, `args: 246`, `func_start: 244`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 377`, `planned_debt: 3`, `duplicate_logic: 26`
* *Architecture:* `api: 227`, `import: 34`
* *Defense:* `safety: 99`, `doc: 42`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.14
  * `Choke Point (Betweenness):` 0.001057 | `Ripple Effect (Closeness):` 0.120982
  * `Imports (Out-Degree: 23):` base64, collections.abc, copy, datetime, decimal, django, django.apps, django.conf...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `tests/forms_tests/tests/test_forms.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.904)
- **Top Global Matches:** file_cluster_15: 5.904, file_cluster_12: 7.503, file_cluster_11: 7.83
- **Magnitude:** 2382.4 | **LOC:** 5681 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%), Complexity Load (formerly Cognitive Load) (16.4%), Connectivity (formerly Api Exposure) (13.5%)
- **Documentation Coverage:** 91.3706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_validating_multiple_fields` **(Compute Cores)** (Impact: 33.8)
    * *Intent:* # There are a couple of ways to do multiple-field validation. If you # want the validation message t...
  * `test_use_required_attribute_true` **(Compute Cores)** (Impact: 27.2)
  * `test_use_required_attribute_false` **(Compute Cores)** (Impact: 27.0)
  * `test_templates_with_forms` **(Compute Cores)** (Impact: 26.9)
  * `test_unicode_values` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* # Unicode values are handled properly. p = Person( { "first_name": "John", "last_name": "\u0160\u011...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 958
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 882`, `args: 210`, `func_start: 205`, `class_start: 187`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 762`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 154`
* *Architecture:* `api: 376`, `import: 17`
* *Defense:* `safety: 15`, `doc: 136`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` .jinja2_tests, copy, datetime, django.core.exceptions, django.core.files.uploadedfile, django.core.validators, django.forms, django.forms.renderers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `django/db/backends/base/schema.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.473)
- **Top Global Matches:** file_cluster_4: 5.473, file_cluster_6: 10.775, file_cluster_16: 11.092
- **Magnitude:** 2179.98 | **LOC:** 2087 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **14**; blast radius 0.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.5%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 56.0976% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_alter_field` **(Many-Argument Workhorses)** (Impact: 328.4)
  * `alter_field` **(Many-Argument Workhorses)** (Impact: 85.4)
    * *Intent:* """ Allow a field's type, uniqueness, nullability, default, column, constraints, etc. to be modified...
  * `_constraint_names` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `_iter_column_sql` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* # Field <-> database mapping functions
  * `_field_should_be_altered` **(Many-Argument Workhorses)** (Impact: 49.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *Api Near Db Sink:* 5 instances
* *State Mutation (weighted view):* 707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 238`, `args: 86`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 279`, `planned_debt: 3`
* *Architecture:* `api: 35`, `import: 14`
* *Defense:* `safety: 13`, `doc: 38`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.326
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.002789
  * `Imports (Out-Degree: 15):` datetime, django.conf, django.core.exceptions, django.db.backends.ddl_references, django.db.backends.utils, django.db.models, django.db.models.expressions, django.db.models.fields.composite...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `tests/queries/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.519)
- **Top Global Matches:** file_cluster_15: 6.519, file_cluster_11: 8.052, file_cluster_12: 8.376
- **Magnitude:** 2127.42 | **LOC:** 4678 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (57.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.0%), Complexity Load (formerly Cognitive Load) (24.0%)
- **Documentation Coverage:** 91.0015% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tickets_5324_6704` **(I/O & Config Routines)** (Impact: 10.6)
  * `test_ordering` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* # Cross model ordering is possible in Meta, too. self.assertSequenceEqual( Ranking.objects.all(), [s...
  * `test_ticket7256` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* # An empty values() call includes all aliases, including those from an # extra() sql = "case when %s...
  * `test_in_list_limit` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* # The "in" lookup works with lists of 1000 items or more. # The numbers amount is picked to force th...
  * `test_ticket8439` **(I/O & Config Routines)** (Impact: 7.5)
    * *Intent:* # Complex combinations of conjunctions, disjunctions and nullable # relations. self.assertSequenceEq...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 879
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 539`, `args: 350`, `func_start: 344`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 781`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 410`, `import: 16`
* *Defense:* `safety: 6`, `doc: 38`, `test: 376`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .models, datetime, django.core.exceptions, django.db, django.db.models, django.db.models.expressions, django.db.models.functions, django.db.models.sql.constants...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `django/db/models/expressions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.048)
- **Top Global Matches:** file_cluster_12: 6.048, file_cluster_15: 7.816, file_cluster_16: 8.81
- **Magnitude:** 2078.02 | **LOC:** 2233 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **128** in-repo importer(s); it depends on **19**; blast radius 3.836; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%)
- **Documentation Coverage:** 95.6019% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as_sql` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `__init__` **(Defensive Guards)** (Impact: 39.2)
  * `as_sql` **(Many-Argument Workhorses)** (Impact: 39.1)
  * `__init__` **(Defensive Guards)** (Impact: 23.2)
  * `__init__` **(Defensive Guards)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 599`, `args: 245`, `func_start: 242`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 323`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 25`
* *Architecture:* `api: 209`, `import: 20`
* *Defense:* `safety: 75`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.836
  * `Choke Point (Betweenness):` 0.000419 | `Ripple Effect (Closeness):` 0.115879
  * `Imports (Out-Degree: 15):` collections, copy, datetime, decimal, django.core.exceptions, django.db, django.db.models, django.db.models.constants...
  * `Imported By (In-Degree: 128):` (Excluded from Brief to save tokens)

### `tests/model_forms/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.207)
- **Top Global Matches:** file_cluster_15: 6.207, file_cluster_12: 7.338, file_cluster_11: 8.093
- **Magnitude:** 1828.64 | **LOC:** 3780 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (62.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.3%), Complexity Load (formerly Cognitive Load) (24.4%)
- **Documentation Coverage:** 75.9104% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_image_field` **(I/O & Config Routines)** (Impact: 9.7)
    * *Intent:* # ImageField and FileField are nearly identical, but they differ # slightly when it comes to validat...
  * `test_prefetch_related_queryset` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* """ ModelChoiceField should respect a prefetch_related() on its queryset. """
  * `test_inherited_unique_for_date` **(I/O & Config Routines)** (Impact: 7.7)
  * `test_unique_for_date` **(I/O & Config Routines)** (Impact: 7.6)
  * `test_foreignkeys_which_use_to_field` **(Type Conversions)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 822
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 602`, `args: 180`, `func_start: 178`, `class_start: 261`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 710`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 436`, `import: 18`
* *Defense:* `safety: 5`, `doc: 67`, `test: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` .models, datetime, decimal, django, django.core.exceptions, django.core.files.uploadedfile, django.db, django.db.models.query...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `django/forms/models.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.464)
- **Top Global Matches:** file_cluster_4: 6.464, file_cluster_12: 8.537, file_cluster_15: 9.982
- **Magnitude:** 1740.32 | **LOC:** 1717 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **15**; blast radius 0.475; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Connectivity (formerly Api Exposure) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 78.7879% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fields_for_model` **(Many-Argument Workhorses)** (Impact: 153.7)
  * `modelform_factory` **(Many-Argument Workhorses)** (Impact: 56.3)
  * `_get_foreign_key` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* """ Find and return the ForeignKey from model to parent if there is one (return None if can_fail is ...
  * `validate_unique` **(Compute Cores)** (Impact: 44.5)
    * *Intent:* # Collect unique_checks and date_checks to run from all the forms. all_unique_checks = set() all_dat...
  * `add_fields` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* """Add a hidden field for the object's primary key."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 217 instances
* *State Mutation (weighted view):* 695
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 235`, `args: 77`, `func_start: 77`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 261`, `fragile_debt: 2`
* *Architecture:* `api: 67`, `import: 19`
* *Defense:* `safety: 49`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.475
  * `Choke Point (Betweenness):` 0.000342 | `Ripple Effect (Closeness):` 0.022527
  * `Imports (Out-Degree: 19):` django.core.exceptions, django.core.validators, django.db, django.db.models, django.db.models.utils, django.forms.fields, django.forms.forms, django.forms.formsets...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `django/db/models/fields/related.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.865)
- **Top Global Matches:** file_cluster_4: 6.865, file_cluster_12: 7.816, file_cluster_15: 7.92
- **Magnitude:** 1730.46 | **LOC:** 2164 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **23**; blast radius 0.919; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.1%)
- **Documentation Coverage:** 80.3419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_relationship_model` **(Many-Argument Workhorses)** (Impact: 104.7)
  * `_check_on_delete` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `_check_clashes` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* """Check accessor and reverse query name clashes."""
  * `_check_unique_target` **(Compute Cores)** (Impact: 30.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 690
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 338`, `args: 114`, `func_start: 112`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 286`, `dead_code: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 90`, `import: 26`
* *Defense:* `safety: 54`, `doc: 24`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.919
  * `Choke Point (Betweenness):` 0.000778 | `Ripple Effect (Closeness):` 0.113313
  * `Imports (Out-Degree: 25):` .Field, .mixins, .related_descriptors, .related_lookups, .reverse_related, django, django.apps, django.conf...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `django/db/models/fields/related_descriptors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.438)
- **Top Global Matches:** file_cluster_12: 7.438, file_cluster_15: 7.94, file_cluster_4: 8.131
- **Magnitude:** 1609.62 | **LOC:** 1713 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.14; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.5%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 79.3814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_forward_many_to_many_manager` **(Many-Argument Workhorses)** (Impact: 180.0)
    * *Intent:* """ Create a manager for the either side of a many-to-many relation. This manager subclasses another...
  * `create_reverse_many_to_one_manager` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* """ Create a manager for the reverse side of a many-to-one relation. This manager subclasses another...
  * `__set__` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* """ Set the related instance through the forward relation. With the example above, when setting ``ch...
  * `_add_items` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `__get__` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* """ Get the related instance through the forward relation. With the example above, when getting ``ch...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 238`, `args: 97`, `func_start: 95`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 246`
* *Architecture:* `api: 66`, `concurrency: 28`, `import: 13`
* *Defense:* `safety: 21`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.14
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.094632
  * `Imports (Out-Degree: 16):` asgiref.sync, django.core.exceptions, django.db, django.db.models, django.db.models.expressions, django.db.models.fields.tuple_lookups, django.db.models.functions, django.db.models.lookups...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/mail/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.569)
- **Top Global Matches:** file_cluster_15: 6.569, file_cluster_12: 6.802, file_cluster_11: 8.443
- **Magnitude:** 1514.7 | **LOC:** 3257 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (60.2%), Complexity Load (formerly Cognitive Load) (18.2%), Concurrency Surface (formerly Concurrency) (14.2%)
- **Documentation Coverage:** 60.6436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_apply_cpython_128110_workaround` **(Defensive Guards)** (Impact: 21.4)
    * *Intent:* """ Updates message in place to correct misparsed rfc2047 display-names in address headers caused by...
  * `assertStartsWith` **(Defensive Guards)** (Impact: 12.8)
  * `assertEndsWith` **(Defensive Guards)** (Impact: 12.8)
  * `test_address_header_injection` **(Compute Cores)** (Impact: 12.0)
  * `test_attach_file` **(I/O & Config Routines)** (Impact: 11.1)
    * *Intent:* """ Test attaching a file against different mimetypes and make sure that a file will be attached and...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 83 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 470`, `args: 205`, `func_start: 204`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 1`, `state_mutation: 472`, `fragile_debt: 4`
* *Architecture:* `io: 33`, `api: 219`, `concurrency: 1`, `import: 42`
* *Defense:* `safety: 16`, `doc: 95`, `test: 166`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000285
  * `Imports (Out-Degree: 14):` aiosmtpd.controller, ast, datetime, django.core, django.core.exceptions, django.core.mail, django.core.mail.backends, django.core.mail.message...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `django/test/client.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.264)
- **Top Global Matches:** file_cluster_15: 6.264, file_cluster_16: 6.583, file_cluster_12: 6.803
- **Magnitude:** 1509.92 | **LOC:** 1753 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **112** in-repo importer(s); it depends on **28**; blast radius 5.773; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (74.0%), Guard Balance (formerly Safety Score) (68.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%)
- **Documentation Coverage:** 74.6269% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generic` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `_follow_redirect` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `generic` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `encode_multipart` **(Defensive Guards)** (Impact: 29.0)
    * *Intent:* """ Encode multipart POST data from a dictionary of form values. The key will be used as the form da...
  * `get` **(Many-Argument Workhorses)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 152 instances
* *Concurrency (weighted view):* 229
* *State Mutation (weighted view):* 580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 249`, `args: 78`, `func_start: 76`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 276`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 63`, `concurrency: 49`, `import: 34`
* *Defense:* `safety: 19`, `doc: 54`, `test: 5`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.773
  * `Choke Point (Betweenness):` 0.001933 | `Ripple Effect (Closeness):` 0.125624
  * `Imports (Out-Degree: 22):` asgiref.sync, collections.abc, copy, django.conf, django.contrib.auth, django.core.handlers.asgi, django.core.handlers.base, django.core.handlers.wsgi...
  * `Imported By (In-Degree: 112):` (Excluded from Brief to save tokens)

### `tests/cache/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.279)
- **Top Global Matches:** file_cluster_15: 6.279, file_cluster_12: 7.579, file_cluster_11: 7.761
- **Magnitude:** 1494.0 | **LOC:** 3129 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.124; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (84.8%), Concurrency Surface (formerly Concurrency) (60.8%), Guard Balance (formerly Safety Score) (55.6%)
- **Documentation Coverage:** 86.9658% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `caches_setting_for_tests` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* # `base` is used to pull in the memcached config from the original # settings, `exclude` is a set of...
  * `_perform_cull_test` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `test_unicode` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* # Unicode values can be cached stuff = { "ascii": "ascii_value", "unicode_ascii": "Iñtërnâtiônàlizæt...
  * `_perform_invalid_key_test` **(Stateful Encapsulated Methods)** (Impact: 8.5)
    * *Intent:* """ All the builtin backends should warn (except memcached that should error) on keys that would be ...
  * `test_cull_queries` **(Defensive Guards)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 69 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 501`, `args: 248`, `func_start: 237`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 358`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 21`, `api: 257`, `concurrency: 23`, `import: 38`
* *Defense:* `safety: 17`, `doc: 36`, `test: 211`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000285
  * `Imports (Out-Degree: 29):` .models, copy, django, django.conf, django.core, django.core.cache, django.core.cache.backends.base, django.core.cache.backends.redis...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/invalid_models_tests/test_models.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.723)
- **Top Global Matches:** file_cluster_12: 6.723, file_cluster_15: 8.015, file_cluster_7: 9.611
- **Magnitude:** 1441.58 | **LOC:** 3126 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.1%), Connectivity (formerly Api Exposure) (15.3%), Complexity Load (formerly Cognitive Load) (14.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.2%)
- **Documentation Coverage:** 98.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_M2M_long_column_name` **(Compute Cores)** (Impact: 20.8)
    * *Intent:* """ #13711 -- Model check for long M2M column names when database has column name length limits. """
  * `test_check_constraint_raw_sql_check` **(Compute Cores)** (Impact: 12.9)
  * `test_index_with_condition` **(Compute Cores)** (Impact: 7.2)
  * `test_index_with_include` **(Compute Cores)** (Impact: 7.2)
  * `test_unique_constraint_with_condition` **(Compute Cores)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 439
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 597`, `args: 145`, `func_start: 144`, `class_start: 337`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 385`, `unreferenced_by_name: 135`
* *Architecture:* `api: 477`, `import: 8`
* *Defense:* `doc: 2`, `test: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` django.core.checks, django.core.checks.model_checks, django.db, django.db.models.functions, django.db.models.signals, django.test, django.test.utils, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/expressions/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.097)
- **Top Global Matches:** file_cluster_15: 6.097, file_cluster_11: 8.128, file_cluster_10: 8.209
- **Magnitude:** 1436.56 | **LOC:** 3055 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.108; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.6%), Guard Balance (formerly Safety Score) (56.9%), Complexity Load (formerly Cognitive Load) (22.0%)
- **Documentation Coverage:** 97.2477% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_delta_update` **(Compute Cores)** (Impact: 12.1)
  * `test_lookups_subquery` **(Compute Cores)** (Impact: 10.7)
  * `test_expressions_range_lookups_join_choice` **(Defensive Guards)** (Impact: 8.3)
  * `test_delta_add` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* # Intentionally no assert
  * `test_resolve_output_field_dates` **(Compute Cores)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 357`, `args: 229`, `func_start: 220`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 442`, `fragile_debt: 1`
* *Architecture:* `api: 241`, `import: 21`
* *Defense:* `safety: 5`, `doc: 11`, `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` .models, collections, copy, datetime, decimal, django.core.exceptions, django.db, django.db.models...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/admin_scripts/tests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.216)
- **Top Global Matches:** file_cluster_15: 8.216, file_cluster_12: 9.719, file_cluster_16: 9.797
- **Magnitude:** 1422.36 | **LOC:** 3343 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **31**; blast radius 0.144; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.3%), Guard Balance (formerly Safety Score) (53.4%), Complexity Load (formerly Cognitive Load) (8.9%)
- **Documentation Coverage:** 43.7262% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_settings` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `assertOutput` **(Defensive Guards)** (Impact: 11.8)
  * `run_test` **(Many-Argument Workhorses)** (Impact: 9.0)
  * `run_manage` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `test_invalid_choice_db_option` **(Compute Cores)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 435
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 461`, `args: 268`, `func_start: 263`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 367`, `duplicate_logic: 87`
* *Architecture:* `io: 175`, `api: 306`, `import: 31`
* *Defense:* `safety: 11`, `doc: 167`, `test: 248`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001743
  * `Imports (Out-Degree: 22):` .urls, black, django, django.conf, django.core.checks, django.core.checks.registry, django.core.exceptions, django.core.management...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `django/test/testcases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.765)
- **Top Global Matches:** file_cluster_12: 5.765, file_cluster_16: 7.777, file_cluster_15: 7.972
- **Magnitude:** 1368.0 | **LOC:** 1895 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **529** in-repo importer(s); it depends on **41**; blast radius 11.181; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.4%), Connectivity (formerly Api Exposure) (59.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.9%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 66.2162% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertFormSetError` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* """ Similar to assertFormError() but for formsets. Use form_index=None to check the formset's non-fo...
  * `_get_template_used` **(Stateful Encapsulated Methods)** (Impact: 35.2)
  * `assertRedirects` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `_assert_form_error` **(Many-Argument Workhorses)** (Impact: 32.7)
  * `_assert_contains` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* # If the response supports deferred rendering and hasn't been rendered # yet, then ensure that it do...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 123 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 335`, `args: 123`, `func_start: 120`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 195`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 80`, `concurrency: 3`, `import: 44`
* *Defense:* `safety: 52`, `doc: 53`, `test: 18`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.181
  * `Choke Point (Betweenness):` 0.005354 | `Ripple Effect (Closeness):` 0.170252
  * `Imports (Out-Degree: 25):` asgiref.sync, collections, contextlib, copy, difflib, django.apps, django.conf, django.core...
  * `Imported By (In-Degree: 529):` (Excluded from Brief to save tokens)

### `django/forms/fields.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.748)
- **Top Global Matches:** file_cluster_12: 6.748, file_cluster_15: 8.804, file_cluster_4: 9.137
- **Magnitude:** 1348.58 | **LOC:** 1395 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **76** in-repo importer(s); it depends on **23**; blast radius 1.7; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Connectivity (formerly Api Exposure) (93.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.9%)
- **Documentation Coverage:** 71.1656% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `clean` **(Defensive Guards)** (Impact: 39.2)
    * *Intent:* """ Validate every value in the given list. A value is validated against the corresponding Field in ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `has_changed` **(Defensive Guards)** (Impact: 16.8)
  * `to_python` **(Compute Cores)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 151 instances
* *State Mutation (weighted view):* 522
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 302`, `args: 95`, `func_start: 95`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 220`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 100`, `import: 24`
* *Defense:* `safety: 61`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.7
  * `Choke Point (Betweenness):` 0.000564 | `Ripple Effect (Closeness):` 0.108458
  * `Imports (Out-Degree: 12):` PIL, copy, datetime, decimal, django.core, django.core.exceptions, django.forms.boundfield, django.forms.utils...
  * `Imported By (In-Degree: 76):` (Excluded from Brief to save tokens)

### `django/forms/widgets.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.765)
- **Top Global Matches:** file_cluster_12: 5.765, file_cluster_15: 7.002, file_cluster_16: 7.76
- **Magnitude:** 1348.46 | **LOC:** 1280 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **58** in-repo importer(s); it depends on **17**; blast radius 1.383; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.8%), Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%)
- **Documentation Coverage:** 73.057% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.0)
  * `optgroups` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* """Return a list of optgroups for this widget."""
  * `create_option` **(Many-Argument Workhorses)** (Impact: 22.1)
  * `format_value` **(Defensive Guards)** (Impact: 22.0)
    * *Intent:* """ Return a dict containing the year, month, and day of the current value. Use dict instead of a da...
  * `__init__` **(Defensive Guards)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 293`, `args: 106`, `func_start: 106`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 271`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 112`, `import: 17`
* *Defense:* `safety: 34`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.383
  * `Choke Point (Betweenness):` 0.000395 | `Ripple Effect (Closeness):` 0.085353
  * `Imports (Out-Degree: 11):` .renderers, collections, copy, datetime, django.forms.utils, django.templatetags.static, django.utils, django.utils.choices...
  * `Imported By (In-Degree: 58):` (Excluded from Brief to save tokens)

### `django/template/defaulttags.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_12: 6.321, file_cluster_15: 6.98, file_cluster_16: 8.485
- **Magnitude:** 1344.84 | **LOC:** 1688 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **21**; blast radius 0.174; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.6%)
- **Documentation Coverage:** 63.8298% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `querystring` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* """ Build a query string using `args` and `kwargs` arguments. This tag constructs a new query string...
  * `do_for` **(Many-Argument Workhorses)** (Impact: 29.2)
    * *Intent:* """ Loop over each item in an array. For example, to display a list of athletes given ``athlete_list...
  * `cycle` **(Many-Argument Workhorses)** (Impact: 28.7)
    * *Intent:* """ Cycle among the given strings each time this tag is encountered. Within a loop, cycles among the...
  * `render` **(Many-Argument Workhorses)** (Impact: 27.5)
  * `partialdef_func` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* """ Declare a partial that can be used in the template. Usage:: {% partialdef partial_name %} Conten...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 202 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 247`, `args: 83`, `func_start: 82`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 273`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 81`, `import: 23`
* *Defense:* `safety: 32`, `doc: 27`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.001464
  * `Imports (Out-Degree: 15):` .base, .context, .defaultfilters, .library, .smartif, collections, collections.abc, datetime...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/auth_tests/test_auth_backends.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.665)
- **Top Global Matches:** file_cluster_15: 7.665, file_cluster_12: 7.667, file_cluster_13: 9.015
- **Magnitude:** 1304.92 | **LOC:** 1447 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.201; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (79.0%), Guard Balance (formerly Safety Score) (53.6%), Complexity Load (formerly Cognitive Load) (31.9%)
- **Documentation Coverage:** 82.996% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `has_perm` **(Defensive Guards)** (Impact: 18.5)
  * `get_all_permissions` **(Defensive Guards)** (Impact: 12.7)
  * `get_group_permissions` **(Defensive Guards)** (Impact: 12.6)
  * `has_module_perms` **(Compute Cores)** (Impact: 6.1)
  * `test_backend_path_login_without_authenticate_multiple_backends` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 98 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 648
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 383`, `args: 122`, `func_start: 122`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 192`, `duplicate_logic: 7`
* *Architecture:* `io: 7`, `api: 155`, `concurrency: 158`, `import: 21`
* *Defense:* `safety: 18`, `doc: 38`, `test: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.201
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.000285
  * `Imports (Out-Degree: 20):` .models, asgiref.sync, datetime, django.contrib.auth, django.contrib.auth.backends, django.contrib.auth.forms, django.contrib.auth.hashers, django.contrib.auth.models...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/wsgi/urls.py` (PYTHON) | Magnitude: 7.36 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, args: 3, ssr_boundaries: 3
- `django/contrib/admin/static/admin/js/urlify.js` (JAVASCRIPT) | Magnitude: 0.42 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 156, core_var_decl: 25, design_upper_case: 17, state_mutation: 10
- `django/contrib/admin/static/admin/js/theme.js` (JAVASCRIPT) | Magnitude: 0.28 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 40, branch: 15, safety: 7, args: 5
- `django/core/files/utils.py` (PYTHON) | Magnitude: 56.16 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 24, args: 20, core_var_decl: 16
- `tests/db_functions/datetime/test_now.py` (PYTHON) | Magnitude: 19.14 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 18, design_snake_case: 18, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/async/test_async_auth.py` (PYTHON) | Magnitude: 345.3 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 61, concurrency: 49, state_mutation: 32
- `tests/backends/base/test_features.py` (PYTHON) | Magnitude: 3.6 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, api: 2, import: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `eslint-recommended.js` (JAVASCRIPT) | Magnitude: 19.32 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 13, safety: 3, immutability_locks: 2
- `django/contrib/gis/forms/fields.py` (PYTHON) | Magnitude: 0.99 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 31, state_mutation: 21, core_var_decl: 21
- `tests/admin_widgets/test_autocomplete_widget.py` (PYTHON) | Magnitude: 95.06 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 155, core_var_decl: 59, design_snake_case: 58, state_mutation: 46
- `tests/asgi/tests.py` (PYTHON) | Magnitude: 1094.8 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 553, structural_boundaries: 293, core_var_decl: 176, state_mutation: 172
- `django/core/files/storage/handler.py` (PYTHON) | Magnitude: 36.04 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 21, state_mutation: 12, core_var_decl: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/properties/tests.py` (PYTHON) | Magnitude: 11.42 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, api: 4, test: 4
- `django/contrib/admin/templates/admin/change_list_object_tools.html` (HTML) | Magnitude: 0.15 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: ssr_boundaries: 10, indent_spaces: 8, branch: 2, args: 2
- `django/contrib/postgres/expressions.py` (PYTHON) | Magnitude: 0.08 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 6, api: 3, import: 3
- `tests/template_tests/filter_tests/test_cut.py` (PYTHON) | Magnitude: 35.7 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 20, api: 12, args: 10
- `tests/template_tests/templatetags/tag_27584.py` (PYTHON) | Magnitude: 7.9 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/test_new_version.sh` (SHELL) | Magnitude: 1.31 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 16, safety_bypasses: 6, cleanup: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/template_tests/filter_tests/test_phone2numeric.py` (PYTHON) | Magnitude: 16.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 14, api: 6, args: 4
- `tests/template_tests/test_autoreloader.py` (PYTHON) | Magnitude: 64.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 27, api: 26, test: 25
- `tests/auth_tests/test_auth_backends.py` (PYTHON) | Magnitude: 1304.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 979, structural_boundaries: 383, core_var_decl: 263, design_snake_case: 237
- `tests/forms_tests/field_tests/__init__.py` (PYTHON) | Magnitude: 6.32 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, api: 3, class_start: 2
- `django/core/mail/backends/dummy.py` (PYTHON) | Magnitude: 3.88 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 5, api: 2, indent_spaces: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `django/contrib/auth/handlers/modwsgi.py` (PYTHON) | Magnitude: 0.36 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, safety: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `django/contrib/gis/geos/__init__.py` (PYTHON) | Magnitude: 0.15 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 18, import: 9, indent_spaces: 4, doc: 1
- `django/core/checks/__init__.py` (PYTHON) | Magnitude: 17.88 | Delta: **0.237** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, import: 15, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `django/contrib/admin/templates/admin/app_index.html` (HTML) | Magnitude: 0.15 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ssr_boundaries: 18, indent_spaces: 9, structural_boundaries: 4, args: 4
- `django/forms/templates/django/forms/ul.html` (HTML) | Magnitude: 16.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ssr_boundaries: 36, indent_spaces: 18, branch: 16, args: 5
- `tests/admin_views/templates/admin/admin_views/article/submit_line.html` (HTML) | Magnitude: 14.12 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: ssr_boundaries: 8, branch: 2, args: 2, api: 1
- `django/contrib/gis/gdal/__init__.py` (PYTHON) | Magnitude: 0.18 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, import: 9, api: 1
- `django/views/templates/directory_index.html` (HTML) | Magnitude: 17.44 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, ssr_boundaries: 13, structural_boundaries: 7, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `django/contrib/admin/templatetags/admin_list.py` (PYTHON) | Magnitude: 4.98 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 392, core_var_decl: 103, design_snake_case: 103, branch: 98
- `django/contrib/admin/static/admin/js/inlines.js` (JAVASCRIPT) | Magnitude: 2.19 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 269, core_var_decl: 53, branch: 39, args: 33
- `django/template/base.py` (PYTHON) | Magnitude: 1130.8 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 693, state_mutation: 237, structural_boundaries: 206, branch: 184

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `django/contrib/auth/management/commands/createsuperuser.py` (PYTHON) | Magnitude: 2.99 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 261, branch: 70, structural_boundaries: 55, state_mutation: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/many_to_many/models.py` (PYTHON) | Magnitude: 42.5 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 28, core_var_decl: 21, design_snake_case: 21
- `django/db/utils.py` (PYTHON) | Magnitude: 238.72 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 82, branch: 36, state_mutation: 36
- `django/core/serializers/jsonl.py` (PYTHON) | Magnitude: 39.94 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 27, state_mutation: 10, args: 7
- `tests/migrations/models.py` (PYTHON) | Magnitude: 1.44 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 21, api: 15, class_start: 13
- `django/core/exceptions.py` (PYTHON) | Magnitude: 153.94 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 70, api: 34, doc: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/schema/fields.py` (PYTHON) | Magnitude: 3.62 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 78, core_var_decl: 25, design_snake_case: 25, structural_boundaries: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `django/db/backends/base/features.py` -> Churn: **100.0%** | Cog Load: 71.8167% | Debt: 18.0232%
- `.github/workflows/check_commit_messages.yml` -> Churn: **99.89%** | Cog Load: 11.57% | Debt: 95.2325%
- `django/db/models/expressions.py` -> Churn: **94.64%** | Cog Load: 75.7468% | Debt: 97.0053%
- `django/db/models/lookups.py` -> Churn: **73.25%** | Cog Load: 67.5787% | Debt: 30.4712%
- `django/db/models/fields/json.py` -> Churn: **69.77%** | Cog Load: 67.3985% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `django/db/models/fields/related.py` -> **Tim Graham** (100.0% isolated ownership) | Magnitude: 1730.46
- `django/test/client.py` -> **Marc Gibbons** (100.0% isolated ownership) | Magnitude: 1509.92
- `tests/invalid_models_tests/test_models.py` -> **Mridul Dhall** (100.0% isolated ownership) | Magnitude: 1441.58
- `django/forms/fields.py` -> **Natalia** (100.0% isolated ownership) | Magnitude: 1348.58
- `django/forms/widgets.py` -> **Johannes Maron** (100.0% isolated ownership) | Magnitude: 1348.46

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `django/conf/__init__.py` -> **Severity: 0.7** (Bridge: 0.007 * Flux: 100.0%)
- `django/urls/resolvers.py` -> **Severity: 0.665** (Bridge: 0.0066 * Flux: 100.0%)
- `django/urls/base.py` -> **Severity: 0.492** (Bridge: 0.0049 * Flux: 100.0%)
- `django/db/__init__.py` -> **Severity: 0.455** (Bridge: 0.0046 * Flux: 99.8341%)
- `django/core/checks/model_checks.py` -> **Severity: 0.258** (Bridge: 0.0026 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `django/core/exceptions.py` -> **Severity: 21.179** (Embedded: 0.2647 * Error Risk: 80.0%)
- `django/conf/__init__.py` -> **Severity: 17.242** (Embedded: 0.2523 * Error Risk: 68.3508%)
- `django/utils/functional.py` -> **Severity: 17.028** (Embedded: 0.2515 * Error Risk: 67.703%)
- `django/apps/registry.py` -> **Severity: 15.414** (Embedded: 0.2062 * Error Risk: 74.7385%)
- `django/urls/base.py` -> **Severity: 15.309** (Embedded: 0.2024 * Error Risk: 75.6213%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `django/db/__init__.py` -> **Severity: 4531.2** (Blast Radius: 45.312 * Doc Risk: 100.0%)
- `django/utils/functional.py` -> **Severity: 3205.563** (Blast Radius: 42.073 * Doc Risk: 76.1905%)
- `django/core/exceptions.py` -> **Severity: 2665.69** (Blast Radius: 29.793 * Doc Risk: 89.4737%)
- `django/conf/__init__.py` -> **Severity: 1882.524** (Blast Radius: 30.591 * Doc Risk: 61.5385%)
- `django/utils/connection.py` -> **Severity: 1671.8** (Blast Radius: 16.718 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 2571 literal sites + 18 sites through wrappers = 2589

- `_test_error_exc_info` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `tests/test_runner/test_parallel.py`
- `func` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `django/utils/functional.py`
- `check_ogr_fld` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `django/contrib/gis/utils/layermapping.py`
- `reraise` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `django/template/backends/django.py`
- `sensitive_args_function` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tests/view_tests/views.py`
- `sensitive_kwargs_function` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tests/view_tests/views.py`
- `trigger_reload` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `django/utils/autoreload.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 118127 call pairs -- scoped 43.3%, unique 0.0%, ambiguous 18.4%, external 38.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 117435 | 43.5% | 0.0% | 18.5% | 38.0% |
| javascript | 662 | 8.9% | 0.0% | 1.8% | 89.3% |
| shell | 25 | 4.0% | 0.0% | 0.0% | 96.0% |
| html | 5 | 40.0% | 0.0% | 0.0% | 60.0% |

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
