# ARCHITECTURAL_BRIEF: AppFlowy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AppFlowy-IO/AppFlowy` |
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
| Total Artifacts | 4597 |
| Analyzed Artifacts (Scanned) | 1799 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2798 |
| Total LOC | 102670 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 39.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7349 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5044 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 821 | 611 | 45.6% |
| RUST | 595 | 74282 | 33.1% |
| DART | 99 | 14839 | 5.5% |
| SQLITE | 65 | 267 | 3.6% |
| CPP | 54 | 2305 | 3.0% |
| PLAINTEXT | 36 | 2 | 2.0% |
| YAML | 34 | 510 | 1.9% |
| MARKDOWN | 26 | 0 | 1.4% |
| JSON | 18 | 8809 | 1.0% |
| SWIFT | 15 | 235 | 0.8% |
| RUBY | 11 | 384 | 0.6% |
| KOTLIN | 7 | 69 | 0.4% |
| GROOVY | 6 | 56 | 0.3% |
| OBJECTIVE-C | 4 | 4 | 0.2% |
| HTML | 3 | 169 | 0.2% |
| JAVA | 3 | 104 | 0.2% |
| JAVASCRIPT | 1 | 19 | 0.1% |
| MAKEFILE | 1 | 5 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1717 | 95.4% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 3.3% |
| Static: Minified & Vendor Opaque Mass | 20 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2798*

**Composition by Extension & Reason:**
- `.dart`: 1876x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 308 LOC)
- `.png`: 201x Excluded (Explicitly Denied Extension: '.png')
- `.rs`: 150x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 88x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded (Unsupported Extension: '.xcworkspacedata'), 11x Excluded (Unsupported Extension: '.entitlements')
- `.json`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Static Asset Blob without Intent: 1064 LOC), 2x Excluded (Massive Static Asset Blob: 3468 LOC)
- `.toml`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.toml')
- `.xcconfig`: 38x Excluded (Unsupported Extension: '.xcconfig')
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 25x Excluded (Explicitly Denied Extension: '.zip')
- `.sh`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 20x Excluded (Explicitly Denied Extension: '.ttf')
- `.yml`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 12.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 37.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 31.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4821 | 493 | 8 | `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` |
| cleanup | 122 | 56 | 0 | `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` |
| guards | 4278 | 455 | 6 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` |
| danger | 931 | 191 | 1 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/color_scheme/badge_color_scheme.dart` |
| concurrency | 5627 | 209 | 3 | `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` |
| connectivity | 6450 | 693 | 9 | `frontend/rust-lib/flowy-ai/src/entities.rs` |
| io | 296 | 72 | 0 | `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 13 | 9 | 0 | `frontend/rust-lib/event-integration-test/src/user_event.rs` |
| time | 38 | 34 | 0 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart` |
| serialization | 58 | 36 | 0 | `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` |
| regex | 28 | 15 | 0 | `frontend/appflowy_flutter/packages/flowy_svg/bin/flowy_svg.dart` |
| events | 1294 | 177 | 0 | `frontend/rust-lib/flowy-database2/src/event_handler.rs` |
| tests | 300 | 36 | 0 | `frontend/rust-lib/flowy-database2/src/services/field/type_options/text_type_option/text_filter.rs` |
| docs | 2393 | 222 | 1 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/data/appflowy_default/primitive.dart` |
| debt | 163 | 60 | 0 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` |
| mutation | 10871 | 561 | 16 | `frontend/rust-lib/flowy-folder/src/manager.rs` |
| dead_code | 3105 | 474 | 5 | `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/data/appflowy_default/primitive.dart` |
| credential | 0 | 0 | 0 | - |
| threat | 105 | 58 | 0 | `frontend/rust-lib/lib-dispatch/src/service/handler.rs` |
| ml_ai | 55 | 26 | 0 | `frontend/rust-lib/flowy-sqlite-vec/src/db.rs` |
| ui | 349 | 58 | 0 | `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (Hits: 22)
- `frontend/appflowy_flutter/packages/appflowy_backend/example/macos/Podfile` (Hits: 20)
- `frontend/appflowy_flutter/packages/flowy_svg/bin/flowy_svg.dart` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **appflowy_theme.dart** (`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/appflowy_theme.dart`) — 13 inbound connections
2. **component.dart** (`frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/component.dart`) — 9 inbound connections
3. **FlutterActivity.java** (`frontend/appflowy_flutter/packages/flowy_infra_ui/example/example/android/app/src/main/java/com/example/flowy_infra_ui_example/FlutterActivity.java`) — 5 inbound connections
4. **emoji_picker.dart** (`frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart`) — 4 inbound connections
5. **emoji_category_models.dart** (`frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/models/emoji_category_models.dart`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **manager.rs** (`frontend/rust-lib/flowy-folder/src/manager.rs`) — 113 outbound dependencies
2. **database_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs`) — 94 outbound dependencies
3. **view_editor.rs** (`frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs`) — 87 outbound dependencies
4. **cloud_service_impl.rs** (`frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs`) — 77 outbound dependencies
5. **appflowy_data_import.rs** (`frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) — 73 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `duplicate_view_with_parent_id` (@ `frontend/rust-lib/flowy-folder/src/manager.rs`) -> Impact: **113.3** | LOC: 173
  * *Intent:* /// Duplicate the view with the given view id and parent view id. /// /// If the view id is the same as the parent view id, it will return an error. /...
- `stream_response` (@ `frontend/rust-lib/flowy-ai/src/chat.rs`) -> Impact: **82.2** | LOC: 145
- `getPositionForChild` (@ `frontend/appflowy_flutter/packages/appflowy_popover/lib/src/layout.dart`) -> Impact: **79.9** | LOC: 143
- `_showOverlay` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_overlay.dart`) -> Impact: **79.9** | LOC: 72
- `init_with_callback` (@ `frontend/rust-lib/flowy-user/src/user_manager/manager.rs`) -> Impact: **71.1** | LOC: 182
  * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This function /// will be invoked each time the user ope...
