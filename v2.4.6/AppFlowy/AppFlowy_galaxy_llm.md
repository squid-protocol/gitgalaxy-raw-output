# ARCHITECTURAL_BRIEF: AppFlowy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/AppFlowy` |
| **Timestamp** | `2026-08-03T19:04:45.606606+00:00` |
| **Scan Duration** | `3.49s` |
| **Git Branch** | `main` |
| **Git Commit** | `4af02cdc87468be10ab15dbb4afd27fbf53ce89b` |
| **Git Remote** | `https://github.com/AppFlowy-IO/AppFlowy` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 792 malicious artifacts.

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
| Total Artifacts | 4597 |
| Analyzed Artifacts (Scanned) | 1704 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2893 |
| Total LOC | 96533 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 37.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8712 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4253 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8182 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 808 | 607 | 47.4% |
| RUST | 595 | 69309 | 34.9% |
| DART | 99 | 14520 | 5.8% |
| CPP | 54 | 2056 | 3.2% |
| PLAINTEXT | 36 | 2 | 2.1% |
| MARKDOWN | 26 | 0 | 1.5% |
| YAML | 21 | 233 | 1.2% |
| JSON | 18 | 8809 | 1.1% |
| SWIFT | 15 | 235 | 0.9% |
| KOTLIN | 7 | 69 | 0.4% |
| RUBY | 7 | 310 | 0.4% |
| GROOVY | 6 | 56 | 0.4% |
| OBJECTIVE-C | 4 | 4 | 0.2% |
| HTML | 3 | 195 | 0.2% |
| JAVA | 3 | 104 | 0.2% |
| JAVASCRIPT | 1 | 19 | 0.1% |
| MAKEFILE | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.038`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1193 | 70.0% |
| file_cluster_13 | 249 | 14.6% |
| file_cluster_0 | 79 | 4.6% |
| file_cluster_4 | 53 | 3.1% |
| file_cluster_16 | 34 | 2.0% |
| file_cluster_17 | 13 | 0.8% |
| file_cluster_2 | 4 | 0.2% |
| Unknown | 2 | 0.1% |
| file_cluster_9 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 3.5% |
| Static: Minified & Vendor Opaque Mass | 16 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2893*

**Composition by Extension & Reason:**
- `.dart`: 1876x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 308 LOC)
- `.png`: 201x Excluded (Explicitly Denied Extension: '.png')
- `.rs`: 150x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded (Unsupported Extension: '.xcworkspacedata'), 11x Excluded (Unsupported Extension: '.entitlements')
- `.json`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1064 LOC), 2x Excluded (Massive Static Asset Blob: 3468 LOC)
- `.sql`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.toml')
- `.svg`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcconfig`: 38x Excluded (Unsupported Extension: '.xcconfig')
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 25x Excluded (Explicitly Denied Extension: '.zip')
- `.sh`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 20x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.4 | 7.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 20.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.5 | 0.2 | 0.2 |
| API Exposure | 0.0 | 19.3 | 1.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 46.5 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 63.1 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.5 | 6.7 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (Hits: 22)
- `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile` (Hits: 20)
- `frontend/appflowy_flutter/packages/flowy_svg/bin/flowy_svg.dart` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **FlutterActivity.java** (`frontend/appflowy_flutter/packages/flowy_infra_ui/example/example/android/app/src/main/java/com/example/flowy_infra_ui_example/FlutterActivity.java`) — 5 inbound connections
2. **emoji_picker.dart** (`frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart`) — 3 inbound connections
3. **sizes.dart** (`frontend/appflowy_flutter/lib/plugins/trash/src/sizes.dart`) — 2 inbound connections
4. **emji_picker_config.dart** (`frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emji_picker_config.dart`) — 2 inbound connections
5. **emoji_view_state.dart** (`frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_view_state.dart`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **manager.rs** (`frontend/rust-lib/flowy-folder/src/manager.rs`) — 113 outbound dependencies
2. **database_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`) — 94 outbound dependencies
3. **view_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs`) — 87 outbound dependencies
4. **cloud_service_impl.rs** (`frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs`) — 77 outbound dependencies
5. **appflowy_data_import.rs** (`frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) — 73 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `generate_import_data` (@ `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) -> Impact: **616.7** | LOC: 1042
  * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as follows: /// root folder: /// - cache.db /// - log...
- `spawn_generate_embeddings` (@ `frontend/rust-lib/flowy-ai/src/embeddings/scheduler.rs`) -> Impact: **428.3** | LOC: 114
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/button/outlined_button/outlined_text_button.dart`) -> Impact: **409.3** | LOC: 219
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/button/outlined_button/outlined_icon_text_button.dart`) -> Impact: **389.3** | LOC: 224
- `init_with_callback` (@ `frontend/rust-lib/flowy-user/src/user_manager/manager.rs`) -> Impact: **354.5** | LOC: 182
  * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This function /// will be invoked each time the user ope...
