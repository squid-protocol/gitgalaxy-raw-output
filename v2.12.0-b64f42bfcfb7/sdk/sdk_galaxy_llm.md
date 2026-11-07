# ARCHITECTURAL_BRIEF: sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dart-lang/sdk` |
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
- **Scope:** 26814 analyzed artifact(s), 4315320 LOC.
- **Load-bearing artifact:** `pkg/expect/lib/expect.dart` -- 5726 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pkg/analyzer/test/src/diagnostics/test_all.dart` -- pulls in 623 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pkg/analyzer/test/src/dart/analysis/driver_test.dart` at magnitude 27349.62 (structural weight, not risk).
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
| Total Artifacts | 54062 |
| Analyzed Artifacts (Scanned) | 26814 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27248 |
| Total LOC | 4315320 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 49.6% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7769 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1247 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1059 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| DART | 23857 | 3679274 | 89.0% |
| CPP | 1080 | 540071 | 4.0% |
| YAML | 745 | 14264 | 2.8% |
| PLAINTEXT | 275 | 18 | 1.0% |
| MARKDOWN | 263 | 0 | 1.0% |
| JAVA | 148 | 10669 | 0.6% |
| PYTHON | 134 | 23472 | 0.5% |
| JSON | 123 | 2122 | 0.5% |
| HTML | 44 | 17663 | 0.2% |
| SHELL | 41 | 1772 | 0.2% |
| XML | 35 | 0 | 0.1% |
| JAVASCRIPT | 24 | 19710 | 0.1% |
| ASSEMBLY | 10 | 465 | 0.0% |
| C | 8 | 580 | 0.0% |
| MAKEFILE | 6 | 206 | 0.0% |
| CSS | 6 | 3732 | 0.0% |
| PROTO | 6 | 770 | 0.0% |
| BATCH | 6 | 64 | 0.0% |
| OBJECTIVE-C | 1 | 18 | 0.0% |
| CSV | 1 | 449 | 0.0% |
| PHP | 1 | 1 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 26796 |
| unknown | unknown | 16 |
| utf-8 | bom | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 22%, State Mutators Files 19%, Large Core Modules (2) 15%, Callbacks & Closures Files 12%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 26271 | 98.0% |
| Unknown | 16 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 522 | 1.9% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27248*

