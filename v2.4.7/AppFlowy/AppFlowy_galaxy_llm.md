# ARCHITECTURAL_BRIEF: AppFlowy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/AppFlowy` |
| **Timestamp** | `2026-08-07T03:29:19.150520+00:00` |
| **Scan Duration** | `3.6s` |
| **Git Branch** | `main` |
| **Git Commit** | `4af02cdc87468be10ab15dbb4afd27fbf53ce89b` |
| **Git Remote** | `https://github.com/AppFlowy-IO/AppFlowy` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 792 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `6.049`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1195 | 70.1% |
| file_cluster_13 | 249 | 14.6% |
| file_cluster_0 | 78 | 4.6% |
| file_cluster_4 | 52 | 3.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 12.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.4 | 9.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.1 | 0.2 | 0.2 |
| API Exposure | 0.0 | 19.3 | 1.9 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 46.5 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 63.1 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.3 | 6.2 | 6.2 |
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

- `generate_import_data` (@ `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) -> Impact: **260.1** | LOC: 1042
  * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as follows: /// root folder: /// - cache.db /// - log...
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/shadcn/_mouse_area.dart`) -> Impact: **151.0** | LOC: 456
- `import` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`) -> Impact: **149.2** | LOC: 247
- `import` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`) -> Impact: **149.2** | LOC: 247
- `import` (@ `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/layout.dart`) -> Impact: **123.9** | LOC: 226
- `duplicate_view_with_parent_id` (@ `frontend/rust-lib/flowy-folder/src/manager.rs`) -> Impact: **119.7** | LOC: 173
- `createState` (@ `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/popover.dart`) -> Impact: **108.4** | LOC: 357
- `init_with_callback` (@ `frontend/rust-lib/flowy-user/src/user_manager/manager.rs`) -> Impact: **107.5** | LOC: 182
  * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This function /// will be invoked each time the user ope...