- `duplicate_view_with_parent_id` (@ `frontend/rust-lib/flowy-folder/src/manager.rs`) -> Impact: **293.6** | LOC: 173
- `createState` (@ `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/popover.dart`) -> Impact: **289.4** | LOC: 357
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/button/filled_button/filled_icon_text_button.dart`) -> Impact: **288.9** | LOC: 197
- `import` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`) -> Impact: **286.0** | LOC: 247
- `import` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`) -> Impact: **286.0** | LOC: 247

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `start` (@ `frontend/rust-lib/flowy-ai/src/completion.rs`) -> **O(2^N) [Recursive]**
- `spawn_generate_embeddings` (@ `frontend/rust-lib/flowy-ai/src/embeddings/scheduler.rs`) -> **O(2^N) [Recursive]**
- `stream` (@ `frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs`) -> **O(2^N) [Recursive]**
- `poll` (@ `frontend/rust-lib/lib-dispatch/src/service/handler.rs`) -> **O(2^N) [Recursive]**
- `get_cells_for_field` (@ `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`) -> **O(2^N) [Recursive]**
- `share_page_with_user` (@ `frontend/rust-lib/flowy-folder/src/manager.rs`) -> **O(2^N) [Recursive]**
- `from_request` (@ `frontend/rust-lib/lib-dispatch/src/service/handler.rs`) -> **O(2^N) [Recursive]**
- `token_stream_for_field` (@ `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/deserialize.rs`) -> **O(2^N) [Recursive]**
- `gen_token_stream` (@ `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/serialize.rs`) -> **O(2^N) [Recursive]**
- `subscribe` (@ `frontend/rust-lib/event-integration-test/src/user_event.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `parse_KV_file_[Truncated]` (@ `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile`) -> DB Complexity: **61**
- `generate_import_data` (@ `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) -> DB Complexity: **52**
  * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as follows: /// root folder: /// - cache.db /// - log...
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/macos/Podfile`) -> DB Complexity: **42**
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/ios/Podfile`) -> DB Complexity: **36**
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/packages/appflowy_backend/example/ios/Podfile`) -> DB Complexity: **24**
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/packages/appflowy_ui/example/macos/Podfile`) -> DB Complexity: **24**
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/example/ios/Podfile`) -> DB Complexity: **24**
- `flutter_root_[Truncated]` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/example/macos/Podfile`) -> DB Complexity: **24**
- `createState` (@ `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart`) -> DB Complexity: **16**
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/shadcn/_mouse_area.dart`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `frontend/appflowy_flutter` | 8 | 5080.06 | 4.34% | 0.0% |
| `frontend/resources/flowy_icons/16x` | 485 | 5007.0 | 4.9% | 0.0% |
| `frontend/rust-lib/flowy-sqlite` | 1 | 5000.0 | 0.0% | 0.0% |
| `frontend/rust-lib/flowy-database2/src/services/database` | 5 | 3331.4 | 41.68% | 49.36% |
| `frontend/rust-lib/flowy-folder/src` | 11 | 2964.06 | 21.27% | 49.5% |
| `frontend/rust-lib/flowy-ai/src` | 11 | 2881.8 | 36.18% | 57.58% |
| `frontend/rust-lib/flowy-user/src/user_manager` | 6 | 2696.52 | 28.38% | 44.44% |
| `frontend/rust-lib/flowy-database2/src` | 6 | 1820.38 | 19.88% | 52.0% |
| `frontend/rust-lib/flowy-core/src` | 10 | 1809.18 | 33.65% | 44.79% |
| `frontend/rust-lib/flowy-storage/src` | 9 | 1805.76 | 32.35% | 67.49% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `frontend/appflowy_flutter/linux/main.cc` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-ast/src/symbol.rs` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-derive/src/dart_event/mod.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-ai/src/local_ai/completion/writer.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-database2/src/entities/board_entities.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `frontend/appflowy_flutter/linux/my_application.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/flowy_infra_ui/linux/flowy_infra_u_i_plugin.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/flowy_infra_ui/linux/flowy_infra_ui_plugin.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/windows/runner/main.cpp` -> **100.0%** Exposure
- `frontend/appflowy_flutter/windows/runner/utils.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` -> **55** Orphaned Functions | **26** Duplicates
- `frontend/rust-lib/flowy-database2/src/event_handler.rs` -> **72** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-user/src/event_handler.rs` -> **53** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-folder/src/event_handler.rs` -> **49** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/event-integration-test/src/database_event.rs` -> **47** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`frontend/appflowy_flutter/packages/appflowy_backend/android/src/main/kotlin/com/plugin/appflowy_backend/AppFlowyBackendPlugin.kt`** -> AI Confidence: **99.48%**
2. **`frontend/appflowy_flutter/packages/flowy_infra_ui/android/src/main/kotlin/com/example/flowy_infra_ui/FlowyInfraUiPlugin.kt`** -> AI Confidence: **99.34%**
3. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`** -> AI Confidence: **99.32%**
4. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`** -> AI Confidence: **99.32%**
5. **`frontend/rust-lib/flowy-sqlite-vec/src/db.rs`** -> AI Confidence: **99.31%**
6. **`frontend/rust-lib/flowy-user/src/services/db.rs`** -> AI Confidence: **99.31%**
7. **`frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs`** -> AI Confidence: **99.31%**
8. **`frontend/rust-lib/lib-infra/src/file_util.rs`** -> AI Confidence: **99.31%**
9. **`frontend/rust-lib/lib-log/src/layer.rs`** -> AI Confidence: **99.31%**
10. **`commitlint.config.js`** -> AI Confidence: **99.29%**
11. **`frontend/appflowy_flutter/macos/Podfile`** -> AI Confidence: **99.29%**
12. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart`** -> AI Confidence: **99.29%**
13. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_dialog.dart`** -> AI Confidence: **99.29%**
14. **`frontend/appflowy_flutter/packages/appflowy_backend/windows/include/appflowy_backend/app_flowy_backend_plugin.h`** -> AI Confidence: **99.29%**
15. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart`** -> AI Confidence: **99.25%**
16. **`frontend/rust-lib/build-tool/flowy-ast/src/pb_attrs.rs`** -> AI Confidence: **99.24%**
17. **`frontend/rust-lib/flowy-ai/src/embeddings/context.rs`** -> AI Confidence: **99.24%**
18. **`frontend/rust-lib/flowy-ai/src/event_handler.rs`** -> AI Confidence: **99.24%**
19. **`frontend/rust-lib/flowy-core/src/app_life_cycle.rs`** -> AI Confidence: **99.24%**
20. **`frontend/rust-lib/flowy-database2/src/entities/filter_entities/util.rs`** -> AI Confidence: **99.24%**
21. **`frontend/rust-lib/flowy-database2/src/entities/type_option_entities/date_entities.rs`** -> AI Confidence: **99.24%**
22. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/number_type_option/number_filter.rs`** -> AI Confidence: **99.24%**
23. **`frontend/rust-lib/flowy-database2/src/services/group/controller_impls/select_option_controller/util.rs`** -> AI Confidence: **99.24%**
24. **`frontend/rust-lib/flowy-document/src/parser/external/utils.rs`** -> AI Confidence: **99.24%**
25. **`frontend/rust-lib/flowy-document/src/parser/parser_entities.rs`** -> AI Confidence: **99.24%**
26. **`frontend/rust-lib/flowy-search-pub/src/tantivy_state.rs`** -> AI Confidence: **99.24%**
27. **`frontend/rust-lib/flowy-user-pub/src/sql/workspace_sql.rs`** -> AI Confidence: **99.24%**
28. **`frontend/rust-lib/flowy-user/src/event_handler.rs`** -> AI Confidence: **99.24%**
29. **`frontend/rust-lib/flowy-user/src/services/billing_check.rs`** -> AI Confidence: **99.24%**
30. **`frontend/rust-lib/flowy-user/src/user_manager/manager.rs`** -> AI Confidence: **99.24%**
31. **`frontend/rust-lib/flowy-user/src/user_manager/manager_user_encryption.rs`** -> AI Confidence: **99.24%**
32. **`frontend/rust-lib/lib-dispatch/src/response/response.rs`** -> AI Confidence: **99.24%**
33. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/shadcn/_mouse_area.dart`** -> AI Confidence: **99.23%**
34. **`frontend/rust-lib/build-tool/flowy-ast/src/event_attrs.rs`** -> AI Confidence: **99.23%**
35. **`frontend/rust-lib/flowy-database2/src/entities/group_entities/group_changeset.rs`** -> AI Confidence: **99.23%**
36. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/appflowy_popover.dart`** -> AI Confidence: **99.2%**
37. **`frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/proto_gen.rs`** -> AI Confidence: **99.18%**
38. **`frontend/rust-lib/dart-ffi/src/appflowy_yaml.rs`** -> AI Confidence: **99.18%**
39. **`frontend/rust-lib/dart-ffi/src/lib.rs`** -> AI Confidence: **99.18%**
40. **`frontend/rust-lib/flowy-ai-pub/src/persistence/collab_metadata_sql.rs`** -> AI Confidence: **99.18%**
41. **`frontend/rust-lib/flowy-ai-pub/src/persistence/local_model_sql.rs`** -> AI Confidence: **99.18%**
42. **`frontend/rust-lib/flowy-ai/src/completion.rs`** -> AI Confidence: **99.18%**
43. **`frontend/rust-lib/flowy-ai/src/embeddings/store.rs`** -> AI Confidence: **99.18%**
44. **`frontend/rust-lib/flowy-ai/src/entities.rs`** -> AI Confidence: **99.18%**
45. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs`** -> AI Confidence: **99.18%**
46. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/llm_chat.rs`** -> AI Confidence: **99.18%**
47. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/mod.rs`** -> AI Confidence: **99.18%**
48. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/retriever/sqlite_retriever.rs`** -> AI Confidence: **99.18%**
49. **`frontend/rust-lib/flowy-ai/src/local_ai/completion/chain.rs`** -> AI Confidence: **99.18%**
50. **`frontend/rust-lib/flowy-ai/src/local_ai/completion/stream_interpreter.rs`** -> AI Confidence: **99.18%**
51. **`frontend/rust-lib/flowy-core/src/deps_resolve/chat_deps.rs`** -> AI Confidence: **99.18%**
52. **`frontend/rust-lib/flowy-core/src/deps_resolve/database_deps.rs`** -> AI Confidence: **99.18%**
53. **`frontend/rust-lib/flowy-core/src/deps_resolve/file_storage_deps.rs`** -> AI Confidence: **99.18%**
54. **`frontend/rust-lib/flowy-core/src/deps_resolve/folder_deps/folder_deps_chat_impl.rs`** -> AI Confidence: **99.18%**
55. **`frontend/rust-lib/flowy-core/src/deps_resolve/user_deps.rs`** -> AI Confidence: **99.18%**
56. **`frontend/rust-lib/flowy-core/src/folder_view_observer.rs`** -> AI Confidence: **99.18%**
57. **`frontend/rust-lib/flowy-core/src/server_layer.rs`** -> AI Confidence: **99.18%**
58. **`frontend/rust-lib/flowy-database2/src/entities/calendar_entities.rs`** -> AI Confidence: **99.18%**
59. **`frontend/rust-lib/flowy-database2/src/entities/cell_entities.rs`** -> AI Confidence: **99.18%**
60. **`frontend/rust-lib/flowy-database2/src/entities/database_entities.rs`** -> AI Confidence: **99.18%**
61. **`frontend/rust-lib/flowy-database2/src/entities/filter_entities/date_filter.rs`** -> AI Confidence: **99.18%**
62. **`frontend/rust-lib/flowy-database2/src/entities/group_entities/group.rs`** -> AI Confidence: **99.18%**
63. **`frontend/rust-lib/flowy-database2/src/entities/setting_entities.rs`** -> AI Confidence: **99.18%**
64. **`frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`** -> AI Confidence: **99.18%**
65. **`frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs`** -> AI Confidence: **99.18%**
66. **`frontend/rust-lib/flowy-database2/src/services/database_view/view_group.rs`** -> AI Confidence: **99.18%**
67. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/checkbox_type_option/checkbox_filter.rs`** -> AI Confidence: **99.18%**
68. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/checkbox_type_option/checkbox_type_option_entities.rs`** -> AI Confidence: **99.18%**
69. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/checklist_type_option/checklist_type_option.rs`** -> AI Confidence: **99.18%**
70. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/selection_type_option/multi_select_type_option.rs`** -> AI Confidence: **99.18%**
71. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/selection_type_option/select_type_option.rs`** -> AI Confidence: **99.18%**
72. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/selection_type_option/type_option_transform.rs`** -> AI Confidence: **99.18%**
73. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/summary_type_option/summary.rs`** -> AI Confidence: **99.18%**
74. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/time_type_option/time.rs`** -> AI Confidence: **99.18%**
75. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/timestamp_type_option/timestamp_type_option.rs`** -> AI Confidence: **99.18%**
76. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/translate_type_option/translate.rs`** -> AI Confidence: **99.18%**
77. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/type_option_cell.rs`** -> AI Confidence: **99.18%**
78. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/url_type_option/url_type_option.rs`** -> AI Confidence: **99.18%**
79. **`frontend/rust-lib/flowy-database2/src/services/group/configuration.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/popover.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/example/lib/src/dropdown_menu/dropdown_menu_page.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/example/lib/src/menu/menu_page.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/mod.rs` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-codegen/src/ts_event/mod.rs` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-codegen/src/util.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-storage/src/sqlite_sql.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `frontend/rust-lib/flowy-ai/src/local_ai/completion/writer.rs` -> **0.001%** Exposure
### Algorithmic DoS Exposure
- `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/default_emoji_picker_view.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/example/lib/src/dropdown_menu/dropdown_menu_page.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/example/lib/src/modal/modal_page.dart` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7258` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `frontend/rust-lib/lib-infra/src/priority_task/scheduler.rs` (RUST) -> Cumulative Risk: **820.81**
- **Archetype:** `file_cluster_4` (Distance: 12.625 IQR)
- **Magnitude:** 251.78 | **LOC:** 215 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9476%)
- **Heaviest Functions:** `process_next_task` (Impact: 50.0), `run` (Impact: 19.2), `run` (Impact: 7.9)

