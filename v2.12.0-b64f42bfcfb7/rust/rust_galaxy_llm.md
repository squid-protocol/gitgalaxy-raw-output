# ARCHITECTURAL_BRIEF: rust
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/rust-lang/rust.git` |
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
- **Scope:** 37244 analyzed artifact(s), 2498054 LOC.
- **Load-bearing artifact:** `library/std/src/lib.rs` -- 2223 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/tools/clippy/clippy_lints/src/lib.rs` -- pulls in 381 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/ui/expr/if/expr-stack-overflow.rs` at magnitude 15452.42 (structural weight, not risk).
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
| Total Artifacts | 58763 |
| Analyzed Artifacts (Scanned) | 37244 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21519 |
| Total LOC | 2498054 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6691 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1567 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 560 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 34805 | 2424824 | 93.5% |
| MARKDOWN | 1378 | 0 | 3.7% |
| PLAINTEXT | 220 | 0 | 0.6% |
| SHELL | 140 | 14859 | 0.4% |
| JAVASCRIPT | 130 | 14218 | 0.3% |
| C | 110 | 8845 | 0.3% |
| HTML | 106 | 1591 | 0.3% |
| DOCKERFILE | 91 | 2817 | 0.2% |
| YAML | 68 | 5001 | 0.2% |
| JSON | 38 | 1385 | 0.1% |
| PYTHON | 33 | 6512 | 0.1% |
| TYPESCRIPT | 29 | 6437 | 0.1% |
| XML | 28 | 0 | 0.1% |
| CPP | 19 | 3856 | 0.1% |
| CSS | 11 | 4316 | 0.0% |
| MAKEFILE | 10 | 266 | 0.0% |
| BATCH | 9 | 39 | 0.0% |
| ASSEMBLY | 6 | 283 | 0.0% |
| POWERSHELL | 4 | 2080 | 0.0% |
| M4 | 3 | 30 | 0.0% |
| NIX | 3 | 118 | 0.0% |
| YACC | 1 | 5 | 0.0% |
| PERL | 1 | 1 | 0.0% |
| LIVECODE | 1 | 571 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 37240 |
| utf-8 | bom | 4 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 33%, State Mutators Files 26%, Generic / Templated Code Files 12%, Declarative / Non-Code 7%, Large Core Modules 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 35640 | 95.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1600 | 4.3% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21519*

**Composition by Extension & Reason:**
- `.stderr`: 12852x Excluded (Unsupported Extension: '.stderr'), 2004x Unsupported Format (.stderr), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 1412x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 202x Excluded: Neighborhood Micro-Mass Limit Exceeded, 26x Excluded (Machine-Generated Source Code Signature: 6 LOC)
- `.fixed`: 1313x Unsupported Format (.fixed)
- `.diff`: 847x Excluded (Unsupported Extension: '.diff'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.diff)
- `.toml`: 543x Unsupported Format (.toml), 21x Excluded (Unsupported Extension: '.toml'), 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rast`: 505x Unsupported Format (.rast), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.stdout`: 298x Excluded (Unsupported Extension: '.stdout'), 46x Unsupported Format (.stdout), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mir`: 357x Unsupported Format (.mir)
- `.goml`: 142x Excluded (Unsupported Extension: '.goml')
- `no_extension`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 54x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 3180 LOC)
- `.coverage`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.coverage')
- `.cov-map`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 31x Unsupported Format (.lock), 14x Excluded (Unsupported Extension: '.lock'), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 49x Unsupported Format (.snap)
- `.md`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1226 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 14.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 74.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 84.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17687 | 3666 | 0 | `src/tools/clippy/clippy_lints/src/lib.rs` |
| cleanup | 1994 | 830 | 0 | `tests/ui/borrowck/borrowck-field-sensitivity-rpass.rs` |
| guards | 77806 | 10424 | 4 | `library/std/src/sys/pal/windows/c/windows_sys.rs` |
| danger | 36880 | 6290 | 2 | `src/tools/rust-analyzer/crates/ide/src/hover/tests.rs` |
| concurrency | 18357 | 3108 | 0 | `src/librustdoc/html/static/js/search.js` |
| connectivity | 146653 | 16827 | 6 | `library/stdarch/crates/core_arch/src/x86/avx512f.rs` |
| io | 4528 | 1100 | 0 | `src/bootstrap/bootstrap.py` |
| crypto | 3 | 3 | 0 | `src/bootstrap/bootstrap.py` |
| ipc | 330 | 248 | 0 | `src/bootstrap/bootstrap.py` |
| time | 351 | 142 | 0 | `src/etc/completions/x.fish` |
| serialization | 189 | 94 | 0 | `src/tools/rustdoc-js/tester.js` |
| regex | 365 | 146 | 0 | `src/librustdoc/html/static/js/search.js` |
| events | 5431 | 909 | 0 | `compiler/rustc_trait_selection/src/traits/select/mod.rs` |
| tests | 58008 | 6246 | 2 | `library/alloc/src/collections/btree/map/tests.rs` |
| docs | 331248 | 7016 | 4 | `library/stdarch/crates/core_arch/src/x86/avx512f.rs` |
| debt | 28207 | 7062 | 2 | `library/std_detect/tests/cpu-detection.rs` |
| mutation | 325604 | 19973 | 14 | `library/stdarch/crates/core_arch/src/x86/avx512f.rs` |
| dead_code | 45990 | 24725 | 2 | `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` |
| credential | 82 | 40 | 0 | `tests/codegen-llvm/sanitizer/cfi/emit-type-metadata-id-itanium-cxx-abi-trait-types.rs` |
| threat | 157 | 48 | 0 | `library/alloc/src/wtf8/tests.rs` |
| ml_ai | 10426 | 1420 | 0 | `library/stdarch/crates/core_arch/src/x86/avx512f.rs` |
| ui | 343 | 45 | 0 | `src/librustdoc/html/static/css/rustdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/bootstrap/bootstrap.py` (Hits: 122)
- `src/etc/completions/x.py.zsh` (Hits: 74)
- `src/etc/completions/x.zsh` (Hits: 74)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`library/std/src/lib.rs`) — 2223 inbound connections
2. **doc-notable_trait_box_is_not_an_iterator.rs** (`tests/rustdoc-html/notable-trait/doc-notable_trait_box_is_not_an_iterator.rs`) — 1383 inbound connections
3. **mod.rs** (`library/core/src/ops/mod.rs`) — 1122 inbound connections
4. **mod.rs** (`library/core/src/mem/mod.rs`) — 1029 inbound connections
5. **mod.rs** (`compiler/rustc_middle/src/ty/mod.rs`) — 946 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`src/tools/clippy/clippy_lints/src/lib.rs`) — 381 outbound dependencies
2. **lib.rs** (`src/tools/rust-analyzer/crates/hir/src/lib.rs`) — 285 outbound dependencies
3. **mod.rs** (`compiler/rustc_middle/src/ty/mod.rs`) — 278 outbound dependencies
4. **SUMMARY.md** (`src/doc/rustc-dev-guide/src/SUMMARY.md`) — 229 outbound dependencies
5. **lib.rs** (`src/tools/clippy/clippy_utils/src/lib.rs`) — 212 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `banana` **(Many-Argument Workhorses)** (@ `tests/ui/expr/if/expr-stack-overflow.rs`) -> Impact: **15244.1** | LOC: 10415
  * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-tidy-filelength
