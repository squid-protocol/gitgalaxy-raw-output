# ARCHITECTURAL_BRIEF: swift
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apple/swift` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 26461 analyzed artifact(s), 2099051 LOC.
- **Load-bearing artifact:** `stdlib/private/StdlibUnittest/StdlibUnittest.swift` -- 758 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `benchmark/utils/main.swift` -- pulls in 197 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Sema/CSSimplify.cpp` at magnitude 12548.66 (structural weight, not risk).
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
| Total Artifacts | 30307 |
| Analyzed Artifacts (Scanned) | 26461 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3846 |
| Total LOC | 2099051 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.3% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5824 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.137 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3828 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 519 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SWIFT | 21339 | 863921 | 80.6% |
| CPP | 3232 | 1125123 | 12.2% |
| OBJECTIVE-C | 724 | 20913 | 2.7% |
| PLAINTEXT | 382 | 6 | 1.4% |
| PYTHON | 286 | 35645 | 1.1% |
| MAKEFILE | 151 | 32295 | 0.6% |
| JSON | 97 | 4177 | 0.4% |
| MARKDOWN | 85 | 0 | 0.3% |
| C | 63 | 2904 | 0.2% |
| SHELL | 30 | 3384 | 0.1% |
| YAML | 23 | 866 | 0.1% |
| YACC | 18 | 1810 | 0.1% |
| XML | 12 | 0 | 0.0% |
| ASSEMBLY | 5 | 486 | 0.0% |
| TD | 4 | 3293 | 0.0% |
| BATCH | 4 | 89 | 0.0% |
| M4 | 2 | 123 | 0.0% |
| POWERSHELL | 2 | 3910 | 0.0% |
| RUBY | 1 | 87 | 0.0% |
| JAVASCRIPT | 1 | 19 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `6.621`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +6.62; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Declarative / Non-Code 13%, Interface Declarations Files 11%, Parameter Forwarders Files 10%, Generic / Templated Code Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 25994 | 98.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 464 | 1.8% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3846*