- `getPositionForChild` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`) -> Impact: **69.5** | LOC: 108
- `getPositionForChild` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`) -> Impact: **69.5** | LOC: 108
- `generate_import_data` (@ `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs`) -> Impact: **64.8** | LOC: 255
  * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as follows: /// root folder: /// - cache.db /// - log...
- `getConstraintsForChild` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart`) -> Impact: **63.8** | LOC: 117
- `getConstraintsForChild` (@ `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/layout.dart`) -> Impact: **63.8** | LOC: 117

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `frontend/resources/flowy_icons/16x` | 495 | 5093.16 | 0.0% | 0.0% |
| `frontend/appflowy_flutter` | 8 | 5069.76 | 0.0% | 9.14% |
| `frontend/rust-lib/flowy-sqlite` | 1 | 5000.0 | 0.0% | 0.0% |
| `frontend/rust-lib/flowy-folder/src` | 11 | 2267.44 | 14.45% | 56.94% |
| `frontend/rust-lib/flowy-database2/src` | 6 | 1922.06 | 19.88% | 42.16% |
| `frontend/rust-lib/flowy-ai/src` | 11 | 1901.12 | 25.48% | 35.48% |
| `frontend/rust-lib/flowy-database2/src/services/database` | 5 | 1869.26 | 23.88% | 48.89% |
| `frontend/rust-lib/flowy-database2/src/services/database_view` | 10 | 1387.42 | 45.03% | 77.34% |
| `frontend/rust-lib/flowy-user/src/user_manager` | 6 | 1349.26 | 15.93% | 58.99% |
| `frontend/resources/flowy_icons/24x` | 128 | 1346.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/data/appflowy_default/primitive.dart` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-database2/src/services/database_view/view_operation.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-database2/src/services/group/action.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-server/src/server.rs` -> **100.0%** Exposure
- `frontend/rust-lib/flowy-user-pub/src/cloud.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/shadcn/_mouse_area.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/textfield/textfield.dart` -> **100.0%** Exposure
- `frontend/appflowy_flutter/packages/flowy_infra_ui/lib/src/flowy_overlay/flowy_popover_layout.dart` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/data/appflowy_default/primitive.dart` -> **214** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` -> **74** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-database2/src/event_handler.rs` -> **72** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs` -> **68** Orphaned Functions | **0** Duplicates
- `frontend/rust-lib/flowy-folder/src/manager.rs` -> **54** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7258` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `frontend/rust-lib/flowy-database2/src/services/group/controller_impls/checkbox_controller.rs` (RUST) -> Cumulative Risk: **700.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 95.82 | **LOC:** 163 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3145%), Concurrency (96.447%)
- **Heaviest Functions:** `add_or_remove_row_when_cell_changed` (Impact: 22.4), `delete_row` (Impact: 7.0), `can_group` (Impact: 6.5)

