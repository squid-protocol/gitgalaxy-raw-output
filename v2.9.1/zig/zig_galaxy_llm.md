# ARCHITECTURAL_BRIEF: zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ziglang/zig.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 17675 analyzed artifact(s), 2205296 LOC.
- **Load-bearing artifact:** `lib/std/std.zig` -- 1494 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/compiler_rt.zig` -- pulls in 224 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/libc/include/generic-glibc/math.h` at magnitude 23844.64 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 17675 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2863 |
| Total LOC | 2205296 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.1% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.845 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1409 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3031 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1074 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 9819 | 1340213 | 55.6% |
| C | 3654 | 182081 | 20.7% |
| ZIG | 2852 | 638088 | 16.1% |
| MAKEFILE | 858 | 17028 | 4.9% |
| ASSEMBLY | 336 | 11309 | 1.9% |
| OBJECTIVE-C | 99 | 13796 | 0.6% |
| PLAINTEXT | 19 | 0 | 0.1% |
| SHELL | 17 | 711 | 0.1% |
| MARKDOWN | 6 | 0 | 0.0% |
| PYTHON | 5 | 1187 | 0.0% |
| POWERSHELL | 3 | 251 | 0.0% |
| CSS | 2 | 280 | 0.0% |
| JSON | 2 | 12 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| JAVASCRIPT | 1 | 338 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.77`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.77; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 47%, Data / Markup / Trivial 22%, Parameter Forwarders Files 8%, Large Core Modules (2) 4%, Compute Cores Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17647 | 99.8% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 0.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2863*

**Composition by Extension & Reason:**
- `.def`: 181x Excluded (Machine-Generated Source Code Signature: 10 LOC), 133x Excluded (Machine-Generated Source Code Signature: 9 LOC), 111x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `.h`: 15x Excluded (Machine-Generated Source Code Signature: 27 LOC), 14x Excluded: Neighborhood Micro-Mass Limit Exceeded, 10x Excluded (Machine-Generated Source Code Signature: 16 LOC)
- `no_extension`: 163x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Binary Format Detected)
- `.zig`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Saturation: Line 16 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 3845 commas in 1095 LOC)
- `.input`: 44x Excluded (Unsupported Extension: '.input')
- `.zon`: 34x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 82 LOC), 1x Excluded (Embedded Hex Payload: 4517 hex tokens in 2703 LOC)
- `.c`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Packed Payload Guard (Impossible Density: 3.46 hits/line), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.tar`: 35x Excluded (Explicitly Denied Extension: '.tar')
- `.xz`: 24x Excluded (Explicitly Denied Extension: '.xz')
- `.x`: 23x Excluded (Unsupported Extension: '.x')
- `.dlg`: 8x Excluded (Unsupported Extension: '.dlg')
- `.lzma`: 5x Excluded (Unsupported Extension: '.lzma')
- `.cmake`: 4x Excluded (Unsupported Extension: '.cmake')
- `.in`: 1x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Lexical Monotony: High structural repetition detected in 2419 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2710 LOC)
- `.rh`: 4x Excluded (Unsupported Extension: '.rh')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.6 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.5 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 293592 | 8060 | 28 | `lib/libc/include/any-windows-any/adoint.h` |
| cleanup | 5515 | 651 | 0 | `lib/std/math/big/int_test.zig` |
| guards | 166360 | 6002 | 12 | `src/codegen/aarch64/Select.zig` |
| danger | 57158 | 4064 | 4 | `test/c_abi/main.zig` |
| concurrency | 3140 | 591 | 0 | `src/codegen/riscv64/CodeGen.zig` |
| connectivity | 59335 | 6758 | 4 | `lib/std/c.zig` |
| io | 2637 | 727 | 0 | `lib/libc/include/generic-freebsd/sys/socketvar.h` |
| crypto | 0 | 0 | 0 | - |
| ipc | 674 | 244 | 0 | `test/standalone/posix/sigaction.zig` |
| time | 468 | 153 | 0 | `lib/libc/include/any-windows-any/time.h` |
| serialization | 5 | 5 | 0 | `lib/std/zig/WindowsSdk.zig` |
| regex | 85 | 39 | 0 | `lib/std/crypto/benchmark.zig` |
| events | 946 | 354 | 0 | `lib/libtsan/tsan_rtl.cpp` |
| tests | 11047 | 822 | 0 | `test/c_abi/main.zig` |
| docs | 54438 | 2549 | 1 | `lib/std/zig/Zir.zig` |
| debt | 9879 | 1933 | 1 | `src/codegen/llvm.zig` |
| mutation | 278662 | 7002 | 22 | `lib/std/c.zig` |
| dead_code | 11925 | 4215 | 1 | `lib/include/lasxintrin.h` |
| credential | 21 | 13 | 0 | `lib/std/crypto/scrypt.zig` |
| threat | 340243 | 9717 | 38 | `lib/libc/include/any-windows-any/winnt.h` |
| ml_ai | 15593 | 1328 | 0 | `lib/include/avx512fintrin.h` |
| ui | 21 | 4 | 0 | `lib/build-web/main.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/libc/include/generic-freebsd/sys/socketvar.h` (Hits: 79)
- `lib/libc/include/generic-netbsd/sys/socketvar.h` (Hits: 76)
- `lib/std/Io/Threaded.zig` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **std.zig** (`lib/std/std.zig`) — 1494 inbound connections
2. **types.h** (`lib/libc/include/any-linux-any/linux/types.h`) — 673 inbound connections
3. **builtin.zig** (`lib/std/builtin.zig`) — 515 inbound connections
4. **move.h** (`lib/libcxx/include/__utility/move.h`) — 250 inbound connections
5. **winapifamily.h** (`lib/libc/include/any-windows-any/winapifamily.h`) — 196 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compiler_rt.zig** (`lib/compiler_rt.zig`) — 224 outbound dependencies
2. **sanitizer_platform_limits_netbsd.cpp** (`lib/libtsan/sanitizer_common/sanitizer_platform_limits_netbsd.cpp`) — 201 outbound dependencies
3. **macos-headers.c** (`tools/macos-headers.c`) — 157 outbound dependencies
4. **behavior.zig** (`test/behavior.zig`) — 113 outbound dependencies
5. **immintrin.h** (`lib/include/immintrin.h`) — 110 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__mingw_swformat` **(Many-Argument Workhorses)** (@ `lib/libc/mingw/stdio/mingw_swformat.c`) -> Impact: **1125.1** | LOC: 1302
- `__mingw_sformat` **(Many-Argument Workhorses)** (@ `lib/libc/mingw/stdio/mingw_sformat.c`) -> Impact: **1113.5** | LOC: 1310
- `INTERCEPTOR_WITH_SUFFIX` **(Many-Argument Workhorses)** (@ `lib/libtsan/sanitizer_common/sanitizer_common_interceptors.inc`) -> Impact: **1102.0** | LOC: 1615
  * *Intent:* // On FreeBSD id_t is always 64-bit wide. #if SANITIZER_FREEBSD && (SANITIZER_WORDSIZE == 32)
- `parseArgs` **(Many-Argument Workhorses)** (@ `lib/compiler/aro/aro/Driver.zig`) -> Impact: **806.5** | LOC: 567
  * *Intent:* ; /// Process command line arguments, returns true if something was written to std_out.
- `__strtodg` **(Many-Argument Workhorses)** (@ `lib/libc/mingw/gdtoa/strtodg.c`) -> Impact: **636.0** | LOC: 717
- `__gdtoa` **(Many-Argument Workhorses)** (@ `lib/libc/mingw/gdtoa/gdtoa.c`) -> Impact: **610.3** | LOC: 626
  * *Intent:* * quantities. * 5. When converting floating-point integers less than 1e16, * we use floating-point arithmetic rather than resorting * to multiple-prec...
- `__dtoa` **(Many-Argument Workhorses)** (@ `lib/libc/mingw/gdtoa/dtoa.c`) -> Impact: **574.4** | LOC: 693
  * *Intent:* * guarantee that the floating-point calculation has given * the correctly rounded result. For k requested digits and * "uniformly" distributed input, ...
- `iconv` **(Many-Argument Workhorses)** (@ `lib/libc/musl/src/locale/iconv.c`) -> Impact: **552.2** | LOC: 463
- `GetInstructionSize` **(Many-Argument Workhorses)** (@ `lib/libtsan/interception/interception_win.cpp`) -> Impact: **515.4** | LOC: 435
  * *Intent:* #endif // Returns 0 on error.
- `main` **(Many-Argument Workhorses)** (@ `stage1/wasm2c.c`) -> Impact: **500.2** | LOC: 1135

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/libc/include/any-windows-any` | 1146 | 49162.59 | 29.89% | 3.84% |
| `lib/std` | 68 | 32855.3 | 12.93% | 13.85% |
| `lib/include` | 201 | 31655.0 | 11.6% | 5.74% |
| `lib/libc/include/generic-glibc` | 112 | 26476.06 | 10.51% | 1.8% |
| `lib/libtsan/sanitizer_common` | 196 | 26024.0 | 30.3% | 37.37% |
| `lib/libc/include/generic-freebsd/sys` | 354 | 25638.63 | 30.85% | 12.31% |
| `lib/libc/include/any-darwin-any` | 112 | 22187.57 | 4.05% | 1.61% |
| `lib/compiler/aro/aro` | 26 | 20573.36 | 21.25% | 9.43% |
| `src/link` | 17 | 15501.58 | 19.54% | 15.72% |
| `lib/std/zig` | 23 | 13787.38 | 11.01% | 9.77% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/libc/musl/src/linux/xattr.c` -> **100.0%** Exposure
- `lib/libc/musl/src/math/acoshl.c` -> **100.0%** Exposure
- `lib/libc/musl/src/math/asinhl.c` -> **100.0%** Exposure
- `lib/libc/musl/src/math/coshl.c` -> **100.0%** Exposure
- `lib/libc/musl/src/math/expl.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/libc/freebsd/lib/csu/common/crtbegin.c` -> **100.0%** Exposure
- `lib/libc/freebsd/lib/csu/common/crtend.c` -> **100.0%** Exposure
- `lib/libc/include/any-windows-any/strsafe.h` -> **100.0%** Exposure
- `lib/libc/mingw/crt/crt_handler.c` -> **100.0%** Exposure
- `lib/libc/mingw/crt/crtexewin.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/include/lasxintrin.h` -> **537** Orphaned Functions | **0** Duplicates
- `lib/include/lsxintrin.h` -> **519** Orphaned Functions | **0** Duplicates
- `lib/libc/include/any-windows-any/mi.h` -> **202** Orphaned Functions | **0** Duplicates
- `lib/std/c.zig` -> **0** Orphaned Functions | **145** Duplicates
- `lib/libc/include/any-linux-any/linux/cec-funcs.h` -> **143** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib/std/crypto/Certificate/Bundle.zig` -> **96.4741%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36261` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/libc/include/generic-glibc/math.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 23844.64 | **LOC:** 1444 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.9%), Mutation Surface (formerly State Flux) (47.9%), Complexity Load (formerly Cognitive Load) (18.0%), Debt Markers (formerly Tech Debt) (8.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 80`, `args: 68`, `func_start: 9`, `class_start: 9`
* *Risk/State:* `state_mutation: 25`, `fragile_debt: 1`
* *Architecture:* `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` floatn.h, flt-eval-method.h, fp-fast.h, fp-logb.h, iscanonical.h, libc-header-start.h, math-vector.h, mathcalls-helper-functions.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/libc/include/generic-freebsd/sys/arb.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 14709.78 | **LOC:** 779 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.029; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.0%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 130`, `args: 68`, `func_start: 1`, `class_start: 11`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cdefs.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/compiler/aro/aro/Parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6877.84 | **LOC:** 10665 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **19**; blast radius 0.142; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (48.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.6%), Complexity Load (formerly Cognitive Load) (26.0%)
- **Documentation Coverage:** 63.4783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `castType` **(Many-Argument Workhorses)** (Impact: 346.4)
  * `adjustTypes` **(Many-Argument Workhorses)** (Impact: 216.8)
    * *Intent:* /// Adjust types for binary operation, returns true if the result can and should be evaluated.
  * `unExpr` **(Defensive Guards)** (Impact: 163.8)
    * *Intent:* /// unExpr /// : (compoundLiteral | primaryExpr) suffixExpr* /// | '&&' IDENTIFIER /// | ('&' | '*' ...
  * `decl` **(Defensive Guards)** (Impact: 146.9)
    * *Intent:* // ====== declarations ====== /// decl /// : declSpec (initDeclarator ( ',' initDeclarator)*)? ';' /...
  * `initDeclarator` **(Many-Argument Workhorses)** (Impact: 131.6)
    * *Intent:* /// initDeclarator : declarator assembly? attributeSpecifier? ('=' initializer)?
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 523 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1652
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2285`, `structural_boundaries: 1369`, `args: 211`, `func_start: 211`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 112`, `state_mutation: 606`, `dead_code: 15`, `planned_debt: 22`
* *Architecture:* `io: 1`, `api: 18`, `import: 19`
* *Defense:* `safety: 2341`, `doc: 262`, `test: 5`, `cleanup: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.002402
  * `Imports (Out-Degree: 18):` Attribute.zig, Builtins.zig, eval.zig, Compilation.zig, Diagnostics.zig, InitList.zig, Diagnostic.zig, Preprocessor.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `lib/include/altivec.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 6741.76 | **LOC:** 19365 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.029; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.7%), Guard Balance (formerly Safety Score) (52.0%), Debt Markers (formerly Tech Debt) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vec_sl` **(Compute Cores)** (Impact: 7.1)
  * `vec_sr` **(Compute Cores)** (Impact: 7.1)
    * *Intent:* #elif defined(__VSX__)
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* /* vec_first_match_or_eos_index */
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 6.1)
  * `vec_first_match_or_eos_index` **(Compute Cores)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 3189`, `args: 347`, `func_start: 2800`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 130`, `fragile_debt: 9`, `duplicate_logic: 4`
