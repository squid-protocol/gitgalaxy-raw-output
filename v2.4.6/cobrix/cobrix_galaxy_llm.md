# ARCHITECTURAL_BRIEF: cobrix
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cobrix` |
| **Timestamp** | `2026-08-03T19:28:45.423788+00:00` |
| **Scan Duration** | `1.98s` |
| **Git Branch** | `master` |
| **Git Commit** | `7200b77cdebb4244137f88b48e908acfc4ccbee1` |
| **Git Remote** | `https://github.com/AbsaOSS/cobrix.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 500 malicious artifacts.

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
| Total Artifacts | 705 |
| Analyzed Artifacts (Scanned) | 625 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 80 |
| Total LOC | 48690 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 88.7% |
| Dominant Lang | SCALA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5783 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2967 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3542 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| SCALA | 447 | 36237 | 71.5% |
| PLAINTEXT | 59 | 276 | 9.4% |
| JSON | 39 | 5922 | 6.2% |
| COBOL | 35 | 1215 | 5.6% |
| XML | 18 | 0 | 2.9% |
| JAVA | 8 | 4939 | 1.3% |
| BINARY_THREAT | 6 | 6 | 1.0% |
| MARKDOWN | 5 | 0 | 0.8% |
| CSV | 4 | 41 | 0.6% |
| SHELL | 2 | 13 | 0.3% |
| GROOVY | 1 | 26 | 0.2% |
| BATCH | 1 | 15 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.221`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 451 | 72.2% |
| file_cluster_16 | 64 | 10.2% |
| file_cluster_15 | 11 | 1.8% |
| file_cluster_13 | 7 | 1.1% |
| Unknown | 6 | 1.0% |
| file_cluster_17 | 4 | 0.6% |
| file_cluster_0 | 4 | 0.6% |
| file_cluster_11 | 2 | 0.3% |
| file_cluster_9 | 2 | 0.3% |
| file_cluster_7 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 58 | 9.3% |
| Static: Minified & Vendor Opaque Mass | 15 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 80*

**Composition by Extension & Reason:**
- `.dat`: 27x Excluded (Unsupported Extension: '.dat'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.g4`: 3x Unsupported Format (.g4)
- `.java`: 1x Excluded (Embedded Hex Payload: 20472 hex tokens in 1352 LOC), 1x Excluded (Embedded Hex Payload: 15144 hex tokens in 985 LOC), 1x Excluded (Embedded Hex Payload: 29256 hex tokens in 999 LOC)
- `.plot`: 3x Excluded (Unsupported Extension: '.plot')
- `.sbt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scala`: 1x Excluded (Embedded Hex Payload: 2080 hex tokens in 912 LOC), 1x Excluded (Embedded Hex Payload: 723 hex tokens in 567 LOC)
- `.json`: 2x Excluded (Static Asset Blob without Intent: 2350 LOC)
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.properties`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bz2`: 1x Excluded (Explicitly Denied Extension: '.bz2')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 15.5 | 7.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.6 | 16.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.0 | 0.2 | 0.0 |
| API Exposure | 0.0 | 15.1 | 2.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 44.8 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.9 | 1.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 84.3 | 5.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.0 | 13.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test5MultisegmentSpec.scala` (Hits: 23)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test13aFixedLenFileHeadersSpec.scala` (Hits: 11)
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test14RdwAdjustmentsSpec.scala` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **SparkTestBase.scala** (`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/base/SparkTestBase.scala`) — 85 inbound connections
2. **CopybookParser.scala** (`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala`) — 59 inbound connections
3. **BinaryFileFixture.scala** (`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/fixtures/BinaryFileFixture.scala`) — 57 inbound connections
4. **Group.scala** (`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Group.scala`) — 42 inbound connections
5. **FileUtils.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/FileUtils.scala`) — 36 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **SparkCobolProcessor.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala`) — 33 outbound dependencies
2. **DefaultSource.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala`) — 29 outbound dependencies
3. **CobolSchema.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala`) — 27 outbound dependencies
4. **CopybookParser.scala** (`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala`) — 26 outbound dependencies
5. **CobolRelation.scala** (`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/CobolRelation.scala`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `extractRecord` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **795.3** | LOC: 165
- `validateSparkCobolOptions` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> Impact: **362.8** | LOC: 235
  * *Intent:* /** * Parses the list of segment levels and it's corresponding segment ids. * * Example: * For * {{{ * sprak.read * .option("segment_id_level0", "SEGI...
- `sparseIndexGenerator` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala`) -> Impact: **356.2** | LOC: 91
- `recordExtractor` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala`) -> Impact: **337.8** | LOC: 36
  * *Intent:* /** * The Cobol data reader for variable length records that gets input binary data as a stream and produces nested structure schema
- `copyMetadata` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala`) -> Impact: **321.9** | LOC: 69
- `extractHierarchicalRecord` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **279.8** | LOC: 195
- `process` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala`) -> Impact: **278.1** | LOC: 228
- `writeToBytes` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala`) -> Impact: **269.9** | LOC: 107
- `putEncodedNumStrToArray` (@ `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala`) -> Impact: **242.7** | LOC: 59
- `process` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/processor/CobolProcessor.scala`) -> Impact: **236.5** | LOC: 123

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `process` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/processor/CobolProcessor.scala`) -> **O(2^N) [Recursive]**
- `withFilter` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/UsingUtils.scala`) -> **O(2^N) [Recursive]**
  * *Intent:* * But `using()` can be nested. * * Example usage: * {{{ * val result = UsingUtils.using(new AutoCloseableResource()) { resource => * // Perform operat...
- `getRawRecordContext` (@ `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/VariableBlockVariableRecordExtractorSuite.scala`) -> **O(2^N) [Recursive]**
- `process` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala`) -> **O(2^N) [Recursive]**
- `recordExtractor` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * The Cobol data reader for variable length records that gets input binary data as a stream and produces nested structure schema
- `parseTree` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Tokenizes a Cobol Copybook contents and returns the AST. * * This method accepts arguments that affect only structure of the output AST. * * @pa...
- `transform` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/NonTerminalsAdder.scala`) -> **O(2^N) [Recursive]**
- `copyMetadata` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala`) -> **O(2^N) [Recursive]**
- `rowToString` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala`) -> **O(2^N) [Recursive]**
- `calculateSchemaSizes` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/BinaryPropertiesAdder.scala`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `main` (@ `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala`) -> DB Complexity: **198**
- `getReaderProperties` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> DB Complexity: **57**
- `resolveHeaderTrailerOffsets` (@ `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala`) -> DB Complexity: **29**
  * *Intent:* /**
- `decodeEbcdicNumber` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala`) -> DB Complexity: **19**
- `main` (@ `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen19WideTransactions.scala`) -> DB Complexity: **17**
  * *Intent:* //val numberOfRecordsToGenerate = rand.nextInt(90000) + 10000
- `specialValues` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> DB Complexity: **16**
- `parse` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala`) -> DB Complexity: **15**
  * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except in compl...
- `identifier` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> DB Complexity: **15**
- `extractHierarchicalRecord` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> DB Complexity: **14**
- `values` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> DB Complexity: **13**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr` | 15 | 5270.75 | 16.89% | 39.84% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders` | 9 | 1938.42 | 32.11% | 49.96% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding` | 5 | 1538.46 | 36.77% | 42.06% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record` | 3 | 1386.76 | 11.97% | 4.69% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters` | 9 | 1202.72 | 9.6% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform` | 10 | 1161.08 | 21.48% | 54.46% |
| `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils` | 8 | 1079.92 | 13.22% | 13.82% |
| `data/test2_data` | 2 | 1000.0 | 0.0% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw` | 11 | 979.84 | 45.06% | 18.18% |
| `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration` | 45 | 898.34 | 8.9% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage1364.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage1388.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage300.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/headerparsers/RecordHeaderParser.scala` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextFullRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/AutoCloseableSpy.scala` -> **100.0%** Exposure
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` -> **0** Orphaned Functions | **145** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` -> **55** Orphaned Functions | **0** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` -> **6** Orphaned Functions | **32** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryNumberDecoders.scala` -> **19** Orphaned Functions | **0** Duplicates
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` -> **13** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala`** -> AI Confidence: **99.48%**
2. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`** -> AI Confidence: **99.44%**
3. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`** -> AI Confidence: **99.44%**
4. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala`** -> AI Confidence: **99.44%**
5. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala`** -> AI Confidence: **99.42%**
6. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala`** -> AI Confidence: **99.42%**
7. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala`** -> AI Confidence: **99.39%**
8. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/SegmentRedefinesMarker.scala`** -> AI Confidence: **99.39%**
9. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/FixedWithRecordLengthExprRawRecordExtractor.scala`** -> AI Confidence: **99.39%**
10. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/VRLRecordReader.scala`** -> AI Confidence: **99.39%**
11. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala`** -> AI Confidence: **99.39%**
12. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala`** -> AI Confidence: **99.39%**
13. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/DependencyMarker.scala`** -> AI Confidence: **99.34%**
14. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala`** -> AI Confidence: **99.34%**
15. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala`** -> AI Confidence: **99.34%**
16. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/BufferedFSDataInputStream.scala`** -> AI Confidence: **99.34%**
17. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/FloatingPointDecoders.scala`** -> AI Confidence: **99.32%**
18. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/lexer/Lexer.scala`** -> AI Confidence: **99.32%**
19. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/DebugFieldsAdder.scala`** -> AI Confidence: **99.31%**
20. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/GroupFillersRenamer.scala`** -> AI Confidence: **99.31%**
21. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/SegmentParentsSetter.scala`** -> AI Confidence: **99.31%**
22. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/FixedLenNestedReader.scala`** -> AI Confidence: **99.31%**
23. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala`** -> AI Confidence: **99.31%**
24. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala`** -> AI Confidence: **99.31%**
25. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/FixedLenNestedRowIterator.scala`** -> AI Confidence: **99.31%**
26. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/VarLenHierarchicalIterator.scala`** -> AI Confidence: **99.31%**
27. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/schema/CobolSchema.scala`** -> AI Confidence: **99.31%**
28. **`cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/validator/ReaderParametersValidator.scala`** -> AI Confidence: **99.31%**
29. **`cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/parse/FieldSizeSpec.scala`** -> AI Confidence: **99.31%**
30. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala`** -> AI Confidence: **99.31%**
31. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/copybook/CopybookContentLoader.scala`** -> AI Confidence: **99.31%**
32. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/IndexBuilder.scala`** -> AI Confidence: **99.31%**
33. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/parameters/CobolParametersValidator.scala`** -> AI Confidence: **99.31%**
34. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/scanners/CobolScanners.scala`** -> AI Confidence: **99.31%**
35. **`spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/FileStreamer.scala`** -> AI Confidence: **99.31%**
36. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSourceSpec.scala`** -> AI Confidence: **99.31%**
37. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/ImprovedNullDetectionSpec.scala`** -> AI Confidence: **99.31%**
38. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/base/CobolTestBase.scala`** -> AI Confidence: **99.31%**
39. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test11CustomRDWParser.scala`** -> AI Confidence: **99.31%**
40. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test13aFixedLenFileHeadersSpec.scala`** -> AI Confidence: **99.31%**
41. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test13bVarLenFileHeadersSpec.scala`** -> AI Confidence: **99.31%**
42. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test14RdwAdjustmentsSpec.scala`** -> AI Confidence: **99.31%**
43. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test15PathWithAsteriskSpec.scala`** -> AI Confidence: **99.31%**
44. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test16FixedLenSegmentRedefinesSpec.scala`** -> AI Confidence: **99.31%**
45. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test1FixedLengthRecordsSpec.scala`** -> AI Confidence: **99.31%**
46. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test1bGeneratedFieldsSpec.scala`** -> AI Confidence: **99.31%**
47. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test25OccursMappings.scala`** -> AI Confidence: **99.31%**
48. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test2RecordOffsetsSpec.scala`** -> AI Confidence: **99.31%**
49. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test37RecordLengthMappingSpec.scala`** -> AI Confidence: **99.31%**
50. **`spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test3SegmentFieldSpec.scala`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookLexer.java` -> **100.0%** Exposure
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/AsciiStringDecoderWrapperSpec.scala` -> **0.0016%** Exposure
### Exploit Generation Surface
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/GroupFillersRenamer.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/NonTerminalsAdder.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BCDNumberDecoders.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2278` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/BufferedFSDataInputStream.scala` (SCALA) -> Cumulative Risk: **788.37**
- **Archetype:** `file_cluster_8` (Distance: 11.507 IQR)
- **Magnitude:** 179.92 | **LOC:** 150 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Algorithmic Dos (99.9997%)
- **Heaviest Functions:** `readFully` (Impact: 70.3), `openStream` (Impact: 22.1), `readFullyHelper` (Impact: 21.9)

### 2. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA) -> Cumulative Risk: **748.14**
- **Archetype:** `file_cluster_0` (Distance: 13.373 IQR)
- **Magnitude:** 2904.86 | **LOC:** 3481 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.9773%), State Flux (99.6505%)
- **Heaviest Functions:** `identifier` (Impact: 117.9), `specialValues` (Impact: 115.6), `values` (Impact: 42.2)

### 3. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA) -> Cumulative Risk: **747.81**
- **Archetype:** `file_cluster_16` (Distance: 12.934 IQR)
- **Magnitude:** 1345.16 | **LOC:** 555 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `extractRecord` (Impact: 795.3), `extractHierarchicalRecord` (Impact: 279.8), `applyRecordPostProcessing` (Impact: 176.7)

### 4. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/VarLenHierarchicalIterator.scala` (SCALA) -> Cumulative Risk: **725.98**
- **Archetype:** `file_cluster_16` (Distance: 12.578 IQR)
- **Magnitude:** 110.64 | **LOC:** 164 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9623%)
- **Heaviest Functions:** `fetchNext` (Impact: 53.9), `next` (Impact: 13.5), `extractRow` (Impact: 2.9)

### 5. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` (SCALA) -> Cumulative Risk: **723.7**
- **Archetype:** `file_cluster_8` (Distance: 12.607 IQR)
- **Magnitude:** 269.0 | **LOC:** 324 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 92.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `resolveHeaderTrailerOffsets` (Impact: 105.8), `createRelation` (Impact: 66.5), `buildEitherReader` (Impact: 16.8)

### 6. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala` (SCALA) -> Cumulative Risk: **720.22**
- **Archetype:** `file_cluster_8` (Distance: 12.266 IQR)
- **Magnitude:** 389.02 | **LOC:** 171 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `sparseIndexGenerator` (Impact: 356.2)

### 7. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/BinaryEncoders.scala` (SCALA) -> Cumulative Risk: **713.25**
- **Archetype:** `file_cluster_8` (Distance: 9.211 IQR)
- **Magnitude:** 208.34 | **LOC:** 72 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (90.7814%)
- **Heaviest Functions:** `encodeBinaryNumber` (Impact: 200.4)

### 8. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/UsingUtils.scala` (SCALA) -> Cumulative Risk: **694.57**
- **Archetype:** `file_cluster_15` (Distance: 11.586 IQR)
- **Magnitude:** 234.92 | **LOC:** 127 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `withFilter` (Impact: 172.7), `using` (Impact: 46.2)

### 9. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BCDNumberDecoders.scala` (SCALA) -> Cumulative Risk: **686.29**
- **Archetype:** `file_cluster_15` (Distance: 11.694 IQR)
- **Magnitude:** 245.46 | **LOC:** 175 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9687%), Verification (80.0%)
- **Heaviest Functions:** `decodeBigBCDNumber` (Impact: 133.7), `decodeBCDIntegralNumber` (Impact: 61.1), `decodeBigBCDDecimal` (Impact: 9.3)

### 10. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA) -> Cumulative Risk: **681.57**
- **Archetype:** `file_cluster_8` (Distance: 10.396 IQR)
- **Magnitude:** 623.86 | **LOC:** 213 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `encodeDisplayNumberSignSeparate` (Impact: 230.5), `encodeDisplayNumberSignOverpunched` (Impact: 210.6), `setPaddedEbcdicNumberWithSignSeparate` (Impact: 75.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.373 IQR)
- **Top Global Matches:** file_cluster_0: 13.373, file_cluster_8: 13.515, file_cluster_11: 13.646
- **Magnitude:** 2904.86 | **LOC:** 3481 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (76.3931%), Tech Debt (99.9773%)
**Top Internal Functions/Classes:**
  * `identifier` (Impact: 117.9 | O(N^1) | DB: 15)
  * `specialValues` (Impact: 115.6 | O(N^1) | DB: 16)
  * `values` (Impact: 42.2 | O(N^1) | DB: 13)
  * `literal` (Impact: 40.4 | O(N^1) | DB: 5)
  * `numericLiteral` (Impact: 38.8 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 823`, `structural_boundaries: 872`, `args: 532`, `func_start: 1071`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 696`, `duplicate_logic: 145`
* *Architecture:* `api: 518`, `import: 4`
* *Defense:* `safety: 178`, `doc: 2`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.09
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 0):` java.util.ArrayList, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.*, org.antlr.v4.runtime.tree.*, org.antlr.v4.runtime.misc.*, java.util.List, java.util.Iterator, org.antlr.v4.runtime.dfa.DFA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.934 IQR)
- **Top Global Matches:** file_cluster_16: 12.934, file_cluster_15: 13.055, file_cluster_11: 13.154
- **Magnitude:** 1345.16 | **LOC:** 555 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (25.9126%), Tech Debt (14.0754%)
**Top Internal Functions/Classes:**
  * `extractRecord` (Impact: 795.3 | O(N^6) | DB: 10)
  * `extractHierarchicalRecord` (Impact: 279.8 | O(N^4) | DB: 14)
  * `applyRecordPostProcessing` (Impact: 176.7 | O(N^6) | DB: 1)
  * `getCorruptFieldsGroup` (Impact: 1.4 | O(N^1))
    * *Intent:* * <p>This method applies additional postprocessing to the schema obtained from a copybook to make it...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 25`, `args: 43`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 73`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `safety: 26`, `doc: 49`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.773
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.015037
  * `Imports (Out-Degree: 7):` za.co.absa.cobrix.cobol.reader.policies.SchemaRetentionPolicy, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, za.co.absa.cobrix.cobol.parser.ast.Group, Primitive, za.co.absa.cobrix.cobol.utils.StringUtils, ListBuffer, Statement, scala.collection.mutable.ArrayBuffer...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.871 IQR)
- **Top Global Matches:** file_cluster_8: 13.871, file_cluster_15: 13.936, file_cluster_11: 13.943
- **Magnitude:** 1114.7 | **LOC:** 880 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (41.2577%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkBounds` (Impact: 130.0 | O(N^3))
  * `replaceUsage` (Impact: 121.2 | O(N^4))
  * `visitPrimitive` (Impact: 94.0 | O(N^2) | DB: 5)
  * `fromNumericZPicRegexDecimalScaled` (Impact: 53.5 | O(N^1) | DB: 2)
  * `visitPic` (Impact: 46.8 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 58`, `args: 121`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 90`
* *Architecture:* `io: 1`, `api: 65`, `import: 1`
* *Defense:* `safety: 172`, `test: 9`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.09
  * `Choke Point (Betweenness):` 0.000136 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 11):` RuleContext, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, Primitive, za.co.absa.cobrix.cobol.parser.CopybookParser, za.co.absa.cobrix.cobol.parser.encoding._, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.parser.ast.datatype._...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.222 IQR)
- **Top Global Matches:** file_cluster_8: 12.222, file_cluster_17: 12.457, file_cluster_15: 12.517
- **Magnitude:** 1035.34 | **LOC:** 1069 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 93.8%
- **Algorithmic:** O(N^6) | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (25.0698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateSparkCobolOptions` (Impact: 362.8 | O(N^2) | DB: 2)
    * *Intent:* /** * Parses the list of segment levels and it's corresponding segment ids. * * Example: * For * {{{...
  * `getSegmentRedefineParents` (Impact: 76.7 | O(N^4))
    * *Intent:* /** * Parses parameters for reading multisegment mainframe files *
  * `getRecordLengthMappings` (Impact: 65.2 | O(N^3))
  * `parseVariableLengthParameters` (Impact: 57.7 | O(N^2))
  * `getReaderProperties` (Impact: 46.9 | O(N^6) | DB: 57)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 65`, `args: 50`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 80`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 49`, `doc: 29`, `immutability_locks: 169`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.19
  * `Choke Point (Betweenness):` 0.000657 | `Ripple Effect (Closeness):` 0.021311
  * `Imports (Out-Degree: 8):` za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.reader.policies.SchemaRetentionPolicy, za.co.absa.cobrix.cobol.parser.policies.DebugFieldsPolicy.DebugFieldsPolicy, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat._, za.co.absa.cobrix.cobol.parser.policies._, scala.collection.mutable.ListBuffer, za.co.absa.cobrix.cobol.parser.CopybookParser...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.23 IQR)
- **Top Global Matches:** file_cluster_15: 12.23, file_cluster_0: 12.414, file_cluster_11: 12.438
- **Magnitude:** 924.42 | **LOC:** 599 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (17.5852%), Tech Debt (10.5992%)
**Top Internal Functions/Classes:**
  * `copyMetadata` (Impact: 321.9 | O(2^N))
  * `flattenSchema` (Impact: 113.3 | O(N^3) | DB: 5)
  * `rowToString` (Impact: 101.2 | O(2^N))
  * `splitFieldPath` (Impact: 66.2 | O(N^3) | DB: 8)
  * `getField` (Impact: 50.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 38`, `args: 108`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 17`, `doc: 35`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.364
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.058894
  * `Imports (Out-Degree: 1):` Row, DataFrame, SparkSession, za.co.absa.cobrix.cobol.internal.Logging, org.apache.hadoop.fs.FileSystem, scala.util.Try, com.fasterxml.jackson.databind.ObjectMapper, scala.collection.mutable.ListBuffer...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.556 IQR)
- **Top Global Matches:** file_cluster_16: 12.556, file_cluster_8: 12.565, file_cluster_15: 12.671
- **Magnitude:** 709.84 | **LOC:** 480 | **CtrlFlow:** 92.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (37.7554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `putEncodedNumStrToArray` (Impact: 242.7 | O(N^6) | DB: 3)
  * `encodeUncompressed` (Impact: 84.5 | O(N^3) | DB: 3)
  * `encodeBcd` (Impact: 30.0 | O(N^2) | DB: 2)
  * `putDecimalToArray` (Impact: 23.1 | O(N^2) | DB: 2)
  * `putShortToArray` (Impact: 21.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 9`, `args: 35`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `duplicate_logic: 4`, `orphaned_logic: 13`
* *Architecture:* `api: 22`, `import: 1`
* *Defense:* `safety: 8`, `doc: 23`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` za.co.absa.cobrix.cobol.parser.common.Constants, scodec.Attempt.Successful, scala.util.Random, za.co.absa.cobrix.cobol.parser.decoders.BinaryUtils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.396 IQR)
- **Top Global Matches:** file_cluster_8: 10.396, file_cluster_16: 10.782, file_cluster_13: 10.895
- **Magnitude:** 623.86 | **LOC:** 213 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (69.228%), Tech Debt (40.7136%)
**Top Internal Functions/Classes:**
  * `encodeDisplayNumberSignSeparate` (Impact: 230.5 | O(N^6))
    * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "Lice...
  * `encodeDisplayNumberSignOverpunched` (Impact: 210.6 | O(N^6))
  * `setPaddedEbcdicNumberWithSignSeparate` (Impact: 75.2 | O(N^2) | DB: 4)
  * `setPaddedEbcdicNumberWithSignOverpunched` (Impact: 73.5 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`, `orphaned_logic: 2`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 3`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` java.math.RoundingMode, za.co.absa.cobrix.cobol.parser.position.Position
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.245 IQR)
- **Top Global Matches:** file_cluster_8: 11.245, file_cluster_16: 11.617, file_cluster_7: 11.713
- **Magnitude:** 615.8 | **LOC:** 292 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.7041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recordExtractor` (Impact: 337.8 | O(2^N))
    * *Intent:* /** * The Cobol data reader for variable length records that gets input binary data as a stream and ...
  * `generateIndex` (Impact: 159.6 | O(N^6))
  * `getRecordIterator` (Impact: 35.9 | O(N^6))
  * `getRootSegmentId` (Impact: 18.8 | O(N^2))
  * `getRecordHeaderParser` (Impact: 16.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 33`, `args: 25`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 37`, `doc: 8`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.323
  * `Choke Point (Betweenness):` 0.000674 | `Ripple Effect (Closeness):` 0.005235
  * `Imports (Out-Degree: 13):` VariableBlock, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.reader.index.entry.SparseIndexEntry, VariableLength, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.reader.stream.SimpleStream, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat.FixedBlock...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.928 IQR)
- **Top Global Matches:** file_cluster_15: 12.928, file_cluster_0: 13.028, file_cluster_16: 13.06
- **Magnitude:** 600.56 | **LOC:** 429 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (44.9052%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `decodeEbcdicNumber` (Impact: 175.8 | O(N^2) | DB: 19)
  * `decodeAsciiNumber` (Impact: 140.0 | O(N^3) | DB: 6)
  * `decodeAsciiString` (Impact: 49.2 | O(N^2) | DB: 2)
    * *Intent:* /** * A decoder for any EBCDIC string fields (alphabetical or any char) * * @param bytes A byte arra...
  * `decodeUtf16String` (Impact: 27.8 | O(N^1))
    * *Intent:* /** * A decoder for any ASCII string fields (alphabetical or any char) * * @param bytes A byte array...
  * `decodeEbcdicString` (Impact: 25.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 26`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 81`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `doc: 93`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 2):` java.nio.charset.StandardCharsets, Constants._, StringTools._, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.common.Constants
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.811 IQR)
- **Top Global Matches:** file_cluster_16: 11.811, file_cluster_15: 11.934, file_cluster_8: 11.951
- **Magnitude:** 578.9 | **LOC:** 480 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.3927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `merge` (Impact: 159.2 | O(2^N))
  * `getFieldByName` (Impact: 124.0 | O(N^3))
  * `generateRecordLayoutPositions` (Impact: 65.5 | O(N^3) | DB: 1)
  * `setPrimitiveField` (Impact: 63.8 | O(N^2))
  * `dropFillers` (Impact: 53.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 44`, `args: 58`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `safety: 25`, `doc: 33`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.842
  * `Choke Point (Betweenness):` 0.001153 | `Ripple Effect (Closeness):` 0.068462
  * `Imports (Out-Degree: 5):` za.co.absa.cobrix.cobol.internal.Logging, java.util.concurrent.ConcurrentHashMap, Copybook._, za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, Primitive, za.co.absa.cobrix.cobol.parser.asttransform.BinaryPropertiesAdder, Statement, scala.collection.mutable.ArrayBuffer...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.101 IQR)
- **Top Global Matches:** file_cluster_0: 12.101, file_cluster_8: 12.4, file_cluster_16: 12.459
- **Magnitude:** 578.42 | **LOC:** 516 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (66.5756%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `value` (Impact: 66.5 | O(N^1) | DB: 8)
  * `obj` (Impact: 29.6 | O(N^1) | DB: 10)
  * `arr` (Impact: 29.6 | O(N^1) | DB: 10)
  * `accept` (Impact: 14.3 | O(N^1))
  * `accept` (Impact: 14.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 146`, `args: 66`, `func_start: 142`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 96`, `duplicate_logic: 32`, `orphaned_logic: 6`
* *Architecture:* `api: 75`, `import: 4`
* *Defense:* `safety: 26`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.ArrayList, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.*, org.antlr.v4.runtime.tree.*, org.antlr.v4.runtime.misc.*, java.util.List, java.util.Iterator, org.antlr.v4.runtime.dfa.DFA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.177 IQR)
- **Top Global Matches:** file_cluster_8: 11.177, file_cluster_15: 11.24, file_cluster_7: 11.379
- **Magnitude:** 546.74 | **LOC:** 476 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.3993%), Tech Debt (35.7648%)
**Top Internal Functions/Classes:**
  * `writeToBytes` (Impact: 269.9 | O(2^N) | DB: 3)
  * `buildGroupNode` (Impact: 121.2 | O(N^4))
    * *Intent:* /** * Constructs a writer AST (Abstract Syntax Tree) from a copybook and Spark schema for serializat...
  * `buildPrimitiveNode` (Impact: 92.6 | O(N^3))
  * `combine` (Impact: 46.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 29`, `args: 31`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 45`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Row, za.co.absa.cobrix.cobol.reader.parameters.ReaderParameters, Integral, za.co.absa.cobrix.cobol.parser.ast.Group, Primitive, za.co.absa.cobrix.cobol.parser.ast.datatype.Decimal, NestedRecordCombiner._, org.apache.spark.sql.types.ArrayType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test15_data/a/example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test15_data/b/example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test1_data/example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test2_data/example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `data/test2_data/example2.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/example_data/raw_data/file1.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.493, file_cluster_15: 11.573, file_cluster_16: 11.631
- **Magnitude:** 453.84 | **LOC:** 150 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (30.1966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEncoder` (Impact: 126.5 | O(N^4))
    * *Intent:* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "License...
  * `getDisplayEncoder` (Impact: 103.1 | O(N^6))
  * `getBdcEncoder` (Impact: 96.6 | O(N^5))
  * `getBinaryEncoder` (Impact: 72.4 | O(N^5))
  * `getStringEncoder` (Impact: 47.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 25`, `args: 46`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`
* *Architecture:* `io: 1`, `api: 5`, `import: 1`
* *Defense:* `safety: 19`, `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.411
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.068556
  * `Imports (Out-Degree: 9):` COMP3U, Integral, java.nio.charset.Charset, Decimal, za.co.absa.cobrix.cobol.parser.decoders.BinaryUtils, COMP3, StandardCharsets, java.util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.277 IQR)
- **Top Global Matches:** file_cluster_8: 10.277, file_cluster_15: 10.614, file_cluster_16: 10.655
- **Magnitude:** 425.74 | **LOC:** 444 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (19.2645%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parsePrimitive` (Impact: 116.5 | O(N^2))
  * `createSparkSchema` (Impact: 112.6 | O(N^5))
  * `parseGroup` (Impact: 84.9 | O(2^N))
  * `builder` (Impact: 19.6 | O(N^2) | DB: 11)
  * `addExtendedPrimitiveMetadata` (Impact: 16.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 33`, `args: 54`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `safety: 4`, `doc: 15`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018029
  * `Imports (Out-Degree: 11):` COMP1, Integral, COMP5, za.co.absa.cobrix.cobol.parser.policies.MetadataPolicy, za.co.absa.cobrix.spark.cobol.parameters.MetadataFields.MAX_ELEMENTS, CorruptFieldsPolicy, MIN_ELEMENTS, za.co.absa.cobrix.cobol.parser.common.Constants...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/index/IndexGenerator.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.266 IQR)
- **Top Global Matches:** file_cluster_8: 12.266, file_cluster_16: 12.305, file_cluster_11: 12.373
- **Magnitude:** 389.02 | **LOC:** 171 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (75.1143%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sparseIndexGenerator` (Impact: 356.2 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 14`, `args: 4`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.358
  * `Choke Point (Betweenness):` 0.000207 | `Ripple Effect (Closeness):` 0.007458
  * `Imports (Out-Degree: 8):` za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.reader.extractors.raw.RawRecordExtractor, za.co.absa.cobrix.cobol.reader.common.Constants, za.co.absa.cobrix.cobol.reader.stream.SimpleStream, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParser, scala.collection.mutable.ArrayBuffer, za.co.absa.cobrix.cobol.reader.index.entry.SparseIndexEntry, za.co.absa.cobrix.cobol.parser.ast.Primitive...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_15` (Drift: 11.219 IQR)
- **Top Global Matches:** file_cluster_15: 11.219, file_cluster_8: 11.337, file_cluster_16: 11.584
- **Magnitude:** 332.44 | **LOC:** 354 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.0921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBinaryEncodedIntegralDecoder` (Impact: 97.3 | O(N^2))
  * `getStringDecoder` (Impact: 84.5 | O(N^6))
    * *Intent:* /** * Gets a decoder function suitable for converting the specified COBOL data type * to a target ty...
  * `getDecoder` (Impact: 75.6 | O(N^4))
  * `getBCDIntegralDecoder` (Impact: 45.1 | O(N^3))
  * `getStringStrimmingType` (Impact: 14.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 25`, `args: 78`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 22`, `doc: 17`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.548
  * `Choke Point (Betweenness):` 0.00056 | `Ripple Effect (Closeness):` 0.069089
  * `Imports (Out-Degree: 6):` za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat.FloatingPointFormat, java.nio.charset.Charset, za.co.absa.cobrix.cobol.parser.common.Constants, za.co.absa.cobrix.cobol.utils.StringUtils, StandardCharsets, za.co.absa.cobrix.cobol.parser.position.Position, CodePageCommon, maxLongPrecision...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.491 IQR)
- **Top Global Matches:** file_cluster_16: 11.491, file_cluster_8: 11.501, file_cluster_4: 11.773
- **Magnitude:** 321.24 | **LOC:** 292 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (28.8432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 278.1 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 51`, `args: 26`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 15`, `import: 1`
* *Defense:* `safety: 14`, `doc: 11`, `immutability_locks: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` org.apache.hadoop.fs.Path, SerializableConfiguration, za.co.absa.cobrix.spark.cobol.source.CobolRelation, za.co.absa.cobrix.cobol.utils.UsingUtils, za.co.absa.cobrix.cobol.reader.index.entry.SparseIndexEntry, za.co.absa.cobrix.spark.cobol.source.streaming.FileStreamer, DefaultSource, za.co.absa.cobrix.cobol.processor.CobolProcessingStrategy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.804 IQR)
- **Top Global Matches:** file_cluster_15: 12.804, file_cluster_8: 12.897, file_cluster_16: 13.146
- **Magnitude:** 305.94 | **LOC:** 249 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (21.8656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBytesCount` (Impact: 168.0 | O(N^3) | DB: 1)
  * `decodeBinaryNumber` (Impact: 86.1 | O(N^2))
  * `decodeString` (Impact: 25.1 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 12`, `args: 39`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 8`, `doc: 15`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.903
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.069979
  * `Imports (Out-Degree: 2):` Encoding, za.co.absa.cobrix.cobol.parser.common.Constants, Constants._, za.co.absa.cobrix.cobol.parser.ast.datatype._, za.co.absa.cobrix.cobol.parser.encoding.EBCDIC
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.409 IQR)
- **Top Global Matches:** file_cluster_16: 11.409, file_cluster_8: 11.634, file_cluster_15: 11.718
- **Magnitude:** 270.4 | **LOC:** 491 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (7.3227%), Tech Debt (51.2752%)
**Top Internal Functions/Classes:**
  * `parseTree` (Impact: 42.0 | O(N^4))
    * *Intent:* /**
  * `getParentToChildrenMap` (Impact: 29.4 | O(N^3))
    * *Intent:* /** * Tokenizes a Cobol Copybook contents and returns the AST. * * @param copyBookContents A string ...
  * `parseSimple` (Impact: 28.9 | O(N^4) | DB: 4)
    * *Intent:* /**
  * `findCycleInAMap` (Impact: 25.4 | O(N^3))
    * *Intent:* * * @param enc Encoding of the data file (either ASCII/EBCDIC). The encoding of the copybook is expe...
  * `getRootSegmentAST` (Impact: 24.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 30`, `func_start: 15`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 17`, `import: 1`
* *Defense:* `safety: 3`, `doc: 83`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.278
  * `Choke Point (Betweenness):` 0.003946 | `Ripple Effect (Closeness):` 0.092656
  * `Imports (Out-Degree: 14):` za.co.absa.cobrix.cobol.parser.decoders.FloatingPointFormat, StringTrimmingPolicy, Primitive, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage, scala.annotation.tailrec, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.internal.Logging, za.co.absa.cobrix.cobol.parser.antlr.ANTLRParser...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonBaseVisitor.java` (JAVA) | Magnitude: 39.8 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 13, api: 12, args: 11
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA) | Magnitude: 2904.86 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 3316, func_start: 1071, structural_boundaries: 872, sec_reflection_metaprogramming: 867
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA) | Magnitude: 578.42 | Delta: **0.299 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 459, structural_boundaries: 146, func_start: 142, branch: 105
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` (JAVA) | Magnitude: 194.68 | Delta: **0.485 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 60, doc: 57, api: 56, args: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen17Hierarchical.scala` (SCALA) | Magnitude: 112.1 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 163, immutability_locks: 51, state_mutation: 45, generics: 23
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/VRLRecordReader.scala` (SCALA) | Magnitude: 154.1 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 46, branch: 29, safety: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/ResourceUtils.scala` (SCALA) | Magnitude: 18.26 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` (SCALA) | Magnitude: 15.48 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 6, encapsulation: 5, func_start: 3
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/AstTransformer.scala` (SCALA) | Magnitude: 17.74 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/mock/CustomRecordExtractorMock.scala` (SCALA) | Magnitude: 26.62 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 6, state_mutation: 5, branch: 4
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/mocks/FixedRecordExtractorNoIndex.scala` (SCALA) | Magnitude: 24.96 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 9, structural_boundaries: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BCDNumberDecoders.scala` (SCALA) | Magnitude: 245.46 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, branch: 47, state_mutation: 36, structural_boundaries: 12
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` (SCALA) | Magnitude: 203.92 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 46, branch: 42, closures: 28
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/UsingUtils.scala` (SCALA) | Magnitude: 234.92 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, branch: 21, args: 17, closures: 17
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/ParameterParsingUtils.scala` (SCALA) | Magnitude: 50.46 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, branch: 13, closures: 9, structural_boundaries: 5
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` (SCALA) | Magnitude: 98.94 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 131, branch: 50, doc: 36, closures: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` (SCALA) | Magnitude: 29.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: explicit_casts: 513, indent_spaces: 464, safety: 329, test: 271
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/LocationBalancer.scala` (SCALA) | Magnitude: 33.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 51, closures: 16, generics: 15, comprehensions: 11
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/FixedRecordLengthRawRecordExtractor.scala` (SCALA) | Magnitude: 27.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 8, branch: 5, safety: 5
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA) | Magnitude: 709.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 325, branch: 103, state_mutation: 90, immutability_locks: 39
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/mocks/CustomRecordExtractorWithFileHeaderMock.scala` (SCALA) | Magnitude: 22.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 5, branch: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/spark-cobol-app/src/main/scala/com/example/spark/cobol/app/SparkCobolApp.scala` (SCALA) | Magnitude: 7.6 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, bitwise_ops: 15, structural_boundaries: 6, immutability_locks: 6
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/apps/CobolSparkExample3.scala` (SCALA) | Magnitude: 7.62 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, bitwise_ops: 14, immutability_locks: 7, structural_boundaries: 6
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/apps/CobolSparkExample2.scala` (SCALA) | Magnitude: 7.58 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, bitwise_ops: 14, immutability_locks: 7, structural_boundaries: 6
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/processor/impl/CobolProcessorBaseSuite.scala` (SCALA) | Magnitude: 23.84 | Delta: **0.352 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, safety: 11, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/headerparsers/RecordHeaderParser.scala` (SCALA) | Magnitude: 4.08 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, api: 2, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen7Fillers.scala` (SCALA) | Magnitude: 30.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, immutability_locks: 13, structural_boundaries: 9, branch: 7
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/extract/BinaryExtractorSpec.scala` (SCALA) | Magnitude: 42.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 148, explicit_casts: 140, immutability_locks: 56, safety: 35
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderBdwSuite.scala` (SCALA) | Magnitude: 17.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 117, generics: 46, safety: 40, test: 40
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/FileUtils.scala` (SCALA) | Magnitude: 9.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 11, indent_spaces: 10, structural_boundaries: 9, closures: 4
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/BinaryPropertiesAdder.scala` (SCALA) | Magnitude: 210.32 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, branch: 25, immutability_locks: 18, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test6TypeVarietySpec.scala` (SCALA) | Magnitude: 15.98 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 39, immutability_locks: 17, structural_boundaries: 11, branch: 8
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/generate_classes.sh` (SHELL) | Magnitude: 11.98 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 6, io: 5, reflection_metaprogramming: 4, branch: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` -> Churn: **63.37%** | Cog Load: 50.9047% | Debt: 97.1601%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 1114.7
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Ruslan Iushchenko** (93.8% isolated ownership) | Magnitude: 1035.34
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 924.42
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 623.86
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 615.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **Severity: 0.08** (Bridge: 0.0039 * Flux: 20.3379%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/processor/CobolProcessor.scala` -> **Severity: 0.07** (Bridge: 0.0017 * Flux: 40.0859%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/RawRecordContext.scala` -> **Severity: 0.039** (Bridge: 0.001 * Flux: 38.2635%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/VarOccursRecordExtractor.scala` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 99.4449%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 91.4695%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 11.59** (Embedded: 0.1449 * Error Risk: 80.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` -> **Severity: 5.484** (Embedded: 0.0686 * Error Risk: 80.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/StringUtils.scala` -> **Severity: 4.514** (Embedded: 0.0564 * Error Risk: 80.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Severity: 3.684** (Embedded: 0.0685 * Error Risk: 53.8095%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/DecoderSelector.scala` -> **Severity: 3.127** (Embedded: 0.0691 * Error Risk: 45.2672%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 3757.244** (Blast Radius: 39.312 * Doc Risk: 95.575%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Group.scala` -> **Severity: 1500.359** (Blast Radius: 15.12 * Doc Risk: 99.2301%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **Severity: 1408.5** (Blast Radius: 14.085 * Doc Risk: 100.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 1023.8** (Blast Radius: 10.238 * Doc Risk: 100.0%)
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Severity: 936.4** (Blast Radius: 9.364 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
