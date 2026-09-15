# ARCHITECTURAL_BRIEF: tauri
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tauri-apps/tauri` |
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
| Total Artifacts | 1064 |
| Analyzed Artifacts (Scanned) | 682 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 382 |
| Total LOC | 85489 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 64.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7833 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1488 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3783 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 317 | 71594 | 46.5% |
| MARKDOWN | 73 | 0 | 10.7% |
| JSON | 57 | 2512 | 8.4% |
| KOTLIN | 42 | 1961 | 6.2% |
| PLAINTEXT | 39 | 0 | 5.7% |
| JAVASCRIPT | 34 | 1013 | 5.0% |
| HTML | 31 | 2477 | 4.5% |
| TYPESCRIPT | 27 | 3525 | 4.0% |
| XML | 24 | 2 | 3.5% |
| SWIFT | 17 | 761 | 2.5% |
| SHELL | 5 | 1055 | 0.7% |
| CSS | 3 | 133 | 0.4% |
| GROOVY | 3 | 60 | 0.4% |
| OBJECTIVE-C | 3 | 14 | 0.4% |
| YAML | 3 | 264 | 0.4% |
| POWERSHELL | 2 | 34 | 0.3% |
| BATCH | 1 | 66 | 0.1% |
| RUBY | 1 | 18 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z -1.28; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Large Core Modules 17%, Generic / Templated Code Files 7%, Defensive Guards Files 6%, State Mutators Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 568 | 83.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 112 | 16.4% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 382*

**Composition by Extension & Reason:**
- `.png`: 79x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 34x Excluded (Unsupported Extension: '.toml'), 26x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 4x Excluded (Unsupported Extension: '.crate-manifest')
- `.yml`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2402 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 4031 LOC)
- `.nsh`: 24x Unsupported Format (.nsh)
- `.0`: 13x Excluded (Unsupported Extension: '.0')
- `.sh`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 12x Excluded (Unsupported Extension: '.snap')
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 3877 LOC), 1x Excluded (Massive Static Asset Blob: 3109 LOC)
- `.ico`: 7x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 581 LOC)
- `.rs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Statistical Anomaly (Z-Score: -4.62 < -4.55)
- `.html`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 5x Excluded (Unsupported Extension: '.pro')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.0 | 5.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 34.0 | 45.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.7 | 4.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 2.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 76.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.5 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 88.1 | 7.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 48.7 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4124 | 290 | 13 | `crates/tauri-runtime-wry/src/lib.rs` |
| cleanup | 39 | 22 | 0 | `crates/tauri-runtime-wry/src/lib.rs` |
| guards | 2517 | 310 | 12 | `crates/tauri-runtime-wry/src/lib.rs` |
| danger | 2001 | 235 | 8 | `crates/tauri-runtime-wry/src/lib.rs` |
| concurrency | 1804 | 131 | 6 | `packages/api/src/window.ts` |
| connectivity | 4733 | 354 | 15 | `crates/tauri-utils/src/config.rs` |
| io | 694 | 133 | 2 | `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` |
| crypto | 0 | 0 | 0 | - |
| ipc | 36 | 26 | 0 | `crates/tauri-macros/src/command/wrapper.rs` |
| time | 31 | 19 | 0 | `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` |
| serialization | 152 | 63 | 0 | `crates/tauri-utils/src/config.rs` |
| regex | 38 | 15 | 0 | `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` |
| events | 542 | 138 | 2 | `crates/tauri-runtime-wry/src/lib.rs` |
| tests | 817 | 80 | 2 | `crates/tauri-utils/src/config.rs` |
| docs | 12457 | 245 | 24 | `crates/tauri-utils/src/config.rs` |
| debt | 576 | 117 | 1 | `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` |
| mutation | 11681 | 395 | 47 | `crates/tauri-runtime-wry/src/lib.rs` |
| dead_code | 1705 | 275 | 4 | `crates/tauri/src/webview/webview_window.rs` |
| credential | 9 | 7 | 0 | `crates/tauri-bundler/src/bundle/windows/msi/mod.rs` |
| threat | 252 | 62 | 0 | `crates/tauri/mobile/android/src/main/java/app/tauri/PathPlugin.kt` |
| ml_ai | 235 | 34 | 0 | `crates/tauri-runtime-wry/src/lib.rs` |
| ui | 451 | 90 | 1 | `crates/tauri/src/webview/mod.rs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (Hits: 127)
- `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (Hits: 85)
- `packages/api/src/path.ts` (Hits: 44)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TauriPlugin.kt** (`crates/tauri/mobile/android/src/main/java/app/tauri/annotation/TauriPlugin.kt`) — 21 inbound connections
2. **Window.svelte** (`examples/api/src/views/Window.svelte`) — 14 inbound connections
3. **base.ts** (`packages/api/src/menu/base.ts`) — 6 inbound connections
4. **InvokeArg.kt** (`crates/tauri/mobile/android/src/main/java/app/tauri/annotation/InvokeArg.kt`) — 5 inbound connections
5. **Permission.kt** (`crates/tauri/mobile/android/src/main/java/app/tauri/annotation/Permission.kt`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/tauri-runtime-wry/src/lib.rs`) — 136 outbound dependencies
2. **lib.rs** (`crates/tauri/src/lib.rs`) — 110 outbound dependencies
3. **app.rs** (`crates/tauri/src/app.rs`) — 93 outbound dependencies
4. **mod.rs** (`crates/tauri/src/webview/mod.rs`) — 83 outbound dependencies
5. **webview_window.rs** (`crates/tauri/src/webview/webview_window.rs`) — 71 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `build_nsis_app_installer` **(Many-Argument Workhorses)** (@ `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs`) -> Impact: **249.1** | LOC: 509
- `create_webview` **(Many-Argument Workhorses)** (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **231.3** | LOC: 666
- `build_wix_app_installer` **(Many-Argument Workhorses)** (@ `crates/tauri-bundler/src/bundle/windows/msi/mod.rs`) -> Impact: **209.4** | LOC: 468
  * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating the MSI installer. For now the only supported pla...
- `handle_user_message` **(Many-Argument Workhorses)** (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **162.8** | LOC: 817
- `resolve_access_message` **(Many-Argument Workhorses)** (@ `crates/tauri/src/ipc/authority.rs`) -> Impact: **137.4** | LOC: 209
- `tauri_config_to_bundle_settings` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/interface/rust.rs`) -> Impact: **121.5** | LOC: 337
- `get_size` **(Compute Cores)** (@ `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg`) -> Impact: **118.5** | LOC: 559
- `context_codegen` **(Compute Cores)** (@ `crates/tauri-codegen/src/context.rs`) -> Impact: **111.3** | LOC: 360
  * *Intent:* /// Build a `tauri::Context` for including in application code.
