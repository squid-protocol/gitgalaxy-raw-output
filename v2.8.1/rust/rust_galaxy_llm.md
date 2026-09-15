# ARCHITECTURAL_BRIEF: rust
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/rust.git` |
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
| Total Artifacts | 58763 |
| Analyzed Artifacts (Scanned) | 37425 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21338 |
| Total LOC | 2451166 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.7% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8874 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2727 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7641 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 235 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 34934 | 2379022 | 93.3% |
| MARKDOWN | 1370 | 0 | 3.7% |
| PLAINTEXT | 226 | 0 | 0.6% |
| SHELL | 159 | 11347 | 0.4% |
| JAVASCRIPT | 136 | 15570 | 0.4% |
| DOCKERFILE | 112 | 3054 | 0.3% |
| C | 110 | 8694 | 0.3% |
| HTML | 105 | 1542 | 0.3% |
| YAML | 45 | 3058 | 0.1% |
| JSON | 39 | 1417 | 0.1% |
| PYTHON | 35 | 7072 | 0.1% |
| ASSEMBLY | 30 | 3058 | 0.1% |
| TYPESCRIPT | 29 | 6437 | 0.1% |
| XML | 28 | 0 | 0.1% |
| CPP | 19 | 3856 | 0.1% |
| CSS | 11 | 4316 | 0.0% |
| MAKEFILE | 10 | 266 | 0.0% |
| BATCH | 9 | 39 | 0.0% |
| POWERSHELL | 4 | 2080 | 0.0% |
| BINARY_THREAT | 4 | 4 | 0.0% |
| M4 | 3 | 30 | 0.0% |
| NIX | 3 | 118 | 0.0% |
| SCHEME | 2 | 180 | 0.0% |
| YACC | 1 | 5 | 0.0% |
| PERL | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +1.29; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, State Mutators Files 22%, Interface Declarations Files 9%, Generic / Templated Code Files 8%, Annotated Framework Methods Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 35821 | 95.7% |
| Unknown | 4 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1598 | 4.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21338*

**Composition by Extension & Reason:**
- `.stderr`: 12852x Excluded (Unsupported Extension: '.stderr'), 2003x Unsupported Format (.stderr), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 1165x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 202x Excluded: Neighborhood Micro-Mass Limit Exceeded, 67x Unsupported Format (.undeterminable)
- `.fixed`: 1297x Unsupported Format (.fixed)
- `.diff`: 847x Excluded (Unsupported Extension: '.diff'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.diff)
- `.toml`: 556x Unsupported Format (.toml), 23x Excluded (Unsupported Extension: '.toml'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rast`: 505x Unsupported Format (.rast), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.stdout`: 298x Excluded (Unsupported Extension: '.stdout'), 44x Unsupported Format (.stdout), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mir`: 357x Unsupported Format (.mir)
- `.goml`: 142x Excluded (Unsupported Extension: '.goml')
- `no_extension`: 56x Unsupported Format (.undeterminable), 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3180 LOC)
- `.coverage`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.coverage')
- `.cov-map`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 25x Unsupported Format (.lock), 15x Excluded (Unsupported Extension: '.lock'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 15827 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1226 LOC)
- `.snap`: 49x Unsupported Format (.snap)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 93.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 74.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 83.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 140509 | 16415 | 7 | `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` |
| cleanup | 2005 | 835 | 0 | `tests/ui/borrowck/borrowck-field-sensitivity-rpass.rs` |
| guards | 75293 | 10522 | 4 | `compiler/rustc_codegen_llvm/src/llvm/ffi.rs` |
| danger | 37234 | 6297 | 2 | `src/tools/rust-analyzer/crates/ide/src/hover/tests.rs` |
| concurrency | 18232 | 3103 | 0 | `src/librustdoc/html/static/js/search.js` |
| connectivity | 120192 | 16257 | 5 | `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` |
| io | 4614 | 1121 | 0 | `src/bootstrap/bootstrap.py` |
| crypto | 3 | 3 | 0 | `src/bootstrap/bootstrap.py` |
| ipc | 335 | 253 | 0 | `src/bootstrap/bootstrap.py` |
| time | 355 | 146 | 0 | `src/etc/completions/x.fish` |
| serialization | 188 | 94 | 0 | `src/tools/rustdoc-js/tester.js` |
| regex | 373 | 152 | 0 | `src/librustdoc/html/static/js/search.js` |
| events | 5422 | 906 | 0 | `compiler/rustc_trait_selection/src/traits/select/mod.rs` |
| tests | 58940 | 6303 | 2 | `library/alloc/src/collections/btree/map/tests.rs` |
| docs | 318861 | 7159 | 5 | `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` |
| debt | 28237 | 7101 | 2 | `library/std_detect/tests/cpu-detection.rs` |
| mutation | 312802 | 20176 | 15 | `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` |
| dead_code | 95457 | 29033 | 4 | `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` |
| credential | 80 | 38 | 0 | `tests/codegen-llvm/sanitizer/cfi/emit-type-metadata-id-itanium-cxx-abi-trait-types.rs` |
| threat | 9801 | 3594 | 0 | `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` |
| ml_ai | 12665 | 1583 | 0 | `library/compiler-builtins/crates/musl-math-sys/src/lib.rs` |
| ui | 338 | 44 | 0 | `src/librustdoc/html/static/css/rustdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/bootstrap/bootstrap.py` (Hits: 122)
- `library/std/src/fs/tests.rs` (Hits: 95)
- `src/etc/completions/x.py.zsh` (Hits: 74)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Node.html** (`src/tools/generate-copyright/templates/Node.html`) — 158 inbound connections
2. **trace.rs** (`compiler/rustc_borrowck/src/type_check/liveness/trace.rs`) — 93 inbound connections
3. **find_attr.rs** (`tests/ui-fulldeps/internal-lints/find_attr.rs`) — 92 inbound connections
4. **html.rs** (`src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/html.rs`) — 45 inbound connections
5. **smallvec.rs** (`src/tools/miri/tests/pass/both_borrows/smallvec.rs`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`compiler/rustc_middle/src/ty/mod.rs`) — 238 outbound dependencies
2. **SUMMARY.md** (`src/doc/rustc-dev-guide/src/SUMMARY.md`) — 229 outbound dependencies
3. **lib.rs** (`src/tools/rust-analyzer/crates/hir/src/lib.rs`) — 197 outbound dependencies
4. **mod.rs** (`library/compiler-builtins/libm/src/math/mod.rs`) — 190 outbound dependencies
5. **lib.rs** (`src/tools/clippy/clippy_utils/src/lib.rs`) — 171 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `banana` **(Compute Cores)** (@ `tests/ui/expr/if/expr-stack-overflow.rs`) -> Impact: **3730.8** | LOC: 2548
  * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-tidy-filelength #![crate_type = "rlib"]
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/unix/foreign_items.rs`) -> Impact: **1230.4** | LOC: 1190
- `eval_simd_intrinsic` **(Many-Argument Workhorses)** (@ `compiler/rustc_const_eval/src/interpret/intrinsics/simd.rs`) -> Impact: **846.6** | LOC: 792
  * *Intent:* /// Returns `true` if emulation happened. /// Here we implement the intrinsics that are common to all CTFE instances; individual machines can add thei...
- `initSearch` **(Many-Argument Workhorses)** (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **816.4** | LOC: 1967
  * *Intent:* /** * @param {stringdex.Stringdex} Stringdex * @param {typeof stringdex.RoaringBitmap} RoaringBitmap * @param {stringdex.Hooks} hooks */
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/windows/foreign_items.rs`) -> Impact: **804.0** | LOC: 1187
- `exec_intrinsic` **(Many-Argument Workhorses)** (@ `src/tools/rust-analyzer/crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **657.1** | LOC: 783
- `execQuery` **(Many-Argument Workhorses)** (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **591.4** | LOC: 1387
  * *Intent:* /** * Executes the parsed query and builds a {ResultsTable}. * * @param {rustdoc.ParsedQuery<rustdoc.ParserQueryElement>} parsedQuery * - The parsed u...
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/foreign_items.rs`) -> Impact: **577.8** | LOC: 631
- `note_obligation_cause_code` **(Many-Argument Workhorses)** (@ `compiler/rustc_trait_selection/src/error_reporting/traits/suggestions.rs`) -> Impact: **550.6** | LOC: 1053
- `LLVMRustOptimize` **(Many-Argument Workhorses)** (@ `compiler/rustc_llvm/llvm-wrapper/PassWrapper.cpp`) -> Impact: **510.4** | LOC: 388

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `library/stdarch/crates/core_arch/src/x86` | 48 | 21131.78 | 2.47% | 69.11% |
| `compiler/rustc_mir_transform/src` | 78 | 12674.94 | 11.29% | 65.96% |
| `src/librustdoc/html/static/js` | 11 | 11571.9 | 27.77% | 20.66% |
| `compiler/rustc_parse/src/parser` | 16 | 11222.64 | 10.46% | 23.68% |
| `compiler/rustc_hir_typeck/src` | 27 | 10991.54 | 7.97% | 41.63% |
| `compiler/rustc_resolve/src` | 12 | 10441.42 | 10.98% | 40.77% |
| `compiler/rustc_middle/src/ty` | 38 | 8596.48 | 6.43% | 53.32% |
| `compiler/rustc_lint/src` | 53 | 8412.14 | 7.37% | 42.23% |
| `compiler/rustc_borrowck/src/diagnostics` | 13 | 6970.18 | 10.39% | 45.28% |
| `src/librustdoc/html/render` | 11 | 6777.52 | 13.91% | 38.87% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/tools/clippy/.github/ISSUE_TEMPLATE/false_negative.yml` -> **100.0%** Exposure
- `compiler/rustc_ast_pretty/src/pp/ring.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_gcc/src/declare.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_gcc/src/mono_item.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_gcc/src/type_.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compiler/rustc_ast/src/util/comments.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_cranelift/scripts/rustc-clif.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_cranelift/scripts/rustdoc-clif.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_gcc/build_system/src/fuzz/reduce.rs` -> **100.0%** Exposure
- `compiler/rustc_session/src/config/cfg.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` -> **1186** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` -> **934** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` -> **826** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` -> **555** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/mips/msa.rs` -> **527** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/ci/citool/tests/test-jobs.yml` -> **99.9973%** Exposure
- `src/ci/github-actions/jobs.yml` -> **98.5331%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `38` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `110620` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/etc/lldb_providers.py` (PYTHON) -> Cumulative Risk: **742.44**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.13)
- **Magnitude:** 1285.76 | **LOC:** 1400 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.3122%)
- **Heaviest Functions:** `update` (Compute Cores, Impact: 39.4), `sequence_formatter` (Many-Argument Workhorses, Impact: 15.2), `MSVCEnumSummaryProvider` (Many-Argument Workhorses, Impact: 14.3)

### 2. `src/etc/gdb_providers.py` (PYTHON) -> Cumulative Risk: **713.44**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.71)
- **Magnitude:** 611.7 | **LOC:** 504 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9991%), Safety Score (99.6653%)
- **Heaviest Functions:** `children_of_btree_map` (Compute Cores, Impact: 23.7), `children_of_node` (Compute Cores, Impact: 22.7), `__init__` (Type Conversions, Impact: 11.2)

### 3. `src/tools/rust-analyzer/editors/code/src/tasks.ts` (TYPESCRIPT) -> Cumulative Risk: **665.59**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.67)
- **Magnitude:** 0.11 | **LOC:** 147 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `targetToExecution` (Defensive Guards, Impact: 35.2), `buildRustTask` (Many-Argument Workhorses, Impact: 8.2), `provideTasks` (I/O & Config Routines, Impact: 6.2)

### 4. `library/alloc/src/collections/btree/map/tests.rs` (RUST) -> Cumulative Risk: **658.04**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Tests & Verification Files` (z +1.93)
- **Magnitude:** 1306.52 | **LOC:** 2798 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9966%), Tech Debt (96.4802%)
- **Heaviest Functions:** `test_clone_panic_leak` (Compute Cores, Impact: 22.3), `test_basic_large` (Tests & Verification, Impact: 13.6), `test_ord_absence` (Tests & Verification, Impact: 11.3)

