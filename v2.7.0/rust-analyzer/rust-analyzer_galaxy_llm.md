# ARCHITECTURAL_BRIEF: rust-analyzer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/rust-analyzer.git` |
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
| Total Artifacts | 2262 |
| Analyzed Artifacts (Scanned) | 1405 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 857 |
| Total LOC | 444925 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 62.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7525 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3708 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.8655 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1235 | 437791 | 87.9% |
| PLAINTEXT | 102 | 0 | 7.3% |
| TYPESCRIPT | 27 | 6076 | 1.9% |
| MARKDOWN | 17 | 0 | 1.2% |
| HTML | 11 | 516 | 0.8% |
| JSON | 9 | 432 | 0.6% |
| XML | 2 | 0 | 0.1% |
| SHELL | 1 | 21 | 0.1% |
| PYTHON | 1 | 89 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1286 | 91.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 119 | 8.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 857*

**Composition by Extension & Reason:**
- `.rast`: 507x Excluded (Unsupported Extension: '.rast')
- `.rs`: 193x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Unsupported Format (.undeterminable), 1x Excluded (Saturation: Line 39 exceeds 500 chars)
- `.toml`: 48x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 4x Excluded (Saturation: Line 53 exceeds 500 chars), 2x Excluded (Saturation: Line 54 exceeds 500 chars), 2x Excluded (Saturation: Line 44 exceeds 500 chars)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable), 1x Excluded (Embedded Array/Matrix Payload: 8237 commas in 561 LOC)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 6421 LOC), 1x Excluded (Massive Static Asset Blob: 12817 LOC)
- `.yaml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.ungram`: 2x Excluded (Unsupported Extension: '.ungram')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.3 | 6.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 33.5 | 44.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.6 | 37.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 29.2 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 89.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.1 | 2.0 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 14.9 | 4.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 77.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18630 | 884 | 34 | `crates/hir/src/lib.rs` |
| cleanup | 202 | 79 | 0 | `crates/ide-db/src/text_edit.rs` |
| guards | 12799 | 878 | 24 | `crates/ide-completion/src/tests/expression.rs` |
| danger | 6619 | 539 | 11 | `crates/ide/src/hover/tests.rs` |
| concurrency | 1987 | 205 | 2 | `editors/code/src/commands.ts` |
| connectivity | 16687 | 918 | 30 | `crates/hir/src/lib.rs` |
| io | 262 | 64 | 0 | `editors/code/src/bootstrap.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 10 | 0 | `crates/ide/src/expand_macro.rs` |
| time | 17 | 13 | 0 | `lib/lsp-server/src/lib.rs` |
| serialization | 54 | 22 | 0 | `lib/smol_str/tests/test.rs` |
| regex | 30 | 12 | 0 | `editors/code/src/commands.ts` |
| events | 700 | 121 | 0 | `crates/hir-ty/src/method_resolution/probe.rs` |
| tests | 10115 | 592 | 19 | `crates/ide/src/hover/tests.rs` |
| docs | 15186 | 712 | 29 | `crates/rust-analyzer/src/config.rs` |
| debt | 2933 | 465 | 5 | `crates/ide-assists/src/handlers/add_missing_match_arms.rs` |
| mutation | 46101 | 1000 | 86 | `crates/ide-assists/src/handlers/extract_function.rs` |
| dead_code | 10825 | 913 | 21 | `crates/parser/test_data/generated/runner.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 1582 | 236 | 2 | `crates/hir-def/src/nameres/tests/macros.rs` |
| ml_ai | 581 | 74 | 0 | `crates/hir-ty/src/tests/patterns.rs` |
| ui | 8 | 2 | 0 | `editors/code/src/commands.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.8571**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editors/code/src/bootstrap.ts` (Hits: 32)
- `crates/ide-db/src/imports/insert_use/tests.rs` (Hits: 24)
- `editors/code/src/util.ts` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ast.rs** (`crates/syntax/src/ast.rs`) — 83 inbound connections
2. **make.rs** (`crates/syntax/src/ast/make.rs`) — 39 inbound connections
3. **iter.rs** (`crates/tt/src/iter.rs`) — 20 inbound connections
4. **lsp_ext.ts** (`editors/code/src/lsp_ext.ts`) — 18 inbound connections
5. **ted.rs** (`crates/syntax/src/ted.rs`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/hir/src/lib.rs`) — 197 outbound dependencies
2. **interner.rs** (`crates/hir-ty/src/next_solver/interner.rs`) — 159 outbound dependencies
3. **lib.rs** (`crates/ide/src/lib.rs`) — 157 outbound dependencies
4. **lower.rs** (`crates/hir-ty/src/lower.rs`) — 139 outbound dependencies
5. **semantics.rs** (`crates/hir/src/semantics.rs`) — 138 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `exec_intrinsic` (@ `crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **657.1** | LOC: 783
- `classify_name_ref` (@ `crates/ide-completion/src/context/analysis.rs`) -> Impact: **476.7** | LOC: 814
- `lower_expr_to_place_without_adjust` (@ `crates/hir-ty/src/mir/lower.rs`) -> Impact: **430.9** | LOC: 925
- `else_completion_after_if` (@ `crates/ide-completion/src/tests/expression.rs`) -> Impact: **370.9** | LOC: 1059
- `hir_fmt` (@ `crates/hir-ty/src/display.rs`) -> Impact: **324.6** | LOC: 533
- `eval_rvalue` (@ `crates/hir-ty/src/mir/eval.rs`) -> Impact: **295.0** | LOC: 500
- `complete_expr_path` (@ `crates/ide-completion/src/completions/expr.rs`) -> Impact: **250.6** | LOC: 406
- `run_inference` (@ `crates/rust-analyzer/src/cli/analysis_stats.rs`) -> Impact: **236.2** | LOC: 368
- `infer_expr_inner` (@ `crates/hir-ty/src/infer/expr.rs`) -> Impact: **234.4** | LOC: 753
- `pattern_match_inner` (@ `crates/hir-ty/src/mir/lower/pattern_matching.rs`) -> Impact: **207.6** | LOC: 395

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/ide-assists/src/handlers` | 134 | 25602.86 | 10.28% | 72.7% |
| `crates/ide/src` | 43 | 10789.94 | 9.05% | 49.82% |
| `crates/hir/src` | 11 | 7990.54 | 11.41% | 34.72% |
| `crates/hir-ty/src` | 29 | 7242.54 | 8.96% | 43.56% |
| `crates/hir-def/src` | 20 | 6315.18 | 10.13% | 62.31% |
| `crates/ide-diagnostics/src/handlers` | 52 | 4596.9 | 9.61% | 80.54% |
| `editors/code/src` | 19 | 4243.46 | 51.99% | 21.48% |
| `crates/ide-db/src` | 23 | 3893.38 | 8.94% | 60.2% |
| `crates/hir-ty/src/mir` | 5 | 3865.58 | 17.78% | 26.49% |
| `crates/hir-ty/src/next_solver` | 21 | 3713.38 | 7.32% | 57.25% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/hir-ty/src/next_solver/infer/opaque_types/table.rs` -> **100.0%** Exposure
- `crates/ide-db/src/famous_defs.rs` -> **100.0%** Exposure
- `crates/parser/test_data/generated/runner.rs` -> **100.0%** Exposure
- `crates/parser/test_data/parser/ok/0031_extern.rs` -> **100.0%** Exposure
- `crates/paths/src/lib.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/ide-assists/src/utils/gen_trait_fn_body.rs` -> **100.0%** Exposure
- `crates/ide-assists/src/utils/ref_field_expr.rs` -> **100.0%** Exposure
- `crates/syntax-bridge/src/prettify_macro_expansion.rs` -> **100.0%** Exposure
- `lib/smol_str/src/gdb_smolstr_printer.py` -> **100.0%** Exposure
- `crates/ide-db/src/syntax_helpers/format_string_exprs.rs` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/parser/test_data/generated/runner.rs` -> **279** Orphaned Functions | **0** Duplicates
- `crates/hir/src/lib.rs` -> **175** Orphaned Functions | **87** Duplicates
- `crates/ide/src/hover/tests.rs` -> **254** Orphaned Functions | **0** Duplicates
- `crates/hir-ty/src/tests/traits.rs` -> **172** Orphaned Functions | **0** Duplicates
- `crates/ide-assists/src/handlers/extract_function.rs` -> **147** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19268` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editors/code/src/commands.ts` (TYPESCRIPT) -> Cumulative Risk: **740.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 879.64 | **LOC:** 1553 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Documentation (99.2647%), State Flux (81.0247%)
- **Heaviest Functions:** `viewFileUsingTextDocumentContentProvider` (Impact: 20.6), `asWorkspaceSnippetEdit` (Impact: 18.0), `elementToString` (Impact: 15.2)

### 2. `editors/code/src/client.ts` (TYPESCRIPT) -> Cumulative Risk: **726.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 411.6 | **LOC:** 423 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9245%), State Flux (91.9334%)
- **Heaviest Functions:** `createClient` (Impact: 146.7), `handleDiagnostics` (Impact: 65.0), `provideCodeActions` (Impact: 29.0)

### 3. `editors/code/src/test_explorer.ts` (TYPESCRIPT) -> Cumulative Risk: **718.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 194.0 | **LOC:** 213 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9685%)
- **Heaviest Functions:** `removeByFile` (Impact: 23.8), `addTest` (Impact: 20.6), `addTestGroup` (Impact: 9.3)

### 4. `editors/code/src/config.ts` (TYPESCRIPT) -> Cumulative Risk: **695.29**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 403.1 | **LOC:** 614 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.1127%), Documentation (94.2857%), Concurrency (93.3392%)
- **Heaviest Functions:** `substituteVariablesInEnv` (Impact: 47.7), `toggleCheckOnSave` (Impact: 21.7), `runnablesExtraEnv` (Impact: 20.2)

### 5. `editors/code/src/ctx.ts` (TYPESCRIPT) -> Cumulative Risk: **694.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 435.84 | **LOC:** 647 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9851%), State Flux (99.9282%), Documentation (95.6522%)
- **Heaviest Functions:** `prepareSyntaxTreeView` (Impact: 29.6), `updateStatusBarItem` (Impact: 17.3), `updateCommands` (Impact: 16.9)

### 6. `crates/parser/src/grammar/items.rs` (RUST) -> Cumulative Risk: **660.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 262.32 | **LOC:** 501 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (96.966%), Documentation (91.3043%), Verification (80.0%)
- **Heaviest Functions:** `opt_item` (Impact: 66.7), `opt_item_without_modifiers` (Impact: 31.3), `item_or_macro` (Impact: 18.9)

### 7. `editors/code/src/tasks.ts` (TYPESCRIPT) -> Cumulative Risk: **660.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 109.4 | **LOC:** 147 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%), Cognitive Load (94.4485%)
- **Heaviest Functions:** `targetToExecution` (Impact: 35.2), `buildRustTask` (Impact: 8.2), `provideTasks` (Impact: 6.2)

### 8. `crates/hir-ty/src/next_solver/interner.rs` (RUST) -> Cumulative Risk: **657.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 905.58 | **LOC:** 2709 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 68.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (96.7262%), Api Exposure (93.1832%), Churn (92.39%)
- **Heaviest Functions:** `new` (Impact: 25.1), `for_each_relevant_impl` (Impact: 22.9), `unsizing_params_for_adt` (Impact: 19.5)

### 9. `editors/code/src/debug.ts` (TYPESCRIPT) -> Cumulative Risk: **655.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.1 | **LOC:** 455 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9005%), State Flux (96.8866%)
- **Heaviest Functions:** `getDebugConfiguration` (Impact: 58.5), `getDebugConfig` (Impact: 15.7), `makeDebugConfig` (Impact: 15.2)

### 10. `crates/ide-assists/src/handlers/toggle_async_sugar.rs` (RUST) -> Cumulative Risk: **647.48**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 188.58 | **LOC:** 594 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9658%), Tech Debt (97.7023%)
- **Heaviest Functions:** `sugar_impl_future_into_async` (Impact: 36.5), `desugar_async_into_impl_future` (Impact: 23.2), `unwrap_future_output` (Impact: 7.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/hir/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3351.76 | **LOC:** 7283 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 49.3%
- **Risk Profile:** Cognitive Load (8.6793%), Tech Debt (99.9727%)
**Top Internal Functions/Classes:**
  * `diagnostics` (Impact: 144.6)
    * *Intent:* /// Fills `acc` with the module's diagnostics.
  * `diagnostics` (Impact: 138.4)
  * `fn_ptr_type` (Impact: 22.7)
  * `iterate_method_candidates_split_inherent` (Impact: 22.4)
    * *Intent:* /// Allows you to treat inherent and non-inherent methods differently. /// /// Note that inherent me...
  * `contains_reference` (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *Amplified Sql Injection:* 5 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 677`, `structural_boundaries: 1100`, `args: 819`, `func_start: 589`, `class_start: 90`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 8`, `state_mutation: 101`, `dead_code: 5`, `fragile_debt: 33`, `duplicate_logic: 87`, `unreferenced_by_name: 175`
* *Architecture:* `api: 586`, `concurrency: 2`, `import: 22`
* *Defense:* `safety: 66`, `doc: 181`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyImplId, AssocItemId, AssocItemLoc, AstPtr, BindingId, BuiltinDeriveImplId, CallableDefId, ClauseKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2014.86 | **LOC:** 3193 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 51.9%
- **Risk Profile:** Cognitive Load (27.8444%), Tech Debt (23.0861%)
**Top Internal Functions/Classes:**
  * `eval_rvalue` (Impact: 295.0)
  * `rec` (Impact: 103.3)
  * `create_memory_map` (Impact: 91.3)
  * `interpret_mir` (Impact: 82.2)
  * `patch_addresses` (Impact: 80.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 88 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 662`, `args: 193`, `func_start: 90`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 10`, `state_mutation: 106`, `fragile_debt: 12`, `unreferenced_by_name: 8`
* *Architecture:* `api: 14`, `import: 26`
* *Defense:* `safety: 79`, `doc: 22`, `test: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Address::*, BasicBlockId, BinOp, CastKind, ComplexMemoryMap, ConstBytes, ConstEvalError, ConstKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-assists/src/handlers/extract_function.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1669.5 | **LOC:** 6541 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 38.9%
- **Risk Profile:** Cognitive Load (10.0489%), Tech Debt (84.3704%)
**Top Internal Functions/Classes:**
  * `analyze_container` (Impact: 66.1)
  * `extract_function` (Impact: 55.7)
    * *Intent:* // -> // ``` // fn main() { // let n = 1; // fun_name(n); // let g = 3; // } // // fn $0fun_name(n: ...
  * `make_body` (Impact: 37.1)
  * `make_call` (Impact: 35.1)
  * `fix_param_usages` (Impact: 32.8)
    * *Intent:* /// change all usages to account for added `&`/`&mut` for some params
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 1228`, `args: 685`, `func_start: 589`, `class_start: 100`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 82`, `dead_code: 17`, `fragile_debt: 10`, `unreferenced_by_name: 147`
* *Architecture:* `api: 13`, `concurrency: 27`, `import: 14`
* *Defense:* `safety: 75`, `doc: 68`, `test: 153`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Assists, AstNode, AstToken, COMMENT, HasAttrs, HasGenericParams, HasName, HirDisplay...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/display.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1639.02 | **LOC:** 2489 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 61.1%
- **Risk Profile:** Cognitive Load (26.2193%), Tech Debt (16.4655%)
**Top Internal Functions/Classes:**
  * `hir_fmt` (Impact: 324.6)
  * `write_bounds_like_dyn_trait` (Impact: 157.2)
  * `render_const_scalar_inner` (Impact: 148.4)
  * `hir_fmt` (Impact: 132.1)
  * `hir_fmt` (Impact: 129.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 426`, `args: 94`, `func_start: 70`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 11`, `state_mutation: 52`, `dead_code: 4`, `fragile_debt: 13`
* *Architecture:* `api: 49`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 35`, `doc: 47`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` BoundVarIndexKind, Clause, ClauseKind, Const, ConstKind, CoroutineArgsParts, CoroutineClosureArgsParts, DbInterner...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/handlers/request.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1462.48 | **LOC:** 2712 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 53.8%
- **Risk Profile:** Cognitive Load (17.0761%), Tech Debt (11.4039%)
**Top Internal Functions/Classes:**
  * `run_rustfmt` (Impact: 83.8)
  * `handle_runnables` (Impact: 55.6)
  * `handle_will_rename_files` (Impact: 50.0)
  * `handle_code_action_resolve` (Impact: 40.3)
  * `handle_completion_resolve` (Impact: 39.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 669`, `args: 175`, `func_start: 84`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 76`, `dead_code: 2`, `fragile_debt: 7`
* *Architecture:* `api: 65`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 69`, `doc: 13`, `test: 2`, `sync_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AbsPathBuf, AssistResolveStrategy, CallHierarchyIncomingCallsParams, CallHierarchyItem, CallHierarchyOutgoingCall, CallHierarchyOutgoingCallsParams, CallHierarchyPrepareParams, Cancellable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/semantics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1416.5 | **LOC:** 2786 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (9.4437%), Tech Debt (26.8302%)
**Top Internal Functions/Classes:**
  * `descend_into_macros_impl` (Impact: 106.2)
  * `locals_used` (Impact: 41.0)
  * `is_inside_unsafe` (Impact: 33.5)
    * *Intent:* /// Returns `true` if the `node` is inside an `unsafe` context.
  * `lint_attrs` (Impact: 32.3)
  * `analyze_impl` (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 521`, `args: 373`, `func_start: 196`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 49`, `dead_code: 4`, `fragile_debt: 23`
* *Architecture:* `api: 178`, `import: 15`
* *Defense:* `safety: 54`, `doc: 102`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Adjustment, Adt, AnyFunctionId, AstToken, AutoBorrow, BindingMode, BuiltinAttr, Callable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/hover/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1401.1 | **LOC:** 11407 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (5.6306%), Tech Debt (81.6958%)
**Top Internal Functions/Classes:**
  * `hover_intra_inner_attr` (Impact: 20.0)
  * `hover_intra_outer_attr` (Impact: 20.0)
  * `type_alias_without_docs` (Impact: 18.1)
  * `drop_glue` (Impact: 17.6)
  * `hover_const_eval` (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 1022`, `args: 677`, `func_start: 660`, `class_start: 356`
* *Risk/State:* `safety_bypasses: 486`, `state_mutation: 108`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 254`
* *Architecture:* `api: 162`, `concurrency: 16`, `import: 32`
* *Defense:* `safety: 3`, `doc: 157`, `test: 283`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HoverDocFormat, MemoryLayoutHoverConfig, MemoryLayoutHoverRenderKind, Option::Some, b::B, base_db::SourceDatabase, c::C, core::fmt::Debug...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/eval/shim.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1334.14 | **LOC:** 1525 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 63.2%
- **Risk Profile:** Cognitive Load (16.9005%), Tech Debt (49.6977%)
**Top Internal Functions/Classes:**
  * `exec_intrinsic` (Impact: 657.1)
  * `exec_extern_c` (Impact: 172.2)
  * `exec_atomic_intrinsic` (Impact: 138.7)
  * `detect_and_exec_special_function` (Impact: 57.8)
  * `exec_clone` (Impact: 56.8)
    * *Intent:* /// Clone has special impls for tuples and function pointers
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 408`, `structural_boundaries: 470`, `args: 46`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 12`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 14`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 21`, `doc: 4`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AdtId, Arc, EvalLangItem::*, Evaluator, FunctionId, GenericArgs, HasModule, HirDisplay...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/tests/expression.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1232.06 | **LOC:** 3697 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 81.2%
- **Risk Profile:** Cognitive Load (8.3173%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `else_completion_after_if` (Impact: 370.9)
  * `inside_faulty_format_args_completions_work` (Impact: 184.9)
  * `completes_after_ref_expr` (Impact: 49.7)
  * `completes_let_else` (Impact: 34.4)
  * `let_in_previous_line_of_ambiguous_expr` (Impact: 32.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 688`, `structural_boundaries: 872`, `args: 352`, `func_start: 310`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 97`, `high_risk_execution: 1`, `fragile_debt: 1`, `unreferenced_by_name: 58`
* *Architecture:* `api: 22`, `concurrency: 39`, `import: 41`
* *Defense:* `safety: 116`, `doc: 2`, `test: 62`, `immutability_locks: 136`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TEST_CONFIG, _69latrick::*, check, check_edit, check_with_base_items, completion_list_with_config, config::AutoImportExclusionType, crate::
    CompletionConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/mir/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1207.22 | **LOC:** 2341 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 57.7%
- **Risk Profile:** Cognitive Load (21.7798%), Tech Debt (31.9902%)
**Top Internal Functions/Classes:**
  * `lower_expr_to_place_without_adjust` (Impact: 430.9)
  * `lower_block_to_place` (Impact: 51.5)
  * `lower_params_and_bindings` (Impact: 48.4)
  * `pretty_print` (Impact: 48.1)
  * `mir_body_for_closure_query` (Impact: 42.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 50 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 464`, `args: 101`, `func_start: 60`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 3`, `state_mutation: 80`, `dead_code: 6`, `fragile_debt: 11`, `unreferenced_by_name: 9`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 13`
* *Defense:* `safety: 81`, `doc: 21`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Adjustment, Arena, Array, AutoBorrow, BasicBlock, BasicBlockId, BinOp, BinaryOp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir/src/source_analyzer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1189.4 | **LOC:** 2014 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 48.1%
- **Risk Profile:** Cognitive Load (11.2896%), Tech Debt (90.6915%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 162.9)
  * `resolve_hir_path_` (Impact: 87.7)
  * `resolve_offset_of_field` (Impact: 37.5)
  * `resolve_hir_path_qualifier` (Impact: 37.2)
    * *Intent:* /// Resolves a path where we know it is a qualifier of another path. /// /// For example, if we have...
  * `resolve_record_field` (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 394`, `args: 183`, `func_start: 77`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `dead_code: 5`, `fragile_debt: 12`, `unreferenced_by_name: 39`
* *Architecture:* `api: 58`, `import: 13`
* *Defense:* `safety: 59`, `doc: 23`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyFunctionId, AssocItem, AssocItemId, AstNode, BindingMode, BodySourceMap, BuiltinAttr, BuiltinType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-def/src/expr_store/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1154.38 | **LOC:** 2961 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 42.3%
- **Risk Profile:** Cognitive Load (13.5399%), Tech Debt (35.0429%)
**Top Internal Functions/Classes:**
  * `maybe_collect_expr` (Impact: 113.9)
    * *Intent:* /// Returns `None` if and only if the expression is `#[cfg]`d out.
  * `collect_pat` (Impact: 70.2)
  * `lower_body` (Impact: 54.1)
  * `maybe_collect_expr_as_pat` (Impact: 51.7)
  * `lower_type_ref` (Impact: 30.1)
    * *Intent:* /// Converts an `ast::TypeRef` to a `hir::TypeRef`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 734`, `args: 274`, `func_start: 103`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 114`, `dead_code: 10`, `fragile_debt: 14`, `unreferenced_by_name: 12`
* *Architecture:* `api: 28`, `concurrency: 4`, `import: 14`
* *Defense:* `safety: 99`, `doc: 60`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArrayExprKind, AstChildren, AstPtr, Binding, BindingAnnotation, BindingId, BindingProblems, BlockExpr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide-completion/src/context/analysis.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1115.54 | **LOC:** 2116 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 82.4%
- **Risk Profile:** Cognitive Load (15.3962%), Tech Debt (11.3595%)
**Top Internal Functions/Classes:**
  * `classify_name_ref` (Impact: 476.7)
  * `expected_type_and_name` (Impact: 123.8)
    * *Intent:* /// Calculate the expected type and name of the cursor position.
  * `expand` (Impact: 100.5)
  * `analyze` (Impact: 80.6)
    * *Intent:* /// Fill the completion context, this is what does semantic reasoning about the surrounding context ...
  * `pattern_context_for` (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 418`, `args: 225`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`, `dead_code: 10`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 62`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AstToken, AttrKind, BreakableKind, COMPLETION_MARKER, CompletionAnalysis, Direction, DotAccess, DotAccessExprCtx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/goto_definition.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1107.6 | **LOC:** 4103 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (9.4184%), Tech Debt (8.8344%)
**Top Internal Functions/Classes:**
  * `goto_definition` (Impact: 67.7)
    * *Intent:* // Feature: Go to Definition // // Navigates to the definition of an identifier. // // For outline m...
  * `find_definition_for_known_blanket_dual_impls` (Impact: 67.5)
    * *Intent:* // If the token is into(), try_into(), search the definition of From, TryFrom.
  * `nav_for_exit_points` (Impact: 38.3)
  * `goto_question_mark_conversions` (Impact: 31.3)
    * *Intent:* /// When the `?` operator is used on `Result`, go to the `From` impl if it exists as this provides m...
  * `find_branch_root` (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 599`, `args: 473`, `func_start: 431`, `class_start: 168`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 7`, `dead_code: 3`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 222`, `concurrency: 7`, `import: 38`
* *Defense:* `safety: 14`, `doc: 26`, `test: 168`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001614
  * `Imports (Out-Degree: 1):` AssocItem, AstToken, CallableKind, FileRange, Foo::str, HasCrate, IdentClass, InFile...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/hir-ty/src/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1056.44 | **LOC:** 2681 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 55.8%
- **Risk Profile:** Cognitive Load (9.5967%), Tech Debt (78.3962%)
**Top Internal Functions/Classes:**
  * `resolve_type_param_assoc_type_shorthand` (Impact: 78.6)
    * *Intent:* /// Predicates for `param_id` of the form `P: SomeTrait`. If /// `assoc_name` is provided, only retu...
  * `lower_dyn_trait` (Impact: 60.2)
  * `generic_predicates` (Impact: 46.4)
    * *Intent:* /// Resolve the where clause(s) of an item with generics, /// with a given filter
  * `query` (Impact: 25.9)
  * `supertraits_info` (Impact: 25.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Amplified Sql Injection:* 6 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 504`, `args: 197`, `func_start: 111`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 96`, `dead_code: 9`, `fragile_debt: 22`, `unreferenced_by_name: 23`
* *Architecture:* `api: 100`, `import: 15`
* *Defense:* `safety: 31`, `doc: 93`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ArenaMap, AssocItemId, Binder, BoundExistentialPredicates, BoundVarIndexKind, CallableDefId, Clause, ClauseKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/rust-analyzer/src/lsp/to_proto.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1041.08 | **LOC:** 3091 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (12.0769%), Tech Debt (7.9681%)
**Top Internal Functions/Classes:**
  * `completion_item` (Impact: 142.3)
  * `code_lens` (Impact: 58.1)
  * `merge_text_and_snippet_edits` (Impact: 37.1)
  * `semantic_tokens` (Impact: 34.8)
  * `inlay_hint` (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 419`, `args: 174`, `func_start: 86`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 1`, `state_mutation: 76`, `fragile_debt: 1`
* *Architecture:* `api: 67`, `import: 23`
* *Defense:* `safety: 26`, `doc: 11`, `test: 33`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00142
  * `Imports (Out-Degree: 3):` AnnotationKind, Assist, AssistKind, Cancellable, ClientCommandsConfig, CompletionFieldsToResolve, CompletionItem, CompletionItemKind...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/config.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1033.04 | **LOC:** 4368 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 28.1%
- **Risk Profile:** Cognitive Load (3.4579%), Tech Debt (19.5325%)
**Top Internal Functions/Classes:**
  * `field_props` (Impact: 68.0)
  * `apply_change_with_sink` (Impact: 47.0)
    * *Intent:* // FIXME @alibektas : Server's health uses error sink but in other places it is not used atm. /// Ch...
  * `inlay_hints` (Impact: 23.8)
  * `cargo` (Impact: 19.8)
  * `lens` (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 514`, `args: 215`, `func_start: 149`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 51`, `dead_code: 2`, `planned_debt: 8`, `fragile_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 184`, `import: 25`
* *Defense:* `safety: 58`, `doc: 677`, `test: 29`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ::std::io::Read, AbsPathBuf, AssistConfig, CallHierarchyConfig, CallableSnippets, CargoFeatures, CfgDiff, CompletionConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/highlight_related.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1023.12 | **LOC:** 2552 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (14.1407%), Tech Debt (8.0556%)
**Top Internal Functions/Classes:**
  * `highlight_references` (Impact: 79.8)
  * `highlight_related` (Impact: 50.4)
    * *Intent:* // Feature: Highlight Related // // Highlights constructs related to the thing under the cursor: // ...
  * `hl` (Impact: 40.2)
  * `highlight_break_points` (Impact: 37.6)
  * `highlight_branch_exit_points` (Impact: 30.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 349`, `structural_boundaries: 325`, `args: 256`, `func_start: 186`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 28`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 91`, `concurrency: 44`, `import: 14`
* *Defense:* `safety: 30`, `doc: 3`, `test: 72`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.672
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001065
  * `Imports (Out-Degree: 1):` FilePosition, FileRange, FxHashSet, HasLoopBody, HirFileId, IDENT, INT_NUMBER, IdentClass...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/rust-analyzer/src/cli/analysis_stats.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1008.34 | **LOC:** 1651 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 44.1%
- **Risk Profile:** Cognitive Load (29.5313%), Tech Debt (15.5026%)
**Top Internal Functions/Classes:**
  * `run_inference` (Impact: 236.2)
  * `run_body_lowering` (Impact: 145.8)
  * `run_term_search` (Impact: 119.9)
    * *Intent:* /// Invariant: `file_ids` must be sorted and deduped before passing into here
  * `run` (Impact: 100.4)
  * `run_mir_lowering` (Impact: 50.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 386`, `args: 105`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 65`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 18`
* *Defense:* `safety: 38`, `doc: 4`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnalysisHost, AnnotationConfig, AssocItem, BodySourceMap, CfgDiff, CfgOverrides, Crate, DefWithBody...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/ide/src/rename.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 996.9 | **LOC:** 3934 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (9.6687%), Tech Debt (12.5334%)
**Top Internal Functions/Classes:**
  * `transform_method_call_into_assoc_fn` (Impact: 80.0)
  * `find_definitions` (Impact: 67.0)
  * `transform_assoc_fn_into_method_call` (Impact: 60.2)
  * `rename_to_self` (Impact: 40.4)
  * `rename` (Impact: 33.4)
    * *Intent:* // Feature: Rename // // Renames the item below the cursor and all of its references // // | Editor ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 560`, `args: 415`, `func_start: 331`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 7`, `state_mutation: 40`, `dead_code: 10`, `fragile_debt: 13`
* *Architecture:* `api: 151`, `import: 43`
* *Defense:* `safety: 36`, `doc: 9`, `test: 122`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FileRange, FindPathConfig, Foo, HasArgList, HasContainer, HirDisplay, InFile, Name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-def/src/nameres/collector.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 993.72 | **LOC:** 2839 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 63.2%
- **Risk Profile:** Cognitive Load (8.1294%), Tech Debt (36.04%)
**Top Internal Functions/Classes:**
  * `push_res_and_update_glob_vis` (Impact: 89.8)
  * `collect` (Impact: 75.5)
  * `resolve_macros` (Impact: 72.6)
  * `record_resolved_import` (Impact: 50.4)
  * `seed_with_top_level` (Impact: 42.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 62 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 448`, `args: 103`, `func_start: 41`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 4`, `state_mutation: 102`, `dead_code: 7`, `planned_debt: 4`, `fragile_debt: 16`, `unreferenced_by_name: 4`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 80`, `doc: 107`, `test: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AssocItemId, AstId, AstIdWithPath, AttrId, Attrs, AttrsOrCfg, BuiltinDeriveImplId, BuiltinDeriveImplLoc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-def/src/attrs.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 979.08 | **LOC:** 1695 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 58.3%
- **Risk Profile:** Cognitive Load (15.5227%), Tech Debt (9.995%)
**Top Internal Functions/Classes:**
  * `parse_repr_tt` (Impact: 38.3)
  * `match_attr_flags` (Impact: 33.7)
  * `derive_info` (Impact: 28.3)
  * `find_ast_range` (Impact: 27.0)
  * `derive_info` (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *Amplified Sql Injection:* 7 instances
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 384`, `args: 134`, `func_start: 67`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 113`, `fragile_debt: 3`
* *Architecture:* `api: 39`, `import: 23`
* *Defense:* `safety: 43`, `doc: 48`, `test: 14`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AstIdLoc, AstToken, AttrDefId, AttrDocCommentIter, BuiltinUint, CfgOptions, Docs, FieldId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/infer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 964.04 | **LOC:** 2254 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.6465%), Tech Debt (99.9088%)
**Top Internal Functions/Classes:**
  * `resolve_variant` (Impact: 117.2)
  * `resolve_all` (Impact: 41.8)
    * *Intent:* // FIXME: This function should be private in module. It is currently only used in the consteval, sin...
  * `struct_tail_with_normalize` (Impact: 28.3)
    * *Intent:* /// Returns the deeply last field of nested structures, or the same type if /// not a structure at a...
  * `infer_query_with_inspect` (Impact: 18.6)
  * `collect_fn` (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 348`, `args: 180`, `func_start: 126`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 88`, `dead_code: 5`, `fragile_debt: 30`, `unreferenced_by_name: 65`
* *Architecture:* `api: 96`, `import: 20`
* *Defense:* `safety: 43`, `doc: 230`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AssocItemId, BindingId, CapturedItem, CapturedItemWithoutTy, CastError, Const, ConstId, ConstParamId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/hir-ty/src/tests/traits.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 953.0 | **LOC:** 5246 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 70.6%
- **Risk Profile:** Cognitive Load (4.8247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `more_qualified_paths` (Impact: 19.7)
  * `iterator_chain` (Impact: 19.4)
  * `proc_macro_server_types` (Impact: 13.4)
  * `associated_type_in_struct_expr_path_enum` (Impact: 13.3)
  * `closure_as_argument_inference_order` (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 1224`, `args: 679`, `func_start: 564`, `class_start: 325`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 3`, `dead_code: 3`, `fragile_debt: 8`, `unreferenced_by_name: 172`
* *Architecture:* `api: 52`, `concurrency: 99`, `import: 29`
* *Defense:* `safety: 10`, `test: 282`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alloc::collections::Vec, check_infer, check_infer_with_mismatches, check_no_mismatches, check_types, core::default::Default::default, core::future::Future, core::marker::PhantomData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/syntax/src/ast/make.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 929.78 | **LOC:** 1564 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (9.5206%), Tech Debt (14.7647%)
**Top Internal Functions/Classes:**
  * `fn_` (Impact: 49.0)
  * `impl_trait` (Impact: 45.4)
  * `item_static` (Impact: 19.6)
  * `impl_` (Impact: 17.1)
  * `hacky_block_expr` (Impact: 15.2)
    * *Intent:* /// Ideally this function wouldn't exist since it involves manual indenting. /// It differs from `ma...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 306`, `args: 307`, `func_start: 195`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 6`, `state_mutation: 13`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 178`, `concurrency: 4`, `import: 20`
* *Defense:* `safety: 56`, `doc: 29`, `test: 9`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.401
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.028708
  * `Imports (Out-Degree: 2):` *, Param, Parse, SourceFile, SyntaxKind, SyntaxKind::*, SyntaxToken, T...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/hir/src/lib.rs` -> Churn: **100.0%** | Cog Load: 8.6793% | Debt: 99.9727%
- `crates/hir-ty/src/lower.rs` -> Churn: **92.84%** | Cog Load: 9.5967% | Debt: 78.3962%
- `crates/hir-ty/src/next_solver/interner.rs` -> Churn: **92.39%** | Cog Load: 10.0202% | Debt: 85.2534%
- `crates/hir-ty/src/infer.rs` -> Churn: **87.95%** | Cog Load: 12.6465% | Debt: 99.9088%
- `crates/syntax/src/ast/syntax_factory/constructors.rs` -> Churn: **87.95%** | Cog Load: 7.6281% | Debt: 95.3488%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/ide-completion/src/tests/expression.rs` -> **A4-Tacks** (81.2% isolated ownership) | Magnitude: 1232.06
- `crates/ide-completion/src/context/analysis.rs` -> **A4-Tacks** (82.4% isolated ownership) | Magnitude: 1115.54
- `crates/syntax/src/ast/make.rs` -> **A4-Tacks** (85.7% isolated ownership) | Magnitude: 929.78
- `crates/syntax/src/ast/syntax_factory/constructors.rs` -> **bit-aloo** (81.0% isolated ownership) | Magnitude: 875.68
- `crates/hir-def/src/find_path.rs` -> **Lukas Wirth** (100.0% isolated ownership) | Magnitude: 674.3

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/syntax/src/ast/make.rs` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 18.6345%)
- `crates/syntax/src/syntax_editor.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 32.3817%)
- `editors/code/src/toolchain.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 96.0509%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/syntax/src/ast.rs` -> **Severity: 5.915** (Embedded: 0.0663 * Error Risk: 89.2064%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 1.487** (Embedded: 0.0287 * Error Risk: 51.7873%)
- `crates/ide-completion/src/tests/use_tree.rs` -> **Severity: 1.128** (Embedded: 0.0161 * Error Risk: 70.1341%)
- `crates/tt/src/iter.rs` -> **Severity: 1.052** (Embedded: 0.0143 * Error Risk: 73.4211%)
- `crates/syntax/src/ted.rs` -> **Severity: 0.536** (Embedded: 0.0105 * Error Risk: 51.2051%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/syntax/src/ast.rs` -> **Severity: 4701.326** (Blast Radius: 52.142 * Doc Risk: 90.1639%)
- `crates/syntax/src/ast/make.rs` -> **Severity: 1871.378** (Blast Radius: 19.401 * Doc Risk: 96.4578%)
- `crates/ide-completion/src/tests/use_tree.rs` -> **Severity: 850.786** (Blast Radius: 8.913 * Doc Risk: 95.4545%)
- `crates/tt/src/iter.rs` -> **Severity: 769.908** (Blast Radius: 9.988 * Doc Risk: 77.0833%)
- `crates/syntax/src/ted.rs` -> **Severity: 452.868** (Blast Radius: 4.634 * Doc Risk: 97.7273%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