- `initSearch` **(Many-Argument Workhorses)** (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **1993.3** | LOC: 4747
  * *Intent:* /** */
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/unix/foreign_items.rs`) -> Impact: **1227.9** | LOC: 1190
- `_x` **(Many-Argument Workhorses)** (@ `src/etc/completions/x.sh`) -> Impact: **1089.5** | LOC: 4282
- `eval_simd_intrinsic` **(Many-Argument Workhorses)** (@ `compiler/rustc_const_eval/src/interpret/intrinsics/simd.rs`) -> Impact: **838.6** | LOC: 792
  * *Intent:* /// Returns `true` if emulation happened. /// Here we implement the intrinsics that are common to all CTFE instances; individual machines can add thei...
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/windows/foreign_items.rs`) -> Impact: **804.0** | LOC: 1187
- `execQuery` **(Many-Argument Workhorses)** (@ `src/librustdoc/html/static/js/search.js`) -> Impact: **774.4** | LOC: 1847
  * *Intent:* /** * Executes the parsed query and builds a {ResultsTable}. * * - The parsed user query * */
- `loadDatabase` **(Many-Argument Workhorses)** (@ `src/librustdoc/html/static/js/stringdex.js`) -> Impact: **678.5** | LOC: 2595
  * *Intent:* /** */
- `exec_intrinsic` **(Many-Argument Workhorses)** (@ `src/tools/rust-analyzer/crates/hir-ty/src/mir/eval/shim.rs`) -> Impact: **624.1** | LOC: 783
- `emulate_foreign_item_inner` **(Many-Argument Workhorses)** (@ `src/tools/miri/src/shims/foreign_items.rs`) -> Impact: **577.8** | LOC: 631

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `library/stdarch/crates/core_arch/src/x86` | 49 | 39912.22 | 2.42% | 2.27% |
| `tests/ui/expr/if` | 24 | 15694.08 | 4.47% | 0.0% |
| `src/librustdoc/html/static/js` | 11 | 12657.4 | 27.29% | 32.57% |
| `compiler/rustc_mir_transform/src` | 78 | 12551.44 | 11.18% | 64.08% |
| `compiler/rustc_parse/src/parser` | 16 | 11053.14 | 10.28% | 8.94% |
| `compiler/rustc_hir_typeck/src` | 27 | 10717.34 | 7.72% | 20.98% |
| `compiler/rustc_resolve/src` | 12 | 10412.12 | 10.86% | 18.51% |
| `compiler/rustc_middle/src/ty` | 38 | 8534.78 | 6.37% | 38.64% |
| `compiler/rustc_lint/src` | 53 | 8362.74 | 7.23% | 14.96% |
| `compiler/rustc_borrowck/src/diagnostics` | 13 | 6757.48 | 10.17% | 23.53% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/tools/clippy/.github/ISSUE_TEMPLATE/false_negative.yml` -> **100.0%** Exposure
- `compiler/rustc_codegen_ssa/src/back/linker.rs` -> **100.0%** Exposure
- `compiler/rustc_middle/src/query/into_query_key.rs` -> **100.0%** Exposure
- `compiler/rustc_middle/src/query/keys.rs` -> **100.0%** Exposure
- `compiler/rustc_mir_transform/src/post_analysis_normalize.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compiler/rustc_ast/src/util/comments.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_cranelift/scripts/rustc-clif.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_cranelift/scripts/rustdoc-clif.rs` -> **100.0%** Exposure
- `compiler/rustc_codegen_gcc/build_system/src/fuzz/reduce.rs` -> **100.0%** Exposure
- `compiler/rustc_session/src/config/cfg.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` -> **555** Orphaned Functions | **0** Duplicates
- `compiler/rustc_codegen_ssa/src/back/linker.rs` -> **0** Orphaned Functions | **114** Duplicates
- `compiler/rustc_llvm/llvm-wrapper/RustWrapper.cpp` -> **105** Orphaned Functions | **0** Duplicates
- `tests/ui/delegation/generics/mapping/trait-to-trait-pass.rs` -> **1** Orphaned Functions | **98** Duplicates
- `tests/ui/lint/improper-ctypes/lint-enum.rs` -> **88** Orphaned Functions | **0** Duplicates

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
- **Binary Anomalies (X-Ray):** `45` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `111773` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/ui/expr/if/expr-stack-overflow.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 9.92)
- **Top Global Matches:** file_cluster_1: 9.92, file_cluster_3: 48.987, file_cluster_8: 70.632
- **Magnitude:** 15452.42 | **LOC:** 10421 | **CtrlFlow:** 99.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (13.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `banana` **(Many-Argument Workhorses)** (Impact: 15244.1)
    * *Intent:* //! regression test for <https://github.com/rust-lang/rust/issues/74564> //@ build-pass // ignore-ti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10410`, `args: 1`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `library/stdarch/crates/core_arch/src/x86/avx512f.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.863)
- **Top Global Matches:** file_cluster_13: 7.863, file_cluster_15: 9.44, file_cluster_16: 10.128
- **Magnitude:** 15312.44 | **LOC:** 62633 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.8%), Debt Markers (formerly Tech Debt) (7.7%)
- **Documentation Coverage:** 47.672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm512_set_epi8` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* /// Set packed 8-bit integers in dst with the supplied values. /// /// [Intel's documentation](https...
  * `_mm512_set_epi16` **(Many-Argument Workhorses)** (Impact: 8.0)
    * *Intent:* /// Set packed 16-bit integers in dst with the supplied values. /// /// [Intel's documentation](http...
  * `_mm512_alignr_epi32` **(Many-Argument Workhorses)** (Impact: 7.3)
    * *Intent:* /// Concatenate a and b into a 128-byte immediate result, shift the result right by imm8 32-bit elem...
  * `_mm512_mask_slli_epi32` **(Many-Argument Workhorses)** (Impact: 7.0)
    * *Intent:* /// Shift packed 32-bit integers in a left by imm8 while shifting in zeros, and store the results in...
  * `_mm256_mask_slli_epi32` **(Many-Argument Workhorses)** (Impact: 7.0)
    * *Intent:* /// Shift packed 32-bit integers in a left by imm8 while shifting in zeros, and store the results in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 9679`, `args: 4406`, `func_start: 4401`, `class_start: 50`