### 2. `frontend/rust-lib/flowy-storage/src/uploader.rs` (RUST) -> Cumulative Risk: **792.12**
- **Archetype:** `file_cluster_4` (Distance: 11.759 IQR)
- **Magnitude:** 377.76 | **LOC:** 381 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.144%), Cognitive Load (97.103%)
- **Heaviest Functions:** `process_next` (Impact: 103.0), `run` (Impact: 36.6), `remove_task` (Impact: 21.0)

### 3. `frontend/rust-lib/lib-dispatch/src/service/handler.rs` (RUST) -> Cumulative Risk: **790.4**
- **Archetype:** `file_cluster_4` (Distance: 11.435 IQR)
- **Magnitude:** 195.5 | **LOC:** 247 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (97.4328%)
- **Heaviest Functions:** `poll` (Impact: 61.7), `poll` (Impact: 29.1), `from_request` (Impact: 10.7)

### 4. `frontend/rust-lib/flowy-ai/src/completion.rs` (RUST) -> Cumulative Risk: **750.64**
- **Archetype:** `file_cluster_4` (Distance: 11.424 IQR)
- **Magnitude:** 285.82 | **LOC:** 208 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Cognitive Load (90.5214%)
- **Heaviest Functions:** `start` (Impact: 144.1), `handle_error` (Impact: 19.9), `create_complete_task` (Impact: 18.4)

### 5. `frontend/rust-lib/flowy-database2/src/services/group/controller_impls/checkbox_controller.rs` (RUST) -> Cumulative Risk: **749.32**
- **Archetype:** `file_cluster_13` (Distance: 12.242 IQR)
- **Magnitude:** 109.86 | **LOC:** 163 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9987%), State Flux (99.5559%), Concurrency (97.7059%)
- **Heaviest Functions:** `add_or_remove_row_when_cell_changed` (Impact: 28.4), `delete_row` (Impact: 11.0), `can_group` (Impact: 7.3)

