# ARCHITECTURAL_BRIEF: node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nodejs/node` |
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
| Total Artifacts | 47394 |
| Analyzed Artifacts (Scanned) | 34974 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12420 |
| Total LOC | 5636782 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.8% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1089 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 732 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 19258 | 1226330 | 55.1% |
| CPP | 7112 | 2363819 | 20.3% |
| C | 2966 | 866961 | 8.5% |
| PLAINTEXT | 2120 | 276 | 6.1% |
| HTML | 720 | 34085 | 2.1% |
| PYTHON | 692 | 166650 | 2.0% |
| ASSEMBLY | 641 | 723956 | 1.8% |
| MARKDOWN | 331 | 0 | 0.9% |
| PERL | 308 | 203194 | 0.9% |
| JSON | 259 | 12785 | 0.7% |
| TYPESCRIPT | 224 | 15858 | 0.6% |
| SHELL | 131 | 5036 | 0.4% |
| M4 | 48 | 5286 | 0.1% |
| MAKEFILE | 40 | 5801 | 0.1% |
| BATCH | 31 | 1254 | 0.1% |
| YAML | 30 | 172 | 0.1% |
| POWERSHELL | 16 | 402 | 0.0% |
| CSS | 14 | 1594 | 0.0% |
| RUST | 12 | 2736 | 0.0% |
| XML | 11 | 0 | 0.0% |
| NIX | 6 | 338 | 0.0% |
| DOCKERFILE | 1 | 10 | 0.0% |
| RUBY | 1 | 16 | 0.0% |
| SCHEME | 1 | 222 | 0.0% |
| BINARY_THREAT | 1 | 1 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32521 | 93.0% |
| Unknown | 273 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2176 | 6.2% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12420*

