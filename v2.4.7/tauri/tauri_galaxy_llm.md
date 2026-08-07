# ARCHITECTURAL_BRIEF: tauri
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/tauri` |
| **Timestamp** | `2026-08-07T04:08:25.367486+00:00` |
| **Scan Duration** | `2.09s` |
| **Git Branch** | `dev` |
| **Git Commit** | `b27be063ff3052cb1071ac3ec719cfa104460fa4` |
| **Git Remote** | `https://github.com/tauri-apps/tauri.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 423 malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.882`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 267 | 42.6% |
| file_cluster_0 | 111 | 17.7% |
| file_cluster_13 | 69 | 11.0% |
| file_cluster_16 | 39 | 6.2% |
| file_cluster_4 | 23 | 3.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 16.0 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 24.1 | 15.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.2 | 3.1 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.6 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 86.2 | 8.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.8 | 15.5 | 0.0 |
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

- `new` (@ `crates/tauri-cli/src/interface/rust.rs`) -> Impact: **429.7** | LOC: 1554
- `build_nsis_app_installer` (@ `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs`) -> Impact: **262.2** | LOC: 491
- `usage` (@ `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg`) -> Impact: **255.9** | LOC: 451
- `build_wix_app_installer` (@ `crates/tauri-bundler/src/bundle/windows/msi/mod.rs`) -> Impact: **231.4** | LOC: 468
  * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating the MSI installer. For now the only supported pla...
- `get_config` (@ `crates/tauri-cli/src/mobile/ios/mod.rs`) -> Impact: **230.6** | LOC: 432
- `handle_user_message` (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **182.4** | LOC: 831
- `show_usage_[Truncated]` (@ `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh`) -> Impact: **181.0** | LOC: 311
- `read_source` (@ `crates/tauri-cli/src/icon.rs`) -> Impact: **150.4** | LOC: 368
- `context_codegen` (@ `crates/tauri-codegen/src/context.rs`) -> Impact: **145.1** | LOC: 341
  * *Intent:* /// Build a `tauri::Context` for including in application code.
- `tauri_config_to_bundle_settings` (@ `crates/tauri-cli/src/interface/rust.rs`) -> Impact: **130.8** | LOC: 337

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/tauri/src` | 9 | 1921.3 | 19.19% | 66.13% |
| `crates/tauri-runtime-wry/src` | 4 | 1790.74 | 18.62% | 41.85% |
| `crates/tauri-utils/src` | 12 | 1672.36 | 7.3% | 60.3% |
| `crates/tauri-cli/src` | 12 | 1466.46 | 14.9% | 28.18% |
| `crates/tauri-cli/src/helpers` | 17 | 1392.98 | 15.16% | 32.31% |
| `crates/tauri/src/menu` | 8 | 1323.46 | 5.23% | 15.99% |
| `crates/tauri-cli/src/interface` | 2 | 1220.88 | 12.66% | 34.99% |
| `crates/tauri-utils/src/acl` | 8 | 1085.92 | 6.41% | 60.01% |
| `crates/tauri-cli/src/mobile/ios` | 6 | 1027.22 | 11.78% | 14.63% |
| `crates/tauri/src/webview` | 3 | 991.94 | 14.18% | 58.33% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/tauri-cli/src/error.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/flock.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/plist.rs` -> **100.0%** Exposure
- `crates/tauri-runtime-wry/src/monitor/mod.rs` -> **100.0%** Exposure
- `crates/tauri-runtime/src/dpi.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/tauri-bundler/src/utils/http_utils.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/utils/mod.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/config.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/prompts.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/template.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/tauri/src/test/mock_runtime.rs` -> **110** Orphaned Functions | **65** Duplicates
- `crates/tauri-runtime-wry/src/lib.rs` -> **33** Orphaned Functions | **94** Duplicates
- `crates/tauri-utils/src/config.rs` -> **0** Orphaned Functions | **71** Duplicates
- `crates/tauri-utils/src/config_v1/mod.rs` -> **6** Orphaned Functions | **55** Duplicates
- `crates/tauri/src/lib.rs` -> **25** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`bench/src/run_benchmark.rs`** -> AI Confidence: **99.31%**
2. **`bench/src/utils.rs`** -> AI Confidence: **99.31%**
3. **`crates/tauri-build/src/acl.rs`** -> AI Confidence: **99.31%**
4. **`crates/tauri-build/src/codegen/context.rs`** -> AI Confidence: **99.31%**
5. **`crates/tauri-build/src/lib.rs`** -> AI Confidence: **99.31%**
6. **`crates/tauri-build/src/manifest.rs`** -> AI Confidence: **99.31%**
7. **`crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy.rs`** -> AI Confidence: **99.31%**
8. **`crates/tauri-bundler/src/bundle/linux/debian.rs`** -> AI Confidence: **99.31%**
9. **`crates/tauri-bundler/src/bundle/linux/rpm.rs`** -> AI Confidence: **99.31%**
10. **`crates/tauri-bundler/src/bundle/macos/app.rs`** -> AI Confidence: **99.31%**
11. **`crates/tauri-bundler/src/bundle/macos/ios.rs`** -> AI Confidence: **99.31%**
12. **`crates/tauri-bundler/src/bundle/macos/sign.rs`** -> AI Confidence: **99.31%**
13. **`crates/tauri-bundler/src/bundle/settings.rs`** -> AI Confidence: **99.31%**
14. **`crates/tauri-bundler/src/bundle/windows/nsis/mod.rs`** -> AI Confidence: **99.31%**
15. **`crates/tauri-bundler/src/bundle/windows/util.rs`** -> AI Confidence: **99.31%**
16. **`crates/tauri-cli/src/acl/capability/new.rs`** -> AI Confidence: **99.31%**
17. **`crates/tauri-cli/src/acl/permission/add.rs`** -> AI Confidence: **99.31%**
18. **`crates/tauri-cli/src/acl/permission/ls.rs`** -> AI Confidence: **99.31%**
19. **`crates/tauri-cli/src/acl/permission/new.rs`** -> AI Confidence: **99.31%**
20. **`crates/tauri-cli/src/acl/permission/rm.rs`** -> AI Confidence: **99.31%**
21. **`crates/tauri-cli/src/build.rs`** -> AI Confidence: **99.31%**
22. **`crates/tauri-cli/src/completions.rs`** -> AI Confidence: **99.31%**
23. **`crates/tauri-cli/src/helpers/app_paths.rs`** -> AI Confidence: **99.31%**
24. **`crates/tauri-cli/src/helpers/npm.rs`** -> AI Confidence: **99.31%**
25. **`crates/tauri-cli/src/info/env_system.rs`** -> AI Confidence: **99.31%**
26. **`crates/tauri-cli/src/init.rs`** -> AI Confidence: **99.31%**
27. **`crates/tauri-cli/src/migrate/migrations/v2_beta.rs`** -> AI Confidence: **99.31%**
28. **`crates/tauri-cli/src/migrate/mod.rs`** -> AI Confidence: **99.31%**
29. **`crates/tauri-cli/src/mobile/android/android_studio_script.rs`** -> AI Confidence: **99.31%**
30. **`crates/tauri-cli/src/mobile/android/build.rs`** -> AI Confidence: **99.31%**
31. **`crates/tauri-cli/src/mobile/android/mod.rs`** -> AI Confidence: **99.31%**
32. **`crates/tauri-cli/src/mobile/ios/mod.rs`** -> AI Confidence: **99.31%**
33. **`crates/tauri-cli/src/mobile/ios/xcode_script.rs`** -> AI Confidence: **99.31%**
34. **`crates/tauri-cli/src/mobile/mod.rs`** -> AI Confidence: **99.31%**
35. **`crates/tauri-macros/src/menu.rs`** -> AI Confidence: **99.31%**
36. **`crates/tauri-utils/src/config/parse.rs`** -> AI Confidence: **99.31%**
37. **`crates/tauri/src/manager/window.rs`** -> AI Confidence: **99.31%**
38. **`crates/tauri/src/menu/menu.rs`** -> AI Confidence: **99.31%**
39. **`crates/tauri/src/path/plugin.rs`** -> AI Confidence: **99.31%**
40. **`crates/tauri/src/window/plugin.rs`** -> AI Confidence: **99.31%**
41. **`crates/tauri-cli/templates/mobile/android/buildSrc/src/main/kotlin/BuildTask.kt`** -> AI Confidence: **99.31%**
42. **`crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `packages/api/src/core.ts` -> **99.9618%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4393` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginManager.kt` (KOTLIN) -> Cumulative Risk: **710.76**
- **Archetype:** `file_cluster_13` (Distance: 11.662 IQR)
- **Magnitude:** 158.64 | **LOC:** 225 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7748%), State Flux (99.5629%), Concurrency (99.4317%)
- **Heaviest Functions:** `dispatchPluginMessage` (Impact: 16.7), `onActivityCreate` (Impact: 13.5), `runCommand` (Impact: 7.6)

### 2. `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (SHELL) -> Cumulative Risk: **696.37**
- **Archetype:** `file_cluster_4` (Distance: 13.199 IQR)
- **Magnitude:** 325.92 | **LOC:** 328 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `show_usage_[Truncated]` (Impact: 181.0), `Anonymous_Block` (Impact: 5.2), `__global_context__` (Impact: 1.5)

### 3. `packages/api/src/core.ts` (TYPESCRIPT) -> Cumulative Risk: **690.08**
- **Archetype:** `file_cluster_4` (Distance: 12.297 IQR)
- **Magnitude:** 12.12 | **LOC:** 356 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9998%), Secrets Risk (99.9618%)
- **Heaviest Functions:** `constructor` (Impact: 15.4), `cb` (Impact: 6.8), `transformCallback` (Impact: 6.0)