### 6. `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` (RUST) -> Cumulative Risk: **748.5**
- **Archetype:** `file_cluster_4` (Distance: 13.175 IQR)
- **Magnitude:** 2806.9 | **LOC:** 2465 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.962%), Tech Debt (99.7823%)
- **Heaviest Functions:** `async_load_rows` (Impact: 133.1), `get_cells_for_field` (Impact: 85.7), `open_database_view` (Impact: 76.7)

### 7. `frontend/rust-lib/lib-infra/src/ref_map.rs` (RUST) -> Cumulative Risk: **712.51**
- **Archetype:** `file_cluster_4` (Distance: 11.762 IQR)
- **Magnitude:** 100.78 | **LOC:** 93 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9961%), Cognitive Load (96.4846%)
- **Heaviest Functions:** `remove` (Impact: 26.8), `insert` (Impact: 12.4), `values` (Impact: 3.8)

### 8. `frontend/rust-lib/flowy-storage/src/sqlite_sql.rs` (RUST) -> Cumulative Risk: **703.24**
- **Archetype:** `file_cluster_17` (Distance: 12.91 IQR)
- **Magnitude:** 220.28 | **LOC:** 259 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Algorithmic Dos (99.9989%), State Flux (99.9613%)
- **Heaviest Functions:** `delete_upload_file_by_file_id` (Impact: 40.7), `_delete_upload_file` (Impact: 9.5), `update_upload_file_upload_id` (Impact: 8.9)

### 9. `frontend/rust-lib/lib-log/src/layer.rs` (RUST) -> Cumulative Risk: **698.9**
- **Archetype:** `file_cluster_13` (Distance: 12.844 IQR)
- **Magnitude:** 373.32 | **LOC:** 262 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (98.6166%), Concurrency (91.4901%)
- **Heaviest Functions:** `on_event` (Impact: 142.8), `serialize_span` (Impact: 86.6), `format_event_message` (Impact: 20.0)

### 10. `frontend/rust-lib/flowy-user-pub/src/sql/workspace_sql.rs` (RUST) -> Cumulative Risk: **684.59**
- **Archetype:** `file_cluster_17` (Distance: 11.805 IQR)
- **Magnitude:** 190.72 | **LOC:** 277 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (96.5986%), Injection Surface (94.3195%)
- **Heaviest Functions:** `sync_user_workspaces_with_diff` (Impact: 56.8), `delete_user_workspace` (Impact: 11.0), `from_version` (Impact: 9.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `frontend/appflowy_flutter/dsa_pub.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-sqlite/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.175 IQR)
- **Top Global Matches:** file_cluster_4: 13.175, file_cluster_8: 13.591, file_cluster_13: 13.61
- **Magnitude:** 2806.9 | **LOC:** 2465 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (95.4098%), Tech Debt (99.7823%)
**Top Internal Functions/Classes:**
  * `async_load_rows` (Impact: 133.1 | O(N^4) | DB: 7)
  * `get_cells_for_field` (Impact: 85.7 | O(2^N))
  * `open_database_view` (Impact: 76.7 | O(N^3) | DB: 5)
  * `new` (Impact: 72.3 | O(2^N))
  * `duplicate_row` (Impact: 65.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 715`, `args: 122`, `func_start: 129`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 150`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 26`, `orphaned_logic: 55`
* *Architecture:* `api: 84`, `concurrency: 885`, `import: 50`
* *Defense:* `safety: 347`, `doc: 20`, `test: 1`, `sync_locks: 19`, `immutability_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib_infra::priority_task::TaskDispatcher, stringify_cell, warn, collab_database::template::timestamp_parse::TimestampCellData, collab_database::database::Database, collab::lock::RwLock, lib_infra::box_any::BoxAny, crate::services::database_view::
  DatabaseViewChanged...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.795 IQR)
- **Top Global Matches:** file_cluster_4: 13.795, file_cluster_13: 13.939, file_cluster_0: 13.968
- **Magnitude:** 1870.96 | **LOC:** 2638 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (31.2871%), Tech Debt (60.5181%)
**Top Internal Functions/Classes:**
  * `duplicate_view_with_parent_id` (Impact: 293.6 | O(N^4) | DB: 4)
  * `get_shared_page_details` (Impact: 125.0 | O(2^N) | DB: 3)
  * `publish_view` (Impact: 120.6 | O(2^N) | DB: 2)
  * `share_page_with_user` (Impact: 99.5 | O(2^N) | DB: 2)
  * `initialize_after_sign_up` (Impact: 64.6 | O(N^3))
    * *Intent:* /// Initialize the folder for the new user. /// Using the [DefaultFolderBuilder] to create the defau...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 385`, `args: 113`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 102`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 26`
* *Architecture:* `api: 61`, `concurrency: 254`, `import: 36`
* *Defense:* `safety: 232`, `doc: 144`, `sync_locks: 41`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collab_folder::folder_diff::FolderViewChange, Section, ViewLayoutPB, FolderData, RepeatedViewIdPB, collab::lock::RwLock, RepeatedSharedViewResponsePB, crate::entities::
  AFAccessLevelPB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.278 IQR)