### 2. `frontend/rust-lib/lib-infra/src/priority_task/scheduler.rs` (RUST) -> Cumulative Risk: **679.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 127.98 | **LOC:** 215 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9955%), Concurrency (99.9888%)
- **Heaviest Functions:** `process_next_task` (Impact: 16.1), `run` (Impact: 9.7), `add_task` (Impact: 4.3)

### 3. `frontend/rust-lib/flowy-database2/src/services/group/controller_impls/url_controller.rs` (RUST) -> Cumulative Risk: **671.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 123.06 | **LOC:** 221 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (97.7472%), Concurrency (92.4634%)
- **Heaviest Functions:** `create_or_delete_group_when_cell_changed` (Impact: 19.9), `add_or_remove_row_when_cell_changed` (Impact: 13.3), `delete_row` (Impact: 11.5)

### 4. `frontend/rust-lib/flowy-database2/src/services/sort/controller.rs` (RUST) -> Cumulative Risk: **671.07**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 221.28 | **LOC:** 366 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9988%), Cognitive Load (90.2971%), Documentation (88.5714%)
- **Heaviest Functions:** `apply_changeset` (Impact: 22.0), `cmp_row` (Impact: 19.3), `did_create_row` (Impact: 10.0)

### 5. `frontend/rust-lib/lib-infra/src/ref_map.rs` (RUST) -> Cumulative Risk: **664.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 86.78 | **LOC:** 93 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.9062%)
- **Heaviest Functions:** `remove` (Impact: 9.5), `insert` (Impact: 6.4), `get` (Impact: 1.9)

### 6. `frontend/rust-lib/flowy-ai/src/mcp/manager.rs` (RUST) -> Cumulative Risk: **661.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 54.68 | **LOC:** 40 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `connect_server` (Impact: 5.5), `remove_server` (Impact: 5.5), `tool_list` (Impact: 3.8)

### 7. `frontend/rust-lib/flowy-database2/src/services/group/controller_impls/select_option_controller/multi_select_controller.rs` (RUST) -> Cumulative Risk: **645.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 87.12 | **LOC:** 180 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (98.5048%), Tech Debt (98.0358%)
- **Heaviest Functions:** `delete_group` (Impact: 11.2), `create_group` (Impact: 7.7), `update_type_option_when_update_group` (Impact: 7.2)

### 8. `frontend/rust-lib/flowy-database2/src/services/group/controller_impls/select_option_controller/single_select_controller.rs` (RUST) -> Cumulative Risk: **644.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 87.14 | **LOC:** 181 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (98.4539%), Tech Debt (97.9556%)
- **Heaviest Functions:** `delete_group` (Impact: 11.2), `create_group` (Impact: 7.7), `update_type_option_when_update_group` (Impact: 7.2)

### 9. `frontend/rust-lib/flowy-database2/src/services/filter/controller.rs` (RUST) -> Cumulative Risk: **640.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 331.16 | **LOC:** 563 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.7413%), Documentation (93.9394%), Verification (80.0%)
- **Heaviest Functions:** `apply_filter` (Impact: 41.4), `apply_changeset` (Impact: 29.7), `fill_cells` (Impact: 22.8)