**Composition by Extension & Reason:**
- `.expect`: 25005x Excluded (Unsupported Extension: '.expect'), 284x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dart`: 164x Excluded: Neighborhood Micro-Mass Limit Exceeded, 78x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded (Machine-Generated Source Code Signature: 13 LOC)
- `no_extension`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 122x Unsupported Format (.darttemplate), 27x Excluded (Unsupported Extension: '.outline_extracted')
- `.options`: 211x Excluded (Unsupported Extension: '.options'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 102x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 18 LOC)
- `.gni`: 55x Excluded (Unsupported Extension: '.gni'), 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.gni)
- `.html`: 81x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Zero-Density Threshold (LOC: 56, Signals: 0), 4x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.status`: 66x Excluded (Unsupported Extension: '.status'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 60x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 28838 LOC), 1x Excluded (Massive Static Asset Blob: 67431 LOC)
- `.crash_dart`: 67x Excluded (Unsupported Extension: '.crash_dart')
- `.gn`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Excluded (Unsupported Extension: '.gn')
- `.wat`: 41x Excluded (Unsupported Extension: '.wat')
- `.py`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `.h`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 23802 LOC), 1x Excluded (Machine-Generated Source Code Signature: 54 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.2 | 25.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.4 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 83.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 27699 | 3723 | 1 | `runtime/vm/compiler/assembler/assembler_riscv_test.cc` |
| cleanup | 4678 | 1334 | 0 | `tests/lib/async/stream_controller_test.dart` |
| guards | 374431 | 15839 | 28 | `runtime/vm/object.cc` |
| danger | 76787 | 8884 | 5 | `pkg/_fe_analyzer_shared/lib/src/parser/parser_impl.dart` |
| concurrency | 182618 | 7152 | 12 | `pkg/analyzer/test/src/dart/analysis/driver_test.dart` |
| connectivity | 227689 | 21303 | 14 | `tests/web/deferred/many_parts/libB.dart` |
| io | 12583 | 1825 | 0 | `pkg/analysis_server/doc/api.html` |
| crypto | 2 | 2 | 0 | `tools/bots/bot_utils.py` |
| ipc | 2381 | 741 | 0 | `tests/ffi/async_void_function_callbacks_test.dart` |
| time | 2118 | 849 | 0 | `tests/corelib/duration_test.dart` |
| serialization | 1728 | 463 | 0 | `pkg/analysis_server/lib/protocol/protocol_generated.dart` |
| regex | 3470 | 567 | 0 | `tests/corelib/regexp/regexp_test.dart` |
| events | 7285 | 1245 | 0 | `pkg/vm_snapshot_analysis/lib/src/assets/d3/src/d3.js` |
| tests | 49257 | 2153 | 0 | `runtime/vm/compiler/assembler/assembler_riscv_test.cc` |
| docs | 172630 | 5439 | 7 | `sdk/lib/typed_data/typed_data.dart` |
| debt | 59026 | 7699 | 4 | `runtime/vm/compiler/backend/il.h` |
| mutation | 677385 | 18954 | 47 | `tests/language/regress/regress41983_test.dart` |
| dead_code | 58860 | 15968 | 3 | `runtime/vm/object.cc` |
| credential | 4109 | 18 | 0 | `benchmarks/StringPool/dart/version1a.dart` |
| threat | 316 | 70 | 0 | `runtime/vm/unicode_test.cc` |
| ml_ai | 4859 | 1043 | 0 | `sdk/lib/_internal/vm/lib/typed_data_patch.dart` |
| ui | 4334 | 227 | 0 | `pkg/analysis_server/doc/api.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pkg/analysis_server/doc/api.html` (Hits: 975)
- `pkg/frontend_server/test/frontend_server_test.dart` (Hits: 374)
- `pkg/analyzer_plugin/doc/api.html` (Hits: 355)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **expect.dart** (`pkg/expect/lib/expect.dart`) — 5726 inbound connections
2. **process_check_arguments_script.dart** (`tests/standalone/io/process_check_arguments_script.dart`) — 3784 inbound connections
3. **diagnostic.dart** (`pkg/analyzer/lib/src/diagnostic/diagnostic.dart`) — 1105 inbound connections
4. **async_helper.dart** (`pkg/expect/lib/async_helper.dart`) — 784 inbound connections
5. **context_collection_resolution.dart** (`pkg/analyzer/test/src/dart/resolution/context_collection_resolution.dart`) — 779 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_all.dart** (`pkg/analyzer/test/src/diagnostics/test_all.dart`) — 623 outbound dependencies
2. **test_all.dart** (`pkg/analysis_server/test/src/services/correction/fix/test_all.dart`) — 277 outbound dependencies
3. **fix_internal.dart** (`pkg/analysis_server/lib/src/services/correction/fix_internal.dart`) — 263 outbound dependencies
4. **rules.dart** (`pkg/linter/lib/src/rules.dart`) — 256 outbound dependencies
5. **all.dart** (`pkg/linter/test/rules/all.dart`) — 243 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Compute Cores)** (@ `tests/language/syntax/deep_nesting_statement_test.dart`) -> Impact: **3089.1** | LOC: 2942
- `ConstantInstr::EmitMoveToLocation` **(Many-Argument Workhorses)** (@ `runtime/vm/compiler/backend/il_riscv.cc`) -> Impact: **3065.9** | LOC: 6355
- `ExpressionVisitor` **(I/O & Config Routines)** (@ `pkg/dev_compiler/lib/src/kernel/compiler_new.dart`) -> Impact: **1916.5** | LOC: 9770
- `Compiler` **(Stateful Encapsulated Methods)** (@ `pkg/dev_compiler/lib/src/kernel/compiler.dart`) -> Impact: **1858.2** | LOC: 9144
- `dartProgram` **(Defensive Guards)** (@ `pkg/dart_runtime_service/test/web/sse_smoke_driver.dart.js`) -> Impact: **1829.8** | LOC: 4217
- `NullShortingMixin` **(Defensive Guards)** (@ `pkg/analyzer/lib/src/generated/resolver.dart`) -> Impact: **1054.0** | LOC: 4920
- `incByIfThenElseDispatch256` **(Defensive Guards)** (@ `pkg/front_end/benchmarks/patterns/generated/datatype256.dart`) -> Impact: **912.6** | LOC: 515
- `main` **(I/O & Config Routines)** (@ `pkg/_fe_analyzer_shared/test/flow_analysis/flow_analysis_test.dart`) -> Impact: **705.7** | LOC: 12813
- `incByIfThenElseDispatch192` **(Defensive Guards)** (@ `pkg/front_end/benchmarks/patterns/generated/datatype192.dart`) -> Impact: **684.5** | LOC: 387
- `deserialize` **(Many-Argument Workhorses)** (@ `pkg/wasm_builder/lib/src/ir/instruction.dart`) -> Impact: **681.7** | LOC: 494

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `runtime/vm` | 461 | 117369.08 | 20.9% | 48.96% |
| `tests/standalone/io/certificates` | 16 | 75001.42 | 0.0% | 0.0% |
| `pkg/analyzer/test/src/diagnostics` | 623 | 73117.48 | 1.32% | 0.0% |
| `tests/language/function_type` | 101 | 68587.12 | 28.55% | 0.0% |
| `pkg/analysis_server/test/src/services/correction/fix` | 275 | 55228.94 | 3.38% | 0.0% |
| `runtime/vm/compiler/backend` | 75 | 53935.68 | 22.4% | 54.41% |
| `pkg/linter/test/rules` | 245 | 44065.58 | 1.51% | 0.0% |
| `pkg/analyzer/test/src/dart/analysis` | 26 | 38384.58 | 15.21% | 0.0% |
| `pkg/analyzer/test/src/dart/resolution` | 109 | 31446.32 | 2.03% | 0.0% |
| `runtime/vm/compiler/assembler` | 30 | 29012.88 | 19.84% | 37.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tools/patches/utils.sh` -> **100.0%** Exposure
- `tools/dom/scripts/emitter_test.py` -> **100.0%** Exposure
- `benchmarks/AsyncLiveVars/dart/AsyncLiveVars.dart` -> **100.0%** Exposure
- `benchmarks/FfiBoringssl/dart/types.dart` -> **100.0%** Exposure
- `benchmarks/FfiMemory/dart/FfiMemory.dart` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pkg/dart2wasm/tool/compile_benchmark` -> **100.0%** Exposure
- `pkg/dart2wasm/tool/run_benchmark` -> **100.0%** Exposure
- `pkg/front_end/tool/cfe` -> **100.0%** Exposure
- `pkg/vm/tool/dart_precompiled_runtime2` -> **100.0%** Exposure
- `pkg/vm/tool/dump_kernel` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `runtime/vm/object.cc` -> **1309** Orphaned Functions | **4** Duplicates
- `runtime/vm/compiler/backend/il.h` -> **0** Orphaned Functions | **735** Duplicates
- `pkg/analysis_server/lib/protocol/protocol_generated.dart` -> **323** Orphaned Functions | **354** Duplicates
- `pkg/analysis_server_client/lib/src/protocol/protocol_generated.dart` -> **323** Orphaned Functions | **354** Duplicates
- `sdk/lib/_internal/vm/lib/typed_data_patch.dart` -> **164** Orphaned Functions | **299** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `runtime/bin/secure_socket_utils_test.cc` -> **99.9997%** Exposure
- `tests/standalone/io/issue_26954_test.dart` -> **99.9946%** Exposure
- `pkg/compiler/test/codesize/swarm/appengine/main.py` -> **20.7243%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70280` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pkg/analyzer/test/src/dart/analysis/driver_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 18.613)
- **Top Global Matches:** file_cluster_15: 18.613, file_cluster_16: 18.894, file_cluster_12: 19.099
- **Magnitude:** 27349.62 | **LOC:** 102578 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **53**; blast radius 0.018; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.8%), Connectivity (formerly Api Exposure) (85.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.4%), Guard Balance (formerly Safety Score) (51.0%)
- **Documentation Coverage:** 99.9151% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_runChangeScenario` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `_runLibraryManifestScenario` **(Many-Argument Workhorses)** (Impact: 42.0)
  * `_listenSchedulerEvents` **(Stateful Encapsulated Methods)** (Impact: 19.5)
  * `_runChangeScenarioTA` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `_runLibraryManifestScenario` **(Many-Argument Workhorses)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 429 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 5850