- **Top Global Matches:** file_cluster_13: 13.278, file_cluster_4: 13.35, file_cluster_0: 13.39
- **Magnitude:** 1168.06 | **LOC:** 925 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (30.6321%), Tech Debt (37.7242%)
**Top Internal Functions/Classes:**
  * `init_with_callback` (Impact: 354.5 | O(N^5) | DB: 7)
    * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This f...
  * `new` (Impact: 94.9 | O(2^N) | DB: 2)
  * `refresh_user_profile` (Impact: 39.9 | O(N^2))
  * `sign_in` (Impact: 38.1 | O(2^N))
    * *Intent:* /// Performs a user sign-in, initializing user awareness and sending relevant notifications. /// ///...
  * `sign_out` (Impact: 30.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 201`, `args: 47`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 86`, `import: 38`
* *Defense:* `safety: 171`, `doc: 29`, `sync_locks: 9`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UserSettingPB, flowy_user_pub::workspace_service::UserWorkspaceService, flowy_user_pub::entities::*, collab_user::core::UserAwareness, flowy_sqlite::schema::user_table, flowy_user_pub::cloud::UserCloudServiceProvider, warn, flowy_user_pub::session::Session...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.909 IQR)
- **Top Global Matches:** file_cluster_0: 11.909, file_cluster_4: 11.933, file_cluster_8: 11.939
- **Magnitude:** 1144.7 | **LOC:** 1451 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (52.5266%), Tech Debt (99.7998%)
**Top Internal Functions/Classes:**
  * `update_database_setting_handler` (Impact: 48.7 | O(N^1))
  * `rename_media_cell_file_handler` (Impact: 36.8 | O(N^2) | DB: 1)
    * *Intent:* /// We use a custom handler to rename the media file, as the ordering /// of the files must be maint...
  * `get_default_database_view_id_handler` (Impact: 19.1 | O(N^2) | DB: 1)
  * `new_select_option_handler` (Impact: 16.1 | O(N^2))
  * `update_field_type_option_handler` (Impact: 14.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 462`, `args: 82`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 12`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 72`
* *Architecture:* `api: 72`, `concurrency: 248`, `import: 15`
* *Defense:* `safety: 115`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::services::field::date_filter::DateCellChangeset, crate::services::share::csv::CSVFormat, tracing::info, FlowyResult, RowCover, lib_infra::box_any::BoxAny, crate::manager::DatabaseManager, collab_database::rows::Cell...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.524 IQR)
- **Top Global Matches:** file_cluster_4: 12.524, file_cluster_8: 12.602, file_cluster_13: 12.723
- **Magnitude:** 1050.3 | **LOC:** 822 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (69.0755%), Tech Debt (24.5883%)
**Top Internal Functions/Classes:**
  * `get_all_user_workspaces` (Impact: 109.3 | O(N^4) | DB: 5)
  * `open_workspace` (Impact: 102.7 | O(N^2) | DB: 2)
  * `get_workspace_settings` (Impact: 58.2 | O(N^3) | DB: 5)
  * `create_workspace` (Impact: 50.6 | O(2^N) | DB: 2)
  * `upload_collab_data` (Impact: 42.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 207`, `args: 37`, `func_start: 32`
* *Risk/State:* `state_mutation: 72`, `orphaned_logic: 10`
* *Architecture:* `api: 26`, `concurrency: 110`, `import: 19`
* *Defense:* `safety: 88`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WorkspaceSubscriptionInfoPB, ImportedFolder, UpdateUserWorkspaceSettingPB, FlowyResult, flowy_user_pub::session::Session, client_api::entity::billing_dto::SubscriptionPlan, WorkspaceMember, flowy_sqlite::ConnectionPool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.925 IQR)
- **Top Global Matches:** file_cluster_4: 12.925, file_cluster_8: 13.091, file_cluster_13: 13.144
- **Magnitude:** 996.9 | **LOC:** 892 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (64.104%), Tech Debt (54.3678%)
**Top Internal Functions/Classes:**
  * `start_upload` (Impact: 130.2 | O(N^3) | DB: 7)
  * `complete_upload` (Impact: 113.8 | O(2^N) | DB: 2)
  * `new` (Impact: 103.9 | O(2^N) | DB: 3)
  * `create_upload` (Impact: 77.7 | O(N^3))
  * `resume_upload` (Impact: 52.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 229`, `args: 36`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 66`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 5`, `api: 15`, `concurrency: 153`, `import: 25`
* *Defense:* `safety: 159`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` delete_upload_file, MIN_CHUNK_SIZE, allo_isolate::Isolate, collab_importer::util::FileId, Signal, UploadTask, watch, async_trait::async_trait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-sqlite-vec/src/db.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.392 IQR)
- **Top Global Matches:** file_cluster_8: 12.392, file_cluster_13: 12.439, file_cluster_17: 12.487
- **Magnitude:** 890.8 | **LOC:** 639 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (43.7732%), Tech Debt (17.543%)
**Top Internal Functions/Classes:**
  * `upsert_collabs_embeddings` (Impact: 214.6 | O(N^4) | DB: 4)
    * *Intent:* /// Inserts or replaces all of `fragments` for the given (workspace_id, object_id), /// deleting any...
  * `select_all_embedded_documents` (Impact: 104.8 | O(N^4) | DB: 5)
  * `delete_collab` (Impact: 71.0 | O(2^N) | DB: 1)
  * `select_collabs_fragment_ids` (Impact: 68.1 | O(2^N) | DB: 3)
  * `select_all_embedded_content` (Impact: 57.5 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 146`, `args: 29`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 94`, `orphaned_logic: 5`
* *Architecture:* `api: 12`, `concurrency: 21`, `import: 14`
* *Defense:* `safety: 46`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warn, SqliteEmbeddedFragment, serde_json::Value, crate::init_sqlite_vector_extension, params, anyhow::Context, r2d2::Pool, r2d2_sqlite::SqliteConnectionManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.379 IQR)
- **Top Global Matches:** file_cluster_8: 12.379, file_cluster_0: 12.537, file_cluster_7: 13.04
- **Magnitude:** 847.56 | **LOC:** 538 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (99.996%)
**Top Internal Functions/Classes:**
  * `TextStyle` (Impact: 183.7 | O(2^N))
  * `TextStyle` (Impact: 183.7 | O(2^N))
  * `TextStyle` (Impact: 183.7 | O(2^N))
  * `TextStyle` (Impact: 183.7 | O(2^N))
  * `import` (Impact: 14.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 50`, `args: 40`, `func_start: 94`, `class_start: 9`
* *Risk/State:* `duplicate_logic: 24`, `orphaned_logic: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 199`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` widgets.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.58 IQR)
- **Top Global Matches:** file_cluster_13: 12.58, file_cluster_8: 12.648, file_cluster_17: 12.705
- **Magnitude:** 837.94 | **LOC:** 1410 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (18.286%), Tech Debt (10.6348%)
**Top Internal Functions/Classes:**
  * `generate_import_data` (Impact: 616.7 | O(N^4) | DB: 52)
    * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as ...
  * `prepare_import` (Impact: 54.0 | O(N^2) | DB: 4)
  * `migrate_user_awareness` (Impact: 2.8 | O(N^1) | DB: 1)
  * `with_container_name` (Impact: 1.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 257`, `args: 74`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `state_mutation: 112`, `dead_code: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 12`, `concurrency: 17`, `import: 39`
* *Defense:* `safety: 111`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::services::data_import::importer::load_collab_by_object_ids, Update, ViewLayout, flowy_folder_pub::entities::
  ImportFrom, flowy_user_pub::sql::select_user_auth_type, warn, crate::services::db::UserDBPath, collab_database::workspace_database::WorkspaceDatabase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.758 IQR)
- **Top Global Matches:** file_cluster_8: 11.758, file_cluster_13: 12.144, file_cluster_16: 12.205
- **Magnitude:** 829.8 | **LOC:** 919 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.0282%), Tech Debt (13.3418%)
**Top Internal Functions/Classes:**
  * `upload_part` (Impact: 28.1 | O(2^N))
  * `get_plugins` (Impact: 24.1 | O(N^4))
  * `generate_search_summary` (Impact: 22.8 | O(2^N))
  * `create_upload` (Impact: 17.7 | O(2^N))
  * `complete_upload` (Impact: 17.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 149`, `args: 67`, `func_start: 65`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `concurrency: 121`, `import: 37`
* *Defense:* `safety: 94`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_document::deps::DocumentData, TranslateRowContent, serde_json::Value, SyncPlugin, UserCloudServiceProvider, flowy_error::FlowyError, CollabPluginProviderContext, SharedViewDetails...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/ai_manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.603 IQR)
- **Top Global Matches:** file_cluster_4: 12.603, file_cluster_8: 12.782, file_cluster_13: 12.788
- **Magnitude:** 794.9 | **LOC:** 814 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (55.7497%), Tech Debt (31.0481%)
**Top Internal Functions/Classes:**
  * `open_chat` (Impact: 65.2 | O(2^N) | DB: 3)
  * `toggle_local_ai` (Impact: 49.0 | O(2^N) | DB: 2)
  * `reload_with_workspace_id` (Impact: 44.0 | O(N^2))
  * `sync_chat_documents` (Impact: 41.8 | O(N^3))
  * `stream_regenerate_response` (Impact: 29.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 234`, `args: 42`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `orphaned_logic: 12`
* *Architecture:* `api: 36`, `concurrency: 170`, `import: 24`
* *Defense:* `safety: 137`, `doc: 15`, `sync_locks: 12`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChatSettings, select_chat_rag_ids, CustomPromptDatabaseConfigurationPB, chat_notification_builder, ServerModelStorageImpl, warn, LocalAiSource, crate::middleware::chat_service_mw::ChatServiceMiddleware...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.257 IQR)
- **Top Global Matches:** file_cluster_0: 12.257, file_cluster_8: 12.335, file_cluster_16: 12.351
- **Magnitude:** 729.04 | **LOC:** 865 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (45.4728%), Tech Debt (98.6313%)
**Top Internal Functions/Classes:**
  * `import_appflowy_data_folder_handler` (Impact: 22.4 | O(N^2))
  * `get_workspace_member_info` (Impact: 20.6 | O(2^N))
  * `set_cloud_config_handler` (Impact: 19.7 | O(N^1) | DB: 1)
  * `get_date_time_settings` (Impact: 18.4 | O(N^3) | DB: 2)
  * `get_user_profile_handler` (Impact: 17.2 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 238`, `args: 60`, `func_start: 57`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 53`
* *Architecture:* `api: 55`, `concurrency: 119`, `import: 17`
* *Defense:* `safety: 100`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sync::Arc, flowy_user_pub::entities::*, FlowyResult, serde_json::Value, lib_infra::box_any::BoxAny, crate::services::data_import::prepare_import, std::sync::Weak, crate::user_manager::UserManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/embeddings/scheduler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.334 IQR)
- **Top Global Matches:** file_cluster_13: 12.334, file_cluster_8: 12.368, file_cluster_4: 12.378
- **Magnitude:** 716.36 | **LOC:** 355 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.6553%), Tech Debt (13.3418%)
**Top Internal Functions/Classes:**
  * `spawn_generate_embeddings` (Impact: 428.3 | O(2^N) | DB: 5)
  * `spawn_write_embeddings` (Impact: 109.9 | O(2^N) | DB: 4)
  * `search` (Impact: 46.8 | O(2^N))
  * `generate_summary` (Impact: 26.8 | O(N^3))
  * `delete_collab` (Impact: 12.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 74`, `args: 18`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `orphaned_logic: 2`
* *Architecture:* `api: 9`, `concurrency: 46`, `import: 16`
* *Defense:* `safety: 57`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::search::summary::LLMDocument, UnboundedSender, flowy_ai_pub::cloud::search_dto::
  SearchContentType, crate::embeddings::indexer::IndexerProvider, crate::embeddings::embedder::Embedder, OllamaEmbedder, warn, unbounded_channel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/chat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.976 IQR)
