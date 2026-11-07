# ARCHITECTURAL_BRIEF: swift
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/apple/swift` |
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
- **Scope:** 26522 analyzed artifact(s), 2117877 LOC.
- **Load-bearing artifact:** `stdlib/public/core/Assert.swift` -- 1021 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `benchmark/utils/main.swift` -- pulls in 197 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Sema/CSSimplify.cpp` at magnitude 12506.56 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 26522 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3785 |
| Total LOC | 2117877 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5943 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1437 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.5511 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 624 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SWIFT | 21431 | 878134 | 80.8% |
| CPP | 3364 | 1134111 | 12.7% |
| OBJECTIVE-C | 471 | 16365 | 1.8% |
| PLAINTEXT | 466 | 6 | 1.8% |
| PYTHON | 286 | 35645 | 1.1% |
| MAKEFILE | 151 | 32295 | 0.6% |
| JSON | 97 | 4177 | 0.4% |
| MARKDOWN | 87 | 0 | 0.3% |
| C | 64 | 2925 | 0.2% |
| SHELL | 30 | 3384 | 0.1% |
| YAML | 28 | 1141 | 0.1% |
| YACC | 18 | 1810 | 0.1% |
| XML | 12 | 0 | 0.0% |
| ASSEMBLY | 5 | 486 | 0.0% |
| TD | 4 | 3293 | 0.0% |
| BATCH | 4 | 89 | 0.0% |
| POWERSHELL | 2 | 3910 | 0.0% |
| RUBY | 1 | 87 | 0.0% |
| JAVASCRIPT | 1 | 19 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 5 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 26515 |
| cp1252 | cp1252-fallback | 3 |
| latin-1 | latin-1-fallback | 2 |
| utf-8 | bom | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Declarative / Non-Code 13%, Interface Declarations Files 11%, Parameter Forwarders Files 10%, Generic / Templated Code Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 25964 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 555 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3785*

**Composition by Extension & Reason:**
- `.sil`: 1293x Excluded (Unsupported Extension: '.sil'), 2x Unsupported Format (.sil)
- `.modulemap`: 243x Excluded (Unsupported Extension: '.modulemap'), 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Unsupported Format (.modulemap)
- `.swift`: 48x Excluded (Machine-Generated Source Code Signature: 85 LOC), 25x Excluded (Machine-Generated Source Code Signature: 101 LOC), 25x Excluded (Machine-Generated Source Code Signature: 90 LOC)
- `.expected`: 306x Excluded (Unsupported Extension: '.expected'), 3x Unsupported Format (.expected)
- `.gyb`: 252x Unsupported Format (.gyb), 28x Excluded (Unsupported Extension: '.gyb')
- `no_extension`: 105x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 41x Unsupported Format (.undeterminable), 36x Excluded (Unsupported Extension: '.swiftoverlay')
- `.cmake`: 178x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 273 LOC), 1x Excluded (Machine-Generated Source Code Signature: 219 LOC)
- `.h`: 139x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Embedded Hex Payload: 16950 hex tokens in 1728 LOC)
- `.md`: 104x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 104 LOC), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `.response`: 100x Excluded (Unsupported Extension: '.response')
- `.apinotes`: 49x Excluded (Unsupported Extension: '.apinotes'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 53x Excluded (Unsupported Extension: '.test'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 46x Excluded (Unsupported Extension: '.cfg'), 2x Unsupported Format (.cfg)
- `.test-sh`: 41x Excluded (Unsupported Extension: '.test-sh')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 11.7 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.7 | 96.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 55370 | 3925 | 2 | `lib/AST/Decl.cpp` |
| cleanup | 926 | 347 | 0 | `unittests/SourceKit/SwiftLang/EditingTest.cpp` |
| guards | 135739 | 6655 | 7 | `include/swift/SIL/SILInstruction.h` |
| danger | 18692 | 2662 | 1 | `lib/AST/ASTVerifier.cpp` |
| concurrency | 23335 | 1710 | 0 | `test/Concurrency/transfernonsendable.swift` |
| connectivity | 76340 | 8379 | 6 | `stdlib/private/StdlibCollectionUnittest/MinimalCollections.swift` |
| io | 3224 | 367 | 0 | `unittests/Basic/ManglingTestData.def` |
| crypto | 2 | 2 | 0 | `utils/bug_reducer/bug_reducer/subprocess_utils.py` |
| ipc | 362 | 94 | 0 | `test/Inputs/clang-importer-sdk/usr/include/Foundation.h` |
| time | 173 | 72 | 0 | `stdlib/public/Concurrency/Clock.cpp` |
| serialization | 108 | 42 | 0 | `test/Interpreter/SDK/check_class_for_archiving.swift` |
| regex | 364 | 86 | 0 | `utils/analyze_code_size.py` |
| events | 1821 | 378 | 0 | `validation-test/StdlibUnittest/AtomicInt.swift` |
| tests | 5492 | 232 | 0 | `utils/build_swift/tests/build_swift/test_shell.py` |
| docs | 170910 | 3528 | 3 | `include/swift/AST/Decl.h` |
| debt | 36771 | 5799 | 3 | `utils/bug_reducer/tests/testfuncbugreducer_testbasic.swift` |
| mutation | 349045 | 14077 | 22 | `lib/Sema/CSSimplify.cpp` |
| dead_code | 63034 | 10580 | 4 | `test/Runtime/null_vtable_entry_ptrauth.swift` |
| credential | 547 | 189 | 0 | `test/SILGen/objc_async_from_swift.swift` |
| threat | 333 | 53 | 0 | `test/stdlib/StringIndex.swift` |
| ml_ai | 10276 | 1186 | 0 | `test/AutoDiff/Sema/derivative_attr_type_checking.swift` |
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

1. **Assert.swift** (`stdlib/public/core/Assert.swift`) — 1021 inbound connections
2. **Assertions.h** (`include/swift/Basic/Assertions.h`) — 741 inbound connections
3. **Decl.h** (`include/swift/AST/Decl.h`) — 338 inbound connections
4. **ASTContext.h** (`include/swift/AST/ASTContext.h`) — 313 inbound connections
5. **Types.h** (`include/swift/AST/Types.h`) — 284 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.swift** (`benchmark/utils/main.swift`) — 197 outbound dependencies
2. **SwiftMusl.h** (`stdlib/public/Platform/SwiftMusl.h`) — 175 outbound dependencies
3. **SwiftAndroidNDK.h** (`stdlib/public/Platform/SwiftAndroidNDK.h`) — 123 outbound dependencies
4. **ClangImporter.cpp** (`lib/ClangImporter/ClangImporter.cpp`) — 105 outbound dependencies
5. **diags-with-many-imports.swift** (`test/ClangImporter/diags-with-many-imports.swift`) — 100 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `SILParser::parseSpecificSILInstruction` **(Many-Argument Workhorses)** (@ `lib/SIL/Parser/ParseSIL.cpp`) -> Impact: **3850.2** | LOC: 4206
- `NodePrinter::print` **(Many-Argument Workhorses)** (@ `lib/Demangling/NodePrinter.cpp`) -> Impact: **1400.5** | LOC: 2130
- `SILDeserializer::readSILInstruction` **(Many-Argument Workhorses)** (@ `lib/Serialization/DeserializeSIL.cpp`) -> Impact: **1371.7** | LOC: 2525
- `ConstraintSystem::repairFailures` **(Many-Argument Workhorses)** (@ `lib/Sema/CSSimplify.cpp`) -> Impact: **1365.5** | LOC: 1804
  * *Intent:* /// Attempt to repair typing failures and record fixes if needed. /// \return true if at least some of the failures has been repaired /// successfully...
- `parseDeclSILOptional` **(Many-Argument Workhorses)** (@ `lib/SIL/Parser/ParseSIL.cpp`) -> Impact: **1203.0** | LOC: 338
- `foo` **(Compute Cores)** (@ `test/SourceKit/Misc/parser-cutoff.swift`) -> Impact: **1155.3** | LOC: 789
- `foo` **(Compute Cores)** (@ `validation-test/compiler_crashers_fixed/parser-cutoff.swift`) -> Impact: **1155.3** | LOC: 789
- `ConstraintSystem::matchTypes` **(Many-Argument Workhorses)** (@ `lib/Sema/CSSimplify.cpp`) -> Impact: **1099.0** | LOC: 1355
- `Parser::parseNewDeclAttribute` **(Many-Argument Workhorses)** (@ `lib/Parse/ParseDecl.cpp`) -> Impact: **888.0** | LOC: 1526
- `diagSyntacticUseRestrictions` **(Many-Argument Workhorses)** (@ `lib/Sema/MiscDiagnostics.cpp`) -> Impact: **842.6** | LOC: 1423
  * *Intent:* /// limitations. /// - "&" (aka InOutExpressions) may only exist directly in function call /// argument lists. /// - 'self.init' and 'super.init' cann...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Sema` | 107 | 113114.38 | 25.0% | 54.26% |
| `validation-test/compiler_crashers_fixed` | 6334 | 75486.48 | 1.61% | 7.96% |
| `lib/AST` | 114 | 67198.72 | 25.58% | 81.11% |
| `lib/IRGen` | 169 | 63765.72 | 12.13% | 40.28% |
| `lib/SILGen` | 71 | 36612.72 | 17.32% | 49.52% |
| `stdlib/public/core` | 226 | 32949.92 | 12.3% | 60.16% |
| `test/Concurrency` | 282 | 27612.8 | 13.59% | 0.0% |
| `test/SILOptimizer` | 558 | 26832.84 | 4.62% | 0.0% |
| `include/swift/AST` | 245 | 25806.04 | 3.53% | 15.12% |
| `lib/ClangImporter` | 41 | 25294.04 | 24.23% | 55.16% |

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
- **Binary Anomalies (X-Ray):** `77` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `35706` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Sema/CSSimplify.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.691)
- **Top Global Matches:** file_cluster_8: 7.691, file_cluster_6: 11.438, file_cluster_4: 19.628
- **Magnitude:** 12506.56 | **LOC:** 16663 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 32.2%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 0.035; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.7%)
- **Documentation Coverage:** 83.5897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ConstraintSystem::repairFailures` **(Many-Argument Workhorses)** (Impact: 1365.5)
    * *Intent:* /// Attempt to repair typing failures and record fixes if needed. /// \return true if at least some ...
  * `ConstraintSystem::matchTypes` **(Many-Argument Workhorses)** (Impact: 1099.0)
  * `ConstraintSystem::simplifyFixConstraint` **(Many-Argument Workhorses)** (Impact: 539.7)
  * `matchCallArgumentsImpl` **(Many-Argument Workhorses)** (Impact: 522.4)
  * `performMemberLookup` **(Many-Argument Workhorses)** (Impact: 508.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 593 instances
* *State Mutation (weighted view):* 1824
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3772`, `structural_boundaries: 2913`, `args: 862`, `func_start: 184`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 638`, `dead_code: 11`, `planned_debt: 18`, `fragile_debt: 59`, `unreferenced_by_name: 97`
* *Architecture:* `api: 3`, `import: 37`
* *Defense:* `safety: 116`, `doc: 152`, `immutability_locks: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.015388
  * `Imports (Out-Degree: 70):` CSDiagnostics.h, OpenedExistentials.h, TypeCheckConcurrency.h, TypeCheckEffects.h, TypeChecker.h, ArrayRef.h, SetVector.h, Compiler.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `lib/SIL/Parser/ParseSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_6: 7.059, file_cluster_8: 13.006, file_cluster_4: 13.167
- **Magnitude:** 9502.14 | **LOC:** 9066 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 18.8%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **38**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.6%), Guard Balance (formerly Safety Score) (62.5%)
- **Documentation Coverage:** 52.381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILParser::parseSpecificSILInstruction` **(Many-Argument Workhorses)** (Impact: 3850.2)
  * `parseDeclSILOptional` **(Many-Argument Workhorses)** (Impact: 1203.0)
  * `SILParser::parseKeyPathPatternComponent` **(Many-Argument Workhorses)** (Impact: 319.9)
  * `SILParser::parseCallInstruction` **(Many-Argument Workhorses)** (Impact: 183.6)
  * `parseSILWitnessTableEntry` **(Many-Argument Workhorses)** (Impact: 141.4)
    * *Intent:* /// Parser a single SIL wtable entry and add it to either \p witnessEntries /// or \c conditionalCon...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 684 instances
