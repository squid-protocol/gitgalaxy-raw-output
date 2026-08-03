# ARCHITECTURAL_BRIEF: tauri
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/tauri` |
| **Timestamp** | `2026-08-03T19:47:34.148606+00:00` |
| **Scan Duration** | `2.27s` |
| **Git Branch** | `dev` |
| **Git Commit** | `b27be063ff3052cb1071ac3ec719cfa104460fa4` |
| **Git Remote** | `https://github.com/tauri-apps/tauri.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 423 malicious artifacts.

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
| Total Artifacts | 1065 |
| Analyzed Artifacts (Scanned) | 627 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 438 |
| Total LOC | 76534 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 58.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7743 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1626 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.941 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 300 | 63496 | 47.8% |
| MARKDOWN | 60 | 0 | 9.6% |
| JSON | 52 | 2340 | 8.3% |
| KOTLIN | 36 | 1733 | 5.7% |
| PLAINTEXT | 35 | 0 | 5.6% |
| JAVASCRIPT | 30 | 917 | 4.8% |
| HTML | 28 | 2353 | 4.5% |
| TYPESCRIPT | 26 | 3316 | 4.1% |
| XML | 23 | 2 | 3.7% |
| SWIFT | 17 | 761 | 2.7% |
| SHELL | 5 | 1029 | 0.8% |
| CSS | 3 | 133 | 0.5% |
| GROOVY | 3 | 60 | 0.5% |
| YAML | 3 | 264 | 0.5% |
| POWERSHELL | 2 | 34 | 0.3% |
| OBJECTIVE-C | 2 | 11 | 0.3% |
| BATCH | 1 | 67 | 0.2% |
| RUBY | 1 | 18 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.914`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 271 | 43.2% |
| file_cluster_0 | 110 | 17.5% |
| file_cluster_13 | 66 | 10.5% |
| file_cluster_16 | 38 | 6.1% |
| file_cluster_4 | 24 | 3.8% |
| file_cluster_2 | 11 | 1.8% |
| file_cluster_17 | 6 | 1.0% |
| file_cluster_11 | 1 | 0.2% |
| file_cluster_12 | 1 | 0.2% |
| file_cluster_15 | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 95 | 15.2% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 438*

**Composition by Extension & Reason:**
- `.png`: 79x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 29x Excluded (Unsupported Extension: '.toml'), 26x Unsupported Format (.toml), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.crate-manifest'), 1x Excluded (Unsupported Extension: '.xcworkspacedata')
- `.md`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2402 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 4031 LOC)
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nsh`: 24x Unsupported Format (.nsh)
- `.rs`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.json`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 3877 LOC), 1x Excluded (Massive Static Asset Blob: 3109 LOC)
- `.0`: 11x Excluded (Unsupported Extension: '.0'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 12x Excluded (Unsupported Extension: '.snap')
- `.js`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 581 LOC)
- `.html`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 7x Excluded (Explicitly Denied Extension: '.ico')
- `.kts`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.1 | 8.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 20.4 | 10.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.2 | 2.4 | 0.0 |
| API Exposure | 0.0 | 13.2 | 3.1 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.7 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 88.5 | 8.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.5 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 19.5 | 1.1 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (Hits: 126)
- `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (Hits: 80)
- `packages/api/src/path.ts` (Hits: 59)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TauriPlugin.kt** (`crates/tauri/mobile/android/src/main/java/app/tauri/annotation/TauriPlugin.kt`) — 21 inbound connections
2. **Window.svelte** (`examples/api/src/views/Window.svelte`) — 14 inbound connections
3. **base.ts** (`packages/api/src/menu/base.ts`) — 6 inbound connections
4. **InvokeArg.kt** (`crates/tauri/mobile/android/src/main/java/app/tauri/annotation/InvokeArg.kt`) — 5 inbound connections
5. **event.ts** (`packages/api/src/event.ts`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/tauri-runtime-wry/src/lib.rs`) — 136 outbound dependencies
2. **lib.rs** (`crates/tauri/src/lib.rs`) — 110 outbound dependencies
3. **app.rs** (`crates/tauri/src/app.rs`) — 93 outbound dependencies
4. **mod.rs** (`crates/tauri/src/webview/mod.rs`) — 83 outbound dependencies
5. **webview_window.rs** (`crates/tauri/src/webview/webview_window.rs`) — 71 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `new` (@ `crates/tauri-cli/src/interface/rust.rs`) -> Impact: **1847.7** | LOC: 1554
- `build_nsis_app_installer` (@ `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs`) -> Impact: **630.8** | LOC: 491
- `usage` (@ `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg`) -> Impact: **483.6** | LOC: 451
- `get_config` (@ `crates/tauri-cli/src/mobile/ios/mod.rs`) -> Impact: **444.9** | LOC: 432
- `handle_user_message` (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **393.7** | LOC: 831
- `migrate_imports` (@ `crates/tauri-cli/src/migrate/migrations/v1/frontend.rs`) -> Impact: **348.9** | LOC: 218
- `build_wix_app_installer` (@ `crates/tauri-bundler/src/bundle/windows/msi/mod.rs`) -> Impact: **338.7** | LOC: 468
  * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating the MSI installer. For now the only supported pla...
- `resolve` (@ `crates/tauri-utils/src/acl/resolved.rs`) -> Impact: **323.1** | LOC: 112
  * *Intent:* /// Resolves the ACL for the given plugin permissions and app capabilities.
- `parse` (@ `crates/tauri-macros/src/context.rs`) -> Impact: **314.2** | LOC: 124
- `new` (@ `crates/tauri/src/scope/fs.rs`) -> Impact: **297.6** | LOC: 451
  * *Intent:* /// Creates a new scope from a [`FsScope`] configuration.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parse` (@ `crates/tauri-macros/src/context.rs`) -> **O(2^N) [Recursive]**
- `apply` (@ `crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/RustPlugin.kt`) -> **O(2^N) [Recursive]**
- `rm_permission_files` (@ `crates/tauri-cli/src/acl/permission/rm.rs`) -> **O(2^N) [Recursive]**
- `items` (@ `crates/tauri-cli/src/info/packages_rust.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `crates/tauri-cli/src/interface/rust.rs`) -> **O(2^N) [Recursive]**
- `resolve` (@ `crates/tauri-utils/src/acl/resolved.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Resolves the ACL for the given plugin permissions and app capabilities.
- `invoke` (@ `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift`) -> **O(2^N) [Recursive]**
- `bundle_project` (@ `crates/tauri-bundler/src/bundle.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Bundles the project. /// Returns the list of paths where the bundles can be found.
- `output_ok` (@ `crates/tauri-bundler/src/utils/mod.rs`) -> **O(2^N) [Recursive]**
- `platforms` (@ `crates/tauri-cli/src/acl/permission/add.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `usage` (@ `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg`) -> DB Complexity: **390**
- `show_usage_[Truncated]` (@ `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh`) -> DB Complexity: **290**
- `new` (@ `crates/tauri-cli/src/interface/rust.rs`) -> DB Complexity: **59**
- `Anonymous_Block` (@ `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg`) -> DB Complexity: **39**
  * *Intent:* # Adding EULA resources
- `Anonymous_Block` (@ `crates/tauri-cli/templates/mobile/android/gradlew`) -> DB Complexity: **31**
  * *Intent:* # For Cygwin or MSYS, switch paths to Windows format before running java
- `read_source` (@ `crates/tauri-cli/src/icon.rs`) -> DB Complexity: **26**
- `gen` (@ `crates/tauri-cli/src/mobile/ios/project.rs`) -> DB Complexity: **25**
  * *Intent:* // unprefixed app_root seems pretty dangerous!! // TODO: figure out what cargo-mobile meant by that
- `handle_user_message` (@ `crates/tauri-runtime-wry/src/lib.rs`) -> DB Complexity: **25**
- `get_response` (@ `crates/tauri/src/protocol/asset.rs`) -> DB Complexity: **24**
- `new` (@ `crates/tauri/src/scope/fs.rs`) -> DB Complexity: **24**
  * *Intent:* /// Creates a new scope from a [`FsScope`] configuration.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/tauri-runtime-wry/src` | 4 | 2779.24 | 18.67% | 41.85% |
| `crates/tauri/src/menu` | 8 | 2620.46 | 5.25% | 15.59% |
| `crates/tauri/src` | 9 | 2568.5 | 19.36% | 66.13% |
| `crates/tauri-utils/src` | 12 | 2230.26 | 7.52% | 60.25% |
| `crates/tauri-cli/src/interface` | 2 | 2108.88 | 12.47% | 16.95% |
| `crates/tauri-cli/src/helpers` | 17 | 2048.18 | 15.35% | 32.31% |
| `crates/tauri-cli/src` | 12 | 1911.66 | 16.7% | 26.02% |
| `crates/tauri-utils/src/acl` | 8 | 1772.92 | 6.47% | 60.01% |
| `crates/tauri/src/manager` | 5 | 1453.96 | 9.08% | 15.24% |
| `crates/tauri-cli/src/mobile/ios` | 6 | 1423.52 | 11.81% | 7.83% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/tauri-cli/src/helpers/flock.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/plist.rs` -> **100.0%** Exposure
- `crates/tauri-runtime/src/dpi.rs` -> **100.0%** Exposure
- `crates/tauri/src/async_runtime.rs` -> **100.0%** Exposure
- `crates/tauri/src/ipc/command.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/tauri-bundler/src/utils/http_utils.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/utils/mod.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/config.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/prompts.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/template.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/tauri/src/test/mock_runtime.rs` -> **110** Orphaned Functions | **65** Duplicates
- `crates/tauri-runtime-wry/src/lib.rs` -> **32** Orphaned Functions | **92** Duplicates
- `crates/tauri-utils/src/config.rs` -> **0** Orphaned Functions | **69** Duplicates
- `crates/tauri-utils/src/config_v1/mod.rs` -> **6** Orphaned Functions | **55** Duplicates
- `crates/tauri/src/lib.rs` -> **25** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/BuildTask.kt`** -> AI Confidence: **99.48%**
2. **`crates/tauri-cli/templates/plugin/android/src/main/java/ExamplePlugin.kt`** -> AI Confidence: **99.48%**
3. **`crates/tauri/mobile/android/src/main/java/app/tauri/AppPlugin.kt`** -> AI Confidence: **99.48%**
4. **`crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`** -> AI Confidence: **99.48%**
5. **`crates/tauri/mobile/android/src/main/java/app/tauri/PathPlugin.kt`** -> AI Confidence: **99.48%**
6. **`crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt`** -> AI Confidence: **99.48%**
7. **`crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginManager.kt`** -> AI Confidence: **99.48%**
8. **`examples/api/src-tauri/tauri-plugin-sample/android/src/main/java/com/plugin/sample/ExamplePlugin.kt`** -> AI Confidence: **99.48%**
9. **`crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginHandle.kt`** -> AI Confidence: **99.44%**
10. **`crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/RustPlugin.kt`** -> AI Confidence: **99.34%**
11. **`crates/tauri/mobile/android/src/main/java/app/tauri/PermissionHelper.kt`** -> AI Confidence: **99.34%**
12. **`crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginResult.kt`** -> AI Confidence: **99.34%**
13. **`crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Invoke.kt`** -> AI Confidence: **99.32%**
14. **`bench/src/run_benchmark.rs`** -> AI Confidence: **99.31%**
15. **`bench/src/utils.rs`** -> AI Confidence: **99.31%**
16. **`crates/tauri-build/src/acl.rs`** -> AI Confidence: **99.31%**
17. **`crates/tauri-build/src/codegen/context.rs`** -> AI Confidence: **99.31%**
18. **`crates/tauri-build/src/lib.rs`** -> AI Confidence: **99.31%**
19. **`crates/tauri-build/src/manifest.rs`** -> AI Confidence: **99.31%**
20. **`crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy.rs`** -> AI Confidence: **99.31%**
21. **`crates/tauri-bundler/src/bundle/linux/debian.rs`** -> AI Confidence: **99.31%**
22. **`crates/tauri-bundler/src/bundle/linux/rpm.rs`** -> AI Confidence: **99.31%**
23. **`crates/tauri-bundler/src/bundle/macos/app.rs`** -> AI Confidence: **99.31%**
24. **`crates/tauri-bundler/src/bundle/macos/ios.rs`** -> AI Confidence: **99.31%**
25. **`crates/tauri-bundler/src/bundle/macos/sign.rs`** -> AI Confidence: **99.31%**
26. **`crates/tauri-bundler/src/bundle/settings.rs`** -> AI Confidence: **99.31%**
27. **`crates/tauri-bundler/src/bundle/windows/nsis/mod.rs`** -> AI Confidence: **99.31%**
28. **`crates/tauri-bundler/src/bundle/windows/util.rs`** -> AI Confidence: **99.31%**
29. **`crates/tauri-cli/src/acl/capability/new.rs`** -> AI Confidence: **99.31%**
30. **`crates/tauri-cli/src/acl/permission/add.rs`** -> AI Confidence: **99.31%**
31. **`crates/tauri-cli/src/acl/permission/ls.rs`** -> AI Confidence: **99.31%**
32. **`crates/tauri-cli/src/acl/permission/new.rs`** -> AI Confidence: **99.31%**
33. **`crates/tauri-cli/src/acl/permission/rm.rs`** -> AI Confidence: **99.31%**
34. **`crates/tauri-cli/src/build.rs`** -> AI Confidence: **99.31%**
35. **`crates/tauri-cli/src/completions.rs`** -> AI Confidence: **99.31%**
36. **`crates/tauri-cli/src/helpers/app_paths.rs`** -> AI Confidence: **99.31%**
37. **`crates/tauri-cli/src/helpers/npm.rs`** -> AI Confidence: **99.31%**
38. **`crates/tauri-cli/src/info/env_system.rs`** -> AI Confidence: **99.31%**
39. **`crates/tauri-cli/src/init.rs`** -> AI Confidence: **99.31%**
40. **`crates/tauri-cli/src/migrate/migrations/v2_beta.rs`** -> AI Confidence: **99.31%**
41. **`crates/tauri-cli/src/migrate/mod.rs`** -> AI Confidence: **99.31%**
42. **`crates/tauri-cli/src/mobile/android/android_studio_script.rs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/api/eslint.config.js` -> **100.0%** Exposure
- `crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/RustPlugin.kt` -> **100.0%** Exposure
- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt` -> **100.0%** Exposure
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **100.0%** Exposure
- `packages/api/src/window.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `crates/tauri-macos-sign/src/lib.rs` -> **100.0%** Exposure
- `crates/tauri/src/ipc/mod.rs` -> **100.0%** Exposure
- `packages/api/eslint.config.js` -> **100.0%** Exposure
- `packages/cli/tauri.js` -> **100.0%** Exposure
- `crates/tauri-cli/scripts/kill-children.sh` -> **100.0%** Exposure
### Raw Memory Manipulation
- `crates/tauri-runtime/src/lib.rs` -> **0.0004%** Exposure
- `crates/tauri/src/webview/webview_window.rs` -> **0.0003%** Exposure
### Hardcoded Payload Artifacts
- `packages/api/src/core.ts` -> **99.9618%** Exposure
### Algorithmic DoS Exposure
- `crates/tauri-bundler/src/bundle.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/bundle/linux/rpm.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/bundle/macos/ios.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/bundle/updater_bundle.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4393` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` (KOTLIN) -> Cumulative Risk: **851.21**
- **Archetype:** `file_cluster_13` (Distance: 13.039 IQR)
- **Magnitude:** 492.66 | **LOC:** 515 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `requestPermissions` (Impact: 75.0), `isPermissionDeclared` (Impact: 73.0), `getPermissionStates` (Impact: 71.9)

### 2. `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (SHELL) -> Cumulative Risk: **831.71**
- **Archetype:** `file_cluster_4` (Distance: 13.083 IQR)
- **Magnitude:** 378.92 | **LOC:** 328 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `show_usage_[Truncated]` (Impact: 239.0), `Anonymous_Block` (Impact: 3.2), `__global_context__` (Impact: 1.5)

### 3. `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginManager.kt` (KOTLIN) -> Cumulative Risk: **774.09**
- **Archetype:** `file_cluster_13` (Distance: 12.075 IQR)
- **Magnitude:** 199.74 | **LOC:** 225 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5629%), Tech Debt (99.5095%), Concurrency (99.4317%)
- **Heaviest Functions:** `dispatchPluginMessage` (Impact: 24.5), `onActivityCreate` (Impact: 19.5), `runCommand` (Impact: 10.9)

### 4. `packages/api/src/window.ts` (TYPESCRIPT) -> Cumulative Risk: **749.08**
- **Archetype:** `file_cluster_4` (Distance: 13.458 IQR)
- **Magnitude:** 117.32 | **LOC:** 2673 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (96.6022%)
- **Heaviest Functions:** `setSizeConstraints` (Impact: 34.1), `handler` (Impact: 12.6), `setMinSize` (Impact: 11.6)

### 5. `crates/tauri-cli/src/interface/rust/desktop.rs` (RUST) -> Cumulative Risk: **738.37**
- **Archetype:** `file_cluster_17` (Distance: 13.347 IQR)
- **Magnitude:** 542.68 | **LOC:** 423 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.3474%)
- **Heaviest Functions:** `build` (Impact: 146.9), `run_dev` (Impact: 135.4), `cargo_command` (Impact: 36.7)

### 6. `crates/tauri-bundler/src/utils/mod.rs` (RUST) -> Cumulative Risk: **737.16**
- **Archetype:** `file_cluster_4` (Distance: 13.413 IQR)
- **Magnitude:** 223.96 | **LOC:** 142 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `output_ok` (Impact: 139.8), `resource_relative_paths` (Impact: 2.5), `is_retina` (Impact: 2.4)

### 7. `crates/tauri-cli/src/dev/builtin_dev_server.rs` (RUST) -> Cumulative Risk: **727.15**
- **Archetype:** `file_cluster_4` (Distance: 11.742 IQR)
- **Magnitude:** 195.0 | **LOC:** 170 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.7715%), Documentation (86.6582%)
- **Heaviest Functions:** `start` (Impact: 62.5), `watch` (Impact: 42.7), `handler` (Impact: 14.5)