* *Architecture:* `api: 126`, `import: 1`
* *Defense:* `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stddef.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/libtsan/sanitizer_common/sanitizer_common_interceptors.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 6497.28 | **LOC:** 10694 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (50.1%), Complexity Load (formerly Cognitive Load) (47.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INTERCEPTOR_WITH_SUFFIX` **(Many-Argument Workhorses)** (Impact: 1102.0)
    * *Intent:* // On FreeBSD id_t is always 64-bit wide. #if SANITIZER_FREEBSD && (SANITIZER_WORDSIZE == 32)
  * `INTERCEPTOR` **(Many-Argument Workhorses)** (Impact: 82.6)
    * *Intent:* #else #define INIT_READDIR64 #endif #if SANITIZER_INTERCEPT_PTRACE
  * `INTERCEPTOR` **(Many-Argument Workhorses)** (Impact: 58.6)
    * *Intent:* #define INIT_PUTS COMMON_INTERCEPT_FUNCTION(puts) #else #define INIT_PUTS #endif #if SANITIZER_INTER...
  * `INTERCEPTOR` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* #define INIT_NL_LANGINFO COMMON_INTERCEPT_FUNCTION(nl_langinfo) #else #define INIT_NL_LANGINFO #endi...
  * `INTERCEPTOR` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* #define INIT_POPEN COMMON_INTERCEPT_FUNCTION(popen) #else #define INIT_POPEN #endif #if SANITIZER_IN...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2023`, `structural_boundaries: 1702`, `args: 761`, `func_start: 587`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 935`, `state_mutation: 152`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 153`