**Composition by Extension & Reason:**
- `.h`: 631x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 114x Excluded (Machine-Generated Source Code Signature: 132 LOC), 59x Excluded (Machine-Generated Source Code Signature: 106 LOC)
- `.js`: 1338x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 10x Excluded (Machine-Generated Source Code Signature: 106 LOC)
- `no_extension`: 1002x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 178x Unsupported Format (.undeterminable), 12x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.rs`: 967x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 58x Excluded (Machine-Generated Source Code Signature: 47 LOC), 58x Excluded (Machine-Generated Source Code Signature: 49 LOC), 57x Excluded (Machine-Generated Source Code Signature: 405 LOC)
- `.cc`: 662x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Monolithic Amalgamation: 100051 LOC exceeds safe regex boundaries), 1x Excluded (Embedded Array/Matrix Payload: 11861 commas in 2671 LOC)
- `.json`: 353x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Massive Static Asset Blob: 4982 LOC)
- `.md`: 285x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 334 LOC), 1x Excluded (Machine-Generated Source Code Signature: 90 LOC)
- `.tq`: 243x Unsupported Format (.tq), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.tq')
- `.s`: 6x Excluded (Embedded Hex Payload: 3204 hex tokens in 2682 LOC), 6x Excluded (Lexical Monotony: High structural repetition detected in 3059 LOC), 6x Excluded (Lexical Monotony: High structural repetition detected in 2622 LOC)
- `.map`: 145x Excluded (Unsupported Extension: '.map'), 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3`: 152x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5820 LOC)
- `.snapshot`: 136x Excluded (Unsupported Extension: '.snapshot')
- `.headers`: 135x Excluded (Unsupported Extension: '.headers')
- `.py`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1170 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1390 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.6 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 42.2 | 56.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 69.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 94.2 | 0.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 60.2 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 802156 | 10874 | 39 | `deps/ngtcp2/ngtcp2/lib/ngtcp2_conn.c` |
| cleanup | 7989 | 3083 | 0 | `deps/undici/undici.js` |
| guards | 365582 | 14981 | 24 | `deps/v8/src/maglev/maglev-ir.h` |
| danger | 68454 | 8688 | 3 | `deps/v8/test/mjsunit/asm/embenchen/box2d.js` |
| concurrency | 52060 | 5387 | 2 | `deps/v8/test/mjsunit/harmony/async-generators-basic.js` |
| connectivity | 94692 | 10392 | 6 | `deps/v8/test/mjsunit/harmony/modules-skip-large2.mjs` |
| io | 23955 | 4972 | 1 | `deps/ngtcp2/ngtcp2/third-party/libev/ev.pod` |
| crypto | 942 | 577 | 0 | `lib/internal/crypto/webcrypto.js` |
| ipc | 10652 | 2108 | 0 | `deps/openssl/openssl/crypto/bn/asm/ppc64-mont.pl` |
| time | 4611 | 1385 | 0 | `deps/ngtcp2/ngtcp2/third-party/libev/ev.pod` |
| serialization | 2302 | 653 | 0 | `deps/v8/test/mjsunit/json.js` |
| regex | 11225 | 1784 | 0 | `deps/openssl/openssl/crypto/chacha/asm/chacha-loongarch64.pl` |
| events | 33845 | 4615 | 2 | `deps/v8/src/codegen/x64/assembler-x64.cc` |
| tests | 90675 | 7590 | 4 | `deps/v8/test/unittests/compiler/arm64/turboshaft-instruction-selector-arm64-unittest.cc` |
| docs | 42514 | 3014 | 0 | `deps/icu-small/source/tools/toolutil/json-json.hpp` |
| debt | 31002 | 5812 | 1 | `deps/v8/src/maglev/maglev-ir.h` |
| mutation | 1036181 | 26102 | 54 | `deps/v8/test/mjsunit/asm/embenchen/box2d.js` |
| dead_code | 80634 | 9058 | 3 | `deps/v8/src/codegen/code-stub-assembler.cc` |
| credential | 3268 | 120 | 0 | `src/node_root_certs.h` |
| threat | 87312 | 9945 | 3 | `deps/openssl/openssl/include/openssl/cryptoerr_legacy.h` |
| ml_ai | 1998 | 220 | 0 | `deps/ngtcp2/ngtcp2/lib/ngtcp2_log.c` |
| ui | 1939 | 340 | 0 | `deps/openssl/openssl/crypto/ec/asm/ecp_nistz256-sparcv9.pl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `deps/ngtcp2/ngtcp2/third-party/libev/ev.pod` (Hits: 337)
- `test/parallel/test-fs-null-bytes.js` (Hits: 184)
- `deps/npm/test/lib/commands/cache.js` (Hits: 181)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **h.cjs** (`test/fixtures/test-runner/shards/h.cjs`) — 2632 inbound connections
2. **utypes.h** (`deps/icu-small/source/common/unicode/utypes.h`) — 875 inbound connections
3. **tmpdir.js** (`test/common/tmpdir.js`) — 744 inbound connections
4. **globals.h** (`deps/v8/src/common/globals.h`) — 597 inbound connections
5. **vector.h** (`deps/v8/src/base/vector.h`) — 566 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **api.cc** (`deps/v8/src/api/api.cc`) — 157 outbound dependencies
2. **isolate.cc** (`deps/v8/src/execution/isolate.cc`) — 146 outbound dependencies
3. **pipeline.cc** (`deps/v8/src/compiler/pipeline.cc`) — 131 outbound dependencies
4. **heap.cc** (`deps/v8/src/heap/heap.cc`) — 130 outbound dependencies
5. **all-objects-inl.h** (`deps/v8/src/objects/all-objects-inl.h`) — 101 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `msvcp110_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcp110_dll_lookup.hpp`) -> Impact: **3574.8** | LOC: 559
- `msvcp120_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcp120_dll_lookup.hpp`) -> Impact: **3566.3** | LOC: 559
- `msvcr100_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcr100_dll_lookup.hpp`) -> Impact: **2206.4** | LOC: 1108
- `msvcr120_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcr120_dll_lookup.hpp`) -> Impact: **2188.0** | LOC: 1023
- `msvcr110_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcr110_dll_lookup.hpp`) -> Impact: **2180.4** | LOC: 1011
- `decLnOp` (@ `deps/icu-small/source/i18n/decNumber.cpp`) -> Impact: **1576.7** | LOC: 2421
  * *Intent:* /* would certainly save at least one if it were made ten times */ /* bigger, too (for truncated fractions 0.100 through 0.999). */ /* However, for mos...
- `ntdll_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/ntdll_dll_lookup.hpp`) -> Impact: **1574.0** | LOC: 1075
- `Verifier::Visitor::Check` (@ `deps/v8/src/compiler/verifier.cc`) -> Impact: **1398.3** | LOC: 1569
  * *Intent:* #endif // DEBUG
- `kernel32_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/kernel32_dll_lookup.hpp`) -> Impact: **1392.6** | LOC: 954
- `msvcrt_dll_lookup` (@ `deps/LIEF/src/PE/utils/ordinals_lookup_tables/msvcrt_dll_lookup.hpp`) -> Impact: **1351.3** | LOC: 835

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/fixtures/keys` | 185 | 910000.25 | 0.0% | 0.0% |
| `test/fixtures/x509-escaping` | 49 | 235000.02 | 0.06% | 0.0% |
| `deps/openssl/openssl/apps` | 79 | 151419.34 | 63.81% | 9.18% |
| `deps/icu-small/source/i18n` | 432 | 132091.76 | 29.85% | 53.92% |
| `deps/icu-small/source/common` | 305 | 127816.88 | 42.66% | 41.96% |
| `test/parallel` | 4076 | 109042.62 | 7.8% | 0.0% |
| `deps/v8/test/mjsunit/regress` | 2843 | 99381.16 | 8.6% | 0.0% |
| `deps/v8/test/mjsunit/wasm/embenchen` | 9 | 94591.48 | 88.89% | 0.0% |
| `deps/v8/test/mjsunit/asm/embenchen` | 8 | 94590.16 | 100.0% | 0.0% |
| `deps/LIEF/third-party/mbedtls/library` | 162 | 74581.78 | 45.2% | 19.74% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `deps/v8/tools/testrunner/testproc/loader_test.py` -> **100.0%** Exposure
- `tools/gyp/pylib/packaging/_structures.py` -> **100.0%** Exposure
- `tools/gyp/pylib/packaging/requirements.py` -> **100.0%** Exposure
- `benchmark/async_hooks/promises.js` -> **100.0%** Exposure
- `deps/v8/test/mjsunit/sandbox/regress/regress-445209324.js` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `deps/zstd/lib/libzstd.mk` -> **100.0%** Exposure
- `deps/npm/bin/npm` -> **100.0%** Exposure
- `deps/npm/bin/npx` -> **100.0%** Exposure
- `deps/npm/lib/utils/completion.sh` -> **100.0%** Exposure
- `deps/openssl/openssl/util/find-unused-errs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `deps/v8/src/maglev/maglev-ir.h` -> **0** Orphaned Functions | **897** Duplicates
- `deps/v8/src/codegen/code-stub-assembler.cc` -> **756** Orphaned Functions | **0** Duplicates
- `deps/v8/src/maglev/maglev-ir.cc` -> **698** Orphaned Functions | **2** Duplicates
- `deps/v8/src/maglev/maglev-graph-builder.cc` -> **610** Orphaned Functions | **8** Duplicates
- `deps/v8/src/compiler/turboshaft/operations.h` -> **0** Orphaned Functions | **551** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/parallel/test-crypto.js` -> **100.0%** Exposure
- `test/parallel/test-tls-use-after-free-regression.js` -> **100.0%** Exposure
- `src/node_root_certs.h` -> **100.0%** Exposure
- `deps/LIEF/third-party/mbedtls/library/pk_internal.h` -> **100.0%** Exposure
- `tools/mk-ca-bundle.pl` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `21` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `88452` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/repl.js` (JAVASCRIPT) -> Cumulative Risk: **771.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1463.5 | **LOC:** 1506 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9983%), Documentation (98.7805%), Cognitive Load (94.2153%)
- **Heaviest Functions:** `constructor` (Impact: 415.5), `defaultEval` (Impact: 105.6), `_handleError` (Impact: 60.0)

### 2. `deps/npm/lib/commands/team.js` (JAVASCRIPT) -> Cumulative Risk: **770.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 181.08 | **LOC:** 159 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.7469%)
- **Heaviest Functions:** `listUsers` (Impact: 16.3), `listTeams` (Impact: 16.3), `exec` (Impact: 15.4)

### 3. `benchmark/streams/iter-throughput-compression.js` (JAVASCRIPT) -> Cumulative Risk: **769.34**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 129.7 | **LOC:** 105 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9835%)
- **Heaviest Functions:** `benchWebStream` (Impact: 10.2), `benchIter` (Impact: 10.1), `benchClassic` (Impact: 10.0)

### 4. `deps/npm/lib/commands/pkg.js` (JAVASCRIPT) -> Cumulative Risk: **768.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 132.6 | **LOC:** 128 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9775%)
- **Heaviest Functions:** `exec` (Impact: 15.0), `set` (Impact: 11.6), `get` (Impact: 9.7)

### 5. `deps/uv/src/unix/linux.c` (C) -> Cumulative Risk: **765.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2179.28 | **LOC:** 2745 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.1701%)
- **Heaviest Functions:** `uv__io_poll` (Impact: 87.2), `uv_cpu_info` (Impact: 72.0), `uv__iou_init` (Impact: 42.1)

### 6. `benchmark/streams/iter-throughput-pipeto.js` (JAVASCRIPT) -> Cumulative Risk: **761.08**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 155.28 | **LOC:** 122 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9927%)
- **Heaviest Functions:** `benchIter` (Impact: 10.1), `benchClassic` (Impact: 10.0), `benchWebStream` (Impact: 10.0)

### 7. `lib/internal/fs/promises.js` (JAVASCRIPT) -> Cumulative Risk: **760.13**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1819.36 | **LOC:** 2000 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9801%), Cognitive Load (95.5345%)
- **Heaviest Functions:** `writer` (Impact: 155.1), `readFileHandle` (Impact: 56.5), `pull` (Impact: 48.0)

### 8. `benchmark/streams/iter-throughput-broadcast.js` (JAVASCRIPT) -> Cumulative Risk: **759.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 210.58 | **LOC:** 146 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `benchClassic` (Impact: 23.9), `benchWebStream` (Impact: 19.0), `benchIter` (Impact: 16.4)

### 9. `deps/npm/lib/commands/shrinkwrap.js` (JAVASCRIPT) -> Cumulative Risk: **758.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 56.98 | **LOC:** 71 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Concurrency (99.9961%)
- **Heaviest Functions:** `exec` (Impact: 18.9)

### 10. `benchmark/streams/iter-throughput-identity.js` (JAVASCRIPT) -> Cumulative Risk: **755.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 162.96 | **LOC:** 133 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9935%)
- **Heaviest Functions:** `benchClassic` (Impact: 10.4), `benchWebStream` (Impact: 10.3), `benchIter` (Impact: 10.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `deps/v8/test/mjsunit/regress/regress-1200351.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 65308.52 | **LOC:** 2033 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 546 instances
* *Amplified Cascading Flux:* 208 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 624
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 665`, `structural_boundaries: 359`, `args: 91`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 137`, `high_risk_execution: 546`, `state_mutation: 208`
* *Architecture:* `api: 23`
* *Defense:* `safety: 1054`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/wasm/embenchen/box2d.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31235.18 | **LOC:** 20328 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__ZN12b2EPCollider7CollideEP10b2ManifoldPK11b2EdgeShapeRK11b2TransformPK14b2PolygonShapeS7_` (Impact: 310.2)
  * `__formatString` (Impact: 298.3)
  * `__ZN7b2World8SolveTOIERK10b2TimeStep` (Impact: 248.0)
  * `_free` (Impact: 230.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 6717 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 61
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 23450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3814`, `structural_boundaries: 2258`, `args: 769`, `func_start: 522`
* *Risk/State:* `safety_bypasses: 885`, `high_risk_execution: 5`, `state_mutation: 10016`, `dead_code: 34`, `planned_debt: 17`, `fragile_debt: 13`, `duplicate_logic: 9`, `unreferenced_by_name: 45`
* *Architecture:* `io: 42`, `concurrency: 21`, `import: 5`
* *Defense:* `safety: 571`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/asm/embenchen/box2d.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31235.14 | **LOC:** 20323 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__ZN12b2EPCollider7CollideEP10b2ManifoldPK11b2EdgeShapeRK11b2TransformPK14b2PolygonShapeS7_` (Impact: 310.2)
  * `__formatString` (Impact: 298.3)
  * `__ZN7b2World8SolveTOIERK10b2TimeStep` (Impact: 248.0)
  * `_free` (Impact: 230.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 6717 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 61
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 23450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3814`, `structural_boundaries: 2257`, `args: 769`, `func_start: 522`
* *Risk/State:* `safety_bypasses: 885`, `high_risk_execution: 5`, `state_mutation: 10016`, `dead_code: 34`, `planned_debt: 17`, `fragile_debt: 13`, `duplicate_logic: 9`, `unreferenced_by_name: 45`
* *Architecture:* `io: 42`, `concurrency: 21`, `import: 5`
* *Defense:* `safety: 571`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/code-coverage-block.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 27289.28 | **LOC:** 1271 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4512%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 74
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 223`, `args: 77`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 32`
* *Architecture:* `concurrency: 59`
* *Defense:* `safety: 109`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/wasm/embenchen/zlib.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21791.52 | **LOC:** 14758 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_inflate` (Impact: 807.3)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `_malloc` (Impact: 609.8)
  * `_deflate` (Impact: 448.3)
  * `__formatString` (Impact: 298.3)
  * `_inflate_table` (Impact: 232.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 4902 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 15697
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3466`, `structural_boundaries: 1842`, `args: 576`, `func_start: 326`
* *Risk/State:* `safety_bypasses: 900`, `high_risk_execution: 4`, `state_mutation: 5893`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`
* *Architecture:* `io: 42`, `api: 38`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 481`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/asm/embenchen/zlib.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21791.48 | **LOC:** 14753 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_inflate` (Impact: 807.3)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `_malloc` (Impact: 609.8)
  * `_deflate` (Impact: 448.3)
  * `__formatString` (Impact: 298.3)
  * `_inflate_table` (Impact: 232.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 4902 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 15697
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3466`, `structural_boundaries: 1841`, `args: 576`, `func_start: 326`
* *Risk/State:* `safety_bypasses: 900`, `high_risk_execution: 4`, `state_mutation: 5893`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`
* *Architecture:* `io: 42`, `api: 38`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 481`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/ngtcp2/ngtcp2/lib/ngtcp2_conn.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 12294.78 | **LOC:** 14160 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1593%), Tech Debt (25.8598%)
**Top Internal Functions/Classes:**
  * `conn_write_pkt` (Impact: 800.5)
    * *Intent:* * * If |require_padding| is nonzero, padding bytes are added to occupy * the remaining packet payloa...
  * `conn_recv_pkt` (Impact: 549.9)
    * *Intent:* * NGTCP2_ERR_ACK_FRAME * ACK frame is malformed. * NGTCP2_ERR_STREAM_STATE * Frame is received to th...
  * `conn_recv_handshake_pkt` (Impact: 393.6)
    * *Intent:* * NGTCP2_ERR_FRAME_FORMAT * Frame is badly formatted * NGTCP2_ERR_ACK_FRAME * ACK frame is malformed...
  * `ngtcp2_conn_write_vmsg` (Impact: 298.3)
  * `conn_write_handshake_pkt` (Impact: 286.5)
    * *Intent:* * at. |type| specifies long packet type. It should be either * NGTCP2_PKT_INITIAL or NGTCP2_PKT_HAND...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1489 instances
