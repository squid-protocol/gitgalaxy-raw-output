# ARCHITECTURAL_BRIEF: cobrix
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/cobrix` |
| **Timestamp** | `2026-08-07T03:50:57.438038+00:00` |
| **Scan Duration** | `1.81s` |
| **Git Branch** | `master` |
| **Git Commit** | `7200b77cdebb4244137f88b48e908acfc4ccbee1` |
| **Git Remote** | `https://github.com/AbsaOSS/cobrix.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 500 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `6.234`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 452 | 72.3% |
| file_cluster_16 | 63 | 10.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 15.4 | 7.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 29.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.9 | 0.2 | 0.0 |
| API Exposure | 0.0 | 15.1 | 2.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 97.3 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 44.8 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 85.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.9 | 1.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 84.3 | 5.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.0 | 11.9 | 0.0 |
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

- `pic` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **284.2** | LOC: 184
- `validateSparkCobolOptions` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala`) -> Impact: **245.8** | LOC: 235
  * *Intent:* /** * Parses the list of segment levels and it's corresponding segment ids. * * Example: * For * {{{ * sprak.read * .option("segment_id_level0", "SEGI...
- `extractRecord` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **233.1** | LOC: 165
- `extractHierarchicalRecord` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala`) -> Impact: **225.8** | LOC: 195
- `enterRule` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **129.6** | LOC: 172
- `group` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **129.4** | LOC: 83
- `setState` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **128.4** | LOC: 168
- `decodeEbcdicNumber` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala`) -> Impact: **118.2** | LOC: 62
- `identifier` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **117.9** | LOC: 122
- `specialValues` (@ `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java`) -> Impact: **115.6** | LOC: 121

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr` | 15 | 9069.95 | 14.65% | 39.84% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders` | 9 | 1372.62 | 32.11% | 49.96% |
| `data/test2_data` | 2 | 1000.0 | 0.0% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform` | 10 | 882.88 | 21.48% | 54.46% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record` | 3 | 859.76 | 11.97% | 32.84% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters` | 9 | 816.12 | 9.6% | 0.0% |
| `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw` | 11 | 786.04 | 45.06% | 18.18% |
| `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils` | 8 | 762.12 | 13.22% | 22.11% |
| `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration` | 45 | 748.24 | 8.9% | 0.0% |
| `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators` | 15 | 701.64 | 26.94% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage1364.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage1388.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage300.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/lexer/Token.scala` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextFullRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/TextRecordExtractor.scala` -> **100.0%** Exposure
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/AutoCloseableSpy.scala` -> **100.0%** Exposure
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` -> **0** Orphaned Functions | **606** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` -> **6** Orphaned Functions | **65** Duplicates
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` -> **55** Orphaned Functions | **0** Duplicates
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2278` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA) -> Cumulative Risk: **627.97**
- **Archetype:** `file_cluster_0` (Distance: 13.109 IQR)
- **Magnitude:** 6807.66 | **LOC:** 3481 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.4998%), State Flux (97.8668%)
- **Heaviest Functions:** `pic` (Impact: 284.2), `enterRule` (Impact: 129.6), `group` (Impact: 129.4)

### 2. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` (SCALA) -> Cumulative Risk: **612.23**
- **Archetype:** `file_cluster_8` (Distance: 11.461 IQR)
- **Magnitude:** 178.44 | **LOC:** 292 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.708%), Concurrency (97.2679%), Documentation (85.9466%)
- **Heaviest Functions:** `process` (Impact: 49.5), `getRecordRdd` (Impact: 24.3), `load` (Impact: 14.8)

### 3. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA) -> Cumulative Risk: **598.45**
- **Archetype:** `file_cluster_0` (Distance: 11.642 IQR)
- **Magnitude:** 754.92 | **LOC:** 516 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (98.6833%), State Flux (92.5923%)
- **Heaviest Functions:** `value` (Impact: 66.5), `obj` (Impact: 29.6), `arr` (Impact: 29.6)