### 4. `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gstreamer.sh` (SHELL) -> Cumulative Risk: **688.45**
- **Archetype:** `file_cluster_8` (Distance: 11.356 IQR)
- **Magnitude:** 163.22 | **LOC:** 166 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 16.4), `Anonymous_Block` (Impact: 16.4), `Anonymous_Block` (Impact: 12.3)

### 5. `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL) -> Cumulative Risk: **601.0**
- **Archetype:** `file_cluster_12` (Distance: 13.908 IQR)
- **Magnitude:** 595.9 | **LOC:** 639 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (96.7693%)
- **Heaviest Functions:** `usage` (Impact: 255.9), `Anonymous_Block` (Impact: 13.6), `Anonymous_Block` (Impact: 12.6)

### 6. `crates/tauri-cli/templates/mobile/android/gradlew` (SHELL) -> Cumulative Risk: **593.19**
- **Archetype:** `file_cluster_8` (Distance: 13.517 IQR)
- **Magnitude:** 217.54 | **LOC:** 186 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 34.7), `Anonymous_Block` (Impact: 18.7), `Anonymous_Block` (Impact: 17.0)

### 7. `crates/tauri-bundler/src/bundle/windows/msi/uninstall-task.ps1` (POWERSHELL) -> Cumulative Risk: **591.95**
- **Archetype:** `file_cluster_8` (Distance: 10.908 IQR)
- **Magnitude:** 8.5 | **LOC:** 24 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9996%), State Flux (99.981%), Documentation (98.2064%)
- **Heaviest Functions:** `Test-Admin` (Impact: 1.2)