* *State Mutation (weighted view):* 3496
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 9799`, `args: 3432`, `func_start: 5882`, `class_start: 2707`
* *Risk/State:* `safety_bypasses: 121`, `high_risk_execution: 5`, `state_mutation: 3466`, `planned_debt: 1`, `fragile_debt: 25`, `duplicate_logic: 143`
* *Architecture:* `io: 34`, `api: 3065`, `concurrency: 3705`, `import: 524`
* *Defense:* `safety: 891`, `doc: 12`, `test: 109`, `sync_locks: 5`, `immutability_locks: 332`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 30):` $innerUri, diff.dart, element_printer.dart, b.dart, context_collection_resolution.dart, node_text_expectations.dart, resolution.dart, :...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/web/deferred/many_parts/libB.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.571)
- **Top Global Matches:** file_cluster_0: 9.571, file_cluster_10: 12.602, file_cluster_13: 13.048
- **Magnitude:** 23266.74 | **LOC:** 24584 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **1**; blast radius 0.115; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `v` **(Generic / Templated Code)** (Impact: 2.2)
  * `f_000_000_000_000_1` **(Generic / Templated Code)** (Impact: 1.8)
  * `f_000_000_000_001_1` **(Generic / Templated Code)** (Impact: 1.8)
  * `f_000_000_000_010_1` **(Generic / Templated Code)** (Impact: 1.8)
  * `f_000_000_000_011_1` **(Generic / Templated Code)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8192`, `args: 8192`, `func_start: 8192`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 8192`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` expect.dart
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/language/regress/regress41983_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.456)
- **Top Global Matches:** file_cluster_2: 6.456, file_cluster_17: 8.308, file_cluster_15: 8.321
- **Magnitude:** 20418.16 | **LOC:** 20015 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.1%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 20015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 20001`, `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 2):` expect.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/object.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.077)
- **Top Global Matches:** file_cluster_4: 11.077, file_cluster_15: 11.163, file_cluster_16: 12.294
- **Magnitude:** 14713.38 | **LOC:** 28795 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **131** in-repo importer(s); it depends on **76**; blast radius 0.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Class::IsSubtypeOf` **(Many-Argument Workhorses)** (Impact: 110.5)
    * *Intent:* // Checks if type T0 is a subtype of type T1. // Type T0 is specified by class 'cls' parameterized w...
  * `Function::RecognizedKindForceOptimize` **(Compute Cores)** (Impact: 97.7)
  * `Class::GenerateUserVisibleName` **(Compute Cores)** (Impact: 97.2)
    * *Intent:* #endif // !defined(PRODUCT) || defined(FORCE_INCLUDE_SAMPLING_HEAP_PROFILER)
  * `VerifyEntryPoint` **(Many-Argument Workhorses)** (Impact: 91.3)
    * *Intent:* #endif
  * `AbstractType::IsSubtypeOf` **(Many-Argument Workhorses)** (Impact: 86.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1163 instances
* *State Mutation (weighted view):* 4073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3931`, `structural_boundaries: 3556`, `args: 2970`, `func_start: 1712`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 1747`, `dead_code: 3`, `planned_debt: 77`, `duplicate_logic: 4`, `unreferenced_by_name: 1309`
* *Architecture:* `api: 17`, `import: 76`
* *Defense:* `safety: 17`, `doc: 3`, `test: 26`, `immutability_locks: 3651`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 143):` dart_api.h, integers.h, stacktrace.h, memory, assert.h, text_buffer.h, unaligned.h, unicode.h...
  * `Imported By (In-Degree: 131):` (Excluded from Brief to save tokens)

### `pkg/analysis_server/lib/protocol/protocol_generated.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.498)
- **Top Global Matches:** file_cluster_0: 9.498, file_cluster_10: 9.613, file_cluster_13: 10.043
- **Magnitude:** 12113.6 | **LOC:** 19424 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **174** in-repo importer(s); it depends on **5**; blast radius 0.842; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (40.8%), Complexity Load (formerly Cognitive Load) (28.7%)
- **Documentation Coverage:** 75.3634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FlutterOutline.fromJson` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `HoverInformation.fromJson` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `ElementDeclaration.fromJson` **(Many-Argument Workhorses)** (Impact: 68.0)
  * `FlutterWidgetProperty.fromJson` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `RuntimeCompletionExpressionType.fromJson` **(Many-Argument Workhorses)** (Impact: 58.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 974 instances
* *State Mutation (weighted view):* 2954
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3106`, `structural_boundaries: 1967`, `args: 1289`, `func_start: 1441`, `class_start: 211`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1006`, `planned_debt: 211`, `duplicate_logic: 354`, `unreferenced_by_name: 323`
* *Architecture:* `api: 211`, `import: 5`
* *Defense:* `safety: 2613`, `doc: 2603`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.842
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 5):` dart:convert, protocol.dart, protocol_internal.dart, protocol_common.dart, client_uri_converter.dart
  * `Imported By (In-Degree: 174):` (Excluded from Brief to save tokens)

### `pkg/dart_runtime_service/test/web/sse_smoke_driver.dart.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 19.143)
- **Top Global Matches:** file_cluster_12: 19.143, file_cluster_7: 19.585, file_cluster_5: 19.819
- **Magnitude:** 10629.92 | **LOC:** 4217 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 0.038; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.5%), Concurrency Surface (formerly Concurrency) (57.9%), Complexity Load (formerly Cognitive Load) (49.9%), Connectivity (formerly Api Exposure) (41.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dartProgram` **(Defensive Guards)** (Impact: 1829.8)
  * `t` **(Defensive Guards)** (Impact: 112.1)
  * `aj` **(Defensive Guards)** (Impact: 64.8)
  * `ae` **(Defensive Guards)** (Impact: 56.3)
  * `fA` **(Many-Argument Workhorses)** (Impact: 53.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 1338 instances
* *Concurrency (weighted view):* 123
* *State Mutation (weighted view):* 4336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1618`, `structural_boundaries: 1711`, `args: 1093`, `func_start: 1168`
* *Risk/State:* `safety_bypasses: 433`, `state_mutation: 1660`, `duplicate_logic: 53`
* *Architecture:* `io: 6`, `api: 16`, `concurrency: 23`
* *Defense:* `safety: 653`, `test: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pkg/_fe_analyzer_shared/lib/src/parser/parser_impl.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.019)
- **Top Global Matches:** file_cluster_6: 12.019, file_cluster_4: 16.424, file_cluster_8: 16.606
- **Magnitude:** 10099.84 | **LOC:** 12395 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 46.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **27**; blast radius 0.065; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.2%)
- **Documentation Coverage:** 36.6224% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseMethod` **(Many-Argument Workhorses)** (Impact: 513.9)
  * `parseClassOrMixinOrExtensionOrEnumMemberImpl` **(Many-Argument Workhorses)** (Impact: 263.2)
    * *Intent:* /// constructorDeclaration | /// methodDeclaration /// ; /// /// mixinMember: /// fieldDeclaration |...
  * `_parsePrecedenceExpressionLoop` **(Many-Argument Workhorses)** (Impact: 248.3)
  * `parseFormalParameter` **(Many-Argument Workhorses)** (Impact: 233.4)
    * *Intent:* /// ; /// /// functionFormalParameter: /// metadata 'covariant'? returnType? identifier formalParame...
  * `parseTopLevelKeywordDeclaration` **(Many-Argument Workhorses)** (Impact: 221.2)
    * *Intent:* /// Parse any top-level declaration that begins with a keyword. /// [beginToken] is the first token ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 1093 instances
* *Concurrency (weighted view):* 76
* *State Mutation (weighted view):* 3494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2521`, `structural_boundaries: 794`, `args: 282`, `func_start: 286`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1040`, `state_mutation: 1308`, `dead_code: 5`, `planned_debt: 58`
* *Architecture:* `api: 27`, `concurrency: 21`, `import: 27`
* *Defense:* `safety: 543`, `doc: 1236`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 27):` flags.dart, codes.dart, scanner.dart, token.dart, token_constants.dart, assert.dart, async_modifier.dart, block_kind.dart...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `pkg/front_end/lib/src/type_inference/inference_visitor.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.167)
- **Top Global Matches:** file_cluster_6: 9.167, file_cluster_4: 10.11, file_cluster_12: 17.021
- **Magnitude:** 9846.16 | **LOC:** 17567 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 54.2%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **43**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%)
- **Documentation Coverage:** 95.3608% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InferenceVisitor` **(I/O & Config Routines)** (Impact: 267.6)
  * `_inferSpreadMapEntry` **(Many-Argument Workhorses)** (Impact: 129.4)
  * `_computePropertySet` **(Many-Argument Workhorses)** (Impact: 116.1)
    * *Intent:* /// /// [fileOffset] is used as the file offset for created nodes. [propertyName] /// is used for er...
  * `_computeIndexSet` **(Many-Argument Workhorses)** (Impact: 106.3)
    * *Intent:* /// Creates an index set operation of [writeTarget] on [receiver] using /// [index] and [value] as t...
  * `_computeBinaryExpression` **(Many-Argument Workhorses)** (Impact: 105.8)
    * *Intent:* /// Creates a binary expression of the binary operator with [binaryName] using /// [left] and [right...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1027 instances
* *State Mutation (weighted view):* 3315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2117`, `structural_boundaries: 743`, `args: 474`, `func_start: 456`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 200`, `state_mutation: 1261`, `dead_code: 7`, `planned_debt: 43`
* *Architecture:* `api: 224`, `import: 44`
* *Defense:* `safety: 1053`, `doc: 179`, `immutability_locks: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 46):` experimental_flags.dart, compiler_context.dart, messages.dart, problems.dart, uri_offset.dart, library_builder.dart, dill_library_builder.dart, body_builder.dart...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pkg/analysis_server/test/services/completion/dart/completion_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 12.814)
- **Top Global Matches:** file_cluster_12: 12.814, file_cluster_11: 13.585, file_cluster_15: 13.721
- **Magnitude:** 9316.96 | **LOC:** 11236 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **20**; blast radius 0.128; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (91.8%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_completion_import_lib_1` **(I/O & Config Routines)** (Impact: 137.0)
  * `test_completion_export_dart_1` **(I/O & Config Routines)** (Impact: 43.8)
  * `test_014_1` **(I/O & Config Routines)** (Impact: 4.5)
  * `test_014_2` **(I/O & Config Routines)** (Impact: 4.5)
  * `test_014_4` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 925 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 5980