### 4. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA) -> Cumulative Risk: **594.51**
- **Archetype:** `file_cluster_16` (Distance: 12.884 IQR)
- **Magnitude:** 818.16 | **LOC:** 555 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.5075%), State Flux (91.4695%), Safety Score (81.1438%)
- **Heaviest Functions:** `extractRecord` (Impact: 233.1), `extractHierarchicalRecord` (Impact: 225.8), `applyRecordPostProcessing` (Impact: 53.0)

### 5. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/AutoCloseableSpy.scala` (SCALA) -> Cumulative Risk: **591.74**
- **Archetype:** `file_cluster_8` (Distance: 10.98 IQR)
- **Magnitude:** 19.4 | **LOC:** 41 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9842%)
- **Heaviest Functions:** `dummyAction` (Impact: 5.5), `close` (Impact: 5.5)

### 6. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/streaming/BufferedFSDataInputStream.scala` (SCALA) -> Cumulative Risk: **583.36**
- **Archetype:** `file_cluster_8` (Distance: 11.507 IQR)
- **Magnitude:** 128.42 | **LOC:** 150 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (91.9675%), Verification (80.0%)
- **Heaviest Functions:** `readFully` (Impact: 36.3), `openStream` (Impact: 15.2), `readFullyHelper` (Impact: 14.8)

### 7. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/reader/SparkCobolRowType.scala` (SCALA) -> Cumulative Risk: **553.81**
- **Archetype:** `file_cluster_16` (Distance: 10.809 IQR)
- **Magnitude:** 10.72 | **LOC:** 38 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.999%), State Flux (98.448%), Documentation (96.3949%)
- **Heaviest Functions:** `foreach` (Impact: 4.4)

### 8. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/TwoByteCodePage.scala` (SCALA) -> Cumulative Risk: **550.11**
- **Archetype:** `file_cluster_8` (Distance: 10.505 IQR)
- **Magnitude:** 72.56 | **LOC:** 116 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (89.5472%), State Flux (88.18%), Verification (80.0%)
- **Heaviest Functions:** `convert` (Impact: 30.9), `readDoubleByte` (Impact: 5.9), `readSingleByte` (Impact: 5.8)

### 9. `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/BinaryEncoders.scala` (SCALA) -> Cumulative Risk: **543.98**
- **Archetype:** `file_cluster_8` (Distance: 9.211 IQR)
- **Magnitude:** 66.94 | **LOC:** 72 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (90.7814%), Verification (80.0%), Safety Score (78.1788%)
- **Heaviest Functions:** `encodeBinaryNumber` (Impact: 59.0)

### 10. `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` (SCALA) -> Cumulative Risk: **541.83**
- **Archetype:** `file_cluster_8` (Distance: 12.596 IQR)
- **Magnitude:** 185.9 | **LOC:** 324 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 92.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.1601%), State Flux (91.1717%), Safety Score (67.9545%)
- **Heaviest Functions:** `resolveHeaderTrailerOffsets` (Impact: 55.5), `createRelation` (Impact: 31.9), `buildEitherReader` (Impact: 16.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.109 IQR)
- **Top Global Matches:** file_cluster_0: 13.109, file_cluster_8: 13.252, file_cluster_11: 13.408
- **Magnitude:** 6807.66 | **LOC:** 3481 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.0981%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `pic` (Impact: 284.2)
  * `enterRule` (Impact: 129.6)
  * `group` (Impact: 129.4)
  * `setState` (Impact: 128.4)
  * `identifier` (Impact: 117.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 823`, `structural_boundaries: 872`, `args: 447`, `func_start: 1071`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 544`, `duplicate_logic: 606`
* *Architecture:* `api: 518`, `import: 4`
* *Defense:* `safety: 178`, `doc: 2`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.09
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 0):` org.antlr.v4.runtime.*, java.util.ArrayList, org.antlr.v4.runtime.tree.*, java.util.Iterator, org.antlr.v4.runtime.dfa.DFA, java.util.List, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.misc.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.871 IQR)
- **Top Global Matches:** file_cluster_8: 13.871, file_cluster_15: 13.936, file_cluster_11: 13.943
- **Magnitude:** 869.3 | **LOC:** 880 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.2577%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkBounds` (Impact: 65.9)
  * `visitPrimitive` (Impact: 64.0)
  * `fromNumericZPicRegexDecimalScaled` (Impact: 53.5)
  * `replaceUsage` (Impact: 49.2)
  * `fromNumericSPicRegexDecimalScaled` (Impact: 42.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 58`, `args: 121`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 90`
* *Architecture:* `io: 1`, `api: 65`, `import: 1`
* *Defense:* `safety: 172`, `test: 9`, `immutability_locks: 90`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.09
  * `Choke Point (Betweenness):` 0.000136 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 11):` za.co.absa.cobrix.cobol.parser.ast.Group, Primitive, scala.util.matching.Regex, za.co.absa.cobrix.cobol.parser.position.Left, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage, za.co.absa.cobrix.cobol.parser.exceptions.SyntaxErrorException, java.nio.charset.Charset, za.co.absa.cobrix.cobol.parser.decoders.DecoderSelector...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.884 IQR)
- **Top Global Matches:** file_cluster_16: 12.884, file_cluster_15: 13.006, file_cluster_11: 13.101
- **Magnitude:** 818.16 | **LOC:** 555 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (25.9126%), Tech Debt (98.5075%)
**Top Internal Functions/Classes:**
  * `extractRecord` (Impact: 233.1)
  * `extractHierarchicalRecord` (Impact: 225.8)
  * `applyRecordPostProcessing` (Impact: 53.0)
  * `extractArray` (Impact: 44.1)
  * `extractArray` (Impact: 37.2)
    * *Intent:* /** * This method extracts a record from the specified array of bytes. The copybook for the record n...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 25`, `args: 43`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 73`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 11`, `import: 1`