### 8. `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` (KOTLIN) -> Cumulative Risk: **588.63**
- **Archetype:** `file_cluster_13` (Distance: 12.723 IQR)
- **Magnitude:** 335.36 | **LOC:** 515 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.825%), Tech Debt (92.0713%), Safety Score (89.8669%)
- **Heaviest Functions:** `requestPermissions` (Impact: 39.0), `getPermissionStates` (Impact: 30.4), `isPermissionDeclared` (Impact: 19.1)

### 9. `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift` (SWIFT) -> Cumulative Risk: **572.13**
- **Archetype:** `file_cluster_0` (Distance: 10.985 IQR)
- **Magnitude:** 126.1 | **LOC:** 158 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.3689%), Documentation (84.9939%), Concurrency (81.7574%)
- **Heaviest Functions:** `invoke` (Impact: 31.7), `runCommand` (Impact: 11.7), `assetUrl` (Impact: 11.5)

### 10. `crates/tauri-cli/src/dev.rs` (RUST) -> Cumulative Risk: **568.57**
- **Archetype:** `file_cluster_0` (Distance: 12.317 IQR)
- **Magnitude:** 237.38 | **LOC:** 372 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.5497%), Concurrency (93.5273%), Verification (80.0%)
- **Heaviest Functions:** `setup` (Impact: 107.2), `on_app_exit` (Impact: 11.6), `kill_before_dev_process` (Impact: 10.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/tauri-runtime-wry/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.447 IQR)
- **Top Global Matches:** file_cluster_0: 13.447, file_cluster_8: 13.612, file_cluster_16: 13.651
- **Magnitude:** 1475.34 | **LOC:** 5354 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 29.4%
- **Risk Profile:** Cognitive Load (13.9848%), Tech Debt (99.9434%)
**Top Internal Functions/Classes:**
  * `handle_user_message` (Impact: 182.4)
  * `handle_event_loop` (Impact: 67.9)
  * `create_window` (Impact: 48.2)
  * `with_config` (Impact: 46.8)
  * `map_from_tao` (Impact: 13.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 580`, `args: 327`, `func_start: 244`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 2`, `state_mutation: 200`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 94`, `orphaned_logic: 33`
* *Architecture:* `api: 97`, `concurrency: 69`, `import: 52`
* *Defense:* `safety: 567`, `doc: 34`, `sync_locks: 66`, `immutability_locks: 38`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tao::
  dpi::
    LogicalPosition, Icon, WindowBuilderExtMacOS, WindowBuilder, windows::Win32::UI::WindowsAndMessaging::AdjustWindowRect, WindowDispatch, wry::WebViewBuilderExtUnix, window::WindowExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/interface/rust.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.079 IQR)
- **Top Global Matches:** file_cluster_0: 13.079, file_cluster_8: 13.11, file_cluster_16: 13.139
- **Magnitude:** 1144.66 | **LOC:** 1895 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (14.4481%), Tech Debt (20.7589%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 429.7)
  * `tauri_config_to_bundle_settings` (Impact: 130.8)
  * `new` (Impact: 52.3)
  * `build_ignore_matcher` (Impact: 47.5)
  * `get_bundle_settings` (Impact: 46.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 244`, `args: 111`, `func_start: 38`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 96`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 67`, `concurrency: 20`, `import: 17`
* *Defense:* `safety: 205`, `doc: 41`, `test: 20`, `sync_locks: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` str::FromStr, MacOsSettings, Context, Size, Manifest, crate::helpers::config::custom_sign_settings, std::process::Command, sync::mpsc::sync_channel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.843 IQR)
- **Top Global Matches:** file_cluster_0: 13.843, file_cluster_16: 14.071, file_cluster_13: 14.155
- **Magnitude:** 924.32 | **LOC:** 4454 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (4.0715%), Tech Debt (99.9758%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 33.9)
  * `add_configured_headers` (Impact: 31.6)
  * `add_configured_headers` (Impact: 29.4)
  * `visit_str` (Impact: 24.3)
  * `deserialize` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 513`, `args: 130`, `func_start: 117`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 122`, `dead_code: 6`, `planned_debt: 6`, `duplicate_logic: 71`
* *Architecture:* `api: 228`, `import: 34`
* *Defense:* `safety: 359`, `doc: 1311`, `test: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` str::FromStr, serde::
  de::Deserializer, fs::read_to_string, std::str::FromStr, Serializer, crate::literal_struct, tokens::*, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.792 IQR)
- **Top Global Matches:** file_cluster_0: 16.792, file_cluster_4: 17.038, file_cluster_13: 17.11
- **Magnitude:** 780.02 | **LOC:** 2606 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (27.852%), Tech Debt (99.6691%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 58.7)
    * *Intent:* #[cfg(not(feature = "wry"))] #[cfg_attr(docsrs, doc(cfg(not(feature = "wry"))))]
  * `on_event_loop_event` (Impact: 32.6)
    * *Intent:* /// use std::{collections::HashMap, sync::Mutex}; /// use tauri::State; /// // here we use Mutex to ...
  * `register_core_plugins` (Impact: 18.2)
  * `init_app_menu` (Impact: 16.5)
    * *Intent:* /// println!("app is ready"); /// } /// RunEvent::WindowEvent { label, event, .. } => { /// println!...
  * `setup` (Impact: 15.5)
    * *Intent:* /// refers to a different `T`. /// /// Managed state can be retrieved by any command handler via the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 253`, `args: 120`, `func_start: 86`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 1`, `state_mutation: 70`, `dead_code: 56`, `planned_debt: 2`, `duplicate_logic: 33`
* *Architecture:* `api: 104`, `concurrency: 191`, `import: 26`
* *Defense:* `safety: 204`, `doc: 844`, `test: 3`, `sync_locks: 39`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tauri::Listener, MSG, TrayIconId, tauri::menu::*, MutexGuard, runtime::
    window::WebviewEvent, TrayIconBuilder, Runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/webview/webview_window.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 19.467 IQR)