- `run_build` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/mobile/ios/build.rs`) -> Impact: **108.3** | LOC: 187
- `migrate_imports` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/migrate/migrations/v1/frontend.rs`) -> Impact: **104.8** | LOC: 218

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/tauri-runtime-wry/src` | 4 | 2157.98 | 10.41% | 22.36% |
| `crates/tauri-utils/src` | 12 | 1845.3 | 6.76% | 35.1% |
| `crates/tauri/src` | 9 | 1804.72 | 14.57% | 43.77% |
| `packages/api/src` | 14 | 1667.31 | 28.11% | 9.67% |
| `crates/tauri/src/webview` | 3 | 1531.98 | 12.95% | 61.83% |
| `crates/tauri-cli/src` | 12 | 1491.56 | 15.73% | 7.96% |
| `crates/tauri/src/menu` | 8 | 1362.96 | 5.97% | 47.22% |
| `crates/tauri-cli/src/helpers` | 17 | 1325.6 | 14.39% | 14.68% |
| `crates/tauri/src/ipc` | 7 | 1195.32 | 8.69% | 35.09% |
| `crates/tauri-cli/src/mobile/ios` | 6 | 1092.54 | 12.47% | 15.15% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/tauri-runtime/src/lib.rs` -> **100.0%** Exposure
- `crates/tauri/src/path/android.rs` -> **100.0%** Exposure
- `crates/tauri/src/path/desktop.rs` -> **100.0%** Exposure
- `crates/tauri/src/webview/webview_window.rs` -> **99.9983%** Exposure
- `crates/tauri/src/resources/mod.rs` -> **99.996%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/tauri-bundler/src/bundle/kmp/mod.rs` -> **100.0%** Exposure
- `crates/tauri-bundler/src/utils/mod.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/cargo_manifest.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/mod.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/pbxproj.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/tauri/src/webview/webview_window.rs` -> **160** Orphaned Functions | **0** Duplicates
- `crates/tauri/src/test/mock_runtime.rs` -> **112** Orphaned Functions | **23** Duplicates
- `crates/tauri-runtime/src/lib.rs` -> **94** Orphaned Functions | **27** Duplicates
- `crates/tauri/src/window/mod.rs` -> **104** Orphaned Functions | **0** Duplicates
- `crates/tauri/src/webview/mod.rs` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/api/src/core.ts` -> **99.9218%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4418` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginManager.kt` (KOTLIN) -> Cumulative Risk: **778.4**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.01)
- **Magnitude:** 127.24 | **LOC:** 225 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9945%), Concurrency (99.3338%)
- **Heaviest Functions:** `dispatchPluginMessage` (Compute Cores, Impact: 13.3), `onActivityCreate` (Callbacks & Closures, Impact: 8.6), `runCommand` (Many-Argument Workhorses, Impact: 7.6)