- `focusNode.dispose` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart`) -> Impact: **97.1** | LOC: 273
- `flatten_element_to_json` (@ `frontend/rust-lib/flowy-document/src/parser/external/utils.rs`) -> Impact: **94.1** | LOC: 273

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `frontend/appflowy_flutter` | 8 | 5080.06 | 4.34% | 0.0% |
| `frontend/resources/flowy_icons/16x` | 485 | 5007.0 | 4.9% | 0.0% |
| `frontend/rust-lib/flowy-sqlite` | 1 | 5000.0 | 0.0% | 0.0% |
| `frontend/rust-lib/flowy-database2/src/services/database` | 5 | 2465.2 | 41.46% | 49.36% |
| `frontend/rust-lib/flowy-ai/src` | 11 | 2140.2 | 36.83% | 59.0% |
| `frontend/rust-lib/flowy-folder/src` | 11 | 2003.06 | 20.99% | 49.5% |
| `frontend/rust-lib/flowy-database2/src` | 6 | 1681.68 | 19.42% | 52.91% |
| `frontend/rust-lib/flowy-user/src/user_manager` | 6 | 1672.02 | 27.81% | 44.44% |
| `frontend/resources/flowy_icons/24x` | 128 | 1346.56 | 5.0% | 0.0% |
| `frontend/rust-lib/flowy-storage/src` | 9 | 1254.46 | 32.24% | 67.49% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `frontend/appflowy_flutter/packages/appflowy_result/lib/src/result.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/linux/main.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/web/index.html` -> **100.0%** Exposure
- `frontend/rust-lib/build-tool/flowy-ast/src/symbol.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `frontend/appflowy_flutter/linux/my_application.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/flowy_infra_ui/linux/flowy_infra_u_i_plugin.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/flowy_infra_ui/linux/flowy_infra_ui_plugin.cc` -> **100.0%** Exposure
- `frontend/appflowy_flutter/windows/runner/main.cpp` -> **100.0%** Exposure
- `frontend/appflowy_flutter/windows/runner/utils.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` -> **56** Orphaned Functions | **26** Duplicates
- `frontend/rust-lib/flowy-database2/src/event_handler.rs` -> **72** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-user/src/event_handler.rs` -> **53** Orphaned Functions | **0** Duplicates
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` -> **1** Orphaned Functions | **51** Duplicates
- `frontend/rust-lib/flowy-folder/src/event_handler.rs` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`** -> AI Confidence: **99.32%**
2. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`** -> AI Confidence: **99.32%**
3. **`frontend/rust-lib/flowy-user/src/services/db.rs`** -> AI Confidence: **99.31%**
4. **`frontend/rust-lib/lib-infra/src/file_util.rs`** -> AI Confidence: **99.31%**
5. **`commitlint.config.js`** -> AI Confidence: **99.29%**
6. **`frontend/appflowy_flutter/macos/Podfile`** -> AI Confidence: **99.29%**
7. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart`** -> AI Confidence: **99.29%**
8. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_dialog.dart`** -> AI Confidence: **99.29%**
9. **`frontend/appflowy_flutter/packages/appflowy_backend/windows/include/appflowy_backend/app_flowy_backend_plugin.h`** -> AI Confidence: **99.29%**
10. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart`** -> AI Confidence: **99.25%**
11. **`frontend/rust-lib/build-tool/flowy-ast/src/event_attrs.rs`** -> AI Confidence: **99.24%**
12. **`frontend/rust-lib/flowy-ai/src/embeddings/context.rs`** -> AI Confidence: **99.24%**
13. **`frontend/rust-lib/flowy-ai/src/event_handler.rs`** -> AI Confidence: **99.24%**
14. **`frontend/rust-lib/flowy-core/src/app_life_cycle.rs`** -> AI Confidence: **99.24%**
15. **`frontend/rust-lib/flowy-database2/src/entities/filter_entities/util.rs`** -> AI Confidence: **99.24%**
16. **`frontend/rust-lib/flowy-database2/src/entities/type_option_entities/date_entities.rs`** -> AI Confidence: **99.24%**
17. **`frontend/rust-lib/flowy-database2/src/services/field/type_options/number_type_option/number_filter.rs`** -> AI Confidence: **99.24%**
18. **`frontend/rust-lib/flowy-database2/src/services/group/controller_impls/select_option_controller/util.rs`** -> AI Confidence: **99.24%**
19. **`frontend/rust-lib/flowy-document/src/parser/external/utils.rs`** -> AI Confidence: **99.24%**
20. **`frontend/rust-lib/flowy-document/src/parser/parser_entities.rs`** -> AI Confidence: **99.24%**
21. **`frontend/rust-lib/flowy-search-pub/src/tantivy_state.rs`** -> AI Confidence: **99.24%**
22. **`frontend/rust-lib/flowy-user-pub/src/sql/workspace_sql.rs`** -> AI Confidence: **99.24%**
23. **`frontend/rust-lib/flowy-user/src/event_handler.rs`** -> AI Confidence: **99.24%**
24. **`frontend/rust-lib/flowy-user/src/services/billing_check.rs`** -> AI Confidence: **99.24%**
25. **`frontend/rust-lib/flowy-user/src/user_manager/manager.rs`** -> AI Confidence: **99.24%**
26. **`frontend/rust-lib/flowy-user/src/user_manager/manager_user_encryption.rs`** -> AI Confidence: **99.24%**
27. **`frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs`** -> AI Confidence: **99.24%**
28. **`frontend/rust-lib/lib-dispatch/src/response/response.rs`** -> AI Confidence: **99.24%**
29. **`frontend/rust-lib/lib-log/src/layer.rs`** -> AI Confidence: **99.24%**
30. **`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/shadcn/_mouse_area.dart`** -> AI Confidence: **99.23%**
31. **`frontend/rust-lib/flowy-database2/src/entities/group_entities/group_changeset.rs`** -> AI Confidence: **99.23%**
32. **`frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/appflowy_popover.dart`** -> AI Confidence: **99.2%**
33. **`frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/mod.rs`** -> AI Confidence: **99.18%**
34. **`frontend/rust-lib/build-tool/flowy-codegen/src/protobuf_file/proto_gen.rs`** -> AI Confidence: **99.18%**
35. **`frontend/rust-lib/dart-ffi/src/appflowy_yaml.rs`** -> AI Confidence: **99.18%**
36. **`frontend/rust-lib/flowy-ai-pub/src/persistence/collab_metadata_sql.rs`** -> AI Confidence: **99.18%**
37. **`frontend/rust-lib/flowy-ai-pub/src/persistence/local_model_sql.rs`** -> AI Confidence: **99.18%**
38. **`frontend/rust-lib/flowy-ai/src/completion.rs`** -> AI Confidence: **99.18%**
39. **`frontend/rust-lib/flowy-ai/src/embeddings/store.rs`** -> AI Confidence: **99.18%**
40. **`frontend/rust-lib/flowy-ai/src/entities.rs`** -> AI Confidence: **99.18%**
41. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs`** -> AI Confidence: **99.18%**
42. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/mod.rs`** -> AI Confidence: **99.18%**
43. **`frontend/rust-lib/flowy-ai/src/local_ai/chat/retriever/sqlite_retriever.rs`** -> AI Confidence: **99.18%**
44. **`frontend/rust-lib/flowy-ai/src/local_ai/completion/chain.rs`** -> AI Confidence: **99.18%**
45. **`frontend/rust-lib/flowy-ai/src/local_ai/completion/stream_interpreter.rs`** -> AI Confidence: **99.18%**
46. **`frontend/rust-lib/flowy-ai/src/local_ai/request.rs`** -> AI Confidence: **99.18%**
47. **`frontend/rust-lib/flowy-ai/src/model_select.rs`** -> AI Confidence: **99.18%**
48. **`frontend/rust-lib/flowy-core/src/deps_resolve/chat_deps.rs`** -> AI Confidence: **99.18%**
49. **`frontend/rust-lib/flowy-core/src/deps_resolve/database_deps.rs`** -> AI Confidence: **99.18%**
50. **`frontend/rust-lib/flowy-core/src/deps_resolve/file_storage_deps.rs`** -> AI Confidence: **99.18%**
51. **`frontend/rust-lib/flowy-core/src/deps_resolve/folder_deps/folder_deps_chat_impl.rs`** -> AI Confidence: **99.18%**
52. **`frontend/rust-lib/flowy-core/src/deps_resolve/reminder_deps.rs`** -> AI Confidence: **99.18%**
53. **`frontend/rust-lib/flowy-core/src/deps_resolve/user_deps.rs`** -> AI Confidence: **99.18%**
54. **`frontend/rust-lib/flowy-core/src/indexing_data_runner.rs`** -> AI Confidence: **99.18%**
55. **`frontend/rust-lib/flowy-core/src/server_layer.rs`** -> AI Confidence: **99.18%**
56. **`frontend/rust-lib/flowy-database2/src/entities/calendar_entities.rs`** -> AI Confidence: **99.18%**
57. **`frontend/rust-lib/flowy-database2/src/entities/cell_entities.rs`** -> AI Confidence: **99.18%**
58. **`frontend/rust-lib/flowy-database2/src/entities/database_entities.rs`** -> AI Confidence: **99.18%**
59. **`frontend/rust-lib/flowy-database2/src/entities/filter_entities/date_filter.rs`** -> AI Confidence: **99.18%**
60. **`frontend/rust-lib/flowy-database2/src/entities/group_entities/group.rs`** -> AI Confidence: **99.18%**
61. **`frontend/rust-lib/flowy-database2/src/entities/setting_entities.rs`** -> AI Confidence: **99.18%**
62. **`frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`** -> AI Confidence: **99.18%**
63. **`frontend/rust-lib/flowy-database2/src/services/database/database_observe.rs`** -> AI Confidence: **99.18%**
64. **`frontend/rust-lib/flowy-database2/src/services/database/util.rs`** -> AI Confidence: **99.18%**
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
79. **`frontend/rust-lib/flowy-database2/src/services/group/controller_impls/checkbox_controller.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7258` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `frontend/rust-lib/lib-infra/src/ref_map.rs` (RUST) -> Cumulative Risk: **617.6**
- **Archetype:** `file_cluster_4` (Distance: 11.762 IQR)
- **Magnitude:** 72.38 | **LOC:** 93 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.9961%), Cognitive Load (96.4846%)
- **Heaviest Functions:** `remove` (Impact: 9.5), `insert` (Impact: 6.4), `new` (Impact: 2.3)

### 2. `frontend/rust-lib/lib-infra/src/priority_task/scheduler.rs` (RUST) -> Cumulative Risk: **612.54**
- **Archetype:** `file_cluster_4` (Distance: 12.592 IQR)
- **Magnitude:** 206.18 | **LOC:** 215 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `process_next_task` (Impact: 22.0), `run` (Impact: 13.2), `run` (Impact: 4.5)

### 3. `frontend/rust-lib/lib-infra/src/wasm/future.rs` (RUST) -> Cumulative Risk: **599.18**
- **Archetype:** `file_cluster_4` (Distance: 12.155 IQR)
- **Magnitude:** 44.22 | **LOC:** 66 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9729%)
- **Heaviest Functions:** `new` (Impact: 2.4), `poll` (Impact: 2.0), `poll` (Impact: 1.9)

### 4. `frontend/rust-lib/flowy-database2/src/services/database_view/views.rs` (RUST) -> Cumulative Risk: **591.34**
- **Archetype:** `file_cluster_4` (Distance: 13.203 IQR)
- **Magnitude:** 90.44 | **LOC:** 92 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.4995%)
- **Heaviest Functions:** `get_or_init_view_editor` (Impact: 9.4), `remove_view` (Impact: 3.8), `new` (Impact: 3.1)

### 5. `frontend/rust-lib/flowy-ai/src/mcp/manager.rs` (RUST) -> Cumulative Risk: **580.4**
- **Archetype:** `file_cluster_4` (Distance: 12.828 IQR)
- **Magnitude:** 37.48 | **LOC:** 40 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.821%)
- **Heaviest Functions:** `connect_server` (Impact: 5.5), `remove_server` (Impact: 5.5), `tool_list` (Impact: 3.8)

### 6. `frontend/rust-lib/flowy-database2/src/services/field/field_operation.rs` (RUST) -> Cumulative Risk: **578.58**
- **Archetype:** `file_cluster_4` (Distance: 13.072 IQR)
- **Magnitude:** 75.44 | **LOC:** 49 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9689%)
- **Heaviest Functions:** `edit_field_type_option` (Impact: 12.4), `edit_single_select_type_option` (Impact: 2.6), `edit_multi_select_type_option` (Impact: 2.6)

### 7. `frontend/rust-lib/lib-dispatch/src/util/ready.rs` (RUST) -> Cumulative Risk: **574.54**
- **Archetype:** `file_cluster_4` (Distance: 11.634 IQR)
- **Magnitude:** 28.82 | **LOC:** 33 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `into_inner` (Impact: 2.2), `ready` (Impact: 2.1), `poll` (Impact: 2.0)

### 8. `frontend/rust-lib/lib-infra/src/stream_util.rs` (RUST) -> Cumulative Risk: **567.1**
- **Archetype:** `file_cluster_13` (Distance: 12.029 IQR)
- **Magnitude:** 16.78 | **LOC:** 22 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.9673%), Cognitive Load (99.1752%)
- **Heaviest Functions:** `mpsc_channel_stream` (Impact: 2.5), `poll_next` (Impact: 1.9)

### 9. `frontend/rust-lib/flowy-document/src/event_handler.rs` (RUST) -> Cumulative Risk: **566.6**
- **Archetype:** `file_cluster_4` (Distance: 14.02 IQR)
- **Magnitude:** 380.66 | **LOC:** 506 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9323%), Verification (80.0%)
- **Heaviest Functions:** `convert_document_handler` (Impact: 17.6), `open_document_handler` (Impact: 12.7), `apply_action_handler` (Impact: 10.7)

### 10. `frontend/rust-lib/lib-infra/src/native/future.rs` (RUST) -> Cumulative Risk: **566.23**
- **Archetype:** `file_cluster_4` (Distance: 11.67 IQR)
- **Magnitude:** 51.2 | **LOC:** 36 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (76.8525%)
- **Heaviest Functions:** `poll` (Impact: 1.9), `to_fut` (Impact: 1.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `frontend/appflowy_flutter/dsa_pub.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_4` (Drift: 13.25 IQR)
- **Top Global Matches:** file_cluster_4: 13.25, file_cluster_8: 13.663, file_cluster_13: 13.683
- **Magnitude:** 2094.1 | **LOC:** 2465 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.3647%), Tech Debt (99.7973%)
**Top Internal Functions/Classes:**
  * `async_load_rows` (Impact: 56.7)
  * `open_database_view` (Impact: 40.9)
  * `move_group_row` (Impact: 31.0)
  * `get_prompts_from_database` (Impact: 25.9)
  * `delete_select_options` (Impact: 25.8)
    * *Intent:* /// Insert the options into the field's type option and update the cell content with the new options...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 260`, `structural_boundaries: 715`, `args: 212`, `func_start: 129`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 150`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 26`, `orphaned_logic: 56`
