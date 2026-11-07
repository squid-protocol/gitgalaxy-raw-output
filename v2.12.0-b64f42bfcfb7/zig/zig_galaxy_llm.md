# ARCHITECTURAL_BRIEF: zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ziglang/zig.git` |
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
- **Scope:** 14749 analyzed artifact(s), 2236538 LOC.
- **Load-bearing artifact:** `lib/std/std.zig` -- 1514 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/compiler_rt.zig` -- pulls in 226 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/include/arm_neon.h` at magnitude 19082.56 (structural weight, not risk).
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
| Total Artifacts | 20538 |
| Analyzed Artifacts (Scanned) | 14749 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5789 |
| Total LOC | 2236538 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.8% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8758 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1192 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4202 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1367 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 8842 | 1311738 | 59.9% |
| ZIG | 2870 | 761818 | 19.5% |
| C | 2646 | 126404 | 17.9% |
| ASSEMBLY | 311 | 8354 | 2.1% |
| FORTRAN | 24 | 16701 | 0.2% |
| SHELL | 17 | 711 | 0.1% |
| PLAINTEXT | 13 | 0 | 0.1% |
| MARKDOWN | 6 | 0 | 0.0% |
| OBJECTIVE-C | 5 | 770 | 0.0% |
| PYTHON | 5 | 1187 | 0.0% |
| POWERSHELL | 3 | 251 | 0.0% |
| CSS | 2 | 280 | 0.0% |
| JSON | 2 | 12 | 0.0% |
| HTML | 1 | 7789 | 0.0% |
| JAVASCRIPT | 1 | 338 | 0.0% |
| MAKEFILE | 1 | 185 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 14747 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 50%, Data / Markup / Trivial 21%, Parameter Forwarders Files 9%, Large Core Modules (2) 4%, State Mutators Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14728 | 99.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 0.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5789*

**Composition by Extension & Reason:**
- `.def`: 2652x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1299x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Excluded (Machine-Generated Source Code Signature: 27 LOC), 14x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.c`: 743x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `no_extension`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 37x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.zig`: 83x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1095 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1151 LOC)
- `.cpp`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.input`: 44x Excluded (Unsupported Extension: '.input')
- `.zon`: 34x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Embedded Hex Payload: 4517 hex tokens in 2703 LOC), 1x Zero-Density Threshold (LOC: 203, Signals: 0)
- `.tar`: 35x Excluded (Explicitly Denied Extension: '.tar')
- `.s`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5331 LOC)
- `.in`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xz`: 24x Excluded (Explicitly Denied Extension: '.xz')
- `.x`: 23x Excluded (Unsupported Extension: '.x')
- `.ipp`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hpp`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.4 | 19.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 34.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.5 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 27994 | 1907 | 1 | `lib/std/os/linux.zig` |
| cleanup | 5283 | 537 | 0 | `lib/std/math/big/int_test.zig` |
| guards | 158497 | 4689 | 11 | `test/behavior/x86_64/cast.zig` |
| danger | 55727 | 4021 | 6 | `test/c_abi/main.zig` |
| concurrency | 2808 | 558 | 0 | `src/codegen/riscv64/CodeGen.zig` |
| connectivity | 54810 | 5554 | 4 | `lib/std/c.zig` |
| io | 3163 | 670 | 0 | `lib/libtsan/sanitizer_common/sanitizer_interceptors_ioctl_netbsd.inc` |
| crypto | 0 | 0 | 0 | - |
| ipc | 616 | 226 | 0 | `test/standalone/posix/sigaction.zig` |
| time | 364 | 103 | 0 | `lib/libc/include/any-windows-any/time.h` |
| serialization | 138 | 8 | 0 | `lib/libtsan/sanitizer_common/sanitizer_common_interceptors.inc` |
| regex | 82 | 38 | 0 | `lib/std/crypto/benchmark.zig` |
| events | 816 | 330 | 0 | `lib/libtsan/tsan_rtl.cpp` |
| tests | 11253 | 828 | 0 | `test/c_abi/main.zig` |
| docs | 73215 | 2257 | 1 | `lib/include/avx2intrin.h` |
| debt | 9224 | 1691 | 1 | `src/codegen/llvm.zig` |
| mutation | 289551 | 5589 | 23 | `lib/include/arm_neon.h` |
| dead_code | 8157 | 2863 | 1 | `lib/include/lasxintrin.h` |
| credential | 25 | 16 | 0 | `lib/std/crypto/scrypt.zig` |
| threat | 434 | 46 | 0 | `lib/std/crypto/siphash.zig` |
| ml_ai | 36169 | 1236 | 0 | `test/behavior/x86_64/cast.zig` |
| ui | 71 | 5 | 0 | `doc/langref.html.in` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/libtsan/sanitizer_common/sanitizer_interceptors_ioctl_netbsd.inc` (Hits: 413)
- `lib/libtsan/sanitizer_common/sanitizer_common_interceptors_ioctl.inc` (Hits: 114)
- `lib/libtsan/sanitizer_common/sanitizer_common_interceptors.inc` (Hits: 110)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **std.zig** (`lib/std/std.zig`) — 1514 inbound connections
2. **types.h** (`lib/libc/include/any-linux-any/linux/types.h`) — 676 inbound connections
3. **builtin.zig** (`lib/std/builtin.zig`) — 548 inbound connections
4. **syscall_ret.c** (`lib/libc/musl/src/internal/syscall_ret.c`) — 239 inbound connections
5. **common.zig** (`lib/compiler_rt/common.zig`) — 218 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compiler_rt.zig** (`lib/compiler_rt.zig`) — 226 outbound dependencies
2. **sanitizer_platform_limits_netbsd.cpp** (`lib/libtsan/sanitizer_common/sanitizer_platform_limits_netbsd.cpp`) — 201 outbound dependencies
3. **macos-headers.c** (`tools/macos-headers.c`) — 157 outbound dependencies
4. **behavior.zig** (`test/behavior.zig`) — 114 outbound dependencies
5. **immintrin.h** (`lib/include/immintrin.h`) — 110 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `body` **(Many-Argument Workhorses)** (@ `src/codegen/aarch64/Select.zig`) -> Impact: **2912.9** | LOC: 6642
- `main` **(Many-Argument Workhorses)** (@ `stage1/wasm2c.c`) -> Impact: **1191.9** | LOC: 2222
- `parseArgs` **(Many-Argument Workhorses)** (@ `lib/compiler/aro/aro/Driver.zig`) -> Impact: **806.5** | LOC: 567
  * *Intent:* ; /// Process command line arguments, returns true if something was written to std_out.
- `ArrayHashMapUnmanaged` **(Many-Argument Workhorses)** (@ `lib/std/array_hash_map.zig`) -> Impact: **575.1** | LOC: 1485
  * *Intent:* /// the (well defined) behavior when mixing insertions and deletions with iteration. /// /// This type does not store an `Allocator` field - the `Allo...