* *State Mutation (weighted view):* 530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 2059`, `args: 1160`, `func_start: 1475`, `class_start: 399`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 456`, `planned_debt: 52`, `fragile_debt: 9`, `duplicate_logic: 77`
* *Architecture:* `io: 17`, `api: 959`, `concurrency: 1355`, `import: 75`
* *Defense:* `safety: 278`, `doc: 23`, `immutability_locks: 109`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` completion_driver_test.dart, ^, ^uri, dart:^, dart:convert, dart:math, dart:math
import, exp1a.dart...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pkg/analysis_server_client/lib/src/protocol/protocol_generated.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.347)
- **Top Global Matches:** file_cluster_0: 9.347, file_cluster_10: 9.873, file_cluster_13: 10.215
- **Magnitude:** 9156.52 | **LOC:** 16855 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 0.234; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.3%)
- **Documentation Coverage:** 73.4738% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FlutterOutline.fromJson` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `HoverInformation.fromJson` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `ElementDeclaration.fromJson` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `FlutterWidgetProperty.fromJson` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `ExtractMethodFeedback.fromJson` **(Many-Argument Workhorses)** (Impact: 48.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 718 instances
* *State Mutation (weighted view):* 2442
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2183`, `structural_boundaries: 1924`, `args: 1247`, `func_start: 1376`, `class_start: 211`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1006`, `planned_debt: 211`, `duplicate_logic: 354`, `unreferenced_by_name: 323`
* *Architecture:* `api: 211`, `import: 4`
* *Defense:* `safety: 1046`, `doc: 2603`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 4):` dart:convert, protocol_base.dart, protocol_common.dart, protocol_internal.dart
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pkg/dev_compiler/lib/src/kernel/compiler_new.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.995)
- **Top Global Matches:** file_cluster_4: 11.995, file_cluster_12: 13.526, file_cluster_16: 14.761
- **Magnitude:** 7137.88 | **LOC:** 10110 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **40**; blast radius 0.064; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.8%)
- **Documentation Coverage:** 68.1467% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExpressionVisitor` **(I/O & Config Routines)** (Impact: 1916.5)
  * `visitStaticInvocation` **(Compute Cores)** (Impact: 142.1)
  * `_emitClassSignature` **(Many-Argument Workhorses)** (Impact: 88.3)
    * *Intent:* /// Emit the signature on the class recording the runtime type information
  * `_defineClass` **(Many-Argument Workhorses)** (Impact: 84.8)
    * *Intent:* /// Emits code required to represent [c] as a series of statements in [body]. /// /// [properties] h...
  * `_emitBinaryOperator` **(Many-Argument Workhorses)** (Impact: 70.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 359 instances
* *Concurrency (weighted view):* 125
* *State Mutation (weighted view):* 1234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1464`, `structural_boundaries: 2122`, `args: 534`, `func_start: 433`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 128`, `state_mutation: 516`, `dead_code: 26`, `planned_debt: 111`, `fragile_debt: 3`
* *Architecture:* `api: 116`, `concurrency: 25`, `import: 41`
* *Defense:* `safety: 517`, `doc: 974`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.064
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 36):` options.dart, js_names.dart, js_utils.dart, module_builder.dart, module_containers.dart, rewrite_async.dart, js_ast.dart, source_map_printer.dart...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pkg/front_end/lib/src/kernel/body_builder.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.455)
- **Top Global Matches:** file_cluster_4: 8.455, file_cluster_12: 11.949, file_cluster_6: 13.109
- **Magnitude:** 7044.2 | **LOC:** 11556 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 47.6%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **78**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.2%), Connectivity (formerly Api Exposure) (72.7%), Guard Balance (formerly Safety Score) (47.1%)
- **Documentation Coverage:** 92.3634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveAndBuildConstructorInvocation` **(Many-Argument Workhorses)** (Impact: 531.8)
  * `processLookupResult` **(Many-Argument Workhorses)** (Impact: 318.2)
  * `endFormalParameter` **(Many-Argument Workhorses)** (Impact: 192.6)
  * `endSwitchCase` **(Many-Argument Workhorses)** (Impact: 157.3)
  * `beginSwitchCase` **(Many-Argument Workhorses)** (Impact: 112.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 437 instances
* *State Mutation (weighted view):* 1380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1919`, `structural_boundaries: 366`, `args: 436`, `func_start: 407`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 506`, `dead_code: 10`, `planned_debt: 57`
* *Architecture:* `api: 240`, `import: 78`
* *Defense:* `safety: 1169`, `doc: 163`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 81):` experimental_flags.dart, lowering_predicates.dart, compiler_context.dart, constant_context.dart, crash.dart, extension_scope.dart, identifiers.dart, label_scope.dart...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pkg/dev_compiler/lib/src/kernel/compiler.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.885)
- **Top Global Matches:** file_cluster_4: 11.885, file_cluster_12: 13.494, file_cluster_5: 14.674
- **Magnitude:** 6926.46 | **LOC:** 9287 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **37**; blast radius 0.071; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Concurrency Surface (formerly Concurrency) (37.9%)
- **Documentation Coverage:** 69.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Compiler` **(Stateful Encapsulated Methods)** (Impact: 1858.2)
  * `visitStaticInvocation` **(Compute Cores)** (Impact: 132.5)
  * `_defineClass` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `_emitClassSignature` **(Many-Argument Workhorses)** (Impact: 88.2)
    * *Intent:* /// Emit the signature on the class recording the runtime type information
  * `_emitBinaryOperator` **(Many-Argument Workhorses)** (Impact: 70.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 358 instances
* *Concurrency (weighted view):* 125
* *State Mutation (weighted view):* 1214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1419`, `structural_boundaries: 1998`, `args: 521`, `func_start: 414`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 498`, `dead_code: 10`, `planned_debt: 104`, `fragile_debt: 3`
* *Architecture:* `api: 110`, `concurrency: 25`, `import: 38`
* *Defense:* `safety: 486`, `doc: 866`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 34):` options.dart, js_names.dart, js_utils.dart, module_builder.dart, module_containers.dart, rewrite_async.dart, js_ast.dart, source_map_printer.dart...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pkg/front_end/lib/src/util/parser_ast_helper.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 11.713)
- **Top Global Matches:** file_cluster_0: 11.713, file_cluster_10: 12.766, file_cluster_13: 13.207
- **Magnitude:** 6542.22 | **LOC:** 14214 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **12**; blast radius 0.054; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Connectivity (formerly Api Exposure) (91.5%), Concurrency Surface (formerly Concurrency) (64.9%), Guard Balance (formerly Safety Score) (39.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `beginClassDeclaration` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `beginNamedMixinApplication` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `beginConstructor` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `endFields` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `beginMethod` **(Many-Argument Workhorses)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 708`, `structural_boundaries: 1907`, `args: 1879`, `func_start: 2637`, `class_start: 382`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `duplicate_logic: 237`
* *Architecture:* `api: 755`, `concurrency: 379`, `import: 12`
* *Defense:* `safety: 1247`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 12):` messages.dart, flags.dart, assert.dart, block_kind.dart, constructor_reference_context.dart, declaration_kind.dart, formal_parameter_kind.dart, identifier_context.dart...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `pkg/analyzer/test/src/summary/elements/class_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.063)
- **Top Global Matches:** file_cluster_13: 6.063, file_cluster_2: 8.589, file_cluster_11: 8.905
- **Magnitude:** 6423.36 | **LOC:** 35775 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.015; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.3%), Connectivity (formerly Api Exposure) (88.6%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.0%)
- **Documentation Coverage:** 99.0449% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `async` **(Annotated & Test Methods)** (Impact: 14.6)
  * `async` **(Annotated & Test Methods)** (Impact: 14.2)
  * `async` **(Annotated & Test Methods)** (Impact: 10.0)
  * `async` **(I/O & Config Routines)** (Impact: 8.8)
  * `async` **(Annotated & Test Methods)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 139 instances