### 8. `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift` (SWIFT) -> Cumulative Risk: **722.85**
- **Archetype:** `file_cluster_0` (Distance: 11.01 IQR)
- **Magnitude:** 257.6 | **LOC:** 158 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (99.9995%)
- **Heaviest Functions:** `invoke` (Impact: 149.5), `load` (Impact: 13.9), `runCommand` (Impact: 13.7)

### 9. `crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/RustPlugin.kt` (KOTLIN) -> Cumulative Risk: **715.13**
- **Archetype:** `file_cluster_13` (Distance: 12.274 IQR)
- **Magnitude:** 145.86 | **LOC:** 85 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9957%)
- **Heaviest Functions:** `apply` (Impact: 115.4)

### 10. `crates/tauri-cli/src/dev.rs` (RUST) -> Cumulative Risk: **706.53**
- **Archetype:** `file_cluster_0` (Distance: 12.338 IQR)
- **Magnitude:** 339.68 | **LOC:** 372 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (97.5497%)
- **Heaviest Functions:** `setup` (Impact: 205.2), `kill_before_dev_process` (Impact: 15.0), `on_app_exit` (Impact: 11.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/tauri-runtime-wry/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.451 IQR)
- **Top Global Matches:** file_cluster_0: 13.451, file_cluster_8: 13.617, file_cluster_16: 13.655
- **Magnitude:** 2339.14 | **LOC:** 5354 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 29.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (14.1789%), Tech Debt (99.9293%)
**Top Internal Functions/Classes:**
  * `handle_user_message` (Impact: 393.7 | O(N^4) | DB: 25)
  * `handle_event_loop` (Impact: 284.0 | O(N^5) | DB: 5)
  * `create_window` (Impact: 175.9 | O(N^3) | DB: 12)
  * `with_config` (Impact: 66.8 | O(N^2) | DB: 2)
  * `map_from_tao` (Impact: 34.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 580`, `args: 328`, `func_start: 244`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 2`, `state_mutation: 200`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 92`, `orphaned_logic: 32`
* *Architecture:* `api: 97`, `concurrency: 69`, `import: 52`
* *Defense:* `safety: 567`, `doc: 34`, `sync_locks: 66`, `immutability_locks: 38`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tauri_utils::
  config::Color, Result, WebViewBuilder, tauri_utils::TitleBarStyle, UserEvent, Sender, LogicalSize, HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/interface/rust.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.089 IQR)
- **Top Global Matches:** file_cluster_0: 13.089, file_cluster_8: 13.108, file_cluster_16: 13.143
- **Magnitude:** 2058.56 | **LOC:** 1895 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (14.082%), Tech Debt (11.8925%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 1847.7 | O(2^N) | DB: 59)
  * `from` (Impact: 2.6 | O(N^1))
  * `from` (Impact: 2.6 | O(N^1))
  * `from` (Impact: 2.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 244`, `args: 115`, `func_start: 38`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 96`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 57`, `concurrency: 20`, `import: 17`
* *Defense:* `safety: 205`, `doc: 41`, `test: 20`, `sync_locks: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time::Duration, Write, crate::helpers::config::custom_sign_settings, tauri_utils::config::parse::is_configuration_file, wix_settings, std::
  collections::HashMap, MacOsSettings, DevProcess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.826 IQR)
- **Top Global Matches:** file_cluster_0: 13.826, file_cluster_16: 14.055, file_cluster_13: 14.138
- **Magnitude:** 1213.02 | **LOC:** 4454 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (4.0984%), Tech Debt (99.9673%)
**Top Internal Functions/Classes:**
  * `add_configured_headers` (Impact: 87.0 | O(2^N) | DB: 1)
  * `deserialize` (Impact: 80.9 | O(N^4) | DB: 3)
  * `fmt` (Impact: 42.5 | O(2^N) | DB: 2)
    * *Intent:* /// App resources to bundle. /// Each resource is a path to a file or directory. /// Glob patterns a...
  * `fmt` (Impact: 42.5 | O(2^N) | DB: 2)
  * `deserialize` (Impact: 37.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 513`, `args: 77`, `func_start: 117`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 124`, `dead_code: 6`, `planned_debt: 6`, `duplicate_logic: 69`
* *Architecture:* `api: 226`, `import: 34`
* *Defense:* `safety: 359`, `doc: 1311`, `test: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
  collections::HashMap, Serialize, crate::literal_struct, TokenStreamExt, WindowEffectState, Visitor, quote::quote, crate::acl::capability::Capability...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.776 IQR)