* *Architecture:* `api: 84`, `concurrency: 885`, `import: 50`
* *Defense:* `safety: 347`, `doc: 20`, `test: 1`, `sync_locks: 19`, `immutability_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::services::calculations::Calculation, default_group_setting, collab_database::fields::media_type_option::MediaCellData, RowDetail, collab_database::entity::DatabaseView, pin_mut, select_type_option_from_field, FilterChangeset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.907 IQR)
- **Top Global Matches:** file_cluster_0: 11.907, file_cluster_4: 11.931, file_cluster_8: 11.936
- **Magnitude:** 1113.3 | **LOC:** 1451 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.9507%), Tech Debt (99.7998%)
**Top Internal Functions/Classes:**
  * `update_database_setting_handler` (Impact: 48.7)
  * `rename_media_cell_file_handler` (Impact: 25.8)
    * *Intent:* /// We use a custom handler to rename the media file, as the ordering /// of the files must be maint...
  * `update_field_type_option_handler` (Impact: 14.9)
  * `update_relation_cell_handler` (Impact: 14.2)
  * `get_primary_field_handler` (Impact: 13.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 462`, `args: 82`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 12`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `orphaned_logic: 72`
* *Architecture:* `api: 72`, `concurrency: 248`, `import: 15`
* *Defense:* `safety: 115`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_error::FlowyError, RowCover, crate::services::field::
  RelationCellChangeset, tokio::sync::oneshot, collab_database::fields::media_type_option::MediaCellData, type_option_data_from_pb, crate::manager::DatabaseManager, SelectOptionCellChangeset...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.788 IQR)
- **Top Global Matches:** file_cluster_4: 13.788, file_cluster_13: 13.932, file_cluster_0: 13.961
- **Magnitude:** 1111.86 | **LOC:** 2638 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.1143%), Tech Debt (60.5181%)
**Top Internal Functions/Classes:**
  * `duplicate_view_with_parent_id` (Impact: 119.7)
  * `initialize_after_sign_up` (Impact: 33.5)
    * *Intent:* /// Initialize the folder for the new user. /// Using the [DefaultFolderBuilder] to create the defau...
  * `publish_view` (Impact: 32.4)
  * `get_batch_publish_payload` (Impact: 29.1)
  * `get_shared_page_details` (Impact: 28.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 385`, `args: 112`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 102`, `dead_code: 5`, `planned_debt: 1`, `orphaned_logic: 26`
* *Architecture:* `api: 61`, `concurrency: 254`, `import: 36`
* *Defense:* `safety: 232`, `doc: 144`, `sync_locks: 41`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` select_all_workspace_shared_users, DuplicateViewParams, PublishDocumentPayload, collab_folder::hierarchy_builder::ParentChildViews, crate::publish_util::generate_publish_name, GatherEncodedCollab, std::fmt::Display, client_api::entity::workspace_dto::PublishInfoView...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.512 IQR)
- **Top Global Matches:** file_cluster_13: 12.512, file_cluster_8: 12.571, file_cluster_17: 12.641
- **Magnitude:** 734.34 | **LOC:** 1410 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.9905%), Tech Debt (20.008%)
**Top Internal Functions/Classes:**
  * `generate_import_data` (Impact: 260.1)
    * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as ...
  * `migrate_folder_views` (Impact: 63.6)
  * `replace_document_ref_ids` (Impact: 39.3)
  * `upload_collab_objects_data` (Impact: 30.7)
  * `gen_sv_and_doc_state` (Impact: 26.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 257`, `args: 74`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `state_mutation: 106`, `dead_code: 3`, `orphaned_logic: 12`
* *Architecture:* `api: 12`, `concurrency: 12`, `import: 39`
* *Defense:* `safety: 111`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StateVector, ReadTxn, collab_database::rows::database_row_document_id_from_row_id, flowy_error::FlowyError, Doc, collab_database::workspace_database::WorkspaceDatabase, std::ops::Deref, collab_plugins::local_storage::kv::KVTransactionDB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.502 IQR)
- **Top Global Matches:** file_cluster_4: 12.502, file_cluster_8: 12.575, file_cluster_13: 12.702
- **Magnitude:** 693.8 | **LOC:** 822 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2137%), Tech Debt (24.5883%)
**Top Internal Functions/Classes:**
  * `open_workspace` (Impact: 59.1)
  * `get_all_user_workspaces` (Impact: 34.4)
  * `get_workspace_settings` (Impact: 30.2)
  * `upload_collab_data` (Impact: 26.6)
  * `create_workspace` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 207`, `args: 37`, `func_start: 32`
* *Risk/State:* `state_mutation: 72`, `orphaned_logic: 10`
* *Architecture:* `api: 26`, `concurrency: 110`, `import: 19`
* *Defense:* `safety: 88`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UserWorkspace, UserCloudServiceProvider, UserNotification, flowy_user_pub::entities::
  AuthType, tracing::error, NaiveDateTime, UserWorkspacePB, std::str::FromStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.246 IQR)