* *State Mutation (weighted view):* 4723
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2318`, `structural_boundaries: 1398`, `args: 399`, `func_start: 360`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1745`, `dead_code: 1`, `planned_debt: 16`, `unreferenced_by_name: 89`
* *Architecture:* `api: 135`, `import: 19`
* *Defense:* `safety: 573`, `doc: 2`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` assert.h, ngtcp2_addr.h, ngtcp2_callbacks.h, ngtcp2_cid.h, ngtcp2_conn.h, ngtcp2_conn_info.h, ngtcp2_conv.h, ngtcp2_frame_chain.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/icu-small/source/i18n/decNumber.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10597.06 | **LOC:** 8186 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6791%), Tech Debt (32.5612%)
**Top Internal Functions/Classes:**
  * `decLnOp` (Impact: 1576.7)
    * *Intent:* /* would certainly save at least one if it were made ten times */ /* bigger, too (for truncated frac...
  * `decDivideOp` (Impact: 486.8)
    * *Intent:* /* exp=exp-1 */ /* end outer_loop */ /* exp=exp+1 -- set the proper exponent */ /* if have=0 then ge...
  * `decAddOp` (Impact: 279.2)
    * *Intent:* /* overlap the A or B coefficient */ /* then the result must be calculated into a temporary buffer. ...
  * `uprv_decNumberPower` (Impact: 266.7)
    * *Intent:* /* Mathematical function restrictions apply (see above); a NaN is */ /* returned with Invalid_operat...
  * `decCompareOp` (Impact: 240.4)
    * *Intent:* /* */ /* res is C, the result. C may be A and/or B (e.g., X=X?X) */ /* lhs is A */ /* rhs is B */ /*...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 1452 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 4422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1881`, `structural_boundaries: 288`, `args: 86`, `func_start: 100`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1518`, `dead_code: 88`, `fragile_debt: 4`, `unreferenced_by_name: 50`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 204`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` cmemory.h, ctype.h, decNumber.h, decNumberLocal.h, stdlib.h, string.h, uassert.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/wasm/embenchen/fasta.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9283.18 | **LOC:** 8611 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `demangle` (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1942 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2148`, `structural_boundaries: 1448`, `args: 559`, `func_start: 309`
