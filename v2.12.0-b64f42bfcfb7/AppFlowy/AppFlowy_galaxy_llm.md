# ARCHITECTURAL_BRIEF: AppFlowy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AppFlowy-IO/AppFlowy` |
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
- **Scope:** 3384 analyzed artifact(s), 329479 LOC.
- **Load-bearing artifact:** `frontend/rust-lib/flowy-error/src/lib.rs` -- 153 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `frontend/rust-lib/flowy-folder/src/manager.rs` -- pulls in 113 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `frontend/rust-lib/flowy-sqlite/.env` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 4597 |
| Analyzed Artifacts (Scanned) | 3384 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1213 |
| Total LOC | 329479 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 73.6% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7135 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0602 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.5549 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 247 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| DART | 1622 | 225946 | 47.9% |
| XML | 787 | 614 | 23.3% |
| RUST | 745 | 89327 | 22.0% |
| SQLITE | 65 | 267 | 1.9% |
| JSON | 42 | 10623 | 1.2% |
| YAML | 30 | 1599 | 0.9% |
| MARKDOWN | 29 | 0 | 0.9% |
| PLAINTEXT | 23 | 1 | 0.7% |
| HTML | 15 | 127 | 0.4% |
| CPP | 13 | 583 | 0.4% |
| GROOVY | 3 | 130 | 0.1% |
| SWIFT | 3 | 106 | 0.1% |
| RUBY | 2 | 122 | 0.1% |
| JAVASCRIPT | 1 | 19 | 0.0% |
| MAKEFILE | 1 | 5 | 0.0% |
| KOTLIN | 1 | 4 | 0.0% |
| OBJECTIVE-C | 1 | 1 | 0.0% |
| CSV | 1 | 5 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3382 |
| unknown | unknown | 1 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Large Core Modules (2) 21%, Large Core Modules (3) 8%, State Mutators Files 8%, Generic / Templated Code Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3306 | 97.7% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 51 | 1.5% |
| Static: Minified & Vendor Opaque Mass | 26 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1213*

**Composition by Extension & Reason:**
- `.dart`: 354x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 201x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.xcworkspacedata'), 3x Excluded (Unsupported Extension: '.entitlements')
- `.toml`: 48x Excluded (Unsupported Extension: '.toml'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 3211 LOC), 2x Excluded (Massive Static Asset Blob: 3468 LOC)
- `.xcconfig`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Excluded (Unsupported Extension: '.xcconfig')
- `.h`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 25x Excluded (Explicitly Denied Extension: '.zip')
- `.yaml`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 261, Signals: 0)
- `.md`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.plist`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 20x Excluded (Explicitly Denied Extension: '.ttf')
- `.txt`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.7 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 20.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.1 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 23.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 886 | 318 | 0 | `frontend/appflowy_flutter/test/unit_test/document/text_robot/markdown_text_robot_test.dart` |
| cleanup | 1456 | 520 | 2 | `frontend/appflowy_flutter/lib/ai/service/view_selector_cubit.dart` |
| guards | 31476 | 1864 | 27 | `frontend/appflowy_flutter/lib/shared/popup_menu/appflowy_popup_menu.dart` |
| danger | 2821 | 672 | 2 | `frontend/rust-lib/event-integration-test/tests/sql_test/chat_message_test.rs` |
| concurrency | 15804 | 1037 | 12 | `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` |
| connectivity | 13440 | 2275 | 9 | `frontend/rust-lib/flowy-ai/src/entities.rs` |
| io | 436 | 142 | 0 | `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 11 | 8 | 0 | `frontend/rust-lib/event-integration-test/src/user_event.rs` |
| time | 343 | 199 | 0 | `frontend/appflowy_flutter/lib/workspace/presentation/widgets/date_picker/widgets/reminder_selector.dart` |
| serialization | 194 | 96 | 0 | `frontend/appflowy_flutter/lib/workspace/application/view/view_ext.dart` |
| regex | 94 | 45 | 0 | `frontend/appflowy_flutter/lib/shared/patterns/common_patterns.dart` |
| events | 2787 | 687 | 2 | `frontend/rust-lib/flowy-database2/src/event_handler.rs` |
| tests | 3783 | 317 | 0 | `frontend/appflowy_flutter/test/widget_test/date_picker_test.dart` |
| docs | 5593 | 523 | 3 | `frontend/appflowy_flutter/lib/shared/popup_menu/appflowy_popup_menu.dart` |
| debt | 1105 | 269 | 0 | `frontend/appflowy_flutter/test/widget_test/date_picker_test.dart` |
| mutation | 33858 | 1948 | 28 | `frontend/rust-lib/flowy-folder/src/manager.rs` |
| dead_code | 2478 | 854 | 2 | `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/i18n/editor_i18n.dart` |
| credential | 8 | 7 | 0 | `frontend/appflowy_flutter/test/unit_test/link_preview/link_preview_test.dart` |
| threat | 290 | 3 | 0 | `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_lists.dart` |
| ml_ai | 165 | 106 | 0 | `frontend/rust-lib/flowy-sqlite-vec/src/db.rs` |
| ui | 6994 | 957 | 7 | `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/simple_table/simple_table_widgets/_simple_table_bottom_sheet_actions.dart` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (Hits: 22)
- `frontend/appflowy_flutter/packages/flowy_svg/bin/flowy_svg.dart` (Hits: 17)
- `frontend/rust-lib/flowy-sqlite/src/schema.rs` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`frontend/rust-lib/flowy-error/src/lib.rs`) — 153 inbound connections
2. **errors.rs** (`frontend/rust-lib/flowy-error/src/errors.rs`) — 141 inbound connections
3. **lib.rs** (`frontend/rust-lib/build-tool/flowy-derive/src/lib.rs`) — 84 inbound connections
4. **field_entities.rs** (`frontend/rust-lib/flowy-database2/src/entities/field_entities.rs`) — 83 inbound connections
5. **mod.rs** (`frontend/rust-lib/flowy-database2/src/entities/mod.rs`) — 74 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **manager.rs** (`frontend/rust-lib/flowy-folder/src/manager.rs`) — 113 outbound dependencies
2. **database_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`) — 94 outbound dependencies
3. **view_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs`) — 87 outbound dependencies
4. **plugins.dart** (`frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/plugins.dart`) — 78 outbound dependencies
5. **cloud_service_impl.rs** (`frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs`) — 77 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `showMobileBottomSheet` **(Many-Argument Workhorses)** (@ `frontend/appflowy_flutter/lib/mobile/presentation/bottom_sheet/show_mobile_bottom_sheet.dart`) -> Impact: **218.5** | LOC: 184
- `main` **(Callbacks & Closures)** (@ `frontend/appflowy_flutter/test/bloc_test/workspace_test/workspace_bloc_test.dart`) -> Impact: **164.2** | LOC: 725
- `afLabel` **(I/O & Config Routines)** (@ `frontend/appflowy_flutter/lib/workspace/presentation/settings/pages/settings_shortcuts_view.dart`) -> Impact: **152.6** | LOC: 192
- `BlockComponentBackgroundColorMixin` **(Stateful Encapsulated Methods)** (@ `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/simple_table/simple_table_cell_block_component.dart`) -> Impact: **113.9** | LOC: 518
- `duplicate_view_with_parent_id` **(Many-Argument Workhorses)** (@ `frontend/rust-lib/flowy-folder/src/manager.rs`) -> Impact: **113.3** | LOC: 173
  * *Intent:* /// Duplicate the view with the given view id and parent view id. /// /// If the view id is the same as the parent view id, it will return an error. /...