- **Top Global Matches:** file_cluster_0: 12.246, file_cluster_8: 12.323, file_cluster_16: 12.338
- **Magnitude:** 670.04 | **LOC:** 865 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5865%), Tech Debt (98.6313%)
**Top Internal Functions/Classes:**
  * `set_cloud_config_handler` (Impact: 19.7)
  * `import_appflowy_data_folder_handler` (Impact: 13.3)
  * `get_user_workspace_handler` (Impact: 12.6)
  * `get_user_profile_handler` (Impact: 12.0)
  * `get_cloud_config_handler` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 238`, `args: 60`, `func_start: 57`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 53`
* *Architecture:* `api: 55`, `concurrency: 119`, `import: 17`
* *Defense:* `safety: 100`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UserNotification, std::sync::Weak, std::str::FromStr, flowy_user_pub::entities::*, uuid::Uuid, save_cloud_config, FlowyError, crate::services::data_import::prepare_import...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.256 IQR)
- **Top Global Matches:** file_cluster_13: 13.256, file_cluster_4: 13.33, file_cluster_0: 13.369
- **Magnitude:** 642.96 | **LOC:** 925 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.42%), Tech Debt (37.7242%)
**Top Internal Functions/Classes:**
  * `init_with_callback` (Impact: 107.5)
    * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This f...
  * `refresh_user_profile` (Impact: 27.6)
  * `continue_sign_up` (Impact: 24.8)
  * `sign_in` (Impact: 20.2)
    * *Intent:* /// Performs a user sign-in, initializing user awareness and sending relevant notifications. /// ///...
  * `new` (Impact: 18.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 201`, `args: 47`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 42`, `concurrency: 86`, `import: 38`
* *Defense:* `safety: 171`, `doc: 29`, `sync_locks: 9`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::migrations::migration::
  save_migration_record, UserLocalDataMigration, crate::services::authenticate_user::AuthenticateUser, Ordering, collab::lock::RwLock, AuthStatePB, std::str::FromStr, crate::services::collab_interact::DefaultCollabInteract...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.921 IQR)