- **Top Global Matches:** file_cluster_8: 11.976, file_cluster_4: 11.98, file_cluster_13: 12.093
- **Magnitude:** 675.58 | **LOC:** 668 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (38.6307%), Tech Debt (30.9554%)
**Top Internal Functions/Classes:**
  * `stream_response` (Impact: 283.9 | O(N^6) | DB: 4)
  * `load_remote_chat_messages` (Impact: 72.3 | O(N^3) | DB: 2)
  * `load_prev_chat_messages` (Impact: 22.4 | O(N^2) | DB: 1)
    * *Intent:* /// Load chat messages for a given `chat_id`. /// /// 1. When opening a chat: /// - Loads local chat...
  * `get_question_id_from_answer_id` (Impact: 21.4 | O(N^2))
  * `stream_chat_message` (Impact: 18.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 146`, `args: 27`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 27`, `orphaned_logic: 10`
* *Architecture:* `api: 13`, `concurrency: 101`, `import: 18`
* *Defense:* `safety: 86`, `doc: 12`, `sync_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chat_notification_builder, futures::SinkExt, select_chat_messages, flowy_ai_pub::persistence::
  ChatMessageTable, crate::middleware::chat_service_mw::ChatServiceMiddleware, FlowyResult, PredefinedFormatPB, crate::notification::ChatNotification...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/filter/controller.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.993 IQR)
- **Top Global Matches:** file_cluster_4: 12.993, file_cluster_13: 13.292, file_cluster_8: 13.441
- **Magnitude:** 659.7 | **LOC:** 563 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (97.5913%), Tech Debt (52.5488%)
**Top Internal Functions/Classes:**
  * `filter_row` (Impact: 112.8 | O(N^3) | DB: 4)
    * *Intent:* /// Returns `Some` if the visibility of the row changed after applying the filter and `None` /// oth...
  * `new` (Impact: 62.1 | O(2^N) | DB: 6)
  * `delete_filter` (Impact: 58.3 | O(2^N) | DB: 4)
  * `apply_changeset` (Impact: 55.7 | O(N^3) | DB: 6)
  * `fill_cells` (Impact: 51.3 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 157`, `args: 31`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 69`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `concurrency: 170`, `import: 22`
* *Defense:* `safety: 95`, `doc: 3`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::entities::filter_entities::*, RowMetaPB, Serialize, async_trait::async_trait, collab_database::template::timestamp_parse::TimestampCellData, crate::services::cell::CellCache, crate::services::field::TypeOptionCellExt, collab::lock::RwLock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.502 IQR)
- **Top Global Matches:** file_cluster_4: 12.502, file_cluster_13: 12.668, file_cluster_8: 12.761
- **Magnitude:** 630.44 | **LOC:** 576 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (78.3767%), Tech Debt (12.9174%)
**Top Internal Functions/Classes:**
  * `stream` (Impact: 203.6 | O(2^N) | DB: 3)
  * `get_documents_or_result` (Impact: 73.8 | O(N^4) | DB: 1)
  * `execute` (Impact: 52.4 | O(N^3) | DB: 7)
  * `get_question` (Impact: 23.9 | O(N^3) | DB: 1)
  * `build` (Impact: 22.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 160`, `args: 28`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `orphaned_logic: 3`
* *Architecture:* `api: 23`, `concurrency: 127`, `import: 26`
* *Defense:* `safety: 112`, `doc: 2`, `sync_locks: 14`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sync::Arc, Serialize, crate::SqliteVectorStore, async_trait::async_trait, FlowyResult, futures_util::StreamExt, StuffQAPromptBuilder, serde_json::Value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.989 IQR)
- **Top Global Matches:** file_cluster_4: 12.989, file_cluster_13: 13.0, file_cluster_8: 13.135
- **Magnitude:** 596.04 | **LOC:** 1227 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (51.1135%), Tech Debt (62.5854%)
**Top Internal Functions/Classes:**
  * `open_database` (Impact: 108.3 | O(N^4) | DB: 2)
  * `open_database_with_retry` (Impact: 38.8 | O(N^3))
  * `flush_collabs` (Impact: 33.0 | O(N^3))
    * *Intent:* #[instrument(level = "debug", skip_all)]
  * `initialize` (Impact: 29.4 | O(N^2) | DB: 1)
    * *Intent:* /// When initialize with new workspace, all the resources will be cleared.
  * `load_collab` (Impact: 22.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 179`, `args: 58`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`, `planned_debt: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 20`, `concurrency: 121`, `import: 38`
* *Defense:* `safety: 129`, `doc: 9`, `sync_locks: 24`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib_infra::priority_task::TaskDispatcher, RowMetaPB, TranslateRowContent, DatabaseMeta, async_trait::async_trait, collab_database::rows::RowId, crate::services::share::csv::CSVFormat, DatabaseCollabPersistenceService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-server/src/af_cloud/impls/user/cloud_service_impl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.204 IQR)
- **Top Global Matches:** file_cluster_8: 12.204, file_cluster_4: 12.38, file_cluster_13: 12.439
- **Magnitude:** 584.32 | **LOC:** 693 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (46.781%), Tech Debt (82.1386%)
**Top Internal Functions/Classes:**
  * `patch_workspace` (Impact: 22.9 | O(2^N))
  * `get_user_profile` (Impact: 21.5 | O(N^1) | DB: 2)
  * `create_workspace` (Impact: 16.1 | O(2^N))
  * `update_workspace_member` (Impact: 15.3 | O(2^N))
  * `batch_create_collab_object` (Impact: 14.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 211`, `args: 55`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 25`
* *Architecture:* `api: 4`, `concurrency: 99`, `import: 25`
* *Defense:* `safety: 104`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UserUpdateReceiver, tracing::instrument, AFWorkspaceSettingsChange, QueryWorkspaceParam, FlowyResult, PatchWorkspaceParam, AFWorkspaceInvitation, crate::af_cloud::impls::user::dto::
  af_update_from_update_params...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.079 IQR)