- `copyWith` **(Many-Argument Workhorses)** (@ `frontend/appflowy_flutter/lib/features/share_tab/logic/share_tab_state.dart`) -> Impact: **105.8** | LOC: 36
- `copyWith` **(Many-Argument Workhorses)** (@ `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/mobile_toolbar_v3/aa_menu/_toolbar_theme.dart`) -> Impact: **92.1** | LOC: 40
- `copyWith` **(Defensive Guards)** (@ `frontend/appflowy_flutter/lib/workspace/presentation/widgets/date_picker/widgets/date_picker_dialog.dart`) -> Impact: **91.6** | LOC: 30
- `showMenu` **(Many-Argument Workhorses)** (@ `frontend/appflowy_flutter/lib/shared/popup_menu/appflowy_popup_menu.dart`) -> Impact: **82.8** | LOC: 57
  * *Intent:* /// [MaterialLocalizations.popupMenuLabel]. /// /// The `clipBehavior` argument is used to clip the shape of the menu. Defaults to /// [Clip.none]. //...
- `stream_response` **(Many-Argument Workhorses)** (@ `frontend/rust-lib/flowy-ai/src/chat.rs`) -> Impact: **82.2** | LOC: 145

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `frontend/resources/flowy_icons/16x` | 495 | 5093.16 | 0.0% | 0.0% |
| `frontend/rust-lib/flowy-sqlite` | 1 | 5000.0 | 0.0% | 0.0% |
| `frontend/rust-lib/flowy-folder/src` | 11 | 2273.54 | 14.41% | 2.82% |
| `frontend/rust-lib/flowy-database2/src` | 6 | 1922.56 | 19.86% | 2.94% |
| `frontend/rust-lib/flowy-ai/src` | 11 | 1908.92 | 25.46% | 0.0% |
| `frontend/rust-lib/flowy-database2/src/services/database` | 5 | 1881.56 | 23.85% | 1.55% |
| `frontend/appflowy_flutter/lib/plugins/ai_chat/application` | 20 | 1779.98 | 37.21% | 14.93% |
| `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/simple_table/simple_table_widgets` | 19 | 1612.44 | 14.37% | 5.91% |
| `frontend/appflowy_flutter/lib/workspace/presentation/settings/pages` | 8 | 1557.9 | 20.91% | 20.46% |
| `frontend/appflowy_flutter/lib/plugins/document/application` | 15 | 1542.38 | 41.36% | 42.09% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/core/config/kv.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/features/workspace/data/repositories/workspace_repository.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/plugins/blank/blank.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_notification.dart` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `frontend/appflowy_flutter/lib/core/helpers/url_launcher.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/mobile/presentation/setting/appearance/text_scale_setting.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/menu/menu_extension.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/plugins/shared/sync_indicator.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/shared/af_image.dart` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/i18n/editor_i18n.dart` -> **111** Orphaned Functions | **0** Duplicates
- `frontend/appflowy_flutter/test/widget_test/date_picker_test.dart` -> **6** Orphaned Functions | **65** Duplicates
- `frontend/appflowy_flutter/test/bloc_test/grid_test/cell/date_cell_bloc_test.dart` -> **2** Orphaned Functions | **37** Duplicates
- `frontend/appflowy_flutter/test/widget_test/lib/features/share_section/shared_page_actions_button_test.dart` -> **1** Orphaned Functions | **32** Duplicates
- `frontend/appflowy_flutter/test/bloc_test/grid_test/cell/select_option_cell_test.dart` -> **2** Orphaned Functions | **27** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `22109` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `frontend/rust-lib/flowy-sqlite/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.58)
- **Top Global Matches:** file_cluster_0: 7.58, file_cluster_15: 8.386, file_cluster_12: 9.446
- **Magnitude:** 1636.56 | **LOC:** 2465 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **94**; blast radius 0.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.5%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 92.2078% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `async_load_rows` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `open_database_view` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* /// Open database view /// When opening database view, it will load database rows from remote if the...
  * `move_group_row` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `delete_select_options` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `get_prompts_from_database` **(Defensive Guards)** (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 532
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 723`, `args: 218`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `api: 105`, `concurrency: 422`, `import: 50`
* *Defense:* `safety: 79`, `doc: 20`, `test: 2`, `sync_locks: 19`, `immutability_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.578
  * `Choke Point (Betweenness):` 0.000808 | `Ripple Effect (Closeness):` 0.023138
  * `Imports (Out-Degree: 31):` arc_swap::ArcSwapOption, async_trait::async_trait, collab::core::collab_plugin::CollabPluginType, collab::lock::RwLock, collab_database::database::Database, collab_database::entity::DatabaseView, collab_database::fields::Field, collab_database::fields::TypeOptionData...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-folder/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.338)
- **Top Global Matches:** file_cluster_0: 8.338, file_cluster_16: 9.432, file_cluster_15: 9.706
- **Magnitude:** 1447.64 | **LOC:** 2638 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **113**; blast radius 0.553; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.0%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 45.3552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `duplicate_view_with_parent_id` **(Many-Argument Workhorses)** (Impact: 113.3)
    * *Intent:* /// Duplicate the view with the given view id and parent view id. /// /// If the view id is the same...
  * `move_view` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /// Move the view with given id from one position to another position. /// The view will be moved to...
  * `initialize_after_sign_up` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// Initialize the folder for the new user. /// Using the [DefaultFolderBuilder] to create the defau...
  * `publish_view` **(Many-Argument Workhorses)** (Impact: 29.8)
    * *Intent:* /// Publishes a view identified by the given `view_id`. /// /// If `publish_name` is `None`, a defau...
  * `create_view_with_params` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* /// Asynchronously creates a view with provided parameters and notifies the workspace if update is n...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 269
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 639`, `args: 192`, `func_start: 103`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `api: 90`, `concurrency: 219`, `import: 36`
* *Defense:* `safety: 113`, `doc: 144`, `sync_locks: 88`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.553
  * `Choke Point (Betweenness):` 0.000155 | `Ripple Effect (Closeness):` 0.013149
  * `Imports (Out-Degree: 22):` arc_swap::ArcSwapOption, client_api::entity::AFAccessLevel, client_api::entity::AFRole, client_api::entity::PublishInfo, client_api::entity::guest_dto::RevokeSharedViewAccessRequest, client_api::entity::guest_dto::ShareViewWithGuestRequest, client_api::entity::guest_dto::SharedUser, client_api::entity::guest_dto::SharedViewDetails...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-database2/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.085)