- **Top Global Matches:** file_cluster_0: 16.776, file_cluster_4: 17.022, file_cluster_13: 17.094
- **Magnitude:** 1160.02 | **LOC:** 2606 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (28.0113%), Tech Debt (99.6691%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 204.2 | O(2^N) | DB: 5)
    * *Intent:* #[cfg(not(feature = "wry"))] #[cfg_attr(docsrs, doc(cfg(not(feature = "wry"))))]
  * `on_event_loop_event` (Impact: 72.8 | O(N^4))
    * *Intent:* /// use std::{collections::HashMap, sync::Mutex}; /// use tauri::State; /// // here we use Mutex to ...
  * `fetch_data_store_identifiers` (Impact: 37.4 | O(2^N))
  * `remove_data_store` (Impact: 37.3 | O(2^N))
    * *Intent:* /// A handle to the currently running application. ///
  * `setup` (Impact: 30.2 | O(2^N) | DB: 1)
    * *Intent:* /// refers to a different `T`. /// /// Managed state can be retrieved by any command handler via the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 253`, `args: 94`, `func_start: 86`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 1`, `state_mutation: 70`, `dead_code: 56`, `planned_debt: 2`, `duplicate_logic: 33`
* *Architecture:* `api: 104`, `concurrency: 191`, `import: 26`
* *Defense:* `safety: 204`, `doc: 844`, `test: 3`, `sync_locks: 39`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Submenu, StateManager, sync::atomic, MSG, CallbackFn, RunEvent, MenuEvent, Monitor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.769 IQR)
- **Top Global Matches:** file_cluster_8: 11.769, file_cluster_0: 11.859, file_cluster_17: 11.864
- **Magnitude:** 884.28 | **LOC:** 891 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 63.6%
- **Algorithmic:** O(N^4) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (15.73%), Tech Debt (8.5834%)
**Top Internal Functions/Classes:**
  * `build_nsis_app_installer` (Impact: 630.8 | O(N^4) | DB: 23)
  * `generate_resource_data` (Impact: 44.8 | O(N^2) | DB: 2)
  * `bundle_project` (Impact: 41.0 | O(N^2) | DB: 6)
    * *Intent:* /// Runs all of the commands to build the NSIS installer. /// Returns a vector of PathBuf that shows...
  * `generate_binaries_data` (Impact: 22.6 | O(N^2) | DB: 1)
  * `try_add_numeric_build_number` (Impact: 16.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 141`, `args: 45`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 41`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 1`, `import: 8`
* *Defense:* `safety: 69`, `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sign_command, std::io::BufWriter, Write, tauri_utils::display_path, utils::
    http_utils::download_and_verify, HashAlgorithm, try_sign, Settings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/menu/plugin.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.629 IQR)