- **Top Global Matches:** file_cluster_4: 12.079, file_cluster_0: 12.927, file_cluster_13: 12.977
- **Magnitude:** 576.66 | **LOC:** 418 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (75.6944%), Tech Debt (48.2646%)
**Top Internal Functions/Classes:**
  * `next_chunk` (Impact: 19.2 | O(N^2) | DB: 4)
    * *Intent:* /// Read the next chunk from the file.
  * `from_file` (Impact: 13.1 | O(N^2) | DB: 3)
    * *Intent:* /// Create a `ChunkedBytes` instance from a file.
  * `test_file_slightly_larger_than_chunk_siz` (Impact: 8.5 | O(2^N) | DB: 10)
  * `set_offset` (Impact: 8.3 | O(N^2) | DB: 1)
    * *Intent:* /// Set the offset for the next chunk to be read.
  * `test_exact_multiple_chunk_file` (Impact: 8.3 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 193`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 70`, `orphaned_logic: 7`
* *Architecture:* `io: 22`, `api: 9`, `concurrency: 377`, `import: 11`
* *Defense:* `safety: 31`, `doc: 7`, `test: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, std::path::Path, tokio::io::AsyncWriteExt, tokio::io::SeekFrom, std::fmt::Display, tokio::io::AsyncReadExt, tokio::fs::File, anyhow::anyhow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/app_life_cycle.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.071 IQR)
- **Top Global Matches:** file_cluster_8: 11.071, file_cluster_13: 11.251, file_cluster_4: 11.427
- **Magnitude:** 575.04 | **LOC:** 537 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (31.3408%), Tech Debt (25.9664%)
**Top Internal Functions/Classes:**
  * `on_launch_if_authenticated` (Impact: 148.2 | O(2^N))
  * `on_workspace_opened` (Impact: 81.6 | O(2^N))
  * `on_sign_in` (Impact: 77.2 | O(2^N))
  * `on_sign_up` (Impact: 43.2 | O(N^1))
  * `folder_init_data_source` (Impact: 19.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 112`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 23`, `concurrency: 62`, `import: 29`
* *Defense:* `safety: 61`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_user::services::entities::UserConfig, flowy_search_pub::tantivy_state_init::close_document_tantivy_state, FolderManager, flowy_user::event_map::AppLifeCycle, UserPaths, FlowyResult, client_api::entity::billing_dto::SubscriptionPlan, flowy_ai::ai_manager::AIManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.935 IQR)
- **Top Global Matches:** file_cluster_0: 11.935, file_cluster_16: 11.954, file_cluster_8: 11.973
- **Magnitude:** 517.48 | **LOC:** 603 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (58.3456%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `read_favorites_handler` (Impact: 11.2 | O(N^2) | DB: 1)
  * `create_view_handler` (Impact: 10.7 | O(N^1))
  * `create_orphan_view_handler` (Impact: 10.7 | O(N^1))
  * `update_recent_views_handler` (Impact: 8.7 | O(N^1))
  * `set_default_publish_view_handler` (Impact: 8.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 197`, `args: 56`, `func_start: 50`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 49`
* *Architecture:* `api: 49`, `concurrency: 112`, `import: 10`
* *Defense:* `safety: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AFPluginState, crate::entities::*, crate::share::ImportParams, data_result_ok, tracing::instrument, crate::manager::FolderManager, lib_dispatch::prelude::AFPluginData, std::sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/filter/entities.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.182 IQR)
- **Top Global Matches:** file_cluster_13: 12.182, file_cluster_16: 12.323, file_cluster_8: 12.326
- **Magnitude:** 486.58 | **LOC:** 527 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (9.2277%), Tech Debt (12.4567%)
**Top Internal Functions/Classes:**
  * `from` (Impact: 194.7 | O(2^N) | DB: 2)
  * `find_parent_of_filter` (Impact: 42.6 | O(2^N) | DB: 3)
    * *Intent:* /// Recursively find the parent of a filter whose id is `filter_id`. Returns `None` if the filter //...
  * `find_filter` (Impact: 35.5 | O(2^N) | DB: 3)
    * *Intent:* /// Recursively find a filter based on `filter_id`. Returns `None` if the filter cannot be found.
  * `try_from` (Impact: 25.7 | O(N^3))
  * `get_children` (Impact: 25.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 91`, `args: 21`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 46`, `doc: 27`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::entities::
  CheckboxFilterPB, collab_database::rows::RowId, TimeFilterPB, collab_database::views::FilterMap, FlowyResult, std::mem, SelectOptionFilterPB, lib_infra::box_any::BoxAny...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-document/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.979 IQR)
- **Top Global Matches:** file_cluster_4: 12.979, file_cluster_13: 13.02, file_cluster_0: 13.209
- **Magnitude:** 468.28 | **LOC:** 526 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (43.1585%), Tech Debt (69.0822%)
**Top Internal Functions/Classes:**
  * `create_document_instance` (Impact: 46.7 | O(N^2) | DB: 4)
    * *Intent:* /// Returns Document for given object id /// If the document does not exist in local disk, try get t...
  * `collab_for_document` (Impact: 29.0 | O(N^2))
  * `create_document` (Impact: 27.3 | O(N^2))
    * *Intent:* /// Create a new document. /// /// if the document already exists, return the existing document. ///...
  * `is_doc_exist` (Impact: 18.8 | O(N^2))
  * `get_encoded_collab_with_view_id` (Impact: 16.4 | O(N^2))
    * *Intent:* /// Get the encoded collab of the document.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 149`, `args: 47`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`, `dead_code: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 26`, `concurrency: 91`, `import: 29`