- `parse` **(Many-Argument Workhorses)** (@ `src/link/Wasm/Object.zig`) -> Impact: **568.4** | LOC: 1168
- `iconv` **(Many-Argument Workhorses)** (@ `lib/libc/musl/src/locale/iconv.c`) -> Impact: **552.2** | LOC: 463
- `printInstruction` **(Many-Argument Workhorses)** (@ `src/codegen/aarch64/Disassemble.zig`) -> Impact: **512.9** | LOC: 1338
- `GetInstructionSize` **(Many-Argument Workhorses)** (@ `lib/libtsan/interception/interception_win.cpp`) -> Impact: **508.5** | LOC: 435
  * *Intent:* #endif // Returns 0 on error.
- `toBitcode` **(Many-Argument Workhorses)** (@ `lib/std/zig/llvm/Builder.zig`) -> Impact: **461.9** | LOC: 1999
- `fromType` **(Many-Argument Workhorses)** (@ `src/codegen/c/Type.zig`) -> Impact: **400.7** | LOC: 1508

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/include` | 209 | 52233.16 | 2.05% | 5.77% |
| `lib/libc/include/any-windows-any` | 1161 | 44045.22 | 2.55% | 3.41% |
| `lib/std` | 69 | 34168.78 | 12.33% | 13.56% |
| `lib/compiler/aro/aro` | 28 | 21782.48 | 21.13% | 8.4% |
| `lib/libtsan/sanitizer_common` | 196 | 18172.51 | 24.35% | 34.61% |
| `src/link` | 17 | 15653.68 | 19.69% | 15.24% |
| `lib/std/zig` | 23 | 14100.78 | 10.86% | 9.19% |
| `lib/libc/include/any-darwin-any/simd` | 16 | 13778.24 | 9.8% | 1.41% |
| `src/codegen/aarch64` | 7 | 12636.76 | 9.76% | 4.47% |
| `lib/libc/musl/src/math` | 222 | 12438.24 | 39.44% | 26.68% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/libc/musl/src/linux/xattr.c` -> **100.0%** Exposure
- `lib/libc/musl/src/stdio/ext.c` -> **100.0%** Exposure
- `lib/libc/musl/src/thread/pthread_attr_get.c` -> **100.0%** Exposure
- `lib/include/arm_acle.h` -> **100.0%** Exposure
- `lib/include/lasxintrin.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/libc/freebsd/lib/csu/common/crtbegin.c` -> **100.0%** Exposure
- `lib/libc/freebsd/lib/csu/common/crtend.c` -> **100.0%** Exposure
- `lib/libc/musl/compat/time32/clock_adjtime32.c` -> **100.0%** Exposure
- `lib/libc/musl/ldso/dlstart.c` -> **100.0%** Exposure
- `lib/libc/musl/src/aio/aio.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/include/lasxintrin.h` -> **537** Orphaned Functions | **0** Duplicates
- `lib/include/lsxintrin.h` -> **519** Orphaned Functions | **0** Duplicates
- `lib/include/wasm_simd128.h` -> **272** Orphaned Functions | **0** Duplicates
- `lib/libc/include/any-windows-any/mi.h` -> **202** Orphaned Functions | **0** Duplicates
- `lib/std/c.zig` -> **0** Orphaned Functions | **145** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib/std/crypto/Certificate/Bundle.zig` -> **96.4741%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `25445` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/include/arm_neon.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.036)
- **Top Global Matches:** file_cluster_17: 5.036, file_cluster_2: 5.761, file_cluster_15: 7.162
- **Magnitude:** 19082.56 | **LOC:** 74048 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.174; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.3%), Dead Code Surface (formerly Dead Code) (6.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5242`, `args: 15570`
* *Risk/State:* `state_mutation: 17661`, `dead_code: 1`
* *Architecture:* `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.002356
  * `Imports (Out-Degree: 3):` arm_bf16.h, arm_vector_types.h, stdint.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/compiler/aro/aro/Parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.813)
- **Top Global Matches:** file_cluster_6: 7.813, file_cluster_8: 10.761, file_cluster_4: 15.243
- **Magnitude:** 7062.94 | **LOC:** 10665 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **19**; blast radius 0.127; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (48.9%), Guard Balance (formerly Safety Score) (35.5%), Complexity Load (formerly Cognitive Load) (26.0%)
- **Documentation Coverage:** 63.4783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `castType` **(Many-Argument Workhorses)** (Impact: 346.4)
  * `adjustTypes` **(Many-Argument Workhorses)** (Impact: 216.8)
    * *Intent:* /// Adjust types for binary operation, returns true if the result can and should be evaluated.
  * `coerceExtra` **(Many-Argument Workhorses)** (Impact: 166.5)
  * `unExpr` **(Defensive Guards)** (Impact: 163.8)
    * *Intent:* /// unExpr /// : (compoundLiteral | primaryExpr) suffixExpr* /// | '&&' IDENTIFIER /// | ('&' | '*' ...
  * `decl` **(Defensive Guards)** (Impact: 146.9)
    * *Intent:* // ====== declarations ====== /// decl /// : declSpec (initDeclarator ( ',' initDeclarator)*)? ';' /...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 523 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1652
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2284`, `structural_boundaries: 1369`, `args: 211`, `func_start: 211`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 606`, `dead_code: 2`, `planned_debt: 22`
* *Architecture:* `io: 1`, `api: 18`, `import: 19`
* *Defense:* `safety: 2341`, `doc: 262`, `test: 5`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.127
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.019449
  * `Imports (Out-Degree: 21):` Attribute.zig, Builtins.zig, eval.zig, Compilation.zig, Diagnostics.zig, InitList.zig, Diagnostic.zig, Preprocessor.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/codegen/aarch64/Select.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.059)
- **Top Global Matches:** file_cluster_6: 12.059, file_cluster_4: 14.74, file_cluster_8: 18.66
- **Magnitude:** 6662.26 | **LOC:** 12572 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.05; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.1%), Mutation Surface (formerly State Flux) (53.1%), Connectivity (formerly Api Exposure) (50.2%), Guard Balance (formerly Safety Score) (38.7%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `body` **(Many-Argument Workhorses)** (Impact: 2912.9)
  * `next` **(Many-Argument Workhorses)** (Impact: 243.7)
  * `finish` **(Many-Argument Workhorses)** (Impact: 237.4)
  * `layout` **(Many-Argument Workhorses)** (Impact: 188.0)
    * *Intent:* /// * SP to outgoing stack arguments/locals must only pass through [S] /// * entry/exit SP to prolog...
  * `addOrSubtract` **(Many-Argument Workhorses)** (Impact: 171.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2550`, `structural_boundaries: 1749`, `args: 132`, `func_start: 129`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 864`, `high_risk_execution: 1`, `state_mutation: 378`, `planned_debt: 1`
* *Architecture:* `api: 63`, `import: 8`
* *Defense:* `safety: 3034`, `doc: 134`, `sync_locks: 15`, `cleanup: 138`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.022726
  * `Imports (Out-Degree: 7):` Air.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/include/altivec.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.481)
- **Top Global Matches:** file_cluster_15: 7.481, file_cluster_17: 8.921, file_cluster_16: 8.954
- **Magnitude:** 6198.16 | **LOC:** 19365 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.7%), Guard Balance (formerly Safety Score) (50.5%), Debt Markers (formerly Tech Debt) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vec_addec` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* #ifdef __powerpc64__
  * `vec_addec` **(Many-Argument Workhorses)** (Impact: 5.0)
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* /* vec_first_match_or_eos_index */
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 4.4)
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 3189`, `args: 347`, `func_start: 2800`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 130`, `fragile_debt: 9`, `duplicate_logic: 4`
* *Architecture:* `api: 126`, `import: 1`
* *Defense:* `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.105
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.005041
  * `Imports (Out-Degree: 2):` stddef.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/std/zig/AstGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.994)
- **Top Global Matches:** file_cluster_6: 8.994, file_cluster_4: 9.487, file_cluster_12: 15.037
- **Magnitude:** 5766.5 | **LOC:** 14223 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.1%), Mutation Surface (formerly State Flux) (62.9%), Guard Balance (formerly Safety Score) (43.0%), Connectivity (formerly Api Exposure) (31.4%)
- **Documentation Coverage:** 74.6575% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `switchExpr` **(Many-Argument Workhorses)** (Impact: 232.9)
  * `switchExprErrUnion` **(Many-Argument Workhorses)** (Impact: 184.1)
  * `whileExpr` **(Many-Argument Workhorses)** (Impact: 183.8)
  * `forExpr` **(Many-Argument Workhorses)** (Impact: 137.1)
  * `varDecl` **(Many-Argument Workhorses)** (Impact: 136.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 243 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 888
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1447`, `structural_boundaries: 1556`, `args: 246`, `func_start: 241`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 353`, `state_mutation: 402`, `dead_code: 1`, `planned_debt: 9`
* *Architecture:* `api: 13`, `concurrency: 16`, `import: 3`
* *Defense:* `safety: 1797`, `doc: 302`, `test: 7`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.036642
  * `Imports (Out-Degree: 3):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/codegen/llvm.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.41)