* *Risk/State:* `state_mutation: 82`, `dead_code: 1`, `planned_debt: 18`
* *Architecture:* `api: 4323`, `import: 8`
* *Defense:* `doc: 10212`, `test: 260`, `immutability_locks: 1206`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` core::hint::unreachable_unchecked, crate::arch::asm, crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::hint::black_box, crate::intrinsics::fmaf32, crate::intrinsics::fmaf64...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/librustdoc/html/static/js/search.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.97)
- **Top Global Matches:** file_cluster_6: 9.97, file_cluster_8: 10.338, file_cluster_4: 17.265
- **Magnitude:** 7114.78 | **LOC:** 5573 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.02; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (65.0%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 13.1483% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initSearch` **(Many-Argument Workhorses)** (Impact: 1993.3)
    * *Intent:* /** */
  * `execQuery` **(Many-Argument Workhorses)** (Impact: 774.4)
    * *Intent:* /** * Executes the parsed query and builds a {ResultsTable}. * * - The parsed user query * */
  * `innerRunTypeQuery` **(Many-Argument Workhorses)** (Impact: 260.4)
  * `unifyFunctionTypes` **(Many-Argument Workhorses)** (Impact: 179.5)
    * *Intent:* * - Map query generics to function generics (never modified). * - Called for each `mgens` solution. ...
  * `getNextElem` **(Many-Argument Workhorses)** (Impact: 136.5)
    * *Intent:* /** * - This is where the new {QueryElement} will be added. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 395 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 458
* *State Mutation (weighted view):* 1269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 653`, `args: 200`, `func_start: 114`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 10`, `state_mutation: 479`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 2`, `concurrency: 208`
* *Defense:* `safety: 481`, `doc: 164`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/x86/avx512fp16.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.026)
- **Top Global Matches:** file_cluster_13: 7.026, file_cluster_15: 9.18, file_cluster_0: 9.49
- **Magnitude:** 6333.2 | **LOC:** 27594 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.011; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.8%), Debt Markers (formerly Tech Debt) (7.7%)
- **Documentation Coverage:** 68.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm512_set_ph` **(Many-Argument Workhorses)** (Impact: 7.9)
    * *Intent:* /// Set packed half-precision (16-bit) floating-point elements in dst with the supplied values. /// ...
  * `_mm512_setr_ph` **(Many-Argument Workhorses)** (Impact: 7.9)
    * *Intent:* /// Set packed half-precision (16-bit) floating-point elements in dst with the supplied values in re...
  * `_mm_mask_fmadd_round_sh` **(Many-Argument Workhorses)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
  * `_mm_mask3_fmadd_round_sh` **(Many-Argument Workhorses)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
  * `_mm_maskz_fmadd_round_sh` **(Many-Argument Workhorses)** (Impact: 5.6)
    * *Intent:* /// Multiply the lower half-precision (16-bit) floating-point elements in a and b, and add the inter...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 4054`, `args: 1992`, `func_start: 1992`
* *Risk/State:* `state_mutation: 35`, `fragile_debt: 2`
* *Architecture:* `api: 1843`, `import: 8`
* *Defense:* `doc: 6405`, `test: 60`, `immutability_locks: 349`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` crate::arch::asm, crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::intrinsics::fmaf16, crate::intrinsics::simd::*, crate::ptr, crate::ptr::addr_of...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/x86/avx512bw.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 12.781)
- **Top Global Matches:** file_cluster_13: 12.781, file_cluster_15: 13.766, file_cluster_16: 14.009
- **Magnitude:** 5461.1 | **LOC:** 22275 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.1%)
- **Documentation Coverage:** 66.9864% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm512_alignr_epi8` **(Type Conversions)** (Impact: 17.4)
    * *Intent:* /// Concatenate pairs of 16-byte blocks in a and b into a 32-byte temporary result, shift the result...
  * `_mm512_bslli_epi128` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* /// Shift 128-bit lanes in a left by imm8 bytes while shifting in zeros, and store the results in ds...
  * `_mm512_bsrli_epi128` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* /// Shift 128-bit lanes in a right by imm8 bytes while shifting in zeros, and store the results in d...
  * `mask` **(Type Conversions)** (Impact: 7.3)
  * `mask` **(Type Conversions)** (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 4231`, `args: 1718`, `func_start: 1676`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 1652`, `import: 7`
* *Defense:* `doc: 2524`, `test: 331`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 7):` crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::hint::black_box, crate::intrinsics::simd::*, crate::mem, crate::ptr, stdarch_test::assert_instr...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/mips/msa.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.716)
- **Top Global Matches:** file_cluster_13: 5.716, file_cluster_2: 8.48, file_cluster_17: 8.963
- **Magnitude:** 4302.4 | **LOC:** 18398 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.2%), Debt Markers (formerly Tech Debt) (8.9%)
- **Documentation Coverage:** 74.5238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_msa_binsl_b` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_msa_binsr_b` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_msa_bmnz_v` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_msa_bmz_v` **(Annotated & Test Methods)** (Impact: 3.0)
  * `test_msa_bsel_v` **(Annotated & Test Methods)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1496`, `args: 1573`, `func_start: 1573`, `class_start: 10`
* *Risk/State:* `dead_code: 21`, `fragile_debt: 15`
* *Architecture:* `api: 1056`, `import: 4`
* *Defense:* `doc: 3559`, `test: 527`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` crate::core_arch::mips::msa::*, crate::core_arch::simd::*, crate::mem, stdarch_test::assert_instr, stdarch_test::simd_test
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/librustdoc/html/static/js/stringdex.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.934)
- **Top Global Matches:** file_cluster_4: 6.934, file_cluster_15: 11.447, file_cluster_6: 11.962
- **Magnitude:** 3981.96 | **LOC:** 4412 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.038; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (83.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 13.3339% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadDatabase` **(Many-Argument Workhorses)** (Impact: 678.5)
    * *Intent:* /** */
  * `makeSearchTreeFromBase64` **(Many-Argument Workhorses)** (Impact: 212.8)
    * *Intent:* /** */
  * `makeBranchesFromBinaryData` **(Many-Argument Workhorses)** (Impact: 117.3)
    * *Intent:* /** * "might_have_prefix_branches": SearchTreeBranches<SearchTree>, * "branches": SearchTreeBranches...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 82.7)
    * *Intent:* /** */
  * `intersection` **(Defensive Guards)** (Impact: 54.8)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 523 instances
* *Concurrency (weighted view):* 155
* *State Mutation (weighted view):* 1850
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 627`, `structural_boundaries: 424`, `args: 128`, `func_start: 112`, `class_start: 20`
* *Risk/State:* `state_mutation: 804`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `concurrency: 45`
* *Defense:* `safety: 188`, `doc: 197`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/etc/completions/x.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.249)
- **Top Global Matches:** file_cluster_1: 6.249, file_cluster_3: 48.292, file_cluster_8: 70.107
- **Magnitude:** 3560.4 | **LOC:** 4289 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (73.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_x` **(Many-Argument Workhorses)** (Impact: 1089.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 657 instances
* *Concurrency (weighted view):* 154
* *State Mutation (weighted view):* 2226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 622`, `structural_boundaries: 2895`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 912`
* *Architecture:* `io: 57`, `concurrency: 44`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_trait_selection/src/error_reporting/traits/suggestions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.287)
- **Top Global Matches:** file_cluster_8: 9.287, file_cluster_3: 17.507, file_cluster_6: 20.478
- **Magnitude:** 3444.3 | **LOC:** 6062 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **93**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.1%), Mutation Surface (formerly State Flux) (53.7%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `note_obligation_cause_code` **(Many-Argument Workhorses)** (Impact: 521.4)
  * `note_function_argument_obligation` **(Many-Argument Workhorses)** (Impact: 188.2)
  * `suggest_add_reference_to_arg` **(Many-Argument Workhorses)** (Impact: 140.9)
  * `suggest_dereferences` **(Many-Argument Workhorses)** (Impact: 140.8)
    * *Intent:* /// Provide a suggestion to dereference arguments to functions and binary operators, if that /// wou...
  * `note_obligation_cause_for_async_await` **(Many-Argument Workhorses)** (Impact: 100.2)
    * *Intent:* /// Unconditionally adds the diagnostic note described in /// `maybe_note_obligation_cause_for_async...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 103 instances
* *Concurrency (weighted view):* 71
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 993`, `structural_boundaries: 1353`, `args: 256`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 128`, `dead_code: 3`, `planned_debt: 15`, `fragile_debt: 22`
* *Architecture:* `api: 46`, `concurrency: 41`, `import: 38`
* *Defense:* `safety: 181`, `doc: 96`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 47):` crate::error_reporting::TypeErrCtxt, crate::errors, crate::infer::InferCtxtExt, crate::traits::ImplDerivedCause, crate::traits::NormalizeExt, crate::traits::ObligationCtxt, crate::traits::query::evaluate_obligation::InferCtxtExt, itertools::EitherOrBoth...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/x86_64/avx512f.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.815)
- **Top Global Matches:** file_cluster_13: 6.815, file_cluster_11: 8.827, file_cluster_2: 8.891
- **Magnitude:** 3369.44 | **LOC:** 13199 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (9.6%)
- **Documentation Coverage:** 98.7572% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_mm512_mask_i64gather_epi32` **(Annotated & Test Methods)** (Impact: 2.8)
  * `test_mm512_i32scatter_pd` **(Annotated & Test Methods)** (Impact: 2.8)
  * `test_mm512_mask_i32scatter_pd` **(Annotated & Test Methods)** (Impact: 2.8)
  * `test_mm512_i64scatter_pd` **(Annotated & Test Methods)** (Impact: 2.8)
  * `test_mm512_mask_i64scatter_pd` **(Annotated & Test Methods)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 5294`, `args: 1234`, `func_start: 1228`, `class_start: 4`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1216`, `import: 7`