### 10. `frontend/rust-lib/flowy-storage/src/uploader.rs` (RUST) -> Cumulative Risk: **639.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 209.06 | **LOC:** 381 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9674%), Cognitive Load (82.6971%)
- **Heaviest Functions:** `process_next` (Impact: 25.8), `run` (Impact: 17.6), `remove_task` (Impact: 14.3)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/database/database_editor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1624.26 | **LOC:** 2465 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7697%), Tech Debt (93.9993%)
**Top Internal Functions/Classes:**
  * `async_load_rows` (Impact: 53.4)
  * `open_database_view` (Impact: 37.1)
    * *Intent:* /// Open database view /// When opening database view, it will load database rows from remote if the...
  * `move_group_row` (Impact: 29.2)
  * `delete_select_options` (Impact: 24.0)
  * `init_database_row` (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 532
* *Memory Alloc (weighted view):* 17
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 723`, `args: 218`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 74`
* *Architecture:* `api: 85`, `concurrency: 422`, `import: 50`
* *Defense:* `safety: 79`, `doc: 20`, `test: 2`, `sync_locks: 19`, `immutability_locks: 1`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CSVFormat, Cells, CollabBuilderConfig, DatabaseRow, DatabaseViewEditor, DatabaseViewOperation, DatabaseViews, EditorByViewId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1450.04 | **LOC:** 2638 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.011%), Tech Debt (78.4145%)
**Top Internal Functions/Classes:**
  * `duplicate_view_with_parent_id` (Impact: 113.3)
    * *Intent:* /// Duplicate the view with the given view id and parent view id. /// /// If the view id is the same...
  * `move_view` (Impact: 31.6)
    * *Intent:* /// Move the view with given id from one position to another position. /// The view will be moved to...
  * `initialize_after_sign_up` (Impact: 31.5)
    * *Intent:* /// Initialize the folder for the new user. /// Using the [DefaultFolderBuilder] to create the defau...
  * `publish_view` (Impact: 29.8)
    * *Intent:* /// Publishes a view identified by the given `view_id`. /// /// If `publish_name` is `None`, a defau...
  * `create_view_with_params` (Impact: 28.6)
    * *Intent:* /// Asynchronously creates a view with provided parameters and notifies the workspace if update is n...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 269
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 639`, `args: 192`, `func_start: 103`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 29`, `dead_code: 5`, `planned_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `api: 89`, `concurrency: 219`, `import: 36`
* *Defense:* `safety: 113`, `doc: 144`, `sync_locks: 88`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AFRole, AFRolePB, CollabBuilderConfig, CollabPersistenceImpl, CreateViewParams, DeletedViewPB, DuplicateViewParams, EncodedCollab...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1001.3 | **LOC:** 1451 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2537%), Tech Debt (99.7998%)
**Top Internal Functions/Classes:**
  * `update_database_setting_handler` (Impact: 42.5)
  * `rename_media_cell_file_handler` (Impact: 22.9)
    * *Intent:* /// We use a custom handler to rename the media file, as the ordering /// of the files must be maint...
  * `update_field_type_option_handler` (Impact: 13.1)
  * `update_relation_cell_handler` (Impact: 12.6)
  * `get_primary_field_handler` (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 462`, `args: 82`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 3`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 72`