* *State Mutation (weighted view):* 2096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2637`, `structural_boundaries: 1163`, `args: 1404`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `state_mutation: 728`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 12`, `unreferenced_by_name: 61`
* *Architecture:* `api: 1`, `import: 44`
* *Defense:* `safety: 78`, `doc: 230`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.014001
  * `Imports (Out-Degree: 78):` SILParser.h, SILParserFunctionBuilder.h, SILParserState.h, StringSwitch.h, CommandLine.h, SaveAndRestore.h, ASTWalker.h, ConformanceLookup.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lib/Parse/ParseDecl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.71)
- **Top Global Matches:** file_cluster_8: 7.71, file_cluster_6: 18.157, file_cluster_3: 19.536
- **Magnitude:** 7405.2 | **LOC:** 10979 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 26.9%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **41**; blast radius 0.036; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.6%), Guard Balance (formerly Safety Score) (58.5%)
- **Documentation Coverage:** 65.8385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Parser::parseNewDeclAttribute` **(Many-Argument Workhorses)** (Impact: 888.0)
  * `Parser::parseDecl` **(Many-Argument Workhorses)** (Impact: 323.9)
    * *Intent:* /// /// \verbatim /// decl: /// decl-typealias /// decl-extension /// decl-let /// decl-var /// decl...
  * `Parser::parseTypeAttribute` **(Many-Argument Workhorses)** (Impact: 251.9)
    * *Intent:* /// \verbatim /// attribute-type: /// 'noreturn' /// \endverbatim /// /// \param justChecking - if t...
  * `Parser::parseDeclVar` **(Many-Argument Workhorses)** (Impact: 179.9)
    * *Intent:* /// Parse a 'var', 'let', or 'inout' declaration, doing no token skipping on error.
  * `Parser::parseExtendedAvailabilitySpecList` **(Many-Argument Workhorses)** (Impact: 132.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 540 instances
* *State Mutation (weighted view):* 1684
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2386`, `structural_boundaries: 1127`, `args: 1376`, `func_start: 138`, `class_start: 5`
* *Risk/State:* `state_mutation: 604`, `dead_code: 2`, `planned_debt: 14`, `fragile_debt: 7`, `unreferenced_by_name: 91`
* *Architecture:* `api: 1`, `import: 47`
* *Defense:* `safety: 100`, `doc: 387`, `immutability_locks: 46`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.036
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.015146
  * `Imports (Out-Degree: 76):` algorithm, initializer_list, PointerUnion.h, StringSwitch.h, Twine.h, Compiler.h, MemoryBuffer.h, Path.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/AST/Decl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.681)