- **Top Global Matches:** file_cluster_0: 19.467, file_cluster_11: 19.731, file_cluster_13: 19.754
- **Magnitude:** 609.08 | **LOC:** 2661 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 29.4%
- **Risk Profile:** Cognitive Load (14.0795%), Tech Debt (43.3705%)
**Top Internal Functions/Classes:**
  * `window_features` (Impact: 7.6)
    * *Intent:* /// Forces a theme or uses the system settings if None was provided. ///
  * `transient_for` (Impact: 4.0)
    * *Intent:* /// Sets whether or not the window icon should be hidden from the taskbar.
  * `build` (Impact: 3.7)
    * *Intent:* /// Set a download event handler to be notified when a download is requested or finished. /// /// Re...
  * `icon` (Impact: 3.7)
    * *Intent:* /// Prevent the window from overflowing the working area (e.g. monitor size - taskbar size) /// on c...
  * `parent` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 154`, `args: 161`, `func_start: 141`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 72`, `dead_code: 91`, `duplicate_logic: 10`, `orphaned_logic: 2`
* *Architecture:* `api: 134`, `concurrency: 77`, `import: 23`
* *Defense:* `safety: 116`, `doc: 1238`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tauri_macros::default_runtime, tauri::ipc::CommandScope, Size, runtime::window::CursorIcon, super::DownloadEvent, Effect, sync::Arc, UserAttentionType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config_v1/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.625 IQR)
- **Top Global Matches:** file_cluster_0: 12.625, file_cluster_16: 12.897, file_cluster_8: 13.076
- **Magnitude:** 604.14 | **LOC:** 3166 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.3553%), Tech Debt (99.9896%)
**Top Internal Functions/Classes:**
  * `visit_str` (Impact: 24.2)
    * *Intent:* /// Allowlist for the global shortcut APIs. /// /// See more: https://tauri.app/v1/api/config#global...
  * `deserialize` (Impact: 8.9)
  * `to_features` (Impact: 8.7)
    * *Intent:* /// The user agent for the webview #[serde(alias = "user-agent")]
  * `to_features` (Impact: 7.7)
  * `merge` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 230`, `args: 72`, `func_start: 65`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 76`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 55`, `orphaned_logic: 6`
* *Architecture:* `api: 213`, `import: 9`
* *Defense:* `safety: 162`, `doc: 853`, `test: 8`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` str::FromStr, serde::
  de::Deserializer, fs::read_to_string, Schema, Serializer, Serialize, path::PathBuf, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.908 IQR)
- **Top Global Matches:** file_cluster_12: 13.908, file_cluster_11: 13.949, file_cluster_8: 14.022
- **Magnitude:** 595.9 | **LOC:** 639 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (79.7792%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 255.9)
  * `Anonymous_Block` (Impact: 13.6)
    * *Intent:* # Adding EULA resources
  * `Anonymous_Block` (Impact: 12.6)
    * *Intent:* # Make the top window open itself on mount:
  * `hdiutil_detach_retry` (Impact: 12.3)
  * `Anonymous_Block` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 65`, `args: 42`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 228`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 126`, `concurrency: 6`, `import: 3`
* *Defense:* `safety: 56`, `sync_locks: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` -f, folder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/msi/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.86 IQR)
- **Top Global Matches:** file_cluster_8: 11.86, file_cluster_0: 12.112, file_cluster_17: 12.123
- **Magnitude:** 572.1 | **LOC:** 1142 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (21.9225%), Tech Debt (12.6482%)
**Top Internal Functions/Classes:**
  * `build_wix_app_installer` (Impact: 231.4)
    * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating...
  * `generate_resource_data` (Impact: 46.6)
    * *Intent:* /// Generates the data required for the resource bundling on wix
  * `convert_version` (Impact: 23.5)
    * *Intent:* // WiX requires versions to be numeric only in a `major.minor.patch.build` format
  * `run_candle` (Impact: 21.2)
    * *Intent:* /// Runs the Candle.exe executable for Wix. Candle parses the wxs file and generates the code for bu...
  * `generate_binaries_data` (Impact: 18.3)
    * *Intent:* /// Generates the data required for the external binaries and extra binaries bundling.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 201`, `args: 45`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 98`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 5`, `import: 8`