* *Concurrency (weighted view):* 1889
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12245`, `args: 892`, `func_start: 1061`, `class_start: 1405`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 91`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 1389`, `concurrency: 1194`, `import: 48`
* *Defense:* `safety: 199`, `doc: 95`, `test: 13`, `immutability_locks: 268`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.015
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 6):` node_text_expectations.dart, elements_base.dart, a.dart, a1.dart, a11.dart, a12.dart, a2.dart, a21.dart...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `runtime/vm/compiler/backend/il_riscv.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.383)
- **Top Global Matches:** file_cluster_4: 9.383, file_cluster_6: 10.733, file_cluster_15: 15.565
- **Magnitude:** 6266.98 | **LOC:** 7122 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.5%), Complexity Load (formerly Cognitive Load) (20.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConstantInstr::EmitMoveToLocation` **(Many-Argument Workhorses)** (Impact: 3065.9)
  * `BinarySmiOpInstr::EmitNativeCode` **(Compute Cores)** (Impact: 155.6)
  * `StoreIndexedInstr::EmitNativeCode` **(Compute Cores)** (Impact: 89.5)
  * `BinaryInt64OpInstr::EmitNativeCode` **(Compute Cores)** (Impact: 78.9)
  * `BinaryInt32OpInstr::EmitNativeCode` **(Compute Cores)** (Impact: 77.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1375`, `structural_boundaries: 345`, `args: 737`, `func_start: 222`, `class_start: 4`
* *Risk/State:* `state_mutation: 64`, `dead_code: 13`, `planned_debt: 46`, `unreferenced_by_name: 183`
* *Architecture:* `api: 4`, `import: 19`
* *Defense:* `safety: 5`, `test: 2`, `immutability_locks: 602`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 39):` memory_sanitizer.h, flow_graph.h, flow_graph_compiler.h, il.h, locations.h, locations_helpers.h, range_analysis.h, native_calling_convention.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/analysis_server/test/lsp/completion_dart_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.292)
- **Top Global Matches:** file_cluster_12: 9.292, file_cluster_10: 11.284, file_cluster_15: 11.296
- **Magnitude:** 5583.64 | **LOC:** 5793 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **69**; blast radius 0.014; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (82.6%), Guard Balance (formerly Safety Score) (49.7%), Complexity Load (formerly Cognitive Load) (41.6%)
- **Documentation Coverage:** 94.1463% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_completionTrigger_brace_string` **(I/O & Config Routines)** (Impact: 150.0)
  * `test_completionTrigger_brace_rawString` **(I/O & Config Routines)** (Impact: 119.1)
  * `test_completionTrigger_brace_interpolatedStringExpression` **(I/O & Config Routines)** (Impact: 119.0)
  * `expectLabels` **(Defensive Guards)** (Impact: 33.3)
    * *Intent:* /// Expect that invoking completion at the position marked in [content] in /// [completionFileUri] p...
  * `expectLabel` **(Defensive Guards)** (Impact: 25.2)
    * *Intent:* /// A helper for [expectLabels] that only verifies a single label.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 404 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 3037
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 1478`, `args: 625`, `func_start: 862`, `class_start: 155`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 214`, `planned_debt: 5`, `fragile_debt: 4`, `duplicate_logic: 247`
* *Architecture:* `io: 5`, `api: 577`, `concurrency: 1017`, `import: 139`
* *Defense:* `safety: 112`, `doc: 76`, `test: 268`, `sync_locks: 8`, `immutability_locks: 27`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 36):` imported.dart, other_file.dart, matchers.dart, matchers.dart, test_code_extensions.dart, ^, a.dart, b.dart...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `runtime/vm/app_snapshot.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.0)
- **Top Global Matches:** file_cluster_15: 10.0, file_cluster_4: 11.28, file_cluster_16: 11.294
- **Magnitude:** 5510.56 | **LOC:** 10298 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **32**; blast radius 0.019; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (88.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Serializer::NewClusterForClass` **(Many-Argument Workhorses)** (Impact: 141.3)
  * `Deserializer::ReadCluster` **(Compute Cores)** (Impact: 84.5)
  * `WriteFill` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `Serializer::CreateArtificialNodeIfNeeded` **(Compute Cores)** (Impact: 57.7)
    * *Intent:* #if !defined(DART_PRECOMPILED_RUNTIME)
  * `Serializer::PrepareInstructions` **(Compute Cores)** (Impact: 54.4)
    * *Intent:* #endif // defined(DART_PRECOMPILER)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 632 instances