- **Top Global Matches:** file_cluster_4: 7.681, file_cluster_15: 9.345, file_cluster_16: 10.632
- **Magnitude:** 6899.38 | **LOC:** 13528 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 19.5%
- **Blast Radius:** changing it is visible to **94** in-repo importer(s); it depends on **71**; blast radius 0.197; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.8%), Mutation Surface (formerly State Flux) (55.3%)
- **Documentation Coverage:** 92.8144% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `swift::conflicting` **(Many-Argument Workhorses)** (Impact: 103.8)
  * `checkAccess` **(Many-Argument Workhorses)** (Impact: 95.6)
    * *Intent:* /// Checks if \p VD may be used from \p useDC, taking \@testable and \@_spi /// imports into account...
  * `AbstractFunctionDecl::getObjCSelector` **(Many-Argument Workhorses)** (Impact: 89.9)
  * `Decl::getAttributeInsertionLoc` **(Compute Cores)** (Impact: 72.2)
  * `MacroDecl::getIntroducedNames` **(Many-Argument Workhorses)** (Impact: 72.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 320 instances
* *State Mutation (weighted view):* 1046
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2785`, `structural_boundaries: 3170`, `args: 1066`, `func_start: 796`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 406`, `planned_debt: 7`, `fragile_debt: 31`, `duplicate_logic: 2`, `unreferenced_by_name: 676`
* *Architecture:* `api: 2`, `import: 93`
* *Defense:* `safety: 222`, `doc: 195`, `immutability_locks: 770`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.025461
  * `Imports (Out-Degree: 111):` algorithm, Attr.h, DeclObjC.h, CharInfo.h, Module.h, TargetInfo.h, MacroInfo.h, DenseMap.h...
  * `Imported By (In-Degree: 94):` (Excluded from Brief to save tokens)

### `lib/ClangImporter/ImportDecl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.911)
- **Top Global Matches:** file_cluster_6: 5.911, file_cluster_4: 11.505, file_cluster_8: 13.79
- **Magnitude:** 6691.06 | **LOC:** 11207 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 36.7%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **82**; blast radius 0.038; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Debt Markers (formerly Tech Debt) (83.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 75.1174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `importFunctionDecl` **(Many-Argument Workhorses)** (Impact: 270.4)
  * `getSwiftStdlibType` **(Many-Argument Workhorses)** (Impact: 254.9)
    * *Intent:* #endif /// Map a well-known C type to a swift type from the standard library. /// /// \param IsError...
  * `VisitRecordDecl` **(Compute Cores)** (Impact: 237.0)
  * `validateForeignReferenceType` **(Many-Argument Workhorses)** (Impact: 169.1)
  * `ClangImporter::Implementation::importAttributes` **(Many-Argument Workhorses)** (Impact: 163.2)
    * *Intent:* /// Import Clang attributes as Swift attributes.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 427 instances
* *State Mutation (weighted view):* 1340
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2300`, `structural_boundaries: 1796`, `args: 661`, `func_start: 210`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 486`, `planned_debt: 39`, `fragile_debt: 63`, `unreferenced_by_name: 105`
* *Architecture:* `api: 4`, `import: 82`
* *Defense:* `safety: 137`, `doc: 259`, `immutability_locks: 320`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.021169
  * `Imports (Out-Degree: 94):` CFTypeInfo.h, CXXMethodBridging.h, ClangDerivedConformances.h, ImporterImpl.h, InferredAttributes.def, MappedTypes.def, SwiftDeclSynthesizer.h, algorithm...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lib/Sema/MiscDiagnostics.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.08)
- **Top Global Matches:** file_cluster_6: 8.08, file_cluster_8: 13.141, file_cluster_4: 13.964
- **Magnitude:** 5589.34 | **LOC:** 6989 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 15.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **40**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%)
- **Documentation Coverage:** 73.5751% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `diagSyntacticUseRestrictions` **(Many-Argument Workhorses)** (Impact: 842.6)
    * *Intent:* /// limitations. /// - "&" (aka InOutExpressions) may only exist directly in function call /// argum...
  * `checkForSuspiciousBitCasts` **(Many-Argument Workhorses)** (Impact: 270.8)
  * `diagnoseUnintendedOptionalBehavior` **(Many-Argument Workhorses)** (Impact: 153.7)
  * `walkToExprPre` **(Compute Cores)** (Impact: 132.4)
  * `swift::diagnoseArgumentLabelError` **(Many-Argument Workhorses)** (Impact: 125.8)
    * *Intent:* /// Diagnose an argument labeling issue, returning true if we successfully /// diagnosed the issue.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 339 instances
* *State Mutation (weighted view):* 1035
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1483`, `structural_boundaries: 1201`, `args: 815`, `func_start: 185`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 357`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 19`
* *Architecture:* `api: 18`, `import: 40`
* *Defense:* `safety: 77`, `doc: 196`, `immutability_locks: 179`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.015366
  * `Imports (Out-Degree: 61):` MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckEmbedded.h, TypeCheckInvertible.h, TypeChecker.h, DeclObjC.h, MapVector.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/ClangImporter/ClangImporter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.514)
- **Top Global Matches:** file_cluster_4: 5.514, file_cluster_6: 9.665, file_cluster_15: 11.768
- **Magnitude:** 5509.48 | **LOC:** 9269 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **105**; blast radius 0.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Debt Markers (formerly Tech Debt) (98.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.1%), Complexity Load (formerly Cognitive Load) (59.6%)
- **Documentation Coverage:** 97.0674% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `importer::getNormalInvocationArguments` **(Many-Argument Workhorses)** (Impact: 140.4)
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
* *Structure:* `branch: 1679`, `structural_boundaries: 1697`, `args: 602`, `func_start: 341`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 506`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 52`, `duplicate_logic: 2`, `unreferenced_by_name: 221`
* *Architecture:* `api: 14`, `import: 105`
* *Defense:* `safety: 109`, `doc: 20`, `immutability_locks: 363`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.021902
  * `Imports (Out-Degree: 99):` CFTypeInfo.h, ClangDerivedConformances.h, ClangDiagnosticConsumer.h, ClangIncludePaths.h, ImporterImpl.h, SwiftDeclSynthesizer.h, algorithm, ASTContext.h...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `lib/AST/ASTPrinter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.816)
- **Top Global Matches:** file_cluster_4: 6.816, file_cluster_15: 10.488, file_cluster_16: 11.769
- **Magnitude:** 5471.56 | **LOC:** 9031 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 11.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **70**; blast radius 0.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.0%), Mutation Surface (formerly State Flux) (77.3%)
- **Documentation Coverage:** 93.4426% of unit weight undocumented
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
* *Structure:* `branch: 1956`, `structural_boundaries: 1420`, `args: 1267`, `func_start: 473`, `class_start: 7`
* *Risk/State:* `state_mutation: 288`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 25`, `unreferenced_by_name: 322`
* *Architecture:* `api: 4`, `import: 72`
* *Defense:* `safety: 35`, `doc: 121`, `immutability_locks: 247`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.020115
  * `Imports (Out-Degree: 85):` FeatureSet.h, algorithm, ASTContext.h, Attr.h, Decl.h, DeclObjC.h, Module.h, SourceManager.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/Sema/CSApply.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.935)
- **Top Global Matches:** file_cluster_4: 7.935, file_cluster_15: 12.346, file_cluster_6: 12.63
- **Magnitude:** 5302.82 | **LOC:** 9896 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 38.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **43**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (88.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.4%)
- **Documentation Coverage:** 73.6264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExprRewriter::coerceToType` **(Many-Argument Workhorses)** (Impact: 555.7)
  * `buildMemberRef` **(Many-Argument Workhorses)** (Impact: 186.1)
    * *Intent:* /// Build a new member reference with the given base and member.
  * `ExprRewriter::coerceCallArguments` **(Many-Argument Workhorses)** (Impact: 145.3)
  * `ExprWalker::rewriteTarget` **(Compute Cores)** (Impact: 139.0)
  * `visitObjCSelectorExpr` **(Compute Cores)** (Impact: 98.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 431 instances
* *State Mutation (weighted view):* 1375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1500`, `structural_boundaries: 1725`, `args: 567`, `func_start: 260`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 513`, `dead_code: 2`, `planned_debt: 11`, `fragile_debt: 32`, `duplicate_logic: 4`, `unreferenced_by_name: 137`
* *Architecture:* `api: 8`, `import: 44`
* *Defense:* `safety: 157`, `doc: 413`, `immutability_locks: 104`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.015456
  * `Imports (Out-Degree: 72):` CSDiagnostics.h, CodeSynthesis.h, MiscDiagnostics.h, OpenedExistentials.h, TypeCheckConcurrency.h, TypeCheckEmbedded.h, TypeCheckMacros.h, TypeCheckProtocol.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/Sema/TypeCheckConcurrency.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.539)
- **Top Global Matches:** file_cluster_6: 7.539, file_cluster_8: 10.687, file_cluster_4: 14.918
- **Magnitude:** 5295.14 | **LOC:** 9034 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 49.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **35**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (58.4%)
- **Documentation Coverage:** 59.596% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `computeActorIsolation` **(Many-Argument Workhorses)** (Impact: 197.2)
  * `checkFunctionConversion` **(Many-Argument Workhorses)** (Impact: 135.2)
    * *Intent:* /// Some function conversions synthesized by the constraint solver may not /// be correct AND the so...
  * `checkReference` **(Many-Argument Workhorses)** (Impact: 132.6)
    * *Intent:* /// Check a reference to the given declaration. /// /// \param base For a reference to a member, the...
  * `swift::tryDiagnoseExecutorConformance` **(Many-Argument Workhorses)** (Impact: 114.5)
  * `checkApply` **(Compute Cores)** (Impact: 98.5)
    * *Intent:* /// Check actor isolation for a particular application.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 253 instances