* *Defense:* `safety: 26`, `doc: 49`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.773
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.015037
  * `Imports (Out-Degree: 7):` za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.reader.policies.SchemaRetentionPolicy, COMP4, scala.collection.mutable.ArrayBuffer, scala.collection.mutable, za.co.absa.cobrix.cobol.parser.encoding.RAW, za.co.absa.cobrix.cobol.utils.StringUtils...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.642 IQR)
- **Top Global Matches:** file_cluster_0: 11.642, file_cluster_8: 11.913, file_cluster_16: 11.998
- **Magnitude:** 754.92 | **LOC:** 516 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.323%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `value` (Impact: 66.5)
  * `obj` (Impact: 29.6)
  * `arr` (Impact: 29.6)
  * `enterRule` (Impact: 29.2)
  * `setState` (Impact: 28.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 146`, `args: 56`, `func_start: 142`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 66`, `duplicate_logic: 65`, `orphaned_logic: 6`
* *Architecture:* `api: 75`, `import: 4`
* *Defense:* `safety: 26`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.antlr.v4.runtime.*, java.util.ArrayList, org.antlr.v4.runtime.tree.*, java.util.Iterator, org.antlr.v4.runtime.dfa.DFA, java.util.List, org.antlr.v4.runtime.atn.*, org.antlr.v4.runtime.misc.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.228 IQR)
- **Top Global Matches:** file_cluster_8: 12.228, file_cluster_17: 12.462, file_cluster_15: 12.523
- **Magnitude:** 669.54 | **LOC:** 1069 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 93.8%
- **Risk Profile:** Cognitive Load (25.0698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validateSparkCobolOptions` (Impact: 245.8)
    * *Intent:* /** * Parses the list of segment levels and it's corresponding segment ids. * * Example: * For * {{{...
  * `parseVariableLengthParameters` (Impact: 39.5)
  * `getRecordLengthMappings` (Impact: 33.2)
  * `getSegmentRedefineParents` (Impact: 31.6)
    * *Intent:* /** * Parses parameters for reading multisegment mainframe files *
  * `getIsEbcdic` (Impact: 27.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 65`, `args: 52`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 80`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 49`, `doc: 29`, `immutability_locks: 169`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.19
  * `Choke Point (Betweenness):` 0.000657 | `Ripple Effect (Closeness):` 0.021311
  * `Imports (Out-Degree: 8):` scala.collection.mutable.ListBuffer, za.co.absa.cobrix.cobol.reader.policies.SchemaRetentionPolicy, za.co.absa.cobrix.cobol.parser.antlr.ParserJson, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat, za.co.absa.cobrix.cobol.parser.recordformats.RecordFormat._, za.co.absa.cobrix.cobol.parser.policies.StringTrimmingPolicy.StringTrimmingPolicy, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.policies.DebugFieldsPolicy.DebugFieldsPolicy...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.227 IQR)