### 5. `compiler/rustc_errors/src/lib.rs` (RUST) -> Cumulative Risk: **655.29**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.49)
- **Magnitude:** 679.48 | **LOC:** 1710 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 42.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.364%), State Flux (83.2502%), Verification (80.0%)
- **Heaviest Functions:** `emit_diagnostic` (Many-Argument Workhorses, Impact: 68.4), `print_error_count` (Compute Cores, Impact: 26.7), `flush_delayed` (Compute Cores, Impact: 16.3)

### 6. `src/tools/rust-analyzer/editors/code/src/commands.ts` (TYPESCRIPT) -> Cumulative Risk: **652.0**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +1.14)
- **Magnitude:** 0.88 | **LOC:** 1553 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Documentation (99.2647%), State Flux (81.0247%)
- **Heaviest Functions:** `viewFileUsingTextDocumentContentProvider` (Many-Argument Workhorses, Impact: 20.6), `asWorkspaceSnippetEdit` (Compute Cores, Impact: 18.0), `elementToString` (Defensive Guards, Impact: 15.2)

### 7. `library/std/src/io/cursor.rs` (RUST) -> Cumulative Risk: **645.31**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z -1.02)
- **Magnitude:** 265.16 | **LOC:** 758 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (86.3725%), Verification (80.0%)
- **Heaviest Functions:** `slice_write_vectored` (Many-Argument Workhorses, Impact: 10.8), `reserve_and_pad` (Many-Argument Workhorses, Impact: 10.0), `vec_write_all_vectored` (Many-Argument Workhorses, Impact: 9.4)