- **Top Global Matches:** file_cluster_4: 12.921, file_cluster_8: 13.087, file_cluster_13: 13.141
- **Magnitude:** 606.7 | **LOC:** 892 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9922%), Tech Debt (54.3678%)
**Top Internal Functions/Classes:**
  * `start_upload` (Impact: 68.2)
  * `create_upload` (Impact: 41.0)
  * `complete_upload` (Impact: 40.2)
  * `new` (Impact: 23.9)
  * `query_file_state` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 229`, `args: 36`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 66`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 5`, `api: 15`, `concurrency: 153`, `import: 25`
* *Defense:* `safety: 159`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::broadcast, FileProgressReceiver, delete_upload_file, FileUploaderRunner, calculate_offsets, flowy_storage_pub::chunked_byte::ChunkedBytes, Signal, SinkExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/ai_manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.577 IQR)
- **Top Global Matches:** file_cluster_4: 12.577, file_cluster_8: 12.75, file_cluster_13: 12.762
- **Magnitude:** 558.5 | **LOC:** 814 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.8159%), Tech Debt (31.0481%)
**Top Internal Functions/Classes:**
  * `reload_with_workspace_id` (Impact: 26.7)
  * `sync_chat_documents` (Impact: 21.7)
  * `open_chat` (Impact: 18.4)
  * `toggle_local_ai` (Impact: 16.1)
  * `update_rag_ids` (Impact: 15.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 234`, `args: 42`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`, `orphaned_logic: 12`
* *Architecture:* `api: 36`, `concurrency: 170`, `import: 24`
* *Defense:* `safety: 137`, `doc: 15`, `sync_locks: 12`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tracing::error, crate::notification::ChatNotification, ChatSettings, crate::model_select::
  GLOBAL_ACTIVE_MODEL_KEY, std::str::FromStr, std::path::PathBuf, select_chat_metadata, FilePB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.079 IQR)
- **Top Global Matches:** file_cluster_4: 12.079, file_cluster_0: 12.927, file_cluster_13: 12.977
- **Magnitude:** 543.46 | **LOC:** 418 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6944%), Tech Debt (48.2646%)
**Top Internal Functions/Classes:**
  * `next_chunk` (Impact: 13.2)
    * *Intent:* /// Read the next chunk from the file.
  * `from_file` (Impact: 9.1)
    * *Intent:* /// Create a `ChunkedBytes` instance from a file.
  * `set_offset` (Impact: 5.7)
    * *Intent:* /// Set the offset for the next chunk to be read.
  * `test_chunked_bytes_large_file` (Impact: 5.0)
  * `test_file_slightly_larger_than_chunk_siz` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 193`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 70`, `orphaned_logic: 7`
* *Architecture:* `io: 22`, `api: 9`, `concurrency: 377`, `import: 11`
* *Defense:* `safety: 31`, `doc: 7`, `test: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` anyhow::anyhow, AsyncSeekExt, super::*, tokio::io::SeekFrom, tokio::io::self, tokio::io::AsyncWriteExt, tokio::fs::File, bytes::Bytes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.357 IQR)
- **Top Global Matches:** file_cluster_8: 12.357, file_cluster_0: 12.508, file_cluster_7: 13.019
- **Magnitude:** 523.06 | **LOC:** 538 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `TextStyle` (Impact: 46.1)
  * `TextStyle` (Impact: 46.1)
  * `TextStyle` (Impact: 46.1)
  * `TextStyle` (Impact: 46.1)
  * `TextStyle` (Impact: 46.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 50`, `args: 40`, `func_start: 84`, `class_start: 9`