* *Architecture:* `api: 72`, `concurrency: 223`, `import: 15`
* *Defense:* `safety: 21`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AFPluginState, DataResult, FlowyResult, RowCover, RowId, SelectOptionCellChangeset, TypeOptionCellExt, Weak...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/database_view/view_editor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 874.78 | **LOC:** 1345 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.102%), Tech Debt (80.9957%)
**Top Internal Functions/Classes:**
  * `v_did_update_row` (Impact: 34.4)
    * *Intent:* /// Notify the view that the row has been updated. If the view has groups, /// send the group notifi...
  * `v_did_create_row` (Impact: 18.2)
  * `v_set_layout_settings` (Impact: 16.5)
    * *Intent:* /// Update the layout settings and send the notification to refresh the UI
  * `v_get_layout_settings` (Impact: 15.9)
    * *Intent:* /// Returns the current calendar settings
  * `v_delete_group` (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 334
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 444`, `args: 84`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 19`, `unreferenced_by_name: 44`
* *Architecture:* `api: 61`, `concurrency: 249`, `import: 30`
* *Defense:* `safety: 58`, `doc: 26`, `test: 1`, `sync_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CalculationChangeset, CalculationsController, CalendarEventPB, CellCache, Cells, CreateRowParams, CreateRowPayloadPB, DatabaseLayoutMetaPB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 845.76 | **LOC:** 1227 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.9415%), Tech Debt (78.143%)
**Top Internal Functions/Classes:**
  * `build_collab` (Impact: 40.9)
    * *Intent:* ///NOTE: this method doesn't initialize plugins, however it is passed into WorkspaceDatabase, /// th...
  * `translate_row` (Impact: 30.5)
  * `summarize_row` (Impact: 29.1)
  * `initialize` (Impact: 20.4)
    * *Intent:* /// When initialize with new workspace, all the resources will be cleared.
  * `create_linked_view` (Impact: 20.0)
    * *Intent:* /// A linked view is a view that is linked to existing database.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 346`, `args: 101`, `func_start: 55`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `planned_debt: 1`, `unreferenced_by_name: 27`
* *Architecture:* `api: 36`, `concurrency: 133`, `import: 38`
* *Defense:* `safety: 33`, `doc: 9`, `sync_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CSVImporter, CollabBuilderConfig, CollabKVDB, CollabType, CreateViewParams, DatabaseCloudService, DatabaseCollabPersistenceService, DatabaseCollabService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/text_style/base/default_text_style.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 640.96 | **LOC:** 538 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `underline` (Impact: 16.7)
  * `standard` (Impact: 16.6)
  * `enhanced` (Impact: 16.6)
  * `prominent` (Impact: 16.6)
  * `standard` (Impact: 16.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 50`, `args: 40`, `func_start: 53`, `class_start: 9`
* *Risk/State:* `duplicate_logic: 28`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 199`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` widgets.dart
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `frontend/rust-lib/flowy-user/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 611.94 | **LOC:** 865 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.7437%), Tech Debt (98.7936%)
**Top Internal Functions/Classes:**
  * `set_cloud_config_handler` (Impact: 17.9)
  * `import_appflowy_data_folder_handler` (Impact: 11.7)
  * `get_user_workspace_handler` (Impact: 11.0)
  * `get_user_profile_handler` (Impact: 10.1)
  * `get_cloud_config_handler` (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 124
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 238`, `args: 60`, `func_start: 57`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 54`
* *Architecture:* `api: 55`, `concurrency: 114`, `import: 17`
* *Defense:* `safety: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FlowyError, FlowyResult, UserNotification, crate::entities::*, crate::notification::send_notification, crate::services::cloud_config::
  get_cloud_config, crate::services::data_import::prepare_import, crate::user_manager::UserManager...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager_user_workspace.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 553.8 | **LOC:** 822 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3071%), Tech Debt (66.2043%)
**Top Internal Functions/Classes:**
  * `open_workspace` (Impact: 53.5)
  * `get_all_user_workspaces` (Impact: 31.1)
  * `get_workspace_settings` (Impact: 26.5)
  * `upload_collab_data` (Impact: 24.0)
  * `create_workspace` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 207`, `args: 37`, `func_start: 32`
* *Risk/State:* `unreferenced_by_name: 23`
* *Architecture:* `api: 26`, `concurrency: 85`, `import: 19`
* *Defense:* `safety: 11`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FlowyError, FlowyResult, ImportedCollabData, ImportedFolder, ImportedFolderData, NaiveDateTime, Role, SubscribeWorkspacePB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/services/data_import/appflowy_data_import.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 525.06 | **LOC:** 1410 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5588%), Tech Debt (12.7012%)
**Top Internal Functions/Classes:**
  * `generate_import_data` (Impact: 64.8)
    * *Intent:* /// This path refers to the directory where AppFlowy stores its data. The directory structure is as ...
  * `migrate_folder_views` (Impact: 60.2)
  * `migrate_databases` (Impact: 33.0)
  * `replace_document_ref_ids` (Impact: 32.7)
  * `upload_collab_objects_data` (Impact: 29.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 290`, `args: 82`, `func_start: 24`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `dead_code: 3`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `concurrency: 5`, `import: 39`
