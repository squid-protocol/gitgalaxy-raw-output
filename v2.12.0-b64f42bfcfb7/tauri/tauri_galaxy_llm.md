# ARCHITECTURAL_BRIEF: tauri
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tauri-apps/tauri` |
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
- **Scope:** 664 analyzed artifact(s), 78893 LOC.
- **Load-bearing artifact:** `crates/tauri-cli/src/error.rs` -- 68 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `crates/tauri-runtime-wry/src/lib.rs` -- pulls in 157 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/tauri-runtime-wry/src/lib.rs` at magnitude 1667.58 (structural weight, not risk).
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
| Total Artifacts | 1064 |
| Analyzed Artifacts (Scanned) | 664 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 400 |
| Total LOC | 78893 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 62.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6231 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1252 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0544 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 283 | 64423 | 42.6% |
| MARKDOWN | 72 | 0 | 10.8% |
| JSON | 56 | 2358 | 8.4% |
| KOTLIN | 42 | 1961 | 6.3% |
| PLAINTEXT | 38 | 0 | 5.7% |
| JAVASCRIPT | 34 | 1013 | 5.1% |
| YAML | 31 | 1949 | 4.7% |
| HTML | 31 | 2477 | 4.7% |
| TYPESCRIPT | 27 | 3525 | 4.1% |
| XML | 21 | 2 | 3.2% |
| SWIFT | 17 | 761 | 2.6% |
| CSS | 3 | 133 | 0.5% |
| GROOVY | 3 | 60 | 0.5% |
| SHELL | 2 | 136 | 0.3% |
| OBJECTIVE-C | 2 | 11 | 0.3% |
| BATCH | 1 | 66 | 0.2% |
| RUBY | 1 | 18 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 664 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Generic / Templated Code Files 13%, Large Core Modules (2) 9%, Large Core Modules (3) 8%, Declarative / Non-Code 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 552 | 83.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 110 | 16.6% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 400*

**Composition by Extension & Reason:**
- `.png`: 79x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 34x Excluded (Unsupported Extension: '.toml'), 23x Unsupported Format (.toml), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Unsupported Extension: '.crate-manifest'), 2x Excluded (Unsupported Extension: 'no_extension')
- `.rs`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Statistical Anomaly (Z-Score: -4.74 < -4.55)
- `.md`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2402 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 4031 LOC)
- `.nsh`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 11x Excluded (Unsupported Extension: '.0'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 12x Excluded (Unsupported Extension: '.snap')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 3877 LOC), 1x Excluded (Massive Static Asset Blob: 3109 LOC)
- `.ico`: 7x Excluded (Explicitly Denied Extension: '.ico')
- `.js`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 581 LOC)
- `.html`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pro`: 5x Excluded (Unsupported Extension: '.pro')
- `.xml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 27 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.9 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.9 | 29.8 | 47.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 92.6 | 19.4 | 8.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.1 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 83.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.9 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 481 | 106 | 1 | `crates/tauri-cli/src/icon.rs` |
| cleanup | 32 | 18 | 0 | `crates/tauri-runtime-wry/src/lib.rs` |
| guards | 2268 | 282 | 10 | `crates/tauri-runtime-wry/src/lib.rs` |
| danger | 1655 | 211 | 7 | `crates/tauri-runtime-wry/src/lib.rs` |
| concurrency | 1763 | 140 | 5 | `packages/api/src/window.ts` |
| connectivity | 4588 | 361 | 16 | `crates/tauri-utils/src/config.rs` |
| io | 452 | 127 | 2 | `packages/api/src/path.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 31 | 21 | 0 | `crates/tauri-macros/src/command/wrapper.rs` |
| time | 26 | 18 | 0 | `examples/api/src/views/Window.svelte` |
| serialization | 149 | 60 | 0 | `crates/tauri-utils/src/config.rs` |
| regex | 14 | 10 | 0 | `crates/tauri-cli/templates/mobile/android/gradlew` |
| events | 477 | 126 | 2 | `crates/tauri-runtime-wry/src/lib.rs` |
| tests | 713 | 70 | 1 | `crates/tauri-utils/src/config.rs` |
| docs | 11824 | 248 | 23 | `crates/tauri-utils/src/config.rs` |
| debt | 438 | 110 | 1 | `crates/tauri-runtime/src/lib.rs` |
| mutation | 10158 | 373 | 42 | `crates/tauri-runtime-wry/src/lib.rs` |
| dead_code | 644 | 111 | 1 | `crates/tauri/src/window/mod.rs` |
| credential | 7 | 6 | 0 | `crates/tauri-utils/src/acl/build.rs` |
| threat | 24 | 1 | 0 | `crates/tauri/src/ipc/format_callback.rs` |
| ml_ai | 221 | 29 | 0 | `crates/tauri-runtime-wry/src/lib.rs` |
| ui | 447 | 89 | 1 | `crates/tauri/src/webview/mod.rs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/api/src/path.ts` (Hits: 44)
- `examples/api/src/App.svelte` (Hits: 16)
- `crates/tauri-cli/templates/mobile/android/gradlew` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **error.rs** (`crates/tauri-cli/src/error.rs`) — 68 inbound connections
2. **lib.rs** (`crates/tauri/src/lib.rs`) — 60 inbound connections
3. **config.rs** (`crates/tauri-utils/src/config.rs`) — 43 inbound connections
4. **app.rs** (`crates/tauri/src/app.rs`) — 38 inbound connections
5. **mod.rs** (`crates/tauri/src/scope/mod.rs`) — 31 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/tauri-runtime-wry/src/lib.rs`) — 157 outbound dependencies
2. **lib.rs** (`crates/tauri/src/lib.rs`) — 124 outbound dependencies
3. **mod.rs** (`crates/tauri/src/webview/mod.rs`) — 87 outbound dependencies
4. **app.rs** (`crates/tauri/src/app.rs`) — 82 outbound dependencies
5. **mod.rs** (`crates/tauri/src/window/mod.rs`) — 66 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handle_user_message` **(Many-Argument Workhorses)** (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **162.8** | LOC: 817
- `resolve_access_message` **(Many-Argument Workhorses)** (@ `crates/tauri/src/ipc/authority.rs`) -> Impact: **132.2** | LOC: 209
- `tauri_config_to_bundle_settings` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/interface/rust.rs`) -> Impact: **118.7** | LOC: 337
- `context_codegen` **(Compute Cores)** (@ `crates/tauri-codegen/src/context.rs`) -> Impact: **109.9** | LOC: 360
  * *Intent:* /// Build a `tauri::Context` for including in application code.
