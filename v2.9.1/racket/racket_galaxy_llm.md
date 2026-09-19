# ARCHITECTURAL_BRIEF: racket
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/racket/racket` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 4213 analyzed artifact(s), 933709 LOC.
- **Load-bearing artifact:** `racket/collects/racket/base.rkt` -- 102 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `racket/src/cs/c/configure.ac` -- pulls in 41 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `racket/src/bc/src/optimize.c` at magnitude 14218.3 (structural weight, not risk).
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
| Total Artifacts | 5828 |
| Analyzed Artifacts (Scanned) | 4213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1615 |
| Total LOC | 933709 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8984 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2206 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9872 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 218 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCHEME | 2776 | 542251 | 65.9% |
| C | 798 | 331448 | 18.9% |
| PLAINTEXT | 141 | 1 | 3.3% |
| MAKEFILE | 107 | 6836 | 2.5% |
| M4 | 80 | 17102 | 1.9% |
| ASSEMBLY | 59 | 13659 | 1.4% |
| JSON | 52 | 1328 | 1.2% |
| MARKDOWN | 51 | 0 | 1.2% |
| SHELL | 37 | 9394 | 0.9% |
| CPP | 25 | 2412 | 0.6% |
| BATCH | 12 | 298 | 0.3% |
| HTML | 10 | 2253 | 0.2% |
| ADA | 10 | 1744 | 0.2% |
| PYTHON | 9 | 1035 | 0.2% |
| CSHARP | 9 | 879 | 0.2% |
| CSS | 8 | 172 | 0.2% |
| XML | 8 | 0 | 0.2% |
| APEX | 7 | 1137 | 0.2% |
| YAML | 5 | 440 | 0.1% |
| JAVASCRIPT | 4 | 1125 | 0.1% |
| PERL | 2 | 182 | 0.0% |
| PHP | 2 | 4 | 0.0% |
| POWERSHELL | 1 | 9 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `3.984`
> **Composition Archetype:** `Flat Modular Platform` (z +3.98; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 26%, Data / Markup / Trivial 20%, Large Core Modules 15%, Many-Argument Workhorses Files 13%, Large Core Modules (3) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4021 | 95.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 191 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1615*

**Composition by Extension & Reason:**
- `.scrbl`: 510x Excluded (Unsupported Extension: '.scrbl'), 8x Unsupported Format (.scrbl), 1x Excluded (Machine-Generated Source Code Signature: 1432 LOC)
- `.rktl`: 191x Excluded (Unsupported Extension: '.rktl'), 2x Unsupported Format (.rktl)
- `.zuo`: 159x Unsupported Format (.zuo)
- `.rkt`: 146x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 53 LOC)
- `no_extension`: 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 47x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 9058 LOC)
- `.rktd`: 55x Excluded (Unsupported Extension: '.rktd')
- `.patch`: 46x Unsupported Format (.patch)
- `.ms`: 37x Unsupported Format (.ms)
- `.vcxproj`: 32x Unsupported Format (.vcxproj)
- `.stex`: 27x Unsupported Format (.stex)
- `.aux`: 20x Unsupported Format (.aux)
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 14x Unsupported Format (.rc)
- `.exp`: 14x Unsupported Format (.exp)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.1 | 5.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.9 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 74.5 | 1.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.8 | 96.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 111436 | 1324 | 20 | `racket/src/bc/src/optimize.c` |
| cleanup | 1644 | 352 | 0 | `racket/src/zuo/zuo.c` |
| guards | 20266 | 1081 | 6 | `racket/src/zuo/zuo.c` |
| danger | 14767 | 1353 | 5 | `racket/src/bc/src/optimize.c` |
| concurrency | 409 | 130 | 0 | `pkgs/racket-test/tests/future/future.rkt` |
| connectivity | 13787 | 997 | 4 | `racket/src/bc/src/schpriv.h` |
| io | 7579 | 971 | 3 | `racket/src/bc/foreign/foreign.rktc` |
| crypto | 2 | 2 | 0 | `racket/src/ChezScheme/lz4/tests/test-lz4-speed.py` |
| ipc | 414 | 55 | 0 | `racket/src/bc/src/portfun.c` |
| time | 135 | 30 | 0 | `racket/src/ChezScheme/c/stats.c` |
| serialization | 33 | 12 | 0 | `racket/src/bc/foreign/libffi/man/Makefile.in` |
| regex | 230 | 36 | 0 | `racket/src/ChezScheme/configure` |
| events | 792 | 119 | 0 | `racket/src/bc/foreign/libffi/testsuite/libffi.bhaible/test-callback.c` |
| tests | 3405 | 242 | 0 | `racket/src/io/demo.rkt` |
| docs | 5882 | 411 | 0 | `racket/src/ChezScheme/s/syntax.ss` |
| debt | 5338 | 920 | 2 | `racket/src/bc/foreign/libffi/testsuite/libffi.bhaible/test-callback.c` |
| mutation | 127799 | 1629 | 32 | `racket/src/bc/src/fun.c` |
| dead_code | 4558 | 1011 | 2 | `racket/src/ChezScheme/mats/foreign2.c` |
| credential | 19 | 13 | 0 | `pkgs/net-test/tests/net/base64.rkt` |
| threat | 14112 | 884 | 4 | `racket/src/bc/src/lightning/arm/asm.h` |
| ml_ai | 2218 | 287 | 0 | `racket/src/ChezScheme/zlib/examples/gzlog.c` |
| ui | 272 | 16 | 0 | `racket/src/ChezScheme/zlib/examples/zlib_how.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `racket/src/bc/foreign/foreign.rktc` (Hits: 605)
- `racket/src/ChezScheme/zlib/configure` (Hits: 399)
- `racket/src/ChezScheme/configure` (Hits: 249)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.rkt** (`racket/collects/racket/base.rkt`) — 102 inbound connections
2. **schpriv.h** (`racket/src/bc/src/schpriv.h`) — 63 inbound connections
3. **types.h** (`racket/src/ChezScheme/c/types.h`) — 47 inbound connections
4. **ffi_common.h** (`racket/src/bc/foreign/libffi/include/ffi_common.h`) — 47 inbound connections
5. **place.rkt** (`racket/collects/racket/place.rkt`) — 35 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **configure.ac** (`racket/src/cs/c/configure.ac`) — 41 outbound dependencies
2. **configure.ac** (`racket/src/bc/configure.ac`) — 38 outbound dependencies
3. **newgc.c** (`racket/src/bc/gc2/newgc.c`) — 25 outbound dependencies
4. **zuo.c** (`racket/src/zuo/zuo.c`) — 25 outbound dependencies
5. **expeditor.c** (`racket/src/ChezScheme/c/expeditor.c`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `scheme_generate_arith_for` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/jitarith.c`) -> Impact: **1666.2** | LOC: 1003
- `print` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/print.c`) -> Impact: **1616.3** | LOC: 1582
- `scheme_generate_inlined_nary` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/jitinline.c`) -> Impact: **1542.6** | LOC: 1212
- `scheme_generate_inlined_binary` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/jitinline.c`) -> Impact: **1510.5** | LOC: 1230
- `scheme_generate_inlined_unary` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/jitinline.c`) -> Impact: **1443.0** | LOC: 1321
- `scheme_read_number` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/numstr.c`) -> Impact: **1436.9** | LOC: 1143
  * *Intent:* */