* *Defense:* `safety: 32`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AuthType, Collab, CollabKVDB, DerefMut, Doc, FlowyResult, HashSet, ImportedAppFlowyData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-user/src/user_manager/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 513.2 | **LOC:** 925 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5327%), Tech Debt (74.2249%)
**Top Internal Functions/Classes:**
  * `init_with_callback` (Impact: 71.1)
    * *Intent:* /// Initializes the user session, including data migrations and user awareness configuration. This f...
  * `refresh_user_profile` (Impact: 25.1)
  * `continue_sign_up` (Impact: 22.9)
  * `sign_in` (Impact: 18.4)
    * *Intent:* /// Performs a user sign-in, initializing user awareness and sending relevant notifications. /// ///...
  * `new` (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 203`, `args: 51`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 61`, `import: 38`
* *Defense:* `safety: 24`, `doc: 29`, `sync_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AuthStatePB, DBConnection, DefaultUserStatusCallback, ExpressionMethods, FIRST_TIME_INSTALL_VERSION, Ordering, UserDataMigration, UserLocalDataMigration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/deps_resolve/cloud_service_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 500.3 | **LOC:** 919 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.2019%), Tech Debt (99.6641%)
**Top Internal Functions/Classes:**
  * `get_plugins` (Impact: 19.2)
  * `upload_part` (Impact: 9.6)
  * `create_upload` (Impact: 8.6)
  * `complete_upload` (Impact: 8.6)
  * `generate_search_summary` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 155`, `args: 71`, `func_start: 69`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 68`
* *Architecture:* `concurrency: 121`, `import: 37`
* *Defense:* `safety: 19`, `doc: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChatCloudService, ChatMessage, ChatMessageType, ChatSettings, CollabOrigin, CollabPluginProviderContext, CollabPluginProviderType, CompleteTextParams...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/ai_manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 498.78 | **LOC:** 814 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.2461%), Tech Debt (61.8445%)
**Top Internal Functions/Classes:**
  * `reload_with_workspace_id` (Impact: 21.5)
  * `sync_chat_documents` (Impact: 19.6)
  * `open_chat` (Impact: 18.4)
  * `update_rag_ids` (Impact: 15.6)
  * `stream_regenerate_response` (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 145
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 234`, `args: 42`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `unreferenced_by_name: 21`
* *Architecture:* `api: 36`, `concurrency: 120`, `import: 24`
* *Defense:* `safety: 19`, `doc: 15`, `sync_locks: 12`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChatCloudService, ChatInfoPB, ChatMessageListPB, ChatMessagePB, ChatSettings, ChatSettingsPB, CustomPromptDatabaseConfigurationPB, FilePB...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 479.3 | **LOC:** 892 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.0749%), Tech Debt (24.9979%)
**Top Internal Functions/Classes:**
  * `start_upload` (Impact: 60.4)
  * `create_upload` (Impact: 37.8)
  * `complete_upload` (Impact: 37.8)
  * `new` (Impact: 21.2)
  * `query_file_state` (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 229`, `args: 36`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 11`
* *Architecture:* `io: 5`, `api: 15`, `concurrency: 78`, `import: 25`
* *Defense:* `safety: 33`, `doc: 2`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CreatedUpload, FileProgress, FileProgressReceiver, FileUploadState, FileUploaderRunner, FlowyError, FlowyResult, MIN_CHUNK_SIZE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-folder/src/event_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 467.88 | **LOC:** 603 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.4576%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `create_view_handler` (Impact: 9.3)
  * `create_orphan_view_handler` (Impact: 9.3)
  * `update_recent_views_handler` (Impact: 7.6)
  * `set_default_publish_view_handler` (Impact: 7.6)
  * `remove_user_from_shared_page_handler` (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 112
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 197`, `args: 56`, `func_start: 50`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `planned_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `api: 49`, `concurrency: 102`, `import: 10`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AFPluginState, DataResult, FlowyResult, Weak, client_api::entity::guest_dto::RevokeSharedViewAccessRequest, crate::entities::*, crate::manager::FolderManager, crate::share::ImportParams...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-server/src/af_cloud/impls/user/cloud_service_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 419.72 | **LOC:** 693 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.0172%), Tech Debt (97.7691%)
**Top Internal Functions/Classes:**
  * `get_user_profile` (Impact: 19.4)
  * `create_collab_object` (Impact: 11.0)
  * `user_sign_in_with_url` (Impact: 10.0)
  * `get_user_awareness_doc_state` (Impact: 9.8)
  * `generate_sign_in_url_with_email` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 211`, `args: 55`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 39`
* *Architecture:* `api: 4`, `concurrency: 94`, `import: 25`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AFServer, AFWorkspaceInvitation, AFWorkspaceSettings, AFWorkspaceSettingsChange, AuthProvider, AuthResponse, AuthType, ClientConfiguration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-document/src/manager.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 394.18 | **LOC:** 526 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5509%), Tech Debt (73.5796%)
**Top Internal Functions/Classes:**
  * `create_document_instance` (Impact: 27.1)
    * *Intent:* /// Returns Document for given object id /// If the document does not exist in local disk, try get t...
  * `collab_for_document` (Impact: 18.4)
  * `create_document` (Impact: 17.3)
    * *Intent:* /// Create a new document. /// /// if the document already exists, return the existing document. ///...
  * `is_doc_exist` (Impact: 12.7)
  * `doc_state_from_document_data` (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 101
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 149`, `args: 47`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `dead_code: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 26`, `concurrency: 61`, `import: 29`
* *Defense:* `safety: 14`, `doc: 14`, `sync_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CollabBuilderConfig, CollabPersistenceImpl, DocumentSnapshotMeta, DocumentSnapshotMetaPB, DocumentSnapshotPB, FlowyError, FlowyResult, StorageService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-storage-pub/src/chunked_byte.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 391.06 | **LOC:** 418 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6898%), Tech Debt (78.9089%)
**Top Internal Functions/Classes:**
  * `next_chunk` (Impact: 9.7)
    * *Intent:* /// Read the next chunk from the file.
  * `from_file` (Impact: 8.0)
    * *Intent:* /// Create a `ChunkedBytes` instance from a file.
  * `set_offset` (Impact: 5.7)
    * *Intent:* /// Set the offset for the next chunk to be read.
  * `calculate_offsets` (Impact: 4.1)
  * `test_chunked_bytes_large_file` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 272
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 193`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 20`, `unreferenced_by_name: 11`
* *Architecture:* `io: 22`, `api: 9`, `concurrency: 82`, `import: 11`
* *Defense:* `safety: 6`, `doc: 7`, `test: 33`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncSeekExt, anyhow::anyhow, bytes::Bytes, std::env::temp_dir, std::fmt::Display, std::path::Path, super::*, tokio::fs::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-core/src/app_life_cycle.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 350.14 | **LOC:** 537 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3509%), Tech Debt (39.5247%)
**Top Internal Functions/Classes:**
  * `on_launch_if_authenticated` (Impact: 46.6)
  * `on_workspace_opened` (Impact: 40.4)
  * `on_sign_up` (Impact: 38.2)
  * `on_sign_in` (Impact: 35.4)
  * `folder_init_data_source` (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 72
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 112`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 10`
* *Architecture:* `api: 23`, `concurrency: 62`, `import: 29`
* *Defense:* `safety: 15`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FlowyResult, FolderManager, UserCloudServiceProvider, UserPaths, UserWorkspace, Weak, WorkspaceType, anyhow::Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/chat.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 331.58 | **LOC:** 668 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.6949%), Tech Debt (30.9554%)
**Top Internal Functions/Classes:**
  * `stream_response` (Impact: 82.2)
  * `load_remote_chat_messages` (Impact: 28.3)
  * `get_question_id_from_answer_id` (Impact: 13.2)
  * `stream_chat_message` (Impact: 12.8)
  * `load_prev_chat_messages` (Impact: 12.2)
    * *Intent:* /// Load chat messages for a given `chat_id`. /// /// 1. When opening a chat: /// - Loads local chat...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 71
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 146`, `args: 26`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 10`
* *Architecture:* `api: 13`, `concurrency: 51`, `import: 18`
* *Defense:* `safety: 11`, `doc: 12`, `sync_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicI64, ChatCloudService, ChatMessage, ChatMessageListPB, ChatMessagePB, FlowyError, FlowyResult, MessageCursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-database2/src/services/filter/controller.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 331.16 | **LOC:** 563 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1885%), Tech Debt (58.249%)
**Top Internal Functions/Classes:**
  * `apply_filter` (Impact: 41.4)
    * *Intent:* /// Recursively applies a `Filter` to a `Row`'s cells.
  * `apply_changeset` (Impact: 29.7)
  * `fill_cells` (Impact: 22.8)
  * `delete_filter` (Impact: 20.2)
  * `new` (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 162`, `args: 38`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 15`, `planned_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 12`, `concurrency: 50`, `import: 22`
* *Defense:* `safety: 23`, `doc: 3`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cells, DatabaseViewChangedNotifier, FilterChangeset, FilterInner, FilterResultNotification, InsertedRowPB, Row, RowDetail...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-ai/src/local_ai/chat/chains/conversation_chain.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 330.14 | **LOC:** 576 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2488%), Tech Debt (12.9174%)
**Top Internal Functions/Classes:**
  * `stream` (Impact: 31.8)
  * `execute` (Impact: 25.2)
  * `get_documents_or_result` (Impact: 24.6)
  * `get_question` (Impact: 11.5)
  * `get_related_questions` (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 160`, `args: 28`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 3`
* *Architecture:* `api: 23`, `concurrency: 47`, `import: 26`
* *Defense:* `safety: 12`, `doc: 2`, `sync_locks: 14`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChainError, CondenseQuestionGeneratorChain, CondenseQuestionPromptBuilder, Document, FlowyResult, Message, PromptArgs, QuestionStreamValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/flowy-sqlite-vec/src/db.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 317.6 | **LOC:** 639 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.77%), Tech Debt (27.3648%)
**Top Internal Functions/Classes:**
  * `upsert_collabs_embeddings` (Impact: 48.9)
    * *Intent:* /// Inserts or replaces all of `fragments` for the given (workspace_id, object_id), /// deleting any...
  * `select_all_embedded_documents` (Impact: 34.2)
  * `select_all_embedded_content` (Impact: 24.8)
  * `select_collabs_fragment_ids` (Impact: 19.4)
  * `process_search_results` (Impact: 17.1)
    * *Intent:* /// Process the query results and convert them to SearchResult objects
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 146`, `args: 29`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 8`
* *Architecture:* `api: 12`, `concurrency: 16`, `import: 14`
* *Defense:* `safety: 7`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashSet, PendingIndexedCollab, Result, SearchResult, SqliteEmbeddedDocument, SqliteEmbeddedFragment, anyhow::Context, crate::entities::
  EmbeddedContent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frontend/rust-lib/event-integration-test/src/database_event.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 298.14 | **LOC:** 737 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.3875%)