* *State Mutation (weighted view):* 770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2083`, `structural_boundaries: 1579`, `args: 353`, `func_start: 198`, `class_start: 10`
* *Risk/State:* `state_mutation: 264`, `planned_debt: 3`, `fragile_debt: 28`, `unreferenced_by_name: 73`
* *Architecture:* `api: 6`, `import: 35`
* *Defense:* `safety: 115`, `doc: 298`, `immutability_locks: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.017605
  * `Imports (Out-Degree: 64):` MiscDiagnostics.h, NonisolatedNonsendingByDefaultMigration.h, TypeCheckConcurrency.h, TypeCheckDistributed.h, TypeCheckInvertible.h, TypeCheckProtocol.h, TypeCheckType.h, TypeChecker.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/SILGen/SILGenApply.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.657)
- **Top Global Matches:** file_cluster_4: 6.657, file_cluster_15: 9.998, file_cluster_16: 11.284
- **Magnitude:** 4827.16 | **LOC:** 8479 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **45**; blast radius 0.032; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.2%)
- **Documentation Coverage:** 80.7074% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILGenFunction::emitApply` **(Many-Argument Workhorses)** (Impact: 290.8)
    * *Intent:* //===----------------------------------------------------------------------===// // Top Level Entryp...
  * `emitRawApply` **(Many-Argument Workhorses)** (Impact: 140.5)
    * *Intent:* /// Emit a raw apply operation, performing no additional lowering of /// either the arguments or the...
  * `SILGenFunction::findStorageReferenceExprForMoveOnly` **(Many-Argument Workhorses)** (Impact: 90.6)
  * `SILGenFunction::tryEmitAddressableParameterAsAddress` **(Many-Argument Workhorses)** (Impact: 81.0)
  * `emitEnumElementPayloads` **(Many-Argument Workhorses)** (Impact: 81.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 402 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1183`, `structural_boundaries: 1171`, `args: 838`, `func_start: 306`, `class_start: 24`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 486`, `dead_code: 1`, `planned_debt: 31`, `fragile_debt: 15`, `unreferenced_by_name: 95`
* *Architecture:* `api: 18`, `import: 45`
* *Defense:* `safety: 188`, `doc: 224`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.032
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.01291
  * `Imports (Out-Degree: 81):` ArgumentScope.h, ArgumentSource.h, Callee.h, Conversion.h, ExecutorBreadcrumb.h, FormalEvaluation.h, Initialization.h, LValue.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `lib/Sema/TypeCheckAttr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.915)
- **Top Global Matches:** file_cluster_6: 5.915, file_cluster_4: 11.036, file_cluster_8: 14.359
- **Magnitude:** 4689.54 | **LOC:** 9168 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 16.1%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **44**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.9%), Debt Markers (formerly Tech Debt) (82.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.4%)
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
* *Structure:* `branch: 1838`, `structural_boundaries: 1701`, `args: 925`, `func_start: 224`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 276`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 22`, `unreferenced_by_name: 145`
* *Architecture:* `api: 2`, `import: 44`
* *Defense:* `safety: 44`, `doc: 135`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.017692
  * `Imports (Out-Degree: 82):` MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckDistributed.h, TypeCheckEmbedded.h, TypeCheckMacros.h, TypeCheckObjC.h, TypeCheckType.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/Sema/TypeCheckProtocol.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.644)
- **Top Global Matches:** file_cluster_8: 8.644, file_cluster_6: 9.418, file_cluster_4: 17.421
- **Magnitude:** 4663.68 | **LOC:** 7702 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 19.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **56**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.0%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 56.1151% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TypeChecker::checkConformancesInContext` **(Compute Cores)** (Impact: 235.1)
  * `diagnoseMatch` **(Many-Argument Workhorses)** (Impact: 217.6)
    * *Intent:* /// Diagnose a requirement match, describing what went wrong (or not).
  * `swift::matchWitness` **(Many-Argument Workhorses)** (Impact: 158.4)
  * `WitnessChecker::findBestWitness` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `checkIndividualConformance` **(Compute Cores)** (Impact: 126.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1652`, `structural_boundaries: 1241`, `args: 462`, `func_start: 135`, `class_start: 12`
* *Risk/State:* `state_mutation: 319`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 32`, `unreferenced_by_name: 36`
* *Architecture:* `api: 4`, `import: 56`
* *Defense:* `safety: 76`, `doc: 154`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.022064
  * `Imports (Out-Degree: 94):` DerivedConformance.h, MiscDiagnostics.h, OpenedExistentials.h, TypeAccessScopeChecker.h, TypeCheckAccess.h, TypeCheckAvailability.h, TypeCheckBitwise.h, TypeCheckConcurrency.h...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `lib/Frontend/CompilerInvocation.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.626)
- **Top Global Matches:** file_cluster_6: 5.626, file_cluster_4: 9.668, file_cluster_8: 15.424
- **Magnitude:** 4605.48 | **LOC:** 4569 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseIRGenArgs` **(Many-Argument Workhorses)** (Impact: 624.2)
  * `ParseLangArgs` **(Many-Argument Workhorses)** (Impact: 524.7)
  * `ParseSILArgs` **(Many-Argument Workhorses)** (Impact: 319.4)
  * `ParseSearchPathArgs` **(Many-Argument Workhorses)** (Impact: 189.8)
  * `ParseEnabledFeatureArgs` **(Many-Argument Workhorses)** (Impact: 166.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 542 instances
* *State Mutation (weighted view):* 1770
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 953`, `structural_boundaries: 340`, `args: 1085`, `func_start: 62`, `class_start: 2`
* *Risk/State:* `state_mutation: 686`, `planned_debt: 4`, `fragile_debt: 14`, `unreferenced_by_name: 18`
* *Architecture:* `import: 32`
* *Defense:* `safety: 44`, `doc: 17`, `immutability_locks: 171`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.027
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000181
  * `Imports (Out-Degree: 37):` ArgsToFrontendOptionsConverter.h, Driver.h, STLExtras.h, Arg.h, ArgList.h, Option.h, FileSystem.h, LineIterator.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Sema/TypeCheckType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.314)