### 2. `crates/tauri-bundler/src/bundle/linux/appimage/linuxdeploy-plugin-gtk.sh` (SHELL) -> Cumulative Risk: **670.16**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.17)
- **Magnitude:** 232.86 | **LOC:** 328 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (99.5757%)
- **Heaviest Functions:** `__global_context__` (I/O & Config Routines, Impact: 13.9), `get_pkgconf_variable` (Compute Cores, Impact: 10.8), `Anonymous_Block` (Compute Cores, Impact: 9.8)

### 3. `crates/tauri/src/webview/webview_window.rs` (RUST) -> Cumulative Risk: **645.82**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +2.27)
- **Magnitude:** 825.6 | **LOC:** 2649 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9983%), Concurrency (94.9098%), Verification (80.0%)
- **Heaviest Functions:** `window_features` (Many-Argument Workhorses, Impact: 7.6), `on_download` (Callbacks & Closures, Impact: 6.3), `transient_for` (Generic / Templated Code, Impact: 4.0)

### 4. `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL) -> Cumulative Risk: **612.48**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.29)
- **Magnitude:** 453.42 | **LOC:** 639 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `get_size` (Compute Cores, Impact: 118.5), `find_mount_dir` (Many-Argument Workhorses, Impact: 68.3), `usage_[Truncated]` (I/O & Config Routines, Impact: 12.9)

### 5. `crates/tauri-cli/src/dev/auto-reload.js` (JAVASCRIPT) -> Cumulative Risk: **609.27**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.46)
- **Magnitude:** 18.4 | **LOC:** 31 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.7872%)
- **Heaviest Functions:** `onmessage` (Callbacks & Closures, Impact: 3.2), `reload_upon_connect` (Callbacks & Closures, Impact: 1.4), `onopen` (Callbacks & Closures, Impact: 1.4)

### 6. `crates/tauri-cli/src/dev/builtin_dev_server.rs` (RUST) -> Cumulative Risk: **608.56**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.17)
- **Magnitude:** 93.1 | **LOC:** 170 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.7527%), Verification (80.0%)
- **Heaviest Functions:** `start` (Many-Argument Workhorses, Impact: 22.6), `watch` (Defensive Guards, Impact: 11.5), `handler` (Defensive Guards, Impact: 10.2)

### 7. `crates/tauri-cli/src/helpers/pbxproj.rs` (RUST) -> Cumulative Risk: **598.77**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.30)
- **Magnitude:** 192.44 | **LOC:** 332 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Compute Cores, Impact: 60.9), `set_build_settings` (Many-Argument Workhorses, Impact: 17.4), `serialize` (Defensive Guards, Impact: 6.6)

### 8. `packages/api/src/dpi.ts` (TYPESCRIPT) -> Cumulative Risk: **598.52**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.56)
- **Magnitude:** 148.58 | **LOC:** 414 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9979%), Tech Debt (99.988%), Safety Score (86.5033%)
- **Heaviest Functions:** `constructor` (State Mutators, Impact: 8.0), `constructor` (State Mutators, Impact: 8.0), `constructor` (State Mutators, Impact: 8.0)

### 9. `crates/tauri-runtime/src/webview.rs` (RUST) -> Cumulative Risk: **588.43**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.17)
- **Magnitude:** 289.54 | **LOC:** 815 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Concurrency (90.4691%), State Flux (88.717%)
- **Heaviest Functions:** `from` (Defensive Guards, Impact: 16.9), `new` (Generic / Templated Code, Impact: 6.4), `new` (State Mutators, Impact: 2.5)