- **Top Global Matches:** file_cluster_4: 8.41, file_cluster_6: 9.865, file_cluster_12: 13.434
- **Magnitude:** 5401.18 | **LOC:** 13385 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 0.07; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.4%), Debt Markers (formerly Tech Debt) (75.0%), Mutation Surface (formerly State Flux) (70.1%), Connectivity (formerly Api Exposure) (42.7%)
- **Documentation Coverage:** 87.7256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lowerDebugType` **(Many-Argument Workhorses)** (Impact: 228.7)
  * `updateFunc` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `lowerValue` **(Many-Argument Workhorses)** (Impact: 174.2)
  * `airAssembly` **(Many-Argument Workhorses)** (Impact: 155.3)
  * `emit` **(Many-Argument Workhorses)** (Impact: 122.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 27 instances
* *Amplified Cascading Flux:* 259 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 923
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1596`, `structural_boundaries: 1211`, `args: 264`, `func_start: 257`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 287`, `high_risk_execution: 11`, `state_mutation: 405`, `dead_code: 4`, `planned_debt: 811`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 23`, `import: 21`
* *Defense:* `safety: 2472`, `doc: 146`, `cleanup: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.07
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.023145
  * `Imports (Out-Degree: 22):` Air.zig, Compilation.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/std/zig/llvm/Builder.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 12.956)
- **Top Global Matches:** file_cluster_12: 12.956, file_cluster_5: 13.626, file_cluster_7: 14.681
- **Magnitude:** 5212.64 | **LOC:** 15173 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 0.057; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.6%), Guard Balance (formerly Safety Score) (52.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.3%), Debt Markers (formerly Tech Debt) (26.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toBitcode` **(Many-Argument Workhorses)** (Impact: 461.9)
  * `print` **(Many-Argument Workhorses)** (Impact: 225.0)
  * `format` **(Defensive Guards)** (Impact: 77.8)
  * `finish` **(Many-Argument Workhorses)** (Impact: 68.8)
  * `format` **(Many-Argument Workhorses)** (Impact: 68.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 120 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 998`, `structural_boundaries: 1048`, `args: 643`, `func_start: 635`, `class_start: 238`
* *Risk/State:* `safety_bypasses: 622`, `high_risk_execution: 3`, `state_mutation: 219`, `planned_debt: 115`, `duplicate_logic: 32`
* *Architecture:* `io: 3`, `api: 733`, `import: 4`
* *Defense:* `safety: 1162`, `cleanup: 87`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.027894
  * `Imports (Out-Degree: 7):` std.zig, bitcode_writer.zig, builtin, ir.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/std/c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 11.623)
- **Top Global Matches:** file_cluster_15: 11.623, file_cluster_12: 12.49, file_cluster_16: 12.592
- **Magnitude:** 5181.82 | **LOC:** 11591 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.887; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.5%)
- **Documentation Coverage:** 96.5116% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `versionCheck` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* /// * If not linking libc, returns `false`. /// * If linking musl libc, returns `true`. /// * If lin...
  * `recvfrom` **(Many-Argument Workhorses)** (Impact: 8.3)
  * `recv` **(State Mutators)** (Impact: 7.0)
  * `getdents` **(State Mutators)** (Impact: 6.2)
  * `errno` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* /// Get the errno if rc is -1 and SUCCESS if rc is not -1.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 531`, `structural_boundaries: 199`, `args: 538`, `func_start: 513`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 34`, `duplicate_logic: 145`
* *Architecture:* `io: 21`, `api: 4056`, `import: 10`
* *Defense:* `safety: 13`, `doc: 1034`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.887
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.054085
  * `Imports (Out-Degree: 10):` builtin, darwin.zig, dragonfly.zig, freebsd.zig, haiku.zig, illumos.zig, netbsd.zig, openbsd.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/AvailabilityInternalLegacy.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 5.876)
- **Top Global Matches:** file_cluster_17: 5.876, file_cluster_2: 6.924, file_cluster_15: 8.839
- **Magnitude:** 5028.04 | **LOC:** 4347 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 0.645; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 4927`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.645
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009613
  * `Imports (Out-Degree: 0):` AvailabilityInternal.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/codegen/aarch64/encoding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.217)