* *Risk/State:* `duplicate_logic: 51`, `orphaned_logic: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 199`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` widgets.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.935 IQR)
- **Top Global Matches:** file_cluster_0: 11.935, file_cluster_16: 11.954, file_cluster_8: 11.973
- **Magnitude:** 514.08 | **LOC:** 603 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.4576%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `create_view_handler` (Impact: 10.7)
  * `create_orphan_view_handler` (Impact: 10.7)
  * `update_recent_views_handler` (Impact: 8.7)
  * `set_default_publish_view_handler` (Impact: 8.7)
  * `remove_user_from_shared_page_handler` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 197`, `args: 56`, `func_start: 50`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 49`
* *Architecture:* `api: 49`, `concurrency: 112`, `import: 10`
* *Defense:* `safety: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_error::FlowyError, uuid::Uuid, crate::manager::FolderManager, std::sync::Arc, DataResult, data_result_ok, lib_dispatch::prelude::AFPluginData, crate::share::ImportParams...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/filter/controller.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.968 IQR)
- **Top Global Matches:** file_cluster_4: 12.968, file_cluster_13: 13.265, file_cluster_8: 13.408
- **Magnitude:** 497.9 | **LOC:** 563 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.1842%), Tech Debt (52.5488%)
**Top Internal Functions/Classes:**
  * `filter_row` (Impact: 52.5)
    * *Intent:* /// Returns `Some` if the visibility of the row changed after applying the filter and `None` /// oth...
  * `apply_filter` (Impact: 45.0)
    * *Intent:* // Create a filter result cache if it doesn't exist
  * `apply_changeset` (Impact: 29.7)
  * `fill_cells` (Impact: 22.8)
  * `delete_filter` (Impact: 20.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 157`, `args: 38`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 65`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `concurrency: 170`, `import: 22`
* *Defense:* `safety: 95`, `doc: 3`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::services::database_view::DatabaseViewChanged, serde::Deserialize, tracing::error, collab::lock::RwLock, DatabaseViewChangedNotifier, std::str::FromStr, RowDetail, crate::services::field::TypeOptionCellExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.752 IQR)
- **Top Global Matches:** file_cluster_8: 11.752, file_cluster_13: 12.143, file_cluster_16: 12.203
- **Magnitude:** 493.6 | **LOC:** 919 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.92%), Tech Debt (13.3418%)
**Top Internal Functions/Classes:**
  * `upload_part` (Impact: 10.1)
  * `get_plugins` (Impact: 9.3)
  * `create_upload` (Impact: 9.2)
  * `complete_upload` (Impact: 9.2)
  * `generate_search_summary` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 149`, `args: 67`, `func_start: 65`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `concurrency: 121`, `import: 37`
* *Defense:* `safety: 94`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TranslateRowResponse, ModelList, CollabPluginProviderContext, flowy_ai_pub::cloud::
  AIModel, client_api::entity::PublishInfo, FolderSnapshot, ResponseFormat, crate::server_layer::ServerProvider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.995 IQR)
- **Top Global Matches:** file_cluster_13: 12.995, file_cluster_4: 12.996, file_cluster_8: 13.13
- **Magnitude:** 491.44 | **LOC:** 1227 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1122%), Tech Debt (68.0404%)
**Top Internal Functions/Classes:**
  * `open_database` (Impact: 48.6)
  * `build_collab` (Impact: 44.3)
    * *Intent:* // When the user opens the database from the left-side bar, it may fail because the workspace databa...
  * `open_database_with_retry` (Impact: 20.8)
  * `initialize` (Impact: 20.4)
    * *Intent:* /// When initialize with new workspace, all the resources will be cleared.
  * `get_collabs` (Impact: 16.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 179`, `args: 58`, `func_start: 32`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`, `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `api: 20`, `concurrency: 116`, `import: 38`
* *Defense:* `safety: 129`, `doc: 9`, `sync_locks: 24`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lib_infra::priority_task::TaskDispatcher, flowy_error::FlowyError, CollabType, EncodeCollabByOid, tracing::error, DatabaseCollabPersistenceService, collab_plugins::local_storage::kv::KVTransactionDB, collab::lock::RwLock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-server/src/af_cloud/impls/user/cloud_service_impl.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.202 IQR)
- **Top Global Matches:** file_cluster_8: 12.202, file_cluster_4: 12.378, file_cluster_13: 12.438
- **Magnitude:** 458.12 | **LOC:** 693 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.6079%), Tech Debt (82.1386%)
**Top Internal Functions/Classes:**
  * `get_user_profile` (Impact: 21.5)
  * `create_collab_object` (Impact: 12.2)
  * `user_sign_in_with_url` (Impact: 11.3)
  * `get_user_awareness_doc_state` (Impact: 10.6)
  * `generate_sign_in_url_with_email` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 211`, `args: 55`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 25`
* *Architecture:* `api: 4`, `concurrency: 99`, `import: 25`
* *Defense:* `safety: 104`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UpdateUserProfileParams, UserWorkspace, CollabType, from_af_workspace_member, flowy_user_pub::sql::select_user_workspace, QueryWorkspaceMember, AFServer, PatchWorkspaceParam...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-document/src/manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.961 IQR)
- **Top Global Matches:** file_cluster_4: 12.961, file_cluster_13: 13.006, file_cluster_0: 13.194
- **Magnitude:** 389.68 | **LOC:** 526 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.8719%), Tech Debt (87.0489%)
**Top Internal Functions/Classes:**
  * `create_document_instance` (Impact: 29.9)
    * *Intent:* /// Returns Document for given object id /// If the document does not exist in local disk, try get t...
  * `collab_for_document` (Impact: 19.8)
  * `create_document` (Impact: 18.7)
    * *Intent:* /// Create a new document. /// /// if the document already exists, return the existing document. ///...
  * `doc_state_from_document_data` (Impact: 13.1)
  * `is_doc_exist` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 149`, `args: 47`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`, `dead_code: 2`, `duplicate_logic: 2`, `orphaned_logic: 15`
* *Architecture:* `api: 26`, `concurrency: 91`, `import: 29`
* *Defense:* `safety: 100`, `doc: 14`, `sync_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::entities::
  DocumentSnapshotData, DocumentSnapshotMeta, DocumentSnapshotMetaPB, std::sync::Weak, collab_document::document_data::default_document_data, lib_infra::util::timestamp, collab::lock::RwLock, collab::core::origin::CollabOrigin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/chat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.919 IQR)
- **Top Global Matches:** file_cluster_8: 11.919, file_cluster_4: 11.93, file_cluster_13: 12.042
- **Magnitude:** 388.58 | **LOC:** 668 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.2855%), Tech Debt (30.9554%)
**Top Internal Functions/Classes:**
  * `stream_response` (Impact: 86.3)
  * `load_remote_chat_messages` (Impact: 30.7)
  * `get_question_id_from_answer_id` (Impact: 14.7)
  * `stream_chat_message` (Impact: 14.0)
  * `load_prev_chat_messages` (Impact: 13.4)
    * *Intent:* /// Load chat messages for a given `chat_id`. /// /// 1. When opening a chat: /// - Loads local chat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 146`, `args: 26`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 27`, `orphaned_logic: 10`
* *Architecture:* `api: 13`, `concurrency: 101`, `import: 18`
* *Defense:* `safety: 86`, `doc: 12`, `sync_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tracing::error, StreamExt, AtomicI64, crate::notification::ChatNotification, flowy_ai_pub::cloud::
  AIModel, std::path::PathBuf, ResponseFormat, std::sync::atomic::AtomicBool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-sqlite-vec/src/db.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.197 IQR)