- `run_build` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/mobile/ios/build.rs`) -> Impact: **108.3** | LOC: 187
- `migrate_imports` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/migrate/migrations/v1/frontend.rs`) -> Impact: **104.8** | LOC: 218
- `setup` **(Many-Argument Workhorses)** (@ `crates/tauri-cli/src/dev.rs`) -> Impact: **96.5** | LOC: 185
- `get_response` **(Many-Argument Workhorses)** (@ `crates/tauri/src/protocol/asset.rs`) -> Impact: **95.9** | LOC: 198
- `try_build` **(Defensive Guards)** (@ `crates/tauri-build/src/lib.rs`) -> Impact: **94.3** | LOC: 245
  * *Intent:* /// Same as [`build()`], but takes an extra configuration argument, and does not panic.
- `create_window` **(Many-Argument Workhorses)** (@ `crates/tauri-runtime-wry/src/lib.rs`) -> Impact: **93.1** | LOC: 221

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/tauri-runtime-wry/src` | 4 | 1889.48 | 9.33% | 8.88% |
| `crates/tauri-utils/src` | 12 | 1862.5 | 6.73% | 8.22% |
| `crates/tauri/src` | 9 | 1801.82 | 15.67% | 32.54% |
| `packages/api/src` | 14 | 1646.61 | 27.92% | 9.29% |
| `crates/tauri/src/webview` | 3 | 1493.18 | 11.99% | 28.5% |
| `crates/tauri-cli/src` | 12 | 1468.16 | 15.42% | 3.87% |
| `crates/tauri/src/menu` | 8 | 1362.96 | 5.97% | 10.46% |
| `crates/tauri-cli/src/helpers` | 17 | 1314.0 | 14.32% | 5.85% |
| `crates/tauri/src/ipc` | 7 | 1185.22 | 8.26% | 20.64% |
| `crates/tauri-cli/src/mobile/ios` | 6 | 1080.94 | 12.17% | 5.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **100.0%** Exposure
- `crates/tauri-runtime/src/lib.rs` -> **100.0%** Exposure
- `.github/workflows/publish-cli-js.yml` -> **99.9964%** Exposure
- `crates/tauri/src/resources/mod.rs` -> **99.996%** Exposure
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginManager.kt` -> **99.9933%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/tauri-cli/src/helpers/cargo_manifest.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/mod.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/pbxproj.rs` -> **100.0%** Exposure
- `crates/tauri-cli/src/helpers/prompts.rs` -> **100.0%** Exposure
- `examples/api/src/components/MenuItemBuilder.svelte` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/tauri-runtime/src/lib.rs` -> **94** Orphaned Functions | **27** Duplicates
- `crates/tauri/src/window/mod.rs` -> **104** Orphaned Functions | **0** Duplicates
- `crates/tauri/src/webview/mod.rs` -> **49** Orphaned Functions | **0** Duplicates
- `crates/tauri-runtime-wry/src/lib.rs` -> **36** Orphaned Functions | **9** Duplicates
- `crates/tauri/src/lib.rs` -> **38** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/api/src/core.ts` -> **99.9218%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4040` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/tauri-runtime-wry/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.35)
- **Top Global Matches:** file_cluster_5: 9.35, file_cluster_12: 10.113, file_cluster_0: 10.856
- **Magnitude:** 1667.58 | **LOC:** 5291 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **157**; blast radius 1.436; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (66.3%), Guard Balance (formerly Safety Score) (55.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.1%)
- **Documentation Coverage:** 93.3824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handle_user_message` **(Many-Argument Workhorses)** (Impact: 162.8)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `handle_event_loop` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `create_webview` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `with_config` **(Defensive Guards)** (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 676`, `args: 368`, `func_start: 262`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 7`, `state_mutation: 208`, `planned_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 36`
* *Architecture:* `api: 98`, `concurrency: 39`, `import: 49`
* *Defense:* `safety: 114`, `doc: 34`, `sync_locks: 72`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.436
  * `Choke Point (Betweenness):` 0.002421 | `Ripple Effect (Closeness):` 0.052804
  * `Imports (Out-Degree: 13):` dialog, monitor, undecorated_resizing, util, webview, window, CursorIcon::*, http::Request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/tauri-utils/src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.82)
- **Top Global Matches:** file_cluster_0: 7.82, file_cluster_5: 9.482, file_cluster_12: 9.555
- **Magnitude:** 971.72 | **LOC:** 4454 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **38**; blast radius 29.722; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.6%), Guard Balance (formerly Safety Score) (46.4%)
- **Documentation Coverage:** 75.1515% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_configured_headers` **(Defensive Guards)** (Impact: 29.4)
    * *Intent:* /// Add the headers defined in the tauri configuration file to http responses /// /// this is a util...
  * `visit_str` **(Defensive Guards)** (Impact: 24.3)
  * `deserialize` **(Defensive Guards)** (Impact: 22.4)
  * `fmt` **(Generic / Templated Code)** (Impact: 11.3)
  * `fmt` **(Compute Cores)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 553`, `args: 152`, `func_start: 134`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 34`, `planned_debt: 6`