- **Top Global Matches:** file_cluster_6: 6.314, file_cluster_8: 12.252, file_cluster_4: 12.918
- **Magnitude:** 4600.18 | **LOC:** 7468 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 14.7%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **59**; blast radius 0.033; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Debt Markers (formerly Tech Debt) (80.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 82.5843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TypeResolver::resolveASTFunctionType` **(Many-Argument Workhorses)** (Impact: 219.2)
  * `TypeResolver::resolveAttributedType` **(Many-Argument Workhorses)** (Impact: 196.0)
  * `TypeResolver::resolveSILFunctionType` **(Many-Argument Workhorses)** (Impact: 145.4)
  * `TypeResolver::resolveType` **(Many-Argument Workhorses)** (Impact: 142.0)
  * `TypeResolver::resolveImplicitlyUnwrappedOptionalType` **(Many-Argument Workhorses)** (Impact: 108.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1517`, `structural_boundaries: 1226`, `args: 509`, `func_start: 166`, `class_start: 9`
* *Risk/State:* `state_mutation: 349`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 34`, `unreferenced_by_name: 86`
* *Architecture:* `api: 9`, `import: 60`
* *Defense:* `safety: 66`, `doc: 106`, `immutability_locks: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.033
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.016087
  * `Imports (Out-Degree: 81):` LiteralExpressionFolding.h, MiscDiagnostics.h, NonisolatedNonsendingByDefaultMigration.h, TypeCheckAccess.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckInvertible.h, TypeCheckProtocol.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `lib/Sema/CSDiagnostics.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.688)
- **Top Global Matches:** file_cluster_4: 7.688, file_cluster_6: 8.669, file_cluster_15: 14.549
- **Magnitude:** 4535.96 | **LOC:** 9761 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 21.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **39**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.2%), Mutation Surface (formerly State Flux) (97.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.2%)
- **Documentation Coverage:** 95.6811% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ContextualFailure::diagnoseAsError` **(I/O & Config Routines)** (Impact: 93.8)
  * `AllowTypeOrInstanceMemberFailure::diagnoseAsError` **(Compute Cores)** (Impact: 86.8)
  * `MissingMemberFailure::diagnoseUnsafeCxxMethod` **(Many-Argument Workhorses)** (Impact: 86.5)
  * `ContextualFailure::getDiagnosticFor` **(Compute Cores)** (Impact: 80.5)
  * `GenericArgumentsMismatchFailure::diagnoseAsError` **(I/O & Config Routines)** (Impact: 73.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 390 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2038`, `structural_boundaries: 2288`, `args: 416`, `func_start: 299`, `class_start: 5`
* *Risk/State:* `state_mutation: 399`, `dead_code: 9`, `planned_debt: 8`, `fragile_debt: 15`, `duplicate_logic: 3`, `unreferenced_by_name: 259`
* *Architecture:* `api: 2`, `import: 39`
* *Defense:* `safety: 68`, `doc: 14`, `immutability_locks: 211`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.013122
  * `Imports (Out-Degree: 67):` CSDiagnostics.h, MiscDiagnostics.h, TypeCheckAvailability.h, TypeCheckConcurrency.h, TypeCheckProtocol.h, TypeCheckType.h, TypoCorrection.h, ArrayRef.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/Serialization/DeserializeSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.618)
- **Top Global Matches:** file_cluster_6: 7.618, file_cluster_4: 8.303, file_cluster_15: 15.801
- **Magnitude:** 4353.62 | **LOC:** 5555 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (80.0%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 84.6939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILDeserializer::readSILInstruction` **(Many-Argument Workhorses)** (Impact: 1371.7)
  * `SILDeserializer::readSILFunctionChecked` **(Many-Argument Workhorses)** (Impact: 457.8)
  * `SILDeserializer::SILDeserializer` **(Many-Argument Workhorses)** (Impact: 144.1)
  * `SILDeserializer::readGlobalVar` **(Many-Argument Workhorses)** (Impact: 96.6)
  * `SILDeserializer::readWitnessTableEntries` **(Many-Argument Workhorses)** (Impact: 54.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 426 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1215`, `structural_boundaries: 706`, `args: 1141`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 505`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 62`
* *Architecture:* `api: 2`, `import: 31`
* *Defense:* `safety: 183`, `doc: 36`, `immutability_locks: 22`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.010743
  * `Imports (Out-Degree: 53):` BCReadingExtras.h, DeserializationErrors.h, DeserializeSIL.h, ModuleFile.h, SILFormat.h, SILSerializationFunctionBuilder.h, SerializationFormat.h, Statistic.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Serialization/Deserialization.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.494)
- **Top Global Matches:** file_cluster_4: 6.494, file_cluster_6: 10.634, file_cluster_15: 12.268
- **Magnitude:** 4295.94 | **LOC:** 9639 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 21.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **48**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.9%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 82.7434% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ModuleFile::resolveCrossReference` **(Many-Argument Workhorses)** (Impact: 365.6)
  * `DeclDeserializer::deserializeDeclCommon` **(I/O & Config Routines)** (Impact: 193.9)
  * `ModuleFile::finishNormalConformance` **(Many-Argument Workhorses)** (Impact: 134.7)
  * `deserializeAnyFunc` **(Many-Argument Workhorses)** (Impact: 115.7)
  * `filterValues` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /// Remove values from \p values that don't match the expected type or module. /// /// Any of \p exp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 418 instances
* *State Mutation (weighted view):* 1304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1489`, `structural_boundaries: 1516`, `args: 871`, `func_start: 196`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 468`, `planned_debt: 5`, `fragile_debt: 22`, `unreferenced_by_name: 122`
* *Architecture:* `api: 7`, `import: 50`
* *Defense:* `safety: 129`, `doc: 84`, `immutability_locks: 77`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.009916
  * `Imports (Out-Degree: 77):` BCReadingExtras.h, DeclTypeRecordNodes.def, DeserializationErrors.h, ModuleFile.h, ModuleFormat.h, Attr.h, DeclTemplate.h, AttributeCommonInfo.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/IRGen/GenCall.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.874)
- **Top Global Matches:** file_cluster_4: 5.874, file_cluster_15: 10.979, file_cluster_6: 11.1
- **Magnitude:** 4272.28 | **LOC:** 7072 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **58**; blast radius 0.037; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (93.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.6%)
- **Documentation Coverage:** 88.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CallEmission::externalizeArguments` **(Many-Argument Workhorses)** (Impact: 131.1)
  * `NativeConventionSchema::mapIntoNative` **(Many-Argument Workhorses)** (Impact: 119.3)
  * `SignatureExpansion::expandExternalSignatureTypes` **(Compute Cores)** (Impact: 97.7)
    * *Intent:* /// Expand the result and parameter types to the appropriate LLVM IR /// types for C, C++ and Object...
  * `irgen::emitAsyncReturn` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `setArgs` **(Many-Argument Workhorses)** (Impact: 84.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1195`, `structural_boundaries: 1152`, `args: 851`, `func_start: 273`, `class_start: 9`
* *Risk/State:* `state_mutation: 494`, `dead_code: 1`, `planned_debt: 13`, `fragile_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 154`
* *Architecture:* `api: 5`, `import: 59`
* *Defense:* `safety: 241`, `doc: 67`, `immutability_locks: 117`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.037
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.012819
  * `Imports (Out-Degree: 60):` CallEmission.h, ConstantBuilder.h, EntryPointArgumentEmission.h, Explosion.h, GenCall.h, GenCoro.h, GenFunc.h, GenHeap.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `lib/IRGen/IRGenSIL.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_4: 7.625, file_cluster_15: 8.145, file_cluster_16: 9.861
- **Magnitude:** 4215.58 | **LOC:** 8722 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 35.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **87**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Mutation Surface (formerly State Flux) (95.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.9%)
- **Documentation Coverage:** 89.4988% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitEntryPointArgumentsNativeCC` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /// Emit entry point arguments for a SILFunction with the Swift calling /// convention.
  * `IRGenSILFunction::visitFullApplySite` **(Compute Cores)** (Impact: 106.6)
  * `IRGenSILFunction::emitDebugInfoAfterAllocStack` **(Many-Argument Workhorses)** (Impact: 73.2)
    * *Intent:* /// Do not instantiate type metadata in here, since this may allocate on-stack /// packs which will ...
  * `isSafeForMemCpyPeephole` **(Many-Argument Workhorses)** (Impact: 71.6)
  * `LoweredValue::getCallee` **(Many-Argument Workhorses)** (Impact: 70.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 298 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 945
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1208`, `structural_boundaries: 1614`, `args: 957`, `func_start: 419`, `class_start: 16`
* *Risk/State:* `state_mutation: 349`, `dead_code: 4`, `planned_debt: 17`, `fragile_debt: 20`, `duplicate_logic: 20`, `unreferenced_by_name: 241`
* *Architecture:* `api: 8`, `import: 89`
* *Defense:* `safety: 177`, `doc: 148`, `immutability_locks: 111`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.012813
  * `Imports (Out-Degree: 92):` CallEmission.h, EntryPointArgumentEmission.h, Explosion.h, GenArchetype.h, GenBorrow.h, GenBuiltin.h, GenCall.h, GenCast.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/SILGen/SILGenExpr.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.264)
- **Top Global Matches:** file_cluster_4: 7.264, file_cluster_15: 8.638, file_cluster_16: 10.182
- **Magnitude:** 4058.0 | **LOC:** 7793 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 36.7%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **54**; blast radius 0.041; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Debt Markers (formerly Tech Debt) (91.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.7%)
- **Documentation Coverage:** 89.4161% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILGenModule::emitKeyPathComponentForDecl` **(Many-Argument Workhorses)** (Impact: 271.4)
  * `RValueEmitter::visitKeyPathExpr` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `SILGenFunction::emitOptionalEvaluation` **(Many-Argument Workhorses)** (Impact: 91.0)
  * `convertFunctionRepresentation` **(Many-Argument Workhorses)** (Impact: 87.5)
    * *Intent:* // Change the representation without changing the signature or // abstraction level.
  * `getOrCreateKeyPathEqualsAndHash` **(Many-Argument Workhorses)** (Impact: 78.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 327 instances
* *State Mutation (weighted view):* 1054
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 969`, `structural_boundaries: 1221`, `args: 1232`, `func_start: 272`, `class_start: 12`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 400`, `planned_debt: 12`, `fragile_debt: 17`, `unreferenced_by_name: 148`
* *Architecture:* `api: 9`, `import: 54`
* *Defense:* `safety: 192`, `doc: 110`, `immutability_locks: 50`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.01294
  * `Imports (Out-Degree: 91):` ArgumentScope.h, ArgumentSource.h, Callee.h, Condition.h, Conversion.h, Initialization.h, LValue.h, RValue.h...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `lib/AST/ASTContext.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.361)
- **Top Global Matches:** file_cluster_4: 8.361, file_cluster_12: 8.493, file_cluster_15: 8.937
- **Magnitude:** 4003.26 | **LOC:** 7562 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **248** in-repo importer(s); it depends on **92**; blast radius 0.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Mutation Surface (formerly State Flux) (89.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.0%)
- **Documentation Coverage:** 89.2583% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SILFunctionType::SILFunctionType` **(Many-Argument Workhorses)** (Impact: 249.0)
  * `ASTContext::canImportModuleImpl` **(Many-Argument Workhorses)** (Impact: 100.5)
  * `swift::computeSelfParam` **(Many-Argument Workhorses)** (Impact: 94.2)
  * `SILFunctionType::get` **(Many-Argument Workhorses)** (Impact: 87.5)
  * `ASTContext::getProtocol` **(Compute Cores)** (Impact: 87.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 245 instances
* *Memory Alloc (weighted view):* 94
* *State Mutation (weighted view):* 794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1174`, `structural_boundaries: 1497`, `args: 811`, `func_start: 376`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 304`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 13`, `unreferenced_by_name: 272`
* *Architecture:* `import: 102`
* *Defense:* `safety: 187`, `doc: 203`, `immutability_locks: 288`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.727
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.028393
  * `Imports (Out-Degree: 113):` AbstractConformance.h, ClangTypeConverter.h, ForeignRepresentationInfo.h, RewriteContext.h, SubstitutionMapStorage.h, algorithm, Type.h, dlfcn.h...
  * `Imported By (In-Degree: 248):` (Excluded from Brief to save tokens)

### `lib/IRGen/GenEnum.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.129)
- **Top Global Matches:** file_cluster_15: 7.129, file_cluster_16: 8.776, file_cluster_4: 9.083
- **Magnitude:** 3947.7 | **LOC:** 7879 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **35**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.5%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.2%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 88.5167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EnumImplStrategy::get` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `emitIndirectInitialize` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `MultiPayloadEnumImplStrategy::completeFixedLayout` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `emitValueSwitch` **(Many-Argument Workhorses)** (Impact: 77.7)
  * `MultiPayloadEnumImplStrategy` **(Many-Argument Workhorses)** (Impact: 66.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 783
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 845`, `structural_boundaries: 1150`, `args: 1432`, `func_start: 418`, `class_start: 17`
* *Risk/State:* `state_mutation: 301`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 15`, `duplicate_logic: 22`, `unreferenced_by_name: 49`
* *Architecture:* `api: 25`, `import: 35`
* *Defense:* `safety: 379`, `doc: 115`, `immutability_locks: 417`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.012835
  * `Imports (Out-Degree: 47):` BitPatternBuilder.h, ClassTypeInfo.h, GenDecl.h, GenEnum.h, GenMeta.h, GenProto.h, GenType.h, IRGenDebugInfo.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `stdlib/public/runtime/Metadata.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.995)
- **Top Global Matches:** file_cluster_12: 7.995, file_cluster_15: 10.067, file_cluster_4: 10.458
- **Magnitude:** 3792.0 | **LOC:** 8514 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **44**; blast radius 0.045; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Mutation Surface (formerly State Flux) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%)
- **Documentation Coverage:** 82.4034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TupleCacheEntry::tryInitialize` **(Many-Argument Workhorses)** (Impact: 84.9)
  * `swift::_swift_addRefCountStringForMetatype` **(Many-Argument Workhorses)** (Impact: 73.7)
  * `findAnyTransitiveMetadata` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* /// Search all the metadata that the given type has transitive completeness /// requirements on for ...
  * `swift_cvw_initStructMetadataWithLayoutStringImpl` **(Many-Argument Workhorses)** (Impact: 42.9)
  * `_swift_initClassMetadataImpl` **(Many-Argument Workhorses)** (Impact: 42.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 300 instances
* *State Mutation (weighted view):* 1051
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 821`, `structural_boundaries: 1586`, `args: 704`, `func_start: 440`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 144`, `state_mutation: 451`, `planned_debt: 24`, `fragile_debt: 7`, `duplicate_logic: 59`, `unreferenced_by_name: 135`
* *Architecture:* `api: 28`, `import: 54`
* *Defense:* `safety: 176`, `doc: 248`, `sync_locks: 1`, `immutability_locks: 901`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.045
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.019577
  * `Imports (Out-Degree: 57):` CompatibilityOverride.h, CompatibilityOverrideIncludePath.h, BytecodeLayouts.h, ErrorObject.h, ExistentialMetadataImpl.h, GenericCacheEntry.h, MetadataCache.h, ObjCRuntimeGetImageNameFromClass.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `lib/SIL/IR/SILFunctionType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.633)
- **Top Global Matches:** file_cluster_4: 5.633, file_cluster_6: 9.803, file_cluster_15: 11.725
- **Magnitude:** 3717.42 | **LOC:** 5658 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **32**; blast radius 0.095; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.8%)
- **Documentation Coverage:** 77.4869% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSILFunctionType` **(Many-Argument Workhorses)** (Impact: 276.1)
    * *Intent:* /// reabstracted to the most general type, which means that we'd /// expect the wrong abstraction co...
  * `getAutoDiffPullbackType` **(Many-Argument Workhorses)** (Impact: 128.1)
    * *Intent:* /// Returns the pullback type for the given original function type, parameter /// indices, and resul...
  * `getNativeSILFunctionType` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `swift::buildSILFunctionThunkType` **(Many-Argument Workhorses)** (Impact: 118.8)
    * *Intent:* /// Build the type of a function transformation thunk.
  * `areABICompatibleParamsOrReturns` **(Many-Argument Workhorses)** (Impact: 118.5)
    * *Intent:* // TODO: We should compare generic signatures. Class and witness methods // allow variance in "self"...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 777
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1056`, `structural_boundaries: 909`, `args: 373`, `func_start: 189`, `class_start: 17`
* *Risk/State:* `state_mutation: 295`, `planned_debt: 14`, `fragile_debt: 14`, `duplicate_logic: 14`, `unreferenced_by_name: 39`
* *Architecture:* `api: 9`, `import: 32`
* *Defense:* `safety: 162`, `doc: 159`, `immutability_locks: 209`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.095
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.022646
  * `Imports (Out-Degree: 54):` ASTContext.h, Attr.h, DeclCXX.h, DeclObjC.h, CocoaConventions.h, CommandLine.h, Compiler.h, Debug.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `include/swift/AST/ASTVisitor.h` (CPP) | Magnitude: 30.96 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 97, indent_spaces: 87, args: 44, pointers: 29