* *Risk/State:* `safety_bypasses: 382`, `high_risk_execution: 4`, `state_mutation: 2251`, `dead_code: 34`, `planned_debt: 17`, `fragile_debt: 13`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 517`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/asm/embenchen/fasta.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9283.14 | **LOC:** 8606 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `demangle` (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1942 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2148`, `structural_boundaries: 1447`, `args: 559`, `func_start: 309`
* *Risk/State:* `safety_bypasses: 382`, `high_risk_execution: 4`, `state_mutation: 2251`, `dead_code: 34`, `planned_debt: 17`, `fragile_debt: 13`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 517`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/wasm/embenchen/fannkuch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9180.54 | **LOC:** 8441 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `__Z15fannkuch_workerPv` (Impact: 88.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1953 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2129`, `structural_boundaries: 1379`, `args: 531`, `func_start: 281`
* *Risk/State:* `safety_bypasses: 355`, `high_risk_execution: 4`, `state_mutation: 2231`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 466`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/asm/embenchen/fannkuch.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 9180.5 | **LOC:** 8436 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `__Z15fannkuch_workerPv` (Impact: 88.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1953 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2129`, `structural_boundaries: 1378`, `args: 531`, `func_start: 281`
* *Risk/State:* `safety_bypasses: 355`, `high_risk_execution: 4`, `state_mutation: 2231`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 466`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/wasm/embenchen/memops.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8620.2 | **LOC:** 8093 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `demangle` (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1818 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 5727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2048`, `structural_boundaries: 1348`, `args: 528`, `func_start: 278`
* *Risk/State:* `safety_bypasses: 336`, `high_risk_execution: 4`, `state_mutation: 2091`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 466`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/test/mjsunit/asm/embenchen/memops.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8620.16 | **LOC:** 8088 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_malloc` (Impact: 609.8)
    * *Intent:* // EMSCRIPTEN_START_FUNCS
  * `__formatString` (Impact: 298.3)
  * `_free` (Impact: 230.2)
  * `_sysconf` (Impact: 182.3)
  * `demangle` (Impact: 82.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1818 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 5727
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2048`, `structural_boundaries: 1347`, `args: 528`, `func_start: 278`
* *Risk/State:* `safety_bypasses: 336`, `high_risk_execution: 4`, `state_mutation: 2091`, `dead_code: 31`, `planned_debt: 17`, `fragile_debt: 10`, `duplicate_logic: 9`, `unreferenced_by_name: 38`
* *Architecture:* `io: 42`, `concurrency: 16`, `import: 5`
* *Defense:* `safety: 466`, `doc: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fs, path, ws
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/maglev/maglev-graph-builder.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 8223.76 | **LOC:** 17078 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.6683%), Tech Debt (99.5971%)
**Top Internal Functions/Classes:**
  * `MaglevGraphBuilder::TryBuildPolymorphicPropertyAccess` (Impact: 190.8)
  * `MaglevGraphBuilder::TryBuildPolymorphicElementAccess` (Impact: 112.6)
  * `MaglevGraphBuilder::TryReadBoilerplateForFastLiteral` (Impact: 111.4)
  * `MaglevGraphBuilder::TryBuildNamedAccess` (Impact: 109.8)
  * `MaglevGraphBuilder::TryReduceArrayIteratingBuiltin` (Impact: 107.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 390 instances
* *State Mutation (weighted view):* 1221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2771`, `structural_boundaries: 2168`, `args: 1315`, `func_start: 733`, `class_start: 27`
* *Risk/State:* `state_mutation: 441`, `dead_code: 13`, `planned_debt: 212`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 610`
* *Architecture:* `api: 11`, `import: 76`
* *Defense:* `safety: 75`, `test: 33`, `immutability_locks: 258`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 73):` algorithm, iomanip, limits, optional, bits.h, bounds.h, container-utils.h, division-by-constant.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/LIEF/third-party/mbedtls/library/ssl_tls.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7585.6 | **LOC:** 10188 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.5855%), Tech Debt (44.8882%)
**Top Internal Functions/Classes:**
  * `ssl_tls12_populate_transform` (Impact: 310.3)
    * *Intent:* * [in] must be just initialised with mbedtls_ssl_transform_init() * [out] fully populated, ready for...
  * `mbedtls_ssl_cipher_to_psa` (Impact: 225.4)
    * *Intent:* #if defined(MBEDTLS_USE_PSA_CRYPTO) || defined(MBEDTLS_SSL_PROTO_TLS1_3)
  * `mbedtls_ssl_config_defaults` (Impact: 138.7)
    * *Intent:* #endif /* MBEDTLS_DEBUG_C && MBEDTLS_SSL_HANDSHAKE_WITH_CERT_ENABLED */ /* * Load default in mbedtls...
  * `mbedtls_ssl_verify_certificate` (Impact: 134.2)
  * `ssl_context_load` (Impact: 101.0)
    * *Intent:* /* * Deserialize context, see mbedtls_ssl_context_save() for format. * * This internal version is wr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 970 instances
* *State Mutation (weighted view):* 3070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1915`, `structural_boundaries: 808`, `args: 1029`, `func_start: 237`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1130`, `planned_debt: 4`, `unreferenced_by_name: 114`
* *Architecture:* `api: 213`, `import: 18`
* *Defense:* `safety: 259`, `doc: 1`, `immutability_locks: 289`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` common.h, debug_internal.h, constant_time.h, error.h, oid.h, platform.h, platform_util.h, psa_util.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/execution/mips64/simulator-mips64.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6785.54 | **LOC:** 7911 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (63.2707%)
**Top Internal Functions/Classes:**
  * `Simulator::DecodeTypeImmediate` (Impact: 318.6)
    * *Intent:* // Type 2: instructions using a 16, 21 or 26 bits immediate. (e.g. beq, beqc).
  * `Simulator::Msa3RInstrHelper` (Impact: 306.7)
  * `Simulator::DecodeTypeRegisterSPECIAL` (Impact: 262.8)
  * `Msa3RFInstrHelper` (Impact: 228.5)
  * `Msa2RFInstrHelper` (Impact: 224.6)
    * *Intent:* #undef QUIET_BIT_S #undef QUIET_BIT_D
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 769 instances
* *State Mutation (weighted view):* 2369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2694`, `structural_boundaries: 404`, `args: 329`, `func_start: 188`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 831`, `dead_code: 1`, `planned_debt: 9`, `unreferenced_by_name: 138`
* *Architecture:* `api: 1`, `import: 17`
* *Defense:* `safety: 3`, `test: 1`, `sync_locks: 15`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` cmath, limits.h, bits.h, memory.h, platform.h, strings.h, vector.h, assembler-inl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/codegen/mips64/macro-assembler-mips64.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6574.7 | **LOC:** 6889 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.6063%), Tech Debt (99.2804%)
**Top Internal Functions/Classes:**
  * `MacroAssembler::TruncateDoubleToI` (Impact: 1311.4)
  * `MacroAssembler::CallRecordWriteStub` (Impact: 1104.7)
  * `MacroAssembler::BranchShortHelperR6` (Impact: 333.9)
  * `MacroAssembler::BranchAndLinkShortHelperR6` (Impact: 193.1)
  * `MacroAssembler::li_optimized` (Impact: 140.8)
    * *Intent:* // All changes to if...else conditions here must be added to // InstrCountForLi64Bit as well.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1305`, `structural_boundaries: 491`, `args: 596`, `func_start: 367`