### 10. `packages/api/src/core.ts` (TYPESCRIPT) -> Cumulative Risk: **587.63**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.27)
- **Magnitude:** 82.24 | **LOC:** 356 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Secrets Risk (99.9218%), Concurrency (98.9139%), Documentation (59.0909%)
- **Heaviest Functions:** `constructor` (Compute Cores, Impact: 16.4), `invoke` (Generic / Templated Code, Impact: 4.3), `transformCallback` (Generic / Templated Code, Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/tauri-runtime-wry/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1936.08 | **LOC:** 5291 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (20.7915%), Tech Debt (35.5176%)
**Top Internal Functions/Classes:**
  * `create_webview` **(Many-Argument Workhorses)** (Impact: 231.3)
  * `handle_user_message` **(Many-Argument Workhorses)** (Impact: 162.8)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `handle_event_loop` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `with_config` **(Defensive Guards)** (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 115 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 438
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 676`, `args: 368`, `func_start: 262`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 7`, `state_mutation: 208`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 36`
* *Architecture:* `api: 98`, `concurrency: 39`, `import: 49`
* *Defense:* `safety: 114`, `doc: 34`, `sync_locks: 72`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, AtomicU32, BTreeMap, Cookie, CursorIcon::*, DetachedWindow, DetachedWindowWebview, DeviceEventFilter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 973.12 | **LOC:** 4454 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (3.3549%), Tech Debt (8.3746%)
**Top Internal Functions/Classes:**
  * `add_configured_headers` **(Defensive Guards)** (Impact: 29.4)
    * *Intent:* /// Add the headers defined in the tauri configuration file to http responses /// /// this is a util...
  * `visit_str` **(Defensive Guards)** (Impact: 24.3)
  * `deserialize` **(Defensive Guards)** (Impact: 22.4)
  * `fmt` **(Compute Cores)** (Impact: 11.3)
  * `fmt` **(Compute Cores)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 553`, `args: 152`, `func_start: 134`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 34`, `dead_code: 6`, `planned_debt: 6`
* *Architecture:* `api: 358`, `import: 32`
* *Defense:* `safety: 23`, `doc: 1311`, `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deserialize, Display, Error, Serialize, Serializer, TitleBarStyle, ToTokens, TokenStreamExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/window/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 881.12 | **LOC:** 2471 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.7452%), Tech Debt (99.8822%)
**Top Internal Functions/Classes:**
  * `build_internal` **(Defensive Guards)** (Impact: 34.3)
    * *Intent:* /// Creates a new window with an optional webview.
  * `set_menu` **(Defensive Guards)** (Impact: 12.3)
    * *Intent:* /// Sets the window menu and returns the previous one. /// /// ## Platform-specific: /// /// - **mac...
  * `remove_menu` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /// Removes the window menu and returns it. /// /// ## Platform-specific: /// /// - **macOS:** Unsup...
  * `is_menu_visible` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /// Shows the window menu.
  * `hide_menu` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* /// Hides the window menu.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 240`, `args: 230`, `func_start: 188`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 77`, `planned_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `api: 191`, `concurrency: 15`, `import: 15`
* *Defense:* `safety: 31`, `doc: 526`, `test: 2`, `sync_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CommandItem, CursorIcon, Effect, EffectState, EffectsBuilder, EmitPayload, Emitter, EventId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/interface/rust.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 845.18 | **LOC:** 1895 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 36.8%
- **Risk Profile:** Cognitive Load (10.7971%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tauri_config_to_bundle_settings` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `run_dev_watcher` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `new` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `get_bundle_settings` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `get_binaries` **(Many-Argument Workhorses)** (Impact: 36.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 279`, `args: 125`, `func_start: 49`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 4`, `state_mutation: 48`
* *Architecture:* `io: 6`, `api: 73`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 51`, `doc: 41`, `test: 20`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AppImageSettings, Arc, BundleBinary, BundleResources, BundleSettings, Config, ConfigMetadata, ConfigValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/webview/webview_window.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 825.6 | **LOC:** 2649 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (17.4094%), Tech Debt (99.9983%)
**Top Internal Functions/Classes:**
  * `window_features` **(Many-Argument Workhorses)** (Impact: 7.6)
    * *Intent:* /// Set the window features. /// Useful if you need to share the same window features, for instance ...
  * `on_download` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* /// Set a download event handler to be notified when a download is requested or finished. /// /// Re...
  * `transient_for` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /// Sets the window to be created transient for parent. /// /// See <https://docs.gtk.org/gtk3/metho...
  * `from_config` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// async fn open_window_multiple(app: tauri::AppHandle) { /// let mut conf = app.config().app.windo...
  * `icon` **(Generic / Templated Code)** (Impact: 3.7)
    * *Intent:* /// Sets the window icon.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 147`, `args: 214`, `func_start: 208`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 96`, `dead_code: 91`, `unreferenced_by_name: 160`
* *Architecture:* `api: 196`, `concurrency: 21`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1234`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AppHandle, Color, CommandItem, CspDirectiveSources, Effect, EffectState, EffectsBuilder, Emitter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/app.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 803.56 | **LOC:** 2606 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.8655%), Tech Debt (97.7746%)
**Top Internal Functions/Classes:**
  * `build` **(Many-Argument Workhorses)** (Impact: 58.7)
    * *Intent:* /// Builds the application.
  * `on_event_loop_event` **(Many-Argument Workhorses)** (Impact: 29.8)
  * `set_menu` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* /// Sets the app-wide menu and returns the previous one. /// /// If a window was not created with an...
  * `register_core_plugins` **(Compute Cores)** (Impact: 15.0)
  * `remove_data_store` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* /// Deletes a Data Store of this app /// /// Needs to be called from Main Thread
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 141
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 258`, `args: 142`, `func_start: 110`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 12`, `state_mutation: 29`, `dead_code: 56`, `planned_debt: 2`, `duplicate_logic: 12`, `unreferenced_by_name: 33`
* *Architecture:* `io: 1`, `api: 112`, `concurrency: 61`, `import: 18`
* *Defense:* `safety: 37`, `doc: 844`, `test: 3`, `sync_locks: 34`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AppManager, Arc, Asset, CallbackFn, CommandArg, CommandItem, Context, DefaultTemplate...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-utils/src/config_v1/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 775.22 | **LOC:** 3166 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.817%), Tech Debt (31.8838%)
**Top Internal Functions/Classes:**
  * `visit_str` **(Defensive Guards)** (Impact: 24.2)
  * `deserialize` **(Defensive Guards)** (Impact: 22.3)
  * `fmt` **(Compute Cores)** (Impact: 11.3)
  * `merge` **(State Mutators)** (Impact: 7.5)
  * `deserialize` **(Generic / Templated Code)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 269`, `args: 101`, `func_start: 92`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 7`, `unreferenced_by_name: 6`