**Composition by Extension & Reason:**
- `.sil`: 1293x Excluded (Unsupported Extension: '.sil'), 2x Unsupported Format (.sil)
- `.swift`: 48x Excluded (Machine-Generated Source Code Signature: 85 LOC), 45x Excluded (Saturation: Line 1 exceeds 500 chars), 25x Excluded (Machine-Generated Source Code Signature: 101 LOC)
- `.modulemap`: 334x Excluded (Unsupported Extension: '.modulemap'), 10x Unsupported Format (.modulemap)
- `.expected`: 306x Excluded (Unsupported Extension: '.expected'), 3x Unsupported Format (.expected)
- `.gyb`: 251x Unsupported Format (.gyb), 28x Excluded (Unsupported Extension: '.gyb'), 1x Excluded (Embedded Hex Payload: 2187 hex tokens in 1920 LOC)
- `.cmake`: 178x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 79x Excluded (Unsupported Extension: '.cmake'), 2x Unsupported Format (.cmake)
- `no_extension`: 59x Unsupported Format (.undeterminable), 51x Excluded (Unsupported Extension: '.swiftoverlay'), 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 22 LOC), 1x Excluded (Machine-Generated Source Code Signature: 104 LOC)
- `.response`: 100x Excluded (Unsupported Extension: '.response')
- `.apinotes`: 57x Excluded (Unsupported Extension: '.apinotes')
- `.rst`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 53x Excluded (Unsupported Extension: '.test'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 46x Excluded (Unsupported Extension: '.cfg'), 2x Unsupported Format (.cfg)
- `.test-sh`: 41x Excluded (Unsupported Extension: '.test-sh')
- `.h`: 13x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Machine-Generated Source Code Signature: 122 LOC), 2x Excluded (Embedded Hex Payload: 16950 hex tokens in 1728 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 11.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.4 | 96.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 358056 | 5917 | 9 | `lib/Sema/CSSimplify.cpp` |
| cleanup | 953 | 348 | 0 | `unittests/SourceKit/SwiftLang/EditingTest.cpp` |
| guards | 133949 | 6600 | 7 | `include/swift/SIL/SILInstruction.h` |
| danger | 18730 | 2682 | 1 | `lib/AST/ASTVerifier.cpp` |
| concurrency | 23164 | 1693 | 0 | `test/Concurrency/transfernonsendable.swift` |
| connectivity | 74902 | 8256 | 6 | `stdlib/private/StdlibCollectionUnittest/MinimalCollections.swift` |
| io | 3221 | 364 | 0 | `unittests/Basic/ManglingTestData.def` |
| crypto | 2 | 2 | 0 | `utils/bug_reducer/bug_reducer/subprocess_utils.py` |
| ipc | 362 | 94 | 0 | `test/Inputs/clang-importer-sdk/usr/include/Foundation.h` |
| time | 175 | 73 | 0 | `stdlib/public/Concurrency/Clock.cpp` |
| serialization | 108 | 42 | 0 | `test/Interpreter/SDK/check_class_for_archiving.swift` |
| regex | 364 | 86 | 0 | `utils/analyze_code_size.py` |
| events | 1814 | 375 | 0 | `validation-test/StdlibUnittest/AtomicInt.swift` |
| tests | 5472 | 229 | 0 | `utils/build_swift/tests/build_swift/test_shell.py` |
| docs | 169488 | 3489 | 3 | `include/swift/AST/Decl.h` |
| debt | 36304 | 5760 | 3 | `utils/bug_reducer/tests/testfuncbugreducer_testbasic.swift` |
| mutation | 347120 | 14020 | 22 | `lib/Sema/CSSimplify.cpp` |
| dead_code | 66988 | 10976 | 4 | `test/Runtime/null_vtable_entry_ptrauth.swift` |
| credential | 534 | 184 | 0 | `test/SILGen/objc_async_from_swift.swift` |
| threat | 14315 | 3590 | 1 | `test/attr/attr_objc.swift` |
| ml_ai | 9983 | 1174 | 0 | `test/AutoDiff/Sema/derivative_attr_type_checking.swift` |
| ui | 1088 | 240 | 0 | `utils/parser-lib/profile-input.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `unittests/Basic/ManglingTestData.def` (Hits: 489)
- `utils/build-script-impl` (Hits: 222)
- `include/swift/AST/Builtins.def` (Hits: 218)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **StdlibUnittest.swift** (`stdlib/private/StdlibUnittest/StdlibUnittest.swift`) — 758 inbound connections
2. **Assertions.h** (`include/swift/Basic/Assertions.h`) — 738 inbound connections
3. **ASTContext.h** (`include/swift/AST/ASTContext.h`) — 310 inbound connections
4. **Decl.h** (`include/swift/AST/Decl.h`) — 303 inbound connections
5. **LLVM.h** (`include/swift/Basic/LLVM.h`) — 249 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.swift** (`benchmark/utils/main.swift`) — 197 outbound dependencies
2. **SwiftMusl.h** (`stdlib/public/Platform/SwiftMusl.h`) — 175 outbound dependencies
3. **SwiftAndroidNDK.h** (`stdlib/public/Platform/SwiftAndroidNDK.h`) — 123 outbound dependencies
4. **ClangImporter.cpp** (`lib/ClangImporter/ClangImporter.cpp`) — 105 outbound dependencies
5. **diags-with-many-imports.swift** (`test/ClangImporter/diags-with-many-imports.swift`) — 100 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ConstraintSystem::repairFailures` **(Many-Argument Workhorses)** (@ `lib/Sema/CSSimplify.cpp`) -> Impact: **1365.5** | LOC: 1804
  * *Intent:* /// Attempt to repair typing failures and record fixes if needed. /// \return true if at least some of the failures has been repaired /// successfully...
- `SILParser::parseSpecificSILInstruction` **(Many-Argument Workhorses)** (@ `lib/SIL/Parser/ParseSIL.cpp`) -> Impact: **1280.9** | LOC: 1466
- `parseDeclSILOptional` **(Many-Argument Workhorses)** (@ `lib/SIL/Parser/ParseSIL.cpp`) -> Impact: **1203.0** | LOC: 338
- `foo` **(Compute Cores)** (@ `test/SourceKit/Misc/parser-cutoff.swift`) -> Impact: **1155.3** | LOC: 789
- `foo` **(Compute Cores)** (@ `validation-test/compiler_crashers_fixed/parser-cutoff.swift`) -> Impact: **1155.3** | LOC: 789
- `ConstraintSystem::matchTypes` **(Many-Argument Workhorses)** (@ `lib/Sema/CSSimplify.cpp`) -> Impact: **1106.3** | LOC: 1355
- `NodePrinter::print` **(Many-Argument Workhorses)** (@ `lib/Demangling/NodePrinter.cpp`) -> Impact: **1087.2** | LOC: 1384
- `Parser::parseNewDeclAttribute` **(Many-Argument Workhorses)** (@ `lib/Parse/ParseDecl.cpp`) -> Impact: **899.2** | LOC: 1526
- `diagSyntacticUseRestrictions` **(Many-Argument Workhorses)** (@ `lib/Sema/MiscDiagnostics.cpp`) -> Impact: **853.8** | LOC: 1423
  * *Intent:* /// limitations. /// - "&" (aka InOutExpressions) may only exist directly in function call /// argument lists. /// - 'self.init' and 'super.init' cann...
- `SILDeserializer::readSILInstruction` **(Many-Argument Workhorses)** (@ `lib/Serialization/DeserializeSIL.cpp`) -> Impact: **732.4** | LOC: 1187

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Sema` | 106 | 114280.4 | 25.16% | 56.18% |
| `validation-test/compiler_crashers_fixed` | 6329 | 76633.78 | 1.66% | 7.94% |
| `lib/AST` | 114 | 68195.12 | 25.65% | 81.64% |
| `lib/IRGen` | 169 | 64865.72 | 12.4% | 42.04% |
| `lib/SILGen` | 71 | 36940.02 | 17.5% | 50.77% |
| `stdlib/public/core` | 225 | 33585.24 | 13.1% | 60.33% |
| `test/Concurrency` | 281 | 27625.24 | 14.5% | 0.0% |
| `test/SILOptimizer` | 555 | 26840.68 | 4.73% | 0.0% |
| `include/swift/AST` | 245 | 25903.34 | 3.89% | 16.72% |
| `lib/ClangImporter` | 41 | 25664.94 | 24.36% | 57.78% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `SwiftCompilerSources/Sources/SIL/Builder.swift` -> **100.0%** Exposure
- `benchmark/single-source/PolymorphicCalls.swift` -> **100.0%** Exposure
- `lib/ASTGen/Sources/ASTGen/EmbeddedSupport.swift` -> **100.0%** Exposure
- `stdlib/private/StdlibCollectionUnittest/MinimalCollections.swift` -> **100.0%** Exposure
- `stdlib/private/StdlibUnittest/OpaqueIdentityFunctions.swift` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `SwiftCompilerSources/Sources/SIL/Effects.swift` -> **100.0%** Exposure
- `benchmark/multi-source/Monoids/Trie.swift` -> **100.0%** Exposure
- `benchmark/single-source/DictTest3.swift` -> **100.0%** Exposure
- `benchmark/single-source/HTTP2StateMachine.swift` -> **100.0%** Exposure
- `benchmark/single-source/Hash.swift` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/Runtime/null_vtable_entry_ptrauth.swift` -> **1002** Orphaned Functions | **0** Duplicates
- `lib/AST/Decl.cpp` -> **676** Orphaned Functions | **2** Duplicates
- `lib/Demangling/Remangler.cpp` -> **393** Orphaned Functions | **0** Duplicates
- `lib/Demangling/OldRemangler.cpp` -> **383** Orphaned Functions | **0** Duplicates
- `test/SILOptimizer/moveonly_addresschecker_diagnostics.swift` -> **377** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `75` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `35605` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Sema/CSSimplify.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 12548.66 | **LOC:** 16663 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 32.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 83.6735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConstraintSystem::repairFailures` **(Many-Argument Workhorses)** (Impact: 1365.5)
    * *Intent:* /// Attempt to repair typing failures and record fixes if needed. /// \return true if at least some ...
  * `ConstraintSystem::matchTypes` **(Many-Argument Workhorses)** (Impact: 1106.3)
  * `ConstraintSystem::simplifyFixConstraint` **(Many-Argument Workhorses)** (Impact: 542.3)
  * `matchCallArgumentsImpl` **(Many-Argument Workhorses)** (Impact: 528.4)
  * `performMemberLookup` **(Many-Argument Workhorses)** (Impact: 508.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 593 instances
* *State Mutation (weighted view):* 1824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3789`, `structural_boundaries: 2913`, `args: 862`, `func_start: 185`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 638`, `dead_code: 42`, `planned_debt: 18`, `fragile_debt: 59`, `unreferenced_by_name: 97`
* *Architecture:* `api: 3`, `import: 37`
* *Defense:* `safety: 116`, `doc: 152`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` CSDiagnostics.h, OpenedExistentials.h, TypeCheckConcurrency.h, TypeCheckEffects.h, TypeChecker.h, ArrayRef.h, SetVector.h, Compiler.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Parse/ParseDecl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 7470.2 | **LOC:** 10979 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 25.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.5%)
- **Documentation Coverage:** 65.8385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::parseNewDeclAttribute` **(Many-Argument Workhorses)** (Impact: 899.2)
  * `Parser::parseDecl` **(Many-Argument Workhorses)** (Impact: 323.9)
    * *Intent:* /// /// \verbatim /// decl: /// decl-typealias /// decl-extension /// decl-let /// decl-var /// decl...
  * `Parser::parseTypeAttribute` **(Many-Argument Workhorses)** (Impact: 256.8)
    * *Intent:* /// \verbatim /// attribute-type: /// 'noreturn' /// \endverbatim /// /// \param justChecking - if t...
  * `Parser::parseDeclVar` **(Many-Argument Workhorses)** (Impact: 179.9)
    * *Intent:* /// Parse a 'var', 'let', or 'inout' declaration, doing no token skipping on error.
  * `Parser::parseExtendedAvailabilitySpecList` **(Many-Argument Workhorses)** (Impact: 134.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 544 instances
* *State Mutation (weighted view):* 1692
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2416`, `structural_boundaries: 1127`, `args: 1376`, `func_start: 138`, `class_start: 5`
* *Risk/State:* `state_mutation: 604`, `dead_code: 8`, `planned_debt: 14`, `fragile_debt: 7`, `unreferenced_by_name: 91`
* *Architecture:* `api: 1`, `import: 47`
* *Defense:* `safety: 100`, `doc: 387`, `immutability_locks: 46`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` algorithm, initializer_list, PointerUnion.h, StringSwitch.h, Twine.h, Compiler.h, MemoryBuffer.h, Path.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/AST/Decl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6960.08 | **LOC:** 13528 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **71**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.0%), Guard Balance (formerly Safety Score) (59.1%)
- **Documentation Coverage:** 92.8315% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `swift::conflicting` **(Many-Argument Workhorses)** (Impact: 103.8)
  * `checkAccess` **(Many-Argument Workhorses)** (Impact: 95.6)
    * *Intent:* /// Checks if \p VD may be used from \p useDC, taking \@testable and \@_spi /// imports into account...
  * `AbstractFunctionDecl::getObjCSelector` **(Many-Argument Workhorses)** (Impact: 89.9)
  * `Decl::getAttributeInsertionLoc` **(Compute Cores)** (Impact: 72.2)
  * `MacroDecl::getIntroducedNames` **(Many-Argument Workhorses)** (Impact: 72.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 1048
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2849`, `structural_boundaries: 3170`, `args: 1066`, `func_start: 798`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 406`, `dead_code: 10`, `planned_debt: 7`, `fragile_debt: 31`, `duplicate_logic: 2`, `unreferenced_by_name: 676`
* *Architecture:* `api: 2`, `import: 93`
* *Defense:* `safety: 222`, `doc: 195`, `immutability_locks: 770`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 63):` algorithm, Attr.h, DeclObjC.h, CharInfo.h, Module.h, TargetInfo.h, MacroInfo.h, DenseMap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/SIL/Parser/ParseSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6947.84 | **LOC:** 9066 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 18.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILParser::parseSpecificSILInstruction` **(Many-Argument Workhorses)** (Impact: 1280.9)
  * `parseDeclSILOptional` **(Many-Argument Workhorses)** (Impact: 1203.0)
  * `SILParser::parseKeyPathPatternComponent` **(Many-Argument Workhorses)** (Impact: 322.7)
  * `SILParser::parseCallInstruction` **(Many-Argument Workhorses)** (Impact: 185.8)
  * `parseSILWitnessTableEntry` **(Many-Argument Workhorses)** (Impact: 141.4)
    * *Intent:* /// Parser a single SIL wtable entry and add it to either \p witnessEntries /// or \c conditionalCon...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 689 instances
* *State Mutation (weighted view):* 2106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2680`, `structural_boundaries: 1163`, `args: 1404`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `state_mutation: 728`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 12`, `unreferenced_by_name: 61`
* *Architecture:* `api: 1`, `import: 44`
* *Defense:* `safety: 78`, `doc: 230`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` SILParser.h, SILParserFunctionBuilder.h, SILParserState.h, StringSwitch.h, CommandLine.h, SaveAndRestore.h, ASTWalker.h, ConformanceLookup.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ClangImporter/ImportDecl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6789.26 | **LOC:** 11207 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 37.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **82**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.2%), Debt Markers (formerly Tech Debt) (84.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 75.463% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `importFunctionDecl` **(Many-Argument Workhorses)** (Impact: 272.9)
  * `getSwiftStdlibType` **(Many-Argument Workhorses)** (Impact: 262.2)
    * *Intent:* #endif /// Map a well-known C type to a swift type from the standard library. /// /// \param IsError...
  * `VisitRecordDecl` **(Compute Cores)** (Impact: 241.2)
  * `validateForeignReferenceType` **(Many-Argument Workhorses)** (Impact: 169.1)
  * `SwiftDeclConverter::importConstructor` **(Many-Argument Workhorses)** (Impact: 165.9)
    * *Intent:* /// Given an imported method, try to import it as a constructor. /// /// Objective-C methods in the ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 431 instances
* *State Mutation (weighted view):* 1348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2327`, `structural_boundaries: 1796`, `args: 661`, `func_start: 213`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 486`, `dead_code: 18`, `planned_debt: 39`, `fragile_debt: 63`, `unreferenced_by_name: 107`
* *Architecture:* `api: 4`, `import: 82`
* *Defense:* `safety: 137`, `doc: 259`, `immutability_locks: 320`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 58):` CFTypeInfo.h, CXXMethodBridging.h, ClangDerivedConformances.h, ImporterImpl.h, InferredAttributes.def, MappedTypes.def, SwiftDeclSynthesizer.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/MiscDiagnostics.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5650.84 | **LOC:** 6989 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 15.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.9%)
- **Documentation Coverage:** 73.5751% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagSyntacticUseRestrictions` **(Many-Argument Workhorses)** (Impact: 853.8)
    * *Intent:* /// limitations. /// - "&" (aka InOutExpressions) may only exist directly in function call /// argum...
  * `checkForSuspiciousBitCasts` **(Many-Argument Workhorses)** (Impact: 272.5)
  * `diagnoseUnintendedOptionalBehavior` **(Many-Argument Workhorses)** (Impact: 167.5)
  * `walkToExprPre` **(Compute Cores)** (Impact: 132.4)
  * `swift::diagnoseArgumentLabelError` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /// Diagnose an argument labeling issue, returning true if we successfully /// diagnosed the issue.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1035
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1503`, `structural_boundaries: 1201`, `args: 815`, `func_start: 185`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 357`, `dead_code: 11`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 19`
* *Architecture:* `api: 18`, `import: 40`
* *Defense:* `safety: 77`, `doc: 196`, `immutability_locks: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckEmbedded.h, TypeCheckInvertible.h, TypeChecker.h, DeclObjC.h, MapVector.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/AST/ASTPrinter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5608.16 | **LOC:** 9031 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 13.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **70**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (77.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.3%)
- **Documentation Coverage:** 93.5354% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PrintAST::printSingleDepthOfGenericSignature` **(Many-Argument Workhorses)** (Impact: 198.1)
  * `PrintAST::printAccessors` **(Compute Cores)** (Impact: 182.4)
  * `PrintOptions::printSwiftInterfaceFile` **(Many-Argument Workhorses)** (Impact: 172.3)
  * `ShouldPrintChecker::shouldPrint` **(Compute Cores)** (Impact: 153.1)
  * `printFunctionExtInfo` **(Compute Cores)** (Impact: 132.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 240 instances
* *State Mutation (weighted view):* 768
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2000`, `structural_boundaries: 1420`, `args: 1267`, `func_start: 480`, `class_start: 7`
* *Risk/State:* `state_mutation: 288`, `dead_code: 11`, `planned_debt: 7`, `fragile_debt: 25`, `unreferenced_by_name: 322`
* *Architecture:* `api: 4`, `import: 72`
* *Defense:* `safety: 35`, `doc: 121`, `immutability_locks: 247`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 59):` FeatureSet.h, algorithm, ASTContext.h, Attr.h, Decl.h, DeclObjC.h, Module.h, SourceManager.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/ClangImporter/ClangImporter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5547.48 | **LOC:** 9269 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 29.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **105**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Debt Markers (formerly Tech Debt) (98.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.7%), Guard Balance (formerly Safety Score) (73.6%)
- **Documentation Coverage:** 97.076% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `importer::getNormalInvocationArguments` **(Many-Argument Workhorses)** (Impact: 148.4)
  * `ClangImporter::create` **(Many-Argument Workhorses)** (Impact: 139.6)
  * `importer::addCommonInvocationArguments` **(Many-Argument Workhorses)** (Impact: 121.7)
  * `ClangImporter::Implementation::lookupValue` **(Many-Argument Workhorses)** (Impact: 112.0)
  * `ClangImporter::Implementation::loadNamedMembers` **(Many-Argument Workhorses)** (Impact: 93.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 435 instances
* *Memory Alloc (weighted view):* 45
* *State Mutation (weighted view):* 1376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1698`, `structural_boundaries: 1697`, `args: 602`, `func_start: 342`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 506`, `dead_code: 9`, `planned_debt: 12`, `fragile_debt: 52`, `duplicate_logic: 2`, `unreferenced_by_name: 221`
* *Architecture:* `api: 14`, `import: 105`
* *Defense:* `safety: 109`, `doc: 20`, `immutability_locks: 363`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` CFTypeInfo.h, ClangDerivedConformances.h, ClangDiagnosticConsumer.h, ClangIncludePaths.h, ImporterImpl.h, SwiftDeclSynthesizer.h, algorithm, ASTContext.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/CSApply.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5385.02 | **LOC:** 9896 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 35.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (88.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.1%)
- **Documentation Coverage:** 73.3577% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExprRewriter::coerceToType` **(Many-Argument Workhorses)** (Impact: 577.7)
  * `buildMemberRef` **(Many-Argument Workhorses)** (Impact: 192.1)
    * *Intent:* /// Build a new member reference with the given base and member.
  * `ExprRewriter::coerceCallArguments` **(Many-Argument Workhorses)** (Impact: 147.9)
  * `ExprWalker::rewriteTarget` **(Compute Cores)** (Impact: 139.0)
  * `ExprRewriter::finishApply` **(Many-Argument Workhorses)** (Impact: 104.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 432 instances
* *State Mutation (weighted view):* 1377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1544`, `structural_boundaries: 1725`, `args: 567`, `func_start: 261`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 513`, `dead_code: 9`, `planned_debt: 11`, `fragile_debt: 32`, `duplicate_logic: 4`, `unreferenced_by_name: 137`
* *Architecture:* `api: 8`, `import: 44`
* *Defense:* `safety: 157`, `doc: 413`, `immutability_locks: 104`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` CSDiagnostics.h, CodeSynthesis.h, MiscDiagnostics.h, OpenedExistentials.h, TypeCheckConcurrency.h, TypeCheckEmbedded.h, TypeCheckMacros.h, TypeCheckProtocol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/TypeCheckConcurrency.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5353.84 | **LOC:** 9034 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.6%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `computeActorIsolation` **(Many-Argument Workhorses)** (Impact: 197.2)
  * `checkFunctionConversion` **(Many-Argument Workhorses)** (Impact: 135.2)
    * *Intent:* /// Some function conversions synthesized by the constraint solver may not /// be correct AND the so...
  * `checkReference` **(Many-Argument Workhorses)** (Impact: 132.6)
    * *Intent:* /// Check a reference to the given declaration. /// /// \param base For a reference to a member, the...
  * `swift::tryDiagnoseExecutorConformance` **(Many-Argument Workhorses)** (Impact: 114.5)
  * `getIsolationFromAttributes` **(Many-Argument Workhorses)** (Impact: 99.5)
    * *Intent:* /// Determine actor isolation solely from attributes. /// /// \returns the actor isolation determine...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 253 instances