- **Top Global Matches:** file_cluster_15: 12.227, file_cluster_0: 12.403, file_cluster_11: 12.432
- **Magnitude:** 626.72 | **LOC:** 599 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.5852%), Tech Debt (76.901%)
**Top Internal Functions/Classes:**
  * `copyMetadata` (Impact: 67.1)
  * `flattenSchema` (Impact: 59.6)
  * `splitFieldPath` (Impact: 34.1)
  * `getField` (Impact: 25.8)
  * `processArray` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 38`, `args: 108`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 45`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 39`, `import: 1`
* *Defense:* `safety: 17`, `doc: 35`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.364
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.058894
  * `Imports (Out-Degree: 1):` scala.collection.mutable.ListBuffer, org.apache.spark.sql.expressions.UserDefinedFunction, Row, org.apache.spark.sql.Column, za.co.absa.cobrix.spark.cobol.parameters.MetadataFields.MAX_ELEMENTS, za.co.absa.cobrix.spark.cobol.utils.impl.HofsWrapper.transform, org.apache.spark.sql.functions._, DataFrame...
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `data/test15_data/a/example.bin` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.924 IQR)
- **Top Global Matches:** file_cluster_15: 12.924, file_cluster_0: 13.024, file_cluster_16: 13.057
- **Magnitude:** 464.86 | **LOC:** 429 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.9052%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `decodeEbcdicNumber` (Impact: 118.2)
  * `decodeAsciiNumber` (Impact: 71.4)
  * `decodeAsciiString` (Impact: 33.2)
    * *Intent:* /** * A decoder for any EBCDIC string fields (alphabetical or any char) * * @param bytes A byte arra...
  * `decodeUtf16String` (Impact: 27.8)
    * *Intent:* /** * A decoder for any ASCII string fields (alphabetical or any char) * * @param bytes A byte array...
  * `decodeEbcdicString` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 26`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 81`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `doc: 93`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 2):` java.nio.charset.StandardCharsets, scala.util.control.NonFatal, za.co.absa.cobrix.cobol.parser.encoding.codepage.CodePage, Constants._, StringTools._, za.co.absa.cobrix.cobol.parser.common.Constants
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.802 IQR)
- **Top Global Matches:** file_cluster_16: 11.802, file_cluster_15: 11.925, file_cluster_8: 11.942
- **Magnitude:** 436.4 | **LOC:** 480 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.3927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getFieldByName` (Impact: 64.0)
  * `merge` (Impact: 55.1)
  * `setPrimitiveField` (Impact: 42.9)
  * `generateRecordLayoutPositions` (Impact: 34.3)
  * `dropFillers` (Impact: 27.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 44`, `args: 58`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `safety: 25`, `doc: 33`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.842
  * `Choke Point (Betweenness):` 0.001153 | `Ripple Effect (Closeness):` 0.068462
  * `Imports (Out-Degree: 5):` za.co.absa.cobrix.cobol.parser.CopybookParser.CopybookAST, za.co.absa.cobrix.cobol.parser.ast.Group, za.co.absa.cobrix.cobol.internal.Logging, scala.collection.mutable.ArrayBuffer, java.util.concurrent.ConcurrentHashMap, Primitive, scala.collection.mutable, Copybook._...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.556 IQR)