* *Architecture:* `api: 335`, `import: 9`
* *Defense:* `safety: 6`, `doc: 853`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deserialize, Display, Error, Schema, Serialize, Serializer, Visitor, fmt::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/webview/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 632.66 | **LOC:** 2342 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (8.7924%), Tech Debt (76.1558%)
**Top Internal Functions/Classes:**
  * `on_message` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* /// Handles this window receiving an [`InvokeRequest`].
  * `resolve_command_scope` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* /// use tauri::Manager; /// /// #[derive(Debug, serde::Deserialize)] /// struct ScopeType { /// some...
  * `is_local_url` **(Compute Cores)** (Impact: 14.2)
  * `create_window` **(Callbacks & Closures)** (Impact: 8.6)
    * *Intent:* /// Initializes a webview builder with the given webview label and URL to load. /// /// # Known issu...
  * `emit_js` **(State Mutators)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 304`, `args: 167`, `func_start: 116`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 1`, `state_mutation: 53`, `dead_code: 13`, `planned_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `api: 140`, `concurrency: 37`, `import: 51`
* *Defense:* `safety: 18`, `doc: 533`, `test: 4`, `sync_locks: 14`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AppHandle, CommandArg, CommandItem, CommandScope, CspDirectiveSources, Emitter, Event, EventId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/api/src/window.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 591.58 | **LOC:** 2673 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (44.1043%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `emitTo` **(Generic / Templated Code)** (Impact: 10.9)
    * *Intent:* /** * Emits an event to all {@link EventTarget|targets} matching the given target. * * @example * ``...
  * `setSizeConstraints` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Sets the window inner size constraints. * @example * ```typescript * import { getCurrentWindow...
  * `constructor` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* * ```typescript * import { Window } from '@tauri-apps/api/window'; * const appWindow = new Window('m...
  * `emit` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* /** * Emits an event to all {@link EventTarget|targets}. * @example * ```typescript * import { getCu...
  * `_handleTauriEvent` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* /** @ignore */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 217
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 242`, `args: 124`, `func_start: 101`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`
* *Architecture:* `api: 84`, `concurrency: 197`, `import: 7`
* *Defense:* `safety: 8`, `doc: 209`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core, dpi, event, image, webview, webviewWindow, dialog, webview...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/msi/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 587.0 | **LOC:** 1142 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.082%), Tech Debt (12.6482%)
**Top Internal Functions/Classes:**
  * `build_wix_app_installer` **(Many-Argument Workhorses)** (Impact: 209.4)
    * *Intent:* // fn get_icon_data() -> crate::Result<()> { // Ok(()) // } // Entry point for bundling and creating...
  * `generate_resource_data` **(Compute Cores)** (Impact: 34.9)
    * *Intent:* /// Generates the data required for the resource bundling on wix
  * `run_candle` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// Runs the Candle.exe executable for Wix. Candle parses the wxs file and generates the code for bu...
  * `convert_version` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* // WiX requires versions to be numeric only in a `major.minor.patch.build` format
  * `bundle_project` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* /// Runs all of the commands to build the MSI installer. /// Returns a vector of PathBuf that shows ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 201`, `args: 45`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 3`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 5`, `import: 8`
* *Defense:* `safety: 23`, `doc: 31`, `test: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommandExt, File, Handlebars, HashAlgorithm, HashMap, HashSet, PathBuf, Serialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/migrate/migrations/v1/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 571.9 | **LOC:** 1257 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (37.2762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_bundle` **(Defensive Guards)** (Impact: 65.2)
  * `migrate_config` **(Defensive Guards)** (Impact: 37.8)
  * `allowlist_to_permissions` **(Compute Cores)** (Impact: 37.8)
  * `process_security` **(Compute Cores)** (Impact: 25.1)
  * `migrate` **(Compute Cores)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 79 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 158`, `args: 89`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 84`, `dead_code: 1`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 53`, `test: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ErrorExt, HashSet, PermissionEntry, Result, Scopes, Value, crate::error::Context, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/windows/nsis/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 544.88 | **LOC:** 891 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (36.4976%), Tech Debt (8.5626%)
**Top Internal Functions/Classes:**
  * `build_nsis_app_installer` **(Many-Argument Workhorses)** (Impact: 249.1)
  * `bundle_project` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* /// Runs all of the commands to build the NSIS installer. /// Returns a vector of PathBuf that shows...
  * `generate_resource_data` **(Compute Cores)** (Impact: 22.6)
  * `get_and_extract_nsis` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* // Gets NSIS and verifies the download via Sha1
  * `generate_binaries_data` **(Compute Cores)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 141`, `args: 45`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 58`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 1`, `import: 8`
* *Defense:* `safety: 30`, `doc: 4`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommandExt, Error, Handlebars, HashAlgorithm, NSIS_OUTPUT_FOLDER_NAME, NSIS_UPDATER_OUTPUT_FOLDER_NAME, NsisCompression, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/test/mock_runtime.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 544.24 | **LOC:** 1387 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.4937%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 25.9)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 8.2)
    * *Intent:* /// Create a new webview window.
  * `create_window` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `send_message` **(State Mutators)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 96`, `args: 209`, `func_start: 204`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 19`, `state_mutation: 28`, `planned_debt: 4`, `duplicate_logic: 23`, `unreferenced_by_name: 112`
* *Architecture:* `api: 9`, `concurrency: 17`, `import: 6`
* *Defense:* `safety: 8`, `doc: 4`, `sync_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, AtomicU32, DetachedWindow, DetachedWindowWebview, DeviceEventFilter, Error, EventLoopProxy, ExitRequestedEventAction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/menu/plugin.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 458.48 | **LOC:** 927 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.0354%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `insert` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `popup` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `create_item` **(Defensive Guards)** (Impact: 19.8)
  * `create_item` **(Defensive Guards)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 172`, `args: 52`, `func_start: 30`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`
* *Architecture:* `api: 21`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 40`, `sync_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` *, Channel, Manager, ResourceTable, RunEvent, Runtime, Serialize, State...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/macos/dmg/bundle_dmg` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 453.42 | **LOC:** 639 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (12.2156%)
**Top Internal Functions/Classes:**
  * `get_size` **(Compute Cores)** (Impact: 118.5)
  * `find_mount_dir` **(Many-Argument Workhorses)** (Impact: 68.3)
    * *Intent:* --format)
  * `usage_[Truncated]` **(I/O & Config Routines)** (Impact: 12.9)
  * `hdiutil_detach_retry` **(Compute Cores)** (Impact: 8.0)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 56 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 256`, `args: 44`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 110`, `unreferenced_by_name: 2`