- **Top Global Matches:** file_cluster_0: 8.085, file_cluster_16: 9.323, file_cluster_13: 10.521
- **Magnitude:** 999.6 | **LOC:** 1451 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 0.197; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.2%), Complexity Load (formerly Cognitive Load) (48.2%)
- **Documentation Coverage:** 97.2414% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_database_setting_handler` **(Defensive Guards)** (Impact: 42.5)
  * `rename_media_cell_file_handler` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /// We use a custom handler to rename the media file, as the ordering /// of the files must be maint...
  * `update_field_type_option_handler` **(Stateful Encapsulated Methods)** (Impact: 13.1)
  * `update_relation_cell_handler` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `get_primary_field_handler` **(Stateful Encapsulated Methods)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 462`, `args: 82`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 3`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 72`, `concurrency: 223`, `import: 15`
* *Defense:* `safety: 21`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.006929
  * `Imports (Out-Degree: 10):` collab_database::fields::media_type_option::MediaCellData, collab_database::rows::Cell, collab_database::rows::RowCover, collab_database::rows::RowId, crate::entities::*, crate::manager::DatabaseManager, crate::services::field::RelationCellChangeset, crate::services::field::SelectOptionCellChangeset...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.323)
- **Top Global Matches:** file_cluster_0: 7.323, file_cluster_15: 7.944, file_cluster_12: 9.3
- **Magnitude:** 872.98 | **LOC:** 1345 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **87**; blast radius 0.252; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.1%), Connectivity (formerly Api Exposure) (63.2%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `v_did_update_row` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /// Notify the view that the row has been updated. If the view has groups, /// send the group notifi...
  * `v_did_create_row` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `v_set_layout_settings` **(Many-Argument Workhorses)** (Impact: 16.5)
    * *Intent:* /// Update the layout settings and send the notification to refresh the UI
  * `v_get_layout_settings` **(Defensive Guards)** (Impact: 15.9)
    * *Intent:* /// Returns the current calendar settings
  * `v_delete_group` **(Defensive Guards)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 334
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 444`, `args: 84`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`
* *Architecture:* `api: 61`, `concurrency: 249`, `import: 30`
* *Defense:* `safety: 58`, `doc: 26`, `test: 1`, `sync_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.018955
  * `Imports (Out-Degree: 37):` collab_database::database::gen_database_calculation_id, collab_database::database::gen_database_sort_id, collab_database::database::gen_row_id, collab_database::entity::DatabaseView, collab_database::fields::Field, collab_database::rows::Cell, collab_database::rows::Cells, collab_database::rows::CreateRowParams...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_0: 7.67, file_cluster_15: 8.453, file_cluster_16: 9.706
- **Magnitude:** 847.96 | **LOC:** 1227 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **65**; blast radius 0.981; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.4%), Complexity Load (formerly Cognitive Load) (60.9%)
- **Documentation Coverage:** 85.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_collab` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* ///NOTE: this method doesn't initialize plugins, however it is passed into WorkspaceDatabase, /// th...
  * `translate_row` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `summarize_row` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `initialize` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* /// When initialize with new workspace, all the resources will be cleared.
  * `create_linked_view` **(Many-Argument Workhorses)** (Impact: 20.0)
    * *Intent:* /// A linked view is a view that is linked to existing database.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 346`, `args: 101`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `planned_debt: 1`
* *Architecture:* `api: 40`, `concurrency: 133`, `import: 38`
* *Defense:* `safety: 33`, `doc: 9`, `sync_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.981
  * `Choke Point (Betweenness):` 0.001047 | `Ripple Effect (Closeness):` 0.029823
  * `Imports (Out-Degree: 17):` anyhow::anyhow, arc_swap::ArcSwapOption, async_trait::async_trait, collab::core::collab::DataSource, collab::core::origin::CollabOrigin, collab::lock::RwLock, collab::preclude::Collab, collab_database::database::Database...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-user/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.801)
- **Top Global Matches:** file_cluster_0: 5.801, file_cluster_13: 9.836, file_cluster_15: 10.23
- **Magnitude:** 611.94 | **LOC:** 865 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.19; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (85.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_cloud_config_handler` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `import_appflowy_data_folder_handler` **(Generic / Templated Code)** (Impact: 11.7)
  * `get_user_workspace_handler` **(Generic / Templated Code)** (Impact: 11.0)
  * `get_user_profile_handler` **(Generic / Templated Code)** (Impact: 10.1)
  * `get_cloud_config_handler` **(Generic / Templated Code)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 124
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 238`, `args: 60`, `func_start: 57`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 55`, `concurrency: 114`, `import: 17`
* *Defense:* `safety: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.19
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.010134
  * `Imports (Out-Degree: 13):` crate::entities::*, crate::notification::UserNotification, crate::notification::send_notification, crate::services::cloud_config::get_cloud_config, crate::services::cloud_config::get_or_create_cloud_config, crate::services::cloud_config::save_cloud_config, crate::services::data_import::prepare_import, crate::user_manager::UserManager...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/plugins/database/application/field/field_controller.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.069)
- **Top Global Matches:** file_cluster_0: 8.069, file_cluster_10: 9.429, file_cluster_12: 10.031
- **Magnitude:** 584.0 | **LOC:** 774 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Mutation Surface (formerly State Flux) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.2%)
- **Documentation Coverage:** 75.6098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addListener` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `removeListener` **(Defensive Guards)** (Impact: 30.4)
  * `_listenOnFieldChanges` **(Callbacks & Closures)** (Impact: 19.4)
    * *Intent:* /// Listen for field changes in the backend.
  * `_listenOnSortChanged` **(Callbacks & Closures)** (Impact: 17.8)
    * *Intent:* /// Listen for sort changes in the backend.
  * `addSingleFieldListener` **(Defensive Guards)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 69
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 139`, `args: 93`, `func_start: 68`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 63`, `duplicate_logic: 5`
* *Architecture:* `api: 21`, `concurrency: 34`, `import: 21`
* *Defense:* `safety: 49`, `doc: 14`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000946
  * `Imports (Out-Degree: 4):` setting_service.dart, dart:collection, field_info.dart, filter_entities.dart, row_cache.dart, setting_listener.dart, database_view_service.dart, field_listener.dart...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/ai/operations/ai_writer_cubit.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.577)