* *Architecture:* `io: 20`, `api: 3`, `import: 14`
* *Defense:* `test: 7`, `immutability_locks: 393`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.6e-05
  * `Imports (Out-Degree: 13):` interception.h, sanitizer_addrhashmap.h, sanitizer_common_interceptors_format.inc, sanitizer_common_interceptors_ioctl.inc, sanitizer_common_interceptors_netbsd_compat.inc, sanitizer_dl.h, sanitizer_errno.h, sanitizer_interceptors_ioctl_netbsd.inc...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/std/zig/AstGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5808.7 | **LOC:** 14223 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.375; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (63.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.3%), Connectivity (formerly Api Exposure) (31.4%), Guard Balance (formerly Safety Score) (30.1%)
- **Documentation Coverage:** 74.6575% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `switchExpr` **(Many-Argument Workhorses)** (Impact: 247.6)
  * `switchExprErrUnion` **(Many-Argument Workhorses)** (Impact: 196.3)
  * `whileExpr` **(Many-Argument Workhorses)** (Impact: 186.4)
  * `forExpr` **(Many-Argument Workhorses)** (Impact: 142.3)
  * `varDecl` **(Many-Argument Workhorses)** (Impact: 136.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 245 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 892
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1470`, `structural_boundaries: 1556`, `args: 246`, `func_start: 241`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 353`, `state_mutation: 402`, `dead_code: 17`, `planned_debt: 9`
* *Architecture:* `api: 13`, `concurrency: 16`, `import: 3`
* *Defense:* `safety: 1797`, `doc: 302`, `test: 7`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.375
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030893
  * `Imports (Out-Degree: 1):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/unistd.h` (OBJECTIVE-C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 5559.59 | **LOC:** 800 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (88.1%), Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (48.1%), Debt Markers (formerly Tech Debt) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 5`, `args: 66`, `func_start: 170`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 2`, `dead_code: 41`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `import: 20`
* *Defense:* `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` Availability.h, _bounds.h, _ctermid.h, _types.h, gethostuuid.h, _dev_t.h, _gid_t.h, _intptr_t.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/codegen/llvm.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5281.38 | **LOC:** 13385 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 53.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (75.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.5%), Mutation Surface (formerly State Flux) (70.1%), Connectivity (formerly Api Exposure) (38.1%)
- **Documentation Coverage:** 87.7256% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lowerDebugType` **(Many-Argument Workhorses)** (Impact: 232.7)
  * `updateFunc` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `lowerValue` **(Many-Argument Workhorses)** (Impact: 174.2)
  * `airAssembly` **(Many-Argument Workhorses)** (Impact: 155.3)
  * `lowerType` **(Many-Argument Workhorses)** (Impact: 111.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 27 instances
* *Amplified Cascading Flux:* 259 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 923
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1600`, `structural_boundaries: 1211`, `args: 264`, `func_start: 257`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 287`, `high_risk_execution: 11`, `state_mutation: 405`, `dead_code: 15`, `planned_debt: 811`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 23`, `import: 21`
* *Defense:* `safety: 2472`, `doc: 146`, `cleanup: 87`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 7.5e-05
  * `Imports (Out-Degree: 16):` Air.zig, Compilation.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/std/c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 5181.82 | **LOC:** 11591 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.1%)
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
* *Structure:* `branch: 532`, `structural_boundaries: 199`, `args: 538`, `func_start: 513`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 34`, `dead_code: 2`, `duplicate_logic: 145`
* *Architecture:* `io: 21`, `api: 4056`, `import: 10`
* *Defense:* `safety: 13`, `doc: 1034`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` builtin, darwin.zig, dragonfly.zig, freebsd.zig, haiku.zig, illumos.zig, netbsd.zig, openbsd.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/libcxx/src/locale.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4998.86 | **LOC:** 5644 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Guard Balance (formerly Safety Score) (93.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init_pat` **(Many-Argument Workhorses)** (Impact: 340.4)
    * *Intent:* #endif // _LIBCPP_HAS_WIDE_CHARACTERS // moneypunct_byname
  * `utf8_to_utf16` **(Many-Argument Workhorses)** (Impact: 170.2)
  * `utf8_to_utf16` **(Many-Argument Workhorses)** (Impact: 170.2)
  * `utf8_to_ucs4` **(Many-Argument Workhorses)** (Impact: 167.1)
  * `utf8_to_utf16_length` **(Many-Argument Workhorses)** (Impact: 156.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 710 instances
* *State Mutation (weighted view):* 2345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1482`, `structural_boundaries: 703`, `args: 126`, `func_start: 97`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 925`, `dead_code: 5`, `fragile_debt: 3`
* *Architecture:* `api: 35`, `import: 18`
* *Defense:* `safety: 66`, `immutability_locks: 905`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __undef_macros, no_destroy.h, algorithm, clocale, codecvt, cstddef, cstdio, cstdlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/std/zig/llvm/Builder.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4959.74 | **LOC:** 15173 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.6%), Guard Balance (formerly Safety Score) (52.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.5%), Debt Markers (formerly Tech Debt) (26.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toBitcode` **(Many-Argument Workhorses)** (Impact: 278.9)
  * `print` **(Many-Argument Workhorses)** (Impact: 224.3)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.023177
  * `Imports (Out-Degree: 4):` std.zig, bitcode_writer.zig, builtin, ir.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/codegen/aarch64/encoding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4567.66 | **LOC:** 16598 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.032; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.3%), Debt Markers (formerly Tech Debt) (12.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000913
  * `Imports (Out-Degree: 1):` aarch64.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libunwind/src/Registers.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4165.56 | **LOC:** 5336 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 0.08; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.0%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 99.6146% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Registers_ve::getRegisterName` **(Compute Cores)** (Impact: 227.2)
  * `Registers_ppc64::getRegisterName` **(Compute Cores)** (Impact: 169.6)
  * `Registers_arm::getRegisterName` **(Compute Cores)** (Impact: 128.6)
  * `Registers_ppc::getRegisterName` **(Compute Cores)** (Impact: 106.0)
  * `Registers_arm64::getRegisterName` **(Compute Cores)** (Impact: 106.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1717`, `structural_boundaries: 2040`, `args: 433`, `func_start: 329`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 282`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 24`
* *Architecture:* `api: 203`, `import: 5`
* *Defense:* `safety: 46`, `doc: 39`, `immutability_locks: 333`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000327
  * `Imports (Out-Degree: 2):` config.h, libunwind.h, shadow_stack_unwind.h, stdint.h, string.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/_stdlib.h` (OBJECTIVE-C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3972.93 | **LOC:** 404 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.6%), Connectivity (formerly Api Exposure) (20.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.6%), Complexity Load (formerly Cognitive Load) (7.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 6`, `args: 55`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 45`, `high_risk_execution: 3`
* *Architecture:* `api: 2`, `import: 20`
* *Defense:* `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Availability.h, _abort.h, _bounds.h, _mb_cur_max.h, _types.h, _uint32_t.h, alloca.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/std/os/linux.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3928.8 | **LOC:** 9979 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 43.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.117; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (97.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.9%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sigaction` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `fadvise` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `copy_file_range` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `pread` **(Type Conversions)** (Impact: 17.6)
  * `pwrite` **(Type Conversions)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 391`, `args: 286`, `func_start: 280`, `class_start: 250`
* *Risk/State:* `safety_bypasses: 312`, `high_risk_execution: 1`, `state_mutation: 59`, `dead_code: 14`, `planned_debt: 8`
* *Architecture:* `io: 15`, `api: 2659`, `concurrency: 3`, `import: 32`
* *Defense:* `safety: 15`, `doc: 1083`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.117
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.02989
  * `Imports (Out-Degree: 13):` dynamic_library.zig, std.zig, builtin, IoUring.zig, bpf.zig, io_uring_sqe.zig, ioctl.zig, seccomp.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/include/vecintrin.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3889.84 | **LOC:** 12869 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.041; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.8%), Connectivity (formerly Api Exposure) (50.0%), Debt Markers (formerly Tech Debt) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `t` **(Compute Cores)** (Impact: 25.0)
  * `vec_max` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* #endif
  * `vec_min` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* #endif
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
  * `t` **(I/O & Config Routines)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 3533`, `args: 135`, `func_start: 1763`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `duplicate_logic: 10`
* *Architecture:* `api: 63`
* *Defense:* `immutability_locks: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.6e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-darwin-any/simd/matrix.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3586.16 | **LOC:** 2866 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.037; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simd_transpose` **(I/O & Config Routines)** (Impact: 7.1)
  * `simd_transpose` **(I/O & Config Routines)** (Impact: 7.0)
  * `simd_transpose` **(I/O & Config Routines)** (Impact: 7.0)
  * `simd_transpose` **(I/O & Config Routines)** (Impact: 7.0)
  * `simd_transpose` **(I/O & Config Routines)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 1191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 1147`, `args: 110`, `func_start: 1137`
* *Risk/State:* `state_mutation: 679`
* *Architecture:* `import: 5`
* *Defense:* `immutability_locks: 936`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.6e-05
  * `Imports (Out-Degree: 5):` base.h, extern.h, geometry.h, logic.h, matrix_types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/codegen/riscv64/CodeGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3523.62 | **LOC:** 8501 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (37.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.8%), Debt Markers (formerly Tech Debt) (26.7%), Mutation Surface (formerly State Flux) (23.5%)
- **Documentation Coverage:** 92.0635% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `airAsm` **(Many-Argument Workhorses)** (Impact: 290.8)
  * `genBinOp` **(Many-Argument Workhorses)** (Impact: 234.0)
    * *Intent:* /// Does the same thing as binOp however is meant to be used internally to the backend. /// /// The ...
  * `airAtomicRmw` **(Defensive Guards)** (Impact: 97.1)
  * `genSetReg` **(Many-Argument Workhorses)** (Impact: 95.3)
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
* *Structure:* `branch: 1203`, `structural_boundaries: 861`, `args: 235`, `func_start: 234`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 256`, `high_risk_execution: 14`, `state_mutation: 98`, `dead_code: 9`, `planned_debt: 203`, `fragile_debt: 3`
* *Architecture:* `api: 13`, `import: 21`
* *Defense:* `safety: 1242`, `doc: 74`, `sync_locks: 110`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Air.zig, Compilation.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/libc/musl/src/regex/regcomp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3433.28 | **LOC:** 2954 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.029; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tre_add_tags` **(Many-Argument Workhorses)** (Impact: 202.3)
    * *Intent:* /* Adds tags to appropriate locations in the parse tree in `tree', so that subexpressions marked for...
  * `tre_expand_ast` **(Many-Argument Workhorses)** (Impact: 117.0)
    * *Intent:* /* Expands each iteration node that has a finite nonzero minimum or maximum iteration count to a cat...
  * `parse_atom` **(Many-Argument Workhorses)** (Impact: 116.8)
    * *Intent:* */
  * `tre_parse` **(Compute Cores)** (Impact: 106.7)
  * `tre_compute_nfl` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* /* Computes and fills in the fields `nullable', `firstpos', and `lastpos' for the nodes of the AST `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 651 instances
* *State Mutation (weighted view):* 1996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 276`, `args: 58`, `func_start: 36`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 694`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 8`
* *Defense:* `safety: 20`, `doc: 5`, `test: 11`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, ctype.h, limits.h, regex.h, stdint.h, stdlib.h, string.h, tre.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/libc/wasi/libc-top-half/musl/src/regex/regcomp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3433.28 | **LOC:** 2954 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.029; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tre_add_tags` **(Many-Argument Workhorses)** (Impact: 202.3)
    * *Intent:* /* Adds tags to appropriate locations in the parse tree in `tree', so that subexpressions marked for...
  * `tre_expand_ast` **(Many-Argument Workhorses)** (Impact: 117.0)
    * *Intent:* /* Expands each iteration node that has a finite nonzero minimum or maximum iteration count to a cat...
  * `parse_atom` **(Many-Argument Workhorses)** (Impact: 116.8)
    * *Intent:* */
  * `tre_parse` **(Compute Cores)** (Impact: 106.7)
  * `tre_compute_nfl` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* /* Computes and fills in the fields `nullable', `firstpos', and `lastpos' for the nodes of the AST `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 651 instances
* *State Mutation (weighted view):* 1996
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 276`, `args: 58`, `func_start: 36`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 694`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 8`
* *Defense:* `safety: 20`, `doc: 5`, `test: 11`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, ctype.h, limits.h, regex.h, stdint.h, stdlib.h, string.h, tre.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/codegen/c.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3386.74 | **LOC:** 8433 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 43.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.2%), Connectivity (formerly Api Exposure) (56.5%), Mutation Surface (formerly State Flux) (21.5%), Complexity Load (formerly Cognitive Load) (11.6%)
- **Documentation Coverage:** 95.4198% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderValue` **(Many-Argument Workhorses)** (Impact: 277.9)
  * `renderUndefValue` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `airAsm` **(Defensive Guards)** (Impact: 117.0)
  * `airCall` **(Defensive Guards)** (Impact: 88.0)
  * `airSwitchBr` **(Defensive Guards)** (Impact: 79.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 60 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1089`, `structural_boundaries: 577`, `args: 234`, `func_start: 229`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 2`, `state_mutation: 83`, `dead_code: 15`, `planned_debt: 39`, `fragile_debt: 4`
* *Architecture:* `api: 65`, `import: 14`
* *Defense:* `safety: 2841`, `doc: 94`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 7.5e-05
  * `Imports (Out-Degree: 8):` Air.zig, Compilation.zig, InternPool.zig, Module.zig, Type.zig, Value.zig, Zcu.zig, dev.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-windows-any/wabdefs.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 3381.41 | **LOC:** 1432 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.034; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (84.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 197`, `args: 235`, `func_start: 16`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 4`
* *Defense:* `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.034
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.6e-05
  * `Imports (Out-Degree: 2):` objbase.h, objerror.h, stddef.h, windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/libc/include/any-windows-any/strsafe.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3326.22 | **LOC:** 1931 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 0.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.1%), Guard Balance (formerly Safety Score) (82.2%), Test Surface (formerly Verification) (80.0%)
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
* *Structure:* `branch: 588`, `structural_boundaries: 135`, `args: 207`, `func_start: 84`
* *Risk/State:* `state_mutation: 429`
* *Architecture:* `api: 178`, `import: 5`
* *Defense:* `safety: 420`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000289
  * `Imports (Out-Degree: 2):` _mingw_unicode.h, specstrings.h, stdarg.h, stdio.h, string.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/include/avx512vlintrin.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3104.8 | **LOC:** 8438 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.029; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 5.6e-05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/codegen/aarch64/Select.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3046.46 | **LOC:** 12572 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (53.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.0%), Connectivity (formerly Api Exposure) (50.2%), Complexity Load (formerly Cognitive Load) (22.4%)
- **Documentation Coverage:** 97.1098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `layout` **(Many-Argument Workhorses)** (Impact: 188.0)
    * *Intent:* /// * SP to outgoing stack arguments/locals must only pass through [S] /// * entry/exit SP to prolog...
  * `addOrSubtract` **(Many-Argument Workhorses)** (Impact: 171.7)
  * `loadReg` **(Many-Argument Workhorses)** (Impact: 138.0)
  * `storeReg` **(Many-Argument Workhorses)** (Impact: 118.5)
  * `param` **(Many-Argument Workhorses)** (Impact: 104.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2551`, `structural_boundaries: 1749`, `args: 132`, `func_start: 129`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 864`, `high_risk_execution: 1`, `state_mutation: 378`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 63`, `import: 8`
* *Defense:* `safety: 3034`, `doc: 134`, `sync_locks: 15`, `cleanup: 138`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000895
  * `Imports (Out-Degree: 6):` Air.zig, InternPool.zig, Package.zig, Type.zig, Value.zig, Zcu.zig, codegen.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/codegen/llvm.zig` -> Churn: **70.55%** | Cog Load: 18.0266% | Debt: 74.9973%
- `lib/std/c.zig` -> Churn: **68.06%** | Cog Load: 3.223% | Debt: 76.9737%
- `lib/compiler/build_runner.zig` -> Churn: **59.38%** | Cog Load: 57.9418% | Debt: 8.8332%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/libc/include/any-darwin-any/unistd.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 5559.59
- `lib/libc/include/any-darwin-any/_stdlib.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 3972.93
- `lib/libc/include/any-darwin-any/simd/matrix.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 3586.16
- `lib/libc/include/any-darwin-any/simd/vector_make.h` -> **Alex Rønne Petersen** (100.0% isolated ownership) | Magnitude: 2984.62
- `lib/std/Io/Threaded.zig` -> **Andrew Kelley** (89.1% isolated ownership) | Magnitude: 2892.34

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/std/os/uefi.zig` -> **Severity: 0.009** (Bridge: 0.0002 * Flux: 51.2242%)
- `lib/std/Io.zig` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 82.2894%)
- `lib/std/Random.zig` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 91.2791%)
- `lib/std/os.zig` -> **Severity: 0.005** (Bridge: 0.0003 * Flux: 16.1747%)
- `lib/std/hash.zig` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.2406%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/std/Random.zig` -> **Severity: 3.89** (Embedded: 0.0442 * Error Risk: 88.0938%)
- `lib/std/Progress.zig` -> **Severity: 3.67** (Embedded: 0.0442 * Error Risk: 83.1199%)
- `lib/std/leb128.zig` -> **Severity: 3.533** (Embedded: 0.0442 * Error Risk: 80.0%)
- `lib/std/os.zig` -> **Severity: 3.533** (Embedded: 0.0442 * Error Risk: 80.0%)
- `lib/std/posix.zig` -> **Severity: 3.533** (Embedded: 0.0442 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/std/builtin.zig` -> **Severity: 666.999** (Blast Radius: 20.01 * Doc Risk: 33.3333%)
- `lib/std/zig.zig` -> **Severity: 526.723** (Blast Radius: 9.677 * Doc Risk: 54.4304%)
- `lib/init/src/root.zig` -> **Severity: 394.0** (Blast Radius: 7.88 * Doc Risk: 50.0%)
- `lib/libc/include/any-windows-any/_mingw.h` -> **Severity: 392.5** (Blast Radius: 3.925 * Doc Risk: 100.0%)
- `lib/libtsan/sanitizer_common/sanitizer_internal_defs.h` -> **Severity: 269.5** (Blast Radius: 2.695 * Doc Risk: 100.0%)

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