- **Top Global Matches:** file_cluster_16: 12.556, file_cluster_8: 12.565, file_cluster_15: 12.671
- **Magnitude:** 428.94 | **LOC:** 480 | **CtrlFlow:** 92.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `putEncodedNumStrToArray` (Impact: 71.5)
  * `encodeUncompressed` (Impact: 42.8)
  * `encodeBcd` (Impact: 20.5)
  * `encodeBinSigned` (Impact: 18.6)
  * `putDecimalToArray` (Impact: 15.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 9`, `args: 35`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `duplicate_logic: 4`, `orphaned_logic: 13`
* *Architecture:* `api: 22`, `import: 1`
* *Defense:* `safety: 8`, `doc: 23`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` scodec.Attempt.Successful, za.co.absa.cobrix.cobol.parser.common.Constants, scala.util.Random, za.co.absa.cobrix.cobol.parser.decoders.BinaryUtils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/schema/CobolSchema.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.343 IQR)
- **Top Global Matches:** file_cluster_8: 10.343, file_cluster_15: 10.65, file_cluster_16: 10.693
- **Magnitude:** 285.04 | **LOC:** 444 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (20.3576%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parsePrimitive` (Impact: 78.5)
  * `createSparkSchema` (Impact: 39.8)
  * `parseGroup` (Impact: 22.5)
  * `builder` (Impact: 14.6)
  * `addExtendedPrimitiveMetadata` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 33`, `args: 56`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`
* *Architecture:* `api: 30`, `import: 2`
* *Defense:* `safety: 4`, `doc: 15`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018029
  * `Imports (Out-Degree: 11):` MIN_ELEMENTS, za.co.absa.cobrix.cobol.parser.ast._, MAX_LENGTH, COMP1, Parameters, COMP2, za.co.absa.cobrix.cobol.parser.encoding.RAW, scala.collection.mutable...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/DisplayEncoders.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.396 IQR)
- **Top Global Matches:** file_cluster_8: 10.396, file_cluster_16: 10.782, file_cluster_13: 10.895
- **Magnitude:** 252.46 | **LOC:** 213 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.228%), Tech Debt (40.7136%)
**Top Internal Functions/Classes:**
  * `encodeDisplayNumberSignSeparate` (Impact: 67.9)
    * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "Lice...
  * `encodeDisplayNumberSignOverpunched` (Impact: 62.1)
  * `setPaddedEbcdicNumberWithSignSeparate` (Impact: 50.7)
  * `setPaddedEbcdicNumberWithSignOverpunched` (Impact: 37.7)
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

### `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/utils/UsingUtilsSuite.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.497 IQR)
- **Top Global Matches:** file_cluster_8: 14.497, file_cluster_17: 14.536, file_cluster_11: 14.593
- **Magnitude:** 246.5 | **LOC:** 513 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.6605%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 57`, `args: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 223`
* *Architecture:* `import: 1`
* *Defense:* `safety: 102`, `test: 102`, `immutability_locks: 20`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.scalatest.wordspec.AnyWordSpec, UsingUtils.Implicits._
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen6TypeVariety.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.839 IQR)
- **Top Global Matches:** file_cluster_8: 11.839, file_cluster_7: 12.385, file_cluster_13: 12.444
- **Magnitude:** 227.26 | **LOC:** 575 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.6035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 10.5)
  * `getVeryBigNumber` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 207`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.example.spark.cobol.examples.parser.generators.utils.GeneratorTools._, FileOutputStream, java.io.BufferedOutputStream, scala.util.Random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/writer/NestedRecordCombiner.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.149 IQR)