- **Top Global Matches:** file_cluster_12: 6.577, file_cluster_15: 7.959, file_cluster_16: 8.823
- **Magnitude:** 582.58 | **LOC:** 817 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.512; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.1%), Debt Markers (formerly Tech Debt) (95.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runResponseAction` **(Defensive Guards)** (Impact: 42.2)
  * `runCommand` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `_startInforming` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `_startSuggestingEdits` **(Many-Argument Workhorses)** (Impact: 32.0)
  * `_startContinueWriting` **(Many-Argument Workhorses)** (Impact: 30.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 163
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 107`, `args: 19`, `func_start: 57`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 7`, `state_mutation: 26`, `duplicate_logic: 16`
* *Architecture:* `api: 17`, `concurrency: 98`, `import: 16`
* *Defense:* `safety: 42`, `doc: 3`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.512
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.001511
  * `Imports (Out-Degree: 5):` markdown_text_robot.dart, ai_writer_block_operations.dart, ai_writer_entities.dart, ai_writer_node_extension.dart, dart:async, ai.dart, startup.dart, view_service.dart...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/flutter/af_dropdown_menu.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.866)
- **Top Global Matches:** file_cluster_4: 8.866, file_cluster_5: 10.611, file_cluster_12: 10.689
- **Magnitude:** 573.5 | **LOC:** 1066 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.149; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (64.6%), Guard Balance (formerly Safety Score) (50.2%), Complexity Load (formerly Cognitive Load) (38.9%)
- **Documentation Coverage:** 95.122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Defensive Guards)** (Impact: 63.2)
  * `RenderBoxContainerDefaultsMixin` **(Defensive Guards)** (Impact: 52.1)
  * `_buildButtons` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `didUpdateWidget` **(Generic / Templated Code)** (Impact: 16.2)
  * `computeDryLayout` **(Defensive Guards)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 60`, `args: 39`, `func_start: 43`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 81`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 109`, `doc: 176`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dart:math, material.dart, rendering.dart, services.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.007)
- **Top Global Matches:** file_cluster_0: 7.007, file_cluster_15: 8.363, file_cluster_16: 9.855
- **Magnitude:** 566.6 | **LOC:** 919 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **77**; blast radius 0.158; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.7%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 95.6204% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_plugins` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `upload_part` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `create_upload` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `complete_upload` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `generate_search_summary` **(Generic / Templated Code)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 155`, `args: 71`, `func_start: 69`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 68`, `concurrency: 121`, `import: 37`
* *Defense:* `safety: 19`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.006988
  * `Imports (Out-Degree: 19):` client_api::collab_sync::SinkConfig, client_api::collab_sync::SyncObject, client_api::collab_sync::SyncPlugin, client_api::entity::PublishInfo, client_api::entity::ai_dto::RepeatedRelatedQuestion, client_api::entity::workspace_dto::PublishInfoView, collab::core::origin::CollabClient, collab::core::origin::CollabOrigin...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/actions/block_action_option_cubit.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.627)
- **Top Global Matches:** file_cluster_4: 6.627, file_cluster_6: 11.087, file_cluster_12: 11.456
- **Magnitude:** 541.72 | **LOC:** 691 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (94.2%), Complexity Load (formerly Cognitive Load) (85.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `turnIntoSingleToggleHeading` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* // turn a single node into toggle heading block // 1. find the sibling nodes after the selected node...
  * `turnIntoBlock` **(Many-Argument Workhorses)** (Impact: 52.4)
  * `_extractNameFromNodes` **(Defensive Guards)** (Impact: 26.5)
  * `handleAction` **(Compute Cores)** (Impact: 26.0)
  * `turnIntoPage` **(Many-Argument Workhorses)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 105`, `args: 32`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`, `duplicate_logic: 4`, `unreferenced_by_name: 8`
* *Architecture:* `api: 2`, `concurrency: 50`, `import: 14`
* *Defense:* `safety: 41`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` document_bloc.dart, document_data_pb_extension.dart, editor_notification.dart, clipboard_service.dart, plugins.dart, constants.dart, prelude.dart, startup.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.476)
- **Top Global Matches:** file_cluster_9: 8.476, file_cluster_4: 8.535, file_cluster_15: 9.361
- **Magnitude:** 539.8 | **LOC:** 822 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **48**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.8%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_workspace` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `get_workspace_settings` **(Compute Cores)** (Impact: 26.5)
  * `create_workspace` **(Compute Cores)** (Impact: 21.4)
  * `get_all_user_workspaces` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `upload_collab_data` **(Many-Argument Workhorses)** (Impact: 20.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 207`, `args: 37`, `func_start: 32`
* *Risk/State:* None
* *Architecture:* `api: 26`, `concurrency: 85`, `import: 19`
* *Defense:* `safety: 11`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000394
  * `Imports (Out-Degree: 15):` chrono::Duration, chrono::NaiveDateTime, chrono::Utc, client_api::entity::billing_dto::RecurringInterval, client_api::entity::billing_dto::SubscriptionPlan, client_api::entity::billing_dto::SubscriptionPlanDetail, client_api::entity::billing_dto::WorkspaceUsageAndLimit, crate::entities::RepeatedUserWorkspacePB...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/workspace/presentation/settings/pages/settings_shortcuts_view.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.772)
- **Top Global Matches:** file_cluster_4: 8.772, file_cluster_16: 9.303, file_cluster_10: 9.875
- **Magnitude:** 528.8 | **LOC:** 720 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.3%), Guard Balance (formerly Safety Score) (65.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `afLabel` **(I/O & Config Routines)** (Impact: 152.6)
  * `initState` **(I/O & Config Routines)** (Impact: 16.9)
  * `build` **(Callbacks & Closures)** (Impact: 11.4)
  * `_renderKeybindings` **(Stateful Encapsulated Methods)** (Impact: 8.8)
  * `_toParts` **(Stateful Encapsulated Methods)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 92`, `args: 38`, `func_start: 29`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 92`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 29`
* *Defense:* `safety: 24`, `immutability_locks: 25`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` flowy_svgs.g.dart, locale_keys.g.dart, custom_text_align_command.dart, string_extension.dart, custom_copy_command.dart, custom_cut_command.dart, custom_paste_command.dart, math_equation_shortcut.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.816)
- **Top Global Matches:** file_cluster_4: 8.816, file_cluster_6: 8.998, file_cluster_0: 14.652
- **Magnitude:** 521.06 | **LOC:** 1410 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **73**; blast radius 0.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.1%), Guard Balance (formerly Safety Score) (51.4%), Connectivity (formerly Api Exposure) (34.4%)
- **Documentation Coverage:** 93.5484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_import_data` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as ...
  * `migrate_folder_views` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `replace_document_ref_ids` **(Defensive Guards)** (Impact: 32.7)
  * `migrate_databases` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `upload_collab_objects_data` **(Many-Argument Workhorses)** (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 290`, `args: 82`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `api: 15`, `concurrency: 5`, `import: 39`