* *Defense:* `safety: 60`, `doc: 31`, `test: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WIX_OUTPUT_FOLDER_NAME, File, WIX_UPDATER_OUTPUT_FOLDER_NAME, Settings, try_sign, handlebars::html_escape, http_utils::download_and_verify, regex::Regex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/window/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.578 IQR)
- **Top Global Matches:** file_cluster_0: 13.578, file_cluster_16: 13.606, file_cluster_8: 13.774
- **Magnitude:** 568.42 | **LOC:** 2471 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (6.4735%), Tech Debt (97.3072%)
**Top Internal Functions/Classes:**
  * `build_internal` (Impact: 38.9)
  * `set_menu` (Impact: 12.3)
  * `remove_menu` (Impact: 12.0)
  * `is_menu_visible` (Impact: 11.8)
  * `hide_menu` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 197`, `args: 150`, `func_start: 115`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 15`
* *Architecture:* `api: 119`, `concurrency: 30`, `import: 18`
* *Defense:* `safety: 182`, `doc: 526`, `test: 2`, `sync_locks: 7`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tauri_macros::default_runtime, Size, WindowBuilder, Effect, WindowDispatch, MenuId, Hasher, sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/test/mock_runtime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.938 IQR)
- **Top Global Matches:** file_cluster_0: 13.938, file_cluster_8: 14.067, file_cluster_16: 14.154
- **Magnitude:** 568.32 | **LOC:** 1400 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (7.2144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 21.8)
  * `send_message` (Impact: 7.7)
  * `create_window` (Impact: 6.4)
    * *Intent:* /// Create a new webview window.
  * `create_window` (Impact: 6.4)
  * `create_window` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 99`, `args: 210`, `func_start: 205`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 53`, `planned_debt: 4`, `duplicate_logic: 65`, `orphaned_logic: 110`
* *Architecture:* `api: 9`, `concurrency: 33`, `import: 6`
* *Defense:* `safety: 349`, `doc: 4`, `sync_locks: 16`, `immutability_locks: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Icon, Size, WindowBuilder, WindowEventId, WindowDispatch, Ordering, UserAttentionType, collections::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.73 IQR)
- **Top Global Matches:** file_cluster_8: 11.73, file_cluster_0: 11.822, file_cluster_17: 11.827
- **Magnitude:** 467.98 | **LOC:** 891 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (15.5869%), Tech Debt (8.5834%)
**Top Internal Functions/Classes:**
  * `build_nsis_app_installer` (Impact: 262.2)
  * `generate_resource_data` (Impact: 30.8)
  * `bundle_project` (Impact: 28.0)
    * *Intent:* /// Runs all of the commands to build the NSIS installer. /// Returns a vector of PathBuf that shows...
  * `generate_binaries_data` (Impact: 15.6)
  * `get_and_extract_nsis` (Impact: 13.4)
    * *Intent:* // Gets NSIS and verifies the download via Sha1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 141`, `args: 45`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 41`, `dead_code: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 1`, `import: 8`
* *Defense:* `safety: 69`, `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WebviewInstallMode, the system default path
    None, fs, Settings, std::io::BufWriter, tauri_utils::display_path, NSIS_UPDATER_OUTPUT_FOLDER_NAME, try_sign...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/menu/plugin.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.636 IQR)
- **Top Global Matches:** file_cluster_0: 12.636, file_cluster_16: 12.706, file_cluster_8: 12.723
- **Magnitude:** 445.2 | **LOC:** 927 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.85%), Tech Debt (29.0521%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 34.8)
  * `insert` (Impact: 22.6)
  * `create_item` (Impact: 21.9)
  * `create_item` (Impact: 21.5)
  * `popup` (Impact: 21.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 173`, `args: 51`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `duplicate_logic: 5`, `orphaned_logic: 1`
* *Architecture:* `api: 21`, `concurrency: 8`, `import: 6`
* *Defense:* `safety: 215`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Channel, crate::
  command, Serialize, plugin::Builder, ResourceTable, ipc::channel::JavaScriptChannelId, tauri_runtime::dpi::Position, Runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/ios/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.213 IQR)
- **Top Global Matches:** file_cluster_0: 12.213, file_cluster_8: 12.329, file_cluster_17: 12.361
- **Magnitude:** 444.86 | **LOC:** 699 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.2312%), Tech Debt (29.3741%)
**Top Internal Functions/Classes:**
  * `get_config` (Impact: 230.6)
  * `synchronize_project_config` (Impact: 86.9)
  * `simulator_prompt` (Impact: 24.1)
  * `ensure_ios_runtime_installed` (Impact: 13.9)
  * `signing_from_env` (Impact: 13.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 80`, `args: 38`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 11`, `dead_code: 3`, `orphaned_logic: 8`
* *Architecture:* `api: 16`, `import: 8`
* *Defense:* `safety: 96`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` str::FromStr, relativize_path, teams::find_development_teams, sublime_fuzzy::best_match, clap::Parser, ErrorExt, std::
  env::set_var, tauri_utils::resources::ResourcePaths...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/manager/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.036 IQR)
- **Top Global Matches:** file_cluster_0: 12.036, file_cluster_16: 12.221, file_cluster_8: 12.317
- **Magnitude:** 403.6 | **LOC:** 1029 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.5398%), Tech Debt (76.2199%)
**Top Internal Functions/Classes:**
  * `get_asset` (Impact: 33.2)
  * `emit_to` (Impact: 24.9)
  * `filter_target` (Impact: 15.3)
  * `replace_csp_nonce` (Impact: 14.6)
  * `check_get_url` (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 125`, `args: 61`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 61`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 55`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 88`, `doc: 28`, `test: 15`, `sync_locks: 16`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tauri_macros::default_runtime, CspHash, Listeners, Context, event::EmitArgs, Wry, Assets, collections::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/icon.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.517 IQR)
- **Top Global Matches:** file_cluster_8: 12.517, file_cluster_13: 12.604, file_cluster_0: 12.644
- **Magnitude:** 394.14 | **LOC:** 987 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (10.6373%), Tech Debt (8.5051%)
**Top Internal Functions/Classes:**
  * `read_source` (Impact: 150.4)
  * `apply_round_mask` (Impact: 56.6)
  * `png` (Impact: 38.4)
  * `content_bounds` (Impact: 21.9)
  * `resize_asset` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 98`, `args: 19`, `func_start: 11`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 3`, `import: 8`
* *Defense:* `safety: 39`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` str::FromStr, File, resvg::tiny_skia, ExtendedColorType, open, clap::Parser, sync::Arc, ErrorExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.539 IQR)
- **Top Global Matches:** file_cluster_0: 16.539, file_cluster_13: 16.764, file_cluster_11: 16.902
- **Magnitude:** 377.34 | **LOC:** 1255 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (11.5823%), Tech Debt (99.9876%)
**Top Internal Functions/Classes:**
  * `features_are_documented` (Impact: 9.2)
    * *Intent:* /// Emits an event to all [targets](EventTarget) based on the given filter. /// /// # Examples /// `...
  * `encode` (Impact: 6.8)
  * `webview_windows` (Impact: 5.9)
  * `aliased_features_exist` (Impact: 5.8)
  * `get_webview_window` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 200`, `args: 92`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 43`, `dead_code: 31`, `planned_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 25`