- **Top Global Matches:** file_cluster_12: 10.217, file_cluster_4: 11.603, file_cluster_15: 12.219
- **Magnitude:** 4570.26 | **LOC:** 16598 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.054; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Debt Markers (formerly Tech Debt) (12.9%)
- **Documentation Coverage:** 46.6187% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode` **(Compute Cores)** (Impact: 232.3)
  * `parse` **(Defensive Guards)** (Impact: 62.5)
  * `fmov` **(Many-Argument Workhorses)** (Impact: 51.8)
    * *Intent:* /// C7.2.129 FMOV (vector, immediate) /// C7.2.130 FMOV (register) /// C7.2.131 FMOV (general) /// C...
  * `ldr` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* /// C6.2.166 LDR (immediate) /// C6.2.167 LDR (literal) /// C6.2.168 LDR (register) /// C7.2.191 LDR...
  * `decode` **(Compute Cores)** (Impact: 48.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1101`, `structural_boundaries: 868`, `args: 347`, `func_start: 347`, `class_start: 695`
* *Risk/State:* `safety_bypasses: 418`, `state_mutation: 1`, `duplicate_logic: 35`
* *Architecture:* `api: 1538`, `import: 2`
* *Defense:* `safety: 370`, `doc: 960`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.019072
  * `Imports (Out-Degree: 3):` aarch64.zig, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/std/os/linux.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_12: 7.664, file_cluster_7: 9.02, file_cluster_5: 9.96
- **Magnitude:** 3930.3 | **LOC:** 9979 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.114; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (97.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.4%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sigaction` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `fadvise` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `copy_file_range` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `pread` **(Type Conversions)** (Impact: 17.6)
  * `pwrite` **(Type Conversions)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 391`, `args: 286`, `func_start: 280`, `class_start: 250`
* *Risk/State:* `safety_bypasses: 312`, `high_risk_execution: 1`, `state_mutation: 59`, `planned_debt: 8`
* *Architecture:* `io: 15`, `api: 2659`, `concurrency: 3`, `import: 32`
* *Defense:* `safety: 15`, `doc: 1083`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.114
  * `Choke Point (Betweenness):` 0.000169 | `Ripple Effect (Closeness):` 0.036642
  * `Imports (Out-Degree: 31):` dynamic_library.zig, std.zig, builtin, IoUring.zig, aarch64.zig, arm.zig, bpf.zig, hexagon.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/include/vecintrin.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 23.545)
- **Top Global Matches:** file_cluster_15: 23.545, file_cluster_16: 23.903, file_cluster_12: 24.338
- **Magnitude:** 3882.84 | **LOC:** 12869 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.038; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%), Connectivity (formerly Api Exposure) (50.0%), Debt Markers (formerly Tech Debt) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `t` **(Compute Cores)** (Impact: 25.0)
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 3533`, `args: 135`, `func_start: 1763`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `duplicate_logic: 10`
* *Architecture:* `api: 63`
* *Defense:* `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 6.8e-05
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/codegen/riscv64/CodeGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.925)
- **Top Global Matches:** file_cluster_4: 9.925, file_cluster_12: 10.845, file_cluster_7: 12.914
- **Magnitude:** 3467.42 | **LOC:** 8501 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.058; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.7%), Connectivity (formerly Api Exposure) (41.3%), Guard Balance (formerly Safety Score) (39.7%), Debt Markers (formerly Tech Debt) (26.6%)
- **Documentation Coverage:** 92.0635% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `airAsm` **(Many-Argument Workhorses)** (Impact: 287.3)
  * `genBinOp` **(Many-Argument Workhorses)** (Impact: 228.3)
    * *Intent:* /// Does the same thing as binOp however is meant to be used internally to the backend. /// /// The ...
  * `airAtomicRmw` **(Defensive Guards)** (Impact: 97.1)
  * `genSetReg` **(Many-Argument Workhorses)** (Impact: 90.8)
    * *Intent:* /// Sets the value of `src_mcv` into `reg`. Assumes you have a lock on it.
  * `genCall` **(Many-Argument Workhorses)** (Impact: 83.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 60 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1163`, `structural_boundaries: 861`, `args: 235`, `func_start: 234`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 256`, `high_risk_execution: 14`, `state_mutation: 98`, `planned_debt: 203`, `fragile_debt: 3`
* *Architecture:* `api: 13`, `import: 21`
* *Defense:* `safety: 1242`, `doc: 74`, `sync_locks: 110`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.02288
  * `Imports (Out-Degree: 19):` Air.zig, Compilation.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/libc/musl/src/regex/regcomp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.914)