- `test/SILOptimizer/lifetime_dependence/dependence_insertion.swift` (SWIFT) | Magnitude: 42.24 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 54, decorators: 20, args: 17
- `test/SILGen/addressor_dependence.swift` (SWIFT) | Magnitude: 6.06 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, api: 3, args: 2
- `benchmark/single-source/TaskGroups.swift` (SWIFT) | Magnitude: 35.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 12, concurrency: 7, args: 4
- `test/SILOptimizer/moveonly_modify_coroutine.swift` (SWIFT) | Magnitude: 21.04 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 50, indent_spaces: 43, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/ConstValues/FunctionTypesSyntactic.swift` (SWIFT) | Magnitude: 2.88 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 20, structural_boundaries: 6, args: 5, closures: 3
- `test/DebugInfo/async-boxed-arg.swift` (SWIFT) | Magnitude: 9.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, concurrency: 5, args: 4
- `test/stdlib/RangeReplaceableFilterCompatibility.swift` (SWIFT) | Magnitude: 18.52 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 11, comprehensions: 7, core_var_decl: 7
- `lib/IDE/AfterPoundExprCompletion.cpp` (CPP) | Magnitude: 11.36 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, args: 11, pointers: 8
- `test/embedded/concurrency-discardingtaskgroup.swift` (SWIFT) | Magnitude: 22.68 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, concurrency: 12, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/SIL/IR/SILDefaultWitnessTable.cpp` (CPP) | Magnitude: 40.72 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 46, pointers: 20, args: 15, structural_boundaries: 11
- `test/attr/accessibility_proto.swift` (SWIFT) | Magnitude: 85.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 118, indent_spaces: 70, class_start: 52, api: 51
- `lib/SILOptimizer/Mandatory/MoveOnlyBorrowToDestructureTester.cpp` (CPP) | Magnitude: 24.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 17, import: 17, pointers: 10
- `test/IRGen/trap-function.swift` (SWIFT) | Magnitude: 10.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, args: 5, func_start: 5
- `test/TBD/enum.swift` (SWIFT) | Magnitude: 13.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 15, class_start: 14, indent_spaces: 14, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `utils/update_checkout/update_checkout/commands/status.py` (PYTHON) | Magnitude: 67.04 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 21, core_var_decl: 14, design_snake_case: 14
- `include/swift/SIL/Test.h` (CPP) | Magnitude: 12.34 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 76, structural_boundaries: 41, indent_spaces: 33, pointers: 22
- `unittests/Basic/TaskQueueTest.cpp` (CPP) | Magnitude: 135.06 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 207, args: 60, test: 50, core_var_decl: 46
- `test/attr/attr_abi.swift` (SWIFT) | Magnitude: 705.82 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1247, indent_spaces: 1038, args: 837, decorators: 693
- `test/SourceKit/CodeFormat/indent-closure.swift` (SWIFT) | Magnitude: 22.86 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 22, args: 18, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `stdlib/public/core/NewtypeWrapper.swift` (SWIFT) | Magnitude: 81.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 56, args: 20, branch: 19
- `test/Concurrency/Runtime/async_task_executor_unstructured_task_ownership.swift` (SWIFT) | Magnitude: 59.5 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 19, concurrency: 13, debug_prints: 8
- `test/Concurrency/Runtime/data_race_detection_crash.swift` (SWIFT) | Magnitude: 39.96 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 26, concurrency: 15, args: 7
- `test/ConstValues/FunctionTypes.swift` (SWIFT) | Magnitude: 2.88 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: decorators: 20, structural_boundaries: 6, args: 5, closures: 3
- `stdlib/public/Concurrency/AsyncThrowingDropWhileSequence.swift` (SWIFT) | Magnitude: 131.8 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 91, doc: 73, structural_boundaries: 57, decorators: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `include/swift/SIL/SILAllocated.h` (CPP) | Magnitude: 3.66 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 10, pointers: 8, doc: 7
- `test/multifile/Inputs/objc-escape/Escaper.h` (OBJECTIVE-C) | Magnitude: 3.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, func_start: 1, class_start: 1
- `stdlib/private/StdlibUnittestFoundationExtras/UnavailableFoundationMethodThunks.mm` (OBJECTIVE-C) | Magnitude: 7.32 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 6, safety_bypasses: 3, pointers: 3, args: 2
- `test/Interop/C/struct/Inputs/noncopyable-struct.h` (CPP) | Magnitude: 1.92 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 10, args: 9, pointers: 8
- `stdlib/include/llvm/Support/AllocatorBase.h` (CPP) | Magnitude: 19.82 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 37, pointers: 32, doc: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/IRGen/Inputs/Foundation.swift` (SWIFT) | Magnitude: 77.94 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 53, api: 23, args: 18
- `test/Constraints/diag_missing_arg.swift` (SWIFT) | Magnitude: 89.6 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 53, state_mutation: 35, args: 31, core_var_decl: 30
- `utils/gen-unicode-data/Sources/GenUtils/Mph.swift` (SWIFT) | Magnitude: 83.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 19, branch: 15, state_mutation: 15
- `utils/swift_build_support/tests/products/test_swift.py` (PYTHON) | Magnitude: 347.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 534, core_var_decl: 214, design_snake_case: 214, state_mutation: 102
- `lib/ClangImporter/ClangSourceBufferImporter.cpp` (CPP) | Magnitude: 53.2 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 22, structural_boundaries: 19, design_camel_case: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `benchmark/single-source/RangeContains.swift` (SWIFT) | Magnitude: 50.54 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 58, branch: 16, structural_boundaries: 10, args: 9
- `SwiftCompilerSources/Sources/Optimizer/FunctionPasses/EmbeddedWitnessCallSpecialization.swift` (SWIFT) | Magnitude: 15.28 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 34, indent_spaces: 34, branch: 7, core_var_decl: 7
- `test/Sema/accessibility_private.swift` (SWIFT) | Magnitude: 60.78 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 86, core_var_decl: 43, encapsulation: 35
- `test/Concurrency/Inputs/has-dispatch-private.h` (CPP) | Magnitude: 2.3 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, macros: 3, args: 2, func_start: 2
- `test/Interop/SwiftToCxx/core/set-min-access-level.swift` (SWIFT) | Magnitude: 18.34 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 17, args: 8, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `lib/IRGen/BitPatternReader.h` (CPP) | Magnitude: 17.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 27, indent_spaces: 22, structural_boundaries: 6, args: 5
- `validation-test/compiler_crashers_fixed/28064-swift-stmtconditionelement-walk.swift` (SWIFT) | Magnitude: 10.52 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 22, branch: 1, args: 1, class_start: 1
- `test/Interop/Cxx/enum/Inputs/nested-enums.h` (CPP) | Magnitude: 17.94 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 16, class_start: 6, core_var_decl: 5
- `validation-test/compiler_crashers_fixed/28267-swift-typechecker-checkconformance.swift` (SWIFT) | Magnitude: 10.52 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, class_start: 1
- `validation-test/compiler_crashers_fixed/28377-swift-expr-walk.swift` (SWIFT) | Magnitude: 10.52 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 5, args: 2, branch: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tools/SourceKit/tools/sourcekitd-test/TestOptions.h` (CPP) | Magnitude: 0.0 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 118, core_var_decl: 24, design_pascal_case: 20, doc: 9
- `test/decl/var/didset_oldvalue.swift` (SWIFT) | Magnitude: 23.8 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, core_var_decl: 7, class_start: 4
- `test/Interop/Cxx/templates/member-templates.swift` (SWIFT) | Magnitude: 16.68 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, core_var_decl: 9, pointers: 7, structural_boundaries: 6
- `validation-test/compiler_crashers_fixed/00791-swift-type-walk.swift` (SWIFT) | Magnitude: 30.84 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 20, class_start: 10, core_var_decl: 4, design_short_vars: 4
- `validation-test/compiler_crashers_fixed/21655-swift-boundgenerictype-get.swift` (SWIFT) | Magnitude: 15.4 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, class_start: 8, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib/ASTGen/Sources/ASTGen/Types.swift` (SWIFT) | Magnitude: 273.52 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 492, structural_boundaries: 104, branch: 93, core_var_decl: 70
- `lib/Sema/TypeOfReference.cpp` (CPP) | Magnitude: 2012.0 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2171, pointers: 773, branch: 553, structural_boundaries: 526
- `lib/IRGen/TBDGen.cpp` (CPP) | Magnitude: 582.68 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 649, structural_boundaries: 211, pointers: 190, branch: 178
- `benchmark/multi-source/Monoids/Presentation.swift` (SWIFT) | Magnitude: 331.46 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 246, structural_boundaries: 119, branch: 87, core_var_decl: 36
- `utils/parser-lib/profile-input.swift` (SWIFT) | Magnitude: 1638.38 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1836, branch: 525, structural_boundaries: 361, core_var_decl: 326

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `test/stdlib/Inputs/NSSlowString/NSSlowString.m` (OBJECTIVE-C) | Magnitude: 25.26 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 11, explicit_casts: 10, api: 7, indent_tabs: 7
- `include/swift/Demangling/TypeLookupError.h` (CPP) | Magnitude: 87.3 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 92, doc: 52, structural_boundaries: 49, pointers: 37
- `validation-test/compiler_crashers_fixed/00973-std-function-func-swift-type-subst.swift` (SWIFT) | Magnitude: 14.16 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, class_start: 2, core_var_decl: 2, design_short_vars: 2
- `include/swift/Threading/ThreadLocalStorage.h` (CPP) | Magnitude: 43.22 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 53, pointers: 28, args: 23
- `include/swift/AST/ClangNode.h` (CPP) | Magnitude: 43.46 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 48, immutability_locks: 38, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `lib/Macros/Sources/ObservationMacros/Extensions.swift` (SWIFT) | Magnitude: 121.5 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 231, branch: 97, structural_boundaries: 94, safety: 22
- `lib/SIL/IR/SILDeclRef.cpp` (CPP) | Magnitude: 1014.88 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1266, branch: 561, structural_boundaries: 504, pointers: 393
- `stdlib/public/Distributed/DistributedActorSystem.swift` (SWIFT) | Magnitude: 237.58 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 532, indent_spaces: 279, structural_boundaries: 124, branch: 37
- `lib/IDE/CodeCompletionResultBuilder.cpp` (CPP) | Magnitude: 150.02 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 197, pointers: 59, branch: 56, args: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `stdlib/public/Concurrency/ExecutorImpl.h` (CPP) | Magnitude: 72.86 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 84, doc: 78, indent_spaces: 76, args: 46
- `lib/IDE/IDEBridging.cpp` (CPP) | Magnitude: 15.84 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, func_start: 7, structural_boundaries: 4, args: 3
- `validation-test/compiler_crashers_fixed/01824-swift-typebase-getcanonicaltype.swift` (SWIFT) | Magnitude: 14.68 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 6, class_start: 4, safety_bypasses: 1, generics: 1
- `stdlib/public/SwiftShims/swift/shims/LibcOverlayShims.h` (CPP) | Magnitude: 32.8 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 42, macros: 29, indent_spaces: 23, func_start: 16
- `stdlib/public/Concurrency/AsyncStream.cpp` (CPP) | Magnitude: 7.3 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: sync_locks: 13, structural_boundaries: 7, pointers: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `lib/Sema/TypeCheckGeneric.cpp` (CPP) | Magnitude: 816.62 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_3`
  * Top Architectural Signatures: indent_spaces: 871, pointers: 330, branch: 246, structural_boundaries: 206

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib/SILOptimizer/Mandatory/MoveOnlyTempAllocationFromLetTester.cpp` (CPP) | Magnitude: 12.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 12, import: 6, pointers: 6
- `utils/gen-unicode-data/Sources/GenNormalization/Decomp.swift` (SWIFT) | Magnitude: 93.3 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 23, branch: 17, state_mutation: 15
- `test/Interpreter/SDK/Reflection_KVO.swift` (SWIFT) | Magnitude: 28.9 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 15, branch: 8, structural_boundaries: 8, core_var_decl: 7
- `lib/SILOptimizer/UtilityPasses/RCIdentityDumper.cpp` (CPP) | Magnitude: 31.8 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 14, pointers: 12, doc: 8
- `lib/SILGen/Scope.cpp` (CPP) | Magnitude: 53.28 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, branch: 17, structural_boundaries: 13, args: 11

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/ClangImporter/ClangImporter.cpp` -> Churn: **97.09%** | Cog Load: 59.6123% | Debt: 98.5523%
- `utils/build.ps1` -> Churn: **95.49%** | Cog Load: 74.8808% | Debt: 29.3736%
- `lib/Sema/CSBindings.cpp` -> Churn: **95.23%** | Cog Load: 44.1215% | Debt: 94.8506%
- `lib/Sema/CSSimplify.cpp` -> Churn: **92.66%** | Cog Load: 58.6793% | Debt: 53.3942%
- `lib/Sema/TypeCheckConcurrency.cpp` -> Churn: **88.53%** | Cog Load: 17.7505% | Debt: 58.4322%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/ClangImporter/ImportName.cpp` -> **Gabor Horvath** (83.3% isolated ownership) | Magnitude: 2308.32
- `test/Concurrency/transfernonsendable.swift` -> **Michael Gottesman** (85.7% isolated ownership) | Magnitude: 2244.14
- `stdlib/public/RuntimeModule/Dwarf.swift` -> **Alastair Houghton** (88.9% isolated ownership) | Magnitude: 2171.08
- `stdlib/public/core/Codable.swift` -> **Zev Eisenberg** (100.0% isolated ownership) | Magnitude: 2088.8
- `test/SILOptimizer/moveonly_objectchecker_diagnostics.swift` -> **Aidan Hall** (100.0% isolated ownership) | Magnitude: 2079.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `stdlib/public/runtime/SwiftObject.mm` -> **Severity: 2.832** (Embedded: 0.0354 * Error Risk: 80.0%)
- `utils/embedded-test-support/libc.c` -> **Severity: 2.746** (Embedded: 0.0343 * Error Risk: 80.0%)
- `test/Inputs/clang-importer-sdk/usr/include/objc/NSObject.h` -> **Severity: 2.225** (Embedded: 0.0278 * Error Risk: 80.0%)
- `unittests/runtime/Stdlib.cpp` -> **Severity: 2.138** (Embedded: 0.0251 * Error Risk: 85.2449%)
- `stdlib/include/llvm/Support/MemAlloc.h` -> **Severity: 2.111** (Embedded: 0.0264 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `stdlib/public/core/Assert.swift` -> **Severity: 1539.432** (Blast Radius: 28.072 * Doc Risk: 54.8387%)
- `test/SourceKit/CodeComplete/issue-76944.swift` -> **Severity: 810.9** (Blast Radius: 8.109 * Doc Risk: 100.0%)
- `stdlib/public/core/Builtin.swift` -> **Severity: 519.854** (Blast Radius: 10.637 * Doc Risk: 48.8722%)
- `stdlib/public/core/Availability.swift` -> **Severity: 495.438** (Blast Radius: 7.927 * Doc Risk: 62.5%)
- `stdlib/public/core/StringCreate.swift` -> **Severity: 418.9** (Blast Radius: 4.189 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 14251 literal sites + 1212 sites through wrappers = 15463
- **`memory_alloc`:** 5074 literal sites + 277 sites through wrappers = 5351
- **`panics_and_aborts`:** 7217 literal sites + 535 sites through wrappers = 7752

- `dump` (function, debug_prints, primitive): 258 call sites in 1 files -- `validation-test/Runtime/enum-multipayload-emptycase-storetag.swift`
- `B` (function, debug_prints, primitive): 126 call sites in 58 files -- `test/IRGen/Inputs/single-module-num-threads-2.swift`
- `expectCrashLater` (function, debug_prints, primitive): 115 call sites in 23 files -- `stdlib/private/StdlibUnittest/StdlibUnittest.swift`
- `_abstract` (function, panics_and_aborts, primitive): 45 call sites in 1 files -- `stdlib/public/core/ExistentialCollection.swift`
- `throwingFn` (function, panics_and_aborts, primitive): 41 call sites in 1 files -- `test/Profiler/coverage_errors_exec.swift`
- `genericPrintFunction` (function, debug_prints, primitive): 35 call sites in 2 files -- `test/Interop/SwiftToCxx/generics/generic-function-in-cxx.swift`
- `readFile` (function, panics_and_aborts, primitive): 33 call sites in 14 files -- `utils/gen-unicode-data/Sources/GenUtils/Files.swift`
- `LOG` (macro, memory_alloc, via LOG_SECTION): 32 call sites in 2 files -- `stdlib/public/runtime/GenericMetadataBuilder.cpp`
- `SWIFT_LAZY_CONSTANT` (macro, memory_alloc, primitive): 28 call sites in 12 files -- `include/swift/Basic/Lazy.h`
- `p` (function, debug_prints, primitive): 27 call sites in 1 files -- `test/Concurrency/async_task_escalate_priority.swift`
- `useP` (function, debug_prints, primitive): 27 call sites in 1 files -- `test/SILOptimizer/specialize_opaque_type_archetypes.swift`
- `tuplify` (function, debug_prints, primitive): 26 call sites in 1 files -- `test/Constraints/result_builder_diags.swift`
*(+572 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 455645 call pairs -- scoped 35.8%, unique 4.0%, ambiguous 43.7%, external 16.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 350182 | 33.8% | 2.7% | 47.5% | 16.0% |
| swift | 92814 | 44.4% | 8.9% | 33.4% | 13.3% |
| python | 8306 | 27.2% | 0.0% | 13.4% | 59.4% |
| objective-c | 2444 | 27.3% | 7.3% | 15.8% | 49.6% |
| powershell | 667 | 18.3% | 0.0% | 0.0% | 81.7% |
| shell | 578 | 15.7% | 0.0% | 0.0% | 84.3% |
| c | 456 | 29.8% | 14.3% | 13.4% | 42.5% |
| yacc | 173 | 0.0% | 33.5% | 17.3% | 49.1% |
| ruby | 25 | 0.0% | 0.0% | 0.0% | 100.0% |

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