### 8. `library/core/src/slice/iter.rs` (RUST) -> Cumulative Risk: **643.25**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.01)
- **Magnitude:** 961.66 | **LOC:** 3188 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7948%), Documentation (93.0556%), State Flux (81.4555%)
- **Heaviest Functions:** `next` (Defensive Guards, Impact: 10.7), `next_back` (Defensive Guards, Impact: 10.7), `next` (Defensive Guards, Impact: 10.6)

### 9. `library/core/src/fmt/mod.rs` (RUST) -> Cumulative Risk: **642.95**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.82)
- **Magnitude:** 870.28 | **LOC:** 3185 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Dead Code (96.1296%), Tech Debt (94.7713%), State Flux (94.6716%)
- **Heaviest Functions:** `pad_integral` (Many-Argument Workhorses, Impact: 51.9), `write` (Many-Argument Workhorses, Impact: 41.9), `fmt` (Compute Cores, Impact: 24.8)

### 10. `library/core/src/range/iter.rs` (RUST) -> Cumulative Risk: **642.36**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z -0.84)
- **Magnitude:** 114.5 | **LOC:** 447 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (91.6667%), Verification (80.0%)
- **Heaviest Functions:** `nth` (Defensive Guards, Impact: 9.9), `next` (Compute Cores, Impact: 7.2), `remainder` (Annotated Framework Methods, Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/librustdoc/html/static/js/search.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 6150.38 | **LOC:** 5573 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.7388%), Tech Debt (13.099%)
**Top Internal Functions/Classes:**
  * `initSearch` **(Many-Argument Workhorses)** (Impact: 816.4)
    * *Intent:* /** * @param {stringdex.Stringdex} Stringdex * @param {typeof stringdex.RoaringBitmap} RoaringBitmap...
  * `execQuery` **(Many-Argument Workhorses)** (Impact: 591.4)
    * *Intent:* /** * Executes the parsed query and builds a {ResultsTable}. * * @param {rustdoc.ParsedQuery<rustdoc...
  * `innerRunTypeQuery` **(Many-Argument Workhorses)** (Impact: 260.4)
  * `unifyFunctionTypes` **(Many-Argument Workhorses)** (Impact: 179.5)
    * *Intent:* * @param {rustdoc.QueryElement[]} queryElems - The elements from the parsed query. * @param {rustdoc...
  * `getNextElem` **(Many-Argument Workhorses)** (Impact: 136.5)
    * *Intent:* /** * @param {rustdoc.ParsedQuery<rustdoc.ParserQueryElement>} query * @param {rustdoc.ParserState} ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 51 instances
* *Amplified Cascading Flux:* 398 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 463
* *State Mutation (weighted view):* 1275
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1045`, `structural_boundaries: 653`, `args: 200`, `func_start: 114`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 10`, `state_mutation: 479`, `dead_code: 8`, `fragile_debt: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 2`, `concurrency: 208`
* *Defense:* `safety: 481`, `doc: 164`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5413.2 | **LOC:** 27594 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.7842%), Tech Debt (99.1678%)
**Top Internal Functions/Classes:**
  * `_mm512_set_ph` **(Many-Argument Workhorses)** (Impact: 7.9)
    * *Intent:* /// Set packed half-precision (16-bit) floating-point elements in dst with the supplied values. /// ...
  * `_mm512_setr_ph` **(Many-Argument Workhorses)** (Impact: 7.9)
    * *Intent:* /// Set packed half-precision (16-bit) floating-point elements in dst with the supplied values in re...
  * `_mm_mask_fmadd_round_sh` **(Annotated Framework Methods)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
  * `_mm_mask3_fmadd_round_sh` **(Annotated Framework Methods)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
  * `_mm_maskz_fmadd_round_sh` **(Annotated Framework Methods)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 4054`, `args: 1992`, `func_start: 1992`
* *Risk/State:* `state_mutation: 35`, `dead_code: 11`, `fragile_debt: 2`, `unreferenced_by_name: 934`
* *Architecture:* `api: 923`, `import: 8`
* *Defense:* `doc: 6405`, `test: 60`, `immutability_locks: 349`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` addr_of_mut, crate::arch::asm, crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::intrinsics::fmaf16, crate::ptr, crate::ptr::addr_of...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4635.1 | **LOC:** 22275 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (2.6616%), Tech Debt (98.7604%)
**Top Internal Functions/Classes:**
  * `_mm512_alignr_epi8` **(Type Conversions)** (Impact: 17.4)
    * *Intent:* /// Concatenate pairs of 16-byte blocks in a and b into a 32-byte temporary result, shift the result...
  * `_mm512_bslli_epi128` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* /// Shift 128-bit lanes in a left by imm8 bytes while shifting in zeros, and store the results in ds...
  * `_mm512_bsrli_epi128` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* /// Shift 128-bit lanes in a right by imm8 bytes while shifting in zeros, and store the results in d...
  * `mask` **(Type Conversions)** (Impact: 7.3)
  * `mask` **(Type Conversions)** (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 4231`, `args: 1718`, `func_start: 1676`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`, `unreferenced_by_name: 826`
* *Architecture:* `api: 826`, `import: 7`
* *Defense:* `doc: 2524`, `test: 331`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    core_arch::simd::*, crate::core_arch::assert_eq_const, crate::core_arch::x86::*, crate::hint::black_box, crate::mem::self, intrinsics::simd::*, ptr, stdarch_test::assert_instr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/expr/if/expr-stack-overflow.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3939.12 | **LOC:** 10421 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4342%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `banana` **(Compute Cores)** (Impact: 3730.8)
    * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-ti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10410`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/mips/msa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3783.4 | **LOC:** 18398 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (97.7947%)
**Top Internal Functions/Classes:**
  * `test_msa_binsl_b` **(Tests & Verification)** (Impact: 3.0)
  * `test_msa_binsr_b` **(Tests & Verification)** (Impact: 3.0)
  * `test_msa_bmnz_v` **(Tests & Verification)** (Impact: 3.0)
  * `test_msa_bmz_v` **(Tests & Verification)** (Impact: 3.0)
  * `test_msa_bsel_v` **(Tests & Verification)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1496`, `args: 1573`, `func_start: 1573`, `class_start: 10`
* *Risk/State:* `dead_code: 85`, `fragile_debt: 15`, `unreferenced_by_name: 527`
* *Architecture:* `api: 537`, `import: 4`
* *Defense:* `doc: 3559`, `test: 527`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
        core_arch::mips::msa::*, crate::mem, mem, simd::*, stdarch_test::assert_instr, stdarch_test::simd_test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/librustdoc/html/static/js/stringdex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3760.66 | **LOC:** 4412 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.1261%), Tech Debt (14.4105%)
**Top Internal Functions/Classes:**
  * `loadDatabase` **(Compute Cores)** (Impact: 424.2)
    * *Intent:* /** * @param {stringdex.Hooks} hooks * @returns {Promise<stringdex.Database>} */
  * `makeSearchTreeFromBase64` **(Compute Cores)** (Impact: 212.8)
    * *Intent:* /** * @param {string} inputBase64 * @returns {[Uint8Array, SearchTree]} */
  * `makeBranchesFromBinaryData` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* /** * @param {Uint8Array} input * @param {number} i * @param {number} compression_tag * @returns {{ ...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 82.7)
    * *Intent:* /** * @param {Uint8Array|null} u8array * @param {number} [startingOffset] */
  * `intersection` **(Compute Cores)** (Impact: 54.8)
    * *Intent:* /** * @param {RoaringBitmap} that * @returns {RoaringBitmap} */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 527 instances