* *Architecture:* `api: 84`, `concurrency: 35`, `import: 45`
* *Defense:* `safety: 86`, `doc: 444`, `test: 13`, `sync_locks: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Builder, LogicalUnit, fs::read_to_string, http, self::window::WindowBuilder, WebviewUrl, UriSchemeResponder, Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/migrate/migrations/v1/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.938 IQR)
- **Top Global Matches:** file_cluster_8: 10.938, file_cluster_0: 11.23, file_cluster_17: 11.406
- **Magnitude:** 348.16 | **LOC:** 1257 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.8343%), Tech Debt (12.4958%)
**Top Internal Functions/Classes:**
  * `migrate_config` (Impact: 49.2)
  * `allowlist_to_permissions` (Impact: 44.1)
  * `migrate` (Impact: 26.7)
  * `process_security` (Impact: 25.1)
  * `process_updater` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 116`, `args: 51`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 70`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 65`, `test: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` serde_json::Map, Result, crate::error::Context, HashSet, fs, path::Path, tauri_utils::acl::
  capability::Capability, std::
  collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.723 IQR)
- **Top Global Matches:** file_cluster_13: 12.723, file_cluster_0: 12.986, file_cluster_11: 12.994
- **Magnitude:** 335.36 | **LOC:** 515 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.4127%), Tech Debt (92.0713%)
**Top Internal Functions/Classes:**
  * `requestPermissions` (Impact: 39.0)
  * `getPermissionStates` (Impact: 30.4)
  * `isPermissionDeclared` (Impact: 19.1)
  * `getPermissionStringsForAliases` (Impact: 10.6)
  * `checkPermissions` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 76`, `args: 35`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 84`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 23`, `concurrency: 12`, `import: 21`
* *Defense:* `safety: 4`, `doc: 46`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00639
  * `Imports (Out-Degree: 8):` app.tauri.Logger, app.tauri.FsUtils, app.tauri.annotation.InvokeArg, app.tauri.annotation.TauriPlugin, android.content.Intent, androidx.core.app.ActivityCompat, android.webkit.WebView, app.tauri.annotation.ActivityCallback...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `crates/tauri/src/manager/webview.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.314 IQR)
- **Top Global Matches:** file_cluster_0: 11.314, file_cluster_8: 11.428, file_cluster_16: 11.485
- **Magnitude:** 334.1 | **LOC:** 740 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.2307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare_webview` (Impact: 102.0)
  * `prepare_pending_webview` (Impact: 93.4)
  * `on_webview_event` (Impact: 19.3)
  * `initialization_script` (Impact: 18.7)
  * `attach_webview` (Impact: 10.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 120`, `args: 30`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `api: 26`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 70`, `doc: 10`, `test: 6`, `sync_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ipc::InvokeHandler, UriSchemeContext, webview::PageLoadPayload, sync::Arc, collections::HashMap, Scopes, Mutex, UriSchemeResponder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.07 IQR)
- **Top Global Matches:** file_cluster_0: 12.07, file_cluster_8: 12.102, file_cluster_13: 12.185
- **Magnitude:** 334.08 | **LOC:** 623 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 54.5%
- **Risk Profile:** Cognitive Load (16.3486%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `ensure_init` (Impact: 64.1)
  * `use_network_address_for_dev_url` (Impact: 45.6)
  * `env_vars` (Impact: 18.3)
  * `local_ip_address` (Impact: 18.0)
  * `get_app` (Impact: 17.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 102`, `args: 47`, `func_start: 21`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 32`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `api: 17`, `concurrency: 10`, `import: 15`
* *Defense:* `safety: 71`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Options, ffi::OsString, IpAddr, str::FromStr, Ipv4Addr, fs::read_to_string, ExitStatus, heck::ToSnekCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.199 IQR)
- **Top Global Matches:** file_cluster_4: 13.199, file_cluster_11: 13.346, file_cluster_0: 13.431
- **Magnitude:** 325.92 | **LOC:** 328 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (22.1872%)
**Top Internal Functions/Classes:**
  * `show_usage_[Truncated]` (Impact: 181.0)
  * `Anonymous_Block` (Impact: 5.2)
  * `__global_context__` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 53`, `args: 10`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 107`, `dead_code: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 80`, `api: 13`, `concurrency: 13`
* *Defense:* `safety: 12`, `test: 2`, `sync_locks: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/interface/rust/desktop.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.332 IQR)
- **Top Global Matches:** file_cluster_17: 13.332, file_cluster_4: 13.35, file_cluster_8: 13.487
- **Magnitude:** 321.98 | **LOC:** 423 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (65.3821%), Tech Debt (35.3662%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 50.7)
  * `run_dev` (Impact: 45.1)
  * `cargo_command` (Impact: 36.7)
  * `build_production_app` (Impact: 16.9)
  * `rename_app` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 93`, `args: 30`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 69`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 32`, `import: 8`
* *Defense:* `safety: 77`, `sync_locks: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Options, Win32::
      Foundation::CloseHandle, ptr, ExitStatus, Ordering, ErrorExt, GENERIC_WRITE, System::Console::
        GetConsoleScreenBufferInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/ios/build.rs` (RUST | Tier 1 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.626 IQR)
- **Top Global Matches:** file_cluster_0: 12.626, file_cluster_13: 12.801, file_cluster_8: 12.811
- **Magnitude:** 318.66 | **LOC:** 560 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 47.4%
- **Risk Profile:** Cognitive Load (20.9687%), Tech Debt (11.1784%)
**Top Internal Functions/Classes:**
  * `run_build` (Impact: 113.7)
  * `run` (Impact: 84.8)
  * `auth_credentials_from_env` (Impact: 6.1)
  * `from_str` (Impact: 4.4)
  * `pre_xcode_15_4_name` (Impact: 3.8)
    * *Intent:* /// Xcode 15.4 deprecated these names (in this case we should use the Display impl).
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 98`, `args: 14`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 19`, `import: 7`
* *Defense:* `safety: 63`, `doc: 24`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Options, TargetDevice, BuildConfig, target::call_for_targets_with_fallback, write_options, fs, inject_resources, ErrorExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/plugin.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.719 IQR)
- **Top Global Matches:** file_cluster_0: 17.719, file_cluster_4: 17.868, file_cluster_11: 17.904
- **Magnitude:** 313.36 | **LOC:** 1062 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (24.7435%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 12.7)
    * *Intent:* /// .on_event(|app_handle, event| { /// match event { /// RunEvent::ExitRequested { api, .. } => { /...
  * `deserialize` (Impact: 6.7)
  * `on_navigation` (Impact: 6.5)
  * `extend_api` (Impact: 6.5)
    * *Intent:* /// Plugin struct that is returned by the [`Builder`]. Should only be constructed through the builde...
  * `drop` (Impact: 4.2)
    * *Intent:* /// Callback invoked when the event loop receives a new event. /// /// # Examples /// /// ```rust //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 116`, `args: 89`, `func_start: 52`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `dead_code: 36`, `planned_debt: 2`, `duplicate_logic: 34`, `orphaned_logic: 4`