* *State Mutation (weighted view):* 2019
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1102`, `structural_boundaries: 1096`, `args: 1074`, `func_start: 764`, `class_start: 135`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 755`, `planned_debt: 23`, `duplicate_logic: 24`, `unreferenced_by_name: 190`
* *Architecture:* `api: 125`, `import: 32`
* *Defense:* `safety: 129`, `test: 11`, `immutability_locks: 635`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 64):` memory, assert.h, utility, app_snapshot.h, bootstrap.h, bss_relocs.h, canonical_tables.h, class_id.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `runtime/vm/compiler/backend/il.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.59)
- **Top Global Matches:** file_cluster_4: 7.59, file_cluster_15: 10.787, file_cluster_16: 11.906
- **Magnitude:** 5296.94 | **LOC:** 9109 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **42**; blast radius 0.044; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.2%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BinaryIntegerOpInstr::Canonicalize` **(Compute Cores)** (Impact: 152.5)
  * `LoadFieldInstr::Canonicalize` **(Compute Cores)** (Impact: 134.2)
  * `FfiCallInstr::EmitParamMoves` **(Many-Argument Workhorses)** (Impact: 84.3)
  * `SimdOpInstr::KindForOperator` **(Compute Cores)** (Impact: 54.6)
  * `StoreFieldInstr::EmitNativeCode` **(Compute Cores)** (Impact: 54.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 325 instances
* *Memory Alloc (weighted view):* 115
* *State Mutation (weighted view):* 994
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1968`, `structural_boundaries: 1139`, `args: 780`, `func_start: 472`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 344`, `planned_debt: 72`, `unreferenced_by_name: 415`
* *Architecture:* `api: 2`, `import: 42`
* *Defense:* `safety: 2`, `test: 8`, `immutability_locks: 697`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 79):` assert.h, globals.h, bit_vector.h, bootstrap.h, code_entry_kind.h, dispatch_table_generator.h, object_pool_builder.h, code_statistics.h...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `tests/standalone/io/certificates/bad_server_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key_malformed.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client2_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.014
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` n/a
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pkg/perf_witness/lib/recorder.dart` (DART) | Magnitude: 217.98 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 303, structural_boundaries: 58, concurrency: 45, branch: 44
- `pkg/analysis_server/lib/src/server/crash_reporting.dart` (DART) | Magnitude: 40.28 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 67, branch: 13, structural_boundaries: 10, safety: 10
- `runtime/tests/vm/dart/isolates/shared_fail_without_flag_test.dart` (DART) | Magnitude: 32.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 14, import: 9, core_var_decl: 9
- `pkg/analysis_server/lib/src/services/user_prompts/user_prompts.dart` (DART) | Magnitude: 53.46 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, doc: 39, structural_boundaries: 33, safety: 20
- `pkg/front_end/testcases/nnbd/constants.dart` (DART) | Magnitude: 9.54 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, immutability_locks: 23, core_var_decl: 23, globals: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `pkg/analysis_server/lib/src/services/completion/postfix/postfix_completion.dart` (DART) | Magnitude: 347.5 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 553, structural_boundaries: 155, branch: 86, safety: 79
- `pkg/dart2bytecode/lib/recognized_methods.dart` (DART) | Magnitude: 50.94 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 86, branch: 19, structural_boundaries: 19, core_var_decl: 8
- `pkg/linter/test/rules/cancel_subscriptions_test.dart` (DART) | Magnitude: 501.9 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 140, concurrency: 110, structural_boundaries: 55, func_start: 55
- `tests/lib/html/xhr_cross_origin_test.dart` (DART) | Magnitude: 44.18 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 34, core_var_decl: 20, concurrency: 18
- `tests/lib/isolate/deferred_in_isolate2_test.dart` (DART) | Magnitude: 21.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 7, concurrency: 7, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pkg/compiler/test/codesize/swarm/ConfigHintDialog.dart` (DART) | Magnitude: 10.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 4, args: 4, func_start: 4
- `tests/hot_reload/mixin_changed/main.0.dart` (DART) | Magnitude: 13.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, branch: 3, func_start: 3
- `tests/hot_reload/mixin_changed/main.1.dart` (DART) | Magnitude: 13.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, branch: 3, func_start: 3
- `tests/language/invalid_returns/async_invalid_return_40_test.dart` (DART) | Magnitude: 10.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: concurrency: 5, indent_spaces: 4, structural_boundaries: 3, api: 3
- `tests/language/invalid_returns/async_invalid_return_52_test.dart` (DART) | Magnitude: 10.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: concurrency: 5, indent_spaces: 4, structural_boundaries: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pkg/analysis_server/test/lsp_over_legacy/implementation_test.dart` (DART) | Magnitude: 10.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, import: 5, api: 4
- `pkg/_fe_analyzer_shared/lib/src/parser/type_info.dart` (DART) | Magnitude: 348.34 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 327, branch: 111, doc: 97, structural_boundaries: 58
- `pkg/front_end/lib/src/fragment/factory/body_builder_context.dart` (DART) | Magnitude: 49.96 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 23, func_start: 15, api: 15
- `pkg/front_end/test/tool/reload.dart` (DART) | Magnitude: 117.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 43, concurrency: 35, doc: 34
- `pkg/analyzer/lib/src/dart/micro/analysis_context.dart` (DART) | Magnitude: 79.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 61, func_start: 24, decorators: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pkg/linter/lib/src/rules/avoid_init_to_null.dart` (DART) | Magnitude: 37.76 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 23, branch: 14, import: 11
- `tests/language/instance/field_initializer_test.dart` (DART) | Magnitude: 14.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 16, args: 11, func_start: 9, structural_boundaries: 4
- `pkg/front_end/test/language_versioning/data/parts_agreeing/main.dart` (DART) | Magnitude: 2.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1
- `pkg/front_end/test/language_versioning/data/parts_agreeing_two_versions/main.dart` (DART) | Magnitude: 2.16 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1
- `tests/language/constructor/name_clash_test.dart` (DART) | Magnitude: 4.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `pkg/front_end/parser_testcases/record/record_literal_04.dart` (DART) | Magnitude: 5.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: immutability_locks: 7, core_var_decl: 7, design_snake_case: 7, structural_boundaries: 6
- `pkg/compiler/tool/kernel_visitor/test/info_visitor_test.dart` (DART) | Magnitude: 25.46 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 30, safety_bypasses: 17, closures: 12
- `pkg/compiler/test/impact/data/injected_cast.dart` (DART) | Magnitude: 115.08 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: branch: 31, safety: 31, indent_spaces: 31, structural_boundaries: 24
- `pkg/front_end/testcases/patterns/coercion_in_if_case_element.dart` (DART) | Magnitude: 27.0 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 17, branch: 8, safety: 6, safety_bypasses: 5
- `tests/web/internal/rti/runtime_type_2_test.dart` (DART) | Magnitude: 6.08 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 12, generics: 7, safety_bypasses: 6, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `runtime/vm/signal_handler_android.cc` (CPP) | Magnitude: 52.26 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 46, macros: 37, pointers: 34, args: 31
- `pkg/kernel/lib/verifier.dart` (DART) | Magnitude: 1251.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1898, branch: 435, structural_boundaries: 200, safety: 199
- `pkg/analysis_server/lib/src/cider/local_library_contributor.dart` (DART) | Magnitude: 135.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 204, branch: 64, structural_boundaries: 34, func_start: 16
- `pkg/_fe_analyzer_shared/test/flow_analysis/definite_assignment/data/binary_expression.dart` (DART) | Magnitude: 20.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, safety: 10, structural_boundaries: 8, args: 8
- `pkg/analysis_server/tool/code_completion/flutter_metrics.dart` (DART) | Magnitude: 137.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 72, core_var_decl: 41, doc: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pkg/analyzer/lib/src/summary2/library_builder.dart` (DART) | Magnitude: 575.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 807, structural_boundaries: 209, branch: 137, core_var_decl: 129
- `sdk/lib/_internal/vm/bin/sync_socket_patch.dart` (DART) | Magnitude: 207.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 284, structural_boundaries: 60, branch: 58, func_start: 41
- `pkg/dartdev/lib/src/sdk_cache.dart` (DART) | Magnitude: 210.7 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 261, safety: 49, branch: 45, structural_boundaries: 44
- `tests/language/nnbd/try_catch/default_catch_type_error_test.dart` (DART) | Magnitude: 4.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, args: 2, func_start: 2, safety: 2
- `pkg/analysis_server/lib/src/utilities/import_analyzer.dart` (DART) | Magnitude: 224.94 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 282, structural_boundaries: 84, branch: 83, doc: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkg/analyzer/lib/src/diagnostic/diagnostic_code_values.dart` (DART) | Magnitude: 12.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, import: 4, reflection_metaprogramming: 1
- `runtime/vm/constants_x86.h` (CPP) | Magnitude: 6.4 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 105, core_var_decl: 27, design_upper_case: 26, bitwise_ops: 9
- `tests/language/string/const_interpolation2_test.dart` (DART) | Magnitude: 3.78 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 52, core_var_decl: 45, design_snake_case: 45, indent_spaces: 42
- `tests/language/dot_shorthands/simple/simple_identifier_error_test.dart` (DART) | Magnitude: 3.66 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, core_var_decl: 5, structural_boundaries: 3, design_snake_case: 3
- `tests/language/mixin_constructor_forwarding/const_constructor_with_field_error_test.dart` (DART) | Magnitude: 19.84 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: func_start: 13, indent_spaces: 13, unreferenced_by_name: 13, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeQuestion.dart` (DART) | Magnitude: 8.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 4, indent_spaces: 3, safety: 2, args: 1
- `pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeQuestion.dart` (DART) | Magnitude: 8.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 4, indent_spaces: 3, safety: 2, args: 1
- `pkg/front_end/testcases/inference/infer_parameter_type_setter_from_setter.dart` (DART) | Magnitude: 6.26 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, args: 3, func_start: 3, class_start: 2
- `tests/web/super_constructor2_test.dart` (DART) | Magnitude: 7.8 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, func_start: 3, class_start: 3
- `tests/language/super/call3_test.dart` (DART) | Magnitude: 14.98 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, func_start: 7, class_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pkg/vm/lib/transformations/no_dynamic_invocations_annotator.dart` (DART) | Magnitude: 172.9 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 178, branch: 40, structural_boundaries: 25, func_start: 22
- `pkg/analysis_server_plugin/lib/src/correction/ignore_diagnostic.dart` (DART) | Magnitude: 146.34 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 201, structural_boundaries: 86, core_var_decl: 52, branch: 36
- `pkg/analyzer/tool/generators/ast_generator.dart` (DART) | Magnitude: 696.58 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 966, structural_boundaries: 327, branch: 220, core_var_decl: 130
- `pkg/linter/lib/src/rules/prefer_const_constructors_in_immutables.dart` (DART) | Magnitude: 104.1 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 106, branch: 50, structural_boundaries: 45, safety: 26
- `tools/dom/scripts/emitter.py` (PYTHON) | Magnitude: 0.34 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 170, state_mutation: 66, branch: 56, structural_boundaries: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `pkg/compiler/lib/src/js_emitter/native_emitter.dart` (DART) | Magnitude: 263.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 161, branch: 65, structural_boundaries: 60, core_var_decl: 35
- `tests/language/covariant/subtyping_unsafe_call2_test.dart` (DART) | Magnitude: 6.58 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, args: 3, func_start: 3
- `pkg/front_end/lib/src/kernel/dynamic_module_validator.dart` (DART) | Magnitude: 595.54 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 840, branch: 158, structural_boundaries: 131, args: 94
- `pkg/vm_service/test/pause_on_start_and_exit_test.dart` (DART) | Magnitude: 21.06 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, concurrency: 10, structural_boundaries: 9, core_var_decl: 9
- `tests/standalone/io/https_client_certificate_test.dart` (DART) | Magnitude: 8.68 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 7, closures: 7, io: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `pkg/front_end/test/comments_on_certain_arguments_tool.dart` (DART) | Magnitude: 322.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 362, branch: 86, core_var_decl: 62, structural_boundaries: 59
- `runtime/vm/regexp/regexp.cc` (CPP) | Magnitude: 267.12 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 342, pointers: 84, branch: 61, immutability_locks: 51
- `pkg/analyzer/lib/src/dart/resolver/type_property_resolver.dart` (DART) | Magnitude: 382.62 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 307, core_var_decl: 89, branch: 74, state_mutation: 65
- `pkg/analyzer/lib/src/dart/resolver/function_expression_resolver.dart` (DART) | Magnitude: 120.86 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 47, branch: 37, core_var_decl: 23
- `pkg/vm/lib/modular/transformations/ffi/definitions.dart` (DART) | Magnitude: 567.4 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 987, branch: 191, core_var_decl: 143, structural_boundaries: 106

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/lib/html/js_interop_1_test.dart` (DART) | Magnitude: 49.98 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, concurrency: 9, structural_boundaries: 7, sync_locks: 5
- `pkg/analysis_server/lib/src/utilities/file_string_sink.dart` (DART) | Magnitude: 12.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 20, args: 5, func_start: 5, decorators: 4
- `pkg/analysis_server/test/lsp/definition_test.dart` (DART) | Magnitude: 823.42 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 936, structural_boundaries: 459, concurrency: 379, func_start: 316
- `pkg/analyzer/test/src/ignore_comments/ignore_info_test.dart` (DART) | Magnitude: 123.04 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 72, concurrency: 59, args: 38
- `pkg/compiler/test/codesize/swarm/swarm_ui_lib/touch/ClickBuster.dart` (DART) | Magnitude: 136.58 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 96, doc: 43, branch: 20, core_var_decl: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/_fe_analyzer_shared/test/exhaustiveness/data/null_assert.dart` (DART) | Magnitude: 73.18 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 29, branch: 27, closures: 9
- `tests/language/least_upper_bound/least_upper_bound_test.dart` (DART) | Magnitude: 93.44 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, branch: 32, safety: 32, core_var_decl: 18
- `pkg/front_end/tool/benchmarker_golem.dart` (DART) | Magnitude: 82.88 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 96, branch: 17, state_mutation: 14, safety: 5
- `tests/language/exception/try_catch_optimized5_test.dart` (DART) | Magnitude: 67.46 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, branch: 18, panics_and_aborts: 16, state_mutation: 9
- `runtime/tools/run_clang_tidy.dart` (DART) | Magnitude: 0.09 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 206, core_var_decl: 22, debug_prints: 15, structural_boundaries: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pkg/front_end/lib/src/type_inference/inference_visitor.dart` -> Churn: **100.0%** | Cog Load: 51.6564% | Debt: 8.6357%
- `pkg/analyzer/lib/src/generated/error_verifier.dart` -> Churn: **88.24%** | Cog Load: 8.4763% | Debt: 54.2842%
- `pkg/analyzer/lib/src/dart/resolver/resolution_visitor.dart` -> Churn: **78.55%** | Cog Load: 34.8781% | Debt: 99.9766%
- `pkg/vm/lib/transformations/record_use/record_instance.dart` -> Churn: **78.23%** | Cog Load: 6.8065% | Debt: 97.1877%
- `pkg/vm/lib/transformations/record_use/record_call.dart` -> Churn: **76.98%** | Cog Load: 8.7378% | Debt: 84.1131%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pkg/analyzer/test/src/dart/analysis/driver_test.dart` -> **Konstantin Shcheglov** (100.0% isolated ownership) | Magnitude: 27349.62
- `pkg/dart_runtime_service/test/web/sse_smoke_driver.dart.js` -> **Ben Konyi** (100.0% isolated ownership) | Magnitude: 10629.92
- `pkg/analysis_server/test/services/completion/dart/completion_test.dart` -> **Brian Wilkerson** (100.0% isolated ownership) | Magnitude: 9316.96
- `pkg/analysis_server_client/lib/src/protocol/protocol_generated.dart` -> **Paul Berry** (100.0% isolated ownership) | Magnitude: 9156.52
- `pkg/analyzer/test/src/summary/elements/class_test.dart` -> **Konstantin Shcheglov** (100.0% isolated ownership) | Magnitude: 6423.36

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/standalone/dwarf_stack_trace_test.dart` -> **Severity: 2443.6** (Blast Radius: 24.436 * Doc Risk: 100.0%)
- `tests/standalone/io/process_check_arguments_script.dart` -> **Severity: 2321.0** (Blast Radius: 23.21 * Doc Risk: 100.0%)
- `pkg/vm/testcases/transformations/deferred_loading/h.dart` -> **Severity: 1749.3** (Blast Radius: 17.493 * Doc Risk: 100.0%)
- `pkg/expect/lib/expect.dart` -> **Severity: 1360.4** (Blast Radius: 44.339 * Doc Risk: 30.6818%)
- `pkg/vm/testcases/transformations/deferred_loading/g.dart` -> **Severity: 1331.9** (Blast Radius: 13.319 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 18822 literal sites + 984 sites through wrappers = 19806
- **`memory_alloc`:** 4340 literal sites + 201 sites through wrappers = 4541
- **`panics_and_aborts`:** 24118 literal sites + 2110 sites through wrappers = 26228

- `f` (function, panics_and_aborts, primitive): 252 call sites in 1 files -- `pkg/front_end/testcases/nnbd/numbers_inferred.dart`
- `usageException` (function, debug_prints, primitive): 72 call sites in 30 files -- `pkg/dart2js_info/bin/src/usage_exception.dart`
- `usageException` (function, panics_and_aborts, primitive): 72 call sites in 30 files -- `pkg/dart2js_info/bin/src/usage_exception.dart`
- `kast` (function, panics_and_aborts, primitive): 49 call sites in 1 files -- `tests/language/optimize/inline_throw_test.dart`
- `unknown` (function, debug_prints, primitive): 42 call sites in 1 files -- `pkg/native_compiler/test/back_end/arm64/disassembler.dart`
- `_fail` (function, panics_and_aborts, primitive): 39 call sites in 1 files -- `pkg/expect/lib/expect.dart`
- `_reportError` (function, panics_and_aborts, primitive): 39 call sites in 1 files -- `pkg/_fe_analyzer_shared/lib/src/util/libraries_specification.dart`
- `error` (function, panics_and_aborts, primitive): 35 call sites in 1 files -- `pkg/js_ast/lib/src/builder.dart`
- `deconstruct` (function, panics_and_aborts, primitive): 32 call sites in 1 files -- `tests/language/nnbd/top_merge/top_merge_interfaces_direct_error_test.dart`
- `deconstruct` (function, panics_and_aborts, primitive): 32 call sites in 1 files -- `tests/language/nnbd/top_merge/top_merge_interfaces_mixin_error_test.dart`
- `error` (function, panics_and_aborts, primitive): 31 call sites in 1 files -- `pkg/dev_compiler/lib/src/js_ast/builder.dart`
- `f` (function, panics_and_aborts, primitive): 30 call sites in 1 files -- `pkg/front_end/testcases/inference_new/infer_assign_to_index_full.dart`
*(+907 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 735519 call pairs -- scoped 50.1%, unique 1.0%, ambiguous 28.9%, external 20.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| dart | 552483 | 54.5% | 0.0% | 28.7% | 16.8% |
| cpp | 170673 | 38.0% | 4.3% | 30.8% | 26.9% |
| javascript | 5127 | 18.7% | 0.0% | 2.7% | 78.5% |
| python | 5058 | 25.0% | 0.0% | 12.3% | 62.6% |
| java | 1857 | 18.7% | 1.2% | 26.7% | 53.5% |
| shell | 192 | 17.7% | 1.0% | 0.0% | 81.2% |
| html | 82 | 17.1% | 0.0% | 0.0% | 82.9% |
| c | 44 | 2.3% | 52.3% | 0.0% | 45.5% |
| assembly | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