* *Architecture:* `io: 127`, `concurrency: 1`
* *Defense:* `safety: 2`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/settings.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 452.5 | **LOC:** 1312 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (3.147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `binary_arch` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* /// Returns the architecture for the binary being bundled (e.g. "arm", "x86" or "x86_64").
  * `build` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* /// Builds a Settings from the CLI args. /// /// Package settings will be read from Cargo.toml. /// ...
  * `package_types` **(Compute Cores)** (Impact: 10.1)
    * *Intent:* /// If a list of package types was specified by the command-line, returns /// that list filtered by ...
  * `binary_path` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* /// Returns the path to the specified binary.
  * `copy_binaries` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* /// Copies external binaries to a path. /// /// Returns the list of destination paths.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 85`, `args: 81`, `func_start: 71`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 13`, `dead_code: 6`
* *Architecture:* `api: 220`, `import: 7`
* *Defense:* `safety: 11`, `doc: 447`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DeepLinkProtocol, FileAssociation, NSISInstallerMode, NsisCompression, PathBuf, ResourcePaths, RpmCompression, crate::bundle::platform::target_triple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/ipc/authority.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 450.2 | **LOC:** 1194 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.4276%), Tech Debt (38.77%)
**Top Internal Functions/Classes:**
  * `resolve_access_message` **(Many-Argument Workhorses)** (Impact: 137.4)
  * `has_permissions_allowing_command` **(Defensive Guards)** (Impact: 23.2)
  * `resolve_access` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* /// Checks if the given IPC execution is allowed and returns the [`ResolvedCommand`] if it is.
  * `get_command_scope_typed` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `add_capability_inner` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 153`, `args: 66`, `func_start: 36`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 28`, `dead_code: 10`, `duplicate_logic: 4`, `unreferenced_by_name: 9`