**Top Internal Functions/Classes:**
  * `insert_option` (Impact: 3.9)
  * `create_calendar` (Impact: 3.5)
  * `update_group` (Impact: 3.4)
  * `create_grid` (Impact: 3.3)
    * *Intent:* /// The initial data can refer to the [FolderOperationHandler::create_view_with_view_data] method.
  * `create_board` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 103`, `args: 58`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `unreferenced_by_name: 51`
* *Architecture:* `api: 57`, `concurrency: 88`, `import: 17`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.531
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RowId, SelectOption, SingleSelectTypeOption, bytes::Bytes, collab_database::database::timestamp, collab_database::fields::Field, collab_database::fields::select_type_option::
  MultiSelectTypeOption, collab_database::rows::Row...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/textfield/textfield.dart` -> **Lucas** (100.0% isolated ownership) | Magnitude: 91.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/component/popover/popover.dart` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/appflowy_theme.dart` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 9.7566%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/appflowy_theme.dart` -> **Severity: 334.929** (Blast Radius: 4.689 * Doc Risk: 71.4286%)
- `frontend/appflowy_flutter/lib/workspace/presentation/settings/widgets/emoji_picker/src/emoji_picker.dart` -> **Severity: 238.255** (Blast Radius: 2.803 * Doc Risk: 85.0%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/spacing/spacing.dart` -> **Severity: 203.2** (Blast Radius: 2.032 * Doc Risk: 100.0%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/border_radius/border_radius.dart` -> **Severity: 180.6** (Blast Radius: 1.806 * Doc Risk: 100.0%)
- `frontend/appflowy_flutter/packages/appflowy_ui/lib/src/theme/definition/shadow/shadow.dart` -> **Severity: 180.6** (Blast Radius: 1.806 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