- **Top Global Matches:** file_cluster_8: 12.197, file_cluster_13: 12.274, file_cluster_17: 12.321
- **Magnitude:** 388.0 | **LOC:** 639 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5268%), Tech Debt (17.543%)
**Top Internal Functions/Classes:**
  * `upsert_collabs_embeddings` (Impact: 52.9)
    * *Intent:* /// Inserts or replaces all of `fragments` for the given (workspace_id, object_id), /// deleting any...
  * `select_all_embedded_documents` (Impact: 37.7)
  * `select_all_embedded_content` (Impact: 26.9)
  * `select_collabs_fragment_ids` (Impact: 22.1)
  * `delete_pending_indexed_collab` (Impact: 17.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 146`, `args: 29`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `orphaned_logic: 5`
* *Architecture:* `api: 12`, `concurrency: 21`, `import: 14`
* *Defense:* `safety: 46`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::init_sqlite_vector_extension, tracing::trace, PendingIndexedCollab, flowy_ai_pub::entities::EmbeddedChunk, std::path::PathBuf, uuid::Uuid, HashSet, SqliteEmbeddedFragment...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-document/src/event_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.02 IQR)
- **Top Global Matches:** file_cluster_4: 14.02, file_cluster_13: 14.268, file_cluster_16: 14.322
- **Magnitude:** 380.66 | **LOC:** 506 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5614%), Tech Debt (99.9323%)
**Top Internal Functions/Classes:**
  * `convert_document_handler` (Impact: 17.6)
    * *Intent:* /// Handler for converting a document to a JSON string, HTML string, or plain text string. /// /// C...
  * `open_document_handler` (Impact: 12.7)
  * `apply_action_handler` (Impact: 10.7)
  * `create_document_handler` (Impact: 10.6)
  * `convert_data_to_document_internal` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 154`, `args: 38`, `func_start: 30`
* *Risk/State:* `state_mutation: 27`, `dead_code: 9`, `duplicate_logic: 7`, `orphaned_logic: 21`
* *Architecture:* `api: 22`, `concurrency: 101`, `import: 13`
* *Defense:* `safety: 21`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collab_document::blocks::
  BlockAction, flowy_error::FlowyError, crate::manager::DocumentManager, std::str::FromStr, BlockEvent, uuid::Uuid, BlockActionType, DataResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.574 IQR)
- **Top Global Matches:** file_cluster_4: 13.574, file_cluster_13: 13.763, file_cluster_16: 14.182
- **Magnitude:** 371.8 | **LOC:** 1345 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.8404%), Tech Debt (68.5397%)
**Top Internal Functions/Classes:**
  * `v_did_update_row` (Impact: 34.2)
    * *Intent:* /// Notify the view that the row has been updated. If the view has groups,
  * `v_did_create_row` (Impact: 19.3)
  * `v_will_create_row` (Impact: 14.0)
  * `v_did_delete_row` (Impact: 10.2)
  * `insert_row` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 126`, `args: 19`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`, `orphaned_logic: 10`
* *Architecture:* `api: 19`, `concurrency: 184`, `import: 30`
* *Defense:* `safety: 65`, `doc: 26`, `sync_locks: 5`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::services::calculations::Calculation, RowDetail, collab_database::entity::DatabaseView, UpdatedCells, crate::services::database_view::view_calculations::make_calculations_controller, FilterChangeset, database_view_setting_pb_from_view, RowId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/app_life_cycle.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.055 IQR)
- **Top Global Matches:** file_cluster_8: 11.055, file_cluster_13: 11.239, file_cluster_4: 11.414
- **Magnitude:** 354.84 | **LOC:** 537 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.8076%), Tech Debt (25.9664%)
**Top Internal Functions/Classes:**
  * `on_launch_if_authenticated` (Impact: 49.2)
  * `on_workspace_opened` (Impact: 42.6)
  * `on_sign_up` (Impact: 40.2)
  * `on_sign_in` (Impact: 37.6)
  * `folder_init_data_source` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 112`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 23`, `concurrency: 62`, `import: 29`
* *Defense:* `safety: 61`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_error::FlowyError, UserWorkspace, flowy_user::event_map::AppLifeCycle, tracing::error, flowy_document::manager::DocumentManager, collab_plugins::local_storage::kv::KVTransactionDB, UserCloudServiceProvider, flowy_user::services::entities::UserConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.492 IQR)
- **Top Global Matches:** file_cluster_4: 12.492, file_cluster_13: 12.658, file_cluster_8: 12.75
- **Magnitude:** 353.04 | **LOC:** 576 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.0562%), Tech Debt (12.9174%)
**Top Internal Functions/Classes:**
  * `stream` (Impact: 35.6)
  * `execute` (Impact: 28.4)
  * `get_documents_or_result` (Impact: 27.9)
  * `get_question` (Impact: 12.7)
  * `get_related_questions` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 160`, `args: 28`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`, `orphaned_logic: 3`