* *Concurrency (weighted view):* 155
* *State Mutation (weighted view):* 1858
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 634`, `structural_boundaries: 424`, `args: 128`, `func_start: 112`, `class_start: 20`
* *Risk/State:* `state_mutation: 804`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `concurrency: 45`
* *Defense:* `safety: 188`, `doc: 197`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 3.6e-05
  * `Imports (Out-Degree: 1):` stringdex.d.ts
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_trait_selection/src/error_reporting/traits/suggestions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3513.1 | **LOC:** 6062 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (15.9093%), Tech Debt (15.1626%)
**Top Internal Functions/Classes:**
  * `note_obligation_cause_code` **(Many-Argument Workhorses)** (Impact: 550.6)
  * `note_function_argument_obligation` **(Many-Argument Workhorses)** (Impact: 188.2)
  * `suggest_add_reference_to_arg` **(Many-Argument Workhorses)** (Impact: 148.3)
  * `suggest_dereferences` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* /// Provide a suggestion to dereference arguments to functions and binary operators, if that /// wou...
  * `point_at_assoc_type_restriction` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* /// On `impl` evaluation cycles, look for `Self::AssocTy` restrictions in `where` clauses, explain /...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 105 instances
* *Concurrency (weighted view):* 71
* *State Mutation (weighted view):* 338
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1018`, `structural_boundaries: 1353`, `args: 256`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 128`, `dead_code: 13`, `planned_debt: 15`, `fragile_debt: 22`
* *Architecture:* `api: 46`, `concurrency: 41`, `import: 38`
* *Defense:* `safety: 181`, `doc: 96`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AdtKind, AmbigArg, CoroutineDesugaring, CoroutineKind, CoroutineSource, DUMMY_SP, DefKind, DefineOpaqueTypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_typeck/src/method/suggest.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3191.8 | **LOC:** 4893 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (14.4079%), Tech Debt (13.3627%)
**Top Internal Functions/Classes:**
  * `suggest_traits_to_import` **(Many-Argument Workhorses)** (Impact: 462.4)
  * `handle_unsatisfied_predicates` **(Many-Argument Workhorses)** (Impact: 353.8)
  * `report_failed_method_call_on_numerical_infer_var` **(Many-Argument Workhorses)** (Impact: 112.8)
  * `report_method_error` **(Many-Argument Workhorses)** (Impact: 112.1)
  * `note_candidates_on_method_error` **(Many-Argument Workhorses)** (Impact: 112.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 801`, `structural_boundaries: 979`, `args: 252`, `func_start: 59`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 117`, `dead_code: 11`, `planned_debt: 16`, `fragile_debt: 13`
* *Architecture:* `api: 10`, `concurrency: 5`, `import: 48`
* *Defense:* `safety: 139`, `doc: 29`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` CandidateTraitNote, DefKind, Diag, ErrorGuaranteed, ExpnKind, ExprKind, FileName, FnCtxt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_borrowck/src/diagnostics/conflict_errors.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2772.5 | **LOC:** 4741 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (12.5026%), Tech Debt (26.7813%)
**Top Internal Functions/Classes:**
  * `suggest_ref_or_clone` **(Many-Argument Workhorses)** (Impact: 195.4)
  * `suggest_cloning` **(Many-Argument Workhorses)** (Impact: 140.3)
  * `explain_iterator_advancement_in_for_loop_if_applicable` **(Many-Argument Workhorses)** (Impact: 119.9)
    * *Intent:* /// Suggest using `while let` for call `next` on an iterator in a for loop. /// /// For example: ///...
  * `report_use_of_moved_or_uninitialized` **(Many-Argument Workhorses)** (Impact: 119.5)
  * `suggest_slice_method_if_applicable` **(Many-Argument Workhorses)** (Impact: 104.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 791`, `structural_boundaries: 1044`, `args: 174`, `func_start: 68`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 120`, `dead_code: 34`, `planned_debt: 4`, `fragile_debt: 16`, `duplicate_logic: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `concurrency: 8`, `import: 52`
* *Defense:* `safety: 149`, `doc: 110`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AggregateKind, BindingForm, BorrowKind, ClearCrossCrate, ConstraintCategory, CoroutineKind, CoroutineSource, Diag...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/hexagon/v128.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2533.44 | **LOC:** 7490 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9162%)
**Top Internal Functions/Classes:**
  * `q6_vgather_aqrmvh` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vv32.h).h` /// /// This is a compound operation composed of mu...
  * `q6_vgather_aqrmww` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vvv32.w).h` /// /// This is a compound operation composed of m...
  * `q6_vgather_aqrmvw` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.w=vgather(Rt32,Mu2,Vv32.w).w` /// /// This is a compound operation composed of mu...
  * `q6_vscatter_qrmvhv` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vv32.h).h=Vw32` /// /// This is a compound operation composed of mul...
  * `q6_vscatter_qrmwwv` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vvv32.w).h=Vw32` /// /// This is a compound operation composed of mu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 952`, `func_start: 952`, `class_start: 3`