* *Defense:* `doc: 168`, `test: 220`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 5):` crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::core_arch::x86_64::*, crate::hint::black_box, crate::mem::transmute, stdarch_test::assert_instr, stdarch_test::simd_test
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/std/src/sys/pal/windows/c/windows_sys.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 9.19)
- **Top Global Matches:** file_cluster_13: 9.19, file_cluster_17: 9.357, file_cluster_15: 9.842
- **Magnitude:** 3107.86 | **LOC:** 3664 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.016; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.0%), Complexity Load (formerly Cognitive Load) (5.5%)
- **Documentation Coverage:** 94.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_u128` **(Type Conversions)** (Impact: 1.8)
  * `default` **(State Mutators)** (Impact: 1.1)
  * `default` **(State Mutators)** (Impact: 1.1)
  * `default` **(State Mutators)** (Impact: 1.1)
  * `default` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 314`, `args: 190`, `func_start: 50`, `class_start: 74`
* *Risk/State:* `duplicate_logic: 49`
* *Architecture:* `api: 2979`
* *Defense:* `immutability_locks: 2396`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_hir_typeck/src/method/suggest.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.591)
- **Top Global Matches:** file_cluster_8: 7.591, file_cluster_6: 18.084, file_cluster_3: 19.585
- **Magnitude:** 3089.0 | **LOC:** 4893 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **85**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (56.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.7%), Guard Balance (formerly Safety Score) (50.5%)
- **Documentation Coverage:** 73.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `suggest_traits_to_import` **(Many-Argument Workhorses)** (Impact: 444.3)
  * `handle_unsatisfied_predicates` **(Many-Argument Workhorses)** (Impact: 343.0)
  * `report_method_error` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `note_candidates_on_method_error` **(Many-Argument Workhorses)** (Impact: 105.7)
  * `report_failed_method_call_on_numerical_infer_var` **(Many-Argument Workhorses)** (Impact: 103.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 87 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 768`, `structural_boundaries: 979`, `args: 252`, `func_start: 59`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 117`, `dead_code: 3`, `planned_debt: 16`, `fragile_debt: 13`
* *Architecture:* `api: 10`, `concurrency: 5`, `import: 48`
* *Defense:* `safety: 139`, `doc: 29`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 48):` core::ops::ControlFlow, crate::Expectation, crate::FnCtxt, crate::errors, crate::errors::CandidateTraitNote, crate::errors::NoAssociatedItem, crate::method::probe::UnsatisfiedPredicates, hir::Expr...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `compiler/rustc_borrowck/src/diagnostics/conflict_errors.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.32)
- **Top Global Matches:** file_cluster_8: 9.32, file_cluster_3: 17.122, file_cluster_6: 20.694
- **Magnitude:** 2656.2 | **LOC:** 4741 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **105**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.1%), Guard Balance (formerly Safety Score) (49.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.9%)
- **Documentation Coverage:** 77.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `suggest_ref_or_clone` **(Many-Argument Workhorses)** (Impact: 189.7)
  * `suggest_cloning` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `report_use_of_moved_or_uninitialized` **(Many-Argument Workhorses)** (Impact: 119.5)
  * `suggest_slice_method_if_applicable` **(Many-Argument Workhorses)** (Impact: 104.3)
  * `explain_iterator_advancement_in_for_loop_if_applicable` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* /// Suggest using `while let` for call `next` on an iterator in a for loop. /// /// For example: ///...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 1044`, `args: 174`, `func_start: 68`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 120`, `dead_code: 19`, `planned_debt: 4`, `fragile_debt: 16`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `concurrency: 8`, `import: 52`
* *Defense:* `safety: 149`, `doc: 110`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 55):` crate::InitializationRequiringAction, crate::MirBorrowckCtxt, crate::WriteKind, crate::borrow_set::BorrowData, crate::borrow_set::TwoPhaseActivation, crate::borrowck_errors, crate::diagnostics::CapturedMessageOpt, crate::diagnostics::call_kind...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/x86/avx512dq.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.205)
- **Top Global Matches:** file_cluster_13: 7.205, file_cluster_0: 9.367, file_cluster_15: 9.539
- **Magnitude:** 2615.7 | **LOC:** 11178 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.011; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (81.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.5%), Complexity Load (formerly Cognitive Load) (2.6%)
- **Documentation Coverage:** 68.2578% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm512_inserti32x8` **(Annotated & Test Methods)** (Impact: 4.9)
    * *Intent:* /// Copy a to dst, then insert 256 bits (composed of 8 packed 32-bit integers) from b into dst at th...
  * `_mm512_insertf32x8` **(Annotated & Test Methods)** (Impact: 4.8)
    * *Intent:* // Insert /// Copy a to dst, then insert 256 bits (composed of 8 packed single-precision (32-bit) fl...
  * `_mm512_inserti64x2` **(Annotated & Test Methods)** (Impact: 4.4)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed 64-bit integers) from b into dst at th...
  * `_mm512_insertf64x2` **(Annotated & Test Methods)** (Impact: 4.3)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed double-precision (64-bit) floating-poi...
  * `_mm256_inserti64x2` **(Annotated & Test Methods)** (Impact: 4.3)
    * *Intent:* /// Copy a to dst, then insert 128 bits (composed of 2 packed 64-bit integers) from b into dst at th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 1660`, `args: 858`, `func_start: 858`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 798`, `import: 5`
* *Defense:* `doc: 2515`, `test: 55`, `immutability_locks: 201`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` crate::core_arch::assert_eq_const, crate::core_arch::simd::*, crate::core_arch::x86::*, crate::intrinsics::simd::*, crate::mem::transmute, self::*, stdarch_test::simd_test
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/hexagon/v128.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.166)
- **Top Global Matches:** file_cluster_13: 7.166, file_cluster_0: 8.51, file_cluster_2: 9.347
- **Magnitude:** 2533.44 | **LOC:** 7490 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.016; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `q6_vgather_aqrmvh` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vv32.h).h` /// /// This is a compound operation composed of mu...
  * `q6_vgather_aqrmww` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vvv32.w).h` /// /// This is a compound operation composed of m...
  * `q6_vgather_aqrmvw` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.w=vgather(Rt32,Mu2,Vv32.w).w` /// /// This is a compound operation composed of mu...
  * `q6_vscatter_qrmvhv` **(State Mutators)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vv32.h).h=Vw32` /// /// This is a compound operation composed of mul...
  * `q6_vscatter_qrmwwv` **(State Mutators)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vvv32.w).h=Vw32` /// /// This is a compound operation composed of mu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 952`, `func_start: 952`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 479`, `import: 2`
* *Defense:* `doc: 2036`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` crate::intrinsics::simd::simd_add, crate::intrinsics::simd::simd_and, crate::intrinsics::simd::simd_or, crate::intrinsics::simd::simd_sub, crate::intrinsics::simd::simd_xor, stdarch_test::assert_instr
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/core_arch/src/hexagon/v64.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.166)
- **Top Global Matches:** file_cluster_13: 7.166, file_cluster_0: 8.51, file_cluster_2: 9.347
- **Magnitude:** 2533.44 | **LOC:** 7490 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.016; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `q6_vgather_aqrmvh` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vv32.h).h` /// /// This is a compound operation composed of mu...
  * `q6_vgather_aqrmww` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.h=vgather(Rt32,Mu2,Vvv32.w).h` /// /// This is a compound operation composed of m...
  * `q6_vgather_aqrmvw` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vtmp.w=vgather(Rt32,Mu2,Vv32.w).w` /// /// This is a compound operation composed of mu...
  * `q6_vscatter_qrmvhv` **(State Mutators)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vv32.h).h=Vw32` /// /// This is a compound operation composed of mul...
  * `q6_vscatter_qrmwwv` **(State Mutators)** (Impact: 3.3)
    * *Intent:* /// `if (Qs4) vscatter(Rt32,Mu2,Vvv32.w).h=Vw32` /// /// This is a compound operation composed of mu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 952`, `func_start: 952`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 479`, `import: 2`