- **Top Global Matches:** file_cluster_0: 12.629, file_cluster_16: 12.699, file_cluster_8: 12.716
- **Magnitude:** 879.1 | **LOC:** 927 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.85%), Tech Debt (29.0521%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 113.4 | O(2^N) | DB: 2)
  * `insert` (Impact: 64.9 | O(2^N) | DB: 1)
  * `append` (Impact: 60.1 | O(2^N))
  * `prepend` (Impact: 60.1 | O(2^N))
  * `remove_at` (Impact: 60.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 173`, `args: 47`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `duplicate_logic: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 8`, `import: 6`
* *Defense:* `safety: 215`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` crate::
  command, Serialize, TauriPlugin, State, Webview, RunEvent, *, ipc::channel::JavaScriptChannelId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/webview/webview_window.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 19.472 IQR)
- **Top Global Matches:** file_cluster_0: 19.472, file_cluster_11: 19.736, file_cluster_13: 19.759
- **Magnitude:** 878.38 | **LOC:** 2661 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 29.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (14.1289%), Tech Debt (43.3705%)
**Top Internal Functions/Classes:**
  * `on_document_title_changed` (Impact: 9.8 | O(2^N) | DB: 1)
  * `window_features` (Impact: 7.6 | O(N^1) | DB: 1)
    * *Intent:* /// Forces a theme or uses the system settings if None was provided. ///
  * `on_page_load` (Impact: 7.5 | O(2^N) | DB: 1)
  * `transient_for` (Impact: 7.5 | O(2^N) | DB: 1)
    * *Intent:* /// Sets whether or not the window icon should be hidden from the taskbar.
  * `from_config` (Impact: 7.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 154`, `args: 161`, `func_start: 141`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 72`, `dead_code: 91`, `duplicate_logic: 10`, `orphaned_logic: 2`
* *Architecture:* `api: 134`, `concurrency: 77`, `import: 23`
* *Defense:* `safety: 116`, `doc: 1238`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Submenu, window::Monitor, window::Color, http::header::HeaderValue, Size, UserAttentionType, EventName, path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.887 IQR)
- **Top Global Matches:** file_cluster_12: 13.887, file_cluster_11: 13.928, file_cluster_8: 14.0
- **Magnitude:** 815.6 | **LOC:** 639 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 390
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (79.7792%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 483.6 | O(2^N) | DB: 390)
  * `Anonymous_Block` (Impact: 13.6 | O(N^1) | DB: 39)
    * *Intent:* # Adding EULA resources
  * `hdiutil_detach_retry` (Impact: 12.3 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 10.6 | O(N^1))
    * *Intent:* # Make the top window open itself on mount:
  * `Anonymous_Block` (Impact: 10.6 | O(N^1) | DB: 6)
    * *Intent:* # Enable "internet", whatever that is
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 69`, `args: 41`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 226`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 126`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 56`, `sync_locks: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` folder, -f
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/window/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.58 IQR)
- **Top Global Matches:** file_cluster_0: 13.58, file_cluster_16: 13.608, file_cluster_8: 13.775
- **Magnitude:** 790.72 | **LOC:** 2471 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (6.4735%), Tech Debt (97.3072%)
**Top Internal Functions/Classes:**
  * `build_internal` (Impact: 61.9 | O(N^2) | DB: 3)
  * `set_menu` (Impact: 17.5 | O(N^2))
  * `remove_menu` (Impact: 17.2 | O(N^2))
  * `is_menu_visible` (Impact: 17.0 | O(N^2))
  * `hide_menu` (Impact: 16.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 197`, `args: 150`, `func_start: 115`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 15`
* *Architecture:* `api: 119`, `concurrency: 30`, `import: 18`
* *Defense:* `safety: 182`, `doc: 526`, `test: 2`, `sync_locks: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` window::DetachedWindow, Submenu, WindowDispatch, Hasher, monitor::Monitor, runtime::
    dpi::Position, std::sync::mpsc::channel, window::Color...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/msi/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.885 IQR)