* *State Mutation (weighted view):* 770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2090`, `structural_boundaries: 1579`, `args: 353`, `func_start: 200`, `class_start: 10`
* *Risk/State:* `state_mutation: 264`, `dead_code: 13`, `planned_debt: 3`, `fragile_debt: 28`, `unreferenced_by_name: 73`
* *Architecture:* `api: 6`, `import: 35`
* *Defense:* `safety: 115`, `doc: 298`, `immutability_locks: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` MiscDiagnostics.h, NonisolatedNonsendingByDefaultMigration.h, TypeCheckConcurrency.h, TypeCheckDistributed.h, TypeCheckInvertible.h, TypeCheckProtocol.h, TypeCheckType.h, TypeChecker.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/SILGen/SILGenApply.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4880.96 | **LOC:** 8479 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 15.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.7%), Debt Markers (formerly Tech Debt) (70.6%)
- **Documentation Coverage:** 80.7074% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILGenFunction::emitApply` **(Many-Argument Workhorses)** (Impact: 297.5)
    * *Intent:* //===----------------------------------------------------------------------===// // Top Level Entryp...
  * `emitRawApply` **(Many-Argument Workhorses)** (Impact: 140.5)
    * *Intent:* /// Emit a raw apply operation, performing no additional lowering of /// either the arguments or the...
  * `SILGenFunction::findStorageReferenceExprForMoveOnly` **(Many-Argument Workhorses)** (Impact: 90.6)
  * `SILGenFunction::tryEmitAddressableParameterAsAddress` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `emitDelayedArguments` **(Many-Argument Workhorses)** (Impact: 81.6)
    * *Intent:* /// Perform the formal-access phase of call argument emission by emitting /// all of the delayed arg...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 402 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1210`, `structural_boundaries: 1171`, `args: 838`, `func_start: 306`, `class_start: 24`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 486`, `dead_code: 7`, `planned_debt: 31`, `fragile_debt: 15`, `unreferenced_by_name: 95`