- **Top Global Matches:** file_cluster_8: 11.149, file_cluster_15: 11.214, file_cluster_7: 11.352
- **Magnitude:** 217.54 | **LOC:** 476 | **CtrlFlow:** 71.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.3993%), Tech Debt (35.7648%)
**Top Internal Functions/Classes:**
  * `writeToBytes` (Impact: 71.5)
  * `buildGroupNode` (Impact: 46.2)
    * *Intent:* /** * Constructs a writer AST (Abstract Syntax Tree) from a copybook and Spark schema for serializat...
  * `buildPrimitiveNode` (Impact: 44.3)
  * `combine` (Impact: 31.6)
  * `addDependee` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 29`, `args: 31`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 45`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Integral, za.co.absa.cobrix.cobol.parser.ast.Group, org.apache.spark.sql.DataFrame, org.apache.spark.rdd.RDD, za.co.absa.cobrix.cobol.parser.Copybook, Row, za.co.absa.cobrix.cobol.parser.ast.datatype.Decimal, StructType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.94 IQR)
- **Top Global Matches:** file_cluster_0: 12.94, file_cluster_8: 13.425, file_cluster_7: 13.461
- **Magnitude:** 194.68 | **LOC:** 416 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visitMain` (Impact: 2.5)
    * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "Lice...
  * `visitLiteral` (Impact: 2.5)
    * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "Lice...
  * `visitNumericLiteral` (Impact: 2.5)
    * *Intent:* /* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "Lice...
  * `visitIntegerLiteral` (Impact: 2.5)
    * *Intent:* * Copyright 2018 ABSA Group Limited * * Licensed under the Apache License, Version 2.0 (the "License...
  * `visitBooleanLiteral` (Impact: 2.5)
    * *Intent:* * Licensed under the Apache License, Version 2.0 (the "License"); * you may not use this file except...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 60`, `args: 55`, `func_start: 55`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 55`
* *Architecture:* `api: 56`, `import: 1`
* *Defense:* `doc: 57`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` org.antlr.v4.runtime.tree.AbstractParseTreeVisitor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryUtils.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_15` (Drift: 12.804 IQR)
- **Top Global Matches:** file_cluster_15: 12.804, file_cluster_8: 12.897, file_cluster_16: 13.146
- **Magnitude:** 186.44 | **LOC:** 249 | **CtrlFlow:** 87.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.8656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBytesCount` (Impact: 84.7)
  * `decodeBinaryNumber` (Impact: 57.9)
  * `decodeString` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 12`, `args: 39`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 8`, `doc: 15`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.903
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.069979
  * `Imports (Out-Degree: 2):` Encoding, za.co.absa.cobrix.cobol.parser.ast.datatype._, Constants._, za.co.absa.cobrix.cobol.parser.encoding.EBCDIC, za.co.absa.cobrix.cobol.parser.common.Constants
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.596 IQR)
- **Top Global Matches:** file_cluster_8: 12.596, file_cluster_15: 12.645, file_cluster_17: 12.709
- **Magnitude:** 185.9 | **LOC:** 324 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 92.3%
- **Risk Profile:** Cognitive Load (51.1714%), Tech Debt (97.1601%)
**Top Internal Functions/Classes:**
  * `resolveHeaderTrailerOffsets` (Impact: 55.5)
    * *Intent:* /**
  * `createRelation` (Impact: 31.9)
  * `buildEitherReader` (Impact: 16.8)
  * `createRelation` (Impact: 5.1)
    * *Intent:* /** * This class represents a Cobol data source. */
  * `schema` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 45`, `args: 28`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 13`, `doc: 9`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001603
  * `Imports (Out-Degree: 13):` za.co.absa.cobrix.cobol.parser.ast.Group, org.apache.spark.sql.DataFrame, za.co.absa.cobrix.cobol.reader.parameters.CobolParameters, org.slf4j.Logger, SparkSession, org.apache.spark.sql.sources._, org.apache.spark.sql.types.StructType, za.co.absa.cobrix.spark.cobol.writer.RawBinaryOutputFormat...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/VarLenNestedReader.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.245 IQR)