* *Defense:* `safety: 100`, `doc: 14`, `sync_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collab::entity::EncodedCollab, FlowyResult, tracing::info, collab::preclude::Collab, subscribe_document_snapshot_state, collab::lock::RwLock, lib_infra::util::timestamp, collab_integrate::collab_builder::
  AppFlowyCollabBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `frontend/rust-lib/build-tool/flowy-ast/src/ctxt.rs` (RUST) | Magnitude: 37.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, safety: 9, state_mutation: 9, api: 8
- `frontend/rust-lib/flowy-ai/src/local_ai/controller.rs` (RUST) | Magnitude: 341.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 389, structural_boundaries: 105, safety: 70, branch: 58
- `frontend/appflowy_flutter/packages/flowy_infra_ui/flowy_infra_ui_platform_interface/lib/src/method_channel_flowy_infra_ui.dart` (DART) | Magnitude: 18.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, immutability_locks: 8, encapsulation: 6
- `frontend/rust-lib/flowy-database2/src/entities/type_option_entities/select_option_entities.rs` (RUST) | Magnitude: 105.3 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 187, generics: 42, api: 38, encapsulation: 38
- `frontend/rust-lib/flowy-error/src/impl_from/collab.rs` (RUST) | Magnitude: 11.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, decorators: 6, generics: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frontend/rust-lib/flowy-database2/src/services/field_settings/field_settings_builder.rs` (RUST) | Magnitude: 45.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 18, args: 9, api: 9
- `frontend/rust-lib/flowy-user-pub/src/cloud.rs` (RUST) | Magnitude: 72.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 177, safety: 61, doc: 58, args: 44
- `frontend/rust-lib/flowy-core/src/deps_resolve/folder_deps/folder_deps_chat_impl.rs` (RUST) | Magnitude: 52.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 18, safety: 17, concurrency: 15
- `frontend/rust-lib/flowy-user/src/entities/parser/user_password.rs` (RUST) | Magnitude: 30.24 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, branch: 11, safety: 9
- `frontend/rust-lib/flowy-database2/src/services/field/type_options/checklist_type_option/checklist_type_option.rs` (RUST) | Magnitude: 71.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 43, safety: 20, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `frontend/rust-lib/lib-dispatch/src/service/service.rs` (RUST) | Magnitude: 27.04 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 16, api: 9, encapsulation: 8
- `frontend/rust-lib/flowy-database2/src/services/database_view/view_operation.rs` (RUST) | Magnitude: 150.49 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, concurrency: 41, args: 39, func_start: 39
- `frontend/rust-lib/flowy-user/src/services/cloud_config.rs` (RUST) | Magnitude: 22.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, generics: 10, safety: 9
- `frontend/rust-lib/flowy-folder/src/entities/parser/workspace/workspace_id.rs` (RUST) | Magnitude: 11.52 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, api: 5, safety: 3
- `frontend/rust-lib/lib-dispatch/src/errors/errors.rs` (RUST) | Magnitude: 67.1 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 28, generics: 23, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frontend/rust-lib/build-tool/flowy-derive/src/node/mod.rs` (RUST) | Magnitude: 201.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 91, state_mutation: 37, safety: 34
- `frontend/rust-lib/build-tool/flowy-codegen/src/ts_event/mod.rs` (RUST) | Magnitude: 50.36 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 51, args: 17, state_mutation: 15
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart` (DART) | Magnitude: 180.28 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 316, func_start: 69, branch: 67, safety: 60
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/mask.dart` (DART) | Magnitude: 42.5 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, func_start: 21, structural_boundaries: 16, state_mutation: 15
- `frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/mod.rs` (RUST) | Magnitude: 175.98 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 233, structural_boundaries: 69, branch: 29, safety_bypasses: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/popover.dart` (DART) | Magnitude: 329.08 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 422, func_start: 121, branch: 83, ui_framework: 64
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/appflowy_theme.dart` (DART) | Magnitude: 51.98 | Delta: **0.151 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 101, func_start: 33, structural_boundaries: 18, doc: 18
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/default_emoji_picker_view.dart` (DART) | Magnitude: 144.12 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 250, func_start: 49, ui_framework: 46, encapsulation: 38
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/button/base_button/base_button.dart` (DART) | Magnitude: 88.9 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 130, ui_framework: 30, func_start: 24, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `frontend/rust-lib/flowy-core/src/indexed_data_consumer.rs` (RUST) | Magnitude: 325.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 96, safety: 71, concurrency: 55
- `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST) | Magnitude: 596.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 564, structural_boundaries: 179, safety: 129, concurrency: 121
- `frontend/rust-lib/flowy-search/src/services/manager.rs` (RUST) | Magnitude: 203.28 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 64, concurrency: 38, safety: 29
- `frontend/rust-lib/flowy-document/src/manager.rs` (RUST) | Magnitude: 468.28 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 149, safety: 100, concurrency: 91
- `frontend/rust-lib/flowy-ai/src/mcp/manager.rs` (RUST) | Magnitude: 40.88 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 17, concurrency: 12, safety: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `frontend/rust-lib/flowy-database2/src/entities/group_entities/configuration.rs` (RUST) | Magnitude: 42.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 19, decorators: 19, api: 12
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/focus/auto_unfocus_overlay.dart` (DART) | Magnitude: 9.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, func_start: 5, structural_boundaries: 4, ui_framework: 4
- `frontend/rust-lib/flowy-ai/src/chat.rs` (RUST) | Magnitude: 675.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 552, structural_boundaries: 146, concurrency: 101, safety: 86
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/option_overlay.dart` (DART) | Magnitude: 64.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 82, func_start: 19, safety: 17, branch: 16
- `frontend/rust-lib/flowy-ai-pub/src/persistence/collab_sql.rs` (RUST) | Magnitude: 55.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 13, api: 9, encapsulation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `frontend/rust-lib/build-tool/flowy-derive/src/dart_event/mod.rs` (RUST) | Magnitude: 3.18 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 10, safety: 2, structural_boundaries: 1, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 30.0611%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emji_picker_config.dart` -> **Severity: 124.5** (Blast Radius: 1.779 * Doc Risk: 69.9834%)
- `frontend/appflowy_flutter/lib/plugins/trash/src/sizes.dart` -> **Severity: 86.635** (Blast Radius: 1.557 * Doc Risk: 55.6425%)
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart` -> **Severity: 69.343** (Blast Radius: 1.557 * Doc Risk: 44.5364%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/menu/section.dart` -> **Severity: 68.267** (Blast Radius: 0.74 * Doc Risk: 92.2528%)
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/default_emoji_picker_view.dart` -> **Severity: 63.735** (Blast Radius: 1.334 * Doc Risk: 47.7775%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