* *Defense:* `doc: 2036`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.016
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` crate::intrinsics::simd::simd_add, crate::intrinsics::simd::simd_and, crate::intrinsics::simd::simd_or, crate::intrinsics::simd::simd_sub, crate::intrinsics::simd::simd_xor, stdarch_test::assert_instr
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_resolve/src/late/diagnostics.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.687)
- **Top Global Matches:** file_cluster_8: 8.687, file_cluster_6: 9.309, file_cluster_4: 17.39
- **Magnitude:** 2458.74 | **LOC:** 4585 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **92**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.1%), Guard Balance (formerly Safety Score) (49.3%), Mutation Surface (formerly State Flux) (42.4%)
- **Documentation Coverage:** 70.8861% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `smart_resolve_context_dependent_help` **(Many-Argument Workhorses)** (Impact: 248.2)
    * *Intent:* /// Provides context-dependent help for errors reported by the `smart_resolve_path_fragment` /// fun...
  * `add_missing_lifetime_specifiers_label` **(Many-Argument Workhorses)** (Impact: 209.7)
  * `try_lookup_name_relaxed` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `suggest_assoc_type_from_bounds` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /// This does best-effort work to generate suggestions for associated types.
  * `make_base_error` **(Many-Argument Workhorses)** (Impact: 115.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 756`, `structural_boundaries: 996`, `args: 248`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 87`, `dead_code: 6`, `fragile_debt: 8`
* *Architecture:* `api: 26`, `concurrency: 2`, `import: 61`
* *Defense:* `safety: 136`, `doc: 81`, `test: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 34):` crate::Finalize, crate::Module, crate::ModuleKind, crate::ModuleOrUniformRoot, crate::ParentScope, crate::PathResult, crate::PathSource, crate::Resolver...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/stdarch-gen-loongarch/lasxintrin.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.081)
- **Top Global Matches:** file_cluster_15: 6.081, file_cluster_17: 6.89, file_cluster_2: 7.304
- **Magnitude:** 2230.24 | **LOC:** 5533 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Connectivity (formerly Api Exposure) (16.3%)
- **Documentation Coverage:** 60.325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__lasx_xvmadd_b` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_h` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_w` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmadd_d` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lasx_xvmsub_b` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 599`, `args: 555`, `func_start: 555`
* *Risk/State:* `safety_bypasses: 2`, `unreferenced_by_name: 555`
* *Architecture:* `api: 1133`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 1):` lsxintrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compiler/rustc_resolve/src/late.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.966)
- **Top Global Matches:** file_cluster_4: 6.966, file_cluster_0: 10.348, file_cluster_12: 10.738
- **Magnitude:** 2218.0 | **LOC:** 5611 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **102**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (76.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.1%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 84.4156% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `smart_resolve_path_fragment` **(Many-Argument Workhorses)** (Impact: 133.0)
  * `with_generic_param_rib` **(Many-Argument Workhorses)** (Impact: 94.1)
  * `resolve_anonymous_lifetime` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `resolve_elided_lifetimes_in_path` **(Many-Argument Workhorses)** (Impact: 91.2)
  * `resolve_qpath` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* /// Handles paths that may refer to associated items.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 101 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 913`, `args: 361`, `func_start: 131`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 6`, `state_mutation: 195`, `dead_code: 2`, `fragile_debt: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 44`, `import: 34`
* *Defense:* `safety: 106`, `doc: 274`, `test: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 40):` diagnostics, LifetimeBinderKind::*, ResolutionError::*, crate::BindingError, crate::BindingKey, crate::Decl, crate::DelegationFnSig, crate::Finalize...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `compiler/rustc_parse/src/parser/expr.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.466)
- **Top Global Matches:** file_cluster_4: 6.466, file_cluster_6: 11.25, file_cluster_16: 12.144
- **Magnitude:** 2182.84 | **LOC:** 4451 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **110**; blast radius 0.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.0%), Guard Balance (formerly Safety Score) (51.5%), Mutation Surface (formerly State Flux) (45.8%)
- **Documentation Coverage:** 52.1505% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_expr_bottom` **(Compute Cores)** (Impact: 128.1)
    * *Intent:* /// At the bottom (top?) of the precedence hierarchy, /// Parses things like parenthesized exprs, ma...
  * `parse_expr_assoc_rest_with` **(Many-Argument Workhorses)** (Impact: 108.7)
    * *Intent:* /// Parses the rest of an associative expression (i.e. the part after the lhs) with operators /// of...
  * `parse_struct_fields` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `parse_arm` **(Compute Cores)** (Impact: 62.1)
  * `parse_expr_labeled` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* /// Parse `'label: $expr`. The label is already parsed.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 807`, `structural_boundaries: 866`, `args: 314`, `func_start: 145`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 88`, `dead_code: 7`, `fragile_debt: 12`
* *Architecture:* `api: 42`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 76`, `doc: 130`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.012
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 37):` FloatComponent::*, ast::CoroutineKind, ast::ForLoopKind, ast::GenBlockKind, ast::MatchKind, ast::Pat, ast::Path, ast::PathSegment...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `compiler/rustc_hir_typeck/src/fn_ctxt/suggestions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.499)
- **Top Global Matches:** file_cluster_6: 7.499, file_cluster_8: 11.913, file_cluster_4: 14.427
- **Magnitude:** 2106.0 | **LOC:** 3743 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **72**; blast radius 0.011; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.7%), Connectivity (formerly Api Exposure) (30.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.3%)
- **Documentation Coverage:** 52.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `suggest_deref_or_ref` **(Many-Argument Workhorses)** (Impact: 218.2)
    * *Intent:* /// /// ```compile_fail,E0308 /// fn some_fn(s: &str) {} /// /// let x = "hey!".to_owned(); /// some...
  * `suggest_cast` **(Many-Argument Workhorses)** (Impact: 192.8)
  * `suggest_deref_ref_or_into` **(Many-Argument Workhorses)** (Impact: 152.3)
  * `suggest_compatible_variants` **(Many-Argument Workhorses)** (Impact: 102.9)
    * *Intent:* /// If the expected type is an enum (Issue #55250) with any variants whose /// sole field is of the ...
  * `note_type_is_not_clone` **(Many-Argument Workhorses)** (Impact: 91.8)
    * *Intent:* /// Suggest that `&T` was cloned instead of `T` because `T` does not implement `Clone`, /// which is...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 655`, `structural_boundaries: 758`, `args: 133`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 3`, `state_mutation: 39`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 9`
* *Architecture:* `api: 39`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 100`, `doc: 114`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.011
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 39):` core::cmp::min, core::iter, crate::errors, crate::fn_ctxt::rustc_span::BytePos, crate::method::probe, crate::method::probe::IsSuggestion, crate::method::probe::Mode, crate::method::probe::ProbeScope...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_parse/src/parser/item.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.009)
- **Top Global Matches:** file_cluster_6: 6.009, file_cluster_4: 12.564, file_cluster_8: 12.772
- **Magnitude:** 2098.74 | **LOC:** 3645 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **56**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.1%), Guard Balance (formerly Safety Score) (50.8%), Mutation Surface (formerly State Flux) (35.7%)
- **Documentation Coverage:** 38.3838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_item_kind` **(Many-Argument Workhorses)** (Impact: 292.9)
    * *Intent:* /// Parses one of the items allowed by the flags.
  * `parse_fn_front_matter` **(Many-Argument Workhorses)** (Impact: 100.3)
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
* *Structure:* `branch: 781`, `structural_boundaries: 757`, `args: 218`, `func_start: 84`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 4`, `state_mutation: 50`, `dead_code: 9`, `fragile_debt: 13`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 62`, `doc: 230`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 31):` ast::token::IdentIsRaw, crate::errors, crate::errors::FnPointerCannotBeAsync, crate::errors::FnPointerCannotBeConst, crate::errors::MacroExpandsToAdtField, crate::exp, rustc_ast, rustc_ast::ast::*...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `library/stdarch/crates/stdarch-gen-loongarch/lsxintrin.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.989)
- **Top Global Matches:** file_cluster_15: 5.989, file_cluster_17: 6.554, file_cluster_2: 7.041
- **Magnitude:** 2093.84 | **LOC:** 5220 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.02; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%)
- **Documentation Coverage:** 60.325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__lsx_vmadd_b` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_h` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_w` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmadd_d` **(Parameter Forwarders)** (Impact: 2.2)
  * `__lsx_vmsub_b` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 563`, `args: 519`, `func_start: 519`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 1061`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `compiler/rustc_middle/src/ty/print/pretty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.722)
