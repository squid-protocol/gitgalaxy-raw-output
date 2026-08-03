# ARCHITECTURAL_BRIEF: sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/sdk` |
| **Timestamp** | `2026-08-03T21:36:34.379738+00:00` |
| **Scan Duration** | `66.46s` |
| **Git Branch** | `main` |
| **Git Commit** | `eb59896079d9cda5351c2f713a22be89b9f9562c` |
| **Git Remote** | `https://github.com/dart-lang/sdk` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 11658 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 54062 |
| Analyzed Artifacts (Scanned) | 12745 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 41317 |
| Total LOC | 1854033 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 23.6% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.223 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 385 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| DART | 10509 | 1499302 | 82.5% |
| CPP | 909 | 286511 | 7.1% |
| YAML | 590 | 16609 | 4.6% |
| MARKDOWN | 231 | 0 | 1.8% |
| PLAINTEXT | 153 | 27 | 1.2% |
| PYTHON | 125 | 22467 | 1.0% |
| JSON | 55 | 698 | 0.4% |
| SHELL | 38 | 1679 | 0.3% |
| JAVA | 38 | 1104 | 0.3% |
| XML | 28 | 0 | 0.2% |
| HTML | 16 | 8268 | 0.1% |
| JAVASCRIPT | 11 | 11859 | 0.1% |
| ASSEMBLY | 10 | 508 | 0.1% |
| C | 8 | 580 | 0.1% |
| MAKEFILE | 6 | 202 | 0.0% |
| BATCH | 6 | 97 | 0.0% |
| PROTO | 5 | 326 | 0.0% |
| CSS | 3 | 2892 | 0.0% |
| OBJECTIVE-C | 1 | 18 | 0.0% |
| CSV | 1 | 449 | 0.0% |
| PHP | 1 | 1 | 0.0% |
| M4 | 1 | 436 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.234`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3599 | 28.2% |
| file_cluster_13 | 2949 | 23.1% |
| file_cluster_9 | 1683 | 13.2% |
| file_cluster_0 | 1229 | 9.6% |
| file_cluster_4 | 1167 | 9.2% |
| file_cluster_17 | 681 | 5.3% |
| file_cluster_11 | 461 | 3.6% |
| file_cluster_16 | 424 | 3.3% |
| file_cluster_15 | 92 | 0.7% |
| file_cluster_6 | 54 | 0.4% |
| Unknown | 27 | 0.2% |
| file_cluster_2 | 15 | 0.1% |
| file_cluster_7 | 4 | 0.0% |
| file_cluster_12 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 358 | 2.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 41317*

**Composition by Extension & Reason:**
- `.expect`: 24375x Excluded (Unsupported Extension: '.expect'), 914x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dart`: 13648x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 164x Excluded: Neighborhood Micro-Mass Limit Exceeded, 13x Excluded (Lexical Monotony: High structural repetition detected in 4112 LOC)
- `no_extension`: 173x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 122x Unsupported Format (.darttemplate), 27x Excluded (Unsupported Extension: '.outline_extracted')
- `.yaml`: 215x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2780 LOC), 1x Excluded (Massive Static Asset Blob: 3889 LOC)
- `.options`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 85x Excluded (Unsupported Extension: '.options')
- `.cc`: 164x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 25462 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1024 LOC)
- `.json`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3380 LOC), 1x Excluded (Massive Static Asset Blob: 3598 LOC)
- `.md`: 126x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC), 1x Excluded (Machine-Generated Source Code Signature: 215 LOC)
- `.html`: 112x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gni`: 82x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.gni), 10x Excluded (Unsupported Extension: '.gni')
- `.status`: 43x Excluded (Unsupported Extension: '.status'), 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.crash_dart`: 67x Excluded (Unsupported Extension: '.crash_dart')
- `.golden`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5096 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2167 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.1 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 19.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.1 | 1.7 | 0.0 |
| API Exposure | 0.0 | 20.0 | 3.8 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 15.9 | 17.0 | 23.1 |
| Specification Exposure | 0.0 | 100.0 | 80.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.8 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.7 | 13.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pkg/analysis_server/doc/api.html` (Hits: 975)
- `pkg/analyzer_plugin/doc/api.html` (Hits: 355)
- `pkg/analysis_server/lib/src/services/correction/fix.dart` (Hits: 150)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **h.dart** (`pkg/vm/testcases/transformations/deferred_loading/h.dart`) — 886 inbound connections
2. **context_collection_resolution.dart** (`pkg/analyzer/test/src/dart/resolution/context_collection_resolution.dart`) — 104 inbound connections
3. **models.dart** (`pkg/analyzer/tool/fine/ab_mutate/models.dart`) — 87 inbound connections
4. **memory.dart** (`pkg/wasm_builder/lib/src/ir/memory.dart`) — 75 inbound connections
5. **stdio.h** (`runtime/bin/stdio.h`) — 39 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_all.dart** (`pkg/analyzer/test/src/diagnostics/test_all.dart`) — 623 outbound dependencies
2. **test_all.dart** (`pkg/analysis_server/test/src/services/correction/fix/test_all.dart`) — 277 outbound dependencies
3. **fix_internal.dart** (`pkg/analysis_server/lib/src/services/correction/fix_internal.dart`) — 263 outbound dependencies
4. **rules.dart** (`pkg/linter/lib/src/rules.dart`) — 256 outbound dependencies
5. **legacy_analysis_server.dart** (`pkg/analysis_server/lib/src/legacy_analysis_server.dart`) — 115 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `InlineTypedDataIndexCheck` (@ `runtime/vm/compiler/call_specializer.cc`) -> Impact: **3566.9** | LOC: 358
- `EmitNativeCode` (@ `runtime/vm/compiler/backend/il_x64.cc`) -> Impact: **3551.9** | LOC: 1445
- `BlockEntryInstr::FindOsrEntryRecursive` (@ `runtime/vm/compiler/backend/il.cc`) -> Impact: **3440.3** | LOC: 1657
- `_visitExpression` (@ `pkg/dev_compiler/lib/src/kernel/compiler_new.dart`) -> Impact: **3231.0** | LOC: 1786
- `RELEASE_ASSERT` (@ `runtime/vm/debugger.cc`) -> Impact: **3181.4** | LOC: 1657
- `null` (@ `pkg/analyzer/lib/src/fine/requirements.dart`) -> Impact: **3139.3** | LOC: 1644
- `visitDeclaredVariablePattern` (@ `pkg/analysis_server/lib/src/services/completion/dart/in_scope_completion_pass.dart`) -> Impact: **2987.8** | LOC: 1560
- `context` (@ `pkg/front_end/lib/src/type_inference/inference_visitor_base.dart`) -> Impact: **2813.3** | LOC: 1533
- `Service::PostEvent` (@ `runtime/vm/service.cc`) -> Impact: **2757.3** | LOC: 1623
- `InferredTypeListener` (@ `pkg/front_end/lib/src/source/source_extension_type_declaration_builder.dart`) -> Impact: **2743.2** | LOC: 1031

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_CheckFormat` (@ `PRESUBMIT.py`) -> **O(2^N) [Recursive]**
- `CheckSorted` (@ `pkg/analyzer/PRESUBMIT.py`) -> **O(2^N) [Recursive]**
- `CreateAvd` (@ `runtime/tools/android_finder.py`) -> **O(2^N) [Recursive]**
- `ParseAndroidListSdkResult` (@ `runtime/tools/android_finder.py`) -> **O(2^N) [Recursive]**
- `WriteBytesAsText` (@ `runtime/tools/create_snapshot_file.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Writes byte contents of the input_file into out file as text. Output is formatted as a list of comma separated integer values - one value for each ...
- `makeString` (@ `runtime/tools/create_string_literal.py`) -> **O(2^N) [Recursive]**
- `generate_dart` (@ `runtime/tools/dartfuzz/minimize.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # If the new_mask has new bits and has not been tested yet. # We need to check both because only masks that produce an
- `NotifyBuildDone` (@ `tools/build.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `tools/dom/new_scripts/compiler.py`) -> **O(2^N) [Recursive]**
- `GenerateFromDatabase` (@ `tools/dom/scripts/dartdomgenerator.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `FlowGraphBuilder::BuildGraphOfRecognized` (@ `runtime/vm/compiler/frontend/kernel_to_il.cc`) -> DB Complexity: **618**
- `StreamingFlowGraphBuilder::BuildGraphOfF` (@ `runtime/vm/compiler/frontend/kernel_binary_flowgraph.cc`) -> DB Complexity: **602**
- `Service::PostEvent` (@ `runtime/vm/service.cc`) -> DB Complexity: **489**
- `StreamingFlowGraphBuilder::BuildAssertSt` (@ `runtime/vm/compiler/frontend/kernel_binary_flowgraph.cc`) -> DB Complexity: **480**
- `FlowGraphAllocator::ConnectOutgoingPhiMo` (@ `runtime/vm/compiler/backend/linearscan.cc`) -> DB Complexity: **426**
- `VariableLivenessAnalysis::ComputeInitial` (@ `runtime/vm/compiler/backend/flow_graph.cc`) -> DB Complexity: **385**
- `StrengthenAlignment` (@ `runtime/vm/compiler/backend/il.cc`) -> DB Complexity: **340**
- `BlockEntryInstr::FindOsrEntryRecursive` (@ `runtime/vm/compiler/backend/il.cc`) -> DB Complexity: **338**
- `CanShareObject` (@ `runtime/vm/object_graph_copy.cc`) -> DB Complexity: **319**
- `Precompiler::DoCompileAll` (@ `runtime/vm/compiler/aot/precompiler.cc`) -> DB Complexity: **306**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `runtime/vm` | 374 | 143405.75 | 54.98% | 62.89% |
| `tests/standalone/io/certificates` | 25 | 120001.42 | 0.0% | 0.0% |
| `runtime/vm/compiler/backend` | 58 | 97061.12 | 64.65% | 69.51% |
| `pkg/analyzer/test/src/diagnostics` | 623 | 56010.16 | 21.96% | 0.0% |
| `runtime/bin` | 211 | 49691.84 | 50.37% | 59.84% |
| `pkg/analysis_server/test/src/services/correction/fix` | 275 | 38806.86 | 44.58% | 0.0% |
| `runtime/vm/compiler/assembler` | 22 | 35389.36 | 72.35% | 83.14% |
| `pkg/analyzer/test/src/dart/resolution` | 109 | 27032.3 | 19.76% | 0.0% |
| `pkg/analysis_server/lib/src/services/correction/dart` | 306 | 26237.46 | 24.06% | 16.95% |
| `pkg/analyzer/test/src/fasta/recovery/partial_code` | 32 | 26127.2 | 3.77% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.agents/skills/read_gerrit_cl/scripts/read_comments.sh` -> **100.0%** Exposure
- `.agents/skills/read_gerrit_cl/scripts/read_patch.sh` -> **100.0%** Exposure
- `pkg/analyzer/tool/fasta_migration_progress.sh` -> **100.0%** Exposure
- `pkg/dart2js_info/tool/update_proto.sh` -> **100.0%** Exposure
- `pkg/vm/testcases/transformations/type_flow/transformer/protobuf_handler/compile_protos.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.agents/skills/read_gerrit_cl/scripts/read_comments.sh` -> **100.0%** Exposure
- `.agents/skills/read_gerrit_cl/scripts/read_patch.sh` -> **100.0%** Exposure
- `pkg/analyzer/tool/fasta_migration_progress.sh` -> **100.0%** Exposure
- `pkg/dart2wasm/tool/compile_benchmark` -> **100.0%** Exposure
- `pkg/dart2wasm/tool/run_benchmark` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pkg/front_end/parser_testcases/error_recovery/keyword_named_formal_parameter.dart` -> **0** Orphaned Functions | **250** Duplicates
- `pkg/front_end/parser_testcases/error_recovery/keyword_named_formal_parameter_prime.dart` -> **0** Orphaned Functions | **250** Duplicates
- `runtime/vm/compiler/assembler/assembler_ia32.cc` -> **137** Orphaned Functions | **113** Duplicates
- `runtime/vm/compiler/assembler/assembler_riscv.cc` -> **249** Orphaned Functions | **0** Duplicates
- `pkg/wasm_builder/lib/src/ir/instruction.dart` -> **0** Orphaned Functions | **245** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pkg/_fe_analyzer_shared/lib/src/metadata/parser.dart`** -> AI Confidence: **99.48%**
2. **`pkg/_fe_analyzer_shared/lib/src/parser/listener.dart`** -> AI Confidence: **99.48%**
3. **`pkg/compiler/lib/src/js/size_estimator.dart`** -> AI Confidence: **99.48%**
4. **`pkg/front_end/lib/src/kernel/forwarding_node.dart`** -> AI Confidence: **99.48%**
5. **`runtime/bin/dartdev_options.cc`** -> AI Confidence: **99.48%**
6. **`runtime/bin/file_test.cc`** -> AI Confidence: **99.48%**
7. **`runtime/platform/globals.h`** -> AI Confidence: **99.48%**
8. **`runtime/vm/code_descriptors.cc`** -> AI Confidence: **99.48%**
9. **`runtime/vm/compiler/assembler/disassembler.cc`** -> AI Confidence: **99.48%**
10. **`runtime/vm/compiler/assembler/disassembler_x86.cc`** -> AI Confidence: **99.48%**
11. **`runtime/vm/compiler/backend/il_arm.cc`** -> AI Confidence: **99.48%**
12. **`runtime/vm/compiler/backend/il_ia32.cc`** -> AI Confidence: **99.48%**
13. **`runtime/vm/compiler/backend/il_riscv.cc`** -> AI Confidence: **99.48%**
14. **`runtime/vm/compiler/frontend/kernel_to_il.cc`** -> AI Confidence: **99.48%**
15. **`runtime/vm/deferred_objects.cc`** -> AI Confidence: **99.48%**
16. **`runtime/vm/interpreter.cc`** -> AI Confidence: **99.48%**
17. **`runtime/vm/simulator_riscv.cc`** -> AI Confidence: **99.48%**
18. **`runtime/vm/source_report.cc`** -> AI Confidence: **99.48%**
19. **`runtime/vm/timeline_android.cc`** -> AI Confidence: **99.48%**
20. **`runtime/vm/timeline_fuchsia.cc`** -> AI Confidence: **99.48%**
21. **`runtime/vm/timeline_linux.cc`** -> AI Confidence: **99.48%**
22. **`pkg/front_end/lib/src/kernel/body_builder.dart`** -> AI Confidence: **99.44%**
23. **`pkg/front_end/lib/src/kernel/hierarchy/members_node.dart`** -> AI Confidence: **99.44%**
24. **`pkg/front_end/lib/src/source/fragment_factory.dart`** -> AI Confidence: **99.44%**
25. **`pkg/front_end/lib/src/source/outline_builder.dart`** -> AI Confidence: **99.44%**
26. **`pkg/dart_runtime_service_vm/lib/src/native_bindings.dart`** -> AI Confidence: **99.43%**
27. **`pkg/analysis_server/lib/src/services/correction/dart/add_null_check.dart`** -> AI Confidence: **99.39%**
28. **`pkg/analyzer_plugin/lib/src/utilities/completion/optype.dart`** -> AI Confidence: **99.39%**
29. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/widgets/text.dart`** -> AI Confidence: **99.39%**
30. **`pkg/compiler/lib/src/common/codegen.dart`** -> AI Confidence: **99.39%**
31. **`pkg/compiler/lib/src/js_backend/enqueuer.dart`** -> AI Confidence: **99.39%**
32. **`pkg/compiler/lib/src/js_backend/impact_transformer.dart`** -> AI Confidence: **99.39%**
33. **`pkg/compiler/lib/src/js_backend/resolution_listener.dart`** -> AI Confidence: **99.39%**
34. **`pkg/compiler/lib/src/resolution/enqueuer.dart`** -> AI Confidence: **99.39%**
35. **`pkg/dds/lib/src/dap/adapters/dart_cli_adapter.dart`** -> AI Confidence: **99.39%**
36. **`pkg/dds/lib/src/devtools/machine_mode_command_handler.dart`** -> AI Confidence: **99.39%**
37. **`pkg/front_end/lib/src/fragment/factory/encoding.dart`** -> AI Confidence: **99.39%**
38. **`pkg/front_end/lib/src/testing/verifying_analysis.dart`** -> AI Confidence: **99.39%**
39. **`pkg/front_end/lib/src/util/textual_outline.dart`** -> AI Confidence: **99.39%**
40. **`pkg/front_end/test/utils/suite_utils.dart`** -> AI Confidence: **99.39%**
41. **`pkg/front_end/tool/coverage_merger.dart`** -> AI Confidence: **99.39%**
42. **`pkg/front_end/tool/parser_ast_helper_creator.dart`** -> AI Confidence: **99.39%**
43. **`pkg/frontend_server/lib/src/resident_frontend_server.dart`** -> AI Confidence: **99.39%**
44. **`runtime/bin/eventhandler_linux.cc`** -> AI Confidence: **99.39%**
45. **`runtime/bin/eventhandler_macos.cc`** -> AI Confidence: **99.39%**
46. **`runtime/bin/gen_snapshot.cc`** -> AI Confidence: **99.39%**
47. **`runtime/bin/io_service.cc`** -> AI Confidence: **99.39%**
48. **`runtime/bin/io_service_no_ssl.cc`** -> AI Confidence: **99.39%**
49. **`runtime/bin/secure_socket_filter.cc`** -> AI Confidence: **99.39%**
50. **`runtime/bin/virtual_memory_posix.cc`** -> AI Confidence: **99.39%**
51. **`runtime/vm/bytecode_reader.cc`** -> AI Confidence: **99.39%**
52. **`runtime/vm/compiler/backend/flow_graph.cc`** -> AI Confidence: **99.39%**
53. **`runtime/vm/compiler/backend/flow_graph_compiler.cc`** -> AI Confidence: **99.39%**
54. **`runtime/vm/compiler/backend/flow_graph_compiler_arm64.cc`** -> AI Confidence: **99.39%**
55. **`runtime/vm/compiler/backend/flow_graph_compiler_riscv.cc`** -> AI Confidence: **99.39%**
56. **`runtime/vm/compiler/backend/il_arm64.cc`** -> AI Confidence: **99.39%**
57. **`runtime/vm/compiler/backend/il_x64.cc`** -> AI Confidence: **99.39%**
58. **`runtime/vm/compiler/backend/inliner.cc`** -> AI Confidence: **99.39%**
59. **`runtime/vm/compiler/backend/linearscan.cc`** -> AI Confidence: **99.39%**
60. **`runtime/vm/compiler/call_specializer.cc`** -> AI Confidence: **99.39%**
61. **`runtime/vm/compiler/frontend/kernel_binary_flowgraph.cc`** -> AI Confidence: **99.39%**
62. **`runtime/vm/compiler/frontend/prologue_builder.cc`** -> AI Confidence: **99.39%**
63. **`runtime/vm/cpu_arm.cc`** -> AI Confidence: **99.39%**
64. **`runtime/vm/cpu_riscv.cc`** -> AI Confidence: **99.39%**
65. **`runtime/vm/debugger.cc`** -> AI Confidence: **99.39%**
66. **`runtime/vm/exceptions.cc`** -> AI Confidence: **99.39%**
67. **`runtime/vm/heap/heap.cc`** -> AI Confidence: **99.39%**
68. **`runtime/vm/heap/marker.cc`** -> AI Confidence: **99.39%**
69. **`runtime/vm/heap/page.cc`** -> AI Confidence: **99.39%**
70. **`runtime/vm/heap/verifier.cc`** -> AI Confidence: **99.39%**
71. **`runtime/vm/regexp/regexp-compiler-tonode.cc`** -> AI Confidence: **99.39%**
72. **`runtime/vm/simulator_arm.cc`** -> AI Confidence: **99.39%**
73. **`runtime/vm/simulator_arm64.cc`** -> AI Confidence: **99.39%**
74. **`runtime/vm/virtual_memory_fuchsia.cc`** -> AI Confidence: **99.39%**
75. **`pkg/front_end/lib/src/builder/function_type_builder.dart`** -> AI Confidence: **99.35%**
76. **`pkg/front_end/lib/src/kernel/combined_member_signature.dart`** -> AI Confidence: **99.35%**
77. **`pkg/linter/lib/src/rules/prefer_is_empty.dart`** -> AI Confidence: **99.35%**
78. **`pkg/sourcemap_testing/lib/src/stacktrace_helper.dart`** -> AI Confidence: **99.35%**
79. **`runtime/bin/eventhandler_fuchsia.cc`** -> AI Confidence: **99.35%**
80. **`runtime/vm/compiler/backend/flow_graph_compiler_arm.cc`** -> AI Confidence: **99.35%**
81. **`runtime/vm/compiler/backend/flow_graph_compiler_x64.cc`** -> AI Confidence: **99.35%**
82. **`runtime/vm/message_handler.cc`** -> AI Confidence: **99.35%**
83. **`pkg/_fe_analyzer_shared/lib/src/parser/parser_impl.dart`** -> AI Confidence: **99.34%**
84. **`pkg/analysis_server/lib/src/status/utilities/ast_writer.dart`** -> AI Confidence: **99.34%**
85. **`pkg/analyzer/lib/src/dart/resolver/scope_context.dart`** -> AI Confidence: **99.34%**
86. **`pkg/analyzer/lib/src/summary2/metadata_resolver.dart`** -> AI Confidence: **99.34%**
87. **`pkg/analyzer/test/src/summary/resolved_ast_printer.dart`** -> AI Confidence: **99.34%**
88. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/painting/text_style.dart`** -> AI Confidence: **99.34%**
89. **`pkg/compiler/lib/src/ir/impact_data.dart`** -> AI Confidence: **99.34%**
90. **`pkg/compiler/lib/src/ssa/codegen.dart`** -> AI Confidence: **99.34%**
91. **`pkg/dds/lib/src/dap/base_debug_adapter.dart`** -> AI Confidence: **99.34%**
92. **`pkg/front_end/lib/src/kernel/hierarchy/extension_type_members.dart`** -> AI Confidence: **99.34%**
93. **`pkg/front_end/lib/src/kernel/type_algorithms.dart`** -> AI Confidence: **99.34%**
94. **`pkg/front_end/lib/src/type_inference/closure_context.dart`** -> AI Confidence: **99.34%**
95. **`pkg/front_end/tool/kernel_ast_file_rewriter.dart`** -> AI Confidence: **99.34%**
96. **`pkg/kernel/bin/dill_extractor.dart`** -> AI Confidence: **99.34%**
97. **`runtime/bin/socket_base_win.h`** -> AI Confidence: **99.34%**
98. **`runtime/vm/compiler/assembler/assembler_arm64.cc`** -> AI Confidence: **99.34%**
99. **`runtime/vm/compiler/ffi/native_type.cc`** -> AI Confidence: **99.34%**
100. **`runtime/vm/debugger_arm.cc`** -> AI Confidence: **99.34%**
101. **`runtime/vm/debugger_arm64.cc`** -> AI Confidence: **99.34%**
102. **`runtime/vm/debugger_riscv.cc`** -> AI Confidence: **99.34%**
103. **`runtime/vm/debugger_x64.cc`** -> AI Confidence: **99.34%**
104. **`runtime/vm/simulator.h`** -> AI Confidence: **99.34%**
105. **`runtime/vm/tsan_symbolize.cc`** -> AI Confidence: **99.34%**
106. **`pkg/_fe_analyzer_shared/lib/src/parser/identifier_context_impl.dart`** -> AI Confidence: **99.33%**
107. **`pkg/compiler/lib/src/io/position_information.dart`** -> AI Confidence: **99.33%**
108. **`pkg/front_end/lib/src/kernel/constructor_tearoff_lowering.dart`** -> AI Confidence: **99.33%**
109. **`pkg/front_end/lib/src/type_inference/matching_cache.dart`** -> AI Confidence: **99.33%**
110. **`runtime/tools/bin_to_coff.py`** -> AI Confidence: **99.32%**
111. **`tools/list_dart_files.py`** -> AI Confidence: **99.32%**
112. **`pkg/_fe_analyzer_shared/lib/src/scanner/scanner_main.dart`** -> AI Confidence: **99.32%**
113. **`pkg/_fe_analyzer_shared/lib/src/testing/id_generation.dart`** -> AI Confidence: **99.32%**
114. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/material/scaffold.dart`** -> AI Confidence: **99.32%**
115. **`pkg/compiler/test/sourcemaps/tools/load.dart`** -> AI Confidence: **99.32%**
116. **`pkg/compiler/tool/modular_dart2js.dart`** -> AI Confidence: **99.32%**
117. **`pkg/scrape/example/null_aware.dart`** -> AI Confidence: **99.32%**
118. **`tests/standalone/io/stdout_stderr_test_script.dart`** -> AI Confidence: **99.32%**
119. **`runtime/bin/process_test.cc`** -> AI Confidence: **99.32%**
120. **`runtime/platform/floating_point_win.cc`** -> AI Confidence: **99.32%**
121. **`runtime/vm/base64.cc`** -> AI Confidence: **99.32%**
122. **`runtime/vm/regexp/char-predicates.cc`** -> AI Confidence: **99.32%**
123. **`PRESUBMIT.py`** -> AI Confidence: **99.31%**
124. **`tools/build.py`** -> AI Confidence: **99.31%**
125. **`tools/dom/new_scripts/code_generator_dart.py`** -> AI Confidence: **99.31%**
126. **`tools/dom/scripts/dartmetadata.py`** -> AI Confidence: **99.31%**
127. **`tools/dom/scripts/fremontcutbuilder.py`** -> AI Confidence: **99.31%**
128. **`tools/dom/scripts/idlsync.py`** -> AI Confidence: **99.31%**
129. **`tools/dom/scripts/systemnative.py`** -> AI Confidence: **99.31%**
130. **`tools/generate_idefiles.py`** -> AI Confidence: **99.31%**
131. **`tools/gn.py`** -> AI Confidence: **99.31%**
132. **`benchmarks/Utf8Decode/dart/Utf8Decode.dart`** -> AI Confidence: **99.31%**
133. **`pkg/_fe_analyzer_shared/lib/src/flow_analysis/flow_analysis.dart`** -> AI Confidence: **99.31%**
134. **`pkg/_fe_analyzer_shared/lib/src/parser/stack_listener.dart`** -> AI Confidence: **99.31%**
135. **`pkg/_fe_analyzer_shared/lib/src/scanner/utf8_bytes_scanner.dart`** -> AI Confidence: **99.31%**
136. **`pkg/_js_interop_checks/lib/src/transformations/js_util_optimizer.dart`** -> AI Confidence: **99.31%**
137. **`pkg/_js_interop_checks/lib/src/transformations/shared_interop_transformer.dart`** -> AI Confidence: **99.31%**
138. **`pkg/analysis_server/benchmark/integration/main.dart`** -> AI Confidence: **99.31%**
139. **`pkg/analysis_server/lib/src/cider/local_library_contributor.dart`** -> AI Confidence: **99.31%**
140. **`pkg/analysis_server/lib/src/computer/computer_color.dart`** -> AI Confidence: **99.31%**
141. **`pkg/analysis_server/lib/src/computer/computer_document_highlights.dart`** -> AI Confidence: **99.31%**
142. **`pkg/analysis_server/lib/src/computer/computer_highlights.dart`** -> AI Confidence: **99.31%**
143. **`pkg/analysis_server/lib/src/computer/computer_hover.dart`** -> AI Confidence: **99.31%**
144. **`pkg/analysis_server/lib/src/computer/computer_inlay_hint.dart`** -> AI Confidence: **99.31%**
145. **`pkg/analysis_server/lib/src/computer/computer_signature.dart`** -> AI Confidence: **99.31%**
146. **`pkg/analysis_server/lib/src/domains/analysis/occurrences_dart.dart`** -> AI Confidence: **99.31%**
147. **`pkg/analysis_server/lib/src/flutter/flutter_outline_computer.dart`** -> AI Confidence: **99.31%**
148. **`pkg/analysis_server/lib/src/lsp/handlers/commands/abstract_refactor.dart`** -> AI Confidence: **99.31%**
149. **`pkg/analysis_server/lib/src/lsp/handlers/custom/editable_arguments/handler_editable_arguments.dart`** -> AI Confidence: **99.31%**
150. **`pkg/analysis_server/lib/src/lsp/handlers/handler_type_definition.dart`** -> AI Confidence: **99.31%**
151. **`pkg/analysis_server/lib/src/lsp/mapping.dart`** -> AI Confidence: **99.31%**
152. **`pkg/analysis_server/lib/src/plugin/server_isolate_channel.dart`** -> AI Confidence: **99.31%**
153. **`pkg/analysis_server/lib/src/protocol/protocol_internal.dart`** -> AI Confidence: **99.31%**
154. **`pkg/analysis_server/lib/src/scheduler/message_scheduler.dart`** -> AI Confidence: **99.31%**
155. **`pkg/analysis_server/lib/src/services/completion/dart/candidate_suggestion.dart`** -> AI Confidence: **99.31%**
156. **`pkg/analysis_server/lib/src/services/completion/dart/declaration_helper.dart`** -> AI Confidence: **99.31%**
157. **`pkg/analysis_server/lib/src/services/completion/dart/feature_computer.dart`** -> AI Confidence: **99.31%**
158. **`pkg/analysis_server/lib/src/services/completion/dart/in_scope_completion_pass.dart`** -> AI Confidence: **99.31%**
159. **`pkg/analysis_server/lib/src/services/completion/dart/keyword_helper.dart`** -> AI Confidence: **99.31%**
160. **`pkg/analysis_server/lib/src/services/completion/dart/suggestion_builder.dart`** -> AI Confidence: **99.31%**
161. **`pkg/analysis_server/lib/src/services/completion/dart/uri_helper.dart`** -> AI Confidence: **99.31%**
162. **`pkg/analysis_server/lib/src/services/completion/dart/utilities.dart`** -> AI Confidence: **99.31%**
163. **`pkg/analysis_server/lib/src/services/completion/statement/statement_completion.dart`** -> AI Confidence: **99.31%**
164. **`pkg/analysis_server/lib/src/services/correction/dart/add_async.dart`** -> AI Confidence: **99.31%**
165. **`pkg/analysis_server/lib/src/services/correction/dart/add_diagnostic_property_reference.dart`** -> AI Confidence: **99.31%**
166. **`pkg/analysis_server/lib/src/services/correction/dart/add_enum_constant.dart`** -> AI Confidence: **99.31%**
167. **`pkg/analysis_server/lib/src/services/correction/dart/add_explicit_cast.dart`** -> AI Confidence: **99.31%**
168. **`pkg/analysis_server/lib/src/services/correction/dart/add_field_formal_parameters.dart`** -> AI Confidence: **99.31%**
169. **`pkg/analysis_server/lib/src/services/correction/dart/add_late.dart`** -> AI Confidence: **99.31%**
170. **`pkg/analysis_server/lib/src/services/correction/dart/add_missing_enum_case_clauses.dart`** -> AI Confidence: **99.31%**
171. **`pkg/analysis_server/lib/src/services/correction/dart/add_missing_parameter_named.dart`** -> AI Confidence: **99.31%**
172. **`pkg/analysis_server/lib/src/services/correction/dart/add_return_type.dart`** -> AI Confidence: **99.31%**
173. **`pkg/analysis_server/lib/src/services/correction/dart/add_super_constructor_invocation.dart`** -> AI Confidence: **99.31%**
174. **`pkg/analysis_server/lib/src/services/correction/dart/add_super_parameter.dart`** -> AI Confidence: **99.31%**
175. **`pkg/analysis_server/lib/src/services/correction/dart/convert_into_final_field.dart`** -> AI Confidence: **99.31%**
176. **`pkg/analysis_server/lib/src/services/correction/dart/convert_into_getter.dart`** -> AI Confidence: **99.31%**
177. **`pkg/analysis_server/lib/src/services/correction/dart/convert_null_check_to_null_aware_element_or_entry.dart`** -> AI Confidence: **99.31%**
178. **`pkg/analysis_server/lib/src/services/correction/dart/convert_related_to_cascade.dart`** -> AI Confidence: **99.31%**
179. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_boolean_expression.dart`** -> AI Confidence: **99.31%**
180. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_declaring_parameter.dart`** -> AI Confidence: **99.31%**
181. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_flutter_style_todo.dart`** -> AI Confidence: **99.31%**
182. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_function_declaration.dart`** -> AI Confidence: **99.31%**
183. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_if_null.dart`** -> AI Confidence: **99.31%**
184. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_initializing_formal.dart`** -> AI Confidence: **99.31%**
185. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_named_arguments.dart`** -> AI Confidence: **99.31%**
186. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_secondary_constructor.dart`** -> AI Confidence: **99.31%**
187. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_set_literal.dart`** -> AI Confidence: **99.31%**
188. **`pkg/analysis_server/lib/src/services/correction/dart/convert_to_super_parameters.dart`** -> AI Confidence: **99.31%**
189. **`pkg/analysis_server/lib/src/services/correction/dart/create_class.dart`** -> AI Confidence: **99.31%**
190. **`pkg/analysis_server/lib/src/services/correction/dart/create_constructor_super.dart`** -> AI Confidence: **99.31%**
191. **`pkg/analysis_server/lib/src/services/correction/dart/create_extension_member.dart`** -> AI Confidence: **99.31%**
192. **`pkg/analysis_server/lib/src/services/correction/dart/create_getter.dart`** -> AI Confidence: **99.31%**
193. **`pkg/analysis_server/lib/src/services/correction/dart/create_mixin.dart`** -> AI Confidence: **99.31%**
194. **`pkg/analysis_server/lib/src/services/correction/dart/create_operator.dart`** -> AI Confidence: **99.31%**
195. **`pkg/analysis_server/lib/src/services/correction/dart/create_parameter.dart`** -> AI Confidence: **99.31%**
196. **`pkg/analysis_server/lib/src/services/correction/dart/create_setter.dart`** -> AI Confidence: **99.31%**
197. **`pkg/analysis_server/lib/src/services/correction/dart/encapsulate_field.dart`** -> AI Confidence: **99.31%**
198. **`pkg/analysis_server/lib/src/services/correction/dart/flutter_swap_with_child.dart`** -> AI Confidence: **99.31%**
199. **`pkg/analysis_server/lib/src/services/correction/dart/inline_typedef.dart`** -> AI Confidence: **99.31%**
200. **`pkg/analysis_server/lib/src/services/correction/dart/join_else_with_if.dart`** -> AI Confidence: **99.31%**
201. **`pkg/analysis_server/lib/src/services/correction/dart/make_field_public.dart`** -> AI Confidence: **99.31%**
202. **`pkg/analysis_server/lib/src/services/correction/dart/remove_async.dart`** -> AI Confidence: **99.31%**
203. **`pkg/analysis_server/lib/src/services/correction/dart/remove_leading_underscore.dart`** -> AI Confidence: **99.31%**
204. **`pkg/analysis_server/lib/src/services/correction/dart/remove_type_annotation.dart`** -> AI Confidence: **99.31%**
205. **`pkg/analysis_server/lib/src/services/correction/dart/remove_unexpected_underscores.dart`** -> AI Confidence: **99.31%**
206. **`pkg/analysis_server/lib/src/services/correction/dart/remove_unused.dart`** -> AI Confidence: **99.31%**
207. **`pkg/analysis_server/lib/src/services/correction/dart/remove_unused_parameter.dart`** -> AI Confidence: **99.31%**
208. **`pkg/analysis_server/lib/src/services/correction/dart/replace_with_interpolation.dart`** -> AI Confidence: **99.31%**
209. **`pkg/analysis_server/lib/src/services/correction/dart/replace_with_is_empty.dart`** -> AI Confidence: **99.31%**
210. **`pkg/analysis_server/lib/src/services/correction/dart/replace_with_var.dart`** -> AI Confidence: **99.31%**
211. **`pkg/analysis_server/lib/src/services/correction/fix/data_driven/element_matcher.dart`** -> AI Confidence: **99.31%**
212. **`pkg/analysis_server/lib/src/services/correction/fix/data_driven/modify_parameters.dart`** -> AI Confidence: **99.31%**
213. **`pkg/analysis_server/lib/src/services/correction/fix/data_driven/rename.dart`** -> AI Confidence: **99.31%**
214. **`pkg/analysis_server/lib/src/services/correction/fix/data_driven/replaced_by.dart`** -> AI Confidence: **99.31%**
215. **`pkg/analysis_server/lib/src/services/correction/statement_analyzer.dart`** -> AI Confidence: **99.31%**
216. **`pkg/analysis_server/lib/src/services/flutter/property.dart`** -> AI Confidence: **99.31%**
217. **`pkg/analysis_server/lib/src/services/flutter/widget_descriptions.dart`** -> AI Confidence: **99.31%**
218. **`pkg/analysis_server/lib/src/services/pub/pub_api.dart`** -> AI Confidence: **99.31%**
219. **`pkg/analysis_server/lib/src/services/refactoring/legacy/extract_method.dart`** -> AI Confidence: **99.31%**
220. **`pkg/analysis_server/lib/src/services/refactoring/legacy/refactoring.dart`** -> AI Confidence: **99.31%**
221. **`pkg/analysis_server/lib/src/services/refactoring/legacy/refactoring_manager.dart`** -> AI Confidence: **99.31%**
222. **`pkg/analysis_server/lib/src/services/snippets/dart_snippet_request.dart`** -> AI Confidence: **99.31%**
223. **`pkg/analysis_server/lib/src/status/pages/plugins_page.dart`** -> AI Confidence: **99.31%**
224. **`pkg/analysis_server/lib/src/status/pages/timing_page.dart`** -> AI Confidence: **99.31%**
225. **`pkg/analysis_server/lib/src/status/utilities/tree_writer.dart`** -> AI Confidence: **99.31%**
226. **`pkg/analysis_server/lib/src/utilities/import_analyzer.dart`** -> AI Confidence: **99.31%**
227. **`pkg/analysis_server/test/src/services/correction/fix/add_missing_enum_case_clauses_test.dart`** -> AI Confidence: **99.31%**
228. **`pkg/analysis_server/tool/benchmark_tools/big_chain_benchmark/files/copy_me/copy_me.dart`** -> AI Confidence: **99.31%**
229. **`pkg/analysis_server/tool/benchmark_tools/language_server_benchmark.dart`** -> AI Confidence: **99.31%**
230. **`pkg/analysis_server/tool/code_completion/relevance_metrics.dart`** -> AI Confidence: **99.31%**
231. **`pkg/analysis_server/tool/log_player/server_driver.dart`** -> AI Confidence: **99.31%**
232. **`pkg/analysis_server/tool/presubmit/verify_error_fix_status.dart`** -> AI Confidence: **99.31%**
233. **`pkg/analyzer/lib/src/analysis_options/options_file_validator.dart`** -> AI Confidence: **99.31%**
234. **`pkg/analyzer/lib/src/context/source.dart`** -> AI Confidence: **99.31%**
235. **`pkg/analyzer/lib/src/dart/analysis/analysis_context_collection.dart`** -> AI Confidence: **99.31%**
236. **`pkg/analyzer/lib/src/dart/analysis/analysis_options.dart`** -> AI Confidence: **99.31%**
237. **`pkg/analyzer/lib/src/dart/analysis/context_locator.dart`** -> AI Confidence: **99.31%**
238. **`pkg/analyzer/lib/src/dart/analysis/index.dart`** -> AI Confidence: **99.31%**
239. **`pkg/analyzer/lib/src/dart/ast/extensions.dart`** -> AI Confidence: **99.31%**
240. **`pkg/analyzer/lib/src/dart/constant/constant_verifier.dart`** -> AI Confidence: **99.31%**
241. **`pkg/analyzer/lib/src/dart/constant/evaluation.dart`** -> AI Confidence: **99.31%**
242. **`pkg/analyzer/lib/src/dart/constant/potentially_constant.dart`** -> AI Confidence: **99.31%**
243. **`pkg/analyzer/lib/src/dart/element/display_string_builder.dart`** -> AI Confidence: **99.31%**
244. **`pkg/analyzer/lib/src/dart/element/extensions.dart`** -> AI Confidence: **99.31%**
245. **`pkg/analyzer/lib/src/dart/element/least_upper_bound.dart`** -> AI Confidence: **99.31%**
246. **`pkg/analyzer/lib/src/dart/element/replacement_visitor.dart`** -> AI Confidence: **99.31%**
247. **`pkg/analyzer/lib/src/dart/element/scope.dart`** -> AI Confidence: **99.31%**
248. **`pkg/analyzer/lib/src/dart/element/subtype.dart`** -> AI Confidence: **99.31%**
249. **`pkg/analyzer/lib/src/dart/resolver/annotation_resolver.dart`** -> AI Confidence: **99.31%**
250. **`pkg/analyzer/lib/src/dart/resolver/assignment_expression_resolver.dart`** -> AI Confidence: **99.31%**
251. **`pkg/analyzer/lib/src/dart/resolver/binary_expression_resolver.dart`** -> AI Confidence: **99.31%**
252. **`pkg/analyzer/lib/src/dart/resolver/body_inference_context.dart`** -> AI Confidence: **99.31%**
253. **`pkg/analyzer/lib/src/dart/resolver/comment_reference_resolver.dart`** -> AI Confidence: **99.31%**
254. **`pkg/analyzer/lib/src/dart/resolver/element_binding_visitor.dart`** -> AI Confidence: **99.31%**
255. **`pkg/analyzer/lib/src/dart/resolver/flow_analysis_visitor.dart`** -> AI Confidence: **99.31%**
256. **`pkg/analyzer/lib/src/dart/resolver/for_resolver.dart`** -> AI Confidence: **99.31%**
257. **`pkg/analyzer/lib/src/dart/resolver/function_reference_resolver.dart`** -> AI Confidence: **99.31%**
258. **`pkg/analyzer/lib/src/dart/resolver/instance_creation_expression_resolver.dart`** -> AI Confidence: **99.31%**
259. **`pkg/analyzer/lib/src/dart/resolver/method_invocation_resolver.dart`** -> AI Confidence: **99.31%**
260. **`pkg/analyzer/lib/src/dart/resolver/named_type_resolver.dart`** -> AI Confidence: **99.31%**
261. **`pkg/analyzer/lib/src/dart/resolver/prefix_expression_resolver.dart`** -> AI Confidence: **99.31%**
262. **`pkg/analyzer/lib/src/dart/resolver/prefixed_identifier_resolver.dart`** -> AI Confidence: **99.31%**
263. **`pkg/analyzer/lib/src/dart/resolver/property_element_resolver.dart`** -> AI Confidence: **99.31%**
264. **`pkg/analyzer/lib/src/dart/resolver/resolution_visitor.dart`** -> AI Confidence: **99.31%**
265. **`pkg/analyzer/lib/src/dart/resolver/simple_identifier_resolver.dart`** -> AI Confidence: **99.31%**
266. **`pkg/analyzer/lib/src/dart/resolver/type_property_resolver.dart`** -> AI Confidence: **99.31%**
267. **`pkg/analyzer/lib/src/dart/resolver/typed_literal_resolver.dart`** -> AI Confidence: **99.31%**
268. **`pkg/analyzer/lib/src/dart/resolver/variable_declaration_resolver.dart`** -> AI Confidence: **99.31%**
269. **`pkg/analyzer/lib/src/dart/resolver/yield_statement_resolver.dart`** -> AI Confidence: **99.31%**
270. **`pkg/analyzer/lib/src/dart/scanner/translate_error_token.dart`** -> AI Confidence: **99.31%**
271. **`pkg/analyzer/lib/src/error/base_or_final_type_verifier.dart`** -> AI Confidence: **99.31%**
272. **`pkg/analyzer/lib/src/error/best_practices_verifier.dart`** -> AI Confidence: **99.31%**
273. **`pkg/analyzer/lib/src/error/const_argument_verifier.dart`** -> AI Confidence: **99.31%**
274. **`pkg/analyzer/lib/src/error/constructor_fields_verifier.dart`** -> AI Confidence: **99.31%**
275. **`pkg/analyzer/lib/src/error/dead_code_verifier.dart`** -> AI Confidence: **99.31%**
276. **`pkg/analyzer/lib/src/error/deprecated_functionality_verifier.dart`** -> AI Confidence: **99.31%**
277. **`pkg/analyzer/lib/src/error/duplicate_definition_verifier.dart`** -> AI Confidence: **99.31%**
278. **`pkg/analyzer/lib/src/error/element_usage_detector.dart`** -> AI Confidence: **99.31%**
279. **`pkg/analyzer/lib/src/error/ignore_validator.dart`** -> AI Confidence: **99.31%**
280. **`pkg/analyzer/lib/src/error/inheritance_override.dart`** -> AI Confidence: **99.31%**
281. **`pkg/analyzer/lib/src/error/literal_element_verifier.dart`** -> AI Confidence: **99.31%**
282. **`pkg/analyzer/lib/src/error/member_duplicate_definition_verifier.dart`** -> AI Confidence: **99.31%**
283. **`pkg/analyzer/lib/src/error/required_parameters_verifier.dart`** -> AI Confidence: **99.31%**
284. **`pkg/analyzer/lib/src/error/return_type_verifier.dart`** -> AI Confidence: **99.31%**
285. **`pkg/analyzer/lib/src/error/type_arguments_verifier.dart`** -> AI Confidence: **99.31%**
286. **`pkg/analyzer/lib/src/error/unused_local_elements_verifier.dart`** -> AI Confidence: **99.31%**
287. **`pkg/analyzer/lib/src/fasta/ast_builder.dart`** -> AI Confidence: **99.31%**
288. **`pkg/analyzer/lib/src/fasta/doc_comment_builder.dart`** -> AI Confidence: **99.31%**
289. **`pkg/analyzer/lib/src/fasta/error_converter.dart`** -> AI Confidence: **99.31%**
290. **`pkg/analyzer/lib/src/fine/manifest_context.dart`** -> AI Confidence: **99.31%**
291. **`pkg/analyzer/lib/src/generated/element_resolver.dart`** -> AI Confidence: **99.31%**
292. **`pkg/analyzer/lib/src/generated/error_detection_helpers.dart`** -> AI Confidence: **99.31%**
293. **`pkg/analyzer/lib/src/generated/error_verifier.dart`** -> AI Confidence: **99.31%**
294. **`pkg/analyzer/lib/src/generated/ffi_verifier.dart`** -> AI Confidence: **99.31%**
295. **`pkg/analyzer/lib/src/generated/resolver.dart`** -> AI Confidence: **99.31%**
296. **`pkg/analyzer/lib/src/hint/sdk_constraint_verifier.dart`** -> AI Confidence: **99.31%**
297. **`pkg/analyzer/lib/src/lint/constants.dart`** -> AI Confidence: **99.31%**
298. **`pkg/analyzer/lib/src/lint/options_rule_validator.dart`** -> AI Confidence: **99.31%**
299. **`pkg/analyzer/lib/src/manifest/manifest_validator.dart`** -> AI Confidence: **99.31%**
300. **`pkg/analyzer/lib/src/summary2/ast_binary_writer.dart`** -> AI Confidence: **99.31%**
301. **`pkg/analyzer/lib/src/summary2/bundle_writer.dart`** -> AI Confidence: **99.31%**
302. **`pkg/analyzer/lib/src/summary2/default_types_builder.dart`** -> AI Confidence: **99.31%**
303. **`pkg/analyzer/lib/src/summary2/element_builder.dart`** -> AI Confidence: **99.31%**
304. **`pkg/analyzer/lib/src/summary2/informative_data.dart`** -> AI Confidence: **99.31%**
305. **`pkg/analyzer/lib/src/summary2/types_builder.dart`** -> AI Confidence: **99.31%**
306. **`pkg/analyzer/lib/src/summary2/variance_builder.dart`** -> AI Confidence: **99.31%**
307. **`pkg/analyzer/lib/src/test_utilities/find_element2.dart`** -> AI Confidence: **99.31%**
308. **`pkg/analyzer/lib/src/wolf/ir/ast_to_ir.dart`** -> AI Confidence: **99.31%**
309. **`pkg/analyzer/test/src/dart/analysis/result_printer.dart`** -> AI Confidence: **99.31%**
310. **`pkg/analyzer/test/src/dart/constant/value_test.dart`** -> AI Confidence: **99.31%**
311. **`pkg/analyzer/test/src/dart/element/subtype_test.dart`** -> AI Confidence: **99.31%**
312. **`pkg/analyzer/tool/generators/ast_generator.dart`** -> AI Confidence: **99.31%**
313. **`pkg/analyzer/tool/stable_analysis.dart`** -> AI Confidence: **99.31%**
314. **`pkg/analyzer/tool/summary/generate.dart`** -> AI Confidence: **99.31%**
315. **`pkg/analyzer/tool/summary/mini_ast.dart`** -> AI Confidence: **99.31%**
316. **`pkg/analyzer_cli/lib/src/error_formatter.dart`** -> AI Confidence: **99.31%**
317. **`pkg/analyzer_cli/lib/src/options.dart`** -> AI Confidence: **99.31%**
318. **`pkg/analyzer_plugin/lib/src/utilities/change_builder/change_builder_core.dart`** -> AI Confidence: **99.31%**
319. **`pkg/analyzer_plugin/lib/src/utilities/change_builder/change_builder_dart.dart`** -> AI Confidence: **99.31%**
320. **`pkg/analyzer_plugin/lib/src/utilities/completion/completion_target.dart`** -> AI Confidence: **99.31%**
321. **`pkg/analyzer_plugin/lib/src/utilities/completion/suggestion_builder.dart`** -> AI Confidence: **99.31%**
322. **`pkg/analyzer_plugin/lib/src/utilities/navigation/navigation_dart.dart`** -> AI Confidence: **99.31%**
323. **`pkg/analyzer_utilities/lib/src/api_summary/src/api_description.dart`** -> AI Confidence: **99.31%**
324. **`pkg/compiler/lib/src/dart2js.dart`** -> AI Confidence: **99.31%**
325. **`pkg/compiler/lib/src/diagnostics/diagnostic_listener.dart`** -> AI Confidence: **99.31%**
326. **`pkg/compiler/lib/src/dump_info.dart`** -> AI Confidence: **99.31%**
327. **`pkg/compiler/lib/src/inferrer/builder.dart`** -> AI Confidence: **99.31%**
328. **`pkg/compiler/lib/src/inferrer/locals_handler.dart`** -> AI Confidence: **99.31%**
329. **`pkg/compiler/lib/src/io/kernel_source_information.dart`** -> AI Confidence: **99.31%**
330. **`pkg/compiler/lib/src/io/source_map_builder.dart`** -> AI Confidence: **99.31%**
331. **`pkg/compiler/lib/src/js_backend/backend.dart`** -> AI Confidence: **99.31%**
332. **`pkg/compiler/lib/src/js_backend/field_analysis.dart`** -> AI Confidence: **99.31%**
333. **`pkg/compiler/lib/src/js_backend/runtime_types.dart`** -> AI Confidence: **99.31%**
334. **`pkg/compiler/lib/src/js_backend/specialized_checks.dart`** -> AI Confidence: **99.31%**
335. **`pkg/compiler/lib/src/js_backend/string_reference.dart`** -> AI Confidence: **99.31%**
336. **`pkg/compiler/lib/src/js_backend/type_reference.dart`** -> AI Confidence: **99.31%**
337. **`pkg/compiler/lib/src/js_model/element_map_impl.dart`** -> AI Confidence: **99.31%**
338. **`pkg/compiler/lib/src/kernel/kernel_world.dart`** -> AI Confidence: **99.31%**
339. **`pkg/compiler/lib/src/kernel/native_basic_data.dart`** -> AI Confidence: **99.31%**
340. **`pkg/compiler/lib/src/ssa/builder.dart`** -> AI Confidence: **99.31%**
341. **`pkg/compiler/lib/src/ssa/invoke_dynamic_specializers.dart`** -> AI Confidence: **99.31%**
342. **`pkg/compiler/lib/src/ssa/loop_handler.dart`** -> AI Confidence: **99.31%**
343. **`pkg/compiler/lib/src/ssa/type_builder.dart`** -> AI Confidence: **99.31%**
344. **`pkg/compiler/lib/src/universe/class_hierarchy.dart`** -> AI Confidence: **99.31%**
345. **`pkg/compiler/lib/src/universe/codegen_world_builder.dart`** -> AI Confidence: **99.31%**
346. **`pkg/compiler/lib/src/universe/member_hierarchy.dart`** -> AI Confidence: **99.31%**
347. **`pkg/compiler/lib/src/util/memory_compiler.dart`** -> AI Confidence: **99.31%**
348. **`pkg/compiler/test/sourcemaps/tools/diff_view.dart`** -> AI Confidence: **99.31%**
349. **`pkg/compiler/test/sourcemaps/tools/source_mapping_tester.dart`** -> AI Confidence: **99.31%**
350. **`pkg/dart2js_info/bin/src/text_print.dart`** -> AI Confidence: **99.31%**
351. **`pkg/dart2js_info/bin/src/to_devtools_format.dart`** -> AI Confidence: **99.31%**
352. **`pkg/dart2js_tools/bin/deobfuscate.dart`** -> AI Confidence: **99.31%**
353. **`pkg/dartdev/lib/src/commands/analyze.dart`** -> AI Confidence: **99.31%**
354. **`pkg/dartdev/lib/src/commands/compile.dart`** -> AI Confidence: **99.31%**
355. **`pkg/dartdev/lib/src/commands/doc.dart`** -> AI Confidence: **99.31%**
356. **`pkg/dartdev/lib/src/commands/install.dart`** -> AI Confidence: **99.31%**
357. **`pkg/dartdev/lib/src/generate_kernel.dart`** -> AI Confidence: **99.31%**
358. **`pkg/dartdev/lib/src/sdk_cache.dart`** -> AI Confidence: **99.31%**
359. **`pkg/dds/lib/src/dap/adapters/dart_test_adapter.dart`** -> AI Confidence: **99.31%**
360. **`pkg/dds/lib/src/dap/isolate_manager.dart`** -> AI Confidence: **99.31%**
361. **`pkg/dds/lib/src/dap/protocol_converter.dart`** -> AI Confidence: **99.31%**
362. **`pkg/dds/lib/src/devtools/handler.dart`** -> AI Confidence: **99.31%**
363. **`pkg/front_end/lib/src/api_prototype/language_version.dart`** -> AI Confidence: **99.31%**
364. **`pkg/front_end/lib/src/base/import.dart`** -> AI Confidence: **99.31%**
365. **`pkg/front_end/lib/src/base/incremental_compiler.dart`** -> AI Confidence: **99.31%**
366. **`pkg/front_end/lib/src/base/scope.dart`** -> AI Confidence: **99.31%**
367. **`pkg/front_end/lib/src/builder/constructor_reference_builder.dart`** -> AI Confidence: **99.31%**
368. **`pkg/front_end/lib/src/builder/synthesized_type_builder.dart`** -> AI Confidence: **99.31%**
369. **`pkg/front_end/lib/src/fragment/constructor/declaration.dart`** -> AI Confidence: **99.31%**
370. **`pkg/front_end/lib/src/fragment/constructor/encoding.dart`** -> AI Confidence: **99.31%**
371. **`pkg/front_end/lib/src/fragment/field/declaration.dart`** -> AI Confidence: **99.31%**
372. **`pkg/front_end/lib/src/fragment/getter/encoding.dart`** -> AI Confidence: **99.31%**
373. **`pkg/front_end/lib/src/fragment/method/encoding.dart`** -> AI Confidence: **99.31%**
374. **`pkg/front_end/lib/src/kernel/implicit_field_type.dart`** -> AI Confidence: **99.31%**
375. **`pkg/front_end/lib/src/kernel/kernel_target.dart`** -> AI Confidence: **99.31%**
376. **`pkg/front_end/lib/src/kernel_generator_impl.dart`** -> AI Confidence: **99.31%**
377. **`pkg/front_end/presubmit_helper_spawn.dart`** -> AI Confidence: **99.31%**
378. **`pkg/front_end/tool/compile_files_in_folders.dart`** -> AI Confidence: **99.31%**
379. **`pkg/front_end/tool/fuzz/fuzz.dart`** -> AI Confidence: **99.31%**
380. **`pkg/front_end/tool/fuzz/minimizer.dart`** -> AI Confidence: **99.31%**
381. **`pkg/front_end/tool/generate_ast_equivalence.dart`** -> AI Confidence: **99.31%**
382. **`pkg/frontend_server_client/lib/src/dartdevc_frontend_server_client.dart`** -> AI Confidence: **99.31%**
383. **`pkg/linter/lib/src/rules/always_specify_types.dart`** -> AI Confidence: **99.31%**
384. **`pkg/linter/lib/src/rules/analyzer_element_model_tracking.dart`** -> AI Confidence: **99.31%**
385. **`pkg/linter/lib/src/rules/analyzer_public_api.dart`** -> AI Confidence: **99.31%**
386. **`pkg/linter/lib/src/rules/annotate_overrides.dart`** -> AI Confidence: **99.31%**
387. **`pkg/linter/lib/src/rules/avoid_dynamic_calls.dart`** -> AI Confidence: **99.31%**
388. **`pkg/linter/lib/src/rules/avoid_function_literals_in_foreach_calls.dart`** -> AI Confidence: **99.31%**
389. **`pkg/linter/lib/src/rules/avoid_null_checks_in_equality_operators.dart`** -> AI Confidence: **99.31%**
390. **`pkg/linter/lib/src/rules/avoid_redundant_argument_values.dart`** -> AI Confidence: **99.31%**
391. **`pkg/linter/lib/src/rules/avoid_shadowing_type_parameters.dart`** -> AI Confidence: **99.31%**
392. **`pkg/linter/lib/src/rules/avoid_type_to_string.dart`** -> AI Confidence: **99.31%**
393. **`pkg/linter/lib/src/rules/avoid_types_as_parameter_names.dart`** -> AI Confidence: **99.31%**
394. **`pkg/linter/lib/src/rules/curly_braces_in_flow_control_structures.dart`** -> AI Confidence: **99.31%**
395. **`pkg/linter/lib/src/rules/diagnostic_describe_all_properties.dart`** -> AI Confidence: **99.31%**
396. **`pkg/linter/lib/src/rules/invalid_case_patterns.dart`** -> AI Confidence: **99.31%**
397. **`pkg/linter/lib/src/rules/invalid_runtime_check_with_js_interop_types.dart`** -> AI Confidence: **99.31%**
398. **`pkg/linter/lib/src/rules/library_private_types_in_public_api.dart`** -> AI Confidence: **99.31%**
399. **`pkg/linter/lib/src/rules/no_literal_bool_comparisons.dart`** -> AI Confidence: **99.31%**
400. **`pkg/linter/lib/src/rules/non_constant_identifier_names.dart`** -> AI Confidence: **99.31%**
401. **`pkg/linter/lib/src/rules/noop_primitive_operations.dart`** -> AI Confidence: **99.31%**
402. **`pkg/linter/lib/src/rules/parameter_assignments.dart`** -> AI Confidence: **99.31%**
403. **`pkg/linter/lib/src/rules/prefer_asserts_in_initializer_lists.dart`** -> AI Confidence: **99.31%**
404. **`pkg/linter/lib/src/rules/prefer_const_constructors_in_immutables.dart`** -> AI Confidence: **99.31%**
405. **`pkg/linter/lib/src/rules/prefer_const_literals_to_create_immutables.dart`** -> AI Confidence: **99.31%**
406. **`pkg/linter/lib/src/rules/prefer_contains.dart`** -> AI Confidence: **99.31%**
407. **`pkg/linter/lib/src/rules/prefer_int_literals.dart`** -> AI Confidence: **99.31%**
408. **`pkg/linter/lib/src/rules/prefer_interpolation_to_compose_strings.dart`** -> AI Confidence: **99.31%**
409. **`pkg/linter/lib/src/rules/prefer_void_to_null.dart`** -> AI Confidence: **99.31%**
410. **`pkg/linter/lib/src/rules/public_member_api_docs.dart`** -> AI Confidence: **99.31%**
411. **`pkg/linter/lib/src/rules/require_trailing_commas.dart`** -> AI Confidence: **99.31%**
412. **`pkg/linter/lib/src/rules/strict_top_level_inference.dart`** -> AI Confidence: **99.31%**
413. **`pkg/linter/lib/src/rules/tighten_type_of_initializing_formals.dart`** -> AI Confidence: **99.31%**
414. **`pkg/linter/lib/src/rules/type_annotate_public_apis.dart`** -> AI Confidence: **99.31%**
415. **`pkg/linter/lib/src/rules/unnecessary_null_aware_operator_on_extension_on_nullable.dart`** -> AI Confidence: **99.31%**
416. **`pkg/linter/lib/src/rules/unnecessary_null_checks.dart`** -> AI Confidence: **99.31%**
417. **`pkg/linter/lib/src/rules/unnecessary_overrides.dart`** -> AI Confidence: **99.31%**
418. **`pkg/linter/lib/src/rules/unnecessary_parenthesis.dart`** -> AI Confidence: **99.31%**
419. **`pkg/linter/lib/src/rules/unnecessary_string_escapes.dart`** -> AI Confidence: **99.31%**
420. **`pkg/linter/lib/src/rules/unreachable_from_main.dart`** -> AI Confidence: **99.31%**
421. **`pkg/linter/lib/src/rules/use_build_context_synchronously.dart`** -> AI Confidence: **99.31%**
422. **`pkg/linter/lib/src/rules/use_enums.dart`** -> AI Confidence: **99.31%**
423. **`pkg/linter/lib/src/rules/use_key_in_widget_constructors.dart`** -> AI Confidence: **99.31%**
424. **`pkg/linter/lib/src/rules/use_late_for_private_fields_and_variables.dart`** -> AI Confidence: **99.31%**
425. **`pkg/linter/lib/src/rules/use_null_aware_elements.dart`** -> AI Confidence: **99.31%**
426. **`pkg/linter/lib/src/rules/void_checks.dart`** -> AI Confidence: **99.31%**
427. **`pkg/linter/lib/src/util/leak_detector_visitor.dart`** -> AI Confidence: **99.31%**
428. **`pkg/native_stack_traces/bin/decode.dart`** -> AI Confidence: **99.31%**
429. **`pkg/native_stack_traces/lib/src/dwarf.dart`** -> AI Confidence: **99.31%**
430. **`pkg/observatory/lib/src/elements/containers/virtual_collection.dart`** -> AI Confidence: **99.31%**
431. **`pkg/observatory/lib/src/elements/containers/virtual_tree.dart`** -> AI Confidence: **99.31%**
432. **`pkg/observatory/lib/src/elements/cpu_profile/virtual_tree.dart`** -> AI Confidence: **99.31%**
433. **`pkg/observatory/lib/src/elements/debugger.dart`** -> AI Confidence: **99.31%**
434. **`pkg/observatory/lib/src/elements/helpers/any_ref.dart`** -> AI Confidence: **99.31%**
435. **`pkg/observatory/lib/src/elements/isolate/location.dart`** -> AI Confidence: **99.31%**
436. **`pkg/observatory/lib/src/elements/nav/notify_event.dart`** -> AI Confidence: **99.31%**
437. **`pkg/sourcemap_testing/lib/src/stepping_helper.dart`** -> AI Confidence: **99.31%**
438. **`pkg/vm/bin/kernel_service.dart`** -> AI Confidence: **99.31%**
439. **`pkg/vm/bin/protobuf_aware_treeshaker.dart`** -> AI Confidence: **99.31%**
440. **`pkg/vm/tool/generate_entry_point_shims.dart`** -> AI Confidence: **99.31%**
441. **`pkg/vm_snapshot_analysis/lib/src/commands/summary.dart`** -> AI Confidence: **99.31%**
442. **`runtime/tests/concurrency/generate_stress_test_list.dart`** -> AI Confidence: **99.31%**
443. **`runtime/tools/dartfuzz/dartfuzz_test.dart`** -> AI Confidence: **99.31%**
444. **`runtime/tools/dartfuzz/gen_api_table.dart`** -> AI Confidence: **99.31%**
445. **`runtime/tools/dartfuzz/gen_type_table.dart`** -> AI Confidence: **99.31%**
446. **`runtime/tools/heapsnapshot/lib/src/cli.dart`** -> AI Confidence: **99.31%**
447. **`sdk/lib/_internal/vm/bin/builtin.dart`** -> AI Confidence: **99.31%**
448. **`tests/ffi/generator/address_of_test_generator.dart`** -> AI Confidence: **99.31%**
449. **`tests/ffi/generator/structs_by_value_tests_generator.dart`** -> AI Confidence: **99.31%**
450. **`runtime/bin/console_posix.cc`** -> AI Confidence: **99.31%**
451. **`runtime/bin/console_win.cc`** -> AI Confidence: **99.31%**
452. **`runtime/bin/crashpad.cc`** -> AI Confidence: **99.31%**
453. **`runtime/bin/crypto_linux.cc`** -> AI Confidence: **99.31%**
454. **`runtime/bin/dartdev.cc`** -> AI Confidence: **99.31%**
455. **`runtime/bin/dfe.cc`** -> AI Confidence: **99.31%**
456. **`runtime/bin/directory.cc`** -> AI Confidence: **99.31%**
457. **`runtime/bin/directory_fuchsia.cc`** -> AI Confidence: **99.31%**
458. **`runtime/bin/directory_linux.cc`** -> AI Confidence: **99.31%**
459. **`runtime/bin/directory_macos.cc`** -> AI Confidence: **99.31%**
460. **`runtime/bin/elf_loader.cc`** -> AI Confidence: **99.31%**
461. **`runtime/bin/eventhandler_win.cc`** -> AI Confidence: **99.31%**
462. **`runtime/bin/file.cc`** -> AI Confidence: **99.31%**
463. **`runtime/bin/file_fuchsia.cc`** -> AI Confidence: **99.31%**
464. **`runtime/bin/file_linux.cc`** -> AI Confidence: **99.31%**
465. **`runtime/bin/file_macos.cc`** -> AI Confidence: **99.31%**
466. **`runtime/bin/file_support.cc`** -> AI Confidence: **99.31%**
467. **`runtime/bin/file_system_watcher_linux.cc`** -> AI Confidence: **99.31%**
468. **`runtime/bin/file_win.cc`** -> AI Confidence: **99.31%**
469. **`runtime/bin/ifaddrs.cc`** -> AI Confidence: **99.31%**
470. **`runtime/bin/loader.cc`** -> AI Confidence: **99.31%**
471. **`runtime/bin/macho_loader.cc`** -> AI Confidence: **99.31%**
472. **`runtime/bin/main_impl.cc`** -> AI Confidence: **99.31%**
473. **`runtime/bin/main_options.cc`** -> AI Confidence: **99.31%**
474. **`runtime/bin/namespace_fuchsia.cc`** -> AI Confidence: **99.31%**
475. **`runtime/bin/native_assets_api_impl.cc`** -> AI Confidence: **99.31%**
476. **`runtime/bin/process.cc`** -> AI Confidence: **99.31%**
477. **`runtime/bin/process_fuchsia.cc`** -> AI Confidence: **99.31%**
478. **`runtime/bin/process_linux.cc`** -> AI Confidence: **99.31%**
479. **`runtime/bin/process_macos.cc`** -> AI Confidence: **99.31%**
480. **`runtime/bin/process_win.cc`** -> AI Confidence: **99.31%**
481. **`runtime/bin/run_vm_tests.cc`** -> AI Confidence: **99.31%**
482. **`runtime/bin/secure_socket_utils.cc`** -> AI Confidence: **99.31%**
483. **`runtime/bin/security_context.cc`** -> AI Confidence: **99.31%**
484. **`runtime/bin/security_context_linux.cc`** -> AI Confidence: **99.31%**
485. **`runtime/bin/security_context_win.cc`** -> AI Confidence: **99.31%**
486. **`runtime/bin/snapshot_utils.cc`** -> AI Confidence: **99.31%**
487. **`runtime/bin/socket.cc`** -> AI Confidence: **99.31%**
488. **`runtime/bin/socket_base.cc`** -> AI Confidence: **99.31%**
489. **`runtime/bin/socket_base_linux.cc`** -> AI Confidence: **99.31%**
490. **`runtime/bin/socket_base_macos.cc`** -> AI Confidence: **99.31%**
491. **`runtime/bin/socket_base_posix.cc`** -> AI Confidence: **99.31%**
492. **`runtime/bin/socket_base_win.cc`** -> AI Confidence: **99.31%**
493. **`runtime/bin/socket_fuchsia.cc`** -> AI Confidence: **99.31%**
494. **`runtime/bin/socket_linux.cc`** -> AI Confidence: **99.31%**
495. **`runtime/bin/stdio.cc`** -> AI Confidence: **99.31%**
496. **`runtime/bin/sync_socket.cc`** -> AI Confidence: **99.31%**
497. **`runtime/bin/virtual_memory_fuchsia.cc`** -> AI Confidence: **99.31%**
498. **`runtime/engine/engine.cc`** -> AI Confidence: **99.31%**
499. **`runtime/platform/utils.cc`** -> AI Confidence: **99.31%**
500. **`runtime/vm/analyze_snapshot_api_impl.cc`** -> AI Confidence: **99.31%**
501. **`runtime/vm/bootstrap.cc`** -> AI Confidence: **99.31%**
502. **`runtime/vm/class_finalizer.cc`** -> AI Confidence: **99.31%**
503. **`runtime/vm/class_table.cc`** -> AI Confidence: **99.31%**
504. **`runtime/vm/code_patcher_x64.cc`** -> AI Confidence: **99.31%**
505. **`runtime/vm/compiler/aot/aot_call_specializer.cc`** -> AI Confidence: **99.31%**
506. **`runtime/vm/compiler/aot/precompiler.cc`** -> AI Confidence: **99.31%**
507. **`runtime/vm/compiler/assembler/assembler.h`** -> AI Confidence: **99.31%**
508. **`runtime/vm/compiler/assembler/assembler_base.cc`** -> AI Confidence: **99.31%**
509. **`runtime/vm/compiler/assembler/assembler_riscv.cc`** -> AI Confidence: **99.31%**
510. **`runtime/vm/compiler/assembler/assembler_x64.cc`** -> AI Confidence: **99.31%**
511. **`runtime/vm/compiler/backend/constant_propagator.cc`** -> AI Confidence: **99.31%**
512. **`runtime/vm/compiler/backend/flow_graph_compiler_ia32.cc`** -> AI Confidence: **99.31%**
513. **`runtime/vm/compiler/backend/il.cc`** -> AI Confidence: **99.31%**
514. **`runtime/vm/compiler/backend/il_printer.cc`** -> AI Confidence: **99.31%**
515. **`runtime/vm/compiler/backend/il_serializer.cc`** -> AI Confidence: **99.31%**
516. **`runtime/vm/compiler/backend/il_test_helper.cc`** -> AI Confidence: **99.31%**
517. **`runtime/vm/compiler/backend/locations.cc`** -> AI Confidence: **99.31%**
518. **`runtime/vm/compiler/backend/redundancy_elimination.cc`** -> AI Confidence: **99.31%**
519. **`runtime/vm/compiler/backend/slot.cc`** -> AI Confidence: **99.31%**
520. **`runtime/vm/compiler/backend/type_propagator.cc`** -> AI Confidence: **99.31%**
521. **`runtime/vm/compiler/cha.cc`** -> AI Confidence: **99.31%**
522. **`runtime/vm/compiler/compiler_pass.cc`** -> AI Confidence: **99.31%**
523. **`runtime/vm/compiler/compiler_state.cc`** -> AI Confidence: **99.31%**
524. **`runtime/vm/compiler/frontend/flow_graph_builder.cc`** -> AI Confidence: **99.31%**
525. **`runtime/vm/compiler/frontend/kernel_translation_helper.cc`** -> AI Confidence: **99.31%**
526. **`runtime/vm/compiler/intrinsifier.cc`** -> AI Confidence: **99.31%**
527. **`runtime/vm/compiler/jit/compiler.cc`** -> AI Confidence: **99.31%**
528. **`runtime/vm/compiler/jit/jit_call_specializer.cc`** -> AI Confidence: **99.31%**
529. **`runtime/vm/compiler/offsets_extractor.cc`** -> AI Confidence: **99.31%**
530. **`runtime/vm/compiler/stub_code_compiler.cc`** -> AI Confidence: **99.31%**
531. **`runtime/vm/compiler/stub_code_compiler_arm.cc`** -> AI Confidence: **99.31%**
532. **`runtime/vm/compiler/stub_code_compiler_arm64.cc`** -> AI Confidence: **99.31%**
533. **`runtime/vm/compiler/stub_code_compiler_ia32.cc`** -> AI Confidence: **99.31%**
534. **`runtime/vm/compiler/stub_code_compiler_riscv.cc`** -> AI Confidence: **99.31%**
535. **`runtime/vm/compiler/stub_code_compiler_x64.cc`** -> AI Confidence: **99.31%**
536. **`runtime/vm/constants.h`** -> AI Confidence: **99.31%**
537. **`runtime/vm/cpu_arm64.cc`** -> AI Confidence: **99.31%**
538. **`runtime/vm/dart_api_message.h`** -> AI Confidence: **99.31%**
539. **`runtime/vm/debugger_ia32.cc`** -> AI Confidence: **99.31%**
540. **`runtime/vm/dwarf.cc`** -> AI Confidence: **99.31%**
541. **`runtime/vm/elf.cc`** -> AI Confidence: **99.31%**
542. **`runtime/vm/ffi_callback_metadata.cc`** -> AI Confidence: **99.31%**
543. **`runtime/vm/handles.cc`** -> AI Confidence: **99.31%**
544. **`runtime/vm/heap/become.cc`** -> AI Confidence: **99.31%**
545. **`runtime/vm/heap/compactor.cc`** -> AI Confidence: **99.31%**
546. **`runtime/vm/heap/freelist.cc`** -> AI Confidence: **99.31%**
547. **`runtime/vm/heap/incremental_compactor.cc`** -> AI Confidence: **99.31%**
548. **`runtime/vm/heap/pages.cc`** -> AI Confidence: **99.31%**
549. **`runtime/vm/heap/sampler.cc`** -> AI Confidence: **99.31%**
550. **`runtime/vm/heap/scavenger.cc`** -> AI Confidence: **99.31%**
551. **`runtime/vm/heap/sweeper.cc`** -> AI Confidence: **99.31%**
552. **`runtime/vm/heap/weak_code.cc`** -> AI Confidence: **99.31%**
553. **`runtime/vm/image_snapshot.cc`** -> AI Confidence: **99.31%**
554. **`runtime/vm/instructions_arm64.cc`** -> AI Confidence: **99.31%**
555. **`runtime/vm/instructions_riscv.cc`** -> AI Confidence: **99.31%**
556. **`runtime/vm/instructions_x64.cc`** -> AI Confidence: **99.31%**
557. **`runtime/vm/isolate.cc`** -> AI Confidence: **99.31%**
558. **`runtime/vm/isolate_reload.cc`** -> AI Confidence: **99.31%**
559. **`runtime/vm/json_stream.cc`** -> AI Confidence: **99.31%**
560. **`runtime/vm/kernel.cc`** -> AI Confidence: **99.31%**
561. **`runtime/vm/kernel_binary.cc`** -> AI Confidence: **99.31%**
562. **`runtime/vm/kernel_isolate.cc`** -> AI Confidence: **99.31%**
563. **`runtime/vm/kernel_loader.cc`** -> AI Confidence: **99.31%**
564. **`runtime/vm/libfuzzer/dart_libfuzzer.cc`** -> AI Confidence: **99.31%**
565. **`runtime/vm/mach_o.cc`** -> AI Confidence: **99.31%**
566. **`runtime/vm/megamorphic_cache_table.cc`** -> AI Confidence: **99.31%**
567. **`runtime/vm/message.cc`** -> AI Confidence: **99.31%**
568. **`runtime/vm/message_snapshot.cc`** -> AI Confidence: **99.31%**
569. **`runtime/vm/metrics.cc`** -> AI Confidence: **99.31%**
570. **`runtime/vm/module_snapshot.cc`** -> AI Confidence: **99.31%**
571. **`runtime/vm/native_api_impl.cc`** -> AI Confidence: **99.31%**
572. **`runtime/vm/object.cc`** -> AI Confidence: **99.31%**
573. **`runtime/vm/object_graph.cc`** -> AI Confidence: **99.31%**
574. **`runtime/vm/object_reload.cc`** -> AI Confidence: **99.31%**
575. **`runtime/vm/object_service.cc`** -> AI Confidence: **99.31%**
576. **`runtime/vm/os_android.cc`** -> AI Confidence: **99.31%**
577. **`runtime/vm/os_linux.cc`** -> AI Confidence: **99.31%**
578. **`runtime/vm/os_thread.cc`** -> AI Confidence: **99.31%**
579. **`runtime/vm/profiler.cc`** -> AI Confidence: **99.31%**
580. **`runtime/vm/profiler_service.cc`** -> AI Confidence: **99.31%**
581. **`runtime/vm/raw_object.cc`** -> AI Confidence: **99.31%**
582. **`runtime/vm/regexp/regexp-compiler.cc`** -> AI Confidence: **99.31%**
583. **`runtime/vm/regexp/regexp-macro-assembler.cc`** -> AI Confidence: **99.31%**
584. **`runtime/vm/regexp/regexp-parser.cc`** -> AI Confidence: **99.31%**
585. **`runtime/vm/regexp/regexp.cc`** -> AI Confidence: **99.31%**
586. **`runtime/vm/report.cc`** -> AI Confidence: **99.31%**
587. **`runtime/vm/resolver.cc`** -> AI Confidence: **99.31%**
588. **`runtime/vm/runtime_entry.cc`** -> AI Confidence: **99.31%**
589. **`runtime/vm/service.cc`** -> AI Confidence: **99.31%**
590. **`runtime/vm/service_isolate.cc`** -> AI Confidence: **99.31%**
591. **`runtime/vm/stack_frame.cc`** -> AI Confidence: **99.31%**
592. **`runtime/vm/stub_code.cc`** -> AI Confidence: **99.31%**
593. **`runtime/vm/symbols.cc`** -> AI Confidence: **99.31%**
594. **`runtime/vm/tags.cc`** -> AI Confidence: **99.31%**
595. **`runtime/vm/thread.cc`** -> AI Confidence: **99.31%**
596. **`runtime/vm/thread_interrupter_android.cc`** -> AI Confidence: **99.31%**
597. **`runtime/vm/thread_interrupter_fuchsia.cc`** -> AI Confidence: **99.31%**
598. **`runtime/vm/thread_interrupter_macos.cc`** -> AI Confidence: **99.31%**
599. **`runtime/vm/timeline.cc`** -> AI Confidence: **99.31%**
600. **`runtime/vm/type_testing_stubs.cc`** -> AI Confidence: **99.31%**
601. **`runtime/vm/virtual_memory_posix.cc`** -> AI Confidence: **99.31%**
602. **`runtime/vm/virtual_memory_win.cc`** -> AI Confidence: **99.31%**
603. **`pkg/compiler/tool/szcmp`** -> AI Confidence: **99.29%**
604. **`pkg/dart2js_info/tool/update_proto.sh`** -> AI Confidence: **99.29%**
605. **`pkg/dart2wasm/tool/run_benchmark`** -> AI Confidence: **99.29%**
606. **`pkg/front_end/tool/cfe`** -> AI Confidence: **99.29%**
607. **`pkg/vm/tool/gen_kernel`** -> AI Confidence: **99.29%**
608. **`sdk/bin/dart`** -> AI Confidence: **99.29%**
609. **`tools/dom/scripts/go.sh`** -> AI Confidence: **99.29%**
610. **`tools/debian_package/BUILD.gn`** -> AI Confidence: **99.29%**
611. **`benchmarks/MapLookup/generate_maps.dart`** -> AI Confidence: **99.29%**
612. **`benchmarks/SwitchFSM/dart/match_class.dart`** -> AI Confidence: **99.29%**
613. **`benchmarks/SwitchFSM/dart/match_enum.dart`** -> AI Confidence: **99.29%**
614. **`benchmarks/SwitchFSM/dart/match_int.dart`** -> AI Confidence: **99.29%**
615. **`benchmarks/SwitchFSM/dart/match_string.dart`** -> AI Confidence: **99.29%**
616. **`pkg/_fe_analyzer_shared/lib/src/debug_helpers/print.dart`** -> AI Confidence: **99.29%**
617. **`pkg/_fe_analyzer_shared/lib/src/exhaustiveness/types/record.dart`** -> AI Confidence: **99.29%**
618. **`pkg/_fe_analyzer_shared/lib/src/flow_analysis/factory_type_test_helper.dart`** -> AI Confidence: **99.29%**
619. **`pkg/_fe_analyzer_shared/lib/src/metadata/elements.dart`** -> AI Confidence: **99.29%**
620. **`pkg/_fe_analyzer_shared/lib/src/metadata/util.dart`** -> AI Confidence: **99.29%**
621. **`pkg/_fe_analyzer_shared/lib/src/sdk/allowed_experiments.dart`** -> AI Confidence: **99.29%**
622. **`pkg/_fe_analyzer_shared/lib/src/testing/features.dart`** -> AI Confidence: **99.29%**
623. **`pkg/_fe_analyzer_shared/lib/src/testing/metadata_helper.dart`** -> AI Confidence: **99.29%**
624. **`pkg/_fe_analyzer_shared/lib/src/type_inference/shared_inference_log.dart`** -> AI Confidence: **99.29%**
625. **`pkg/analyzer/lib/src/dart/ast/ast.g.dart`** -> AI Confidence: **99.29%**
626. **`pkg/analyzer/lib/src/test_utilities/function_ast_visitor.dart`** -> AI Confidence: **99.29%**
627. **`pkg/analyzer/lib/src/util/graph.dart`** -> AI Confidence: **99.29%**
628. **`pkg/analyzer_plugin/lib/src/utilities/library.dart`** -> AI Confidence: **99.29%**
629. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/material/app_bar.dart`** -> AI Confidence: **99.29%**
630. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/material/ink_well.dart`** -> AI Confidence: **99.29%**
631. **`pkg/analyzer_testing/lib/src/mock_packages/flutter/widgets/gesture_detector.dart`** -> AI Confidence: **99.29%**
632. **`pkg/cfg/testcases/constant_propagation.dart`** -> AI Confidence: **99.29%**
633. **`pkg/cfg/testcases/dominators.dart`** -> AI Confidence: **99.29%**
634. **`pkg/cfg/testcases/expressions.dart`** -> AI Confidence: **99.29%**
635. **`pkg/cfg/testcases/loops.dart`** -> AI Confidence: **99.29%**
636. **`pkg/cfg/testcases/value_numbering.dart`** -> AI Confidence: **99.29%**
637. **`pkg/compiler/lib/src/js_emitter/interceptor_stub_generator.dart`** -> AI Confidence: **99.29%**
638. **`pkg/compiler/lib/src/serialization/sink.dart`** -> AI Confidence: **99.29%**
639. **`pkg/compiler/test/sourcemaps/tools/translate_dart2js_stacktrace.dart`** -> AI Confidence: **99.29%**
640. **`pkg/dart2bytecode/testcases/switch.dart`** -> AI Confidence: **99.29%**
641. **`pkg/dart2bytecode/testcases/try_blocks.dart`** -> AI Confidence: **99.29%**
642. **`pkg/dart2wasm/bin/wasm2wat.dart`** -> AI Confidence: **99.29%**
643. **`pkg/dart_data_home/lib/src/pid_files.dart`** -> AI Confidence: **99.29%**
644. **`pkg/dartdev/test/data/dart_app/bin/dart_app.dart`** -> AI Confidence: **99.29%**
645. **`pkg/front_end/lib/src/base/file_system_dependency_tracker.dart`** -> AI Confidence: **99.29%**
646. **`pkg/front_end/lib/src/dill/dill_extension_type_declaration_builder.dart`** -> AI Confidence: **99.29%**
647. **`pkg/front_end/lib/src/kernel/member_covariance.dart`** -> AI Confidence: **99.29%**
648. **`pkg/front_end/lib/src/source/source_extension_type_declaration_builder.dart`** -> AI Confidence: **99.29%**
649. **`pkg/front_end/parser_testcases/also-nnbd/issue_40267_conditional.dart`** -> AI Confidence: **99.29%**
650. **`pkg/front_end/parser_testcases/error_recovery/bad_variable_in_if.dart`** -> AI Confidence: **99.29%**
651. **`pkg/front_end/parser_testcases/error_recovery/empty_for.dart`** -> AI Confidence: **99.29%**
652. **`pkg/front_end/parser_testcases/error_recovery/for_in_with_colon.dart`** -> AI Confidence: **99.29%**
653. **`pkg/front_end/parser_testcases/error_recovery/issue_50908.dart`** -> AI Confidence: **99.29%**
654. **`pkg/front_end/parser_testcases/error_recovery/with_outline/typing_15.dart`** -> AI Confidence: **99.29%**
655. **`pkg/front_end/parser_testcases/general/ambiguous_builder_01.dart`** -> AI Confidence: **99.29%**
656. **`pkg/front_end/parser_testcases/general/call_on_after_try_block.dart`** -> AI Confidence: **99.29%**
657. **`pkg/front_end/parser_testcases/general/call_on_after_try_block2.dart`** -> AI Confidence: **99.29%**
658. **`pkg/front_end/parser_testcases/general/call_on_after_try_block2_prime.dart`** -> AI Confidence: **99.29%**
659. **`pkg/front_end/parser_testcases/general/call_on_after_try_block3.dart`** -> AI Confidence: **99.29%**
660. **`pkg/front_end/parser_testcases/general/call_on_after_try_block3_prime.dart`** -> AI Confidence: **99.29%**
661. **`pkg/front_end/parser_testcases/general/call_on_after_try_block4.dart`** -> AI Confidence: **99.29%**
662. **`pkg/front_end/parser_testcases/general/call_on_after_try_block4_prime.dart`** -> AI Confidence: **99.29%**
663. **`pkg/front_end/parser_testcases/general/call_on_after_try_block5.dart`** -> AI Confidence: **99.29%**
664. **`pkg/front_end/parser_testcases/general/call_on_after_try_block5_prime.dart`** -> AI Confidence: **99.29%**
665. **`pkg/front_end/parser_testcases/general/call_on_after_try_block_prime.dart`** -> AI Confidence: **99.29%**
666. **`pkg/front_end/parser_testcases/general/for.dart`** -> AI Confidence: **99.29%**
667. **`pkg/front_end/parser_testcases/general/for_no_decl.dart`** -> AI Confidence: **99.29%**
668. **`pkg/front_end/parser_testcases/general/not_call_on_after_try_block.dart`** -> AI Confidence: **99.29%**
669. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_01.dart`** -> AI Confidence: **99.29%**
670. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_01_2.dart`** -> AI Confidence: **99.29%**
671. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_02.dart`** -> AI Confidence: **99.29%**
672. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_02_2.dart`** -> AI Confidence: **99.29%**
673. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_03.dart`** -> AI Confidence: **99.29%**
674. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_03_2.dart`** -> AI Confidence: **99.29%**
675. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_04.dart`** -> AI Confidence: **99.29%**
676. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_04_2.dart`** -> AI Confidence: **99.29%**
677. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_05.dart`** -> AI Confidence: **99.29%**
678. **`pkg/front_end/parser_testcases/nnbd/issue_40267_case_05_2.dart`** -> AI Confidence: **99.29%**
679. **`pkg/front_end/parser_testcases/nnbd/issue_40267_conditional.dart`** -> AI Confidence: **99.29%**
680. **`pkg/front_end/parser_testcases/nnbd/issue_40267_lookup_plus.dart`** -> AI Confidence: **99.29%**
681. **`pkg/front_end/parser_testcases/nnbd/issue_40267_lookup_plus_plus.dart`** -> AI Confidence: **99.29%**
682. **`pkg/front_end/parser_testcases/nnbd/issue_40267_plus_plus_lookup.dart`** -> AI Confidence: **99.29%**
683. **`pkg/front_end/parser_testcases/nnbd/issue_40793.dart`** -> AI Confidence: **99.29%**
684. **`pkg/front_end/parser_testcases/nnbd/issue_40793_prime.dart`** -> AI Confidence: **99.29%**
685. **`pkg/front_end/parser_testcases/nnbd/issue_40793_prime2.dart`** -> AI Confidence: **99.29%**
686. **`pkg/front_end/parser_testcases/nnbd/issue_40793_prime3.dart`** -> AI Confidence: **99.29%**
687. **`pkg/front_end/parser_testcases/nnbd/issue_40834_01.dart`** -> AI Confidence: **99.29%**
688. **`pkg/front_end/parser_testcases/nnbd/issue_40834_03.dart`** -> AI Confidence: **99.29%**
689. **`pkg/front_end/parser_testcases/nnbd/issue_41177.dart`** -> AI Confidence: **99.29%**
690. **`pkg/front_end/parser_testcases/nnbd/issue_47020.dart`** -> AI Confidence: **99.29%**
691. **`pkg/front_end/parser_testcases/nnbd/issue_48999.dart`** -> AI Confidence: **99.29%**
692. **`pkg/front_end/parser_testcases/nnbd/issue_48999_prime.dart`** -> AI Confidence: **99.29%**
693. **`pkg/front_end/parser_testcases/nnbd/issue_49132.dart`** -> AI Confidence: **99.29%**
694. **`pkg/front_end/parser_testcases/nnbd/issue_49132_not_nullable.dart`** -> AI Confidence: **99.29%**
695. **`pkg/front_end/parser_testcases/nnbd/issue_49132_prime.dart`** -> AI Confidence: **99.29%**
696. **`pkg/front_end/parser_testcases/null_aware_elements/split_question_period.dart`** -> AI Confidence: **99.29%**
697. **`pkg/front_end/parser_testcases/null_aware_elements/unsplit_question_period.dart`** -> AI Confidence: **99.29%**
698. **`pkg/front_end/parser_testcases/patterns/assignedVariable_namedWhen.dart`** -> AI Confidence: **99.29%**
699. **`pkg/front_end/parser_testcases/patterns/boolean_literal_inside_case.dart`** -> AI Confidence: **99.29%**
700. **`pkg/front_end/parser_testcases/patterns/boolean_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
701. **`pkg/front_end/parser_testcases/patterns/boolean_literal_inside_if_case.dart`** -> AI Confidence: **99.29%**
702. **`pkg/front_end/parser_testcases/patterns/boolean_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
703. **`pkg/front_end/parser_testcases/patterns/boolean_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
704. **`pkg/front_end/parser_testcases/patterns/caseHead_withClassicPattern_guarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
705. **`pkg/front_end/parser_testcases/patterns/caseHead_withClassicPattern_guarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
706. **`pkg/front_end/parser_testcases/patterns/caseHead_withClassicPattern_unguarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
707. **`pkg/front_end/parser_testcases/patterns/caseHead_withClassicPattern_unguarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
708. **`pkg/front_end/parser_testcases/patterns/caseHead_withNewPattern_guarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
709. **`pkg/front_end/parser_testcases/patterns/caseHead_withNewPattern_guarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
710. **`pkg/front_end/parser_testcases/patterns/caseHead_withNewPattern_unguarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
711. **`pkg/front_end/parser_testcases/patterns/caseHead_withNewPattern_unguarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
712. **`pkg/front_end/parser_testcases/patterns/case_identifier_dot_incomplete.dart`** -> AI Confidence: **99.29%**
713. **`pkg/front_end/parser_testcases/patterns/cast_insideCast.dart`** -> AI Confidence: **99.29%**
714. **`pkg/front_end/parser_testcases/patterns/cast_insideCast_parenthesized.dart`** -> AI Confidence: **99.29%**
715. **`pkg/front_end/parser_testcases/patterns/cast_insideNullAssert.dart`** -> AI Confidence: **99.29%**
716. **`pkg/front_end/parser_testcases/patterns/cast_insideNullCheck.dart`** -> AI Confidence: **99.29%**
717. **`pkg/front_end/parser_testcases/patterns/cast_inside_case.dart`** -> AI Confidence: **99.29%**
718. **`pkg/front_end/parser_testcases/patterns/cast_inside_extractor_pattern.dart`** -> AI Confidence: **99.29%**
719. **`pkg/front_end/parser_testcases/patterns/cast_inside_list_pattern.dart`** -> AI Confidence: **99.29%**
720. **`pkg/front_end/parser_testcases/patterns/cast_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
721. **`pkg/front_end/parser_testcases/patterns/cast_inside_logical_and_rhs.dart`** -> AI Confidence: **99.29%**
722. **`pkg/front_end/parser_testcases/patterns/cast_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
723. **`pkg/front_end/parser_testcases/patterns/cast_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
724. **`pkg/front_end/parser_testcases/patterns/cast_inside_map_pattern.dart`** -> AI Confidence: **99.29%**
725. **`pkg/front_end/parser_testcases/patterns/cast_inside_parenthesized_pattern.dart`** -> AI Confidence: **99.29%**
726. **`pkg/front_end/parser_testcases/patterns/cast_inside_record_pattern_named.dart`** -> AI Confidence: **99.29%**
727. **`pkg/front_end/parser_testcases/patterns/cast_inside_record_pattern_unnamed.dart`** -> AI Confidence: **99.29%**
728. **`pkg/front_end/parser_testcases/patterns/const_patterns.dart`** -> AI Confidence: **99.29%**
729. **`pkg/front_end/parser_testcases/patterns/const_patterns_binary.dart`** -> AI Confidence: **99.29%**
730. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_builtin.dart`** -> AI Confidence: **99.29%**
731. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_insideCase.dart`** -> AI Confidence: **99.29%**
732. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_insideCast.dart`** -> AI Confidence: **99.29%**
733. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_insideIfCase.dart`** -> AI Confidence: **99.29%**
734. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
735. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
736. **`pkg/front_end/parser_testcases/patterns/constant_identifier_doublyPrefixed_pseudoKeyword.dart`** -> AI Confidence: **99.29%**
737. **`pkg/front_end/parser_testcases/patterns/constant_identifier_inside_case.dart`** -> AI Confidence: **99.29%**
738. **`pkg/front_end/parser_testcases/patterns/constant_identifier_inside_cast.dart`** -> AI Confidence: **99.29%**
739. **`pkg/front_end/parser_testcases/patterns/constant_identifier_inside_if_case.dart`** -> AI Confidence: **99.29%**
740. **`pkg/front_end/parser_testcases/patterns/constant_identifier_inside_null_assert.dart`** -> AI Confidence: **99.29%**
741. **`pkg/front_end/parser_testcases/patterns/constant_identifier_inside_null_check.dart`** -> AI Confidence: **99.29%**
742. **`pkg/front_end/parser_testcases/patterns/constant_identifier_namedAs.dart`** -> AI Confidence: **99.29%**
743. **`pkg/front_end/parser_testcases/patterns/constant_identifier_namedWhen.dart`** -> AI Confidence: **99.29%**
744. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixedWithUnderscore_insideCase.dart`** -> AI Confidence: **99.29%**
745. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_builtin.dart`** -> AI Confidence: **99.29%**
746. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_insideCase.dart`** -> AI Confidence: **99.29%**
747. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_insideCast.dart`** -> AI Confidence: **99.29%**
748. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_insideIfCase.dart`** -> AI Confidence: **99.29%**
749. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
750. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
751. **`pkg/front_end/parser_testcases/patterns/constant_identifier_prefixed_pseudoKeyword.dart`** -> AI Confidence: **99.29%**
752. **`pkg/front_end/parser_testcases/patterns/constant_identifier_unprefixed_beforeWhen.dart`** -> AI Confidence: **99.29%**
753. **`pkg/front_end/parser_testcases/patterns/constant_identifier_unprefixed_builtin.dart`** -> AI Confidence: **99.29%**
754. **`pkg/front_end/parser_testcases/patterns/constant_identifier_unprefixed_pseudoKeyword.dart`** -> AI Confidence: **99.29%**
755. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_empty_insideCase.dart`** -> AI Confidence: **99.29%**
756. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_empty_insideCast.dart`** -> AI Confidence: **99.29%**
757. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_empty_insideIfCase.dart`** -> AI Confidence: **99.29%**
758. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_empty_insideNullAssert.dart`** -> AI Confidence: **99.29%**
759. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_empty_insideNullCheck.dart`** -> AI Confidence: **99.29%**
760. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_nonEmpty_insideCase.dart`** -> AI Confidence: **99.29%**
761. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_nonEmpty_insideCast.dart`** -> AI Confidence: **99.29%**
762. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_nonEmpty_insideIfCase.dart`** -> AI Confidence: **99.29%**
763. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_nonEmpty_insideNullAssert.dart`** -> AI Confidence: **99.29%**
764. **`pkg/front_end/parser_testcases/patterns/constant_list_typed_nonEmpty_insideNullCheck.dart`** -> AI Confidence: **99.29%**
765. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_empty_insideCase.dart`** -> AI Confidence: **99.29%**
766. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_empty_insideCast.dart`** -> AI Confidence: **99.29%**
767. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_empty_insideIfCase.dart`** -> AI Confidence: **99.29%**
768. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_empty_insideNullAssert.dart`** -> AI Confidence: **99.29%**
769. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_empty_insideNullCheck.dart`** -> AI Confidence: **99.29%**
770. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_nonEmpty_insideCase.dart`** -> AI Confidence: **99.29%**
771. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_nonEmpty_insideCast.dart`** -> AI Confidence: **99.29%**
772. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_nonEmpty_insideIfCase.dart`** -> AI Confidence: **99.29%**
773. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_nonEmpty_insideNullAssert.dart`** -> AI Confidence: **99.29%**
774. **`pkg/front_end/parser_testcases/patterns/constant_list_untyped_nonEmpty_insideNullCheck.dart`** -> AI Confidence: **99.29%**
775. **`pkg/front_end/parser_testcases/patterns/constant_map_typed_insideCase.dart`** -> AI Confidence: **99.29%**
776. **`pkg/front_end/parser_testcases/patterns/constant_map_typed_insideCast.dart`** -> AI Confidence: **99.29%**
777. **`pkg/front_end/parser_testcases/patterns/constant_map_typed_insideIfCase.dart`** -> AI Confidence: **99.29%**
778. **`pkg/front_end/parser_testcases/patterns/constant_map_typed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
779. **`pkg/front_end/parser_testcases/patterns/constant_map_typed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
780. **`pkg/front_end/parser_testcases/patterns/constant_map_untyped_insideCase.dart`** -> AI Confidence: **99.29%**
781. **`pkg/front_end/parser_testcases/patterns/constant_map_untyped_insideCast.dart`** -> AI Confidence: **99.29%**
782. **`pkg/front_end/parser_testcases/patterns/constant_map_untyped_insideIfCase.dart`** -> AI Confidence: **99.29%**
783. **`pkg/front_end/parser_testcases/patterns/constant_map_untyped_insideNullAssert.dart`** -> AI Confidence: **99.29%**
784. **`pkg/front_end/parser_testcases/patterns/constant_map_untyped_insideNullCheck.dart`** -> AI Confidence: **99.29%**
785. **`pkg/front_end/parser_testcases/patterns/constant_objectExpression_insideCase.dart`** -> AI Confidence: **99.29%**
786. **`pkg/front_end/parser_testcases/patterns/constant_objectExpression_insideCast.dart`** -> AI Confidence: **99.29%**
787. **`pkg/front_end/parser_testcases/patterns/constant_objectExpression_insideIfCase.dart`** -> AI Confidence: **99.29%**
788. **`pkg/front_end/parser_testcases/patterns/constant_objectExpression_insideNullAssert.dart`** -> AI Confidence: **99.29%**
789. **`pkg/front_end/parser_testcases/patterns/constant_objectExpression_insideNullCheck.dart`** -> AI Confidence: **99.29%**
790. **`pkg/front_end/parser_testcases/patterns/constant_parenthesized_insideCase.dart`** -> AI Confidence: **99.29%**
791. **`pkg/front_end/parser_testcases/patterns/constant_parenthesized_insideCast.dart`** -> AI Confidence: **99.29%**
792. **`pkg/front_end/parser_testcases/patterns/constant_parenthesized_insideIfCase.dart`** -> AI Confidence: **99.29%**
793. **`pkg/front_end/parser_testcases/patterns/constant_parenthesized_insideNullAssert.dart`** -> AI Confidence: **99.29%**
794. **`pkg/front_end/parser_testcases/patterns/constant_parenthesized_insideNullCheck.dart`** -> AI Confidence: **99.29%**
795. **`pkg/front_end/parser_testcases/patterns/constant_set_typed_insideCase.dart`** -> AI Confidence: **99.29%**
796. **`pkg/front_end/parser_testcases/patterns/constant_set_typed_insideCast.dart`** -> AI Confidence: **99.29%**
797. **`pkg/front_end/parser_testcases/patterns/constant_set_typed_insideIfCase.dart`** -> AI Confidence: **99.29%**
798. **`pkg/front_end/parser_testcases/patterns/constant_set_typed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
799. **`pkg/front_end/parser_testcases/patterns/constant_set_typed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
800. **`pkg/front_end/parser_testcases/patterns/constant_set_untyped_insideCase.dart`** -> AI Confidence: **99.29%**
801. **`pkg/front_end/parser_testcases/patterns/constant_set_untyped_insideCast.dart`** -> AI Confidence: **99.29%**
802. **`pkg/front_end/parser_testcases/patterns/constant_set_untyped_insideNullAssert.dart`** -> AI Confidence: **99.29%**
803. **`pkg/front_end/parser_testcases/patterns/constant_set_untyped_insideNullCheck.dart`** -> AI Confidence: **99.29%**
804. **`pkg/front_end/parser_testcases/patterns/double_literal_inside_case.dart`** -> AI Confidence: **99.29%**
805. **`pkg/front_end/parser_testcases/patterns/double_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
806. **`pkg/front_end/parser_testcases/patterns/double_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
807. **`pkg/front_end/parser_testcases/patterns/double_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
808. **`pkg/front_end/parser_testcases/patterns/error_recovery_after_question_suffix_in_expression.dart`** -> AI Confidence: **99.29%**
809. **`pkg/front_end/parser_testcases/patterns/extractor_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
810. **`pkg/front_end/parser_testcases/patterns/extractor_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
811. **`pkg/front_end/parser_testcases/patterns/extractor_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
812. **`pkg/front_end/parser_testcases/patterns/extractor_pattern_with_type_args_inside_null_assert.dart`** -> AI Confidence: **99.29%**
813. **`pkg/front_end/parser_testcases/patterns/extractor_prefixedNamedUnderscore_withTypeArgs_insideCase.dart`** -> AI Confidence: **99.29%**
814. **`pkg/front_end/parser_testcases/patterns/extractor_prefixedNamedUnderscore_withoutTypeArgs_insideCase.dart`** -> AI Confidence: **99.29%**
815. **`pkg/front_end/parser_testcases/patterns/extractor_unprefixedNamedUnderscore_withTypeArgs_insideCase.dart`** -> AI Confidence: **99.29%**
816. **`pkg/front_end/parser_testcases/patterns/extractor_unprefixedNamedUnderscore_withoutTypeArgs_insideCase.dart`** -> AI Confidence: **99.29%**
817. **`pkg/front_end/parser_testcases/patterns/final_variable_inside_case.dart`** -> AI Confidence: **99.29%**
818. **`pkg/front_end/parser_testcases/patterns/final_variable_inside_cast.dart`** -> AI Confidence: **99.29%**
819. **`pkg/front_end/parser_testcases/patterns/final_variable_inside_null_assert.dart`** -> AI Confidence: **99.29%**
820. **`pkg/front_end/parser_testcases/patterns/final_variable_inside_null_check.dart`** -> AI Confidence: **99.29%**
821. **`pkg/front_end/parser_testcases/patterns/functionExpression_allowed_insideSwitchStatementInWhenClause.dart`** -> AI Confidence: **99.29%**
822. **`pkg/front_end/parser_testcases/patterns/identifier_as_when.dart`** -> AI Confidence: **99.29%**
823. **`pkg/front_end/parser_testcases/patterns/identifier_when_as.dart`** -> AI Confidence: **99.29%**
824. **`pkg/front_end/parser_testcases/patterns/identifier_when_not.dart`** -> AI Confidence: **99.29%**
825. **`pkg/front_end/parser_testcases/patterns/identifier_when_when.dart`** -> AI Confidence: **99.29%**
826. **`pkg/front_end/parser_testcases/patterns/integer_literal_inside_case.dart`** -> AI Confidence: **99.29%**
827. **`pkg/front_end/parser_testcases/patterns/integer_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
828. **`pkg/front_end/parser_testcases/patterns/integer_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
829. **`pkg/front_end/parser_testcases/patterns/integer_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
830. **`pkg/front_end/parser_testcases/patterns/issue51415.dart`** -> AI Confidence: **99.29%**
831. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_case.dart`** -> AI Confidence: **99.29%**
832. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_case_empty.dart`** -> AI Confidence: **99.29%**
833. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_case_empty_whitespace.dart`** -> AI Confidence: **99.29%**
834. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_case_with_type_arguments.dart`** -> AI Confidence: **99.29%**
835. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
836. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
837. **`pkg/front_end/parser_testcases/patterns/list_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
838. **`pkg/front_end/parser_testcases/patterns/list_recovery_bogusTokensAfterListElement.dart`** -> AI Confidence: **99.29%**
839. **`pkg/front_end/parser_testcases/patterns/list_recovery_missingClosingBracket.dart`** -> AI Confidence: **99.29%**
840. **`pkg/front_end/parser_testcases/patterns/list_recovery_missingComma.dart`** -> AI Confidence: **99.29%**
841. **`pkg/front_end/parser_testcases/patterns/logical_and_inside_if_case.dart`** -> AI Confidence: **99.29%**
842. **`pkg/front_end/parser_testcases/patterns/logical_and_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
843. **`pkg/front_end/parser_testcases/patterns/logical_and_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
844. **`pkg/front_end/parser_testcases/patterns/logical_and_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
845. **`pkg/front_end/parser_testcases/patterns/logical_or_inside_if_case.dart`** -> AI Confidence: **99.29%**
846. **`pkg/front_end/parser_testcases/patterns/logical_or_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
847. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_case.dart`** -> AI Confidence: **99.29%**
848. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_case_empty.dart`** -> AI Confidence: **99.29%**
849. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_case_with_type_arguments.dart`** -> AI Confidence: **99.29%**
850. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
851. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
852. **`pkg/front_end/parser_testcases/patterns/map_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
853. **`pkg/front_end/parser_testcases/patterns/map_recovery_bogusTokensAfterMapElement.dart`** -> AI Confidence: **99.29%**
854. **`pkg/front_end/parser_testcases/patterns/map_recovery_missingClosingBrace.dart`** -> AI Confidence: **99.29%**
855. **`pkg/front_end/parser_testcases/patterns/map_recovery_missingComma.dart`** -> AI Confidence: **99.29%**
856. **`pkg/front_end/parser_testcases/patterns/nullAssert_insideCast.dart`** -> AI Confidence: **99.29%**
857. **`pkg/front_end/parser_testcases/patterns/nullAssert_insideNullAssert.dart`** -> AI Confidence: **99.29%**
858. **`pkg/front_end/parser_testcases/patterns/nullAssert_insideNullCheck.dart`** -> AI Confidence: **99.29%**
859. **`pkg/front_end/parser_testcases/patterns/nullCheck_insideCast.dart`** -> AI Confidence: **99.29%**
860. **`pkg/front_end/parser_testcases/patterns/nullCheck_insideNullAssert.dart`** -> AI Confidence: **99.29%**
861. **`pkg/front_end/parser_testcases/patterns/nullCheck_insideNullCheck.dart`** -> AI Confidence: **99.29%**
862. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_case.dart`** -> AI Confidence: **99.29%**
863. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_extractor_pattern.dart`** -> AI Confidence: **99.29%**
864. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_list_pattern.dart`** -> AI Confidence: **99.29%**
865. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
866. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_logical_and_rhs.dart`** -> AI Confidence: **99.29%**
867. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
868. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
869. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_map_pattern.dart`** -> AI Confidence: **99.29%**
870. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_parenthesized_pattern.dart`** -> AI Confidence: **99.29%**
871. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_record_pattern_named.dart`** -> AI Confidence: **99.29%**
872. **`pkg/front_end/parser_testcases/patterns/null_assert_inside_record_pattern_unnamed.dart`** -> AI Confidence: **99.29%**
873. **`pkg/front_end/parser_testcases/patterns/null_check_inside_case.dart`** -> AI Confidence: **99.29%**
874. **`pkg/front_end/parser_testcases/patterns/null_check_inside_extractor_pattern.dart`** -> AI Confidence: **99.29%**
875. **`pkg/front_end/parser_testcases/patterns/null_check_inside_list_pattern.dart`** -> AI Confidence: **99.29%**
876. **`pkg/front_end/parser_testcases/patterns/null_check_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
877. **`pkg/front_end/parser_testcases/patterns/null_check_inside_logical_and_rhs.dart`** -> AI Confidence: **99.29%**
878. **`pkg/front_end/parser_testcases/patterns/null_check_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
879. **`pkg/front_end/parser_testcases/patterns/null_check_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
880. **`pkg/front_end/parser_testcases/patterns/null_check_inside_map_pattern.dart`** -> AI Confidence: **99.29%**
881. **`pkg/front_end/parser_testcases/patterns/null_check_inside_parenthesized_pattern.dart`** -> AI Confidence: **99.29%**
882. **`pkg/front_end/parser_testcases/patterns/null_check_inside_record_pattern_implicitly_named.dart`** -> AI Confidence: **99.29%**
883. **`pkg/front_end/parser_testcases/patterns/null_check_inside_record_pattern_named.dart`** -> AI Confidence: **99.29%**
884. **`pkg/front_end/parser_testcases/patterns/null_check_inside_record_pattern_unnamed.dart`** -> AI Confidence: **99.29%**
885. **`pkg/front_end/parser_testcases/patterns/null_literal_inside_case.dart`** -> AI Confidence: **99.29%**
886. **`pkg/front_end/parser_testcases/patterns/null_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
887. **`pkg/front_end/parser_testcases/patterns/null_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
888. **`pkg/front_end/parser_testcases/patterns/null_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
889. **`pkg/front_end/parser_testcases/patterns/object_dynamic.dart`** -> AI Confidence: **99.29%**
890. **`pkg/front_end/parser_testcases/patterns/object_recovery_bogusTokensAfterPatternField.dart`** -> AI Confidence: **99.29%**
891. **`pkg/front_end/parser_testcases/patterns/object_recovery_missingClosingParen.dart`** -> AI Confidence: **99.29%**
892. **`pkg/front_end/parser_testcases/patterns/object_recovery_missingComma.dart`** -> AI Confidence: **99.29%**
893. **`pkg/front_end/parser_testcases/patterns/parenthesized_insideCase.dart`** -> AI Confidence: **99.29%**
894. **`pkg/front_end/parser_testcases/patterns/parenthesized_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
895. **`pkg/front_end/parser_testcases/patterns/parenthesized_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
896. **`pkg/front_end/parser_testcases/patterns/parenthesized_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
897. **`pkg/front_end/parser_testcases/patterns/prefixed_extractor_pattern_with_type_args_inside_null_check.dart`** -> AI Confidence: **99.29%**
898. **`pkg/front_end/parser_testcases/patterns/recordPattern_nonNullable_beforeAs.dart`** -> AI Confidence: **99.29%**
899. **`pkg/front_end/parser_testcases/patterns/recordPattern_nonNullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
900. **`pkg/front_end/parser_testcases/patterns/recordPattern_nullable_beforeAs.dart`** -> AI Confidence: **99.29%**
901. **`pkg/front_end/parser_testcases/patterns/recordPattern_nullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
902. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeAnd.dart`** -> AI Confidence: **99.29%**
903. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeAs.dart`** -> AI Confidence: **99.29%**
904. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeColon.dart`** -> AI Confidence: **99.29%**
905. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeComma.dart`** -> AI Confidence: **99.29%**
906. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeExclamation.dart`** -> AI Confidence: **99.29%**
907. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeOr.dart`** -> AI Confidence: **99.29%**
908. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeQuestion.dart`** -> AI Confidence: **99.29%**
909. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeRightBrace.dart`** -> AI Confidence: **99.29%**
910. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeRightBracket.dart`** -> AI Confidence: **99.29%**
911. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeRightParen.dart`** -> AI Confidence: **99.29%**
912. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nonNullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
913. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeAnd.dart`** -> AI Confidence: **99.29%**
914. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeAs.dart`** -> AI Confidence: **99.29%**
915. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeColon.dart`** -> AI Confidence: **99.29%**
916. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeComma.dart`** -> AI Confidence: **99.29%**
917. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeExclamation.dart`** -> AI Confidence: **99.29%**
918. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeOr.dart`** -> AI Confidence: **99.29%**
919. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeQuestion.dart`** -> AI Confidence: **99.29%**
920. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeRightBrace.dart`** -> AI Confidence: **99.29%**
921. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeRightBracket.dart`** -> AI Confidence: **99.29%**
922. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeRightParen.dart`** -> AI Confidence: **99.29%**
923. **`pkg/front_end/parser_testcases/patterns/recordTypedVariablePattern_nullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
924. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeAnd.dart`** -> AI Confidence: **99.29%**
925. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeAs.dart`** -> AI Confidence: **99.29%**
926. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeColon.dart`** -> AI Confidence: **99.29%**
927. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeComma.dart`** -> AI Confidence: **99.29%**
928. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeExclamation.dart`** -> AI Confidence: **99.29%**
929. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeOr.dart`** -> AI Confidence: **99.29%**
930. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeQuestion.dart`** -> AI Confidence: **99.29%**
931. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeRightBrace.dart`** -> AI Confidence: **99.29%**
932. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeRightBracket.dart`** -> AI Confidence: **99.29%**
933. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeRightParen.dart`** -> AI Confidence: **99.29%**
934. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nonNullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
935. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeAnd.dart`** -> AI Confidence: **99.29%**
936. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeAs.dart`** -> AI Confidence: **99.29%**
937. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeColon.dart`** -> AI Confidence: **99.29%**
938. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeComma.dart`** -> AI Confidence: **99.29%**
939. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeExclamation.dart`** -> AI Confidence: **99.29%**
940. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeOr.dart`** -> AI Confidence: **99.29%**
941. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeQuestion.dart`** -> AI Confidence: **99.29%**
942. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeRightBrace.dart`** -> AI Confidence: **99.29%**
943. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeRightBracket.dart`** -> AI Confidence: **99.29%**
944. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeRightParen.dart`** -> AI Confidence: **99.29%**
945. **`pkg/front_end/parser_testcases/patterns/recordTypedWildcardPattern_nullable_beforeWhen.dart`** -> AI Confidence: **99.29%**
946. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_case.dart`** -> AI Confidence: **99.29%**
947. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_case_empty.dart`** -> AI Confidence: **99.29%**
948. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_case_singleton.dart`** -> AI Confidence: **99.29%**
949. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
950. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
951. **`pkg/front_end/parser_testcases/patterns/record_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
952. **`pkg/front_end/parser_testcases/patterns/relational_containingBitwiseOrExpression_equality.dart`** -> AI Confidence: **99.29%**
953. **`pkg/front_end/parser_testcases/patterns/relational_containingBitwiseOrExpression_relational.dart`** -> AI Confidence: **99.29%**
954. **`pkg/front_end/parser_testcases/patterns/relational_containingRelationalExpression_equality.dart`** -> AI Confidence: **99.29%**
955. **`pkg/front_end/parser_testcases/patterns/relational_containingRelationalExpression_relational.dart`** -> AI Confidence: **99.29%**
956. **`pkg/front_end/parser_testcases/patterns/relational_insideNullCheck_equal.dart`** -> AI Confidence: **99.29%**
957. **`pkg/front_end/parser_testcases/patterns/relational_insideNullCheck_greaterThan.dart`** -> AI Confidence: **99.29%**
958. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_equal.dart`** -> AI Confidence: **99.29%**
959. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_greater_than.dart`** -> AI Confidence: **99.29%**
960. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_greater_than_or_equal.dart`** -> AI Confidence: **99.29%**
961. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_less_than.dart`** -> AI Confidence: **99.29%**
962. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_less_than_or_equal.dart`** -> AI Confidence: **99.29%**
963. **`pkg/front_end/parser_testcases/patterns/relational_inside_case_not_equal.dart`** -> AI Confidence: **99.29%**
964. **`pkg/front_end/parser_testcases/patterns/relational_inside_extractor_pattern.dart`** -> AI Confidence: **99.29%**
965. **`pkg/front_end/parser_testcases/patterns/relational_inside_list_pattern.dart`** -> AI Confidence: **99.29%**
966. **`pkg/front_end/parser_testcases/patterns/relational_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
967. **`pkg/front_end/parser_testcases/patterns/relational_inside_logical_and_rhs.dart`** -> AI Confidence: **99.29%**
968. **`pkg/front_end/parser_testcases/patterns/relational_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
969. **`pkg/front_end/parser_testcases/patterns/relational_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
970. **`pkg/front_end/parser_testcases/patterns/relational_inside_map_pattern.dart`** -> AI Confidence: **99.29%**
971. **`pkg/front_end/parser_testcases/patterns/relational_inside_parenthesized_pattern.dart`** -> AI Confidence: **99.29%**
972. **`pkg/front_end/parser_testcases/patterns/relational_inside_record_pattern_named.dart`** -> AI Confidence: **99.29%**
973. **`pkg/front_end/parser_testcases/patterns/relational_inside_record_pattern_unnamed.dart`** -> AI Confidence: **99.29%**
974. **`pkg/front_end/parser_testcases/patterns/rest_subpatternStartingTokens.dart`** -> AI Confidence: **99.29%**
975. **`pkg/front_end/parser_testcases/patterns/rest_withoutSubpattern_insideList.dart`** -> AI Confidence: **99.29%**
976. **`pkg/front_end/parser_testcases/patterns/rest_withoutSubpattern_insideMap.dart`** -> AI Confidence: **99.29%**
977. **`pkg/front_end/parser_testcases/patterns/string_literal_inside_case.dart`** -> AI Confidence: **99.29%**
978. **`pkg/front_end/parser_testcases/patterns/string_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
979. **`pkg/front_end/parser_testcases/patterns/string_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
980. **`pkg/front_end/parser_testcases/patterns/string_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
981. **`pkg/front_end/parser_testcases/patterns/syntheticIdentifier_insideListPattern.dart`** -> AI Confidence: **99.29%**
982. **`pkg/front_end/parser_testcases/patterns/syntheticIdentifier_insideMapPattern.dart`** -> AI Confidence: **99.29%**
983. **`pkg/front_end/parser_testcases/patterns/syntheticIdentifier_insideParenthesizedPattern.dart`** -> AI Confidence: **99.29%**
984. **`pkg/front_end/parser_testcases/patterns/syntheticIdentifier_insideRecordPattern.dart`** -> AI Confidence: **99.29%**
985. **`pkg/front_end/parser_testcases/patterns/typeQuestionBeforeWhen_guard.dart`** -> AI Confidence: **99.29%**
986. **`pkg/front_end/parser_testcases/patterns/typed_final_variable_inside_case.dart`** -> AI Confidence: **99.29%**
987. **`pkg/front_end/parser_testcases/patterns/typed_final_variable_inside_cast.dart`** -> AI Confidence: **99.29%**
988. **`pkg/front_end/parser_testcases/patterns/typed_final_variable_inside_null_assert.dart`** -> AI Confidence: **99.29%**
989. **`pkg/front_end/parser_testcases/patterns/typed_final_variable_inside_null_check.dart`** -> AI Confidence: **99.29%**
990. **`pkg/front_end/parser_testcases/patterns/typed_variable_inside_case.dart`** -> AI Confidence: **99.29%**
991. **`pkg/front_end/parser_testcases/patterns/typed_variable_inside_cast.dart`** -> AI Confidence: **99.29%**
992. **`pkg/front_end/parser_testcases/patterns/typed_variable_inside_null_assert.dart`** -> AI Confidence: **99.29%**
993. **`pkg/front_end/parser_testcases/patterns/typed_variable_inside_null_check.dart`** -> AI Confidence: **99.29%**
994. **`pkg/front_end/parser_testcases/patterns/var_variable_inside_null_check.dart`** -> AI Confidence: **99.29%**
995. **`pkg/front_end/parser_testcases/patterns/variable_type_record_empty_inMatchingContext.dart`** -> AI Confidence: **99.29%**
996. **`pkg/front_end/parser_testcases/patterns/variable_type_record_nonEmpty_inMatchingContext.dart`** -> AI Confidence: **99.29%**
997. **`pkg/front_end/parser_testcases/patterns/wildcard_bare_beforeWhen.dart`** -> AI Confidence: **99.29%**
998. **`pkg/front_end/parser_testcases/patterns/wildcard_bare_insideCase.dart`** -> AI Confidence: **99.29%**
999. **`pkg/front_end/parser_testcases/patterns/wildcard_bare_insideCast.dart`** -> AI Confidence: **99.29%**
1000. **`pkg/front_end/parser_testcases/patterns/wildcard_bare_insideNullAssert.dart`** -> AI Confidence: **99.29%**
1001. **`pkg/front_end/parser_testcases/patterns/wildcard_bare_insideNullCheck.dart`** -> AI Confidence: **99.29%**
1002. **`pkg/front_end/parser_testcases/patterns/wildcard_final_typed_insideCase.dart`** -> AI Confidence: **99.29%**
1003. **`pkg/front_end/parser_testcases/patterns/wildcard_final_typed_insideCast.dart`** -> AI Confidence: **99.29%**
1004. **`pkg/front_end/parser_testcases/patterns/wildcard_final_typed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
1005. **`pkg/front_end/parser_testcases/patterns/wildcard_final_typed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
1006. **`pkg/front_end/parser_testcases/patterns/wildcard_final_untyped_insideCase.dart`** -> AI Confidence: **99.29%**
1007. **`pkg/front_end/parser_testcases/patterns/wildcard_final_untyped_insideCast.dart`** -> AI Confidence: **99.29%**
1008. **`pkg/front_end/parser_testcases/patterns/wildcard_final_untyped_insideNullAssert.dart`** -> AI Confidence: **99.29%**
1009. **`pkg/front_end/parser_testcases/patterns/wildcard_final_untyped_insideNullCheck.dart`** -> AI Confidence: **99.29%**
1010. **`pkg/front_end/parser_testcases/patterns/wildcard_typed_insideCase.dart`** -> AI Confidence: **99.29%**
1011. **`pkg/front_end/parser_testcases/patterns/wildcard_typed_insideCast.dart`** -> AI Confidence: **99.29%**
1012. **`pkg/front_end/parser_testcases/patterns/wildcard_typed_insideNullAssert.dart`** -> AI Confidence: **99.29%**
1013. **`pkg/front_end/parser_testcases/patterns/wildcard_typed_insideNullCheck.dart`** -> AI Confidence: **99.29%**
1014. **`pkg/front_end/parser_testcases/patterns/wildcard_var_insideNullCheck.dart`** -> AI Confidence: **99.29%**
1015. **`pkg/front_end/parser_testcases/record/is_and_as.dart`** -> AI Confidence: **99.29%**
1016. **`pkg/front_end/parser_testcases/record/is_record_conditional_expression.dart`** -> AI Confidence: **99.29%**
1017. **`pkg/front_end/parser_testcases/record/modifier_before_type_question.dart`** -> AI Confidence: **99.29%**
1018. **`pkg/front_end/parser_testcases/record/on.dart`** -> AI Confidence: **99.29%**
1019. **`pkg/front_end/parser_testcases/record/record_type_04.dart`** -> AI Confidence: **99.29%**
1020. **`pkg/front_end/parser_testcases/record/record_type_as_named_parameter.dart`** -> AI Confidence: **99.29%**
1021. **`pkg/front_end/parser_testcases/record/record_type_as_optional_parameter.dart`** -> AI Confidence: **99.29%**
1022. **`pkg/front_end/parser_testcases/record/record_type_in_for_loop.dart`** -> AI Confidence: **99.29%**
1023. **`pkg/front_end/testcases/closure_context_lowering/catch_variables.dart`** -> AI Confidence: **99.29%**
1024. **`pkg/front_end/testcases/closure_context_lowering/foo42.dart`** -> AI Confidence: **99.29%**
1025. **`pkg/front_end/testcases/dart2js/issue41657.dart`** -> AI Confidence: **99.29%**
1026. **`pkg/front_end/testcases/dart2js/issue49198.dart`** -> AI Confidence: **99.29%**
1027. **`pkg/front_end/testcases/dartdevc/issue49198.dart`** -> AI Confidence: **99.29%**
1028. **`pkg/front_end/testcases/dot_shorthands/bool_parse.dart`** -> AI Confidence: **99.29%**
1029. **`pkg/front_end/testcases/extension_types/nullability.dart`** -> AI Confidence: **99.29%**
1030. **`pkg/front_end/testcases/extension_types/representation_type.dart`** -> AI Confidence: **99.29%**
1031. **`pkg/front_end/testcases/extensions/explicit_context.dart`** -> AI Confidence: **99.29%**
1032. **`pkg/front_end/testcases/extensions/null_aware.dart`** -> AI Confidence: **99.29%**
1033. **`pkg/front_end/testcases/general/async_method_with_invalid_type.dart`** -> AI Confidence: **99.29%**
1034. **`pkg/front_end/testcases/general/bad_setter_abstract.dart`** -> AI Confidence: **99.29%**
1035. **`pkg/front_end/testcases/general/constants/issue52532.dart`** -> AI Confidence: **99.29%**
1036. **`pkg/front_end/testcases/general/constants/js_semantics/various.dart`** -> AI Confidence: **99.29%**
1037. **`pkg/front_end/testcases/general/constants/rudimentary_test_01.dart`** -> AI Confidence: **99.29%**
1038. **`pkg/front_end/testcases/general/continue_label_invalid.dart`** -> AI Confidence: **99.29%**
1039. **`pkg/front_end/testcases/general/continue_loop.dart`** -> AI Confidence: **99.29%**
1040. **`pkg/front_end/testcases/general/control_flow_collection.dart`** -> AI Confidence: **99.29%**
1041. **`pkg/front_end/testcases/general/empty_switch.dart`** -> AI Confidence: **99.29%**
1042. **`pkg/front_end/testcases/general/error_recovery/empty_for.dart`** -> AI Confidence: **99.29%**
1043. **`pkg/front_end/testcases/general/error_recovery/for_in_with_colon.dart`** -> AI Confidence: **99.29%**
1044. **`pkg/front_end/testcases/general/error_recovery/parse_error_in_try_on_clause.dart`** -> AI Confidence: **99.29%**
1045. **`pkg/front_end/testcases/general/error_recovery/weekly_bot_83_failure.dart`** -> AI Confidence: **99.29%**
1046. **`pkg/front_end/testcases/general/error_recovery/weekly_bot_83_failure_2.dart`** -> AI Confidence: **99.29%**
1047. **`pkg/front_end/testcases/general/expressions.dart`** -> AI Confidence: **99.29%**
1048. **`pkg/front_end/testcases/general/for_in_scope.dart`** -> AI Confidence: **99.29%**
1049. **`pkg/front_end/testcases/general/function_type_default_value.dart`** -> AI Confidence: **99.29%**
1050. **`pkg/front_end/testcases/general/functions.dart`** -> AI Confidence: **99.29%**
1051. **`pkg/front_end/testcases/general/if_case_disabled.dart`** -> AI Confidence: **99.29%**
1052. **`pkg/front_end/testcases/general/if_null_assign.dart`** -> AI Confidence: **99.29%**
1053. **`pkg/front_end/testcases/general/implicit_constant_in_switch.dart`** -> AI Confidence: **99.29%**
1054. **`pkg/front_end/testcases/general/issue44654.dart`** -> AI Confidence: **99.29%**
1055. **`pkg/front_end/testcases/general/issue47223a.dart`** -> AI Confidence: **99.29%**
1056. **`pkg/front_end/testcases/general/issue47223b.dart`** -> AI Confidence: **99.29%**
1057. **`pkg/front_end/testcases/general/issue48323.dart`** -> AI Confidence: **99.29%**
1058. **`pkg/front_end/testcases/general/issue48808.dart`** -> AI Confidence: **99.29%**
1059. **`pkg/front_end/testcases/general/issue54563.dart`** -> AI Confidence: **99.29%**
1060. **`pkg/front_end/testcases/general/issue_47541.dart`** -> AI Confidence: **99.29%**
1061. **`pkg/front_end/testcases/general/issue_48999.dart`** -> AI Confidence: **99.29%**
1062. **`pkg/front_end/testcases/general/issue_49132.dart`** -> AI Confidence: **99.29%**
1063. **`pkg/front_end/testcases/general/issue_49132_not_nullable.dart`** -> AI Confidence: **99.29%**
1064. **`pkg/front_end/testcases/general/labeled_default.dart`** -> AI Confidence: **99.29%**
1065. **`pkg/front_end/testcases/general/labeled_loop_break.dart`** -> AI Confidence: **99.29%**
1066. **`pkg/front_end/testcases/general/labeled_loop_continue.dart`** -> AI Confidence: **99.29%**
1067. **`pkg/front_end/testcases/general/null_aware.dart`** -> AI Confidence: **99.29%**
1068. **`pkg/front_end/testcases/general/null_aware_spread.dart`** -> AI Confidence: **99.29%**
1069. **`pkg/front_end/testcases/general/omitted_break.dart`** -> AI Confidence: **99.29%**
1070. **`pkg/front_end/testcases/general/promoted_null_aware_access.dart`** -> AI Confidence: **99.29%**
1071. **`pkg/front_end/testcases/general/spread_collection.dart`** -> AI Confidence: **99.29%**
1072. **`pkg/front_end/testcases/general/statements.dart`** -> AI Confidence: **99.29%**
1073. **`pkg/front_end/testcases/general/type_variable_nullability.dart`** -> AI Confidence: **99.29%**
1074. **`pkg/front_end/testcases/general/with_dependencies/mixin_from_dill/mixin_from_dill.dart`** -> AI Confidence: **99.29%**
1075. **`pkg/front_end/testcases/general/with_dependencies/mixin_from_dill/mixin_from_dill.no_link.dart`** -> AI Confidence: **99.29%**
1076. **`pkg/front_end/testcases/inference/bug30624.dart`** -> AI Confidence: **99.29%**
1077. **`pkg/front_end/testcases/inference/switch_continue.dart`** -> AI Confidence: **99.29%**
1078. **`pkg/front_end/testcases/inference_update_1/write_capture_deferral.dart`** -> AI Confidence: **99.29%**
1079. **`pkg/front_end/testcases/inference_update_2/cascaded_field_promotion.dart`** -> AI Confidence: **99.29%**
1080. **`pkg/front_end/testcases/inference_update_4/assignment_promotion_in_if_statement.dart`** -> AI Confidence: **99.29%**
1081. **`pkg/front_end/testcases/nnbd/assignability.dart`** -> AI Confidence: **99.29%**
1082. **`pkg/front_end/testcases/nnbd/forin.dart`** -> AI Confidence: **99.29%**
1083. **`pkg/front_end/testcases/nnbd/future_or_variables.dart`** -> AI Confidence: **99.29%**
1084. **`pkg/front_end/testcases/nnbd/instance_duplicates.dart`** -> AI Confidence: **99.29%**
1085. **`pkg/front_end/testcases/nnbd/issue41114.dart`** -> AI Confidence: **99.29%**
1086. **`pkg/front_end/testcases/nnbd/issue41520.dart`** -> AI Confidence: **99.29%**
1087. **`pkg/front_end/testcases/nnbd/issue41657.dart`** -> AI Confidence: **99.29%**
1088. **`pkg/front_end/testcases/nnbd/issue41700a.dart`** -> AI Confidence: **99.29%**
1089. **`pkg/front_end/testcases/nnbd/issue42089.dart`** -> AI Confidence: **99.29%**
1090. **`pkg/front_end/testcases/nnbd/issue42143.dart`** -> AI Confidence: **99.29%**
1091. **`pkg/front_end/testcases/nnbd/issue43278.dart`** -> AI Confidence: **99.29%**
1092. **`pkg/front_end/testcases/nnbd/issue43495.dart`** -> AI Confidence: **99.29%**
1093. **`pkg/front_end/testcases/nnbd/issue44362.dart`** -> AI Confidence: **99.29%**
1094. **`pkg/front_end/testcases/nnbd/issue49198.dart`** -> AI Confidence: **99.29%**
1095. **`pkg/front_end/testcases/nnbd/never_receiver.dart`** -> AI Confidence: **99.29%**
1096. **`pkg/front_end/testcases/nnbd/no_support_for_old_null_aware_index_access_syntax.dart`** -> AI Confidence: **99.29%**
1097. **`pkg/front_end/testcases/nnbd/null_aware_static_access.dart`** -> AI Confidence: **99.29%**
1098. **`pkg/front_end/testcases/nnbd/null_aware_this_access.dart`** -> AI Confidence: **99.29%**
1099. **`pkg/front_end/testcases/nnbd/null_shorting.dart`** -> AI Confidence: **99.29%**
1100. **`pkg/front_end/testcases/nnbd/null_shorting_explicit_extension.dart`** -> AI Confidence: **99.29%**
1101. **`pkg/front_end/testcases/nnbd/null_shorting_extension.dart`** -> AI Confidence: **99.29%**
1102. **`pkg/front_end/testcases/nnbd/nullable_receiver.dart`** -> AI Confidence: **99.29%**
1103. **`pkg/front_end/testcases/nnbd/nullable_setter.dart`** -> AI Confidence: **99.29%**
1104. **`pkg/front_end/testcases/nnbd/override_inference.dart`** -> AI Confidence: **99.29%**
1105. **`pkg/front_end/testcases/nnbd/potentially_non_nullable_field.dart`** -> AI Confidence: **99.29%**
1106. **`pkg/front_end/testcases/nnbd/strictly_non_nullable_warnings.dart`** -> AI Confidence: **99.29%**
1107. **`pkg/front_end/testcases/nnbd/switch_redesign_fall_over.dart`** -> AI Confidence: **99.29%**
1108. **`pkg/front_end/testcases/null_aware_elements/constant_collections.dart`** -> AI Confidence: **99.29%**
1109. **`pkg/front_end/testcases/null_aware_elements/constant_null_aware_map_entry_shorting.dart`** -> AI Confidence: **99.29%**
1110. **`pkg/front_end/testcases/null_aware_elements/constant_null_aware_map_entry_shorting_erroneous.dart`** -> AI Confidence: **99.29%**
1111. **`pkg/front_end/testcases/null_aware_elements/evaluation_order.dart`** -> AI Confidence: **99.29%**
1112. **`pkg/front_end/testcases/null_aware_elements/simple_positive.dart`** -> AI Confidence: **99.29%**
1113. **`pkg/front_end/testcases/null_aware_elements/type_inference_simple_positive.dart`** -> AI Confidence: **99.29%**
1114. **`pkg/front_end/testcases/offsets/ddc/spreads.dart`** -> AI Confidence: **99.29%**
1115. **`pkg/front_end/testcases/offsets/spreads.dart`** -> AI Confidence: **99.29%**
1116. **`pkg/front_end/testcases/patterns/boolean_literal_inside_case.dart`** -> AI Confidence: **99.29%**
1117. **`pkg/front_end/testcases/patterns/boolean_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
1118. **`pkg/front_end/testcases/patterns/boolean_literal_inside_if_case.dart`** -> AI Confidence: **99.29%**
1119. **`pkg/front_end/testcases/patterns/boolean_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1120. **`pkg/front_end/testcases/patterns/boolean_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
1121. **`pkg/front_end/testcases/patterns/caseHead_withClassicPattern_guarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
1122. **`pkg/front_end/testcases/patterns/caseHead_withClassicPattern_guarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
1123. **`pkg/front_end/testcases/patterns/caseHead_withNewPattern_guarded_insideIfStatement.dart`** -> AI Confidence: **99.29%**
1124. **`pkg/front_end/testcases/patterns/caseHead_withNewPattern_guarded_insideSwitchStatement.dart`** -> AI Confidence: **99.29%**
1125. **`pkg/front_end/testcases/patterns/cast_inside_case.dart`** -> AI Confidence: **99.29%**
1126. **`pkg/front_end/testcases/patterns/cast_inside_extractor_pattern.dart`** -> AI Confidence: **99.29%**
1127. **`pkg/front_end/testcases/patterns/cast_inside_list_pattern.dart`** -> AI Confidence: **99.29%**
1128. **`pkg/front_end/testcases/patterns/cast_inside_logical_and_lhs.dart`** -> AI Confidence: **99.29%**
1129. **`pkg/front_end/testcases/patterns/cast_inside_logical_and_rhs.dart`** -> AI Confidence: **99.29%**
1130. **`pkg/front_end/testcases/patterns/cast_inside_logical_or_lhs.dart`** -> AI Confidence: **99.29%**
1131. **`pkg/front_end/testcases/patterns/cast_inside_logical_or_rhs.dart`** -> AI Confidence: **99.29%**
1132. **`pkg/front_end/testcases/patterns/cast_inside_map_pattern.dart`** -> AI Confidence: **99.29%**
1133. **`pkg/front_end/testcases/patterns/cast_inside_parenthesized_pattern.dart`** -> AI Confidence: **99.29%**
1134. **`pkg/front_end/testcases/patterns/cast_inside_record_pattern_named.dart`** -> AI Confidence: **99.29%**
1135. **`pkg/front_end/testcases/patterns/cast_inside_record_pattern_unnamed.dart`** -> AI Confidence: **99.29%**
1136. **`pkg/front_end/testcases/patterns/coercion_in_if_case_element.dart`** -> AI Confidence: **99.29%**
1137. **`pkg/front_end/testcases/patterns/coersion_in_if_case.dart`** -> AI Confidence: **99.29%**
1138. **`pkg/front_end/testcases/patterns/const_patterns.dart`** -> AI Confidence: **99.29%**
1139. **`pkg/front_end/testcases/patterns/const_patterns_binary.dart`** -> AI Confidence: **99.29%**
1140. **`pkg/front_end/testcases/patterns/constant_identifier_inside_case.dart`** -> AI Confidence: **99.29%**
1141. **`pkg/front_end/testcases/patterns/constant_identifier_inside_cast.dart`** -> AI Confidence: **99.29%**
1142. **`pkg/front_end/testcases/patterns/constant_identifier_inside_if_case.dart`** -> AI Confidence: **99.29%**
1143. **`pkg/front_end/testcases/patterns/constant_identifier_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1144. **`pkg/front_end/testcases/patterns/constant_identifier_inside_null_check.dart`** -> AI Confidence: **99.29%**
1145. **`pkg/front_end/testcases/patterns/constant_pattern_in_if.dart`** -> AI Confidence: **99.29%**
1146. **`pkg/front_end/testcases/patterns/constant_pattern_in_switch.dart`** -> AI Confidence: **99.29%**
1147. **`pkg/front_end/testcases/patterns/double_literal_inside_case.dart`** -> AI Confidence: **99.29%**
1148. **`pkg/front_end/testcases/patterns/double_literal_inside_cast.dart`** -> AI Confidence: **99.29%**
1149. **`pkg/front_end/testcases/patterns/double_literal_inside_if_case.dart`** -> AI Confidence: **99.29%**
1150. **`pkg/front_end/testcases/patterns/double_literal_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1151. **`pkg/front_end/testcases/patterns/double_literal_inside_null_check.dart`** -> AI Confidence: **99.29%**
1152. **`pkg/front_end/testcases/patterns/error_cases.dart`** -> AI Confidence: **99.29%**
1153. **`pkg/front_end/testcases/patterns/error_recovery_after_question_suffix_in_expression.dart`** -> AI Confidence: **99.29%**
1154. **`pkg/front_end/testcases/patterns/exhaustiveness/bool_switch.dart`** -> AI Confidence: **99.29%**
1155. **`pkg/front_end/testcases/patterns/extractor_pattern_inside_cast.dart`** -> AI Confidence: **99.29%**
1156. **`pkg/front_end/testcases/patterns/extractor_pattern_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1157. **`pkg/front_end/testcases/patterns/extractor_pattern_inside_null_check.dart`** -> AI Confidence: **99.29%**
1158. **`pkg/front_end/testcases/patterns/extractor_pattern_with_type_args_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1159. **`pkg/front_end/testcases/patterns/final_variable_inside_case.dart`** -> AI Confidence: **99.29%**
1160. **`pkg/front_end/testcases/patterns/final_variable_inside_cast.dart`** -> AI Confidence: **99.29%**
1161. **`pkg/front_end/testcases/patterns/final_variable_inside_if_case.dart`** -> AI Confidence: **99.29%**
1162. **`pkg/front_end/testcases/patterns/final_variable_inside_null_assert.dart`** -> AI Confidence: **99.29%**
1163. **`pkg/front_end/testcases/patterns/final_variable_inside_null_check.dart`** -> AI Confidence: **99.29%**
1164. **`pkg/front_end/testcases/patterns/integer_literal_inside_case.dart`** -> AI Confidence: **99.29%**
1165. **`pkg/front_end/testcases/patterns/integer_literal_inside_cast.dart`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `runtime/vm/object.cc` -> **100.0%** Exposure
- `runtime/vm/object.h` -> **99.9572%** Exposure
- `runtime/vm/compiler/backend/il_riscv.cc` -> **99.7104%** Exposure
- `runtime/vm/runtime_entry.cc` -> **47.5245%** Exposure
- `runtime/vm/compiler/backend/il_ia32.cc` -> **2.0647%** Exposure
### Exploit Generation Surface
- `tools/bots/try_benchmarks.sh` -> **100.0%** Exposure
- `PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/_fe_analyzer_shared/PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/analysis_server/PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/analyzer/PRESUBMIT.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `pkg/vm/testcases/transformations/type_flow/transformer/protobuf_handler/compile_protos.sh` -> **100.0%** Exposure
- `tests/co19/update.sh` -> **100.0%** Exposure
- `tools/bots/try_benchmarks.sh` -> **100.0%** Exposure
- `PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/analysis_server/PRESUBMIT.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `runtime/bin/socket_base_win.cc` -> **10.0%** Exposure
- `runtime/vm/compiler/aot/aot_call_specializer.cc` -> **10.0%** Exposure
- `runtime/vm/compiler/backend/branch_optimizer.cc` -> **10.0%** Exposure
- `runtime/vm/compiler/backend/constant_propagator.cc` -> **10.0%** Exposure
- `runtime/vm/compiler/backend/flow_graph.cc` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `runtime/bin/secure_socket_utils_test.cc` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `pkg/dart2wasm/tool/compile_benchmark` -> **100.0%** Exposure
- `tools/patches/utils.sh` -> **100.0%** Exposure
- `PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/_fe_analyzer_shared/PRESUBMIT.py` -> **100.0%** Exposure
- `pkg/analysis_server/PRESUBMIT.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `39187` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tools/diff_results.dart` (DART) -> Cumulative Risk: **922.19**
- **Archetype:** `file_cluster_4` (Distance: 12.884 IQR)
- **Magnitude:** 0.33 | **LOC:** 413 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getResults` (Impact: 43.5), `GroupedDiff` (Impact: 30.7), `continue` (Impact: 24.6)

### 2. `runtime/vm/runtime_entry.cc` (CPP) -> Cumulative Risk: **920.6**
- **Archetype:** `file_cluster_8` (Distance: 14.751 IQR)
- **Magnitude:** 4977.74 | **LOC:** 5535 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (99.9876%)
- **Heaviest Functions:** `PatchableCallHandler::ResolveTargetFunct` (Impact: 1149.5), `TrySwitchInstanceCall` (Impact: 133.7), `PatchableCallHandler::DoICDataMissJIT` (Impact: 128.0)

### 3. `pkg/compiler/lib/src/dart2js.dart` (DART) -> Cumulative Risk: **910.18**
- **Archetype:** `file_cluster_11` (Distance: 13.953 IQR)
- **Magnitude:** 502.32 | **LOC:** 1465 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `parseCommandLine` (Impact: 22.3), `setOutput` (Impact: 16.4), `setCategories` (Impact: 13.9)

### 4. `pkg/test_runner/lib/src/test_configurations.dart` (DART) -> Cumulative Risk: **906.28**
- **Archetype:** `file_cluster_13` (Distance: 12.594 IQR)
- **Magnitude:** 134.54 | **LOC:** 280 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.7877%)
- **Heaviest Functions:** `testSuites.add` (Impact: 30.4), `testSuites.add` (Impact: 16.3), `configurations.any` (Impact: 13.7)

### 5. `pkg/test_runner/lib/src/command.dart` (DART) -> Cumulative Risk: **903.45**
- **Archetype:** `file_cluster_0` (Distance: 11.099 IQR)
- **Magnitude:** 610.66 | **LOC:** 985 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `nonBatchArguments` (Impact: 131.4), `VMCommandOutput` (Impact: 96.5), `extraLibraries` (Impact: 57.4)

### 6. `benchmarks/Startup/dart/Startup.dart` (DART) -> Cumulative Risk: **902.94**
- **Archetype:** `file_cluster_4` (Distance: 13.546 IQR)
- **Magnitude:** 167.36 | **LOC:** 88 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `gen_kernel` (Impact: 107.9)

### 7. `pkg/test_runner/lib/src/test_case.dart` (DART) -> Cumulative Risk: **890.44**
- **Archetype:** `file_cluster_4` (Distance: 12.903 IQR)
- **Magnitude:** 487.92 | **LOC:** 400 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `else` (Impact: 231.8), `import` (Impact: 115.2), `_createCommandOutput` (Impact: 22.0)

### 8. `pkg/observatory/lib/src/debugger/debugger_location.dart` (DART) -> Cumulative Risk: **887.02**
- **Archetype:** `file_cluster_4` (Distance: 12.646 IQR)
- **Magnitude:** 519.6 | **LOC:** 493 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `debugger` (Impact: 150.8), `assert` (Impact: 15.7), `assert` (Impact: 12.6)

### 9. `runtime/vm/object.cc` (CPP) -> Cumulative Risk: **880.51**
- **Archetype:** `file_cluster_13` (Distance: 14.915 IQR)
- **Magnitude:** 1781.8 | **LOC:** 28795 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Obscured Payload (100.0%)
- **Heaviest Functions:** `FindEntryPointPragma` (Impact: 127.3), `RecordShape::Register` (Impact: 95.4), `Function::MaxNumberOfParametersInRegiste` (Impact: 58.5)

### 10. `pkg/test_runner/lib/src/fuchsia.dart` (DART) -> Cumulative Risk: **879.89**
- **Archetype:** `file_cluster_4` (Distance: 13.272 IQR)
- **Magnitude:** 128.16 | **LOC:** 116 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `import` (Impact: 55.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `runtime/vm/compiler/backend/il.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.94 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.308 IQR)
- **Top Global Matches:** file_cluster_8: 14.94, file_cluster_13: 15.134, file_cluster_11: 15.139
- **Magnitude:** 11513.46 | **LOC:** 9109 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 340
- **Risk Profile:** Cognitive Load (94.9149%), Tech Debt (94.2218%)
**Top Internal Functions/Classes:**
  * `BlockEntryInstr::FindOsrEntryRecursive` (Impact: 3440.3 | O(N^6) | DB: 338)
  * `StrengthenAlignment` (Impact: 2259.5 | O(N^6) | DB: 340)
  * `HierarchyInfo::BuildRangesFor` (Impact: 158.3 | O(N^6) | DB: 19)
  * `InstanceCallInstr::EmitNativeCode` (Impact: 125.1 | O(N^6) | DB: 32)
  * `StaticCallInstr::Evaluate` (Impact: 107.0 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1191`, `structural_boundaries: 625`, `args: 550`, `func_start: 271`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3175`, `dead_code: 3`, `planned_debt: 52`, `duplicate_logic: 2`, `orphaned_logic: 127`
* *Architecture:* `api: 2`, `import: 42`
* *Defense:* `safety: 2`, `test: 6`, `immutability_locks: 419`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart_entry.h, runtime_api.h, cpu.h, native_calling_convention.h, runtime_entry.h, scopes.h, object.h, bootstrap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/backend/il_x64.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.893 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.988 IQR)
- **Top Global Matches:** file_cluster_8: 13.893, file_cluster_13: 14.197, file_cluster_11: 14.23
- **Magnitude:** 8235.42 | **LOC:** 6665 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 295
- **Risk Profile:** Cognitive Load (94.0783%), Tech Debt (54.6749%)
**Top Internal Functions/Classes:**
  * `EmitNativeCode` (Impact: 3551.9 | O(2^N) | DB: 209)
  * `MemoryCopyInstr::EmitComputeStartPointer` (Impact: 2438.3 | O(N^6) | DB: 295)
  * `MemoryCopyInstr::EmitLoopCopy` (Impact: 179.2 | O(N^6) | DB: 4)
  * `Instruction::MakeCallSummary` (Impact: 99.7 | O(N^6) | DB: 2)
    * *Intent:* // Generic summary for call instructions that have all arguments pushed // on the stack and return t...
  * `BitCastInstr::MakeLocationSummary` (Impact: 86.3 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 654`, `structural_boundaries: 187`, `args: 514`, `func_start: 148`, `class_start: 3`
* *Risk/State:* `state_mutation: 1333`, `dead_code: 5`, `planned_debt: 28`, `duplicate_logic: 2`, `orphaned_logic: 34`
* *Architecture:* `api: 3`, `import: 23`
* *Defense:* `safety: 3`, `test: 4`, `immutability_locks: 264`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart_entry.h, runtime_api.h, parser.h, native_calling_convention.h, globals.h, symbols.h, compiler.h, type_testing_stubs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/service.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.55 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.262 IQR)
- **Top Global Matches:** file_cluster_8: 14.55, file_cluster_13: 14.681, file_cluster_11: 14.794
- **Magnitude:** 7259.68 | **LOC:** 6358 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 489
- **Risk Profile:** Cognitive Load (91.4975%), Tech Debt (63.9369%)
**Top Internal Functions/Classes:**
  * `Service::PostEvent` (Impact: 2757.3 | O(N^6) | DB: 489)
  * `Resume` (Impact: 130.3 | O(N^3) | DB: 46)
  * `ElementCount` (Impact: 118.2 | O(N^4) | DB: 24)
    * *Intent:* // Returns number of elements in the list. -1 on parse error.
  * `GetVMTimelineCommon` (Impact: 114.7 | O(N^6) | DB: 6)
  * `Service::InvokeMethod` (Impact: 96.1 | O(N^6) | DB: 43)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 618`, `structural_boundaries: 496`, `args: 326`, `func_start: 200`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 2594`, `dead_code: 2`, `planned_debt: 13`, `duplicate_logic: 28`
* *Architecture:* `io: 1`, `api: 51`, `import: 52`
* *Defense:* `safety: 3`, `immutability_locks: 415`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dart_entry.h, cpu.h, parser.h, dart_api.h, dart_native_api.h, message_handler.h, object.h, message.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/backend/il_arm.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.92 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.906 IQR)
- **Top Global Matches:** file_cluster_8: 13.92, file_cluster_11: 14.224, file_cluster_13: 14.245
- **Magnitude:** 7062.62 | **LOC:** 7254 | **CtrlFlow:** 80.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (72.5795%), Tech Debt (99.8012%)
**Top Internal Functions/Classes:**
  * `EmitShiftInt64ByConstant` (Impact: 241.0 | O(N^6) | DB: 2)
  * `MemoryCopyInstr::EmitLoopCopy` (Impact: 226.6 | O(N^6) | DB: 11)
  * `LoadCodeUnitsInstr::EmitNativeCode` (Impact: 198.6 | O(N^6) | DB: 11)
  * `DEFINE_EMIT` (Impact: 177.7 | O(N^3))
    * *Intent:* // Need register < Q7 for float operations. // TODO(30953): Support register range constraints in th...
  * `MemoryCopyInstr::EmitComputeStartPointer` (Impact: 160.0 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 217`, `args: 519`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `state_mutation: 1595`, `dead_code: 16`, `planned_debt: 35`, `duplicate_logic: 32`, `orphaned_logic: 127`
* *Architecture:* `api: 2`, `import: 21`
* *Defense:* `safety: 3`, `test: 4`, `immutability_locks: 320`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart_entry.h, cpu.h, parser.h, native_calling_convention.h, simulator.h, globals.h, symbols.h, compiler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/simulator_riscv.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.694 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.087 IQR)
- **Top Global Matches:** file_cluster_8: 13.694, file_cluster_7: 14.115, file_cluster_13: 14.126
- **Magnitude:** 6931.56 | **LOC:** 3839 | **CtrlFlow:** 81.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (96.7543%), Tech Debt (94.8933%)
**Top Internal Functions/Classes:**
  * `Simulator::InterpretOPFP` (Impact: 1311.5 | O(N^6) | DB: 53)
    * *Intent:* #endif // XLEN >= 64
  * `Simulator::Interpret` (Impact: 869.0 | O(N^5) | DB: 53)
  * `Simulator::InterpretOPIMM` (Impact: 325.2 | O(N^6) | DB: 8)
  * `Simulator::InterpretSYSTEM` (Impact: 270.0 | O(N^4) | DB: 25)
  * `Simulator::InterpretOP_0` (Impact: 129.5 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1398`, `structural_boundaries: 318`, `args: 206`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1665`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 14`, `orphaned_logic: 87`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 2`, `sync_locks: 3`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants.h, stdlib.h, native_arguments.h, setjmp.h, simulator.h, globals.h, bit, stack_frame.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/vm_service/lib/src/vm_service.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.03 IQR)
- **Top Global Matches:** file_cluster_0: 15.03, file_cluster_16: 15.327, file_cluster_15: 15.329
- **Magnitude:** 6497.3 | **LOC:** 8714 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (28.7743%), Tech Debt (98.809%)
**Top Internal Functions/Classes:**
  * `toString` (Impact: 1608.1 | O(2^N))
  * `toJson` (Impact: 619.4 | O(2^N))
  * `createServiceObject` (Impact: 503.0 | O(2^N) | DB: 4)
  * `toString` (Impact: 477.7 | O(2^N))
  * `toString` (Impact: 409.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1377`, `structural_boundaries: 335`, `args: 263`, `func_start: 710`, `class_start: 52`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 4`, `dead_code: 10`, `planned_debt: 1`, `duplicate_logic: 45`
* *Architecture:* `api: 49`, `concurrency: 79`, `import: 4`
* *Defense:* `safety: 940`, `doc: 1279`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.189
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart:typed_data, dart:async, snapshot_graph.dart, dart:convert
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `runtime/vm/compiler/frontend/kernel_binary_flowgraph.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.236 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.031 IQR)
- **Top Global Matches:** file_cluster_8: 15.236, file_cluster_13: 15.487, file_cluster_11: 15.498
- **Magnitude:** 6463.44 | **LOC:** 6317 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 602
- **Risk Profile:** Cognitive Load (90.1227%), Tech Debt (41.6651%)
**Top Internal Functions/Classes:**
  * `StreamingFlowGraphBuilder::BuildAssertSt` (Impact: 1206.8 | O(N^6) | DB: 480)
  * `StreamingFlowGraphBuilder::BuildGraphOfF` (Impact: 921.9 | O(N^6) | DB: 602)
  * `StreamingFlowGraphBuilder::BuildStaticIn` (Impact: 174.9 | O(N^6) | DB: 32)
  * `StreamingFlowGraphBuilder::BuildRecordLi` (Impact: 76.7 | O(N^6) | DB: 44)
  * `StreamingFlowGraphBuilder::BuildIsTest` (Impact: 56.9 | O(N^6) | DB: 12)
    * *Intent:* // We only need to make sure that if the finalizer ended normally, we
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 165`, `args: 287`, `func_start: 100`
* *Risk/State:* `state_mutation: 3625`, `dead_code: 10`, `planned_debt: 7`, `duplicate_logic: 2`, `orphaned_logic: 33`
* *Architecture:* `import: 12`
* *Defense:* `immutability_locks: 274`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` callback.h, recognized_method.h, closure_functions_cache.h, compiler.h, kernel_binary.h, object_store.h, prologue_builder.h, stack_frame.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/frontend/kernel_to_il.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.876 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.586 IQR)
- **Top Global Matches:** file_cluster_8: 14.876, file_cluster_13: 15.009, file_cluster_11: 15.106
- **Magnitude:** 6344.34 | **LOC:** 6179 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 618
- **Risk Profile:** Cognitive Load (93.9939%), Tech Debt (61.7912%)
**Top Internal Functions/Classes:**
  * `FlowGraphBuilder::BuildGraphOfRecognized` (Impact: 2046.8 | O(N^6) | DB: 618)
  * `FlowGraphBuilder::IsRecognizedMethodForF` (Impact: 417.0 | O(N^1) | DB: 2)
  * `FlowGraphBuilder::FfiNativeLookupAddress` (Impact: 211.2 | O(N^6) | DB: 74)
  * `FlowGraphBuilder::TranslateInstantiatedT` (Impact: 166.0 | O(N^6) | DB: 70)
  * `FlowGraphBuilder::ThrowNoSuchMethodError` (Impact: 119.3 | O(N^6) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 642`, `structural_boundaries: 140`, `args: 361`, `func_start: 59`
* *Risk/State:* `state_mutation: 2492`, `dead_code: 8`, `planned_debt: 6`, `duplicate_logic: 8`, `orphaned_logic: 29`
* *Architecture:* `import: 35`
* *Defense:* `safety: 3`, `test: 24`, `immutability_locks: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` runtime_api.h, native_calling_convention.h, runtime_entry.h, scopes.h, longjump.h, native_entry.h, utility, symbols.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/frontend/kernel_translation_helper.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.331 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.618 IQR)
- **Top Global Matches:** file_cluster_8: 14.331, file_cluster_13: 14.7, file_cluster_7: 14.753
- **Magnitude:** 5642.66 | **LOC:** 4060 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 135
- **Risk Profile:** Cognitive Load (93.1024%), Tech Debt (99.7519%)
**Top Internal Functions/Classes:**
  * `TypeTranslator::BuildInterfaceType` (Impact: 592.5 | O(N^6) | DB: 135)
  * `KernelReaderHelper::SkipExpression` (Impact: 244.1 | O(N^2) | DB: 6)
  * `ClassHelper::ReadUntilExcluding` (Impact: 161.7 | O(N^3) | DB: 41)
  * `TypeTranslator::BuildTypeInternal` (Impact: 158.4 | O(N^5) | DB: 6)
  * `ProcedureHelper::ReadUntilExcluding` (Impact: 125.1 | O(N^3) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 735`, `structural_boundaries: 416`, `args: 252`, `func_start: 156`
* *Risk/State:* `state_mutation: 2487`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 19`, `orphaned_logic: 125`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 171`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` kernel_translation_helper.h, closure_functions_cache.h, parser.h, symbols.h, object_store.h, class_finalizer.h, precompiler.h, flags.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/call_specializer.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.707 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.509 IQR)
- **Top Global Matches:** file_cluster_8: 13.707, file_cluster_13: 13.968, file_cluster_11: 14.016
- **Magnitude:** 5526.48 | **LOC:** 3542 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (95.6631%), Tech Debt (77.1987%)
**Top Internal Functions/Classes:**
  * `InlineTypedDataIndexCheck` (Impact: 3566.9 | O(2^N) | DB: 49)
  * `CallSpecializer::TryReplaceWithBinaryOp` (Impact: 355.4 | O(N^6) | DB: 40)
  * `CallSpecializer::InstanceOfAsBool` (Impact: 122.2 | O(N^6) | DB: 26)
  * `CallSpecializer::TryReplaceWithEqualityO` (Impact: 113.6 | O(N^6) | DB: 21)
  * `CallSpecializer::VisitStaticCall` (Impact: 99.1 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 124`, `args: 182`, `func_start: 33`
* *Risk/State:* `state_mutation: 710`, `dead_code: 2`, `planned_debt: 6`, `orphaned_logic: 24`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cpu.h, compiler_timings.h, cha.h, compiler_state.h, flow_graph_compiler.h, inliner.h, call_specializer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/analysis_server/lib/src/services/completion/dart/in_scope_completion_pass.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.718 IQR)
- **Top Global Matches:** file_cluster_8: 12.718, file_cluster_0: 12.824, file_cluster_15: 12.828
- **Magnitude:** 5413.72 | **LOC:** 5015 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (17.5695%), Tech Debt (78.2862%)
**Top Internal Functions/Classes:**
  * `visitDeclaredVariablePattern` (Impact: 2987.8 | O(N^6) | DB: 2)
  * `identifierHelper` (Impact: 1809.8 | O(2^N) | DB: 6)
  * `visitClassDeclaration` (Impact: 96.2 | O(N^5))
  * `visitPropertyAccess` (Impact: 48.9 | O(N^2))
  * `visitConstructorFieldInitializer` (Impact: 36.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 923`, `structural_boundaries: 498`, `args: 172`, `func_start: 663`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `dead_code: 2`, `planned_debt: 33`, `duplicate_logic: 11`, `orphaned_logic: 26`
* *Architecture:* `api: 14`, `import: 30`
* *Defense:* `safety: 294`, `doc: 121`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` candidate_suggestion.dart, declaration_helper.dart, visibility_tracker.dart, suggestion_collector.dart, completion_request.dart, keyword_helper.dart, override_helper.dart, nullability_suffix.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/vm/compiler/backend/redundancy_elimination.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.464 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.355 IQR)
- **Top Global Matches:** file_cluster_8: 14.464, file_cluster_13: 14.72, file_cluster_11: 14.785
- **Magnitude:** 5013.06 | **LOC:** 4728 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 259
- **Risk Profile:** Cognitive Load (95.0713%), Tech Debt (74.8544%)
**Top Internal Functions/Classes:**
  * `ComputeInitialSets` (Impact: 1648.5 | O(N^6) | DB: 259)
  * `SetIndex` (Impact: 362.7 | O(N^6) | DB: 48)
    * *Intent:* // Construct a place from an allocation where the place represents a store to // a slot that corresp...
  * `AnyUseCreatesAlias` (Impact: 254.9 | O(2^N) | DB: 23)
  * `ReplacePhiWith` (Impact: 94.4 | O(N^6) | DB: 15)
  * `NumberPlaces` (Impact: 86.6 | O(N^6) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 262`, `args: 220`, `func_start: 118`, `class_start: 6`
* *Risk/State:* `state_mutation: 1633`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 10`, `orphaned_logic: 16`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `immutability_locks: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` il_printer.h, hash_map.h, object_store.h, loops.h, class_id.h, redundancy_elimination.h, il.h, flow_graph.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/bad_server_chain.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/bad_server_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client1_key_malformed.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client2.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client2_key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client_authority.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client_authority.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/client_authority_malformed.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/standalone/io/certificates/server_chain.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `benchmarks/Utf8Encode/dart/Utf8Encode.dart` (DART) | Magnitude: 32.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, func_start: 17, structural_boundaries: 13, closures: 12
- `pkg/analysis_server/lib/src/lsp/handlers/handler_signature_help.dart` (DART) | Magnitude: 86.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 40, func_start: 24, branch: 16
- `pkg/analysis_server/lib/src/services/refactoring/legacy/refactoring_internal.dart` (DART) | Magnitude: 20.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 43, func_start: 34, closures: 24
- `pkg/analysis_server/lib/src/services/snippets/dart/flutter_stateless_widget.dart` (DART) | Magnitude: 39.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 21, func_start: 19, concurrency: 11
- `pkg/analysis_server/lib/src/utilities/index_range.dart` (DART) | Magnitude: 24.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 25, func_start: 11, structural_boundaries: 10, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pkg/analyzer/lib/src/binary/string_table.dart` (DART) | Magnitude: 180.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, bitwise_ops: 55, state_mutation: 54, func_start: 45
- `pkg/front_end/testcases/general/invalid_operator2.dart` (DART) | Magnitude: 2.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 2, closures: 2
- `pkg/front_end/testcases/nnbd/field_setter_conflict.dart` (DART) | Magnitude: 7.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: func_start: 3, branch: 2, args: 2, safety: 2
- `pkg/analysis_server/lib/src/services/correction/dart/add_missing_enum_case_clauses.dart` (DART) | Magnitude: 163.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 37, branch: 33, func_start: 32
- `pkg/front_end/testcases/general/mixin_application_lub.dart` (DART) | Magnitude: 7.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 6, class_start: 5, api: 5, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `runtime/vm/regexp/base.h` (CPP) | Magnitude: 102.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: macros: 58, reflection_metaprogramming: 57, state_mutation: 51, indent_spaces: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pkg/analysis_server/lib/src/session_logger/log_entry.dart` (DART) | Magnitude: 11.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 36, indent_spaces: 34, structural_boundaries: 33, closures: 29
- `pkg/analyzer/lib/src/manifest/manifest_validator.dart` (DART) | Magnitude: 309.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 269, encapsulation: 119, branch: 87, func_start: 83
- `pkg/analysis_server/lib/src/status/pages/timing_page.dart` (DART) | Magnitude: 111.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 120, func_start: 42, branch: 31, structural_boundaries: 27
- `pkg/analysis_server/test/src/services/correction/assist/surround_with_for_in_test.dart` (DART) | Magnitude: 13.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, func_start: 14, structural_boundaries: 9, closures: 7
- `pkg/analyzer/lib/src/generated/element_resolver.dart` (DART) | Magnitude: 261.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 295, branch: 77, func_start: 74, doc: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/analysis_server/lib/src/services/correction/status.dart` (DART) | Magnitude: 44.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 66, func_start: 30, doc: 24, structural_boundaries: 21
- `pkg/status_file/lib/src/disjunctive.dart` (DART) | Magnitude: 295.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 289, structural_boundaries: 102, doc: 94, func_start: 89
- `pkg/compiler/lib/src/io/source_map_builder.dart` (DART) | Magnitude: 433.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 310, func_start: 102, branch: 54, closures: 48
- `pkg/front_end/testcases/general/invalid_operator.dart` (DART) | Magnitude: 27.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 139, args: 133, func_start: 133, closures: 133
- `pkg/compiler/lib/src/serialization/member_data.dart` (DART) | Magnitude: 157.56 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 206, encapsulation: 63, structural_boundaries: 55, func_start: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pkg/front_end/testcases/general/redirecting_constructors_declaration_order_3.dart` (DART) | Magnitude: 9.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, func_start: 7, generics: 5, immutability_locks: 5
- `pkg/vm/testcases/transformations/type_flow/transformer/regress_41452.dart` (DART) | Magnitude: 11.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: encapsulation: 17, indent_spaces: 11, func_start: 8, generics: 8
- `pkg/front_end/testcases/constructor_tearoffs/lowering/typedef_tear_off.dart` (DART) | Magnitude: 28.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, func_start: 92, structural_boundaries: 53, test: 46
- `pkg/front_end/testcases/general/top_level_promotion.dart` (DART) | Magnitude: 24.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 14, generics: 13, indent_spaces: 13, safety: 9
- `pkg/front_end/testcases/inference/constructors_infer_from_arguments_factory_calls_constructor.dart` (DART) | Magnitude: 2.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: func_start: 5, structural_boundaries: 4, indent_spaces: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkg/analysis_server/lib/src/services/correction/dart/convert_to_named_arguments.dart` (DART) | Magnitude: 164.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 33, branch: 31, closures: 25
- `pkg/front_end/lib/src/source/check_helper.dart` (DART) | Magnitude: 1041.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 552, safety: 117, branch: 102, func_start: 77
- `pkg/front_end/testcases/extensions/extension_setter.dart` (DART) | Magnitude: 63.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, func_start: 127, test: 97, branch: 57
- `pkg/front_end/testcases/general/mixin_covariant.dart` (DART) | Magnitude: 273.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: safety: 133, branch: 114, indent_spaces: 56, func_start: 50
- `pkg/front_end/testcases/enhanced_enums/simple_mixins.dart` (DART) | Magnitude: 20.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, func_start: 17, structural_boundaries: 8, closures: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tools/dom/src/_chrome/_chrome.dart` (DART) | Magnitude: 0.02 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, func_start: 14, encapsulation: 9, structural_boundaries: 7
- `pkg/analysis_server/test/src/cider/completion_test.dart` (DART) | Magnitude: 272.08 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 507, func_start: 318, encapsulation: 212, structural_boundaries: 161
- `pkg/_fe_analyzer_shared/lib/src/util/text_conversion.dart` (DART) | Magnitude: 16.76 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 28, branch: 10, doc: 10, state_mutation: 9
- `pkg/analysis_server/test/src/services/correction/assist/flutter_wrap_column_test.dart` (DART) | Magnitude: 47.18 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, func_start: 58, structural_boundaries: 44, ui_framework: 36
- `pkg/analysis_server/test/src/services/correction/assist/sort_child_property_last_test.dart` (DART) | Magnitude: 49.58 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, func_start: 79, ui_framework: 36, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pkg/analysis_server/test/src/services/correction/fix/remove_unused_import_test.dart` (DART) | Magnitude: 116.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 97, func_start: 92, indent_spaces: 86, concurrency: 81
- `pkg/analyzer_utilities/test/api_summary/src/api_description_test.dart` (DART) | Magnitude: 288.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 446, func_start: 271, structural_boundaries: 241, concurrency: 121
- `pkg/analysis_server/test/src/services/correction/fix/replace_boolean_with_bool_test.dart` (DART) | Magnitude: 19.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: func_start: 24, indent_spaces: 24, structural_boundaries: 13, closures: 10
- `pkg/analyzer/test/src/diagnostics/set_element_from_deferred_library_test.dart` (DART) | Magnitude: 19.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 17, func_start: 15, immutability_locks: 10
- `pkg/analysis_server/test/src/services/correction/fix/remove_operator_test.dart` (DART) | Magnitude: 19.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 18, func_start: 13, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `pkg/analysis_server/lib/src/server/stdio_server.dart` (DART) | Magnitude: 5.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, doc: 10, structural_boundaries: 5, func_start: 5
- `pkg/front_end/test/utils/values.dart` (DART) | Magnitude: 12.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 4, indent_spaces: 3, sec_high_risk_execution: 2, structural_boundaries: 1
- `pkg/analysis_server/lib/src/provisional/completion/completion_core.dart` (DART) | Magnitude: 13.04 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 17, structural_boundaries: 2, class_start: 2, api: 2
- `pkg/analysis_server/lib/src/services/execution/execution_context.dart` (DART) | Magnitude: 13.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 3, indent_spaces: 3, structural_boundaries: 1, func_start: 1
- `pkg/_fe_analyzer_shared/lib/src/base/customized_codes.dart` (DART) | Magnitude: 11.04 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 2, generics: 2, immutability_locks: 2, dead_code: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pkg/analyzer/lib/src/fine/annotations.dart` (DART) | Magnitude: 5.9 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 50, encapsulation: 28, immutability_locks: 21, structural_boundaries: 9
- `samples/ffi/sqlite/lib/src/bindings/constants.dart` (DART) | Magnitude: 19.24 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 65, globals: 56, immutability_locks: 56, indent_spaces: 56
- `pkg/dtd/lib/src/constants.dart` (DART) | Magnitude: 23.18 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 65, immutability_locks: 49, globals: 48, indent_spaces: 48
- `pkg/front_end/lib/src/base/modifiers.dart` (DART) | Magnitude: 47.74 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 196, encapsulation: 73, indent_spaces: 53, bitwise_ops: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pkg/analysis_server/test/src/services/correction/assist/flutter_wrap_value_listenable_builder_test.dart` (DART) | Magnitude: 51.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, func_start: 56, structural_boundaries: 48, closures: 31
- `pkg/analyzer_plugin/lib/src/utilities/change_builder/change_builder_dart.dart` (DART) | Magnitude: 1392.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1004, func_start: 305, branch: 274, structural_boundaries: 187
- `pkg/front_end/parser_testcases/error_recovery/with_outline/typing_string_interpolation_2.dart` (DART) | Magnitude: 8.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 9, args: 6, closures: 6, func_start: 4
- `pkg/front_end/testcases/patterns/side_effect.dart` (DART) | Magnitude: 5.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, branch: 5, func_start: 5, structural_boundaries: 4
- `runtime/bin/io_service.h` (CPP) | Magnitude: 12.74 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, args: 48, structural_boundaries: 7, macros: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/front_end/testcases/general/issue39421.dart` (DART) | Magnitude: 7.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 4, class_start: 4, api: 4, args: 3
- `runtime/platform/allocation.cc` (CPP) | Magnitude: 25.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, state_mutation: 9, safety_bypasses: 7
- `pkg/front_end/testcases/general/issue38812.dart` (DART) | Magnitude: 3.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: generics: 3, structural_boundaries: 2, func_start: 2, api: 2
- `pkg/front_end/testcases/inference/infer_types_on_generic_instantiations_infer.dart` (DART) | Magnitude: 7.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: func_start: 7, indent_spaces: 7, structural_boundaries: 4, closures: 3
- `pkg/front_end/testcases/nnbd/switch_redesign_fall_over.dart` (DART) | Magnitude: 3.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, branch: 6, func_start: 6, closures: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pkg/front_end/lib/src/type_inference/inference_visitor.dart` -> Churn: **100.0%** | Cog Load: 6.8981% | Debt: 89.787%
- `pkg/analyzer/lib/src/generated/resolver.dart` -> Churn: **96.64%** | Cog Load: 7.566% | Debt: 62.3355%
- `pkg/analyzer/lib/src/generated/error_verifier.dart` -> Churn: **88.24%** | Cog Load: 10.0468% | Debt: 90.083%
- `pkg/compiler/lib/src/universe/recorded_use.dart` -> Churn: **75.66%** | Cog Load: 9.4627% | Debt: 99.9488%
- `pkg/front_end/lib/src/source/outline_builder.dart` -> Churn: **75.66%** | Cog Load: 9.8488% | Debt: 80.1729%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `runtime/vm/service.cc` -> **Ryan Macnak** (100.0% isolated ownership) | Magnitude: 7259.68
- `runtime/vm/compiler/backend/il_arm.cc` -> **Ryan Macnak** (100.0% isolated ownership) | Magnitude: 7062.62
- `runtime/vm/simulator_riscv.cc` -> **Ryan Macnak** (100.0% isolated ownership) | Magnitude: 6931.56
- `pkg/vm_service/lib/src/vm_service.dart` -> **Nourhan Hasan** (100.0% isolated ownership) | Magnitude: 6497.3
- `runtime/vm/compiler/frontend/kernel_to_il.cc` -> **Alexander Markov** (100.0% isolated ownership) | Magnitude: 6344.34

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pkg/vm/testcases/transformations/deferred_loading/h.dart` -> **Severity: 493.091** (Blast Radius: 124.098 * Doc Risk: 3.9734%)
- `pkg/vm/testcases/transformations/deferred_loading/g.dart` -> **Severity: 429.695** (Blast Radius: 108.143 * Doc Risk: 3.9734%)
- `pkg/analyzer/tool/fine/ab_mutate/models.dart` -> **Severity: 153.779** (Blast Radius: 4.924 * Doc Risk: 31.2306%)
- `pkg/observatory/lib/src/models/objects/code.dart` -> **Severity: 107.269** (Blast Radius: 1.461 * Doc Risk: 73.4218%)
- `pkg/compiler/lib/src/serialization/serialization.dart` -> **Severity: 88.344** (Blast Radius: 0.902 * Doc Risk: 97.9425%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