- **Top Global Matches:** file_cluster_8: 11.885, file_cluster_0: 12.135, file_cluster_17: 12.146
- **Magnitude:** 788.6 | **LOC:** 1142 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (22.2216%), Tech Debt (12.6482%)
**Top Internal Functions/Classes:**
  * `build_wix_app_installer` (Impact: 338.7 | O(N^2) | DB: 23)
    * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating...
  * `generate_resource_data` (Impact: 86.7 | O(N^3) | DB: 6)
    * *Intent:* /// Generates the data required for the resource bundling on wix
  * `run_candle` (Impact: 38.4 | O(N^2) | DB: 3)
    * *Intent:* /// Runs the Candle.exe executable for Wix. Candle parses the wxs file and generates the code for bu...
  * `get_wix_data` (Impact: 38.2 | O(2^N) | DB: 3)
    * *Intent:* /// Generates the wix XML string to bundle this directory resources recursively
  * `convert_version` (Impact: 34.5 | O(N^2))
    * *Intent:* // WiX requires versions to be numeric only in a `major.minor.patch.build` format
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 201`, `args: 43`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 98`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 5`, `import: 8`
* *Defense:* `safety: 60`, `doc: 31`, `test: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` uuid::Uuid, display_path, HashAlgorithm, try_sign, Settings, extract_zip, Serialize, path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config_v1/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.637 IQR)
- **Top Global Matches:** file_cluster_0: 12.637, file_cluster_16: 12.909, file_cluster_8: 13.088
- **Magnitude:** 757.14 | **LOC:** 3166 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.3725%), Tech Debt (99.9896%)
**Top Internal Functions/Classes:**
  * `visit_str` (Impact: 57.9 | O(N^4) | DB: 2)
    * *Intent:* /// Allowlist for the global shortcut APIs. /// /// See more: https://tauri.app/v1/api/config#global...
  * `deserialize` (Impact: 18.8 | O(2^N))
    * *Intent:* /// A set of command arguments allowed to be executed by the webview API. /// /// A value of `true` ...
  * `deserialize` (Impact: 18.7 | O(2^N))
    * *Intent:* /// Enable the shell open API, with a custom regex that the opened path must match against. /// /// ...
  * `deserialize` (Impact: 16.9 | O(2^N))
  * `merge` (Impact: 14.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 230`, `args: 75`, `func_start: 65`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 76`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 55`, `orphaned_logic: 6`
* *Architecture:* `api: 213`, `import: 9`
* *Defense:* `safety: 162`, `doc: 853`, `test: 8`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
  collections::HashMap, Serialize, Visitor, semver::Version, schemars::schema::Metadata, url::Url, fs::read_to_string, fmt::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/test/mock_runtime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.63 IQR)
- **Top Global Matches:** file_cluster_0: 13.63, file_cluster_8: 13.763, file_cluster_16: 13.851
- **Magnitude:** 697.32 | **LOC:** 1400 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.7097%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 70.9 | O(N^5) | DB: 3)
  * `create_window` (Impact: 13.2 | O(N^2) | DB: 1)
    * *Intent:* /// Create a new webview window.
  * `create_window` (Impact: 13.2 | O(N^2) | DB: 2)
  * `create_window` (Impact: 13.2 | O(N^2) | DB: 1)
  * `send_message` (Impact: 11.2 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 99`, `args: 7`, `func_start: 205`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 53`, `planned_debt: 4`, `duplicate_logic: 65`, `orphaned_logic: 110`
* *Architecture:* `api: 9`, `concurrency: 33`, `import: 6`
* *Defense:* `safety: 349`, `doc: 4`, `sync_locks: 16`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Receiver, Result, WindowDispatch, sync::
    atomic::AtomicBool, monitor::Monitor, Size, UserAttentionType, tauri_utils::TitleBarStyle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/acl/resolved.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.768 IQR)