* *Architecture:* `api: 18`, `import: 45`
* *Defense:* `safety: 188`, `doc: 224`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` ArgumentScope.h, ArgumentSource.h, Callee.h, Conversion.h, ExecutorBreadcrumb.h, FormalEvaluation.h, Initialization.h, LValue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/TypeCheckAttr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4720.44 | **LOC:** 9168 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 13.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.9%), Debt Markers (formerly Tech Debt) (82.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findAutoDiffOriginalFunctionDecl` **(Many-Argument Workhorses)** (Impact: 144.5)
    * *Intent:* /// function name, lookup context, and the expected original function type. /// /// If the base type...
  * `typeCheckDerivativeAttr` **(Compute Cores)** (Impact: 109.5)
    * *Intent:* /// Type-checks the given `@derivative` attribute `attr` on declaration `D`. /// /// Effects are: //...
  * `AttributeChecker::visitObjCAttr` **(Compute Cores)** (Impact: 94.6)
  * `suggestAnyAppleOSAvailability` **(Many-Argument Workhorses)** (Impact: 93.2)
    * *Intent:* /// Check for platform availability attributes that could be consolidated using /// a single `@avail...
  * `AttributeChecker::visitNonisolatedAttr` **(Compute Cores)** (Impact: 82.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1857`, `structural_boundaries: 1701`, `args: 925`, `func_start: 224`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 276`, `dead_code: 11`, `planned_debt: 11`, `fragile_debt: 22`, `unreferenced_by_name: 145`
* *Architecture:* `api: 2`, `import: 44`
* *Defense:* `safety: 44`, `doc: 135`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 41):` MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckDistributed.h, TypeCheckEmbedded.h, TypeCheckMacros.h, TypeCheckObjC.h, TypeCheckType.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/TypeCheckProtocol.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 4688.58 | **LOC:** 7702 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **56**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.2%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 56.1151% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TypeChecker::checkConformancesInContext` **(Compute Cores)** (Impact: 236.5)
  * `diagnoseMatch` **(Many-Argument Workhorses)** (Impact: 217.6)
    * *Intent:* /// Diagnose a requirement match, describing what went wrong (or not).
  * `swift::matchWitness` **(Many-Argument Workhorses)** (Impact: 158.4)
  * `WitnessChecker::findBestWitness` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `checkIndividualConformance` **(Compute Cores)** (Impact: 126.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1665`, `structural_boundaries: 1241`, `args: 462`, `func_start: 135`, `class_start: 12`
* *Risk/State:* `state_mutation: 319`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 32`, `unreferenced_by_name: 36`
* *Architecture:* `api: 4`, `import: 56`
* *Defense:* `safety: 76`, `doc: 154`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 54):` DerivedConformance.h, MiscDiagnostics.h, OpenedExistentials.h, TypeAccessScopeChecker.h, TypeCheckAccess.h, TypeCheckAvailability.h, TypeCheckBitwise.h, TypeCheckConcurrency.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/TypeCheckType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4635.48 | **LOC:** 7468 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 14.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **59**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Debt Markers (formerly Tech Debt) (81.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.4%)
- **Documentation Coverage:** 82.5843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TypeResolver::resolveASTFunctionType` **(Many-Argument Workhorses)** (Impact: 219.2)
  * `TypeResolver::resolveAttributedType` **(Many-Argument Workhorses)** (Impact: 196.0)
  * `TypeResolver::resolveSILFunctionType` **(Many-Argument Workhorses)** (Impact: 147.4)
  * `TypeResolver::resolveType` **(Many-Argument Workhorses)** (Impact: 143.7)
  * `TypeResolver::resolveImplicitlyUnwrappedOptionalType` **(Many-Argument Workhorses)** (Impact: 110.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 321 instances
* *State Mutation (weighted view):* 991
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1530`, `structural_boundaries: 1226`, `args: 509`, `func_start: 166`, `class_start: 9`
* *Risk/State:* `state_mutation: 349`, `dead_code: 6`, `planned_debt: 12`, `fragile_debt: 34`, `unreferenced_by_name: 86`
* *Architecture:* `api: 9`, `import: 60`
* *Defense:* `safety: 66`, `doc: 106`, `immutability_locks: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 56):` LiteralExpressionFolding.h, MiscDiagnostics.h, NonisolatedNonsendingByDefaultMigration.h, TypeCheckAccess.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckInvertible.h, TypeCheckProtocol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Frontend/CompilerInvocation.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4627.48 | **LOC:** 4569 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 12.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.6%), Complexity Load (formerly Cognitive Load) (89.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.6%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseIRGenArgs` **(Many-Argument Workhorses)** (Impact: 624.2)
  * `ParseLangArgs` **(Many-Argument Workhorses)** (Impact: 536.9)
  * `ParseSILArgs` **(Many-Argument Workhorses)** (Impact: 319.4)
  * `ParseSearchPathArgs` **(Many-Argument Workhorses)** (Impact: 189.8)
  * `ParseEnabledFeatureArgs` **(Many-Argument Workhorses)** (Impact: 166.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 543 instances
* *State Mutation (weighted view):* 1772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 963`, `structural_boundaries: 340`, `args: 1085`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `state_mutation: 686`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 14`, `unreferenced_by_name: 18`
* *Architecture:* `import: 32`
* *Defense:* `safety: 44`, `doc: 17`, `immutability_locks: 171`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` ArgsToFrontendOptionsConverter.h, Driver.h, STLExtras.h, Arg.h, ArgList.h, Option.h, FileSystem.h, LineIterator.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Sema/CSDiagnostics.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4596.36 | **LOC:** 9761 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 21.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.2%), Mutation Surface (formerly State Flux) (97.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 95.7096% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ContextualFailure::diagnoseAsError` **(I/O & Config Routines)** (Impact: 93.8)
  * `AllowTypeOrInstanceMemberFailure::diagnoseAsError` **(Compute Cores)** (Impact: 87.8)
  * `MissingMemberFailure::diagnoseUnsafeCxxMethod` **(Many-Argument Workhorses)** (Impact: 86.5)
  * `ContextualFailure::getDiagnosticFor` **(Compute Cores)** (Impact: 80.5)
  * `GenericArgumentsMismatchFailure::diagnoseAsError` **(I/O & Config Routines)** (Impact: 73.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 390 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2075`, `structural_boundaries: 2288`, `args: 416`, `func_start: 301`, `class_start: 5`
* *Risk/State:* `state_mutation: 399`, `dead_code: 15`, `planned_debt: 8`, `fragile_debt: 15`, `duplicate_logic: 3`, `unreferenced_by_name: 259`
* *Architecture:* `api: 2`, `import: 39`
* *Defense:* `safety: 68`, `doc: 14`, `immutability_locks: 211`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 38):` CSDiagnostics.h, MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckProtocol.h, TypeCheckType.h, TypoCorrection.h, ArrayRef.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Serialization/Deserialization.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4395.24 | **LOC:** 9639 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 23.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 82.7434% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ModuleFile::resolveCrossReference` **(Many-Argument Workhorses)** (Impact: 370.8)
  * `DeclDeserializer::deserializeDeclCommon` **(I/O & Config Routines)** (Impact: 196.9)
  * `ModuleFile::finishNormalConformance` **(Many-Argument Workhorses)** (Impact: 136.4)
  * `deserializeAnyFunc` **(Many-Argument Workhorses)** (Impact: 115.7)
  * `filterValues` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /// Remove values from \p values that don't match the expected type or module. /// /// Any of \p exp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 421 instances
* *State Mutation (weighted view):* 1310
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1553`, `structural_boundaries: 1516`, `args: 871`, `func_start: 196`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 468`, `planned_debt: 5`, `fragile_debt: 22`, `unreferenced_by_name: 122`
* *Architecture:* `api: 7`, `import: 50`
* *Defense:* `safety: 129`, `doc: 84`, `immutability_locks: 77`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` BCReadingExtras.h, DeclTypeRecordNodes.def, DeserializationErrors.h, ModuleFile.h, ModuleFormat.h, Attr.h, DeclTemplate.h, AttributeCommonInfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/IRGen/GenCall.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4336.18 | **LOC:** 7072 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (93.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%)
- **Documentation Coverage:** 88.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CallEmission::externalizeArguments` **(Many-Argument Workhorses)** (Impact: 136.4)
  * `NativeConventionSchema::mapIntoNative` **(Many-Argument Workhorses)** (Impact: 119.3)
  * `SignatureExpansion::expandExternalSignatureTypes` **(Compute Cores)** (Impact: 101.7)
    * *Intent:* /// Expand the result and parameter types to the appropriate LLVM IR /// types for C, C++ and Object...
  * `irgen::emitAsyncReturn` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `SignatureExpansion::expandParameters` **(Compute Cores)** (Impact: 86.6)
    * *Intent:* /// Expand the abstract parameters of a SIL function type into the physical /// parameters of an LLV...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1239`, `structural_boundaries: 1152`, `args: 851`, `func_start: 273`, `class_start: 9`
* *Risk/State:* `state_mutation: 494`, `dead_code: 14`, `planned_debt: 13`, `fragile_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 154`
* *Architecture:* `api: 5`, `import: 59`
* *Defense:* `safety: 241`, `doc: 67`, `immutability_locks: 117`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` CallEmission.h, ConstantBuilder.h, EntryPointArgumentEmission.h, Explosion.h, GenCall.h, GenCoro.h, GenFunc.h, GenHeap.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/IRGen/IRGenSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4319.68 | **LOC:** 8722 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 29.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **87**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Mutation Surface (formerly State Flux) (95.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.0%)
- **Documentation Coverage:** 89.4988% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitEntryPointArgumentsNativeCC` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /// Emit entry point arguments for a SILFunction with the Swift calling /// convention.
  * `IRGenSILFunction::visitFullApplySite` **(Compute Cores)** (Impact: 108.0)
  * `LoweredValue::getCallee` **(Many-Argument Workhorses)** (Impact: 76.5)
  * `IRGenSILFunction::emitDebugInfoAfterAllocStack` **(Many-Argument Workhorses)** (Impact: 73.2)
    * *Intent:* /// Do not instantiate type metadata in here, since this may allocate on-stack /// packs which will ...
  * `isSafeForMemCpyPeephole` **(Many-Argument Workhorses)** (Impact: 71.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 298 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 945
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1277`, `structural_boundaries: 1614`, `args: 957`, `func_start: 419`, `class_start: 16`
* *Risk/State:* `state_mutation: 349`, `dead_code: 8`, `planned_debt: 17`, `fragile_debt: 20`, `duplicate_logic: 20`, `unreferenced_by_name: 241`
* *Architecture:* `api: 8`, `import: 89`
* *Defense:* `safety: 177`, `doc: 148`, `immutability_locks: 111`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 72):` CallEmission.h, EntryPointArgumentEmission.h, Explosion.h, GenArchetype.h, GenBorrow.h, GenBuiltin.h, GenCall.h, GenCast.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/SILGen/SILGenExpr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4116.5 | **LOC:** 7793 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 36.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **54**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Debt Markers (formerly Tech Debt) (91.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.8%)
- **Documentation Coverage:** 89.4161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILGenModule::emitKeyPathComponentForDecl` **(Many-Argument Workhorses)** (Impact: 271.4)
  * `convertFunctionRepresentation` **(Many-Argument Workhorses)** (Impact: 97.3)
    * *Intent:* // Change the representation without changing the signature or // abstraction level.
  * `RValueEmitter::visitKeyPathExpr` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `SILGenFunction::emitOptionalEvaluation` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `getOrCreateKeyPathEqualsAndHash` **(Many-Argument Workhorses)** (Impact: 78.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 327 instances
* *State Mutation (weighted view):* 1054
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1000`, `structural_boundaries: 1221`, `args: 1232`, `func_start: 272`, `class_start: 12`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 400`, `dead_code: 6`, `planned_debt: 12`, `fragile_debt: 17`, `unreferenced_by_name: 148`
* *Architecture:* `api: 9`, `import: 54`
* *Defense:* `safety: 192`, `doc: 110`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` ArgumentScope.h, ArgumentSource.h, Callee.h, Condition.h, Conversion.h, Initialization.h, LValue.h, RValue.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/AST/ASTContext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4093.36 | **LOC:** 7562 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **92**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Mutation Surface (formerly State Flux) (90.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.2%)
- **Documentation Coverage:** 89.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILFunctionType::SILFunctionType` **(Many-Argument Workhorses)** (Impact: 249.0)
  * `ASTContext::canImportModuleImpl` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `swift::computeSelfParam` **(Many-Argument Workhorses)** (Impact: 94.2)
  * `SILFunctionType::get` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `ASTContext::getProtocol` **(Compute Cores)** (Impact: 87.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 248 instances
* *Memory Alloc (weighted view):* 94
* *State Mutation (weighted view):* 800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1229`, `structural_boundaries: 1497`, `args: 811`, `func_start: 376`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 304`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 272`
* *Architecture:* `import: 102`
* *Defense:* `safety: 187`, `doc: 203`, `immutability_locks: 288`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 81):` AbstractConformance.h, ClangTypeConverter.h, ForeignRepresentationInfo.h, RewriteContext.h, SubstitutionMapStorage.h, algorithm, Type.h, dlfcn.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stdlib/public/runtime/Metadata.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4029.3 | **LOC:** 8514 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.0%), Guard Balance (formerly Safety Score) (75.3%)
- **Documentation Coverage:** 82.3276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TupleCacheEntry::tryInitialize` **(Many-Argument Workhorses)** (Impact: 84.9)
  * `swift::_swift_addRefCountStringForMetatype` **(Many-Argument Workhorses)** (Impact: 83.5)
  * `findAnyTransitiveMetadata` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* /// Search all the metadata that the given type has transitive completeness /// requirements on for ...
  * `_swift_initClassMetadataImpl` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `swift_getAssociatedTypeWitnessSlowImpl` **(Many-Argument Workhorses)** (Impact: 48.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 329 instances
* *State Mutation (weighted view):* 1109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 945`, `structural_boundaries: 1586`, `args: 704`, `func_start: 438`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 144`, `state_mutation: 451`, `dead_code: 8`, `planned_debt: 24`, `fragile_debt: 7`, `unreferenced_by_name: 133`
* *Architecture:* `api: 28`, `import: 54`
* *Defense:* `safety: 176`, `doc: 248`, `sync_locks: 1`, `immutability_locks: 901`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` CompatibilityOverride.h, CompatibilityOverrideIncludePath.h, BytecodeLayouts.h, ErrorObject.h, ExistentialMetadataImpl.h, GenericCacheEntry.h, MetadataCache.h, ObjCRuntimeGetImageNameFromClass.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/IRGen/GenEnum.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4025.1 | **LOC:** 7879 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.5%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 88.5167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitValueSwitch` **(Many-Argument Workhorses)** (Impact: 86.6)
  * `EnumImplStrategy::get` **(Many-Argument Workhorses)** (Impact: 85.5)
  * `MultiPayloadEnumImplStrategy::completeFixedLayout` **(Many-Argument Workhorses)** (Impact: 84.6)
  * `emitIndirectInitialize` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `MultiPayloadEnumImplStrategy` **(Many-Argument Workhorses)** (Impact: 69.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 243 instances
* *State Mutation (weighted view):* 787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 880`, `structural_boundaries: 1150`, `args: 1432`, `func_start: 418`, `class_start: 17`
* *Risk/State:* `state_mutation: 301`, `dead_code: 14`, `planned_debt: 12`, `fragile_debt: 15`, `duplicate_logic: 22`, `unreferenced_by_name: 49`
* *Architecture:* `api: 25`, `import: 35`
* *Defense:* `safety: 379`, `doc: 115`, `immutability_locks: 417`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 31):` BitPatternBuilder.h, ClassTypeInfo.h, GenDecl.h, GenEnum.h, GenMeta.h, GenProto.h, GenType.h, IRGenDebugInfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Serialization/DeserializeSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3783.92 | **LOC:** 5555 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 21.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 83.6957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILDeserializer::readSILInstruction` **(Many-Argument Workhorses)** (Impact: 732.4)
  * `SILDeserializer::readSILFunctionChecked` **(Many-Argument Workhorses)** (Impact: 471.0)
  * `SILDeserializer::SILDeserializer` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `SILDeserializer::readGlobalVar` **(Many-Argument Workhorses)** (Impact: 98.3)
  * `SILDeserializer::readWitnessTableChecked` **(Many-Argument Workhorses)** (Impact: 56.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 431 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1272`, `structural_boundaries: 706`, `args: 1141`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 505`, `dead_code: 7`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 62`
* *Architecture:* `api: 2`, `import: 31`
* *Defense:* `safety: 183`, `doc: 36`, `immutability_locks: 22`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` BCReadingExtras.h, DeserializationErrors.h, DeserializeSIL.h, ModuleFile.h, SILFormat.h, SILSerializationFunctionBuilder.h, SerializationFormat.h, Statistic.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/SIL/IR/SILFunctionType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3778.92 | **LOC:** 5658 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.8%), Guard Balance (formerly Safety Score) (64.8%)
- **Documentation Coverage:** 77.4869% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSILFunctionType` **(Many-Argument Workhorses)** (Impact: 290.0)
    * *Intent:* /// reabstracted to the most general type, which means that we'd /// expect the wrong abstraction co...
  * `getAutoDiffPullbackType` **(Many-Argument Workhorses)** (Impact: 128.1)
    * *Intent:* /// Returns the pullback type for the given original function type, parameter /// indices, and resul...
  * `getNativeSILFunctionType` **(Many-Argument Workhorses)** (Impact: 124.6)
  * `swift::buildSILFunctionThunkType` **(Many-Argument Workhorses)** (Impact: 118.8)
    * *Intent:* /// Build the type of a function transformation thunk.
  * `areABICompatibleParamsOrReturns` **(Many-Argument Workhorses)** (Impact: 118.5)
    * *Intent:* // TODO: We should compare generic signatures. Class and witness methods // allow variance in "self"...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 777
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1090`, `structural_boundaries: 909`, `args: 373`, `func_start: 189`, `class_start: 17`
* *Risk/State:* `state_mutation: 295`, `dead_code: 7`, `planned_debt: 14`, `fragile_debt: 14`, `duplicate_logic: 14`, `unreferenced_by_name: 39`
* *Architecture:* `api: 9`, `import: 32`
* *Defense:* `safety: 162`, `doc: 159`, `immutability_locks: 209`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` ASTContext.h, Attr.h, DeclCXX.h, DeclObjC.h, CocoaConventions.h, CommandLine.h, Compiler.h, Debug.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/ClangImporter/ClangImporter.cpp` -> Churn: **96.68%** | Cog Load: 59.8925% | Debt: 98.5677%
- `utils/build.ps1` -> Churn: **94.96%** | Cog Load: 74.8808% | Debt: 29.7858%
- `lib/Sema/CSBindings.cpp` -> Churn: **92.84%** | Cog Load: 44.6502% | Debt: 95.0154%
- `lib/Sema/CSSimplify.cpp` -> Churn: **91.05%** | Cog Load: 58.8574% | Debt: 53.5628%
- `lib/Sema/TypeCheckConcurrency.cpp` -> Churn: **86.75%** | Cog Load: 17.8035% | Debt: 58.728%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/ClangImporter/ImportName.cpp` -> **Gabor Horvath** (83.3% isolated ownership) | Magnitude: 2317.62
- `stdlib/public/RuntimeModule/Dwarf.swift` -> **Alastair Houghton** (88.9% isolated ownership) | Magnitude: 2188.48
- `stdlib/public/core/Codable.swift` -> **Zev Eisenberg** (100.0% isolated ownership) | Magnitude: 2114.1
- `test/SILOptimizer/moveonly_objectchecker_diagnostics.swift` -> **Aidan Hall** (100.0% isolated ownership) | Magnitude: 2079.48
- `lib/Sema/CSBindings.cpp` -> **Slava Pestov** (82.1% isolated ownership) | Magnitude: 1819.08

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `stdlib/private/StdlibUnittest/StdlibUnittest.swift` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 78.7197%)
- `include/swift/Basic/LangOptions.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 65.7035%)
- `include/swift/IRGen/Linking.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 89.3047%)
- `include/swift/Parse/IDEInspectionCallbacks.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 75.8469%)
- `include/swift/SILOptimizer/Utils/InstOptUtils.h` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `stdlib/include/llvm/ADT/SmallVector.h` -> **Severity: 2.465** (Embedded: 0.0336 * Error Risk: 73.4319%)
- `stdlib/include/llvm/Support/MemAlloc.h` -> **Severity: 2.315** (Embedded: 0.0255 * Error Risk: 90.7207%)
- `stdlib/include/llvm/ADT/Hashing.h` -> **Severity: 2.165** (Embedded: 0.0313 * Error Risk: 69.2506%)
- `stdlib/include/llvm/Support/PointerLikeTypeTraits.h` -> **Severity: 2.04** (Embedded: 0.0214 * Error Risk: 95.2574%)
- `stdlib/include/llvm/Support/Allocator.h` -> **Severity: 1.92** (Embedded: 0.0208 * Error Risk: 92.1901%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `stdlib/private/StdlibUnittest/StdlibUnittest.swift` -> **Severity: 2244.753** (Blast Radius: 26.174 * Doc Risk: 85.7627%)
- `stdlib/private/SwiftPrivateLibcExtras/SwiftPrivateLibcExtras.swift` -> **Severity: 711.546** (Blast Radius: 7.827 * Doc Risk: 90.9091%)
- `stdlib/private/SwiftPrivate/SwiftPrivate.swift` -> **Severity: 594.139** (Blast Radius: 11.034 * Doc Risk: 53.8462%)
- `stdlib/private/SwiftPrivateThreadExtras/SwiftPrivateThreadExtras.swift` -> **Severity: 418.08** (Blast Radius: 7.839 * Doc Risk: 53.3333%)
- `benchmark/utils/TestsUtils.swift` -> **Severity: 395.424** (Blast Radius: 4.506 * Doc Risk: 87.7551%)

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