* *Defense:* `safety: 32`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.008345
  * `Imports (Out-Degree: 16):` anyhow::anyhow, collab::core::collab::DataSource, collab::core::origin::CollabOrigin, collab::preclude::Any, collab::preclude::Collab, collab::preclude::Doc, collab::preclude::ReadTxn, collab::preclude::StateVector...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/shared/popup_menu/appflowy_popup_menu.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.293)
- **Top Global Matches:** file_cluster_4: 9.293, file_cluster_5: 9.85, file_cluster_12: 10.049
- **Magnitude:** 514.56 | **LOC:** 1668 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.149; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (78.1%), Debt Markers (formerly Tech Debt) (65.5%), Guard Balance (formerly Safety Score) (32.9%), Complexity Load (formerly Cognitive Load) (17.4%)
- **Documentation Coverage:** 72.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showMenu` **(Many-Argument Workhorses)** (Impact: 82.8)
    * *Intent:* /// [MaterialLocalizations.popupMenuLabel]. /// /// The `clipBehavior` argument is used to clip the ...
  * `build` **(Defensive Guards)** (Impact: 29.1)
  * `build` **(Defensive Guards)** (Impact: 27.0)
  * `showButtonMenu` **(Defensive Guards)** (Impact: 25.4)
    * *Intent:* /// A method to show a popup menu with the items supplied to /// [PopupMenuButton.itemBuilder] at th...
  * `buildPage` **(Many-Argument Workhorses)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 90`, `args: 48`, `func_start: 73`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 12`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 169`, `doc: 572`, `immutability_locks: 27`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` animated_gesture.dart, foundation.dart, material.dart, rendering.dart, scheduler.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/appflowy_flutter/lib/workspace/application/sidebar/space/space_bloc.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.676)
- **Top Global Matches:** file_cluster_4: 7.676, file_cluster_12: 11.459, file_cluster_0: 11.588
- **Magnitude:** 510.0 | **LOC:** 805 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.9%), Mutation Surface (formerly State Flux) (63.4%)
- **Documentation Coverage:** 97.3684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SpaceBloc` **(Many-Argument Workhorses)** (Impact: 80.1)
  * `async` **(I/O & Config Routines)** (Impact: 52.7)
  * `migrate` **(Compute Cores)** (Impact: 32.8)
  * `_createSpace` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `_setSpaceExpandStatus` **(Stateful Encapsulated Methods)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 142
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 138`, `args: 35`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 27`, `unreferenced_by_name: 7`
* *Architecture:* `api: 5`, `concurrency: 82`, `import: 27`
* *Defense:* `safety: 78`, `doc: 2`, `test: 1`, `immutability_locks: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart:async, dart:convert, kv.dart, kv_keys.dart, list_extension.dart, startup.dart, user_service.dart, string_extension.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.241)
- **Top Global Matches:** file_cluster_0: 8.241, file_cluster_15: 8.838, file_cluster_16: 9.343
- **Magnitude:** 505.9 | **LOC:** 925 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **57**; blast radius 0.343; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.8%), Guard Balance (formerly Safety Score) (46.8%)
- **Documentation Coverage:** 87.9518% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init_with_callback` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This f...
  * `refresh_user_profile` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `continue_sign_up` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `sign_in` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* /// Performs a user sign-in, initializing user awareness and sending relevant notifications. /// ///...
  * `new` **(Many-Argument Workhorses)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 203`, `args: 51`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 47`, `concurrency: 61`, `import: 38`