- **Top Global Matches:** file_cluster_0: 11.768, file_cluster_8: 11.821, file_cluster_17: 11.86
- **Magnitude:** 615.46 | **LOC:** 684 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.7673%), Tech Debt (34.768%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 323.1 | O(2^N) | DB: 9)
    * *Intent:* /// Resolves the ACL for the given plugin permissions and app capabilities.
  * `get_permission_set_permissions` (Impact: 106.0 | O(2^N) | DB: 1)
  * `resolve_command` (Impact: 31.6 | O(N^2) | DB: 2)
  * `get_permissions` (Impact: 24.0 | O(N^1))
  * `manifest` (Impact: 9.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 106`, `args: 38`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 46`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 55`, `doc: 28`, `test: 28`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ExecutionContext, crate::platform::Target, TokenStreamExt, crate::literal_struct, super::
  capability::Capability, PermissionEntry, std::collections::BTreeMap, Permission...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/manager/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.077 IQR)
- **Top Global Matches:** file_cluster_0: 12.077, file_cluster_16: 12.263, file_cluster_8: 12.359
- **Magnitude:** 571.9 | **LOC:** 1029 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.773%), Tech Debt (76.2199%)
**Top Internal Functions/Classes:**
  * `get_asset` (Impact: 62.2 | O(N^3) | DB: 6)
  * `emit_to` (Impact: 46.2 | O(N^2))
  * `emit_filter` (Impact: 35.6 | O(2^N))
    * *Intent:* #[cfg(feature = "tracing")]
  * `emit` (Impact: 30.5 | O(2^N))
    * *Intent:* /// # Panics
  * `set_csp` (Impact: 29.2 | O(N^3) | DB: 5)
    * *Intent:* /// Sets the CSP value to the asset HTML if needed (on Linux). /// Returns the CSP string for access...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 125`, `args: 66`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 61`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 55`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 88`, `doc: 28`, `test: 15`, `sync_locks: 16`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Receiver, time::Duration, StateManager, std::
    sync::mpsc::channel, Arc, EventName, crate::
  app::
    AppHandle, Webview...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/manager/webview.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.32 IQR)
- **Top Global Matches:** file_cluster_0: 11.32, file_cluster_8: 11.435, file_cluster_16: 11.492
- **Magnitude:** 570.2 | **LOC:** 740 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (12.167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare_webview` (Impact: 210.0 | O(N^3) | DB: 4)
  * `prepare_pending_webview` (Impact: 186.7 | O(N^3) | DB: 8)
  * `on_webview_event` (Impact: 36.6 | O(N^3))
  * `initialization_script` (Impact: 26.6 | O(N^2))
  * `attach_webview` (Impact: 14.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 120`, `args: 30`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `api: 26`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 70`, `doc: 10`, `test: 6`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AppManager, ipc::InvokeHandler, Webview, DefaultTemplate, EmitPayload, Mutex, EventLoopMessage, url::Url...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.077 IQR)
- **Top Global Matches:** file_cluster_0: 12.077, file_cluster_8: 12.109, file_cluster_13: 12.192
- **Magnitude:** 569.58 | **LOC:** 623 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 54.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (16.3486%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `ensure_init` (Impact: 151.4 | O(N^4) | DB: 10)
  * `use_network_address_for_dev_url` (Impact: 87.3 | O(N^3) | DB: 5)
  * `local_ip_address` (Impact: 66.0 | O(2^N))
  * `get_app` (Impact: 32.3 | O(N^3))
  * `from_str` (Impact: 24.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 102`, `args: 49`, `func_start: 21`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 32`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `api: 17`, `concurrency: 10`, `import: 15`
* *Defense:* `safety: 71`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ServerBuilder, Write, net::AddrParseError, Result, sync::
    atomic::AtomicBool, ConfigMetadata, std::
  collections::HashMap, DevProcess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/interface/rust/desktop.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.347 IQR)
- **Top Global Matches:** file_cluster_17: 13.347, file_cluster_4: 13.366, file_cluster_8: 13.502
- **Magnitude:** 542.68 | **LOC:** 423 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (65.3821%), Tech Debt (35.3662%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 146.9 | O(2^N) | DB: 6)
  * `run_dev` (Impact: 135.4 | O(N^3) | DB: 13)
  * `cargo_command` (Impact: 36.7 | O(N^1) | DB: 3)
  * `build_production_app` (Impact: 24.7 | O(N^2) | DB: 2)
  * `validate_target` (Impact: 21.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 93`, `args: 31`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 69`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 32`, `import: 8`
* *Defense:* `safety: 77`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Write, sync::
    atomic::AtomicBool, GENERIC_READ, Win32::
      Foundation::CloseHandle, DevProcess, Arc, std::mem, Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/migrate/migrations/v1/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.953 IQR)
- **Top Global Matches:** file_cluster_8: 10.953, file_cluster_0: 11.244, file_cluster_17: 11.421
- **Magnitude:** 530.06 | **LOC:** 1257 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (11.8961%), Tech Debt (12.4958%)
**Top Internal Functions/Classes:**
  * `migrate_config` (Impact: 93.9 | O(N^3) | DB: 6)
  * `process_security` (Impact: 76.1 | O(N^4) | DB: 3)
  * `allowlist_to_permissions` (Impact: 61.5 | O(N^2) | DB: 2)
  * `migrate` (Impact: 38.7 | O(N^2) | DB: 3)
  * `migrate` (Impact: 37.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 116`, `args: 53`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 70`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 65`, `test: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` serde_json::Map, crate::error::Context, std::
  collections::BTreeMap, Result, fs, ErrorExt, path::Path, tauri_utils::acl::
  capability::Capability...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/ios/build.rs` (RUST | Tier 1 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.639 IQR)
- **Top Global Matches:** file_cluster_0: 12.639, file_cluster_13: 12.813, file_cluster_8: 12.824
- **Magnitude:** 527.16 | **LOC:** 560 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 47.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (21.1051%), Tech Debt (11.1784%)
**Top Internal Functions/Classes:**
  * `run_build` (Impact: 278.1 | O(N^4) | DB: 13)
  * `run` (Impact: 122.8 | O(N^2) | DB: 20)
  * `auth_credentials_from_env` (Impact: 8.7 | O(N^2))
  * `fmt` (Impact: 7.3 | O(2^N) | DB: 1)
  * `from_str` (Impact: 4.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 98`, `args: 16`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 19`, `import: 7`
* *Defense:* `safety: 63`, `doc: 24`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` plist::merge_plist, Result, BuildConfig, ConfigMetadata, synchronize_project_config, target::ArchiveConfig, Target, inject_resources...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.934 IQR)
- **Top Global Matches:** file_cluster_0: 12.934, file_cluster_13: 13.057, file_cluster_4: 13.078
- **Magnitude:** 511.7 | **LOC:** 439 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (34.3407%), Tech Debt (12.1994%)
**Top Internal Functions/Classes:**
  * `output_ok` (Impact: 172.8 | O(2^N) | DB: 17)
    * *Intent:* // The `pipe` function sets the stdout and stderr to properly // show the command output in the Node...
  * `from_str` (Impact: 113.5 | O(2^N) | DB: 6)
  * `try_run` (Impact: 97.4 | O(N^2) | DB: 2)
    * *Intent:* /// Run the Tauri CLI with the passed arguments. /// /// It is similar to [`run`], but instead of ex...
  * `fmt` (Impact: 11.0 | O(2^N) | DB: 1)
  * `run` (Impact: 4.5 | O(N^1))
    * *Intent:* /// Run the Tauri CLI with the passed arguments, exiting if an error occurs. /// /// The passed argu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 103`, `args: 27`, `func_start: 13`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 52`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 30`, `import: 12`
* *Defense:* `safety: 67`, `doc: 22`, `test: 4`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FromArgMatches, Write, Result, Output, log::Level, Serialize, env_logger::Builder, Style...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/ios/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.219 IQR)
- **Top Global Matches:** file_cluster_0: 12.219, file_cluster_8: 12.327, file_cluster_17: 12.36
- **Magnitude:** 506.86 | **LOC:** 699 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (9.2984%), Tech Debt (9.1358%)
**Top Internal Functions/Classes:**
  * `get_config` (Impact: 444.9 | O(N^3) | DB: 7)
  * `command` (Impact: 25.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 80`, `args: 38`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 11`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `api: 16`, `import: 8`
* *Defense:* `safety: 96`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` teams::find_development_teams, time::Duration, Result, ConfigMetadata, path::Path, tauri_utils::resources::ResourcePaths, Target, Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/init.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.856 IQR)
- **Top Global Matches:** file_cluster_8: 11.856, file_cluster_13: 12.101, file_cluster_17: 12.107
- **Magnitude:** 494.84 | **LOC:** 399 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.1301%), Tech Debt (9.7979%)
**Top Internal Functions/Classes:**
  * `exec` (Impact: 186.6 | O(N^3) | DB: 5)
  * `unprefix_path` (Impact: 54.1 | O(2^N) | DB: 2)
  * `prefix_path` (Impact: 43.3 | O(2^N) | DB: 2)
  * `join` (Impact: 24.7 | O(2^N) | DB: 2)
  * `app_root` (Impact: 24.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 63`, `args: 26`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 60`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Result, Output, RenderError, crate::
  helpers::app_paths::Dirs, RenderErrorReason, Target, heck::ToSnekCase, template::JsonMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.039 IQR)
- **Top Global Matches:** file_cluster_13: 13.039, file_cluster_0: 13.303, file_cluster_11: 13.35
- **Magnitude:** 492.66 | **LOC:** 515 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (54.4195%), Tech Debt (92.0713%)
**Top Internal Functions/Classes:**
  * `requestPermissions` (Impact: 75.0 | O(N^3) | DB: 10)
  * `isPermissionDeclared` (Impact: 73.0 | O(2^N) | DB: 2)
  * `getPermissionStates` (Impact: 71.9 | O(N^4) | DB: 5)
  * `getPermissionStringsForAliases` (Impact: 15.6 | O(N^2) | DB: 1)
  * `checkPermissions` (Impact: 12.8 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `args: 35`, `func_start: 33`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 84`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 22`, `concurrency: 12`, `import: 21`
* *Defense:* `safety: 4`, `doc: 46`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00639
  * `Imports (Out-Degree: 8):` app.tauri.Logger, app.tauri.annotation.Command, android.webkit.WebView, app.tauri.annotation.InvokeArg, java.util.*, android.content.res.Configuration, androidx.activity.result.IntentSenderRequest, androidx.core.app.ActivityCompat...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/migrate/migrations/v1/frontend.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.799 IQR)
- **Top Global Matches:** file_cluster_13: 10.799, file_cluster_0: 10.864, file_cluster_17: 11.133
- **Magnitude:** 481.96 | **LOC:** 693 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.4228%), Tech Debt (8.982%)
**Top Internal Functions/Classes:**
  * `migrate_imports` (Impact: 348.9 | O(N^5) | DB: 7)
  * `migrate` (Impact: 67.2 | O(N^3) | DB: 8)
    * *Intent:* /// Returns a list of migrated plugins
  * `migrates_vue` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 140`, `args: 19`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 42`, `dead_code: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 9`, `api: 1`, `concurrency: 10`, `import: 50`
* *Defense:* `safety: 27`, `doc: 1`, `test: 13`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, helpers::app_paths::walk_builder, pretty_assertions::assert_eq, Result, oxc_parser::Parser, npm::PackageManager, Error, ErrorExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/ipc/protocol.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.93 IQR)
- **Top Global Matches:** file_cluster_0: 10.93, file_cluster_8: 11.101, file_cluster_13: 11.286
- **Magnitude:** 457.96 | **LOC:** 753 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (8.7673%), Tech Debt (19.0897%)
**Top Internal Functions/Classes:**
  * `handle_ipc_message` (Impact: 198.4 | O(N^5) | DB: 8)
  * `parse_invoke_request` (Impact: 121.0 | O(N^4) | DB: 4)
  * `get` (Impact: 81.1 | O(N^5) | DB: 8)
  * `parse_invoke_request_isolation` (Impact: 8.7 | O(N^1) | DB: 4)
  * `parse_invoke_request` (Impact: 7.5 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 132`, `args: 35`, `func_start: 8`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 23`, `dead_code: 2`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 76`, `test: 21`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ACCESS_CONTROL_EXPOSE_HEADERS, http::
  header::
    ACCESS_CONTROL_ALLOW_HEADERS, StateManager, Method, webview::InvokeRequest, http::header::*, UriSchemeProtocolHandler, tauri_macros::generate_context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/tauri-cli/src/helpers/http.rs` (RUST) | Magnitude: 9.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 4, decorators: 2, args: 1
- `crates/tauri/src/tray/plugin.rs` (RUST) | Magnitude: 285.18 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 156, safety: 60, generics: 53, structural_boundaries: 48
- `crates/tauri-cli/src/helpers/cargo.rs` (RUST) | Magnitude: 70.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 66, safety: 35, api: 16, structural_boundaries: 15
- `crates/tauri-cli/src/mobile/android/android_studio_script.rs` (RUST) | Magnitude: 233.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 31, branch: 30, safety: 17
- `crates/tauri-runtime-wry/src/dialog/windows.rs` (RUST) | Magnitude: 45.06 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 26, safety: 12, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/tauri-macros/src/command/handler.rs` (RUST) | Magnitude: 104.9 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 50, state_mutation: 28, branch: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL) | Magnitude: 815.6 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 300, branch: 228, state_mutation: 226, io: 126

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/api/rollup.config.ts` (TYPESCRIPT) | Magnitude: 5.71 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 20, args: 14, func_start: 12
- `crates/tauri-cli/src/add.rs` (RUST) | Magnitude: 20.56 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 6, safety: 5, api: 5
- `crates/tauri-runtime-wry/src/webview.rs` (RUST) | Magnitude: 30.76 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, api: 11, encapsulation: 11
- `crates/tauri-cli/src/helpers/config.rs` (RUST) | Magnitude: 246.94 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 269, structural_boundaries: 56, state_mutation: 46, branch: 39
- `crates/tauri-build/src/codegen/context.rs` (RUST) | Magnitude: 111.1 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 92, branch: 27, doc: 23, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/tauri-bundler/src/bundle/windows/msi/install-task.ps1` (POWERSHELL) | Magnitude: 12.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 7, closures: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/tauri-build/src/acl.rs` (RUST) | Magnitude: 349.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 76, branch: 71, doc: 38
- `crates/tauri/src/menu/builders/normal.rs` (RUST) | Magnitude: 31.48 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, doc: 13, safety: 9, generics: 9
- `crates/tauri/src/event/listener.rs` (RUST) | Magnitude: 196.72 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 64, safety: 48, args: 35
- `packages/api/src/event.ts` (TYPESCRIPT) | Magnitude: 7.46 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, doc: 27, structural_boundaries: 25, concurrency: 14
- `crates/tauri-utils/src/acl/schema.rs` (RUST) | Magnitude: 186.06 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 255, structural_boundaries: 71, safety: 56, branch: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/tauri-cli/src/interface/rust/desktop.rs` (RUST) | Magnitude: 542.68 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 93, branch: 78, safety: 77
- `examples/api/src/views/WebRTC.svelte` (HTML) | Magnitude: 30.9 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, func_start: 11, branch: 7, structural_boundaries: 7
- `crates/tauri/src/protocol/asset.rs` (RUST) | Magnitude: 308.2 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 66, branch: 53, state_mutation: 48
- `crates/tauri/src/menu/builders/menu.rs` (RUST) | Magnitude: 424.12 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 378, doc: 214, args: 86, api: 80
- `crates/tauri/src/window/scripts/drag.js` (JAVASCRIPT) | Magnitude: 45.24 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, branch: 27, safety: 19, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/tauri/mobile/ios-api/Sources/Tauri/UiUtils.swift` (SWIFT) | Magnitude: 23.3 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, branch: 5, ui_framework: 3, structural_boundaries: 2
- `examples/multiwindow/main.rs` (RUST) | Magnitude: 17.94 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, args: 5, ui_framework: 5, structural_boundaries: 3
- `examples/splashscreen/main.rs` (RUST) | Magnitude: 6.8 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, safety_bypasses: 5, ui_framework: 5, args: 2
- `examples/isolation/main.rs` (RUST) | Magnitude: 12.26 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, ui_framework: 4, branch: 2, args: 2
- `examples/helloworld/main.rs` (RUST) | Magnitude: 7.36 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, ui_framework: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/api/src/webviewWindow.ts` (TYPESCRIPT) | Magnitude: 13.18 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 48, concurrency: 47, branch: 30
- `bench/tests/cpu_intensive/public/worker.js` (JAVASCRIPT) | Magnitude: 44.04 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 15, structural_boundaries: 9, branch: 7
- `packages/api/src/image.ts` (TYPESCRIPT) | Magnitude: 8.03 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 52, concurrency: 30, structural_boundaries: 20, args: 12
- `crates/tauri-utils/src/pattern/isolation.js` (JAVASCRIPT) | Magnitude: 86.24 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, doc: 20, concurrency: 18, branch: 17
- `examples/api/src/views/App.svelte` (HTML) | Magnitude: 62.56 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, branch: 11, structural_boundaries: 11, concurrency: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/tauri-cli/src/mobile/ios/xcode_script.rs` (RUST) | Magnitude: 67.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 159, branch: 39, structural_boundaries: 37, state_mutation: 13
- `crates/tauri-plugin/src/lib.rs` (RUST) | Magnitude: 17.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 9, structural_boundaries: 4, api: 2, doc: 2
- `examples/api/src/views/Tray.svelte` (HTML) | Magnitude: 19.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, decorators: 13, args: 10
- `crates/tauri-utils/src/pattern/mod.rs` (RUST) | Magnitude: 12.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, doc: 1, decorators: 1
- `crates/tauri-macos-sign/src/certificate.rs` (RUST) | Magnitude: 22.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 10, api: 10, encapsulation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/tauri-cli/templates/mobile/ios/Podfile` (RUBY) | Magnitude: 7.06 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, closures: 5, args: 3, duplicate_logic: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/tauri-utils/src/config.rs` -> Churn: **88.49%** | Cog Load: 4.0984% | Debt: 99.9673%
- `crates/tauri-runtime-wry/src/lib.rs` -> Churn: **79.46%** | Cog Load: 14.1789% | Debt: 99.9293%
- `crates/tauri/src/app.rs` -> Churn: **58.06%** | Cog Load: 28.0113% | Debt: 99.6691%
- `crates/tauri-cli/src/helpers/config.rs` -> Churn: **57.17%** | Cog Load: 16.6202% | Debt: 53.5995%
- `crates/tauri/src/window/mod.rs` -> Churn: **51.24%** | Cog Load: 6.4735% | Debt: 97.3072%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/tauri-utils/src/acl/resolved.rs` -> **Thomas Eizinger** (100.0% isolated ownership) | Magnitude: 615.46
- `crates/tauri/src/manager/mod.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 571.9
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Lucas Fernandes Nogueira** (100.0% isolated ownership) | Magnitude: 492.66
- `crates/tauri-cli/src/migrate/migrations/v1/frontend.rs` -> **Lucas Fernandes Nogueira** (100.0% isolated ownership) | Magnitude: 481.96
- `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` -> **Fabian-Lars** (100.0% isolated ownership) | Magnitude: 378.92

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginHandle.kt` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 86.563%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/tauri/mobile/android/src/main/java/app/tauri/annotation/Permission.kt` -> **Severity: 1.822** (Embedded: 0.0228 * Error Risk: 80.0%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Severity: 0.508** (Embedded: 0.0064 * Error Risk: 79.5208%)
- `packages/api/src/menu/checkMenuItem.ts` -> **Severity: 0.419** (Embedded: 0.0079 * Error Risk: 53.3284%)
- `packages/api/src/menu/menuItem.ts` -> **Severity: 0.378** (Embedded: 0.0079 * Error Risk: 48.1259%)
- `packages/api/src/menu/predefinedMenuItem.ts` -> **Severity: 0.364** (Embedded: 0.0079 * Error Risk: 46.3031%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/api/src/menu/base.ts` -> **Severity: 1903.205** (Blast Radius: 34.199 * Doc Risk: 55.6509%)
- `packages/api/src/menu/checkMenuItem.ts` -> **Severity: 746.562** (Blast Radius: 9.289 * Doc Risk: 80.3705%)
- `crates/tauri-cli/src/helpers/template.rs` -> **Severity: 525.2** (Blast Radius: 5.252 * Doc Risk: 100.0%)
- `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift` -> **Severity: 469.0** (Blast Radius: 4.69 * Doc Risk: 100.0%)
- `packages/api/src/menu/menuItem.ts` -> **Severity: 442.826** (Blast Radius: 9.289 * Doc Risk: 47.6721%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