* *Architecture:* `api: 358`, `import: 32`
* *Defense:* `safety: 23`, `doc: 1311`, `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.722
  * `Choke Point (Betweenness):` 0.001877 | `Ripple Effect (Closeness):` 0.125571
  * `Imports (Out-Degree: 4):` parse, crate::TitleBarStyle, crate::WindowEffect, crate::WindowEffectState, crate::acl::capability::Capability, crate::literal_struct, crate::tokens::*, http::response::Builder...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `crates/tauri/src/window/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.845)
- **Top Global Matches:** file_cluster_0: 8.845, file_cluster_5: 9.382, file_cluster_12: 10.023
- **Magnitude:** 861.52 | **LOC:** 2471 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **66**; blast radius 4.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.3%), Guard Balance (formerly Safety Score) (49.9%)
- **Documentation Coverage:** 6.8047% of unit weight undocumented
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
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 240`, `args: 230`, `func_start: 188`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 77`, `planned_debt: 1`, `unreferenced_by_name: 104`
* *Architecture:* `api: 191`, `concurrency: 15`, `import: 15`
* *Defense:* `safety: 31`, `doc: 526`, `test: 2`, `sync_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.195
  * `Choke Point (Betweenness):` 0.001361 | `Ripple Effect (Closeness):` 0.059114
  * `Imports (Out-Degree: 20):` plugin, crate::CursorIcon, crate::Emitter, crate::EventLoopMessage, crate::EventName, crate::Listener, crate::Manager, crate::ResourceTable...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `crates/tauri/src/webview/webview_window.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.233)
- **Top Global Matches:** file_cluster_0: 7.233, file_cluster_13: 9.702, file_cluster_15: 10.695
- **Magnitude:** 832.8 | **LOC:** 2649 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **58**; blast radius 2.405; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.8%), Connectivity (formerly Api Exposure) (76.4%)
- **Documentation Coverage:** 4.3902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `window_features` **(Many-Argument Workhorses)** (Impact: 7.6)
    * *Intent:* /// Set the window features. /// Useful if you need to share the same window features, for instance ...
  * `transient_for` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /// Sets the window to be created transient for parent. /// /// See <https://docs.gtk.org/gtk3/metho...
  * `from_config` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// async fn open_window_multiple(app: tauri::AppHandle) { /// let mut conf = app.config().app.windo...
  * `icon` **(Generic / Templated Code)** (Impact: 3.7)
    * *Intent:* /// Sets the window icon.
  * `parent` **(Generic / Templated Code)** (Impact: 3.7)
    * *Intent:* /// Sets a parent to the window to be created. /// /// ## Platform-specific /// /// - **Windows**: T...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 147`, `args: 214`, `func_start: 208`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 96`
* *Architecture:* `api: 208`, `concurrency: 21`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1234`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.405
  * `Choke Point (Betweenness):` 0.000465 | `Ripple Effect (Closeness):` 0.05454
  * `Imports (Out-Degree: 19):` crate::AppHandle, crate::Emitter, crate::Event, crate::EventId, crate::EventName, crate::Listener, crate::Manager, crate::ResourceTable...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/interface/rust.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.0)
- **Top Global Matches:** file_cluster_4: 9.0, file_cluster_5: 10.678, file_cluster_12: 11.359
- **Magnitude:** 823.98 | **LOC:** 1895 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **65**; blast radius 5.316; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (70.7%), Connectivity (formerly Api Exposure) (60.8%)
- **Documentation Coverage:** 80.5195% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tauri_config_to_bundle_settings` **(Many-Argument Workhorses)** (Impact: 118.7)
  * `run_dev_watcher` **(Many-Argument Workhorses)** (Impact: 54.8)
  * `get_bundle_settings` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `new` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `get_binaries` **(Many-Argument Workhorses)** (Impact: 36.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 279`, `args: 125`, `func_start: 49`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 4`, `state_mutation: 48`
* *Architecture:* `io: 6`, `api: 73`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 51`, `doc: 41`, `test: 20`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.316
  * `Choke Point (Betweenness):` 0.001782 | `Ripple Effect (Closeness):` 0.026033
  * `Imports (Out-Degree: 13):` cargo_config, desktop, installation, manifest, cargo_config::Config, crate::ConfigValue, crate::error::Context, crate::error::Error...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `crates/tauri/src/app.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.73)
- **Top Global Matches:** file_cluster_5: 7.73, file_cluster_0: 9.243, file_cluster_12: 9.657
- **Magnitude:** 799.86 | **LOC:** 2606 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **38** in-repo importer(s); it depends on **82**; blast radius 10.298; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.1%), Debt Markers (formerly Tech Debt) (63.3%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
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
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 7
* *Concurrency (weighted view):* 141
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 258`, `args: 142`, `func_start: 110`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 12`, `state_mutation: 29`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 1`, `api: 117`, `concurrency: 61`, `import: 18`
* *Defense:* `safety: 37`, `doc: 844`, `test: 3`, `sync_locks: 34`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.298
  * `Choke Point (Betweenness):` 0.002681 | `Ripple Effect (Closeness):` 0.069414
  * `Imports (Out-Degree: 26):` plugin, crate::ActivationPolicy, crate::Context, crate::DeviceEventFilter, crate::Emitter, crate::Event, crate::EventLoopMessage, crate::EventName...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `crates/tauri-utils/src/config_v1/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.746)
- **Top Global Matches:** file_cluster_0: 6.746, file_cluster_13: 9.616, file_cluster_15: 10.094
- **Magnitude:** 775.22 | **LOC:** 3166 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 2.49; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.5%), Debt Markers (formerly Tech Debt) (31.9%), Mutation Surface (formerly State Flux) (25.8%)
- **Documentation Coverage:** 75.5319% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_str` **(Defensive Guards)** (Impact: 24.2)
  * `deserialize` **(Defensive Guards)** (Impact: 22.3)
  * `fmt` **(Generic / Templated Code)** (Impact: 11.3)
  * `merge` **(State Mutators)** (Impact: 7.5)
  * `deserialize` **(Generic / Templated Code)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 269`, `args: 101`, `func_start: 92`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `planned_debt: 2`, `duplicate_logic: 7`, `unreferenced_by_name: 6`