* *Risk/State:* `unreferenced_by_name: 476`
* *Architecture:* `api: 479`, `import: 2`
* *Defense:* `doc: 2036`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::intrinsics::simd::simd_add, simd_and, simd_or, simd_sub, simd_xor, stdarch_test::assert_instr
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/hexagon/v64.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2533.44 | **LOC:** 7490 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9162%)
**Top Internal Functions/Classes:**
  * `q6_vgather_aqrmvh` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vv32.h).h` /// /// This is a compound operation composed of mu...
  * `q6_vgather_aqrmww` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vvv32.w).h` /// /// This is a compound operation composed of m...
  * `q6_vgather_aqrmvw` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.w=vgather(Rt32,Mu2,Vv32.w).w` /// /// This is a compound operation composed of mu...
  * `q6_vscatter_qrmvhv` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vv32.h).h=Vw32` /// /// This is a compound operation composed of mul...
  * `q6_vscatter_qrmwwv` **(Annotated Framework Methods)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vvv32.w).h=Vw32` /// /// This is a compound operation composed of mu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 952`, `func_start: 952`, `class_start: 3`
* *Risk/State:* `unreferenced_by_name: 476`
* *Architecture:* `api: 479`, `import: 2`
* *Defense:* `doc: 2036`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::intrinsics::simd::simd_add, simd_and, simd_or, simd_sub, simd_xor, stdarch_test::assert_instr
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/late/diagnostics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2494.14 | **LOC:** 4585 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (11.4665%), Tech Debt (10.0252%)
**Top Internal Functions/Classes:**
  * `smart_resolve_context_dependent_help` **(Many-Argument Workhorses)** (Impact: 251.2)
    * *Intent:* /// Provides context-dependent help for errors reported by the `smart_resolve_path_fragment` /// fun...
  * `add_missing_lifetime_specifiers_label` **(Many-Argument Workhorses)** (Impact: 214.2)
  * `try_lookup_name_relaxed` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `suggest_assoc_type_from_bounds` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /// This does best-effort work to generate suggestions for associated types.
  * `make_base_error` **(Many-Argument Workhorses)** (Impact: 115.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 771`, `structural_boundaries: 996`, `args: 248`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 87`, `dead_code: 22`, `fragile_debt: 8`
* *Architecture:* `api: 26`, `concurrency: 2`, `import: 61`
* *Defense:* `safety: 136`, `doc: 81`, `test: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, AngleBracketedArg, AssocItemKind, CtorKind, CtorOf, DUMMY_NODE_ID, DefId, DefKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/late.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2239.4 | **LOC:** 5611 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (7.3163%), Tech Debt (20.4152%)
**Top Internal Functions/Classes:**
  * `smart_resolve_path_fragment` **(Many-Argument Workhorses)** (Impact: 133.0)
  * `with_generic_param_rib` **(Many-Argument Workhorses)** (Impact: 94.1)
  * `resolve_anonymous_lifetime` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `resolve_elided_lifetimes_in_path` **(Many-Argument Workhorses)** (Impact: 91.2)
  * `resolve_qpath` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* /// Handles paths that may refer to associated items.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 104 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 913`, `args: 361`, `func_start: 131`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 6`, `state_mutation: 195`, `dead_code: 16`, `fragile_debt: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 44`, `import: 34`
* *Defense:* `safety: 106`, `doc: 274`, `test: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` *, BindingKey, BoundKind, CtorKind, DUMMY_SP, Decl, DefId, DefKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_parse/src/parser/expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2237.44 | **LOC:** 4451 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (10.6155%), Tech Debt (11.9467%)
**Top Internal Functions/Classes:**
  * `parse_expr_bottom` **(Compute Cores)** (Impact: 135.1)
    * *Intent:* /// At the bottom (top?) of the precedence hierarchy, /// Parses things like parenthesized exprs, ma...
  * `parse_expr_assoc_rest_with` **(Many-Argument Workhorses)** (Impact: 108.7)
    * *Intent:* /// Parses the rest of an associative expression (i.e. the part after the lhs) with operators /// of...
  * `parse_struct_fields` **(Many-Argument Workhorses)** (Impact: 91.8)
  * `parse_arm` **(Compute Cores)** (Impact: 72.0)
  * `parse_if_after_cond` **(Many-Argument Workhorses)** (Impact: 63.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 837`, `structural_boundaries: 866`, `args: 314`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 88`, `dead_code: 17`, `fragile_debt: 12`
* *Architecture:* `api: 42`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 76`, `doc: 130`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AnonConst, Arm, AssignOp, AssignOpKind, AttrStyle, AttrVec, BinOp, BinOpKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 2230.24 | **LOC:** 5533 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.7541%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__lasx_xvmadd_b` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_h` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_w` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_d` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmsub_b` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 599`, `args: 555`, `func_start: 555`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 11`, `unreferenced_by_name: 555`
* *Architecture:* `api: 1133`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` lsxintrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512dq.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2216.7 | **LOC:** 11178 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.6467%), Tech Debt (93.1637%)
**Top Internal Functions/Classes:**
  * `_mm512_inserti32x8` **(Annotated Framework Methods)** (Impact: 4.9)
    * *Intent:* /// Copy a to dst, then insert 256 bits (composed of 8 packed 32-bit integers) from b into dst at th...
  * `_mm512_insertf32x8` **(Annotated Framework Methods)** (Impact: 4.8)
    * *Intent:* // Insert /// Copy a to dst, then insert 256 bits (composed of 8 packed single-precision (32-bit) fl...
  * `_mm512_inserti64x2` **(Annotated Framework Methods)** (Impact: 4.4)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed 64-bit integers) from b into dst at th...
  * `_mm512_insertf64x2` **(Annotated Framework Methods)** (Impact: 4.3)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed double-precision (64-bit) floating-poi...
  * `_mm256_inserti64x2` **(Annotated Framework Methods)** (Impact: 4.3)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed 64-bit integers) from b into dst at th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 1660`, `args: 858`, `func_start: 858`
* *Risk/State:* `state_mutation: 4`, `dead_code: 3`, `unreferenced_by_name: 399`
* *Architecture:* `api: 399`, `import: 5`
* *Defense:* `doc: 2515`, `test: 55`, `immutability_locks: 201`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    core_arch::simd::*, crate::core_arch::assert_eq_const, crate::core_arch::x86::*, intrinsics::simd::*, mem::transmute, stdarch_test::simd_test, super::*, x86::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2183.44 | **LOC:** 13199 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.753%), Tech Debt (99.9483%)
**Top Internal Functions/Classes:**
  * `test_mm512_mask_i64gather_epi32` **(Interface Declarations)** (Impact: 2.8)
  * `test_mm512_i32scatter_pd` **(Tests & Verification)** (Impact: 2.8)
  * `test_mm512_mask_i32scatter_pd` **(Tests & Verification)** (Impact: 2.8)
  * `test_mm512_i64scatter_pd` **(Tests & Verification)** (Impact: 2.8)
  * `test_mm512_mask_i64scatter_pd` **(Tests & Verification)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 5294`, `args: 1234`, `func_start: 1228`, `class_start: 4`