* *Architecture:* `api: 25`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 15`, `doc: 133`, `test: 21`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` APP_ACL_KEY, CommandItem, Deserialize, Display, ExecutionContext, Manager, ResolvedCommand, ResolvedScope...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/icon.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 446.26 | **LOC:** 987 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (10.5258%), Tech Debt (8.0256%)
**Top Internal Functions/Classes:**
  * `android` **(Many-Argument Workhorses)** (Impact: 92.3)
  * `apply_round_mask` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `png` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* // Generate .png files in 32x32, 64x64, 128x128, 256x256, 512x512 (icon.png) // Main target: Linux
  * `command` **(Defensive Guards)** (Impact: 31.4)
  * `ico` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* // Generate .ico file with layers for the most common sizes. // Main target: Windows
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 191`, `args: 39`, `func_start: 23`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 22`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 2`, `import: 8`
* *Defense:* `safety: 17`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DynamicImage, Error, ErrorExt, ExtendedColorType, File, FilterType, GenericImageView, IcoFrame...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-bundler/src/bundle/macos/app.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 405.76 | **LOC:** 768 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (29.9629%), Tech Debt (17.4778%)
**Top Internal Functions/Classes:**
  * `create_info_plist` **(Many-Argument Workhorses)** (Impact: 72.6)
    * *Intent:* // Creates the Info.plist file.
  * `bundle_project` **(Compute Cores)** (Impact: 47.4)
    * *Intent:* /// Bundles the project. /// Returns a vector of PathBuf that shows where the .app was created.
  * `copy_frameworks_to_bundle` **(Compute Cores)** (Impact: 42.8)
    * *Intent:* // Copies the macOS application bundle frameworks to the .app
  * `add_nested_code_sign_path` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `copy_custom_files_to_bundle` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /// Copies user-defined files to the app under Contents.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 116`, `args: 40`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 50`, `unreferenced_by_name: 6`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 23`, `doc: 10`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommandExt, Error::GenericError, ErrorExt, MacOsSettings, NotarizeAuthError, PackageSettings, PathBuf, Settings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/manager/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 401.18 | **LOC:** 1029 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.1397%), Tech Debt (49.3601%)
**Top Internal Functions/Classes:**
  * `get_asset` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* // TODO: Change to return `crate::Result` here in v3
  * `emit_to` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `emit_filter` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `replace_csp_nonce` **(Generic / Templated Code)** (Impact: 13.6)
  * `emit` **(Many-Argument Workhorses)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 125`, `args: 64`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 27`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 59`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 12`, `doc: 28`, `test: 15`, `sync_locks: 16`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App, Arc, Assets, ChannelInterceptor, Context, CspDirectiveSources, CspHash, DebugAppIcon...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/drag/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 357.44 | **LOC:** 419 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.6599%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 99`, `args: 44`, `func_start: 2`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 4`, `api: 19`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-cli/src/mobile/ios/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 337.9 | **LOC:** 699 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.9636%), Tech Debt (22.7936%)
**Top Internal Functions/Classes:**
  * `synchronize_project_config` **(Many-Argument Workhorses)** (Impact: 81.8)
  * `get_config` **(Many-Argument Workhorses)** (Impact: 81.5)
  * `simulator_prompt` **(Defensive Guards)** (Impact: 28.9)
  * `connected_device_prompt` **(Defensive Guards)** (Impact: 23.1)
  * `inject_resources` **(Defensive Guards)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 103`, `args: 42`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `dead_code: 3`, `unreferenced_by_name: 8`
* *Architecture:* `api: 16`, `import: 8`
* *Defense:* `safety: 35`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CliOptions, Config, ConfigMetadata, ConfigValue, DEFAULT_ASSET_DIR, Device, Error, ErrorExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/manager/webview.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 337.44 | **LOC:** 740 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.4819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare_webview` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `prepare_pending_webview` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `on_webview_event` **(Compute Cores)** (Impact: 19.3)
  * `initialization_script` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `attach_webview` **(Many-Argument Workhorses)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 120`, `args: 30`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 24`, `dead_code: 1`
