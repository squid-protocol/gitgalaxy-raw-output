# ARCHITECTURAL_BRIEF: rust
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/rust` |
| **Timestamp** | `2026-08-07T04:07:03.225572+00:00` |
| **Scan Duration** | `83.7s` |
| **Git Branch** | `main` |
| **Git Commit** | `55e86c996809902e8bbad512cfb4d2c18be446d9` |
| **Git Remote** | `https://github.com/rust-lang/rust.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 32936 malicious artifacts.

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
| Total Artifacts | 58764 |
| Analyzed Artifacts (Scanned) | 34713 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24051 |
| Total LOC | 2085904 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 59.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.225 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 203 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 32413 | 2028534 | 93.4% |
| MARKDOWN | 1339 | 0 | 3.9% |
| PLAINTEXT | 194 | 0 | 0.6% |
| JAVASCRIPT | 156 | 13577 | 0.4% |
| SHELL | 142 | 10523 | 0.4% |
| HTML | 105 | 1924 | 0.3% |
| DOCKERFILE | 69 | 2544 | 0.2% |
| C | 48 | 940 | 0.1% |
| YAML | 44 | 3055 | 0.1% |
| PYTHON | 31 | 6499 | 0.1% |
| JSON | 31 | 1293 | 0.1% |
| TYPESCRIPT | 29 | 5036 | 0.1% |
| ASSEMBLY | 28 | 3151 | 0.1% |
| XML | 26 | 0 | 0.1% |
| CPP | 19 | 2760 | 0.1% |
| CSS | 9 | 3449 | 0.0% |
| BATCH | 8 | 46 | 0.0% |
| POWERSHELL | 4 | 2072 | 0.0% |
| MAKEFILE | 4 | 163 | 0.0% |
| BINARY_THREAT | 4 | 4 | 0.0% |
| M4 | 3 | 30 | 0.0% |
| NIX | 3 | 118 | 0.0% |
| SCHEME | 2 | 180 | 0.0% |
| YACC | 1 | 5 | 0.0% |
| PERL | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.418`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 21625 | 62.3% |
| file_cluster_16 | 5148 | 14.8% |
| file_cluster_13 | 2893 | 8.3% |
| file_cluster_0 | 2444 | 7.0% |
| file_cluster_4 | 493 | 1.4% |
| file_cluster_17 | 252 | 0.7% |
| file_cluster_7 | 99 | 0.3% |
| file_cluster_9 | 71 | 0.2% |
| file_cluster_6 | 66 | 0.2% |
| file_cluster_11 | 59 | 0.2% |
| file_cluster_12 | 17 | 0.0% |
| file_cluster_2 | 5 | 0.0% |
| Unknown | 4 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1533 | 4.4% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24051*

**Composition by Extension & Reason:**
- `.stderr`: 12451x Excluded (Unsupported Extension: '.stderr'), 2003x Unsupported Format (.stderr), 406x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 3697x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 202x Excluded: Neighborhood Micro-Mass Limit Exceeded, 67x Unsupported Format (.undeterminable)
- `.fixed`: 1297x Unsupported Format (.fixed)
- `.diff`: 811x Excluded (Unsupported Extension: '.diff'), 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.diff)
- `.toml`: 556x Unsupported Format (.toml), 15x Excluded (Unsupported Extension: '.toml'), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rast`: 505x Unsupported Format (.rast), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.stdout`: 313x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 44x Unsupported Format (.stdout), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.mir`: 357x Unsupported Format (.mir)
- `no_extension`: 118x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 38x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 3180 LOC)
- `.goml`: 137x Excluded (Unsupported Extension: '.goml'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.coverage`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cov-map`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 15827 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1226 LOC)
- `.c`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 25x Unsupported Format (.lock), 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 18.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.8 | 1.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 72.4 | 86.7 | 100.0 |
| Instability Exposure | 0.0 | 74.6 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/ui/asm/powerpc/bad-reg.rs` (Hits: 221)
- `library/stdarch/crates/core_arch/src/riscv_shared/p.rs` (Hits: 172)
- `src/bootstrap/bootstrap.py` (Hits: 134)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Node.html** (`src/tools/generate-copyright/templates/Node.html`) — 158 inbound connections
2. **trace.rs** (`compiler/rustc_borrowck/src/type_check/liveness/trace.rs`) — 93 inbound connections
3. **str.rs** (`library/alloc/src/str.rs`) — 49 inbound connections
4. **smallvec.rs** (`src/tools/miri/tests/pass/both_borrows/smallvec.rs`) — 41 inbound connections
5. **higher.rs** (`src/tools/clippy/clippy_utils/src/higher.rs`) — 29 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`compiler/rustc_middle/src/ty/mod.rs`) — 238 outbound dependencies
2. **lib.rs** (`src/tools/rust-analyzer/crates/hir/src/lib.rs`) — 197 outbound dependencies
3. **mod.rs** (`library/compiler-builtins/libm/src/math/mod.rs`) — 190 outbound dependencies
4. **lib.rs** (`src/tools/clippy/clippy_utils/src/lib.rs`) — 171 outbound dependencies
5. **interner.rs** (`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/interner.rs`) — 159 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `banana` (@ `tests/ui/expr/if/expr-stack-overflow.rs`) -> Impact: **5223.4** | LOC: 2548
  * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-tidy-filelength #![crate_type = "rlib"]
- `emulate_foreign_item_inner` (@ `src/tools/miri/src/shims/unix/foreign_items.rs`) -> Impact: **969.7** | LOC: 1014
- `unifyGenericTypes` (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **924.0** | LOC: 1140
- `link_natively` (@ `compiler/rustc_codegen_ssa/src/back/link.rs`) -> Impact: **919.3** | LOC: 1563
- `getItemsBefore` (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **880.5** | LOC: 1376
- `initSearch` (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **806.0** | LOC: 1439
  * *Intent:* /**
- `lookup_import_candidates_from_module` (@ `compiler/rustc_resolve/src/diagnostics.rs`) -> Impact: **799.3** | LOC: 1335
- `sysconf` (@ `src/tools/miri/src/shims/unix/foreign_items.rs`) -> Impact: **783.7** | LOC: 1055
  * *Intent:* // Querying system information
- `pretty_print_opaque_impl_type` (@ `compiler/rustc_middle/src/ty/print/pretty.rs`) -> Impact: **781.0** | LOC: 1420
- `emulate_foreign_item_inner` (@ `src/tools/miri/src/shims/windows/foreign_items.rs`) -> Impact: **741.3** | LOC: 1186
  * *Intent:* // There's no more `/`.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `library/alloc/src/collections/btree` | 15 | 25525.01 | 18.71% | 29.12% |
| `library/stdarch/crates/core_arch/src/x86` | 48 | 17138.92 | 3.27% | 79.6% |
| `compiler/rustc_hir_typeck/src` | 27 | 16556.1 | 9.96% | 57.52% |
| `compiler/rustc_parse/src/parser` | 16 | 15342.26 | 15.87% | 32.72% |
| `compiler/rustc_mir_transform/src` | 78 | 14347.48 | 15.97% | 75.14% |
| `compiler/rustc_resolve/src` | 12 | 11276.5 | 11.92% | 49.04% |
| `compiler/rustc_middle/src/ty` | 38 | 9056.74 | 9.97% | 79.35% |
| `src/librustdoc/html/static/js` | 11 | 8984.42 | 17.27% | 59.64% |
| `compiler/rustc_lint/src` | 53 | 7535.48 | 9.92% | 52.06% |
| `compiler/rustc_borrowck/src/diagnostics` | 13 | 7105.98 | 12.65% | 64.51% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/tools/clippy/.github/ISSUE_TEMPLATE/bug_report.yml` -> **100.0%** Exposure
- `src/tools/clippy/.github/ISSUE_TEMPLATE/false_negative.yml` -> **100.0%** Exposure
- `src/tools/clippy/.github/ISSUE_TEMPLATE/false_positive.yml` -> **100.0%** Exposure
- `src/tools/clippy/.github/workflows/clippy_changelog.yml` -> **100.0%** Exposure
- `src/tools/clippy/.github/workflows/remark.yml` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `compiler/rustc_ast/src/mut_visit.rs` -> **100.0%** Exposure
- `compiler/rustc_ast/src/util/comments.rs` -> **100.0%** Exposure
- `compiler/rustc_ast/src/util/unicode.rs` -> **100.0%** Exposure
- `compiler/rustc_ast/src/visit.rs` -> **100.0%** Exposure
- `compiler/rustc_builtin_macros/src/define_opaque.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` -> **1186** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` -> **931** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` -> **827** Orphaned Functions | **2** Duplicates
- `library/stdarch/crates/core_arch/src/mips/msa.rs` -> **527** Orphaned Functions | **0** Duplicates
- `library/stdarch/crates/core_arch/src/hexagon/v128.rs` -> **476** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`compiler/rustc_expand/src/mbe.rs`** -> AI Confidence: **99.48%**
2. **`library/core/src/macros/mod.rs`** -> AI Confidence: **99.48%**
3. **`src/tools/clippy/clippy_utils/src/ast_utils/mod.rs`** -> AI Confidence: **99.48%**
4. **`src/tools/rust-analyzer/crates/rust-analyzer/src/lsp/capabilities.rs`** -> AI Confidence: **99.48%**
5. **`tests/run-make-cargo/compiler-builtins/rmake.rs`** -> AI Confidence: **99.48%**
6. **`tests/run-make/output-type-permutations/rmake.rs`** -> AI Confidence: **99.48%**
7. **`tests/run-make/repr128-dwarf/rmake.rs`** -> AI Confidence: **99.48%**
8. **`tests/ui/structs-enums/tag-variant-disr-val.rs`** -> AI Confidence: **99.48%**
9. **`compiler/rustc_incremental/src/persist/file_format.rs`** -> AI Confidence: **99.39%**
10. **`compiler/rustc_parse/src/parser/nonterminal.rs`** -> AI Confidence: **99.39%**
11. **`compiler/rustc_target/src/asm/x86.rs`** -> AI Confidence: **99.39%**
12. **`library/core/src/intrinsics/mod.rs`** -> AI Confidence: **99.39%**
13. **`src/tools/clippy/clippy_lints/src/operators/bit_mask.rs`** -> AI Confidence: **99.39%**
14. **`src/tools/clippy/tests/ui-internal/repeated_is_diagnostic_item_unfixable.rs`** -> AI Confidence: **99.39%**
15. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/merge_nested_if.rs`** -> AI Confidence: **99.39%**
16. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/move_guard.rs`** -> AI Confidence: **99.39%**
17. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/missing_match_arms.rs`** -> AI Confidence: **99.39%**
18. **`tests/run-make/cross-lang-lto-upstream-rlibs/rmake.rs`** -> AI Confidence: **99.39%**
19. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/add_label_to_loop.rs`** -> AI Confidence: **99.35%**
20. **`src/tools/clippy/clippy_dummy/build.rs`** -> AI Confidence: **99.34%**
21. **`src/tools/tidy/src/rustdoc_templates.rs`** -> AI Confidence: **99.34%**
22. **`tests/run-make/emit-shared-files/rmake.rs`** -> AI Confidence: **99.34%**
23. **`src/ci/docker/run.sh`** -> AI Confidence: **99.34%**
24. **`compiler/rustc_mir_transform/src/remove_storage_markers.rs`** -> AI Confidence: **99.32%**
25. **`library/std/src/sys/io/error/sgx.rs`** -> AI Confidence: **99.32%**
26. **`src/tools/clippy/clippy_dev/src/dogfood.rs`** -> AI Confidence: **99.32%**
27. **`src/tools/clippy/tests/ui/comparison_chain.rs`** -> AI Confidence: **99.32%**
28. **`src/tools/clippy/tests/ui/entry_with_else.rs`** -> AI Confidence: **99.32%**
29. **`src/tools/miri/tests/genmc/pass/litmus/2cowr.rs`** -> AI Confidence: **99.32%**
30. **`src/tools/miri/tests/genmc/pass/litmus/IRIW-acq-sc.rs`** -> AI Confidence: **99.32%**
31. **`src/tools/miri/tests/genmc/pass/litmus/LB.rs`** -> AI Confidence: **99.32%**
32. **`src/tools/miri/tests/genmc/pass/litmus/MP.rs`** -> AI Confidence: **99.32%**
33. **`src/tools/miri/tests/genmc/pass/litmus/SB.rs`** -> AI Confidence: **99.32%**
34. **`src/tools/miri/tests/genmc/pass/litmus/corr.rs`** -> AI Confidence: **99.32%**
35. **`src/tools/miri/tests/genmc/pass/litmus/corr0.rs`** -> AI Confidence: **99.32%**
36. **`src/tools/miri/tests/genmc/pass/litmus/corr1.rs`** -> AI Confidence: **99.32%**
37. **`src/tools/miri/tests/genmc/pass/litmus/corr2.rs`** -> AI Confidence: **99.32%**
38. **`src/tools/miri/tests/genmc/pass/litmus/corw.rs`** -> AI Confidence: **99.32%**
39. **`src/tools/miri/tests/genmc/pass/litmus/cowr.rs`** -> AI Confidence: **99.32%**
40. **`src/tools/miri/tests/genmc/pass/litmus/cumul-release.rs`** -> AI Confidence: **99.32%**
41. **`src/tools/miri/tests/genmc/pass/litmus/default.rs`** -> AI Confidence: **99.32%**
42. **`src/tools/miri/tests/genmc/pass/litmus/fr_w_w_w_reads.rs`** -> AI Confidence: **99.32%**
43. **`src/tools/rust-analyzer/crates/hir-expand/src/inert_attr_macro.rs`** -> AI Confidence: **99.32%**
44. **`tests/run-make/atomic-lock-free/rmake.rs`** -> AI Confidence: **99.32%**
45. **`src/ci/run.sh`** -> AI Confidence: **99.32%**
46. **`compiler/rustc_abi/src/callconv.rs`** -> AI Confidence: **99.31%**
47. **`compiler/rustc_ast_passes/src/ast_validation.rs`** -> AI Confidence: **99.31%**
48. **`compiler/rustc_ast_passes/src/feature_gate.rs`** -> AI Confidence: **99.31%**
49. **`compiler/rustc_ast_pretty/src/pprust/state/expr.rs`** -> AI Confidence: **99.31%**
50. **`compiler/rustc_attr_parsing/src/attributes/deprecation.rs`** -> AI Confidence: **99.31%**
51. **`compiler/rustc_borrowck/src/place_ext.rs`** -> AI Confidence: **99.31%**
52. **`compiler/rustc_borrowck/src/polonius/dump.rs`** -> AI Confidence: **99.31%**
53. **`compiler/rustc_borrowck/src/region_infer/dump_mir.rs`** -> AI Confidence: **99.31%**
54. **`compiler/rustc_codegen_gcc/build_system/src/config.rs`** -> AI Confidence: **99.31%**
55. **`compiler/rustc_codegen_gcc/build_system/src/prepare.rs`** -> AI Confidence: **99.31%**
56. **`compiler/rustc_codegen_gcc/build_system/src/test.rs`** -> AI Confidence: **99.31%**
57. **`compiler/rustc_codegen_gcc/src/asm.rs`** -> AI Confidence: **99.31%**
58. **`compiler/rustc_codegen_gcc/src/attributes.rs`** -> AI Confidence: **99.31%**
59. **`compiler/rustc_codegen_gcc/src/common.rs`** -> AI Confidence: **99.31%**
60. **`compiler/rustc_codegen_gcc/src/type_.rs`** -> AI Confidence: **99.31%**
61. **`compiler/rustc_codegen_llvm/src/asm.rs`** -> AI Confidence: **99.31%**
62. **`compiler/rustc_codegen_llvm/src/attributes.rs`** -> AI Confidence: **99.31%**
63. **`compiler/rustc_codegen_llvm/src/base.rs`** -> AI Confidence: **99.31%**
64. **`compiler/rustc_codegen_llvm/src/callee.rs`** -> AI Confidence: **99.31%**
65. **`compiler/rustc_codegen_llvm/src/llvm/conversions.rs`** -> AI Confidence: **99.31%**
66. **`compiler/rustc_codegen_ssa/src/back/link.rs`** -> AI Confidence: **99.31%**
67. **`compiler/rustc_codegen_ssa/src/codegen_attrs.rs`** -> AI Confidence: **99.31%**
68. **`compiler/rustc_codegen_ssa/src/debuginfo/mod.rs`** -> AI Confidence: **99.31%**
69. **`compiler/rustc_codegen_ssa/src/debuginfo/type_names.rs`** -> AI Confidence: **99.31%**
70. **`compiler/rustc_codegen_ssa/src/target_features.rs`** -> AI Confidence: **99.31%**
71. **`compiler/rustc_const_eval/src/const_eval/fn_queries.rs`** -> AI Confidence: **99.31%**
72. **`compiler/rustc_const_eval/src/const_eval/machine.rs`** -> AI Confidence: **99.31%**
73. **`compiler/rustc_const_eval/src/const_eval/type_info.rs`** -> AI Confidence: **99.31%**
74. **`compiler/rustc_const_eval/src/const_eval/type_info/adt.rs`** -> AI Confidence: **99.31%**
75. **`compiler/rustc_const_eval/src/interpret/call.rs`** -> AI Confidence: **99.31%**
76. **`compiler/rustc_const_eval/src/interpret/cast.rs`** -> AI Confidence: **99.31%**
77. **`compiler/rustc_const_eval/src/interpret/intrinsics.rs`** -> AI Confidence: **99.31%**
78. **`compiler/rustc_const_eval/src/interpret/intrinsics/simd.rs`** -> AI Confidence: **99.31%**
79. **`compiler/rustc_const_eval/src/interpret/operand.rs`** -> AI Confidence: **99.31%**
80. **`compiler/rustc_const_eval/src/interpret/operator.rs`** -> AI Confidence: **99.31%**
81. **`compiler/rustc_const_eval/src/interpret/step.rs`** -> AI Confidence: **99.31%**
82. **`compiler/rustc_const_eval/src/interpret/validity.rs`** -> AI Confidence: **99.31%**
83. **`compiler/rustc_const_eval/src/util/check_validity_requirement.rs`** -> AI Confidence: **99.31%**
84. **`compiler/rustc_expand/src/mbe/diagnostics.rs`** -> AI Confidence: **99.31%**
85. **`compiler/rustc_hir_typeck/src/expr_use_visitor.rs`** -> AI Confidence: **99.31%**
86. **`compiler/rustc_hir_typeck/src/fn_ctxt/suggestions.rs`** -> AI Confidence: **99.31%**
87. **`compiler/rustc_hir_typeck/src/loops.rs`** -> AI Confidence: **99.31%**
88. **`compiler/rustc_hir_typeck/src/op.rs`** -> AI Confidence: **99.31%**
89. **`compiler/rustc_infer/src/infer/outlives/for_liveness.rs`** -> AI Confidence: **99.31%**
90. **`compiler/rustc_lint/src/autorefs.rs`** -> AI Confidence: **99.31%**
91. **`compiler/rustc_lint/src/drop_forget_useless.rs`** -> AI Confidence: **99.31%**
92. **`compiler/rustc_lint/src/early/diagnostics/check_cfg.rs`** -> AI Confidence: **99.31%**
93. **`compiler/rustc_lint/src/interior_mutable_consts.rs`** -> AI Confidence: **99.31%**
94. **`compiler/rustc_lint/src/internal.rs`** -> AI Confidence: **99.31%**
95. **`compiler/rustc_lint/src/non_ascii_idents.rs`** -> AI Confidence: **99.31%**
96. **`compiler/rustc_lint/src/ptr_nulls.rs`** -> AI Confidence: **99.31%**
97. **`compiler/rustc_lint/src/types.rs`** -> AI Confidence: **99.31%**
98. **`compiler/rustc_lint/src/types/literal.rs`** -> AI Confidence: **99.31%**
99. **`compiler/rustc_metadata/src/dependency_format.rs`** -> AI Confidence: **99.31%**
100. **`compiler/rustc_metadata/src/native_libs.rs`** -> AI Confidence: **99.31%**
101. **`compiler/rustc_middle/src/mir/pretty.rs`** -> AI Confidence: **99.31%**
102. **`compiler/rustc_middle/src/ty/consts/int.rs`** -> AI Confidence: **99.31%**
103. **`compiler/rustc_middle/src/ty/consts/lit.rs`** -> AI Confidence: **99.31%**
104. **`compiler/rustc_middle/src/ty/inhabitedness/inhabited_predicate.rs`** -> AI Confidence: **99.31%**
105. **`compiler/rustc_middle/src/ty/print/pretty.rs`** -> AI Confidence: **99.31%**
106. **`compiler/rustc_middle/src/ty/region.rs`** -> AI Confidence: **99.31%**
107. **`compiler/rustc_middle/src/ty/relate.rs`** -> AI Confidence: **99.31%**
108. **`compiler/rustc_middle/src/ty/util.rs`** -> AI Confidence: **99.31%**
109. **`compiler/rustc_mir_build/src/builder/custom/parse/instruction.rs`** -> AI Confidence: **99.31%**
110. **`compiler/rustc_mir_build/src/thir/print.rs`** -> AI Confidence: **99.31%**
111. **`compiler/rustc_mir_transform/src/liveness.rs`** -> AI Confidence: **99.31%**
112. **`compiler/rustc_mir_transform/src/validate.rs`** -> AI Confidence: **99.31%**
113. **`compiler/rustc_next_trait_solver/src/resolve.rs`** -> AI Confidence: **99.31%**
114. **`compiler/rustc_parse/src/parser/asm.rs`** -> AI Confidence: **99.31%**
115. **`compiler/rustc_parse/src/parser/expr.rs`** -> AI Confidence: **99.31%**
116. **`compiler/rustc_parse/src/parser/generics.rs`** -> AI Confidence: **99.31%**
117. **`compiler/rustc_parse/src/parser/item.rs`** -> AI Confidence: **99.31%**
118. **`compiler/rustc_parse/src/parser/pat.rs`** -> AI Confidence: **99.31%**
119. **`compiler/rustc_parse/src/parser/path.rs`** -> AI Confidence: **99.31%**
120. **`compiler/rustc_parse/src/parser/stmt.rs`** -> AI Confidence: **99.31%**
121. **`compiler/rustc_parse/src/parser/ty.rs`** -> AI Confidence: **99.31%**
122. **`compiler/rustc_passes/src/reachable.rs`** -> AI Confidence: **99.31%**
123. **`compiler/rustc_passes/src/stability.rs`** -> AI Confidence: **99.31%**
124. **`compiler/rustc_passes/src/weak_lang_items.rs`** -> AI Confidence: **99.31%**
125. **`compiler/rustc_pattern_analysis/src/constructor.rs`** -> AI Confidence: **99.31%**
126. **`compiler/rustc_pattern_analysis/src/rustc/print.rs`** -> AI Confidence: **99.31%**
127. **`compiler/rustc_public/src/mir/pretty.rs`** -> AI Confidence: **99.31%**
128. **`compiler/rustc_resolve/src/check_unused.rs`** -> AI Confidence: **99.31%**
129. **`compiler/rustc_resolve/src/ident.rs`** -> AI Confidence: **99.31%**
130. **`compiler/rustc_resolve/src/imports.rs`** -> AI Confidence: **99.31%**
131. **`compiler/rustc_session/src/session.rs`** -> AI Confidence: **99.31%**
132. **`compiler/rustc_target/src/asm/aarch64.rs`** -> AI Confidence: **99.31%**
133. **`compiler/rustc_target/src/asm/arm.rs`** -> AI Confidence: **99.31%**
134. **`compiler/rustc_target/src/asm/mod.rs`** -> AI Confidence: **99.31%**
135. **`compiler/rustc_target/src/asm/powerpc.rs`** -> AI Confidence: **99.31%**
136. **`compiler/rustc_target/src/asm/riscv.rs`** -> AI Confidence: **99.31%**
137. **`compiler/rustc_target/src/asm/sparc.rs`** -> AI Confidence: **99.31%**
138. **`compiler/rustc_target/src/callconv/nvptx64.rs`** -> AI Confidence: **99.31%**
139. **`compiler/rustc_target/src/callconv/powerpc64.rs`** -> AI Confidence: **99.31%**
140. **`compiler/rustc_target/src/callconv/s390x.rs`** -> AI Confidence: **99.31%**
141. **`compiler/rustc_target/src/callconv/wasm.rs`** -> AI Confidence: **99.31%**
142. **`compiler/rustc_target/src/callconv/x86.rs`** -> AI Confidence: **99.31%**
143. **`compiler/rustc_target/src/callconv/x86_64.rs`** -> AI Confidence: **99.31%**
144. **`compiler/rustc_target/src/callconv/x86_win64.rs`** -> AI Confidence: **99.31%**
145. **`compiler/rustc_target/src/spec/base/apple/mod.rs`** -> AI Confidence: **99.31%**
146. **`compiler/rustc_target/src/spec/targets/armv7_wrs_vxworks_eabihf.rs`** -> AI Confidence: **99.31%**
147. **`compiler/rustc_ty_utils/src/consts.rs`** -> AI Confidence: **99.31%**
148. **`compiler/rustc_ty_utils/src/instance.rs`** -> AI Confidence: **99.31%**
149. **`library/compiler-builtins/libm-test/src/precision.rs`** -> AI Confidence: **99.31%**
150. **`library/compiler-builtins/libm-test/src/run_cfg.rs`** -> AI Confidence: **99.31%**
151. **`library/compiler-builtins/libm/src/math/support/float_traits.rs`** -> AI Confidence: **99.31%**
152. **`library/core/src/char/methods.rs`** -> AI Confidence: **99.31%**
153. **`library/core/src/cmp.rs`** -> AI Confidence: **99.31%**
154. **`library/core/src/num/imp/flt2dec/mod.rs`** -> AI Confidence: **99.31%**
155. **`library/core/src/str/lossy.rs`** -> AI Confidence: **99.31%**
156. **`library/core/src/str/pattern.rs`** -> AI Confidence: **99.31%**
157. **`library/core/src/wtf8.rs`** -> AI Confidence: **99.31%**
158. **`library/std/src/sync/mpmc/array.rs`** -> AI Confidence: **99.31%**
159. **`library/std/src/sys/fs/common.rs`** -> AI Confidence: **99.31%**
160. **`library/std/src/sys/net/connection/uefi/tcp.rs`** -> AI Confidence: **99.31%**
161. **`library/std/src/sys/path/windows.rs`** -> AI Confidence: **99.31%**
162. **`library/std/src/sys/sync/mutex/fuchsia.rs`** -> AI Confidence: **99.31%**
163. **`library/std/src/sys/sync/rwlock/futex.rs`** -> AI Confidence: **99.31%**
164. **`library/std/src/sys/sync/rwlock/queue.rs`** -> AI Confidence: **99.31%**
165. **`library/stdarch/crates/intrinsic-test/src/arm/types.rs`** -> AI Confidence: **99.31%**
166. **`library/stdarch/crates/intrinsic-test/src/common/gen_rust.rs`** -> AI Confidence: **99.31%**
167. **`library/stdarch/crates/intrinsic-test/src/common/intrinsic_helpers.rs`** -> AI Confidence: **99.31%**
168. **`library/stdarch/crates/intrinsic-test/src/x86/types.rs`** -> AI Confidence: **99.31%**
169. **`library/stdarch/crates/stdarch-gen-arm/src/context.rs`** -> AI Confidence: **99.31%**
170. **`library/stdarch/crates/stdarch-gen-arm/src/matching.rs`** -> AI Confidence: **99.31%**
171. **`library/stdarch/crates/stdarch-gen-arm/src/predicate_forms.rs`** -> AI Confidence: **99.31%**
172. **`library/stdarch/crates/stdarch-gen-arm/src/typekinds.rs`** -> AI Confidence: **99.31%**
173. **`library/stdarch/crates/stdarch-gen-arm/src/wildcards.rs`** -> AI Confidence: **99.31%**
174. **`library/stdarch/crates/stdarch-test/src/lib.rs`** -> AI Confidence: **99.31%**
175. **`library/test/src/formatters/junit.rs`** -> AI Confidence: **99.31%**
176. **`library/test/src/formatters/pretty.rs`** -> AI Confidence: **99.31%**
177. **`library/test/src/formatters/terse.rs`** -> AI Confidence: **99.31%**
178. **`src/bootstrap/src/core/build_steps/clean.rs`** -> AI Confidence: **99.31%**
179. **`src/bootstrap/src/core/build_steps/llvm.rs`** -> AI Confidence: **99.31%**
180. **`src/bootstrap/src/core/build_steps/toolstate.rs`** -> AI Confidence: **99.31%**
181. **`src/bootstrap/src/core/sanity.rs`** -> AI Confidence: **99.31%**
182. **`src/bootstrap/src/utils/helpers.rs`** -> AI Confidence: **99.31%**
183. **`src/bootstrap/src/utils/render_tests.rs`** -> AI Confidence: **99.31%**
184. **`src/doc/rustc-dev-guide/ci/sembr/src/main.rs`** -> AI Confidence: **99.31%**
185. **`src/librustdoc/clean/cfg.rs`** -> AI Confidence: **99.31%**
186. **`src/librustdoc/html/format.rs`** -> AI Confidence: **99.31%**
187. **`src/librustdoc/html/render/print_item.rs`** -> AI Confidence: **99.31%**
188. **`src/librustdoc/passes/lint/html_tags.rs`** -> AI Confidence: **99.31%**
189. **`src/tools/build-manifest/src/versions.rs`** -> AI Confidence: **99.31%**
190. **`src/tools/clippy/clippy_dev/src/main.rs`** -> AI Confidence: **99.31%**
191. **`src/tools/clippy/clippy_lints/src/absolute_paths.rs`** -> AI Confidence: **99.31%**
192. **`src/tools/clippy/clippy_lints/src/arbitrary_source_item_ordering.rs`** -> AI Confidence: **99.31%**
193. **`src/tools/clippy/clippy_lints/src/attrs/deprecated_cfg_attr.rs`** -> AI Confidence: **99.31%**
194. **`src/tools/clippy/clippy_lints/src/attrs/non_minimal_cfg.rs`** -> AI Confidence: **99.31%**
195. **`src/tools/clippy/clippy_lints/src/attrs/unnecessary_clippy_cfg.rs`** -> AI Confidence: **99.31%**
196. **`src/tools/clippy/clippy_lints/src/attrs/utils.rs`** -> AI Confidence: **99.31%**
197. **`src/tools/clippy/clippy_lints/src/borrow_deref_ref.rs`** -> AI Confidence: **99.31%**
198. **`src/tools/clippy/clippy_lints/src/byte_char_slices.rs`** -> AI Confidence: **99.31%**
199. **`src/tools/clippy/clippy_lints/src/casts/cast_ptr_alignment.rs`** -> AI Confidence: **99.31%**
200. **`src/tools/clippy/clippy_lints/src/casts/unnecessary_cast.rs`** -> AI Confidence: **99.31%**
201. **`src/tools/clippy/clippy_lints/src/casts/utils.rs`** -> AI Confidence: **99.31%**
202. **`src/tools/clippy/clippy_lints/src/checked_conversions.rs`** -> AI Confidence: **99.31%**
203. **`src/tools/clippy/clippy_lints/src/collapsible_if.rs`** -> AI Confidence: **99.31%**
204. **`src/tools/clippy/clippy_lints/src/default.rs`** -> AI Confidence: **99.31%**
205. **`src/tools/clippy/clippy_lints/src/dereference.rs`** -> AI Confidence: **99.31%**
206. **`src/tools/clippy/clippy_lints/src/doc/doc_paragraphs_missing_punctuation.rs`** -> AI Confidence: **99.31%**
207. **`src/tools/clippy/clippy_lints/src/doc/doc_suspicious_footnotes.rs`** -> AI Confidence: **99.31%**
208. **`src/tools/clippy/clippy_lints/src/doc/include_in_doc_without_cfg.rs`** -> AI Confidence: **99.31%**
209. **`src/tools/clippy/clippy_lints/src/doc/markdown.rs`** -> AI Confidence: **99.31%**
210. **`src/tools/clippy/clippy_lints/src/doc/missing_headers.rs`** -> AI Confidence: **99.31%**
211. **`src/tools/clippy/clippy_lints/src/else_if_without_else.rs`** -> AI Confidence: **99.31%**
212. **`src/tools/clippy/clippy_lints/src/field_scoped_visibility_modifiers.rs`** -> AI Confidence: **99.31%**
213. **`src/tools/clippy/clippy_lints/src/floating_point_arithmetic/custom_abs.rs`** -> AI Confidence: **99.31%**
214. **`src/tools/clippy/clippy_lints/src/floating_point_arithmetic/powf.rs`** -> AI Confidence: **99.31%**
215. **`src/tools/clippy/clippy_lints/src/formatting.rs`** -> AI Confidence: **99.31%**
216. **`src/tools/clippy/clippy_lints/src/functions/impl_trait_in_params.rs`** -> AI Confidence: **99.31%**
217. **`src/tools/clippy/clippy_lints/src/functions/too_many_lines.rs`** -> AI Confidence: **99.31%**
218. **`src/tools/clippy/clippy_lints/src/implicit_saturating_sub.rs`** -> AI Confidence: **99.31%**
219. **`src/tools/clippy/clippy_lints/src/ineffective_open_options.rs`** -> AI Confidence: **99.31%**
220. **`src/tools/clippy/clippy_lints/src/infinite_iter.rs`** -> AI Confidence: **99.31%**
221. **`src/tools/clippy/clippy_lints/src/item_name_repetitions.rs`** -> AI Confidence: **99.31%**
222. **`src/tools/clippy/clippy_lints/src/legacy_numeric_constants.rs`** -> AI Confidence: **99.31%**
223. **`src/tools/clippy/clippy_lints/src/len_without_is_empty.rs`** -> AI Confidence: **99.31%**
224. **`src/tools/clippy/clippy_lints/src/let_if_seq.rs`** -> AI Confidence: **99.31%**
225. **`src/tools/clippy/clippy_lints/src/literal_representation.rs`** -> AI Confidence: **99.31%**
226. **`src/tools/clippy/clippy_lints/src/loops/char_indices_as_byte_indices.rs`** -> AI Confidence: **99.31%**
227. **`src/tools/clippy/clippy_lints/src/loops/empty_loop.rs`** -> AI Confidence: **99.31%**
228. **`src/tools/clippy/clippy_lints/src/loops/explicit_iter_loop.rs`** -> AI Confidence: **99.31%**
229. **`src/tools/clippy/clippy_lints/src/loops/infinite_loop.rs`** -> AI Confidence: **99.31%**
230. **`src/tools/clippy/clippy_lints/src/loops/needless_range_loop.rs`** -> AI Confidence: **99.31%**
231. **`src/tools/clippy/clippy_lints/src/loops/unused_enumerate_index.rs`** -> AI Confidence: **99.31%**
232. **`src/tools/clippy/clippy_lints/src/loops/utils.rs`** -> AI Confidence: **99.31%**
233. **`src/tools/clippy/clippy_lints/src/loops/while_let_loop.rs`** -> AI Confidence: **99.31%**
234. **`src/tools/clippy/clippy_lints/src/loops/while_let_on_iterator.rs`** -> AI Confidence: **99.31%**
235. **`src/tools/clippy/clippy_lints/src/manual_checked_ops.rs`** -> AI Confidence: **99.31%**
236. **`src/tools/clippy/clippy_lints/src/manual_clamp.rs`** -> AI Confidence: **99.31%**
237. **`src/tools/clippy/clippy_lints/src/manual_is_power_of_two.rs`** -> AI Confidence: **99.31%**
238. **`src/tools/clippy/clippy_lints/src/manual_option_as_slice.rs`** -> AI Confidence: **99.31%**
239. **`src/tools/clippy/clippy_lints/src/manual_pop_if.rs`** -> AI Confidence: **99.31%**
240. **`src/tools/clippy/clippy_lints/src/manual_rem_euclid.rs`** -> AI Confidence: **99.31%**
241. **`src/tools/clippy/clippy_lints/src/manual_retain.rs`** -> AI Confidence: **99.31%**
242. **`src/tools/clippy/clippy_lints/src/manual_string_new.rs`** -> AI Confidence: **99.31%**
243. **`src/tools/clippy/clippy_lints/src/matches/collapsible_match.rs`** -> AI Confidence: **99.31%**
244. **`src/tools/clippy/clippy_lints/src/matches/manual_map.rs`** -> AI Confidence: **99.31%**
245. **`src/tools/clippy/clippy_lints/src/matches/manual_unwrap_or.rs`** -> AI Confidence: **99.31%**
246. **`src/tools/clippy/clippy_lints/src/matches/manual_utils.rs`** -> AI Confidence: **99.31%**
247. **`src/tools/clippy/clippy_lints/src/matches/match_as_ref.rs`** -> AI Confidence: **99.31%**
248. **`src/tools/clippy/clippy_lints/src/matches/match_wild_enum.rs`** -> AI Confidence: **99.31%**
249. **`src/tools/clippy/clippy_lints/src/matches/redundant_guards.rs`** -> AI Confidence: **99.31%**
250. **`src/tools/clippy/clippy_lints/src/matches/redundant_pattern_match.rs`** -> AI Confidence: **99.31%**
251. **`src/tools/clippy/clippy_lints/src/matches/single_match.rs`** -> AI Confidence: **99.31%**
252. **`src/tools/clippy/clippy_lints/src/methods/case_sensitive_file_extension_comparisons.rs`** -> AI Confidence: **99.31%**
253. **`src/tools/clippy/clippy_lints/src/methods/double_ended_iterator_last.rs`** -> AI Confidence: **99.31%**
254. **`src/tools/clippy/clippy_lints/src/methods/filter_map.rs`** -> AI Confidence: **99.31%**
255. **`src/tools/clippy/clippy_lints/src/methods/iter_filter.rs`** -> AI Confidence: **99.31%**
256. **`src/tools/clippy/clippy_lints/src/methods/lib.rs`** -> AI Confidence: **99.31%**
257. **`src/tools/clippy/clippy_lints/src/methods/lines_filter_map_ok.rs`** -> AI Confidence: **99.31%**
258. **`src/tools/clippy/clippy_lints/src/methods/manual_c_str_literals.rs`** -> AI Confidence: **99.31%**
259. **`src/tools/clippy/clippy_lints/src/methods/map_clone.rs`** -> AI Confidence: **99.31%**
260. **`src/tools/clippy/clippy_lints/src/methods/needless_character_iteration.rs`** -> AI Confidence: **99.31%**
261. **`src/tools/clippy/clippy_lints/src/methods/needless_collect.rs`** -> AI Confidence: **99.31%**
262. **`src/tools/clippy/clippy_lints/src/methods/open_options.rs`** -> AI Confidence: **99.31%**
263. **`src/tools/clippy/clippy_lints/src/methods/or_fun_call.rs`** -> AI Confidence: **99.31%**
264. **`src/tools/clippy/clippy_lints/src/methods/range_zip_with_len.rs`** -> AI Confidence: **99.31%**
265. **`src/tools/clippy/clippy_lints/src/methods/read_line_without_trim.rs`** -> AI Confidence: **99.31%**
266. **`src/tools/clippy/clippy_lints/src/methods/suspicious_splitn.rs`** -> AI Confidence: **99.31%**
267. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_map_or.rs`** -> AI Confidence: **99.31%**
268. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_min_or_max.rs`** -> AI Confidence: **99.31%**
269. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_sort_by.rs`** -> AI Confidence: **99.31%**
270. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_to_owned.rs`** -> AI Confidence: **99.31%**
271. **`src/tools/clippy/clippy_lints/src/methods/unwrap_expect_used.rs`** -> AI Confidence: **99.31%**
272. **`src/tools/clippy/clippy_lints/src/misc.rs`** -> AI Confidence: **99.31%**
273. **`src/tools/clippy/clippy_lints/src/missing_asserts_for_indexing.rs`** -> AI Confidence: **99.31%**
274. **`src/tools/clippy/clippy_lints/src/missing_doc.rs`** -> AI Confidence: **99.31%**
275. **`src/tools/clippy/clippy_lints/src/needless_bool.rs`** -> AI Confidence: **99.31%**
276. **`src/tools/clippy/clippy_lints/src/needless_continue.rs`** -> AI Confidence: **99.31%**
277. **`src/tools/clippy/clippy_lints/src/needless_else.rs`** -> AI Confidence: **99.31%**
278. **`src/tools/clippy/clippy_lints/src/needless_ifs.rs`** -> AI Confidence: **99.31%**
279. **`src/tools/clippy/clippy_lints/src/needless_question_mark.rs`** -> AI Confidence: **99.31%**
280. **`src/tools/clippy/clippy_lints/src/no_effect.rs`** -> AI Confidence: **99.31%**
281. **`src/tools/clippy/clippy_lints/src/non_canonical_impls.rs`** -> AI Confidence: **99.31%**
282. **`src/tools/clippy/clippy_lints/src/non_copy_const.rs`** -> AI Confidence: **99.31%**
283. **`src/tools/clippy/clippy_lints/src/non_send_fields_in_send_ty.rs`** -> AI Confidence: **99.31%**
284. **`src/tools/clippy/clippy_lints/src/operators/const_comparisons.rs`** -> AI Confidence: **99.31%**
285. **`src/tools/clippy/clippy_lints/src/operators/eq_op.rs`** -> AI Confidence: **99.31%**
286. **`src/tools/clippy/clippy_lints/src/operators/float_cmp.rs`** -> AI Confidence: **99.31%**
287. **`src/tools/clippy/clippy_lints/src/operators/invalid_upcast_comparisons.rs`** -> AI Confidence: **99.31%**
288. **`src/tools/clippy/clippy_lints/src/operators/manual_div_ceil.rs`** -> AI Confidence: **99.31%**
289. **`src/tools/clippy/clippy_lints/src/operators/manual_is_multiple_of.rs`** -> AI Confidence: **99.31%**
290. **`src/tools/clippy/clippy_lints/src/operators/modulo_arithmetic.rs`** -> AI Confidence: **99.31%**
291. **`src/tools/clippy/clippy_lints/src/option_if_let_else.rs`** -> AI Confidence: **99.31%**
292. **`src/tools/clippy/clippy_lints/src/panic_unimplemented.rs`** -> AI Confidence: **99.31%**
293. **`src/tools/clippy/clippy_lints/src/panicking_overflow_checks.rs`** -> AI Confidence: **99.31%**
294. **`src/tools/clippy/clippy_lints/src/question_mark.rs`** -> AI Confidence: **99.31%**
295. **`src/tools/clippy/clippy_lints/src/ranges.rs`** -> AI Confidence: **99.31%**
296. **`src/tools/clippy/clippy_lints/src/redundant_clone.rs`** -> AI Confidence: **99.31%**
297. **`src/tools/clippy/clippy_lints/src/redundant_type_annotations.rs`** -> AI Confidence: **99.31%**
298. **`src/tools/clippy/clippy_lints/src/returns/let_and_return.rs`** -> AI Confidence: **99.31%**
299. **`src/tools/clippy/clippy_lints/src/returns/needless_return_with_question_mark.rs`** -> AI Confidence: **99.31%**
300. **`src/tools/clippy/clippy_lints/src/same_length_and_capacity.rs`** -> AI Confidence: **99.31%**
301. **`src/tools/clippy/clippy_lints/src/semicolon_block.rs`** -> AI Confidence: **99.31%**
302. **`src/tools/clippy/clippy_lints/src/single_range_in_vec_init.rs`** -> AI Confidence: **99.31%**
303. **`src/tools/clippy/clippy_lints/src/size_of_in_element_count.rs`** -> AI Confidence: **99.31%**
304. **`src/tools/clippy/clippy_lints/src/slow_vector_initialization.rs`** -> AI Confidence: **99.31%**
305. **`src/tools/clippy/clippy_lints/src/strings.rs`** -> AI Confidence: **99.31%**
306. **`src/tools/clippy/clippy_lints/src/swap.rs`** -> AI Confidence: **99.31%**
307. **`src/tools/clippy/clippy_lints/src/swap_ptr_to_ref.rs`** -> AI Confidence: **99.31%**
308. **`src/tools/clippy/clippy_lints/src/transmute/eager_transmute.rs`** -> AI Confidence: **99.31%**
309. **`src/tools/clippy/clippy_lints/src/transmute/transmute_ptr_to_ptr.rs`** -> AI Confidence: **99.31%**
310. **`src/tools/clippy/clippy_lints/src/transmute/transmute_ptr_to_ref.rs`** -> AI Confidence: **99.31%**
311. **`src/tools/clippy/clippy_lints/src/transmute/transmute_undefined_repr.rs`** -> AI Confidence: **99.31%**
312. **`src/tools/clippy/clippy_lints/src/types/borrowed_box.rs`** -> AI Confidence: **99.31%**
313. **`src/tools/clippy/clippy_lints/src/undocumented_unsafe_blocks.rs`** -> AI Confidence: **99.31%**
314. **`src/tools/clippy/clippy_lints/src/uninit_vec.rs`** -> AI Confidence: **99.31%**
315. **`src/tools/clippy/clippy_lints/src/unnecessary_struct_initialization.rs`** -> AI Confidence: **99.31%**
316. **`src/tools/clippy/clippy_lints/src/unused_unit.rs`** -> AI Confidence: **99.31%**
317. **`src/tools/clippy/clippy_lints/src/visibility.rs`** -> AI Confidence: **99.31%**
318. **`src/tools/clippy/clippy_lints/src/volatile_composites.rs`** -> AI Confidence: **99.31%**
319. **`src/tools/clippy/clippy_lints/src/zero_div_zero.rs`** -> AI Confidence: **99.31%**
320. **`src/tools/clippy/clippy_utils/src/check_proc_macro.rs`** -> AI Confidence: **99.31%**
321. **`src/tools/clippy/clippy_utils/src/consts.rs`** -> AI Confidence: **99.31%**
322. **`src/tools/clippy/clippy_utils/src/eager_or_lazy.rs`** -> AI Confidence: **99.31%**
323. **`src/tools/clippy/clippy_utils/src/hir_utils.rs`** -> AI Confidence: **99.31%**
324. **`src/tools/clippy/clippy_utils/src/lib.rs`** -> AI Confidence: **99.31%**
325. **`src/tools/clippy/clippy_utils/src/qualify_min_const_fn.rs`** -> AI Confidence: **99.31%**
326. **`src/tools/clippy/clippy_utils/src/ty/mod.rs`** -> AI Confidence: **99.31%**
327. **`src/tools/clippy/tests/ui/single_match.rs`** -> AI Confidence: **99.31%**
328. **`src/tools/compiletest/src/directives.rs`** -> AI Confidence: **99.31%**
329. **`src/tools/compiletest/src/directives/cfg.rs`** -> AI Confidence: **99.31%**
330. **`src/tools/compiletest/src/directives/needs.rs`** -> AI Confidence: **99.31%**
331. **`src/tools/compiletest/src/errors.rs`** -> AI Confidence: **99.31%**
332. **`src/tools/compiletest/src/json.rs`** -> AI Confidence: **99.31%**
333. **`src/tools/compiletest/src/runtest.rs`** -> AI Confidence: **99.31%**
334. **`src/tools/compiletest/src/runtest/ui.rs`** -> AI Confidence: **99.31%**
335. **`src/tools/lint-docs/src/lib.rs`** -> AI Confidence: **99.31%**
336. **`src/tools/miri/miri-script/src/commands.rs`** -> AI Confidence: **99.31%**
337. **`src/tools/miri/src/bin/miri.rs`** -> AI Confidence: **99.31%**
338. **`src/tools/miri/src/borrow_tracker/stacked_borrows/stack.rs`** -> AI Confidence: **99.31%**
339. **`src/tools/miri/src/borrow_tracker/tree_borrows/perms.rs`** -> AI Confidence: **99.31%**
340. **`src/tools/miri/src/borrow_tracker/tree_borrows/tree/tests.rs`** -> AI Confidence: **99.31%**
341. **`src/tools/miri/src/intrinsics/math.rs`** -> AI Confidence: **99.31%**
342. **`src/tools/miri/src/intrinsics/simd.rs`** -> AI Confidence: **99.31%**
343. **`src/tools/miri/src/math.rs`** -> AI Confidence: **99.31%**
344. **`src/tools/miri/src/shims/aarch64.rs`** -> AI Confidence: **99.31%**
345. **`src/tools/miri/src/shims/backtrace.rs`** -> AI Confidence: **99.31%**
346. **`src/tools/miri/src/shims/env.rs`** -> AI Confidence: **99.31%**
347. **`src/tools/miri/src/shims/foreign_items.rs`** -> AI Confidence: **99.31%**
348. **`src/tools/miri/src/shims/sig.rs`** -> AI Confidence: **99.31%**
349. **`src/tools/miri/src/shims/unix/android/foreign_items.rs`** -> AI Confidence: **99.31%**
350. **`src/tools/miri/src/shims/unix/foreign_items.rs`** -> AI Confidence: **99.31%**
351. **`src/tools/miri/src/shims/unix/freebsd/foreign_items.rs`** -> AI Confidence: **99.31%**
352. **`src/tools/miri/src/shims/unix/fs.rs`** -> AI Confidence: **99.31%**
353. **`src/tools/miri/src/shims/unix/linux/foreign_items.rs`** -> AI Confidence: **99.31%**
354. **`src/tools/miri/src/shims/unix/linux_like/syscall.rs`** -> AI Confidence: **99.31%**
355. **`src/tools/miri/src/shims/unix/macos/foreign_items.rs`** -> AI Confidence: **99.31%**
356. **`src/tools/miri/src/shims/unix/macos/sync.rs`** -> AI Confidence: **99.31%**
357. **`src/tools/miri/src/shims/unix/solarish/foreign_items.rs`** -> AI Confidence: **99.31%**
358. **`src/tools/miri/src/shims/windows/env.rs`** -> AI Confidence: **99.31%**
359. **`src/tools/miri/src/shims/windows/foreign_items.rs`** -> AI Confidence: **99.31%**
360. **`src/tools/miri/src/shims/windows/fs.rs`** -> AI Confidence: **99.31%**
361. **`src/tools/miri/src/shims/windows/sync.rs`** -> AI Confidence: **99.31%**
362. **`src/tools/miri/src/shims/x86/avx.rs`** -> AI Confidence: **99.31%**
363. **`src/tools/miri/src/shims/x86/avx2.rs`** -> AI Confidence: **99.31%**
364. **`src/tools/miri/src/shims/x86/avx512.rs`** -> AI Confidence: **99.31%**
365. **`src/tools/miri/src/shims/x86/mod.rs`** -> AI Confidence: **99.31%**
366. **`src/tools/miri/src/shims/x86/sse.rs`** -> AI Confidence: **99.31%**
367. **`src/tools/miri/src/shims/x86/sse2.rs`** -> AI Confidence: **99.31%**
368. **`src/tools/miri/src/shims/x86/sse41.rs`** -> AI Confidence: **99.31%**
369. **`src/tools/miri/src/shims/x86/sse42.rs`** -> AI Confidence: **99.31%**
370. **`src/tools/miri/tests/pass/float.rs`** -> AI Confidence: **99.31%**
371. **`src/tools/miri/tests/pass/float_nan.rs`** -> AI Confidence: **99.31%**
372. **`src/tools/opt-dist/src/main.rs`** -> AI Confidence: **99.31%**
373. **`src/tools/opt-dist/src/training.rs`** -> AI Confidence: **99.31%**
374. **`src/tools/run-make-support/src/external_deps/c_build.rs`** -> AI Confidence: **99.31%**
375. **`src/tools/rust-analyzer/crates/cfg/src/cfg_expr.rs`** -> AI Confidence: **99.31%**
376. **`src/tools/rust-analyzer/crates/cfg/src/dnf.rs`** -> AI Confidence: **99.31%**
377. **`src/tools/rust-analyzer/crates/cfg/src/lib.rs`** -> AI Confidence: **99.31%**
378. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/lower/asm.rs`** -> AI Confidence: **99.31%**
379. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/lower/path.rs`** -> AI Confidence: **99.31%**
380. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/path.rs`** -> AI Confidence: **99.31%**
381. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/pretty.rs`** -> AI Confidence: **99.31%**
382. **`src/tools/rust-analyzer/crates/hir-def/src/nameres/proc_macro.rs`** -> AI Confidence: **99.31%**
383. **`src/tools/rust-analyzer/crates/hir-expand/src/fixup.rs`** -> AI Confidence: **99.31%**
384. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/eval.rs`** -> AI Confidence: **99.31%**
385. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/eval/shim.rs`** -> AI Confidence: **99.31%**
386. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/lower/pattern_matching.rs`** -> AI Confidence: **99.31%**
387. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/monomorphization.rs`** -> AI Confidence: **99.31%**
388. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/resolve.rs`** -> AI Confidence: **99.31%**
389. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/snapshot/fudge.rs`** -> AI Confidence: **99.31%**
390. **`src/tools/rust-analyzer/crates/hir-ty/src/representability.rs`** -> AI Confidence: **99.31%**
391. **`src/tools/rust-analyzer/crates/hir/src/display.rs`** -> AI Confidence: **99.31%**
392. **`src/tools/rust-analyzer/crates/hir/src/from_id.rs`** -> AI Confidence: **99.31%**
393. **`src/tools/rust-analyzer/crates/hir/src/source_analyzer.rs`** -> AI Confidence: **99.31%**
394. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/add_return_type.rs`** -> AI Confidence: **99.31%**
395. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/apply_demorgan.rs`** -> AI Confidence: **99.31%**
396. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_bool_then.rs`** -> AI Confidence: **99.31%**
397. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_let_else_to_match.rs`** -> AI Confidence: **99.31%**
398. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_range_for_to_while.rs`** -> AI Confidence: **99.31%**
399. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_two_arm_bool_match_to_matches_macro.rs`** -> AI Confidence: **99.31%**
400. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_while_to_loop.rs`** -> AI Confidence: **99.31%**
401. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/extract_variable.rs`** -> AI Confidence: **99.31%**
402. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/inline_const_as_literal.rs`** -> AI Confidence: **99.31%**
403. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/invert_if.rs`** -> AI Confidence: **99.31%**
404. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/pull_assignment_up.rs`** -> AI Confidence: **99.31%**
405. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/remove_else_branches.rs`** -> AI Confidence: **99.31%**
406. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/remove_parentheses.rs`** -> AI Confidence: **99.31%**
407. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/replace_if_let_with_match.rs`** -> AI Confidence: **99.31%**
408. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/toggle_macro_delimiter.rs`** -> AI Confidence: **99.31%**
409. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/unwrap_block.rs`** -> AI Confidence: **99.31%**
410. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/keyword.rs`** -> AI Confidence: **99.31%**
411. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/lifetime.rs`** -> AI Confidence: **99.31%**
412. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/pattern.rs`** -> AI Confidence: **99.31%**
413. **`src/tools/rust-analyzer/crates/ide-completion/src/context/analysis.rs`** -> AI Confidence: **99.31%**
414. **`src/tools/rust-analyzer/crates/ide-db/src/defs.rs`** -> AI Confidence: **99.31%**
415. **`src/tools/rust-analyzer/crates/ide-db/src/famous_defs.rs`** -> AI Confidence: **99.31%**
416. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/remove_unnecessary_else.rs`** -> AI Confidence: **99.31%**
417. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/tests/overly_long_real_world_cases.rs`** -> AI Confidence: **99.31%**
418. **`src/tools/rust-analyzer/crates/ide/src/highlight_related.rs`** -> AI Confidence: **99.31%**
419. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/closing_brace.rs`** -> AI Confidence: **99.31%**
420. **`src/tools/rust-analyzer/crates/ide/src/syntax_highlighting.rs`** -> AI Confidence: **99.31%**
421. **`src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/highlight.rs`** -> AI Confidence: **99.31%**
422. **`src/tools/rust-analyzer/crates/parser/src/grammar/expressions.rs`** -> AI Confidence: **99.31%**
423. **`src/tools/rust-analyzer/crates/parser/src/grammar/items.rs`** -> AI Confidence: **99.31%**
424. **`src/tools/rust-analyzer/crates/parser/src/lexed_str.rs`** -> AI Confidence: **99.31%**
425. **`src/tools/rust-analyzer/crates/proc-macro-srv/src/token_stream.rs`** -> AI Confidence: **99.31%**
426. **`src/tools/rust-analyzer/crates/rust-analyzer/src/bin/main.rs`** -> AI Confidence: **99.31%**
427. **`src/tools/rust-analyzer/crates/syntax/src/ast/edit_in_place.rs`** -> AI Confidence: **99.31%**
428. **`src/tools/rust-analyzer/crates/syntax/src/ast/expr_ext.rs`** -> AI Confidence: **99.31%**
429. **`src/tools/rust-analyzer/crates/syntax/src/ast/prec.rs`** -> AI Confidence: **99.31%**
430. **`src/tools/rust-analyzer/crates/syntax/src/validation.rs`** -> AI Confidence: **99.31%**
431. **`src/tools/rust-analyzer/xtask/src/install.rs`** -> AI Confidence: **99.31%**
432. **`src/tools/rust-analyzer/xtask/src/pgo.rs`** -> AI Confidence: **99.31%**
433. **`src/tools/rust-analyzer/xtask/src/publish/notes.rs`** -> AI Confidence: **99.31%**
434. **`src/tools/rust-installer/src/combiner.rs`** -> AI Confidence: **99.31%**
435. **`src/tools/rust-installer/src/generator.rs`** -> AI Confidence: **99.31%**
436. **`src/tools/rust-installer/src/util.rs`** -> AI Confidence: **99.31%**
437. **`src/tools/rustfmt/src/bin/main.rs`** -> AI Confidence: **99.31%**
438. **`src/tools/rustfmt/src/cargo-fmt/main.rs`** -> AI Confidence: **99.31%**
439. **`src/tools/rustfmt/src/comment.rs`** -> AI Confidence: **99.31%**
440. **`src/tools/rustfmt/src/config/mod.rs`** -> AI Confidence: **99.31%**
441. **`src/tools/rustfmt/src/lists.rs`** -> AI Confidence: **99.31%**
442. **`src/tools/rustfmt/src/matches.rs`** -> AI Confidence: **99.31%**
443. **`src/tools/rustfmt/src/modules.rs`** -> AI Confidence: **99.31%**
444. **`src/tools/rustfmt/src/overflow.rs`** -> AI Confidence: **99.31%**
445. **`src/tools/rustfmt/src/types.rs`** -> AI Confidence: **99.31%**
446. **`src/tools/tidy/src/deps.rs`** -> AI Confidence: **99.31%**
447. **`src/tools/tidy/src/style.rs`** -> AI Confidence: **99.31%**
448. **`src/tools/tidy/src/target_specific_tests.rs`** -> AI Confidence: **99.31%**
449. **`src/tools/tidy/src/tests_revision_unpaired_stdout_stderr.rs`** -> AI Confidence: **99.31%**
450. **`tests/run-make/native-link-modifier-bundle/rmake.rs`** -> AI Confidence: **99.31%**
451. **`tests/run-make/no-builtins-linker-plugin-lto/rmake.rs`** -> AI Confidence: **99.31%**
452. **`tests/run-make/optimization-remarks-dir-pgo/rmake.rs`** -> AI Confidence: **99.31%**
453. **`tests/run-make/optimization-remarks-dir/rmake.rs`** -> AI Confidence: **99.31%**
454. **`tests/run-make/symbols-all-mangled/rmake.rs`** -> AI Confidence: **99.31%**
455. **`tests/ui/enum/namespaced-enum-emulate-flat-xc.rs`** -> AI Confidence: **99.31%**
456. **`tests/ui/rfcs/rfc-2008-non-exhaustive/omitted-patterns.rs`** -> AI Confidence: **99.31%**
457. **`tests/ui/rfcs/rfc-2091-track-caller/std-panic-locations.rs`** -> AI Confidence: **99.31%**
458. **`tests/ui/std/stdio-from.rs`** -> AI Confidence: **99.31%**
459. **`src/bootstrap/bootstrap.py`** -> AI Confidence: **99.31%**
460. **`src/etc/htmldocck.py`** -> AI Confidence: **99.31%**
461. **`src/etc/lldb_batchmode.py`** -> AI Confidence: **99.31%**
462. **`x.py`** -> AI Confidence: **99.31%**
463. **`src/tools/rust-analyzer/editors/code/src/client.ts`** -> AI Confidence: **99.31%**
464. **`src/tools/rust-analyzer/editors/code/src/ctx.ts`** -> AI Confidence: **99.31%**
465. **`compiler/rustc_data_structures/src/base_n/tests.rs`** -> AI Confidence: **99.29%**
466. **`compiler/rustc_middle/src/arena.rs`** -> AI Confidence: **99.29%**
467. **`library/compiler-builtins/compiler-builtins/src/avr.rs`** -> AI Confidence: **99.29%**
468. **`library/compiler-builtins/compiler-builtins/src/macros.rs`** -> AI Confidence: **99.29%**
469. **`library/compiler-builtins/compiler-builtins/src/sync/arm_thumb_shared.rs`** -> AI Confidence: **99.29%**
470. **`library/compiler-builtins/crates/panic-handler/src/lib.rs`** -> AI Confidence: **99.29%**
471. **`library/compiler-builtins/libm/src/math/generic/fmaximum.rs`** -> AI Confidence: **99.29%**
472. **`library/compiler-builtins/libm/src/math/generic/fmaximum_num.rs`** -> AI Confidence: **99.29%**
473. **`library/compiler-builtins/libm/src/math/generic/fminimum.rs`** -> AI Confidence: **99.29%**
474. **`library/compiler-builtins/libm/src/math/generic/fminimum_num.rs`** -> AI Confidence: **99.29%**
475. **`library/compiler-builtins/libm/src/math/rem_pio2_large.rs`** -> AI Confidence: **99.29%**
476. **`library/core/src/bool.rs`** -> AI Confidence: **99.29%**
477. **`library/std/src/sys/platform_version/darwin/public_extern.rs`** -> AI Confidence: **99.29%**
478. **`library/std/src/sys/thread_local/guard/key.rs`** -> AI Confidence: **99.29%**
479. **`library/std_detect/src/detect/macros.rs`** -> AI Confidence: **99.29%**
480. **`library/stdarch/crates/core_arch/src/x86/macros.rs`** -> AI Confidence: **99.29%**
481. **`library/stdarch/crates/core_arch/src/x86_64/macros.rs`** -> AI Confidence: **99.29%**
482. **`library/windows_link/src/lib.rs`** -> AI Confidence: **99.29%**
483. **`src/build_helper/src/targets.rs`** -> AI Confidence: **99.29%**
484. **`src/tools/clippy/build.rs`** -> AI Confidence: **99.29%**
485. **`src/tools/clippy/clippy_lints/src/deprecated_lints.rs`** -> AI Confidence: **99.29%**
486. **`src/tools/clippy/tests/ui-toml/collapsible_if/collapsible_else_if.rs`** -> AI Confidence: **99.29%**
487. **`src/tools/clippy/tests/ui-toml/collapsible_if/collapsible_if.rs`** -> AI Confidence: **99.29%**
488. **`src/tools/clippy/tests/ui/author/loop.rs`** -> AI Confidence: **99.29%**
489. **`src/tools/clippy/tests/ui/author/macro_in_loop.rs`** -> AI Confidence: **99.29%**
490. **`src/tools/clippy/tests/ui/bool_to_int_with_if.rs`** -> AI Confidence: **99.29%**
491. **`src/tools/clippy/tests/ui/checked_unwrap/complex_conditionals.rs`** -> AI Confidence: **99.29%**
492. **`src/tools/clippy/tests/ui/checked_unwrap/if_let_chains.rs`** -> AI Confidence: **99.29%**
493. **`src/tools/clippy/tests/ui/cognitive_complexity_attr_used.rs`** -> AI Confidence: **99.29%**
494. **`src/tools/clippy/tests/ui/collapsible_else_if_unfixable.rs`** -> AI Confidence: **99.29%**
495. **`src/tools/clippy/tests/ui/collapsible_if.rs`** -> AI Confidence: **99.29%**
496. **`src/tools/clippy/tests/ui/collapsible_if_unfixable.rs`** -> AI Confidence: **99.29%**
497. **`src/tools/clippy/tests/ui/crashes/ice-11755.rs`** -> AI Confidence: **99.29%**
498. **`src/tools/clippy/tests/ui/crashes/ice-11939.rs`** -> AI Confidence: **99.29%**
499. **`src/tools/clippy/tests/ui/crashes/ice-1588.rs`** -> AI Confidence: **99.29%**
500. **`src/tools/clippy/tests/ui/crashes/ice-7231.rs`** -> AI Confidence: **99.29%**
501. **`src/tools/clippy/tests/ui/crashes/if_same_then_else.rs`** -> AI Confidence: **99.29%**
502. **`src/tools/clippy/tests/ui/crashes/issue-825.rs`** -> AI Confidence: **99.29%**
503. **`src/tools/clippy/tests/ui/crashes/match_same_arms_const.rs`** -> AI Confidence: **99.29%**
504. **`src/tools/clippy/tests/ui/crate_level_checks/no_std_main_recursion.rs`** -> AI Confidence: **99.29%**
505. **`src/tools/clippy/tests/ui/double_comparison.rs`** -> AI Confidence: **99.29%**
506. **`src/tools/clippy/tests/ui/else_if_without_else.rs`** -> AI Confidence: **99.29%**
507. **`src/tools/clippy/tests/ui/empty_loop.rs`** -> AI Confidence: **99.29%**
508. **`src/tools/clippy/tests/ui/empty_loop_no_std.rs`** -> AI Confidence: **99.29%**
509. **`src/tools/clippy/tests/ui/exit1.rs`** -> AI Confidence: **99.29%**
510. **`src/tools/clippy/tests/ui/exit1_compile_flag_test.rs`** -> AI Confidence: **99.29%**
511. **`src/tools/clippy/tests/ui/exit2.rs`** -> AI Confidence: **99.29%**
512. **`src/tools/clippy/tests/ui/exit2_compile_flag_test.rs`** -> AI Confidence: **99.29%**
513. **`src/tools/clippy/tests/ui/exit3.rs`** -> AI Confidence: **99.29%**
514. **`src/tools/clippy/tests/ui/exit3_compile_flag_test.rs`** -> AI Confidence: **99.29%**
515. **`src/tools/clippy/tests/ui/floating_point_abs.rs`** -> AI Confidence: **99.29%**
516. **`src/tools/clippy/tests/ui/if_not_else.rs`** -> AI Confidence: **99.29%**
517. **`src/tools/clippy/tests/ui/if_not_else_bittest.rs`** -> AI Confidence: **99.29%**
518. **`src/tools/clippy/tests/ui/if_same_then_else.rs`** -> AI Confidence: **99.29%**
519. **`src/tools/clippy/tests/ui/ifs_same_cond.rs`** -> AI Confidence: **99.29%**
520. **`src/tools/clippy/tests/ui/iter_out_of_bounds.rs`** -> AI Confidence: **99.29%**
521. **`src/tools/clippy/tests/ui/manual_assert.rs`** -> AI Confidence: **99.29%**
522. **`src/tools/clippy/tests/ui/manual_filter.rs`** -> AI Confidence: **99.29%**
523. **`src/tools/clippy/tests/ui/manual_float_methods.rs`** -> AI Confidence: **99.29%**
524. **`src/tools/clippy/tests/ui/match_overlapping_arm.rs`** -> AI Confidence: **99.29%**
525. **`src/tools/clippy/tests/ui/match_wild_err_arm.rs`** -> AI Confidence: **99.29%**
526. **`src/tools/clippy/tests/ui/needless_bitwise_bool.rs`** -> AI Confidence: **99.29%**
527. **`src/tools/clippy/tests/ui/needless_continue.rs`** -> AI Confidence: **99.29%**
528. **`src/tools/clippy/tests/ui/needless_else.rs`** -> AI Confidence: **99.29%**
529. **`src/tools/clippy/tests/ui/needless_ifs.rs`** -> AI Confidence: **99.29%**
530. **`src/tools/clippy/tests/ui/only_used_in_recursion.rs`** -> AI Confidence: **99.29%**
531. **`src/tools/clippy/tests/ui/panicking_overflow_checks.rs`** -> AI Confidence: **99.29%**
532. **`src/tools/clippy/tests/ui/println_empty_string.rs`** -> AI Confidence: **99.29%**
533. **`src/tools/clippy/tests/ui/question_mark_used.rs`** -> AI Confidence: **99.29%**
534. **`src/tools/clippy/tests/ui/result_unit_error_no_std.rs`** -> AI Confidence: **99.29%**
535. **`src/tools/clippy/tests/ui/reversed_empty_ranges_loops_fixable.rs`** -> AI Confidence: **99.29%**
536. **`src/tools/clippy/tests/ui/reversed_empty_ranges_loops_unfixable.rs`** -> AI Confidence: **99.29%**
537. **`src/tools/clippy/tests/ui/same_functions_in_if_condition.rs`** -> AI Confidence: **99.29%**
538. **`src/tools/clippy/tests/ui/semicolon_outside_block.rs`** -> AI Confidence: **99.29%**
539. **`src/tools/clippy/tests/ui/single_match_else_deref_patterns.rs`** -> AI Confidence: **99.29%**
540. **`src/tools/clippy/tests/ui/starts_ends_with.rs`** -> AI Confidence: **99.29%**
541. **`src/tools/clippy/tests/ui/suspicious_else_formatting.rs`** -> AI Confidence: **99.29%**
542. **`src/tools/clippy/tests/ui/uninlined_format_args_panic.rs`** -> AI Confidence: **99.29%**
543. **`src/tools/clippy/tests/ui/unnecessary_semicolon_feature_stmt_expr_attributes.rs`** -> AI Confidence: **99.29%**
544. **`src/tools/clippy/tests/workspace_test/path_dep/src/lib.rs`** -> AI Confidence: **99.29%**
545. **`src/tools/miri/bench-cargo-miri/big-allocs/src/main.rs`** -> AI Confidence: **99.29%**
546. **`src/tools/miri/bench-cargo-miri/range-iteration/src/main.rs`** -> AI Confidence: **99.29%**
547. **`src/tools/miri/cargo-miri/build.rs`** -> AI Confidence: **99.29%**
548. **`src/tools/miri/tests/fail/alloc/no_global_allocator.rs`** -> AI Confidence: **99.29%**
549. **`src/tools/miri/tests/fail/panic/abort_unwind.rs`** -> AI Confidence: **99.29%**
550. **`src/tools/miri/tests/genmc/fail/shims/exit.rs`** -> AI Confidence: **99.29%**
551. **`src/tools/miri/tests/pass/function_calls/tail_call.rs`** -> AI Confidence: **99.29%**
552. **`src/tools/miri/tests/pass/issues/issue-17877.rs`** -> AI Confidence: **99.29%**
553. **`src/tools/miri/tests/pass/loop-break-value.rs`** -> AI Confidence: **99.29%**
554. **`src/tools/run-make-support/src/artifact_names.rs`** -> AI Confidence: **99.29%**
555. **`src/tools/rust-analyzer/crates/hir-def/src/macro_expansion_tests/mbe/meta_syntax.rs`** -> AI Confidence: **99.29%**
556. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/break_outside_of_loop.rs`** -> AI Confidence: **99.29%**
557. **`src/tools/rust-analyzer/crates/parser/test_data/parser/err/0008_item_block_recovery.rs`** -> AI Confidence: **99.29%**
558. **`src/tools/rust-analyzer/crates/parser/test_data/parser/err/0010_unsafe_lambda_block.rs`** -> AI Confidence: **99.29%**
559. **`src/tools/rust-analyzer/crates/parser/test_data/parser/err/0032_match_arms_inner_attrs.rs`** -> AI Confidence: **99.29%**
560. **`src/tools/rust-analyzer/crates/parser/test_data/parser/err/0033_match_arms_outer_attrs.rs`** -> AI Confidence: **99.29%**
561. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/err/match_arms_recovery.rs`** -> AI Confidence: **99.29%**
562. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/break_ambiguity.rs`** -> AI Confidence: **99.29%**
563. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/break_expr.rs`** -> AI Confidence: **99.29%**
564. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/closure_binder.rs`** -> AI Confidence: **99.29%**
565. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/closure_body_underscore_assignment.rs`** -> AI Confidence: **99.29%**
566. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/closure_range_method_call.rs`** -> AI Confidence: **99.29%**
567. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/continue_expr.rs`** -> AI Confidence: **99.29%**
568. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/exclusive_range_pat.rs`** -> AI Confidence: **99.29%**
569. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/for_range_from.rs`** -> AI Confidence: **99.29%**
570. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/if_expr.rs`** -> AI Confidence: **99.29%**
571. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/label.rs`** -> AI Confidence: **99.29%**
572. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/literal_pattern.rs`** -> AI Confidence: **99.29%**
573. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_arm.rs`** -> AI Confidence: **99.29%**
574. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_arms_commas.rs`** -> AI Confidence: **99.29%**
575. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_arms_inner_attribute.rs`** -> AI Confidence: **99.29%**
576. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_arms_outer_attributes.rs`** -> AI Confidence: **99.29%**
577. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_expr.rs`** -> AI Confidence: **99.29%**
578. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/no_semi_after_block.rs`** -> AI Confidence: **99.29%**
579. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/or_pattern.rs`** -> AI Confidence: **99.29%**
580. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/range_pat.rs`** -> AI Confidence: **99.29%**
581. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/stmt_postfix_expr_ambiguity.rs`** -> AI Confidence: **99.29%**
582. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0033_label_break.rs`** -> AI Confidence: **99.29%**
583. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0052_for_range_block.rs`** -> AI Confidence: **99.29%**
584. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0056_neq_in_type.rs`** -> AI Confidence: **99.29%**
585. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0057_loop_in_call.rs`** -> AI Confidence: **99.29%**
586. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0059_loops_in_parens.rs`** -> AI Confidence: **99.29%**
587. **`src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0071_stmt_attr_placement.rs`** -> AI Confidence: **99.29%**
588. **`src/tools/rust-analyzer/crates/syntax/test_data/parser/fuzz-failures/0003.rs`** -> AI Confidence: **99.29%**
589. **`src/tools/rustfmt/config_proc_macro/src/attrs.rs`** -> AI Confidence: **99.29%**
590. **`src/tools/rustfmt/src/release_channel.rs`** -> AI Confidence: **99.29%**
591. **`src/tools/rustfmt/tests/parser/issue-4126/invalid.rs`** -> AI Confidence: **99.29%**
592. **`src/tools/rustfmt/tests/parser/unclosed-delims/issue_4466.rs`** -> AI Confidence: **99.29%**
593. **`src/tools/rustfmt/tests/source/arrow_in_comments/arrow_in_single_comment.rs`** -> AI Confidence: **99.29%**
594. **`src/tools/rustfmt/tests/source/arrow_in_comments/multiple_arrows.rs`** -> AI Confidence: **99.29%**
595. **`src/tools/rustfmt/tests/source/binary-expr.rs`** -> AI Confidence: **99.29%**
596. **`src/tools/rustfmt/tests/source/binop-separator-back/comp.rs`** -> AI Confidence: **99.29%**
597. **`src/tools/rustfmt/tests/source/binop-separator-back/logic.rs`** -> AI Confidence: **99.29%**
598. **`src/tools/rustfmt/tests/source/binop-separator-back/patterns.rs`** -> AI Confidence: **99.29%**
599. **`src/tools/rustfmt/tests/source/cfg_if/detect/arch/aarch64.rs`** -> AI Confidence: **99.29%**
600. **`src/tools/rustfmt/tests/source/cfg_if/detect/arch/x86.rs`** -> AI Confidence: **99.29%**
601. **`src/tools/rustfmt/tests/source/cfg_if/detect/error_macros.rs`** -> AI Confidence: **99.29%**
602. **`src/tools/rustfmt/tests/source/closure-block-labels.rs`** -> AI Confidence: **99.29%**
603. **`src/tools/rustfmt/tests/source/configs/control_brace_style/always_next_line.rs`** -> AI Confidence: **99.29%**
604. **`src/tools/rustfmt/tests/source/configs/control_brace_style/always_same_line.rs`** -> AI Confidence: **99.29%**
605. **`src/tools/rustfmt/tests/source/configs/control_brace_style/closing_next_line.rs`** -> AI Confidence: **99.29%**
606. **`src/tools/rustfmt/tests/source/configs/disable_all_formatting/false.rs`** -> AI Confidence: **99.29%**
607. **`src/tools/rustfmt/tests/source/configs/disable_all_formatting/true.rs`** -> AI Confidence: **99.29%**
608. **`src/tools/rustfmt/tests/source/configs/force_multiline_block/false.rs`** -> AI Confidence: **99.29%**
609. **`src/tools/rustfmt/tests/source/configs/force_multiline_block/true.rs`** -> AI Confidence: **99.29%**
610. **`src/tools/rustfmt/tests/source/configs/match_arm_blocks/false.rs`** -> AI Confidence: **99.29%**
611. **`src/tools/rustfmt/tests/source/configs/match_arm_blocks/true.rs`** -> AI Confidence: **99.29%**
612. **`src/tools/rustfmt/tests/source/configs/match_arm_indent/attrs.rs`** -> AI Confidence: **99.29%**
613. **`src/tools/rustfmt/tests/source/configs/match_arm_indent/guards.rs`** -> AI Confidence: **99.29%**
614. **`src/tools/rustfmt/tests/source/configs/match_arm_indent/leading_pipes.rs`** -> AI Confidence: **99.29%**
615. **`src/tools/rustfmt/tests/source/configs/match_arm_indent/nested.rs`** -> AI Confidence: **99.29%**
616. **`src/tools/rustfmt/tests/source/configs/match_arm_indent/unindent.rs`** -> AI Confidence: **99.29%**
617. **`src/tools/rustfmt/tests/source/configs/match_arm_leading_pipes/always.rs`** -> AI Confidence: **99.29%**
618. **`src/tools/rustfmt/tests/source/configs/match_arm_leading_pipes/never.rs`** -> AI Confidence: **99.29%**
619. **`src/tools/rustfmt/tests/source/configs/match_arm_leading_pipes/preserve.rs`** -> AI Confidence: **99.29%**
620. **`src/tools/rustfmt/tests/source/configs/match_block_trailing_comma/false.rs`** -> AI Confidence: **99.29%**
621. **`src/tools/rustfmt/tests/source/configs/match_block_trailing_comma/true.rs`** -> AI Confidence: **99.29%**
622. **`src/tools/rustfmt/tests/source/control-brace-style-always-next-line.rs`** -> AI Confidence: **99.29%**
623. **`src/tools/rustfmt/tests/source/control-brace-style-always-same-line.rs`** -> AI Confidence: **99.29%**
624. **`src/tools/rustfmt/tests/source/else-if-brace-style-always-next-line.rs`** -> AI Confidence: **99.29%**
625. **`src/tools/rustfmt/tests/source/else-if-brace-style-always-same-line.rs`** -> AI Confidence: **99.29%**
626. **`src/tools/rustfmt/tests/source/else-if-brace-style-closing-next-line.rs`** -> AI Confidence: **99.29%**
627. **`src/tools/rustfmt/tests/source/issue-1021.rs`** -> AI Confidence: **99.29%**
628. **`src/tools/rustfmt/tests/source/issue-1239.rs`** -> AI Confidence: **99.29%**
629. **`src/tools/rustfmt/tests/source/issue-2496.rs`** -> AI Confidence: **99.29%**
630. **`src/tools/rustfmt/tests/source/issue-2955.rs`** -> AI Confidence: **99.29%**
631. **`src/tools/rustfmt/tests/source/issue-3131.rs`** -> AI Confidence: **99.29%**
632. **`src/tools/rustfmt/tests/source/issue-3227/two.rs`** -> AI Confidence: **99.29%**
633. **`src/tools/rustfmt/tests/source/issue-3272/v1.rs`** -> AI Confidence: **99.29%**
634. **`src/tools/rustfmt/tests/source/issue-3272/v2.rs`** -> AI Confidence: **99.29%**
635. **`src/tools/rustfmt/tests/source/issue-3532.rs`** -> AI Confidence: **99.29%**
636. **`src/tools/rustfmt/tests/source/issue-4427.rs`** -> AI Confidence: **99.29%**
637. **`src/tools/rustfmt/tests/source/issue-447.rs`** -> AI Confidence: **99.29%**
638. **`src/tools/rustfmt/tests/source/issue-4577.rs`** -> AI Confidence: **99.29%**
639. **`src/tools/rustfmt/tests/source/issue-4615/minimum_example.rs`** -> AI Confidence: **99.29%**
640. **`src/tools/rustfmt/tests/source/issue-855.rs`** -> AI Confidence: **99.29%**
641. **`src/tools/rustfmt/tests/source/issue_3844.rs`** -> AI Confidence: **99.29%**
642. **`src/tools/rustfmt/tests/source/issue_3868.rs`** -> AI Confidence: **99.29%**
643. **`src/tools/rustfmt/tests/source/issue_5912.rs`** -> AI Confidence: **99.29%**
644. **`src/tools/rustfmt/tests/source/label_break.rs`** -> AI Confidence: **99.29%**
645. **`src/tools/rustfmt/tests/source/match-block-trailing-comma.rs`** -> AI Confidence: **99.29%**
646. **`src/tools/rustfmt/tests/source/match-flattening.rs`** -> AI Confidence: **99.29%**
647. **`src/tools/rustfmt/tests/source/match-nowrap-trailing-comma.rs`** -> AI Confidence: **99.29%**
648. **`src/tools/rustfmt/tests/source/match-nowrap.rs`** -> AI Confidence: **99.29%**
649. **`src/tools/rustfmt/tests/source/match_overflow_expr.rs`** -> AI Confidence: **99.29%**
650. **`src/tools/rustfmt/tests/source/nested-if-else.rs`** -> AI Confidence: **99.29%**
651. **`src/tools/rustfmt/tests/source/pattern-condense-wildcards.rs`** -> AI Confidence: **99.29%**
652. **`src/tools/rustfmt/tests/source/postfix-match/pf-match.rs`** -> AI Confidence: **99.29%**
653. **`src/tools/rustfmt/tests/source/struct_tuple_visual.rs`** -> AI Confidence: **99.29%**
654. **`src/tools/rustfmt/tests/source/trailing-semicolon/loop-bodies-edition-2021-style-edition-2027.rs`** -> AI Confidence: **99.29%**
655. **`src/tools/rustfmt/tests/source/trailing-semicolon/loop-bodies-edition-2024-style-edition-2024.rs`** -> AI Confidence: **99.29%**
656. **`src/tools/rustfmt/tests/source/trailing-semicolon/loop-bodies.rs`** -> AI Confidence: **99.29%**
657. **`tests/assembly-llvm/x86_64-no-jump-tables.rs`** -> AI Confidence: **99.29%**
658. **`tests/coverage-run-rustdoc/auxiliary/doctest_crate.rs`** -> AI Confidence: **99.29%**
659. **`tests/crashes/138361.rs`** -> AI Confidence: **99.29%**
660. **`tests/crashes/auxiliary/overlapping_spans_helper.rs`** -> AI Confidence: **99.29%**
661. **`tests/debuginfo/constant-in-match-pattern.rs`** -> AI Confidence: **99.29%**
662. **`tests/debuginfo/step-into-match.rs`** -> AI Confidence: **99.29%**
663. **`tests/incremental/hashes/match_expressions.rs`** -> AI Confidence: **99.29%**
664. **`tests/incremental/mir-opt.rs`** -> AI Confidence: **99.29%**
665. **`tests/incremental/spans_significant_w_panic.rs`** -> AI Confidence: **99.29%**
666. **`tests/incremental/static_refering_to_other_static3/issue.rs`** -> AI Confidence: **99.29%**
667. **`tests/incremental/user-written-closure-synthetic-closure-conflict.rs`** -> AI Confidence: **99.29%**
668. **`tests/mir-opt/box_partial_move.rs`** -> AI Confidence: **99.29%**
669. **`tests/mir-opt/building/match/deref-patterns/string.rs`** -> AI Confidence: **99.29%**
670. **`tests/mir-opt/building/match/exponential_or.rs`** -> AI Confidence: **99.29%**
671. **`tests/mir-opt/building/match/sort_candidates.rs`** -> AI Confidence: **99.29%**
672. **`tests/mir-opt/building/while_storage.rs`** -> AI Confidence: **99.29%**
673. **`tests/mir-opt/const_goto_const_eval_fail.rs`** -> AI Confidence: **99.29%**
674. **`tests/mir-opt/const_prop/switch_int.rs`** -> AI Confidence: **99.29%**
675. **`tests/mir-opt/dataflow-const-prop/issue_81605.rs`** -> AI Confidence: **99.29%**
676. **`tests/mir-opt/derefer_complex_case.rs`** -> AI Confidence: **99.29%**
677. **`tests/mir-opt/early_otherwise_branch.rs`** -> AI Confidence: **99.29%**
678. **`tests/mir-opt/early_otherwise_branch_noopt.rs`** -> AI Confidence: **99.29%**
679. **`tests/mir-opt/inline/forced_closure.rs`** -> AI Confidence: **99.29%**
680. **`tests/mir-opt/instsimplify/bool_compare.rs`** -> AI Confidence: **99.29%**
681. **`tests/mir-opt/issue_62289.rs`** -> AI Confidence: **99.29%**
682. **`tests/mir-opt/match_arm_scopes.rs`** -> AI Confidence: **99.29%**
683. **`tests/mir-opt/multiple_return_terminators.rs`** -> AI Confidence: **99.29%**
684. **`tests/mir-opt/optimize_none.rs`** -> AI Confidence: **99.29%**
685. **`tests/mir-opt/or_pattern.rs`** -> AI Confidence: **99.29%**
686. **`tests/mir-opt/otherwise_drops.rs`** -> AI Confidence: **99.29%**
687. **`tests/mir-opt/range/ssa_range.rs`** -> AI Confidence: **99.29%**
688. **`tests/mir-opt/remove_fake_borrows.rs`** -> AI Confidence: **99.29%**
689. **`tests/mir-opt/simplify_cfg.rs`** -> AI Confidence: **99.29%**
690. **`tests/mir-opt/simplify_if.rs`** -> AI Confidence: **99.29%**
691. **`tests/mir-opt/simplify_locals_removes_unused_discriminant_reads.rs`** -> AI Confidence: **99.29%**
692. **`tests/pretty/hir-if-else.rs`** -> AI Confidence: **99.29%**
693. **`tests/pretty/hir-pretty-loop.rs`** -> AI Confidence: **99.29%**
694. **`tests/pretty/if-else.rs`** -> AI Confidence: **99.29%**
695. **`tests/pretty/issue-19077.rs`** -> AI Confidence: **99.29%**
696. **`tests/pretty/never-pattern.rs`** -> AI Confidence: **99.29%**
697. **`tests/pretty/or-pattern-paren.rs`** -> AI Confidence: **99.29%**
698. **`tests/pretty/postfix-match/simple-matches.rs`** -> AI Confidence: **99.29%**
699. **`tests/pretty/try-blocks.rs`** -> AI Confidence: **99.29%**
700. **`tests/pretty/unary-op-disambig.rs`** -> AI Confidence: **99.29%**
701. **`tests/run-make/linker-warning/fake-linker.rs`** -> AI Confidence: **99.29%**
702. **`tests/run-make/missing-unstable-trait-bound/missing-bound.rs`** -> AI Confidence: **99.29%**
703. **`tests/run-make/mixing-formats/rmake.rs`** -> AI Confidence: **99.29%**
704. **`tests/run-make/option-output-no-space/rmake.rs`** -> AI Confidence: **99.29%**
705. **`tests/run-make/pgo-branch-weights/interesting.rs`** -> AI Confidence: **99.29%**
706. **`tests/run-make/pgo-branch-weights/main.rs`** -> AI Confidence: **99.29%**
707. **`tests/run-make/wasm-spurious-import/main.rs`** -> AI Confidence: **99.29%**
708. **`tests/rustdoc-gui/src/scrape_examples/examples/check.rs`** -> AI Confidence: **99.29%**
709. **`tests/rustdoc-html/array-links.rs`** -> AI Confidence: **99.29%**
710. **`tests/rustdoc-html/decl-line-wrapping-empty-arg-list.rs`** -> AI Confidence: **99.29%**
711. **`tests/rustdoc-html/inline_cross/auxiliary/macro-vis.rs`** -> AI Confidence: **99.29%**
712. **`tests/rustdoc-html/notable-trait/doc-notable_trait-mut_t_is_not_ref_t.rs`** -> AI Confidence: **99.29%**
713. **`tests/rustdoc-html/slice-links.rs`** -> AI Confidence: **99.29%**
714. **`tests/rustdoc-html/source-code-pages/shebang.rs`** -> AI Confidence: **99.29%**
715. **`tests/rustdoc-js/never-search.rs`** -> AI Confidence: **99.29%**
716. **`tests/rustdoc-json/lifetime/longest.rs`** -> AI Confidence: **99.29%**
717. **`tests/rustdoc-ui/issues/auxiliary/panic-handler.rs`** -> AI Confidence: **99.29%**
718. **`tests/rustdoc-ui/issues/duplicate-panic-impl-107918.rs`** -> AI Confidence: **99.29%**
719. **`tests/ui/abi/extern/auxiliary/extern-crosscrate-source.rs`** -> AI Confidence: **99.29%**
720. **`tests/ui/abi/interrupt-returns-never-or-unit.rs`** -> AI Confidence: **99.29%**
721. **`tests/ui/argument-suggestions/extra_arguments.rs`** -> AI Confidence: **99.29%**
722. **`tests/ui/array-slice-vec/match_arr_unknown_len.rs`** -> AI Confidence: **99.29%**
723. **`tests/ui/array-slice-vec/slice-pat-type-mismatches.rs`** -> AI Confidence: **99.29%**
724. **`tests/ui/array-slice-vec/vec-matching-fixed.rs`** -> AI Confidence: **99.29%**
725. **`tests/ui/asm/binary_asm_labels.rs`** -> AI Confidence: **99.29%**
726. **`tests/ui/asm/binary_asm_labels_allowed.rs`** -> AI Confidence: **99.29%**
727. **`tests/ui/asm/simple_global_asm.rs`** -> AI Confidence: **99.29%**
728. **`tests/ui/asm/x86_64/global_asm_escape.rs`** -> AI Confidence: **99.29%**
729. **`tests/ui/associated-inherent-types/issue-111879-1.rs`** -> AI Confidence: **99.29%**
730. **`tests/ui/async-await/async-closure-matches-expr.rs`** -> AI Confidence: **99.29%**
731. **`tests/ui/async-await/async-fn/method-call-pos.rs`** -> AI Confidence: **99.29%**
732. **`tests/ui/async-await/issue-73541-1.rs`** -> AI Confidence: **99.29%**
733. **`tests/ui/async-await/issue-73541-2.rs`** -> AI Confidence: **99.29%**
734. **`tests/ui/async-await/issue-73541-3.rs`** -> AI Confidence: **99.29%**
735. **`tests/ui/async-await/issue-73541.rs`** -> AI Confidence: **99.29%**
736. **`tests/ui/async-await/issue-84841.rs`** -> AI Confidence: **99.29%**
737. **`tests/ui/async-await/labeled-break-in-async-fn-ice-66702.rs`** -> AI Confidence: **99.29%**
738. **`tests/ui/async-await/try-in-sync.rs`** -> AI Confidence: **99.29%**
739. **`tests/ui/attributes/dump_def_parents.rs`** -> AI Confidence: **99.29%**
740. **`tests/ui/attributes/statement-attribute-validation.rs`** -> AI Confidence: **99.29%**
741. **`tests/ui/binding/borrowed-ptr-pattern-2.rs`** -> AI Confidence: **99.29%**
742. **`tests/ui/binding/borrowed-ptr-pattern-3.rs`** -> AI Confidence: **99.29%**
743. **`tests/ui/binding/const-param.rs`** -> AI Confidence: **99.29%**
744. **`tests/ui/binding/exhaustive-bool-match-sanity.rs`** -> AI Confidence: **99.29%**
745. **`tests/ui/binding/match-borrowed_str.rs`** -> AI Confidence: **99.29%**
746. **`tests/ui/binding/match-pattern-simple.rs`** -> AI Confidence: **99.29%**
747. **`tests/ui/binding/match-range-static.rs`** -> AI Confidence: **99.29%**
748. **`tests/ui/binding/match-range.rs`** -> AI Confidence: **99.29%**
749. **`tests/ui/binding/match-unique-bind.rs`** -> AI Confidence: **99.29%**
750. **`tests/ui/binding/match-var-hygiene.rs`** -> AI Confidence: **99.29%**
751. **`tests/ui/binding/match-vec-alternatives.rs`** -> AI Confidence: **99.29%**
752. **`tests/ui/binding/match-vec-rvalue.rs`** -> AI Confidence: **99.29%**
753. **`tests/ui/binding/optional_comma_in_match_arm.rs`** -> AI Confidence: **99.29%**
754. **`tests/ui/binding/pat-tuple-1.rs`** -> AI Confidence: **99.29%**
755. **`tests/ui/binding/pat-tuple-7.rs`** -> AI Confidence: **99.29%**
756. **`tests/ui/binding/range-inclusive-pattern-precedence.rs`** -> AI Confidence: **99.29%**
757. **`tests/ui/binop/can-have-side-effects-consider-operands.rs`** -> AI Confidence: **99.29%**
758. **`tests/ui/block-result/block-must-not-have-result-do.rs`** -> AI Confidence: **99.29%**
759. **`tests/ui/block-result/block-must-not-have-result-while.rs`** -> AI Confidence: **99.29%**
760. **`tests/ui/box/unit/unique-pat.rs`** -> AI Confidence: **99.29%**
761. **`tests/ui/c-variadic/variadic-unreachable-arg-error.rs`** -> AI Confidence: **99.29%**
762. **`tests/ui/cast/cast-to-char-compare.rs`** -> AI Confidence: **99.29%**
763. **`tests/ui/cfg/auxiliary/cfg_inner_static.rs`** -> AI Confidence: **99.29%**
764. **`tests/ui/check-cfg/allow-macro-cfg.rs`** -> AI Confidence: **99.29%**
765. **`tests/ui/check-cfg/allow-top-level.rs`** -> AI Confidence: **99.29%**
766. **`tests/ui/closures/binder/async-closure-with-binder.rs`** -> AI Confidence: **99.29%**
767. **`tests/ui/closures/binder/const-bound.rs`** -> AI Confidence: **99.29%**
768. **`tests/ui/closures/binder/disallow-const.rs`** -> AI Confidence: **99.29%**
769. **`tests/ui/closures/binder/disallow-ty.rs`** -> AI Confidence: **99.29%**
770. **`tests/ui/closures/binder/nested-closures-regions.rs`** -> AI Confidence: **99.29%**
771. **`tests/ui/closures/binder/nested-closures.rs`** -> AI Confidence: **99.29%**
772. **`tests/ui/closures/binder/type-bound-2.rs`** -> AI Confidence: **99.29%**
773. **`tests/ui/closures/binder/type-bound.rs`** -> AI Confidence: **99.29%**
774. **`tests/ui/closures/closure-array-break-length.rs`** -> AI Confidence: **99.29%**
775. **`tests/ui/closures/deeply-nested_closures.rs`** -> AI Confidence: **99.29%**
776. **`tests/ui/closures/issue-1460.rs`** -> AI Confidence: **99.29%**
777. **`tests/ui/closures/issue-48109.rs`** -> AI Confidence: **99.29%**
778. **`tests/ui/closures/issue-52437.rs`** -> AI Confidence: **99.29%**
779. **`tests/ui/closures/issue-67123.rs`** -> AI Confidence: **99.29%**
780. **`tests/ui/closures/issue-90871.rs`** -> AI Confidence: **99.29%**
781. **`tests/ui/closures/issue-99565.rs`** -> AI Confidence: **99.29%**
782. **`tests/ui/closures/nested-closure-call.rs`** -> AI Confidence: **99.29%**
783. **`tests/ui/closures/old-closure-expr-precedence.rs`** -> AI Confidence: **99.29%**
784. **`tests/ui/closures/semistatement-in-lambda.rs`** -> AI Confidence: **99.29%**
785. **`tests/ui/closures/unsized_value_move.rs`** -> AI Confidence: **99.29%**
786. **`tests/ui/const-generics/associated-const-bindings/dyn-const-projection-escaping-bound-vars.rs`** -> AI Confidence: **99.29%**
787. **`tests/ui/const-generics/early/const_arg_trivial_macro_expansion-1.rs`** -> AI Confidence: **99.29%**
788. **`tests/ui/const-generics/early/const_arg_trivial_macro_expansion-3-pass.rs`** -> AI Confidence: **99.29%**
789. **`tests/ui/const-generics/generic-const-array-pattern-ice-139815.rs`** -> AI Confidence: **99.29%**
790. **`tests/ui/const-generics/generic_const_exprs/closures.rs`** -> AI Confidence: **99.29%**
791. **`tests/ui/const-generics/invalid-rustc_legacy_const_generics-issue-123077.rs`** -> AI Confidence: **99.29%**
792. **`tests/ui/consts/closure-structural-match-issue-90013.rs`** -> AI Confidence: **99.29%**
793. **`tests/ui/consts/const-closure-fn-trait-object.rs`** -> AI Confidence: **99.29%**
794. **`tests/ui/consts/const-enum-vec-index.rs`** -> AI Confidence: **99.29%**
795. **`tests/ui/consts/const-eval/const_signed_pat.rs`** -> AI Confidence: **99.29%**
796. **`tests/ui/consts/const-eval/field-access-after-const-eval-fail-in-ty.rs`** -> AI Confidence: **99.29%**
797. **`tests/ui/consts/const-eval/issue-70723.rs`** -> AI Confidence: **99.29%**
798. **`tests/ui/consts/const-eval/issue-70804-fn-subtyping.rs`** -> AI Confidence: **99.29%**
799. **`tests/ui/consts/const-eval/parse_ints.rs`** -> AI Confidence: **99.29%**
800. **`tests/ui/consts/const-eval/stable-metric/ctfe-recursion.rs`** -> AI Confidence: **99.29%**
801. **`tests/ui/consts/const-expr-addr-operator.rs`** -> AI Confidence: **99.29%**
802. **`tests/ui/consts/const-fn-ptr.rs`** -> AI Confidence: **99.29%**
803. **`tests/ui/consts/const-for-feature-gate.rs`** -> AI Confidence: **99.29%**
804. **`tests/ui/consts/const-for.rs`** -> AI Confidence: **99.29%**
805. **`tests/ui/consts/const-labeled-break.rs`** -> AI Confidence: **99.29%**
806. **`tests/ui/consts/const-match-pattern-arm.rs`** -> AI Confidence: **99.29%**
807. **`tests/ui/consts/const-negation.rs`** -> AI Confidence: **99.29%**
808. **`tests/ui/consts/const-static-ref-to-closure.rs`** -> AI Confidence: **99.29%**
809. **`tests/ui/consts/const-try-feature-gate.rs`** -> AI Confidence: **99.29%**
810. **`tests/ui/consts/const_in_pattern/arrays-and-slices.rs`** -> AI Confidence: **99.29%**
811. **`tests/ui/consts/const_in_pattern/issue-34784-match-on-non-int-raw-ptr.rs`** -> AI Confidence: **99.29%**
812. **`tests/ui/consts/const_prop_slice_pat_ice.rs`** -> AI Confidence: **99.29%**
813. **`tests/ui/consts/const_unsafe_unreachable.rs`** -> AI Confidence: **99.29%**
814. **`tests/ui/consts/const_unsafe_unreachable_ub.rs`** -> AI Confidence: **99.29%**
815. **`tests/ui/consts/control-flow/short-circuit.rs`** -> AI Confidence: **99.29%**
816. **`tests/ui/consts/deref_in_pattern.rs`** -> AI Confidence: **99.29%**
817. **`tests/ui/consts/different-fn-ptr-binders-during-ctfe.rs`** -> AI Confidence: **99.29%**
818. **`tests/ui/consts/do-not-ice-long-constant-evaluation-in-for-loop.rs`** -> AI Confidence: **99.29%**
819. **`tests/ui/consts/issue-104155.rs`** -> AI Confidence: **99.29%**
820. **`tests/ui/consts/issue-17074.rs`** -> AI Confidence: **99.29%**
821. **`tests/ui/consts/issue-28113.rs`** -> AI Confidence: **99.29%**
822. **`tests/ui/consts/issue-43105.rs`** -> AI Confidence: **99.29%**
823. **`tests/ui/consts/issue-56164.rs`** -> AI Confidence: **99.29%**
824. **`tests/ui/consts/issue-96169.rs`** -> AI Confidence: **99.29%**
825. **`tests/ui/consts/issue-broken-mir.rs`** -> AI Confidence: **99.29%**
826. **`tests/ui/consts/min_const_fn/allow_const_fn_ptr_run_pass.rs`** -> AI Confidence: **99.29%**
827. **`tests/ui/consts/min_const_fn/cast_fn.rs`** -> AI Confidence: **99.29%**
828. **`tests/ui/consts/miri_unleashed/const_refers_to_static_cross_crate.rs`** -> AI Confidence: **99.29%**
829. **`tests/ui/consts/nested_erroneous_ctfe.rs`** -> AI Confidence: **99.29%**
830. **`tests/ui/consts/precise-drop-allow-const-fn-unstable.rs`** -> AI Confidence: **99.29%**
831. **`tests/ui/consts/precise-drop-with-coverage.rs`** -> AI Confidence: **99.29%**
832. **`tests/ui/consts/repeat_match.rs`** -> AI Confidence: **99.29%**
833. **`tests/ui/consts/transmute-size-mismatch-before-typeck.rs`** -> AI Confidence: **99.29%**
834. **`tests/ui/consts/try-operator.rs`** -> AI Confidence: **99.29%**
835. **`tests/ui/consts/value-suggestion-ice-123906.rs`** -> AI Confidence: **99.29%**
836. **`tests/ui/contracts/internal_machinery/internal-feature-gating.rs`** -> AI Confidence: **99.29%**
837. **`tests/ui/delegation/generics/const-type-ice-153433.rs`** -> AI Confidence: **99.29%**
838. **`tests/ui/deref-patterns/deref-non-pointer.rs`** -> AI Confidence: **99.29%**
839. **`tests/ui/deref/deref-in-for-loop.rs`** -> AI Confidence: **99.29%**
840. **`tests/ui/did_you_mean/bad-assoc-pat.rs`** -> AI Confidence: **99.29%**
841. **`tests/ui/did_you_mean/brackets-to-braces-single-element.rs`** -> AI Confidence: **99.29%**
842. **`tests/ui/enum-discriminant/discr-foreign.rs`** -> AI Confidence: **99.29%**
843. **`tests/ui/error-codes/E0030-teach.rs`** -> AI Confidence: **99.29%**
844. **`tests/ui/error-codes/E0030.rs`** -> AI Confidence: **99.29%**
845. **`tests/ui/error-codes/E0268.rs`** -> AI Confidence: **99.29%**
846. **`tests/ui/error-codes/E0416.rs`** -> AI Confidence: **99.29%**
847. **`tests/ui/error-codes/E0426.rs`** -> AI Confidence: **99.29%**
848. **`tests/ui/error-codes/E0522.rs`** -> AI Confidence: **99.29%**
849. **`tests/ui/error-codes/E0730.rs`** -> AI Confidence: **99.29%**
850. **`tests/ui/error-codes/E0767.rs`** -> AI Confidence: **99.29%**
851. **`tests/ui/explicit-tail-calls/become-macro.rs`** -> AI Confidence: **99.29%**
852. **`tests/ui/explicit-tail-calls/caller-lifetime-presence.rs`** -> AI Confidence: **99.29%**
853. **`tests/ui/explicit-tail-calls/constck.rs`** -> AI Confidence: **99.29%**
854. **`tests/ui/explicit-tail-calls/in-closure.rs`** -> AI Confidence: **99.29%**
855. **`tests/ui/explicit-tail-calls/ret-ty-hr-mismatch.rs`** -> AI Confidence: **99.29%**
856. **`tests/ui/explicit-tail-calls/ret-ty-modulo-anonymization.rs`** -> AI Confidence: **99.29%**
857. **`tests/ui/expr/if-panic-all.rs`** -> AI Confidence: **99.29%**
858. **`tests/ui/expr/if/attrs/else-attrs.rs`** -> AI Confidence: **99.29%**
859. **`tests/ui/expr/if/attrs/gate-whole-expr.rs`** -> AI Confidence: **99.29%**
860. **`tests/ui/expr/if/attrs/stmt-expr-gated.rs`** -> AI Confidence: **99.29%**
861. **`tests/ui/expr/if/bad-if-let-suggestion.rs`** -> AI Confidence: **99.29%**
862. **`tests/ui/expr/if/expr-if-panic.rs`** -> AI Confidence: **99.29%**
863. **`tests/ui/expr/if/expr-stack-overflow.rs`** -> AI Confidence: **99.29%**
864. **`tests/ui/expr/if/if-cond-bot.rs`** -> AI Confidence: **99.29%**
865. **`tests/ui/expr/if/if-loop.rs`** -> AI Confidence: **99.29%**
866. **`tests/ui/expr/if/if-typeck.rs`** -> AI Confidence: **99.29%**
867. **`tests/ui/extern/bad-external-async-fn-issue-146754.rs`** -> AI Confidence: **99.29%**
868. **`tests/ui/feature-gates/feature-gate-closure_lifetime_binder.rs`** -> AI Confidence: **99.29%**
869. **`tests/ui/feature-gates/feature-gate-precise_pointer_size_matching.rs`** -> AI Confidence: **99.29%**
870. **`tests/ui/float/target-has-reliable-nightly-float.rs`** -> AI Confidence: **99.29%**
871. **`tests/ui/fmt/ifmt-bad-format-args.rs`** -> AI Confidence: **99.29%**
872. **`tests/ui/fn/issue-80179.rs`** -> AI Confidence: **99.29%**
873. **`tests/ui/for-loop-while/break-continue-in-loop-while-condition.rs`** -> AI Confidence: **99.29%**
874. **`tests/ui/for-loop-while/break-outside-loop.rs`** -> AI Confidence: **99.29%**
875. **`tests/ui/for-loop-while/break.rs`** -> AI Confidence: **99.29%**
876. **`tests/ui/for-loop-while/cleanup-rvalue-during-if-and-while.rs`** -> AI Confidence: **99.29%**
877. **`tests/ui/for-loop-while/for-else-err.rs`** -> AI Confidence: **99.29%**
878. **`tests/ui/for-loop-while/for-loop-diagnostic-span.rs`** -> AI Confidence: **99.29%**
879. **`tests/ui/for-loop-while/for-loop-has-unit-body.rs`** -> AI Confidence: **99.29%**
880. **`tests/ui/for-loop-while/for-loop-refutable-pattern-error-message.rs`** -> AI Confidence: **99.29%**
881. **`tests/ui/for-loop-while/for-loop-unconstrained-element-type.rs`** -> AI Confidence: **99.29%**
882. **`tests/ui/for-loop-while/issue-2216.rs`** -> AI Confidence: **99.29%**
883. **`tests/ui/for-loop-while/labeled-break.rs`** -> AI Confidence: **99.29%**
884. **`tests/ui/for-loop-while/loop-diverges.rs`** -> AI Confidence: **99.29%**
885. **`tests/ui/for-loop-while/while-else-err.rs`** -> AI Confidence: **99.29%**
886. **`tests/ui/force-inlining/deny-closure.rs`** -> AI Confidence: **99.29%**
887. **`tests/ui/function-pointer/sized-ret-with-binder.rs`** -> AI Confidence: **99.29%**
888. **`tests/ui/generic-const-items/reference-outlives-referent.rs`** -> AI Confidence: **99.29%**
889. **`tests/ui/generic-const-items/user_type_annotations_pattern.rs`** -> AI Confidence: **99.29%**
890. **`tests/ui/half-open-range-patterns/exclusive_range_pattern_syntax_collision.rs`** -> AI Confidence: **99.29%**
891. **`tests/ui/half-open-range-patterns/exclusive_range_pattern_syntax_collision2.rs`** -> AI Confidence: **99.29%**
892. **`tests/ui/half-open-range-patterns/exclusive_range_pattern_syntax_collision3.rs`** -> AI Confidence: **99.29%**
893. **`tests/ui/half-open-range-patterns/half-open-range-pats-exhaustive-pass.rs`** -> AI Confidence: **99.29%**
894. **`tests/ui/half-open-range-patterns/half-open-range-pats-ref-ambiguous-interp.rs`** -> AI Confidence: **99.29%**
895. **`tests/ui/half-open-range-patterns/half-open-range-pats-syntactic-pass.rs`** -> AI Confidence: **99.29%**
896. **`tests/ui/half-open-range-patterns/half-open-range-pats-thir-lower-empty.rs`** -> AI Confidence: **99.29%**
897. **`tests/ui/half-open-range-patterns/pat-tuple-4.rs`** -> AI Confidence: **99.29%**
898. **`tests/ui/half-open-range-patterns/pat-tuple-5.rs`** -> AI Confidence: **99.29%**
899. **`tests/ui/higher-ranked/subtype/hr-subtype.rs`** -> AI Confidence: **99.29%**
900. **`tests/ui/higher-ranked/trait-bounds/hrtb-parse.rs`** -> AI Confidence: **99.29%**
901. **`tests/ui/higher-ranked/trait-bounds/issue-59311.rs`** -> AI Confidence: **99.29%**
902. **`tests/ui/hygiene/duplicate_lifetimes.rs`** -> AI Confidence: **99.29%**
903. **`tests/ui/hygiene/for-loop.rs`** -> AI Confidence: **99.29%**
904. **`tests/ui/hygiene/hygienic-label-2.rs`** -> AI Confidence: **99.29%**
905. **`tests/ui/hygiene/hygienic-label-4.rs`** -> AI Confidence: **99.29%**
906. **`tests/ui/hygiene/hygienic-labels.rs`** -> AI Confidence: **99.29%**
907. **`tests/ui/impl-trait/member-constraints/min-choice.rs`** -> AI Confidence: **99.29%**
908. **`tests/ui/inference/newlambdas-ret-infer2.rs`** -> AI Confidence: **99.29%**
909. **`tests/ui/inline-const/break-inside-inline-const-issue-128604.rs`** -> AI Confidence: **99.29%**
910. **`tests/ui/inline-const/expr-with-block.rs`** -> AI Confidence: **99.29%**
911. **`tests/ui/inline-const/in-pat-recovery.rs`** -> AI Confidence: **99.29%**
912. **`tests/ui/inline-const/required-const.rs`** -> AI Confidence: **99.29%**
913. **`tests/ui/issues/issue-18711.rs`** -> AI Confidence: **99.29%**
914. **`tests/ui/issues/issue-18845.rs`** -> AI Confidence: **99.29%**
915. **`tests/ui/issues/issue-23311.rs`** -> AI Confidence: **99.29%**
916. **`tests/ui/issues/issue-25343.rs`** -> AI Confidence: **99.29%**
917. **`tests/ui/issues/issue-29071.rs`** -> AI Confidence: **99.29%**
918. **`tests/ui/issues/issue-30891.rs`** -> AI Confidence: **99.29%**
919. **`tests/ui/issues/issue-3574.rs`** -> AI Confidence: **99.29%**
920. **`tests/ui/issues/issue-39848.rs`** -> AI Confidence: **99.29%**
921. **`tests/ui/issues/issue-46311.rs`** -> AI Confidence: **99.29%**
922. **`tests/ui/issues/issue-5067.rs`** -> AI Confidence: **99.29%**
923. **`tests/ui/issues/issue-51655.rs`** -> AI Confidence: **99.29%**
924. **`tests/ui/iterators/float_iterator_hint.rs`** -> AI Confidence: **99.29%**
925. **`tests/ui/iterators/integral.rs`** -> AI Confidence: **99.29%**
926. **`tests/ui/iterators/ranges.rs`** -> AI Confidence: **99.29%**
927. **`tests/ui/label/continue-pointing-to-block-ice-113379.rs`** -> AI Confidence: **99.29%**
928. **`tests/ui/label/continue-pointing-to-block-ice-121623.rs`** -> AI Confidence: **99.29%**
929. **`tests/ui/label/label-beginning-with-underscore.rs`** -> AI Confidence: **99.29%**
930. **`tests/ui/label/label_break_value_continue.rs`** -> AI Confidence: **99.29%**
931. **`tests/ui/label/label_break_value_illegal_uses.rs`** -> AI Confidence: **99.29%**
932. **`tests/ui/label/label_break_value_unlabeled_break.rs`** -> AI Confidence: **99.29%**
933. **`tests/ui/label/label_misspelled.rs`** -> AI Confidence: **99.29%**
934. **`tests/ui/label/label_misspelled_2.rs`** -> AI Confidence: **99.29%**
935. **`tests/ui/lang-items/lang-item-missing.rs`** -> AI Confidence: **99.29%**
936. **`tests/ui/lang-items/lang-item-unknown-definition-error.rs`** -> AI Confidence: **99.29%**
937. **`tests/ui/late-bound-lifetimes/cross_crate_alias.rs`** -> AI Confidence: **99.29%**
938. **`tests/ui/lifetimes/closure-lifetime-bounds-10291.rs`** -> AI Confidence: **99.29%**
939. **`tests/ui/lifetimes/issue-67498.rs`** -> AI Confidence: **99.29%**
940. **`tests/ui/lifetimes/lifetime-bound-will-change-warning.rs`** -> AI Confidence: **99.29%**
941. **`tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else-2.rs`** -> AI Confidence: **99.29%**
942. **`tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else-3.rs`** -> AI Confidence: **99.29%**
943. **`tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-if-else.rs`** -> AI Confidence: **99.29%**
944. **`tests/ui/lifetimes/lifetime-errors/ex1b-return-no-names-if-else.rs`** -> AI Confidence: **99.29%**
945. **`tests/ui/linking/executable-no-mangle-strip.rs`** -> AI Confidence: **99.29%**
946. **`tests/ui/lint/break-with-label-and-unsafe-block.rs`** -> AI Confidence: **99.29%**
947. **`tests/ui/lint/for-loops-over-fallibles/auxiliary/external-macro-issue-148114.rs`** -> AI Confidence: **99.29%**
948. **`tests/ui/lint/for-loops-over-fallibles/macro-issue-140747.rs`** -> AI Confidence: **99.29%**
949. **`tests/ui/lint/for-loops-over-fallibles/macro-iterator-next.rs`** -> AI Confidence: **99.29%**
950. **`tests/ui/lint/for_loop_over_fallibles.rs`** -> AI Confidence: **99.29%**
951. **`tests/ui/lint/issue-103435-extra-parentheses.rs`** -> AI Confidence: **99.29%**
952. **`tests/ui/lint/issue-109529.rs`** -> AI Confidence: **99.29%**
953. **`tests/ui/lint/lint-attr-non-item-node.rs`** -> AI Confidence: **99.29%**
954. **`tests/ui/lint/lint-change-warnings.rs`** -> AI Confidence: **99.29%**
955. **`tests/ui/lint/lint-match-arms.rs`** -> AI Confidence: **99.29%**
956. **`tests/ui/lint/lint-unconditional-recursion-tail-calls.rs`** -> AI Confidence: **99.29%**
957. **`tests/ui/lint/reasons-erroneous.rs`** -> AI Confidence: **99.29%**
958. **`tests/ui/lint/rfc-2383-lint-reason/expect_with_forbid.rs`** -> AI Confidence: **99.29%**
959. **`tests/ui/lint/rfc-2383-lint-reason/lint-attribute-only-with-reason.rs`** -> AI Confidence: **99.29%**
960. **`tests/ui/lint/rfc-2383-lint-reason/no_ice_for_partial_compiler_runs.rs`** -> AI Confidence: **99.29%**
961. **`tests/ui/lint/unaligned_references_fake_borrow.rs`** -> AI Confidence: **99.29%**
962. **`tests/ui/lint/unused-parens-labeled-break-issue-143256.rs`** -> AI Confidence: **99.29%**
963. **`tests/ui/lint/unused/break-label-with-parens-147542.rs`** -> AI Confidence: **99.29%**
964. **`tests/ui/lint/unused/issue-71290-unused-paren-binop.rs`** -> AI Confidence: **99.29%**
965. **`tests/ui/lint/unused/issue-88519-unused-paren.rs`** -> AI Confidence: **99.29%**
966. **`tests/ui/lint/unused/issue-90807-unused-paren-error.rs`** -> AI Confidence: **99.29%**
967. **`tests/ui/lint/unused/issue-90807-unused-paren.rs`** -> AI Confidence: **99.29%**
968. **`tests/ui/lint/unused/issue-92751.rs`** -> AI Confidence: **99.29%**
969. **`tests/ui/lint/unused/match_with_guard.rs`** -> AI Confidence: **99.29%**
970. **`tests/ui/lint/unused_labels.rs`** -> AI Confidence: **99.29%**
971. **`tests/ui/lint/unused_parens_remove_json_suggestion.rs`** -> AI Confidence: **99.29%**
972. **`tests/ui/liveness/liveness-missing-ret2.rs`** -> AI Confidence: **99.29%**
973. **`tests/ui/loop-match/const-continue-to-block.rs`** -> AI Confidence: **99.29%**
974. **`tests/ui/loops/for-each-loop-panic.rs`** -> AI Confidence: **99.29%**
975. **`tests/ui/loops/infinite-loop-simplify-cfg-75704.rs`** -> AI Confidence: **99.29%**
976. **`tests/ui/loops/issue-43162.rs`** -> AI Confidence: **99.29%**
977. **`tests/ui/loops/issue-50576.rs`** -> AI Confidence: **99.29%**
978. **`tests/ui/loops/label-on-block-suggest-move.rs`** -> AI Confidence: **99.29%**
979. **`tests/ui/loops/loop-break-value.rs`** -> AI Confidence: **99.29%**
980. **`tests/ui/loops/loop-else-err.rs`** -> AI Confidence: **99.29%**
981. **`tests/ui/lowering/issue-96847.rs`** -> AI Confidence: **99.29%**
982. **`tests/ui/lub-glb/old-lub-glb-hr-noteq1.rs`** -> AI Confidence: **99.29%**
983. **`tests/ui/lub-glb/old-lub-glb-hr-noteq2.rs`** -> AI Confidence: **99.29%**
984. **`tests/ui/macros/assert-ne-no-invalid-help-issue-146204.rs`** -> AI Confidence: **99.29%**
985. **`tests/ui/macros/assert-trailing-junk.rs`** -> AI Confidence: **99.29%**
986. **`tests/ui/macros/auxiliary/foreign-crate-macro-pat.rs`** -> AI Confidence: **99.29%**
987. **`tests/ui/macros/concat-rpass.rs`** -> AI Confidence: **99.29%**
988. **`tests/ui/macros/issue-112342-1.rs`** -> AI Confidence: **99.29%**
989. **`tests/ui/macros/issue-16098.rs`** -> AI Confidence: **99.29%**
990. **`tests/ui/macros/issue-57597.rs`** -> AI Confidence: **99.29%**
991. **`tests/ui/macros/issue-70446.rs`** -> AI Confidence: **99.29%**
992. **`tests/ui/macros/macro-at-most-once-rep-2015.rs`** -> AI Confidence: **99.29%**
993. **`tests/ui/macros/macro-at-most-once-rep-2018.rs`** -> AI Confidence: **99.29%**
994. **`tests/ui/macros/macro-expansion-empty-span-147408.rs`** -> AI Confidence: **99.29%**
995. **`tests/ui/macros/macro-follow.rs`** -> AI Confidence: **99.29%**
996. **`tests/ui/macros/macro-in-expression-context-2.rs`** -> AI Confidence: **99.29%**
997. **`tests/ui/macros/macro-in-or-pattern.rs`** -> AI Confidence: **99.29%**
998. **`tests/ui/macros/macro-lifetime-used-with-labels.rs`** -> AI Confidence: **99.29%**
999. **`tests/ui/macros/macro-pat-follow-2018.rs`** -> AI Confidence: **99.29%**
1000. **`tests/ui/macros/macro-pat.rs`** -> AI Confidence: **99.29%**
1001. **`tests/ui/macros/metavar-expressions/concat-repetitions.rs`** -> AI Confidence: **99.29%**
1002. **`tests/ui/macros/no-close-delim-issue-139248.rs`** -> AI Confidence: **99.29%**
1003. **`tests/ui/macros/remove-repetition-issue-139480.rs`** -> AI Confidence: **99.29%**
1004. **`tests/ui/macros/syntax-extension-cfg.rs`** -> AI Confidence: **99.29%**
1005. **`tests/ui/macros/trace_macros-format.rs`** -> AI Confidence: **99.29%**
1006. **`tests/ui/macros/vec-macro-in-pattern.rs`** -> AI Confidence: **99.29%**
1007. **`tests/ui/match/closure-in-match-guard.rs`** -> AI Confidence: **99.29%**
1008. **`tests/ui/match/const_non_normal_zst_ref_pattern.rs`** -> AI Confidence: **99.29%**
1009. **`tests/ui/match/expr_before_ident_pat.rs`** -> AI Confidence: **99.29%**
1010. **`tests/ui/match/intended-binding-pattern-is-const.rs`** -> AI Confidence: **99.29%**
1011. **`tests/ui/match/issue-11319.rs`** -> AI Confidence: **99.29%**
1012. **`tests/ui/match/issue-18060.rs`** -> AI Confidence: **99.29%**
1013. **`tests/ui/match/issue-46920-byte-array-patterns.rs`** -> AI Confidence: **99.29%**
1014. **`tests/ui/match/issue-72680.rs`** -> AI Confidence: **99.29%**
1015. **`tests/ui/match/issue-82866.rs`** -> AI Confidence: **99.29%**
1016. **`tests/ui/match/issue-92100.rs`** -> AI Confidence: **99.29%**
1017. **`tests/ui/match/match-const-tuple-type-mismatch.rs`** -> AI Confidence: **99.29%**
1018. **`tests/ui/match/match-disc-bot.rs`** -> AI Confidence: **99.29%**
1019. **`tests/ui/match/match-ill-type2.rs`** -> AI Confidence: **99.29%**
1020. **`tests/ui/match/match-large-array.rs`** -> AI Confidence: **99.29%**
1021. **`tests/ui/match/match-option-result-mismatch.rs`** -> AI Confidence: **99.29%**
1022. **`tests/ui/match/match-range-char-const.rs`** -> AI Confidence: **99.29%**
1023. **`tests/ui/match/match-range-fail-2.rs`** -> AI Confidence: **99.29%**
1024. **`tests/ui/match/match-range-fail.rs`** -> AI Confidence: **99.29%**
1025. **`tests/ui/match/match-static-pattern.rs`** -> AI Confidence: **99.29%**
1026. **`tests/ui/match/match-tail-expr-never-type-error.rs`** -> AI Confidence: **99.29%**
1027. **`tests/ui/match/match-usize-min-max-pattern.rs`** -> AI Confidence: **99.29%**
1028. **`tests/ui/match/match-vec-mismatch-2.rs`** -> AI Confidence: **99.29%**
1029. **`tests/ui/match/match-wildcards.rs`** -> AI Confidence: **99.29%**
1030. **`tests/ui/match/overeager-sub-match-pruning-13027.rs`** -> AI Confidence: **99.29%**
1031. **`tests/ui/match/pattern-deref-miscompile.rs`** -> AI Confidence: **99.29%**
1032. **`tests/ui/match/postfix-match/match-after-as.rs`** -> AI Confidence: **99.29%**
1033. **`tests/ui/match/postfix-match/no-unused-parens.rs`** -> AI Confidence: **99.29%**
1034. **`tests/ui/match/postfix-match/pf-match-chain.rs`** -> AI Confidence: **99.29%**
1035. **`tests/ui/match/postfix-match/pf-match-exhaustiveness.rs`** -> AI Confidence: **99.29%**
1036. **`tests/ui/match/postfix-match/pf-match-types.rs`** -> AI Confidence: **99.29%**
1037. **`tests/ui/match/tuple-usize-pattern-14393.rs`** -> AI Confidence: **99.29%**
1038. **`tests/ui/match/validate-range-endpoints.rs`** -> AI Confidence: **99.29%**
1039. **`tests/ui/methods/method-call-lifetime-args-lint-fail.rs`** -> AI Confidence: **99.29%**
1040. **`tests/ui/mir/mir-cfg-unpretty-no-panic-81918.rs`** -> AI Confidence: **99.29%**
1041. **`tests/ui/mir/mir_codegen_switchint.rs`** -> AI Confidence: **99.29%**
1042. **`tests/ui/mir/mir_match_arm_guard.rs`** -> AI Confidence: **99.29%**
1043. **`tests/ui/mir/mir_temp_promotions.rs`** -> AI Confidence: **99.29%**
1044. **`tests/ui/mir/unreachable-loop-jump-threading.rs`** -> AI Confidence: **99.29%**
1045. **`tests/ui/mismatched_types/array-len-is-closure.rs`** -> AI Confidence: **99.29%**
1046. **`tests/ui/mismatched_types/dont-point-return-on-E0308.rs`** -> AI Confidence: **99.29%**
1047. **`tests/ui/mismatched_types/for-loop-has-unit-body.rs`** -> AI Confidence: **99.29%**
1048. **`tests/ui/mismatched_types/for-loop-in-vec-type-mismatchrs-50585.rs`** -> AI Confidence: **99.29%**
1049. **`tests/ui/mismatched_types/issue-38371-unfixable.rs`** -> AI Confidence: **99.29%**
1050. **`tests/ui/mismatched_types/mismatched-types-issue-126222.rs`** -> AI Confidence: **99.29%**
1051. **`tests/ui/missing/missing-allocator.rs`** -> AI Confidence: **99.29%**
1052. **`tests/ui/missing/missing-block-hint.rs`** -> AI Confidence: **99.29%**
1053. **`tests/ui/missing/missing-comma-in-match.rs`** -> AI Confidence: **99.29%**
1054. **`tests/ui/never_type/fallback_change/lint-breaking-2024-assign-underscore.rs`** -> AI Confidence: **99.29%**
1055. **`tests/ui/never_type/regress/loop-in-array-length.rs`** -> AI Confidence: **99.29%**
1056. **`tests/ui/never_type/regress/malformed-range-to-never.rs`** -> AI Confidence: **99.29%**
1057. **`tests/ui/never_type/regress/never-as-function-argument.rs`** -> AI Confidence: **99.29%**
1058. **`tests/ui/never_type/regress/never-type-method-call-15207.rs`** -> AI Confidence: **99.29%**
1059. **`tests/ui/nll/issue-98589-closures-relate-named-regions.rs`** -> AI Confidence: **99.29%**
1060. **`tests/ui/no_std/no-std-no-start-binary.rs`** -> AI Confidence: **99.29%**
1061. **`tests/ui/no_std/no-std-unwind-binary.rs`** -> AI Confidence: **99.29%**
1062. **`tests/ui/numbers-arithmetic/float.rs`** -> AI Confidence: **99.29%**
1063. **`tests/ui/numbers-arithmetic/int-abs-overflow.rs`** -> AI Confidence: **99.29%**
1064. **`tests/ui/numbers-arithmetic/next-power-of-two-overflow-ndebug.rs`** -> AI Confidence: **99.29%**
1065. **`tests/ui/or-patterns/bindings-runpass-1.rs`** -> AI Confidence: **99.29%**
1066. **`tests/ui/or-patterns/bindings-runpass-2.rs`** -> AI Confidence: **99.29%**
1067. **`tests/ui/or-patterns/exhaustiveness-non-exhaustive.rs`** -> AI Confidence: **99.29%**
1068. **`tests/ui/or-patterns/exhaustiveness-pass.rs`** -> AI Confidence: **99.29%**
1069. **`tests/ui/or-patterns/exhaustiveness-unreachable-pattern.rs`** -> AI Confidence: **99.29%**
1070. **`tests/ui/or-patterns/issue-70413-no-unreachable-pat-and-guard.rs`** -> AI Confidence: **99.29%**
1071. **`tests/ui/or-patterns/mix-with-wild.rs`** -> AI Confidence: **99.29%**
1072. **`tests/ui/or-patterns/multiple-pattern-typo.rs`** -> AI Confidence: **99.29%**
1073. **`tests/ui/or-patterns/simplification_subtleties.rs`** -> AI Confidence: **99.29%**
1074. **`tests/ui/or-patterns/while-parsing-this-or-pattern.rs`** -> AI Confidence: **99.29%**
1075. **`tests/ui/panic-handler/weak-lang-item-2.rs`** -> AI Confidence: **99.29%**
1076. **`tests/ui/panics/panic-handler-closures.rs`** -> AI Confidence: **99.29%**
1077. **`tests/ui/panics/panic-parens.rs`** -> AI Confidence: **99.29%**
1078. **`tests/ui/panics/short-ice-remove-middle-frames-2.rs`** -> AI Confidence: **99.29%**
1079. **`tests/ui/panics/short-ice-remove-middle-frames.rs`** -> AI Confidence: **99.29%**
1080. **`tests/ui/panics/while-panic.rs`** -> AI Confidence: **99.29%**
1081. **`tests/ui/parser/assoc/assoc-oddities-1.rs`** -> AI Confidence: **99.29%**
1082. **`tests/ui/parser/assoc/assoc-oddities-2.rs`** -> AI Confidence: **99.29%**
1083. **`tests/ui/parser/attribute/attr-incomplete.rs`** -> AI Confidence: **99.29%**
1084. **`tests/ui/parser/bad-if-statements.rs`** -> AI Confidence: **99.29%**
1085. **`tests/ui/parser/break-in-unlabeled-block.rs`** -> AI Confidence: **99.29%**
1086. **`tests/ui/parser/doc-comment-in-if-statement.rs`** -> AI Confidence: **99.29%**
1087. **`tests/ui/parser/else-no-if.rs`** -> AI Confidence: **99.29%**
1088. **`tests/ui/parser/expr-as-stmt-2.rs`** -> AI Confidence: **99.29%**
1089. **`tests/ui/parser/expr-as-stmt.rs`** -> AI Confidence: **99.29%**
1090. **`tests/ui/parser/fn-returns-fn-pointer.rs`** -> AI Confidence: **99.29%**
1091. **`tests/ui/parser/generic-param-default-in-binder.rs`** -> AI Confidence: **99.29%**
1092. **`tests/ui/parser/if-in-in.rs`** -> AI Confidence: **99.29%**
1093. **`tests/ui/parser/issues/issue-103381.rs`** -> AI Confidence: **99.29%**
1094. **`tests/ui/parser/issues/issue-13483.rs`** -> AI Confidence: **99.29%**
1095. **`tests/ui/parser/issues/issue-33262.rs`** -> AI Confidence: **99.29%**
1096. **`tests/ui/parser/issues/issue-51602.rs`** -> AI Confidence: **99.29%**
1097. **`tests/ui/parser/issues/issue-61858.rs`** -> AI Confidence: **99.29%**
1098. **`tests/ui/parser/issues/issue-62973.rs`** -> AI Confidence: **99.29%**
1099. **`tests/ui/parser/issues/issue-68091-unicode-ident-after-if.rs`** -> AI Confidence: **99.29%**
1100. **`tests/ui/parser/issues/issue-7222.rs`** -> AI Confidence: **99.29%**
1101. **`tests/ui/parser/issues/issue-84148-1.rs`** -> AI Confidence: **99.29%**
1102. **`tests/ui/parser/issues/issue-84148-2.rs`** -> AI Confidence: **99.29%**
1103. **`tests/ui/parser/issues/issue-88770.rs`** -> AI Confidence: **99.29%**
1104. **`tests/ui/parser/issues/issue-98601-delimiter-error-1.rs`** -> AI Confidence: **99.29%**
1105. **`tests/ui/parser/label-is-actually-char.rs`** -> AI Confidence: **99.29%**
1106. **`tests/ui/parser/labeled-no-colon-expr.rs`** -> AI Confidence: **99.29%**
1107. **`tests/ui/parser/lifetime_starts_expressions.rs`** -> AI Confidence: **99.29%**
1108. **`tests/ui/parser/macro/break-in-unlabeled-block-in-macro.rs`** -> AI Confidence: **99.29%**
1109. **`tests/ui/parser/macro/macro-incomplete-parse.rs`** -> AI Confidence: **99.29%**
1110. **`tests/ui/parser/macro/trailing-question-in-macro-type.rs`** -> AI Confidence: **99.29%**
1111. **`tests/ui/parser/missing-expression-in-for-loop.rs`** -> AI Confidence: **99.29%**
1112. **`tests/ui/parser/pat-lt-bracket-1.rs`** -> AI Confidence: **99.29%**
1113. **`tests/ui/parser/pat-tuple-1.rs`** -> AI Confidence: **99.29%**
1114. **`tests/ui/parser/pat-tuple-2.rs`** -> AI Confidence: **99.29%**
1115. **`tests/ui/parser/pat-tuple-3.rs`** -> AI Confidence: **99.29%**
1116. **`tests/ui/parser/pattern-matching-with-double-references-61475.rs`** -> AI Confidence: **99.29%**
1117. **`tests/ui/parser/range_inclusive.rs`** -> AI Confidence: **99.29%**
1118. **`tests/ui/parser/recover/recover-labeled-non-block-expr.rs`** -> AI Confidence: **99.29%**
1119. **`tests/ui/parser/recover/recover-pat-ranges.rs`** -> AI Confidence: **99.29%**
1120. **`tests/ui/parser/recover/recover-pat-wildcards.rs`** -> AI Confidence: **99.29%**
1121. **`tests/ui/parser/recover/recover-unticked-labels.rs`** -> AI Confidence: **99.29%**
1122. **`tests/ui/parser/type-ascription-in-pattern.rs`** -> AI Confidence: **99.29%**
1123. **`tests/ui/pattern/box-pattern-constructor-mismatch.rs`** -> AI Confidence: **99.29%**
1124. **`tests/ui/pattern/const-pattern-str-match-lifetime.rs`** -> AI Confidence: **99.29%**
1125. **`tests/ui/pattern/deref-patterns/basic.rs`** -> AI Confidence: **99.29%**
1126. **`tests/ui/pattern/deref-patterns/default-infer.rs`** -> AI Confidence: **99.29%**
1127. **`tests/ui/pattern/deref-patterns/dont-ice-on-slice-in-deref-pat-in-closure.rs`** -> AI Confidence: **99.29%**
1128. **`tests/ui/pattern/deref-patterns/implicit-const-deref.rs`** -> AI Confidence: **99.29%**
1129. **`tests/ui/pattern/deref-patterns/refs.rs`** -> AI Confidence: **99.29%**
1130. **`tests/ui/pattern/deref-patterns/typeck_fail.rs`** -> AI Confidence: **99.29%**
1131. **`tests/ui/pattern/deref-patterns/usefulness/mixed-constructors.rs`** -> AI Confidence: **99.29%**
1132. **`tests/ui/pattern/deref-patterns/usefulness/non-exhaustive.rs`** -> AI Confidence: **99.29%**
1133. **`tests/ui/pattern/deref-patterns/usefulness/unreachable-patterns.rs`** -> AI Confidence: **99.29%**
1134. **`tests/ui/pattern/inc-range-pat.rs`** -> AI Confidence: **99.29%**
1135. **`tests/ui/pattern/issue-6449.rs`** -> AI Confidence: **99.29%**
1136. **`tests/ui/pattern/match-at-pattern-shadows-name.rs`** -> AI Confidence: **99.29%**
1137. **`tests/ui/pattern/pat-tuple-field-count-cross.rs`** -> AI Confidence: **99.29%**
1138. **`tests/ui/pattern/pattern-ident-path-generics.rs`** -> AI Confidence: **99.29%**
1139. **`tests/ui/pattern/premature-match-scrutinee-temporary-drop-10683.rs`** -> AI Confidence: **99.29%**
1140. **`tests/ui/pattern/range-pattern-meant-to-be-slice-rest-pattern.rs`** -> AI Confidence: **99.29%**
1141. **`tests/ui/pattern/rfc-3637-guard-patterns/macro-rules.rs`** -> AI Confidence: **99.29%**
1142. **`tests/ui/pattern/rfc-3637-guard-patterns/name-resolution.rs`** -> AI Confidence: **99.29%**
1143. **`tests/ui/pattern/rfc-3637-guard-patterns/only-resolve-top-level-guard-expr-once-ice-141265.rs`** -> AI Confidence: **99.29%**
1144. **`tests/ui/pattern/suggest-adding-appropriate-missing-pattern-excluding-comments.rs`** -> AI Confidence: **99.29%**
1145. **`tests/ui/pattern/usefulness/const-pat-ice.rs`** -> AI Confidence: **99.29%**
1146. **`tests/ui/pattern/usefulness/empty-match-check-notes.rs`** -> AI Confidence: **99.29%**
1147. **`tests/ui/pattern/usefulness/floats.rs`** -> AI Confidence: **99.29%**
1148. **`tests/ui/pattern/usefulness/guards.rs`** -> AI Confidence: **99.29%**
1149. **`tests/ui/pattern/usefulness/integer-ranges/gap_between_ranges.rs`** -> AI Confidence: **99.29%**
1150. **`tests/ui/pattern/usefulness/integer-ranges/issue-117648-overlapping_range_endpoints-false-positive.rs`** -> AI Confidence: **99.29%**
1151. **`tests/ui/pattern/usefulness/integer-ranges/overlapping_range_endpoints.rs`** -> AI Confidence: **99.29%**
1152. **`tests/ui/pattern/usefulness/integer-ranges/pointer-sized-int.rs`** -> AI Confidence: **99.29%**
1153. **`tests/ui/pattern/usefulness/integer-ranges/precise_pointer_matching-message.rs`** -> AI Confidence: **99.29%**
1154. **`tests/ui/pattern/usefulness/integer-ranges/reachability.rs`** -> AI Confidence: **99.29%**
1155. **`tests/ui/pattern/usefulness/integer-ranges/regression-switchint-sorting-with-ranges.rs`** -> AI Confidence: **99.29%**
1156. **`tests/ui/pattern/usefulness/issue-13727.rs`** -> AI Confidence: **99.29%**
1157. **`tests/ui/pattern/usefulness/issue-2111.rs`** -> AI Confidence: **99.29%**
1158. **`tests/ui/pattern/usefulness/issue-3096-1.rs`** -> AI Confidence: **99.29%**
1159. **`tests/ui/pattern/usefulness/issue-66501.rs`** -> AI Confidence: **99.29%**
1160. **`tests/ui/pattern/usefulness/issue-71930-type-of-match-scrutinee.rs`** -> AI Confidence: **99.29%**
1161. **`tests/ui/pattern/usefulness/issue-78549-ref-pat-and-str.rs`** -> AI Confidence: **99.29%**
1162. **`tests/ui/pattern/usefulness/issue-85222-types-containing-non-exhaustive-types.rs`** -> AI Confidence: **99.29%**
1163. **`tests/ui/pattern/usefulness/match-byte-array-patterns.rs`** -> AI Confidence: **99.29%**
1164. **`tests/ui/pattern/usefulness/match-non-exhaustive.rs`** -> AI Confidence: **99.29%**
1165. **`tests/ui/pattern/usefulness/match-slice-patterns.rs`** -> AI Confidence: **99.29%**
1166. **`tests/ui/pattern/usefulness/slice-pattern-const-2.rs`** -> AI Confidence: **99.29%**
1167. **`tests/ui/pattern/usefulness/slice-pattern-const-3.rs`** -> AI Confidence: **99.29%**
1168. **`tests/ui/pattern/usefulness/slice-pattern-const.rs`** -> AI Confidence: **99.29%**
1169. **`tests/ui/pattern/usefulness/slice-patterns-exhaustiveness.rs`** -> AI Confidence: **99.29%**
1170. **`tests/ui/pattern/usefulness/slice_of_empty.rs`** -> AI Confidence: **99.29%**
1171. **`tests/ui/pattern/usefulness/type_polymorphic_byte_str_literals.rs`** -> AI Confidence: **99.29%**
1172. **`tests/ui/privacy/unreachable-issue-121455.rs`** -> AI Confidence: **99.29%**
1173. **`tests/ui/proc-macro/identity-closure-preserving.rs`** -> AI Confidence: **99.29%**
1174. **`tests/ui/proc-macro/issue-76182-leading-vert-pat.rs`** -> AI Confidence: **99.29%**
1175. **`tests/ui/proc-macro/macro-quote-cond.rs`** -> AI Confidence: **99.29%**
1176. **`tests/ui/proc-macro/proc-macro-gates2.rs`** -> AI Confidence: **99.29%**
1177. **`tests/ui/proc-macro/signature.rs`** -> AI Confidence: **99.29%**
1178. **`tests/ui/range/range-inclusive-pattern-precedence.rs`** -> AI Confidence: **99.29%**
1179. **`tests/ui/range/range-inclusive-pattern-precedence2.rs`** -> AI Confidence: **99.29%**
1180. **`tests/ui/range/range-negative-literal-unsigned-type.rs`** -> AI Confidence: **99.29%**
1181. **`tests/ui/reachable/expr_loop.rs`** -> AI Confidence: **99.29%**
1182. **`tests/ui/regions/issue-102392.rs`** -> AI Confidence: **99.29%**
1183. **`tests/ui/resolve/auxiliary/fake_matches.rs`** -> AI Confidence: **99.29%**
1184. **`tests/ui/resolve/const-iter-no-conflict-for-loop.rs`** -> AI Confidence: **99.29%**
1185. **`tests/ui/resolve/issue-114433-invalid-unused-qualifications-suggestion.rs`** -> AI Confidence: **99.29%**
1186. **`tests/ui/resolve/resolve-label.rs`** -> AI Confidence: **99.29%**
1187. **`tests/ui/resolve/token-error-correct-2.rs`** -> AI Confidence: **99.29%**
1188. **`tests/ui/resolve/unresolved-module-error-33293.rs`** -> AI Confidence: **99.29%**
1189. **`tests/ui/return/dont-suggest-through-inner-const.rs`** -> AI Confidence: **99.29%**
1190. **`tests/ui/return/tail-expr-if-as-return.rs`** -> AI Confidence: **99.29%**
1191. **`tests/ui/rfcs/rfc-0000-never_patterns/ICE-119271-never-arm-attr-in-guard.rs`** -> AI Confidence: **99.29%**
1192. **`tests/ui/rfcs/rfc-0000-never_patterns/typeck.rs`** -> AI Confidence: **99.29%**
1193. **`tests/ui/rfcs/rfc-0107-bind-by-move-pattern-guards/former-E0008-now-pass.rs`** -> AI Confidence: **99.29%**
1194. **`tests/ui/rfcs/rfc-1937-termination-trait/termination-trait-for-str-err.rs`** -> AI Confidence: **99.29%**
1195. **`tests/ui/rfcs/rfc-2008-non-exhaustive/enum.rs`** -> AI Confidence: **99.29%**
1196. **`tests/ui/rfcs/rfc-2396-target_feature-11/closures-inherit-target_feature.rs`** -> AI Confidence: **99.29%**
1197. **`tests/ui/rfcs/rfc-2497-if-let-chains/no-double-assigments.rs`** -> AI Confidence: **99.29%**
1198. **`tests/ui/self/self_type_macro_name.rs`** -> AI Confidence: **99.29%**
1199. **`tests/ui/single-use-lifetime/fn-types.rs`** -> AI Confidence: **99.29%**
1200. **`tests/ui/span/E0805.rs`** -> AI Confidence: **99.29%**
1201. **`tests/ui/static/issue-24446.rs`** -> AI Confidence: **99.29%**
1202. **`tests/ui/static/static-closures.rs`** -> AI Confidence: **99.29%**
1203. **`tests/ui/structs/struct-variant-privacy-xc.rs`** -> AI Confidence: **99.29%**
1204. **`tests/ui/suggestions/fn-to-method-deeply-nested.rs`** -> AI Confidence: **99.29%**
1205. **`tests/ui/suggestions/for-loop-missing-in.rs`** -> AI Confidence: **99.29%**
1206. **`tests/ui/suggestions/issue-81839.rs`** -> AI Confidence: **99.29%**
1207. **`tests/ui/suggestions/issue-83892.rs`** -> AI Confidence: **99.29%**
1208. **`tests/ui/suggestions/issue-83943.rs`** -> AI Confidence: **99.29%**
1209. **`tests/ui/suggestions/issue-94171.rs`** -> AI Confidence: **99.29%**
1210. **`tests/ui/suggestions/js-style-comparison-op-separate-eq-token.rs`** -> AI Confidence: **99.29%**
1211. **`tests/ui/suggestions/js-style-comparison-op.rs`** -> AI Confidence: **99.29%**
1212. **`tests/ui/suggestions/option-to-bool.rs`** -> AI Confidence: **99.29%**
1213. **`tests/ui/suggestions/return-elided-lifetime.rs`** -> AI Confidence: **99.29%**
1214. **`tests/ui/suggestions/suggest-labels.rs`** -> AI Confidence: **99.29%**
1215. **`tests/ui/suggestions/suggest-let-for-assignment.rs`** -> AI Confidence: **99.29%**
1216. **`tests/ui/target-feature/implied-features-nvptx.rs`** -> AI Confidence: **99.29%**
1217. **`tests/ui/target-feature/target-feature-detection.rs`** -> AI Confidence: **99.29%**
1218. **`tests/ui/thir-print/str-patterns.rs`** -> AI Confidence: **99.29%**
1219. **`tests/ui/thread-local/spawn-hook-atexit.rs`** -> AI Confidence: **99.29%**
1220. **`tests/ui/trait-bounds/for-binder-placement-error-39089.rs`** -> AI Confidence: **99.29%**
1221. **`tests/ui/traits/const-traits/call.rs`** -> AI Confidence: **99.29%**
1222. **`tests/ui/traits/const-traits/gate.rs`** -> AI Confidence: **99.29%**
1223. **`tests/ui/traits/const-traits/match-non-const-eq.rs`** -> AI Confidence: **99.29%**
1224. **`tests/ui/traits/next-solver/coercion/coerce-depth.rs`** -> AI Confidence: **99.29%**
1225. **`tests/ui/traits/next-solver/slice-match-byte-lit.rs`** -> AI Confidence: **99.29%**
1226. **`tests/ui/traits/next-solver/typeck/structurally-resolve-in-resolve_for_branch.rs`** -> AI Confidence: **99.29%**
1227. **`tests/ui/traits/non_lifetime_binders/on-ptr.rs`** -> AI Confidence: **99.29%**
1228. **`tests/ui/traits/question-mark-span-144304.rs`** -> AI Confidence: **99.29%**
1229. **`tests/ui/treat-err-as-bug/panic-causes-oom-112708.rs`** -> AI Confidence: **99.29%**
1230. **`tests/ui/try-block/try-block-heterogeneous.rs`** -> AI Confidence: **99.29%**
1231. **`tests/ui/try-block/try-block-in-match.rs`** -> AI Confidence: **99.29%**
1232. **`tests/ui/try-block/try-block-in-while.rs`** -> AI Confidence: **99.29%**
1233. **`tests/ui/try-trait/bad-interconversion.rs`** -> AI Confidence: **99.29%**
1234. **`tests/ui/try-trait/incompatible-types-with-question-mark-51632.rs`** -> AI Confidence: **99.29%**
1235. **`tests/ui/try-trait/issue-32709.rs`** -> AI Confidence: **99.29%**
1236. **`tests/ui/try-trait/try-operator-expansion-hygiene.rs`** -> AI Confidence: **99.29%**
1237. **`tests/ui/try-trait/try-operator-on-main.rs`** -> AI Confidence: **99.29%**
1238. **`tests/ui/type-alias-impl-trait/different_defining_uses_never_type2.rs`** -> AI Confidence: **99.29%**
1239. **`tests/ui/type/type-check/assignment-in-if.rs`** -> AI Confidence: **99.29%**
1240. **`tests/ui/typeck/auxiliary/extern-macro-issue-139050.rs`** -> AI Confidence: **99.29%**
1241. **`tests/ui/typeck/consider-borrowing-141810-1.rs`** -> AI Confidence: **99.29%**
1242. **`tests/ui/typeck/consider-borrowing-141810-2.rs`** -> AI Confidence: **99.29%**
1243. **`tests/ui/typeck/deref-multi.rs`** -> AI Confidence: **99.29%**
1244. **`tests/ui/typeck/for-in-const-eval.rs`** -> AI Confidence: **99.29%**
1245. **`tests/ui/typeck/issue-114918/const-in-fn-return-type.rs`** -> AI Confidence: **99.29%**
1246. **`tests/ui/typeck/issue-81943.rs`** -> AI Confidence: **99.29%**
1247. **`tests/ui/typeck/issue-91328.rs`** -> AI Confidence: **99.29%**
1248. **`tests/ui/typeck/issue-92481.rs`** -> AI Confidence: **99.29%**
1249. **`tests/ui/typeck/typeck-closure-to-unsafe-fn-ptr.rs`** -> AI Confidence: **99.29%**
1250. **`tests/ui/typeck/while-loop-block-cond.rs`** -> AI Confidence: **99.29%**
1251. **`tests/ui/typeck/while-type-error.rs`** -> AI Confidence: **99.29%**
1252. **`tests/ui/unboxed-closures/issue-18661.rs`** -> AI Confidence: **99.29%**
1253. **`tests/ui/unpretty/thir-tree-break-outside-loop-83048.rs`** -> AI Confidence: **99.29%**
1254. **`tests/ui/unsafe/break-inside-unsafe-block-issue-128604.rs`** -> AI Confidence: **99.29%**
1255. **`tests/ui/unsafe/issue-115348-false-positive-warning-of-unnecessary-unsafe.rs`** -> AI Confidence: **99.29%**
1256. **`tests/ui/unsized-locals/unsized-non-place-exprs.rs`** -> AI Confidence: **99.29%**
1257. **`configure`** -> AI Confidence: **99.29%**
1258. **`src/ci/docker/host-x86_64/disabled/dist-x86_64-haiku/llvm-config.sh`** -> AI Confidence: **99.29%**
1259. **`src/ci/docker/host-x86_64/pr-check-1/check-default-config-profiles.sh`** -> AI Confidence: **99.29%**
1260. **`src/ci/docker/host-x86_64/x86_64-gnu-miri/check-miri.sh`** -> AI Confidence: **99.29%**
1261. **`src/ci/docker/scripts/cross-apt-packages.sh`** -> AI Confidence: **99.29%**
1262. **`src/ci/docker/scripts/i686-gnu-nopt-2.sh`** -> AI Confidence: **99.29%**
1263. **`src/ci/docker/scripts/musl.sh`** -> AI Confidence: **99.29%**
1264. **`src/ci/docker/scripts/stage_2_test_set1.sh`** -> AI Confidence: **99.29%**
1265. **`src/ci/docker/scripts/stage_2_test_set2.sh`** -> AI Confidence: **99.29%**
1266. **`src/ci/scripts/create-doc-artifacts.sh`** -> AI Confidence: **99.29%**
1267. **`src/doc/rustc-dev-guide/ci/linkcheck.sh`** -> AI Confidence: **99.29%**
1268. **`src/etc/cat-and-grep.sh`** -> AI Confidence: **99.29%**
1269. **`src/etc/completions/x.fish`** -> AI Confidence: **99.29%**
1270. **`src/etc/completions/x.py.fish`** -> AI Confidence: **99.29%**
1271. **`src/etc/completions/x.py.zsh`** -> AI Confidence: **99.29%**
1272. **`src/etc/completions/x.zsh`** -> AI Confidence: **99.29%**
1273. **`src/etc/installer/pkg/postinstall`** -> AI Confidence: **99.29%**
1274. **`src/etc/rust-gdb`** -> AI Confidence: **99.29%**
1275. **`src/etc/rust-gdbgui`** -> AI Confidence: **99.29%**
1276. **`src/tools/clippy/tests/ui/short_circuit_statement.fixed`** -> AI Confidence: **99.29%**
1277. **`src/tools/clippy/tests/ui/single_char_pattern.fixed`** -> AI Confidence: **99.29%**
1278. **`src/tools/linkchecker/linkcheck.sh`** -> AI Confidence: **99.29%**
1279. **`src/tools/miri/miri`** -> AI Confidence: **99.29%**
1280. **`src/tools/rustfmt/bootstrap.sh`** -> AI Confidence: **99.29%**
1281. **`src/etc/completions/x.ps1`** -> AI Confidence: **99.29%**
1282. **`src/etc/completions/x.py.ps1`** -> AI Confidence: **99.29%**
1283. **`src/ci/docker/host-aarch64/aarch64-gnu-debug/Dockerfile`** -> AI Confidence: **99.29%**
1284. **`src/ci/docker/host-aarch64/aarch64-gnu-llvm-21/Dockerfile`** -> AI Confidence: **99.29%**
1285. **`src/ci/docker/host-aarch64/aarch64-gnu/Dockerfile`** -> AI Confidence: **99.29%**
1286. **`src/ci/docker/host-x86_64/arm-android/Dockerfile`** -> AI Confidence: **99.29%**
1287. **`src/ci/docker/host-x86_64/armhf-gnu/Dockerfile`** -> AI Confidence: **99.29%**
1288. **`src/ci/docker/host-x86_64/disabled/dist-aarch64-android/Dockerfile`** -> AI Confidence: **99.29%**
1289. **`src/ci/docker/host-x86_64/disabled/dist-armv7-android/Dockerfile`** -> AI Confidence: **99.29%**
1290. **`src/ci/docker/host-x86_64/disabled/dist-i686-android/Dockerfile`** -> AI Confidence: **99.29%**
1291. **`src/ci/docker/host-x86_64/disabled/dist-m68k-linux/Dockerfile`** -> AI Confidence: **99.29%**
1292. **`src/ci/docker/host-x86_64/disabled/dist-powerpcspe-linux/Dockerfile`** -> AI Confidence: **99.29%**
1293. **`src/ci/docker/host-x86_64/disabled/dist-sparc64-linux/Dockerfile`** -> AI Confidence: **99.29%**
1294. **`src/ci/docker/host-x86_64/disabled/dist-x86_64-android/Dockerfile`** -> AI Confidence: **99.29%**
1295. **`src/ci/docker/host-x86_64/disabled/dist-x86_64-dragonfly/Dockerfile`** -> AI Confidence: **99.29%**
1296. **`src/ci/docker/host-x86_64/disabled/riscv64gc-gnu/Dockerfile`** -> AI Confidence: **99.29%**
1297. **`src/ci/docker/host-x86_64/dist-android/Dockerfile`** -> AI Confidence: **99.29%**
1298. **`src/ci/docker/host-x86_64/dist-ohos-aarch64/Dockerfile`** -> AI Confidence: **99.29%**
1299. **`src/ci/docker/host-x86_64/dist-ohos-armv7/Dockerfile`** -> AI Confidence: **99.29%**
1300. **`src/ci/docker/host-x86_64/dist-ohos-x86_64/Dockerfile`** -> AI Confidence: **99.29%**
1301. **`src/ci/docker/host-x86_64/dist-sparcv9-solaris/Dockerfile`** -> AI Confidence: **99.29%**
1302. **`src/ci/docker/host-x86_64/dist-various-1/Dockerfile`** -> AI Confidence: **99.29%**
1303. **`src/ci/docker/host-x86_64/dist-x86_64-freebsd/Dockerfile`** -> AI Confidence: **99.29%**
1304. **`src/ci/docker/host-x86_64/dist-x86_64-illumos/Dockerfile`** -> AI Confidence: **99.29%**
1305. **`src/ci/docker/host-x86_64/dist-x86_64-solaris/Dockerfile`** -> AI Confidence: **99.29%**
1306. **`src/ci/docker/host-x86_64/i686-gnu-nopt/Dockerfile`** -> AI Confidence: **99.29%**
1307. **`src/ci/docker/host-x86_64/i686-gnu/Dockerfile`** -> AI Confidence: **99.29%**
1308. **`src/ci/docker/host-x86_64/optional-x86_64-gnu-parallel-frontend/Dockerfile`** -> AI Confidence: **99.29%**
1309. **`src/ci/docker/host-x86_64/pr-check-1/Dockerfile`** -> AI Confidence: **99.29%**
1310. **`src/ci/docker/host-x86_64/pr-check-2/Dockerfile`** -> AI Confidence: **99.29%**
1311. **`src/ci/docker/host-x86_64/test-various/Dockerfile`** -> AI Confidence: **99.29%**
1312. **`src/ci/docker/host-x86_64/tidy/Dockerfile`** -> AI Confidence: **99.29%**
1313. **`src/ci/docker/host-x86_64/x86_64-gnu-aux/Dockerfile`** -> AI Confidence: **99.29%**
1314. **`src/ci/docker/host-x86_64/x86_64-gnu-debug/Dockerfile`** -> AI Confidence: **99.29%**
1315. **`src/ci/docker/host-x86_64/x86_64-gnu-distcheck/Dockerfile`** -> AI Confidence: **99.29%**
1316. **`src/ci/docker/host-x86_64/x86_64-gnu-gcc/Dockerfile`** -> AI Confidence: **99.29%**
1317. **`src/ci/docker/host-x86_64/x86_64-gnu-llvm-21/Dockerfile`** -> AI Confidence: **99.29%**
1318. **`src/ci/docker/host-x86_64/x86_64-gnu-llvm-22/Dockerfile`** -> AI Confidence: **99.29%**
1319. **`src/ci/docker/host-x86_64/x86_64-gnu-miri/Dockerfile`** -> AI Confidence: **99.29%**
1320. **`src/ci/docker/host-x86_64/x86_64-gnu-nopt/Dockerfile`** -> AI Confidence: **99.29%**
1321. **`src/ci/docker/host-x86_64/x86_64-gnu-tools/Dockerfile`** -> AI Confidence: **99.29%**
1322. **`src/ci/docker/host-x86_64/x86_64-gnu/Dockerfile`** -> AI Confidence: **99.29%**
1323. **`src/ci/docker/host-x86_64/x86_64-rust-for-linux/Dockerfile`** -> AI Confidence: **99.29%**
1324. **`src/tools/error_index_generator/error-index.js`** -> AI Confidence: **99.29%**
1325. **`tests/rustdoc-js-std/option-type-signatures.js`** -> AI Confidence: **99.29%**
1326. **`tests/rustdoc-js-std/parser-errors.js`** -> AI Confidence: **99.29%**
1327. **`tests/rustdoc-js-std/parser-quote.js`** -> AI Confidence: **99.29%**
1328. **`tests/rustdoc-js-std/parser-reference.js`** -> AI Confidence: **99.29%**
1329. **`tests/rustdoc-js-std/simd-type-signatures.js`** -> AI Confidence: **99.29%**
1330. **`tests/rustdoc-js/basic.js`** -> AI Confidence: **99.29%**
1331. **`tests/rustdoc-js/case.js`** -> AI Confidence: **99.29%**
1332. **`tests/rustdoc-js/doc-alias.js`** -> AI Confidence: **99.29%**
1333. **`tests/rustdoc-js/merged-doc.js`** -> AI Confidence: **99.29%**
1334. **`tests/rustdoc-js/reference.js`** -> AI Confidence: **99.29%**
1335. **`tests/rustdoc-js/search-method-disambiguate.js`** -> AI Confidence: **99.29%**
1336. **`compiler/rustc_ast/src/token.rs`** -> AI Confidence: **99.25%**
1337. **`compiler/rustc_borrowck/src/places_conflict.rs`** -> AI Confidence: **99.25%**
1338. **`compiler/rustc_codegen_llvm/src/llvm_util.rs`** -> AI Confidence: **99.25%**
1339. **`compiler/rustc_target/src/target_features.rs`** -> AI Confidence: **99.25%**
1340. **`compiler/rustc_trait_selection/src/error_reporting/traits/call_kind.rs`** -> AI Confidence: **99.25%**
1341. **`library/core/src/marker.rs`** -> AI Confidence: **99.25%**
1342. **`library/core/src/task/ready.rs`** -> AI Confidence: **99.25%**
1343. **`library/std/src/sys/random/linux.rs`** -> AI Confidence: **99.25%**
1344. **`src/tools/miri/cargo-miri/src/setup.rs`** -> AI Confidence: **99.25%**
1345. **`src/tools/miri/src/shims/alloc.rs`** -> AI Confidence: **99.25%**
1346. **`src/tools/rust-analyzer/crates/hir-ty/src/layout/target.rs`** -> AI Confidence: **99.25%**
1347. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/attribute/lint.rs`** -> AI Confidence: **99.25%**
1348. **`src/tools/rust-analyzer/crates/rust-analyzer/src/lsp/from_proto.rs`** -> AI Confidence: **99.25%**
1349. **`src/tools/rust-analyzer/crates/rust-analyzer/src/reload.rs`** -> AI Confidence: **99.25%**
1350. **`src/tools/rust-analyzer/crates/syntax-bridge/src/prettify_macro_expansion.rs`** -> AI Confidence: **99.25%**
1351. **`src/tools/rustfmt/src/utils.rs`** -> AI Confidence: **99.25%**
1352. **`src/tools/rust-analyzer/editors/code/src/debug.ts`** -> AI Confidence: **99.25%**
1353. **`compiler/rustc_abi/src/lib.rs`** -> AI Confidence: **99.24%**
1354. **`compiler/rustc_ast/src/util/literal.rs`** -> AI Confidence: **99.24%**
1355. **`compiler/rustc_ast/src/visit.rs`** -> AI Confidence: **99.24%**
1356. **`compiler/rustc_ast_lowering/src/asm.rs`** -> AI Confidence: **99.24%**
1357. **`compiler/rustc_ast_pretty/src/pprust/state.rs`** -> AI Confidence: **99.24%**
1358. **`compiler/rustc_ast_pretty/src/pprust/state/item.rs`** -> AI Confidence: **99.24%**
1359. **`compiler/rustc_attr_parsing/src/attributes/cfg.rs`** -> AI Confidence: **99.24%**
1360. **`compiler/rustc_attr_parsing/src/attributes/codegen_attrs.rs`** -> AI Confidence: **99.24%**
1361. **`compiler/rustc_attr_parsing/src/attributes/diagnostic/mod.rs`** -> AI Confidence: **99.24%**
1362. **`compiler/rustc_attr_parsing/src/attributes/doc.rs`** -> AI Confidence: **99.24%**
1363. **`compiler/rustc_attr_parsing/src/parser.rs`** -> AI Confidence: **99.24%**
1364. **`compiler/rustc_borrowck/src/diagnostics/conflict_errors.rs`** -> AI Confidence: **99.24%**
1365. **`compiler/rustc_borrowck/src/diagnostics/explain_borrow.rs`** -> AI Confidence: **99.24%**
1366. **`compiler/rustc_borrowck/src/diagnostics/mod.rs`** -> AI Confidence: **99.24%**
1367. **`compiler/rustc_borrowck/src/diagnostics/mutability_errors.rs`** -> AI Confidence: **99.24%**
1368. **`compiler/rustc_borrowck/src/polonius/legacy/loan_invalidations.rs`** -> AI Confidence: **99.24%**
1369. **`compiler/rustc_builtin_macros/src/asm.rs`** -> AI Confidence: **99.24%**
1370. **`compiler/rustc_builtin_macros/src/concat_bytes.rs`** -> AI Confidence: **99.24%**
1371. **`compiler/rustc_builtin_macros/src/edition_panic.rs`** -> AI Confidence: **99.24%**
1372. **`compiler/rustc_builtin_macros/src/format.rs`** -> AI Confidence: **99.24%**
1373. **`compiler/rustc_builtin_macros/src/test.rs`** -> AI Confidence: **99.24%**
1374. **`compiler/rustc_codegen_cranelift/src/inline_asm.rs`** -> AI Confidence: **99.24%**
1375. **`compiler/rustc_codegen_gcc/build_system/src/fuzz.rs`** -> AI Confidence: **99.24%**
1376. **`compiler/rustc_codegen_gcc/src/back/write.rs`** -> AI Confidence: **99.24%**
1377. **`compiler/rustc_codegen_gcc/src/callee.rs`** -> AI Confidence: **99.24%**
1378. **`compiler/rustc_codegen_llvm/src/abi.rs`** -> AI Confidence: **99.24%**
1379. **`compiler/rustc_codegen_ssa/src/back/apple.rs`** -> AI Confidence: **99.24%**
1380. **`compiler/rustc_codegen_ssa/src/back/lto.rs`** -> AI Confidence: **99.24%**
1381. **`compiler/rustc_codegen_ssa/src/back/symbol_export.rs`** -> AI Confidence: **99.24%**
1382. **`compiler/rustc_codegen_ssa/src/common.rs`** -> AI Confidence: **99.24%**
1383. **`compiler/rustc_codegen_ssa/src/mir/rvalue.rs`** -> AI Confidence: **99.24%**
1384. **`compiler/rustc_const_eval/src/check_consts/resolver.rs`** -> AI Confidence: **99.24%**
1385. **`compiler/rustc_const_eval/src/interpret/discriminant.rs`** -> AI Confidence: **99.24%**
1386. **`compiler/rustc_const_eval/src/interpret/memory.rs`** -> AI Confidence: **99.24%**
1387. **`compiler/rustc_const_eval/src/interpret/place.rs`** -> AI Confidence: **99.24%**
1388. **`compiler/rustc_const_eval/src/interpret/projection.rs`** -> AI Confidence: **99.24%**
1389. **`compiler/rustc_const_eval/src/interpret/visitor.rs`** -> AI Confidence: **99.24%**
1390. **`compiler/rustc_driver_impl/src/highlighter.rs`** -> AI Confidence: **99.24%**
1391. **`compiler/rustc_errors/src/markdown/parse.rs`** -> AI Confidence: **99.24%**
1392. **`compiler/rustc_expand/src/config.rs`** -> AI Confidence: **99.24%**
1393. **`compiler/rustc_expand/src/mbe/quoted.rs`** -> AI Confidence: **99.24%**
1394. **`compiler/rustc_expand/src/placeholders.rs`** -> AI Confidence: **99.24%**
1395. **`compiler/rustc_feature/src/builtin_attrs.rs`** -> AI Confidence: **99.24%**
1396. **`compiler/rustc_hir/src/lang_items.rs`** -> AI Confidence: **99.24%**
1397. **`compiler/rustc_hir_analysis/src/check/check.rs`** -> AI Confidence: **99.24%**
1398. **`compiler/rustc_hir_analysis/src/check/region.rs`** -> AI Confidence: **99.24%**
1399. **`compiler/rustc_hir_analysis/src/check_unused.rs`** -> AI Confidence: **99.24%**
1400. **`compiler/rustc_hir_analysis/src/errors/wrong_number_of_generic_args.rs`** -> AI Confidence: **99.24%**
1401. **`compiler/rustc_hir_pretty/src/lib.rs`** -> AI Confidence: **99.24%**
1402. **`compiler/rustc_hir_typeck/src/cast.rs`** -> AI Confidence: **99.24%**
1403. **`compiler/rustc_hir_typeck/src/demand.rs`** -> AI Confidence: **99.24%**
1404. **`compiler/rustc_hir_typeck/src/expr.rs`** -> AI Confidence: **99.24%**
1405. **`compiler/rustc_hir_typeck/src/fn_ctxt/adjust_fulfillment_errors.rs`** -> AI Confidence: **99.24%**
1406. **`compiler/rustc_hir_typeck/src/fn_ctxt/checks.rs`** -> AI Confidence: **99.24%**
1407. **`compiler/rustc_hir_typeck/src/method/suggest.rs`** -> AI Confidence: **99.24%**
1408. **`compiler/rustc_hir_typeck/src/pat.rs`** -> AI Confidence: **99.24%**
1409. **`compiler/rustc_infer/src/infer/canonical/query_response.rs`** -> AI Confidence: **99.24%**
1410. **`compiler/rustc_infer/src/infer/lexical_region_resolve/mod.rs`** -> AI Confidence: **99.24%**
1411. **`compiler/rustc_infer/src/infer/outlives/obligations.rs`** -> AI Confidence: **99.24%**
1412. **`compiler/rustc_infer/src/infer/outlives/test_type_match.rs`** -> AI Confidence: **99.24%**
1413. **`compiler/rustc_infer/src/infer/resolve.rs`** -> AI Confidence: **99.24%**
1414. **`compiler/rustc_infer/src/infer/snapshot/fudge.rs`** -> AI Confidence: **99.24%**
1415. **`compiler/rustc_lint/src/builtin.rs`** -> AI Confidence: **99.24%**
1416. **`compiler/rustc_lint/src/dangling.rs`** -> AI Confidence: **99.24%**
1417. **`compiler/rustc_lint/src/early/diagnostics.rs`** -> AI Confidence: **99.24%**
1418. **`compiler/rustc_lint/src/for_loops_over_fallibles.rs`** -> AI Confidence: **99.24%**
1419. **`compiler/rustc_lint/src/if_let_rescope.rs`** -> AI Confidence: **99.24%**
1420. **`compiler/rustc_lint/src/invalid_from_utf8.rs`** -> AI Confidence: **99.24%**
1421. **`compiler/rustc_lint/src/macro_expr_fragment_specifier_2024_migration.rs`** -> AI Confidence: **99.24%**
1422. **`compiler/rustc_lint/src/map_unit_fn.rs`** -> AI Confidence: **99.24%**
1423. **`compiler/rustc_lint/src/non_fmt_panic.rs`** -> AI Confidence: **99.24%**
1424. **`compiler/rustc_lint/src/non_local_def.rs`** -> AI Confidence: **99.24%**
1425. **`compiler/rustc_lint/src/nonstandard_style.rs`** -> AI Confidence: **99.24%**
1426. **`compiler/rustc_lint/src/reference_casting.rs`** -> AI Confidence: **99.24%**
1427. **`compiler/rustc_lint/src/shadowed_into_iter.rs`** -> AI Confidence: **99.24%**
1428. **`compiler/rustc_lint/src/static_mut_refs.rs`** -> AI Confidence: **99.24%**
1429. **`compiler/rustc_lint/src/transmute.rs`** -> AI Confidence: **99.24%**
1430. **`compiler/rustc_lint/src/unused.rs`** -> AI Confidence: **99.24%**
1431. **`compiler/rustc_lint/src/unused/must_use.rs`** -> AI Confidence: **99.24%**
1432. **`compiler/rustc_macros/src/diagnostics/diagnostic_builder.rs`** -> AI Confidence: **99.24%**
1433. **`compiler/rustc_macros/src/diagnostics/message.rs`** -> AI Confidence: **99.24%**
1434. **`compiler/rustc_macros/src/diagnostics/subdiagnostic.rs`** -> AI Confidence: **99.24%**
1435. **`compiler/rustc_macros/src/diagnostics/utils.rs`** -> AI Confidence: **99.24%**
1436. **`compiler/rustc_metadata/src/creader.rs`** -> AI Confidence: **99.24%**
1437. **`compiler/rustc_metadata/src/locator.rs`** -> AI Confidence: **99.24%**
1438. **`compiler/rustc_middle/src/dep_graph/dep_node.rs`** -> AI Confidence: **99.24%**
1439. **`compiler/rustc_middle/src/hir/map.rs`** -> AI Confidence: **99.24%**
1440. **`compiler/rustc_middle/src/middle/codegen_fn_attrs.rs`** -> AI Confidence: **99.24%**
1441. **`compiler/rustc_middle/src/middle/privacy.rs`** -> AI Confidence: **99.24%**
1442. **`compiler/rustc_middle/src/mir/consts.rs`** -> AI Confidence: **99.24%**
1443. **`compiler/rustc_middle/src/mir/interpret/error.rs`** -> AI Confidence: **99.24%**
1444. **`compiler/rustc_middle/src/mir/interpret/value.rs`** -> AI Confidence: **99.24%**
1445. **`compiler/rustc_middle/src/traits/specialization_graph.rs`** -> AI Confidence: **99.24%**
1446. **`compiler/rustc_middle/src/ty/adt.rs`** -> AI Confidence: **99.24%**
1447. **`compiler/rustc_middle/src/ty/erase_regions.rs`** -> AI Confidence: **99.24%**
1448. **`compiler/rustc_middle/src/ty/inhabitedness/mod.rs`** -> AI Confidence: **99.24%**
1449. **`compiler/rustc_middle/src/ty/layout.rs`** -> AI Confidence: **99.24%**
1450. **`compiler/rustc_middle/src/ty/pattern.rs`** -> AI Confidence: **99.24%**
1451. **`compiler/rustc_middle/src/ty/significant_drop_order.rs`** -> AI Confidence: **99.24%**
1452. **`compiler/rustc_middle/src/ty/structural_impls.rs`** -> AI Confidence: **99.24%**
1453. **`compiler/rustc_mir_build/src/builder/matches/buckets.rs`** -> AI Confidence: **99.24%**
1454. **`compiler/rustc_mir_build/src/builder/matches/user_ty.rs`** -> AI Confidence: **99.24%**
1455. **`compiler/rustc_mir_build/src/builder/matches/util.rs`** -> AI Confidence: **99.24%**
1456. **`compiler/rustc_mir_build/src/check_unsafety.rs`** -> AI Confidence: **99.24%**
1457. **`compiler/rustc_mir_build/src/thir/pattern/check_match.rs`** -> AI Confidence: **99.24%**
1458. **`compiler/rustc_mir_dataflow/src/impls/liveness.rs`** -> AI Confidence: **99.24%**
1459. **`compiler/rustc_mir_dataflow/src/value_analysis.rs`** -> AI Confidence: **99.24%**
1460. **`compiler/rustc_mir_transform/src/dataflow_const_prop.rs`** -> AI Confidence: **99.24%**
1461. **`compiler/rustc_mir_transform/src/deduce_param_attrs.rs`** -> AI Confidence: **99.24%**
1462. **`compiler/rustc_mir_transform/src/ffi_unwind_calls.rs`** -> AI Confidence: **99.24%**
1463. **`compiler/rustc_mir_transform/src/gvn.rs`** -> AI Confidence: **99.24%**
1464. **`compiler/rustc_mir_transform/src/inline/cycle.rs`** -> AI Confidence: **99.24%**
1465. **`compiler/rustc_mir_transform/src/known_panics_lint.rs`** -> AI Confidence: **99.24%**
1466. **`compiler/rustc_mir_transform/src/lint.rs`** -> AI Confidence: **99.24%**
1467. **`compiler/rustc_mir_transform/src/lower_intrinsics.rs`** -> AI Confidence: **99.24%**
1468. **`compiler/rustc_mir_transform/src/match_branches.rs`** -> AI Confidence: **99.24%**
1469. **`compiler/rustc_mir_transform/src/ref_prop.rs`** -> AI Confidence: **99.24%**
1470. **`compiler/rustc_mir_transform/src/simplify_comparison_integral.rs`** -> AI Confidence: **99.24%**
1471. **`compiler/rustc_mir_transform/src/single_use_consts.rs`** -> AI Confidence: **99.24%**
1472. **`compiler/rustc_mir_transform/src/ssa.rs`** -> AI Confidence: **99.24%**
1473. **`compiler/rustc_mir_transform/src/unreachable_enum_branching.rs`** -> AI Confidence: **99.24%**
1474. **`compiler/rustc_monomorphize/src/mono_checks/abi_check.rs`** -> AI Confidence: **99.24%**
1475. **`compiler/rustc_next_trait_solver/src/canonical/canonicalizer.rs`** -> AI Confidence: **99.24%**
1476. **`compiler/rustc_next_trait_solver/src/solve/alias_relate.rs`** -> AI Confidence: **99.24%**
1477. **`compiler/rustc_next_trait_solver/src/solve/assembly/structural_traits.rs`** -> AI Confidence: **99.24%**
1478. **`compiler/rustc_next_trait_solver/src/solve/mod.rs`** -> AI Confidence: **99.24%**
1479. **`compiler/rustc_parse/src/lexer/unescape_error_reporting.rs`** -> AI Confidence: **99.24%**
1480. **`compiler/rustc_parse/src/parser/attr.rs`** -> AI Confidence: **99.24%**
1481. **`compiler/rustc_parse/src/parser/cfg_select.rs`** -> AI Confidence: **99.24%**
1482. **`compiler/rustc_parse/src/parser/diagnostics.rs`** -> AI Confidence: **99.24%**
1483. **`compiler/rustc_parse/src/parser/mod.rs`** -> AI Confidence: **99.24%**
1484. **`compiler/rustc_passes/src/eii.rs`** -> AI Confidence: **99.24%**
1485. **`compiler/rustc_pattern_analysis/src/pat.rs`** -> AI Confidence: **99.24%**
1486. **`compiler/rustc_pattern_analysis/src/usefulness.rs`** -> AI Confidence: **99.24%**
1487. **`compiler/rustc_public/src/mir/mono.rs`** -> AI Confidence: **99.24%**
1488. **`compiler/rustc_public/src/visitor.rs`** -> AI Confidence: **99.24%**
1489. **`compiler/rustc_public_bridge/src/context/impls.rs`** -> AI Confidence: **99.24%**
1490. **`compiler/rustc_resolve/src/build_reduced_graph.rs`** -> AI Confidence: **99.24%**
1491. **`compiler/rustc_resolve/src/diagnostics.rs`** -> AI Confidence: **99.24%**
1492. **`compiler/rustc_resolve/src/late/diagnostics.rs`** -> AI Confidence: **99.24%**
1493. **`compiler/rustc_resolve/src/macros.rs`** -> AI Confidence: **99.24%**
1494. **`compiler/rustc_resolve/src/rustdoc.rs`** -> AI Confidence: **99.24%**
1495. **`compiler/rustc_session/src/config/cfg.rs`** -> AI Confidence: **99.24%**
1496. **`compiler/rustc_session/src/options.rs`** -> AI Confidence: **99.24%**
1497. **`compiler/rustc_session/src/output.rs`** -> AI Confidence: **99.24%**
1498. **`compiler/rustc_session/src/utils.rs`** -> AI Confidence: **99.24%**
1499. **`compiler/rustc_span/src/source_map.rs`** -> AI Confidence: **99.24%**
1500. **`compiler/rustc_symbol_mangling/src/legacy.rs`** -> AI Confidence: **99.24%**
1501. **`compiler/rustc_symbol_mangling/src/lib.rs`** -> AI Confidence: **99.24%**
1502. **`compiler/rustc_symbol_mangling/src/v0.rs`** -> AI Confidence: **99.24%**
1503. **`compiler/rustc_target/src/callconv/aarch64.rs`** -> AI Confidence: **99.24%**
1504. **`compiler/rustc_target/src/callconv/arm.rs`** -> AI Confidence: **99.24%**
1505. **`compiler/rustc_target/src/callconv/loongarch.rs`** -> AI Confidence: **99.24%**
1506. **`compiler/rustc_target/src/callconv/mips64.rs`** -> AI Confidence: **99.24%**
1507. **`compiler/rustc_target/src/callconv/riscv.rs`** -> AI Confidence: **99.24%**
1508. **`compiler/rustc_target/src/callconv/sparc64.rs`** -> AI Confidence: **99.24%**
1509. **`compiler/rustc_target/src/json.rs`** -> AI Confidence: **99.24%**
1510. **`compiler/rustc_target/src/spec/mod.rs`** -> AI Confidence: **99.24%**
1511. **`compiler/rustc_trait_selection/src/error_reporting/infer/mod.rs`** -> AI Confidence: **99.24%**
1512. **`compiler/rustc_trait_selection/src/error_reporting/infer/need_type_info.rs`** -> AI Confidence: **99.24%**
1513. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/static_impl_trait.rs`** -> AI Confidence: **99.24%**
1514. **`compiler/rustc_trait_selection/src/error_reporting/infer/note_and_explain.rs`** -> AI Confidence: **99.24%**
1515. **`compiler/rustc_trait_selection/src/error_reporting/infer/region.rs`** -> AI Confidence: **99.24%**
1516. **`compiler/rustc_trait_selection/src/error_reporting/infer/suggest.rs`** -> AI Confidence: **99.24%**
1517. **`compiler/rustc_trait_selection/src/error_reporting/traits/fulfillment_errors.rs`** -> AI Confidence: **99.24%**
1518. **`compiler/rustc_trait_selection/src/error_reporting/traits/suggestions.rs`** -> AI Confidence: **99.24%**
1519. **`compiler/rustc_trait_selection/src/traits/query/type_op/implied_outlives_bounds.rs`** -> AI Confidence: **99.24%**
1520. **`compiler/rustc_trait_selection/src/traits/select/candidate_assembly.rs`** -> AI Confidence: **99.24%**
1521. **`compiler/rustc_trait_selection/src/traits/select/mod.rs`** -> AI Confidence: **99.24%**
1522. **`compiler/rustc_trait_selection/src/traits/util.rs`** -> AI Confidence: **99.24%**
1523. **`compiler/rustc_ty_utils/src/abi.rs`** -> AI Confidence: **99.24%**
1524. **`compiler/rustc_ty_utils/src/layout/invariant.rs`** -> AI Confidence: **99.24%**
1525. **`compiler/rustc_type_ir/src/canonical.rs`** -> AI Confidence: **99.24%**
1526. **`compiler/rustc_type_ir/src/relate/combine.rs`** -> AI Confidence: **99.24%**
1527. **`compiler/rustc_type_ir/src/search_graph/mod.rs`** -> AI Confidence: **99.24%**
1528. **`library/alloc/src/alloc.rs`** -> AI Confidence: **99.24%**
1529. **`library/compiler-builtins/crates/libm-macros/src/parse.rs`** -> AI Confidence: **99.24%**
1530. **`library/compiler-builtins/crates/symbol-check/src/main.rs`** -> AI Confidence: **99.24%**
1531. **`library/compiler-builtins/crates/util/src/main.rs`** -> AI Confidence: **99.24%**
1532. **`library/compiler-builtins/libm-test/src/num.rs`** -> AI Confidence: **99.24%**
1533. **`library/compiler-builtins/libm/src/math/arch/mod.rs`** -> AI Confidence: **99.24%**
1534. **`library/compiler-builtins/libm/src/math/generic/fma_wide.rs`** -> AI Confidence: **99.24%**
1535. **`library/compiler-builtins/libm/src/math/jn.rs`** -> AI Confidence: **99.24%**
1536. **`library/compiler-builtins/libm/src/math/support/hex_float.rs`** -> AI Confidence: **99.24%**
1537. **`library/core/src/bstr/mod.rs`** -> AI Confidence: **99.24%**
1538. **`library/core/src/convert/mod.rs`** -> AI Confidence: **99.24%**
1539. **`library/core/src/net/ip_addr.rs`** -> AI Confidence: **99.24%**
1540. **`library/core/src/net/socket_addr.rs`** -> AI Confidence: **99.24%**
1541. **`library/core/src/num/f64.rs`** -> AI Confidence: **99.24%**
1542. **`library/core/src/num/imp/flt2dec/strategy/dragon.rs`** -> AI Confidence: **99.24%**
1543. **`library/core/src/num/wrapping.rs`** -> AI Confidence: **99.24%**
1544. **`library/core/src/ops/arith.rs`** -> AI Confidence: **99.24%**
1545. **`library/core/src/ops/bit.rs`** -> AI Confidence: **99.24%**
1546. **`library/core/src/ops/range.rs`** -> AI Confidence: **99.24%**
1547. **`library/core/src/time.rs`** -> AI Confidence: **99.24%**
1548. **`library/portable-simd/crates/core_simd/src/simd/num/float.rs`** -> AI Confidence: **99.24%**
1549. **`library/proc_macro/src/lib.rs`** -> AI Confidence: **99.24%**
1550. **`library/std/src/fs.rs`** -> AI Confidence: **99.24%**
1551. **`library/std/src/io/error.rs`** -> AI Confidence: **99.24%**
1552. **`library/std/src/os/fd/owned.rs`** -> AI Confidence: **99.24%**
1553. **`library/std/src/os/linux/process.rs`** -> AI Confidence: **99.24%**
1554. **`library/std/src/os/solid/io.rs`** -> AI Confidence: **99.24%**
1555. **`library/std/src/os/wasi/fs.rs`** -> AI Confidence: **99.24%**
1556. **`library/std/src/os/windows/io/handle.rs`** -> AI Confidence: **99.24%**
1557. **`library/std/src/path.rs`** -> AI Confidence: **99.24%**
1558. **`library/std/src/sync/mpmc/error.rs`** -> AI Confidence: **99.24%**
1559. **`library/std/src/sys/backtrace.rs`** -> AI Confidence: **99.24%**
1560. **`library/std/src/sys/fs/motor.rs`** -> AI Confidence: **99.24%**
1561. **`library/std/src/sys/fs/solid.rs`** -> AI Confidence: **99.24%**
1562. **`library/std/src/sys/fs/unix.rs`** -> AI Confidence: **99.24%**
1563. **`library/std/src/sys/io/kernel_copy/linux.rs`** -> AI Confidence: **99.24%**
1564. **`library/std/src/sys/pal/sgx/abi/usercalls/mod.rs`** -> AI Confidence: **99.24%**
1565. **`library/std/src/sys/pal/unix/time.rs`** -> AI Confidence: **99.24%**
1566. **`library/std/src/sys/pal/windows/mod.rs`** -> AI Confidence: **99.24%**
1567. **`library/std/src/sys/path/windows_prefix.rs`** -> AI Confidence: **99.24%**
1568. **`library/std/src/sys/paths/uefi.rs`** -> AI Confidence: **99.24%**
1569. **`library/std/src/sys/process/unix/vxworks.rs`** -> AI Confidence: **99.24%**
1570. **`library/std/src/sys/sync/thread_parking/windows7.rs`** -> AI Confidence: **99.24%**
1571. **`library/std/src/sys/thread_local/key/windows.rs`** -> AI Confidence: **99.24%**
1572. **`library/std/src/thread/join_handle.rs`** -> AI Confidence: **99.24%**
1573. **`library/std/src/thread/scoped.rs`** -> AI Confidence: **99.24%**
1574. **`library/std/src/thread/tests.rs`** -> AI Confidence: **99.24%**
1575. **`library/stdarch/crates/stdarch-gen-arm/src/assert_instr.rs`** -> AI Confidence: **99.24%**
1576. **`library/stdarch/crates/stdarch-gen-arm/src/expression.rs`** -> AI Confidence: **99.24%**
1577. **`library/stdarch/crates/stdarch-gen-arm/src/fn_suffix.rs`** -> AI Confidence: **99.24%**
1578. **`library/stdarch/crates/stdarch-gen-arm/src/intrinsic.rs`** -> AI Confidence: **99.24%**
1579. **`library/stdarch/crates/stdarch-gen-hexagon/src/main.rs`** -> AI Confidence: **99.24%**
1580. **`library/test/src/cli.rs`** -> AI Confidence: **99.24%**
1581. **`src/bootstrap/src/core/build_steps/compile.rs`** -> AI Confidence: **99.24%**
1582. **`src/bootstrap/src/core/build_steps/dist.rs`** -> AI Confidence: **99.24%**
1583. **`src/bootstrap/src/core/build_steps/gcc.rs`** -> AI Confidence: **99.24%**
1584. **`src/bootstrap/src/core/build_steps/setup.rs`** -> AI Confidence: **99.24%**
1585. **`src/bootstrap/src/core/builder/mod.rs`** -> AI Confidence: **99.24%**
1586. **`src/bootstrap/src/core/config/config.rs`** -> AI Confidence: **99.24%**
1587. **`src/bootstrap/src/core/config/flags.rs`** -> AI Confidence: **99.24%**
1588. **`src/bootstrap/src/core/config/mod.rs`** -> AI Confidence: **99.24%**
1589. **`src/bootstrap/src/core/config/toml/llvm.rs`** -> AI Confidence: **99.24%**
1590. **`src/bootstrap/src/core/config/toml/rust.rs`** -> AI Confidence: **99.24%**
1591. **`src/bootstrap/src/core/download.rs`** -> AI Confidence: **99.24%**
1592. **`src/ci/citool/src/main.rs`** -> AI Confidence: **99.24%**
1593. **`src/librustdoc/clean/mod.rs`** -> AI Confidence: **99.24%**
1594. **`src/librustdoc/doctest/make.rs`** -> AI Confidence: **99.24%**
1595. **`src/librustdoc/doctest/runner.rs`** -> AI Confidence: **99.24%**
1596. **`src/librustdoc/html/macro_expansion.rs`** -> AI Confidence: **99.24%**
1597. **`src/librustdoc/html/render/mod.rs`** -> AI Confidence: **99.24%**
1598. **`src/librustdoc/html/render/search_index.rs`** -> AI Confidence: **99.24%**
1599. **`src/librustdoc/json/conversions.rs`** -> AI Confidence: **99.24%**
1600. **`src/librustdoc/passes/collect_intra_doc_links.rs`** -> AI Confidence: **99.24%**
1601. **`src/librustdoc/passes/lint/bare_urls.rs`** -> AI Confidence: **99.24%**
1602. **`src/librustdoc/passes/lint/redundant_explicit_links.rs`** -> AI Confidence: **99.24%**
1603. **`src/librustdoc/passes/lint/unescaped_backticks.rs`** -> AI Confidence: **99.24%**
1604. **`src/librustdoc/passes/propagate_stability.rs`** -> AI Confidence: **99.24%**
1605. **`src/librustdoc/passes/stripper.rs`** -> AI Confidence: **99.24%**
1606. **`src/tools/clippy/clippy_lints/src/almost_complete_range.rs`** -> AI Confidence: **99.24%**
1607. **`src/tools/clippy/clippy_lints/src/approx_const.rs`** -> AI Confidence: **99.24%**
1608. **`src/tools/clippy/clippy_lints/src/arc_with_non_send_sync.rs`** -> AI Confidence: **99.24%**
1609. **`src/tools/clippy/clippy_lints/src/assertions_on_constants.rs`** -> AI Confidence: **99.24%**
1610. **`src/tools/clippy/clippy_lints/src/assertions_on_result_states.rs`** -> AI Confidence: **99.24%**
1611. **`src/tools/clippy/clippy_lints/src/assigning_clones.rs`** -> AI Confidence: **99.24%**
1612. **`src/tools/clippy/clippy_lints/src/attrs/blanket_clippy_restriction_lints.rs`** -> AI Confidence: **99.24%**
1613. **`src/tools/clippy/clippy_lints/src/attrs/useless_attribute.rs`** -> AI Confidence: **99.24%**
1614. **`src/tools/clippy/clippy_lints/src/blocks_in_conditions.rs`** -> AI Confidence: **99.24%**
1615. **`src/tools/clippy/clippy_lints/src/bool_to_int_with_if.rs`** -> AI Confidence: **99.24%**
1616. **`src/tools/clippy/clippy_lints/src/booleans.rs`** -> AI Confidence: **99.24%**
1617. **`src/tools/clippy/clippy_lints/src/box_default.rs`** -> AI Confidence: **99.24%**
1618. **`src/tools/clippy/clippy_lints/src/cargo/multiple_crate_versions.rs`** -> AI Confidence: **99.24%**
1619. **`src/tools/clippy/clippy_lints/src/casts/cast_lossless.rs`** -> AI Confidence: **99.24%**
1620. **`src/tools/clippy/clippy_lints/src/casts/cast_nan_to_int.rs`** -> AI Confidence: **99.24%**
1621. **`src/tools/clippy/clippy_lints/src/casts/cast_possible_truncation.rs`** -> AI Confidence: **99.24%**
1622. **`src/tools/clippy/clippy_lints/src/casts/cast_possible_wrap.rs`** -> AI Confidence: **99.24%**
1623. **`src/tools/clippy/clippy_lints/src/casts/cast_sign_loss.rs`** -> AI Confidence: **99.24%**
1624. **`src/tools/clippy/clippy_lints/src/casts/confusing_method_to_numeric_cast.rs`** -> AI Confidence: **99.24%**
1625. **`src/tools/clippy/clippy_lints/src/casts/needless_type_cast.rs`** -> AI Confidence: **99.24%**
1626. **`src/tools/clippy/clippy_lints/src/casts/ptr_cast_constness.rs`** -> AI Confidence: **99.24%**
1627. **`src/tools/clippy/clippy_lints/src/comparison_chain.rs`** -> AI Confidence: **99.24%**
1628. **`src/tools/clippy/clippy_lints/src/default_union_representation.rs`** -> AI Confidence: **99.24%**
1629. **`src/tools/clippy/clippy_lints/src/derivable_impls.rs`** -> AI Confidence: **99.24%**
1630. **`src/tools/clippy/clippy_lints/src/derive/derive_partial_eq_without_eq.rs`** -> AI Confidence: **99.24%**
1631. **`src/tools/clippy/clippy_lints/src/derive/expl_impl_clone_on_copy.rs`** -> AI Confidence: **99.24%**
1632. **`src/tools/clippy/clippy_lints/src/doc/lazy_continuation.rs`** -> AI Confidence: **99.24%**
1633. **`src/tools/clippy/clippy_lints/src/doc/too_long_first_doc_paragraph.rs`** -> AI Confidence: **99.24%**
1634. **`src/tools/clippy/clippy_lints/src/double_parens.rs`** -> AI Confidence: **99.24%**
1635. **`src/tools/clippy/clippy_lints/src/drop_forget_ref.rs`** -> AI Confidence: **99.24%**
1636. **`src/tools/clippy/clippy_lints/src/empty_drop.rs`** -> AI Confidence: **99.24%**
1637. **`src/tools/clippy/clippy_lints/src/empty_with_brackets.rs`** -> AI Confidence: **99.24%**
1638. **`src/tools/clippy/clippy_lints/src/endian_bytes.rs`** -> AI Confidence: **99.24%**
1639. **`src/tools/clippy/clippy_lints/src/entry.rs`** -> AI Confidence: **99.24%**
1640. **`src/tools/clippy/clippy_lints/src/equatable_if_let.rs`** -> AI Confidence: **99.24%**
1641. **`src/tools/clippy/clippy_lints/src/error_impl_error.rs`** -> AI Confidence: **99.24%**
1642. **`src/tools/clippy/clippy_lints/src/excessive_bools.rs`** -> AI Confidence: **99.24%**
1643. **`src/tools/clippy/clippy_lints/src/exit.rs`** -> AI Confidence: **99.24%**
1644. **`src/tools/clippy/clippy_lints/src/explicit_write.rs`** -> AI Confidence: **99.24%**
1645. **`src/tools/clippy/clippy_lints/src/extra_unused_type_parameters.rs`** -> AI Confidence: **99.24%**
1646. **`src/tools/clippy/clippy_lints/src/fallible_impl_from.rs`** -> AI Confidence: **99.24%**
1647. **`src/tools/clippy/clippy_lints/src/floating_point_arithmetic/mul_add.rs`** -> AI Confidence: **99.24%**
1648. **`src/tools/clippy/clippy_lints/src/floating_point_arithmetic/radians.rs`** -> AI Confidence: **99.24%**
1649. **`src/tools/clippy/clippy_lints/src/format_args.rs`** -> AI Confidence: **99.24%**
1650. **`src/tools/clippy/clippy_lints/src/format_impl.rs`** -> AI Confidence: **99.24%**
1651. **`src/tools/clippy/clippy_lints/src/four_forward_slashes.rs`** -> AI Confidence: **99.24%**
1652. **`src/tools/clippy/clippy_lints/src/from_raw_with_void_ptr.rs`** -> AI Confidence: **99.24%**
1653. **`src/tools/clippy/clippy_lints/src/functions/must_use.rs`** -> AI Confidence: **99.24%**
1654. **`src/tools/clippy/clippy_lints/src/functions/ref_option.rs`** -> AI Confidence: **99.24%**
1655. **`src/tools/clippy/clippy_lints/src/functions/result.rs`** -> AI Confidence: **99.24%**
1656. **`src/tools/clippy/clippy_lints/src/if_not_else.rs`** -> AI Confidence: **99.24%**
1657. **`src/tools/clippy/clippy_lints/src/if_then_some_else_none.rs`** -> AI Confidence: **99.24%**
1658. **`src/tools/clippy/clippy_lints/src/ifs/ifs_same_cond.rs`** -> AI Confidence: **99.24%**
1659. **`src/tools/clippy/clippy_lints/src/ifs/mod.rs`** -> AI Confidence: **99.24%**
1660. **`src/tools/clippy/clippy_lints/src/implicit_return.rs`** -> AI Confidence: **99.24%**
1661. **`src/tools/clippy/clippy_lints/src/implicit_saturating_add.rs`** -> AI Confidence: **99.24%**
1662. **`src/tools/clippy/clippy_lints/src/implied_bounds_in_impls.rs`** -> AI Confidence: **99.24%**
1663. **`src/tools/clippy/clippy_lints/src/incompatible_msrv.rs`** -> AI Confidence: **99.24%**
1664. **`src/tools/clippy/clippy_lints/src/indexing_slicing.rs`** -> AI Confidence: **99.24%**
1665. **`src/tools/clippy/clippy_lints/src/int_plus_one.rs`** -> AI Confidence: **99.24%**
1666. **`src/tools/clippy/clippy_lints/src/items_after_test_module.rs`** -> AI Confidence: **99.24%**
1667. **`src/tools/clippy/clippy_lints/src/large_include_file.rs`** -> AI Confidence: **99.24%**
1668. **`src/tools/clippy/clippy_lints/src/large_stack_arrays.rs`** -> AI Confidence: **99.24%**
1669. **`src/tools/clippy/clippy_lints/src/len_zero.rs`** -> AI Confidence: **99.24%**
1670. **`src/tools/clippy/clippy_lints/src/lifetimes.rs`** -> AI Confidence: **99.24%**
1671. **`src/tools/clippy/clippy_lints/src/literal_string_with_formatting_args.rs`** -> AI Confidence: **99.24%**
1672. **`src/tools/clippy/clippy_lints/src/loops/manual_flatten.rs`** -> AI Confidence: **99.24%**
1673. **`src/tools/clippy/clippy_lints/src/loops/manual_memcpy.rs`** -> AI Confidence: **99.24%**
1674. **`src/tools/clippy/clippy_lints/src/loops/manual_while_let_some.rs`** -> AI Confidence: **99.24%**
1675. **`src/tools/clippy/clippy_lints/src/loops/missing_spin_loop.rs`** -> AI Confidence: **99.24%**
1676. **`src/tools/clippy/clippy_lints/src/loops/mod.rs`** -> AI Confidence: **99.24%**
1677. **`src/tools/clippy/clippy_lints/src/loops/mut_range_bound.rs`** -> AI Confidence: **99.24%**
1678. **`src/tools/clippy/clippy_lints/src/loops/same_item_push.rs`** -> AI Confidence: **99.24%**
1679. **`src/tools/clippy/clippy_lints/src/macro_use.rs`** -> AI Confidence: **99.24%**
1680. **`src/tools/clippy/clippy_lints/src/manual_abs_diff.rs`** -> AI Confidence: **99.24%**
1681. **`src/tools/clippy/clippy_lints/src/manual_assert.rs`** -> AI Confidence: **99.24%**
1682. **`src/tools/clippy/clippy_lints/src/manual_async_fn.rs`** -> AI Confidence: **99.24%**
1683. **`src/tools/clippy/clippy_lints/src/manual_bits.rs`** -> AI Confidence: **99.24%**
1684. **`src/tools/clippy/clippy_lints/src/manual_float_methods.rs`** -> AI Confidence: **99.24%**
1685. **`src/tools/clippy/clippy_lints/src/manual_hash_one.rs`** -> AI Confidence: **99.24%**
1686. **`src/tools/clippy/clippy_lints/src/manual_ignore_case_cmp.rs`** -> AI Confidence: **99.24%**
1687. **`src/tools/clippy/clippy_lints/src/manual_is_ascii_check.rs`** -> AI Confidence: **99.24%**
1688. **`src/tools/clippy/clippy_lints/src/manual_let_else.rs`** -> AI Confidence: **99.24%**
1689. **`src/tools/clippy/clippy_lints/src/manual_range_patterns.rs`** -> AI Confidence: **99.24%**
1690. **`src/tools/clippy/clippy_lints/src/manual_rotate.rs`** -> AI Confidence: **99.24%**
1691. **`src/tools/clippy/clippy_lints/src/manual_slice_size_calculation.rs`** -> AI Confidence: **99.24%**
1692. **`src/tools/clippy/clippy_lints/src/manual_strip.rs`** -> AI Confidence: **99.24%**
1693. **`src/tools/clippy/clippy_lints/src/manual_take.rs`** -> AI Confidence: **99.24%**
1694. **`src/tools/clippy/clippy_lints/src/matches/manual_filter.rs`** -> AI Confidence: **99.24%**
1695. **`src/tools/clippy/clippy_lints/src/matches/manual_ok_err.rs`** -> AI Confidence: **99.24%**
1696. **`src/tools/clippy/clippy_lints/src/matches/match_bool.rs`** -> AI Confidence: **99.24%**
1697. **`src/tools/clippy/clippy_lints/src/matches/match_like_matches.rs`** -> AI Confidence: **99.24%**
1698. **`src/tools/clippy/clippy_lints/src/matches/match_same_arms.rs`** -> AI Confidence: **99.24%**
1699. **`src/tools/clippy/clippy_lints/src/matches/match_wild_err_arm.rs`** -> AI Confidence: **99.24%**
1700. **`src/tools/clippy/clippy_lints/src/matches/needless_match.rs`** -> AI Confidence: **99.24%**
1701. **`src/tools/clippy/clippy_lints/src/matches/overlapping_arms.rs`** -> AI Confidence: **99.24%**
1702. **`src/tools/clippy/clippy_lints/src/matches/significant_drop_in_scrutinee.rs`** -> AI Confidence: **99.24%**
1703. **`src/tools/clippy/clippy_lints/src/matches/try_err.rs`** -> AI Confidence: **99.24%**
1704. **`src/tools/clippy/clippy_lints/src/matches/wild_in_or_pats.rs`** -> AI Confidence: **99.24%**
1705. **`src/tools/clippy/clippy_lints/src/methods/bytecount.rs`** -> AI Confidence: **99.24%**
1706. **`src/tools/clippy/clippy_lints/src/methods/clear_with_drain.rs`** -> AI Confidence: **99.24%**
1707. **`src/tools/clippy/clippy_lints/src/methods/drain_collect.rs`** -> AI Confidence: **99.24%**
1708. **`src/tools/clippy/clippy_lints/src/methods/format_collect.rs`** -> AI Confidence: **99.24%**
1709. **`src/tools/clippy/clippy_lints/src/methods/implicit_clone.rs`** -> AI Confidence: **99.24%**
1710. **`src/tools/clippy/clippy_lints/src/methods/io_other_error.rs`** -> AI Confidence: **99.24%**
1711. **`src/tools/clippy/clippy_lints/src/methods/iter_kv_map.rs`** -> AI Confidence: **99.24%**
1712. **`src/tools/clippy/clippy_lints/src/methods/iter_skip_zero.rs`** -> AI Confidence: **99.24%**
1713. **`src/tools/clippy/clippy_lints/src/methods/join_absolute_paths.rs`** -> AI Confidence: **99.24%**
1714. **`src/tools/clippy/clippy_lints/src/methods/manual_contains.rs`** -> AI Confidence: **99.24%**
1715. **`src/tools/clippy/clippy_lints/src/methods/manual_inspect.rs`** -> AI Confidence: **99.24%**
1716. **`src/tools/clippy/clippy_lints/src/methods/manual_is_variant_and.rs`** -> AI Confidence: **99.24%**
1717. **`src/tools/clippy/clippy_lints/src/methods/manual_ok_or.rs`** -> AI Confidence: **99.24%**
1718. **`src/tools/clippy/clippy_lints/src/methods/manual_str_repeat.rs`** -> AI Confidence: **99.24%**
1719. **`src/tools/clippy/clippy_lints/src/methods/map_identity.rs`** -> AI Confidence: **99.24%**
1720. **`src/tools/clippy/clippy_lints/src/methods/no_effect_replace.rs`** -> AI Confidence: **99.24%**
1721. **`src/tools/clippy/clippy_lints/src/methods/option_as_ref_deref.rs`** -> AI Confidence: **99.24%**
1722. **`src/tools/clippy/clippy_lints/src/methods/readonly_write_lock.rs`** -> AI Confidence: **99.24%**
1723. **`src/tools/clippy/clippy_lints/src/methods/repeat_once.rs`** -> AI Confidence: **99.24%**
1724. **`src/tools/clippy/clippy_lints/src/methods/search_is_some.rs`** -> AI Confidence: **99.24%**
1725. **`src/tools/clippy/clippy_lints/src/methods/should_implement_trait.rs`** -> AI Confidence: **99.24%**
1726. **`src/tools/clippy/clippy_lints/src/methods/str_splitn.rs`** -> AI Confidence: **99.24%**
1727. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_fallible_conversions.rs`** -> AI Confidence: **99.24%**
1728. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_fold.rs`** -> AI Confidence: **99.24%**
1729. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_iter_cloned.rs`** -> AI Confidence: **99.24%**
1730. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_lazy_eval.rs`** -> AI Confidence: **99.24%**
1731. **`src/tools/clippy/clippy_lints/src/methods/unnecessary_literal_unwrap.rs`** -> AI Confidence: **99.24%**
1732. **`src/tools/clippy/clippy_lints/src/methods/useless_asref.rs`** -> AI Confidence: **99.24%**
1733. **`src/tools/clippy/clippy_lints/src/methods/utils.rs`** -> AI Confidence: **99.24%**
1734. **`src/tools/clippy/clippy_lints/src/methods/wrong_self_convention.rs`** -> AI Confidence: **99.24%**
1735. **`src/tools/clippy/clippy_lints/src/minmax.rs`** -> AI Confidence: **99.24%**
1736. **`src/tools/clippy/clippy_lints/src/misc_early/unneeded_field_pattern.rs`** -> AI Confidence: **99.24%**
1737. **`src/tools/clippy/clippy_lints/src/missing_const_for_fn.rs`** -> AI Confidence: **99.24%**
1738. **`src/tools/clippy/clippy_lints/src/missing_const_for_thread_local.rs`** -> AI Confidence: **99.24%**
1739. **`src/tools/clippy/clippy_lints/src/missing_fields_in_debug.rs`** -> AI Confidence: **99.24%**
1740. **`src/tools/clippy/clippy_lints/src/mixed_read_write_in_expression.rs`** -> AI Confidence: **99.24%**
1741. **`src/tools/clippy/clippy_lints/src/multiple_bound_locations.rs`** -> AI Confidence: **99.24%**
1742. **`src/tools/clippy/clippy_lints/src/mutex_atomic.rs`** -> AI Confidence: **99.24%**
1743. **`src/tools/clippy/clippy_lints/src/needless_borrows_for_generic_args.rs`** -> AI Confidence: **99.24%**
1744. **`src/tools/clippy/clippy_lints/src/needless_for_each.rs`** -> AI Confidence: **99.24%**
1745. **`src/tools/clippy/clippy_lints/src/needless_late_init.rs`** -> AI Confidence: **99.24%**
1746. **`src/tools/clippy/clippy_lints/src/needless_pass_by_ref_mut.rs`** -> AI Confidence: **99.24%**
1747. **`src/tools/clippy/clippy_lints/src/needless_pass_by_value.rs`** -> AI Confidence: **99.24%**
1748. **`src/tools/clippy/clippy_lints/src/non_expressive_names.rs`** -> AI Confidence: **99.24%**
1749. **`src/tools/clippy/clippy_lints/src/non_octal_unix_permissions.rs`** -> AI Confidence: **99.24%**
1750. **`src/tools/clippy/clippy_lints/src/non_std_lazy_statics.rs`** -> AI Confidence: **99.24%**
1751. **`src/tools/clippy/clippy_lints/src/non_zero_suggestions.rs`** -> AI Confidence: **99.24%**
1752. **`src/tools/clippy/clippy_lints/src/only_used_in_recursion.rs`** -> AI Confidence: **99.24%**
1753. **`src/tools/clippy/clippy_lints/src/operators/arithmetic_side_effects.rs`** -> AI Confidence: **99.24%**
1754. **`src/tools/clippy/clippy_lints/src/operators/cmp_owned.rs`** -> AI Confidence: **99.24%**
1755. **`src/tools/clippy/clippy_lints/src/operators/decimal_bitwise_operands.rs`** -> AI Confidence: **99.24%**
1756. **`src/tools/clippy/clippy_lints/src/operators/identity_op.rs`** -> AI Confidence: **99.24%**
1757. **`src/tools/clippy/clippy_lints/src/operators/manual_midpoint.rs`** -> AI Confidence: **99.24%**
1758. **`src/tools/clippy/clippy_lints/src/operators/needless_bitwise_bool.rs`** -> AI Confidence: **99.24%**
1759. **`src/tools/clippy/clippy_lints/src/operators/op_ref.rs`** -> AI Confidence: **99.24%**
1760. **`src/tools/clippy/clippy_lints/src/operators/verbose_bit_mask.rs`** -> AI Confidence: **99.24%**
1761. **`src/tools/clippy/clippy_lints/src/pathbuf_init_then_push.rs`** -> AI Confidence: **99.24%**
1762. **`src/tools/clippy/clippy_lints/src/pattern_type_mismatch.rs`** -> AI Confidence: **99.24%**
1763. **`src/tools/clippy/clippy_lints/src/ptr/mod.rs`** -> AI Confidence: **99.24%**
1764. **`src/tools/clippy/clippy_lints/src/ptr/ptr_eq.rs`** -> AI Confidence: **99.24%**
1765. **`src/tools/clippy/clippy_lints/src/redundant_closure_call.rs`** -> AI Confidence: **99.24%**
1766. **`src/tools/clippy/clippy_lints/src/redundant_else.rs`** -> AI Confidence: **99.24%**
1767. **`src/tools/clippy/clippy_lints/src/redundant_locals.rs`** -> AI Confidence: **99.24%**
1768. **`src/tools/clippy/clippy_lints/src/redundant_slicing.rs`** -> AI Confidence: **99.24%**
1769. **`src/tools/clippy/clippy_lints/src/redundant_test_prefix.rs`** -> AI Confidence: **99.24%**
1770. **`src/tools/clippy/clippy_lints/src/ref_option_ref.rs`** -> AI Confidence: **99.24%**
1771. **`src/tools/clippy/clippy_lints/src/reference.rs`** -> AI Confidence: **99.24%**
1772. **`src/tools/clippy/clippy_lints/src/regex.rs`** -> AI Confidence: **99.24%**
1773. **`src/tools/clippy/clippy_lints/src/repeat_vec_with_capacity.rs`** -> AI Confidence: **99.24%**
1774. **`src/tools/clippy/clippy_lints/src/reserve_after_initialization.rs`** -> AI Confidence: **99.24%**
1775. **`src/tools/clippy/clippy_lints/src/returns/needless_return.rs`** -> AI Confidence: **99.24%**
1776. **`src/tools/clippy/clippy_lints/src/same_name_method.rs`** -> AI Confidence: **99.24%**
1777. **`src/tools/clippy/clippy_lints/src/semicolon_if_nothing_returned.rs`** -> AI Confidence: **99.24%**
1778. **`src/tools/clippy/clippy_lints/src/set_contains_or_insert.rs`** -> AI Confidence: **99.24%**
1779. **`src/tools/clippy/clippy_lints/src/shadow.rs`** -> AI Confidence: **99.24%**
1780. **`src/tools/clippy/clippy_lints/src/single_call_fn.rs`** -> AI Confidence: **99.24%**
1781. **`src/tools/clippy/clippy_lints/src/single_option_map.rs`** -> AI Confidence: **99.24%**
1782. **`src/tools/clippy/clippy_lints/src/std_instead_of_core.rs`** -> AI Confidence: **99.24%**
1783. **`src/tools/clippy/clippy_lints/src/string_patterns.rs`** -> AI Confidence: **99.24%**
1784. **`src/tools/clippy/clippy_lints/src/strlen_on_c_strings.rs`** -> AI Confidence: **99.24%**
1785. **`src/tools/clippy/clippy_lints/src/suspicious_xor_used_as_pow.rs`** -> AI Confidence: **99.24%**
1786. **`src/tools/clippy/clippy_lints/src/time_subtraction.rs`** -> AI Confidence: **99.24%**
1787. **`src/tools/clippy/clippy_lints/src/transmute/transmute_ref_to_ref.rs`** -> AI Confidence: **99.24%**
1788. **`src/tools/clippy/clippy_lints/src/transmute/useless_transmute.rs`** -> AI Confidence: **99.24%**
1789. **`src/tools/clippy/clippy_lints/src/tuple_array_conversions.rs`** -> AI Confidence: **99.24%**
1790. **`src/tools/clippy/clippy_lints/src/types/owned_cow.rs`** -> AI Confidence: **99.24%**
1791. **`src/tools/clippy/clippy_lints/src/unconditional_recursion.rs`** -> AI Confidence: **99.24%**
1792. **`src/tools/clippy/clippy_lints/src/unicode.rs`** -> AI Confidence: **99.24%**
1793. **`src/tools/clippy/clippy_lints/src/unit_return_expecting_ord.rs`** -> AI Confidence: **99.24%**
1794. **`src/tools/clippy/clippy_lints/src/unit_types/let_unit_value.rs`** -> AI Confidence: **99.24%**
1795. **`src/tools/clippy/clippy_lints/src/unit_types/unit_arg.rs`** -> AI Confidence: **99.24%**
1796. **`src/tools/clippy/clippy_lints/src/unnecessary_owned_empty_strings.rs`** -> AI Confidence: **99.24%**
1797. **`src/tools/clippy/clippy_lints/src/unnecessary_self_imports.rs`** -> AI Confidence: **99.24%**
1798. **`src/tools/clippy/clippy_lints/src/unnecessary_semicolon.rs`** -> AI Confidence: **99.24%**
1799. **`src/tools/clippy/clippy_lints/src/unused_io_amount.rs`** -> AI Confidence: **99.24%**
1800. **`src/tools/clippy/clippy_lints/src/unused_rounding.rs`** -> AI Confidence: **99.24%**
1801. **`src/tools/clippy/clippy_lints/src/upper_case_acronyms.rs`** -> AI Confidence: **99.24%**
1802. **`src/tools/clippy/clippy_lints/src/useless_conversion.rs`** -> AI Confidence: **99.24%**
1803. **`src/tools/clippy/clippy_lints/src/vec_init_then_push.rs`** -> AI Confidence: **99.24%**
1804. **`src/tools/clippy/clippy_lints/src/wildcard_imports.rs`** -> AI Confidence: **99.24%**
1805. **`src/tools/clippy/clippy_lints/src/write/literal.rs`** -> AI Confidence: **99.24%**
1806. **`src/tools/clippy/clippy_lints/src/zero_repeat_side_effects.rs`** -> AI Confidence: **99.24%**
1807. **`src/tools/clippy/clippy_lints/src/zombie_processes.rs`** -> AI Confidence: **99.24%**
1808. **`src/tools/clippy/clippy_lints_internal/src/almost_standard_lint_formulation.rs`** -> AI Confidence: **99.24%**
1809. **`src/tools/clippy/clippy_lints_internal/src/symbols.rs`** -> AI Confidence: **99.24%**
1810. **`src/tools/clippy/clippy_lints_internal/src/unnecessary_def_path.rs`** -> AI Confidence: **99.24%**
1811. **`src/tools/clippy/clippy_utils/src/attrs.rs`** -> AI Confidence: **99.24%**
1812. **`src/tools/clippy/clippy_utils/src/higher.rs`** -> AI Confidence: **99.24%**
1813. **`src/tools/clippy/clippy_utils/src/macros.rs`** -> AI Confidence: **99.24%**
1814. **`src/tools/clippy/clippy_utils/src/mir/mod.rs`** -> AI Confidence: **99.24%**
1815. **`src/tools/clippy/clippy_utils/src/paths.rs`** -> AI Confidence: **99.24%**
1816. **`src/tools/clippy/clippy_utils/src/res.rs`** -> AI Confidence: **99.24%**
1817. **`src/tools/clippy/clippy_utils/src/source.rs`** -> AI Confidence: **99.24%**
1818. **`src/tools/clippy/clippy_utils/src/str_utils.rs`** -> AI Confidence: **99.24%**
1819. **`src/tools/clippy/clippy_utils/src/ty/type_certainty/mod.rs`** -> AI Confidence: **99.24%**
1820. **`src/tools/clippy/clippy_utils/src/visitors.rs`** -> AI Confidence: **99.24%**
1821. **`src/tools/clippy/src/driver.rs`** -> AI Confidence: **99.24%**
1822. **`src/tools/clippy/tests/dogfood.rs`** -> AI Confidence: **99.24%**
1823. **`src/tools/linkchecker/main.rs`** -> AI Confidence: **99.24%**
1824. **`src/tools/miri/miri-script/src/util.rs`** -> AI Confidence: **99.24%**
1825. **`src/tools/miri/src/alloc_addresses/reuse_pool.rs`** -> AI Confidence: **99.24%**
1826. **`src/tools/miri/src/borrow_tracker/stacked_borrows/mod.rs`** -> AI Confidence: **99.24%**
1827. **`src/tools/miri/src/borrow_tracker/tree_borrows/tree.rs`** -> AI Confidence: **99.24%**
1828. **`src/tools/miri/src/concurrency/data_race.rs`** -> AI Confidence: **99.24%**
1829. **`src/tools/miri/src/concurrency/genmc/mod.rs`** -> AI Confidence: **99.24%**
1830. **`src/tools/miri/src/concurrency/genmc/run.rs`** -> AI Confidence: **99.24%**
1831. **`src/tools/miri/src/diagnostics.rs`** -> AI Confidence: **99.24%**
1832. **`src/tools/miri/src/eval.rs`** -> AI Confidence: **99.24%**
1833. **`src/tools/miri/src/helpers.rs`** -> AI Confidence: **99.24%**
1834. **`src/tools/miri/src/intrinsics/mod.rs`** -> AI Confidence: **99.24%**
1835. **`src/tools/miri/src/machine.rs`** -> AI Confidence: **99.24%**
1836. **`src/tools/miri/src/operator.rs`** -> AI Confidence: **99.24%**
1837. **`src/tools/miri/src/shims/math.rs`** -> AI Confidence: **99.24%**
1838. **`src/tools/miri/src/shims/native_lib/trace/parent.rs`** -> AI Confidence: **99.24%**
1839. **`src/tools/miri/src/shims/time.rs`** -> AI Confidence: **99.24%**
1840. **`src/tools/miri/src/shims/tls.rs`** -> AI Confidence: **99.24%**
1841. **`src/tools/miri/src/shims/unix/env.rs`** -> AI Confidence: **99.24%**
1842. **`src/tools/miri/src/shims/unix/fd.rs`** -> AI Confidence: **99.24%**
1843. **`src/tools/miri/src/shims/unix/linux_like/epoll.rs`** -> AI Confidence: **99.24%**
1844. **`src/tools/miri/src/shims/unix/socket.rs`** -> AI Confidence: **99.24%**
1845. **`src/tools/miri/src/shims/unix/unnamed_socket.rs`** -> AI Confidence: **99.24%**
1846. **`src/tools/miri/src/shims/x86/ssse3.rs`** -> AI Confidence: **99.24%**
1847. **`src/tools/miri/tests/ui.rs`** -> AI Confidence: **99.24%**
1848. **`src/tools/rust-analyzer/crates/hir-def/src/lang_item.rs`** -> AI Confidence: **99.24%**
1849. **`src/tools/rust-analyzer/crates/hir-def/src/lib.rs`** -> AI Confidence: **99.24%**
1850. **`src/tools/rust-analyzer/crates/hir-def/src/nameres/path_resolution.rs`** -> AI Confidence: **99.24%**
1851. **`src/tools/rust-analyzer/crates/hir-def/src/resolver.rs`** -> AI Confidence: **99.24%**
1852. **`src/tools/rust-analyzer/crates/hir-def/src/visibility.rs`** -> AI Confidence: **99.24%**
1853. **`src/tools/rust-analyzer/crates/hir-expand/src/attrs.rs`** -> AI Confidence: **99.24%**
1854. **`src/tools/rust-analyzer/crates/hir-expand/src/lib.rs`** -> AI Confidence: **99.24%**
1855. **`src/tools/rust-analyzer/crates/hir-expand/src/mod_path.rs`** -> AI Confidence: **99.24%**
1856. **`src/tools/rust-analyzer/crates/hir-expand/src/name.rs`** -> AI Confidence: **99.24%**
1857. **`src/tools/rust-analyzer/crates/hir-expand/src/span_map.rs`** -> AI Confidence: **99.24%**
1858. **`src/tools/rust-analyzer/crates/hir-ty/src/dyn_compatibility.rs`** -> AI Confidence: **99.24%**
1859. **`src/tools/rust-analyzer/crates/hir-ty/src/infer/cast.rs`** -> AI Confidence: **99.24%**
1860. **`src/tools/rust-analyzer/crates/hir-ty/src/infer/mutability.rs`** -> AI Confidence: **99.24%**
1861. **`src/tools/rust-analyzer/crates/hir-ty/src/infer/op.rs`** -> AI Confidence: **99.24%**
1862. **`src/tools/rust-analyzer/crates/hir-ty/src/lib.rs`** -> AI Confidence: **99.24%**
1863. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/borrowck.rs`** -> AI Confidence: **99.24%**
1864. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/lower.rs`** -> AI Confidence: **99.24%**
1865. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/def_id.rs`** -> AI Confidence: **99.24%**
1866. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/generic_arg.rs`** -> AI Confidence: **99.24%**
1867. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/canonical/instantiate.rs`** -> AI Confidence: **99.24%**
1868. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/relate/generalize.rs`** -> AI Confidence: **99.24%**
1869. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/solver.rs`** -> AI Confidence: **99.24%**
1870. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/ty.rs`** -> AI Confidence: **99.24%**
1871. **`src/tools/rust-analyzer/crates/hir/src/attrs.rs`** -> AI Confidence: **99.24%**
1872. **`src/tools/rust-analyzer/crates/hir/src/has_source.rs`** -> AI Confidence: **99.24%**
1873. **`src/tools/rust-analyzer/crates/hir/src/semantics/source_to_def.rs`** -> AI Confidence: **99.24%**
1874. **`src/tools/rust-analyzer/crates/hir/src/term_search/expr.rs`** -> AI Confidence: **99.24%**
1875. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/add_braces.rs`** -> AI Confidence: **99.24%**
1876. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/add_missing_match_arms.rs`** -> AI Confidence: **99.24%**
1877. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_from_to_tryfrom.rs`** -> AI Confidence: **99.24%**
1878. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_into_to_from.rs`** -> AI Confidence: **99.24%**
1879. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_match_to_let_else.rs`** -> AI Confidence: **99.24%**
1880. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_to_guarded_return.rs`** -> AI Confidence: **99.24%**
1881. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/flip_or_pattern.rs`** -> AI Confidence: **99.24%**
1882. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/merge_match_arms.rs`** -> AI Confidence: **99.24%**
1883. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/remove_dbg.rs`** -> AI Confidence: **99.24%**
1884. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/replace_is_method_with_if_let_method.rs`** -> AI Confidence: **99.24%**
1885. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/replace_method_eager_lazy.rs`** -> AI Confidence: **99.24%**
1886. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/unwrap_return_type.rs`** -> AI Confidence: **99.24%**
1887. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/wrap_return_type.rs`** -> AI Confidence: **99.24%**
1888. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/wrap_unwrap_cfg_attr.rs`** -> AI Confidence: **99.24%**
1889. **`src/tools/rust-analyzer/crates/ide-assists/src/utils.rs`** -> AI Confidence: **99.24%**
1890. **`src/tools/rust-analyzer/crates/ide-assists/src/utils/ref_field_expr.rs`** -> AI Confidence: **99.24%**
1891. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/attribute/cfg.rs`** -> AI Confidence: **99.24%**
1892. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/expr.rs`** -> AI Confidence: **99.24%**
1893. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/flyimport.rs`** -> AI Confidence: **99.24%**
1894. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/fn_param.rs`** -> AI Confidence: **99.24%**
1895. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/type.rs`** -> AI Confidence: **99.24%**
1896. **`src/tools/rust-analyzer/crates/ide-completion/src/render/literal.rs`** -> AI Confidence: **99.24%**
1897. **`src/tools/rust-analyzer/crates/ide-completion/src/render/pattern.rs`** -> AI Confidence: **99.24%**
1898. **`src/tools/rust-analyzer/crates/ide-completion/src/tests/expression.rs`** -> AI Confidence: **99.24%**
1899. **`src/tools/rust-analyzer/crates/ide-db/src/imports/import_assets.rs`** -> AI Confidence: **99.24%**
1900. **`src/tools/rust-analyzer/crates/ide-db/src/imports/merge_imports.rs`** -> AI Confidence: **99.24%**
1901. **`src/tools/rust-analyzer/crates/ide-db/src/prime_caches.rs`** -> AI Confidence: **99.24%**
1902. **`src/tools/rust-analyzer/crates/ide-db/src/rename.rs`** -> AI Confidence: **99.24%**
1903. **`src/tools/rust-analyzer/crates/ide-db/src/search.rs`** -> AI Confidence: **99.24%**
1904. **`src/tools/rust-analyzer/crates/ide-db/src/syntax_helpers/node_ext.rs`** -> AI Confidence: **99.24%**
1905. **`src/tools/rust-analyzer/crates/ide-ssr/src/matching.rs`** -> AI Confidence: **99.24%**
1906. **`src/tools/rust-analyzer/crates/ide-ssr/src/parsing.rs`** -> AI Confidence: **99.24%**
1907. **`src/tools/rust-analyzer/crates/ide-ssr/src/resolving.rs`** -> AI Confidence: **99.24%**
1908. **`src/tools/rust-analyzer/crates/ide-ssr/src/search.rs`** -> AI Confidence: **99.24%**
1909. **`src/tools/rust-analyzer/crates/ide/src/doc_links.rs`** -> AI Confidence: **99.24%**
1910. **`src/tools/rust-analyzer/crates/ide/src/folding_ranges.rs`** -> AI Confidence: **99.24%**
1911. **`src/tools/rust-analyzer/crates/ide/src/hover.rs`** -> AI Confidence: **99.24%**
1912. **`src/tools/rust-analyzer/crates/ide/src/hover/render.rs`** -> AI Confidence: **99.24%**
1913. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/generic_param.rs`** -> AI Confidence: **99.24%**
1914. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/implicit_drop.rs`** -> AI Confidence: **99.24%**
1915. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/param_name.rs`** -> AI Confidence: **99.24%**
1916. **`src/tools/rust-analyzer/crates/ide/src/join_lines.rs`** -> AI Confidence: **99.24%**
1917. **`src/tools/rust-analyzer/crates/ide/src/moniker.rs`** -> AI Confidence: **99.24%**
1918. **`src/tools/rust-analyzer/crates/ide/src/navigation_target.rs`** -> AI Confidence: **99.24%**
1919. **`src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/inject.rs`** -> AI Confidence: **99.24%**
1920. **`src/tools/rust-analyzer/crates/mbe/src/parser.rs`** -> AI Confidence: **99.24%**
1921. **`src/tools/rust-analyzer/crates/parser/src/grammar/items/use_item.rs`** -> AI Confidence: **99.24%**
1922. **`src/tools/rust-analyzer/crates/parser/src/parser.rs`** -> AI Confidence: **99.24%**
1923. **`src/tools/rust-analyzer/crates/paths/src/lib.rs`** -> AI Confidence: **99.24%**
1924. **`src/tools/rust-analyzer/crates/proc-macro-api/src/legacy_protocol/msg/flat.rs`** -> AI Confidence: **99.24%**
1925. **`src/tools/rust-analyzer/crates/proc-macro-api/src/process.rs`** -> AI Confidence: **99.24%**
1926. **`src/tools/rust-analyzer/crates/project-model/src/build_dependencies.rs`** -> AI Confidence: **99.24%**
1927. **`src/tools/rust-analyzer/crates/project-model/src/sysroot.rs`** -> AI Confidence: **99.24%**
1928. **`src/tools/rust-analyzer/crates/project-model/src/workspace.rs`** -> AI Confidence: **99.24%**
1929. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/analysis_stats.rs`** -> AI Confidence: **99.24%**
1930. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/ssr.rs`** -> AI Confidence: **99.24%**
1931. **`src/tools/rust-analyzer/crates/rust-analyzer/src/flycheck.rs`** -> AI Confidence: **99.24%**
1932. **`src/tools/rust-analyzer/crates/rust-analyzer/src/handlers/request.rs`** -> AI Confidence: **99.24%**
1933. **`src/tools/rust-analyzer/crates/rust-analyzer/tests/slow-tests/support.rs`** -> AI Confidence: **99.24%**
1934. **`src/tools/rust-analyzer/crates/span/src/ast_id.rs`** -> AI Confidence: **99.24%**
1935. **`src/tools/rust-analyzer/crates/syntax-bridge/src/lib.rs`** -> AI Confidence: **99.24%**
1936. **`src/tools/rust-analyzer/crates/syntax/src/ast/node_ext.rs`** -> AI Confidence: **99.24%**
1937. **`src/tools/rust-analyzer/crates/syntax/src/syntax_editor/edits.rs`** -> AI Confidence: **99.24%**
1938. **`src/tools/rust-analyzer/crates/syntax/test_data/parser/fuzz-failures/0001.rs`** -> AI Confidence: **99.24%**
1939. **`src/tools/rust-analyzer/crates/tt/src/iter.rs`** -> AI Confidence: **99.24%**
1940. **`src/tools/rust-analyzer/crates/tt/src/lib.rs`** -> AI Confidence: **99.24%**
1941. **`src/tools/rust-analyzer/lib/lsp-server/examples/minimal_lsp.rs`** -> AI Confidence: **99.24%**
1942. **`src/tools/rust-analyzer/lib/smol_str/src/borsh.rs`** -> AI Confidence: **99.24%**
1943. **`src/tools/rust-analyzer/lib/smol_str/src/lib.rs`** -> AI Confidence: **99.24%**
1944. **`src/tools/rust-analyzer/lib/ungrammar/src/parser.rs`** -> AI Confidence: **99.24%**
1945. **`src/tools/rust-analyzer/xtask/src/dist.rs`** -> AI Confidence: **99.24%**
1946. **`src/tools/rust-analyzer/xtask/src/metrics.rs`** -> AI Confidence: **99.24%**
1947. **`src/tools/rust-installer/src/compression.rs`** -> AI Confidence: **99.24%**
1948. **`src/tools/rustfmt/src/attr.rs`** -> AI Confidence: **99.24%**
1949. **`src/tools/rustfmt/src/chains.rs`** -> AI Confidence: **99.24%**
1950. **`src/tools/rustfmt/src/closures.rs`** -> AI Confidence: **99.24%**
1951. **`src/tools/rustfmt/src/config/config_type.rs`** -> AI Confidence: **99.24%**
1952. **`src/tools/rustfmt/src/config/file_lines.rs`** -> AI Confidence: **99.24%**
1953. **`src/tools/rustfmt/src/expr.rs`** -> AI Confidence: **99.24%**
1954. **`src/tools/rustfmt/src/formatting.rs`** -> AI Confidence: **99.24%**
1955. **`src/tools/rustfmt/src/items.rs`** -> AI Confidence: **99.24%**
1956. **`src/tools/rustfmt/src/macros.rs`** -> AI Confidence: **99.24%**
1957. **`src/tools/rustfmt/src/missed_spans.rs`** -> AI Confidence: **99.24%**
1958. **`src/tools/rustfmt/src/pairs.rs`** -> AI Confidence: **99.24%**
1959. **`src/tools/rustfmt/src/parse/macros/cfg_if.rs`** -> AI Confidence: **99.24%**
1960. **`src/tools/rustfmt/src/patterns.rs`** -> AI Confidence: **99.24%**
1961. **`src/tools/tidy/src/bins.rs`** -> AI Confidence: **99.24%**
1962. **`src/tools/tidy/src/extra_checks/mod.rs`** -> AI Confidence: **99.24%**
1963. **`src/tools/tidy/src/features.rs`** -> AI Confidence: **99.24%**
1964. **`tests/run-make/apple-deployment-target/rmake.rs`** -> AI Confidence: **99.24%**
1965. **`tests/run-make/cross-lang-lto/rmake.rs`** -> AI Confidence: **99.24%**
1966. **`src/ci/docker/scripts/fuchsia-test-runner.py`** -> AI Confidence: **99.24%**
1967. **`src/tools/publish_toolstate.py`** -> AI Confidence: **99.24%**
1968. **`src/ci/docker/scripts/qemu-bare-bones-addentropy.c`** -> AI Confidence: **99.24%**
1969. **`compiler/rustc_llvm/llvm-wrapper/PassWrapper.cpp`** -> AI Confidence: **99.24%**
1970. **`compiler/rustc_llvm/llvm-wrapper/RustWrapper.cpp`** -> AI Confidence: **99.24%**
1971. **`compiler/rustc_ast/src/attr/data_structures.rs`** -> AI Confidence: **99.23%**
1972. **`compiler/rustc_ast/src/attr/version.rs`** -> AI Confidence: **99.23%**
1973. **`compiler/rustc_codegen_cranelift/build_system/abi_cafe.rs`** -> AI Confidence: **99.23%**
1974. **`compiler/rustc_graphviz/src/lib.rs`** -> AI Confidence: **99.23%**
1975. **`compiler/rustc_middle/src/mir/graphviz.rs`** -> AI Confidence: **99.23%**
1976. **`compiler/rustc_middle/src/mir/interpret/pointer.rs`** -> AI Confidence: **99.23%**
1977. **`compiler/rustc_middle/src/verify_ich.rs`** -> AI Confidence: **99.23%**
1978. **`compiler/rustc_mir_transform/src/check_inline_always_target_features.rs`** -> AI Confidence: **99.23%**
1979. **`compiler/rustc_mir_transform/src/cost_checker.rs`** -> AI Confidence: **99.23%**
1980. **`compiler/rustc_parse/src/lexer/diagnostics.rs`** -> AI Confidence: **99.23%**
1981. **`compiler/rustc_target/src/callconv/xtensa.rs`** -> AI Confidence: **99.23%**
1982. **`compiler/rustc_ty_utils/src/representability.rs`** -> AI Confidence: **99.23%**
1983. **`library/compiler-builtins/libm/src/math/generic/ceil.rs`** -> AI Confidence: **99.23%**
1984. **`library/compiler-builtins/libm/src/math/support/int_traits/narrowing_div.rs`** -> AI Confidence: **99.23%**
1985. **`library/core/src/tuple.rs`** -> AI Confidence: **99.23%**
1986. **`library/std/src/net/test.rs`** -> AI Confidence: **99.23%**
1987. **`library/test/src/test_result.rs`** -> AI Confidence: **99.23%**
1988. **`src/bootstrap/src/core/builder/cli_paths.rs`** -> AI Confidence: **99.23%**
1989. **`src/build_helper/src/npm.rs`** -> AI Confidence: **99.23%**
1990. **`src/ci/citool/src/metrics.rs`** -> AI Confidence: **99.23%**
1991. **`src/librustdoc/docfs.rs`** -> AI Confidence: **99.23%**
1992. **`src/librustdoc/theme.rs`** -> AI Confidence: **99.23%**
1993. **`src/tools/bump-stage0/src/main.rs`** -> AI Confidence: **99.23%**
1994. **`src/tools/clippy/clippy_lints/src/doc/needless_doctest_main.rs`** -> AI Confidence: **99.23%**
1995. **`src/tools/clippy/clippy_lints/src/ifs/same_functions_in_if_cond.rs`** -> AI Confidence: **99.23%**
1996. **`src/tools/clippy/clippy_lints/src/matches/rest_pat_in_fully_bound_struct.rs`** -> AI Confidence: **99.23%**
1997. **`src/tools/clippy/clippy_lints/src/misc_early/unneeded_wildcard_pattern.rs`** -> AI Confidence: **99.23%**
1998. **`src/tools/clippy/clippy_lints/src/partialeq_ne_impl.rs`** -> AI Confidence: **99.23%**
1999. **`src/tools/clippy/clippy_lints/src/trailing_empty_array.rs`** -> AI Confidence: **99.23%**
2000. **`src/tools/clippy/tests/ui/significant_drop_in_scrutinee.rs`** -> AI Confidence: **99.23%**
2001. **`src/tools/compiletest/src/runtest/codegen_units.rs`** -> AI Confidence: **99.23%**
2002. **`src/tools/generate-windows-sys/src/main.rs`** -> AI Confidence: **99.23%**
2003. **`src/tools/miri/src/shims/unix/android/thread.rs`** -> AI Confidence: **99.23%**
2004. **`src/tools/opt-dist/src/bolt.rs`** -> AI Confidence: **99.23%**
2005. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/extern_block.rs`** -> AI Confidence: **99.23%**
2006. **`src/tools/rust-analyzer/crates/ide/src/view_mir.rs`** -> AI Confidence: **99.23%**
2007. **`src/tools/rustfmt/src/parse/macros/cfg_match.rs`** -> AI Confidence: **99.23%**
2008. **`src/tools/rustfmt/src/spanned.rs`** -> AI Confidence: **99.23%**
2009. **`src/tools/tidy/src/error_codes.rs`** -> AI Confidence: **99.23%**
2010. **`tests/run-make/remove-dir-all-race/rmake.rs`** -> AI Confidence: **99.23%**
2011. **`tests/ui/consts/references.rs`** -> AI Confidence: **99.23%**
2012. **`tests/ui/iterators/string.rs`** -> AI Confidence: **99.23%**
2013. **`tests/ui/pattern/deref-patterns/branch.rs`** -> AI Confidence: **99.23%**
2014. **`tests/ui/process/core-run-destroy.rs`** -> AI Confidence: **99.23%**
2015. **`tests/ui/rfcs/rfc-0000-never_patterns/check.rs`** -> AI Confidence: **99.23%**
2016. **`src/ci/docker/host-x86_64/dist-x86_64-linux/dist.sh`** -> AI Confidence: **99.23%**
2017. **`src/ci/shared.sh`** -> AI Confidence: **99.23%**
2018. **`src/ci/docker/scripts/android-sdk-manager.py`** -> AI Confidence: **99.23%**
2019. **`src/tools/clippy/util/gh-pages/theme.js`** -> AI Confidence: **99.23%**
2020. **`src/tools/rust-analyzer/editors/code/src/run.ts`** -> AI Confidence: **99.23%**
2021. **`src/tools/rust-analyzer/editors/code/src/toolchain.ts`** -> AI Confidence: **99.23%**
2022. **`tests/ui/consts/std/iter.rs`** -> AI Confidence: **99.22%**
2023. **`src/tools/clippy/tests/ui/infinite_loops.rs`** -> AI Confidence: **99.2%**
2024. **`src/tools/miri/tests/pass/path.rs`** -> AI Confidence: **99.2%**
2025. **`src/tools/run-make-support/src/targets.rs`** -> AI Confidence: **99.2%**
2026. **`compiler/rustc_abi/src/layout/coroutine.rs`** -> AI Confidence: **99.18%**
2027. **`compiler/rustc_arena/src/lib.rs`** -> AI Confidence: **99.18%**
2028. **`compiler/rustc_ast/src/ast_traits.rs`** -> AI Confidence: **99.18%**
2029. **`compiler/rustc_ast_lowering/src/delegation/generics.rs`** -> AI Confidence: **99.18%**
2030. **`compiler/rustc_ast_lowering/src/item.rs`** -> AI Confidence: **99.18%**
2031. **`compiler/rustc_ast_lowering/src/lib.rs`** -> AI Confidence: **99.18%**
2032. **`compiler/rustc_attr_parsing/src/attributes/autodiff.rs`** -> AI Confidence: **99.18%**
2033. **`compiler/rustc_attr_parsing/src/attributes/diagnostic/on_move.rs`** -> AI Confidence: **99.18%**
2034. **`compiler/rustc_attr_parsing/src/attributes/link_attrs.rs`** -> AI Confidence: **99.18%**
2035. **`compiler/rustc_attr_parsing/src/attributes/prototype.rs`** -> AI Confidence: **99.18%**
2036. **`compiler/rustc_attr_parsing/src/attributes/rustc_dump.rs`** -> AI Confidence: **99.18%**
2037. **`compiler/rustc_attr_parsing/src/attributes/stability.rs`** -> AI Confidence: **99.18%**
2038. **`compiler/rustc_borrowck/src/borrow_set.rs`** -> AI Confidence: **99.18%**
2039. **`compiler/rustc_borrowck/src/nll.rs`** -> AI Confidence: **99.18%**
2040. **`compiler/rustc_borrowck/src/polonius/constraints.rs`** -> AI Confidence: **99.18%**
2041. **`compiler/rustc_borrowck/src/region_infer/graphviz.rs`** -> AI Confidence: **99.18%**
2042. **`compiler/rustc_borrowck/src/region_infer/values.rs`** -> AI Confidence: **99.18%**
2043. **`compiler/rustc_borrowck/src/renumber.rs`** -> AI Confidence: **99.18%**
2044. **`compiler/rustc_borrowck/src/type_check/free_region_relations.rs`** -> AI Confidence: **99.18%**
2045. **`compiler/rustc_borrowck/src/type_check/relate_tys.rs`** -> AI Confidence: **99.18%**
2046. **`compiler/rustc_borrowck/src/used_muts.rs`** -> AI Confidence: **99.18%**
2047. **`compiler/rustc_builtin_macros/src/alloc_error_handler.rs`** -> AI Confidence: **99.18%**
2048. **`compiler/rustc_builtin_macros/src/cfg_select.rs`** -> AI Confidence: **99.18%**
2049. **`compiler/rustc_builtin_macros/src/deriving/cmp/eq.rs`** -> AI Confidence: **99.18%**
2050. **`compiler/rustc_builtin_macros/src/deriving/cmp/partial_eq.rs`** -> AI Confidence: **99.18%**
2051. **`compiler/rustc_builtin_macros/src/deriving/coerce_pointee.rs`** -> AI Confidence: **99.18%**
2052. **`compiler/rustc_builtin_macros/src/deriving/from.rs`** -> AI Confidence: **99.18%**
2053. **`compiler/rustc_builtin_macros/src/iter.rs`** -> AI Confidence: **99.18%**
2054. **`compiler/rustc_builtin_macros/src/source_util.rs`** -> AI Confidence: **99.18%**
2055. **`compiler/rustc_builtin_macros/src/standard_library_imports.rs`** -> AI Confidence: **99.18%**
2056. **`compiler/rustc_codegen_cranelift/build_system/build_backend.rs`** -> AI Confidence: **99.18%**
2057. **`compiler/rustc_codegen_cranelift/build_system/tests.rs`** -> AI Confidence: **99.18%**
2058. **`compiler/rustc_codegen_cranelift/src/base.rs`** -> AI Confidence: **99.18%**
2059. **`compiler/rustc_codegen_cranelift/src/concurrency_limiter.rs`** -> AI Confidence: **99.18%**
2060. **`compiler/rustc_codegen_cranelift/src/debuginfo/line_info.rs`** -> AI Confidence: **99.18%**
2061. **`compiler/rustc_codegen_cranelift/src/driver/aot.rs`** -> AI Confidence: **99.18%**
2062. **`compiler/rustc_codegen_cranelift/src/value_and_place.rs`** -> AI Confidence: **99.18%**
2063. **`compiler/rustc_codegen_gcc/build_system/src/utils.rs`** -> AI Confidence: **99.18%**
2064. **`compiler/rustc_codegen_gcc/example/alloc_system.rs`** -> AI Confidence: **99.18%**
2065. **`compiler/rustc_codegen_gcc/src/builder.rs`** -> AI Confidence: **99.18%**
2066. **`compiler/rustc_codegen_gcc/src/debuginfo.rs`** -> AI Confidence: **99.18%**
2067. **`compiler/rustc_codegen_gcc/src/declare.rs`** -> AI Confidence: **99.18%**
2068. **`compiler/rustc_codegen_gcc/src/intrinsic/mod.rs`** -> AI Confidence: **99.18%**
2069. **`compiler/rustc_codegen_gcc/src/intrinsic/simd.rs`** -> AI Confidence: **99.18%**
2070. **`compiler/rustc_codegen_gcc/src/mono_item.rs`** -> AI Confidence: **99.18%**
2071. **`compiler/rustc_codegen_llvm/src/back/archive.rs`** -> AI Confidence: **99.18%**
2072. **`compiler/rustc_codegen_llvm/src/builder.rs`** -> AI Confidence: **99.18%**
2073. **`compiler/rustc_codegen_llvm/src/coverageinfo/mapgen/covfun.rs`** -> AI Confidence: **99.18%**
2074. **`compiler/rustc_codegen_llvm/src/debuginfo/create_scope_map.rs`** -> AI Confidence: **99.18%**
2075. **`compiler/rustc_codegen_llvm/src/debuginfo/gdb.rs`** -> AI Confidence: **99.18%**
2076. **`compiler/rustc_codegen_llvm/src/debuginfo/metadata/enums/cpp_like.rs`** -> AI Confidence: **99.18%**
2077. **`compiler/rustc_codegen_llvm/src/debuginfo/metadata/enums/mod.rs`** -> AI Confidence: **99.18%**
2078. **`compiler/rustc_codegen_llvm/src/debuginfo/metadata/enums/native.rs`** -> AI Confidence: **99.18%**
2079. **`compiler/rustc_codegen_llvm/src/debuginfo/metadata/type_map.rs`** -> AI Confidence: **99.18%**
2080. **`compiler/rustc_codegen_llvm/src/debuginfo/mod.rs`** -> AI Confidence: **99.18%**
2081. **`compiler/rustc_codegen_llvm/src/errors.rs`** -> AI Confidence: **99.18%**
2082. **`compiler/rustc_codegen_llvm/src/mono_item.rs`** -> AI Confidence: **99.18%**
2083. **`compiler/rustc_codegen_llvm/src/type_.rs`** -> AI Confidence: **99.18%**
2084. **`compiler/rustc_codegen_llvm/src/typetree.rs`** -> AI Confidence: **99.18%**
2085. **`compiler/rustc_codegen_llvm/src/va_arg.rs`** -> AI Confidence: **99.18%**
2086. **`compiler/rustc_codegen_ssa/src/errors.rs`** -> AI Confidence: **99.18%**
2087. **`compiler/rustc_codegen_ssa/src/mir/intrinsic.rs`** -> AI Confidence: **99.18%**
2088. **`compiler/rustc_codegen_ssa/src/mir/locals.rs`** -> AI Confidence: **99.18%**
2089. **`compiler/rustc_codegen_ssa/src/mir/mod.rs`** -> AI Confidence: **99.18%**
2090. **`compiler/rustc_codegen_ssa/src/traits/debuginfo.rs`** -> AI Confidence: **99.18%**
2091. **`compiler/rustc_codegen_ssa/src/traits/type_.rs`** -> AI Confidence: **99.18%**
2092. **`compiler/rustc_const_eval/src/check_consts/post_drop_elaboration.rs`** -> AI Confidence: **99.18%**
2093. **`compiler/rustc_const_eval/src/const_eval/dummy_machine.rs`** -> AI Confidence: **99.18%**
2094. **`compiler/rustc_const_eval/src/const_eval/error.rs`** -> AI Confidence: **99.18%**
2095. **`compiler/rustc_const_eval/src/interpret/util.rs`** -> AI Confidence: **99.18%**
2096. **`compiler/rustc_const_eval/src/util/caller_location.rs`** -> AI Confidence: **99.18%**
2097. **`compiler/rustc_data_structures/src/fingerprint.rs`** -> AI Confidence: **99.18%**
2098. **`compiler/rustc_data_structures/src/graph/iterate/mod.rs`** -> AI Confidence: **99.18%**
2099. **`compiler/rustc_data_structures/src/graph/scc/mod.rs`** -> AI Confidence: **99.18%**
2100. **`compiler/rustc_data_structures/src/sharded.rs`** -> AI Confidence: **99.18%**
2101. **`compiler/rustc_data_structures/src/stable_hasher.rs`** -> AI Confidence: **99.18%**
2102. **`compiler/rustc_data_structures/src/sync.rs`** -> AI Confidence: **99.18%**
2103. **`compiler/rustc_data_structures/src/sync/worker_local.rs`** -> AI Confidence: **99.18%**
2104. **`compiler/rustc_data_structures/src/transitive_relation.rs`** -> AI Confidence: **99.18%**
2105. **`compiler/rustc_data_structures/src/unord.rs`** -> AI Confidence: **99.18%**
2106. **`compiler/rustc_data_structures/src/vec_cache.rs`** -> AI Confidence: **99.18%**
2107. **`compiler/rustc_driver_impl/src/pretty.rs`** -> AI Confidence: **99.18%**
2108. **`compiler/rustc_driver_impl/src/signal_handler.rs`** -> AI Confidence: **99.18%**
2109. **`compiler/rustc_errors/src/decorate_diag.rs`** -> AI Confidence: **99.18%**
2110. **`compiler/rustc_errors/src/formatting.rs`** -> AI Confidence: **99.18%**
2111. **`compiler/rustc_expand/src/proc_macro.rs`** -> AI Confidence: **99.18%**
2112. **`compiler/rustc_feature/src/unstable.rs`** -> AI Confidence: **99.18%**
2113. **`compiler/rustc_fs_util/src/lib.rs`** -> AI Confidence: **99.18%**
2114. **`compiler/rustc_hir/src/attrs/data_structures.rs`** -> AI Confidence: **99.18%**
2115. **`compiler/rustc_hir/src/attrs/diagnostic.rs`** -> AI Confidence: **99.18%**
2116. **`compiler/rustc_hir/src/limit.rs`** -> AI Confidence: **99.18%**
2117. **`compiler/rustc_hir/src/stable_hash_impls.rs`** -> AI Confidence: **99.18%**
2118. **`compiler/rustc_hir_analysis/src/delegation.rs`** -> AI Confidence: **99.18%**
2119. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/dyn_trait.rs`** -> AI Confidence: **99.18%**
2120. **`compiler/rustc_hir_analysis/src/outlives/implicit_infer.rs`** -> AI Confidence: **99.18%**
2121. **`compiler/rustc_hir_analysis/src/outlives/utils.rs`** -> AI Confidence: **99.18%**
2122. **`compiler/rustc_hir_analysis/src/variance/terms.rs`** -> AI Confidence: **99.18%**
2123. **`compiler/rustc_hir_typeck/src/errors.rs`** -> AI Confidence: **99.18%**
2124. **`compiler/rustc_hir_typeck/src/fn_ctxt/inspect_obligations.rs`** -> AI Confidence: **99.18%**
2125. **`compiler/rustc_hir_typeck/src/gather_locals.rs`** -> AI Confidence: **99.18%**
2126. **`compiler/rustc_hir_typeck/src/opaque_types.rs`** -> AI Confidence: **99.18%**
2127. **`compiler/rustc_incremental/src/persist/load.rs`** -> AI Confidence: **99.18%**
2128. **`compiler/rustc_infer/src/infer/canonical/mod.rs`** -> AI Confidence: **99.18%**
2129. **`compiler/rustc_infer/src/infer/snapshot/undo_log.rs`** -> AI Confidence: **99.18%**
2130. **`compiler/rustc_infer/src/infer/type_variable.rs`** -> AI Confidence: **99.18%**
2131. **`compiler/rustc_infer/src/traits/util.rs`** -> AI Confidence: **99.18%**
2132. **`compiler/rustc_interface/src/interface.rs`** -> AI Confidence: **99.18%**
2133. **`compiler/rustc_interface/src/passes.rs`** -> AI Confidence: **99.18%**
2134. **`compiler/rustc_lint/src/async_fn_in_trait.rs`** -> AI Confidence: **99.18%**
2135. **`compiler/rustc_lint/src/default_could_be_derived.rs`** -> AI Confidence: **99.18%**
2136. **`compiler/rustc_lint/src/errors.rs`** -> AI Confidence: **99.18%**
2137. **`compiler/rustc_lint/src/expect.rs`** -> AI Confidence: **99.18%**
2138. **`compiler/rustc_lint/src/function_cast_as_integer.rs`** -> AI Confidence: **99.18%**
2139. **`compiler/rustc_lint/src/gpukernel_abi.rs`** -> AI Confidence: **99.18%**
2140. **`compiler/rustc_lint/src/impl_trait_overcaptures.rs`** -> AI Confidence: **99.18%**
2141. **`compiler/rustc_lint/src/lints.rs`** -> AI Confidence: **99.18%**
2142. **`compiler/rustc_lint/src/opaque_hidden_inferred_bound.rs`** -> AI Confidence: **99.18%**
2143. **`compiler/rustc_lint/src/precedence.rs`** -> AI Confidence: **99.18%**
2144. **`compiler/rustc_macros/src/diagnostics/error.rs`** -> AI Confidence: **99.18%**
2145. **`compiler/rustc_metadata/src/foreign_modules.rs`** -> AI Confidence: **99.18%**
2146. **`compiler/rustc_metadata/src/rmeta/def_path_hash_map.rs`** -> AI Confidence: **99.18%**
2147. **`compiler/rustc_middle/src/dep_graph/mod.rs`** -> AI Confidence: **99.18%**
2148. **`compiler/rustc_middle/src/hir/mod.rs`** -> AI Confidence: **99.18%**
2149. **`compiler/rustc_middle/src/hooks/mod.rs`** -> AI Confidence: **99.18%**
2150. **`compiler/rustc_middle/src/ich/hcx.rs`** -> AI Confidence: **99.18%**
2151. **`compiler/rustc_middle/src/ich/impls_syntax.rs`** -> AI Confidence: **99.18%**
2152. **`compiler/rustc_middle/src/mir/basic_blocks.rs`** -> AI Confidence: **99.18%**
2153. **`compiler/rustc_middle/src/mir/interpret/allocation.rs`** -> AI Confidence: **99.18%**
2154. **`compiler/rustc_middle/src/mir/terminator.rs`** -> AI Confidence: **99.18%**
2155. **`compiler/rustc_middle/src/query/caches.rs`** -> AI Confidence: **99.18%**
2156. **`compiler/rustc_middle/src/query/erase.rs`** -> AI Confidence: **99.18%**
2157. **`compiler/rustc_middle/src/query/job.rs`** -> AI Confidence: **99.18%**
2158. **`compiler/rustc_middle/src/query/plumbing.rs`** -> AI Confidence: **99.18%**
2159. **`compiler/rustc_middle/src/traits/mod.rs`** -> AI Confidence: **99.18%**
2160. **`compiler/rustc_middle/src/ty/abstract_const.rs`** -> AI Confidence: **99.18%**
2161. **`compiler/rustc_middle/src/ty/codec.rs`** -> AI Confidence: **99.18%**
2162. **`compiler/rustc_middle/src/ty/diagnostics.rs`** -> AI Confidence: **99.18%**
2163. **`compiler/rustc_middle/src/ty/error.rs`** -> AI Confidence: **99.18%**
2164. **`compiler/rustc_middle/src/ty/fold.rs`** -> AI Confidence: **99.18%**
2165. **`compiler/rustc_middle/src/ty/list.rs`** -> AI Confidence: **99.18%**
2166. **`compiler/rustc_middle/src/ty/normalize_erasing_regions.rs`** -> AI Confidence: **99.18%**
2167. **`compiler/rustc_middle/src/ty/predicate.rs`** -> AI Confidence: **99.18%**
2168. **`compiler/rustc_middle/src/ty/trait_def.rs`** -> AI Confidence: **99.18%**
2169. **`compiler/rustc_middle/src/ty/visit.rs`** -> AI Confidence: **99.18%**
2170. **`compiler/rustc_middle/src/ty/vtable.rs`** -> AI Confidence: **99.18%**
2171. **`compiler/rustc_mir_build/src/builder/expr/as_operand.rs`** -> AI Confidence: **99.18%**
2172. **`compiler/rustc_mir_build/src/builder/expr/as_place.rs`** -> AI Confidence: **99.18%**
2173. **`compiler/rustc_mir_build/src/builder/expr/as_rvalue.rs`** -> AI Confidence: **99.18%**
2174. **`compiler/rustc_mir_build/src/builder/expr/into.rs`** -> AI Confidence: **99.18%**
2175. **`compiler/rustc_mir_build/src/builder/expr/stmt.rs`** -> AI Confidence: **99.18%**
2176. **`compiler/rustc_mir_build/src/thir/cx/mod.rs`** -> AI Confidence: **99.18%**
2177. **`compiler/rustc_mir_build/src/thir/pattern/mod.rs`** -> AI Confidence: **99.18%**
2178. **`compiler/rustc_mir_dataflow/src/drop_flag_effects.rs`** -> AI Confidence: **99.18%**
2179. **`compiler/rustc_mir_dataflow/src/framework/direction.rs`** -> AI Confidence: **99.18%**
2180. **`compiler/rustc_mir_dataflow/src/framework/mod.rs`** -> AI Confidence: **99.18%**
2181. **`compiler/rustc_mir_dataflow/src/impls/storage_liveness.rs`** -> AI Confidence: **99.18%**
2182. **`compiler/rustc_mir_dataflow/src/move_paths/mod.rs`** -> AI Confidence: **99.18%**
2183. **`compiler/rustc_mir_transform/src/check_packed_ref.rs`** -> AI Confidence: **99.18%**
2184. **`compiler/rustc_mir_transform/src/elaborate_box_derefs.rs`** -> AI Confidence: **99.18%**
2185. **`compiler/rustc_mir_transform/src/errors.rs`** -> AI Confidence: **99.18%**
2186. **`compiler/rustc_mir_transform/src/lib.rs`** -> AI Confidence: **99.18%**
2187. **`compiler/rustc_mir_transform/src/mentioned_items.rs`** -> AI Confidence: **99.18%**
2188. **`compiler/rustc_mir_transform/src/prettify.rs`** -> AI Confidence: **99.18%**
2189. **`compiler/rustc_mir_transform/src/shim.rs`** -> AI Confidence: **99.18%**
2190. **`compiler/rustc_mir_transform/src/unreachable_prop.rs`** -> AI Confidence: **99.18%**
2191. **`compiler/rustc_monomorphize/src/graph_checks/statics.rs`** -> AI Confidence: **99.18%**
2192. **`compiler/rustc_monomorphize/src/mono_checks/move_check.rs`** -> AI Confidence: **99.18%**
2193. **`compiler/rustc_next_trait_solver/src/canonical/mod.rs`** -> AI Confidence: **99.18%**
2194. **`compiler/rustc_next_trait_solver/src/solve/inspect/build.rs`** -> AI Confidence: **99.18%**
2195. **`compiler/rustc_next_trait_solver/src/solve/normalizes_to/opaque_types.rs`** -> AI Confidence: **99.18%**
2196. **`compiler/rustc_parse/src/errors.rs`** -> AI Confidence: **99.18%**
2197. **`compiler/rustc_parse/src/parser/tokenstream/tests.rs`** -> AI Confidence: **99.18%**
2198. **`compiler/rustc_passes/src/diagnostic_items.rs`** -> AI Confidence: **99.18%**
2199. **`compiler/rustc_passes/src/entry.rs`** -> AI Confidence: **99.18%**
2200. **`compiler/rustc_passes/src/lib_features.rs`** -> AI Confidence: **99.18%**
2201. **`compiler/rustc_pattern_analysis/src/errors.rs`** -> AI Confidence: **99.18%**
2202. **`compiler/rustc_pattern_analysis/src/lib.rs`** -> AI Confidence: **99.18%**
2203. **`compiler/rustc_public/src/mir/alloc.rs`** -> AI Confidence: **99.18%**
2204. **`compiler/rustc_public/src/mir/body.rs`** -> AI Confidence: **99.18%**
2205. **`compiler/rustc_public/src/rustc_internal/mod.rs`** -> AI Confidence: **99.18%**
2206. **`compiler/rustc_public/src/unstable/convert/internal.rs`** -> AI Confidence: **99.18%**
2207. **`compiler/rustc_public/src/unstable/convert/stable/mod.rs`** -> AI Confidence: **99.18%**
2208. **`compiler/rustc_public/src/unstable/convert/stable/ty.rs`** -> AI Confidence: **99.18%**
2209. **`compiler/rustc_public/src/unstable/internal_cx/mod.rs`** -> AI Confidence: **99.18%**
2210. **`compiler/rustc_public_bridge/src/alloc.rs`** -> AI Confidence: **99.18%**
2211. **`compiler/rustc_query_impl/src/query_impl.rs`** -> AI Confidence: **99.18%**
2212. **`compiler/rustc_sanitizers/src/cfi/typeid/itanium_cxx_abi/encode.rs`** -> AI Confidence: **99.18%**
2213. **`compiler/rustc_serialize/src/opaque.rs`** -> AI Confidence: **99.18%**
2214. **`compiler/rustc_session/src/errors.rs`** -> AI Confidence: **99.18%**
2215. **`compiler/rustc_span/src/caching_source_map_view.rs`** -> AI Confidence: **99.18%**
2216. **`compiler/rustc_span/src/hygiene.rs`** -> AI Confidence: **99.18%**
2217. **`compiler/rustc_span/src/span_encoding.rs`** -> AI Confidence: **99.18%**
2218. **`compiler/rustc_target/src/spec/base/nto_qnx.rs`** -> AI Confidence: **99.18%**
2219. **`compiler/rustc_thread_pool/src/job.rs`** -> AI Confidence: **99.18%**
2220. **`compiler/rustc_thread_pool/src/spawn/tests.rs`** -> AI Confidence: **99.18%**
2221. **`compiler/rustc_thread_pool/src/thread_pool/tests.rs`** -> AI Confidence: **99.18%**
2222. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/mod.rs`** -> AI Confidence: **99.18%**
2223. **`compiler/rustc_trait_selection/src/error_reporting/traits/ambiguity.rs`** -> AI Confidence: **99.18%**
2224. **`compiler/rustc_trait_selection/src/errors.rs`** -> AI Confidence: **99.18%**
2225. **`compiler/rustc_trait_selection/src/regions.rs`** -> AI Confidence: **99.18%**
2226. **`compiler/rustc_trait_selection/src/solve/delegate.rs`** -> AI Confidence: **99.18%**
2227. **`compiler/rustc_trait_selection/src/solve/inspect/analyse.rs`** -> AI Confidence: **99.18%**
2228. **`compiler/rustc_trait_selection/src/traits/mod.rs`** -> AI Confidence: **99.18%**
2229. **`compiler/rustc_trait_selection/src/traits/normalize.rs`** -> AI Confidence: **99.18%**
2230. **`compiler/rustc_trait_selection/src/traits/query/type_op/ascribe_user_type.rs`** -> AI Confidence: **99.18%**
2231. **`compiler/rustc_trait_selection/src/traits/query/type_op/custom.rs`** -> AI Confidence: **99.18%**
2232. **`compiler/rustc_trait_selection/src/traits/query/type_op/prove_predicate.rs`** -> AI Confidence: **99.18%**
2233. **`compiler/rustc_trait_selection/src/traits/select/_match.rs`** -> AI Confidence: **99.18%**
2234. **`compiler/rustc_trait_selection/src/traits/select/confirmation.rs`** -> AI Confidence: **99.18%**
2235. **`compiler/rustc_trait_selection/src/traits/structural_normalize.rs`** -> AI Confidence: **99.18%**
2236. **`compiler/rustc_traits/src/normalize_erasing_regions.rs`** -> AI Confidence: **99.18%**
2237. **`compiler/rustc_transmute/src/layout/dfa.rs`** -> AI Confidence: **99.18%**
2238. **`compiler/rustc_ty_utils/src/assoc.rs`** -> AI Confidence: **99.18%**
2239. **`compiler/rustc_ty_utils/src/implied_bounds.rs`** -> AI Confidence: **99.18%**
2240. **`compiler/rustc_type_ir/src/error.rs`** -> AI Confidence: **99.18%**
2241. **`compiler/rustc_type_ir/src/infer_ctxt.rs`** -> AI Confidence: **99.18%**
2242. **`compiler/rustc_type_ir/src/ir_print.rs`** -> AI Confidence: **99.18%**
2243. **`compiler/rustc_type_ir/src/region_kind.rs`** -> AI Confidence: **99.18%**
2244. **`compiler/rustc_type_ir/src/ty_info.rs`** -> AI Confidence: **99.18%**
2245. **`library/alloc/src/boxed/convert.rs`** -> AI Confidence: **99.18%**
2246. **`library/alloc/src/boxed/iter.rs`** -> AI Confidence: **99.18%**
2247. **`library/alloc/src/boxed/thin.rs`** -> AI Confidence: **99.18%**
2248. **`library/alloc/src/collections/btree/map.rs`** -> AI Confidence: **99.18%**
2249. **`library/alloc/src/collections/btree/map/entry.rs`** -> AI Confidence: **99.18%**
2250. **`library/alloc/src/collections/btree/map/tests.rs`** -> AI Confidence: **99.18%**
2251. **`library/alloc/src/collections/btree/navigate.rs`** -> AI Confidence: **99.18%**
2252. **`library/alloc/src/collections/btree/remove.rs`** -> AI Confidence: **99.18%**
2253. **`library/alloc/src/collections/btree/set.rs`** -> AI Confidence: **99.18%**
2254. **`library/alloc/src/collections/btree/set/entry.rs`** -> AI Confidence: **99.18%**
2255. **`library/alloc/src/collections/vec_deque/into_iter.rs`** -> AI Confidence: **99.18%**
2256. **`library/alloc/src/collections/vec_deque/iter.rs`** -> AI Confidence: **99.18%**
2257. **`library/alloc/src/collections/vec_deque/iter_mut.rs`** -> AI Confidence: **99.18%**
2258. **`library/alloc/src/collections/vec_deque/mod.rs`** -> AI Confidence: **99.18%**
2259. **`library/alloc/src/collections/vec_deque/spec_extend.rs`** -> AI Confidence: **99.18%**
2260. **`library/alloc/src/task.rs`** -> AI Confidence: **99.18%**
2261. **`library/alloc/src/vec/drain.rs`** -> AI Confidence: **99.18%**
2262. **`library/alloc/src/vec/extract_if.rs`** -> AI Confidence: **99.18%**
2263. **`library/alloc/src/vec/in_place_collect.rs`** -> AI Confidence: **99.18%**
2264. **`library/alloc/src/vec/into_iter.rs`** -> AI Confidence: **99.18%**
2265. **`library/alloc/src/vec/mod.rs`** -> AI Confidence: **99.18%**
2266. **`library/alloc/src/wtf8/mod.rs`** -> AI Confidence: **99.18%**
2267. **`library/compiler-builtins/builtins-test/src/lib.rs`** -> AI Confidence: **99.18%**
2268. **`library/compiler-builtins/compiler-builtins/src/float/conv.rs`** -> AI Confidence: **99.18%**
2269. **`library/compiler-builtins/compiler-builtins/src/float/div.rs`** -> AI Confidence: **99.18%**
2270. **`library/compiler-builtins/compiler-builtins/src/mem/x86_64.rs`** -> AI Confidence: **99.18%**
2271. **`library/compiler-builtins/crates/libm-macros/src/enums.rs`** -> AI Confidence: **99.18%**
2272. **`library/compiler-builtins/libm/src/math/arch/x86/detect.rs`** -> AI Confidence: **99.18%**
2273. **`library/compiler-builtins/libm/src/math/generic/fma.rs`** -> AI Confidence: **99.18%**
2274. **`library/compiler-builtins/libm/src/math/generic/fmod.rs`** -> AI Confidence: **99.18%**
2275. **`library/compiler-builtins/libm/src/math/generic/sqrt.rs`** -> AI Confidence: **99.18%**
2276. **`library/core/src/alloc/layout.rs`** -> AI Confidence: **99.18%**
2277. **`library/core/src/array/drain.rs`** -> AI Confidence: **99.18%**
2278. **`library/core/src/bstr/traits.rs`** -> AI Confidence: **99.18%**
2279. **`library/core/src/cell.rs`** -> AI Confidence: **99.18%**
2280. **`library/core/src/error.rs`** -> AI Confidence: **99.18%**
2281. **`library/core/src/fmt/float.rs`** -> AI Confidence: **99.18%**
2282. **`library/core/src/fmt/num.rs`** -> AI Confidence: **99.18%**
2283. **`library/core/src/hash/mod.rs`** -> AI Confidence: **99.18%**
2284. **`library/core/src/iter/adapters/array_chunks.rs`** -> AI Confidence: **99.18%**
2285. **`library/core/src/iter/adapters/flatten.rs`** -> AI Confidence: **99.18%**
2286. **`library/core/src/iter/adapters/fuse.rs`** -> AI Confidence: **99.18%**
2287. **`library/core/src/iter/adapters/skip_while.rs`** -> AI Confidence: **99.18%**
2288. **`library/core/src/iter/adapters/step_by.rs`** -> AI Confidence: **99.18%**
2289. **`library/core/src/marker/variance.rs`** -> AI Confidence: **99.18%**
2290. **`library/core/src/mem/maybe_uninit.rs`** -> AI Confidence: **99.18%**
2291. **`library/core/src/num/imp/dec2flt/mod.rs`** -> AI Confidence: **99.18%**
2292. **`library/core/src/num/nonzero.rs`** -> AI Confidence: **99.18%**
2293. **`library/core/src/pin/unsafe_pinned.rs`** -> AI Confidence: **99.18%**
2294. **`library/core/src/ptr/metadata.rs`** -> AI Confidence: **99.18%**
2295. **`library/core/src/range/iter.rs`** -> AI Confidence: **99.18%**
2296. **`library/core/src/slice/mod.rs`** -> AI Confidence: **99.18%**
2297. **`library/core/src/slice/sort/stable/drift.rs`** -> AI Confidence: **99.18%**
2298. **`library/core/src/str/iter.rs`** -> AI Confidence: **99.18%**
2299. **`library/portable-simd/crates/core_simd/src/masks.rs`** -> AI Confidence: **99.18%**
2300. **`library/portable-simd/crates/core_simd/src/ops/assign.rs`** -> AI Confidence: **99.18%**
2301. **`library/portable-simd/crates/core_simd/src/swizzle.rs`** -> AI Confidence: **99.18%**
2302. **`library/portable-simd/crates/core_simd/src/vector.rs`** -> AI Confidence: **99.18%**
2303. **`library/proc_macro/src/bridge/buffer.rs`** -> AI Confidence: **99.18%**
2304. **`library/proc_macro/src/bridge/client.rs`** -> AI Confidence: **99.18%**
2305. **`library/proc_macro/src/bridge/mod.rs`** -> AI Confidence: **99.18%**
2306. **`library/std/src/collections/hash/map/tests.rs`** -> AI Confidence: **99.18%**
2307. **`library/std/src/io/buffered/bufwriter.rs`** -> AI Confidence: **99.18%**
2308. **`library/std/src/io/impls.rs`** -> AI Confidence: **99.18%**
2309. **`library/std/src/io/stdio.rs`** -> AI Confidence: **99.18%**
2310. **`library/std/src/net/socket_addr.rs`** -> AI Confidence: **99.18%**
2311. **`library/std/src/net/tcp.rs`** -> AI Confidence: **99.18%**
2312. **`library/std/src/net/udp.rs`** -> AI Confidence: **99.18%**
2313. **`library/std/src/os/fd/net.rs`** -> AI Confidence: **99.18%**
2314. **`library/std/src/os/fd/raw.rs`** -> AI Confidence: **99.18%**
2315. **`library/std/src/os/fortanix_sgx/io.rs`** -> AI Confidence: **99.18%**
2316. **`library/std/src/os/net/linux_ext/socket.rs`** -> AI Confidence: **99.18%**
2317. **`library/std/src/os/unix/fs.rs`** -> AI Confidence: **99.18%**
2318. **`library/std/src/os/unix/net/stream.rs`** -> AI Confidence: **99.18%**
2319. **`library/std/src/os/windows/net/listener.rs`** -> AI Confidence: **99.18%**
2320. **`library/std/src/os/xous/services.rs`** -> AI Confidence: **99.18%**
2321. **`library/std/src/panicking.rs`** -> AI Confidence: **99.18%**
2322. **`library/std/src/sync/lazy_lock.rs`** -> AI Confidence: **99.18%**
2323. **`library/std/src/sync/mpmc/context.rs`** -> AI Confidence: **99.18%**
2324. **`library/std/src/sync/mpmc/waker.rs`** -> AI Confidence: **99.18%**
2325. **`library/std/src/sync/nonpoison/condvar.rs`** -> AI Confidence: **99.18%**
2326. **`library/std/src/sync/nonpoison/mutex.rs`** -> AI Confidence: **99.18%**
2327. **`library/std/src/sync/poison/mutex.rs`** -> AI Confidence: **99.18%**
2328. **`library/std/src/sys/alloc/windows.rs`** -> AI Confidence: **99.18%**
2329. **`library/std/src/sys/args/zkvm.rs`** -> AI Confidence: **99.18%**
2330. **`library/std/src/sys/exit.rs`** -> AI Confidence: **99.18%**
2331. **`library/std/src/sys/fd/motor.rs`** -> AI Confidence: **99.18%**
2332. **`library/std/src/sys/fd/sgx.rs`** -> AI Confidence: **99.18%**
2333. **`library/std/src/sys/fs/windows/dir.rs`** -> AI Confidence: **99.18%**
2334. **`library/std/src/sys/io/kernel_copy/linux/tests.rs`** -> AI Confidence: **99.18%**
2335. **`library/std/src/sys/net/connection/sgx.rs`** -> AI Confidence: **99.18%**
2336. **`library/std/src/sys/net/connection/uefi/mod.rs`** -> AI Confidence: **99.18%**
2337. **`library/std/src/sys/net/connection/xous/tcplistener.rs`** -> AI Confidence: **99.18%**
2338. **`library/std/src/sys/os_str/bytes.rs`** -> AI Confidence: **99.18%**
2339. **`library/std/src/sys/pal/uefi/helpers.rs`** -> AI Confidence: **99.18%**
2340. **`library/std/src/sys/pal/unix/linux/pidfd/tests.rs`** -> AI Confidence: **99.18%**
2341. **`library/std/src/sys/pal/unix/weak/dlsym.rs`** -> AI Confidence: **99.18%**
2342. **`library/std/src/sys/pal/vexos/mod.rs`** -> AI Confidence: **99.18%**
2343. **`library/std/src/sys/pal/windows/compat.rs`** -> AI Confidence: **99.18%**
2344. **`library/std/src/sys/pipe/unsupported.rs`** -> AI Confidence: **99.18%**
2345. **`library/std/src/sys/platform_version/darwin/mod.rs`** -> AI Confidence: **99.18%**
2346. **`library/std/src/sys/process/uefi.rs`** -> AI Confidence: **99.18%**
2347. **`library/std/src/sys/process/unix/common/tests.rs`** -> AI Confidence: **99.18%**
2348. **`library/std/src/sys/stdio/xous.rs`** -> AI Confidence: **99.18%**
2349. **`library/std/src/sys/sync/condvar/itron.rs`** -> AI Confidence: **99.18%**
2350. **`library/std/src/sys/sync/condvar/pthread.rs`** -> AI Confidence: **99.18%**
2351. **`library/std/src/sys/sync/once_box.rs`** -> AI Confidence: **99.18%**
2352. **`library/std/src/sys/sync/thread_parking/futex.rs`** -> AI Confidence: **99.18%**
2353. **`library/std/src/sys/sync/thread_parking/pthread.rs`** -> AI Confidence: **99.18%**
2354. **`library/std/src/sys/sync/thread_parking/xous.rs`** -> AI Confidence: **99.18%**
2355. **`library/std/src/sys/thread/xous.rs`** -> AI Confidence: **99.18%**
2356. **`library/std/src/sys/thread_local/key/xous.rs`** -> AI Confidence: **99.18%**
2357. **`library/std/src/time.rs`** -> AI Confidence: **99.18%**
2358. **`library/stdarch/crates/core_arch/src/powerpc/macros.rs`** -> AI Confidence: **99.18%**
2359. **`library/stdarch/crates/core_arch/src/s390x/macros.rs`** -> AI Confidence: **99.18%**
2360. **`library/stdarch/crates/intrinsic-test/src/arm/json_parser.rs`** -> AI Confidence: **99.18%**
2361. **`library/stdarch/crates/intrinsic-test/src/x86/xml_parser.rs`** -> AI Confidence: **99.18%**
2362. **`library/stdarch/crates/stdarch-gen-arm/src/input.rs`** -> AI Confidence: **99.18%**
2363. **`library/stdarch/crates/stdarch-gen-arm/src/wildstring.rs`** -> AI Confidence: **99.18%**
2364. **`library/test/src/formatters/json.rs`** -> AI Confidence: **99.18%**
2365. **`library/test/src/time.rs`** -> AI Confidence: **99.18%**
2366. **`src/bootstrap/src/bin/rustc.rs`** -> AI Confidence: **99.18%**
2367. **`src/bootstrap/src/core/build_steps/check.rs`** -> AI Confidence: **99.18%**
2368. **`src/bootstrap/src/core/build_steps/run.rs`** -> AI Confidence: **99.18%**
2369. **`src/bootstrap/src/utils/cache.rs`** -> AI Confidence: **99.18%**
2370. **`src/bootstrap/src/utils/exec.rs`** -> AI Confidence: **99.18%**
2371. **`src/bootstrap/src/utils/job.rs`** -> AI Confidence: **99.18%**
2372. **`src/ci/citool/src/test_dashboard.rs`** -> AI Confidence: **99.18%**
2373. **`src/doc/rustc-dev-guide/ci/date-check/src/main.rs`** -> AI Confidence: **99.18%**
2374. **`src/doc/rustc-dev-guide/examples/rustc-driver-example.rs`** -> AI Confidence: **99.18%**
2375. **`src/doc/rustc-dev-guide/examples/rustc-driver-interacting-with-the-ast.rs`** -> AI Confidence: **99.18%**
2376. **`src/librustdoc/doctest/rust.rs`** -> AI Confidence: **99.18%**
2377. **`src/librustdoc/externalfiles.rs`** -> AI Confidence: **99.18%**
2378. **`src/librustdoc/html/layout.rs`** -> AI Confidence: **99.18%**
2379. **`src/librustdoc/html/markdown/footnotes.rs`** -> AI Confidence: **99.18%**
2380. **`src/librustdoc/html/render/context.rs`** -> AI Confidence: **99.18%**
2381. **`src/librustdoc/html/render/type_layout.rs`** -> AI Confidence: **99.18%**
2382. **`src/librustdoc/json/ids.rs`** -> AI Confidence: **99.18%**
2383. **`src/librustdoc/json/mod.rs`** -> AI Confidence: **99.18%**
2384. **`src/librustdoc/markdown.rs`** -> AI Confidence: **99.18%**
2385. **`src/librustdoc/passes/propagate_doc_cfg.rs`** -> AI Confidence: **99.18%**
2386. **`src/librustdoc/passes/strip_aliased_non_local.rs`** -> AI Confidence: **99.18%**
2387. **`src/librustdoc/scrape_examples.rs`** -> AI Confidence: **99.18%**
2388. **`src/tools/build-manifest/src/main.rs`** -> AI Confidence: **99.18%**
2389. **`src/tools/build-manifest/src/manifest.rs`** -> AI Confidence: **99.18%**
2390. **`src/tools/clippy/clippy_dev/src/generate.rs`** -> AI Confidence: **99.18%**
2391. **`src/tools/clippy/clippy_dev/src/lint.rs`** -> AI Confidence: **99.18%**
2392. **`src/tools/clippy/clippy_dev/src/utils.rs`** -> AI Confidence: **99.18%**
2393. **`src/tools/clippy/clippy_lints/src/async_yields_async.rs`** -> AI Confidence: **99.18%**
2394. **`src/tools/clippy/clippy_lints/src/attrs/should_panic_without_expect.rs`** -> AI Confidence: **99.18%**
2395. **`src/tools/clippy/clippy_lints/src/await_holding_invalid.rs`** -> AI Confidence: **99.18%**
2396. **`src/tools/clippy/clippy_lints/src/bool_assert_comparison.rs`** -> AI Confidence: **99.18%**
2397. **`src/tools/clippy/clippy_lints/src/bool_comparison.rs`** -> AI Confidence: **99.18%**
2398. **`src/tools/clippy/clippy_lints/src/casts/as_underscore.rs`** -> AI Confidence: **99.18%**
2399. **`src/tools/clippy/clippy_lints/src/casts/cast_enum_constructor.rs`** -> AI Confidence: **99.18%**
2400. **`src/tools/clippy/clippy_lints/src/casts/char_lit_as_u8.rs`** -> AI Confidence: **99.18%**
2401. **`src/tools/clippy/clippy_lints/src/casts/fn_to_numeric_cast.rs`** -> AI Confidence: **99.18%**
2402. **`src/tools/clippy/clippy_lints/src/casts/mod.rs`** -> AI Confidence: **99.18%**
2403. **`src/tools/clippy/clippy_lints/src/coerce_container_to_any.rs`** -> AI Confidence: **99.18%**
2404. **`src/tools/clippy/clippy_lints/src/default_constructed_unit_structs.rs`** -> AI Confidence: **99.18%**
2405. **`src/tools/clippy/clippy_lints/src/derive/mod.rs`** -> AI Confidence: **99.18%**
2406. **`src/tools/clippy/clippy_lints/src/disallowed_macros.rs`** -> AI Confidence: **99.18%**
2407. **`src/tools/clippy/clippy_lints/src/disallowed_methods.rs`** -> AI Confidence: **99.18%**
2408. **`src/tools/clippy/clippy_lints/src/floating_point_arithmetic/ln1p.rs`** -> AI Confidence: **99.18%**
2409. **`src/tools/clippy/clippy_lints/src/format_push_string.rs`** -> AI Confidence: **99.18%**
2410. **`src/tools/clippy/clippy_lints/src/functions/duplicate_underscore_argument.rs`** -> AI Confidence: **99.18%**
2411. **`src/tools/clippy/clippy_lints/src/future_not_send.rs`** -> AI Confidence: **99.18%**
2412. **`src/tools/clippy/clippy_lints/src/infallible_try_from.rs`** -> AI Confidence: **99.18%**
2413. **`src/tools/clippy/clippy_lints/src/let_with_type_underscore.rs`** -> AI Confidence: **99.18%**
2414. **`src/tools/clippy/clippy_lints/src/lib.rs`** -> AI Confidence: **99.18%**
2415. **`src/tools/clippy/clippy_lints/src/loops/explicit_counter_loop.rs`** -> AI Confidence: **99.18%**
2416. **`src/tools/clippy/clippy_lints/src/loops/for_kv_map.rs`** -> AI Confidence: **99.18%**
2417. **`src/tools/clippy/clippy_lints/src/methods/chars_cmp.rs`** -> AI Confidence: **99.18%**
2418. **`src/tools/clippy/clippy_lints/src/methods/clone_on_ref_ptr.rs`** -> AI Confidence: **99.18%**
2419. **`src/tools/clippy/clippy_lints/src/methods/expect_fun_call.rs`** -> AI Confidence: **99.18%**
2420. **`src/tools/clippy/clippy_lints/src/methods/filetype_is_file.rs`** -> AI Confidence: **99.18%**
2421. **`src/tools/clippy/clippy_lints/src/methods/filter_map_next.rs`** -> AI Confidence: **99.18%**
2422. **`src/tools/clippy/clippy_lints/src/methods/flat_map_option.rs`** -> AI Confidence: **99.18%**
2423. **`src/tools/clippy/clippy_lints/src/methods/from_iter_instead_of_collect.rs`** -> AI Confidence: **99.18%**
2424. **`src/tools/clippy/clippy_lints/src/methods/get_first.rs`** -> AI Confidence: **99.18%**
2425. **`src/tools/clippy/clippy_lints/src/methods/into_iter_on_ref.rs`** -> AI Confidence: **99.18%**
2426. **`src/tools/clippy/clippy_lints/src/methods/iter_nth.rs`** -> AI Confidence: **99.18%**
2427. **`src/tools/clippy/clippy_lints/src/methods/iter_nth_zero.rs`** -> AI Confidence: **99.18%**
2428. **`src/tools/clippy/clippy_lints/src/methods/manual_next_back.rs`** -> AI Confidence: **99.18%**
2429. **`src/tools/clippy/clippy_lints/src/methods/map_collect_result_unit.rs`** -> AI Confidence: **99.18%**
2430. **`src/tools/clippy/clippy_lints/src/methods/map_flatten.rs`** -> AI Confidence: **99.18%**
2431. **`src/tools/clippy/clippy_lints/src/methods/map_unwrap_or_else.rs`** -> AI Confidence: **99.18%**
2432. **`src/tools/clippy/clippy_lints/src/methods/mut_mutex_lock.rs`** -> AI Confidence: **99.18%**
2433. **`src/tools/clippy/clippy_lints/src/methods/needless_option_as_deref.rs`** -> AI Confidence: **99.18%**
2434. **`src/tools/clippy/clippy_lints/src/methods/ptr_offset_with_cast.rs`** -> AI Confidence: **99.18%**
2435. **`src/tools/clippy/clippy_lints/src/methods/result_map_or_else_none.rs`** -> AI Confidence: **99.18%**
2436. **`src/tools/clippy/clippy_lints/src/methods/return_and_then.rs`** -> AI Confidence: **99.18%**
2437. **`src/tools/clippy/clippy_lints/src/methods/seek_from_current.rs`** -> AI Confidence: **99.18%**
2438. **`src/tools/clippy/clippy_lints/src/methods/sliced_string_as_bytes.rs`** -> AI Confidence: **99.18%**
2439. **`src/tools/clippy/clippy_lints/src/methods/stable_sort_primitive.rs`** -> AI Confidence: **99.18%**
2440. **`src/tools/clippy/clippy_lints/src/methods/unit_hash.rs`** -> AI Confidence: **99.18%**
2441. **`src/tools/clippy/clippy_lints/src/methods/vec_resize_to_zero.rs`** -> AI Confidence: **99.18%**
2442. **`src/tools/clippy/clippy_lints/src/methods/verbose_file_reads.rs`** -> AI Confidence: **99.18%**
2443. **`src/tools/clippy/clippy_lints/src/methods/waker_clone_wake.rs`** -> AI Confidence: **99.18%**
2444. **`src/tools/clippy/clippy_lints/src/mut_key.rs`** -> AI Confidence: **99.18%**
2445. **`src/tools/clippy/clippy_lints/src/needless_borrowed_ref.rs`** -> AI Confidence: **99.18%**
2446. **`src/tools/clippy/clippy_lints/src/no_mangle_with_rust_abi.rs`** -> AI Confidence: **99.18%**
2447. **`src/tools/clippy/clippy_lints/src/operators/absurd_extreme_comparisons.rs`** -> AI Confidence: **99.18%**
2448. **`src/tools/clippy/clippy_lints/src/operators/assign_op_pattern.rs`** -> AI Confidence: **99.18%**
2449. **`src/tools/clippy/clippy_lints/src/operators/double_comparison.rs`** -> AI Confidence: **99.18%**
2450. **`src/tools/clippy/clippy_lints/src/operators/duration_subsec.rs`** -> AI Confidence: **99.18%**
2451. **`src/tools/clippy/clippy_lints/src/operators/integer_division_remainder_used.rs`** -> AI Confidence: **99.18%**
2452. **`src/tools/clippy/clippy_lints/src/panic_in_result_fn.rs`** -> AI Confidence: **99.18%**
2453. **`src/tools/clippy/clippy_lints/src/precedence.rs`** -> AI Confidence: **99.18%**
2454. **`src/tools/clippy/clippy_lints/src/ptr/cmp_null.rs`** -> AI Confidence: **99.18%**
2455. **`src/tools/clippy/clippy_lints/src/pub_use.rs`** -> AI Confidence: **99.18%**
2456. **`src/tools/clippy/clippy_lints/src/rc_clone_in_vec_init.rs`** -> AI Confidence: **99.18%**
2457. **`src/tools/clippy/clippy_lints/src/ref_patterns.rs`** -> AI Confidence: **99.18%**
2458. **`src/tools/clippy/clippy_lints/src/tests_outside_test_module.rs`** -> AI Confidence: **99.18%**
2459. **`src/tools/clippy/clippy_lints/src/toplevel_ref_arg.rs`** -> AI Confidence: **99.18%**
2460. **`src/tools/clippy/clippy_lints/src/transmute/mod.rs`** -> AI Confidence: **99.18%**
2461. **`src/tools/clippy/clippy_lints/src/types/option_option.rs`** -> AI Confidence: **99.18%**
2462. **`src/tools/clippy/clippy_lints/src/types/rc_buffer.rs`** -> AI Confidence: **99.18%**
2463. **`src/tools/clippy/clippy_lints/src/types/rc_mutex.rs`** -> AI Confidence: **99.18%**
2464. **`src/tools/clippy/clippy_lints/src/types/redundant_allocation.rs`** -> AI Confidence: **99.18%**
2465. **`src/tools/clippy/clippy_lints/src/types/type_complexity.rs`** -> AI Confidence: **99.18%**
2466. **`src/tools/clippy/clippy_lints/src/unnecessary_mut_passed.rs`** -> AI Confidence: **99.18%**
2467. **`src/tools/clippy/clippy_lints/src/unused_peekable.rs`** -> AI Confidence: **99.18%**
2468. **`src/tools/clippy/clippy_lints/src/unused_result_ok.rs`** -> AI Confidence: **99.18%**
2469. **`src/tools/clippy/clippy_lints/src/write/use_debug.rs`** -> AI Confidence: **99.18%**
2470. **`src/tools/clippy/clippy_lints/src/zero_sized_map_values.rs`** -> AI Confidence: **99.18%**
2471. **`src/tools/clippy/clippy_utils/src/diagnostics.rs`** -> AI Confidence: **99.18%**
2472. **`src/tools/clippy/lintcheck/src/driver.rs`** -> AI Confidence: **99.18%**
2473. **`src/tools/clippy/lintcheck/src/output.rs`** -> AI Confidence: **99.18%**
2474. **`src/tools/clippy/tests/config-metadata.rs`** -> AI Confidence: **99.18%**
2475. **`src/tools/clippy/tests/ui-toml/mut_key/mut_key.rs`** -> AI Confidence: **99.18%**
2476. **`src/tools/clippy/tests/ui/auxiliary/proc_macro_attr.rs`** -> AI Confidence: **99.18%**
2477. **`src/tools/clippy/tests/ui/auxiliary/proc_macro_suspicious_else_formatting.rs`** -> AI Confidence: **99.18%**
2478. **`src/tools/clippy/tests/ui/let_and_return.rs`** -> AI Confidence: **99.18%**
2479. **`src/tools/compiletest/src/runtest/run_make.rs`** -> AI Confidence: **99.18%**
2480. **`src/tools/coverage-dump/src/covfun.rs`** -> AI Confidence: **99.18%**
2481. **`src/tools/features-status-dump/src/main.rs`** -> AI Confidence: **99.18%**
2482. **`src/tools/miri/cargo-miri/src/util.rs`** -> AI Confidence: **99.18%**
2483. **`src/tools/miri/genmc-sys/build.rs`** -> AI Confidence: **99.18%**
2484. **`src/tools/miri/src/borrow_tracker/tree_borrows/wildcard.rs`** -> AI Confidence: **99.18%**
2485. **`src/tools/miri/src/concurrency/genmc/global_allocations.rs`** -> AI Confidence: **99.18%**
2486. **`src/tools/miri/src/concurrency/genmc/helper.rs`** -> AI Confidence: **99.18%**
2487. **`src/tools/miri/src/data_structures/range_object_map.rs`** -> AI Confidence: **99.18%**
2488. **`src/tools/miri/src/shims/files.rs`** -> AI Confidence: **99.18%**
2489. **`src/tools/miri/tests/pass-dep/concurrency/windows_join_multiple.rs`** -> AI Confidence: **99.18%**
2490. **`src/tools/miri/tests/utils/libc.rs`** -> AI Confidence: **99.18%**
2491. **`src/tools/opt-dist/src/exec.rs`** -> AI Confidence: **99.18%**
2492. **`src/tools/opt-dist/src/tests.rs`** -> AI Confidence: **99.18%**
2493. **`src/tools/opt-dist/src/utils/artifact_size.rs`** -> AI Confidence: **99.18%**
2494. **`src/tools/opt-dist/src/utils/mod.rs`** -> AI Confidence: **99.18%**
2495. **`src/tools/run-make-support/src/command.rs`** -> AI Confidence: **99.18%**
2496. **`src/tools/rust-analyzer/crates/base-db/src/input.rs`** -> AI Confidence: **99.18%**
2497. **`src/tools/rust-analyzer/crates/hir-def/src/builtin_derive.rs`** -> AI Confidence: **99.18%**
2498. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/expander.rs`** -> AI Confidence: **99.18%**
2499. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/lower/generics.rs`** -> AI Confidence: **99.18%**
2500. **`src/tools/rust-analyzer/crates/hir-def/src/expr_store/lower/path/tests.rs`** -> AI Confidence: **99.18%**
2501. **`src/tools/rust-analyzer/crates/hir-def/src/find_path.rs`** -> AI Confidence: **99.18%**
2502. **`src/tools/rust-analyzer/crates/hir-def/src/item_tree.rs`** -> AI Confidence: **99.18%**
2503. **`src/tools/rust-analyzer/crates/hir-def/src/nameres.rs`** -> AI Confidence: **99.18%**
2504. **`src/tools/rust-analyzer/crates/hir-def/src/nameres/assoc.rs`** -> AI Confidence: **99.18%**
2505. **`src/tools/rust-analyzer/crates/hir-def/src/nameres/attr_resolution.rs`** -> AI Confidence: **99.18%**
2506. **`src/tools/rust-analyzer/crates/hir-def/src/per_ns.rs`** -> AI Confidence: **99.18%**
2507. **`src/tools/rust-analyzer/crates/hir-def/src/src.rs`** -> AI Confidence: **99.18%**
2508. **`src/tools/rust-analyzer/crates/hir-ty/src/builtin_derive.rs`** -> AI Confidence: **99.18%**
2509. **`src/tools/rust-analyzer/crates/hir-ty/src/consteval/tests.rs`** -> AI Confidence: **99.18%**
2510. **`src/tools/rust-analyzer/crates/hir-ty/src/display.rs`** -> AI Confidence: **99.18%**
2511. **`src/tools/rust-analyzer/crates/hir-ty/src/generics.rs`** -> AI Confidence: **99.18%**
2512. **`src/tools/rust-analyzer/crates/hir-ty/src/infer/autoderef.rs`** -> AI Confidence: **99.18%**
2513. **`src/tools/rust-analyzer/crates/hir-ty/src/lower.rs`** -> AI Confidence: **99.18%**
2514. **`src/tools/rust-analyzer/crates/hir-ty/src/method_resolution/confirm.rs`** -> AI Confidence: **99.18%**
2515. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/eval/tests.rs`** -> AI Confidence: **99.18%**
2516. **`src/tools/rust-analyzer/crates/hir-ty/src/mir/pretty.rs`** -> AI Confidence: **99.18%**
2517. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/fold.rs`** -> AI Confidence: **99.18%**
2518. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/canonical/mod.rs`** -> AI Confidence: **99.18%**
2519. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/mod.rs`** -> AI Confidence: **99.18%**
2520. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/region_constraints/mod.rs`** -> AI Confidence: **99.18%**
2521. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/snapshot/undo_log.rs`** -> AI Confidence: **99.18%**
2522. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/infer/traits.rs`** -> AI Confidence: **99.18%**
2523. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/interner.rs`** -> AI Confidence: **99.18%**
2524. **`src/tools/rust-analyzer/crates/hir-ty/src/next_solver/opaques.rs`** -> AI Confidence: **99.18%**
2525. **`src/tools/rust-analyzer/crates/hir-ty/src/specialization.rs`** -> AI Confidence: **99.18%**
2526. **`src/tools/rust-analyzer/crates/hir-ty/src/tests/incremental.rs`** -> AI Confidence: **99.18%**
2527. **`src/tools/rust-analyzer/crates/hir-ty/src/tests/patterns.rs`** -> AI Confidence: **99.18%**
2528. **`src/tools/rust-analyzer/crates/hir-ty/src/upvars.rs`** -> AI Confidence: **99.18%**
2529. **`src/tools/rust-analyzer/crates/hir-ty/src/variance.rs`** -> AI Confidence: **99.18%**
2530. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/add_missing_impl_members.rs`** -> AI Confidence: **99.18%**
2531. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/bind_unused_param.rs`** -> AI Confidence: **99.18%**
2532. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_char_literal.rs`** -> AI Confidence: **99.18%**
2533. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_comment_block.rs`** -> AI Confidence: **99.18%**
2534. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_comment_from_or_to_doc.rs`** -> AI Confidence: **99.18%**
2535. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_for_to_while_let.rs`** -> AI Confidence: **99.18%**
2536. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_integer_literal.rs`** -> AI Confidence: **99.18%**
2537. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/convert_tuple_return_type_to_struct.rs`** -> AI Confidence: **99.18%**
2538. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/desugar_doc_comment.rs`** -> AI Confidence: **99.18%**
2539. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/expand_rest_pattern.rs`** -> AI Confidence: **99.18%**
2540. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/extract_module.rs`** -> AI Confidence: **99.18%**
2541. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/extract_type_alias.rs`** -> AI Confidence: **99.18%**
2542. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/flip_comma.rs`** -> AI Confidence: **99.18%**
2543. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_blanket_trait_impl.rs`** -> AI Confidence: **99.18%**
2544. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_delegate_trait.rs`** -> AI Confidence: **99.18%**
2545. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_deref.rs`** -> AI Confidence: **99.18%**
2546. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_enum_variant.rs`** -> AI Confidence: **99.18%**
2547. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_from_impl_for_enum.rs`** -> AI Confidence: **99.18%**
2548. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_function.rs`** -> AI Confidence: **99.18%**
2549. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_getter_or_setter.rs`** -> AI Confidence: **99.18%**
2550. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_is_empty_from_len.rs`** -> AI Confidence: **99.18%**
2551. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_mut_trait_impl.rs`** -> AI Confidence: **99.18%**
2552. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/generate_single_field_struct_from.rs`** -> AI Confidence: **99.18%**
2553. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/inline_macro.rs`** -> AI Confidence: **99.18%**
2554. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/inline_type_alias.rs`** -> AI Confidence: **99.18%**
2555. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/into_to_qualified_from.rs`** -> AI Confidence: **99.18%**
2556. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/move_bounds.rs`** -> AI Confidence: **99.18%**
2557. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/number_representation.rs`** -> AI Confidence: **99.18%**
2558. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/promote_local_to_const.rs`** -> AI Confidence: **99.18%**
2559. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/remove_underscore.rs`** -> AI Confidence: **99.18%**
2560. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/reorder_fields.rs`** -> AI Confidence: **99.18%**
2561. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/reorder_impl_items.rs`** -> AI Confidence: **99.18%**
2562. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/replace_arith_op.rs`** -> AI Confidence: **99.18%**
2563. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/split_import.rs`** -> AI Confidence: **99.18%**
2564. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/toggle_async_sugar.rs`** -> AI Confidence: **99.18%**
2565. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/toggle_ignore.rs`** -> AI Confidence: **99.18%**
2566. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/unqualify_method_call.rs`** -> AI Confidence: **99.18%**
2567. **`src/tools/rust-analyzer/crates/ide-assists/src/handlers/unwrap_type_to_generic_arg.rs`** -> AI Confidence: **99.18%**
2568. **`src/tools/rust-analyzer/crates/ide-assists/src/tests.rs`** -> AI Confidence: **99.18%**
2569. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/env_vars.rs`** -> AI Confidence: **99.18%**
2570. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/extern_abi.rs`** -> AI Confidence: **99.18%**
2571. **`src/tools/rust-analyzer/crates/ide-completion/src/completions/postfix/format_like.rs`** -> AI Confidence: **99.18%**
2572. **`src/tools/rust-analyzer/crates/ide-completion/src/render/type_alias.rs`** -> AI Confidence: **99.18%**
2573. **`src/tools/rust-analyzer/crates/ide-completion/src/tests/special.rs`** -> AI Confidence: **99.18%**
2574. **`src/tools/rust-analyzer/crates/ide-db/src/items_locator.rs`** -> AI Confidence: **99.18%**
2575. **`src/tools/rust-analyzer/crates/ide-db/src/path_transform.rs`** -> AI Confidence: **99.18%**
2576. **`src/tools/rust-analyzer/crates/ide-db/src/source_change.rs`** -> AI Confidence: **99.18%**
2577. **`src/tools/rust-analyzer/crates/ide-db/src/syntax_helpers/suggest_name.rs`** -> AI Confidence: **99.18%**
2578. **`src/tools/rust-analyzer/crates/ide-db/src/syntax_helpers/tree_diff.rs`** -> AI Confidence: **99.18%**
2579. **`src/tools/rust-analyzer/crates/ide-db/src/traits.rs`** -> AI Confidence: **99.18%**
2580. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/json_is_not_rust.rs`** -> AI Confidence: **99.18%**
2581. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/mismatched_arg_count.rs`** -> AI Confidence: **99.18%**
2582. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/missing_fields.rs`** -> AI Confidence: **99.18%**
2583. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/trait_impl_missing_assoc_item.rs`** -> AI Confidence: **99.18%**
2584. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/handlers/unresolved_field.rs`** -> AI Confidence: **99.18%**
2585. **`src/tools/rust-analyzer/crates/ide-diagnostics/src/tests.rs`** -> AI Confidence: **99.18%**
2586. **`src/tools/rust-analyzer/crates/ide-ssr/src/from_comment.rs`** -> AI Confidence: **99.18%**
2587. **`src/tools/rust-analyzer/crates/ide/src/file_structure.rs`** -> AI Confidence: **99.18%**
2588. **`src/tools/rust-analyzer/crates/ide/src/goto_implementation.rs`** -> AI Confidence: **99.18%**
2589. **`src/tools/rust-analyzer/crates/ide/src/goto_type_definition.rs`** -> AI Confidence: **99.18%**
2590. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/bind_pat.rs`** -> AI Confidence: **99.18%**
2591. **`src/tools/rust-analyzer/crates/ide/src/inlay_hints/binding_mode.rs`** -> AI Confidence: **99.18%**
2592. **`src/tools/rust-analyzer/crates/ide/src/interpret.rs`** -> AI Confidence: **99.18%**
2593. **`src/tools/rust-analyzer/crates/ide/src/runnables.rs`** -> AI Confidence: **99.18%**
2594. **`src/tools/rust-analyzer/crates/ide/src/syntax_highlighting/escape.rs`** -> AI Confidence: **99.18%**
2595. **`src/tools/rust-analyzer/crates/ide/src/typing/on_enter.rs`** -> AI Confidence: **99.18%**
2596. **`src/tools/rust-analyzer/crates/ide/src/view_syntax_tree.rs`** -> AI Confidence: **99.18%**
2597. **`src/tools/rust-analyzer/crates/intern/src/gc.rs`** -> AI Confidence: **99.18%**
2598. **`src/tools/rust-analyzer/crates/mbe/src/expander.rs`** -> AI Confidence: **99.18%**
2599. **`src/tools/rust-analyzer/crates/proc-macro-api/src/legacy_protocol.rs`** -> AI Confidence: **99.18%**
2600. **`src/tools/rust-analyzer/crates/proc-macro-srv-cli/src/main_loop.rs`** -> AI Confidence: **99.18%**
2601. **`src/tools/rust-analyzer/crates/proc-macro-srv-cli/tests/bidirectional_postcard.rs`** -> AI Confidence: **99.18%**
2602. **`src/tools/rust-analyzer/crates/proc-macro-srv-cli/tests/legacy_json.rs`** -> AI Confidence: **99.18%**
2603. **`src/tools/rust-analyzer/crates/proc-macro-srv/src/lib.rs`** -> AI Confidence: **99.18%**
2604. **`src/tools/rust-analyzer/crates/proc-macro-srv/src/server_impl/rust_analyzer_span.rs`** -> AI Confidence: **99.18%**
2605. **`src/tools/rust-analyzer/crates/project-model/src/toolchain_info/version.rs`** -> AI Confidence: **99.18%**
2606. **`src/tools/rust-analyzer/crates/query-group-macro/src/lib.rs`** -> AI Confidence: **99.18%**
2607. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/diagnostics.rs`** -> AI Confidence: **99.18%**
2608. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/lsif.rs`** -> AI Confidence: **99.18%**
2609. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/parse.rs`** -> AI Confidence: **99.18%**
2610. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/scip.rs`** -> AI Confidence: **99.18%**
2611. **`src/tools/rust-analyzer/crates/rust-analyzer/src/cli/unresolved_references.rs`** -> AI Confidence: **99.18%**
2612. **`src/tools/rust-analyzer/crates/rust-analyzer/src/lsp/semantic_tokens.rs`** -> AI Confidence: **99.18%**
2613. **`src/tools/rust-analyzer/crates/rust-analyzer/src/lsp/utils.rs`** -> AI Confidence: **99.18%**
2614. **`src/tools/rust-analyzer/crates/rust-analyzer/src/test_runner.rs`** -> AI Confidence: **99.18%**
2615. **`src/tools/rust-analyzer/crates/rust-analyzer/src/tracing/json.rs`** -> AI Confidence: **99.18%**
2616. **`src/tools/rust-analyzer/crates/rust-analyzer/tests/slow-tests/ratoml.rs`** -> AI Confidence: **99.18%**
2617. **`src/tools/rust-analyzer/crates/stdx/src/thread/pool.rs`** -> AI Confidence: **99.18%**
2618. **`src/tools/rust-analyzer/crates/stdx/src/variance.rs`** -> AI Confidence: **99.18%**
2619. **`src/tools/rust-analyzer/crates/syntax-bridge/src/tests.rs`** -> AI Confidence: **99.18%**
2620. **`src/tools/rust-analyzer/crates/syntax/src/lib.rs`** -> AI Confidence: **99.18%**
2621. **`src/tools/rust-analyzer/crates/syntax/src/parsing/reparsing.rs`** -> AI Confidence: **99.18%**
2622. **`src/tools/rust-analyzer/crates/syntax/src/tests.rs`** -> AI Confidence: **99.18%**
2623. **`src/tools/rust-analyzer/crates/test-fixture/src/lib.rs`** -> AI Confidence: **99.18%**
2624. **`src/tools/rust-analyzer/crates/test-utils/src/minicore.rs`** -> AI Confidence: **99.18%**
2625. **`src/tools/rust-analyzer/lib/la-arena/src/lib.rs`** -> AI Confidence: **99.18%**
2626. **`src/tools/rust-analyzer/lib/lsp-server/src/socket.rs`** -> AI Confidence: **99.18%**
2627. **`src/tools/rust-analyzer/lib/smol_str/benches/bench.rs`** -> AI Confidence: **99.18%**
2628. **`src/tools/rust-analyzer/lib/smol_str/src/serde.rs`** -> AI Confidence: **99.18%**
2629. **`src/tools/rust-analyzer/xtask/src/codegen.rs`** -> AI Confidence: **99.18%**
2630. **`src/tools/rust-analyzer/xtask/src/codegen/diagnostics_docs.rs`** -> AI Confidence: **99.18%**
2631. **`src/tools/rustdoc-themes/main.rs`** -> AI Confidence: **99.18%**
2632. **`src/tools/rustfmt/config_proc_macro/src/item_enum.rs`** -> AI Confidence: **99.18%**
2633. **`src/tools/rustfmt/src/config/options.rs`** -> AI Confidence: **99.18%**
2634. **`src/tools/rustfmt/tests/source/issue-2896.rs`** -> AI Confidence: **99.18%**
2635. **`src/tools/test-float-parse/src/gen_/fuzz.rs`** -> AI Confidence: **99.18%**
2636. **`src/tools/test-float-parse/src/gen_/many_digits.rs`** -> AI Confidence: **99.18%**
2637. **`src/tools/tidy/src/arg_parser.rs`** -> AI Confidence: **99.18%**
2638. **`src/tools/tidy/src/diagnostics.rs`** -> AI Confidence: **99.18%**
2639. **`src/tools/tidy/src/main.rs`** -> AI Confidence: **99.18%**
2640. **`src/tools/tidy/src/unstable_book.rs`** -> AI Confidence: **99.18%**
2641. **`src/tools/unicode-table-generator/src/case_mapping.rs`** -> AI Confidence: **99.18%**
2642. **`tests/run-make-cargo/uefi-qemu/uefi_qemu_test/src/main.rs`** -> AI Confidence: **99.18%**
2643. **`tests/run-make/crate-hash-rustc-version/rmake.rs`** -> AI Confidence: **99.18%**
2644. **`tests/run-make/cross-lang-lto-riscv-abi/rmake.rs`** -> AI Confidence: **99.18%**
2645. **`tests/run-make/embed-source-dwarf/rmake.rs`** -> AI Confidence: **99.18%**
2646. **`tests/run-make/extra-filename-with-temp-outputs/rmake.rs`** -> AI Confidence: **99.18%**
2647. **`tests/run-make/libstd-no-protected/rmake.rs`** -> AI Confidence: **99.18%**
2648. **`tests/run-make/pgo-embed-bc-lto/rmake.rs`** -> AI Confidence: **99.18%**
2649. **`tests/rustdoc-gui/src/test_docs/lib.rs`** -> AI Confidence: **99.18%**
2650. **`tests/ui/async-await/async-drop/async-drop-box-allocator.rs`** -> AI Confidence: **99.18%**
2651. **`tests/ui/async-await/async-drop/async-drop-box.rs`** -> AI Confidence: **99.18%**
2652. **`tests/ui/async-await/async-drop/async-drop-future-from-future.rs`** -> AI Confidence: **99.18%**
2653. **`tests/ui/async-await/async-drop/async-drop-future-in-sync-context.rs`** -> AI Confidence: **99.18%**
2654. **`tests/ui/async-await/async-drop/async-drop-glue-array.rs`** -> AI Confidence: **99.18%**
2655. **`tests/ui/async-await/async-drop/async-drop-glue-generic.rs`** -> AI Confidence: **99.18%**
2656. **`tests/ui/async-await/async-drop/async-drop.rs`** -> AI Confidence: **99.18%**
2657. **`tests/ui/async-await/async-drop/live-dead-storage4.rs`** -> AI Confidence: **99.18%**
2658. **`tests/ui/async-await/issues/issue-65419/issue-65419-async-fn-resume-after-panic.rs`** -> AI Confidence: **99.18%**
2659. **`tests/ui/async-await/track-caller/panic-track-caller.rs`** -> AI Confidence: **99.18%**
2660. **`tests/ui/binop/augmented-assignment.rs`** -> AI Confidence: **99.18%**
2661. **`tests/ui/command/command-pre-exec.rs`** -> AI Confidence: **99.18%**
2662. **`tests/ui/consts/const-eval/const-eval-overflow-2.rs`** -> AI Confidence: **99.18%**
2663. **`tests/ui/coroutine/smoke-resume-args.rs`** -> AI Confidence: **99.18%**
2664. **`tests/ui/errors/trait-bound-error-spans/blame-trait-error.rs`** -> AI Confidence: **99.18%**
2665. **`tests/ui/mir/mir_augmented_assignments.rs`** -> AI Confidence: **99.18%**
2666. **`tests/ui/panics/abort-on-panic.rs`** -> AI Confidence: **99.18%**
2667. **`tests/ui/threads-sendsync/tls-in-global-alloc.rs`** -> AI Confidence: **99.18%**
2668. **`src/bootstrap/bootstrap_test.py`** -> AI Confidence: **99.18%**
2669. **`compiler/rustc_llvm/llvm-wrapper/CoverageMappingWrapper.cpp`** -> AI Confidence: **99.18%**
2670. **`src/tools/rust-analyzer/editors/code/src/commands.ts`** -> AI Confidence: **99.18%**
2671. **`compiler/rustc_ast/src/util/classify.rs`** -> AI Confidence: **99.17%**
2672. **`compiler/rustc_attr_parsing/src/validate_attr.rs`** -> AI Confidence: **99.17%**
2673. **`compiler/rustc_codegen_cranelift/build_system/build_sysroot.rs`** -> AI Confidence: **99.17%**
2674. **`compiler/rustc_hir/src/attrs/mod.rs`** -> AI Confidence: **99.17%**
2675. **`compiler/rustc_hir/src/def.rs`** -> AI Confidence: **99.17%**
2676. **`compiler/rustc_trait_selection/src/errors/note_and_explain.rs`** -> AI Confidence: **99.17%**
2677. **`compiler/rustc_trait_selection/src/traits/const_evaluatable.rs`** -> AI Confidence: **99.17%**
2678. **`library/alloc/src/collections/btree/fix.rs`** -> AI Confidence: **99.17%**
2679. **`library/compiler-builtins/libm/src/math/generic/floor.rs`** -> AI Confidence: **99.17%**
2680. **`library/compiler-builtins/libm/src/math/support/macros.rs`** -> AI Confidence: **99.17%**
2681. **`library/core/src/arch.rs`** -> AI Confidence: **99.17%**
2682. **`library/std/src/os/fd/stdio.rs`** -> AI Confidence: **99.17%**
2683. **`library/std/src/sync/poison.rs`** -> AI Confidence: **99.17%**
2684. **`library/std/src/sys/fs/unix/tests.rs`** -> AI Confidence: **99.17%**
2685. **`library/std/src/sys/fs/windows/remove_dir_all.rs`** -> AI Confidence: **99.17%**
2686. **`library/std/src/sys/time/uefi.rs`** -> AI Confidence: **99.17%**
2687. **`library/std_detect/src/detect/cache.rs`** -> AI Confidence: **99.17%**
2688. **`src/tools/clippy/tests/ui-toml/ifs_same_cond/ifs_same_cond.rs`** -> AI Confidence: **99.17%**
2689. **`src/tools/clippy/tests/ui/collapsible_else_if.rs`** -> AI Confidence: **99.17%**
2690. **`src/tools/clippy/tests/ui/collapsible_match_fixable.rs`** -> AI Confidence: **99.17%**
2691. **`src/tools/clippy/tests/ui/crashes/ice-6254.rs`** -> AI Confidence: **99.17%**
2692. **`src/tools/clippy/tests/ui/filetype_is_file.rs`** -> AI Confidence: **99.17%**
2693. **`src/tools/clippy/tests/ui/manual_find.rs`** -> AI Confidence: **99.17%**
2694. **`src/tools/clippy/tests/ui/match_ref_pats.rs`** -> AI Confidence: **99.17%**
2695. **`src/tools/clippy/tests/ui/missing_spin_loop.rs`** -> AI Confidence: **99.17%**
2696. **`src/tools/clippy/tests/ui/never_loop_fixable.rs`** -> AI Confidence: **99.17%**
2697. **`src/tools/clippy/tests/ui/return_and_then.rs`** -> AI Confidence: **99.17%**
2698. **`src/tools/clippy/tests/ui/semicolon_inside_block.rs`** -> AI Confidence: **99.17%**
2699. **`src/tools/clippy/tests/ui/single_element_loop.rs`** -> AI Confidence: **99.17%**
2700. **`src/tools/clippy/tests/ui/suspicious_operation_groupings.rs`** -> AI Confidence: **99.17%**
2701. **`src/tools/clippy/tests/ui/suspicious_unary_op_formatting.rs`** -> AI Confidence: **99.17%**
2702. **`src/tools/clippy/tests/ui/ty_fn_sig.rs`** -> AI Confidence: **99.17%**
2703. **`src/tools/clippy/tests/ui/unit_cmp.rs`** -> AI Confidence: **99.17%**
2704. **`src/tools/miri/src/concurrency/weak_memory.rs`** -> AI Confidence: **99.17%**
2705. **`src/tools/rust-analyzer/crates/hir-ty/src/consteval.rs`** -> AI Confidence: **99.17%**
2706. **`src/tools/rust-analyzer/crates/ide-db/src/imports/insert_use.rs`** -> AI Confidence: **99.17%**
2707. **`src/tools/rust-analyzer/crates/ide/src/typing.rs`** -> AI Confidence: **99.17%**
2708. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/match_guard.rs`** -> AI Confidence: **99.17%**
2709. **`src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/while_expr.rs`** -> AI Confidence: **99.17%**
2710. **`src/tools/rust-analyzer/crates/syntax/src/algo.rs`** -> AI Confidence: **99.17%**
2711. **`src/tools/rustfmt/tests/source/cfg_if/detect/arch/powerpc.rs`** -> AI Confidence: **99.17%**
2712. **`src/tools/rustfmt/tests/source/cfg_if/detect/arch/powerpc64.rs`** -> AI Confidence: **99.17%**
2713. **`src/tools/rustfmt/tests/source/issue-1211.rs`** -> AI Confidence: **99.17%**
2714. **`src/tools/rustfmt/tests/source/issue-1468.rs`** -> AI Confidence: **99.17%**
2715. **`src/tools/rustfmt/tests/source/issue-3029.rs`** -> AI Confidence: **99.17%**
2716. **`src/tools/rustfmt/tests/source/issue-4120.rs`** -> AI Confidence: **99.17%**
2717. **`src/tools/rustfmt/tests/source/loop.rs`** -> AI Confidence: **99.17%**
2718. **`src/tools/rustfmt/tests/source/one_line_if_v1.rs`** -> AI Confidence: **99.17%**
2719. **`src/tools/rustfmt/tests/source/one_line_if_v2.rs`** -> AI Confidence: **99.17%**
2720. **`src/tools/rustfmt/tests/source/single-line-if-else.rs`** -> AI Confidence: **99.17%**
2721. **`tests/assembly-llvm/manual-eq-efficient.rs`** -> AI Confidence: **99.17%**
2722. **`tests/mir-opt/building/issue_49232.rs`** -> AI Confidence: **99.17%**
2723. **`tests/mir-opt/building/loop_match_diverges.rs`** -> AI Confidence: **99.17%**
2724. **`tests/mir-opt/building/match/never_patterns.rs`** -> AI Confidence: **99.17%**
2725. **`tests/mir-opt/separate_const_switch.rs`** -> AI Confidence: **99.17%**
2726. **`tests/ui/asm/naked-functions-rustic-abi.rs`** -> AI Confidence: **99.17%**
2727. **`tests/ui/attributes/issue-90873.rs`** -> AI Confidence: **99.17%**
2728. **`tests/ui/binding/match-byte-array-patterns.rs`** -> AI Confidence: **99.17%**
2729. **`tests/ui/binding/match-range-infer.rs`** -> AI Confidence: **99.17%**
2730. **`tests/ui/binding/pat-tuple-4.rs`** -> AI Confidence: **99.17%**
2731. **`tests/ui/borrowck/borrowck-match-binding-is-assignment.rs`** -> AI Confidence: **99.17%**
2732. **`tests/ui/c-variadic/naked-invalid.rs`** -> AI Confidence: **99.17%**
2733. **`tests/ui/closures/labeled-break-inside-closure-62480.rs`** -> AI Confidence: **99.17%**
2734. **`tests/ui/consts/const-big-enum.rs`** -> AI Confidence: **99.17%**
2735. **`tests/ui/consts/const_in_pattern/issue-44333.rs`** -> AI Confidence: **99.17%**
2736. **`tests/ui/consts/const_refs_to_static_fail_invalid.rs`** -> AI Confidence: **99.17%**
2737. **`tests/ui/contracts/contracts-ensures-early-fn-exit.rs`** -> AI Confidence: **99.17%**
2738. **`tests/ui/drop/drop_order.rs`** -> AI Confidence: **99.17%**
2739. **`tests/ui/expr/if/attrs/cfg-false-if-attr.rs`** -> AI Confidence: **99.17%**
2740. **`tests/ui/expr/if/expr-if-panic-pass.rs`** -> AI Confidence: **99.17%**
2741. **`tests/ui/expr/if/expr-if.rs`** -> AI Confidence: **99.17%**
2742. **`tests/ui/expr/if/if-no-match-bindings.rs`** -> AI Confidence: **99.17%**
2743. **`tests/ui/expr/if/issue-4201.rs`** -> AI Confidence: **99.17%**
2744. **`tests/ui/feature-gates/feature-gate-guard-patterns.rs`** -> AI Confidence: **99.17%**
2745. **`tests/ui/feature-gates/feature-gate-naked_functions_rustic_abi.rs`** -> AI Confidence: **99.17%**
2746. **`tests/ui/feature-gates/feature-gate-never_patterns.rs`** -> AI Confidence: **99.17%**
2747. **`tests/ui/for-loop-while/label_break_value.rs`** -> AI Confidence: **99.17%**
2748. **`tests/ui/for-loop-while/loop-break-cont.rs`** -> AI Confidence: **99.17%**
2749. **`tests/ui/for-loop-while/loop-break-value.rs`** -> AI Confidence: **99.17%**
2750. **`tests/ui/for-loop-while/loop-labeled-break-value.rs`** -> AI Confidence: **99.17%**
2751. **`tests/ui/for-loop-while/nested-loop-break-unit.rs`** -> AI Confidence: **99.17%**
2752. **`tests/ui/generics/generic-extern-lifetime.rs`** -> AI Confidence: **99.17%**
2753. **`tests/ui/hygiene/hir-res-hygiene.rs`** -> AI Confidence: **99.17%**
2754. **`tests/ui/inference/issue-86094-suggest-add-return-to-coerce-ret-ty.rs`** -> AI Confidence: **99.17%**
2755. **`tests/ui/issues/issue-28279.rs`** -> AI Confidence: **99.17%**
2756. **`tests/ui/issues/issue-29071-2.rs`** -> AI Confidence: **99.17%**
2757. **`tests/ui/iterators/array-of-ranges.rs`** -> AI Confidence: **99.17%**
2758. **`tests/ui/iterators/array.rs`** -> AI Confidence: **99.17%**
2759. **`tests/ui/label/undeclared-label-span.rs`** -> AI Confidence: **99.17%**
2760. **`tests/ui/lifetimes/lifetime-errors/liveness-assign-imm-local-notes.rs`** -> AI Confidence: **99.17%**
2761. **`tests/ui/loop-match/panic-in-const.rs`** -> AI Confidence: **99.17%**
2762. **`tests/ui/loop-match/unsupported-type.rs`** -> AI Confidence: **99.17%**
2763. **`tests/ui/loops/loop-labeled-break-value.rs`** -> AI Confidence: **99.17%**
2764. **`tests/ui/lub-glb/old-lub-glb-hr-eq.rs`** -> AI Confidence: **99.17%**
2765. **`tests/ui/macros/macro-at-most-once-rep-2015-rpass.rs`** -> AI Confidence: **99.17%**
2766. **`tests/ui/macros/macro-at-most-once-rep-2018-rpass.rs`** -> AI Confidence: **99.17%**
2767. **`tests/ui/match/dont-highlight-diverging-arms.rs`** -> AI Confidence: **99.17%**
2768. **`tests/ui/match/guards.rs`** -> AI Confidence: **99.17%**
2769. **`tests/ui/match/issue-82392.rs`** -> AI Confidence: **99.17%**
2770. **`tests/ui/match/match-on-negative-integer-ranges.rs`** -> AI Confidence: **99.17%**
2771. **`tests/ui/match/uninhabited-granular-moves.rs`** -> AI Confidence: **99.17%**
2772. **`tests/ui/nll/closure-captures.rs`** -> AI Confidence: **99.17%**
2773. **`tests/ui/parser/diff-markers/enum-2.rs`** -> AI Confidence: **99.17%**
2774. **`tests/ui/parser/diff-markers/long-conflict-markers.rs`** -> AI Confidence: **99.17%**
2775. **`tests/ui/parser/issues/issue-72373.rs`** -> AI Confidence: **99.17%**
2776. **`tests/ui/parser/issues/issue-91421.rs`** -> AI Confidence: **99.17%**
2777. **`tests/ui/parser/label-after-block-like.rs`** -> AI Confidence: **99.17%**
2778. **`tests/ui/parser/macro/statement-boundaries.rs`** -> AI Confidence: **99.17%**
2779. **`tests/ui/parser/or-in-let-chain.rs`** -> AI Confidence: **99.17%**
2780. **`tests/ui/pattern/pat-tuple-underfield.rs`** -> AI Confidence: **99.17%**
2781. **`tests/ui/pattern/usefulness/doc-hidden-non-exhaustive.rs`** -> AI Confidence: **99.17%**
2782. **`tests/ui/pattern/usefulness/empty-types.rs`** -> AI Confidence: **99.17%**
2783. **`tests/ui/pattern/usefulness/issue-30240-b.rs`** -> AI Confidence: **99.17%**
2784. **`tests/ui/pattern/usefulness/issue-30240.rs`** -> AI Confidence: **99.17%**
2785. **`tests/ui/pattern/usefulness/slice-patterns-reachability.rs`** -> AI Confidence: **99.17%**
2786. **`tests/ui/pattern/usefulness/top-level-alternation.rs`** -> AI Confidence: **99.17%**
2787. **`tests/ui/rfcs/rfc-0000-never_patterns/ICE-133063-never-arm-no-otherwise-block.rs`** -> AI Confidence: **99.17%**
2788. **`tests/ui/rfcs/rfc-0000-never_patterns/ICE-133117-duplicate-never-arm.rs`** -> AI Confidence: **99.17%**
2789. **`tests/ui/rfcs/rfc-2008-non-exhaustive/omitted-patterns-dont-lint-on-arm.rs`** -> AI Confidence: **99.17%**
2790. **`tests/ui/rfcs/rfc-2008-non-exhaustive/uninhabited/match.rs`** -> AI Confidence: **99.17%**
2791. **`tests/ui/rfcs/rfc-2294-if-let-guard/loop-mutability.rs`** -> AI Confidence: **99.17%**
2792. **`tests/ui/rfcs/rfc-2497-if-let-chains/ast-validate-guards.rs`** -> AI Confidence: **99.17%**
2793. **`tests/ui/rfcs/rfc-2497-if-let-chains/if_let_guard_indirect_let_chains.rs`** -> AI Confidence: **99.17%**
2794. **`tests/ui/suggestions/if-let-typo.rs`** -> AI Confidence: **99.17%**
2795. **`tests/ui/suggestions/match-ergonomics.rs`** -> AI Confidence: **99.17%**
2796. **`tests/ui/suggestions/while-let-typo.rs`** -> AI Confidence: **99.17%**
2797. **`tests/ui/target-feature/feature-hierarchy.rs`** -> AI Confidence: **99.17%**
2798. **`tests/ui/target-feature/no-llvm-leaks.rs`** -> AI Confidence: **99.17%**
2799. **`tests/ui/traits/next-solver/coercion/fn-def-coerce-nested-obligations.rs`** -> AI Confidence: **99.17%**
2800. **`tests/ui/traits/next-solver/unsize-overflow.rs`** -> AI Confidence: **99.17%**
2801. **`tests/ui/try-block/try-block-unused-delims.rs`** -> AI Confidence: **99.17%**
2802. **`tests/ui/type/pattern_types/matching_fail.rs`** -> AI Confidence: **99.17%**
2803. **`tests/ui/type/type-error-break-tail.rs`** -> AI Confidence: **99.17%**
2804. **`tests/ui/typeck/consider-borrowing-141810-3.rs`** -> AI Confidence: **99.17%**
2805. **`tests/ui/typeck/issue-112007-leaked-writeln-macro-internals.rs`** -> AI Confidence: **99.17%**
2806. **`tests/ui/typeck/issue-114529-illegal-break-with-value.rs`** -> AI Confidence: **99.17%**
2807. **`tests/ui/typeck/question-mark-operator-suggestion-span.rs`** -> AI Confidence: **99.17%**
2808. **`tests/ui/uninhabited/uninhabited-unstable-field.rs`** -> AI Confidence: **99.17%**
2809. **`tests/ui/uninhabited/unreachable.rs`** -> AI Confidence: **99.17%**
2810. **`tests/ui/uninhabited/void-branch.rs`** -> AI Confidence: **99.17%**
2811. **`src/ci/docker/host-x86_64/x86_64-fuchsia/build-fuchsia.sh`** -> AI Confidence: **99.17%**
2812. **`src/ci/scripts/setup-environment.sh`** -> AI Confidence: **99.17%**
2813. **`src/ci/scripts/upload-artifacts.sh`** -> AI Confidence: **99.17%**
2814. **`src/ci/scripts/verify-backported-commits.sh`** -> AI Confidence: **99.17%**
2815. **`src/etc/pre-push.sh`** -> AI Confidence: **99.17%**
2816. **`src/etc/rust-lldb`** -> AI Confidence: **99.17%**
2817. **`src/tools/cherry-pick.sh`** -> AI Confidence: **99.17%**
2818. **`src/tools/clippy/util/etc/pre-commit.sh`** -> AI Confidence: **99.17%**
2819. **`src/tools/clippy/util/fetch_prs_between.sh`** -> AI Confidence: **99.17%**
2820. **`src/tools/miri/ci/ci.sh`** -> AI Confidence: **99.17%**
2821. **`src/tools/rust-installer/install-template.sh`** -> AI Confidence: **99.17%**
2822. **`x`** -> AI Confidence: **99.17%**
2823. **`src/ci/docker/host-x86_64/dist-various-2/Dockerfile`** -> AI Confidence: **99.17%**
2824. **`src/ci/docker/host-x86_64/dist-x86_64-musl/Dockerfile`** -> AI Confidence: **99.17%**
2825. **`src/ci/docker/host-x86_64/x86_64-fuchsia/Dockerfile`** -> AI Confidence: **99.17%**
2826. **`src/librustdoc/html/static/js/settings.js`** -> AI Confidence: **99.17%**
2827. **`src/tools/rust-analyzer/editors/code/src/bootstrap.ts`** -> AI Confidence: **99.17%**
2828. **`compiler/rustc_abi/src/extern_abi.rs`** -> AI Confidence: **99.16%**
2829. **`compiler/rustc_abi/src/layout.rs`** -> AI Confidence: **99.16%**
2830. **`compiler/rustc_abi/src/layout/ty.rs`** -> AI Confidence: **99.16%**
2831. **`compiler/rustc_ast/src/ast.rs`** -> AI Confidence: **99.16%**
2832. **`compiler/rustc_ast/src/attr/mod.rs`** -> AI Confidence: **99.16%**
2833. **`compiler/rustc_ast/src/expand/autodiff_attrs.rs`** -> AI Confidence: **99.16%**
2834. **`compiler/rustc_ast/src/tokenstream.rs`** -> AI Confidence: **99.16%**
2835. **`compiler/rustc_ast_lowering/src/delegation.rs`** -> AI Confidence: **99.16%**
2836. **`compiler/rustc_ast_lowering/src/format.rs`** -> AI Confidence: **99.16%**
2837. **`compiler/rustc_ast_lowering/src/pat.rs`** -> AI Confidence: **99.16%**
2838. **`compiler/rustc_ast_lowering/src/path.rs`** -> AI Confidence: **99.16%**
2839. **`compiler/rustc_attr_parsing/src/attributes/cfg_select.rs`** -> AI Confidence: **99.16%**
2840. **`compiler/rustc_attr_parsing/src/attributes/rustc_internal.rs`** -> AI Confidence: **99.16%**
2841. **`compiler/rustc_attr_parsing/src/attributes/traits.rs`** -> AI Confidence: **99.16%**
2842. **`compiler/rustc_attr_parsing/src/attributes/util.rs`** -> AI Confidence: **99.16%**
2843. **`compiler/rustc_attr_parsing/src/interface.rs`** -> AI Confidence: **99.16%**
2844. **`compiler/rustc_attr_parsing/src/safety.rs`** -> AI Confidence: **99.16%**
2845. **`compiler/rustc_attr_parsing/src/target_checking.rs`** -> AI Confidence: **99.16%**
2846. **`compiler/rustc_borrowck/src/dataflow.rs`** -> AI Confidence: **99.16%**
2847. **`compiler/rustc_borrowck/src/diagnostics/bound_region_errors.rs`** -> AI Confidence: **99.16%**
2848. **`compiler/rustc_borrowck/src/diagnostics/find_use.rs`** -> AI Confidence: **99.16%**
2849. **`compiler/rustc_borrowck/src/diagnostics/move_errors.rs`** -> AI Confidence: **99.16%**
2850. **`compiler/rustc_borrowck/src/diagnostics/opaque_types.rs`** -> AI Confidence: **99.16%**
2851. **`compiler/rustc_borrowck/src/diagnostics/region_errors.rs`** -> AI Confidence: **99.16%**
2852. **`compiler/rustc_borrowck/src/diagnostics/region_name.rs`** -> AI Confidence: **99.16%**
2853. **`compiler/rustc_borrowck/src/lib.rs`** -> AI Confidence: **99.16%**
2854. **`compiler/rustc_borrowck/src/path_utils.rs`** -> AI Confidence: **99.16%**
2855. **`compiler/rustc_borrowck/src/polonius/legacy/facts.rs`** -> AI Confidence: **99.16%**
2856. **`compiler/rustc_borrowck/src/polonius/legacy/loan_kills.rs`** -> AI Confidence: **99.16%**
2857. **`compiler/rustc_borrowck/src/polonius/legacy/mod.rs`** -> AI Confidence: **99.16%**
2858. **`compiler/rustc_borrowck/src/region_infer/mod.rs`** -> AI Confidence: **99.16%**
2859. **`compiler/rustc_borrowck/src/region_infer/opaque_types/member_constraints.rs`** -> AI Confidence: **99.16%**
2860. **`compiler/rustc_borrowck/src/region_infer/opaque_types/mod.rs`** -> AI Confidence: **99.16%**
2861. **`compiler/rustc_borrowck/src/type_check/mod.rs`** -> AI Confidence: **99.16%**
2862. **`compiler/rustc_borrowck/src/universal_regions.rs`** -> AI Confidence: **99.16%**
2863. **`compiler/rustc_builtin_macros/src/assert.rs`** -> AI Confidence: **99.16%**
2864. **`compiler/rustc_builtin_macros/src/autodiff.rs`** -> AI Confidence: **99.16%**
2865. **`compiler/rustc_builtin_macros/src/cfg_accessible.rs`** -> AI Confidence: **99.16%**
2866. **`compiler/rustc_builtin_macros/src/concat.rs`** -> AI Confidence: **99.16%**
2867. **`compiler/rustc_builtin_macros/src/contracts.rs`** -> AI Confidence: **99.16%**
2868. **`compiler/rustc_builtin_macros/src/derive.rs`** -> AI Confidence: **99.16%**
2869. **`compiler/rustc_builtin_macros/src/deriving/clone.rs`** -> AI Confidence: **99.16%**
2870. **`compiler/rustc_builtin_macros/src/deriving/cmp/partial_ord.rs`** -> AI Confidence: **99.16%**
2871. **`compiler/rustc_builtin_macros/src/deriving/debug.rs`** -> AI Confidence: **99.16%**
2872. **`compiler/rustc_builtin_macros/src/deriving/default.rs`** -> AI Confidence: **99.16%**
2873. **`compiler/rustc_builtin_macros/src/deriving/generic/mod.rs`** -> AI Confidence: **99.16%**
2874. **`compiler/rustc_builtin_macros/src/eii.rs`** -> AI Confidence: **99.16%**
2875. **`compiler/rustc_builtin_macros/src/env.rs`** -> AI Confidence: **99.16%**
2876. **`compiler/rustc_builtin_macros/src/pattern_type.rs`** -> AI Confidence: **99.16%**
2877. **`compiler/rustc_builtin_macros/src/proc_macro_harness.rs`** -> AI Confidence: **99.16%**
2878. **`compiler/rustc_builtin_macros/src/util.rs`** -> AI Confidence: **99.16%**
2879. **`compiler/rustc_codegen_cranelift/build_system/prepare.rs`** -> AI Confidence: **99.16%**
2880. **`compiler/rustc_codegen_cranelift/build_system/utils.rs`** -> AI Confidence: **99.16%**
2881. **`compiler/rustc_codegen_cranelift/src/abi/mod.rs`** -> AI Confidence: **99.16%**
2882. **`compiler/rustc_codegen_cranelift/src/abi/pass_mode.rs`** -> AI Confidence: **99.16%**
2883. **`compiler/rustc_codegen_cranelift/src/common.rs`** -> AI Confidence: **99.16%**
2884. **`compiler/rustc_codegen_cranelift/src/constant.rs`** -> AI Confidence: **99.16%**
2885. **`compiler/rustc_codegen_cranelift/src/debuginfo/object.rs`** -> AI Confidence: **99.16%**
2886. **`compiler/rustc_codegen_cranelift/src/debuginfo/unwind.rs`** -> AI Confidence: **99.16%**
2887. **`compiler/rustc_codegen_cranelift/src/global_asm.rs`** -> AI Confidence: **99.16%**
2888. **`compiler/rustc_codegen_cranelift/src/lib.rs`** -> AI Confidence: **99.16%**
2889. **`compiler/rustc_codegen_gcc/build_system/src/build.rs`** -> AI Confidence: **99.16%**
2890. **`compiler/rustc_codegen_gcc/src/abi.rs`** -> AI Confidence: **99.16%**
2891. **`compiler/rustc_codegen_gcc/src/allocator.rs`** -> AI Confidence: **99.16%**
2892. **`compiler/rustc_codegen_gcc/src/back/lto.rs`** -> AI Confidence: **99.16%**
2893. **`compiler/rustc_codegen_gcc/src/base.rs`** -> AI Confidence: **99.16%**
2894. **`compiler/rustc_codegen_gcc/src/consts.rs`** -> AI Confidence: **99.16%**
2895. **`compiler/rustc_codegen_gcc/src/int.rs`** -> AI Confidence: **99.16%**
2896. **`compiler/rustc_codegen_gcc/src/type_of.rs`** -> AI Confidence: **99.16%**
2897. **`compiler/rustc_codegen_llvm/src/allocator.rs`** -> AI Confidence: **99.16%**
2898. **`compiler/rustc_codegen_llvm/src/back/lto.rs`** -> AI Confidence: **99.16%**
2899. **`compiler/rustc_codegen_llvm/src/back/write.rs`** -> AI Confidence: **99.16%**
2900. **`compiler/rustc_codegen_llvm/src/builder/autodiff.rs`** -> AI Confidence: **99.16%**
2901. **`compiler/rustc_codegen_llvm/src/consts.rs`** -> AI Confidence: **99.16%**
2902. **`compiler/rustc_codegen_llvm/src/context.rs`** -> AI Confidence: **99.16%**
2903. **`compiler/rustc_codegen_llvm/src/coverageinfo/mapgen/unused.rs`** -> AI Confidence: **99.16%**
2904. **`compiler/rustc_codegen_llvm/src/debuginfo/metadata.rs`** -> AI Confidence: **99.16%**
2905. **`compiler/rustc_codegen_llvm/src/declare.rs`** -> AI Confidence: **99.16%**
2906. **`compiler/rustc_codegen_llvm/src/intrinsic.rs`** -> AI Confidence: **99.16%**
2907. **`compiler/rustc_codegen_llvm/src/type_of.rs`** -> AI Confidence: **99.16%**
2908. **`compiler/rustc_codegen_ssa/src/assert_module_sources.rs`** -> AI Confidence: **99.16%**
2909. **`compiler/rustc_codegen_ssa/src/back/archive.rs`** -> AI Confidence: **99.16%**
2910. **`compiler/rustc_codegen_ssa/src/back/link/raw_dylib.rs`** -> AI Confidence: **99.16%**
2911. **`compiler/rustc_codegen_ssa/src/back/linker.rs`** -> AI Confidence: **99.16%**
2912. **`compiler/rustc_codegen_ssa/src/back/metadata.rs`** -> AI Confidence: **99.16%**
2913. **`compiler/rustc_codegen_ssa/src/back/write.rs`** -> AI Confidence: **99.16%**
2914. **`compiler/rustc_codegen_ssa/src/base.rs`** -> AI Confidence: **99.16%**
2915. **`compiler/rustc_codegen_ssa/src/mir/analyze.rs`** -> AI Confidence: **99.16%**
2916. **`compiler/rustc_codegen_ssa/src/mir/block.rs`** -> AI Confidence: **99.16%**
2917. **`compiler/rustc_codegen_ssa/src/mir/debuginfo.rs`** -> AI Confidence: **99.16%**
2918. **`compiler/rustc_codegen_ssa/src/mir/operand.rs`** -> AI Confidence: **99.16%**
2919. **`compiler/rustc_codegen_ssa/src/mir/place.rs`** -> AI Confidence: **99.16%**
2920. **`compiler/rustc_const_eval/src/check_consts/check.rs`** -> AI Confidence: **99.16%**
2921. **`compiler/rustc_const_eval/src/check_consts/mod.rs`** -> AI Confidence: **99.16%**
2922. **`compiler/rustc_const_eval/src/check_consts/ops.rs`** -> AI Confidence: **99.16%**
2923. **`compiler/rustc_const_eval/src/const_eval/dyn_trait.rs`** -> AI Confidence: **99.16%**
2924. **`compiler/rustc_const_eval/src/const_eval/eval_queries.rs`** -> AI Confidence: **99.16%**
2925. **`compiler/rustc_const_eval/src/const_eval/valtrees.rs`** -> AI Confidence: **99.16%**
2926. **`compiler/rustc_const_eval/src/interpret/eval_context.rs`** -> AI Confidence: **99.16%**
2927. **`compiler/rustc_const_eval/src/interpret/intern.rs`** -> AI Confidence: **99.16%**
2928. **`compiler/rustc_const_eval/src/interpret/stack.rs`** -> AI Confidence: **99.16%**
2929. **`compiler/rustc_const_eval/src/interpret/traits.rs`** -> AI Confidence: **99.16%**
2930. **`compiler/rustc_data_structures/src/obligation_forest/mod.rs`** -> AI Confidence: **99.16%**
2931. **`compiler/rustc_data_structures/src/profiling.rs`** -> AI Confidence: **99.16%**
2932. **`compiler/rustc_data_structures/src/sorted_map.rs`** -> AI Confidence: **99.16%**
2933. **`compiler/rustc_data_structures/src/sync/freeze.rs`** -> AI Confidence: **99.16%**
2934. **`compiler/rustc_data_structures/src/sync/lock.rs`** -> AI Confidence: **99.16%**
2935. **`compiler/rustc_data_structures/src/sync/parallel.rs`** -> AI Confidence: **99.16%**
2936. **`compiler/rustc_driver_impl/src/lib.rs`** -> AI Confidence: **99.16%**
2937. **`compiler/rustc_error_messages/src/diagnostic_impls.rs`** -> AI Confidence: **99.16%**
2938. **`compiler/rustc_error_messages/src/lib.rs`** -> AI Confidence: **99.16%**
2939. **`compiler/rustc_errors/src/annotate_snippet_emitter_writer.rs`** -> AI Confidence: **99.16%**
2940. **`compiler/rustc_errors/src/diagnostic_impls.rs`** -> AI Confidence: **99.16%**
2941. **`compiler/rustc_errors/src/emitter.rs`** -> AI Confidence: **99.16%**
2942. **`compiler/rustc_errors/src/json.rs`** -> AI Confidence: **99.16%**
2943. **`compiler/rustc_errors/src/lib.rs`** -> AI Confidence: **99.16%**
2944. **`compiler/rustc_expand/src/expand.rs`** -> AI Confidence: **99.16%**
2945. **`compiler/rustc_expand/src/mbe/macro_check.rs`** -> AI Confidence: **99.16%**
2946. **`compiler/rustc_expand/src/mbe/macro_parser.rs`** -> AI Confidence: **99.16%**
2947. **`compiler/rustc_expand/src/mbe/macro_rules.rs`** -> AI Confidence: **99.16%**
2948. **`compiler/rustc_expand/src/mbe/metavar_expr.rs`** -> AI Confidence: **99.16%**
2949. **`compiler/rustc_expand/src/mbe/transcribe.rs`** -> AI Confidence: **99.16%**
2950. **`compiler/rustc_expand/src/proc_macro_server.rs`** -> AI Confidence: **99.16%**
2951. **`compiler/rustc_expand/src/stats.rs`** -> AI Confidence: **99.16%**
2952. **`compiler/rustc_feature/src/lib.rs`** -> AI Confidence: **99.16%**
2953. **`compiler/rustc_hir/src/attrs/pretty_printing.rs`** -> AI Confidence: **99.16%**
2954. **`compiler/rustc_hir/src/hir.rs`** -> AI Confidence: **99.16%**
2955. **`compiler/rustc_hir/src/pat_util.rs`** -> AI Confidence: **99.16%**
2956. **`compiler/rustc_hir/src/target.rs`** -> AI Confidence: **99.16%**
2957. **`compiler/rustc_hir_analysis/src/autoderef.rs`** -> AI Confidence: **99.16%**
2958. **`compiler/rustc_hir_analysis/src/check/always_applicable.rs`** -> AI Confidence: **99.16%**
2959. **`compiler/rustc_hir_analysis/src/check/compare_eii.rs`** -> AI Confidence: **99.16%**
2960. **`compiler/rustc_hir_analysis/src/check/compare_impl_item.rs`** -> AI Confidence: **99.16%**
2961. **`compiler/rustc_hir_analysis/src/check/compare_impl_item/refine.rs`** -> AI Confidence: **99.16%**
2962. **`compiler/rustc_hir_analysis/src/check/entry.rs`** -> AI Confidence: **99.16%**
2963. **`compiler/rustc_hir_analysis/src/check/mod.rs`** -> AI Confidence: **99.16%**
2964. **`compiler/rustc_hir_analysis/src/check/wfcheck.rs`** -> AI Confidence: **99.16%**
2965. **`compiler/rustc_hir_analysis/src/coherence/builtin.rs`** -> AI Confidence: **99.16%**
2966. **`compiler/rustc_hir_analysis/src/coherence/inherent_impls.rs`** -> AI Confidence: **99.16%**
2967. **`compiler/rustc_hir_analysis/src/coherence/inherent_impls_overlap.rs`** -> AI Confidence: **99.16%**
2968. **`compiler/rustc_hir_analysis/src/coherence/mod.rs`** -> AI Confidence: **99.16%**
2969. **`compiler/rustc_hir_analysis/src/coherence/orphan.rs`** -> AI Confidence: **99.16%**
2970. **`compiler/rustc_hir_analysis/src/collect.rs`** -> AI Confidence: **99.16%**
2971. **`compiler/rustc_hir_analysis/src/collect/generics_of.rs`** -> AI Confidence: **99.16%**
2972. **`compiler/rustc_hir_analysis/src/collect/item_bounds.rs`** -> AI Confidence: **99.16%**
2973. **`compiler/rustc_hir_analysis/src/collect/predicates_of.rs`** -> AI Confidence: **99.16%**
2974. **`compiler/rustc_hir_analysis/src/collect/resolve_bound_vars.rs`** -> AI Confidence: **99.16%**
2975. **`compiler/rustc_hir_analysis/src/collect/type_of.rs`** -> AI Confidence: **99.16%**
2976. **`compiler/rustc_hir_analysis/src/collect/type_of/opaque.rs`** -> AI Confidence: **99.16%**
2977. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/bounds.rs`** -> AI Confidence: **99.16%**
2978. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/cmse.rs`** -> AI Confidence: **99.16%**
2979. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/errors.rs`** -> AI Confidence: **99.16%**
2980. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/generics.rs`** -> AI Confidence: **99.16%**
2981. **`compiler/rustc_hir_analysis/src/hir_ty_lowering/mod.rs`** -> AI Confidence: **99.16%**
2982. **`compiler/rustc_hir_analysis/src/hir_wf_check.rs`** -> AI Confidence: **99.16%**
2983. **`compiler/rustc_hir_analysis/src/impl_wf_check.rs`** -> AI Confidence: **99.16%**
2984. **`compiler/rustc_hir_analysis/src/impl_wf_check/min_specialization.rs`** -> AI Confidence: **99.16%**
2985. **`compiler/rustc_hir_analysis/src/lib.rs`** -> AI Confidence: **99.16%**
2986. **`compiler/rustc_hir_analysis/src/variance/constraints.rs`** -> AI Confidence: **99.16%**
2987. **`compiler/rustc_hir_analysis/src/variance/mod.rs`** -> AI Confidence: **99.16%**
2988. **`compiler/rustc_hir_id/src/lib.rs`** -> AI Confidence: **99.16%**
2989. **`compiler/rustc_hir_typeck/src/_match.rs`** -> AI Confidence: **99.16%**
2990. **`compiler/rustc_hir_typeck/src/callee.rs`** -> AI Confidence: **99.16%**
2991. **`compiler/rustc_hir_typeck/src/closure.rs`** -> AI Confidence: **99.16%**
2992. **`compiler/rustc_hir_typeck/src/coercion.rs`** -> AI Confidence: **99.16%**
2993. **`compiler/rustc_hir_typeck/src/fallback.rs`** -> AI Confidence: **99.16%**
2994. **`compiler/rustc_hir_typeck/src/fn_ctxt/_impl.rs`** -> AI Confidence: **99.16%**
2995. **`compiler/rustc_hir_typeck/src/fn_ctxt/mod.rs`** -> AI Confidence: **99.16%**
2996. **`compiler/rustc_hir_typeck/src/inline_asm.rs`** -> AI Confidence: **99.16%**
2997. **`compiler/rustc_hir_typeck/src/intrinsicck.rs`** -> AI Confidence: **99.16%**
2998. **`compiler/rustc_hir_typeck/src/lib.rs`** -> AI Confidence: **99.16%**
2999. **`compiler/rustc_hir_typeck/src/method/mod.rs`** -> AI Confidence: **99.16%**
3000. **`compiler/rustc_hir_typeck/src/method/prelude_edition_lints.rs`** -> AI Confidence: **99.16%**
3001. **`compiler/rustc_hir_typeck/src/method/probe.rs`** -> AI Confidence: **99.16%**
3002. **`compiler/rustc_hir_typeck/src/naked_functions.rs`** -> AI Confidence: **99.16%**
3003. **`compiler/rustc_hir_typeck/src/place_op.rs`** -> AI Confidence: **99.16%**
3004. **`compiler/rustc_hir_typeck/src/upvar.rs`** -> AI Confidence: **99.16%**
3005. **`compiler/rustc_hir_typeck/src/writeback.rs`** -> AI Confidence: **99.16%**
3006. **`compiler/rustc_incremental/src/assert_dep_graph.rs`** -> AI Confidence: **99.16%**
3007. **`compiler/rustc_incremental/src/persist/clean.rs`** -> AI Confidence: **99.16%**
3008. **`compiler/rustc_incremental/src/persist/fs.rs`** -> AI Confidence: **99.16%**
3009. **`compiler/rustc_incremental/src/persist/save.rs`** -> AI Confidence: **99.16%**
3010. **`compiler/rustc_index/src/bit_set.rs`** -> AI Confidence: **99.16%**
3011. **`compiler/rustc_infer/src/infer/at.rs`** -> AI Confidence: **99.16%**
3012. **`compiler/rustc_infer/src/infer/canonical/canonicalizer.rs`** -> AI Confidence: **99.16%**
3013. **`compiler/rustc_infer/src/infer/canonical/instantiate.rs`** -> AI Confidence: **99.16%**
3014. **`compiler/rustc_infer/src/infer/context.rs`** -> AI Confidence: **99.16%**
3015. **`compiler/rustc_infer/src/infer/freshen.rs`** -> AI Confidence: **99.16%**
3016. **`compiler/rustc_infer/src/infer/mod.rs`** -> AI Confidence: **99.16%**
3017. **`compiler/rustc_infer/src/infer/opaque_types/mod.rs`** -> AI Confidence: **99.16%**
3018. **`compiler/rustc_infer/src/infer/outlives/verify.rs`** -> AI Confidence: **99.16%**
3019. **`compiler/rustc_infer/src/infer/region_constraints/leak_check.rs`** -> AI Confidence: **99.16%**
3020. **`compiler/rustc_infer/src/infer/relate/generalize.rs`** -> AI Confidence: **99.16%**
3021. **`compiler/rustc_infer/src/infer/relate/lattice.rs`** -> AI Confidence: **99.16%**
3022. **`compiler/rustc_infer/src/infer/relate/type_relating.rs`** -> AI Confidence: **99.16%**
3023. **`compiler/rustc_interface/src/queries.rs`** -> AI Confidence: **99.16%**
3024. **`compiler/rustc_interface/src/util.rs`** -> AI Confidence: **99.16%**
3025. **`compiler/rustc_lint/src/context.rs`** -> AI Confidence: **99.16%**
3026. **`compiler/rustc_lint/src/deref_into_dyn_supertrait.rs`** -> AI Confidence: **99.16%**
3027. **`compiler/rustc_lint/src/disallowed_pass_by_ref.rs`** -> AI Confidence: **99.16%**
3028. **`compiler/rustc_lint/src/enum_intrinsics_non_enums.rs`** -> AI Confidence: **99.16%**
3029. **`compiler/rustc_lint/src/foreign_modules.rs`** -> AI Confidence: **99.16%**
3030. **`compiler/rustc_lint/src/let_underscore.rs`** -> AI Confidence: **99.16%**
3031. **`compiler/rustc_lint/src/levels.rs`** -> AI Confidence: **99.16%**
3032. **`compiler/rustc_lint/src/lib.rs`** -> AI Confidence: **99.16%**
3033. **`compiler/rustc_lint/src/lifetime_syntax.rs`** -> AI Confidence: **99.16%**
3034. **`compiler/rustc_lint/src/noop_method_call.rs`** -> AI Confidence: **99.16%**
3035. **`compiler/rustc_lint/src/traits.rs`** -> AI Confidence: **99.16%**
3036. **`compiler/rustc_lint/src/types/improper_ctypes.rs`** -> AI Confidence: **99.16%**
3037. **`compiler/rustc_lint_defs/src/lib.rs`** -> AI Confidence: **99.16%**
3038. **`compiler/rustc_log/src/lib.rs`** -> AI Confidence: **99.16%**
3039. **`compiler/rustc_macros/src/extension.rs`** -> AI Confidence: **99.16%**
3040. **`compiler/rustc_macros/src/query.rs`** -> AI Confidence: **99.16%**
3041. **`compiler/rustc_macros/src/symbols.rs`** -> AI Confidence: **99.16%**
3042. **`compiler/rustc_metadata/src/errors.rs`** -> AI Confidence: **99.16%**
3043. **`compiler/rustc_metadata/src/fs.rs`** -> AI Confidence: **99.16%**
3044. **`compiler/rustc_metadata/src/rmeta/decoder.rs`** -> AI Confidence: **99.16%**
3045. **`compiler/rustc_metadata/src/rmeta/decoder/cstore_impl.rs`** -> AI Confidence: **99.16%**
3046. **`compiler/rustc_metadata/src/rmeta/encoder.rs`** -> AI Confidence: **99.16%**
3047. **`compiler/rustc_middle/src/dep_graph/dep_node_key.rs`** -> AI Confidence: **99.16%**
3048. **`compiler/rustc_middle/src/dep_graph/graph.rs`** -> AI Confidence: **99.16%**
3049. **`compiler/rustc_middle/src/lint.rs`** -> AI Confidence: **99.16%**
3050. **`compiler/rustc_middle/src/middle/exported_symbols.rs`** -> AI Confidence: **99.16%**
3051. **`compiler/rustc_middle/src/middle/region.rs`** -> AI Confidence: **99.16%**
3052. **`compiler/rustc_middle/src/middle/stability.rs`** -> AI Confidence: **99.16%**
3053. **`compiler/rustc_middle/src/mir/interpret/allocation/init_mask.rs`** -> AI Confidence: **99.16%**
3054. **`compiler/rustc_middle/src/mir/interpret/allocation/provenance_map.rs`** -> AI Confidence: **99.16%**
3055. **`compiler/rustc_middle/src/mir/interpret/mod.rs`** -> AI Confidence: **99.16%**
3056. **`compiler/rustc_middle/src/mir/interpret/queries.rs`** -> AI Confidence: **99.16%**
3057. **`compiler/rustc_middle/src/mir/mod.rs`** -> AI Confidence: **99.16%**
3058. **`compiler/rustc_middle/src/mir/mono.rs`** -> AI Confidence: **99.16%**
3059. **`compiler/rustc_middle/src/query/inner.rs`** -> AI Confidence: **99.16%**
3060. **`compiler/rustc_middle/src/query/keys.rs`** -> AI Confidence: **99.16%**
3061. **`compiler/rustc_middle/src/thir/visit.rs`** -> AI Confidence: **99.16%**
3062. **`compiler/rustc_middle/src/traits/select.rs`** -> AI Confidence: **99.16%**
3063. **`compiler/rustc_middle/src/traits/solve.rs`** -> AI Confidence: **99.16%**
3064. **`compiler/rustc_middle/src/ty/assoc.rs`** -> AI Confidence: **99.16%**
3065. **`compiler/rustc_middle/src/ty/closure.rs`** -> AI Confidence: **99.16%**
3066. **`compiler/rustc_middle/src/ty/consts.rs`** -> AI Confidence: **99.16%**
3067. **`compiler/rustc_middle/src/ty/consts/kind.rs`** -> AI Confidence: **99.16%**
3068. **`compiler/rustc_middle/src/ty/consts/valtree.rs`** -> AI Confidence: **99.16%**
3069. **`compiler/rustc_middle/src/ty/context.rs`** -> AI Confidence: **99.16%**
3070. **`compiler/rustc_middle/src/ty/generic_args.rs`** -> AI Confidence: **99.16%**
3071. **`compiler/rustc_middle/src/ty/generics.rs`** -> AI Confidence: **99.16%**
3072. **`compiler/rustc_middle/src/ty/instance.rs`** -> AI Confidence: **99.16%**
3073. **`compiler/rustc_middle/src/ty/mod.rs`** -> AI Confidence: **99.16%**
3074. **`compiler/rustc_middle/src/ty/print/mod.rs`** -> AI Confidence: **99.16%**
3075. **`compiler/rustc_middle/src/ty/sty.rs`** -> AI Confidence: **99.16%**
3076. **`compiler/rustc_middle/src/ty/typeck_results.rs`** -> AI Confidence: **99.16%**
3077. **`compiler/rustc_mir_build/src/builder/coverageinfo.rs`** -> AI Confidence: **99.16%**
3078. **`compiler/rustc_mir_build/src/builder/expr/as_temp.rs`** -> AI Confidence: **99.16%**
3079. **`compiler/rustc_mir_build/src/builder/matches/match_pair.rs`** -> AI Confidence: **99.16%**
3080. **`compiler/rustc_mir_build/src/builder/matches/mod.rs`** -> AI Confidence: **99.16%**
3081. **`compiler/rustc_mir_build/src/builder/mod.rs`** -> AI Confidence: **99.16%**
3082. **`compiler/rustc_mir_build/src/builder/scope.rs`** -> AI Confidence: **99.16%**
3083. **`compiler/rustc_mir_build/src/check_tail_calls.rs`** -> AI Confidence: **99.16%**
3084. **`compiler/rustc_mir_build/src/errors.rs`** -> AI Confidence: **99.16%**
3085. **`compiler/rustc_mir_build/src/thir/constant.rs`** -> AI Confidence: **99.16%**
3086. **`compiler/rustc_mir_build/src/thir/cx/expr.rs`** -> AI Confidence: **99.16%**
3087. **`compiler/rustc_mir_build/src/thir/pattern/const_to_pat.rs`** -> AI Confidence: **99.16%**
3088. **`compiler/rustc_mir_build/src/thir/pattern/migration.rs`** -> AI Confidence: **99.16%**
3089. **`compiler/rustc_mir_dataflow/src/framework/cursor.rs`** -> AI Confidence: **99.16%**
3090. **`compiler/rustc_mir_dataflow/src/framework/graphviz.rs`** -> AI Confidence: **99.16%**
3091. **`compiler/rustc_mir_dataflow/src/impls/initialized.rs`** -> AI Confidence: **99.16%**
3092. **`compiler/rustc_mir_dataflow/src/rustc_peek.rs`** -> AI Confidence: **99.16%**
3093. **`compiler/rustc_mir_transform/src/check_call_recursion.rs`** -> AI Confidence: **99.16%**
3094. **`compiler/rustc_mir_transform/src/coroutine.rs`** -> AI Confidence: **99.16%**
3095. **`compiler/rustc_mir_transform/src/coroutine/by_move_body.rs`** -> AI Confidence: **99.16%**
3096. **`compiler/rustc_mir_transform/src/coroutine/drop.rs`** -> AI Confidence: **99.16%**
3097. **`compiler/rustc_mir_transform/src/cross_crate_inline.rs`** -> AI Confidence: **99.16%**
3098. **`compiler/rustc_mir_transform/src/dead_store_elimination.rs`** -> AI Confidence: **99.16%**
3099. **`compiler/rustc_mir_transform/src/dest_prop.rs`** -> AI Confidence: **99.16%**
3100. **`compiler/rustc_mir_transform/src/elaborate_drops.rs`** -> AI Confidence: **99.16%**
3101. **`compiler/rustc_mir_transform/src/function_item_references.rs`** -> AI Confidence: **99.16%**
3102. **`compiler/rustc_mir_transform/src/inline.rs`** -> AI Confidence: **99.16%**
3103. **`compiler/rustc_mir_transform/src/instsimplify.rs`** -> AI Confidence: **99.16%**
3104. **`compiler/rustc_mir_transform/src/jump_threading.rs`** -> AI Confidence: **99.16%**
3105. **`compiler/rustc_mir_transform/src/lint_tail_expr_drop_order.rs`** -> AI Confidence: **99.16%**
3106. **`compiler/rustc_mir_transform/src/promote_consts.rs`** -> AI Confidence: **99.16%**
3107. **`compiler/rustc_mir_transform/src/remove_uninit_drops.rs`** -> AI Confidence: **99.16%**
3108. **`compiler/rustc_mir_transform/src/simplify.rs`** -> AI Confidence: **99.16%**
3109. **`compiler/rustc_mir_transform/src/sroa.rs`** -> AI Confidence: **99.16%**
3110. **`compiler/rustc_mir_transform/src/ssa_range_prop.rs`** -> AI Confidence: **99.16%**
3111. **`compiler/rustc_mir_transform/src/trivial_const.rs`** -> AI Confidence: **99.16%**
3112. **`compiler/rustc_monomorphize/src/collector.rs`** -> AI Confidence: **99.16%**
3113. **`compiler/rustc_monomorphize/src/partitioning.rs`** -> AI Confidence: **99.16%**
3114. **`compiler/rustc_next_trait_solver/src/coherence.rs`** -> AI Confidence: **99.16%**
3115. **`compiler/rustc_next_trait_solver/src/solve/assembly/mod.rs`** -> AI Confidence: **99.16%**
3116. **`compiler/rustc_next_trait_solver/src/solve/eval_ctxt/mod.rs`** -> AI Confidence: **99.16%**
3117. **`compiler/rustc_next_trait_solver/src/solve/normalizes_to/mod.rs`** -> AI Confidence: **99.16%**
3118. **`compiler/rustc_next_trait_solver/src/solve/trait_goals.rs`** -> AI Confidence: **99.16%**
3119. **`compiler/rustc_parse/src/lexer/mod.rs`** -> AI Confidence: **99.16%**
3120. **`compiler/rustc_parse/src/lexer/tokentrees.rs`** -> AI Confidence: **99.16%**
3121. **`compiler/rustc_parse/src/lexer/unicode_chars.rs`** -> AI Confidence: **99.16%**
3122. **`compiler/rustc_parse/src/lib.rs`** -> AI Confidence: **99.16%**
3123. **`compiler/rustc_parse/src/parser/attr_wrapper.rs`** -> AI Confidence: **99.16%**
3124. **`compiler/rustc_parse/src/parser/tests.rs`** -> AI Confidence: **99.16%**
3125. **`compiler/rustc_passes/src/abi_test.rs`** -> AI Confidence: **99.16%**
3126. **`compiler/rustc_passes/src/check_attr.rs`** -> AI Confidence: **99.16%**
3127. **`compiler/rustc_passes/src/check_export.rs`** -> AI Confidence: **99.16%**
3128. **`compiler/rustc_passes/src/dead.rs`** -> AI Confidence: **99.16%**
3129. **`compiler/rustc_passes/src/lang_items.rs`** -> AI Confidence: **99.16%**
3130. **`compiler/rustc_passes/src/layout_test.rs`** -> AI Confidence: **99.16%**
3131. **`compiler/rustc_passes/src/upvars.rs`** -> AI Confidence: **99.16%**
3132. **`compiler/rustc_pattern_analysis/src/lints.rs`** -> AI Confidence: **99.16%**
3133. **`compiler/rustc_pattern_analysis/src/rustc.rs`** -> AI Confidence: **99.16%**
3134. **`compiler/rustc_pattern_analysis/tests/common/mod.rs`** -> AI Confidence: **99.16%**
3135. **`compiler/rustc_privacy/src/lib.rs`** -> AI Confidence: **99.16%**
3136. **`compiler/rustc_public/src/abi.rs`** -> AI Confidence: **99.16%**
3137. **`compiler/rustc_public/src/ty.rs`** -> AI Confidence: **99.16%**
3138. **`compiler/rustc_public/src/unstable/convert/stable/abi.rs`** -> AI Confidence: **99.16%**
3139. **`compiler/rustc_public/src/unstable/convert/stable/mir.rs`** -> AI Confidence: **99.16%**
3140. **`compiler/rustc_public_bridge/src/context/mod.rs`** -> AI Confidence: **99.16%**
3141. **`compiler/rustc_query_impl/src/execution.rs`** -> AI Confidence: **99.16%**
3142. **`compiler/rustc_query_impl/src/handle_cycle_error.rs`** -> AI Confidence: **99.16%**
3143. **`compiler/rustc_query_impl/src/job.rs`** -> AI Confidence: **99.16%**
3144. **`compiler/rustc_query_impl/src/plumbing.rs`** -> AI Confidence: **99.16%**
3145. **`compiler/rustc_resolve/src/def_collector.rs`** -> AI Confidence: **99.16%**
3146. **`compiler/rustc_resolve/src/effective_visibilities.rs`** -> AI Confidence: **99.16%**
3147. **`compiler/rustc_resolve/src/late.rs`** -> AI Confidence: **99.16%**
3148. **`compiler/rustc_resolve/src/lib.rs`** -> AI Confidence: **99.16%**
3149. **`compiler/rustc_sanitizers/src/cfi/typeid/itanium_cxx_abi/mod.rs`** -> AI Confidence: **99.16%**
3150. **`compiler/rustc_sanitizers/src/cfi/typeid/itanium_cxx_abi/transform.rs`** -> AI Confidence: **99.16%**
3151. **`compiler/rustc_serialize/src/serialize.rs`** -> AI Confidence: **99.16%**
3152. **`compiler/rustc_session/src/config.rs`** -> AI Confidence: **99.16%**
3153. **`compiler/rustc_session/src/config/print_request.rs`** -> AI Confidence: **99.16%**
3154. **`compiler/rustc_session/src/parse.rs`** -> AI Confidence: **99.16%**
3155. **`compiler/rustc_span/src/def_id.rs`** -> AI Confidence: **99.16%**
3156. **`compiler/rustc_span/src/lib.rs`** -> AI Confidence: **99.16%**
3157. **`compiler/rustc_span/src/symbol.rs`** -> AI Confidence: **99.16%**
3158. **`compiler/rustc_symbol_mangling/src/export.rs`** -> AI Confidence: **99.16%**
3159. **`compiler/rustc_target/src/callconv/mod.rs`** -> AI Confidence: **99.16%**
3160. **`compiler/rustc_target/src/spec/base/apple/tests.rs`** -> AI Confidence: **99.16%**
3161. **`compiler/rustc_target/src/spec/json.rs`** -> AI Confidence: **99.16%**
3162. **`compiler/rustc_thread_pool/src/registry.rs`** -> AI Confidence: **99.16%**
3163. **`compiler/rustc_thread_pool/src/sleep/mod.rs`** -> AI Confidence: **99.16%**
3164. **`compiler/rustc_thread_pool/src/thread_pool/mod.rs`** -> AI Confidence: **99.16%**
3165. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/find_anon_type.rs`** -> AI Confidence: **99.16%**
3166. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/mismatched_static_lifetime.rs`** -> AI Confidence: **99.16%**
3167. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/placeholder_error.rs`** -> AI Confidence: **99.16%**
3168. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/trait_impl_difference.rs`** -> AI Confidence: **99.16%**
3169. **`compiler/rustc_trait_selection/src/error_reporting/infer/nice_region_error/util.rs`** -> AI Confidence: **99.16%**
3170. **`compiler/rustc_trait_selection/src/error_reporting/traits/mod.rs`** -> AI Confidence: **99.16%**
3171. **`compiler/rustc_trait_selection/src/error_reporting/traits/on_unimplemented.rs`** -> AI Confidence: **99.16%**
3172. **`compiler/rustc_trait_selection/src/opaque_types.rs`** -> AI Confidence: **99.16%**
3173. **`compiler/rustc_trait_selection/src/solve/fulfill.rs`** -> AI Confidence: **99.16%**
3174. **`compiler/rustc_trait_selection/src/solve/fulfill/derive_errors.rs`** -> AI Confidence: **99.16%**
3175. **`compiler/rustc_trait_selection/src/solve/normalize.rs`** -> AI Confidence: **99.16%**
3176. **`compiler/rustc_trait_selection/src/solve/select.rs`** -> AI Confidence: **99.16%**
3177. **`compiler/rustc_trait_selection/src/traits/auto_trait.rs`** -> AI Confidence: **99.16%**
3178. **`compiler/rustc_trait_selection/src/traits/coherence.rs`** -> AI Confidence: **99.16%**
3179. **`compiler/rustc_trait_selection/src/traits/dyn_compatibility.rs`** -> AI Confidence: **99.16%**
3180. **`compiler/rustc_trait_selection/src/traits/effects.rs`** -> AI Confidence: **99.16%**
3181. **`compiler/rustc_trait_selection/src/traits/fulfill.rs`** -> AI Confidence: **99.16%**
3182. **`compiler/rustc_trait_selection/src/traits/misc.rs`** -> AI Confidence: **99.16%**
3183. **`compiler/rustc_trait_selection/src/traits/project.rs`** -> AI Confidence: **99.16%**
3184. **`compiler/rustc_trait_selection/src/traits/query/dropck_outlives.rs`** -> AI Confidence: **99.16%**
3185. **`compiler/rustc_trait_selection/src/traits/query/evaluate_obligation.rs`** -> AI Confidence: **99.16%**
3186. **`compiler/rustc_trait_selection/src/traits/query/normalize.rs`** -> AI Confidence: **99.16%**
3187. **`compiler/rustc_trait_selection/src/traits/query/type_op/normalize.rs`** -> AI Confidence: **99.16%**
3188. **`compiler/rustc_trait_selection/src/traits/vtable.rs`** -> AI Confidence: **99.16%**
3189. **`compiler/rustc_trait_selection/src/traits/wf.rs`** -> AI Confidence: **99.16%**
3190. **`compiler/rustc_transmute/src/layout/mod.rs`** -> AI Confidence: **99.16%**
3191. **`compiler/rustc_transmute/src/layout/tree.rs`** -> AI Confidence: **99.16%**
3192. **`compiler/rustc_transmute/src/lib.rs`** -> AI Confidence: **99.16%**
3193. **`compiler/rustc_transmute/src/maybe_transmutable/mod.rs`** -> AI Confidence: **99.16%**
3194. **`compiler/rustc_ty_utils/src/layout.rs`** -> AI Confidence: **99.16%**
3195. **`compiler/rustc_ty_utils/src/needs_drop.rs`** -> AI Confidence: **99.16%**
3196. **`compiler/rustc_ty_utils/src/opaque_types.rs`** -> AI Confidence: **99.16%**
3197. **`compiler/rustc_ty_utils/src/sig_types.rs`** -> AI Confidence: **99.16%**
3198. **`compiler/rustc_ty_utils/src/ty.rs`** -> AI Confidence: **99.16%**
3199. **`compiler/rustc_type_ir/src/binder.rs`** -> AI Confidence: **99.16%**
3200. **`compiler/rustc_type_ir/src/const_kind.rs`** -> AI Confidence: **99.16%**
3201. **`compiler/rustc_type_ir/src/fold.rs`** -> AI Confidence: **99.16%**
3202. **`compiler/rustc_type_ir/src/inherent.rs`** -> AI Confidence: **99.16%**
3203. **`compiler/rustc_type_ir/src/interner.rs`** -> AI Confidence: **99.16%**
3204. **`compiler/rustc_type_ir/src/predicate.rs`** -> AI Confidence: **99.16%**
3205. **`compiler/rustc_type_ir/src/relate/solver_relating.rs`** -> AI Confidence: **99.16%**
3206. **`compiler/rustc_type_ir/src/solve/mod.rs`** -> AI Confidence: **99.16%**
3207. **`compiler/rustc_type_ir/src/ty_kind.rs`** -> AI Confidence: **99.16%**
3208. **`compiler/rustc_type_ir/src/ty_kind/closure.rs`** -> AI Confidence: **99.16%**
3209. **`compiler/rustc_type_ir/src/visit.rs`** -> AI Confidence: **99.16%**
3210. **`library/alloc/src/borrow.rs`** -> AI Confidence: **99.16%**
3211. **`library/alloc/src/boxed.rs`** -> AI Confidence: **99.16%**
3212. **`library/alloc/src/bstr.rs`** -> AI Confidence: **99.16%**
3213. **`library/alloc/src/collections/binary_heap/mod.rs`** -> AI Confidence: **99.16%**
3214. **`library/alloc/src/collections/linked_list.rs`** -> AI Confidence: **99.16%**
3215. **`library/alloc/src/collections/vec_deque/tests.rs`** -> AI Confidence: **99.16%**
3216. **`library/alloc/src/ffi/c_str.rs`** -> AI Confidence: **99.16%**
3217. **`library/alloc/src/raw_vec/mod.rs`** -> AI Confidence: **99.16%**
3218. **`library/alloc/src/rc.rs`** -> AI Confidence: **99.16%**
3219. **`library/alloc/src/string.rs`** -> AI Confidence: **99.16%**
3220. **`library/alloc/src/sync.rs`** -> AI Confidence: **99.16%**
3221. **`library/compiler-builtins/crates/libm-macros/src/lib.rs`** -> AI Confidence: **99.16%**
3222. **`library/compiler-builtins/libm-test/src/test_traits.rs`** -> AI Confidence: **99.16%**
3223. **`library/compiler-builtins/libm/src/math/support/big/tests.rs`** -> AI Confidence: **99.16%**
3224. **`library/core/src/any.rs`** -> AI Confidence: **99.16%**
3225. **`library/core/src/char/mod.rs`** -> AI Confidence: **99.16%**
3226. **`library/core/src/ffi/c_str.rs`** -> AI Confidence: **99.16%**
3227. **`library/core/src/fmt/mod.rs`** -> AI Confidence: **99.16%**
3228. **`library/core/src/iter/adapters/chain.rs`** -> AI Confidence: **99.16%**
3229. **`library/core/src/iter/adapters/skip.rs`** -> AI Confidence: **99.16%**
3230. **`library/core/src/iter/adapters/zip.rs`** -> AI Confidence: **99.16%**
3231. **`library/core/src/iter/range.rs`** -> AI Confidence: **99.16%**
3232. **`library/core/src/mem/alignment.rs`** -> AI Confidence: **99.16%**
3233. **`library/core/src/mem/manually_drop.rs`** -> AI Confidence: **99.16%**
3234. **`library/core/src/net/parser.rs`** -> AI Confidence: **99.16%**
3235. **`library/core/src/num/mod.rs`** -> AI Confidence: **99.16%**
3236. **`library/core/src/num/saturating.rs`** -> AI Confidence: **99.16%**
3237. **`library/core/src/panic/unwind_safe.rs`** -> AI Confidence: **99.16%**
3238. **`library/core/src/range.rs`** -> AI Confidence: **99.16%**
3239. **`library/core/src/result.rs`** -> AI Confidence: **99.16%**
3240. **`library/core/src/slice/ascii.rs`** -> AI Confidence: **99.16%**
3241. **`library/core/src/slice/cmp.rs`** -> AI Confidence: **99.16%**
3242. **`library/core/src/slice/iter.rs`** -> AI Confidence: **99.16%**
3243. **`library/core/src/str/mod.rs`** -> AI Confidence: **99.16%**
3244. **`library/core/src/sync/atomic.rs`** -> AI Confidence: **99.16%**
3245. **`library/core/src/task/wake.rs`** -> AI Confidence: **99.16%**
3246. **`library/proc_macro/src/quote.rs`** -> AI Confidence: **99.16%**
3247. **`library/proc_macro/src/to_tokens.rs`** -> AI Confidence: **99.16%**
3248. **`library/std/src/alloc.rs`** -> AI Confidence: **99.16%**
3249. **`library/std/src/backtrace.rs`** -> AI Confidence: **99.16%**
3250. **`library/std/src/env.rs`** -> AI Confidence: **99.16%**
3251. **`library/std/src/error.rs`** -> AI Confidence: **99.16%**
3252. **`library/std/src/ffi/os_str.rs`** -> AI Confidence: **99.16%**
3253. **`library/std/src/io/buffered/bufreader.rs`** -> AI Confidence: **99.16%**
3254. **`library/std/src/io/copy.rs`** -> AI Confidence: **99.16%**
3255. **`library/std/src/io/mod.rs`** -> AI Confidence: **99.16%**
3256. **`library/std/src/os/unix/io/mod.rs`** -> AI Confidence: **99.16%**
3257. **`library/std/src/os/unix/net/addr.rs`** -> AI Confidence: **99.16%**
3258. **`library/std/src/os/unix/net/datagram.rs`** -> AI Confidence: **99.16%**
3259. **`library/std/src/os/unix/net/listener.rs`** -> AI Confidence: **99.16%**
3260. **`library/std/src/os/windows/ffi.rs`** -> AI Confidence: **99.16%**
3261. **`library/std/src/os/windows/io/raw.rs`** -> AI Confidence: **99.16%**
3262. **`library/std/src/os/windows/io/socket.rs`** -> AI Confidence: **99.16%**
3263. **`library/std/src/os/windows/net/addr.rs`** -> AI Confidence: **99.16%**
3264. **`library/std/src/os/windows/net/stream.rs`** -> AI Confidence: **99.16%**
3265. **`library/std/src/process.rs`** -> AI Confidence: **99.16%**
3266. **`library/std/src/process/tests.rs`** -> AI Confidence: **99.16%**
3267. **`library/std/src/rt.rs`** -> AI Confidence: **99.16%**
3268. **`library/std/src/sync/mpmc/list.rs`** -> AI Confidence: **99.16%**
3269. **`library/std/src/sync/mpmc/mod.rs`** -> AI Confidence: **99.16%**
3270. **`library/std/src/sync/mpmc/zero.rs`** -> AI Confidence: **99.16%**
3271. **`library/std/src/sync/mpsc.rs`** -> AI Confidence: **99.16%**
3272. **`library/std/src/sync/nonpoison/rwlock.rs`** -> AI Confidence: **99.16%**
3273. **`library/std/src/sync/once.rs`** -> AI Confidence: **99.16%**
3274. **`library/std/src/sync/oneshot.rs`** -> AI Confidence: **99.16%**
3275. **`library/std/src/sync/poison/condvar.rs`** -> AI Confidence: **99.16%**
3276. **`library/std/src/sync/poison/rwlock.rs`** -> AI Confidence: **99.16%**
3277. **`library/std/src/sync/reentrant_lock.rs`** -> AI Confidence: **99.16%**
3278. **`library/std/src/sys/args/windows.rs`** -> AI Confidence: **99.16%**
3279. **`library/std/src/sys/fd/hermit.rs`** -> AI Confidence: **99.16%**
3280. **`library/std/src/sys/fd/unix.rs`** -> AI Confidence: **99.16%**
3281. **`library/std/src/sys/fs/hermit.rs`** -> AI Confidence: **99.16%**
3282. **`library/std/src/sys/fs/uefi.rs`** -> AI Confidence: **99.16%**
3283. **`library/std/src/sys/fs/unix/dir.rs`** -> AI Confidence: **99.16%**
3284. **`library/std/src/sys/fs/vexos.rs`** -> AI Confidence: **99.16%**
3285. **`library/std/src/sys/fs/windows.rs`** -> AI Confidence: **99.16%**
3286. **`library/std/src/sys/net/connection/motor.rs`** -> AI Confidence: **99.16%**
3287. **`library/std/src/sys/net/connection/socket/hermit.rs`** -> AI Confidence: **99.16%**
3288. **`library/std/src/sys/net/connection/socket/mod.rs`** -> AI Confidence: **99.16%**
3289. **`library/std/src/sys/net/connection/socket/solid.rs`** -> AI Confidence: **99.16%**
3290. **`library/std/src/sys/net/connection/socket/unix.rs`** -> AI Confidence: **99.16%**
3291. **`library/std/src/sys/net/connection/socket/windows.rs`** -> AI Confidence: **99.16%**
3292. **`library/std/src/sys/net/connection/uefi/tcp4.rs`** -> AI Confidence: **99.16%**
3293. **`library/std/src/sys/net/connection/wasip1.rs`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `40` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `106475` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/tools/rust-analyzer/editors/code/src/dependencies_provider.ts` (TYPESCRIPT) -> Cumulative Risk: **677.51**
- **Archetype:** `file_cluster_4` (Distance: 12.349 IQR)
- **Magnitude:** 16.02 | **LOC:** 155 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9621%), Tech Debt (99.8674%)
- **Heaviest Functions:** `getChildren` (Impact: 11.6), `constructor` (Impact: 8.1), `getRootDependencies` (Impact: 6.8)

### 2. `src/ci/run.sh` (SHELL) -> Cumulative Risk: **677.35**
- **Archetype:** `file_cluster_4` (Distance: 13.611 IQR)
- **Magnitude:** 29.9 | **LOC:** 283 | **CtrlFlow:** 89.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3714%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 58.4), `datecheck` (Impact: 13.1), `Anonymous_Block` (Impact: 10.9)

### 3. `src/etc/gdb_providers.py` (PYTHON) -> Cumulative Risk: **673.42**
- **Archetype:** `file_cluster_0` (Distance: 11.638 IQR)
- **Magnitude:** 456.58 | **LOC:** 504 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9971%)
- **Heaviest Functions:** `children_of_btree_map` (Impact: 28.4), `children_of_node` (Impact: 22.7), `__init__` (Impact: 11.2)

### 4. `compiler/rustc_index/src/vec.rs` (RUST) -> Cumulative Risk: **650.98**
- **Archetype:** `file_cluster_0` (Distance: 13.227 IQR)
- **Magnitude:** 204.92 | **LOC:** 352 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7462%), Documentation (84.7634%), Tech Debt (82.7075%)
- **Heaviest Functions:** `drain_enumerated` (Impact: 4.6), `ensure_contains_elem` (Impact: 4.5), `insert` (Impact: 4.2)

### 5. `src/tools/cherry-pick.sh` (SHELL) -> Cumulative Risk: **643.59**
- **Archetype:** `file_cluster_4` (Distance: 11.353 IQR)
- **Magnitude:** 0.02 | **LOC:** 35 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9835%), Concurrency (99.9317%), State Flux (99.1809%)
- **Heaviest Functions:** `commit_message_with_backport_note_[Trunc` (Impact: 5.0), `full_sha` (Impact: 3.1), `print_error` (Impact: 1.7)

### 6. `src/ci/scripts/checkout-submodules.sh` (SHELL) -> Cumulative Risk: **640.85**
- **Archetype:** `file_cluster_4` (Distance: 14.043 IQR)
- **Magnitude:** 8.61 | **LOC:** 74 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9364%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 23.5), `__global_context__` (Impact: 5.6), `Anonymous_Block` (Impact: 5.2)

### 7. `src/etc/lldb_providers.py` (PYTHON) -> Cumulative Risk: **639.64**
- **Archetype:** `file_cluster_16` (Distance: 12.684 IQR)
- **Magnitude:** 825.24 | **LOC:** 1400 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9421%)
- **Heaviest Functions:** `StdStrSummaryProvider` (Impact: 159.5), `update` (Impact: 30.1), `get_template_args` (Impact: 16.9)

### 8. `library/std/src/os/unix/net/tests.rs` (RUST) -> Cumulative Risk: **631.61**
- **Archetype:** `file_cluster_0` (Distance: 12.555 IQR)
- **Magnitude:** 414.68 | **LOC:** 819 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.992%), Safety Score (99.977%), Concurrency (97.4628%)
- **Heaviest Functions:** `long_path` (Impact: 13.4), `test_unix_stream_peek` (Impact: 10.3), `test_send_vectored_with_ancillary_to_uni` (Impact: 8.6)

### 9. `library/std/src/sys/sync/once/no_threads.rs` (RUST) -> Cumulative Risk: **629.59**
- **Archetype:** `file_cluster_0` (Distance: 10.603 IQR)
- **Magnitude:** 62.5 | **LOC:** 120 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.593%), State Flux (94.2676%)
- **Heaviest Functions:** `call` (Impact: 7.5), `state` (Impact: 4.5), `set_state` (Impact: 3.9)

### 10. `src/librustdoc/html/static/js/stringdex.js` (JAVASCRIPT) -> Cumulative Risk: **621.38**
- **Archetype:** `file_cluster_8` (Distance: 13.986 IQR)
- **Magnitude:** 1577.66 | **LOC:** 4412 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.5116%), Safety Score (85.3533%)
- **Heaviest Functions:** `constructor` (Impact: 82.7), `intersection` (Impact: 54.8), `union` (Impact: 52.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `library/alloc/src/collections/btree/set.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 18.475 IQR)
- **Top Global Matches:** file_cluster_0: 18.475, file_cluster_17: 18.715, file_cluster_11: 18.728
- **Magnitude:** 23291.81 | **LOC:** 2535 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.4104%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 520`, `args: 166`, `func_start: 126`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 231`, `dead_code: 151`
* *Architecture:* `api: 72`, `import: 69`
* *Defense:* `safety: 177`, `doc: 1136`, `test: 109`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BitXor, core::borrow::Borrow, self::entry::Entry, min, core::hash::Hash, TrustedLen, BTreeMap, Keys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/librustdoc/html/static/js/search.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.913 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.873 IQR)
- **Top Global Matches:** file_cluster_4: 13.913, file_cluster_0: 14.109, file_cluster_17: 14.289
- **Magnitude:** 6043.54 | **LOC:** 5573 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.4545%), Tech Debt (66.5397%)
**Top Internal Functions/Classes:**
  * `unifyGenericTypes` (Impact: 924.0)
  * `getItemsBefore` (Impact: 880.5)
  * `initSearch` (Impact: 806.0)
    * *Intent:* /**
  * `formatDisplayTypeSignature` (Impact: 680.6)
  * `execQuery` (Impact: 621.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 300`, `args: 94`, `func_start: 95`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 545`, `dead_code: 5`, `duplicate_logic: 17`, `orphaned_logic: 24`
* *Architecture:* `io: 79`, `api: 1`, `concurrency: 365`
* *Defense:* `safety: 261`, `doc: 303`, `test: 5`, `immutability_locks: 226`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/ui/expr/if/expr-stack-overflow.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.647 IQR)
- **Top Global Matches:** file_cluster_8: 10.647, file_cluster_7: 11.294, file_cluster_1: 11.472
- **Magnitude:** 5431.72 | **LOC:** 10421 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4342%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `banana` (Impact: 5223.4)
    * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-ti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10410`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.664 IQR)
- **Top Global Matches:** file_cluster_8: 10.664, file_cluster_7: 10.868, file_cluster_0: 10.893
- **Magnitude:** 4191.82 | **LOC:** 27594 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.7666%), Tech Debt (99.9069%)
**Top Internal Functions/Classes:**
  * `vcvtsh2sd` (Impact: 69.3)
    * *Intent:* /// Compare packed half-precision (16-bit) floating-point elements in a and b, and store packed mini...
  * `_mm512_setr_ph` (Impact: 8.0)
  * `_mm_mask3_fmadd_round_sh` (Impact: 6.0)
    * *Intent:* /// Multiply the lower complex numbers in a and b, and store the result in the lower elements of dst...
  * `_mm_mask3_fmsub_round_sh` (Impact: 6.0)
    * *Intent:* /// Multiply packed complex numbers in a and b, and store the results in dst using zeromask k (the e...
  * `_mm_mask3_fnmadd_round_sh` (Impact: 6.0)
    * *Intent:* /// Multiply packed complex numbers in a by the complex conjugates of packed complex numbers in b, a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 3906`, `args: 1544`, `func_start: 1544`
* *Risk/State:* `state_mutation: 53`, `dead_code: 11`, `fragile_debt: 2`, `orphaned_logic: 931`
* *Architecture:* `io: 21`, `api: 469`, `import: 8`
* *Defense:* `doc: 6405`, `test: 60`, `immutability_locks: 483`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::arch::asm, crate::intrinsics::fmaf16, crate::core_arch::simd::*, x86::*, simd::*, crate::ptr, crate::core_arch::x86::*, addr_of_mut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_trait_selection/src/error_reporting/traits/suggestions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.746 IQR)
- **Top Global Matches:** file_cluster_8: 13.746, file_cluster_17: 13.811, file_cluster_11: 13.814
- **Magnitude:** 4020.84 | **LOC:** 6062 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (34.1035%), Tech Debt (43.072%)
**Top Internal Functions/Classes:**
  * `note_function_argument_obligation` (Impact: 699.4)
  * `extract_callable_info` (Impact: 550.0)
  * `suggest_add_clone_to_arg` (Impact: 504.6)
  * `suggest_change_mut` (Impact: 419.9)
  * `look_for_iterator_item_mistakes` (Impact: 384.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 780`, `structural_boundaries: 1093`, `args: 199`, `func_start: 49`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 347`, `dead_code: 13`, `planned_debt: 15`, `fragile_debt: 22`, `duplicate_logic: 7`
* *Architecture:* `api: 56`, `concurrency: 133`, `import: 38`
* *Defense:* `safety: 499`, `doc: 96`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` struct_span_code_err, iter, ObligationCtxt, Symbol, TypeSuperFoldable, with_forced_trimmed_paths, suggest_arbitrary_trait_bound, CoroutineDesugaring...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.15 IQR)
- **Top Global Matches:** file_cluster_8: 10.15, file_cluster_0: 10.342, file_cluster_7: 10.448
- **Magnitude:** 3833.22 | **LOC:** 22275 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (2.8714%), Tech Debt (99.8892%)
**Top Internal Functions/Classes:**
  * `vpmovuswbmem` (Impact: 63.1)
  * `_mm512_alignr_epi8` (Impact: 17.4)
  * `_mm512_bslli_epi128` (Impact: 14.3)
    * *Intent:* /// Load packed 16-bit integers from memory into dst using zeromask k /// (elements are zeroed out w...
  * `_mm512_srli_epi16` (Impact: 8.1)
    * *Intent:* /// Compare packed unsigned 16-bit integers in a and b for equality, and store the results in mask v...
  * `_mm512_mask_slli_epi16` (Impact: 7.7)
    * *Intent:* /// Compare packed signed 16-bit integers in a and b for greater-than-or-equal, and store the result...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 3883`, `args: 1290`, `func_start: 1262`
* *Risk/State:* `state_mutation: 98`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 827`
* *Architecture:* `api: 413`, `import: 7`
* *Defense:* `safety: 12`, `doc: 2524`, `test: 331`, `immutability_locks: 1144`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    core_arch::simd::*, crate::hint::black_box, stdarch_test::assert_instr, x86::*, intrinsics::simd::*, ptr, crate::core_arch::x86::*, crate::core_arch::assert_eq_const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_parse/src/parser/item.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.939 IQR)
- **Top Global Matches:** file_cluster_13: 14.939, file_cluster_11: 14.952, file_cluster_17: 14.991
- **Magnitude:** 3538.34 | **LOC:** 3645 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (27.479%), Tech Debt (17.3159%)
**Top Internal Functions/Classes:**
  * `parse_item_list` (Impact: 662.0)
  * `is_use_closure` (Impact: 513.5)
  * `parse_tuple_struct_body` (Impact: 352.9)
  * `parse_item_kind` (Impact: 306.7)
    * *Intent:* /// Parses one of the items allowed by the flags.
  * `expect_field_ty_separator` (Impact: 130.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 613`, `structural_boundaries: 623`, `args: 152`, `func_start: 59`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 283`, `dead_code: 24`, `fragile_debt: 13`
* *Architecture:* `api: 26`, `concurrency: 7`, `import: 33`
* *Defense:* `safety: 369`, `doc: 230`, `sync_locks: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MacroExpandsToAdtField, struct_span_code_err, kw, thin_vec, super::ty::AllowPlus, TokenTree, crate::errors::self, std::mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/mips/msa.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.697 IQR)
- **Top Global Matches:** file_cluster_0: 9.697, file_cluster_8: 9.8, file_cluster_7: 10.081
- **Magnitude:** 3377.76 | **LOC:** 18398 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (97.8276%)
**Top Internal Functions/Classes:**
  * `test_msa_binsl_b` (Impact: 3.7)
  * `test_msa_binsr_b` (Impact: 3.7)
  * `test_msa_bmnz_v` (Impact: 3.7)
  * `test_msa_bmz_v` (Impact: 3.7)
  * `test_msa_bsel_v` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1496`, `args: 1569`, `func_start: 1569`, `class_start: 10`
* *Risk/State:* `state_mutation: 40`, `dead_code: 85`, `fragile_debt: 15`, `orphaned_logic: 527`
* *Architecture:* `api: 533`, `import: 4`
* *Defense:* `doc: 3559`, `test: 527`, `immutability_locks: 138`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
        core_arch::mips::msa::*, crate::mem, stdarch_test::assert_instr, simd::*, stdarch_test::simd_test, mem
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_typeck/src/fn_ctxt/suggestions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.289 IQR)
- **Top Global Matches:** file_cluster_13: 13.289, file_cluster_8: 13.311, file_cluster_16: 13.333
- **Magnitude:** 3276.22 | **LOC:** 3743 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (8.199%), Tech Debt (13.1381%)
**Top Internal Functions/Classes:**
  * `suggest_into` (Impact: 596.0)
  * `suggest_associated_const` (Impact: 531.9)
  * `suggest_missing_break_or_return_expr` (Impact: 477.9)
  * `suggest_deref_ref_or_into` (Impact: 304.7)
  * `suggest_cast` (Impact: 264.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 615`, `args: 99`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 130`, `dead_code: 19`, `planned_debt: 4`, `fragile_debt: 9`
* *Architecture:* `api: 55`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 332`, `doc: 114`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` StmtKind, GenericBound, MacroKind, crate::errors, rustc_errors::Applicability, Arm, rustc_session::errors::ExprParenthesesNeeded, Span...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.079 IQR)
- **Top Global Matches:** file_cluster_8: 9.079, file_cluster_0: 9.602, file_cluster_7: 9.82
- **Magnitude:** 3242.62 | **LOC:** 13199 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6742%), Tech Debt (99.955%)
**Top Internal Functions/Classes:**
  * `vcvttsd2usi64` (Impact: 68.4)
  * `test_mm512_mask_i32scatter_pd` (Impact: 4.3)
  * `test_mm512_mask_i64scatter_pd` (Impact: 4.3)
  * `test_mm512_mask_i64scatter_ps` (Impact: 4.3)
  * `test_mm512_mask_i32scatter_epi64` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 5280`, `args: 1219`, `func_start: 1213`, `class_start: 4`
* *Risk/State:* `state_mutation: 238`, `orphaned_logic: 1186`
* *Architecture:* `api: 15`, `import: 7`
* *Defense:* `doc: 168`, `test: 220`, `immutability_locks: 659`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    core_arch::simd::*, crate::hint::black_box, crate::core_arch::x86_64::*, x86_64::*, stdarch_test::assert_instr, x86::*, crate::core_arch::x86::*, crate::core_arch::assert_eq_const...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_borrowck/src/diagnostics/conflict_errors.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.217 IQR)
- **Top Global Matches:** file_cluster_17: 14.217, file_cluster_11: 14.249, file_cluster_13: 14.261
- **Magnitude:** 3059.42 | **LOC:** 4741 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (22.3575%), Tech Debt (71.5829%)
**Top Internal Functions/Classes:**
  * `report_use_of_moved_or_uninitialized` (Impact: 659.2)
  * `get_moved_indexes` (Impact: 423.0)
  * `annotate_argument_and_return_for_borrow` (Impact: 205.1)
  * `explain_iterator_advancement_in_for_loop` (Impact: 128.1)
  * `suggest_cloning` (Impact: 119.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 707`, `structural_boundaries: 964`, `args: 143`, `func_start: 55`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 359`, `dead_code: 34`, `planned_debt: 4`, `fragile_debt: 16`, `duplicate_logic: 16`, `orphaned_logic: 13`
* *Architecture:* `api: 12`, `concurrency: 8`, `import: 57`
* *Defense:* `safety: 471`, `doc: 110`, `test: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` struct_span_code_err, Place, rustc_span::def_id::DefId, rustc_span::BytePos, rustc_errors::Applicability, Rvalue, ObligationCtxt, Symbol...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_typeck/src/pat.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.648 IQR)
- **Top Global Matches:** file_cluster_16: 13.648, file_cluster_13: 13.69, file_cluster_8: 13.76
- **Magnitude:** 3032.36 | **LOC:** 3341 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (10.1978%), Tech Debt (21.4033%)
**Top Internal Functions/Classes:**
  * `check_pat_ident` (Impact: 619.0)
  * `check_deref_pattern` (Impact: 453.4)
  * `check_pat` (Impact: 447.9)
  * `pattern_cause` (Impact: 387.1)
  * `error_inexistent_fields` (Impact: 262.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 461`, `args: 107`, `func_start: 55`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 139`, `dead_code: 13`, `planned_debt: 4`, `fragile_debt: 15`
* *Architecture:* `api: 6`, `import: 37`
* *Defense:* `safety: 280`, `doc: 209`, `test: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` struct_span_code_err, kw, rustc_middle::ty::self, crate::expectation::Expectation, rustc_span::BytePos, rustc_data_structures::fx::FxHashMap, rustc_hir::def_id::DefId, rustc_errors::codes::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_typeck/src/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.617 IQR)
- **Top Global Matches:** file_cluster_16: 13.617, file_cluster_13: 13.623, file_cluster_11: 13.742
- **Magnitude:** 3008.48 | **LOC:** 3919 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (10.6539%), Tech Debt (17.6849%)
**Top Internal Functions/Classes:**
  * `check_expr_break` (Impact: 519.6)
    * *Intent:* // We want to remove some Sized bounds from std functions,
  * `check_expr_unop` (Impact: 513.9)
  * `check_expr_with_expectation_and_args` (Impact: 450.6)
  * `check_expr_continue` (Impact: 412.5)
  * `check_expr_if` (Impact: 363.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 373`, `args: 82`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 113`, `dead_code: 13`, `fragile_debt: 10`
* *Architecture:* `api: 15`, `import: 40`
* *Defense:* `safety: 192`, `doc: 96`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` struct_span_code_err, CoroutineTypes, rustc_infer::traits::query::NoSolution, ObligationCtxt, Symbol, Adjustment, rustc_infer::infer::self, HirId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_trait_selection/src/traits/select/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.526 IQR)
- **Top Global Matches:** file_cluster_16: 14.526, file_cluster_13: 14.54, file_cluster_11: 14.574
- **Magnitude:** 2973.02 | **LOC:** 3204 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (13.4863%), Tech Debt (26.859%)
**Top Internal Functions/Classes:**
  * `evaluate_predicates_recursively` (Impact: 529.5)
    * *Intent:* // If there is more than one candidate, first winnow them down // by considering extra conditions (n...
  * `insert_candidate_cache` (Impact: 462.5)
  * `candidate_from_obligation` (Impact: 450.2)
  * `winnow_candidates` (Impact: 408.5)
  * `can_use_global_caches` (Impact: 402.9)
    * *Intent:* // that we want to avoid cycles. Imagine an impl like: // // impl<T:Eq> Eq for Vec<T> // // and a tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 451`, `args: 151`, `func_start: 61`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 162`, `dead_code: 22`, `planned_debt: 4`, `fragile_debt: 21`
* *Architecture:* `api: 36`, `concurrency: 23`, `import: 42`
* *Defense:* `safety: 359`, `doc: 411`, `test: 18`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` PolyTraitObligation, RefCell, super::
    ImplDerivedCause, may_use_unstable_feature, rustc_middle::dep_graph::DepKind, util, wf, rustc_span::Symbol...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/diagnostics.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.308 IQR)
- **Top Global Matches:** file_cluster_13: 14.308, file_cluster_17: 14.365, file_cluster_11: 14.445
- **Magnitude:** 2732.42 | **LOC:** 3685 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (12.9641%), Tech Debt (9.9421%)
**Top Internal Functions/Classes:**
  * `lookup_import_candidates_from_module` (Impact: 799.3)
  * `add_typo_suggestion` (Impact: 503.3)
  * `make_path_suggestion` (Impact: 214.1)
  * `report_path_resolution_error` (Impact: 184.7)
  * `report_conflict` (Impact: 177.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 562`, `args: 128`, `func_start: 39`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 218`, `dead_code: 23`, `fragile_debt: 5`
* *Architecture:* `api: 50`, `concurrency: 2`, `import: 58`
* *Defense:* `safety: 372`, `doc: 180`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` struct_span_code_err, BindingError, DefId, rustc_session::Session, issue_59764::makro, Symbol, rustc_hir::def::self, NodeId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_parse/src/parser/diagnostics.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.721 IQR)
- **Top Global Matches:** file_cluster_13: 14.721, file_cluster_0: 14.769, file_cluster_11: 14.769
- **Magnitude:** 2725.92 | **LOC:** 3162 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.4742%), Tech Debt (53.6312%)
**Top Internal Functions/Classes:**
  * `check_no_chained_comparison` (Impact: 485.7)
    * *Intent:* // We have encountered the following: // fn foo() -> Foo { // field: value, // } // Suggest: // fn f...
  * `recover_from_inc_dec` (Impact: 430.8)
  * `check_mistyped_turbofish_with_multiple_t` (Impact: 421.2)
  * `expected_ident_found` (Impact: 179.7)
  * `parameter_without_type` (Impact: 156.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 332`, `structural_boundaries: 397`, `args: 117`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 227`, `dead_code: 19`, `fragile_debt: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 73`, `concurrency: 32`, `import: 24`
* *Defense:* `safety: 286`, `doc: 148`, `test: 1`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ComparisonOperatorsCannotBeChainedSugg, QSelf, AmbiguousPlus, rustc_span::BytePos, ast::token::IdentIsRaw, MisspelledKw, Symbol, QuestionMarkInTypeSugg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_middle/src/ty/print/pretty.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.049 IQR)
- **Top Global Matches:** file_cluster_16: 14.049, file_cluster_13: 14.083, file_cluster_11: 14.127
- **Magnitude:** 2652.22 | **LOC:** 3559 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (29.8022%), Tech Debt (97.1774%)
**Top Internal Functions/Classes:**
  * `pretty_print_opaque_impl_type` (Impact: 781.0)
  * `pretty_print_const_valtree` (Impact: 364.7)
  * `pretty_print_type` (Impact: 137.3)
    * *Intent:* // // This is correct, as the visible parent of `std::sys::unix::ext` is in fact // `std::os`. // //...
  * `fold_region` (Impact: 101.2)
  * `pretty_print_const_scalar_int` (Impact: 79.7)
    * *Intent:* // Do not call `pretty_print_value_path` as if a parent of this anon // const is an impl it will att...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 670`, `structural_boundaries: 475`, `args: 163`, `func_start: 96`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 258`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 21`, `duplicate_logic: 22`
* *Architecture:* `api: 60`, `concurrency: 2`, `import: 33`
* *Defense:* `safety: 344`, `doc: 120`, `test: 1`, `immutability_locks: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` IndexEntry, rustc_hir::definitions::DefKey, kw, Pointer, ty::abstract_const::CastKind, TypeFoldable, Half, Size...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/ident.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.064 IQR)
- **Top Global Matches:** file_cluster_17: 14.064, file_cluster_13: 14.076, file_cluster_0: 14.1
- **Magnitude:** 2574.84 | **LOC:** 2086 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (13.4841%), Tech Debt (24.9627%)
**Top Internal Functions/Classes:**
  * `resolve_ident_in_scope_set_inner` (Impact: 607.9)
  * `visit_scopes` (Impact: 598.6)
    * *Intent:* /// A generic scope visitor. /// Visits scopes in order to resolve some identifier in them or perfor...
  * `resolve_ident_in_module` (Impact: 458.4)
  * `validate_res_from_ribs` (Impact: 299.9)
  * `resolve_path_with_ribs` (Impact: 206.0)
    * *Intent:* // So we have a resolution that's from a glob import. This resolution is determined // if it cannot ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 245`, `args: 49`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 76`, `dead_code: 12`, `planned_debt: 1`, `fragile_debt: 12`
* *Architecture:* `api: 10`, `import: 24`
* *Defense:* `safety: 339`, `doc: 24`, `test: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PartialRes, Namespace::*, ExpnKind, kw, ImportKind, Decl, MacroKinds, MacroKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_parse/src/parser/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.672 IQR)
- **Top Global Matches:** file_cluster_11: 14.672, file_cluster_13: 14.69, file_cluster_8: 14.694
- **Magnitude:** 2477.44 | **LOC:** 4451 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (16.209%), Tech Debt (12.9065%)
**Top Internal Functions/Classes:**
  * `is_mistaken_not_ident_negation` (Impact: 183.6)
  * `parse_struct_fields` (Impact: 111.9)
  * `parse_arm` (Impact: 105.8)
  * `parse_if_after_cond` (Impact: 69.2)
  * `parse_expr_else` (Impact: 63.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 764`, `structural_boundaries: 749`, `args: 231`, `func_start: 107`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 366`, `dead_code: 17`, `fragile_debt: 12`
* *Architecture:* `api: 65`, `concurrency: 25`, `import: 31`
* *Defense:* `safety: 608`, `doc: 130`, `test: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` super::ty::AllowPlus, StmtKind, rustc_span::BytePos, rustc_errors::Applicability, ast::token::IdentIsRaw, Fixity, core::ops::Bound, Trailing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/arm_shared/neon/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.932 IQR)
- **Top Global Matches:** file_cluster_8: 9.932, file_cluster_0: 10.234, file_cluster_7: 10.49
- **Magnitude:** 2343.82 | **LOC:** 5830 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.99%), Tech Debt (9.0608%)
**Top Internal Functions/Classes:**
  * `as_signed` (Impact: 6.4)
  * `test_vbslq_s8` (Impact: 5.6)
  * `test_vbslq_u8` (Impact: 5.6)
  * `test_vbslq_p8` (Impact: 5.6)
  * `test_vceq_s8` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 1257`, `args: 959`, `func_start: 519`, `class_start: 106`
* *Risk/State:* `state_mutation: 11`, `duplicate_logic: 4`
* *Architecture:* `api: 886`, `import: 10`
* *Defense:* `doc: 105`, `test: 332`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::core_arch::aarch64::*, crate::core_arch::simd::*, stdarch_test::assert_instr, stdarch_test::simd_test, intrinsics::simd::*, super::*, crate::core_arch::arm_shared::test_support::*, self::generated::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/late.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.908 IQR)
- **Top Global Matches:** file_cluster_8: 13.908, file_cluster_16: 13.915, file_cluster_0: 13.94
- **Magnitude:** 2294.72 | **LOC:** 5611 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (10.7589%), Tech Debt (58.8405%)
**Top Internal Functions/Classes:**
  * `resolve_elided_lifetimes_in_path` (Impact: 339.7)
  * `visit_pat` (Impact: 313.9)
    * *Intent:* /// Used for recording UnnecessaryQualification. #[derive(Debug)]
  * `find_lifetime_for_self` (Impact: 242.5)
  * `resolve_impl_item` (Impact: 170.4)
  * `resolve_anonymous_lifetime` (Impact: 101.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 636`, `args: 265`, `func_start: 85`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 266`, `dead_code: 16`, `fragile_debt: 19`, `duplicate_logic: 12`
* *Architecture:* `api: 53`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 366`, `doc: 274`, `test: 3`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` DefId, rustc_span::BytePos, Symbol, DelegationFnSig, rustc_hir::def::self, walk_list, std::collections::hash_map::Entry, Finalize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_codegen_ssa/src/back/link.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.35 IQR)
- **Top Global Matches:** file_cluster_13: 13.35, file_cluster_8: 13.415, file_cluster_11: 13.616
- **Magnitude:** 2237.16 | **LOC:** 3623 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (15.7202%), Tech Debt (96.0963%)
**Top Internal Functions/Classes:**
  * `link_natively` (Impact: 919.3)
  * `linker_with_args` (Impact: 144.3)
    * *Intent:* // When attempting to spawn the linker we run a risk of blowing out the // size limits for spawning ...
  * `are_upstream_rust_objects_already_includ` (Impact: 134.8)
  * `add_order_independent_options` (Impact: 106.0)
  * `link_binary` (Impact: 104.4)
    * *Intent:* /// Performs the linkage portion of the compilation phase. This will generate all /// of the request...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 343`, `args: 117`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 122`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 30`, `duplicate_logic: 5`
* *Architecture:* `io: 9`, `api: 20`, `concurrency: 1`, `import: 51`
* *Defense:* `safety: 188`, `doc: 123`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` rustc_session::Session, rustc_session::lint::builtin::LINKER_MESSAGES, std::process::Output, object::read::elf::FileHeader, create_wrapper_file, LinkOutputKind, crate::base::needs_allocator_shim_for_linking, CompiledModule...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_trait_selection/src/error_reporting/infer/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.117 IQR)
- **Top Global Matches:** file_cluster_16: 13.117, file_cluster_13: 13.227, file_cluster_8: 13.25
- **Magnitude:** 2174.28 | **LOC:** 2429 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (13.4864%), Tech Debt (11.8283%)
**Top Internal Functions/Classes:**
  * `maybe_highlight` (Impact: 459.9)
  * `check_and_note_conflicting_crates` (Impact: 420.5)
  * `cmp` (Impact: 368.7)
    * *Intent:* /// If `other_ty` is the same as a type argument present in `sub`, highlight `path` in `t1_out`, ///...
  * `note_type_err` (Impact: 211.3)
  * `cmp_fn_sig` (Impact: 73.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 495`, `args: 65`, `func_start: 44`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 144`, `dead_code: 9`, `planned_debt: 1`, `fragile_debt: 6`
* *Architecture:* `api: 35`, `concurrency: 7`, `import: 35`
* *Defense:* `safety: 234`, `doc: 110`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ValuePairs, Obligation, crate::infer::InferCtxt, iter, rustc_macros::extension, rustc_middle::ty::error::ExpectedFound, crate::errors::ObligationCauseFailureCode, rustc_span::BytePos...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_hir_analysis/src/check/check.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.753 IQR)
- **Top Global Matches:** file_cluster_8: 12.753, file_cluster_13: 12.803, file_cluster_16: 12.903
- **Magnitude:** 2160.82 | **LOC:** 2305 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (20.5968%), Tech Debt (64.4004%)
**Top Internal Functions/Classes:**
  * `check_impl_items_against_trait` (Impact: 372.6)
  * `check_opaque_for_cycles` (Impact: 355.2)
  * `best_definition_site_of_opaque` (Impact: 353.1)
  * `check_opaque_precise_captures` (Impact: 351.6)
  * `check_item_type` (Impact: 82.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 460`, `args: 84`, `func_start: 37`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 149`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 20`, `duplicate_logic: 2`
* *Architecture:* `api: 20`, `import: 36`
* *Defense:* `safety: 194`, `doc: 38`, `test: 3`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` UNSUPPORTED_CALLING_CONVENTIONS, rustc_errors::codes::*, find_attr, TypeFoldable, Diagnostic, rustc_target::spec::AbiMap, rustc_hir::LangItem, rustc_middle::ty::error::TypeErrorToStringExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_llvm/llvm-wrapper/PassWrapper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.961 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.199 IQR)
- **Top Global Matches:** file_cluster_13: 13.961, file_cluster_8: 14.012, file_cluster_11: 14.288
- **Magnitude:** 2113.12 | **LOC:** 1477 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (89.9297%), Tech Debt (85.9404%)
**Top Internal Functions/Classes:**
  * `LLVMRustOptimize` (Impact: 660.6)
    * *Intent:* // Apparently `addPassesToEmitFile` adds a pointer to our on-the-stack output // stream (OS), so the...
  * `LLVMRustCreateTargetMachine` (Impact: 611.4)
  * `LLVMRustCreateThinLTOData` (Impact: 51.5)
  * `fromRust` (Impact: 16.5)
  * `fromRust` (Impact: 16.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 204`, `args: 223`, `func_start: 18`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 557`, `duplicate_logic: 6`, `orphaned_logic: 27`
* *Architecture:* `api: 1`, `import: 50`
* *Defense:* `safety: 12`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Host.h, vector, LTO.h, InstrProfiling.h, CanonicalizeAliases.h, LegacyPassManager.h, LLVMWrapper.h, SmallVector.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `compiler/rustc_middle/src/mir/interpret/value.rs` (RUST) | Magnitude: 278.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 341, api: 86, args: 74, generics: 72
- `library/alloc/src/collections/btree/borrow/tests.rs` (RUST) | Magnitude: 18.36 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, state_mutation: 12, structural_boundaries: 11, test: 3
- `library/alloc/src/raw_vec/tests.rs` (RUST) | Magnitude: 43.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 28, test: 28, generics: 16
- `library/core/src/ffi/va_list.rs` (RUST) | Magnitude: 2.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 123, indent_spaces: 45, decorators: 10, immutability_locks: 9
- `library/portable-simd/crates/core_simd/src/fmt.rs` (RUST) | Magnitude: 3.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 5, indent_spaces: 5, generics: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/tools/miri/tests/pass/issues/issue-139553.rs` (RUST) | Magnitude: 0.01 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, concurrency: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/tools/clippy/clippy_lints/src/format_push_string.rs` (RUST) | Magnitude: 0.03 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, doc: 41, structural_boundaries: 33, generics: 15
- `src/tools/clippy/clippy_lints/src/mut_mut.rs` (RUST) | Magnitude: 0.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 43, state_mutation: 30, doc: 24
- `src/tools/clippy/clippy_lints/src/manual_let_else.rs` (RUST) | Magnitude: 0.29 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 250, structural_boundaries: 114, branch: 76, doc: 70
- `src/tools/rust-analyzer/crates/parser/src/grammar/items.rs` (RUST) | Magnitude: 0.29 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 302, structural_boundaries: 76, branch: 73, state_mutation: 47
- `tests/ui/higher-ranked/trait-bounds/normalize-under-binder/issue-62529-6.rs` (RUST) | Magnitude: 35.12 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 27, generics: 25, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/tools/clippy/util/etc/pre-commit.sh` (SHELL) | Magnitude: 0.01 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 5, io: 5, state_mutation: 3, reflection_metaprogramming: 3
- `tests/ui/consts/issue-17718-const-borrow.rs` (RUST) | Magnitude: 3.98 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: immutability_locks: 8, reflection_metaprogramming: 7, generics: 3, structural_boundaries: 2
- `src/ci/docker/host-x86_64/x86_64-gnu-miri/check-miri.sh` (SHELL) | Magnitude: 3.07 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 12, reflection_metaprogramming: 12, branch: 11
- `tests/ui/consts/unsafe_cell_in_const.rs` (RUST) | Magnitude: 26.94 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 25, structural_boundaries: 9, reflection_metaprogramming: 7, immutability_locks: 3
- `src/ci/scripts/verify-stable-version-number.sh` (SHELL) | Magnitude: 2.06 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 9, branch: 7, reflection_metaprogramming: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/tools/rust-analyzer/crates/proc-macro-srv/src/dylib.rs` (RUST) | Magnitude: 0.09 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 40, doc: 30, generics: 27
- `tests/ui/unboxed-closures/unboxed-closures-infer-fnonce.rs` (RUST) | Magnitude: 16.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, state_mutation: 10, indent_spaces: 10, generics: 4
- `src/tools/clippy/clippy_lints/src/else_if_without_else.rs` (RUST) | Magnitude: 0.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 33, indent_spaces: 21, branch: 13, structural_boundaries: 9
- `compiler/rustc_hir_analysis/src/hir_ty_lowering/cmse.rs` (RUST) | Magnitude: 91.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 44, generics: 27, branch: 20
- `compiler/rustc_query_impl/src/execution.rs` (RUST) | Magnitude: 286.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 293, generics: 91, structural_boundaries: 90, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/ui/closures/moved-upvar-mut-rebind-11958.rs` (RUST) | Magnitude: 7.88 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 3, args: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `compiler/rustc_type_ir/src/walk.rs` (RUST) | Magnitude: 54.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, doc: 28, structural_boundaries: 19, args: 19
- `src/tools/clippy/clippy_lints/src/methods/chars_next_cmp.rs` (RUST) | Magnitude: 0.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, import: 3, generics: 2, args: 1
- `tests/ui/binop/binop-move-semantics.rs` (RUST) | Magnitude: 40.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, state_mutation: 16, generics: 12
- `tests/ui/lifetimes/lifetime-doesnt-live-long-enough.rs` (RUST) | Magnitude: 9.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, generics: 18, bitwise_ops: 12, structural_boundaries: 9
- `tests/ui/nll/issue-52534-1.rs` (RUST) | Magnitude: 18.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 16, indent_spaces: 16, structural_boundaries: 11, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/tools/rust-analyzer/crates/ide-db/src/imports/merge_imports.rs` (RUST) | Magnitude: 0.43 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 335, structural_boundaries: 116, branch: 91, state_mutation: 91
- `src/tools/rust-analyzer/crates/project-model/src/toolchain_info/target_tuple.rs` (RUST) | Magnitude: 0.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, safety: 41, structural_boundaries: 33, branch: 15
- `src/tools/miri/src/bin/miri.rs` (RUST) | Magnitude: 0.41 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 498, branch: 186, safety: 113, structural_boundaries: 110
- `src/tools/rust-analyzer/crates/ide/src/hover/render.rs` (RUST) | Magnitude: 0.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1246, structural_boundaries: 318, safety: 312, branch: 250
- `src/tools/tidy/src/ui_tests.rs` (RUST) | Magnitude: 0.13 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 41, state_mutation: 28, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/librustdoc/html/static/js/rustdoc.d.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 27, doc: 24, generics: 17
- `src/tools/clippy/util/gh-pages/theme.js` (JAVASCRIPT) | Magnitude: 0.05 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, branch: 18, globals: 10, state_mutation: 9
- `tests/rustdoc-html/mixing-doc-comments-and-attrs.S3_top-doc.html` (HTML) | Magnitude: 11.56 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, ui_framework: 1, decorators: 1
- `tests/rustdoc-html/enum/strip-enum-variant.no-not-shown.html` (HTML) | Magnitude: 10.52 | Delta: **0.286 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, io: 2, ui_framework: 1, decorators: 1
- `tests/rustdoc-html/strip-block-doc-comments-stars.docblock.html` (HTML) | Magnitude: 11.04 | Delta: **0.37 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, ui_framework: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/ui/cast/ptr-to-trait-obj-add-auto.rs` (RUST) | Magnitude: 12.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: concurrency: 6, generics: 4, structural_boundaries: 3, pointers: 3
- `library/test/src/types.rs` (RUST) | Magnitude: 170.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 50, api: 45, safety: 42
- `library/std/src/sys/pal/unix/linux/pidfd/tests.rs` (RUST) | Magnitude: 21.16 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, safety: 7, import: 7
- `library/std/src/sys/sync/condvar/windows7.rs` (RUST) | Magnitude: 34.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, concurrency: 12, structural_boundaries: 10, sync_locks: 10
- `tests/ui/moves/arc-consumed-in-looped-closure.rs` (RUST) | Magnitude: 14.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, safety: 7, generics: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/tools/clippy/tests/ui/needless_doc_main.rs` (RUST) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 126, dead_code: 18, args: 4, func_start: 4
- `src/tools/rustfmt/tests/source/itemized-blocks/no_wrap.rs` (RUST) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 72, args: 3, func_start: 3, orphaned_logic: 3
- `src/tools/rustfmt/tests/source/issue-3055/original.rs` (RUST) | Magnitude: 0.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 39, dead_code: 2, args: 1, func_start: 1
- `src/tools/clippy/clippy_lints/src/iter_not_returning_iterator.rs` (RUST) | Magnitude: 0.03 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 43, doc: 26, structural_boundaries: 17, generics: 10
- `compiler/rustc_thread_pool/src/scope/mod.rs` (RUST) | Magnitude: 13.68 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 458, structural_boundaries: 19, indent_spaces: 18, dead_code: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/rustdoc-ui/lints/redundant_explicit_links-utf8.rs` (RUST) | Magnitude: 19.12 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 11, structural_boundaries: 6, class_start: 6, api: 6
- `library/core/src/arch.rs` (RUST) | Magnitude: 7.48 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 41, decorators: 11, api: 5, encapsulation: 5
- `compiler/rustc_ast_pretty/src/pp.rs` (RUST) | Magnitude: 130.18 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 162, indent_spaces: 153, state_mutation: 40, branch: 30
- `tests/ui/svh/auxiliary/svh-utb.rs` (RUST) | Magnitude: 2.86 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, args: 1, func_start: 1, api: 1
- `src/tools/clippy/tests/ui/doc/unbalanced_ticks.rs` (RUST) | Magnitude: 0.01 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 41, args: 3, func_start: 3, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `compiler/rustc_hir_analysis/src/outlives/explicit.rs` (RUST) | Magnitude: 24.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 12, generics: 7, args: 6
- `tests/ui/const-generics/issues/issue-70167.rs` (RUST) | Magnitude: 2.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 2, bitwise_ops: 2, args: 1, func_start: 1
- `tests/ui/impl-trait/closure-in-impl-trait-arg.rs` (RUST) | Magnitude: 4.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 2, func_start: 2, generics: 2, fragile_debt: 2
- `tests/ui/self/elision/lt-assoc.rs` (RUST) | Magnitude: 12.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, generics: 11, structural_boundaries: 7, args: 7
- `tests/ui/trait-bounds/for-binder-placement-error-39089.rs` (RUST) | Magnitude: 6.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: args: 2, func_start: 2, branch: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `library/stdarch/crates/intrinsic-test/src/x86/constraint.rs` (RUST) | Magnitude: 8.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, safety: 17, structural_boundaries: 3, branch: 2
- `tests/ui/static/extern-static-normalization-failure-issue-148161.rs` (RUST) | Magnitude: 2.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, class_start: 2, generics: 2
- `src/tools/rustfmt/tests/source/issue_4057.rs` (RUST) | Magnitude: 0.01 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 12, dead_code: 2, structural_boundaries: 1, class_start: 1
- `library/std/src/hash/random.rs` (RUST) | Magnitude: 11.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 49, dead_code: 6, indent_spaces: 2
- `src/tools/rustfmt/tests/source/doc-comment-with-example.rs` (RUST) | Magnitude: 0.0 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 9, args: 1, func_start: 1, dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/rustc_middle/src/query/plumbing.rs` -> Churn: **100.0%** | Cog Load: 4.0314% | Debt: 99.5554%
- `compiler/rustc_query_impl/src/plumbing.rs` -> Churn: **99.05%** | Cog Load: 9.9405% | Debt: 99.9078%
- `src/tools/rust-analyzer/crates/syntax/src/ast/syntax_factory/constructors.rs` -> Churn: **85.83%** | Cog Load: 65.6065% | Debt: 11.386%
- `compiler/rustc_lint/src/lints.rs` -> Churn: **80.69%** | Cog Load: 7.503% | Debt: 67.8357%
- `src/librustdoc/clean/mod.rs` -> Churn: **76.32%** | Cog Load: 14.8395% | Debt: 56.5575%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `library/stdarch/crates/core_arch/src/mips/msa.rs` -> **cyrgani** (100.0% isolated ownership) | Magnitude: 3377.76
- `src/librustdoc/clean/mod.rs` -> **Guillaume Gomez** (90.0% isolated ownership) | Magnitude: 1710.66
- `compiler/rustc_hir_typeck/src/upvar.rs` -> **Guillaume Gomez** (100.0% isolated ownership) | Magnitude: 1606.5
- `compiler/rustc_parse/src/parser/stmt.rs` -> **Esteban Küber** (100.0% isolated ownership) | Magnitude: 1595.46
- `src/librustdoc/html/static/js/stringdex.js` -> **Michael Howell** (100.0% isolated ownership) | Magnitude: 1577.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/tools/clippy/clippy_utils/src/higher.rs` -> **Severity: 46.837** (Blast Radius: 0.611 * Doc Risk: 76.6564%)
- `src/tools/rust-analyzer/crates/syntax/src/ted.rs` -> **Severity: 31.183** (Blast Radius: 0.334 * Doc Risk: 93.3625%)
- `src/tools/rust-analyzer/crates/syntax/src/algo.rs` -> **Severity: 30.2** (Blast Radius: 0.302 * Doc Risk: 100.0%)
- `src/tools/rust-analyzer/editors/code/src/lsp_ext.ts` -> **Severity: 24.594** (Blast Radius: 0.246 * Doc Risk: 99.974%)
- `compiler/rustc_borrowck/src/type_check/liveness/trace.rs` -> **Severity: 24.317** (Blast Radius: 2.04 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