* *Defense:* `safety: 24`, `doc: 29`, `sync_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.343
  * `Choke Point (Betweenness):` 0.000286 | `Ripple Effect (Closeness):` 0.011989
  * `Imports (Out-Degree: 27):` client_api::entity::GotrueTokenResponse, collab::lock::RwLock, collab_integrate::CollabKVDB, collab_integrate::collab_builder::AppFlowyCollabBuilder, collab_user::core::UserAwareness, crate::entities::AuthStateChangedPB, crate::entities::AuthStatePB, crate::entities::UserProfilePB...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/user/application/reminder/reminder_bloc.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.649)
- **Top Global Matches:** file_cluster_4: 9.649, file_cluster_6: 9.991, file_cluster_12: 15.453
- **Magnitude:** 500.26 | **LOC:** 722 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.7%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkReminderAvailable` **(Defensive Guards)** (Impact: 47.6)
  * `_dispatch` **(Callbacks & Closures)** (Impact: 39.9)
  * `async` **(I/O & Config Routines)** (Impact: 39.7)
  * `_onArchived` **(Stateful Encapsulated Methods)** (Impact: 17.7)
    * *Intent:* /// Archive or unarchive reminders /// /// If the [reminderIds] is null, all reminders will be archi...
  * `ReminderState` **(Defensive Guards)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 113
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 116`, `args: 41`, `func_start: 29`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 45`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `concurrency: 58`, `import: 27`
* *Defense:* `safety: 51`, `doc: 16`, `test: 1`, `immutability_locks: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart:async, locale_keys.g.dart, document_data_pb_extension.dart, document_service.dart, mention_block.dart, list_extension.dart, startup.dart, reminder_extension.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/ai_manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.331)
- **Top Global Matches:** file_cluster_0: 7.331, file_cluster_15: 7.841, file_cluster_12: 9.146
- **Magnitude:** 496.78 | **LOC:** 814 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **58**; blast radius 0.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.3%), Guard Balance (formerly Safety Score) (48.7%)
- **Documentation Coverage:** 95.5224% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reload_with_workspace_id` **(Defensive Guards)** (Impact: 21.5)
  * `sync_chat_documents` **(Defensive Guards)** (Impact: 19.6)
  * `open_chat` **(Compute Cores)** (Impact: 18.4)
  * `update_rag_ids` **(Compute Cores)** (Impact: 15.6)
  * `stream_regenerate_response` **(Many-Argument Workhorses)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 145
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 234`, `args: 42`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `api: 36`, `concurrency: 120`, `import: 24`
* *Defense:* `safety: 19`, `doc: 15`, `sync_locks: 12`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.010615
  * `Imports (Out-Degree: 17):` crate::chat::Chat, crate::entities::AIModelPB, crate::entities::ChatInfoPB, crate::entities::ChatMessageListPB, crate::entities::ChatMessagePB, crate::entities::ChatSettingsPB, crate::entities::CustomPromptDatabaseConfigurationPB, crate::entities::FilePB...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/simple_table/simple_table_widgets/_simple_table_bottom_sheet_actions.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.078)
- **Top Global Matches:** file_cluster_16: 8.078, file_cluster_15: 8.612, file_cluster_0: 8.768
- **Magnitude:** 481.32 | **LOC:** 1298 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.2%), Guard Balance (formerly Safety Score) (44.2%), Debt Markers (formerly Tech Debt) (32.3%), Complexity Load (formerly Cognitive Load) (19.1%)
- **Documentation Coverage:** 90.411% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_onActionTap` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `_onActionTap` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `_onActionTap` **(Stateful Encapsulated Methods)** (Impact: 17.0)
  * `_onActionTap` **(Stateful Encapsulated Methods)** (Impact: 15.0)
  * `_buildActions` **(Callbacks & Closures)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 119`, `args: 62`, `func_start: 93`, `class_start: 23`
* *Risk/State:* `state_mutation: 19`, `duplicate_logic: 8`
* *Architecture:* `api: 17`, `concurrency: 28`, `import: 13`
* *Defense:* `safety: 87`, `doc: 37`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` flowy_svgs.g.dart, animated_gesture.dart, block_action_option_cubit.dart, option_actions.dart, clipboard_service.dart, simple_table.dart, startup.dart, log.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/appflowy_flutter/test/widget_test/date_picker_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.519)
- **Top Global Matches:** file_cluster_12: 8.519, file_cluster_11: 8.634, file_cluster_10: 8.804
- **Magnitude:** 474.64 | **LOC:** 914 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (43.4%), Guard Balance (formerly Safety Score) (37.8%), Connectivity (formerly Api Exposure) (0.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 48.4)
  * `build` **(Callbacks & Closures)** (Impact: 9.5)
  * `updateDateCellData` **(Defensive Guards)** (Impact: 7.4)
  * `async` **(I/O & Config Routines)** (Impact: 5.3)
  * `getLastMonth` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 148
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 127`, `args: 18`, `func_start: 106`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 65`, `duplicate_logic: 65`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `concurrency: 113`, `import: 18`
* *Defense:* `safety: 30`, `test: 257`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` util.dart, flowy_svgs.g.dart, date.dart, date_time_format.dart, appflowy_date_picker_base.dart, desktop_date_picker.dart, date_picker.dart, date_time_text_field.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.569)
- **Top Global Matches:** file_cluster_4: 8.569, file_cluster_15: 8.805, file_cluster_0: 8.832
- **Magnitude:** 472.2 | **LOC:** 892 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **61**; blast radius 0.287; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.2%), Guard Balance (formerly Safety Score) (46.8%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start_upload` **(Many-Argument Workhorses)** (Impact: 56.9)
  * `complete_upload` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `create_upload` **(Many-Argument Workhorses)** (Impact: 35.6)
  * `new` **(Defensive Guards)** (Impact: 21.2)
  * `query_file_state` **(Defensive Guards)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 229`, `args: 36`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 5`, `api: 17`, `concurrency: 78`, `import: 25`
* *Defense:* `safety: 33`, `doc: 2`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.287
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.009738
  * `Imports (Out-Degree: 15):` allo_isolate::Isolate, async_trait::async_trait, collab_importer::util::FileId, crate::entities::FileStatePB, crate::file_cache::FileTempStorage, crate::notification::StorageNotification, crate::notification::make_notification, crate::sqlite_sql::UploadFilePartTable...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-folder/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.545)
- **Top Global Matches:** file_cluster_0: 7.545, file_cluster_16: 9.569, file_cluster_13: 10.475
- **Magnitude:** 467.88 | **LOC:** 603 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.22; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.5%), Guard Balance (formerly Safety Score) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_view_handler` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `create_orphan_view_handler` **(Stateful Encapsulated Methods)** (Impact: 9.3)
  * `update_recent_views_handler` **(Stateful Encapsulated Methods)** (Impact: 7.6)
  * `set_default_publish_view_handler` **(Stateful Encapsulated Methods)** (Impact: 7.6)
  * `remove_user_from_shared_page_handler` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 112
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 197`, `args: 56`, `func_start: 50`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `api: 49`, `concurrency: 102`, `import: 10`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.009707
  * `Imports (Out-Degree: 6):` client_api::entity::guest_dto::RevokeSharedViewAccessRequest, crate::entities::*, crate::manager::FolderManager, crate::share::ImportParams, flowy_error::FlowyError, flowy_error::FlowyResult, lib_dispatch::prelude::AFPluginData, lib_dispatch::prelude::AFPluginState...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-server/src/af_cloud/impls/user/cloud_service_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_0: 6.321, file_cluster_15: 8.672, file_cluster_16: 9.275