* *Architecture:* `api: 25`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 16`, `doc: 10`, `test: 6`, `sync_locks: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AppManager, DRAG_DROP_EVENT, DRAG_ENTER_EVENT, DRAG_LEAVE_EVENT, DRAG_OVER_EVENT, DefaultTemplate, EmitPayload, EventLoopMessage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-runtime/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 331.44 | **LOC:** 994 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (5.1733%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `find_class` **(Generic / Templated Code)** (Impact: 2.6)
    * *Intent:* /// Finds an Android class in the project scope.
  * `remove_data_store` **(Annotated Framework Methods)** (Impact: 2.4)
  * `new_any_thread` **(State Mutators)** (Impact: 2.4)
    * *Intent:* /// Creates a new webview runtime on any thread.
  * `create_window` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* /// Create a new window.
  * `create_webview` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* /// Create a new webview.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 58`, `args: 150`, `func_start: 150`, `class_start: 17`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 27`, `unreferenced_by_name: 94`
* *Architecture:* `api: 33`, `concurrency: 27`, `import: 13`
* *Defense:* `doc: 352`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DetachedWindow, InvalidHeaderValue, PendingWebview, PendingWindow, PhysicalSize, Position, RawWindow, Rect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 326.34 | **LOC:** 1255 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (9.2385%), Tech Debt (99.9822%)
**Top Internal Functions/Classes:**
  * `get_webview_window` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* /// Fetch a single webview window from the manager.
  * `features_are_documented` **(Tests & Verification)** (Impact: 5.5)
  * `encode` **(Type Conversions)** (Impact: 5.1)
    * *Intent:* /// Encode bytes with [Z85]. /// /// # Panics /// /// Will panic if the input bytes are not a multip...
  * `webview_windows` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* /// Fetch all managed webview windows.
  * `emit_to` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* /// for i in 1..100 { /// std::thread::sleep(std::time::Duration::from_millis(150)); /// // emit a d...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 179`, `args: 87`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 8`, `dead_code: 31`, `planned_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 38`
* *Architecture:* `api: 84`, `concurrency: 23`, `import: 39`
* *Defense:* `safety: 3`, `doc: 444`, `test: 10`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AppHandle, AssetResolver, Builder, CloseRequestApi, CspHash, Debug, DeviceEventFilter, DragDropEvent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/tauri/src/webview/webview_window.rs` -> Churn: **61.14%** | Cog Load: 17.4094% | Debt: 99.9983%
- `crates/tauri/src/webview/mod.rs` -> Churn: **57.21%** | Cog Load: 8.7924% | Debt: 76.1558%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/tauri-utils/src/config_v1/mod.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 775.22
- `crates/tauri/src/manager/mod.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 401.18
- `examples/drag/index.html` -> **Amr Bashir** (100.0% isolated ownership) | Magnitude: 357.44
- `crates/tauri/src/plugin.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 279.68
- `crates/tauri-utils/src/acl/resolved.rs` -> **Thomas Eizinger** (100.0% isolated ownership) | Magnitude: 272.12

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 99.2493%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginHandle.kt` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.7916%)
- `packages/api/src/menu/base.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9209%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/tauri/mobile/android/src/main/java/app/tauri/annotation/Permission.kt` -> **Severity: 1.315** (Embedded: 0.022 * Error Risk: 59.7314%)
- `packages/api/src/menu/base.ts` -> **Severity: 0.718** (Embedded: 0.0094 * Error Risk: 76.464%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/PermissionHelper.kt` -> **Severity: 0.549** (Embedded: 0.0074 * Error Risk: 73.9521%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt` -> **Severity: 0.545** (Embedded: 0.0059 * Error Risk: 92.9811%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/JSObject.kt` -> **Severity: 0.442** (Embedded: 0.0059 * Error Risk: 75.337%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/api/src/menu/base.ts` -> **Severity: 1578.5** (Blast Radius: 31.57 * Doc Risk: 50.0%)
- `crates/tauri-cli/src/helpers/template.rs` -> **Severity: 487.1** (Blast Radius: 4.871 * Doc Risk: 100.0%)
- `crates/tauri/mobile/android/src/main/java/app/tauri/Logger.kt` -> **Severity: 451.3** (Blast Radius: 4.513 * Doc Risk: 100.0%)
- `crates/tauri/mobile/ios-api/Sources/Tauri/Tauri.swift` -> **Severity: 435.0** (Blast Radius: 4.35 * Doc Risk: 100.0%)
- `crates/tauri-cli/src/helpers/flock.rs` -> **Severity: 427.291** (Blast Radius: 5.392 * Doc Risk: 79.2453%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