* *Architecture:* `api: 335`, `import: 9`
* *Defense:* `safety: 6`, `doc: 853`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.49
  * `Choke Point (Betweenness):` 0.000407 | `Ripple Effect (Closeness):` 0.086633
  * `Imports (Out-Degree: 1):` parse, schemars::schema::Metadata, schemars::schema::Schema, self::*, semver::Version, serde::Deserialize, serde::Serialize, serde::Serializer...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/tauri/src/test/mock_runtime.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.261)
- **Top Global Matches:** file_cluster_0: 9.261, file_cluster_5: 11.355, file_cluster_13: 11.416
- **Magnitude:** 656.24 | **LOC:** 1387 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **49**; blast radius 0.913; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (75.6%), Guard Balance (formerly Safety Score) (59.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.5%), Complexity Load (formerly Cognitive Load) (6.5%)
- **Documentation Coverage:** 98.1073% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 8.2)
    * *Intent:* /// Create a new webview window.
  * `create_window` **(Generic / Templated Code)** (Impact: 8.2)
  * `create_window` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `send_message` **(State Mutators)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 96`, `args: 209`, `func_start: 204`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 19`, `state_mutation: 28`, `planned_debt: 4`, `duplicate_logic: 23`
* *Architecture:* `api: 121`, `concurrency: 17`, `import: 6`
* *Defense:* `safety: 8`, `doc: 4`, `sync_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.913
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.039659
  * `Imports (Out-Degree: 7):` std::cell::RefCell, std::collections::HashMap, std::fmt, std::sync::Arc, std::sync::Mutex, std::sync::atomic::AtomicBool, std::sync::atomic::AtomicU32, std::sync::atomic::Ordering...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/tauri/src/webview/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.489)
- **Top Global Matches:** file_cluster_5: 7.489, file_cluster_12: 9.06, file_cluster_0: 9.434
- **Magnitude:** 586.66 | **LOC:** 2342 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **24** in-repo importer(s); it depends on **87**; blast radius 6.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 9.816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_message` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* /// Handles this window receiving an [`InvokeRequest`].
  * `resolve_command_scope` **(Many-Argument Workhorses)** (Impact: 17.9)
    * *Intent:* /// use tauri::Manager; /// /// #[derive(Debug, serde::Deserialize)] /// struct ScopeType { /// some...
  * `is_local_url` **(Compute Cores)** (Impact: 10.8)
  * `emit_js` **(Stateful Encapsulated Methods)** (Impact: 8.4)
  * `listen_js` **(Stateful Encapsulated Methods)** (Impact: 7.8)
    * *Intent:* /// Register a JS event listener and return its identifier.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 304`, `args: 167`, `func_start: 116`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 46`, `high_risk_execution: 1`, `state_mutation: 53`, `planned_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `api: 140`, `concurrency: 37`, `import: 51`