- **Magnitude:** 458.72 | **LOC:** 693 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **69**; blast radius 0.222; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.4%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_user_profile` **(Defensive Guards)** (Impact: 19.4)
  * `create_collab_object` **(Compute Cores)** (Impact: 11.0)
  * `user_sign_in_with_url` **(Generic / Templated Code)** (Impact: 10.0)
  * `get_user_awareness_doc_state` **(Generic / Templated Code)** (Impact: 9.8)
  * `generate_sign_in_url_with_email` **(Generic / Templated Code)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 211`, `args: 55`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 43`, `concurrency: 94`, `import: 25`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.222
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.005316
  * `Imports (Out-Degree: 13):` anyhow::anyhow, arc_swap::ArcSwapOption, client_api::Client, client_api::ClientConfiguration, client_api::entity::AFWorkspace, client_api::entity::AFWorkspaceInvitation, client_api::entity::AFWorkspaceSettings, client_api::entity::AFWorkspaceSettingsChange...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `frontend/appflowy_flutter/lib/startup/tasks/deeplink/login_deeplink_handler.dart` (DART) | Magnitude: 12.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, import: 8, concurrency: 5
- `frontend/appflowy_flutter/lib/plugins/database/widgets/share_button.dart` (DART) | Magnitude: 45.54 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 35, args: 15, import: 15
- `frontend/appflowy_flutter/test/unit_test/theme/theme_test.dart` (DART) | Magnitude: 24.0 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 59, test: 20, structural_boundaries: 14, closures: 10
- `frontend/appflowy_flutter/lib/plugins/ai_chat/presentation/message/ai_metadata.dart` (DART) | Magnitude: 42.62 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 34, branch: 16, import: 15
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/bulleted_list/bulleted_list_icon.dart` (DART) | Magnitude: 29.24 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, core_var_decl: 12, structural_boundaries: 11, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `frontend/appflowy_flutter/lib/mobile/presentation/database/view/database_filter_bottom_sheet_cubit.dart` (DART) | Magnitude: 36.58 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, func_start: 13, structural_boundaries: 11, args: 11
- `frontend/appflowy_flutter/lib/plugins/database/application/field/type_option/select_option_type_option_bloc.dart` (DART) | Magnitude: 15.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 9, closures: 8, immutability_locks: 7
- `frontend/appflowy_flutter/lib/plugins/database/widgets/cell/editable_cell_skeleton/time.dart` (DART) | Magnitude: 40.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 29, import: 13, func_start: 11
- `frontend/appflowy_flutter/lib/features/util/extensions.dart` (DART) | Magnitude: 54.72 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 40, branch: 29, func_start: 10
- `frontend/appflowy_flutter/lib/plugins/database/calendar/presentation/calendar_event_card.dart` (DART) | Magnitude: 38.14 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 183, structural_boundaries: 31, import: 20, immutability_locks: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/inline_math_equation/inline_math_equation_toolbar_item.dart` (DART) | Magnitude: 6.12 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 15, branch: 12, core_var_decl: 12
- `frontend/appflowy_flutter/lib/startup/tasks/windows.dart` (DART) | Magnitude: 133.36 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 41, concurrency: 39, func_start: 23
- `frontend/appflowy_flutter/lib/plugins/ai_chat/application/chat_edit_document_service.dart` (DART) | Magnitude: 74.1 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 27, branch: 18, import: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `frontend/rust-lib/lib-infra/src/validator_fn.rs` (RUST) | Magnitude: 9.86 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, doc: 10, structural_boundaries: 5, branch: 4
- `frontend/appflowy_flutter/lib/mobile/presentation/widgets/flowy_option_tile.dart` (DART) | Magnitude: 156.76 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 282, branch: 55, safety: 51, structural_boundaries: 21
- `frontend/appflowy_flutter/lib/mobile/presentation/favorite/mobile_favorite_folder.dart` (DART) | Magnitude: 21.16 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 23, import: 13, args: 7
- `frontend/appflowy_flutter/lib/plugins/database/widgets/cell/card_cell_builder.dart` (DART) | Magnitude: 22.9 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 35, import: 18, closures: 14
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/actions/drag_to_reorder/draggable_option_button.dart` (DART) | Magnitude: 60.86 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 25, branch: 19, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frontend/appflowy_flutter/lib/ai/widgets/ai_prompt_modal/ai_prompt_onboarding.dart` (DART) | Magnitude: 13.22 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 12, import: 8, ui_framework: 5
- `frontend/appflowy_flutter/lib/workspace/presentation/widgets/date_picker/widgets/date_time_settings.dart` (DART) | Magnitude: 14.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 14, args: 9, func_start: 6
- `frontend/appflowy_flutter/lib/plugins/database/widgets/setting/setting_property_list.dart` (DART) | Magnitude: 37.48 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 31, import: 15, safety: 11
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/header/cover_editor.dart` (DART) | Magnitude: 32.44 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 14, safety: 13, func_start: 9
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/error/error_block_component_builder.dart` (DART) | Magnitude: 43.84 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 28, func_start: 16, import: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `frontend/rust-lib/flowy-document/tests/document/document_test.rs` (RUST) | Magnitude: 198.6 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 168, structural_boundaries: 90, core_var_decl: 58, design_snake_case: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/enum_serde.rs` (RUST) | Magnitude: 20.1 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 10, core_var_decl: 6, branch: 5
- `frontend/appflowy_flutter/lib/plugins/document/application/document_appearance_cubit.dart` (DART) | Magnitude: 236.74 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 174, branch: 46, safety: 37, concurrency: 31
- `frontend/appflowy_flutter/lib/mobile/presentation/notifications/widgets/tab_bar.dart` (DART) | Magnitude: 13.02 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 7, safety: 5, import: 4
- `frontend/appflowy_flutter/lib/shared/icon_emoji_picker/colors.dart` (DART) | Magnitude: 14.14 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 7, safety: 5, api: 5
- `frontend/rust-lib/flowy-server/src/local_server/util.rs` (RUST) | Magnitude: 13.5 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 13, import: 9, dead_code: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `frontend/appflowy_flutter/lib/user/application/reminder/reminder_listener.dart` (DART) | Magnitude: 46.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, branch: 14, structural_boundaries: 14, safety: 11
- `frontend/appflowy_flutter/lib/plugins/database/widgets/field/type_option_editor/relation.dart` (DART) | Magnitude: 30.22 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 29, safety: 13, import: 13
- `frontend/appflowy_flutter/lib/plugins/database/widgets/field/type_option_editor/media.dart` (DART) | Magnitude: 13.32 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 20, import: 13, args: 6
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/shared/document_color_setting_button.dart` (DART) | Magnitude: 96.12 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 346, structural_boundaries: 49, safety: 38, func_start: 27
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/cancel_plan_survey_dialog.dart` (DART) | Magnitude: 100.54 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 365, structural_boundaries: 32, func_start: 26, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frontend/rust-lib/flowy-user/src/services/mod.rs` (RUST) | Magnitude: 20.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, encapsulation: 1
- `frontend/rust-lib/flowy-ai/src/local_ai/mod.rs` (RUST) | Magnitude: 21.16 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7
- `frontend/rust-lib/flowy-database2/src/services/group/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, encapsulation: 6
- `frontend/rust-lib/flowy-server/src/local_server/impls/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, encapsulation: 6
- `frontend/rust-lib/flowy-database2/src/lib.rs` (RUST) | Magnitude: 22.2 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, api: 7, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `frontend/rust-lib/flowy-folder/src/entities/mod.rs` (RUST) | Magnitude: 26.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, api: 11, import: 6
- `frontend/rust-lib/flowy-storage/src/lib.rs` (RUST) | Magnitude: 17.68 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, api: 3
- `frontend/rust-lib/flowy-document/tests/assets/html/todo_list.html` (HTML) | Magnitude: 0.01 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, args: 2, api: 2, core_var_decl: 1
- `frontend/rust-lib/flowy-database2/tests/database/filter_test/mod.rs` (RUST) | Magnitude: 14.68 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/theme_upload/theme_upload_decoration.dart` (DART) | Magnitude: 7.32 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 6, ui_framework: 4, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `frontend/rust-lib/flowy-search/src/document/cloud_search_handler.rs` (RUST) | Magnitude: 55.74 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 42, import: 13, branch: 11
- `frontend/appflowy_flutter/lib/plugins/database/tab_bar/tab_bar_view.dart` (DART) | Magnitude: 229.16 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 383, structural_boundaries: 78, core_var_decl: 56, branch: 52
- `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/deserialize.rs` (RUST) | Magnitude: 107.12 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 57, core_var_decl: 43, design_snake_case: 36
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` (DART) | Magnitude: 205.5 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 59, core_var_decl: 35, concurrency: 34
- `frontend/rust-lib/flowy-document/tests/parser/json/block_test.rs` (RUST) | Magnitude: 14.8 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 22, test: 22, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `frontend/rust-lib/flowy-search-pub/src/tantivy_state.rs` (RUST) | Magnitude: 215.8 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 340, structural_boundaries: 96, branch: 67, core_var_decl: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `frontend/rust-lib/event-integration-test/tests/sql_test/chat_message_ordering_test.rs` (RUST) | Magnitude: 148.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 402, structural_boundaries: 138, core_var_decl: 91, design_snake_case: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/base/link_to_page_widget.dart` (DART) | Magnitude: 50.18 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 18, branch: 13, import: 9
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/base/cover_title_command.dart` (DART) | Magnitude: 53.62 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 80, branch: 24, structural_boundaries: 23, doc: 18
- `frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs` (RUST) | Magnitude: 539.8 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 693, structural_boundaries: 207, branch: 165, core_var_decl: 96
- `frontend/appflowy_flutter/lib/plugins/shared/share/share_button.dart` (DART) | Magnitude: 40.7 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 27, import: 17, branch: 13
- `frontend/appflowy_flutter/lib/plugins/ai_chat/chat_page.dart` (DART) | Magnitude: 26.6 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 19, import: 10, branch: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `frontend/appflowy_flutter/lib/workspace/application/sidebar/space/space_bloc.dart` -> Churn: **100.0%** | Cog Load: 97.8846% | Debt: 18.137%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `frontend/appflowy_flutter/lib/workspace/application/sidebar/space/space_bloc.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 510.0
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/outline/outline_block_component.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 179.76
- `frontend/appflowy_flutter/lib/features/share_tab/logic/share_tab_bloc.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 131.74
- `frontend/appflowy_flutter/lib/mobile/presentation/search/mobile_search_cell.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 63.76
- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/font/customize_font_toolbar_item.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 52.08

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/mod.rs` -> **Severity: 0.136** (Bridge: 0.0014 * Flux: 99.1837%)
- `frontend/rust-lib/event-integration-test/src/lib.rs` -> **Severity: 0.091** (Bridge: 0.0024 * Flux: 37.313%)
- `frontend/rust-lib/flowy-database2/src/manager.rs` -> **Severity: 0.054** (Bridge: 0.001 * Flux: 51.2989%)
- `frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/mod.rs` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 99.9036%)
- `frontend/rust-lib/flowy-database2/src/services/cell/cell_operation.rs` -> **Severity: 0.043** (Bridge: 0.0005 * Flux: 92.605%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `frontend/rust-lib/flowy-error/src/errors.rs` -> **Severity: 3.564** (Embedded: 0.0718 * Error Risk: 49.6063%)
- `frontend/rust-lib/build-tool/flowy-derive/src/node/mod.rs` -> **Severity: 3.378** (Embedded: 0.0525 * Error Risk: 64.3137%)
- `frontend/rust-lib/build-tool/flowy-ast/src/ctxt.rs` -> **Severity: 2.998** (Embedded: 0.0428 * Error Risk: 70.0%)
- `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/mod.rs` -> **Severity: 2.814** (Embedded: 0.0525 * Error Risk: 53.5654%)
- `frontend/rust-lib/lib-infra/src/validator_fn.rs` -> **Severity: 2.664** (Embedded: 0.0525 * Error Risk: 50.7142%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/rust-lib/build-tool/flowy-derive/src/lib.rs` -> **Severity: 2904.8** (Blast Radius: 29.048 * Doc Risk: 100.0%)
- `frontend/rust-lib/flowy-error/src/code.rs` -> **Severity: 1406.0** (Blast Radius: 14.06 * Doc Risk: 100.0%)
- `frontend/rust-lib/flowy-error/src/errors.rs` -> **Severity: 1156.9** (Blast Radius: 11.569 * Doc Risk: 100.0%)
- `frontend/rust-lib/build-tool/flowy-ast/src/ctxt.rs` -> **Severity: 874.5** (Blast Radius: 8.745 * Doc Risk: 100.0%)
- `frontend/rust-lib/build-tool/flowy-derive/src/dart_event/mod.rs` -> **Severity: 839.0** (Blast Radius: 8.39 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 112 literal sites + 266 sites through wrappers = 378
- **`panics_and_aborts`:** 219 literal sites + 9 sites through wrappers = 228

- `test` (function, debug_prints, primitive): 262 call sites in 57 files -- `frontend/rust-lib/flowy-database2/src/services/field/type_options/checklist_type_option/checklist_filter.rs`
- `_logOperations` (function, debug_prints, primitive): 4 call sites in 1 files -- `frontend/appflowy_flutter/lib/plugins/document/application/document_diff.dart`
- `stopAndExit` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `frontend/appflowy_flutter/lib/plugins/document/presentation/editor_plugins/ai/widgets/ai_writer_scroll_wrapper.dart`
- `FolderEventGetCurrentWorkspaceSetting` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `frontend/appflowy_flutter/test/bloc_test/home_test/view_bloc_test.dart`
- `load_asset_content` (function, panics_and_aborts, primitive): 2 call sites in 2 files -- `frontend/rust-lib/flowy-ai/tests/main.rs`
- `load_text_file_content` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `frontend/rust-lib/event-integration-test/tests/util.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 68461 call pairs -- scoped 15.6%, unique 0.0%, ambiguous 26.7%, external 57.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| dart | 42941 | 16.0% | 0.0% | 34.4% | 49.6% |
| rust | 25259 | 15.0% | 0.0% | 14.0% | 71.1% |
| cpp | 158 | 15.2% | 1.9% | 3.8% | 79.1% |
| ruby | 73 | 1.4% | 0.0% | 0.0% | 98.6% |
| swift | 25 | 12.0% | 0.0% | 0.0% | 88.0% |
| html | 5 | 20.0% | 0.0% | 0.0% | 80.0% |

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