- **Top Global Matches:** file_cluster_8: 11.245, file_cluster_16: 11.617, file_cluster_7: 11.713
- **Magnitude:** 181.7 | **LOC:** 292 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.7041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `recordExtractor` (Impact: 57.8)
    * *Intent:* /** * The Cobol data reader for variable length records that gets input binary data as a stream and ...
  * `generateIndex` (Impact: 47.8)
  * `getRootSegmentId` (Impact: 12.7)
  * `getRecordIterator` (Impact: 11.4)
  * `getRecordHeaderParser` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 33`, `args: 25`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 37`, `doc: 8`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.323
  * `Choke Point (Betweenness):` 0.000674 | `Ripple Effect (Closeness):` 0.005235
  * `Imports (Out-Degree: 13):` za.co.absa.cobrix.cobol.reader.stream.SimpleStream, za.co.absa.cobrix.cobol.parser.headerparsers.RecordHeaderParser, za.co.absa.cobrix.cobol.reader.parameters.ReaderParameters, za.co.absa.cobrix.cobol.reader.extractors.record.RecordHandler, za.co.absa.cobrix.cobol.reader.extractors.raw._, za.co.absa.cobrix.cobol.reader.iterator.VarLenHierarchicalIterator, scala.reflect.ClassTag, za.co.absa.cobrix.cobol.reader.schema.CobolSchema...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` (SCALA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.461 IQR)
- **Top Global Matches:** file_cluster_8: 11.461, file_cluster_16: 11.463, file_cluster_4: 11.747
- **Magnitude:** 178.44 | **LOC:** 292 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.0544%), Tech Debt (99.708%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 49.5)
  * `getRecordRdd` (Impact: 24.3)
  * `load` (Impact: 14.8)
  * `processListOfFiles` (Impact: 10.1)
  * `save` (Impact: 7.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 51`, `args: 26`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 15`, `import: 1`
* *Defense:* `safety: 14`, `doc: 11`, `immutability_locks: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.005
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` za.co.absa.cobrix.cobol.reader.common.Constants, za.co.absa.cobrix.spark.cobol.utils.FileUtils, scala.concurrent.Await, za.co.absa.cobrix.spark.cobol.source.parameters.LocalityParameters, org.apache.spark.rdd.RDD, za.co.absa.cobrix.cobol.reader.parameters.CobolParameters, org.apache.spark.sql.SparkSession, java.util.concurrent.ExecutorService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonBaseVisitor.java` (JAVA) | Magnitude: 39.8 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 13, api: 12, args: 11
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParser.java` (JAVA) | Magnitude: 6807.66 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 3316, func_start: 1071, structural_boundaries: 872, sec_reflection_metaprogramming: 867
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/jsonParser.java` (JAVA) | Magnitude: 754.92 | Delta: **0.271 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 459, structural_boundaries: 146, func_start: 142, branch: 105
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/copybookParserBaseVisitor.java` (JAVA) | Magnitude: 194.68 | Delta: **0.485 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 60, doc: 57, api: 56, args: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen17Hierarchical.scala` (SCALA) | Magnitude: 112.1 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 163, immutability_locks: 51, state_mutation: 45, generics: 23
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/iterator/VRLRecordReader.scala` (SCALA) | Magnitude: 113.8 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 46, branch: 29, safety: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/ResourceUtils.scala` (SCALA) | Magnitude: 18.26 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` (SCALA) | Magnitude: 15.48 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 6, encapsulation: 5, func_start: 3
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/asttransform/AstTransformer.scala` (SCALA) | Magnitude: 17.74 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/mock/CustomRecordExtractorMock.scala` (SCALA) | Magnitude: 17.92 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 6, state_mutation: 5, branch: 4
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/mocks/FixedRecordExtractorNoIndex.scala` (SCALA) | Magnitude: 24.96 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 9, structural_boundaries: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/BCDNumberDecoders.scala` (SCALA) | Magnitude: 151.16 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, branch: 47, state_mutation: 36, structural_boundaries: 12
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/expression/parser/Parser.scala` (SCALA) | Magnitude: 129.42 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 46, branch: 42, closures: 28
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/UsingUtils.scala` (SCALA) | Magnitude: 88.82 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, branch: 21, args: 17, closures: 17
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/ParameterParsingUtils.scala` (SCALA) | Magnitude: 35.46 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, branch: 13, closures: 9, structural_boundaries: 5
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` (SCALA) | Magnitude: 79.64 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 131, branch: 50, doc: 36, args: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/decoders/BinaryDecoderSpec.scala` (SCALA) | Magnitude: 29.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: explicit_casts: 513, indent_spaces: 464, safety: 329, test: 271
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/index/LocationBalancer.scala` (SCALA) | Magnitude: 25.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 51, closures: 16, generics: 15, comprehensions: 11
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/raw/FixedRecordLengthRawRecordExtractor.scala` (SCALA) | Magnitude: 25.14 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 8, branch: 5, safety: 5
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/utils/GeneratorTools.scala` (SCALA) | Magnitude: 428.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 325, branch: 103, state_mutation: 90, immutability_locks: 39
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/mocks/CustomRecordExtractorWithFileHeaderMock.scala` (SCALA) | Magnitude: 13.82 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 5, branch: 4, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/spark-cobol-app/src/main/scala/com/example/spark/cobol/app/SparkCobolApp.scala` (SCALA) | Magnitude: 6.6 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, bitwise_ops: 15, structural_boundaries: 6, immutability_locks: 6
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/apps/CobolSparkExample3.scala` (SCALA) | Magnitude: 6.62 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, bitwise_ops: 14, immutability_locks: 7, structural_boundaries: 6
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/apps/CobolSparkExample2.scala` (SCALA) | Magnitude: 6.58 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, bitwise_ops: 14, immutability_locks: 7, structural_boundaries: 6
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/processor/impl/CobolProcessorBaseSuite.scala` (SCALA) | Magnitude: 23.84 | Delta: **0.352 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, safety: 11, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/headerparsers/RecordHeaderParser.scala` (SCALA) | Magnitude: 4.08 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, api: 2, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/SparkCobolProcessor.scala` (SCALA) | Magnitude: 178.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 51, immutability_locks: 38, args: 26
- `examples/examples-collection/src/main/scala/com/example/spark/cobol/examples/parser/generators/TestDataGen7Fillers.scala` (SCALA) | Magnitude: 22.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, immutability_locks: 13, structural_boundaries: 9, branch: 7
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/parser/extract/BinaryExtractorSpec.scala` (SCALA) | Magnitude: 18.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 148, explicit_casts: 140, immutability_locks: 56, safety: 35
- `cobol-parser/src/test/scala/za/co/absa/cobrix/cobol/reader/recordheader/RecordHeaderDecoderBdwSuite.scala` (SCALA) | Magnitude: 17.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 117, generics: 46, safety: 40, test: 40
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/processor/CobolProcessor.scala` (SCALA) | Magnitude: 122.62 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 32, branch: 18, api: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `spark-cobol/src/test/scala/za/co/absa/cobrix/spark/cobol/source/integration/Test6TypeVarietySpec.scala` (SCALA) | Magnitude: 15.98 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 39, immutability_locks: 17, structural_boundaries: 11, branch: 8
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/generate_classes.sh` (SHELL) | Magnitude: 11.98 | Delta: **0.169 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 6, io: 5, reflection_metaprogramming: 4, branch: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/source/DefaultSource.scala` -> Churn: **63.37%** | Cog Load: 51.1714% | Debt: 97.1601%
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/extractors/record/RecordExtractors.scala` -> Churn: **56.89%** | Cog Load: 25.9126% | Debt: 98.5075%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/antlr/ParserVisitor.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 869.3
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/reader/parameters/CobolParametersParser.scala` -> **Ruslan Iushchenko** (93.8% isolated ownership) | Magnitude: 669.54
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 626.72
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/decoders/StringDecoders.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 464.86
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/Copybook.scala` -> **Ruslan Iushchenko** (100.0% isolated ownership) | Magnitude: 436.4

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

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 13.408** (Embedded: 0.1449 * Error Risk: 92.5532%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/EncoderSelector.scala` -> **Severity: 5.484** (Embedded: 0.0686 * Error Risk: 80.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/encoding/codepage/CodePage.scala` -> **Severity: 5.217** (Embedded: 0.079 * Error Risk: 66.0659%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/utils/StringUtils.scala` -> **Severity: 5.106** (Embedded: 0.0564 * Error Risk: 90.486%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/CopybookParser.scala` -> **Severity: 5.1** (Embedded: 0.0927 * Error Risk: 55.0432%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/internal/Logging.scala` -> **Severity: 2420.389** (Blast Radius: 39.312 * Doc Risk: 61.5687%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Group.scala` -> **Severity: 1445.398** (Blast Radius: 15.12 * Doc Risk: 95.5951%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/datatype/Usage.scala` -> **Severity: 1408.5** (Blast Radius: 14.085 * Doc Risk: 100.0%)
- `cobol-parser/src/main/scala/za/co/absa/cobrix/cobol/parser/ast/Primitive.scala` -> **Severity: 1023.8** (Blast Radius: 10.238 * Doc Risk: 100.0%)
- `spark-cobol/src/main/scala/za/co/absa/cobrix/spark/cobol/utils/SparkUtils.scala` -> **Severity: 936.4** (Blast Radius: 9.364 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