* *Defense:* `safety: 18`, `doc: 533`, `test: 4`, `sync_locks: 14`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.055
  * `Choke Point (Betweenness):` 0.001445 | `Ripple Effect (Closeness):` 0.064983
  * `Imports (Out-Degree: 22):` plugin, webview_window, cookie, crate::AppHandle, crate::Emitter, crate::Event, crate::EventId, crate::EventLoopMessage...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `packages/api/src/window.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.857)
- **Top Global Matches:** file_cluster_0: 6.857, file_cluster_15: 7.946, file_cluster_11: 8.135
- **Magnitude:** 586.18 | **LOC:** 2673 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 1.779; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.3%), Guard Balance (formerly Safety Score) (49.1%)
- **Documentation Coverage:** 3.4091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitTo` **(Generic / Templated Code)** (Impact: 10.9)
    * *Intent:* /** * * ```typescript * await getCurrentWindow().emit('main', 'window-loaded', { loggedIn: true, tok...
  * `setSizeConstraints` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Sets the window inner size constraints. * ```typescript * await getCurrentWindow().setSizeCons...
  * `constructor` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* * ```typescript * const appWindow = new Window('my-label'); * appWindow.once('tauri://created', func...
  * `emit` **(Generic / Templated Code)** (Impact: 9.4)
    * *Intent:* /** * ```typescript * await getCurrentWindow().emit('window-loaded', { loggedIn: true, token: 'authT...
  * `_handleTauriEvent` **(Generic / Templated Code)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 217
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 242`, `args: 124`, `func_start: 101`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`
* *Architecture:* `api: 84`, `concurrency: 197`, `import: 7`
* *Defense:* `safety: 8`, `doc: 209`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.779
  * `Choke Point (Betweenness):` 0.00012 | `Ripple Effect (Closeness):` 0.010179
  * `Imports (Out-Degree: 6):` core, dpi, event, image, webview, webviewWindow
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/migrate/migrations/v1/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.236)
- **Top Global Matches:** file_cluster_4: 9.236, file_cluster_6: 9.705, file_cluster_12: 13.946
- **Magnitude:** 570.5 | **LOC:** 1257 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.905; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.6%), Connectivity (formerly Api Exposure) (53.5%), Complexity Load (formerly Cognitive Load) (37.2%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_bundle` **(Defensive Guards)** (Impact: 65.2)
  * `migrate_config` **(Defensive Guards)** (Impact: 37.8)
  * `allowlist_to_permissions` **(Compute Cores)** (Impact: 37.8)
  * `process_security` **(Defensive Guards)** (Impact: 23.7)
  * `migrate` **(Compute Cores)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 79 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 158`, `args: 89`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 84`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 53`, `test: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.905
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.01196
  * `Imports (Out-Degree: 4):` crate::ErrorExt, crate::Result, crate::error::Context, serde_json::Map, serde_json::Value, std::collections::BTreeMap, std::collections::HashSet, std::fs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/tauri/src/menu/plugin.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.835)
- **Top Global Matches:** file_cluster_0: 7.835, file_cluster_9: 9.687, file_cluster_5: 9.889
- **Magnitude:** 458.48 | **LOC:** 927 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.981; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (67.8%), Connectivity (formerly Api Exposure) (59.9%), Guard Balance (formerly Safety Score) (50.2%), Complexity Load (formerly Cognitive Load) (15.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `insert` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `popup` **(Generic / Templated Code)** (Impact: 20.0)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.981
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.039157
  * `Imports (Out-Degree: 15):` crate::Manager, crate::ResourceTable, crate::RunEvent, crate::Runtime, crate::State, crate::Webview, crate::Window, crate::command...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/tauri/src/ipc/authority.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.089)
- **Top Global Matches:** file_cluster_5: 7.089, file_cluster_12: 8.407, file_cluster_0: 10.112
- **Magnitude:** 445.2 | **LOC:** 1194 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **27**; blast radius 5.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (62.8%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (46.7%)
- **Documentation Coverage:** 48.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_access_message` **(Many-Argument Workhorses)** (Impact: 132.2)
  * `has_permissions_allowing_command` **(Defensive Guards)** (Impact: 23.2)
  * `resolve_access` **(Many-Argument Workhorses)** (Impact: 18.8)
    * *Intent:* /// Checks if the given IPC execution is allowed and returns the [`ResolvedCommand`] if it is.
  * `get_command_scope_typed` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `add_capability_inner` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 153`, `args: 66`, `func_start: 36`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 28`, `duplicate_logic: 4`
* *Architecture:* `api: 31`, `concurrency: 6`, `import: 16`
* *Defense:* `safety: 15`, `doc: 133`, `test: 21`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.603
  * `Choke Point (Betweenness):` 0.000875 | `Ripple Effect (Closeness):` 0.05587
  * `Imports (Out-Degree: 13):` crate::AppHandle, crate::Manager, crate::Runtime, crate::StateManager, crate::Webview, crate::ipc::InvokeError, crate::ipc::Origin, crate::sealed::ManagerBase...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/icon.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.746)
- **Top Global Matches:** file_cluster_6: 6.746, file_cluster_4: 11.71, file_cluster_8: 14.732
- **Magnitude:** 443.76 | **LOC:** 987 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.829; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Mutation Surface (formerly State Flux) (51.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `android` **(Many-Argument Workhorses)** (Impact: 89.8)
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
* *Structure:* `branch: 143`, `structural_boundaries: 191`, `args: 39`, `func_start: 23`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 22`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 2`, `import: 8`
* *Defense:* `safety: 17`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.829
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022424
  * `Imports (Out-Degree: 1):` clap::Parser, crate::Result, crate::error::Context, crate::error::Error, crate::error::ErrorExt, icns::IconFamily, icns::IconType, image::DynamicImage...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/tauri/src/manager/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.401)
- **Top Global Matches:** file_cluster_5: 6.401, file_cluster_12: 8.209, file_cluster_0: 8.999
- **Magnitude:** 401.18 | **LOC:** 1029 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **64**; blast radius 2.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.1%), Guard Balance (formerly Safety Score) (54.8%), Debt Markers (formerly Tech Debt) (49.4%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_asset` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* // TODO: Change to return `crate::Result` here in v3
  * `emit_to` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `emit_filter` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `replace_csp_nonce` **(Generic / Templated Code)** (Impact: 13.6)
  * `emit` **(Stateful Encapsulated Methods)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 125`, `args: 64`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 27`, `planned_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 59`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 12`, `doc: 28`, `test: 15`, `sync_locks: 16`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.753
  * `Choke Point (Betweenness):` 0.000899 | `Ripple Effect (Closeness):` 0.056911
  * `Imports (Out-Degree: 25):` menu, tray, webview, window, crate::App, crate::Assets, crate::Context, crate::DebugAppIcon...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `crates/tauri/src/manager/webview.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.894)
- **Top Global Matches:** file_cluster_6: 9.894, file_cluster_4: 10.456, file_cluster_5: 14.63
- **Magnitude:** 332.94 | **LOC:** 740 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **42**; blast radius 1.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (67.4%), Guard Balance (formerly Safety Score) (55.3%), Connectivity (formerly Api Exposure) (44.0%)
- **Documentation Coverage:** 78.2609% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_webview` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `prepare_pending_webview` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `on_webview_event` **(Compute Cores)** (Impact: 19.3)
  * `initialization_script` **(Many-Argument Workhorses)** (Impact: 17.5)
  * `attach_webview` **(Many-Argument Workhorses)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 120`, `args: 30`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 2`, `state_mutation: 24`
* *Architecture:* `api: 25`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 16`, `doc: 10`, `test: 6`, `sync_locks: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.483
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.048224
  * `Imports (Out-Degree: 13):` crate::EventLoopMessage, crate::EventTarget, crate::Manager, crate::Runtime, crate::Scopes, crate::UriSchemeContext, crate::Webview, crate::Window...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/mobile/ios/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.435)
- **Top Global Matches:** file_cluster_6: 7.435, file_cluster_4: 10.75, file_cluster_8: 16.574
- **Magnitude:** 331.7 | **LOC:** 699 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **52**; blast radius 1.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.1%), Mutation Surface (formerly State Flux) (36.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `synchronize_project_config` **(Many-Argument Workhorses)** (Impact: 81.8)
  * `get_config` **(Many-Argument Workhorses)** (Impact: 81.5)
  * `simulator_prompt` **(Defensive Guards)** (Impact: 25.4)
  * `connected_device_prompt` **(Defensive Guards)** (Impact: 21.4)
  * `inject_resources` **(Defensive Guards)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 103`, `args: 42`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `unreferenced_by_name: 8`
* *Architecture:* `api: 16`, `import: 8`
* *Defense:* `safety: 35`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` 0.000833 | `Ripple Effect (Closeness):` 0.018571
  * `Imports (Out-Degree: 14):` build, dev, project, run, xcode_script, cargo_mobile2::apple::config::Config, cargo_mobile2::apple::config::Metadata, cargo_mobile2::apple::config::Platform...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/tauri-runtime/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.818)
- **Top Global Matches:** file_cluster_0: 6.818, file_cluster_13: 9.915, file_cluster_15: 11.724
- **Magnitude:** 331.44 | **LOC:** 994 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 4.63; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (43.2%)
- **Documentation Coverage:** 2.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_class` **(Generic / Templated Code)** (Impact: 2.6)
    * *Intent:* /// Finds an Android class in the project scope.
  * `remove_data_store` **(Generic / Templated Code)** (Impact: 2.4)
  * `new_any_thread` **(State Mutators)** (Impact: 2.4)
    * *Intent:* /// Creates a new webview runtime on any thread.
  * `create_window` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* /// Create a new window.
  * `create_webview` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* /// Create a new webview.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 58`, `args: 150`, `func_start: 150`, `class_start: 17`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 27`, `unreferenced_by_name: 94`
* *Architecture:* `api: 33`, `concurrency: 27`, `import: 13`
* *Defense:* `doc: 352`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.000624 | `Ripple Effect (Closeness):` 0.073066
  * `Imports (Out-Degree: 6):` dpi, monitor, webview, window, cookie::Cookie, dpi::PhysicalPosition, dpi::PhysicalSize, dpi::Position...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `crates/tauri/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.342)
- **Top Global Matches:** file_cluster_0: 7.342, file_cluster_5: 7.66, file_cluster_12: 9.923
- **Magnitude:** 324.94 | **LOC:** 1255 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **124**; blast radius 21.285; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.6%)
- **Documentation Coverage:** 28.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_webview_window` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* /// Fetch a single webview window from the manager.
  * `features_are_documented` **(Annotated & Test Methods)** (Impact: 5.5)
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
* *Structure:* `branch: 35`, `structural_boundaries: 179`, `args: 87`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 8`, `planned_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 38`
* *Architecture:* `api: 84`, `concurrency: 23`, `import: 39`
* *Defense:* `safety: 3`, `doc: 444`, `test: 10`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.285
  * `Choke Point (Betweenness):` 0.012027 | `Ripple Effect (Closeness):` 0.092552
  * `Imports (Out-Degree: 33):` app, async_runtime, error, event, image, ios, ipc, manager...
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/mobile/android/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.214)
- **Top Global Matches:** file_cluster_4: 8.214, file_cluster_6: 8.797, file_cluster_12: 13.948
- **Magnitude:** 294.98 | **LOC:** 679 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **53**; blast radius 1.722; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (41.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ensure_sdk` **(Compute Cores)** (Impact: 34.4)
  * `generate_tauri_properties` **(Many-Argument Workhorses)** (Impact: 33.1)
  * `ensure_ndk` **(Defensive Guards)** (Impact: 26.8)
  * `adb_device_prompt` **(Defensive Guards)** (Impact: 21.3)
  * `emulator_prompt` **(Defensive Guards)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 91`, `args: 40`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 11`, `unreferenced_by_name: 7`
* *Architecture:* `io: 2`, `api: 7`, `import: 8`
* *Defense:* `safety: 23`, `doc: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.722
  * `Choke Point (Betweenness):` 0.000592 | `Ripple Effect (Closeness):` 0.018338
  * `Imports (Out-Degree: 11):` android_studio_script, build, dev, project, run, cargo_mobile2::android::adb, cargo_mobile2::android::config::Config, cargo_mobile2::android::config::Metadata...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/tauri-build/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.498)
- **Top Global Matches:** file_cluster_4: 9.498, file_cluster_5: 10.32, file_cluster_12: 10.766
- **Magnitude:** 294.66 | **LOC:** 701 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **26**; blast radius 1.471; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Mutation Surface (formerly State Flux) (28.7%)
- **Documentation Coverage:** 26.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_build` **(Defensive Guards)** (Impact: 94.3)
    * *Intent:* /// Same as [`build()`], but takes an extra configuration argument, and does not panic.
  * `copy_frameworks` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* // Copies the macOS application bundle frameworks to the target folder
  * `copy_dir` **(Compute Cores)** (Impact: 27.0)
  * `copy_binaries` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `copy_resources` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* /// Copies resources to a path.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 108`, `args: 37`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 19`, `import: 10`
* *Defense:* `safety: 20`, `doc: 130`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.471
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.003012
  * `Imports (Out-Degree: 8):` acl, codegen, manifest, mobile, static_vcruntime, acl::AppManifest, acl::DefaultPermissionRule, acl::InlinedPlugin...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/drag/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.465)
- **Top Global Matches:** file_cluster_13: 4.465, file_cluster_2: 5.792, file_cluster_17: 6.378
- **Magnitude:** 290.36 | **LOC:** 419 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.4%), Connectivity (formerly Api Exposure) (9.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 99`, `args: 44`, `func_start: 2`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `io: 4`, `api: 19`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.749
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/tauri-runtime/src/webview.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.618)
- **Top Global Matches:** file_cluster_0: 6.618, file_cluster_13: 8.852, file_cluster_15: 10.645
- **Magnitude:** 289.54 | **LOC:** 815 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **19**; blast radius 3.415; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.5%), Connectivity (formerly Api Exposure) (89.6%), Mutation Surface (formerly State Flux) (88.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 13.0435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from` **(Defensive Guards)** (Impact: 16.9)
  * `new` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Create a new [`PendingWebview`] with a label from the given [`WebviewAttributes`].
  * `new` **(State Mutators)** (Impact: 2.5)
  * `new` **(State Mutators)** (Impact: 2.4)
    * *Intent:* /// Initializes the default attributes for a webview.
  * `on_webview_created` **(Generic / Templated Code)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 82`, `args: 37`, `func_start: 36`, `class_start: 12`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `api: 106`, `concurrency: 23`, `import: 6`
* *Defense:* `safety: 6`, `doc: 230`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.415
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.060977
  * `Imports (Out-Degree: 4):` crate::Rect, crate::Runtime, crate::UserEvent, crate::window::WindowId, crate::window::is_label_valid, http::Request, std::borrow::Cow, std::collections::HashMap...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/mobile/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.639)
- **Top Global Matches:** file_cluster_4: 8.639, file_cluster_6: 11.326, file_cluster_5: 12.066
- **Magnitude:** 286.16 | **LOC:** 623 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **57**; blast radius 3.467; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Mutation Surface (formerly State Flux) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.8%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ensure_init` **(Many-Argument Workhorses)** (Impact: 57.3)
  * `use_network_address_for_dev_url` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `get_app` **(Many-Argument Workhorses)** (Impact: 16.3)
  * `write_options` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /// Writes CLI options to be used later on the Xcode and Android Studio build commands
  * `local_ip_address` **(Defensive Guards)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 102`, `args: 47`, `func_start: 21`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 11`, `unreferenced_by_name: 11`
* *Architecture:* `io: 8`, `api: 17`, `concurrency: 5`, `import: 15`
* *Defense:* `safety: 11`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.467
  * `Choke Point (Betweenness):` 0.001829 | `Ripple Effect (Closeness):` 0.024297
  * `Imports (Out-Degree: 10):` android, init, ios, cargo_mobile2::ChildHandle, cargo_mobile2::config::app::App, cargo_mobile2::config::app::Raw, cargo_mobile2::env::Env, cargo_mobile2::env::Error...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `crates/tauri-cli/src/mobile/ios/build.rs` (RUST | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.312)
- **Top Global Matches:** file_cluster_8: 9.312, file_cluster_6: 10.656, file_cluster_4: 18.348
- **Magnitude:** 283.76 | **LOC:** 560 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **51**; blast radius 0.802; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.6%), Connectivity (formerly Api Exposure) (66.8%), Guard Balance (formerly Safety Score) (53.3%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_build` **(Many-Argument Workhorses)** (Impact: 108.3)
  * `run` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `fmt` **(Generic / Templated Code)** (Impact: 3.8)
  * `pre_xcode_15_4_name` **(State Mutators)** (Impact: 3.2)
    * *Intent:* /// Xcode 15.4 deprecated these names (in this case we should use the Display impl).
  * `from_str` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 98`, `args: 14`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`
* *Architecture:* `io: 3`, `api: 20`, `import: 7`
* *Defense:* `safety: 8`, `doc: 24`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.802
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.014578
  * `Imports (Out-Degree: 11):` cargo_mobile2::apple::config::Config, cargo_mobile2::apple::target::ArchiveConfig, cargo_mobile2::apple::target::BuildConfig, cargo_mobile2::apple::target::ExportConfig, cargo_mobile2::apple::target::Target, cargo_mobile2::env::Env, cargo_mobile2::opts::NoiseLevel, cargo_mobile2::opts::Profile...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/tauri/src/event/plugin.rs` (RUST) | Magnitude: 19.46 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 43, generics: 13, structural_boundaries: 10, decorators: 8
- `crates/tauri-cli/src/migrate/migrations/v1/frontend/partial_loader/svelte.rs` (RUST) | Magnitude: 24.6 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 25, core_var_decl: 18, design_snake_case: 18
- `bench/src/utils.rs` (RUST) | Magnitude: 120.56 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 173, branch: 39, structural_boundaries: 37, api: 27
- `crates/tauri/src/tray/plugin.rs` (RUST) | Magnitude: 139.28 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 156, generics: 53, structural_boundaries: 48, core_var_decl: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `crates/tauri-utils/src/pattern/isolation.js` (JAVASCRIPT) | Magnitude: 81.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 82, branch: 19, safety: 19, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/api/src/menu/checkMenuItem.ts` (TYPESCRIPT) | Magnitude: 38.34 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 23, concurrency: 16, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/tauri/mobile/ios-api/Sources/Tauri/Plugin/Plugin.swift` (SWIFT) | Magnitude: 54.32 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 26, api: 13, core_var_decl: 11
- `examples/file-associations/index.html` (HTML) | Magnitude: 25.98 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 5, structural_boundaries: 4, design_snake_case: 4
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/InvalidPluginMethodException.kt` (KOTLIN) | Magnitude: 5.92 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 3, func_start: 3, indent_spaces: 3, structural_boundaries: 2
- `crates/tauri/test/fixture/isolation/isolation-dist/index.html` (HTML) | Magnitude: 0.02 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, core_var_decl: 3, design_snake_case: 3
- `examples/api/isolation-dist/index.html` (HTML) | Magnitude: 15.2 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, core_var_decl: 3, design_snake_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Channel.kt` (KOTLIN) | Magnitude: 15.58 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, args: 4, api: 4
- `examples/api/src/components/MenuItemBuilder.svelte` (HTML) | Magnitude: 81.48 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 130, core_var_decl: 53, design_snake_case: 48, structural_boundaries: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/tauri/src/pattern.rs` (RUST) | Magnitude: 23.3 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, doc: 17, decorators: 16, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/api/src/index.ts` (TYPESCRIPT) | Magnitude: 16.52 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, import: 12, indent_spaces: 12, io: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/tauri-runtime-wry/src/monitor/macos.rs` (RUST) | Magnitude: 8.0 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, core_var_decl: 4, design_snake_case: 4
- `crates/tauri/src/vibrancy/macos.rs` (RUST) | Magnitude: 14.54 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, args: 12, structural_boundaries: 9, branch: 4
- `packages/api/src/menu.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6, doc: 1
- `packages/cli/tauri.js` (JAVASCRIPT) | Magnitude: 39.7 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 22, branch: 13, core_var_decl: 10, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/tauri-cli/src/bundle.rs` (RUST) | Magnitude: 146.9 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 51, branch: 48, core_var_decl: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/tests/acl/src/lib.rs` (RUST) | Magnitude: 12.22 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 21, core_var_decl: 15, design_snake_case: 15
- `crates/tauri-macos-sign/src/keychain/identity.rs` (RUST) | Magnitude: 39.7 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 17, args: 15, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `examples/multiwindow/main.rs` (RUST) | Magnitude: 5.84 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, ui_framework: 5, structural_boundaries: 3, args: 3
- `examples/multiwebview/main.rs` (RUST) | Magnitude: 9.7 | Delta: **0.193** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 8, core_var_decl: 8, design_snake_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/tauri-cli/src/helpers/mod.rs` (RUST) | Magnitude: 85.22 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, structural_boundaries: 36, api: 20, branch: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/tauri/src/webview/mod.rs` -> Churn: **57.97%** | Cog Load: 6.239% | Debt: 76.1558%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/tauri/src/manager/mod.rs` -> **Tony** (100.0% isolated ownership) | Magnitude: 401.18
- `crates/tauri-cli/src/mobile/ios/mod.rs` -> **sftse** (100.0% isolated ownership) | Magnitude: 331.7
- `crates/tauri/src/lib.rs` -> **Lucas Fernandes Nogueira** (100.0% isolated ownership) | Magnitude: 324.94
- `crates/tauri-cli/src/mobile/android/mod.rs` -> **sftse** (100.0% isolated ownership) | Magnitude: 294.98
- `examples/drag/index.html` -> **Amr Bashir** (100.0% isolated ownership) | Magnitude: 290.36

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/tauri-cli/src/helpers/mod.rs` -> **Severity: 0.362** (Bridge: 0.0036 * Flux: 100.0%)
- `crates/tauri-cli/src/lib.rs` -> **Severity: 0.297** (Bridge: 0.0058 * Flux: 50.7734%)
- `crates/tauri/src/lib.rs` -> **Severity: 0.181** (Bridge: 0.012 * Flux: 15.0534%)
- `crates/tauri-runtime-wry/src/lib.rs` -> **Severity: 0.16** (Bridge: 0.0024 * Flux: 66.283%)
- `crates/tauri-cli/src/info/mod.rs` -> **Severity: 0.152** (Bridge: 0.0017 * Flux: 87.7461%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/tauri-utils/src/plugin.rs` -> **Severity: 5.909** (Embedded: 0.0856 * Error Risk: 69.0625%)
- `crates/tauri-utils/src/acl/mod.rs` -> **Severity: 5.896** (Embedded: 0.1005 * Error Risk: 58.6885%)
- `crates/tauri-utils/src/config.rs` -> **Severity: 5.828** (Embedded: 0.1256 * Error Risk: 46.4096%)
- `crates/tauri-utils/src/lib.rs` -> **Severity: 5.773** (Embedded: 0.1239 * Error Risk: 46.5816%)
- `crates/tauri-utils/src/html2.rs` -> **Severity: 5.678** (Embedded: 0.086 * Error Risk: 66.036%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/tauri-cli/src/error.rs` -> **Severity: 2661.662** (Blast Radius: 30.419 * Doc Risk: 87.5%)
- `crates/tauri-utils/src/config.rs` -> **Severity: 2233.653** (Blast Radius: 29.722 * Doc Risk: 75.1515%)
- `crates/tauri-utils/src/lib.rs` -> **Severity: 1187.817** (Blast Radius: 26.132 * Doc Risk: 45.4545%)
- `crates/tauri-macos-sign/src/lib.rs` -> **Severity: 1077.6** (Blast Radius: 10.776 * Doc Risk: 100.0%)
- `crates/tauri-utils/src/acl/mod.rs` -> **Severity: 646.657** (Blast Radius: 13.521 * Doc Risk: 47.8261%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 191 literal sites + 28 sites through wrappers = 219

- `jsonPut` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/PluginResult.kt`
- `env_var` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `crates/tauri/build.rs`
- `shouldLog` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/Logger.kt`
- `getBooleanInternal` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/JSObject.kt`
- `getIntegerInternal` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/JSObject.kt`
- `hasListener` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt`
- `isDownloadsDocument` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`
- `isExternalStorageDocument` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`
- `isGooglePhotosUri` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`
- `isMediaDocument` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`
- `jsonMapper` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/plugin/Plugin.kt`
- `legacyPrimaryPath` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `crates/tauri/mobile/android/src/main/java/app/tauri/FsUtils.kt`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 18367 call pairs -- scoped 17.1%, unique 0.2%, ambiguous 12.3%, external 70.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 17145 | 15.4% | 0.0% | 12.9% | 71.7% |
| typescript | 470 | 68.3% | 0.0% | 1.9% | 29.8% |
| kotlin | 392 | 29.1% | 3.1% | 5.6% | 62.2% |
| html | 122 | 5.7% | 9.0% | 0.0% | 85.2% |
| swift | 120 | 19.2% | 5.8% | 18.3% | 56.7% |
| javascript | 96 | 16.7% | 0.0% | 5.2% | 78.1% |
| ruby | 12 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 9 | 33.3% | 0.0% | 0.0% | 66.7% |
| objective-c | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