- **Top Global Matches:** file_cluster_8: 5.914, file_cluster_6: 16.766, file_cluster_3: 19.889
- **Magnitude:** 3413.18 | **LOC:** 2954 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tre_add_tags` **(Many-Argument Workhorses)** (Impact: 202.3)
    * *Intent:* /* Adds tags to appropriate locations in the parse tree in `tree', so that subexpressions marked for...
  * `tre_expand_ast` **(Many-Argument Workhorses)** (Impact: 117.0)
    * *Intent:* /* Expands each iteration node that has a finite nonzero minimum or maximum iteration count to a cat...
  * `parse_atom` **(Many-Argument Workhorses)** (Impact: 113.3)
    * *Intent:* */
  * `tre_parse` **(Compute Cores)** (Impact: 102.5)
  * `tre_compute_nfl` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* /* Computes and fills in the fields `nullable', `firstpos', and `lastpos' for the nodes of the AST `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 646 instances
* *State Mutation (weighted view):* 1986
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 563`, `structural_boundaries: 276`, `args: 58`, `func_start: 36`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 694`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 8`
* *Defense:* `safety: 20`, `doc: 5`, `test: 11`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` assert.h, ctype.h, limits.h, regex.h, stdint.h, stdlib.h, string.h, tre.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/codegen/c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.382)
- **Top Global Matches:** file_cluster_4: 8.382, file_cluster_12: 10.571, file_cluster_15: 12.393
- **Magnitude:** 3409.44 | **LOC:** 8433 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 0.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.6%), Connectivity (formerly Api Exposure) (61.3%), Mutation Surface (formerly State Flux) (21.5%), Guard Balance (formerly Safety Score) (20.5%)
- **Documentation Coverage:** 95.4198% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderValue` **(Many-Argument Workhorses)** (Impact: 277.9)
  * `renderUndefValue` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `airAsm` **(Defensive Guards)** (Impact: 117.0)
  * `airCall` **(Defensive Guards)** (Impact: 88.0)
  * `airReduce` **(Defensive Guards)** (Impact: 74.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 60 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1073`, `structural_boundaries: 577`, `args: 234`, `func_start: 229`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 2`, `state_mutation: 83`, `dead_code: 5`, `planned_debt: 39`, `fragile_debt: 4`
* *Architecture:* `api: 65`, `import: 14`
* *Defense:* `safety: 2841`, `doc: 94`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.022899
  * `Imports (Out-Degree: 13):` Air.zig, Compilation.zig, InternPool.zig, Module.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/simd/matrix.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.533)
- **Top Global Matches:** file_cluster_15: 6.533, file_cluster_11: 7.864, file_cluster_17: 8.254
- **Magnitude:** 3299.46 | **LOC:** 2866 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.034; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%), Guard Balance (formerly Safety Score) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simd_mul` **(Compute Cores)** (Impact: 3.5)
  * `simd_mul` **(Compute Cores)** (Impact: 3.5)
  * `simd_mul` **(Compute Cores)** (Impact: 3.5)
  * `simd_mul` **(Compute Cores)** (Impact: 3.5)
  * `simd_mul` **(Compute Cores)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 1003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 1147`, `args: 110`, `func_start: 1137`
* *Risk/State:* `state_mutation: 679`
* *Architecture:* `import: 5`
* *Defense:* `immutability_locks: 936`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 9e-05
  * `Imports (Out-Degree: 6):` base.h, extern.h, geometry.h, logic.h, matrix_types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-windows-any/strsafe.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.643)
- **Top Global Matches:** file_cluster_6: 6.643, file_cluster_4: 8.711, file_cluster_15: 16.084
- **Magnitude:** 3158.82 | **LOC:** 1931 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.036; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `StringCopyNExWorkerA` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `StringCopyNExWorkerW` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `StringCatNExWorkerA` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `StringCatNExWorkerW` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `StringVPrintfExWorkerA` **(Many-Argument Workhorses)** (Impact: 102.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 429 instances
* *State Mutation (weighted view):* 1287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 576`, `structural_boundaries: 131`, `args: 287`, `func_start: 84`
* *Risk/State:* `state_mutation: 429`
* *Architecture:* `import: 5`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000217
  * `Imports (Out-Degree: 8):` _mingw_unicode.h, specstrings.h, stdarg.h, stdio.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/include/avx512vlintrin.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.585)
- **Top Global Matches:** file_cluster_12: 7.585, file_cluster_15: 7.696, file_cluster_17: 8.199
- **Magnitude:** 3104.8 | **LOC:** 8438 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); blast radius 0.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm_mask_fmadd_pd` **(Parameter Forwarders)** (Impact: 2.7)
  * `_mm_mask3_fmadd_pd` **(Parameter Forwarders)** (Impact: 2.7)
  * `_mm_maskz_fmadd_pd` **(Parameter Forwarders)** (Impact: 2.7)
  * `_mm_mask_fmsub_pd` **(Parameter Forwarders)** (Impact: 2.7)
  * `_mm_maskz_fmsub_pd` **(Parameter Forwarders)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1103`, `args: 234`, `func_start: 918`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 4`
* *Architecture:* `api: 845`
* *Defense:* `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000548
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/std/Io/Threaded.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 11.06)
- **Top Global Matches:** file_cluster_12: 11.06, file_cluster_7: 11.424, file_cluster_4: 11.574
- **Magnitude:** 3077.74 | **LOC:** 6260 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 38.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.09; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (71.6%), Mutation Surface (formerly State Flux) (66.3%), Connectivity (formerly Api Exposure) (45.1%)
- **Documentation Coverage:** 91.453% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `netLookupFallible` **(Many-Argument Workhorses)** (Impact: 112.5)
  * `lookupDns` **(Many-Argument Workhorses)** (Impact: 104.9)
  * `netReceivePosix` **(Many-Argument Workhorses)** (Impact: 72.6)
  * `dirOpenFilePosix` **(Many-Argument Workhorses)** (Impact: 64.6)
  * `dirCreateFilePosix` **(Many-Argument Workhorses)** (Impact: 59.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 122 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 118
* *State Mutation (weighted view):* 416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 914`, `structural_boundaries: 1613`, `args: 191`, `func_start: 188`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 440`, `high_risk_execution: 25`, `state_mutation: 172`, `planned_debt: 47`, `fragile_debt: 9`
* *Architecture:* `io: 49`, `api: 31`, `concurrency: 53`, `import: 3`
* *Defense:* `safety: 628`, `doc: 84`, `sync_locks: 48`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.09
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.036642
  * `Imports (Out-Degree: 5):` std.zig, test.zig, builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/simd/vector_make.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 13.771)
- **Top Global Matches:** file_cluster_15: 13.771, file_cluster_0: 13.891, file_cluster_16: 14.513
- **Magnitude:** 2984.62 | **LOC:** 8760 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 0.185; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (49.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make` **(Compute Cores)** (Impact: 179.0)
    * *Intent:* #if __has_feature(cxx_constexpr) /*! @abstract Templated make function based on return type and argu...
  * `make_undef` **(Compute Cores)** (Impact: 179.0)
    * *Intent:* /*! @abstract Templated make_undef function based on return type and * argument type. */...
  * `simd_make_char4` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* /*! @abstract Concatenates `x`, `y`, `z` and `w` to form a vector of four * 8-bit signed (twos-compl...
  * `simd_make_uchar4` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* /*! @abstract Concatenates `x`, `y`, `z` and `w` to form a vector of four * 8-bit unsigned integers....
  * `simd_make_short4` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* /*! @abstract Concatenates `x`, `y`, `z` and `w` to form a vector of four * 16-bit signed (twos-comp...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 2863`, `args: 328`, `func_start: 996`, `class_start: 142`
* *Risk/State:* `state_mutation: 748`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 194`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003033
  * `Imports (Out-Degree: 2):` packed.h, vector_types.h, stddef.h, tuple
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/codegen/wasm/CodeGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.982)
- **Top Global Matches:** file_cluster_4: 11.982, file_cluster_12: 12.296, file_cluster_7: 13.17
- **Magnitude:** 2961.8 | **LOC:** 7584 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 0.038; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.7%), Connectivity (formerly Api Exposure) (41.3%), Guard Balance (formerly Safety Score) (36.4%), Debt Markers (formerly Tech Debt) (19.2%)
- **Documentation Coverage:** 69.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildOpcode` **(Compute Cores)** (Impact: 225.0)
    * *Intent:* /// TODO: deprecated, should be split up per tag.
  * `airAtomicRmw` **(Defensive Guards)** (Impact: 69.3)
  * `airSwitchBr` **(Defensive Guards)** (Impact: 66.3)
  * `airCall` **(Defensive Guards)** (Impact: 61.1)
  * `memcpy` **(Many-Argument Workhorses)** (Impact: 56.7)
    * *Intent:* /// Performs a copy of bytes for a given type. Copying all bytes /// from rhs to lhs.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1075`, `structural_boundaries: 1112`, `args: 204`, `func_start: 203`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 426`, `high_risk_execution: 1`, `state_mutation: 46`, `dead_code: 5`, `planned_debt: 133`
* *Architecture:* `api: 12`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 1545`, `doc: 219`, `test: 1`, `cleanup: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.022863
  * `Imports (Out-Degree: 11):` Air.zig, Compilation.zig, InternPool.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig, abi.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/link/Dwarf.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.564)
- **Top Global Matches:** file_cluster_4: 10.564, file_cluster_12: 11.457, file_cluster_5: 12.157
- **Magnitude:** 2934.78 | **LOC:** 6450 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 0.062; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (64.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.7%), Mutation Surface (formerly State Flux) (45.7%), Guard Balance (formerly Safety Score) (40.0%)
- **Documentation Coverage:** 98.5507% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateComptimeNavInner` **(Many-Argument Workhorses)** (Impact: 226.4)
  * `updateLazyType` **(Many-Argument Workhorses)** (Impact: 209.3)
  * `updateContainerTypeWriterError` **(Many-Argument Workhorses)** (Impact: 178.8)
  * `updateLazyValue` **(Many-Argument Workhorses)** (Impact: 172.8)
  * `initWipNavInner` **(Many-Argument Workhorses)** (Impact: 116.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 916`, `structural_boundaries: 446`, `args: 162`, `func_start: 162`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 374`, `high_risk_execution: 2`, `state_mutation: 161`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 52`, `import: 15`
* *Defense:* `safety: 1360`, `doc: 10`, `cleanup: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.062
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.022963
  * `Imports (Out-Degree: 11):` InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig, bits.zig, dev.zig...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/std/posix.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.438)
- **Top Global Matches:** file_cluster_7: 9.438, file_cluster_12: 10.128, file_cluster_5: 11.034
- **Magnitude:** 2854.5 | **LOC:** 6673 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.887; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.6%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ptrace` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `dl_iterate_phdr` **(Defensive Guards)** (Impact: 39.5)
  * `copy_file_range` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* /// /// If `fd_in` and `fd_out` are the same, source and target ranges must not overlap. /// The fil...
  * `fchmodat2` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `setSockFlags` **(Defensive Guards)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1022`, `structural_boundaries: 2186`, `args: 204`, `func_start: 204`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 591`, `high_risk_execution: 2`, `state_mutation: 14`, `planned_debt: 14`, `fragile_debt: 6`
* *Architecture:* `io: 35`, `api: 460`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 338`, `doc: 874`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.887
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.054085
  * `Imports (Out-Degree: 6):` builtin, dynamic_library.zig, test.zig, root, std.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/include/avx512fintrin.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.061)
- **Top Global Matches:** file_cluster_15: 7.061, file_cluster_17: 7.561, file_cluster_12: 8.142
- **Magnitude:** 2746.46 | **LOC:** 9788 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); blast radius 0.435; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Mutation Surface (formerly State Flux) (8.5%)
- **Documentation Coverage:** 99.0753% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mm512_set_epi8` **(Many-Argument Workhorses)** (Impact: 9.2)
  * `_mm512_set_epi16` **(Many-Argument Workhorses)** (Impact: 6.4)
  * `_mm512_set_epi32` **(Many-Argument Workhorses)** (Impact: 4.6)
  * `_mm512_set_ps` **(Many-Argument Workhorses)** (Impact: 4.6)
  * `_mm512_set_epi64` **(Parameter Forwarders)** (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 997`, `args: 575`, `func_start: 838`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 53`
* *Architecture:* `api: 676`
* *Defense:* `doc: 222`, `immutability_locks: 97`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.435
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003768
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/link/MachO.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.094)
- **Top Global Matches:** file_cluster_12: 8.094, file_cluster_4: 9.268, file_cluster_15: 10.661
- **Magnitude:** 2727.52 | **LOC:** 5436 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **37**; blast radius 0.391; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (97.3%), Mutation Surface (formerly State Flux) (91.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.1%), Guard Balance (formerly Safety Score) (40.9%)
- **Documentation Coverage:** 94.6237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flush` **(Many-Argument Workhorses)** (Impact: 159.6)
  * `dumpArgv` **(Defensive Guards)** (Impact: 106.9)
    * *Intent:* /// --verbose-link output
  * `parseDependentDylibs` **(Defensive Guards)** (Impact: 64.7)
  * `initSyntheticSections` **(Defensive Guards)** (Impact: 46.2)
  * `calcSectionSizes` **(Defensive Guards)** (Impact: 38.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 143 instances
* *High Risk Execution (weighted view):* 4
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 580`, `args: 231`, `func_start: 231`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 126`, `high_risk_execution: 6`, `state_mutation: 244`, `dead_code: 3`, `planned_debt: 43`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 162`, `concurrency: 5`, `import: 37`
* *Defense:* `safety: 865`, `doc: 183`, `sync_locks: 2`, `cleanup: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.391
  * `Choke Point (Betweenness):` 0.001173 | `Ripple Effect (Closeness):` 0.03724
  * `Imports (Out-Degree: 37):` Compilation.zig, InternPool.zig, Value.zig, Zcu.zig, codegen.zig, dev.zig, link.zig, target.zig...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/behavior/wrapping_arithmetic.zig` (ZIG) | Magnitude: 17.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 88, safety: 57, core_var_decl: 11, structural_boundaries: 10
- `doc/langref/test_structs.zig` (ZIG) | Magnitude: 15.0 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 16, scientific: 11, safety: 9
- `test/cases/compile_errors/packed_struct_with_fields_of_not_allowed_types.zig` (ZIG) | Magnitude: 32.46 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, core_var_decl: 17, design_short_vars: 17, args: 16
- `test/behavior/generics.zig` (ZIG) | Magnitude: 190.68 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 425, structural_boundaries: 102, core_var_decl: 93, args: 74
- `lib/std/std.zig` (ZIG) | Magnitude: 99.18 | Delta: **0.193** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: core_var_decl: 106, api: 95, globals: 95, import: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/libc/musl/arch/powerpc/pthread_arch.h` (CPP) | Magnitude: 2.52 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: reflection_metaprogramming: 5, macros: 5, indent_tabs: 3, structural_boundaries: 2
- `lib/libc/musl/arch/powerpc64/pthread_arch.h` (CPP) | Magnitude: 2.52 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: reflection_metaprogramming: 5, macros: 5, indent_tabs: 3, structural_boundaries: 2
- `lib/libc/musl/src/thread/m68k/syscall_cp.s` (ASSEMBLY) | Magnitude: 10.12 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 11, func_start: 4, api: 4, branch: 1
- `lib/libc/include/generic-netbsd/sparc/mcontext.h` (CPP) | Magnitude: 4.84 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 50, reflection_metaprogramming: 39, indent_tabs: 34, structural_boundaries: 23
- `lib/libc/include/sparc-netbsd-none/machine/mcontext.h` (CPP) | Magnitude: 4.84 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 50, reflection_metaprogramming: 39, indent_tabs: 34, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `lib/libc/include/generic-freebsd/sys/bufobj.h` (CPP) | Magnitude: 16.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 41, pointers: 27, macros: 20, args: 19
- `src/link/Elf/ZigObject.zig` (ZIG) | Magnitude: 1606.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1928, core_var_decl: 484, design_snake_case: 443, branch: 379
- `lib/libc/include/generic-netbsd/net/npf.h` (CPP) | Magnitude: 7.2 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 94, reflection_metaprogramming: 86, indent_tabs: 61, structural_boundaries: 50
- `lib/libc/musl/src/stdio/fputws.c` (C) | Magnitude: 24.54 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 15, pointers: 10, structural_boundaries: 6, state_mutation: 5
- `test/standalone/child_process/child.zig` (ZIG) | Magnitude: 22.3 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, core_var_decl: 16, design_snake_case: 14, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `lib/compiler_rt/popcountdi2_test.zig` (ZIG) | Magnitude: 8.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, explicit_casts: 15, core_var_decl: 11, design_snake_case: 10
- `lib/compiler_rt/popcountsi2_test.zig` (ZIG) | Magnitude: 8.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, explicit_casts: 15, core_var_decl: 11, design_snake_case: 10
- `lib/compiler_rt/popcountti2_test.zig` (ZIG) | Magnitude: 8.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, explicit_casts: 15, core_var_decl: 11, design_snake_case: 10
- `lib/libc/include/generic-freebsd/sys/systm.h` (CPP) | Magnitude: 39.38 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 257, pointers: 198, args: 167, macros: 97
- `lib/std/crypto/test.zig` (ZIG) | Magnitude: 0.12 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, safety: 3, safety_bypasses: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/include/avx512ifmavlintrin.h` (CPP) | Magnitude: 30.48 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 38, macros: 12, structural_boundaries: 8, func_start: 8
- `lib/libtsan/tsan_interface_atomic.cpp` (CPP) | Magnitude: 475.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 410, structural_boundaries: 254, pointers: 245, func_start: 136
- `lib/libc/musl/src/signal/sigfillset.c` (C) | Magnitude: 24.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 9, pointers: 7, state_mutation: 6, macros: 3
- `lib/libc/musl/src/network/herror.c` (C) | Magnitude: 5.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: branch: 2, import: 2, structural_boundaries: 1, args: 1
- `lib/libc/musl/src/math/x32/expl.s` (ASSEMBLY) | Magnitude: 11.3 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 64, structural_boundaries: 14, scientific: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `lib/libc/musl/src/misc/setrlimit.c` (C) | Magnitude: 28.12 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 12, pointers: 12, branch: 5
- `lib/libc/musl/src/network/res_state.c` (C) | Magnitude: 2.32 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, pointers: 2, indent_tabs: 2, func_start: 1
- `lib/libc/include/riscv64-freebsd-none/machine/tls.h` (C) | Magnitude: 5.48 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, macros: 5, indent_tabs: 4, args: 2
- `lib/libc/musl/src/math/log.c` (C) | Magnitude: 83.16 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 51, state_mutation: 30, core_var_decl: 28, design_snake_case: 28
- `lib/libc/musl/src/passwd/getpwent_a.c` (C) | Magnitude: 121.1 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 37, state_mutation: 29, pointers: 26, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `lib/libc/include/powerpc-linux-any/asm/stat.h` (C) | Magnitude: 19.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 51, macros: 7, structural_boundaries: 3, class_start: 3
- `lib/libc/include/any-windows-any/tcguid.h` (CPP) | Magnitude: 15.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 16, indent_spaces: 16, macros: 2, doc: 1
- `lib/libc/musl/src/stdio/rename.c` (C) | Magnitude: 3.46 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: args: 6, macros: 4, structural_boundaries: 3, import: 3
- `lib/libc/include/powerpc-linux-musl/bits/shm.h` (CPP) | Magnitude: 15.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 4, class_start: 4, reflection_metaprogramming: 1
- `lib/libc/musl/arch/powerpc/bits/shm.h` (CPP) | Magnitude: 15.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 4, class_start: 4, reflection_metaprogramming: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib/libc/include/any-windows-any/tabflicks.h` (CPP) | Magnitude: 21.2 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 23, design_upper_case: 23, structural_boundaries: 14
- `lib/libc/include/any-windows-any/casetup.h` (CPP) | Magnitude: 17.94 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 32, core_var_decl: 32, design_upper_case: 32, design_long_vars: 28
- `lib/libc/include/any-windows-any/bdatypes.h` (CPP) | Magnitude: 41.66 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 455, structural_boundaries: 207, core_var_decl: 133, design_upper_case: 124
- `lib/libc/include/generic-glibc/bits/math-vector.h` (CPP) | Magnitude: 12.6 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 1, macros: 1
- `test/stack_traces.zig` (ZIG) | Magnitude: 22.26 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 216, args: 26, structural_boundaries: 13, bitwise_ops: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib/std/Progress.zig` (ZIG) | Magnitude: 955.4 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1059, core_var_decl: 239, branch: 230, design_snake_case: 203
- `src/link/SpirV/BinaryModule.zig` (ZIG) | Magnitude: 270.92 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 326, core_var_decl: 73, design_snake_case: 61, structural_boundaries: 58
- `src/codegen/spirv/CodeGen.zig` (ZIG) | Magnitude: 1959.96 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 4379, core_var_decl: 1436, design_snake_case: 1320, safety: 1213
- `src/link/Elf/SharedObject.zig` (ZIG) | Magnitude: 338.38 | Delta: **0.174** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 386, core_var_decl: 113, design_snake_case: 100, structural_boundaries: 94

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `lib/std/math/cosh.zig` (ZIG) | Magnitude: 24.48 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 73, scientific: 34, safety: 28, core_var_decl: 21
- `lib/compiler_rt/fmax.zig` (ZIG) | Magnitude: 46.88 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, scientific: 25, structural_boundaries: 14, api: 14
- `lib/compiler_rt/fmin.zig` (ZIG) | Magnitude: 46.88 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, scientific: 25, structural_boundaries: 14, api: 14
- `src/libs/mingw/implib.zig` (ZIG) | Magnitude: 359.7 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 857, safety: 190, structural_boundaries: 133, core_var_decl: 118
- `lib/std/zig/c_translation/builtins.zig` (ZIG) | Magnitude: 183.5 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 99, scientific: 78, structural_boundaries: 59, args: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `lib/std/zip.zig` (ZIG) | Magnitude: 336.22 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 508, structural_boundaries: 106, branch: 105, core_var_decl: 96
- `src/zig_llvm.cpp` (CPP) | Magnitude: 408.44 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 324, pointers: 87, branch: 79, state_mutation: 61
- `src/codegen/wasm/Emit.zig` (ZIG) | Magnitude: 218.1 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 898, panics_and_aborts: 248, high_risk_execution: 239, planned_debt: 239

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `lib/compiler_rt/float_from_int_test.zig` (ZIG) | Magnitude: 83.64 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 638, safety: 579, explicit_casts: 110, core_var_decl: 53
- `lib/libc/include/wasm-wasi-musl/bits/alltypes.h` (CPP) | Magnitude: 22.1 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 266, args: 170, structural_boundaries: 104, reflection_metaprogramming: 92
- `lib/libc/include/any-darwin-any/_stdio.h` (CPP) | Magnitude: 32.06 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: macros: 100, pointers: 88, args: 84, reflection_metaprogramming: 50
- `lib/libc/include/generic-netbsd/netinet/tcp_debug.h` (CPP) | Magnitude: 15.78 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 16, macros: 14, structural_boundaries: 9, reflection_metaprogramming: 7
- `lib/libc/include/generic-netbsd/sparc64/z8530var.h` (CPP) | Magnitude: 15.7 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 16, pointers: 12, macros: 11, indent_tabs: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib/libc/musl/src/env/unsetenv.c` (C) | Magnitude: 37.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 17, branch: 10, pointers: 10, state_mutation: 6
- `lib/libc/musl/src/math/sincosl.c` (C) | Magnitude: 82.92 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 45, pointers: 22, scientific: 20, state_mutation: 19
- `lib/libc/musl/src/process/execvp.c` (C) | Magnitude: 80.14 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 39, branch: 14, state_mutation: 14, structural_boundaries: 10
- `lib/libtsan/sanitizer_common/sanitizer_procmaps_solaris.cpp` (CPP) | Magnitude: 65.52 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, pointers: 36, state_mutation: 16, branch: 13
- `lib/libc/musl/src/passwd/getgrent_a.c` (C) | Magnitude: 161.62 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 52, state_mutation: 37, pointers: 35, branch: 15

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/codegen/llvm.zig` -> Churn: **84.39%** | Cog Load: 17.9967% | Debt: 74.956%
- `lib/std/c.zig` -> Churn: **72.46%** | Cog Load: 3.2212% | Debt: 76.9284%
- `lib/compiler/build_runner.zig` -> Churn: **60.85%** | Cog Load: 57.7016% | Debt: 8.6443%
- `lib/std/crypto/blake3.zig` -> Churn: **54.66%** | Cog Load: 74.2324% | Debt: 0.0%
- `src/codegen/sparc64/CodeGen.zig` -> Churn: **54.66%** | Cog Load: 8.2962% | Debt: 76.6347%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/compiler/aro/aro/Parser.zig` -> **Veikka Tuominen** (100.0% isolated ownership) | Magnitude: 7062.94
- `lib/libc/include/any-darwin-any/AvailabilityInternalLegacy.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 5028.04
- `lib/libc/include/any-darwin-any/simd/matrix.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 3299.46
- `lib/libc/include/any-darwin-any/simd/vector_make.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 2984.62
- `lib/std/math/big/int.zig` -> **Justus Klausecker** (100.0% isolated ownership) | Magnitude: 2509.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/link/MachO.zig` -> **Severity: 0.107** (Bridge: 0.0012 * Flux: 91.3539%)
- `lib/libtsan/tsan_rtl.cpp` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 99.9895%)
- `lib/libtsan/sanitizer_common/sanitizer_linux.cpp` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 92.5502%)
- `lib/libtsan/tsan_interceptors_posix.cpp` -> **Severity: 0.038** (Bridge: 0.0006 * Flux: 66.953%)
- `lib/libtsan/sanitizer_common/sanitizer_symbolizer_libcdep.cpp` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 99.9984%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/std/Random.zig` -> **Severity: 4.327** (Embedded: 0.0541 * Error Risk: 80.0%)
- `lib/std/leb128.zig` -> **Severity: 4.327** (Embedded: 0.0541 * Error Risk: 80.0%)
- `lib/std/os.zig` -> **Severity: 4.327** (Embedded: 0.0541 * Error Risk: 80.0%)
- `lib/std/posix.zig` -> **Severity: 4.327** (Embedded: 0.0541 * Error Risk: 80.0%)
- `lib/std/Thread.zig` -> **Severity: 3.889** (Embedded: 0.0541 * Error Risk: 71.9122%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/std/builtin.zig` -> **Severity: 738.866** (Blast Radius: 22.166 * Doc Risk: 33.3333%)
- `lib/libc/musl/src/internal/syscall.h` -> **Severity: 576.9** (Blast Radius: 5.769 * Doc Risk: 100.0%)
- `lib/libc/include/generic-netbsd/sys/cdefs.h` -> **Severity: 521.2** (Blast Radius: 5.212 * Doc Risk: 100.0%)
- `lib/std/Target.zig` -> **Severity: 482.52** (Blast Radius: 7.031 * Doc Risk: 68.6275%)
- `lib/libc/include/any-windows-any/_mingw.h` -> **Severity: 441.9** (Blast Radius: 4.419 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 783 literal sites + 44 sites through wrappers = 827
- **`memory_alloc`:** 2383 literal sites + 330 sites through wrappers = 2713
- **`panics_and_aborts`:** 9016 literal sites + 285 sites through wrappers = 9301

- `malloc` (macro, memory_alloc, primitive): 70 call sites in 48 files -- `lib/libc/include/any-windows-any/crtdbg.h`
- `FuncGen_stackPush` (function, memory_alloc, primitive): 66 call sites in 1 files -- `stage1/FuncGen.h`
- `readLeb` (function, panics_and_aborts, primitive): 51 call sites in 1 files -- `src/link/Wasm/Object.zig`
- `uleb128Bytes` (function, panics_and_aborts, primitive): 32 call sites in 1 files -- `src/link/Dwarf.zig`
- `realloc` (macro, memory_alloc, via _realloc_dbg): 27 call sites in 17 files -- `lib/libc/include/any-windows-any/crtdbg.h`
- `calloc` (macro, memory_alloc, via _calloc_dbg): 26 call sites in 18 files -- `lib/libc/include/any-windows-any/crtdbg.h`
- `writeUleb128` (function, panics_and_aborts, primitive): 23 call sites in 1 files -- `src/codegen/wasm/Emit.zig`
- `calcTwosCompLimbCount` (function, panics_and_aborts, primitive): 20 call sites in 2 files -- `lib/std/math/big/int.zig`
- `badUsage` (function, panics_and_aborts, primitive): 17 call sites in 1 files -- `src/zig_llvm-ar.cpp`
- `fatalWithHint` (function, debug_prints, primitive): 14 call sites in 1 files -- `lib/compiler/build_runner.zig`
- `testValid` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `lib/std/unicode.zig`
- `strdup` (function, memory_alloc, primitive): 10 call sites in 6 files -- `lib/libc/musl/src/string/strdup.c`
*(+178 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 155597 call pairs -- scoped 22.3%, unique 5.5%, ambiguous 34.8%, external 37.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 96039 | 26.4% | 0.0% | 42.9% | 30.7% |
| cpp | 51982 | 15.7% | 11.7% | 22.9% | 49.7% |
| c | 6988 | 16.6% | 34.5% | 15.2% | 33.8% |
| python | 388 | 14.4% | 0.0% | 0.0% | 85.6% |
| javascript | 106 | 17.9% | 0.0% | 0.0% | 82.1% |
| shell | 57 | 0.0% | 0.0% | 0.0% | 100.0% |
| objective-c | 23 | 0.0% | 4.3% | 4.3% | 91.3% |
| assembly | 14 | 0.0% | 42.9% | 21.4% | 35.7% |

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