* *Risk/State:* `state_mutation: 114`, `dead_code: 4`, `planned_debt: 5`, `unreferenced_by_name: 277`
* *Architecture:* `import: 20`
* *Defense:* `safety: 22`, `test: 5`, `immutability_locks: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` limits.h, bits.h, division-by-constant.h, builtins-inl.h, assembler-inl.h, callable.h, code-factory.h, external-reference-table.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/codegen/code-stub-assembler.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6496.3 | **LOC:** 20199 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.5235%), Tech Debt (99.3182%)
**Top Internal Functions/Classes:**
  * `CodeStubAssembler::EmitElementStore` (Impact: 197.9)
  * `CodeStubAssembler::CopyFixedArrayElements` (Impact: 131.8)
  * `CodeStubAssembler::RelationalComparison` (Impact: 121.0)
  * `CodeStubAssembler::BuildFastLoop` (Impact: 72.1)
  * `CodeStubAssembler::BranchIfNumberRelationalComparison` (Impact: 66.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 1344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1046`, `structural_boundaries: 1545`, `args: 3742`, `func_start: 982`, `class_start: 4`
* *Risk/State:* `state_mutation: 798`, `dead_code: 34`, `planned_debt: 91`, `fragile_debt: 2`, `unreferenced_by_name: 756`
* *Architecture:* `api: 1`, `import: 37`
* *Defense:* `safety: 198`, `test: 5`, `immutability_locks: 231`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 36):` functional, v8-internal.h, optional, macros.h, builtins-inl.h, code-stub-assembler-inl.h, code-stub-assembler.h, define-code-stub-assembler-macros.inc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/undici/undici.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6305.0 | **LOC:** 17435 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.4714%), Tech Debt (7.9239%)
**Top Internal Functions/Classes:**
  * `parseURL` (Impact: 49.0)
  * `assertRequestHandler` (Impact: 31.6)
  * `add` (Impact: 29.6)
    * *Intent:* /** * @param {string} key * @param {any} value * @returns {void} */
  * `wrapRequestBody` (Impact: 23.8)
  * `removeChars` (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 84 instances
* *Amplified Cascading Flux:* 1428 instances
* *Concurrency (weighted view):* 593
* *State Mutation (weighted view):* 4649
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3593`, `structural_boundaries: 2647`, `args: 1105`, `func_start: 778`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 298`, `state_mutation: 1793`, `dead_code: 2`, `planned_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 30`, `api: 23`, `concurrency: 173`, `import: 99`
* *Defense:* `safety: 1790`, `doc: 212`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 138`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` dispatcher, client.js, proxy-agent, request.js, client.js, eventsource-stream, receiver, websocket...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `deps/icu-small/source/common/ucnvmbcs.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6272.06 | **LOC:** 5721 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.7846%), Tech Debt (9.8454%)
**Top Internal Functions/Classes:**
  * `ucnv_MBCSFromUnicodeWithOffsets` (Impact: 435.6)
  * `ucnv_MBCSToUnicodeWithOffsets` (Impact: 226.7)
  * `ucnv_MBCSGetFilteredUnicodeSetForUnicode` (Impact: 218.6)
  * `ucnv_MBCSLoad` (Impact: 168.3)
    * *Intent:* /* MBCS setup functions ----------------------------------------------------- */
  * `ucnv_DBCSFromUTF8` (Impact: 163.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1120 instances
* *State Mutation (weighted view):* 3552
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1202`, `structural_boundaries: 143`, `args: 99`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1312`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `import: 15`
* *Defense:* `doc: 5`, `immutability_locks: 158`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` cmemory.h, cstring.h, ucnv_bld.h, ucnv_cnv.h, ucnv_ext.h, ucnvmbcs.h, umutex.h, ucnv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/wasm/interpreter/wasm-interpreter.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6222.5 | **LOC:** 13184 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2784%), Tech Debt (23.9711%)
**Top Internal Functions/Classes:**
  * `WasmBytecodeGenerator::DoEncodeInstruction` (Impact: 1076.2)
  * `WasmBytecodeGenerator::HasSideEffects` (Impact: 708.3)
    * *Intent:* #ifdef DEBUG // static
  * `WasmBytecodeGenerator::DecodeInstruction` (Impact: 212.1)
  * `WasmBytecodeGenerator::DecodeGCOp` (Impact: 120.3)
  * `WasmBytecodeGenerator::DoEncodeSuperInstruction` (Impact: 103.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 377 instances
* *State Mutation (weighted view):* 1248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2482`, `structural_boundaries: 987`, `args: 1453`, `func_start: 309`, `class_start: 2`
* *Risk/State:* `state_mutation: 494`, `dead_code: 5`, `planned_debt: 20`, `unreferenced_by_name: 92`
* *Architecture:* `api: 2`, `import: 20`
* *Defense:* `safety: 25`, `doc: 30`, `immutability_locks: 886`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` atomic, v8-metrics.h, limits, optional, overflowing-math.h, builtins.h, global-handles-inl.h, heap-write-barrier.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/ssl/ssl_lib.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6215.7 | **LOC:** 8321 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8983%), Tech Debt (99.3625%)
**Top Internal Functions/Classes:**
  * `SSL_CTX_new_ex` (Impact: 127.2)
    * *Intent:* #endif
  * `SSL_CTX_ctrl` (Impact: 124.4)
  * `ossl_ctrl_internal` (Impact: 123.9)
  * `dane_tlsa_add` (Impact: 109.5)
  * `ossl_bytes_to_cipher_list` (Impact: 83.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 669 instances
* *State Mutation (weighted view):* 2145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1377`, `structural_boundaries: 1260`, `args: 631`, `func_start: 406`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 807`, `dead_code: 6`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 301`
* *Architecture:* `io: 1`, `api: 368`, `import: 24`
* *Defense:* `safety: 139`, `doc: 15`, `immutability_locks: 320`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` fcntl.h, cryptlib.h, e_os.h, e_winsock.h, ktls.h, nelem.h, refcount.h, ssl_unwrap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/LIEF/third-party/mbedtls/library/psa_crypto.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6185.92 | **LOC:** 9460 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.956%), Tech Debt (43.9212%)
**Top Internal Functions/Classes:**
  * `mbedtls_to_psa_error` (Impact: 177.3)
    * *Intent:* PSA_WANT_KEY_TYPE_DH_KEY_PAIR_GENERATE */
  * `psa_hkdf_input` (Impact: 92.1)
    * *Intent:* #if defined(BUILTIN_ALG_ANY_HKDF)
  * `psa_key_policy_algorithm_intersection` (Impact: 62.9)
    * *Intent:* /** Calculate the intersection of two algorithm usage policies. * * Return 0 (which allows no operat...
  * `psa_key_derivation_set_maximum_capacity` (Impact: 61.4)
  * `psa_export_public_key_internal` (Impact: 58.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 665 instances
* *State Mutation (weighted view):* 2077
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1538`, `structural_boundaries: 827`, `args: 561`, `func_start: 220`, `class_start: 2`
* *Risk/State:* `state_mutation: 747`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 101`
* *Architecture:* `api: 134`, `import: 53`
* *Defense:* `safety: 265`, `doc: 53`, `immutability_locks: 163`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` check_crypto_config.h, common.h, entropy_poll.h, aes.h, asn1.h, asn1write.h, bignum.h, camellia.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/v8/src/diagnostics/arm64/disasm-arm64.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6143.82 | **LOC:** 4748 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.3013%), Tech Debt (76.8882%)
**Top Internal Functions/Classes:**
  * `DisassemblingDecoder::VisitNEON2RegMisc` (Impact: 225.8)
  * `DisassemblingDecoder::VisitNEONLoadStoreSingleStruct` (Impact: 147.1)
  * `DisassemblingDecoder::VisitNEONLoadStoreSingleStructPostIndex` (Impact: 146.6)
  * `DisassemblingDecoder::SubstituteImmediateField` (Impact: 135.8)
  * `DisassemblingDecoder::SubstituteRegisterField` (Impact: 121.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 954 instances
* *State Mutation (weighted view):* 2874
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1925`, `structural_boundaries: 166`, `args: 418`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 966`, `planned_debt: 1`, `unreferenced_by_name: 107`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 9`, `immutability_locks: 242`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` assert.h, bitset, platform.h, wrappers.h, strings.h, vector.h, decoder-arm64-inl.h, utils-arm64.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/node_sqlite.cc` -> Churn: **76.86%** | Cog Load: 26.513% | Debt: 53.2947%
- `lib/internal/test_runner/test.js` -> Churn: **73.74%** | Cog Load: 94.362% | Debt: 12.3933%
- `lib/repl.js` -> Churn: **73.74%** | Cog Load: 94.2153% | Debt: 10.4447%
- `src/node_options.cc` -> Churn: **73.74%** | Cog Load: 65.6097% | Debt: 24.5167%
- `src/node_zlib.cc` -> Churn: **73.74%** | Cog Load: 52.7453% | Debt: 96.533%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `deps/v8/src/codegen/code-stub-assembler.cc` -> **Joyee Cheung** (100.0% isolated ownership) | Magnitude: 6496.3
- `deps/undici/undici.js` -> **Node.js GitHub Bot** (100.0% isolated ownership) | Magnitude: 6305.0
- `deps/llhttp/src/llhttp.c` -> **Node.js GitHub Bot** (100.0% isolated ownership) | Magnitude: 5869.98
- `deps/v8/src/codegen/riscv/macro-assembler-riscv.cc` -> **Vivian Wang** (100.0% isolated ownership) | Magnitude: 5187.26
- `deps/v8/src/heap/heap.cc` -> **Joyee Cheung** (100.0% isolated ownership) | Magnitude: 3822.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `deps/v8/src/compiler/turboshaft/phase.h` -> **Severity: 0.018** (Bridge: 0.0003 * Flux: 70.7564%)
- `deps/v8/src/execution/arm64/pointer-authentication-arm64.h` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 73.3187%)
- `deps/v8/src/objects/lookup-inl.h` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 98.7914%)
- `deps/LIEF/third-party/frozen/include/frozen/algorithm.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.9999%)
- `deps/v8/src/base/strings.h` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 68.9974%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `deps/v8/src/base/macros.h` -> **Severity: 833.0** (Blast Radius: 8.33 * Doc Risk: 100.0%)
- `deps/v8/src/common/globals.h` -> **Severity: 642.9** (Blast Radius: 6.429 * Doc Risk: 100.0%)
- `deps/v8/src/base/logging.h` -> **Severity: 635.5** (Blast Radius: 6.355 * Doc Risk: 100.0%)
- `deps/v8/src/base/vector.h` -> **Severity: 507.3** (Blast Radius: 5.073 * Doc Risk: 100.0%)
- `lib/internal/errors.js` -> **Severity: 419.86** (Blast Radius: 6.018 * Doc Risk: 69.7674%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