* *Risk/State:* `state_mutation: 18`, `unreferenced_by_name: 1186`
* *Architecture:* `api: 30`, `import: 7`
* *Defense:* `doc: 168`, `test: 220`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    core_arch::simd::*, crate::core_arch::assert_eq_const, crate::core_arch::x86::*, crate::core_arch::x86_64::*, crate::hint::black_box, mem::transmute, stdarch_test::assert_instr, stdarch_test::simd_test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_typeck/src/fn_ctxt/suggestions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2145.5 | **LOC:** 3743 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (8.2359%), Tech Debt (11.8372%)
**Top Internal Functions/Classes:**
  * `suggest_deref_or_ref` **(Many-Argument Workhorses)** (Impact: 220.5)
    * *Intent:* /// /// ```compile_fail,E0308 /// fn some_fn(s: &str) {} /// /// let x = "hey!".to_owned(); /// some...
  * `suggest_cast` **(Many-Argument Workhorses)** (Impact: 200.7)
  * `suggest_deref_ref_or_into` **(Many-Argument Workhorses)** (Impact: 152.3)
  * `suggest_compatible_variants` **(Many-Argument Workhorses)** (Impact: 102.9)
    * *Intent:* /// If the expected type is an enum (Issue #55250) with any variants whose /// sole field is of the ...
  * `suggest_missing_break_or_return_expr` **(Many-Argument Workhorses)** (Impact: 94.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 758`, `args: 133`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 39`, `dead_code: 19`, `planned_debt: 4`, `fragile_debt: 9`
* *Architecture:* `api: 39`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 100`, `doc: 114`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Arm, Article, Binder, CoroutineDesugaring, CoroutineKind, CoroutineSource, CtorOf, DefKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_parse/src/parser/item.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2126.14 | **LOC:** 3645 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (9.1487%), Tech Debt (13.9738%)
**Top Internal Functions/Classes:**
  * `parse_item_kind` **(Many-Argument Workhorses)** (Impact: 292.9)
    * *Intent:* /// Parses one of the items allowed by the flags.
  * `parse_fn_front_matter` **(Many-Argument Workhorses)** (Impact: 102.5)
    * *Intent:* /// Parses all the "front matter" (or "qualifiers") for a `fn` declaration, /// up to and including ...
  * `parse_item_impl` **(Many-Argument Workhorses)** (Impact: 85.6)
    * *Intent:* /// Parses an implementation item. /// /// ```ignore (illustrative) /// impl<'a, T> TYPE { /* impl i...
  * `parse_param_general` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* /// Parses a single function parameter. /// /// - `self` is syntactically allowed when `first_param`...
  * `parse_self_param` **(Compute Cores)** (Impact: 56.7)
    * *Intent:* /// Returns the parsed optional self parameter and whether a self shortcut was used.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 795`, `structural_boundaries: 757`, `args: 218`, `func_start: 84`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 4`, `state_mutation: 50`, `dead_code: 24`, `fragile_debt: 13`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 62`, `doc: 230`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, ::*, AttrWrapper, Delimiter, ErrorGuaranteed, ExpKeywordPair, ExpTokenPair, FnPointerCannotBeAsync...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/librustdoc/html/render/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2101.38 | **LOC:** 3062 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.0758%), Tech Debt (9.3787%)
**Top Internal Functions/Classes:**
  * `render_impl` **(Many-Argument Workhorses)** (Impact: 360.3)
  * `doc_impl_item` **(Many-Argument Workhorses)** (Impact: 214.8)
    * *Intent:* // For trait implementations, the `interesting` output contains all methods that have doc // comment...
  * `repr_attribute` **(Many-Argument Workhorses)** (Impact: 58.8)
    * *Intent:* /// Compute the *public* `#[repr]` of the item given by `DefId`. /// /// Read more about it here: //...
  * `render_impl_summary` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `render_call_locations` **(Many-Argument Workhorses)** (Impact: 44.0)
    * *Intent:* /// Generates the HTML for example call locations generated via the --scrape-examples flag.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 118 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 470`, `structural_boundaries: 564`, `args: 182`, `func_start: 74`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 5`, `state_mutation: 165`, `dead_code: 5`, `fragile_debt: 4`
* *Architecture:* `api: 45`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 56`, `doc: 81`, `test: 10`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CallLocation, DefIdSet, Defaultness, DeprecatedSince, Deprecation, Display, FxIndexMap, FxIndexSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_middle/src/ty/print/pretty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2096.58 | **LOC:** 3559 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (25.0222%), Tech Debt (52.8807%)
**Top Internal Functions/Classes:**
  * `pretty_print_type` **(Compute Cores)** (Impact: 327.6)
  * `pretty_print_opaque_impl_type` **(Many-Argument Workhorses)** (Impact: 195.0)
  * `pretty_print_const_valtree` **(Many-Argument Workhorses)** (Impact: 115.0)
  * `pretty_print_const_scalar_int` **(Many-Argument Workhorses)** (Impact: 88.7)
  * `try_print_visible_def_path_recur` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* /// Does the work of `try_print_visible_def_path`, building the /// full definition path recursively...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 894`, `structural_boundaries: 600`, `args: 224`, `func_start: 124`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 68`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 21`, `duplicate_logic: 7`
* *Architecture:* `api: 63`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 65`, `doc: 120`, `test: 2`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CtorKind, DefIdSet, DefKind, DefPathDataName, DerefMut, Expr, ExternCrateSource, GenericArgKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/stdarch-gen-loongarch/lsxintrin.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 2093.84 | **LOC:** 5220 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4739%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__lsx_vmadd_b` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_h` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_w` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_d` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmsub_b` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 563`, `args: 519`, `func_start: 519`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 13`
* *Architecture:* `api: 1061`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.7e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_resolve/src/diagnostics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2066.12 | **LOC:** 3685 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (9.6249%), Tech Debt (9.5342%)
**Top Internal Functions/Classes:**
  * `report_path_resolution_error` **(Many-Argument Workhorses)** (Impact: 212.4)
  * `show_candidates` **(Many-Argument Workhorses)** (Impact: 198.6)
    * *Intent:* /// When an entity with a given name is not available in scope, we search for /// entities with that...
  * `lookup_import_candidates_from_module` **(Many-Argument Workhorses)** (Impact: 160.1)
  * `into_struct_error` **(Many-Argument Workhorses)** (Impact: 121.3)
  * `report_privacy_error` **(Many-Argument Workhorses)** (Impact: 95.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 90 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 573`, `structural_boundaries: 685`, `args: 164`, `func_start: 52`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 118`, `dead_code: 23`, `fragile_debt: 5`
* *Architecture:* `api: 40`, `concurrency: 2`, `import: 48`
* *Defense:* `safety: 89`, `doc: 180`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` *, AMBIGUOUS_GLOB_IMPORTS, AMBIGUOUS_IMPORT_VISIBILITIES, AMBIGUOUS_PANIC_IMPORTS, AddedMacroUse, AmbiguityKind, AmbiguityWarning, BindingError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_codegen_ssa/src/back/link.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2014.76 | **LOC:** 3623 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (8.3184%), Tech Debt (31.6863%)
**Top Internal Functions/Classes:**
  * `link_natively` **(Many-Argument Workhorses)** (Impact: 271.3)
    * *Intent:* /// Create a dynamic library or executable. /// /// This will invoke the system linker/cc to create ...
  * `add_order_independent_options` **(Many-Argument Workhorses)** (Impact: 108.0)
  * `link_binary` **(Many-Argument Workhorses)** (Impact: 107.4)
    * *Intent:* /// Performs the linkage portion of the compilation phase. This will generate all /// of the request...
  * `add_native_libs_from_crate` **(Many-Argument Workhorses)** (Impact: 97.9)
  * `exec_linker` **(Many-Argument Workhorses)** (Impact: 83.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 46 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 520`, `args: 174`, `func_start: 76`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 2`, `state_mutation: 48`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 27`
* *Architecture:* `io: 9`, `api: 11`, `concurrency: 1`, `import: 51`
* *Defense:* `safety: 71`, `doc: 123`, `test: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 2.7e-05
  * `Imports (Out-Degree: 4):` ArchiveBuilderBuilder, BufWriter, CFGuard, Cc, CfgAbi, CompiledModule, CompiledModules, CrateInfo...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/s390x/vector.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1937.74 | **LOC:** 7617 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.2605%), Tech Debt (58.1579%)
**Top Internal Functions/Classes:**
  * `vec_msum_u128` **(Annotated Framework Methods)** (Impact: 5.0)
    * *Intent:* /// Vector Multiply Sum Logical
  * `genmasks` **(Type Conversions)** (Impact: 4.7)
  * `validate_block_boundary` **(State Mutators)** (Impact: 4.7)
  * `genmask` **(Interface Declarations)** (Impact: 3.9)
  * `validate_compare_range_imm` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 797`, `args: 717`, `func_start: 717`, `class_start: 125`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 28`, `dead_code: 14`, `fragile_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 101`
* *Architecture:* `api: 343`, `import: 13`
* *Defense:* `doc: 316`, `test: 184`, `immutability_locks: 133`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::core_arch::simd::*, intrinsics::simd::*, mem::MaybeUninit, mem::transmute, std::mem::transmute, stdarch_test::assert_instr, stdarch_test::simd_test, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/rustc_middle/src/query/plumbing.rs` -> Churn: **100.0%** | Cog Load: 3.5045% | Debt: 96.1079%
- `compiler/rustc_query_impl/src/plumbing.rs` -> Churn: **99.05%** | Cog Load: 7.7486% | Debt: 99.9885%
- `src/tools/rust-analyzer/crates/syntax/src/ast/syntax_factory/constructors.rs` -> Churn: **85.83%** | Cog Load: 7.643% | Debt: 94.9479%
- `compiler/rustc_passes/src/check_attr.rs` -> Churn: **75.95%** | Cog Load: 7.1091% | Debt: 64.593%
- `compiler/rustc_middle/src/ty/context.rs` -> Churn: **75.1%** | Cog Load: 5.4625% | Debt: 62.348%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `library/stdarch/crates/core_arch/src/mips/msa.rs` -> **cyrgani** (100.0% isolated ownership) | Magnitude: 3783.4
- `src/librustdoc/html/static/js/stringdex.js` -> **Michael Howell** (100.0% isolated ownership) | Magnitude: 3760.66
- `src/librustdoc/html/render/mod.rs` -> **Guillaume Gomez** (100.0% isolated ownership) | Magnitude: 2101.38
- `library/stdarch/crates/core_arch/src/s390x/vector.rs` -> **Ralf Jung** (100.0% isolated ownership) | Magnitude: 1937.74
- `src/librustdoc/clean/mod.rs` -> **Guillaume Gomez** (90.0% isolated ownership) | Magnitude: 1312.32

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/ui-fulldeps/internal-lints/find_attr.rs` -> **Severity: 0.196** (Embedded: 0.0025 * Error Risk: 79.7611%)
- `compiler/rustc_borrowck/src/type_check/liveness/trace.rs` -> **Severity: 0.132** (Embedded: 0.0025 * Error Risk: 51.9062%)
- `src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/html.rs` -> **Severity: 0.082** (Embedded: 0.0014 * Error Risk: 60.72%)
- `compiler/rustc_codegen_gcc/build_system/src/info.rs` -> **Severity: 0.038** (Embedded: 0.0008 * Error Risk: 47.8585%)
- `src/tools/rustfmt/src/emitter/diff.rs` -> **Severity: 0.037** (Embedded: 0.0006 * Error Risk: 60.4806%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/ui-fulldeps/internal-lints/find_attr.rs` -> **Severity: 156.6** (Blast Radius: 1.566 * Doc Risk: 100.0%)
- `src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/html.rs` -> **Severity: 98.4** (Blast Radius: 0.984 * Doc Risk: 100.0%)
- `src/tools/miri/tests/pass/both_borrows/smallvec.rs` -> **Severity: 90.0** (Blast Radius: 0.9 * Doc Risk: 100.0%)
- `compiler/rustc_codegen_gcc/build_system/src/info.rs` -> **Severity: 65.5** (Blast Radius: 0.655 * Doc Risk: 100.0%)
- `src/tools/rustfmt/tests/source/configs/short_array_element_width_threshold/10.rs` -> **Severity: 57.7** (Blast Radius: 0.577 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