* *Architecture:* `api: 39`, `concurrency: 74`, `import: 17`
* *Defense:* `safety: 90`, `doc: 434`, `sync_locks: 1`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tauri_macros::default_runtime, webview::PageLoadPayload, std::path::PathBuf, tauri::plugin::Builder, sync::Arc, collections::HashMap, Serializer, serde::
  de::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/linux/debian.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.869 IQR)
- **Top Global Matches:** file_cluster_13: 12.869, file_cluster_8: 12.926, file_cluster_17: 13.071
- **Magnitude:** 309.9 | **LOC:** 404 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.6456%), Tech Debt (10.5612%)
**Top Internal Functions/Classes:**
  * `generate_control_file` (Impact: 95.7)
    * *Intent:* /// Generates the debian control file and stores it under the `control_dir`.
  * `bundle_project` (Impact: 35.2)
    * *Intent:* /// Bundles the project. /// Returns a vector of PathBuf that shows where the DEB was created.
  * `generate_data` (Impact: 29.5)
    * *Intent:* /// Generate the debian data folders and files.
  * `generate_md5sums` (Impact: 25.4)
    * *Intent:* /// Create an `md5sums` file in the `control_dir` containing the MD5 checksums /// for each file wit...
  * `generate_scripts` (Impact: 16.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 90`, `args: 21`, `func_start: 9`
* *Risk/State:* `state_mutation: 57`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 2`, `import: 6`
* *Defense:* `safety: 36`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File, Settings, ErrorExt, flate2::write::GzEncoder, Write, error::Context, tar::HeaderMode, Compression...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/tauri-cli/src/helpers/http.rs` (RUST) | Magnitude: 5.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 4, decorators: 2, args: 1
- `crates/tauri-cli/src/mobile/ios/xcode_script.rs` (RUST) | Magnitude: 63.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 159, branch: 39, structural_boundaries: 37, state_mutation: 13
- `crates/tauri/src/tray/plugin.rs` (RUST) | Magnitude: 122.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 156, safety: 60, generics: 53, structural_boundaries: 48
- `crates/tauri-cli/src/helpers/cargo.rs` (RUST) | Magnitude: 59.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 66, safety: 35, api: 16, structural_boundaries: 15
- `crates/tauri-cli/src/mobile/android/android_studio_script.rs` (RUST) | Magnitude: 95.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 31, branch: 30, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/tauri-macros/src/command/handler.rs` (RUST) | Magnitude: 84.0 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 50, state_mutation: 28, branch: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL) | Magnitude: 595.9 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 300, branch: 236, state_mutation: 228, io: 126

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/tauri-cli/src/add.rs` (RUST) | Magnitude: 20.56 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 6, safety: 5, api: 5
- `crates/tauri-runtime-wry/src/webview.rs` (RUST) | Magnitude: 30.76 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, api: 11, encapsulation: 11
- `crates/tauri-cli/src/helpers/config.rs` (RUST) | Magnitude: 190.44 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 269, structural_boundaries: 56, state_mutation: 46, branch: 37
- `crates/tauri-build/src/codegen/context.rs` (RUST) | Magnitude: 64.3 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 92, branch: 27, doc: 23, structural_boundaries: 18
- `crates/tauri-cli/src/info/packages_nodejs.rs` (RUST) | Magnitude: 80.8 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 31, branch: 24, safety: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/tauri-bundler/src/bundle/windows/msi/install-task.ps1` (POWERSHELL) | Magnitude: 12.58 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 7, closures: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/tauri-build/src/acl.rs` (RUST) | Magnitude: 213.46 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 76, branch: 70, doc: 38
- `crates/tauri/mobile/android/src/main/java/app/tauri/annotation/TauriPlugin.kt` (KOTLIN) | Magnitude: 13.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 2, class_start: 1, decorators: 1
- `crates/tauri/src/menu/builders/normal.rs` (RUST) | Magnitude: 26.78 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, doc: 13, safety: 9, generics: 9
- `packages/api/src/event.ts` (TYPESCRIPT) | Magnitude: 5.71 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, doc: 27, structural_boundaries: 25, concurrency: 14
- `crates/tauri/src/event/listener.rs` (RUST) | Magnitude: 147.02 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 64, safety: 48, args: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/tauri-cli/src/interface/rust/desktop.rs` (RUST) | Magnitude: 321.98 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 93, branch: 78, safety: 77
- `examples/api/src/views/WebRTC.svelte` (HTML) | Magnitude: 33.3 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, func_start: 11, branch: 7, structural_boundaries: 7
- `crates/tauri/src/protocol/asset.rs` (RUST) | Magnitude: 188.0 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 66, branch: 53, state_mutation: 48
- `crates/tauri/src/menu/builders/menu.rs` (RUST) | Magnitude: 287.62 | Delta: **0.234 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 378, doc: 214, args: 86, api: 80
- `crates/tauri/src/window/scripts/drag.js` (JAVASCRIPT) | Magnitude: 40.04 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, branch: 27, safety: 19, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/tauri/mobile/ios-api/Sources/Tauri/UiUtils.swift` (SWIFT) | Magnitude: 12.9 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, branch: 5, structural_boundaries: 3, ui_framework: 3
- `examples/multiwindow/main.rs` (RUST) | Magnitude: 12.84 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, ui_framework: 5, structural_boundaries: 3, args: 3
- `examples/splashscreen/main.rs` (RUST) | Magnitude: 6.8 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, safety_bypasses: 5, ui_framework: 5, args: 2
- `examples/isolation/main.rs` (RUST) | Magnitude: 7.06 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, ui_framework: 4, args: 2, func_start: 2
- `examples/helloworld/main.rs` (RUST) | Magnitude: 7.36 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, ui_framework: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/api/src/webviewWindow.ts` (TYPESCRIPT) | Magnitude: 12.25 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 48, concurrency: 47, branch: 30
- `packages/api/src/image.ts` (TYPESCRIPT) | Magnitude: 7.21 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 52, concurrency: 30, structural_boundaries: 20, args: 11
- `crates/tauri-utils/src/pattern/isolation.js` (JAVASCRIPT) | Magnitude: 64.14 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, doc: 20, concurrency: 18, branch: 17
- `examples/api/src/views/App.svelte` (HTML) | Magnitude: 56.96 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, branch: 11, structural_boundaries: 11, concurrency: 10
- `crates/tauri/src/state.rs` (RUST) | Magnitude: 176.9 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 199, structural_boundaries: 75, concurrency: 60, generics: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/tauri-plugin/src/lib.rs` (RUST) | Magnitude: 17.32 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: decorators: 9, structural_boundaries: 4, api: 2, doc: 2
- `examples/api/src/views/Tray.svelte` (HTML) | Magnitude: 17.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 18, decorators: 13, args: 10
- `crates/tauri-utils/src/pattern/mod.rs` (RUST) | Magnitude: 12.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, doc: 1, decorators: 1
- `crates/tauri-macos-sign/src/certificate.rs` (RUST) | Magnitude: 22.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 10, api: 10, encapsulation: 10
- `crates/tauri-cli/src/acl/capability/new.rs` (RUST) | Magnitude: 71.88 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, safety: 39, branch: 30, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/tauri-cli/templates/mobile/ios/Podfile` (RUBY) | Magnitude: 7.06 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 8, closures: 5, args: 3, duplicate_logic: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/tauri-utils/src/config.rs` -> Churn: **86.2%** | Cog Load: 4.0715% | Debt: 99.9758%
- `crates/tauri-runtime-wry/src/lib.rs` -> Churn: **79.46%** | Cog Load: 13.9848% | Debt: 99.9434%
- `crates/tauri/src/app.rs` -> Churn: **58.06%** | Cog Load: 27.852% | Debt: 99.6691%
- `crates/tauri-cli/src/helpers/config.rs` -> Churn: **53.49%** | Cog Load: 16.1448% | Debt: 53.5995%
- `crates/tauri/src/window/mod.rs` -> Churn: **51.24%** | Cog Load: 6.4735% | Debt: 97.3072%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/tauri/src/manager/mod.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 403.6
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Lucas Fernandes Nogueira** (100.0% isolated ownership) | Magnitude: 335.36
- `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` -> **Fabian-Lars** (100.0% isolated ownership) | Magnitude: 325.92
- `crates/tauri-utils/src/acl/resolved.rs` -> **Thomas Eizinger** (100.0% isolated ownership) | Magnitude: 247.66
- `crates/tauri-utils/src/acl/build.rs` -> **Sebastian Neubauer** (100.0% isolated ownership) | Magnitude: 237.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginHandle.kt` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 86.563%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/tauri/mobile/android/src/main/java/app/tauri/annotation/Permission.kt` -> **Severity: 1.822** (Embedded: 0.0228 * Error Risk: 80.0%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/PermissionHelper.kt` -> **Severity: 0.6** (Embedded: 0.0081 * Error Risk: 74.2025%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Severity: 0.574** (Embedded: 0.0064 * Error Risk: 89.8669%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/JSObject.kt` -> **Severity: 0.517** (Embedded: 0.0064 * Error Risk: 80.9421%)
- `packages/api/src/menu/checkMenuItem.ts` -> **Severity: 0.419** (Embedded: 0.0079 * Error Risk: 53.3284%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/api/src/menu/base.ts` -> **Severity: 1822.236** (Blast Radius: 34.199 * Doc Risk: 53.2833%)
- `packages/api/src/menu/checkMenuItem.ts` -> **Severity: 682.364** (Blast Radius: 9.289 * Doc Risk: 73.4594%)
- `crates/tauri-cli/src/helpers/template.rs` -> **Severity: 481.612** (Blast Radius: 5.252 * Doc Risk: 91.7007%)
- `packages/api/src/menu/menuItem.ts` -> **Severity: 449.578** (Blast Radius: 9.289 * Doc Risk: 48.399%)
- `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift` -> **Severity: 398.621** (Blast Radius: 4.69 * Doc Risk: 84.9939%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