- `install-packages` **(Many-Argument Workhorses)** (@ `racket/collects/pkg/private/install.rkt`) -> Impact: **1276.0** | LOC: 1110
- `validate_expr` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/validate.c`) -> Impact: **1020.1** | LOC: 796
  * *Intent:* #define CAN_RESET_STACK_SLOT 0 #if !CAN_RESET_STACK_SLOT # define WHEN_CAN_RESET_STACK_SLOT(x) 0 #else # define WHEN_CAN_RESET_STACK_SLOT(x) (x) #endi...
- `get-ffi-lib` **(Many-Argument Workhorses)** (@ `racket/collects/ffi/unsafe.rkt`) -> Impact: **908.1** | LOC: 1430
- `scheme_generate` **(Many-Argument Workhorses)** (@ `racket/src/bc/src/jit.c`) -> Impact: **875.0** | LOC: 1481

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `racket/src/bc/src` | 153 | 196090.83 | 45.32% | 11.99% |
| `racket/src/ChezScheme/s` | 121 | 40334.04 | 10.19% | 4.21% |
| `racket/src/ChezScheme/c` | 55 | 28475.54 | 54.56% | 27.3% |
| `racket/src/rktio` | 36 | 18440.84 | 59.69% | 39.27% |
| `racket/src/ChezScheme/zlib` | 35 | 11673.52 | 39.78% | 22.91% |
| `racket/src/bc/gc2` | 37 | 11529.44 | 38.67% | 3.84% |
| `racket/collects/racket/private` | 113 | 11068.22 | 11.03% | 3.83% |
| `racket/src/cs/rumble` | 66 | 10313.52 | 11.41% | 34.78% |
| `racket/collects/racket` | 103 | 9119.51 | 9.43% | 2.62% |
| `racket/src/ChezScheme/stex/src` | 6 | 8099.56 | 6.72% | 1.45% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `racket/collects/syntax/parse/private/tree-util.rkt` -> **100.0%** Exposure
- `racket/src/ChezScheme/mats/foreign2.c` -> **100.0%** Exposure
- `racket/src/ChezScheme/mats/foreign3.c` -> **100.0%** Exposure
- `racket/src/cs/rumble/pthread.ss` -> **99.9996%** Exposure
- `Makefile` -> **99.9972%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `racket/src/ChezScheme/configure` -> **100.0%** Exposure
- `racket/src/ChezScheme/makefiles/installsh` -> **100.0%** Exposure
- `racket/src/ChezScheme/zlib/configure` -> **100.0%** Exposure
- `racket/src/ChezScheme/zlib/os400/make.sh` -> **100.0%** Exposure
- `racket/src/bc/foreign/libffi/compile` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `racket/src/ChezScheme/mats/foreign2.c` -> **92** Orphaned Functions | **0** Duplicates
- `racket/src/bc/src/port.c` -> **83** Orphaned Functions | **0** Duplicates
- `racket/src/bc/src/thread.c` -> **72** Orphaned Functions | **0** Duplicates
- `racket/src/bc/src/startup-glue.inc` -> **60** Orphaned Functions | **0** Duplicates
- `racket/src/bc/src/error.c` -> **56** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `176` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3513` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `racket/src/bc/src/optimize.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 14218.3 | **LOC:** 11064 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (95.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimize_lets` **(Many-Argument Workhorses)** (Impact: 542.9)
  * `scheme_optimize_linklet` **(Many-Argument Workhorses)** (Impact: 423.4)
  * `scheme_omittable_expr` **(Many-Argument Workhorses)** (Impact: 356.8)
  * `finish_optimize_application3` **(Many-Argument Workhorses)** (Impact: 343.9)
  * `scheme_is_simple_make_struct_type` **(Many-Argument Workhorses)** (Impact: 309.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1911 instances
* *State Mutation (weighted view):* 5988
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3129`, `structural_boundaries: 1021`, `args: 609`, `func_start: 214`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 492`, `high_risk_execution: 2`, `state_mutation: 2166`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 8`
* *Architecture:* `api: 59`, `import: 6`
* *Defense:* `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` mzmark_optimize.inc, mzstkchk.h, schmach.h, schpriv.h, schrunst.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/fun.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12210.26 | **LOC:** 10416 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `restore_continuation` **(Many-Argument Workhorses)** (Impact: 331.6)
  * `get_or_check_arity` **(Many-Argument Workhorses)** (Impact: 324.9)
  * `continuation_marks` **(Many-Argument Workhorses)** (Impact: 291.0)
  * `scheme_apply_chaperone` **(Many-Argument Workhorses)** (Impact: 270.5)
    * *Intent:* /* must be at least 3: */ #define MAX_QUICK_CHAP_ARGV 5 #define CHAPERONE_KIND_STR(px) (!(SCHEME_CHA...
  * `grab_continuation` **(Many-Argument Workhorses)** (Impact: 183.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1957 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 6167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2206`, `structural_boundaries: 778`, `args: 613`, `func_start: 282`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 261`, `high_risk_execution: 2`, `state_mutation: 2253`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 56`
* *Architecture:* `api: 143`, `import: 10`
* *Defense:* `test: 7`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mzmark_fun.inc, mzstkchk.h, schmach.h, schmap.inc, schpriv.h, schrktio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/s/print.ss` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 10648.36 | **LOC:** 1433 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.9%), Mutation Surface (formerly State Flux) (19.7%), Complexity Load (formerly Cognitive Load) (15.7%), Debt Markers (formerly Tech Debt) (9.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 134`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 10`, `fragile_debt: 2`
* *Architecture:* `io: 9`
* *Defense:* `safety: 2`, `doc: 18`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/regexp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9884.9 | **LOC:** 6265 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (95.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.1651% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translate` **(Many-Argument Workhorses)** (Impact: 573.8)
  * `regexec` **(Many-Argument Workhorses)** (Impact: 432.0)
    * *Intent:* */
  * `regmatch` **(Many-Argument Workhorses)** (Impact: 430.9)
    * *Intent:* * * Conceptually the strategy is simple: check to see whether the current * node matches, call self ...
  * `gen_compare` **(Many-Argument Workhorses)** (Impact: 399.2)
  * `regatom` **(Many-Argument Workhorses)** (Impact: 363.5)
    * *Intent:* * * Optimization: gobbles an entire sequence of ordinary characters so that * it can turn them into ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1693 instances
* *State Mutation (weighted view):* 5175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1816`, `structural_boundaries: 408`, `args: 290`, `func_start: 95`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 1789`, `fragile_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `doc: 4`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` my_qsort.c, mzmark_regexp.inc, mzstkchk.h, schgencat.h, schmach.h, schpriv.h, schrx.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/thread.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9234.98 | **LOC:** 10170 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Complexity Load (formerly Cognitive Load) (91.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.8236% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheme_thread_block` **(Compute Cores)** (Impact: 135.9)
  * `do_sync` **(Many-Argument Workhorses)** (Impact: 120.3)
  * `check_sleep` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `current_stats` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `set_sync_target` **(Many-Argument Workhorses)** (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1463 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 4830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1743`, `structural_boundaries: 861`, `args: 853`, `func_start: 380`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 301`, `high_risk_execution: 8`, `state_mutation: 1904`, `planned_debt: 1`, `unreferenced_by_name: 72`
* *Architecture:* `api: 224`, `import: 11`
* *Defense:* `doc: 2`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` future.h, malloc.h, math.h, mzmark_thread.inc, mzstkchk.h, schgc.h, schmach.h, schpriv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/jitinline.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7651.28 | **LOC:** 5989 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Guard Balance (formerly Safety Score) (89.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheme_generate_inlined_nary` **(Many-Argument Workhorses)** (Impact: 1542.6)
  * `scheme_generate_inlined_binary` **(Many-Argument Workhorses)** (Impact: 1510.5)
  * `scheme_generate_inlined_unary` **(Many-Argument Workhorses)** (Impact: 1443.0)
  * `generate_vector_op` **(Many-Argument Workhorses)** (Impact: 386.9)
  * `generate_inlined_struct_op` **(Many-Argument Workhorses)** (Impact: 255.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 517 instances
* *State Mutation (weighted view):* 1626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1923`, `structural_boundaries: 747`, `args: 476`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 3`, `state_mutation: 592`, `dead_code: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` future.h, jit.h, jit_ts.c, schmach.h, schpriv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/zuo/zuo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7604.12 | **LOC:** 7672 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `zuo_in` **(Many-Argument Workhorses)** (Impact: 361.1)
  * `zuo_out` **(Many-Argument Workhorses)** (Impact: 227.2)
  * `zuo_process` **(Compute Cores)** (Impact: 170.5)
  * `zuo_main` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* /*======================================================================*/ /* main */ /*============...
  * `zuo_fd_open_output` **(Many-Argument Workhorses)** (Impact: 69.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 89 instances
* *Amplified Cascading Flux:* 1211 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 3882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1622`, `structural_boundaries: 672`, `args: 561`, `func_start: 333`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 223`, `high_risk_execution: 7`, `state_mutation: 1460`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `unreferenced_by_name: 29`
* *Architecture:* `io: 15`, `api: 79`, `import: 29`
* *Defense:* `safety: 1`, `immutability_locks: 117`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, crt_externs.h, ctype.h, direct.h, dirent.h, errno.h, fcntl.h, io.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/struct.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7566.12 | **LOC:** 6790 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_struct_type` **(Many-Argument Workhorses)** (Impact: 338.2)
  * `do_chaperone_struct` **(Many-Argument Workhorses)** (Impact: 253.6)
    * *Intent:* /**********************************************************************/
  * `make_struct_type` **(Many-Argument Workhorses)** (Impact: 158.5)
  * `scheme_init_struct` **(Many-Argument Workhorses)** (Impact: 112.0)
  * `make_struct_type_property_from_c` **(Many-Argument Workhorses)** (Impact: 108.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1177 instances
* *State Mutation (weighted view):* 3695
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1468`, `structural_boundaries: 576`, `args: 444`, `func_start: 205`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 277`, `state_mutation: 1341`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 70`, `import: 7`
* *Defense:* `doc: 7`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` mzmark_struct.inc, mzstkchk.h, schmach.h, schpriv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/port.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7322.68 | **LOC:** 7459 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Complexity Load (formerly Cognitive Load) (91.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.5413% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheme_get_byte_string_unless` **(Many-Argument Workhorses)** (Impact: 490.9)
  * `do_file_position` **(Many-Argument Workhorses)** (Impact: 206.0)
  * `scheme_do_open_output_file` **(Many-Argument Workhorses)** (Impact: 170.1)
  * `subprocess` **(Many-Argument Workhorses)** (Impact: 168.8)
  * `scheme_peeked_read_via_get` **(Many-Argument Workhorses)** (Impact: 99.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 991 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 3227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1417`, `structural_boundaries: 655`, `args: 486`, `func_start: 290`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 202`, `state_mutation: 1245`, `dead_code: 3`, `planned_debt: 3`, `unreferenced_by_name: 83`
* *Architecture:* `io: 2`, `api: 174`, `concurrency: 3`, `import: 15`
* *Defense:* `doc: 13`, `sync_locks: 3`, `immutability_locks: 59`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` expeditor.c, version.h, errno.h, mzmark_port.inc, mzstkchk.h, pthread.h, schmach.h, schpriv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/string.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7254.88 | **LOC:** 5878 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Complexity Load (formerly Cognitive Load) (88.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.437% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `utf8_decode_x` **(Many-Argument Workhorses)** (Impact: 513.8)
    * *Intent:* /**********************************************************************/ /* utf8 converter */ /*****...
  * `scheme_do_format` **(Many-Argument Workhorses)** (Impact: 367.6)
    * *Intent:* /********************************************************************/ /* format */ /***************...
  * `do_convert` **(Many-Argument Workhorses)** (Impact: 266.8)
  * `utf8_encode_x` **(Many-Argument Workhorses)** (Impact: 222.8)
  * `convert_one` **(Many-Argument Workhorses)** (Impact: 175.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 1054 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1357`, `structural_boundaries: 393`, `args: 353`, `func_start: 157`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 1`, `state_mutation: 1161`, `dead_code: 6`, `fragile_debt: 29`
* *Architecture:* `api: 84`, `import: 12`
* *Defense:* `safety: 5`, `doc: 33`, `immutability_locks: 83`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ctype.h, errno.h, mzmark_string.inc, racket_version.h, schpriv.h, schrktio.h, schsys.h, schustr.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/error.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6782.02 | **LOC:** 5642 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (91.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.9399% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sch_vsprintf` **(Many-Argument Workhorses)** (Impact: 393.7)
    * *Intent:* */
  * `make_arity_expect_string` **(Many-Argument Workhorses)** (Impact: 190.6)
  * `apply_one_adjuster` **(Many-Argument Workhorses)** (Impact: 118.7)
    * *Intent:* #define adjust_CONTRACT_MODE 0 #define adjust_MESSAGE_MODE 1 #define adjust_NAME_MODE 2
  * `scheme_log_name_pfx_message` **(Many-Argument Workhorses)** (Impact: 102.2)
  * `do_wrong_syntax` **(Many-Argument Workhorses)** (Impact: 94.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1089 instances
* *State Mutation (weighted view):* 3380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1159`, `structural_boundaries: 350`, `args: 411`, `func_start: 201`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 117`, `high_risk_execution: 5`, `state_mutation: 1202`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 56`
* *Architecture:* `io: 1`, `api: 87`, `import: 10`
* *Defense:* `safety: 7`, `doc: 3`, `immutability_locks: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ctype.h, errno.h, schexn.h, schpriv.h, schrktio.h, windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/file.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6535.5 | **LOC:** 5423 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Complexity Load (formerly Cognitive Load) (93.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.0149% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_simplify_path` **(Many-Argument Workhorses)** (Impact: 385.1)
  * `do_build_path` **(Many-Argument Workhorses)** (Impact: 381.6)
    * *Intent:* #define PATH_EXTRA_SPACE 4
  * `do_split_path` **(Many-Argument Workhorses)** (Impact: 361.9)
  * `do_expand_filename` **(Many-Argument Workhorses)** (Impact: 219.2)
  * `check_dos_slashslash_qm` **(Many-Argument Workhorses)** (Impact: 190.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 881 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 2747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1391`, `structural_boundaries: 357`, `args: 291`, `func_start: 142`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 985`, `unreferenced_by_name: 31`
* *Architecture:* `api: 56`, `import: 3`
* *Defense:* `safety: 1`, `doc: 6`, `immutability_locks: 46`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, schpriv.h, schrktio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/gc2/newgc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5765.4 | **LOC:** 6497 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.349; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Complexity Load (formerly Cognitive Load) (85.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.2406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `garbage_collect` **(Many-Argument Workhorses)** (Impact: 335.1)
    * *Intent:* /*****************************************************************************/ /* Garbage collectio...
  * `GC_dump_with_traces` **(Many-Argument Workhorses)** (Impact: 239.2)
    * *Intent:* #define SUMMARY_SUFFIX "/BT" #define BT_ALLOC_COUNTS alloc_counts #else #define SUMMARY_SUFFIX "" #d...
  * `repair_heap` **(Compute Cores)** (Impact: 166.9)
  * `GC_mark2` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* /* This is the first mark routine. It's a bit complicated. */
  * `mark_backpointers` **(Compute Cores)** (Impact: 62.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 880 instances
* *High Risk Execution (weighted view):* 9
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 2836
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1123`, `structural_boundaries: 658`, `args: 385`, `func_start: 247`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 10`, `state_mutation: 1076`, `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `api: 171`, `import: 28`
* *Defense:* `safety: 54`, `doc: 51`, `test: 23`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.349
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000236
  * `Imports (Out-Degree: 19):` schpriv.h, assert.h, backtrace.c, errno.h, execinfo.h, fnls.c, gc2.h, gc2_dump.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `racket/src/bc/src/print.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5605.48 | **LOC:** 4285 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (96.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.0952% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print` **(Many-Argument Workhorses)** (Impact: 1616.3)
  * `check_cycles` **(Many-Argument Workhorses)** (Impact: 223.5)
    * *Intent:* #endif #define CHECK_CHECK_HAS_UNQUOTE 0x1 #define CHECK_CHECK_HAS_CYCLE 0x2
  * `print_pair` **(Many-Argument Workhorses)** (Impact: 199.9)
  * `print_to_string` **(Many-Argument Workhorses)** (Impact: 135.8)
  * `setup_graph_table` **(Many-Argument Workhorses)** (Impact: 134.4)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 729 instances
* *State Mutation (weighted view):* 2337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1243`, `structural_boundaries: 228`, `args: 238`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 166`, `state_mutation: 879`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 15`
* *Architecture:* `api: 27`, `import: 14`
* *Defense:* `doc: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` my_qsort.c, ctype.h, malloc.h, mzmark_print.inc, mzstkchk.h, print_vector.inc, racket_version.h, schcpt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/setup/private/pkg-deps.rkt` (SCHEME | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5400.54 | **LOC:** 788 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (9.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.2%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 11`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 18`, `import: 1`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/gmp/gmp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 5294.52 | **LOC:** 5875 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mpn_tdiv_qr` **(Many-Argument Workhorses)** (Impact: 168.2)
  * `mpn_kara_mul_n` **(Many-Argument Workhorses)** (Impact: 126.1)
    * *Intent:* /*-- mpn_kara_mul_n ---------------------------------------------------------------*/ /* Multiplies ...
  * `mpn_gcd` **(Many-Argument Workhorses)** (Impact: 125.6)
    * *Intent:* #endif
  * `mpn_kara_sqr_n` **(Many-Argument Workhorses)** (Impact: 116.0)
  * `mpn_set_str` **(Many-Argument Workhorses)** (Impact: 104.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1034 instances
* *State Mutation (weighted view):* 3288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 127`, `args: 139`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 5`, `state_mutation: 1220`, `dead_code: 2`, `fragile_debt: 6`, `unreferenced_by_name: 10`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `safety: 14`, `doc: 11`, `test: 3`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` schpriv.h, gmp-impl.h, gmp.h, gmplonglong.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/resolve.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5256.48 | **LOC:** 4340 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (92.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_lambda` **(Many-Argument Workhorses)** (Impact: 336.6)
  * `compute_possible_lifts` **(Many-Argument Workhorses)** (Impact: 186.1)
  * `unresolve_expr` **(Many-Argument Workhorses)** (Impact: 175.8)
  * `scheme_resolve_lets` **(Many-Argument Workhorses)** (Impact: 160.4)
  * `maybe_unresolve_app_refs` **(Many-Argument Workhorses)** (Impact: 95.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 949 instances
* *State Mutation (weighted view):* 3070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 837`, `structural_boundaries: 287`, `args: 275`, `func_start: 95`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 211`, `state_mutation: 1172`, `dead_code: 2`, `planned_debt: 4`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` mzmark_resolve.inc, mzstkchk.h, schmach.h, schpriv.h, schrunst.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/number.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5047.98 | **LOC:** 6160 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.4%), Complexity Load (formerly Cognitive Load) (91.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheme_expt` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `scheme_init_number` **(Many-Argument Workhorses)** (Impact: 98.1)
  * `sch_pow` **(Compute Cores)** (Impact: 94.1)
    * *Intent:* #else # define protected_pow pow # ifdef MZ_LONG_DOUBLE # define protected_powl long_double_pow # en...
  * `sch_powl` **(Compute Cores)** (Impact: 90.4)
    * *Intent:* #ifdef MZ_LONG_DOUBLE
  * `atan_prim` **(Many-Argument Workhorses)** (Impact: 89.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 660 instances
* *State Mutation (weighted view):* 2127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1278`, `structural_boundaries: 619`, `args: 585`, `func_start: 261`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 807`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 53`
* *Architecture:* `api: 126`, `import: 15`
* *Defense:* `doc: 11`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ctype.h, float.h, fpu_control.h, ieeefp.h, jit_ts_protos.h, longdouble.c, longdouble.h, fpu.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/collects/openssl/test.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/sgc/sgc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4928.9 | **LOC:** 5252 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (88.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_malloc` **(Many-Argument Workhorses)** (Impact: 230.8)
    * *Intent:* #else # define ALLOC_STATISTIC(x) /* empty */ #endif #if KEEP_SET_NO || KEEP_CHUNK_SET_NO #define SE...
  * `do_GC_gcollect` **(Many-Argument Workhorses)** (Impact: 129.3)
    * *Intent:* #endif
  * `register_finalizer` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* #endif
  * `sgc_fprintf` **(Many-Argument Workhorses)** (Impact: 72.0)
    * *Intent:* # endif #endif #include <stdarg.h> #include <ctype.h> #define NP_BUFSIZE 512 /* Non-allocating print...
  * `collect_finish_common` **(Many-Argument Workhorses)** (Impact: 68.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 955 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 2951
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 946`, `structural_boundaries: 434`, `args: 216`, `func_start: 119`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 3`, `state_mutation: 1041`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 39`
* *Architecture:* `io: 2`, `api: 70`, `import: 25`
* *Defense:* `safety: 26`, `doc: 22`, `immutability_locks: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` alloc_cache.c, my_qsort.c, sconfig.h, schiptr.h, splay.c, alloc.h, autostat.inc, collect.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/portfun.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4878.3 | **LOC:** 4713 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Complexity Load (formerly Cognitive Load) (94.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `user_read_result` **(Many-Argument Workhorses)** (Impact: 227.9)
    * *Intent:* #define MAX_USER_INPUT_REUSE_SIZE 1024 /* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ...
  * `do_general_read_bytes` **(Many-Argument Workhorses)** (Impact: 180.3)
  * `do_read_char` **(Many-Argument Workhorses)** (Impact: 159.3)
  * `user_write_result` **(Many-Argument Workhorses)** (Impact: 134.5)
  * `make_output_port` **(Many-Argument Workhorses)** (Impact: 126.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 573 instances
* *State Mutation (weighted view):* 1780
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1125`, `structural_boundaries: 399`, `args: 363`, `func_start: 197`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 634`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 21`
* *Architecture:* `api: 37`, `import: 4`
* *Defense:* `doc: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` mzmark_portfun.inc, racket_version.h, schpriv.h, schrktio.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/read.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4756.54 | **LOC:** 4140 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_inner` **(Many-Argument Workhorses)** (Impact: 371.8)
  * `read_compact` **(Many-Argument Workhorses)** (Impact: 361.5)
    * *Intent:* /* never a valid symtab value: */ #define SYMTAB_IN_PROGRESS SCHEME_MULTIPLE_VALUES
  * `read_string` **(Many-Argument Workhorses)** (Impact: 232.7)
    * *Intent:* /*========================================================================*/ /* string reader */ /*=...
  * `resolve_references` **(Many-Argument Workhorses)** (Impact: 225.6)
    * *Intent:* #endif
  * `read_list` **(Many-Argument Workhorses)** (Impact: 133.8)
    * *Intent:* /* "(" (or other opener) has already been read */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 798 instances
* *State Mutation (weighted view):* 2534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 890`, `structural_boundaries: 357`, `args: 203`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 938`, `unreferenced_by_name: 14`
* *Architecture:* `io: 8`, `api: 20`, `import: 12`
* *Defense:* `safety: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ctype.h, malloc.h, mzmark_read.inc, mzstkchk.h, racket_version.h, schcpt.h, schmach.h, schminc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/ChezScheme/lz4/programs/platform.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 4540.75 | **LOC:** 156 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 0.622; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (53.7%), Connectivity (formerly Api Exposure) (9.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 2`, `args: 33`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.622
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001817
  * `Imports (Out-Degree: 0):` fcntl.h, io.h, stdio.h, unistd.h, windows.h, winioctl.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `racket/src/bc/src/hash.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4505.82 | **LOC:** 4117 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.2%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `equal_hash_key` **(Many-Argument Workhorses)** (Impact: 231.8)
  * `equal_hash_key2` **(Many-Argument Workhorses)** (Impact: 215.5)
    * *Intent:* #undef OVERFLOW_HASH #define OVERFLOW_HASH() overflow_equal_hash_key2(o, hi)
  * `do_hash` **(Many-Argument Workhorses)** (Impact: 156.7)
  * `get_bucket` **(Many-Argument Workhorses)** (Impact: 137.1)
  * `scheme_hash_tree_set_w_key_wraps` **(Many-Argument Workhorses)** (Impact: 106.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 719 instances
* *State Mutation (weighted view):* 2267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 805`, `structural_boundaries: 408`, `args: 182`, `func_start: 126`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 145`, `state_mutation: 829`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 48`
* *Architecture:* `api: 100`, `import: 27`
* *Defense:* `safety: 7`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` gc2_obj.h, ctype.h, hamt_subset.inc, math.h, mzhashchk.inc, mzmark_hash.inc, schmach.h, schpriv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `racket/src/bc/src/jitarith.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4396.5 | **LOC:** 2534 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.189; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.8%), Guard Balance (formerly Safety Score) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scheme_generate_arith_for` **(Many-Argument Workhorses)** (Impact: 1666.2)
  * `generate_float_point_arith` **(Many-Argument Workhorses)** (Impact: 845.1)
  * `scheme_generate_nary_arith` **(Many-Argument Workhorses)** (Impact: 328.2)
  * `is_inline_unboxable_op` **(Many-Argument Workhorses)** (Impact: 199.0)
  * `generate_arith_slow_path` **(Many-Argument Workhorses)** (Impact: 83.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 295 instances
* *State Mutation (weighted view):* 907
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 918`, `structural_boundaries: 288`, `args: 169`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 317`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 17`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` future.h, jit.h, jit_ts.c, schmach.h, schpriv.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `racket/src/bc/src/fun.c` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 12210.26
- `racket/src/bc/src/regexp.c` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 9884.9
- `racket/src/bc/src/thread.c` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 9234.98
- `racket/src/zuo/zuo.c` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 7604.12
- `racket/src/bc/src/port.c` -> **Matthew Flatt** (100.0% isolated ownership) | Magnitude: 7322.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `racket/src/bc/include/scheme.h` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 26.877%)
- `racket/src/bc/src/jit.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 46.1424%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `racket/src/ChezScheme/c/types.h` -> **Severity: 0.993** (Embedded: 0.0142 * Error Risk: 70.0311%)
- `racket/src/bc/include/scheme.h` -> **Severity: 0.873** (Embedded: 0.0143 * Error Risk: 60.9076%)
- `racket/src/bc/foreign/libffi/include/ffi_common.h` -> **Severity: 0.824** (Embedded: 0.0111 * Error Risk: 74.2466%)
- `racket/src/bc/src/schpriv.h` -> **Severity: 0.809** (Embedded: 0.0149 * Error Risk: 54.3135%)
- `racket/src/bc/src/schexn.h` -> **Severity: 0.763** (Embedded: 0.0096 * Error Risk: 79.6655%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `racket/collects/racket/place.rkt` -> **Severity: 577.1** (Blast Radius: 5.771 * Doc Risk: 100.0%)
- `racket/collects/racket/cmdline.rkt` -> **Severity: 432.2** (Blast Radius: 4.322 * Doc Risk: 100.0%)
- `racket/src/bc/include/scheme.h` -> **Severity: 309.5** (Blast Radius: 3.095 * Doc Risk: 100.0%)
- `racket/collects/setup/dirs.rkt` -> **Severity: 251.6** (Blast Radius: 2.516 * Doc Risk: 100.0%)
- `racket/collects/ffi/unsafe.rkt` -> **Severity: 235.6** (Blast Radius: 2.356 * Doc Risk: 100.0%)

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