* *Architecture:* `api: 23`, `concurrency: 127`, `import: 26`
* *Defense:* `safety: 112`, `doc: 2`, `sync_locks: 14`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.576
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` flowy_error::FlowyError, serde::Deserialize, tracing::error, langchain_rust::memory::SimpleMemory, langchain_rust::prompt::FormatPrompter, json, StreamData, pin_mut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `frontend/rust-lib/build-tool/flowy-ast/src/ctxt.rs` (RUST) | Magnitude: 36.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, safety: 9, state_mutation: 9, api: 8
- `frontend/rust-lib/flowy-ai/src/local_ai/controller.rs` (RUST) | Magnitude: 245.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 389, structural_boundaries: 105, safety: 70, concurrency: 48
- `frontend/appflowy_flutter/packages/flowy_infra_ui/flowy_infra_ui_platform_interface/lib/src/method_channel_flowy_infra_ui.dart` (DART) | Magnitude: 20.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, immutability_locks: 8, encapsulation: 6
- `frontend/rust-lib/flowy-database2/src/entities/type_option_entities/select_option_entities.rs` (RUST) | Magnitude: 83.9 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 187, generics: 42, api: 38, encapsulation: 38
- `frontend/rust-lib/flowy-error/src/impl_from/collab.rs` (RUST) | Magnitude: 11.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, decorators: 6, generics: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST) | Magnitude: 491.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 564, structural_boundaries: 179, safety: 129, concurrency: 116
- `frontend/rust-lib/flowy-search/src/document/cloud_search_handler.rs` (RUST) | Magnitude: 60.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 42, safety: 34, import: 13
- `frontend/rust-lib/flowy-database2/src/services/field_settings/field_settings_builder.rs` (RUST) | Magnitude: 41.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 18, args: 9, api: 9
- `frontend/rust-lib/flowy-core/src/deps_resolve/folder_deps/folder_deps_chat_impl.rs` (RUST) | Magnitude: 52.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 18, safety: 17, concurrency: 15
- `frontend/rust-lib/flowy-user-pub/src/cloud.rs` (RUST) | Magnitude: 111.76 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 177, safety: 61, doc: 58, args: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `frontend/rust-lib/flowy-database2/src/services/database_view/view_operation.rs` (RUST) | Magnitude: 150.49 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, concurrency: 41, args: 39, func_start: 39
- `frontend/rust-lib/flowy-user/src/services/cloud_config.rs` (RUST) | Magnitude: 22.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, generics: 10, safety: 9
- `frontend/rust-lib/lib-dispatch/src/service/service.rs` (RUST) | Magnitude: 30.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 16, api: 10, encapsulation: 8
- `frontend/rust-lib/flowy-folder/src/entities/parser/workspace/workspace_id.rs` (RUST) | Magnitude: 11.52 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, api: 5, safety: 3
- `frontend/rust-lib/build-tool/flowy-ast/src/ty_ext.rs` (RUST) | Magnitude: 66.84 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 113, safety: 51, structural_boundaries: 36, generics: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frontend/rust-lib/build-tool/flowy-derive/src/node/mod.rs` (RUST) | Magnitude: 120.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 91, state_mutation: 37, safety: 34
- `frontend/rust-lib/build-tool/flowy-codegen/src/ts_event/mod.rs` (RUST) | Magnitude: 54.46 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 51, args: 17, state_mutation: 15
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/mask.dart` (DART) | Magnitude: 47.7 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 16, state_mutation: 13, closures: 12
- `frontend/rust-lib/build-tool/flowy-derive/src/proto_buf/serialize.rs` (RUST) | Magnitude: 105.2 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 185, safety: 56, structural_boundaries: 38, branch: 29
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart` (DART) | Magnitude: 294.88 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 316, branch: 67, safety: 60, func_start: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/popover.dart` (DART) | Magnitude: 326.88 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 422, branch: 83, ui_framework: 64, structural_boundaries: 62
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/appflowy_theme.dart` (DART) | Magnitude: 54.58 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 18, doc: 18, func_start: 17
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/default_emoji_picker_view.dart` (DART) | Magnitude: 136.62 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 250, ui_framework: 46, encapsulation: 38, structural_boundaries: 29
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/button/base_button/base_button.dart` (DART) | Magnitude: 85.4 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 130, ui_framework: 30, branch: 19, structural_boundaries: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `frontend/rust-lib/flowy-core/src/indexed_data_consumer.rs` (RUST) | Magnitude: 233.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 96, safety: 71, concurrency: 55
- `frontend/rust-lib/flowy-search/src/services/manager.rs` (RUST) | Magnitude: 100.48 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 64, concurrency: 38, safety: 29
- `frontend/rust-lib/flowy-document/src/manager.rs` (RUST) | Magnitude: 389.68 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 149, safety: 100, concurrency: 91
- `frontend/rust-lib/flowy-ai/src/mcp/manager.rs` (RUST) | Magnitude: 37.48 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 17, concurrency: 12, safety: 10
- `frontend/rust-lib/flowy-database2/src/services/group/action.rs` (RUST) | Magnitude: 77.8 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 78, doc: 76, concurrency: 35, generics: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `frontend/rust-lib/flowy-database2/src/entities/group_entities/configuration.rs` (RUST) | Magnitude: 40.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 19, decorators: 19, api: 12
- `frontend/appflowy_flutter/lib/startup/plugin/src/sandbox.dart` (DART) | Magnitude: 29.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 14, closures: 10, encapsulation: 10
- `frontend/rust-lib/flowy-ai-pub/src/persistence/collab_sql.rs` (RUST) | Magnitude: 45.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 13, api: 9, encapsulation: 9
- `frontend/rust-lib/flowy-database2/src/entities/filter_entities/number_filter.rs` (RUST) | Magnitude: 13.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, safety: 11, structural_boundaries: 9, decorators: 6
- `frontend/rust-lib/flowy-database2/src/entities/filter_entities/text_filter.rs` (RUST) | Magnitude: 13.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, safety: 11, structural_boundaries: 9, decorators: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `frontend/rust-lib/build-tool/flowy-derive/src/dart_event/mod.rs` (RUST) | Magnitude: 3.18 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 10, safety: 2, structural_boundaries: 1, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emji_picker_config.dart` -> **Severity: 92.394** (Blast Radius: 1.779 * Doc Risk: 51.9361%)
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart` -> **Severity: 77.635** (Blast Radius: 1.557 * Doc Risk: 49.8621%)
- `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/mutex.dart` -> **Severity: 64.991** (Blast Radius: 0.821 * Doc Risk: 79.1603%)
- `frontend/rust-lib/build-tool/flowy-ast/src/symbol.rs` -> **Severity: 57.6** (Blast Radius: 0.576 * Doc Risk: 99.9996%)
- `frontend/rust-lib/flowy-ai-pub/src/entities.rs` -> **Severity: 57.6** (Blast Radius: 0.576 * Doc Risk: 99.9997%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