- **Top Global Matches:** file_cluster_4: 8.722, file_cluster_6: 10.426, file_cluster_0: 14.193
- **Magnitude:** 2087.28 | **LOC:** 3559 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **84** in-repo importer(s); it depends on **67**; blast radius 0.142; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.1%), Debt Markers (formerly Tech Debt) (52.9%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 74.0506% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pretty_print_type` **(Many-Argument Workhorses)** (Impact: 327.6)
  * `pretty_print_opaque_impl_type` **(Many-Argument Workhorses)** (Impact: 195.0)
  * `pretty_print_const_valtree` **(Many-Argument Workhorses)** (Impact: 111.0)
  * `pretty_print_const_scalar_int` **(Many-Argument Workhorses)** (Impact: 88.7)
  * `try_print_visible_def_path_recur` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* /// Does the work of `try_print_visible_def_path`, building the /// full definition path recursively...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 889`, `structural_boundaries: 600`, `args: 224`, `func_start: 124`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 68`, `planned_debt: 1`, `fragile_debt: 21`, `duplicate_logic: 7`
* *Architecture:* `api: 63`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 65`, `doc: 120`, `test: 2`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 41):` crate::mir::UnOp, crate::mir::interpret::AllocRange, crate::mir::interpret::GlobalAlloc, crate::mir::interpret::Pointer, crate::mir::interpret::Provenance, crate::mir::interpret::Scalar, crate::query::IntoQueryKey, crate::query::Providers...
  * `Imported By (In-Degree: 84):` (Excluded from Brief to save tokens)

### `src/librustdoc/html/render/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.763)
- **Top Global Matches:** file_cluster_6: 7.763, file_cluster_4: 8.691, file_cluster_12: 16.063
- **Magnitude:** 2084.98 | **LOC:** 3062 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **90**; blast radius 0.031; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%), Connectivity (formerly Api Exposure) (34.4%)
- **Documentation Coverage:** 82.7957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_impl` **(Many-Argument Workhorses)** (Impact: 357.3)
  * `doc_impl_item` **(Many-Argument Workhorses)** (Impact: 211.5)
    * *Intent:* // For trait implementations, the `interesting` output contains all methods that have doc // comment...
  * `repr_attribute` **(Many-Argument Workhorses)** (Impact: 58.8)
    * *Intent:* /// Compute the *public* `#[repr]` of the item given by `DefId`. /// /// Read more about it here: //...
  * `render_impl_summary` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `render_call_locations` **(Many-Argument Workhorses)** (Impact: 44.0)
    * *Intent:* /// Generates the HTML for example call locations generated via the --scrape-examples flag.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 117 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 564`, `args: 182`, `func_start: 74`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 5`, `state_mutation: 165`, `fragile_debt: 4`
* *Architecture:* `api: 45`, `concurrency: 1`, `import: 39`
* *Defense:* `safety: 56`, `doc: 81`, `test: 10`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 47):` context, ordered_json, print_item, search_index, sidebar, sorted_template, span_map, tests...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/tools/clippy/clippy_lints/src/zero_repeat_side_effects.rs` (RUST) | Magnitude: 0.09 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 44, branch: 29, doc: 25
- `tests/ui/consts/const-blocks/const-repeat.rs` (RUST) | Magnitude: 5.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 3, func_start: 3
- `tests/ui/privacy/private-method.rs` (RUST) | Magnitude: 7.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 4, args: 3, func_start: 3
- `src/tools/rust-installer/src/compression.rs` (RUST) | Magnitude: 0.1 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 49, generics: 39, branch: 32
- `tests/ui/drop/explicit-call-to-dtor.rs` (RUST) | Magnitude: 3.06 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/tools/miri/tests/fail-dep/concurrency/libc_pthread_mutex_free_while_queued.rs` (RUST) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 10, sync_locks: 7, args: 6
- `tests/ui/contracts/internal_machinery/contracts-lowering-requires-is-not-inherited-when-nesting.rs` (RUST) | Magnitude: 2.84 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, args: 3, structural_boundaries: 2, func_start: 2
- `tests/ui/closures/2229_closure_analysis/migrations/migrations_rustfix.rs` (RUST) | Magnitude: 8.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, args: 6, core_var_decl: 5
- `tests/ui/proc-macro/auxiliary/make-macro.rs` (RUST) | Magnitude: 16.32 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, debug_prints: 3, structural_boundaries: 2, decorators: 2
- `src/tools/miri/tests/genmc/pass/litmus/2w2w_3sc_1rel.rs` (RUST) | Magnitude: 0.03 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, state_mutation: 6, decorators: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/tools/clippy/tests/ui-toml/toml_trivially_copy/test.rs` (RUST) | Magnitude: 0.01 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, decorators: 4, args: 3, func_start: 3
- `tests/ui/async-await/issues/issue-59972.rs` (RUST) | Magnitude: 13.32 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, concurrency: 6, args: 5
- `tests/ui/lint/non-snake-case/allow-snake-case-field-destructuring-issue-89469.rs` (RUST) | Magnitude: 4.64 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, args: 3, func_start: 3
- `tests/ui/async-await/await-keyword/2015-edition-error-various-positions.rs` (RUST) | Magnitude: 14.84 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 16, concurrency: 10, indent_spaces: 6, args: 2
- `src/tools/clippy/tests/ui-toml/undocumented_unsafe_blocks/undocumented_unsafe_blocks.rs` (RUST) | Magnitude: 0.2 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 321, structural_boundaries: 112, args: 80, func_start: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/tools/miri/src/borrow_tracker/tree_borrows/diagnostics.rs` (RUST) | Magnitude: 0.41 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 548, doc: 205, structural_boundaries: 149, core_var_decl: 75
- `src/tools/miri/tests/pass/arrays.rs` (RUST) | Magnitude: 0.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 16, core_var_decl: 16, args: 14
- `src/tools/remote-test-client/src/main.rs` (RUST) | Magnitude: 0.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 284, structural_boundaries: 103, core_var_decl: 56, design_snake_case: 51
- `src/librustdoc/html/escape/tests.rs` (RUST) | Magnitude: 8.66 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, test: 36, structural_boundaries: 5, import: 3
- `compiler/rustc_thread_pool/src/sleep/mod.rs` (RUST) | Magnitude: 157.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 199, doc: 58, structural_boundaries: 49, branch: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `library/coretests/tests/clone.rs` (RUST) | Magnitude: 42.62 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 79, test: 44, core_var_decl: 42
- `tests/ui/parser/issues/issue-27255.rs` (RUST) | Magnitude: 1.18 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1
- `tests/assembly-llvm/regparm-module-flag.rs` (RUST) | Magnitude: 12.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: pointers: 12, structural_boundaries: 9, indent_spaces: 7, decorators: 6
- `tests/ui/consts/const-nullary-enum.rs` (RUST) | Magnitude: 4.86 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, branch: 2, high_risk_execution: 2, globals: 2
- `tests/ui/span/issue-27522.rs` (RUST) | Magnitude: 2.7 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/ui/derived-errors/issue-31997-1.rs` (RUST) | Magnitude: 12.9 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 22, core_var_decl: 14, design_snake_case: 14
- `src/tools/miri/tests/pass-dep/libc/prctl-threadname.rs` (RUST) | Magnitude: 0.02 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 24, core_var_decl: 13, design_snake_case: 13
- `src/librustdoc/build.rs` (RUST) | Magnitude: 13.64 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 63, immutability_locks: 35, structural_boundaries: 12, safety_bypasses: 10
- `tests/ui/lint/rfc-2383-lint-reason/expect_tool_lint_rfc_2383.rs` (RUST) | Magnitude: 46.1 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 27, doc: 23, core_var_decl: 20
- `tests/ui/lint/rfc-2383-lint-reason/expect_nested_lint_levels.rs` (RUST) | Magnitude: 10.16 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, safety_bypasses: 7, decorators: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `library/std/src/sys/random/fuchsia.rs` (RUST) | Magnitude: 4.54 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 2, func_start: 2
- `tests/codegen-llvm/global-allocator-attributes.rs` (RUST) | Magnitude: 9.22 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, pointers: 8, args: 4
- `tests/ui/methods/suggest-method-on-call-for-ambig-receiver.rs` (RUST) | Magnitude: 6.94 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, core_var_decl: 3, structural_boundaries: 2, args: 2
- `tests/ui/abi/variadic-ffi.rs` (RUST) | Magnitude: 24.36 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 22, test: 13, core_var_decl: 11
- `tests/ui/or-patterns/binding-typo-2.rs` (RUST) | Magnitude: 26.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, branch: 10, structural_boundaries: 9, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `compiler/rustc_target/src/spec/targets/armv7s_apple_ios.rs` (RUST) | Magnitude: 3.44 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 3, import: 2, args: 1
- `src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0012_visibility.rs` (RUST) | Magnitude: 0.01 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 5, func_start: 5, api: 5, unreferenced_by_name: 5
- `compiler/rustc_target/src/spec/base/solaris.rs` (RUST) | Magnitude: 2.78 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 1, args: 1, func_start: 1
- `compiler/rustc_target/src/spec/targets/powerpc64_ibm_aix.rs` (RUST) | Magnitude: 4.66 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 3, args: 1, func_start: 1
- `compiler/rustc_target/src/spec/targets/i686_unknown_helenos.rs` (RUST) | Magnitude: 7.68 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 4, structural_boundaries: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/ui/consts/const-meth-pattern.rs` (RUST) | Magnitude: 3.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, core_var_decl: 3, structural_boundaries: 2, args: 2
- `tests/ui/inline-const/expr-unsafe-err.rs` (RUST) | Magnitude: 2.56 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, args: 2, func_start: 2, immutability_locks: 2
- `tests/ui/macros/issue-57597.rs` (RUST) | Magnitude: 2.5 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, branch: 18, reflection_metaprogramming: 12, macros: 12
- `tests/ui/const-generics/early/const_arg_trivial_macro_expansion-1.rs` (RUST) | Magnitude: 550.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 389, args: 362, func_start: 361, branch: 240
- `tests/mir-opt/const_allocation2.rs` (RUST) | Magnitude: 1.22 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 2, immutability_locks: 2, indent_spaces: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/tools/rustfmt/tests/source/issue_4675.rs` (RUST) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, reflection_metaprogramming: 1, macros: 1
- `tests/rustdoc-json/traits/has_body.rs` (RUST) | Magnitude: 12.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 7, func_start: 7, indent_spaces: 7, unreferenced_by_name: 7
- `tests/rustdoc-html/extern/link-extern-crate-title-33178.rs` (RUST) | Magnitude: 13.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 2, decorators: 1
- `tests/ui/simd/portable-intrinsics-arent-exposed.rs` (RUST) | Magnitude: 1.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, args: 1, func_start: 1
- `tests/ui/consts/const-eval/parse_ints.rs` (RUST) | Magnitude: 1.24 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 3, immutability_locks: 3, indent_spaces: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `compiler/rustc_mir_transform/src/inline.rs` (RUST) | Magnitude: 698.9 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 978, structural_boundaries: 289, branch: 177, generics: 149
- `compiler/rustc_builtin_macros/src/format_foreign.rs` (RUST) | Magnitude: 409.7 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 644, structural_boundaries: 174, core_var_decl: 124, branch: 102
- `src/tools/rust-analyzer/crates/hir-def/src/attrs.rs` (RUST) | Magnitude: 0.98 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1396, structural_boundaries: 384, branch: 222, core_var_decl: 205
- `src/tools/miri/src/concurrency/genmc/shims.rs` (RUST) | Magnitude: 0.09 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 46, sync_locks: 46, generics: 38
- `src/tools/unicode-table-generator/src/raw_emitter.rs` (RUST) | Magnitude: 0.2 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 284, structural_boundaries: 86, branch: 48, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/ui/allocator/no_std-alloc-error-handler-custom.rs` (RUST) | Magnitude: 24.22 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 18, pointers: 15, decorators: 12
- `library/alloctests/tests/boxed.rs` (RUST) | Magnitude: 81.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 50, pointers: 33, core_var_decl: 25
- `library/stdarch/crates/stdarch-gen-arm/src/predicate_forms.rs` (RUST) | Magnitude: 114.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 162, branch: 38, structural_boundaries: 36, args: 21
- `src/tools/rustfmt/src/emitter/checkstyle.rs` (RUST) | Magnitude: 0.05 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 47, core_var_decl: 33, design_snake_case: 28
- `compiler/rustc_codegen_llvm/src/llvm/enzyme_ffi.rs` (RUST) | Magnitude: 210.16 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 424, structural_boundaries: 99, pointers: 73, args: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `compiler/rustc_span/src/edit_distance.rs` (RUST) | Magnitude: 151.26 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 49, doc: 49, branch: 37
- `src/tools/clippy/clippy_lints/src/useless_conversion.rs` (RUST) | Magnitude: 0.27 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 124, branch: 101, core_var_decl: 39
- `src/tools/clippy/clippy_lints/src/loops/same_item_push.rs` (RUST) | Magnitude: 0.13 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 50, generics: 42, branch: 36
- `src/tools/clippy/clippy_lints/src/derivable_impls.rs` (RUST) | Magnitude: 0.13 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 56, branch: 45, doc: 35
- `library/stdarch/crates/stdarch-gen-arm/src/intrinsic.rs` (RUST) | Magnitude: 882.2 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1379, structural_boundaries: 332, branch: 276, args: 135

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/run-make/rustdoc-map-file/rmake.rs` (RUST) | Magnitude: 20.2 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 11, branch: 7, core_var_decl: 7
- `src/tools/clippy/tests/ui/redundant_slicing.rs` (RUST) | Magnitude: 0.0 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 23, core_var_decl: 15, design_short_vars: 11
- `compiler/rustc_codegen_cranelift/build_system/bench.rs` (RUST) | Magnitude: 53.26 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 34, core_var_decl: 32, design_snake_case: 31
- `library/stdarch/ci/intrinsic-test-docker.sh` (SHELL) | Magnitude: 1.48 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 17, args: 7, debug_prints: 6
- `tests/ui/contracts/contracts-ensures-early-fn-exit.rs` (RUST) | Magnitude: 11.12 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 13, decorators: 7, branch: 5, test: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `compiler/rustc_mir_transform/src/validate.rs` (RUST) | Magnitude: 710.56 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1456, branch: 251, structural_boundaries: 242, core_var_decl: 101
- `src/tools/clippy/clippy_lints/src/methods/unnecessary_to_owned.rs` (RUST) | Magnitude: 0.5 | Delta: **0.186** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 569, branch: 180, structural_boundaries: 172, generics: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `compiler/rustc_hir_analysis/src/hir_ty_lowering/cmse.rs` (RUST) | Magnitude: 88.0 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 41, branch: 24, generics: 24
- `src/tools/clippy/tests/ui/set_contains_or_insert.rs` (RUST) | Magnitude: 0.13 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 114, branch: 29, state_mutation: 25, structural_boundaries: 24
- `compiler/rustc_target/src/callconv/hexagon.rs` (RUST) | Magnitude: 40.8 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 18, branch: 17, generics: 12
- `src/tools/clippy/clippy_lints/src/operators/manual_is_multiple_of.rs` (RUST) | Magnitude: 0.06 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, generics: 22, structural_boundaries: 21, branch: 19
- `library/stdarch/crates/stdarch-gen-arm/src/context.rs` (RUST) | Magnitude: 109.66 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 216, args: 37, structural_boundaries: 35, branch: 32

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `compiler/rustc_middle/src/query/plumbing.rs` -> Churn: **100.0%** | Cog Load: 3.4442% | Debt: 64.5159%
- `compiler/rustc_query_impl/src/plumbing.rs` -> Churn: **99.05%** | Cog Load: 7.576% | Debt: 56.9001%
- `compiler/rustc_middle/src/ty/context.rs` -> Churn: **75.1%** | Cog Load: 5.4217% | Debt: 62.348%
- `compiler/rustc_query_impl/src/dep_kind_vtables.rs` -> Churn: **68.96%** | Cog Load: 4.9001% | Debt: 79.35%
- `compiler/rustc_infer/src/infer/relate/generalize.rs` -> Churn: **67.89%** | Cog Load: 7.9503% | Debt: 60.8539%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `library/stdarch/crates/core_arch/src/mips/msa.rs` -> **cyrgani** (100.0% isolated ownership) | Magnitude: 4302.4
- `src/librustdoc/html/static/js/stringdex.js` -> **Michael Howell** (100.0% isolated ownership) | Magnitude: 3981.96
- `src/etc/completions/x.sh` -> **Urhengulas** (100.0% isolated ownership) | Magnitude: 3560.4
- `src/librustdoc/html/render/mod.rs` -> **Guillaume Gomez** (100.0% isolated ownership) | Magnitude: 2084.98
- `library/stdarch/crates/core_arch/src/s390x/vector.rs` -> **Ralf Jung** (100.0% isolated ownership) | Magnitude: 1991.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `library/core/src/marker.rs` -> **Severity: 1710.77** (Blast Radius: 39.918 * Doc Risk: 42.8571%)
- `library/core/src/marker/variance.rs` -> **Severity: 1086.78** (Blast Radius: 18.113 * Doc Risk: 60.0%)
- `library/core/src/hash/mod.rs` -> **Severity: 982.865** (Blast Radius: 16.204 * Doc Risk: 60.6557%)
- `tests/rustdoc-html/notable-trait/doc-notable_trait_box_is_not_an_iterator.rs` -> **Severity: 907.0** (Blast Radius: 9.07 * Doc Risk: 100.0%)
- `library/core/src/fmt/mod.rs` -> **Severity: 490.208** (Blast Radius: 18.8 * Doc Risk: 26.0749%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 9583 literal sites + 471 sites through wrappers = 10054
- **`panics_and_aborts`:** 5174 literal sites + 269 sites through wrappers = 5443

- `eprint` (function, debug_prints, primitive): 42 call sites in 1 files -- `src/bootstrap/bootstrap.py`
- `foo` (function, debug_prints, primitive): 24 call sites in 1 files -- `src/tools/clippy/tests/ui/unit_arg.rs`
- `make_foo` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `tests/ui/borrowck/borrowck-borrow-from-owned-ptr.rs`
- `make_foo` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `tests/ui/borrowck/borrowck-borrow-from-stack-variable.rs`
- `foo_rslice` (function, debug_prints, primitive): 12 call sites in 1 files -- `src/tools/clippy/tests/ui/useless_asref.rs`
- `tracked_env_var_os` (function, debug_prints, primitive): 12 call sites in 1 files -- `compiler/rustc_llvm/build.rs`
- `repeat` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `src/tools/clippy/tests/ui/match_same_arms_non_exhaustive.rs`
- `consume` (function, debug_prints, primitive): 9 call sites in 1 files -- `tests/ui/lint/dangling-pointers-from-temporaries/calls.rs`
- `foo_mrslice` (function, debug_prints, primitive): 8 call sites in 1 files -- `src/tools/clippy/tests/ui/useless_asref.rs`
- `panic_action` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `src/tools/clippy/clippy_dev/src/utils.rs`
- `show` (function, debug_prints, primitive): 8 call sites in 1 files -- `tests/ui/issues/issue-21922.rs`
- `cond` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `tests/ui/borrowck/borrowck-lend-flow-loop.rs`
*(+392 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 557867 call pairs -- scoped 28.7%, unique 0.0%, ambiguous 40.3%, external 31.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 549744 | 28.8% | 0.0% | 40.8% | 30.4% |
| python | 1852 | 24.2% | 0.0% | 1.0% | 74.8% |
| javascript | 1606 | 25.9% | 0.0% | 17.5% | 56.6% |
| c | 1406 | 0.7% | 0.4% | 1.6% | 97.3% |
| shell | 1102 | 17.2% | 6.4% | 1.2% | 75.2% |
| cpp | 1090 | 8.9% | 2.2% | 2.8% | 86.1% |
| typescript | 1051 | 31.2% | 0.0% | 6.5% | 62.3% |
| livecode | 14 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
